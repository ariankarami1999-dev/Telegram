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
<img src="https://cdn4.telesco.pe/file/RB7jsSRsErKHaUH4E-YOuKK3iyxmnVoDJal7tEXsd31ndInj26JdZsN5DWeodzvKBtGxD6DhtlgS8hrJvD73NdOjjOLUKrbpTM_7XNfqmF5pTDPAjb4w_K1-hI9hVkJULmpqMaG-2IpysWUr_ayMm75Z9iXmgD5aGb8EYGGxzFCXqAlTDQoMP2jaY-iWdqYPqmQ85RhXJ-CwcpKVuk9pxOaWTVHApNaZuRqRlpGuS-QO0fYJOOTyuANU7zNNY0wOi4q3yznZSP2z-0UaOd5HOf2M0d_7jd-J0C2DbO3evPWQNHBazSG0QwoI9UVO3vqaB3S3IivPRDW2lFZJCLndWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 162K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 13:15:04</div>
<hr>

<div class="tg-post" id="msg-68526">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6daaa9359.mp4?token=NnZNY146_4UQIX5sC7hnbSmomDrnKNUZWCgVa7ulxWrl4o34WSy1weGLPLosmMLCZWrQbcRpQIp72AjPX6XqSVqDIs7KHZj4EiEFJExY7uLs-_zSC2JDQgUSJIHkoKIRf5EIcfXBLoLCFzrEtEghiUKJ60vDDV7LOlr7vkusnXVxuxC9DnQt7nOVzYMfRH1AfWLVTweDsrOPRDn5uUMsOuffTXdFPeAD-3DA1Eo9qT6luMu-v776ledK3SQU_eQ6yM7wwlXIny5nZuBY7Zs4bwSOLDuld5dXPoFGJlTijsAoRpinRoAHRsD7OFr1l3FTQdjC9iiZG7uvMpvJXM4OpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویری از انهدام یک پهپاد نظامی مدل MQ9 متعلق به ارتش آمریکا در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/68526" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c817c7306c.mp4?token=BkZpSxO2uNFfpZeD02Kg5gxCGUq31puKF7oMGq3f92Y_IC7ZSOaYkgddn1gfgpFqpYiKrRYvLE4K2UrZdWo5SdmnLg4SL3E8YaQrijKDU2Cs-jRDJZweiSUMVj69Cj_sPIZ80Z-LekvenmTU1l0UMrQGsixPOPpqwF7a8GqZWkhYqSu8Jk_YkC_cy_utNE49XcAY4mpLx-Vreg1kDZH1m06Kh_XYVV_kda9QLZ0NPlnZFxK9tXmNjkdTXnzi2Eh1d9_9Y74KtUkRFFGKOtjDbpLBkV2bRd_g9TSUsQlRZ7YhK-L_-GYcbtWSNNV3Vh8EHSvd_veHlTGgjs8H5TkJpmb9TlA_hwLq4ffdEU5z3BU9hyjvpfieh_fxk1mGiRXjL4XQCgXpu5le9xMS2oD40I4hT3ZXeEqJ4auEvmC7-z5fItpZ3L3Fm9wz8syeJBeOLUbkFKMqQgEVkXPwE9ShgudiU48Q34ChPH74weJhZd_EFBebsBLRBEhhAwTgfCkiBfWjni5Ggr_5fjrQWW9jQ5w3rYicaObLNxv7uREiE01vaNRqhAYMPvnosC3GiYIpSR0JBnB0u6W8jFW1avstuLHLI8d7tXD9V7TjcVmvLLo-gZbcuPcNDdCQ93QZlJjQZekY8sEgUWxTGgl9AeC6IFdTwzOmwCZQBLQo1mTLH_Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
🇮🇷
مصاحبه عراقچی با جواد موگویی؛
جواد موگویی: دست فرمان شما دوباره باعث جنگ شد.
عراقچی: دست فرمان من نبود.
عراقچی:اگه ده روز زودتر آتش‌بس رو انجام میدادیم لاریجانی رو داشتیم خطیب رو داشتیم عسلویه رو داشتیم فولاد مبارکه رو داشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/news_hut/68525" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4be1f5800.mp4?token=Rb4CJ_GmckZMg9uFnTfFm7vZdokB4z5MNpcYPyX-cP2OUVMEE70rreqlSrNS0N6njHjLDApskkNWvCt9IVpd3G-gPYBP7JlwBfNPEmQOoDx7sZ1sYUyN7om-TyFdgvqJygHjwVzghirUOta2Sfs0JhW_QYzsm_exoPxEgRePiHk0ri-PcCZUMIPCEkHvTTHMDPMpzgl5_voxSA0POG7Ialfzu_yBSmgMFudL7zEVvIQisPkGEnkw9zzyvgSI6TGzPomvC7eehvFAvcSe9QS9Aap9y-t4zjUX6JNdPT97bQvHDdPiunj2xBMe9ESVdKECmydI0IbSLFzyU-Dt6rpD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/68524" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇮🇷
فعال شدن آژیر خطر در بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/68523" target="_blank">📅 11:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3dTHwDJE1eHwsWaNvZuLeL9X32J2h1URQGoIf3vUMIl0bi_ITo_UmdIxReUMIIf5BY4sRab3aSzUkSrgs4JlNR6F5QtemOI3OOfaz9GmirNeouBMsF2_tpMBuVPijX_y6oYpf20FuKYD2al0nsimhbFx6Ys8FwqKTcMZfSddX8pH3DtnxAjK5IlzldvAFUHDA86hMkfTEQg6mLhZBnXXb0M4Gv3dLUgkK0ThpmU2DVwJoIIYhOi-w2iRn9Jc_eiC5sZ3PDgSxh00uUKgUhP1j0X8nNl0IUAh6YDi6EjMlLnyMHyvb-tBvcYJTac_xKcxqzOFbWG-e88bnHYIiFVIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14 زندانی تو زندان دستگرد اصفهان برای اجرای حکم اعدام به سلول انفرادی منتقل شدن؛
این 12 نفر از متهمای
پرونده میدان علیخانی
هستن.
+پرونده میدان علیخانی مربوط به
اعتراضات 18 دی 1404 تو اصفهانه؛ اون روز بین معترضا و نیروهای حکومتی درگیری شد و جمهوری اسلامی مدعی شد؛ چهار نفر از نیروهای بسیج و فراجا تو اون درگیری‌ها کشته شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/68522" target="_blank">📅 11:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef80c8768.mp4?token=AsjhMFu-IlvppITciFPTuZw5Kp1lwYag5b3hyvT1MbgzxMxlsWOaUIHMhxAkKTi0GaB_UTe3jFpZba4pN89vcdjjcl4dLZQgJoB1Uay8ItpN0elovcW4ymB2zASBlaUxvovh7RetOXAHzS0Q5zzOqRCy3k1esHa7dXC9bpoCmMYptupKhxNBAhpIcowHrE1ATq_CL9sPbPwor2LTTLQ64HdiIIQ_wr25IxqosOboPzZd9kHqraj8tI0HLSKCN0z_e6u0aVXpw57gFS8v2FPhuBxBEnxrMFrG3oN8H275J2rgMBWG4MXvwwTQYEnamkMTMbuBn5Hs4kLUoKX94Wzphg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
در هشتمین شب متوالی حملات ایالات متحده، نیروهای CENTCOM با موفقیت به تأسیسات نظارت ساحلی و پدافند هوایی نظامی در ایران، قابلیت‌های دریایی و انبارهای موشک و پهپاد حمله کردند تا به تضعیف قابلیت‌های نظامی در ایران ادامه دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68521" target="_blank">📅 10:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
جدیدا تو جشن های تعیین جنسیت دیگه خبری از ترکوندن بادکنک نیست
الان پدر بچه رو میکنن تو منجنیق پرتش میکنن تو بادکنک و آب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68520" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68519">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0c1d5cc2.mp4?token=F4jKt383PcCm37SyCgjCwgjMIGAZMTSLJRNPOYBaDwlxTfIv-XxfMi9zRD0hT47aIGWdWcHX2T-6xHAsEYfCQ1mK96MtB85m-hw8DyfsxPiYEzGqhxMUKsFH60M0xmcXIup2TztC9ZUfs5UA_WkzkXARIb7MAX_BhTYsr0bLVRbFBbGDRK9xHq8jc_ggac-31JJFw1DBGkv3bwRabhEw9fJOk5cAs4Gw4xpopz1FjQoEK-zfI3_AnzsBBjlBnXQPlep38fK9h_QxkdEEprLYZe9AAuElRLSr2tir-P8mP1LmV_MSmaAEvw0L0uQ_o688NqgT3gXrOwIrIeD5KsYQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇱🇧
پس از ترور خامنه‌ای، یک گروه از حزب‌الله تلاش کرد تا پسر نخست‌وزیر اسرائیل، بنیامین نتانیاهو، به نام یایر نتانیاهو، را در خانه‌اش در میامی ترور کند.
⏺
سازمان امنیت اسرائیل، شین‌بت، این توطئه را در آخرین لحظه خنثی کرد، زمانی که این گروه از حزب‌الله به طبقه زیر آپارتمان او رسیده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68519" target="_blank">📅 09:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68518">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68518" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68517">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=iTvL29JICXu8WT3aJCTrxd_u1ss5OLCrU7tdYIHCMjYXIuWeqJtVKnaKVbOKWFWwcC0obRQ8dmVXX248NsGEMFPNQYuKBkwKotwvxl5vhSJY7a_GBOz7YaFB7Ix2SswCI_s8qXN40nah7DV5ORFTJBYPRzUirFabtEvtRX2gdVlyX_FYIrUCcxQfaZMaqSaa1WIcFpm9qzYl5jVLWGgxBpk31xPSOEleQhmwf_h5_nAefA5xnjJUPo7VZck3zCEE3srSk2CtMx9FdjDVcg-RuWdE1XJSxpr_n1MSM9h85MO9i5YOZfuokpNHgAIDF2EOANLjZLbjax--0RYF3lHuYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68517" target="_blank">📅 03:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BA-6FGctFNYRpd6hMy0xGM_gk5VYoIghPIDR8TJVKeoBRIfwGobA704WJi_2f89GPeChy8HPsDDXeTmoAW8RkhSf9l5XtULmhKuLagBMIT8lkwu4VJKHPR86NlsCeDcT6XYh9DLg23vcQH3IqIstv_7rj-10MMZQrrouCCI-w5OoBVhQAEaOtcod60dXI5eDRkOk0cSFl-REqNvhLpt1gsoAdR0hawn-Vl4Yx_8Buz80RCQftfGbVFJvQJXMQH_9QArdLqQCaVAkwd47CjyfU1lvkhCkcMUHCFf625yP7iEbD0U-9GaY3AcIzRX-RcaJyRTjaOEANBJaYPnMYKqJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr0fI8WKVu5xLfh6Y40N6WKTfz9tOwfieHTR5-WZEVWuRPLRrF07-g3zslo22gNxSQcllLCQPEhWdr5wJRHiViV6nrcYlciIpXGV2A-lAeybwnDNAkoNztjLE3avwJXaLHWYRP0DrkMw_-mHDFAeFMtPzWLg8mqggYDaINbN6xqLN4SsbAh6AeaIi-LDVVttATM-PTvgzB6woTG-FQwF6J15247lyx_RtRL_hhDzmExJbKsyITz_MS9N585BwS5jiLsVtwgpg21vfB3mz55rD41jdgWZZfhvYXCm0lx-weSoVejtH2qiNOPaypDvICc0xJ7X_XTizrjqbdQlhaZiuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
حملات موشکی روسیه به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68515" target="_blank">📅 03:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🏆
رده‌بندی جام‌جهانی فوتبال|انگلیس برنده جدال بازندگان در یک رالی تماشایی گلزنی؛ دشان و تیمش در روز رکوردشکنی امباپه و اولیسه با مقام چهارم با جام ۲۶‌ام وداع کردند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
😃
-
😀
فرانسه
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68514" target="_blank">📅 02:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
تسنیم:
حملات نظامی دشمن آمریکایی به حوالی حاجی آباد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68513" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
بهبهان صدای انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68512" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
دو انفجار در بندر‌لنگه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68511" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68510">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
صدای جنگنده در آسمان کیش
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68510" target="_blank">📅 02:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68509">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d71f9fb5e.mp4?token=G9bRB2iZNmh3r3zYM3P7AlkgldaRm0Ez0kEwTcThaSr5T1pd496mL599sY-Ju4klRKtMgwkTmEYNzfJArD6Qcuau8Gz04VQ8BQww8r9a3DZcBonX2UCD9KsvBX6_cLByvrgDzDrmnFCSKF0o-cr7-_vRT1iL_GGC-XDS_iTiJRTQzbw4N1JLGwyrcjMEtVB9pGb0cfi9DOhYI_1ag9jMM3YyZi2S_6XRGVYv2eat6s3i198NP70lz6FWk28zEMhnn5i16M7dSmpVlNdVnfU_ejV8WjZCiK2HLsZwu_PaGW4B8S8uTxw79VX4XeYieOfi0WClo3gt0tMjoLseMRbhzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68509" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68508">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68508" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68507">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph-wYO6kmrLWyjEc8ZM63zlPKSmi9rTGSG_YaXEb3D65vfio8WF6mciqTyhj88U_lZ_YH4MyZgw_V7yGZIlyzMdR2YwgPYqq9J7DBu5IbeswbouLMPhM75IKcQQxoZIZHw71x_WmZQqn3Ine7fVj_hODaygPk3ZhPRQMc_U0g6q_SX7bccSykLLBz2TL38zhbRUsDE5n4Llh-BRFCaRm7yD9_QY_LPsX2wBFxiz6wpYvEpn46oQzylomdM0fNVBNaIgwqZLdJj4DRYVwHD7_U4fuaFVMIe_6oahsiJQVFmawN2fIzsg79jwqd0GCDMuHgmvj66h1SJqRMNhDq2at-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ عصر به وقت شرقی، نیروهای ایالات متحده به دستور فرمانده کل قوا، حملات هوایی جدیدی را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و تنبیه فوری نیروهای سپاه پاسداران انقلاب اسلامی است که شب گذشته به نظامیان آمریکایی در اردن حمله کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68507" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68506">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام اعلام کرد دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68506" target="_blank">📅 01:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68505">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm9llfHlOia3Hzh2XeNhHNa8_JxSZUmcIU_sP5iPn1FcWTnyHNB5mByMQj8JNKL8my83wLFg5U1NdBCzzD9WU6-oCaI0gIYiSM3KjJUvOomXH3x9eLbBNxq8_4rnNp-qOSHDlmMCerLLQ0x7d1Dq3QnkgVR_acHCj4vvG7kls_P_Sx4No_44Ref_OmQhTt2s5Ny4e74YgSrQTch5H3L6-rs3pGZ0JYCjC6ZAqUxbsBUSsbJYrDVrZWb_qdKqSuiT8w4whyriu8QQvO0ivGEqkKX72EPayqUIK3HGyIne-ieLJ68hUQdIPfvh7W_682dNL5ONBj-hbqxIjhrtu_3fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
حداقل پل صراطو نزن بتونیم رد شیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68505" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68503">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vdoanx6icZ7tyHyl6UphWr_Iim43skmrbVRj_SyzdBjv9A3SUazfFHUQ4z7iYY2ENXn_rljxiuhb1gGVtzL5XlK8kAoHKekgFf0-FJeQWR4YWJ7jmR2DArpNYC2C98G89J0l62Gxb1A-XrTjo2fenDVWEqYnxbdWIPwKz8B5iCIwc8w-R_Z8cgoprjHkxAVaoifjlW31jP8NgGfjykY6Z_aEerjDyMaCiVYrslgTyX7ZcYh9hmDB-PnrCUd8NeUMEi-5S2nbc65dZJc0K0u7WwObJHHHGCSm4Bz2Uh9M-Y_u5l_ARIj8_R8LfcEB1lvL-KMaFohBB5DrKWko-aEL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPZqwzuv-HwZMS2Gjp9nWH8VcUCKKpPj0b31u7feRxsUC79V6vkqcdRHPNWHED8YTHEtFUayJcT8Dkf_Xs6QSgOMshzb_m23x2B3pAArKlCLx_pwap9NSGMZetMvlQr2e9bpFMych9BviWxeZUobJ-H3NQwu5dePmhBUTPMozlA8m1zSFzSIl3_JdnAUcHm4tlbdnE4_Apqj4OAYTRvogiRRmNov6XW4h2ggPE_Jow16RagzXv8APnilugbaFYWTReC2okHA_b9fNh3F7dMWWP1MP5rCYdz0eriCpOBomjVvXMKx3Q30ukiCC2wSq_NNAFvut8ifATov9b8CrkiIPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
امارات خواستار توقف فوری تشدید تنش‌های منطقه‌ای، بازگشت به مذاکرات، حفاظت از کشتیرانی در تنگه هرمز و پایان دادن به حملات علیه زیرساخت‌های غیرنظامی است
🤟
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68503" target="_blank">📅 01:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68502">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرنگار: ایران اعلام کرده دیگه به تفاهم پایبند نیست نظرت چیه؟
ترامپ: خب بتخمم
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68502" target="_blank">📅 01:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68501">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68501" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68499">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rH7wumbhHuQmyGMOCCy3ZiuSI0w1XJJ0orbq_GTtestDGVs-WJUdKrF8j_Fon6E_3bWr6zkd1YWIPg3R_oCK8pjhyZboWvxJX8gKFiZLnkex08Xo9ija6hoW_YGwkxq3VNK3Iofr5EWw9G0tcS6V7g8LkrR00fvYGMcCF9BP8EVjq94urfC52LwYWK4GXajlWgIjXpBlzPXV32Nw_j90ALX7MPtxsdG7nAfda36MXMcoR8DCqkPYIajjO1e40uqc17XhEcJr9A3qGR_Ha-JW_94ydFim5Rl6IGE0VCzkmfRtUyojir75WQGrZypiAXCaI6zwPKM6eSUlwCnc4A32qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6WT8yE2iehIlRT2q07PJzL7M9fP-Bha2WT2Xx9TaDF55Q_Gaxix1-Nvde4IKDi_85XlR5eYnxNRG1a3mqrM2h6n4f_x4__PF6ipE1D80uTRxmqgcU5-NOhMojQloNTcELBzyQfY8YL_TCpBGYtOi4fC0nE8-vvdcLvDpntrvgiIWvGAyRNPDQh4G4f_B8QKMIVirdoqMo6FHrNx3MPSBXZbg5f4tv7ldQaLYEGo6Zbi4CyzbvUPpSeOy-0iZfZG4kl83s2xEzHKNx5RDvnKjiWb_JbXO8pkMwwaOAu44iF7AvJYqXtpL8jwWmkdsI7t_1Y6gwupwpBvsAqAfGgA5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دو فروند هواپیمای تانکر متعلق به نیروی هوایی ایالات متحده آمریکا از پایگاه هوایی العديد در قطر تخلیه و به سمت اسرائیل منتقل شدند، به این دلیل که از احتمال هدف قرار گرفتن آنها توسط ایران نگران بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68499" target="_blank">📅 01:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68498">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDqjtEJdFHIS-eJVL0s0KyVCse8EQ3OLRDbXilZRcT_L3KU-8Uykp6q9-q1bJAK8ZtX3IsCaLHA0x0QG0GuenOWL5kv6H6GSLKnL1CpCU7bEkKXVO0uiwtR6LC9GJZC_yeda600jCUI2h9LVoLZ_J-IDf8aqYFTQOp_4vRBK6oLgqSdyZm0MRjCDmBwERLmwLPOEghXgrRz5XXB5GjdpzhWl8fLoS3Wy8Q2F8bjHPwaTjNqd0DFJz0UClZv92KM-z8HqzGTdF9lv_LHaRkp6nLFbWhKu2Gg7GvTrO2-xtxXCS4kwmt6r6EK6XP6qVig125jmR2p94HdDnsGc7p99aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
دونالد ترامپ، رئیس‌جمهور آمریکا به «نیوزنیشن»، در واکنش به کشته شدن دو نیروی نظامی این کشور در حملات ایران در اردن:
«بسیار غم‌انگیز است؛ اتفاقی بسیار تأسف‌بار است. ما از وقوع چنین چیزی بیزاریم. آن‌ها در راه خدمت به کشورمان جان باختند.»
او بار دیگر تأکید کرد: «ما هرگز به ایران اجازه نخواهیم داد که به سلاح هسته‌ای دست یابد.»
ترامپ همچنین اظهار داشت که برایش «اصلاً اهمیتی ندارد» که ایران اعلام کرده دیگر به تفاهم‌نامه (MoU) پایبند نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68498" target="_blank">📅 01:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68497">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JULJDxvLcuw8_Zl2MURHK-hac4MVnxiPxKgEKTDtI5UJXatpWTuIe8h45PZnKeMEUzSoRAPvcnlfh2A9XEXvaVmi_J_KKgwkUSIM84kYnegEKXHEvG1dfGnTL_j36uV02lBUcBmLvIBjvdVrmI-jaN8II0HnFmBV6pK_GPGs_sWjV4XOWmn1wAXvNYNwe9E3-6oSNuuJLdlJUUmTe4pEKgJbjITO0okNtS2eboqa6yUrvw2Qi3wMLQL3BDSak9SOnr7rArgpS2ftn-bYCJoYzOTX1rgWuWtmnoc8igOmuoVKFAr5DgtWoMTXZrL0MuxlvJuJYayqimGBzwe1kcBA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
شبکه المیادین گزارش داد که در پی حملات ایران در خاورمیانه طی هفته گذشته، ۳۰ سرباز آمریکایی مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68497" target="_blank">📅 00:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68496">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
بندرعباس زلزله!  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68496" target="_blank">📅 00:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68495">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
بندرعباس زلزله
!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68495" target="_blank">📅 00:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68494">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwwiuoBtZLtjce1KRm1dVj6lbkuv-dR9T7FST0XWzGhh5qbvLvD_A9RC4Lqj7y1ad2d6m1BOSxRmMlTQIYzDtB1WifY0AaMyhWMUXDzyxdT-RZA2CkCMLYhrXF_pO7zd06oaWuVsBcbK2vV26wYOvVq1ppn2E_oapuvGpnuo9T0gSCtx2neFKhkKqzsvVUo_xY_MxjNYNdgk5mpEyEv8DJ8NpY5JIbGjo0bVMYVs0IbKbAKOaDYk3ylRDVj5P4l8bIBD54ymw0jfct6LVIzhQxEeltanvCTxLW_66bcQ1Wq5q2HDnTLnGlWuP29FMzDHqfY94TqnHTw6ssE8DWwUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: ایران در طول پنج روز، چهار حمله علیه نیروهای آمریکایی در اردن انجام داده است.
اولین حمله، یک مرکز مسکونی در پایگاه هوایی شاه فیصل را هدف قرار داد و تا پنج سرباز آمریکایی را مجروح کرد.
دومین حمله، یک پایگاه شرقی در اردن که توسط بالگردهای بلک هاوک آمریکایی استفاده می‌شد، را هدف قرار داد و به چندین فروند هواپیما خسارت وارد کرد.
دو روز بعد، موشک‌های ایرانی به پایگاه هوایی موافق سالتی در ازرق اصابت کردند و حدود ۲۰ سرباز آمریکایی که در پناهگاه‌ها پناه گرفته بودند، مجروح شدند.
یک حمله دیگر در روز جمعه به پایگاه هوایی موافق سالتی انجام شد که در نتیجه دو سرباز آمریکایی کشته شدند، یک نفر مفقود شد و چهار نفر دیگر مجروح شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68494" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlhvRlPY63YQ41UNdlH3tNBpQPW5uUUjdRdHbjZzaGZr_xDtzw0KLX9qZF9Dg6b_NGeifX5EGA3eax-INIpNb7aLRA2yDuE6zCdLSc1BgufL0lXfP1DzNaVOOLfqlLqAUmcM0y-fU9cQ-gzymJyHj30zrvPuzCc4QoSn3ognXNOUJMwGb7mF1vPysrs4CvSvMgxI1VUTNDpHAg8onTjnAbFywVlIPPk3R7ukUUqD96UOX8ggA2CPukxWEfpP1WuizADlevByuEmifUklNgp7_3Yk2-Nxvyqr60Bb_7IJrWJq_xADMlynrzHhTApHvXx60u8ELTxzSGhz-64RCDDZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیومدن؟
#hjAly‌</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68492" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ciPDXrqd7sb9FgmWPlKC49aTXnXU_sS0aXN4Q6nTBBvlP2GRDvurw7VeUncctp43VcYIg2SXlnurhX9VtchO893zyDD1yhjFkEq_BNqWNzg_-nfTyeEtQVwfC3_qExDRIFd80ApRormo79VQl-0JPAU89MSNGdIIdo1eR1KG-_wm3HeD2KxYUrzQFKeVSIUyUVSr7l3ics4txe5Jdk5KVU_zc9fnMQhdBZQquig1KOwtJbgzrzeJXmcUQE8tL7ym2bnrlMgr1_g9md_MjU0WYYk4GjbGyW5VvG7jA68Vrvo8lsYOhcacpuzr0932ObvLL74JYTBO7p_SB_A4B7ePtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PgzxwtKj5fjAS_NcfGEwB4tZ5JXmzfJWeD5J2E0-jXw95cD7_tJ265OIfos6Pf7Kz3e95USbhwR0o6ndkNdv-OIIExTZz_KznwdN3THT8ZN4YggaNTF6KXeie0DkOV0RxVNdzGb2G71UBpj9ihs5IBXk-eKrmpGXPBtQ8ELvL_Et1gkW-bIc4qxrt5RnTozBIV2-xCw8nhXvvN2j0eNyLn4AIxLauIihHT0N-oYAZgQX7yqO5Dz1nD554W98g5WEYW_v41imP2pgihTr1eAhthDerXB4SG4XW-77OFpX4F_bBL7XxgeXvm6to48LNG8h2ww03e0v5m3DK7bCYrx8fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیلی افشار دوست‌دختر سابق تتلو و پویان مختاری هم این وسط تصمیم گرفته پورن استار شه و یک کانال زده تلگرام که ورودیش 2500 استارز یعنی معادل 8 میلیون تومن پول می‌خواد، البته محتویات کانالش لو رفتن و کافیه کلیک کنید رو لینک های مدنظر پایین :)))
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو‌مسیج های لو‌رفته
(Part2)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part1)
🔞
🔗
مشاهده ویدیو های لو‌رفته
(Part2)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part1)
🔞
🔗
مشاهده تصاویر لو‌رفته
(Part)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part1)
🔥
🔗
مشاهده تصاویر لو رفته جدید
(Part2)
🔥
🔗
مشاهده ویدیو های لو رفته جدید
(Part3)
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68490" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68489">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اماراتی های کاکولدزاده خواستار پایان درگیری ها شدند
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68489" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=VdL8ahBdtOF4nKaxwxldFZ-GDubYT_W_Au5nMAJXQdKwaKCi97CF32ggpb3vkS-QLaoKIhk3eqNgDuK3GgH51GJDaU-e3bt5p-o02ZW2OnsBJ-dPKs2-JIhK14HVH47jmT2rnANGEzbWIBGhZ-BqzvrOhk8ggAAGVunTtReKDTBIDKKcU5h_bV9K_-_pIcRAo7mDIsxV8GN8fmSiSl5IzzD54azsHv1VE5tSc4_mmf6abLe3Z6G_2kU6yV-zydpZA0ithQNZ1SqW39xK1pbSi7te0N4SODWI1xhVF1cvmoLa7LBFtE6zLvH6ATDzbgICLUsuQJ4Q9Z4QI4p6r1MeFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b7aa9105.mp4?token=VdL8ahBdtOF4nKaxwxldFZ-GDubYT_W_Au5nMAJXQdKwaKCi97CF32ggpb3vkS-QLaoKIhk3eqNgDuK3GgH51GJDaU-e3bt5p-o02ZW2OnsBJ-dPKs2-JIhK14HVH47jmT2rnANGEzbWIBGhZ-BqzvrOhk8ggAAGVunTtReKDTBIDKKcU5h_bV9K_-_pIcRAo7mDIsxV8GN8fmSiSl5IzzD54azsHv1VE5tSc4_mmf6abLe3Z6G_2kU6yV-zydpZA0ithQNZ1SqW39xK1pbSi7te0N4SODWI1xhVF1cvmoLa7LBFtE6zLvH6ATDzbgICLUsuQJ4Q9Z4QI4p6r1MeFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایونت ورزشی، ۲۶ تیر؛
پارک پردیسان پونک
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68487" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
یک مقام آمریکایی به شبکه NPR گفت:
«رئیس‌جمهور ترامپ دستور داده است که فرماندهی مرکزی نیروهای آمریکایی (سنتکام) در ساعات آینده، «دروازه‌های جهنم» را به روی ایران باز کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68486" target="_blank">📅 23:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=Ikr_M6sZjzTiOO5o2iVQGqu9avvIfdE03RaAR_Yf4cCW4eTjX4QWsN7ltI6EeqbNkGHI6qBHoFDFBSCh23IVcJL64BxDC1RkWxoQMmgb5OmEnJRs7khQtRZnlLtKWEYABCgi2aHC6rLgPj-C0jl9gsm73A7T5ttg-3Er8_XXgbwDjIFF2ZEg3a8oQZQEeancv4Yf1mk9J9jRw5rZZ6coQfwBNTwKkj5cbuzwfy9x5-K2e_p1RTGEzXW8y_qVsCWTwltj_XuqGDcKgS9yYLrxVOBLjrUZ9_armIyaGecqlWe7807yThi-0lvh6qw-W-DqYYMRR4UjrVQlGWMstvAc5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51feb96ae6.mp4?token=Ikr_M6sZjzTiOO5o2iVQGqu9avvIfdE03RaAR_Yf4cCW4eTjX4QWsN7ltI6EeqbNkGHI6qBHoFDFBSCh23IVcJL64BxDC1RkWxoQMmgb5OmEnJRs7khQtRZnlLtKWEYABCgi2aHC6rLgPj-C0jl9gsm73A7T5ttg-3Er8_XXgbwDjIFF2ZEg3a8oQZQEeancv4Yf1mk9J9jRw5rZZ6coQfwBNTwKkj5cbuzwfy9x5-K2e_p1RTGEzXW8y_qVsCWTwltj_XuqGDcKgS9yYLrxVOBLjrUZ9_armIyaGecqlWe7807yThi-0lvh6qw-W-DqYYMRR4UjrVQlGWMstvAc5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که دن اسکاویینو، از مقامات ارشد تیم ترامپ در پلتفرم ایکس منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68485" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68484">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68484" target="_blank">📅 22:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68483">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
نتانیاهو شیرِ یهود برای آرژانتین در فینال جام جهانی در مقابل چپول های اسپانیایی آرزوی موفقیت کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68483" target="_blank">📅 22:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68482">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68482" target="_blank">📅 22:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68481">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ پیت هگست: خدا نگهدار قهرمانان؛ فداکاری آنها فقط عزم ما را راسخ‌تر می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68481" target="_blank">📅 22:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖄𝖚𝖘𝖊𝖋</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=V0hb7TIC4wix7eepWJCHXe10lx-03kvKnqlOLsTsxNruTOXhklyvceMzS-BJQ8WcuIB2brFR850ucwxjVMh4XXLUyI7vfFIWlcsr_KCJa0vWf8z957n81AGHUGtaby0ejCIaH5mYPJOM5TFmndKl53OLumsKsanM6xcK3PQpLWnMlgqp4h1Lfqi_ACHQetj8qUwV3fwkiFvpA_W0j55xZgH7xl4SHBWApgEKnolVs8Weyp3Vm_mcq13pX1HUqrxYZ1r2ANDi-17049F7D0FtUT3vsRikLg_gTcW6EXQ5--pR8Fr3TQJvptJn2Zk2FmUNZEdVtVquhAv8iT_Lp6hlDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27909ab46b.mp4?token=V0hb7TIC4wix7eepWJCHXe10lx-03kvKnqlOLsTsxNruTOXhklyvceMzS-BJQ8WcuIB2brFR850ucwxjVMh4XXLUyI7vfFIWlcsr_KCJa0vWf8z957n81AGHUGtaby0ejCIaH5mYPJOM5TFmndKl53OLumsKsanM6xcK3PQpLWnMlgqp4h1Lfqi_ACHQetj8qUwV3fwkiFvpA_W0j55xZgH7xl4SHBWApgEKnolVs8Weyp3Vm_mcq13pX1HUqrxYZ1r2ANDi-17049F7D0FtUT3vsRikLg_gTcW6EXQ5--pR8Fr3TQJvptJn2Zk2FmUNZEdVtVquhAv8iT_Lp6hlDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش پیت هگست به کشته شدن ۲ تن از سربازان امریکایی</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68480" target="_blank">📅 22:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68479">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=kfGFuiRGZt3-hX3VAMVHC10EPGypCe_JupNAQ_gZs6Mf-IOLqdJObkTLGi1H6mVYjBb-UTEEjdhLPxolmR3rdpx5iA4wKLGkQE7mWetBIG1CokYk-zBYko1d0D3eG0nm6COOECHlImEQreQOKzu9biSSskvWMc0_2UMi_yir4t00oGv2E9qmPRm9KdmIdKThQrM7C10WW_l63WVD_QtPAPZEGQD6HNTya0cmaFQIomNidvB9DxdWP4dA99CiYEiKXRkro3TQOop-F5gDnIuXY4fYpb7cxvJCdDBaGw3-fs94dJj3SU18gz9a1CA54Zq6Qp0nnveHqRM9hcwKLvvBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59058bcce.mp4?token=kfGFuiRGZt3-hX3VAMVHC10EPGypCe_JupNAQ_gZs6Mf-IOLqdJObkTLGi1H6mVYjBb-UTEEjdhLPxolmR3rdpx5iA4wKLGkQE7mWetBIG1CokYk-zBYko1d0D3eG0nm6COOECHlImEQreQOKzu9biSSskvWMc0_2UMi_yir4t00oGv2E9qmPRm9KdmIdKThQrM7C10WW_l63WVD_QtPAPZEGQD6HNTya0cmaFQIomNidvB9DxdWP4dA99CiYEiKXRkro3TQOop-F5gDnIuXY4fYpb7cxvJCdDBaGw3-fs94dJj3SU18gz9a1CA54Zq6Qp0nnveHqRM9hcwKLvvBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه اصابت موشک‌های بالستیک به پایگاه موفق‌السلطی اردن که گویا منجر به کشته‌شدن دوسرباز آمریکایی و مفقود شدن چندتن دیگه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68479" target="_blank">📅 22:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68478">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پیش‌بینی می‌کنم که حملات امشب، از دیشب هم شدیدتر خواهد بود... #hjAly‌</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68478" target="_blank">📅 21:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68477">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">همونطور که پیش‌بینی می‌شد، دامنه حملات امشب گسترده تر از شب های دیگه شده و حتی حملات به یزد هم کشیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68477" target="_blank">📅 21:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68476">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=kfZ1rh5epNN5p0FjCOLkwEGt4436X_fdzzjji-hAmPyv7QkMycLpEOz3pOHuOY11OBFqWYItqEIIxE_1izFIBY5U-Ne_iipI6WaDlehDyiJBTPtwqGaCZSbYO12yi2jXxF-jaeamtM_9Ev2mErt-ufMotnvdJi_16dE6dzTb3WrAkkKLkKWHHEaoChRPrw5TDAq5muMISx8kHpPptAPlulSNIcOdBVDKGMPPJtfyfLzz2x79EN_3m-SNmmCXJX7pCchBye2PokAES7jVYc3ou3B89ZC8QAsN8RPtFhGvHyvZsNVFPhkVnjMyGe1hgOa2TCKqrScKaPGgJID_4AOVZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c6a7a84.mp4?token=kfZ1rh5epNN5p0FjCOLkwEGt4436X_fdzzjji-hAmPyv7QkMycLpEOz3pOHuOY11OBFqWYItqEIIxE_1izFIBY5U-Ne_iipI6WaDlehDyiJBTPtwqGaCZSbYO12yi2jXxF-jaeamtM_9Ev2mErt-ufMotnvdJi_16dE6dzTb3WrAkkKLkKWHHEaoChRPrw5TDAq5muMISx8kHpPptAPlulSNIcOdBVDKGMPPJtfyfLzz2x79EN_3m-SNmmCXJX7pCchBye2PokAES7jVYc3ou3B89ZC8QAsN8RPtFhGvHyvZsNVFPhkVnjMyGe1hgOa2TCKqrScKaPGgJID_4AOVZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
یادی کنیم از این سکانس که ترامپ چند وقت پیش در تروث‌سوشال پست کرده بود: اگر یک آمریکایی را بکشید ما با پاسخ متناسب برنمی‌گردیم با فاجعه کامل برمی‌گردیم
این صحنه از قسمت «پاسخ متناسب» است. در داستان سریال، یک هواپیمای آمریکایی در مأموریتی پزشکی هدف قرار گرفته و شماری از آمریکایی‌ها، از جمله پزشک شخصی رئیس‌جمهور، کشته شده‌اند. در اتاق وضعیت کاخ سفید، فرماندهان ارتش گزینه‌هایی برای یک حمله محدود و «متناسب» ارائه می‌کنند؛ اما رئیس‌جمهور خیالی، جِد بارتلت، با خشم می‌پرسد فایده چنین پاسخی چیست؟ او می‌گوید اگر دشمن می‌داند آمریکا همیشه محدود و قابل‌پیش‌بینی پاسخ می‌دهد، پس این پاسخ دیگر بازدارنده نیست.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68476" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68475">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:  در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68475" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW6gKbDCuvOA7GQVRWw4PKvNTnNKqO1MwnV1ECzInUdSYjd2y5J7I49zRcE2IoyFpES5oXDRe2xXWfLAI2mlHqROWFjXldIFXswJERboVI_q2xcURmkCzsft5VmjMUVQBd1UnYxsnj5J68mHGB0D9Mj7TbmLmdZIYekZlppO0tBsWgh_rMVGjdjKlWo3B3bcTTuv3ymymfbKRPf8zGn0T49vkXUr6DzC0FjdWYM0zkSwBfmbBuogGVxE09DzZsRIEHykCyB8_hqrNwjW3cE3WvS9AV_-SX3VIaSsMMtZ7J8cF9MfPsd4JGjr6E2fQRDTjiWXHfqZv0jLcEPOiK9T8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
در تاریخ ۱۷ ژوئیه، دو تن از نیروهای نظامی ایالات متحده در اردن و در جریان عملیات دفاعی در برابر حملات موشک‌های بالستیک و پهپادهای ایران — که توسط فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای هم‌پیمان انجام شد — جان باختند.
همچنین، یک نیروی نظامی دیگر در حال حاضر مفقود است.
چهار نیروی نظامی آمریکایی برای مداوا به بیمارستان‌های اردن منتقل شدند که همگی تاکنون مرخص شده‌اند.
سایر پرسنلی که به دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به محل خدمت خود بازگشته‌اند.
سنتکام به احترام خانواده‌ها، از انتشار اطلاعات تکمیلی — از جمله هویت نظامیان جان‌باخته — تا ۲۴ ساعت پس از اطلاع‌رسانی به بستگان درجه‌یک آن‌ها، خودداری خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68474" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=Roqr3LOFJKQSEPFeoSk7eoK6c_A-fFYDRr5mC1anMfTzRnU5gnCwN5bu2deFCgyNWfRoJu6J9u5_1OYOx0gTGPjjB6ANKvSjSmYqwqbdan6aaduD_cnJeElV0El1MrEXHd-ZmjxuQdWFspYYCzepIfXMzJ1F5d1TnpkyfP2793C0heWOcknbm907ejf4SgYTRQ11WihRXgEm6OZshT3NM8fbdiT-D1uLWhR6VCbw-MSnQjVnZ5o2yRpIcUilHKPNukzQFl3UWffy-BdNMvxFW0nscU9L_6Pt95uihStxV6WnK5TfIyarP76NQgeW1m2Y6ayuojsNMrRebgYIjn_vDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7081b32d41.mp4?token=Roqr3LOFJKQSEPFeoSk7eoK6c_A-fFYDRr5mC1anMfTzRnU5gnCwN5bu2deFCgyNWfRoJu6J9u5_1OYOx0gTGPjjB6ANKvSjSmYqwqbdan6aaduD_cnJeElV0El1MrEXHd-ZmjxuQdWFspYYCzepIfXMzJ1F5d1TnpkyfP2793C0heWOcknbm907ejf4SgYTRQ11WihRXgEm6OZshT3NM8fbdiT-D1uLWhR6VCbw-MSnQjVnZ5o2yRpIcUilHKPNukzQFl3UWffy-BdNMvxFW0nscU9L_6Pt95uihStxV6WnK5TfIyarP76NQgeW1m2Y6ayuojsNMrRebgYIjn_vDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
اگه حملات آمریکا تا چند روز دیگه ادامه پیدا کنه، وارد مرحله تهاجمی کامل میشیم
اون موقع دیگه فقط جواب حمله رو نمیدیم و حملاتمون گسترده‌تر میشه همه جارو میزنیم
آمریکاس که ریده به مفاد تفاهم‌ نامه و همرو یکی‌یکی زیر پا گذاشته و عملا از تفاهم نامه فقط اسمش باقی موند
آمریکا از جنوب لبنان عقب‌ نشینی نکرد، توی تنگه هرمز مسیر غیرقانونی ایجاد کرد، به حاکمیت ایران احترام نذاشت، به سواحل ایران حمله کرد و اموال ایران رو هم آزاد نکرد
دیگه نه روی کاغذ و نه توی عمل چیزی به اسم تفاهم‌نامه اسلام‌آباد وجود نداره
اگه دوباره مذاکره‌ای شروع بشه، از طرف آمریکاست و اونه که دنبال نوشتن یه تفاهم‌نامه جدید با تغییرات تازه‌ست
اجازه نمیدیم نیروهای دژمن از تنگه هرمز رد شن و وارد خلیج فارس بشن، چون امنیت کشورمون به خطر میوفته
🌅
قبول نداریم آمریکا توی تنگه هرمز، که گلوگاه انرژی جهانه، نقش یا حضور داشته باشه
آمریکایی‌ ها منتظر موج موشک‌ ها و پهپادهای ایران باشن چون ما جواب حرف‌ های ترامپ رو توی میدون میدیم
فعلا سیاست ایران اینه که هر حمله موشکی رو با همون شدت جواب بده
انتقام خون فرمانده شهید و شهدای جنگ رو میگیریم
آمریکا میخواد با محاصره دریایی، مقاومت ایران رو بشکنه
ممکنه دوباره به سایت‌های هسته‌ای حمله کنه یا بعد از اقدام نظامی، ایران رو به مذاکره با شرایط جدید مجبور کنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68473" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68472" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68471">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=drLYxriB9D28IqGzP53YAgJVszZ8ytJBnTsXP-suP-titF85oCFqNMvmZHQHW7bbMMKbFSsU6NltfYkuHKf_VEJxlvu6eSL2dNIP18KEEFhGQwzv_hcWCnvKg9Vf-roA9IGgmp8RQ3SdkRF6AwU7eZWyzRRMEfsLWFxYSw0Ikkidz3f9UgzuvCeEa9U0H_kGGsbVO64bLlxM3Jt7pqf5cKM52uK3XZd6f_ZqjCOztRo5N_rp4_zG-EAp03vujPw3jbQHryf8QVdaABDjlqBgI6Mosi85brW0h7Q-0xPnqqF12fQCuAu3y1BwRKeYqmgsp-rhmIimcNWenlOsQF4lww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=drLYxriB9D28IqGzP53YAgJVszZ8ytJBnTsXP-suP-titF85oCFqNMvmZHQHW7bbMMKbFSsU6NltfYkuHKf_VEJxlvu6eSL2dNIP18KEEFhGQwzv_hcWCnvKg9Vf-roA9IGgmp8RQ3SdkRF6AwU7eZWyzRRMEfsLWFxYSw0Ikkidz3f9UgzuvCeEa9U0H_kGGsbVO64bLlxM3Jt7pqf5cKM52uK3XZd6f_ZqjCOztRo5N_rp4_zG-EAp03vujPw3jbQHryf8QVdaABDjlqBgI6Mosi85brW0h7Q-0xPnqqF12fQCuAu3y1BwRKeYqmgsp-rhmIimcNWenlOsQF4lww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68471" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO) اعلام کرد که گزارشی مبنی بر وقوع حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی، در فاصله حدود ۱۰۰ مایل دریایی به شرق شهر الدقم در کشور عمان دریافت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68470" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
تفاهم‌نامه بار دیگر ثابت کرد که امضای رئیس‌جمهور ایالات متحده هیچ ارزشی ندارد و هیچ اعتبار ندارد، و مردم ایران درس‌هایی فراموش‌نشدنی برای دشمن آمریکایی دارند.
امروز، "شیطان بزرگ" بار دیگر بدون هیچ پوششی، چهره واقعی خود را آشکار کرد. این تجربه تلخ از جنایات و نقض عهد، مدرکی جدید و قاطع بر دروغگویی، بی‌منطق بودن، عدم شایستگی اعتماد و فریبکاری ایالات متحده است.
اکنون که دشمن آمریکایی در تلاش است تا جنگ را شعله‌ور کند و هزینه‌های گزاف بیشتری را متحمل شود و اعتبار خود را بیشتر از دست بدهد، باید بداند که مردم عزیز ایران و جبهه مقاومت، درس‌هایی فراموش‌نشدنی برای او دارند. در این روزها، شجاعت رزمندگان اسلام و جوانان مناطق جنوبی، نمونه‌هایی از این درس‌ها را نشان داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68469" target="_blank">📅 20:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای ساعت ۲۰ پیامی را منتشر خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68468" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68466">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
هم‌اکنون زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68466" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68465">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZuf4sfWlmDuhcO8mCgABhWgcEDFa-9vg0hG0CIubz--z1heWFhw9fmc8Gm3j3wfzEp-hlALzdoz07Bj0w06p_MZkMEFQmCgtNX9013Zd8MRvLgO7UBnC4AyMI0FoVFOVdZLDHjF6GXFSl3sQoXTu-gV2lA-CbuhlEV9iaCfScLvVdvOd4tomttbsxJ0O3azmPMW5bqOkC6J90LBpPN-jmbHAXeZd0vOP3P18ZxbFo8EoKnaVQ1BSe-z267lMFusvQX0Offsi1a6DIzE6_bgsX4kGXb25_U0pGQoCcs9BynvMQ0AMujnAfBbizNNW-JjXVRTxd-yfCqs3Zsql6ijcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان  @News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68465" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68464">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
گزارش های اولیه از حمله به زاهدان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68464" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68463">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=mg_riPl1FIUrEicnrrqqAAv_pM-FVhXzb_UF2_Xi_WcHK6LkFPoWksTX9z0yWFc0fUrhA8GYcrwdm_QjVzQ8x-x1tYSqXiIZjcf7vz7ZNdwTZMD9yxrrip6e-_9lnK2WGf5tl8nrl19Y8_mT163VTuWzUmCl56m5f3gj00C2kzWwVchiiTOKvfPtXDh_8NnCJr2BcFChvrtgl0clV3dv2XC6e0cn1E_ki8Nx7l6VMe-pmr5mpGb3sat5c_k1055UcqQn-1pJxvn019SJ9PHO3bzgse3uMBv4q1OuJe6wFF3KdJu5bGZXkHc4_jIv0dI3sl4CnDKUDDUHThyeOUf5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739a0556b.mp4?token=mg_riPl1FIUrEicnrrqqAAv_pM-FVhXzb_UF2_Xi_WcHK6LkFPoWksTX9z0yWFc0fUrhA8GYcrwdm_QjVzQ8x-x1tYSqXiIZjcf7vz7ZNdwTZMD9yxrrip6e-_9lnK2WGf5tl8nrl19Y8_mT163VTuWzUmCl56m5f3gj00C2kzWwVchiiTOKvfPtXDh_8NnCJr2BcFChvrtgl0clV3dv2XC6e0cn1E_ki8Nx7l6VMe-pmr5mpGb3sat5c_k1055UcqQn-1pJxvn019SJ9PHO3bzgse3uMBv4q1OuJe6wFF3KdJu5bGZXkHc4_jIv0dI3sl4CnDKUDDUHThyeOUf5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
این ویدیو کامل نشون میده که تحرکات هواپیماها های ترابری امریکایی از سمت اروپا به خاورمیانه بشدت افزایش داشته.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68463" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68462">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7jfb3t99AxlKZn6IjKaAW5VhjkhP7R7Yevz0CFP5M-_gKVtfnW5TXli2VpEmf3VgZvx6TdMmnAaRrgkDlsPq3H5Twxa70xHTzvE_4RnC7T9FhPZD-yallyZs_cYFxAKkZiZKd1AZXDEUvbyleLZlUCjTpRV5UOTZEh1QdkU_zMnmAEh0XOuHSRIRoe0oXZaXBWax1gjDFI6MSDR-Yb32Y0uNMHdZR2ETejzWhpBo26-qlsKPnJk4ko1WJX-rMHPh8HFQo-AQUjIWFT085TOs4bfhgL8G4kTzWkOZfJ4Jy2RhEf1HfwHl0t3G3vXY-WsGUqioG2NZZHlHKX3b4Ymwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز چندین جنگنده اضافی به پایگاه‌های آمریکا در خاورمیانه اعزام شدن و 4 فروند هواپیمای سوخت‌رسان KC-135R هم اونا رو همراهی کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68462" target="_blank">📅 18:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68461">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g71xko1sbeurfUsFBA0y2-StrtzT6Dr7AwdMclyRL8_3Cvaa_q1M79E9pcHGJpnk1xCWnmUg1CbXQtDTJ3V-6UmfoV7eUI2RyTg2eayD_TALzDkhG0QAWWGm_FfmHvu6nNgjI-eDtR87TU5f5uLuMBFZLsl-ZiEtVYQkabU4pMo5CDozJcZcnIE5-FvhboAd252jugqyKkVNG9RNE9zyNguie56Cbexmkkz0HWIE7wst9N7t-eZ7XXzv8g67-JKYKP_mcfghdl6ezcgJzpa0PB1kvW9na0L8TOdeZ5QbjeJfGLSLecJP749xJOSYHi0xj8ylVc82rV71QpQgYMTGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نماینده مجلس:
بنزین گزان میشود؛لیتری 10 هزارتومان
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68461" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68460">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:  «اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68460" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس:
«اگر ایالات متحده امشب به زیرساخت‌های غیرنظامی در ایران حمله کند، برای حفظ جان شهروندان این کشور، باید فرودگاه‌های دبی و ابوظبی، و همچنین بنادر فجیره و جبل علی، فورا تخلیه شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68459" target="_blank">📅 17:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68456">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=i1xh-t5bJ1Sry95uLnVBk2jSn5bbxY3UE5UNVGzpYNsty5EyZoXkiVEe90ipnw2HOTZC83EvnqWSvV7WrlB8KLr-uJPB-D4QUQmXzyB231xokaooBxOnwvSb3HuolUzBq0LgMxWymuzMpuCEEENAS4BtMkNKVPJmzllpII1JlGSk34dNmttsR-nRwFbRHhCvxaRPn5jaHI7glxqyejROS9R9TZRR4htgSoC02u0GGgA2VXP5CvDl_TBj7At45rdKG2QM3QPf6q3GsJQ8Fn44HBzDWOC_isBJWOeGqWIMFOpmjUwzn8uTcclmAMAwLFF2oJVBOzYiz9vmTHs-XTFJ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f3f310f.mp4?token=i1xh-t5bJ1Sry95uLnVBk2jSn5bbxY3UE5UNVGzpYNsty5EyZoXkiVEe90ipnw2HOTZC83EvnqWSvV7WrlB8KLr-uJPB-D4QUQmXzyB231xokaooBxOnwvSb3HuolUzBq0LgMxWymuzMpuCEEENAS4BtMkNKVPJmzllpII1JlGSk34dNmttsR-nRwFbRHhCvxaRPn5jaHI7glxqyejROS9R9TZRR4htgSoC02u0GGgA2VXP5CvDl_TBj7At45rdKG2QM3QPf6q3GsJQ8Fn44HBzDWOC_isBJWOeGqWIMFOpmjUwzn8uTcclmAMAwLFF2oJVBOzYiz9vmTHs-XTFJ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی در کویت به دلیل حملات موشکی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68456" target="_blank">📅 17:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68455">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAFKVLJNa0Z0rEBjN6PwsML9B71Fnc3cYF0Z8885xVehaTI-HWeWd-dTcIaSXzjqvo3GToUEghQI9fC21fsud88A34sr2yEIv0OLVz3Bkd-sbh2LZdTlcwmrAUxU49ZAMLIoDm5UhGYL2-W0x4bxRVGPQ11tyrNrtwWdcZkWtH4QcJ_S0416wqkol-epLVw8AF2e2DLrdrX6cS-vgD4EK2gyZ4itfe1QCWk8PGReElAQJiRfiuKvMBZZ-V-LrNl0jWeiGIj36IR1CHWS0-hy6joZTxOZQdz2_22-lcx99127JM-POy3nUKdROLUHJWU2bCRG0yoLn8EcyhaVNiIl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛معاون وزیر امور خارجه جمهوری اسلامی، کاظم غریب‌آبادی:
«از این لحظه به بعد، ایران اجرای تمامی تعهدات خود را بر اساس یادداشت تفاهم، به حالت تعلیق در می‌آورد.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68455" target="_blank">📅 16:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00f574479.mp4?token=TLSlBt7HMHMfhhCaE4m5LFXxW573jbzxIjbDjBWcNRL33K9zYWVIlDQeKRpDYKl3v_DHNq19qgphM2PfIsZ5z4fQGeja8D-AY-9Z5NGDhvsMe0AMjfeEd92_MHHZ003nF1Hxmtv2749jNhxXpvOnPQoWjuGneNHjmaXWXulRX81NAMW-GRj33Y1u7tO4d3K_C5K7rTDz3hlDtkKQKHRp574Gwqgzp6gsoLdDWNJ7iEloxABRWJdcnnQNyHl9sfbOxcyr_GByr3TjbhMxeb3LFt5oHdspAH_EcuJFbmju_c_bBkSZAWpTWCm8X3nXUq6nuJZxsDSVH7MpYImLTqMW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00f574479.mp4?token=TLSlBt7HMHMfhhCaE4m5LFXxW573jbzxIjbDjBWcNRL33K9zYWVIlDQeKRpDYKl3v_DHNq19qgphM2PfIsZ5z4fQGeja8D-AY-9Z5NGDhvsMe0AMjfeEd92_MHHZ003nF1Hxmtv2749jNhxXpvOnPQoWjuGneNHjmaXWXulRX81NAMW-GRj33Y1u7tO4d3K_C5K7rTDz3hlDtkKQKHRp574Gwqgzp6gsoLdDWNJ7iEloxABRWJdcnnQNyHl9sfbOxcyr_GByr3TjbhMxeb3LFt5oHdspAH_EcuJFbmju_c_bBkSZAWpTWCm8X3nXUq6nuJZxsDSVH7MpYImLTqMW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
چند روز پیش یه ویدئو از یه پسر نوجوون وایرال شد که از سرکار اومده بود و داشت موتورهای یه نمایشگاه رو با بغض نگاه میکرد و حسرت می‌خورد؛
⏺
این ویدیو خیلی دست به دست شد و نهایتا مردمِ نازنین ایران، تو کمتر از یک هفته پول جمع کردن و واسه آقا یاسین موتور خریدن و اینجوری سورپرایزش کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68452" target="_blank">📅 16:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون جنوبی:
همه دارن از جنوب صحبت میکنن که دمشون گرم ولی منی که خودم جنوبم نمیدونم چی بگم.
درمورد پمپ بنزینی که یکساعته داخلشم صحبت کنیم یا مثلا درمورد برقی که الان رفته و نمیتونم برم خونه صحبت کنم
درمورد ماشینی که نمیتونم خرجش کنم صحبت کنم؟
درمورد وسیله ای که میخواستم بخرم و امروز صاحابش 40 میلیون گذاشت روش صحبت کنم؟
یعنی حتی نمیدونم از کجا شروع کنم
ببین قبلا به موجودی کار نگاه میکنم میگم خب بعدا این چنین میشه اما الان تخمم نیست
الان میگم بتخمم ک میزنن نهایتش اینه منو میزنه و میمیرم
چرا برق بقیه شهر های دنیا نمیره برق ما میره ؟ ما اضافه ایم ؟
بدترین اب و هوا و اکوسیستم و بی برقی و جنگ مال ماست نمیدونم از چی باید بگم
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68451" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68450">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud9G6HLO_9ci7_VQowQlq46XIh4ou1HCyXXVgk1WRmDgJngEfJjvl6TK0NoXeT_Pwqdp9XcxRW4u_OE8usl-NUWm5DAlayaG_1VS1HZrkwD-n_hbHWLVE6_co-Vq6IQzlKOYFFppv8i635SPTc1gCvq_m2rHyV3PfpWQYDKdusPTY0OyjWHC4fELJhWaNF57CrxOMOU3SC-VgBpt81PgPsg7unbRaQt7UhBUos3DorZVT-YisbA_JN-tBoGddVc-uOIJUc5qIrHb0m-s27R81XxqWECSXEWaqhNeLzPABtoO03eoAC8pmhfRTxR4nG_mEK3wG7D5XHAXWMKM3zeOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حکومت داره به جانفداها زنگ میزنه که بیان آموزش با اسلحه ببینن و برای جنگ آماده بشن
😂
😂
اگه کسیم بهونه بیاره که مثلاً مشکل دارم و نمیتونم بیام، میگن اشکال نداره، بیا آشپزی کن یا کارای دیگه انجام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68450" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68449">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=fbuXT01ZOMZt6H_rQ7ys4G0guxCpD1Q7Gv9phYKV6QHDbqOjgKwr90V67F6CFgoLIOyG8r8qhxoqq9T8EPmHnYEfDO4mQIqeDg0Ph9cEm5Y3sDhaUjJaY5X6TJpnmWiTDege96L70H5UaXEKt4fkUqSfr1HBVzm7xpdSCjl2gbb1EyI0rNOleOU1v7ik4CRaIKzUf65OiwOe-6ND5wlq9rywjsgNUdO3ZZu5HELMyvHTKIggUL98fOIh4RCP6qJOac6zUFcsEnTtRd8tPzcFZrLvwwyhz54g0UZekeiZUlwoFYcgYO71fN96ka8rVNoF5XEiAeJfxgkgjDvfhCQL-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5326ecb6.mp4?token=fbuXT01ZOMZt6H_rQ7ys4G0guxCpD1Q7Gv9phYKV6QHDbqOjgKwr90V67F6CFgoLIOyG8r8qhxoqq9T8EPmHnYEfDO4mQIqeDg0Ph9cEm5Y3sDhaUjJaY5X6TJpnmWiTDege96L70H5UaXEKt4fkUqSfr1HBVzm7xpdSCjl2gbb1EyI0rNOleOU1v7ik4CRaIKzUf65OiwOe-6ND5wlq9rywjsgNUdO3ZZu5HELMyvHTKIggUL98fOIh4RCP6qJOac6zUFcsEnTtRd8tPzcFZrLvwwyhz54g0UZekeiZUlwoFYcgYO71fN96ka8rVNoF5XEiAeJfxgkgjDvfhCQL-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واسه دومین بار طی دو روز گذشته، جمهوری اسلامی به نیروگاه برق و تأسیسات آب‌شیرین‌کن تو کویت حمله کرد و باعث آتش‌سوزی شد.
کویت حدود 90 درصد آب آشامیدنیش رو از طریق آب‌شیرین‌کن‌ها تأمین میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68449" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68448">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN6PxxnrxQsMEt_xW0gJWD_X2cPGDehd50a2FyHOpIww9-7aMbLolTxvQivxigg_TISbAYK2Um54GHTR6MmNsmCzKnVyr95Rp4qjnTw1tgfebJMCgvjpPxZXfdAXwqSv3tFJ5B0Q9Nq8HP7FWkfGopR7kIuW3E5cAl7oPS1AyIPhBefLgut8j5kL3yVFtxcL0G5ItFsmnZ_o76xfca-GCoYJELTsySpzXsDVjHvUlJvcTMB1FbnKhbXhj1eVo5e1WeM_VFbR0SF3DHkmjpf7xpkXs1139wdG-ckf9k1QsZz0RLHYYP-g18eoDrk22lcn5gRuSeHv9DFKIMotTicM5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68448" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68447">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68447" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68446">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=r4LT05HGH68yaQr8SMVDdQ__fsjCGIsR4iu6FkGsTZqN0b6K7_7klOe5zIkAtMfY__JMguET7tOoGLnf0GXCjVd28tR4CioGM78sjdnWETx8wyFvHQ0fyXFXbrOUrZgdavN1Z0ldUusl9SjAGdGZi1i5fzqn0alPUvCVAXsKA4FQHAnN5bktWKrF3ycBG6-uRpyTvUE-ZtE8XMWO-oQpPPt5R839Y2d78gi4z3ORqSIwVDMV55knqYih9QirZJYQCoj9yul95mxm5epUNN5vpConKLi3nLirQu_51p-8k59VH2-hMqJg2t6SrT85wgLVL7USR2FDbz82v5qLuyJqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=r4LT05HGH68yaQr8SMVDdQ__fsjCGIsR4iu6FkGsTZqN0b6K7_7klOe5zIkAtMfY__JMguET7tOoGLnf0GXCjVd28tR4CioGM78sjdnWETx8wyFvHQ0fyXFXbrOUrZgdavN1Z0ldUusl9SjAGdGZi1i5fzqn0alPUvCVAXsKA4FQHAnN5bktWKrF3ycBG6-uRpyTvUE-ZtE8XMWO-oQpPPt5R839Y2d78gi4z3ORqSIwVDMV55knqYih9QirZJYQCoj9yul95mxm5epUNN5vpConKLi3nLirQu_51p-8k59VH2-hMqJg2t6SrT85wgLVL7USR2FDbz82v5qLuyJqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68446" target="_blank">📅 14:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68445">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⏺
وزارت نفت کویت:
خسارات مالی سنگین در پی حمله‌ به یک تأسیسات نفتی‌مان رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68445" target="_blank">📅 13:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68443">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=Bve9TU6Sr6DPV1nZeBDivHbFgJ6e7rldstKYs0FusLKjONb03GS_9EAcZhRtzJeecyK55X2IhXTHkkQDznmQ9KwYRD3XlJOgtAzUVXMOK3iUg1ss2HWB9BNhVaCSCWf9U1wCRXAOZ_NOZJNStdoBBzwQsQ1eVExbPauCr74vGHhdI55Njac7VkcsRgAVEncQrpu4aAloSuEVdcl3RoVO-KHL7ER76NyCj4w55gXtScNEusCm6iySrRea1PHmD1TF3wP_HX7EcnjKso6CX33dpZNq-BrJzLmAQyYVsb-4cMzKk3oAQRXrUNzGZePOZ213gmtmhYMWnMFbccVIrVQ2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aabd1106.mp4?token=Bve9TU6Sr6DPV1nZeBDivHbFgJ6e7rldstKYs0FusLKjONb03GS_9EAcZhRtzJeecyK55X2IhXTHkkQDznmQ9KwYRD3XlJOgtAzUVXMOK3iUg1ss2HWB9BNhVaCSCWf9U1wCRXAOZ_NOZJNStdoBBzwQsQ1eVExbPauCr74vGHhdI55Njac7VkcsRgAVEncQrpu4aAloSuEVdcl3RoVO-KHL7ER76NyCj4w55gXtScNEusCm6iySrRea1PHmD1TF3wP_HX7EcnjKso6CX33dpZNq-BrJzLmAQyYVsb-4cMzKk3oAQRXrUNzGZePOZ213gmtmhYMWnMFbccVIrVQ2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
موج جدید حملات موشکی و پهبادی سپاه پاسداران به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68443" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68442">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=ChJJSe0dzEJqxgKi9_-36yd5m7UywyI_0g-q0Uli-eYSmBKNXvlwcsumL4CKy82fMmrxeGUGQVbRJaZeFb-h56iOBXVb96HsgXsFgPsOLnH085BhF3Hv8TymD4m8rUC1zBfuO23aoM2etsC23NyqpFTAyHIgMpbEJXZh7ufv-lv-GQkLw7H5MblVN6G5TuJh-cLz2AlvbgXNdjiMia-cGxuOzI5tmaUto3osyCOT-EhBKrPNwxPmlZ7aAiOtihdoc_2tGpsYWQLWTVfmETsLICX82OcBA5Zwof7BBdY5zPfzp-Cfo-gNTYiCKoA6COVTaoNNTifjVf6vth25P4774g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc8bace1d.mp4?token=ChJJSe0dzEJqxgKi9_-36yd5m7UywyI_0g-q0Uli-eYSmBKNXvlwcsumL4CKy82fMmrxeGUGQVbRJaZeFb-h56iOBXVb96HsgXsFgPsOLnH085BhF3Hv8TymD4m8rUC1zBfuO23aoM2etsC23NyqpFTAyHIgMpbEJXZh7ufv-lv-GQkLw7H5MblVN6G5TuJh-cLz2AlvbgXNdjiMia-cGxuOzI5tmaUto3osyCOT-EhBKrPNwxPmlZ7aAiOtihdoc_2tGpsYWQLWTVfmETsLICX82OcBA5Zwof7BBdY5zPfzp-Cfo-gNTYiCKoA6COVTaoNNTifjVf6vth25P4774g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپهبد خلبان نادر جهانبانی؛ میخواهم شاهد پرواز گلوله ها باشم
🫡
نادر جهانبانی (۲۷ فروردین ۱۳۰۷ – ۲۲ اسفند ۱۳۵۷) سپهبد خلبان نیروی هوایی شاهنشاهی ایران و معاون فرماندهی معروف به ژنرال چشم‌آبی بود.
وی بنیان‌گذار و سرپرست تیم آکروجت تاج طلایی است. از او به عنوان یکی از بهترین و برجسته‌ترین خلبانان عصر خود نام می‌برند.
نادر جهانبانی دانش‌آموختهٔ دانشگاه خلبانی نیروی هوایی روسیه و آموزش‌دیدهٔ دوره‌های خلبانی جنگنده‌های جت از آلمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68442" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68438">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=ou8zJTpc2IRfF8RNZOhgyZxgCyjSLAiV82NWR-ejW4WHXtNVPyRRiO-gzsU30sd_gTxMMYzavKOlxgdBJuf2KGAah6Je41jMI_39-78mN9IamHvx3FwnJ91VpHVG9adW0Xw79SfYb2RgAYcJuWFXUkT5r2eybnBCE9L16b37URq2EO8QxN-jC1__NZGToZdhHYvq2NLCxeasvrcjLj6bzHQndaLRSJl7fxIF4Xma9sn52fO4AyMN2DdXPkMG4Da_97dWbu0qAYvtzeoidxrJ8pJEoN4wZOvfSTl6ozDmZGfwrvq95stMUAyo37zseBfE59aBA9J1c-vcX_97-2JJQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc56ea3cff.mp4?token=ou8zJTpc2IRfF8RNZOhgyZxgCyjSLAiV82NWR-ejW4WHXtNVPyRRiO-gzsU30sd_gTxMMYzavKOlxgdBJuf2KGAah6Je41jMI_39-78mN9IamHvx3FwnJ91VpHVG9adW0Xw79SfYb2RgAYcJuWFXUkT5r2eybnBCE9L16b37URq2EO8QxN-jC1__NZGToZdhHYvq2NLCxeasvrcjLj6bzHQndaLRSJl7fxIF4Xma9sn52fO4AyMN2DdXPkMG4Da_97dWbu0qAYvtzeoidxrJ8pJEoN4wZOvfSTl6ozDmZGfwrvq95stMUAyo37zseBfE59aBA9J1c-vcX_97-2JJQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🚀
🇷🇺
حجم آتش‌سوزی در مسکو پایتخت روسیه بعد از حملات پهبادی اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68438" target="_blank">📅 13:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68437">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=uoerknm_etrg-2DFY8qr5cGoiD-OlDOeT7ts7nLySh-MBC90Sx5ZhsJTcFIEl21VvF-gX4XQ1io3vKhk3V9-GChMq64PEreKaa85oH6hjhhHuvw8N-kmNYUtrQH6dTMYg5A6jospDWQ7ioJT2Ww0fcI8PIvqX-0z9H7ky26sWm4d9undRUaX9Vp7h-1w_ozmqohbZlJNqk5I-wFIR51Hno19l-NT0ESFASDFgklPFvLJemz4JIN4bxQhWhyXlIG8igRlCMjy1Nj1IkFS_nqSDF50BIaiy7Hzi8y6mE2RbBERQSjvV0h6TQ9Q3P2lxEo7bLvI94j1VAIwoud5KxGIlD1S-RBlR-Zv1QRBlOvlRoMzAnXGW9LZd9iqkT5FX8qM0v6mVzpfDRJkUITdcWr6Ra7AwhXrQTZ0Q1RpOsnzP6QbKKRTySEx5p65hZInvtb26vrIlVlCPZZRymGqYhBzBvwOCQorzLLeQ84GeEwjA0LMxEFI4w1Kcp_7XAJGORPIccSpYNgM-6rKFe2Z83tokaqlGGaStdR8NESvePqRZ_e79eVj8lvqqwrhw6dqVx2CheG-aum4vtJQbzrbf7XNiQHMOJTEFI5z1GUGwdsNuSMPo-YMppZT8YQ5xjZuEpsYc2GhSlKx-6N5wsyxm_s17BdSm4I-beXVTQS2-C4k98Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe648570f6.mp4?token=uoerknm_etrg-2DFY8qr5cGoiD-OlDOeT7ts7nLySh-MBC90Sx5ZhsJTcFIEl21VvF-gX4XQ1io3vKhk3V9-GChMq64PEreKaa85oH6hjhhHuvw8N-kmNYUtrQH6dTMYg5A6jospDWQ7ioJT2Ww0fcI8PIvqX-0z9H7ky26sWm4d9undRUaX9Vp7h-1w_ozmqohbZlJNqk5I-wFIR51Hno19l-NT0ESFASDFgklPFvLJemz4JIN4bxQhWhyXlIG8igRlCMjy1Nj1IkFS_nqSDF50BIaiy7Hzi8y6mE2RbBERQSjvV0h6TQ9Q3P2lxEo7bLvI94j1VAIwoud5KxGIlD1S-RBlR-Zv1QRBlOvlRoMzAnXGW9LZd9iqkT5FX8qM0v6mVzpfDRJkUITdcWr6Ra7AwhXrQTZ0Q1RpOsnzP6QbKKRTySEx5p65hZInvtb26vrIlVlCPZZRymGqYhBzBvwOCQorzLLeQ84GeEwjA0LMxEFI4w1Kcp_7XAJGORPIccSpYNgM-6rKFe2Z83tokaqlGGaStdR8NESvePqRZ_e79eVj8lvqqwrhw6dqVx2CheG-aum4vtJQbzrbf7XNiQHMOJTEFI5z1GUGwdsNuSMPo-YMppZT8YQ5xjZuEpsYc2GhSlKx-6N5wsyxm_s17BdSm4I-beXVTQS2-C4k98Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حاضری به عنوان یه جان‌فدا، بخاطر مملکتت، بخاطرآب و خاکت بری بجنگی و از مملکتت دفاع کنی؟
🇮🇷
جان‌فدا : آره، من بخاطر مملکتم جان میدم.
🎙
خب الان بیاین امضا و اثر انگشت بزنیم که بریم خط مقدم جنگ.
🇮🇷
جان‌فدا : من بخاطر مملکتم جان میدم، ولی الان کار دارم، شما برید من بعداً میام.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68437" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHeSYXrWUj9E8QhTh_OADZiXMtUZKHz8tcfo9IRa3L2cKGJfSImZhNmMszN6Q3Mc-4cPFOLOKWFF5LNEDqQvcnUDcNjezVXNyEJrneM_jiy-h47cD0py7HuDqkSUJvrruu-4utukcElppPQ4-OQ-gWGvPMAu_ph6jWAN8ek3TQkz_kkGjc_MgbZ91WWekkvgijccL4haakJCquUwWiXZvgUmKGr2q2QifBaXGRhEGSh5pPo59Xq4it4spHm8QNHqvKWtBLkQtnL5WPlr5xDTKExId1g2-kjWWrINRLQ8-C7hKgH7Jm28EBQxPJUWnCJjy9AtVpLNayKxP29VZtc28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDD7yhD5bx0MUc8_0VQJcZRjy-XwstBO4BlXwqdObv2qhFJvSXbZ4ctRVp0BhaTwYdx7E3M2B5Y3gO05dTM_MatgSZBKCmYd91EUPJtkYljnzXv_OpypMjzeLgH9xBFOTUKxBVcs5adtYQhTOlPPPrL1HqAthZEqGMjzJCV1BZQ64_qukQoi1kfYmTP4LHtwaI_Muq6wurRjr-8ngo4G33V99a1_-YuTwj7-lE6ngPdTgJ0Hj_drJFt81CYMYEyRqVc3OK0l8HJ6w3bR1YGh7t8V2S-SHBkCnLHXcLS03j9AUtHN1SP1pdwJcWx8IHzbyu0xdjSslX9N_ea4eniXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_EYsXz2DjSlYj7hqkoX7Caj9OFxm4fZOuEM-Im81nfMAeurGmLqFjxxos5Q1TyKhpwazf86msDZfoQIf9jVxGTqv9ZBzgMujYs_wjoijnIJPGnUcoeW24zarail-Acd6EZOI3-UL0GQbdxmn1lQFU4FEwx_3eQ-Jv0YUjDBAcwBE0C6ZbcOyp_DhjE3I537-v0CEqz1imajuoh2xFXaodspP_JeOJm7FrOInIm4Qwuf4Lt0CLHUdpPDVC0vmNqOZFTcKfpRfWI7EUnmUFSD1LxDKkUnJmMXMU-pbprKaeza1BOhLTvvr7AVQmrEzz2UIK9Ea2EuAifiqAfH0COlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-0fgbN9todbJt-mkvw77z3xxojRmI3H-Up_rBht3RYgqqACDJuVQjQWJ5doFnK58XSTpPNnqB5YYdxkYJpTzi35uxvYRd2WFi37m3_BlysosTVZUOZeVllO9kjnJ-UHvbgRxHp-m3wsU4nF00dgQSATonYcCyL4oevsVouo4f9lCgYWKYqce4tZy6cdQXwCMM19lK_dDFFU-B1bhfUojyrf0xcu43ho4FrP-6vdULYsiyZ1TzhlMRgzbkXHaUY0ENJhJnF1j_gW29Fnpsh2vFgn2GJLOd79k6HR1jBZ4S8WefriWrPPuK1sV-p1aTIWutPWo5j5dvdn9hkNYI6dMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXh0IAsZ7Tpl87IV-0FChxKXRWozDYDZrCrYRixtdaigF8-YwKGopGSPCQHR-zEMAshkoCnFmT8VS1JeiZNpzH73-u1_kyhj7u6J1gE35LNBqpPszCL6tpxhjjCrResXbTZJxVIBba9K4FEDsbtAxjCPzdlQkapBm30I1U90hOgcUNboTu_hk3YH1-iRlVcKpaqNlHmv7ZQVzz1ok04GeMoqZR6pKt4-UQQkrwjasMUCwqHaHx30InO1nJsT-iOP88roxTTpzZohud2-r8fzEv1elzp1kKzN6b8l37BpESQyF5Gt9l7Kc9fepqPPrRUb9vZtAbRqRGPDgidiRdLcIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kqNVTEpjphkv51efRGIYiVCLNT3kctYByCTottKdgvYvfhfBeaIm3Ps84Q_DLxb-6xE1SC17KQO-5Ve01Pq6JCX73N1sh-ND4K0CWxpyfQz_p3T9HZ1q8W_ctuJ1CvuXmxNEUwuUxx9Q_D_KiYNReDFVY_LDPHWAe1jLR-Yotmt4yTg-lfi34A1eaRURpMbbR4XO9_6cXVEC2Qx5dpalhsp6a_0bjh4VbaAcccznXnlg41rnmScTbvyKZr9QAzvmj7Dwz9IMSgF9fZsspooY1TtcBkWBUEboRfvWjXMnKp7YzQ50OkIzQj2l7XbMTSPAOIaQ7KROVN2kHpLHcKDzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Om1LFQmmn0LUoQh6toVBS0KOyKAoDHfHdNj2P-esxvQvXn7TROcJ3aUbXDtdrURvh9V2h2J5ZMIFZN1tdIQcDecWFF3H4CLQlHlV7sGMCYdB0zHr3_N-TWOp5CbUpGKzZsJY_uCwt_W_PnlucJegmjzUQZ85sfxC4-GNUkrYAhEso_fMdzxRoRSJFp4R7jwO67uEQgb6VA2YPErhVa2taNay6XriqgIAuSSpyECsjQ2BGe-n9YZPD-HDriHPqnPIbhcZdcK-_jOVih4R7JR63bUmJeMCkF9WqSjn9xfqtzSFFRhNLahy6Qgj50oDCx1fhFw7Ppp8X6ADHIZhbfavnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXAf4AfAdOvHOS_A-lM65s7Lq3wpxT5sZOjIvomTsOAWGixfUNtUmjOJrGYaQ_Kfr1yjRyLgBTJSCLz863vcGCnSp9wiiPbze6my9EFMlQLDb6ZlC0iBswMgGK-I4JAtWpXwdtg-dFq02FwIXRgWY60rgHNm646OzN4IkyVW5645aazsqMD_dF9jl0JPlE8Zh5b3mz48tvIqlp7wqv36TN4KsemwYfL7XfqF8DZaJcm-4qXUWVuz-e1WvozA5QYjjYagyjNb8pnYGoqRVBTBMKi55dXTNSde_ADFI2McaWUg70iTDzU6YIvs30X5NBYrGSCaiRuTx7hrnRE77HKEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4meF3s2RPHKwCviyKTzC6dZV-r7ys0JHrJsHAjcCGvqpikpJMEwMUFqgRJFEtDzn5iSTdnhscLg1kebLJUS8cXWSlJqdK05zoK5dASZNiujj1VUk5MsI6HbneF4QuD8sVS9t-qrfO6685eqfihnj7LllEMT0j0Nsn4drVZgvvyyX1xZy1uWOb8HuiZGlEz6GZk3nsf_rT5JSVl5PaJ_8ozGgUjBn43XcY6G8lCJ5c-6iLoNuobuaEmDoYiGfCtxHMhcZ7HIlI6MKOQbvVvvYxXZQb-E_31_Kxh4-Sa7LaF2VvkPbfhOWroodC8th7rF-NRlyRtw-etSSDEj8xXS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oq0KlbX2K31A-mVY1iKw2ZYLfopf27S0hLjx7NeeBYLMAQIuRlX4nLseqfPYnwtySLgWZFqBFG0WwSwa9iSXxxrjLOwpVi2jHhwuLwrVVaGnoewWN_ZaMptQtmtKjcZCB9Ff2tqXY20AGSxTLrIcR2kqQ3God1d2gD2vjG8Ua2zd882yBhqksUtDDWjdIi8gBJykRZxbFTt2KxMcY2VLNPcscqBhTVql4o3WvF3WgDM9GpNktf0ryhFhLb58eGvnXgcJn5sxxTnApopT2erlgEkoh3W9A1-AOnG6Two8_Vvds_JryiUFQ1GEIt7HJYY5cnmHAeYol9RgcmX_kThiQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آب‌شیرین‌كن  بونجی جاسك تخریب شده
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68427" target="_blank">📅 12:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=lywc2_bFOo_p6fRR4eJkg7KRUQGpzVWgKyp7IYJcC4IJDulI-d2megk7fiQLoSJtfPB9VTCuopfl3LxHm_kNPVPSVz1-957XM1CdnuzKfhuy3hFmus9stpN94a2R8A0-dy5W8qPQFRJZrHauMdWGybcyr6ovlpn6xABP_81muoSaZl5-94QZukGszFw6YdkVxQBuVHezOIAd8izFSlUqY3TDsFPLo6ngjXzTClmzu0vderCBciPFsk_CDBgy-Sk5TpheQYFmYCtY7hqpA8mTqvhP4v6cQPYaUOgerDcA1E2bBBMMSf_kT2UbBw66hd2Sduguwjevrx5adv_UYZ9Pkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcefe98033.mp4?token=lywc2_bFOo_p6fRR4eJkg7KRUQGpzVWgKyp7IYJcC4IJDulI-d2megk7fiQLoSJtfPB9VTCuopfl3LxHm_kNPVPSVz1-957XM1CdnuzKfhuy3hFmus9stpN94a2R8A0-dy5W8qPQFRJZrHauMdWGybcyr6ovlpn6xABP_81muoSaZl5-94QZukGszFw6YdkVxQBuVHezOIAd8izFSlUqY3TDsFPLo6ngjXzTClmzu0vderCBciPFsk_CDBgy-Sk5TpheQYFmYCtY7hqpA8mTqvhP4v6cQPYaUOgerDcA1E2bBBMMSf_kT2UbBw66hd2Sduguwjevrx5adv_UYZ9Pkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تونل گلوگاه، در حملات شب گذشته آمریکا آسیب جدی دید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68426" target="_blank">📅 11:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68425" target="_blank">📅 11:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjD7bU2Dr5cHfsMkgQGDmn4sZTkviNwL753-5o4OMacTOCmUtsVSbn8C09V3iTbS9EvLPOYlzJrGVula1L4TcjIDg9CJSJ6gCUdd7hMMr5LeNfnOPBwCu79WaCmh3xbl06hGOwMsYsuNUrPdnTB5FtMf8-eMeWp00XBajcN8W1CoAch2xNgi2NcG6m57b1Anbu0yS5CC7SnFJlx77t_bk6ffpB13vd1Z595lzoCNNJm58K0uRKxFw66eR2YOcmwT8NT6fJYVThFjSxtX_9cSIKVACEsPnBMIdYOtuYaYAmw26SeCjMHvdyUdO-lRNWopp4g_Wx7E8R5xL07rvrjITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است که دو نفت‌کش در تنگه هرمز، پس از برخورد با مین در این آبراه بین‌المللی، منفجر شده‌اند.
✔️
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران، نادرست است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68424" target="_blank">📅 10:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=HzFrDmltdOQ5sAm8l3ITqZ0BX1UDyG4dXZMOnnYsYlaCNlTjlxJ-HWFcLpilJaY9HCHQZvFDpRNIGJwF9g_zmtxZfTCD7VAYerHieUg9ZNptyUhRk273SFAYrcysG-1Gcv0dHKZ0vzPjRHNe15TirRZUlRznTvd0nZqZWyDlDYUo5DUuJed34Qy6_PKrJfsmoeipexkujBMiqw2DOyEqgb1z4dEocIb5142Ovh0zuE8jPLYtDW36tN0H3yRGbG9lGAZjsJJdEL4zL455k7Ow4eA9yxNTJFnnDKJ1tTPpEFPCznb-1z0_OoYkk6vqYTEcbUizMoPtnPrOUe013eOqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a18b81da85.mp4?token=HzFrDmltdOQ5sAm8l3ITqZ0BX1UDyG4dXZMOnnYsYlaCNlTjlxJ-HWFcLpilJaY9HCHQZvFDpRNIGJwF9g_zmtxZfTCD7VAYerHieUg9ZNptyUhRk273SFAYrcysG-1Gcv0dHKZ0vzPjRHNe15TirRZUlRznTvd0nZqZWyDlDYUo5DUuJed34Qy6_PKrJfsmoeipexkujBMiqw2DOyEqgb1z4dEocIb5142Ovh0zuE8jPLYtDW36tN0H3yRGbG9lGAZjsJJdEL4zL455k7Ow4eA9yxNTJFnnDKJ1tTPpEFPCznb-1z0_OoYkk6vqYTEcbUizMoPtnPrOUe013eOqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه حامیان حکومت در تجمعات شبانه:
اشکال نداره زیرساخت مارو بزنن، مام زیرساخت اونا رو می‌زنیم.
بچه‌های فلسطینی چی بگن، ۸ ساله دارن میجنگن، مگه خون ما رنگی تر از اوناست؟
اگه تو این جنگ نابود هم بشیم اشکال نداره، لااقل ایستاده مردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68423" target="_blank">📅 10:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeLsc539IVeT1jhV-d4M92fzpAi31_y58fvGaG6rUPSCgIlkfnhzCLnRMEoeXF3fOixWpLBdj4x6oFwUkU1gQHtOhAuZrsm8k6wY6ff-HxQ5yWykXGg9b0efuIf-VZmKAatOc9TWPqR1WCaE8XPkrFUWJ47ca2nsCTRRKpd--lWXoubg36IkBmODns2IpbuBXaqfSEtG9Q44x-wTCQVL_VqqxVwrs1WELVOoYivcC2wira4JTpFEI9I9oQNq_4qWqUyM2JZX8d8eCj18NI_k0Mr7gI6d3ch1vR0I2Xdxxll5F3lZUXfftFn2KYVS7DbROxAOU30ZiLTeY_d5GPPMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اکسیوس:سه مقام آمریکایی و اسرائیلی اعلام کردند که دولت ترامپ به اسرائیل اطلاع داده است که در آستانه احتمال گسترش عملیات نظامی علیه ایران، ده‌ها فروند هواپیمای سوخت‌رسان دیگر به این کشور اعزام می‌کند.
پس از آنکه روز سه‌شنبه چندین طرح نظامی جدید در جلسه «اتاق وضعیت» (Situation Room) به رئیس‌جمهور ترامپ ارائه شد، او در حال بررسی یک عملیات تهاجمی گسترده علیه ایران است؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
از جمله گزینه‌های در دست بررسی می‌توان به:
⏺
بمباران تأسیسات زیرساختی ایران مانند نیروگاه‌های برق،
⏺
انجام حملات بیشتر به تأسیسات هسته‌ای ایران با هدف مدفون کردن عمیق‌تر اورانیوم غنی‌شده این کشور، و بمباران تأسیسات زیرزمینی «کوه پیک‌اکس» (Pickaxe Mountain) اشاره کرد که گمان می‌رود مرکزی در حال ساخت باشد.
ترامپ هنوز تصمیم نهایی را نگرفته است، اما به نظر می‌رسد مایل است با تشدید درگیری و وارد کردن خساراتی سنگین، حکومت ایران را وادار به بازگشایی تنگه هرمز و پذیرش شرایط هسته‌ای ترامپ کند.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68422" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68421" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARgO4JxAkJQKl1_cArq5u-eyMN_0z-DZxORt1e8WMCcZw6ZNR4eOLpF49OjJ3dHR3Aih45xJ4s3UG8SFjYQo1sb10sl-rgEfr6-18koKwvu4CmUxDTtjG_sXXriwAHVhONSBqTySnWIGElPUkdHiAiwcjs7L4OCKp_ub1oxePWQsdVjQiktvZqx_KXcNV_fWjk83-Dg8woLc0jNKdv7pCNpnwjNjzlWjQ5zQRl6ZBb-fSCy5Ai-HWS7Pv6YaZte-l8qSIdjbUSMHhmk3twgIiFpHPMCD2bq4PdLGyuVCXE9-3yB9IEp7Jra3kxU2OZUpYHlriMmEF_mgL0BM2Az6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68420" target="_blank">📅 03:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در جزیره لارک
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68419" target="_blank">📅 03:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1LpIfJai-X99Tg6anPoyU8mkMhi7Shlmckvd2IYpPVWSBbzxev946bhEjQFdRdjzTe7RM8eh7XG3yN2DXL_bpxlIN5x7uD4icm6jZO88GHFpoL9GvIyiZuv4Uges3COThdIZ7vQ68W6k-yp-OtQbyj8TrM1to1U769Z-DrceydvKZmheTdCOnhSIpNn2JbDJHEteCmPyiyhGfvLUh8J1u4_TL6SCtbHy3YnzXkpPuV3uZ_9AKUgzeoFBIpvewzWai2oYJtqTwQQyFZ4QNwWJXlW6kNPuFdTUoMeGAHP0bJgXZr30lAc6r2sSxjxQrcB9ouIO0Zf6PkSZdgKZV7Mxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۳ نفر در اثر حمله به پل بندرعباس_رودان کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68418" target="_blank">📅 02:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:    ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.   اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.  @News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68417" target="_blank">📅 02:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF26tQu74EUWCbS4yP9cWcv999ZHcQRNNMAWOxYEeNk62oVuOEsisw-fCzg2Jb3Oh3XphWYRulxLiOffdbNg2rg-s2CdMU3PTgUUToRSRGcQ-A2Rrlyfw1iQ7UOCD-7qAu2I9I21PyFOVutRZ3lz028gfKWPDRZFGLWqKvokaenhLP9vU8hUrEkxoLfC052D8pLpIGmVkAPLgWGEjvg7UpP-aDk6rd9HR42ozSV6qdErjWNtG_9a7vkbGuZyz4NwyLa2ZcH_bjoeOR-gQtPpCl_-Ftex7fN-ZzZV-wucdJpyB8PrvIWYuHevBG7WESDXmia_mPz9Q1NBVoggpiBdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
باراک راوید به نقل از مقام ارشد آمریکایی:
ایران یک موشک بالستیک به سمت پایگاهی آمریکایی در عربستان سعودی شلیک کرد.
اهمیت موضوع: این نخستین حمله مستقیم ایران به عربستان سعودی در حدود چهار ماه گذشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68416" target="_blank">📅 02:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏺
رویترز:پاکستان به جمهوری اسلامی درباره حملات حوثی ها به عربستان هشدار داده و این اقدام را تعرض به خاک خود تلقی کرده است.  حملات این هفته حوثی‌های یمن - که هم‌پیمان ایران هستند - به عربستان سعودی، موجب نارضایتی پاکستان شده و این کشور را در معرض خطر کشیده شدن…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68415" target="_blank">📅 02:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
فارس به نقل از منابع عربی:
حملۀ گسترده موشکی و پهپادی علیه منافع و پایگاه‌های آمریکایی در عربستان سعودی در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68414" target="_blank">📅 02:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=YSRfFlx6cCFIRV7LjuB6AThVZmWSnBMzWYL110NS8AWAR13MfM_KhtPWhpqgJ0Akg-2R8nG5xV9ZxAZ5eLhoZpjFQEpFJFDeh1X3mzqb6iREkgiKOGf0Ki8uBE1NBmXDBtohODQT2Kw3RD59XDdvdOYoguHnjmd0m2RBRtR4Yhla27TDlp61s-ByCadkeXZppcr2fOsltjUvuoHnpu1ke9yaLDKNWIeipXpWscMBFWmUWTVe-_z6NY_gbxwfqscgXK_ohg9yzJXpohJsbEmRwhQFSvq9A9AmyJ_YIcsZ1mmiEMAD1eIrz7oLvYbY4VXwWLQBuMJzfbZJrsC5PAlj2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4391e385.mp4?token=YSRfFlx6cCFIRV7LjuB6AThVZmWSnBMzWYL110NS8AWAR13MfM_KhtPWhpqgJ0Akg-2R8nG5xV9ZxAZ5eLhoZpjFQEpFJFDeh1X3mzqb6iREkgiKOGf0Ki8uBE1NBmXDBtohODQT2Kw3RD59XDdvdOYoguHnjmd0m2RBRtR4Yhla27TDlp61s-ByCadkeXZppcr2fOsltjUvuoHnpu1ke9yaLDKNWIeipXpWscMBFWmUWTVe-_z6NY_gbxwfqscgXK_ohg9yzJXpohJsbEmRwhQFSvq9A9AmyJ_YIcsZ1mmiEMAD1eIrz7oLvYbY4VXwWLQBuMJzfbZJrsC5PAlj2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پل مسیر بندرعباس رودان
بعد از ایست بازرسی چغازردی حوالی روستای سرزه پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68413" target="_blank">📅 02:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BESb266jnAZAAU5Dkf0xFfOBOA9mWwv31jOcJr2azHFlSGloy3DQg4gJ4-wIM9mt2B-4mfZsyDuzAAv2Vw1BOEDIZgQUkK_gGIQYFJqBJU6k_Uf4mwz3sBhQMV15hV7TdEUbLJsVSIMSS8Q7Y28W6lgf__H3IaTYJTHTSzNtd9aWUG5UFJWRsipAiCwYugRrtDZ4G9RWA7gdVQAWT47BSsdu4oOIoyiM6tqzYI7Vnbg_iErZBYvr_JGq6nrCjETZCb8_pNw0ZlhQCs_5b3IgHxr4g3E4jsk3DuaSBxuDDptYMEEbnUjFV2xWvEh7PS7ZAkYVVCrp27GDWrzhdBcC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیرهای هشدار در شهر الخرج، واقع در عربستان سعودی، به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68412" target="_blank">📅 02:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSp2V2Dg3kj151thNp8oxmqaDAxVX5mkLnGGquJnzwOZ-_hdUh8TgIcauy8JijBYubd10YRJdQG63SIDgf5-lMjcv6SXPiZzsZRt5oNmsvKBpGVWwrknGDT0XjnMnlnAiXZpjv2BVcaNz-RVB88U0jemzNGqwl_NKHJe_NHNh33Bs_0kP_XutHJ2fgG03unZf0Z5lildEC53yxgWaTw5HaL8-i4fegJMt2EQZF847YdQeYd1B4sUCyMwraNuRM0qN3zIdfXGOj8tgWLv0FQlJtqUdS7dXl41FehB_s3XXUJsQVaBzYNUJsHCIptJCRlCocj9EpBt7GDFDCiFbp1_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پل سه‌راه‌ میناب به‌سمت رودان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68411" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68409">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UO84gB-Ww2skvzcGkYT7So-TO3cE8sqIlGOYIFR88ZFZe24-DgzI4XcbG5T_gQuj5FQ5czF6wHk-md7Br-mYWc8BfDtITv0r2tEWzwDKzc_0Ec8CiDU9w110346e7s2pFmBFAYiccTUEjbB6x6l5aVl_H983XFVXtUzGv8x0tz-1GiK5TlbNiWo6JrcUIS_xo-At6l9httCF6TubdoC5IBlODLNF_iwjvdTDvB6kfYvrg-mRmASM2RVljX4w2Kwi6HFLIMf5aVK-6cit_Xs8cSoeesrhFhW0lGcDuJWA1S1_MFXfkVDpxbZf5RxfVl-NGNSoJKsIRmX0t90QucOt8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFkOPOCFc6ub-MBFICl_spvrvuaLBn9kLp-zTPpWBRv5jD3PjWI1B6Yy4vvjQ8LNfVbG9ZsZx4zS05xmA7dDKgokbv2LUVBAiSC4jQK3RXzqMybuC4wHDonQdBZn-higs_UpRzBx3ybrKR0Geck7VJzBBfFnMJHGY9BmWCFgPAqpTXlsXfs3z2_H6djjPXbYWoX8AXl5wwm6X_fVAqioWsjE0MZFJtHZ9cw0augFarahf37POqb3UG2zcU8PozoVCeZx7hDsbSx_fzLyV77wUrvF0Mo1pGS424Nso0_TaKiRQmSZZY9FQuy3MnJVmgc9vjgdBUD0DVscFIHG7aT-oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ارسالی از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68409" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68408">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=Wxalu9CG7_SrYo2NiDIcGHYnvF44yQP8LjeMD7IRwuMlppHmcaDVyavv5b5HwPs130Ji_OL46MOW7rd1EFVkhCxKyvamw0cKFd-VLfS_ZuGG2sQjdPlSZwS1RB3L3ucEB3fKLsgwkZk2hhgXzlblFQWNmVfd1WrpMo2EsxT47z71Yeb4zfrm4JVdWqOGd0CTfCeULw9IkuzXZjl6N7MjZ-i5oHERdSv_ZRRRYSgasJUGeEeLrcQm1IcQyzeTtRk1FNn0lZIsq5ZKD6nVpuUYoW8n6Oit_0r6PGKSJzEQhdazvHhbq4z9Plw-p-Tpan0KjekijAu8_KihdTj53R3lQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db5043a70.mp4?token=Wxalu9CG7_SrYo2NiDIcGHYnvF44yQP8LjeMD7IRwuMlppHmcaDVyavv5b5HwPs130Ji_OL46MOW7rd1EFVkhCxKyvamw0cKFd-VLfS_ZuGG2sQjdPlSZwS1RB3L3ucEB3fKLsgwkZk2hhgXzlblFQWNmVfd1WrpMo2EsxT47z71Yeb4zfrm4JVdWqOGd0CTfCeULw9IkuzXZjl6N7MjZ-i5oHERdSv_ZRRRYSgasJUGeEeLrcQm1IcQyzeTtRk1FNn0lZIsq5ZKD6nVpuUYoW8n6Oit_0r6PGKSJzEQhdazvHhbq4z9Plw-p-Tpan0KjekijAu8_KihdTj53R3lQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68408" target="_blank">📅 02:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68407">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
دو انفجار در خرم آباد شنیده شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68407" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68406">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از تبریز موشک شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68406" target="_blank">📅 02:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68405">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=DrxZyBZ08n3YzggnhvK1TjHY6idxFC4XZjf-HpXX2XwBT5T_3ViBOtamyBcNhmigF1yAksb0plBeXb5TWAWsCKAak4JFki368ZublFyU0Dv-_NDUh7pcnVhe43VIV_UZktoStngoDJf_J7AgYzOvhuNupYvhDJXS1NB1fKH9bvLslrpNRu7k9RdQbcT9fMjnPJTbUAehy7uaBwwqMvV-UsUCuunKaiV1TUzv_0h3F0xDi5DJbzrQt-mrRRxEXCZOsNs1I_psrq_aSCIGbupalQMUyxT9QJF7bGg0oTW5MCaKpk6E7CIPPAsEWn6j7AJuXTH5ZXKLDzKWiYwCrlaSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f8e07bfa.mp4?token=DrxZyBZ08n3YzggnhvK1TjHY6idxFC4XZjf-HpXX2XwBT5T_3ViBOtamyBcNhmigF1yAksb0plBeXb5TWAWsCKAak4JFki368ZublFyU0Dv-_NDUh7pcnVhe43VIV_UZktoStngoDJf_J7AgYzOvhuNupYvhDJXS1NB1fKH9bvLslrpNRu7k9RdQbcT9fMjnPJTbUAehy7uaBwwqMvV-UsUCuunKaiV1TUzv_0h3F0xDi5DJbzrQt-mrRRxEXCZOsNs1I_psrq_aSCIGbupalQMUyxT9QJF7bGg0oTW5MCaKpk6E7CIPPAsEWn6j7AJuXTH5ZXKLDzKWiYwCrlaSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
گویا پل یا پل‌های دیگری در میان راه استان کرمان به استان هرمزگان هدف حملات هوایی آمریکا قرار گرفتند:
پل گلوگاه بعد گنو بندرعباس و سرزه جاده رودان'
صدای ویدیو: راننده‌های سیرجانی اصلا سمت بندر نیایید ... پل بعد گلوگاه رو زدند همه ایستادند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68405" target="_blank">📅 02:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68404">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68404" target="_blank">📅 02:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68403">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
منابع داخلی:
چند محور مواصلاتی هرمزگان در پی حملات آمریکا مسدود شد
؛
⏺
بر اساس اعلام منابع رسمی، تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت به دلیل حملات دشمن تا اطلاع ثانوی مسدود شده است.
⏺
همچنین پل «شور» هدف حمله قرار گرفته است.
⏺
بر پایه این گزارش، پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرزه، نیز مورد حمله دشمن قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68403" target="_blank">📅 02:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68402">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlK1ZCuhUcPoHYc-9emcOMQ-tXc9snBG2rSwcKxpPaHaNhfFT8JPFlvokcXgFEEkjNBn3t3GMJsGtE3n-5jgZaQn_kYKVxp6sJVjNu-44qqD5xYKqfeCOsKmcaNomgT41TOPZTljV97w9IgGR7jKpzheDAOg7mThXR6JwIjCE0kXy_rx_DJBkVVA4jA6Vmz8BOfiOkYhbNAd2lyAXEFS7mM0mWi_hkotUHzXi2yvbfbev6wzHkyjB_6J74E6TZpgVxLhCZHXsaPINNUW5GWRtdIcUMe9GknYWZ3AemYhYQs4lAeq1c5lRxmiPfEwFSJoAfOJZl4yfm9GiUG-xzNaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پل مسیر بندرعباس رودان هدف قرار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68402" target="_blank">📅 01:58 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
