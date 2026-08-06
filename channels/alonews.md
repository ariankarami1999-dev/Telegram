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
<img src="https://cdn4.telesco.pe/file/kF-7X85kdkktmzHvQFspvR44Z0S0k0TotNH7CzwYqCxATVyV4Kwb6fOpXRsUBP_XW7CAtAGbhAiwSPsO3nGoI3_UsT1qPd7bVfY3YI8zaIX1oZWW-_jli1gWptMDMANW7mDWIkT6mxDuKM4PHX3hVXIQMhhNenrG5WBl0bH05-IuF85aHfHpjY2_0imotGtiafLzPoGFHNImvuPK78DkNyD799dTdZkw0Hx4_oSe0ZHdOtRmnQeViFPol6omDlZYwqsUkNslR1Wv7uOOkh46EgREbLEuorSvS0SiPxBdGqugvg9g8A-x09ZfgcmcJS_QKEP9MW7RBdYUMU5S7pap5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnPgnFbkFg-bVdXCLqpB1taeTTbs68G78FovTHOLltC810zSciVcEQAAsMGR3W63po1fsj8D756ZKVLcxMPemSf1BZcSGGNpEaDS_vZjyGftNjOdPrD1qKr257JcIVYycAHqMdAbG4Ve-mRDd4AKjNj22h0jR5YQS8_7T2iDXC54BBnALghn3i0-09Q5jjQ3KXX8ME7UNaIRUwxW2HGUpGJIIImCYMIZbs8lunmGyMVIH5AZdBx1dtFLVivz-ub37bCgfQC8xptdkRfnw9NyNNsZACP0ZCWn2daAwYpaovIb4PFTyKoAnoKvVp6JMg8Gtvl6obv1XdqYV8DhkPNm9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن روحانی:
در سال ۱۳۸۳ میخواستن برای سخنرانی امام زمان در تهران جایگاه درست کنن و سیستم های صوتی پیشرفته هم‌‌ بزارن تا وقتی ظهور کرد و اومد سخنرانی کنه؛ صداش در کل تهران پخش بشه. رهبر موضوع رو فهمید و گفت اومدیمو امام زمان ۳۰۰ سال دیگه ظهور کرد از الان جایگاه درست میکنید؟! جمعش کنید سریع.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/140234" target="_blank">📅 18:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
هواشناسی: به نظر نمی‌رسد تهران دیگر رنگ دمای ۴۰ درجه را به خودش ببیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/140233" target="_blank">📅 17:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueAOVORmOeSnixPqu5R1UI9cW0IviyWM8f1ldAGMqEwu8_sxTeDrKPibhVu5TLt0lWATbEtDhfePRJiG1GqNmuOnY5EZvgTFuWGZylkbso1gbSP-xAmkTHER_2V2XgEpN254TV85wNgd_UBtHLE_I7EzY24KoOZn4B-XZWttQe-9kigfMknDkpyhdluWZEooquQNfWnDzEylYfWndIos9brp1xS0yWVkXhQQcp0E1Nx-pimre8ZoUw2kVfTbVXxhmNIIkZXElzs_BnAPpUqR_YvG6RR3qupe9SuEbMlj6IrrZ89WDE9MMa1bbf7fqsNwXPB5WMr2dxEVHURHhbj03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
بعد اینکه آقا رو زدن باید دنیا رو به آتیش میکشیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/140232" target="_blank">📅 17:35 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e9af9adf.mp4?token=Gg3VLzeY8klfwWlWO3ovpn-N83tL5kCwd5YjvDW-BMP7x2dmUd-0awcmMj1UQLQaBtRYfK-JKUwConFi6jFGAidQZDBNCPs_24VcltCgPLOIKMIIl8isZcyIilMCRF1aNHKGa9abtMLp3t_gXf9KGFYsHoP-nCL5SobhTI3JR-vMbJn5T7PW5qIha-ZVVZ1_1kIVgmcmqx_brR6uPn2e8bsOGkN_StpfVJlqIETAdBsZBRluCJiBWfVbgHIkviNi2x6nBVAxdPtdnZ06Mts_Gwwq3fzGquDg203zJwlwYjvPjNRJ92swu2fkA-bFu6wQCUY2SBruV2KTyPVgLuTR-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e9af9adf.mp4?token=Gg3VLzeY8klfwWlWO3ovpn-N83tL5kCwd5YjvDW-BMP7x2dmUd-0awcmMj1UQLQaBtRYfK-JKUwConFi6jFGAidQZDBNCPs_24VcltCgPLOIKMIIl8isZcyIilMCRF1aNHKGa9abtMLp3t_gXf9KGFYsHoP-nCL5SobhTI3JR-vMbJn5T7PW5qIha-ZVVZ1_1kIVgmcmqx_brR6uPn2e8bsOGkN_StpfVJlqIETAdBsZBRluCJiBWfVbgHIkviNi2x6nBVAxdPtdnZ06Mts_Gwwq3fzGquDg203zJwlwYjvPjNRJ92swu2fkA-bFu6wQCUY2SBruV2KTyPVgLuTR-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فعال فعال مذهبی:
آمریکایی ها دنبال DNA امام زمان میگردن تا از روی اون پیداش کنن. برای همین به حرم امام حسن عسکری حمله کرده بودن تا DNAیشو بردارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/140231" target="_blank">📅 17:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4xJDPL5gU1FQJrjzsgCPHr75EoscB9w14kUhKdJCD4rTHa3oytrQkBfQhupgV6714KQA_HOOzGhQU1axlyuw6q4dZcHOd1N7I9yG_6NqZCRrrQYn_-bbfZ3PbZSK9a004wa5fGcFdy3zubL2Ah_nQ-dsRT4irhmu1xIKPdo_t9KRVN9hTdoGqBM7oHZpjpPdsq9i8GdrtIf7OSFd9NrDEdOE-uuDzxfNZplXtWWSH6yiBh1zfGq1epSX46e1vrNxax3AcKw05Q027D4hrSngauPHoBpLwYupoqhx3hQxU7zv0P_hTxqjBKAMATFxXRqcRGW19BostGiobJ13TfZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جی‌دی ونس: مذاکره با ایران مانند قدم به جلو و عقب است؛ ایرانی‌ها بسیار سرسخت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/140230" target="_blank">📅 17:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
حسین شریعتمداری: باز شدن تنگه هرمز یعنی باز کردن راه فرار دشمن و از دست دادن یکی از مهم‌ترین اهرم‌های فشار جمهوری اسلامی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/140229" target="_blank">📅 17:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
مجری تلویزیون: مردم از افزایش قیمت ماشین خیلی ناراحت نمی‌شوند ولی اینکه کیفیت افزایش پیدا نکنه بهشون فشار میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140228" target="_blank">📅 17:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
هم صدایی سایت‌های اسرائیلی با جبهه منحوس پایداری
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/140226" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140225">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4mX4qZ_bqgMoJSQJcWmFmBFTLLc8k5hpXskI2RyuCqV5bOiriEBciMXzOm6trgCA_-qPWd9bVNLe6iD_MXmsnWXX-jMg3Y6y6USrcg2DEKjiwf7GJuISEZ3iCri9sojdmsTYbsAWMJ_4Bv4xTZ2bjVodXkAIx-mCEK1sdV8LdSsdPhpb-qXWbV4n4aGjjGrGNIKD8slf-F8_HPNRngVNVeoaXNbdK_-lGi5IEgEqkyF7LCTaCdaG0VSJyXDUt_n4vjxatYdWn9iBcIJ7V6jiwNKh6bBdqXkOBKl-I3NirOg6U79Yn6AXcnQaNaZ_mXHR4JElMZqnYV8QxX32sBXgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنایه عضو هیئت رئیسه مجلس به بقایی: شما سخنگو هستید، نه سخن‌نگو!!
‏
🔴
علیرضا سلیمی، نماینده تهران و عضو هیئت رئیسه مجلس، در شبکه ایکس نوشت: «حضرت آقای دکتر بقائی سخنگوی محترم وزارت خارجه وتیم مذاکره کننده! جنابعالی سخنگو هستید نه سخن‌نگو!! برخی خبرگزاری‌های عالم از چیزی بنام توافق جدید خبر میدهند لطفا ملت مبعوث‌شده را نیز محرم بدانید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140225" target="_blank">📅 16:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6580b7d6.mp4?token=ZxmLYviAANCn8PepTLPW48BikyK7YWuDsK45I9T_Ro2CD0hYW8-ClQxs4EjtE2gK3wt_inGMZ6o9rZIhLaR-XuxDPKdEJgMtGKonMXXcwLUI-sV8DamHqIKQDyDo1meptna2yeAYJoRHDPgNqi_udTTIvI1boIrjbXyGbv5pX0z6o7jVNHYZZ6voZz1FSVWzJIln4h_A5_l4rZoXbI5iUjWYliM2w8ktQ7lhBsWLdnYxu9JjRqeJzOfP_8jf74O9yaFaFJupJ6ZBkYXj1jZV43mBYKCSgp9iLJ-bICcjU6t60GVWWam4G8x7XxTdfjkOjpCo6C9uRIW64bcYnVJnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6580b7d6.mp4?token=ZxmLYviAANCn8PepTLPW48BikyK7YWuDsK45I9T_Ro2CD0hYW8-ClQxs4EjtE2gK3wt_inGMZ6o9rZIhLaR-XuxDPKdEJgMtGKonMXXcwLUI-sV8DamHqIKQDyDo1meptna2yeAYJoRHDPgNqi_udTTIvI1boIrjbXyGbv5pX0z6o7jVNHYZZ6voZz1FSVWzJIln4h_A5_l4rZoXbI5iUjWYliM2w8ktQ7lhBsWLdnYxu9JjRqeJzOfP_8jf74O9yaFaFJupJ6ZBkYXj1jZV43mBYKCSgp9iLJ-bICcjU6t60GVWWam4G8x7XxTdfjkOjpCo6C9uRIW64bcYnVJnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا سیما: در تفاهم جدید آمریکا پذیرفته که نظارت بر تنگه هرمز با ایران باشد
‏
🔴
هنوز ساز و کار نحوه رفت و آمد کشتی‌ها مشخص نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140224" target="_blank">📅 16:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140223">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b89f92fb.mp4?token=WSk1IMDw7Gte7wSvJfLCAtVrmr6WU9eMA4JRS2f4ZXO4_IzWWgr2SW-xjxmGM0bY7X7kmGAYqxpFmNeeUc75w6YLuI-6GCCYwo79JffzD40eFzNcyjirtQLsoW3OadE_Ct7uZ_Ti-_qwgeFpNvHZuxvFV7a9Ad3fQxeK8e6Gn58BFhbON6ZhqqGhi5ygwkqXaYQcUNqTHRRRQOesyJg1BE-e66J8BXuI2d5fDj3gT31dvqyARb1WjeOq1y3IHHSCu-I8XZYJ-EiqKvPr4tiSuoc_LybnO2wJJUoAUsPjKeZHVXBv_bcGXxkOHFk6dSs7UziQPEgg6c6f01BzvgUL2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b89f92fb.mp4?token=WSk1IMDw7Gte7wSvJfLCAtVrmr6WU9eMA4JRS2f4ZXO4_IzWWgr2SW-xjxmGM0bY7X7kmGAYqxpFmNeeUc75w6YLuI-6GCCYwo79JffzD40eFzNcyjirtQLsoW3OadE_Ct7uZ_Ti-_qwgeFpNvHZuxvFV7a9Ad3fQxeK8e6Gn58BFhbON6ZhqqGhi5ygwkqXaYQcUNqTHRRRQOesyJg1BE-e66J8BXuI2d5fDj3gT31dvqyARb1WjeOq1y3IHHSCu-I8XZYJ-EiqKvPr4tiSuoc_LybnO2wJJUoAUsPjKeZHVXBv_bcGXxkOHFk6dSs7UziQPEgg6c6f01BzvgUL2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت موشک‌های نیروهای یمنی به اردوگاه‌های نیروهای تحت حمایت عربستان در حضرموت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140223" target="_blank">📅 16:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140222">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
اکانت رسمی کاخ سفید: کومونیسم بزرگترین تهدید برای آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140222" target="_blank">📅 16:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140221">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پلیس سوئد دو تبعه خارجی را در منطقه لوون، واقع در غرب استکهلم، دستگیر کرد. این افراد به اتهام پرواز با پهپاد بر فراز یک منطقه حفاظت‌شده دستگیر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140221" target="_blank">📅 16:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140220">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_soNkp_dKtN2P581VNOV28nj7vv8sypMKST4P_jUCZWU6BQ1Hdo1NafI4zd6IAzz2-kQaABmggehMTirGzCUfRKbxsNqFdQFUB1w1XvU66gqi2Ud-74gUQOCRVu74mMy8valhTV9WrD9TrLT68hfT0lCxX_wRB9sypdsjimFPk-_wXQsqgCSAutyfQB1Inu_beFKySf2nlLEwLqfkzhOBJqdJ2_yXqHRqGVHnbxj0qGlci3Fk_OykDnJmOj0gNBqKn1bYzUKFGkKEolVFid5xKWNp0Kpgi31TTqjxKxLc1eUFXf35th-WNz4JPDMaKtpEXuNTtN3-ZzX9VMKrBblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران به کشورهای خلیج فارس هشدار داد که مگر اینکه از رئیس‌جمهور ترامپ بخواهند حملات برنامه‌ریزی‌شده آمریکا را لغو کرده و به مذاکره روی آورند، زیرساخت‌های نفتی، برق و آب را هدف قرار خواهد داد؛ محمد بن سلمان، ولیعهد عربستان سعودی، از ترامپ خواست اقدام نظامی را به تعویق انداخته و به دنبال دیپلماسی باشد. گزارش‌های رویترز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140220" target="_blank">📅 16:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140219">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رویترز به نقل از منابع آگاه: هنوز جزئیاتی در مورد چگونگی تعریف «کنترل» بر تنگه هرمز، تعیین نشده
🔴
ایران به دنبال دریافت عوارضی بین ۵ تا ۷ درصد از ارزش محموله‌ها کشتی‌ها است، عمان در حال مذاکره بر سر عوارضی در حدود ۳ درصد است، در حالی که واشنگتن هیچ هزینه‌ای را نمی‌خواهد
🔴
مسائل مهمی حل نشده باقی مانده
🔴
توافق پیشنهادی کنترل کشتی‌های ورودی به خلیج فارس را به تهران می‌دهد، این یکی از بزرگ‌ترین امتیازات اعطا شده به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140219" target="_blank">📅 16:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140218">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_Hapjlnzs5hlK2ZQm0gFQwHBQA2P2IEKsHYXhnM4DiaENLisTd-nVUAswD95WMFap1q6OE9wuhJ06idqVYZc_dQMxIsXrBtB1p9YHjPX9vZxN7TNs6YgLnQinrRUtSNC2mmTFy2nPkhDjCrp9QkH93i_Y8d1JRVV_nKNfecK35V-5kUBqdMdcD2nTdL6-YdLmnMcagiV0zFUT-dApx7BXz4ZgWYtLWkUeqyukYu2k0cxAzavsXCOHIC-rid1TV8DQUrnv9NB9DGBlK5pwMANG5Eyh_M0-7-OQC1qVHL2NZPqKT0WNoGr_cCQb6UWXFANNzCOWMoU2GG6ph_w2AtZAuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47221b6a95.mp4?token=qO8gxhP222Zv_2FXO0s28MsfpZJdkxqDM4v3vWSmi1E_gJlFqdoGJkhkl1Rb0_15u8GOgaxLja75S6h2bX2tX0wDpx3MLRtqw81nLQcCVepzEW0NNKjfh687TX9t6Tylo90-M0J6B0rMpONUKtMhgHO1P_bw-RJMMFp0itdm97-zOXyb4y4A7YqEYdFvGzkvqSbsNCLaEb80Dx2-7qaebYXPy2GThhpbQuJ75SIidTS7FJnbAnQGm4KPM7sHzGST3l6RhM2VqVWdaEinlHWrqmdWgfKMqCnqd4BU0BoGa284TMlfACf56ciUYnduWxrfdimNJRQS_X8K0NNfut7L_Hapjlnzs5hlK2ZQm0gFQwHBQA2P2IEKsHYXhnM4DiaENLisTd-nVUAswD95WMFap1q6OE9wuhJ06idqVYZc_dQMxIsXrBtB1p9YHjPX9vZxN7TNs6YgLnQinrRUtSNC2mmTFy2nPkhDjCrp9QkH93i_Y8d1JRVV_nKNfecK35V-5kUBqdMdcD2nTdL6-YdLmnMcagiV0zFUT-dApx7BXz4ZgWYtLWkUeqyukYu2k0cxAzavsXCOHIC-rid1TV8DQUrnv9NB9DGBlK5pwMANG5Eyh_M0-7-OQC1qVHL2NZPqKT0WNoGr_cCQb6UWXFANNzCOWMoU2GG6ph_w2AtZAuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل در پاسخ به حمله بمب کنار جاده‌ای در مجدل زون که منجر به کشته شدن دو سرباز وظیفه و زخمی شدن چهار نفر شد، به اهداف حزب‌الله در سراسر جنوب لبنان حمله کرد. اهداف شامل انبارهای سلاح، مراکز فرماندهی و زیرساخت‌ها بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140218" target="_blank">📅 16:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7Hqs8v4kygozklrv-1MpRkl0_dkJdtiTNCBlepVfinsaEs7eyLB7PAeWM5HwsTlMGX_slcfH3-f3D3nF6kGV01U6qHXn4w4KSNlgOZBkoobNxfrSji-T87V1O7sPixKTPt_wUFvC_ROBWNoQhd7rU74z3atONBa7aPWy2iiTOzU_KgNOccaeXCMHNsinTpnT7REwvJrLnBUZzn6_meGJyjySLsEEs_fxs93Dwo6vtowY0R1NHteuzrHuwU8HPSP3qwaR8w3H3A-JZmqELaGw52EE1SsUMGmztCvYp9UDPGoKXLqK5QIpQoxleGrek6cU7DG2II4N1KLUiXkihnYGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/em-UsJrzPSyfDcjEndda6QI_zF2wJ72z7K-Xb_y93wkjrJq34oT3mNyLg-XES8y4ntMq9CMJXRR51O3HsJAFY2RhDJ1K0hNLKuOPvqisVxVQOyrjYT4je-tS05-A7eaLF-FUroVsKh2R0KHbTQ_xoItKTkiE0OYS5CV0qzenvqfStrOHBpgNSWpcrLMC0ltIIEiHHsrSm-so24G4Njt9Mw_WaAP1-wmRhtVjUDaEHzw4ZE4NxeCLq0k5oDkfny0k0goKn3BV6XGWWVo-G_OtD1_r-nB2HaSfinyEWvw2RDnoVDEmnsFoqpsTfASiDJ6sbob1IaXh5ls8GWrmMyIgQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروهای یمنی، یک پایگاه نظامی متعلق به نیروهای "دفاع وطن" که به عربستان سعودی وفادار هستند، در منطقه "الودعیه" را مورد هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140216" target="_blank">📅 16:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140215">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMfrKqH-Iu2OkG-Cnii0ixx3ti07wjR-5mLLDJ5hBcXqQT8LDXEJA-c5RUPclcWh4tyH8MJDRTMbD8wxevmy60hWwpkZshIckKCBbOnWfTpI05c9E243cDLqhEh280IDcqPh7xfxppUv99TarVnaVywvDTbjh0i_slRpxf36lgPFPLgYLaZoyi0k_MqtfT2APxvoL5Nv49w5Wisd1Mi-9ZEW0LglrXRldiIK2LKym6PIp5yBwtWSZXef3YXYdGne9mrtvMVUYI-3q5oe2ouDypn2vJy5ZU2sdyZvfQvE4JAkrE9hDjhh0ZPSE60ZrPKtEt7GYARcoQ-CEx4QEVRbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از حملات هوایی اسرائیل، شلیک توپخانه اکنون به منطقه المنصوریه در جنوب لبنان هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140215" target="_blank">📅 15:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140214">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نیروی هوایی آمریکا در پی نزدیک شدن توافق بین ایران و آمریکا، شروع به خارج کردن سوخت‌رسان هایش از فرودگاه بن گوریون اسرائیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140214" target="_blank">📅 15:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140213">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
به ادعای یک منبع در وزارت آموزش کویت، مقام‌های کویتی دستور تعطیلی تنها مدرسه ایرانی این کشور را صادر کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140213" target="_blank">📅 15:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140212">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
زلنسکی: توسعه سیستم دفاع موشکی بومی ما وظیفه‌ای است که تاکنون تنها توسط تعداد اندکی از کشورهای جهان با موفقیت انجام شده است. اوکراین این توانایی را دارد.
🔴
ما می‌توانیم با اطمینان بگوییم که سازندگان سلاح ما بالفعل به سطح مورد نیاز رسیده‌اند. انتظار داریم که تا سال‌های ۲۰۲۶ تا ۲۰۲۷، اوکراین به نتایج لازم دست یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140212" target="_blank">📅 15:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140211">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad0eb3047f.mp4?token=M8qm9IBDk9YjJWgPKeA9Arzh45njCWG7vOR1MfR-kahsbkkwgX8grqrwoeh4ZNRmTg9g3kyvgJxygwpT5RueptIxUuXP1YMQGGZU1QMhcNxZvmvRs-wqCY4ANigUpLu2qCRSnqJeF3Y-q5mt-A3n6WoeB8IbX7QGfKdbs84i-FYt8F-7QlUVAeZPZ1k4v_z58ViWniVAps2F0LWcydRqOtl8kq7-Ns2gAuCQcKK59tM92HW8hCW0A6_7Zkengr3jzZJ1ZNwjhsoIsojRYCuEw9NWYlEp-t1mbKCItJ5aqF0h0lFbKkPqFbAP7oF_9aCWvek-ebr_x7-bkq5ugpNNlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad0eb3047f.mp4?token=M8qm9IBDk9YjJWgPKeA9Arzh45njCWG7vOR1MfR-kahsbkkwgX8grqrwoeh4ZNRmTg9g3kyvgJxygwpT5RueptIxUuXP1YMQGGZU1QMhcNxZvmvRs-wqCY4ANigUpLu2qCRSnqJeF3Y-q5mt-A3n6WoeB8IbX7QGfKdbs84i-FYt8F-7QlUVAeZPZ1k4v_z58ViWniVAps2F0LWcydRqOtl8kq7-Ns2gAuCQcKK59tM92HW8hCW0A6_7Zkengr3jzZJ1ZNwjhsoIsojRYCuEw9NWYlEp-t1mbKCItJ5aqF0h0lFbKkPqFbAP7oF_9aCWvek-ebr_x7-bkq5ugpNNlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
پالایشگاه بزرگ نفت روسیه هدف حمله قرار گرفت
‏
🔴
در پی حمله چندین پهپاد اوکراینی، پالایشگاه نفت یاروسلاول روسیه دچار انفجار و آتش‌سوزی شد.
‏
🔴
این پالایشگاه، یکی از ۵ پالایشگاه بزرگ روسیه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/140211" target="_blank">📅 15:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140209">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=cSO3e-MkaVoXvoKgn3dsrlYj42Ho2AI7flzWUNIL-jgjuoFypAB-84G2ht8Me1JxfcWSMiNQ2I0PkhSeAzGFpYsDYwzVJP6KY92yDI7nwnG_4mUceAicElBVZV1oD46BV6JJ9VkIM7-BCFaf7MXr6lJ_adPaAGXBoee_dnJ-FOxgYGlIMuYHNt1EDDXPxu792rSOanEdP0IciUfDIb9lOVtmFbjfal9THjJ7pYlC8j-LbhB_CSs2sGXox5LfCOHwNl5RjSLgUUAxx3yHG3acGjX53MQMRVzUH8ohHBKat55-CNYAW-DVxkfj6LbELufBCE0rmQsxFunH_zDkIfSz2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761165b2c7.mp4?token=cSO3e-MkaVoXvoKgn3dsrlYj42Ho2AI7flzWUNIL-jgjuoFypAB-84G2ht8Me1JxfcWSMiNQ2I0PkhSeAzGFpYsDYwzVJP6KY92yDI7nwnG_4mUceAicElBVZV1oD46BV6JJ9VkIM7-BCFaf7MXr6lJ_adPaAGXBoee_dnJ-FOxgYGlIMuYHNt1EDDXPxu792rSOanEdP0IciUfDIb9lOVtmFbjfal9THjJ7pYlC8j-LbhB_CSs2sGXox5LfCOHwNl5RjSLgUUAxx3yHG3acGjX53MQMRVzUH8ohHBKat55-CNYAW-DVxkfj6LbELufBCE0rmQsxFunH_zDkIfSz2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منابع خبری از کشته شدن ۴۵ نفر از نیروهای وفادار به عربستان سعودی به عنوان آمار اولیه تلفات حمله موشکی و پهپادی یک گروه یمنی به پایگاه‌های نظامی در حضرموت و مأرب خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140209" target="_blank">📅 15:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140208">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
الحدث به نقل از منابع آگاه: بیانیه‌ای مشترک از سوی عمان و ایران به‌زودی منتشر خواهد شد که از ایجاد یک گذرگاه موقت در تنگه هرمز خبر می‌دهد؛ این گذرگاه تا زمان نهایی شدن ترتیبات مربوط به عبور دائمی مورد استفاده قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140208" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140207">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8c5c0f143.mp4?token=R__fpo1az5zNDKh6wGTWH-YoNEv_GyuuXuHFTbuyLPpu9xFbMDqDbwwUVypiBk9gfSkHHxhkMwLswax8XN7yTFGecPwxuTci1soUKNrqSakYkqHF8bd5WIj1fqdiXfXaYTB_jDrLAlU4vwW4CPAMC-_7fsEi0MceSJn2Y2pzzrpLrroEY3IFyK9KMyYNS6MGD6kJFF4iW_OySUziHupGj4otlcMsNpkZO83zgTkrocs8eTimVG6cwHaZUMKa3qw6tiUWgZw5gyjqDVGV_Hmlz92fWJEgqQ8wtiC0QxxbKmLZ_srfZh5iGV9XtqatOWXUyjNkJ1YcKBGTiG4m78Ez-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8c5c0f143.mp4?token=R__fpo1az5zNDKh6wGTWH-YoNEv_GyuuXuHFTbuyLPpu9xFbMDqDbwwUVypiBk9gfSkHHxhkMwLswax8XN7yTFGecPwxuTci1soUKNrqSakYkqHF8bd5WIj1fqdiXfXaYTB_jDrLAlU4vwW4CPAMC-_7fsEi0MceSJn2Y2pzzrpLrroEY3IFyK9KMyYNS6MGD6kJFF4iW_OySUziHupGj4otlcMsNpkZO83zgTkrocs8eTimVG6cwHaZUMKa3qw6tiUWgZw5gyjqDVGV_Hmlz92fWJEgqQ8wtiC0QxxbKmLZ_srfZh5iGV9XtqatOWXUyjNkJ1YcKBGTiG4m78Ez-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در منطقه المانصوری، در جنوب لبنان، عملیات تخریب گسترده‌ای را انجام می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140207" target="_blank">📅 15:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140206">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه: در مورد مسائل فراتر از تنگه هرمز، به‌ویژه در مسئله هسته‌ای، توافقات اصولی مشخصی میان ایران و آمریکا حاصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140206" target="_blank">📅 15:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140205">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSywSfbokS5XdO-EgTf0aBB74qNsav_I7o9m8O1ALSae-id-h6q9bZCqI_7h6VgR2_uLHDx8XiMmNTB5qs7XAsbdzwq1N8Znxv4CCs1QEbYw_VYYQPgBcKxtDcS1hcktOijjWhnbfw48XXKaXKpf9VzQPPrBMD3zRkuG-1JC98d0zR1Q-M7Fo9ny7x3zA3Fz9LEb4AZ1crpLwo7DEzRsxR35wPEON56nuApdispZpR_r43mBB-WrERxlaJHIi6-ffPfIIzuxxajAYgWk7OiR_3EDz4ysXRs2z5RbSkQATamh7Yc7ewkknobJghEHGfIWA-zmTCl-LrUWxhy1kOnZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدودف، معاون رئیس شورای امنیت روسیه: چه ننگ‌آوری که در یادآوری بمباران هسته‌ای هیروشیما و ناگازاکی اخیراً، نه یک بار هم نخست‌وزیر ژاپن یا هیچ مقام ژاپنی دیگری به این نکته اشاره نکردند که چه کسی این کار را انجام داد.
🔴
ژاپن یک کشور تحت سلطه ایالات متحده است و در نهایت، به یک کشور بی‌ارتباط با هیچ قدرت دیگری تبدیل خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140205" target="_blank">📅 15:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140204">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNCdVZPwTBXkajljDs0-_i1Snq3Ee7lr6z7v1KMuZbVo7dWADq44lUS26xP9dem-y625T4Un0XqW7-nNtd9kn9ly10w4iB6f-6HcaXexzmnQyh0rb2BC-9FE_VS8-TKgTT-NBnp5NhtT5wvlPgI3PIgDivTs_nwFHL3_1BrpQHNvxx980APX3BDV6yCrhvwK2shvW_rAN23L41mCMgxoQLyrSVg_agPWARvW7gKMcBIUsVD-ssAlHAGSZn3eGY9vmXy-zjATuT1sRv4s0zsJlVoHXdn_jCEFz-51GRzgHi_TdPxW2KYKX0qbV9-r5iW8_rT7v84wx7vGeMZUNYHzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه پیشین هند :
توانمندی‌های نظامی ایران واقعاً شگفت‌انگیز است
🔴
او از توان نظامی چشمگیر و تاب‌آوری ایران که در طول دهه‌ها تحریم و هزاران حمله آمریکا و اسرائیل شکل گرفته، تمجید می‌کند و می گوید
🔴
ایران از آن دسته توانمندی‌های نظامی برخوردار است که بیشتر کشورهای جنوب جهانی اساساً در اختیار ندارند. آن‌ها چگونه توانسته‌اند به چنین سطحی از توانایی دست پیدا کنند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140204" target="_blank">📅 15:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140203">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آنکارا: امیدواریم تنگه هرمز به زودی بازگشایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140203" target="_blank">📅 15:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140202">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ea3ead7d.mp4?token=jJBqJZkcOLYw8JJNOMvMd4tqoiyT_Ca_n5QS6r5HHMuknvYEuLWLKkp9CmZvxJypWy_x_mU8ibCxqDQuEUYRKdwyDc3JilwK-kwkzlPbml_yR_mKWQ9ZYG__4ud6Ukv_yZ3tXwlmxxfw3pyY4VfCdQP40cf-Zm3dbgZZLZKSx-UD_6zNf-vAmM2KJrZCWa4j5gONJjAiDvgwzKdtmJYR5WZn0E9oo_Ws475JNCMlkWFqURjC3mq-vL64F5ZSNbo0H2JGPkG-47giPX0mPOykw_XBtGvZQRr0vIeqYyB6oDap7oaTUmR71JBmQ6vOxwA78C9dDDHagwhNi6sYwdooxKra-W9XgUwhETI5WGWtl5Vg86Ig3swoLoOEr9xaveVtI5PpkcmXjIJMSa8MiPcH0b2pnpmO449V1MRwhsn_vQH3KFIogSHeII-Dq-R2mGu5ZvRVXe0EU7ekxWhxPc-VGAmxs6HgNKQj6KKGyn2W1faQOVU_YcQ7NU3Dk472nEZ3Yrs1E1kO1-xelnSUzhY-u2njYJFfo7RcT-LlmlN97rG2J6Vgs8Dw8grbcVyuXCyV0kEkQSNCnx8xr7dL7hMnToOEiH3iRW_wDmCJlXazPoYF4Hsd9BNmc9ZxM2QHPaDJXc-MGucZ7j3iLFsEs6wYp3zMASbI3pSm2EGninnZ0jM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ea3ead7d.mp4?token=jJBqJZkcOLYw8JJNOMvMd4tqoiyT_Ca_n5QS6r5HHMuknvYEuLWLKkp9CmZvxJypWy_x_mU8ibCxqDQuEUYRKdwyDc3JilwK-kwkzlPbml_yR_mKWQ9ZYG__4ud6Ukv_yZ3tXwlmxxfw3pyY4VfCdQP40cf-Zm3dbgZZLZKSx-UD_6zNf-vAmM2KJrZCWa4j5gONJjAiDvgwzKdtmJYR5WZn0E9oo_Ws475JNCMlkWFqURjC3mq-vL64F5ZSNbo0H2JGPkG-47giPX0mPOykw_XBtGvZQRr0vIeqYyB6oDap7oaTUmR71JBmQ6vOxwA78C9dDDHagwhNi6sYwdooxKra-W9XgUwhETI5WGWtl5Vg86Ig3swoLoOEr9xaveVtI5PpkcmXjIJMSa8MiPcH0b2pnpmO449V1MRwhsn_vQH3KFIogSHeII-Dq-R2mGu5ZvRVXe0EU7ekxWhxPc-VGAmxs6HgNKQj6KKGyn2W1faQOVU_YcQ7NU3Dk472nEZ3Yrs1E1kO1-xelnSUzhY-u2njYJFfo7RcT-LlmlN97rG2J6Vgs8Dw8grbcVyuXCyV0kEkQSNCnx8xr7dL7hMnToOEiH3iRW_wDmCJlXazPoYF4Hsd9BNmc9ZxM2QHPaDJXc-MGucZ7j3iLFsEs6wYp3zMASbI3pSm2EGninnZ0jM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنی سندرز، سناتور مستقل آمریکا : باید جلوی جنگ‌های بی‌پایان رو بگیریم
🔴
باید به هزینه‌های بیش از حد نظامی پایان بدیم
🔴
باید حمایت مالی از دولت افراطی اسرائیل، که به گفته او علیه فلسطینی‌ها جنایت مرتکب شده، متوقف بشه
🔴
باید این روند رو تموم کنیم و به‌جاش روی مردم خودمون، مثل مسکن، آموزش و خدمات درمانی، سرمایه‌گذاری کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140202" target="_blank">📅 15:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140201">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
برنی سندرز، سناتور مستقل آمریکا : وقتی بچه بودم، مبارزه ما علیه جنگ ویتنام بود
🔴
جنگی که ۵۹ هزار آمریکایی رو کشت و خیلی‌های دیگه هم بعد از برگشتن به کشور، بی‌خانمان شدند
🔴
اون جنگ بر پایه یک دروغ بود
🔴
جنگ عراق هم که زمان حضورم در کنگره بهش رأی منفی دادم، بر اساس یک دروغ بود
🔴
حالا هم جنگ با ایران و این ادعا که "ایران فردا سلاح هسته‌ای می‌سازه و به آمریکا حمله می‌کنه"، به نظر من بر پایه یک دروغه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140201" target="_blank">📅 15:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140200">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الجزیره: لبنان در مذاکرات رم، خواستار خروج اسرائیل از حدود ۶۰ شهر و روستایی است که از ماه مارس اشغال شده‌اند و توقف حملات هوایی را نیز مطالبه می‌کند
🔴
دو طرف با ایجاد یک «منطقه آزمایشی» برای خروج نیروهای اسرائیلی از سه روستا موافقت کرده‌اند
🔴
یکی از مهم‌ترین نقاط اختلاف، تپه «علی‌الطاهر» است که اسرائیل مدعی شده مرکز زیرزمینی حزب‌الله در آن قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140200" target="_blank">📅 14:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140199">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f16afca4.mp4?token=hAgzdab7HS_B8auaN8GGzoOQcFCaUH0HULY65acXYQPd4mEWSC1S2Il5jglp1gEOluQ-Sw63GueOZlcwN3aPoiqL3xxNJRnudL2fbcTzND2DFF8HpZop4GFUt_9iMnBl8rhxXovZGIkMUbitEX2EuBhumzaSdyuKUaKWHEwNy4srnWUEU-fpd4kFKSwKqOgJ5YE-0IiVckOZCVYoEa-MPfiqlkIMUJPv86xtgBK4c0StSTcnVZnH9QImFKvEnkOTqThDWDibe7ylJdj7EVLXonvhueh-cT8ppA1AK68vC7Ct9ZoqRrzCtcjyJjryl6wiwfHE3iNkA1B2JPwpwkUFgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f16afca4.mp4?token=hAgzdab7HS_B8auaN8GGzoOQcFCaUH0HULY65acXYQPd4mEWSC1S2Il5jglp1gEOluQ-Sw63GueOZlcwN3aPoiqL3xxNJRnudL2fbcTzND2DFF8HpZop4GFUt_9iMnBl8rhxXovZGIkMUbitEX2EuBhumzaSdyuKUaKWHEwNy4srnWUEU-fpd4kFKSwKqOgJ5YE-0IiVckOZCVYoEa-MPfiqlkIMUJPv86xtgBK4c0StSTcnVZnH9QImFKvEnkOTqThDWDibe7ylJdj7EVLXonvhueh-cT8ppA1AK68vC7Ct9ZoqRrzCtcjyJjryl6wiwfHE3iNkA1B2JPwpwkUFgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:ما بچه که بودیم پنکه نداشتیم
مجری: آخه آذربایجان خنکه
🔴
پزشکیان: من تو زابل خدمت میکردم
مجری: آخه شما میگی وقتی بچه بودم
🔴
پزشکیان: من تو زابل خدمت میکردم و پنکه‌ام نداشتم، حالا چی میگی؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140199" target="_blank">📅 14:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140197">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruYNaxlmogd7sBMwrj_J_xbTIu3eb8P-4GbFzd7gdei_unndSq65k8uktlpa7bc5Hrh_JY6IUGk2_e4IpPtT6mR6G6ueZmm3bb4JUjrrYiiuDdGHMX9_EB3Q0ItCcUvCRvjjDCjySzQjdqgDnrN4LaEnXMkpoF9LAJjn3E_Z7nK02jHZfbI5O5-G-yf4g1qsx00va9LJUDbeiOeGJzcu_2gi7AKO6pBF2l-pntGnCbgWlpz8YZcMH_F_TVULyVqkjj606o8G7EcddRx_Dk08kTPOtx9IKmOIskH4PsGCQeDifQHDz7ajQjNnXrqlIKJMMMppl5GQtwFCoIA6lo3pyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3ND4yzhPPXG5Uys8YZevMvEnH0ZJH60xYqA1PledRfmssyVUUuWp2I1CuFl_H_Il0avIQZK_Twwxgavg7-WMTKSkRUYxR9-CYYIZ8Bn8BvH-GnRW7kz8OzjGc-LwLobNowVfxlNIR7fqkLBoRDLkV0IeEO6RkyzJqsRxejkm573sZlvJ3hvOnzTSDQkPIgmxqMSxyzfke6x-zCsGhALq2wFyxp94NaOMZFtOD3NSfpJSxDGFXzakVN6e4Mn7oDADF5q1JtoMPRF_6gDIPaNau5-BIPc0zSHvuuPfsuxDGi-je0kp-OHDTcH6pTK0yeTipQqyNQ2fUVbULYYqVu3Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل (IDF) رسماً اعلام کرد که دو سرباز ذخیره اسرائیلی در جریان انفجار یک بمب دست‌ساز در یک ساختمان مین‌گذاری‌شده در منطقه مجدل زون، در جنوب لبنان، دیروز کشته شدند و چهار نفر دیگر به شدت مجروح شدند.
🔴
افراد کشته‌شده به عنوان سرهنگ (بازنشسته) هارل بیرن‌استوک، 34 ساله، فرمانده یک گروه، و سروان (بازنشسته) تمیر واکنین، 33 ساله، شناسایی شدند.
🔴
این اولین تلفات نظامی اسرائیل از زمان برقراری آتش‌بس در ماه ژوئن با حزب‌الله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140197" target="_blank">📅 14:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140196">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
واشنگتن پست: ترامپ در یک جلسه خصوصی با  حامیان مالی خود، گفته است که باید در نهایت جی دی ونس را انتخاب کنیم.
🔴
این بدان معنی است که با احتمال زیاد جی دی ونس نامزد جمهوری خواهان در انتخابات ریاست جمهوری ۲۰۲۸ آمریکا خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/140196" target="_blank">📅 14:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140195">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb122a804.mp4?token=LCcxZItRWqOB_KHlam0SUaR2gGp6hy786CPyYkVBPxQg9V-rDuBWpMjz8IVXsJpyzxZsrXYfyhl1j1KN4PvMEpt1r2yVJGattLPgpDxobWqYLzcXSjsGF1-BQHQjDEW4Ev4jaG13PTMYcywhhDwqgVRBz_T4c2goYuL4oFfalMwSWqqb6LVMpp-DEMisEUu8DnRo0NLejB34VIhGxDNZrHuapDZJBz-kOPDlc9nAKCTlsLav1QieYzTgzWQegw3Dl39nRFDhGQFiSfjzJOpfGQUJiygCOcXNVmJT--lo6a-ukmRTxk6PLe8wyahWyf_gz9qX9bhN6K5-bm4uRYy3xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb122a804.mp4?token=LCcxZItRWqOB_KHlam0SUaR2gGp6hy786CPyYkVBPxQg9V-rDuBWpMjz8IVXsJpyzxZsrXYfyhl1j1KN4PvMEpt1r2yVJGattLPgpDxobWqYLzcXSjsGF1-BQHQjDEW4Ev4jaG13PTMYcywhhDwqgVRBz_T4c2goYuL4oFfalMwSWqqb6LVMpp-DEMisEUu8DnRo0NLejB34VIhGxDNZrHuapDZJBz-kOPDlc9nAKCTlsLav1QieYzTgzWQegw3Dl39nRFDhGQFiSfjzJOpfGQUJiygCOcXNVmJT--lo6a-ukmRTxk6PLe8wyahWyf_gz9qX9bhN6K5-bm4uRYy3xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، جمهوری خواه و رئیس مجلس نمایندگان آمریکا: ما در این انتخابات پیروز خواهیم شد، چه وضعیت ایران را قبل از انتخابات حل کنیم و چه نکنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/140195" target="_blank">📅 14:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140194">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
خبرگزاری قوه قضاییه ادعای نماینده مجلس درباره چگونگی رد زنی محل استقرار علی لاریجانی را تکذیب کرد/در خصوص ترور دبیر شورای عالی امنیت ملی، پرونده تشکیل شده و درحال بررسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/140194" target="_blank">📅 14:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140193">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb15b8b182.mp4?token=rgeePbcNL9bd32614MoqC_-3pKEuKYMTH71G89HyEInQoOI9HT3G651QVSJkP8MWXhvC_5T4_LY27eDoElBYPkfx_QElHI3y1dHO1n8kb1ONHbUWPw4CLd87QSZN_m1kO54Xl6jNtkUZLpAWZIaWI2SRpPbRpVrYywU_1m5ma9hdQga6KY6pcAoANudcPgs4kqlDIPG9X7Uu78dBqL0_X4oZj_yNTceqdLAN0MIxucdenaaNjoJ7WzmrMl8fBVW1IfNYEcJlaVyKaC8SQoFxNk79FPdg8DfhfFqO1-a5kZG8I9KivfChzgMHGT-iz7ckJXBt7KocH1Xr-7-g6GYkbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb15b8b182.mp4?token=rgeePbcNL9bd32614MoqC_-3pKEuKYMTH71G89HyEInQoOI9HT3G651QVSJkP8MWXhvC_5T4_LY27eDoElBYPkfx_QElHI3y1dHO1n8kb1ONHbUWPw4CLd87QSZN_m1kO54Xl6jNtkUZLpAWZIaWI2SRpPbRpVrYywU_1m5ma9hdQga6KY6pcAoANudcPgs4kqlDIPG9X7Uu78dBqL0_X4oZj_yNTceqdLAN0MIxucdenaaNjoJ7WzmrMl8fBVW1IfNYEcJlaVyKaC8SQoFxNk79FPdg8DfhfFqO1-a5kZG8I9KivfChzgMHGT-iz7ckJXBt7KocH1Xr-7-g6GYkbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه همچنان چندین ایستگاه قطار اوکراین رو با پهپاد میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/140193" target="_blank">📅 14:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140192">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0QctPWJJHfu0tZvNZbyja-F4a1gE_FQleGUQcAQVwpboTc5Y_xNPWgIvbOLARkep65GA8G1mMPxcIpcwJ6sreEZ1O5o5S53uNvDNBCMZhy8A2NcvCZnD4hyGQ17CDTtiQLv64zXbXecBYNDjLErtLWhFU9a6Z8J0_uZdvcrSZJe_np_tm3bTipMxUjJrU9pUJBCfxCqZxj0vdKVDeISaL_fNWzIqjr18UEd3kQ3d7T1mgpPvLoWNkQgnfXWMsLLYvZKcXoR0bN0DIolZHQxCYITn6vHR4h1EIR4evRhltdZ11ZeTS-qyLaWmKF5OJXiaBPsLPwjxrhw7xgMsmQcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی به پالایشگاه نفت "اسلاونهفت-یانو" در شهر یاوروسلاول، روسیه، حمله کردند. در پی این حملات، حداقل چهار محل اصابت در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140192" target="_blank">📅 14:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140191">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه درباره مذاکرات ایران و آمریکا: انشاالله مذاکرات ایران و آمریکا امروز با خبرهای خوبی به پایان خواهد رسید.
🔴
صادقانه بگویم، موضوع [تنگه/هرمز] دارای پیچیدگی هایی است. البته جزئیات فنی آن - عمان نیز نقشی را که باید در مورد نقشه ایفا کند، دارد.
🔴
با چه مکانیسم و ​​روشی و برای چه مدتی این [گذر] باز می ماند؟ البته روی این موضوع کار می شود.
🔴
مهم این است که توافق در مورد دوره انتقالی حاصل شود. نفت باید به جریان خود ادامه دهد تا قیمت جهانی نفت و قیمت انرژی افزایش نیابد. و ثانیاً، به طوری که این فرآیندی را ایجاد می کند که امکان یک توافق پایدار را فراهم می کند.
🔴
بنابراین یک دوره 60 روزه در حال بحث است. اگر در آن دوره 60 روزه به نتیجه برسد، می توان به توافق دائمی بین طرفین رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140191" target="_blank">📅 14:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUDtcYTIaIyT4hSYtxf1uAhdIWkJNqvDMf6TjAuJkn7kvoXhsQ9tmoLkmAtF25aY0LodrhBabOI5ucfh6lBrAEWMcoQ8EYFXckzDn54Vr1Zh2_vmoLe36j3eljQmC84qyCokWc195uWybyq1Av1snlGStdfeYUST6l_jXocYeUvW2iW7zjJOg--aQzSOcCoFTmSOXRKyw2YzLjJoYe_IZZRjcXTNH-mnmWT1IGEvPlcBo7-wwQFQXcv7rkJhriwUWcF6rt4Yvsiq6-1jR3q6Z2QTfgqxTyMB8WvNtcRgf9xXnQyVprtYWPJou5PHQJ9kHLa9DwzpaBGCj_KsKtHu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است
‏
🔴
این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/140190" target="_blank">📅 13:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140189">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0700f7505f.mp4?token=ps9dMUUUzfyfvVEnuIXdU8XIsgeVEBbkPKivXu952PnognNUUqxseD_Nziolkx0_4HHX3wDnvPw-Y2vkLbkY2LcxLG8b6RJMAgHqIYgiV49Fk1YMpSwOwYijL4JYc-JOSOKoGcW7n7QhHAbUqtMZQYJLesSXbaDsJcsCUxej1xj5Ky2w6G5mCHURuN0CKibjhg0SeExZriSvsiL2DhGbRb8tnxbs41PMysVccGS7i_k9jBA5bfkw8zkSO2r6Ee2kiODI0aKDxLKhJw5_Pz3ACoj0sftzJnAsIbSfacmKcHrcSN9b_cCZeF_9iglAyLWuX3rQ6yhT91GQITLqiZyGgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0700f7505f.mp4?token=ps9dMUUUzfyfvVEnuIXdU8XIsgeVEBbkPKivXu952PnognNUUqxseD_Nziolkx0_4HHX3wDnvPw-Y2vkLbkY2LcxLG8b6RJMAgHqIYgiV49Fk1YMpSwOwYijL4JYc-JOSOKoGcW7n7QhHAbUqtMZQYJLesSXbaDsJcsCUxej1xj5Ky2w6G5mCHURuN0CKibjhg0SeExZriSvsiL2DhGbRb8tnxbs41PMysVccGS7i_k9jBA5bfkw8zkSO2r6Ee2kiODI0aKDxLKhJw5_Pz3ACoj0sftzJnAsIbSfacmKcHrcSN9b_cCZeF_9iglAyLWuX3rQ6yhT91GQITLqiZyGgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا هنوز باور دارید که نوعی تغییر رژیم در ایران ممکن است؟
🔴
مایک پمپئو وزیر خارجه اسبق آمریکا: صد در صد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140189" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140188">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
۸۱ سال پیش در چنین روزی ایالات متحده آمریکا با استفاده از سلاح اتمی به هیروشیما حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140188" target="_blank">📅 13:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140187">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=i0FS6JYGk3Gf6wgHGknSkYa_2iYdE80zaWCPppG0HIAug0OYiwqT76EKeAPEZNGk8rCIzD3UV4dLhP2PGWaudUAzimAe-8bZk0nPOa_HToBsIvxf-dX0_JxYiC6-REsMY10lUpB37BFpUMwu7z1a3A6fNS4uM8TI_Cd6oPuUpBcPKUFXNve0MLjh8DUqityc0h228E94wpCGuoqyTZOJ9o7jRVprV20ouJQRSxObzEKMg9onAH5x4PKU1PoAb5UglSfcWuY3B4WRIrZtvLWJCPJRJ66k2GAmuGaEy2TTMLeGBjmbRv06C_bpP_gDbPT-_iF8YzY3bni0LOUrUeIRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=i0FS6JYGk3Gf6wgHGknSkYa_2iYdE80zaWCPppG0HIAug0OYiwqT76EKeAPEZNGk8rCIzD3UV4dLhP2PGWaudUAzimAe-8bZk0nPOa_HToBsIvxf-dX0_JxYiC6-REsMY10lUpB37BFpUMwu7z1a3A6fNS4uM8TI_Cd6oPuUpBcPKUFXNve0MLjh8DUqityc0h228E94wpCGuoqyTZOJ9o7jRVprV20ouJQRSxObzEKMg9onAH5x4PKU1PoAb5UglSfcWuY3B4WRIrZtvLWJCPJRJ66k2GAmuGaEy2TTMLeGBjmbRv06C_bpP_gDbPT-_iF8YzY3bni0LOUrUeIRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / انصارالله یمن 8 فروند موشک بالستیک به سمت اردوگاه های لشکر یکم عربستان پرتاب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140187" target="_blank">📅 13:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=UwfKlT3yO_xcSmbT6MbPp2j_Lf4snrJ9xsvaiXt2MLwDvDbniebFiRqZS4NcuROXILdJgzldRbJQGlySvM8KMzYbqXnkKHq6jJOzEKVP7qs_O9uHoik2TlFpSmhSCRKwG43RR3iJvAMMc_nWabss1WOoqJIdTPjtwXqnKpKU90ZrQDO4zgc8-i_JmFpl5CAQ7cDb4cWMQEvMjXaa8vcZLANC-5HOBabZR032lEs6rB2VOwyNcav7lar4tvwTGZeeW6ZSBapSKrQrBwyW3lkUTGDq-wb3V5GDmMuYVzg62s0MjTQBGQCDYwaaYphnV1orpusRVuQsY5XmXDpBbZK4iACTVXBz_kooOEcVrlfovANnJB96le-mc0iUWIu6F7Yrad5K7tEOQ0hNvvpo0BeppgQBp1TkxWuT8yCOhwFGJ2bsTiBpTtREjWk34D0qRuaN2yLWsRcdia6OUKkBez6Pheh7-_e8ePeigeVyG7x1Ou7J2J5sBhQhxN8yMry-KOMpkdt7XWJoLZd_LokNEEgOrNSuejrqq1J3sssyZT2Jnb5Hxa_LsgN0eFzo5tPo9MCfD-H1C_o7XCpGA3AEsW9qules2crh_0lKKWZmZf6CeY9bAw2ptQwtlpCojV8QOcHQYsrOtYGWHCT4UCs6M4GmKGo5mj7QJ_Vc4oI0mz3X9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d7912f58.mp4?token=UwfKlT3yO_xcSmbT6MbPp2j_Lf4snrJ9xsvaiXt2MLwDvDbniebFiRqZS4NcuROXILdJgzldRbJQGlySvM8KMzYbqXnkKHq6jJOzEKVP7qs_O9uHoik2TlFpSmhSCRKwG43RR3iJvAMMc_nWabss1WOoqJIdTPjtwXqnKpKU90ZrQDO4zgc8-i_JmFpl5CAQ7cDb4cWMQEvMjXaa8vcZLANC-5HOBabZR032lEs6rB2VOwyNcav7lar4tvwTGZeeW6ZSBapSKrQrBwyW3lkUTGDq-wb3V5GDmMuYVzg62s0MjTQBGQCDYwaaYphnV1orpusRVuQsY5XmXDpBbZK4iACTVXBz_kooOEcVrlfovANnJB96le-mc0iUWIu6F7Yrad5K7tEOQ0hNvvpo0BeppgQBp1TkxWuT8yCOhwFGJ2bsTiBpTtREjWk34D0qRuaN2yLWsRcdia6OUKkBez6Pheh7-_e8ePeigeVyG7x1Ou7J2J5sBhQhxN8yMry-KOMpkdt7XWJoLZd_LokNEEgOrNSuejrqq1J3sssyZT2Jnb5Hxa_LsgN0eFzo5tPo9MCfD-H1C_o7XCpGA3AEsW9qules2crh_0lKKWZmZf6CeY9bAw2ptQwtlpCojV8QOcHQYsrOtYGWHCT4UCs6M4GmKGo5mj7QJ_Vc4oI0mz3X9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه در حال آموزش نیروهای جدید از کره شمالی است احتمالاً به منظور آماده‌سازی برای عملیات  در اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140186" target="_blank">📅 13:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
عملیات انهدام مهمات عمل نکرده در برخی از شهرستان‌های آذربایجان‌غربی اجرا می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140185" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/INlf0bcjb3wprP61qq1-ylY3i5Mw8-itwR9Bav_14FGe9NeULpJn1PEChMOdU4G720eYA5fNssPV5e7XNk2ET_RaVCTUeuUrEok3gOI-4QpY3cuW3ZFtKSD3XKK-aQzM4f29KbN7bUJg0AIR-lpbmTs0r7A6bIsEKWmo4EqPXH0eFFtnHXKCMEwYiR6hAthOQaeYKtAalDz-UAY7-yGmHiTjxPcCesVU7RVYBS6gojkkwaAnXZK0UP1boVgZRoAfkEdBktotyEzs6QTdOzGtsEULE5XGNpcuVLYvcAeudeouHmXxRDbYDZ8Aqk3cuT2yw5Fd9khE1g3pTNaAbIa5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
اسرائیل با سم‌پاشی هوایی، با استفاده از ماده گلایفوسیت بخش‌هایی از اراضی کشاورزی سوریه را هدف قرار داده است
‏
🔴
آزمایش خاک در حدود ۲۰ روستا، آلودگی و غیرقابل‌کشت شدن این اراضی را نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140184" target="_blank">📅 13:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ccbf767f0.mp4?token=Fj_0P2dyWQCWGQFMXKqAe4SglWDFKKAcuxXGxDUKA0L6AkE5YrbiM59kcPHyXA1jPvI9_-4SSGlhRPdSsqxTidp2nLfgJ2-nE1J7urdLoLDXx_DZ62cFQsdySCmtiu-ZI7fazG_jf1PAOpb6gPnqk5qpHpO5Jg2WKC4idTandjGRr39kemAO-5efYIbHVi-hPEwFUH_edhEggwIJ1hFkdGEj69xIt1E3iu7V1_3DXCDTdvbGGQDpo75XmMfvXUI-NF_YPiQageB74VwVOW2_zo6pqVzWviXLWXvP4j77etfnQR4v1tiDCvvOkY0vT4g4x5-QtKKn1QiMKZJxdxmfSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ccbf767f0.mp4?token=Fj_0P2dyWQCWGQFMXKqAe4SglWDFKKAcuxXGxDUKA0L6AkE5YrbiM59kcPHyXA1jPvI9_-4SSGlhRPdSsqxTidp2nLfgJ2-nE1J7urdLoLDXx_DZ62cFQsdySCmtiu-ZI7fazG_jf1PAOpb6gPnqk5qpHpO5Jg2WKC4idTandjGRr39kemAO-5efYIbHVi-hPEwFUH_edhEggwIJ1hFkdGEj69xIt1E3iu7V1_3DXCDTdvbGGQDpo75XmMfvXUI-NF_YPiQageB74VwVOW2_zo6pqVzWviXLWXvP4j77etfnQR4v1tiDCvvOkY0vT4g4x5-QtKKn1QiMKZJxdxmfSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل تصویری دقیق از زیرساخت‌های حزب‌الله که در چند ماه گذشته هدف قرار گرفته‌اند، منتشر کرد. عملیات‌های انجام شده توسط فرماندهی شمالی ارتش اسرائیل، مراکز فرماندهی، پایگاه‌های عملیاتی، پرتابگرها، ایستگاه‌های مشاهده، زیرساخت‌های زیرزمینی و مقادیر زیادی سلاح حزب‌الله را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140183" target="_blank">📅 13:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346341c053.mp4?token=klSTXUHyZcx9Jzbuh5lM4_qU1HLH6iCvD-3rbSHhEMxwivBDOoswRtu1SjXOaIq5r5Iqr9EAc_Tao6qXYtcWmcfYHezHdxOp0QbcVPL0jNCaudHluisGB6FnDFhV8Q6Ps83OHTPCNeVjFXcBBSTOVqgGKzuHSEndoipHV8r2sSp1yFUpylBhQB5XhZnotnS1I6ZJgUJLhn8fIhRthjuFUf4zInsSHUK9SQDvxUOVlO2deYGncMlEUngZOVNpa2NO3bSrneUYQP0xOS4GeGBc0cxTtYDS_58ulIkfBONV_vvLXBpv0-TpUAMK4dnOAHbqeGGmJSQbCUpoS0Vmi8gr7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346341c053.mp4?token=klSTXUHyZcx9Jzbuh5lM4_qU1HLH6iCvD-3rbSHhEMxwivBDOoswRtu1SjXOaIq5r5Iqr9EAc_Tao6qXYtcWmcfYHezHdxOp0QbcVPL0jNCaudHluisGB6FnDFhV8Q6Ps83OHTPCNeVjFXcBBSTOVqgGKzuHSEndoipHV8r2sSp1yFUpylBhQB5XhZnotnS1I6ZJgUJLhn8fIhRthjuFUf4zInsSHUK9SQDvxUOVlO2deYGncMlEUngZOVNpa2NO3bSrneUYQP0xOS4GeGBc0cxTtYDS_58ulIkfBONV_vvLXBpv0-TpUAMK4dnOAHbqeGGmJSQbCUpoS0Vmi8gr7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز صبح یک انفجار توسط ارتش اسرائیل شهر زواتر الشرقیه را در منطقه امنیتی جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140182" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دور سوم مذاکرات بین لبنان و اسرائیل در شهر رم، ایتالیا، آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/140181" target="_blank">📅 12:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHl7K6HWKMd8GrUfgT2GGEIhXom-OjaOomNTFHQJMaS2g0qD-pA8YMGwTzj3MRXob5iI4KyCrWN5v8yM7hfhkXHQJW2Y3uWpJcI3A2pRjtlIUI6sBGGSVRIpxa4qyvT_W3ecA3zAZmZrvGb4zy-jQMYO3HZUTWeCilyQ994uJ8_atLq7BwhhIxTjorB1ZZJZDjxytsO2goRw7OYHftZ5mwr3cLIQQ_s0rl1BsQgpbC-cCd-26HI_jI08b9EsunyC0OGYNLU8axjkTNQrBaF9XDUg1C-Gy3Au94ciq8YgqSXRX-26odIOanz1vYIdeyZk1PSpdGWHeLoUy9IG8DrjJztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8b9829e0.mp4?token=fqAOz3sfd-dJLK6wSNMy2c-xUYjy_vyDQ_7kOKTU4nzkhLF_J_ie_IldqXd-MvHKeFT1dUrkwxLC-kGHH27g5zTXkirCasc3ymLIA2MbNF0xuhI80NlgZ3ETTL9KPUn7lCxsYGSEBuKzy65Su_rtQCXTGlXfk6yqrZbhuY1Fm9f0_MbEfaxw9mMF311Ad5fMhrUbPwwYlFeDE0ckzJeACvnuHokTFBWOYHrE57fPUjZNiXTRZGco-o1Oq-aYkSTq3oV5qy_M5frRiE1TvcEK4LHbbR9VQxpddST0W4lf_6k4016yQfP0RKJB9yCOQFzMESsI1NpqMtXkAVlUKRTZHl7K6HWKMd8GrUfgT2GGEIhXom-OjaOomNTFHQJMaS2g0qD-pA8YMGwTzj3MRXob5iI4KyCrWN5v8yM7hfhkXHQJW2Y3uWpJcI3A2pRjtlIUI6sBGGSVRIpxa4qyvT_W3ecA3zAZmZrvGb4zy-jQMYO3HZUTWeCilyQ994uJ8_atLq7BwhhIxTjorB1ZZJZDjxytsO2goRw7OYHftZ5mwr3cLIQQ_s0rl1BsQgpbC-cCd-26HI_jI08b9EsunyC0OGYNLU8axjkTNQrBaF9XDUg1C-Gy3Au94ciq8YgqSXRX-26odIOanz1vYIdeyZk1PSpdGWHeLoUy9IG8DrjJztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیرعامل توانیر: ۲۷ میلیارد تومان، پاداش گزارش ماینر پرداخت کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140180" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
داده‌های حمل‌ و نقل دریایی: تردد از طریق تنگه‌های هرمز و باب‌المندب، نسبت به روز قبل به طور چشم‌گیری کاهش یافته
🔴
تنها دو کشتی از تنگه هرمز عبور کرده‌اند و یک کشتی از باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140179" target="_blank">📅 12:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140178">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رسانه های آمریکایی: اسرائیل در آستانه انجام یک عملیات بی‌سابقه در لبنان پس از حادثه تلخ بود، اما آمریکا در لحظه آخر مانع شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/140178" target="_blank">📅 12:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140177">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وال‌استریت ژورنال: امارات خواستار تشدید فشار نظامی آمریکا علیه ایران شد
🔴
روزنامه وال‌استریت ژورنال در گزارشی نوشت: مقام‌های اماراتی در گفت‌وگوهای خصوصی با دولت دونالد ترامپ، خواستار اقدام نظامی شدیدتر علیه ایران شده‌اند. بر اساس این گزارش، برخی مقام‌های اماراتی معتقد بودند فشار بیشتر آمریکا، از جمله کنترل تنگه هرمز و بررسی گزینه عملیات زمینی، می‌تواند تهران را به مصالحه وادار کند.
🔴
این گزارش همچنین از اختلاف دیدگاه میان کشورهای منطقه خبر داده و نوشته است در حالی که برخی کشورها از جمله عربستان، قطر و دیگر میانجی‌ها بر کاهش تنش و ادامه مسیر دیپلماسی تأکید داشته‌اند، امارات رویکرد سخت‌گیرانه‌تری در قبال ایران داشته است.
🔴
مقام‌های اماراتی یا دولت آمریکا درباره جزئیات این گزارش اظهارنظر رسمی گسترده‌ای ارائه نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140177" target="_blank">📅 12:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140176">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
یک منبع بلندپایه به العربیه: اعلام توافق برای بازگشایی دوباره تنگه هرمز ممکن است طی چند روز آینده انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140176" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140175">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ-cDvALCp9sFkyU7DI7kzcJou3ytswGJMnJkMysyUHX8UMfrfqvhXpR5-k4pyD1Z7SiE39WoODh4qNwzhLGpKA6aj5AhjMjf7-7WSU4H-snWPYvixePQsRJQYbDltQ1JR9nLFmG1ZXT9hSzW0h3cIxEAaRZsh0oS4NnEIoA4fYMbxbf7dJ7XBcoTyNPcEyRL9m7HIH__n3xy4EpohM7JcR1u2zvwZifv1UtW4Tzhp7tTdsVX47emykUW9nFog8i7VILxdL7i2OpEulFjlcg86e-d4RrvK-_bYVMSxn9IPKNjj0X1TBHLsKMjC9GtpDU_hMEsUxqej6J_Y6b9lB0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز: عبدال‌السید، نامزد چپ‌گرای سنا امریکا ، بیش از ۱۱۵ هزار دلار از اعضای سازمانی دریافت کرده که ظاهراً با حماس مرتبط است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140175" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سردار ابن‌الرضا: فناوری بومی ایران، برتر از هر سامانه وارداتی در منطقه است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140174" target="_blank">📅 12:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
منبعی بلندپایه به خبرگزاری الحدث:
وزیر امور خارجه پاکستان از همتای ایرانی خود برای سفر به اسلام‌آباد دعوت کرده است.
🔴
سفر عراقچی به اسلام‌آباد برای روزهای آینده پیش‌بینی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140173" target="_blank">📅 12:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بر اساس گزارش واشنگتن پست، رئیس‌جمهور ترامپ در کمپ دیوید، پیت هگست، وزیر دفاع آمریکا، را به دلیل کمبود مهمات که گزینه‌های نظامی ایالات متحده در قبال ایران را تحت تأثیر قرار داده است، مورد بازخواست قرار داد. کمبود شدید موشک‌های رهگیر، ارتش آمریکا را وادار کرده است تاکتیک‌های خود را تغییر دهد و تهدیدهای ورودی را نادیده بگیرد، مگر اینکه ارزیابی شود مستقیماً به سمت یک هدف مشخص در حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140172" target="_blank">📅 12:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یک منبع بلندپایه به العربیه: اعلام توافق برای بازگشایی دوباره تنگه هرمز ممکن است طی چند روز آینده انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140171" target="_blank">📅 12:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi-X1q0N4bUpl0XhVyknBfXEbpycr9-8udTBsssjWZnVGMjGjOonTc4XPm_KqdoKBSxngmEFrXcIdgqo6Xgu620izR20_xifKXh3VKaSWXF2Ga8PxgxSxy8OFzOq0I1E9xkvZYzUsTA3ORbJCBASIFtQnhPkDF5OC92XnWBRZ0LyetNouAczfKniKHjalAENKiHXOihSHw1WiuYvHN1JSLVDIlPlGuSONyK0OPIs0nUHwl4aikI-2jM3-7u4a73Q1iunySR72qYlFSWs3H5C6XPCHLkSvCzfJ6tu_74Rwsf9DaKRi8S6l0UQCyjtT_9BZvMwNs8QaSBE865tbQJKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن پالیسی: کاهش تنش میان عربستان و امارات می‌تواند به کشورهای خلیج فارس برای هماهنگی بیشتر در برابر تهدیدهای ایران کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140170" target="_blank">📅 12:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رویترز: ترامپ بار دیگر از روند گفت‌ وگوها با ایران تصویری مثبت ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140169" target="_blank">📅 12:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دولت ژاپن : کره شمالی یه موشک بالستیک مشکوک رو شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/140168" target="_blank">📅 12:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJsa1Y0LArFQZ4n7hiouxX3PROobOa-JSuoK96Vo-BLc1Qwby11meMAo-IPI4hAInXgz3csy8rPfgpoEnVexFIJ7129Gc3EMRuXsYX6Tjlfte9M54xo_f9g6GV-H7fIbEUQXO2QnB-eda5WwdRaTSpVoriPp1X_IGXtRkO9xX07ejANwD1bRV4YmvOjJ46XDojlgxwV1BzyiOsMYLE9eJzXCNuNG9m1Qosg2Qfy20_-WRnxEZ7lZ3NMYEU6wWD4qjjR9MkJVBkFNGPMyLQQT3cNbVnSkj9Ln0WihhC9Uo8QA4WHVKU6er8d8bhO9K3rjnYP447KI0cCtFU992CVAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ژاپن : کره شمالی یه موشک بالستیک مشکوک رو شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140167" target="_blank">📅 12:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ارتش اسرائیل: ۱۵ شهروند اسرائیلی وارد خاک لبنان شدند؛ نتانیاهو فرستاده ویژه خود را راهی واشنگتن کرد
🔴
ارتش اسرائیل اعلام کرد حدود ۱۵ شهروند اسرائیلی روز گذشته به منطقه غجر رفته، به حصار مرزی آسیب زده و از مرز عبور کرده و وارد خاک لبنان شده‌اند. به گفته ارتش، نیروهای ارتش و پلیس مرزی وارد عمل شدند و این افراد را شناسایی و به اسرائیل بازگرداندند.
🔴
همچنین روزنامه هاآرتص به نقل از منابع آگاه گزارش داد که بنیامین نتانیاهو، ران درمر، وزیر امور راهبردی اسرائیل، را به واشنگتن اعزام کرده تا از شدت تنش‌ها با دولت آمریکا بر سر جنگ غزه بکاهد. این گزارش تاکنون از سوی دفتر نخست‌وزیر اسرائیل به‌طور رسمی تأیید یا تکذیب نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140166" target="_blank">📅 11:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سپاه: احتمال شنیده شدن صدای انفجار ناشی از عملیات فنی در پاکدشت تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140165" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIGJ05C15ya09ldeZNsCJmLrsp6mM187IdHtJU4Drl9eDbxXFsJ7-NkJuk-aIjV6iqNHNS0DvAtysEr0FTecUcv7QoZNYyZ0VMXaJLTFKQz__hRO8EfYhh8doUAuukCTtWvYrJHpZZndqYsD4BTq6u5_nlOJ1cmMXmOQCkeCwKNYfuUl-ySMVEOWQuQwM3N8POE4lJ_ZYsFlO35Q_o6W45OO2lnwdcEnatE7hB-egc_KyPoy_cfyR694qIOOvVD33AXtMgnaD81EbjoCRDLKPSAm4uTu_qcPCJQopqSF0Vi4D3tDLEi2AqG986QAd-j04MJVaAFzcxHNpXBOmSAdYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک موشک از یمن به سمت کشتی‌های سعودی در دریای سرخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140164" target="_blank">📅 11:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4iGj1u4PvSQfa7lGTp1HHZbYYP7vP6RIJ2MDwqc7H4rFIVs72u7hGVmY-MOaJLBC8YnRZKQXg61zBsStzeu-fdPqE0THiMVMl1b-YZWguX6I-xBl5R_wkvVEyVO--XhUlD_RFcVN6GjXeGHaQftFnTlkNdUhrulN1-6VInR3bOqRMjJThAE20N2az5Uapexc0Wo-HXgrFG2n6lsqolevlnp1DTjgW1POnMQlOwbYU4gJFI2hOzBmkVrixv0x6muMxmOtJp56A3MovknaOhShzwnAghuJbE2JzAZ-Ti8Rpx7BU8XAtZTLSp13ygighpr1ByYWjox_G3KNlXJPw027A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان جهانی هواشناسی به‌تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔴
براساس پیش‌بینی‌های موجود، تمام ماه‌های پاییز از بارش بالاتر از نرمال برخوردار خواهند بود، اما اوج این بارش‌ها در ماه اکتبر (۱۰ مهر تا ۱۰ آبان) متمرکز شده است.
🔴
در این بازۀ زمانی، انتظار می‌رود سامانه‌های بارشی متعددی وارد کشور شوند و بخش‌های وسیعی از ایران، به‌ویژه نیمه شمالی، غربی و مناطق زاگرس را تحت تأثیر قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140163" target="_blank">📅 11:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سوال : در مورد ایران، چه چیزی باعث می‌شه فکر کنید که این بار اوضاع متفاوتره؟
🔴
ترامپ‌ : نمی‌شه با قاطعیت گفت، شاید این بار اوضاع فرق داشته باشه، شاید هم نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/140162" target="_blank">📅 11:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me2TngbZtBQKsh2_dGTZv0bLLrWX4ilaO9aTtqWes70yfzk5MH-hfVZvh8Kf1cZtKzMv9Lzm9fQow8Q53LGkjiHuscO4umG0VVVm1LpbH60pu1tdqD5kKYBQQwF2Vd9beI-Hp2GEnoxf98Ya49Q745Lth6gg1u2rbM0WmNwhXHlC6xhW-aHbXnH5l8o4OQg9Oe7xhKxIuNBq8g9a3hbW0nwoHDBgdnFMuki2V6PXaKx_N9tsDTbt4Y77VWD1m_y1mG6TYOTENXcOice7VfKZDLK5x4ZLrBfaD10owfigq1klzFnIUReXDHmyJUFZBuik9oDsPhkEdYxRRNMWK13_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حادثه امنیتی در نزدیکی سواحل عمان رخ داد.
🔴
یک نفتکش تو ۹ مایل دریایی جنوب‌شرق کومزار عمان، موقع عبور از تنگه، صدای دو انفجار شنیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/140161" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140160">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e77000cff5.mp4?token=ivHmDxWY-6gez23YXRR6YvIHBB_Cnp4EiKb07b6JEyGbhz3yIipXUoADd8DzJyVoG_KQpK3spnvyDWdZdalzNTJ75yLYZ65lIkLFmnI8W9jzCbtgZPjmaUSLCiyrPDmgBAQufJ_YLu8jWRYq4eyr-FVA3491nbfsPbMOVaGXbb8QmuGCI-cpfjzW1Gb0id-wDMXfpDIuvjL-XlBwUXOIw6pzrKsSD0SCYivWIXL0dfw718p5DFUGQzrjKewJD5XIt-rsji1p-znOuwC1Gzt6NM4BVt8_0yuuA85GNICkGgt6BENxdhuHEOx6IaRbrGkSrtIywx9qftZYLPWKn5UOGH9gYuihGsoM0yAuALa9f7qZ1iaLjJkL5DRfooPXJo8nJvHFnaDzFUgJQXBGyhzrttNJI10_1qn34wd4AsDvdFlw6mUgJkCrfBJke6PGmLcG5x3syl5lpbfiuKokd5cT6K7HIrPQimoPnmA4bxS_ZTjEvJ1Z6Vt2QBOMi9ssqcgwad_9PtTeAeoNDzmDyOP6n_PN1z2yczkx8zbEVwbnxtteUZdNYkCK2rIw95Bm4woQkgMwZoap2fZayFQgBdDtG1TWYrfVHAufEjqmOtTKqOf5WYwIPiH6cAK5XsM14Xb0jddKj95Nzh-HK8niFUzN-9HDgUCLdaZbeN5YHcLUPHI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e77000cff5.mp4?token=ivHmDxWY-6gez23YXRR6YvIHBB_Cnp4EiKb07b6JEyGbhz3yIipXUoADd8DzJyVoG_KQpK3spnvyDWdZdalzNTJ75yLYZ65lIkLFmnI8W9jzCbtgZPjmaUSLCiyrPDmgBAQufJ_YLu8jWRYq4eyr-FVA3491nbfsPbMOVaGXbb8QmuGCI-cpfjzW1Gb0id-wDMXfpDIuvjL-XlBwUXOIw6pzrKsSD0SCYivWIXL0dfw718p5DFUGQzrjKewJD5XIt-rsji1p-znOuwC1Gzt6NM4BVt8_0yuuA85GNICkGgt6BENxdhuHEOx6IaRbrGkSrtIywx9qftZYLPWKn5UOGH9gYuihGsoM0yAuALa9f7qZ1iaLjJkL5DRfooPXJo8nJvHFnaDzFUgJQXBGyhzrttNJI10_1qn34wd4AsDvdFlw6mUgJkCrfBJke6PGmLcG5x3syl5lpbfiuKokd5cT6K7HIrPQimoPnmA4bxS_ZTjEvJ1Z6Vt2QBOMi9ssqcgwad_9PtTeAeoNDzmDyOP6n_PN1z2yczkx8zbEVwbnxtteUZdNYkCK2rIw95Bm4woQkgMwZoap2fZayFQgBdDtG1TWYrfVHAufEjqmOtTKqOf5WYwIPiH6cAK5XsM14Xb0jddKj95Nzh-HK8niFUzN-9HDgUCLdaZbeN5YHcLUPHI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور قالیباف: اقلیت پر سر و صدا حیا کند! یک جا ترمز خود را بکشید و از نظر اکثریت و قوه عاقله نظام تمکین کنید
🔴
سیستم امنیتی به آنها خواهد گفت که مستندانشان در مورد کودتا را ارائه کنند
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/140160" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140159">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سخنگوی ارتش: ارتش در آمادگی کامل قرار دارد و با نوسازی سامانه‌های آسیب‌دیده، ورود تجهیزات جدید و تکیه بر توان داخلی، بی‌وقفه مسیر افزایش آمادگی عملیاتی را دنبال می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140159" target="_blank">📅 11:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140158">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شرکت هواپیمایی "ویز ایر" اعلام کرد که به دلیل افزایش هزینه‌های سوخت هواپیماها، ناشی از جنگ در ایران، متحمل زیان شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140158" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140157">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWqbHG9uQxUFHFYFvIlD5zuFeVPJU8xCuWkyaDycjEJFHZ3NhS_xB2vx1rVHL_Y0M2hnah3O3LWIE91emeawaq_7c52CKVYv2EFNOuWvXtERmV9TwxgIzal987tHJ9wMCi__55GhDaR1n3hWSR37qvOEAOwNg403C_IZD4igj6G9u42x60yIxMmFPpE-_ZAkart6vZGLT_W03h_DLxiGm4vJo9OkEQ6N6GmXsCAj-QR4Y0RlLjUW_DUTFVzktp_qs-Y7cbDqvyKtVI56ow1V7gLqPPKO31RgEsMbMK3vy7yxVBvNFgm_gwqt44bkVrF_darC4nYKlrMPzPoPdO55zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هوایی جدید از حجم ویرانی در روستای مجدل زون در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140157" target="_blank">📅 10:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان:
سلطنت عمان نقش مهمی در حل‌وفصل مسئله تنگه هرمز ایفا کرده است.
🔴
ما همچنان با سایر کشورها در مورد بحران خاورمیانه و وضعیت در هرمز در حال رایزنی هستیم.
🔴
تلاشهای دیپلماتیک ما برای دستیابی به راه‌حلی جامع و پایدار دربارهٔ تنگهٔ هرمز ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140153" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
روسیه: ۲ کشتی حامل محموله‌های نظامی را در دریای سیاه هدف گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/140152" target="_blank">📅 10:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سازمان وظیفه عمومی فراجا در اطلاعیه ای ضمن تکذیب شایعات فضای مجازی با عنوان "معافیت سربازان فراری" اعلام کرد: آن دسته از کارکنان وظیفه که به هردلیل خدمت سربازی خود را به اتمام نرسانده‌اند، می بایست وضعیت سربازی خود را از طریق یگان خدمتی تعیین تکلیف کنند و هیچ نوع معافیت جدیدی برای آنان در نظرگرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/140151" target="_blank">📅 10:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140150">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
رویترز: پس از آنکه حوثی‌ها اعلام کردند یک نفتکش سعودی را هدف قرار داده‌اند، تردد کشتی‌ها در آب‌های خلیج فارس کاهش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/140150" target="_blank">📅 10:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140149">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaU5vg6nk7REpv6PuY2omHOnci_2qmgBgppSpgIqm1DpuH9FkilfoBFuZVuc-p48kVeljiYE0Gix6a1xlpqXZhV0EAQXyvuYrWADVbWy8OUPOZzK0bxFWWUV-Ddi-qSW8G_RWs0B7JkyGQ0X5MMlyWB67_E4yj0sCQdZrUzkk1ejsq1YWDKYbUR_ctdnZCRmHGOjYtlrY36bxpsDQAsV0LgmU89KSUnh8j-po8sprrwqMjjeeXC5gtQDn0e4NG3Aj2HznEyFgH4DTRUPj_zy6SVzdO0onp9dASVNi2zPerVmMIgqbIQTc63WpcvanReoVWNmbt_-PrxtkhnckJ3gCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشست چهارجانبه وزرای خارجه عربستان، پاکستان، مصر و ترکیه در امان برای بررسی تحولات منطقه‌ای و امنیت گذرگاه‌های آبی برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140149" target="_blank">📅 10:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ونس درباره ایران :  ایران هرگز به سلاح هسته‌ای دست نخواهد یافت و ایالات متحده نیز در موقعیت قدرتمندتری قرار خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140148" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43713c064d.mp4?token=qMQT5dqBgB3a1bEL8eFZp5TO6DjK5KK8-LruVZrfDBG6gbo1qnGyf4MkWq0mdmnQGdRusG4OsA9Y1yAsYpxpYbkgqFwBvTBxMFije83V8hqDtFAtPaoz1G43NEfnmKWrUbpn464--mZSG1L9DlLeyxJM3KJ0lYr0TLt-7FFkD4ty53JtVlNF-A55DBjzp_-WvNF_41s2xLszN5C36nd9CREUXjXi85NoaYZGy1UwE8x0GZPnC4enr2ZZvEB5IhYkdkD2V_r5ynqq4sJHvpmco7-v2qKVRu3mFSFGuB-_D4aNN4GadwNq8Y-cZo_RGChpMYNeolkqme_oYzgY9j-gz6KEybaRrfcsSFsqJB8tSLAdjDa2rxM9xFNQPMomTAQdZb3hmzWxOAZNabKl3NJXte-4Oy4ZPsyvzQkcc61dbQo3ZQzjEPWjNkPn2_MimmaD0HWLhb1zRsjjTbH7z6o9wNBten-e3RUu3KKV6DvRpZ0gpFdcvMlyPnYIkruZzh7Z95BpPrWbztYiUKr8QG-965zX6bIHLRP7u4q6yb8SjYyGku2iSwXFyPsWkt6HS9ACrBxrz1ZXBc02g7Polp_1nyslBkhT-7htvWYGelP-FvkKs8wWKTr8McDIO4shRHSaPfARMT7jGMJw9Ms2LrJSfV5duvUE2hcbCw9ZnYgKY5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43713c064d.mp4?token=qMQT5dqBgB3a1bEL8eFZp5TO6DjK5KK8-LruVZrfDBG6gbo1qnGyf4MkWq0mdmnQGdRusG4OsA9Y1yAsYpxpYbkgqFwBvTBxMFije83V8hqDtFAtPaoz1G43NEfnmKWrUbpn464--mZSG1L9DlLeyxJM3KJ0lYr0TLt-7FFkD4ty53JtVlNF-A55DBjzp_-WvNF_41s2xLszN5C36nd9CREUXjXi85NoaYZGy1UwE8x0GZPnC4enr2ZZvEB5IhYkdkD2V_r5ynqq4sJHvpmco7-v2qKVRu3mFSFGuB-_D4aNN4GadwNq8Y-cZo_RGChpMYNeolkqme_oYzgY9j-gz6KEybaRrfcsSFsqJB8tSLAdjDa2rxM9xFNQPMomTAQdZb3hmzWxOAZNabKl3NJXte-4Oy4ZPsyvzQkcc61dbQo3ZQzjEPWjNkPn2_MimmaD0HWLhb1zRsjjTbH7z6o9wNBten-e3RUu3KKV6DvRpZ0gpFdcvMlyPnYIkruZzh7Z95BpPrWbztYiUKr8QG-965zX6bIHLRP7u4q6yb8SjYyGku2iSwXFyPsWkt6HS9ACrBxrz1ZXBc02g7Polp_1nyslBkhT-7htvWYGelP-FvkKs8wWKTr8McDIO4shRHSaPfARMT7jGMJw9Ms2LrJSfV5duvUE2hcbCw9ZnYgKY5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره اسرائیل
:
نتانیاهو با من برخورد تقابلی نداشت. گفت‌وگویی صریح و در عین حال دوستانه داشتیم.
🔴
همان‌طور که بارها گفته‌ام، اسرائیل شریک بسیار خوبی برای ما و یکی از متحدان ایالات متحده است؛ درست مانند فرانسه، بریتانیا یا دیگر متحدان آمریکا. طبیعی است که گاهی میان متحدان اختلاف‌نظر وجود داشته باشد.
🔴
فکر می‌کنم رسانه‌های آمریکایی بیش از حد مجذوب این موضوع شده‌اند. واقعیت این است که وظیفه من، پیشبرد منافع هیچ کشوری جز ایالات متحده آمریکا نیست.بنابراین، هرجا منافع ما با اسرائیل همسو باشد، درباره نحوه تحقق اهداف مشترک گفت‌وگو می‌کنیم. هرجا هم دیدگاه من با نظر نخست‌وزیر اسرائیل متفاوت باشد، درباره آن صریح و بی‌پرده صحبت می‌کنیم.
🔴
من این دیدار را گفت‌وگویی دوستانه، اما مستقیم توصیف می‌کنم. احساس نکردم که با من برخورد تقابلی شده باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140147" target="_blank">📅 09:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو زمین سوخته‌ای را به جا گذاشته و اسرائیل نیاز به التیام دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140146" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
معاون رئیس‌جمهور آمریکا در مصاحبه با شبکۀ «فاکس‌نیوز» مدعی شد که از تمام ابزارها شامل نظامی، اقتصادی و دیپلماتیک برای رسیدن به راهکاری برای ایران استفاده می‌کنند.
🔴
ونس: ایرانی‌ها مذاکره‌کنندگان سرسختی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140145" target="_blank">📅 09:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxPc_SNC0IUxVXknU7Q88GpdYjeMwh0E0oGlfD7z2RzsKqxUqKIJ1Qrl_rjkKFaBVJ6BA8bjFejN9L1ZGLeAM_9eSayzuppfSK6B4W8IGgfs0XqxketZg2CPX-_oWcB2hSBxuYRRbGJ1ZZtrVdkHiPoo2xEEYV62mYedzOKNDRXrqKUPMEG7pc2vTt6HUnHQ1RryoD8bGrDQsFo-xkV3oLCviXtFyTkowrrjHtvDlIz480Z94XRcPYZiUvy2Od2lrCRHUOMdpCIHxrGy_mwFsWHL0suJ2Xoka77exf-aAtRTWPOYAksiJP_Wt6Po8Anv_e4A70AiGoszq0e1lMlACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت
🔴
نفت آمریکا (WTI): ۷۴.۷۵ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۷۹.۰۹ دلار
🔴
نفت امارات: ۷۷.۹۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140144" target="_blank">📅 09:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سپاه تهران اعلام کرد: صدای انفجار احتمالی در پاکدشت بین ساعات ۹ تا ۱۲ امروز، ناشی از انهدام مهمات عمل‌نکرده است و جای نگرانی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/140143" target="_blank">📅 09:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=HYFUS4gcYr_TMFiDiYlKGpJsNVfUS-ulMCGAomE6ymmpd7ORDmJahuZRYvGO2ox0ocef4mrvt9BSsjE5shcII7FQjmyppxrdYtCd0257242y6OrHqj5RZ9nnC34iua1DBijqOQ2WYj5qIXPks_J9HDd261ib6_UXCd9C69ujf9JEK7OEKMwJ6vXmlH68P2IE1AqCfPiEb0h4iFjUe1iI12jWDqvtR8QCYm4CcB5smJee4ookhAY8rKLPaq5Gu5gYcgRz_6RvI9Ctm1U0T4IIIpe7_z7X58H70R6CdrD_KtUcT9HQ38N2zjKgCdA4XEpaG5bc3gZzx1ABUuvs2Ei5wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a86cac7b.mp4?token=HYFUS4gcYr_TMFiDiYlKGpJsNVfUS-ulMCGAomE6ymmpd7ORDmJahuZRYvGO2ox0ocef4mrvt9BSsjE5shcII7FQjmyppxrdYtCd0257242y6OrHqj5RZ9nnC34iua1DBijqOQ2WYj5qIXPks_J9HDd261ib6_UXCd9C69ujf9JEK7OEKMwJ6vXmlH68P2IE1AqCfPiEb0h4iFjUe1iI12jWDqvtR8QCYm4CcB5smJee4ookhAY8rKLPaq5Gu5gYcgRz_6RvI9Ctm1U0T4IIIpe7_z7X58H70R6CdrD_KtUcT9HQ38N2zjKgCdA4XEpaG5bc3gZzx1ABUuvs2Ei5wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور آمریکا در مصاحبه با شبکۀ «فاکس‌نیوز» مدعی شد که از تمام ابزارها شامل نظامی، اقتصادی و دیپلماتیک برای رسیدن به راهکاری برای ایران استفاده می‌کنند.
🔴
ونس: ایرانی‌ها مذاکره‌کنندگان سرسختی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140142" target="_blank">📅 09:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزیره: قیمت نفت در پی امیدها به توافق ایران و آمریکا در مورد تنگه هرمز، کاهش یافت
🔴
بهای معاملات آتی نفت خام برنت با ۳۷ سنت کاهش، به ۷۹ دلار و ۸ سنت در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/140141" target="_blank">📅 09:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4caa2d703.mp4?token=nkCq-72MlzKv-XRq3O5rOTwk3SiWdOTfziU_RVGwI_3RGV1EaJD13SgIrHf8uY34kk8p7ChfbaV5PzZvV55oRy07_q71aDi4_6IJZQW6DG7ipo1BfR2ank-3i--jNOYazNd9VqJTxHlSOwCt4X1om0hdbAfTLNSUcdJwUFHH0hdFy8LFnCiNJouSAjuo-lLnS2CV-Jw-I5aIO4DOgUFTeflniFANuDbS6xTVsA9QpQL1lmS9pubSRv452C08pTKtw6BNsSpNe2qTlSYSXqba90HhsP2etTE1lVvTgHth6g_lKBPPANhUTW8sNHw0OBsooaJKuQ_QWXjNhkS84GK8LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4caa2d703.mp4?token=nkCq-72MlzKv-XRq3O5rOTwk3SiWdOTfziU_RVGwI_3RGV1EaJD13SgIrHf8uY34kk8p7ChfbaV5PzZvV55oRy07_q71aDi4_6IJZQW6DG7ipo1BfR2ank-3i--jNOYazNd9VqJTxHlSOwCt4X1om0hdbAfTLNSUcdJwUFHH0hdFy8LFnCiNJouSAjuo-lLnS2CV-Jw-I5aIO4DOgUFTeflniFANuDbS6xTVsA9QpQL1lmS9pubSRv452C08pTKtw6BNsSpNe2qTlSYSXqba90HhsP2etTE1lVvTgHth6g_lKBPPANhUTW8sNHw0OBsooaJKuQ_QWXjNhkS84GK8LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد اینکه اجازه نداد بچه روی استیج بیفته رو زمین: نخواستم مثل بایدن بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140140" target="_blank">📅 09:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=Obz4V7hmBwHPB_BIcJw18-8LEmYE_s9KGud-nOlM3V6UWtnKIM6Rz9AQEntmNyix8NUW1vXZHd73P3H7GrGJufpZLMM7VagrfEpJZmOSU_ULw1ZRF1MdsWrA8NVZP3h3r49o8IH-p423uvSeOjcuNtbAHoO3nOpfpeUNzEEhpw5qaZQUxPU4r_TGnmYPGjYikfPRjvRIPGId8e6ZuQPxkJo95PU-TzS--x3Hr9M8RWvoVunTZ4JnndTaAQieWTnN1inhOSCow9jDeCkvA6zTUMtAP-fgQv9Peg_GvFBN3_vC7nBF7e2LeV9EjtdXxH15-A6LRP06eg8hkzYOPB06wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=Obz4V7hmBwHPB_BIcJw18-8LEmYE_s9KGud-nOlM3V6UWtnKIM6Rz9AQEntmNyix8NUW1vXZHd73P3H7GrGJufpZLMM7VagrfEpJZmOSU_ULw1ZRF1MdsWrA8NVZP3h3r49o8IH-p423uvSeOjcuNtbAHoO3nOpfpeUNzEEhpw5qaZQUxPU4r_TGnmYPGjYikfPRjvRIPGId8e6ZuQPxkJo95PU-TzS--x3Hr9M8RWvoVunTZ4JnndTaAQieWTnN1inhOSCow9jDeCkvA6zTUMtAP-fgQv9Peg_GvFBN3_vC7nBF7e2LeV9EjtdXxH15-A6LRP06eg8hkzYOPB06wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی عجیب در آمریکا: عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/140139" target="_blank">📅 09:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سازمان UKMTO از وقوع حادثه برای یک نفتکش در ۹ مایلی جنوب شرق کمزار عمان خبر داد.
🔴
ناخدای نفتکش گزارش داده هنگام عبور از تنگه هرمز صدای دو انفجار شنیده شده، اما کشتی و خدمه در امنیت کامل هستند و هیچ آسیب زیست‌محیطی رخ نداده است. از شناورها خواسته شده با احتیاط عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/140138" target="_blank">📅 09:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga1hXNiloeOaqL4SV1BkPwcbSadM3IEKVdnPgsGf4VoVsUkPZuBG4NzagRclynIg1QMphC954Kym4L9J_vJhLtnbPVCIckXzH4u3qC5FwFOHXkZE8b_C4ad1g6858omN-lLBuWE3o0g3Tf2LmYKRuYUAyo_U44-mWs4pHS01bUOatpoBiXQ9sKSj6aXssGHfkenM-3r7ai7rw7y5laE3_lEtX-B1KYbwn4ROXbP38OApSzVz1NyAEmuL1HBlm7zt3kmAQVlfev8vz66qOH3zLsFpBjqaCjW_GQqqmq_i0NvG7QIiZLOXBgM0WIMStd8NEW2Gd9xGYZolLqZm94N2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: مهمات فراوانی داریم؛افشا گران خیانت کرده‌اند
🔴
در ایالات متحده، ذخایر عظیمی از "مهمات" وجود دارد، به ویژه از برخی از انواع آنها. علاوه بر این، حجم زیادی از این مهمات در داخل ایالات متحده تولید و در صورت نیاز، عرضه می‌شود.
🔴
شرکت‌های دفاعی در حال ساخت بزرگترین تعداد کارخانه و تولیدگاه در تاریخ کشور ما هستند. افرادی که این اظهارات خیانت‌آمیز را فاش کردند، تحت تعقیب هستند.
🔴
آن‌ها به مجازات‌های طولانی مدت در زندان محکوم خواهند شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/140137" target="_blank">📅 09:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=eAGSVZ4m2DGUDWLFO3JXTf5GDJudSdaq0N91Bzg-eEqKsbTRQdAlrV5nCkrKh6s2PwO6ylZ6twMb7nA7_-1Ut1kJTGbId_-elJxY4Gyx4ROJ5XcmEkmEO20UuueJAdQTA2ZdiW8miOT0hVUIFjP1w52EnprJDf0POT7gi8vRyLhayAC2lb6pEdKwvzkhUuTdn7wK6TuDXq-bB3bP-I22rmBS7HYrhjvgbtvI1lGDOnprEZHFcAFAKAqesM-CgoluTrBYHnRw8T-ybCWDyOBtNIWmBw7oo3a2t4h_6jPT54hi8NTb2FNh6OXimFNvjJ2mfbaW6-yVDptioONivodrpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc78d3794b.mp4?token=eAGSVZ4m2DGUDWLFO3JXTf5GDJudSdaq0N91Bzg-eEqKsbTRQdAlrV5nCkrKh6s2PwO6ylZ6twMb7nA7_-1Ut1kJTGbId_-elJxY4Gyx4ROJ5XcmEkmEO20UuueJAdQTA2ZdiW8miOT0hVUIFjP1w52EnprJDf0POT7gi8vRyLhayAC2lb6pEdKwvzkhUuTdn7wK6TuDXq-bB3bP-I22rmBS7HYrhjvgbtvI1lGDOnprEZHFcAFAKAqesM-CgoluTrBYHnRw8T-ybCWDyOBtNIWmBw7oo3a2t4h_6jPT54hi8NTb2FNh6OXimFNvjJ2mfbaW6-yVDptioONivodrpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی عجیب در آمریکا، همین الان عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/140136" target="_blank">📅 02:39 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw_Oy9X1IPnDBz-HqMahggaywA8eTubvt9P6wb_Z2r-DTTdZaSCR_ycIPlsts8iDepIZw-b3pjd0UwHnLZStmyq-IZ1zRSrmP5IoIQxPAUyPoTuBz-CpsGTVlBSDPk2tSND3-5pPp7rfPKug8-PVumw3hYkcixDgMQQOUUeDDbTWnDMRyEBsspH4PYRoLpzPs1_hYTiKUiAcUoG2emtcRlc7FV5KCkbBO7NuPBmceFqyRDyUxOkM4Ubyrynrdpc9cF5Z36LdY3wX3uEGDE_5k3ZADcQleb5ZGSjzhhy1PN1zdxeK1dyF52yhqRoKyp_P01--1SL3I8ooL7564pqtyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ad3d54a7.mp4?token=YfO_ufmSzvWxTKiYzIc-XpswNxMMsXj-VCynI-h1Ayonuoz7e5O8JvFwp7BK_aQE6f3vP49Y3Uk_fYkd8q5gc-Gjl5OZ0Rrtzrh9tGEwebs2KyC3h6cA5uvjDBTuBtxKzA03vCLOXpXRE3hxrSteDglWaShFfFiiFDLm8H35hCK8VFd5hIRW1PfMcM4uClf_tYQzn5COd-TyEKqJXqJOfh1Q_WBypqQ8ljmRkVYFHpItl5JRnOn3hs3KA0ip9rUoaOLm5YJ96Y3xrn3GViV9fPeporitbeYaQ6qNLNx1h7jBRDXUc8ouU8OgGM7aStMzIjbpBw697Me1g_w07n8V8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ad3d54a7.mp4?token=YfO_ufmSzvWxTKiYzIc-XpswNxMMsXj-VCynI-h1Ayonuoz7e5O8JvFwp7BK_aQE6f3vP49Y3Uk_fYkd8q5gc-Gjl5OZ0Rrtzrh9tGEwebs2KyC3h6cA5uvjDBTuBtxKzA03vCLOXpXRE3hxrSteDglWaShFfFiiFDLm8H35hCK8VFd5hIRW1PfMcM4uClf_tYQzn5COd-TyEKqJXqJOfh1Q_WBypqQ8ljmRkVYFHpItl5JRnOn3hs3KA0ip9rUoaOLm5YJ96Y3xrn3GViV9fPeporitbeYaQ6qNLNx1h7jBRDXUc8ouU8OgGM7aStMzIjbpBw697Me1g_w07n8V8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/140133" target="_blank">📅 02:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: یک فرصت دیگر به ایران دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/140132" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ترامپ: ضمناً داریم همین کار را در جمهوری اسلامی دوست‌داشتنی ایران هم انجام می‌دهیم.
🔴
داریم انجامش می‌دهیم.
قرار نیست از آنجا گورمان را گم کنیم.
قرار نیست از آنجا گورمان را گم کنیم.
🔴
ترجیح می‌دهم توافق کنیم، چون نمی‌خواهم مردم را بکشم.
من نمی‌خواهم مردم را بکشم.
🔴
برای بزرگ‌ترین حمله در میان تمام حملات آماده شده بودیم. و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
🔴
ما کاملاً برای بزرگ‌ترین حمله از زمان جنگ جهانی دوم آماده بودیم.
و آن‌ها با من تماس گرفتند و گفتند:
«لطفاً این کار را نکنید. بیایید مذاکره کنیم.»
🔴
و بعد انکارش می‌کنند.
گفتند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟
رسانه‌های جعلی می‌دانند که آن‌ها این حرف را زدند.
🔴
اما داریم مذاکره می‌کنیم. ببینیم چه می‌شود. اما آن‌ها برای ما احترام قائل‌اند.
برای ما احترام قائل‌اند.
🔴
۴۷ سال گذشته، اما در واقع ۵۰ سال بوده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال بوده است.
🔴
و هیچ رئیس‌جمهور دیگری کاری را که باید خیلی وقت پیش انجام می‌شد، انجام نداده است.
🔴
چون ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
نمی‌تواند داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/140131" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b2de1aaf.mp4?token=T6LOCEIgIqkWQOvdYcPSV5gO-G7dE5a1eFv0fUhqTD08kbyDPAORiCb7_QIGvgy0rdOEcyDikLMUeEaxfQ1bC0TExT1zIlkdZEPeQSJgEen6w8cbTH9sjvtHzX-52HTr7kGvscE6Byg-sN71iVTfuz2JCs1Cx4a793Ayjk9dNaC_HDi54SKgts_iq6k4KlIAHkg5_0MOWLj26OTqT50khPN5OVLbqj9P9QKEPyiJhx1NFFwwo8LL3eBoVdwayX4BaxpZFlzx_aOdKx-JO5sDanIUMeXO_hgKbmZQ2njl-urowR0zunwvKiBWJD0avnHVQkdv_Lf1tWMG_kZb5Ul5vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b2de1aaf.mp4?token=T6LOCEIgIqkWQOvdYcPSV5gO-G7dE5a1eFv0fUhqTD08kbyDPAORiCb7_QIGvgy0rdOEcyDikLMUeEaxfQ1bC0TExT1zIlkdZEPeQSJgEen6w8cbTH9sjvtHzX-52HTr7kGvscE6Byg-sN71iVTfuz2JCs1Cx4a793Ayjk9dNaC_HDi54SKgts_iq6k4KlIAHkg5_0MOWLj26OTqT50khPN5OVLbqj9P9QKEPyiJhx1NFFwwo8LL3eBoVdwayX4BaxpZFlzx_aOdKx-JO5sDanIUMeXO_hgKbmZQ2njl-urowR0zunwvKiBWJD0avnHVQkdv_Lf1tWMG_kZb5Ul5vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات توپخانه‌ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/140130" target="_blank">📅 01:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7e04ce18.mp4?token=taf251xk8dz3-1QQgmRSnm71NvgT7_hNEuUcVtQG3LA5iBGYOLhrRpK1lOKbrlQFi0Sxgc-fidv1wxvYlQC38sLN5SNWUcsBUXH2j41P0HOuaa1tBN3Afy7v2VkG6nqjGt8jyjqrcwce12IfHajknBjAamBWoR48L1_a1BhpGbtR6haOCms6rhGNE5Z9AqExH_8_j_iuLjETBUByGiXJHK4vNUDjb9fBASB9JO4O2KFdh-C4wlahWyTG4FloCMRA0UvnfALUqPY5m2YyDzCa-VkslcJkJwwbwZSbKU-LbKuEP_ysas_DHKcb4HYgYTEBqRMK-RJN4jmUdmy1Rl3WtwYlPNKzon8JbUcmKGgI33obDSUVYsnd5iQjEOuabBYRvRYkgszpHE3BRBPXvafYIDDZ-EdKVL9yxchi4LBLHDJoQlU4rhIdQgoVwodLTY8zdZgPegigKHsVJ_XcGS0srDqmtJXDYOlNVuesRpObKz053gUwxulVn6mU-Rnh21JgajYaSqZZplu2pE_dypmYE8t_rmTYStSFTunKiInQFJ8_yX8-IvKZwKzW6ZQ1D_wAR6coaD07HoqD4hEi4o3NHmLhcoKQn9jqCi1I1maMlDKUzYzKm4EIi7YVTZgbqaupUnPKcNfftfGli2DEgncjQ2WEV-scWglWFy2mJ0ovDbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7e04ce18.mp4?token=taf251xk8dz3-1QQgmRSnm71NvgT7_hNEuUcVtQG3LA5iBGYOLhrRpK1lOKbrlQFi0Sxgc-fidv1wxvYlQC38sLN5SNWUcsBUXH2j41P0HOuaa1tBN3Afy7v2VkG6nqjGt8jyjqrcwce12IfHajknBjAamBWoR48L1_a1BhpGbtR6haOCms6rhGNE5Z9AqExH_8_j_iuLjETBUByGiXJHK4vNUDjb9fBASB9JO4O2KFdh-C4wlahWyTG4FloCMRA0UvnfALUqPY5m2YyDzCa-VkslcJkJwwbwZSbKU-LbKuEP_ysas_DHKcb4HYgYTEBqRMK-RJN4jmUdmy1Rl3WtwYlPNKzon8JbUcmKGgI33obDSUVYsnd5iQjEOuabBYRvRYkgszpHE3BRBPXvafYIDDZ-EdKVL9yxchi4LBLHDJoQlU4rhIdQgoVwodLTY8zdZgPegigKHsVJ_XcGS0srDqmtJXDYOlNVuesRpObKz053gUwxulVn6mU-Rnh21JgajYaSqZZplu2pE_dypmYE8t_rmTYStSFTunKiInQFJ8_yX8-IvKZwKzW6ZQ1D_wAR6coaD07HoqD4hEi4o3NHmLhcoKQn9jqCi1I1maMlDKUzYzKm4EIi7YVTZgbqaupUnPKcNfftfGli2DEgncjQ2WEV-scWglWFy2mJ0ovDbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رانت حکومتی به مداحی هم رسید
🔴
برادر حسین طاهری با این صدای مزخرف هم در کربلا میکروفون گرفت
🔴
سوال اینجاست آقای طاهری که دم از انقلاب و عدل و اسلام میزند چرا میکروفون رو همیشه به همچین صدای مزخرفی میدهد؟
#فساد_سلولی
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/140129" target="_blank">📅 01:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: ما پشت هم پیروز میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/140128" target="_blank">📅 01:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ: در حال آماده شدن برای انجام بزرگترین حمله از زمان جنگ جهانی دوم بودیم، اما ایرانی ها از من خواستند که مذاکرات را انجام دهم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/140127" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49df8df3b5.mp4?token=Y5ywFjUNcNmRgfFkpmTyZo47f7bss1Dbk1gTymcxEIZTvB6H5LR0oB1SfDLMUiTwCOPev9KOWEg19hcG8OirVRnXF0bI0k-mU-bDq9Co8XajU4mIwsGwprD5Pz4z5-TVEKdGr5J2cSIjwK3jL1nP6RkUPscbyUp2Uk87ocWeVvLOTEh-QnmsmZcAToTxYdAUj8RLOBC5iD4qsSp6AjwpMDqCnM0OFzNoqegtd8TfmFzf1waskQQbytuMfiAuE2v9x94xJNiWC8U0oeLIViFtadfgu6tcKhlYnyK3BRJa4egDn17hpw-BqByKmgHuV0vUEPc3-tJk-pMlfI-fe4MLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49df8df3b5.mp4?token=Y5ywFjUNcNmRgfFkpmTyZo47f7bss1Dbk1gTymcxEIZTvB6H5LR0oB1SfDLMUiTwCOPev9KOWEg19hcG8OirVRnXF0bI0k-mU-bDq9Co8XajU4mIwsGwprD5Pz4z5-TVEKdGr5J2cSIjwK3jL1nP6RkUPscbyUp2Uk87ocWeVvLOTEh-QnmsmZcAToTxYdAUj8RLOBC5iD4qsSp6AjwpMDqCnM0OFzNoqegtd8TfmFzf1waskQQbytuMfiAuE2v9x94xJNiWC8U0oeLIViFtadfgu6tcKhlYnyK3BRJa4egDn17hpw-BqByKmgHuV0vUEPc3-tJk-pMlfI-fe4MLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایران به ما احترام میگذارد. آنها به ما احترام میگذارند.
🔴
داریم صحبت میکنیم. ببینیم چه میشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/140126" target="_blank">📅 01:21 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
