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
<img src="https://cdn4.telesco.pe/file/iBBnj6TmPR_opyBQUkrk1K27OUvrgYHEsBE8EcfElK7up-zrRZrGEORGCE8oT0_UQI_VVqVv4CkOHE7ixwpsxDkOOV7YAcOaumtR4tz2aMLuR486YVaS1uUKidGNZNfPgtvxlhZhYRT779hIMhEeag55ztyoMBN1xmexdjO26p2SfddNYJtTnYC5aMXMrU09AZynoiVbEG-WYGm3tkJnFp7-3qt1iw8J1Hm8rFKsxbFo5jOCTHpI4ZK0DlFtYXVx-wFAFde5Yfc20yrzpRyWgYCHtjZwvc2_hzjZ_NpmH4ljWOzm0SAN3xwv-SAxCxB9OIKsgGY6_owvYgAGjqe02Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 09:00:12</div>
<hr>

<div class="tg-post" id="msg-677177">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGNuZKP13IH3ejSPj8hSGZFfoxM2QEfh2cV2lNayUxJJKVsaOTGN_WnyyckRt4coJeD7IIRq5ckTftebR7Mvr-hynIKiKDnfaAi_O6IIjOfbtIcaNMYjPWmctMGWK5Sd7tTRn6mx90oXoJ9x0yj9x71rERy7UU7HKeZmHwI7BoifqQjetFGLd2M1ZC5zxt5NtqvnjjzFr8M6djPzmrAKPeIeeQB_98mcqBpZ46P_UQ9irR75WNgXA6ZRUnb1C2RTej9jwHcCaEe_p49Tk_jrjkro8jZYbUj3KSLMfCgDfGo8ycWsblOEHo_HgGH9HZOWRuemJZebpeiEeHc2HffCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: گسترش جنگ، فشار اقتصادی و سیاسی بر ترامپ را افزایش می‌دهد
روزنامه «ایندیپندنت»:
🔹
جنگ برنامه‌ریزی‌نشده ترامپ علیه ایران، برخلاف وعده‌ها، به درگیری فرسایشی تبدیل شده و اهداف آمریکا را محقق نکرده است.
🔹
ایران توان موشکی و پهپادی خود را حفظ کرده و حملات در دریای سرخ، عراق و مناطق دیگر، امنیت پایگاه‌های آمریکا و انتقال نفت و گاز جهانی را تهدید می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/akhbarefori/677177" target="_blank">📅 08:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677176">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
آسوشیتدپرس: میزان رضایت از  ترامپ در مدیریت بحران ایران به سطح کم‌سابقه ۲۸ درصد کاهش یافته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/677176" target="_blank">📅 08:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677175">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22170fd624.mp4?token=fkY6-Uoe6yK-oENwdwEqGMTPySKS_EMlZ3YL1UGYAJ1p-egZ5fN0xua4z2WFoYmai79JU6_EqPs7j9SDZOv94CIM7RDy6LDTvMWupQGln_Ib2BdfwLPwJqRwFZ138JYFKBgJ7MdPNL93vSQdy49dJ6HsghabWio_YXUDxbJ0P2-aZA_AyR8jUMeA4Dk09Cc83fr36yzq6E2QmUc-pKX22nR22WIMBvrwtt4ujDKZkoZblVhMQbb5E7gxIEc1koqsKNc2h4ESV4DBqBjfwZX77AULS2MBfeb-t_X8aCPK11N9ghLE4d-JZz-iI1aRZjaAk9PhJkobbqigrC8dVzT7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22170fd624.mp4?token=fkY6-Uoe6yK-oENwdwEqGMTPySKS_EMlZ3YL1UGYAJ1p-egZ5fN0xua4z2WFoYmai79JU6_EqPs7j9SDZOv94CIM7RDy6LDTvMWupQGln_Ib2BdfwLPwJqRwFZ138JYFKBgJ7MdPNL93vSQdy49dJ6HsghabWio_YXUDxbJ0P2-aZA_AyR8jUMeA4Dk09Cc83fr36yzq6E2QmUc-pKX22nR22WIMBvrwtt4ujDKZkoZblVhMQbb5E7gxIEc1koqsKNc2h4ESV4DBqBjfwZX77AULS2MBfeb-t_X8aCPK11N9ghLE4d-JZz-iI1aRZjaAk9PhJkobbqigrC8dVzT7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از کمال شرف درباره صلح آمریکایی ـ اسرائیلی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/akhbarefori/677175" target="_blank">📅 08:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677174">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اوکراین: حمله موشکی بامداد امروز روسیه به کی‌یف، ۹ کشته و ۲۳ زخمی بر جای گذاشت/ انتخاب
🔹
لتونی مرز خود با بلاروس را بست.
🔹
شورای روابط خارجی: چین برای نخستین‌بار در دو دهه از آمریکا در محبوبیت جهانی پیشی گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/677174" target="_blank">📅 08:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677173">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f919a67bb.mp4?token=mZK22nmpB-VrF8Rs9fMMwwPVjaoWT4BhWAcF8YwSFZhKS9ANxOq0DkWUyx4m6QFW0tR8rFRhpi1CRokvm5Ws0uC3Kmf3Zqf-FbPeg0znUfWO1IYtSj_TteMf7TtYi1LypTGCFOq01wxhkfa3HQk0tv-BYS9lp2C41LSsc0yW9bPZvOjESM1H2M0lOlN310JWmSNx1IUUV0itlX41yEOPbteHm3M2w3t9TCRDPyen4OlwPej2ZbiymBVXI2t_iRX_Ihb0Gp3ZHtK05Kl7hesmrjqhe6ZtQxINITgbXGWN-jtC-mij_uxccv__QcGemBqV5dIUmx8rCCdolGUuZ--gAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f919a67bb.mp4?token=mZK22nmpB-VrF8Rs9fMMwwPVjaoWT4BhWAcF8YwSFZhKS9ANxOq0DkWUyx4m6QFW0tR8rFRhpi1CRokvm5Ws0uC3Kmf3Zqf-FbPeg0znUfWO1IYtSj_TteMf7TtYi1LypTGCFOq01wxhkfa3HQk0tv-BYS9lp2C41LSsc0yW9bPZvOjESM1H2M0lOlN310JWmSNx1IUUV0itlX41yEOPbteHm3M2w3t9TCRDPyen4OlwPej2ZbiymBVXI2t_iRX_Ihb0Gp3ZHtK05Kl7hesmrjqhe6ZtQxINITgbXGWN-jtC-mij_uxccv__QcGemBqV5dIUmx8rCCdolGUuZ--gAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زمین‌لرزه ۴.۷ ریشتری جنوب ایتالیا خسارات جدی وارد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/677173" target="_blank">📅 08:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677172">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svx93fFatieukhE4-aZqDF9mjV4hir0a--CeQi3_aWwA1V6STjz6NzceUAZ4ndh9sGL5_yPC1u_lFsp33IMaVJ3u5fl8z07ECdF3PUpDcxfm3VDQ3RBhoBUQ30zEHzzFyYMEuoPogMo2neJXy8nePlhUay1PrrOQq3HZw65xur45E4S0AnF6y4RflF_xyU40rv5qGkwXZ2JtuBgLkqFSYBR272lu2wu7d1dBB6Xee1gNJcuEgTI5miGWjLw8Rtu_gbTJPLTLeFYKqUYxqR9dA2sVTOfvvNPE_GpoMza9K8h4jqQaGpTL6PX5S8tY5vb5pESJgO8NPSr4lua-HlFiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرفروش‌ترین خودروهای تمام دوران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/677172" target="_blank">📅 08:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677171">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoizkShXTPoEFHnaB40dFilj83MACxVJmKYUF3d_UAgzfSGpFmpBXKjT7pxUMqn9pyzPtOzJ7hWcCpi2Bk_CKKgJx5NNyiREj8_WEaUik27sACVrAcKCb3pYSRq7Vn30iHaGvvf9zRCMOo5NSkQUB5lLXSgExD4ATqVdVc3MiklyjOUk3-82UUDqiQKek1k7uz7aygomtUTuVZPzQ0f_4Tz6XWISBecKACzNCcC3uvsDtCx2nW0skt__-9ynDQ-CONTgMEkvxTijLtOcIhbFaGUUHQ7FbF7ClOSwJPhcvOTyQ1VVWk1wgRlsY3XLYeoGY8Kykwzw9D1-n4VhfIv8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ زرد در تروث‌سوشال: آنچه که در اسپانیا اتفاق می‌افتد، با ده‌ها هزار مهاجر غیرقانونی که به آن حمله کرده‌اند، در ایالات متحده در دوران دولت خواب‌آلود جو بایدن اتفاق افتاد، و اگر دموکرات‌ها دوباره به قدرت برسند، دوباره اتفاق خواهد افتاد، حتی بدتر.نگذارید کشورمان نابود شود. به جمهوری‌خواهان رأی دهید و به ایالات متحده افتخار کنید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/677171" target="_blank">📅 08:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677170">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdHNVgsXqbp3yr99Trk72CA-RdqrKmZQKTjGUEyg19agVQ6BG0ouN2LXlf6ZF6SOp1UGgGeh88363e3nH2ClEyBpE1d_Y9K_64MeXp9GmCb_jgHTsMqDptCrGCK4ULoWmjeHOV-PKVS5S4KiE-mJ0HDtkX0o2seLMzd8XOpM3HTkGvF_G9GB8Q5e7LdYFjZCqZHmnWgV1mtDcBGEOKUPzqPxekFvXyHMnfoceDrpMenQyplDzZgzvOC7CXMNqnhE8figeFU23UfiIoVThpfpO2oRGYzVWQkRlOzqH6tXwycjpMbrawSTAQ9q0_yEKlhFtV3DcNcGyF-swcttoaWK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قند رایج در مواد غذایی می‌تواند به پخش سلول‌های سرطانی کمک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/677170" target="_blank">📅 08:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677169">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4862af396f.mp4?token=BzlR9-yQNhn_MwHS-5H5Ffo2oKqLTfyJ-fMx8QiP35cZC-LQ3klJGJofQDjznr_puyzdH3KQNUCJqV5mPRFba4ilNiO6RVNLEIAg8mkeLnK1qeL8BTLcWu5F6OazD_22vOK7uwbSTJH1TxJZnJMz1N2MXwUevZbNJasD7_URByKPXyu5r1t_Ew5wElOzJs4LUgp2fFCVDvTtlKbLpSyrK6mTfh59c7_zoOUCzQl6V1afiJEWhkhrPPILvf0w6vQbaHUMJ6GVXrssddbhtEs8xPtV6tZfcGrGOCZBrHX99mTDM55UsWpuw31YV5L7rYue4n8rpDKDhgzFbxEAjfYBug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4862af396f.mp4?token=BzlR9-yQNhn_MwHS-5H5Ffo2oKqLTfyJ-fMx8QiP35cZC-LQ3klJGJofQDjznr_puyzdH3KQNUCJqV5mPRFba4ilNiO6RVNLEIAg8mkeLnK1qeL8BTLcWu5F6OazD_22vOK7uwbSTJH1TxJZnJMz1N2MXwUevZbNJasD7_URByKPXyu5r1t_Ew5wElOzJs4LUgp2fFCVDvTtlKbLpSyrK6mTfh59c7_zoOUCzQl6V1afiJEWhkhrPPILvf0w6vQbaHUMJ6GVXrssddbhtEs8xPtV6tZfcGrGOCZBrHX99mTDM55UsWpuw31YV5L7rYue4n8rpDKDhgzFbxEAjfYBug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر زانو درد، درد هنگام راه رفتن یا احساس ضعف در مفصل زانو دارید این ویدئو رو حتما ببینید #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/677169" target="_blank">📅 08:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677168">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رسانه‌ آمریکایی سی‌بی‌اس در مورد حمله به زیرساخت‌های ایران
🔹
رسانه‌ آمریکایی سی‌بی‌اس در ادعایی عنوان کرد آمریکا و اسراییل با فرا رسیدن پایان هفته میلادی برای بمباران زیرساخت‌های ایران از جمله نیروگاه‌های برق و پالایشگاه‌ها آماده می‌شوند.  بیشتر بخوانید
👇
…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/677168" target="_blank">📅 07:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677167">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10622cd675.mp4?token=djSfikl_BlHzJvn3dUiqiuvL_KUqaoaeA8x2jgn5UeyVn3LVnG-iZpkzNtPyPL_f9NV1zfA6r3Qxf6B9tQ--XaVevuQeVicyRgJTCpo6cxtQYKcVGoctluMMTSP7SF3Y730Minc4bqkAsywitK5rz9t85xKDIgIHOORXc9dwbHPKL1p35KgoTULBKpFob7UWpgwISuA73sdN6KkxKJ1w2oCTw1lzxxGMUERaF-6pZ5LVPzzuLmV3dBGSLzgx_yxg1yYH4LaspXRgQ9U1PnXB83XN4C7UpWhlUjZFRNmmJNYa0YeNPsl4Bprw_f-wD4TsZ1af-jQWjFUjq1PQnxprZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10622cd675.mp4?token=djSfikl_BlHzJvn3dUiqiuvL_KUqaoaeA8x2jgn5UeyVn3LVnG-iZpkzNtPyPL_f9NV1zfA6r3Qxf6B9tQ--XaVevuQeVicyRgJTCpo6cxtQYKcVGoctluMMTSP7SF3Y730Minc4bqkAsywitK5rz9t85xKDIgIHOORXc9dwbHPKL1p35KgoTULBKpFob7UWpgwISuA73sdN6KkxKJ1w2oCTw1lzxxGMUERaF-6pZ5LVPzzuLmV3dBGSLzgx_yxg1yYH4LaspXRgQ9U1PnXB83XN4C7UpWhlUjZFRNmmJNYa0YeNPsl4Bprw_f-wD4TsZ1af-jQWjFUjq1PQnxprZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو: جنگ آمریکا و چین فاجعه‌بار خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/677167" target="_blank">📅 07:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677166">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btn6_va2XBVxqPlopWXWNMHFgkR7hMVc8Euro2bXFHJ4DjOe9mXQ0B1QjxWPSC_HBAmk49uLh3R1Ah3O_Cj9yTYOxG76WpFNaR5RlRR7iwHkRyACzXNz4JXg7Qv1JOP6behwhZNZO4juDXBfNAkuJ4do0oXu7NbxdpVU70ADhIJWqtDGqrWGw9snA-DOmX9l0eRMlpqJH3cPnlWxZqU3emIShy3fW0McJXwcfBoKUp1pQnX01nknKXsTAx9TYU1wu_wATQSlwt1crA0PNl_J6nWb0zwngDfZMC8hLEEXuTXanISkUhRN4X2DV7NI44o50iVH7-s7oz8DFcBKgd7iiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۱۰ مرداد ماه
۱۷ صفر ‌۱۴۴۸
۱ آگوست ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/677166" target="_blank">📅 07:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677164">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس فیفا در بیانیه ای رسمی از طرح خصوصی سازی جام جهانی فوتبال عقب‌نشینی کرد.
🔹
سی‌ان‌ان: هیچ نشانه‌ای وجود ندارد که اسرائیل در موج جدید حملات آمریکا علیه ایران مشارکت خواهد کرد.
🔹
العربیه: نیروهای آمریکایی خروج تدریجی از کردستان عراق را آغاز کردند.
🔹
امروز آخرین مهلت اعتراض داوطلبان آزمون ارتقاء دستیاران تخصصی پزشکی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/677164" target="_blank">📅 07:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677163">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31504b214d.mp4?token=kn6mgeBMo3eFS6xr7-_3ECURSszYCnmKWICKQ7-GGB2gjxfcgNE3yLYrQyLia31lb7QqUTGdpofGmuy0nXJjeByNMW0xHqrcBhU-OO8Pndrszm1bMKpY6fw3jGLor8ewNE2Ied50CTosAE6leS2Xey2aFaxDms6Qb4Sn3l6-WMbTsrvNBajBbGN-cPTOpSOSIA8wn6zsGojGf_UbIGHo9qj6mOOB5Tw9-p5F2wgGnTYgEGmOVxiT0zmQ7CAtR22qncJDTmRx-Mkrr0N7lyRrsKsX2ev7O19v2-oJUlPsnTZBPv75r0iE8ZrJdqitLmEYe0uo0YnSJduncb73mHHLZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31504b214d.mp4?token=kn6mgeBMo3eFS6xr7-_3ECURSszYCnmKWICKQ7-GGB2gjxfcgNE3yLYrQyLia31lb7QqUTGdpofGmuy0nXJjeByNMW0xHqrcBhU-OO8Pndrszm1bMKpY6fw3jGLor8ewNE2Ied50CTosAE6leS2Xey2aFaxDms6Qb4Sn3l6-WMbTsrvNBajBbGN-cPTOpSOSIA8wn6zsGojGf_UbIGHo9qj6mOOB5Tw9-p5F2wgGnTYgEGmOVxiT0zmQ7CAtR22qncJDTmRx-Mkrr0N7lyRrsKsX2ev7O19v2-oJUlPsnTZBPv75r0iE8ZrJdqitLmEYe0uo0YnSJduncb73mHHLZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقی‌ها هم در حمایت از ایران، پرچم خونخواهی امام شهید را به دست گرفتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/677163" target="_blank">📅 06:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
حادثۀ دریایی در دریای عمان
مرکز عملیات تجارت دریایی انگلیس:
🔹
در پی اصابت یک پرتابه به یک نفتکش در نزدیکی سواحل عمان، موتورخانه این شناور دچار آسیب شد و کنترل خود را از دست داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/677161" target="_blank">📅 06:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd91ee725.mp4?token=bvrET8X5jKdhL_Y9WuXPnXNz-xB5BolPBfoxbtKMj4dr4uj_8jn2azKdv56UoH11KxJ05ue7jDkiRZTCjxH9HV6uQwchvsttEbJqF-AwJKz0yoJ8xAzCgjqoJrCTnxJWAw9sq14ipRwsfsq74O1PhMSQxwJMyIeZmxyZX1iyopYzwuYXGVPNO_E3fYNB6XC2X35Arm5IEAFpFJTStHkpN8YnqDbOYz9dBWMJJbTnIDbSUrJPMNePmJWAXi5DWXLMF6XA7gtp58NZPLLYeJGt1vc1qO5f8lodwfUrcR4IZ2sGviILtuzZ2avaOBUlcscblAvC8He4qhf9xIoadJwUel5x2uj0aCZpldguNK7Uvjp13OAI09_6Vk7_ZFGcU2DBWQD57vztAM2Dz8Nxk96ZDDvX7ZoS5VCo-7--O3arzeVFEX6zYgVvmLWm8WnuM9ciAeIPURby7EIBbFusnneh2F9BCuvcmVq3UC2V3Qc852py_a1-44vS0xPbiepU2Kytb4fbsls8Vc3GpE77g5X8pLAswijzQn00sqZGO91zXVMZRmekpWdvZ9uxDxIQLgA6r_s_VnfIq3qquflDUtY7dGUEAMkJr3SbOYqYx4oQl4S3o1f7vHzvDuwI0_UEraj-wrUikADdrnwsL11peiZ2xI9U8rVoEk1zpYytebjVNos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd91ee725.mp4?token=bvrET8X5jKdhL_Y9WuXPnXNz-xB5BolPBfoxbtKMj4dr4uj_8jn2azKdv56UoH11KxJ05ue7jDkiRZTCjxH9HV6uQwchvsttEbJqF-AwJKz0yoJ8xAzCgjqoJrCTnxJWAw9sq14ipRwsfsq74O1PhMSQxwJMyIeZmxyZX1iyopYzwuYXGVPNO_E3fYNB6XC2X35Arm5IEAFpFJTStHkpN8YnqDbOYz9dBWMJJbTnIDbSUrJPMNePmJWAXi5DWXLMF6XA7gtp58NZPLLYeJGt1vc1qO5f8lodwfUrcR4IZ2sGviILtuzZ2avaOBUlcscblAvC8He4qhf9xIoadJwUel5x2uj0aCZpldguNK7Uvjp13OAI09_6Vk7_ZFGcU2DBWQD57vztAM2Dz8Nxk96ZDDvX7ZoS5VCo-7--O3arzeVFEX6zYgVvmLWm8WnuM9ciAeIPURby7EIBbFusnneh2F9BCuvcmVq3UC2V3Qc852py_a1-44vS0xPbiepU2Kytb4fbsls8Vc3GpE77g5X8pLAswijzQn00sqZGO91zXVMZRmekpWdvZ9uxDxIQLgA6r_s_VnfIq3qquflDUtY7dGUEAMkJr3SbOYqYx4oQl4S3o1f7vHzvDuwI0_UEraj-wrUikADdrnwsL11peiZ2xI9U8rVoEk1zpYytebjVNos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع پیکرهای شهدای «تیپ ۳۰» الحشد الشعبی در نینوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/677160" target="_blank">📅 05:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cf6df173.mp4?token=XzcLByAbRNmqACsZbiPZsjhdBibAJ8jxsyDLqSAaapg_5kg_TDUDNxVqSplJb0yHugu0eZFwGPjS4Iw4wTNP0oJyrtT_pirMPdszERBD4gWsDioUvsSoypj8CF4p1bNTI9k1AalN6JzEO_6K9MUPGxoxNrIciXwGDyUM5O0Khz_HKlhYmLHZnQqfO7qSeTQxGbZuWV32VUe3iUblRnEd5bAdD9BdfoLjFr6rgTEcAboFkah4BugsAOF3m8Kfum91s5H2qyCnWBeNfNq1LkBiHaBieX3SMUUm1UUIDoCh1NHYNP6i1VescqKMOlVTN1oVVL8ADGzCNOnV8eIglhw8Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cf6df173.mp4?token=XzcLByAbRNmqACsZbiPZsjhdBibAJ8jxsyDLqSAaapg_5kg_TDUDNxVqSplJb0yHugu0eZFwGPjS4Iw4wTNP0oJyrtT_pirMPdszERBD4gWsDioUvsSoypj8CF4p1bNTI9k1AalN6JzEO_6K9MUPGxoxNrIciXwGDyUM5O0Khz_HKlhYmLHZnQqfO7qSeTQxGbZuWV32VUe3iUblRnEd5bAdD9BdfoLjFr6rgTEcAboFkah4BugsAOF3m8Kfum91s5H2qyCnWBeNfNq1LkBiHaBieX3SMUUm1UUIDoCh1NHYNP6i1VescqKMOlVTN1oVVL8ADGzCNOnV8eIglhw8Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: تنگه هرمز متعلق به ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/677159" target="_blank">📅 05:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhvAzdP2X6uoHXOIkx9VHF31cjJ16fJd7_7dl5gKWWFaOcgNJtUa_ev1Gz9chzzusvQzPsWLrCg6aVe_aP_No0v-HzavWNiyiGlW8iI-O7tNeXb6qfzsnFKgtAvRdumrk2dccfKnXge8QlOnWD8tCDwbpqmsmCf7wYMcTmu4-Ho3rPtzEZVUouAyHFohQ8KawO0i0gajLJNYE1HJycE2vnVHTxf2YkbjYWTF7SLWGtO3KFQ94rbN9PQ7S-FfGJu5hQgIhkO6KcuiGVK0umaJtQ8aC2AKAsqAOeViDtqfSymUv3L3-yf2v373vcMm1Ev_3dnJV2S94pSKe0TcBd0aWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxaRLRKwoSib8zuNT2tedT9Db28ETEIuq1oA5McnzEhxqJHd8rA2bFP4Yhpqr3LqzuaI-kcT7PYB7TJQc1yQv8PyIvq45y2j0prCvwrqGXzb0FB-NguEH5vucFJa9xoL6hjLYTRPKSfTD0ehFdJkoLlgqGhkIiDiyFCHd4WUrzlqx3j3smabjdyV6-DTEyc8kQUdcagkxzlq8Huwk1OmARCHbqpFV9Kgdvx8IwhkzQS_Ha1nsI6DP6cYaxYU1eUvEc55a21I3uS_3egYmE8FpbxlMS1fwKmdccwE2OYJ8nZr8gJnhzJUEqVbn5sbPWA4qoga5vCyOOIi4n7u0vBDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRmi0GFapgA5CKW4aFggDhfsoZaw3ry2IdCYfTrdEEMV20JnfeoP_rWI7KG1q2llbyv9VUSCIGf4l959F6Y8fKJYzjFET6MOpQmFX4t3ODsACLGN6SVpReMT_1su_AwFyEdjZHgjZU20w4ceUbMvPGGkvutZTxzWiJ5iNtnhFfwCxvj8HVRiYFhDcDKfAxEYltXOOXhNC2cIcJ7EDykjaloQF9Q9LMz-EcIEq_ClWKLwUqgbDpLrnOZaDoeZAFi9CMxPUvXuhn2AhDXKDUJW1H1iyA7mg_ZWCde9BCV_ai-iFAgAqhJ5APM7ir9WtDAi-fDnQvym4zA8EcNa1pu50g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش سی‌ان‌ان از جلسات پرتنش و عصبانیت ترامپ درباره ایران
🔹
شبکه سی‌ان‌ان در گزارشی از خشم وناامیدی ترامپ درباره تحولات مربوط به جنگ با ایران خبر داد و نوشت، این موضوع به برگزاری نشست‌های پرتنش پشت درهای بسته و تماس‌های تلفنی همراه با الفاظ تند با متحدانش منجر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/677156" target="_blank">📅 05:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677151">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia4HfAFIHeh0Wct3ga5-ZiJd0srxhrxkO5_S_I-MRkGNtLH7xuZCcUDo9klPLMDUGf4S4T5Usoygkeg_K26BNiw_BPFsClggC3VmnRIOR8i9bQL7x1lQzA2W2bXNkFKbwb2U7x3VtzomT42y_wkmNKDMksAOSBX7vbutWKTd-mQq6MTq7pgA7t_ly7N7J1Ap5B98XbY13iEQ2iBZJXfL_FEJDEccikTJuH9xIAzSYL-MdAqDmwg_xpJ4-2F8quqBAVb_sB7xyclo2uoX8dpnRRzBl64Mvq7chL12mCzLkTAxV_-ayI-d7-4q5USchH4RvA6oz3mIO-SH1ZE4fQ0Cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تخریب گسترده زیرساخت‌ها در جنوب لبنان توسط نظامیان صهیونیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/677151" target="_blank">📅 04:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677150">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
رسانه‌های صهیونیستی از وقوع یک حادثۀ امنیتی برای ارتش این رژیم خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/677150" target="_blank">📅 04:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677149">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مرکز هماهنگی عملیات‌های بشردوستانه (HOCC) در صنعا: اخبار منتشر شده درباره تصمیم یمن برای تعیین و دریافت عوارض عبور از کشتی‌ها در تنگه باب‌المندب صحت ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/677149" target="_blank">📅 03:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677148">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85be2ef3d0.mp4?token=OfLrKoN0yV48dJPl2N2qjyVPVMb55CRW8AAqZkf-NIjLEQLgmrr6fMCsYfAcaEaKEesgzhw46HLv9KzQBLWRCNuFSDhlL9U0LZi7ijyIcuxUL1pzNUaM_rItGyJrrHA-Ui4j5PlNN1Z8vAEG6-C83dDp_ykBegi-WTPhj6qDZVVlNEpckyvuhga3rG3l6bOPlclTZ4QVF8tah8v-pQSfyuLnxcUFLEFQcQoqiTW7WXD7RN99wxLBLj4p3PVwYFwNFcI_T-k8-lG2ABzbdoRpitGYts5ZAteDc0FYbtPx-eNNH8DK5ZfvNM8bHonLC051b3AGFxIseyIT6j5Y61I7uz58FZHxSXJ44ldJ6QaBSl8Zl5Tia_1YL4bm8q_P2MtElSIGX3FHBBpyfxbWGgc6nSvya_dyPhC6rTLsFcuqIcaDvuEzPxHOVHPNU0plwAeEppNXMy-NcMQJiOvaC3GKqj7wAG97dZbQC97bZ8qmCMAbQhwiUozQyWXkQmAQvEHsKNDywFtBYEfFhq_JrbFvwdoR1AUxGHc6RabtALy6rz2bKwbMOHKrFwILEijCbIL0po_ZZ3sRjxSHbczh5QO7UJ815mOgYFIIucpWcoaLUo7GgayKh3eYsh86cDh3VzLcBkvJpg63kPvr9BLpLkUdLpTJgYrH520hr10OBNoGb0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85be2ef3d0.mp4?token=OfLrKoN0yV48dJPl2N2qjyVPVMb55CRW8AAqZkf-NIjLEQLgmrr6fMCsYfAcaEaKEesgzhw46HLv9KzQBLWRCNuFSDhlL9U0LZi7ijyIcuxUL1pzNUaM_rItGyJrrHA-Ui4j5PlNN1Z8vAEG6-C83dDp_ykBegi-WTPhj6qDZVVlNEpckyvuhga3rG3l6bOPlclTZ4QVF8tah8v-pQSfyuLnxcUFLEFQcQoqiTW7WXD7RN99wxLBLj4p3PVwYFwNFcI_T-k8-lG2ABzbdoRpitGYts5ZAteDc0FYbtPx-eNNH8DK5ZfvNM8bHonLC051b3AGFxIseyIT6j5Y61I7uz58FZHxSXJ44ldJ6QaBSl8Zl5Tia_1YL4bm8q_P2MtElSIGX3FHBBpyfxbWGgc6nSvya_dyPhC6rTLsFcuqIcaDvuEzPxHOVHPNU0plwAeEppNXMy-NcMQJiOvaC3GKqj7wAG97dZbQC97bZ8qmCMAbQhwiUozQyWXkQmAQvEHsKNDywFtBYEfFhq_JrbFvwdoR1AUxGHc6RabtALy6rz2bKwbMOHKrFwILEijCbIL0po_ZZ3sRjxSHbczh5QO7UJ815mOgYFIIucpWcoaLUo7GgayKh3eYsh86cDh3VzLcBkvJpg63kPvr9BLpLkUdLpTJgYrH520hr10OBNoGb0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله صهیونیست‌ها به انبار دارو بیمارستان شهدای الاقصی در دیرالبلح
🔹
گزارش‌های اولیه حاکی است که در حمله رژیم صهیونیستی انبار دارو و تجهیزات پزشکی متعلق به بیمارستان شهدای الاقصی در دیرالبلح هدف حمله قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/677148" target="_blank">📅 03:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677147">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1749506c74.mp4?token=F1yRj6nX3JhmAhAXbPLGv5kEgjjKdRjbWUwdSI5k9Rd5bg35NPRByvSewWpx-v_rEuQuQ5ic2JcIX9GqF6HgPpfFZoxh8LWoK_sJL_by6iqo1cZSYXeLCFKn47aPXR9LPg7bgJfywZZeORpUfay2Q3Z6oqYGtqbmYc78s7Es-MbkA-nWllhJ8l06Y2PNXtZCgmy2ywa2NQOiQ_UOrM070EuJn8ZafIn--T3ca7X35O8Ombi_VjexPCXrvuFpcX_qHJGO3fzHyerGabNWb0p4GYOKCYPAPrqW887_oKCkrkCKr3qYfE-Ln41K-42G8wvEPtfqdePQ6nk-djeQHKRWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1749506c74.mp4?token=F1yRj6nX3JhmAhAXbPLGv5kEgjjKdRjbWUwdSI5k9Rd5bg35NPRByvSewWpx-v_rEuQuQ5ic2JcIX9GqF6HgPpfFZoxh8LWoK_sJL_by6iqo1cZSYXeLCFKn47aPXR9LPg7bgJfywZZeORpUfay2Q3Z6oqYGtqbmYc78s7Es-MbkA-nWllhJ8l06Y2PNXtZCgmy2ywa2NQOiQ_UOrM070EuJn8ZafIn--T3ca7X35O8Ombi_VjexPCXrvuFpcX_qHJGO3fzHyerGabNWb0p4GYOKCYPAPrqW887_oKCkrkCKr3qYfE-Ln41K-42G8wvEPtfqdePQ6nk-djeQHKRWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از موکب‌داران عراقی با انتشار کلیپی نوشت: این تصویر آقای علی لاریجانی در منطقه شط ‌الله (منطقه‌ای روستایی تابع طویریج) هنگام عبور او در زیارت اربعین و در میان عراقی‌های ساده و معمولی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/677147" target="_blank">📅 03:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677146">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b623cfa5e7.mp4?token=OdE7JpfMw-KPoNt7IOz4t_zghUKr99GJtLia83O_bQw9DnPmz0bf2Lp7hjay7Xpaif5aqfcwyqHaizMf3oiTIcekDpfCI2LOLg2F6heDOZ3HFvvCCHxpJ_h7RSvY68E5y_X-d40K74H1upN-jPCadPdTauzT2tOl-qQsFfrr2S8FkhPOcMKlsnuF7nnUMixajwVkpPLR0YOmCLqaXFUaxOSL5WHpfUNy8wpwOT264RhzuwcPwAqJWZHdvyvGFRXaUvLpx3SMS_8P6181F3YXC30-xAAinsarHbQqTzjWfpkUOHO9_Ry8d2osnEEbOrXyqjYnfg_COp-zsfCV5IOAWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b623cfa5e7.mp4?token=OdE7JpfMw-KPoNt7IOz4t_zghUKr99GJtLia83O_bQw9DnPmz0bf2Lp7hjay7Xpaif5aqfcwyqHaizMf3oiTIcekDpfCI2LOLg2F6heDOZ3HFvvCCHxpJ_h7RSvY68E5y_X-d40K74H1upN-jPCadPdTauzT2tOl-qQsFfrr2S8FkhPOcMKlsnuF7nnUMixajwVkpPLR0YOmCLqaXFUaxOSL5WHpfUNy8wpwOT264RhzuwcPwAqJWZHdvyvGFRXaUvLpx3SMS_8P6181F3YXC30-xAAinsarHbQqTzjWfpkUOHO9_Ry8d2osnEEbOrXyqjYnfg_COp-zsfCV5IOAWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات موشکی به اوکراین، آسمان کی‌یف را مثل روز روشن کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/677146" target="_blank">📅 03:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677145">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
هشدار عراقچی به انگلیس درباره همکاری با متجاوزان
🔹
عراقچی در گفت‌وگوی تلفنی با وزیر خارجه انگلیس، هرگونه همکاری با متجاوزان یا استفاده آنان از قلمرو و امکانات کشورها برای حمله به ایران را غیرقابل‌قبول و مشمول حق دفاع مشروع دانست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/677145" target="_blank">📅 02:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677144">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/677144" target="_blank">📅 02:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677143">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
تیراندازی قایق‌های جنگی رژیم صهیونیستی به سواحل رفح
🔹
منابع محلی فلسطینی گزارش دادند قایق‌های جنگی ارتش رژیم صهیونیستی در بحبوحه‌ی تداوم تجاوزات، به سوی سواحل شهر رفح در جنوب غزه آتش گشودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/677143" target="_blank">📅 02:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677142">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neNY5hMrMCh_qDc8WX58ZA2_NWXUieTwbDu5CHZ75J7fn-7-3wK9it_AbPw5OL3mREBZq-Qilp6A6Ub2fIOrzllQcIKGmHAvLYv3eI1LJSMMbsZnSEMghPQMaGEWTDHRLHQ6eUNQQy5Su5K69ti-Jlz5YvhEnrJPNaWgTmJC8bn1BQdcvoGbUt12GhVVSHeCFBwfOnXhb_v5ptEinteT_lU9lkYL1EhbZO5FZuZL2rPpkbCTpa-92S4p2vL7ZZSdV8u31XwamlzLKTcRf1UUghjeRPgetO7lMdhF2_fLMIZORiQZfty7n1s-JZejbWreQev5_S5rpiUvY-17igCgBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عربستان سعودی رسما تشکیل ائتلاف بین‌المللی برای حفاظت از تردد کشتی‌ها در دریای سرخ را با حضور ۱۴ کشور اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/677142" target="_blank">📅 02:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677141">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
نگرانی ترامپ از حملات تلافی‌جویانۀ ایران به زیرساخت‌های انرژی منطقه
سی‌ان‌ان:
🔹
آمریکا به‌دلیل نگرانی از حملات تلافی‌جویانه ایران علیه زیرساخت‌های انرژی منطقه و تأثیر آن بر بازار نفت، هنوز تصمیم نهایی برای حمله به تأسیسات انرژی ایران نگرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/677141" target="_blank">📅 02:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677140">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
یک مقام ارشد امنیتی: برنامه گسترده‌ای برای پاسخ به دیوانگی احتمالی آمریکا آماده کرده‌ایم
یک مقام ارشد امنیتی:
🔹
ادعاهای رسانه‌های آمریکایی در مورد حملات احتمالی امریکا و رژیم به زیرساخت‌های ایران را نوعی دیوانگی قلمداد می کنیم. چون ما برنامه گسترده‌ای برای پاسخ اماده کرده‌ایم که شامل زیرساخت‌های حیاتی رژیم صهیونی و زیرساخت‌های انرژی آمریکا در منطقه است و برای آن اماده‌ایم.
🔹
نیروهای مسلح ایران، چه در جنگ ۴۰ روزه و چه در تداوم آن در هفته‌های اخیر نشان داده‌اند که هم توان انجام چنین کاری را دارند و هم اراده آن‌ را./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/677140" target="_blank">📅 01:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677139">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از یک مقام آمریکایی: ترامپ در حال بررسی آغاز حملات علیه اهداف انرژی در ایران طی روزهای آینده است، اما هنوز دستور نهایی برای انجام آن را صادر نکرده است/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/677139" target="_blank">📅 01:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677138">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
نورالدین الدغیر خبرنگار الجزیره در تهران: در میان افزایش لحن تهدیدآمیز واشنگتن علیه ایران و بسته شدن تنگه هرمز توسط تهران،
نشانه‌هایی وجود دارد که حاکی از آن است که مذاکرات مربوط به تنگه (هرمز) دست‌کم در شرایط فعلی، برای رسیدن به نتیجه نهایی با دشواری مواجه شده است
/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/677138" target="_blank">📅 01:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N_xo1A2-JzfhroSFlLZ2a84XBWUEY7i-NLC3KxDVR9yjNfBDIudgSt670rqhOBEdGa7aZSO3Gl8tnr7uDR710R7kNJ_ykP0FqNcH21J2_uZQvhsj-eNDSeo-I7tKiYNEVyTlpvqOnJeu8uau-PgBs-3OdMGirbQbWAZEYphIrqFuA26x524S2xn8X4W0sVJpTXF4IzMvzWPo-AbL_77m1vqUEniNC-tuiPMgy41324SXr4XxSFY7Iy9eaEyAe-38bqQ9TH7ReGd_-nyAZaAEjf2W-FvU2NyQbb4ViIFCqncTTq8GVzTZ_uydp7A3s02EAIEb9g-Si-_p1aZi4tPnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUbG2zJ5rNoiI4mB3MKiyiGfqy-sj7mUp4xvm_7HlhKIgrHzvbv9uEIP1LTT6u6vTtrm0jn1owTUUdasvDCDkSKbTuxm4KLqhYkmeiP0TjnnRZuV5yw2S82DUunYvXBPIipo61Qe6IfVsbnz1MgiRDEHT1mIeY5MZUR_r5T3uVJg8JPAU1ag9LeFFRuw-fifQ5XCmvuoOwVvao6YfRB75_XRdcHFkzniKvvFLRu06ASkY3Tm2K0cEJU-tdq_COYwokpaDSDTH7nl9EnrMDI047Raf-sLi_yiZD2sPw2TShxx6P-7d-P90l1RNZwVEbShCCR3VpEifuPqr-XBD2pkYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1p77JLFa-khSLUAmktEx9wJHSQUZJi2R_wz-vbELu_lb4ojhTE9L_XiyFxJ-gUqgaOBp2aQO5U7opzGIBY7YY68Yr6dWQGDwsGOMUBmycZfYmX78_cgL63JyPJShkNM8CEYwQ0PTq1UPsaCrZ7Cr9U6O7UX1w3LNY-KvXUfAR8EURS8wG2qBjOfK3QKD0qUTWAtib93o_Ucz7NfYYN_E03RgoHpudt3oIFipxdMOUOSzHWAskzN7iOxN1DvnaNGIqBBvm5-yG-McyAdObfwEBdvJUqP-efRPDa_FRGBmKfg4V2tqsBqdXC0cfLYiEZVw9ZROKTgOIs6y32IBOPC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUKY7zo-vT1pcSJBdsNwjqX7MsCePWxdnpCyVA9-SXR9GvjZQZE3ofaXoeuxYbEsGSFYNocIGrlwo8pMg0GgspJSk44-XlYReYuAoQvWsIz4JAAMa8drMcIqPWFTtCjWwkQDIi7MWozXyp6EbcClsjowcong9_Gg-s-5ctT-780p1195z0xBK6mwGMNhwRMPyQYhwda4PWiBDvx8fJJqm3FoEmAppwfCNUzZh83vjqWb6RFXR0sjeFXvPiA1tv1LjYIZ3SwitzTY6lec2-IFip7LvqFrw4tZI01lV7_Kwe-ykgu62YBP1HHiPOPx-H0p7IlgUiKlfy-junjMSYH1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJurk_zMf-Z9_ebfuf_PlAr1FQTUCpfjxXhmLQUJx5YP6q6znZYKvzNNUWU12v9zBJwiRKnT5LAqy1suWa2FdPbKfLABYWbWmFe1-BRsJp1-nBzNPpMG4sbt_ZjApqfXO19OxlgcxSjIV9PILo4vHLyjai6ts47byvLKC15-0pDPMs6PT7cslzImoi3CXQX9Qhy5vtt0sdaKVtL5ICxuc8iD4gGwTWe9PTYy4GRYaMJV9dvqzapJuE-EPk7kyzEeYHSnBQ_i6JPDW3wq3SP2dE-Gv3p_8DQjXnMp7iI8pZE002GR09xaadTh8bNGifalQIqEeKtQbPUhtIMUT7QWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROGpe-X5gvfBMqfZUILlGjVmMxrBaUSUN3j4sTzshl0qeycruYrgkrkYiaEzIKTvXrxR8x3uWApuz4hWPD5tFDUwxr5DAjgP7dvSGsLmYL7KC4F0BXwmGb6BlCag4FL65iKhzCWHcXeE1hwVbzWKEt-AYIE1qC-2oiv4t-8dAaesksqilMtUASdjqKhyB5XPYNim5fVm0V-Q8bKYtnIVJjaDBygRryOjuMZ_Pc_1zmHaa0dBNH_nSV1TWoHDS-936nHqHvRrVQQkDX8CAlEu2ox0hpWczlrYtNAdCCDGQ5ihuJxJXKWM8yjvYnTXyQuZos5qmC_bO3hmrYySvbzZow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5RKQcrLOezXamWiNDO9twCSf1p4yU86V894GW0Cc-HN8MFFrSqAR1yzBq7Cnn0p3TDZEU6QUvduPwT-7carrJ260IfYCPfKOy6TwGMeYduCS_jygYlynauTR5RNLmhNHn6VEuuHPclTBfjd8-w2udbKdf_CuBqQogpJqAGgs9WdrpSoaHFwwXL2JuJZQEM2mtwfxLPHhktYYcNf3Ak32cl2b52jQUzSRgUXQkzeF9QJvlT703XR2Bn8OzqmMLVDFT_mRWmeGo9oWr8A0RcBqknZ2Gg3EtQkXZYQrOkp96m0Zi-bMBv4G9SNKsOc--Lh2175F4eIzTZyWDQhnEbHHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0AdbCZkQu27bOjFySRA4w9jhHczExyuV2vZoz-QaWn_CwfbdA8lb3hexGDX6mLhGr_yjk8rnmIXK_IxT_HYFIbVdC9nY44kXbDmTI7_0flqaozTPC6BzNLMyQtNUG2WUM52mgFHRdMKbJ9h3UKzKoYvLAg6U0abbVz4s-EbW3WzhR3Cm4XM2ViU9KCXUmGIynKx93CKYsd0p_M-k7cG_TxzzH8V0wl6snIm_nSLj18MYpJ_I4Hs21sgAwRz3XnDWJakwGY44_kjQ8ihkhRkdE_sFkDeFnAvkX7M6nN0M1flJDHIvQkL2zGwSdXAsat1_VLubeI43OqEV_xfLSmvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUKSN5vQzk0zLPO6OipKW2CICT-GmTNzJUq_qiJQSqS2FHFWgaFUlA92ZB-ceBLN5T6WzL0NaNzNxZ11PBEUfcrbW8uI0pIDAjhZ8QAHDrNKOsRUqggQg6_wSmYCNpKzWJUDr_LXfGr30AQx2ZlQAZ3N3CHvq2l7GTepdWeZ3JTJ70aeUxne4NZUblyF7N7tXEHeWWv09AK95FeoZnJtg1z5Z3y5LGiVqgOBYHFT6WHvWW1Pv26W0TWyoYUNquEBB8iOAl7FYFKKhlm-0fj_HO_NFk0XwpCgp52Wtz9YMgXG7HJMCYiyjVuCA2px7zNyjS4z1Gj2dmz1BhlHtEy3CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت از جنسِ ایثار
💫
✨
آنچه از مکتب حسینی به یادگار مانده، تنها یک روایت نیست؛ فرهنگی‌ست از ایثار، همدلی و خدمت.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با توزیع گوشت قربانی، این فرهنگ را در مسیر حمایت از خانواده‌های ایرانی زنده نگه داشته است.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/677129" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2frpUXQd2oxMbfGi71lZuDYOIpFiolw0oNj9SRlz__8I7BOMACVNN7sxVYR7AA25LGg7SJHR7E_7vh1xrk3KIwsvyDAJ0MTroWPGBPQLAmn6sLnFz7xD12959ZWN1mya4rjpYL34wWLjHQvt9ONOIUfg0VGX1Aez2LYPgJftdwj3qhR8Yi2nHrR1p4mwYA1F5KneGFer3w0NbR86bkgqD52ODEOyMqPwM_UVHdfS9pQXS0f2x-TOw_vqPM1R8iMJUdph1gc6uA58EVDJn3AG6UY6zXs_Kh-uGRWPGLA1sUdmy3Ao2WXpx1J7hi8odhgB73Ww6KpWD7ur106B-MZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام محمدباقر ذوالقدر دبیر شورای عالی امنیت ملی: ادامه آتش‌افروزی آمریکا قفل تنگه هرمز را محکم‌تر می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/677128" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9Yrzcvagh11FMmFVLJ75D1COW-au5tmescEKc37lXC-u7skzoGWinLRmZy07FjME4GWhN0QU44P8pfP9B-3BlemAgwFEl0jjl_iBjPQLtIK0WPjYnGveyd0gj8IH7aaQgS75aoKSUHdysp9XRUETlaJeBc38jGmvo5kFwCHiXMzGwD49dNMLS3Xwt9MKCrUfAzagdoZ0FQost3CU9u3jZe6Yz5EZT9t2ICPXvLGTy0aNQi9kA_QuhqLYCac6CBaY946WqjkGebqGmazmV2iijQlSSG8-p-pJFreqg-GSDYsws2c98VSrV_xnbjMeqEM67fgFMlhYeOjJaQ5Ho2Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش قیمت نفت به اخبار این چند دقیقه درباره حمله آمریکا به زیرساخت‌های ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/677127" target="_blank">📅 01:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
فایل مکالمه اخطار نیروی دریایی سپاه و برگشتن نفتکش ها از مسیر غیرقانونی و بدون مجوز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/677126" target="_blank">📅 00:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
رسانه‌ آمریکایی سی‌بی‌اس در مورد حمله به زیرساخت‌های ایران
🔹
رسانه‌ آمریکایی سی‌بی‌اس در ادعایی عنوان کرد آمریکا و اسراییل با فرا رسیدن پایان هفته میلادی برای بمباران زیرساخت‌های ایران از جمله نیروگاه‌های برق و پالایشگاه‌ها آماده می‌شوند.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3234572</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/677125" target="_blank">📅 00:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
تعداد مأموران شهید درگیری مسلحانهٔ دیروز در شادگان به ۳ تن رسید  فرمانده انتظامی خوزستان:
🔹
شهید علیرضا فتحی که دیروز در مأموریت مقابله با قاچاقچیان مسلح مجروح شده بود، با وجود تلاش کادر درمان، بر اثر شدت جراحات به شهادت رسید.
🔹
پیش‌تر هم شهید مهدی مهدوی‌کیا…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/677124" target="_blank">📅 00:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd8ca2165.mp4?token=g5Yr4aFHc-q5iQWefOuAzO3ZI9PP13ddnqH83rTyd8pELzkhRzZ4JtmTbijsPZZZtwYkQv4C_8tdtLAsXX1m3rt5V4Mha1pvbhyJXTTI7KI6x5aktZyYGpBAUasfUK_VXP5XL62UIPuNZ8GYVdt6LhLy5P1kfGc8efFsonf0MJ0fBkOHkOSRZNwYJWdbaNo6XKo9KcijRZiAiR7TiPmlZ6Tff7YmSzBohSqtZRO1WFMpcBgZkEKAy0EuERSFPntGoESId6wVw5Xk9bhCZJYluYdgknnr_5kfiN1YzzYiu6spkdkdcnyq4H1ugPys6kIFk0QEWZ6fZFX3fE8XD-VevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd8ca2165.mp4?token=g5Yr4aFHc-q5iQWefOuAzO3ZI9PP13ddnqH83rTyd8pELzkhRzZ4JtmTbijsPZZZtwYkQv4C_8tdtLAsXX1m3rt5V4Mha1pvbhyJXTTI7KI6x5aktZyYGpBAUasfUK_VXP5XL62UIPuNZ8GYVdt6LhLy5P1kfGc8efFsonf0MJ0fBkOHkOSRZNwYJWdbaNo6XKo9KcijRZiAiR7TiPmlZ6Tff7YmSzBohSqtZRO1WFMpcBgZkEKAy0EuERSFPntGoESId6wVw5Xk9bhCZJYluYdgknnr_5kfiN1YzzYiu6spkdkdcnyq4H1ugPys6kIFk0QEWZ6fZFX3fE8XD-VevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل جمعیت عاشقان از نجف به سوی کربلای معلی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/677123" target="_blank">📅 00:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای بی اساس و تکراری سگ زرد: اگر به تاسیسات هسته ای ایران حمله نمی‌کردیم اسرائیلی وجود نداشت
رئیس‌جمهور جنایتکار آمریکا:
🔹
آنها قرار بود وارد عمل شوند؛ در عمل هستند. اگر من نبودم، اسرائیل امروز وجود نداشت.
🔹
ما با بمب‌افکن‌های بی‌۲ آن را از بین بردیم و در حالی که آنجا را نابود کردیم، آنها فقط دو هفته با داشتن سلاح هسته‌ای فاصله داشتند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/677122" target="_blank">📅 00:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf23f5a92a.mp4?token=mGqfFqyoFGHPPbDyJm8WAdej2KYZgwcIoZttRTCY53JmHMqmr8_e3D2AWxNSFXRyyDwxtT7Xc3VR2PqR9OMed3DXEr3t3IX1MmxZthRY5QOfHyE4qOFZl_rGejYG_tjWFGHM1B-RdmrF_nvtEHEbXM6KVBOeqbfQGhYtgwf82sDrpytOJ9QOn66-4OF5z_fQa4HYG4MBMSm2ZPW6yRvOpaiOKog_sTGE93sraRT7PWn1YjxVmkLAwDBX5r2uNvv2GzKkWO__eCtIAR88nrG8S1r9GjQ-MZzEhi7ldbg3nKsjIJrjoxA4mBvANVKtc6972oMcpiIJa-t4BjdyNWWVyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf23f5a92a.mp4?token=mGqfFqyoFGHPPbDyJm8WAdej2KYZgwcIoZttRTCY53JmHMqmr8_e3D2AWxNSFXRyyDwxtT7Xc3VR2PqR9OMed3DXEr3t3IX1MmxZthRY5QOfHyE4qOFZl_rGejYG_tjWFGHM1B-RdmrF_nvtEHEbXM6KVBOeqbfQGhYtgwf82sDrpytOJ9QOn66-4OF5z_fQa4HYG4MBMSm2ZPW6yRvOpaiOKog_sTGE93sraRT7PWn1YjxVmkLAwDBX5r2uNvv2GzKkWO__eCtIAR88nrG8S1r9GjQ-MZzEhi7ldbg3nKsjIJrjoxA4mBvANVKtc6972oMcpiIJa-t4BjdyNWWVyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: من پیش‌بینی کردم که قبل از اینکه از قدرت کناره‌گیری کنی، گرینلند تحت کنترل عملیاتی آمریکا قرار خواهد گرفت
🔹
ترامپ: اگر این پیش‌بینی را کردی، درست گفتی. در واقع، باید روی این موضوع شرط ببندی.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/677121" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
یمن: ۸ نفتکش سعودی مجبور به تغییر مسیر شدند
یحیی سریع، سخنگوی نیروهای مسلح یمن:
🔹
در راستای تثبیت معادلۀ محاصره در برابر محاصره، ۸ فروند نفت‌کش سعودی مجبور به بازگشت و تغییر مسیر خود شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/677120" target="_blank">📅 00:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqS8VjuAPThkWWlR_BdcXJantZxhrjjwZ_Ecs7P5y0bp5yye14mlajXN_EYQAuKtrpQQWcKncEHsM5Z51XKBgSt0JEHXMaUA9zWSG6KeDTCl5TUrpdptxiUgv9xd4ziuojPX1yG54zyj31HR8JSKvW8mDZsGp0WQBPWYX7RQ8cma9euVJWfBCgG4inMpKLTwHicXc7EV9InV4XDjYq7UK4wbkEGnZeXYhTPIHA6FmVePZglMF4WyHO3Bvd283UFimBEj5mcA3kZmFlEwz5LwM-rx_khM2_dmmZAUXFRifTlrNt10OaR5QX31y4EmXK5VAX_b92dw75udpPO2Gq-YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یکی از جلوه‌های زیبای اربعین اینه که پابه پای عراقی‌ها، ما هم از زوار حسین(ع) میزبانی کنیم
#میزبان_باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/677119" target="_blank">📅 00:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHcgzo6qEaJhU5K56ere1YUrVCmtbXVRPWi3RBTIXzCJpNbRwN9fsZ6DMvLvdmgNKZbMcSRi4QKgrTlDJFfW-BC7MrdesKrIR87BpiqrMxYhqcQwxBh325eMbwajoVgnWGIj8JoTp9fQr8Ga4fQ48FFg8X3KaIrti3ol8ych1IDKh7nWsKWr26TFhqpgC9cwGFsQXtoX8hyhc8hUrc9vEvxeao1cdTLHfv3OmkcOcnZEmjw-Vi9LOBof-cSOcuS30jXYO7DZoVC5uZFnMobZh5wmzfsQT9ckkkLUcuvq7BJEKeRjgFEFDflRteAQgQlHb3BDdbRcmJMqmrxv0w5G7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
از مهمون بودن تا خادم شدن، تو طریق‌الحسین فقط به اندازه یه پیش‌بند بستن فاصله‌ست. برادریِ عراقی و ایرانی تو همین چای‌خونه‌های ساده معنا پیدا میکنه.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/677118" target="_blank">📅 00:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOLLtgglD7KxGn4Mi2uu1tBfQK1PjPy6-5TPywQTuyxQIgF6lPhQAAxSegxwZkOOgBOacLlbJEoeQjMOIwNMoT8JNoqN-B8I3Zen9yxXKal1Zzrfo56mFvKijXbdVEemY_X8YF_G88u_7rTnSL9XayS79u350Ilx3K0NUsnTXy9YN2oJDCVkB3SR0yVMONRgsLg1evmwXR3fi-yIKVsTYcnCFMszY3vfdfqxnjsHp64sTATDctbv_Tna2tvBp4Dk8HADTo18xensgPSqxfdKr77k-oURJFjE3Bd99IYNk5Cp1D_FtTKh9SY2Uah22rB1LTlAVNH_bIZl65775yFuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/677117" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677116">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
گنج ۱۲۴ هزار مگاواتی ایران؛ ثروتی که خاموش است
🔹
برآوردهای سازمان انرژی‌های تجدیدپذیر و بهره‌وری انرژی برق نشان می‌دهد ایران از ظرفیت توسعه ۱۲۴ هزار مگاوات انرژی‌های تجدیدپذیر برخوردار است. ظرفیتی که ۷۱ هزار مگاوات آن به انرژی خورشیدی و ۴۹ هزار مگاوات به انرژی بادی اختصاص دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/677116" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677115">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تعداد مأموران شهید درگیری مسلحانهٔ دیروز در شادگان به ۳ تن رسید
فرمانده انتظامی خوزستان
:
🔹
شهید علیرضا فتحی که دیروز در مأموریت مقابله با قاچاقچیان مسلح مجروح شده بود، با وجود تلاش کادر درمان، بر اثر شدت جراحات به شهادت رسید.
🔹
پیش‌تر هم شهید مهدی مهدوی‌کیا و شهید سینا سیاه‌نژاد در همین حادثه به شهادت رسیده بودند/ فارس
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/677115" target="_blank">📅 23:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677114">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab10cc9b66.mp4?token=U4Z5_y7tIsulriwsW3AzZnbP_2SxWTFB7jc1vcs1O2zwvpw4H7cEAzMBB4BEcvusPQRmhU8trjP8p7L1465igs7ybNQn9NF_tlz5Bw0CF1W5Ay3WvN3qELh__tGtghD9VZaKoflh23s6PzyFb_umLRdjyX5eouBVh1iGlF-4fvnETSOO4rXXj0p2rOeAk9wHv9Z0wKGFdib4RrAQUK8FR4VktlmSfJb064j7Dz0lcJph-H6_xBZAT1md9kc6oeRTjoky8MfRhMJLDC14HwWDFTu62fyRqBe3QFIaBk_K-aZk7lSrzyi4tiwXT5aIfdZ5ksXUbDSvfIfDl248A3qvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab10cc9b66.mp4?token=U4Z5_y7tIsulriwsW3AzZnbP_2SxWTFB7jc1vcs1O2zwvpw4H7cEAzMBB4BEcvusPQRmhU8trjP8p7L1465igs7ybNQn9NF_tlz5Bw0CF1W5Ay3WvN3qELh__tGtghD9VZaKoflh23s6PzyFb_umLRdjyX5eouBVh1iGlF-4fvnETSOO4rXXj0p2rOeAk9wHv9Z0wKGFdib4RrAQUK8FR4VktlmSfJb064j7Dz0lcJph-H6_xBZAT1md9kc6oeRTjoky8MfRhMJLDC14HwWDFTu62fyRqBe3QFIaBk_K-aZk7lSrzyi4tiwXT5aIfdZ5ksXUbDSvfIfDl248A3qvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون، مجری آمریکایی: ما ایران را به یک قدرت جهانی تبدیل کردیم، و این کشور حداقل تا پایان عمر ما یک قدرت جهانی باقی خواهد ماند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/677114" target="_blank">📅 23:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677112">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emp99Tnl3b6ivsQpfl70uiablkuVkA7v-4J0HVAi0lii5OL5ybx9Mhef6EbYVy1Ez-uW0Hd4LLc1n_6hSsp0aNofAhTLpeGIxn3BRgir_qwrR2geDPt-BMCQZzFnZc-Rk1OWJcr1oTgPEsS1pP1fNcbAIvywrS0qavPk7HwiDqshxjqXOsASiGNT7trzfnWOsi_IviCpE-k6vxzIC9nliyMp7O3_FV1RpCzFJ_qx1ASgorm5p6czZQ9qDVSeCPwlUU76g_trtV6RMPvZ6J6HZ0UZntbSInJycBGhO3ZDb9rgbLotVCjayswIK41I47F_YjEezG37AJ707ew0wOCa-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiUEysvGXgtHbnAiBFLBwN64MRUEc7f3FjmuzxYUxyShve035ggLg9IT_Z61i7ljOi7gF-vCsiQtgOg4m6rfv72RDyPGGPznHny-gFaDfJ5c-rDiBpYEz43M_kCu1JOzTrTr6hD7wOw8tAzzpHJWgXZ_NgjsWzMSqceNGnHjrT1Ii-ZiF8aZY3y_RnqE6gJ6jmc4LXadxLnKht0NLHsstx4P5vCyE5jVevtQQq1W0f-mKlc764Ys6KNJ142i0dwBkyONTRQw4awM2OmsTA24KEk5p3eLL-vkXqvLq3K0-oBDY7ya1gr5pGCRskhkk-GhRPvXy2YDCvKn7od1tBy-jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امید عالیشاه با انتشار پستی در صفحه اینستاگرام خود از هواداران پرسپولیس خداحافظی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/677112" target="_blank">📅 23:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677111">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9cudVq80xD-OzwZYhxZMXmaVyKYa7dAwOzBOEhRExr6UkS7cPuel74DuLs1jlZAVcVrZlsPiA65V6ypAaF12dcHXxDFZU_FtOPJ9PJMfwce3wYbgI9Rm4FwBPlle0SKu6nl7u9-uviVpatQ4vrtWtpaJLDqATPRHW3qK7h5d13hFFU5qC8lbxcOMKEY5_6p1FPcrQjLTqpvbV2LfbMMBFh_Px7XZsBZ7VsW0BsZHJWcIJtq89NY7IQJLWxtJFdZl6kIur7kdMFZIzKrZzqgA9TT1CQucRggENyp4aDR9lvqXgENFSTnlJ8n5BpPbHhO9DNlb7qH5KX_I9uDXzt7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
۱۰۰۱ سفر کربلا
✨
▫️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/677111" target="_blank">📅 23:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677110">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acBll130bGO2lazDFo7CB4fKy7_Ex0VrwH_WZxjkvyuuLa3y6k2G6sl7c7HAU_xQkTJocNEikRCjuZlMdv0nnPBfBJO1maaSVjNj9b74_rm2ahRJGiAyaQ94jo0fJVuC2HM6AoBCZcV_7XtX-K3UxTYFO9f8DlHYcP--nPRMezgaWfXb0Sx55wqVC6lPtYCWakY0YvtfVN3-Dsi82AKzCg836MO6TTqekssyauIUT6Lf8UXlLG5itf07H_aFU_czniPaTM5w9dkMpCSbtPlr8ixFk-RQ7kgd7sQjzsbADLxLee2_FFN6LAjUmRGVAH0on1IwXejnOH7weqXHwW_H5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
نیویورک پست: سنتکام طرح بمباران دو هفته‌ای ایران را آماده کرد
🔹
طرح شامل یک بمباران مداوم دو هفته‌ای است، نه حملات شبانه محدود که در دور قبلی درگیری‌ها دیده می‌شد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/677110" target="_blank">📅 23:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677109">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/677109" target="_blank">📅 23:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677108">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جنوب کشور در جنگ ۵.۵ همت خسارت دید
هادی هاشم‌نیا، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
۲۰۰ قایق شخصی و ۵۰ لنج بر اثر حملات دشمن در جنوب نابود شده‌اند، چندین اسکله در سیریک و بندرعباس آسیب کلی و نسبی دیده‌اند و به‌ صورت کلی ۵.۵ همت خسارت وارد شده‌ است. خسارت‌ها بر اثر جنگ باید اولویت‌بندی شود و بین نهادهای متولی تقسیم شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/677108" target="_blank">📅 23:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677107">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
آمریکا واردات از ۴۳ شرکت چینی را ممنوع کرد
وزارت امنیت داخلی آمریکا:
🔹
«وزارت امنیت داخلی، از طرف کارگروه اجرای قوانین کار اجباری، افزودن ۴۳ شرکت به فهرست نهادهای مشمول قانون پیشگیری از کار اجباری و همچنین به‌روزرسانی فنی اطلاعات دو نهاد موجود را اعلام می‌کند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/677107" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677106">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ساعت فعالیت دستگاه‌های اجرایی استان قم و ایلام روز شنبه ۱۰ مرداد ۱۴۰۵ از ساعت ۷ تا ۱۳ خواهد بود.
🔹
معاون ستاد ملی جمعیت: تا چند دهه دیگر، متوسط سن مردم ایران ۴۰ سال خواهد شد.
🔹
حزب‌الله: دولت لبنان باید کاری کند، وگرنه صبرمان لبریز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/677106" target="_blank">📅 23:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677105">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df730cd0b5.mp4?token=uuayB0sKJJwKMJbc1KaWpIE5Ec-SPyJawNecPOriHrJOd98HSl0nYWToN_ndVTNZ2SVKOqkMnw6ULCLx-Kt2VJDB2SGfeNe_qdYPOTRK2wYZBTIOUfxHdybd-izPhw3xdnV6fymteBscvGHi2sB6PYmJIyC80nksOC3DVYqd6-gd269fkf9D65-Wzx_ei9fPQn_dls5D7_2IALdqI749EZ7vg-WVimtcDtlv_yS8BlBMbk_blaoDl6ULhkmWMb8Qe3tQQc4jGp0z4B6hsFbeeJ-eTwpRVggCZ-uphdujEEv9Tw3cOHZ6dftZCWbxzt3SJCeqd3lfty6ar3pi784dWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df730cd0b5.mp4?token=uuayB0sKJJwKMJbc1KaWpIE5Ec-SPyJawNecPOriHrJOd98HSl0nYWToN_ndVTNZ2SVKOqkMnw6ULCLx-Kt2VJDB2SGfeNe_qdYPOTRK2wYZBTIOUfxHdybd-izPhw3xdnV6fymteBscvGHi2sB6PYmJIyC80nksOC3DVYqd6-gd269fkf9D65-Wzx_ei9fPQn_dls5D7_2IALdqI749EZ7vg-WVimtcDtlv_yS8BlBMbk_blaoDl6ULhkmWMb8Qe3tQQc4jGp0z4B6hsFbeeJ-eTwpRVggCZ-uphdujEEv9Tw3cOHZ6dftZCWbxzt3SJCeqd3lfty6ar3pi784dWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدا راه شکست را به سوی امتی که در برابر ظلم ایستادگی کردن، بسته است... #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/677105" target="_blank">📅 23:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677104">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سخنگوی فرمانده کل نیروهای مسلح عراق اعلام کرد که نخست‌وزیر و فرمانده کل نیروهای مسلح دستور افزایش سطح آماده‌باش در پادگان‌ها و پایگاه‌های نظامی را صادر کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/677104" target="_blank">📅 23:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677103">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
الجزیره: قراردادهای آتی نفت خام برنت ۱.۲۲ درصد افزایش یافت و در زمان تسویه به ۹۰.۱۲ دلار در هر بشکه رسید./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/677103" target="_blank">📅 23:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677102">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nky-uNatfgk3TvS4XJFzBciCdGuna9OCOeqptKTWXaeJERwd9-mn0V3nQxP4Wmxa3idu6L1jMHvtrjZj2HUrTaw1OfOWtOLuHRunVsJQlJSi0Q4_BQbc8ztqDnpfxOSUzcWE6cVnWCuuVElfuBMajQ_FICwDia3X7neyB1i21ekUlmEl8VqFdVSDJtuQutBpOd-Keh7c_hCCHfdsMQt_lFCWdxL6Q_VNup2giHom0ui5hUUYV09Um6fyS2IP3cUIhFKA9jYEeBPyCO5dxx3cKm_3MAqmv1FkjFF0TLd-rTeDqt3SNKstk0AN3ZkuS6LqcXokWSdBwE_pyyHu66GP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاوشگر کنجکاو ناسا دریاچه‌ای عجیب از الگوهای کندویی‌شکل در مریخ پیدا کرد
🔹
مریخ‌نورد ناسا در دهانه گیل، تصاویری از دشتی با الگوهای چندضلعی ۴ تا ۸ سانتی‌متری ثبت کرده که می‌توانند نشانه‌ای از وجود آب در مریخ باشند.
🔹
این ترک‌ها احتمالاً بر اثر انقباض و انبساط گِل ناشی از تغییرات دما یا خروج آب از رسوبات ایجاد شده‌اند. کنجکاوی پیش‌تر مولکول‌های ارگانیکی در خاک مریخ یافته بود که نشان‌دهنده شرایط مناسب برای حیات در گذشته این سیاره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/677102" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677101">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHm14TI0KCCULVr5Lkv2lxuSzUP-wdqEICT_sSmbF6o9FHcnhSahVhDATus31uDR0CLCPCivLAXvqrftxeBTF202aJR8UsiUDFyj_HnSMyMQFe-z0Qop24ClWn6uWAmBBAMDLkIoLWHa6-rroUmJC9YuhsZypuHPJ-zss_oT12jom7jQQjlwWX-YbRVFYBbkZLu7KDvcCvgWzN9OqVIoqmbObh8-KdDinysYpURggX3datt-NcmLhMmZ1vO1nA5ju6ZYWc24tnE_qt67Ru8KJcmVtEMGWP8ukEnafEphCwKyBUvxwfkwHi7v_xo-wANJcYHKVKQSCuFdiyAnKHxmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
در راهِ حسین(ع)، بعضی‌ها فقط عبور نمی‌کنند؛ می‌مانند و خادمی می‌کنند.
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/677101" target="_blank">📅 23:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
فوربس: آذربایجان همزمان با جنگ ایران پدافند هوایی خود را تقویت کرد
ادعای فوربس:
🔹
آذربایجان در سایه جنگ ایران، پدافند هوایی خود را به طور قابل توجهی تقویت کرد. باکو اخیراً با خرید سیستم‌های زمینی دوربرد اضافی و جت‌های جنگنده نسل ۴.۵ که می‌توانند با طیف وسیعی از تهدیدات هوایی مقابله کنند، دفاع هوایی قابل توجه و متنوع خود را به طور پیوسته تقویت کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/677100" target="_blank">📅 23:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmRX2BdGDnzp5mahhovOvCvNqnxd94Ox2VFuJbSBArbhKaSLdH4JoIXcl555lWOAcfnrzlE84uU5gmUFdlPtMkX4PmBq44qGSeEqAJPvZUPh4KNG6MC5lBbq_yN-AslIgIQG0zzR9azdDyVQ174jaP5XCyudFOCI29hWjVDsw5y0Z8ICSPuEz3Xe0dHr67vfujzsZlsw8NjElBFfKL9BC0jxp1Oo-BInn1SuohPP9Rdu7AQp1EIhikb1ltsZk98ltVugCh6zibPvK4WQflvs_6szWPMyt33tRbd7p9XwnvVJvqZFW22eZ66WF3mijKs72uNo3AkU5BMtVGXQCwp_yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری دانشگاه و صنعت؛ چرا ایران در رتبه ۱۱۷ جهان قرار دارد؟
🔹
بر اساس آمار، ایران با امتیاز ۱۷ از ۱۰۰ در شاخص همکاری دانشگاه‌ها و صنعت در تحقیق و توسعه (R&D)، رتبه ۱۱۷ جهان را کسب کرده است.
🔹
این شاخص نشان می‌دهد دانشگاه‌ها و شرکت‌ها تا چه اندازه در انجام پژوهش، توسعه فناوری و تبدیل ایده به محصول با یکدیگر همکاری می‌کنند.
🔹
کشورهایی که در این شاخص عملکرد بهتری دارند، معمولاً چند ویژگی مشترک دارند:
سرمایه‌گذاری گسترده در تحقیق و توسعه، ارتباط نزدیک دانشگاه با نیازهای صنعت، حضور شرکت‌های دانش‌بنیان، حمایت از تجاری‌سازی پژوهش‌ها و مشوق‌های مؤثر برای نوآوری.
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/677099" target="_blank">📅 22:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKwk6HJ3apdYZSG7tDOoM6vvgkMZllZ3s09tNSlX_TJpbHdf3HxJrYKZt78_DPXQaumDD8e7tL3ak6XfqmZy2_Q6xpkuxh-fzQ2jWairJZVyNkOS01R0YsbwAZTJzvkFYe5wejQ91bGHGIGzMCjZL8T7UCNrNkW7F88XH5OrIl4WRcfQClOQ_Vj6LmunFgil3pCmXYeHdB7YNRRoC4ocmPYRM_53nRF7mDihA2NvQOTsxvRQ1WsL8P0b6u7cFnPvBUmKvBITvQxGMSj_sAIj1rvQpiRR6ymsU5hjYua9FPeKMmvZaAvN8BTTduwKOhuzhydwLv7t58lQPSVm9YXqcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنفدراسیون فوتبال آسیا هم علیه فیفا شد
🔹
«ای‌اف‌سی» در محکومیت طرح پیشنهادی فیفا برای سرمایه‌گذاری خصوصی، به یوفا و کونکاکاف پیوست واعلام کرد نگران است که این طرح به نقطه‌ای رسیده باشد که «تحریم جام جهانی وارد گفتمان عمومی شده باشد».
🔹
با استعفای کارلوس کوردیرو، مشاور ارشد فیفا، ضربه‌ای مخرب به رئیس فیفا وارد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/677098" target="_blank">📅 22:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7264884e.mp4?token=feGEnwM94di3qTmf5qKRTK3nM1LBhhU7qXFR43TfUY-1NgUcWTZpib-kCW_mwMK8_2xqbwLavOvBHfTRnSbDP7shzj9XI2i8hJoBn6UIw4SjvLqVYQe11SZdAATm1ChBSqpe_k42HjnsTbaeagNLMOBzRYCHaMFsZRGCMnd9JpGTwedVTdVU5i53f-T79iNoK9gmmuX0bIx7TzM5tgIEDOPQm0VbGek7Xps53zYLaPc0aWLfagBIJ_23Tg36YQEkhQnf60OEX5fnCFrEoKRR0d4ObvzWCwu2BddcopFo3zKDfog-6jaer1Xu6Yr631i-smv01RuemJp7KIv4r6p9lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7264884e.mp4?token=feGEnwM94di3qTmf5qKRTK3nM1LBhhU7qXFR43TfUY-1NgUcWTZpib-kCW_mwMK8_2xqbwLavOvBHfTRnSbDP7shzj9XI2i8hJoBn6UIw4SjvLqVYQe11SZdAATm1ChBSqpe_k42HjnsTbaeagNLMOBzRYCHaMFsZRGCMnd9JpGTwedVTdVU5i53f-T79iNoK9gmmuX0bIx7TzM5tgIEDOPQm0VbGek7Xps53zYLaPc0aWLfagBIJ_23Tg36YQEkhQnf60OEX5fnCFrEoKRR0d4ObvzWCwu2BddcopFo3zKDfog-6jaer1Xu6Yr631i-smv01RuemJp7KIv4r6p9lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه آتش سوزی جنگلی در فرانسه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/677097" target="_blank">📅 22:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581477b92b.mp4?token=BQLthWv4GyLY90PBWWNvyQYu8t0wsTLsZCYSvIETZerOU-C0-sgSLcluRoLHRVZP4j-DB04yye9bwLpV6uRvEgOFaeL1RxVFQj7LsvXcCZZ50627D0o5cfwo9wCNr6i5dU8nCLcrjM-Yr2qa3pLOSB5Q2lihTvPWY318xvAbJXLw2dt1SldNrmvlFwyZck0bBbjkIbs1hDEMbmx0YpiAWu2_0iYnWleesvipsgfLo_A8-Fpo7c9k00saTbEJ-W_knqNsk5Fepa4LZvU7MOq-yekePN6OkYNn-INNXWkuGzD1qW9oW1WLZHPp0N6wklF7tuRLvXXHzNH5PI78MPTIsp2qDuvR2Nrghts-ucmyWcB-kuhOf3U2lem-7QoPuQR3cuUIW1mYJijb8cR6V3do3kDD_UkKKhEiQH0CwSFP3wjNIGMwB0rgKaJz6mxAv72Yf1n3d0RIGxwSrfS9C4c6agGxA2TfnNvVe1AjxBvaT04wmfmZ-XTRtucPFIlQJaEsiEJKK_5gu-De5H4sVLSBzp3DMa1WG09wmz8S2qUywPSDSynGqJsQpdBvyWplWevJK1uy5QPHJ9lNC2tM9o0R1vrlq-OIvAsGnNgXxRf7Uy4LPi0UKWdp6aaWaoFFppFkmwuUrMCC-wzb_mA62d9HFtjsRlMwB673oqCCC2jfBTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581477b92b.mp4?token=BQLthWv4GyLY90PBWWNvyQYu8t0wsTLsZCYSvIETZerOU-C0-sgSLcluRoLHRVZP4j-DB04yye9bwLpV6uRvEgOFaeL1RxVFQj7LsvXcCZZ50627D0o5cfwo9wCNr6i5dU8nCLcrjM-Yr2qa3pLOSB5Q2lihTvPWY318xvAbJXLw2dt1SldNrmvlFwyZck0bBbjkIbs1hDEMbmx0YpiAWu2_0iYnWleesvipsgfLo_A8-Fpo7c9k00saTbEJ-W_knqNsk5Fepa4LZvU7MOq-yekePN6OkYNn-INNXWkuGzD1qW9oW1WLZHPp0N6wklF7tuRLvXXHzNH5PI78MPTIsp2qDuvR2Nrghts-ucmyWcB-kuhOf3U2lem-7QoPuQR3cuUIW1mYJijb8cR6V3do3kDD_UkKKhEiQH0CwSFP3wjNIGMwB0rgKaJz6mxAv72Yf1n3d0RIGxwSrfS9C4c6agGxA2TfnNvVe1AjxBvaT04wmfmZ-XTRtucPFIlQJaEsiEJKK_5gu-De5H4sVLSBzp3DMa1WG09wmz8S2qUywPSDSynGqJsQpdBvyWplWevJK1uy5QPHJ9lNC2tM9o0R1vrlq-OIvAsGnNgXxRf7Uy4LPi0UKWdp6aaWaoFFppFkmwuUrMCC-wzb_mA62d9HFtjsRlMwB673oqCCC2jfBTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اربعین امسال رنگ دیگری دارد؛ به نیابت از رهبر شهید راهی کربلا شدیم، اما داغ این فراق هنوز تازه است/تنها ظهور حضرت ولی‌عصر(عج) می‌تواند مرهم داغ دل شیعیان باشد
/ موکب رسانه‌ای یالثارات الحسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/677096" target="_blank">📅 22:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مدیر دفتر الجزیره در تهران: اطلاعاتی به تهران رسیده که اگر گفت‌وگوهای ایران و عمان به گشایش تنگه هرمز بینجامد، واشنگتن محاصره دریایی و تحریم‌های نفتی را لغو خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/677095" target="_blank">📅 22:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eece875fa5.mp4?token=I-MgxsifSBn_xfP4Rr8r3AYERLOV--f7-uV7tZ7n4Pq8OqOqv_WE_Y6iRpVnfvR2HIb2jFbCZtWaj128OkQJuwWXot2XKmftAjTZTMqK_JOnXCpLJ1X9S40YdGvGdzF5rc0RSjc2O7U__d6K8QFxO_IE52884fz0bCNw70CoN8Dcbl9epCFg50OJhMkdfrJeS8y-ZogwK7xNluQ89pLSMb7L_O0n60eTuhak4Hsv8IyASzeOUnPZHQ4__aBpghgPisyhA6wXucgq3QdplRV2EAYMr15pR06fOMiOupQZCvqh2gLgpCLpPk8nXSaBE4PU-ti6J6f2IuRbHOPmgSzTL6IcAyLz5kc67purqwnpNjXDPBPdGMlCC6ZwPzDe7QTXfupHynB-9m4fUV2tQ99OyJK8aZs52OfWODKzDaEfIKwsGhiOw8SfLuiMJxY1z0I2q5fjrzitBJCWp6IQ6X7v0BB738TSwU1Rlz505lruPTp3TANB-_eKIOCRhYQzIkPiTCFidY4YgqhjBDWp5LcWQD4s6h3KiP9L6HTgcTqWb-pFmNa_XcSgvt00GAmjZdYJcQYMhhcBTwlqQaT8upkQDE0YfvMxDXdBSkEcewyrV9dFyEQc0g4ujiLHSawjD6NROClH_5WWTXWa0ayeuFhLeago3GOL5r3IS6VFZuhF7UU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eece875fa5.mp4?token=I-MgxsifSBn_xfP4Rr8r3AYERLOV--f7-uV7tZ7n4Pq8OqOqv_WE_Y6iRpVnfvR2HIb2jFbCZtWaj128OkQJuwWXot2XKmftAjTZTMqK_JOnXCpLJ1X9S40YdGvGdzF5rc0RSjc2O7U__d6K8QFxO_IE52884fz0bCNw70CoN8Dcbl9epCFg50OJhMkdfrJeS8y-ZogwK7xNluQ89pLSMb7L_O0n60eTuhak4Hsv8IyASzeOUnPZHQ4__aBpghgPisyhA6wXucgq3QdplRV2EAYMr15pR06fOMiOupQZCvqh2gLgpCLpPk8nXSaBE4PU-ti6J6f2IuRbHOPmgSzTL6IcAyLz5kc67purqwnpNjXDPBPdGMlCC6ZwPzDe7QTXfupHynB-9m4fUV2tQ99OyJK8aZs52OfWODKzDaEfIKwsGhiOw8SfLuiMJxY1z0I2q5fjrzitBJCWp6IQ6X7v0BB738TSwU1Rlz505lruPTp3TANB-_eKIOCRhYQzIkPiTCFidY4YgqhjBDWp5LcWQD4s6h3KiP9L6HTgcTqWb-pFmNa_XcSgvt00GAmjZdYJcQYMhhcBTwlqQaT8upkQDE0YfvMxDXdBSkEcewyrV9dFyEQc0g4ujiLHSawjD6NROClH_5WWTXWa0ayeuFhLeago3GOL5r3IS6VFZuhF7UU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظامیان اسپانیا مانع ورود مهاجران مراکشی به سئوتا می‌شوند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/677094" target="_blank">📅 22:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بنزین ۱۰ هزار تومان شود، تورم چقدر بالا می‌رود؟
یوسف کاووسی، مدیرکل اسبق بازرسی بانک مرکزی در
#گفتگو
با خبرفوری:
🔹
در کنار سیاست‌های بانک مرکزی برای کنترل تورم، در دولت بحث افزایش قیمت بنزین از ۵ هزار تومان به ۱۰ هزار تومان مطرح است که می‌تواند اثر این سیاست‌ها را تضعیف کند.
🔹
برآوردها نشان می‌دهد این افزایش قیمت، حتی با وجود سهمیه‌ها، می‌تواند حدود ۵ واحد درصد به نرخ تورم اضافه کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/677093" target="_blank">📅 22:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96e63300c9.mp4?token=LrpulLivNoxA4LbJuMoXtItCCaJyytGmKzCK3dNTlSjGjASwnlDTVB6Gy8lgXJZu3kXBNruydPGpAQ0QkmRAi3JgSoyj0kwwV8GrXupvdQEIPfW4zUwlOLMwPGeXArOCCMlVMEpAyZG8DYe8aNIlWvcUWSpGHvxqQblaCIrnfteOPRkbbkmsGWk3Pgu7Bxpb62JOwwk_EDRtGi84lnVehUrHbXyE-R-6in0hTI51_vZQnkmSRVsVI3gsuCG8x8CF3DTcciuJBhoGCU57MIBmvHf9KPrKxmeydcoy0JkWAl3UOqZZVR03WX5q_uO1cATbfqahOVi1GAa51NYQnKLtlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96e63300c9.mp4?token=LrpulLivNoxA4LbJuMoXtItCCaJyytGmKzCK3dNTlSjGjASwnlDTVB6Gy8lgXJZu3kXBNruydPGpAQ0QkmRAi3JgSoyj0kwwV8GrXupvdQEIPfW4zUwlOLMwPGeXArOCCMlVMEpAyZG8DYe8aNIlWvcUWSpGHvxqQblaCIrnfteOPRkbbkmsGWk3Pgu7Bxpb62JOwwk_EDRtGi84lnVehUrHbXyE-R-6in0hTI51_vZQnkmSRVsVI3gsuCG8x8CF3DTcciuJBhoGCU57MIBmvHf9KPrKxmeydcoy0JkWAl3UOqZZVR03WX5q_uO1cATbfqahOVi1GAa51NYQnKLtlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر سقوط اف-۳۵ آمریکایی در سن‌دیگو
🔹
بقایای این جنگندهٔ بیش از ۱۰۰ میلیون دلاری هنوز در آتش می‌سوزد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/677092" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmvEMGRzj5UFP91sCOMj7dhtbxtThBmOiQVkk1skPHMxYe6YMpJVE4drufNZY3fwmADwwdNAYE36_hRss_PvL76jna9zDnwLdwMdpxjyfm4peY4QnK8tLUDK3j4CsVjxav8ruBRV1ij0cN3oyW-dmtBM-CrKaUiDnWRe5zPy_5LERyZqUhlEdn_AiYuhGTCFWQUnZ3GJs7e8Uqe9S4avy6Lbz8UYPEGw0EwtRBiei1HKaM4YAyxUTS5XPFHPx2Yb-P1HAe3_gmYfNaOCk9NQgJmKZsw9UP2OV_fd3PL5tR5MiW3db50Cu7s8ClOXaJ9iyRlrWUhs-P2dbxNcVMYW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ستایش سقف‌ها...
🔹
سقف ورودی کاروانسرای شاه‌عباسی؛ جایی که آجر، نور و هندسه در هم می‌آمیزند و شاهکاری ماندگار از معماری ایرانی را روایت می‌کنند.
🔹
حسین کریم زاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/677091" target="_blank">📅 22:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
نتانیاهو به‌دنبال عادی‌سازی روابط با عربستان پیش از انتخابات
روزنامه‌ هاآرتص:
🔹
نتانیاهو به چند تن از دستیارانش گفته است که پیش از انتخابات به «یک دستاورد بزرگ دیگر» نیاز دارد و منظور او توافق با ریاض است. نتانیاهو امیدوار است موفقیت حزب لیکود در انتخابات، زمینه‌ساز ادامه نخست‌وزیری او شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/677090" target="_blank">📅 22:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سنای آمریکا به طرح توقف جنگ علیه ایران رأی منفی داد
🔹
مجلس سنای آمریکا به طرحی که خواستار توقف هرگونه عملیات نظامی علیه ایران در صورت عدم دریافت مجوز از کنگره بود، رأی منفی داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/677089" target="_blank">📅 22:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNqMkFnxThQDncNCwE392XnYeeapDDY-Q5NsZJaffW2Z5JzIekDlrTyeHukgNU0pJFry2TEWunrsO93QK8wVUSOaG4h_EHuWh4vzJ4aYXUDEeVUeWlH6iC8vkwpMA40idOLnrv3TegXTj2DumSMi06HpiFPWCpeakUTLNlv2K47RGbgeUtGBFL3BnO-ptwfzF1ikPlWunMqx6FePAl9YEo3rGsFLLT8Pdb87ZVg1aelv-oNChjZJmFrg2gQt-6Aj7_KuqWJo9igYG4pHAwlr1CDgBnMeKgL3Gya06sqLLLvwu2fl6a7XSpAHcvB6B9WodXvmykVLlumZ8O8GQVP4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/677088" target="_blank">📅 22:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677086">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW91SAGC9C5ZZ5GueOfqFB2U3COLu4cJ_FE3t666k40Qxn1lGr6dOvhnB3dqQ69gRP0JVagtXSuqgEbFJoNlRjFJD4_7hR8FYI0riwcqrGcjE-2m_R5lVWg1S7LVazguFjCnruNkpEjSgP7s_Suy_aMEV8aSgiHezmCnHe6ecfeCdhZ1UBwCAWFMviHtY9278wRKzMUfLhAMIqfghPnTY1CNEFmGsOmPwKIg0ji-WGLkAPaal2kKLG-OsA2bw19cxynCiu5TeHy0fW2Kv3c7GwN9RFUrngfL3Vn7ZM3m7ncIBh0OQGERMFFrS_w-5rtQ3qFJEm7AJpYt1h7ZSp46sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۳
جمهوری‌خواه در جنگ ایران، صف خود را از ترامپ جدا کردند
تایم:
🔹
۳ جمهوری‌خواه در تلاش برای محدود کردن اختیارات جنگی ترامپ علیه ایران، از صف خارج شدند. سنای آمریکا با اختلاف کمی تلاش عمدتاً نمادین برای محدود کردن اختیارات جنگی ترامپ علیه ایران را رد کرد.
🔹
رأی‌گیری ۴۹ به ۵۰ روز پنجشنبه عمدتاً در راستای خطوط حزبی بود. سه سناتور جمهوری‌خواه لیزا مورکوفسکی، رند پال و سوزان کالینز در تلاش برای مهار کمپین نظامی جدید دولت ترامپ از صف خارج شدند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/677086" target="_blank">📅 22:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677085">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVLwnDQG1nAfgNXo7V7b_wK8o7-G2du-rmA2kr1SWivCFOd68OjkqybVypARQTDHPdB8Z5mi3FVe25gCSjiE9ha7JblOnLQKnbMfS2xkOyTWLnytjo_BhJEnXfmZjZdPvOGIAjm1C_tkQm3gGuTWZowYoELv5bScV8P0VU5QzL0dDujK7vs68HLQm5sYLXeifr5QF5tlGH9TJcSfPeHn5pkbV57OF24-P6qVtqIPPG_s_1qHVJievD9z-SrycrHxtwYyuk6H0TF_sj1bYDwgBpsZeJGcVY0VpnHgNu8wR54Clj-oQMKgxjU6239ltm-wY1pjm6t1MUcaZEPU7ltz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨️
قبل از قدم گذاشتن در مسیر اربعین، خوب است چند نکته ساده را رعایت کنیم:
▫️
ما فقط زائر این مسیر نیستیم؛ در کنار برادران عراقی‌مان، بخشی از این میزبانی بزرگ هستیم.‌..
▫️
با استفاده از لیوان شخصی زباله پلاستیکی کمتری تولید کنیم
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/677085" target="_blank">📅 22:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677084">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184f60d6b5.mp4?token=rRWMaRu2e1W7U_4wecl1P72brgenx1m9ymNrdSBCx3gKMQMFjRlbJbchqkVoFhTmUwUpqiDBwQoYhqgE8fjpVqRmUiyAE-iqFvbRHghQurKoXcDJLQrOhBGladDJGDvxIsvX-f7fMzAlXTmDFbxZS7qzrwPYGz4_BTsS_9CRzinCKKHm6mOfjW3z_zPm_khDR3_CSMSam1eWOiZCPM8uXSArhW6lonNzbVvCABDfVqHu6aiT7YplUiKjIB2ciCnzAQmIeep9bev7ouFS04LdVXfeMTIAOzAMVAysTVT6FJTxDBQ8krnmHmDTdvW4s40brB71px3AfwjPckhm6EwnrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184f60d6b5.mp4?token=rRWMaRu2e1W7U_4wecl1P72brgenx1m9ymNrdSBCx3gKMQMFjRlbJbchqkVoFhTmUwUpqiDBwQoYhqgE8fjpVqRmUiyAE-iqFvbRHghQurKoXcDJLQrOhBGladDJGDvxIsvX-f7fMzAlXTmDFbxZS7qzrwPYGz4_BTsS_9CRzinCKKHm6mOfjW3z_zPm_khDR3_CSMSam1eWOiZCPM8uXSArhW6lonNzbVvCABDfVqHu6aiT7YplUiKjIB2ciCnzAQmIeep9bev7ouFS04LdVXfeMTIAOzAMVAysTVT6FJTxDBQ8krnmHmDTdvW4s40brB71px3AfwjPckhm6EwnrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش‌های ایرانی که حتما باید بشناسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/677084" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677083">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da87f3ea8a.mp4?token=b0jVHnjXtw3o5-TuEKgRudIDXsVzcecYKUhEUpgX-ONpdA9dgyaOzntTQpM6QvCeV1nm5KafPyCljaKTuunvzqNe9euXfQsa0-wl1ncvryvAHP3VbCaFj15_LX6F2VNQY1OmEYZj4BBtf8q_j2WLQZp2O1v_ExUvzGtNxLlgzke-8-kSw-afZEFxMhleJV79Qt5fDahNjBOZyG3hfItIdbkD5A48hTXSWfOMmeYNIFIYPobb0mHuAVPXLND9jvVGA6Orp0Cyq5vtCGni-QNbojAxx12nvo-FF8e0CJ6HuDByXiRd1ET1zdX5OMMr5Lq6PObVl3Y9vFU-eGhuuVHXHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da87f3ea8a.mp4?token=b0jVHnjXtw3o5-TuEKgRudIDXsVzcecYKUhEUpgX-ONpdA9dgyaOzntTQpM6QvCeV1nm5KafPyCljaKTuunvzqNe9euXfQsa0-wl1ncvryvAHP3VbCaFj15_LX6F2VNQY1OmEYZj4BBtf8q_j2WLQZp2O1v_ExUvzGtNxLlgzke-8-kSw-afZEFxMhleJV79Qt5fDahNjBOZyG3hfItIdbkD5A48hTXSWfOMmeYNIFIYPobb0mHuAVPXLND9jvVGA6Orp0Cyq5vtCGni-QNbojAxx12nvo-FF8e0CJ6HuDByXiRd1ET1zdX5OMMr5Lq6PObVl3Y9vFU-eGhuuVHXHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های آمریکایی: یک جنگنده اف-۳۵ صبح روز جمعه در پایگاه هوایی نیروی تفنگداران دریایی در میرامارِ سن دیگو، سقوط کرد
🔹
دود غلیظی حدود ساعت ۱۰ صبح مشاهده گردید و تیم‌های امدادی در محل حادثه حاضر شدند. مقامات در حال بررسی علت این حادثه هستند و هنوز جزئیات…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/677083" target="_blank">📅 21:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ اشفع لنا فی الجنه</div>
  <div class="tg-doc-extra">محمد حسین پویانفر قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/677080" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
