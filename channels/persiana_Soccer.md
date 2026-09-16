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
<img src="https://cdn4.telesco.pe/file/l0oCevYuAzu8-6evub6TXK_nCnwt-wU05fsP3PBBF6K5Qx4mntzGR6pQlHpTd-Ghb6AixaLqtLNchxwmp0NFA8y3wt7j_1p4sFU6CNbZhs6TKo7G0JHYzV4-rQe5--X2S-tsu8_ISxZwGG6pL-ts6HfnNZCxHMS2iqkz5ZdZUuHnrb96YX4mdj4BEJZGMlOvzQ75uVF17s6QIqIL4HSmXLt4esf14-j1ZlKjoYyRQRmnF41KOjiqnHjlNYRwfvTDXzpTI1pZRp7IhToU9CvLXTKGrvegZkEPJIFxnZW_IWGDSY1UXlpsJwbDUJ6QykCez0604nZy3Fx6_9-hI12Jzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 503K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
<hr>

<div class="tg-post" id="msg-29886">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDti5yAQV-m6fhpR8LXcuf9GkwZ-GUXEbheiWqjH848L48nP1DAZGaU5KRjDlFi47cFgrgOPFo7b29pzL0fZ1tPLIl0W84XC9Q4EtTFGbK5ipDJ5dIIurnk8PQgfWo0piSNdpBJ9DZJIDmlbUUBAJ5Tnyfk3m1S34t45ef_CkB3r_n2XpEyZ3APNLUyuVJIFOLSWIzqG9KfQv6tmuv-BU0x0D9UbSVgWbY5VX5jkkYpx2cAemM46G-O6bhPRMyuB-YfdMUCtNKWYF2ekxrQVKoLBDJVQKODQ5HiBZbJYhy4GXi0nMjUrIy3GLWEmmGk7M-sjyFObLRePu-JLNNz_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/persiana_Soccer/29886" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29885">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R52eR578eXpklm1FBIV1GRWuBM4aIO-6e0nfOOgLJY7Djt-lnr2aaMd3UOAjbSycLY4Cmx9ykppCNjhCJn_KPCtgnOzWropd2a3igS-h2s_I5ZFb3x-Z5owrydKOGbXe8om8svqCnBQA6QyT6ZzbEFOrW-wfyoD9WFFAKAbNqLw1Zk-zI56rk5hGkmY4eCG4JewKaIO2179qu8N6QXpQnUqgUHfoJOX1SHLXa-coksuOTdDILptnljc4ZQcDL6btUJFk7NvRKq1nF9O4pkWp5uqJWDwf_qw_vsJK98LKIRC8poIIMnaAkwjlUigI9RHu6Z7BQSL_Q6wOgAFJqmKo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو: این زمستون رو نبین ما هم بهاری داشتیم. افسوس که نامه جوانی‌ام طی شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/29885" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29884">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1SZcH2z6WMjk9oPYn-QQ-H6VY6KAb8-t54_3lAbsbv6qIrW0scf4JKYmI-hSQEN__-nejYfkb6EfSQv3eWfK9QDbZ5fjbD3Tw1zBjnnaFtAWK6HRdf8pmHmE-0uVnXWZSCO5m1AkRc3X4CSFg9kH6kVPBS68haBB6JmNbQEGsy0TlCiKQrXzlRz9ux7DRhiUb0k3mfLlTnHfsEthevUQqs2n4ptKm5j_oOFBDB_ZHyfkhPc-qZUSlcdMU-pITpJk_kiM_gP90rKBiz3-BH5_EUGAxVrUhb_IHkyqFvv56nIcmiVEwSbpVEl06OKh5sPDkaaY64IpOM0L2M3CJJcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ازابتدای‌این‌فصل تا کنون 17 موقعیت‌گل‌صدرصدی رو در بازی‌های رئال مادرید از دست داده‌که باعث‌شاکی‌شدن هواداران رئال شده. پرز هفتگی داره 600 هزار دلار به وینی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/29884" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29883">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/29883" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/29882" target="_blank">📅 17:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت
؛ علیرضا بیرانوند، داوود نوشی صوفیانی و فرزین گروسیان سه دروازه‌بانی هستند که تا پایان هفته هفتم لیگ برتر موفق به ثبت پاس گل شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/29881" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Utuex_a_ANeu6HGDsuJ7IfnyNHMCgCtyNWRNSmZkm5FdbQsScxww8kCUrVLglsUmCqGAKDxqO6gemXdm0ivj_Azq9JIzrUuwUggUeHEURh9WLNEenvkbLjzuokMbHixfb6Im9cotzOnMWDOYNIf-WdO-DO2QMZoryB5lEjppK_YTngyS0e-MADzoIvciMrIzyes5jG0p9BSzBGM1ukOnLaa_rkUvrYt47FAZVZXmua_bBCZE-ILfHSzaB3ktZ4wMDz4HglaU9NlQfw5C-46ymQl7Mv2R4wcJCJk5zhm8X_VpOCAYkwoK1vkmRS__fqFSK0p8wroiW2Yo2IOgFSSHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان:
یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم روزی کاری میکنم هرجا رفتی با افتخار بگی زلاتان شاگرد من بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/29879" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltBCX1xXLJYktdvEGNgkp40J2FTulOnXHRVQ0D-wSzxXrcpdul8UbinTVXCV5B6pYDwIRscTCZPueQyI7ywBalWnyLVR1meRzkpy4rz6vN6yb7Tw9jvfoprWDcHF4RrfsJxrtzpLcYCXRnadUGiGBnptGEKcPKnKk4Q1skkBbEGd-ut0CEVmI4IOiTia1nICO0k0jdCNu8n8y103z-p05KlbSPMXzQfIa7HIpiYDUrGEOepI6eo3gKKSeAd5aYml6qtNCFZeMVQcNfa4pIl1oqhs8I-BmBONomOsYTI_JbLBrvLDXOs_6If7zHV5n1KJEe0QJlRI9nAo70C8gQTVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌معاون‌سازمان‌نظام‌وظیفه؛ از بین قایدی، حسینی، قلی زاده و جهانبخش تنها کاپیتان تیم ملی علیرضت جهانبخش معافیت تحصیلی اش به پایان رسیده و باید تکلیف سربازی‌اش رو روشن کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/29878" target="_blank">📅 16:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf87MZ2OL1TQR4cSkxAKjb0ymmoMDOMf_YHe-PyrSGhjSx-Lne-hF5CigwSchuzkAIYN_ZU_5oU1o6ShTRXn_y3V5TqrFXZuy8wFdMBTa4h51xTqxAQ0wYsJ6o6GbY1V1R9x3Hh0EP9BoY7-_FHEfJJ9cew03qu1EReF62vsOcsgVlpRwNp7TcEVay42-5XyJJpoJeXxJjYqMdGVnM4Vb_lsNCxTWjfkZm4UBNWSQiNuLsYodabtadNqcvil3_VCn_qammMC1gqerXyuNrWpbG6eKZjeFxqYC8JUKytFVrwvMypFO9TF-1YzjRvJTJIn8BlyozHUw_ysCslbACEHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29877" target="_blank">📅 16:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owgrbg0cFAmSdBuYttNyhlKVVWd0I-u9dwLuNij0GsISiUmaH8jQOK6OlHMU7Rrb-t_nNPEmiPUYPxXwZn7OlnQZ10DRGgS0iEJa7Wy7JqLyiBzWsnpU2Bg8FVs09TNDw6YnAguN8VC81DuPK9FA-U-8d16aKclfpAp8ccMqFoKVC324j7qTsbKb65Dl3TZlB3yW8lFY73DReytlgxj4WBoR9rqtNjDssd27Vrv64YewomZ-f001lw3GCm9MVvYRwvI0fN91tmwCxE8m7dn4obJ5eKk0kEWy43xH7zpj2CVXxQ06ozm7sYfLVe6O4kTFLYFF0PCsSKsOerDGtLfydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دوتیم‌آرژانتین و پرتغال به مناسبت خدافطی فوق ستاره آرژانتینی تاریخ از دنیای مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/29876" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky0wlvvfXxy1pEfYdvB10kTWR2QN0EZLZQXrZXa3UDUXxnYviJfh4P76BXcmFNxE1NVtJFA6XIkcxE-8-VkwpUX4ujnE-EZQg8-Pq1lIgj3LvFQ4p9TJZAoFnxc1thUuD4Xt9-pGXOGLPJj4y0uDDCiMVgKyjrwCJaPZvRHjc06XX17gXGqhqqtFalfRO04t1bnIILqO8t56DA-BLo6vtZ-n6tdMd5I0ETigjNxZfmxQqp-4wcPK9-rFDLJxh0UVk7UW-bnBcPNkvKybADY2cfrqLprNZ-WzCLt0HLaoN6e_iFrh5w4AaYL_YDB1wa7IwMMAsLfa0MiU3_XYW5qb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/29875" target="_blank">📅 15:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO4jGbua6eV8GP7MxEGIEKIp8ZCmvJKyuwepzTX8R4BekZm-Xjk81bggqcGap2WIqqmSqIPaoJXYOtNqmk4cKczPsib6oJn9dZZ1R1DIs5bn75Q4Bc1h9IomPlXks47jIlkZ9o4C6qjv5zyf4nT2xmGvhbIHxHlEmfiofiQSOKFCyl4bvYoqhL4AaXqYvJKQQc0HhJlHtxsiSvneGlU1jxJWEa2VAbXKAUOcMAlyMhclv7ulKTmKHrrSmBGGDyDpwO7P9p5ZpRbqRKVvRbI8TFTha2NrU1A2Z1vErdOjZ6D0oWdrJtTLNfmyq90sGQPVqdsHOoIKCPBFKMgq7L1H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29874" target="_blank">📅 15:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHsgxYSBianWCEP_M-prFpkDetpBPvJUs2BBNDsDdEjkHSeHqAlzgoDJfhOfWWPRUsso0tI4IWZfGhdp8OGWIgfv6KyfLBumR3j6It_jbpHQiwECPsuMfDmlC8mRietZPSBrv6DnFgKwyH5Wzh6shaE-Cwxgegt5W-9HczGdiojVukv1ThccuJRZ1hVIHFJ07TaZpf8FsXxI-itBI8C-ihAnzShvTGXQTXKNLxMYPJc9-iPxXw51zIyUgv33GULHr6S9x0kmC2kCRdZPpXTZgQeCR8SxqSPfPZUV32GXA0soJDv0Q8hW1GxPPt__BX-ZDZcaT6-Jz43QJsq-cU0qMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29873" target="_blank">📅 15:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flRs-VKEfqmH40Nyhte9LZ7WrSMSeupT3HXS9I7q_1bdjF_pFGDDKDEYrNm-rR9T4pDxFoyOnIIYxnUsx30guDnvZxAru3CCkXpoUWcnEU9cWKkPonHWZqj-dGJgWUQ819fIHvLB5ojLyVqWHe-ye_WmDn6j6JziPBYyY-gtjLxGA-2gRejUcki3gKJSZEp5vX-oGrlEedqkvXMX8snaJRZInR9x-vEBafxGPy5TGLa0k3SBP81tzXJGiN13O8-dUSW78mpE_d9R-Ac3FQsCTHBejko2q08TeegBHPF7m5vln10jubijnoMy1Dq5mpCU88VphqXYDP57l-T8iqac7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته ششم لالیگا؛ شاگردان خوزه مورینیو دردیداری فوق‌العاده سخت و نفسگیر مقابل تیم قعر نشین الچه با نتیجه سه بر دو پیروز شد و سه امتیاز ارزشمند این دیدار خارج از خونه رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/29872" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq1kWI_vjB0p3YRv8SJV8HJs1ad4_cyyNWTjERETplrWczGstwB5a_J8QKhIGnt_GAE4BjMECWDc4L8l40GMKLaQXi_6uFp1Lppp9JwE0zv2ZOEwHccKW9A8unQo4Rqkx0qb2MtkxrYsAFobiCr6V6nNc4JKR3-2zjVr45TaDgSy3Qyi_6rTN_I47ON4BZJ6jf-Rr1jTsaUeqWxVVzi2hS00DoQDHC2vg9S7ej2lcM6Qxh3Sd8VxqXMl5TosoZPMYlB1czKKZ6J_JBDMw1jMRbrY6Gz3hVOh51iU6q8CQt7g6ah2iVqmv-tZSYAcgv0DA9U2eQrn89SCiK-C0tgCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/29871" target="_blank">📅 14:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29870" target="_blank">📅 13:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoXLaFD3jGyLd5m1D0WJe988ZQ3-XzpSzuGZfwJBh3rNbiOHY_rRaxycl-Q9gMjXOUR37HY0u2MOQcWhTUr6E7mScuIE1JG-nbF_s7K-kgD5jzcFhXe_wIumjYwV5SrbJxOM_2YSX_5eG-HfIEsByKLYw7SVP3VZSEzhTfOFFLzVNf_Poa6ZqaDWfEx1aBzAxg8yAeiNphksQh3xWwYUudB_fAxTir-y8UVsBs5ILGYIfYuWLQZo9ziUcIB5Gkc0rJk1FJUCZJcP2Czm9wNkw7PGH8JmgoVvY7mUi51p2F5JNgjtw3feafCIMzprrY1I104uJGuBRjahd5Ewcx_sIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
سهراب بختیاری زاده نام دو مربی جدید ایتالیایی و پرتغالی رو به مدیریت تیم استقلال داده تا با یکی از این دو گزینه برای دستیاری او در استقلال به توافق برسند. بختیاری زاده اصرار ویژه‌ای برای جذب دستیار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29869" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29868">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRm8Dl42dBusc6xs7yVj8SkK21Gv_QhBRjBVUt6XyZUTqOmmq-yKkrzs_cbQDUglENNkn8n-ME0qkSQGlTFmEN7eHN37rpPtQzF5hGfdtBlv3yyeZRfo9VjCNyhmhJ1N8XwwoWLbAI_cq-oLA9b654QWEgge0E6i1_Kx9HpPuASq9_INV22uDG8th6fg3XtPEgwO_MaFzPapFwuf7Dma8mhJN-O4kP4atfthRtRrO6HNlttJCSl3LSI6nYh6RkkDkSXEzmr0L6SgvO2O6ufP103pw88eyXSzjLglIhmHyg9YWGQLbLQvdgZK44x5pR_VYD9T6a_dPTdzRnXQ95QBsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد حبیب فرعباسی دروازه‌بان استقلال درفصل جدید در تمام مسابقات: 8 مسابقه، 7 کلین شیت، 19 سیو، میانگین نمره 7.9 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/29868" target="_blank">📅 13:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29867">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX8mfiNUjrBY46_ln8ITK3l5y4CiR6V1vYsOhLFt8F8_BQIzzenIH5-8XHXQ8iPaDm3dtFKT5lclAwv7tbtvc3OIITLdv2ACMHQ8RWButLmAoWqhcWJE27-MTe2sAU_hCyRdUNY9Q6UhujHE2dWK0GKUqJeqW-WjbvciOGHYjXQTJRezCZ7iHoshh9JZSWkJezXIcHGEkkHGQpS3GjFZWx4cCxqJQ7_BXCVEwfkkxUgZ0lVQsvtpgvdAzEGG2m1pn14rmFTXShteBbnoGalZ6Z4F3-i53D-0TO5nOhKo7pE-Ft2Z4AkXui4C7cjTruPOEBYDu_wqeAGNbPuFXGrSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29867" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29866">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/29866" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29865">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxMt0BVO8Y2CDkOZ0dKJu3wey6ETgSS2ddAMCYVlSpJC4179XMZQARiTaDXIbOH7XA4pChx5uRAO1diM-_VOh4nDvP1lXJvKMbLQ63WUJaHGWik8Afn0qc_NNDQy3q3N1PKy9X9KtzQjiUFuN2VEIC_bHjkh7TcE-Clr8YnGdAOOEShviiVvgXa0X_hoW5D7e0_v8tvNLM-w7vANwaus28b7TJROYHLLeRc1JeX44Nd-d0VAUkJ77zL_Y7_q30hakTLwYcGQ9KpvaT14tQmXLVGjcfj1lOFnhGl1ceVAqsU4Ec4aX50hJ-w-5qfuvUwJKvin3f1WjCjne26m5o3NWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤬
گردونه شانس پین فلک
👑
هم برنده باش هم لذت گردونه رو تجربه کن
🤩
واریز کن
🤩
ازپشتیبانی کد رو بگیر
🤩
گردونه رو بچرخون
🤩
بدون پوچ همیشه برنده باش
🌟
جوایز بی نظیر سایت بزرگ پین باهیس
👇
⭐️
آیفون 17
⭐️
ایرپاد پرو
⭐️
پلی استیشن 5
⭐️
300
💵
جایزه نقدی
⭐️
و هزاران جوایز ارزنده
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r25
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29865" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29863">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THiQ7essGBwDRbFHjTFrXBRQ6WyM4EyMX62c4IyihdANdWiLrV2Cd0hWlSARsivE3quT1909SpmPKppTYs1cevr2mWDi2BDCB-dljEn-yyo022ujXymdt6FA0EqSvagjKxeOnXS-ypyYHbWHTKeglldnftLHCZ32RpWPH5avd1UpxVj_UpcB5vV44-Z8iRQ9XcY49ywEVzNgltOPZiUTHP27fAZHe2jrD2-I_86Qp6qI2EbIThiXIfuPDiUei5THkut0MazvpL5pTPdy_B1_Lip6MGUxKKgwNWpwhdoZPCZVwTUqAm_kJ-mykx5KWvuEhTLLyaBdjqKmB-OlWaNYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراکتوری‌هایی که در پایان فصل قرار دادشون به پایان میرسه:
علیرضا بیرانوند، شجاع خلیل زاده، محمد نادری، کریم آذر، دانیال اسماعیلی فر، صادق محرمی، مهدی شیری، اودیل خامربکوف، تیبور هالیلویچ، مهدی حسینی، مهدی ترابی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29863" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5t6oAzywEFCDsE5-OBMu7CtJ7VXyS-FRjxFPe1Ic3FcmRZidnotItHGfBiMCsZis-r2trLlr0OLrwQipoobFRYG3vpfN3Js8FAYVswzYyuqsHZfmajKnEnx8Hky4G-SKMLitIj_LSq8DuIKp3tybxGEi5Qwhxp_4hTKDCr4y5izu_-C_mq2CbUFu2xiSb4RdwACkWAUziISP5awluDvSkYfikV6CpoFlkw9Gx3vxRXkWlKjFU5CLPwhUJaJak1PpCg-YdBWt0Ye1Kwu39H-e8s8hxNWfIjyrJw6F4INrMsqi4P1rWBVKZiV6f95_oRer_M0_jufJwFoeAHVY4Yk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه:
محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29861" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29860">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJPjGIjKOAxmiC9WlLWXtJEKOpjzsb1u2rG-ZSAiJCogwagtPvCnMubSHYwMMC9iQiLjphJtNrs8JmdnwJ_0MGIyd7pkbLDXpDF6PEqKxwlB3vdUf9o1p4_aSd5yaxz1gVNxzRZokZWhaRuiyHaKIeJEqqCnjXS6n5VgLNGxCNuq7gk1qM-JsL5MnFLVgHwXlAVtRlzQmrCsXld-KxzZ_NQkd7yDMHFTiAhQ-0SY6ImpWOLaOSs2zuoJJ9injZDxvJxFDc6DPbxvlwsTNA44nr7xKANbwrVKg5R1fImG9s7ieHVq_xf2pM8iUtBbfABZLUFWyWuW42ixMJq4GiSC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29860" target="_blank">📅 12:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWldIdBKC-c4_cbgqqIVnBkZFVh8gPViMZL7jbxDZhtK1mySdo8tj_97lapDnWzMLG7KCuJjOE4bxVTLEjKAkydcbaTFpZUKUwRto24pAyklWdd8-4er7MblxOF2o0WS_ogapRgaugDjCmpP-9df-qdQLTOxVl3WbPv6AfWJnGDyA7tUlp1F6Q9CU9C4SBmXoReZrt7Ny-VeXtTstT1pHYpY9xUeqMaZTA-oMbCYd4wanUE-QqPL1D9nbiEDhNAd29SQtxlLP15sxlR7sjiSZ76bJij2A2cCsB0F2Z49joCR0tPRciTzyIocjKs-SHl5cL0Xb2qw9SOtcckzv2QzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه:
پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه. بقیه‌فعلاحرفی نزدن باهاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29858" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ula_GVsUMOda3StiP63AJS4rLLPjz-SvkHem9F9mckdgQWhW8JnMnQKuyo61vHUkBPlac-HedmzpUcxmq84BhZMUghXEO9Uf2qPH43rWzh-HqOHjZGhWIitdZxQ2JVP0putgit8FWCX3XzLq2MSjHbm_AlU3Feiyh0LpEAsAHXR1dRWCdpkGAwbWTrN8WCsLPJJ4-eZB8MA4yhYbtjKEJbnvimkJUs_U2hjvQFpchEOLVIZbtQQASf4rObTBRKKjioft-9FoI8b-8f8PL53P4xJUdeniCR_apgYmGiZElQReFXYv3Osh7dOixhDpNQ-MGQBlp3IxwjkTmQQpK5lLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
فابیان روییز ستاره PSG
: اگه توپ طلا رو براساس‌تعدادجام‌درسال و بازی جوانمردانه میدهند خب‌قطعاهیشکی شایسته‌تر از من پیدا نمیشه. تموم جام‌های‌سال2026 روبردم. تو زمین‌هم‌همیشه سعی کردم آدم‌آرومی‌باشم و بابازیکنان‌حریف درگیر نشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29857" target="_blank">📅 11:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
⚫️
آنالیزدقیق‌بازی‌استقلالِ‌سهراب بختیاری زاده مقابل تیم السد قطر در هفته اول لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29856" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDP5-7CCPW07vFXZJ_tET7IuOPVGmTW65LrZUJ0A5vd3XWsxAXlcpJHPZ4HGaXXLfzcq2DB1EaQlsKukYhMnuYdO8rfPs2ea_Fil4wGP5NIDRd3b6njUjua1B7cyI78X0Y_Wpd3jAFi1PKWAwxPoxqtLfms4zQkgpGE2vwtVoDkKXiU8dOrA9BxOzU9WCn_WDkinltZNJYrWvM03iqKsBExeF_gIV6NX9ls9S7hMEGsohOpr0R4hD-Njq93OP1HKspyW-7MDZhQe3jwEap0pu9DRf1p_kuqNLZ_wPgjZtwcKs5yUOyEwM9gm1DFwZdMtUHI9oqmkGurr6vOkugPByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه اتلتیک: به احتمال زیاد جیجی گابریل ستاره 15 ساله منچستریونایتد طی روزهای آینده با عقدقراردادی10ساله به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29855" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4KmUHs5y7fkMz53oiCRHISQyWbhi4jAJTTG2N_oblwqCrGLuQ6pxnfvbrqXvEQ1QqfZVCpneH5-3PaeF1kZATXFVZcgSfgMAbToRDlfW4hxFrBREf2o80-AyBq6iTEsW0XSUEhWTtPtEbvIuVuSNsI3eVw6wdXda1iJTwEj6yK4Q6tjDCgVOzec0IX8g9O91GdMut_P2Z6V1kT8iv8yf85jlLbasGz2GRhrR03EkBzBvn8_Vr1FyGQbYui_ca6tMCF-NPpepDdk9rqHrh9bslfrkCZjyMPS3gy56mhX9bqdjEYWMhGMNNbjdYK20HrbFrS5m2Yv31F-2ZpqxnMdqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4KmUHs5y7fkMz53oiCRHISQyWbhi4jAJTTG2N_oblwqCrGLuQ6pxnfvbrqXvEQ1QqfZVCpneH5-3PaeF1kZATXFVZcgSfgMAbToRDlfW4hxFrBREf2o80-AyBq6iTEsW0XSUEhWTtPtEbvIuVuSNsI3eVw6wdXda1iJTwEj6yK4Q6tjDCgVOzec0IX8g9O91GdMut_P2Z6V1kT8iv8yf85jlLbasGz2GRhrR03EkBzBvn8_Vr1FyGQbYui_ca6tMCF-NPpepDdk9rqHrh9bslfrkCZjyMPS3gy56mhX9bqdjEYWMhGMNNbjdYK20HrbFrS5m2Yv31F-2ZpqxnMdqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌دیدارجذاب امروز صبح دو تیم امید ایران و امید امارات در مسابقات آسیا که با برتری سه بر یک ملی پوشان ایرانی به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29854" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/29853" target="_blank">📅 02:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛ صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/29852" target="_blank">📅 01:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBdJGP1Wfq1vmsMHEZIYOaDeJmZD2sLOsgUXKLbGGMHEw0RGHG4BWtf3AVDw3K4tTBJQZE4FRx46DWFsdRAsYfdj1AIE6SgawgbMxsdYpytO_lw4LnMgDdQ4oOmZz-W5zg0M4POHp3-VUkH9N8d3wxMHfwWQ9POvWPohWMnSUEFDVmQ8N-yRImIHM4oAUAK8iCTkNy-8i9cAABFnYoV6iifagN7z1GO7yQ9HCv5z1-T0wazRPinUJLMkoWAgFoEsU73ZT3wcLVzAaOkUha7d5Wx-RdbG3e8Fo8QldTaGWCLav1sHWXkaohfeD-JzzOf26zpOcDysJZE3-fbO-pQ1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ از دوئل یونایتدی‌ها با تیم آماده برایتون تا جدال بارساییا با تیم تازه وارد لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29850" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29849">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeoIi57ehT8BpiOSLCOXU3wGISM52GrXYlyCbzFax3WzZ3nEs1lglW6fEm1HA0wJzFNpPIo5oXUt7EyzZqSIcm-qLAXvCeCrru4bzaauxec8Lpq9mKdlw0zDLB6tYkD1zKV3-GOPggmG8lwVibvQ3oEn07VVVKmq1I8UXutyEyx81ryfvqi_J3iRAq3-QM9dvG_c49lq7GPfEEcx72hl3afMJsEJta5kSO1FezQt2sqzeIj-oZY4RyA8twPFkSPtMnqfSn2RSHMnqCjx7KkLm4sUpa_cZP57v7HfTipXp51MIeHPsFpeGXMz_KTbThFZ5x441RWrnJeLl9B57rb3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
رستگاری‌رئالی‌هاباگل اسپی و پیروزی غیرمنتظره العین در جدال با یاران رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29849" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29846">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCimgnv-UdOjxeBCN1JCFGQPM7mcMtng3yzhwqGaeTg8RbbrnOqyq4WG1dZPuvtmoVUu1mbF0NovfOETSA5apfLXgbDEnG_BfwB52MK60B91Dql36ebKPcl8PI2RZs7eCK9nuA76rSkWdWYMGEvg9k2XJrFMZ3Eyn7tNIV6kwWbKEfiYdk-WHTmsrNhdJ6CV4uXqc06ZEXctvCUA9HwhGa8R9EK_0SdY7s_bflgKli_Nmz_5Z01RBHM9Rx2QETwnqw5o3qqt-g-12HfFNaes278P2RsJHycIU65gngai9DHhc4OEjTuWjyHJSbhmCQIACd5ZDLLr2aM9vgIkvnVXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ مهدی تارتار سرمربی پرسپولیس امشب موافقت خود را باجذب بشار رسن هافبک عراقی 29 ساله پاختاکور ازبکستان به‌مدیرعامل‌سرخ‌ها اعلام‌کرده. بدین ترتیب پیمان حدادی بزودی مذاکرات رسمی خود را با ستاره سابق پرسپولیس برای بازگشت…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/29846" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29845">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw57bTXuAjElbw1gDPF-xO8GSiS_2_jZ2qgGon4aiRO87oDahMxVp8iOh6UXxxrEsPYlM-tJKAuTajpPPA34B9inkjG-4PK8rRUREMWwzlO2Z1C76F-mGYG-U_uzrz9N9R69A9qqXa3N5_TXwOzJo53ahBFtDQGyPLyiqSVPdTUw0BzgMBLqWBm9PDyMWfOrlmVbivIws-RTGbM-8M9nK28xEjq73EzHjL0aFrBws-P8MnMnkmfZO0F0pSeo6eZ563IhuTlWYW9Da07QI3csCwc88lEYY5IiIIN0wcbwyqmoc241LE6naoNXLFqTyOHmMwpsjz8QDZECjoAQkBhu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس تا اواسط هفته‌آینده پاسخ نهایی خود درخصوص جذب احتمالی بشار رسن هافبک‌ عراقی در نیم‌فصل خواهد داد. پاسخ تارتار مثبت باشد بشار رسن به پرسپولیس بازخواهدگشت و مارکوباکیچ و دنیل‌گرا جدامیشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/29845" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29844">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_02RzcWOdTTAeDb1Cx_t-DaeLb1GiuUcP72CyfiyH1a6yPbjK_d3lQW5wY4-LGQyPXe4hS0psZJbNH_16EdcJw9H8CNtnM-TlOOpzdsL4F0ZMQ3SJ0eNUgb8V2CHLolKiGfhsWEtMPrszLZNSP6kgvOJagpUlBCmROMmBttB5mY6HV_sUtYlIAbn_wklHLVbx733VbbZnG2mtQzBfPOVjGQXAilOqPcn0aRyA1z_TcQy8YlkBJoegd54dvfRQjHIUtlQvaBL_iPAbheGEgX0ILmeT5wKMzFclYDG1ffbf8PWA1JCngdOHWS-cVl6G1jtwRy6932MAaf8rc5-wWpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/29844" target="_blank">📅 00:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29842">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L68F1F5JF6moj64ueQiw7_99oqa6BJ3LqL5mWTnghco3sfjk-v9XtkcsIJ91Jf4sEZSIPJnVjy7kw7GGNch6a9yIlSE1FCClJtUycpkFobarmAdbRhmF_1Vao3MYfNFQ0KtGsuLURfy7wjI5-X7rltNg7h_TcGDENTGfxL45CZpTgA-2p80jrX2SvmAZNEmF6SuoUDoDXph_KpNgFPG2Pxfk6T_lwV45k7sJ0prIeUOTKU1d3UwbyxYf_fWM4_opwnWR3O0OWBoLPWlDCUYkuC2Q8EVDlVptxA1pgmqOsstQ5w8nyIF1RjX-gCZvGU0jZSCCP7c2NHpS7dZIWzx2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29842" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29840">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHVRRl-wM629S_BG_8PynuMAox2cbPgHVfaGg1NR8UA0hhZdDfyyBN2YPQSh5PyCEDZtHUpjHeD_k5cunnYyD6o-lFdEPcFO82M0GoJwZMT-2SbmYE0kWGyHVFM3euHE1LEjqfGcddTv9Jxugoty9VRupjFzq97mUqP40a9U7-fI3GLTzbrkZDNx2InTVFGph6OrdAdc0SoBcUPrPOEFY1L5vI7o4V3nqIK8NpFeMySu83pCw_xj5e-lt0PQvXM_AXdedia3HjhyWbMocHbx-_Gn4U-xa8jaw4gHZcgQAg32fccxY7wwPlLlwbXDdVcUIXFhL6roshMuLhwv44NwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auEbOyAwVUake6hHYQg4XStpQWvIYCGhVGPTov0LSnjaX-gVh0kA4wfNfZgT5b_R9KNQ4ZRIKmcfn4hHqNzQ0bh8yTsBx96hdc6qR8hZdsA3Pn5g-psSPK1NWVefMJ5FLzWUmnHS6v5pjU4ab3qpUsnZDkJyGkyLktTQObOTm5CZbWlX-zEounTO5-OpXNKbuPdJHBGOjVJgLzz6xXwqGl6p5aqfehv7sTHiP4jG3BSw_3mx-ejTqGJOqknvOGoxm90ipPibGNTWEfijC2hyvVmA9HcW5SPa-s5jIALleH3i_Yx8UmFeiZ-C1ud6E1UlSmJIuH8DaPhVxWeXkn2lkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛
صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29840" target="_blank">📅 00:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29839">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqvu3uKK6JT4TvlJISi-XktZeXtzB8SznIqBgCrGXZmPk6AmwRY-4gefUx1wKq_HzYgOo1SRLH_Upw40gGp-1h9ESnAzp06jq5zH0reAxfejbrlOjnSdPKOCI2_0CxjTGIQjibto-KqxenqHDq_ZuYmQEMeTgEJ2Tp8VGoK3OaPVleXuZSLwqULOKW17C1lb_bCepBbP0wM95ubddapkGM9ypy0jOcBGMUlzUJA4F16SFCwFZb9p5kCp6KQjm1vvSzI45QTQu4rEnda34EeciMyNRvWva01UCWSc47spMrb12whQIGUam11vZOcKHMni3uoL-mvCLA3OPt96ibKtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29839" target="_blank">📅 00:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29838">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T5Wr8zXnIFsI_aUQghsyOcTOICHgqn_YyaqqtFkk8JWiRvaDalEvxKubIa_BDamdGImsLh3GJkq5J897npVRcot93tPTe8OFL4SkdJTDdvh6w7_MfEtcAzpwIG1mTXSgzt2affXOV4BrqxAmxMYHQH7A88mO5PkiLBttribBPmRJJ11tNyhWcOpIl5j2xyx7KbGy2pmhCitZLRIK3knx2Uoy--P7pOzpndfgTcssShpTnZ2IF9xdB5ozlIuHhS9ndzfJPnvdlA64VrNLD_0Yw_ewDzIlFIR0GmsYw4UOu9_nenHZs6rAKdsuj8ssgfoPXnF_GTYPAuwKyST5GqU1xJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T5Wr8zXnIFsI_aUQghsyOcTOICHgqn_YyaqqtFkk8JWiRvaDalEvxKubIa_BDamdGImsLh3GJkq5J897npVRcot93tPTe8OFL4SkdJTDdvh6w7_MfEtcAzpwIG1mTXSgzt2affXOV4BrqxAmxMYHQH7A88mO5PkiLBttribBPmRJJ11tNyhWcOpIl5j2xyx7KbGy2pmhCitZLRIK3knx2Uoy--P7pOzpndfgTcssShpTnZ2IF9xdB5ozlIuHhS9ndzfJPnvdlA64VrNLD_0Yw_ewDzIlFIR0GmsYw4UOu9_nenHZs6rAKdsuj8ssgfoPXnF_GTYPAuwKyST5GqU1xJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه‌برنامه‌اینترنتی شب گذشته لیگ نخبگان؛
محمود فکری کارشناس‌بازی بود. مجریان برنامه 500 بار "حاج محمود" او رو صدا زدند اونم کیف میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29838" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29837">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5vk123rSQBrqWjpFt5cjs21JVG8E77z6oTY7-9QBETAcQehfS8MBtHOsnXfQ-2KUduvlAN2B-um4uXFuU-cu4NOY08-5qH7CMrDd2iyB764f4mDVw5Sx_VdLSqC7B62Q7Q81IQjyN8sRH_fqwxMphAb8Atk1-Cbo7mrvZKmqs_qLj-qkxPTrxtmfQyV6IfjQwwgg4fY58-iw0K5mfjUfTa5Hhsa35C1oD3XMx2nUULCdE0UBo5wdoKIFrO1aNrl_QE9JE2YG4YPpyyKW8UH_QUTcuh92Ik1KANYqpzkqCrfqa9wvBcrw8SIVrOAjF-CRhh5s6k3grPqU_4Rfn_AFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رونالدو امشب‌توبازی با‌العین اعصاب نداشت، مدافع العین هم خودش رو چسپوند بهش اونم این حرکت رو روش پیاده کرد. 4 تا زدین ولکن دیگه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29837" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29836">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h-JMvii-CtokTdQntHbB5nien3fvoWukgp8aoXsaxBRW-wbBn3HSlCsO7T_XzjkE-tl0Y6Le2uSRlaDaRrsjslBZL4zYPbsM6evgEfj7sUzEQqbiJiY7U0vj6BCdckFZN2Si1i1G4e6zu0wubg0bfmNsuGwP0Gwd9gIcTWCpSDC65BSyp7YBKlXgdoPsTKLbmVfRNVpNqMsANGVgrp18APU1yX93JGvqvlsXT3mDCFRGoLUhbwNU0cHTkDpsCY_mpUGf-sAdjgDE8EqzzyAatfQlOYIMUAX1E-8bHO4kNyIjeq7e9WO_Uc8yNcA6ka0fWDujBq7zcbxypOUhIcce8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h-JMvii-CtokTdQntHbB5nien3fvoWukgp8aoXsaxBRW-wbBn3HSlCsO7T_XzjkE-tl0Y6Le2uSRlaDaRrsjslBZL4zYPbsM6evgEfj7sUzEQqbiJiY7U0vj6BCdckFZN2Si1i1G4e6zu0wubg0bfmNsuGwP0Gwd9gIcTWCpSDC65BSyp7YBKlXgdoPsTKLbmVfRNVpNqMsANGVgrp18APU1yX93JGvqvlsXT3mDCFRGoLUhbwNU0cHTkDpsCY_mpUGf-sAdjgDE8EqzzyAatfQlOYIMUAX1E-8bHO4kNyIjeq7e9WO_Uc8yNcA6ka0fWDujBq7zcbxypOUhIcce8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29836" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29835">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=kZaKjqhiwgQ3P8VDX9bqZGactgroliSITpm1oXdvUF9BRJ4_eHNr7Dd__xBNJh0j94NXhrLG3re5CLO9o7VILyavobxxoXHn_w6RMyE_Ev1QWdTElVlGMoigg0f8wN-OXgYgprB5IljPFhrVxNapRHBj7g0Lfu9ZZ1Rzbo58AMxtWQkeusTgx_waXNZMhky63MOIJYkURqN6hkCbST43DUDh3_R_aAZ02na30fNqaB7sQTqwmFTJYR-sG17HgpJ3rrECmcuUrdF23CwVv5vVzURS4gbid1SfwF4yeadbIFuY4rAFscYeF_PoSI79JQXOsgys9x4sEqfSmv87u1woBGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=kZaKjqhiwgQ3P8VDX9bqZGactgroliSITpm1oXdvUF9BRJ4_eHNr7Dd__xBNJh0j94NXhrLG3re5CLO9o7VILyavobxxoXHn_w6RMyE_Ev1QWdTElVlGMoigg0f8wN-OXgYgprB5IljPFhrVxNapRHBj7g0Lfu9ZZ1Rzbo58AMxtWQkeusTgx_waXNZMhky63MOIJYkURqN6hkCbST43DUDh3_R_aAZ02na30fNqaB7sQTqwmFTJYR-sG17HgpJ3rrECmcuUrdF23CwVv5vVzURS4gbid1SfwF4yeadbIFuY4rAFscYeF_PoSI79JQXOsgys9x4sEqfSmv87u1woBGvKLiWBe5FFYy_i17Q9Cpc3KHVegn8XDvamTtCzRt075we4MId4pS0I_hyJNUQfODrNhKBHmY7lOjEdntc-cs0cnYmuzaWwhdE9GeUH7cXI8-quae_OxipWr6sPe-AFC3zxHd_ryABNRHP-wiJ57xm4caX0yASe_P0kzPL0VOnOeTrXDTYfXq8s83JaZHUxcJ3w06MuPQJBzyAk5AVfEsSjuu9qQnO0DKSo18M64gRDQpyBFGDcqNSutXkvQr4F-cHHOiUjkPtScwXZ8P3-Y-y5IJiLmzU6y5WyGTJDRCOotQ7MmWI1XH4twlCCt27_fERaULjLvhbcwhaX2XjZqvI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
توضیحات‌مهدی‌زارع ستاره‌جوان پرسپولیس درباره مصدومیت‌عجیبش؛ دیروز  پزشک پرسپولیس خبر داد پای مهدی زارع در تمرین ریکاوری امروز طی برخورد با یک جسم تیز پاره شد که بخیه زدیم. زارع امروز خودش در استروی نوشته پای چپش به شیار تخلیه آب گیر کرده و اصلا هم جدی نیست.…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29835" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29834">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29834" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29833">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=fa99aJnza-YOMEv8NjFaSVrdTPa9bit-hLsdedfo5DFTLq5gwXK8ubBhx4kLjEjd_6jtKbHGDcQl9R3Ps-MAn1XIpvQf3W29sBy6Y4NuK3jN6NNiCqlArVRmykcGqxV4MyKcnB4DdbDuLscpoNN1nRDFL0dxTW-aj6XfOJGL0THCi7nt_NPPfl58pQPga6y9wHwfak6k40ySPgRdf7PVXrLwX0m3azXSDiyJyg6QC7zDFAUGo8oJpaxUkI2HtMur4--VHXn86ts22Y057lnvdWp_J7ZJTtFiJ972EFL-n4hTxktSe1Ck-Er6r0y8065K_YmJK70_woxBGIFBQiB6EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=fa99aJnza-YOMEv8NjFaSVrdTPa9bit-hLsdedfo5DFTLq5gwXK8ubBhx4kLjEjd_6jtKbHGDcQl9R3Ps-MAn1XIpvQf3W29sBy6Y4NuK3jN6NNiCqlArVRmykcGqxV4MyKcnB4DdbDuLscpoNN1nRDFL0dxTW-aj6XfOJGL0THCi7nt_NPPfl58pQPga6y9wHwfak6k40ySPgRdf7PVXrLwX0m3azXSDiyJyg6QC7zDFAUGo8oJpaxUkI2HtMur4--VHXn86ts22Y057lnvdWp_J7ZJTtFiJ972EFL-n4hTxktSe1Ck-Er6r0y8065K_YmJK70_woxBGIFBQiB6EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
درهفته‌اول‌لیگ‌نخبگان‌آسیا؛ العینی‌ها بادرخشش خیره کننده برادران رحیمی توانستند با نتیجه پر گل چهار برصفر یاران کریس رونالدو رو شکست بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29833" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29832">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRbDTt8IuJ_so9vT1xj1_uSTsxyoE6JNX0CU0EffJvhacqnddblClaiUW2z71tJGPoHZZjgH4zczCWCdvXszVul6QfNtXUesz5woESnOaZHN7zs10PfCOj6C_7nHML_RyEqtK9buvGkaxQg0jPCMWUluYnD_ul00S3euZ-sEgxz4ss6j47xHwcQ8h7wmAOxNCLNVT8chb3HX4YP9SX68A5JQqZImEt5e5eJBLHWc8egkfnh7DbVLUqTKj3YXuzWvbON1unMQrigZT71kB1i7BFZNgsPxhR-R53Ilydxh6CRPpWV62LGSUlWCSwEFIVAP3IQQ7aRQinpCgS0894djOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29832" target="_blank">📅 22:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29831">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jakg5NHnl1D9J9nZuEUsQv_n3932bvztBuozfLEKhv1yo29BFprOZ3FrYYL1FLtfX0zhegsihFfUFiypubbREtpNQj7VG-1fcmTFolKOpYqIW-df8QKbofGyMwZs4PCSLBkbI3gGnXr-SUiCUujV4fGMYCmWKp9z6B-70Y0ttrOF7W04CfswtAAkzB4ihYAYRaFBf6R89H3oNn2MHvxbjPdl0SVlCiy8ws93s00PNd1f4hnU0FmF0nGtdenMqE2agXwG1kEpuEu_1ZUBipsiuuxgTUCmSkTyeL7VVYWVf-2oDzJQm7FaAwYwEX5Lr6YjYNOL6EuPpSBrLAUmyMDYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29831" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29830">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSMbLlGu-evlV70cd6EL5ycPFBRj0u4gxl4qZCxFLKnOqGGuydSPqU5pb05HU7wYUfqHJSYZ8OVZMtAOX8Rq7kG8WQLYqg0fMUkimY1yfh8Rtog7OdctSRJrBefEAQyvzbtkxUoA5tYj7FByi2nHLHq7BtUQpegyE1sq2xqz0fRDLwcjCsFCa9R5ob2wLXu0nyoWwJEXPK5d_DpDwt0Pmn54XtmtA66NONGDcpEtZFCb9pA-J-6-eCr01x3jJU7btJb2kkW9tYbjudFFNiopK0mdfF9tO9qYvYHkP2h8sqOig2KS7aBP4TAHRQNVkGyzDZOzC3A6RpI_5FO3jkAIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛
شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام
در سایت میتونید مسابقه بازی
رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29830" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29829">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V85HEzOUArPene7xnY4uq8ufGMF9HjICHUc2E0TlT3oZ7Zt1s6iityUhxjJImYfOjoXZuEgxgDGifwdoEZ2XewEMcpt6duKR4FmZjH9r4KinOblSozKkfV2urVn_1HJRALjKrJI9wpfZeu1xxGkxDtO8OvikI4LsxPZ9DAUJE6jwhAGOqTqjrQMZQKsnAZdvAYKtS3ASZ5dk9HQ5UrlpwztOEsk3nMJ6VNTE44X4wolYBX8PursRuXkJCOn_t51dzk--edzBbwjylei37ff7C9S5yIQoOOGMXljrdA4ZzKAwuxmPIoqk91661zW-4jUDtvYNxL5VyZa8R3026aD7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇨🇴
#تقویم؛دقیقا 11 سال‌پیش درچنین روزی؛ خامس رودریگز فوق‌ستاره‌کلمبیا این گل فوق العاده تماشایی رو در جام جهانی 2014 به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29829" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29828">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29828" target="_blank">📅 21:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29827">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=k7-CmG_trdiCRttkg065vJNNAinDASCbp_A-k8OxBlmMkOXyAvbCxGgw8HTiDuIbcylYkxw7TJYVHp9EoQ33dSFG8A6PXDfLg3DfI53LRG8Vn2auvlWqZotX8vSm7elH6ahRHoN6yrpVF_0QMeIp5FeANF0eZ6dZQFnMa6f7Jg0isY52Ywi0lJOm_35FPRa-lH29sguk_zhAKOLpU0Cwx4EfnqwEzCserkejvBXrWZaxVrYP70MoQtcLsvU7dbh-abU2n0ednljl888i4vyD3oOWwR2uI0roRjICYiUlT56CKe4pG8-qofwC5gTARNA8NCqKK8Bn-lVUW8peOmDefw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=k7-CmG_trdiCRttkg065vJNNAinDASCbp_A-k8OxBlmMkOXyAvbCxGgw8HTiDuIbcylYkxw7TJYVHp9EoQ33dSFG8A6PXDfLg3DfI53LRG8Vn2auvlWqZotX8vSm7elH6ahRHoN6yrpVF_0QMeIp5FeANF0eZ6dZQFnMa6f7Jg0isY52Ywi0lJOm_35FPRa-lH29sguk_zhAKOLpU0Cwx4EfnqwEzCserkejvBXrWZaxVrYP70MoQtcLsvU7dbh-abU2n0ednljl888i4vyD3oOWwR2uI0roRjICYiUlT56CKe4pG8-qofwC5gTARNA8NCqKK8Bn-lVUW8peOmDefw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای‌ایلان‌ماسک:
گوشی‌های هوشمند امروزی تا پنج الی شش سال دیگر کانل ناپدید میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29827" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29826">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_yCGs_YTXiZdPhtDCgWONKXgWY3yYZbJqrAHxDJLyIIVDmJLnq9bpE1wSZzhshdCqrJ9RZ6QQjxU2fnVAojlqwoRTDmBpUjKM3b8FlX5fjljCA-WwWItw0loH_Tk_fPY9a9wf-JmO1rT2AAiQqzuSKH9ZyfWRICZiQNSpTJKzVHmYOkPx5VyWfbHHktX-5iCM0lgkFRAJF9vGrgL2xTAXd3-zDHAbX_ow0i_MkxRATgQ50a1sTsJn6vqC25eerwvP_bq0-8a1CLu5uuwhOAQX4I02S2TZ-BaycM9a6BcwdjXaRhGM0aQ6hsc6etn3_gXCE-fg0UOu6F9Lz7ik_auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29826" target="_blank">📅 20:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29825">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJTTpj8i-viyOG9UanY9ghc_m8LR4guqR9LX-7khYLfYFczrVx7kbF7vkSQ1zHuOdqhDXZiNfHY4IbxxHVxsuLh6NbwPgZ87c3ysVTKEHLiXZT30FkHwKTFrVMEQ8rE4ODzuZz_7kz1O9-y321j-NWW6RAgNgeq7eoLwakXVDwbbfSWw4Pr4ddWn6_dagjeLEx8kX01BDv_sYlMvsfUlQvAzUqX5tV725zOyaha5blPjMKBcHI70IFy70RfA69CyN6i7ZnHC-flmc7GfUMS5yhxS0OzzzjaGGZhaTrD2cFOjmcoqedl2pqSlVewHXzkp32nCjuRoVEQfC1UiYCqXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
رودری ستاره30ساله‌جدید بارسلونا:
رد کردن پیشنهادباشگاه‌رئال‌مادرید اصلا برام آسان نبود. بله‌ابتدا درآستانه‌پیوستن به رئال مادرید قرار داشتم اما بعدِصحبت‌هایی‌که با دکو و هانسی فلیک داشتم تصمیم گرفتم به پیشنهاد رئال مادرید پاسخ منفی بدهد و با باشگاه بارسلونا قرارداد امضا کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29825" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29824">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de2283857.mp4?token=RSdvBbX0A1Q6688yQpmziwT-jM4wzpnbjg1pH65AxXjFQdxiR9VwJ0hEIg-0tdnRPWQmCGQxPsaUk1ZSeUv_7NNH9m8zcXjHUwc2c6bNZU5HxDWoQ9xcyTIrWKXoLYLCCxGRUwRNslUWR4aJUYlxDdGKIIwVtpoV8qDJTESJSYaH5-iBIK5tFQLk9olXX_15zb3NWX32Ih7Cvfz5Q0YccItuzHyOXfUTEeqj9mkCoVsDI4pm8axGwqie0VZI-JhWJMMc4tJGSzX36qewq9AdMEmFxwe8Ikar8GhnakI2cGqjn1PFwaV146tBftTeiElv4Yh2UtKeNEVYe2ZaBohGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de2283857.mp4?token=RSdvBbX0A1Q6688yQpmziwT-jM4wzpnbjg1pH65AxXjFQdxiR9VwJ0hEIg-0tdnRPWQmCGQxPsaUk1ZSeUv_7NNH9m8zcXjHUwc2c6bNZU5HxDWoQ9xcyTIrWKXoLYLCCxGRUwRNslUWR4aJUYlxDdGKIIwVtpoV8qDJTESJSYaH5-iBIK5tFQLk9olXX_15zb3NWX32Ih7Cvfz5Q0YccItuzHyOXfUTEeqj9mkCoVsDI4pm8axGwqie0VZI-JhWJMMc4tJGSzX36qewq9AdMEmFxwe8Ikar8GhnakI2cGqjn1PFwaV146tBftTeiElv4Yh2UtKeNEVYe2ZaBohGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی‌از عملکرد خیره کننده جیجی گابریل ستاره 15 ساله تیم منچستریونایتد در فصل گذشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29824" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29823">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRVddUdjMo575Hm2K7fkBZnowAUGi0ZB7TTjevWScsYFOM-BY_ebOCapCkGj5nXHVcUkU9Jy_Yts7TFrcNp__TTY3ZK6tSd7Skj-cNj6Rjm4Xg3mO1_i7hZoHZ0gwlehemXF7sbOTeQH0zYxUyzd_wVWpIgwh287WmylOwpYBt-Yp6W8UwIL7HY3pBedHanxZAa_LoLxgoF2jp8oMCrMxQnfTyQdKkW7YWufI6N9VXNzA1GWJ1hlgvfUj80vT0sjnK4bPuzpIwE6c67eauzXJsef8OGBL6jAm-0v9XDemo7XIzW0LYCTxEi07pDDCFw5p2EM9dhbALeC4zX_3QgZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق به ثبت 27 گل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29823" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29822">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jssshMa_SIKmRnXwI7s5VXjvzs9fcTbfaI-wgJ6FhnkiTlKwV1qHAt-CBB5eJ58994gsOsfSBtVBOLQItx52EHgAkCguVIJbJ1n0PzdtgdsESTpwQLuSbVvK8H-U_f9h007OFWrW22br9WBJqPt-v8lNrrxP9BOgXHSf09wULUyirB5KFnHcE3xaFyD6e3dfyx7hPaI2vZQUk-hWt1P01apO0kQLMchLEczxael3HnJA30OL2uOh4brSQhcthsb3RU3azQwfiBI_X48qJvUbBBh7fV38l2wCc3_AlxZ68KQxDHEhFlDbJN__yTxNbEtgnVn7Ajw5Wki-FekhSF9y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29822" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29821">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8dtSNYSh4IsRQdhLQ111RnFYyg9GhaZYvNo3AVgKmWiE5tQfLnepltQ0IwiTJqs5Ku9VWBh_uEEWtBCay4f5xeScPyTD5CYJM4UOEtLcFKZQeIzp0tMT30qbS9HUnIPgvuEaB7WjlBJuvMBiB4fxOvF8dcIl9C_AlB-zB8c3nBUMMHfvCQRF4GIrPbSwzWxwPd7G4vkKj3NKUm7xdBRzNTvU0RqHwbKKJEqptq8y0txPIWmXd9hJO8WQS4PQqnDJCV9q8t_GByEUiM27MaoHy5QtyiIzdIcnf2r2kOPKBh2qMXUJClg25ImYS62ykVYHRPvYQ1B9nPG0gLj_m7UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29821" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29820">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29820" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29819">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_YagaCaOk3TeDMQHCNLxw7eTQyZJboSICWZ-eOTmxhvZ-LkedkmuWposG3BXqpjovC4XJlARqc148pGk6bdSdHD12e-3i9vQ0uwNPOzj4uwftdJ7SeyklEQ1J9qbyL2qgc8biUg-bgksQ3HJCI0gKlWO3ivKMox4r4Qe3gqRhP5OY2tO42gh3sHRCiVm6TtrhqB8JmbnbF2nm13qsGWLFIwolJs7emN8UN-F48txzpE-YA4wkjFPdzOM7BnK7HmyEUvqRtYkvd3GnCEIb93PiqVoWYoiHJi9NLYOHx4850qYRq49Mg05UPGEk0tlEuJOfVn9H3YrOgMFfBsECyXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
الچه
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29819" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29818">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtYzkbQMPnHhffMtij3vF9nRbkRugTNgivHyOYJ-3w60J-Fz2wSoeu-77ZRemq2jsjGvjnIaFiqaGdzfLH4MqKD1OKBvU2usRHbT_VFG07WdM8weaeUcsz0sbs_vv2pmiRFipw2S6w3AgkmseE8-3m3hKESsAvYCn2ajxeLAEtpV0uZZCeoKpxH9MW2ZHGa4SWsgS5DGufUmb2fuXsaWCmCPx4ns7Nu-l9pVHMbnUfX0sL8DfUzq4wy0N9FMA3exHjwpKUqbgEqL48QV_VYcdQF0hoQ2mS8ZLLEMGjpnip0L-8O4DCDLNTiNBPI16lcQHoeBW6U40yZR98aKRmGz1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29818" target="_blank">📅 19:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29817">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVTRXCFrsaOpZNrbUzwQkMaaBSTHxfkVDl10kw5km0OxUXlljEIOuRUCU6JE8Yh5deaSKpOV1TtAPcMto_XPuyrnkwRc7tCRycTjDqLhARM3juo-yIQUx2Tb13rugCkL2QlPXckhWNJRSbtL9lg8TTY7FWImNoB-2mocUtzxc3Cw4kprw55WZGTu9Z-tgIMvsVXhtcG-cVcN7IyC0_-OaZEoFeoMXSFeb2DjXemwPNd0u-CTV-wUK0nWUvOnIm_k75rruGmtZEnQ_Liv61HAJkn77z5V3cag7YwHbjQNNHR017pcjQr5B_fM093o54dyFQREUySQIquqRVpxAWN4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29817" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29816">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3a9maJcp_TJeEBZ1ql4VUTd5xMLkuIvLGr8Gr-84WcxrE0yXsBE-FTKAhZIsTMwn-cWGd9fQWtjp6yePtMODHq3dEnruN8eV_NMTHgKn1lSiotoDCnOuQoetz7gTIsMNMvbg7Wje76evcEo9zUdO2I3BajyCjZMLxfWnSPdAph95uV6-JHjn1YfoqdKvw1MfFalugO7D6h1_XBccl1wmgHKRcIWoXtNF_1Btjf0cOC6viOM4Ky5-Jpbt-kgwqEaZ8y2mK-pSmaUgpkJJn_wxYAD943wBa3VApDwJLRnewkJo4ceQETQh9qrkihYRu3TkyZi3LkyE3PdbqbPY3ACCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29816" target="_blank">📅 18:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29815">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFT8kok-1BVnqHoL5A3lbTelsmAgCYtwL_-grmZNH0b2K5GHCUnT8AoxY1S4_keXSsREZ1QTRAWdSfOMhZlqcuv0JDwckwn3N_ojjeLsCD41BBlkUO7DrL4XHyzAdTOrEANhLqVxMq0A6etjBIMvG7ej9wQJduAA3TnjHnAVZpvhvDkoWK7rsagLUQfxjUg311zXwDnMjf-hAen3AyNYP5cXyUdEYGOQWz7JZvj_SSwCJ6qB9zb2OEET9q7j6CfvgZPvDo26mwCs61EeGrpbiActQfaJmpiHz4iw5W24gnuG9DEAAsqtoffUn4vHAU5l_IzTVmJTi5VPPDloMLthHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29815" target="_blank">📅 17:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29814">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boA5ybG9J1CfOIyMgSV0xhzHq58za0HSuSJ9kTnKDOpodAAhh2Kq-OujB4YwyuZb3AI2mgJIE46PkiHBXgSObZB8TiUdw-oX--e93HzuJiPuFbkWwLSbJUrCWlwKRL7FNeQMwROR5d2G6gBNoIWZsZK1w2gCJDJAbkwz_ZihHzGFqeYbf7V7ETs3yjg-R_IvbWlUVJ9Xuv5B7RezzWfrxxhKiZI-zvq4qqyaz8Cu1Pyd0wLeCmP4ucd5lroDkqr4zoII5OHg5NxPyI7EcwdRnpC50fpdCfXfOsEscIOiUMb5pVR_6MWcb0AzDDcCXaczXxmrIT1evpAO35RivbWKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29814" target="_blank">📅 17:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29813">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0RCLUo9c3aR4jr1tLe4pz5hw_5DVpD9nKiSBszkrDjMLa3KAXxmC-Cd7CHUoRSxJmh9CeqqX8vQIeacu4OUTJHOiefrwMwqlzXXA_lGxaVQaqxmK9M--JJQ6bVFtgzqauSFZHYjoU_ALnQmHvkyhm_pM8L_q_DJvCD7H6cxbvNASXcJVjtj0xMI0mFgLeDjFMY_zQvkwYbU32FIuS726svQrHHA6vEPphSEyYwddn3lCqcEKER77LhGPYlij9x35kXk3DNEWoYsrzPL7YUcQMJ80yjp32uO2Zvh8umAhEAiN911sOZhlvkDhrSCX36PQQe1FTq4uJo12Pl_btr8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمپین تبلیغاتی جدید سیدنی سوئینی برای پلتفرم Novig هیت زیادی ازسمت ورزشکارهای زن گرفته اونا میگن این کارهای بانو ورزش زنان رو جنسیتی میکنه و اینجور به نظر میاد که تنها استفاده زنا از ورزش این حرکتای سکسیه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29813" target="_blank">📅 17:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29812">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyOKfhJBPey9HhqwEj8E-y1TbmiqyNARsficiw9QIG3hZDbyF2lOOvOjpLWtNZam8QJoo3tcrNy7fHTtlLo7P0JzFmIyliFdyVbAd9p_WYv1lRQuSRQ2yqiYHdmWBhqV16f4OA1RJSlTbgN-nM0GUsYpGExe2hVLDjBAVB7KPy9u80x0-R-oski6dYCxwcU5hLr5qn28FJgL9heDYZN0rJD2PAwUeiZa4zff3E9jIN_RDauktgf-mwXg_LjU5LguW_r8DmS2Fow-FVAEy6U04clDA35lrFbmG8r0-LOUUx8uRrIMcGhCrglh0ik94vNVJKTHIRGMbCmbIk4kvXuDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای تیم امید ایران در مرحله گروهی بازی‌های آسیایی ناگویا 2026؛ فردا اولین بازیمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29812" target="_blank">📅 17:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29811">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-5Shn2Sdxjd1XXuB88-eds91U9Ri2kt9y_ZZ-OQTiwZ4G_IJG3TjgYWcF46ql6f9OGImKC_ALkYxL9ZBBl9s1tXqGHxLsNsYXMzFeNtphQyeLdQNyh5EhHdSidj3pgeEepwDyx9IvKXJMPMrBu-4xBtGnDDGWaUpRy6EM8Jja0IK-mCBhRl4f60mF44ZxobcKOH3SoBy4rpAGw_WnVy4FqE0ca3KRvOKFbUZZJ_oeQqzu9aqgclDrtkKmiOvIhhCxlxZkinkW63ZLFPfydQvbzc81tbUbd2vBsHW0idWrXRDPS-KvYG2N0pqg0OXNyww_PKAV7VTawkBGJX0QMnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ویدیویی‌زیبابه‌بهانه خداحافظی مانوئل نویر 40 ساله از بازی‌های ملی. نویر گفته دو سال دیگه کلا از دنیای مستطیل سبز برای همیشه خداحافظی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29811" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29810">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLoM2ZY-rfhFJ9kx0Yxi9vMIL3ugvk3mlzeCuCy_IhAWNT-1f5RBSjCE5b05MBgluh4ckR5NKVl-4P_fd4Cqd835o9HLkxRR-LhxKOyT0Qvb9CWFaS44cfsUxT2KiiFmM_yChqRK0-1auFt6hXf1cVdRXh253_fwMMpAynW6EfN8XyzAzTobG8JQKuooaLsn-TrW-x39123U-DzKgau5kRlHTGl3AGuEPtYN8MbNzPjeW30NAB0hn_uPD7Q_O5V4q8aD7P2lAGVrlObYo2rdJayXse2ThbBBF1ZTP7ZsjjSy0l164lijHkCxIaVo8QjhniE9-klnsdOusRofcVIntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29810" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29809">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sheKuZ8kAAliRmhuL5rkbOPmRU4JdFu9Xxl-7ZSwEcHVfsCzLuArXD5XMxLRDCufBX4_96GTFxt5WgFqqxDCPRjo43rngblun5dx55ZsTM-4W-6qNIVZZ7wMm0zOTpmtV978Wv_4KUdOYY2VjCACm7vF5LB5LS-KNog32TCFSSV9D0OtA2QR3mWFZRjw5cgHr5O1Fv8az4Tnk4roiHQ6AqJtuIpmJXtel4iY8iS4uZi9rG5yJOzmB-wM-sFRaxESX9gYIUe7r5s3QrmqY6WZhYSyjOkyOSGkhefuVhw3ezxmvR2tN3CxR61WxC3DVtOGm9sVRNxv72v3cPQHD6QGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29809" target="_blank">📅 16:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29808">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx40SFXFkNUYNXLm2CkhMgC1NimWRRNCYnS7yx5ePgbuW-sZyoV2-aLHB4s239aoNiwnThcqGO8lACywWn0uq4KqEVkbZmPIdschO4sfsL5L17A4zUtfeYQ1QFaiS-P9XYl2Z6S9AXGIMZ1unhWfwju3PBLkPFuSS4iYPemEfmyHCD7ndu5s4xB2cIAPpzHCCFKqQLEg2uLuYZIzdm0ncAgWcNzG3jqc18ZHwAITzqiGMQ0ofzeRZr37YJQP9YNlCcbSOWvM15K0jAmVGFy-CYwaY3Nk9sTI5o193iMpN80hOzMBUjdAFcmo0422BfonGO_BZc50c7luk-fRuqZX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ در قرارداد شهاب زاهدی با باشگاه جوهور دارالتعظیم بند فسخ 150 هزار دلاری گنجانده شده است. هر باشگاه لیگ برتری که شهاب زاهدی رو برای نیم فصل بخواهند باید 150 هزار به باشگاه مالزیایی پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29808" target="_blank">📅 15:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkbSkCmcXxIDgaiifwQEsPNnMrh-5yX64XpLP3jKt60AmMd3elY_nhs8gl7tEpLG1PODv9dWx9wu0TCKtkT-jyLSAG06gvOeZknRX0Utik5XMKfqKvwiB7U9rmX73Ql5YSSpjmbILtv2WH9hLb8_RTrEOC8R1NY2_VIp6zPqUG7JGR30ZAe7_ucb7DVR2MOXZdf2CKv_wbzSt_kyQIhbP83AFYWF04wmBgasdx79rNPq-8gg9yjeRsaVT80p3n7Etjc9TBIjOhoQ3NJRgLe034uZn7nZPUi1xLQlN2aXROc7rbAsQrijxDkmPxdwgmc-4I-NyuHfjnS5PaJ-tEr0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRf30070mdLNjYh05LVVz4E7NReGe1M7MICvtFhI1hBYSI_UG1tQ1K478BKmUT4bl7NDYwTICfLoeNVxYVdhjLdbuuoCaXZX8l5GoKt15qhopbZsQFi1cesuP4-ChG0ICTKpDqDoVsxqmHy_M9Tj6MlEN5tTM6pNsK1_SPc9io2Pc0x0wpL3Elwlt0s-mHC5xuafpir-_6FJSkG_kvyglg_5ClKAyNN5OFduwclv6V0RyhoPVOqx655hXVcWe3egtNdZuk34SLAaXcWAjHCqXYzUsHZbzBn6G4b28ul-0fSPavgW7z-AdAaKBev87fCRQC5Eh_MJfUUZuQI8KaqbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29805">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKL3Zp2tyN2dCS65TwlXJ9c5XMMzk5XX7Kyrudqi2FHRlTeqiLAkmWTmKBt3KOOuCmIzTHNmp0AIelu5vpkQx3cRmKq459ZxSTRWah_BV1_g0M8N4EeYzfGVZzdxhHVC18ZA1aZPQUWXH7Y1s3lntfcIPfP2_4PV4-dIClnsB2ykMDvraVQ-eMgECLCdWh2-qpLA91HLIsUMQNEWKC3_uypIGwTrss6dRgtSI7pDxjOt9ZCW-ESQ10HqAdysMOx1uaYj5-OSIRtuLQa5W-eFvSEKFidkQQe_-fLzqVLL_Pt0rlVXZCbAf0Xi1Fa4zysUnQ62RsQ7jn2f3YBcRcC-gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امیرنوری‌بازیگرسینماچندروزپیش در مصاحبه‌‌ای گفته بود که خیلی پولدارم از هفت سالگی فیلم بازی کردم و اولین خونه ام رو تو پانزده سالگی خریدم.
‼️
خلاصه‌کلی از اتفاقات مثبت زندگیش گفت. بنده خدا فکر کنم چشم‌ خورد دیشب‌ تصادف شدید کرده الان بستریه. زندگی‌خودتون رو رسانه ای نکنید لطفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29805" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29804">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfM4FHt_21cRiH_Oj0rSJhlYK4EgdejTOgHjJybPOYescbVYaEPSIgrGFFsvlXnZ6ZaiCA2RrOpIyjCnuPjN9dGeBIQgmUbdTke50NsHGctRU3325L_A2C11s0jwz6ogpcUjDf9Nq2JR3Ln8HZFYm6Xc4C-D-BJIfjtC-z2PNoGBnsuW2AKvK5O4bj5XGEUf8zoIavPLr750tXsSbqgcWIYZR_BpZ9P-BxHJTMySYlgLhJRPLvJZW62LNSgp8gC0IQmHH5y9rY4gFJVjib7jf7QRiRy-X1HYnBAmPz4X3QgTPr2Q4KNOrbSo4TQa1fkyRoYfNdMQ8IDlViWu5J8jMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سسک‌فابرگاس سرمربی‌جوان‌وموفق کومو در گفتگو با گاتزتا گفته در وهله اول اولویت فابرگاس موفقیت کومو دراین‌ فصله اما اگه درپایان فصل رئال مادرید به او پیشنهاد بدهد باعث افتخار ماست که با باشگاه رئال مادرید کار کنیم و سسک به اونجا برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29804" target="_blank">📅 13:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29803">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj0QZTmFBLNzepfT4-OGGZjNYMNd8d4ZjJBjuiRDN5d_HQGCIN5Ud9cncIdcRmBFbY_xS4I-k3G3h4lrgPQwOhT79D_CDjr5-fdQEBk--bAYMeZ3UxAt740NMEJkjSweqCKD9BNFQuHK8lrIjG9_uhqaDjlkaw9ulMyY23yJ9v4Fl5IkMhzGjcirkxHiCODHuoPkNdrmWsi_4CW6NazDU3_Xn6w9uaehaYZbG5u8kYn7Q9kgk9L66LLX-msLgptWLyFvFV7mDSsFvWLbeMNV9N_qCl5-fECBWPwaXFtuRsg6L8CfIk2LWk6zJ6ImnKFgcMy1qYTWD7OE5CUb_ytStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29803" target="_blank">📅 13:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29802">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH9haA6b6Z1T1ZAK9rAgPzespU5c9IHrRxYjnUlbVwQGDt81tb17-u7SIEzv455S0KCuJi-z8iefWnn8fjhBx4YsSwZFc5EHgnTXkQrmmdlkJ6DN_Pp1CmhBpwD1KsNgJJJMQ-GpjEbZ2F1wdtUeCR_VTTbBmRBcDAsYEr3Up9sCSLoImoklS4niDPmfoMatKHD1n3_1sYbr-Tczpq6EENCegIlus6PPSg1fGab3oILvGhCOjhuxirKsxYCeRzmgS1mTDAdG6QlkCEsvm563a4hcsCVY-TChjDk3Wy8mv3sq0ZGnz-r6sScASquB15vmeZLQy8lD_fQaxMdQrM5xcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دراتفاقی‌جالب‌وبی‌نظیر؛
در هفته چهارم رقابت های لیگ جزیره؛ لیدز یونایتد تنها تیم میزبان بود که موفق به کسب سه امتیاز شیرین مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29802" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29801">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrunTL6R4kOZqqkXG92UxRPIsM5yVmULb7ELggnY99H_yqb3pMyRjCD1OV32Iiydm35Hb5HUKhjxNZIsnOE5gQA6bNCj5HPS8Ww4KJlG5xp4CVE8D77Ny5adR2bWkImiWilJAHzJXISyvyYfFnysPS5nPLRAhgGN-lvhvl_wiEXdg2_llN6DzcLa17MmF1EhyhLYVCQ1dAXLNl2U_KtSCLuc4NyX1tCpxMMHkLhcrsxfUpE8MDnLvms4V2R8ObviVNVKl6HmNv-b2toDjCy1lx40mwORYMbSzR_Ax0eQvtt1xE-QpAItVUBZyLsuP3SrZ2u5bamg21r8btCbs3t9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29801" target="_blank">📅 13:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29800">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRJPaDcNE6TdBVyOP8kggUqB1VKem20PxzMqclLOxLOW-jwpa_X-rHnj_XzbpF3HUqVUQY-555x7WB0ipaYxVdXfZwubgFtlO07lJkHKDaEPoKAsqSJYA2rth1fcTZ1T2baN2ldszh53JXzAqRmZ9Jvin5P4qpDb541JrUhTEPQRxKVAnxCcGoiTfJkUXuTd1wsSGjdG-AyCAq99F_BxL8Wb-EvSZpQGiqm8x0xkHh43PPHlgCe7yUxw6trcMOw5ckVPQiQSytOPp-CeEA0f97Yx9ZzSQdY3hxjuKCjYp7hlVOZoG3IEwtlviYrDFT-dDfeWqCdDlkPrVMszl-VzCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های علی قلی‌زاده امشب به محسن خلیلی گفته درنیم فصل با پرداخت 700 هزار دلار به لخ‌پوزنان میتونه موافقت مدیریت این باشگاه رو برای صادر کردن رضایت‌نامه علی قلی زاده بگیرد. خلیلی قراره با حدادی و بانک شهر در میان بگذارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29800" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29799">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhfKcpyx3pKkZmYdIv9kwCBjMcRSfRK5SqqiaSCdhwEhk3C40kgaWotp3K_TBYpL2BApy5ADMjsf-GLEOZw9hNs1mOnZq19g2YpETfKfgd-NLrB7tK9CbuPOF_K54Vspzt4iKpDkpzLh9waU8YRn2uxM1aRSP_4c9aByeYWugc1Qk67Brzi9f2wfQBNXeP8AWfy0oqIfyf5GlIB63Hmv9Wn02sehlNi0ebgUCfSKhh9PhDNlc0JmKFNthf61fQvn9161NBUgiAjB-1fXmb8ZrUw7_nUGq-39NZHcfLwoVDRBWD3ngJEvrtuvenJhyVmvFyONY-g2jkvm3VESEYYriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درخواست‌عجیب‌وغریب علیرضا بیرانوند از سازمان نظام‌وظیفه: مریض هستم یه ماه سربازی ام رو بندازین عقب که بتونم برای تراکتور بازی کنم!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29799" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29798">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8yx5D3cEp0zd-t-69K5DHPWJ2clzVKbsxv1HShHs6IBgxrsREv0SRQi9RK6ClCEB1u-WX0yZktd5GBLsgo1SG69FNzrB3okoGGX8NpXanB7xc9GHvwsrqFMu-xPZxbg_ElQDlbqNt_uoZuFlnKGwo8Tip6ijL0tVEMR5bumWmJ27wYXRXg1R65R7uobvG_UsUpHXq97CfEpVmKtVWQE24mv7bH9a0kkKE4p23PDiRBGh-idqnvEVAzUp6WEKvRAbr68lkTVJWRZ7rkGOWCB6JjZ3BRmMMDcxSiwnOBljHIIJvEQMSVJMQeyOuW9afCsQpod1hnblh7AbLz4JawSlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29798" target="_blank">📅 12:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29796">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0KCnlvJ0h12Cy1vP9LDmFZuN4qKL1gC-_MKI5WSHx1vuXlOzJYaUiT6CDGDnEgzNjcnD79uvygWVImJUWcF9T_xt1Mo3HeMfBUasWcg_h1mT_05PHwF_O1IFZYeaOUeC4cixvkrW4xk_Iqu8Iw11m2GoAPH8w3hQD4ScSB1fn2M0bXmcNkXXppLLP-p4_tM_dHpl0BV1O9S3ryVlk3CEwOHDG7z7Ermq-WiDbdd9lMVZnIc7SXzfXxJeCnUFPU8ZKo-CvN3ieoB1s0CnQCX-PkljWBwypNctUGK06wXhhAysh-n2bHdhQjvS4yGmcoRFms7FYCgVscRQFhBWDcTnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoogNbHRvXxjzd3R9aRQ87YbZ-0JlwA-fPYoAPuo9OG42P8K--fWOTjfbsEfvTPVdsmrWsjuvrbknxFqT_ZLwo3KppycjSHTMIu3x5LxA3b5lBZXJgU_5PccWvZYq_J9yO9IxxhRlbN0E8MKE4Tuc-XHSWcne02bSok_iE5W7sRy_Q5FEUsGkbZswr5bcgHasMWqrR_CHT-HZMW8x5CcCtSOZXvlq59dgz-eC1J_Jyy2PJh2tsck0rE0A6sa1qdEOHfS32r7qY6upGwzDdAw6ehJPvpBdrhboiIwSf7BCyhZh8LoO8JLseXz6fW1AISoKIhnJw3ALI2XpITPvoaQeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
تمام قهرمانان رقابت‌ های لیگ قهرمانان آسیا از ابتدا تاکنون؛ الهلال‌پرافتخارترین تیم قاره کهن. نکته جالب این که تیم الاهلی تا همین دو سال پیش هیچ افتخاری نداشت اما درست هزینه کرد و عین باقلوا دوتا قهرمانی شیرین در این مسابقات بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29796" target="_blank">📅 11:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29795">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0979ZxGPkTPDyw4NcnAg6MYF6ikgK4uc5OeqmJxAUq6gOsG7_9aKuNDYCFKzdN5gPxG3u89LrjmPB9KaLJL3X97S2ZzJBclF0Wr_RMX_xHy62-ISq-DhDFQVTfxrwZ2_g-lE-Ukb16W_Ag9XJlIZXolG2s_KE71ksKpfTd4uWUG-NjdyuRQp3vYuXCDDL_YTzx05CKuK7Z59rM02dv2KjhZv3dbp-JKrB8nD9lCQdyG9cnhNCM6QXWYueX82sd5A7HKHQSKP8Gk91VB7BIXcBzbYC6_aKICLgNVsYeEo7Fcl0dh-p86V_gVjYQ-76AYqC2NVQX_i7VeR42xRcM9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابیو آبرئو تا پایان نیمه اول بازی امروز بیجینگ گوان درسوپرلیگ‌چین؛ موفق به به ثبت سه گل شده که‌یکی‌ش داور بازی مردود اعلام کرد. نمره آبرئو در این بازی تا پایان نیمه اول 9.1 ثبت شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29795" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29794">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghynQpgIm8cJx0RosWnTR1IxQ6zoU3cnY-bRdxvuy-j-rwm8wNN0e0RJDpatxjpV32O1xoBP8hGRT8TTH9T4seG2h84jFFp3DkZLbpEN8PgaCQ56J3Sw0VfOnrhBskGkjSNpfUxKLEUOuPA7CCkrXaDImkGnMIO7_rVEvM1GlLun5JyOeaF4KlR5ihXP1xFlHyuPnwXf2Xym3WQiHEcnxxL3Sg81bhXUutn5UkdBFTpXZm-DOwLROw3ll0z-lstyKKT06cotBEzK9ra5aiQN5AkxwR8TtYPiLWHPymXCbXt7RpbdryBbqAJ6wU2vMmNKZX54X6zxMGac1rANcBvWdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/29794" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29793">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7gwMLC5m3Y1gVNB00gxHH0WktQEySeizM-B-yA6i3ouhRVafktgnfFIUxwjFh4tLwC6dW4o4FXrlY_22y1gvFMAp_xrCLS0RTo0ORcYa5wthSiaveHaOMx7B_hWGLzPz5N-nUDFiJlSwwACyiTnrIRROrWPjb2bPLqifld2vN1SwN8IRfgihadj9EDJQOHOCrr-k1ojprOUGbR6Rhiq8IOMBc84pl31aC1iipubN8Ctf_WnLWvDYxfRGu2fMjHYSZoTFge70v8owf3DhhrzZwvLsg-HO5DxLDCrkQ2kO9-Edq9WHN0jderp4W84xom_h7yfFnGJcWWiwoZB3olrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/29793" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29792">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29792" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29790">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKFR048qPfT8rc1iXHX8I80q73_N73Nx-JQ-NiMFtPLt3NhVCWs3Zfm-OwEVpgW3cE0-PuG2kH28r2Npi_YRMyZWsdC9EJM_fJgkUvdcChNrYftJn8get6aQp_ikxlAuJAeQz-kuphzjw-NOK7Ipj2r2Ki1PyISOXixzTNO8kxbs8pLwSdUBgkOP4vfhsBIPeha2_gKtb3FFkFSJSOUG9kK7XeWIvNQq3LajPPwaYbNUvma74kTA1sWzdfeqxy1y6s4xvniTUQPgridQyX3JhzYZbVNKhFJQ7i2WkGld48ZErsqRLcWbxY52g9plUUc9BNSLa68gz_UshsZkxv0xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29790" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29789">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSDqCMn0ppntHuotYfMEDLFyXwIJL24NyInLCcOat2LE8wEA-4pmzk2pXnnYkgpizeXIvxR6B4d-12eHBZgrufbaO4UGCLQi9BIlvIRo9hgg90HdTc9aFWOjZD6CQ83Ga55QcQfBEC8ktYmXrCjVzvn9M2CyM8rrrxiynd22cPOOa_TQa6dyVn5g4dTQNx-tm4d_Vp96AcuEDQYtCHfDOOHDYXmhvqzhZCq4fvTD7x_ByUX1ZxUeenE5grthTn_n4EtNxRgu2j44iG6PIfSKX7cOFKOm_5AznCCdhah0grTUtSQY2-4TRdSvsLTq6BuTsRLR01hvXUg9B0dhPfHWJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌کادرپزشکی‌تیم استقلال؛ مصدومیت یاسر آسانی جزئی بوده و او مشکلی‌برای همراهی‌آبی‌ها در بازی روز دوشنبه مقابل السد قطر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29789" target="_blank">📅 10:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29788">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agtIKAsanuufyrrNwe0R-IsYz0s8LgEO1iOrc4sF07C57TOb2xgiYZO2VzcUM94pgu379Ya_16e5efjCU_CnDkboWhsxDby0_5u-hpIw99oeXZ4rPy7N67IDn5jyw94gotKvDE2B4gVsUkguyG1vN4sqQ0CjmAHlvpQFev6JIRPX01emCQrejCEUJu-g8sF5vIr2CKBZl5w63dhqBC6jBEbH-JBqIaiAeD-_615FypSzcl1vv35uU3DKFKa2PEJQzX9rdJaJ65Rxel11dhlyUebSwmU2UvSxhYeFqKia759gzrWROs0Hh92Q6KR9zMYDFBXvAXtJRFj5mKOD3ZuTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودیگو گومز ستاره پرتغالی ولورهمپتون در کنار دوس‌دخترش؛ پارتنرش‌به‌حدی گومز رو دوست داره که تموم بازی‌ها برای حمایت از استادیوم میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/29788" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=I836BjIz0IKAWPIGSTQe2AO8zD5IIVBXbKp-BgAIrvkUXboRaLKc3Xpx_mwCJHvGhJ-Df-wnZvf6yGAX9g-pe1P2bT7tXBvr9YKw0PXfcXWMoocKObzlgCbLC6_5ypCtR2tt7tFLDDks6_IHINPKdezr0j200CyaxxQitJjrW2jEHRqs_LSNS_l0YyXP1tMbPhPAitawSbMDpgnN0TGB6IgBZK3wC4ISv3kSGTivuExXCp3UU8e5ts1IbpxXmNClxe_Q_QT-HjQwVf6rJQ80ZPCj8Hg9MJzEBebPRYfsGXwc9eQzezugyVEQLUa_8T2k43VBKmOBGHx-FpSoMDbUYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=I836BjIz0IKAWPIGSTQe2AO8zD5IIVBXbKp-BgAIrvkUXboRaLKc3Xpx_mwCJHvGhJ-Df-wnZvf6yGAX9g-pe1P2bT7tXBvr9YKw0PXfcXWMoocKObzlgCbLC6_5ypCtR2tt7tFLDDks6_IHINPKdezr0j200CyaxxQitJjrW2jEHRqs_LSNS_l0YyXP1tMbPhPAitawSbMDpgnN0TGB6IgBZK3wC4ISv3kSGTivuExXCp3UU8e5ts1IbpxXmNClxe_Q_QT-HjQwVf6rJQ80ZPCj8Hg9MJzEBebPRYfsGXwc9eQzezugyVEQLUa_8T2k43VBKmOBGHx-FpSoMDbUYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/29787" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29786">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkFoeU_ZU99S68v-lAmTfJ5KrNiI0ZDq7aGHrhJ8l2Se_LhsVJMRDxeg70qIt01GCa_jM6NhWF0VJpG9nQtiH0BTEnF9L2j8dfjVldC7-fOWjgbxuGgWwbx5GXq4mEtCUeMRq6dWAMEOFihPButruZ6S7YdREwnLKU4MNj5ixbOtnXryK22qdVqeiYYcUyEzDtTu6H_1UQb7eoLgESdJlDXqT_xg_9vCA64WAqTvC2jNUGCcfhwVTr297DNnVoFzBUjO8MHvuy7IO9bqCMoScRa5xQNw7by_jygElFXnynaxEwa7VTyBq04JM4-PjyiPlahTE4A5U5DrFFoOX9RBKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/persiana_Soccer/29786" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29784">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9WNg0He1cjJZYTZlLViJ_ILSxoTx8gEsfZSpIKEj9Rc94Q3XYObiwKoKum_s_Sj_uuJKmsH6jCPZ4UEJdetk9tIjevBScNvIAv1OL9KhkSofp4NarOQ-Q7qdYsYcJDf9sOhGNPA1OmebbaERoPNlrM8dhgl6NSzNQCZYE7uhY3MxmittK-BisspZK83HNSJmkAL5iScv4xrQlnC_XQJdc8_WQCvX-VKUj-5gBeLglSMmBtoGX9XoCSQ7nF52MDQ0bHtqupIgglbBe00zgi71MnJWaUxjCLCA7qVLaApkijnG0RIJUglkKIYno92g9TbxghWaTdvhox3aLFZoSp4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/persiana_Soccer/29784" target="_blank">📅 01:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29783">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGmkOlcZ824zsA6NmkdiSf06XUmTD5Fmc_HWzKsB36K_6wjo_q1GSHExuzAa4kl5m_yXS8ned9wn0KHW_oDW81CsIc0zRTHjMkKqx9df9FMKqITla7rvbUyheILEBVH477adTrFOZaCEh51Qrt3DrL9b9jjl86dIPzi-uEoJrnaJPV5_RkGo8vnqZaT297F9QKTG4Eq0ew50wY1fXJ_B1Uiqp-TM8ex2JiSCckXUAayJSpGGE39E2c4TOAuLCyBAVakScWRDXVvfnsafyvY1HMMkhLZqutwGZ_0mjgH2tx4KzOKCzklEaVkpD7rkaqhsYbaFncQ0pMHk4tlg3GYaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/persiana_Soccer/29783" target="_blank">📅 01:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29782">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnpU9fdNUwIhEgtepJt0PP8-VDYX3lU11sLOEfs2N5epVvLgCVsBttW2YkrnJr2FhBdTwn37bJQO68drAHR2FNsWjlu-tf5URs3AUzs5SbqiZgcKxacYk0xKQVcVNPgyIX10VbsOXx9aH4oaU0E8rlHgSsdQSQCnb8Nk-KQmO5NjC4LCxQrXB10Ef1__MKahX0S4RiXNYUzj4NxrvNALRQ_y_G9rPbuZJ3ipS5muc1lvvkFO9PSHyHwZZY3rsRj2x1hB7tNgeCnFVJdyNpQrOCuFTsxQADa3YSWbXHwSCzPXpgRm65KsvDwBWZ6N9va2iZVLS7RRyRtP_G4Gw0E5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ تقابل‌لیورپولیها با شاگردان دی‌زربی در کارابائوکاپ و مصاف رئال مادرید با الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/29782" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29781">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYpqLjOgxwfU2vQ0he16zEIMlTr0NISBLHvsWpBGzoDCNOflcK_mGrmWF9-HU_qA7TRTXm7PT3DyEu3yRuX9AqNpP83VTvUTsuJdKY560JDQlq_Jx_7atsvWxxw6Ct5GNuiZdoBD726H0xahjNadWApqG6USXWivF7uEUCytfgYiRABwbBkjWVlDgK84vgp9MgowK8RhXSTYxm2RqdkgseHJUnhnAoY-kLaoOkRFjVh9Ezj1NJnNmCte0CrSvlHcturbErvnlg_FjOsi7u3qcSDGHwL0mwGgFqrOfKrpo2aIMbDtWa-hZwSrHlOsaKXC_oQ4rXrpJi9hpjRnt-wfiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرد شاهکار استقلال برابر قهرمان قطر تاصدرنشینی‌یاران دیبالا در سری‌آ ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/29781" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29779">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXrstNPmIh9Na6m3zGh73MzhOG2lRDPESpTq1LLlvYv3_xkqUoRdEWGvJ_WGCImH7UNctmkuN4RqgBhU7Gq_HLa160yKYsTdC6JNay_7Ic2EaHdMd14ls4ov8vMSIv2Uu7f8wuKwvcwYyt8rMqwn-Sf_6ElCNhSNHGm9zTiqwW0x757XsB2KNk-y_WSNYbB0j3K2dw41e9G0v8ERU1pyM8Wg6-WHeXhK6lXnWM2JVP5bapPb-juXJpmvNhUvzsjs9mqjIFgnPNKFNElrJEezS4Y67oF73jKwP2eX0LcwqMrX91y-CvlbakgeEW5go6SlEUc-gyqffOVRwbd72MnyYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیربرنامه‌های علی قلی زاده که رفاقت نزدیکی که با محسن خلیلی داره با توجه به چراغ سبز علی قلی زاده به پیوستن به پرسپولیس قصد داره این بازیکن رو در نیم فصل به پرسپولیس بیاره و صحبت‌های اولیه شروع شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/persiana_Soccer/29779" target="_blank">📅 01:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29778">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFLZkeQTUwSA5QyIBku7HaANcIDGPLbcv85tsEniV5f1K1Vyev7MJ3Q1Z2i7M6Aau16ylmYdHjTXPztwq1Pc7SFPn25jomBhFBDbTG7nfx-UWIfMSaNfofXqTnB_2e4ISCaMJf38ceJi-NjXw8pd_gcY_26jByTh_l9XYD1DxQw7ksaCUVgITjPgtP4GY2xkBnb9szq0r_Qxkgbc5p33fG9tTPQFaI-l9HGwVfILOfgXTktUoFnNtL19ZwyZOJNnMS8uOmsVhup6uKiGzGZurpA5O23KkZiYCRg6pK6VnEGjKqgGpXXTnKtnFPSRThnLUDmVfJIrhbdnqGSuFcia1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/persiana_Soccer/29778" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29777">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoaMzm8YGs-j83lQgeb3ZVeoaCGLKTh9eOjeanq-Vw-7NDoLHoZgh_faSFDub9t6ewENsujCBiEeA-Hgq_iFgadV09_A7_Wh8cNVhQ5izJgcPcHiZYk_SjDemOBzH0PSdFdnKjyzu0Wq5fuExSNM1bnMPcKWdJGCP-RVHCtMNAQnQ-ujtr0IoLIG8IzU9o4eD4zoIF88pcsYmGKUbJtMcUIQOJUiZXNCyv6TdQxDq1OwcPdtIoQ6_-M9DiCsahXDCvpNmOt_OoRROBXbdneclkfCB-eN-Jq22HqVoVWnwDVWyy1WnGiBri9T15rKpxVop9HAsHnn84I5-3IpyVlyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/persiana_Soccer/29777" target="_blank">📅 00:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29776">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqu-blekwNlj1ehyq009ni8m_PuxQzrSvhUYrPuXHpCT1HgvHSaqOIP4TprBHcBWsCxXrTJI9MuRvUIc07kZka82ZlJDUxd8M2slf3cmtgj_kCFPzP9vJGicuva8XUyxitGcFbkx9RUpSUcwzhtLUGm-6MHZQfLAXZO-_yxyBXs6Sk2HWYUyVKvztgmsXHEc5ABvI6qqaNoeLO2IIIU7APXUW3zVl8dWJ6fkWI9eWx4XwrcmOrmjJ3QQa-Rurg-3nNq9jCN82A_J3kR2GV_EPIOxcENVl_nHArBjiVyNIifrEZf3S5sRdSFZcddvEtV8qseknpB5immbOOeYomQ2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال‌ میخواد درروزهای آتی با پرداخت 800هزاردلار به‌فابیو کاریله پرونده او ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/persiana_Soccer/29776" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29775">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0F_wW0ZxP6X-B20qrZxCNB5B5yXcP3iStYkfvs-1bPcOUxnupAvUigMGstJoKq6MJhhzdvVCOeWs7ghwspGWLDGTLKs0YePbXdH4juJobmiI6xVordGojvDKlXLJWO8ZFS95DgqfofhJ6hXmFtSzfMuCKqQG4E8J-pbwcSudlpsPTjQG0VwyOpcKOJ3uYZFJP8j5LUXvOuYgSDfqXeqqJEDZATf6SBGoyneVS51seEy15L9OMEvuRUF6dtSCBy-i3T56gGvbiULPzjT5Bh9L-bg0n1qJSZrB4POa_F93SXKr0oC9zrBmGE4JNN7vRCL1Y6buDc5cJTHZ1xJ5aMQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم سری‌آ؛ آاس رم گاسپرینی با دو گل سه‌امتیازارزشمند رو از تورینوگرفت‌و با چهار پیروزی پیاپی درصدرجدول ایستاد. شاگردان سسک فابرگاس هم دو بر یک ازسد پارماگذشت و با10 امتیاز در رتبه دوم جدول رده بندی سری‌آ ایتالیا قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/29775" target="_blank">📅 00:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29774">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEnDiXnd2o4LxRFDwiex56FSGDy2ICCYYgqmjyGUjqJw5Ei6US8B2AkZ6K6e4ENCfP_R_oHp9RxleAE8svpv9Z7e_90H0-RvgD1qryLKqF2LSJdG4d3dyP0_VaVUZrGScF1eQmUpFhpXwLx4BTbSfbGdPs2G4DD1va0uoz2QZOxLoPSwyUIGfOYJu9_BRUEZ8s0FM2ZqtG3b5ExqWXThhZD1-PUPW62I-SIAOlYP8GELCudmaR99l_zXCGETxJdnSGd1iEVZi9tcCNcNWLlA9Mrkov0MlFgoH_ePlUCYszV4YM4GF6PqvDCx-esL19rPWBeTOLqfiPClpDjiy0ur7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/29774" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
