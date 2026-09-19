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
<img src="https://cdn4.telesco.pe/file/lQ5eBmZuy9sQEKPD5kx9_Zxf0N-ahKEH5AjJHktRR2BCeqUO2GcBQdnx5MM6oVoc3lvpgG7SUYqn2iFsNUfdO4Qu0v6I-zOzcHTGRZZLjtcS9Qn2BTQlYBsdqYSX8tkQy_4x3kRX8DV1i4_B5hsY6NJWAincDByEs_d2dSP9_dY137SE3p_ww3irBvbL0N9vVhgr1316r3gZfRfC0-xnEGEpRAzGLnu8x0wNPO7nn4DDMvElCCbp-4VzkmzX9aUfNl-FQZLV3zmn0IIQcUGiLNAAMzMMfOuRN63zk4kHrft-H_D8Q7z2RTsuIkAWy14OmHCnoKddMrF1d_5IWPx0Ow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 249K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 05:53:03</div>
<hr>

<div class="tg-post" id="msg-83754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1PRcFKJxxrcfE39jS5VrQpWnLpbPBKKabBeXBNbQ26QB_KKsJEOYIyTz6y4TH2LSQlIFj0BmNo__3MNaIlfj3k_t3Y8odj62WtHy-IODADnLC1U25T94cTCEiN8J7S1NxhLCMRb-3pHUWAhu0KxVepj-Q9zMMBBX1nH12GwF93nbPNw2WQ3P6aqIyhuAga7pZrZBuDQkjWaROenoHnrr-mFYUmKofdANu6sw9Czk7Jg-0o7QEBNuR7RxAIyXcpytmjglFLdobqcy-jKLg4I1Eu_R7JZfhcP6tCvZVaZ0LXdZd8C9gLeI4ZHqNhZnAS1N6s7Xh_UNHcbUWV8SYaGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/83754" target="_blank">📅 02:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دیگه کم کم آخرین باری که یه نسل چهاری سوپر هیت دادو یادم نمیاد(اگه کصشرایی که با پول پخش کردن ترند میکننو سوپر هیت حساب نکنیم)</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/funhiphop/83753" target="_blank">📅 02:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83752">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بهداد اقبالی زنتو گاییدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/83752" target="_blank">📅 00:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL2lkd3HoUNfFUW1ne0K81aybXnVAS30w4CdAV5LOwUuWDsgarRli8wWEcoiCCBrYg7yx9QYosLZ1JF3HqRQPcrphIK1fdbxhNiEya0cJ6ZWXniP3x1sReR3QGV6ovMuw3XPHuO1ljcBXiej1aA36DkR13vSJgKhgWA1SZgBQn_OxfILIWhbPXZ6FUpfT1NrWm2-f7xEA1yEtBrt2REaFQO0Nrm6XYuz3RcAF5V8j0z4HiSaIDp49VgBjEYVe4_NrVBpxTXDITiCFFnrlzT8LRvaur7iIh4Q8qr2AamiLUPwtCqdBragWUvBznCJMRQX-FUjyVVzLny6JC-86I6QBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83747" target="_blank">📅 22:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83745">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83745" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83744">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8926315b1c.mp4?token=SDWtOtD8fdRFVRGDPjtIc8rbeYvD-3aZRWvSzVudvMwNNFSejpY8ltzmO6bPuaaps1TMZgwrzgEDLfnqKv816zBPhZBcrDyzln2AZek8LE58dtjDMcN9ltHf7bgK2yZhxc1aNHVUSUx773ZIPNKa705sKqjL4CsVLx3KmlITNCWk3iplVuTAoD0ijVguvaWELlrckP6wreuAfSOZTN823yDJAH8CJ9qL4JJMj1YTe4fPSKTEEINSzlfsCX5rEDX2onduriRFZQw8TIB0caEoiaFCSHlF4AfZm7uEO1f2DFs_uXZeNOyw-8VWp1ti0-wQ_FFqL9irnqLA4ZQt_YSJtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8926315b1c.mp4?token=SDWtOtD8fdRFVRGDPjtIc8rbeYvD-3aZRWvSzVudvMwNNFSejpY8ltzmO6bPuaaps1TMZgwrzgEDLfnqKv816zBPhZBcrDyzln2AZek8LE58dtjDMcN9ltHf7bgK2yZhxc1aNHVUSUx773ZIPNKa705sKqjL4CsVLx3KmlITNCWk3iplVuTAoD0ijVguvaWELlrckP6wreuAfSOZTN823yDJAH8CJ9qL4JJMj1YTe4fPSKTEEINSzlfsCX5rEDX2onduriRFZQw8TIB0caEoiaFCSHlF4AfZm7uEO1f2DFs_uXZeNOyw-8VWp1ti0-wQ_FFqL9irnqLA4ZQt_YSJtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83744" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83743">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVlsqeEx_tG0tsUonRKRWa0xZSkgUQy9KfIDJ29poT6lGj2XEkndyeDJ5ShucJkeEv1M9pz2hqYpfeN3Xb-nx2DqG1-GvGurqgfM5MBRyf_-HzzY9vhu3H9Z-256zvL0XVg8e-nHOH-YKCuHIDxlGj5Dd-nzsVm4wP4U-meAvoWCLS4iaegKyP4ewj5t9doY3y4S6fZklYAyK4bCCfcncNxgieLDjw6_wINrfrjfS-7hwUIUjBL7yCjh2XZmxA9kgrFR3mHrWouhe6gz4VFkd1m-Ykoj76UxGtSdkoLXHQ7a6RY9oixdYFbWuTDpvArHPnejp9W9AKUy7cUhtCaPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب وقتشه که پنتاگونو بمبارون کنید  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83743" target="_blank">📅 22:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83742">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پوتک به ده تا رپر دیس داد دیشب
کی جوابشو داد؟ ایمانمون، تنها کسی که پوتک بهش هیچی نگفته بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83742" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83724">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83724" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83723">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4397dc1e0c.mp4?token=hZaaEBSAUmOYcjHOhPb4nmByZF22XOcadEF9cequt3QAb3NOxjrFBoJyJcQGMpC2lij9-zB3EF-WHSvXdNy_Hczqu0DSdCa0WdOA7JKwIzMGfmtr-S8Np96gq-7YvGQWHD6dGm7ZCR4LUI5Od09uWjCsk-U6V7RDnLwZ2a_-G3Qf0UQogI84opaJgbnUJujFZuyXJyi6c9GnNfptBPwOvB22zI-5YmZTU-GyE_1DsNjZkkQwmIH4xSdhoj_1hCvKhFznqk8V5oFE8rJlwq4fTQvuf8s55Ge8dD6Cju8jcnV3C7_idx0znSnMK6d9UQcSLglPfOt2RMc1eXixqOV7Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4397dc1e0c.mp4?token=hZaaEBSAUmOYcjHOhPb4nmByZF22XOcadEF9cequt3QAb3NOxjrFBoJyJcQGMpC2lij9-zB3EF-WHSvXdNy_Hczqu0DSdCa0WdOA7JKwIzMGfmtr-S8Np96gq-7YvGQWHD6dGm7ZCR4LUI5Od09uWjCsk-U6V7RDnLwZ2a_-G3Qf0UQogI84opaJgbnUJujFZuyXJyi6c9GnNfptBPwOvB22zI-5YmZTU-GyE_1DsNjZkkQwmIH4xSdhoj_1hCvKhFznqk8V5oFE8rJlwq4fTQvuf8s55Ge8dD6Cju8jcnV3C7_idx0znSnMK6d9UQcSLglPfOt2RMc1eXixqOV7Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83723" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83721">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1443105ba1.mp4?token=pBYLsPKKqOtSRUnnqi6lK2JAjAsAaHuVClt1dgWx-dYLAYLiocSyBi5UkwCV-SXXQj2kzV4HnsgzeaL2QF9tyQUTOJWiEYpcaoLonWndEtvVasB-fziKJqSQs7gAuZvC2f32ae8IG-bZH-cnXgkgEZ7M-sD0IZZXjqwc-ea4nHc1kra-lAPam4AADTNuiyb6AqvMFoVn7lHMdaycPHgRD-FsxTmnEzIC5cwDERRaVKws6cyaK1Pk0FLClbafUdB2GSj6RABY4TDGZNumzekURWaO0EC9FAcEY5csXNHAt2S2bCeN-_RZnE4CU1LOn327JEptZDVYcJcJgYXMFj6img" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1443105ba1.mp4?token=pBYLsPKKqOtSRUnnqi6lK2JAjAsAaHuVClt1dgWx-dYLAYLiocSyBi5UkwCV-SXXQj2kzV4HnsgzeaL2QF9tyQUTOJWiEYpcaoLonWndEtvVasB-fziKJqSQs7gAuZvC2f32ae8IG-bZH-cnXgkgEZ7M-sD0IZZXjqwc-ea4nHc1kra-lAPam4AADTNuiyb6AqvMFoVn7lHMdaycPHgRD-FsxTmnEzIC5cwDERRaVKws6cyaK1Pk0FLClbafUdB2GSj6RABY4TDGZNumzekURWaO0EC9FAcEY5csXNHAt2S2bCeN-_RZnE4CU1LOn327JEptZDVYcJcJgYXMFj6img" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83721" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83720">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a3000ee.mp4?token=BFnP89t1vjxYQizpIPPKRR_eRnn5LmysW51S52vUE6800Ne2Z2qfhF9pmpFg93EVil8vk-0USixqQOqs3hMfkyMYYHHzBL6WCOP_bbPEHoGN4gOG3b_svSvx7Vs3SgS71w-VHw7yVpg2OiumSYmKSYApGfx-lHQp9R2KeSZhxhpDDZcA3AM08aTaVbzkeaSIKs9Z2xK2aRbRcwhvjdpTIac8bMGUi7-Gmm7u1ewS50owbOqeaeYS4X3s7GAxN4x2x_q59c3ielYlBPYqzyZGPc85phZIFSjF16Gy77jEVzhVo4uUi-T-Z0L2aXH7CjyUPPnuTyUHGOsRWwBRuWMpFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a3000ee.mp4?token=BFnP89t1vjxYQizpIPPKRR_eRnn5LmysW51S52vUE6800Ne2Z2qfhF9pmpFg93EVil8vk-0USixqQOqs3hMfkyMYYHHzBL6WCOP_bbPEHoGN4gOG3b_svSvx7Vs3SgS71w-VHw7yVpg2OiumSYmKSYApGfx-lHQp9R2KeSZhxhpDDZcA3AM08aTaVbzkeaSIKs9Z2xK2aRbRcwhvjdpTIac8bMGUi7-Gmm7u1ewS50owbOqeaeYS4X3s7GAxN4x2x_q59c3ielYlBPYqzyZGPc85phZIFSjF16Gy77jEVzhVo4uUi-T-Z0L2aXH7CjyUPPnuTyUHGOsRWwBRuWMpFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوروش هم فهمید که تولد ریری از همه‌ی این بچه بازیا مهم تره و همه‌چیز رو ول کرد تا بره تو اون یکی چنلش به ریری تبریک تولد بگه. تیم رسانه بین‌المللی و مردمی فان‌هیپ‌هاپ هم به نوبه و وسع خود، این رویداد استثنایی و تولد ریری را به خودش، فن‌هایش و تمام مردم جهان…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83720" target="_blank">📅 21:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83719">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b843e8143c.mp4?token=K3b-qSacA4fOuvkZsNcR6Vr0-Eb8c7DGMf6oDLcAAfy5LcJ4gXAXexqKMb-zmfFqwdAZo5U9xuQK-RnYumlPg55xq7cRVbGQ3_wErn0MSpo6-oi_DTK2Mn7wDqL6d2XJ19APa0zva-yMZ7rSjcFz4IRDLuc716GgXI4dsjRWbi92aFFChpjPJKZvHNXkJCjQQsQywkx-duYVAG7lGHOKEgFhLRPZfGpqKlJj-Gr3_pOwmnbMbRi4-K1UcpcxRjzuG_Nly0FmVxikRGI9vOPUsMXnhlnM2wrdpaFFjS2oXy1REpjac8El7IJpjE57fycVh9On2xh7tv5QCcVs_-Jw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b843e8143c.mp4?token=K3b-qSacA4fOuvkZsNcR6Vr0-Eb8c7DGMf6oDLcAAfy5LcJ4gXAXexqKMb-zmfFqwdAZo5U9xuQK-RnYumlPg55xq7cRVbGQ3_wErn0MSpo6-oi_DTK2Mn7wDqL6d2XJ19APa0zva-yMZ7rSjcFz4IRDLuc716GgXI4dsjRWbi92aFFChpjPJKZvHNXkJCjQQsQywkx-duYVAG7lGHOKEgFhLRPZfGpqKlJj-Gr3_pOwmnbMbRi4-K1UcpcxRjzuG_Nly0FmVxikRGI9vOPUsMXnhlnM2wrdpaFFjS2oXy1REpjac8El7IJpjE57fycVh9On2xh7tv5QCcVs_-Jw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوریا علاقه‌ی شدیدی به ایفای نقش باتم در رابطه جنسی BDSM با هرزگان دارد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83719" target="_blank">📅 20:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آرتا داداش ۲۳ سانت دیگه دودول نیست دسته بیله، دودول برا همون ۳ سانته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83718" target="_blank">📅 20:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83717">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83717" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83716">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83716" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83715">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu3EZ5htXy3gWmCS6pOOWr_K7NxhEGxuDCFet552NbdJpd3sBVuAgJ5lPGswtKZIkPgcPF9_ihjWqBhHaoNnWgYeI5mN4WpIzhfT-jOOHwiO6NyZCFFDwCGsVWXSregQpfJ9ohw0MJ3mIQNnsSHmoqC62B0n8ecC1hagRLR6TXj8mdAcNouKeCG8LiW7z36hRw0HApLq7vLZJLokv52O5WdOpE87Vn_6ASF2WVCW5mEjtYdYcaBSThC4LvjMzoS0BMEk3J5jQs8Bfg-KYZ5QJ-4ZMqkC8xe1b74Hs8cBHk7pvYGDdCVTjKaVUA1qCMQGS5xBTdjcLMXx_QJRS2O5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83715" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83714">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سال ۹۰ یه آلبوم سولو داد واقعا خفن بود</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83714" target="_blank">📅 19:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83713">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83713" target="_blank">📅 19:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83712">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WanuxHNyINX6OamkQS7RrxkDde8U706mG4g87PujNy31Pd2mjbwONHmGYOPEeI1xJK7tP42aWVo_Dx5eYOaeUHEFY2yR14bGRCH8oWDg6NXxFvsTUruUPoJOZLsx0YTkbx_iWqthZxsDcxtgW4TxPO_0VDGER_A9fB70ZrJOlnJM-LtepzAmJ7dVQxqlRLRsTHgqbKYpGFdUEbamE3HL4pptY0aRzBX6UfAbw-4n07bWCTPP5GpVtnaOd1FYiCuuLzW-7Vra2MYcbtxDNHxCs8-6DUzv9Qbu-w6F4fjgrWOV0mLGhExfCdTy7rta5PaIabEo5r2yc40hPUsOFEPXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83712" target="_blank">📅 19:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83711">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgCuwnVybAYjZYDxmHHsMWJfTBOXHXzFJpAk9Lwex7S8hm86zqQd0AmtcK6ATAonJb1T6bvoLdqyDUjCVCyj4fYQ8AUADpI_tViLYaKL9O83A_tH2haP1xzf0bFRN4QdSVGmk91cB3hC7YmAVeE9I1rfQiFrU75RRNmuLvMF6J_Dz7W7OdQLZvomLVygIRbBhynqrXbzBYq66z94wVD_FMlzxbbb1b5wStZcvu3qSzWnyRJwYPFTWZmc2Q1y1FGdkVcx7cFNXuUzj7uKk04alEoNCYldbgv9xVfbxTnFkwZ9-VgCt8BHP2b_Wn4w1r2L4MPvyE3sJFDmp1juRk5t2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست جمعی روانی شدید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83711" target="_blank">📅 19:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83710">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مصاحبه ها یامال یجوریه که بیشتر از خودش برا امباپه میماله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83710" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2JbWL9xKfYt-tCWi5tyk_sfOW7VopImwQQsCE0Ih8QMN7JskdXzGIqs2L8_qT7sovq4o9rcwsz-JLv-_W37Er6G2CtvF16JlxXAwIAWIttUTT40a2deiezy21LpmHlgYh_nqtt-sE7mF5SeDWzOpdW9jNg3B7JNsrkXezCECVifbivr1p9iVwCHF4eCK8voe-R_zrhjlyTLH042mAmZempDhWknX4-k7lllpChlq43o_E290tkJTEs57YSJ5vyJ9ObCXYaDAIFLiUcZWTLjYYwvqiy2Ek1aCgEL0mZ7VvrCPR5S2TdfuvUL-g1FXPwtdfutThYt1RQ04tUTM5GR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااین اوبنه ای رفته تو رابطه؟</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83708" target="_blank">📅 18:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lb62JxgB9JbEw1dZy51rcoPw2viENlybyg2yd8MIxc4HyxBogXY2twPHuRlB2tNlqyKUzbz9N6SQl4xfBq61sCp-ve3wV3VxbyqeUf8zH_hVeUYRZeF8doQTtgPhSzGJiCUj_EET9gB7i7ogh0ifiCddLIzqX_NsjzVrdvlvKbXsKCxlYaOQVv3GX92cZM41zlRMBgVXu7cPOZW1ZpcBsRWLaBdzoshEaniEatFA6T5dVinMWQ9Z6JLxK4gFxCj7fAqYQ7KzMTRv5wUQhhzzvc0VBGnIIIMb4LHoxC3-XiacW8I_FdEHixmjJV6150oaNzCg2iQNfxR68MIgP1W0iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر پوتک همین دیروز با اسباب بازیاش بازی میکرد پوتک ویدیو میذاشت ازش، کی انقد بزرگ شد که بره تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83707" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkMahLaoBIarAF9gREJh3NDZe3Lw7qsj6hS6QQaBGtEoEf4RY-R0-5Ch_eaDL1KQZMkxbE7GI7e3Tmnr2V9xWJxz0sNMu_v7WvND7L-rQNtb71kuhfTkhEZ37MqNG0pgaOgIoRb36yxnGn3zqmP8IeGCRt7Id3PgwvoOc3NoMvQHSXJxxlgBEBYeGu6Im0GtIvpbvpngNHRNJAiXVmaRswYSqBnk8lyPaTk6v-ukutbiq-YriPO1997H2kGRYOJapF0cGyh0UosQhIHTCIRhmXUUOMdJkPQsSh4Q25ksB4xSCM7m5yYduwEE3QYPYynTk3YaNRRs4oTzo3gLP1beug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
27g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83706" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دلو به منم پول بده تعریف کنم از ترکت</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83705" target="_blank">📅 18:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzOH1qT-uSRQ4v40GQ25tPv1HERIj3eGwBh2h7ta9odGxk7TVafy3ihpqtKhSsr2A9drAS7Ff0cxeeK_hA06xpg0ODyEsciDuH21G2DhvE86p6y9E2bL3eO5-qu1tzYsMTvn_hbNhZ1PFeSR03bJWEiAoBzU9ipZa8azdarbnvFosy5D_HE5KLS7vahrWRtC2RWrw492Puck3grh5e37W9Ht4M3zV_3qcWu6CIxS2-rKJ_OJlPSfRR-3YVCQLO7o2XkpTpO3B5WPdOqOfiRiZZ_YE_P2NhEvgxBdCzBJAmEbyR6hS2XpGqdXUqYp58n93LPxF9m_gFIxuzRJto6S_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام DUH! ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83704" target="_blank">📅 18:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83701">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1dY4jH0Mtwh6ucW7BajgaTEfPatmh3aW-RCCQx2fN0KPb9-LYAmWEH2P30hO89oPzYCFlXrssPgCRnnJMXEGUo91leGaqdL5q3Di6OVDBtvY4QMGmFEHzCTDGvamL1Uxuw9UR_-bNF2_tuB38cOc6Dmp9sDzwYeZvhcJWK_TSJumWn4Yy8BBnzkms_-hiRo9rX4nObqpjcK450-0AQ-YwZTKqcdss-iAmjdqMwUZSEvvxSBSMYSyStBIBtq9crN3dY29qIHcfptYwZKDSS0TyTNKdLkdJKQ9wgJ4N6G7YCTkM0UkvmyHzo_4dCdwNL6ekwBSrcSu-RTFIF7BTNTFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا انگار داره آینده ای که نیمار پسش زد رو زندگی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83701" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83700">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترک جدید امین تیجی به نام "قلبم نی" منتشر شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83700" target="_blank">📅 17:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ome4hTbySaFfZ68pHQ6n7bvDXEnRxnbYS8kXNUa6X7roiDXSs7wImIBT7mtiF-uKqPWCj26VS1MuEIVauqkwbIQeNun3ZhoifukYAMFy4mH8LIO03GSJgXM0cTilMKAL_-5Uas1hc9lhbjn3bITc2UBMegHJUU0Ik2Bla6syHX8tMHnry3UKMBMct1dxnyHESUDV3uOLOVu57SmpTYnJfKhcY8cxWfWy-MpQIusMwycQ4iSalp9d5ziGhqissmEEhACiQTPjr5D8kzA1KkyGXvSVgUNcvhl3Lp1MZaD5Ib-On2FaB5G9If7ICTHygX6-n3yV0s9-g5BeEk3qeEuUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید امین تیجی به نام "قلبم نی" منتشر شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83699" target="_blank">📅 17:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpGdfRVje6_CP-YobtGBqEn1plIp3KSyEEnIzRwaOBHEDHlOpEko913IdVQOJELgye_kRaAZiY2OCmA84CmqSSnx2FSCOx1mdMlxC73rM8QmZf1w-YmNHL1ZIoQ1mrT_lGmwnXZSdwfwlp-RcGwEQissO7O-JjTTp01tKDIwjcxZ0deAon6YZ8qsdrC09I8KUnTGcRpHXNbVu31WdtMmmkG7JIzZDI35Lm6KT7weSzFOYNkv0S6r4HUmHq_XjO_bTX-4SYFDZPRQfK_crKrLhmDjR_bxNuCFAWAIuf4cbVJWBicLpNwGun3MZKmlredWB1csnZ8rAuK7EVpRm9kVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر خونده پوتک: واقعا خنده داره که شما احمقا متوجه نیستید با این کاراتون باعث میشید پیج من بیشتر دیده بشه و فالور بگیرم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83698" target="_blank">📅 17:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UipKYZnV5kzk6XM1kxCDL_AGJCxY-cnpSHB8nhfd3Kwip4rXlEPtJdizEtEVc1tBPk8VRUCefpVWfALcpah6HLW1Rg7Adc44JOhLqcCUSuXurZrNNZlx6xAn_dXi7aKhNTSXkxB5hSP1Vn3JkSNQCPm5d6kqZugCIcnhCPGBQsXcI9iFwnrtwlx0h1f-Mkt4Erv7M0GJ5ImMEh3fsT44JyOeMlnx09zDdeLt5EMQsBSWfEBvtXRkikYuPa9jrC5zAlVb4jK5ZgyRVL-Hfs2f4ACgv9gDMn0c7empicXtzSzTkkOLVpFzZyeR3YcsDuUCtjm5dD-Th85yCccA-Ktn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلان ماسک: «یا باید ویدیوگیم بازی کنید یا احمق بمانید؛ فقط همین دو انتخاب را دارید.» این اظهارنظر در واکنش به پژوهشی روی ۹۲۳ نفر مطرح شد که نشان می‌دهد گیمرها در عملکردهای شناختی، مشابه افراد حدود ۱۳.۷ سال جوان‌تر عمل می‌کنند. این مطالعه همچنین ارتباط بازی منظم با عملکرد بهتر حافظه، استدلال و سرعت پردازش اطلاعات را نشان داده، اما ثابت نمی‌کند که بازی‌کردن مستقیماً باعث جوان‌تر شدن مغز می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83697" target="_blank">📅 16:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l89JEI0nRunJXoNKTf8pSfqCgud9UKbhupQic40-gLiBCKcqFytcnt57_VfhMsuLv6yHTwZkrH39HotEH1JKTjYPtPsjdbU0wdG4pTjuUsfH6ANw3YoM98JPXJUQeggO_xY78m80xl3X9U0_CGslglz5LQud4PQ1bG8KXsfKTUK-wka3aCFMu_8Zooche95E4dj52BI4wDS36CuYnrMEcIp11w9vQSKD-RiRrs60-u6_2VPuyzm-gBGwa6_vU0hm1LQvkf8B46s7Z-iiE58oW0yZurDMFxOqCRbrNxsla5dddcRbMIeBtBMQqr-TpOPB7VC_QBODqRjCGBPy6lHeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5f4b92ce.mp4?token=VU7cA-dBhcIKCU_LBCHCpTHihWJ3lUjsBQkeXYRW0LOm_QR8J5HOVdkcpNBEm1RoQ_6J2m71GcTrQbvFivX3ChcqSkoK7tlRukr45OMf_Xob7X_zM6cwET-0FPqJJNCaK3CiLUHtupT1ICZORIwTXe4Ri2wsnZm_KJNp0NUwfX4wf2PTHyU4QP_5y6Eaa6c2f6eCtPcorjAhaQyTx1uVi6VkGqopb7L9KDxu9SUOpf_Jv3t6x1YNYbe7TUJ5QjVbOPg3YM-6-931Ew8xQtQIFbGyXzXJyoWY701jz5I__1jDfVf03s667Mxa1IfiJkUKM_SSPPqfZUzgXhmSxzfvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5f4b92ce.mp4?token=VU7cA-dBhcIKCU_LBCHCpTHihWJ3lUjsBQkeXYRW0LOm_QR8J5HOVdkcpNBEm1RoQ_6J2m71GcTrQbvFivX3ChcqSkoK7tlRukr45OMf_Xob7X_zM6cwET-0FPqJJNCaK3CiLUHtupT1ICZORIwTXe4Ri2wsnZm_KJNp0NUwfX4wf2PTHyU4QP_5y6Eaa6c2f6eCtPcorjAhaQyTx1uVi6VkGqopb7L9KDxu9SUOpf_Jv3t6x1YNYbe7TUJ5QjVbOPg3YM-6-931Ew8xQtQIFbGyXzXJyoWY701jz5I__1jDfVf03s667Mxa1IfiJkUKM_SSPPqfZUzgXhmSxzfvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بازی FC27 وقتی پک جمال موسیالا رو بازکنی، تو انیمیشن ورودش غش میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83695" target="_blank">📅 16:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2b646200.mp4?token=v6wnXIoCvIwKmBUUXDM35FHhEEjcC8Jyxus9Ut3jv3bMgAsi9ee194VrtKms9g63-SSzMYF8Y_0zrnHLMYNt0I3Qv6WFoNx3w5gyXHwiJ1jS7EkIVe_g0P48cySXFq83oPq_-1D_0rt5WB-0GGF00AM9NWcdCqV71yE_JecD7BD7ahUTNtTSjJCclLA9Rlbq-LlzstAmHdcVVljFSWIvnoF9966k46FKiUnZCAQ9_T8-9YnkloKya4akyh-ly_pwoBt3M1fBVP4jhZjlld64vXzrgVsTiPtSZ7UssmUz9eZ3hiuT4V4l3vjefjmpRAJSPM3of8FeEnGY5ZrNYOTTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2b646200.mp4?token=v6wnXIoCvIwKmBUUXDM35FHhEEjcC8Jyxus9Ut3jv3bMgAsi9ee194VrtKms9g63-SSzMYF8Y_0zrnHLMYNt0I3Qv6WFoNx3w5gyXHwiJ1jS7EkIVe_g0P48cySXFq83oPq_-1D_0rt5WB-0GGF00AM9NWcdCqV71yE_JecD7BD7ahUTNtTSjJCclLA9Rlbq-LlzstAmHdcVVljFSWIvnoF9966k46FKiUnZCAQ9_T8-9YnkloKya4akyh-ly_pwoBt3M1fBVP4jhZjlld64vXzrgVsTiPtSZ7UssmUz9eZ3hiuT4V4l3vjefjmpRAJSPM3of8FeEnGY5ZrNYOTTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من به خدا آدم خوبیم نمی‌دونم چرا خدا این محتواها رو می‌ذاره تو اکسپلور من.
راستی تا یادم نرفته بگم آرتا هم گفت امروز دستش بنده، ولی فردا یه دیس‌بک خیلی خفن به پوریا پوتک می‌ده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83694" target="_blank">📅 16:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1seRR9hKu07kLjlZob4hc8ieFFZ3mPiTTc7zHihb0vfOJ9ObPxln2FHtOwp-uVEBHYj7Fv2smmBjtRtsROUGxUiE0KqnmjMoPD1TrEMZbLvc7ZOA598o34uNWS-f9lSy2--OWQ6ljk1OYBnxIXx_ur16ZHFG_83KTud-kvGthWkEye0ThB8NY2Ld20XWQVxetHGujFGh_TbekAuDgyJ0_P9pLJKpSjG6KQc4erTYvYcUsOhaOL3SYWMhh64mGSX8E2XniSXXYxT64i7ZTUYb7DibIpitJllESnwHnx0_A6ponVKfDTxk5C21XVEjygeF5tivYZdPp1AM0HXzep2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب وقتشه که پنتاگونو بمبارون کنید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83693" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14cd46867.mp4?token=SYNhRUGTt0JSFWxwohizutElY2LAYgouXvWQxjSgW0FIp1SVjZF-CJ5opZ3EFvwUR2A6yneD0P9_PUqkdviu1U0xKuT-tCY4xopRlQe3edg1jY0DfiAKfmkzC8HdUBH9FcJQHoASWFqlefR6axZzizeY9tCH6zd8oION-Zm-7kzYlSuLgoT86vfq9Y-SHh351gZDeu3tN_sfArfBYASqpC_VA7WmUq0VCtvcb8FJVckUCYg_hY_uWyrYPQ8LqbCA9NEUsT7Xnngw2Lpzul3Faa7m4gKV9LZS-PY70_e0LpnGyfjbQCT930nMQSfDR06fyJ2z4LGsPWmSzdbvljNdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14cd46867.mp4?token=SYNhRUGTt0JSFWxwohizutElY2LAYgouXvWQxjSgW0FIp1SVjZF-CJ5opZ3EFvwUR2A6yneD0P9_PUqkdviu1U0xKuT-tCY4xopRlQe3edg1jY0DfiAKfmkzC8HdUBH9FcJQHoASWFqlefR6axZzizeY9tCH6zd8oION-Zm-7kzYlSuLgoT86vfq9Y-SHh351gZDeu3tN_sfArfBYASqpC_VA7WmUq0VCtvcb8FJVckUCYg_hY_uWyrYPQ8LqbCA9NEUsT7Xnngw2Lpzul3Faa7m4gKV9LZS-PY70_e0LpnGyfjbQCT930nMQSfDR06fyJ2z4LGsPWmSzdbvljNdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین محمود شوماخر چقد‌ بخت زدس که از سجاد همیلتون اسکی میره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83692" target="_blank">📅 15:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محمود کوتاه بیا ناموسا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83691" target="_blank">📅 14:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83689">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rq-HbOUdEHYeX1lFbjDnhVjWm4AS9iJ1f4PNTECg4qOTGBCcI03uV9ysSznAhD4O5214cn9HC_R8hryG48jQ82LiiDROn1b6MViS99fnNgbVmEdcbNTBk7DTCScPGHSMH0AAQyTtwe9XXDqHs3TnJ2JqGiVHvax_Ly_9ZoLrko53xfmFSsvl0kLmm-UB2vOWKRXzpUNXZefYgzuIg5ZLHy5PwqjzbfXfteRWek1NrH2bpyWkaAIZr_TJyFI955b7Zy0pHBgUSkaGTtHrDdkAB8Xrj8dgoPesSRmWngQY6FMjJ0pim8GLFUgY7obXtAu3Et786SXrQU8KIHzQ_2nzOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKOurTvIXmKKvLSIazsyXje4CcDR1T3imSWCDa60V-NT1_MkxlQdBCMwGF0iwabzkvl78FM-ERYW5lbBsrcqs6ugKF7a_25g5-4OowW9gZLwaqNALoEIhyduRTeq60c9C67CiEaYb89gsBXpmKE1rcnsgGiNaaPt6l6FahyxzyNn1it5MoQYXKulJ2C_PpxFquLhbuYSeFgBM3W1gebFk8yPGCN8rX5EcNkaLDZsVSDGoup1Inh4Cpe3J0TnFL2gNCCUovMNm4Y1A5_M9lyQ59jtmvbbsrlJy-G2AtfFiN46IqA0BEMXDV-feqj0jRIyCWhXlx8U_2vBLYCHZxnSuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یعنی من باور کنم آرتا کیرش از گوریل بزرگ تره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83689" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83688">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیول - الچه
⏰
ساعت ۲۲:۳۰
🌎
📲
برنتفورد - چلسی
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83688" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83687">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpY-K_mR_oe5OaEt3El8UyQzejQ9VWIN1O3mU1d4rY-QsFXDTuf-M1ZRqv0s24cHxeHGS4PSCT7Y6nOx4JoNTKfndhbrkU2BHXGtnXPB1PP5gKzCsu1bSm82RunV770BFjZOmOuADkNimRfEEvd3WKnHLFL_hcMsAD684kbsCDcwhbn7qo9RBZokh3kqIjiHyXMHJnt1Q_-jxcn27XTdVAYdaMC4BtjXebOuhWD2Mu01aRU5YlagxN1NZ7iahtsI-sNqHwz86jcvg8cDjz7Y8W9KkVKXHijfSVEjYJe6-5B9gFh6GRMqulAAEbjyBJp0FZESgg29Y7Nd1FvYIJMekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیول - الچه
⏰
ساعت ۲۲:۳۰
🌎
📲
برنتفورد - چلسی
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R27
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83687" target="_blank">📅 14:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83686">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKmX3e3kAgzMEaKgmXFntgDLYRKxGXmixfQ8nABld642QTjn2fgAayjtEkEKqlH6kRyd-7PchNG7BAo2V8yDX-oGny2hAtgXEZj1lPmCEhMvnHz7PiqaDdi0Ke7bgFtMwyL5w7-G56U5Gbe0PW0dgfE_X3wp4PC_4HqD8t6lS49qkBefqBpFbuIMtCdFw4PnhKwx5qglSZAxeDupuoYUTntIWAcDUu2k_6M1ckj9Xch4n6banRT1uX8SMCObnCUzEnQAoD3QD7JPOjP8ZIO28Li3D1rXrxm3c4QoaWlKZX_f-v8-lIGmVpGcSzvIRSv-_3mj75x1Y7YGV20aMY6p3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور سیاسی مجتبی خامنه‌ای:
اگه ترامپ و نتانیاهو از قدرت کنار برن تنگه هرمز رو باز می‌کنیم.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83686" target="_blank">📅 13:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83684">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/945ef1ce48.mp4?token=YEVItaDbo7KDcbcsSq2I8aDnWlJLjRAyV8HOPcckAci4GHaNYcx9ZOF_jSKB7YJKyuMKSaoR4OnqqB8WTNRbLcAhf1gddlrx14obkt26eFRGVBkMUIngnzNpRlXSNgDdIBwaL_bmFDboaQc0p7lOJIW7GQgHZvM6xiWoD4YaKztBzFzQNfEMb3IcczQc-4-zmj1V7DHTAzxNUcp6-aQP7NFM6RqADkEX4PRtO-97Z5injFbcckyhuJdLzrzQHY6pW0d9zUQaB6to3GuWoxUqIvsO-WDQyuUcSwZE6JiOTqLJrG4SB5KbCdmXdrOJutvD84_1qOef8ZzhxAlfMDCaOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/945ef1ce48.mp4?token=YEVItaDbo7KDcbcsSq2I8aDnWlJLjRAyV8HOPcckAci4GHaNYcx9ZOF_jSKB7YJKyuMKSaoR4OnqqB8WTNRbLcAhf1gddlrx14obkt26eFRGVBkMUIngnzNpRlXSNgDdIBwaL_bmFDboaQc0p7lOJIW7GQgHZvM6xiWoD4YaKztBzFzQNfEMb3IcczQc-4-zmj1V7DHTAzxNUcp6-aQP7NFM6RqADkEX4PRtO-97Z5injFbcckyhuJdLzrzQHY6pW0d9zUQaB6to3GuWoxUqIvsO-WDQyuUcSwZE6JiOTqLJrG4SB5KbCdmXdrOJutvD84_1qOef8ZzhxAlfMDCaOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین دوتا از اسطوره‌های موزیک فارسی برا کنسرت‌های جدیدشون.
کدومشون بهتر بود؟
🔥
👌
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83684" target="_blank">📅 13:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83683">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlTsOaxXvsFF0ENsb5AR4ib53JPTy7LKiuazRFZWc2laakZmUTgWRV20am2RzJmxRFk3n_vNM9slShNDSbjshvbVYAPX9qYab9GrmFTJxRN2vd8wgp7O-fXGosJvn1Wks4AeTTRJs5R8DnvppVrP30fRYFVs7xnr88udevPgt645t1dp0IU8j76zyelFIkfjSHSQTEHT7xlidzR660z_tsveFFFi1xnF4gKAs425XKYqtEglpfZv985pvh4PteN1Qm9M7RsPOib1TCpXstNpxeRcucKX-th6ampmq6XYcj4uxcGeHunm9KbzdNaUvWcUHKOzJfw7BR9dJZwddPuU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Yeat
📋
Title:
COCOON
🛑
Featured: Drake
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83683" target="_blank">📅 10:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83682">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbwp8_yN54rQqaMtVUXPnfMgyy727wK7stxAxY5CcAChsCXHm3G3lp5IgPVmREUZhQ4fFGofpGxdLQuLc5RAPa_87yNCDKDPgkq4XA8E5ZwRwd4lsuD_GEJ0yvk5Z_5v7vGSgs_vb6Tw-yRxFaeuUxd9k5DzxFtpSOuB_l5lUmXTrqYXCx5uA-wTEt-wWkLU9ot_9GcZ5FUnnvjm4zV19bxCnHpZ9U2jqDoq4mxieIUaXnOCQ6g3ASpgf1WaFmqXqkN37HXrpVH73Yt-lkSxkh8a59TCJFnUcH5Bf9TFYiPfGBLMJvcxWoEWJMYBjvSeWD4kaUqiPIU5_noRL1yD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفته آینده قراره به هیئت از ایران بره تو سازمان ملل تو یه نشست سالانه کنار هیئت کشورهای دیگه سخنرانی کنه.
آمریکا هم به چند نفر از مقامات بلند پایه که می‌خواستن برن ویزا نداده و الان هم آمریکا گفته که هیچ‌کس از این هیئت حق نداره از هتل خارج شه برا خودش آزادانه تو آمریکا خرید انجام بده!
معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران تحت سرکوب وحشیانه، کمبود آب و برق و افزایش شدید قیمت‌ها رنج می‌برند، مقامات رژیم قصد دارند به خرید و تفریح در نیویورک بپردازند. این اتفاق تحت نظارت ما نخواهد افتاد.
ما اجازه نخواهیم داد که مقامات رژیم ایران از مجمع عمومی سازمان ملل برای انجام خریدهای لوکس با هزینه رنج مردم ایران سوء استفاده کنند، در حالی که این رژیم ثروت ایران را به حمایت از عوامل تروریستی خود اختصاص می‌دهد.
ایالات متحده به ممنوعیت خرید اعضای ارشد مأموریت ایران در سازمان ملل، مقامات بازدیدکننده و خانواده‌هایشان از فروشگاه‌های عمده‌فروشی یا کالاهای لوکس در این کشور ادامه خواهد داد.
به فروشندگان منطقه نیویورک: هوشیار باشید و در این تخلفات سهیم نشوید.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83682" target="_blank">📅 08:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83681">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jODj7PPgHzUWxI5_M-q9lnwqxUwp0RolFmbDe2UXYabKxy8XcizxBClMfgRPa-7f8E4An6hfQvM3pbIPCIcbrFniyAY7Lr7234nwNM_5VNIiNSHA_7xg5UBan0Q0zlxNG6hkgzk7s44Il15NulPa_1V7u8oDCkKXsbNtfb69UjQJhjmToZl0J2XyLD7Adrcm8J71YdqaIOLaJCvRP_jIZNV3W0ar_MPze6AGj34hW4amz4fuvUcEKtkX3Ou6zXWTkpPoXhM0I2m3ICJtpVO44Gf2gAji7WgNJBtmfXIrrpniNx-pD7yCrVANHPbawdXxj0WIDleoekPOwqKfLG38_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام عزیزان صبح زیباتون بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83681" target="_blank">📅 07:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6UDmPzXdmqXUnH2JtcI2RiNfpHNbNOVELTk8gwzE1bvZiQteo79JgkC7KCecfe0OAUg5eZnnRw8R0t3no__wG9NjG_ddnHf760PczUl2tkWxcaV4ab-zTFUWHo9M8fojH01c08B9b5TyOtw1uNhcT6PNA0TUBDDjEfMfCWGOXsgFtr5Lnm-esT317iGX1Fp0pm2F8H0p38uQZu7mOdFHAqctunycjXNcv7Wb9C2QJMAnnE2LxNmJkg2jlaXBHzNw3529yhOudl9KFT20TbJyOh3JQW_wYkkPPHGeXLpuomcnh1bacLxDY8C4RaZrdX_OL4w5_vTjqIZbpSrSDbC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش اینجوریه که بعد از ۵ ساعت بحث می‌گه نه آخه می‌دونی از چی حرصم می‌گیره؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83679" target="_blank">📅 05:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvSrPVNfO1ekEy6lsZ8lLLgoiIU-ljq_nHllomr0Wv-RZY03sVwqJa2ck6NcZ4hbrovt4sGeUu11gP4cV5TzzInGSkUUhD5nt34fBm6cjNgd7WLVMVE6bBA-elkRHluhNzdzbPEAiFRwb6Sv5Emm3L35vKDvieZZ00Ypli2UOd2QC_TYe77K30ADI_GDl_pINI5ZadFWQ15VbeU4zG4I46pvgaBVR2LpibPfNuQIxM19T7jOwbO0f7vxqYjqTW3x6IHTKXXsgKz_1o_GHp1M1OxsDpGOHkMTdJxeC1LskJ3inJkDGXCGRRHJpNTjR3uWmcyDm7B5Txur36bu15xKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش هم فهمید که تولد ریری از همه‌ی این بچه بازیا مهم تره و همه‌چیز رو ول کرد تا بره تو اون یکی چنلش به ریری تبریک تولد بگه.
تیم رسانه بین‌المللی و مردمی فان‌هیپ‌هاپ هم به نوبه و وسع خود، این رویداد استثنایی و تولد ریری را به خودش، فن‌هایش و تمام مردم جهان تبریک و تهنیت عرض می‌کند به امید موفقیت‌های بسیار بزرگ و روز افزون در پناه حق استوار و مانا باشید.
🌹
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83678" target="_blank">📅 04:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بعد از اون فاجعه اسکم استارلینکا، فقط چنین معجزه‌ی دور از ذهن و عجیب غریبی از طرف دوتا از بزرگ‌ترین رپرای مارکت (کوروش و آرتا) می‌تونست یکم محبوبیت پوتک خدا زده رو دوباره بالا بیاره که خب نمی‌دونم چرا ولی انجامش دادن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83677" target="_blank">📅 04:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVlOwMvH6Ht34yeUCi5uwEsT7RLJWRofrOIi1cRpCzAGIWToR0PKJkg7WqgDkqYpakV5Q-3vz-51sbJNBYso-cQ70rObNQh3diDCpNDmeJe5zfr_y3wKuaoavqsY5wL_GKY_-KxR8n6NQdeFxi1gEdBPAwV8xkWvMQw08Kk7cx31abYkqxFLxqQXd3p1_xayQ0OGtrhdlPL9E_NU3qf1d7sm0cjFSetOIeOBOFSYIpFpI04xRnVnXToq9CqXDzc-FZKRlkAjUhgOlTwvIStmxaDT6A14DVVp8v4vG0KkUYtMhfTwH00Dl9iEZ96vaEIyD3P4_ulXYy9k2v8hVuFOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک در جواب این همه ویس و ادعاهای مطرح شده، فقط این عکسو از آمار یوتیوبش گذاشت چنلش
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83676" target="_blank">📅 04:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfVSYFfuqW-wefKDPSc0BaUNFw3ruQcGP2PV4kXI5rY-esiv9f9GqsWzM0VUlGJDHTCKBw1Go_A9XmlpBuuVnQrWmUhMUfOxRBCngWjIWJAtlI191HrSdfScOe1uDMaqM_Vpd2X5Gp6thCkhryB-XR7IkBrhyRqpu9ZdaU85CcOIREcuVPPzhaCuKjcGhcbLyZG2wOTT0zIanS3zIr8oe4J68thG3QcQz7oQDCEh2zEEBiR_Nm71iT96xeWiXqPcl4NyswS4CN9G1Fhiy78nV-VAC9GVtbPu9eT9lqZooaWDOAJKQzzKzCRS5g8q0NJO0gGOuCETOy7Cv7QWtOc8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو فکر کنم هر کلمه رو یک پانچ در نظر میگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83675" target="_blank">📅 04:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">داستان ادعایی کوروش وانتونز از نحوه تولد دختر و پسر پوتک
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83674" target="_blank">📅 04:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=QytTdvZE5QDYidOzZSbKtaLK9XT6qWSQsjY6B25K72lDf3pSqAuBKFnrn1vI-wqWs-zpT7Py2Z65MQdGWw4k8Bd3A8HR6zEgEi3fhgdpJpQG6po2FJDzrYOMx8rcES751n2OP9ImTomscSiq8c7udi0BD7K5wZotlSpY0y9wscP-vD8Neht0RlLO-onRRQuzUZapLWliBenabj3YXc0RTjxtWlIjWqk4XEl8WyGukAa47dAcE3wqX3f70g94AInJ1H4hCJNucgqsIQJl-5m6IUJvpXmckvjSxpiZYySOjgASeeaGBjTep8pYTLMPBnNnFnIH_VmRWQe2d_CSwzkjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389c5e1170.mp4?token=QytTdvZE5QDYidOzZSbKtaLK9XT6qWSQsjY6B25K72lDf3pSqAuBKFnrn1vI-wqWs-zpT7Py2Z65MQdGWw4k8Bd3A8HR6zEgEi3fhgdpJpQG6po2FJDzrYOMx8rcES751n2OP9ImTomscSiq8c7udi0BD7K5wZotlSpY0y9wscP-vD8Neht0RlLO-onRRQuzUZapLWliBenabj3YXc0RTjxtWlIjWqk4XEl8WyGukAa47dAcE3wqX3f70g94AInJ1H4hCJNucgqsIQJl-5m6IUJvpXmckvjSxpiZYySOjgASeeaGBjTep8pYTLMPBnNnFnIH_VmRWQe2d_CSwzkjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند عدد از افشاگری‌های کوروش درمورد پوریا در این موسیقی: منیجر پوریا وصل است. پوریا با اکس منیجرش لب گرفته است. حق فیت حصین رحمتی ۵۰ هزار دلار است اما پوریا این پول را نداشته است. پوریا موادهای مخدرش را زیر تخت ریچ (پسرش) جاساز کرده است. پوریا به عمد همسر…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83673" target="_blank">📅 04:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=v1K0jFlGJBCAR299XTwAVBTVaYTRz_HlSMO4OsqAMhKTF9s58c8YExGTVTarv4IPZyTQvTLlOxfIkzBqlWaVuBolWq3xicQRRDUH8dCrUOw-_dRq7s2imn2Bp9BfeYP8ZuPAKdKKAATMd5FlKFJnHTJFcQFL9MMGsWhKBDsNDKdq36H07GR98CLHFn7k59t-E_p7NsKIgxCyVHXDlvDlgapm1ftUYXyduiyq14jBhSoa4NDmiVwTDSnfj702NXCzGpkaFAP2-rwf3NWfPA3FMQoonTi2S7uBfgydDD_4KyoVUGoYf1MXJT96TPXLFA6xf7RogzzL8vsEOWlmhoARXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=v1K0jFlGJBCAR299XTwAVBTVaYTRz_HlSMO4OsqAMhKTF9s58c8YExGTVTarv4IPZyTQvTLlOxfIkzBqlWaVuBolWq3xicQRRDUH8dCrUOw-_dRq7s2imn2Bp9BfeYP8ZuPAKdKKAATMd5FlKFJnHTJFcQFL9MMGsWhKBDsNDKdq36H07GR98CLHFn7k59t-E_p7NsKIgxCyVHXDlvDlgapm1ftUYXyduiyq14jBhSoa4NDmiVwTDSnfj702NXCzGpkaFAP2-rwf3NWfPA3FMQoonTi2S7uBfgydDD_4KyoVUGoYf1MXJT96TPXLFA6xf7RogzzL8vsEOWlmhoARXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عجب شب خنده داری شده پسر مدعیان حامی حقوق زنان و زن زندگی آزادی دارن زنو بچه همو تو یه درگیری رپی میگان</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83672" target="_blank">📅 03:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کوروش چرا به این اشاره نمیکنی که پوتک نسل دویی‌عه و اصلا نسل سه‌ای نیست و چون تو خودش ندید با فدایی و سورنا رقابت کنه خودشو شاهِ نسل سه جا زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83671" target="_blank">📅 03:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کوروش وانتونز ادعا کرد زن پوریا پوتک سابقا رقصنده میله یا استریپر بوده و در ادامه برای دفاع از اعمال خود این حرف‌ها را زد:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83670" target="_blank">📅 03:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9B05xfnNqUkf6zJlsaJWVW_aPyrLcq5LqK3496cJOeRVuAg9WptGHQOAbRspsjOp3C9Z_sa0Z64CJaoF6ZZAz53DJ1IEjcoJZdVSwaicBu2jxuEaD229JsVK0NNS3aPep3AyazM7KTZ0x3bH-hjWU1iIx-f5HT3oLtVf7GuW8i0Ts-zx7U5wiAojY5k_XMNz4cfSATI4czYql81V-5K7OpfPL9h5--WPrmLmgakogYtw1eNjwD-L_V2LB_x_poicQMVNLi6APnmRWL3Dsft6uCqdEUAYyAMFDQ5D8dzSB75cydAkWsqSdCPq93SGiqZReXK2zWDe6jCsY_T1tjPCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا باباش ارتاس جون ناموست برو بخواب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83669" target="_blank">📅 03:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83668" target="_blank">📅 03:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaJpIEuXguHLUTXbd0_Zkm3LON19Bw8gprvGrUUPDPJoyzPgFDLugJP-BYmXdlyk5fcBTZl4W44Xt_PJTtTH0H-tRDHfwb0Sen5j0ZLhHzr9U8377x3QYmIUeRezXRPjB0KcrvrB8h1lziq0DL65plsRQb0xuBRhAasYeCSXHb_y2S06uF_XKuz16cXY643Vor19-TJLTVdCVoVXL4jd0atqELorYvCSQhIivu5265N2cYzUyPi5OrIdGRvShoblsVg6hw06YcGSRyeR5qngBTqPQpgqHODvwGyWpf-FpNlWDZGlhYpLYzEAfn4CwvBsuhVhBde2ate5SlptgeRhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش وانتونز ادعا می‌کند پوریا در کلاب‌ها به همسر خود دراگ می‌دهد تا کنترل خود را از دست دهد و پوریا بتواند به برقراری رابطه با سایر زن‌ها بپردازد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83667" target="_blank">📅 03:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گنده لات یک مدرسه رو نگاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83666" target="_blank">📅 03:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mR3_PPU-eacxDYrIyoqWxdkDSv1F3WytZOzKOOCsqhBIShBDdsNWv2Tn0RGyxjn25Bg_iriQ2mw8ZJEi3Q0efmTJzkaPGuPpvb8JU1ZFYZI7vDbZRDLJgJjFjBZqL0I57WnRArynCa7XaWbfIb3NTjmLPMgBQ7vBGcgt8AxE_tJu1tQ_fm1hO5HbsxzuU6vtWtQp-1RvLEXQK78Lf48SQYFfM8DjiFI-_Kr6Ez7wM_EPD2vj6goPpLuYa30MF5sQ52w6P_Hc6QFC5XgCvrU5NmdGklrSk--6aTg_U_bwiZMADGQLsz7QIsZJ3mwOvHNdh40Hu2NAGtR4cJfcqV-PnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saqZqkhmu5Vw6eU2SKvMbt0DZ62DP7M-6IM47-z_OxgrhBawgOcSp0HLXzNvMiXEEoBNIvp76TcFinqKJ2UqpF4m6RnKgXcaYpo9euZn62BLMPulamuRFc0Tnbmb_qoomC_WWikgMRbRsFyqrrW3lohZzH7zAi7b7ojQqAAiabhTABJTH4ncA8QapTMdklCQzF3ufWKRTlEoxNwQeqF-_XvyxDwEZLaJWgIegf3r1zGYTHZOdP5yEqNE9PsWrLJovSjj-puMK1Zx39UruQoouGcdHx4W1-p3TPfD5KJbyOABQB1cdpEIin2N-a5_qJS-_SoIEDsVCRntelrLyDmEGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوروش واقعا رد داده
رفته با گوگل ترنسلیت یه طومار فحش به اوکراینی ترجمه کرده به دایرکت پیج دختر پوتک فرستاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83664" target="_blank">📅 03:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا خوبه دیس پوتک ضعیف بود که این دو تا اینجوری ولکن نیستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83663" target="_blank">📅 03:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83662">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFktwaNHeR1_2pPUQMXJW6o4T-8xYUNHACKHx3Q1pFsnUPnxiHLi2zDhjG0MgNqWPj1A2IGo2kmqtSM1hkr_6ur60kCCCAo49b3Hl0nL0ZkpaTt10YA_FJCK4vZXk1uYXk5VbwEg-m4qIKw0ZITkYdGvHvpTwfaFWQH-u2GNVJ04krceP7okQWEqztGOqjn9i2ISie-vEY0o_lmiLuw8nOfiu1US3Lb7fyF37OvA6NGARsgq007dG9cO638SUtjZFbr8LRvqueGUDXcF57OOHOWLTGBe83q1bDUC_pzzoAsyhaPfOvyuR_cmxoprT1iSh_EeIOyVnym0Ne7-RubmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان من چیزی به ذهنم نرسید راجبش بگم شما خودتون نظر بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83662" target="_blank">📅 03:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نه دیگه نشد داری زیاده روی می‌کنی.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83661" target="_blank">📅 03:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جدی یکی از خنده دار ترین بیف ها(بعد از بیف شایان رگ و آدرویت) بیف پوتک و وانتونزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83660" target="_blank">📅 03:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">میگم چرا همش بگ میپوشه، تو شلوار های عادی جا نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83657" target="_blank">📅 02:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArta</strong></div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83656" target="_blank">📅 02:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83655" target="_blank">📅 02:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83653">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کوروش: من مثل توی مادرجنده نیستم ناموسی بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83653" target="_blank">📅 01:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83652">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تو همون دوران وعده وعید های پوتک، کوروش هم موزیک سیاسی میخوند میفروخت به رادیو جوان
خلاصه کون هردو گوهیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83652" target="_blank">📅 01:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83651">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استارلینکا رفت تو کون کوروش
مگه وظیفه یارو بوده بده</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83651" target="_blank">📅 01:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83650">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کوروش: استارلینکا سابات چیشد
پوتک: مادرت جندس دافت جندس به دوس دخترت خیانت کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83650" target="_blank">📅 01:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83649">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کوروش جان قصد دخالت ندارما ولی این که اوایل ریلیز ترک لایک رو بیشتر از ویو نشون میده باگ یوتوبه که وقتی اتفاق میفته که حجم زیادی آدم هجوم میارن برا گوش دادن اون موزیک یا دیدن اون ویدیو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83649" target="_blank">📅 01:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83648">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRt4bdHMIM0ka1WJs824idOxBoFI7GlRo34yPe_38LadYTAxSw1KuD5Y6mbpT7INurX9-dHjJrS1wlVH86HIdqOIs6LB-3vFwGt02VThiMfzTQR0JWxf0ljhpC_WLZtMb3lATP1BeBaVqL_2NUj-8TOi_SN-hBKnp6MrOAzAPvRHMl8Qt3wiENnD5nVupsJbpEL-4PkqpU4Giz-0V3Le66akt0EI156e6vna6_nI_CVk5us4d5VK2AIxgwLCkXgWnls-04wFdsg-3FJ1oVdTSmhpmtiKWw7eeZjSENBiTbrVewlMKD3g3efQFiX9kwZGMvjWflQLKAp8jkTYWGPqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83648" target="_blank">📅 01:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83647">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آقا کوروش یک گنده لاتا مدرسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83647" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83646">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83646" target="_blank">📅 01:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83645">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خب دیگه بسه خیلی حال داد حالا وقتشه طبق عادت بگیم از بیف ملتفت با تعداد کثیری از خواننده ها رسیدیم به بیفِ کیا؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83645" target="_blank">📅 00:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83644">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SblycIWORvHkyc6hLYamHP0iyW-Ka5MAkwHQbCJqKuztrEBEVRlLJWK_bFxBEF5UKPeVjOyfEneIVLBm-unUpSeUFZ2wuoPMNv5T9wh1U5VKUeVRL7weCImrmeZWUEDaLWJY1fJaXeSxok_5wQHYaCrTqwLfkMdBI7ur9li78LJy3apH68SXXXulMQmIqhnViCAXs9CFAuH4ZVqTZAWj315jK1_1YztXBTFSOYg0auDTdg-J0GUh6q7-voDr73zYnboOO5O3SvGlPcV1FGpwizCeMXseb6LncLJYQ7swhRfr0xN6VO1Z8HBvOCeST41er68T1Tc50q0cAafidlKxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش زودتر از ما گوش داد ترکو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83644" target="_blank">📅 00:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83643">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-poll">
<h4>📊 تا اینجا کی</h4>
<ul>
<li>✓ وانتونز با دوستای فرز و شیطونش</li>
<li>✓ پوتک با ریچِ کصکش گو</li>
</ul>
</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83643" target="_blank">📅 00:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83642">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">عاشق کصکش گفتن ریچ شدم حاجی</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83642" target="_blank">📅 00:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83641">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83641" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83640">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83640" target="_blank">📅 00:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83639">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83639" target="_blank">📅 00:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83638">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آقا اینطور که بوش میاد کوروش به هلیا خیانت کرده</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83638" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83637">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83637" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83636" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83635">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بچه کونی اینهمه مدت بلد بودی همچین چیزی بخونی و ده سال کصشر به خورد گوش ما دادی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83635" target="_blank">📅 00:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83633">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد  YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83633" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83632">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LVDut-clVtvSkeiMmnmIXs1p6qyV0Ibsa0D5mKCUslaIenmHqCqIpwKaVQtDyGpDm_f_a4mzgD2LBr6vLwD1LmTjK9pZPAToLlt1cwCNMR077XGMCHV9bLorxaS1UBTRnyJMlS84PMoK1zNC6nA2XQwQeTVb7xpEAmXOw83_xfSedWSBdBwzPnissliZj0EeVAzxzcVT7fEAYmnX0Cggxz0Q-pbbY7jvbXpB6UvRCCxPAEtJa-XCQAo0Rw-XxMbocJU1soa6A-XnNgT8XwSiDi4k687lNqUplGDb3xqntGflp6VfNvLMTIM6KqAbz7e58-PPvBWY62EFqiXSjhWRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید پوتک به نام "HELIA (YADEGARI 3)" منتشر شد
YOUTUBE
🔴
SOUNDCLOUD
🟠
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83632" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ریدم چرا اسمش هلیاعه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83630" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83629">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پوتک دیس داد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83629" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83628">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H95e_PawhWCkoXwev_Gn78sMB4uBLUzM9t_dvmr-dYKaM-l8O8MM249jbr6ywRnd_SLe0sVONLDYRJbqdCck_NWwXp1rmVHenreHN7RCvB-PFNavbR3QzGE3n8gWnUYBGziMEvVmu-hovaLWCeN-SgzrGx7ZZrkQJSPqaUQ8PNQcxeCAP3D2J66Bnff4zPan3vOvthf9NuBE9Evdze8sAD6JKuD3MlJnOYlCXZ27Uc9AQwZ-Gyl4hU-3M8VSQfUADl7glWghEsJIUdOX08KZMQppqBTzj6p3RL_nQNY7P1hLXLL7lmqbTpDxp6O13jhcYWaFAfPs_9lQGXfjdQXiKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک: داف زدم روی داف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83628" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83624">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شب زیباتون بخیر عزیزان
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83624" target="_blank">📅 22:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83623">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کیرگوزی سمی لو کم بود فقط.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83623" target="_blank">📅 21:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83622">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حالا که جوش خوابیده میخوام با یه حقیقتی روبروتون کنم، بابای من کلا یدونه خواهر داره و اصلا داداشی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/83622" target="_blank">📅 20:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83621">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پوتک ترکتو بده بالا میخوام برم بیرون</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83621" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83620">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محمد باقر ذوالقدر، مشاور سیاسی مجتبی خامنه‌ای:
اگه ترامپ و نتانیاهو از قدرت کنار برن تنگه هرمز رو باز می‌کنیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83620" target="_blank">📅 20:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83619">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اینایی که تو اینستا میگن "من از این نسل نیستم" منتظرن جایزه کیر طلایی بدیم بهشون؟ خب بکیرم نیستی کصکش به ما چه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83619" target="_blank">📅 19:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83618">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هیئت حقیقت یاب سازمان ملل:
آمریکا تو حملات به میناب و لامرد، مرتکب "جنایت جنگی" شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83618" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83617">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgtWJ_ePDNVd5b2In8sDHDt-NeWiwbnQJ_MSpewc8p3UVEdZKj8__YLIogjjxfiwDgcaNSgRB16DNNA2UH8UQuU6pl90bAOVTMQ2Z2tbV0BTQaAUBoscdR9g83IG8Ty93v0G-DDOg2v0HHyw_MxYXB60c_iAo-LSiU_x8jepYdxY3jKwMdB9aCBZSMC2KFDNExiE08_EgKOXe_z1A56go_KrbwbIKaGHFNE4yQrmoaNW4gVcIS1hxpCr5QlRhruW3Vku-go2PqdXy62OsVsHeRAc3FjNgFPbUILLdfapCZz0CmDXmMbTYC6P2sDhf6ISuC4YL8MVHpiczEoHdyP_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی والیبال قطر یه دریافت کننده ۱۳ ساله داره که ۲۱۰ سانته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83617" target="_blank">📅 19:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83616">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این نزول خورا چرا ورشکست نمیشن حاجی هرجور حساب میکنم تو ضررن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83616" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
