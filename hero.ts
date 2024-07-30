import React from "react";
import { Avatar, Box, Button, Container, List, ListItem, ListItemAvatar, ListItemText, Stack, Typography } from "@material-ui/core";
import { useTheme } from "@material-ui/core/styles";
import StarIcon from "@material-ui/icons/Star";
import { useTranslation } from "react-i18next";
import { Link as RouterLink } from "react-router-dom";
import { useAuth } from "../../auth/contexts/AuthProvider";
import LandingLayout from "../components/LandingLayout";

// HeroSection Component
const HeroSection: React.FC = () => {
  const { userInfo } = useAuth();
  const theme = useTheme();
  const { t } = useTranslation();

  return (
    <Box sx={{ py: 6 }}>
      <Container maxWidth="sm">
        <Typography variant="h1" align="center" color="text.primary" marginBottom={4}>
          {t("landing.title")}
        </Typography>
        <Stack sx={{ pt: 3 }} direction="row" spacing={2} justifyContent="center">
          <Button
            component="a"
            href={process.env.REACT_APP_SOURCE_LINK}
            rel="noopener noreferrer"
            target="_blank"
            variant="outlined"
          >
            {t("landing.cta.secondary")}
          </Button>
          {userInfo ? (
            <Button
              component={RouterLink}
              to={`/${process.env.PUBLIC_URL}/admin`}
              variant="contained"
            >
              {t("landing.cta.mainAuth", { name: userInfo.firstName })}
            </Button>
          ) : (
            <Button
              component={RouterLink}
              to={`/${process.env.PUBLIC_URL}/login`}
              variant="contained"
            >
              {t("landing.cta.main")}
            </Button>
          )}
        </Stack>
      </Container>
    </Box>
  );
};

// ImageSection Component
const ImageSection: React.FC = () => {
  const theme = useTheme();

  return (
    <Container sx={{ py: 6 }} maxWidth="md">
      <img
        alt="Application demo"
        src={`img/template-${theme.palette.mode}.png`}
        style={{
          borderRadius: 24,
          borderStyle: "solid",
          borderWidth: 4,
          borderColor: theme.palette.background.default,
          width: "100%",
        }}
      />
    </Container>
  );
};

// FeaturesSection Component
const FeaturesSection: React.FC = () => {
  const { t } = useTranslation();
  const features = [
    { name: "Bootstraped with Create React App" },
    { name: "Components & Themes built on top of Material-UI" },
    { name: "Data Fetching with React Query" },
    { name: "Written in TypeScript" },
    { name: "Real-world examples" },
    { name: "Best Practices" },
    { name: "MIT License" },
  ];

  return (
    <Container sx={{ py: 8 }} maxWidth="md">
      <Stack alignItems="center">
        <Typography variant="h2" align="center" color="text.primary" gutterBottom>
          {t("landing.features.title")}
        </Typography>
        <List sx={{ pt: 3 }}>
          {features.map((feature, index) => (
            <ListItem key={index}>
              <ListItemAvatar>
                <Avatar>
                  <StarIcon />
                </Avatar>
              </ListItemAvatar>
              <ListItemText primary={feature.name} />
            </ListItem>
          ))}
        </List>
        <Button
          component="a"
          href={process.env.REACT_APP_SOURCE_LINK}
          rel="noopener noreferrer"
          target="_blank"
          sx={{ mt: 3 }}
          variant="outlined"
        >
          {t("landing.features.more")}
        </Button>
      </Stack>
    </Container>
  );
};

// Main Landing Component
const Landing: React.FC = () => {
  return (
    <LandingLayout>
      <main>
        <HeroSection />
        <ImageSection />
        <FeaturesSection />
      </main>
    </LandingLayout>
  );
};

export default Landing;

  );
};

export default Landing;
