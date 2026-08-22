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
<img src="https://cdn4.telesco.pe/file/hjVexr1im7Me5ZaS5Mk9Ju1IMy0w6lo34zzGXriWtMMQHP4D-86BhfrJ2n2fkAK9vXgusS6kj-PBNcckeDWLlsFnJVRbuRh8w3NdXL1ePNh3zxSgOyZzfXdQrHHaoGU7E-slx9_wh5U965dZs4SL3dPtkbjeh-PGbVjz68o4KyTEZ7lWzs3d67tHZD48q_z4v-B5WOwmM6d1uu2_kWncEIymShvI8c93qtAl7E9lRK9Fw-3_-kSPf5MOjAdSJLBWA37Sv5AlEdfNhvmoS3MA5D2FL-AIq2dt__PMwPeINY2UtzfYRitGNeB-BWQ0Eh5M7wxfBXSr-dtNlBfV2ZT2zg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.53K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 01:12:59</div>
<hr>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsFDbB5XRpd2qRp1xWLuGbVTr25tGhmAeucObnnn1RbG38kGE8DEccIqlmYVcH6cPoOFfnVkkZYa6gQhQmL5FaLqH3JM7Re86Ju35KofBN_HHnuZGJaOIPRZ0cac-bYdSOj23mvYn-SmX3xGtY8LChXph2HJTMh2YHmfDaeJ__QqSribXWs4DIpz5J58pqgqDAYlCI5VR_DVS4LLvlTDl8c5RvyqviLGAaR0NUhhamNAXymOzRDtzhLpBb0HMTB_ylFs51U_RB6c6FC7RSl53OcxRcumeFquGdPu3LAfVZ-DdVgmXWjhbWnkTPEyhVKOw-5E1IUBZqqrGcojrvePmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
GLM5.3 با رشد خیره کننده ای معرفی شد.   z.ai این مدل رو به zcode اضافه کرده و بنچمارک‌های جالبی هم به دست آورده با اینکه بر مبنای مدل قبلی کار شده و post-training شده    @danialtaherifar</div>
<div class="tg-footer">👁️ 295 · <a href="https://t.me/danialtaherifar/952" target="_blank">📅 17:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvgI57VK3S9_yVKfqlu0ukyj7N-lPXRjXtMM9Esn3kcfP-yMtlLFCSLagAkdFYQbJSlAnw3946WRKQa9nh5gYGyjiEP3P1yavXdFS24P947Uz8eb4pBHA6FUDFlli72N05JeFVm7-Esr9xw81molDaEDlpgvbfuW5NMoIASvgr2pFMX6HjdaAPL7ZxHcZIGG6l4UiAJs6bgp7TbGaDKCJYjeaW0J4i6UwNFLiTtWr1Nm9x7fRMoyjvDMk2bmDHAZaUpvyzyiN8hRGrxeJKWLOPmueX9Udy9719ICRg0aDrhdZT9t0KTIms5djbVF9EJKi78XvEjayGTlWkf8b98TdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
GLM5.3 با رشد خیره کننده ای معرفی شد.
z.ai
این مدل رو به zcode اضافه کرده و بنچمارک‌های جالبی هم به دست آورده با اینکه بر مبنای مدل قبلی کار شده و post-training شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 355 · <a href="https://t.me/danialtaherifar/951" target="_blank">📅 15:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-950">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UogUKNWiE498fqwxQzZzQnUoqfb6cj9K0ICC7D6B32OI_931Kh3-dniMogruAW-LCostxy0zOyXrwl9tmhEbl_4pcRWJOtO8T7gad2-o-cbDjeyJA5vuPUtgiMtHdXSpbsCZI1MI2fREMlFJ7N3onJ68fqnd7w5bcxRrRG2k6MBISd3ObgF7m2XADUDVvOkxIwZ-oTvs-qQJjcPE4rMOICXclgJq-xAMJNNRnyE7GQXN2j7f4uy-cUf6dWOxvfA9PZgtI3O4KjvSQtWB1H03AgeDEx15u8vhGJkVtBBVJteI0Y3T1D60oA8fGIZSZek3o9XZE7AbMX2n9MTgUdLrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اضافه کردن پراپرتی های سوشال به سرچ کنسول اضافه شد به صورت سراسری
@danialtaherifar</div>
<div class="tg-footer">👁️ 560 · <a href="https://t.me/danialtaherifar/950" target="_blank">📅 23:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mE8b-RqVgAN4cT52_ZgrmZMPO51t_hkX-aZNrsEtHYgLWOj_HvUuZLx-46iHUf3emXhaSVeqOXxpU0RztEXTTPIpbpScAV-bHeWnw1ZWZIhNJHuk5-XsuXxKqY1qmw3TAHJTm8uJoTi-NBkA9zoK4BHBggk4PZX7JH1Hzy_9f9oSeNCVIxTZShdnlJBFjRqe-Fk-yi6UKb9GW9MdaJJQxzlzR9a6idz8R7bATRkgK0o4WEe7dsaGEm7k21QqVrRgkkivXkoQ5cwRNmrhTXiAvrCZlPX_FIkjUBsA4gNjUlmOHGHSqxOhC4XXb-UtMCVAh4QDDcAYrNA0KLzRsLmjCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfacG4fx44aj3_ymSROZF0U_XLxXVEyd3ytzK9xLiO1SW1DWif148Oj6PKQ_EGjLeDOs0RCNFCTtHpiqKZ_2VGiMQYG7Cu5vi5SMJ6Ji2HZAPdHRTjhHFf74co7f5xjE7SZrP6YPB73q22nivS4zIgl-G8NQbV3pjsNJU0kZ-1CHtYytWdEIkTKfejpfIO61u8BWt0Ezm2WJtr_K-6Yv7Y0xQKFGoc6QOgq9TiVTxLE3thzp_XwKHGNzFOnOHln08a_05zTglLeMQ-JuydtQwO714-tPhPzp7y4956-hhXLVEMow3iHXNQBCllcsKujZrFME9ws7y2oz9pHhVzfQrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😒
کلاد ایمیل میزنه به اون اکانتی که بن کرده که بیا fable5 استفاده کن.
دلخوش میشی که شاید ....
و بعد با تصویر دوم روبرو میشی :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 658 · <a href="https://t.me/danialtaherifar/948" target="_blank">📅 14:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hebud06rfmgwHcnPTBRe4I8H3lNSyIz0_mFCxy8vJ_n8PCUsjGFoJIBzRWiqmqIkXrN-Nog6UiliqJbWphRIG_QVFqAMoqfdWubTzqhMdeWTBFdBn_f2HKkVdvwzGoCEn1XKl7dHRpt9aeGy3slS4Ul5VH57F1IEfVa2WtpKf3RkzvHL-OcjpWHuq30mXpwGtU0dRVkVL_JMnA-oEm9gDRWkErqZnA0RfTjXWbdXGqyNVO6VmSTUrJNyRLLlSuuzR80cbHj10FK8npcMbEQdq6lTtupcYWXnOo6sFA_BVJJlhwMP1ffpYhXNMPpNtwSVx7--3vGGh0x5rIi2EGI7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌بابا هم اعلام کرد که مدل Qwen 3.8 با 2.4 تریلیون پارامتر و به صورت open weight به زودی منتشر میشه و در حد و اندازه های مدل های سطح بالا بعد از fable5 هست.
خواهیم دید
😁
#ai
@danialtaherifar</div>
<div class="tg-footer">👁️ 618 · <a href="https://t.me/danialtaherifar/947" target="_blank">📅 13:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این وسط با kimi3 هم آشنا بشید!    یک مدل هوش مصنوعی با 2.8 تریلیون پارامتر! و کانتکست ۱ میلیونی که عملکرد فوق العاده ای داشته و در سطحی نزدیک به Fable 5 , gpt5.6 ظاهر شده.   این اتفاق بسیار بزرگی هست برای مدل های چینی و ما تحریم شده‌ها از امکانات دنیای غرب.…</div>
<div class="tg-footer">👁️ 619 · <a href="https://t.me/danialtaherifar/946" target="_blank">📅 18:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSFDiMRP0JK66h-s80gFHJLszy3i0HdgNuBEYA_wSA5RkG529F45wN-trSI5imgqnYBxfyWrlaAhF100iRSoe7i28OaHFtRfsoNWB8x8-qjoImOSYlUNwDYoYkN79SGa9-8X2cPEtGe9RwKWwRwGirL4tlQAwS8rFQ8uue-ApWkGMtEY3A33oZXKr6arosLuOuLw1X2NNqmMwP-CvO7MhI-txgCGLpk-cqGzOQtcIBalhNdkpRSjubTsBxSSV6uFML0IsrQM-Aa3j8puxFrrdlt1Z5SqtqE8mxqtPbMB1TRRuurVXWFdOCud2seVDgADl4NUo0YBKS45sjQIv-W-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=kVLSf_wLw3Gk3H7clktvbl-jx7zcmS9MFU2eMpghV0CAbzyFYqRBTxc2kkQqp-ZY8OyGK89lAGiUWIwda1dD7x-UWvgLVi2sEavM8eV-d0aCbLqCVXntFhWkDhmYa1aI1xK7yvABg_UTLf4mDrpErRQ_p85gapkvu9r6AT2McifNApSK02ucZVslXCDeJCQoFhsijws-Q0MBFXiRSJjj0D6npZyVw4zJ_9OPpr6qw0LXCwRTNnxYKNBHRpFPHvsXELwnmu0OGTqg13AYfwSbanZvs4h-xMDKcePcMFL9wNNXT4fFsYp_r6OixQiClEIvWsrXyNqTvkBnX_AzmRrenw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=kVLSf_wLw3Gk3H7clktvbl-jx7zcmS9MFU2eMpghV0CAbzyFYqRBTxc2kkQqp-ZY8OyGK89lAGiUWIwda1dD7x-UWvgLVi2sEavM8eV-d0aCbLqCVXntFhWkDhmYa1aI1xK7yvABg_UTLf4mDrpErRQ_p85gapkvu9r6AT2McifNApSK02ucZVslXCDeJCQoFhsijws-Q0MBFXiRSJjj0D6npZyVw4zJ_9OPpr6qw0LXCwRTNnxYKNBHRpFPHvsXELwnmu0OGTqg13AYfwSbanZvs4h-xMDKcePcMFL9wNNXT4fFsYp_r6OixQiClEIvWsrXyNqTvkBnX_AzmRrenw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط با kimi3 هم آشنا بشید!
یک مدل هوش مصنوعی با 2.8 تریلیون پارامتر! و کانتکست ۱ میلیونی که عملکرد فوق العاده ای داشته و در سطحی نزدیک به Fable 5 , gpt5.6 ظاهر شده.
این اتفاق بسیار بزرگی هست برای مدل های چینی و ما تحریم شده‌ها از امکانات دنیای غرب.
من تجربه کار با GLM 5.2 رو بعد از بسته شدن اکانت آنتروپیک داشتم که اونم سطح بسیار خوبی داشت، اما قابل اتکا نبود برای تصمیم گیری ها، و الان امیدوارم فرصتش بشه که kimi 3 هم تجربه کنم (اگر خاورمیانه بذاره).
@danialtaherifar</div>
<div class="tg-footer">👁️ 646 · <a href="https://t.me/danialtaherifar/944" target="_blank">📅 01:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mozHzwk4OsYHrcq8byqc5p_7LrGutxm_PzTwpOYOhX1h09iuVP_YmSbCJ4smNljE2dr4j3kRthzHcC-84NPT8-u8dhFwuLKZCst054a8FGp8fhLt8y0mRj1P8asty4bN7FWgsTfF_HFbreuorXNvQKHOF3DfoXekhsunqvXoeiTJo6toZdiNZKlZCeBKCnuWQTws7VK_xckj1ThjA3aSx8hbg_9CCdT_sfp7-HUczmN4s4-i9fABm2zNKro3vHfMma6XZ0nLxiBH6fssfI5CpHnShlSBojvTHHu-ytcc0Jm3hY9oFeSTBMDwf3KanbmrtDiA6FgJWDaMkpOLLeSxOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ظهر امروز اوضاع نت اصلا خوب نیست و رو به بدتر رفتن هم رفته
کارای مهمتون رو انجام بدین، احتمال هر شرایطی هست مجددا
@danialtaherifar</div>
<div class="tg-footer">👁️ 539 · <a href="https://t.me/danialtaherifar/943" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-942">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">باز بریم بک آپ سایت هارو بگیریم :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/danialtaherifar/942" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-941">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">📚
۷ ایده از Phil Chen درباره آینده کسب‌وکار در عصر هوش مصنوعی
چند روز پیش رشته‌توییتی از Phil Chen، از اعضای سابق OpenAI، DeepMind و Scale AI، خواندم که به نظرم یکی از ارزشمندترین مطالبی بود که اخیراً درباره آینده کار و کسب‌وکار منتشر شده است.
خلاصه مهم‌ترین ایده‌های آن:
۱.
هر کاری که خروجی آن قابل ارزیابی باشد، دیر یا زود خودکار می‌شود.
بنابراین ارزش انسان به سمت قضاوت، خلاقیت، تصمیم‌گیری در ابهام و اعتمادسازی حرکت می‌کند.
۲.
کمیاب‌ترین منابع آینده پول نیستند.
زمان، اعتبار و روابط واقعی، دارایی‌هایی هستند که به‌سادگی قابل کپی شدن نیستند.
۳.
مهم‌ترین مهارت، انتخاب مسئله درست است.
وقتی هوش مصنوعی می‌تواند بسیاری از مسائل را حل کند، مزیت رقابتی در انتخاب مسئله‌ای است که ارزش حل شدن دارد.
۴.
به‌جای ساخت راه‌حل‌های موقت، سیستم‌های مقیاس‌پذیر بسازید.
هوش مصنوعی سرعت ساخت را بالا برده؛ بنابراین مزیت پایدار از سیستم‌ها به دست می‌آید، نه از ترفندها.
۵.
تمایز واقعی در «آخرین ۱۰ درصد» ساخته می‌شود.
AI پیش‌نویس خوبی تولید می‌کند، اما کیفیت نهایی، سلیقه، جزئیات و استاندارد اجرا همان چیزی است که برند شما را می‌سازد.
۶.
هم فرصت بسازید، هم از فرصت استفاده کنید.
برندسازی، شبکه‌سازی و قرار گرفتن در محیط مناسب، کیفیت فرصت‌ها را افزایش می‌دهد؛ اما اجرای درست است که آن فرصت را به نتیجه تبدیل می‌کند.
۷.
هوش مصنوعی فقط یک ابزار نیست؛ یک طرز فکر است.
هدف صرفاً سریع‌تر کار کردن نیست؛ بلکه ساختن سیستم‌هایی است که بدون وابستگی کامل به شما نیز بتوانند رشد کنند.
جمع‌بندی:
به‌نظر من مهم‌ترین پیام این نوشته این است:
مزیت رقابتی آینده از «کار بیشتر» به دست نمی‌آید؛ از «
اهرم بهتر
» به دست می‌آید.
هوش مصنوعی دیگر یک ابزار جانبی نیست؛ بخشی از معماری هر کسب‌وکار مدرن است.
📖
منبع: رشته‌توییت Phil Chen در X
https://x.com/philhchen/status/2072793818945167475
@danialtaherifar</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/941" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnZFCB_p8UqTT6oSfw8sK5rE1meL5pyFtO3vIcMEA3qHS8VdAnXrSvPcZmD7h7JHP1nlObjcEN5ReMe1FdZ2v5j-ubkoFI4WTaYUjoM9XqZUFM7YciiTmhvfNMdTxs5FbenOV1Xq4NCCTTrf_EJNQMiufwU1HBMgk1DHeCIpjtfuS4kYtbdtOthLWxiw44K6sBmZ3ckz63ysVzRVEYF5czUcX0LGaqAaUxOYGRKf0WmJ3cH4Z-U3x_Pcpo1ptWk9qGYriXsRFgFu-mQOdp2Dhl-sr1AVS1iIjE_mOUt699tvjFc1ODsZ6PQcnvXYBAnPeaCEX9GjT5mhuq8c4VcvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=Uvnj4F66kkMYfeq0q9i8XNhgq30NmHCvEu-MOpTAenHVz4Psxi3LQcuEOW1E2EDEecWTpf1pCnoyLc6Mxt0jt8JVVRrKxCRNAwRYgBSDi48Mm1qzwkDZR20Dy79AiIFZrzjSzOczGfagViKlBQ4P6f-rcWHLvv7cANCwlmhiTRLT2UjqKavFvtjezy_I8PQ4EVeNEl72rUsM4pYMouhGKV26OQo78918-sDbC_FXipOhGcOy-weIgoKKD9DDW3uY2bO4SocZ6Q0qdCol24JilUERzlxzrnSuSzXCbJbM3xjQX-FBGVIEh8nrtz0c0OK7FllGluct6gurA--wCb2hOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=Uvnj4F66kkMYfeq0q9i8XNhgq30NmHCvEu-MOpTAenHVz4Psxi3LQcuEOW1E2EDEecWTpf1pCnoyLc6Mxt0jt8JVVRrKxCRNAwRYgBSDi48Mm1qzwkDZR20Dy79AiIFZrzjSzOczGfagViKlBQ4P6f-rcWHLvv7cANCwlmhiTRLT2UjqKavFvtjezy_I8PQ4EVeNEl72rUsM4pYMouhGKV26OQo78918-sDbC_FXipOhGcOy-weIgoKKD9DDW3uY2bO4SocZ6Q0qdCol24JilUERzlxzrnSuSzXCbJbM3xjQX-FBGVIEh8nrtz0c0OK7FllGluct6gurA--wCb2hOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhZXTe7M32Tfd5X5rM1YZfOd4GdaG3__UYK_88oiDgSSp5hbq2NaFASIeVvx3bWZWF-fTB1QiOA7L0arajQYOJSTKKjPrXV3DDm7HUdp5obRdZiC0PD0W7RQ2i4cwOec-wyOb_Fm-EGzZ_QAGhmKZJ5YalYdMwhwXx8OXnaWJjrrXFv10U-PO3VrjgwHzlL6iVH4SlZWUvZGCuc2IkPjCiNPzZCJLwQzOZAcpB4ctdfUqWvRAw9Nv7BgmWt6eMxDNKWYLKnejmBUSiVsW3EMSsOAateDnkQ4B-VcCv3Q6BDMby6yjVYoByQEWPVZjSxqhlsaEbB1VGKsd6btpP_OyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 870 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 826 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DO-5bT5kiRFr3hqE4TqkoFORBRRdrZ--rFSW8tiq7y7YXBjEVa3fD6qxCww8jEsbLTfy_HXwZtSnBa35rt62Z7qt3zcsZXRqskeWfdQgIQXHsLMi38bAqXvKh3AuGMATPNXhm63qYW82BG55bZkql1TLhSyu0k-e6gQMIPtp4YLkvEE8rUF9Eb7eEoXZITFj6SwcPlVJ3yxVJxcgKsPv8LMTNEvYHUT5X-OXMpDMBx37M1D0Oa_uQMwUaKJfwUNCw9qFF_yJ51SQ_roduN8CabqEM9oW-n5cH0DztuLbQOPuO-tD8e3K3EmCH0LxzRKiULbQXOK_hDrInHfXQA7JAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faLU3HuRd8Nc0eGymx8GXvSBabdswQ95Xv4ndbGqfR1h6ldWJ2DhVS223NDxOEdxIyyL8kBUuERYAzVeVkHWSMCXqGc1I0I3ByUGrNv9uCTfZN4sUUCYrjq2hm0aYGIOzLQVsl9gdqIkhfsjMJY-gGpbALpoLkbS1L8WScKGlLfrcVPTdtr2JBLVpugCychpzkgWhz3MFcTwNlNvKttOF0dJYptHHGKyZB9Px9t4lGbeN7or0ku3FHACLBVLOdjLXfxpJ_XTWhIBOGYmdQ2fMmoYHe3QT7fQqpGwDd0M0dS6zvkJmAGVSGzFr9U36LgazacdiFDL4txKt29Lzd34fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlvU35ZqUt83UBF1irp0IONy2F_Z7BnV3IimEYzTd6UAeFP_tsx8NCJsSWpFJtWlndbqXEA0Nif6Xz-dpMafmCDMe5Y7FvfnOhd44Xm54inhdDICRA2uleP9UsZ1qu99wCWBFW8T3k7hVOczlyGBlHjn0NyOKX0J1YKslZU1HQstbJiDqnBqKRHNNHT5EvEdqzNizUtHIImHiV22pequkfG-AQvFctSjAX-EWpaqjIoU5vHGSuPh2-0XaDWAzuSeQzoPUPpxJPWNX8WQeDsGdB9C26P3Lwv2c63ryk9kfgFEBTWWi8RcyZY8wG-Z_MAGOVjkTevoyClHKvbE6hhRYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNZP1fyzOqmvmChur3uqnPuWyUmj-_6J2f0di2ivoWWwrAVNqoc1EVbencP3BkgO-kwMRGptoZ_Vcj_Zn1mM41dlq0lrPEtGZBbdsrXs1Q4Sx-LirIa-MDm6w889o50CBm11S587LQnlxh2BVsXe9JWTOPiuDVRejN7FClDfvEEkJoj_TW3k5DCMl6U9gT96gd6nnNAjMVJZ5lqYYt_8jWAym44glV97nURYHnS7EYj5sv6wx1yGSpGbCNKLPV5i8X-ekt-hAA8_I8tsTqAEe04Xu5rTTiXKhEk7f5eWXs4RB_o_BhjIf75gzgtfIEzuefnlIVI5UnrCM3UeiHtiGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9jqPOf_enCGWCFS9N8SAHGl7y-77OcFARgFTPGKuGtDrxt0BG5NltHt8Yu6MNsiRjkWdFlzvBmOmPl6uoDRN9QEXkLihAWrcb3pA7k6T8O14AgHUWgJOXBLG-Hy9feiVaML_VnhjTbLbJt3hAj61yYp_GRNyFbauov--4egKjDj4_lkqXev5MOTZullv0Ur2SkCInwKvIi-FO18pnBBNIyEgve1FdHjKAIYZAGmGzjfs0aIGGOi5vN11lRx4P_FgxyZRrhK64_ktnrWbw7TSv9Gpsa_vRmdGcRyuQHdvvNdd_82NpqMWW3uDiu5glskQ4v00mu_9kUnXDntKCa_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdXebt_PEDd-6Bbpt0hZFhgApWoeamDuHPok236q50OSwym74FPASLGOWuoKaBBzR1DOEDkCb0iHQfyUnamxD6uLUHBQ_qe5AFUeb3aLoUmoKKDB3ePctWwAQ6-TIegkQPrlmjGYBYDMmiP3hUl2qIsKS3VIiF60ShJGAX0Rx9IxPVr6KkgqzF5d0K7NGPvALwBynbfdgdvaiaAVlyuoldoQSgrzE_0L2O5-SLHUqKbgaPI1Tjk-GGYUlWbNLy9FwwOQzghDKzE2c6_2CAbqMy5azBqsNmQHMJEMSqCuoOoMyKSe-GLFdYTH9PucjdY3QptWj4CazcoruxvVFdql_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0WzgKUY2jtnSgCXGWgyzT3vYK0b1karL1EpNEVMDLopUpVC90IG5HzPyl-RpVyqdjjlacx7ol7bhM0Id1NMlAulo-Lr77bbo27rHnWzZ_wxbJx5bkDRfDrX9T0o6YC84vHg1_4BtU3w5sl9KUxKzX-tF2Ugdp6N7Hu2Jr2BYCJ0UFQ-f4gkvuojgxTCMj5YRZBfCj65hq9WIR4ZkOvFUzfLxnA4rgJmPRxlpTS88s0C1upVtp04cHATnZxriALvYVQgxQSRueBp8XUonS6otWWbYDAW2iX9NwafBfsZyg8qeIvODLZE3ZbpE2r8egrO2TuFWNNm-xydozz_L8NtHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1K1_Nh9I_ttLVAal002XMo0na1KX1p1zOXROp-pQRwgMUbwkLpNKUc6jDCDlF0tUYgD4ji6wO5mCRKJx9ieFfr1_EdikVTd9fd6TK5Uo-GkQNHsJHWZJREq1JuUO5RbAWex1EgLWyR3YBGg7B3XhewwH3THSNCIEVLmA3B-4CsPrZTPAw-3vd-W9_i3iI63iS1lHsIoVODNkbBbXgbUPEvZCD78hAsccKB5tXucKkJ2LpkS8VqpamUWdUDXe39AiVRvcn8uLvQsU4ghBRUkFQ7nQu06JFEbQtOJsD-9KdEsBhKekqDROZJDMieAbx3ddMfDLrqQVj5JZdlYj77UrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daf7oHObiWdCIBrhtIYhKyB3Xx69tHYRfT-YsQVpebMociHZoeNHn2yQkZcym4ffZGxJdo7aNLo_ngH4ZruthCY0Yzn7T_BvMM1GS9TsL9_GBHq7D7iJtPf_xqQId3usF2p7eVYgpMgpaaeAv9LC7DQhAlH84tYCj6rY0tb3p5ACwCch_7eR3DLkGvseRvMCIJTwd4hSrQxs0RS4aSXClARCvG8iMIb4oR0BdNLz8FdmPa9al5juxemXmbGyWm1mXRYsJ2VUnOtqtrHlOK0cD9XpGfEoy9mxt-S9CV9TpjOsVUW7umNGWoIzBYHKI0QqbhpQvVsgIhw-aO5yj7fiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 915 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 863 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
