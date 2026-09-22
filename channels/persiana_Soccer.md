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
<img src="https://cdn4.telesco.pe/file/pCk9_c_qhult3DUj9RBj2Xzs3hwBSwngvklLjKDB71KNhdH2qW1AvEXPih4h_k9Zso0vyj75CB6toKmqFcD63cuqcKoC0YAIO0hWTO1K6PuHnIR5oYtjOprRbg6CK1-OLdnD__dARESixlNWr5XFyB-eIzjs-VctMl3E0nohqX57le2pALfM4KAQMtfLzhxWVKrTyVlUoNrjBfj09esFWulovy4MOrFuyUgHJ0xUGhOkQQ8cZAUow_thLzXJAgOMgl8e5naPGBtHXSdidUvfnk5ZsG17xAJKc4kP_JVmTXL-2E8hpPQM-IZj_Shq4D4AMuF9QPSwNeHElGtrBSXmsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 462K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsdX8REOlgJoZuQY4a2TMRqNndkOXm-Kh3huHKz4g_XZZwsUS_doe2-16wy9feajPgNaqUNMwH2llL9tCiSZdFMHNlEp_apgm9KjXpDN37SsEXlU8niaiS1WfuEHIQbXB35Now-_huFOSpgQZDr1PPxO7PH9Y6d17uF6UpmSOOMiePm2h7CkD00_ONQcjK5Lwb0Cb63PRHT1g79vbZHe-PXwRQZ5wI8LWRMiHi0kaowYAYH-Kunw81znKU38ky6O4-gs4BK4SfgJWhGN-KFfPPupruKRo8T5B8ogORgCsiG7WOi9Mp9_eE6q5zRzVkpiAoVd38psIiFgjeIRJy6RnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bC_HRRWP1hRRir52Jhrk1EiS_ghTWze7isE8ju9l1Ri6CUNkUJRTX7cYByqPqd1_v5enGENp_84IRReXd0YKSHJJ8hJJ3OaiW1dQyVvHiPwUqEwoLYy3mg4CiimN48Jcz1zjYUd31uVYX8qM1Kv1QqaOYES1n6WdnQviTjPZ2zM8MknK56Wp3j-LZ5Vx9_QaUBtV7xT8qnJGeesBM3-o-iU2CP0VHXVdQI-1tg-g-yVmo70p6w1eDDXTTq11GCyXuecedLMmQYcMLOiDZg5hC7tFI_rcqcbz2CroB00H9OADHrHpi4vtkXsr-jLy1IopaAZAcMbmqGtn6xEPNB2H1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZsXtc1hQY-rXqRNIp_zVtraUw-lz7e7o0qmPdlrZgjHQfY0SMwurIrDAUAwSeztFKAEoM0V5EhNrj_e5nZbG3sV1Sa1Gdbd-QBjcfalRUgyeNPksvJebwHsulDuZJLpKypqsIh1e0uWRe3eGTH7NOMgwBuDU-QtpjXdRqujbUQX-F8Sa8hLxBKsm_gHp5A_wxKcGPamZ2w4JAjXEaoyiZQw3xHEcCio5Qf6R1_5m22ODhFWDfZB6l_YJ7sI9VV2ddZ-FbYJd-T5gcoXmswnlqERyCmXRW-RUTQiyYVpSaO6k8VPqsJATbmHq_Wkg1mtx4OuFiyWUP41c2lAhtJkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=O5gzquJErXub5ybjpB6NztJPgcUMQmC0_0xpJksrFtDbRIhlCXE1W94o5bDoX92uvGUeFKzn1tuSBxuokJeuzEOXd9AhGm23oUq3aRXcuQTGrQehgzdsoRKZGsPxQN-n02E0v_Y-S2LO3VYk2scx_493UieeXNkBu6F1a-c9yPkPDS2kEoxhi1dMB_MV358ZD0ddAfAu5j8B_lmb0bftJmt6TINPwsVcY6ZUKuzV_ITSPtm9b6NWNmboXVvHju_wIT-D32NosKDb0x3DXtGley6XErhMiTq53_7hy24qWwxx4NwNI9NyZDU8YUVtXGncDhHdAsr35nIEYHw2kLoN6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=O5gzquJErXub5ybjpB6NztJPgcUMQmC0_0xpJksrFtDbRIhlCXE1W94o5bDoX92uvGUeFKzn1tuSBxuokJeuzEOXd9AhGm23oUq3aRXcuQTGrQehgzdsoRKZGsPxQN-n02E0v_Y-S2LO3VYk2scx_493UieeXNkBu6F1a-c9yPkPDS2kEoxhi1dMB_MV358ZD0ddAfAu5j8B_lmb0bftJmt6TINPwsVcY6ZUKuzV_ITSPtm9b6NWNmboXVvHju_wIT-D32NosKDb0x3DXtGley6XErhMiTq53_7hy24qWwxx4NwNI9NyZDU8YUVtXGncDhHdAsr35nIEYHw2kLoN6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI7Z2XTaugHaHJfQbFlw9L51KdgAg2vyphjV6td9URW-oP1cRzKjYqNpGKwZdNynV4ScgHhvqSuBNuApUvARG39nW1949cUcSx5lym6nqirJVLiQzkyYiAo8aG692xSOeYcTNfjlnR4UA0Tent_IaGJrbbuw-iN5d_OD-ueMtGCDTPwwNGq3NwqednSrUsCQVYykgWNsrQIj9cpRFVQee3KTyhCSAxJPWNGYMLF-JBxFAmewpeYgB2pGcdtE50gTFLOUtBeMWlPWVSP2-vR0lVB_uAlyGYBBGBJTwn8VRFH1itCOuhkvDFviNdJPC1B4S15hJJQGomE2jLShFk7QGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=ExplXyC7aPjaN5e_7Nbf36dhHCcsHQKVKmZIsH2reUu19YLThC0UWyMX8yI5zhfes78zb9VVueO-c6d_QntgAi8jBY1b7akBr5tlZuMku_3qZN4nXtp71o0_jE9xK5M3ABgF4K20LCKpQ3sZ1Cg_VhL5Eg4D2t_nFOT803tH1ncMKHLWyt4Ni_jX-9wHG_QVTgJYuwfqjj_X-DZ2O5pdssw3m4BtJEp4t8il5mKuRNdL-DDJZDr5Z1dyo83G46lqf2iqByS2V-QCaSqgX8480Nv083AJ_ENs-iE_RXlY1mC3nAiVbvgdJhJAn0YdbRTY3Empk5jGI2WxY_3D7NRcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=ExplXyC7aPjaN5e_7Nbf36dhHCcsHQKVKmZIsH2reUu19YLThC0UWyMX8yI5zhfes78zb9VVueO-c6d_QntgAi8jBY1b7akBr5tlZuMku_3qZN4nXtp71o0_jE9xK5M3ABgF4K20LCKpQ3sZ1Cg_VhL5Eg4D2t_nFOT803tH1ncMKHLWyt4Ni_jX-9wHG_QVTgJYuwfqjj_X-DZ2O5pdssw3m4BtJEp4t8il5mKuRNdL-DDJZDr5Z1dyo83G46lqf2iqByS2V-QCaSqgX8480Nv083AJ_ENs-iE_RXlY1mC3nAiVbvgdJhJAn0YdbRTY3Empk5jGI2WxY_3D7NRcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMM9X5svIBxEro4wDmnVZRHtfgfV5i57fw0nwjBpLsnVuboJ9xZSlAxBieBOzrkiZ6Uwn6Qwf-hpNY1fHgzemk5XMqR0Jc4e_vpLM2ShWlbYl8Arodtg7saJ2hwYVi_5f4If045naP0AAE6o35Tmhg9in45VWxA2C5-svul45jsruVih9uA1FVAMah3OM5ukjM4YOlrElvk-IVEQgPNNKqFuOMsU4pTTPgtWsCAPiJ_PmGZuyG3hYjOAAM-3oUa_eLz95PN5ZnMwRB__2HaXYPPMNqns_DwZFtowaNIMrcovmg7hfpnINsPcEF3HqlaL2X5vtdXEcB-W6pHzQIATrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFtDdl4f12L4RsNQ4PhHF-23V0saXLzO7Cyn0__US6ZIzcPvvTRFeuxM-rRWvEX7jUCVmWQDS80nK4Yehl0WT9t0w5psZ1paXJWG4HEbHg4oow6vtLYJQqIFFZh9rUOcHAMHDUwCatLNm1mSxiSwQAWLDOwJXBJBpUi2mDmZb8H70kmT3VDCRLF8jWBa_9v4sT5Q1ICvg0mi0Bu2qL-Tav0gb4Fwu5bWR8zL5UYZNmODV7eXnsLZDrE7t09XWIGuB1kRN0zXFHbvxohGIHWJxLyXGOzl-brh7e7mLbC3Dqb-Nz45EUDr1IXer9aFVUDyKJpfNRN5D-7atCRjTZY9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=cT_iG4-4kAievd9Ghtaj-AfCJmFhtJS7f-WD-KVtiCMd6E-RzbCl1nN5-uYX2pAUQ1kQpf7rK5Q0CdlkA0t9GM51NF9PzHT4YAIgifl_6o6yUqcf98p5EBFogbs5s-LXuGipx61R-3Xs1LjrEM9JW-s46ciqo6Zk4iRiO6PRa-dqxaLT5mkXOlF1cIjTd_DUTmC2Cq3VinEqPxiv7lZV93OJOeULGL1fYob7zGhk6YhGiCGpk5FcKMibcq0n5LcHeXNdbDZEZvdU1JiwekAmJMNLvZs-T6zwW_oMjn4csXO8zXKRnimX5-HlFKtG4l4iX0mlRSR0xMzgXgirAj4aoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=cT_iG4-4kAievd9Ghtaj-AfCJmFhtJS7f-WD-KVtiCMd6E-RzbCl1nN5-uYX2pAUQ1kQpf7rK5Q0CdlkA0t9GM51NF9PzHT4YAIgifl_6o6yUqcf98p5EBFogbs5s-LXuGipx61R-3Xs1LjrEM9JW-s46ciqo6Zk4iRiO6PRa-dqxaLT5mkXOlF1cIjTd_DUTmC2Cq3VinEqPxiv7lZV93OJOeULGL1fYob7zGhk6YhGiCGpk5FcKMibcq0n5LcHeXNdbDZEZvdU1JiwekAmJMNLvZs-T6zwW_oMjn4csXO8zXKRnimX5-HlFKtG4l4iX0mlRSR0xMzgXgirAj4aoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSYZqSyVbbfIr9WMC-OB12R1UV4C1oxUznBZuevUaEbQrnmd5Bv-2hwq1HcJSVSAfe-v4peOk86dTj5Q1vhsYOVeAA1llmUOrW7NKqzqTe3a6w8IPCfZgjn2IbVrIsnDau6p3RWsClUR-b6nNXPWHg2fb0Zu5yMiooAXI1iCdYh9U_LWF_55LsHQ_a5x7nQJfBg3tUs5VntfwRkgPSFIFQRyrSJka_T60Id-FvCjZEVYwe_EGA_1TMv_ovt3BoyuKAc3w2CHGiNuqnYdLHDT6RUFqxlOPLNH4pXDcFSnAyLf2G8AQXkW0aBcYntOmI8Hn51l8dC3vLXiula3tb_QJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=WI-Tg-y30GNB2kyB3PPaunAgiAK-G6Xq2M9zGRWeUoywHEQbInVNFsgDIJUhuY_WKosXG3BL8pt1VbInWGfhEduNTOUOBOvq7J8Qwx2bB3JYb1R-iBYlTe-m8Uq6BI4lrLarAyuqbOwu-3wTqW11-twc_Rh5VE5pK1wEH3v9XJetk-r1oYeS8zUZVpR2YloeVHkOzrJA-sS1u6kV_Q69icK61Jm5uv5RMfZu79uJnJgEERD5TY47VN1PbxEP0WtxN5Fu8aPKzIP1FSi4L4GU3Zdi-sEkVZJ8QQKxoMDd4fVzt5RvPF8yDafdo-1Z-pUzOLd5-xAhOs09ml0aLx8HO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=WI-Tg-y30GNB2kyB3PPaunAgiAK-G6Xq2M9zGRWeUoywHEQbInVNFsgDIJUhuY_WKosXG3BL8pt1VbInWGfhEduNTOUOBOvq7J8Qwx2bB3JYb1R-iBYlTe-m8Uq6BI4lrLarAyuqbOwu-3wTqW11-twc_Rh5VE5pK1wEH3v9XJetk-r1oYeS8zUZVpR2YloeVHkOzrJA-sS1u6kV_Q69icK61Jm5uv5RMfZu79uJnJgEERD5TY47VN1PbxEP0WtxN5Fu8aPKzIP1FSi4L4GU3Zdi-sEkVZJ8QQKxoMDd4fVzt5RvPF8yDafdo-1Z-pUzOLd5-xAhOs09ml0aLx8HO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hc4EfyrX7uBga12yzXHUs8WkM9SIRIu29_sLxvpz1jK7thUlwXk4TynWemRbEG9hVjeLn00ZZV3tEuH66kuJwvmpo1Y-TJVrfswN7-aT5FhGgQ14MQdrxLmLwXdA6m1UDgI6UmIWCs6V-7FTp6DDRcOvMN_UWG1whZT-a6MmwN-eZ9Bp_r6u5WO8ZTMgBUwMkjjkhN-RLH0xKdENyFaKQiRyHXRJTfWg7bz75_NJR9g4FqCIqlL8ryQ8Sz3zpTrD7RmCA5WOHzG9Wj3dw8dI5za1f6eaJ7Qm_hqgIUsJFlhPNQXgVO5UdtfWIAlqvthFNUnVpejm-yh2-wxEg_F-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منصور عظیمی معاون ورزشی باشگاه تراکتور که ارتباط خوبی باستاره‌های‌ایرانی و خارجی داره بعد از اختلاف بامالک‌تراکتور از این باشگاه جداشد. در طول سه سال‌اخیر عظیمی‌مسئول‌مذاکره با بازیکنان بود و مذاکرات حرفه‌ای او باعث شد که تراکتور ستاره های زیادی در طی این چند فصل جذب کنه. هر باشگاهی عظیمی رواستخدام‌کنه از همین حالا نقل و انتقالات نیم فصل اول رقابت‌های لیگ برتر رو برده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30231" target="_blank">📅 12:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkXV051yzgHAAJR83YcehotCKkWVRSZJPoTF5VMXm-Wh44DqqWpkrUvi_M9uAs2cLXCu7bFMcyhpmGgZEppVfKzOV4Iosf3-bCUPV7ib7-d0TjYjeCf746tD2trIXPmeEejHSrk30K--CAsVboacgWO0-CsgFp0CEIo3mIehonlxwgaCMPqCjAE2rlhEHJejCczCnowm7fFmQnbZEUv-f0nAXXjjo22X1T5fx_EoIBQLgFa19WntiDsaPZLiyKh9D_Va2AMeMsIP6HuSLKG9RYz8vvcTO3IKjvLNo8DF-ubaj8mxb5IjmDI010ZYr0l4_60mSPOAngWKHVFgj3wblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30230" target="_blank">📅 12:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول‌برنامه‌جدید و فان ابوطالب حسینی برای‌حواشی‌فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30229" target="_blank">📅 12:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: توپ‌طلافوتبال به بهترین بازیکن دنیا داده میشه نه‌اینکه‌بدن به بازیکنی که فقط 80 گل‌ زده چون که برای‌گلزنی جایزه آقای گلی رو میدن. اینا خیلی‌ متفاوته! بهترین بازیکن جهان کسی هستش که وقتی به عنوان گزارشگر یا تماشاگر بازی رو بخاطرش میبینی لذت‌میبری…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30228" target="_blank">📅 11:59 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgzRiAsNDcNwDvjAG39xsdq6gYxz6Fe45ONkU-C9MFFJVn2l1-f_4JgBj130OLGOcm3UIdxULqXZYHfuctG7aRJ1IkRrBaOyNjENN4uf52ur2Vwx__R0xQHRDT29R8fwl8P5S3CgdkGCqrcWozIURCa4R4Pl0jzC8JZl8NbU3lOmzyQAzPKNOHmssFxqoWZDiO6jWeqaT3ZLQEg5SqZ6_QVhL0d68F0q4_Eb03V2OKmDdsYWKMe9RswOb52uq_KNAXKQr9PcGo_NAJ2ghFrlOLDBKHPBlBLlR33VC6VvUVExRbCV2zMqqBscoMOtBP354a2HcQT6ALqS7APUrHSn-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
مسی درتعقیب‌رکوردی تاریخی؛ لیونل مسی حالا تعدادگل‌هایش‌از روی‌ضربات ایستگاهی را به ۷۵ گل رسانده و تنها ۳ گل با مارسلینیو کاریوکا، برترین گلزن تاریخ فوتبال از روی ضربه آزاد، فاصله دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/30227" target="_blank">📅 11:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇫🇷
ویدیویی از اولین تمرین تیم ملی فرانسه بعد از جام جهانی 2026 تحت هدایت زین الدیت زیدان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30226" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30225">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=FubKMF8oYkQw0ELXK_Gs3O7Jjw_yoBGpjUQS8nHJMbCGMxFNc-UDDGo4pg1pSLegfWdkCxN6VXogZHf0jD-J7eYYSNsk5wrModtorbvgj3F9dgycZwwJntOfXHmfw8Gg2kNkFOtXQYRNAoU_gJbtv4YsfdgahxQitG0JQW6ysRAH1c3aRlWF2HnqvDYoPMeFOvOCpBwAhsr2Wy6oq8OtmwBroITkxhl52ZjtpuHjol_ulEagwHqelWVgZX41DND4D4Tcd5pXAmnxayCgelW4TiqkcHSMD688sgr6FamlKehFg5uddq9tOE6pOe2fhYdcB98R25SM-jRoCXHcYn7zSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46dfa14d7e.mp4?token=FubKMF8oYkQw0ELXK_Gs3O7Jjw_yoBGpjUQS8nHJMbCGMxFNc-UDDGo4pg1pSLegfWdkCxN6VXogZHf0jD-J7eYYSNsk5wrModtorbvgj3F9dgycZwwJntOfXHmfw8Gg2kNkFOtXQYRNAoU_gJbtv4YsfdgahxQitG0JQW6ysRAH1c3aRlWF2HnqvDYoPMeFOvOCpBwAhsr2Wy6oq8OtmwBroITkxhl52ZjtpuHjol_ulEagwHqelWVgZX41DND4D4Tcd5pXAmnxayCgelW4TiqkcHSMD688sgr6FamlKehFg5uddq9tOE6pOe2fhYdcB98R25SM-jRoCXHcYn7zSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده:
من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30225" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30224">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGQFLLvF5Tfh9Mq0rTXijX8vdCG49pOwIvjA3AZxgpoMkl8GdLD9HD1BqVy8XK0H5iwTNUiD7bG63x0rH0GBiEQCV2n9CzQyuXtfxIV0Q5kWlJ8WgPapv68_YfBb6f6ZHnfOMpg8prXMQMcIDi38H60v3kYTqa9QleLcCGk8KUT-SghzQiGm2ziKlJ5H98EYP00x_y-pGay9tfltkcA1RVruebdedZ5HIjJrYUAZl_nol0q7sgTs0BTBxafh0GUew6BYv-Tsofg_z3cDupWgMv2BD_-tDZFkhbW-UrfpNItboznDSbRia7VzDS35X-SkPshZRdGgagi0ocZ7wb0DIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران میتوانند در روز جمعه پس از هر بار شارژ حساب کاربری خود از پشتیبانی بانس
🤩
🤩
🤩
کازینو را تا سقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r31
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30224" target="_blank">📅 11:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30223">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619db5893c.mp4?token=dZIKLOJRVTZGkLvqdPeDGhq-261JP10tAUXiZ5BmCCYZvflRP5jRKBJ-XMs8LyA8EpH51oCmGl5oexXkDw3ImRNRQ00uELyD8JIuhJQmBaMmjY9u3vaxjlbAlis0vjpBZFOq6dcTkxDLD9MU7zgCCQVVQBmEbxFj6eiu1xY0HfUMAbcLldHjb3UmN3h4A_7Aly1bvhulgRf0I3Nr-3CuN0HcQysIJKgspWZdLaQd_u77eSRJ2G2Mgp4AKOaxgDDO0GvU1iJRiGQKysbe-WKkrgQq5BbeYLIbhroeIKdmaXa6AUwCJyaNQ-q2Md1NSItjF5ayqI1_uvBI3HpHclAEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619db5893c.mp4?token=dZIKLOJRVTZGkLvqdPeDGhq-261JP10tAUXiZ5BmCCYZvflRP5jRKBJ-XMs8LyA8EpH51oCmGl5oexXkDw3ImRNRQ00uELyD8JIuhJQmBaMmjY9u3vaxjlbAlis0vjpBZFOq6dcTkxDLD9MU7zgCCQVVQBmEbxFj6eiu1xY0HfUMAbcLldHjb3UmN3h4A_7Aly1bvhulgRf0I3Nr-3CuN0HcQysIJKgspWZdLaQd_u77eSRJ2G2Mgp4AKOaxgDDO0GvU1iJRiGQKysbe-WKkrgQq5BbeYLIbhroeIKdmaXa6AUwCJyaNQ-q2Md1NSItjF5ayqI1_uvBI3HpHclAEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد ضیا مجری‌سابق‌صداوسیما که بعدِ اتفاقات 1401 از این سازمان اومد بیرون درباره خداداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/30223" target="_blank">📅 10:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30222">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c1024d94.mp4?token=vgnq1FiGXCvIpVmQA9dp9R9LYQikjFk5nFomwnL2mSG442v0d_reqk6qG9Yxj7GWw84pFpMLMevw33oMkV5PV3u8INXPfbPNaQ8c-XPXYL-MwZRp-xj60xhOu_PXeOgLRsqA_kAt2si8y7vDQFNdlN2R7wXakHsLb1ws9ojXqycQE7slPkgnhzi0hdtI-j-BtCmNqtrsxeHNW_hKThzGO2VpOA96APXqP39TZXimSAe8_3NZPIbrNULXdLDSrKUcjiRyO2OOuU8UilwsFiQ_YGwtHv1sXUVY5Y_KxlceAjmwHICMc6DCVGr7a0KobYcJiw7vle-uWrlM-guc6JxWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس‌سنگین‌ابوطالب به خدادادعزیزی در قسمت اول برنامه جدیدش: قلب آدم صاف باشه نه پاهاش، شما قلبت پرانتزیه آقای خداداد عزیزی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30222" target="_blank">📅 10:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30221">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyolV2tO0SG37ARp0g_I2BmmNtP1_K6n9zr8nkVkwrN85Bk2urzSluu84sxPNZkJWiYbOgjxfpPY25RRO5s1ZV0ojEOOliGJmtwoP4ltLCUjlXKkVAVIx3nCJ5_2BN1TsP0ugdtyHntOXvi4Zz4Ahu8TVq1HjQEDniCpL-muVOlzFS3Ay1ZSQYZJVxyVKoIlj2xkck8U39xRp0rUW22r0XtXq9Llxvwzkpl6LhZQzpSB4r3-wnF5hggkUcqDlr6LiUWmi_RDyDLUI_pC80wyaj_GPA3qgSfRnlhT5DG4BfeoLqOYpzuZbINMlUwzRPu6TkGJPEi7we1GMzEjfIyl2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری از علیرضا بیرانوند در روزهای آینده در سالن تتو کارها. این‌بشر شده کل بدنش رو تتو میکنه مثل بدن امیر تتلو تا بالاخره معافیت رو بگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30221" target="_blank">📅 09:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30220">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0ywFHAwxftJZsYQ88xzEJ9RLRLNHkf7EJKZCqfah8DFzWs_pNDxm2gTrzasvw1sBi8qCH4YpYETFpxPSScHXMuKsume_uSDPMNpKxuDRBKZ1V2gDYCCj4KU7kHoyDjo599XtNIrF6RKG31aw9CFOuFOLzfx_LFZu4Nyl9ZkdH3clml81X_Zkonvyfb3wEXRQ9VqrmHcjMGyxMj53S77x6bug_HWtm1mhaUIseMgzjYk8CdjhIKc8sCJRNXI54BYldU4PknQzmSNDKfkCMjbmIBb1kK25MFCKwdNEQp72UwI6M5kXQwDpfE9HTdZ9EaftNZP6viTphT4W8jK-o2miw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری مدیربرنامه‌های یاسر آسانی در تایید خبر ظهرامروزپرشیانا: همیشه به‌آبی وفادار خواهیم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30220" target="_blank">📅 09:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30219">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67b45eb828.mp4?token=Y-78dDlxl_FQ0aiDtMg4qlY4a1gj19Zf6mL4sOWMnVD4pZ2qFOR3goy8222sJFx6-a4Ydw5oIE7bsKsnfmggte3q88p7W-cg6c3QZICXdkfstEtxYmngNNZR7r19t0NzFg4DSD4pcFNIi2MKig6VGKbF_3LPxsdJZChKP4BGVyaWdWeKvglvCnlYiCpIY8UmPtaPy3OW8e7BjG2eihSaseBB0fCINEFhW-OQF92KguxlyP17_DKOiR1--08NJthQrULhW4GVFT-q4jCBJ3zzAZGAbyiCR7FVoQckzWZOYqv8wvyJbJoUM7SdpA6mEXMbeAeDLOCyk48WtP7xRncmlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی‌هوش‌مصنوعی‌از قهرمان فصل گذشته لیگ برتر؛ رقابت بین دو تیم تراکتور
🆚
استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30219" target="_blank">📅 01:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30218">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEwkNtBgB6UJPdyEFUzox8kj6oI_TMRqv6B67L6nKUgNdocwHlCJglWoKN7t3ZpZgoL9ILcD8ATqusXFpqy0I_BgEJ_AzRwHExuPVlAPQ195cyIH6BPu2B6cqtdsky8ZSMLwCiUndqt7IpgcfEz5FMXFXa6Zyh-iNE3lp6WUKIuIzUjvbFxHAa5WPfu9I14KBqZGD6aAf6lvtcvSIFL6Yb84WtcSU__euZN-IHvUY9bPAViYBqDJWEOHRY1uRgKzN4MD_07vOR-_qjwx7ib4m2_55Uto-z9TJKO2hu-hFomfbBAteZKItdxxgv-p4kVcCv2mv6QFnK0zZ5JtvTbZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30218" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30217">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8PprnrHuUj6P1Qunh8ppUTWApMSOHpzLKuAYrTMjcFwskvJjqgGFG_3DN6VaFKGF1AM48s9dqnjc_vpWID9NXH8vnrQFjnABOkmnPkmmjqWmxWlYnuO_cZlWo9VIQRtOVIhLP0pFX1SDNmgGikKz8ggwxia6XeF9MtGKLmKbCtVTbh-lsBWNJRrUaUibnDyNjurBlnyJ4bSSpmfT5WUgqlzC9iaZ_Ya42g415XFTs6iKR7XU-lLNDag6ssfKJjvyY758j15DtIy0J1mxnk3XP-li8wqa1pbe3bea-JHeeXg9idgVEelQvyZ3Xm9lrrIOglP-W49PI3VxM1T10YXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها: رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30217" target="_blank">📅 01:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30215">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30215" target="_blank">📅 00:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30214">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5c924093.mp4?token=kVacGnyS4ePa9VhUgq0Ql60zvajLbpOElM7CcgPyxQGDivrix2y0Af4EbCuZ7fUdzDsPCbRIeLRPd2_SYEejVxNbbZ_H1O8q_bO4aoiR6yd4WytGocTSuiph69rGtuyMhLuEv9wRu5V4A8eMZI1uWKbTX8-nmesnJODvH14zOOrtCP93SkX3fwBfWUr0VCvML4dCSa18F_aa3L4bQnAXC_ykbJongn7XS6w4MImUaKrEvzuPYy0hpI4L_C4kiWc-B662R1izrdpFlMDW9vd96X3X_D9XFmdp1OAnXA8Ns_7AYufBKGCPaFVcMHIXR8HL7eKhUV5-x3g7vpAf9MvIhLX-pAG_3FjrK7Nn66017ehdpHZnIi9k_wGE75JAJh7DDDKyJgbCR2s4ZZZ5eR39Wcoe3scv8kFQrOlGyNcgXFv55VqNdB_Yd8vZCh8fJr47aCgoH0YdnIJUj_2sajV9lAkSPB69ully5lf5PzYQNYV9Ps9vlqechqDRDtNdUvzydqP90L9Py7RFS68l_JMhmhdZjRYrLswNlT5kTEb-m2V2H4lTa6N3Ve3-3qMUtRCI-2Y6cM8zGDHd3XFyhiqGe87DhBtFVmKkFAqqyXmLh_-bYTn06yGa1SGemt_rYektlyHi4FVbFPzmTRGEvroR1JCgQFsOwp1KC4uQmWhGrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منفجرشدن عادل از حرف پوریا پورعلی؛ عادل پرسید مهدی زارع تو حموم چرا اونجوری شد پوریا گفت من و مهدی باهم بودیم که اونجوری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30214" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30213">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5iOohwdnf-G_mYVgJRBpgJaUPLDFsIaYS1Z6Fln5P-_hPiAsbXJVAJLs_AyZrS0H0rgkm9H2g69-are2oOSRCU_GTSitu76yQXRsfnrKq8m1VtyFPYmv2acCWiinKVxJmI5Im87nGSenY8lzfQe7686OJfZCjHEtUHikad2uAKzDl4quXsswYJ_ZSnswb74u3pb1YeYFgtYaYXEru75UUJGCnPVnwGsvR9Egigg4A9EOOXXinf2Ftktr5oF4sSssvdhzl0QYFPLcSeV_JkMX_opRfKFVEJlxMJj_kMUG_nHVShaimsDCiBxMESORq_ss4zBsTPQKrk-cmABTFdE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30213" target="_blank">📅 00:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30212">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8W1VLChaLGrKD2_Y5sLsL9jaZnfqcZjvNTRjK331rjw7xZ2jDEm6DdlKk00fPgjyr0KpjaI9TFE8GuIexIDNKy28_hAfcAw-c636oECLjQgJO37K0KNSIOFtcS9NKRqYjWHqkacIG2btyaLu6ZMSoaUN2OGy1HQxp-Vkv0xXC8GvIynLMSHCNO2F6sIND8kmTtVDwvCD3e1Aa_pylEth7n21DgI7KnBDW4Ri_v4C16lk3wwO4SEsX65Hr3p_pVomzf0KIYQ7ybQKK_qXIeaZlK6h0rJlHunrZMAmwvV8I9d2Ffiiagmvge_7DCJumS5lM53E-n2CDcA-HxVXQC-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعید الهویی مربی‌تیم‌ملی: با اللهیار صیادمنش در ارتباط بودیم و قصد داشتیم در این فیفادی او رو به تیم ملی دعوت کنیم اما مخالفت‌هایی شد. منظور الهویی احتمالا اون تتوی شیر و خورشید اللهیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30212" target="_blank">📅 23:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30211">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9Iu2H3gnLgLov0a13u6c5tj7mjyWr7bdfAK6Aud92uGMACWy3h-uLB0qt1zF4eQSiJwTuVd5ojGehdlehlfQyP-QPFwpV8pqu9BJeWSjFwUNAFgplhRhn5g5NLm9SuQq2ZOBN-1PuU8bKaFTPIKEnE4CpVm413TWeNH4HcaJS5dwYG-MZrIIIHTdyhE2Y2LQZxJQvIe889mYQ3wdlHXp4RUoSqZtauz-gewslgJKl5MchIQFvU2dGLbBgGCenJvriDmFKgfGenUKck8SPmzskHSz56m29p78HBIfnVyebv6Kr0tIGMT4dkP3T_dkBEDzupFA7YuJWWrlhlwuTpStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30211" target="_blank">📅 23:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d4ab1809.mp4?token=rZw_hptfWEmFIUPuZGzgRzb29nhKQaUX4QZ8oarWZuD1ZfiDp1yoD9l8FOi6SPuTFS_gARdaC83roTdly1qibCoCNBsfPIYjHrgoezTQRiVYI1LI2IRLEk3KuCx5-klnOIJKBszeIaa1K0nnszL-aKtfNzO65zxZf00-c-n3pukq4PyFuYOpeAzAsCp7Wa-_IJe0KDTRGYut8Ow9ivq4CTWtzUUNqJk60to2Qijb0bt5Tm6HoBSj0Z1Jvj-_Ca87Qdwj1fyyGB5VeVc8TSfhqY2Omx9kcjep6Iv3pmwB4u441JFXhJGnVCMVhZ2ZZUcSPlilOU0yo0O5k-JKMFH_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30210" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30209">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=seEdeI-y23AR7H918btR9aeeikm5d8RXfdeEW4lmF2mSDqY6rbU1QXQW-0fni4EUN3I7vPaMMCvNQFaLj7mFOGQHNBhMj-1R8ClctpMuF4k0B_Wyu8BRUbnm2_8n9i-W1BJacZBqXqlp8KGeVBxc-OVnZ8wL-F7o8EKZq9SWSSCuDDuYLQlNCcTDqmP2DCUzGwjvGYvGFxPZJrgQTH6vyzTZEkLiE8iG7sKSPx6NIzGTNi7f5fuApMbDGDo9_vAa4CIWwDAw7hJAttQ9Eu3uJGpzskl2naHysTnUo-8Z0Yr9IQYSkKVbXHmgv9GciZ5Jzgj_iM1olO_sgDb9WxYJtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21acb31ef.mp4?token=seEdeI-y23AR7H918btR9aeeikm5d8RXfdeEW4lmF2mSDqY6rbU1QXQW-0fni4EUN3I7vPaMMCvNQFaLj7mFOGQHNBhMj-1R8ClctpMuF4k0B_Wyu8BRUbnm2_8n9i-W1BJacZBqXqlp8KGeVBxc-OVnZ8wL-F7o8EKZq9SWSSCuDDuYLQlNCcTDqmP2DCUzGwjvGYvGFxPZJrgQTH6vyzTZEkLiE8iG7sKSPx6NIzGTNi7f5fuApMbDGDo9_vAa4CIWwDAw7hJAttQ9Eu3uJGpzskl2naHysTnUo-8Z0Yr9IQYSkKVbXHmgv9GciZ5Jzgj_iM1olO_sgDb9WxYJtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌جالب‌عادل‌فردوسی‌پور به برگزاری دیدار دوستانه شاگردان امیر قلعه نویی مقابل ازبکستان: دیگه پدرمون درومد ازبس با این تیم بازی کردیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30209" target="_blank">📅 22:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30208">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxQ0ZYkgijpvYN8gQq2KMMgheJAVIacQnOHGvIzR2f8pB6OPVsiTf7RmZLvZy3bnqexHmT57nI99DhEBAZwJtoAqWhZeQY-MTacgy646ybdcAoXP1CCVyNxOQ8wFeENmCc3Up-rdXggmjUOMYMDf0ITfEQBgPgBmiiGrwgo4vFIuFgYMISuBkK-gkXFNRn41f0MjDOOGuzU4oW2gQV8M9SywU4SYOlONa4zpzKDXvfZNDfWEPkQrv0RgusneNxia5n0fg5BVfpMte2OSVtfd-f6ziCIV7sp-4lO5jfdZ06VNcc0ST8H00YllmHYOp3STe8Mjg0l5igXYBPB8lN7xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال2022دورتموند هالند رو داد منچسترسیتی سال‌بعد منچسترسیتی‌قهرمان UCL شد. سال 2023 دورتموند جودبلینگهام روداد رئال‌مادرید سال بعدش قهرمان UCL شدند. سال 2026 دورتموند آدیمی رو داد به بارسا، یاران فلیک قهرمان UCL میشن؟
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30208" target="_blank">📅 21:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30207">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3VIk_G8_hRdrLsSxifKCP20kfQHR87QY7zwgj5VH7zMd9F0tR241Ieej8Y991IG--HPoela74S1Lm9Q9CPaqHH0_ZsFGDEvklvVwOKv2hlmR0ANxGKJcYnQwltyu0lO3BaNb4El6H5y6OSeADH5ZgsiSZzRr4coo5jXZ5bTWWwIbt4HaYoF1h4e-VHbVIFzHMLwvtz0tRBtm4R0XrbMo_wbwpjdNrCnfYbHXlycC6b8lcnx9Un5E57KG5Pu1SbQ9x7H3N3tn0jHOX3zPKf7Zfu8R5yVIgXLydRabvPXihUtWuJo9ADr795_8XlSk0I2_t7PD_KwZd2nL02FkfAnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30207" target="_blank">📅 21:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXWEZ5h5RkS1oScG05Humf0vhaM4-yW90gCPnJQRXdVh8a3UJ7zW8e5VderKfAy2zhuBCnxnnbNh3upkYogaNsRuYxnE65zNf5Zlvde_fGkoOYnJFtdlU7UOqkc5004cp0YUYRFKWzqNMowtIzbQ6I05m52RUkj8LqT7Nbe9FcNVpiyb5KrcM4hrpEJhidkjEfwzn4vei21jjUkqSo8Pk8JgvcOsM7WNOtTiByaDCNL9UjwfZqvVJi0lBzTp8bMwY2XLqyijx_IdSHqwSFJOUMpUHB7j-SkzQtiIIndnt1np8E05W_z-DQnOEDpa2NNJUvjzHgS15V5AgOJU6EiT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-w7hhQDVdhBLZHm7UGae26nYi5nZySGv6vsl1uxoEYWFI9F7zTmHlp2mw3V0z2rUN5gToFNrP3eM0RGuvema8WlcpaXEXwMQX2tj-DS1EIV2D_xfLuvBwFuCVZ4Mk77nCilAeWW6HHQZEWezsHry32Yg7H0JH8gBaIutjq0kFd9iRSmIK46PwXymenweMEWWzuLTG3NsWM7qRKUp-CY_cYJPKN5w1RWVJXOGof2Svp5iK3kid6g5g7f_KSzXzXPDU3U_McDh4aOeE2WLg1x4IynFV3PFSKHcU0ab35q7YHOBQEfXy0wRdgnZm55BXI1FOx0WOOTncxv2yAFSSipqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtO2v2p7Uebg_UYOnR8UabkAAX3YUD8S7mlV9lV0EtA5fKn7QHARBhiIw3BkfBXOS-ZPP2I0zQ0gsfYoP8WHd7LYKzQw1kXkYEa0gkDykDT3hznOcZs5razZKX0Vx2S9mfaTPk2kM3NRWy08sTZQ3lvx_7yJ158PqtQnWme3L5AA4baU4DL4aDX59XJo7UD6--WvQVLXor4S64wxMPgC2sCFBb_M0VXI51JS7pUoZ8k8ZJTVVHeyY8CGksThd3myPXkhELqgUJZvcbsR-3pUGu9-PXqJe-OwufCxJdQOMrQdQN9KGY5DxZ1TOyIYksBqEg_gpCQFFIZ8XYT_7dW9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OM-R5Q0DznyOM3TDqshpoe_GlpBSLCXCdK3c7jt7_KyT6c9f_yOlgOLj0zULXcaS8ASsodkLwpK4iMJGnJA6aB7rvDJLsn1fvba2wDFRsanN3XumHd4qOXUoFoOPl5TE2vxbNckIQy8m3pDC0qFjR5uPe0rglxsx9edloTv7jDmaVoMZA_2AjHaqfYBhEJw4N9n8BmrOy6IbiXHnOMDz_zBGIIX8KrjTnNZ_NQ4m1lDFeMZnkBqeliJArYXRKxaEMIGFBvpwDAa1pftz7JSIJhOYnaePMuXM7UiMXAApSmp_bjiV13-dsHsYiTUqDIp2X-w7-kLoYbdm9OLcYZzqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcRZ01_-A_mWhOe6BeKD8ZH1D2u82vXhTTXBmSfy4yHBB0tHBzuz-CkOdrj9cAWWAQ2HvzYogT_KXw22SdyoEVsARU08soFhKtSNlSlUYhYzbSd6zFC0S5NCS764gNxUoZwf6DNJbI-7LS7qmrASCXgFfcXjyn6sXyyl0K934GdArgK7H8xvQpU4LATd4Wn_qkmicg8tDQiCSfsPsrJLA_8dm-REMugrxZk1XdXxlSjiGNfiZ6mIc31XQ9ExueyIS1INILKHnYWGFBNgztzR9csWD-HXzkJi770-qnwY5gEBQgORBTzSDend1sY6TUQ4iBVxMMd6I7z_vVrWDaKmgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vilQnevTIGHlENHStwxEoY4XrU8GWjOZXmIKXVITEQ7FEyy6iMaS2xvYgJ5HPWdAHTUyvyaKHneLw4MkEdAT5OsT4B4u_pOkKe_3gaCGzLayhwQ5hjNsgx3fuPq_P7HgAe-qMebS4XQj6s_jxnz95-QjtGdvht9HP7eUOlMNEAyqiaOqKImfqFs8zizAQULcy63QKk10I4ungKAabxQD2qk_WyHsFGAYfo8lZyxWFTMWTz7CRYEWW8-xbMAvj-qFnUjOJsB1wmTAGwW1SchDOrtknYwEaCKB-q8KxLUW78xydk0O296V2owiJeNp-XM8URpQE6wZLCWpTTVG_tPxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yct5yqz8pRkqFAVC5_TMK7u25_9Pc3pPZ2i7FJ4CNLxmqTMnwxbWvo1PwT-Var4Nzlbp6LoTnOirRPyKBqP539-4BauDMWMQmTP2RJj56Kojyia1uC6DueqN-UFz1tEov-kaEmHIpVs8aASEQ7nZt2-a_yMGOLgu0LGZyE6GrhOZr9HvPb1nyz7GDmkXfZsnCnlHKvu2EYcBv-Y6_gnA2mS4mJlHz0R2I71ZdI0w3yLhHqAslu-4mhY1v2P_0rIOSM2IJ_TtTrI_w1CxFDIa_WmmBDsoX-LarLKGshLtjX5--520kk73VOIxFgq5QIIUUbWH4rNoteBCZ3rWG8XkEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNHMnuPZ85NZPRm0EdX7vTVasp0pJOL4xAApbLMTYZEkAnAnO6bGGYGb297k7kMMr-TqnGuUQnlLWTezQ1U8F7K8SSlixqkT2abpCAkNKgf_5hrw9HtWj7_ZBZwcDox264imhA6dbtoZf4qDIGAAJwdc7y9iluLyQwsfa0gR89QIATh8nvMX7RfXIgFfQ84xeqAAERwJmH_2mwMMCveCgJ8x-6Z7oUGxc1IWo8Qr7ll29ZgnmYkQXniFpr5UUDxM8xf05PvVVtQyReAT0nzyYEApZOXlxUhh2JV1yIJ6Tr749_1MmvcHdVNyryVE-wfJLHY69noCmISgDEyixcp8ddTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IXkzwEx5ni6QuU29k116kYR2O6h8m3b0el09VoZ0MVOCRFhpK9MF8eXypOIkIQRluq77pU-sK87s-zz22qVTPbuFRbZ_D6DXu-XeUZlD_M6MTIAR1aqJCNzWwJ9jwYsBAFiXAIJoAGXp7jC9V0ao0_Wn23UA1Qs-LVVOiDSMGZ_2jVQRDSFlE3REcQy-cyOGGEAtIH8-0TfHNDs7nZeKFJsp475J2LiW-abrRrMMLUB1uAPLW488-HR4Z5PZmNjAWi0isFn7iVLcNp5xOJsnpufl3UmmdraIpVRMW6rrnIY4tQ-QaC2X6kL2WtepMsE6_teUZ3yMjed5LbGSDq_sNHMnuPZ85NZPRm0EdX7vTVasp0pJOL4xAApbLMTYZEkAnAnO6bGGYGb297k7kMMr-TqnGuUQnlLWTezQ1U8F7K8SSlixqkT2abpCAkNKgf_5hrw9HtWj7_ZBZwcDox264imhA6dbtoZf4qDIGAAJwdc7y9iluLyQwsfa0gR89QIATh8nvMX7RfXIgFfQ84xeqAAERwJmH_2mwMMCveCgJ8x-6Z7oUGxc1IWo8Qr7ll29ZgnmYkQXniFpr5UUDxM8xf05PvVVtQyReAT0nzyYEApZOXlxUhh2JV1yIJ6Tr749_1MmvcHdVNyryVE-wfJLHY69noCmISgDEyixcp8ddTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8DcrN6jjA7-5XIyOIWmUUNI9hUQcke8LNDSFlYEAsk_WSDO8cghxxBvRYbDFApXzEeajfX9Jk0O1IIHCqae_8VTla9Ri81o6b80PH_0qd8IHnXinwvnsdMk3ezEH84P0JVxqcLpPSPMbl6kZXy3iYS7HiMMFwbVCZhMggrJGKEwLpBjX85VCzGNwcEYe7mGi74RUnAP_TbEGibm00X1LWkiXUN3b6zodA29538qVSObXykg13hWRvSckz0lSKTZ8-nFZhdfzUHN1t1f6_p8gQQ8mMgM384CLpOh-Nl3RgMCSJcyYychibUGOUNBZzSkhmG4pcEOPBJWs9PFyxAAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSYbQ-uodxl_lzt_nMKpv-Ugh41FdaCjQm2G8KyZJWIfH5r6ef3GgTXCaDrE8T4hrf17ko9GVt3_qmaovQDhUZDc9oIM-ySKwkdPw4cQIG6v8I4vsbPKTRlqs1EH5gSCcssOTPXbxp51tYAdAqXjfXT97ekAFm_Q2W98mQpRi1gEkPfp3ZgIsDgTA5QQhWYkTZDSXXwTfT4uun_lEvdFRgLek8V2uz0fvrw1aojg0NYSqS-6d_R2V2qFq2H1Pk5F5w2eZw5hIyXawpqP8_17KwX68titjGT1E0TFJJZ1f_nbnEAQrOIWeUyfXtCLWff7ZlPQ66pMAj0phWKAc4ftnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWF6Dw_2mJZZAjOncHkstBETezk_ydE7g_7Os6CSR183PsXTj0iSuM721L97N-Pi-C_YGXvMUvpWKLLsTdqM0mG1roPaQkjxK4YPnMqrhqDVcyU32FRA-hQ6w7vJoTt_Xzw9gOu6mOxYZeIDg7_ee9K2tPrxYOWVpTuZye7AbUBiuGMTJ6R0gUj4sOmllmagHfPN05wAx7H5ICi_D1HLSZ_i0LHtbVeSfPmTTo7NMgJM5PGxk4rHCkXjvBhbGgC3xlJVz-6prYatpr8KTgwqU9b1QEhmsXf2SUKt7JljPB_njad1WLWDAiTIdzLWfrmAQUOc33Hu5r_j36fvs7OuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRUBC8G16Fr06B6OsaDpyQkqELy6PTh2w1qLhuMOCfj8r63qOT8GnclVw_BQgM9E5jJvXfWoLtlKCw4aVwmNqx8-m-BYm6AyBMSgg5FfCD-x6LV37H5Int3aC7VaoQVpclCaTvh-7LWsam1I1ZTQDPn0GYcfEfHpXkFYfscIkZW4H6sglaEhKd-P-sxPelZTlFLPl1t26R6lMAafKFccDZRxNeVhAp793UksAmn9s8QwkzaTibO_LscjbdphpMuZ1j2mkk0R-KAJBL7T31RXd-uURms205l0yzyRkY8h8_xbtGtAuOGVJlue5Y1U29oFenVbGwZLyM_EjW68wH-iKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=LWt0KrtEw1dRVcCNAiDS4m7ImsZPklGvpsQ4b2NUD9gnFJaDuRiF9D9r8eaQw7oAY7sUuwD4ptt0IEme62ZbwKhgL1LPZL1Ud35OXwO2C-41PcmbYwgA6SlygKFtLz9gDdlxzR15OaNMLDQeuSXwdXF1_QHYN190c-oUI57UUlbe-zlle29iYgf8aF6NKGowFMGnk4HW7qk4xnUYT1sBPmDWERpNYSSdaTtMBf4dhtRDHcc9j3ctfzCGT-ojEgczmQ1zMJ9uhYShgkk14mQ_vTFEZGsVV7IOINIzxTlc-t_7L5aRJJQ31oxcIsNPOi45jJ8_Mp38WuRoDxxF614fuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=LWt0KrtEw1dRVcCNAiDS4m7ImsZPklGvpsQ4b2NUD9gnFJaDuRiF9D9r8eaQw7oAY7sUuwD4ptt0IEme62ZbwKhgL1LPZL1Ud35OXwO2C-41PcmbYwgA6SlygKFtLz9gDdlxzR15OaNMLDQeuSXwdXF1_QHYN190c-oUI57UUlbe-zlle29iYgf8aF6NKGowFMGnk4HW7qk4xnUYT1sBPmDWERpNYSSdaTtMBf4dhtRDHcc9j3ctfzCGT-ojEgczmQ1zMJ9uhYShgkk14mQ_vTFEZGsVV7IOINIzxTlc-t_7L5aRJJQ31oxcIsNPOi45jJ8_Mp38WuRoDxxF614fuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1F389GQo72_TNEHiBg-NRKwnNo_1e6-gND_mcIFaIIhJO5Ooh_vHfyU-2npN99vN0YELygqSDp725Vz95WRai5DP_iZOu1lckcnJzKHZhN2Z-LoMuZ6_HMmLigJGAFTFb89CtGIOWsGT5SaDdmrkto5nyta44G0sukz9sl0Fmrm5ga5w0Lk5fLz0t_RLaaH_FcdpmRodICe7PbsaxRApGwrgUIZgnOlHMT-aR_p734ojLt-xj6YNU8TkfEeUvcqb3y8UeImylxbQBXXpe6WL6XldPSUmUxz19O5PGeZPibYPyY0lQrtsjxLXlpvgGyP9eMWowgd5skAPd16x6YRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=ARKazdq48QG3q0jRp_NqxL8oSNa-7EZWcY5uSmtebYb0CLazAirs8xj-iw82OUU4rFmBmmhPW-uvgTG_aonYrKnrmpFjKysEZP7zYd8ZqHwGG6CgNZ7fKV5gcuHE0wI68SvWTl6PwVBtTibqmKFvrHieMZ6Hfyl2NsEIPfYUZs65xZMC469FPAn9DiPq9PJBwtvXo2vj2TF7F3rPF4nuXwrVJS7ULE31BYfeRwL8OBV706PoSxloQtvFY2ZNALaSls67aRScct60rfEdOZL3ofGDiGIh2zxMkn6HF8cxXNIcjXGI3Ats_IZwNUvozcoMq1m08gjl2KrRYrR-NqEsd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=ARKazdq48QG3q0jRp_NqxL8oSNa-7EZWcY5uSmtebYb0CLazAirs8xj-iw82OUU4rFmBmmhPW-uvgTG_aonYrKnrmpFjKysEZP7zYd8ZqHwGG6CgNZ7fKV5gcuHE0wI68SvWTl6PwVBtTibqmKFvrHieMZ6Hfyl2NsEIPfYUZs65xZMC469FPAn9DiPq9PJBwtvXo2vj2TF7F3rPF4nuXwrVJS7ULE31BYfeRwL8OBV706PoSxloQtvFY2ZNALaSls67aRScct60rfEdOZL3ofGDiGIh2zxMkn6HF8cxXNIcjXGI3Ats_IZwNUvozcoMq1m08gjl2KrRYrR-NqEsd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzkbVsZslMWO7S3JeWctC3iQ9uxrXLB0HcsTbriykqs4795hW4_vlAcz1Pm_yJUeTCDjooC_vF-EAE4YXMSbsUgtdNHrbp28BdqqdIZ6kgBvvoSzLZtXKD1Ew_sk-efdi7HnG4zsmPS80txGUczX68S8QpvjCdbgxD4pm13vVOqojBruI4OIqCbbS4kRVJbC4nDmRTqv3uRLbxuDczZJPLiXl-YOmu5YpF_x-MwPo_rMQP8tTmIUeW_vi6Kg64kA-5M7txGPI_qd0cQz4egXFgaHE59P-xISYDpO3HnrIVbg-RYzHrecKui1AU5qpYGCGT7fYDHU2a-ANUbeCWv5eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCbmlJ_BFViEein-E8GAypG1MFM0iKREGV-b09PNs3qmYxQs5ETZqHvX8b5mHuEZrM3C1xGeCXbS31uDBExXNkq7ylpHvq4fiyQthAMSn_ZeJWcTcsHJMjvk1_qG1yZtDGO2-nIG6wG6n6OCgUzSOu3JMMeRQ7dp3_F7aj36F6o56NiacHaNEABEvQQIgc32UuJQP5IkiBU9-WdfU_r-zpq72Kcsemv5o94gMWatTWPuWt0lOalEijVd3MtCwPBdR_Nr5LL45iCUXMA_GL1yY3_rKzFfmNMeSWfw_yJLKPnr_iffhUbzLAkQlgmOteT9QurfmEuUUO1mqoC2ijycnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCiUyoBNVVsspDwxKYJuNTMX0eg1ug_f2Mxq1geuSqJXXKOukc8-CDY3xKdMIeWANwDdIB6NsQBqcpncpU00pWNIuCy4xhxHNam2jnBtUyL4MYoGwPvH_i5XbzCeNnzyk_vsAg2RkehnXn7d2uFHezb7sOasFcAetAMylhhi9CYY5tdmLMil-Q3tE1h4RZh1bpdMo-LyqducVZEBdUkJb8x5ETZMNabns3TItrWMUWdRQ7xx1vCjUdLlsJfT-gU1OBNIragn8BLafpqIefSh-SdZ0-DH_oVqaazHmCs8KOwyv8vlYt9IzDys-cPuYwsP0Td_R6eNOXe9FL11YIpokA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h160QcIWNJCmwOtQw_ivS5zVmeFLgyoYPvY0nznjqv4cx8gaCppQF8R7N1PuF5RPsTVRDL_gCKcuYogeMxpyV_lKG8MmnLr7He0ATWGjK9L0aV4oxmNL-hx01mJ9I8Z6ZWE2n8kZ72B8IvkEBgnMixbaspghIYo7uXkcGBNM7WvokKpKab0l3c83H-6SVMDJtPl5uVI6ab9-wcZAOsvNwJqWAk5PlCRriNy9PnFY8hjOU3T1HCzIqNGGVa5DJPaFhRDZBw3lONoFVUlnLhcTm3_EK5T0eZ1FZWlY53AFuYCxJG7GRO-YyHgB2D9cg2d07ZvnSDuiQSiR-Gv2s4HS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKK6gq-C50Az3QvrZuhbOu-Fo-msZiVb-6i5nlkuO_9odD5ZadmCf6TD9TcueeodpcrMkobxtJVfSBc362pub3N2yPb7YFTz-K0JS3sLbXI1XyIxu4mAu8s6ACt6s9-SpjxbSLfQltpLVB4e3-Zfd7qqpWyCoQG5hcdh4Sk86Cd0LG008KNlKTeOTIbAZfoLwR__6rqlamgqOQDJrJb7LUZbUzO5Yts6lfMh9jmfpCMUDewX7FQovoC1JADdwyysGnFZDdgoWRfypr1a6gY9TTNYXZozAu3P1v_C_uCwbPKb_b1r_qYIyhxUrHu0eOoBruY5Sk5H-3xLAVZZt8QHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpZZEreBI2saSl_t3pDztJy8VJMG3r2jeOaT-aBjvnCy0EMdB8AAttK1XnHr0Sxji2uBQI2bz0_b-NqpeOwnUswASoB9WxxBl5KamJqVOAzHA0nCT6EC7nSiC0HTDS4-x8Mt0g6LFHe9uSNB2MK6vlKaJF13pWQuM1cZmBFg9QTzejkPmMH7MY16JOAtMAmedAaXv4e5Mg9cWLNwR1Myl8gPpWjA_Nh79dXsenqHLrFGA28idwpZ6PUM0Su8vifcbmOoXp68O4FRNfQ5LKrw3SHR3bIXN417sKAOkCJGh89PmPozDqzDPqOeDedM-cp0A4oIpqfC4Osqx6SWOhWLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzavkrW0d4QUyln4wYCURcJ4foaHp8oTut7Ghl3PN2sHPvvPkYbU8rkDmK4Wsl7z5cKdIgS3CeqvilqC4Cgu0CPrEVCCCjXPomUoX9_09v3JEmFOefW9sycBnQhls0GnlZFEVUg3F9wLE4MwXTZDbgpdHPuKKE_4ccoUCfYZVanv62pqodS5yM_ZvJMD_j-MZXGp62MAuI5pvAXmkNYnCJldk42cSjH8nKsdfmDrfraGDceGmNeVqYB-h7Zh99b_PxFjsMw19qUiZSimwCHjJE-JOOFMlo-iybpyoiqc3cFA4VOst50frHnXNb4MDIBValUjlfk8uW3QzRnOzUxFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjtl9AkPLZZA47yxHl5DdZigf4WpFl5htY6iQko8nWOOPe_TeARE9y0yLyfQRYxoooMCvGVYYAF516-34MbKS6zZbW1eSRAdPS3syJT7XLQ3PhqwQ4nJB82jxE0Z-oJMgXMcfBF8J7Isa3fR7QFihbYQ5ZI1L0DikzuCGrA9mrvsZMMo0ESHuDOCxvjz-odVbQZOmCDLHkJxlR27WD-Kgni58BodgLW0Rh4X-GpzD1sCutxY_eBlAI21oTrVVodngrJHjjfcnjsTXjB227KKMEqOX_AtN42FqdyTHL9BFOQZSd47kFNd5Y4eJTAQI15nMQJIL46e1LRHTB761_1MoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBncGgBfHIlzb3Eves7CE6VomGOLCNA3yLwV7e-15DS36Z8uSibmvhnjWineTjcO7lY28cqF_O1N2hmeQapMPv7A99Kyw-D25dY6NEJlZQiT3fLHLLl8ndm9IwZN0ZmqFoYXA69l4dc1COH-vIg1FmCFaUwmqtRhEfQaqN5WnAt6gy_b9XncTXPROFK5oB5eFyobwmJ0VKAiegI9X8JhfQswPG8jKa-eFX-2KJ0A7Tv-g1UsU5koFWyE5BuT3_K3Bl-QiInGoVVmRVztd5gStVgeKvsaI5uIHwxEt-Gq8wE5PUajMND5SMHFhrkUd52vSNwNWBN8CPOa-L2t7ntKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHkMIaI7SxgbY-GVsf78chHi5VUxADwM3r_ncIMX9GdOZd5xkKHqs-UWLViD2objTqQwziZx6rvZj8LW5Mz6Mefx_pfDswZ5jj2ugB1EKK03IQONQuqJA1U7iZ8uMYiL1660hkF0bePiv5RelWDU_Lpz4QTGj-AjpYFm0w4tYjanm2YsgVIy2uZc8LUSVGBzPX9N2u7k3GXAFIZuvekIZ1Y7lpiVB7_TklTyLy8mQSejrPKyQBapBTTWMVI7JHDRc1rDGwJ9oZ_1Z6CAvhP-Tugdj2BOEf2WeAsdjr_Ub-kkcMrjjD6nCQjA1OzwhkfgRk9if23dHnXTco9n9h_b0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=jtf2pvm7n3dWqPVJo8HStTHGxhmxo9x0IWczLm1YwmsX_RdINs9PYsRtyYngTcwkNQ05aWtF0DVVdyM8oWAGWJ-ORfh-XQduBf3GZwiEtwzjq1l43vrrh6aTmds7BIzRhyn1Q9K2V2W7ImGmzP7rqiwMKTZnk13jNRu_WkOw3oebD8hbpA-ec8aq23r7mCkrdpEBt_n1czWCempZcpOzJysjx_j1JLnrouJenyLkkUTnEk02MP2ElVIEnYgJJzWAhvpLBjOa54i3ac0MLqgAnPw-oOZClSBvq-ZKdppN_wHc28g2CBM8qq5tpIZdcoxNiMoF2UR4Ia7LICggFxevAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=jtf2pvm7n3dWqPVJo8HStTHGxhmxo9x0IWczLm1YwmsX_RdINs9PYsRtyYngTcwkNQ05aWtF0DVVdyM8oWAGWJ-ORfh-XQduBf3GZwiEtwzjq1l43vrrh6aTmds7BIzRhyn1Q9K2V2W7ImGmzP7rqiwMKTZnk13jNRu_WkOw3oebD8hbpA-ec8aq23r7mCkrdpEBt_n1czWCempZcpOzJysjx_j1JLnrouJenyLkkUTnEk02MP2ElVIEnYgJJzWAhvpLBjOa54i3ac0MLqgAnPw-oOZClSBvq-ZKdppN_wHc28g2CBM8qq5tpIZdcoxNiMoF2UR4Ia7LICggFxevAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=kgowjpYmKrNLA4N90qlUSPed9wxyVI1cTZZjzG9KbWwzDlmZHRM4W21ReZ4HVXolTqOPvf-QiFgDlIG6txKo89tBrgkeJzNyWxd2FvuZjveHM4Y5gixaAEWp90HoqhLNzRV7je1eMM-72NPVOyzOuNiuFnhA5Z7LKJTAHn5ebxt5HvwIU5Kd9c4wWnpzmCawIvYbFkHrJJsHK96dww5JssF2fEJaR-nFmSJgAjVkSenyD7nYaHP7ND7qWnZpLtdmxvMZO7Ls4y4nlp1AWB1NzrtSO2OtFKv5CG2YVD-NtuEcltPjnPWPOWP_pzd2U0zR2LAk0ji-IY3iMAQv8CFPeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=kgowjpYmKrNLA4N90qlUSPed9wxyVI1cTZZjzG9KbWwzDlmZHRM4W21ReZ4HVXolTqOPvf-QiFgDlIG6txKo89tBrgkeJzNyWxd2FvuZjveHM4Y5gixaAEWp90HoqhLNzRV7je1eMM-72NPVOyzOuNiuFnhA5Z7LKJTAHn5ebxt5HvwIU5Kd9c4wWnpzmCawIvYbFkHrJJsHK96dww5JssF2fEJaR-nFmSJgAjVkSenyD7nYaHP7ND7qWnZpLtdmxvMZO7Ls4y4nlp1AWB1NzrtSO2OtFKv5CG2YVD-NtuEcltPjnPWPOWP_pzd2U0zR2LAk0ji-IY3iMAQv8CFPeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30173">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YndWC9RAc1qbmlFNAIKoBvjt_tOouJqaBTuTAPzISaKC0SY7OiqpzXxYjLRPMGCXWAl91oi-T80GlRz02uIZ1-1jJWlKCb5kqCFWLuD-mYXV7M6Yzw6KLZzazX6fnNBdQnsZ2AX7rkEzkAx6eBghuzar2exSPS13by6120hI5UydAzqzeMMA2a8v6Qeo4sKS3yB0Lu7vt6ykZTj1o2z253AOkt_8oDfWpc75ZUXKchdVU8vSEQi2xv3qBtH50iuChA60sObe_pSa4vb7OyN9qyt07rh5EiYGDzl-EMjJ-H8PYn_hivoX86N6IxyVUlWzpxa3wxWTU3xyi0g2kUc1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🫰
لذت بازی های کازینو با 100% هدیه خوش‌آمدگویی تا سقف 100 میلیون ریال
🎮
بیش از 5000 هزار بازی کازینو زنده و اسلات
💲
🤩
🤩
🤩
فریبت ویژه واریز با درگاه های کریپتو
⭐️
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💱
🤩
🤩
🤩
کشبک اسلات ماشین و کازینو زنده بدون سقف
🛎
گردونه شانس یک بت با هدایای نفیس
🪀
هر روز تا 180 فری اسپین (چرخش رایگان) در یک بت
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30173" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfwlFf3VInbxbaWUp0g4ojgPybd59FUcsjOIn4YlmE83Pgo5dzJW4aNLgLtTWThFAFRgTxjQtUlkKAlRJrw353dpiCC1S2fJ6j_GC9s-1ja9JuFSpuBTkoGTDL7A3yTp42CD7ME3xcuDxmt8XxFxf9IdCctTkYHUo0qj7jfUYCTs0HW5qyw_-RZZ5ObwbDxsFF5ru_pkgK7Xi3SMyqlXvyBqSlyz1-m452Ku8Pi5s5QgdKITs-QDvIkd8jflZCb5xABTv92oHlCZxMq_KAOlPH-AbXHY1Sqfv-uBBhYFZ44urttixyqWnYEMW9fC-Kpzp4SqtQ_OpREUylDkPvtr9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqBAe9vl5xlq3wY_CfqL8wbPKRlxkdknb7O5T0uxE1s11kih5-MEvTQAFB5uGJyych5BiscsNNKDl0w6Ox1-a47fNIyPdVMsSoUJgY7fsKNjnFtWabqUuYUVpL1gYo21-US1zigMMInWWnIIkm-7ftZ5YhX-Xo3w7TN4K7oYSCfnVrC58iDPI_DF7gGfBrCIl2RB-ybCsNY1uvTrEOQuJUqITa0hxrEKfQn2PKgNSGEILzJYniJA4Yb7X4H3jgHgeLIWWGhiEfezB0LOM7T5la_iorHN_SDqH5hNoNN5xhc1mVUzwHbbHGt3ll0PLYi5J8wG9IsAdB-weDLT0hfGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30169">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kL7rqelWrfKbcjiGet8LQrDQ9A6Iz7Z638y1NRR0UajvW_g2T3wnS5vdvZoKYFJhrLn8Xyg_VdxawiK4TXxa16BtYFtuAMZMuJmkHimGdxL4VP1uynNIdEL0TJiayewHlu7_8QZoM3yFfFFQuNxs6OvcJ63GUniXryPhpzslr7jvNzYh3IDzpqNMDLlTsVnKdjo-AKRMmTS49K8f9y0t4ZO8JLqXUU7qEMnj5NGc-xnnB1po7rFCG_vd85nnOBwfKnH2veYNGVo64Gl4m_X8RTo0aWdVM0hSHn-0rgtYCSWGrhVIfeDgnbGnWOgHjEqa2DJJVkVU-jCz__yGT9ZFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cb6dPv7mF2brl_Nt42A9oZSrNkthMOsO9qMIgUbmO-4eXppENLRTXhXFkvgUHvUxu88QoO-zs9mIDArZIL_kwD6q430jmcWfzLLDfmQhhX4ZljDct_MFw6m8CA6SUH4P1-cz9ifkELlLXafejs1uQrWIFSDeVQ4h9HFgcHr1SpXqcltVmGAvnaevOyEMYGuYhTWo5HsDWCx55UyFxKYgNHd1FTEDvnyIOels9mSxP24feXJ0aflmoq5Ye-9IXWwlWqsJSmW_ucQyQOKgz85N1KifMxDlZkCpp3JlqO5bez8b2UQ8brcJ9pqpGfJ3bDdsXph_DZIwKe3-NGL-iGlkfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30169" target="_blank">📅 10:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30168">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2RFzxksXNUCy-lbwW_jR1Aur8tYugI22Z6PDZnoPmCWcdDEve1P0HdIYDVDrIUHkXo13olZvV5XPubal4_lIa6DzpmagoVFRGYwDZ5XP4uNiNmShjc1T8hu-WRVfwd_50m1y_9wt7bMbJH5VcxPi6FZikZJROTmu6TZhlMiH1d9lC8lETFrxeu1xMqTeOrpiQZS-oISIKALYXA8Wd6kw6lKWARaZFjLVlmvOy6AkVqjAQUb188KC-zI8_wQOdWsMyH_nZ2uYz7hQt1Nf2qcZVVweAjzOdHpbw9Sp--S2iTp-Ry-1ZbODZrWh16Itfjq75AeYxy1nQWLxPmH94mN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30168" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30167">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015580725f.mp4?token=YKOLaA36hoqe348HAgOaz-BdsgopU3zRLuNizs3htafVa-qXSKbbN6nkasEmFMKmhnB3RvvwyC5tPgt7-VWDy91a8U6PfIHxAFtvTS_vUh05_iRYqvk4aVGpch-3h8g_wZwcTe1dpW3aNxanTuUZ1R8nHdfjTzFXlDCD9TaoyHE-A5ZV8vmCKFIJP4R9yEqf9MJgxZ9GfL5vwB2N2T2IoWHYkmG8sv1uj0oprBotzD1wI0--vBwJ1fsYzq_a604S9-Qi2Qc2B4ci673pi3d1812S-6o4JRjpea1lmhlINGZemxOlZVm9VwIPj4IxP3YBn1Kz3K2SGrN8PRrAc92tcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015580725f.mp4?token=YKOLaA36hoqe348HAgOaz-BdsgopU3zRLuNizs3htafVa-qXSKbbN6nkasEmFMKmhnB3RvvwyC5tPgt7-VWDy91a8U6PfIHxAFtvTS_vUh05_iRYqvk4aVGpch-3h8g_wZwcTe1dpW3aNxanTuUZ1R8nHdfjTzFXlDCD9TaoyHE-A5ZV8vmCKFIJP4R9yEqf9MJgxZ9GfL5vwB2N2T2IoWHYkmG8sv1uj0oprBotzD1wI0--vBwJ1fsYzq_a604S9-Qi2Qc2B4ci673pi3d1812S-6o4JRjpea1lmhlINGZemxOlZVm9VwIPj4IxP3YBn1Kz3K2SGrN8PRrAc92tcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30167" target="_blank">📅 09:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30166">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpyxPckpvAr9hPR3XGoqVceHpyzu9YcHZa6OeBdi3L04MvTma3uG61PEC6TcRgl4YZtBUYuiCJbip4_IS3Xyp80BcjJFCj0ssaj_I3DO_5kdwyLgTrWF3ihpENRKo1NCE1rZM6WHMx2Bsse90kHFyDkeO7sH4p3c9fAgKDhfesjBkP4Vu2g4AnrQeHOQnj_pFjSpMQdxd50hEaqlOyFGSg_uS2A37weicyPzSmmqNQoENk8CjR4Zzf8TcsDbED1rJvr6PM_-3afuEEmwQxolbHw1NoSv2chfD-mZFFm_-I0pRO51O50UhcZOwEO_p7NPYBeDB70Gj-jzr1gKlHGu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30166" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30165">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=Zd0bU7aGrHCmTfU4QITx9d4a4d8q_ExvHr5oLBr15jXL-tTeq-GKvZxRx0bfyDpg-RDMfsC-807bODw-Wp7uIRiEZp3tcUBfRGDe7ZjPQSwwaLb8bokQCD2OETsSDSsjH91AV-56Rdx04s5XL3EqZif6O2Hh-c7d35mCFMWr4mMa3JaNsV1ipGu1R3Gg2njUx8nNwnVWRy_Uv4mimi9TqSedT9L4cJxYTkz1y7tOf2xh7RO8nJEnoFUFG7Nqq0Y5vGkr7fGPeMfNzMhS5D8TtB2ERmrYwrZevshgZlDmmrAGbDvO_LtgNf61Jq5b6FWPQ6clWSyOmGiYrbl2moEPig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=Zd0bU7aGrHCmTfU4QITx9d4a4d8q_ExvHr5oLBr15jXL-tTeq-GKvZxRx0bfyDpg-RDMfsC-807bODw-Wp7uIRiEZp3tcUBfRGDe7ZjPQSwwaLb8bokQCD2OETsSDSsjH91AV-56Rdx04s5XL3EqZif6O2Hh-c7d35mCFMWr4mMa3JaNsV1ipGu1R3Gg2njUx8nNwnVWRy_Uv4mimi9TqSedT9L4cJxYTkz1y7tOf2xh7RO8nJEnoFUFG7Nqq0Y5vGkr7fGPeMfNzMhS5D8TtB2ERmrYwrZevshgZlDmmrAGbDvO_LtgNf61Jq5b6FWPQ6clWSyOmGiYrbl2moEPig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه جذاب از عملکرد کریس رونالدو و لیونل مسی که ابر ستاره تاریخ در فوتبال اروپا رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30165" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rn_HjjXucSAkVqsMT677MNHuDE0rc6DTOCQn7c7izm1vOTAtSwzQnLZ6X_VbRXwvqomsaz82-bAgOfT1kNhGyD0knJcyvPWs1Js6E3A08pj7EakMyutMZ58C0ULKTuqvanlaQSdnjOausB6iiJH-poMqRnNPjPPDB2_n7eejKMHotdLwnXejB5UT_R_xNrnK28JSjjkirmUSo--rR0eF097bw88RsoqwzqNJSZ6N3ZTriXDvsAfEhJx7PdEPHomVKs6Zx4DLf7_QWgERonMYkvZ1nA-TyCd5wx8kE3DXkxewIodcOU8tbzziLNKglwh4rH9nnFaN_jJlUNYTNhRWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ck88ExGL8lgJbrBHSEPMnxzpVkex2UuVLT6ZOcRF71FhkbjJhO1Gl1H-0nYZBHdhiW1VMmflcdLFLj0jfBTUnhNzdEM2Apuat6wwuWoovSMHr74HG43wkNeZh6t8Wr2Ap6GFymvK2FXGlffpOkGjmvO79Z1TpRmHM0r5RtdF8ozyxEw6dH3go8plaaAR22UgLIFajhpS0otBStDZOFu0Brs4QUDwupcH4xtxVIvLZs-KjcbfPB973ZRmIy6t_fInzhWG8ry4ZwmJJYuyPSlTAY4AGqAeH33tn9Tfzut8i4PrVI4JqVJXyUvmuPjhCFHrfiaLBV3vGInpKsAvSdVvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQVcGK2glIKO9xucaQ7xnyPsPiIiVUm2Ppv9ChufZdGopHK5MziF377qCb3ZNTjFXtlHKvjMYyaP_BU9pXAQrj4i2ErT7tJopMoTWuSeXdflEFP743F8g7zzrdpJ9b-1LGfn772NCrRUhrSWzC8GYrGSpCamBBKDUscNb6NGr5BT9ZZ5Ci5sjYa0FOf1oVlb3PaaUeTbmK0iBkfcimi1xqxTqLjghX-0GG2IK8ihgjckBSYaCSPSTpcJ0AEGtA_G7X_Lg1dVxy5DMIpSV_2YjkIP7HRB0TZ9QET4MOJJtR6Q-fpTQ2TA3jYd7rs0esUMi0-U5gwkqDklkrHvLXs5mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJd5v7R_1eYlOaxwmI7uAJjqcbBkBzYc6z0YqsfyLACQeHlvOtXfeuHGvw2rzFsFKRCKW-bwhHvLg9inlz5KZFY-lyh7ofqVVRMOQmbGiF9q79hlIZPDJyjTrbSX7aLOQMoNUmQfVhV9yJi3C06tO8r91pOk8WIdKTyLKFkEEOOIug1o0wSd1yisKCrkLgxWP_pxkksSF7yCyLC1C-RFo3Sg9DNEkK5d7tGHRJayki4zjwumqNrWSvQK6YrFuFeXW2ApEDTG3Q24uOB-04caavLlDZBBhFl7bI9edEMg3zHdkA7H2PYQ8PM5To6-dG83n4pEs4qe2jDAJPZZT_I9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=ZzVvP7wwMQtWLXY2M-yA9qxR0r7s9JppZ50ETrQvsBojVU4EYAfADztZNvSikW7CEyccEfmRIWK8_B_wvlYJezs1u6b4VeFwweyjROlFH3TR4IvkjlVKBa2rdTKtZqunZ_JVoNhO8wnj9ZxLEEyv93irB8K7EYhX5P3B7UgoGhAH2fbCN62t8V6jhCoFsKuhm9MznQhoOVEhaUwer-aD3JyazYmGVb_jA_kU3ztfEOACkYZ5Tm4Q5YUn0IBjvElp_dH6pN_KYrdFi80Qu5jAcjGmIrPIdU73635spi6CYFRT9D8fxUTME6Vh2dJ7gkasfr73gt3zlmssO_BkMAUfPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=ZzVvP7wwMQtWLXY2M-yA9qxR0r7s9JppZ50ETrQvsBojVU4EYAfADztZNvSikW7CEyccEfmRIWK8_B_wvlYJezs1u6b4VeFwweyjROlFH3TR4IvkjlVKBa2rdTKtZqunZ_JVoNhO8wnj9ZxLEEyv93irB8K7EYhX5P3B7UgoGhAH2fbCN62t8V6jhCoFsKuhm9MznQhoOVEhaUwer-aD3JyazYmGVb_jA_kU3ztfEOACkYZ5Tm4Q5YUn0IBjvElp_dH6pN_KYrdFi80Qu5jAcjGmIrPIdU73635spi6CYFRT9D8fxUTME6Vh2dJ7gkasfr73gt3zlmssO_BkMAUfPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q94AHqYxsjkk2rKoZAjW07x48iEEqebBKci_SgkUcl-gS6VRYiToVeueCOdKFUtJBh1TYw_wpDN8uGzvtVfjfPiAbdxoNNWLsMkVC24YDsCMYylo6nNDLqhxoOvB4yI7jtwB5H5fAq757KmS9cB1ZpEnprGaHKTaHMcpEgDBMrfuRk9CAcL42HodDALuGP_-1tDMCMBPm4eaUO3zSuPqHBPjjyQ8zs83AYXHeqotWCh4Gxsq5wEGg_N4LKa6ax1yMO4Tbh4pxMWcHEf36yDzdgSHAonWThhuDjKcG1J9t6Upocamaxlp40BYUirrAmAkt-efMLsazlRvV5gIfeXM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEe9nYrnUVUKUbbDk3regQzVRM8bX1Pwy3qS1Z6fHue0MR9r4clV5WHcoNgyciACY9N85c8IqTT7wuPQs_I_Hl1yKdyHJ3jIzFB870oDCX4s3KwL5JZXLILPYgw_BThcR-PRFB0LfxQATIx_noCxpIvXAXsViL0H42M4Yfc-GKeshB7cFqUX41kxeF8Zh3eg-jbewiBTZJDpHmegmp9xmLd9tNSdJGMRhsKbdUIeiBM7LTmakCWSu1tEpHt5v_eH04yzuq-z0QAZitw3q1G8fg2zIy9DkRCRzNWHebXOIw3z6kQOVNoteT7938i2Zkqiak1_6xLtNwkqVPRGDUXmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAfCvYk5oTBUrtVFCTsNQXS3VQ8mBLpbqO3JFlvVmI4L-gn9jRGGvcrn2cV1Qk9LW2XkgSzadIfBuUykpebRag4kmrA9e0ufgUHdfLm8BDvgF_1mzdGriOp74UuHHJosiD-D5YtyfRaX8HwdhOmWmu8emVXbEOpm0vlBFehTssM0g2vA_3ZbB78slqeK6uabNym-_d_Bb8yar4lpXxqGiund1Bzu5ZJeC0pKMkyCnp7Cu_xezIJ7plqRgWLI6ZFmScI_cnTbcXa0Y8HLnMbzIOg1EUXDvA4HCy6KjPxJrqi06UqXj9cL4YutkZFfonzrQDaeeAm6GrSW_8PtY-tUaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4Jurs6JoplJnnHqrHBEQ5IlbiK4f5LcvjXm3_Jm8miIVRZxNU2WRfw4HJrbhmnxJRkuzXJ9dMbiGTiMN7ftMam9vYaqmNLlpnODSjkZ6u-e0geMV3GS56abOdLyf4VmAk5p4G-Pi5icqYtow5Jex_Dlc89-v-Ke_WM82Rr-NOf3KSQQ5YmN81UvJJ8V2Q0hkM58j4dV20h_4XKTWMkTx11fml__5Bqq74uTs0K8U1PCDkVcA2wXuhSFPIJvG19FmmIvq8NDLus5romh9H8HkjPnezzo809UnQE79hjaL6IuNihZqTJ4ifL2GvMiP7H7kEXtVXZOxLE_vAqNb1pU-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b81dT7Z0qRT3V4CumBhsyTPaL81o6jeRp3bhZMHSz-Ub-tN9AOdEnPpTEfNFNzluDzV0nMHlN6eCyWCv4cvLLGUAOJjv2C31wxPYDopyt_8PQkNgE2mrgGJ5hNkt06LzT8wI01WJkM8XppgbGRmbz6bIQvIG-UJWKK68SHsNFNehDCIoVhyQ43fl3TJYS0X8YD9Th4M_kb3ziyX7DsJmXa1XHghcjp321pzknG-UYWXWvpIVEyfj-WC52P9ppt-m3zBPJjqwM9paTDF1lNluH8jBlBdSH5R2f_jvwD6GPw1KRn5qi8yYfgrbaRGWBvbNg4p0X-ETahl_DaXHzDrziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojJzlwcrG3Wh2InkvSVqeUWKhrmZVO6-UmQpM8PeuY4UyLtW74HBJiEtetRQGhYZXfuTS5ZEAFt3L5o562GSF3SvidwHTPYy0O8zRBMvoRtY_cB-G1NcK_P51WKg9jp4wzY1KpGTVLwdDVvemrMaAaYDzMe_gdsd77FIXCjePoK-VwXIXbkZ_tvSBwsQqh_VkPcmz-zBbi4Zot51cIHp8a3z0Av9dABK3YYzNtGiLRy2WA0kbS6d-lcpKpoH1KB_SEHeuWJ-JI8v9YIfJv2snWN07SlfNE6fTW3gJ_F9VgCcFWb4D-TGoBm1cs2NuF-P78SYdJkg8v6l50VEYASGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaEV8K0isS_Q42ll_7nORnJjsVHo6dsKKwsdosA5qvhk8DentpnwWXf8fmCH1FT2SgeGeeVdzFAnjIar_1fMaReghwKTi87Qu1cfQK6TNd5Xv1ypxyZJMgZfNaDQxiT8g8kecgIjO-4HTplGSl6KZO8u0Jru5EwngWIkLxN6sL4ZFozBgvlqXTSUtRnV93odN9WiyAWyY9Sqjlo4g7aOWN33jQrJ9zOIfzLWsDhs8mhltxf7SLrX6Qu2CjcpbL5fbD0k0a6bWLJPI2jH4MG2xQ-cUIueiUrSeZeoBkDJJFPxJ24sHcQTno1NtLE4gjn8LMjrLCLjljf9btMv_yfX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYqcFFkKxEE4XjXfW7u328NALUQ4F8hVTcCLv9xrO3xk453Pwnt2CZlNyGkfkSSDRdXfsb0x14rKZU32MRvmlMYg_j3VnqNBgQa6PTGodOiBVAQcUEhVCvinC_0AaILb1c6DQzdYBoGtNTqzTDoHDS6YVlMdpRPk0YafX0xlnPM8xyCKhijBfyG3rqZ2cfbGDbDbZbO-2Dc92GkSt77SJsWa1HoPrAVedzjLsyF6PDgwXJFO5XJ_otqiQLUbhpI8U61KU9CRDt2C9X-xIk-Q1XcvpGh4JJGTeXoKsy4bVw3abRxb29etFFo2LMeitzeXp0i_zatmyDxXzXfKxw7Vrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfEq0i3TW6PirYmoOhoKpAxg62vbXrpYN_PV-j6CREGRSo-h5p99oJ4h-mK2xjEwdM5xv9DJ01fR8fqIExe9HEaDkCzodHdZfyfZVu2kdNcW1WNcEPxr3yikKw7fJ2ejtqcWSlqj9YY6NyzWK2p-6jAlFOoloSBbdLQiEzA5MPeEqNlvUSm0XIIWx79m4chheuTkwOlG5elLxC2OZD5_EOMuLv2kCz91s5QB3LuWBocREEBkcDZqbJgyaE4bzAqTptpzuPS3gb6thxJoGa3Ckqjvc8msho8A8BOptn3CJ4PF1xdbAkMDoMP6qskWSQN6opwh4TIDFKOtAyo4HsLuS7M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfEq0i3TW6PirYmoOhoKpAxg62vbXrpYN_PV-j6CREGRSo-h5p99oJ4h-mK2xjEwdM5xv9DJ01fR8fqIExe9HEaDkCzodHdZfyfZVu2kdNcW1WNcEPxr3yikKw7fJ2ejtqcWSlqj9YY6NyzWK2p-6jAlFOoloSBbdLQiEzA5MPeEqNlvUSm0XIIWx79m4chheuTkwOlG5elLxC2OZD5_EOMuLv2kCz91s5QB3LuWBocREEBkcDZqbJgyaE4bzAqTptpzuPS3gb6thxJoGa3Ckqjvc8msho8A8BOptn3CJ4PF1xdbAkMDoMP6qskWSQN6opwh4TIDFKOtAyo4HsLuS7M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=Kri2-3Vm302gOrxTsPulJOkc3V7SyVXtY5neZ9PBsukXVBfIq-cfXtaKx7Ntm43mu6m3wg5ETBc2IpNgq8hiYHkSOd1MdfCsQYwSmppsfw8I8jzA4yIoNjh2KQhOUSNb8RddvSAxrx3C4iGBzSWBtuc4v2HBMZNE2FXagEEU0ELKLVIyZEUhAqk_bxyIm27Ive3sf1WTYTMGg8JqK7zt8n-HCWgXlby5vgtRXzPUDBnlooNpJhzJMEVgJgbp57hFIMCv21Il-AHKssKdfxS1iszxs_Rj6ANAKKFWDuxpbQi91atcgpo0gZSMMH9cdsmTS4iGFc_QpBpRWJ6_Z-v4Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=Kri2-3Vm302gOrxTsPulJOkc3V7SyVXtY5neZ9PBsukXVBfIq-cfXtaKx7Ntm43mu6m3wg5ETBc2IpNgq8hiYHkSOd1MdfCsQYwSmppsfw8I8jzA4yIoNjh2KQhOUSNb8RddvSAxrx3C4iGBzSWBtuc4v2HBMZNE2FXagEEU0ELKLVIyZEUhAqk_bxyIm27Ive3sf1WTYTMGg8JqK7zt8n-HCWgXlby5vgtRXzPUDBnlooNpJhzJMEVgJgbp57hFIMCv21Il-AHKssKdfxS1iszxs_Rj6ANAKKFWDuxpbQi91atcgpo0gZSMMH9cdsmTS4iGFc_QpBpRWJ6_Z-v4Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=atydaJlB2oGX-KiW-K5FBJYUya1nn0Eg0vAnwKD7Fo0lskONPhG-rzPYqxG7shu39cQW5skh_fQxMJQlFUVeZMEmPvh2ofvLgiM7ZEytZ5jCevz2SVALCpUPMNUPxRsMQpv1Ax15hk8RKYSbyZ6L8yrrw71dWw1_tHwHHdV_NbM78D-aeI9FRa-bAdwFj2KmEbtb3-5DCB3q3kuTP0hWNnBAsMLAmJajDoecKOtIdhvYX6K2vcEizd_U7oyKjsKaOoxN-mlbOplibejqZTLv31YcjHSJUMMUqV6iPVEFCs2Zi3YS9oOywiEXsEV3DdiRoIrEPoYIXeOkio2Nu89glw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=atydaJlB2oGX-KiW-K5FBJYUya1nn0Eg0vAnwKD7Fo0lskONPhG-rzPYqxG7shu39cQW5skh_fQxMJQlFUVeZMEmPvh2ofvLgiM7ZEytZ5jCevz2SVALCpUPMNUPxRsMQpv1Ax15hk8RKYSbyZ6L8yrrw71dWw1_tHwHHdV_NbM78D-aeI9FRa-bAdwFj2KmEbtb3-5DCB3q3kuTP0hWNnBAsMLAmJajDoecKOtIdhvYX6K2vcEizd_U7oyKjsKaOoxN-mlbOplibejqZTLv31YcjHSJUMMUqV6iPVEFCs2Zi3YS9oOywiEXsEV3DdiRoIrEPoYIXeOkio2Nu89glw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYFOBGM2XJsZdSxEp1wZKIjGiiHSVXvKr7rjRJtlLMQixdF_eBqNTvwscEryXgmQZBzLmZEYeVANjqx4u3wtgNKBKCvjMV5Yer9MxzpFVP-s07xr920ml-RN_hMbVC-PFPJ4kp5qXIGPOgacvr_IM8WqUkJuANOmXXoAngccjcGusZ8j0oHESw6gJzDU1vGgd4aX4pDpQ-XS8BIrVfWuv6tSx-NnHKqkIZArtMwOPKwmmqvHokRhbEml6FRbGsqzpuUVdI_SAnlUo_-Ewv7je7RUDkWDXhRyZmB7py9Fts_BkdHm9Y9EtCDZdPH_px17IbcPvpOV_aDkWWnqMWOUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrMV0SDCKn2NGkSbz8F2V9sbxrj1SKrrZRlN2Brsjif9rkaOjTysJdJ1uNHet_E2A18s069Br_kazDVvkI4crObEyJaKVjWl8OgpNPKfuzvowhpMHH25pSeokW8OXFUxsZTcnMPVQoa6VyJMxdfkuKngwTlvelkEBeJRbc960HvHUyJnwGPtRPg0i-U42UOJIMALbECAGeLAr2BsXT2MzzdYwbrW554V81nzkYsGLGNZhRWV-nEWqx7hF9pyNx5FQtbD_LGYiYKeApSHODy_YGxCBhqLp6jGtepLi6AbfrZDZf1S9zEEE6yBjZvMDizOHdM9Z7GU6M3c4UqgikOUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkxOS1rWJMP8Q23_7Oh170-bYyrydVTLNK-PD-tgVCtuhNRd5R1ML82U3DvC6MK8u_nJ53ZYKjJCvJHrY-umLomfHikAVfFNgh_v53wDyC04yVzf8aG89blcc60gJDoR1DH7V9metBWdkxaPq0y4awh0vrMGNe9M6HziavRlG-ov5NpJilkHauYY92YYwaYjAXv1uhzgm9EABJNORbhwoT40GWbq2s696h3rJR4evYRapIMIRhld7Fjheej0YP4sjgqdlrrv-NXzJ8HroGpkpRTkABoIaaKgIcoEkju3GhD-wDs3aklr0137bGoW0VR7XTEUX7Oy68PdjGhJSGvLzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=kgigcxDY1O9r-AJs3DYaVkynm4WK6iIqiMq1IDiksh9V4zTguxKInOatQKjbDrhBQDx50GqIbHdgKuuvI3ypZq-flryTmdgnHPHo6W00FLrp-KjOqva5vq-ffu_uOsh3RWgy6e2h0YwvzgdPyrK7C65Xgjrpj58ntJc2zO0wGvEj_CjRqy5es05yha8fMkez1ntMnHygo5WBS9r9UY7nNHQ0uXU2BHqRF04b9qsHEyn8kMu2dlyPPPyKLIS8mWTluEPTlQ4FYWPvpWzA5e1GGUvUOe5QHoY0O6S2JeAhreoJOKdFPt3xRA6a8WXLxAVb16w_2kSDS5mg_KcBLaIxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=kgigcxDY1O9r-AJs3DYaVkynm4WK6iIqiMq1IDiksh9V4zTguxKInOatQKjbDrhBQDx50GqIbHdgKuuvI3ypZq-flryTmdgnHPHo6W00FLrp-KjOqva5vq-ffu_uOsh3RWgy6e2h0YwvzgdPyrK7C65Xgjrpj58ntJc2zO0wGvEj_CjRqy5es05yha8fMkez1ntMnHygo5WBS9r9UY7nNHQ0uXU2BHqRF04b9qsHEyn8kMu2dlyPPPyKLIS8mWTluEPTlQ4FYWPvpWzA5e1GGUvUOe5QHoY0O6S2JeAhreoJOKdFPt3xRA6a8WXLxAVb16w_2kSDS5mg_KcBLaIxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XG_rjYz7f174a-MRHQ3Uqz9zvQ4z3r0fFaMRLx7OO0XBFRsrv_KOMU3wS-ilfenZqBZO4IGRcg2F3rd_qphfACpIS-97CtT5pnJjvcTzcOR-UHCmb3donH91ieVFTa2UsTFwWtFGnYPmqLN6QIFkDLFngAqMZ3pZrVxLSZ1CkDcxiSrlwX60mWTEdBNdIq_bdJu9SkvXP8VQs0n8-M65X0KAf2pD9WWB0oX3nXeKkid7VAz-ZN3NcZPw7LedPjYSwC76RqnCBNvgcZ9wZZiQYCfmppwy_b1StYf84A75F59cASMvh8uJjKpIPB0CfXCgcDGd0VZJFAJlverIbosSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwnGdzoMwuJUgJCPsSus52HumpT2PCHVPudeUqeVenOWeJ1Ky22f1rpHz_BDqzN9BAEAr-kdaR_ndxM04gI2Usavc97XvV2o0V4ZIRThYUwhC7WJMmqzV2DLwOO6GGw8BovBzKHq0jeBOyyt35gjnFASWWEbwsKHdc8NC_e26aRLqB7YDiG_3oTGPQwo8FN1FnwZ2ZkFNRHnKanafOFbidwNmkK1H9u6wsNI1qMPK7ODFC74-4J7I-lvfWMTnqBS5fW90ki0jnRWCo67WCIp8HUMbjFvWLaOrPOQL1l5knGmAN1BSD1R_f8LGJwlo4IzA23PrallD-Uq00MQXSDwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=T1ILhZD7-avjm1drEEVZP0D5dDIKwYU2GuCQ7KVnVqc1p9TtF24uappNgM7RPrmirZPxJjdRrTM8reNk7UHumDidugIm_7NZlAUfB-FzyLKn59Dqvw0wnmMgFFEA9SrN1O4I65NXfs-jTDX-BOCBRz5wHrof78LlsYnrKL2QBr7ocNTnnN_5PuuEYTtwO2Z9JcMsZjomnmLseCVfzt99bgV2yxUjmlbsrGztoAe6MMbjidj-krKYflXKf4EW1a1cqo6DpHM59mb_v7eJ--Zz_HQHYeUMwKiQzeF_HeWD-SEMjckEZPnfWAN--LHKgr_cyTg5ixA8MR6kvsL1pQorkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=T1ILhZD7-avjm1drEEVZP0D5dDIKwYU2GuCQ7KVnVqc1p9TtF24uappNgM7RPrmirZPxJjdRrTM8reNk7UHumDidugIm_7NZlAUfB-FzyLKn59Dqvw0wnmMgFFEA9SrN1O4I65NXfs-jTDX-BOCBRz5wHrof78LlsYnrKL2QBr7ocNTnnN_5PuuEYTtwO2Z9JcMsZjomnmLseCVfzt99bgV2yxUjmlbsrGztoAe6MMbjidj-krKYflXKf4EW1a1cqo6DpHM59mb_v7eJ--Zz_HQHYeUMwKiQzeF_HeWD-SEMjckEZPnfWAN--LHKgr_cyTg5ixA8MR6kvsL1pQorkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJKamK1mDR7EsQ61KDYmhYEOzUa3Z25c2OzyV_pl7jvs_sDaI4MBdmxpUOF0a5wKIguAE49uxsJD3jbPS_n0cU_5Kt-k3MmlnOSRno6VcwfgURDDh1dYtM722n_KrQHqXRiJE6_kVFYyYDvRFhovxWvovAtcphxLK3s8stkxOCOnz2F9gRBOIeUKUr9PPLexev9FDuWe6FjRrnawVO1-b4YkfGNDX8NdiJ6K-zAHvRlxbPvN0MRE9RQWb2JUQTFtO6cTgDA3d59PsfZV3qIzZ7pWwyG1vz20X71bIJN7xbozB-gt33Czjvk-HVzJJ1w-oa97FzvgF1ryVdGc_QXQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRpEplfYo0Y9lzmIQTo9s1vE4Ih1mf7LsUQs5sR5RFYhwzXkSoSr0PlD33nbosFAubF5COxaLqptaLi7ZUlmPrGnw1oBaQwkDJ9hfgmIla2WKLYLjNIkOahsAdckwtJ10yF58mG9dA7nmltGN0tcUEtIuvtbykWHudFwrdNh8Sf0p0gCm6xkVVCr3oeo1KrOpFtDqhF_D_xIvGkgwIkY6rJGnjV6E7sENnqrQjfu3gNslRU1jfuzAJKkzmOzbvePaFXgsY1mvoHwMTnHuSFQZANDRe-U-clmuGBysZ1f_MJAogvu39TRkZwxgN8Ag4voxNQN9iDGY8w9NWb2MX51zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=HPB2HRbaXgpYq_7bd32g2Z3Z4WNd88WhdMsNY1cw25WrVnLwFqMNmBx-F6BiaScdczrdVPevk7BptZZ8NrW0pZb8xHghh2ZJi8AXvI5B59CT8Hvu0e-SUQqAXS3eXCE2FoZGyF2LcghoRbBw9PXjAwbX-bWuqqxCyn0U99VztakSuL8129FVgl2mLBglXEZH3NzJ9RDCoVwJv-AhFKPZ-X6x02lqA-S1SUHdmgAuVVNoEf8MbKFebM1rELLNEEgPQ4j7JsK8YlIz4k-lNhxoEaGgCQwWndMX19BdbWCJhlg8fPVMVhEbmt-c6pKskAQu-JjzQ5M2FkWYE_JgFZuIBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=HPB2HRbaXgpYq_7bd32g2Z3Z4WNd88WhdMsNY1cw25WrVnLwFqMNmBx-F6BiaScdczrdVPevk7BptZZ8NrW0pZb8xHghh2ZJi8AXvI5B59CT8Hvu0e-SUQqAXS3eXCE2FoZGyF2LcghoRbBw9PXjAwbX-bWuqqxCyn0U99VztakSuL8129FVgl2mLBglXEZH3NzJ9RDCoVwJv-AhFKPZ-X6x02lqA-S1SUHdmgAuVVNoEf8MbKFebM1rELLNEEgPQ4j7JsK8YlIz4k-lNhxoEaGgCQwWndMX19BdbWCJhlg8fPVMVhEbmt-c6pKskAQu-JjzQ5M2FkWYE_JgFZuIBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=qo3nUf7ugDc-VhVnonuUgXwlPBhHH2dXZpuVGLUdmuOcFLm_cuh78kA2TjO0Nu5PpsSqDmluu1gMKbWhVXKgLGxM-1jtNWs4n9e6hhb_Q48WiCuadXK2J-bIQ2IIA7gS4O1TL-SWSr8POKAjuYpfcqcmwC9EosqpuCRMwmETi7b3zfuS2H97qC0sfD-DQLY9KLkwn59w6eNolTWK4b6Dmo2MvbuaBlhX9vVX5c0A9jkX5kVwCjJLqFJQ_eM8XGP-jNd__WxPeh4ITpShJ0lWMUYDMo0Pi2mK7csYJm3_CELIUe_5UVxDDPe45pWyLK4EpvE5V8hdvVT_RlbDz3_fjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=qo3nUf7ugDc-VhVnonuUgXwlPBhHH2dXZpuVGLUdmuOcFLm_cuh78kA2TjO0Nu5PpsSqDmluu1gMKbWhVXKgLGxM-1jtNWs4n9e6hhb_Q48WiCuadXK2J-bIQ2IIA7gS4O1TL-SWSr8POKAjuYpfcqcmwC9EosqpuCRMwmETi7b3zfuS2H97qC0sfD-DQLY9KLkwn59w6eNolTWK4b6Dmo2MvbuaBlhX9vVX5c0A9jkX5kVwCjJLqFJQ_eM8XGP-jNd__WxPeh4ITpShJ0lWMUYDMo0Pi2mK7csYJm3_CELIUe_5UVxDDPe45pWyLK4EpvE5V8hdvVT_RlbDz3_fjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDYvtcymlNZ4OnH0d5npu3Uf7Jw9ThxIeadQJuI3jDnQtenIfOqz8ja8cxspl3gLfZ_ydHnvF8SeEh0bR8ocWde_rZF6wbUbd0fx2tAucvjZG96ax9JYU8E2ggAsOzp7DL-eZJBGuk2oWbMAnxXxgSHLFBxPbGJ7ejYygdpBNNBDeJEgsGnkc47LfzA-T66O7w7A8OpoAN08oODJz8uITyu5jNn8TYin9pN_ygyrXiE_MN0rbLKoENf-S1wQyPOvvWPOW1OPo_cwon6hnyaflFEQVl9Pb7J1IOuh0njeL9OBRcWZN0rpOsEPShUrtpdLF9Zgj4st2EjmjD7NkBW-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iB8khwenb30aTwwr6y29juXorSjmtDXrFOBWZXW3BsVQgIDdv39xNjpdAAFZpH_WOat_ujNSfWciHDcLdw3ByViJIa5wQCgFQzQBeDgTsumS_QuT_nThEHhVpiEWfEuIQAw10yOvCBjd3SMM7-b92gxFZLV6dXvy2Qg92nVL5S8-HBYOju34RREYifeUek2kwsvblPdHmfq3Vu1x7zod7_md6K2pzINlMtV34gfkwAVCQTqcxOgJj6YxZpVp9kC8SJxuKnvtU8n1jzEQqgj9aN66ZvQmAYQ9_aenpcyKCeSB6_P9RtSECh4s0GcpPOqkZvcaHcEAdBDHJMJLCMgSyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_7zilrEfx81fcC4uXWXQaciWEyHV3QTuvgjMJwpGrB5f8cOTNlc6Vvnccif-NIi6tEzdyXru-UPWaKDs6Pbyl7w_yaQQ8my3ZZQv2i--CQ3Ca96ecXnwM4K-toEaxAyLx8SFmI50ju70NLmVRH_Q_Z5htV1hcRfayR_r_CLmmXdf0b70d45GGgRaO77vul6HVv3rDbR4tkhz3D1l-MFPjY5mMtHcvP93zgYVmlQjYSJHuuazy88rBY1rXdhwd6FoF2qevkioeH5UE02f6Js0EOk40PdPQ3ea2DTePfYigT48ktiLx4obKOl2g-JzwqG5qkX3-q9iBM_fqQ00JUbGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
