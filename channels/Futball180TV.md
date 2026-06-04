<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/Q9ju-4Oqm_lw00WxzMmgyUZk5Jeo7lqM-ZDBghPgnkcQWI0S48yKFphb9NmxOFi88r2_UaEqKM89SrnTAi7_L5ZIqO5WAXulhtSFVz5wbngaf3myJMBLnXeYRQWGDnYk98crWjMW_aCUeUc94BkyQsqfCMZbdsm34RsaKsckLMqk7Dk8VjOWkb0k73uxK-41Z93f9YtyyfKeDvICh7BOJyawxI8GFNyuoJcneqpCK03vtovT6JbQm1GrpYjPARbPskhMv9gu_zRSL0j1Rz_tLR379R6RxKwbmqyK3tjrjr6LHyKCe0a8XriGEIaiL1VMakWOSi4HRvzJiI24b4pd9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 167K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 13:55:57</div>
<hr>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چالش جدید هوادار رئال‌ با موزیک ترند شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/Futball180TV/90889" target="_blank">📅 13:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C31pbG1yvUtARG6ADVJ23Fr6G5IWEMPrvmzS_dgNaNZM-fk4rpxPMmivhcMrYs2_1ItNsH_uFJLzUanaDb_Vzo_Dfa8rOy9tOeGz-TvXXI8_R8YAiIpeXe1AgCypypw72ZihIvA0Wo6XqZutywuqsnyM_Z1qlSSv7DamfGCbqUp8_WLYAYKUuiAHHl_z-HcGJ2UeOdJYVA_3pE51OEg75UQuKzKKz9vNH2PlTkvZAK13YIlodX1Xary1Qt-TbbGPvU23APJUACfYxrTY4zSTMnb5sQ_ZJsw09sK8DCk1SBfa2S-MsOnF55kIYxJKStvG6EI2GtP8MOjsUX7havEwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📰
#فووووووری
از اسکای اسپورت:
🇪🇸
بارسلونا نخستین تماس‌های خود را برای جذب آندره‌آ کامبیاسو آغاز کرده است.  این مدافع چپ ایتالیایی در فهرست گزینه‌های باشگاه قرار دارد و مذاکرات اولیه برای بررسی شرایط این انتقال انجام شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/90888" target="_blank">📅 13:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام نیکولا شیرا خبرنگار سرشناس ایتالیایی، قرارداد ژائو کانسلو با بارسا دائمی و تا 2028 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/90887" target="_blank">📅 13:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvCJQV0Eu5jhrTINrGJ8jR6oYulJ1W5hLSUgZA8Uo8szKt1N7l8AAIrn0AJA6XffMZTWIYhdpAP4nnuXv2lzADbBeyfDWsOIllcOPwtxhqYqZg7eXxh_kEzsBY1UiLDJtqVhFewICysGTm0fMSQ2YX8hOI1PCiXGV_AcpQjGQwowF34iNuzDstuFcaki8tzYODAEuBldQddvBbMybbS0eCSu2V2DJQNB4iiyomx9as-fABy57LpXn_8IBqK9UttIMmNwPgmJoIcQSIr5IXg0N3hj6s56ZluuejdgsZZaFT43i1AInK2s5R-1rGcGZZJs26kf4qETjYUzof33LCm_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جوانترین مربیان فعلی جام‌جهانی، نکته پشم‌ریزون اینکه سن نویر از ناگلزمن بیشتره :|
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/Futball180TV/90886" target="_blank">📅 13:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
اسپاتیفای رفع فیلتر شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/90885" target="_blank">📅 13:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOTn2tQg_whUJcSHLgjKZ0gloB5FRTWTwCgKXlihuJ4YRe-nFM-oK0z34nWZUGWEo6rQSHxMoR3KG1Zby_lteo12-1SwWoEuHsOJDmR5Fk5W7S6z0A9TxINi6NvO37IAcPDIkyCjWT_xSHdl_OQBVKoCgTEpjMIuWqvvSAJmHkDqwQtSZ5pyesB46VDXjkYENSDtLW6lnU63fnoG0-kYBaCfvBQrjYsGR8LWOF3EFCYO0EMio1e0DwYF8Zqsa8BwX5NCp9IawMun3rUz30aPCkbcWQCvEYvwmNGDhrRhzodEzG5T0h8Q7M-p-YaDNo6XW07RJLpjaELvyQqO_QHCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تاتنهام بدنبال جذب ساوینیو بازیکن منچسترسیتی رفته. گفته شده اولین پیشنهاد تاتنهام رقمی نزدیک به ۴۰ میلیون یورو هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/90884" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
چیچاریتو مکزیکی تولدش رو اینجوری به سبک چالش ترند شده فضای مجازی جشن گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/90883" target="_blank">📅 13:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6tl-Jp4OvMFvZ7fAQztMCY8UVuoSUPfgtg-eRIApQ-xBvfzA8zQbtTvQNlM6720vfVAh33k3Yi5tfHcjM9GPoEzydlr1Nn3ZtKxajp6VIYNYzNBW4F4vDXDUBDzKZFA7uBIC3FD7Q19iRGuF-hLvoUA-yFTO2i3eXasNxX4npMICqLG5tg8fZ0S32nowQ12GY9kA8WcgF77NF-Og59fPPD5HPYo1AeHvwmZL_ICObaZeRy1D4_Ef5yQi_BXFmTGulHXky5EoRvtgnAD18-2nrsucOLrX66hIt7cg85nNrrxwIfZVXFM4o_jsFVxAPlOgJRPp7uLxwdsPC_fuCn-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رتبه اسپانیا تو ادوار مختلف جام جهانی‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/90882" target="_blank">📅 12:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بی‌بی سریال متهم گریخت پس از ۲۱ سال
🥲
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/90881" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دهن سرویسا چی میسازن
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/90880" target="_blank">📅 12:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دوستان گشادی که به هر دلیلی باشگاه نمیرن و ورزش و سیکس‌پک در خونه میخوان
👆🏻
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/90879" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90878">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARoW9lAPbEdwnj79tDLFsouuX8u3t7Gyw5Wp2wJvv4H4bTiWEPCiRs09acXUnRDqVE-FPtP3fxXjvYJT4Kevdeo49arcBT0x0CTM0dxxpbPm3SSsiGSOLoLVFIMWt6i3cLQNkzvdyX62Tm_3usH3lmEb08ESgR_CBxokX3xml_I5-VwPuFgQ5i6qd9q_GegBf15FVOWC5Pg_KZu_ecLhqYxqGv80ESFl6_7Gjn55boqQUiylbW-V1PtKhrEVsQDzfS-VcnmLfY8lyAfSRvvnqXucfWMAiGS5IsRXEdn7dXYJXAMiKTDcIa_OOedo6XxRav5iQYkChVwWboc2Y6HqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتلتیک : اگه تو جام جهانی در فاصله 13 کیلومتری ورزشگاه رعد و برقی ثبت بشه بازی به مدت 30 دقیقه متوقف میشه اگه تو این 30 دقیقه رعد و برق جدیدی ثبت نشه بازی دوباره به جریان می افته
در صورت ثبت رعد و برق جدید شمارش 30 دقیقه از اول انجام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/Futball180TV/90878" target="_blank">📅 11:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90877">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشمامممممممممممممم؛ اشتراک تصاویر جوانانی که در کالیفرنیا زانو می‌زنند و ۱۰ تا ۲۰ دلار برای نوشیدن جرعه‌ای آب‌میوه از انگشتان یا پاشنه پای دختران جوان می‌پردازند، در فضای مجازی سر و صدای زیادی به پا کرده است.
😂
😂
😂
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/Futball180TV/90877" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90876">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برای توضیحات بیشتر: قرارداد هالند با منچسترسیتی تا سال ۲۰۳۴ معتبره و بند فسخ ۱ میلیارد یورویی داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/Futball180TV/90876" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90875">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ax9vu1EzfENjOMmRPaK95EJLr7r_2Fpo2H5p4uOY0veZW0A9UmvYzozP3ILm5FocbwWn1AzbJM1OZ2qUm_XvMFjvfz9HRgrtOFtOe7GuPZ2pXa1k6-E38WMTLfmP8aX4gL1-Ve-2BsoKcR78BEykD7w16adzkpzPjc1S3NZfsMG2DwQ5uW3YV-NlapdjKK9Mhf71c1Vg7UIaQabwrSV5io89aFmaEREegHUMemNuqIVHC3SjVJaVAAuoJ9Sl53Rtb-4vj5I-w9DO48EL5s-2T9oBIWTXcBMpxI7qbsg8lpPsqjgc6KzzcVLviovuKgk82Qx0XTC0WWDWWA8M1b_8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/90875" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90874">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
مازیار لرستانی: از اینکه پسر شدم خیلی خوشحالم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90874" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90873">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM7WIMrlwvVNx8CtILQZHJ9iidvJx1hDXP_8UBDUenXkyiL39TPGJM2OIsV7v7zDsxRbbVCqNs3nd-Sq_Mqsn4UocKIsAGRw_BOlnm5vM1uvr3IRa6UNlWU9K97Ee98CCVoBl4YZGdkjGQ4tILnCPqGqYIjC4h6qK4zFG6Ee73vczYcnKYxYx_oVBY7ck4EV8aCQJaTPRjybxSsKNO_5i-5-nYMtnw5Ml8x_of0ld5p2G_SQzmUp-0TXaOEr6Jg55wxYPJL_ZcQsF72G2jvFgmaFyfemTlu0FNpM9DRElOZWneYCjWOjzRREOmwwR8igKmbGiFuRM4pWM3w8CF5QIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90873" target="_blank">📅 10:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90872">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbKS5Dew-j-8nR73kzwn7R43jRzd0S1VyvkPXBvIYmqqQvNfA5JVDZAowvVAybji-EBQcedjTiFelNLT-64KVmqgA9bZm40NW8NkI9yPMZvFu23k25cVwqxTLV03t1x_GOvzblBD1hU4YxhiRyAA2l-A3QLt6Xv_dzMFhqUJ6R0XxUsQncL2jUOVU7wD_-p7Kb3sc8AYN9spR50a8xWSl9hw2OA9VxkkOUivPMfRLXFWweAhvyniBcuHaFFtOt06jPJfgj38lDVhMwjePucTA26y8QAU4dwaTC333uXwvnD6qAXTMJzg1QYan7nOI4_XmZMb_m1Nl06821CefifgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بی‌ارزش‌ترین تیم‌های جام‌جهانی؛ تیم قلعه‌نویی در رده ۴۴‌ام قراره داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90872" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjB0qaDWOs2AlO21YbJ1l_Z9QXvbdQ_5ag7XHB1s1uDysxCVlhYNGluHjYPMWb6BxviDCAmwpiakeUAXu8E2gjYpre-rgdm7b_12PxPBei_PH9P8aW4i90py40Qlb2JlbqDk56jW8m4DneLs6zG83h9Roypx6ynbcffPBDOo4yydpEcVAGcufVMgtKWBaIH5MbEy3GqVsOkUtba5uRrbcGCYBNAuCeRYwWIZpTqRZ5PVg0HOUm2WWayDPI-jHgkNo6Ad7rxN8LpwiwfBUKAPIRMOJDy7AgQ13Ow05DHb1h8UHLBoUsCdybuRMvclKM5fse5tDtFZR-uxsxv_sUvaQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇲🇽
رائول آلونسو خیمنز، که قرار است شماره ۹ اصلی مکزیک در جام جهانی ۲۰۲۶ باشد، تنها ۱۱۶ دقیقه در جام‌های جهانی بازی کرده است. او هرگز در یک بازی به عنوان بازیکن اصلی حضور نداشته است. اگر بازی مقابل آفریقای جنوبی را کامل کند، زمان بازی‌اش در سه جام جهانی قبلی برابر خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90871" target="_blank">📅 10:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn449nsOAIevUxFpsNgKHoOkVTi55c7U7qT0dm_DATr4YMzxjZWTP44nn5OIoATLjqNR-d3_N5CWzmDsE8V5CtQRewV18BN16_Zvb_0Yc552xG4L2bwpqloKd0kdeDuKjym2MD-fY4LbgAVOXI2iZHvvMOS0Hvt1389pMdvjlbSZk8WxoefT-K6982xs2LABeZGmMyn4Kr7mHPUidLj3ZtmeZ5WQncMF5f0p4v6THFeMyu5FDwVNar45NAfZpigT_y6NFYV3lOwGx09zl3hJk22I7TwqiRHFQMe3Le9oni4YLBOTiOKWF0amz5U8JY5D5qtmnGADyKRFNBSIHXormg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد ریدمان کی‌روش با غنا در آستانه WC
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90870" target="_blank">📅 10:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=TRIigx2Qh5la3YOj7n9cFit_laMHtENaHtVSvR7uy7vBjme69mMIOmVvzmTJcKOJ5mUStO0JINoqecceimZeJxxXXrwCNjB4wCR_EgjqG-QEjpoBuLloyHjSgpl_Yz_z7zeklO4egOdVTUxshoLH9BoFIQN_vFbWDNBCWOdLpbBkog9uB1nT1AuQHIrj1eL3XNgOr_EBovXZIX_Ex_xfV_LbbOP-TmpucVqo7_PnqTD9-06enuBl1oUttJ58wpz-D8ZjFVDGYyFAwZBBhejYwrdUZ2oOqP0dZmbS4rxuApt8RziNsb-IsIoSUILXInGxI41QZDa-Fhhd5xGs3MzX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=TRIigx2Qh5la3YOj7n9cFit_laMHtENaHtVSvR7uy7vBjme69mMIOmVvzmTJcKOJ5mUStO0JINoqecceimZeJxxXXrwCNjB4wCR_EgjqG-QEjpoBuLloyHjSgpl_Yz_z7zeklO4egOdVTUxshoLH9BoFIQN_vFbWDNBCWOdLpbBkog9uB1nT1AuQHIrj1eL3XNgOr_EBovXZIX_Ex_xfV_LbbOP-TmpucVqo7_PnqTD9-06enuBl1oUttJ58wpz-D8ZjFVDGYyFAwZBBhejYwrdUZ2oOqP0dZmbS4rxuApt8RziNsb-IsIoSUILXInGxI41QZDa-Fhhd5xGs3MzX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🏆
چالش بلاگر آرژانتینی با موزیک جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/Futball180TV/90869" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇧🇷
مردم ریودوژانیرو این‌شکلی در آستانه جام‌جهانی؛ خداوکیلی خونه‌هارو میبینم حس خفگی میگیرم
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90868" target="_blank">📅 09:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=CtIdN5WnAbZKJXcgZUz11MzonzELmI2oo-xwOQdhw_mGmVY1obrGPIBxMGdhOTyPAzJwd1b2HGOclrv4K9w-RPIMlxzaExppGYgjvGEBBus4SChv1kZ_sEm9swC3Q2UNdXWCwnVkEXkAecMWr7jh7taoApbHxCLvWU1geWD6hRMOEiHK6Y9OWw81lD8gk0s6HjsdqzkHBwfPplQCcx43yOJf55sieb-GpQ2MYj9q3gvIF1I8SRTLSBeob4LaoaQZA1yVT7UL3XVrU9rfm0XAeR7KO8DV1WcTbef2d4KV0OW6JLlSCA7d7qAgh7DV8IMPgItJXEHX5jpTSGpx_VldXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=CtIdN5WnAbZKJXcgZUz11MzonzELmI2oo-xwOQdhw_mGmVY1obrGPIBxMGdhOTyPAzJwd1b2HGOclrv4K9w-RPIMlxzaExppGYgjvGEBBus4SChv1kZ_sEm9swC3Q2UNdXWCwnVkEXkAecMWr7jh7taoApbHxCLvWU1geWD6hRMOEiHK6Y9OWw81lD8gk0s6HjsdqzkHBwfPplQCcx43yOJf55sieb-GpQ2MYj9q3gvIF1I8SRTLSBeob4LaoaQZA1yVT7UL3XVrU9rfm0XAeR7KO8DV1WcTbef2d4KV0OW6JLlSCA7d7qAgh7DV8IMPgItJXEHX5jpTSGpx_VldXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر کانادایی تو استادیوم داشت ویدیو می‌گرفت که اینجوری مامور امنیتی کاسه کوزشو شکوند
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90867" target="_blank">📅 09:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90866" target="_blank">📅 02:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcRfkflayUPlncw-Sg9UqSzJmWbklzFsx-V5ie5CtH2v7hqusnwT0Hg91GJwWONTvcroE2trvSQG2g2Uv1lAVoeTkWmBUG3GzYrwApEXpg39ZX9pYNIW7i7GXWsaT9oFtqM9qH3tNn1H7P2EblIwiRmshlCTdUJFZtmj7jKUBytCjsTrQ5KX1_rGWjsHFylSx-ocojkDIU8iDmOXDSmOD-kKu3P-40_x-RtzaDaNfJzEl2Rxl5mUCRMu4slnvivSTCke6bekKHavAqPqA0BQUp2H5ApOIWRK_mwIT4MhnOPY2NJDvQ_mpVyW01G-IOkuj94MXkIcjw3lp_P3uh0Vhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ با اعلام رومانو، کوناته با قراردادی چهار ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/90865" target="_blank">📅 01:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/90864" target="_blank">📅 00:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری؛ ریکلمه: ارلینگ هالند با من قرارداد رسمی امضا کرده. اسنادش موجوده و نمیتونه بزنه زیرش. فصل بعدی شماره ۹ رئال‌مادرید در اختیارشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90863" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/90862" target="_blank">📅 00:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtaWKSmS9W6Ocprr4BGujmo887xm5l-7jwLswRpjQ3qBWYYe6a5tWZ_dacb7Z4jutLQAJNhoVFWb-k70Zn31q50cx3BEawjurKb0toJyfa9YgtfXfzMJdwzO-sOwpddALNHcwlTY3gKJel1czm-M0FNnGZ2i375szGwwd-9cT0moI95VeyuT2KDylfgrPxjHlgwo5OYiEy1eCdb5BZ7zUAzRvDMXFMKwoQoP7npkvX59XwPl8pLaa9era_f3tJ926X5eGEvNMqTVEAaDgGoqVFfcSa69Q7eIrkZpLtq_JUa1OzSTirCOV6g8l7jCU_aUrS90tIW2xOtD7R2cfeV3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد بزرگ پرز: کوناته.
‼️
قرارداد بزرگ ریکلمه: هالند.
⁉️
با ریکشن بگید شما: پرز
🔥
یا ریکلمه
❤️
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90861" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZx6RgfW3cYmb_1F7IaJI26hfLxQAWoN8p48LQ6IHqBwvmyytjhZgDlGTJKURem3pEitT-HpxMifJznRrqZbQ_bnRHUULjjIp10ekFpdLCH4jyYGoEtudq6rBTz9oF3X0NaVAAIs1z5TF1AprgaUuB75C6Ke5a9ejFGQqM2GXnsCNQ9RggkstEH-o9Sr97nxIuMGm9WL9wQypt6nRgF76Qx37LuS5j-wcTA6eJ4CFMJwFjXcU9Ql9gz6_fw7SLjxvRZfozkGwQDecUOy3zl1UMpG5OCcHpo3T_eaapYpMcC-EEyU6dAlLIo-4XIubvxs5fsoDB0lZvNAKSGWbvtLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90860" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90859" target="_blank">📅 00:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw9KhKc19WkMrgnfungAjTqG-zWyoftsBmegkYYOYJg3nxG-TXq5tNvAPZi0i8p4pxQ8Tjw1lAZnGZLoxPEK0DH03Zo44AE0-7r2yUcRSMUr2emppmWVADygJhsLGpsRQCpHUDJ288X5Zs78D2ZbmlJhSfeuA91BRQAVKf4TjeXcgdChxBhxlUId0GiYurYfqSAmubHjfGUsRF1_mA9LK8nu5xdryjBDkWd-Mr9KHeF3pok2BYG64nMoP9K6VNY6mmacd3fR1_0qGFUHX4U-9OzSBTajEvu7zfzjkRJePRt0jQtGxMv7Mkmc3Yq5ii4seW6y1Y9_3LVELAFN7q_7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤲
🚨
👤
استوری سردار آزمون برای مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90858" target="_blank">📅 00:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90857" target="_blank">📅 00:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=A3WnLfPxqUNZHmvZKKnHqSnv2C0JnrvaXU_CSt9qsQX56w5etSk9spFz4-vQtP0TSJoZnEzUfYbN2oY2nlW0sCAgaXgsUCBEvGXxUKWWnjGIDh15vHqWeQ62AqGs68t7exPjxUReZzb3My8VStm7f6WePSJzOWBJbTLXYV2Bh2bz-lnGG5mj1CHZ1J7c8eRPeGpIDG0uWeRC2NInI-LPFYBIBO0bB_Juek3CAxgLh2Q1gCKK9rvbolBqnry0OCHfzVF7BsBhvqSPeF64XRNcsxR82L54b1dh-bZgbOAR1Ox2aLmJ_wus32nLJ6TzeAG5PT9zqGjqeINkRvPEXIZJ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=A3WnLfPxqUNZHmvZKKnHqSnv2C0JnrvaXU_CSt9qsQX56w5etSk9spFz4-vQtP0TSJoZnEzUfYbN2oY2nlW0sCAgaXgsUCBEvGXxUKWWnjGIDh15vHqWeQ62AqGs68t7exPjxUReZzb3My8VStm7f6WePSJzOWBJbTLXYV2Bh2bz-lnGG5mj1CHZ1J7c8eRPeGpIDG0uWeRC2NInI-LPFYBIBO0bB_Juek3CAxgLh2Q1gCKK9rvbolBqnry0OCHfzVF7BsBhvqSPeF64XRNcsxR82L54b1dh-bZgbOAR1Ox2aLmJ_wus32nLJ6TzeAG5PT9zqGjqeINkRvPEXIZJ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خنده‌های عجیب ریکمله به انتصاب مورینیو به عنوان سرمربی جدید پروژه فلورنتینو پرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90856" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90855" target="_blank">📅 00:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9utrce-aBAYIuguhZGGdKtC-43EvdYwkpVU5Swio5CL-4U6__AqA-YHxMlhiKtFxhsJX6BfQ9t6v3S3_z0zOQViN3u-XdE3T1R9po8c6_rZGaoNxjRozZcZ0VGxXmRhDxyiBw3oa4BXznWy7zfr6wxWnQmrRMBV7Azyr6sPCgCjfXj-dLC7L7Uo4BPmI8gVCuSWvFGJblsXaYu-CR_EGkRqWTatvCCWgPFLxQxV47Oj7037uviPZUZB6VKCd_EUKTS_JRPLEvml0gYIgNMVEy0hIEiofZ2kMT3MkR-RFhMNl14rtrSIs22PvJkyfI2mrJGV8D35L8XsULsSxoWjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته اجداد ریکلمه رو بگیری به خمینی برمیگرده
😂</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90854" target="_blank">📅 00:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه: سرمربی تیم من بزرگترین و بهترین سرمربی فعلی جهانه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90853" target="_blank">📅 00:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90852" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIOq0yTqyp5IHVlZtSXDFtu8fj74RfZuRg8MElE9m88-b2VMY2KcWadepfoG0xMEdxSfRmEoCjsXtKZBcpe4y1Tu2FK3P9xtAbzwOu_tBfbnzD8E-q00vDcEV7Q07lEIuutHPIHByESMfUq1rMAAeJU-HrGA917kV-hbd9HSnBJQmVhISEGvJjMKIhsIBPkuFaoJiqfnSRu23RQryFB0OUiRPFR1Qj5SN_eGVVvJ-yfcmgY45Gw-KfBkBnqR1AGwTYUUJ1On_cmBiNzQzIJrOYJ2H1BTCtjlWKYpoz9F9-BTsNAKfzI4Z7peYTVlFzC3-KCtN6G4HUs-vO5MY6dhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه
:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90851" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
‼️
انریکه ریکلمه کاندید ریاست رئال: در تاريخ ‌فوتبال تیمی به شرارت و کثیفی بارسلونا ندیدم!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90850" target="_blank">📅 00:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90849" target="_blank">📅 00:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90848" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90847" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90846" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90845" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90844" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtlxaVUjlYfAvll13zhDk7mRnTuCHeC6Bpd3YXjmYccVLC4Tp3UH2GYhoqeztft_zCyrWQh714ccIZViegHsojrKMDdWzIYFtcaIWHJgqh09lt40-YyBOz34-FBpOt5rLEXSDLN0C9K8ZcNTNy6kddQpmwuvJ5m6DFm9LJbom7rpQdft5u_26RCnobVUZXoyuedqUnPAHFkfKDo47xBXUz4ED6QZ7XJrxLE1bXWps41y0ELRtgKIbEN7YNNzsL51sfURYsvdsnlBETclQP5BBU7AszpKe_xZUa0Z_yYvTKEJ2LE3BzqxJhxy2hWH49eFCyr5Rts2BbUpRCdvluGE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ پرز فردا از کوناته رونمایی میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/90843" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHGxewESev4u86IJrjBMlEjfkNyvbxR1Goh1HqW4ZuXZQLxtIpiLjGhkcGNhtrE008c-OWahVEpp890bDVdcZhdH_fm8SIts2Aerl4cdLhz5jjytFkkXQbYb2JfKX1dgBm8uptdX75MTK63mAX1H68fm1XbUDx5gIL6Pa7D0auZ0IIW1YMKzroCbrt1gimrWkMQxs1ozS6ocjfueE_sp-4tL_CCCCVzqMWFa4NmGD_H7JPikdU7TXrfU4TxE7nsebOzpc3CFRkBhANq8vXqro8aRFil9bY_0zBkhO2fKsd-9oJ_FUeyn5SJwUUnsqDkng5qRb_uxav214jLu_exU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90842" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkRC2MII4vJWgk4ic8zcjjEJItkv67Ti2EK-3g9JK95fJHoRNU6suHfnNYMCXxhTMrEE_0WkgLT9L6clS-IzeSATsFFBdgSiglSz4dev8O6L1cZB7BK5CRe-oL7oSEXFbafS-SO3GX4dtj3y0t5MhGMqMjlYppOk_sgXC_H3tH6AgqzUABMMOhioB-X5sHvFyJsNkPx9xiCj2-643HbmrC-cKsVY_RwH9EE1avAZmA17sRqla-ap2upqY5FI47V0HB3Sb0zZmR8jdXRs-NZV6GZ4QrULF-9cFDy6xFOoBz4l2Yfoxup_k224rXa_cjGtRkvX9YeZwWPh3W0QbBWzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
14 خیابان در پاریس به افتخار بازیکنان پاریسن ژرمن تغییر نام داده شد
عثمان دمبله تبدیل به بلوار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90841" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ie0NLerD76xf0rqr-oST8noq2Om6yzpkDqW6gl15HoYFtdLM4eavn33sxE26btOK14FnXgpDpC0DVdZhlXgL2rJlMd1seaTAePUmrX3Ox7uBqaj6dg-JmJ5lxnjph8KGFBjm1V59BE7ED6Se1Oc-M9F9z7Li3Kmm7r5V1eOvt1wgjwZrbR0ZrLw2F8YdapeUpNaS5sQAkgcbkiBTpHZVj0CU2g0DDIMS3VrdlH3QVjTAvbRQuK-Zy698bDq2DmNueUBiIohm4fN2pAvhzppH7c5tQ8mn-2Mk_vYT0QUYpqCMH9jATslrsDZuVk1Dk5m7G5u5vX6qG83-_sfFtrIKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEVwRE-F0nEj46vCMfHIm9YOH-R1PmIfLfmuNe0CObLBSZK0uNjpZOs8E7V25xe_6ICS2eznsJkvUqCs1kE3a_L8HktcHNUIRavOizJ4wnQoTvc8qILnl2-LU0RRqzYsKJDLCN76Gm_PgGabMxe5tC-MmcTN6MiJoKhHzqozF4OnpkhsC6Qt0QNWLhyOxwwKmZS0u8AnlI8qFYHolb_S9MDKJDObdNFQ35bhg4-MOjpbyINPSBbKxvt1p0_zMhrtIYLxOnErFWYH6SoA-ADko1ICFhhDSYcxymPsFWHkzWIRvf1qSypGFnXM_T_ObN1SbYScqmOXuWofN8Xb4RG7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJ8iowIwgtE93LaFwoYiMe3cD4Ko7-aVkXcCW7EkNppfqC3Yqz_aMFLcN8PsESQAyyjJVFQZLmoQlOtVxp7iY3aUkLgvaEV3teWh8Od8xaMpWpn-gM6uAau6hEUPSrVVEazC4kqNwaAt3DzkRNwW77G3Nvo6mmPzF67qFtmKEK9msRGwA8_KZE7jLPcr2kEOcBr0-zatvYL_wj523-ybp6NodgZATY9NFn_jut2i0qpwzFQ6xPkiODfNu75TelBvPhappazLE10vkj-DNTkGseTvftj-lXLN3DjVKe9JluJc3xcs_2V-X4NDZ1qTTdKQOnmH_PV6CJBcogziQRFUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCn5xtgpXR2ypbUVQ1neHMxhruLEDKUyz5S-r0r9NUIvj8boEBBwWpk4ZDUzHa_EtR-COE9IhBLkfwfLt-9QcmNZDUmQtjumubqfQcUkiZ1Y-E1wCb-IHjxFqnkwGmNk5Mg0D7VeI15ma3-1ss48y3R3NJyFOl9WnGUomaiwrfmmsHlESUYGSaTrCll9-IpwWFGdDuG2GXGI5ZLVlVvu72zfxJ8H0Yglwiy1prLZMT0IU-LXr6-ENUBqG5aHQS0jXc38CZl96aGjfRRkLCmXqLTiOGNr4ldixDlFEYrv4Sk77eJHs4dhzudG57l8EOr8BC96KTji8oBFN8N1bP-4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oesGE-aNYOantEkxX-QhyF8151l96hoOjdI1RPzHJOv6L02nHuTokOINJHHxPhSo8onxY_nCYneVWujnZZYDXfhXXoSR8F1nOJ1Sd7P0HN-hD2rt0BdBgjRKQnYtRSbYuEULli0VYMUaPBgRJICpbfZwCBqWQWqaQUUxJk2l6rmrAGiATvkFgC2GhwLz5vnyEcjdjb07vD7PTpRQkZVjgn9bvfVPMzyCrbq1u_5fxu16ayWLbs_3sxuUYQnQsOJr93VruUPnvb97ID0wflCTLFXz1EQCGQm2Pgmjw2KDMP8TxZgkHjbJ27SoQq6L6prdvsC9UcU5nm6eld0ZZS--hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 روز مونده به شروع جام جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90834" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-k44PVJq4ExVqIww6N884qfTIXJfJqvCih9Cfu4jW2km-_cjxwrx8-r0Q48q_p53MVIjJGKHy2OdMa4621QRzPWt3L5GY_5yfcykwv2Yu7kp5bSSLGqzZhA47BG0tAR3RwWtn8_C7QPmnXK7fzVRnwRVVoNAdJfJDds11eQopy11XXquOeAQRHDrPorlRmH-YABi2vQExROTBWRde-_Kpb2eklJqBt5NwRLukUUMjeLCREXppUnIot70Sq04l0pYYuIn3akQlXxTTdIZAO9hyo0Fcx4lqG_kwTe8SMWJRBHDKz1aODKwwyHjxRUfnDAYPZrYokRZbFZM4V28EsPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شجاع خلیل‌زاده با ارزش‌ ۱۰۰ هزار دلاری، جز کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت.
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90833" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNOscJRSDZbD2ITD8IYxxyXwiZR6OfK1KWBqEaMbwtnZVW_-4n4dVfA6NorWKYWtB6Hbt4q5zbn1dT6rlh62floA9TKJRn1kc5PdS68sOsWBRA-hcIDsk7td35VOcE6C5w533HoQJ-HBY1vLdiTQ1VYEy0bcpb76mi8yhgkVL0vD6EYsECoLhFj0nd5K4sARLtPp351xZ4b8G9jYSkJij2rsDTCoRRTmLbPtRSkaNDFOvRclD88jmVsMO1pC61TtbZqZU-vZA4gnC3ai-QEJhvMHhloY56eH--dOM4PGBNjHtagBoMkkMhOkvyvK_ncoC9l6BIPu92ClB3y79NxRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری باشگاه استقلال برای تبریک تولد فرهاد مجیدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90832" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9WgZyW3OOwn2cdFkWRClZBgaB9ma5SZ7RW02wFQqHhYmbYQ32oOk3YklzCK5CWOVTLoq5KSl9mKaCDYin7IDHvhUbJvSQ2dS2m833xcogA2dtaiDE4Hzee1-V5BzjTjWf04KAHtHakH4oeyDkz0uXmP7IskOWQVg40mgdwxTRDY0iD5ERMFnswwVU9ZwNUVeUJ_Lrh8QGZ9V4DrD_RLbB_8L8aFccCVmMgPkomqekLI1Cs7km5nNJPZRn6Oi1ZU45nHZKHz2WoLQD9jIPruH0FXZMkuIzDJOd3XQ2d52E1i_dE87vzspvNYylQq2AG9-hq_ot3g2vklc2JxU48R5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در
۲۸
بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در
۷
بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر اسپانیا
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر عراق
۱.۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90831" target="_blank">📅 22:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIz3pVApn8-KIz8tBA3pJdoCChD7LmA8IDvljDcb4tta6uw-M688HbykqV7ZtM4FAjDjOAdgg6vagSPhOhyI83RXugePvwE_9TFaVeGEmLP1ndafDPBe8hKtP3JngiFqVOIVKNZs9SZkI3CeoIcU5X3TuHb2QOzpCtSCkhh2h54l6LjDVqD4jO1fNpwWqeUL64YuFL-F-jF5IjdTGX9wPrFkvwu-k2PILIAXzxuNi-xrmqbqaHyDjV3Ppjf0Bz6lgW0AIE5lHT5ImvTAEZYTNulhkDri6wC6N1z0qlQJkpO0i60I14W1SY3LAd-d65rr_88f3ljvgdRjeb5L_1HMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TOO FUN🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90830" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVDC0UrLA7vf-HGJpEjKGYu0DOIf3ne6KpneBKBX_VfxtLiKULTGiowMaJRfGHu-bkSzeCeTnYSaU9iQLHDmRGlFJG-XnxL6MaxHw9jYIM9ySs00ZHXyY44KIDKYictqKaPNR_tic5YHHemMmGXgYaFHrNga1Xyr051xtMQbXieN1rre1kuSzra85Bf1gbFLQnet-mCpNS-funa-6-iTqhdw1lN9-T1es6s94PLnrGZQ2gUtYYy2oeCc0NDMCthKav4b8yol7P5zkG_jnCA8SC3YiqkqWRT0aG30aIimhrc9SzzYO8rKAUvMXAFLornwP5qPU9QoChZTJfbKUUj2PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: برناردو سیلوا تصمیم‌گیری درباره آینده‌اش را به بعد از جام جهانی موکول کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90829" target="_blank">📅 21:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwxUFnYeStkYJ3qKaAH-TT_KCBj9dLjX-pPYIjMH0ZJZzifBheljJhgCZnrzBepWDL1ndr6mjpDrFK7Q3a1H4bLgOFG3VoPCyTWmvGolFZfiKKPTdEjb9sY9d2SJggdQud_rqRCQh0uzUg24ZmhVxK8IQApDCHRrRvR-xIWaAZ4eL9HS2BVzxLds74SK3GsrJmM3cEooQfsDEPJqf3qo3HlPHHTmzkokGKa4SsAaZFjLsg1gMLvMv36tO75u6sTY-xBwNpQa_5elKcl4i-pDH5khJJuhJnHN-bZhOJbeIvM1RK93cL-FTVULEdzsK5VrUtCnVouLTSrXoSlwD7sCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzgD3OZO8kFNh0orEor8lSUXDK-sLd2b0EwqZkMejIh4_8OtHqUpXsanMX-NIa98Mo8ol8fHoi_XX_HMKP-6WuRFpHwIhbLfzZD06rbBk7Vu9KFx12rdXgwdD91GHUDPxhBfwCYqeHIVPaooWJ4zaklwn_x4pXad3zeKJfOS1o21lkFhwluIkKvp8UGn8L7AIEeNC0407VgqCc6Hl4skXVQ9Glj1wWYei0XE7ht1z22qJqL0yS-McyDPlZVGYjKOfi-7rGJVmzsBikadIi7Vx3qSkYYRhtuU9jz11EwPPWSgnaX2L3CN3_JsD2Bpv-NrUJ5QhFMq0RCz13J0Sotg_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEwje1ikEHamw5zQxGG14UGHKvh5v1o0MYOwBXE-nnj2zrBBTaB3fZ38rAgE0wgdVXJyoqaoJP4ADq7KTFAgbE9VVDnkgDSjbD8uzNL02ocRqMaX0CsXMdOBNt6TA-P3uiNlP1mLR9S8_ZoR4I8TkgDHSJ7I_Odq68qG1UdgLjzVitn826Dz6Yuo3LriPJ0hNVaqM6PFuvd58JNpmJt4DCZ-p5a49vqqTh3NPK7D2IPxKuYogO6oEHQOiGh9fkTIjMop9a3N22s6scg3nSeMNP7CFQzjJPwvdREG_QiSp6-xETFbWXl-x-bLPpdgIWjjXzDxkv46Qj9phjjbUY85gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و حال امباپه و بانو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90826" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
موناکو در آستانه خرید کاسادو از بارسلونا است، به محض قطعی شدن برناردو سیلوا هم به بارسلونا میپیونده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90825" target="_blank">📅 20:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0kZy7dm-0HR8wlNvfZ0yGK9QCtsQxVquDPOTEE80bbFNjO0Qzpsrs4fpZ8z5IZ9aVlztGo268lc4ucanVY-pWXV8ju9kHMpWhDPoeechLwsXFsCK64EQ7u9a2w0QhweBbocMmzmao7UXjL8o_M_etjeFRNd5lgEoWBa0fI5n2C-fpPItoKl_SxgKq2afPPmgeo2SmCPOp5L3RbU0I61u-NiWgqehux7H8woFXOQbH9tUwh-VpXTmhJeC08YCVPSTmB4uZQAE5vgJzM5b34QrC9brJ5WNqRBgtci4_DimN9ShCO2ZRq0yNz83duR4omKZbh--4QCeagBwJCn1i3S7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ در صورت منتفی شدن جذب گواردیول، رئال‌مادرید با درخواست مورینیو بدنبال جذب کالافیوری ستاره آرسنال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90824" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=jyNQmQmUctspffgH2MEzEI_TKnnhAyk9VDD7_1pRBTZBHKtl-3XySCTOjzsMyxwlz7BAdbmN3bUEv77gD4MK-j1gEfEFCsFGebIigBcOoN_b4g6mNVwBa0tAOJ4nW-1vksEBRyzqYPpJbQdlhjh48Z1kcOQCY7XiNeYQVB9Tku9AjKQYMYA7iO124ruQ5wovqlgYZ0pjZVuRL-aybMTT-8CLq73-Zy0NA4Eysm2H-_9sEMVyqMpQTIQPThwWuMRxCDg64EKPkAB-QGzzkwuf2xDuiWV8nX0lluqzp8r4Qkwshpw4Fix8O2cfli_Eu1DdkYpQp9-6_lMhp7vlYRw46EiQEtBnkAapkvHRel7CYM0CwfDNQp6pmqcOiQRM2c0AYBgw9Zy-CACB5_ZCpSNXl1L9Q9z21xXZn1ezeII7dpResfpLLD79voL2oQYYKnCIdtUGGgQLtFUHh0zEZLvXy0Q2LDSQ0c1Px6Gyr7lLKpIg2tjVIkwUG1HxbjY5DzycUeYyEgJlfpmteh5SrNBPpnMapkZrPTc_4qotL1_UxVfZeKKhLxC91TvOWRkLRgmO1iXeTZNAJZh_AgN5rTVQRHiPElzEdinoNaUH5mtL2Edw4FsuVv4k1nwX1zHAzXI7qKgvn-t1tARD7vKA4GgburGj1KgXyAKnz025GLwqyyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=jyNQmQmUctspffgH2MEzEI_TKnnhAyk9VDD7_1pRBTZBHKtl-3XySCTOjzsMyxwlz7BAdbmN3bUEv77gD4MK-j1gEfEFCsFGebIigBcOoN_b4g6mNVwBa0tAOJ4nW-1vksEBRyzqYPpJbQdlhjh48Z1kcOQCY7XiNeYQVB9Tku9AjKQYMYA7iO124ruQ5wovqlgYZ0pjZVuRL-aybMTT-8CLq73-Zy0NA4Eysm2H-_9sEMVyqMpQTIQPThwWuMRxCDg64EKPkAB-QGzzkwuf2xDuiWV8nX0lluqzp8r4Qkwshpw4Fix8O2cfli_Eu1DdkYpQp9-6_lMhp7vlYRw46EiQEtBnkAapkvHRel7CYM0CwfDNQp6pmqcOiQRM2c0AYBgw9Zy-CACB5_ZCpSNXl1L9Q9z21xXZn1ezeII7dpResfpLLD79voL2oQYYKnCIdtUGGgQLtFUHh0zEZLvXy0Q2LDSQ0c1Px6Gyr7lLKpIg2tjVIkwUG1HxbjY5DzycUeYyEgJlfpmteh5SrNBPpnMapkZrPTc_4qotL1_UxVfZeKKhLxC91TvOWRkLRgmO1iXeTZNAJZh_AgN5rTVQRHiPElzEdinoNaUH5mtL2Edw4FsuVv4k1nwX1zHAzXI7qKgvn-t1tARD7vKA4GgburGj1KgXyAKnz025GLwqyyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم ینی؛
مصاحبه شاهکار این مرد وایرال شده؛ نزدیک خونش رو زدن و اومدن باهاش مصاحبه کنن
😂
😂
😂
+ خبرنگار: شما که خونه نبودین.
_ نه ولی کیرم دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو کصکش؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90823" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=ZXbI7hTLg2Jl0uac2jIHabKYSMYduQSR3KMJrMxkVm0nG_KOA3sWnEU5Cbzeoj4fnNo0lX9NOSH0LYT-MlAu0DZ3wm52p1aTEu6RTp44hKdeaZbdkFrLNrS3_Cu9i9Qk8yEo1C65YuUhCrTND8upvLvUaUWBoB7_Sw0C-iPDFiaKdbxvCqp-Y_GTfOGHQBbUdpk4ILlVNZemSyUOx_mLlVx1kJbc7yCJnVmonijOoolxkLzpaPl_QH50pFUBdfKe4DxAwe5jmDMNtvOBG09j_T9OtbsT9aRsOgoL3WVQ477aZkPS6dxYSyA5J1IOis4aiNevOfo8eQ8TZt-OTtsAlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=ZXbI7hTLg2Jl0uac2jIHabKYSMYduQSR3KMJrMxkVm0nG_KOA3sWnEU5Cbzeoj4fnNo0lX9NOSH0LYT-MlAu0DZ3wm52p1aTEu6RTp44hKdeaZbdkFrLNrS3_Cu9i9Qk8yEo1C65YuUhCrTND8upvLvUaUWBoB7_Sw0C-iPDFiaKdbxvCqp-Y_GTfOGHQBbUdpk4ILlVNZemSyUOx_mLlVx1kJbc7yCJnVmonijOoolxkLzpaPl_QH50pFUBdfKe4DxAwe5jmDMNtvOBG09j_T9OtbsT9aRsOgoL3WVQ477aZkPS6dxYSyA5J1IOis4aiNevOfo8eQ8TZt-OTtsAlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ گواردیولا برای پپسی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90822" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=F7OYgy4S6yFJBhMhYGye_Gjs0_efyGYj73uxLXLvfbnxTTN3hGMHDSIwFFIA7uFLxF1Ez34XttgwupqoFWb-nMtNd4NxwlnyPnlnWAlXh4CcnMobtgWkltbxH8alF5eUxvm0FNoVkYmXnZrT8UZcDUs3YULKHgfO0OX9_7KjbzbO8WxVDNq-K5qcFUxyMzsRdBH08MM5Ow7FZuDFum6995FQ7VQcpR9jVg1U4jfQH8GsoxemHPUF8Gb3g0jOrSKHEvunuHFR5eluPNIoeWMd6aqdvrUVUjDgRUWsyC7oqe3r2QgaDs-zf18M9ljrNNxsMMCyZl84fiF6KFmkG08luA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=F7OYgy4S6yFJBhMhYGye_Gjs0_efyGYj73uxLXLvfbnxTTN3hGMHDSIwFFIA7uFLxF1Ez34XttgwupqoFWb-nMtNd4NxwlnyPnlnWAlXh4CcnMobtgWkltbxH8alF5eUxvm0FNoVkYmXnZrT8UZcDUs3YULKHgfO0OX9_7KjbzbO8WxVDNq-K5qcFUxyMzsRdBH08MM5Ow7FZuDFum6995FQ7VQcpR9jVg1U4jfQH8GsoxemHPUF8Gb3g0jOrSKHEvunuHFR5eluPNIoeWMd6aqdvrUVUjDgRUWsyC7oqe3r2QgaDs-zf18M9ljrNNxsMMCyZl84fiF6KFmkG08luA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف عکاسی با رونالدو توسط بازیکنان زنان پرتغال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90821" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=I-4030WPxZFymLuen4JrXNQ22SwDFYnBLy2Vp1SRT8tKXZ-G3wYaIinIqjSbufIDaSwOgctS2iCdKiBPWkWFpd5TrBCVaHVwfRfoH77K77RrUUFVp7cqc4MkgQxdVPNU1X9hwRTR8aPxN3fTiJWFbs8GhS4gQYcnDn-TjZtvfko43uZ7XM4wj_u2Mzz3qoIP5wdIVcOjVskq6SgCPmbwdGH9jIi1YFQKThvnWBGmfbo59SC2yP1Y-hQd1DFo7lPgpe58Br9AGycjmtuitFZpOuLry3iz3tgnzQiGYB3bOQN2UxCz-bqxda7EQU7AwXJU_1AE9P0bhmv_3yJGFJyVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=I-4030WPxZFymLuen4JrXNQ22SwDFYnBLy2Vp1SRT8tKXZ-G3wYaIinIqjSbufIDaSwOgctS2iCdKiBPWkWFpd5TrBCVaHVwfRfoH77K77RrUUFVp7cqc4MkgQxdVPNU1X9hwRTR8aPxN3fTiJWFbs8GhS4gQYcnDn-TjZtvfko43uZ7XM4wj_u2Mzz3qoIP5wdIVcOjVskq6SgCPmbwdGH9jIi1YFQKThvnWBGmfbo59SC2yP1Y-hQd1DFo7lPgpe58Br9AGycjmtuitFZpOuLry3iz3tgnzQiGYB3bOQN2UxCz-bqxda7EQU7AwXJU_1AE9P0bhmv_3yJGFJyVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
ویدیو منتشر شده عجیب از دولا پهنا شدن بازیکنای تیم قهرمان کره‌شمالی با حضور رهبر این کشور
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90820" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNEX VPN</strong></div>
<div class="tg-text">⭕
محدودیتی که لازم بود برداشته بشه برای پایین اومدن قیمت کانفیگ برداشته شد
❗️
گرون نخرید
⭕
طی ساعات آینده قیمت هامون به قیمت های قبل از جنگ برمیگرده
😇
منتظر باشید …
آیدی کانال :
@nexphonevpn
آیدی ربات :
@nexvpnshop_bot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90819" target="_blank">📅 19:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
#فوووووری
؛ باشگاه موناکو فرانسه بدنبال جذب مارک کاسادو هافبک  بارسا؛ احتمالا بارسلونا از فروش این بازیکن رقمی بیش از ۲۰ میلیون یورو درخواست کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90818" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90817" target="_blank">📅 19:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu6MlmYLJDWlyiIQOeK9KAY-VFNxSW8vO1olawCVWDiyxRCjfrdon2uVVCSxpvB9semZ-EyzGCxx2qSDDjcA0UEwo-91jlxmdNBTtN8cO_x1t1DN5i4qRR5iaH_Xa6s--TWWoBNg8TF-7JG1T26wvZMfxi3AYQ4E5N1fyI-B3zsX1rj9L3tc7jmQrt_-NGtZdaQY34KubSpRWNzspnQ9n8LwrgilYVJZNeDEAuR0s3D2GjCmBLYzJMPdACpoYHyRrwtS5bOkC4SYDv7JoomF2OFouuy6IPi0xmf5csarwIK3Elxg2XlABc1MF9cYBtbBfciHGrojZ4hHqDErBEfMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کونده :
«تا سال ۲۰۳۰ قرارداد دارم. در ذهن من ، موضوع تا حد زیادی روشن است. وقتی در اردوی تیم ملی فرانسه هستم ، این مسائل در حاشیه قرار می‌گیرند. فعلاً تمام تمرکزم روی مسابقات است. من در بارسلونا هستم و امیدوارم به حضورم در آنجا ادامه دهم.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/90816" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تهیه کننده برنامه پاورقی: خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90815" target="_blank">📅 19:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URjF0-lEJt94eZx3EyZtZNvRs37UfLjApM7UqegX6SdvS6GWz1xtkUIvfyi3O7-GQVkkN5-IlRk38fuqZwlkc8moQ_OwWVZK2TpuWayp17GGjMbXF4_KNSbFay7Wl9EaR-N1EHVAA4Q6CpVaTEYYzrz2tv9UNND-Fi6edlQrIsAgxmbcSqGjd-hC8fHypi1ld-JRYPW1cxzIMSmlwvdS3fTzn-WAwGgBcJqwBupJK1hPeJykC6lXiAxV2S3ZerPLmxKoV40pagBXmPA0bdGw52uGNpAhUrHjgKbfffqGVKlfyaCoyVX9I-CzABXyFpQwM7e1ZGYNvKis_06dSKiF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز هیچکس نفهمیده چرا زبون ویتینیا آبیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90814" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تهیه کننده برنامه پاورقی:
خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90813" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH7vz_TPnPhWkq3GJXcIc8boXkGekdDgNcZ_pO_fr_-xsTnLrKQUHkxOoUKN3N0UyzG_WNOo_HxF31bPi2k6avRNRuv79ZsGxugZK8wOA8yzo6Yfcl2uiM_-88eZB3aqCjYdE_O9ug_e5uHyfy5AFUdYxMUQJEgRVnG9TP37ZuZe_ytzB33XhP8pVMGDKHPKSJZoWQVtdRpN_8kveEu8yEqG9mtI28qduvIYKqbkJ3IhtB3ALfh0kTrv1HKfG-ceM4B4mT5HIGGPRtI0LPDVDBMmvC7S0GcG20O4nU4wl1q380A6UrO7BAr-9IAoDVkIL6TpSb8YZ_h_3N02B9VvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90810" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhgVnkqPGcCnp5AzxjzVOPqzuKy1G5Z9pef5j_PhauGx1stCSUTTCO5h6StPc1LYZM2UadY9U0Tg-nFtGnkrxSSsM84vKcWEKlPkGix4GqTLI_GvnBRklh_UILkwFNZiONWo31XRg98f6kcUAZ3UQHJ5vZRIB8dI6lAoDiDO3qPRrqgsUPML-D7hZmgmrTk-XQGoULejEE8GIrJsANwpgwk7wsUlcxWkj3Sac2G0SeMVJ2JnwuCaU_OUX_Lx4pcOE7q1JuFY9HX31X9ouCwPSMfRguGrDb_vaynko8moZAkt-Oq9Ykun6jiah5_X2lT0XcSuXE3z6TFdrvX6UKPINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل کمپ ۴۸ تیم حاضر در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90809" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcV_rRAlvlLadpDDNcxLnrU1kgDL9Ek3MVqAKFT1dIB6ovSUnl9Cz2c4BWCyNLoO09cL6PlWJsh1H3UlzH07vpU48AD8zLyZlDke3l4VWfDbaks3OJCumkLv4AOLdPoZDEJuFtchsJMVhCXnDTwSbW5M3UZF0SVqNekFhMESKguXup-fvqe3FHnB9bON4iUuV25PW73-c9JtRG7JsKeLQTkedrw6_cNT7w2yl_Ze3bRUISKv9LAO4Nx-tjFEhsLtIJVxjbDoE52rvgqom1TyHT_BltGqW3RFQ0PDaZ-jq4L4zFFuv99G4brhdHrIHfV7Bf8NKCXD6y4qGxdNrKe74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی و ثابت تیم اردشیر تو جام جهانی طبق گفته رسانه ها:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90808" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QauogZS-Xvh9FNoqYympzijq0pV6mRFJ4cMAwtO8k8uWpCf3Tb7v1Xxdmjo428nLbMXT5ETbonernAr4IS1YDNGV6HwABmxACnE-dQhA_ENeoo7OnhrDj9VyvyXosT17a3fdFCIsAit1KoemMxugSeRxOPRdfwQgFESQgt9apMXijnxBBcd-CRL-R2Q5eg6p_vWiil6-NKgqDYZ2WJnpFhIjFYmIotj1TeP4ab8WWN-32xdJDZ6_k8UN96hjN0-AhAMnjIdjo7P3mRwE5_84jk94erEHVIKj3-ILV-reXxlcU6Kgbqq60TA65UL6RxBssRFhADMWh53tDPdbjIgCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90807" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0kzUs7kk65RReaoMsL9t7DoLLMfN4ijyYIAaXHZs6pwsWs0i42fA_At0BWGxSX-o0lm0f74jynccKHwRbYB5yBn5Y_Daw9sCGaEJ-d2Uw1d1p69K1jhqFcxt2X325PbHNDnxP38AUM5PYE35yxvX1LGelLwQC4fzQYdj0QmHNpBSl3mIGPfxSA-kb_aGvJq4hE6Vj_J2fjxsq2XGqQF_FmJK186dJa6dfWwiBpXldvBVvzUFWXigOV_sUuQNNfOBgR9e94p63htSLGykDcKI5stgoUIJ3IyYOkMEPKWq3xlqVSH0bQPIFGcalZkxQ4SVSv4Q-IzLs96c_IxAyd0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 مربی سابق چلسی که تو این جام جهانی هدایت تیمای مختلف رو به عهده دارن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90806" target="_blank">📅 17:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90805" target="_blank">📅 17:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pg2fQPf6tkQ_43mVSy5ix5JsHzZLRD-4PgLTKsmnIsw4-TmRnMSnWKE_CQnxu2ozTJ26ZJIt33vPU6nqNju05E6oGWCAAQnQIjkEnT5mK8WlaHX7evDybtEhOqPrlOCp1angXyQ2o_xriAVkJ9EV_IG5x9HBVG1gar-ZjbSINYPfFt-NWaktTmLPb4sJHLOkWEPV9xW57bjtqeukB1rOCVPVowZViizRFIvnIZtfGnWOlni3H2EYafLDDPUTdgsZUhgwCVKHJl5I3O1CMa6V6X6JSUyyJVF34ofAYayMk_2r3BLc7M1JQsJBewZPvBcQF_QrNHANS7uldkbZZzlpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدربزرگ هالند مثل سیبیه که از وسط نصفش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90804" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167838926a.mp4?token=OuNnhCCEnHGfrqZb81eNAeOSyCSAS3PUq68GO18jwoWzo5hJC3vHNgjNwPw8knF4SUJPOSg0J4asFEe2xCC1Mpte8eALS9Bi5K9g87Dnis20QWZnmhm5iTPJR9EWV33mPf0umjj2oB3mIU4vonqu97WDR8JpbKbTTlbBpx6TKHEvgE3jtN5U_T5JsSfcPAiXq48xinJ5v3Wvp5kjvZcVlL9BCuQncyacu75E_Tb6cFtMFwGmWgZVSGOe3dljc28rJgow1ar8cmCzJUBkCG83K9nPiQD_nDcry4jykZ0MIbOWYhW712AUYVWyfdO2QD0GpjWDg_mGtwlITzXE0kd1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167838926a.mp4?token=OuNnhCCEnHGfrqZb81eNAeOSyCSAS3PUq68GO18jwoWzo5hJC3vHNgjNwPw8knF4SUJPOSg0J4asFEe2xCC1Mpte8eALS9Bi5K9g87Dnis20QWZnmhm5iTPJR9EWV33mPf0umjj2oB3mIU4vonqu97WDR8JpbKbTTlbBpx6TKHEvgE3jtN5U_T5JsSfcPAiXq48xinJ5v3Wvp5kjvZcVlL9BCuQncyacu75E_Tb6cFtMFwGmWgZVSGOe3dljc28rJgow1ar8cmCzJUBkCG83K9nPiQD_nDcry4jykZ0MIbOWYhW712AUYVWyfdO2QD0GpjWDg_mGtwlITzXE0kd1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش پسر مارسلو با رفقاش به یاد پدر
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90803" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e389c70190.mp4?token=mUdEzdaayb2HRNVqqZ7WQ-54oav53ZS5K3Vzubvq-ZdTqR2qDq5E5fOnl841eDE_MCKlu5G8ZS0qA4SAgGOwbEioL1cuxmuWmMcLt3g38z7ERIHBNsnx87y2vJi5mE_oNTfMavhaEMqlXqgcSQGgx7tPTa3PCR9TQjALV7cEAw3fCIfj-DflaMpjzFWpLGJ3VpvNsTLNsBGqKkIE38Ggn8bTZHEtkVKFJXJD5_gWRlpMpfJis0zv0WkIEWVWUmM0WYQ8aEdIBnQp9ddvoY29fE0CaqOxU6-NWj8sLMB321Sk9v1WfwG9gzI91NbGWanl93QpicGek7MBReFSViNsOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e389c70190.mp4?token=mUdEzdaayb2HRNVqqZ7WQ-54oav53ZS5K3Vzubvq-ZdTqR2qDq5E5fOnl841eDE_MCKlu5G8ZS0qA4SAgGOwbEioL1cuxmuWmMcLt3g38z7ERIHBNsnx87y2vJi5mE_oNTfMavhaEMqlXqgcSQGgx7tPTa3PCR9TQjALV7cEAw3fCIfj-DflaMpjzFWpLGJ3VpvNsTLNsBGqKkIE38Ggn8bTZHEtkVKFJXJD5_gWRlpMpfJis0zv0WkIEWVWUmM0WYQ8aEdIBnQp9ddvoY29fE0CaqOxU6-NWj8sLMB321Sk9v1WfwG9gzI91NbGWanl93QpicGek7MBReFSViNsOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
کاش برمیگشتیم به این دوران و این بازی و کلی هیجان و خیال آسوده فوتبال دیدن...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90802" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=T4fiN_ig0DOTeuorVrVb9hUgU6n2-n5Ko2GI2jhOkMw3H9WoiS4r3FenyARTDkTlOeHOVXsAxlTlUzvZI4Sjv-LRZwNU-zuBTSSxzxc4NqnRZqXkUuYJuo4f79H5aF5eIL_k6OtmPOhf5juOQ9C00xNpvjyBR4zIP_APxF7M24a5rIvuD1FcR2MV5t5lZV_YREqmV8NRU2J4FM3NI7kI-OXp0T_x78u8m-Ep8JGHn7yGTYPKQ0VOXAj-vJIcnXYaWZ6vuucDCGHIu9z-d9QsxCh71z5O5ep0Bz7zmL7YFZXbl2djGHQA2Qv_6kLQerKUQ50hJmWWBwl6ebIs1Dg_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=T4fiN_ig0DOTeuorVrVb9hUgU6n2-n5Ko2GI2jhOkMw3H9WoiS4r3FenyARTDkTlOeHOVXsAxlTlUzvZI4Sjv-LRZwNU-zuBTSSxzxc4NqnRZqXkUuYJuo4f79H5aF5eIL_k6OtmPOhf5juOQ9C00xNpvjyBR4zIP_APxF7M24a5rIvuD1FcR2MV5t5lZV_YREqmV8NRU2J4FM3NI7kI-OXp0T_x78u8m-Ep8JGHn7yGTYPKQ0VOXAj-vJIcnXYaWZ6vuucDCGHIu9z-d9QsxCh71z5O5ep0Bz7zmL7YFZXbl2djGHQA2Qv_6kLQerKUQ50hJmWWBwl6ebIs1Dg_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم آسیا موقع دیدن جام‌جهانی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90801" target="_blank">📅 16:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke3Tn2Av00gQRAu__SvhYtx8fPJzfPOeIJdc0BiezJzIXPNg-YFAy6xOrTUVLHoX-iwbrUbJSWAC4aNwtfz8YSgujEOq13ZxG-E_28tccMKnkBthJRZP1iUW2PnqUXfcZgJWnUo3de5ASAPb0FT7lQbelOEqOs-N4oxpjfuavWv4TRSF7b7mPP9F0QJ6LSlVrBHs0Lih4dJdhOll-vHoV-OZeal7w0jrC0rEMHGdQgeLf-FoZ98yWuCcySU05ajraXruuJDgZ6Td0f30VprVW-Smo-B3bS075JqwdK8FBAZQYpa8TWWpPi1QTKKHrqno02MaJQmyKT4qwSfsg47OjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ایده 48 تیمه کردن جام جهانی واقعا مسخره بود؛ فک کن سه روز اول اینقدر بازی حساسی نداریم که باید 4.30 صبح پاشی آمریکا-پاراگوئه ببینی:)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90800" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=R7IulA0EbV4GaU47jPt-_iS3GMeyi7nWmAHKOLO6_44jZMpM2TQ4Gtv25ZHvq6YmgP_Ew3SumsgCbHoawyUQxwAQkuGd-sc_LjI_ZiGmMGaKEU_QXw-uW9dmPzMytP7tDbvwvTmyV8WI8plGcOVJwDwlvowe6k9_L9jzO8rITwVCS9zkrio6EFtdypLAo-sJUNTICW2-cVyvGauLBLk_7wDyBZA-qQ5CB6RSF5z107XgeYeWrBXxluCSK3peW2aHypbzcK5wcrha-0HaCIygfYnys1nlOrno1E7CoX_DqaL9gfuT4UXvclwCWNg3Lg4kPhnNheQT5MIvE8lAKcIIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=R7IulA0EbV4GaU47jPt-_iS3GMeyi7nWmAHKOLO6_44jZMpM2TQ4Gtv25ZHvq6YmgP_Ew3SumsgCbHoawyUQxwAQkuGd-sc_LjI_ZiGmMGaKEU_QXw-uW9dmPzMytP7tDbvwvTmyV8WI8plGcOVJwDwlvowe6k9_L9jzO8rITwVCS9zkrio6EFtdypLAo-sJUNTICW2-cVyvGauLBLk_7wDyBZA-qQ5CB6RSF5z107XgeYeWrBXxluCSK3peW2aHypbzcK5wcrha-0HaCIygfYnys1nlOrno1E7CoX_DqaL9gfuT4UXvclwCWNg3Lg4kPhnNheQT5MIvE8lAKcIIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروز قربانی: عاشق تتلو ام و آهنگاشو گوش میدم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90799" target="_blank">📅 15:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkjqonmZFwmYvvl48uEPHpeQFFro6XtI2PmNPotW6ClQSjX8ILvh1ybjZna2NBiEb9RDZjSDsWZv6ydU5QdVO5K9sS6n4sigq7A5_R_-16QdC_IDF0kHDl3FmUf9Z70BvCopIZjjMBHvWDMywP3PKgzKHfw1mbKIsGzM9iXKUByGRWuzMpx-5D-myV44-ckDYM6CgXOR-vfJq2tp9sCB0DojmEmWXJ5dKJ9DqERviExWVDn_MMNrbl8l2G5bNH5nL1U7LKFRpyEEJr5qUQfqOZUXPOUxkZXRw3KvOpYX1pu44cBxAAgn6ywRyBOLFQGhbt805bLUaxLGERZyYHSJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: افتخار دیدار با آیت‌الله خامنه‌ای را نداشته‌ام. به نظر می‌رسد که ما با آیت‌الله رابطه خوبی داریم و دوست دارم او را ملاقات کنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90798" target="_blank">📅 15:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cM-rm6-JwvobbTaVtLkOEkalB29OA7Ce79tyddbV6pvUEyHptzQLqXNkZZlG5M2ZlRtdlZr8gW_lIGi5zTYONbBydOtT0OSL1WyTdVGPnruQ4Sj3_y5hstq9jKTqAvCQBPe1We22dn0KCRbw0whIlc73RppoLzpKHhj-8dg9Sel_xWkZr8tk0H4C4oH6Ke5jn2nuuLU7UgncDJ4V0wN1y7ou80xdJ0l1UIWQbfh0x_mBOy_DeNqO5XIImkDGdG4RdJ5hJxb8-Ab5fUZlkpC9um8RIWhwt1en9pe9aACHYoG5dEsMqmC12ky3SST4rPTzeU7edMaGaFJVZMH8UB5xNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=cM-rm6-JwvobbTaVtLkOEkalB29OA7Ce79tyddbV6pvUEyHptzQLqXNkZZlG5M2ZlRtdlZr8gW_lIGi5zTYONbBydOtT0OSL1WyTdVGPnruQ4Sj3_y5hstq9jKTqAvCQBPe1We22dn0KCRbw0whIlc73RppoLzpKHhj-8dg9Sel_xWkZr8tk0H4C4oH6Ke5jn2nuuLU7UgncDJ4V0wN1y7ou80xdJ0l1UIWQbfh0x_mBOy_DeNqO5XIImkDGdG4RdJ5hJxb8-Ab5fUZlkpC9um8RIWhwt1en9pe9aACHYoG5dEsMqmC12ky3SST4rPTzeU7edMaGaFJVZMH8UB5xNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردها اینجوری بعد باخت خنده و بعد برد گریه میکنن..
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90797" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmXx3LC-Z0YFzVf60C_wOgdIVgICDw4el-TTKgQzhSZmC1mi8rCKuFakKG5KchrcFZSv6KJrAFc3WckkbqvHVHhDlp9nL4GVKiruBI68QWDPggFbvvZKcOLuFDsgCJ4F82L6UW5_1tquW26yfyntmDbbBnXh7KcepgmnnjV6gBU5M6E_eC8YWdITlaL6yI2GVgSFteWiKO78l3OaRuES_9egs3-J1ZFxo8c90lLvBS_2pUZDhmX-s5KyVnN7JRn_-1iYaoF9yr41MoIbsJ2AV_i4Rjej3T6kwx8aOQ-kqPrrPYFYeWR3_oo5AH28eLhYYFmt1uQi9K870V1xP7am4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🏆
سامورایی‌های شگفتی‌ساز که طی چند سال اخیر حداقل یکبار تیم‌های مطرح دنیا رو شکست دادن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90796" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال: امشب اعلام خواهم کرد که یک ستاره جهانی درجه یک را جذب کرده‌ایم. من به طور رسمی یک سند قانونی الزام‌آور امضا خواهم کرد که تضمین می‌کند قرارداد با او را نهایی خواهم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90795" target="_blank">📅 14:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=hJFaWpyH9DytnLDSX2XDm3yVek_gb7GwZaTOo7-5weDW5pxY8VTIHSwOJz4VSJm4FKq8k2iq5AJL8rkFCS7NGrdYDjXf5utGKnUhlrCfEkGLmgkCZ1zZTIZ8XhhL5YC0gm5zblijuacvuMhlsC-lqWTSQMTKyACtGkRYDUstgDMroLy9E8t_tvECVxbtTmM7ytwoGqXLExeFPpaum3Oz3hGXkA-BA5yAB4G4Dyy0PqmTTzid_EW_STJK5ssp76v4xjPamBECi4Ud8Vmh5GrcZy29vCgxrNBV-w7LmWHFWZPhI13KA0FIXlTM97oEJpZSeldzy-YhDhjtEnBhStdzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=hJFaWpyH9DytnLDSX2XDm3yVek_gb7GwZaTOo7-5weDW5pxY8VTIHSwOJz4VSJm4FKq8k2iq5AJL8rkFCS7NGrdYDjXf5utGKnUhlrCfEkGLmgkCZ1zZTIZ8XhhL5YC0gm5zblijuacvuMhlsC-lqWTSQMTKyACtGkRYDUstgDMroLy9E8t_tvECVxbtTmM7ytwoGqXLExeFPpaum3Oz3hGXkA-BA5yAB4G4Dyy0PqmTTzid_EW_STJK5ssp76v4xjPamBECi4Ud8Vmh5GrcZy29vCgxrNBV-w7LmWHFWZPhI13KA0FIXlTM97oEJpZSeldzy-YhDhjtEnBhStdzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که از هم‌باشگاهی هم شانس نیاوردی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90794" target="_blank">📅 14:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476676c77a.mp4?token=nAN0z-uh6KkwlznQShepN6yhN99Ui7SH6I6j-hm5dwwchQAjdjddfugoQIVO1li7yGzXF5HgFZGX1xvXAqUK58HIlerAK0p9w_Q0W3AhJZXKEz0UCX1iiEeIR1ifUAtyovIVJUYVPXjBsmMBvsC14WJ5LXKtRDnqjGiGtq8aBGtZiMEAE4_pg5KWGl7DCvFPqQgJQioCXdf0sH0bagM6pKVNEYry-NVm_lT8Sx64UBt0LScTFAcvk3oW-MAsS8uRvb9sStde_Ui3cUdHxf2tsPOmZLCPNcDreP62iPzbVn82Cmy7jgLpjOxONAAnuZTYagIRSJT16cXbkbKZz6aJUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476676c77a.mp4?token=nAN0z-uh6KkwlznQShepN6yhN99Ui7SH6I6j-hm5dwwchQAjdjddfugoQIVO1li7yGzXF5HgFZGX1xvXAqUK58HIlerAK0p9w_Q0W3AhJZXKEz0UCX1iiEeIR1ifUAtyovIVJUYVPXjBsmMBvsC14WJ5LXKtRDnqjGiGtq8aBGtZiMEAE4_pg5KWGl7DCvFPqQgJQioCXdf0sH0bagM6pKVNEYry-NVm_lT8Sx64UBt0LScTFAcvk3oW-MAsS8uRvb9sStde_Ui3cUdHxf2tsPOmZLCPNcDreP62iPzbVn82Cmy7jgLpjOxONAAnuZTYagIRSJT16cXbkbKZz6aJUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
🔥
Colombia
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90793" target="_blank">📅 14:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90792" target="_blank">📅 14:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=IflbWpKn1avtouPlPhUTyWods-eiIyIqooqhnIAUYKpICgfP9SwPIWuE9MiYvj5H5XFfA_7SkhBeOhOgsxGUKmfCVmaaWk81wxHXWHeW95Yed4Pa8-c3qv-Ee0bCTIuq7xGaUWPoq6A4XbJ5qdJZ3BYlSNAOAG0Xy42Vb3Gm-Rl87-8KkyeIZuqalmXKVk7UkS6hUJ-IkSnOKRflcex0F-1_QYy8KwGEHSXpLkRGnT5NGoNhgSZlmxAIEr7pAo14N3Ro4DK0_VttwrX7xtvxrpHqDiFWCaI_DwXZ53NtCNTebeJ3wreZPT681agKi56swHpK6ERXouM7tMSNxad2vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9285a340b.mp4?token=IflbWpKn1avtouPlPhUTyWods-eiIyIqooqhnIAUYKpICgfP9SwPIWuE9MiYvj5H5XFfA_7SkhBeOhOgsxGUKmfCVmaaWk81wxHXWHeW95Yed4Pa8-c3qv-Ee0bCTIuq7xGaUWPoq6A4XbJ5qdJZ3BYlSNAOAG0Xy42Vb3Gm-Rl87-8KkyeIZuqalmXKVk7UkS6hUJ-IkSnOKRflcex0F-1_QYy8KwGEHSXpLkRGnT5NGoNhgSZlmxAIEr7pAo14N3Ro4DK0_VttwrX7xtvxrpHqDiFWCaI_DwXZ53NtCNTebeJ3wreZPT681agKi56swHpK6ERXouM7tMSNxad2vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات تابستونی دوستان در بلاد کفر
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90791" target="_blank">📅 13:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: احتمال داره بزودی با آیت‌الله دیدار و ملاقات داشته باشم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90790" target="_blank">📅 13:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLT4FfG7N7UjLuxwvIyFalyUkyYJsioC0n29mTrUB3QblkP8b_8PNmM_SoBFc3bF45zZMZU9UVS3z-2knEdNOH6g458XJrnYAWxvX9P-a--u4eQZv4O4bCBA2jxTErQs3zfYQL1TgYMr_Czles4gf5Eibz7oLDLD5XKn3L208vs5U9oUxmB5kSmpS-EYxNQGBZOntQWNuEvWAyTAyMWCprZV-zb8L_3UN4knbHJd_uaSff1vDifeO_1vEqe6idALz3g4sy4QGDbzRb7hdS1yqcOAH-a1hu39ay7SYxJhZiQgjsqH7FpnkDWlwN6AZqIii8EbtgVvLCT1r7W_nZL1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90789" target="_blank">📅 13:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idz9mHpSO8qBnidJpCXcOyEu9VIv3etiR6TdSW3EyvwCxTMeOOfoyoOvcBAZNTfShniVjRLgrhju1SMfu4mte5WlmuhRnf6mNmMCzm6x3TE0QDELMCg0OdD6JI5MvEcypDHIsIZzIn68aR7Z7V4ZvmMjNWTAojaz88kGgrUIyEvkgICAEYmZwR4-RwdG3jmjGu8RwZ4vOJS6f3IuCrFlPluXy6V8YL-gqY8y-5XUbt7lBuPG18GOaH-ip9Lbp4J7WPQRe49Mk8kNt5nOcQqHstLSkCPaLNz_7ttedId-RtyBcYQle-JqXa3G1B6JS5Au_4zj67m0c2jtPKGTpf8jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
منچستر سیتی در صدر تیم‌های با بیشترین تعداد بازیکن در جام جهانی
2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90788" target="_blank">📅 13:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_Fq8Pe2XbbgjjVa_d0iJy01UQ7e6scI_TgTQZ-_lCMj80lB2yfTDsd5nj9nmypkFFVauEDVXROPrVWapnBpNkLnV-HWzqt9TKSrl2wVoUGPUgceqZs095Hjoh1yKxZ6tQVaqtchhtEc3p2bw7c0IG-FD3q6CupcCCGoPgDpEGMYquSkAPDIug3yGNt3xKqDCp6ymW-h5aoKIB9PlziBK4f1ICe8JE_dcf3NSz7R31XzZhP5OydZOg5iA_1EX3s9EIGuwFCtpOX2Es3ZTuJapW3O9OQOCUauBe4HL_kJ8itKvceEfcR3Ugju17o-8ftEZam39zppxrfFnrYSRZI9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام جهانی واقعا برامون غم انگیزه..
پایان نسلی پر از اسطوره و پر از خاطره
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90787" target="_blank">📅 13:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90786" target="_blank">📅 13:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_sw91yetFGwa2-r7FDM466Qz9uK-VgweuBNeA_zVfaEi-CGihfrG9mVb32_qGP7R6_dLoEb4cFRsovoCwc-ATSK1sNqnRUplYDu46AERU9fFhqm_MHzL-h5pMiUHz-eEihRxOhxRTnUd9kENYpXnF-Q1L4w1oNGMYxUK_k8E1GMsT_6KEMiimN1X9qMgrKYX67zrBAuZJtBxTTMk46oxXJ4_gL-jn6XBUwq369Yer561n9pvO2zWcdKEasMWpxVxDv3dAbOHwp8cvZMZKh8THL7ndcDeSfydKR5vIWsky1aEv5chbAK4fqxK76jjI915YYm1li5CiTaqu95pbJS1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فووووووری
؛ ژوزه مورینیو خواستار عقد قرارداد با گواردیول شده‌است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90785" target="_blank">📅 13:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnPmH8E-8BSHKwfAv7MTj_wS5nnwQBsgseH7W86uajH7hZPmmhme-AMCW7098ewn6Fw6qHAQUlxpuLpNBbmaJpdCrgsr3Q4ZMBFUWZxTw5bbWhFIWaGi_aG4lC3MpLODCBDdkXZ-O32qjAE4NQ-ZzKe2LJED8bQe14aAMI4wFtBkQ2yEObLzzl0VR56bunFBpjhfM88whrp_iv5X9zP1u6Gn4L5Qpd8M8AWZxEwvalvhTvXp4779mxwvrg-qF_74MWGcjnVArAgG0po4Iv23V0AchXrCOYRhtqceolSbJtgmJ_-vJ1LDJlzsZfnvXrouQ7k8pu1T-0aE03GauQgYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستام وقتی میخوان تولدمو تبریک بگن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90784" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=n0fqa1aeTjkcFFlx6FVVMvpLa5PNrDnOKJFHz0NRP5PDwv9AY4IRNzohtEBuWHTAWJAz47AiepDuqbgt47mafMVguPvkU9mfPm2z2FTPKYF_6GUrhEjMSi1Z_1bzOq4yFtPPmpe2aFyhDYN6wmTXVnvM8DSHQ0Av6pDKddKLwDqbRtiscUeDouhLeuytXne5d_opSMD9tB8B1jHabo9XP8-lROIdPv1ck3IkrXnoaS8DfgTpVbPoO9RB3l19yT8V0v1QG52lpJe0ZaRbz9Ka8RYZFrtqvjrs1GoyPmvHIYGMLAxlInn8V_upEe8n49K4t0O7WKWxLuPIPzAJRywNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8caed85c.mp4?token=n0fqa1aeTjkcFFlx6FVVMvpLa5PNrDnOKJFHz0NRP5PDwv9AY4IRNzohtEBuWHTAWJAz47AiepDuqbgt47mafMVguPvkU9mfPm2z2FTPKYF_6GUrhEjMSi1Z_1bzOq4yFtPPmpe2aFyhDYN6wmTXVnvM8DSHQ0Av6pDKddKLwDqbRtiscUeDouhLeuytXne5d_opSMD9tB8B1jHabo9XP8-lROIdPv1ck3IkrXnoaS8DfgTpVbPoO9RB3l19yT8V0v1QG52lpJe0ZaRbz9Ka8RYZFrtqvjrs1GoyPmvHIYGMLAxlInn8V_upEe8n49K4t0O7WKWxLuPIPzAJRywNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇫🇷
تنها تیم‌ملی که تیم‌ملی نیست:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90783" target="_blank">📅 12:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5gQAnd3-_bOg3HNJVkqgvbMK0y-pRqfctoyR01_Zorg2NzL6K8V02DGywn_CnvOHxh7jIX8dVRyV4k63KgyhYTzeoOdcAQ3zxn6x-N6z_KYS1W9huxLFjZCoPjGk2X-Bj4YM8SbxP9ciw2UC-P8k-cWoQhugR3eaL-YIoZUBCMoP_suQFKGsTGqFcZtc357cKPZZ4ak5qAVXRFws1njsAvDwuTFX6wDAcvf_cZAsZYGE2WoOSitjyEcXPPDUFw4AmsbI34kQytY4Lv-FyBZb-J4TCEHNhgJOmM5LX16cVt1e9XjUtd8yu6DlNFC_NdgW2bKbcivNNVyAtrsqctP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پیراهن اول رئال مادرید برای فصل 27_2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90782" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=OY0SrQB6YLn65L2LrmdAfcZs8rDUCTlGRG9TK4sZxomXlSeY4Dv7zNRvd-dhy3xxdoM9BXsluzm0v-SSMExSA2gB9r2fHrj1xYpCYOIRS_lWnYn750GOh99x9Mp2QDpf4mkNJjNp6BRc1Ytv-1CtuYc6iC6PoSjVmkBz3U3z-blrHR-TNR6VD9wL9TvxfcLA__X0G8wizGg-ByYfxP0KhRbFqwiwm9XLovKfSuakvGQPaWAfJ4rQ0oeztvXCp6YGhYRhP1-V86WYbrmiAcizyk2QNiaDBPZ7z48iV572ODNnKctYap3fpTvHZbu68clZGPmFZxrBT9-APeGKHt_4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9a85cfef.mp4?token=OY0SrQB6YLn65L2LrmdAfcZs8rDUCTlGRG9TK4sZxomXlSeY4Dv7zNRvd-dhy3xxdoM9BXsluzm0v-SSMExSA2gB9r2fHrj1xYpCYOIRS_lWnYn750GOh99x9Mp2QDpf4mkNJjNp6BRc1Ytv-1CtuYc6iC6PoSjVmkBz3U3z-blrHR-TNR6VD9wL9TvxfcLA__X0G8wizGg-ByYfxP0KhRbFqwiwm9XLovKfSuakvGQPaWAfJ4rQ0oeztvXCp6YGhYRhP1-V86WYbrmiAcizyk2QNiaDBPZ7z48iV572ODNnKctYap3fpTvHZbu68clZGPmFZxrBT9-APeGKHt_4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇹🇳
این دختره که می‌بینید از بیکاری زده به سرش و رو قهرمانی ترکیه با شانس یک درصد، تو جام‌جهانی بیش از ۵ هزار دلار شرط بسته
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90781" target="_blank">📅 12:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=Bn_4-Db0TqmObkGj1iSkt7hclVghpK9hVyHD6t8ltEAykZtgN37v6vNRo1t1rlyfxBU0hB2Th2wjkipdpqPND2dLtu7HDrX9gPsnEF5w2r156KQfJ3zQ9HZmr8mMUhshv4CnrDtlbWDhlhiCtqi2Q3SLuew4D0qXo98lBNBBVERJIGghxlvPtDmcwitPGbEO2WyasO4uubhfzGdpu3MvqJLBxFGDBeEDjCZ0tokXYLP52VXpWyhrMUzCYGTtYXM_rWVsJpw4Nb805YPt_yCQKhTwBOBp1GrODbtfzgA9b6j4dVsi1iDbeOP5Arl3H34dKOHUCfukruRAkJ9gxLcy-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0dddef5c.mp4?token=Bn_4-Db0TqmObkGj1iSkt7hclVghpK9hVyHD6t8ltEAykZtgN37v6vNRo1t1rlyfxBU0hB2Th2wjkipdpqPND2dLtu7HDrX9gPsnEF5w2r156KQfJ3zQ9HZmr8mMUhshv4CnrDtlbWDhlhiCtqi2Q3SLuew4D0qXo98lBNBBVERJIGghxlvPtDmcwitPGbEO2WyasO4uubhfzGdpu3MvqJLBxFGDBeEDjCZ0tokXYLP52VXpWyhrMUzCYGTtYXM_rWVsJpw4Nb805YPt_yCQKhTwBOBp1GrODbtfzgA9b6j4dVsi1iDbeOP5Arl3H34dKOHUCfukruRAkJ9gxLcy-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بسوزه پدر هوش‌مصنوعی که مردمو از راه به در کرده
😊
🎧
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90780" target="_blank">📅 11:50 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
