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
<img src="https://cdn4.telesco.pe/file/uuaO_30NAUJFOZne5QEs6BFqWzcpVW1cDLkuBzsJ7iKzdEsDSeTpvyVvolx1fevRsMWz-rDvUz5Fbnj7anr_OTt7_CUx3lADW6w34HDrdEmjiPFo58uKp9UyAYFbcIP23whoSQlYezdEwxW35pjI5t1naZKG7ltae7-w2h_8ShvYkhmhRe35V7QhD8yn6AfwO0hQ8xEt3ZMaa341qh2L4D5L6Vjq7WQo-I30LoQxCjL0kKqKp3sDDdw7cJhDAwSSX_s_hgXTGmZR0YgjDta6xbCSwRBTfBZbrTMo2v2mdSisN1B8n9Q-p0qQjLOTvNrYgV0Dbd64PxWE1aFiWs7wgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-151286">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
گوترش دبیرکل سازمان ملل متحد: خیلی نگران جنگم از آمریکا و ایران میخوام خیلی سریع دیپلماسی بازگردند و به جنگ پایان دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/151286" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151285">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f2b181f4.mp4?token=ZAM_8b3tS9LutO_onoBmp2BjQ1XI4DlQ5mzpRjZ7oaSW-fwIn6_Ja8iwJlJzox9fljVbZ0TkTwbLyTNdFi7sViNyDEqETYjfLFQJ8vtzHC6Ro9Zp1DLfS33pYd1LW23GHNnCnaoW2vHzHzJptr0LCpb9nRJjDX7xNxg6fUzWpTwHrhtLDkvoC7Io6CuyaOWf6pMWtuA4RyINYwiw1PrRWhAnvYNrp2ZxCwiE2Yp1sOMZAVzB3ijOTeigZLjV-NR-tjnoCQzvFFtRnoKyIGZR3aBVioROaZCTr92EcIMeKONVOAMaaLFVgQBY38djkrFMKpDbuSWT5twa0DCjN0Vcjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f2b181f4.mp4?token=ZAM_8b3tS9LutO_onoBmp2BjQ1XI4DlQ5mzpRjZ7oaSW-fwIn6_Ja8iwJlJzox9fljVbZ0TkTwbLyTNdFi7sViNyDEqETYjfLFQJ8vtzHC6Ro9Zp1DLfS33pYd1LW23GHNnCnaoW2vHzHzJptr0LCpb9nRJjDX7xNxg6fUzWpTwHrhtLDkvoC7Io6CuyaOWf6pMWtuA4RyINYwiw1PrRWhAnvYNrp2ZxCwiE2Yp1sOMZAVzB3ijOTeigZLjV-NR-tjnoCQzvFFtRnoKyIGZR3aBVioROaZCTr92EcIMeKONVOAMaaLFVgQBY38djkrFMKpDbuSWT5twa0DCjN0Vcjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی به ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/151285" target="_blank">📅 16:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151284">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی به آمریکا:
شما در جنگ نظامی شکست خوردید و در جنگ اقتصادی نیز شکست خواهید خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/151284" target="_blank">📅 16:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151283">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDWUUxjP2cHXmRhocMWFrXWl4Ulg_eBDpdwB0njqdJDgTrql3-up9VyrfwX_f7rM37c8fHLQBoc9681s2ag1luqmcGnXyYxBQ90uECxLw53G6kB3jogBRnucKJdggrnQgEKMoCCUYP_UQOozUhokrjiEx6zBzTFkIiZ6ak-ANBss7ierY6h9FJX04lbRDji3-tRlQDrGEJKkJlK46A3XGXFUdT0LplYwx8zOw8vddSEFlu_1K3zhSUUuMIqzCt-zRK67FpiRH2psOm0yvgvpl3RlhhIWwywVbcNuSjg7BnfhEk9-tWCKHrxzx88nN2Kc-F0MCann7llITyD50DEJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: گزارش ها مبنی بر سقوط یکی از هلیکوپترهای ما دیشب در دریای سرخ نادرست است. نیروهای ما در خاورمیانه در امنیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/151283" target="_blank">📅 16:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151282">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJXtr_LqaonnANHb-yF-NL1AWo65YqcX5T71FC7FQZrtkqclQ0-hEIfl9fggdsmOb35m4NQ3USQT8YG45mlRYzyPZnzEQOTlMVfIhU04xhVS3EOQ98M42Kyw4GnqdW8GYFcRmCxL9HcqOlCPOqr_OFzv8dLX3RQ6QyJ3DKRI5n4qSqC3u5qbOfOVj5Cm6znAktoAnPtWomp18sfdDLo9a3zZms2D5S4eVYwNgZxe-znxmRTXDEusufobBrPWwYaarZeieBnrAYfV1jL-YXN9IPUtyHM1q1hPAvuHRHlqODt8RGPWxFof7ZwwUr62Km38iNzt5sxOIGDJm0rPZAsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت هم‌اکنون ۹۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/151282" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151281">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=hcXk320HXxHf1VDCAcCbJerGEIh-Ao7CU5RG8iBful4h6O9UIvDe4VbY_KnOadmorsybFF8ITynv-UVIOBaKutAwihLXIE3piTcbseDiyouK1A5m4PAisU1EXgDyoITB1LbHxtakQQzhbWGf9jTDDDx8jy2mPBbPylDkXivtMF3T1YB38bXy_p5IDH9m2A5TFM8qZlE5tOarO8wMgqFXx3AIMlhjG0maDLaGDXDlAU6QUIyqXpFd7yYYOyViKvxk_ti4Jmhbw9BjgnrKIAp_NQnC1_zPCDcOPwstBzi8J-gHJ8cRcVWzNDKHPxgEnmfRqNFlqNWUgVeO32Y1Zpt4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=hcXk320HXxHf1VDCAcCbJerGEIh-Ao7CU5RG8iBful4h6O9UIvDe4VbY_KnOadmorsybFF8ITynv-UVIOBaKutAwihLXIE3piTcbseDiyouK1A5m4PAisU1EXgDyoITB1LbHxtakQQzhbWGf9jTDDDx8jy2mPBbPylDkXivtMF3T1YB38bXy_p5IDH9m2A5TFM8qZlE5tOarO8wMgqFXx3AIMlhjG0maDLaGDXDlAU6QUIyqXpFd7yYYOyViKvxk_ti4Jmhbw9BjgnrKIAp_NQnC1_zPCDcOPwstBzi8J-gHJ8cRcVWzNDKHPxgEnmfRqNFlqNWUgVeO32Y1Zpt4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد  #سیرک
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/151281" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151280">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
پزشکیان با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد
#سیرک
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/151280" target="_blank">📅 16:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151279">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پلیس انگلیس: یک شهروند به اتهام تلاش برای انجام اقدامات تروریستی در نزدیکی پایگاه نیروی هوایی فیرفورد دستگیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/151279" target="_blank">📅 16:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151278">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e00a668e.mp4?token=vRNaaeWRlZbsSAYANDRPMPy08yw0Nxfq9v3i88eT-11iyoOm-lu263TjxSmngcJkImGGJxumNurokuq7kqQiayOZaEdKf6ouLCBzgLJd_SaZ5N-J7gGj0EirWGG6WGtCnadjVTvs1r8Ktu0XKY53cBGZeO9QKgOnXKhOHWebPwre9dMbKVP_HLRi2EbsdNk_yU1hmPKdGAycC6wvk4axSrwhfCkzD9R5H8RBAe9916haMSd2NQ2tLsaON65f8KaiMZMMFKG7jRuYjtYZ2fxIiZ7gfVvT8tW0RbW93GzNBla_rZjgsnEj_Gmzg4GivjesxG56FQhQaAEi7DAI80mMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e00a668e.mp4?token=vRNaaeWRlZbsSAYANDRPMPy08yw0Nxfq9v3i88eT-11iyoOm-lu263TjxSmngcJkImGGJxumNurokuq7kqQiayOZaEdKf6ouLCBzgLJd_SaZ5N-J7gGj0EirWGG6WGtCnadjVTvs1r8Ktu0XKY53cBGZeO9QKgOnXKhOHWebPwre9dMbKVP_HLRi2EbsdNk_yU1hmPKdGAycC6wvk4axSrwhfCkzD9R5H8RBAe9916haMSd2NQ2tLsaON65f8KaiMZMMFKG7jRuYjtYZ2fxIiZ7gfVvT8tW0RbW93GzNBla_rZjgsnEj_Gmzg4GivjesxG56FQhQaAEi7DAI80mMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداد عادل : هربار میومدم خونه و میدیدم یه جفت کفش له و درب و داغون جلو دره، میفهمیدم مجتبی اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/151278" target="_blank">📅 16:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151277">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مارکو روبیو: جهان در طول ۲۰ سال گذشته تغییر کرده است. تمرکز ما تغییر کرده است.
🔴
من فکر می‌کنم ایسلند و موقعیت آن نقش حیاتی در دفاع از اروپا و میهن ایالات متحده ایفا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151277" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151276">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a8054a9b.mp4?token=nxKu2qEnIzaw2YU1EXnE4LHOz0BZDnLRuO9ZPrtBNC4u-IOKtAlxXu57H7il2nrXw4MUCF3j437-mAPrpxk84t6zY2B513b5BFRfNKvGD-3i8KG6NGcQjYqNoMoBjIRFiSKQjRZdQoBUinDnc-Byc8WICiPlTZ_M7aDDr-nNI3xBhHHEn-Tl_QQwHAJrPOqj-6hYCeHk4yjbljIOHvGR9GaTzPjbLC_8ViK_llfswMpo4CF6X1ssX2MrYBAOz6DH-xGW8dLL6gEmSnSGvsdKB8JM-B0PEx-0OLOOp2NlNqAzaOasJoBTXJo61P01z8Lp42PPw8gqQobTbhWioFkHao3YLZgL-uTIGex4Ojq9KBgcPPZD_M8Xb_skZr1iGk-Jzts6U3z-B-WCk_FyOXBwQ0HDZdBW31ivp8i-zZZ1PwZhN1F8KSmxQ08wwxoOyaC67l4sozlM3eV1DHWwPSjir7a0jHz3GKnNB_-eAB_VJyLVtnBhs6vH2-Rjwz-TUpsnpVOwZuUMlJhvX7IaqI_wt4lRs7bWq4heQeTUJxMbcuwG5OrOijO_BIkZJ7bAZa_YJ0Zal0XJDHNusDblWYJTHmphzDlqmxTAuxtC7yoYxQfpI9ueM7351n8QLwSomV-w98sily5zzyB5W2SFx2Za6OyA0KO2P1jzg6cZuBiA7AM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a8054a9b.mp4?token=nxKu2qEnIzaw2YU1EXnE4LHOz0BZDnLRuO9ZPrtBNC4u-IOKtAlxXu57H7il2nrXw4MUCF3j437-mAPrpxk84t6zY2B513b5BFRfNKvGD-3i8KG6NGcQjYqNoMoBjIRFiSKQjRZdQoBUinDnc-Byc8WICiPlTZ_M7aDDr-nNI3xBhHHEn-Tl_QQwHAJrPOqj-6hYCeHk4yjbljIOHvGR9GaTzPjbLC_8ViK_llfswMpo4CF6X1ssX2MrYBAOz6DH-xGW8dLL6gEmSnSGvsdKB8JM-B0PEx-0OLOOp2NlNqAzaOasJoBTXJo61P01z8Lp42PPw8gqQobTbhWioFkHao3YLZgL-uTIGex4Ojq9KBgcPPZD_M8Xb_skZr1iGk-Jzts6U3z-B-WCk_FyOXBwQ0HDZdBW31ivp8i-zZZ1PwZhN1F8KSmxQ08wwxoOyaC67l4sozlM3eV1DHWwPSjir7a0jHz3GKnNB_-eAB_VJyLVtnBhs6vH2-Rjwz-TUpsnpVOwZuUMlJhvX7IaqI_wt4lRs7bWq4heQeTUJxMbcuwG5OrOijO_BIkZJ7bAZa_YJ0Zal0XJDHNusDblWYJTHmphzDlqmxTAuxtC7yoYxQfpI9ueM7351n8QLwSomV-w98sily5zzyB5W2SFx2Za6OyA0KO2P1jzg6cZuBiA7AM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره اوکراین: عضویت در ناتو در حال حاضر روی میز نیست
🔴
در حال حاضر، ما صرفاً بر پایان این تعارض تمرکز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/151276" target="_blank">📅 16:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151275">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مارکو روبیو درباره مورد مشکوک طاعون در روسیه: به نظر می‌رسد روسیه موظف است که به وضوح اطلاعات بیشتری را با جهان به اشتراک بگذارد
🔴
این کاری است که باید انجام دهند. امیدواریم که این کار را انجام دهند
🔴
ما این موضوع را به دقت زیر نظر داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151275" target="_blank">📅 16:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151274">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/151274" target="_blank">📅 16:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151273">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151273" target="_blank">📅 16:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151272">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP48Egffxc1UAh4dEfh30EGCVRYa3ofkZdohrRAXNfb9dZmzPsjVcwz8utXXQuWZUYDKxu6ZTBmykr0d91rDzG5PRu_2QCi78u3r0sz6GKNqI3EP3E4aZwsDfq9L9iLm5Fp_9VAzS3U0JB3XzNZIQcTXYHsbfNBe2Yb1bE4x-3i9d7HmdJQ0ACemAVBrfH8sUcMl5w3dYA_bY3lAeHTlkOqCFWtlxczkZR_v7SIUXqDDin6ATOml3VNpoSSnpv6qzB4ATT6fIKLVMY4Vn5nr7lSIcbW3-et9FN29XYIk3sH_Dv2mZwatvRbDlvGhwq0NnbV6mWFbgHKe6pJVa6kXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: باید جلوی دستیابی ایران به سلاح های هسته ای را بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151272" target="_blank">📅 16:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151271">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه اینجا رو بخون تا درآمد دلاری داشته باشی
👇
👇
https://t.me/+ja5I7eWou95iNWUx</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151271" target="_blank">📅 16:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151270">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNLqIceCoAhnUc1YLW7EEvaF6F1eeW8GFdLJT2ycVQ8o_0-cPzQpJB7B83EVrGiNoQZBov05nBBGE4X7gFPBBvanu5MeEgo0TkM0e1O4uqEG4jm7pqukOO6MXD8RLpAUEL6wdIeBwNjnBFhdDS48PnabacwZCtO-6YLJkWlpfqT_wPN4hyisjGdM3wjJIu_ppfwHr84MuKuC1UQMJB4ZiAdQUj8TbE18XieehpA3QdCAQN2sJQQ0EYI9-vJXntzHtyr9V7mQyO5hH2yzfRFngovSHF7AoDOpab-_RK6esCKelef3DcfE0RCfnZR34PEkg1tBlOvwrLmQj2kw0TL7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش که در حال عبور خروجی از تنگه هرمز بود، در تاریخ ۶ اکتبر هدف اصابت یک پرتابه ناشناس قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/151270" target="_blank">📅 15:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151269">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
گزارشات از اختلال شدید در اینترنت
👎
👍
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/151269" target="_blank">📅 15:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151268">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر کشور در دوحه: از نقش منصفانه و میانجی‌گرایانه قطر و پاکستان تشکر کردیم
🔴
بحث‌های مطرح شد که ان‌شاءالله سطح تنش‌ها کاهش پیدا کند و سایه جنگ از منطقه دور شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/151268" target="_blank">📅 15:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رویترز: پالایشگاه‌های نفتی چین، خرید خود از نفت خام عراق را افزایش داده‌اند تا کمبود عرضه نفت ایران از طریق تنگه هرمز را جبران کنند
🔴
بر اساس این گزارش، حداقل ۱۲ میلیون بشکه نفت خام از عراق و قطر خریداری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151267" target="_blank">📅 15:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عارف: ما به هیچ‌وجه نگران تحریم‌ها نیستیم، چونکه کشور ما در برابر تحریم‌ها آب‌دیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151266" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151265">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تسنیم: پلیس فرانسه حقوق معترضین رو رعایت نمیکنه و تا حالا ۶۰۰۰ نفر از معترضین رو بازداشت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/151265" target="_blank">📅 15:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151264">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرگزاری دولتی سوریه: احمد الشرع برای دیدار با محمد بن سلمان وارد ریاض شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/151264" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151263">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
قاتل فراری پس از ۱۹ سال دستگیر شد
🔴
مردی که سال ۱۳۸۶ در جریان درگیری در یک زمین کشاورزی در فشافویه، فردی را با شلیک گلوله به قتل رسانده و متواری شده بود، پس از ۱۹ سال شناسایی و دستگیر شد
🔴
براساس تحقیقات، ماجرا پس از ورود گوسفندان به زمین مقتول و اعتراض او آغاز شد. در جریان درگیری و تیراندازی، چوپان با سلاح شکاری به سمت صاحب زمین شلیک کرد که به مرگ او منجر شد.
🔴
کارآگاهان اداره دهم پلیس آگاهی تهران بزرگ پس از سال‌ها پیگیری، سرنخی از محل اختفای متهم در یکی از روستاهای اطراف مشهد به دست آوردند و او را در عملیاتی دستگیر کردند.
🔴
متهم برای ادامه تحقیقات در اختیار پلیس آگاهی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151263" target="_blank">📅 15:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151262">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
وزیرخارجه روسیه: مذاکرات ایران و آمریکا به بن‌بست خورده و بعیده توافقی انجام بشه.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/151262" target="_blank">📅 15:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151261">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41d64143a.mp4?token=WHQE7uNGMUh_1JlxUK_GEf7TOL7bJmy3kYQVLPNyPtY433yZ6l8QH1H2U7_gRetBzh3rT6oZgM3VIIzenmme33Lr784jvs3mFwI_CblFEkIlQhxLRkFN8cEQ2rgQscFasQkHQ5TC43DaKkrXHo6ldSP7BlYRffZTUMOn-y6dMosX9WFUQ0GXBoXwug8Tbw8RYdytGcEz2GMVj7ZrGONF4g_VpdoflOiew2tYM8rJYKhUy4rcL4UPiXCbT--YNUT9hXJp8ol3_Op2gpyZIkLT_VIdmXkq7AMDGDmRnd-3WjjWIRCY8S1ia_qq3C6M0V_o7geF2g7Ao8KFxRkaEEjuY7YPcPREG-Q0ZK6Q4JWaCJCs7DlLNTGSOysLeUUU0kGVj9UCfM2dSRwOsI-ev8JjDO_qIoqaeJXWGcLbHZY1KVbg8Lu-LpGtElObzA6ZlSJ6yb3ZGSPRcLlRzyG-d0NTl70UptzU61KaSybvTTNi8Z8VIzDlwJYaUgXbzF-Yo07MciXTLy7OBiZhRYeEpEF27MogxjbMxkFEp3lxpCZoaeoF-Qm2EyZEM09adLQAYDXIQ6Sa5smhjp0CVgtJJ9Im2-p54ACw7QrssgEWIVXsvkEqnk3UlOaGwLbRjkUJAg-Y_uWZenHtn3nNAg45zueO_pYzLFXBt3-SkWw20qEcIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41d64143a.mp4?token=WHQE7uNGMUh_1JlxUK_GEf7TOL7bJmy3kYQVLPNyPtY433yZ6l8QH1H2U7_gRetBzh3rT6oZgM3VIIzenmme33Lr784jvs3mFwI_CblFEkIlQhxLRkFN8cEQ2rgQscFasQkHQ5TC43DaKkrXHo6ldSP7BlYRffZTUMOn-y6dMosX9WFUQ0GXBoXwug8Tbw8RYdytGcEz2GMVj7ZrGONF4g_VpdoflOiew2tYM8rJYKhUy4rcL4UPiXCbT--YNUT9hXJp8ol3_Op2gpyZIkLT_VIdmXkq7AMDGDmRnd-3WjjWIRCY8S1ia_qq3C6M0V_o7geF2g7Ao8KFxRkaEEjuY7YPcPREG-Q0ZK6Q4JWaCJCs7DlLNTGSOysLeUUU0kGVj9UCfM2dSRwOsI-ev8JjDO_qIoqaeJXWGcLbHZY1KVbg8Lu-LpGtElObzA6ZlSJ6yb3ZGSPRcLlRzyG-d0NTl70UptzU61KaSybvTTNi8Z8VIzDlwJYaUgXbzF-Yo07MciXTLy7OBiZhRYeEpEF27MogxjbMxkFEp3lxpCZoaeoF-Qm2EyZEM09adLQAYDXIQ6Sa5smhjp0CVgtJJ9Im2-p54ACw7QrssgEWIVXsvkEqnk3UlOaGwLbRjkUJAg-Y_uWZenHtn3nNAg45zueO_pYzLFXBt3-SkWw20qEcIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه، شاهد اولین آزمایش پرتاب موشک بالستیک جدید M51.3 از زیردریایی هسته‌ای "لو ویژیلانت" بود.
🔴
مکرون گفت این آزمایش، قابلیت اطمینان بازدارنده هسته‌ای فرانسه را نشان می‌دهد و افزود: "برای اینکه آزاد باشید، باید ترسناک باشید. و برای اینکه ترسناک باشید، باید قدرتمند باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/151261" target="_blank">📅 15:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151260">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یدیعوت آحارونوت: از زمان حادثه فلای دبی، 7415 اسرائیلی از امارات به کشورشان بازگردانده شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/151260" target="_blank">📅 15:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151259">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3251d4a5c7.mp4?token=usZEVxwjTBWflPL_3ZGWDCNR5oSgmb5AJ6HpEGGz5GsHlqMkMmX2mHoRbRJBOlD-T443oWUcbj3V1gCPFYkPOcxjifPzotMI6DRgHaBwFlXPI5OGgc25nvgkcPcV3tGaPZh27xMDVnj0rp0qza5_u1rWenBbjOmRzVrJjx9t5OnunDUZLgxFpMCfKI2aRFMk-vrg0qetCexQ-ZzVmVc5vuRQnsiT1ra5c2QUW3Dhq-qHojmbdCABQNQ2IFM6Xj3LySeQnB9TFvJoC8_EQktEFFD7ww18J4y49JarscPKXR_Of4u0itsxR149IzTHW-uTyu2DZ9LcLryld1yTs6mCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3251d4a5c7.mp4?token=usZEVxwjTBWflPL_3ZGWDCNR5oSgmb5AJ6HpEGGz5GsHlqMkMmX2mHoRbRJBOlD-T443oWUcbj3V1gCPFYkPOcxjifPzotMI6DRgHaBwFlXPI5OGgc25nvgkcPcV3tGaPZh27xMDVnj0rp0qza5_u1rWenBbjOmRzVrJjx9t5OnunDUZLgxFpMCfKI2aRFMk-vrg0qetCexQ-ZzVmVc5vuRQnsiT1ra5c2QUW3Dhq-qHojmbdCABQNQ2IFM6Xj3LySeQnB9TFvJoC8_EQktEFFD7ww18J4y49JarscPKXR_Of4u0itsxR149IzTHW-uTyu2DZ9LcLryld1yTs6mCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: اسرائیل اسم خیابان‌های ایران رو عوض می‌کنه
🔴
مراد ویسی میگه اسرائیل داره اسم خیابون‌های ایران رو تغییر میده. شورای شهر هم فقط تابلو رو عوض می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/151259" target="_blank">📅 15:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151257">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
اکونومیست: آزمون اصلی بازار گاز هنوز در راه است؛ زمستان به دو «اگر» بزرگ بستگی دارد
🔴
اکونومیست می‌نویسد با وجود آرامش نسبی بازار، بحران LNG هنوز تمام نشده است. قطر از زمان اختلال در هرمز صدها محموله کمتر از سال قبل صادر کرده و قیمت LNG در آسیا همچنان حدود ۱۴۰ درصد بالاتر از پیش از جنگ است
🔴
به نوشته اکونومیست، عبور اروپا از زمستان پیش‌رو به دو شرط مهم بستگی دارد: هوا نسبتاً گرم بماند و صادرات LNG قطر تا دسامبر به وضعیت عادی برگردد. اگر هرکدام محقق نشود، رقابت اروپا و آسیا برای محموله‌های محدود می‌تواند قیمت گاز را دوباره به‌شدت بالا ببرد؛ در یک سناریوی سرمای زودرس، قیمت‌ها حتی ممکن است به ۳۰ تا ۴۰ دلار به ازای هر میلیون BTU برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/151257" target="_blank">📅 14:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151256">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1oq3L_xDc77r9_dWR_yeQywiTclDE1Yt7sD70jumjg0Tmu6-UlKzB2D8I1Wn3LGjnohVG0Cmqls92jrT5RDTI7JW6fYUFzR4mzrio3QFbJ8yFcZ2rkEUmPA7EQgeRAvLEa0dkbyMD0agNNcHLh80_PeRenMj5Ly9xbZsujqzmfCP-TZIewbY3MJfdTVdGcagQB2_9PYz1XH5FqGhec7IzsRM3JZb7niu2gAkCms0N5WTgceE8IvLL94ekzIaGfYOHIqy4lXZV46j1S8UOxkaE6ttJxuVEt-Z0BKm1s3Agctp7xWcZhh9ME7DdZcNCcUkOWNw0IaitFeGTJN-3dH3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز 6 October ، روز جهانی فلج‌های مغزیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/151256" target="_blank">📅 14:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151255">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANF9WzVYYWN3p1USaxAPAFVBqDsXiEtVVIc_z6SKHF5VTd0-V4235hu13RMDCys8lywb7SqFsoRMsakwWrLLsArRlAV4WWPsKYBH9PCwq725hoI0sGMEl-sVRNS2sdFZIiGlNWX4C1rKb2sV6PvO-qcQwT9iHlsLl-tlJUblLlum7siF7VPfu8pS2wKoy-4yW4z1NEhlFs8xr8IPBYBkaiVCf459N-PMzb2xfA71HpcE7iyPES5hwP-as-R4NOrNFZJobvDepWTOYOp-XKMkaEM7PHjazj8ZlYMY3SgRSLVj4b9BXFyilKck7cR2UFnaWVW3NfNGIu-n8OcokJMqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اختلال هوایی در پرواز های ابها عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/151255" target="_blank">📅 14:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151254">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سخنگوی دولت: برای مذاکره آمادگی داریم و از آن ترسی نداریم/ منطق ایجاب می‌کند که مذاکره را انتخاب کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/151254" target="_blank">📅 14:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151253">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وال‌استریت‌‌ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151253" target="_blank">📅 14:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151252">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وال‌استریت‌‌ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151252" target="_blank">📅 14:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151251">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزارت امور خارجه هند: ۱۲ خدمه یک کشتی تجاری با پرچم پاناما در حمله‌ای در سواحل عمان زخمی شدند که ۱۱ نفر از آنها هندی بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151251" target="_blank">📅 14:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رئیس سازمان ضد جاسوسی آلمان به اتهام جاسوسی دستگیر شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151249" target="_blank">📅 14:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فرانسه: تحت نظارت مستقیم امانوئل مکرون، یک فروند موشک راهبردی جدید با قابلیت حمل کلاهک هسته‌ای با موفقیت از یک زیردریایی آزمایش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151248" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزارت خارجه قطر: تماس‌ها و رایزنی‌هایی که از سوی میانجی‌گران میان واشنگتن و تهران در حال انجام است، همچنان ادامه دارد
🔴
اعلام برنامه سفر وزیر کشور ایران به دوحه بر عهده وزارت کشور قطر است و این وزارتخانه درباره دستور کار این سفر اطلاع‌رسانی خواهد کرد
🔴
مذاکرات درباره ایران در جریان است و نگرانی‌های طرف‌های مختلف را در نظر می‌گیرد
🔴
برای سفر طرف ایرانی به‌منظور اطلاع از اقدامات انجام‌شده درباره پرونده خلبانان، آمادگی داریم
🔴
آخرین تحولات پرونده خلبانان ایرانی را به طرف ایرانی اطلاع داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151247" target="_blank">📅 13:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c01e4ed6.mp4?token=QN5coTq_nV9bTMItSA9xs5Khj6kuyN0zv5zXROGmaj3w-1Vkg5xj2Rl0gg-4YFgjEI2g45uHUntLwg7a8J7VuuOqjRBKXXij8rQOQrSx2t5fTSZNLjpljeRXNEfc75re3ca3rVDALRvHyzbPHszeCSnRO1B7PQ4VEVtpb7utH0mj62MMczFXdd5zXIZMdT0NJY0rehDyr9YS5_6IAUhzHLrHEoLw2KTJ3iMJ_iCK4tq0kWNc-kZ1DiugDtjU8OE9Gen2fIlTLLlwNZ3Zenmh0U-JkQP5aJ8boxKkAVHkQvQ7ckXpLnpTECbsP7wlwERq8h6gQJHMUHut-HiQjuQfAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c01e4ed6.mp4?token=QN5coTq_nV9bTMItSA9xs5Khj6kuyN0zv5zXROGmaj3w-1Vkg5xj2Rl0gg-4YFgjEI2g45uHUntLwg7a8J7VuuOqjRBKXXij8rQOQrSx2t5fTSZNLjpljeRXNEfc75re3ca3rVDALRvHyzbPHszeCSnRO1B7PQ4VEVtpb7utH0mj62MMczFXdd5zXIZMdT0NJY0rehDyr9YS5_6IAUhzHLrHEoLw2KTJ3iMJ_iCK4tq0kWNc-kZ1DiugDtjU8OE9Gen2fIlTLLlwNZ3Zenmh0U-JkQP5aJ8boxKkAVHkQvQ7ckXpLnpTECbsP7wlwERq8h6gQJHMUHut-HiQjuQfAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو
:
معجزه‌ای که جهان امروز می‌بیند — حتی برخی از کسانی که ما را محکوم می‌کنند، پنهانی می‌گویند: «وای، ادامه بده، ادامه بده»، زیرا آن‌ها این قدرت را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/151246" target="_blank">📅 13:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فروش تسلیحاتی ۲.۲۷ میلیارد دلاری آمریکا به سه کشور عربی
🔴
وزارت خارجه آمریکا با سه فروش احتمالی تسلیحاتی به امارات، مصر و کویت به ارزش مجموع حدود ۲.۲۷ میلیارد دلار موافقت کرده و این بسته‌ها برای بررسی به کنگره اطلاع داده شده‌اند.
🔴
بزرگ‌ترین بسته مربوط به امارات با ارزش ۱.۰۴ میلیارد دلار و شامل تا ۱۰ هزار سامانه هدایت APKWS-II است؛ مصر نیز قرار است سامانه‌های موشکی جاولین به ارزش ۸۳۲ میلیون دلار و کویت خدمات تعمیر و پشتیبانی سامانه پاتریوت به ارزش ۴۰۰ میلیون دلار دریافت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/151245" target="_blank">📅 13:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9vGzTj9NHqy7yfIvFJ_9dQw-3lzglvkRvpDcD5tThAwqatSvAzwxxu0XIaOpMFy0skek6zJXfI9YZNHclXqABpU_Ke6PCJEom38MPTjomX1jZ9OyS24Wofj5wLD3_gfQi4ab3m8U8LC7AdZj4Lamd-FUGVRJDLnKiKRHpK1dS2jJNa3bGn2OOiunPeeV7mH2docp8gI-zdSJJWW-iTKRNy_xepCaWFulttfbU7FIdSViXW8OEqFiOn54KrbcGLfvI_Y-eS1IfqimMwuRxMQd3eNzS-XiSJT0GhXX_l807oUGng8lu4z8LCH_gJehYh-MQvEMKWSw1S1FCLdGDvt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PO8oZloReoZsdx1DCx5aTtcD5m23bLCnAzNO3HcqCYnupaFUaPJBl-FR7qSXqIduuWkkZIJHH1PabivLWOOboap4csoms0SjZulCaGmmqBeOu0EE_h9MNfsRAOzM5b60boZBdtBm0Mc0veMvBXDm5Ag4VlW5QjzemDZ1MMaDcTOBAbSqyqWt8udnKFNZMjfr2BhmUbvRlhIm5aH9wuUVrrZH2DQDRvgIdV60YvD3jIRfUp2YEiJTxJA_sXENptWbiH213pN4ZOrQTTsDS7PEivRk6WFSWQLgbMB0KP0GWnFMGLIODNR6gMLwFm8yb2Zsl_q7RPzBhSKgevo9ZvI6dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بدون شرح از جانفداها
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151243" target="_blank">📅 13:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q85GDun1MdYfBNrP8Hcq9XO1_02k7OvmVh__y143-VyItWxsYl7P2t3c1AfwgzKu3Lu_iwkIg_H2KUW_MHgtWv46Fkhi74iar4GRtrdk_lNPQhohsaqwzNuvUMSgDKhjIArcT97jr-iLdcTw4X5-A1ci1dJp5y4xfu4LU1NOwijCfvj0J9oTTpiQkI2ZlPwUtqrtF09TIP93RZzdf_B1JLy6vCUx1413hNodY1xTMsBTJ0-S0mk1Yh71XGBufHgycxs_HpRJzkqTueqCN0kbzT54ifRgkVZOCdeGAbR16LAm_Fks2U2LB7ZlPPndQJCtMgI7XeDqODU0cUskzZYAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی منابع اعلام کردند زین واکر بازیگر دو رگه ایرانی آمریکایی و برنده جایزه نخل طلایی وارد ایران شد
🔴
وی پیشتر گفته بود قصد دارد برای دفاع از ایران بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151242" target="_blank">📅 13:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خاویر بلاس، ستون‌نویس حوزه انرژی و کالا در بلومبرگ، به نقل از «راسل هاردی» مدیرعامل ویتول نوشته است که طی ۷ تا ۱۰ روز اخیر، به‌طور متوسط روزانه حدود ۱۴ میلیون بشکه نفت و فرآورده نفتی از تنگه هرمز عبور کرده؛ شامل حدود ۱۲ میلیون بشکه نفت خام و ۲ میلیون بشکه فرآورده‌های پالایشی.
🔴
بلاس تأکید کرده این رقم فقط مربوط به عبور مستقیم از هرمز است و صادرات از خطوط لوله جایگزین جداگانه محاسبه می‌شود. رویترز نیز حجم اخیر عبور نفت از هرمز را حدود ۱۴.۲ میلیون بشکه در روز، معادل نزدیک به ۸۰ درصد سطح پیش از جنگ، برآورد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151241" target="_blank">📅 13:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_gGuYsJzhSBBagABoq7J0b6Oe95TwUKq9EKwMHCiVnkqbQglVpXzUqE5GPd5F4d_8pMkDxwdQ2TTTDk-PpWQYAEurT5Y4E9i1cxaUCcJ-wGog8za8tnFQwZ18fkIMnXRePnwk6CCw2SGxYOmFq3mrJXa_8pOtF_nQV6SKENmuKwPhGX4rNsyDiMZzDHtT4affxUzqBUaZjxbGQo3nQn6QFy5Bh8UIm8C7Oj2nX8_-S4UoDzB09CKX7yvGoXBnXXap6lCAjwbvCTMDoSbl0H8l_sbaSbuPp8lkO_WskFG9FbxAI4MzvIHoT0p8mGqoftC_9LZQ-Lfp0Q9oVf379MDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار کلاهبرداری
‼️
🔴
کانال فوق ارز دیجیتال فیک معرفی میکنه و میگه بخرید تا سود کنید
🔴
به هیچ عنوان به اشخاصی که ارزهای ناشناس و بی پشتوانه معرفی میکنن اعتماد نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151240" target="_blank">📅 13:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151238">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOi3eka5qbnHBD1cYXT7S4621Fj3TyBadRm8BTBpYPtKI8nUF9LqnvqZzQCwEfB4r5u7b-jWntVhC8xlVyWhAKAXcqmtroH12eWcgTrP4fVDirJy5Ikm6yaLnOf3njJBRFtpwFfwUxuolKFK_XI8wlRAwBod4JzDBjyQwbVQBXl5kKihLnKKMiSukxgT9JEzbIlZRRHPypFzi__LsewW9fIPnzp8zbszWsgZ9EJLQStUz3r0MLlc2HUevXASgyrcCSHXSGvEGkdmoEeNy3Lp-jU93fABc13k-GSkCtf96GtM1iL0MNM0tIXgOOoR3DaTelU8MX11nqMHw-_1nm_oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnPK3H2N_H-gzFW4D4ZrkPPrPHYLIi-I5hnskPqEiF2UW5GVqOvJzpXNhYDuD1jbTeAm8vRSjK2zu7tZoOyz8MxCU9LwdUGHtuyERx48Ts5USscOg9AnQHERowEA35FiRaoso9ky1aCdTCfq-tTS0fYIWUPGc2G94Ka9TSBeZvBZd5GKC2eZw7foEyny6rMpWm0G9M2wfliIzeaZs8KsJ4_9S47fnZcV8N8_pby56Zi_0HYobMnXSkplIbRORjfNyLxS-gore8woQtjfcQanTrDogoa58M9-nI6Hl6xAy-F3OJOOLwyxqvV5t5Voyn1QJ7WK_0SItDW9f-Pd_ZPhZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اعتراض دانشجویان دانشگاه جندی شاپور دزفول به کیفیت غذای سلف این دانشگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/151238" target="_blank">📅 13:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151237">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
مینو محرز: طاعون روسی جدی نیست، کافیه از ماسک و دستکش استفاده کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151237" target="_blank">📅 13:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
یحیی سریع سخنگوی ارتش جنبش انصارالله حوثی ها گفت که این گروه فرودگاه بین المللی ابها را با یک موشک بالستیک هدف قرار داد که باعث اختلال در رفت و آمد هوایی در آنجا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151234" target="_blank">📅 13:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
سود امروز حساب های متصل به کپی ترید  پشتیبانی
👇
@shahab_amir_support  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151233" target="_blank">📅 13:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8873094f08.mp4?token=UMepIiTuh75S3Z9tF4-l00cHN1mNweX-PSZLwkbpR28k-s6CsTiBK6wqhUk4QGKzjtoOeimGGjvPEIRZ8WI5HV6oLU_aBl5tQuUpv9185oCnJYSlKv7oAJMQQELs3JRmQ-sPMZCx-DWsE2XZ8c9BsFI_rxrk7eDgX-TV-5sCbky8ONoAQLrpEhqAvzRAOyzKRiptJF0lQFvmaIfwPDSRwaXBda9Aq3rFkIZoGenU9fAMd6SmEpRmVZR7GnQYA50d0pY6cwPxR4n82tjHGaUahCcMj-g1nOB0KYG79b2956OaOV_FZLa7ELQ5kzwszVjtgScy0siU03tIGxoHTBkPjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8873094f08.mp4?token=UMepIiTuh75S3Z9tF4-l00cHN1mNweX-PSZLwkbpR28k-s6CsTiBK6wqhUk4QGKzjtoOeimGGjvPEIRZ8WI5HV6oLU_aBl5tQuUpv9185oCnJYSlKv7oAJMQQELs3JRmQ-sPMZCx-DWsE2XZ8c9BsFI_rxrk7eDgX-TV-5sCbky8ONoAQLrpEhqAvzRAOyzKRiptJF0lQFvmaIfwPDSRwaXBda9Aq3rFkIZoGenU9fAMd6SmEpRmVZR7GnQYA50d0pY6cwPxR4n82tjHGaUahCcMj-g1nOB0KYG79b2956OaOV_FZLa7ELQ5kzwszVjtgScy0siU03tIGxoHTBkPjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: در دنیای غرب امروز، در دموکراسی‌ها، آن‌ها نیز انتخابی ندارند — و نمی‌جنگند. ما انتخابی نداریم، و می‌جنگیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/151232" target="_blank">📅 13:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151231">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
صدای انفجار در شمال ریاض، پایتخت عربستان سعودی شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151231" target="_blank">📅 12:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869ee22d10.mp4?token=EXt0JxK8nNc8f7Hts5PR5nDrkJJfAucZosQ_H6Aj9uUCrnltABjOkgfE6_kT7KlbOb_-yNjB3FqENXtR5qdxfWV17JI46MRgAufqNkcAdvtKxZgxpcY7SJhV69KtictskXlBF9lv03Ckq9OJA-3FE63WjH9s8Qb9kylJqcNOEJQzTg0hyiEry7oVq6Dq14huKvVlVJp3LnEM4HEpZRtzrKPsmkNfv5D-mNDaLt6UEoXz4gfs64jM3MOFBmB29kd1vrw9DhFUr67p6_lGZzWtjgvarEXFumZrOkddqXLEKP3v0CKWsdduTwdEqiBrberfEuuJNb2JZGfk3mF7Ywf1_EKIqf4lyM_rbMVAB90mPbJafLJlHQ3dTcmcSu3mLOybNBALvqDWZOkRNJ0JQPF_V0MybT-4KbdIK8cDUtW1Oa3Z5x80-RdqfTLYp34pU31VJxtCTa3e-XmbgiEDZcJKely9YGoRM-ZLUJSqRnZ-NGOGUG-M-yOu5CKS5wj0E-_e0-hCrEDtzgRF8omrKDvE8IY7yJu_BUPWsBwhgy9LieBAbOar3mtItXzImL5Ogc5OpwrXc2MvUg7UV1v1zTNdB7m-3KJRvXC9l9VxlTaChXjEcHhdOWOWJYP1T7LR5BqQNgPfEoQFupETAbKBOfwYpe3m9-ZD6mnsoMMzpBXtVTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869ee22d10.mp4?token=EXt0JxK8nNc8f7Hts5PR5nDrkJJfAucZosQ_H6Aj9uUCrnltABjOkgfE6_kT7KlbOb_-yNjB3FqENXtR5qdxfWV17JI46MRgAufqNkcAdvtKxZgxpcY7SJhV69KtictskXlBF9lv03Ckq9OJA-3FE63WjH9s8Qb9kylJqcNOEJQzTg0hyiEry7oVq6Dq14huKvVlVJp3LnEM4HEpZRtzrKPsmkNfv5D-mNDaLt6UEoXz4gfs64jM3MOFBmB29kd1vrw9DhFUr67p6_lGZzWtjgvarEXFumZrOkddqXLEKP3v0CKWsdduTwdEqiBrberfEuuJNb2JZGfk3mF7Ywf1_EKIqf4lyM_rbMVAB90mPbJafLJlHQ3dTcmcSu3mLOybNBALvqDWZOkRNJ0JQPF_V0MybT-4KbdIK8cDUtW1Oa3Z5x80-RdqfTLYp34pU31VJxtCTa3e-XmbgiEDZcJKely9YGoRM-ZLUJSqRnZ-NGOGUG-M-yOu5CKS5wj0E-_e0-hCrEDtzgRF8omrKDvE8IY7yJu_BUPWsBwhgy9LieBAbOar3mtItXzImL5Ogc5OpwrXc2MvUg7UV1v1zTNdB7m-3KJRvXC9l9VxlTaChXjEcHhdOWOWJYP1T7LR5BqQNgPfEoQFupETAbKBOfwYpe3m9-ZD6mnsoMMzpBXtVTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: بیشتر اقوام باستانی دیگر وجود ندارند. آن‌ها این پیوستگی، این رشته‌ی وجود، این چشم‌انداز بازگشت و آمادگی برای فداکاری، برای آمدن، برای سکونت‌گزیدن و یک‌بار دیگر به دست گرفتن شمشیر داوود را نداشتند
🔴
بیشتر اقوام ناپدید شدند. قوم اسرائیل در اینجا توانایی‌های فوق‌العاده‌ای را به نمایش می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151230" target="_blank">📅 12:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hOkxwAEF65gcBiMM4AQBxSHSQ0cq5-GMTNumsKDW4Uf0vSFurEEfe27QSRA4f6QOwARNdXHBeyeFN6S8keXUluYJK6bWTYDZTD0vw4gN7rikcZp8KjaA1Kom9WxZVbkgEJnuVVAN-fVh4MhrIdFul5dv2InQ2y4Bw6qYZleQcycOqmXyU8-C_gEPCWXJlX8AV8OHfZNePKdPUMI3QrEHUAyTfQMtJHfLQjb6QU3JKUbMsxn-a9sVEOmXBPTx4h7l8N3OJb1ZGVfdT-oROIdpV7j_qxIlbEWb9m2aKaC7bG9gSq3RenNfZg8OVBr1u1FgOgzp38CAtc2lHkmfW2IHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های پروازی نشان می‌دهد که در پی حملات یمن، فعالیت فرودگاه بین‌المللی ریاض به حالت تعلیق درآمده و چندین پرواز نیز موفق به فرود در این فرودگاه نشده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151229" target="_blank">📅 12:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93c4fbc3d.mp4?token=PZxNA4OypzSK1LrlrcJ4X6qV0S827vWABuwMr8YRUnVRXhyA1U0lAmr45j-jl_FD9T9_CaEQRenhI7ghJn9KPxhnRVe_vGeTHYFuj-DkO5nIc3NSiQfH7Lca_ck0ugH6mcZJ-NAj3FHwKchZ0fYYsV801szRNkHB2gzf9rzjMt5moLnuQDsMSNFEoXz3s8rjaN_1IuSQFoUO0Ndl8zB4RrTL6WfwB8Hw3Rt6zqPDpah2xXxy98jpPrm_PxdukW6WZJzKVB2Qn2z9ABYPqeRDk--OrNc3vOQy51hEilywcpISzDQI4H1B13asRzPvEfmfSXRwQ3HakR_GTYpxurf3rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93c4fbc3d.mp4?token=PZxNA4OypzSK1LrlrcJ4X6qV0S827vWABuwMr8YRUnVRXhyA1U0lAmr45j-jl_FD9T9_CaEQRenhI7ghJn9KPxhnRVe_vGeTHYFuj-DkO5nIc3NSiQfH7Lca_ck0ugH6mcZJ-NAj3FHwKchZ0fYYsV801szRNkHB2gzf9rzjMt5moLnuQDsMSNFEoXz3s8rjaN_1IuSQFoUO0Ndl8zB4RrTL6WfwB8Hw3Rt6zqPDpah2xXxy98jpPrm_PxdukW6WZJzKVB2Qn2z9ABYPqeRDk--OrNc3vOQy51hEilywcpISzDQI4H1B13asRzPvEfmfSXRwQ3HakR_GTYpxurf3rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس: باید به شما بگویم، من فقط به مدت دو سال سناتور بودم. این شغل آن‌قدرها هم سخت نیست. شما حاضر می‌شوید. برای مردم خودتان می‌جنگید.
🔴
حداقل، فقط حاضر شوید و رأی خود را ثبت کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151228" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151227">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07fe7b3ea.mp4?token=dFeV5DhBnLAjWZaSPG_lFhxz-_TAjBGqUGAXm53t8NPsZKDkXMt7sDt0AEwDb7M4C6T5m8id5K-xL6aaUplZ5G4D-ACuI4njSP7PV9F0pbokx1UanPS6F0Q8J_vv6lBykidtjzMXE3rM8lIjm-NbIFnIoNgfzRpWT0SYtxZSONMs7gQww_dp0jiwNcv10GcHbxTX5p-y5ndiyiWf_GIal2LY33FIoDUN6M49FadPXjP4P4qVC6X8tILlJCgJZ3y7ZdtuAuonjNa_epT93Im-Z36oVneDDDXhlLEmMYvl65j_hRU45EIMwbY3579hzddYz5mseKUg3pxqg92Gzi7D7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07fe7b3ea.mp4?token=dFeV5DhBnLAjWZaSPG_lFhxz-_TAjBGqUGAXm53t8NPsZKDkXMt7sDt0AEwDb7M4C6T5m8id5K-xL6aaUplZ5G4D-ACuI4njSP7PV9F0pbokx1UanPS6F0Q8J_vv6lBykidtjzMXE3rM8lIjm-NbIFnIoNgfzRpWT0SYtxZSONMs7gQww_dp0jiwNcv10GcHbxTX5p-y5ndiyiWf_GIal2LY33FIoDUN6M49FadPXjP4P4qVC6X8tILlJCgJZ3y7ZdtuAuonjNa_epT93Im-Z36oVneDDDXhlLEmMYvl65j_hRU45EIMwbY3579hzddYz5mseKUg3pxqg92Gzi7D7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: برای مدت بسیار طولانی، دشمنان آمریکا به آلاسکا نگاه می‌کردند — با منابع طبیعی باورنکردنی، فرصت‌های باورنکردنی و فرصت‌های راهبردی این ایالت — و دشمن قلمرویی را می‌دید که بدون دفاع بود
🔴
ما این را تغییر دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/151227" target="_blank">📅 12:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151226">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLYfIHSXuAWTJG48sukBV7nYjfb9RildiZ1WyTjtwVb8cD9EbqVKzdvFnmgN-tIUHQN3-jSGYYiI5fsmstIrd78DxCx9muxKSFnCIVa8RxHJ-LdK4WNt_Yu5Igd8Ls7DwN_yoOglxIoA2cfqCarlt2IXsD_C247U0MG_MrEc_iZyBDoT0JrdgWy6J321jB5dzDBfI5dJfNx4QFTDTGUXQtowql5iX3xl9ofb6cHCMGkkaqRu01jXU7Oi6kJyyLHayLn_YYFwuvRvdl0HwzpQfv7lEik7gkpLOYEVjvIss3VQRizNeF10kZlGEHNV_yO4PN9x31m_6xkRZHRG_Ddhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت همچنان به ۹۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151226" target="_blank">📅 12:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151225">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203e8b13d6.mp4?token=Z-fnFf33D3o9txR9Zp_h3GlHk59BBWUn6ZrhgWzjDfUQT5DV-5o45RJFA8g93IHcXQXBiVjODuHOJ79Sn5Wbvztz7mSW9r7U6eMaaQAS_aNcDAQbO3LBcER_vI2t5qpXgwrQJt5QMCSED-X4-4G7TyfONyHqKkjPb7UpAxOBeTi-kVXEdiPsq9ScixWpD5w03jbG0odOVJJZ-F5MVcnTAQ4PptUlfpyIucHQd7nE55E42sLAaGqwH9is6OIWoyL_Xf1BwIqed6_ccbHOIL__xhB9t4Rz1NjbDLXKSFY25WaczifdwlvZRpvopB5EzhSHS9mnFwPe-nT_EsTVicRHjqMBRC5OvTynrzc02ipvZnjfSGyyL34aR64tSU7ScZ_TwohuT0QGJiu8Pu7GF_SuzlFeGKEqJAnqDR0UZsnCwri13N8YlyB7wxYtMQq2g5sB48hZKsEBYVXYy2L3Yvh-aJ-7HFQ8t8bfCzGR1TDjWaM2uJqybjYftSvBMlb7izv__bFWRuvrweou6OSHzqnVlAp8y800ub2D-qJkemNe7vlW5EmnbI0FgPFaOqGREItMEQQpgqkbKWVEl1xk_C3r6CkOiLBXAoYUlsMlJDF1kQQJplFqL15lFjuulDXC3ScngzJeigajA0Fa2VAPudtnje-5U1ijrRY_VvQU0cvTFKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203e8b13d6.mp4?token=Z-fnFf33D3o9txR9Zp_h3GlHk59BBWUn6ZrhgWzjDfUQT5DV-5o45RJFA8g93IHcXQXBiVjODuHOJ79Sn5Wbvztz7mSW9r7U6eMaaQAS_aNcDAQbO3LBcER_vI2t5qpXgwrQJt5QMCSED-X4-4G7TyfONyHqKkjPb7UpAxOBeTi-kVXEdiPsq9ScixWpD5w03jbG0odOVJJZ-F5MVcnTAQ4PptUlfpyIucHQd7nE55E42sLAaGqwH9is6OIWoyL_Xf1BwIqed6_ccbHOIL__xhB9t4Rz1NjbDLXKSFY25WaczifdwlvZRpvopB5EzhSHS9mnFwPe-nT_EsTVicRHjqMBRC5OvTynrzc02ipvZnjfSGyyL34aR64tSU7ScZ_TwohuT0QGJiu8Pu7GF_SuzlFeGKEqJAnqDR0UZsnCwri13N8YlyB7wxYtMQq2g5sB48hZKsEBYVXYy2L3Yvh-aJ-7HFQ8t8bfCzGR1TDjWaM2uJqybjYftSvBMlb7izv__bFWRuvrweou6OSHzqnVlAp8y800ub2D-qJkemNe7vlW5EmnbI0FgPFaOqGREItMEQQpgqkbKWVEl1xk_C3r6CkOiLBXAoYUlsMlJDF1kQQJplFqL15lFjuulDXC3ScngzJeigajA0Fa2VAPudtnje-5U1ijrRY_VvQU0cvTFKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه آلمان، واده‌فول: ما همچنین باید بتوانیم دولت اسرائیل را نقد کنیم.
👈
اما باید این موضوع را از محاسبه‌کردن هر یهودی به‌خاطر اعمال دولت جدا کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151225" target="_blank">📅 12:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151224">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دولت فرانسه اجازه ازدواج مرد با مرد رو صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151224" target="_blank">📅 12:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151223">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تسنیم: استیضاح عراقچی در سامانه مجلس ثبت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151223" target="_blank">📅 12:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزارت خارجه فرانسه از تخصیص سه میلیون یوروی دیگر برای عملیات نظامی در یمن خبر داد.
🔴
بدین ترتیب، مجموع کمک‌های مالی اختصاص‌یافته از سوی فرانسه، به 7 میلیون یورو رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151222" target="_blank">📅 12:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی قوه قضائیه با اشاره به رأی پرونده‌ کلثوم اکبری: ۱۰ خانواده‌ درخواست‌ قصاص کردند؛ به ۱۰ بار قصاص محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151221" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رویترز به نقل از سازمان هواپیمایی کشوری عربستان سعودی: فرودگاه‌های نجران و جازان شامگاه دوشنبه هدف حمله قرار گرفتند.
🔴
در این حمله ۳ نفر زخمی شدند و خسارات مادی نیز گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151220" target="_blank">📅 11:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7970a23c01.mp4?token=JG-gxE0FQwvQMIZRqZSEIKI7wH_3e9ZEcXwwulG8ysX6PJbCewF3hN9Hy4sm-rL1VH7NhKtVRptIL-QAGmuVuQt8gPQw1uSXZfwBBQVwOcfsbLYsMewViL57gJip4ZJDkFt2o30yVipYX00UojN_zhMMHYO5xb6rEp04sZ-G3r9YMcx8pp8e4hcEiG8nlDTTLqMlxYfFPOpSGlW8a6NLNduy3P--TiwG7770miIKS4SU-redVHzLfaVTQZKLaWBpKA107jBzg17ZCYv9GYmun2p9opphjAU0bfeHxflo4aqsJR__5T7Q2mg936akZf_emBKi8gdHo1bFotnH2c1p3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7970a23c01.mp4?token=JG-gxE0FQwvQMIZRqZSEIKI7wH_3e9ZEcXwwulG8ysX6PJbCewF3hN9Hy4sm-rL1VH7NhKtVRptIL-QAGmuVuQt8gPQw1uSXZfwBBQVwOcfsbLYsMewViL57gJip4ZJDkFt2o30yVipYX00UojN_zhMMHYO5xb6rEp04sZ-G3r9YMcx8pp8e4hcEiG8nlDTTLqMlxYfFPOpSGlW8a6NLNduy3P--TiwG7770miIKS4SU-redVHzLfaVTQZKLaWBpKA107jBzg17ZCYv9GYmun2p9opphjAU0bfeHxflo4aqsJR__5T7Q2mg936akZf_emBKi8gdHo1bFotnH2c1p3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استاد مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151219" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndtK4NTI8mWGs5QbqahSdG0YvEDiJrisw5U-NYbaY_hpatESH28-SFX1Raqn2BRa4bGsEp_UFPw6jC_Agp7MFWg_-Y2Vz9XwYr-iQslIN9a7IH9Q_AuTqaWrdNuG9nWkItbzNwUokbotnbCcod74NR-eksN7ebDxEsdoydTEI5wJOIXijyxymRoAAiDcsHyeANnIqrdC6lJ7VVx7oC4fVFKTOdWeTIHQN5XCMsyhnr-CReL4m2lwehF-3m1593QG6ofMFzJX_hm5yHRWY27rH9fIitTbJkjW3FyDEPa0wd3W1fzaIEPcDvVJ7sK5gTxhgiA5N87-wgfxb-AyRY3AHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدباقر خرازی پس از یک ماه بازداشت با صدور قرار وثیقه و پذیرش آن آزاد شد/تحقیقات مقدماتی پرونده ادامه دارد و هنوز کیفرخواستی صادر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151218" target="_blank">📅 11:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ3SLrvRk9mbZJuxrkgf-V8hBeNzxfC46n3Hld_apjhELZ5KZvZhg5pVeyCRZJ05l5DVliwzez98IBCZGmjsYZvL_4JEEj38wqWPlG4BU-kRpOW0j26zX7mi4cuiNePoi7pHeTTx9lHYy4b4U4PbAab0U8LORBNeNVN6Q7Ox-s0El5A9zs9u7U1Pw8ETatCIfV2N3pK5gAfTuIQDzDtb2HlpJbs-_3ucnykW2bUUWzCR1riBbRipxsAq0TgoT8dJIyBRutXHq33OZ1IT_f4UFob7uT-mGntX4ct6MlWsk1usuPZSj8nMovop2u31WsVwl_WKseO1VhNuLmfPPhWHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس اماکن تهران: موزیک و اجرا تو کافه‌ها ممنوعه و برخورد میکنیم
🔴
پ.ن: لابد اینجاها هم میخواهید مداح بزارید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151217" target="_blank">📅 11:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151216">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liDdqZbmRay5tDoQh7o9iPY6isvVReNbOZ47wsCS3OLsL9j8MQrz-fHFoORd_IpNpeAjsOHwDxybFL85gMwz5HFKMbPH_ODkND849_jJuPS3fBXDQFaKjNLkJkJHNrceQ8qbcr8_Tk2oHE1NRVwfGZKc7kYiMxITClf9VhLMfnKlpGdcmJTwSCQ3nOo_97VFlFpH2zxREIbAaJwRQ89cTzZ-AE0x8fuuXzriCEm5_fkMA0yghgRSpPJ6UuG1XNLAFu-yvSw8DqSEcpLvh02d985MGGqbbxYhwestI71vNlY8kTbBx14uCPM23orRyM-SMdLIdYH69d3JSrsJVdbi4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت آموزش و پرورش ترکیه تو جلد کتاب درسی جدید خودش، تمام مناطق شمالی و شمال‌غربی ایران رو، جزو نقشه‌ی "دنیای ترک" قرار داده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151216" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151214">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpITOqDcovz8Z8bbojLg976NRSkgzzYSv2v_LxXzZlgYHvso2TlJJbnj22wzL5RCORgJqrpw9Fm12_6YqDFxCpHFAVQGzf2A5xJyfjYe_K4RQ4ktf5qVq-Hk7Dx3yYfmXYG9_ZaVl2GEX60m6zqMD08xq_hy3m97Hh9TLG6o6cqjJzJJ6GPi_gmPUcuymPz5zXKhyxndI-jVhWed45On0686mESQ-yOiqoe5-G6_hlQJOb1qjLxU3PqEpTKKseXRjWNjBVY3pjgzsd9URZuw_j2tdGYZdR0I17i0tX8BFX8TEFOGNtQ5KO7ISPkJfRrFg_ED-6Zy0sBmI1oWtk98Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1qzV7_FLq6WyzaDal9lFsA2m3O16zm_dxiHB568dHiIpZvVz6xiMJa1TQI06Cwbwm6ZERyEYX59I0sdHRiTxYl8RbbxmZvf-1w4nQku5m9YBEfbzBhP6AACanQx6FM0piUlPp3x8pNDMqiWXM3zu4MhPyfGL_R8yOyspjnz6OJ2OHUG-DjTJOkK_zCqhSQihX94S8EsF3qh6mlDG-7fBq_-BioOaF0sl4sXEaifTTwb0X3OqUKlLhNVQqOk6PWGc5x4tomLsODMO_GsowKozRA30H0ZhnlQoYexPrxbISGdME3IuvISn9OMxssEb676PAnVWvfSESpIhL--sXEqaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای تانکر سوخت‌رسان بریتانیایی به سمت یمن در حال حرکت است تا از عملیات هوایی عربستان سعودی در تهاجمش به یمن پشتیبانی کند. همچنین، هواپیماهای سعودی اکنون به جای جده، از پایگاه هوایی سلطان که توسط نیروهای آمریکایی اداره می‌شود، پرواز خود را آغاز می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/151214" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تسنیم: وزیر کشور برای پیگیری آخرین وضعیت خلبانان ایرانی به قطر سفر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/151212" target="_blank">📅 11:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMtW-kdSqPh51EIAPZZ53sGlwpRz6RsWNkqdFN3FDIOk5XWqoFQbvJhPKjUupvDoNSS8cjBvrOG9Y7MJI2OEW225mI4dzmDf00MLEHzrKQkRvi27TS3IdXF0fNirSMPROrZKHd8JJFOOvg82NWhbRH9z7nfGAxnPjcbUdXhKHsE_KHjhfF-63tV99lQCDAlPFodjFuSbFDuzljTJ2FtIrlaSEm_hJGfN5hbzRrV6MkJ7H1MNrwuMv-YTx-3tpXZiSV-nPAc3COC8v26NjgVhly9apesoa8BDK62BL5zx_7N53ulxsAorBOwbr1-rf8W6h3_kCZ6pCZHb2zYgHGMZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یوسف پزشکیان: جانفداها حاضر نیستن تو زندگی خودشون صرفه جویی کنن بعد دنبال اینن ایران رو تبدیل به یمن کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151211" target="_blank">📅 11:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151210">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e67bcae40.mp4?token=VEY9DKCpWXQx-mA8q5RSvjkfdyyeTK3FpFREQdnWFu-cMKLMmz6-_E5Y325W2eKh0cG-INQgooSsaVz9GxOGv8c4FRLyeecYhZujE6SlM3MECfQlaBhaEfz5gRtzWHtTxv2e8aDTK5Xn0PWc-RVuSEUkofKzAjjio1rMbd8_28GX8ccLPNa691gyfmG43HrMAu6Zt7vW37xhFoXeNWS_RphpF0QBaQkd3FPrQtGAwNT0mRKOBFCsm0aPXHU4iukc9JqAtaCISADPSW55XImgnnZcvZUcsYBihnOqOYf1vXXMFzwmuS4yIVywVMrK5jZcCMQp5kMh40n1PBqPgIfumQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e67bcae40.mp4?token=VEY9DKCpWXQx-mA8q5RSvjkfdyyeTK3FpFREQdnWFu-cMKLMmz6-_E5Y325W2eKh0cG-INQgooSsaVz9GxOGv8c4FRLyeecYhZujE6SlM3MECfQlaBhaEfz5gRtzWHtTxv2e8aDTK5Xn0PWc-RVuSEUkofKzAjjio1rMbd8_28GX8ccLPNa691gyfmG43HrMAu6Zt7vW37xhFoXeNWS_RphpF0QBaQkd3FPrQtGAwNT0mRKOBFCsm0aPXHU4iukc9JqAtaCISADPSW55XImgnnZcvZUcsYBihnOqOYf1vXXMFzwmuS4yIVywVMrK5jZcCMQp5kMh40n1PBqPgIfumQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: میخوام اینجا رو امضا کنم، کاری که جو بایدن نمیتونست انجام بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151210" target="_blank">📅 11:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151209">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نماینده مشهد در مجلس اعلام کرد استیضاح احمد میدری، وزیر کار، پس از قرار گرفتن در دستور، بدون استمزاج از نمایندگان و بدون اعلام دلیل از دستور کار مجلس خارج شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151209" target="_blank">📅 10:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkiUedGltl4ka9oXVgx0UHg6CkWsrpe8VulWpK7-3T34yo5sE2LOJWYEboaz67z6g61X52VZkBSBonFUI0t6IdfXwoq3Z0xuxSBvG9GrQSqtfUlA62mXNKKvpSR9S9FOEyzD3jhlrvdGIVrLSabGGCeh91b-ou4EnDXlHIXr7TzQzT46FDboZBz4rQQGel5hWVRspzv31hiq4OQULTX-v7w2TP8f1_853kQmpqafO8OX0bts4viIwf2Af4T_78vyr_8-w190xVdoDs6P_NY-JBNFzfppD9jCltBhvyLwstBpxW6E28Zyn-B116Sjxf6McR8Dh7ibtz44dCwLV585vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در جده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151208" target="_blank">📅 10:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚗
بازار خودرو رسماً از کنترل خارج شد!
🔴
قیمت بعضی ماشین‌ها تو چند روز اخیر ده‌ها تا چندصد میلیون تومن بالا رفته؛ انقدر بازار نوسانی شده که حتی سایت‌های قیمت‌گذاری هم از آپدیت قیمت‌ها جا موندن!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151207" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCFW9uKVA55p-Nd5fpvsLOy2jznoUV3QFGYMzeVNyEe0msi929za4672KO7EoDr0ed7NM-X4-SI6J5P8C04-BXwgms9Hl6Li46o93KcZI8lyAiNLibk_JV8bAodwIAOPl0VsXjoNz5v8W5O491HX_kCsnFUI8S5biQFxC-l_TyHKgOLXrPCj6VQy7_YSteiFlRquttxKzNKK823yIAiV5TCrz6WfX-4XzmVIhDKWK5U5X-tifyxATno_NDqlzu8vmI-EnstsUCuKlQeAWiV8rdKCM7fddHP7iBNWhyrllM1vYS1xlAsbTHMLr12svHwYiE6yFhb7yqhf02tFFn40iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند شناور اماراتی را که قصد عبور از آبراه جنوبی تنگه هرمز داشت، وادار به بازگشت از مسیر خود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151206" target="_blank">📅 10:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qhl6lU1SuUBZf_Z53MxJsg5Kwst61RURcxJEBJrjDgzHVvWmf9D2c0biSgVou9LY1Q2-Gxo61Y6W06kXKHGa7rrnBT7-DAXPOfZzGvqUIx-i-Vv_yv1kAazB1cajGXRKxgCkELDaibx67gCos5weV0j8OvUUngdN0CPYTSUxlu5TNDuTwvYrKxZ8CXi18cRcm7GKD35y-OIBxIyNrD2txTgsDMS2TeEhJifxV8dOmui_nBAmj3n6Qcn7ShcT_9v7-Pvk7Wn5B9zgS53-P_DKy2C3HMhobSjxa-QevuPiTkKBb1r7LE5dWqqvlC3hETGvjW2EsobJnQC9JdDRIiLwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) به مؤسسات مالی خارجی یادآوری کرد که در صورت ادامه همکاری و انجام معاملات با ایران، ممکن است در هر زمان و بدون هشدار قبلی تحت تحریم‌های آمریکا قرار گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151205" target="_blank">📅 10:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151204">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3d_4HyvP2ILSuX_HKSL_yoL23cVy-SuzdwUlAVJonlLADd95CAxSTJfyAx8Yb7j3KGvZ-KX-MwozK1BkUGC-3pcNlnah5OJiboiDjNqdHVLtbUnNi80w7XgtJx8x3B7NJbJUaVSJSaAafumZSIQyNMqHOOyriY51x3_4EVn4vX2ez7cO76PxvG0IczA2-FL8o733nBiBWbe7Q2FS_Fcea9A6_-FmKODBwhWThIkh2XcnsyEgxfrbLA1CKU4aH5mGFMpBJyQnJTElMuKWoMMRMV-IMSqwusmr0A-kKYPv09syTqJ93lKr_Z__34he2jUaoQAK1ptftyEYXEM5dw1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: بعد از بازرسی بازرسان-که دور از ذهن است ایران اجازه انجام آن را درمورد کوه کلنگ دهد- آمریکا تصمیم می‌گیرد که با چه کیفیتی باقی مانده فردو و کوه کلنگ را مورد اصابت قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151204" target="_blank">📅 10:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151203">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3288f3052e.mp4?token=cLH2XA9W6OqREJpdBaVHONmMwDtjOYOig9nmHOK_7OrhjunFF3p0eOrYwDojHVOYUJqFexahgsAKYqc_IlNx7dbEpvPLRGlu5H6Cx8Ldv4RsMcBNWatTStR5PNLZdXPOOQ5f2MEJjeKEOt5xpP7pRty_LEXX2gJnyEIQz-HD8H9w4xWt2e0Sti3ZQtGysfCqFWL-X1NIx5GWmuD0T3-9rvOYrKyr00LGuMu1QC-7RKGqrtgN7Di42KoiID7TgTGk9p1NoBMQrelEeEncu5XWliLlK1YWaDWdcOSpuAZl91eIRSpENCJtzd5i6ww0R5F29KSI7Gphrb3b7HMJ8LxlXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3288f3052e.mp4?token=cLH2XA9W6OqREJpdBaVHONmMwDtjOYOig9nmHOK_7OrhjunFF3p0eOrYwDojHVOYUJqFexahgsAKYqc_IlNx7dbEpvPLRGlu5H6Cx8Ldv4RsMcBNWatTStR5PNLZdXPOOQ5f2MEJjeKEOt5xpP7pRty_LEXX2gJnyEIQz-HD8H9w4xWt2e0Sti3ZQtGysfCqFWL-X1NIx5GWmuD0T3-9rvOYrKyr00LGuMu1QC-7RKGqrtgN7Di42KoiID7TgTGk9p1NoBMQrelEeEncu5XWliLlK1YWaDWdcOSpuAZl91eIRSpENCJtzd5i6ww0R5F29KSI7Gphrb3b7HMJ8LxlXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌های شلیک شده از یمن، تاسیسات نفتی در ریاض، عربستان سعودی را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151203" target="_blank">📅 10:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151202">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca28e1a91.mp4?token=WnOwZOEbeIcT0tuyJBpA6Fv-Lq5j9UoGTI3StX855m82HT-zsgcYmwV1MLkpjOFKfFhQmbqLRWNRbggy-vAVWXiQ6_LATCN5F76eyj0rP-RT6CW-4fJ325PxMAEO8dFz1KHA6NCud-4x-3TIo3u6Z9crQMZwUJ_Smn-VKZP4t0Kn4QQCvQrpWKyL9zOeRlH-ptm6s_mO3DrDIlf4gQT-fxo_rFOhbIR8cEyOMTnRQ1erDfndg3m-HMp1V0UCOGETMn03Bf4OdSyt_C8p3JVsxEWFahTjrXoZky_PYkqA0Cp6TlDBCL3JCCdVqgcBHfkShe8HILZOS2ppNKt9LIb7HjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca28e1a91.mp4?token=WnOwZOEbeIcT0tuyJBpA6Fv-Lq5j9UoGTI3StX855m82HT-zsgcYmwV1MLkpjOFKfFhQmbqLRWNRbggy-vAVWXiQ6_LATCN5F76eyj0rP-RT6CW-4fJ325PxMAEO8dFz1KHA6NCud-4x-3TIo3u6Z9crQMZwUJ_Smn-VKZP4t0Kn4QQCvQrpWKyL9zOeRlH-ptm6s_mO3DrDIlf4gQT-fxo_rFOhbIR8cEyOMTnRQ1erDfndg3m-HMp1V0UCOGETMn03Bf4OdSyt_C8p3JVsxEWFahTjrXoZky_PYkqA0Cp6TlDBCL3JCCdVqgcBHfkShe8HILZOS2ppNKt9LIb7HjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درمورد مردم فلسطین : آموزش نفرت از یهودیان و اسرائیلی‌ها در خون آن‌هاس! آن‌ها از زمانی که شیرخوار هستن دشمنی با اسرائیلی‌ها رو یاد میگیرن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151202" target="_blank">📅 10:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151201">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
اگه نمیدونی دلار و طلا بخری یا بفروشی حتما اینجارو داشته باش
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151201" target="_blank">📅 10:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151200">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نیروهای دولتی یمن: ما به همراه نیروهای مقاومت مردمی، کنترل کوه‌های المنظره، الاشارف و ذیبان در حیفان، واقع در جنوب تعز را به دست گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151200" target="_blank">📅 10:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151199">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مدیرکل فرودگاه مهرآباد: ممنوعیت پروازهای نیمه شب در فرودگاه مهرآباد برداشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151199" target="_blank">📅 10:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QENpdGmcTXWGGQTqRTLTPjvIvomWf-hRzDzzT31gHQj6pk3T2ev_I9ynXm6EVlLSMoBipp_gn9HhNs6DHeFXiaCeYPTAhXUtR3EeWfHGWoDWJIdfKyP3iSkZOMb-QFNo5i2k1hFOh0F0yO4XUoh052R2V6piEuh2_FqFtqx3YY74JBb9_Ydapm-H-a7zYFhqZGcuv5-eYpYTUPmEbUEz5DmjmdLaHPeBXDi-tNpmtVnqGqA4-84INhNMdLdJDBcoKQ95Qjo_H3UGKdySFpZi0D6N_pGuAy5o7t56P_Moj0HQqXY4xhAbszLmSiQjiph45afLgbSiaIrn7GSNtkNWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رتبه‌های برتری که مدرسه نمونه دولتیِ فرهنگ (وابسته به حدادعادل) تو کنکور امسال داده :
🔴
زرین، پسرِ بادیگاردِ علی خامنه‌ای : 16 انسانی
🔴
محمدباقر، پسرِ مجتبی خامنه‌ای : 106 انسانی
🔴
محمد‌امین، پسرِ بذرپاش (وزیر راه سابق) : 173 انسانی
🔴
محمد، نوه حداد عادل : 910 انسانی
🔴
محمد، نوه محسن رضایی : 1700 انسانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151198" target="_blank">📅 10:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
اکسیوس: اظهارات رئیس‌جمهور آمریکا درباره علت خروج ۱۲ بمب‌افکن B-1 از پایگاه فیرفورد، با آنچه وزیر خارجه او گفته، در تضاد است
🔴
روبیو این جابه‌جایی را معمول و دوره‌ای توصیف کرده، اما ترامپ می‌گوید اقدام مذکور به دلیل وجود تهدید امنیتی از سوی ایران انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151197" target="_blank">📅 09:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151196">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
رئیس سازمان وظیفه عمومی فراجا: خرید خدمت نداریم، اما معافیت ۳ و ۴ فرزندی همچنان پا برجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151196" target="_blank">📅 09:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151195">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
👈
پژو ۲۰۷ از مرز ۴ میلیارد تومان عبور کرد
‏
🔴
قیمت پژو ۲۰۷ اتوماتیک سقف شیشه‌ای امروز در بازار آزاد با افزایش ۲۰۰ میلیون تومانی به ۴ میلیارد و ۵۰ میلیون تومان رسید؛ جهشی که همزمان با افزایش قیمت‌ها و نوسانات شدید در بازار خودرو رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151195" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151194">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyHoR6y3zCss_QdezGWgCz1_w85gQJQW6cf2uoutErB6xmQPLQb-CcHfO9_s8VcY3oc-QalJYGNa5xjAAqwprjet9rVoUMp3LPVyP2ny1Cgy94-TyNHc4TD3NFHzWiFvOajKxWXj7At6vTp31w6GLm3DweuU_naYL6w-HdWb6ZyxyBu2Hk1BHABT6ZWGpwVrx9gU0EeXL6CTcCdPbvDuVgdJ90BGieRYsZ-lbeeqZOnUtLoamujf9CKsvYX724HLfAdVy17Ie30A63rFznuoqg40S_EqUfR0om3JlYgTa86kjXrYNwpw1piKK2ChYAuTGKL1cbPTClJV3rO6a4Gcyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پولیتیکو: مدیرعامل آرامکو هشدار داد ذخایر جهانی نفت به سطح خطرناکی رسیده است
‏
🔴
امین ناصر گفت از زمان آغاز جنگ با ایران، نزدیک به ۳ میلیارد بشکه از عرضه نفت جهان از دست رفته است.
‏
🔴
آزادسازی ذخایر نفتی تنها می‌تواند به‌طور موقت کمبود عرضه را جبران کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151194" target="_blank">📅 09:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قیمت خودرو از کنترل خارج شد؛ سایت‌ها هم از اعلام نرخ جا ماندند
🔴
بازار خودرو در اواسط مهرماه ۱۴۰۵ با موج تازه افزایش قیمت روبه‌رو شده و بهای برخی خودروهای داخلی و مونتاژی طی روزهای اخیر چند ده تا چند صد میلیون تومان افزایش یافته است.
🔴
شدت نوسانات و قیمت‌های غیرعادی باعث شده به‌روزرسانی نرخ‌ها در برخی سایت‌های تخصصی کند یا متوقف شود؛ وضعیتی که تعیین قیمت واقعی خودروها را دشوارتر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151193" target="_blank">📅 09:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس پلیس اماکن: قلیان و موسیقی زنده در کافه‌های تهران ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151192" target="_blank">📅 09:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گوترش وارد اسلام‌آباد شد
🔴
گفت‌و‌گو درباره تلاش‌های دیپلماتیک میان ایران و آمریکا، از محورهای اصلی این سفر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151191" target="_blank">📅 08:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ecb9b656.mp4?token=Le3jmgtChyvsvXQ-97m9cWp6CodUwlJebteCkswaO_CfigtQVmEvOrivt-8zlSZSIEbFy3oeKxngZPfljQG-Poyj3qxjqn7F2eEXt_50u-uVG-LJKhCEWFxGAlgjlSba-3sVaqWXKCGxdz6i_GhHJG8Zk2ST4pW_VItqWQzo5mrMUgnE79DVIJ_O_ac9bC9ACnIlGqHKIxCjvjAbenl38YYtViR4O3DjDUuM52ifsnwgXz8jkQ4sdnu17J4-uKUZqw94ER3GbE5KgIEKJpgozbpxDo3RtJWU_RztpJ348qrFTt4aB9jYU7BVI83wNHzY4mGot1WiWoEMOoH7xk-Xeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ecb9b656.mp4?token=Le3jmgtChyvsvXQ-97m9cWp6CodUwlJebteCkswaO_CfigtQVmEvOrivt-8zlSZSIEbFy3oeKxngZPfljQG-Poyj3qxjqn7F2eEXt_50u-uVG-LJKhCEWFxGAlgjlSba-3sVaqWXKCGxdz6i_GhHJG8Zk2ST4pW_VItqWQzo5mrMUgnE79DVIJ_O_ac9bC9ACnIlGqHKIxCjvjAbenl38YYtViR4O3DjDUuM52ifsnwgXz8jkQ4sdnu17J4-uKUZqw94ER3GbE5KgIEKJpgozbpxDo3RtJWU_RztpJ348qrFTt4aB9jYU7BVI83wNHzY4mGot1WiWoEMOoH7xk-Xeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: سامانۀ بارش‌زایی صبح امروز از غرب وارد کشور شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151190" target="_blank">📅 08:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvjOLp19ioHZh5vm9IGDvSt0J2-YuR7gNjaSDTA61qD4Ywg4lZtm5-GtJI6KBmDWINLNXjlAoZhUkMhjtapvbFN4rngNjjvQeCYmIJVUNFikFScK5VvPm_f2WM6DeGaIx_tEMp8XEmCY9C9Ga2rM3cJlvm-uVQ6Movf9vAMH6wNfYNCxEFkJL3CHaHwgOEiaRFgi-u1r5TDV5dEf1OE1tEAxeipo6p9fsn0XpNvp16YIbF8AwbUP19yI6rL6LGB3mhk0LP60hcCj1XaZVwjcxcb6GDcHPmWaLjatbC9cQPBqLJZ2WRvoULhmglNtOae5LfkIudZ_1h_Vjkr2IraoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک بالگرد MH-60R نیروی دریایی آمریکا در نزدیکی ینبع عربستان سعودی بر فراز دریای سرخ، کد اضطراری ۷۷۰۰ را مخابره کرد.
🔴
این بالگرد یا روی یک ناوشکن فرود آمده است، یا در دریا سقوط کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151189" target="_blank">📅 08:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151188">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sa-rxb7TNAhCsLz4g4W8ILuzWqfsb8oiScNJFHz4roWJ2Msvvjb41RhQsKYXh1Z6maWswNZp1ZVnR7aKF9Ajbsf8AVM4v5a2WYcKZ6i8w85IArxIM0xadp2mqULcohM6x6lLatdbKObDMxfoDEaXaLT2mLB3WPZUv6bcF3jLIVeaFik9LNQR8LvIpr-6ijYeqGZcvOU7v9KCWGF05Z4Z3es9p71OQYoXlJMX4e2LVH2Oc9ijp_DuYAqxJ1Kz28My5jfF8-nFCBo2KfxTfDh_1qBYTgVTmQiQ6JlIAsvLKznIgkL6oGshbcevJ6VeQk863B_UzMsPjCgUn8xd_lCc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ حکم اعدام یک نظامی آمریکایی را از طریق تیرباران امضا کرد
🔴
نضال حسن در ۵ نوامبر ۲۰۰۹ در پایگاه فورت هود تگزاس به سمت نظامیان آمریکایی تیراندازی کرد و ۱۳ نظامی را کشت و ۳۲ نفر را زخمی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151188" target="_blank">📅 08:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151187">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9396b51645.mp4?token=d6eaZAWQZ560asBF7HGROKJbteYC8JAKB95HWGCoPTla6i5vmLR4RW1TTqhopBBWgs1TSqghgCna7yaIsgaAKbyQTN_YJKHfBLoG_aVRLLoePf4_InZ0BPou1qvkwtOAz4ZuHCxoZ-nhPBhX0IQo2k2xdVcXKqfqGBYTCD0zca5K3_EiQwKuIvmufNiw4wlUw1zum6HeBTefXW4y4rHUqzjfQ12pZPvFt9isPIcPX1AKQ9J5lP75S28d6M_FTBTeZSeoUCPGNH0iO9HLTZsODHGGGtVFS7RN_ORSBAIUlu7c75KvEBSw8KGZyTiqRpRVq4mUcD1BcaaXV6KBopGx26JTz9RC93FN8zryx7fMo_M5gwqFOxDJPkuXKmYrtJIpAMSmGteqhTNyzkTdw0WA-mhJPe4X3FDWK1fonHO5uDjbBwjiLzEDeSgBg8vxsbenPs7GJ6ax6xOMXJmyhozU69Tbc36RNBjxpUTf6vRcpjXZNIUpuwNiI1ew47MtZzdmaIRfQX8j8E-acX7GJnt0c4DzMBtfEI3lEzU5pD_r7IEbdw11Wtw4z0gErRtLbCepmGKsJqEKUCBGXcpS9ZMIPLh063bMB87G6a1kw8VfaEGZkumlp5i2vfUEnUwHV7DR0kHHgdYhbUez4UpszihltVKRsjbY6LEUMiC1UTCc0C8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9396b51645.mp4?token=d6eaZAWQZ560asBF7HGROKJbteYC8JAKB95HWGCoPTla6i5vmLR4RW1TTqhopBBWgs1TSqghgCna7yaIsgaAKbyQTN_YJKHfBLoG_aVRLLoePf4_InZ0BPou1qvkwtOAz4ZuHCxoZ-nhPBhX0IQo2k2xdVcXKqfqGBYTCD0zca5K3_EiQwKuIvmufNiw4wlUw1zum6HeBTefXW4y4rHUqzjfQ12pZPvFt9isPIcPX1AKQ9J5lP75S28d6M_FTBTeZSeoUCPGNH0iO9HLTZsODHGGGtVFS7RN_ORSBAIUlu7c75KvEBSw8KGZyTiqRpRVq4mUcD1BcaaXV6KBopGx26JTz9RC93FN8zryx7fMo_M5gwqFOxDJPkuXKmYrtJIpAMSmGteqhTNyzkTdw0WA-mhJPe4X3FDWK1fonHO5uDjbBwjiLzEDeSgBg8vxsbenPs7GJ6ax6xOMXJmyhozU69Tbc36RNBjxpUTf6vRcpjXZNIUpuwNiI1ew47MtZzdmaIRfQX8j8E-acX7GJnt0c4DzMBtfEI3lEzU5pD_r7IEbdw11Wtw4z0gErRtLbCepmGKsJqEKUCBGXcpS9ZMIPLh063bMB87G6a1kw8VfaEGZkumlp5i2vfUEnUwHV7DR0kHHgdYhbUez4UpszihltVKRsjbY6LEUMiC1UTCc0C8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعقیب و گریز هیجانی نیروی آگاهی پلیس و شلیک برای متوقف کردن سارقین متواری شده با موتور سیکلت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151187" target="_blank">📅 08:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a2c104bc.mp4?token=BArUsoFbX2JtH-Rf307Yqknt0nVcHK2ncpQtFpzqbbAvESeypemQcsymUFux9xM2V4rinF9u55xBKhXZaQS492w4BA4iNUWpPjnMOuyLCVF_WiDg9sGlKYsOR4xzRu3PKrgKswG5ZOLgGsJhDUefVJV0CAhjn_KXoTXpaetjJMeyOPLJ4TFmP-3sE_XVP31Dz1U4C42qL5ptXoSa2Wfd_QwtAXX0ZOFrOTy_gLj-WLEjnaOGfh38nn7Sw6CATO4tHB2NA8XPNwLKpPuqzjihN_rLx-OpEQl9XvS0xVTXojln2aiPk9u2Z9a3hk6FKtC4RfTs5pqx_HRLj_vJldKQtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a2c104bc.mp4?token=BArUsoFbX2JtH-Rf307Yqknt0nVcHK2ncpQtFpzqbbAvESeypemQcsymUFux9xM2V4rinF9u55xBKhXZaQS492w4BA4iNUWpPjnMOuyLCVF_WiDg9sGlKYsOR4xzRu3PKrgKswG5ZOLgGsJhDUefVJV0CAhjn_KXoTXpaetjJMeyOPLJ4TFmP-3sE_XVP31Dz1U4C42qL5ptXoSa2Wfd_QwtAXX0ZOFrOTy_gLj-WLEjnaOGfh38nn7Sw6CATO4tHB2NA8XPNwLKpPuqzjihN_rLx-OpEQl9XvS0xVTXojln2aiPk9u2Z9a3hk6FKtC4RfTs5pqx_HRLj_vJldKQtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از آتش‌سوزی در فرودگاه بین‌المللی «ریاض» بعد از هدف قرار گرفتن توسط موشک بالستیک یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/151186" target="_blank">📅 08:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox2Ldy4A3G8JCVUq34kcKYVAlx7Uq4IDQKFGmc3iDLrBLhDKKFjqvchez6sCRvH10CYAfuIlHuWLK4gQJ8J4AKUXbIl5vXp4SD_LxUICOCVTl0rpOeD_tIm1uqZ58IovEByyB1acE0ZrgksNjNQlZDvGsHnqMQkEsYY0DwZ3qZ3vgprinDoFK2SVojpQ791ZRv53vaJq2u_ovQEd4jdwsNxJDx34VOci2nSUDw97JJimtvSV6q6oMCRb_o2C63_hv3Lg10Be6-ORfyIec4qfw1_H-Mc2AeRERPqPaCKEld_vkblSYx5XpyPuixgkXyWwosQ4gBmhR3ynSL6urhZP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هاگوپیان: طاعونی که تو روسیه پخش شده، حدود 100 برابر کشنده‌تر از کروناست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/151185" target="_blank">📅 07:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmQ2DP7vc1Z9ENha1NKwyK0NGIGud2J-BVk_tcXW748yFFUcJIgCJOmxuJan8nibGFfuac06FrDcSIFERpzRxYWp7o4toN_DBGk4LGGUVqEYTjvrz2yzmH6OoALmoExYbvWttYfjfB3I7_EatKkZddG0ZEnyi0vr3qCKyjyuIteDvB-33GyN02RHppN1kUsDGKB7F1PXddRFOpvAX0cvCEpyENTBohMAML8jYSKnUxs2HQxAvye3RROrQLSsmUEwy2np6SBTDElzfnBhPPxYIXdYhxR-dAhEFzxyp7vSJ5Qev15Kg8ZYLp_jsBlG1YHHOcVr-uPk7gu_4zROCl6TZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آخرالزمانی در روسیه
‼️
🔴
ثانیه به ثانیه طاعون درحال گسترشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/151184" target="_blank">📅 07:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: کاری که ما در ایران انجام می‌دهیم، جهان را از بدترین فاجعه نجات خواهد داد‌‌
🔴
رادارها و پدافند ضدهوایی ایران را منهدم کردیم و کنترل تنگه هرمز را به دست گرفتیم.‌‌
🔴
قیمت های بالا هزینه کوچکی است که ما در ازای ایمن نگه داشتن جهان متحمل می شویم‌‌
🔴
هر هفته نفت به شکلی بی سابقه وارد کشور ما می شود‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/151183" target="_blank">📅 07:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiZ7OYbobFtikWwgzXEIisKSxY2NgE7cZxVyLvYO9r5XJK6imWGM2uA2TnJl61PXGlwn-sdG1qN3VYzF8RAh5SvLQXkYxDClwMhLhxcNo-WYTlKvjM_z5j8HKdfC2pOg6PmfhUQ4kVimXnlDowWfvJQev2UEWCJz9oCzkxBuipbZekw-qDn0bwSZ83EiwlXM-Nsp7zp_JGr5nnEPr34tEmNxaAwRzi43FuMEG-gHKc05E5AEhe8xqiYwQcjuJL4mzrRRO7aXfA1JlAJLG6UJGkdxNeJLgpHG2XXyrcgUKAHDiG4Uf4AEnqmv4ob92OJ2e944KjH1fJ2BfF68B9QvqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وقتی یه مسیر می‌خوابه، قرار نیست اینترنت تو هم بخوابه!
⚡️
+130 لینک فعال
🌍
+35 لوکیشن مختلف
🇺🇸
+۴۰
سرور فقط از آمریکا
🤖
مناسب
ChatGPT، Gemini
و
بقیه
ابزارهای هوش مصنوعی
🎬
مناسب
استریم
و استفاده
روزمره
🔄
آپدیت مداوم سرورها و مسیرها
💚
اینجا قرار نیست دنبال کانفیگ سالم بگردی؛
وصل شو و کارت رو انجام بده.
🔥
خرید از ربات:
@litvpn_bot
❤️
پشتیبانی ۲۴ساعته:
@mahan_lit
.
🔥
LIT؛ همیشه یه مسیر دیگه هست.
🌐</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/151182" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا:
به موسسات مالی خارجی که همچنان با ایران یا بخش مالی آن همکاری می‌کنند هشدار داده میشود که ممکن است واشینگتن بدون اطلاع قبلی آن‌ها را تحریم کند، تمام موسسات مالی جهان باید فورا برای پایان دادن به تراکنش‌ها و روابط خود با ایران اقدام کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/151181" target="_blank">📅 01:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CQ3YcaHjODVCXBQhi1fgpoEWQGhaImb9tLDY21HNVJvhDcGwnaTh3FXuMk8ngVIGPavFVy1ADtWibS6rgFHQ6dIVjhfZ_T9WPGDUTmho9EC5oD0bP8hQAoff9UD_pxObqoDqP-6kkysJB2ujGmx9IKi4TEXJlPDXYKt0pRWszOCh2aLkVsy2rGl2cd8In5rGb0pocWaiBJVfgkPBNElVw6eioG5zJY9EK-W55jduEccznB_JX5c9N34Y5i6jzrIvUnjop45T4R-ApRDMjVMBkynSwQcPMhTl-m3zn5qFfc6Z1W4UEAwaQc8GBIMKRpf0bsiIJs_ukdkkL2Cn0UcGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mb7wTZyNr2T6rFQnLEUvMRkGt4_52bh00wwmXXK8rUFHe5VQbuw_vXAlmmNqkmjHpHs2fj4zyeySwTPPG7NrLmdt5x-8gfChF9aZvG_95e5ggKEhKMGhmeJw3PWVSjemLBed_T311--ZgfMpjO0706A-1WBGK63PCt7v_iShTaYEHvle0iUh2S7CSiiTL4G586kIEpbRPyQwkVNBMmFGGWw_7tZnT_HFBvHjnY-9XbsqaIEHI_cc0qXFvYAPyizAGUYJmhUnZwmlbupQISH-L8U8_0wUFwC0OCkpknuuf4HzJTwlsh01EGOFEp6InXe5z9dYkcnxiN-eNCYaWHV_0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اختلال بزرگ در فرودگاه ریاض در پی انفجارها در فرودگاه.
تابلوهای اعلانات پرواز در فرودگاه بین المللی ملک خالد اکنون نشان می دهد که تاخیر و لغو گسترده پس از گزارش ها مبنی بر حمله موشکی حوثی ها به ریاض در امشب وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/151179" target="_blank">📅 01:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=e4NTyEdUBoYJEf1TNlTp-LsKNFw5pHTf5gN6jPObnYXtWztocsy2qDsX16gvUW4smovi5VugLyZGgv7J2IrHSCfQJ3jIBjeBtShiegkjlRHyfj41CZr4XSRYjB6qcghcXTLeuNV5L2-ZyrOi2yem6DpSXizdnsMtMey12Jhv_Is6sdXZMd28Mx8dS3vJpyDHvemWS6_4tfOu08GJJeUvsZMk89-I14NAcrbiMODNhfxSdR2bZtME_qbfN6JLyrsbJ-WH_jccD4OaouVXSjHzXCSDyPdIotv-ycqbyh37yGfgGcQASX6KdHdEWbXz67SFsqm3QTez3CpSbMINc2KJsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=e4NTyEdUBoYJEf1TNlTp-LsKNFw5pHTf5gN6jPObnYXtWztocsy2qDsX16gvUW4smovi5VugLyZGgv7J2IrHSCfQJ3jIBjeBtShiegkjlRHyfj41CZr4XSRYjB6qcghcXTLeuNV5L2-ZyrOi2yem6DpSXizdnsMtMey12Jhv_Is6sdXZMd28Mx8dS3vJpyDHvemWS6_4tfOu08GJJeUvsZMk89-I14NAcrbiMODNhfxSdR2bZtME_qbfN6JLyrsbJ-WH_jccD4OaouVXSjHzXCSDyPdIotv-ycqbyh37yGfgGcQASX6KdHdEWbXz67SFsqm3QTez3CpSbMINc2KJsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین ویدئوها از شهر طاعون زده شلخوف در روسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/alonews/151178" target="_blank">📅 01:11 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
