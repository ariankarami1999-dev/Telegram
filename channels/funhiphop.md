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
<img src="https://cdn4.telesco.pe/file/nbbBaaOK-_Xcv8Fwpww0mLzgRB8IVc7fE-SLb-TwzHtdOh-G_vxkmb0Gqe5A2UEzUXc7dKONVJ_WpudzduCChle0oMQXEIYlmUr2Zzu8Qh8Tr9AzD8bJwfkLBnnWaNh45goOb_sQS1JWhY1LMs8-cONHZD1objzBvr95vz4drhLifCZrw9SDsH3R5zx0LbfeNt2WdBNB4u7ct0U6RWQNLBQDm2joimOS3nkK87CSW0oeCpddZd9F8ItsztI7qzvn37EHp6pLsKC73Vc1N0bigSa6mezxVIilic4N7pZm_m7CMeaT94GvFhhyAmdA36ENUlvminILR7SnltU7vs212w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 176K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-76898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5lO7jQq_iO9Q4ZpJ6KTTL9upOsF-NAu_rZRWpFWjjoD5NXtTQ2y5XMSkuQpeeGnfroMegkKXzReaQVJRptwBQ-ejN47XtKFOhxylyXe9QiKckCz-mxs25lFkr0ipirP7M_duSzrfpNpP-dyU7Mf7E01hzKgJgxZ_A8Th5nDY9PayA5qzo6VE9SV_hsO564E0QdBO7GY98IsSz2S0EqMbN0HfX2dfPfyyV_2kFVOVOahXKDGtU68j-ZUw0KJUz8jSNLC9NRcibdORsDkV7UqfkHOuYOizB7KOh_vc4KcR96bpLzVu_5Wmf1y49JcvyHdyUa1yZRFiitvYP_LGOnAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید ملکه جدید فرانسه بزودی قراره گلشیفته فراهانی بازیگر ایرانی بشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/funhiphop/76898" target="_blank">📅 15:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/funhiphop/76897" target="_blank">📅 14:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUmPXyAk7XI5Vmfo1q9I7VfIJ6l3IlQG_Xqw8xWVlReCzJGj8hQhKkOsJ26Yz7pc0uXTp9ZPdWNbIhRK5TRtZ_UVrg4r3MBN7bVHzKxaawvZB1zIRniKN9v2R7pZ6wo-pSApzB8xd44mhClIy5ZA6gOz8CSVJy4tK6Y5t95rXjBmH2MrPP5793GoErhuBeHkcTp04xxIeQLy-SU-SAo86TMrPtkRMEHVpTswsbSX5WfWV_XdJMkMtkmfJhzlFZ0BRH7ULk0HmwVPZ1-wDotdHleOS3_CF2SHaMyeoYv6gFGL_vISrlkW7-lTHvdokzzUzg6xSNSqtRxEkVfgmvYTvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ برا جام جهانی عجب حرکت خفنی زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/76896" target="_blank">📅 14:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نزدن رعد و برقه نترسید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/76895" target="_blank">📅 14:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76894">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اسرائیل جنایتکار حملات خودش رو به جنوب لبنان دوباره آغاز کرده، خواسته این مردم حمله به صهیونیست های کثیف و حمایت از برادران لبنانی ماست، لطفا بزنید، لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/76894" target="_blank">📅 14:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76893">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وای اگر قالیشاه حکم جهادم دهد.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/funhiphop/76893" target="_blank">📅 13:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76892">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-U4ZfRm68pC6ZdN7Hazm45ypBvJAHXyPkl3xggf_rw0GbrHIfkkXrl-cIbVI7dTB5akcT0mtnewdZCxhnYunHbh-gYaVcfEfCtXC8Rrq-jlI_HR_6iqPzvIgAYmf-LXKJJbqvooVlvma5_vS_wdDnIQ7uAV1Br-Zvn8zWPQlrxMF_4TqQcAYu83DptKvPePaLip3_bd9XG9LK0pwW0BR9cPcuEHYG7xNenXKEqdQe_X7zZxzu7cMNLSl4KIa22U9yWcRxI8JcXqYP62U7bgb37ZGrEVwAdPFiB1GuMs8sXKAtBbGmiPQoK89sPmx1_8ztOid-7iO6z1cmmoHwF9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/funhiphop/76892" target="_blank">📅 13:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76891">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مرکز ملی فضای مجازی:
طبق بررسی های فنی و ارزیابی‌ های عملیاتی که انجام دادیم، قطع اینترنت الکی بوده همچین تاثیر معناداری روی خنثی‌ سازی حملات سایبری پیشرفته نداشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/76891" target="_blank">📅 13:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76890">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=G5qwebDaz34cK0wQwS50t0gScbTIv0uYBPmFAZKFb6OzWhrxJy9CDcShU4fy0Hm60Kz6G-7jwMFUgPXV75lyeBbQodqcJnmVQU4NqRxnByaPs2wVwifG25mQGBk59i7FI15T9ASCO95kC9HsrgV6dVZCzCTK9tsPLlxhkFBW87Vv3Zeph5cxMpqPUHw6n9pX5kyXaseK35kaAhU_J_4VflRyfbUeFNoSBvGMwoadkGQ64ziXnU-osMXXg3vzPPmmiEkI5Ka1xbM0wTYa5atTaBJnvQkXCdeSHnDIiQJ7xpbm61hWg62FE0WGjtyFuLEiEUWLLd4oN1tV5NQERFdyTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4cedd5da.mp4?token=G5qwebDaz34cK0wQwS50t0gScbTIv0uYBPmFAZKFb6OzWhrxJy9CDcShU4fy0Hm60Kz6G-7jwMFUgPXV75lyeBbQodqcJnmVQU4NqRxnByaPs2wVwifG25mQGBk59i7FI15T9ASCO95kC9HsrgV6dVZCzCTK9tsPLlxhkFBW87Vv3Zeph5cxMpqPUHw6n9pX5kyXaseK35kaAhU_J_4VflRyfbUeFNoSBvGMwoadkGQ64ziXnU-osMXXg3vzPPmmiEkI5Ka1xbM0wTYa5atTaBJnvQkXCdeSHnDIiQJ7xpbm61hWg62FE0WGjtyFuLEiEUWLLd4oN1tV5NQERFdyTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه اوه جنگ داخلی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/76890" target="_blank">📅 13:17 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76889">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تون 1.5 دلار شد
Make Pavel Mom Great Again
#MPMGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/76889" target="_blank">📅 12:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76888">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تو هند 4 تا دختر یه پسرو دزدیدن بردن بهش تجاوز کردن.
پسره الان رفته برا باکرگیش شکایت کرده.
دخترا هم دستگیر شدن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76888" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76887">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ممه های دوسدختر صادن کو</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76887" target="_blank">📅 11:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76886">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhFlm_V-JzAmdYGZD_rMwF4ojPDhgaBHeV27J_U9gJ5JMW3iZh-C60vGFpkbsWD2ryU86p5ams6uPEchwrJJ3qkIk905-5VMCvbetjvGwo3HoZ73c5ykcpoINUXW-6hXBD9WnyeQVRI6R-RMoenpgn22Om4YQsKs7xBbew8bLkeQgjh1hcNEYtpCFcS7fc0Rpjlsk2cVW8QM2RLC6BZ-Fo-Mhmvr14RsaLuIah23LMlHnDsB9AOOQlrYR9CBuMQACASG7AIH4AI-y-K-amI-ucIMBE_AuIQLeaVS3xzaQbxGEOMXoq03YIA6pt5wHI4pDbIGq3pI7ogaYF_1JwU_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چالش حدس پا.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76886" target="_blank">📅 11:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76884">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3rjGyimQlhK0fNNs9NmcHaSITvYMrfcd34U1C-7mq_g_VZTetlRRjVBuKj6eIbqlSVhoiDYunCCScSgGyJFsUfOtX2_noIbhjRawvItrtBGtwcKZVS3fw859v95NOlKYvb30hthpy9ACKKAWic6GBypWX_n5z4V2eGlEgSHym2r6EediqyztaJ7kM42E2X5LTMPUAeUGyPt9L-G6jxXVcj4ITWlxtFEsanwfTroM1Y6QR3xLkxU68ijnvQyTbW4hKxvwjSNaS1OISMr8lTGGo2OzjV5ZKt_zpC3cTz7WJGkmq0qPlA9BreTKDnajFJ4cD-DsmWyHqHleLWrnuSCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون سوال شده باشه که کنعانی زادگان چرا انقد مادرج چیز یعنی موفق و بازیکن خوبیه، باید خدمتتون عرض کنم مربی خوب داشتن تمام ماجراس.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76884" target="_blank">📅 10:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76883">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbvqzce0SDSQu6WH3IT0tlkoHrCJgZqE-sUrg5CCTWJmtBrUw4BH7eAW9BvakLfmkd4Y5zWM7Rc0DHMQbgZQMBd2Uhnf_sGyWNUaV87RzAuGVVAjcoqoWyhGtg2sKKQOfvkqnSrLHsAci4cV7oKY9xcToXv90fHbiVkppblwYafWEfWbtDJEoelFqsoG4-GpD6sOWLAk0de4mdctkrk9W3ca0PXlIPVWAxayYhnyY6jI5ocVIHlbX-CxC_uv1CzOnmUgAmlReC-co37YZvR2mCOPrxs2GC1wgrW8XzvpgeFc9rLw-Sd8kGu9__Mizzt-JMbwRooZlT5yZXkb1l5yLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفیق حسین رحمتی بودن مزایای خودشو هم داره
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76883" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76882">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxaNAjqv85y0EjULkD6v5YdmPIGNCN64kl_kTsIsszHCEPFZ-pvPnAoiFwRKPAMb-SSfsJL8zPjteLgSjb8OGD0ZAgf7QWivCHFqZffvg49zY9uGSiUf5zHHe4imi7qJV36H5cjRlsFlWNPwFQbp5WGMdG7XRvOpfrGzVVHypVMQKqrM3B9NF9ThiSaC_Xp5C5WwUhki14lMqNVNdkNm6oHSu6Fek_HbcMlmMAZfXuldND8Vnpdeb3XXoQGUdAmwvHiq_SgdA0aYea5p2GYinWBGKNJjHSO2l7b-Y1gvOYIWRYmRZV2hOdA5ddelTRNKNexbKZeV4im17Yc1GwEXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇨🇱
شیلی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
شنبه ساعت ۲۱:۱۵
🏟
ورزشگاه ملی لیسبون
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
شیلی در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳.۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر شیلی
۲
.
۵
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: نتیجه مسابقه: پرتغال - ضریب:
۱.۲۰
🧠
پیش‌بینی آگاهانه، تمرین شناخت خود است.
👍
ورود به سایت با فیلترشکن
R15
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76882" target="_blank">📅 09:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76881">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ولی همیشه داغه نفس اژدها  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76881" target="_blank">📅 09:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76880">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXOcZn4rkXmRdmkUoP1XnVvEGAMyc4e6w9WiObPDQlz9XnBAiUpkv9YcZn_H3Mug4XLkrUVW9f-WIo3s2Dd7YAa1GmD9Nb9EJGuBZdFAjnSlHdKZm7pLQuLSzK93Ej6yRiRU6nBBEHkJ94b3HJMSjiGOCN3KckVw5K26knqUY6AAnjKznxvarWVohH473-J_ymo1PAIsNaX-wjhVfOAsDw1F3jPJCCcxW6OxSed07QU9z344kPDoaPdigPlgtc5nAKi7YC08PYS6jtGPB_ZiPGJgow9gUysapK8I0jP3i8gURpmmvyqMOSpGdleXhx_xw3r3jVpEcsjWyOy0e7SJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی همیشه داغه نفس اژدها
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76880" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76879">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4rVkGLIIwh7yphtqSLZp-j4hzgBVyZpQ0YyOuNcem1VPZ7DG9tEVrYVAzo7Gph3qFFUEsB7n8tiWbNuQdzCyA7czh7PChDjMHqk-HeUN_j-XZhbd7N3NNZk0QSqzKNm5DpcC6c2f-ArqPGOzTOxW4BROdQageMQ8MKCaaJGolbdLcY2y4jBpH7swFUtm3eC0yLC5fm10U1sYs3t4x16vAo5Chqyt2bzL7nIkSniUaVU51jOekLs1M7xhn02Pdfyr9F9W7lxJL4ZxNW3spFuvY-hny0wHxEMQhxoBzi-crNfxUraw5CHqlu-aqB7HjiwWBWhqTfU3yeVPqz5dP9rMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبی که با آلبوم جدید Blok3 شروع شه تا شب باید بخوابی سرجات افسردگی بکشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76879" target="_blank">📅 08:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لری جانسون افسر سابق سیا و تحلیلگر امنیتی مدعی شده از یک منبع آگاه اطلاعاتی دریافت کرده که نشان می‌دهد ایران به کلاهک هسته‌ای دست یافته است!
به گفته او و پپه اسکوبار، پس از حملات اخیر آمریکا به قشم و بندرعباس، شورای عالی امنیت ملی ایران تصمیم به فعال‌سازی «بازدارندگی نهایی» گرفته است.
ایران از طریق نخست‌وزیر پاکستان یک اولتیماتوم سه‌مرحله‌ای به آمریکا ارسال کرده که مرحله سوم آن، انفجار یک کلاهک هسته‌ای در خاک ایران برای اثبات توان هسته‌ای کشور است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76876" target="_blank">📅 02:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HedsQBAn7G5zs-z1zxiqvs-Pxsim7slPEV2DM5W7neJGrcBfUBqpZa64bpwq67VwBEsj5hZCA-VfScUqoG4xLE_NY2cg5BcD1ELON_SpFkmTxpEw5egpZqAJfsnxq9DjZwCcWiv_gevgaXhPF-TQPEn0OmIgrUcyz6Q6-IY6651CQCSuFo1bZW92ZxTaGxU9Z0zmHKAQj0efrDCj72a8l17JuXFD1izDuK3SY0cK2SU7-0pfKb4uwzPmuqP5WGK9qc6lTBnxPW-f_TKhWzJc1pk8Ahks5gRAA2TKKw1X6dJRuquEry4MnkGrm_6zUpEuhxqD9OhbaKOvSjLK4LqDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفعه‌ی قبلی که این اتاق جنگ اسرائیل از این دلقک بازیا درآورد فرداش ترامپ
پست گذاشت
که همه‌چی آماده بود می‌خواستم فردا حمله کنما ولی ببخشید لب‌های عاصم منیر مهم تره.
الان باز اتاق جنگ اسرائیل دلقک بازیش گل کرده و خواهیم دید این دفعه چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76875" target="_blank">📅 02:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">برای بیانیه نیاز به اشتراک Plus دارید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76874" target="_blank">📅 01:59 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۲۵ بهمن ۱۴۰۴  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76873" target="_blank">📅 01:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76872">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artists: Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title: FIFA WORLD CUP 2026  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76872" target="_blank">📅 01:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76871">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m88sZ5U-BUkzxeXGqAuDRTCkv_BV1HlgmQneBO74USEb0Uf8tY5WT-dxn6TtLKtL6Ns-SsUPPQft4l4yeeuE_eTYH5XCAy6v3Ac3QVvGBQKgNhZJZ446j6gIuAQYxPJ2LS9DKHoEQowMAEUWhjiI3sO3y-lsQQ_XIch53PlaVQsmhpD0sADNVL5g6Eyipg6POeW_nnNfMbnEdgoDuO4A77uI_8PMcelNzkb9vVTaFitx_WQinLR-NzQ6O-Xu25DyVbu1bNtnUsNYFBljXQA_BcGXY9fh0zqL6eKk8mwQ1ogwziFDi6GNfZHgMSO5tlg_UJEO7WBcNyqZlWzJdDh7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artists:
Future, Shakira, Tyla, IShowspeed, 21 Savage, French Montana, The rolling stones, Lisa & …
📋
Title:
FIFA WORLD CUP 2026
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76871" target="_blank">📅 01:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu0kPQJqlXlVMMOlp_WCy-beCCR-dochU_6kl5EHTk4IEHrMQZy51aAYG5p6R2NMwRCrp-6MLvhTt6_NeuT-4DH7jREmSs9hjKNaJKDeOhmcGnEmOC7n0jsgSuoWUUXcfrTDjdngnUOswbkX8RJthfGun0glfay93HsKTOgmMFrrs1HZK9_hY_2v-0qfHmbUQKZ2RIK2VZgLCTX_0-dJ7NxR-l4J00WrsOmJP1JxV7Q5e8kmdclipQtCmJbzyi4MkKFx7Y4fSVrCoxh-n4ExjFwhS8UnJ7p67Xhx0ftgT_-kcNnqEw8Z8UjNazm2WJhu_76STJJLQcdhfPKG9KcXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم. خبرنگار: شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟ ترامپ:  خب من…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76870" target="_blank">📅 01:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76869" target="_blank">📅 00:22 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ:
من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم و در این دیدار من محترمانه رفتار می‌کردم.
خبرنگار:
شما پدر، همسر و فرزند مجتبی خامنه‌ای را کشتید، چگونه می‌خواهید با او کنار بیایید؟
ترامپ:
خب من قطعا فرد مورد علاقه او نیستم، اما احتمالاً او یک فرد حرفه‌ای است و آداب حرفه‌ای رفتار کردن را می‌داند.
او در برخی محافل شهرت بسیار خوبی دارد، در واقع.
برخی افراد درباره‌اش بد می‌گویند، اما خیلی‌ها درباره من هم بد می‌گویند که نادرست است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76868" target="_blank">📅 00:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: جنگ را یا از طریق مذاکره با ایران یا از راه دیگر پیروز خواهیم شد، اما قطعا پیروز خواهیم شد
ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76867" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7Z7D9wj3v8ew9OJVNrzBsEyXYXS78Q4CkLR8mtaVkywdX7EzPZoHQjy9-2JBNB-ejBDsgk4kDAOCTiRrXiF_R7fMob4R6um0zgzFL89ahZkqk0BP7qQxRwHOKdL9zOg5dERusFvJW8ADfcORQ4V9f_qxnFtwBCJVrAqc3L-H1bjrp9jRKGZintsbOxfAhWT6fikDNsxWKgneKAFVuemDJpM5Xjj-L5k-0ZSj_3Ht_W_CHVJzL_djCV0V2c9-Xpbq7t367Uvl7lOe-aqru33NiFcotpiFyyFIoraNm-ynhGBinO1EL3HGlUoplqW-Ypj_qIImmfy26zJuvnNiK6Aeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلن نامحدود فروش باز شد به شدت محدود
🥚
هم براى ايفون هم براى اندرويد
🍏
🤖
600
تا اکانت شارژ شد
📣
قیمت آف شدید خورد
🏧
فقط و فقط تا پایان ظهر قیمت 397/000  هزارتومان
( )
➡️
حداقل خرید به علت محدودیت درگاه (
٣٩٧
/
000
) میباشد
💓
جهت خرید ریالی از ربات زیر
❤️
@V2boxinobot
اينم تخفيف امروز
💓
تضمين بازگشت وجه
➡️
➡️
➡️
بدون يكـ ثانيه قطعى
👍
اپليكيشن تخصصى
🤖
🍏
💻
اكانت  ٣١ روزه تكـ كاربر
✅
📣
:
@v2boxino</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76865" target="_blank">📅 23:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه طهلیل ریز بریم
آمریکا تنها یک شب بعد از هشدار دادن به شهروندانش حمله رو شروع نمیکنه
در نتیجه حداقل تا جمعه هفته آینده خبری نخواهد بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76864" target="_blank">📅 23:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟ فردا چن شنبس  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76863" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">میگم جنگ تحمیلی دوم چه روزی شروع شد؟ صبح جمعه؟
فردا چن شنبس
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76862" target="_blank">📅 23:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76861" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76860" target="_blank">📅 22:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76859" target="_blank">📅 22:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH3bMYOGmfFFXv5c9w5VLfbPrIqC3JHYS3SU-6ANYyZU1YQCsPdCuqmzRSG6Ly3VIxgUyrFer0nO1utuwpe68pGzxBXLhpnO6Dt8JpwWR8adACbtXAJinb0hz2kLOV2U099JBaBH1eaO4Vaeia4MzRT9YlPe2GDmg_Uy6fygoOqjtfQF7hV2_YsZOT2jIeOwJPjgXZMAHMqZNr5bU4pTCIKGZ2jEnWzIq0tcKEXNXJo2p113rmHxKNpdfwzJNmOqlZ4X9L8QG-CESZYawmPjl3kXwpDDJwGuO-6dxURuQOvHlCs3v0DZm3SIkmowfZ5xaMXaUHTMzKNu9s3Brm85SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا هشدار سفر به اسرائیل صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76858" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76856">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بخاطر وجود بزرگترین تهدید علیه جمهوری اسلامی یعنی پوریا پوتک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76856" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76855">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد پورنهاب بخاطر داشتن سوپر فیلتر شد  این وسط نمیدونم یوتوب برای چی فیلتر شد    @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76855" target="_blank">📅 22:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76854">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تلگرام چون با ایران همکاری نکرد و مشخصات کاربرهاش رو نداد فیلتر شد
اینستاگرام و فیسبوک به دلیل نشر محتوای ضدحکومت فیلتر شد
پورنهاب بخاطر داشتن سوپر فیلتر شد
این وسط نمیدونم یوتوب برای چی فیلتر شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76854" target="_blank">📅 22:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76853">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYkfhW0duR7YoOZ1bI936VOKLE8TO15St7Rqp-i7ISet-V33DQ9Q6l0libMLmroD_T_Y75waRwAVLYr1O766uKtbo4GaqqFc2NFr_FiN8obrk2-wzt88VyQV6pwIL5oaMTBOI1eXqItV8hfWXhk7DeXPjagp7a_vvcbY9C7P4RttqsM6jgsP-LMgbBvzaPmPcKmP_Mnfjj-4Au1Erz77IOLuL7CmYbmkXO-oHQ_g7LRFmRQdMr4HtckzrLMJoVnWwTxLPq4IV18o9kyT_ZiQ4qtlXJghMsYgAFm_JclkU5SvwsBV99louBIue36AjzW2dMkAMMaRbCpyuoq2_tt_lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76853" target="_blank">📅 22:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76852">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeQz46ZZaulQ93wtz4A1Qtrfwcl6ZXrsA3ryMjrKNfLSdL4bFxeMA7KRB_fP0rYKbzOgHBlBl_M3NkN2QVHWljXkzkw-dhwEiZ1h3oxFBhPZY1J_L_6b8ZjLB4HDRyZ2USV7oiwHNV1FzaW7D6edVPznjkrNS-FYuC79_tZ8jORzRVNPsF-OgzEWqQ4WzU36eQJ47ShFzp-y3PdlX6y9CCGBQN-7sCf68922ornHO8qJxKmA5kUlMps9bHp-M2e3vvR35m1QquqzOR4i5-pUAICBgEx6oaEpgMqnuZ9lg7yV2mW8ljxgh2PKpZXT94uVM-l1zC4e1VzL4irujNVuRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش تحت تعقیبیما
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76852" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76851">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07e570681.mp4?token=QMG-GYYNvrE-FMCr78ojqTEmPd-V6Q_BvzuJfYTJ96pG_KFh_FVuWMKR6o8KhZzRpITGJRm4ijQdfqQEXPvA01iYw_pKhfcuH_o0dW2WjD7zGeujRYZEBs0hi8IN0_rlt-n2uteeP8cLcEQY0vInc0SvmWrO13kgfWB-v7hKJlKvll079w75KQo3TEONUPkBulFlPtCkvJ1JUZIs3mEuuUKZq-3uG5riB1hzwNLt9pdWlUZ1r6cSWiR6vMPWn1u1lISM9ttduqByyL26kXdb1X_7e_df89uV8bHByGAkGv29iocYPi3n0i2gceW41mp0OiVWoZokYFjM8PEIAp8PnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07e570681.mp4?token=QMG-GYYNvrE-FMCr78ojqTEmPd-V6Q_BvzuJfYTJ96pG_KFh_FVuWMKR6o8KhZzRpITGJRm4ijQdfqQEXPvA01iYw_pKhfcuH_o0dW2WjD7zGeujRYZEBs0hi8IN0_rlt-n2uteeP8cLcEQY0vInc0SvmWrO13kgfWB-v7hKJlKvll079w75KQo3TEONUPkBulFlPtCkvJ1JUZIs3mEuuUKZq-3uG5riB1hzwNLt9pdWlUZ1r6cSWiR6vMPWn1u1lISM9ttduqByyL26kXdb1X_7e_df89uV8bHByGAkGv29iocYPi3n0i2gceW41mp0OiVWoZokYFjM8PEIAp8PnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلر جدید عصر یخبندان ۶
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76851" target="_blank">📅 21:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76850">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🛍
قیمت به گیگی 8 هزار تومان کاهش پیدا کرد
🛍
حراج ویژه تا پایان امشب
⭐️
💎
30G-295
💎
50G-470
💎
70G-590
💎
100G-800
🤩
لود بالانس شده و مولتی آیپی
🤩
🤩
بدون ضریب و محدودیت کاربر
🤩
🔴
ظرفیت به شدت محدود هست
💬
خرید
🚀
کانال مشتریان</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76850" target="_blank">📅 21:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76849">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شهر صور در جنوب لبنان بمباران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76849" target="_blank">📅 20:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76848">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ژنرال محسن رضایی:
از این به بعد آقای ترامپ را باید روی ویلچر ببرند که بتونه آمریکا را اداره کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76848" target="_blank">📅 19:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76847">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2HVN2cjqxebKmsMc-GalUwnJq-27Z6jncbRW19Rh979n38EmxTZajHOK9EEos9JYxqN67ya-ZvPW9kKz1Nit6ziVaMpCA-ZFzMlvEz5_UduuHqe-1bbFCyMHeZeEG8S_a5mzIoS63VrO3q197KqrXr0TJcvUyniY6gQXT9iibyECSS1hrY-uQwNCh_a0qpEcZZhDWUXBRlRVRYwk9zNuFGkTv4Txpm-GFr1wz_SbzoeMc7paxujzC4jE4S707CsRMi-0UiYbo_yAGYXuZEugwkgG1LSjVkrq_ib1TYSMXhe9SlSR-U0Bq7uAd_OPmPztyjDaIfK61ngLkdVn2WM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۷ سال پیش در چنین روزی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76847" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76845">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyEFqLZRSxyrn1AvP_N4GwsNKZd9sz6hDtH2R0LzGGsI5OD5jRYK_wh5oc-cAhjODNHyLJ7p8U4hz0TykGgE8TMTlwYkdkt6HMr3nbo77p_M5mPA75EhNLFgyHKLOCTOFyBWafVaDuqhDODiCN6g2wICxe_Eer3diyVvLabuBtSrzAJIz1Ruvqzk5SS5WyUeqOT-sUG-SVK_90taxo0HOJhjpIEytzgU0KEG_6axLxUlmT-B0xfTe3Eh5rBJ03KO0eoDclVufLczQwedM9SMi6-ikOkaf48JwhGbArXB2XJMNG9jMcpnbBq3R4WDyRKXtjIyNHp_PGYyARtBa8urjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :  @Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76845" target="_blank">📅 18:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76844">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حاجی کاکولدی چیزی هستی این کارارو میکنی؟
- اولین سوالم از حصین وقتی حضوری دیدمش.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76844" target="_blank">📅 18:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76843">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=LDSdQ5wGZ2UMZmxYlOC_wxWn0YhPby290VBzAjYbps3N7KA9wGZ1LwKC6QG_4rA0_7OHQJLrcqykZXuQ5-Hxuh6XnMbQm3xoNYVcVPz1E6ai5hs4gxA9ADXTP8T7rNJ7cRFuGpnvF_qcRv7B7kDwjN2WpYVYCMch2iSTWG2WwuCfp8dSYKGTrxJgLcrAuT7bD0HlIEeeatpQyJlf7-qO7_-fI1YaQrlpmya2pb8KKtTozA9FB24VjJ9xvhTYQkEfY5q-btfQsPQ6SZCNbWun664bWHhD5eVpASCzhd4QRt3uB37mJoNBkKOObUcr2lPYdurMMEr9NlPQCpj9smto_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bca6df80.mp4?token=LDSdQ5wGZ2UMZmxYlOC_wxWn0YhPby290VBzAjYbps3N7KA9wGZ1LwKC6QG_4rA0_7OHQJLrcqykZXuQ5-Hxuh6XnMbQm3xoNYVcVPz1E6ai5hs4gxA9ADXTP8T7rNJ7cRFuGpnvF_qcRv7B7kDwjN2WpYVYCMch2iSTWG2WwuCfp8dSYKGTrxJgLcrAuT7bD0HlIEeeatpQyJlf7-qO7_-fI1YaQrlpmya2pb8KKtTozA9FB24VjJ9xvhTYQkEfY5q-btfQsPQ6SZCNbWun664bWHhD5eVpASCzhd4QRt3uB37mJoNBkKOObUcr2lPYdurMMEr9NlPQCpj9smto_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آه فدایی آروم تر
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76843" target="_blank">📅 17:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76842">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=XrEukHXCA3KiLq9l4gtjk2HwFRW5hd-jKANOSvfjaIHpS5ku2FSMpXysL5K6TENMoqWLO_6zHplweGQ1gObJjA0JlrkFqQ83uiHSautPPRQwfyC_xUjEBjluVSDnFEG3hBWiGT5Lda4XGX4YcQetxYBqjXuhcA3LGVwMPOnWLLUfGLsIZntIeqvtz02Vye3Ycyxsko53B-A-9xm8Dnc8wVV638PhgsYuMtVDDeGdjzEy1q2B5GBCmydZRHQvWdELaGb2IE6Kk0El6YHcPdA5o2SrYZpZuZ2tPByuaburhNxIsH_8s28n7FePaBKXpggmkPdFPztPuAjhVGl0fn1SeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d10c25c4a.mp4?token=XrEukHXCA3KiLq9l4gtjk2HwFRW5hd-jKANOSvfjaIHpS5ku2FSMpXysL5K6TENMoqWLO_6zHplweGQ1gObJjA0JlrkFqQ83uiHSautPPRQwfyC_xUjEBjluVSDnFEG3hBWiGT5Lda4XGX4YcQetxYBqjXuhcA3LGVwMPOnWLLUfGLsIZntIeqvtz02Vye3Ycyxsko53B-A-9xm8Dnc8wVV638PhgsYuMtVDDeGdjzEy1q2B5GBCmydZRHQvWdELaGb2IE6Kk0El6YHcPdA5o2SrYZpZuZ2tPByuaburhNxIsH_8s28n7FePaBKXpggmkPdFPztPuAjhVGl0fn1SeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید حصین رحمتی درحال نوحه خوانی :
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76842" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76841">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اگ دنبال یه سایت با هدایا خفن و کاربردی هستی اینجارو از دست نده
🎁
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/funhiphop/76841" target="_blank">📅 17:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرایدی که پرچم حزب الله داشت با موتوری که پرچم جمهوری اسلامی داشت تصادف کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76839" target="_blank">📅 17:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گروه هکری حنظله، وابسته به سپاه پاسداران انقلاب اسلامی:
امروز صبح یکی از مدیران ارشد موساد مرتبط با ایران رو با بمب تو ماشینش کشتیم ولی احتمال می‌دیم دشمن مثل همیشه جرئت بیان واقعیت رو نداشته باشه و تکذیبش کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76838" target="_blank">📅 16:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسپاتیفای تست کنید بدون فیلترشکن میاد بالا</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76837" target="_blank">📅 16:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnqrx9GYscGE_HN3iLbuYsycHkMpR7Qk4NEN9bTf8K5D83qbDKtLLN_vz-CioZUgSGsllSfdhySK9PjpUbGVhndldXjP0CWxXy8d5NSFksO0IHXAf7u9cPqJ_oEyMjr-5nRmUfgJNvQCZkgJ3ggvVcMAJqetqnGjbbM2IT7M46DB-okA2P_xP5lxSR_OKLSCEJI58nBFegtIrZWxENBSQjK4RI-0A7Vr_SZ5kPIFbughjEVPhm6mC22u76i5aeLzPjsiwQex81WaR3XGB3-uYbRMQCYoYI5soh_GVOPKsqW6DebuSJr6mnYR534abja5cS8Ok6bLCdt4QBo6Ht4iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتی داشت مینوشت سپاهیاوووو یه همچین حسی داشته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76835" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">https://t.me/+nm4DbCzoFJVkOGRh
https://t.me/+nm4DbCzoFJVkOGRh
ی جغ مهمون ما
💋
دیگه لازم نیست برای جغ ب سایت های پورن و فیلم های مورده و قدیمی بری
🫦
تو این گپ با تصویر کار و زنده ارضا میشی
🥰</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76833" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یاااوووو</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76832" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پروفسور سید عباس عراقچی در مصاحبه با المیادین:
در لحظه شهادت رهبری، من نیز در دفتر ایشان بودم که مورد حمله قرار گرفت اما به صورت معجزه آسایی قسمتی که من در آن بودم مورد حمله قرار نگرفت و سالم ماند.
من آنجا بودم تا در جلسه به ایشان اطلاع بدهم که با توجه به مذاکرات روز قبل از آن، احتمال جنگ بسیار بالا رفته که متاسفانه این توفیق نصیبم نشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76831" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">امین منیجر داره هد میزنه میگه میووو</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76830" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ی دور از کص خوند ی دور از موش خوند، ی دور از سپاه خوند، ی دور از بسیجیای محلشون خوند
آخرشم گفت گذشته ی هرکس به خودش مربوطه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76829" target="_blank">📅 14:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدونالد ترامپ</strong></div>
<div class="tg-text">ویناک بهم گفت نابغه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76828" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.  YouTube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76826" target="_blank">📅 14:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رضا پیشرو نسل جدید</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76824" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عجب سمیه
😂
😂</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76823" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOUh9Ak_sFzTVoVBXBJF6wnuZ6iXNIN7d6K3fmFM2cZzgF2rZDD0db4tmqIwnsnNBsfagUYANL26NwpAsYD9WqlObQ3YdoGMxA5QZKJFHTYOG-Z_D4M0jEbeT0ICrOGezTQumgzIUE4LaFdlQTDFbSCLzNIk960Mu3KfVrW1TMZc4xwelivCIBGD4cogndJSiG4mBDr75BIb0cqn6hUkZiBvYIGSmFu47y45W_y8yXiOAGxJRiI_3rM5GpBgLZNOyJEHmHODCnbvti_Kfd7ZCQteXvRaoxUaReVBXXQYOQKnOXmkSrACz0uTEGK7Xd2QYnSEAxE5FGWAwz_QEHz13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.
YouTube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76822" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsi6_VqoZvqOv9GvFL6ZtpLSPew0ilr0XG_P_CawXH4cs-uxHt9RrRmo2PGg4zDWeAaZcwze5xMd6hhJMOLGJ8PqGE5mRMiM99oc87l07nrp4MpbDW9gmVUcEHUfvN7n1nBuhY6XnlcbmQOfz58_1uQDouKtQGYKQaZVjM9QylxrwLG50AM1ozkJ6aBANt8tywAyrEBZ8OsG9XCuSIIHVvxqhqM5rvTa6urGqiKyc9xcjE4QMzOJHgqa1soMz3P6hIFKVPdknWZENYzvRFhKe4bqM5jSfgAPGAtNaEKyMZFBtDA84pWK39i4KPA6SNpYyCebrmFSTCmtc5r1PQxjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1dRMI7jrpWAOVixKD-wUJZkYkl__S9d6-FZTbLN6nEZwhFUQ5NDf_6nC2s53779m3xqWJ7CkDtKps6wK0J4WOwMuVatXbosl5ZTLro40IlaRL85LmRk6CP86kOGjnZRmQWb10nU1bfxNkKNDHsONOFl73r2hwVXQoUG7aKPN6Z_Jq7g-lErH1PLQa6tlPVLiP5lfz3uSCem8DAvPkdx-G-FU_XKreH9JTsRxInxHJMKWdYnfxDiDgK4rCWKfd0XWUyxPKrugZPv3CQ5oC1Q3DgVkhqDVYfWZezJbt9q21W5tgRPsnIpLwiEtljkW4Z6k35y6I5TB1WaMsZ-iuZUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76816" target="_blank">📅 12:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76815" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76814" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76813" target="_blank">📅 12:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این مدگل چیشد حاجی زندس؟</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76812" target="_blank">📅 12:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTfi0WIXfkdIhRnb8knFqbJZypb68OHfVVz_Gbn4YChu3lgxipP3DN9D_dV45-siz-G2MKdoWibPr4Sw1ZER3iVH91cvYlj2aczjtDV_xpKn6uD66rI029ZuA4KyGJ2pmRpTjqtoCL2pp8MbQt-F__eRQ8M_HbkbHZFtR-muMC9bCgp3qhU30RTJtbrqU5sDZOLt07uF717DtH__SP4u6wPrhgoo2r0BNQHeIjTkYYjkoZtjmQp04V2NP68WOuUnZati5XqtAFF5SAwp0qM9M1QouZgpLrk6MNwFOk-6slIpxeZWUxqd0iGfVIywTgQPkGJHZieS9pQfu0EBbVV3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه رپفارسی با دمبل 5 کیلویی داره بدنو میسازه؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76811" target="_blank">📅 11:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=buxNK8Xhz9zvScwgdscR33NCQjfE8W_pBxCB4zPCxOSEsZ89JIfBJw26HJvBssjrt1bzbhkd_52nGFTzDnzV1-QCZ-Mc4ooGYh_zdqdcHDewIKlp4GZia64XK6bsV1TxT5wSj1GVkSDLnj20E-J_sdK1FGqieD1AoqVR-FOTOg_iLmAzH_XakIVTNArG5yP-ZarJGHcd36E_hIB0RF_SEDJzWoIjZyDK09mkHPD-Y13zZBmZC3zWGNeipLQE4zHEcMxPUhhaacc54f3CXxjskFCSmLB3tt9bJvp3ELXbhm04swKQ8rWsp9WlAmbmxnLayJWNYH4DL-IeBtOl5w0bIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=buxNK8Xhz9zvScwgdscR33NCQjfE8W_pBxCB4zPCxOSEsZ89JIfBJw26HJvBssjrt1bzbhkd_52nGFTzDnzV1-QCZ-Mc4ooGYh_zdqdcHDewIKlp4GZia64XK6bsV1TxT5wSj1GVkSDLnj20E-J_sdK1FGqieD1AoqVR-FOTOg_iLmAzH_XakIVTNArG5yP-ZarJGHcd36E_hIB0RF_SEDJzWoIjZyDK09mkHPD-Y13zZBmZC3zWGNeipLQE4zHEcMxPUhhaacc54f3CXxjskFCSmLB3tt9bJvp3ELXbhm04swKQ8rWsp9WlAmbmxnLayJWNYH4DL-IeBtOl5w0bIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط 7 روز تا شروع جام‌جهانی مونده.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76810" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmasapPzkF-h7e80FpxC1JyadaO6gsd0wGEQzXtRFtuEIVVDaitrx8dGFZ_J75QdJAV4YIkQA5L0EZIhHYZQFGx5saNky36HEvVAIffN3BGqvJsA88VwhmVp-nVh7e6Pw0BzPCgU21hIWZKpHGoW9lFFngkNLWcBVu5eg68NzZmouTVhsUq6elARppzS-KzFLSrCdDhYqkFqx_Ni_hq_tpFzaI9uasQSsu7E2pccTHK1KPLTSdRJmZwqzum385qEulRRorNJ8OwId0Rmu-S_qkC779GxqPnSZUkTNfgpNGKP1Nn2H_LwyhBGuBrzSUKlJcu9IGWkBFMmMibbGAvVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیبیلاتو نزنیا آقایی، عصبی میشم
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76809" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=RFsm3mHE4mlpg2AQkUejzzrt215W-80Wj9d1nyUd3U-Cg4ijXC6fc55lXbXhgFxlcDCPIg6KebsqSeSqjjcbS2uZ6UwvX-niqt_UMKmuGNzEcb6XDL2kFtAb4L_Gw5mJ3MfvEX_ie-rrpLTEPnhmwyr2Qyi1PQGl8Mt1Gp2841c07ZxLZy5beMQ7Bp6YEwrGhvzf_A_MZY4mpVKRzUv_UpZZNWrYlwC4Fuwe88ap4E7J5DqmRIPcgAFI79ANsewjiBy8Qszed0Ws_jEN93MeaD-v2trrSjFC99AskPb_WQ3IIejxKOTN5mykGXVBIK19S2PEH88-fpsP7FkqdovTFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=RFsm3mHE4mlpg2AQkUejzzrt215W-80Wj9d1nyUd3U-Cg4ijXC6fc55lXbXhgFxlcDCPIg6KebsqSeSqjjcbS2uZ6UwvX-niqt_UMKmuGNzEcb6XDL2kFtAb4L_Gw5mJ3MfvEX_ie-rrpLTEPnhmwyr2Qyi1PQGl8Mt1Gp2841c07ZxLZy5beMQ7Bp6YEwrGhvzf_A_MZY4mpVKRzUv_UpZZNWrYlwC4Fuwe88ap4E7J5DqmRIPcgAFI79ANsewjiBy8Qszed0Ws_jEN93MeaD-v2trrSjFC99AskPb_WQ3IIejxKOTN5mykGXVBIK19S2PEH88-fpsP7FkqdovTFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=BpoNyaMYdSgcFvMkBNGTU3l4yoAkUDdi4xIRzt47iepe1_Oku41N3zFo9RsO8gKurIi1e0HLFudgwMVueWUtK8qb5mv9juqvFd_B28Y5eRP-XWNARHfmnxZXBWF4lVLkks6eIG8YzkmwO0RiW1MTyucvEloM2qMDz9TfnZNFuq7NlhSWGLr3z3tpo0SDQUFrh9GlC-VevAkRmXltmGE6cFUhjiWT_bc5ehVKVYkGzzYADFriVm-LMhzx16wpaZccFshrliRFwT6nU0VOUFYBF5WURcbtucnlYVbrND-uX1Jr-D0TVLGCERoMVhJ66kNgj1ZzM98SNFlvscpMMf4DTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=BpoNyaMYdSgcFvMkBNGTU3l4yoAkUDdi4xIRzt47iepe1_Oku41N3zFo9RsO8gKurIi1e0HLFudgwMVueWUtK8qb5mv9juqvFd_B28Y5eRP-XWNARHfmnxZXBWF4lVLkks6eIG8YzkmwO0RiW1MTyucvEloM2qMDz9TfnZNFuq7NlhSWGLr3z3tpo0SDQUFrh9GlC-VevAkRmXltmGE6cFUhjiWT_bc5ehVKVYkGzzYADFriVm-LMhzx16wpaZccFshrliRFwT6nU0VOUFYBF5WURcbtucnlYVbrND-uX1Jr-D0TVLGCERoMVhJ66kNgj1ZzM98SNFlvscpMMf4DTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل اینکه خوشش اومده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7x7JY0xlAXreV7mycXGq8KXXm_n_oWhG_cSrciHvmExV1bMnTBtwISOaVtZb73GURpdXK_KgZtbimqbxCweKzDtak9YsLYH5qo2s3vtXuC4AGw67DoXEcAlWKz7iBMkIFy8KkfrYS8wfDacJpKR0vLgugd3EE9kHq0LGKl0UfpCn61L6dJUMiroAlmjQqzqHnb8Ja-WA39YlO9QBOOYH86qKArTE_OuvRiXVfDBtxxdvm_N2kGdblqAoHLnRZQvWbTM-gejX37snmkG5I4mGLJb2AiwW-T5-Yx6GoTd3hnnVyVTy6AVe5DL2rav78H5Km5hgmVVUYVRIJwsW-VbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVwXoUsy3IgnpXX0Bdz8VznW3tBzNH2kghjEymiYpgNIFSo85oac7WUDD7xg0ZBOzTxdJe3yLlpfM04-ANXW81108Tce67rcs-BlFif3ktvxQejiUf305xLc0z0IeosazGby9ZyCss2jVbN5LbvQqW0TpJX8YbaLd65W7LVGoTMujGxKWLcmY574Gbl25yw0_EGz9k7CyGDuwQi4Zvs5PAw6Z6c9TWlKJqxCO8rfwTQHvgnvK8ZE-4NEsZpCLORkzHKstJlFVcycs_yAdbAmggDiaLef78lGis9WeORQOnjFCWhptLGQYDeLW134Mw5oflz6oDnSG2SWXDGNtWEXpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7keBzy0Fx7us7CygLGpFp1WnyMpSLn7YlctKsyMmPNkUHn-_CeTBDAReY-bPwuNj6Ev-lx9H-Wae6bxe2iVCmN0Re2Ze3f6fxqPW5gkNAyhezSbop5plDcOzVlzpm8_GrHRcOUkP0xTZhFwuFfOK572SFScqegEki3yS_aD11uJpzuA4687Oh9w_bnl7472OiyiVuggXahHbc0zj4CBfq0BR117-nfJUXjr8bfDz-eyMijM7pVlSPGPYq8nthCaDiKvOwZNUH1nxctmFmIiCi3-njHNszhR1WGOlTFIauhhBAO_e_pfiYfETATvNTg4LA25Fo_S29QVyaa6zzN5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=dKRy8-tMfZD4eNDv6axW8Mpw7-Imr_BgmZ8gCFPo6L0Vh3PpeY95yEI-EqO6ZX95-kGje786kDAHgv3iPZ_AoeZXa_TNJ2oW7BFyaia6OKHHBGgj46CGgjAMtGZqjKmjKupHtCcIF-Dpsqp27v_eWrvdZLN-BAlrvvOOd1_KRGvMR5ZEKO8vlH689swcrMgzogk2DVv2YSXKxLSaBeyQ12FykT5EC96h-DZIXt4GdiaK101dQZvSsMVYYmAwRUKIk-bVqtk9qt_0n94lwNrjBMfu1GMVsTprfAnRUK5NqRxkDjvr-veXT0lUW9aTA4gF1pm77YQ6SBsFCD1a_CYwdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=dKRy8-tMfZD4eNDv6axW8Mpw7-Imr_BgmZ8gCFPo6L0Vh3PpeY95yEI-EqO6ZX95-kGje786kDAHgv3iPZ_AoeZXa_TNJ2oW7BFyaia6OKHHBGgj46CGgjAMtGZqjKmjKupHtCcIF-Dpsqp27v_eWrvdZLN-BAlrvvOOd1_KRGvMR5ZEKO8vlH689swcrMgzogk2DVv2YSXKxLSaBeyQ12FykT5EC96h-DZIXt4GdiaK101dQZvSsMVYYmAwRUKIk-bVqtk9qt_0n94lwNrjBMfu1GMVsTprfAnRUK5NqRxkDjvr-veXT0lUW9aTA4gF1pm77YQ6SBsFCD1a_CYwdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_xzS3q9mWb1upqETjdbMd4z2N86tidMBta1RagKZARIzCABUicnqyDFnIyZbT-9va6ZsM3pD60TofexEw1l4tEEwda5wyc-xFp6yuYsPTv_BB1l_AAzJ3djmNIV_eS6ocBbUGWlaAFb0V5-7uvvrTyCFmEr5rb_2vF80P8Xo87_6bT-Frk6StK-yOPGox5K3F5mjcMO6tzKXcVP_J4U4st_y8RId81f6jB1Vr7NZDUtQxTdkE74MEA-C_e-KXOrxppFUPrvR9zYN3qW-hkqfhxK6VoRD2VA7sFF-j9BnyFkYP_595BQnzPp7Lh1SUMNjzPSSgal8KT3foNNlbwg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
