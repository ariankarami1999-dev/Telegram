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
<img src="https://cdn4.telesco.pe/file/AHGVQRwjnDu03HUwWlU4xv9qrO4mqXSA4GbV7LdAWpu_K6-zmu0mf7aJZC2_g1a5smW7j10hAuG8WGeG3lGx2Thza6BncWJgD09iAEby4D7qXKp6lKlqd8ksVVRX4Iu65Alfv9hW_xGqf0zNixFO3glg_cBDXj2YWIS4NEDVeraOCxhVpein-Ti4wSjrKGYzK4XPT-JblbLR8vPR-pLox_zAEJDE-JEnZsvdpElwXOd-cE0JAfDSVKenK7NMYNtctEfs0Cy3zV_y9cRSmcV1NpAEMeoEYdGpoMD1-IkB5BjFeTMwA8DnbWMNvR7BNybUt6HVidqZx1WXaWSKqc1zBw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-666204">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع محلی از حملات توپخانه‌ای رژیم صهیونیستی به منطقه «ارنون» در جنوب لبنان خبر دادند. گزارش‌ها حاکی است نظامیان اشغالگر این منطقه را هدف حملات سنگین قرار داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/666204" target="_blank">📅 08:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666203">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1221868c.mp4?token=UeQBod6cALkdfiNxnYvWOgVPH6V1Bu6GfFhZO1uRqrPbXAYksbgE5fKe-d2B6U6KfMG0ic_KiBWbeLCCadC3WNu36inLfYMsjBipydqY5FtFFLrSlXBg-3Kb_pyghTF-0bezLMFXzfe--UOOkFdjz61IJSOpEVMsd-uKLS_-1lkB-IudVJT9GJfExuFE4vhN9za26I4A-stiJzOnm9-ARs_a9noDG2OwxYcvjJZlMm_g_GT5nmthH6f-KxmFSLwUVoqsNVLgQ6hpd3AVWTej_XEF74Lw6qy71neBfWH4c-VH5E2jBp2-a5PGMZhJia4f9yubK8oeqwIXuAB0dzQk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1221868c.mp4?token=UeQBod6cALkdfiNxnYvWOgVPH6V1Bu6GfFhZO1uRqrPbXAYksbgE5fKe-d2B6U6KfMG0ic_KiBWbeLCCadC3WNu36inLfYMsjBipydqY5FtFFLrSlXBg-3Kb_pyghTF-0bezLMFXzfe--UOOkFdjz61IJSOpEVMsd-uKLS_-1lkB-IudVJT9GJfExuFE4vhN9za26I4A-stiJzOnm9-ARs_a9noDG2OwxYcvjJZlMm_g_GT5nmthH6f-KxmFSLwUVoqsNVLgQ6hpd3AVWTej_XEF74Lw6qy71neBfWH4c-VH5E2jBp2-a5PGMZhJia4f9yubK8oeqwIXuAB0dzQk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یالثارات القائد الشهید
🔹
شعار خونخواهی مردم عزادار در مراسم وداع با «آقای شهید ایران»
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/666203" target="_blank">📅 08:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666202">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meoJgnJSJYYqDoyFqSYszi1M8iMkl83G5xCYZ-6LVGzknqLL7_6FVzgd7j5qltgCXGyemMbdBIufNa6Cvuoqmii2hpJm7gRaL3OG6vCOa3G5kZBiDDBxQTq9ByLxIAF_dp8tg1r_fXwkgIgaVz9VuaeBDpCKlUiGMlCF6co-HRrAJoGxDpPom1tOlBJJGWXuJ19wR6f44dGKeB-isXHXQI8RY0woqV3Puq19DxaYg1r2Itz6RiacN9TI0doKl_bp7h86SDIvnr3F1y5FOpTjeBpxrw9Yh8fnEGinI-A9R5Ythb71u2p4FrEQHr8SI0lLAMFhhV03gziz42cV3_2LdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرچم کشتن ترامپ در مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/666202" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666201">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD9xgGGVlUFkUceayMUxx9J17THAtmF9WZmqsEtGl4h5diKlwGVqFEvalxxbmw3GUC6dZJux5YbTYZU7l-HvevuIdyjeTXjA1tWmRYRLHyMnyw5mIouAuSfFXZkQ7ybz7L9qUgLgE8opDqi514tmwXo0AD5osCtWnQCKd2_Jtlbdq-_Zew5Ff1Vs-Wn2kYgDTlCYnahxxnHVkQFoJhD_XQw2MbbW68eWvOuxGRqfutuUQyOlzj8I3Brd5VMD8SSE2avjUlg1AuuXAIHvWM2Ot7NXAVbKaDPRdim2Dezq2eL3n0L7JA8dDE6slXLrTED_dNlY6otvAZLXnl7HUCobvwOjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ebe347e2.mp4?token=JMBvAzPBDUYSPqB1MCU05jB6wQNR9PhAUnJYM9fG2w0y0rCFcjJboXWTtgjGi3uY4utvnRq4oprhLDiqzr0NybpRZTU3KBXMeXfGoGIRyLf0aLKR246fX02jNY3vz_7QnIbWLWk85qhz4x9Ial1G-rXsa0_IYiIcPDvrjzeRfDG2HgaltybM0jYSA7R67xuwxdO6j1MKycONbXZIKk0kQptPWz5J5V4YWkp17drcmWQMK4ELNB9D2YA0SiEXMSmTDYvVYQTxpkGOWrgYSVck3yZCLTw2YDJcD6yp7HX8k00Z2sEXb-_zT53ozw3RMVrzPT7i0eSr3kk4ArU88zyD9xgGGVlUFkUceayMUxx9J17THAtmF9WZmqsEtGl4h5diKlwGVqFEvalxxbmw3GUC6dZJux5YbTYZU7l-HvevuIdyjeTXjA1tWmRYRLHyMnyw5mIouAuSfFXZkQ7ybz7L9qUgLgE8opDqi514tmwXo0AD5osCtWnQCKd2_Jtlbdq-_Zew5Ff1Vs-Wn2kYgDTlCYnahxxnHVkQFoJhD_XQw2MbbW68eWvOuxGRqfutuUQyOlzj8I3Brd5VMD8SSE2avjUlg1AuuXAIHvWM2Ot7NXAVbKaDPRdim2Dezq2eL3n0L7JA8dDE6slXLrTED_dNlY6otvAZLXnl7HUCobvwOjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاشا، در انتقامت بشود کوتاهی
کَلا، زمین بماند علم خون‌خواهی
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/akhbarefori/666201" target="_blank">📅 08:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ژست ضد ایرانی جدید ترامپ
🔹
ترامپ که درباره جنگ علیه ایران تحت فشار داخلی و خارجی است، این‌بار مدعی شد به ایران وقت داده تا مراسم تشییع رهبر شهید را برگزار کند.
🔹
او که کشورش در کنار رژیم صهیونیستی مسئول به شهادت رسیدن رهبر شهید ایران، در حملات هوایی ۲۸ فوریه به تهران است، این‌بار تلاش کرد از غم ملی ایرانیان یک ژست سیاسی بسازد.
🔹
ترامپ مدعی شد که ایران برای رسیدن به توافق «لحظه‌شماری می‌کند» و «به شدت خواهان مصالحه است.»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/666200" target="_blank">📅 08:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e5351b53.mp4?token=bIQDium1CCyZOLrYLbEHW8ZHnTh9FDE3Z_z2cvhMfvXAWAG8NpVJzZjixFOnYeuII4ddu_hZvvloJzbqEqQmcPICOhd662m-EUTJzmteCl6jmVzXzZMpZRvLaMALc7me3noBKj7IkSXm4aXWONgTD0TSTD0ISGL3z1uBt_78XM5Y8joA47-LWojIz--XvYtSnyifa0UyAXrNXrTrrWmdJYQyALI2eDwmxyAA9GTLPsfKc7HC40uDHquWA3z9ObsuDKmtdsYuJQEKn4__Aae6LSf4fuZaqz3OoMO2MWFU6cAMWZOmZjHCy8xtZcJuU0mMycIZQBpF7R81Ehbo_5yk6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e5351b53.mp4?token=bIQDium1CCyZOLrYLbEHW8ZHnTh9FDE3Z_z2cvhMfvXAWAG8NpVJzZjixFOnYeuII4ddu_hZvvloJzbqEqQmcPICOhd662m-EUTJzmteCl6jmVzXzZMpZRvLaMALc7me3noBKj7IkSXm4aXWONgTD0TSTD0ISGL3z1uBt_78XM5Y8joA47-LWojIz--XvYtSnyifa0UyAXrNXrTrrWmdJYQyALI2eDwmxyAA9GTLPsfKc7HC40uDHquWA3z9ObsuDKmtdsYuJQEKn4__Aae6LSf4fuZaqz3OoMO2MWFU6cAMWZOmZjHCy8xtZcJuU0mMycIZQBpF7R81Ehbo_5yk6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار یک‌صدای «لعنت الله علی اسرائیل» مردم در مراسم وداع با پیکر رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/666199" target="_blank">📅 08:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d21bb4459.mp4?token=M7uOo-qepaKzqL6Msl28LTt8DNvDA1LMTYIcn6xkYoKZLnAYsJRxoqCqGbgoKJKjQL0tQTOLBwgbvWLbDE9JIpeAhzFVFKG2qAzVyWQTSdky0PAKlvCxhIiad9zjZpHkyhxd5joBplkR3MKwG5p4h3N50DCMgAYKnOVeUvgSyqcDIF3qEfKBNFVXpalmGj4KgRHdF4hF2P6YwnCr_0S1ATljp0DbBLf8a5A-PxuC3dT9o-lU5PRZCdvsKVGjjeyWGFuTC84trzxi675b3KhyB2fRJsURaGB4RB1EbMGor1QM3NFv-Q7dmgZsxAGMPLYC4GkTdsnmpIf7-6lvrLcxHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d21bb4459.mp4?token=M7uOo-qepaKzqL6Msl28LTt8DNvDA1LMTYIcn6xkYoKZLnAYsJRxoqCqGbgoKJKjQL0tQTOLBwgbvWLbDE9JIpeAhzFVFKG2qAzVyWQTSdky0PAKlvCxhIiad9zjZpHkyhxd5joBplkR3MKwG5p4h3N50DCMgAYKnOVeUvgSyqcDIF3qEfKBNFVXpalmGj4KgRHdF4hF2P6YwnCr_0S1ATljp0DbBLf8a5A-PxuC3dT9o-lU5PRZCdvsKVGjjeyWGFuTC84trzxi675b3KhyB2fRJsURaGB4RB1EbMGor1QM3NFv-Q7dmgZsxAGMPLYC4GkTdsnmpIf7-6lvrLcxHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت اصلاحی تخصصی برای آرتروز لگن (hip_arthritis) #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/666198" target="_blank">📅 08:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نکاتی برای حفظ آب بدن و پیشگیری از گرمازدگی در مراسم تشییع رهبر شهید
مدیر‌کل تغذیه وزارت بهداشت:
🔹
سردرد، سرگیجه، گرفتگی‌های عضلانی، تهوع، افت قند خون از علائم گرمازدگی هستند. شرکت‌کنندگان در مراسم تشییع رهبر شهید در برابر تابش نور خورشید قرار نگیرند.
🔹
پیش از شرکت در آیین تشییع می‌بایست بدن را هیدراته نگه‌ دارند. داشتن یک بطری آب به شرکت‌کنندگان این مراسم توصیه می‌شود.
🔹
مقدار کمی نمک برای تامین سدیم توصیه می‌شود. استفاده از نوشیدنی‌هایی مانند ترکیب «آب با عسل» و «آب و مقدار اندکی نمک» به سلامت شرکت‌کنندگان کمک می‌کند.
🔹
همراه داشتن میوه‌های خشک مانند توت خشک، برگه هلو و برگه زردآلو توصیه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666197" target="_blank">📅 07:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666196">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
متروی تهران از امروز ۲۴ ساعته شد
مدیرعامل متروی تهران:
🔹
تا ساعت یک بامداد روز سه‌شنبه، ۱۶ تیر، خدمات مترو به‌ صورت ۲۴ ساعته و رایگان ارائه می‌شود
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/666196" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666195">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e2332db0.mp4?token=CL6DoKCn0E77ch2B1V6H8egF6RsmxOAa1fjGM58-azClg-HesyhFtQazkBkjfQVhHFWGQj6PPs5SSyEg5EZgEPQG0RzJa0YB6Bsd72P7ZaHyGnJ20Xv1q01O8Kch8B22pnQ4uYtfw3DTIiwAWuCNTvi684G1fxiOsuD4HIlEUav0FajRSopjvjPIM-Z8-xLNnxS2x9f5uRSSgy8XCLGfsrxju8yOuUMCSQ025WNpT2I2UcMtBnSCyDv_-JhX9kGXDRZEIm482d6A3OpR7vkpXC0EZ5mAkKZsesl3Nl_L0HBz4B4GqYBBTtZi5JjLaFJDWxyHmIxiTPWfBORpD0n4PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e2332db0.mp4?token=CL6DoKCn0E77ch2B1V6H8egF6RsmxOAa1fjGM58-azClg-HesyhFtQazkBkjfQVhHFWGQj6PPs5SSyEg5EZgEPQG0RzJa0YB6Bsd72P7ZaHyGnJ20Xv1q01O8Kch8B22pnQ4uYtfw3DTIiwAWuCNTvi684G1fxiOsuD4HIlEUav0FajRSopjvjPIM-Z8-xLNnxS2x9f5uRSSgy8XCLGfsrxju8yOuUMCSQ025WNpT2I2UcMtBnSCyDv_-JhX9kGXDRZEIm482d6A3OpR7vkpXC0EZ5mAkKZsesl3Nl_L0HBz4B4GqYBBTtZi5JjLaFJDWxyHmIxiTPWfBORpD0n4PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار یک‌ صدای مردم در مصلی: «انتقام، انتقام»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666195" target="_blank">📅 07:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666194">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=DukTmsGc1gInhHgYAgRBqTtXYTJnBRKcfV5G3nK9nvpDWRAIJZLJo_WJJL3IadpmvMzueLI7ANrZvxfZ0RMPftX3vKU9B6E071gmCwOOu5_b9fm-PVsKWDdAZKW_i5JRFobs1et3DJnx5spkb-RhRjiCsxeyNgN7xve_ZjJotTOpwnj3nq4RlR1E5oLJhEGy8yvvx6yGHD5mOm2ih4aMIUVfoB7nR0uZUmmVm8PlI2Xuxm4BsKb-NB-KjkPkMuReTUy1ygMrm4Bnuo6NmMFQC6YXOuqiOtwfvUoKWhevz8JP8rPVpvtIWWq3vLYaq9Nqx8N77JLF8O73LTGZeZCx1x_dADCEPVPG9DOzWcG34mXg7pW32z7MlCfmUH8G5DqexFiUgfnmCfMwnL97w9sijyWkwOw2e7JZcSqX690BLeYKquP6afXzY1tyiq49Yvk4yqG5lc88tvsflOVT0K0gXQFiK0e57BWW8ZXXdI4CMFLLV06uHWLMc8Heqtw1GS043SOycGBAOr2ExWQjQu92yY3nUnQZ0hn2GTu9d_06CBFPWo5wwKqIMxiH8DA_zVExIBYmiUglqB4zBn7-dJ9haTqjv2eonPcCiUV37fjB8rDU88ESKdZsY3a2BEx0jlIMOeLeMb2aHiQ8XlWCVWnDVFm3LxKodprvVMsQHz9Ovz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13d158d39.mp4?token=DukTmsGc1gInhHgYAgRBqTtXYTJnBRKcfV5G3nK9nvpDWRAIJZLJo_WJJL3IadpmvMzueLI7ANrZvxfZ0RMPftX3vKU9B6E071gmCwOOu5_b9fm-PVsKWDdAZKW_i5JRFobs1et3DJnx5spkb-RhRjiCsxeyNgN7xve_ZjJotTOpwnj3nq4RlR1E5oLJhEGy8yvvx6yGHD5mOm2ih4aMIUVfoB7nR0uZUmmVm8PlI2Xuxm4BsKb-NB-KjkPkMuReTUy1ygMrm4Bnuo6NmMFQC6YXOuqiOtwfvUoKWhevz8JP8rPVpvtIWWq3vLYaq9Nqx8N77JLF8O73LTGZeZCx1x_dADCEPVPG9DOzWcG34mXg7pW32z7MlCfmUH8G5DqexFiUgfnmCfMwnL97w9sijyWkwOw2e7JZcSqX690BLeYKquP6afXzY1tyiq49Yvk4yqG5lc88tvsflOVT0K0gXQFiK0e57BWW8ZXXdI4CMFLLV06uHWLMc8Heqtw1GS043SOycGBAOr2ExWQjQu92yY3nUnQZ0hn2GTu9d_06CBFPWo5wwKqIMxiH8DA_zVExIBYmiUglqB4zBn7-dJ9haTqjv2eonPcCiUV37fjB8rDU88ESKdZsY3a2BEx0jlIMOeLeMb2aHiQ8XlWCVWnDVFm3LxKodprvVMsQHz9Ovz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصلا نمیشه باورم...
🔹
لحظاتی از شعرخوانی حاج مهدی رسولی در مراسم وداع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666194" target="_blank">📅 07:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666193">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4w7OmmOY5sX3NK4QN-K5Pio9h0ztZGVuYFs0pX6ra923rzyJNhN6nFGHBCz_tFNU3JLoNReTemumgOIk2iGmVmC6kVNhjmWq406Q-LRbbO8la2fpz0Y84NTZsxhoUPcXhVnGezuLxsZChKHUPnrdMAaKR83TD7r3JITQWNvQloNM1HAZ4bjTkvIF_bwbARyaJVbR2THgupPXOBXJRaOLyHG292XOoLwf5lvYyOuV-vjjqsG-P3LZjpggpmoyPlqBVNPZtJGc9FmMvmISSR_h0WfPMDdX2wy0CehQ_mozBgM_OIXxi2nkLFdWS6l0JPGkx4ZjJTy3ilVhGWdisB3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفتن تأسیسات نفتی بندر سن‌پترزبورگ در شمال‌غرب ساحلی روسیه توسط پهپادهای اوکراینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666193" target="_blank">📅 07:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666192">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32082aa377.mp4?token=cqUXcQjtajkC-z7LTF1V_Bz0_pwsSyS_t4matsNx5DzBYd2NjodBJJhzlr_aypRJP8hFqMFgaW7hvJHX_qo0jZiqB652qQh0YcZikCvRHZa0J4x8LnzG1mJtbJFu3vBDuhlTKDT87pszScHFF9A-RnhTUkNxOlUZ2Fc_be_geuKRji8t9yJvNocnO93td3jPyMEOgRhWOdb0fBUVO6K36jAxNPt78Bde1QAXBjc1AnXzInfH9x3_MLG--gxeOu4fif0iacE_EXphxcmbmxR3RZVsFHUQpZlHuLDvkpm7sC1WCxk9QkpARVN1HrjrAGzNeODP_9ViBYCGcMRHceegsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32082aa377.mp4?token=cqUXcQjtajkC-z7LTF1V_Bz0_pwsSyS_t4matsNx5DzBYd2NjodBJJhzlr_aypRJP8hFqMFgaW7hvJHX_qo0jZiqB652qQh0YcZikCvRHZa0J4x8LnzG1mJtbJFu3vBDuhlTKDT87pszScHFF9A-RnhTUkNxOlUZ2Fc_be_geuKRji8t9yJvNocnO93td3jPyMEOgRhWOdb0fBUVO6K36jAxNPt78Bde1QAXBjc1AnXzInfH9x3_MLG--gxeOu4fif0iacE_EXphxcmbmxR3RZVsFHUQpZlHuLDvkpm7sC1WCxk9QkpARVN1HrjrAGzNeODP_9ViBYCGcMRHceegsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
و اما آخرین دیدار
.....
لحظه پخش صدای رهبر شهید انقلاب در مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666192" target="_blank">📅 07:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666191">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=GdQUcUWo9bRn4iJF1-TM1_0rIHgDPMrzzrmbdUUOvzwYuAfit6DCILeuvRflkujVkP61mEbtoFVrJyx5fhb6kS7dz-UIQSTl9SKSZdjzotLEJn1fJgjzNVUfXpliuVZyRee1mHrSg2DX_zTJ3UObhX1vVTrlkIbPbhaQCSGvjGULB3DaE5y_irAMd8SehfYVfnq_BueN3FyfpAUJC5kUd7NEy5McJHcYMWNzc1V7Zn2PR-KS6p1A6ZC5wnIyM8u38i_sut4SpMKqmb-j5QhsuFlx0lf_2xBarDbwcUf13q-pTl2bFbLPIlC7KxTD56AfgswqbCHqr3vXAn257wXhWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db21ec429.mp4?token=GdQUcUWo9bRn4iJF1-TM1_0rIHgDPMrzzrmbdUUOvzwYuAfit6DCILeuvRflkujVkP61mEbtoFVrJyx5fhb6kS7dz-UIQSTl9SKSZdjzotLEJn1fJgjzNVUfXpliuVZyRee1mHrSg2DX_zTJ3UObhX1vVTrlkIbPbhaQCSGvjGULB3DaE5y_irAMd8SehfYVfnq_BueN3FyfpAUJC5kUd7NEy5McJHcYMWNzc1V7Zn2PR-KS6p1A6ZC5wnIyM8u38i_sut4SpMKqmb-j5QhsuFlx0lf_2xBarDbwcUf13q-pTl2bFbLPIlC7KxTD56AfgswqbCHqr3vXAn257wXhWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای ناگهان عزم سفر کرده، خداحافظ...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/666191" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666190">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1I9Yb5Nj1XPe4h9Vrxbo6RyqWsddyf2rTRYUNGCiN-ILe872T_fx21MWdQYvTnFKSTL3k_1mPIJj6LHM56Gh1znO4fU5z2392_BsS4l2kKHt0KAvr83HavlYFj9OfqiljLTKYUCfWbTdYBsNuYjnMTaBCdlk2atnnwHunSYRmToLctJpyjAtXAWNNCpGMuJT-Na3Z61jz_xvkmH2mBzWOqFOHD4h7cgG_7HO-nF4lfr2F764ZAhzqwMihhDGSfB3pG6JGfQVrr7zQtB1ZWd_-dmGTPi3j4XTo2HWsEXYdz-eOgj16r8x-csI9VJInkUR2dk1Q6M7MMtxylMNfPBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرار گرفتن پیکرهای مطهر رهبر شهید انقلاب و خانواده گرامی ایشان در جایگاه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/666190" target="_blank">📅 07:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666189">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce199e3827.mp4?token=t5i4dxK-Rf5IZN4FWus-W2dmtaMe8JpRRwmPkwb2uyCNpJEsBIPmsVKFRwjrV4hMtcQws83KBGVLGHu2q0iMJ0TDv2lFx-GuQQzqmWkAOanTadB1X8h-pchGqT1Z99yJn0CLMnEWHD8XvMjWQUThzulbQwlO-Hwe-anKoAOLkVm63TpvLnsbGPIIZJrs7fUSXroi1o_L_nufYQYGSxWsN9WPvINpmZOZyY-FlMNhTif6p3BJR-8n1UAePMK4HVcG7VtKz8zJNINnNMBMoJBmYkGecybXwZJUpqI5JYyJkubecUGuZOUW_OmeSlAXJdr1PM0L0vGzdY-D6nafLGcd2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce199e3827.mp4?token=t5i4dxK-Rf5IZN4FWus-W2dmtaMe8JpRRwmPkwb2uyCNpJEsBIPmsVKFRwjrV4hMtcQws83KBGVLGHu2q0iMJ0TDv2lFx-GuQQzqmWkAOanTadB1X8h-pchGqT1Z99yJn0CLMnEWHD8XvMjWQUThzulbQwlO-Hwe-anKoAOLkVm63TpvLnsbGPIIZJrs7fUSXroi1o_L_nufYQYGSxWsN9WPvINpmZOZyY-FlMNhTif6p3BJR-8n1UAePMK4HVcG7VtKz8zJNINnNMBMoJBmYkGecybXwZJUpqI5JYyJkubecUGuZOUW_OmeSlAXJdr1PM0L0vGzdY-D6nafLGcd2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری ماندگار از وفاداری؛ با عصا آمد تا با آقایش وداع کند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/666189" target="_blank">📅 07:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666188">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090512834a.mp4?token=nsq3y8gGIGzVKJZ6fUFHVfVrs_GUwweIMx73tr6y3Zj4VdOZOILVWowLZBWfPF70GCh18BIYoFFOJKSOaJZ3hpI-Pwr8UWcfKLSp3UoAQfFxIzeF2vRP8TuvfeJ84fbQ4qplGc1iy6pc-3CjsMfoLuxLDRJlm0db7IMzw34JWS_tFhAQgBRfsiYLKptt0F-9qZWlYFq0a3M4kz2TCneYV2BclTTU_TG86U6EDC7PCWQgjeq1ZppalOAeFTnSafcCStSXbBe6mcHOdTO_NAU1P8kpUb647CAfWhcNzqEVreULrec4esyLY65bPlVO6XTkiuNkuXiXaGttNAQvZFj6mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090512834a.mp4?token=nsq3y8gGIGzVKJZ6fUFHVfVrs_GUwweIMx73tr6y3Zj4VdOZOILVWowLZBWfPF70GCh18BIYoFFOJKSOaJZ3hpI-Pwr8UWcfKLSp3UoAQfFxIzeF2vRP8TuvfeJ84fbQ4qplGc1iy6pc-3CjsMfoLuxLDRJlm0db7IMzw34JWS_tFhAQgBRfsiYLKptt0F-9qZWlYFq0a3M4kz2TCneYV2BclTTU_TG86U6EDC7PCWQgjeq1ZppalOAeFTnSafcCStSXbBe6mcHOdTO_NAU1P8kpUb647CAfWhcNzqEVreULrec4esyLY65bPlVO6XTkiuNkuXiXaGttNAQvZFj6mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طنین ندای ای پسر فاطمه منتظر تو هستیم در صحن مملو از جمعیت مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/666188" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666187">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=VUZ04HanBhDWPQX9IgJkLAMZuvDcIzR9dTt0OwnZ2ATUxXmGhQpoQBnhgMECAzWqgbDo9NvQMEiobS4N3f2TKbp8ukCSMcmEpxsIfqeJgADGySo0pWKFyQLwJYHmi1EC36-rN59Mp5neK8vA3EcAv-1u2UxOR_lcjiYRu3WsvLN-ocIbvOwskro0Qo6nKlsJ9q-U9B-5aFQLhqzUbeJXE2YEm0kwiZNzr1fMlOQ_kdh7eYg9hOrG-Ihw4TD04G4Px9VKMfnzQ1AlvXTSmMsqiV_m6hXKSZnqOakeQoSJtkSbmsSWIN-1jgueiJaXfzCaxMaeMSTB4mDO3zJdMxcl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4f7f5387.mp4?token=VUZ04HanBhDWPQX9IgJkLAMZuvDcIzR9dTt0OwnZ2ATUxXmGhQpoQBnhgMECAzWqgbDo9NvQMEiobS4N3f2TKbp8ukCSMcmEpxsIfqeJgADGySo0pWKFyQLwJYHmi1EC36-rN59Mp5neK8vA3EcAv-1u2UxOR_lcjiYRu3WsvLN-ocIbvOwskro0Qo6nKlsJ9q-U9B-5aFQLhqzUbeJXE2YEm0kwiZNzr1fMlOQ_kdh7eYg9hOrG-Ihw4TD04G4Px9VKMfnzQ1AlvXTSmMsqiV_m6hXKSZnqOakeQoSJtkSbmsSWIN-1jgueiJaXfzCaxMaeMSTB4mDO3zJdMxcl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت بی‌پایان در خیابان‌های منتهی به مصلای تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/666187" target="_blank">📅 07:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666186">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8c335e616.mp4?token=k0OHEbu-YIYILvrbYeHNY2VTv_CJT6IeJzPq9E7yekUpPHzs1edVRg_gqDr_m8HbuLpN0Xc_6ZlxhlmAibVmDLQ97fsxB9HUl6raFB7BTsGZJGG_c5zCliCeDZOY2rAC7VuDiEXn6nryFUW00ceA4ORA2A7L_yupgmUKLlSCbw46R1SYioNJDWMYypUL1Sg8HPf5az88WCnWFTFotNsJSw061QBe8WgEbxOTE7H3il_7J7V87wDzaALaS2RH2lsYqIKMC2NypWyerLPY3bmzxBkccYnkk66pveuq7UcCWT-SZaWtOgrrqIldFMihcclJXth3rT_7QDwIoSwU8f7d3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8c335e616.mp4?token=k0OHEbu-YIYILvrbYeHNY2VTv_CJT6IeJzPq9E7yekUpPHzs1edVRg_gqDr_m8HbuLpN0Xc_6ZlxhlmAibVmDLQ97fsxB9HUl6raFB7BTsGZJGG_c5zCliCeDZOY2rAC7VuDiEXn6nryFUW00ceA4ORA2A7L_yupgmUKLlSCbw46R1SYioNJDWMYypUL1Sg8HPf5az88WCnWFTFotNsJSw061QBe8WgEbxOTE7H3il_7J7V87wDzaALaS2RH2lsYqIKMC2NypWyerLPY3bmzxBkccYnkk66pveuq7UcCWT-SZaWtOgrrqIldFMihcclJXth3rT_7QDwIoSwU8f7d3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این جمعیت عاشق داغدار با پرچم‌های یالثارات الحسین برای دیدار آخر آمده‌اند...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/666186" target="_blank">📅 07:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lqCqAROORw-VXYXjC8OF138tdmNv0EgyqKHnQWtGjE-MoPyO6HGSdnvJEh837m0snKVVgULsDNa-FmaJFJZapF3bNeMrPBbw_NxvB1hVhZC4X36INyxzZk7rdS_jHvypxfCU15v4JqCZrEYArcLSEekUNb73RiI81ASS4PCKX8qy4OyTGE9JozyNXrBPPlsLO4oJbuLGsdk5WU0wH3KSazCsWQwe3uhV8V08r7G7VOoYFfzlEsE9_OCzB60d1gtrRAS27chP3zPQHk3JH-SYv0dDW2Ev-XVPwDPYB-wpNp3FB-u8S_HyHf0ozTJXJ3Qpidg1YlSluHR31E8EhpMzjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tELJ7CMWs2L49m8dW7-c9J-a6L8KqPEkINJDmZd_KWAuRgyBUnVnsvAp89jvq95CjyKp6ga82gV8kw_I5T51QUrJYZyUJKaKJPGew3v_-7AxXioCFSoY5M8joGgBZEU862Oy-1gxfZz-k9qeGV5TPwbOYg23gzksux88Nf4Omj9IjL3v162yGHY3eZY6haPXGvyRwL7l4Ls9cb0yevm1lT961vfzIy03LcKrD490tJ3jb_CzNNErDFrY1hBJw7cJC8JsJ-mL9YgLPzN6HphlTxFL6W8EnNN7MhRJjhdkoRdFORD_Bybf5n77A1RW2Oex_4JH9tez_Dl4E-BSbEEudA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ مصلی امام خمینی (ره) تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/666184" target="_blank">📅 07:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_HC8eS_UdLjK3YneTp9DbK81vr8m2BN85iahdxPT6lG7I-x0bnpIfNqBA8YtZDZ6PV6wJZxS8or2iEEshYV00vCkwsm_uvVl3w0eJiwM8GKnzLbG_v5GhXvcyPHfQ6e7q6holx65nTjhN8ePe7tz0DOQytLro-RtwV5kztlSBZr_aX3_j5JpO86xvSYOuv9UNhlGNt_2prZJzqxGfNKbiDbSDK3tbZwp6wZpxquPKdPGBaJK_S7Wgp1FEuCMvP-vQm3FC5q75SuCL_wxawThzkv9aWlYmNONQsDBLzeoZHRqXX-WPfIwjgjCvVfLCp1HfRZwoqZ1ukSMZkK4j-DwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار جدید مرحله حذفی جام جهانی ۲۰۲۶ با اتمام مرحله یک‌شانزدهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/666183" target="_blank">📅 07:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25dfa59cbb.mp4?token=L3Yx4_gTbXj1ZOW6Zg_1c9DCwiDYKJ3RE7CZtBrFv1zfE35NwjoDQyUraMOE6dys3lv_oSLPX74kCYaAx18_prEjl9R3OBAt6hnCDH9HgpPjXquVlzHCpHhfcvTb4L-0jCrtASq4v895H0zNTpz4NRfCqZtNd6B8BumnCPOAIKSmlNObvnF_sgwXy7wSNtPyOVgMRmBX8Nr8nXbKugHr3ufke73rLFGHBB67ZIFkpRN3YXgmuumje507dWfBOZ0fZRPmCynE69WWJSv5GrU1y_jIU2XnRZPyNIHoGZKrRw5z_htMTLnfpPbgY_wvADx22_SeXEpnIo4W-Gf4ye712g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25dfa59cbb.mp4?token=L3Yx4_gTbXj1ZOW6Zg_1c9DCwiDYKJ3RE7CZtBrFv1zfE35NwjoDQyUraMOE6dys3lv_oSLPX74kCYaAx18_prEjl9R3OBAt6hnCDH9HgpPjXquVlzHCpHhfcvTb4L-0jCrtASq4v895H0zNTpz4NRfCqZtNd6B8BumnCPOAIKSmlNObvnF_sgwXy7wSNtPyOVgMRmBX8Nr8nXbKugHr3ufke73rLFGHBB67ZIFkpRN3YXgmuumje507dWfBOZ0fZRPmCynE69WWJSv5GrU1y_jIU2XnRZPyNIHoGZKrRw5z_htMTLnfpPbgY_wvADx22_SeXEpnIo4W-Gf4ye712g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شروع رسمی مراسم وداع با امام شهید امت با تلاوت قرآن مجید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/666182" target="_blank">📅 07:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c898339bc.mp4?token=LzbE9-_iOY-CcaN5Pq10dnS_uikUlm9FVVNzseD7I2LJ9KtPf_sblkX-vG9uU2RYFmA7wr2gLccArEBmLebpj4oq1ls_raEo-_9cxaCgp3rwVxetkY_u3FNIa_J_jsQ6K-qwucOac6F5_v43KOREvKNK8YxbdqmWisOhbso2he1BsngIywh_pqqlX48uHG96TqS1r-bD4gujvOWjn_iN-mvKpnUc0rwnk4O0llMo7BtXXSQ_TW1wbqXptyq2WxJvIDl7D8EEkgvS-aR0wPZ16EFCQpt8WpDZPkmbam61fGOf7HSfDiOaVSgo8rvGRIlRvtMOKNRhbMUVqH3lJCFz1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c898339bc.mp4?token=LzbE9-_iOY-CcaN5Pq10dnS_uikUlm9FVVNzseD7I2LJ9KtPf_sblkX-vG9uU2RYFmA7wr2gLccArEBmLebpj4oq1ls_raEo-_9cxaCgp3rwVxetkY_u3FNIa_J_jsQ6K-qwucOac6F5_v43KOREvKNK8YxbdqmWisOhbso2he1BsngIywh_pqqlX48uHG96TqS1r-bD4gujvOWjn_iN-mvKpnUc0rwnk4O0llMo7BtXXSQ_TW1wbqXptyq2WxJvIDl7D8EEkgvS-aR0wPZ16EFCQpt8WpDZPkmbam61fGOf7HSfDiOaVSgo8rvGRIlRvtMOKNRhbMUVqH3lJCFz1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم یالثارات‌ الحسین بر فراز گنبد مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/666181" target="_blank">📅 07:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr5T4RbYMJx9nkcz9Xl22aAbIPXGZn0u2aNZnBmc_p7-Plb_4RSSjP58XykZKlrUXLn4sz4_fNiyLyhaxmU3XvAmULD5uT0LSCuKJsNxOf2C-GjSer8vdMZAX_FxvL1k-f2rx3EQeUZQSTAZ6nCkNYG08I7cXrmm0l1UiLG213gvBmgCiWBl7HNwm6rr3DXk0EdFbcsNsMb4RpzGiZ0g83blfKxCcsmMo0MsoCPlU3tGnk6vIK3aiGcM-kHFxfi9JQi-zr4NYxIuZJwJQBWISUZewb2d9oBpbN1VUrhhTgGyrOtWNIH-HDMa59qNQ3PQ2NYj1c893mDClMB_gKnzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیتر متفاوت روزنامه لبنانی الاخبار: «تشییع قرن»
🔹
روزنامه لبنانی "الاخبار" با انتخاب تیتری متفاوت برای مراسم وداع با رهبر شهید انقلاب و حضور مقامات ارشد کشورهای جهان، از این رویداد با عنوان «تشییع قرن» یاد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/666180" target="_blank">📅 07:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck-5SFIrlCcDrnePMGyO-2s15qfrw-7B8LUYYwwhm2KFPx3ahzluQXOlu7fxcg-XLWsNZZlRAGpHM-weV6NKdZOnerqqFDayqx9s4uGVzJ0jLjgaLUZvuA4WRDIpj9NRGH9IlMMrhtGMGIITSLXmbqs-iX9Gah64FSa9WPdLeoPZ8INzyAH301enrqWvWw6fIFkBy4-36BbHaBJcPSc6tuANL9eO_3an9UC6smNP3-viwHdIWKS7lst0Dbh7aY3gwY3CHxG-63v-gkywkc97liL6q1dFqO3HGhf-XYukfneaB6_7KX7pj96ozn6cGkhswKiGWrmUGytIHNQBEbUl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهمان گرجستانی اولین روز وداع با رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/666179" target="_blank">📅 07:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
نمایی از جایگاه پیکر رهبر شهید انقلاب در مصلی تهران برای وداع مردم ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/666178" target="_blank">📅 07:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671d6d7cfb.mp4?token=nv2VFA7znHB7djwyVOejcC5bALT9CUSBi5CqYsdH69u_UhOWdo-VkPpN6zLF8VwJxwQc9086icuYIqPLltCM_5Fl4tTE3VsLW2pJlbaEdzHfOd9vtpB2jSjxw8hAN15OeRZWY1RDo7OqICUT_ZrDyNfVQ2OFELrTXVxhv8gSbiUiXK4xUtirZMs1cqgTHiGh8F8vRXT5DsHxFWiPQcES9YPvRfoxuM3CnbZ5h2WOiKkD--ZLtx-Yb6X-IuY8nUT9yGjA_cyY23N_03LSiykcTJus7sMS-bcthuawz6Y6W0KSzdT98DQdgxHCbsRRApDIwZVrF3nF0pvGhI43FNmXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671d6d7cfb.mp4?token=nv2VFA7znHB7djwyVOejcC5bALT9CUSBi5CqYsdH69u_UhOWdo-VkPpN6zLF8VwJxwQc9086icuYIqPLltCM_5Fl4tTE3VsLW2pJlbaEdzHfOd9vtpB2jSjxw8hAN15OeRZWY1RDo7OqICUT_ZrDyNfVQ2OFELrTXVxhv8gSbiUiXK4xUtirZMs1cqgTHiGh8F8vRXT5DsHxFWiPQcES9YPvRfoxuM3CnbZ5h2WOiKkD--ZLtx-Yb6X-IuY8nUT9yGjA_cyY23N_03LSiykcTJus7sMS-bcthuawz6Y6W0KSzdT98DQdgxHCbsRRApDIwZVrF3nF0pvGhI43FNmXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور گسترده مردم در ساعت ابتدایی نخستین روز مراسم وداع با رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/666177" target="_blank">📅 07:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfF7G0IHQHL5C9XXVOncbnTHZh0lptR6-RYV3dZpXbg7DLhvO9DgpR8ho74ATHrbCiKm9UQTAhKLB5aUrh84iAtL-EXenHTOi6_E6x5sSTUQe1qCIRYSwPptCVHy7sPTG9r0ECA4zzhJHJ6QlhyWYJqDY0j89xjC8PTyHCRz_AWJJevkkN-X36H9zz1CsI1m3FnVsMWLFNKNGsLVpgK_wQsDGa1vGOAMlOJrxzwrabH0OsbMJJP0egLXoWsnFsFJ_EE2t2-tMZRyQ2Xgzgugrzdq1KT-e-hPJP6hcWt-k8o1HCgZO4_Bj4plGZC-jBCMNx1Kisu4a3ArqA1fDvxRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۳ تیر ماه
۱۹ محرم ‌۱۴۴۸
۴ ژولای ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/666176" target="_blank">📅 07:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d543c6c364.mp4?token=qp5NYpcoM6Xpp3cKtuODzFVB2EY8I5KpUqp2_-Wi7554-u2nrYsUl9kuV4SljZ6aF3C1lpT4i1tNyR5penlP-EkgdtqBZBJxNi3jWKUU-xk7yV-vAb4f12LRTomc-DT21YiE0HiriqmkbI-wofLNzCNT8NlbcxhvWD2OciUHWawfO57EqKW5p9lbbL4AE9RDBjNfrU11z2mckPuFOp1CG-Kqps13iMOBNvotl-HtU5Q3MJKhx29UYb8O8izgYkFJKrdrDqU_K-D015V2NSknzF0pQxom4Ro7-0tgjSR1YcaOmafpFRRzMWEZyvq4IBrytR2RRhcY49R5J0Bl7gMozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d543c6c364.mp4?token=qp5NYpcoM6Xpp3cKtuODzFVB2EY8I5KpUqp2_-Wi7554-u2nrYsUl9kuV4SljZ6aF3C1lpT4i1tNyR5penlP-EkgdtqBZBJxNi3jWKUU-xk7yV-vAb4f12LRTomc-DT21YiE0HiriqmkbI-wofLNzCNT8NlbcxhvWD2OciUHWawfO57EqKW5p9lbbL4AE9RDBjNfrU11z2mckPuFOp1CG-Kqps13iMOBNvotl-HtU5Q3MJKhx29UYb8O8izgYkFJKrdrDqU_K-D015V2NSknzF0pQxom4Ro7-0tgjSR1YcaOmafpFRRzMWEZyvq4IBrytR2RRhcY49R5J0Bl7gMozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج قاسم برات مهمون اومده… آقام از میدون غرق خون اومده…
🔹
بدرقه آقای شهید ایران
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/666175" target="_blank">📅 04:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چهار نشده در را باز کردند و غمی عظیم به حیاط مصلی سرازیر شد. غمی که آدم‌ها با خودشان از گیت‌های بازرسی عبور می‌دادند و هیچ‌کس نبود که غم را از شانه‌هاشان بردارد.
غم به‌جای این‌که تقسیم شود تکثیر شده است، با همان وزن، با همان اندازه و آدم‌هایی که داخل می‌شوند همه خم‌خم راه می‌روند.
دعای عهد از بلندگوها پخش می‌شود و آن‌جا که می‌خواند: "إِنَّهُمْ یَرَوْنَهُ بَعِیدا وَ نَرَاهُ قَرِیبا" به تصویر آقا نگاه می‌کنم که زیر یکی از ورودی‌ها برای مردم دست بلند کرده است. بعد فکر می‌کنم که قریب به زبان ما چند سال است؟ برای ما که توی همین صد و چند روز صد و چند سال پیر شدیم.
به سکوی مراسم که زیر ایوان است نگاه می‌کنم. زیلوهای آبی، پرچم‌های ایران و آن صندلی که روی قلب‌ام نشسته است و ده‌ها هزارکیلو وزن دارد.
آفتاب هنوز سر نزده است و من نمی‌دانم امروز اصلا خورشیدی طلوع خواهد کرد یا نه!
🔹
به قلم مرتضی درخشان
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/666174" target="_blank">📅 04:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kw6R4bjWL7VyhPUZoQ0-EpNmIEPxYv99lF918-lQzFb8rpMJM3PFEJqV6BsveKgYYlTDs3g37s-Gh5z6b34Bj00kdmuM1AmK1EVgQgJRrbz3m-ZKWjCbJ2keTfF6gfM-MZNy13nLW4Jaxt9jtJbFMHi1msxE9W76sNxZ2orhgSJ0fUixZQcbfxhtS1TQ3mT5t3paql_TC-krwpB3oUBdprcKBnnZ9JScAICxgLaxuoiDkUtm4TjUK5lfvkATmSCvw5F4MBFRS-8ChXDkN8A59xKnw6oYTuxR5g1NgZlMz0G5k-L0BXNPJRyQN2r9p2DBTH64QlK0Hk0tKAQUz5ELMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و زیلوهای آبی رنگی که آمدند تا برای آخرین بار فرش زیر پای آقای شهید شوند
تو چقدر با وفا بودی زیلو..
💔
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/666173" target="_blank">📅 04:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=gc7z-3Fsugc9T4TVB401hnfCmOL-w5S4nqkNlA1IRyU1xUiWWTH6M6TUPhA5iA4Cm-711pmA3hbUcSRHgsmHU2NCnMF5kx2FtVbzIao2sUzWGNLX1DTtrB0rsxE0sQQo_SafYQodeEUx53i8D18tAcWdKRRsrQOVjSoZn8AJagMmSqXoUCnWN5JzsOjDIHiEQ1lpM-G_9LLXdJcSTcmuBo2ZQlZfYbZlgMhDCThvTAPTlwY-QTgP3sQlfGGOtZQmQ4vPL4n7L6tnz0k4TwtfsXZNSl9VmZysTRrgTEN-kJ9P6gLYgqaSGHhZf8BVtxD7AeAlbgkcbdqVyVo5l8uNhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=gc7z-3Fsugc9T4TVB401hnfCmOL-w5S4nqkNlA1IRyU1xUiWWTH6M6TUPhA5iA4Cm-711pmA3hbUcSRHgsmHU2NCnMF5kx2FtVbzIao2sUzWGNLX1DTtrB0rsxE0sQQo_SafYQodeEUx53i8D18tAcWdKRRsrQOVjSoZn8AJagMmSqXoUCnWN5JzsOjDIHiEQ1lpM-G_9LLXdJcSTcmuBo2ZQlZfYbZlgMhDCThvTAPTlwY-QTgP3sQlfGGOtZQmQ4vPL4n7L6tnz0k4TwtfsXZNSl9VmZysTRrgTEN-kJ9P6gLYgqaSGHhZf8BVtxD7AeAlbgkcbdqVyVo5l8uNhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه‌خوانی نریمان پناهی در حیاط مصلای تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/666172" target="_blank">📅 04:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c5542627.mp4?token=MtZP1y_V_cX7yaaj1g9MnblZG1F1NYVlvkOpR2PmEx0uYydWEYmo02QUkVU9OOtSIeH7oJrruSgtBDDV1B5Dn19NEctrR16nYC-o6CYEKQ_mZRiT2ZmGA-3bhkXkXuwRDQU_8Ddk_zD8XlbQrD47Tzd-8EsP644_sM99VaGwv46DaA6v69u-0BRXsR72eH1iXCiL07N-v8IWBLCFtblZX4-H1p-1AFDL-svB41kA9lijYFaQ3g8ehOHMKUivhCbk2n9IkS6SOfVw7AbR8v0GNwvdPRvbir3M64lqQpgok3tSCCaN106juV7ted2z-zWG6UmCg0holrJcqgCOIGsY7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c5542627.mp4?token=MtZP1y_V_cX7yaaj1g9MnblZG1F1NYVlvkOpR2PmEx0uYydWEYmo02QUkVU9OOtSIeH7oJrruSgtBDDV1B5Dn19NEctrR16nYC-o6CYEKQ_mZRiT2ZmGA-3bhkXkXuwRDQU_8Ddk_zD8XlbQrD47Tzd-8EsP644_sM99VaGwv46DaA6v69u-0BRXsR72eH1iXCiL07N-v8IWBLCFtblZX4-H1p-1AFDL-svB41kA9lijYFaQ3g8ehOHMKUivhCbk2n9IkS6SOfVw7AbR8v0GNwvdPRvbir3M64lqQpgok3tSCCaN106juV7ted2z-zWG6UmCg0holrJcqgCOIGsY7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مسیر زیارت رهبر شهید، کوچک و بزرگ وارد مصلی تهران شدند
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/666171" target="_blank">📅 04:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
درهای شمالی مصلای تهران هم باز شد
🔹
درب های ۶، ۸ و ۱۱ مصلای تهران در ضلع شرقی و درب‌های ۱۹، ۲۰، ۲۱  در ضلع شمالی به‌علت ازدحام مردم پیش از زمان اعلامی برای آغاز مراسم به روی مشتاقان زیارت رهبر شهید باز شده است.
🔹
مردم در انتظار ورود پیکر مطهر رهبر محبوبشان به جایگاه تعیین شده هستند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/666170" target="_blank">📅 04:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOsQqCVXhZZiizw1wkdlqUehwH0mUINhDy2D8o235g5XAt3bYfogiPkEOAPFYv_yBnR9Vek0YVNp2sc0OZRgUAzpZW6VVfoQgsELAe6AqIhbkNXv4RNYKviGzjyucKuDNx7RLhJOzmxBn_jiVp4QBf_QzFGRF_fsXlgnbyoDM7wyrC2R8bIMrGW8FHgQ-_3B9R3Q9jP_2nH5dmmWd8VueCbOnz1KBplw2jzamwc_95nYxOlyJuCSGSdjJiZXdy3DTMrCvX2Lot0Q8Q1UU5aTEEYGmO9VDe5DerCGP5k0CqOAImZ9OtbFhG2gGzHaSXi7tIKHYscTJwfFzNLbR_6g7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی از فراز جایگاه پیکر مطهر رهبر شهید انقلاب و افزایش تدریجی زائران به صحن مصلی تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/666169" target="_blank">📅 04:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA1FiLsfz3lmECj1kEw9wl01fdgYnksei_kTRUGDwy7pG0kKmOAODAlpBopsRU8I1Z1ED0BwCuON50OBA-OBtv8UmhSktZ5TUCzBDGTcNmbFTOG8N2iPA8M5K9kIa3W71S5rhwo0gwvjRIUIQPsdN2u8zelYVIFZIDWrb58LjZboJGzFbVBhH9vhvy_PZotuzGB039wor5B4K-s2anftRbkg3jj8qQMGsQ5aOLHx_BL3TuE0Ag6uu5OcxqtA1Q5pKBEjYASB00pkDu3XRWAW60bQZ_YRFdamGP55T2b_4Bvq-4yJmn1lKE2WplOmdxEgmMAMnNCteee1-Q5DnqHn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دقایقی قبل رفته رفته درب‌های مصلی برای ورود مردم بازگشایی می‌شود
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/666168" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666167">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a51b0270fa.mp4?token=CAvF_C9SHw84xMxw9KwTkT7W4pSva6RT1YUH2HC6t6fMjALus6eJBfo-ya-z_tfSzPWeJlXMkFwyTTBiqOXiRzcP0PEiGYdPSWvDtUhD_Gap4aQS4ZQFxSEszXQHe_GPc56hzrfuOJcqyzlShIY3we2knZ3riuLzxRCwlbUlXbhTZMrG92Kv8SPRoJUTz6UV2sxkAkWRyvkEcFyRcM1RXvRcYnz5zLuGO73I4Vhdht01n1MNX8f95EpNyCrgiTQ0RzezoDGhLVbpoYoQxstpyIUmx7z8GEERktV1IIvkK_y06YM-3IQz2D18DSz4dxeQUvnvBHQXM9YMk_UdExg_VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a51b0270fa.mp4?token=CAvF_C9SHw84xMxw9KwTkT7W4pSva6RT1YUH2HC6t6fMjALus6eJBfo-ya-z_tfSzPWeJlXMkFwyTTBiqOXiRzcP0PEiGYdPSWvDtUhD_Gap4aQS4ZQFxSEszXQHe_GPc56hzrfuOJcqyzlShIY3we2knZ3riuLzxRCwlbUlXbhTZMrG92Kv8SPRoJUTz6UV2sxkAkWRyvkEcFyRcM1RXvRcYnz5zLuGO73I4Vhdht01n1MNX8f95EpNyCrgiTQ0RzezoDGhLVbpoYoQxstpyIUmx7z8GEERktV1IIvkK_y06YM-3IQz2D18DSz4dxeQUvnvBHQXM9YMk_UdExg_VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج مهدی رسولی: ما در آستانه تمدنی‌ترین و باشکوه‌ترین و بی‌نظیرترین تشییع تاریخیم
مجلس، مجلس خاکسپاری نیست؛ مجلس قیام لله است
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/666167" target="_blank">📅 04:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666166">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr8wvGm6M_NiWOTQvFSnkwl0oA6b4e-BaBhzpE3Olo8LfMC4iJK7hmoz_wRB63FnQBh_V4XHtkBdAOc51HyjkWrNRl4nqPlhbfePNZYyMntuqnwWFk6mQfEP0vlANQenMvzSym6jHDZSeQQNU4MA-UMuCGYrfV0vmEFE7Ya6oTh4EhkSu1xB7m5A3UOn02g2d9k5_UcoTbD8DbaXdYX1WSw0AljPjU-zGhAGty6Re5AhHTjWuYiRfKBYxXM_a0d_jUBC6kBAvVjQgAP91_spMOJwlzieEzxXPNCVmXFrM-9svHORdFGLWNZ7atj2fPnAztcYGZvB8ZaYC0bzC2boRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مسدودی خیابان‌های منتهی به مصلی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/666166" target="_blank">📅 01:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666165">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb537e4fe0.mp4?token=NUS9O-n3SJ7n1NmjMqoRvkWS15SZFHMYUXVnorPJA3PW0r17drxfaH1kTpZYpSgRH80vhuoiIMlYDsoSv2PPCiBu09N3fLpjf69vE0C1qout4gsgtnlp7B90_WCvMzMP3WrKalT4Gnes40kBxCEu4YZ71o6Jn-LYTnuBG5UnzMPMMzSKKqyuJyTcZyUZQf0KpmYN0TdQ0VQM2TxwVDumasunYsS0kCWiHo_hMaycPjDR45nY-V3JvI2YSoNBcCW9ZDnYxn24Gpc0FrEZqDdk8qfYv7vZTgOikO4YA52jKIHvb3MUCsTF-tJKRWcdtziv7GBKZa7SWls03hdy814p-T4rSPBMz5IkxaLkKwXhFUBz8ZeNr1NqXJjagwT_cAwIXt_MHEFH9eKz_V3mbBgmA8r1z_RPaqzehcpJ2ip8afmtwqZErJVKMcy-6h_FE_5gCgC1Nt_krZBgtF_hJoJJ3tpa5BRj2gAa-IFgMLdPWK7OQkBh3C44uYu6miUZShYPx4smSfSty_7ys4krbbhJb_--0tUDwkL99qlz-6Vq1vI8ILwKmFuU2SoVc3BeZnbK-y2cFDz1UwcyG5ZeE3-XKeXAe7GYRd0Z6F5Ub7aGsqUZ2AcuzERLHBT7_BaJMvKvzLOMuuHuyuIYeXFe91BeOtUqvUl1i7BhPxnMHIKALbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb537e4fe0.mp4?token=NUS9O-n3SJ7n1NmjMqoRvkWS15SZFHMYUXVnorPJA3PW0r17drxfaH1kTpZYpSgRH80vhuoiIMlYDsoSv2PPCiBu09N3fLpjf69vE0C1qout4gsgtnlp7B90_WCvMzMP3WrKalT4Gnes40kBxCEu4YZ71o6Jn-LYTnuBG5UnzMPMMzSKKqyuJyTcZyUZQf0KpmYN0TdQ0VQM2TxwVDumasunYsS0kCWiHo_hMaycPjDR45nY-V3JvI2YSoNBcCW9ZDnYxn24Gpc0FrEZqDdk8qfYv7vZTgOikO4YA52jKIHvb3MUCsTF-tJKRWcdtziv7GBKZa7SWls03hdy814p-T4rSPBMz5IkxaLkKwXhFUBz8ZeNr1NqXJjagwT_cAwIXt_MHEFH9eKz_V3mbBgmA8r1z_RPaqzehcpJ2ip8afmtwqZErJVKMcy-6h_FE_5gCgC1Nt_krZBgtF_hJoJJ3tpa5BRj2gAa-IFgMLdPWK7OQkBh3C44uYu6miUZShYPx4smSfSty_7ys4krbbhJb_--0tUDwkL99qlz-6Vq1vI8ILwKmFuU2SoVc3BeZnbK-y2cFDz1UwcyG5ZeE3-XKeXAe7GYRd0Z6F5Ub7aGsqUZ2AcuzERLHBT7_BaJMvKvzLOMuuHuyuIYeXFe91BeOtUqvUl1i7BhPxnMHIKALbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میزبانی از دلدادگان در چهل سر، محلی برای استراحت، پذیرایی و خدمات درمانی عزادارانی که از سراسر کشور به تهران آمده‌اند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/666165" target="_blank">📅 00:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666164">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgjxVjvGw0GsbL4ahmi3IukMcVF_hrKpFJ62PaOF_6aRrdBNxu4PH2ABX-7E142NQrzbn8liz6sU3BIzKs9EwRMD4WTRtF5PKqkzGebqTGY9TBGsgLJhD8p7JmdrY0JR2XHxgFDqO_1_SlcPsxEIbSlA4BBsnc9M9eCZPI5-cMnovrRJcSTPS2Bo2onTKhGJER4EN77OvqIgF5n4iv8C9OZ5h7-9dPrBvKW6almtn90ugfFHKkPJwDCrDqzue8fUWrGE7hvCcGgLtKJOnrDVs_3fVUBO_bbI1RoAJkSdxcdHZT5fPxdOzYtrSUS15T3UklKPXAE4ZG9VcXpDEHPv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های صعود کرده به مرحله بعدی جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/666164" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666163">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxoL3poJaa_wkICiDJeaEQ_KusXJYags5mbuDYmBs-XPW1pqUeT_rRh6xD1EyAC5nk_0oD3RxHiyh26yz6gaYOIlng_rZ8666NlOpyyNFVpHrcsx0-O5-Mawfcz-hlk4kkkbMpoPIfiVBbQeh3ZaH6-3tnOmapxoA7LGJ96lGePqBnY2JRGlk4Du2LihkjshtausXhux_M7HAAn5QwDnPrxS5qJcrOq4zA6MOB55FL-9yG3KeWLQEhG7aY9_nRnp3JEY3YYoTSRn8mYC7eNvEytWFsUJq2rFUpqDKFDy6NNq0UVkpQ6vMnMxa4en1K2CvCGlIglFZ4GTe6o8sUe5jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقریبا تمام جهان برای مراسم تشییع آیت‌الله خامنه‌ای در تهران حضور دارد
ایتن لوینز، روزنامه نگار و تحلیلگر آمریکایی:
🔹
به‌ معنای واقعی کلمه، تقریبا تمام جهان برای مراسم تشییع آیت‌الله خامنه‌ای در تهران حضور دارد.
🔹
روسیه، چین، عربستان سعودی، قطر، صربستان، هر دو کره، ونزوئلا، گواتمالا، گرجستان، ارمنستان و کشورهای دیگر.
🔹
کشورهایی از همه قاره‌ها و با پیروان همه ادیان گرد هم آمده‌اند تا در برابر امپریالیسم آمریکا متحد شوند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/666163" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666162">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
خودرو شخصی به مرکز تهران نیاورید/ برخلاف جهت جمعیت حرکت نکنید
سخنگوی سازمان آتش‌نشانی:
🔹
از مردم می‌خواهیم از آوردن خودروهای شخصی به داخل شهر خودداری کنند.
🔹
مردم با استفاده از ناوگان حمل‌ونقل عمومی به محل برگزاری مراسم مراجعه کنند.
🔹
یکی از حوادث رایج در تجمع‌های گسترده، گم شدن کودکان است و خانواده‌ها باید در این زمینه دقت ویژه‌ای داشته باشند.
🔹
مردم از قرار گرفتن در کنار ستون‌ها، موانع و سازه‌های ثابت خودداری کنند.
🔹
به همراه داشتن آب و تجهیزات محافظتی ضروری است.
🔹
به هیچ عنوان برخلاف جهت حرکت جمعیت حرکت نکنید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/666162" target="_blank">📅 00:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba94eddbdb.mp4?token=omvxc8ybsT63rsOEYqJ53YvLt_wcc7G7BnWpYSjSTypJSaEY5fXGn96N0CRDpRpDPTMVdwhum0RPQsvFkf6nvu6XSwy8Z6bP9W9ckfRe6tRcg2zgna1ldV5yLrTSaHeyIKrFjXRRrfY0bWlcUfKxYR3L__YyPre3dJLEELvsTwNadtaoPCx9Cv5w-EF2fonF6OBtXEmbahyIodEGTAao8beiT0xv7uWfnkcxYVkcz9LvtBiE1uJiHw7zd-sfj0TahiKelJhCkVkSdHSYTCjcuhjDG9_BSPbScLO2z3v9BymOi875af9U7Xemr2Nai73DOd-lTM6QPdftqecJc-MhYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba94eddbdb.mp4?token=omvxc8ybsT63rsOEYqJ53YvLt_wcc7G7BnWpYSjSTypJSaEY5fXGn96N0CRDpRpDPTMVdwhum0RPQsvFkf6nvu6XSwy8Z6bP9W9ckfRe6tRcg2zgna1ldV5yLrTSaHeyIKrFjXRRrfY0bWlcUfKxYR3L__YyPre3dJLEELvsTwNadtaoPCx9Cv5w-EF2fonF6OBtXEmbahyIodEGTAao8beiT0xv7uWfnkcxYVkcz9LvtBiE1uJiHw7zd-sfj0TahiKelJhCkVkSdHSYTCjcuhjDG9_BSPbScLO2z3v9BymOi875af9U7Xemr2Nai73DOd-lTM6QPdftqecJc-MhYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو دوست داشتی با این شخص دیدار داشته باشی؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/666158" target="_blank">📅 00:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666157">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or5Dv8cH9QZX8LfnocpWc3yH_wWVmSrcsPVN3uRyfDCcldMLKr8HZ2nqExsRwHgj-BrPWLr0ggyNqf3ZpTkuPAk6epWaViE9_8_2Z_83wcxH7lL5b1bbclIfr1PiRkLReldKbH9R2o1xBqf4Yrj9Q7A_EkYXVudtmQKcw9Lmqq2SFHCJINcwuz2-YJY1bOvqvDJnRLt5_TtZI7Sm9nt_SwYQGftff6iEauyti8rQ5lhjq09nmKQz5XdsoNUBYlLloUwLnWQnkwEdc49Gu3-pJtaaiqCGu9kbHEC1nd5qfV6JkcQiqUbXrU3Gj-jwUihldBgJTewY6bq_xJNjTUO2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مصری‌ها در ضربات پنالتی صعود کردند/ آخرین نماینده آسیا هم حذف شد
استرالیا ۱(۲)
مصر۱ (۴)
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/666157" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666155">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290eeb6909.mp4?token=a2Ui4qt-Sloz9Mx-c_BhD6D-zWFoNRMMfi91ZvfTyoVGWxpSwE-uG_zhFaLlHarREox9gadIP1Iqij1Az465AfWSdd_nkO9y2Y3YYAWYU9eBnGz2HW2XvaD9pDCgUxMa8tahC9QSDCw3plUSyM70tUO6YkqQ8NMap6HrG_KCSCy02Lu6xvJlERezC4uK9PgWCkBcPhau7Vi2633HchZY5sS7eGNoZSr_Dsxxwz_LhKU9g-mYSL1eeAtukwCbzJct2D_C38lgCHg0T0D3eM5P4tL3lsq0FVXSlSaAI_fM4USx3qPyUCKqxOHqCJi2JHu2c_vk4DnoPDN_0JZpFIF-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290eeb6909.mp4?token=a2Ui4qt-Sloz9Mx-c_BhD6D-zWFoNRMMfi91ZvfTyoVGWxpSwE-uG_zhFaLlHarREox9gadIP1Iqij1Az465AfWSdd_nkO9y2Y3YYAWYU9eBnGz2HW2XvaD9pDCgUxMa8tahC9QSDCw3plUSyM70tUO6YkqQ8NMap6HrG_KCSCy02Lu6xvJlERezC4uK9PgWCkBcPhau7Vi2633HchZY5sS7eGNoZSr_Dsxxwz_LhKU9g-mYSL1eeAtukwCbzJct2D_C38lgCHg0T0D3eM5P4tL3lsq0FVXSlSaAI_fM4USx3qPyUCKqxOHqCJi2JHu2c_vk4DnoPDN_0JZpFIF-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه اتو زدن پیراهن مردانه را یاد بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/666155" target="_blank">📅 00:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666154">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7490dc516f.mp4?token=MIYVTrELfkNtBQ0KAIOgvJsREbyxuQSygwCDd82_25SGD6NLrF6rs7RmzQNoIjDhYdEInJgw0Q3h7UijI1rDfOLOr91t_MeyKSm0Va5SXAvkWJFmmT7lWGsOF5QYrxoP14yERB99pEcAuoJq4beg_7GjYjHC-byuUOO720WZVpEP099wWYA13RaxqvxQ4t0n_zvguELcbCzecB_Wicesk_jDDGjuUFnfz2vPmFgqg6aUiqgwPeOBF_-mmS35J62B2iwf3TRaf7tHgYg0ZlwlcxZcsfQa-fyOZC-8ZxV6MO-aKMmwdkAzLrIqzSvLvjyXBbuHWYtWdFSam160h1_2X4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7490dc516f.mp4?token=MIYVTrELfkNtBQ0KAIOgvJsREbyxuQSygwCDd82_25SGD6NLrF6rs7RmzQNoIjDhYdEInJgw0Q3h7UijI1rDfOLOr91t_MeyKSm0Va5SXAvkWJFmmT7lWGsOF5QYrxoP14yERB99pEcAuoJq4beg_7GjYjHC-byuUOO720WZVpEP099wWYA13RaxqvxQ4t0n_zvguELcbCzecB_Wicesk_jDDGjuUFnfz2vPmFgqg6aUiqgwPeOBF_-mmS35J62B2iwf3TRaf7tHgYg0ZlwlcxZcsfQa-fyOZC-8ZxV6MO-aKMmwdkAzLrIqzSvLvjyXBbuHWYtWdFSam160h1_2X4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار CNN که مجدداً به تهران آمده است، از جزئیات مراسم تشییع رهبر ایران می‌گوید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/666154" target="_blank">📅 00:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666153">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22aadd1e25.mp4?token=Q-XxJHkqXb0ntD3VZGk0gW_C_ZLksB509bAvzhl1UJz_MOIhYNu8wXRnLWro4_QPxiBqOMWaL42FB2-PTrnJFLRLqVTFFAkooN9UriLl_TWbZApPleeqW_LGwoMibvs0oIntZoRH6ZnPTLtnoxu1IiWGx2TLBtGJHqDYKnob612napdG-D5dw54a7TBlJoryUx6cqeChWveXKYi8o0g-sFTUgadHoYi4mLH9ZbbbtAh9iNsSdZmBWJ9hjToq9tgenkgWajnd0n6El9UCH4PiY7VGc0Ge7phADKc_5ct1qKguiHf5-zInFVIPxpUpN6MeNWHSQfG7JG0AMlmmr08EhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22aadd1e25.mp4?token=Q-XxJHkqXb0ntD3VZGk0gW_C_ZLksB509bAvzhl1UJz_MOIhYNu8wXRnLWro4_QPxiBqOMWaL42FB2-PTrnJFLRLqVTFFAkooN9UriLl_TWbZApPleeqW_LGwoMibvs0oIntZoRH6ZnPTLtnoxu1IiWGx2TLBtGJHqDYKnob612napdG-D5dw54a7TBlJoryUx6cqeChWveXKYi8o0g-sFTUgadHoYi4mLH9ZbbbtAh9iNsSdZmBWJ9hjToq9tgenkgWajnd0n6El9UCH4PiY7VGc0Ge7phADKc_5ct1qKguiHf5-zInFVIPxpUpN6MeNWHSQfG7JG0AMlmmr08EhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی محل استقرار پیکر رهبر شهید برای مراسم وداع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/666153" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666152">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpAQDV8iIlxzqrgp--5m8KONF-PZuYq9KyX8WXuPxyygJTKdEqFuFsxZnGR7YTcOAcm83g1JawRlTUHKVXvLZhN4aiqpw-tgvrrytAGOdAJhFIw4p1irDouv67BYobROFpkynuwcq-4maVnl5N4vy3uwgNOCorHfO5oXbFmFXEO9s2ZJwOsNWLpBq5YK_PzAhxP02a2gB68yynaWQ3IoJ9cHoB7RKHm24GLAgE2uY6LbUrN2tJq3VKEJbx_pHPUIFy0II9pYJel2HfpA-gE1mWgVkZKYa4IyUQzrcdSa5qaefoO3BovuBxsEipFrmpIP-9nL7oCdXgkGapX6hYxo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد هانی در تاریخ جام جهانی رکورددار یک آمار تلخ شد
🔹
محمد هانی یک رکورد منفی تاریخی ثبت کرد؛ او پس از ایوان ووتسوف، مدافع بلغارستان در جام جهانی ۱۹۶۶، تنها بازیکن تاریخ جام جهانی است که در یک دوره از مسابقات دو گل به خودی به ثبت رسانده است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/666152" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666151">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار گیلان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5baacd183.mp4?token=X8h8yacHSVdxaiHPtV7kF9dBmeK1nUPfvKuo_jBSSx-T5PiLZocXDb8IBZru2HozGvqGx2iDU1lwdkJS46xD_TlNRifgG909Za5NbPqPFXZseRRjWzo40RchLj_5ji2jNLZsYUrMTWjEFMItSi4Iyx8cCqkFfhxNYCnA7iJWHYtFp-yqK4kOLK-uTrwsbIcP33ocFXISovjU_9dkT2xITG6YN6Rvu961Q1Clc-r8wklYllxRHHkeAGqwt6_ESp6AoJkBVU7Z9xjCcxdmP67HJ3fIwujIxspGgdSxW8qnkZsUqrPEaieBX7-sp5GSP2nxnaGz33yq_uNCbkdGuRXf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5baacd183.mp4?token=X8h8yacHSVdxaiHPtV7kF9dBmeK1nUPfvKuo_jBSSx-T5PiLZocXDb8IBZru2HozGvqGx2iDU1lwdkJS46xD_TlNRifgG909Za5NbPqPFXZseRRjWzo40RchLj_5ji2jNLZsYUrMTWjEFMItSi4Iyx8cCqkFfhxNYCnA7iJWHYtFp-yqK4kOLK-uTrwsbIcP33ocFXISovjU_9dkT2xITG6YN6Rvu961Q1Clc-r8wklYllxRHHkeAGqwt6_ESp6AoJkBVU7Z9xjCcxdmP67HJ3fIwujIxspGgdSxW8qnkZsUqrPEaieBX7-sp5GSP2nxnaGz33yq_uNCbkdGuRXf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش جالب رهبر انقلاب به ایستادن مردم در زیر باران در هنگام سخنرانی ایشان
@akhbaregilan</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/666151" target="_blank">📅 00:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2uE6nKR_5d7NPdPI4adzh7wdkQ2RQpyCGBlzbSlQb2_1tft7VdMWos8meOAlDkFdq1MQrUIAqdWNRb871STSoC8sw4PVhk6BE-nL-jA0oDzRupceNFQuT_bAVeE73PcW0A-oP6WjE2pU99D6FoJGOTXoGHB8cL5OhS4rPiMRtWz6KlpogkPMRUJdkrec8Y6QpaptiMVdllbd0PFMXxIFWMklnAZfz82wRIauMIKas4Ugh4shkK0sUafM8Qg_PtsybOmcOPTVMDB3dq-mboZNeE9tdOOWY3zRZsGJm9ImMvXZhXe65Ur2XrHOujaohoKv5vOmXutRsUvvwZxx2tIOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرخی این مچ‌بند، یادآور خون شهیدان است
🔹
با مچ‌بند سرخ در مراسم تشییع حاضر شویم.
🔹
تا عهد خود را با راه شهیدان تجدید کنیم. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/666150" target="_blank">📅 00:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666149">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDX99QrriDJxfMjkeCRq06vYk1JHdTo_jltSj4rHUSkL2zrgsxN9ffDe4OBdaKgFb5W9-0AwP1-KE_e-dyB-mghK2DuTHC1eiPVGMLH6-3y9ECC2ebnWDCSvXuLGM0Pg-1zXRNgC6SK17g5N0onHPI3ZW_zmEFbtZBivxWMwG0fLn_hCpfoCzOOUr_L8duj62STFx4FFdB6OIx9QKScjsR4R187wcLIHKxQUypnZDin99u_jAxcO9L8HE2ZqdxT61usSmmn6B5F4u97F7mi5I12svoDjXAAJ6qsm24-pi7FSjklcHRpPDaqQNZPBiQtF0JqDWXUE2sPEtLqWU2VPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/666149" target="_blank">📅 00:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666148">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L677KhVfKJ4cyUOCskcyEy17UDu2-xz0YmYYtm_uuz3cP9Bs5K9Zl_GWx-HOUj-XlalRF1FQCSZz4yHal_ExXSjYKVLG7PTOGMnJTilKfxNvOrlylkKGmHV-k1lcOZ8oyQwmCvB7csvweHYCO-5NWqgGXnv1Uqwv5dkFlULYRadLjdXBWHLEKthK8QDhle4n49OWFwygp_h2xE4yZ2goz0tF9NvimkCLLnVBhZE-uUti8KS4TFABqfLoo2JCpqzg6iSXohqBCcUFQ55ajD5W-V2RagpaqLZ2VpiX7iyIM3Ds0U46mzSfYFF8PpPDxLz5TPgYlfHxNPuOYATBA7f3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا به کانال ۱۸ میلیون تومان نزدیک شد.
📊
بازار طلا برای دومین روز متوالی روندی صعودی را در پیش گرفت و به آستانه کانال ۱۸ میلیون تومان نزدیک شد.
مشاهده قیمت طلای معاملاتی در میلی</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/666148" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
امروز در مراسم وداع با پیکر رهبر شهید انقلاب چه گذشت؟ + ویدئوی کامل همه هیات‌های خارجی
👇
khabarfoori.com/fa/tiny/news-3227494
🔹
ترامپ از حمله تازه به ایران خبرداد: رادار جدیدشان را دیشب نابود کردیم!
👇
khabarfoori.com/fa/tiny/news-3227444
🔹
جزئیات اتهام‌های متعدد جنسی علیه کاپیتان سابق تیم والیبال ایران!
👇
khabarfoori.com/fa/tiny/news-3227506
🔹
مدل جدید تذکر حجاب در تهران + عکس
👇
khabarfoori.com/fa/tiny/news-3227466
🔹
مجری مشهور صداوسیما تغییر جنسیت داد
👇
khabarfoori.com/fa/tiny/news-3227473
🔹
ویدئوهای جنجالی را در آپارات خبرفوری ببینید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/666147" target="_blank">📅 23:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bc6f80d9.mp4?token=YS9PpWERBOgB_PkLWK2GEMmSZMxCarW9W6l8O898spFHmVqayAIZDKLsnrn6UH4pgd3cVoFUiYd2GP4NyIovuX3xR_l8Gw4TVS4je1Wy9XtUspn_zHctwKw8yMK-Lg09pvfBDrAeABEMeCQcgihEr4FpPAAuBYh5Zq-YeSl3XhKVOjy22i3Z69glCPiuZkA9SatROWm7Q7wlcBXuwSB8VoQNaXXbUAKZPKcanL_7AHCLmbyhRMmIh3XmO79c1GbHwH0z8NfNY2HWhPMNpYMHVKvGMIv6dOllPVaI2721zGx3uFhUwcjGDTMxFpBA1M1D4lcOuGalqxEaiO91cnjcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bc6f80d9.mp4?token=YS9PpWERBOgB_PkLWK2GEMmSZMxCarW9W6l8O898spFHmVqayAIZDKLsnrn6UH4pgd3cVoFUiYd2GP4NyIovuX3xR_l8Gw4TVS4je1Wy9XtUspn_zHctwKw8yMK-Lg09pvfBDrAeABEMeCQcgihEr4FpPAAuBYh5Zq-YeSl3XhKVOjy22i3Z69glCPiuZkA9SatROWm7Q7wlcBXuwSB8VoQNaXXbUAKZPKcanL_7AHCLmbyhRMmIh3XmO79c1GbHwH0z8NfNY2HWhPMNpYMHVKvGMIv6dOllPVaI2721zGx3uFhUwcjGDTMxFpBA1M1D4lcOuGalqxEaiO91cnjcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامه به رهبر شهید
🔹
شرکت ملی پست ایران و شورای اطلاع‌رسانی دولت در اقدامی مشترک و همزمان با با برگزاری مراسم وداع و تشییع پیکر مطهر رهبرشهید انقلاب اقدام به برگزاری پویش مردمی «نامه به رهبر شهید» کرده‌اند.
🔹
در همین راستا عموم مردم می‌توانند نامه‌های خود به رهبر شهید انقلاب را تا تاریخ ۲۵ تیرماه ۱۴۰۵ با مراجعه به دفاتر پستی سراسر کشور به صندوق پستی۸۸۱۱-۱۵۸۷۵ ارسال کنند.
#باید_برخاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/666146" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بازتاب وداع با رهبر شهید انقلاب در رسانه‌های مطرح دنیا
🔹
مهم‌ترین رسانه‌های جهانی هر کدام با نگاه خاص خود به پوشش مراسم وداع با رهبر شهید انقلاب پرداختند.
رویترز:
🔹
شهادت آیت‌الله خامنه‌ای در پی یک حمله دشمن «با سنت قدرتمند شیعی شهادت و سوگواری همخوانی دارد؛ سنتی که در آن گروه‌های عزادار با زدن بر سینه و زنجیر زدن به سوگ می‌نشینند.»
گاردین:
🔹
مراسم وداع با رهبر شهید ایران به‌گونه‌ای طراحی شده است که نمایشی باشکوه از سوگ ملی، اقتدار، روحیه مقاومت و همبستگی اجتماعی در ایران باشد.
فرانس ۲۴:
🔹
ایران در حالی که برای تشییع رهبر شهید خود آماده می‌شود، به آمریکا و رژیم اسرائیل در مورد هرگونه حمله هشدار داده است.
ایندین اکسپرس:
🔹
مقامات جمهوری اسلامی این مراسم را نماد وحدت ملی، تداوم راه انقلاب اسلامی و تجدید بیعت با آرمان‌های متعالی انقلاب اسلامی می‌دانند.
شینهوا:
🔹
مقامات و نمایندگانی از بیش از ۱۰۰ کشور در مراسم تشییع شرکت کردند؛ از جمله سران کشورها، روسای مجالس، وزرای خارجه و شخصیت‌های سیاسی از نقاط مختلف جهان.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/666145" target="_blank">📅 23:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpTpdv0AekE8OGs_o4xnhWPC2UZaykwyIQHMPblaaPvZZEDsZdIvRPjN9_MGg-rQMtO8awTsoFYIFVRSGo5EPonQv5j7tVHYUpNVb6zzrcGx5-b3ySH7a4dgCC-tnV1aLYWdNzozqqidaeOS0r1yz_aNWQpMYQ8RWEVN5JbWgEnZDOIg8lw1PIOoLeqy7IZRrN4O9TGPftHWhHaJtMwwbVMJ3JNEnCLKI5-DPPk40FQqdJwd2F7NfWCuoGnZpjoaaooAoq8-Tmdxs39zOyv9Mt70F72jSOo5jtZxhD2d7ccilWhnhLOo30zYXTsSlKQUioS0ppGN4OKICYPsxzZ-Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویرسازی حشد شعبی برای مراسم تشییع قائد شهید امت اسلام: حضور پیدا خواهیم کرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/666144" target="_blank">📅 23:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تفسیر جالب رسانه غربی از مراسم تشییع رهبر شهید انقلاب
میدل‌ایست‌مانیتور:
🔹
آنچه این تشییع را واقعاً بدیع می‌کند، تبدیل اندوه به ارز ژئوپلیتیکی است. حملات غرب برای «بریدن سر» طراحی شده‌اند؛ تشییع نشان می‌دهد که بدن اجتماعی می‌تواند سر خود را به شکل نمادین بازتولید کند.
🔹
جمعیت خود به سلاح تبدیل می‌شود. پانزده تا بیست میلیون بدن که در صفوف راهپیمایی می‌کنند، بیانی زنده را شکل می‌دهند که اراده خاموش نشده است.
🔹
این رویداد تنها یک آیین مذهبی نیست؛ بلکه یک مانیفست ژئوپلیتیکی و یک همه‌پرسی متافیزیکی درباره خود امپریالیسم است./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/666142" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYaPmtypZJssl-y9N-X2DVlruXlgyL8sbht_dMAtbgtMNMQNJXEFGhkpknAw5yv6WE3PIvapVqg9D2Gc2yOcD9pU4ZOM6p5nqPW4PQAPqxurgPkbpWD6j_0ARSAwtjbbaIuc2PTX0w_oEe9OU0UiLypk350TrVwe3T1nOrGiJXV2iwyZAIS4G9Cnx9vNFqbnK7YGuXKTN5qzx0oDppwOXBfLxE80RpJhPV4CBKFUCHKfmcaOe_Uc29TiRAR8Y1a_ZmC3yVWRf5ZGQb8dVIvQHodZqGFeGr9Q-gkszZLPAPpaDqqO0OiOSXlIWyCIxPB-s3pYdZ8B25YqWewem9S1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
اشک‌های سران قوه و مشاور نظامی فرمانده کل قوا در لحظه وداع با رهبر انقلاب
🔹
‏این غم مقدس است این اشک‌ها خوب است اما مطالبه مردم این است که این اشک و این غم به خشم علیه استکبار جنایتکار بدل شده و عزم شما را برای خونخواهی رهبر شهید راسخ‌ و قطعی کند.
#خونخواهی
‏⁧
#هزینه_خواهید_داد
⁩
‏⁦
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/666141" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/666140" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/666140" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/666139" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/666139" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXrzpLJD92uZPh47nvzeJyPONofqpnG8PL1bpQe4R5k_SIC2NCYxE8hDLavZmO6uxEcqRe9Jx8jj0vmS--lApIziXH43S-XYfUci0Vxe2LspGhujBAyc3qmwdnUu2BAEnXhaN2XujagXh0IJCcDA46jE2E1YwC_0SjQ58J6NguckFTXTgmI5YlnZu978yjL0Lfg5CvCq3Jm7QJABTQiV8Ocpn6uPdh6vBfXIlq5bn1v6RlYgOCaO7yCONuDspugjsaHP0eoZcCNG76B8ZS8iWRmeGNAOcQh8zeVGAlQIwnKbkUz-2Q22sppjnNMOrLITYrZOwBGc89N8QRxgukkewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مچ‌بند سرخ در آستانه مراسم تشییع
🔹
مچ‌بندی به رنگ خون؛ نمادی از وفاداری، حق‌طلبی و مطالبه خون شهیدان.
🔹
اگر شما هم در مراسم حضور دارید، تصویری از مچ‌بند سرخ خود را برای خبرفوری ارسال کنید. #مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/666138" target="_blank">📅 23:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استان واسط عراق و ذی‌قار هم به مناسبت مراسم تشییع قائد شهید امت تعطیل شد.
🔹
رئیس اقلیم کردستان عراق: جمهوری اسلامی ایران با پشتیبانی مردم وارد مرحله جدیدی شده است.
🔹
مکرون: ناو هواپیمابر شارل دوگل در پی تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/666137" target="_blank">📅 23:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW3MyPK7RkDGtA1y9LIAtsoEtSFullvhB5cQ8A-R_lbQwmBr2EPg2-tytmsGHEGHe1kzDva-EIlmcNEuI15FFWpZxv3GDdyCIMWGIytLhCtlwnRdrdAXpyP0poeflAEHkJEwV2O6MVE5ympXohmL-odLl-fyHPc2GBSKO-Mg2mLQLVWNA5Hy4c_iWFdNd8fTcsa8E5Ma1QFveOCEQeFzE7CyI62kr_1vSOXE1zyJ-zrUjtf2Me-x3hg_HvMQX3Ubu8hUaPDdRo3-0vr-1rRn4OicEcETaEzs7yVF04a4QI4cEYq8x7pnuxE5jI1rj4hnPf9CtI7PS28h2kmDMo9hLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شعار نوشته‌شده روی موشک عماد با سرجنگی شدیدالانفجار
🔹
رزمندگان هوافضای سپاه در آماده‌باش کامل عملیاتی حس حضور در مراسم بدرقه رهبر شهید را به شهرهای موشکی آوردند و شعار
باید برخاست
را بر روی موشک‌های آماده روی لانچر نوشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/666136" target="_blank">📅 23:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
عطارزاده: مردم بصره و شیعیان پاکستان خواهان میزبانی از پیکر مطهر رهبر شهید شدند
سخنگوی ستاد بدرقه «آقای شهید ایران»:
🔹
دولت عراق برای برگزاری مراسم در عتبات عالیات ستادی به ریاست نخست‌وزیر تشکیل داده است.
🔹
مردم جنوب عراق، به‌ویژه بصره، و شیعیان پاکستان خواهان تشییع پیکر در کشورهای خود بودند، اما به دلیل محدودیت زمانی این درخواست‌ها عملی نشد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/666134" target="_blank">📅 23:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666133">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCWwWdxidYeS1nX66qm1shpkhdAzL4fs-Spctl94K0XVclqa1xfUR1-4vs_5-cJssAIc-nFGB0hDEw42cqIu59NLmgnuEcO_2absFLvjsKBjllufpDVyBvFIsvks2fTrmtiC3mO57DFkFHd7wVgJd-kY0puWSXrqKLBZJoE_RnpG--r7CG5AwfLVRe3p0KTGddtMCJy-8zRaD53BmOrg55LmwNV7wkImdk2WGTPoevuITly5HqMO1-ciK4bhXVCU2hQt68IFFxboFJg2I1M3fjWFbLR_xLlTA2oBifGiD4dofnaz32Us14X2FT3JaonPnHhx_GsowQKomXjQX_67lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_نهم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید حسین آجیلی  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/666133" target="_blank">📅 23:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666132">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dee87ae4.mp4?token=bfmUI8BkK1xevMpoKOgk8lxfEQzivLmfGuX_Nbb7qT79GrCGNjN5GAsd2bEs2CDBIqNkXVtJeS9i8leE26duvSzP1oDY36c8UpVkpJqCng_RLLKjknws0XSiDL9Dalop1Lby1oAn12CzA_iItCm-3vGA_TscGLdG7hq9cEzqq3YR58Bd15xJaBD5zEdIfNvP2jGohVDu-7BQ-rziit4CSUnuOmhgBDnbQVK7_D5WOpfTRZpelZQre_dmOpVs2xpqOUjbGMgKGoo78yh2eNGDg5IbaspEM07Z4EgcBYc_CwePz-Zfz1AixSSJsAWUoY1-aNfjYDgoMy-cY-iswxmRNGZw3yTZUt6Qg415MQgMN3SseEdOlY6N5R7BgOzdniaESS3yb0iVtT5AayudVyYjy7XpSH5IEVSuYtnnBc2dDNndKL5Fi2T-JvKjOFU9S0ahRH_ZYlqyBbS_eX5nT44NplgXa2_Wrh3E3UZ--YIGlF0RXxM4o9QIzN-52KJHlyHfgdtlnSTvhQxPlgN7HboB99-DIpgmyqq9VwBnOpj8VSvTLFMID6OpF4Q1xUi5iJicTWjqhb8a5UUDd2DfOEQ4JULyourQ1ruJxAIZawwmD4ALzwe6w_eTQ2tQ_p6RDfFk5A-PwitMlQoyb1L1JyDsC2fg88jq9R0D4PhMT8qmeJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dee87ae4.mp4?token=bfmUI8BkK1xevMpoKOgk8lxfEQzivLmfGuX_Nbb7qT79GrCGNjN5GAsd2bEs2CDBIqNkXVtJeS9i8leE26duvSzP1oDY36c8UpVkpJqCng_RLLKjknws0XSiDL9Dalop1Lby1oAn12CzA_iItCm-3vGA_TscGLdG7hq9cEzqq3YR58Bd15xJaBD5zEdIfNvP2jGohVDu-7BQ-rziit4CSUnuOmhgBDnbQVK7_D5WOpfTRZpelZQre_dmOpVs2xpqOUjbGMgKGoo78yh2eNGDg5IbaspEM07Z4EgcBYc_CwePz-Zfz1AixSSJsAWUoY1-aNfjYDgoMy-cY-iswxmRNGZw3yTZUt6Qg415MQgMN3SseEdOlY6N5R7BgOzdniaESS3yb0iVtT5AayudVyYjy7XpSH5IEVSuYtnnBc2dDNndKL5Fi2T-JvKjOFU9S0ahRH_ZYlqyBbS_eX5nT44NplgXa2_Wrh3E3UZ--YIGlF0RXxM4o9QIzN-52KJHlyHfgdtlnSTvhQxPlgN7HboB99-DIpgmyqq9VwBnOpj8VSvTLFMID6OpF4Q1xUi5iJicTWjqhb8a5UUDd2DfOEQ4JULyourQ1ruJxAIZawwmD4ALzwe6w_eTQ2tQ_p6RDfFk5A-PwitMlQoyb1L1JyDsC2fg88jq9R0D4PhMT8qmeJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از روایت مردمی که ساعت‌ها در انتظار ایستاده‌اند؛ از سال‌ها همراهی، احساس دلتنگی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/666132" target="_blank">📅 23:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666131">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8xf3YgFe6HihVg3eBim0pkQVh8ivdb3kcWAzmjABO7tZMx0jEzuYRdzl-Nd6FXmAKlBMUVTQajbOhvNQp2dQs7CLOyzsaz_h0-ZjpGn5SyAve9SvQS8EF21JjQTwPFvyT2tvPEWG69AtXO_SqT_bA6UkMwPidXwW9lK89pj-Wh1s1FetP4Jclarq0pn3kc_cF7iistWq1bT1CE9-0mOyBwm08sR4Jr4O7Kl2mHJOu8qt6kP_Yx4dsFpvr0v1fDfTYKWiOaBRMwmuB1JtdFUcjeitix-63BOHvMyGohDJFMWHEFQd8g_8VsrA7nTLJrJrhrL2pWXbnUHx-qPouHuJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱.۸ میلیارد سال تا پایان حیات؛ زمین بیشتر از آنچه فکر می‌کردیم زنده می‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/666131" target="_blank">📅 23:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666130">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ نامه ای از آقا</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/666130" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
سلام عزیزای دل من
دل منم تنگه براتون
برای اون حماسه هاتون
توی خیابونای این شهر
منم میام هر شب باهاتون
🎙
#مهدی_رسولی
#رهبر_شهید
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/666130" target="_blank">📅 23:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666129">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استاندار تهران: مدارس، مساجد و ادارات مسیر بدرقه، برای خدمت‌رسانی به مردم باز خواهند بود.
🔹
تعطیلی رسمی در بغداد به مناسبت مراسم تشییع رهبر شهید ایران
🔹
ادعای فایننشال تایمز: تردد کشتی‌ها از تنگه هرمز در هفته گذشته بیش از چهار برابر افزایش یافت.
🔹
سازمان جهانی بهداشت پایان شیوع هانتاویروس را اعلام کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/666129" target="_blank">📅 22:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666128">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10891a982.mp4?token=WGLQdYujWgkpcvV-3jn3Z4xh8Ijtc17ZA7iEbGbp2hrum2Sq7jhm2noLSKUP7if7SEDoKlrDwmLFqihKzID864xJ17EKScHZVyPu-F7GRVFdARQZddm-zNqk6EwB9n6aH5w9sDZ7OETh49ajJakwAtmLvpfBfuWHuaSu5BJMfczfNiSsd2DFdhFBA8zAzdhdrWt1DdHWSgUZRiN5h64T5h4jBl7_7ubakw9Re9VLPNWO61grp26EUJjVU7ojtqdxQVvNzRrNnnBw4yh4xL6pgs4Ewh0jI3JMCDiBvp6o99uYL3IZWxIXNQetp8_1M_ZdbyzlR5-XQTZ1NGcdx3C--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10891a982.mp4?token=WGLQdYujWgkpcvV-3jn3Z4xh8Ijtc17ZA7iEbGbp2hrum2Sq7jhm2noLSKUP7if7SEDoKlrDwmLFqihKzID864xJ17EKScHZVyPu-F7GRVFdARQZddm-zNqk6EwB9n6aH5w9sDZ7OETh49ajJakwAtmLvpfBfuWHuaSu5BJMfczfNiSsd2DFdhFBA8zAzdhdrWt1DdHWSgUZRiN5h64T5h4jBl7_7ubakw9Re9VLPNWO61grp26EUJjVU7ojtqdxQVvNzRrNnnBw4yh4xL6pgs4Ewh0jI3JMCDiBvp6o99uYL3IZWxIXNQetp8_1M_ZdbyzlR5-XQTZ1NGcdx3C--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت نهم مستند احیاء و حقیقت | باران مذاب
🔹
وقتی یک سایت فولادسازی هدف بمباران قرار می‌گیرد، انفجار تازه آغاز ماجراست...
🔹
در میان کوره‌ها، خطوط تولید و تجهیزات عظیم، هر بمب می‌تواند زنجیره‌ای از بحران‌ها را رقم بزند.
🔹
بارش مواد مذاب با دمایی سوزان... نشت…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/666128" target="_blank">📅 22:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666127">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVmfF_Py2y2MI4nDdHrYMJzVm8qtRsSMLslmTSb-2aI1nJ-JZsr7UDY23j1gAPpFKESOCL7MfSC2rGNJCmWWZ2h3Bf-sbrQZB_sS6D3NNqidc2owoi2Gk-7UG3-M4A8Z-4uMV4AsD9vbfuw1pVKoKOJRNppi6COYQ0HzOnS8nFCkMWQx2hZ0OYM6PyP4quP57KYm52LfswUDwyoJyEkDeycJatA-W19gE5xB2sbo1jBaXo1JsrPRMpeTFWRsx6aaMDzR1Yormpbu46hQbBKTEpFSqi3P4uQ6_p9lUN43TGT6fPNUT5QvS0e_VV7RLQy-3Uqzn78Ob8fCY-q3SNlb1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرمربی کره جنوبی استعفا کرد و پنهانی از کشور خارج شد!
🔹
سرمربی تیم ملی کره جنوبی، پس از حذف تیمش در مرحله گروهی جام جهانی ۲۰۲۶ (با ۳ امتیاز) استعفا کرد و به دلیل موج گسترده تهدید و انتقادها، مجبور شد کشور را ترک کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/666127" target="_blank">📅 22:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666126">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VW_GlUQbo0uxe_uZQXFev0cBVHSXvtqiP1ycGAFYwVsu5YWBBh3UNv5bcNiaJysyjJjUtD3F8Anhgetu12rqz9HCfOrhdBANa4IxVqeNu3lKlzu0_FPGiLblMcMTMULewSjt3MLdbTOhX36LjZ9E0HqDbPb7coNb_v7L6WaeYCUIJju-tIasgYXkGwk6pn0vMB40J-lJnxfzd51rPETC92upwJH-4_amX6a_5isoJFxkrzRYNd3-II1UwW6b1iC9NJxLZvb_bVcQFZcSjGD5Rikt_4a14aYtqpOpsvX_mb69e5EyaCtpBGnqC_YlQERGLa0FH1rP8ZzgZI2BUMKzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مچ‌بند سرخ در آستانه مراسم تشییع
🔹
مچ‌بندی به رنگ خون؛ نمادی از وفاداری، حق‌طلبی و مطالبه خون شهیدان.
🔹
اگر شما هم در مراسم حضور دارید، تصویری از مچ‌بند سرخ خود را برای خبرفوری ارسال کنید.
#مچ‌بند_سرخ
🔹
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/666126" target="_blank">📅 22:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666125">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=JTzu4vS9jRGSHMaLD0-DvQUHNYxuzwmGCSQqVjd3b7BttrYc9yGZ5sS5IgNIQS_4KRfyPnFzPn8Do9yaVgy0pc3lMvbQpxhB_TSf1UxH-Ee7cBVBn-P87ybZBkeId24VZQCgDwiBq4cGCC6hQHhJcqEJqLJBJBUQWzbuEo4FvS6JdSf2dJrdiCg8HmkPit_9ZK3BpwcSK3WHVxbJoH5njcKE6WyzZveBJp7528S93n66miUg1vX5E3BFKcrh5AFXm4l6iSLK_C88jdJo9VBsbiV4vlm_M5qy6GvNBPQ3ARKYD-x0eStea_XHSoYahyhT6KbvWeCPqQyXkdcwvnUJ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=JTzu4vS9jRGSHMaLD0-DvQUHNYxuzwmGCSQqVjd3b7BttrYc9yGZ5sS5IgNIQS_4KRfyPnFzPn8Do9yaVgy0pc3lMvbQpxhB_TSf1UxH-Ee7cBVBn-P87ybZBkeId24VZQCgDwiBq4cGCC6hQHhJcqEJqLJBJBUQWzbuEo4FvS6JdSf2dJrdiCg8HmkPit_9ZK3BpwcSK3WHVxbJoH5njcKE6WyzZveBJp7528S93n66miUg1vX5E3BFKcrh5AFXm4l6iSLK_C88jdJo9VBsbiV4vlm_M5qy6GvNBPQ3ARKYD-x0eStea_XHSoYahyhT6KbvWeCPqQyXkdcwvnUJ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر دیده‌نشده از حضور رهبر شهید در حرم امام رضا(ع) در سال ۱۳۷۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/666125" target="_blank">📅 22:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666124">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070fa33f86.mp4?token=XJNyZlfij8gD-64ZFRbkHgq3dzGjuZPyXH9saRD_dShc8AyVJX0cGZ5jkEWZeqn52GIq3vokuc3Iz9ykam8n-pyyTSjJbICwkc_SFaAqjSpxQSETSdYrejpww9brpRvzNtumvoBxNics7ku98Q0qAhPTfLIJTXeu6PkVMhwMEj3KSnHCd7-RsleVUmO7mbD-vdX3zEFC4YTpUaG2xacsdJIjlOMGjjfp51AfrYDQzanAjidzYYpWVHpFyfB6mdipCJroCqNOXBjZDfewOqUfWQsvDc47TvMqnB3uFB0YIDGWfGTPl72-3TQYwkEGmOlhuvjBNHJhEnbd0elWfp3CJQiPvcFC-QYy5fTzF1X2Z1dCQzy6zPxjCKi-X53wcG-1-3yxbykSUskziMw8AKSRo3aYMDn5dahstrXffN-cGNJmQ-i56kA54bNsjOTzDdaiO-dkVnKspgcVNAR9Lg2OueS78lF_HHidPGUy6_YE9lPvqucMOYEHdj3dm_VDUQ4SpWGEiYu8EL5LSqj4Iq8SB4DEX8N0CahArw63ukhNafQUpfrrRqde77woXL8fA5-Wlmk67MdxShSsInuyyw9Kuzo0ZUpPKXaf7g2a5z9oFK3SvvaP-cL9uOalxDWkTzj4edweW-GwDKxtjuzDLA65HKWBs6gs56XzrGMfBs8Ku-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070fa33f86.mp4?token=XJNyZlfij8gD-64ZFRbkHgq3dzGjuZPyXH9saRD_dShc8AyVJX0cGZ5jkEWZeqn52GIq3vokuc3Iz9ykam8n-pyyTSjJbICwkc_SFaAqjSpxQSETSdYrejpww9brpRvzNtumvoBxNics7ku98Q0qAhPTfLIJTXeu6PkVMhwMEj3KSnHCd7-RsleVUmO7mbD-vdX3zEFC4YTpUaG2xacsdJIjlOMGjjfp51AfrYDQzanAjidzYYpWVHpFyfB6mdipCJroCqNOXBjZDfewOqUfWQsvDc47TvMqnB3uFB0YIDGWfGTPl72-3TQYwkEGmOlhuvjBNHJhEnbd0elWfp3CJQiPvcFC-QYy5fTzF1X2Z1dCQzy6zPxjCKi-X53wcG-1-3yxbykSUskziMw8AKSRo3aYMDn5dahstrXffN-cGNJmQ-i56kA54bNsjOTzDdaiO-dkVnKspgcVNAR9Lg2OueS78lF_HHidPGUy6_YE9lPvqucMOYEHdj3dm_VDUQ4SpWGEiYu8EL5LSqj4Iq8SB4DEX8N0CahArw63ukhNafQUpfrrRqde77woXL8fA5-Wlmk67MdxShSsInuyyw9Kuzo0ZUpPKXaf7g2a5z9oFK3SvvaP-cL9uOalxDWkTzj4edweW-GwDKxtjuzDLA65HKWBs6gs56XzrGMfBs8Ku-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.  #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/666124" target="_blank">📅 22:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666123">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FRSII3I4L1aaAiRvbiX3_3Whdmxm6-YTZsekUXtDaLEa17gw70qqtpqaRkM6G8ExOj15rc258bMzKiAamdNVXbkCEkCIJxoceiVLyMEwBTD6HvtWFfMQrRd31pmpkAgmGKnBZeK6bOsSToGwS3VkZYYsMM2oCZ0XauwQRuBcUh1-Nx1b7WWw7YG0cQzCDTaY9ZcvmLjwOE_O4j16OWUda7vKWx5Ovu3RrZPGigqdkxeQnKkr5tA-azYaKsNcM8BD61DbpjxNSaubM0ykd8mIlpKZcgc91w8tRj6PpfSypfMgYkcr5VTL9uZ5VTuvdqgR_uFlTrU7LB4gDYhSRWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت امارات تأیید کرد که شرکت ECT Aviation Support عربستانی که توی اماراته، ۵ فروند بوئینگ به ماهان ایر ایران تحویل داده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/666123" target="_blank">📅 22:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666122">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u51fJ7hbgOhQ2g7ypBIUrdofePovVQl1jyFerrG9C0v9TqtJPaPdsYw81JpgDX5w0ZCs_1NlJFm5_3_i1Um6ae910hwjW3XgRO3yfadlD6E1Xw3v5MQjZdHMBXSuZqmbEFGzm0XkrpL-8No4BtSc_BXm6codkoPLRmT-C_fwMEB8llhzAXzFd_WQpyFBdbeyw6q0MDFCaMHXDNcDabse4c1lJsVjAvoYBF86snzn2cSMjRhiL-wVy_3-MjTGWub_tzfrHJBu4brkZOnufsqSGyyYWoIr3tS4dptyqyOwQwO1Z9WfaOw6ngvtuRkZ57qzBxoWLe90YnVnCJ-J6_9BiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۳)
🔹
به عنوان کاربر فضای مجازی در اکانت خود:
۱. ویدیو، عکس و متن از بدرقه رهبری را به جای استوری و نمایه، پست کنید.
۲. محتواهای جذاب این روزها را حمایت کنید
۳. برای پست‌هایتان کپشن انگلیسی و عربی بنویسید
۴. از هشتگ‌های معروف این روزها استفاده کنید
▪️
پ.ن: پیام بدرقه باید امید باشد چون او نماد ایستادگی، استقلال و شکوه آینده ایران بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/666122" target="_blank">📅 22:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666121">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aadf84bc2.mp4?token=STA_eM32h1yvuktHH2s5UWYmntgAMKotUE-1c-g9EQuphwuRZwWOJ-TAg6XFJ6lWpl_nUJ7RSIbi68cuxTmdQ0BWLihpJMBfkzetCre2I_fPM1VyOLZjEU1VwbQxxei9g0TQ9Xwos2yjaqtuEdHFXuF8o2avB3hGFjnahv8soSLP7KHnFveTWHwy2jWAoOUT2nrjOneG-hPlgV1c8b_rawXNO9LYkeWE_D-q0uu4T1GTgRrONpt96iTMbSzluNz1tfVTUODqEJVecZJCB335CDOQyqblnguiMs6VmBMYtXtIujhDJLpmxtjOim5BIWgzw0Nju0bYUZLEAyYia_OTGmssCJEMeqYRqeJT3t7q7Wmnf_avW1TqM0PmABum-F00DgaOT0TlV5_AFyKLyfDzl_JukxqJ-oIX7eR-QBhpfTS2GYMkgA2D3-3fU5_p3haxfHdPtLkHXO39JQTdR1nXv_XvV70xWUT-H5TLgt9ZtqfXXPus-4PWFC_hWjhm4DpPCCJ7WZ2SlVzd_PfcdWz362-W00dFjx4_OYifhYtFM-XrrFAaLVM2avqFAte20hY2lN2WNUMuHWJkrRsuDW1YwkXFQsbywS10vX8K8aBDPkjirMu9RzhJaRTQLGu70cUSczsbP9P679CmNMxOfhxOBwqm58UDvLXZ1e3P922XeEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aadf84bc2.mp4?token=STA_eM32h1yvuktHH2s5UWYmntgAMKotUE-1c-g9EQuphwuRZwWOJ-TAg6XFJ6lWpl_nUJ7RSIbi68cuxTmdQ0BWLihpJMBfkzetCre2I_fPM1VyOLZjEU1VwbQxxei9g0TQ9Xwos2yjaqtuEdHFXuF8o2avB3hGFjnahv8soSLP7KHnFveTWHwy2jWAoOUT2nrjOneG-hPlgV1c8b_rawXNO9LYkeWE_D-q0uu4T1GTgRrONpt96iTMbSzluNz1tfVTUODqEJVecZJCB335CDOQyqblnguiMs6VmBMYtXtIujhDJLpmxtjOim5BIWgzw0Nju0bYUZLEAyYia_OTGmssCJEMeqYRqeJT3t7q7Wmnf_avW1TqM0PmABum-F00DgaOT0TlV5_AFyKLyfDzl_JukxqJ-oIX7eR-QBhpfTS2GYMkgA2D3-3fU5_p3haxfHdPtLkHXO39JQTdR1nXv_XvV70xWUT-H5TLgt9ZtqfXXPus-4PWFC_hWjhm4DpPCCJ7WZ2SlVzd_PfcdWz362-W00dFjx4_OYifhYtFM-XrrFAaLVM2avqFAte20hY2lN2WNUMuHWJkrRsuDW1YwkXFQsbywS10vX8K8aBDPkjirMu9RzhJaRTQLGu70cUSczsbP9P679CmNMxOfhxOBwqm58UDvLXZ1e3P922XeEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای سوزناک ترومپت در مقابل مصلی/ شهروندی که نمی‌داند چرا ساز می‌زند اما مبعوث شده
🔹
روایت شهروند تهرانی که از روز اول جنگ پس از سال‌ها ساز زدن را مجدد شروع کرد و حالا مقابل مصلی منتظر شروع مراسم تشییع پیکر رهبر شهید انقلاب است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/666121" target="_blank">📅 22:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666120">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a99d98f1.mp4?token=dDzw7VLp5azFpyp76_7qwteL8qqX-XdnhUWCI_3QZ9Sa7PlIOHZhX23AY7zwXMpRF2T5nh5DOoXM0MUzrzPC3wfoBoiQIY-Te-xxmb3-tX-oh7-Js7ZD0xgybCZLwgrFozal6WF6eljDdKemSOJ4SXmLziN2zgzhhe4u2UGWWRjQpO6X0Zy9E-XumU-Rdu5kMEUZ49m-v7jg1ZIOB0nlqHg65PO5I6OxZN2AeXMcdiLxQWHfGWTlWlZHn5DKdJytBuaT0WbBklYWOs_HoK-sJTnRbGyk79wOw4XLoPhUsSl0zvgPGi0s-r8okJNKbIc5p1jt8KbwMQRJFgJkcX05PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a99d98f1.mp4?token=dDzw7VLp5azFpyp76_7qwteL8qqX-XdnhUWCI_3QZ9Sa7PlIOHZhX23AY7zwXMpRF2T5nh5DOoXM0MUzrzPC3wfoBoiQIY-Te-xxmb3-tX-oh7-Js7ZD0xgybCZLwgrFozal6WF6eljDdKemSOJ4SXmLziN2zgzhhe4u2UGWWRjQpO6X0Zy9E-XumU-Rdu5kMEUZ49m-v7jg1ZIOB0nlqHg65PO5I6OxZN2AeXMcdiLxQWHfGWTlWlZHn5DKdJytBuaT0WbBklYWOs_HoK-sJTnRbGyk79wOw4XLoPhUsSl0zvgPGi0s-r8okJNKbIc5p1jt8KbwMQRJFgJkcX05PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اطلاعیه مهم برای حاضران در مراسم تشییع
خبرنگار خبرفوری:
🔹
از مردم درخواست شده از تجمع مقابل مبادی ورودی مصلی خودداری کنند. درهای مصلی از ساعت ۶ صبح باز می‌شود و زائرانی که از شهرهای مختلف آمده‌اند، برای اسکان و پذیرایی به درِ شماره ۴ مراجعه کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/666120" target="_blank">📅 22:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666119">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65dc29f2e0.mp4?token=fvJOI4g77f4noe_kY3zX9OIk-34oNMXzVwdv0wWp0EJfg0HCGx2dh9WnIkZtFy0JqcPkpME74lZWCIyDtnrgZ-ra3y_mqAjIUDulCY2Lh0A1wkDESI_WhVMjAxD3jp0DAongoFLHQHAizxQodEDAsl6tHDJsXSKWzdMxSHs8mFv27X5p7S1UcA9W9dt-RY0ou18xcGvAtuzyTKpSyP_dj03s9HRCq-muCUQLIjCGysFVby8nYbhXBF3rRH3T5LN5WkCrYwyoH2v--KLmSTc6JSxQauZx1T3Z2-psIOts_CJr9taB_U3hyJk1IaAt85PnnBmpvGoptT0E0_a-2uNglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65dc29f2e0.mp4?token=fvJOI4g77f4noe_kY3zX9OIk-34oNMXzVwdv0wWp0EJfg0HCGx2dh9WnIkZtFy0JqcPkpME74lZWCIyDtnrgZ-ra3y_mqAjIUDulCY2Lh0A1wkDESI_WhVMjAxD3jp0DAongoFLHQHAizxQodEDAsl6tHDJsXSKWzdMxSHs8mFv27X5p7S1UcA9W9dt-RY0ou18xcGvAtuzyTKpSyP_dj03s9HRCq-muCUQLIjCGysFVby8nYbhXBF3rRH3T5LN5WkCrYwyoH2v--KLmSTc6JSxQauZx1T3Z2-psIOts_CJr9taB_U3hyJk1IaAt85PnnBmpvGoptT0E0_a-2uNglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/666119" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666118">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ایران آماده میشود؛ برای دردناک‌ترین و در عین حال باشکوه‌ترین بدرقه تاریخ...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/666118" target="_blank">📅 22:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666117">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آغاز محدودیت‌های ترافیکی مراسم وداع با رهبر شهید در محدوده مصلی تهران
🔹
محدودیت های ترافیکی در محدوده مصلی تهران به دلیل پیش بینی حجم بالای شرکت کنندگان آغاز شده است و ضرورت دارد شهروندان برای شرکت در مراسم حتما از حمل و نقل عمومی استفاده کنند. #بدرقه_یار…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/666117" target="_blank">📅 22:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666116">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oit2iYYuICEJgvDnTqbboaoBYTVugJ0ZBaRnbU9Cc5bspyLGIMZ87TcySr9PVLylBOG9Rbtgp_4L0T4J2z732qkFwl8WDaWuOQOVxw3J3fNtAWoei44V5xKbzp7YhQk4otuU_oR_lf_7gGUNZgfsSm9Xx_aKndO26a8Y0XJ12pVi9UldOT4wjFrp7MzxdyVUAYRjuO50sSgNdhHPhGv6DZWgsFX0Z_YrwQPDHt6IEsTdaSI2Ve7YwtNG7HNN574lXIeUjeDr65g0N7CVKHVfdvhxM5eeZw4VwKAJaoPRkDFmL21NxiKtNivvqBM00yBt15Prn1e8AWjxcrFUqRwFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/666116" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666115">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c51b3a8791.mp4?token=kCpquN0cqxdxwucHd3YZYysDa_eXvy_xpbG9nc_SuDM1oKJt6m4RQQ3nRn9-g1g2RquoOO3kA2n7oaoNpzFWC8Z44zGD1xyxWCDbtwMYeRBIq4h5jnflCWZtZrUAJqPVbqhavJ-mFfCwsEUYkCW5BuQookphmLIxUrtULXlNf7J3d6j0kPPsUXsMWLi0-iVsT9-JsLYzLh_BgwrKfwR2_kLVM0iOjXzpfjABam2N_1OZMWaN3U_lpvmy310QfJvdTpCfz7VPATuADwGNraRiPLpgXfrW8N12qYApYlx8oxrLwUKupIthezf0NPxPznvSk2shWFGqWz3bnMlmuno1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c51b3a8791.mp4?token=kCpquN0cqxdxwucHd3YZYysDa_eXvy_xpbG9nc_SuDM1oKJt6m4RQQ3nRn9-g1g2RquoOO3kA2n7oaoNpzFWC8Z44zGD1xyxWCDbtwMYeRBIq4h5jnflCWZtZrUAJqPVbqhavJ-mFfCwsEUYkCW5BuQookphmLIxUrtULXlNf7J3d6j0kPPsUXsMWLi0-iVsT9-JsLYzLh_BgwrKfwR2_kLVM0iOjXzpfjABam2N_1OZMWaN3U_lpvmy310QfJvdTpCfz7VPATuADwGNraRiPLpgXfrW8N12qYApYlx8oxrLwUKupIthezf0NPxPznvSk2shWFGqWz3bnMlmuno1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای خونخواهی مردم از زبان مداحان: این مردم پرچم خون خواهی را زمین نخواهند گذاشت...
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/666115" target="_blank">📅 22:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666114">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvly_IMaVE2PFO8_Eh3_JDNM-HMyyGm9T-0d6UUK7p2LxanzgwNl34xu31a6Nw0vv1FJ5ykNSe7P1nR-qjm6Nwnw72dAl5Ate8_Y8VMsTGV_CLlUaDs-zNS7ZKbovXAykjONosrz5mRCwS07RrfqYBQE1bSBjU-h7iJmB9wrppdfubIy6zb7HWvMZHfkVWv-fnis0Ge4sRmLG6xWPajsQRXOCEGXiAB9cZdDgniNmUTXwJpsbX7JBd0cwVpM-UzEMq1x8N25q4RCrDY9ZiJvRF7LrwYwxIq0PkRoBGmOTMGN0edECgwUX7Hc7-RCRE43d3zjwPrfL6kbpLAJbnA8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◼️
ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری برگزار می‌کند
کارگاه فشرده «عکاسی با موبایل»
◾️
تصاویر ارسالی شرکت‌کنندگان، در صورت برخورداری از کیفیت و استانداردهای لازم، در رسانه‌های خبرفوری منتشر خواهد شد.
#بدرقه_یار
ثبت نام از طریق لینک زیر
👇
https://survey.porsline.ir/s/3PHWMjxm
@Badragheyar</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/666114" target="_blank">📅 22:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666113">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdHpbm5vQ4i_k6yZ55BhQxvSFuBvPv5CudHmdrstiQVCg6SxfvC2nz7C7n-_uCI0CcFz-evJkAkI410HU9Rltgod7kaBoGakDk4t9MDmrrrxeavIJb0-_V7u8sJ8QRcoqgxbXymBt3Urk2iyllYKDslshx5UHAx-ce7Cd1kVxdWDVymJ0Dgbd_V671gPxVFTXNe-goY-4pjoquvgBNbFOMBsb_YPHD58t5dboR_QNV8UMK7gyMJaJUoQF9au38ueHQ2V-3spSipp4jwIZhhkCE6gkTEBLLsrXBr6rqI1gZGAw8o5FKcAxD57pw5_qWA-pNE8Ivva2B40XOkN4nY5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قالیباف به گزافه‌گویی ترامپ علیه مردم ایران: به فکر سوء تغذیه ۴۰ میلیون نفر در آمریکا باش، مشکلات خود را به دیگران نسبت نده، ایران خودش درباره دارایی‌هایش تصمیم می‌گیرد
قالیباف:
🔹
تصور کنید بیش از چهل میلیون نفر از شهروندان کشورتان برای تأمین غذای روزانه به کمک‌های دولتی وابسته باشند، اما همان کشور، ملت دیگری را به گرسنگی متهم کند.
این حرف از سر واقع‌بینی نیست؛ یک فرافکنی آشکار است.
🔹
توصیه‌هایتان درباره برنامه کمک غذایی (SNAP) را برای خودتان نگه دارید.
دارایی‌ها مال ماست، انتخاب هم با ماست؛ شما هم بهتر است به نرخ بالای سوءتغذیه در کشور خودتان بپردازید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/666113" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666111">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
چراغ راه مبارزان حق
🔹
در تاریخ پرشور شیعه، نام‌هایی هستند که فراتر از یک شخصیت سیاسی، به اسطوره‌های مقاومت تبدیل می‌شوند. شخصیت ایت‌الله خامنه‌ای نه‌تنها به عنوان یک رهبر، که فانوسی فروزان در شبستان تقوا و عدالت بود؛ مرجعی که کلامش، طنین زنگارِ ظلم را در هم شکست.
🔹
او در قامت یک مرجع تقلید، پل میان آسمان فقاهت و زمین مبارزه ساخت. خونِ پاکش، نه پایان راه، که آغازگر حماسه‌ای تازه شد؛ حماسه‌ای که در آن، هر شیعه وارثی برای خونخواهی اوست.
🔹
خونخواهی او، فقط یک شعار عاطفی نیست؛ این رسالتی است بر دوش تاریخ. خونخواهی یعنی زنده نگه‌داشتن خطِ مبارزه با طاغوت، یعنی تکرار نکردن خطای کوفیان در تنها گذاشتن امام خویش. این مطالبه، فریادِ حق‌طلبیِ نسلی است که خونِ شهید را در رگ‌هایش حس می‌کند.
🔹
امروز، دل‌های مؤمنان با یاد او می‌تپد و مشت‌هایشان برای قصاصِ این جنایت، گره می‌خورد. خونخواهی، لبیکی است به ندای غیبی او که از ما خواست تا بیدار بمانیم. ما مدیون خون او هستیم و این خون، تا ظهورِ منجی، چراغ راهِ مبارزان حق خواهد بود؛ مسیری که در آن، ظلم هرگز به اوج نمی‌رسد، چراکه خونِ طاهرِ مرجعیت، سدی استوار در برابر سیلِ ستم است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/666111" target="_blank">📅 22:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666110">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548f5f5f40.mp4?token=A0yt_2xc_Gg5lHyRIVh9YxDPXAprDfURv0TEGlJdi6XelwmDGsfxEyGJlkrQZBOE231UY12YILcvAz8WG5AwAx5pHLZVNuwSTob2F-JWdfHbz5Angl0Wm5usZgKJUwzwgOm3LWTin01-Zoebyx7Qpn71shGkGzXC4d5vDen8ouvK1L6_hUCGkKfxX80XhtuNPSnapRSWcNwdCPp2WTq6Q2kxj0FH-Dwrok8vp9cVGE0bUSb5a3GHiuamwGrb_Svc8f2rWYZkYRwagmz0vcmeULSoOTIl9CtJS2s-XuolNYFaxd5b7z4q8E6zKqSwOQNpcy4wZQRpTQ4Yli7VsoacKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548f5f5f40.mp4?token=A0yt_2xc_Gg5lHyRIVh9YxDPXAprDfURv0TEGlJdi6XelwmDGsfxEyGJlkrQZBOE231UY12YILcvAz8WG5AwAx5pHLZVNuwSTob2F-JWdfHbz5Angl0Wm5usZgKJUwzwgOm3LWTin01-Zoebyx7Qpn71shGkGzXC4d5vDen8ouvK1L6_hUCGkKfxX80XhtuNPSnapRSWcNwdCPp2WTq6Q2kxj0FH-Dwrok8vp9cVGE0bUSb5a3GHiuamwGrb_Svc8f2rWYZkYRwagmz0vcmeULSoOTIl9CtJS2s-XuolNYFaxd5b7z4q8E6zKqSwOQNpcy4wZQRpTQ4Yli7VsoacKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار سید مجید موسوی، فرمانده نیروی هوافضای سپاه در مراسم بدرقه پیکر رهبر شهید انقلاب  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/666110" target="_blank">📅 22:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666109">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
قیمت طلا بالاخره بالا می‌رود یا پایین؟
🔹
بانک سرمایه‌گذاری گلدمن ساکس پیش‌بینی خود از قیمت طلا تا پایان سال را از ۵۴۰۰ دلار به ۴۹۰۰ دلار کاهش داد.
🔹
در مقابل، سایر مؤسسات مالی همچنان دیدگاه صعودی‌تری دارند، به‌طوری که مورگان استنلی قیمت ۵۲۰۰ دلار، جی‌پی مورگان بازه ۵۰۵۵ تا ۶۰۰۰ دلار و دویچه بانک سطح ۶۰۰۰ دلار را برای طلا پیش‌بینی کرده‌اند./‌‌ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/666109" target="_blank">📅 21:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666108">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سی‌ان‌ان: تشییع آیت‌الله خامنه‌ای رژه پیروزی ایران است
🔹
سی‌ان‌ان این مراسم را اقدامی عظیم با مدیریت میلیون‌ها عزادار و تدابیر امنیتی بی‌سابقه توصیف کرد.
🔹
برگزاری چنین رویدادی پس از ناآرامی داخلی و جنگ با آمریکا قابل توجه است.
🔹
یک پژوهشگر نیز تأکید کرد ترور او جایگاه نمادینش را در نگاه حامیانش تقویت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/666108" target="_blank">📅 21:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666107">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6d9ac65.mp4?token=dHf66nVMhuYubEH3kWfT7LiryCMV36s1TgMdQm3dm1ylYB1BYp8L_M-TSMpurJlTamr4DQrWOvu-Ic816dlZtOzZ3DZzVk0llMAD1hToopD9oUYuL_d6M58BVInMZry8l_AaP-H2xTOpWeARCMqKMcUhXlDQ635ZMN3Up_i38qq_MLAZyv_LDHSo2oLV3UWXkAPUr7GTEHXes7-CHsQ3EUGwxYfT2XmxEMwPenfcRGpEB3ijjUuis6OnNForn7620MOWQHT500zISjw-J3ED2L9m5cQSq8YFdRbV8owSKBfPuT-omEEMT8tEKhYgpBK4QahBZGzu7g-WcaFJ19S4HHEagGt7oQylwFsxo_gSrxHXZ3V1qO-09pnw41wGKlwrfNLmh-gADaoKeP9tjVnlYSkQIBKLyc67eMZkirIyr4rjocPlzBVjodp_6adeAFd3x3K9bJKtQuUPpViu3jGpJnzyNSESgRqjGOvnQj1QH-z25RaOEBshRu6-Dqc8lhDFRa3Thks2uOKX14qClMTRhR_gq5qT5F7PWJlcXPdGPK_f1BP9-jhGC34yOpKoUuKwWgyjm9QERPNeNATIGFSVXZdMuotTgob4UA9y0298NV-PGDiIBPmNplD_Kyir77HbxeWuUQk-UPJUL4hjypjjPEeOnZT8O0__BM6IcdF7GeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6d9ac65.mp4?token=dHf66nVMhuYubEH3kWfT7LiryCMV36s1TgMdQm3dm1ylYB1BYp8L_M-TSMpurJlTamr4DQrWOvu-Ic816dlZtOzZ3DZzVk0llMAD1hToopD9oUYuL_d6M58BVInMZry8l_AaP-H2xTOpWeARCMqKMcUhXlDQ635ZMN3Up_i38qq_MLAZyv_LDHSo2oLV3UWXkAPUr7GTEHXes7-CHsQ3EUGwxYfT2XmxEMwPenfcRGpEB3ijjUuis6OnNForn7620MOWQHT500zISjw-J3ED2L9m5cQSq8YFdRbV8owSKBfPuT-omEEMT8tEKhYgpBK4QahBZGzu7g-WcaFJ19S4HHEagGt7oQylwFsxo_gSrxHXZ3V1qO-09pnw41wGKlwrfNLmh-gADaoKeP9tjVnlYSkQIBKLyc67eMZkirIyr4rjocPlzBVjodp_6adeAFd3x3K9bJKtQuUPpViu3jGpJnzyNSESgRqjGOvnQj1QH-z25RaOEBshRu6-Dqc8lhDFRa3Thks2uOKX14qClMTRhR_gq5qT5F7PWJlcXPdGPK_f1BP9-jhGC34yOpKoUuKwWgyjm9QERPNeNATIGFSVXZdMuotTgob4UA9y0298NV-PGDiIBPmNplD_Kyir77HbxeWuUQk-UPJUL4hjypjjPEeOnZT8O0__BM6IcdF7GeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
من آدمی نیستم که با لالایی دشمن خوابم ببره ...
🔹
نگاه تیزبین رهبر شهید انقلاب در  دشمن‌شناسی و جمله‌هایی که ماندگار شد.
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/666107" target="_blank">📅 21:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666106">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=F3XyeoPhAfb972S2syEsFTJBQyKeipC3RJohz1-U34A7orss6PHkD3ckBZrdBgdaest6zz4nvAabZvnkp4kTYKnmGJFvmTiHcih0TpERgAa5VvR_W3VUSfVlmS9m50EdpvqhS-mzV4FF-XVcd-hCHplEhnAGq_3rVTKpLwDQExm_zuzOTdOJWx2a40qnaEux7CsZ49YoQ1Rl3NRk69CgWhpvovdWVRVeUm7R5h1nU1LOdyA5RihPgbdoai_ho3t-aFjr9XSRvpaGHAEWOkmMAiIUtzpla8FdwiyAaQPJFpxprHIr9YD7qCr3ByAh4N3hK5lJdsn_1dwMv2yp5BSKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=F3XyeoPhAfb972S2syEsFTJBQyKeipC3RJohz1-U34A7orss6PHkD3ckBZrdBgdaest6zz4nvAabZvnkp4kTYKnmGJFvmTiHcih0TpERgAa5VvR_W3VUSfVlmS9m50EdpvqhS-mzV4FF-XVcd-hCHplEhnAGq_3rVTKpLwDQExm_zuzOTdOJWx2a40qnaEux7CsZ49YoQ1Rl3NRk69CgWhpvovdWVRVeUm7R5h1nU1LOdyA5RihPgbdoai_ho3t-aFjr9XSRvpaGHAEWOkmMAiIUtzpla8FdwiyAaQPJFpxprHIr9YD7qCr3ByAh4N3hK5lJdsn_1dwMv2yp5BSKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسعود ده‌نمکی: در تمام سلسله‌های گذشته، خاک ایران از دست رفت و کوچک شد ولی این مردم اجازه ندادند در جمهوری اسلامی یک وجب خاک ایران از دست برود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/666106" target="_blank">📅 21:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666105">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=jfG4nzolmnmIalfq9WVs1gq4WJ-EwxO1VpQarOfZtpUlq981id7GIrQ-4FvtTZu7uYtjSR-HJaaEHItfUgAyiq-7-db016XWQFAkhXCDbDLD1hlTJcxhr99RQ9EUkAB_K8Y-Cmt6Qkk3_MzxTS3jGnejWeBqiB4hKWGKLwCe_KnfnPzFPNEKiMeknEUMhzPorE80AVxMvJDaMl3q8VrMVqtBsw2vv1bzLctSLgHw6bDo6TYzSCbAbef7h3djv_k7HJZJ8an8vZNInCg1nYHlPI-QuFzUaFpUBjgOTsDA9mKtSG44908n-VpnwFCFQsYv4blviZKcULDffO_VEaOA4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=jfG4nzolmnmIalfq9WVs1gq4WJ-EwxO1VpQarOfZtpUlq981id7GIrQ-4FvtTZu7uYtjSR-HJaaEHItfUgAyiq-7-db016XWQFAkhXCDbDLD1hlTJcxhr99RQ9EUkAB_K8Y-Cmt6Qkk3_MzxTS3jGnejWeBqiB4hKWGKLwCe_KnfnPzFPNEKiMeknEUMhzPorE80AVxMvJDaMl3q8VrMVqtBsw2vv1bzLctSLgHw6bDo6TYzSCbAbef7h3djv_k7HJZJ8an8vZNInCg1nYHlPI-QuFzUaFpUBjgOTsDA9mKtSG44908n-VpnwFCFQsYv4blviZKcULDffO_VEaOA4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل جهاد اسلامی فلسطین: خون رهبر شهید مسیر آزادی قدس را قوت می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/666105" target="_blank">📅 21:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666104">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7af27e340.mp4?token=uBn7hnydhy-cZP0uf2hDQRtqmsB6n21BUJZlJzQPYvr3Np-DfJA8UG8tttqhdSLQYwMLxkc8iVplR-28S54ObdI19U1AGIySu72hrt8VTRMvkn7LX4BLX2uFddW0BCnIp-G3xYlnPCLq296Eljiay37I3Qw5jeYzaMwLn-p7ZRe5QVkzk4J_1-krfzA75jzHuD5zxBvBZAAkcMp6tJmXrGCDILAOmZw_sLIHyA7IAVfy4sZusqU072z6nkzD4KOZu-RHvcpy_RErgumOWnbJ-OYr1k-pr_0krxk8PCLs9OJXjx2H7k4760ghSwX05E7eHY0z19A-i8cGmg2T9qyRjki0JlqthwncvFaws8D3x2C1P9Fn_89pIsfGJm8BkUcC2Dm8f0SkXrS0IzoiHgiO6QNn92eCjmz0Pk2lfWoohgkpExqBtD2wGQRptuyzl9XlAh4vhU9y6aHfF8i5GyhqFd5oYXgfmNIIftdw88nHWFt2Mb0kssIvyjX_gMv9eiFu4Cc14hKl86EZqd7TbCqYuIWDZn9l0NIohAPY-zAA7z9KQcobFBk26Og0V8Q4F2EHZSUB2fUx99fmJa6XCjRZCz_HpUIvjAouwGuMdkQ2ZyFDS4VdvTFN-bM-fGKD2deTxIFuIm2uIUuYGqzmWBsW6BfWI58aefsoQXMfXdtgAfE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7af27e340.mp4?token=uBn7hnydhy-cZP0uf2hDQRtqmsB6n21BUJZlJzQPYvr3Np-DfJA8UG8tttqhdSLQYwMLxkc8iVplR-28S54ObdI19U1AGIySu72hrt8VTRMvkn7LX4BLX2uFddW0BCnIp-G3xYlnPCLq296Eljiay37I3Qw5jeYzaMwLn-p7ZRe5QVkzk4J_1-krfzA75jzHuD5zxBvBZAAkcMp6tJmXrGCDILAOmZw_sLIHyA7IAVfy4sZusqU072z6nkzD4KOZu-RHvcpy_RErgumOWnbJ-OYr1k-pr_0krxk8PCLs9OJXjx2H7k4760ghSwX05E7eHY0z19A-i8cGmg2T9qyRjki0JlqthwncvFaws8D3x2C1P9Fn_89pIsfGJm8BkUcC2Dm8f0SkXrS0IzoiHgiO6QNn92eCjmz0Pk2lfWoohgkpExqBtD2wGQRptuyzl9XlAh4vhU9y6aHfF8i5GyhqFd5oYXgfmNIIftdw88nHWFt2Mb0kssIvyjX_gMv9eiFu4Cc14hKl86EZqd7TbCqYuIWDZn9l0NIohAPY-zAA7z9KQcobFBk26Og0V8Q4F2EHZSUB2fUx99fmJa6XCjRZCz_HpUIvjAouwGuMdkQ2ZyFDS4VdvTFN-bM-fGKD2deTxIFuIm2uIUuYGqzmWBsW6BfWI58aefsoQXMfXdtgAfE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همونی که براش نمردیم آخر سر فدای ما شد
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/666104" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owDtCvR8tBf_0VZXGLaMzt2WZHtsUoaWmxa-kteMODlSIw48usQmxVfMFMSZltk4q_GqsN8kkyzB5kleDFTFEuyG1rwQvkNBzfB30UOckHqoFQGhDO5sgLtxTn0aL5YyOHkAp_gKSiEPHBU1nIOVBho5jX_tp33YFjRTsdtnvmfx7HoRUw7VJuDyYK2PwiJCfet53di62uLZXyq_FNx4Ls0urrMBX0U_uswonnFUb6RfezLYB_rANUbcsAtq1NB5T4OSDGTa9-j4azMwlFkNJ3B9cH_3B1LLG64jd5QfqJ1bZXVkYrgTvvbgz7ngQYS95tAFxu4JKhQQHx44MgQEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abXf3QGkUZIzM0iXHVg4g7oIEAty9C1grkjAOBk6MaBcLDBf-4OpmAW-m4IRqtMDcpLbleyyk3arfuQ7KP-n8YQuZhKbn2apYEs6Fjcs7QOmfyTIqw7C56ocC6Li-IVkDe0HO_tvhGwaHtxaA5oDRQQVp2i6fTpe_uY4nPFoSjlk4YoZKv9broXz-QRBaUOm6QFCidzrchNQ4cnxvDM8ZBLphcGajHt6PU2GFO55UjWWLwfbNwuStwpf4oqYbZ-ZuU0VMfSAU1Z7qNPVCt5BdbeJTujJpwTmADvDvZrlO9yslyozSccB6-fIsn2ZDaapnPs6YAd3A6CjOfNstNSdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oD7Q_Vb6WQ1QP-pwjxlUo5wmTM8UHnv0GjnDHUl4rAFI6UzU5zTqu2ghjjZh4xZD5zMJQucsJEAkbCH7kzQdeptrmGQoqR07KAuEFPBorYX01SgI5qbeNuTPpBja5bheuFZe4CohpqK14DknIfv-zupe26PvCGNDRmHsxYxB2ymrTijxRWBkK_ldzBmvBrJ6FUQ4G0r9ooFpFxwO50cOwKYdBezyEGl4im0VleWpkAjeTp1GqDQczuzsGf_uWUddnTsi2gdSCDAgey8exPDm12O7DxvXU9UOAZFWUjE4I6P1ILbFlQh1Zsm1ZAJCqqjPXXddMGWE3l_Loc1GM0BFvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnHJq52-4zOrnHLZMn-0JLdMQyvLcfec1Z3B8GnpcGfH8pE6fxo3nl7URbSMrWaHQ0kZc1VtaH9lnqB2klPKAlUxITDW4FkUi7akpGL8YHLhgSuyNEgFPpEc-CqjNZ6t-jG4cq5onc0FknqmDxDrsDv00aTZnPTJwaZIQB0bVzbTZJmfIH8zAc4X-njw6lyhLL98l-NukZa_MYucJh6UWLGHDxqfyIyV4yQueJL7kDuZOel7cYEg1W3NHZ2qp_9jeZ40u-MZzlw64vRUvaWzlUf9NCdQDRkROHN0_rn8NSoFMJ9HxgBO6PW9tNttWpPrnqgItYNkgPVd3bH4ran0mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvavUxoHGvbOdGWl_XrswtRc7d5cNv6G5KulbUKv3Uys038BQKH6yzl_45wDiMTxrtITIorp2W_s0dmqOy5ok_CJYE7BlsliwxBrUdhqT_vGGlaohJNi5Dx4U333RVFD48CBr22AFtVc8QhtR-ua2Cb2jj_7gsWObrP3hSbmMibZXsH2bXuNVD3O2gyesdu51G346AjVFCYJ40XRdGJCWcmxRY9HGhaSE1FnefNvOE77wij3GEr5XzDp_HSy820vMaGByI47T2IBuKiLyKDtnaDq2orJZNJjIaeSmzX0Znrva6KDxh-4rScW9w4t_V8ugk9u5Bhi1heNTKp-2sEdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkXE3lB6p1T2flU5u1M_TnzMWy-lQejL5LEFhPPswd763waTLMgbehMTdly1eJQxpKWi-C0WEJT8yE0DSryZwQnG3bpGgFvPhlwDKDU4cCR5SZpPb8tqhwBbq44KZN_NX6BQoLbFD4P3xXouL_y5VeIgYVd4geuRkTNiTm2f6IYrJdjJCAo_eKozV50y8TFG5aQuI32mX1oswL4dC4ezaTGTcFXlOxZk2tTRU4DjrJtIycp9q5CjZMiTmKbKo0K14NCKoHUCgwNs1IrsUxoNhgNFoANDjfoHtSSCZKB5JvpCN3Ghk67cjAx8lA4Ahamb30CAJ0H7-jZuL1tMpVKrzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دونستن چند نکته میتونین مناسب‌ترین مواد غذایی رو طبق خواستتون خریداری کنین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/666098" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666097">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
افشای‌گری و بهانه تازه در آمریکا برای حمله به مدرسه میناب
🔹
یک مقام آمریکایی با شرط فاش نشدن نام به آسوشیتدپرس گفت که پنتاگون از همان ابتدا می‌دانست که مدرسه میناب مورد اصابت قرار گرفته است. این ساختمان در فهرست «ممنوع‌الضربه» (no-strike list) به‌روز نبود.
🔹
یک تحلیلگر ۷ سال پیش مدرسه بودن آن را شناسایی کرده بود، اما این اطلاعات به‌درستی در میان بخش‌های نظامی و اطلاعاتی به اشتراک گذاشته نشده بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/666097" target="_blank">📅 21:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666096">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=Ihcs4FtnBTYJdZXYSPx1X9FSiee5KeY6EwI5Z_KNMSoMdzGiokluCIOZc-ho68z4p3T1-4s4M1FkFIUWztPFl_uVomkKvlMKzmhuRdw_fRmNeAi6Vh6KJF16kiKGRfEJhsELxiUsuiY9nGBaRdaCNj_S8lCG1lWKI-UMndOmqLysVTZ6cT-WAaMr69V4JQt8_b6OR5W9GYXQFllyaU4jhHfU0SucEHgsrAMFWHNYHqyVktOl1XvqlFOcVZ9rPzwB2ljGFc6f2VT-oL7RaCtUe8HR1Y1rXi5fq6wk11YbPs2BoycD5shanXPdwTzZPjMwCHxNOFz4S8kQ6LMCL2bk-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=Ihcs4FtnBTYJdZXYSPx1X9FSiee5KeY6EwI5Z_KNMSoMdzGiokluCIOZc-ho68z4p3T1-4s4M1FkFIUWztPFl_uVomkKvlMKzmhuRdw_fRmNeAi6Vh6KJF16kiKGRfEJhsELxiUsuiY9nGBaRdaCNj_S8lCG1lWKI-UMndOmqLysVTZ6cT-WAaMr69V4JQt8_b6OR5W9GYXQFllyaU4jhHfU0SucEHgsrAMFWHNYHqyVktOl1XvqlFOcVZ9rPzwB2ljGFc6f2VT-oL7RaCtUe8HR1Y1rXi5fq6wk11YbPs2BoycD5shanXPdwTzZPjMwCHxNOFz4S8kQ6LMCL2bk-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس موزون برای اولین‌بار راز گلیم‌های آبی بیت‌رهبری را فاش کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/666096" target="_blank">📅 21:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3106e1b313.mp4?token=p2Y0lwBNSZ-_aaO08hK6B37mDB6tL6jeainvElhNUWlbUZBlIZADV2_oU6qn1jeMfw4IlUIp5ooz9NBvrImqDKCOeRkq_O1Oc2B2j7bbUpGNs8NAvxjGZtXFhElJhzJTF5LtH62SdVchKlyBSRWKTsQ_KELDAc-6VATjtMnym78DtjDHzGnYHGnfKKrY-DnGdasJPtd6RANLibFaMV4WuTZlQYYozCOC2_mA4X2fiMM_qlL8M-SniYfTVbDNIdg18nu76fxjkLL6t5iFtqqVIcEimqEKDUppVF1NfIW4_uVrzKE8hSL8u0dDYUmniOmaao0rFVA9v96t3doUri5UOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3106e1b313.mp4?token=p2Y0lwBNSZ-_aaO08hK6B37mDB6tL6jeainvElhNUWlbUZBlIZADV2_oU6qn1jeMfw4IlUIp5ooz9NBvrImqDKCOeRkq_O1Oc2B2j7bbUpGNs8NAvxjGZtXFhElJhzJTF5LtH62SdVchKlyBSRWKTsQ_KELDAc-6VATjtMnym78DtjDHzGnYHGnfKKrY-DnGdasJPtd6RANLibFaMV4WuTZlQYYozCOC2_mA4X2fiMM_qlL8M-SniYfTVbDNIdg18nu76fxjkLL6t5iFtqqVIcEimqEKDUppVF1NfIW4_uVrzKE8hSL8u0dDYUmniOmaao0rFVA9v96t3doUri5UOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش خبرنگار خبرفوری از حال و هوای اطراف مصلی تهران در فاصله ۹ساعت مانده به آغاز رسمی مراسم وداع با رهبر شهید انقلاب
/
مردم پشت درب‌های مصلی ایستاده‌اند
#بدرقه_یار
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/666095" target="_blank">📅 21:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1429dd2146.mp4?token=dnu7UC88PXn9p1y9FjX0x4zrdFLx266JBPhszJJrqJNHODs8ZoToxFY20BbYdS9zjUrbxffRmP_H-Jlr6DXhh9Zg7SxGnsAftZfP5dkw_pFgNfdQZSWNLjLETsh9YVsMKwLTEcKDGpGbmJIMaI1tEjLY9ILtqzQbgnsD3ONqRecAzwTvDUcDzU9GPPy6rswqQkZhM3K05OWddD2KpKMZJn_HWJOrA7wAiCY4Bq9KGWFFXf2RLFIbtJbEmaJMRLC7MPIDc7N2MoRz0W2oOmVYeJHK6lvygkQJiNrQM4UAXJYDXqJNzVDqSz-VxGLqsNpO8V_XTYvs70QNsGdGOAXP2EXMk9W1Oe_MlGa9hs-zhR6kJQlwi1d3keAsZAZvSONTIKoAGORt9NhS4TtHLNHjfDMtWuhJmOJQxFzbmxiRTxOnftwMAVjIdme7sNpzILeD2uCN0Q_BN8bLOZJcY4NThid9OIyz98nn3hqSPSs_vlmmLh1YA9KPjK-_bwQwFxhM2-zHG-XTLgK-Mks-qhnVg8PjeqsvYPCXNCMyn-ORh_D9Mkjc-od99EtacAF3OQcCbH_kXejrxNxPmeJxii6edidGEhmuddftgIwjRcuc7omlcGNawE__Gabv_BSHEJXakPNm7_K6GrdGMALDbBLG32AywEPcES2FfL6v8smbFiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1429dd2146.mp4?token=dnu7UC88PXn9p1y9FjX0x4zrdFLx266JBPhszJJrqJNHODs8ZoToxFY20BbYdS9zjUrbxffRmP_H-Jlr6DXhh9Zg7SxGnsAftZfP5dkw_pFgNfdQZSWNLjLETsh9YVsMKwLTEcKDGpGbmJIMaI1tEjLY9ILtqzQbgnsD3ONqRecAzwTvDUcDzU9GPPy6rswqQkZhM3K05OWddD2KpKMZJn_HWJOrA7wAiCY4Bq9KGWFFXf2RLFIbtJbEmaJMRLC7MPIDc7N2MoRz0W2oOmVYeJHK6lvygkQJiNrQM4UAXJYDXqJNzVDqSz-VxGLqsNpO8V_XTYvs70QNsGdGOAXP2EXMk9W1Oe_MlGa9hs-zhR6kJQlwi1d3keAsZAZvSONTIKoAGORt9NhS4TtHLNHjfDMtWuhJmOJQxFzbmxiRTxOnftwMAVjIdme7sNpzILeD2uCN0Q_BN8bLOZJcY4NThid9OIyz98nn3hqSPSs_vlmmLh1YA9KPjK-_bwQwFxhM2-zHG-XTLgK-Mks-qhnVg8PjeqsvYPCXNCMyn-ORh_D9Mkjc-od99EtacAF3OQcCbH_kXejrxNxPmeJxii6edidGEhmuddftgIwjRcuc7omlcGNawE__Gabv_BSHEJXakPNm7_K6GrdGMALDbBLG32AywEPcES2FfL6v8smbFiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رهبر شهید از مردم تبریز:《مردم تبریز را متفاوت‌تر از همه جا دیدم》
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/666094" target="_blank">📅 21:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN3Ec0y0HhxSJaznUj6n2yGgAQK9hqJYoVATDfcimeDgJyxzx81XXhoEjPkbiLW0IiDS4fHxV-AfHlKkQXAsxBXqc5xqdnnu9xoNX8MQcmKltRs3VQXNgbtQ7hp4l620lCeAAczPtfQeUs3PgTsthxsOMVg1cguTcDBl-GkaMbw4PW77-M9jGHa-mb3I6f_PSnLLk9pk_baW4e-dtIZ7vSr_6Vro5LtG9Bl_W7Z5jgq2xbUIhwCD91SrWlhVmRy0UG_HWn4HTdgVMZOgCPb1kNOKBCPi-3a6NrEWxC8HFahM6gfBdkDOi29NZGNJNSOFEhjTg4QbUaGzDXPXrMtU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب ماندگار از پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان در جایگاه مصلای تهران   #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/666093" target="_blank">📅 21:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666091">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae1aa8593.mp4?token=nt-muxMBiOHdP5WRisYD2MSQnT_1Fg1qsv8YHjJHPXAc_7KnlpEeEhCDAVfPC4SN2UEn-YIh5n1uHuMsYf3Z4R48DL4iiI5NB8TfuW3hz0w4ufWpR4e1aWGvn0MHcJhWl7p96hO3g7PYh2JwZz1ce3nlpOxR_z7oCk04v_3j77n2-vYF43PIG8FexfswcKVAt4D8sOhKXh_iLk4UQQTAkCmLPZ5kOjpCvGpFpWHR16IK0U9R1hSvRIUdhnas13yVPzXaHonqt34BP9CaOZbNxRf7mHoREblz_42WpNvc7_xupMhn_3wdF0AIh8Bv7kEeBYGOWp9v1pfl0LgHJrqygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae1aa8593.mp4?token=nt-muxMBiOHdP5WRisYD2MSQnT_1Fg1qsv8YHjJHPXAc_7KnlpEeEhCDAVfPC4SN2UEn-YIh5n1uHuMsYf3Z4R48DL4iiI5NB8TfuW3hz0w4ufWpR4e1aWGvn0MHcJhWl7p96hO3g7PYh2JwZz1ce3nlpOxR_z7oCk04v_3j77n2-vYF43PIG8FexfswcKVAt4D8sOhKXh_iLk4UQQTAkCmLPZ5kOjpCvGpFpWHR16IK0U9R1hSvRIUdhnas13yVPzXaHonqt34BP9CaOZbNxRf7mHoREblz_42WpNvc7_xupMhn_3wdF0AIh8Bv7kEeBYGOWp9v1pfl0LgHJrqygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود خودروی حامل پیکر مطهر رهبر شهید به مصلی تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/666091" target="_blank">📅 21:19 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
