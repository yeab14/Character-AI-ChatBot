import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import {
  Box,
  Button,
  FormControl,
  FormControlLabel,
  FormLabel,
  Radio,
  RadioGroup,
  TextField,
  Typography,
} from "@material-ui/core";
import { useTranslation } from "react-i18next";
import { Link, useNavigate } from "react-router-dom";
import LoadingButton from "@material-ui/lab/LoadingButton";
import BoxedLayout from "../../core/components/BoxedLayout";
import { useSnackbar } from "../../core/contexts/SnackbarProvider";
import useRegister from "../../auth/hooks/useRegister"; // Adjusted import path
import { UserInfo } from "../types/userInfo";

const genders = [
  { label: "auth.register.form.gender.options.f", value: "F" },
  { label: "auth.register.form.gender.options.m", value: "M" },
  { label: "auth.register.form.gender.options.n", value: "NC" },
];

const Register = () => {
  const navigate = useNavigate();
  const snackbar = useSnackbar();
  const { t } = useTranslation();

  const { isRegistering, register } = useRegister();

  const formik = useFormik({
    initialValues: {
      email: "",
      firstName: "",
      gender: "F",
      lastName: "",
      password: "", // Add password field
    },
    validationSchema: Yup.object({
      email: Yup.string()
        .email("Invalid email address")
        .required(t("common.validations.required")),
      firstName: Yup.string()
        .max(20, t("common.validations.max", { size: 20 }))
        .required(t("common.validations.required")),
      lastName: Yup.string()
        .max(30, t("common.validations.max", { size: 30 }))
        .required(t("common.validations.required")),
      password: Yup.string()
        .min(8, t("common.validations.min", { size: 8 }))
        .required(t("common.validations.required")),
    }),
    onSubmit: (values) => handleRegister(values),
  });

  const handleRegister = async (values: Partial<UserInfo>) => {
    register(values as UserInfo)
      .then(() => {
        snackbar.success(t("auth.register.notifications.success"));
        navigate(`/login`);
      })
      .catch(() => {
        snackbar.error(t("common.errors.unexpected.subTitle"));
      });
  };

  return (
    <BoxedLayout>
      <Typography component="h1" variant="h5">
        {t("auth.register.title")}
      </Typography>
      <Box
        component="form"
        marginTop={3}
        noValidate
        onSubmit={formik.handleSubmit}
      >
        <TextField
          margin="normal"
          required
          fullWidth
          id="lastName"
          label={t("auth.register.form.lastName.label")}
          name="lastName"
          autoComplete="family-name"
          autoFocus
          disabled={isRegistering}
          value={formik.values.lastName}
          onChange={formik.handleChange}
          error={formik.touched.lastName && Boolean(formik.errors.lastName)}
          helperText={formik.touched.lastName && formik.errors.lastName}
        />
        <TextField
          margin="normal"
          required
          fullWidth
          id="firstName"
          label={t("auth.register.form.firstName.label")}
          name="firstName"
          autoComplete="given-name"
          disabled={isRegistering}
          value={formik.values.firstName}
          onChange={formik.handleChange}
          error={formik.touched.firstName && Boolean(formik.errors.firstName)}
          helperText={formik.touched.firstName && formik.errors.firstName}
        />
        <TextField
          margin="normal"
          required
          fullWidth
          id="password"
          label={t("auth.register.form.password.label")}
          name="password"
          type="password"
          autoComplete="new-password"
          disabled={isRegistering}
          value={formik.values.password}
          onChange={formik.handleChange}
          error={formik.touched.password && Boolean(formik.errors.password)}
          helperText={formik.touched.password && formik.errors.password}
        />
        <FormControl component="fieldset" margin="normal">
          <FormLabel component="legend">
            {t("auth.register.form.gender.label")}
          </FormLabel>
          <RadioGroup
            row
            aria-label="gender"
            name="gender"
            value={formik.values.gender}
            onChange={formik.handleChange}
          >
            {genders.map((gender) => (
              <FormControlLabel
                control={<Radio />}
                key={gender.value}
                disabled={isRegistering}
                label={t(gender.label)}
                value={gender.value}
              />
            ))}
          </RadioGroup>
        </FormControl>
        <TextField
          margin="normal"
          required
          fullWidth
          id="email"
          label={t("auth.register.form.email.label")}
          name="email"
          autoComplete="email"
          disabled={isRegistering}
          value={formik.values.email}
          onChange={formik.handleChange}
          error={formik.touched.email && Boolean(formik.errors.email)}
          helperText={formik.touched.email && formik.errors.email}
        />
        <LoadingButton
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          disabled={isRegistering}
          loading={isRegistering}
          sx={{ mt: 2 }}
        >
          {t("auth.register.submit")}
        </LoadingButton>
        <Button
          component={Link}
          to={`/login`}
          color="primary"
          fullWidth
          sx={{ mt: 2 }}
        >
          {t("auth.register.back")}
        </Button>
      </Box>
    </BoxedLayout>
  );
};

export default Register;

