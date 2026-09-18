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
<img src="https://cdn4.telesco.pe/file/Z_iIBA8Tzs3ynxtEJINwZHW3sR23xg6IbiNQDaQMzXb4QxYXHmm8wJVkEzvpC-pP4V4lu2Yb6BdAE3dK9oj-o4Ev9VqIIeT2Rar_nRGwNrZcY3wy_53c6ZcHOvi7OogE2mOboFTrcq6d0lm8DZcjPpFTchce3l0PFkbO-lUVH37zMTlKZwYoGXYifDipzX4cRnB8fRqc6_DIxakMcsMbFCyZd4DcqNtKyKK9RxoqtPSQJ6UJnS9AnS_CAmS0xI2rZmTon3alfwUnjNKT2wczm8I9iodMoSoTXRBm819UrVu6m07qjq6TCDQO5jVfw_QXX8Ug-jwSPJPv99PNRNongQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 11:00:35</div>
<hr>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvJ7lEUy5aPTx4GcFEW4LSssWKV9S-vKbB5oDXdsgVMkCScNKBbLmgldWqmiJb8nhe0Rqt7-I5zRlcZXl2RtO46Y2rfNF4rNOKXrvJ7J8E5Xwcig97nFEc2S4OFGBDk9-Jla571mGbtiFG4m6SXrVAfCRlbezfmlwx7TZAdPiaPtIQrbpdYIgy6_AiIZjJNEeCCzLl_vToPfeymi6B4E6xsPfESzNaXpLjodnu9i40J9FMS2_fM5vyIHzdnKUHVCiD1Ol1JshFJ_d-awPVNPvxOwuJvLNjjCeJGQFp2-5fN5sgoNkk26h5jFTMKFunW0n6ilBKklkX5cAAc_SCJZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/naya_foriraq/90857" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/naya_foriraq/90856" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">إعلام العدو: الشاباك والشرطة أوقفا مواطنًا عربيًا إسرائيليًا من سكان مجد الكروم للاشتباه بارتكابه مخالفات أمنية تتعلق بالتواصل مع عميل أجنبي من لبنان.</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/naya_foriraq/90855" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مشاهد تظهر إقتحام وزير الأمن القومي الصهيوني "بن غفير" لحائط البراق غربي المسجد الأقصى الليلة الماضية، حيث أدى طقوساً تلمودية برفقة عشرات المستوطنين الصهاينة.</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/naya_foriraq/90854" target="_blank">📅 10:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حضور الرئيس الإيراني مسعود بزشكيان في مناورات "فدائيون إيران" العسكرية بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/90853" target="_blank">📅 10:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تقيم الجمهورية الإسلامية الإيرانية مناورات "فدائيين إيران" وبحضور 313 ألف عنصر في العاصمة طهران وبشعار "لبیک یا خامنئي".</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/90850" target="_blank">📅 09:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/90849" target="_blank">📅 08:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=T4tVtOV-kUD01l1bxtUYXpnMKnB5Mtvz8CmQ3wJK4E6i94RGeABdGQ2wv5uiXBCcJm78eTE1-cB8h4jayfMSVz8JVuEtHhTaGyZ-ia_zR5SuyMRyglu_s4VPBlQO3PL-bFKnK5GqPZGMarE2qhs5bCyNEDbRp8R4BYhTea_wsZsWBgIBGXg_NxNqvlASOaqdxmH7ywTy4tDYFe5WMPy02CjmL2j6veNR1F91cHtQJGyEdNBnLthzLu9UxlyBzE92b9AS4lzqMwT1b5piRPn-SoBkyliF5uDFPKdBYWN2XvD6BFdPKRMZsuyYLkJ59KyN79o6dFBbXQct21hzhboTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=T4tVtOV-kUD01l1bxtUYXpnMKnB5Mtvz8CmQ3wJK4E6i94RGeABdGQ2wv5uiXBCcJm78eTE1-cB8h4jayfMSVz8JVuEtHhTaGyZ-ia_zR5SuyMRyglu_s4VPBlQO3PL-bFKnK5GqPZGMarE2qhs5bCyNEDbRp8R4BYhTea_wsZsWBgIBGXg_NxNqvlASOaqdxmH7ywTy4tDYFe5WMPy02CjmL2j6veNR1F91cHtQJGyEdNBnLthzLu9UxlyBzE92b9AS4lzqMwT1b5piRPn-SoBkyliF5uDFPKdBYWN2XvD6BFdPKRMZsuyYLkJ59KyN79o6dFBbXQct21hzhboTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إيران تريد عقد صفقة؛ لكنها ليست مستعدة، في رأيي. إما أن نعقد صفقة جيدة، أو لن نعقد صفقة على الإطلاق."</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90848" target="_blank">📅 02:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نايا - NAYA
pinned «
إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/90847" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90846" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تفعيل الدفاعات الجوية في مدينة جدة السعودية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90845" target="_blank">📅 01:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwcJ8ddnCn4fTkBEOR6Q_E_zY2hVqWBEFGxpGnUvte1sLAo7yYqlES8D1rdTKbQl1iM6OoB4Af7bzJfH8ftJlKbUgZjtsfaP30UiS4Ef1ZwPH5JeX6c5Kea3HuzAaL5T6071xwvqXvEJGct72RHL6_WyHO0LeLkEvTDGTfPMjIQzYCeOp1QdLxtKqsXFiJCaYXJnoOwd62SkUfaG3TIO2hV-FBE3WdLq_ngZ4OBVpm9D2boRoPTlJyixX6p1sb-oRn4OO93lkVcGiaXTiDyHt7ELWiHBIZ5LU4atabgshpG9L2BU4whWVWrPs-Jiyw4plAb6Wb38zyTHbz3ID7aLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
الانسحاب المذل للقوات الأمريكية من محافظات اقليم كوردستان العراق مروراً بمدينة البغدادي بأتجاه سريع الأنبار الأردن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90844" target="_blank">📅 01:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بين ياسر المالكي وقاسم عطا المكصوصي من سيختار تيار الحكمة الوطني وزيرا للداخلية العراقية ؟</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/90843" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وزارة الدفاع الأمريكية : خلال فترة ترامب، تدرس خططًا لسحب الطائرات والسفن والأسلحة وأكثر من 25 ألف جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90842" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un4ADKrh1gy715XKacikjVf0vPNoV_JBhAin09fEb4ohCciwD_B_jc1tjQlrIkK6v6n7BE9YFIUTiEP0dfbVDTtBdU5TAmZO9GfnQr_idESQZBzdMjPSahpFVDVHzPv7Jx0myDoKkcfwQ2oZWxeoJ2_p4U2H3SSIkrmxcomK2d774p4uNqMEwAgHqmzBMZ2CuwAJWdKKy4y_2l2MwnOX9zBmt9LjQ6J7gfSlNUncdbZEvsfJ9saRemHA58hvvNm6MQ6rFQiU9QSlca0usYXqzc7-cddOoqyaWyAwy4Bhq3Dfl8t1MHILjQ-__mzOi7UrSwq2YYVbeBRckCqdmE-WIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الصناعية لاندسات 8-9 الملتقطة اليوم أضرارًا إضافية محتملة في محطة أبها لتخزين النفط الخام جنوب غرب المملكة العربية السعودية، وذلك في أعقاب هجمات الحوثيين هذا الأسبوع. ويبدو أن ما تبقى من خزانات تخزين النفط في المحطة قد تعرض للهجوم والتدمير.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90841" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kByKmKegOk66liXDrcbXoMxKsIJjNmKtPzA6IdJmQ49kMVgEQxUz2Ripyf9-A0xNUBx-oDATYyavQfQOfev5ADsDmZE17OI-RlqgeL5ZceRS4rImmmEypOyqB8zpyac3DXano5qavXT0L_jUh9gaIhsE67_0AUHmk_kNWo8X37mnPHh_0_8MnYRXgz7S1vjCTaLStNLETGBL1aS0_wvBdy8GCr8ponjrW2une84e04VwbzPX0RsuvLHtICsgW1Y7H5N9MrcGcJPMXeikCPycD7WI4_aM0KHGg2uTGIMLt3PvA5y5mrExj2IZl3qbD8v5WnSP4FTaSgEOEDw5ldszEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
استهداف سفينة في مضيق هرمز</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90840" target="_blank">📅 23:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvnCW7WWFMX2D66MCLSNXIp-KoD5gFEDA9J2X_slYAp4ZCKT7p8Xo8Fats6lO7IAlCHJz8yPD-3aMHOgo8Lm8rkNGJ1ksvLygz0CSAAVYR2SgFJJzFvTxAU2eZSUO_NRGFwIB_ezBW_al_73Bh3EpvLFLECnX6FlmdYKEl_OIk-Pwynq6w28Nn8n-o2wkI2k5gb-R4wnBhb1ehe4LMBXhS9C7ad7bxgjnmodubHHpoDcfbQOoRmHcDBflUqVqNbajtzwrCt6Y41hsnVOMOcef2X4uuJn0LLfWwWWkOLnAU5oXAHIl_Gv3nbVhb3g5UaQG0PN3iBJbSqRF9qqPUQcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: ‏انتهى النظام الأحادي القطب الذي ينتزع فيه طرف واحد التنازلات بالقوة والإكراه. وقد رفضت الصين وروسيا، باستخدام حق النقض (الفيتو)، الاستغلال السياسي لمجلس الأمن، وأكدتا سيادة القانون. يجب علينا الدفاع عن التعددية؛ فالأحادية لا تخدم مصالح أحد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90839" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90838" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90837" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu6MtomqVP3RaLE7qKzugu1-UpA2LvxU87CT9InPNF7YwscGPCyR0EJS-VdCtC56B9GMD_6fQkaSGk2OlZv_wmF49jYZ9ocU3ek2BgsEtWhHiTmQOYPp1GRAsMb-zCOzLuaKEm8U8HNu57jivuEyWocW5OfBOIUiaJNfkhTsY0QK5MUjhUgjsgAPWKyL6Zc8zSVSbmA42ZhU-FxNebSyUCmVRb24vSmMy7aL4lvS2bIs5NnVSqx5MUJRi6BErvtj29xmEUYD2tS6BtaaEfTrf7on6l1hlXR2cfic-ih8621xsfAac2gRIoU32kByiBh_3pvKf3vafIRVO18dXXTlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
وردت أنباء أولية الآن عن تحطم طائرة من طراز إف-16 في مقاطعة بلير بولاية ميشيغان.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90836" target="_blank">📅 22:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
🇮🇷
الخارجية الاميركية:
واشنطن تمنح تأشيرات دخول لإيران لحضور اجتماعات الأمم المتحدة .</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90835" target="_blank">📅 22:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 37 غارة جوية بطائرات نوع "F15" أقلعت من قاعدة خميس مشيط الجوية واستهدفت محافظات تعز وحجة وخلفت شهداء وجرحى من المدنيين.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90834" target="_blank">📅 22:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
🇨🇳
حادث سير عنيف في محافظة ذي قار اصابة اكثر من ٨ افراد بينهم افراد من الجنسية الصينية.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90833" target="_blank">📅 22:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يغير على المدنيين في محافظة تعز.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90832" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇸🇦
المعارضة السعودية تنشر:
سَنْطِيح مَلْكُكُمْ وَكُلُّ حصونِكُمْ.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/90831" target="_blank">📅 21:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">امريكا تفرض عقوبات على منصة بتبانك للعملات الرقمية بتهمة العمل مع ايران
وعقوبات إضافية على كوبا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90830" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
‏الخارجية الأميركية: صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/90829" target="_blank">📅 21:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
إصابة سفينة الشحن التركية «ماريام إم» بمسيّرة روسية في قناة دلتا الدانوب داخل الأراضي الأوكرانية قرب الحدود الرومانية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90828" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QII8cjcyWw-0S4SueRWL-iauJLqQQin_1m85Ga38QVBiXEW58eGFrhmEplex_WeWa5bDagpjhbJPn93jfyDwaT1e8Y2BXKXETOhJ2qscWu7K0VlMopAEG3JFvj6pZvqJIGvXfJWokNogWRWuzurAChAkwl0thIhAr1r3OmH_AAOR5NSWNlLxhsYpajbpXCSivTgpusWt5Vb4XcmcbtzBgxxgIHvTGd9WhIYXBIfSlpeD8FJj1dJEJAI1cm1WXvwHVWBR4YpbYNIQoieGATSwi2F52iZQZKxGb-QMNUSe3eKg76Hkyn4vNJGA9zNDXBsTDYnDO41Re6UYxFO6AZ_MiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أخبار رائعة! بفضل القيادة الجريئة لصديقي كارول ناوروكي، رئيس بولندا، يتم إحراز تقدم كبير نحو إنشاء الولايات المتحدة.
قاعدة الجيش في بولندا. إذا حدث هذا، فسيتم الإعلان عن الموقع قريبا جدا. ستكون هذه خطوة تاريخية للولايات المتحدة العظمى. /التحالف البولندي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90827" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
🇸🇦
‏
الخارجية الأميركية:
صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90826" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL1VHqpXEEWCRfJl8wzAROTZp40qAaTpLbqUs0HLN5k7eTVP0YAImNVjveWuP0zIEsyRxF7O433hJE7s9wU1k4cAKzqtkIhoxcxkFhEUbsVvbgry2cw8jToh4s-vpKrJFEBTXx0MBk5tXPw3z9TGIilpZb_zfU0ZydYUk4tlEH-b0j-dN791n3rXQ9-iwFWTgrzyhNQOcMvTJ8wb8kVHKGYA6yhUZT1kA40ohERYnISjTCpB7Ggq7azMqUJDDw3Cinb3TqcnlCAzBcqTXwnhw56mX8QRJqyZwdF-ZyVnKPkgt8z_SDUnZVNOdtzDYSXnirFHGJ3oUEx0IaWrUe4Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
آیا ایمان لازم برای انجام این کار رو دارید؟
@Naya_Press</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90825" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇶
متحدث باسم الحكومة العراقية:
رئيس الوزراء سيذهب إلى الولايات المتحدة الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90824" target="_blank">📅 20:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران: لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90823" target="_blank">📅 20:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90822" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=HdPPGsLR8lBsDjzIb3didhuw3e7sAUe31714lSjyWB2ngMqnF_ljlhcfcN_d0Jpwr6J8Knm3qURjxDj69PmtL5GpKat1tb5GYsKvxnrsvDQHaj1US-FvpowZ4uvKPaCFmW4Bx5GAKCmPSU5qeuD_kPc469RN9zjsYVxGWXzdZXVgK-0hUdD-RQEy3TovTEqAu9VwZReeuDZL44RPPHSzdKYUS-9HbJHZ4dUmi2tUoGROpiqF9JmbOv3R86_78_MwLxQ3MIpilwCh0EXzTmb8CtBEOLhJNWRYScsGbvoc87FD8YgWJHO9in0RgTpml7H0nYuuFp4yD1kO2DmbfF6k4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=HdPPGsLR8lBsDjzIb3didhuw3e7sAUe31714lSjyWB2ngMqnF_ljlhcfcN_d0Jpwr6J8Knm3qURjxDj69PmtL5GpKat1tb5GYsKvxnrsvDQHaj1US-FvpowZ4uvKPaCFmW4Bx5GAKCmPSU5qeuD_kPc469RN9zjsYVxGWXzdZXVgK-0hUdD-RQEy3TovTEqAu9VwZReeuDZL44RPPHSzdKYUS-9HbJHZ4dUmi2tUoGROpiqF9JmbOv3R86_78_MwLxQ3MIpilwCh0EXzTmb8CtBEOLhJNWRYScsGbvoc87FD8YgWJHO9in0RgTpml7H0nYuuFp4yD1kO2DmbfF6k4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المندوب السوري في مجلس الأمن: إسرائيل قابلت رغبتنا في السلام والدبلوماسية بالقصف والتوغلات
القدس تنتظرنا يا اخوان</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90821" target="_blank">📅 20:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">إعلام صهيوني : إسقاط طائرة مسيرة تابعة لسلاح الجو الإسرائيلي في البحر قبالة شاطئ بالماتشيم</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90820" target="_blank">📅 20:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اندلاع حريق داخل مبنى وزارة الداخلية العراقية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90819" target="_blank">📅 20:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90818" target="_blank">📅 19:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQIjT3jByE-W3EKnrHIHhXTrQ4NtzKMTxTlOQ_AckAzsJymT5c-aR3fqD2BbF43xEl83id3Kzx9w55mW2V7J1B0KZfu-jQBd0pQBqamU0cszG0pu2RRbIr6rcRTMptHUrzWSOAwXPh3CM2jelLzYjjRuvsHGStQ4l7bMLAVdK-7kJFlTXU8EA6fQ9AZ1-2pOT5761Ls3emaGePOv-42uv5i-WJUv9a_nUIBhGipgoDQYc1IWmDf_I8fXV12d1Txnb9SjtD-fmmq5LpKbmbEMbuk4xqL3WyPgu4pXDEc3wPKx3A0BCdxN46dkMLWs7H8dFko6ZbYvWW3mUFPHi_FIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة معتدية قرب عدن</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90817" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90816" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇸🇦
الاعلام الغربي:
تضررت ثلاث محطات ضخ على طول خط أنابيب النفط الذي يمتد من الشرق إلى الغرب في المملكة العربية السعودية، في هجوم وقع الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90815" target="_blank">📅 19:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdAJ1kjoMjPPP1l_BUrtSzndrSZRQTV6_Jk3N2No0byvPeQ5JyTfJbcZrL_HIpPHPzGSUXcxM8gJjjkb1WIS5fADpZOp-AratD-3TxoPxHQIFssXebhNMAKEt-6_OR8nZRpkS7GIG_u7gb0fNFFej_6xhCPsTy4byhejkU60WkhzMG76zJArdc_M2gIOkroWTrR6jQ4sDegzVh7YIJRTONeU3HR5egFL8JcYVaCC7ffJ5Rbcr3W0hV7QHfhmiajcdkca4DbOs52HDLLTWUXNZYQgyBoFfNA5h6oLWTezUVhLqzxoXVfJ_4gnrQlaRPbIWscpAm6Vmr_Qdkn_TQYWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇶
السفير الروسي يغادر العاصمة بغداد قريبا ..</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90814" target="_blank">📅 18:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">السيد الحوثي: لن نسكت على البهتان السعودي وادعو شعبنا للخروج يوم غد في صنعاء والمحافظات للدفاع عن شرفه الاسلامي</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90813" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90812">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">السيد الحوثي: هناك تبعات شرعية وقانونية لهذا البهتان تجاه شعبنا ولذلك نحتفظ بحقنا في الرد على هذا الظلم والاساءة</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90812" target="_blank">📅 18:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90811">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
استدعاء السفير الألماني في طهران على خلفية تصريحات مسؤولين ألمان ضد إيران.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90811" target="_blank">📅 18:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">السيد الحوثي: الانظمة التي تلقفت البهتان السعودي يتحملون مع السعودي جنبا الى جنب كامل المسؤولية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90810" target="_blank">📅 18:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">السيد الحوثي: كل من ادان البهتان السعودي باستهداف مكة المكرمة هو شريك في العار. انها اساءة لشعبنا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90809" target="_blank">📅 18:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">السيد الحوثي: نحن كشعب يمني أنفسنا وأرواحنا وحياتنا وأموالنا وما نملك فداءً لمكة المكرمة فداءً للمقدسات الإسلامية بكلها.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90807" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">السيد الحوثي: قارون العصر السعودي المفتري يحمل راية هذا البهتان ضد شعبنا وهو قرن الشيطان ومنبع الزلازل والفتن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90806" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">السيد الحوثي يدعو الشعوب الاسلامية لرفض استخدام مكة المكرمة من قبل ال سعود لخدمة عدوانهم الظالم على الشعب اليمني.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90805" target="_blank">📅 17:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يسعى لحرب مباشرة تدخل فيها كل الاطراف الاقليمية.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90804" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90803" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">السيد الحوثي: استهداف مكة المكرمة كذبة كبرى وقبيحة وشنيعة للغاية كررها العدو السعودي عسى ان تلقى بعض الرواج.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90802" target="_blank">📅 17:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">السيد الحوثي: المعتدي السعودي استهدف في بلدنا كل شيء ولم يرع أي حرمة على الإطلاق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90801" target="_blank">📅 17:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90800" target="_blank">📅 17:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90799" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">السيد الحوثي: شعبنا العزيز لم يقبل مصادرة حقوقه وتصدى للعدوان ولم يهاجم سوى القواعد العسكرية والثروة النفطية السعودية</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90798" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يتصور ان قوته واستقراره وتحقيقه لطموحاته يكون بوضع شعبنا ضعيف ومستعبد ومقهورا تصادر حريته ويصادر استقراره ومشتت ومتفرقا</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90797" target="_blank">📅 17:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">السيد الحوثي: العدو السعودي ينفذ عدوانه على اليمن بدعم امريكي واشراف اسرائيلي</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90796" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">السيد الحوثي يبارك للشعب اليمني انتصاراته</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90795" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بدأ كلمة المرگض ال سعود السيد الحوثي</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90794" target="_blank">📅 17:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الكلمة بعد دقائق عند الساعة 4:45م</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90793" target="_blank">📅 17:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90792" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90791" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90791" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os1-A0eE2TE3Fqfm38TfMyLD5DLgIV21HfooET_oep_2GNNdICyc_wC-udtdC6hy6izLBFt-12N2DBDc86vXVZ4t2bN7X68FU5ejawAOswCY53FAgrn-Nm9JEhiiB_jPR5ooPbBnIdqWFOVMberRqESMjt2TFMQ0AJEVHIKXFq3fUTL_f_BsOjVTTquYb_ebvWPCaK_OoqXz3onmA2a00-LunaqeBGJSSqB_bOWVIAhpjq-VC1yFP4gP8ZDqxcEKD-OLyjjcuv5EuuWeqLwApC8C2Dd-yMylwWE5TK9895ibiFhacHC5JQ7TfJPUHxBH4Hl707-h7ftRTFasU4uLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90790" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90789" target="_blank">📅 16:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اسقاط الطائرة المسيرة السعودية في اجواء محافظة ذمار</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/90788" target="_blank">📅 16:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90787" target="_blank">📅 16:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90786" target="_blank">📅 16:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90785" target="_blank">📅 16:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1iSioW0NyDobVqhhq0eBbjnONcm_cfLaKx5jY49bRgHZCUg9e5vArJaFCoFo1xGzrRW_EOrr3ls4ajqH_F-h8lr7JX0GDSKf5l4GTLQ9xC8DThIupthR1_tjP1Z7-ScvyaCEswiVN5eerFxFMWatgWPUc2i2h43bZxyQeFY2wCxA3-t6_zizOqSdAe-9ioTrUi8dDU5ttt6xhI-7m08JXr_FCLPOX6l9wDFoYjstgHEr6iHpwufuNUxKCTKK_7m6DTaTL7G2rXSxmu2ZwkfIJMLaFPwTtCLDk7GmOuK5FWlvhkMnfTfsqCcg2_eRbUddlPDESL61pPbnVgOhVXBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90784" target="_blank">📅 16:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية تقرر بدء الدوام المدرسي في 1 تشرين الأول بعد استكمال استعداداتها لانطلاق العام الدراسي الجديد.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90783" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وسائل اعلام: السعودية تطلب من سلطنة عمان التوسط لدى أنصار الله لهدنة لمدة أسبوعين يبحث خلالها كافة المطالب الإنسانية وتنتهي بنهاية الأسبوع بإعلان اتفاق</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90782" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns3tWI5PhLi4sZVsdj26lsbVBnkSbVBva_NKdFj5CWch-c1yuqQZpChB8Fdj2jU7gcTJ2Tzt4C_cH-a6NLUK0S_iPAKD3c9af3nJ0SGbCPaS9hyn-smn3y8yl6S193sYf7720l5JA4qyJIe7hvcNltJX6FlL1Ib5UArPIyCFm0ypr30c3f1uLUQxrpVCxMzyI2lGgmNFsO8IjFGtyNbXGmOCwsqrLwflBedx135n90rO7Y4PczLONPn2WNKZLMRgGXSA7N4Y7y4ZFanJmY_Unjkclfh_iNdFCfe_C1yzT_dHczUfis51z199OY491iWtf_9OvKsA32eo_xCJVuycYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90781" target="_blank">📅 15:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90780" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">تواصل تصاعد اعمدة الدخان في شمال الكيان بعد تسلل ناجح لطائرات مسيرة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90779" target="_blank">📅 15:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKPKiPOSwf4NSwLCz2InmGUqJCjgoOzTUHc6kUxTI7xxJh0Ne2vKBcBdorp9hTGcUKpA6-9qh-DtOKh73kepCC8qCrG_QPahKyE3WOEzTobflDWW7TRlKYehfzXbnh191mPxEbxkCu27e4Y_O0sgjvbOIt47FF08pRUSpOr1Fbto6NbYgp5aJyTkCBHVcDch1KXpl5ewY_pYs6zMzY-CoVZWYZFM3hRQZxvolKDjLZLGnV2o4RTPqcfNlAAytSPuHsn1MDn6ecdhdmkEpdWUkgqwIm4jwzXQXFExsTyDr7YHNgJjIKHXEcdKWtep16WeHjocqWpkM_EoG14YqqDlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من تفعيل الدفاعات الصهيونية في شمال الكيان</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/90778" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=eaI4RG8T3Hb_PSVgH3xqpK58mNQQrlScEklLSgMJiHRPs1pcv35F2PYx7XpS3xPHAiouSeinYPndDJY1XVMzRodaa2WDXpK5D1QV3TgI41y5OUnkHhG-dMRjRxb4IqOX88J9GPqG626K67MjWI7TmljLVkpuWJ9PSifmN6QQQ_GV1XxCCavcUWv7_EY-M6rJuECVjaVuasTmZQ7gmcjguqYdC1g8tS7LvLFs11Dm6XQMc_9XOw_4II5Uk9PpV4PZoQqQcQTtrmrZ3YryeuKwJL84PerXbE3o8HXs4HaaZC3BsRAtqLryo43V7kw97AwQdG46RAqCJQPTaEKOBInM2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=eaI4RG8T3Hb_PSVgH3xqpK58mNQQrlScEklLSgMJiHRPs1pcv35F2PYx7XpS3xPHAiouSeinYPndDJY1XVMzRodaa2WDXpK5D1QV3TgI41y5OUnkHhG-dMRjRxb4IqOX88J9GPqG626K67MjWI7TmljLVkpuWJ9PSifmN6QQQ_GV1XxCCavcUWv7_EY-M6rJuECVjaVuasTmZQ7gmcjguqYdC1g8tS7LvLFs11Dm6XQMc_9XOw_4II5Uk9PpV4PZoQqQcQTtrmrZ3YryeuKwJL84PerXbE3o8HXs4HaaZC3BsRAtqLryo43V7kw97AwQdG46RAqCJQPTaEKOBInM2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدخان يتصاعد من كيبوتس دان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/90777" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اعمدة الدخان تتصاعد من شمال الكيان</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/90776" target="_blank">📅 15:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds_6LHKjsmSeSit4OG3u46rm1ZZzo6Yl8dNMxgL95ViFAv9gSaajKQFIGx8bl0VGLLe1ltJIyEeh4sippx61_MsCzIvVHuLYxE5raFCiZkBJW2GbbGZJBtS0M5oQ1WLCzgjTCRbx72fEuzAEW-uFoQsKwRB-jsrsqNqczXtlSkTFu2xFznXwv4nITeBhxBfnJpGg65fu4M5XhQHC0cwnMXirTqDAWLLo6dbw3w-TMDMFI7slbq7e1QOCTEBGQIsdgE6ZxUJp2DYWkWsoLV8JoFC2MvhVXb_bEzcLEls8RnK2PnGFx-1QKzkSo3VEymMkx3v6PYG0H_62P8zQakQ-YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من شمال الكيان بعد تسلل طائرات مسيرة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90775" target="_blank">📅 15:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39633299af.mp4?token=m0ybt2m9dMI_fZEKGiD4LO6wWqj7jGaeuJs3HDjIOBRyVFTAXlK1IjVTcf57fkMbb9IUhIx9bZiQUuCPcUqs0AkTl8ZvHvq19ZbFMTn1D4rUd1czbloV8a54zwh-4jffbQlR7srHgagNDOHV-EzFzd6ONZxbOM0pPdJv6cMpAlnmwrEx8eaYDgghqgltfsR6oiY0Dn-2Pir_4Joryuu8TtfmJnzdQBAcZ4Q-7B5peWwnlR_8CkE0jvi22dXvsb9JQJuhbEFgZVpveqTBaKZ7W80gfekHn4gBMkGLG7AbmSehs297na7yy77kI9crPMMoJA2lICfYYQMpI7vM3fUa8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39633299af.mp4?token=m0ybt2m9dMI_fZEKGiD4LO6wWqj7jGaeuJs3HDjIOBRyVFTAXlK1IjVTcf57fkMbb9IUhIx9bZiQUuCPcUqs0AkTl8ZvHvq19ZbFMTn1D4rUd1czbloV8a54zwh-4jffbQlR7srHgagNDOHV-EzFzd6ONZxbOM0pPdJv6cMpAlnmwrEx8eaYDgghqgltfsR6oiY0Dn-2Pir_4Joryuu8TtfmJnzdQBAcZ4Q-7B5peWwnlR_8CkE0jvi22dXvsb9JQJuhbEFgZVpveqTBaKZ7W80gfekHn4gBMkGLG7AbmSehs297na7yy77kI9crPMMoJA2lICfYYQMpI7vM3fUa8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة تسمع شمال إصبع الجليل</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90774" target="_blank">📅 15:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">محاولات للتصدي في شمال الكيان</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/90773" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWxkigrkil2DTmKoHbTZbYZG1DGEK5aK_APWxnpBhZJWnUh_zt9WI7lcV7ZtLghgBz3l1iIPGU6GirNTwXm52n2ojgjL1BAWxi2Zjblk2tgi6l1H5vex0ZZEpnNwzkiXEokYchB_ZQdCZ_bcN8Dy7hXWkerHut3zW6qcxn_JcVeO-7ZwUYMW7wmd4OR8ybEyewTOwk7RL9B3PDz23KPVt5bIkvHG1FnEpBbBW4aOMGwbTWiut5_qlJnLh9PVBuyWdlMQOV4TxTOzHqpv-dGv_07C_Se8T7UoVtKOIF4z3MfBqzJ2hnHHZCbvcJdYhpco-cd_prHowMAE9_QeHzsiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية في المستوطنات الشمالية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90772" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تفعيل أنظمة الإنذار في منطقة منارة ومرجليوت</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90771" target="_blank">📅 15:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90770" target="_blank">📅 15:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90769" target="_blank">📅 15:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90768" target="_blank">📅 14:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b327d0501.mp4?token=nraUQuS-eYLpU_rTN_o3qgeTq9-GY0kd0cHEulFM4jyhW5BPXZ_ZosPs72ncfB2JdtljDX8iXrSsiTDuJ_-F62TvNFKr4tTKUESVv1tAVi_PL6QjDFK3Nf-il11ne2PhpK1fDDv2khjO48q5apIsjYWKkuwQA9VGHKW7SSTh2elYgGrHcY5NYQ5UdBXRpueN6GObd5RX2_bA4EWgMpHpNL_omupUSEUnMIWS0YAYP-btMWfVmqXshMQZK2aNadVF-tcoJCOq6nKoWdsHq3G43dOVWC0FS0_p81lRPOyOaxga_K89qZ077uqRoGpXKsFXsqiHqXtHYGmbG1T1-HpcYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b327d0501.mp4?token=nraUQuS-eYLpU_rTN_o3qgeTq9-GY0kd0cHEulFM4jyhW5BPXZ_ZosPs72ncfB2JdtljDX8iXrSsiTDuJ_-F62TvNFKr4tTKUESVv1tAVi_PL6QjDFK3Nf-il11ne2PhpK1fDDv2khjO48q5apIsjYWKkuwQA9VGHKW7SSTh2elYgGrHcY5NYQ5UdBXRpueN6GObd5RX2_bA4EWgMpHpNL_omupUSEUnMIWS0YAYP-btMWfVmqXshMQZK2aNadVF-tcoJCOq6nKoWdsHq3G43dOVWC0FS0_p81lRPOyOaxga_K89qZ077uqRoGpXKsFXsqiHqXtHYGmbG1T1-HpcYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان سعودي على منطقة الحوبان شرق تعز اليمنية.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90767" target="_blank">📅 14:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
سكرتير مجلس الأمن الروسي سيرغي شويغو:
الولايات المتحدة الأميركية وأوروبا معنيتان بإضعاف موقعي روسيا وإيران وفرض قواعدهما الخاصة في جنوب القوقاز، خطط الغرب تتضمن تقليص تعاون روسيا مع دول الجنوب العالمي وعزلها عن العمليات العالمية.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/90766" target="_blank">📅 14:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ab7a4269.mp4?token=FAlpYruXqZ5PgOdWGsyT9csAq1Wk4P9lQU4uz-2mVirg8m3q9b0CXIOno1x9naZqq4KyVKs3J_-L3NETjj5t_m9xQ3lzRhK9OLVLpdqxrSFpSr4jlIC934bMp5mGWVy0Xwfqgv17oW-kJYLrAzwZkROgEGsOXBZ5myHQ-OwbnozCvDz33MQo5NJOyL9BV_rloxtUma0Y807hI9F4aX5o7bwpIbi8qZBcr5vUSmN2o1AJKZlxEREkkcMNeKG2BXd8EeVJm-YUwT48TRXeDjTjXtNHjJxwZNpookDcGTP4qvUzLcNPdCP5VD13qLeyuu3ZMH3ibvXXMlPtNueG4fWtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ab7a4269.mp4?token=FAlpYruXqZ5PgOdWGsyT9csAq1Wk4P9lQU4uz-2mVirg8m3q9b0CXIOno1x9naZqq4KyVKs3J_-L3NETjj5t_m9xQ3lzRhK9OLVLpdqxrSFpSr4jlIC934bMp5mGWVy0Xwfqgv17oW-kJYLrAzwZkROgEGsOXBZ5myHQ-OwbnozCvDz33MQo5NJOyL9BV_rloxtUma0Y807hI9F4aX5o7bwpIbi8qZBcr5vUSmN2o1AJKZlxEREkkcMNeKG2BXd8EeVJm-YUwT48TRXeDjTjXtNHjJxwZNpookDcGTP4qvUzLcNPdCP5VD13qLeyuu3ZMH3ibvXXMlPtNueG4fWtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدأ موجة احتجاجات كبيرة جديدة في سوريا بسبب تعنت الجولاني وحكومته واصراراه على قرار رفع اسعار الوقود
اهم شي رجعت اصاله عالشام</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90765" target="_blank">📅 13:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
ندين قرار السويد منع أحد دبلوماسيينا من مواصلة مهامه في سفارتنا بستوكهولم وأبلغنا سفير السويد بأنه يتعين على أحد الدبلوماسيين السويديين مغادرة إيران خلال 48 ساعة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90764" target="_blank">📅 13:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله يدعون لخروج جماهيري كبير يوم غد للشعب اليمني الابي في صنعاء والمحافظات اليمنية بعنوان (دعم القوات المسلحة ومعادلة الحصار بالحصار، وفضح أكذوبة استهداف مكة)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90763" target="_blank">📅 12:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNYDoeCIS2bNkl_v_iskzzEfhq3LtJK0xbGoAMAenFA693DLcTK2631pMk8j3ABDOSBypKa24RmeVO46cXzCa3eNv8kWxA-ClelBx2ofajRN03XUIfmJSEhq8im-4gb5a_ov48OE4j90b5-tABC1PxBr0DQQUetfB5vMSJ4ZOAlJJ8Xy4uXLy5X8VatDRedhq16Evkvk7Bn-Lc7fMV6a2V38DbcyhF9oQoZ0WxY9Q2H0nSuuUZORWii0Xr4pCDu0UdE2Hh_3kJx6NTdZZrQ8UBDSId89RL9zJh4S692KOnNYU4MiOOaZ58c-6TJu8lP4EGOj78-vyHSVeZhhz9e6Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر في الحكومة اليمنية لنايا
ندعو الشعب العراقي الكريم بأن يتريثوا هذا العام ولا يقدموا حجز او دفع مالي للحج عبر هيئة العمرة والحج العراقية فقد يكون هذا العام موسم الحج مجاني لكل المسلمين .</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/90762" target="_blank">📅 12:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🏴‍☠️
🇷🇺
زلينسكي : استهدفنا مصفاة ياروسلافل النفطية. و مطار عسكري في روستوف، وزعم زلينسكي عن أضرار لحقت بطائرة أنتونوف An-12 وطائرتين من طراز An-26 وثلاث مروحيات.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90761" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
🇸🇦
🇺🇸
🇨🇳
نييورك تايمز :
حذرت أجهزة الاستخبارات الأمريكية من أن بيع طائرات إف-35 المقاتلة للسعودية قد يُعرّض تكنولوجيا حساسة لخطر الاختراق من قِبل الصين، وقد تناول تقييمٌ أجراه البنتاغون قبل عدة أشهر إمكانية وصول الجيش الصيني إلى قواعد في السعودية، واستخدام الرياض للتكنولوجيا الصينية في بنيتها التحتية للاتصالات .
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90760" target="_blank">📅 09:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94042c2176.mp4?token=ZhWthsGsegCiTVzQhfEK02rMtMozjHQyXm1gOEdpCvKTJ-EduZgX3KpsUWa1VQzO2APKbw-Fw068p80bBzvdKVQqpEpByrs818U7ouM0YuQo4Vk1njdAp3HJcYYncmXeNC7NH0PakvBWxx91bQHBOsjEfuUVqHEVtU7NDoKVJBRxDqXYoE03L4CiUb_2S5Jj78cGuMvVsG5AW0SjH7EtAW_BmJZlyFflDIlvl9pYYyNdVrO7Rcm_92Ns4BMLlMKHEv6c1dNNlYDaw9Cuva2Us4SGdD1NSN6CJqeaMlwc7QlNWLQPTKPDXYXqpbrA2NqUTx7WpUcg-WPt6qccEtmybg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94042c2176.mp4?token=ZhWthsGsegCiTVzQhfEK02rMtMozjHQyXm1gOEdpCvKTJ-EduZgX3KpsUWa1VQzO2APKbw-Fw068p80bBzvdKVQqpEpByrs818U7ouM0YuQo4Vk1njdAp3HJcYYncmXeNC7NH0PakvBWxx91bQHBOsjEfuUVqHEVtU7NDoKVJBRxDqXYoE03L4CiUb_2S5Jj78cGuMvVsG5AW0SjH7EtAW_BmJZlyFflDIlvl9pYYyNdVrO7Rcm_92Ns4BMLlMKHEv6c1dNNlYDaw9Cuva2Us4SGdD1NSN6CJqeaMlwc7QlNWLQPTKPDXYXqpbrA2NqUTx7WpUcg-WPt6qccEtmybg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
القيادي بالمعارضة السعودية
يكشف عن خطة " مبس " بعد فشل التحشيد حول فكرة قصف مكة، محمد بن سلمان قد يتسبب بعمل إرهابي في مكة أو المدينة ليلصقها بالحوثيين. على غرار محاولة ابو جهل بالاستعانة باليهود في الحديبية .</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90759" target="_blank">📅 09:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇸🇾
إندلاع إشتباكات مسلحة عنيفة بين عصابات الجولاني ومسلحين في مدينة الصنمين بريف محافظة درعا السورية؛ سقوط قتلى وجرحى من الطرفين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/90758" target="_blank">📅 07:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=Yr6kN9b5s753WjvDFs23_LugqeCScwleDuQ06e59ueRNbU2hQizrwNDXK6trZ2zfB134dEnsCXPiu5Yx7z9DWZHYwkfeMhiitUF1cmXyGXQBfINRMpa5kxRyprnq7t7rZlVaj6y905aaP9dMhyeqwVTrxbsUCSV1Exm_nv-qXLHPHfzVHj_CgfKe2HHoqGIaQzaokXosdtvMBPgvouBsM6L6o5a_-Z7Y9Jlqqqc45gbEEbt8IpzDx8D7Ew7lEaf_vV6j6U0TqoyiJz2x8mOy3Wzaxy6vJCZEr7GnabmT-UHWOxlkEYJcPkn403Bcg6AQyYU9kljhQCrGYZ7AIPUJ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5f30186f.mp4?token=Yr6kN9b5s753WjvDFs23_LugqeCScwleDuQ06e59ueRNbU2hQizrwNDXK6trZ2zfB134dEnsCXPiu5Yx7z9DWZHYwkfeMhiitUF1cmXyGXQBfINRMpa5kxRyprnq7t7rZlVaj6y905aaP9dMhyeqwVTrxbsUCSV1Exm_nv-qXLHPHfzVHj_CgfKe2HHoqGIaQzaokXosdtvMBPgvouBsM6L6o5a_-Z7Y9Jlqqqc45gbEEbt8IpzDx8D7Ew7lEaf_vV6j6U0TqoyiJz2x8mOy3Wzaxy6vJCZEr7GnabmT-UHWOxlkEYJcPkn403Bcg6AQyYU9kljhQCrGYZ7AIPUJ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب عن إيران: بصراحة، الأمر سينتهي قريبًا لأنهم لا يستطيعون الاستمرار. أمتهم مدمرة.  قد يكون هناك ارتفاع طفيف في أسعار الوقود. لكن هذا سعر زهيد للغاية مقارنة بما فعلناه.  قد يكون الأمر أكثر من ذلك. وبصراحة، حتى لو كان الأمر أكثر بكثير، إلا أن هذا كله…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90757" target="_blank">📅 04:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b525552494.mp4?token=KM2w1JAd__1Mg0pfvRK6AtUfYdp-MzCfNxJ7STGtHGt8LaZshq2sdhymaY3Qxzf-HPF_yAH3pVieQz6ksnU2DxFMqHa2-uVQiJ5uik4sKxcjTXE4VVWMqacn1e-XKbgbpM0Gq8NOfdljLpWT6sCBK-WR5QztT0CHRJBQ0RAah-RczXKACnROzR37erKYvAZK-gn5IaokhFE5aQncpxs7nYyxRdshrRpTKFMLs99QuWIrM9LfxMcq-6A48HaDP-1yWpIvyZpXrbneinUKsNEzFiE0vnitUstkncXHhCm_cmGzV6ZMkOECilJd34aeuSegpoCum6_yHC3d8tlN2kfm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b525552494.mp4?token=KM2w1JAd__1Mg0pfvRK6AtUfYdp-MzCfNxJ7STGtHGt8LaZshq2sdhymaY3Qxzf-HPF_yAH3pVieQz6ksnU2DxFMqHa2-uVQiJ5uik4sKxcjTXE4VVWMqacn1e-XKbgbpM0Gq8NOfdljLpWT6sCBK-WR5QztT0CHRJBQ0RAah-RczXKACnROzR37erKYvAZK-gn5IaokhFE5aQncpxs7nYyxRdshrRpTKFMLs99QuWIrM9LfxMcq-6A48HaDP-1yWpIvyZpXrbneinUKsNEzFiE0vnitUstkncXHhCm_cmGzV6ZMkOECilJd34aeuSegpoCum6_yHC3d8tlN2kfm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
بعد أيام من إستحواذ إيران على قواصة وإستهداف سفن حربية أمريكية.. ترامب: كل شيء دمر في إيران وسلاحها البحري يقبع في قاع الخليج.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/90756" target="_blank">📅 03:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب:  الإيرانيون يتعرضون لخسائر فادحة ويريدون التوصل إلى اتفاق بشدة.  الحرب مع إيران ستنتهي قريبا جدا.  يمكننا التوصل إلى اتفاق بشأن إيران في أي وقت نريده.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90755" target="_blank">📅 03:54 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
