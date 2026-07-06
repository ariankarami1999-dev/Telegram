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
<img src="https://cdn4.telesco.pe/file/sjqaU07aHJT9aIsxjjxmbgbBhJdB-Z006c3Zp3ZZgNKvtpaZhAokryx4QHvxAa6PRAPcD8PmnMjyf1ilKG1CyIt5n4Ky8eD3QmoIcswgBypGEgLczJv3vCdYJmv6vhCaBQIfprnkBq0rAoCxtvLyZvDQt2yek-xybhzhNWxbPHchMk3_Vj485bh5RD9g0U4f5VLpTrDwQeLW0fixQYCDUhDiWJ-gxUeVOpaPp56QgvCIYxcZtWUQ9QrHZV7fm8niKkqsHUWUfhFhr1da2dPzsAxGaC7eVh1mtc4X1zWihxlO8w7J7L-uESNrSgMnqOXeVfWtVRJ53mGtbmUTCXlvIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
<hr>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=na5zg8u8kkHa7NEQBy1prPt7vgcJ0Z9WJyxa5gSLhBzikfFjBVoQspiUf2eq-xkPoAphRYQ2yD8CJAenAitZifNLqT2LszQUXR0G69UmyNB9-awOaEukW4i5upGW0J9YKpGyisgrQm8FWlyesphK4hX6Iv430rdjOgMimOr_Yvm7sYJXNldfgGZ6L2dMV1qIadQSDyE2YwrUdIXcNEM15WJBEH8yMn4mWVqI-84ORRgnLOGdIw4B5OhEMDDVbnf1_d_3oOmy2K15W491x7mCoHcXACd96kqzKjjeGEer3j9H9EqFdPQ_rIusW66IbXq6oH-UWiAANexSaAi3C-yWaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=TVCsUOpAhhpInQaVfZZ_BmU3860xf9JFNSN6_3naEQuL12fxTHsk_pzt6K4iwRJ8VPjvNREcCSFXSabXh6TRlluaKyp1tGBfRcEpw4GRhsGfe8GLVLy3FlQqEj7bpSW19RhFw05U_McZHAoZ7bCzd9h_Dh15j6O3Px3Z9d_Qr6FBDDq0-Fh8dPxtLTPWpU8mx835dHZU0B51a3qtaoiHhQyHa4ZKpifBAV5bsSfEREwjIFFr_RiUj_KJAkXoLmWmBIpJPbuxdbDZSt3WQZEKu5Z0uaxKx8y3mZbL2OyRxtL9emQ3nCo2btumyDFl673m6HWzuZQHHbNy4NyMlrGWwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=ZA9ajhrEox7bZEb4rCnp2cM0YeT73gKspDq9nfmhNZt98g7lYMOTpID30gbEnvtrNjDgwayPz7CmaQI9DI-8YYZwuOpdqDLfsRbTHNbisQuh2v2S2K9QHRPTNYmPRnBo6upVI9o7wWLrVz0ABbp4tIvxy1rbFgvyXLgNOH8BA-Ij9_6dUYH6mskFHNsN_YOZE3QzRgIYvWeYgW240fthE-_FGIgz6HQmqkCSGALRwTtDiPwARPkj-HSKJEEU_djEfJcUn2M8d3pO9F9pWH9av53BVfxwyF_JNCB8uqaBp4un-pt15F8NMH1HwDTCwnhg0h9-E5EQ_EH8znP2anbo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQzQGnop9GX1qdTIWkKXxxQCIWPwxN1-va-cHPac1htjzqoSFR8WzAQ756AkhBoJvGcBDZ_avdwbJAv6XwAU3EXzJF_gqTJPLeu2GuZTrBY5AQI8BC4dxuHWIbAqOYkndryKYZ0hCjILIddb_H1082I6xXSb-9QRHbHgU4dmqGXV9QaPD8qBCKKog1-jq5wLf0zTlM_Z2SA7SDLPiF8YLUcrsrowXmPP-8ND36brcsxyZYXN8i-A_892V2x9rG2CSZrP1kwMCozUiphsu_mpYyQghLl9zkwVVLFYJiu-VbiNHPUB-sL5ox871cD3-zA-DhGGT9Fq3zMEBpsTFYT-DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZbRt2l4wrv16uBvYpA7lsz-yhU4k36b7GfIacvb52HuDQZmTQ-2qudGtIpjoumLkTrtG5m3BWo0G5Vxy792Oa_Kkb1W0zzw0KhfmYbIvURHgL5o-FZWIT0GN32GVjd4cYkMdvvd2lJ-Ys3IoVcW4vra3NI2x6_G8Zyp17ajUodix_j0tNdPzBN7D54gdIE97FWJ80qKQQ0wkUSQkXNpHh3-eXcqB5sSS8bWdnz44ugje_sIFWO40Q-ejtZRbh3eK4w0m9TovG9ZQbAshOATF5WLuW_XB8bUNd3ooYhyyZ3Y83tO8nH406gPRuQyGiXxrnKrbzzxv0G5UAIpnPEwpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqhQu3CUW8C0iUQLu-skWjyLHdNKg7coRdwpl9aRyA13pXhOcbabp9aUkGBOSZJoZak07JX2tun10LTYHx1XT38O1dwupS5NvUClimDZEm4RiFdRZfhnvczJN2s-dBMPiJNY5v3VZRmflCHFNC0_FcE8P5qsNEboPA_5XgrE9cRW81bNsiEx46xHhgCijCZ2csXc94v3ZoOiAEGoPCNix0fd3LVrUpYcfi3hOinUIHYNzp5krympWnUBjbVOGgbEvMlzSa2WupYq6c1MgChjYK5wheV9b1vCG9qAE0yY3R_VtOkMWO1aKj1Dju0HBUrclSGBEDePFR_U9UFQgNHlqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این آخرین تلاشمه …
@withyashar
⚠️
یاشار : عرزشی ها اومدن ریکشن فیک زدن رو این پست ، اتفاقاً این کار ارزش این ویدیو رو بیشتر می‌کنه و نشون میده چقدر سوختن</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/withyashar/16542" target="_blank">📅 02:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT8JaqUohsnl4cMC54Zb7bR68dgjsTFmNbMJNFTsELEswqWYaZVTGdQSJ2Tj_fB2TF3bUo7ZnVw6OBvPQiqAvHH3lXaxc4KiZhS08tiOE2f3rs6e7hMzvXNCULOQsCIhPCxnRHTBxE-U70RM9G7Y86mKGZ8L2fyLOST7QUhD1nmNQffH1us7P-0qw7QTaWMBKLVS9d1qKswLzBOOHqQ8_nCWKqnOkib4n1ijiAn5gQlrfi9B74Swo9MzRYpcoo4Eoogv5egoGJbi8Szp2FHVn7C-dkPxbxn-L74Yr3GO4x5Wo27uDfqd6OpTgSBMQ4pEqWMMnvNPT-WIDlG06R2mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواری شبانه روزی نیرو هوایی آمریکا در‌ تکیه تنگه هرمز در غم عظما
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16541" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4s_nfyC49l-PdEmi31ORWN_H206gh3I_WIq8rCnNtE7dp3a8Mj5BpynxgvQF3Tu5816gyKU8bYJteLJsMEhRdkpbfpnXwoRQ1T6WZap6E5AYyaSOWR_m2clModO8EHfuHNPhre3a9kFopHv1DopZAJlmklPgr9BUypm-OvFhGS9jlvrxwOZj96Kj8rB88U9wioUBeXRaOpYjqUbzbOyl8aFS8CG8Nu76O16Ku7rA0EtGBZjM1cDDX5q5lnXWn6Al93cd3A2p-grjyCNHVgjxSWsw0C2EoCeNuubJet4CQqO0jtW4qxIBApisOyiCWSXq34xNzwwWuuY-o4NI6sVrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفلی جدید
😁
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16540" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش ها از آغاز درگیری شدید میان حوثی ها و ارتش یمن تحت حمایت عربستان در جنوب یمن،ده ها کشته از هر دو طرف تا کنون مخابره شده است.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16538" target="_blank">📅 01:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBipYKfDPqmOklbyvviicWxuY1nbWKrXwyS27GkhX7JGBP_1t5DdMIrlxoXDHC71yawirHanGkpofFXTBpFpByhepH0q0ZURg3kuYNKnpZ5DlJnwc2HQpfjsJZhCPCIJD_AF8BxPhsA6hxAxUeLs6xa34a9drmL-05NqOf8nhh0rufkDIJAWZNUGEnT3pnxKZcrx-3oFjXtCxtDKPERyIu2XXXhG2dhWz6je4_LO9y0mSOt7R4DkKc_fXBSOBN2-nU46caoCOG-_j_WpgvKUaSBtnJ9dHDlH0dmjuxicEiy_HFLiUKJvmbf6PIDLRCt26ApP_ciTzqzFs31Gqz9_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از خانواده خودش در سال ۱۹۱۵ (۱۲۹۴) منتشر کرد و نوشت : پدرم، پدربزرگ و مادربزرگم، عمو و عمه‌ام!
@withyashar
یاشار : میخواد بگه ما از قدیم پولدار و با اصل و نسب هستیم</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16537" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhgusyX1GsfRZfYOTXhWJuEofw7UBsEEBM-imYskrWfbhXNbIPL1G5uFzU7sev9tOpYjSA18y1Hf6Y0AVmpTkWJnrHffm5JFqiYr3i7JDJzIGYAm446PteLVrM-qUa3PxY0kPz32mgtPp3YJetficfj5nvxQZaD59Ts1iZRwqsRxXX0WSpnowfESg_EhYoKrdUVPRXwdK7FUGJuKVbsnH33dAihAgjFgwxiEEDw-BULFA7aJPaRpnKhkjUo_qUu_pyHcZ51Q_8bK7bmmqVFkxGgASYsJj3CJJxKb0QtV7GNU7m2aqUk1TIpjTtHMRZAYBohkGQq6AKgppmhrRhwKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهیه غذای «هانی» اسپانسر تشیع موشلی , دسر هم حتما با «میهن» بوده!
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16536" target="_blank">📅 00:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd2TKAoHNnH4UKt-OjOWblIY8xKNzyhygzAJOnJBj43DH5-bshBQc00UBgrvzNf307Jmf1JzlLCT3M_bDtu_FZ-mC0AiZL2lnaslbLXVofrh6-60d9lBQzwKJxEuyrU-GsPwSywY2wwrum9XRjh0oBjUU8lM6bwl3LxykvizuLkE8IORCtVdCew6dlBZw-zeeiEaZq7Xi7T2WrzhCVtlqwx23iehSlgOIUyM_F2G6fxPQaNlVnQzt30zqT0Mae8JJBkeCnqZKx6Cg0JGZk64kNe4gRf7zUycW1x0_sFhElrbhenWJwL_aWRE5POFxTReu53cZpfMB-TjR_aYL9CEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پستانداران انقلاب اسلامی
وضعیت بدنی نیروهای محافظتی امروز در مصلای تهران
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16535" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2OCsQN2M9E5ezr6kDTA7wRtX7vGWc_N0fT7k4M_LL1ZRYR9KvjuEYDIxk4Imjb1jaGONKYaPYW-uBd_5hQQU4iKidesKJyHCxmtiW5t4m6kJDatVRt_K3s0wtNRJ2OejnDDVI7gbw9o9zp8-8J8Y8TBpF1KsDVDF2a6FbxuXejQq-e42ED-Nf-s7oEBNQjjIzYxBhqjUUumTxbUM_HQOwCiHCihl1-bpF_nq_LkHDhZqLqxnYAsVyK33CN2Z8_CIgquhDuuknCYXf5WnSZuxCY4sw_T0UdnTpWQwaC40__PPqc8wvxOuGBw_xpvs-VNlOi4y8c0AqATvlr98ID0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1oLohXX_-5t2dNP-FZMmRAlUJEPecKxTjt7UeLFLUPRbqWy3gZbIVIJicS8md2BKbKaPN4yhEPH_e4JuCT8rgBhZBqQ5F8prkscoHoPfyo1KAkm4BCdqzl_zc27AwR4cqmxyJW3aokHL1JDeDOSqVW-YcFg-gJNn0TB_BptPx70F8pSsPBq4lnHWISptPe14Zm-QbwkGcNqSQFZARmTBgXyGxxvuh38JSBl5tvf9gTRXwhW4pFmjyKiadtcCf2K--odj3AGJOehVMTnSb_Va3e5biBbYBE3gQmz-xIBD9yF29exrLz-T4sFxaHIqCxRrrt0gCAq6R2cF32Ev1m6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxqplsLSn2vPzP4WsU_J4DaXS_NL9zHYVVe2QLsXmvXlBcLUCv1K_tNUI_0hS_-TA4NSuwW0r6VsMu9pVbPSlw2jEXzKyBTECt6AlrZzCpGUFznVVBDuw1mnAz7jXk7hP4pxtirsE0vgvKMK05M_gamvXAwdFN068Dx4i1YkGZWAFzcssWEoK0A0b_M_ZvDc6uZ5LHvvndiq4XCy3m3NP1z0iO-J-OBy4Ccb2ApuVLWW635isXAsxMqljSZWjNvJxpuLXTaBIDdABvXDn4hqQKFnZHl57Ygo3T6J7jMb9jPr8ZUg6XPYW7hPMyRRwPC93diSHB0jz1nU9uRtE8BAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc574weysxnze-y3BGwSFJrxbg8fVJzMBfooWJWjO4IUc_2-cpq4exCUCZFWE8adHI-qHzjnTj7kicvnLG9aozbON68X7Yx9Ch68zBOAv8bV8fdvoi-2pVTBi8WZnOIwvoSHbB1jJdnDAimWKJM1R7lYce5C5b6FA7-9ys-Tx2WJK6oPMDoyCXEbugiGDGVCxbb0ZxMVSP2TvbJBtUpADbDJgAkCsO-Yu-BtVFeG0gN9belrdmKoVHtXiMoGRBuHKW8Kf60h49T6rd9IpBMTiTBeEbmRxl4OXJzSbvSzUv5n55uY7PXGeC--yVOyIDGvBPjOH3OE__I6SDfkEtOjRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=HIML66NCe6Ra2-kNgOgWTA3_cpMnAdQyLzmL-VXBcmLmvpwfFCYf_utVaXrXkwBXBUTfQh_5AIrygiZLbPHl-qto2VDa9CXrEPW1W0En2Eaes0ytVtX1_IFUfqTiSslz_mvqEcTl0Dp9qoybaKQSiZYHXSZ-jWlm0V2ftZc7ZBA5AOcjczdkIRNcpX2fHfWD3C9Vof274mVYr3mjxYQ-Ng0Ho7klb8gEx1p8BiG0hqfCK6AV8oZR6pougXTeUCVZirhRc2zaob97Sw8liN75kuycHo_Aov-IFVVrcG2z10ZN9nMYd4ee7QMWCMOD0GYryk2AT8EvLTetc2djKqX02wUZiFLKJlB-8caq607saIRG3cG0V4zBhdmbb2eLV_RnPrd05ZYT0CVudYujfEoAboVzHE1e4OdscKEasXxfqk_8QL6WOOd9i_Qb2WUXYkmr7dg4JPd_DumrzlgftSeq14VTk-Z_lv5OHfbiH9KjHpHd2keSAQfh6Dhxf0gNEa_KR4jPrsS12ajof-X7zJsuxSghcq0SkkEi8xpgEcBhSGxT6NeGqmcx_JCfX-r78dXooLfmncAM4P3nCKj0N87_FEREqQv7sUwJIsdKmQrfMlepTbg0bNe7JqDQmJXUjrEC6nacDFESrasMQ9wL0b0AHI-bXFxi0fN9Xbxnc_caegM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=HIML66NCe6Ra2-kNgOgWTA3_cpMnAdQyLzmL-VXBcmLmvpwfFCYf_utVaXrXkwBXBUTfQh_5AIrygiZLbPHl-qto2VDa9CXrEPW1W0En2Eaes0ytVtX1_IFUfqTiSslz_mvqEcTl0Dp9qoybaKQSiZYHXSZ-jWlm0V2ftZc7ZBA5AOcjczdkIRNcpX2fHfWD3C9Vof274mVYr3mjxYQ-Ng0Ho7klb8gEx1p8BiG0hqfCK6AV8oZR6pougXTeUCVZirhRc2zaob97Sw8liN75kuycHo_Aov-IFVVrcG2z10ZN9nMYd4ee7QMWCMOD0GYryk2AT8EvLTetc2djKqX02wUZiFLKJlB-8caq607saIRG3cG0V4zBhdmbb2eLV_RnPrd05ZYT0CVudYujfEoAboVzHE1e4OdscKEasXxfqk_8QL6WOOd9i_Qb2WUXYkmr7dg4JPd_DumrzlgftSeq14VTk-Z_lv5OHfbiH9KjHpHd2keSAQfh6Dhxf0gNEa_KR4jPrsS12ajof-X7zJsuxSghcq0SkkEi8xpgEcBhSGxT6NeGqmcx_JCfX-r78dXooLfmncAM4P3nCKj0N87_FEREqQv7sUwJIsdKmQrfMlepTbg0bNe7JqDQmJXUjrEC6nacDFESrasMQ9wL0b0AHI-bXFxi0fN9Xbxnc_caegM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو توی بازی ماینکرفت از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین @withyashar
😂</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16523" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD5KWA-5e7tJlxWw1DKA2uiJoHqkJzEvbeYUAn9ebT71X4I1IxsPUBz4HuYwLRQ9zUy6q8y6wR0acPQNlmKizHapRy64461T5_QR8UnVXVQfNbFg2uI9iI6v38p0136D3soZ8uwUA4sIQSSyTTTz5Wrn6zkGkwzQs7s_V_8KZ1MvsiC3FZ67TsRRz2aMeC9AtMrp_JVsk5aWlUtgzPD5lvGcwXvi-shCqA6aOeVAXXndJL8eam2bvSkF8dAcKSFaHWjcHH00Sv-RgKiseTDYR9OHsil6VXAo41ezrYl2XHEPdSjDLIB7IXS0OleEiMRgqWDxWY7truq2JuSvzxTwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZrtEnYWezT3JNQpF8m5C1MZT8xnLTnxMpQCunfe_yw7yaYRYT7O6F7VCrdUt9iwOJbEMQmx_J6gGo3Cw2dUDqVUU1c6npkZdXmPJprQ0fHcIYKcHQdFnxh2rRLxagQHMEVNzDjFaG3LBhfPOnXJfmP_QrwxscG8LLB65tI1QsrgLCFYxJjIgDU0Puhy173UEBfUPgN86mtd65rnQNHlN3xM6BSP8Aw_qMmLXDfAnkAExVBVRayBk8WIsknmPgtvxO3i2flSDsZRCmb5DcB69uEsb2-mU67L5vFO-zvjWFuooP3ZjXztWOzatyjZSA6z-q2BrJsjE34T6y_7-Znf8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdlLjJq5qk9PGzzFepcU7344wES35Ds7lhZAZ08s94IAHO9oIiCv7OMGjjZXgmPqvvIN7WphPe4id38oxB0i0ufXxrMavD1-7q9MtsO_dUfmJZH_j6cXePNRqodTtKsriLVf_4koX_Rnad1M1FdiH_hcw-Z9pfGdLJwJ-X1gQKEjLit_tCb95_Wrj05A4UeqcyK5kEEomH7Gn3pxOm909c3KY16ULSkagwYAiSPgvwqBkZvyXR7o1XQwBSNvFW1tQbOxI4Ut69Ze0MDKwGwk2EIMpMtgGbZliOwPVJ_FW1iPLj4HvIbDO3lA8fsvOmScxWqmuNo_o-0nSZWRvQSiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKhZvVK1YmQtD6zABcIQytJ7ESXYFywgJRESA8Mxs_EiJpeULP1uXNTM2i_YbbR-lTF9-404fez3renZTZ08pk3WtyWw5b-EJuueu-_kEga1vt3fLqNkvz4ecH3ymBBp_HtYBezVvGGfBqOYBOlp5UyfjUOEhnoeHUyP7WtJqkpv-RAwwNf-lbDOvVMEc_0QB9t-H4QX7NIyPzx8cddD2-MdwjljiQbUDSJGS6HKgW3Gnf5w3nu9s7CYdggQcsaVDds_sZdeTj1ORMzOLbMenrezD-OdcsT_znIpq7qLbPdKU5KqCf_rjLcSJZDKBXDyCjvze9uKrpgrJwQm-iGCUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn6Yubs4rrjZCODAGPHyHA_k3ALUiv-6MAUTuL3VuXOyxPHuVNZl1rWaxqvzTrCNdMTnCBJV_GGsfmBoOZsiqEnr9B9NGriRoPgCgAflfKcCS_UxZL56RVJcz5geHxzDLFMbdwD0lRNlMd4THeq3o0mmrmvrric3t9NFAXlHnRK0S71Iy7pChXOXn6jWRNENlW6MwCDx66ACzaqAdczK4Q439QAYDHgvY1lzj4qMNZaphL2SoCN3zD-IgM44wX_1Pdhe0qfI9F6efcFCMgmho5TRJutTH5j-YOYnUHT7B0OaP5TdHRFXZ4aaAdsXgRSSdFvaSc4zfByI6Ft4ybG9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی با صدور حکمی، غلامحسین محسنی اژه‌ای را بار دیگر به عنوان رئیس قوه قضائیه منصوب کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16511" target="_blank">📅 19:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیروی دریایی آمریکا: عملیات جستجو برای یافتن سرنشین مفقودشده در پی سقوط بالگرد در دریای عرب در یکم ژوئیه متوقف شد.
@withyashar
یاشار : خبر‌ سقوط بالگرد دوم الان فیک نیوز است</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16510" target="_blank">📅 18:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو به شبکه خبری فاکس نیوز:
ایران، چه با توافق و چه بدون آن، هرگز به سلاح هسته‌ای دست نخواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16509" target="_blank">📅 18:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEmuGdXuAKpGzdZFJlJ_MvkYpq3khEJO2WcwYuVH7YZIE9KNXVWVXvckB-D6fHriEoHVlRT8PrnAAgyNHVEinTcMpgMens_Oyjtx_JFW2havqWclqq1qkiOU3GAT5ZKZAgc8xOpNTR3AFXJkERgZc7KTbPKjI9ym7GO47ZsjChXxMMyEms6LKPvXn1w7e372lYveHyQqZOiphPpaY3LW0xZXXkqdTKI-bpksR_8IsbmfOSrLh-3EXQ-jiuSNGohHPXxovKFMleeF48v_hcnIdSaFe5tVNweBYcyMMgmYwfaipoEsbj5k0pZlyWbPFEBxgviHnPvlMnKdDt9XQoJYVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکولن امروز مشاهده شد  به‌همراه یک نفت‌کش پشتیبانی (که در تصویر دیده نمی‌شود) و یک ناوشکن، در مختصات:
22.2521, 60.8321
حدود ۱۰۰ کیلومتر دورتر از سواحل عمان ، در دریای عرب؛ که احتمالاً نشان می‌دهد توافق برای کاهش تنش در عبور از تنگه هرمز با ایران  همچنان پابرجاست.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16508" target="_blank">📅 17:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرگزاری های اسرائیل :امروز ثابت شد که این فرد به اسم ابراهیم ذوالفقاری وجود خارجی نداره و با هوش مصنوعی ساخته شده. چون حتی احمد وحیدی فرمانده سپاه هم توی مراسم حضور داشت ولی خبری از این نبود
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/16507" target="_blank">📅 17:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام
امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد...
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16506" target="_blank">📅 17:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۴ اسرائیل : اطلاعات جدید نشان می‌دهد که نیروی قدس ایران واحد جدیدی به نام «
مختار
» تشکیل داده است که با کارتل‌های مکزیکی و ایرانیان خارج از کشور برای توطئه ترور رئیس جمهور ترامپ و دیگر مقامات آمریکایی همکاری می‌کند.
@withyashar
🚨
😂</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16505" target="_blank">📅 16:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرودگاه بین‌المللی بندرعباس عصر امروز با فرود نخستین پرواز مسافری از مبدأ مشهد، پس از چهار ماه وقفه، رسماً فعالیت دوباره خود را آغاز کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16504" target="_blank">📅 16:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=URMomNKBa5Fkx9f-2ifN8N8bSzWoLZQDFFHVBXeJGwuGXaqpQAt5TVz23RYytwvzlvqLY6lpCl203WEhiO_swfFma1XOcSOSt2L_LrAj3zxzpJYI642WB_KkXsUqmuqWLp3p_rmPSLKFFtniKnKIFYB0-HEOGtQc49xZJxm_kVGcD8zgU6z0iCM6uSaCsw_HjCPB1SDyYHPTxaTkoDaCmDRUf2Ue8Wq_0pgMkyL6FvZPsBXqHClslUjvX3Ad6Od22QT2A340InJcuabBxDY4ZfjKIG0_zSCfzxKl_ojcvVb_5j3y2bBmsW7W76vES9uKfutmMJenlCHF8jx_QDQBpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d4a6d9f34.mp4?token=URMomNKBa5Fkx9f-2ifN8N8bSzWoLZQDFFHVBXeJGwuGXaqpQAt5TVz23RYytwvzlvqLY6lpCl203WEhiO_swfFma1XOcSOSt2L_LrAj3zxzpJYI642WB_KkXsUqmuqWLp3p_rmPSLKFFtniKnKIFYB0-HEOGtQc49xZJxm_kVGcD8zgU6z0iCM6uSaCsw_HjCPB1SDyYHPTxaTkoDaCmDRUf2Ue8Wq_0pgMkyL6FvZPsBXqHClslUjvX3Ad6Od22QT2A340InJcuabBxDY4ZfjKIG0_zSCfzxKl_ojcvVb_5j3y2bBmsW7W76vES9uKfutmMJenlCHF8jx_QDQBpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان حملات سنگین اسرائیل در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16503" target="_blank">📅 16:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=SgeeysbPrLaGaKMDx4lvs5Sf6qY560M_xGZvwnUryL_DE372pP2G2JaLowj1FbbfFGELB3VwSJWyQp4ASpgv9OpqhfM08Fz3FIHBsRYDe-1qZNhSZuKB3cc6eT_Wzy0YYkLCg58CKSiTIPAkQw4k4gvMVRvrbjPC8eUseVYeJTr_-Fl7NEOIa3RCeKkSKP8HPInvo0Wl2p7E-1VHDZyXK_qXsuKVQ__XYd3umD29bl2YTjgbSNyzyj2xYDafRpoXJ7uf4dAR-LXgd_WLGlMa0OrLFtKMhgN-KwwxvAif7zsG4jqIguRDxK8olcoxno3solfANYrm_5OeovdB-JYErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f20cf4d81.mp4?token=SgeeysbPrLaGaKMDx4lvs5Sf6qY560M_xGZvwnUryL_DE372pP2G2JaLowj1FbbfFGELB3VwSJWyQp4ASpgv9OpqhfM08Fz3FIHBsRYDe-1qZNhSZuKB3cc6eT_Wzy0YYkLCg58CKSiTIPAkQw4k4gvMVRvrbjPC8eUseVYeJTr_-Fl7NEOIa3RCeKkSKP8HPInvo0Wl2p7E-1VHDZyXK_qXsuKVQ__XYd3umD29bl2YTjgbSNyzyj2xYDafRpoXJ7uf4dAR-LXgd_WLGlMa0OrLFtKMhgN-KwwxvAif7zsG4jqIguRDxK8olcoxno3solfANYrm_5OeovdB-JYErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/16502" target="_blank">📅 15:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArSUOKPfXTEzp-hsT1Zs1jLqS3PldiojdIZTx_jj5GwV5HNXubnsR5uChKNhJUz39boi7A4j80Q8oXYnAeCXSeVYlRBPSJYhZSIynV1Yk8SoRgrvOf2YnwqBo2VyElnZ9rNRU9GovY2NaQ-8sI5V4aZ_sdITOiwGgGsuxlhw0OYVSvA3yiD6L8zhUyBQb7Yi5Mw_bz2AXcIhnClUVD94UqGFtkDY47icJR_QfIU88XnaEBbIh6-h0ESWHasfailMHURU9DN7xqRoTjvRsh5jojIsAp5dv_bGq9MTtPII9JFFPSqyV1qBfTYwQQBty1jCeQ_PxGQ8Ga2hfzLdu-cM4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست وزارت خارجه اسرائیل به مراسم تشییع علی‌ خامنه‌ای
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16501" target="_blank">📅 15:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWmxDqBh2nE7s1lpDluO4GeSFW8gHY3Lyta0ZE4Q3wwpvdlyVCEOsSMA4kzOnKhEhB5y1CG8zqumP9wfHtEnpIARIrcJCKjN3wvL8z6fZUW6pJh-uH3fZzF9eKeJBdDh9JjTabBgcXucq5BlA4DeA3k5J8bKAAN6yGuYD1ddZ5SGKK6q4uYsfe9zEGJNt9fU2l7c5Xpid9u9OSBWjcExYsXK71oIMMk603OOaOhyBgm9mwPo4vmnWAw5C-fbeTJgs8gecn-5-rDo4c5-JP_eCusCFijv4W_O3_LuQz39AQc3Ot1ZNHsSgmgzMpyYyGOl433axn3j7N9UScdDJPgnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از زمان آغاز جنگ در ایران، بیش از 273 آمریکایی در شیکاگو هدف گلوله قرار گرفته‌اند
😳
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16500" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b892031853.mp4?token=LpYQdj_6ImaugFIlc_y97LyjvP5VHph3fVr6oiLl7Y1i5oRlkQy6MgtEFIaz2VSshK5OrzKItjYKjTw9syUtOIS8gH-7n_8lTZHCtlmXaS9XN1WdyPXuKxOKKeyK0XMSuV2RoYBedy1iNM3VwtkcoLcSPmBO-C-MXV1Yz0iDLJG5Fm5Nf3nf-d7ESg-JyXu7ADZGhNUlZF8xFnZwo_n3IgZ2s6P0ESX6mGjOwrHkOMhcRoIWUaBM09BlRnEaNCL3SRBO1m0f-kKzJ2Haugi0Wh4UlsWydvI7EFdhWcDWs6Dwb2vQrgM-6rr1MHHZx0pieRo8s_HZxEV931ovC79rJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b892031853.mp4?token=LpYQdj_6ImaugFIlc_y97LyjvP5VHph3fVr6oiLl7Y1i5oRlkQy6MgtEFIaz2VSshK5OrzKItjYKjTw9syUtOIS8gH-7n_8lTZHCtlmXaS9XN1WdyPXuKxOKKeyK0XMSuV2RoYBedy1iNM3VwtkcoLcSPmBO-C-MXV1Yz0iDLJG5Fm5Nf3nf-d7ESg-JyXu7ADZGhNUlZF8xFnZwo_n3IgZ2s6P0ESX6mGjOwrHkOMhcRoIWUaBM09BlRnEaNCL3SRBO1m0f-kKzJ2Haugi0Wh4UlsWydvI7EFdhWcDWs6Dwb2vQrgM-6rr1MHHZx0pieRo8s_HZxEV931ovC79rJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خنده های زننده و گرم گرفتن ملعون وحید خزائی با یکی از عوامل مهم کشته شدن ۴۲،۰۰۰ جاوید نام ،  فرمانده کل انتظامی جمهوری اسلامی احمدرضا رادان
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/16499" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو : حرف‌هایی که درباره درخواست ترامپ برای حمله نکردن به تونل‌های لبنان پخش شده
کاملاً دروغه، ترامپ اصلاً چیزی رو به من نگفته
منم چنین درخواستی ازش نکردم و ما تصمیم‌هامون رو بر اساس ملاحظات خودمون می‌گیریم
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16498" target="_blank">📅 14:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEIPJ5tlI4z3-b662owTl69R9_Y-rLTnLr5yHtHloJBZy2SRAEZ3jRBIe6moIpnbblbmiZ6AaaNIs9dy0rNL1ow8GXORCs0mcSwL6sZMmUg9qrbKPA3EK6HgCXQdxu_jCJrqcrAVRw9_YcLY7UK_0SrXhxmCyAOXBr-Ti6b-tM_7rK1saU2bOyXn7GAG4QIcOOcabRCYEfU2seLZ44F9umJFFMMXteXsatp7bzifIHEli_UwyQnWMshRpS_XePd0tq9WS_h7sZRvygN-rHusfGjEb0ulMVer9mLyDOu9UuumoCorM9cRglYz6guM4UU7eRVCo-YTk9uy4CRST47Uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک جت دولتی ایران از مسکو برگشت و هم اکنون بر روی باند فرودگاه مهر آباد تهران به زمین نشست
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16497" target="_blank">📅 14:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdsifw6-wqYB-sVqjEkcB73mRR8BmIXFLXlmKU79F9IV8zpIi8Ov-yTbdRzlrVW7lOWo0rE5KJMgFzvOlbIUsti_tvRczDkKYy1zOm3iokuG0MAY4B8KNMgHtk4fTOfj6Rw1Yi7tQwHYG70vii9fCBfHEHCzyfVQpnsCJ1yaEgjZYYmVOgl2NSLlMvV_POU7m6XqvbM6r-73yBacdFTeTqCvQlGrhwcpVWXs-jEy0X5apSmBNUJqm0FN2Raq82acOVSL1dr-l0Xjw8wCGJh9R1f0TBGqv0iFnpehB_4EDq5LlkSM-OA4TFtT8e6wmN9MXQKGeDfs46OAJiMltHHTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که در ویس دیشب اشاره کردم که منارههای مصلی یکسان نیستند، در این تصویر هوایی هم کاملا مشخص است که ایده طراحی این بنا کاملا از سنگ توالت برداشت شده.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16496" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۴ اسرائیل : احمد وحیدی، فرمانده کل سپاه پاسداران، که تحت تعقیب اینترپل، تحریم‌شده توسط ایالات متحده و در فهرست اهداف اسرائیل است، دوباره در روز دوم تشییع جنازه خامنه‌ای دیده شد.
@withyashar
اتاق جنگ با یاشار : موساد این روزا حسابی سرش شلوغه و لیست جدید ترور‌ رو داره آماده میکنه تا هفته دیگه بی بی برای تایید پیش ترامپ ببره</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16495" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16494" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کان نیوز : در اسرائیل معتقدند وقوع یک درگیری نظامی مجدد با ایران در آینده نزدیک وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16493" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtArVNSQuoB-4j1slNir4phrw6Cxb-dfbEdB1ipO8e3p8MX06cQish-U_sVgu4uDzljMb6_R6H-U6qqD6Q0WRIqvQuNBo3kE4XoA7z10evlMN81hDukUUAnEZ-sPZWOgPNQ5fQftCXDgN1Lx5SMnY7puBUsG9XtKFkkCCY_VyS5lY2T2gAqsUelsorp9M_Z5RVQoOpBv8qaiI6JC7P60mjlIfiCVOK5GKVToexNFQWVPr6xC3ZJH4FQDivmRMt2Rjv2M_eBTgBVh6cGNcg24xtyDtFwu2k9pCwaK9y-uVBhnXMVHL5YFhywtekycYtLBwL5QCshg-uA8dWcKA87DLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت هواپیمای تهاجمی A-10C Thunderbolt II که در خدمت وینگ ۲۳ ارتش آمریکا هستند، از پایگاه هوایی RAF Lakenheath به پایگاه هوایی موفق سلتی در اردن اعزام شده‌اند @withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16492" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن   ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد @withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/16491" target="_blank">📅 12:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvZAiKCGEJmmd53GGjSMCbGYh36p6vWUaL-mSD44teyGstomk9_ktCFiCuYFvdhZaj2eIGHE685rII9hl3gy2Uni3B01yWuWa4esUgrdCi9nbLFZmYfePz7Djw20cmboNC1SXUxi1iLHEWx0gQlxIMMc9D0YCv4iSn6zvx4DXGbissFxHy6TkrfpIzdJTBC5_g9M5nvZEXG-BUiu59-QnCuuW3Dt22wQBVHNBGwp1jSeS7hJcxbV60lgrLOjrXtVy29gGeKN7R7BhUFzeZOXz1xYGwiJufSHMJ39vyIF9l9793oAurlNf8You_qxXEGKc9p3eSizdBGk1jcNCJXvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16490" target="_blank">📅 12:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال 15 اسرائیلی: جلسه فوق‌العاده کابینه سیاسی-امنیتی به روز سه‌شنبه موکول شد. انتظار می‌رود جلسه کوچکتر کابینه امشب برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16489" target="_blank">📅 12:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=Ccaw62AbR5ZIBAUxNv6vBfUtyjrFCD5VH1brW9EHmXzTcGZDYDFpu6P-6bSibeZSXuPLLBbHpfmjv1xnCYbYVYknMeZw_KbYOr_EhcX1H92JPOh0HnCm37lvxbOSCpkrSlevTgfB0Zpp9tbr7vWnYcBeK4RF46odCf05KiBKDZ7YbyT6Oqz-FWEuDQrWVcJMV_8_ykAdOkrk3xGt7pLBlmicN2jwly3vi8ZG1z9filnmsR4DdtmVA5hj0Um7HuZZpKUAZkls-F_10sXVyWB5MCBN-pFNdQTBSSTQEuc4GmoQ1DNjqHQydAX0qLgSTGEfDnXngQkjAlS-9PtEAl8ggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92ffd63b9.mp4?token=Ccaw62AbR5ZIBAUxNv6vBfUtyjrFCD5VH1brW9EHmXzTcGZDYDFpu6P-6bSibeZSXuPLLBbHpfmjv1xnCYbYVYknMeZw_KbYOr_EhcX1H92JPOh0HnCm37lvxbOSCpkrSlevTgfB0Zpp9tbr7vWnYcBeK4RF46odCf05KiBKDZ7YbyT6Oqz-FWEuDQrWVcJMV_8_ykAdOkrk3xGt7pLBlmicN2jwly3vi8ZG1z9filnmsR4DdtmVA5hj0Um7HuZZpKUAZkls-F_10sXVyWB5MCBN-pFNdQTBSSTQEuc4GmoQ1DNjqHQydAX0qLgSTGEfDnXngQkjAlS-9PtEAl8ggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم ویدیویی از حضور احمد وحیدی در تشییع جنازه نشان دادن. به نظر میرسد در صحنه ای که کات میخورد بر‌اثر هجوم و درگیری‌ بادیگارد ها  کلاهش می افتد.
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/16488" target="_blank">📅 12:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارشی درباره یک حادثه تیراندازی در آمریکا
: طبق گزارش شبکه خبری ABC، حداقل هشت نفر، از جمله چهار کودک، در کونی آیلند، ایالت نیویورک، در جریان جشن‌های روز استقلال آمریکا مورد اصابت گلوله قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/16487" target="_blank">📅 12:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/16486" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37255614f1.mp4?token=UBvbVZNp-sqhBq6X-TbOv2Glz5W5fYlXL-fs_ax7x0x_CPXdvrfbr2sQRV4aLE2eN99gmSNkld7g5insjltFTmGbHabAQ_QXaoye3-xFxbuGb8SOd9F_MIGwGYUGAtP0QuDCQzjQntr1JyPqAAI9RtW1PShQd7HT5apCjhPNGjQANRiwWtHwstsR-hOKMJC9ZtbVVR3kN9ypR5cyH7tgaAH9kDKZQ9ouUPTErO8pnVzyg9vVFKNGrYMHOmBQkd2blaz4CnMWoJ6xcSD3QFtJkLLKm2ffWPzYLPkxIQfHMoPtzQxcQGIVz4e_Mawpc6m6j8We6fPFHJm1dZzu5qPA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37255614f1.mp4?token=UBvbVZNp-sqhBq6X-TbOv2Glz5W5fYlXL-fs_ax7x0x_CPXdvrfbr2sQRV4aLE2eN99gmSNkld7g5insjltFTmGbHabAQ_QXaoye3-xFxbuGb8SOd9F_MIGwGYUGAtP0QuDCQzjQntr1JyPqAAI9RtW1PShQd7HT5apCjhPNGjQANRiwWtHwstsR-hOKMJC9ZtbVVR3kN9ypR5cyH7tgaAH9kDKZQ9ouUPTErO8pnVzyg9vVFKNGrYMHOmBQkd2blaz4CnMWoJ6xcSD3QFtJkLLKm2ffWPzYLPkxIQfHMoPtzQxcQGIVz4e_Mawpc6m6j8We6fPFHJm1dZzu5qPA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل : دو فرمانده حماس در حملات  هوایی به غزه کشته شدن
ارتش اسرائیل به عملیات خود برای رفع هرگونه تهدید فوری ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16485" target="_blank">📅 11:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0scI8Au4pKwueVF8ifuUEBTmFWInUjRY0xoB1-krbq_5jDvcCp0QnVBOHKEBFeSOt0t57E4NGJ8T5NYNKIBLNq1Ny0NNwREekxO86ZmMZq86EFH4E9s39xaXtMmbFHT6hJs-XNNMxLpzQxTEprKS9Hu8isKKR7DZ60-_nvZmlVAxGFu-uu3UJwLpgIKYmTPvo6E_vH_bQ7L051hnAfghrRQZ6JtTnBBqcqCumITQS8ldt2kvVEqx5Dx_5L2GbqWo00PzgoIAAUB7HC5XBQ6OHDZIfuMvS-wDsNlOgpCy-x3pKMl08qgfFI3lJgE08YGPYIKcFThjXLYuBU4Yswp3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون با پوشش هوایی و اسکورت سنگین، ارتش ایالات متحده یک کشتی باری (با AIS روشن) را از مسیر عمانی عبور می‌دهد!
این اولین عبور امروز خواهد بود اگر موفقیت آمیز باشد.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16484" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">قایق‌های تندرو سپاه، مسیر عمانی را بستند
هرمزلتر: نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده.
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16483" target="_blank">📅 11:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده. @withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16482" target="_blank">📅 11:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فرمانده نیروی قدس، اسماعیل قاآنی، و فرمانده سپاه پاسداران انقلاب اسلامی، احمد وحیدی، هم امروز در مراسم تشییع جنازه خامنه‌ای حضور داشتند.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/16481" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سخنگوی ارتش ایران: از فرصت آتش‌بس برای تقویت توانایی‌های نظامی خود استفاده می‌کنیم و لحظه‌ای را برای این کار از دست نمی‌دهیم.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/16480" target="_blank">📅 11:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قطر: فعالیت‌های کشتیرانی به‌طور کامل و فوری از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16479" target="_blank">📅 11:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وال استریت ژورنال: ایران، روسیه و کره شمالی، در نحوه تعامل با بازار ارز‌های دیجیتال، ایجاد رمزارز‌های اختصاصی خود و پلتفرم‌های معاملاتی برای دور زدن تحریم‌ها، بسیار پیشرفته‌تر شده‌اند
تهران و مسکو از ارز‌های دیجیتال برای خرید پهپاد و قطعات یدکی تسلیحات استفاده می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16478" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی @withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16477" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نیویورک تایمز: مجتبی خامنه‌ای همچنان در تلاش است تا در تشییع پدرش شرکت کند اما مقامات امنیتی مانع هستند
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/16476" target="_blank">📅 10:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnAezJQtaUpNXpKKbvcmNxuNCkKEiM8VhOcgL_XoW2OmcEh3Ot0DStlIpS9D6jR_y9s5y7CvhswtcCWQaaXrUt1Rt8hsGjbv2sI9nIphddNEul43XMJFdHbhAgND38qMfCu2bkrtvBI93DO5wTdNsMO3oofGD1XAzxRs6H2v4GAQk80eYPggnKW2_xPuv-hzd26KIBu6yhlMthlG3Wwz7w_jm18VijnrQPpFfyat7yIniM_T79iyb7wH58yzqlRIU14mF2dedFqEQKvTjQk8s8OFboiwbfcVdjEP-mAbG_EP3mNT8hSSm_ElDT4ESrmCsCEOgqfzPdhNcZUax8eLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت امام جمعه پاوه ( ماموستا قادری ) با ( هاشمی رفسنجانی ) که دایرکت منو منفجر کرد
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16475" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txc6YMSiligOruBrcE50NJmYrmbZl8HqPnk9YwZh-fCuiFwqPLZPQAEy_mWvem9jJUn6ZmYQQ6AiV8M-AgH88FKimS70H8emihxRLYqDIQIr0TnJ4oqB2xTUYuZWlZDYmB_wsZK1IwTOejX6KUsOJEg2eg5CBIscR0tzMCbDjpsyez8cvvEgQfxlJyaeIQr8ftQk2kx0-t82GS0Qqo_3L5R7ohDQzocrS6Li5pCgH1lyGvr34uNKxqNHOKS4kWFMVBM48A50WRSKY-sjvXgImkmlkLCePbWrRoU_z73CdNq56_UZNxSjvpE7WBsqi2NZ9LdKDs5jQzipouMcjUvIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/16474" target="_blank">📅 10:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=UpcZmSVJ9LxNzTod3Fax0Tpr5jUifuBylDMrJgO6f3npyyqyjtxaUEhi_J0qrQm9TulKDB-PhnkGO9s1KHuo9pyhOQlS9llnbRprD2uvu7zDWmTX02m5GquN41ZUmWTrqLtfVZ64X3LP29E3lc_q6eA15N10_EDnT4LlMD8GuHqctgi9VR1iuOzregNMlviKi47zISZxVqlv_I17ltaB4NgW9Vj_OjtJXRjH1Kf5JCKqSeiuUa6zu0SgN18tKQIMvmw916F-rGevdHMHqWYwIuLB_RhSRUmdCGBolN5suh008cfai3ZS-00-E5bNKdmhhwSJ_Pv_6AH2zTg77inU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a3ad1b.mp4?token=UpcZmSVJ9LxNzTod3Fax0Tpr5jUifuBylDMrJgO6f3npyyqyjtxaUEhi_J0qrQm9TulKDB-PhnkGO9s1KHuo9pyhOQlS9llnbRprD2uvu7zDWmTX02m5GquN41ZUmWTrqLtfVZ64X3LP29E3lc_q6eA15N10_EDnT4LlMD8GuHqctgi9VR1iuOzregNMlviKi47zISZxVqlv_I17ltaB4NgW9Vj_OjtJXRjH1Kf5JCKqSeiuUa6zu0SgN18tKQIMvmw916F-rGevdHMHqWYwIuLB_RhSRUmdCGBolN5suh008cfai3ZS-00-E5bNKdmhhwSJ_Pv_6AH2zTg77inU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های پسران خامنه ای بجز مجتبی
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16473" target="_blank">📅 10:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین. مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است! @withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16472" target="_blank">📅 10:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=qbdJuDg61qe9qHqR7bfC9sQCHeNVXe8KEWxuR78woWRUU46Z76n7kue91T742MYTAhK3UKJTCZaOhr2-xAXKNHLhdrwIbUGPmJKOLOsj8m9DL66eq3dbPWGKqAdXsQaSnNLirn9m5Yiq7LwRb0Ox0f9FbmQdgY5ydsCt5keqE04xI6hePyguuz8uUGNT8izaavMpawr2lEPnd7xId1H0Lm7TuKkEg_qSU--qCW6Ja9I-ilGF3jnQbHTPAnW1Ic_TPbnkbDN15QM-yyOt33xUQMN2Y-cOamYiclHmy0V7kucb4nUKO8nC9MHgOaTvoc9Bh3RoY8X2Bs4St_VVG1kO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c290e0d.mp4?token=qbdJuDg61qe9qHqR7bfC9sQCHeNVXe8KEWxuR78woWRUU46Z76n7kue91T742MYTAhK3UKJTCZaOhr2-xAXKNHLhdrwIbUGPmJKOLOsj8m9DL66eq3dbPWGKqAdXsQaSnNLirn9m5Yiq7LwRb0Ox0f9FbmQdgY5ydsCt5keqE04xI6hePyguuz8uUGNT8izaavMpawr2lEPnd7xId1H0Lm7TuKkEg_qSU--qCW6Ja9I-ilGF3jnQbHTPAnW1Ic_TPbnkbDN15QM-yyOt33xUQMN2Y-cOamYiclHmy0V7kucb4nUKO8nC9MHgOaTvoc9Bh3RoY8X2Bs4St_VVG1kO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور مصطفی،میثم و مسعود خامنه‌ای ، فرزندان موشعلی ، پس از ماه‌ها دوری از رسانه‌ها  در جلوی دوربین.
مجتبی خامنه‌ای دیگر فرزند رهبر پیشین و هم اینک ،  رهبر کنونی جمهوری اسلامی ایران همچنان در رسانه‌ها دیده نشده است!
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/16471" target="_blank">📅 10:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16468">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJN3NFZ6sJ7NpR4ne4CCIwZJTKR4g9fqbCZBLzY4mDqb--Uw17tIZfAVAdDh0P4OVduFexHKcBQIuxw5QfECEOHLIrC2r7HcUjvSrgMnuy5eASMonSxWJX3NIT7NFl9eYK_vzRBFtQk5MkRE0NF4FKMbqhXoyZjvEC_6oQwaOQiOFqu4g6gL0XZT8S6m6m43igbg27makH0EhzBXJ9pMZhYCAxJF6rCZwTMbwPD8KD7Sfx5UddTgZFuj3AJ8mDwGtTsmRGaw3gRHXxN5jaWB44Pg0Sb8T1JHLPhZlrVH620V7Sc0o8jYUrqGkJO5KYqRoVgvLJq-n85Hj6VTrUq_Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGYReSg_D1aw7U3BL6AV0bpLGCmvWhLKfseCMWQoCpWUeQuW7vOdlh_fxblnAZV4ZsjuI7dkvNI6M8h14KQKusf7UgI-EcAPHNqCBPTAmKatjxmz6ssB3fcbe80EbivY6Swva_kLPD5QGIDaIx83m2sRYrJTBu8m2pVNnf3bKYsEUBVWsj_pmRvroCoa9ORzap_N3InI90R54C_tz0XP7jDNSbduL1OtkpN7ZO7_TLvsN_z7UAChQAhIcEnl1-SDaFMIldkxY8HtMXmhAwGGLJQ_pKjtFXEAwccd7Z483iZ3kmG3OUYFGoinsiyJ1o7DaROwdIou9CuGSHa4KL9tCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hQuov0x1-IRFdfsA1sn8do44cYScmn3EM27uYvuOybX1v8110MlbTELSpUTIf1F6RPe6_c8sZhv6lNTViim6Y4cjjJwTiZPYOkdR-5WqhPt8r6rI-xHma0MqGm_iu1hcTv6n5UQUGb8KWDbtrEOukCb82AJc_kWVLU5Qwl80lEKkx1CJfKM59mvSuN5LedAyn5gPEv17AHNf0rH-gxWr6myZkqiBgbWfWhS2NdLlmKuc5gPYPMqaChiX8F0Z2ow7OtwTKcU2Gpo_piMgoe68VO5W1yiIwK_3DC7s-gEdMFf0U6EHP4pvBuxeZYI0tETN9jzI3fBOfGgDSQZtjEnAkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهستان پهلوی (ویس قبل رو گوش کنید)
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16468" target="_blank">📅 00:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16467">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شَهِستان پهلوی، نام یک مجموعه بزرگ شهری در زمین‌های منطقه عباس‌آباد تهران بود که اجرای آن در سال ۱۳۵۴ در زمان محمدرضا پهلوی شروع شد ولی در طرح آمایش سرزمین ۱۳۵۴ ستیران آرمان‌گرایانه اما ناپایدار و مخاطره‌آمیز برای توسعه کشور و شهر تهران قلمداد شد و با وقوع انقلاب ۱۳۵۷ ایران هیچ‌گاه بطور کامل اجرایی نشد. بخشی از این طرح احداث یک برج مخابراتی مانند برج میلاد امروزی بود
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16467" target="_blank">📅 00:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16466">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارشهایی از فعالیت پدافند پرند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16466" target="_blank">📅 00:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16465">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کانال 15 تلویزیون اسرائیل: در‌تماس‌ امروز دونالد ترامپ از بنیامین نتانیاهو خواست اوضاع لبنان را متشنج نکند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16465" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16464">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ارسالی : یاشار جان درود
داداش همین الان از اطراف مصلا برگشتم ، تمام حجم ترافیک و شلوغی برای صف های ایستگاه صلواتی ها و مفت خوری ها بود
یجا مردم بخاطر یدونه تخم مرغ آبپز و یدونه لواش داشتن همدیگرو میزدن همشونم طرفدار اینا
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16464" target="_blank">📅 23:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16463">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اکونومیست: جنگ بعدی خاورمیانه بین اسرائیل و ترکیه است
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16463" target="_blank">📅 22:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16462">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ در تروث : اروپا دارد یاد می‌گیرد که وقتی مجرمان جهان سومی را در خود جای می‌دهد، خودش تبدیل به یک کشور جهان سومی می‌شود. این اتفاق خیلی سریع می‌افتد، فقط در یک چشم به هم زدن. من درست به موقع انتخاب شدم!!!
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16462" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16461">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فردا عصر کابینه امنیتی اسرائیل یک نشست
ویژه برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16461" target="_blank">📅 22:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16460">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رئیس‌جمهور عراق:
عراق نه با ایران در برابر آمریکا متحد است نه با آمریکا در برابر ایران
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16460" target="_blank">📅 21:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16459">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو ۲۵۰ سالگی استقلال آمریکا را به ترامپ تبریک گفت و گفت:
«ممکن است ما در قاره‌های مختلف زندگی کنیم، اما به دلیل سرنوشت مشترکمان، به شدت به هم متصل هستیم. آمریکا بزرگترین نیروی آزادی‌خواهی بوده است که جهان مدرن به خود دیده است. اسرائیل مفتخر است که در کنار آن بایستد. زیرا اتحاد ما نه تنها بر اساس منافع مشترک، بلکه بر اساس ارزش‌های مشترک بنا شده است. امروز، این ارزش‌ها مورد حمله قرار گرفته‌اند. مستبدانی که با آنها روبرو هستیم، شعار مرگ بر آمریکا، مرگ بر اسرائیل سر می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16459" target="_blank">📅 21:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16458">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Bitcoin +63,100
🆙
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/16458" target="_blank">📅 21:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش انفجار شدید در سلیمانیه عراق
@withyashar
🚨</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16457" target="_blank">📅 20:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">العربیه : ارتش اسرائیل شنبه 13 تیر با انجام چهار عملیات جداگانه، اقدام به تخریب گسترده خانه‌ها و مجتمع‌های مسکونی در مناطق شرقی و شمال شرقی شهر خان‌یونس کرد.
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16456" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16455">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده  - ممکنه همین هفتهٔ آینده این دیدار انجام بشه @withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16455" target="_blank">📅 20:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16454">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ به آکسیوس : ایرانی‌ها برای امضای توافق تقلا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/16454" target="_blank">📅 20:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ به آکسیوس : نتانیاهو خودش درخواست دیدار با کاخ سفید رو داده
- ممکنه همین هفتهٔ آینده این دیدار انجام بشه
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16453" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ به اکسیوس : "از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند."
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16452" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ به آکسیوس : هیچ یک از طرفین در طول مراسم تشییع خامنه‌ای، به سمت دیگری شلیک نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16451" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ به آکسیوس:«همه آن‌ها آنجا هستند. یک گلوله می‌توانیم همه آن‌ها را از بین ببریم ، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16450" target="_blank">📅 20:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الحدث: دور جدیدی از مذاکرات بین آمریکا و ایران در پاکستان، در تاریخ ۱۱ جولای برگزار خواهد شد @withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/16449" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZJMPQvwI3c5ZgpQbf0z0Is3DsUeU32BKJK-ELwjBjDA6_WO-WZAr3lFQ1os3FR9Os_wEHSJLNigxCFNcCwlNdiPrs_xxfic9H4ZUmEEv_11ll9pzjRrvSNQV-j-1dNqO16A3sgkkXjWSJZxVqQytmC1nxmMSoFUE6slxQODM8h3KD3k9z3Jz5VFqSGqOPhAUNi1ESd4FnTm0P0n4dB0B-Od0e4pBxHoxV0PDfWc5wk-pi_nAA4-xOvWk3Mi5u5A6dEm4VBTqelCW8OLwWpfk6uUaKC-sCkYVXLGStzVyeqRn651x-3PxLhGTSQTgd8T633AK4XeYiYnVQb9zdaBgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای…..
@withyashar
😂</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16448" target="_blank">📅 20:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYBp5ykoXMaMY7x83HQVIXEP39W_YOWfh8bpwYBXcmgM3QZ96jcbvrtxGsvlrGAH8xq4C5NUaut2pIs4BMgNt89vat5JAjWlXN3hs04tauumvtbZvWNqB17khTjPH_Kpd1-Xfjzj__lx1nlc7FOw-8EEGt9duNTJ3iLwJEAEpkjMg7lzNiBOrxeROdnB77dr4AurShpTMhYoIEntKG2pHcD9o_aQxli-zOCTq8p-dJVAka1ZgeUbwgyJ0RpAEhE-xOzI2uzWatnXYWnKNAcFBw81_xG7_pITwSD3MvMYkd73Z2EuFbYxv8RgEhELh-g9N5C6q6uGzLEXmBZu9jPbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جهانی علی خامنه ای
بیشترین فاصله زمان مرگ تا زمان خاکسپاری رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که علی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ ثبت کرد
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/16447" target="_blank">📅 19:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است. از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد…</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16446" target="_blank">📅 18:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سنتکام : یک فروند هواپیمای HC-130J Combat King II نیروی هوایی ایالات متحده، سوخت چندین هواپیمای تهاجمی A-10C را تأمین می‌کند. سوخت‌گیری هوایی به هواپیماها اجازه می‌دهد تا برای مدت زمان طولانی‌تری به عملیات خود ادامه دهند. @withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/16445" target="_blank">📅 18:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIxAUz_pDwHDai0XSWII1uzzNlDYJi_izkRtqCSh8yKGUsoNhVfr3sdRdBPMXXCH2M-lc0y0ZTBxBLZsPsPXzVLAoTpYSF-slg6qT_gI-0bvmCV8o-oHQKXN2QywNa7OitM3tIKKskie0Gs2X-SnwKZGlyXnsMa7c14XkIRCqxgIaCnqdRbaWxfBjWAuFq_I57IX9H7-du-mxBIch-oBeq-C6EKWZbLaDKPKsg-voBYzSuyL-YUv-0QNEP42yOZ0va4ppa8f5zZ_RtTBQcTwvYam_ixPk0tKT4IzSR8JuBtrnAJquceHl2xuKB65N3R8XYaD6z9WB_dJ1ib2v6F5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشریه نظامی «میلیتاری واچ» نوشت: کارخانه هواپیماسازی کومسومولسک-نا-آمور روسیه
تولید ۲۰ فروند جنگنده سوخو-۳۵ سفارش داده‌شده توسط نیروی هوایی ایران را به پایان رسانده است.
وزارت دفاع ایران در حال حاضر هزینه نگهداری و پشتیبانی این جنگنده‌ها را در داخل روسیه پرداخت می‌کند تا پیش از انتقال به ایران، در روسیه نگهداری شوند
احتمال دارد نخستین سوخو-۳۵ها از پایان سال ۲۰۲۶ وارد ایران شوند؛ آسیب‌دیدگی زیرساخت‌های پایگاه هوایی همدان یکی از عوامل اصلی تأخیر در انتقال است.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16444" target="_blank">📅 18:08 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