هر جایی گیر افتادم
حسین رو برگردوند از من نه
یا وجیها عندالله
حسین اشفع لنا فی الجنه
🎙
#محمد_حسین_پویانفر
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/677080" target="_blank">📅 21:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd5c59a58.mp4?token=nulFSOiw7uzRB_yPNgQJtZJKv8724Pc_5hyzZv-SeoYkEv5bS7f79Z8qecIwL67Qg9SXjipMvHcSLCZ5IkMXPMB_YFOV5FbOWouKtiJ5yG2nd80Id1ZVJM__qAxggSZnYvEkOfrbY_ZRmFdOQ1sC3AdvSoGyFM538xKgpVdYQKg-eYhEfs3OEeckzhZogW4hpid__-NoUf9tntWK3hcaA-wz2JlB7G8joaiaAAYruQIosxr1PHzp6v0lkI9nQAuCCaW0LXKk6vPOV9zLKWGPR18x5zO4TDUOANB2-xHRxzeLES_lwKcyo5NvtLbVNhbPcm-I-BmL3Ng-HSteEsM7sjioyMvduJ4yms54XmIJDMasWrgSzYgbfBpc_KQot0_WgUSEpIjk9hX_sru9YxcJTdtP6QkhkqGjbqhRd8YApoSlbN9-x7MdMTyzQ6eGNDjCg5nExSXqDEcS2a5LOpoSAXVIqHKI86ggycIwCCb2yaeo6r8D5BAVbArhx4B8mwg_ok-3dSBNEIo0G_vsG8eauAhIaWSat_bs1A1L4eiBD4z2UL3yOMrdzsXV-DIk6vobTOhhbGL2GYffZGRmiFnFTGNyro0GIuPQynRHFpQplt1t44OS1g-2xTWn-jtrp7dW_U-Zm5F_jdlP0lW-WhqhOitKlRFObAwH6fWNOXw9HOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd5c59a58.mp4?token=nulFSOiw7uzRB_yPNgQJtZJKv8724Pc_5hyzZv-SeoYkEv5bS7f79Z8qecIwL67Qg9SXjipMvHcSLCZ5IkMXPMB_YFOV5FbOWouKtiJ5yG2nd80Id1ZVJM__qAxggSZnYvEkOfrbY_ZRmFdOQ1sC3AdvSoGyFM538xKgpVdYQKg-eYhEfs3OEeckzhZogW4hpid__-NoUf9tntWK3hcaA-wz2JlB7G8joaiaAAYruQIosxr1PHzp6v0lkI9nQAuCCaW0LXKk6vPOV9zLKWGPR18x5zO4TDUOANB2-xHRxzeLES_lwKcyo5NvtLbVNhbPcm-I-BmL3Ng-HSteEsM7sjioyMvduJ4yms54XmIJDMasWrgSzYgbfBpc_KQot0_WgUSEpIjk9hX_sru9YxcJTdtP6QkhkqGjbqhRd8YApoSlbN9-x7MdMTyzQ6eGNDjCg5nExSXqDEcS2a5LOpoSAXVIqHKI86ggycIwCCb2yaeo6r8D5BAVbArhx4B8mwg_ok-3dSBNEIo0G_vsG8eauAhIaWSat_bs1A1L4eiBD4z2UL3yOMrdzsXV-DIk6vobTOhhbGL2GYffZGRmiFnFTGNyro0GIuPQynRHFpQplt1t44OS1g-2xTWn-jtrp7dW_U-Zm5F_jdlP0lW-WhqhOitKlRFObAwH6fWNOXw9HOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان ارتش از لحظه‌ای می‌گوید که پایگاه آمریکا را بمباران کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/677079" target="_blank">📅 21:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
منابع رسانه‌ای از وقوع انفجارهایی در داخل یک پایگاه نظامی امریکا در کالیفرنیا خبر دادند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/677077" target="_blank">📅 21:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2339d551bf.mp4?token=BbX3A06WgFgbRM3aG0GLppko-7hh4y_Dq_pcdgO9RPTd9UfxxWI1sbBPBwbFvnuqhQh0tC_H90qmzRN0U9WLoAuuvsrwba59cqwuxB3pgSSQh-TOLTW2YYOwlultbHDVWDBFs382bTGpNt6-aBOy_kdy8g_6c3QmxtfSO7E-Awr7pMm1OUnUg-QbUSW7L1sS0Y5uTyPpw71mIsq3_87ZXl9AQC7mFsdiaqWFJX2fx6MUlp-5TebrajmbjuF_XnMwuZpBU0t9x9r3UAO1M6LyInlHa6oekhkBc9k9ocwLt2NJOvJMtAkUMylK_eBf6ou2Obtd_cE9QAYfX2Kd6aW3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2339d551bf.mp4?token=BbX3A06WgFgbRM3aG0GLppko-7hh4y_Dq_pcdgO9RPTd9UfxxWI1sbBPBwbFvnuqhQh0tC_H90qmzRN0U9WLoAuuvsrwba59cqwuxB3pgSSQh-TOLTW2YYOwlultbHDVWDBFs382bTGpNt6-aBOy_kdy8g_6c3QmxtfSO7E-Awr7pMm1OUnUg-QbUSW7L1sS0Y5uTyPpw71mIsq3_87ZXl9AQC7mFsdiaqWFJX2fx6MUlp-5TebrajmbjuF_XnMwuZpBU0t9x9r3UAO1M6LyInlHa6oekhkBc9k9ocwLt2NJOvJMtAkUMylK_eBf6ou2Obtd_cE9QAYfX2Kd6aW3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران فقط یک نقشه نیست؛ خانه‌ای است که ریشه‌های‌مان در آن جان گرفته و هویتمان به آن گره خورده است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/677076" target="_blank">📅 21:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
تعیین‌کنندگان «مُد» در ایران چه کسانی‌ هستند؟
🔹
در ایران کارگروهی تحت عنوان ساماندهی مد و لباس وجود دارد که یکی از وظایف آن بررسی پیشنهادهای پوششی است. در این کارگروه که ریاست آن بر عهده معاونت امور هنر وزیر ارشاد است، نمایندگان تام‌الاختیاری از وزارت صمت، آموزش‌وپرورش و سازمان صداوسیما حضور دارند.
🔹
همچنین سه نفر از نمایندگان صنوف طراحان و تولیدکنندگان پارچه و لباس و همچنین یکی از نمایندگان کمیسیون فرهنگی عضو این کارگروه هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/677075" target="_blank">📅 21:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مرکز اطلاع رسانی فراجا: اتباع خارجی مقیم ایران و متقاضی سفر اربعین، پیش از عزیمت به مرزها، گذرنامه «سند خادم» را در محل سکونت دریافت کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/677074" target="_blank">📅 21:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677073">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNpi2WHMJiegNvgma1gzs-jCtuMm0Cnvm3-OeqPrQWRQvEZhsGG97ofnt54MD93sdKt9l386hw6P-nthOg4CWpExjkYAuwyXCYTZ8nmaZuz3yOJh4O4nw0isAp1yubB-bRr-464_N0q0ePoJnXwvoCCxVZ7dACgZa9eirgP_W4XunzRlWJqpmJRlHPeUZCIye__CpuCzsJfS24qVb2eXICMGw9Yrd8I7sVxjZkP0AN4LYlhSOKA-r4B7ao11HS_2K-aE5kl-mfK_vEltr9Q2Y30iVxh5-8d2bXc4jrca_I8zFnw9Y4Tc2BHCwAWbdp_guEqfN73-oE82feNgqlyEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عسل رو با چی بخوریم؟
🍯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/677073" target="_blank">📅 21:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677072">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2a99dfbcd.mp4?token=LiQ0NHchRtxzzx0Y_gOmO6LESC8Ll-QFHqqzGxpiL3CdVpDZp-VHG4OFgiCyp8ilhN_rMN4-CuNFJZdPTLqyr7p6jpUsNwSQXvGvdn-uRfFYTgfaw5N5LP0N83J-Zv7GZMZnjD82nLFOwxCz01HGN15ZGGdt7DgR1Qc2bcIDjgkeA_sLJ6bIcY6LH7jWhXqTD6TwkgfeewYvoOCfe6g7jBFvpg7I9yZuXnFyFd6xZdv8Ju3Wwkqu1YPefVaWdtp2hvsZw55GbXYLnOauKQ3gZZLx_gfD5Y2AEan32Kj1LaBbS90Kvl0km8TJku4KRU7Lh1FHj0cbMSjfh1xSKRe5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2a99dfbcd.mp4?token=LiQ0NHchRtxzzx0Y_gOmO6LESC8Ll-QFHqqzGxpiL3CdVpDZp-VHG4OFgiCyp8ilhN_rMN4-CuNFJZdPTLqyr7p6jpUsNwSQXvGvdn-uRfFYTgfaw5N5LP0N83J-Zv7GZMZnjD82nLFOwxCz01HGN15ZGGdt7DgR1Qc2bcIDjgkeA_sLJ6bIcY6LH7jWhXqTD6TwkgfeewYvoOCfe6g7jBFvpg7I9yZuXnFyFd6xZdv8Ju3Wwkqu1YPefVaWdtp2hvsZw55GbXYLnOauKQ3gZZLx_gfD5Y2AEan32Kj1LaBbS90Kvl0km8TJku4KRU7Lh1FHj0cbMSjfh1xSKRe5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع رسانه‌ای از وقوع انفجارهایی در داخل یک پایگاه نظامی امریکا در کالیفرنیا خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/677072" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677071">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خبرگزاری فرانسه به نقل از وزیر خارجه ایتالیا: توافق شنگن با اسپانیا تعلیق شد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/677071" target="_blank">📅 21:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677070">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
دستور آماده‌باش کامل در تمام پادگان‌ها و مقرهای حشد شعبی
🔹
سخنگوی فرمانده کل نیروهای مسلح عراق از دستور مستقیم نخست‌وزیر که فرماندهی کل نیروهای مسلح را برعهده دارد، برای ارتقای سطح آماده‌باش به حداکثر توان در تمامی پادگان‌ها، پایگاه‌ها و مقرهای رسمی حشد شعبی خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/677070" target="_blank">📅 21:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کاهش ۱۵ درصدی مصرف روغن در کشور
شریفی، دبیر انجمن صنایع روغن نباتی ایران در
#گفتگو
با خبرفوری:
🔹
مجموع مطالبات ارزی واردکنندگان کالاهای اساسی بیش از ۴ میلیارد دلار است که بخش عمده آن، یعنی حدود یک میلیارد یورو، مربوط به واردکنندگان روغن است.
🔹
پیش از حذف ارز ترجیحی، مصرف سالانه روغن حدود ۲ میلیون و ۱۰۰ هزار تن بود اما پس از حذف ارز ترجیحی، پیش‌بینی می‌شود امسال مصرف کل روغن به کم‌تر از یک میلیون و ۸۰۰ هزار تن کاهش یابد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/677069" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677068">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f349f12e5.mp4?token=WiRfgUl3Nf389v0fdvotXefvd1Qx9NBFP0KEsuqNwa8ZutOVL1g3EpKD7nw-zwI98WstZQuIEPhx99mhKLrBjZQAQC4jLz-4sKRM2snZDpedzrc0FnKi1iS0xWn458aVb-h2dOh4lfxj_MEm9hE1BzyUdaq5Ir2SEWNAINhBlLHRqNG4Wp3x42F2HNG4p6XeA-REH6FbXopLuMX9QTzm7Z-PrEcPVbJ_13ue9WrpQMeqJoF_grkIT34jCMN8kPz9XMdTKO6W5z-K5TMuI8PBl3bQXXB5bCB6P23-vfFZgJRm_V1OSqw8DkzNs1PsilaOSiNn6Z012kVdoPSFcwVtGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f349f12e5.mp4?token=WiRfgUl3Nf389v0fdvotXefvd1Qx9NBFP0KEsuqNwa8ZutOVL1g3EpKD7nw-zwI98WstZQuIEPhx99mhKLrBjZQAQC4jLz-4sKRM2snZDpedzrc0FnKi1iS0xWn458aVb-h2dOh4lfxj_MEm9hE1BzyUdaq5Ir2SEWNAINhBlLHRqNG4Wp3x42F2HNG4p6XeA-REH6FbXopLuMX9QTzm7Z-PrEcPVbJ_13ue9WrpQMeqJoF_grkIT34jCMN8kPz9XMdTKO6W5z-K5TMuI8PBl3bQXXB5bCB6P23-vfFZgJRm_V1OSqw8DkzNs1PsilaOSiNn6Z012kVdoPSFcwVtGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف خوک هار به کم آوردن در برابر مقاومت مردم ایران
رئیس جمهور تروریست آمریکا:
🔹
اکثر مردم هرجا اگر بودند تا الان تسلیم شده بودند. اما ایرانی‌ها تسلیم نشده‌اند.
🔹
بنابراین، من به آن‌ها اعتبار می‌دهم (تحسین می‌کنم).
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/677068" target="_blank">📅 21:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677067">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac896a2c.mp4?token=qre9Ikha5JI1U7e9HRJyp1MWhMEt3v1110QoPNGJODDvxg-N4LFB-rc5zhieGpcruesajX_p18vbQvPU_0QPdG30BhvbJn2J6ffNUm2gR_g4xVrX8BH7O8ww6WSGt5S1ctxHXgf_2A13UnGixNShypTQBmYXKf6z4YFZYdP4-yJGXOlQSkmMMWq_wStYe1zLNeTrvMCIXiGqGMa1UhJZ7Gz6Fq10L5SVxiOBaszbV5MCGduFdhyfNIxCNxYQ_XEvBsDO16sZP_x9WXcgB_gIZGjhDTHMiXt_vEb1wiZZwDqbOdHjC5omlk6aLbmJVnuJeTKJhusQoy3v-woHbjilnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac896a2c.mp4?token=qre9Ikha5JI1U7e9HRJyp1MWhMEt3v1110QoPNGJODDvxg-N4LFB-rc5zhieGpcruesajX_p18vbQvPU_0QPdG30BhvbJn2J6ffNUm2gR_g4xVrX8BH7O8ww6WSGt5S1ctxHXgf_2A13UnGixNShypTQBmYXKf6z4YFZYdP4-yJGXOlQSkmMMWq_wStYe1zLNeTrvMCIXiGqGMa1UhJZ7Gz6Fq10L5SVxiOBaszbV5MCGduFdhyfNIxCNxYQ_XEvBsDO16sZP_x9WXcgB_gIZGjhDTHMiXt_vEb1wiZZwDqbOdHjC5omlk6aLbmJVnuJeTKJhusQoy3v-woHbjilnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
اما لذتِ خدمت برای حسین(ع) را فقط عاشق‌ها می‌فهمند...
#میزبان_باشیم
@Heyate_gharar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/677067" target="_blank">📅 20:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677066">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvNZqogJwY_UF-Nhgd_7cVLxZrVepay-q-DHIPzQTXCoHCQyf-2xnS8b6e5ba3xRWLoHtTbOrMkWbqLwcKqy259o3BBq_6rMoXLJ21G6wuHXomWubCtV5HWciJYFjl84p2JEkLBnmi_4LS3oZCAaxsQoZaPcGvm-NtHouR4uPf9Q-aolYDfwKqhz8nmF7b74L1MiQaTzeybvrUBKegKnfbwH_4aT2gf6QnodBLbgMkvLz-CByvstY4tTdkBOv809ZUsP9xSsyX6n5DDZZEtJNwYK0W4BOJ0HYy4eBYslZHcK6XhdG4xKXcwQ-HBA-kqEaA_--0CIK2VqzV0OeeOdIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بیت‌کوین به زیر ۶۳,۰۰۰ دلار در پی مداخله‌ی آمریکا در بازار ین
🔹
بیت‌کوین در پی انتشار گزارش‌هایی از مداخله‌ی ایالات متحده در بازار ین، سقوطی ناگهانی را تجربه کرد و به زیر ۶۳,۰۰۰ دلار رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/677066" target="_blank">📅 20:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677065">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzrhKfJ1HosicNqqKycn-Cu16TCVGujl1m16Cos1bEWo-ao2SRjdFcfZGGqBmMmjc76p58P9CFBEChbg1OYdt95qA_lODtuKYnMpCkeI7jYEvc_qf2Jf1hDbRkyvdnOqsdoKYLRzf_gMpvXoZip-3Z1Pir0NAXF1sScGqUS3v2An7DU7E6j9Q28NBqwhunS7iSWbu6WJaUa5jERlv0ReaSsdsCKC1jG_6QYV94k-RVGMK1G64c7x7ojGTEOmAAnqQoCaVFV2maMikRulpO6Klm27i55lWP7v6E6B21rv8ohfIQFKZNOvWb6I5Pgv5ZpAtihMOmBAkWodX7oI6_RcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امانوئل مکرون، رئیس‌جمهور فرانسه: در پی بحران مهاجرت در منطقه سئوتای اسپانیا، نیروهای نظامی، هواپیماها و پهپادها در مرز با اسپانیا مستقر شدند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/677065" target="_blank">📅 20:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294f7820ea.mp4?token=rc3o66UXUw4oC2cKxRghKcwIt2Nb4tKVoLe12Od3YKrrnAIjmKmW8ciZHrd0c1C28B1IJgWe32A0LQbQkb7aFz8EKPGipZHUe-DhJrayX2YZrKtclaEK5Q1PzEMOfQLmt7xW_dswC5nqIay0xmXaX0QXBvv19VJcjwluIaOFJupTatETgjUxyHvOzAdhf9S-etTV6QyQVIckv5THuy-uaP5GrMlo6APfXb7LePHPcYvAPJS_XfbssSJhRc2tdiA8UZxAfxRQyeET9KEkXw6mnyOMJXuHhvtqdU5MMI-ePvUW82d_ucycJdSQgipUm-D1GfgVpyMVWDmgVKyxw_447g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294f7820ea.mp4?token=rc3o66UXUw4oC2cKxRghKcwIt2Nb4tKVoLe12Od3YKrrnAIjmKmW8ciZHrd0c1C28B1IJgWe32A0LQbQkb7aFz8EKPGipZHUe-DhJrayX2YZrKtclaEK5Q1PzEMOfQLmt7xW_dswC5nqIay0xmXaX0QXBvv19VJcjwluIaOFJupTatETgjUxyHvOzAdhf9S-etTV6QyQVIckv5THuy-uaP5GrMlo6APfXb7LePHPcYvAPJS_XfbssSJhRc2tdiA8UZxAfxRQyeET9KEkXw6mnyOMJXuHhvtqdU5MMI-ePvUW82d_ucycJdSQgipUm-D1GfgVpyMVWDmgVKyxw_447g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ زرد: میدونید موشک‌هایی که ایران به سمت‌مون میندازه رو چطوری رهگیری می‌کنیم؟! اینطوری: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
#Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/677064" target="_blank">📅 20:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677063">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
سیم خاردار بر بالکن‌های بارسلون؛ اجرای طرح آمریکایی-صهیونیستی برای آشوب در اسپانیا
🔹
تصاویر تازه از بارسلون نشان می‌دهد شهروندان اسپانیایی برای محافظت از خانه‌های خود در برابر مهاجران آفریقایی، بر بالکن‌ها سیم خاردار نصب می‌کنند. این موج مهاجرت هم‌زمان با…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/677063" target="_blank">📅 20:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پزشکان ناامید بودند؛ اما او با ۳ پیام مهم به زندگی برگشت
🔹
00:09:00 چگونگی جداشدن روح از بدن و تبدیل شدن به یک نگاه در کنج دیوار اتاق
🔹
00:28:50 التماس‌های عاجزانه مادر به زائرین حرم برای شفا یافتن پسرش
🔹
00:38:15 درخواست بازگشت از دستی با هاله‌ای سبز رنگ برای دلتنگی‌های مادر
🔹
00:42:05 گفتن یاعلی زیر باران و حاجت‌روایی
🔹
00:51:00 متولد شدن و آموختن دوباره الفبای زندگی بعد از کما
🔹
00:58:00 درخواست اهمیت دادن به مادر، خانواده، نماز، از من در هنگام بازگشت به دنیا
🔹
01:05:50 تغییرات بسیار زیاد تجربه‌گر بعد از تجربه
🔹
قسمت هفدهم (دوباره تولد)، فصل پنجم
🔹
#تجربه‌گر
: سیدسبحان حسینی‌نژاد
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/677061" target="_blank">📅 20:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای رسانه کویتی: ایران به ساختمان یک شرکت چینی در کویت حمله کرد
ادعای تایمزکویت:
🔹
حمله ایران، ساختمانی که متعلق به یک شرکت چینی در کویت بود را هدف قرار داد و منجر به مرگ یک نفر شد.
🔹
مائو سخنگوی وزارت خارجه چین گفت که این حمله به هیچ تبعه چینی آسیبی نرساند. سفارت چین در کویت پس از این حادثه از شهروندان خود خواست تا آگاهی خود را در مورد خطرات افزایش داده و اقدامات ایمنی را تقویت کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/677060" target="_blank">📅 20:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXBViHA-4dvH7_T8_ZOVN2hqT9yd_1w-Mik5sdGculd0bXZcHSxstpmh4caUh2S7RsypDHBfoy674o6BfTfBrWKgY65Z095CvqaiS9NCIGt9RNmdijlInRTiBM-f5fS8_byBsvLAvPGFTys0kAP_4czmCJpo89jZPImQgeJvwh6bYfcMzi1TSwbhh3AcpFHZMe8kam5snNSPGrXiTngsidyTldi42djGgVYaPMAPx-AA2G_1FXQ2SzHfcv9foEHT5Ko6sVqsT3PmJGmO8kQHvy7_-DxW9ftkxd6rCpe9U0Vhf_bV0lnrpBYHnLTNcMOdb8tXGwMjeMb8Vynuf9e67A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کشورهایی از شر بیماری‌های واگیردار خلاص شده‌اند؟
🔹
ریشه‌کنی بیماری‌های واگیردار حاصل دهه‌ها واکسیناسیون، مراقبت مستمر و تقویت نظام سلامت است، اما بسیاری از کشورها هنوز با برخی بیماری‌ها درگیر هستند.
🔹
مقایسه روند حذف آبله، مالاریا، فلج اطفال و سرخک نشان می‌دهد موفقیت در کنترل بیماری‌ها نیازمند برنامه‌ریزی بلندمدت و تداوم اقدامات بهداشتی است.
@amarfact</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/677059" target="_blank">📅 20:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677054">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDdtGIIsTDbwugZEf4ScOCRoarQsyPPO2Vt4krh7ofXkPVHLPVFK8DRW0I3IWHkNC-jqvM-iCY-LsVbATmjOfLREovUjXfuguusvUHwCBS0OBQw_uJqG3uBxCDkBd4UNnIq29lkGjYzWmCmqfjwsDRSCXjnvEONHQ1kE5sHQ18pCbCIsirCw8TfeK__49LhaRQu13UrZielfA3dxLciUS-YDDCjyihKfuOurSeIGEVaspHdg9ha4v56yKQLAXT932pUGc-0qqr5hT8xNIVpxHxAEyNDQYiYyREyoVb4n9-g2u1DsQx_bjt4RnXPSzAw9DPDRRN54Kqh-F7DPK95kiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/677054" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677053">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb554c3360.mp4?token=lNgDm4_BX9oHXkdIHYOPbFwpRnDapw4VlT_OrAN3nKe2a5ZybIVerSEzVxBUV20ycLJeSo0_9Fn59OWU_8zL17djLGXeciogTVMyQ9VwokZDDk-B7H1pFO9Nf4tVjtl8Kq0K6FyxTG0S2ymwPOPWTqDvO9cNqo07c_LdA03wpD5xKeACz9VDBYSqUcsueBqhxEukuiNMwd2JU7IrgGvfFrVj0yYA3sAuMr5lXOMX-limoRgSDChn-3EBQTpG4XKlxQfFb1F6czJmyybZbBtNLGSDm_pn14WT0cVwUj3FG80A2t6Yl7sfnQbGGHe5o8hwdR57BYsnKI3Q9RiKZXqlWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb554c3360.mp4?token=lNgDm4_BX9oHXkdIHYOPbFwpRnDapw4VlT_OrAN3nKe2a5ZybIVerSEzVxBUV20ycLJeSo0_9Fn59OWU_8zL17djLGXeciogTVMyQ9VwokZDDk-B7H1pFO9Nf4tVjtl8Kq0K6FyxTG0S2ymwPOPWTqDvO9cNqo07c_LdA03wpD5xKeACz9VDBYSqUcsueBqhxEukuiNMwd2JU7IrgGvfFrVj0yYA3sAuMr5lXOMX-limoRgSDChn-3EBQTpG4XKlxQfFb1F6czJmyybZbBtNLGSDm_pn14WT0cVwUj3FG80A2t6Yl7sfnQbGGHe5o8hwdR57BYsnKI3Q9RiKZXqlWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: چه کسانی از دولت با ایران صحبت می‌کنند؟
🔹
ادعای ترامپ: ویتکاف، جرد کوشنر، جی‌دی ونس، مارکو روبیو.
🔹
خبرنگار: آنها می‌گویند که مذاکراتی در کار نیست.
🔹
ادعای ترامپ: آنها فقط مرا عصبانی می‌کنند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/677053" target="_blank">📅 20:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677052">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای رویترز: شبکه قمار غیرقانونی ایرانی به دور زدن تحریم‌های ۴ میلیارد دلاری کمک کرد
ادعای رویترز:
🔹
یک صرافی ارز دیجیتال مستقر در دبی به عنوان مرکزی برای جابجایی پول غیرقانونی ایران عمل می‌کند. این صرافی، شلبیت، یک شبکه قمار گسترده را به رهبری دو اینفلوئنسر جهانگرد، استخراج بیت‌کوین و بانک مرکزی ایران، متصل می‌کند.
🔹
شلبیت صدها میلیون دلار ارز دیجیتال را به بایننس، بزرگترین صرافی جهان، ارسال کرده است. شلبیت مرکز عملیات جابجایی پول ایران است که از طریق آن شبکه قمار، بانک مرکزی و سایر نهادهای تحریم شده ایرانی به بازارهای جهانی ارزهای دیجیتال دسترسی دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/677052" target="_blank">📅 20:01 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
