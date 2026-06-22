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
<img src="https://cdn4.telesco.pe/file/R0QujRp0kFMGFtf6GFXynj4rVje2RDKrKsBeb3RNzUpdc3X2eJ98d2R991Ej8CwSnFNxcTHIkRoao110YM8KpDwMsdSbQ50buVGrNVxD5-hn44FWYbOrcA0yKc2Ggo_YU1RYjzJo8TG3j1C9FbnXG_2nKZFR-kJm6gk-JxQO0HuhCTR29-3V7RDsfdRqnZZ3xdIxL5T2ziIcQRcRjd9N6LhBknGb1B0Ux-BJ-93N28C-HpF6jN-a259ATY9yZhzh1IlF_Gg70nMRru1zCHv_C9SvwahXvUM3IFeFHS4V9nx7q3vCVsOw7Uo384ZLFktqSslbpccLKgixcSS7IrUsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-662171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سخنگوی هیئت مذاکره کننده ایران: تشکیل کارگروه‌های فنی برای اجرای مفاد یادداشت تفاهم، از دیگر محورهای بیانیه است. این کارگروه‌ها باید بر اساس بند ۱۲ یادداشت تفاهم شکل بگیرند و قرار شد هیأت‌های فنی دو طرف کار خود را ادامه دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/662171" target="_blank">📅 10:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
دومین کشتی کانتینربر ایرانی امروز در یکی از ترمینال‌های بندرشهید رجایی بندرعباس پهلو می‌گیرد و بارگیری می‌شود
مدیرکل بنادر و دریانوردی هرمزگان:
🔹
این کشتی با ظرفیت دو هزار و ۸۰۰ کانتینر، پس از شکستن محاصره دریایی دشمن آمریکایی علیه کشورمان در جنگ تحمیلی سوم ، در بندر شهیدرجایی پهلو می‌گیرد.
🔹
این کشتی هزار و ۳۰۰ کانتینر را بارگیری می‌کند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/akhbarefori/662170" target="_blank">📅 10:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
سخنگوی هیئت مذاکره کننده ایران: تشکیل کارگروه‌های فنی برای اجرای مفاد یادداشت تفاهم، از دیگر محورهای بیانیه است. این کارگروه‌ها باید بر اساس بند ۱۲ یادداشت تفاهم شکل بگیرند و قرار شد هیأت‌های فنی دو طرف کار خود را ادامه دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/662169" target="_blank">📅 10:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رئیس کانون بازنشستگان تأمین اجتماعی: زمان پرداخت معوقات حقوق بازنشستگان هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/662168" target="_blank">📅 10:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnjjCRDwstb04HeYzc-SAqL41m1EWbeOz8qTQujkMZCJjaYd7660SEukYBHg_gE7-gDxkhDg3uZhAfuIogweFXcvvu5G9irZ6bFunh1Az8qC2jJxQrZi0apmvtHC75REn5_C5lGVZMLNJGiDI6y9ncHM6bQ47qogvSIZbLPHSLAZ2fnta0mR3ytP8lfSnnTfeiJ4szhYc-YJMb4pyINbjbMkW3MTLr6tLiKy0j3vERxd2Rm7wGMPAOwqZt06yK8bXwYGcSn33rGK_i-0t7cJiszl8SktFycNmFXgbjkU6gNJb732Z_ykbYMZjZyg2rfD2phUsbmIIZLPnroXMdNpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل دکتر مصطفی انتظاری هروی تحلیلگر سیاسی از مذاکرات دیروز سوئیس: عبور ایران از جنگ‌هراسی و مذاکره‌گریزی
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/662167" target="_blank">📅 10:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prr1plGYPNiqDhKBOcbVAWzjdG2eDyGz9Xm6Z7FO-IblpCfS715A7qb4tAt8KH7mPDEndvGDLQKjlFpQQx75N1y-Xpp8Cc63bvIyPvrPL7ueDx7QD_pV85n9-I_zNBOXXw3rR6sNGaJa_MMIdGSVt1bqdMCCdbkJg_OJHPzXLUoqQ7BQSxD_qLGzNmik3ELlh-KqkyjLeSQPXRdnUiniAEhqTTGCv3Fjze22umsssTJG45jBHPV_LRDYqfXX96gMWLPBaqEgDM92JZ3RymR64sgd7hr0vC-9njsMjURLGz8R9B_GUCcQzBvgncrwjFvhtidZNFF0m_WiSBhpwKNZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از بلژیک امتیاز گرفت
🔹
تیم ملی ایران در دومین دیدار از جام جهانی ۲۰۲۶ مقابل تیم ملی بلژیک به تساوی بدون گل رسید.
🔹
تیم ملی ایران با این تساوی ۲ امتیازی شد تا همچنان شانس صعود به مرحله حذفی را داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/akhbarefori/662166" target="_blank">📅 10:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662159">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GaGH7RoYUVj_88kkER0tKbhjhR4YIfME6lz63JJ5Yjx4MBRaXzP_6hgUMEu6DJSzjou3LAPbO_11nMin1G22VmXr3_Ltw4Nkz13MV5w7Ro5LhN2nFnnM76h4gqYXJgnx8bc4qNGKB-oy7B6yUSreZbsOz2ch-YHp1w8lRiuyedcKN3wDeKlEwF1tYOVc4bjKrlFzMOGYMsm3gKMvntlAlKxLFQmszqal1lStbziE4y1oEvRDG2NR_LOeZWXnmrZuQzFnVmd_GtGjk2U222BKd6mMkLZ2mag2og3RBpqubjrDWHyKrrmgCzYwEL_dO2o77M9SQi2scMd9cp8D01aMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZ7Ond34yT3DbOL6Jzb-spncdk85iBOFycm601h1avbRZznKF8vn2uz6amZpfuMTDzflFapaSzfCTfcVnsFhwWvxkDMs5ZSw6i16836Uf5rDYS4BHTt1e7bM_PC6nXiTbsJrFfYi0EqFs0vAq0cAZwWYjTtztAo33X7IylMYnQYSXoJzyJSLl9oE4hBsEeThlpL96UON_x2hJ2nxmDmwCh89AYt3QEuxYqZripLrR6uLVVJCzps9YWj0wQI0eb3OA9K2YoLCg9cpKHvEDHofSdCrMVq_mzuzlbsQCA8wBQJj_AQ_jXdF4C2Q9MrH_j9eg2xuga24U_Ce_rU_U3-VZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1LDsVX5XWNNKs0OlASvgbzXaQLS9jyXp988MSlpx9Qm1-D56W-bAvw0poVVanlDtwNBvVh6DBg5OChfrUsLPDgnw6ITJgnJ55rYcBmQiIglPKhXFpIu7G6ZL1AZk5Rd3RJqHOTkxEF0R72YzH5KiImt3fmZTlv9y-KHyFGloxYiIQLXvx8xBOI60XtvdJX50X8dAG63CU1dWFYGuUDhnpknbKFL1Kxd-503g0WlmvhGtCoq1lKZ3kvoCzhIkfrbcC95nl9-OJpiJGEkk31ucH0tbjX_lRfm0ZP81jmyBkMKlt1RC5FY2_C3dgl4ivjWBZHuAHkSRRrkGWW0A_f56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaBMybwI5_nxm1SDL_ixwk48E5Jg9vu1yK2fQ8V5fnoSQl-pR-Ptewivg3fvF-zYfYujsfTZaa_OVdHklIL-8JuAmq8rO8mOueTzkgCWC7KLoHGECZiJa6b_6V5JNTm3FmAUmatsiSopyaFRvwVOGnjN40biJF3dzCT2OKWEGxHJ6FEXmkdPmAAhGB2Opjx0AvJar46aSJ9oE9x7pRainI1A3rw_udL_RNqasmU1NXMQP4j25v8yr0oLTvddKCkyaLoItyZjsIMI-imZVULGOGfvaRl1pEN_1r4DV58MQ7h1H19_OMyLWPEjFKS--iDYYTvhoLHwLJbofD1zgdKmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKYaqk5EFKzAtKgrigrpbAws9bwfNQVzCmuK-j5u0powDlkCUXJRqQvRmQ7sMkwRri2Mk-kLZuKjIXGd8maYzRwMsGxyPy-MG1c4N4V9L8pId-sfW-DBObjjGX-ZrrpWGsU4T3EjfxVyDmBvCu8hIWD5lubEeB-HUgr5YzoRyIGNQIcMBVDWFSug2UUCSeuR_H0d8X97L4xzHHAWv975pTxD4B9870MGqWQq_wsY8dbM3hZPsA9oq9A_s1bPBPinqELRivuXeY-kXCS6MFB371hBON4-JxS89yVcq_feHem031ZPU9EQhC6w8aD0863cKM3mlnHYnvbxCOZDblLhTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZdkN8a_Y9Szv9k_Eqs39gzJ1qRpE63Qs035wXppHJZT5DnU8rtQ7hF8iUZGHC1vg25dUNOcMR8Y0b4gGuCjIaAAYbppEnTPfmDt4ZklQnBUhT3yxbSzTozekYGc5vOY_bRt9PsAYbscOtP7aMDpmd3KN4W6nThbn_fV_gI6qINKb2rxvw_1eb4uL_QzPrDxOkFievgkz0xp2NTaUsUYwS5fsbwWGd1NEW0ip5Gn6bl0uciUBvbZtAgy0ky_tUeCMu0m1VfzvBAHyN2qhSJZIF6Z8ddjbNttg9G6Gzbsoc7WL5A9icULAeOOI8CeEA2W7A4PjbegtjLYFAPyKAg8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJIGR3FoQqUf9YXLB0R1sX5ggQHb7-JqUL852Zbw6ajLi4Un7LxH9hL6M7I7fBSa2vZ3oxM3bAN9PqFkY1nByA_ZHB102zOMCyPdIR6XjUn-qOqlPc8CDiRIKJb54_MZVT1ktmPUN8rno3xG-vCLug60wwejRdmwC1QVMmIix1j3f-92Zv7ClWq4DiWJnSH7qZQ768i3iKPSyFLp6WHsdoP98EfX3upjXrmRuYqu5NylZ7moYgoP7Aq9gHaOTyft-800Od3mpSpJYS7s5TMeWsmKMSGhAMLrSeP4cJfWxQ2kiwGPylThFLxelkQKokP0UeRgpcFiBw3vYaTd_iIh9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بحران «غذا چی درست کنم؟» تمام شد؛ ۷ مدل غذای فوری و خوشمزه زیر ۳۰ دقیقه
برای روزهای شلوغ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/662159" target="_blank">📅 10:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662158">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
دبیرکل ستاد مبارزه با مواد مخدر: کشت خشخاش همچنان ممنوع است و هیچ مجوزی برای آن صادر نشده؛ ادعاهای مطرح‌شده درباره آزادسازی کشت خشخاش مبنای قانونی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/662158" target="_blank">📅 10:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662157">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4G9Mu5ykxdscuk3PmSTiZ0TAqYoxGTAYrvVf6InLuYP-W9fPWrqZ1LiHS5rKtuAsQqM2mkbLIpCKZbfXAX4j8inHzwIhUIJACWocrrBade75-An9ukg94gdpkS5QmCUNey9UfyAaU7D748ulobacgDu5NZqGZnZs9RDydd9VoOuSnMJvFXeVzY9Y8UfZFBDut8-pZ8v-F1t8zE7QWjOfYkiq59xvDgxy4dq15zmOuy2kN6ZZp5MEcGrVm2lxTxmApqhRsRanmY9rtEmFHXChsElGxI7ANOaUJi1TbCwbIqAyJLnR9uwiNFIi8eaaslGVJ5VYQUyPVmsNchlVenKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس:
گروسی را به مذاکرات راه ندهید، او از سنتکام هم وقیح‌تر است و هنوز هم ردِ خون کودکان میناب روی دستش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/662157" target="_blank">📅 10:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662156">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ماجرای ۲ طلافروش‌ که ۳ هزار نفر را به خاک سیاه نشاندند
🔹
پرونده ۲ طلافروش در بجنورد که با فروش کاغذی و بدون پشتوانه طلا فعالیت می‌کردند، تاکنون بیش از ۳ هزار شاکی و حدود ۵ همت بدهی بر جای گذاشته است.
🔹
این پرونده به یکی از بزرگ‌ترین تخلفات بازار طلا در سال‌های اخیر تبدیل شده و به گفته مقامات قضایی، ابعاد آن می‌تواند در زمره اخلال در نظام اقتصادی قرار گیرد./ تسنیم
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/662156" target="_blank">📅 10:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662155">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
خبرگزاری آسوشیتدپرس به نقل از یک دیپلمات آمریکایی: پیشرفت در مذاکرات ما با ایران، از جمله ایجاد سازوکارهایی در مورد هرمز و آتش‌بس در لبنان
هاآرتص به نقل از یک منبع اسرائیلی:
🔹
تیم‌های اسرائیلی و لبنانی در مذاکرات خود مشخص خواهند کرد که کدام مناطق آزمایشی به ارتش لبنان واگذار شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/662155" target="_blank">📅 10:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662154">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
با وجود پیگیری‌های علی تاجرنیا، برگزاری جام حذفی این فصل به دلیل فشردگی برنامه‌ها منتفی شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662154" target="_blank">📅 10:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662153">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18740de51b.mp4?token=GV9VayfrCZfL-hdNtgFM6oadR7H4keGVyW0nDNwKsloz96wsadTuUXIxM2wXXrw2tv9D2wwtVc0yEy2vpDFhY5q3gODA842AQuNSpRjQ2OseeD0c_LlIvcxX0aIWBd6RO3xSo4z5AUTPdblgQT_lOQp5fjj9zzqgc8YWehO3KxkKQfBh3VOBqd9rO9kXeidIJmHGThDfKDSYYMMy6VhzvLkdT8Pnid8TN7TkhAoBQlsc79oyHyLvL4is6lmaEz6UVbWbhDQ-5HA5ud_POf3zoY_d_-qpYY0_NcoxavpjTrBJuKgvueZ-rvH95Ewrc1OaFVF72U7o2cmQGfP-A2ft4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18740de51b.mp4?token=GV9VayfrCZfL-hdNtgFM6oadR7H4keGVyW0nDNwKsloz96wsadTuUXIxM2wXXrw2tv9D2wwtVc0yEy2vpDFhY5q3gODA842AQuNSpRjQ2OseeD0c_LlIvcxX0aIWBd6RO3xSo4z5AUTPdblgQT_lOQp5fjj9zzqgc8YWehO3KxkKQfBh3VOBqd9rO9kXeidIJmHGThDfKDSYYMMy6VhzvLkdT8Pnid8TN7TkhAoBQlsc79oyHyLvL4is6lmaEz6UVbWbhDQ-5HA5ud_POf3zoY_d_-qpYY0_NcoxavpjTrBJuKgvueZ-rvH95Ewrc1OaFVF72U7o2cmQGfP-A2ft4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشکلات همیشه اندازه‌ای که ما تصور می‌کنیم بزرگ نیستند #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/662153" target="_blank">📅 10:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2b79c2e3.mp4?token=u5tHSfyb8iQxn6mrp7n1kPqDtIIJXvdNuNaiotdBAnYa5ECY31soJtP-sXb-mZ-IukFDuTSXgwgd_xdbwQrPenixfysoH7AmiaDrFFjARCwX-aFH5CNR0StFRkD_y6rt4vYztKW0VAsxR3hBSaeqdaVPyYzdj9IVbxDo6zLZMziq1ZZb6j_DXBj-CEPSGJ3NO634iSwoUilx5N_neDi0sxqyfUI6cESyabuNilHq4jVOnV_bly9zCASfkV008tQGjd6-7z7mNw0DPHQ2GW9rU8Jfzp5pM814F4lo8TAugi7vi2Az0QvMozquq5DUQqYwlN6ItooiFC_3Mz0cvxfDyaR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2b79c2e3.mp4?token=u5tHSfyb8iQxn6mrp7n1kPqDtIIJXvdNuNaiotdBAnYa5ECY31soJtP-sXb-mZ-IukFDuTSXgwgd_xdbwQrPenixfysoH7AmiaDrFFjARCwX-aFH5CNR0StFRkD_y6rt4vYztKW0VAsxR3hBSaeqdaVPyYzdj9IVbxDo6zLZMziq1ZZb6j_DXBj-CEPSGJ3NO634iSwoUilx5N_neDi0sxqyfUI6cESyabuNilHq4jVOnV_bly9zCASfkV008tQGjd6-7z7mNw0DPHQ2GW9rU8Jfzp5pM814F4lo8TAugi7vi2Az0QvMozquq5DUQqYwlN6ItooiFC_3Mz0cvxfDyaR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطارزاده: پیکر مطهر رهبر شهید در شب شهادت امام سجاد در حرم رضوی به خاک سپرده خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662152" target="_blank">📅 09:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
شبکه ۱۳ رژیم صهیونیستی: نشست کابینه امنیتی ـ سیاسی رژیم صهیونیستی روز پنجشنبه برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/662151" target="_blank">📅 09:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سخنگوی مراسم وداع، تشییع و تدفین رهبر شهید انقلاب: عنوان مراسم وداع، تشییع و تدفین رهبر شهید «بدرقه آقای شهید ایران» با شعار «باید برخاست» و با نماد «مشت گره کرده» خواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/662150" target="_blank">📅 09:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e1f1d9ae.mp4?token=SXbSgC9gtP1CkXy3wfGOo9-dfdGP9KMurkCsdubqkRnOQoeXP-7tzrWxP625CPvKX6bOlGdFPdDMr9rLha4_hkJ0m-4urYl7--gHHDyZhiupGai6i5IjslezdsnOZFluFHfzrkW3Xd40KxPsLgI_d7yyEvNaVpoaOBoVsvEl0pwwW4aiJ7kDCYfdPdISVf1QPUcv1xJjpwWiJJcal30sMJqSlf_cixI_tQs5Pve6VGsi8xRpDZBPppj5LqxZKKRYwrsRRm16TsYSOU8cvb3_1QnTtj_eKri7HesbAqTUGhprzFH1QR5hqhC4Zt859-UDK31gMofVu1kLZR24fIqsSlNdssxtx9XK1Wf7g_NnVgzskkT9Rje4hKYXI5FPb33R79ah08olAzCPQ7IQ5gDGVvpT8_cSJU9CDlJFLHdKNr5mI2Je-wy83b2tKgcoEfsfHpzjeCotd3JmIwJxA9PS4BVmDfJoG3HFyWNDv3IlrTE3XU8xcm1a43sJIGo_Y01klFHiEwpggUUhNMDmT0uHF9pbddzKT0FH7W-XiQZ15I2KBMXdXo2V73CklmakWyEL37P2bMGU0RLdlMv5T6G0e_8SFMErPyFJvr5HO4jUxTDKqOYVFKe-12yr8Dp2WRCFJl9YSXWoKM1IliGE90TfCDzwfXjRp32i1bSxmyBmdYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e1f1d9ae.mp4?token=SXbSgC9gtP1CkXy3wfGOo9-dfdGP9KMurkCsdubqkRnOQoeXP-7tzrWxP625CPvKX6bOlGdFPdDMr9rLha4_hkJ0m-4urYl7--gHHDyZhiupGai6i5IjslezdsnOZFluFHfzrkW3Xd40KxPsLgI_d7yyEvNaVpoaOBoVsvEl0pwwW4aiJ7kDCYfdPdISVf1QPUcv1xJjpwWiJJcal30sMJqSlf_cixI_tQs5Pve6VGsi8xRpDZBPppj5LqxZKKRYwrsRRm16TsYSOU8cvb3_1QnTtj_eKri7HesbAqTUGhprzFH1QR5hqhC4Zt859-UDK31gMofVu1kLZR24fIqsSlNdssxtx9XK1Wf7g_NnVgzskkT9Rje4hKYXI5FPb33R79ah08olAzCPQ7IQ5gDGVvpT8_cSJU9CDlJFLHdKNr5mI2Je-wy83b2tKgcoEfsfHpzjeCotd3JmIwJxA9PS4BVmDfJoG3HFyWNDv3IlrTE3XU8xcm1a43sJIGo_Y01klFHiEwpggUUhNMDmT0uHF9pbddzKT0FH7W-XiQZ15I2KBMXdXo2V73CklmakWyEL37P2bMGU0RLdlMv5T6G0e_8SFMErPyFJvr5HO4jUxTDKqOYVFKe-12yr8Dp2WRCFJl9YSXWoKM1IliGE90TfCDzwfXjRp32i1bSxmyBmdYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی مراسم وداع، تشییع و تدفین رهبر شهید انقلاب: عنوان مراسم وداع، تشییع و تدفین رهبر شهید «بدرقه آقای شهید ایران» با شعار «باید برخاست» و با نماد «مشت گره کرده» خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/662149" target="_blank">📅 09:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl6mQsH0Px-AbXenglv3YSr9Tj2jcJVyhX5O5SHA5xbVXfakogqVUnjM6pOWRuDOcGiHPrbxCifudScAeMhT-bumRsCUHbVlkxm_ceVUioNhM3_r05O6dY5PcAcicl-NZvN6V45YwZjOg0PzCqK8eRVvhcKZZPRcobPBl0WE4n7gRt9V44963DQ7_jD3IPbjha3xK4E9ly89VdM8eBGISM0_-ysHs2K3d3deyO-Z8FaXeX3BkP_TH07gM0lpxfXKOvrSjYDOCU8MRsUv0A5XI7gjgMitW2pBu0K94Mdiz6RHFCeZv-B3o5pCt5E0a7wKGZQoAQm1lZAloKwTjikNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس تهران در ابتدای معاملات امروز با ریزش ۵۴ هزار واحد در کف کانال ۵ میلیون واحد قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/662148" target="_blank">📅 09:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbEHN0he3P4ARiTKF2c5GheNWqDT5G6O4OLhMw0z_vRJeDcvqTEQwalyPx6Tvi8HGPp_Mr0mtglfG2jOHXk5xaCFCeYSEp8_jzgK7baD_TMzqCmzvdvEOnAw_j7sNDAJYWSXcYGSBCLi7_46MEjqNgWAmr-xHKOY3Fi8yZ_JMaw3_fmFIxYLQ4zslW0zS-uK4qFcXgKSu8_3xRyyDTbkxdgorLEVnRPXsOqKSs1Uwy5jnq-XRK4bNsxSsJJlIN36EL9zBAAKt0hoWFtCo5DS1aldoAOg4KeOo9M091JTyNjiWL00Nf3hjPfxzMFsoG60KZSldSxrOAPhzH3F7AlkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ انقضا وسایل همیشگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/662147" target="_blank">📅 09:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
افزایش کالابرگ به اندازه تورم ممکن نیست  «اندایش»معاون وزیر کار:
🔹
با وجود تورم سبد غذایی، افزایش مبلغ کالابرگ ضروری است، اما کمبود منابع اجازه نمی‌دهد افزایش کامل متناسب با تورم انجام شود.
🔹
برنامه دولت، افزایش کالابرگ فقط برای دهک‌های پایین و خانوارهای تحت…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/662146" target="_blank">📅 09:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79c457fcce.mp4?token=i02zlHAOn8oNTZpHtOlqoi7V1Rj3wKrd42dq8hGM3qU1_dY5SWQIx3bJ6XEkKCV1HM9x2Y4Ux0swJDx3j3tuv_0sHd0dgU863_Gw82lqa7CnfRRii7i5MQbbflJ_Yu6RavRXNO998AEWqxPnhwiXotoB-dUGjf569HSgm3KoZ5u3elWpB-8jAkaIlGA1NEnemZSiBFFKhtOHF-0NxJB6FB8Xg_YRmkA0DO7q9MbasXM7wpJHUrI-AGtQtR8xkni1dN0uXehoyAvZEL0MUjL083zFef3wI5ojT8-bveZQhsv7VjGZ41KOArq2Y6agKBaXCWIt06iof0AF6VM0h_vXYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79c457fcce.mp4?token=i02zlHAOn8oNTZpHtOlqoi7V1Rj3wKrd42dq8hGM3qU1_dY5SWQIx3bJ6XEkKCV1HM9x2Y4Ux0swJDx3j3tuv_0sHd0dgU863_Gw82lqa7CnfRRii7i5MQbbflJ_Yu6RavRXNO998AEWqxPnhwiXotoB-dUGjf569HSgm3KoZ5u3elWpB-8jAkaIlGA1NEnemZSiBFFKhtOHF-0NxJB6FB8Xg_YRmkA0DO7q9MbasXM7wpJHUrI-AGtQtR8xkni1dN0uXehoyAvZEL0MUjL083zFef3wI5ojT8-bveZQhsv7VjGZ41KOArq2Y6agKBaXCWIt06iof0AF6VM0h_vXYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر اقتصاد: تورم سه رقمی را نخواهیم دید/ به سرعت تورم کاهش پیدا می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/662145" target="_blank">📅 09:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_pa8-ysPXmfzzlAq-DkdruP5xHGupzfS3UKO5okcUOyCCXZA3Bs8LDPJrqOXYrptGF1MiFBKRAb092tH_GPLn4v7Jh6rzA_23Rste82OkBt-E3GNewRmpXnM6pmoTWU0oEP_76tIw98dkD0MkcR4edwywF811TipoppARSpAze5NUfw15ssks6KMpVtQEQfpuPa-GaAuspGcHQorifKk8qsTvNht-PfieTOv-qahaDPgpd8-AhQrVwpLYYT0jjtQRWN7Pezo0TAQ5mERVkZRnA9kBUhnEnbevDm7yfvtUMed4JzVukmzx-l6AupWZzNRBMGYSU99Q5elaXUBRzH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش یک صهیونیست به قدرت‌نمایی فوتبالی ایران مقابل بلژیک
🔹
معلوم شد که فقط اسرائیل و آمریکا نیستند که در شکست دادن ایران مشکل دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662144" target="_blank">📅 09:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
شهباز شریف: امیدواریم مذاکرات به سندی منجر شود که صلح و رفاه جهانی را تقویت کند  ‌ نخست‌وزیر پاکستان:
🔹
انتظار دارم مذاکرات جاری در سوئیس به میانجیگری اسلام‌آباد و دوحه برای پایان دادن به جنگ آمریکا و ایران، به «نتایج بسیار سازنده‌ای» منتهی شود.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/662143" target="_blank">📅 09:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHJyupOrepa37WykckmHAB6Y7Yo70Dfdm0N3uoQnAzg_w2Q5PYKFfYmUiB_CW7qEL0QADxkmEDWK5bgURiP1z-6vDvE9vyWgjHiz5QiNZCr2FSsZlnCf6KtDeyYFq23K7yYriXs4DPgl6crbxvMtZLJTQ9_POshaFNRI81ilgPYbUkyUoZ2yG_Iap7QpHKfhezvnwymYqQQN0EGpXNoVu4xw9h2DoNeMf6A70V99vr2U351VEWyizbFmyZ0gdmJjp_ry8NiE-F_dUE1FG5_uJ_Qe6zxucdvF_6SCdtgyy8t9bM0NNhh6S5jFgFfZG_7dzDzmmqQkuCMACKYwzqXN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس فیفا به بازی ایران مقابل بلژیک با انتشار عکسی از بیرانوند: بار دیگر شاهد نمایشی الهام بخش از مقاومت و اشتیاق ایران بودیم؛ تیمی که همچنان در این جام جهانی بدون شکست باقی مانده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/662142" target="_blank">📅 09:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662141">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
افزایش کالابرگ به اندازه تورم ممکن نیست
«اندایش»معاون وزیر کار:
🔹
با وجود تورم سبد غذایی، افزایش مبلغ کالابرگ ضروری است، اما کمبود منابع اجازه نمی‌دهد افزایش کامل متناسب با تورم انجام شود.
🔹
برنامه دولت، افزایش کالابرگ فقط برای دهک‌های پایین و خانوارهای تحت پوشش نهادهای حمایتی اعمال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662141" target="_blank">📅 09:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662140">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
جزئیات شارژ سهمیه بنزین تیرماه
🔹
سهمیه بنزین تیرماه برای کارت‌های سوخت معادل ۶۰ لیتر با نرخ ۱۵۰۰ و ۷۰ لیتر نرخ ۳۰۰۰ تومانی در نظر گرفته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/662140" target="_blank">📅 09:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662139">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پیش‌ثبت‌نام حج تمتع ۱۴۰۶ از اواخر تیر آغاز می‌شود
🔹
چین ۴۶ شرکت آمریکایی را تحریم کرد
🔹
کاهش حضور نظامیان رژیم اسرائیل در جنوب لبنان آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662139" target="_blank">📅 09:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662138">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XApFe1qGulSBx89hcfd-GaksppgdhzxSNfFFeo2C3gqz2UaILS0fXxZt9OKXvwUgua2ZwdxNroX6EebY5xJfX2xuurgP3kzT-ZWoR8W49rr9C8m1snc0Mn80DrQwYnnFM4klQQdDBpKQJPl9c0Q4CJFYgTzYojf0hz9cyJga2Me1lgL6leYP9RqKZW8V0BD9DCcOk252LRi9D6sAiMLbSFn96r-nxTexNpZqSzhFgs09AhY65px586Qe7fr6NCYz9QkSIj6dgq9eATOdhbUPZ58VG5-6ScJBZbAklFRPzM8sgnEN8zbl1RlJ0Co0NQkPftxikxxFjAcWJnd3X8ua-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر دفاع آلمان: ترامپ مقصر بسته شدن تنگه هرمز است
‌
بوریس پیستوریوس:
🔹
در نهایت، دونالد ترامپ مشکل بشته شدن تنگه هرمز را ایجاد کرد، نه ما، اما ما در باز کردن دوباره آن ذینفع هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662138" target="_blank">📅 09:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662137">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glIP6tu1QhPUUXiWcYzisArhNSpZUfRRK6Z8vZpCoXxO3sBQxs1ydqGC_Cx_HclrGgdSI9IEbZGUziSnIUCEF7bM_Zoxo0gp8Pztb_AGR43lbhqQAmAMPhkRcDPJKUJ6Z6xnl9C75B9N4lWeANi_OA8te4WBAKysLVkU0TWPpGoYdaWVzKE8i8gWvCI_fqodf9MdMavKKzimlCjNc_raDQCrTBlMD7o_aqlzbLTCiVJraN_-Hp2lgnNBq1B9KR-2ySiVoP3kOFMSyNKBc-S4PcLiYjz3e91FS8PfNc6s5Wa3g1iD_WP88uWjw5_Y7xqY0B4E99KgU_dHSHBgdYUQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صادرات ۳۶ میلیون بشکه ای نفت ایران در یک هفته
تانکر ترکرز:
🔹
ایران از پانزدهم ژوئن سال ۲۰۲۶، بالغ بر ۳۶ میلیون بشکه نفت خام صادر کرده است همچنین معادل همین میزان  به صورت محموله‌های شناور در نفتکش‌های مستقر در آب‌های سرزمینی ایران ذخیره شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/662137" target="_blank">📅 09:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662136">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9db0f107.mp4?token=pSfyctw9CkuWu9318svLp3Mi6o4dae_4dF4dVdLNexWL_hVNIDIKSi8bR0hE71RIUhb1IIkxzDInwuc3mTIB348VMQnS04JLhCR-XZrSLA_kqWIOiaHr6F-m3tyLyaWZUHln9SlhZQi8EcX1QpD4Q5JD0o60Eg9_gLc5jyDkBdrb89fLe1z-ma_q7CkgY80-_u2CJxV9SYXdJ39o1kb0X_FwKJ-hue3M1F7MD1FanB5A4HNUNYBzIwri9Gbn5Zce2AhxkoT3Tgi_9xLKFy1ZazmFx5B4CnTcrNX-pYXVY5Tuwu0Zl74tPST9UAtps8GQ9s-bb1l7RrtPwFabUoa0rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9db0f107.mp4?token=pSfyctw9CkuWu9318svLp3Mi6o4dae_4dF4dVdLNexWL_hVNIDIKSi8bR0hE71RIUhb1IIkxzDInwuc3mTIB348VMQnS04JLhCR-XZrSLA_kqWIOiaHr6F-m3tyLyaWZUHln9SlhZQi8EcX1QpD4Q5JD0o60Eg9_gLc5jyDkBdrb89fLe1z-ma_q7CkgY80-_u2CJxV9SYXdJ39o1kb0X_FwKJ-hue3M1F7MD1FanB5A4HNUNYBzIwri9Gbn5Zce2AhxkoT3Tgi_9xLKFy1ZazmFx5B4CnTcrNX-pYXVY5Tuwu0Zl74tPST9UAtps8GQ9s-bb1l7RrtPwFabUoa0rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین مصوبه مذاکرات چهارجانبه سوئيس مشخص شد/ تصویب سازوکار جدید برای نظارت بر توقف جنگ در لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/662136" target="_blank">📅 08:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662135">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY35LHOrS2gI2QGfY-qvFGoWj_PJ95JFyJ1SHPDSw9ZpFWr8eUNI6Xvyq07LDdMeb-hXNjHP4qeOXKh0EKn_UZ9wIj2vxBovdUcAXtrI0NQqprn6TJoo5mLWGt73xA4i2QEpb3KOuMqAZDwRAva-yY1FgYtMMKOvKpNAQ99bR6dt6LK5FS0yDYaLG3yq4V30fvGojiVAo91bEHldiK4CSy0fOQJ5lUQxQRceScPvOAoq2coKVEfLxtFTZu70GhH5yno5VnKa5TQM7EKef3m2GFClEuJGOfq7bHsje0x2OE0gAtF0WaF8h924tivgJ1LMdNRc32Ini_anFdgOqBF5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا بیرانوند سومین دروازه‌بان با بیشترین سیو در جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/662135" target="_blank">📅 08:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662134">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAq4k2puFMf8BIOSgMYIvRmHh37kx4mRF9IA45SBiahLt__q046ImLsZh0PnMt_esh4OjrW8mwRPFtH8FwZ7UgOrTWtV7W6iyfhyRm2O3StBgQ1QeuZT33jkVuWVgjFpc7YCmMeEMh7S3T7ld1JRzXS47k_5WdYJAIx65lGO7u32Ih7yySghbv0EuqCHf_cgsHyciMRTOIKm8W6ziGa9vRE3IHeSgID5EBUNG0wYHJ85ZRqJ4Iapg4xZB6X-gPAqeZ4qPt3YLO88ABsSwC4uUc-1XRuUciU8Bd9aA7lI5POHKlNmbkZGp0QQqHdI5mhg4MELjQidTPfWubYOpMpupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت امجد طه کارشناس اماراتی ضد ایران از مذاکرات دیروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/662134" target="_blank">📅 08:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662132">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jA1JLlViowMGCiP2zfSej9d8lRxk6gPwCXRsRF8pM4jFccIDg1UEO83ibCBlJ2T0wQ4rJbcnEbw5_FOFNukwYOSDdgQdqIbpyx-dZkfJkIDhYfGZ1jZDTRlfNmSX5_nAlFs6jzOIQbmNACGtKL34GpTZWiMPokwG2yjNKMxXDrJ1gSTlH67mBwyeLSJilU8gMWw9Ia7eeeoomnosKT0po7fdP_vWcv1do17GdK2FrmXZBRTvBh7ybCWCa3NvxrXB7iMkZQxelEpGW6KGSztYCdrCQHRKk4oKzJZoUxlc-21_OZThdpROXq3ENdyQR5eomXAp9PijhftfhgbEy5h9SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P7dkEuIHHimElUK2a8yOyyY1gHi8XYSJnz2KWHfl86GOQ5HAl-nk1QZr3wGVruXSQnHkN72f_WBYMtUEu3apWicEaHCJLz1IGUJqSloP2VDdm-gPpCVr58sDm_BFyM7soMqiJKM3a06bb5WA9Jktaldsa32oycvbPrg6heT-gf78O2l3DlIdYycpFRtfdXldcYOKWJQDuzQ26-9SODXB-LxroQCjdCxL2sHo98QZUjz4x96J_gdPrwsc7XBnI6NQJD9IecSQDyEIqE30UFUtafT_yrJn9Mreut5teIznfFOXuzwwsyKt18MPTq5uMNNpBHRowhPrChWEg1JIzdVLJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالیباف: ما اینگونه از سرزمین‌مان محافظت می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/662132" target="_blank">📅 08:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662131">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تل‌آویو ۳ شرط برای خروج از جنوب لبنان تعیین کرد
🔹
رژیم صهیونیستی اصرار دارد که «حزب‌الله را به شمال رودخانه لیطانی منتقل کند و زیرساخت‌های آن را در جنوب برچیند» و «آزادی عمل» کامل نظامی را به عنوان شروط اساسی هرگونه خروج از جنوب لبنان تضمین کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/662131" target="_blank">📅 08:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQYHSPylcwk7MiO3SCQvWwkFtMo4GjSuEJ0Q3NdqFpoHqJuE24CuyaOdOIa207yvX50t8Lo7qlVpZUyelNB9oTrlQ3LancXd9qsXmglzdmBleqvvFqJ7bfQbsgeSZv0ZsvotDTLu7P5V5cYV0rgPu_gih96legxtTY9Lg29T30W9JAsgW_UVSl0y6geUtn671N1TD-0x0gOgKlIupn9TU5YY_onVG1Zx2pil7LpEhs4IoGrLQzaI-sOAbmInsRrPgYGiDErbB3hApfSKo2r6jvnG-Qpfwf8tqi4h7-w2p036tcf5cuRV8LZ4519UQjos2nSsPPgEihE9qivLDNqI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیرترین ترکیب یک تیم از سال ۱۹۶۶ (شروع آمارها) تا الان در جام‌جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662130" target="_blank">📅 08:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662129">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
حقوق خردادماه ۹۹ درصد بازنشستگان و وظیفه‌بگیران به حساب آنان واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662129" target="_blank">📅 08:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662128">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تصویری از مذاکره نخست‌وزیر قطر و ونس معاون ترامپ در حضور جراد کوشنر داماد و فرستاده ترامپ در حاشیه مذاکرات سوئیس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662128" target="_blank">📅 08:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662127">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec6ef0348b.mp4?token=ObL_ErSJo2RBnA5_6N6aDw7wX_GI7QKAfL2cfihgcRZaA4B9zVQB2MsxFI7cLqaIZLOqjcn7KMeo1AwUBWqd3c415JojpC-WYwSk9zTDGD-zgrBaWAb8mH7N2Mk2gIHa3vANM77mfpzep5ueLrNIyvHX2-tckPUP0qeNBFdAjj14nN53Mx17l1QXMcbHZGbIUu08rXztjQ2ttYC7s-KA1j3OC4qxxUj0iaZW7FffSBf1EPmpBe8ti9txzqvc0z4o7WhqayOb7WWcDvH0GmbNJpT3Y_zJ2Qc-LAmmJsgMrPSmgsw543mLisLw5vjniHZdtBGz2maUBWoDvQO67pp7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec6ef0348b.mp4?token=ObL_ErSJo2RBnA5_6N6aDw7wX_GI7QKAfL2cfihgcRZaA4B9zVQB2MsxFI7cLqaIZLOqjcn7KMeo1AwUBWqd3c415JojpC-WYwSk9zTDGD-zgrBaWAb8mH7N2Mk2gIHa3vANM77mfpzep5ueLrNIyvHX2-tckPUP0qeNBFdAjj14nN53Mx17l1QXMcbHZGbIUu08rXztjQ2ttYC7s-KA1j3OC4qxxUj0iaZW7FffSBf1EPmpBe8ti9txzqvc0z4o7WhqayOb7WWcDvH0GmbNJpT3Y_zJ2Qc-LAmmJsgMrPSmgsw543mLisLw5vjniHZdtBGz2maUBWoDvQO67pp7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴۰ سال پیش در چنین روزی؛ مارادونا در یک‌چهارم جام جهانی ۱۹۸۶ گل معروف به «دست خدا» را مقابل انگلیس به ثمر رساند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662127" target="_blank">📅 08:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662126">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bcdd3a8b6.mp4?token=Hq8DvBpEQw5Z7WD4IgUNPWFxSOKHJs4sVDcGwvGLrYLycoShoneKCyXd6rLWi_2Tk1V2hqXTeIuYLU-LVp4MPMSxoKlPODJ2U9YMPuNbqbmJX8_VtnHA4z-amXOEFwyPenX5RXaJ-5WN5WSfD49Y1psPupHxg-5m-inoksRyzHfEGbENj6pxYU_WU4Shf48k5jy6Mdns-w2odWw6mw4VrTufMNS6UM6ARXXLlpeVn4mJDMYt8bGFKI00T2X0U130GGC1r_T5i7yLnmAYxoYQKo7FkiEI7VgsCEBEIYnEI-JjDY09u4K5r_d0sNIQ1VP4pO1izdJdxfG53yFunFgRTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bcdd3a8b6.mp4?token=Hq8DvBpEQw5Z7WD4IgUNPWFxSOKHJs4sVDcGwvGLrYLycoShoneKCyXd6rLWi_2Tk1V2hqXTeIuYLU-LVp4MPMSxoKlPODJ2U9YMPuNbqbmJX8_VtnHA4z-amXOEFwyPenX5RXaJ-5WN5WSfD49Y1psPupHxg-5m-inoksRyzHfEGbENj6pxYU_WU4Shf48k5jy6Mdns-w2odWw6mw4VrTufMNS6UM6ARXXLlpeVn4mJDMYt8bGFKI00T2X0U130GGC1r_T5i7yLnmAYxoYQKo7FkiEI7VgsCEBEIYnEI-JjDY09u4K5r_d0sNIQ1VP4pO1izdJdxfG53yFunFgRTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شور ایرانی در آمریکا؛ هواداران با طبل و شعار «ایران، ایران» صحنه‌ساز شدند
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662126" target="_blank">📅 08:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662125">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
هشدار ترکیه درباره احتمال خرابکاری رژیم صهیونیستی در مذاکرات ایران و آمریکا
وزیر خارجه ترکیه:
🔹
مسائل فنی باقی‌مانده در تفاهم‌نامه میان ایران و آمریکا ممکن است به سرعت حل نشوند و در عین حال رژیم صهیونیستی می‌تواند در این روند خرابکاری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662125" target="_blank">📅 08:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662124">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568c2ff66b.mp4?token=TsIVhbai_IOjsOQkhY06Sahg79uG68dJ1o0vIjRj91H_1OrejJEDTASSa1nI3s0441kPt1GCKA5GAqFE3pafXwVcxATrk8yT7e0PlpGe747ih8NhB4qfgYoMuco1dg4s0TvRg44R2NTR3aYyT0RqCycN7j0uYenL5y71TI40DFWda-Yzh8hQmOudB8tfgw5kJ_sKNcf9awEs1Mt716rI8cXcbkXDPGkEhsu5HHmfdOVwNTZiXZOfH3qHSoTuTndCR4kGEsP09H-5Oh5bjRgN_HioU1mbk198yzHS2d8PppKxbWRTCrW5iu022GvbiwXZzXiimxoBogsYvrhcwHRZ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568c2ff66b.mp4?token=TsIVhbai_IOjsOQkhY06Sahg79uG68dJ1o0vIjRj91H_1OrejJEDTASSa1nI3s0441kPt1GCKA5GAqFE3pafXwVcxATrk8yT7e0PlpGe747ih8NhB4qfgYoMuco1dg4s0TvRg44R2NTR3aYyT0RqCycN7j0uYenL5y71TI40DFWda-Yzh8hQmOudB8tfgw5kJ_sKNcf9awEs1Mt716rI8cXcbkXDPGkEhsu5HHmfdOVwNTZiXZOfH3qHSoTuTndCR4kGEsP09H-5Oh5bjRgN_HioU1mbk198yzHS2d8PppKxbWRTCrW5iu022GvbiwXZzXiimxoBogsYvrhcwHRZ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس ترکیه‌ای در برنامه‌ تلویزیونی فوتبال، ضمن تمجید از تیم ملی ایران علیرغم جنگ و تمام مشکلات موجود، موفقیت تیم ملی ترکیه را تنها در آمارهای ظاهری خلاصه دانست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662124" target="_blank">📅 08:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662123">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
وزیر خارجه بریتانیا خواستار کناره‌گیری استارمر از قدرت شد
🔹
اسکای نیوز به نقل از منابعی آگاه گزارش داد که ایوت کوپر، وزیر امور خارجه بریتانیا به طور خصوصی از کی‌یر استارمر، نخست‌وزیر بریتانیا خواسته است تا از قدرت کناره گیری کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662123" target="_blank">📅 08:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662122">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
برگزاری آزمون ورودی مدارس نمونه‌ ممنوع شد
🔹
بر اساس بخشنامۀ جدید آموزش‌و پرورش، ثبت‌نام دانش‌آموزان جدید ورودی پایۀ هفتم مدارس نمونه دولتی، صرفاً بر اساس شرایط عمومی و محدودۀ جغرافیایی، و بدون دریافت شهریه انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662122" target="_blank">📅 08:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662121">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdbdd5a74.mp4?token=WwwR-Mmog4uFHt_hOkmWYNsod03xDjzAmx2ePmey8gfv9QXyPN6-Jq9EuJmL5-GKtT8hn8eIyBkPilVe0fuqsdbiG8dB7N4xqFFnUdk1Go_v_mAl5_hAUDMWyke_XDF87NMMGaaTX0Nu_Ho8WsJsKN-2ChQqzrPrSBUT8qeKSpI0J7TvH_UXCRHxJUu6hcUGcjsfXcSNbSdllg3X0oTM5dEoQ3LifmdlwmVBWix3BqHByFxbitESjS7-G-NaY35AIoqB1pwx3RDorH7hR85wAle8EVekT8nv5tfG8GJyGuyrFk2ae5eqsmoHNb97kaVVMF6P6Sh_mFzJpArXlYh35ZOoFHeagqTcf_6dWP8UEwy2I4b-ffr2Cb-UKWggLnfB7rKmyTeK5fURvtG8kW7FwlupdeeyJgX0YlDjtE7fKViHACmY-9GfDVsi_DpGnPos4x6_GQ8xLKajXRnMjEmQL0X5txrSoigGz3paLaI7SmNGRKskVNItPWPOtPEK1YocAfGmZPxLjI2bMYhWTvMnjknjBloh9hyuAhdBbdGXapbg0iqjXMftxxJa3oZhPDuajV5XmW5vWXsZLiZUJCs7WL97R6KHdV6FNBrJcu6Hd7mk9z95KEx5aKC5mPpJ6IhPuSxiDUzwwHgw4hFWQuqpxB0AMi-QZtk_E5-EBcgrtb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdbdd5a74.mp4?token=WwwR-Mmog4uFHt_hOkmWYNsod03xDjzAmx2ePmey8gfv9QXyPN6-Jq9EuJmL5-GKtT8hn8eIyBkPilVe0fuqsdbiG8dB7N4xqFFnUdk1Go_v_mAl5_hAUDMWyke_XDF87NMMGaaTX0Nu_Ho8WsJsKN-2ChQqzrPrSBUT8qeKSpI0J7TvH_UXCRHxJUu6hcUGcjsfXcSNbSdllg3X0oTM5dEoQ3LifmdlwmVBWix3BqHByFxbitESjS7-G-NaY35AIoqB1pwx3RDorH7hR85wAle8EVekT8nv5tfG8GJyGuyrFk2ae5eqsmoHNb97kaVVMF6P6Sh_mFzJpArXlYh35ZOoFHeagqTcf_6dWP8UEwy2I4b-ffr2Cb-UKWggLnfB7rKmyTeK5fURvtG8kW7FwlupdeeyJgX0YlDjtE7fKViHACmY-9GfDVsi_DpGnPos4x6_GQ8xLKajXRnMjEmQL0X5txrSoigGz3paLaI7SmNGRKskVNItPWPOtPEK1YocAfGmZPxLjI2bMYhWTvMnjknjBloh9hyuAhdBbdGXapbg0iqjXMftxxJa3oZhPDuajV5XmW5vWXsZLiZUJCs7WL97R6KHdV6FNBrJcu6Hd7mk9z95KEx5aKC5mPpJ6IhPuSxiDUzwwHgw4hFWQuqpxB0AMi-QZtk_E5-EBcgrtb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایتش آن‌قدر پرشور بود که اگر نمی‌گفت اهل کنگوست، فکر می‌کردی ایرانیِ دوآتیشه است
/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662121" target="_blank">📅 08:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662120">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d321179f.mp4?token=jOs-lQPHJnEX8CtDGU-jWA3-frmw9drz2mXwXM9u2VIZmBGjNShxUJCXJhoi_P_xmNUn5kXJkZx3f8lkLI3NaPaHHlCk8h-PhP-faROcx4FV75usxo6nS-B7S7RLQzKbu92Jx2ExVxHqAXxeOSnDMC7asRfTWQss4762j3y_L4dfBzrUTHeHAGRm-_RFla1NH1xFHWm1grNKdIn3XArZMBBePwj_HhwSwQlN5px3dgI8AX1pYwPcrI2YtLdCsp8utRqJItsWYE4JvjoWMXMm5xa56wm77QkGVUkUuqEIKRV0IpNbWITIim2sVIVbesArPKJyjwSCH6fF5q4SrdxZHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d321179f.mp4?token=jOs-lQPHJnEX8CtDGU-jWA3-frmw9drz2mXwXM9u2VIZmBGjNShxUJCXJhoi_P_xmNUn5kXJkZx3f8lkLI3NaPaHHlCk8h-PhP-faROcx4FV75usxo6nS-B7S7RLQzKbu92Jx2ExVxHqAXxeOSnDMC7asRfTWQss4762j3y_L4dfBzrUTHeHAGRm-_RFla1NH1xFHWm1grNKdIn3XArZMBBePwj_HhwSwQlN5px3dgI8AX1pYwPcrI2YtLdCsp8utRqJItsWYE4JvjoWMXMm5xa56wm77QkGVUkUuqEIKRV0IpNbWITIim2sVIVbesArPKJyjwSCH6fF5q4SrdxZHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت پلانک معکوس
🔹
اهداف حرکت: افزایش متابولیسم و قدرت بدنی #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662120" target="_blank">📅 08:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662119">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o45PP6Hd17pjuF9RuhOIvjSxYssa5MV-ujK9JpTypDot0kJTR1hvRvORfeMG3lyL-UQA2RLbCBS51jOPlYND-VHsi79UHfv_HGKr8u3BawfdhjybF6AqebUNigewqJLbJn0P5VpQ1XyHaeXWzJKOEp3m6XUNsgqGnZsfdJK6Jf6l8a5eJz_ROPfSs_vdZJjU49hv1O-rlRYI6JZdBZ0sg8Ku7azrQ28j2b2GrP4mxzCRcbCil67KokPhhkVpOlqqQn9fAtGRkwdcC3N4kIDqYP_oX8_bNpb6cxFPp15c2MAths5nI4yrFvWWcmyNtZSr9UXpSzh6N9JSzHP1H5goXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از مذاکره نخست‌وزیر قطر و ونس معاون ترامپ در حضور جراد کوشنر داماد و فرستاده ترامپ در حاشیه مذاکرات سوئیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662119" target="_blank">📅 07:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662118">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ایران بالاتر از عربستان؛ چهارمین تیم برتر آسیا در تاریخ جام جهانی
🔹
تساوی برابر بلژیک باعث شد تیم ملی ایران در مجموع به ۱۵ امتیاز در تاریخ جام جهانی برسد و با عبور از عربستان، به چهارمین تیم برتر آسیایی تاریخ این رقابت‌ها تبدیل شود.
🔹
در حال حاضر کره‌جنوبی (۳۴)، ژاپن (۳۱) و استرالیا (۱۹) بالاتر از ایران، سه تیم برتر آسیا در تاریخ جام جهانی هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662118" target="_blank">📅 07:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662116">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مجروح شدن چندین نفر در انفجار قطر
🔹
وزارت کشور قطر از مجروح شدن چندین نفر در حادثه انفجار در تاسیسات گازی راس لفان خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662116" target="_blank">📅 07:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662115">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGOdYCCY-Sty98PMWouqmYwnnMQ5CoaebRaeyDv3zvQUk09pn9XPt1dSSnFTZXaqOGK4imDBM1bMOm5eyYrBcaGiVvPDeSeTIlQk2OpFCg47KnIOXdcpNXh_YAra3pF5-hF_SqhpsbbY62wxp5Puf6bI05YpIZlFaa1uruYZWIJ7zbrlreC2BHVTbQf1cKoLyrUX7K5k2OQFDt0tzY38gWcXZR4vBH3w0NuWTCvsz0p0xB_0aKMbpRR7dnpAFK2phLuR80g24em9iOQhNm6A1B_ubCMqknqPAGjLzPuDLxBswCBLH5iWYfiP-vFoRIO1-eIRSQvWD1jueshQgJT3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: از زمین فوتبال تا میز مذاکره هدف دفاع از عزت و افتخار مردمان عزیزمان است
وزیر امور خارجه:
🔹
از زمین فوتبال تا میز مذاکره و تا میدان جنگ، هر قدمی که ما به ایرانیان برمی‌داریم بخشی از یک مبارزه بزرگتر است: دفاع از عزت و افتخار مردم عزیزمان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662115" target="_blank">📅 07:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662114">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بوگن اشتوک
🔹
نخستین نشست سطح‌عالی ایران و آمریکا با میانجی‌گری قطر و پاکستان در سوئیس با فضایی مثبت و سازنده پایان یافت.
🔹
طرف‌ها بر تشکیل «کمیته عالی» برای نظارت بر روند مذاکرات و ایجاد کارگروه‌های تخصصی در…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662114" target="_blank">📅 07:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662113">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0NJBZMZHJ_va48YcMK0vQ5QfuhkxY1-EDwVK-ostbncsPAAWpvgh1BHBu23uS4WJjUZTnyKrnJ7Vy2mhTxUmGVpQjkd5D5vjGbbjBat1ff8QOMLIN66fREnN6x7euWVbgQRkcqwG2BI-6oRYhZiKKVaL-iqqCCB15TAUDehG2wsivsfD4bsAMU2Y8SS9RyMj3cxH5MjMAu2BauLPwZCrn1ZlE5Fkym41YpzXKvFSjVObd7hwYw2U9fpgjNWf7LnNI2Vrc80Uq1Z9xe-uUAXQFAWRoqPQqbPM5F3vPu-6ry6fgEA-2uko9AJixHJf85jM86EoWm2c31N9x2FqFRfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بوگن اشتوک
🔹
نخستین نشست سطح‌عالی ایران و آمریکا با میانجی‌گری قطر و پاکستان در سوئیس با فضایی مثبت و سازنده پایان یافت.
🔹
طرف‌ها بر تشکیل «کمیته عالی» برای نظارت بر روند مذاکرات و ایجاد کارگروه‌های تخصصی در حوزه هسته‌ای، تحریم‌ها و حل اختلافات توافق کردند.
🔹
همچنین نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز تدوین شد و یک خط ارتباطی برای جلوگیری از تنش و تضمین امنیت کشتیرانی در تنگه هرمز ایجاد شد.
🔹
قطر و پاکستان ضمن قدردانی از پایبندی ایران و آمریکا به دیپلماسی، بر ادامه تلاش‌ها برای دستیابی به توافق نهایی تأکید کردند.
لوسرن
۲۲ ژوئن ۲۰۲۶ - ۱۵۱/۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/662113" target="_blank">📅 07:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662112">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuIkdAxf1OBI7JvLtXE6VDVoSrNws229swZxPq3vSb2Xiq-HcsCao2M7wI9WC3UPdq4zgH7GQzyS_oFwdo8BoHHe85-fROXj3hb1qupACYFTGb-8h6oP2uwXYjXaMHvrJBXLOAEOXEM9AgAqUtIVLKFRTNcsVtury-v0FZ-F4sZeofJ3rDbH2Syzwn-AVkwvRverdTmI-mshHsAE9wO6Sf9-a9iIER8HkuWz2WmKIVWZxqn5TFQ3XVsDjOtiNpLbNuKIExWQBwVNcCXIqAYmAJ1qUmdR-2HU_qi1UACw-hHZUahUBim51oEpihpx-iCVQ2Ib_Jm3sUfeEu9YXrWrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشریح نتایج مذاکرات روز گذشته توسط وزیر امور خارجه
🔹
میانجی‌گری خستگی ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔹
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصرۀ دریایی برداشته شد، برخی از دارایی‌های مسدود شده آزاد شدند و طرح بزرگ بازسازی و توسعۀ اقتصادی ایران اجرایی شد.
🔹
اولین آزمون واقعی: رفع درگیری‌ها در لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662112" target="_blank">📅 07:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662111">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEoxKwniZ_jG_BFLQ8c1DrtBZ0x56N_4kQNUNC-aRuvJOFQOZI-RZGeyBsdo0ye5rvv5yX963W9QErThhhAbX2dVdv_b1dGeiJj7pQWosWyOEpKyPoxGj6P4bdUTWOnaRJgD_ls0MKjJCtJZHvLRVn9-j_8wfIXmVXpeNK-5QZykYdUkIghcVEpXqq8eW3Hm-hEpkG9f59fN0w0MKQK0kAGM8q1L7xLqopokyYiaf9Ocyk2wVyyUnETCoKecxxPfgd1bH7YYa33Onz-ZZ-afCoW8Mm4IWs4tFBxh6ZbL7wTaJonHfyyje62S1xs6wa12OBbW6aZBSwEkKeGEk4cq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱ تیر ماه
۷ محرم ‌‌۱۴۴۷
۲۲ ژوئن ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662111" target="_blank">📅 07:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662110">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_cK3UdpRsF_FkLPJF9lTEUUXFSuYxPwTgbHjmTNZnOzBQccbspo649_DzLCKzxwnIZb3gRvzWeGuyYQmSramHh6ZbMeT_PFVMOrIbtPN6KbEOMSMnXFL0jRZMluukjRwymJthVsTUZLyGWx3UdvDHkqX_3fiNqlFhH2V20K3PjYPvFzjlq-MWh9930xYDvd3Dp3GbwlgmB6pf9X1J3Qktp7Ozh1gOIdU96auLkYYLM22-dU_GvhGInaqjQNJQP6j1foWDO6n1pSX9t8BfRp5jsBQ_RwBhTeIQN8jm0HijINzrGfkNgJCIdI_0yeh-REkBoLqNOhdtIXV4KzKbo9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">《اقامت۲۴؛ باتجربه در سفر 》
✈️
🏖
تجربه‌ای از دل سال‌ها همراهی
بیش از 20 سال تجربه
بیش از یک میلیون نظر مسافران
و پشتیبانی ۲۴ ساعته
پشتوانه سفرهای شماست
رزرو آنلاین هتل، تور و پرواز
همین حالا مقصدت رو انتخاب کن:
www.eghamat24.com
www.eghamat24.com</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/662110" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662109">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFs8CFUG6UwNtH47Yj82vRyYEEgSE3Di_R3gSggJdoHZzu2NifpU6uSahbVjRr4HHlEwoIL8K1T_feIEFBBOx3ZGwu3im0yaUGMto13kZZWcO7nrgScZ4PaVqLulRNK6wwlc8jVyU5PI1yTlbefD49KGMH7dW4DNc6AcWEP4XrWXoDWVMfNbRJxIofFqNzbUqJSQ6F_JhbRTyHeZMki1ed9E9uy6udAbsSXEBGmK7RrFQDcfMWOwNpBQpXBPZoUnW2nw4QbPLh9g7UVi2KaLx3Rb1Nl4x2rQvx7Xem5HmSW7mVCy0LGHiNY--a2aNpvpkxhNEL4nRXRtOJ94qLbSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر لگویی از علیرضا بیرانوند با اشاره به بسته بودن تنگه هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/662109" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2srdAa-patAG5NoTMWFVX_bCTH0ifg2CrHuqqAhvJbi_kgjpfO0GxJSMxEpzKEKCO8QwZ3nDLv2Vg_MLK9IOGCUCd9Zwvf0gy2PoWdQGlH9xnVQioVwDxWBnHI-jh-gJy28YP0DfMMoWPUZLxD2lxDRhnv4wMCnk1O54fYAxRkJ8PzV4DF2oPVr64eoHTNx-shr3CRQIpcApb1v8Whu0_b-G1ovZcp0dpxOc-yBvwobi1qxKjcg_H-O5sFU11Bi3c3WDjEw6Kq0nVucc57MGA47f91pr6PlEvcmHqzL5pZNyQ-DPF1VKATgyAufqWvgK0s8L5oIg2W6FjMo8WcV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تاد هیکی»، فعال حقوق بشر ایرلندی:
مقاومت این تیم ایران، نماد مقاومت یک ملت است
🔹
با این ورزشکاران توسط سیاستمداران شرم‌آور واشنگتن مثل مجرمان رفتار می‌شود، اما با این حال چه در زمین و چه بیرون از آن، دوشادوش بهترین‌های جهان رقابت می‌کنند.
🔹
هرچه بیشتر [بخواهند] آنها را پایین بکشند، ایران بالاتر می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/662107" target="_blank">📅 01:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeJOZtyk8OgoI0fuo15g13eSu6YrUVK1xUp3Kh1V69m-Jbs-XhQZXiXbIRp5BqqNALNCsfAx5Y5vWszL22874v3B0wUT08wBNvlWTHYCj1bBq_iYtMQyHwbeJxVZa2n-GZa3pXnn8WxZLV3IXP8_2s9NheLhutKyJmi6tYqgPj12VrViXNayh8BC6-f_ZtET4mMFRJw7hx7-AKbWImW0VyqYjkv8SLp5SKPumfd5UeM1G0im2C9asLdww05TmQiLJZTgzqD4pGNsb-XyEtpv7AWaiQ5oaUrv7Ws6RgxCX2E7OxHnYLvDpe0mAc1QjRMo-DLb-7K_H1VkazWa9LQhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ در پستی در تروث سوشال به گزارش نیویورک‌تایمز واکنش نشان داد و نوشت: «بعد از حدود ۴ ماه جنگ، چیزهای زیادی تغییر کرده است؛ از تضعیف توان نظامی و اقتصادی ایران تا باز ماندن تنگه هرمز و رشد بازارهای آمریکا.»
🔹
ترامپ همچنین نیویورک‌تایمز را به «تحریف واقعیت‌ها» متهم کرد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/662106" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feOc5mW_OVXMTM5dkOuHObZkU9kHINq_dtcopFkaNGBr11rfY7dRDJ_Af5LbJ9zxebdVHHKOXEtDORMIZR59_AdTbOldqq2sFGyY5szpnQcb3s1g-znBlPiiOBuJedRUAMnoAfiu-eL1CwlZn72iXu5gFdsLAWOSU_aHQqv97lHpKDWYH3X9ueSyWNW_5EDQCceq9EfGAFjtga9CR9QRw6-VIX9Lm33xAI2-tJ-s6DlOXR9ffZOMNJGmqALp0BOV3aA-BfPZ1AXGThn-UtsQjm4ZnYN4HkL1Dxs2OFad7XBPhHL-YIxCnxrrMMHmstx3gl0yIW2p4eLTKUcJ_9aTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/662105" target="_blank">📅 01:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662104">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrbMlbOft2n5hv219ISgLtLnV3SC25KmmR6oIgD3iRjtRhbYIwh6dVbXOo9nuDF0nN5xU0aaWVJUuniGKrUFirZ7dVIrdFKBdrPfTtGBo-nTXv9GY2RAi2bhOoVS9sW0pAgVVcWVHO1jpP7SmGbgn0a5YChEX4LEGE4jP5YrVrp3X-5Jzg1B3Y4iKidjozrlS6cqfKOfV3UAg5rN16049yIVXimOXKEU4W9ab7vO3r75MkVduItAlsOLhukq2_fSrBVwD9DeOWS315hjEcyfIP3mu-8UdiRkLuJl79V-v6VC4ZGaksgJH7w8I7qcWJHNpLkciBZIH-vDpaVfCr9b3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ما اینگونه از سرزمین‌مان محافظت می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/662104" target="_blank">📅 01:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662103">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhOEZEntHNzoFjZc_pq9wTHD39zeBRlIEd2rG6P382NuGfeagxVyJhX5uIk3iAy55-P8rtPad9rLK9rayvEwMum3a1Hyr1ZNBghpL3-7HaDvWVZzY-QcNWpkcX-oGj_NCnm2Pu2C2gUkwxIE3ocVhFSCJhXSMrEhp5XVYzeZdp5VWegZHFUbsz4CZwfrFXKMC0QfC30oSeLHWv4bZCc6AGCg2IRP4ITZywNeAEl9VADSj4j2oKPQ2XVGeDrsDLaxty4x7gW3bJkICVINcqIEfGFVLkQ4oOUBt8JhlroZXXaZDp2vZNTzFv-GohMVeAG3e6ImO4Fc9wcQexZY5BwWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
استوری قایدی در واکنش به بازی فوق‌العاده بیرانوند
در بازی امشب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/662103" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxcbspyvB9-Gz8y5AIjo-p4FleWCGVREIoEpOKQwpJXktDkUukN_JWMRz7RbWhp4H9-B6eyRZoI87uf-8S2kP7P318kC6F-j6tkHLcAD7qdO0HrmWCMNz2v8hMQ5cDu6WeNc54M163GPMTQkBJR1fLVuQMUcehxs4Bk9p2rcHgpiJk24AQatkzslUampcxct1xgvtC_WStMlOsfcubLuIyri-I7EFoJG7_32xzO4--ohkoizOzr0dMioNRp99tr0ZEjC2RhDr0R2_CZx3wwy-SOF5siu7IReDtXqtVzeSTJ9s8y_vCG-8sib5NfJfAY7wIZLNNH7iKWgawfW_uGW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران چقدر شانس صعود به مرحله حذفی دارد؟
🔹
طبق صد هزار مدل شبیه‌سازی شده در معادلات جام جهانی، نتیجه برابر مصر:
🔹
در صورت برد: ۱۰۰٪ صعود
🔹
در صورت تساوی: ۹۴,۸٪ صعود
🔹
در صورت شکست: ۴,۶۶٪ صعود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/662102" target="_blank">📅 01:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
جدیدترین اخبار از مذاکرات در ژنو
/
مذاکرات چهار جانبه همچنان تعلیق است
یک منبع آگاه:
🔹
مذاکرات ایران و آمریکا در قالب چهارجانبه، حدود ساعت ۱۵ شروع شد و بعد از حدود یکساعت و نیم، برای یک وقفه نیم ساعته جهت مشورت میان هیات‌ها تعلیق شد.
🔹
اما به دلیل اظهارات تهدید آمیز و موهن ترامپ، هیات ایرانی حاضر به بازگشت به مذاکرات در قالب چهارجانبه نشد.
🔹
با وجود این، تلاش قطر و پاکستان ادامه یافت و تبادل پیام از طریق میانجی‌ها انجام شد.
🔹
تلاش میانجی‌ها همچنان ادامه دارد اما تا این لحظه به نتیجه نهایی نرسیده است. در جریان نشست چهارجانبه، هیات ایرانی صریحاً نسبت به نقض تعهدات خصوصا بند یک یادداشت تفاهم اعتراض کرد.
🔹
هیات ایرانی همچنین خواستار تسریع در ایفای تعهدات آمریکا در رابطه با آزادسازی داراییهای بلوکه شده ایران و صدور اسقاطیه‌های صدور نفت ایران شد.
🔹
در رابطه با موضوع هسته‌ای، هیات ایرانی تاکید کرد که شروع مذاکرات درباره هسته‌ای منوط به اجرای تعهدات آمریکا طبق بندهای ۱، ۴، ۱۰ و ۱۱ است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/662101" target="_blank">📅 01:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_bOe_A5Bum-XIhGJzEW8XJfC8YjD2THtivYQzasgfITZZkNtn-0uEfzAvXZfQ6I1A7VI1FdpDMipAwG3WAdWII58zFGcM9N2aflOZKrVGw1pyP5dMY7jDDf48Be0WVHUUcd7dpVS4YYE26CEUKrZdwSKj7uZ3TjLqUyo7rNeWN7NnOgRkqeGdQoz-jRlm9jid_xu0g-hjypdUJQxT8fm09t5oIa0Av3spz2II7GlKdOsdPzZ_F7UveUvwSZ_tqHcKM250poNDNCAQUraDRyLtOHdxg0NUIQVb37Oqnd07Kut2iR9RMBW3x-HfWWyg34Sqix2GjRi-yXgDknaT6uUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاومت در لس‌آنجلس
🔹
تیم ملی فوتبال ایران در دومین دیدار خود در رقابت‌های جام‌جهانی مقابل تیم پرقدرت بلژیک در لس‌آنجلس با یک بازی کاملا منطقی و دفاعی منظم و تاکتیکی به تساوی رسید و امیدها حالا برای صعود به مرحله بعد بیشتر از قبل شد.
🔹
هفتصدوهشتادودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/662100" target="_blank">📅 01:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bdb7bca2.mp4?token=bIEPgi1gdXhWJ3THml2CWhg9KxA-MjYzPRczSvlvI53oLkNdkb9VY6l7RYFzt07frvUlEBFkLzK2TebcnQBmLGJ7_UajdUgpKuXtodN-Id1JJ-px5KXIFwYf-EED484nrdVd_e8ECJ79eKJemTHWZEOBqBmIym0DbdcVFaPDM0XmNmHzfkxm5mfns28CclPwkiStZFhIfdGx9GgByARXsim6H2cjicFwcJgFah-pBf5Do6FqQk5lYbeSbWrTH1JLbSdPBs9Bdxi3u4su6fMAdhLjiG50esebGNQycFt7P_b1TGcRaSSyjeGbdIi0s8pudLuGQOIJMLt1gXWnZn7lzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bdb7bca2.mp4?token=bIEPgi1gdXhWJ3THml2CWhg9KxA-MjYzPRczSvlvI53oLkNdkb9VY6l7RYFzt07frvUlEBFkLzK2TebcnQBmLGJ7_UajdUgpKuXtodN-Id1JJ-px5KXIFwYf-EED484nrdVd_e8ECJ79eKJemTHWZEOBqBmIym0DbdcVFaPDM0XmNmHzfkxm5mfns28CclPwkiStZFhIfdGx9GgByARXsim6H2cjicFwcJgFah-pBf5Do6FqQk5lYbeSbWrTH1JLbSdPBs9Bdxi3u4su6fMAdhLjiG50esebGNQycFt7P_b1TGcRaSSyjeGbdIi0s8pudLuGQOIJMLt1gXWnZn7lzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیندسی گراهام خطاب به مردم لبنان: کمک در راه است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/662099" target="_blank">📅 01:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پرس تی وی: هیئت ایرانی پس از پایان یافتن مذاکرات چهارجانبه، محل مذاکرات را ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/662098" target="_blank">📅 01:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01037f4a6e.mp4?token=ub0bGaYi0JPnjBjibO-hKsG7WbQGKBl2ZP7VN__MvTbpA1nKnRguQYY0p1n5BNY8_y2TyfK15uMUB7qb0zzAQeSzzYZsC5d1Xpqds1lYlGoVQJ5rNX1c9nt1Ht3r7Aq_cA9nVg0cajDTagtWSWiVwDr4wDZSh4VZ0LhYGxxT4ntc-c8Sa-wTLC6QH76geIYbuBsszChilCzHe4P9F8v-bqF_atkgby4aa_RqE6Lm4pGN8vclZqHbWuST3ucgIIqYPFICdOzl_UfJ88SPxILUL9HHPw8lu9hM82AZdRP8ppq9a35Wu66Bb8BLWb97uvDrah6EAcy2YRG3mICQNMxI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01037f4a6e.mp4?token=ub0bGaYi0JPnjBjibO-hKsG7WbQGKBl2ZP7VN__MvTbpA1nKnRguQYY0p1n5BNY8_y2TyfK15uMUB7qb0zzAQeSzzYZsC5d1Xpqds1lYlGoVQJ5rNX1c9nt1Ht3r7Aq_cA9nVg0cajDTagtWSWiVwDr4wDZSh4VZ0LhYGxxT4ntc-c8Sa-wTLC6QH76geIYbuBsszChilCzHe4P9F8v-bqF_atkgby4aa_RqE6Lm4pGN8vclZqHbWuST3ucgIIqYPFICdOzl_UfJ88SPxILUL9HHPw8lu9hM82AZdRP8ppq9a35Wu66Bb8BLWb97uvDrah6EAcy2YRG3mICQNMxI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمجید لوکاکو از عملکرد خیره کننده بیرانوند: او هر توپی که به سمت دروازه آمد را مهار کرد
🔹
بیرانوند هر توپی که بین تیرک‌ها می‌آمد را مهار کرد و همه آن‌ها را دفع کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/662097" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwvjcGqbdSYLz3ineNXm6b15raBZ1HSRtxCjOC9D6oss_h6bwHn7R1vj3wfAUH2QxO79w50ZTuUy2rkyx22atCjhy5xRbdIvW6hx2IS8uXO-r28B9ctkEp3Uj0CcaxBC1Tpi-MLgDVzNGblI0vGvGoudlcd7XbK9cwI_bCTAWfHp3m4imG3IUjzq1jLncim4ECcfBipafv0hFhaT-1x0gztVaT6rQxGa9oL7AThc5zN7gXYEGisGgncMXq4kEs25KN-e7jXr233fUlWikZYx-mbwjeJN-0yu13nzwlSUoGDxfO6LhR7DW9EcZ6Kp45_NnMicskyl8MOYtxRO1rIqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاک پاک وطن! خیالت تخت
نسل آرش هنوز پا بر جاست...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/662096" target="_blank">📅 01:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
لحظه انفجار در راس لفان قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/662095" target="_blank">📅 01:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662093">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzxPhs29-KA_yjkOMWI0N5rsnSQeeDL70ynYjkhhRHCfAC9xVe1K__HL4lvZRYK_8eVgDBmEGi3KZ2MIgg9dxOhFIQOAdGBy3yGRRpzEF7Kg6Z7ggKuFt50psbRtcTF1AYY-BJyLFOByavIphLAgjWVAf1kU-c_03vE9GDCVaGdaCM-51U-lhQsztgjg2hCwmN730Z246KXRIodVn7rwVC92Sh-v65FV2GBW4CPjXpgx8EhZpT20nvPSQg0KxJF0PBzYDsE3K0tTGhdkrKm49ihcTlQbBlywjUG_-PzNn6nB0CWwMbphvxdJx2tcGmOGJHToArBeMP6RPTN861ba5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست پیج معروف ۴۳۳ از عملکرد فوق العاده بیرانوند در بازی مقابل بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/662093" target="_blank">📅 00:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662092">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-Zo4yhYQFa5uZQlZ13EmplLNmvzi7rTq05Mxa-us8YZoIhGAlANZmp24ju8w-Z-RdeKzmeYBFcpZ9A77ohGK6GhHdSfcQp3Ag8dn6P90GABPJZBjWi9TUJgAyWaHHu74-8EnA0NPZTmNBDsjIla-ZJI0aN8JbWDLfbpXall_6H002sG34QsRhNb4vQGueg0QKAvbsq0ImRMk4tXv9JqXwmdT1U3Or659nSZdMDRWxQEyLVrVKsPLEgOocKxbZoiTQLwGAVMd8Gmhvw-VrNxyQ97qu-MPg_dMLWEFnMKWFyxdWpgfnzpnDfOVjnTu2sU4BCKPoinFelIFFQBgzv3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سردار آزمون به تساوی ایران و بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/662092" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662091">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH3Jp17SxHzqELUJTuZ1aZ02sPCDLDj7qk2R-pelex6w0DhAg_qQt_xvPPWcFxCR2iaAu6cXbdxfCs499w0Wg6TSKiI-vPB6N0BvCCSCYTdvrI3UPIVgyEjECEvap1yVoKBN3mYLfDh7CIJpfp19ASUh1vkyGZFqqB1IKvNjc-RaLOGKk0Gb-5_9Onurv8XVSCt-sreYJBRnTnCs4VEdxU_x82BucWKrYwbrBrAhWxIpmZso5IIfxMAfBKJarXnQjW5uKQGe5EuTUIm3-yK9fvjBI40ATVdRcfSpIpTE2JwbN27UCLR0-6vvtqpFX1YDwnmsLiBKEm-c709WcxJrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست پیج میلیونی و معروف ترول فوتبال: تنگه‌ی هرمز بسته شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/662091" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662090">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg3h0WbvkeEcIct7Ywq4d1wefy32Fc55UT__hCJ3F6dAC0iifsetXJI62POg580rlhlnXICmaPSO4EQ4m_YMab_s_mL6wn-THip4gyrJkTHa8-9_2oXt-QyGG3C1YuD2kGfLyUfBDF91x1cBp7UAh-Q3z3iWapIud30BzPK0yICdGVJ34OrSnOvE_MwyT4R5P0NH7vYQiI1tQP35kB8tsgPHf4hu8e6X1rwTxtYiXTIJhkMgVBW715mmbEUskBSgnUw-LOe9b4LhvUx-cLRPN0s0xetFAQQ88kjuyR2vTK5zEUUy8XUzEE08zzuXH9s-nyARLF-t8B04r3alY1Jv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
علیرضا بیرانوند و جایزه بهترین بازیکن زمین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/662090" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662089">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b771a66ca.mp4?token=I1vZgkCQ1FeXO5tEPUq0js6p-psz0-S2RFekLnqBA0_TZfSnX_UTX7PJhEVvt8ohVcrBWq9HyXYzVAHkCoO1Y2cisX1Zrkkn9VVjdhetdrHqmCM8VJMZ56FCzI4CTUxB14ToNLY3P1KmrOX3ahaCkygUM5O2BT5Pv1P111V57GLqCKMfVVodQfH8FEXUBl7LRbQSMdKJi2BmUUJj9YA7K7QV1tXnF-SI4qYP7POhe7aH8-wrCdk-IreIVeEyJUOSz5N4naAB_nRB1dAxWgNM-OfTZOFTbx7PqbvDPuY1fKr5saOIVzOdwR8Tc3YPUCckOvepm1jMyGXDsD59LmQifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b771a66ca.mp4?token=I1vZgkCQ1FeXO5tEPUq0js6p-psz0-S2RFekLnqBA0_TZfSnX_UTX7PJhEVvt8ohVcrBWq9HyXYzVAHkCoO1Y2cisX1Zrkkn9VVjdhetdrHqmCM8VJMZ56FCzI4CTUxB14ToNLY3P1KmrOX3ahaCkygUM5O2BT5Pv1P111V57GLqCKMfVVodQfH8FEXUBl7LRbQSMdKJi2BmUUJj9YA7K7QV1tXnF-SI4qYP7POhe7aH8-wrCdk-IreIVeEyJUOSz5N4naAB_nRB1dAxWgNM-OfTZOFTbx7PqbvDPuY1fKr5saOIVzOdwR8Tc3YPUCckOvepm1jMyGXDsD59LmQifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیرانوند: اگر دقت می‌کردیم می‌توانستیم بازی را ببریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/662089" target="_blank">📅 00:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662088">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
کماندوهای آمریکایی در دانشگاه‌های کشور پیاده شدند!
«وحید جلیلی»، قائم مقام صداوسیما در امور فرهنگی:
🔹
واقعیت این است که آمریکا کماندوهایش را در همین دانشگاه‌ها پیاده کرده است. آن هم کسانی که همین امروز حقوق‌بگیر دانشگاه‌های جمهوری اسلامی هستند!
🔹
در منطق این آقایان، اگر می‌خواهی ببینی کسی خوب درس خوانده یا نه، معیارش این است که آیا تسلیم آمریکا هستی یا خیر. اینها گزاره‌هایی است که با همین صراحت و وقاحت، امروزه دارند در دانشگاه‌های کشور ترو‌یج می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/662088" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662086">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvXEBrYmxQLQ31uRgijw0QZ9-7BHq7HMGASjZWBtNHB3H4ZtyWC6fSb-MdZ7z-e5nfOTS6p5H_9CXqQ9RevhxC-WmRb4n8FWEK6q-CJtZB_x8_Tu9Fh5f3b53EBDwitBOqM0WFcVOGqOjMYFCbQzGkI5rMeklQilpergs1M5jHljSpZ7kKt4jnuZIcAwTyNqqCcaq5AIX02hmvUz3FHw5RzBSafbByOJNmZtlY-QAbdt5uYieicQug4SnxkmqYTx0Lae9mEoqi-nNc6rOaQ_K64oNzLUyzoIGrGq5FBCeFWwJTm3T3fWvnH31LGrqxFfaDJnlQMmLsiRmc00tu857A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۳ درصد اسرائیلی‌ها ادعای نتانیاهو درباره ایران را دروغ می‌دانند
🔹
نتایج یک نظرسنجی نشان می‌دهد که حدود ۷۳ درصد از اسرائیلی‌ها، ادعاهای نتانیاهو نخست وزیر این رژیم مبنی بر کسب دستاوردهای «بزرگ» در جنگ علیه ایران را باور ندارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/662086" target="_blank">📅 00:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662085">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
خبرگزاری دولت: ایران همچنان در محل مذاکرات سوئیس حضور دارد و رایزنی‌ها میان طرف‌ها و میانجی‌های پاکستانی و قطری ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/662085" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662084">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قلعه‌نویی: از تعویض های خودم راضی نبودم، حتی شانس آوردیم بعد از ۱۰ نفره شدن بازی را نباختیم
🔹
فوتبال همین است، مثل بازی قبل تعویض‌ها جواب می‌دهد ولی آنهایی که در این بازی وارد زمین شدند توقع ما را برآورده نکردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/662084" target="_blank">📅 00:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0cYe82tL22oNqHsTj9--ofPtx5j86xLtGZ3tf-RrI_dDAYrGYcHDESJSlMRzXirWRGUDQx9Nim-_2bWzhlBHDnYSvlA3ut5XuS5MgDYTq2Yed_gZNNGuxJ744d89EfGoifQghX8qMZJWrpzbvvzA_E2RoDTzEFIGuBa57p-IEh0DRhhYEM7CQ4oOb7aBUl2IuK2T2zQpmKzeS5bZOSaRmCTqlMskxr6ATbUSpvNNw6H5NcY50NEjgtD6WNFI8dIQfauas7i3y1wbISGPLMILk07w6eopdjtmCFRiyfEmGGgghcC1jDhMgQ7o8Ehtsz8B2WJ9uoBJ0tZDtNTCEgOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی بلژیک برای دومین بار در تاریخ خودش نتونست در دو بازی اولش در جام جهانی حتی یک گل توسط بازیکنانش به ثمر برسونه؛ اتفاقی که آخرین بار در سال ۱۹۳٠ رخ داده بود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/662083" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLDlwdsKanP-ZtVSMGjJw62BfpmPdUmeoReR82ny8NWLvqFWIhRaLTOe9g6cDs5efxUhVFd5o-N7Wmm_cHMnNQDQS5AAg8ofRC-8z_6ekvvCWSWaKLPQs6mkM8Eg9768KruLvWHofss-PlfQ13j_j9txoWJNQ5kRkvpT1n7FCrPKFKRtfyUbdq2iojeqytwoRW77Tk1cIu7XmT0qRMWwmaxd_sJVYStJsziDY0vyrDXS-C98Kce7RWLW9nqMhCGKOtq5Dp8SOB9gaMvem0zdcjVILIj6m5AvQVFXHnix4angpbCUv6UIznbBxNGpy5eYDaAWKOOII7D8FC-ibWrUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمرات بازیکنان ایران و بلژیک پس از پایان بازی از نگاه هواسکورد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/662082" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9657e5566.mp4?token=vxvg8oPqLdp0olBisZqPYYCzB4KNguR6fZN2c8fWBnmeWLJAbPHww48D8RLOW2RO2cznnRF8uPOnkNfkm0vCllBV3oqTYdxbdRB1mRiFzb3-fDAKi9297Fsrv9pdk3NDC97InZuNj3X3-gKHtmKrRqDk9dZqX8QXreujZMa2aKtq9_Ph5w_kuHCtUDhBE-pIfgG4fwpwMX_hY7Ey0LuxD6BzYXA387yteUKqIKzWi1CVm7DcEPvxtzz-hqItBRy-OOgf4PFR3-9hJXpD-O-vnJN04Nctw72EYysGX2buCKxqZ3Dh9taGg9GHhDw7yy1ZHUnGqywQD4KCK47BJFE8pRl3ZrqvoLXMd2oN4vH6TlPtqMEW3V6cldE6dULimN20NDo69WpiHy5OCAR9tU8jmi0oz7bNmgK-o29fZY2E5ojYX7vFEGpY_4K32wCKaCaRMky3w6Fn6EPGutDrmp3L-0OlMXEVvBpaRw-TeteWD3EeXaqwTSBGk3BmC2UxVi8acciCuS_sJyXgc8Nw8NeRaZADppZiX8gCZh1bgIoSPuB9Hbjm2TctFcWi4VJOCv0wBQ3wlyCg0SMz0zFzPnv4ff9fJrMrgplTOQ44Dx1VexCDQU1TXTSwQkWkDLKCBtGejSYUVxqSvCfqsMudn154wI_A6bmlP-xq7I_ARHFpjdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9657e5566.mp4?token=vxvg8oPqLdp0olBisZqPYYCzB4KNguR6fZN2c8fWBnmeWLJAbPHww48D8RLOW2RO2cznnRF8uPOnkNfkm0vCllBV3oqTYdxbdRB1mRiFzb3-fDAKi9297Fsrv9pdk3NDC97InZuNj3X3-gKHtmKrRqDk9dZqX8QXreujZMa2aKtq9_Ph5w_kuHCtUDhBE-pIfgG4fwpwMX_hY7Ey0LuxD6BzYXA387yteUKqIKzWi1CVm7DcEPvxtzz-hqItBRy-OOgf4PFR3-9hJXpD-O-vnJN04Nctw72EYysGX2buCKxqZ3Dh9taGg9GHhDw7yy1ZHUnGqywQD4KCK47BJFE8pRl3ZrqvoLXMd2oN4vH6TlPtqMEW3V6cldE6dULimN20NDo69WpiHy5OCAR9tU8jmi0oz7bNmgK-o29fZY2E5ojYX7vFEGpY_4K32wCKaCaRMky3w6Fn6EPGutDrmp3L-0OlMXEVvBpaRw-TeteWD3EeXaqwTSBGk3BmC2UxVi8acciCuS_sJyXgc8Nw8NeRaZADppZiX8gCZh1bgIoSPuB9Hbjm2TctFcWi4VJOCv0wBQ3wlyCg0SMz0zFzPnv4ff9fJrMrgplTOQ44Dx1VexCDQU1TXTSwQkWkDLKCBtGejSYUVxqSvCfqsMudn154wI_A6bmlP-xq7I_ARHFpjdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای تماشاگران بعد از بازی و تشکر ملی‌پوشان از آن‌ها
/خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/662081" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662079">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6051968a50.mp4?token=N2v3K--9RBYWdwn7DRgGnCbMEeLc9lODqjCh2qsSL2J3vmgFPi1eD4AfZ2dnMgDWZzu8-Ny7SDah0PI1WhhQDu5V5Uhxm8QmWU0vW9Amuolnkm-kGTkmjKEVJu1Td0cUxxLm2XnUY8EcqETucGbBM8MqWye4YNdOmYZml3dwC0FjFzCwoeKDcj_9U6wVebtAfyeeWrgffJDXItQwsIJaup5EkLaRx8iUiEIQ6XucEFPayWnibCyBtcx93wY8gX6kIi4HzejS4U5C6N5SFTUTHsdqHRlUCP7OKBV5ezmqKq5i1lj6huaokUf1mCnRLgFKXSz3zaEQHk_j6Ms-T3ptEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6051968a50.mp4?token=N2v3K--9RBYWdwn7DRgGnCbMEeLc9lODqjCh2qsSL2J3vmgFPi1eD4AfZ2dnMgDWZzu8-Ny7SDah0PI1WhhQDu5V5Uhxm8QmWU0vW9Amuolnkm-kGTkmjKEVJu1Td0cUxxLm2XnUY8EcqETucGbBM8MqWye4YNdOmYZml3dwC0FjFzCwoeKDcj_9U6wVebtAfyeeWrgffJDXItQwsIJaup5EkLaRx8iUiEIQ6XucEFPayWnibCyBtcx93wY8gX6kIi4HzejS4U5C6N5SFTUTHsdqHRlUCP7OKBV5ezmqKq5i1lj6huaokUf1mCnRLgFKXSz3zaEQHk_j6Ms-T3ptEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماکان نبودی ببینی ما با بلژیک تیم دهم جهان مساوی کردیم. ماکان نبودی ببینی ما خیلی خوب بازی کردیم. همه کار کردن ما ببازیم ولی نباختیم
کاش بودی ماکان...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/662079" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662078">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ff0f76ee0.mp4?token=ga6turcPhaktxjbk6wWVl9S9qBLAQGOmH3fLgdom0ZkJRqaEKzGhXKvM7RKDjM4yxEEThTkldIefhdMq42QWdTv-vS_8rzJ9RRCrwVKUba784cp_Tv9ufGmcPiURB4QO3M0yLiF9IFrfsLumhC9Aj0HMq7aVIoE1VkAmpYQ2empJw3R5NGkx-aZcccmMB5ELbokfguE6SPJEzAuR2dPbCQW57ONOcWntP2bhUtXWu18E85T7jIDn-kiC321U9sFP_jf_o_hMYm9s2v7IrlyVOTsAVPpES3oNBLPEQOFmXjNqx1yjkpk-Yvo5zS2OpZhyanCA_fEl-ceXh2-Wb5EbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ff0f76ee0.mp4?token=ga6turcPhaktxjbk6wWVl9S9qBLAQGOmH3fLgdom0ZkJRqaEKzGhXKvM7RKDjM4yxEEThTkldIefhdMq42QWdTv-vS_8rzJ9RRCrwVKUba784cp_Tv9ufGmcPiURB4QO3M0yLiF9IFrfsLumhC9Aj0HMq7aVIoE1VkAmpYQ2empJw3R5NGkx-aZcccmMB5ELbokfguE6SPJEzAuR2dPbCQW57ONOcWntP2bhUtXWu18E85T7jIDn-kiC321U9sFP_jf_o_hMYm9s2v7IrlyVOTsAVPpES3oNBLPEQOFmXjNqx1yjkpk-Yvo5zS2OpZhyanCA_fEl-ceXh2-Wb5EbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاربران فضای مجازی این ویدیو را با کپشن «عادی‌ترین واکنش بیرانوند در بازی امشب» منتشر می‌کنند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/662078" target="_blank">📅 00:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662077">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW_lhgWhFCzotEE8cetvDQm49tM1OMEVFh_HO_FX0ek15dSlXfx3P-hmI9eRGDeg5RULXQ9-71NSB9r1CS8ZLDjt4zS64FVL5YHcSMAmHANwi4oVyl60LATHxIZaUwcX1eptsschsSjpXbmh2Dp6DTBnwj2hZSVhW_mia2BOkUeCXzlIGLfrsKfo1KNJjQgwgIU-KjGWYjV0L-MQJSXwwk17VeG2aYJN_-SxKFD3-d1Ssm2fGKEbgI73yywcUFzWDleLrM8QrcLUGmpptRi61eb8FpTsUymq8YqmNsAu_61Fj9Y-xX1YEBHb0krwdiAtKTiU-NmedS8M6Q0h1BUrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا بیرانوند با عملکرد بی نظیری که داشت بهترین بازیکن زمین شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/662077" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662076">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOHusbyLZ-ozJKBKQbgyM1ajOiGmBhImobrG7IN_6xhr_GwN80tcJVe-aC0JdqoG8bSsvwlfFl7QCgP8ngwr9a4NvwBRU7flk6J5qqi8fTOZ7enMGZNqSw1EQWeC4L3UfAAGGyAUsEeHAg5v50QSu4_u96lNhRB7-gTogUwmdcpqMYamhnds5Gu-TkiGJ6N-Dwi5Bc11abRmf811rh8yz6-Cu1hvXxPjey6W0l-kSFzorxpGIxIj9m58KmkyIkpWE63xYBOvqNYZcYRQW458A4PBNwMeun4Do77UByuy4eZqdvDwZskFGOV9C_VLcrjgEFOsivc1GyyiDH7UuUBpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران صدر نشین گروه G
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/662076" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662075">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfyLpLR2FxQT1zKlwKsl1GAKvGbFky5JW8gZpuCuoxJ5hkTKwA72SanzsDiKojfC6aqkqEyjCOlpYvlo6wh22X98uPpDHKzr-clPpfYPD89Tv09wPiqK9K8ymt7VFLfRT_mBnf2K2LdQM72u00TmnPadIl8U0obAaOqHOSi1x0smh4TDh-9rTs8PLRT9DtZTyadTmsteHwkQa53Hr_EDy-3OnY2-lIKgKqwJUhmvQpd7lGsyKBhsBnY2wShaEX91Neo8-LHHcR-ggyixGqewzVtLLIUSYPNal9ze-JIBKxyLwFjzGpBTzmJfjTJgCIqBTfxIjvvH38sHLHW1HK-PTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا بیرانوند با عملکرد بی نظیری که داشت بهترین بازیکن زمین شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/662075" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662074">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlNa06W0rGiB5giNqXcfW9Cn9iz4TYthi6d1klrRQsP74t27AT7UZovwSZOtRZAdFGMXcUpn85QNGbKVHoWeSRvP9y8Vf1rHr-Xhvy-mwrnjAIIZvwVjNRu1tpGZFMTxhjXYcVT9SDoESvtHpN0VCS5BwoA-p2H3M4C0I1Y1G40DMFIdBA5cyxDL6wOzKsR2KzB-5yeKpkwnB5b0IQhuh6ELsnl4YENJ8IE2Vb5970wykBNYQk_vWO3gDwfSIondaTpKtN8hoHA4Xl2Y9FszI6kzeYxmz9u7TXA2nHLPqg3bufFS4e4QSgp86czfEFiOAWzF6D8RbNRhce6231Niyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از بلژیک امتیاز گرفت
🔹
تیم ملی ایران در دومین دیدار از جام جهانی ۲۰۲۶ مقابل تیم ملی بلژیک به تساوی بدون گل رسید.
🔹
تیم ملی ایران با این تساوی ۲ امتیازی شد تا همچنان شانس صعود به مرحله حذفی را داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/662074" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662073">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایران ۰_۰ بلژیک</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/662073" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662072">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تمام</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662072" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک دقیقه تا پایان</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/662071" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662070">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سرعت بازی به شدت بالا رفته در دقایق پایانی</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/662070" target="_blank">📅 00:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662069">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/662069" target="_blank">📅 00:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662068">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پایان ۹۰ دقیقه</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/662068" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662067">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
دیپلمات آمریکایی: هر چهار طرف از روند مذاکرات راضی هستند
رسانه آمریکایی-صهیونیستی آکسیوس به نقل از یک دیپلمات آمریکایی
مدعی شد:
🔹
مذاکرات با ایران صبح یکشنبه آغاز شد و تقریباً بدون وقفه در قالب‌های مختلف ادامه یافت.
🔹
یکی از موضوعات اصلی بحث، سازوکارهای جلوگیری از اصطکاک و اجرای آتش‌بس در لبنان است.
🔹
ما درباره تنگه هرمز و اظهارات اخیر تهران در مورد احتمال بسته شدن آن با ایران و میانجیگران گفت‌وگو کردیم.
🔹
ما به روشنی گفته‌ایم که می‌خواهیم از باز ماندن کامل تنگه هرمز اطمینان حاصل کنیم.
🔹
ما در موضوع تنگه هرمز پیشرفت خوبی داشته‌ایم.
🔹
ما در مذاکرات روز یکشنبه درباره همه عناصر توافق هسته‌ای بحث کردیم.
🔹
ما مذاکرات مفیدی در مورد سازوکارهای اجرای مفاد یادداشت تفاهم با ایران داشتیم.
🔹
ما در مورد طرحی برای ادامه مذاکرات در سطح رهبری ارشد و تیم‌های فنی بحث کردیم.
🔹
میانجیگران پاکستانی و قطری به هر دو طرف کمک می‌کنند تا بر اختلافات و مشکلات غلبه کنند.
🔹
هر چهار طرف از روند مذاکرات راضی هستند.
🔹
ما احساس می‌کنیم که دور اول مذاکرات، زمینه لازم را برای اعتمادسازی در مرحله بعدی فراهم می‌کند.
🔹
انتظار می‌رود مذاکرات سیاسی سطح بالا روز دوشنبه پایان یابد.
🔹
مذاکرات بین تیم‌های فنی ادامه خواهد یافت و آنها احتمالاً برای ادامه کار خود در سوئیس باقی خواهند ماند./جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/662067" target="_blank">📅 00:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662066">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چه می‌کنه این علیرضا بیرانوند
بهترین زمین بوده با اختلاف</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/662066" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662065">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcjTTv3Fa_4tAAgZjnwOlWPuo1Mz8hXDuq6zFS2TMl1NQSf9KEZ_46I0eAC4Ief1LZF2UHVe9Ec04riplKGtFLyNg1yAui7IcgjicZx-nUPyXnq6QbpoYOaGL6AhQGWFh2qIKcX-plj4B6G0909yBGoxdamhw9Guj5Ba8wup3sI9-NWu2CFsTjrM_HVAeYwerUUUSmv22FkvmHkjAxqIjC8dmwv_5PynI9P88enCm4JGzTIMSkCH8av8tjCmCGfuLOLAKY9e6j-n_3hG779wTKi-N2v9jxRjW8N-QO4fSvNmpJpUlbvclkeJuWWU63RaCUk8Vw42GAZqPEvpXxKZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقابل در توافق
🔹
مذاکرات ایران و آمریکا امروز در ژنو سوئیس با میانجی‌گری قطر و پاکستان برگزار شد. بر اساس گزارش‌های منتشرشده، بخش عمده گفت‌وگوها بر موضوع نقض تعهدات توسط امریکا در پی حمله اسرائیل به لبنان معطوف شد. تهدیدات ترامپ همزمان با این مذاکرات اما با واکنش قاطع هیئت ایرانی مواجه شد و فضای مذاکرات را تحت تأثیر قرار داد. در نتیجه، گفت‌وگوها به شکل مستقیم ادامه نیافت و تبادل مواضع و پیام‌ها از طریق میانجی‌ها دنبال شد تا به طرف آمریکایی ثابت شود که ایران زیر فشار مذاکره نمی‌کند.
🔹
هفتصدوهشتادویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/662065" target="_blank">📅 00:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662064">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd336ae7ba.mp4?token=ZGeklZZTRPIhowcWnZ_-Iw0-fB5xJy9Rmxc0RB2BjR80SYhMoJCmkGug9LRdfRB6AbkZlRs8cQsUpP4eFAWL9ikWaP0yEfq9oxZ7WZXwVscgdk6riCI9IVSjORPcAkmMS-u74_QL4_bIjtdICVvCiJuDxiVXDEdLS-cR9VdgE0SWk4zlui-8b_7L2uXEUlkNS015nc_zMrIKBSuwiwNOQ7gi_rc7lhgE-hegHUMIy5apPD7CW9s-RvGvup6nxP63x3e7b8OjJFt8czAACxsMTye7PBpimYNrpH57Hlaa5OV-rDqueOjIG0tvm9Usgc_DVaO4QQx8X-cQlbw2kOZgVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd336ae7ba.mp4?token=ZGeklZZTRPIhowcWnZ_-Iw0-fB5xJy9Rmxc0RB2BjR80SYhMoJCmkGug9LRdfRB6AbkZlRs8cQsUpP4eFAWL9ikWaP0yEfq9oxZ7WZXwVscgdk6riCI9IVSjORPcAkmMS-u74_QL4_bIjtdICVvCiJuDxiVXDEdLS-cR9VdgE0SWk4zlui-8b_7L2uXEUlkNS015nc_zMrIKBSuwiwNOQ7gi_rc7lhgE-hegHUMIy5apPD7CW9s-RvGvup6nxP63x3e7b8OjJFt8czAACxsMTye7PBpimYNrpH57Hlaa5OV-rDqueOjIG0tvm9Usgc_DVaO4QQx8X-cQlbw2kOZgVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش تک نفره جلوی بلژیکی‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/662064" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662063">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/272dc78b3b.mp4?token=jtcB5q7Pbhf22NP3DoQqvnnsbfASmnJJGebwk84O9gVkc7jF0CIdTxQEeE6QaR3IZ6K1U61H167JXmKVuAFuIx011C_-NEli1foUMf-nFIwLkL21BjB6HHE7sYmO0k4niVjen6k9hNsAvXlz10O1l_Vq_uvxI9yWKBs0mo6AUwVrY3F84ku7OSShSHr1GQnofD00QZ1ytrqDXlAfveT5hRJnWBSSSsWaknOCeasekfU0576xNFB3ovXEN1eLVQ6tCSVZSu2YzoICxqvQmaWlIy9PE7djBqjS-VcefmarU_ysPVWNJHpQpRSapmhkA4uaLZs5YxJ542u4Gpy_tIFqtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/272dc78b3b.mp4?token=jtcB5q7Pbhf22NP3DoQqvnnsbfASmnJJGebwk84O9gVkc7jF0CIdTxQEeE6QaR3IZ6K1U61H167JXmKVuAFuIx011C_-NEli1foUMf-nFIwLkL21BjB6HHE7sYmO0k4niVjen6k9hNsAvXlz10O1l_Vq_uvxI9yWKBs0mo6AUwVrY3F84ku7OSShSHr1GQnofD00QZ1ytrqDXlAfveT5hRJnWBSSSsWaknOCeasekfU0576xNFB3ovXEN1eLVQ6tCSVZSu2YzoICxqvQmaWlIy9PE7djBqjS-VcefmarU_ysPVWNJHpQpRSapmhkA4uaLZs5YxJ542u4Gpy_tIFqtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و بازم علیرضا بیرانوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/662063" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662062">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حسین زاده به جای عزت‌اللهی</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/662062" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662061">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1I_KTfAZX94rd_iVKBaBE3h8a8LPbQblLo14Rn1K3of7X41kfvF8HyNmX5ne1OKky5TfrCcSfORyeC8_G4b1LKZaHqwud4LOILNbzz561hxxCQf1rrsHjw588oXnWRjy1s7ywrgvP9cIuXEDUeXxPD51WNRj5jwETJB4cbisovrV7AnbfZvaNZwFvTVWdJ5RbKaAuQEcUuicE_U45r71cfPR1fu75ru-xp8zRjBajffz_QIvmVqJoCrlFdRcKJPHe5l7Uod-KGcNESycklgsObAA8dfkkqf-DQVi200TH0BCpz84HOMXED4djvdMDZSFgQmHcKDICEY0ZqXGmsRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمجید رسانه تاچ‌لاین انگلیس از دروازه‌بان تیم ملی ایران: بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/662061" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbna88WARwlWd8r-5n3vu6qPsPksZoMak8Ocgvko0Jh00ANA29xBAaIMbl2CkAEz6SfP46XzoCksIqPOAAmAQXjLGMNbaLjj_xwowzVz4_IR2AZlypJ9sskznPgEe6cIWkX98uKvy2_ozgUWu89cS8Y5jPG-vqDW2cCV_1QO332pIo5RouAIoFEN_AhuPuSoL6YIRRkGM0Dj4Q6hX5X8g8KUm7SKB_fArLYpVAgcqG1aEekFATSyT0QKOygnnkYrJ813zOiOQeWN9tPGfUx2S23EMHU4KaH4hPpwRS3TdjncEIWVRGi0rzb42uSezbkdW69rPoVNZRCluJTSsgSQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1M7GKaZz1s87ROZtm6dYSVR0Vje9j2s_6bYVheuuTclxV-7Du65dRj9xopT9Pg3jFCN1-OGdTHgtTzl1RE61U1mzdhmK7wP3QMJzf6a2sgxNLZaStnOsnNhyWjyDT_Tea2jhLV20QVZ0Yl1cl-T4K0d_PcaBfx35GJCoJgSIisz-rsF7nCLaQJLp_8mnxAgjI1j5ysp4R6nsOk_1lUxQ7nmhvXMdeIQFp3DAeLuMVoxZDWw-GtuFPD0dN56QPM4yOKwG-E8Zo5MbIyF93lM3PkA8j9ASo850BRukOyExL2cVNc2qmpAMS6C1z0y4UdvimEvRnmyNKPMML7zPh17nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_A2X7NclBDD6tejv_hRqQduTQZZp1d1QHZNfPYf761fZJbWtbMjQL1M3GDcDs95Th89Fb50OMvR-BUTvDO21JJQp26RtMFnkcUFIPrX7eKGTgHKOX72AXLbTPP_CW3T2NGvT1w2ZciQRySIXJsjkJd4JOSdbM9Co5u4Mo1VLoiwV-3E70l3xznVHcLL2RpSLCUijtA_LbJ_CuR5q7BYhiD7okGqHnYYKCMT24wtukYBt4hmFAY4Bueo07v5QBVDhQny6e7IulGPcAzYjQHWeBcJVvh9mSwaE90W3v16HZeOP6P2vAWN16hQEhWpUNVYOMBszVtEW0V0pDoDRxahzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boAUvqPWmTarIqvzpQB3KombPkEMfzGnQd7d2uL46wwUpKrq5paFTEWBhvDwsvEV6cCBaE2TtSWFgJ_0zzqYHiGNrCUtvr1Wr7IadKCnEcZU-jtQJiuCkU9Yh8OU3mpt2pQi94w5XMhXzgyZYoGzHx2enPL_82VkBrbAUr4UX2YEd_v-T-PaUSRQ0z5Np8_lUk0jmdKr12ufL2u8lxiRjxF4vgwZUG01q7o1RKhHEfgLbtz9U8gWXWmcuzhGsuxNkwEm2Hsu-X4_mmHrXDk9atOAK0NSJg0zkmrS2yAb1tM3E3-nZSG7Hz_qwmqeYR2gLr6pqnV6ZJITGGQwopXInQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب ماندگار فوتبال ایران؛
واکنش بیلچرریپورت به سوپرسیو بیرانوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/662057" target="_blank">📅 00:18 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
