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
<img src="https://cdn4.telesco.pe/file/BFal71OjZxRK_NAfPX7pe1hhSDaomDI_hSdzBOWi8JBmY5FrvJVIxEH7tQn3oU4k0C9eIUFMFE3Say_Fb7U_UuVsZsJwao2UOvCpLIkrNbXSz6nLXsqMGVGt3kYLLaKEXv1blm6FIXMddkjYMzwnGc1wVLcTfOqLsF2LiMboTAhhphn_AMgNd0U-DIVPjMsxmTLM_7K5mX5XdnPzPjP1Q9UJMZDbeEG3bp4sMiP5qVG9D_djmi4IXPj1Lw7nkGH3uDD_4eZ6bb0cwDTsSiVedubwaS3_laBbWBgyQECgbwgPKab8tQ100brNTfQRJgGSu9s59AZrin39MFQC0Iw4cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-83344">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترکوندی شیر باهوش
مدیر سامانه هوشمند سوخت:
خودروهای نو شماره بالای یک میلیارد تومان مشمول بنزین ۳ و ۵ هزار تومانی نمی‌شوند و تنها ۱۱۰ لیتر بنزین با نرخ ۱۰ هزارتومان در کارت سوختشان شارژ می‌شود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/funhiphop/83344" target="_blank">📅 16:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83343">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/funhiphop/83343" target="_blank">📅 16:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/funhiphop/83342" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/funhiphop/83341" target="_blank">📅 16:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmTC0ope4a4gtIqnhcDrZgUg3LDoQG1BEsqknE-5jrgiGLdsZv7hgD0Wq100evo37RrTLBB0giu3GuoujTeJrDgmyG44VI6Ngwwh5MzNB4ZkAkwXsSO9cNItx5Se5EO-mysoda494F-UFPzV1n5hqCE0TtdqNdCzwcFsNRttY_urWK94yhrHUrKjJL-LKdlQA0oQcsOStNiBn7NqURSY2kWax2HoplR2dmX-cWu4Gmz8pnY7JO0CezCNqPFCYuauoyJvSxSoo2-U4f0rKC1sE1BUNqIBnkkU1a94mbWVPv2jTpwZHMhNcQhGbF0svzZTHKeDR0b4g9LqGdqr3Vwq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام “بیداریم شبا” ریلیز شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/funhiphop/83340" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چرا بس نمیکنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/funhiphop/83339" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQplEcNqH9UKbtcOGxBnMXz0eLRjcf1-VrS3ROsL7zy-4Pi7txUoSOumOT3-lJAppzVerlZV_r2lAVpVfhMtyFXoLTp0BM-51Khxae9T8vvMCL_nzyP-uTtNrOVMTA8gzGKVoUnyx3F5hQT0_itYtHj51xeC7Fh3rQR_C8thJapMZ-8G259yS1AAxn6jkoBEDEpIA8cCDJeozxyvQQmvtiUczTIdu2r-zv5nhcmgzo0v_Qa1T2S74QpWcBRuT3AnYnbPziFSoSa8xJ_hYRl1AL6DsloeQrHwjtg9_ESWilBBAS79pzHQ-ub1oP0BeSarggfokg6wwm6_jB6N17Dagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا بس نمیکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/83338" target="_blank">📅 15:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeKs9jzqUzd1cfMo495mLk7c9DvBFEGq4HWpOMLGckuz8kwhyww-3-MuIsoGedUXtpAMe9XVEu5IPz_fvMSHRr3VS5ATVfBZ5EJjKh4iyo4RCKUYcw6lPTYJDVspPfihrP3jiEugLiZBKKGiUZKRmhlORCc1lNkNMpLVyL889vNAzCWNNCXpkbda__Seq5fSzzEmnijvy6QISaN9B1iXo7xjzBAmeBfCUa6PgvZ1NmTBXO-ESkpC96aInPkCbK1KyaYWM90F9Au8p8VaUSjyrvYOAkc6HfY_LEwKAgSBCRstMsfcZ-e5Iv5us4h8FM23ENYtyMnrrFianOMWnZDc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم حالم خوب بود تا نوتیف اومد</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/83337" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این یارو کیکستی چرا اینطوریه، میدونی داره چرت و پرت میخونه ولی کیف میده گوش دادنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/83336" target="_blank">📅 15:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJaYDNRa7diA6mv9GsqX9VKd0T2rtsf-j48lrjPwWrWAe4022U1tsbWljPsndVqoMw1cqZZm5Tlr0Dc2Wz1io0XjA6Iz3caqgzEuVxVbo6RBszZLrsaGim12GHmuDyHd7aKI3pBr06eSiLe8dFkZsTqUlV3ISZZwT1pOjdIbwwSX7lIxh80xuowuTWVtESfhqyga19dgoBegm6chEBEdHQQnIZzwmcQE8TBeoKPjqlBJRpf5fUsqHF68if_7tqTFDbKZq6pG6v1hgUkKGLVdlL4ayhJCF3jUDy6lNvGme9IB_g1iyamzsY4pgTYxB-P52ctcc4AZnj7UqBsI4Yv30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/83335" target="_blank">📅 15:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وضعیت والیبال ایران هم جالبه در نوع خودش، همه میدونیم کیریه، ولی نمیخواییم قبول کنیم کیریه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/83334" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FARov-VDuCalKoCEUzI4QDFV-Fiz5bKg4ou4MyRZhAVfnVBeQVvljZJZ7EVhwoU5AIWtK1wMZyoSTXCKyusgH9j5qYEl0DQ2s27M7LPjof2Lys5vGfyDSJSJUxvE-7lS9Vt_CDzjSMkuB4tQ098Yq27o5z1TcWgtBLdF_5ecFADA9vURFb0X8HotDv49mvQLyxi3Ba-670GYcIDGiV0REfMMo2xOiCGOXS1v2O9ybK6WG9UBo9MoCuLzKSQCvyP3tldA2mwexWspspO56DnMLgdn4kxlKLVdm652V87AYpjPuGfhw-C-5ZjySiWqpONw7IV2kTwhM4pjvJK7D_gocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکیو اینو گذاشته چنلش پایینشم نوشته:  "نسلی که از زندگی خسته میشود، به فراموشی پناه میبرد."  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/83333" target="_blank">📅 14:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c040dfe7.mp4?token=sdvnlpKiH71ZZ7X4iczBTiG0iqQNRe2-H4_j7y4ppABVCKk8jj8R-kORD-FdbIpZzIAO3NfyZIaypuTn0hQ_8YBEqrFGsDH5Iab9FKhfdrMw_S4T01JnzgsMOiJ4AYGh-vm8qksQxOU2NfpIW22lUX6jZ42O3dtHQ_t-pTLWbRhIf7DmqMQ74NsITB1ZucnB18mIQGK30wwOMoDpfnd05q5vrYuNC6EmS9Ou5fLLGLA0jVhAtuzTVJSneeipuFJI0Xq5w8dFS6ntaKxZR2vIuAH1DnVBfM3xpNZuh2YJnYCMkXwz8uwu5ujpHT8vrcNMiOyLdXUy0voFwaRSQzYRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c040dfe7.mp4?token=sdvnlpKiH71ZZ7X4iczBTiG0iqQNRe2-H4_j7y4ppABVCKk8jj8R-kORD-FdbIpZzIAO3NfyZIaypuTn0hQ_8YBEqrFGsDH5Iab9FKhfdrMw_S4T01JnzgsMOiJ4AYGh-vm8qksQxOU2NfpIW22lUX6jZ42O3dtHQ_t-pTLWbRhIf7DmqMQ74NsITB1ZucnB18mIQGK30wwOMoDpfnd05q5vrYuNC6EmS9Ou5fLLGLA0jVhAtuzTVJSneeipuFJI0Xq5w8dFS6ntaKxZR2vIuAH1DnVBfM3xpNZuh2YJnYCMkXwz8uwu5ujpHT8vrcNMiOyLdXUy0voFwaRSQzYRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکیو اینو گذاشته چنلش پایینشم نوشته:
"نسلی که از زندگی خسته میشود، به فراموشی پناه میبرد."
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/83332" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83331">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وضعیت والیبال ایران هم جالبه در نوع خودش، همه میدونیم کیریه، ولی نمیخواییم قبول کنیم کیریه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/funhiphop/83331" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83330">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اجرای قبرستون هیپ هاپ پیشرو تو کنسرتش از دید مخاطبا  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/83330" target="_blank">📅 13:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83329">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71116434dc.mp4?token=MgDUaqTNR5j3sjs521HKy8a7WujmbGzaUpzpSUxJKI8NQO7d16oAyltWWpOYZLu4kDRoklqjppa_9z0u_AOFXA-etKjhCmEKgHahmjwdjkOUJveE_4dpiEeVLRQBsk-Kf4h6kxO_EZoQrCQOgcZRIw8_dv3QSSrqzfT0kMBe8mm6wI6ZmXmrtzW8AcqBgUsm8V6N2_xqeCcLmtW15W4Hb05Gwi-rrm_TSTA1sjNFHb2QV4sLJn_TLkDxVKnmAtTqOsfY3uttSvHFYyH1jHg77a9fm7iDYjom67QUYOFXBwV9O0be-VOxXJOiOE0StxS39nThRWlMYfCsQpH8fYKuU3_U9IEBRIjbshb5RAHGpZS9g_v1pCKNsobJBJbwJUHibtUy3CBsv7O1BUJ9KoCV96MMCYHWWy-KRdJFQUjGELazPxNMnM2FOrBBMVYj0qHRyW55Uy5Q0bjjYOu2DkfLy2gpyyqNkQ7rGmHbv3W_USmc0ghNkJGKAglq6fax51MKlsOsgPIVKRRLSfkSP-IWS6dEp2aWPqDJDkefm0QAdZiU5tsleARElMDI8H2GTgl5yRHiUkW0rnfjo1DH3I56hqzUXFDcLmX50RXVasW8OrQQyYWwAYebbMh7a5ouAMQDnia1Wd449DrFngyfyumgTDL8Q6RDL0ygrymJyMMNrNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71116434dc.mp4?token=MgDUaqTNR5j3sjs521HKy8a7WujmbGzaUpzpSUxJKI8NQO7d16oAyltWWpOYZLu4kDRoklqjppa_9z0u_AOFXA-etKjhCmEKgHahmjwdjkOUJveE_4dpiEeVLRQBsk-Kf4h6kxO_EZoQrCQOgcZRIw8_dv3QSSrqzfT0kMBe8mm6wI6ZmXmrtzW8AcqBgUsm8V6N2_xqeCcLmtW15W4Hb05Gwi-rrm_TSTA1sjNFHb2QV4sLJn_TLkDxVKnmAtTqOsfY3uttSvHFYyH1jHg77a9fm7iDYjom67QUYOFXBwV9O0be-VOxXJOiOE0StxS39nThRWlMYfCsQpH8fYKuU3_U9IEBRIjbshb5RAHGpZS9g_v1pCKNsobJBJbwJUHibtUy3CBsv7O1BUJ9KoCV96MMCYHWWy-KRdJFQUjGELazPxNMnM2FOrBBMVYj0qHRyW55Uy5Q0bjjYOu2DkfLy2gpyyqNkQ7rGmHbv3W_USmc0ghNkJGKAglq6fax51MKlsOsgPIVKRRLSfkSP-IWS6dEp2aWPqDJDkefm0QAdZiU5tsleARElMDI8H2GTgl5yRHiUkW0rnfjo1DH3I56hqzUXFDcLmX50RXVasW8OrQQyYWwAYebbMh7a5ouAMQDnia1Wd449DrFngyfyumgTDL8Q6RDL0ygrymJyMMNrNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای قبرستون هیپ هاپ پیشرو تو کنسرتش از دید مخاطبا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/83329" target="_blank">📅 13:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83328">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d41f1467fa.mp4?token=NYBxMRvT_dWnrFPCAPpNkDMUPmw0UmU1BD1vwW2ZlPcHEyTw_VvID5wzrB4ouhxy2lv04FAnnSTTKwRXcFIgg98QmuJ0TKU7B80D1YDt7x08Kmjsf0YV_c3vVDo9xi3OjwwgcrLhjgKiZUObb1HVoRNA6ycgDejFxA7CT4bh_bj_6f93fDfDGDfxUirSZMNSSwn27Iubj96UOc-i6tJNNvjErsdK33hHkxaxCaGA_efs5Jh-znU2MW-3QcK_PhkpFotRZT7-YGF9-o9ovlxwKVd_3ZG5KMRSd0wuY-ZyDSocmAJlhx2Pv9WFr1Sf_ePDqwDlAA_7sWWaLN-3CHclLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d41f1467fa.mp4?token=NYBxMRvT_dWnrFPCAPpNkDMUPmw0UmU1BD1vwW2ZlPcHEyTw_VvID5wzrB4ouhxy2lv04FAnnSTTKwRXcFIgg98QmuJ0TKU7B80D1YDt7x08Kmjsf0YV_c3vVDo9xi3OjwwgcrLhjgKiZUObb1HVoRNA6ycgDejFxA7CT4bh_bj_6f93fDfDGDfxUirSZMNSSwn27Iubj96UOc-i6tJNNvjErsdK33hHkxaxCaGA_efs5Jh-znU2MW-3QcK_PhkpFotRZT7-YGF9-o9ovlxwKVd_3ZG5KMRSd0wuY-ZyDSocmAJlhx2Pv9WFr1Sf_ePDqwDlAA_7sWWaLN-3CHclLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران داره هر روز ۱۵۰۰ سال نوری میوفته جلو از دنیا
یه پزشک زنان طی گزارشی گفته دختری ۱۳ ساله رو برای ورم شکم به مطب آوردن، اما معاینه نشون داده که او هشت‌ ماهه بارداره و ماه آینده باید زایمان کنه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83328" target="_blank">📅 12:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83327">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فایننشال تایمز: حوثی ها با کمک هوش مصنوعی تونستن موشک بسازن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/83327" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83326">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de166635f8.mp4?token=GUcWmC5GkgQ2d-BCPVaRFnqbGB1GMDMw9z3YQeMVZWJ7VhrK6_fHyVJqr8rFfT8yEuXxZb4DFYzBvczEsM7sj7_3rHDXRy7DkTZCRds0ATogSBGmCtUN7fSMmKQu3yQ3IyxDVBsS4uwAegcWSyKN1g9w351paNIuvDqaBddBv3Hm4aYJB14PcYH7QEUbrLa_J-O93qaYIBSqt6PbjP8e2FpjwmBT8ljmO-NvqOaUSkkJNvepXDFNTS15ld92evCTe5rG_8HffnSg4A4AzrQftvaHdEUKQGnr5QJSJqf5TBdEHWHfGl-FuK93gP4p9HjYFUDjI1VHSV1yBOTkFIkSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de166635f8.mp4?token=GUcWmC5GkgQ2d-BCPVaRFnqbGB1GMDMw9z3YQeMVZWJ7VhrK6_fHyVJqr8rFfT8yEuXxZb4DFYzBvczEsM7sj7_3rHDXRy7DkTZCRds0ATogSBGmCtUN7fSMmKQu3yQ3IyxDVBsS4uwAegcWSyKN1g9w351paNIuvDqaBddBv3Hm4aYJB14PcYH7QEUbrLa_J-O93qaYIBSqt6PbjP8e2FpjwmBT8ljmO-NvqOaUSkkJNvepXDFNTS15ld92evCTe5rG_8HffnSg4A4AzrQftvaHdEUKQGnr5QJSJqf5TBdEHWHfGl-FuK93gP4p9HjYFUDjI1VHSV1yBOTkFIkSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی دیشب زئوس به مازندران حمله کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/83326" target="_blank">📅 10:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83325">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJDtqhxFihYdXMDzwFh0nP63eGgF2dgOsEpEFRAnH5Njdz-Pnna3IqGQubhxjiVj8Fn07Kc0AsNKYdtdcBpuy59Sw9LIWQgIbb9Rd5Paj3A-vAGOOJh7UncDylq5Cxg-Xt8IXzxQSUp27G5btoleIA9CGKPQx9HFtFFUr2BTHxxT3GBkTyALOqgv7Ryo2aSw4-mbrfrJOgLM5et6dBynb-Z797v196dW42sc7MDZohTBZlFBy6_H8q6sCoEyAQ-TAhu5_azIgYfda1EFSAiTTwl4_Dhq0GS0ptdrEGHIskq2BV6CqjQ0L3F0XQNvC1vrIFocsB_6v2B4Aw1BBNOrwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه حملات پهپادی به عربستان رو محکوم کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83325" target="_blank">📅 10:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83324">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gySUyzBI5cWHDjNFqQPzm-HskOJd40kBynZWcfJAPo7EkSz_bzmH9RzYlALrWN0Cm_j8yk42U3Taw14bGGrbmuwv429_aqkXE7E7SNimu98aTr5oCtvI4tVgX1pfUyYExCB6VlgtDm2GAZrag7kpoS6mNdm7dEToNYT8baY-dL2uPzGO9JbeBUIW-6W6Y56oKdaVm89d4Dxl_L19zI6cH6mNmG5I6pnmrYrywdGWCFh8gdRT-paF5WGIMQwV3X8utV4oFeDgCIVf11h3tLgD9GpmDj8t8CbWV-ad_JMpC7diQSID2qkvoIKKz-vEM3R2KuzICk5yGPzbs9UeDCMxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا تا چند ساعت دیگه مجبوریم یه چیزایی گوش کنیم که دلمون نمیخواد دوستان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/83324" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP4xQqoP-ZuWKANNHqmGMtm6_2Pb9y95LDfS6n9xs4fdZfgCc0j7AutZuaIH5G3iDVTrX_6S71Z6JWJfud2ouNs7KoipvM3yXTwSi6k7WdtQ2Ipqz5dXRgfAqXlCt4OCAlHexMjMj26ULJsN02-yEfaKvxXsRbNyJCHtdUgg2Wj8b2vfdoSrcP-l-9mHMpJX-4sH-G4Bw0T7Ci8f3Qh9XLviBEeE7pH9SXzBy9UzL4remNgWLDHtYRgXBL-8c2BPqQsLPPQBLQGF2LWcIP19fuHPjhD3ppehYbF4gx_fUiWc-0cky72Va94AbZDdlcPf5avLrWda8LvidqRndc86xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
منچستر سیتی
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 -
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر یونایتد
🏆
لیگ برتر انگلیس
⚽️
🕔
ساعت ۱۹:۰۰
📍
ورزشگاه اتحاد
✅
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی
💥
دو غول شهر منچستر در یک دیدار حساس و تماشایی مقابل هم قرار می‌گیرند!
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر سیتی؛ مدعی همیشگی قهرمانی با سبک بازی هجومی و ستاره‌های بزرگ
🏴
󐁧󐁢󐁥󐁮󐁧󐁿 منچستر یونایتد؛ شیاطین سرخ با انگیزه بالا برای یک پیروزی مهم در دربی
🎯
انواع آپشن‌های پیش‌بینی مسابقه
📊
ضرایب متنوع برای انتخاب‌های مختلف
🔥
هیجان دربی منچستر را از دست نده!
🌹
کازینو رامسر؛ جایی که هیجان بازی هیچ‌وقت متوقف نمی‌شود...
⚡️
لینک ورود بدون فیلتر شکن به کازینو رامسر
R22
🅰
🗣️
@C_ramsar</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/83323" target="_blank">📅 10:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83322" target="_blank">📅 01:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=tJ8gRpSXFaqBEyzkv2zMosiQJn2ZSUd6APGiTPMOSBYEVIh_AceIS23rQYe0Nm_6_ys6eY63fCzyeHiGuFLCfsaIukkJk7c-0MX3gaSJIxglOBICJK7J5iTdkbYOH598HeXVI4zyEKQrXqaOD3U0Lt_pgFZV77gRvbnFpcgSeQahBM9MbhWgoA044yiKYwfs2grxxc5zn5qrU9j7QqywSYHBhHZooUckTmV4QmkqxaSsqUwUyyF4JcvnfvSWwkjFbBJLfkWAKSOcwg9DnFDJ7VHzBNz_NAReXaSmJwD_xADhfeTlYzh7-CN4_oOpSuwhkjnfSstcsoYfC4aL-jEaN38ZedCotzUnjhdE70H7DuQa9MrwSechKutVNSGXoShBEM9RberLKqP8Ei5tClZfb4bk_xbhQEEq3vz3NV3FbWHJDvB4qAplLjP3U4MkzrG12SzqhCUeMeIUhp-ytr1kgax_Xh6vD2bFaYRN80pQFqsIzEMRkmy0_LmwOMSdttsHYjrdbABZDB3v6EfEbxhYleF4aKcyZs9e1CoPztWE9dzmoC8wXEfnYajus156g7IJn_L5uIc0II0q6F6Plfijl5jjR3HI2QhNpRJTpLa1VlSvV96LfHT9x7H9AQcBpbq00F7FJ87ORyWP9XgdVk62Hc2U7CJzhVyZFWknDApoDGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4ed0fa89.mp4?token=tJ8gRpSXFaqBEyzkv2zMosiQJn2ZSUd6APGiTPMOSBYEVIh_AceIS23rQYe0Nm_6_ys6eY63fCzyeHiGuFLCfsaIukkJk7c-0MX3gaSJIxglOBICJK7J5iTdkbYOH598HeXVI4zyEKQrXqaOD3U0Lt_pgFZV77gRvbnFpcgSeQahBM9MbhWgoA044yiKYwfs2grxxc5zn5qrU9j7QqywSYHBhHZooUckTmV4QmkqxaSsqUwUyyF4JcvnfvSWwkjFbBJLfkWAKSOcwg9DnFDJ7VHzBNz_NAReXaSmJwD_xADhfeTlYzh7-CN4_oOpSuwhkjnfSstcsoYfC4aL-jEaN38ZedCotzUnjhdE70H7DuQa9MrwSechKutVNSGXoShBEM9RberLKqP8Ei5tClZfb4bk_xbhQEEq3vz3NV3FbWHJDvB4qAplLjP3U4MkzrG12SzqhCUeMeIUhp-ytr1kgax_Xh6vD2bFaYRN80pQFqsIzEMRkmy0_LmwOMSdttsHYjrdbABZDB3v6EfEbxhYleF4aKcyZs9e1CoPztWE9dzmoC8wXEfnYajus156g7IJn_L5uIc0II0q6F6Plfijl5jjR3HI2QhNpRJTpLa1VlSvV96LfHT9x7H9AQcBpbq00F7FJ87ORyWP9XgdVk62Hc2U7CJzhVyZFWknDApoDGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینطور که معلومه بزودی داریوشم میاد وردل نامجو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83321" target="_blank">📅 01:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ناموسا این آرسنالو منحل کنید، کیر زده به فوتبال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83320" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز چنل:
🟢
1.32
🔴
1.26
🟢
1.5
🟢
1.3
🟢
1.34
🟢
1.53
🟢
5.1
🔴
2.4
🟢
1.41
🔄
1.86
🟢
1.54
🔄
2.52
🔴
1.52
🟢
1.58
🟢
1.41
🟢
1.83
🟢
1.4
🔄
1.8
🔴
2.8
🟢
2.32
🟢
1.5
🟢
1.5
🟢
1.925
🔴
2.4
🟢
1.4
🔴
1.4
🟢
2
🟢
2.8
🔴
1.8
۲۰ تا وین
۶ تا لوز
۳ تا ریفاند
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یعنی تو دنیا کسی خیلی جدی علی گرامی گوش بده و باهاش حال کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83317" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKqjn_DiPCuI_NZnTxk0pC_Jbg-xGifdNV_GffIafuAMolhKOMz8OHa5xg6vpsJg676hYSF9201wskUNfpHR2r_zOTRrBBb7QYB2nYiMtzuWuHf9sPhcbjt0TCFAEDvz6cwjz5zqe9vZ3MtCbdboGX4Q7AtZIRIXLOrSLtp1ff1CLrooJpMobzZL9rB3mq9OS2lFu9JUw4IegL_urUxbXyuAZ_BNMxxcXgemFc48penMXOIVwnUCk21-prYXjIjAPzn5LI1eeKP-hwMGTFvqpG-LrQawlzK1tmdEVneTv4DBECgKhaPeNzVGSWOgYqfRLrmO3WgsO-DaohgLeP7puA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این استوری هایی که از علی کریمی پخش میشه ۹۹ درصدش فیکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83316" target="_blank">📅 21:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBtOsowJO14JaN6Ww4O3OfR6Y6F3a5Q3oYW84NVom8k0w62dPwcVH6AmnAM1hOorPCyqPZNUpJVevhYzKiKwJNHlkYkbog7v5rcQn_Htn2NHn5sXxRMsqBnfykaHkkfxlBBdDH8q3KXAIhJhSLtLgjAmeJRjHiDqZaO2_KRWgdXnrSAODnm5XRRH95TOR1svou1qersU56ld4ry9ZqlfBlpaEJrdMP6SpC9tbW6IfnCNhXl9Oc4Hy9PD52rfD0x2Zh2xcqvtME3PbIzEhQzjn-dpa6Ln8Kwg95RWaOf6ietFD6BQOdSp2FFd201Z5oT2CW1TKstNgD4R5fq4eeZtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83315" target="_blank">📅 20:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83314">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=fWgORZ4hCdJ6lzogcyPOfWfo8lppoDcMCpbfF2hdf5TFOg2_tQRJjqPr2FYQgfRHWdPNJ_gQIaZS1wiVPHgvcbAOWUie0idsbLOz4rLwL1z85fJ0VeoYx_z9aEuxv8kX2eaSYU3Nvibof1QVJ5C5qzP5AAxxGMDBuK0_jn_CNut2NfgxfpDVpNS5fr-KJHsCcK4DxzMjRUfCIdaoXJRjKSgF5Lv_M8zp-1IkeiKVm45v4jRXMWWKq0UHFZW3ndK7V4bu4FGpPU2b4RSJEeaJYZX2a-0CTt-gD4sSNZtgOpwpHSkYyjbvIdwY9YD7gn65HNcEJSDmoWQDHIX8oUPPKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49da2cdeb6.mp4?token=fWgORZ4hCdJ6lzogcyPOfWfo8lppoDcMCpbfF2hdf5TFOg2_tQRJjqPr2FYQgfRHWdPNJ_gQIaZS1wiVPHgvcbAOWUie0idsbLOz4rLwL1z85fJ0VeoYx_z9aEuxv8kX2eaSYU3Nvibof1QVJ5C5qzP5AAxxGMDBuK0_jn_CNut2NfgxfpDVpNS5fr-KJHsCcK4DxzMjRUfCIdaoXJRjKSgF5Lv_M8zp-1IkeiKVm45v4jRXMWWKq0UHFZW3ndK7V4bu4FGpPU2b4RSJEeaJYZX2a-0CTt-gD4sSNZtgOpwpHSkYyjbvIdwY9YD7gn65HNcEJSDmoWQDHIX8oUPPKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی، شهردار نیویورک:
حادثه ۱۱ سپتامبر واقعا وحشتناک بود چون عمه‌م بعد از اون حادثه دیگه نتونست با خیال راحت با حجابش از مترو استفاده کنه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83314" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83313">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRE1ynebVZdmyDX14K-SWlypUmvg-Z4Y8FFLep3M7ItPb9v-HC_kTuoCaL5kAsAVIXBOq0bWgTlz1lAM525SMtNWH4pWG7JG2YmfmO2XcXmMpwFi2JI5At_FkyDZ4S0gDhfK-5lAVgjEDXyCWGjptPloeuHyuMowS8a6s1KA4LChbO64dTmAUkygW3yrm1DLR4nCk-AvD0ul14I0AM2aFS8Bsma9TkyGvC3Ng_nfYlAhn5p40kprXGCWenkgI2RusDKPO8xXT-FaUnzII9R7Z_2Sr-OhxMsdU0tb_PCwX8RYoK28EOYTwuYbQnTHEJmfSb4pPfRQitUjCrRb84FH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرو و هیچکس کال کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83313" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83312">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-5D3NdOnyBwOeWOC-opwPasOTYiLqsHa7xdwqXltlQORD_FNkLYIVP8tsHW23nyTYrQiyqWJTAXfBT71Nik9e4ZHJnazn2yL1heZJG5hUmHYJlwelmluMAQ-wOH_ItiwyF-5ttrpYO1T22V5HJn4p6AyTX8xE4IyRFJ1NBRJpwWK1atG5r-HoyLvTCyNZDIvr_FU50seBkuDrZ8REXcBSj_8QsYRAsLoFfd-EtAc4cVvqW5zFzjasRzDH5LBFNBVJIhxv9S2Mna8qpnpVPefQj10XjPH3TUi1Be2mK2FmBVW6EFkA3klaB6_XsjkZuKZjZX8208lixdx8Sr9hofCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تعویض طلایی بت‌فوروارد
🔥
🔥
با قابلیت «تعویض طلایی» بت‌فوروارد، پیش‌بینی خود را در مارکت‌های مربوط به زننده گل روی بازیکن مورد نظر ثبت کنید. در صورت موفقیت پیش‌بینی مارکت انتخابی، برنده خواهید شد. همچنین اگر بازیکن انتخابی شما پیش از پایان وقت قانونی مسابقه تعویض شود، پیش‌بینی شما همچنان ادامه خواهد داشت و به‌صورت خودکار به بازیکنی که به‌جای او وارد زمین شده منتقل خواهد شد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/SUBO
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g21
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83312" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83311">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e048011808.mp4?token=StmgDznRA5hXTUmCiNqXmGItWJHAvbz5I6n2PKfi4hZfGU807sYVzugesge4-dvlrmxsIrG54_G74VLk3hRquuD0ktn0rcomIErZ3i0gs7zh2W0LCv4nhNGRuaGbVAx2AWcVX_1qeZVzs15GfYNfGGFj-MwPvkMEpCSsDsmftttYTY0U-l3MVNiBhDaK5c7hg0Jyuun_kbclE6GxXiHy8CqN_yvj5uxnRqAHERCLEc7nN1Z0ofMCOVGX2Mr21V0Oza2arSYNW8Qms1GPnYLrPKwJAEagbETW7CAAkwI1QgdfIku6c3iRvGxkUBXtfMxW0laJ5XXpklNzQa1cyK3TVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e048011808.mp4?token=StmgDznRA5hXTUmCiNqXmGItWJHAvbz5I6n2PKfi4hZfGU807sYVzugesge4-dvlrmxsIrG54_G74VLk3hRquuD0ktn0rcomIErZ3i0gs7zh2W0LCv4nhNGRuaGbVAx2AWcVX_1qeZVzs15GfYNfGGFj-MwPvkMEpCSsDsmftttYTY0U-l3MVNiBhDaK5c7hg0Jyuun_kbclE6GxXiHy8CqN_yvj5uxnRqAHERCLEc7nN1Z0ofMCOVGX2Mr21V0Oza2arSYNW8Qms1GPnYLrPKwJAEagbETW7CAAkwI1QgdfIku6c3iRvGxkUBXtfMxW0laJ5XXpklNzQa1cyK3TVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چی بود
تو سراوان نیروهای سپاه و مسلحین درگیرن بعد اهالی کوچه دارن تماشا میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83311" target="_blank">📅 18:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83310">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGEaoxX8q6P-bsHuKn8GsLPOET9kP0EXCEnjs6zp5pJ3ymeIHPRKe3FrD7927yGXmCXF6WO1GBbBacqq5gbxXBLM7oCRsZ9o3r7NMQyB8_tO83NQX0YyuXwEdbx6-5BTc5_YeKhiOGQRkV5Xy3zFjERid5vU9cOhU12p4numrU4T3YCJPCjU6jGaZo5N0mQSaekrBawxoOBK2cp0nQL_7LCqjTP2zLxyuwb1B6Stvz5hj8N__7mpoGyXaFE5v5Y8VVOgw5VU_1P-6wHxkkTvmL8Hd-cNQaaOblwRjsFl8-7jjtGInecvyjLEOoYyktlDe-CgmAJhbGq6s263YyEvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیت مپ این فصل دیومانده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83310" target="_blank">📅 18:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83309">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkOCr_gnPMY3Jl1wGidrxJSAMd_pcfhJl3-vgVisvNdtC_2OgZma3NfhvmnLMtCkicTpw0wotjw0XwFBz_IOcl7ZmmJWYsYt-PLm0841hIz3jMCml57mzE4AXLeRqAFNtf4qpiVE4x8yvjPVuvaS0K_97mTB50DS2QgPZ-xROruDhSnc0QqewIUJQZehWtSWxR31lR1YrilqGZmaKO99eNfW9yX-aLIMBCZgIp9kHLoxEXlZ6lIJIbx1D0ejIVtasizQd9o_HWt16cpiXZtgzNNQDzS0tQ_r_Tm8n-r_TU9H9L3aLRhLp9ZE6MDr_rcL4TAcEtXZQ7DVOgmjmLs5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83309" target="_blank">📅 18:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6JLVl1KVjWWR3XcHHVC5Izy5YOH37OeKrkV4JRZuylTR4nEhlY7F0zonvQsOex0xB7BjD5yKJ0zMXPp4QFkwBgiC70ftxtnOiaVl2ySaINcLjVc_qIaEIwCU1Co-gAXSvwICS2OVexuNifz6TWKluQolEMyVLhzoy9ppeNNd-wwPemhCLbFqcQPKq1MF5VFnnG0W20M1ple4ka_FIzziyMatm_P0UU_W9kpGqiwksFvFi8x7l0qBknYD86qMVKDoQ5WIVbO17Lhrd6aNJoHpa4TDdNPDpx4iIoHHTYGc3Iw811fkRbxnBBzpqh_fB-UL4oKrL8BTwZuc1xTsZ1how.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمیه یاشاسین تورک میلتی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83308" target="_blank">📅 18:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fJsWYItQrc6u0KSXXTf8JdXUFHPbf3WMn2OoTLkawE7_7iVclr2Tl863nJ2DnGlhzKvptUgm-lhksdtDotKqqkA50vtKBFHMnb6dC_T51Gszy6M5Z5aAwGUf4JaGsQMuxGR3pxsW20cN1MUZ6XOAKvPDkaR537GeSscLpTerjA7aR749YmGWe84nOqSfOhKCRTvfLrRS0yYUGhHmMlKTdN6Hnz90zb8eHBuy0dU8o99jaKnMTIBcwnkUdnE6RpScbzgwyLtR2tN5Rk54c_UgyUDZsIes_GNZLLFyETwP1Ueum_H-B9A3FM4_eRrsoEqtelt0HuV2lDEna4n2I7GGTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370c15519a.mp4?token=Np9tQcKFrQ0kEmKd33UwpkMlz7OvMkjNC3Q455D4fvIS6dqg62PtZc6R9TqctUW6lmY0f8Ah0xPOULib_6KXfB7NDr-5aDyX8snA93O4x8f8EoZOVWWqDde6FrAUvRJn-0skHrLcUL1i7gZv5KDoNZIvKbfGk-9QpMgm0Ijios1EJNXmN8er1rG1LlX1nzsGWMaiBGr5WsLe0rh-zqhHsdqCZTpZ51e9S9uWsl9D6emqYPZ7xC0xQVkI4ehnTlm4aIXU-o0qAGw6UH_wpwkq98CaHFAgZ4pbC9L2woud8FbETNN0R2MzwzfkUsosXSUhk7EfqXhVt31sn2op-g-_fJsWYItQrc6u0KSXXTf8JdXUFHPbf3WMn2OoTLkawE7_7iVclr2Tl863nJ2DnGlhzKvptUgm-lhksdtDotKqqkA50vtKBFHMnb6dC_T51Gszy6M5Z5aAwGUf4JaGsQMuxGR3pxsW20cN1MUZ6XOAKvPDkaR537GeSscLpTerjA7aR749YmGWe84nOqSfOhKCRTvfLrRS0yYUGhHmMlKTdN6Hnz90zb8eHBuy0dU8o99jaKnMTIBcwnkUdnE6RpScbzgwyLtR2tN5Rk54c_UgyUDZsIes_GNZLLFyETwP1Ueum_H-B9A3FM4_eRrsoEqtelt0HuV2lDEna4n2I7GGTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله بلاخره یکی فهمید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83307" target="_blank">📅 17:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پسر یه بار نشد توییترو باز کنم چهارتا آدم تحصیل کرده و سیاست مدار در حال دعوا کردن سر مسائل سیاسی باهم دیگه باشن، هرچی آرتیستو ورزشکارو بلاگر تاریخ مصرف گذشته اس افتادن به جون هم دارن از طرف ملت باهم جرو بحث میکنن</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83306" target="_blank">📅 16:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f927888.mp4?token=uFHx2K3gXNgAtv7unHXX0CFEUZTXOSJ9Z5-331Yx0efSDlQ71ES-XRYev--BTeFVn5jlaoFbXhjZglfqXrALaYcGQ_HF0pbI_n2BsUHCPVVclEcUeoP3tveqILvSy-fY09X6dF-5K7uo31TD9Zze-m4B0PULoBjiUtMVZ4Mz_s2LQWhcEkhQhNhj_Gu1nj15cYN7TVPyVUn5hU6MMgfwYIxewld4U48I-HNi5PNZflT-2a4mK7ELpChFVWourKk81aiFtdq4FSSrtQC4bsF0SmdfeW4I17K1oUYf2wZaQG0qK4XZJ4BrUAgV92ydlAhF00-8t-FZkZe90Rt9PuDtcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f927888.mp4?token=uFHx2K3gXNgAtv7unHXX0CFEUZTXOSJ9Z5-331Yx0efSDlQ71ES-XRYev--BTeFVn5jlaoFbXhjZglfqXrALaYcGQ_HF0pbI_n2BsUHCPVVclEcUeoP3tveqILvSy-fY09X6dF-5K7uo31TD9Zze-m4B0PULoBjiUtMVZ4Mz_s2LQWhcEkhQhNhj_Gu1nj15cYN7TVPyVUn5hU6MMgfwYIxewld4U48I-HNi5PNZflT-2a4mK7ELpChFVWourKk81aiFtdq4FSSrtQC4bsF0SmdfeW4I17K1oUYf2wZaQG0qK4XZJ4BrUAgV92ydlAhF00-8t-FZkZe90Rt9PuDtcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی اینارو حاجی
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83305" target="_blank">📅 15:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=v8zZMNVttx6DnKppC9qW6bEwpOiatximnuJ0b5Sqk2FP9BilloDFfaWLbSrspQv5sQ2dPbS91PlEcQQPl4WmHqt9XMoPanx6myPSfYY6pCzEZuOINRWvGBH8OmcZ_PYRzyD2lIs7qcyy4LgH2b8Xq47DFEBs09tweaLHxDEmeXW2aSpXNc1xGk2ahYjJjhB3d2juWK2ilprmE6GIMQPqiQEXjJALraUI2tUmKjcncFf1j_-dVPJI1zRwpzYCidgpGMvQTrwntADXHMbHohsIv4zzBa0dhh6K9OqMT6Jmp7ZHri4XHas2sDSHeQCORvnfzxu9l7b6n3aI4Z73WxM3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9e4acc8e.mp4?token=v8zZMNVttx6DnKppC9qW6bEwpOiatximnuJ0b5Sqk2FP9BilloDFfaWLbSrspQv5sQ2dPbS91PlEcQQPl4WmHqt9XMoPanx6myPSfYY6pCzEZuOINRWvGBH8OmcZ_PYRzyD2lIs7qcyy4LgH2b8Xq47DFEBs09tweaLHxDEmeXW2aSpXNc1xGk2ahYjJjhB3d2juWK2ilprmE6GIMQPqiQEXjJALraUI2tUmKjcncFf1j_-dVPJI1zRwpzYCidgpGMvQTrwntADXHMbHohsIv4zzBa0dhh6K9OqMT6Jmp7ZHri4XHas2sDSHeQCORvnfzxu9l7b6n3aI4Z73WxM3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر پیر اومد دست این دختره رو بوس کنه نزاشت بی لیاقت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83304" target="_blank">📅 15:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ درباره حمله به خط لوله نفتی عربستان:
ایران به احتمال زیاد مسئول این حمله است!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83303" target="_blank">📅 13:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=AKN-yoZH1laLC-kUla5-yKsXSj3laUPCcHd-yGPmd_gMAQFa899p5wIp7uW2JI6lZgGhI2tG9B5NN026TECOup1fcaFAnQtuCpLMO--Fl5m01NMuUFPSqaQLQIxPAQJ6HwrDUGJfzGKQX-wHf2ox2pn4xTKI9XEbrRTHZlfzEzAY-6bku-ZXImGilxHXa0Tuq4ek6-Nh9_dV5s6CmEDA3WmXzQwzZSwY8dEk0LivYosPbfEWrT_bw1XD_hlC1kdXm9geUj4l2c3-0Rf--L13BA0M-vF282fqzRfnWztexPzJQSU7m3kUc5T1etJmEA2nwcwGq3cMA2Ts5vgSe7pdZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efdf4abb9.mp4?token=AKN-yoZH1laLC-kUla5-yKsXSj3laUPCcHd-yGPmd_gMAQFa899p5wIp7uW2JI6lZgGhI2tG9B5NN026TECOup1fcaFAnQtuCpLMO--Fl5m01NMuUFPSqaQLQIxPAQJ6HwrDUGJfzGKQX-wHf2ox2pn4xTKI9XEbrRTHZlfzEzAY-6bku-ZXImGilxHXa0Tuq4ek6-Nh9_dV5s6CmEDA3WmXzQwzZSwY8dEk0LivYosPbfEWrT_bw1XD_hlC1kdXm9geUj4l2c3-0Rf--L13BA0M-vF282fqzRfnWztexPzJQSU7m3kUc5T1etJmEA2nwcwGq3cMA2Ts5vgSe7pdZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی این چه اکسپلوریه من دارم آخه
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83302" target="_blank">📅 12:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اگه رپ آمریکا به کیرتون هست، باید بگم که Lil Durk تبرئه شده و قراره آزاد شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83300" target="_blank">📅 11:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده جواب هاشون رو ببینید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83299" target="_blank">📅 11:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=Rj1RKMxg7z8Y_BnEOr_qIkr0R4QPF_6vDput9mOflTR6X9QFKb04iMAjnp7yOss1bjcdZ3kuAwttBsI1XvCR0NokPqO8zV-sTsmQHEENId0cAhLuKRiBmM4NGR1GI4N_GF3cVWY0icLH91YCf1JMSLHVQSQ7nxbjAUWf5n_PfBWx7EVTaw6gbE76OYhjz5Ct1zN2iH8uLvnzMmVkzKCQb3td70ZWypLpPu9flHbespJYE4JBTgqA8I6dxhO3SOSFUuJB51SR4EvCTTb1sOab0Ox8q2Lrcaph6LPh5srYFuK2AA9l1mUPky2CcuFt-rxdChHjZNm0pfm8qXkZ-JulLqjog1kIYdObXmTeq6bFT3iTOWy566h0-UqOZkuf4B6s_vbNzRbjZMQd0e54sNIowHXsOILOWlwCozlADlauJ7bdAG9xPrB8ggffJzZbHtiZsKmxw4ebPNJMAYBXib92JVKYlo2CUEo_vvZRYUrN_tBtB6ReXkpsw1a4kFTV6LYGFo6xLKAjdXElle_wdQnjL9mY3UsYz3PD8Ll7SGlJ7t1eNrMnneFH7Ei5EWyn7sYZbOmwDj8_23t8uNRtWlGfU73BGZYsTVm5gvhI-py37HyczgV2ZUfOh1FGKIsAFIvR1ab1ltkIH_8vgpwCyNe4YuWLTveaJGNjJFHs4hWO2O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09e472b3e6.mp4?token=Rj1RKMxg7z8Y_BnEOr_qIkr0R4QPF_6vDput9mOflTR6X9QFKb04iMAjnp7yOss1bjcdZ3kuAwttBsI1XvCR0NokPqO8zV-sTsmQHEENId0cAhLuKRiBmM4NGR1GI4N_GF3cVWY0icLH91YCf1JMSLHVQSQ7nxbjAUWf5n_PfBWx7EVTaw6gbE76OYhjz5Ct1zN2iH8uLvnzMmVkzKCQb3td70ZWypLpPu9flHbespJYE4JBTgqA8I6dxhO3SOSFUuJB51SR4EvCTTb1sOab0Ox8q2Lrcaph6LPh5srYFuK2AA9l1mUPky2CcuFt-rxdChHjZNm0pfm8qXkZ-JulLqjog1kIYdObXmTeq6bFT3iTOWy566h0-UqOZkuf4B6s_vbNzRbjZMQd0e54sNIowHXsOILOWlwCozlADlauJ7bdAG9xPrB8ggffJzZbHtiZsKmxw4ebPNJMAYBXib92JVKYlo2CUEo_vvZRYUrN_tBtB6ReXkpsw1a4kFTV6LYGFo6xLKAjdXElle_wdQnjL9mY3UsYz3PD8Ll7SGlJ7t1eNrMnneFH7Ei5EWyn7sYZbOmwDj8_23t8uNRtWlGfU73BGZYsTVm5gvhI-py37HyczgV2ZUfOh1FGKIsAFIvR1ab1ltkIH_8vgpwCyNe4YuWLTveaJGNjJFHs4hWO2O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه گزارشگر تو شهر وان ترکیه تو یه گزارش خیابونی، نظر مردم این شهر رو درباره گردشگران ایرانی پرسیده
جواب هاشون رو ببینید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83298" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiRc4h138JADidu0SbFcPd-czxMZRBQCEaGyvbkIr7opTvwe6u9dl5a2xLaWBNORFvqTVHdjuULrsHjJL4G8TY4Aii3J8of9aqHOvg14Di2r3oT6HAi_TafYbR89c58AYp3DEA4Nh0Zqu3McxhLLNt59yvKuNsUu3nNBGa9J3Z_nDadV4IK5ZO_iSU_1_edX2-UmeTC-9N1Mqfqa1LRBoFQUcXBMWDqaENhbgEyHmos0kQSUCKWxgmvRZ22z946MDxAGiXD5uOrmxogD1D_Xd80xXgx-89N0Ph3p9Vac-HEfmDRplQcG-WWaqy51KaBZjLMG9QjmC5vwBF9a8wjy0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
شارژ کن، هدیه بگیر! بونوس فوق‌العاده ۴درصد
⭐️
💰
۴٪ بونوس نقدی روی تمام شارژهای حساب دلاری!
💰
🚀
می‌خواهی با سرمایه بیشتری وارد بازی شوی و شانس برد خود را چند برابر کنی؟
🚀
از همین حالا، با هر بار شارژ حساب کاربری‌ات، ۴ درصد بونوس نقدی هدیه بگیر! این یعنی پول بیشتر برای شرط‌بندی، هیجان بالاتر و شانس بیشتر برای پیروزی در بازی‌ها و پیش‌بینی‌ها.
🎯
💥
چرا این بونوس را نباید از دست بدهی؟
✅
اعمال خودکار روی تمامی واریزی‌ها و شارژها
✅
سرمایه بیشتر برای ثبت فرم‌ها و بازی‌های کازینو
✅
فرصتی بی‌نظیر برای چند برابر کردن سود
🃏
همین حالا حسابت را شارژ کن، بونوس‌ات را بگیر و شانس خود را امتحان کن!
🌹
کازینو رامسر جایی که هیجان بازی هیچ‌وقت متوقف نمی‌شود...
🅰
r21
🔗
ورود به سایت و شارژ حساب:
⚡️
لینک ورود بدون فیلتر شکن به کازینو رامسر
💻
@C_ramsar</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83297" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">همینجوری پیش بره ایران میشه نیرو نیابتی یمن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83296" target="_blank">📅 11:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صبح بخیر
مرز شلمچه بین ایران و عراق توسط عراق بسته شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83295" target="_blank">📅 10:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شلتون ست اولو که باخت اومدم ۶ بزنم رو بردش، اشتباهی زدم رو تیافو</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83294" target="_blank">📅 05:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7W2ic-CWxFE0ReToMPLYxkYg1VrR2sG33HffwcvQ5nf1Tbc066k8OIL46McPtqm1KJ9IG70A094KvUke5GrOrUp5tB8urEV5o8Jda9T4dU0nWSU8D8aIg-iIC4MAPlpX3ye9pxQSh8x-v3edz7fhRUDiXsIkvWYuK6r0wu0cNFBsxAiz0YEVuua9-zjLWesRI1Wa_MUZ4qPU1iFuyMx64yrCQV9ABmZfcPAbs8K7KRJoxPByZg0fe6nfjH3JfQx_myBP56jqR_6N0N2BO2HcYozWzsVc69vNZ-Wx0uoR13ntoT0kXV08Azyd0vvGczdleT3nhsGkndzuIymY7topQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلکسیون نمایش زوال عقل با هوش مصنوعی توسط جهان پهلوان کامل شد.
❤️‍🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83293" target="_blank">📅 02:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmndvYNJJPufH04m6qgcg5PQFWN6dbart-V8ZK6b7cRd1PCfdpr5bmBmeniz2WWBbC1CsgcW0AuPmNDtRXiH16Rl4R2hu_BmLXP3K9SdDUkrAnc22NgI_KRyiUV-aJfrf9_GgoGhusmLWKI_zaNBjdm9Ubdt5h298bzwaH045g3Ll2gK9fFBwJpRAGO-J2sW-EhspOCjUhhDKrC97iKs1u3EFnDvChQs-YnNIqCYkoH35T58mlGT1iC8t12chCrM8oU6MEfBlvC8uljrtuq3Llod0403XfPsRSq4UB_L8h1uPcgHNDeKabYZ13XDokiAzLQKUZfYRTYQ8UV9Wi-q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83292" target="_blank">📅 00:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njYuqXBMIlWtFHd47mCHmFRzwLHTHyWxUeQx6oEZym0Tu6pUFu8ojxIJoVbxCqlhR3SVjuGjYyHjW-op1M5WvRa2w2LBF3_8GPtGr0GUxTFFU-fks_Xp7pHC6FyKTPs4Fa-Sm3tmsuQYNxPXByIpl5SOhkDKfi8fMfvmLFpYrDBhWUsmevnL-OUcQHMr71XyAmBcoUxoQeObDfIZBNzBc1Lr-6IaapYt-jrtMq_SzV6CHWXL5YxG-U217wVi95XnpFPj5M9KaGwQ2mGg5L3ULDjUUHhUPuISwDGpyVvuYCR_ibstYrEF_zSe4AnQ1x2dR8BdTg5J_6gHoT2riENZPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پسر تو کون نرو هه با این دختر اسکیت سواره رل زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83291" target="_blank">📅 00:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83287">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شرکت آنتروپیک، سازنده‌ی کلاد اومده یه گزارش مفصل از عملکرد و تهدیدات و اقدامات هوش مصنوعی کلاد منتشر کرده که توش یه بخش راجع‌به حکومت حاکم بر ایران خیلی جالبه؛
این شرکت ادعا کرده که این حکومت با کمک مستقیم نهادهای چینی، به استفاده گسترده از این هوش مصنوعی برای رصد و شناسایی مخالفانش در فضای مجازی پرداخته و تعداد زیادی از مخالفانش در داخل و خارج از ایران رو دقیقا با همین روش طبقه‌بندی و شناسایی کرده.
همچنین این شرکت ادعا کرده که این حکومت، از طریق همین هوش مصنوعی، برای طراحی طرح‌ها، سایت‌ها و بدافزارهایی که تهدید یا استخراج اطلاعات و به دام انداختن مخالفانش رو در پی دارن، تلاش‌های زیادی کرده.
ادعای دیگر این شرکت این است که این حکومت، با استفاده از این هوش مصنوعی صفحات مجازی غیرواقعی زیادی ایجاد کرده و از این طریق پروپاگاندای عظیمی را برای خود رقم زده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83287" target="_blank">📅 23:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83286">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">زندگیتونو بزارید رو برد کارن خوسانوف</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83286" target="_blank">📅 22:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83285">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=M1bTRMKDKUtL3OCEqh0pMIWDgW61CkOAgT8RzR38hLv_mGToEaY1P6t3iAqENU0hc5POpd1sX8XjBGw7WAPxKG9JSr5OnPMi8iXiYwTlfZM_YHKXy6pejI2-VLbR3pSQPbm7sfcqYTtmz7EKM_1DJZckJEMReQeATr_jp8Rb_kI-aIRqTMlMW9XaRuciDQk0PiXFfHsY3650o2_5j3Qto16SqeNgjpWz-Sex-RDbQGgOhVv99HkWwNiudBukZe5OEYLWxf44KvfkMJ7TAFbB8FA4HonZ-uisYkm7CDIR2DW8UiSd7vuiXaq-_aQQMV_-H0ReQYwlx_06kwKcZDPv_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1473c0f40f.mp4?token=M1bTRMKDKUtL3OCEqh0pMIWDgW61CkOAgT8RzR38hLv_mGToEaY1P6t3iAqENU0hc5POpd1sX8XjBGw7WAPxKG9JSr5OnPMi8iXiYwTlfZM_YHKXy6pejI2-VLbR3pSQPbm7sfcqYTtmz7EKM_1DJZckJEMReQeATr_jp8Rb_kI-aIRqTMlMW9XaRuciDQk0PiXFfHsY3650o2_5j3Qto16SqeNgjpWz-Sex-RDbQGgOhVv99HkWwNiudBukZe5OEYLWxf44KvfkMJ7TAFbB8FA4HonZ-uisYkm7CDIR2DW8UiSd7vuiXaq-_aQQMV_-H0ReQYwlx_06kwKcZDPv_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83285" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83284">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PixfEha0PBCbmW3gDNZGMT7x2Fcm86lEtUNjudiS_PR0eIJHVvivO_5pHpcDG5aL70-5aIPeZddmHzJyFjvgwWhql9CWjCtVtvGuGHqIlAeyaQ_A8zpKZ4Xyz9Lhpoh_VL9fpeXyww4OWSrPWgEhET2JVvU6Zl7aeq_g-7hEixKEiZJujP5j8z2I5mGH2UX8Mdju0qoVrHGri-2ddiwH0f_Xf_wJjHAlAFRX2pE3x28cfEXU10_l_Offa1HuT9f1DHbmP9a4Q3bJWFs_qipqafGygxcsxdfagh-jZWcm4sGmuyBSKyRwIllBbdOVRO51g0y59INiio0_GwS8zt0_pncfJckjE1lBMPI_ZwaKO3QrliaJX0cjZ7ywbPYDyDA9lSyuI0ZPFWhkiiZMtSaygquGtoMGfZ3PZc8RdpVNfx0UJL6o00nascS94Ux5gNQXl1_vxRLT7N2XEXQQi2palQKcsd_z-sFi5PXCz_ZgKu1NAUmSeZcho5G7E4FT8kYuCZZN2Bw7JFmeeXM5kPMRUe5m8nIEwkA5MBZYvnHrSEonm3qTAQKcqcPVpHC_gO0FSGLWLY_bN-mJDJ4hVKevchs4pIMcHe2RfzqR6e9s8CWK4mJ2N6OjKdwwZCPQQ0On1RItiLuew3LziKLDDLS8lcI7Kw_2KffzeatY7acjp4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8742f867a0.mp4?token=PixfEha0PBCbmW3gDNZGMT7x2Fcm86lEtUNjudiS_PR0eIJHVvivO_5pHpcDG5aL70-5aIPeZddmHzJyFjvgwWhql9CWjCtVtvGuGHqIlAeyaQ_A8zpKZ4Xyz9Lhpoh_VL9fpeXyww4OWSrPWgEhET2JVvU6Zl7aeq_g-7hEixKEiZJujP5j8z2I5mGH2UX8Mdju0qoVrHGri-2ddiwH0f_Xf_wJjHAlAFRX2pE3x28cfEXU10_l_Offa1HuT9f1DHbmP9a4Q3bJWFs_qipqafGygxcsxdfagh-jZWcm4sGmuyBSKyRwIllBbdOVRO51g0y59INiio0_GwS8zt0_pncfJckjE1lBMPI_ZwaKO3QrliaJX0cjZ7ywbPYDyDA9lSyuI0ZPFWhkiiZMtSaygquGtoMGfZ3PZc8RdpVNfx0UJL6o00nascS94Ux5gNQXl1_vxRLT7N2XEXQQi2palQKcsd_z-sFi5PXCz_ZgKu1NAUmSeZcho5G7E4FT8kYuCZZN2Bw7JFmeeXM5kPMRUe5m8nIEwkA5MBZYvnHrSEonm3qTAQKcqcPVpHC_gO0FSGLWLY_bN-mJDJ4hVKevchs4pIMcHe2RfzqR6e9s8CWK4mJ2N6OjKdwwZCPQQ0On1RItiLuew3LziKLDDLS8lcI7Kw_2KffzeatY7acjp4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید سروش هیچکس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83284" target="_blank">📅 22:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83283">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=Yg3KZgjD1lv9EFBkPNZ_d74WjHRLrJCVYuQGe3MaEXAyTzSPd1nWN7bI7lfVgqWMsTumxmklFGQkBwaZGKTaTIINhE_Gp4FQBzpE1mXem7zyJyGwAKJIrHaCdq4R3OPzzO3SiPRD1mnGIPrECHFj74vCpG_MgwsGCx2ixxPjAPumTwtEwC6ds2jRgo-PfpOqKy1N7X1tCOVbO3rgGa9-BE6NHW4es-sH9sn_rh2-m-pnVGP-nAoPBGjk9V0eF-y6rD601uqaQyaWvMgk9TkmO3X6P-Ecjfwk7elzQlg0LXxZfvv2gh6JhkH_UyWzMvk5xrv2eI5D-tRSnVjF3ggKnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69a6fe9b0.mp4?token=Yg3KZgjD1lv9EFBkPNZ_d74WjHRLrJCVYuQGe3MaEXAyTzSPd1nWN7bI7lfVgqWMsTumxmklFGQkBwaZGKTaTIINhE_Gp4FQBzpE1mXem7zyJyGwAKJIrHaCdq4R3OPzzO3SiPRD1mnGIPrECHFj74vCpG_MgwsGCx2ixxPjAPumTwtEwC6ds2jRgo-PfpOqKy1N7X1tCOVbO3rgGa9-BE6NHW4es-sH9sn_rh2-m-pnVGP-nAoPBGjk9V0eF-y6rD601uqaQyaWvMgk9TkmO3X6P-Ecjfwk7elzQlg0LXxZfvv2gh6JhkH_UyWzMvk5xrv2eI5D-tRSnVjF3ggKnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: هانی رامبد رو من گنده کردم، قبل من هیچکس نمیشناختش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83283" target="_blank">📅 21:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83282">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83282" target="_blank">📅 21:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83281">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3D0OzzRoekvaqCAMoU7tNv0udmVey-1lOcUCsLEkgwPXv393DjAmoNSflcSCOPY4UZcG9nGz3CRIzIgbJ_6O5ONVeknhiyCTuVZ1h-uLBNw958Td_H5XEaN4OqtzdkPVLCUexaBMb9DJb2MFBkoWY4Oa7t-nMVIHyPBfzlWfHAJSqKRg2sseKeTQg2Ubzdm3tZDx95UJEm0t88sBOsULQOr2sKSqj-9-awLZztsG_twPtiO-LH43Hy7WDnIKEsAEkf7XjehEPUCDL4RxhRqBl_2wPKjdZ-E_zBWYjV2eXDt8d9UETRJU4Fw509lY3-iflwvuzjSBFjUwqGy8UZcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین نجفی عجب موزیک ویدیو خفنی ریلیز کرده
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83281" target="_blank">📅 21:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83280">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جدی این وضعیت دیگه داره تکراری و حوصله سربر می‌شه، به نظرتون سیزن بعد از کی شروع میشه یکم پشت کامیونای سازمان ملل بدویم یه ذره هیجان زندگی بالا بره؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83280" target="_blank">📅 20:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83279">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سعی کنید تو این دوره زمونه درامد دلاری داشته باشید
من خودم درامدم دلاریه، دلاری بت میزنم و میبازم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83279" target="_blank">📅 19:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83278">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه سریالی هم هست Special Lioness یجوری توش ایرانو گنده کردن منم کم کم داره باورم میشه ایران ابرقدرته.
- مثلا ایرانیا رفتن افسر ارشد اطلاعاتی CIA رو تو خاک خود آمریکا دزدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83278" target="_blank">📅 19:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83277">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=mUqqLaWTfSdz622WAAHx_8MyEL5BivpSyKWi4d-RygQ01-FwxuU1Xn3j7eCx6WFanQLyLnuKcV3hJ-kcvZ0PswBOrAxWuYaiKMYT_DV2f6naXMRokoRaJUq4wIOFfXbgXcKVoGThaPK8g6V4v3EHfLjRw-MYNzgbvrLAI1OlnUxN33gCRS0OY2PTTeunYT6oZo_naPS94oqva7WOUTOTGqIQu_X-2ROgM1_-DnNsI83j2gQ61Z0AAFrJA2Ke660iowVdvSyosNQ68j2amJPxqIw4ANe5vCTUyI6z917UtKjlZxT0ffp5mPsse8l9QTwzE0oo1BhoaDB5tLdSIsZXyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a6977e47.mp4?token=mUqqLaWTfSdz622WAAHx_8MyEL5BivpSyKWi4d-RygQ01-FwxuU1Xn3j7eCx6WFanQLyLnuKcV3hJ-kcvZ0PswBOrAxWuYaiKMYT_DV2f6naXMRokoRaJUq4wIOFfXbgXcKVoGThaPK8g6V4v3EHfLjRw-MYNzgbvrLAI1OlnUxN33gCRS0OY2PTTeunYT6oZo_naPS94oqva7WOUTOTGqIQu_X-2ROgM1_-DnNsI83j2gQ61Z0AAFrJA2Ke660iowVdvSyosNQ68j2amJPxqIw4ANe5vCTUyI6z917UtKjlZxT0ffp5mPsse8l9QTwzE0oo1BhoaDB5tLdSIsZXyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تجربه شخصی ۹۰ درصد فیلم هایی که تو اینستاگرام معرفی میکنن کصشره و بعد دیدنشون پشیمون میشید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83277" target="_blank">📅 19:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bb5n7U-OQeLVnefTxntF2t7OlCBiawfYHkPY61wKWeSAMNtIjLEImBEc2m-9s4tpM7y27jO1Py1N-9ZpaMUnm6jqxU7VRqSlOvLbr-YfwMF-znDvFmwZUpvCwJD5wXHQoMUAQrkb1jIxDRFwu9gaDO3VUFh_5rB4CvMkBszofp-JAaHwxgJ6tcX9bm4qS3CC7MT6W5eOJg8eyqAAPR-EXQmycJ9j0y1eU8Rm0aJjxoutNM17o5l4ZrHyB6pil9DLE5TW53CQlCppW-1QDUl59KimCvNYfLxbAeePAIgN7LlGGfI29Mx241BRHVoSmmj-lE9Ro9gyO0EPX1FifP582A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیکس چند هفته از تمام دنیا جلوایم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83275" target="_blank">📅 18:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=Z3VPKwndKz4p1GKGPvHePSMjp9qG72sD6Ax2sWpFps0osSh04vGSbwTrWT5RHP82KF0D5uA_b6kxONafyacRnltZAOZArhKSHY7OSooIz-74NLimfcWWr9psxHMh-hw1S64r0rM6dFDzydvxNq7sy-l4guuC8Tlmrelvm7h4nNodg8SwchOho0AJpETkWELBG6B4RXbHgJsKBLJGkLeVAjpvS_nf3j0nVQfp1Z4rotAxVNQERoCAg-c3-NxDjA2HrBs_VPL3iv3gVmTBloq21lDErj4qH5_ulyq-udH5IHkS1paWhYb1SgUuhjQ0rMvisc22e92XAlwAaDSTSByFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edd900df7.mp4?token=Z3VPKwndKz4p1GKGPvHePSMjp9qG72sD6Ax2sWpFps0osSh04vGSbwTrWT5RHP82KF0D5uA_b6kxONafyacRnltZAOZArhKSHY7OSooIz-74NLimfcWWr9psxHMh-hw1S64r0rM6dFDzydvxNq7sy-l4guuC8Tlmrelvm7h4nNodg8SwchOho0AJpETkWELBG6B4RXbHgJsKBLJGkLeVAjpvS_nf3j0nVQfp1Z4rotAxVNQERoCAg-c3-NxDjA2HrBs_VPL3iv3gVmTBloq21lDErj4qH5_ulyq-udH5IHkS1paWhYb1SgUuhjQ0rMvisc22e92XAlwAaDSTSByFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی این بچه چه گناهی داشت که پوتک باباشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83274" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ و‌ آمریکاییا بفهمن با ۱۱ سپتامبر همچین شوخیایی میکنیم همین امشب با اتم ایرانو نابود میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83273" target="_blank">📅 17:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تصویری از فاجعه ۱۱ سپتامبر:
🛬
🏢
🏢
🏢
🏢
🏢
🏢
🛫
🏢
🏢
🏢
🏢
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83272" target="_blank">📅 17:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان رئالی شما برا اولیسه بمالید مالک بایرن نمیگه اینا خوب مالیدن پس اولیسه رو بدیم بهشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83271" target="_blank">📅 16:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دلار ۲۳۵
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83270" target="_blank">📅 16:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83269" target="_blank">📅 15:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83267">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2xQatGzKL2yotUrLhkY9l3aJR-wKRo0szIFK6s7NHjtjKwc6qsyxgjfTjtqgFzXOGJxnfPUpEwEXfSucKSUMOtDf1-Z9fG4lqoeyLCmhtXkxDsbSrFdf9_CaM5aqeQZv6Eo3W43IFNGXEAW5tyeYz4Tm4orwIQwe-2_MnZLsCcFajqElnPXzlaWJQMRbnA9mVcya3c1c5eocoTb7Om0wejKky0uFwWqsCVpDa6W_Z3fnvydm2d96B424T9y29g_MOLS15BvbktxPYOJTanEdISz2YHExvrX6HwLDHi8Ql4UWRSwyGPF5NSqcXvWGbMVJArpaVDRF2N7t8a1PFfLPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5yNdhyrVIYwbFj5gEqRzW7drOuSvN9xZdhUl1KcQtA9lefXuziul8YkA_0ezxVuCQBtcQnRmkjra3_MUKU2o_OHjnG9TIemHti4BhQ9iPTv2M6EZ9op6dCz-vgH04eW_IlxW9djFJR2g4um2UM5bTLcl7vW2yypM2marbjvgySlH6dU87y5qwT9oNcOEV4bflYddChuPWEe5h1mLq_oxi5Hmlgyx1ovePj0q737qprIk1r_LIsW_p25X5ngZtQTkZNTOR6JRp4HQTERKKo7vSv0bUjz_f3LszJ0qjQuXU2SOP3LhUG9h-165jFzyIO3aAwlJ--0f4lEhyCnuqwWmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدردی مردم ایران با مردم آمریکا همزمان با حمله تروریستی القاعده به آمریکا 20 شهریور 1380
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83267" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83266">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=QuX7KimwQZW0GJ-KOshhxzKW8MxXHSXdNZB1ETyPztLiySoVAuApktcRSZflI1EXDaaLih8rwjNYnHvLSALQIh_8IhKcRaeOShs29KkIbIa7B-mf7-xwuPQyTORyVNYHNmEMj9h0HGcgbZYiIs2j-Nh46n8m1SX76aP7cHHJJYg2rqPj0lBfoWwVbn4r-x28DcJm-H0FcLjpOE5JR2UKS2w4z3MCWAI2iTj8URv69QKZKuN_wm4DlidCLX86ByMZpdqYiQnGsXw9Ik2MKz67bOhEzgrhg8muZ1FRALEu-j-ZWcFe4j_Y2aT4KCg456xX8hnW04Aur_JKoXAlr1TbZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=QuX7KimwQZW0GJ-KOshhxzKW8MxXHSXdNZB1ETyPztLiySoVAuApktcRSZflI1EXDaaLih8rwjNYnHvLSALQIh_8IhKcRaeOShs29KkIbIa7B-mf7-xwuPQyTORyVNYHNmEMj9h0HGcgbZYiIs2j-Nh46n8m1SX76aP7cHHJJYg2rqPj0lBfoWwVbn4r-x28DcJm-H0FcLjpOE5JR2UKS2w4z3MCWAI2iTj8URv69QKZKuN_wm4DlidCLX86ByMZpdqYiQnGsXw9Ik2MKz67bOhEzgrhg8muZ1FRALEu-j-ZWcFe4j_Y2aT4KCg456xX8hnW04Aur_JKoXAlr1TbZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت ۱۰۶دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83266" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83265">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیشب نه در آمریکا، بلکه در یک کافه در قم از آیفون ۱۸ رونمایی شده، تو این ایونت همه حضور داشتن الا خود آیفون ۱۸</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83265" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83264">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8758825884.mp4?token=NbMUxXOM99S9_lWXu7gn_BO_OU8Efnbzefd_pNfs4vhxnKp5wGy_J2gdEfG1JS0jUFGmAJN4iF9yIYYEuM0GUJXi0ImxzKMpxJFNIMr_wGZbNJrd4PvbKHKwVDbxGfig0zeYJznaJZakmgbGo_wLAZdddRYfWmJvABErbtNWut1aYhDspijb5rK_NWmtg312T7UNIb72f-RdthDvSiLl3dK9qi6gZ7O-X9yypPXwrGIjORPSEQXT-bRDQmdoGpIRb63ewaLlT7bzW_boOUF7QDB4k_jmR61CZBbEvH1r6NkBXGd9eKE9W1d4fwWEuORgOm3Qsgqua8GV7gqtDGxaUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8758825884.mp4?token=NbMUxXOM99S9_lWXu7gn_BO_OU8Efnbzefd_pNfs4vhxnKp5wGy_J2gdEfG1JS0jUFGmAJN4iF9yIYYEuM0GUJXi0ImxzKMpxJFNIMr_wGZbNJrd4PvbKHKwVDbxGfig0zeYJznaJZakmgbGo_wLAZdddRYfWmJvABErbtNWut1aYhDspijb5rK_NWmtg312T7UNIb72f-RdthDvSiLl3dK9qi6gZ7O-X9yypPXwrGIjORPSEQXT-bRDQmdoGpIRb63ewaLlT7bzW_boOUF7QDB4k_jmR61CZBbEvH1r6NkBXGd9eKE9W1d4fwWEuORgOm3Qsgqua8GV7gqtDGxaUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو منهدم کردن تونل های در علی‌الطاهر که اسرائیل منتشر کرده
انفجار این تونل باعث شده یک زلزله ۴‌.۱ ریشتری بیاد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83264" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83263">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=qEkgWu4R1yrbnkL9Dxipe3gsMWjsY94NuY8MlpVl7KeyNHQxVzyN_QgFymGkMhtqdu6fw2lylMn9fFrxWiWRx4oJuEhwonTz3otahCSZQNi5HHGyhIkjV3R4SJVA1mtEuCjmmOwbFctSCngDYmJZGiHl6pmPp9Bz7dhh0goB_W2ZzNFuOnIQrM5UOyB04VBfCHuOqdGV8NV3katIeqGjpOkU_gVeZquJdeGYZkOFuCsDj8EJr53xDxUFT2CYH7D_bTe2RiJlvwJeQgcCtSYnr19yNF-olPkkDptE_yKeOILJ9c8q08EvfeyEzHGMJAaKHClg_SmQLoHDWshfD_pzIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=qEkgWu4R1yrbnkL9Dxipe3gsMWjsY94NuY8MlpVl7KeyNHQxVzyN_QgFymGkMhtqdu6fw2lylMn9fFrxWiWRx4oJuEhwonTz3otahCSZQNi5HHGyhIkjV3R4SJVA1mtEuCjmmOwbFctSCngDYmJZGiHl6pmPp9Bz7dhh0goB_W2ZzNFuOnIQrM5UOyB04VBfCHuOqdGV8NV3katIeqGjpOkU_gVeZquJdeGYZkOFuCsDj8EJr53xDxUFT2CYH7D_bTe2RiJlvwJeQgcCtSYnr19yNF-olPkkDptE_yKeOILJ9c8q08EvfeyEzHGMJAaKHClg_SmQLoHDWshfD_pzIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی پایدار کی منحل میشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83263" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امروز سالگرد حادثه ۱۱ سپتامبره، یه دژاوومون نشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83260" target="_blank">📅 09:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83259" target="_blank">📅 02:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV6SftnHryJsX7ZoZaXTe2Bfo_vvEWcD2iw3o0YFV4RaCvzlYvhGI09XX81nOjgT85-FA6l_-d9cGiHNxp8b3qSfKgiEoPnjc8_m2x2kOzlYuh3czFGP3BWl8hXjgKrlvqJfYW1PHULb1XQkltztGpfArlyA632yZ0ZB5ffizVfcKqpq3z2kldusCpItLhVsHEgFz-ZyGTyHDdfNLpQPOa_ul0_fZfO4alQHBN-hwkPHanCQSDgJfhjNId9-Y5kJ_JniIuT_X8QnBIvWSpuyZhoTGf_63BzRwE0lN3iEzFrQ2g6YiKMLdtWbVqnO07Yjn7bUSVCj3cdEg7ycsK-GuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا اعلام کرد به دو نفتکش در ۷ کیلومتری عمان حمله شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83258" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">شاهین نجفی الان برا زید جدیدش آهنگ عاشقانه هاشو میفرسته میگه لیلی بهونه بود اینارو برا تو خوندم، درحالی که اون موقع این اصلا بدنیا نیومده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83257" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8aC-amFYIDVQhiPChZrz31xyx6re_2KMNBOPK5h0OTyshohgsdiK619lfSrTd5yuDhbl5sk4IQd3E_uve95nZ1z6Q3_McWboiYQYzovFIKhNxaf80ORydXaL35la_BbfQuzcSY2XcDZUDJeCOP2hKS1x6AXJikazlnEYvzIXbf3iDwCchIqjz5LYE6y0GkTCNE71WdC9C-GLbTubIxf8cr9K6mYC-3I_nQBUEl30LiWHMLI9F1BW3mAEJmV-eP1bD0WuXks667YwJ8_Ms8Z37KyktFQU_zeiWYuaSeIJfKDyjh8cl25kNCz794wyqlltqCjiauGAQhL3okj6PHOKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا یه باند میپیچه دور دستاش، با اون ۶۶ میلیون تهش اونو بدن بهتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83256" target="_blank">📅 22:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83255">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=RSf1Qo1Y2Xp0SZJZGtC64wsjvyRcaFQThu1UTkpXK6tprVtDFuh1A69bJQM30mWrio3jONHOUxV4bbNgOSefADWc97848VMyOQmVNW-8q8l6DG6tZZf3m5_L7cX5TKTXABFo-jAo7FjZS-as27V5yBF756bazJCppPbnFV6vDLe1IcZuyhI7rxMaje9H2N7CeHe-FYk0NydpPp3rTriihL_Oio3z1eI-xUHX9URn8-x09i_QfQgu1g3LGNM5V-EitCG330gWMAlieumf53L6E3pAz7wsyyi0L9JZTmwGZkcH4eIhmnxZSczrqf4EDC3W8CHL3w6vLIRXrGj0InhKiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=RSf1Qo1Y2Xp0SZJZGtC64wsjvyRcaFQThu1UTkpXK6tprVtDFuh1A69bJQM30mWrio3jONHOUxV4bbNgOSefADWc97848VMyOQmVNW-8q8l6DG6tZZf3m5_L7cX5TKTXABFo-jAo7FjZS-as27V5yBF756bazJCppPbnFV6vDLe1IcZuyhI7rxMaje9H2N7CeHe-FYk0NydpPp3rTriihL_Oio3z1eI-xUHX9URn8-x09i_QfQgu1g3LGNM5V-EitCG330gWMAlieumf53L6E3pAz7wsyyi0L9JZTmwGZkcH4eIhmnxZSczrqf4EDC3W8CHL3w6vLIRXrGj0InhKiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو انهدام پایگاه عماد ۴ حزب الله در تپه علی الطاهر توسط ارتش اسرائیل
پایگاه عماد ۴ بزرگ ترین پایگاه گروه حزب الله بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83255" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83254">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83254" target="_blank">📅 22:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=D8ktcMDPy261-cXKRrUo3NVubdxRSOEdjqWwXf2QQWBhu5SR9iudiPVRBe3IChDAg-52bvmBf7uXxemGkovWnlCVUGr95_SLesym3YNg4cch6FwR_eTgAS7f5tki4gXHqnR94ZX9TUXyKi6MwJTElFW6GFOp8VkpwEj16pFyDvzsMuRVcXQdnthk3HGn2iglMdfWiiICjcdVzWvZGi9MCyzLu_luRKbu8Bo0VgJJH9zAVYBxI_WUcLao6WLF2jqixYCokYKhovvTbrXSgz_YfEUa2EJcRSFqBBmRTWyhU1OB388NdUPFtnXHTdvKckm_LT2Td7_1v6hxbSVBm_Fndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=D8ktcMDPy261-cXKRrUo3NVubdxRSOEdjqWwXf2QQWBhu5SR9iudiPVRBe3IChDAg-52bvmBf7uXxemGkovWnlCVUGr95_SLesym3YNg4cch6FwR_eTgAS7f5tki4gXHqnR94ZX9TUXyKi6MwJTElFW6GFOp8VkpwEj16pFyDvzsMuRVcXQdnthk3HGn2iglMdfWiiICjcdVzWvZGi9MCyzLu_luRKbu8Bo0VgJJH9zAVYBxI_WUcLao6WLF2jqixYCokYKhovvTbrXSgz_YfEUa2EJcRSFqBBmRTWyhU1OB388NdUPFtnXHTdvKckm_LT2Td7_1v6hxbSVBm_Fndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83253" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka1MmCuG-_nXvBo-8HUYQBR4OQ3EM6A1IDB5bLpEVf8y5u8VScZnsAWRyo2qXWRfmtgTF8DOFGNSwg6PaxhdJhpZvqeVDFX9e2d5WLidalcOEMaUkFNzz31Avays-6L_oOw_R1-XGeRUncR6LyZYqHDiF7nczuP6nlZtzz-GwdnMkNydeFyyZkFALJ6OSaN316qFmPUpzWo4ov0IYy8GYRZH4HLkJN7gI1i0WLmPSra6Kpem07fQnMpRkDa7BRv6JGU-VyLzN0I4dGjCU96qDLYu1Cs10TrHPweNxh5kvnrUA4v2DFK7iZJbVypE99H-XBR3IB-Dp4Q_K90TChsDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصخل که اشتباه جمع و تفریق کرده ولی جدای این ۲۶ تا میمونه، یه تورکم بوده گیشنیزارو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83252" target="_blank">📅 21:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXc_PvOX4JdexbhnBN_yTkQllbqQ6hO1jQLcBCHvp7EqKJQRTzU-oZqtFNttVVEfAG1WuLZILw-_W26icyJ4QpCEBl6UFj5TSHYzVzY0PoqXttVK-QNtHgUIID8sUoLBNH1BYa_pQKjMA7uGWq9DWmxfXv_1mITW1PsP_708ZD-f4A8ORyW6xpYzFLPuQG476Z1kg2ZPah62V1CK33BQ7mLmYsEOCkc2z3MDIsgoLU-Z2TjYqr8Eespp9sQUvtrKV4tpAU4DSzCqNj8rGxiVmAtKI9LuI3UyG_pMe7pFrBur9avAvRgv6BvhuIsOBF1HmY8b-TXLZTw8in65V8KWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا مهراد هیدن که با اعضای گروهش فرق داره و بحثش جداست اومده ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83251" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aco7UZ5SfMKJI0QD-ZUmtLtsidENsSqMQYrwu16GQxPLGaP6V6BeDGuoFyXd4UoPRcCBr9y2Py1xNaEVNrfgPecABJMcoZPJu7Q8c-fGotIujxtvKc4U1EOsWjE0NQL-UwFm743-VlyKksns-neNvOxIxjflv-cDA4DHXUTK0gqPZXsI1dH_Q8N8O1mRgAj98eXNuGad8yGm7N2wNS-ovEAFnXUVYIB-OuwONWjmcE3_W_1ryJCFxYCXYY1Ao0tMAYo4pjwJzItKUOuQeLMDQGoP57_wDX23O78GhtsXD0sH43uvi98O80HnHgqQ-9lFtihUSrBQ05TjcMxGlg63Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVCdXdVmSNBXSqWlSheSuOQWbMGQWFHVJkKuldDrvdKUFh9wDzS8Pnwo7Bi-B7yCGcSRK3D37btus5zhmNH_TiUFXX15ov53aP8gAIpgR9Im-xR5pXuc5HN-n3EHpv7k3iTHo2MO7BGJ-lZGAnZ9VrHx8XX3h9sUXgediYobVS4GBjpDRH1wmZWHd1EJ2gZCsV_oHsiLs1vUY5a_R0aKuzv1G3mCoeZJKJi5iQBZKuNvB-1j3HjBMDW_vnHYITV7ndOnsSsq34tb9-6MWyWTCyNDZelAxjZxtxmADVctgb8QxvPM5eqjNPtyNXeyG-9dAgkNQ3LmMy4zOJvZi4oX-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آدیداس با انیمیشن ماشین ها همکاری کرده و کفش با طرح مک کویین و ماتر داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83249" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgihR6rguZj9hoh-rCUBPwVWCGgHvtU4s-5oJ1GIfZOqAsbhEvA-xwtr6CG4uTll6fO_ByGQ1YkGQ1sgvHpr6YiCzMAt2HFChT6FUfWxWge3WqZ0-9gY4c-Su1RZ7xwx8uK1O0YyYYgNc4ggDmL8qgSUc_tUQ-J9rNqL_q5c0YApmvQ3IGfabnnlT3fC_MB6Cq4ZWDNwb0sZ4TWmLAflnLb_089wtflqwcR4hikjusYxAX8ZqPv81edGzmftBaCL2dBSGAPTc8ID0XTzvL3_MDaLyJ-MLpVf_4jB0Sd9mE7iKfHHivEzHozyC_ZVg8pwvSmktHA0VxZoOQ4IpVooAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم دیگه بگذره عکس کیر مهدیارم لیک میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83248" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlkfkQFbjuquBWXvZuUa9HumF65PzkBWT4zYmuRpxaykXL2xF1z54q_p8SNPuDpLY6feHsyssWNc5aLZXh53KIwwQY3IhgJjwcSPfcEyixH7rNtwm49KfNj2jQq15VtPa8O0mkuxDoE9fT4joRY5exV2Xw9N6BGetrgsdap4dHc5rHnpwThRnbHfIR1ege_MvAp4tElV6OgZsOw2gtuYLIVZwbrkl_AAGHHbRhM2W20E54LECIXlCjvPVtDeB-geyXk5V1Sbq4J1IFM6u6kF8ERoql0bL6CbFXpjQa4Eso3ZF1KPkPUqwsHQ0PU4pI1tK5g2Kq368LrOqwhaPTlLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مهاجم نوکای تاریخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83246" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خلوت کنید آقای خمسه اومده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83245" target="_blank">📅 17:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83244">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roohiS6jxqMBejNLfUBkOP6KfSNLMY_9YkMkSNebOkPbwyLpt7jlzrxhSu4NFyo6CFLtIXXsbwuCrvVPFD94zdKoVm2tO0xr06hRZj5U_pDoKla2V6pTmob2IdlJL0Hdfy9hRpt--h-YjX0ScgSJjURJUZCAaWU2Co5O8YA7LAYeub6oXWfrQuFhtn19RJtyMCLN1BdIxjDgkHA6PeNlJPFdmoU3TAD-VP43ipiu0lidUHCZfwMy2Bl2WeK8arEYRXA8MIU04GxixWCYPOaT983Pvd8XrtCyxW8hT84T1yXutF3XezsewbyZikoJDAcQfeMYtWuBTvqmKdeQHmuhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب رپفارسی اینه که کسی که به داداش حسین تی ام میشناسنش به سجاد شاهی میگه فید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83244" target="_blank">📅 16:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=j4A8bL1erkVZAQ_V75cA9tf68Hk5ImPs_0V_5Iv8UT1TNVYkSxbtsKLBa1YDAatR-tCn8sTNzRx1I4vlLEE0KuYSSxpXZW-iOS5KvD5RoP44i-dlst6DhcJBbzeO1tDI6b9GRFZ5Rc4Wu9NoMbsCE-5Ud7yObL3MGq8b9cQv32ZbDKajRN5YJPhiVjohXIkQNOtc5p3E3gs7RFO4mbUMv1t29YTFDayNf3sKreOwnaFvGoRYxomuGfmDo4VNzGED3AvGteACy1wjrvdfkKDqeXT-3JiNrZA6koxNkRvzPcLC8LxEP_jzqkoQAfCCZBy3SJIY90y6tsRZ4tLVidCkyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=j4A8bL1erkVZAQ_V75cA9tf68Hk5ImPs_0V_5Iv8UT1TNVYkSxbtsKLBa1YDAatR-tCn8sTNzRx1I4vlLEE0KuYSSxpXZW-iOS5KvD5RoP44i-dlst6DhcJBbzeO1tDI6b9GRFZ5Rc4Wu9NoMbsCE-5Ud7yObL3MGq8b9cQv32ZbDKajRN5YJPhiVjohXIkQNOtc5p3E3gs7RFO4mbUMv1t29YTFDayNf3sKreOwnaFvGoRYxomuGfmDo4VNzGED3AvGteACy1wjrvdfkKDqeXT-3JiNrZA6koxNkRvzPcLC8LxEP_jzqkoQAfCCZBy3SJIY90y6tsRZ4tLVidCkyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83240" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ولی خب طبیعتاً هیچوقت کسی که برا پول میجنگه نمیتونه حریف کسی برا اعتقاد میجنگه بشه، اسرائیلم سر همین جلو اینا دووم اورده و خیلیاشونو نابود کرده، چون اونام اعتقاد خودشونو دارن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83239" target="_blank">📅 14:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83238">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مگه نمیگقتید حوثی ها دارن بگا میرن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83238" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انصار الله و حوثی های یمن به نیروهای تحت حمایت عربستان و امارات کیر زدن و درحال پیشروی ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83237" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZt8Keq4X_60eo0jItMY8NTWGwAJd0jtXSPv3Rv30DsvUOx5KVwuiOsgu9hoCThrtd9zUGNUOrdWqiDu3XrOiB8K2__McMQ2Pdda7q4mQOrbgh3u9GdPg3E2rKQngjh0tlBlbK0bRyGPD2cNtdMxI9KKzhhmZIZyUT14f2ERLC5SaQHvud8cm4Sz0P-tx6ZQDaFk0k9lL_Fcaqd5V9FSiHzCsJquWW1JlvD_6xL6eTsLQXM2YkES4ceBCSndDjlhGhOcnkWLYSCAgGSVpk_9XdQ0uPk398etShP5hpquSHyHGI57aymIjmu4_JKmG0WIJrVp-ZHyI8d3t0kMad4uog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم نظرم عوض شد ولی همچنان لیلی بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83236" target="_blank">📅 14:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIZ_jgeBA4_ql3ilwRvr_nrdqoAlMaoIcej61I8nMiugp2yfCv1mr4wIJAukx_doBe4hm7IG2A9zzr1iC9zZr_L5E1QoA90pHDEebGnChvYwZZnyR68XDfMzxRYCixn7VgVXdyo6WyGRm_vwRXHIIq5CPNkoVnNQyY-oUb6ZyvtLB3JBSTxM3zvwRrMBDclfC9wp42Z5HytpVRhYBROqAuwEcVcbELCOiShxEDf9DKKlUI_DuI2A_SNk8p5CleIep2AbVr-XrdDqegj8kfGM9I2McBXYtvNNDgajzSQveCfw9Gf-X3H7n6GLoJ0RJWvcO8wsZQnfqzpL4txsI_TNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JT98SDS9bzs5ihRcBmIUCxGBJ__9WAu2NO8sP22GVyjTjfsxiAZLqE_S0285Y0j1iHnGSXBiLgcxKG-kuW6w-6cijAAfgsSYdyyPuYsi6u1lnUUfnQp-vvcenhp6zYjtbRzJfwFJjf_jhgE7VgL0sbIZ4i2_N7sawP_4Wwsf4LYEIpyTY3ELsyRsO8FltMabODlCUWvlo3ddluVEMTejJyAVQ1PBoJZF7juqrw1M30UBOrjQz2xG7pLQ2ZPJZI3ZXelRIyIRMnl8cuPLWHvT_EAGc1mAfMi2pdeUqny5PmJTGGcXKsSNbWTe15w_2soGVXVz2f8hGBzubt06vUD5YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لیلی بازرگان بدون دست و پا اینو میزنه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83234" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الان لیلی بازرگان میاد توییت میزنه این کار شاهین نجفی رو به شاهزاده اطلاع دادم و منتظرم باهاش برخورد کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83233" target="_blank">📅 13:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83232" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUbXqkwLTZ4VqqBH6Y8GJ6tUMxjFLpbpKFkBjACv2ap908zADv2KScAoXyz11xcVZjay87k9b68ZS_YrpkuZmeeFlOk7xyKdvpgtDWF7zVzkWhyEWQqiUnZZzs1AvUz79AdMLSDS_5Eim2Fav-ukw7_hXYR8igAHxP2QmNUC2A8QHFk1aQ6MM1inW5Yiq0fKN60Xbthr1Nxm5i_qKrFPQi0hdIpiTeeWjXMmV0YhMY3H7-MbA8bY4Zob7ejGvOvQRgUBMpAKZvLhP3tEDkl6SZord2Y_psUeF7E56bQyA6_GkmRWrpqUlYKZWXRZuO9ZjaiBAXFbHpFmrACuafuhKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smh0Yq_qBtYiv90sbhGhq0a8UjAtJ9T8sZD2pCIipXDmA4mdWZ7hOAP1qOFBBZEtiRd1giXX5jAVzhgtxetKdmOS_Um80K2C1wP7L4hhHBTsaB0Pxdvj4Nw2CbqOM7n-4bLAefw8cWyk4k0rKUzF80KL-AOw0oUnUDQYcuvuuHu283FrhSdyB6OgfZxNZgIx97Fq9EM4LIjKsGpE-KprwHb9AqEec2Gqn2NKtLpYRpn2bTcyQs8249HOlIxJj847Zd77hJrtt4FOOAOkzfkHPVrK1drK-NSH_W2n-ls8YlqXgRDp9uAnIQUfOz1bQ8pfRLwlpf4y4gxfh8d1fnjeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOco4HniFXPU6XZUQ-6qOWnaHI1LRfAOmoKnHWHMqDoiMA4GFcA6UrzVFS7GZYJIJVzhiQi92jaVIbzXCMhepeAyCJHAHBmFAxQzfIWiA3UDSg_YuWbxFaWKhn1IN4ONHokahKYtH1NIHFWtpTY3a2BOvq7wII_Igw9fr2w0WOtce6avS9pbYacjkyANNnFoDCBIF3kq0bqeJFtWSw-eSfjwGCEuFDBjR1GsiZ2IMjW-h4HqsLLQZEjI-QB7iApSEsJjtYsPnntSqlcAA2pf0iAEKPo8yjYfyk4WjUGp4zh5kTHF-T8qDoY8TauR7sOLMgEBK4iUsvDfqEks3IkfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IN-bVPK3NdAd6yA35Pj5XE_XmCtKr_KDa3LNjyLs6uI4eE-LvaOS7R_rzRSLF4LWGhH5Vh0Nl0kpklJkExtFeSVC81lx5BKDYuvBmZVs6oVX5PtelsZ9WLgbGOA6O954wcxkV3shsgH-Nd_Kktv6e-u4ElwGzcdqacH3YxDpkksQfCDGZhmJVZLLXhQa4jIPsHR1ypWEkzeR3SXn3ASu9o81ddl254ACUH7x7PwATjCDqaeAOud2mWv5PzTWpD--7NANQdqVNfrwQsqAc7JVUcMrRYVqf02FjYWQ7KUPFlFORYd4QCmg6ve3XfhJctvv0sKxTqgg35TcQniOxONYDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83228" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83227" target="_blank">📅 13:17 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
