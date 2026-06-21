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
<img src="https://cdn4.telesco.pe/file/QUWrsBeVcezt6XZnOhlTFVmucaUn_uuqX9SOtZjfU0d2nV4T63JPkL6rIBdEZhcPoo1sgEOEcumFFtCxW_8FnHJ592LHjvefFUog-1ealBabOiyovNxaNCrlUZmek6_LWiAE5LKLfWEUq-tPSwpZiANcXbC2gTX7l6WerGDtrjwYWn0nRU2E02wp5deYHfLqJQorwORxiQDic5Sm1syQLuz_LX_RY1yI_-CqLTG4SXGaWYYIUME0xQxaBCUqp3maLeddz63AurkRTfcYXa4lLkJb-kYs1UjHWbk139AGEoeMGGRyNkqxOvE4SX5RKWrL_6KmWVyiBk9-oBijSxN1WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 221K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 21:50:26</div>
<hr>

<div class="tg-post" id="msg-66642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=VQVQ7p-lPUZwAEGGaMYkvmLi8Hw65c57aPEmn2DjDjfBwo9sUkKdkCaJrYaodESJrDDz3CgW0KVB604xfnLpCBMjHZrL29cFo1uXIiMTmzvh10yHySs4Srct49_sI7CPFTDBM-CGARkYgAcZgiE4nbxUiPQa4QlvL9icp7nVgd90BFaxQfd3ykB73Hp-YdpzG6svflMFUqVFehPU50usTGe03nClIR1IqOHbOPthHHAwc-l7mfkQiTTuZWA-RM0puzZWNWgWBkAN5XEVOudoXparrwxwHhoR1eVUUH8ygOHWeAchm6PuuAFpKJjzubxeHZsLXQrYhuLxhd7VZl2xOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae050db23.mp4?token=VQVQ7p-lPUZwAEGGaMYkvmLi8Hw65c57aPEmn2DjDjfBwo9sUkKdkCaJrYaodESJrDDz3CgW0KVB604xfnLpCBMjHZrL29cFo1uXIiMTmzvh10yHySs4Srct49_sI7CPFTDBM-CGARkYgAcZgiE4nbxUiPQa4QlvL9icp7nVgd90BFaxQfd3ykB73Hp-YdpzG6svflMFUqVFehPU50usTGe03nClIR1IqOHbOPthHHAwc-l7mfkQiTTuZWA-RM0puzZWNWgWBkAN5XEVOudoXparrwxwHhoR1eVUUH8ygOHWeAchm6PuuAFpKJjzubxeHZsLXQrYhuLxhd7VZl2xOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون ایران،جدید در مقابل قدیم
😔
@News_Hut</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/news_hut/66642" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hk-2VV0yp9dyjqwhqbnYqIpg7ek8nMTc7qAItbbzKAe9cWA_zXL8T72ypiPHJ_j-OoLNpoOvK4DGcA_yYIGYpEWKxzdyl0unaN1_xkjVmfod2r9JEyeVIBsDCg8xEE0vxRq_cQ-HOwB_S318yNm3rnv68uJHG-xyTBu_kFD-zWidttZ-d6TVmyjbNtw_d8glAhpBjnIvbYMnAbgogAmpH_R_zdR94CNdf113T5YKFLJcaPD1oXLnFkhVnkyE6DLRSVzk_5vgIOxA4xf1ykqduxpD_o3k8Ez14qBoA3fI4ZkkfIt1mNraQQpFaNg3GaXl_Af1Q1wPAa4wsXNtWx01lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/news_hut/66641" target="_blank">📅 21:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66639">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UTxHzvoBKiazieauEgVe34zFtPwFfx9nGyC-S4aYywRdgzeVO7dQPnHtSCVbCcQO6vqMiJrOGzgtvs0x5NbT8NEof1bsQdtv6czeZXR_fiJXHonRlQ3P0FnHu2qQsf090iymJQ1oGuJK5o1XwUYrMyEaRR__wEaE80HAjeZuLunR_MsJUqy2pEuNKVi9zHNRe2jXfOvti-QrJxdqoiM6GhZs9d_h95t1CQvjuOkm3yBH32cpKsJkC3bQvgEz26nD3eHTTaKzTztIZEcmQfSe1JhwA-V6yIQ32ZnwrG6oVY2WH6WL958ZuyWYXwQldaVswQzJ6_oCQ_kSb1QXzlGBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAqrlBkZFz20jIy6xgc7RLL2xxTUx3LjegpXPTdCpDcgJkv4z8VGE29NJRyBUU4tfeJOxv35QAgWGRRC-D8zo8BAzQAfKGXzwTHnaZ4qaxCDVF3dxrp0J1t5Z6ZwOwl_AinJdXq8uW0cyXs60SA5KLKGRNPKBN-Pu46o7R2M8uyjfD8o4Ewmifvgalc4vSGjX92Z2MDq4QUIDR0Axi39dJ6s1SvfMlY44i0KAy-l1_kPgMEA5hmfIK8qNDzH8Om-a5C1ayrl2t31XW_RYpxPvO7zS5ETL2p3xHX0V7ypn5PhNc9np9huJfAy-f4i9hDsZzvlWVuOpMmGyKV6gYjSfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن  سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو بدون سانسور رایگان میزاره گفتم اینجا هم معرفی کنم…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/66639" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66638">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY-WQej0O8O6_aLgF-i9uNqjkxiFHJ_dl9DXJJmrlFtNiSQ6NM520bRhUXK6x2vidY1J_wIf_0s_1VUqbFEEGSa3WmwqF345lMkq7fN-jS6FUOFYuB7AukKs7ytIJE0EbEFZ8BOXZ2fF7GiZf7OX_a4UKgl0UDJCFeQULRs3mPa81RKOn7fJxh6Mjw-HaQJ6yc6RCmhZyDAdILBKy12CquREZQxJ_jb2gq2_DumbeIj7RrBEApHU6-AlFTGbdG35vayQ4O2tzCDm0NJhCRSBahWe5REatdqCCrc7waYXxv4g4JJOMpGexZZFCr8uRlxtY1RgfYgfJisFqBxOyVVO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ایران با بلژیک بازی داره و میدونم نصف کانال دنبال یه پخش درست حسابی می‌گردن
سپی یه پلتفرم دست کرده به اسم چسفیل که علاوه بر خود بازی، تمرینات، ورود بازیکنا به ورزشگاه و… از ساعت 9 از یه شبکه خارجی همرو
بدون سانسور رایگان
میزاره
گفتم اینجا هم معرفی کنم شاید به دردتون بخوره.
هرکی خواست بازی رو با پوشش کامل‌تر دنبال کنه یه سر به چسفیل
بزنه
👇
لینک پخش بازی:
chosefil.com/fa/programs?utm_source=telegram
ایدی کانال تلگرامش:
@officialchosefil</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/66638" target="_blank">📅 21:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66637">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLOuVFdN_3qhS_uMvTbvajYu8EWjPACF-w8wYOcYZwJ1c6Wqo07e4wU4YBzTXqWp49iqfsh3ZQyymhh-Oa17p3oS1YsqcExA_ppXIg_g7NNWFvf_eP44UQi1CcneDMOScWlerE2pGOKwXkQpZ-F0Z3lmpTPKaxYgp-OsoXJJIl4GeriEjTVfZ4vN19CG9pFhzjeI8Ei0yMlwUyIsPMMwQ6SGCsRBvKcLDuVENnqHEd1qgMNZXjvTADu0BIbmn32qNzTi4nW_MVD-ewTDC-AQQWj-BcNqDrfqV6SH7d2C-2gjv_gU9Xq-mW-w4mL_grWcsw9st_dFokSn65sEIsDs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
یک دیپلمات حاضر در مذاکرات در سوئیس ادعا می‌کند که هیئت ایرانی آنجا را ترک نکرده و مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/news_hut/66637" target="_blank">📅 20:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqeVdocc98gkMjs9mOQ8Ko1lSfEiIOLK3omaBv9biAriorh9XJh4xEf_dAS1AZehX8_JutyVFjkx0-nVaLe0R3XOtUI-HQVN_297V13vy2HyS8wyln1H6v1TBTGDQogME7Yo9sflkFWXfbHqc-GO0luS7ity57t9AXNlr7LI_qACsOs36FZmJnnYp8oOMrSTHeMKwqaQmVP7-NthHP68eOO3EgQRmtL7wYy1U1xnJmlBZuxlQaFMfeHjYhte7QqX79fBKvNFg4IdAbd6-6a-GYn-eWmYZ0ApYSjiOEJ8Gs5s8Xl__UoEK9H52nD4T5YhTACLQniLGJ2aoTOYCiqN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
نتانیاهو و صهیونیست‌ها در آستانه نابودی توافق و اقتصاد جهانی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/66636" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZim1s9cPFQfE4vyVg2xqnJbsMdfVgpg5sxyXED9sTIODagMCSrouBbHYLWBcgy8tAWGOZNpQHEuj8Yxd4tjg9UBoRNILJPDSbit4HJH2jHxcNmcio1OJg9FmP_HG_lt0qX1j7ohvP8l0J9Zp3VTFwgEWyvORWAkMppwFWvpEga2KmeVsIJdZoYiGkvFYAHK0tgJI2wih1ixkrF48kAXYJNi6xv4iDFMNlo_KY0gwVFI_8D3Lc2fVg6ejD0OSXjRYeDyGUjX6O3kVo4vkO8JzFNnzBDcN6F3i0hp7FkanN6PvGgLqbtb3hQIj_n7JH3n85h1ZbqskJO__zIJu-KOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pzZ3exCfLqf3TfXWSaXM2D6wexjWxzU0-X2ulDwYjfiwywx5bY7Yn5DbIZ9yguR4-6buMyLRZU_NVPxW4fLHExMLNe_GIP9dXVxCmxah1qxYMA3MkmDU6Zok_W34s9IMnb2b7OewlqSf01uSqBPyL4j1CZTk5dPf2crsTsSLeWKj31-CGXQeFIFPLADcnt0pNRyfb29fk8550dPXKwGO28xEd5jYihNKpq4VOxFZcgJpGXbeLcx_0uCl2P5bdYB521dMY21KxLyreR6AhXOp8FpEuPA8ZGNQn72Wv8wWd8mN8P8NetwZNGyPGg-6r96XrFZK4Xh28-b3Abybz2a3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAn0oQeFrM-BbriUKHF1m_eO3FSuXXfQ6hKUZmXZMf08vYbxGZCeK23oPZ6t6OkN93sRL8bXl4XbRiFooi67CjhParJQBdF3R19JLjXZvgKj4BACyC8s37UujkQtyIK4k4fVAPdVjevNFhB9Ht4mkKj1gZ_k0YLo8dpiY1rvC3H0Ykth-ey6ysR5RulZo6Ak-pA3tWUJEgxFSC9DSkZlP-O6PN5sNp1iDcuWjlgs5zIGJF_c-rhxdtZiIiQ3iLz-RvRZ2Ys0aeAxDL9Wg7zNqGAPybos0nzdYAcDF6w1AYr559s8TBrso6xUI9HvTI48Usgsd3XZp64ZwKUtVhcjwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afzWGhKz8TbyJRQa25jqwLv3RdPruRGvrXD9tqmtD6xqkq4vB8XKPDgePE8lasxhrqOG8vj5Ic7-vGBUNRgNekES8i-MEsBU7fNtemshOFYpcYITVFGwWm0AfUh0dIzlcHpX2_WgvkNzknVV7RmIIlX8Clhp_gotK9Az2LSCxiZJKKz8eDG9EtUoecrSFwlgZW0UYME4KK-Ywly0ZxwiQyDLKDe_YZyQGOey4ru8YiHC4C0TwtrAdn476XhJzyjM13YOdlO2VNWw5JlAPRgcTykTp-SvB0YDHFo-6TVoMCYtEny508ytz2X_nxgj30iV5J9A544NVYvcE4dvt3-XOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
گروه تروریستی حزب‌الله که در زیر روستایی در بالای تپه‌ای در جنوب لبنان، تنها چند کیلومتر دورتر از مرز اسرائیل، مدفون شده است، یک «پایگاه هوایی» زیرزمینی برای پهپادها ساخته است که از آن هواپیماهای بدون سرنشین ساخت ایران را به سمت اسرائیل پرتاب می‌کند.
مقامات نظامی اسرائیل در جریان یک بازدید رسانه‌ای سازمان‌یافته از این مکان در هفته گذشته به تایمز اسرائیل گفتند که این تأسیسات زیرزمینی که با درهای فولادی عظیم ضد انفجار محافظت می‌شود، در دهه گذشته با کمک مستقیم ایران، از جمله برنامه‌ریزی و تأمین مالی، ساخته شده است.
به گفته نیروهای دفاعی اسرائیل، این تونل چند صد متر در دل کوه امتداد دارد و به عمق ۲۹ متر (۹۵ فوت) در زیر مجدل زون - از جمله زیر یک مسجد - می‌رسد.
به گفته ارتش، در داخل تونل، که به اندازه کافی پهن بوده که یک وسیله نقلیه استاندارد بتواند از آن عبور کند، حزب‌الله پهپادهای ساخت ایران را با استفاده از قطعات قاچاق شده به لبنان مونتاژ کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/news_hut/66632" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/news_hut/66631" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QednTlioUa3MqEKwKMw2_6ZhJ0pfzjazyOMJvs4Wls73JlfSGzy2pxEowPdqNq6GVpcsaLJ7rHvMW79I3E_rcBGowv2-a8P4vv5dloOzMw9YAS5X4TInUXvG7O_MXxwRaeSlJn2rsdG_x_mw6s1jZBZ99w-XM0HxV5qF0lPjbKi3WNLN2Neff51inJDOpNvd9AzcTrbbdaboamnuRw1Mxv7xll292V5mmSg-EROF16OhbI8HT8qyq8nSVXx79AVjNDcbZr1M6gdjVYndfSBScDXo0atkDWaEys2lZNka98Ev5Q9j9w80lVHTCil8M9LJ865bvtgOt1gfyCtlzPpCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/news_hut/66630" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYc9nSun1vg1D3IxxSRbMcQPjVPkt4kAR-jqz4fYQHxIiZiqSG1aQilCAm7qq54CADClvOSR--QGQDXSdzOtkoLJspHRnKGhEgA11C_a7SH_iCsNPpOb7E0jzyi1R22iRq97fFLOWUQvnUY-8HsKzsoD7ZCw37XR9TRk7B6d9zyKy1jptx6s7XjAVVeqAmmOGm62tL2-KTNrTWC_Wt7jCqb__sWCyH3pJlN1KmuieiUETE8A9pVU2Kpd9_eSYKnNfmH-VfZ7NLCDGSlDVFpq6iK1SsqGeHCLyI3QmdpYCLXuo1oD_xQ7JbfojkLMvFqY6d1ZUEi29796ZMfkaSOqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=MkmsVmfzJGMLKwAppySTQz_v_pHjlCGI7g4RdzIZQ0r2aaEqL0_4dnli3uq91GkX1biyIHSW7m2vGdmlfT3hlm2TdZBhZzaEmn35eCsWOhGGV0nblDXUM8J7KorPRChSUuYktw5T5TWlULeu-qodCgZmiKUhIttAoyZtnMfciD6IdCH-9evYblQx1nGS8WdW-tN7rQeCxKTLBrFXl2ublYEy07SZVyUeO2a7wA0t6cnxaaQJxHuZHUq8MIJNgyG-gUzJyRPk7SrcHrLGX9yoS6IqHg4rff5Wn5CTx1eSX5IQE7_gLBwrwsVXG1vo90XNIosCt0G_E6OrgiQez9FWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=MkmsVmfzJGMLKwAppySTQz_v_pHjlCGI7g4RdzIZQ0r2aaEqL0_4dnli3uq91GkX1biyIHSW7m2vGdmlfT3hlm2TdZBhZzaEmn35eCsWOhGGV0nblDXUM8J7KorPRChSUuYktw5T5TWlULeu-qodCgZmiKUhIttAoyZtnMfciD6IdCH-9evYblQx1nGS8WdW-tN7rQeCxKTLBrFXl2ublYEy07SZVyUeO2a7wA0t6cnxaaQJxHuZHUq8MIJNgyG-gUzJyRPk7SrcHrLGX9yoS6IqHg4rff5Wn5CTx1eSX5IQE7_gLBwrwsVXG1vo90XNIosCt0G_E6OrgiQez9FWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=azn75r3uaSl2hC6JHZr0mm_VKlWHtU5U7BNoSHJKg7kUGvynCwhlEim5ezjxO--hNhQlIEbw3rLANBOkTvAs7xR1vfRgetXvZt6pxlOfE3tOUJTNXYw9TyHvvhN0PkiZlCjVpBj1Ir1iDg_U_TBrOb9vuaP_MIJfY7fqh3iEH7M77G-A9mORmgfT_L-NDIkViHOROHoGSngiDUCyJVuNCvfjC1uMS-UdAXG59f4vJHfWG_nUttjlgxiiQDGn7dHI3_C6rch4smd6s5BbHzRkfp4B1f0JVkz0LWY2o7EE8wksRAConTBuUB05uDMxpstQ-w-bC4b7pbS26yXNqocGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=azn75r3uaSl2hC6JHZr0mm_VKlWHtU5U7BNoSHJKg7kUGvynCwhlEim5ezjxO--hNhQlIEbw3rLANBOkTvAs7xR1vfRgetXvZt6pxlOfE3tOUJTNXYw9TyHvvhN0PkiZlCjVpBj1Ir1iDg_U_TBrOb9vuaP_MIJfY7fqh3iEH7M77G-A9mORmgfT_L-NDIkViHOROHoGSngiDUCyJVuNCvfjC1uMS-UdAXG59f4vJHfWG_nUttjlgxiiQDGn7dHI3_C6rch4smd6s5BbHzRkfp4B1f0JVkz0LWY2o7EE8wksRAConTBuUB05uDMxpstQ-w-bC4b7pbS26yXNqocGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSWIdyt4SY2HcP_Sg6rXv3UEtiZ3Gb3TNXhSZXywwT4vyfRTEsIN7iNzRHUfUZZQHD1ztExRTL3km1iu_f8xbUQ-xpFzEjjwZ9tTqGoKhX489CVAKWE5iD2im-m9y9mJTLFMrGe6JkJ--PzCZW_QKJpn75Wt8zE2AHuvyi8LVnlDOOvOwU1mlmMB_UtLg0FdNZ7ku2mr2RqG4Nu3ffY5RjK_P8tdNc5vfl4UZwvfkLFkz72WxaZRz8zwqeWgZ_xe_zDkbYr1rzr3pogroX5r6LvxDULeMfepI8iI2QS4YHvTBPbkhWrj4QV999BZDhus3CQ3R24meuLzfYdti89sgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK5cyeWGiIEyH-LgNgm97vXisi8rVISI18k4Q-S5etX2DUVTkZhxyi1TCQXM6NiwgXV7LlyYPuzJSHdPDv6_1CxyHZCcKztY8mqeiCcc9Nmwmro37j03Qq99Deasj2Yi1VN6ejR5equ4Rzb-5c0RIdlaF2xxmRtjKpgcTwvWp5tZ3SBCOKf4K_ilHPlbG8KK7J1KS15d9_aiESCpx3DhNYn-W4YlibJmJCdRRtAVUDgzrVwColqzw4vYdN4Vt6XOxgzu6MXamECy1f_zJdj_iRrbB979bn2dDET1hONU5nZtC1cvuvnJityaAQCLXVl0GhonuRkN3I3H-0gN2PArlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwipsXxZSz9wF-7dzX3lGY5LShWkhFNDj3uBQzRA8xVP4EdZ0av5ymiWWNxESHTUQbIMVMLJkOwFIPeLEmHtXlBDvOY_-y9s2_qGfyqyiX7wr8cgqo0zTKwSUawoK0XqK2TDZDmi_5M3HFkIpCidN15CtzWZbzyvu2kxLa67LI5IAMQ4ErvhFZv9E53ObatZ0ulFEPqZ2XlRR4obdoiSSNd46cElGWVju6juWN4Drq7udUqhfKWYKQDPyIZihdudIUx_142Err0FCqSc7MsbOxVGt-nJcPpEBe4fKcVu90dF_5PxKIvtM4TJAlBtdoo_dC6La0BPXs-BT05XewuuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldhHRenpqVMg03Ru5lK0HkB-uv5qrIh06lexlQWR49j_nr7oJHLyFEUiwAIyaxhRLMiOpT4ZsIoi7OYOjGSMBOqHihKqXZ7Qrwr-mvcbrEI8YHq9hIkr46xb6hSIG7jhV40KKETibYod5BVaGKiqcYQQmSmE05XgOWUxZQr_f8GtC-GY2X4KfebtJZadID6oJfz7SmqpD3h0Cl8y6xxovZg2AZn06U0rs44Yaf9V_oeYthgyHcAlnHPffmwMISiSXrQW3132RK_oOtXdvXbHpFOaUj_HHXoIgmIrDPZqN8pWVQ4ZYxiNJ2UP0lGaFG0mZdhSGdBhOeOHtGWeoOOKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7FPsnAyuwmKYwqqXDz8SKsHHJ10yxr4viSDJkdy7BT3HvExAtkVh5K-zRBuk7q_47qzdlXWulFEkb3UmDbnM4IPUbo1_BsfmcFfaAjK_n_dEaJmE8Qhi8pCN5bkrePy7SSs0X0lvJxDWNbQZfxcyVsIvUkb-E7gYMsx3VjLmtD7ZMkg6hQ_xpa4Hu79mnT0JHmtprXy8bwpaD7S7LaadUemQ01luV9Zfu5HxaxQ8lJXgOmNjAoVSm7wJ94YNac2teplGm6rP20x54enuV4QrndpaB4Ccgs645pqRdTKuHFIxlbxIszadS_pYSpeg58acL-YnnY1fbWiKqeGmSK02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5LTuhy8xIJ5vuoEp9jJ4NTt9zI1ll4Y3m2vLMzv08SW0TJF4Kftp5O1YGTkhZhVhp2c-_w9B_ktw63d8xi6utxWoEDqbS6T0twbxDfXQesGDCKsaokO32uW_b7bYZ6IF33jDmB3zsOT7gUOHPusEKMRWRhiXcFy3-TOVIV2zIbedCTpq0KxlGJuCBen_b-IdY881KBJxRehyfYDSjZUeXLv-7_wZ9keteDMXsnclq1dEsvvO8FtUsIsc1Wx7W6Unx-NIcYlklIOWs6fhJslBzXy8ePkwIplw2hEFQQfrDQ-1SGdjU8bipK48yncGP9G2wFuwVsPyfkF3DUbgvXu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqZ3BDJGTapXBetuDMpLZLY1ma2k2PscrzAW2ri9YK2vgylyf1FM7fIKjNvnROd0v64WXbdkwKMjb-FEhkGqHB0ZMNXxkRF6HPvu3IqSXOItpFa3JL4Q13-u7o-pumGONY-7ZFjy4L9iqwuRT69O9aqmjxfQ5n3Ue8X8x30jRahBdqlobNnDJV2l6LdmVfdjGa5TirYkntn9P9N0r4-UVlzvvdAYFud1qc_38yTgUEwrj4MoP7YIgvURq_o1q_7SdoqzmzSqINuTTVmhxzRjC002KOTwrTPwigjEHHNDZDPNkY6ub3JO2Uus9KHhuKigRs5ktmG_b-PT3WXgrFKEhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncFmRxmqM5ZY07BOhZZHsL-woLQyG4ocYuXbFP6cCalIQjKhYrY8U6RoqPoeQqQCL6T8QqB7wrq4PXnbscenXe35HqyLg_Egww9-EnLa9i1SA4ySENgZv1HMNI1D8CliVFlnd84GRhkF1HRHVUC9Hx13BK0RL9cHTkSQrjC8Z9oQkrJsnuqkIraNfZRM3JIkzH9bl-szw75yoUiplKBW_KJzFVz1G-xAv-TqN8l0FfAw-lPC0Bd0qK4pXJj60WzHEBkA4SFwj3V-fQIApYOzFPAkVbkrjOqU-g5ShJ1QZuslnmy_tmPfJecaOEiFZD4NvCXnZadk1MP6XrJwWtJ_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=SVPhzrBC6JUfBeimiLLUv89KXrI8vxcHwks0y6wcJcuUE5mtzy0eenHPAu1H_2MLEUK9oB8BsUPMQtbeJwT59q1bvhdcwnaqMW3N9aK_qT6i9xphWXuoiTt_0I0tAt8OlKDoqDhzEtSW54y-ir9h7btbVOTUmUCE04bbJSgvVQ2nVKCSFLfdij2iTammoGzCLU1lH01UJioPz8iWXnftyQCwtL7YYm77y29mtymZbiq6yJI20LP4bmvzVZ6AAVbx18n8cxUV7h0mLtiVeaSNCH5xlzI6x1xqRaxj9LaQql5ucSZlLMdMrNA9jydEoF5BSa1QXOHuALIG1iCffppWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=SVPhzrBC6JUfBeimiLLUv89KXrI8vxcHwks0y6wcJcuUE5mtzy0eenHPAu1H_2MLEUK9oB8BsUPMQtbeJwT59q1bvhdcwnaqMW3N9aK_qT6i9xphWXuoiTt_0I0tAt8OlKDoqDhzEtSW54y-ir9h7btbVOTUmUCE04bbJSgvVQ2nVKCSFLfdij2iTammoGzCLU1lH01UJioPz8iWXnftyQCwtL7YYm77y29mtymZbiq6yJI20LP4bmvzVZ6AAVbx18n8cxUV7h0mLtiVeaSNCH5xlzI6x1xqRaxj9LaQql5ucSZlLMdMrNA9jydEoF5BSa1QXOHuALIG1iCffppWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2_4vbQghyo3dbp6f8OBYfW5V6tttJ8ZdgZkXvGaFp5mJwhgEhq0Jm1u8GdRiUKbpMqkI9T4DAje1NsCs6mB1j470ghycH4W1HhkVLY3BecB9WrVnj8ksAiHUcqcGI6ACxIf3zE5RpIhXAA5qY9AToBvs33c5QRWuvdMwXjVDw3ABgh52S0SdxgGCkMIoWw82_sdmGvauFC_ZnJYmHiTgoU_PDgsSwha9rpipsMm0qsPPrf8h7LESYzSInmElD8Gc6-wK-OhZJUvhdQkBIFuEJ1FdS8Ih03NHUll7iZnqfel6znL-1rLxqN1X0US3wiq3C7lyMFHfFVBfxB-JMR-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxume8HH2NNDee5-mJYJRAFdz5U4f8Y6oguPqhqwKZvxbzrJK4NSY8oGBVTxSMgiv2ToE1GYUnIH3bW-uScpfWB1vaz28lXMdKvYncDjrmvMRPEdiNJR7b1Fc1-tfsSpI3MIp0eVVCP8R8OBPI5H4ES6-aorSIKdDP8SsQzLfoEVPa10-3f5bQP2PLgL1JJ7nv6W4bee-8YOXB2TMwA2TlAzySAqL3dNV2Ipref9zDvpLtYf_U6je_W0evaDbJsyKrKqccig-1JWaPCFhJ_-hwYjfvXsmud2U4iqQ9Y3fSp6n-HNrJBSAgwSV43jroyJikCzunMm2nKZFnk3QzSgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=Nqq_XIy1aTCY0ylTvVbcuXUMQKbEHyub-IRU-06G2dSjz-sUQLwowBmcFWKfoiGoEwiBF51P1RQaPNA3Whmnq1dnP5XzOVIZ-ZlBVCURcKih5ESlcgRMH4gqfzr_lGK5HUUkY9rjwaEtrEXBlQ9HVjvk1HtO9gdhEU-__AbPTR8VIa4oPKVdQC68RvUco4EEOtyA3gL6r7WpyyYeZ8PRYoTUULXRxph7iRgtgvip5raxwDUpVgKDs5nwc4JgIAsAVlEOK6clOozsSi1LxM_JzNfq0FMwmli1Gf8yJnfkbtTcbNisOitZl359bfYxTiI_M58ZTTlZL0z8o0oOkw46Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=Nqq_XIy1aTCY0ylTvVbcuXUMQKbEHyub-IRU-06G2dSjz-sUQLwowBmcFWKfoiGoEwiBF51P1RQaPNA3Whmnq1dnP5XzOVIZ-ZlBVCURcKih5ESlcgRMH4gqfzr_lGK5HUUkY9rjwaEtrEXBlQ9HVjvk1HtO9gdhEU-__AbPTR8VIa4oPKVdQC68RvUco4EEOtyA3gL6r7WpyyYeZ8PRYoTUULXRxph7iRgtgvip5raxwDUpVgKDs5nwc4JgIAsAVlEOK6clOozsSi1LxM_JzNfq0FMwmli1Gf8yJnfkbtTcbNisOitZl359bfYxTiI_M58ZTTlZL0z8o0oOkw46Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SHzJCKpn9r8sGp0OTCDH6dTEPCOE5v1eAS3jjVm7swBSR3R91eL-v7fWUpXWbnLJknkkQHcX2TH9baynYypVL1Kpp2uCbNg7f2F2xXjeqLkd7S_9Oqx1m7quMnnP1EiL_stUKeD0Ed0o7Pbrolz_t76RUtBLw32e0iaFqInbhR8DlKBlaxIbr4MePWXprNsiMn3nFtyIprk8Iqo5yo5ieuXjupejYwpx_AV0gh4-W9J6arV3sltpEO5jqTtUp3y7_x8yMG0QTl_-59YcIOTubh6dG9SJ9FzWoUzvGEk-a1urYEPwtvrNp4brM640bcYXLt2TDAM0mGeDmz8jJ5sE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3-kW6gfDOwhRdZXk0ZMY-bFVwQP271XXQ1xnxHHbwo4ojlQDHlpqvB8HCtrDzWVrMhiUTxTl0eUtf0to_sUPO_0GCAl7liRvp9eOCoFaae2Ew8rJXr-Vwqnjljq3Qmhn0zPx9WW0yr8tVL5l84sqb2t0xmMzfu4bDdjWj0jm_tv80mvBoyzTthKuPJK5NzK67ov31Wo_l_3x_KVPWEPN-XQD3Rm06kDv2W6dFp0tVEoKnc0JPHiCsf50KWCBkQfac4Fh8lYp0-WZXH90bWDD9kjA_9EzkQAhLRTRUAeS89u3c-zB2K_jXN_rRmYo3x-bVBAErreqvgmWRH3KcB-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=JxgvGGS-JyYsCJi1gZdofdGyRqC5uwruA9vHYFTv4jI8OCEPrVwcMBu-cc4cQn4jOOAGgveeIf5caJ8TXRvPWM_qy_rtKjkl4kx2YXP-N9A-mEhNYjvYIJTs7WVWjf4TAJREHv4qGHCC5SjCgBDl3VkvZbgI4i1QuPADPbAnfKzXNXFbbQ6eG4SIwny9OdLzaJc3t-Xbz2P-WGTtw9lxDELAuPRrgZ2MvdOHgD2oxTC3Hh1Sum5GqZ3VyMsKYb5ZBIYo4njYHIv6KgZKD1ZnDwmVhWW3jXUb5MBUGu4Rs2ecL32swEdiWOLCYMuIigG9TIwx1_xcmZjAFndIxcSNIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=JxgvGGS-JyYsCJi1gZdofdGyRqC5uwruA9vHYFTv4jI8OCEPrVwcMBu-cc4cQn4jOOAGgveeIf5caJ8TXRvPWM_qy_rtKjkl4kx2YXP-N9A-mEhNYjvYIJTs7WVWjf4TAJREHv4qGHCC5SjCgBDl3VkvZbgI4i1QuPADPbAnfKzXNXFbbQ6eG4SIwny9OdLzaJc3t-Xbz2P-WGTtw9lxDELAuPRrgZ2MvdOHgD2oxTC3Hh1Sum5GqZ3VyMsKYb5ZBIYo4njYHIv6KgZKD1ZnDwmVhWW3jXUb5MBUGu4Rs2ecL32swEdiWOLCYMuIigG9TIwx1_xcmZjAFndIxcSNIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbEBnIfOejjJJUM2WdRaHPEOXJpIQzcliaV3zoRiWXMV69wnN04WEZaR4i2R6iWE_6H5gFTpyMJM-v0R3dY2vd5GbAwCUeog22ZO6MnOQoKa45WesFaTKkIv3TWQeXEbFqI8iJ6Ws4VCGg-f59qxdPaYFxlfzLS-7QCLlnWHWJGiRQPP4fMVpmRHYH2B3A39Nw9fy_OOqwNSRf56WYLW8oAfBOt7wky0lZbH1KRzM0IewWXhOluE0dVWf_2b6GdeE-J42VfZ0K9qg7LMcnp5T-rlza83Y6TGkriET-bQI-XMvHZBN8uuQgT7iOQMAtcCzft4zuKIxM_tlIwEnlG8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=E3_2TrD79y2XIHacJGV1YN1PMpgdjhHLrtw33VFliDuhEi0xZK0gSoHJNDtb3TWwn-kRat3WSLV4IuVf951jM_-6ZHv0q3BBykwjOwePAx2kxOXyh1-KY2nBr1ufOb_j3jsgQoTOJ1537_G5nQPMVjpL5LmaVbC1YpcyFqBORrIGETXrFKbiHq535uF7zf3FCJiXb-yoh_atMhwlziI0h1bk97Oh9iPafLNodHHKSj-vDk4JzpcmSXPTH5dI3jejjDd6kSrcHuYKDg6f9nSQ1ChupUVuW99g65QLqgn7iOuHPThxXAv8GYgV_IdYimAYbX5KNzJ6QQU-mV0pfqGyeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=E3_2TrD79y2XIHacJGV1YN1PMpgdjhHLrtw33VFliDuhEi0xZK0gSoHJNDtb3TWwn-kRat3WSLV4IuVf951jM_-6ZHv0q3BBykwjOwePAx2kxOXyh1-KY2nBr1ufOb_j3jsgQoTOJ1537_G5nQPMVjpL5LmaVbC1YpcyFqBORrIGETXrFKbiHq535uF7zf3FCJiXb-yoh_atMhwlziI0h1bk97Oh9iPafLNodHHKSj-vDk4JzpcmSXPTH5dI3jejjDd6kSrcHuYKDg6f9nSQ1ChupUVuW99g65QLqgn7iOuHPThxXAv8GYgV_IdYimAYbX5KNzJ6QQU-mV0pfqGyeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=mWMDZJjGrUrld7my1gaZEJyttMSIdt8VuWJpRQlXhOC4hLSnmNoyy3d-j1_B-2KgF9X7etfr7oZYjSMdo4SDp3o6Nlyigz_jSL8aAXhw96jchG0ggWmmJZbRjum41AtebNsc2K5vmYQhf_EkBrJcQFmDlWEdav2JnDTc-FpomYslmKmDOxmz9ftmGscK6rp5zcTjcd1jFVQe1XzBzPCN1KuEjALXyPfc3kiXvYM8f09eDFLZ--kLw-_TCPMwyMV47nj_7xxpIFlVRFSUQeaxPKOUaR1ytLNr8epoqAmf3imaxOBvEL7qIo_IBSOia7Kr8NdYVedys2zXwF-isjo6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=mWMDZJjGrUrld7my1gaZEJyttMSIdt8VuWJpRQlXhOC4hLSnmNoyy3d-j1_B-2KgF9X7etfr7oZYjSMdo4SDp3o6Nlyigz_jSL8aAXhw96jchG0ggWmmJZbRjum41AtebNsc2K5vmYQhf_EkBrJcQFmDlWEdav2JnDTc-FpomYslmKmDOxmz9ftmGscK6rp5zcTjcd1jFVQe1XzBzPCN1KuEjALXyPfc3kiXvYM8f09eDFLZ--kLw-_TCPMwyMV47nj_7xxpIFlVRFSUQeaxPKOUaR1ytLNr8epoqAmf3imaxOBvEL7qIo_IBSOia7Kr8NdYVedys2zXwF-isjo6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWEApWiuaOUrSzlwxq4WabrTodbTzaSKA4kVUbMaqIRiH70q3D03ulE_1zz122rBzMvW2Wi3AWcsQcX866NEdDalSUu5X5oT5GuL6OatV3z6URtJEQZTLK_qNm1H0S3eGkyBRfHpTVGpHpSU9bi5bj15OaZrArCg6fb1xpkmXNLLnB3P5bQzi9kjCQUpM9Kvy0z-wFginJd4NpJPk4guW8KJtabEigMgo_Q9s1AT1g43_pyMJj660w1GLQ9VTjkw50yBLRkrWp_SjK1F4BtDVjyi-1ZQ09aHN__KM9wjlqg7lwtlsZlz_M9WTrJm1hGx7jCi_JKA0RuK9WElPBWOUUp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWEApWiuaOUrSzlwxq4WabrTodbTzaSKA4kVUbMaqIRiH70q3D03ulE_1zz122rBzMvW2Wi3AWcsQcX866NEdDalSUu5X5oT5GuL6OatV3z6URtJEQZTLK_qNm1H0S3eGkyBRfHpTVGpHpSU9bi5bj15OaZrArCg6fb1xpkmXNLLnB3P5bQzi9kjCQUpM9Kvy0z-wFginJd4NpJPk4guW8KJtabEigMgo_Q9s1AT1g43_pyMJj660w1GLQ9VTjkw50yBLRkrWp_SjK1F4BtDVjyi-1ZQ09aHN__KM9wjlqg7lwtlsZlz_M9WTrJm1hGx7jCi_JKA0RuK9WElPBWOUUp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=WiqJi40t7KhRDZOQQKou5NXBYLYbxmsq0svy8RjCmvGnZbJV1_w93LAlCiQBGtRolaAc0eyZCxf3DD5qzwEQtIUCjAVfAzbmEOp85KruisonkSqyx2UIqxfWnk1EWuXSnDp69Q9aHZxzv-Y1gOWw2aALSqaRbx-oVPcHhJ1qbBWCkUz6TeepTSGufL-WcHasBZ-sKHYAMsdZPX5AXVuHhuQPbK7RLFcEXC3srWoy9-vDGQn3exkszPMWOxA0JgtDjzaEoJ53beF_Oy9tnxXevSWMhSPyVgVB45575b_hyDaqpjyRlxuNPLke5MZW_9KoyegsxCZ7PBcZY9BWE_T_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=WiqJi40t7KhRDZOQQKou5NXBYLYbxmsq0svy8RjCmvGnZbJV1_w93LAlCiQBGtRolaAc0eyZCxf3DD5qzwEQtIUCjAVfAzbmEOp85KruisonkSqyx2UIqxfWnk1EWuXSnDp69Q9aHZxzv-Y1gOWw2aALSqaRbx-oVPcHhJ1qbBWCkUz6TeepTSGufL-WcHasBZ-sKHYAMsdZPX5AXVuHhuQPbK7RLFcEXC3srWoy9-vDGQn3exkszPMWOxA0JgtDjzaEoJ53beF_Oy9tnxXevSWMhSPyVgVB45575b_hyDaqpjyRlxuNPLke5MZW_9KoyegsxCZ7PBcZY9BWE_T_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3dIpeS4e2qHw_dUSEfrJyysOepA9ljS__H9k25wt3UxNXZEh88EUntJ4p9dWrG2xjVHnt1hZgtXGJLnAapOUziVJ8nSYuPIcoRV-gugF99-npxBIYHbwoCJNgkxLmzevxdUJC6OOJuKc10WuVCv3UHkgR6gZaOhLkjTbmeBEw1fwPyAdNm_NLj03dxjB2leyp4_wcVZL50FqRue1HNPOzqMlB6PbcBnlUMY0UBTIKY7HDlnULU43w_3OZnQk9-y_upSyN9SXfLYpVN2qfc3KsWWwvbyRYz36DjvkKFwk1cef0MnZkhQ113Trbpg66j9Iog633FDNLYkWWFynZjNhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=NiF1e-eHwTSjIPk7sALGkbI8Sk1GDHsFEUusm3KTwJP75tFmvSnzqlpN6979RGH6U6002CE7wdbOpsuwHGsqMYFK-Nb1lFYYof50c2oUPB4GiFbhK8gf1GJ6y_ogYTZj4fyw4Ug3P8vZY2-y8BR9Ug8H105FX9eGxNV-9_MBvtidqcl2fiE2JwY9q4nqFershQ7gVQDgv3MqGi7H1-O3ohJUpQnB4hG2nSgX1gilLJUIifCGHNJ4LM7M_No_yPW5VdEmofa9H5t9hDw0YsSpYGiLCPp6tkXCLb-_5LzmLGgxZ7-bHVLXHsIPlPvOQ_Evc69Kva2nmcq9ZLILZEskQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=NiF1e-eHwTSjIPk7sALGkbI8Sk1GDHsFEUusm3KTwJP75tFmvSnzqlpN6979RGH6U6002CE7wdbOpsuwHGsqMYFK-Nb1lFYYof50c2oUPB4GiFbhK8gf1GJ6y_ogYTZj4fyw4Ug3P8vZY2-y8BR9Ug8H105FX9eGxNV-9_MBvtidqcl2fiE2JwY9q4nqFershQ7gVQDgv3MqGi7H1-O3ohJUpQnB4hG2nSgX1gilLJUIifCGHNJ4LM7M_No_yPW5VdEmofa9H5t9hDw0YsSpYGiLCPp6tkXCLb-_5LzmLGgxZ7-bHVLXHsIPlPvOQ_Evc69Kva2nmcq9ZLILZEskQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okcj53i1vlm4NsSz9qBFAnTnzfSknXCdQnj4veGixkJ6ouDscVRqgYms_CvvJ9B2bK7tFcir3fmrRH3gsjM5iYz6WtCjjT68Z6P_6XMYr0QsMZ24XHGMY5CNrzaPWacUT9SHYanqmbsKNUofiqci9LvFRjfvp-r7DDb8L8SqNhHmvpADgL5-YDSRNCY_o09f1bTresYzRSX7hkk-NjVvIFqtxPnw7we0k0rtjOJSfbwwvstqsfHvChcLuelmM6Z5q8e6X4JgmLS-jthxM5q-3P4PeUxTb3ZGHKFClIxOykfWjqjmBB3S-4CEc9ktGrBT7Fj6OUa1DABtlX6QGlw55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqjHMOSmJ4XzJC7HyjWSUgnTfoICuU3ooE89sOro0P6y3ZXeZ-DQEppLrfFAgYQPqIuHZ6ecX9itDnxG0eXx4as0y9r1CgEL9gyLDGTMfUKebQ_jD7kLIsaA0yJ3Za5g6avxaenkrjNABBcVv5qFMasMJY2o0dwM_iki6ICCOE-xsSg_5pEAXyDDwfbhT72VZYBpCgRNfzJyfkCVfFb43rguNFK9VniuwYDetfvQYXuys4BCAunXwz9EBEHjG3gNI5bgbW1p_SWhdO5isv6gTeJaUHJCEHL-fLoz3F9r5L61crgHOMKRhNUKi8HoTJR4Zz5fgw2j2oIHllEDjB6tNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsM-MkDqctDKvZWVEEfawjzF-pM-SkPL1nnbmwS4H1K_NL24Vc4goynmbWL8gj3wDtTeViqVuRDdQYosdCi3BgAvwY2DBF83zE2mk6fogqEqrG2gNVuH1vqSYegQ3rB-LNM0RRUfGRS7P9wsyeXSB1uVlmnLZfuesyygT9Y0azKT2lcrkq3Br41IP7gnAXGpoLs6w9uLvlCIDVru6spf3qElMCxp3ez01IvaZbbWA9CzzFDQWQoyXgyigto6cZN3mw6ezTCHZLUBoCfGvz8CwaZxYMnYqKezhbNQ-VkLxK5jxHXxjEqce-As5e9Y0EBbaYio-HkRg3xXqWM4fsKJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=Jyo-ZgRm-lz3ogTABGT951BntYvjMxvEzg-ZHnCyxdxYNfk5_U2vpU3q6Ar7l6QnjTfR0d1ROkckjM55-87X8j0_1jP0qA23p_JB1ts7XiY68K37uFZEh9aManqpzsRweNRdtDAEZAWOQhWr7IyVVRmKpk8mawke9Tfr0IBdsU78apTAkEnMS6WOZc3CpJtywwGGzDJkcJcrTNQgIspaqN-k7e3UpMyoUj37eIUlUW_2NkuQPyXciVnoAYMaktxT9CS9pRifKySYLVKFs8gMAzftqH9OFTxhlc-YvgOzT5eK5jlbYW8hmD8OWX-KQNF0Pt-0xN3PRMTKZq0odnxiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=Jyo-ZgRm-lz3ogTABGT951BntYvjMxvEzg-ZHnCyxdxYNfk5_U2vpU3q6Ar7l6QnjTfR0d1ROkckjM55-87X8j0_1jP0qA23p_JB1ts7XiY68K37uFZEh9aManqpzsRweNRdtDAEZAWOQhWr7IyVVRmKpk8mawke9Tfr0IBdsU78apTAkEnMS6WOZc3CpJtywwGGzDJkcJcrTNQgIspaqN-k7e3UpMyoUj37eIUlUW_2NkuQPyXciVnoAYMaktxT9CS9pRifKySYLVKFs8gMAzftqH9OFTxhlc-YvgOzT5eK5jlbYW8hmD8OWX-KQNF0Pt-0xN3PRMTKZq0odnxiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm4EiZcpKMRA8kCmw5JJDQ-vaxycR7eCHTCcjEuEnpuYnklOQC0m_9l5WDJNiNmjvncKlBs5fMU8zjJdgCdQP0n9gRW1v8wymnRDvgHQ0ZnP-5jZr9ZHmuP35oEQ2zsaIONdTOPrhFU6oXu5GiSDVQTfU1S3jO2wh3DjqNvYKdIW_DmQbyr5pIwAh4CgSlKFr1NsBLJ6hoDJERzGK9nMcyWL2-SfyoOXRBcsN88aMHkLhcl3ejg980_89PDhHXQOY3hmYc0ctsuoFGNz3Jn8v-s3aLrpmOs1juiWL2Ej9Way8zHeJa6JtwGYuhz7WGY68aoy1sCLMoLcec1tYOfnvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBnxjYdd115uvnWVK73sdNiJOaS1bJg3rFmnV0eoegCrzCFP8Csm9Ywy3EV5-WMqccI5RKhLBfLBvT4chDU-eG2jCjriIcoVekBTNVmvuucn8hXc1DzuYbIf4yE5s_INXYeUC2g5kod8s683SyEQHz1r-s09obLeSDMW3yaCJdtly92ABNvbmH7i-3B3LMBy2LE8k-NjPPAMwzY4ku-KF2ErpwqbzRVmk8cm5Hr0t8TqLIA8vGrOT3Zcil81ALjs5d8TOjLvYXnvFRQ1sg9b1QVEPgG5iZ4rvgkwPjUSmTBCeA55Nkn_drOSj3GU_zxZAhoqs5E5EmRJifn7BY5Fcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYnKjC3BaxZhL8ZxtsZVxNfg_gWiRW7ny2mpRFhGC2Yp_qrSddxKaIUoKPdg8IE99qz7jznMbvH-ctz7699anRoAXpzBbtJULiETNCOrgiQd8ecprHHGfWRgScfZs2GqWi72oRVVNI2ccv-xF0InEdHc4g2Q0NjPwHvl1HkXkOK9Zm-l5k-Jxr2-IoM3zen3X-yr-uk4WZgbDlzjDT7GsHV69pdM9cpliCtoqrtGsYxwarinUprlSDyUNNCY_tpjnUZJIEdwYi361w2olsjnWGHtfKV__4EAw07honxV5MQ1Hxyp9UFz6M6si9SzQFiIieuM_A3tfmqw0dE1BCZq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=qzkWCN9j_q07FjbWsFu6jfF-y9jFAXRdRDOv0eS0FeHio70F75Ox1gsfiarUhSgEBKBCga03e1CpzNgdcQWVmuTxhMFw64gGUy9Kl7rDt6KvSdYBEHFZH7JvLVjjtC3n4oUCYm4EtitatwVOvn7ePs1tBuq99HZux4geZdODTcQNgtCxv4XoS77h3-KdB68kUQSPxaapqEP5ivrWu9uxtuutOi8LqnNSUMqFYCm3OxKdOOb5AzX0T8JzFUMZiRr8pKvBEU84ZTe1YKyMftPqwFS2XY9vGFoSzNypBXod1__9zAOFrbwvV8jJry4bFLSlegvjrCBIECeN_omRu1YIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=qzkWCN9j_q07FjbWsFu6jfF-y9jFAXRdRDOv0eS0FeHio70F75Ox1gsfiarUhSgEBKBCga03e1CpzNgdcQWVmuTxhMFw64gGUy9Kl7rDt6KvSdYBEHFZH7JvLVjjtC3n4oUCYm4EtitatwVOvn7ePs1tBuq99HZux4geZdODTcQNgtCxv4XoS77h3-KdB68kUQSPxaapqEP5ivrWu9uxtuutOi8LqnNSUMqFYCm3OxKdOOb5AzX0T8JzFUMZiRr8pKvBEU84ZTe1YKyMftPqwFS2XY9vGFoSzNypBXod1__9zAOFrbwvV8jJry4bFLSlegvjrCBIECeN_omRu1YIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=YUSbhEMXAohSywuJ9AKwuSgZEzhcmKbuKU2ppFjcgEMZo0_8EVK7iYTMwpjOxYvlvq-2teVUmJCs9Cj1J3diRMcX70vjRo2xa6a3zp9SSK4Fdy89iCN22qGJ6uzvclpEsA0rjXziEYsK7cDFizKaLCg9cULm_y_lu2KPqDQV-XgBeCkq5Qs8l-o7Qv2yz65jAeiSMkbLjr9pLMpnkulULkC9Fgx6_uC8jQZsKe_aGhJdfbBRDt3ES2YnesgbUi6JFwDkNdUQDRtTf_qQ1uZHX2_L4Xx7MN011RFbtqCOEGxLxUO6dD6j1pS5pXZCx4waC-VyNp_Y-ZNCkZ6aix-ITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=YUSbhEMXAohSywuJ9AKwuSgZEzhcmKbuKU2ppFjcgEMZo0_8EVK7iYTMwpjOxYvlvq-2teVUmJCs9Cj1J3diRMcX70vjRo2xa6a3zp9SSK4Fdy89iCN22qGJ6uzvclpEsA0rjXziEYsK7cDFizKaLCg9cULm_y_lu2KPqDQV-XgBeCkq5Qs8l-o7Qv2yz65jAeiSMkbLjr9pLMpnkulULkC9Fgx6_uC8jQZsKe_aGhJdfbBRDt3ES2YnesgbUi6JFwDkNdUQDRtTf_qQ1uZHX2_L4Xx7MN011RFbtqCOEGxLxUO6dD6j1pS5pXZCx4waC-VyNp_Y-ZNCkZ6aix-ITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=sf5OUhcLmgX1BjguH5GzgctfUZfJPjT5y58QoUGpMg93-pJGUwumOcp5wNd1peuaENRrCLRAPhgnQPuQBvDANcT8FQbr9C2rj0LSETlbKpncB_rhcmWfFkU6r5b73-E0IJ3cOBnuCz3VgO5S-FY6T465BvTu3FqgOzNZIhl5uHNFzCEtk2iDpMO84GZA9PnPNx5sR9-HOQoM7UxQSVwELPxswMmC2b42pDWb8S2T7Tr5fP55VvrvOknYk5Bp6_k5C4c7rzbtYCcN8fEQZqRbTsN5LFFmZxdOyACPFqBYB4saOrf-yDL36ASzXsxrWwKGU0X3OigvX1KhOGoQV-5Jcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=sf5OUhcLmgX1BjguH5GzgctfUZfJPjT5y58QoUGpMg93-pJGUwumOcp5wNd1peuaENRrCLRAPhgnQPuQBvDANcT8FQbr9C2rj0LSETlbKpncB_rhcmWfFkU6r5b73-E0IJ3cOBnuCz3VgO5S-FY6T465BvTu3FqgOzNZIhl5uHNFzCEtk2iDpMO84GZA9PnPNx5sR9-HOQoM7UxQSVwELPxswMmC2b42pDWb8S2T7Tr5fP55VvrvOknYk5Bp6_k5C4c7rzbtYCcN8fEQZqRbTsN5LFFmZxdOyACPFqBYB4saOrf-yDL36ASzXsxrWwKGU0X3OigvX1KhOGoQV-5Jcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=dVVPfUWAFuy-IyFgSZJT9zjAH_K_iQ7on9f50d_jPXLXyn3tVceHRcU1DWu3aW0YGQqmi5CyKX4Rm3Upllp_BEcJSJrtNSRza0pESET8NouR75ugFqjjfDrb-h8GdIJWflZm2qjnXYaN78KQ5XBe6ScBcIR9wwGJRRnLjEpi57YZpLDU68DayU7q1cyiFUJdAYG7eejyun6gchW9p07Y_bO2mTuSJ2ggtAFhBviO1XsBb1XAKlhFbWpFD8nXf_3-FVM1GUAMqYoV3eQ5b-0-Nl-pF8t1qsFIXFLtt2e00GzzoOgdZRMQstK9lcGlwuhY1B749Iwu1ngJQD7OevrjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=dVVPfUWAFuy-IyFgSZJT9zjAH_K_iQ7on9f50d_jPXLXyn3tVceHRcU1DWu3aW0YGQqmi5CyKX4Rm3Upllp_BEcJSJrtNSRza0pESET8NouR75ugFqjjfDrb-h8GdIJWflZm2qjnXYaN78KQ5XBe6ScBcIR9wwGJRRnLjEpi57YZpLDU68DayU7q1cyiFUJdAYG7eejyun6gchW9p07Y_bO2mTuSJ2ggtAFhBviO1XsBb1XAKlhFbWpFD8nXf_3-FVM1GUAMqYoV3eQ5b-0-Nl-pF8t1qsFIXFLtt2e00GzzoOgdZRMQstK9lcGlwuhY1B749Iwu1ngJQD7OevrjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeSjwMfIGL38zs9IGrI_NT4nKBa8Xg-KlPtZszxGD31NCuqDfQRAUAWpfbJcxF07fu8PPuJKA0P-bgQhc9YEliBKoQBVTRaiCuA3ggqggpd7N_De1JqTaont3rBX9QLdNpM5cnnEKajQ7WGGsW2p5yrLhkUj7LjMXn_n9NMuQKuJrqbNVjdP4jc_PDSjqwKbwoWDngc-eeSVCGvGlFiWTnnuLtrHHquV_t3u8UWfxJbKRVbSbCCYENEiysAn3JK1u-RPNMwJjTcja3exthIpWT9KGrTRhdAql-mNSHs4PqGZgKnawBQE7oKmrTFzxhp9U6pmoJh6FqzDkPaoRLyFgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtSFxIgDXQ0rqs5L5XOp_-onMgWClTXUaGpiugLc_KkvfU1LFnNxqX2bU9cPb8csDoCd51RC0oBuLpaD3VaxIsbQgU3iaZebvbmioe_9YNDnSUNCgxIljrzhDGMv8KfD3rVQ_H5blbS00YmIpePb9WBlxHFagI39JxYW1IrPPNCYjMzBSuRquNEU77cQBEqDl3yzQoRnPXQqucgqBPi8K_Q4k9IbjhtvPao3GHfY0tDdD8o0Yl3QK9SxnmM0QO12GFXR0R-ac_u12suZheeiKlBDAFxuR7SYtb4sMdqgV1icIVtjSOA47YBZWIghEsDHroQvWCEnxHsRaXhq-dOyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THYqYGMlIYb7n9qwuYk-luFFZUgObdCZtMi0ZehXp9Ybc1ZiyuyJQbViI4-wRrzV907NitWNPS4fldNiCxouluHEnwm99gxUp4qHE2ZYHwe8FVS0jMNDMw1iMRpjnVwGeH1d9y75Is5yAwgb9SseKG1I98AzTu58p8-xEGN7QktcuS9fmZB97ERZ9tEeZV6gtsxZNKU-4E16nbIMq_KTMrZ_B4qwwFRnWS6BjAJD9mdU6IjBKcgga9pyDfzQKNx4Vgx3oWH0TB_fS0r88rCDpyO3s-zekaR-zp8wVySOWWa7g8PC6YL9tfGmlPZNHgjgaBbx1tvHdFKyzxsf3VNAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmFRpEdcnfD59lg6DJis3LUpAdYlIhdbxBs_3fDYbP-z4YJRkGphiGGw93nbo5vT3uGP57SKudXzYwZCvH48N7-toXbbz2085Z1fGUOoTGmDrrnrfJOTaqjSio-nBf85tKqhvwNu8FpN4SVkV2irhAYVAbvjvVoezqOkOUZwsgztpNm0FKrcMEjEMJjsB61G0kDOCqPuRCq1EbFyvEdVcIxgwgJVN-Icm0McrbT8GFriiZENmSVBYljPl8twFOG_9w6NTlLHN84CKLQVKsQqSZq--UTQ0Go335NyDk4TAHTPFhj0Ul4oOyB_yuI2lpvIKgbmmJuIQkBLcjsfmQE-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM8NhNvEy7P0NFv1yhTk82XcRCTg-fV1xogDUZMuyrdbl80C8xyUOPGOI958tkXjNe8LB1TCuIst25TMyjuZkvmDgfUcI_qw0J5A2V77Q4KeH0LDSujqxe-03Nd1A-yDVSHYJevEj2HdtOyUHoV2KZwBxc3BFT-ti7ohnQUAC2YIqZZtzJ2T8XpW9NKGYWTdx2gM0mKLa1JIBt18kSxafSSVDz679dt1RNb82Urj_QNnvO-Ck5Kw-52awmVP5FJOur5iRcQeIJCu_IlL_5gCUMQI0J0O-IWNso5Tkqj8Fu6mcE5h_CVb968ZPNZ8jtnrXRD4MFU_vvkiou2fF9iKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFtbDaGdHHy883htILYcoMs8t0he36SDElU7Jd9RMJvizHOh2adwdVxFFkYgoQDulosLNB9AeqtHR-O6Re5k_I8I9JC2BjO_LEdmCYbfAKaZdIIfdAcehuD7AX6bB9BzfUBoABcV4XVHhP7eHSn-W6RgiPufxBlEkljdJ31nZSyqRNTsqueo6a_7fp-ldTyrgzBS_3_GQQ-6bcGr2Dqogb7F5BuA9ViPYOl6B4TbL7SlYHQTAeUhkqd_2GG4fsDUgN7pYrVeo5R2RUtwWgDHoFULw4YHdOOiHvbCMVzW4Q-sqy3XfP7EPIfLQQn_WgIAllfIF3fUgtyzpR_2B0VFSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pls9qRHbXpMWyeDfOsc8SiRJKY6JocdGba_WTfDGM8hPzDHSgq-YlRyDVs1CVgiVO6vV0-5ioOzlkVhuv0EoqLgQMXysY0Bks7WkpXHqq7CG8ToNYoz3m4j9KWe37KEH4UAKmh5NYfQMmsszJVUINpEd1a0kA2gnyXB9jBdAx0wKztjE7jzXA1lRE1XVKw0NIayOQHP7gAA9EYifwKqTd1GWKAvilqsnKAa2u8lCjUO3rhuEchBe-OJsNO8Dl75xWFn0T2efwf38KOgV6a_tLFdkIPKMZXuSF0IdzVKdfnIHbJXTs3hqkqpJ4msn-aBrU_61s0gOIwJpsT8aNR37Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=LaWF_j8qq1Xp3OCI4aidREZR4q0jU7Ltfc7y7JKU-beCtGtkdD5wSM3bwpS2QAch-g7bFxAwiXWBoxeG_P6_dX2CMDnQm6weUvB7gzs-kmaSTv8ENrhoy_ioujvu4Q0ECE3UoWyakrajaVDKMemYfdnkvPRyJUn90JCx8a1rnyFk85cJU6_HxXdeq1MhiAxA2xVyMK30AsjSMwpcsUpxkOkIGi1ESmQ7X5tqL_553w7ADlUhH8D17duBzadWE9y8JAh9LMJ3MNNdgCUwjI1uhvww7PgnwxZuhMBGooNxyyZr7LTDDWOiM-PO_IGsa0qq9SoMQ8rAZmwky2ywAMWuVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=LaWF_j8qq1Xp3OCI4aidREZR4q0jU7Ltfc7y7JKU-beCtGtkdD5wSM3bwpS2QAch-g7bFxAwiXWBoxeG_P6_dX2CMDnQm6weUvB7gzs-kmaSTv8ENrhoy_ioujvu4Q0ECE3UoWyakrajaVDKMemYfdnkvPRyJUn90JCx8a1rnyFk85cJU6_HxXdeq1MhiAxA2xVyMK30AsjSMwpcsUpxkOkIGi1ESmQ7X5tqL_553w7ADlUhH8D17duBzadWE9y8JAh9LMJ3MNNdgCUwjI1uhvww7PgnwxZuhMBGooNxyyZr7LTDDWOiM-PO_IGsa0qq9SoMQ8rAZmwky2ywAMWuVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=GogNbI5KUe4sLc3NHKi7iMSD_F3-4OJZv416fXz7Txs8cxeXSuHZMNmF_8fCnGdmou8L_WOcxJIStCG_It4fgbvqaYDyUQ192-PpVFwyAQONF_WdBDnohPlLbNIF0uHiOIYIxIr1rE-3iMrmVTSSUiUlsTElGTlj8HGhIDJPmEjXQK3TPVRnglAI3kD3HKBUnATjx9VDfr07mjDsYBF8TcWI_TWPSOiOyGVhPUIOYh05mExKsI6MeQXDNSoPNyMb1qb6Kk45ay34-Lat2kv9xBZbBHIVjnwzwyKbGJqLB8eZXyXhbzBpffw5nF2QL6209xJr7kzATWmeVZBuMONW4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=GogNbI5KUe4sLc3NHKi7iMSD_F3-4OJZv416fXz7Txs8cxeXSuHZMNmF_8fCnGdmou8L_WOcxJIStCG_It4fgbvqaYDyUQ192-PpVFwyAQONF_WdBDnohPlLbNIF0uHiOIYIxIr1rE-3iMrmVTSSUiUlsTElGTlj8HGhIDJPmEjXQK3TPVRnglAI3kD3HKBUnATjx9VDfr07mjDsYBF8TcWI_TWPSOiOyGVhPUIOYh05mExKsI6MeQXDNSoPNyMb1qb6Kk45ay34-Lat2kv9xBZbBHIVjnwzwyKbGJqLB8eZXyXhbzBpffw5nF2QL6209xJr7kzATWmeVZBuMONW4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=IkkLNX0aWTAfndT_8HXcH3jL_X7OLLHM7_WiRMwYm2xKME6Q_NqSWUWXG9CVuQa2XV5rATL1MGwLANuJWjlAFbavYOEG8AB-48nBa-DQamNqFx7cLW31MVu0_7gG5C5pwPTrj2KHaPLwymJvqdbCvDYJ4et56MUUlWkxFBmP_X4rQLIitL1pOB9O_tf1C0fkQ0mGWjSYeIWRm5SQNPkLVQ9JKRBgOy-Fi2MXcuJG6cKoLDOQtOud1W3qgd6ejMJF4S7xvM-JHqefdjG4K-2MhET4wTgjcqz3s53mu46bwibvYaAn0q0Yn-AL8L5uFSuIQrYl6s0QQt6CfFMK4ZIdJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=IkkLNX0aWTAfndT_8HXcH3jL_X7OLLHM7_WiRMwYm2xKME6Q_NqSWUWXG9CVuQa2XV5rATL1MGwLANuJWjlAFbavYOEG8AB-48nBa-DQamNqFx7cLW31MVu0_7gG5C5pwPTrj2KHaPLwymJvqdbCvDYJ4et56MUUlWkxFBmP_X4rQLIitL1pOB9O_tf1C0fkQ0mGWjSYeIWRm5SQNPkLVQ9JKRBgOy-Fi2MXcuJG6cKoLDOQtOud1W3qgd6ejMJF4S7xvM-JHqefdjG4K-2MhET4wTgjcqz3s53mu46bwibvYaAn0q0Yn-AL8L5uFSuIQrYl6s0QQt6CfFMK4ZIdJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=MR_0uNRmmSHjw9wkgmi6ECrL5uYoiMrZ4GZfvX6DjsAhWK1ljHn5_fl2txZ49KgMxqtBpzJfpsYqMVIEXBVDStYgu-DL2IRHM_-hqHX-LOi3YAuDCe2TB1AewEMFY_qfevGpcWhZGbRhqVOTaRTkC2nNNnueqLztlrBgkMeLqDc36G_ah2DqlL_bsiAKysM3-sVZF25tTm1A2q4A2e3yh9cCPX68xB5poli3d57M9gMsZsC7O1iTSw11UUz9i-enQ8O1v6yvkxWBPxUmLrDhuP8w3EnfAAbSKhZfzGUfpywjL0iR4guE3AwEj73E9hqO1I_937kViZy5SLMQViQ2Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=MR_0uNRmmSHjw9wkgmi6ECrL5uYoiMrZ4GZfvX6DjsAhWK1ljHn5_fl2txZ49KgMxqtBpzJfpsYqMVIEXBVDStYgu-DL2IRHM_-hqHX-LOi3YAuDCe2TB1AewEMFY_qfevGpcWhZGbRhqVOTaRTkC2nNNnueqLztlrBgkMeLqDc36G_ah2DqlL_bsiAKysM3-sVZF25tTm1A2q4A2e3yh9cCPX68xB5poli3d57M9gMsZsC7O1iTSw11UUz9i-enQ8O1v6yvkxWBPxUmLrDhuP8w3EnfAAbSKhZfzGUfpywjL0iR4guE3AwEj73E9hqO1I_937kViZy5SLMQViQ2Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=RwEJwo9xBfgSEQXXqvr6BguL_lxAttwSrkZHM7b6U7ITKYs042aNiZwK00512HQ2oJ0lEXvQ1SsM-K_-342S4284g5qYdFFbJL13vlvHXFifaLcjx_rmsG4SCAB25ZaF4FrTt8u1AekGxWONBksoFxiNLKAPejyxuSg0OyYFo9GcVAp8gqwbvihWPqiT77C8M3CDmYX3Qkucggw8bXCoTiokLzjWq-XPzs0Hd4Ca-HIavFEBlr3yue1ui3SAYELLn0ilzyz3G4RtdWfxjegtoAjejhzbDvIgGnePWmoTH8OZID4q351hIK7EGw4p5G-BBHVToFn1HY95LVkg007tCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=RwEJwo9xBfgSEQXXqvr6BguL_lxAttwSrkZHM7b6U7ITKYs042aNiZwK00512HQ2oJ0lEXvQ1SsM-K_-342S4284g5qYdFFbJL13vlvHXFifaLcjx_rmsG4SCAB25ZaF4FrTt8u1AekGxWONBksoFxiNLKAPejyxuSg0OyYFo9GcVAp8gqwbvihWPqiT77C8M3CDmYX3Qkucggw8bXCoTiokLzjWq-XPzs0Hd4Ca-HIavFEBlr3yue1ui3SAYELLn0ilzyz3G4RtdWfxjegtoAjejhzbDvIgGnePWmoTH8OZID4q351hIK7EGw4p5G-BBHVToFn1HY95LVkg007tCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=KebbkqrK75P8SF7PkXrMNGC54wSAls77nIpm9HxZhMs0_GDM3JqAE-U_t0W1IUsA11emzCc6XG3_4zaSc9VF7-prze1Wc3ikzt_eNudZVgM2oYEDwKDz3OrWYeoqmlQD2oGJB3zNMl8zR0gn0aX52bqqweknHaG7scuWakEyVUHBY8oNwtsXeGBOJa-uV4yZ9fBrRz41dI9nbEhT_E3UC875CaKt5bOVMSOPZ6VOpAd-5dtfnKOXy7QUfN9JUs2OiiNd1yOpWvFJoxt2y2iifYZ_HOS7ysbGj-d6oCZjI4ffhRPmzm-sJ9wWqRJgjGxpKez0ji0gMzLr3UrBdRObJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=KebbkqrK75P8SF7PkXrMNGC54wSAls77nIpm9HxZhMs0_GDM3JqAE-U_t0W1IUsA11emzCc6XG3_4zaSc9VF7-prze1Wc3ikzt_eNudZVgM2oYEDwKDz3OrWYeoqmlQD2oGJB3zNMl8zR0gn0aX52bqqweknHaG7scuWakEyVUHBY8oNwtsXeGBOJa-uV4yZ9fBrRz41dI9nbEhT_E3UC875CaKt5bOVMSOPZ6VOpAd-5dtfnKOXy7QUfN9JUs2OiiNd1yOpWvFJoxt2y2iifYZ_HOS7ysbGj-d6oCZjI4ffhRPmzm-sJ9wWqRJgjGxpKez0ji0gMzLr3UrBdRObJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=PRipC0gB8ec0fiPGB_plKDiiKouXt5EVl6kTuh6iFaCArte0gPXdIOHnbqB2lOLoq9SDN0lE11zVC3yreR7PK3PVWudnNa1JNY3hFSbBWI-P9qKU_dWsbnC-6ukGD7j_o4Djhj2k38jeUmL8-JE6ahjlqgFj0KnjJ9-uBPAlPoaK2geUsw5oHBm0gan9aUghdnGHkvRuEZz6CiLhCb3BWNf-V-l27ZUk9Gd3A8BTWNbspuayeqkLxZSPBdYpEIQEXT5N_MbLFjTcEAvPOwYvCiKEPioKxJpkPp5oOROZIeO-ksjzienSOUdkm9-FDpdrzyPB2zMnMKZlZM4L2EwuhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=PRipC0gB8ec0fiPGB_plKDiiKouXt5EVl6kTuh6iFaCArte0gPXdIOHnbqB2lOLoq9SDN0lE11zVC3yreR7PK3PVWudnNa1JNY3hFSbBWI-P9qKU_dWsbnC-6ukGD7j_o4Djhj2k38jeUmL8-JE6ahjlqgFj0KnjJ9-uBPAlPoaK2geUsw5oHBm0gan9aUghdnGHkvRuEZz6CiLhCb3BWNf-V-l27ZUk9Gd3A8BTWNbspuayeqkLxZSPBdYpEIQEXT5N_MbLFjTcEAvPOwYvCiKEPioKxJpkPp5oOROZIeO-ksjzienSOUdkm9-FDpdrzyPB2zMnMKZlZM4L2EwuhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
