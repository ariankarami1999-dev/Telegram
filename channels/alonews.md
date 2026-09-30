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
<img src="https://cdn4.telesco.pe/file/IKvTy8_gV2jvj-MFsmrDB6mECCFRgRIE9HzaI0pRgMjrbH2CV2OnCXQ__nLY9_ta02gKzK45DaTXIUCJMdV69eNORqkAeVG79idMQNN0wka40G81JJ6sGRSnhaDlSkp_zCkDP8OkYRsHs6osXiQ_DHqFQ6mN4HQ_ZlPwA2gN9_ujzcw1z0-MShmXnVjUs6cRbTW6mRxUVJNnilHzLU51XLmu17YCjtiX0b_hR9EE_KxkD0c-CTENUtGaVuz4WQ_FouXMTtzUe6EE5fdsHT2R0yimXC9fI3W5JIyh2V52ONwk9v3YNNKaEca50k9SplocstD2CP5vgYSezPJmv87Fmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-150316">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
خبرنگار حوادث:
امشب تو تهران یه مرد جوون بخاطر اینکه زنش قصد داشته ازش طلاق بگیره با یه گالن بنزین وارد پاگرد طبقه اول شده و آتیش بپا کرده
تو این اتیش سوزی، خودش و خانمش و مادر زنش کشته شدن...
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/150316" target="_blank">📅 00:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150315">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8de0ac9b.mp4?token=u9eFznJEL0XiQnAbc-GTuFbta5RpEzAtbUmUjS3uAzUOKX7jzL03rDtTglxdpNbXpQ5kvxAMciV7733PXwW4QNryVg88KumREZphF6s2f3HEW5wvgwjqOMuxE_Z190QbpHh9KHCwsE1H1Pn7vlcPPXO65w3J7PoF9WOIE3skazvC3ABJf-ME8botZCtFAXz43FKkiAlLYUbROhy--UdTFfE7Ga4GUCJb8hL0NSxs5xdrD_sxTgQCA_K5RSZldGnNh3zWdd1v3diPdl0s6-7SIvd71pnpIzZiZkSZrjUaQhwI9C9qElp0d4DvpNfCni1Ok7WEadwr8DliVDhV0ZW5Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8de0ac9b.mp4?token=u9eFznJEL0XiQnAbc-GTuFbta5RpEzAtbUmUjS3uAzUOKX7jzL03rDtTglxdpNbXpQ5kvxAMciV7733PXwW4QNryVg88KumREZphF6s2f3HEW5wvgwjqOMuxE_Z190QbpHh9KHCwsE1H1Pn7vlcPPXO65w3J7PoF9WOIE3skazvC3ABJf-ME8botZCtFAXz43FKkiAlLYUbROhy--UdTFfE7Ga4GUCJb8hL0NSxs5xdrD_sxTgQCA_K5RSZldGnNh3zWdd1v3diPdl0s6-7SIvd71pnpIzZiZkSZrjUaQhwI9C9qElp0d4DvpNfCni1Ok7WEadwr8DliVDhV0ZW5Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست خطاب به فرماندهان نظامی:
دروغ‌های رسانه‌ها درباره ذخایر مهمات، جان شما را به خطر می‌اندازد
🔴
این جان شماست که وقتی رسانه‌ها درباره ذخایر مهمات دروغ می‌گویند، مستقیماً به خطر می‌افتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/150315" target="_blank">📅 00:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150312">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af73c34e9e.mp4?token=FPnhi6H7UYO2_qRwcMBzxTFqGYD7nmjeemV77CS17nsKWo-b8NqDdMRKpS2BiGIn7bftUn-YX6hxelNSm93QFjnj0COraFMDS8PenPBca8wJAZcG49i0Us798Og-4JN3qHhGax0BZOYnWbMWoZihGouXfXJon6SUXZXorKDNp-Izmf_6d-Rxm-QEM6v0R5N7AEpFcV7luXiW4EPQV9GvLOFuNvPaTQZqb1MjRXKvQOGM8oYQDN4TDvOwGm0sEqNRZjl-dG8WuaTKm_glda_xiS0fFsTwdJupIlLxZg-ZCD_kB8e0YS4lvzku5r_thY5iPyAw98oBHm51behfzSgUPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af73c34e9e.mp4?token=FPnhi6H7UYO2_qRwcMBzxTFqGYD7nmjeemV77CS17nsKWo-b8NqDdMRKpS2BiGIn7bftUn-YX6hxelNSm93QFjnj0COraFMDS8PenPBca8wJAZcG49i0Us798Og-4JN3qHhGax0BZOYnWbMWoZihGouXfXJon6SUXZXorKDNp-Izmf_6d-Rxm-QEM6v0R5N7AEpFcV7luXiW4EPQV9GvLOFuNvPaTQZqb1MjRXKvQOGM8oYQDN4TDvOwGm0sEqNRZjl-dG8WuaTKm_glda_xiS0fFsTwdJupIlLxZg-ZCD_kB8e0YS4lvzku5r_thY5iPyAw98oBHm51behfzSgUPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت آخر‌الزمانی در مرز ایران و افغانستان که تانکرهای ایرانی درحال سوختن هستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/150312" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150311">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb577d26a.mp4?token=gLQrSSJjTB6tkKRE2DXeXCE1c-aO3ZoOgNFO0PjU8SmEh-B_l-8LfOa3m4nVefj3OC-U3d2EWHclpX3mTysPG44WnQTfSq62PKGGx9XD7F1RO-VDfQrR20CyeNZap3U0HxyYOZDlV1t8ok7q2nVIbKh_d_ECChxH0Uj-ejKINLK-RVVg-41ApaPqg6tRdZ8xadMwFtRAfvqwIqqZK_NU3t5VTiMfZkujYS0yZ8tGQOnTyx-J6xIVwd-f_NNDjv-nYNx71KW1XoJOdn6bcrMHNlU8gOqwJnW4mpwdMn1WDcGcGH_-SRLUONSsn4nm9k3ALZGNF5OlhLzGWW9kwJhSIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb577d26a.mp4?token=gLQrSSJjTB6tkKRE2DXeXCE1c-aO3ZoOgNFO0PjU8SmEh-B_l-8LfOa3m4nVefj3OC-U3d2EWHclpX3mTysPG44WnQTfSq62PKGGx9XD7F1RO-VDfQrR20CyeNZap3U0HxyYOZDlV1t8ok7q2nVIbKh_d_ECChxH0Uj-ejKINLK-RVVg-41ApaPqg6tRdZ8xadMwFtRAfvqwIqqZK_NU3t5VTiMfZkujYS0yZ8tGQOnTyx-J6xIVwd-f_NNDjv-nYNx71KW1XoJOdn6bcrMHNlU8gOqwJnW4mpwdMn1WDcGcGH_-SRLUONSsn4nm9k3ALZGNF5OlhLzGWW9kwJhSIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست: رسانه‌های ما باعث می‌شوند رسانه دولتی ایران منطقی به نظر برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150311" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150310">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: پروردگارا، من اینجام. مرا بفرست. مرا بفرست تا با کت قرمزها بجنگم، مرا بفرست تا با کمونیست‌ها بجنگم، مرا بفرست تا با اسلام‌گرایان بجنگم. مرا بفرست
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/150310" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150309">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
توقف موقت پروازهای شرکت فلای دبی به تل‌آویو
🔴
منابع خبری از توقف موقت پروازهای شرکت هواپیمایی فلای دبی به اسرائیل خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/150309" target="_blank">📅 23:46 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150308">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آهنگ جدید گلزار منتشر شد.  [@AloTweet]</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150308" target="_blank">📅 23:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150307">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرگزاری رسمی سوریه: در پی هدف قرار گرفتن یک خودرو در جاده پل مصیاف در حومه حمص، ۷ نفر کشته و ۴ نفر دیگر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150307" target="_blank">📅 23:37 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150306">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ درباره کوبا: ببینید مارکو روبیو با کوبا چه کار می‌کند. ببینید با کوبا چه خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/150306" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150305">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRLrNaCiXaqaTHdJTVMheBgktTCEpiYly_wdikYcdhu0U4ts7H4u6RkVx_HPF-Fs8_oEIvZoxvBeZcXEZHDDsssTHHzaOqVpfwx4KpNbUw9Ldhowofu2QsDDxGbuPMJuURMVFV8gg-q6Ny4ISpqN7Jz1zCL5RhkeJjKgMuAlhf_sYiS2DA9LiVuZvui0pBXIglQgM1-Yt2nlER7skZL9b8NwhceqPtfR9SPAfR7wQmffPvaWCqHBm2FKRVM_gnRVSGcK93t83AjSfZ1IkhwbGa-zbLYCXwKyuGM9dh2bNNySOAwjnakIV3mdDRl6C2eiP98bR7SNpxQD4srQDnKWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حدود یک دلار میخوان بزارن رو چُس تومن کالابرگ، اینقدر کصشعر درموردش میگن،  چجوری خجالت نمیکشید؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/150305" target="_blank">📅 23:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150304">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbaf3d64e.mp4?token=r66nOnxCSoQ1a4mTw97cxxE4TBggiBUgTlcroCSHauEtokNwtrrPW7dmiX_zj8ED0R3Xev2QZQjHOujg90-R-Sy0d2slv6IHxnIHDvZ5ShGNeM8jRqUNJJWRE22iNBCaZSl-1oaZQIWBoLmH4WPjKcuqKz_u77rAd_zeKGZsTpeAbCinywd3y7QsiDa8CMrGvOojGhY9A6L4Kug8tO3OdoPzO2YpVwFxczwaMilZx2H5UsXlrMXFMpnH17_JgaxcSgLChXr1TWfqQL3ZOXh6nuYcOMLX8MC3qaBSSXrbId7qPLxKq066LS6e_Wmylr6CEL9r3OzaLg9lHmpOHHt9VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbaf3d64e.mp4?token=r66nOnxCSoQ1a4mTw97cxxE4TBggiBUgTlcroCSHauEtokNwtrrPW7dmiX_zj8ED0R3Xev2QZQjHOujg90-R-Sy0d2slv6IHxnIHDvZ5ShGNeM8jRqUNJJWRE22iNBCaZSl-1oaZQIWBoLmH4WPjKcuqKz_u77rAd_zeKGZsTpeAbCinywd3y7QsiDa8CMrGvOojGhY9A6L4Kug8tO3OdoPzO2YpVwFxczwaMilZx2H5UsXlrMXFMpnH17_JgaxcSgLChXr1TWfqQL3ZOXh6nuYcOMLX8MC3qaBSSXrbId7qPLxKq066LS6e_Wmylr6CEL9r3OzaLg9lHmpOHHt9VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پخش شیرینی در شب نشینی میدان انقلاب به مناسبت خروج آمریکا از عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/150304" target="_blank">📅 23:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150303">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
نیوزنیشن: ایالات متحده درحال آماده کردن یک طرح ۶بندی جهت ارائه به ایران است
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/150303" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150302">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سردار نقدی: تمام توان آمریکا همین بود که تو این ۷ ماه انجام داد و شکست خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/150302" target="_blank">📅 23:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150300">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93aa1cd1d.mp4?token=Y5rmofsEgr5d8d9zp1kC6jMM8-bFAB8AEO26n9KIQVgVrzfjDE1JFyHVR_q8AsJ-Bp21qFB4sEKoHC63C7ZSOnjhlOkhaqn1UQ0jrM0wkBqgqeHZ8hieBUypSSXNZ7CRpxa5ijWRFBy_b8Xn0euLq1VWG50XOuRHkc8GYaJIE5RQJx5UoXfxWaHqq1FmaYlwzA7EoRMyBV6opiOS3Eh0JkXoKuGiamukdTz-jROC5yKkIf3DbmWTqhNTCGz8JWrTPHOc0AAb2XLhpsZNl4q2eN5E0-uYPZVPKkb4NcE_UJnwOMNzkEPCn_3NhvFFk4m9s6zUrlSwZlQxqHJ9RwXkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93aa1cd1d.mp4?token=Y5rmofsEgr5d8d9zp1kC6jMM8-bFAB8AEO26n9KIQVgVrzfjDE1JFyHVR_q8AsJ-Bp21qFB4sEKoHC63C7ZSOnjhlOkhaqn1UQ0jrM0wkBqgqeHZ8hieBUypSSXNZ7CRpxa5ijWRFBy_b8Xn0euLq1VWG50XOuRHkc8GYaJIE5RQJx5UoXfxWaHqq1FmaYlwzA7EoRMyBV6opiOS3Eh0JkXoKuGiamukdTz-jROC5yKkIf3DbmWTqhNTCGz8JWrTPHOc0AAb2XLhpsZNl4q2eN5E0-uYPZVPKkb4NcE_UJnwOMNzkEPCn_3NhvFFk4m9s6zUrlSwZlQxqHJ9RwXkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ:
مادورو گفت: "من اینجام، بیایید و من را بگیرید"، و ما هم همین کار را کردیم. اجرای اصل "FAF" (Fuck Around and Find Out)
✅
@AloNewd</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/150300" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150299">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دبیرکل ناتو: «اروپا قادر نبود توانمندی هسته‌ای ایران را از بین ببرد. ما نتوانستیم. اما ظرف ۱۰ سال آینده این توانمندی را خواهیم داشت؛ می‌توانیم و باید این کار را انجام دهیم
🔴
‏همچنین باید این خود ما باشیم که در دریای سرخ با حوثی‌ها مقابله می‌کنیم، نه آمریکایی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/150299" target="_blank">📅 23:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150298">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRU9uFu25qfaM0AATmaRCnTYflkOmfpI1HL30pGPBT03pgIEbvXCY-2-oWUWTAb6ewP5dNtycHKEoe3eEGXixWZhfBosN-gMkDV9vA_pKSuBWwKZL5kcwmW4N-L1atrUuBiPl0xr5kgeBLlg_DohZ2lpQPyQMIOAorHUCz-h8z8L-GwQ4nRpO77e8lqnUXfFOAewAC5a1VaB2B-RHAd4oNci_iviYVYEndmmebNjD5R1jpoS_VMZVY68vEtoQ2l2AbgrWaPMpFK5U57OWEo-otnHHKqL2nhMKcXDH5Rv7EUn3guXNqbOz2RPqMdgBNaMKky7khuj7MWWg2RI99eryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه های اسرائیلی جمهوری اسلامی رو دلیل چاقو خوردن خلبان میدونن و میگن اسرائیل آماده انتقام خیلی سخت از جمهوری اسلامیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150298" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150297">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پیتر هگست : ما دیگر یک بخش "آگاه" یا "ضعیف" نیستیم.
🔴
نه افراد چاق، نه افراد ترنس، نه مردانی با سبیل پرپشت، نه افراد عجیب و غریب، نه افراد ضعیف، نه افراد رادیکال. فقط جنگجوها
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/150297" target="_blank">📅 22:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150296">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پیتر هگست : ما دیگر یک بخش "آگاه" یا "ضعیف" نیستیم.
🔴
نه افراد چاق، نه افراد ترنس، نه مردانی با سبیل پرپشت، نه افراد عجیب و غریب، نه افراد ضعیف، نه افراد رادیکال. فقط جنگجوها
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/150296" target="_blank">📅 22:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150295">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پیتر هیگست، وزیر جنگ:
بله، یک کاهش 20 درصدی در تمام بخش‌ها اعمال خواهد شد. رسانه‌ها این را "پاکسازی" می‌نامند.
🔴
من این را "مسئولیت‌پذیری" و "اقدام بسیار دیر انجام شده" می‌دانم، و صراحتاً، کمترین کاری است که می‌توان انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150295" target="_blank">📅 22:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150294">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فارس: آیت الله مجتبی خامنه ای فردا پیام مهمی برای مردم داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150294" target="_blank">📅 22:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150293">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
خبرگزاری رسمی سوریه: سه نیروگاه برق در پی انفجار خط لوله گاز از مدار خدمت خارج شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/150293" target="_blank">📅 22:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150292">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تام باراک، فرستاده ویژه ترامپ به عراق:
پس از ۲۳ سال از ورود نخستین نیروهای آمریکایی به عراق، ترامپ روند بازگرداندن نیروها را تکمیل کرد؛ اقدامی که به‌گفته او نه عقب‌نشینی، بلکه یکپارچه‌سازی ملاحظات راهبردی بغداد، اربیل، متحدان منطقه‌ای و منافع آمریکا بود.
🔴
این تحول فرصتی برای نخست‌وزیر الزیدی و مردم عراق فراهم می‌کند تا همه نیروهای مسلح عراق زیر فرمان یک دولت واحد قرار گیرند و آمریکا در جایگاه متحد، نه صرفاً حامی نظامی، دیده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/150292" target="_blank">📅 22:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150290">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0920eaa1.mp4?token=WXbF9PUBK8sjrsFU32dOw69v0mVodsw1VSD9lWEljIdUwUEEobRvqjXVD8ChDB7ssKAwyPqSaJQdXY6YnPaFdJXPQqQ5zuCQWxfI1mvOs4RgluJ9UPlvu4jRyHUJirFygXDV6YcS8naGT8qROgk4HThPnEfl9_Tm8j8wyn0Z1lZy1iQl_8zUgUMYK_BTteMQxTcJnILrEu7eKjx6GGaFg0RLe8lBWYwztv3f3p_m1JzoWkEKJ2U14O5PUnQF0kLWmek_TC0MXNvPUwTTYIEnNol7z-HpbZr7iaxZMMpBnh3CTI-5AKZJkMSJ4HllWGCfzNegs5M-RhqyjikyZhG0bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0920eaa1.mp4?token=WXbF9PUBK8sjrsFU32dOw69v0mVodsw1VSD9lWEljIdUwUEEobRvqjXVD8ChDB7ssKAwyPqSaJQdXY6YnPaFdJXPQqQ5zuCQWxfI1mvOs4RgluJ9UPlvu4jRyHUJirFygXDV6YcS8naGT8qROgk4HThPnEfl9_Tm8j8wyn0Z1lZy1iQl_8zUgUMYK_BTteMQxTcJnILrEu7eKjx6GGaFg0RLe8lBWYwztv3f3p_m1JzoWkEKJ2U14O5PUnQF0kLWmek_TC0MXNvPUwTTYIEnNol7z-HpbZr7iaxZMMpBnh3CTI-5AKZJkMSJ4HllWGCfzNegs5M-RhqyjikyZhG0bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع انفجار در دومین خط لوله انتقال گاز در سوریه ظرف دو روز گذشته، پس از انفجار خط لوله عبوری از دیرالزور
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150290" target="_blank">📅 22:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
خبرگزاری فارس:ترامپ هم تلویحا از برنامه‌ریزی برای آشوب در ایران گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150288" target="_blank">📅 22:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فارس: ترامپ دروغ میگه! خیلی از سربازاشون تو جنگ کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150287" target="_blank">📅 21:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: ما از نظر اقتصادی از هر کشور دیگری در جهان عملکرد بهتری داریم.
🔴
شما باید اروپا را ببینید. اروپا در وضعیت نابسامانی قرار دارد. سایر کشورها عملکرد بهتری ندارند
🔴
اولین جمله‌ای که رئیس‌جمهور شی به من گفت این بود: «واو، شما کار بسیار خوبی انجام داده‌اید.» البته، ایشان این را به زبان چینی گفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150286" target="_blank">📅 21:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
کا گ ب ( اطلاعات روسیه) گفته اسرائیل و آمریکا میخوان خیلی سریع حمله مشترکی علیه ایران انجام بدن!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150285" target="_blank">📅 21:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ: من تنها رئیس‌جمهوری هستم که حقوق خود را اهدا کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150284" target="_blank">📅 21:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ : آنها همه را در عراق اخراج کردند: سربازان، ژنرال‌ها، پلیس‌ها
🔴
آنها هیچ‌کس را برای اداره عراق نداشتند. و می‌دانید چه اتفاقی افتاد؟ گروه داعش شکل گرفت.
🔴
ما کارها را بسیار متفاوت انجام می‌دهیم. ما از حماقت‌هایی که آنها در عراق مرتکب شدند، درس گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/150283" target="_blank">📅 21:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما ۱۸ نفر را از دست دادیم، اما آن‌ها ۴۵۰۰ نفر را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/150282" target="_blank">📅 21:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ترامپ :  آمریکا در جنگ ایران به پیروزی کامل نظامی دست یافته است. خیلی زود شاهد اتفاقاتی خواهید بود؛ خیلی زود.
🔴
اما با کشوری روبه‌رو هستیم که عملا ویران شده است. اقتصادشان وضع خوبی ندارد. تورم آنها بیش از ۳۰۰ درصد است.
🔴
نیروی دریایی آنها از بین رفته، نیروی هوایی آنها از بین رفته و تجهیزات ضدهوایی آنها نیز از بین رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150281" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150280">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «به‌زودی شاهد اتفاقاتی خواهید بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/150280" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150279">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
فوری / ترامپ درباره ایران: «به‌زودی شاهد اتفاقاتی خواهید بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150279" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ درباره عراق:
عملیات "عزم راسخ"، که آن‌ها این نام را برای آن انتخاب کردند، در سال 2026 و تحت رهبری رئیس جمهور دونالد ترامپ به پایان خواهد رسید.
🔴
ما به سرعت از آنجا خارج می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150278" target="_blank">📅 21:22 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b3d6d265.mp4?token=VBIDnmYSJQZTaEq4PDr8lABBIFfZ4Hcbri7GLABLLLSM4B2pw8nc-LenJwwB9s_4UqR90HaOlSQ2oi0mEhdHExbS1Qe4omLzVLhYT3QYNC4rnV9HBu6uPmpRRdAHlXtOm8H3u6EdYa7BWfNlsdHXTOKhGAMMY-dQ5Wb3tdQJJ0z_fZ96r-k45b0URAq_iw7n_1FypDVU1FiJHR5Wwf1AhTx8hCy6Oi6LziDWH5xHMB0VqCXFm0Z3rRuA-r5cTWFZ8R6KM7X8mnDpn-9bS8IpkmBhGQiRGOH2k-CfFO7aEC6mbNp0eau5bzCGrccaCgutfwJ_yLVgo0mrMhAqWzeWdbVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b3d6d265.mp4?token=VBIDnmYSJQZTaEq4PDr8lABBIFfZ4Hcbri7GLABLLLSM4B2pw8nc-LenJwwB9s_4UqR90HaOlSQ2oi0mEhdHExbS1Qe4omLzVLhYT3QYNC4rnV9HBu6uPmpRRdAHlXtOm8H3u6EdYa7BWfNlsdHXTOKhGAMMY-dQ5Wb3tdQJJ0z_fZ96r-k45b0URAq_iw7n_1FypDVU1FiJHR5Wwf1AhTx8hCy6Oi6LziDWH5xHMB0VqCXFm0Z3rRuA-r5cTWFZ8R6KM7X8mnDpn-9bS8IpkmBhGQiRGOH2k-CfFO7aEC6mbNp0eau5bzCGrccaCgutfwJ_yLVgo0mrMhAqWzeWdbVtidpGuD3jp4mJg3cwanNP7RyjTOEvTbBUzG29W7GhD-EYqt4YzIaCsU4LXZPr_MhPMYq3NN2QtO9LGWsO7YKK_vrZoTL9e41ob4wRUVrpO1-WOKkyPfvVIEABMjzNqA_kdsdTtb36thikIX_8fwUJSkwe4dPg821ppeHk73gsadtH4sWNSrwr-Lr5-sROINPinrA8Ff_G2WFv7j1TPXfutRSYn0Ph7h9ZUF1-c5HD4PtDlvCrmgcRdf5MyYbNMQgSI8koFyUNA1PJIyMERXy96xvD56y8tgi-4c5TqmogTKZHUkZBoBjykajNWqYZN57ko5Lj2IRDHdnwbMQOL2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره عراق:
امروز، با خوشحالی اعلام می‌کنم که آخرین نیروهای آمریکایی عراق را ترک می‌کنند.
🔴
مدتی طولانی گذشت و تصمیمات بسیار نادرستی اتخاذ شد که ما را در این بحران گرفتار کرد.
🔴
این وضعیت سال‌ها ادامه داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150277" target="_blank">📅 21:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150276">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
آغاز محاصره زمینی؟؟
🔴
انفجار و آتش‌سوزی بزرگ در گمرک اسلام قلعه که ایران از آن به عنوان یک راه تنفسی برای دور زدن محاصره دریایی و هوایی استفاده می‌کرد احتمال خرابکاری عوامل اسرائیل و آمریکا را افزایش داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150276" target="_blank">📅 21:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150275">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شنیده شدن صدای چندین انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/150275" target="_blank">📅 21:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150274">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBP-DrBwNTwGBarbo5Xe3Ev_DBcJap3doKvTCPr4UYGEgcsrL7bXq8q3lRolnJg4bKQu1p9SKCKHnnGf-QLS5oNwBfDXK6kgrUGwUVP38cDS5ASOq8WCgh6lbRAiLGqIIT3Iz35rGgQIeVxb_kSAdYWFVNaXo-rKDAdqRpU2nb0L-faP9AJ9xh9L51VGBAcMrofpKPwC8P_Y4alvj96pe_uZRWbMTGW7iVPUH-m-tmmKS6jO-vVLyL2G5zcwr5lA-YHGTnt5gJC_Ft0Gvj164RZaC2HSlkB7BtW1T-vhdwz9jNGazyNIRrr2nScH7Crjoua70SQC3LEF6Yt7BINnow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: امروز، با خوشحالی اعلام می‌کنم که آخرین نیروهای آمریکایی عراق را ترک می‌کنند! مدت زیادی سپری شد، با تصمیمات بسیار نادرستی که ما را در این بحران گرفتار کرد، اما به زودی، این موضوع به بخشی از تاریخ تبدیل خواهد شد
🔴
امروز روز بزرگی برای آمریکاست و نکته مهم اینکه ما در حالی عراق را ترک می‌کنیم که این کشور از نخست‌وزیری فوق‌العاده و جدید به نام «علی الزیدی» برخوردار است؛ کسی که من از همان ابتدا حامی او بودم و تمام‌قد از او پشتیبانی کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150274" target="_blank">📅 20:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150273">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بلومبرگ: تخفیف ۳۷ دلاری عراق برای خریداران که در داخل خلیج فارس نفت را بارگیری می‌کنند
🔴
برای کسانی که جسارت به خرج می‌دهند یا دیوانه‌اند، این می‌تواند یک فرصت بی سابقه برای کسب سود باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150273" target="_blank">📅 20:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150271">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYyAT950JqP0liTj2KyzepRJjyi1eKKSwQwGvP8gCqg3NbSmGfedJZLjX0mz-sHzGQ_mytluuEO-_GtK-WeI9hAtlL7b25_l9TXTPh5wGT-P72Ai_zSeO2Yl1zvwHLqZ8o1_OUneeUTzKJ_xbf6Uhm5J2bI1gubQKCgNkvcYLl8S4ZuLQ7tf5GPta7Bxjuc2gED2UZY_ruebGH8Vs7jfAE4VFmLIv7RS7CPtO6JbdcaD35LKHv9hzt3P-eLVmqMS2MiTMvuxUOZe3HRiWPoAsABOvUcls2PK-uTT74o5W1qJxfs4tzkRlfPCxhkCM6g5R8tmWCITiAxDJACKIHU58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۹۸ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150271" target="_blank">📅 20:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150270">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_BS09_ecvCVP8Y4p1KxTXHyV0ibQiASeVqrX1N9_FOmlXClUdTyS7GJwZnJSoqQ0jJSuVVJuCpFA-UlfRQyg7Ik_B9i4XUHeHKj4pmE2oPdtbM9yfs_-bK4RdDki4H-fCXCA3Ici9Du8EXpnLj34u1jaGAkQ4eYgMtmu9PNsX-Lgq9Kc1sisJ8JSO6eGotDslpBuv6ow3SC5Cp-MOatGkoYhyxzsn4bKWd2tDK-xOOp6uVnsTNknCKTGu-BNf-g15ga7Sf1uYUDj8FE7YmgWAfa7vC84FBalqN5NpxgIc0abh81TH-0Nfu7oXpgpYkVrOUdK_yfaMF8k9FuFLnhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : کشور ما در بسیاری از زمینه‌ها، عملکرد بسیار خوبی دارد، بهتر از هر زمان دیگری، اما مردم به طور کامل از میزان پیشرفت ما آگاه نیستند.
🔴
رسانه‌های خبری دروغگو از انتشار آمار بی‌نظیر ما خودداری می‌کنند، بنابراین من تمام تلاش خود را می‌کنم تا این کار را شخصاً انجام دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150270" target="_blank">📅 20:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150269">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p244I_vbS09OSsF5QrbvJbObfyaG3tRcnVhBzJz9cyvrRE7wAmaa62fkxnaVF9wwvX3gTcYt2i7Y9IfGUPOW2JmyH21_UR4zMq8jGpJwC5j4X319q65pOnlfd8MfGN-b4up8tTmPfB_7oToywvzoCPG2V2gT-Kr3zkwzurWxyoA2ifBL2dgE1aAj_e72VDIDXYVR9OrJKpN8EwsIDCzOTUFzaIWMa54sWRNAlWp25Z_OOaNO4vXK1VO4lyuOKfsQI44pSJ-CYXKrqVQqaz94bdOyGhX9Z5Maq4ZCp3kG2KBgve_LZ_1VgClvsuZrnq4agFCUJcsVPObZ4TI0oxJefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد اسرائیلی منطقه جارموک در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/150269" target="_blank">📅 20:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150268">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXOru75eXGk0DVNclsWrkeDWfBzHX3G2pFDq35cJlpXMJ5ccSVQlQJ1ZILHlmg-qsHpCX8mjRmDPazzOR9Fw7NbQZOODtj_-mHHeYYlX4Ib-xw6XG4A8F5NeKikuyBOmy58YG3vxbxuRu0pwgEFYgUc9MZelejVX7krx7e-_Xvw_r8xEZnjZsFQ5TLJ9nCPQ6NaEv_j-KKC5zx8jiExm035PzfPPHx-xb8VKqAaZIHXj--0C-RwKjDH2FHJGIBv3pktVb8mi7cfPyQtnDMu5OlZ33V7TwTpvFvlhS8iAvdrID5e-8-qt8lHRF115vr14RNfh1jq3IYyFc-eMzLfcMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار ان بی سی: یک منبع آگاه به من گفت که عباس عراقچی، وزیر امور خارجه ایران، سه‌شنبه در دوحه بود، جایی که میانجیگران قطری نظرات ایالات متحده را در مورد طرح هفت روزه پیشنهادی با هدف اعتمادسازی بین ایالات متحده و ایران به او ارائه کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150268" target="_blank">📅 20:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150267">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nbyH84lQM8AN-GIhtm3vL77HTNhZPnMw1DKCT_ieytrvYOksFTJd3yOnjMqTtIblkUcPCokPmgUK8Tm5D0B3sIrmUfHliSdzJ_PtZdXvz3-hrsSdA2JTH1s_a7jnV_B4W7V1KLbB6v3QzNinwuoISsarRuf62wx7xQEiRkMgWhJBOmhse19Xluv4nvk2QdaUrWOCx0icy6HH8ryui0FfCDqtW3bwiwz5O7vlo45Pa74DhL040BbAnZt3QT6dIKhPGdKbeQhbJg5_I69XFdI4iB5KKEc0k7ThVRNzVmaDBbGtLlcQ8xdXaRZB_hR9-p4Mxlmg6IgzO92hxvgDP06uWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این توئیت برای ۸ سال پیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150267" target="_blank">📅 20:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150266">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی ترامپ و نتانیاهو در پی حادثه پرواز فلای‌دبی
🔴
شبکه ۱۴ عبری گزارش داد که قرار است در ساعات آینده، تماسی تلفنی میان «دونالد ترامپ» و «بنیامین نتانیاهو» در خصوص حادثه پرواز فلای‌دبی برگزار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150266" target="_blank">📅 20:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150265">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEbNi8Nbbhp3Jeyq4kRLHTiLYgxRx-gYsQ_EDdlPeU-YasT7urYyOIQyRrBsSn0HwsM9MCaehImxfZGqhod5187LeaP-OsXolUa-lM6UojDJOwKGnVVtGwwBxRfZhoX0fULVzeqAGIOAVYV6TT9EkL9P1izqG8mS9L01DFaEOwWVgpRR_W0YxXfOLwpCqFklWu3BY95b6fS5IhGZzQkt3lYg3H5C7abDCjJojWQKXhPzjetSKpAZOjuqekJjCoe6zQCCReMjJ6yA1a69IrbpUW9Cfg017daLeD_waqpCLoXZ6QcR7wsMwSyBDjuF6YD3GIEY5aps3rHX7mxhAM-0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای ترابری نظامی آمریکایی اکنون وارد اسرائیل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150265" target="_blank">📅 20:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150264">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg8i2L9AhsZA8eoU8EbQDTn8Z0kQi_oV4ai_cg393iEWKBCwFpyA74pVIv6QMYS4ccs_xzKL7qxi2SX8MPba6LK37sZHNCaA_Qjh052Ocivmvu-2QMS5hGhLq_g_-4eki-lhlm-K6vpnXhqzyhSHXcgm0Irk8RureKg5HI-UmW3hVyBsmZGIC-PhGwkSaPtYvD-xUZ4yfitmVMxRf5JVN6ovzEPjlJPaGAZgXAgCu0hDtrZSYzosj6H4YvejnqDfveb5-eKpYz5o_zEjxJbpk_OJ_6PMMiMbljWs9WOic0LsQRY1zL8wYeb4zz6BVpyxUplV2i_SCDJiH1VHAxfIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادای احترام پزشکیان به روحانی در مراسم ختم «احمد ناطق نوری»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150264" target="_blank">📅 20:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150263">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e800e50ff8.mp4?token=vXQQKJ0nZ4RZUrW8BireETDbQkDVDE7-sPoxChXQ83oTxELC4FjkHq8SsbcOltIsiMWlEp6LFpX1rGTyyqkmm2oOAM5zPUCXbWgsnkoc3ImgFr3Zk3SEOdFxvdGAP_7as8pP_xfBd_5QleVoyeeH9oh7gnQPgj3MtoYVGsHKwFFvSFSt4J5hEnwtWNhK6lNHXizLO1qeXhPzTX5cCBPMT2ajq9fXr_b2Q7kbTjk9tbFbt_jgX_K76bw4oZd_aKObQTNHyNK-Q9de215WBV8F6ZWYz8akww0XGvfirunV2ORkxbYPkhOWopmrbxivruyAw14CI1HVPNm08MCnKJaDpBawKKJYnn0Fcv_eLIj9hvsbd-TVP4uVqGnv06XQGfoqk0jnttTSBPkObJpXb5dzqrqsowfbbou71Xy95vNozaJ8kr-Ow0_ExdxVdGtEeJ_fV_tUrVfbFn6D12tvQO3urvnjJF61Bz3C3uk-1Jk9PHS1GKr2IoO76enUN1pGSl07pzQYOnQzY6HMHguTTR57syLhntf8z_eEcQYP31XPZTunyJ1i4Zz9Iy2m6O4skixjKJN4gq3GRyKbuD9cg9XWPIr9OyBUf5Azjr25DWNuDiwJT3Kh_r1H9oxIRUDCs2eeGM2sZGCAdDQKG_dZJsDAbnYN5sWmKQKcuB0U_T9jcOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e800e50ff8.mp4?token=vXQQKJ0nZ4RZUrW8BireETDbQkDVDE7-sPoxChXQ83oTxELC4FjkHq8SsbcOltIsiMWlEp6LFpX1rGTyyqkmm2oOAM5zPUCXbWgsnkoc3ImgFr3Zk3SEOdFxvdGAP_7as8pP_xfBd_5QleVoyeeH9oh7gnQPgj3MtoYVGsHKwFFvSFSt4J5hEnwtWNhK6lNHXizLO1qeXhPzTX5cCBPMT2ajq9fXr_b2Q7kbTjk9tbFbt_jgX_K76bw4oZd_aKObQTNHyNK-Q9de215WBV8F6ZWYz8akww0XGvfirunV2ORkxbYPkhOWopmrbxivruyAw14CI1HVPNm08MCnKJaDpBawKKJYnn0Fcv_eLIj9hvsbd-TVP4uVqGnv06XQGfoqk0jnttTSBPkObJpXb5dzqrqsowfbbou71Xy95vNozaJ8kr-Ow0_ExdxVdGtEeJ_fV_tUrVfbFn6D12tvQO3urvnjJF61Bz3C3uk-1Jk9PHS1GKr2IoO76enUN1pGSl07pzQYOnQzY6HMHguTTR57syLhntf8z_eEcQYP31XPZTunyJ1i4Zz9Iy2m6O4skixjKJN4gq3GRyKbuD9cg9XWPIr9OyBUf5Azjr25DWNuDiwJT3Kh_r1H9oxIRUDCs2eeGM2sZGCAdDQKG_dZJsDAbnYN5sWmKQKcuB0U_T9jcOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بلاگر یونانی در تهران: میگن حجاب تو ایران اجباریه، ولی این ادعا دروغه؛ من الان اینجام و می‌بینم که خیلی‌ها حجاب ندارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150263" target="_blank">📅 19:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150262">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE0Fn6uw7r_M_gSVPThfmDqPkvn2e7gUXaMboSRxYoaWi3i4IzBKd4QJH8gBzd_Iakm-bSr1n6vDq9jbCOG0DYpu1smBPJ5Mocx73DEDFWl0YjV3k9ZuqYS87LW20SBBkaf-B7XxDQcF8tBY0OU99fCF2b_RngQbnS545g-2ZGmtZTc6P0K-AOw2iIPH-JMq-LalzB20ZrIaT7X946OSAgBCM84gjBu0RNUhDAbr-P8lQWfacRzr_8afEVLCqpGOiKxhbWyhTJ3m93qUwBTapqOokiSvuy-UQzt06a2tj1jETxLQO1tviVSIUKo7C8WOjhlEDH43UliSNXoO0rzOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صف‌آرایی علیه وزیر اقتصاد در سازمان بورس معاون اول پشت تحرکات در سازمان بورس است؟
🔴
با نزدیک شدن به پایان دوره ریاست حجت‌الله صیدی در سازمان بورس، تلاش‌ها برای حفظ او و مقابله با تغییرات مدیریتی، به شکل‌های مختلف شدت گرفته است؛ از مخالفت با برخی تصمیمات وزیر…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/150262" target="_blank">📅 19:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150261">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ایلان ماسک: کمتر از یک سال دیگر ایمپلنت‌های نورالینک قرار است داخل سر انسان‌ها قرار بگیرد؛ حتی افرادی که از بدو تولد مشکل بینایی داشتند می‌توانند با این فناوری ببینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150261" target="_blank">📅 19:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150260">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اندی برنهام، نخست‌وزیر بریتانیا، گفت «نشانه‌های بسیار قوی» وجود دارد که نشان می‌دهد ایران در حادثه پایگاه هوایی فیر‌فورد نیروی هوایی سلطنتی بریتانیا (RAF) دخیل بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150260" target="_blank">📅 19:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150256">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXoQRFRuzsqh2G72vF00bC16h_eYa25p_YU-RXKSIbi_za39Q62YrSXCpMS0G0erI3S8lCjLy9Ds2ZpmGTcNQWn0zwUpf1DxmhsCsIPsKj1_o9Xf4C-9RUCSnL7vnVLxwAm_sDXMP9PjU_UTygRyd7nd0Rps1HelGiIsB4GQUiHdn8Xce9ZihPIMU30g56mbu9gzmjP3KYI7BLNxeWbh6tNKn442QXSb-EIJ8fr5T5JAaHT_dve8W1yu_O6x622Z3Cbg7_wldcV7zpFF1ysF5fO-bpqjrA-V6wKivTus9493SATs3a5TwZ51kFgdHVKkzNGv_Ii7eK2EDsXeJLUREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nyXL2OI_YUePC6z83D4JlFAkjYsExD7mL4CZ_uNg0kE0aFy7vioTfHPZDr70UsHQGtsBeBdq46QV-BK77z8gJlPJohbtf2ReCmOrZMqiTzqt8KKkwUQkoGbrR7jPNSYTmiEqCRYvNrkNofUVIYUFVTeXCf_5KFmO4vOD_zsV821GjO9P6KF_zZYNjCkkcEMHhkK-A_OFmDrqgyKVqwvcfXsMNJ7Wg2rf_x17tiostvCQ2w42qKdoqSTQhiWH41UuRcNirAQFC_SaJfTriXM53brUj81-EBI37LgRI1ubDWbRS7zo-AOYtxDnVCjuCTwzDDj3BYhd_jdEv46PmaYWjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e068cf4205.mp4?token=Uo5s81K4tynhkU67xyeUfl74PF4vSiOR9RsslhNenOVg7a9EFW6hry90ZzWKjM5xpiHwmXeJH0NHsM8pD_EAuiaOhzNiT7fymtqxmCy20lbbPM4OtsecFQ8TYkqA9VAlMG4pfIcN7wYg8vPGFVduLtfDkO78DJAbfiSW6u1Vx9YgtQaAbH1pY1J8kdVtcvgyYtitWpZ9e3FxfNGYVk0FAErLC8tIjIJgjErjdzwZW8cKLAZpNqoYYdfoebSdbWeYbimE9uPvF0I8-3O8IX6shEMenFfXua7Ql8g8vwVRAYip0RBBV_TmdhsLYMT5XstWSbilZ7oskxltnKq4BJHqIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e068cf4205.mp4?token=Uo5s81K4tynhkU67xyeUfl74PF4vSiOR9RsslhNenOVg7a9EFW6hry90ZzWKjM5xpiHwmXeJH0NHsM8pD_EAuiaOhzNiT7fymtqxmCy20lbbPM4OtsecFQ8TYkqA9VAlMG4pfIcN7wYg8vPGFVduLtfDkO78DJAbfiSW6u1Vx9YgtQaAbH1pY1J8kdVtcvgyYtitWpZ9e3FxfNGYVk0FAErLC8tIjIJgjErjdzwZW8cKLAZpNqoYYdfoebSdbWeYbimE9uPvF0I8-3O8IX6shEMenFfXua7Ql8g8vwVRAYip0RBBV_TmdhsLYMT5XstWSbilZ7oskxltnKq4BJHqIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسافران پرواز FZ1073 شرکت هواپیمایی فلاي‌دبي، پس از انتقال از فرودگاه طبوق در عربستان سعودی توسط یک فروند دیگر از هواپیماهای این شرکت، به فرودگاه بن گوریون رسیدند
🔴
جت‌های جنگنده F-15 نیروی هوایی اسرائیل، این هواپیما را پس از ورود به حریم هوایی اسرائیل اسکورت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150256" target="_blank">📅 19:39 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150255">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فووووری
🔴
طبق اعلام بانک مرکزی اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/150255" target="_blank">📅 19:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150254">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
منابع عربی: ایالات متحده دوباره شروع به انتقال هواپیماهای نظامی از قطر کرده است. تعداد هواپیماها نسبت به ۱۰ روز پیش، ۱۰ فروند کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150254" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddd1e8f01a.mp4?token=WNtiWGqJX9bqczfX9JCxPU8qvNaPE30Da-L1KQQ-RYRYnjVq6NTwbQvN_gxg_TiUMHhOGziuDPxax0IoMjCHLrUcRppm0bBV0e13H1UAnelqy344I_P6e3TIISJgxWsTG8VSl7ulWqOHfrx7P1W2WjbvwVJIcnShDLAj_Pl2gzK0rF1EgEjRqnF_Kj_DnLkcsPWqTQAhf8tUjmFC1_giR8c9VZMcnEpT8W3jxmg3INjCqU50O7JNs6SxrY2i-RWWZLMBDZQYH7UZUoEe2KESYGeyurPyKwnty74RdK_V15j7eLBZJy6KrDL3LAfFC8GWKzvaknqyq8gqkNb-GJmU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddd1e8f01a.mp4?token=WNtiWGqJX9bqczfX9JCxPU8qvNaPE30Da-L1KQQ-RYRYnjVq6NTwbQvN_gxg_TiUMHhOGziuDPxax0IoMjCHLrUcRppm0bBV0e13H1UAnelqy344I_P6e3TIISJgxWsTG8VSl7ulWqOHfrx7P1W2WjbvwVJIcnShDLAj_Pl2gzK0rF1EgEjRqnF_Kj_DnLkcsPWqTQAhf8tUjmFC1_giR8c9VZMcnEpT8W3jxmg3INjCqU50O7JNs6SxrY2i-RWWZLMBDZQYH7UZUoEe2KESYGeyurPyKwnty74RdK_V15j7eLBZJy6KrDL3LAfFC8GWKzvaknqyq8gqkNb-GJmU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌های مداوم در تأسیسات نفتی بقیق در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/150251" target="_blank">📅 19:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وام برای خرید طلا و دلار ممنوع شد!  بانک مرکزی:  اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.  بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/150250" target="_blank">📅 19:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وام برای خرید طلا و دلار ممنوع شد
!
بانک مرکزی:
اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
بانک‌ها باید متقاضیان وام را اعتبارسنجی کنند و منابع بانکی را بیشتر به بنگاه‌های اقتصادی مولد اختصاص دهند و بر نحوه مصرف وام نظارت داشته باشند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150249" target="_blank">📅 19:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نامه بانک مرکزی به تمام صرافی های دیجیتال : هر کاربر فقط روزانه اجازه خرید ۲۰۰۰ تتر را دارد
🔴
تسنیم: صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150248" target="_blank">📅 19:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرنگار الجزیره: در مذاکرات، هیچ‌کس به‌طور صریح «نه» نمی‌گوید، بلکه بیشتر با ارائه اصلاحات و پیشنهادهای جدید پاسخ می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/150247" target="_blank">📅 19:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIcbXC05g22HOmz7jDBkQpvqsMpHagdehgeoIDpvBbgHDh6PHRykmAN1pZhula4FXmc8cjpZZMshw99qWBLDyzS-hDzenxO-CS2b2OTG-m0McISkiaVnrcfAHNM0210gtOAfWWZnjrJ8QvYAWvx9VHTzO2NVmuH6BiI_swqDeJ2iNsiNZHzWpqlBpcFIpwCrftmd7YXTKgRWBX8CpriyQ7k4OqHlyJ6uD9RrgnkgCmfamPPho8zazNI97oPvRZfmHofM3ZOoUbImjYh-rZhM8ATKiMA1tEloBUF-z8mAJcB4eeui8YD6pNn8-T3qkuku3CpqMSOe2aLJiuINhkGt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: ایران اکنون در موقعیت ممتازی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150246" target="_blank">📅 19:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150245">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
معاملات شبانه تتر متوقف شد
🔸
صرافی های رمز ارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کردند
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/150245" target="_blank">📅 19:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150244">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
استاد خوش چشم: جنگ قطعی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150244" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150243">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPDVnxYHpeBYactP_hdd3SqkroFxI6TbjkWt3H1iVLRcTa4Hy_midvCxB_PgOTlwg6C78XWJbkPGm85JisrPPIM0IRYe4DNlcsFuM35wf74eKTka0XUvOyn1XtrhKc_74HREfgAXMn6XLw49UgsjKga0An_H1gzQlU2z_lmQWFm_F6tlALYEzVAX47MImgGFsxH1cf5TekHAsElHL-bxiPczzn_rx_Q6gcZu6jcV1gcvN3R4OPFizg9N_YGwGN62Du5JLdBee7JzZ5JEMUIMtbBYCSl05UbJ1QENHZvlfYejKK0I37K8w0BATD8DTXPqRNX94_6yPw7UdDdiLwhjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماچ و بوسه پزشکیان و کروبی در‌ مراسم ختم احمد ناطق نوری
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/150243" target="_blank">📅 18:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150242">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10869c87f.mp4?token=DK06qydIGnPnH0xGPT_gCe_RleuIbpdIZAjFdNwhq6Ym3xJqAkNFscUw5YkfzlICo7HAxwGt33u5Wk1ibeIdAL222Sf1373ydoiLv_DiBpim4zgGlae20Bn9bF-TbbsAa2UTtp8R0fTXgdUFaRpqE71RNfXPdoHFyC4zjTfBMsYpBP9Y7Zs6Imn6ZuVTOln_Q56vmBV_Tkf_DiWOenN-iDUi7WYwWLB3hdN2nkeD_4KLmYQeu94Iqv5oe5Xf5xBsbY1x94MJXQj9_Gxz12h5_bVJ5i_e7Wr6jzBhetrOzFPZoEvUA5DOIm2I7RTI8Ur975XI3j7p2iRfcAl0SceTZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10869c87f.mp4?token=DK06qydIGnPnH0xGPT_gCe_RleuIbpdIZAjFdNwhq6Ym3xJqAkNFscUw5YkfzlICo7HAxwGt33u5Wk1ibeIdAL222Sf1373ydoiLv_DiBpim4zgGlae20Bn9bF-TbbsAa2UTtp8R0fTXgdUFaRpqE71RNfXPdoHFyC4zjTfBMsYpBP9Y7Zs6Imn6ZuVTOln_Q56vmBV_Tkf_DiWOenN-iDUi7WYwWLB3hdN2nkeD_4KLmYQeu94Iqv5oe5Xf5xBsbY1x94MJXQj9_Gxz12h5_bVJ5i_e7Wr6jzBhetrOzFPZoEvUA5DOIm2I7RTI8Ur975XI3j7p2iRfcAl0SceTZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارسالی مخاطبان از شلیک موشک در فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150242" target="_blank">📅 18:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150241">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/شلیک موشک از فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150241" target="_blank">📅 18:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150240">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری/شلیک موشک از فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150240" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150239">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
الجزیره: آمریکا احتمالا پیشنهاد ترتیب‌بندی جدید برای توافق با ایران ارائه کرده است.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/150239" target="_blank">📅 18:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150238">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bd09c687.mp4?token=CnKg3Ay7X2Mg7DpsokLE6uz1oAHbGDMIjEA2ZE5aQRavB38MfTNGjo2V2f7DhxBSuIOeGzuKgk6Fai5DVQI0hlunshS0s5j_G-YKTC_wXOCnial9bgaUBHQzUIpp1JnWUXn3sPCSIXjHQWkXHTK2HrXi-h2OmdPYYK3B2PYaA3Gj7KgSZxLSOWRGM1xTxmZxl5mwyuUI9CrAkq-9U-dLL1Zf3_nONAKzpW1uyPyyx5A0MArHH1wsKJivLluVtyG69FHfmMjbcnr1q9V6epbw5IjjkBVBC4B-BPwwi5JLaLzvZr-1oDAvAxGqDxny4b0kWb2q9BJNn91uC7HUp61Pww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bd09c687.mp4?token=CnKg3Ay7X2Mg7DpsokLE6uz1oAHbGDMIjEA2ZE5aQRavB38MfTNGjo2V2f7DhxBSuIOeGzuKgk6Fai5DVQI0hlunshS0s5j_G-YKTC_wXOCnial9bgaUBHQzUIpp1JnWUXn3sPCSIXjHQWkXHTK2HrXi-h2OmdPYYK3B2PYaA3Gj7KgSZxLSOWRGM1xTxmZxl5mwyuUI9CrAkq-9U-dLL1Zf3_nONAKzpW1uyPyyx5A0MArHH1wsKJivLluVtyG69FHfmMjbcnr1q9V6epbw5IjjkBVBC4B-BPwwi5JLaLzvZr-1oDAvAxGqDxny4b0kWb2q9BJNn91uC7HUp61Pww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالحمید: به تخت جمشید رفتم آنجا محل سکونت ظالمان بود به همراهانم گفتم زود برگردیم
🔴
جوابتون چیه بهش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150238" target="_blank">📅 18:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150237">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا از هدف قرار گرفتن چند کشتی در هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150237" target="_blank">📅 18:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9kt5HTylAhggY3MBFxUXOc0syg1Gaybx2Q4yTRj6jdbvRgeQcMEx08E_vaGnBfAvjqrhz5w1kUEANCadeiG4_n-_mlK9AELKVNja7EiazhLFWuMxwnH6ohLX3t1ivKIRRP4gfY7d7BPVr_uTrSHoRyUdmMVkqSZJ83U5Pw-HduOVaFDvCvV0lt7fhsdKCrihcpls6pRi4pUa-o_wkEhyRJeFidMILWDAjqPPwmg7G9OekvYz2xzfvW5VuaDv1Qe6qA5CCuTbHN39bkS8VKT_xlVhs-ZFDE5cgjGvrKv388TASWg6KClzdmQ9wuw4daVWRULsadG_vx-YDv38KiZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن‌پست:
نیروهای نظامی آمریکا از پایگاه‌های خود در عراق خارج شدند. این خروج پس از دو دهه حضور آمریکا در این کشور صورت گرفت که به مرگ صدها هزار غیرنظامی عراقی و هزاران سرباز آمریکایی منجر شده بود و اکنون ایران آسیب‌دیده اما با نفوذ رو به افزایش را در مرکز آینده منطقه قرار داده است.
🔴
نیروهای آمریکایی عملیات ضدداعش را از مقرهای خود در اردن ادامه خواهند داد. این خروج که روز چهارشنبه ۳۰ سپتامبر ۲۰۲۶ تکمیل شد، پایان ماموریت ۱۲ساله ائتلاف به رهبری آمریکا علیه داعش را رقم زد. آخرین نیروها از پایگاه هوایی اربیل در منطقه کردنشین شمال عراق خارج شدند.
🔴
این توافق در سال ۲۰۲۴ در دوران بایدن امضا و در دولت ترامپ اجرا شد. نخست‌وزیر عراق، علی الزیدی، آن را آغاز فاز جدید حاکمیت ملی توصیف کرد. ایران و گروه‌های وابسته آن این خروج را پیروزی دانستند، در حالی که برخی کارشناسان نسبت به افزایش نفوذ ایران و احتمال احیای داعش هشدار داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150235" target="_blank">📅 18:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150233">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0d82bb00.mp4?token=M_jVW3cCCnchuk47pL4MMYlj87v8AzQCay-Bp3IDD8jpv7jWrpZwCJRzCjhotPfYHWqH5jrfwExmTeHeSu2xiO41_alxUrNaPTFsvXwNFtLy7g5AyoHzLZdsUlEe48ffyTcjMeSwrA2Pzr23D1BVZxgFQGbOdrKzS2srP6fHzSsCD2Xgke9ilR73jGYH5NheloCehHqqpt7oobOGWWIpR-vNDLTz7ZCZ8fuuMNtEHagv5yvHXTA-yJ8AWxBWsPNEIS9r5EDKJKtdM7ff11MrxwlkLW-G0zdr7C3aqzN6rUofFof8YE06vC3PleKK7NmzId-l8GhpBlShiXHlVTmjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0d82bb00.mp4?token=M_jVW3cCCnchuk47pL4MMYlj87v8AzQCay-Bp3IDD8jpv7jWrpZwCJRzCjhotPfYHWqH5jrfwExmTeHeSu2xiO41_alxUrNaPTFsvXwNFtLy7g5AyoHzLZdsUlEe48ffyTcjMeSwrA2Pzr23D1BVZxgFQGbOdrKzS2srP6fHzSsCD2Xgke9ilR73jGYH5NheloCehHqqpt7oobOGWWIpR-vNDLTz7ZCZ8fuuMNtEHagv5yvHXTA-yJ8AWxBWsPNEIS9r5EDKJKtdM7ff11MrxwlkLW-G0zdr7C3aqzN6rUofFof8YE06vC3PleKK7NmzId-l8GhpBlShiXHlVTmjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی تحلیلگر صداوسیما:
دفعه قبل ترامپ اجازه داد تیم جمهوری اسلامی از پاکستان برگرده بعدش محاصره دریایی رو شروع کرد
اما ایندفعه قبل از اینکه تیم جمهوری اسلامی از نیویورک برگرده محاصره هوایی رو شروع کرده و اصلا ترامپ دنبال توافق نیست بلکه میخواد حکومت رو سرنگون کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150233" target="_blank">📅 17:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150232">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AuV8-7l5GOMHlH6wfXmeJNjY8h-fU6gS2-Vvg1tVqzxVemiHBRzcj6rnWDGYGBYyI1O9mjyElclIRZTP96ji89w7bSZDTtKJeuitjVcKCC6mFCMdEAqMjxRivunbGP3JWnX71DMnaO9h6f2ICOvlwj_3yDL3WG5LCUyY2bt2BUCaydktBUDu0LY1PJtfmt62uZPkC2jGjw0dAj9aiIh_2Jki9zT8ViY2PxVzWJziCWZmrUBuTA-RNtRNCGksf0k7tQV2yO7ccIk1GPOeUS92I7wCpqX7d1KgxGzPR07n5faX3pZr69xDWCo_U5dbXxqF5yCmTcrlyoDfNrHy0wzMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قتلی که گلستان رو توی شوک فرو برده!
🔴
تیر ماه امسال یه پسر ۱۷ ساله یه نفرو به قتل می‌رسونه و بازداشت میشه.
🔴
پدر، مادر و داداش کوچیکش برای گرفتن رضایت میرن خونه خونواده مقتول.
🔴
اما اونجا یکی از فامیلای مقتول، با اسلحه هر سه نفرشون رو به قتل می‌رسونه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150232" target="_blank">📅 17:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150231">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYaVrFmaAHHHriNMxDtmtBJqUKP-9n5KN43fTEgmCZzsrxmTX5yjy_0a1FqjSid_Z6ydvtYUEZ0gyL0SpqEBABxkuiMVi6GTAViSVV4zWaVQfIc6wFh0dO99j3j1vPgia91QVvrmezFFkTrE_KYfuGyRQa_W2rVu8Es5xigwPUgN4UR8AFWBr00brdvqq0NtTPHVuZDohz9fda5FFXKBQhSLHngwGamTZ0V4O9HzS7_dUqrLtAK0L7hVEhdTGLGOkCw_BhDE6GtHa0nCenFi49GJh4AnmFbulM-KcdhPHREd3A0yQqdTjiw2yfk0kky1furbI1iP1R2Qc62GTkhpXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امجد طاها، خبرنگار معروف عرب:
به زودی برای مردم ایران اینترنت رایگان و بدون فیلتر وصل میشه و حکومت ایران هم نمیتونه دیگه قطع یا کنترلش کنه و بعد از اون طوفان میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/150231" target="_blank">📅 17:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150230">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو، در مورد "حادثه امنیتی بسیار جدی" که امروز صبح در پرواز شرکت هواپیمایی فلای‌دبی از دبی به تل‌آویو رخ داد، اظهار داشت:
در این حادثه، یکی از خلبان‌ها، خلبان دیگر را مورد حمله قرار داد و
"به نظر می‌رسد که قصد داشت هواپیما را با تمام مسافرانی که در آن حضور داشتند، سرنگون کند."
بی‌بی گفت که هواپیما دچار "چرخش" شد و شروع به "افت آزاد" کرد، قبل از اینکه یک مسافر و یکی از خدمه اسرائیلی وارد کابین خلبان شوند و با مهار کردن مهاجم، از خرابکاری او در سیستم‌های هواپیما جلوگیری کنند.
سپس، سایر اعضای خدمه وارد شدند و به "تثبیت" هواپیما کمک کردند.
نتانیاهو از افرادی که در این حادثه نقش داشتند، به عنوان "قهرمان" یاد کرد که "قدرت و شجاعت فوق‌العاده‌ای" از خود نشان دادند و گفتند که آنها "جان‌های بسیاری را نجات دادند و از یک فاجعه بزرگ جلوگیری کردند."
مهاجم، که مسئول این اقدام بود، پس از فرود هواپیما در فرودگاه طبوق دستگیر شد و توسط مقامات سعودی بازجویی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150230" target="_blank">📅 17:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150229">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDkDpjcJKy2b5QQK-zsvhdjAdRw0NbecJIlWcd1YoinYw1qJWwDy2-qqd-ZByNBVTCxJZhHPxm23xEWHq2MtyZWeJy9bkJ5ra3IesHo5mpm7NG5awEjFMoj8NkOHL5CvBv0t0dT8tiX5NKqp4kR8mjIpMkO4GiI8eVtgT5XuwnfceJ0ocpwd_7pRd-Izne__tsQNjRsVr28BSDnWYG8vv18xbkuOuxUCNoRV14KGkX9OuN7T8Ui0w07wlugYw0xViYJQ5OcO_tdW3aViu-jODiciFxtplk1dIGe4lS5rwnyAvrVAIVyXaaaz-PyVaiegIaxRu7X-smViIisbrzNl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی: اومدم از خاک کشور دفاع کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150229" target="_blank">📅 17:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150228">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تصویری از حضور بیژن مرتضوی در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150228" target="_blank">📅 17:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150227">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMiVN6ATjPWO9Ni2E0GYWtwtcpwjdDpj7V9MqoMIuuk8ZbDLVWgLUD7_NnomE4sjiQS1e7RPZ189ulD5mU3BMpZnPuzJ_PMkWa6WigPPz6-lGFO7LM77jQ7NDEElhxiSJAG1ivlcUJj5leuQ941j0JBfM_fZNFMjz6NgTZp_OR2bi1tDCmgZWAppEVNndVs8IBzyeUECSkuZvAGqN7CVZz9MoY8tLDXIRtKvNs_nqN8iz9vxD-kdkW7PjHRY1kWm09nFrmMe-IQnFm9vtw6KnP_yJEf53Psl0WlNK7-LLzBQMQ4Yia983KOtX4spVBod5zBRzxIW1YfKPaR26E6y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
اسمارت واچ خارجی در دست فرمانده کل پدافند غیرعامل کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150227" target="_blank">📅 17:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150226">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دختری که پاشو میداد پسرها بخورن و فیلمش رو منتشر میکرد، بازداشت شد  مشاهده فیلم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150226" target="_blank">📅 17:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLJNwAKqoIGrb88sKralfSBtgOLWLaZUeN8oGr485S4g00x5qMXd_mLvFiRlW_ZM07w9mbkmanFmgVGQMsfJBqetdxVp3OhgSotpQbcRxidQ8fWTdeqyy35fKyaaN49dhyov400o70XjFj6F-0nAP5Bdn5nAGHdSSM2rVljbPthzV9jdEozV7OTQPDWRpq342PN221DweH1R4dzWVuYzPhuLV0Sz4pPMa1F5IW5HwlapL9heJGDzL-WPYzWTFTlBaDCQtz3qeJC06t0_SlQXmweUeleTTMG6tCSsf7OvN8Ap-7-xRNfF3Oa1X6ShQaTX_WNPOEl7bX_XhszPJmtfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حضور بیژن مرتضوی در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150225" target="_blank">📅 16:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
لغو سفر نتانیاهو و کاتس به غزه در پی فرود اضطراری پرواز «فلای‌دبی»
🔴
بنا بر گزارش‌ها، سفر برنامه‌ ریزی‌ شده نخست‌وزیر، وزیر جنگ و رئیس ستاد ارتش اسرائیل به نوار غزه، در پی فرود اضطراری هواپیمای «فلای‌دبی» و احتمال امنیتی بودن آن لغو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150224" target="_blank">📅 16:51 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150223">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نیویورک‌پست : ارتش آمریکا در حال استقرار لیزرهایی در تنگه هرمز برای از کار انداختن تجهیزات جنگی ایران است و به گفته وزارت جنگ آمریکا که اخیراً تأیید کرده، «پهپادها و موشک‌های کروز ورودی را با هزینه‌ای بسیار کمتر از استفاده از سلاح‌های جنبشی گران‌تر مانند موشک» از بین می‌برد.
🔴
پروژه آمریکا برای مهار قدرت لیزر ۵۰ سال در حال ساخت بوده! ارتش آمریکا ۵۰۰ میلیون دلار برای سلاح‌های لیزری «آماده جنگ» هزینه کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150223" target="_blank">📅 16:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdziZ17PzDAzB57ijUPKVZWU9ZfxxyvWiaPZDRXPSY4_oDk2OB2p_4p16bQUI4buDkdcMYZTOJ9TDJeaJ-b78IP0VWtrAM8_CT4INeqVltuzjIlX125WazQcHWjGiaxjaJnBe_-WIz8evo9tma4nyBou8W2dJDUdqBShhltJ8bvT1JO8OowUOOmTSN4YL6_J0QyJwgQYIEHVUNWcf6I70YdTrZOzB0uiyfNKIPV9a6UDKQhumIQO4D2VdvgSloYD2zo0mwENwMHT0g_XzNH1rcf3aIshU7fnSFgx6YwSraLXBuQxWqVmTT0pnD-odgTbReJxf2t0oolUPHqgYLHUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارزش هر همستر به 420 ریال ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150222" target="_blank">📅 16:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
دقایقی پیش اخباری درباره حمله به شهر نفتی بقیق در عربستان سعودی منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150221" target="_blank">📅 16:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150220">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZLi68tzP4Gxie8rkM3mYKX_tHqRlrb_yJJo5vRH4jYsfNyZloV0ZVfG40KytarW-bHhpROZ3_8Jnynm3OBsROROnbdCTG87dfWFJtrrXTWdY83E7_MuTXb_9pB3CdXYxGbPEoizXGWcodBl_zRcj_khT4vNf8YFNPVT6UEWii_X5ROXoJbZGFqNuQmzZU2msB7rAJXig24Pb1-X8fbJZfZ_KeD-YS3UdZ-tCTqNJXnv-uCCJz-JcXeUHdGkcf_Ditejl9wpdF8W7uV_nMBq0w1cyD-RX19m5O88-ibxUrn9x0a2Ht52ar8D5TBY5LNdi-JxbdK1TeGioVhU1ZT70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استفاده از رمز ۱۱۱۱ برای کارت‌های آزاد جایگاه‌های سوخت دیگر امکان‌پذیر نیست و متقاضیان برای استفاده از این کارت باید ابتدا از طریق کارت بانکی احراز هویت شوند و پس‌از دریافت رمز یک‌بارمصرف، می‌توانند از آن استفاده کنند
🔴
خانوارهای که هیچ‌یک از اعضای آن‌ها مالک‌خودرو نیستند، امکان استفاده از این کارت را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150220" target="_blank">📅 16:21 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
در صرافی های بین المللی 1 ریال ایران = 0.00 دلار  شت کوین ریال !
✅
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150219" target="_blank">📅 16:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKqVB8HUgHcfuLIJOkTn3aDLLpBoI3-uqbbhYpUBlzQEGGAhJAbqfDD68athzFb33jf0jPl3TYzM0AG8RUPAEVJsfsDjW6KtnemDKs0wU8_yJqrntUTRPBt_xS2pOQoRttXRl5mWOksmIBMDOs1amtrmlTaLaSC7_6ZdASHfpJAD1kCauKTJQGt0h9JrOgmB8VBl8-DtuFiFpdPivhivLyPaBfyG8BoTZoMaS7o8to4KQpfa4UNGAZumE2RVnfTczflJ32ADK_YjONCoGfM6qQtMCYtjgoxX7dq6R_Kk_XpHyfQDq4phwVWqtkt8F4Q-kId2fPzUEILr_nU6ZvxC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی بعد اینکه چندروز پیش گفت نمیام ایران و شایعه نسازید، دقایقی پیش تو لایو اینستاگرام در فرودگاه امام خبر بازگشتش به ایران رو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150218" target="_blank">📅 16:14 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
عوستاد رائفی پور: نسل جوان شاهد افول سلطه آمریکا و فروپاشی اون خواهد بود.
👈
فروپاشی اسرائیل رو من هم با این سن‌وسال خواهم دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150217" target="_blank">📅 16:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd4kHHEiAzL2asm4aCeDs_49oZdU2WYGEho9DVBhiZNORK6PLQ9uffLaZlRE6c01vke110FfO_NpWPEWPn6zHj-IWd9RiBHKhYrQJPmR9Ygbr-sBrKy_ZP1WuDtpz3vI0wfcGRZTXy6qywwTrsWBLW85xP-mlkfat7bGi-uGAe31PzlmJZfJ_Aay3e_eOw4K3ONwfkbBhB03KKPwBjSlsbPOLiky07iX-ld4N2KvgY89FQWr4jvZYbEyGUn9Du5PSk3Yp2M73sEz_hn8CF1-JbxKCa_f8WDsuy5YfM0e_mGZDdtJQq2dlhHAfZoUkqFpX_XFuCGY1KjBvQ00y2dNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار عجیب فروش کارت سوخت با قیمت ۱۳ میلیون
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150216" target="_blank">📅 15:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عربستان سعودی از پذیرش یک پرواز تخلیه نظامی اسرائیلی (هواپیمای C-130 هرکولس متعلق به نیروهای دفاعی اسرائیل) و همچنین یک گزینه ارائه شده توسط شرکت هواپیمایی ال عال، برای انتقال مسافرانی که پس از حادثه شرکت هواپیمایی فلی‌دبی در فرودگاه طبوق به دام افتاده بودند، خودداری کرد.
🔴
به جای آن، انتظار می‌رود یک هواپیمای غیرنظامی دیگر متعلق به شرکت فلی‌دبی در طبوق فرود آید و مسافران را به تل‌آویو بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150215" target="_blank">📅 15:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ائتلاف بین‌المللی در عراق: با توجه به خروج ما، دیگر هیچ توجیهی برای حضور گروه‌های مسلح در عراق وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150214" target="_blank">📅 15:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دقایقی پیش صدای ۳ انفجار در حوالی کلانتری ۱۹ زاهدان گزارش می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150213" target="_blank">📅 15:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
همتی در توییتی خطاب به وزیر خزانه داری آمریکا: جوجه رو آخر پاییز میشمارند بچه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150212" target="_blank">📅 15:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
تایمز آف اسرائیل: مری ریگف، وزیر حمل‌ونقل اسرائیل، پس از حادثه صبح امروز در پرواز دبی به تل‌آویو، خواستار تعلیق تمام پروازهای فلی‌دبی به اسرائیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150211" target="_blank">📅 15:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رئیس پارلمان عراق: ایران کشتی‌های عراقی را از ممنوعیت کشتیرانی در تنگه هرمز مستثنی نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150210" target="_blank">📅 15:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3REqAXxcg4t1C5GwQlw1VCg-qlNWUiHfLczeKdmc0O__ogbEv755ILDNn2t4inTijt_F1LOfLxQqiZcZiEcT0yyzhFNmvq9V_RBbOTtn9caOwb7NRRWwUPjtMdjM08jGsyjPG1C-PK2vmLc4GB-ZfIVqEfrNgyc297mPT4-YQN_o0HBpmW-GB7i9nKTvSd0vjdm9ig_hO7y7TVo6xJoaN-VMV7wU4tElaO2S9DjXcWwK8adCL5CJcxrikiL7xEIyzBsIW9wd8kdkFrGvFRbVrAUe5SYHGg6SDecCx7WeqYo9MFSji9qXML_7zNoXK0XgT9yO0VIirFO-xoUAkOrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گارد ساحلی هند: ساعتی پیش یه کشتی باری ایرانی رو گرفتیم که توش 526 کیلوگرم ماده مخدر هروئین و مت آمفتامین(شیشه) توش بود و ارزشش بیش از 330 میلیون دلار بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/150209" target="_blank">📅 15:19 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjCMvSL_UxVgvBjdT6Ql0wTi4McLtUCVcSsKndv18syoLI_jo_PGUoXxkvEwV0_hJRVBl7zw0FFjA55eWuwKJlS44cYrgLzHej-iZWZ4MvxtA0VsSFP2mSQO5komYjNUdVLbncI3Pst3e1JpP_7KH4BtT_0RYEw4t7CWr-Bri2sgR2O48nN5GEeArEIaDGVPCk5xQhq-6KEEtlAdqj4ApYJFqEloECYKnBdcBLhwojqhDangVGOODAs6dNYYZ9t-MkNmv2wO6cPD3vjrAcSPPsdY9C25T7SkeuPTYxo8GvqdwoeKRMd9lg0Pn1yhctDzArCfTB0tqY1BCXfuAA19Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در صرافی های بین المللی 1 ریال ایران = 0.00 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/150208" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد سعودی:
برگزاری دیدار میان نتانیاهو و مقامات عربستانی در امارات، کذب است
🔴
یک مقام ارشد سعودی گزارش‌ها درباره برگزاری دیداری میان مقام‌های سعودی و اسرائیلی را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/150207" target="_blank">📅 15:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
خبرگزاری فارس: مدیریت بازار دلار تهران عملاً به وزیر خزانه‌داری آمریکا سپرده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/150206" target="_blank">📅 14:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
خبرگزاری فارس گزارش می‌دهد که مقامات امنیتی ایران معتقدند اسرائیل در حال برنامه‌ریزی برای یک حمله تروریستی منطقه‌ای است که ممکن است هواپیماها یا فرودگاه‌ها را هدف قرار دهد و در این راستا، ایران را مقصر جلوه دهد تا با این کار، موج جدیدی از فشار بین‌المللی و "اتفاق نظر" علیه تهران ایجاد کند.
🔴
سازمان‌های اطلاعاتی ایران در حال حاضر بر جلوگیری از وقوع چنین سناریویی تمرکز دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/150205" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، به خبرگزاری Axios گفت که جی کلیتون، مدیر سازمان اطلاعات ملی، می‌تواند یکی از نامزدهای تصدی سمت "رهبر هوش مصنوعی" باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/150204" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
