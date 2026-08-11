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
<img src="https://cdn5.telesco.pe/file/Fd4sep041-ilQNu3R6IIKNWK40mdLlzA8aN0zC60LGxl3lgi8uJIfh5qDA8HpLoiWCjtbijxMsXJLbUZ89p_kP1yeMkKv4p5nxmSJJLyx0USWAyFIHdbnhVH-Es1Wf4CKCb7LHy2j89fOrrpvUtLI2qf2ypzdNgHfQe0CSwhzay6FGXGz2lovEnbhkeXLYP9z1VCROc7dPLmRPB9HlWo-ak1dfipvW-QY5KK6Fd6hndKQmkxKep_KlEmwnuK8a03ohqY-0LZyEPXxr560xX3o5feJo1trd0x-_Ip0CGo0kyB4Jx0kmhw0pU71sga17_ebxUqwysDbBWC6MJ9-Nl5eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 477K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 11:33:58</div>
<hr>

<div class="tg-post" id="msg-103336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=CGi0oysZR3eMk9a-rR-2V_X3_iIte_tid2vjFksNJ2vF3wSOwfYaIBW2HJPNw8120ZqTM4sqW3GOvdBQb8AwwGZTA12RySA-gGBJ2_vAshRqff6sOZhto_X0VOX2cWUZtf10aKvz_Crbrfwi3sz2Rereeom04_r7SbJgLin4AqKaxPB4_X8auB_emjeDCXfjbkqdz1VA_ZL9vc5acddDCoZgjQyrbzhtQgUIpLy5MsIfB6PPBa_e3tKuUBJNAIMKsl08cB5O3f8XuslYCderDBaa5dypqwH6n-4V4IIXhuN9XNgBRJYTVRSjKeSPG5THxYZzJmweN35KPYoAum2-oSicI3FBBYl51-1_i3ZFZoq4HIk5Ky3fDQf1ykAqyCGPiqyK2zZLRHQL2mRzXvpvsd0e9dXCyzDlz_1kxnBrkEElzTMarFb5ZF5xKIMRlCqm9aqKgCY940us625lr0H55Zys1R_CDXZ9cPc02sBBpN6B5a1UI30j2kIwGUtA_QHuZC_iXjnzqIEh4UdZcWeM4YJ63VZcvMbijJkpPIMlTmPzxna3oE2LF8wiGXKBfM94PNASTg1fC1eWtNP9lukAxUjzkN1At06fj4c_JWvLdjNhyZyyFgOi8zNtVZniekyZioa2njzVXSmPhpRgLP9KfXtOBNZk4wqmQisxhjuLGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=CGi0oysZR3eMk9a-rR-2V_X3_iIte_tid2vjFksNJ2vF3wSOwfYaIBW2HJPNw8120ZqTM4sqW3GOvdBQb8AwwGZTA12RySA-gGBJ2_vAshRqff6sOZhto_X0VOX2cWUZtf10aKvz_Crbrfwi3sz2Rereeom04_r7SbJgLin4AqKaxPB4_X8auB_emjeDCXfjbkqdz1VA_ZL9vc5acddDCoZgjQyrbzhtQgUIpLy5MsIfB6PPBa_e3tKuUBJNAIMKsl08cB5O3f8XuslYCderDBaa5dypqwH6n-4V4IIXhuN9XNgBRJYTVRSjKeSPG5THxYZzJmweN35KPYoAum2-oSicI3FBBYl51-1_i3ZFZoq4HIk5Ky3fDQf1ykAqyCGPiqyK2zZLRHQL2mRzXvpvsd0e9dXCyzDlz_1kxnBrkEElzTMarFb5ZF5xKIMRlCqm9aqKgCY940us625lr0H55Zys1R_CDXZ9cPc02sBBpN6B5a1UI30j2kIwGUtA_QHuZC_iXjnzqIEh4UdZcWeM4YJ63VZcvMbijJkpPIMlTmPzxna3oE2LF8wiGXKBfM94PNASTg1fC1eWtNP9lukAxUjzkN1At06fj4c_JWvLdjNhyZyyFgOi8zNtVZniekyZioa2njzVXSmPhpRgLP9KfXtOBNZk4wqmQisxhjuLGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از جذاب‌ترین گل‌های آردا گولر ترکیه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/Futball180TV/103336" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از اسپورت: سه باشگاه آرسنال، بایرن‌مونیخ و پاری‌سن‌ژرمن به جذب ژول‌کونده علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/Futball180TV/103335" target="_blank">📅 11:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=DFsvKBcp0XghDCn7LiEO5G1akNBMUUinAN5u9NPunLdortdcIKLpgza-lvIBr-C0sypIweo_Kizc0fdME3wz557llUOhbwywTRmsq_qMpg0OLwFWHyieLc44D3-rxQYOuWVEdLUBktYt9PMPv1FNsauhfbbXVrp61pjpwPFiuFCeysS8AQhoEcvFEtI9hEQQlQ4d3HGhwMrXXAuE_jvYEFzl1TZKrDs0MhHaWwMp64iec2zz9i43sIs4I9kBc2MRaiVfzZ4rDlkCRFvxNnxr1g4m07lmkHTZuyDee3whOVwqo75MqD22pLCw1c98FKrfXRpDf2osqAQLE3tqBw25eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=DFsvKBcp0XghDCn7LiEO5G1akNBMUUinAN5u9NPunLdortdcIKLpgza-lvIBr-C0sypIweo_Kizc0fdME3wz557llUOhbwywTRmsq_qMpg0OLwFWHyieLc44D3-rxQYOuWVEdLUBktYt9PMPv1FNsauhfbbXVrp61pjpwPFiuFCeysS8AQhoEcvFEtI9hEQQlQ4d3HGhwMrXXAuE_jvYEFzl1TZKrDs0MhHaWwMp64iec2zz9i43sIs4I9kBc2MRaiVfzZ4rDlkCRFvxNnxr1g4m07lmkHTZuyDee3whOVwqo75MqD22pLCw1c98FKrfXRpDf2osqAQLE3tqBw25eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ترشتگن در اولین بازی خودش برای آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/Futball180TV/103334" target="_blank">📅 11:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=hfrEWfy4OjzKqmj3AhOCz_O-rP1k4ddOIkWQCmvxTTAtt6vV8MaaMvYdiIsClewh1yyWt9A7IZZVgBIDSQlv4OLpWDS0eK7BbwdILgAVmBf4AhhPQDj3TZjUAd5IcjBKb94lrPoK0e2eFbUFH8rTnWDVrDj4RPP7rOtvCb1IjjSPxNOJEG1zFI65RO84SxhIwJdOifaFq2BepHiB9o3nz6OPVEo0NunwyV3MIua0n2UWkzXyTwJqnRWKsU5VEtm9OlOgboyCXXh7EtHg3Y1I1zJwMf9uAui6RQgU6_Z_YKKT_QCsmG1UcQkbkqVIHxec7bCd2rAke9Ewi8AhV8riEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=hfrEWfy4OjzKqmj3AhOCz_O-rP1k4ddOIkWQCmvxTTAtt6vV8MaaMvYdiIsClewh1yyWt9A7IZZVgBIDSQlv4OLpWDS0eK7BbwdILgAVmBf4AhhPQDj3TZjUAd5IcjBKb94lrPoK0e2eFbUFH8rTnWDVrDj4RPP7rOtvCb1IjjSPxNOJEG1zFI65RO84SxhIwJdOifaFq2BepHiB9o3nz6OPVEo0NunwyV3MIua0n2UWkzXyTwJqnRWKsU5VEtm9OlOgboyCXXh7EtHg3Y1I1zJwMf9uAui6RQgU6_Z_YKKT_QCsmG1UcQkbkqVIHxec7bCd2rAke9Ewi8AhV8riEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
لحظه انفجار در جایگاه CNG یکی از نقاط استان کرمانشاه که با کشته‌شدن یک نفر و زخمی شدن ۳ نفر همراه بوده!
❌
دیدن ویدیو مناسب برای همه افراد نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/Futball180TV/103333" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=B7GzQxMU2uL72AeRI2gRYODa-5leIihUZAVp8pxGdtF0Fvn-A1x4lgv6jAq6e3ME7cdQEfSOYx07VYo4f5r7kwGtAUovsubOCfYn3WptIF8iDlpF4Z2ic-6zeBtuBbU_cNtFpxBGkWI-rv9OebFTQOYt9VbqfQeDOnKl1jRZmN2LC_AdBJ21C978qQjiLudQsoP3EJnrdsovs0e35b9oI_R7LLDCHOTUG9LxH_Y4UFswUoefTwwRUcjelwxHjuYiDTVl0UX42QkPfAE6IOEOpinhPTSPbO8sxlIQTFFGYqbgY2lHayQZpgZUkF2N5QPYPHMDGtrZYNWgegTYVAmitQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=B7GzQxMU2uL72AeRI2gRYODa-5leIihUZAVp8pxGdtF0Fvn-A1x4lgv6jAq6e3ME7cdQEfSOYx07VYo4f5r7kwGtAUovsubOCfYn3WptIF8iDlpF4Z2ic-6zeBtuBbU_cNtFpxBGkWI-rv9OebFTQOYt9VbqfQeDOnKl1jRZmN2LC_AdBJ21C978qQjiLudQsoP3EJnrdsovs0e35b9oI_R7LLDCHOTUG9LxH_Y4UFswUoefTwwRUcjelwxHjuYiDTVl0UX42QkPfAE6IOEOpinhPTSPbO8sxlIQTFFGYqbgY2lHayQZpgZUkF2N5QPYPHMDGtrZYNWgegTYVAmitQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
❌
تصاویری از صحنهٔ گروگان‌گیری دقایقی پیش در خیابان ولیعصر تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/Futball180TV/103332" target="_blank">📅 10:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103331">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=MXydRqRkQrhJo_2t7kx0v5Ns0vWe3oGkOaXfL3JVJ30nWJRb36yCFSzp_kLDBNAQagEhSXgxbKAr5Ci05Tk_5fMyZuIKZ8YISNEw-EbcC185D03qOdy6qGsydq2Wo_0EvMLZWqoVZBUnUDqwc5mUonsG1AJGqgYI84pZyQXWlDw9B5gvsJFKq0XvZT-oppxOPdZ8aXwhlIvlM7db5YybihdGrPJsQsj5Fkdtqat-UaW3RNzn0tRHUbNV4ym7X01AshWrz5kw4zglge0r78V6oCzQLTTRNcZvpbRzGB4CFvGm0sBP_gA-5Rh5MIXYyH5vdPXo9nQCe9EbAZvRkNNDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=MXydRqRkQrhJo_2t7kx0v5Ns0vWe3oGkOaXfL3JVJ30nWJRb36yCFSzp_kLDBNAQagEhSXgxbKAr5Ci05Tk_5fMyZuIKZ8YISNEw-EbcC185D03qOdy6qGsydq2Wo_0EvMLZWqoVZBUnUDqwc5mUonsG1AJGqgYI84pZyQXWlDw9B5gvsJFKq0XvZT-oppxOPdZ8aXwhlIvlM7db5YybihdGrPJsQsj5Fkdtqat-UaW3RNzn0tRHUbNV4ym7X01AshWrz5kw4zglge0r78V6oCzQLTTRNcZvpbRzGB4CFvGm0sBP_gA-5Rh5MIXYyH5vdPXo9nQCe9EbAZvRkNNDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چرا همسرت همیشه صورتشو میپوشونه؟
🎙
عثمان دمبله: همسر من یک زن بسیار مذهبیه، پوشوندن صورت تو اسلام اجباری نیست، اما اون واقعا بهش پایبنده گاهی بهش میگم که حداقل صورتتو تو جمع نشون بده، اما اون همیشه به من میگه: عثمان من میخوام فقط تو صورت من رو ببینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/103331" target="_blank">📅 10:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103330">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YovHjvjDzXCRIYspgEhEGa5h6shyw6GnXu6FM2TFvjR-5HCyehX1i4slngrEsxRD_sQiunU5vlcOYef_45zh_nq0BMXdFRRVpQjqhviWpRFgtJHy_Dw4nBG_1xgsHyIZ6fuSOzX27O--hHgd_JntOH6TtubEjDD7F9KhIuwNBPPor3rHvpPSt4KDzJTbIjGoJo-idTVBk0k_de6Z_E86d9jpcoUzCLlGTPYS77KL7dNYXWyjbp-CNhGCckCxqjaZQk5-LQaMyOe6xDJgiTJQ2hroKws4DFVNv4rCQj-lq1Yckq1q64RL7TbaMz2WPDMOzVyssyo2LjB4ahCn5_VUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
کوپه: ولاهوویچ می‌خواد به بارسلونا بیاد اما دکو و فلیک اعتقادی به او ندارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/103330" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103329">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103329" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/103329" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103328">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGupVjJGMuRQrEyiPekX36jgidDgOIo6xfglFSDQ0h9sqBQuqQVnAtyweOVV8BVy-Xy8IvSyTTJtMsrQinrwO4fCjs_pw4YnEB0t3cSiZmjiaBVILCfnHXPOD9kjEpKjOwE5prznT5NwY_jYuwKIwY7ZDvQfq91hlsVM4Rs0mmB88sksJbzcBzTbFTVhgmmNyEgjM5ZEMODXlOng6LkjmjWbcoGsEA6veCQNiS9eDL1Xfq9t1rWqFgcrTjuUFjXtUMMudtMJOd51UBre2EBRTSZwqfE0mttGwhdjVvsFbGWegPTQREZPEfC5oJjuVKf3IS3GqTFMCU-Yi6r6GgYTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/103328" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103327">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgZhv30MsOAkEEEQCG99S46GHdEAIQWOX5Dt0esVIK65VQrUpBt2_V3VIREahuercTg1st8YlNte4_dVg-g1dr_etJvj4NyKUOetSKEvo-Tddxij_N2q2NhbHGCvEKZVvty7_vkokHG94kiQhQ0rGOVcdpe0sugh6LziOYWeAIkcHFoRcjuKjFzAfYYoL3IQYTdYBnrCWN2bVuKcRQg85ufsW1BvR0rAE1SuEvXv2wVCA4_erfINDsA122TdkI2ot98RjBC9kji-iF7RCBvjlxlkkOQrKx_WZ3GA7PSjE7FkmfGnR6f7X-noHMNHLZBZUN_8y4I232QemGyE0QEF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔺
دیاریو اسپورت:
بارسلونا اقدام برای جذب لائوتارو مارتینز رو تکذیب کرده و گفته در حال حاضر لائوتارو گزینه جایگزین خولیان آلوارز نیست و باشگاه اصلا روی جذب او کار نمیکنه و گزینه‌های دیگری مدنظر هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/103327" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=aY069K8wvRyQxb-Jp_YUPu7MBU_T0W82umY1xhovvAWhEXLWa3q33Ssv1vT2xI3jTAYbxIEDrtzzLsACf3xXqg2je6eJ6Lm71_La_9wcPvIFl0AE1B4mN_jSQdA0CkgbzQosxFhHTVNwPqOX0xXyDAX7BupGSEFNCTyPHQllK2NusTBhyFsujTqXhKKXyORGoheKOEwolww5ifbSpSwWBUomIY14aCpo2pq4P73IFna9v6YbGhx_JIvMVqLGWNN9p4-TrMvpZbghT2SjSoQp_PJhXv3tw6-1hoZTsOvF8doWFbtHxftnHtRq9XwkjTLqXFEcmSVdvKfglk3dkMrHwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=aY069K8wvRyQxb-Jp_YUPu7MBU_T0W82umY1xhovvAWhEXLWa3q33Ssv1vT2xI3jTAYbxIEDrtzzLsACf3xXqg2je6eJ6Lm71_La_9wcPvIFl0AE1B4mN_jSQdA0CkgbzQosxFhHTVNwPqOX0xXyDAX7BupGSEFNCTyPHQllK2NusTBhyFsujTqXhKKXyORGoheKOEwolww5ifbSpSwWBUomIY14aCpo2pq4P73IFna9v6YbGhx_JIvMVqLGWNN9p4-TrMvpZbghT2SjSoQp_PJhXv3tw6-1hoZTsOvF8doWFbtHxftnHtRq9XwkjTLqXFEcmSVdvKfglk3dkMrHwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
😐
سقوط آزاد جرارد پیکه تو مراسم فوتبالی که دیشب دعوت شده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/103326" target="_blank">📅 09:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XATEdCgjFt5T5YipB_HrbkLXma-N25xQ-cSwAO_UNwP25l5wtpfh1Korn_y2cAEgB3rxRHmLjMoppgv0UTCYFhpbEo6xqjhAJPYNzuVNJCKp-W8G9Ezp2VfgrSopuPkltxUeWGmnZA2Yoy2EQpKGOL8aIOVo44Z2p_-m8qEwP1CZpurvNRO-hyUDQh0Kpx_6xInML9MCcRPxEH9YEn0K9RYfMv6_Zif4tUfl5mGeSQdqWtVqGymbER0v402-GAbsWVJIgMQ6p-f54RHMYT6Go0LX_156Wjjao5qPpkiWBkFqjsnko3m7jpqBh5dD1KeI6-7t1GDQG2Y4B00HNPuhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
در ژانویه ۲۰۲۵، بالای لوگوی پاری‌سن‌ژرمن هیچ ستاره‌ای نبود... اما حالا دو ستاره روی لوگوی باشگاه دیده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/103325" target="_blank">📅 09:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103324">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3hug-1SJCk9zkpNUbDq49Ir3r_TtgP6Raf4wXNzAGHldj-rIGvqu_WTelxCwxAtDwIlXuohGzq5YLgRNLk7vcOrteFbt8Twq559G6RforjR20u7fDAYIcM7qp9yDCE0NtI2leBan5fO740RWUlLatiuN8JfZQBFXtP5vz13xW7O5FaFXKQFk1RhUoLuPfS6erddcQ6xLW6pBzrv2b1t2M9_2nrgR1td1sjWGwJCGyXnxJroExNJ9bZJDHJw_1_I2BbM_KNC6MDlceRSohlsoMsej9ptB_89QPGWGMB7THT4czqUU35oFyFoH_wsLTc4DMilvDtviKIJdZParXoiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
اسامی داوران هفته‌اول پریمیرلیگ ایران
🔵
استقلال - مس‌شهربابک/موعود بنیادی‌فر
🟡
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
🔴
تراکتور - پیکان/کوپال ناظمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/103324" target="_blank">📅 09:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103323">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPLEvNcPuTKZghqE7_nI409Xl6eQdJ9qQ4epyCnzylldxjQjutGHjCGJmrfL0LcR-pHV5vlxieoa3mOgmtqHPanPxSczNJK-twurNJzaoA03uXlX-1xCvRfz1fiBhQP0sTUM_jEK-ltZQg-mWmOcz8ve19-1KBhkR491dO_YlJ9pb3eS30BMQEBas9b2krc5642KB6-14SiHAIZHgju0_TbrVrpX43y33gxPmZHXNHCDGSaB0fPBwbi-bXH6cmkrbxgu-CZXmb8TZ38o0ztyTHT2qe61emPZpLDSGxpzBpRKgBsKwYd7FQqRHTOV4ULIVI9IhCHdcCjifmDOig02QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
گلت تو فینال جام جهانی؟
🎙
فران تورس:
من 99 بار از 100 بار توپو بیرون میزدم ولی چشم ‌49 میلیون انسان به من بود و باید گل میکردم‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/103323" target="_blank">📅 09:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103322">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbfNON912o-xvns0VyuG1jVrnYRABlOlK9IHAS1412iTjoBntaH6XeG5pAn5b8dTQpOM2ygN-UXXQPBKRClMRQlufDmhcOeB5DN7Q6PMtU8n91j0ZHl-GRmjKqPZfuTvr82wXBEvwpsdiPOMIJPYTqhlXC8yl-kteZgCSvewTYxy-VkbvJvMTxhgPD1n_0cUiKfSJHD-4Im6eTotpcS76V_pCMngDeC9ucNC1R6vS79TE3fddOJriWNWWsajmkYWyS423qLsEiaBQJQt-dv6Q9QLIRM_IKiknTt9k7HCA8wgd3V78mP035WEWcTMFZOwblo9NwyW4e4zGUSTTJd-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
❌
پائولو مالدینی توضیح داد چرا پپ گواردیولا پیشنهاد هدایت تیم ملی ایتالیا را رد کرد:
مالدینی تاکید کرد که موضوع اصلا پول نبود؛ پپ بعد از سال‌های پرفشار و دیوانه‌وار حضور در لیگ برتر انگلیس، فقط احساس میکرد به استراحت نیاز داره و به همین دلیل پیشنهاد ایتالیا رو نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/103322" target="_blank">📅 08:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103320">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fppRHM7O28Q42v6Pq6W9rbLAE0GtJL5OGE012m0gDhnVvwuuIRFbCtNjwlpNJ9FUHSH11zLObvEnfk3qH-sPM6rh1cC9hL-l_tWwPo8GExdOyOZstJD7IVtVjpxWwlBO4nQPNmox5fgVAqYpx5AeztOq92jeqQdWRi_rkiUm2opezA-EDm3Fn-h0SBP244s1vYYjRAaMTh6BFhFNBKqaOItvuEmHzbpfET7zKC3PRkt1uz4KbJV9_rpe7XhlAkbbQxY0ClSAbrglRYhPFWbf5PEnM_YpvsBHNpn121Q6yf8Of2YKpqotGTESalG4OgoA8-s-ywRygJXrKKU5LbDxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewaOXQZ_OX8e26rRwoiArpo5UH0uwKx--vEhFmustJKoPm_kSDVlrPmH_H6Y6Vv147S7mgQhiUxavebXvHgm4X1DdDijtbUZzXptxL2Ec2UeO8L7arE1UW6wYJVWrVq5uB1CbvhHF_TiGCqj-SEtNThkdLdKaVv7AIZNd9aVvh6CHcH1YdHmwMJo4fu9g6_9WH7oojDDqlJ60zp3lM7aTYCUCVOyKrgqe_R4iudSLu_f9rqs5JQOcUFmh2hmtr4Uhht7BD3HRyIofTldeXbioMml_NEtf_Vu8DRsN9kg4A_54afin-11Ts2YkBIxs1n_Rvgmq15ryOGCztNv16H7sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
⚪️
کریستیانو رونالدو فقط طی ۵ ماه در هر دو باشگاه، هم آقای گل رئال مادرید شد و هم یوونتوس.
🔺
۲۸ گل برای رئال مادرید
🔺
۱۶ گل برای یوونتوس
فقط توی ۵ ماه حضور در هر تیم، بهترین گلزن اون تیم شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/103320" target="_blank">📅 08:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103319">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYeQWEKTwVJfmF-9zvEDibSy93-nO_M4AFXObeTp7ZyMEs0-h50KCh_P_eItYuWLYFJnYz0SApynal_VvlLYwX1mtvLv2lakOUWNVeclU_k31WqoKMQ8Q7G1JOEX6RrpYzO-lr5RqdGmrVt0y9Ef8LCkdnUlJFa_rZo52f8pLktucZdcKEXG9nHtn1yW-q8dXqVQX4e03qBBJcgxNAa-2W-Gck5hbLJF5GAr0DUCEroIlDJS5qJ3tmS0sdO3JReDWAeL5MyjZAxDQpEkLAx7PONK-REGdEkw3MKQpDy4EQBvT91jVNtpFxwra7fIwp8axoXyUbo867c1k6Eeb8Wl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
⚽️
ترامپ:
فدراسیون بین‌المللی فوتبال (فیفا) مرتکب یک اشتباه بزرگ خواهد شد اگر به هر دلیلی، به فکر جایگزینی رئیس، جیانی اینفانتینو، بیفتد. او فوق‌العاده است. او به تازگی موفق‌ترین جام جهانی تاریخ را، برای چهارمین بار، برگزار کرده است. اگر او برود، دیگر موفق یا سودآور نخواهد بود. از توجه شما به این موضوع سپاسگزارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/103319" target="_blank">📅 08:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103318">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-qq2MkViB9XND40kbUy2ImebWWaEZKkZiecwQN-arZn34s-O7J5u-5e0Jd2GKwJfageFwzYgzUSy2SjchYVKdZny_gluR0pkFL5qPaZFhjGrCdOF6YETVLhyTjSjloXRsjhSRGbWMiYwTlwVFn5mP__xYUjdx1FCQCy1ocJmEtpJq45n39tVvv3sEJOKmFGEaefnzvof_L8CbsAn0NTb4uQnnYe3GtpaO35b1UcHyfv529Hd98hmBq4HdZDmmWzPdGLX26jwYcKYUAYsqK68AwsgzAgy92DfHQstSZzUzCp8UcPj3UkvGSYqEE5aZiksjkhUF_-dLjm4tlX4TiI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
شایعاتی درباره رابطه لامین یامال با کِلی ریالس کونئو، مدل ۲۸ ساله کلمبیایی، در شبکه‌های اجتماعی منتشر شده، اما تا این لحظه هیچ عکس یا ویدیوی مشترکی از این دو کنارهم منتشر نشده و نه یامال و نه کلی ریالس این شایعه رو تایید یا تکذیب نکردن؛ تنها نکته‌ای که توجه کاربران رو جلب کرده، دیده نشدن اینس گارسیا، پارتنر یامال، در تعطیلات او در کلمبیاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103318" target="_blank">📅 08:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103317">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psD5f0DwmS9EF865rxB3ZVLZKAIUG9nHLlxqbAiG0y0xpg9-X0tkTq4N4O9MuqftWacFgvxfQRHir8gmuyrcLUhtn2EIBGkXtFLwRCTtpbbLqdgz4W1bjx1rmstZ7mVkRvG4WDsUmGQwbS6ajubammR39g3i_wpfZZvLF_xoN4smXKRytIGAJU0ES9AwtSmHCzx1t3-Tdquvy2Go1Y-qYsAeFtP8S8TQMyUnaTAYXOb0zD6YrjGUZUUk0VxXz9O6W8DFgTYy_Ff2NbCubRFMot8BOUWxprjCSUBxIRoCKgwjQUX06B72V0OErRUGwG4MPNrrtzJtYsCYT3uDVwtuJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
باشگاه رئال مادرید واسه فده والورده پیشنهاد دریافت کرد. اما خود والورده حتی حاضر نشد هیچ گزینه یا پیشنهادی رو بررسی کنه و از همون اول تصمیمش این بود که در رئال مادرید بمونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103317" target="_blank">📅 08:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103316">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49775a0c61.mp4?token=axWxg1_jN4LR10fkHX7-HeuO3WZyzZOudNQx7KJ4_HyVuUUJVjtcottLfXaeGwnF-FI6JoR9c4_K5qjpJzR4daQSDWiGZ2Nv6YA5HyLMsWmJhPQJR4VI8Cmf9TCLpBlrt1LWjF-NS3MF6Ipt_BevnvZ7NmxD03ARuP_s5hKyNC27eRs6CLeKJeIxS4mwOOn1HGU1FQZe1Ik-iKTRLGTkWHl3oAH0sW0fAVBKk0ZjIuBRTy5-Vh2BlXEs-xRX8RACHoGL1dGPSjOUZqtfpzOEQ9NQBfHFJ4o2zOe9A5tqdUuaMRv7G-dsM3pnbAa2sPnXpD88XCoeiL_OqJlILgY8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49775a0c61.mp4?token=axWxg1_jN4LR10fkHX7-HeuO3WZyzZOudNQx7KJ4_HyVuUUJVjtcottLfXaeGwnF-FI6JoR9c4_K5qjpJzR4daQSDWiGZ2Nv6YA5HyLMsWmJhPQJR4VI8Cmf9TCLpBlrt1LWjF-NS3MF6Ipt_BevnvZ7NmxD03ARuP_s5hKyNC27eRs6CLeKJeIxS4mwOOn1HGU1FQZe1Ik-iKTRLGTkWHl3oAH0sW0fAVBKk0ZjIuBRTy5-Vh2BlXEs-xRX8RACHoGL1dGPSjOUZqtfpzOEQ9NQBfHFJ4o2zOe9A5tqdUuaMRv7G-dsM3pnbAa2sPnXpD88XCoeiL_OqJlILgY8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
⚽️
رامین رضاییان: ما هم بلدیم تیپ های خاکی بزنیم به خدا ما هم بچه روستاییم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103316" target="_blank">📅 02:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103315">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eedc94ace.mp4?token=PkQ15jBVSkhaqgLh88FLW32e9v_6wHAC3ixT3jaUCU96ELR933Tvnvkaqtor6lPkmXbXzRsyJkKHqJ_cVPlimv4aRQHLM7hvZATr6nEcxUbIchROX7jRfe9m43IWLDQtrHbQlsCntOhTOMzokavEL6f-hiv-kmYoeYL5s9b2Z0vvrfe0amIG5IF7ChZAUccN0UTdyYmCJbgvuGD9DtRCocoDYuVSPby2LhWfsycb2w2fARiDCqRCOc81hg8WFnrzs17fqy759LcYssuMGjiShJds8lnSkkEqhXHSP9CMpu6YGULbNx9HH3dfgDkfgOxlQFmUE9X4_1f_UJfKK-zq-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eedc94ace.mp4?token=PkQ15jBVSkhaqgLh88FLW32e9v_6wHAC3ixT3jaUCU96ELR933Tvnvkaqtor6lPkmXbXzRsyJkKHqJ_cVPlimv4aRQHLM7hvZATr6nEcxUbIchROX7jRfe9m43IWLDQtrHbQlsCntOhTOMzokavEL6f-hiv-kmYoeYL5s9b2Z0vvrfe0amIG5IF7ChZAUccN0UTdyYmCJbgvuGD9DtRCocoDYuVSPby2LhWfsycb2w2fARiDCqRCOc81hg8WFnrzs17fqy759LcYssuMGjiShJds8lnSkkEqhXHSP9CMpu6YGULbNx9HH3dfgDkfgOxlQFmUE9X4_1f_UJfKK-zq-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
👤
رامین رضاییان: مذاکره با کادیز اسپانیا؟ صحبت هایی بوده است/  در 48 ساعت آینده تیم  جدیدم را مشخص خواهم کرد. خودم دوست دارم در ایران و هیاهوی فوتبال ایران باشم تا مردم از هیجان رامین استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/103315" target="_blank">📅 02:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103314">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
▶️
👤
صحبت‌های شنیدنی و تلخ این جانباز عزیز؛ امیدواریم برسه دست اسطوره علی‌آقادایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103314" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103313">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/103313" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103313" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103312">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJDWAH7sd3ANvAblyrBlip0qmV3A9urNQIXzeIYlTIzMbo_2m3PJ2yJbB9fjWjcR7wbGVHc9sPK3-4_H_QsU-Kl5J1QsfKZyB2sJplFsbwrw0mAS1AI2phu7yOSmhbHCKZaTIB1NO3OU0hA8VquSMzBIHEQejHdlbE3ArgjnPW8usVQD9bOh7WNGunwkUK3mlH2vzpFhCmTvBqyS8O5JYA9NccDe9P8aVlkXr53kcPXi-87iyPwvcUTQvUyG9JFsbc3o0vRrXhLFV38e8PmUxCZ7FOaaShVdFc2Ji74MRfXmuloiyMDK_p2Ikazr1RSZrAJK408q_HdtYqi6vSV_CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103312" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103311">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e8aa4ed3.mp4?token=P42nBBsJEsK7jmuif7v5IwYt07k9ixG-fslMjzHAmO7lMbhH-0dDBbvuEPb2KZwB0psFtKo21DwI3XQWn4aSXd2ux8pV2DETug0f0d9cb4VouM_5gD0GyhpzCFQ41QGMpVM54bzp66ioSmnuxGU2_Gmclz4cSBScYmJoARkF9xUItLBKCzkA3Qo5rFMaLgJ9HJJNknLMujsnoHn7oB7E0UTFR7bcbHdtoxJoXaFr67hG7WylP_9EZHEntODx-UmicwMzOEpudXXDGjOt77ioYtomlRbgMmdTivJVoYo14xrdM_cFp3VpvJZZUvdMJqsqVCztxHPkBTALWI-prLVMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e8aa4ed3.mp4?token=P42nBBsJEsK7jmuif7v5IwYt07k9ixG-fslMjzHAmO7lMbhH-0dDBbvuEPb2KZwB0psFtKo21DwI3XQWn4aSXd2ux8pV2DETug0f0d9cb4VouM_5gD0GyhpzCFQ41QGMpVM54bzp66ioSmnuxGU2_Gmclz4cSBScYmJoARkF9xUItLBKCzkA3Qo5rFMaLgJ9HJJNknLMujsnoHn7oB7E0UTFR7bcbHdtoxJoXaFr67hG7WylP_9EZHEntODx-UmicwMzOEpudXXDGjOt77ioYtomlRbgMmdTivJVoYo14xrdM_cFp3VpvJZZUvdMJqsqVCztxHPkBTALWI-prLVMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🔵
رامین رضاییان: مشکل با آسانی و حردانی؟ من برای یاسر آسانی آرزوی موفقیت می کنم/ من همه بازیکنان استقلال را دوست دارم. با همه بازیکنان استقلال ارتباط خوبی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103311" target="_blank">📅 01:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103310">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5-9t3pM1vzIyz8opMrDgz5UHC-9J87w6mDTKu7iiYhPHe9Hpc53gfnooI19hmSEqKHOpdE1bQotxxDQRIZWhQSjX9m5yGp9Wodl1W-hi5QwYbY5-QFg7PULO-tQGtXm-Kbz944CXYZ6VnlzNkAVPHcpoxq_O0UztJ57Ouwajda1EmB3QeZbloxh5VKW9FLCt8Ln9Lsfp9Lq_Dom0Pdzm6xoMMbBmilqz_z0cm81ofo4DFsr_ukciKjjEO3tGUKKgCp84CxY3ZyXohYOhXHXvK1bSLd4Oyaw9Uu5BsguGvROjKrzA2TDPvRrGi8sPtOGND6Evh8zHkXsSIxmbGx64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری کنایه‌آمیز لحظاتی‌پیش یاسر آسانی با صالح حردانی، هم پست و رقیب رامین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103310" target="_blank">📅 01:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103309">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b865ccd71.mp4?token=Q-IeXVs6wVCytKXLYpKExONTWVmDWmUdcM0gO8TTPh6WyqQ0u5RzGhRleifD1zeWKe0SGDqyKruuHmYa0Qcipmo4NVohTqO3Mds4U0ibcNDf7yQnVM_SzjqYwAtDDdu4tr7pMAzp0RIbNQTn6W0Rk8WlibgefIz7l9nsmWvJ6hhmkZlz_U2dl3yWAyRx_nbZQzuEvCTNBf9rdNxOB-WCUwFhMNrr0o6N3WV6cUwHV710Na64a4zRov9IFPJKt-s-lSdXGdw7H2ZWZJfWWXOav9bhjI1cuxYGwEADHgkgjY0TXQWtkRDU21ANess321JNJYblY-L-TEr2YrecB0tQ31MHX-kj4LXrpAa4KOlxHY9rYQBTf0Yd0VjK6Fk0FqVhezntH03di9VpW7hihj3X9iS1PyeHytTxwgR9kPa_Onh3I-30se2xPQPsepeP0X5K2ci5IP4cHBSr5WK-Yw9KZrViD6zy_d-VF6L9vH6bPQSJU62eTbcKeOR4goukh-kB6OefSEBvQFm3BQdyugO4RFoFdYnZvpRCSN0UCHPV1bBXAUmIMqWfwoh6r1Dnzkubs71Is_OeDylRAee0x_fVrXWhCydZw0DloxmqtXaFndQtCF4lOT3Vcl8FF91wqWDlZY0FK0wZZcYsSsYaG2bpsoUEJtKdL5IwqM36cTB-u6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b865ccd71.mp4?token=Q-IeXVs6wVCytKXLYpKExONTWVmDWmUdcM0gO8TTPh6WyqQ0u5RzGhRleifD1zeWKe0SGDqyKruuHmYa0Qcipmo4NVohTqO3Mds4U0ibcNDf7yQnVM_SzjqYwAtDDdu4tr7pMAzp0RIbNQTn6W0Rk8WlibgefIz7l9nsmWvJ6hhmkZlz_U2dl3yWAyRx_nbZQzuEvCTNBf9rdNxOB-WCUwFhMNrr0o6N3WV6cUwHV710Na64a4zRov9IFPJKt-s-lSdXGdw7H2ZWZJfWWXOav9bhjI1cuxYGwEADHgkgjY0TXQWtkRDU21ANess321JNJYblY-L-TEr2YrecB0tQ31MHX-kj4LXrpAa4KOlxHY9rYQBTf0Yd0VjK6Fk0FqVhezntH03di9VpW7hihj3X9iS1PyeHytTxwgR9kPa_Onh3I-30se2xPQPsepeP0X5K2ci5IP4cHBSr5WK-Yw9KZrViD6zy_d-VF6L9vH6bPQSJU62eTbcKeOR4goukh-kB6OefSEBvQFm3BQdyugO4RFoFdYnZvpRCSN0UCHPV1bBXAUmIMqWfwoh6r1Dnzkubs71Is_OeDylRAee0x_fVrXWhCydZw0DloxmqtXaFndQtCF4lOT3Vcl8FF91wqWDlZY0FK0wZZcYsSsYaG2bpsoUEJtKdL5IwqM36cTB-u6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: کوچک تر از آن هستم که بخواهم بازوبند تیم استقلال را بر بازویم ببندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103309" target="_blank">📅 01:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103308">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e54f7dedb.mp4?token=f2UN8WN7DVtVTohRGjw0eNaxHIevTnYNw1MKlkXRO8UiUgB4sFAvbG1-eTlC2UAhcQh7Tsf-R3txLBijW44uRldZe8eaxcZ0PiugTKA9EJjz1ROMaANjUqGqmyE3unFVfiYE73AWsJ2HDnI1ISzDqxSgO1hwg_FDW0HogNUKg9KMsRSHHC_9VaRrqKFuvXfEwwf5NNrRJJzUSSxTnoAE568CxMgk_bRfMInmwwkHqxJteFcPr4zavUmNYhvhtB_4766OGQks3R7r2DC2aT01sGVr2o9fmb8lBt6Ijc_lsRy3A97EI7MPfPyo-Yp4Q83Gcl0MHi6ZfHvDXvVviz7HIboVM2jmoe25hC67ObitSXYOSrOARAIcgXR5Qbl7SXuX795pUfCduqgnVoBIfM2Hb8fVor0k7Vmi0s3p-bE0Eu7P9O5txN_lPYNqev1_maiUxn4WFhajdoz-YbgDqlYniLlsCVmPeBaN49fsxxJgCgCLNtj_1MfUstb9AZAgTnxHdRHt9YwqbLCtK19mNCSHk5P48yQhIgmi-VM53eB4CJ2oqaaVGYmx1S1cvI9XQTZSJl3JPHyY_aqlH287QgzbWVqL5oY1yY4op2HNZd5g26leU_gWHrQhecj1S7l-c1TcQNDAe7LATfVbgqdTbLd3ilYiMtUVMIpTfJYuDSeRDnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e54f7dedb.mp4?token=f2UN8WN7DVtVTohRGjw0eNaxHIevTnYNw1MKlkXRO8UiUgB4sFAvbG1-eTlC2UAhcQh7Tsf-R3txLBijW44uRldZe8eaxcZ0PiugTKA9EJjz1ROMaANjUqGqmyE3unFVfiYE73AWsJ2HDnI1ISzDqxSgO1hwg_FDW0HogNUKg9KMsRSHHC_9VaRrqKFuvXfEwwf5NNrRJJzUSSxTnoAE568CxMgk_bRfMInmwwkHqxJteFcPr4zavUmNYhvhtB_4766OGQks3R7r2DC2aT01sGVr2o9fmb8lBt6Ijc_lsRy3A97EI7MPfPyo-Yp4Q83Gcl0MHi6ZfHvDXvVviz7HIboVM2jmoe25hC67ObitSXYOSrOARAIcgXR5Qbl7SXuX795pUfCduqgnVoBIfM2Hb8fVor0k7Vmi0s3p-bE0Eu7P9O5txN_lPYNqev1_maiUxn4WFhajdoz-YbgDqlYniLlsCVmPeBaN49fsxxJgCgCLNtj_1MfUstb9AZAgTnxHdRHt9YwqbLCtK19mNCSHk5P48yQhIgmi-VM53eB4CJ2oqaaVGYmx1S1cvI9XQTZSJl3JPHyY_aqlH287QgzbWVqL5oY1yY4op2HNZd5g26leU_gWHrQhecj1S7l-c1TcQNDAe7LATfVbgqdTbLd3ilYiMtUVMIpTfJYuDSeRDnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
رامین رضاییان: من یک سال برای پرسپولیس رایگان بازی کردم/ برانکو من را نخواست
سالی 2.5 میلیون دلار از الدحیل گرفتم/ دو ماه حقوقم را بخشیدم به پرسپولیس بروم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103308" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103307">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926f821e41.mp4?token=X5ifASQYTuiV2omNRkOffyOFNFs5IClu1aintcDWZx10a3icteYM_8lEFkqZxX1OscY8UZWLEytT10EHd9EQFmxRfYCMKBWi7lBBzvbOfLKo77Q_0QQ0N7-tIGMgsRViJqMQ3VvKQOiJvBPNNJTGewknviofFa2cWoKcqtzl9QJEKPj6fyO9e_B2NKUB_FadP9dmmU03pCpzHElgx9LkO3pA0cuV8zMojz0l1JhXJCQyMKqj_2ILjM8lt6L97PUZHHITdMzJLKzqBAhYl3rZEPcjJYCHDMgG25bYFxmtSvmgC3W-9RPfcPZKcBM_Ew_i7aIQvJ1kg90fMPrv3TqkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926f821e41.mp4?token=X5ifASQYTuiV2omNRkOffyOFNFs5IClu1aintcDWZx10a3icteYM_8lEFkqZxX1OscY8UZWLEytT10EHd9EQFmxRfYCMKBWi7lBBzvbOfLKo77Q_0QQ0N7-tIGMgsRViJqMQ3VvKQOiJvBPNNJTGewknviofFa2cWoKcqtzl9QJEKPj6fyO9e_B2NKUB_FadP9dmmU03pCpzHElgx9LkO3pA0cuV8zMojz0l1JhXJCQyMKqj_2ILjM8lt6L97PUZHHITdMzJLKzqBAhYl3rZEPcjJYCHDMgG25bYFxmtSvmgC3W-9RPfcPZKcBM_Ew_i7aIQvJ1kg90fMPrv3TqkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: چه کار کنم که سنم 35 سال است ولی اندازه یک بازیکن 25 ساله دوندگی دارم؟ چرا همه زوم شدید روی رامین رضاییان؟ چرا می خواهید فوتبال من را زود تمام کنید؟ چرا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103307" target="_blank">📅 01:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103306">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f842dcdc91.mp4?token=PkPr56PjzE5embj2yOsMKmASu6qpOQfXAVgO30H2RMDHtqJPKBr5VnNUhmbYzdPUKeWX-5IRJ50WloSBCdW0qEWFrS5ISm4R791d1S1FBEXlFaZ05zoLmDXBVBr9f4Vm4g7jYlR6_ohd4p-15S2bDyDH57z155sK7ulBnza22JBvXQHrrGRacYmjpQfnd5tWUnKVvs9Bqd5MAiQ0Ge1FXhZvbalgdg_EBdSZfa_raHhNB3UW1YzZW8Ft-oTEUOHQt4bcyGUEe2VWSMNNTjT9p8T6sD8NqAOlO56KqsaleDXxA2mlCV1z__yZVTp81nE_xxbfuWCIqtkoe5uNuedHUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f842dcdc91.mp4?token=PkPr56PjzE5embj2yOsMKmASu6qpOQfXAVgO30H2RMDHtqJPKBr5VnNUhmbYzdPUKeWX-5IRJ50WloSBCdW0qEWFrS5ISm4R791d1S1FBEXlFaZ05zoLmDXBVBr9f4Vm4g7jYlR6_ohd4p-15S2bDyDH57z155sK7ulBnza22JBvXQHrrGRacYmjpQfnd5tWUnKVvs9Bqd5MAiQ0Ge1FXhZvbalgdg_EBdSZfa_raHhNB3UW1YzZW8Ft-oTEUOHQt4bcyGUEe2VWSMNNTjT9p8T6sD8NqAOlO56KqsaleDXxA2mlCV1z__yZVTp81nE_xxbfuWCIqtkoe5uNuedHUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
رامین رضاییان: مگر می‌شود بازیکنی مثل من اخلاق نداشته باشد و 8 سال در تیم ملی باشد؟ چرا دل من را می شکنید دلم شکسته است چرا من را جلوی هواداران می گذارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103306" target="_blank">📅 01:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb1415693.mp4?token=diMpynJ1E0a5Zch-l4OZQMqodZxRp3F9grQS49wjzi3MeZ4tXqpNeDNmYThXqEko0BJkXL7UmEfWq2C6XNhN4fmoDNy0_2TMRy-o6pnr3xEYa6f5fJ97wkV5gykPnRxFz0lVu2HyaZfDl43QeWvIw8nAE0IdmmAHreFR9IWDOKJ-SyR6dsdAsJI9mFolQS2rmo6ETCqTdxMGzWrEB76oDY-hbiBEaVXsWAWEklbR_t-y4yYDV3-PeP5838_FimXeJUKz54oo06WHztJTf7u-bJfXvX0pcpE7SKM_ipKpxmLgVfPuxVsSc6wzZIyG2GuXXVtMIigOZS9HcTf5wRcpfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb1415693.mp4?token=diMpynJ1E0a5Zch-l4OZQMqodZxRp3F9grQS49wjzi3MeZ4tXqpNeDNmYThXqEko0BJkXL7UmEfWq2C6XNhN4fmoDNy0_2TMRy-o6pnr3xEYa6f5fJ97wkV5gykPnRxFz0lVu2HyaZfDl43QeWvIw8nAE0IdmmAHreFR9IWDOKJ-SyR6dsdAsJI9mFolQS2rmo6ETCqTdxMGzWrEB76oDY-hbiBEaVXsWAWEklbR_t-y4yYDV3-PeP5838_FimXeJUKz54oo06WHztJTf7u-bJfXvX0pcpE7SKM_ipKpxmLgVfPuxVsSc6wzZIyG2GuXXVtMIigOZS9HcTf5wRcpfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🙂
رامین رضاییان: روزبه چشمی 7 روز پیش با من تماس گرفت گفت چه خبر؟ گفتم هیچ کسی از باشگاه استقلال با من برای مذاکره تماس نگرفته است، روزبه گفت من شب با آقا سهراب صحبت می کنم خبرش را می دهم، هنوز که هنوز منتظر زنگ روزبه هستم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103305" target="_blank">📅 00:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853e2a52d7.mp4?token=hRW2JVErErgt8p3lxrS5G_Bri3LYmY1Lxnq0jI0TuADwoaCbX1mwBqLYai385Bs8qHlBAGwI_coOcc2Z-aSTeSER4wiWVY2FGgL_WxQNGKilimJzpprypb-TpHHZeay3AzdcY4KPPUqOsJ7IJKa2MoooE_OA9uOT14k5xXy0m-aEkedbMQsl4VAnRRJLKmXxuytmKczaySGH_tX0Vti-WZJveY3d9XfSPgEZ49vQiQPJgg9Y7iGGy24nKgOk3SGA_0DKtVd51jyTY8ZSvIBzTyIEbxzMcltM9V3mWptaopX37lMknbWI-evPHAmMVenjzWlyrqP70TLrhwljEZFbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853e2a52d7.mp4?token=hRW2JVErErgt8p3lxrS5G_Bri3LYmY1Lxnq0jI0TuADwoaCbX1mwBqLYai385Bs8qHlBAGwI_coOcc2Z-aSTeSER4wiWVY2FGgL_WxQNGKilimJzpprypb-TpHHZeay3AzdcY4KPPUqOsJ7IJKa2MoooE_OA9uOT14k5xXy0m-aEkedbMQsl4VAnRRJLKmXxuytmKczaySGH_tX0Vti-WZJveY3d9XfSPgEZ49vQiQPJgg9Y7iGGy24nKgOk3SGA_0DKtVd51jyTY8ZSvIBzTyIEbxzMcltM9V3mWptaopX37lMknbWI-evPHAmMVenjzWlyrqP70TLrhwljEZFbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
رامین رضاییان
وسط برنامه پا شد لباسشو نشون میده میگه ببینید بخدا نه مارک نه هیچی، منم بچه کف خیابونم فقر کشیدم، ببخشید اگه یا تیپ و استایلم دلتونو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103304" target="_blank">📅 00:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0631b46480.mp4?token=WJz4x95NOfMtaEQFWuXdwcZhLazax2ggYC9ba1NU2HhIq04W9w-zTqRl6Ld2Ay3Y7svwHyAcoyUc-IXoLvEbx6nmVmxgYIAmAaMPmd3QlhYkCh4CPyNx3uiVx6g8E4WutUb86M89_YJe17n2IpsAvY22HGAIvxhhPJvF8zIx6UXEx0T2W1lYNb_Vx4Ekf3WOCGCGPUANVh-AfU5iGntVrSnnUXhVQLG8TKpcfclxiTlWIEaXnt98qb_MYwyxkMrYxNofVLN1H8MA0vNrIeZp3KMvRZLgCMBgeRL8ruXJFSDIuFzNPVQVkKnwZuh15gceEJDKXe2zX2UACJ0JmBCiig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0631b46480.mp4?token=WJz4x95NOfMtaEQFWuXdwcZhLazax2ggYC9ba1NU2HhIq04W9w-zTqRl6Ld2Ay3Y7svwHyAcoyUc-IXoLvEbx6nmVmxgYIAmAaMPmd3QlhYkCh4CPyNx3uiVx6g8E4WutUb86M89_YJe17n2IpsAvY22HGAIvxhhPJvF8zIx6UXEx0T2W1lYNb_Vx4Ekf3WOCGCGPUANVh-AfU5iGntVrSnnUXhVQLG8TKpcfclxiTlWIEaXnt98qb_MYwyxkMrYxNofVLN1H8MA0vNrIeZp3KMvRZLgCMBgeRL8ruXJFSDIuFzNPVQVkKnwZuh15gceEJDKXe2zX2UACJ0JmBCiig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
رامین رضاییان: من قراردادم را با استقلال فسخ نکردم؛ باشگاه استقلال با من فسخ کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103303" target="_blank">📅 00:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0b3587c2.mp4?token=mhSqmZ9XGxNvXYLrnckz7F504krV99X2br9cu2MrYBru5QQGaYBzunyZGjJnAQa0v-p_n9FlmENmecDOqdzZxeEyymUa7GtbLvNGX4WPHN3-O9wRZCOdvHJ5FVy49zFXaldCR2XLU35oD2Amw_Zq0yvVg3DZbiLxjHQRoKqFBcMZIEqbtJJkEwPfr7RaxBrPg3ywNGD1pq5gYH4pcMheNaHEOQ3diEsiUHjkrvBtkPZewyF0pT7uwxuzRNARPmgJlbJyYsvGjcWb0OygfYxauCHIW8ocnSQbxkzCjvbl94HAiSITQChz_nAFS1JExfVv5nwN_l5ck5TwoaLDdtHfuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0b3587c2.mp4?token=mhSqmZ9XGxNvXYLrnckz7F504krV99X2br9cu2MrYBru5QQGaYBzunyZGjJnAQa0v-p_n9FlmENmecDOqdzZxeEyymUa7GtbLvNGX4WPHN3-O9wRZCOdvHJ5FVy49zFXaldCR2XLU35oD2Amw_Zq0yvVg3DZbiLxjHQRoKqFBcMZIEqbtJJkEwPfr7RaxBrPg3ywNGD1pq5gYH4pcMheNaHEOQ3diEsiUHjkrvBtkPZewyF0pT7uwxuzRNARPmgJlbJyYsvGjcWb0OygfYxauCHIW8ocnSQbxkzCjvbl94HAiSITQChz_nAFS1JExfVv5nwN_l5ck5TwoaLDdtHfuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: آقای تاجرنیا با وکیل من صحبت کرد و گفت من رامین را دوست دارم ولی..
میثاقی: ولی سرمربی استقلال رامین رضاییان را نمی خواهد
رضاییان: خب این را نمی توانستید تلفنی به من بگویید؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103302" target="_blank">📅 00:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66453415a0.mp4?token=Mk4z1U_foTZsqJkl-FTY4VUK4ttTkau36qCw8gQEOmYRJOUCPF28kQYvj3m9Hbu-VpO-6cGlRE30_kw6ESMyYl4XD92RYOJJij_7IVVR5AdWEeenIvpulsMKkpo8YPxPDN3OcuFcEFT6rzGYyB9Vb3L1n1P331-YmTglStq-1IMgA5drKpoI4huRgNlLcexNtH6B6tDM9ZWpx5l5ZtaY-PRemqviUmHKEkbAoD4lyyQFwCv2swQsg7Kyno7IXjxLRimDi47E1LP7BTlZTcNDuXp1c6aK0nd-DaZ-l9CYsaZVcbkLftcKPte8yz42AGDEToAJhNyTMpkQcSUi5qyhWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66453415a0.mp4?token=Mk4z1U_foTZsqJkl-FTY4VUK4ttTkau36qCw8gQEOmYRJOUCPF28kQYvj3m9Hbu-VpO-6cGlRE30_kw6ESMyYl4XD92RYOJJij_7IVVR5AdWEeenIvpulsMKkpo8YPxPDN3OcuFcEFT6rzGYyB9Vb3L1n1P331-YmTglStq-1IMgA5drKpoI4huRgNlLcexNtH6B6tDM9ZWpx5l5ZtaY-PRemqviUmHKEkbAoD4lyyQFwCv2swQsg7Kyno7IXjxLRimDi47E1LP7BTlZTcNDuXp1c6aK0nd-DaZ-l9CYsaZVcbkLftcKPte8yz42AGDEToAJhNyTMpkQcSUi5qyhWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🟠
🔵
رامین رضاییان: رفتنم به جام جهانی را مدیون باشگاه فولاد هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103301" target="_blank">📅 00:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c728b778f4.mp4?token=LyszOOa9c3RHobNXxCknnEuIxbHWUXDuqnBZdsK2VzsLP7aiOYvIHJA5THpd89v2Ig50RdFKmBf_J0ncIC8Q9Muc47e-uDLgHtaoOv-Ft07XvLHGpaBxHnSK_YopH5XcNPlGb-DX4m5PlmrcTYwqrl8bjQT7xPBuRWcqZpFPEaQeWs69rsOELMxq8P1twKvl41_R9XZYt6qxAs25m5ASSs_gmedwC0MdAQZkD3imDFO7_-td-ASHADf_gzzb3cfgNV4k-0IP73J8EcDIitCXGpc41DbKEnXKtypg_-Qq1OseDaDEMzKoe2uj1wsdwUI1aRHqr5USsB0Temp1cCUuuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c728b778f4.mp4?token=LyszOOa9c3RHobNXxCknnEuIxbHWUXDuqnBZdsK2VzsLP7aiOYvIHJA5THpd89v2Ig50RdFKmBf_J0ncIC8Q9Muc47e-uDLgHtaoOv-Ft07XvLHGpaBxHnSK_YopH5XcNPlGb-DX4m5PlmrcTYwqrl8bjQT7xPBuRWcqZpFPEaQeWs69rsOELMxq8P1twKvl41_R9XZYt6qxAs25m5ASSs_gmedwC0MdAQZkD3imDFO7_-td-ASHADf_gzzb3cfgNV4k-0IP73J8EcDIitCXGpc41DbKEnXKtypg_-Qq1OseDaDEMzKoe2uj1wsdwUI1aRHqr5USsB0Temp1cCUuuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🟠
رامین رضاییان: آقای گرشاسبی مدیرعامل فولاد برای جذب من با پای خودش به باشگاه استقلال آمد شاید هیچ مدیری این کارا را نمی کر
د
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/103300" target="_blank">📅 00:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103299">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN70E0Mkjf04gjdbkVeOpv-AA2tW5N3Z-vvCB_XsLM35dKeaMSvzUqpnTBP8lhxtUHDbEOz3LAbr19a0V3CtxoxyiEmp9SlvWsQ2mL56NDkf1fttsNywLCV8N7zbfrWtFOYFB5mlr7OL7tYBg1VN3YON--SVamqDwMxIO7uTFlwcuPKTw9A4E4SE2pAoRidGv0Xndtrmt0ddiOx4Tg2UmebjwYXjO6Fw3JEYKZYo_DfUMauvtW-Yw-H6ih67xqiRyDA5b-3pD9JkYka4wcPvQmaehfb0AB_vvTW2vOLCKfCdRJmYdn-8wUbAoL7e5B_oWfRqrgnfhVYcK0L6pYLCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
#فوووووری
؛
🔺
هلدینگ‌خلیج‌فارس اعلام کرد که سهام باشگاه استقلال بزودی به چند شرکت یا شخص متمول هوادار آبی‌ها به فروش خواهد رسید. مذاکرات در این زمینه آغاز شده و بزودی نتیجه نهایی به مردم اطلاع‌رسانی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103299" target="_blank">📅 00:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103298">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9ef8ef85.mp4?token=pb3sZVNeopqPSLvNcUTOkbbhh6PuKphWJk4v2lx0vR0xhlExFmFGcZK_pb7e91nQxg4dWNri0CPGP98tm4tCjFBGad1XZq0es0KW52L1dz7JuRg1KkJBnXhXHxT36RYQazPySXqz6SZRcge5Fz93bxZNL-Cn-9m-VJZWlMemDfFW3ybrwGJL_jsDEY1fI7VEnGHSmU9Uj4Wso2C7quclJai0gun9Te8aug_dgqEBjvI0yc6Kr4-6RvpftGHIWdMwYA2drbbhkqIX5Mgs1xnsVJKNjISilHhxlhIQ7000_uSeSoLXCkJlyCg53-K-dqkn2wYBaBR0yEjugzlEZkTFOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9ef8ef85.mp4?token=pb3sZVNeopqPSLvNcUTOkbbhh6PuKphWJk4v2lx0vR0xhlExFmFGcZK_pb7e91nQxg4dWNri0CPGP98tm4tCjFBGad1XZq0es0KW52L1dz7JuRg1KkJBnXhXHxT36RYQazPySXqz6SZRcge5Fz93bxZNL-Cn-9m-VJZWlMemDfFW3ybrwGJL_jsDEY1fI7VEnGHSmU9Uj4Wso2C7quclJai0gun9Te8aug_dgqEBjvI0yc6Kr4-6RvpftGHIWdMwYA2drbbhkqIX5Mgs1xnsVJKNjISilHhxlhIQ7000_uSeSoLXCkJlyCg53-K-dqkn2wYBaBR0yEjugzlEZkTFOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
✅
رامین رضاییان: با جان و دل برای استقلال زحمت کشیدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103298" target="_blank">📅 00:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103297">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcad8628a9.mp4?token=O63_h8lPlTT6Hmi3qPcpwj-ars_Si6nUlamsvdz3IDw0rrGdqCmCbrimH31UgDRC-Gw7BDtiwqW-9eUSKEsVx8IkoH59dF7RNe7WEnZ4g3K7S8MEwEyLCvY1_o8re03nnZ80XtfiXpTnwmlyZagCQm_bSehEXuDSYOcX0X8DP6-80mEaONWSmAaSeis_Ci2rSzlkbU2-CSD6-zyPxtSNYRXOlv8kIjfXAdRwnmczKwaRLJuGnKBe1xQzzvGrFgiVW9JfWhNAdVZUXoKe_U1EbWV7PaJ8Px5m9bzv7KcGDSh2MkoSI2rx5cpRgiLBjNOHF_TDr3zEpy7nYUN9sWmf_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcad8628a9.mp4?token=O63_h8lPlTT6Hmi3qPcpwj-ars_Si6nUlamsvdz3IDw0rrGdqCmCbrimH31UgDRC-Gw7BDtiwqW-9eUSKEsVx8IkoH59dF7RNe7WEnZ4g3K7S8MEwEyLCvY1_o8re03nnZ80XtfiXpTnwmlyZagCQm_bSehEXuDSYOcX0X8DP6-80mEaONWSmAaSeis_Ci2rSzlkbU2-CSD6-zyPxtSNYRXOlv8kIjfXAdRwnmczKwaRLJuGnKBe1xQzzvGrFgiVW9JfWhNAdVZUXoKe_U1EbWV7PaJ8Px5m9bzv7KcGDSh2MkoSI2rx5cpRgiLBjNOHF_TDr3zEpy7nYUN9sWmf_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔵
رامین رضاییان: در استقلال تنها ترین بودم. ساپینتو سر تمرین راهم نمیداد به همین دلیل در خیابان تمرین می کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103297" target="_blank">📅 00:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103296">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08091e808e.mp4?token=Obnqvbqhy7xsPwxNRjJrgq-iGu4nCIIcup5ro0lnnZ3yYkyEJqVkWj3h0Xl7AXCx7hiwOxlgYibitRzww_J_aPYH0NSANF358lzSFvs7wQMrWuEXKzX4TvXpadz8fn9iv_VzEjipkELFzc62FRaF1ltFwFw4xij_rpYCvt8evrWveXFKaQ4vkLVk9lOLMQclLWaZ_XDkTbX6ZkPaKfwnAXOq4HLgHMH-oF_KoY57a6sMItRKSEnvDuNv9evITtQda_0l-q7QtffoAjfW0tEL6wwW5VQHt-cD07vbzBrXJ9V6KeM7oKWEnv94t8WJYR-bKE5nnFuybxkmwZ_2Db7ruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08091e808e.mp4?token=Obnqvbqhy7xsPwxNRjJrgq-iGu4nCIIcup5ro0lnnZ3yYkyEJqVkWj3h0Xl7AXCx7hiwOxlgYibitRzww_J_aPYH0NSANF358lzSFvs7wQMrWuEXKzX4TvXpadz8fn9iv_VzEjipkELFzc62FRaF1ltFwFw4xij_rpYCvt8evrWveXFKaQ4vkLVk9lOLMQclLWaZ_XDkTbX6ZkPaKfwnAXOq4HLgHMH-oF_KoY57a6sMItRKSEnvDuNv9evITtQda_0l-q7QtffoAjfW0tEL6wwW5VQHt-cD07vbzBrXJ9V6KeM7oKWEnv94t8WJYR-bKE5nnFuybxkmwZ_2Db7ruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🔵
رامین رضاییان:
🔺
واقعا استقلال برای من یک تیم ملی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/103296" target="_blank">📅 23:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103295">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ddc57b23.mp4?token=r1n5X7YXnItSbKqoZjAvhsJ8tBEgfFXTU4KqyV5datMRX2FqHtG5ZYWvFsM_peg1LYoUdKf-H9GK_8dkymKeS22OXxtHA9_pMCVdgxFZtIEPloUcxrc2YlLDSbsuIe6qn5o8CG649RfQyMzDwEjQ1bXtRk1aHsZeDRbJZjs5Xto0dR5V6-l9sJxcHvHPZd-OZtQy8w_kMJXtgcBoZOTTFEsRTfYFSwyH2orKeUGgOoubJChqhIJK0kjOzXVE86-9DoLxky5YPywWR1uHw6oIkblg6EOevkuVeJ_uXck2us4VWRtSdtgbTwkiSXuUQzVqhnIb3E9_sw9000NA2QonZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ddc57b23.mp4?token=r1n5X7YXnItSbKqoZjAvhsJ8tBEgfFXTU4KqyV5datMRX2FqHtG5ZYWvFsM_peg1LYoUdKf-H9GK_8dkymKeS22OXxtHA9_pMCVdgxFZtIEPloUcxrc2YlLDSbsuIe6qn5o8CG649RfQyMzDwEjQ1bXtRk1aHsZeDRbJZjs5Xto0dR5V6-l9sJxcHvHPZd-OZtQy8w_kMJXtgcBoZOTTFEsRTfYFSwyH2orKeUGgOoubJChqhIJK0kjOzXVE86-9DoLxky5YPywWR1uHw6oIkblg6EOevkuVeJ_uXck2us4VWRtSdtgbTwkiSXuUQzVqhnIb3E9_sw9000NA2QonZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔵
رامین رضاییان: وقتی به استقلال آمدم به شرافتم قسم خوردم که با تمام وجود بازی خواهم کرد و خواهم جنگید/ واقعا تا زمانی که در استقلال بودم هم جنگیدم هم بیرون از زمین تعصب این تیم را داشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103295" target="_blank">📅 23:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103294">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXVhQ0h8dAbogmDFfkrAH5KfHCwImyDcSMQ1xsZyFQDdbsMuHjlRGgGhIgRQm0xl6SDqiwYiPxT5urIqvtSJd8nShS5xTG2R1S9tHsLBjZ9Vr3kI_hXg6Lt75P-6_L7vROyY9FWNPrDtkYiaRpDHW8jq2a-HTbCGoFcafZWRe0S_O9kH-T9wiyH_4cmMSt4gwWMba1ZNJoKS0d_kERR8EEU1sGxlKYZhQd378pQT0qksp2awl925bhqnU4BRHjIUl3bA3mzgaQplguLTXmnqZrvKX9XG6fJb-Ijpmih4P4slfg1PcTfW7BZKux-tUSwSgtTh5tp3GIJNs5ysjtkToA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
🔺
خوزه فلیکس دیاز: اندریک در رئال ماندگار شد و جدا نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103294" target="_blank">📅 23:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103293">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29c3e62b2.mp4?token=Q7Fe_dooS-RiBqKvOmAkz51t3Q2B_S-kobvscZFkWafIxPi7Zd0uaXHc2u73IXdPUUZxvz8KhtmOjPD0-hnWRo43RaUbJAlqqpiCcEnynlwapFRY7y1Codvcmw69g_2aTI4oSXNCRH-OABOu_OeRM28h2leYhwn2y5H59oWWqUNdVN3djFIToz0iey-GjUesu-S0U0dpkRJ_wH_T2RRsugu1Wz4oR9au-YLPTmBSYw0Gr1BHN0XUn-auKpidGIVuAwTXeZBeOfHOwYSJ-mwqPf36iL8m-T52q6CEsu7D3VZngf81GgRo3ZXMC7bmGU5aBYZYkn2OCo3Dz5elAEBnog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29c3e62b2.mp4?token=Q7Fe_dooS-RiBqKvOmAkz51t3Q2B_S-kobvscZFkWafIxPi7Zd0uaXHc2u73IXdPUUZxvz8KhtmOjPD0-hnWRo43RaUbJAlqqpiCcEnynlwapFRY7y1Codvcmw69g_2aTI4oSXNCRH-OABOu_OeRM28h2leYhwn2y5H59oWWqUNdVN3djFIToz0iey-GjUesu-S0U0dpkRJ_wH_T2RRsugu1Wz4oR9au-YLPTmBSYw0Gr1BHN0XUn-auKpidGIVuAwTXeZBeOfHOwYSJ-mwqPf36iL8m-T52q6CEsu7D3VZngf81GgRo3ZXMC7bmGU5aBYZYkn2OCo3Dz5elAEBnog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
از مهدی‌تاج: احتمال دارد در جشن برترین هایی که قرار است برگزار شود جام قهرمانی به استقلال داده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103293" target="_blank">📅 23:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103292">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCY-1ehmcze0Z8K2EzFz37kg3eFfgCzu2nxQ-iCobrReH943pz_RDL3Hc5xwYw1x76jtWFnCBWDPaRuPjrAWLunFROQJ7dksjc2WRowzoyx-TwLTowHcOIESE5K6BS7dw6xW38OG4B9ueNPhKPOfkOVl92VFz1US_aev_ap_fS3qODyEENpzVv4WhXaSdTp20TdMU3V-gB3g24W7JzTeIAMUpV3900dw5F7_rpXBMw-tFKEuX7gpomkKLTSoanqxFw8dBYKJaPEagzIIleoBphOXVsCMM-RJ8n0cmTg72NoB_FYhiz5L_1dKnd4f2eq9vLEw5w2iNWLfNVLxLLBSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ قرارداد میکی‌ون‌دفن ستاره هلندی با تاتنهام انگلیس تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103292" target="_blank">📅 23:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103291">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec95bffbb1.mp4?token=nZFL94Mzf-akqYkifPF7LVh5UXI-D_n2eN0S1k6d1e3fXNYhf-OvzeEkim_Asp26i5RyOm6MxMgoBeyUU6PHnm0DUKLzAFShywdDNvzS5mQ_IraHGXL8rlC6nQ_yOx2eU3vAXwMnL3y0sowh4rkINhjewl110kXpDjt_zkHcl7hAv8AIN9z1T3L5C5Vu0-mssDSs6Xr5rlQ8EJq1Y4yW4jShml52L_FWANXPnq67OmTHozIIhNKOMscknxHCfpP81csm5sF8xwlEDzWT06HBPsUWB2R_LRhVx3vEAMCMwC47CasAdQY4PJLxv8i-DffHLuQIHavj28KNI2rRf3LlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec95bffbb1.mp4?token=nZFL94Mzf-akqYkifPF7LVh5UXI-D_n2eN0S1k6d1e3fXNYhf-OvzeEkim_Asp26i5RyOm6MxMgoBeyUU6PHnm0DUKLzAFShywdDNvzS5mQ_IraHGXL8rlC6nQ_yOx2eU3vAXwMnL3y0sowh4rkINhjewl110kXpDjt_zkHcl7hAv8AIN9z1T3L5C5Vu0-mssDSs6Xr5rlQ8EJq1Y4yW4jShml52L_FWANXPnq67OmTHozIIhNKOMscknxHCfpP81csm5sF8xwlEDzWT06HBPsUWB2R_LRhVx3vEAMCMwC47CasAdQY4PJLxv8i-DffHLuQIHavj28KNI2rRf3LlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
میثاقی: ممبینی مگر هافبک چپ است که با تیم ملی به ترکیه رفته بود؟
تاج: حالا دیگر رفته بود که کمک کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103291" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103290">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/586f4ea605.mp4?token=fwdEuIkBanA9nBs-CSIiOKb3xTWS_ImxDL7bl75wI4Rd2dzlBbuBQJp4PLi2KaivkOyQ3jYfEIDd3NA1xWkwHwexdmWfKAj2kdWdDMEMXlLVrJ0ckZHVMWoUa2VnywCcQdyc0bU1-B6c267ahzn2mDmHAK64c7M-L_N9fdEo58ZdvEM-GO-S9e-xqRxQEssfQHCsVGpgyMmpq1rpI0Uap5F99weiKCUaJH1fItf26FSmX7Zv4iShM-vN4RFCGf8Ibkhuimpe_o37CoRjmXSHbQG2S1QSCN3yqgJ_Z95ZvdshMAKUevm2cShmOpyE3LrHEjxsW7FdNL-RQGim9x53QiGx3Ndj9ogAuxyGNUeud72Ygu0QDL6C36e7kbNTIPN5u3OL2Yt4lKMswoyE92yPR1v9MsZK_QoWOSUZJUg9XEtw3gZGVmpx9pU94m6rjpxLSVSwp_MsWRp0sCKmcaXzgSOjXVD2Q6hi5pOqnLHi9k-PSSB_jEMEwXTcCCS45456daKP_gjCxu3mDBPcRRIRwYZDXaLHFnfyT--82ElrjwsBYrL4ej0mBajIdfbCZb_GnHn96oYnCViDscjWpiSxOKd3y3o7E2bxMnCVyGGzBYuSGoOzaR7YesXTuserAbiEC0-9BF2dvSoAorcrR2AiPCd364e6rUUH_qW4zaUbD3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/586f4ea605.mp4?token=fwdEuIkBanA9nBs-CSIiOKb3xTWS_ImxDL7bl75wI4Rd2dzlBbuBQJp4PLi2KaivkOyQ3jYfEIDd3NA1xWkwHwexdmWfKAj2kdWdDMEMXlLVrJ0ckZHVMWoUa2VnywCcQdyc0bU1-B6c267ahzn2mDmHAK64c7M-L_N9fdEo58ZdvEM-GO-S9e-xqRxQEssfQHCsVGpgyMmpq1rpI0Uap5F99weiKCUaJH1fItf26FSmX7Zv4iShM-vN4RFCGf8Ibkhuimpe_o37CoRjmXSHbQG2S1QSCN3yqgJ_Z95ZvdshMAKUevm2cShmOpyE3LrHEjxsW7FdNL-RQGim9x53QiGx3Ndj9ogAuxyGNUeud72Ygu0QDL6C36e7kbNTIPN5u3OL2Yt4lKMswoyE92yPR1v9MsZK_QoWOSUZJUg9XEtw3gZGVmpx9pU94m6rjpxLSVSwp_MsWRp0sCKmcaXzgSOjXVD2Q6hi5pOqnLHi9k-PSSB_jEMEwXTcCCS45456daKP_gjCxu3mDBPcRRIRwYZDXaLHFnfyT--82ElrjwsBYrL4ej0mBajIdfbCZb_GnHn96oYnCViDscjWpiSxOKd3y3o7E2bxMnCVyGGzBYuSGoOzaR7YesXTuserAbiEC0-9BF2dvSoAorcrR2AiPCd364e6rUUH_qW4zaUbD3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚪️
تاج: قرارداد قلعه نویی و کادرش را قصد داریم برای جام ملتهای آسیا هم تمدید کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103290" target="_blank">📅 22:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltDwVrZ4HsQRUltZbg3oxkOI4ejmLAduNR-XhCHSHcsTq6UX_zKKjJLlpFtKMsxWS0qJJa_hGBi5StiUG0d9WMrIeUN2euCm-YgeYhEhBZQHYgT-1Hnww03VGIyJiJGK9tjfQZPdXP_kSusRvTj8XRmMGTe0ah7DXRSIcSJ4LL04KvJuZvyLtQU2fIj04xsfbie78b18cssfXVH_YKsrFkOB31BtXCl3n4J64TRz1zmagy-WmGJnhHnDwrzr8iCpRyFrsgMpwQ3knLuRChD8uniBNjsEp4dZQOlwK4shK8CPDa3POn3lQkMMUwq58bOcgXnWWk-0Xf95830kWS6xLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورهان خبرنگار ورزشی مشهور ترکیه به دلیل نشر خبر دروغ انتقال موسیالا از بایرن به گالاتاسرای بازداشت شده.
در حالیکه مهمترین رسانه‌های فوتبالی جمهوری اسلامی (فوتبال برتر + ورزش سه) در اختیار مجرمین پرونده فساد مس رفسنجانه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103289" target="_blank">📅 22:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX93_-de_7U_xAJBtCJMQOlnWXykWvUvDsOZ4tS4p71qHGFRB09tz63ohJ-uLRASbJWI-oJNQ62jaUPx5ZHHEBl-JubNCh5O7bHdpdI0wKEqp7pyeaL2zophBIlqCb2F89oCjAcyUOnu_wY2EMTkamjQoGotgqYyQTcZcxe_BYfLKzZGB67M9eEkRWt-ExyWf-HuDyJ98d_IN2BJfgwU-MY1DRdzkfAy7HShSJSNX9LPLvTIrynwkRhChi7fmz9oUTPtIVxheHGjVSYmfo0j5tVCErcBDdGmI_ZuGWxRE1bGFBVEw0Im-5G9Nn4SmhiYv8emR1NKKG6NetnAEjUAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🟣
مارکا
: اینتر میامی در حال حاضر محتمل‌ترین مقصد نیمار بعد از تموم شدن قراردادش با سانتوس به حساب میاد.
🔺
اگه این انتقال انجام بشه، یکی از جذاب‌ترین انگیزه‌های نیمار از نظر ورزشی و تجاری، دوباره کنار هم قرار گرفتن مثلث معروف MSN یعنی مسی، سوارز و نیمار در اینتر میامی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103288" target="_blank">📅 21:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103285">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kaLT95Jsxgn59Yl_9rb2-zIIs-vuM4BtZ2-diFrmOegpZnA6iwsMpvWG2Sihk_H32iKTA74Qz4p5Ptf9fHrYTudcyCb2GY70wIQB0N870NqZU0jBgaHWp-tzdr_BI2FlWO3QusbTbhZfECxB5qp4Ho3iXWgLTMBQLsU3nG9efmzhZcAk9Ls81JMYi5e0IR5dphqz_rghLc7W5r4aUgrFyZJb-RA8YeCY3ygxS0zTv5gWUveGeqpReKgSI057uBAaFIm6ezfiMbqSxSrSpSFxMERqJWpOHrLT0jlD3EfbDTpqayvqdrW-94nH6yGpxi3J_AUXsL7BnpjksrWrfxuDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOTbrofyuh_ShM_AHgakCMO8zdrds7PROFEeEPIyxV-19I9uRD-KgZG9r48Npozw00znMjRHG5PkedD_IPq70m7QOXR0a86L1evnjTcICJzVuxgjYfKSkVPa9eBNqeqrSV_eMcKQpjm-6aBASX5SeETUfodUptyKUyu5olnnCCuFMXh9pSplj93jOcVxLSYcY5tyAi-n06kTZE5uSEOkpwuFwz7f-at1HLqTD2uFb9n_ynb9QhNp0G_BG8Be6xtHpMzrq0yWjscl6hFIZ3GGqNTzA8bghf2Tvywac40mK2hKCSLGtnj1NqyJ4OBdc-Hnb829zvDo-KqW8d6WlQW7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jd4l2XQ3LSuPSfYs1_ts5qBz95yhTmU4aopdaAPT55Ol0dRAjaprcOTmS58-MlvBopQItOhAzIVXD_vSTvTkV7pXpAgkTCRWRgN9fmnVlULiK1w0ycKfpQdk_lmEClwFcq7hdT8-wiZH-TS7jNptWnw9MZUyd1-3rD0T5GMJly4Dg3M6sQ9uc5Cf5h36UrHsyJwAFxXbOzuhao9UC8mhgSVhmyQxUJ96k7hfnWjTSwkUkKG5xWPBRd1iOAw8a-r-k21vQRbTOnLeWj1HLeprNxuhNMv_B5NbjClhjEEGJBRfB5GwpXQW-f2H5q14JBulAW-n5oVe7zMFrN7pts84PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اولین تمرین رونالد آرائوخو در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103285" target="_blank">📅 21:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103284">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری از رومرو: آلوارز امروز با وکیلش جلسه داشته و گفته که به اتلتیکومادرید بگه فقط میخواد به بارسلونا بره و راهی برای موندن نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103284" target="_blank">📅 21:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103283">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از میگل‌ گالان (وکیل ورزشی اسپانیایی)
🔻
احتمالا‌ آلوارز از اتلتیکو به دادگاه ورزشی شکایت کنه تا بتونه یک طرفه فسخ قرارداد بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103283" target="_blank">📅 21:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103282">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_P5LPKfFNv_1qvEz9bPu5i7MYWsUhi1y2zXfgei7ZXrFhYcZdy_Ov-1T9Ctk0_8JegG-PevmY34fSjeKd1QnU3rYwOo5g9q3Zo6TMIO6PXITBoR921YJXWGXaZtWaL-z9myVONVylqgYhJUvgunB4ygtRWiJbTVHCn9qYUMYWofZIuXcELv8LgQaqRIT4uX22uHGN6LAtoyPljC_6lgGnE2RqAOuhS-LCfFKEBLrcPLy9tK0ln5zhyzq7wCjShplYnB7U1gvQ8psU9nyvxIddn-XTIZ4Oenf7cNk46jEKMJmrLAzpCVkrHkquSgbPK30dvyzwmf-MuZHXqgbYgdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری
از رومرو: آلوارز امروز با وکیلش جلسه داشته و گفته که به اتلتیکومادرید بگه فقط میخواد به بارسلونا بره و راهی برای موندن نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103282" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103281">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWGR7cXEv5gjg_IFJMIOPlAjwB_DG_fdpQAx1o2AGTccIt0BxtrjyfPVUz5jGeaYLGAEaO2A_o5ZqDxaNBiTw8SIr0m7y-d9FytsB56R71XwVgLPr_-Sr52HDG4njuXMiX92gUi-5f3MkOuPU0fz93lH5TOpIATh33VIIc-i68Jy7VKJrLN17zZcELjJxjv-4dzsUVUASgLy8KlxotKO08KoeYJTGG1ad5FMbgzMBzJdlZm1kPiHxC4L1JhJQ4g95yPF7v6goFlljhKSXsuw5N7qFqOZtFv9TXZZN5uAR3saMpH1-j4oaJg43eialnjV7IqxsdhC-yK_pdCE3BjA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
رونالد آرائوخو رسماً به لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103281" target="_blank">📅 21:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103280">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADcj_GLQzZ11_chpRUQflagxN-JltrnvV5ovxnZfa95kSiVEwz4ZgrvSUHksDPS7Qp8dbzB-WB2zLjfCn1whpDvBLrHS_T3H_-nNgjMrOWH6FmrLYNTSmF7tKXdSWpSZrTd6gx1eSv7PvjLA4r32UR3NCIj29KmzwvL79CaAaNZfkm0N9kgIiCjt-vi9LrUz0S3Um9OYnKGV_U9ILjSYF0OF2Jzb653UCPIxLRTV8yglfoMCci_K7tLXmCVSnOfXxuVYcoKvPiSTkfMdarsZGZnO4t86H4p81kaa84dMJ68cmskrQZ2UU71VO8XpCDpBgZRvMTRDPFakHQSh5rqJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رسانه TNT برزیل: بارسلونا برای جایگزینی آرائوخو به جذب ناتان، مدافع بتیس فکر می‌کند. بارسا در مورد امکان جذب این بازیکن از بتیس پرس‌وجو کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103280" target="_blank">📅 20:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103279">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAsZYZttSNGYa8MyAkJwf_PXS60pCqCQqnFPgrvnZHsjfuhXB7lkMMXZ4lF9LEEp7gVLNvW5JcNrVUlezWo0Pol3oMZJ0HeuTCNf6wgfrBK7bQfL_tFSNRdz5yWTmhjKKmUx1s216E51XbXAb5gkllwX0Z-P8oA5_W3Sf6w_w0t8QU4FV5XJCCpjKtF6QHaOsu_p2Kj3hUMrwpku5RTYpNGNzY5hCrd4wpYieuX4AyKcrZbiaibVdWjE6fnvAbUsDa7WpCb2KmqCnlYNQqPU0kNxmN3NmmkrbcwAKZi4wJQPH61NjG7VjJ9QkItfTRolQ6iMTaublCPy4zwftGed0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
پائول هیرست
:
⚽️
منچسترسیتی برای فروش رودری ۷۰ میلیون یورو می‌خواهد. بارسا اماده است ۶۴ + ۶ بپردازد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103279" target="_blank">📅 20:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103278">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcHD9nk5nfW8ZGhJY3hqkXXg5KZk6lsUzOfMOh5WtBdGfYLcAZTQrnL4pmUGldnJQQ428rZw7RtSShi-f9rGJpBZJSeKFWo30UgZI8d0NXmG03hJoFli7A6Ny-nIG5zMQ4UlL1FO-RafLt9kL2-cD26GmWNGo4lCR9lWPq2kiN4hjGRd9L4eiwIeNwtKn3-I1KSFU1WCDYJ1A2l5LTTkES7UmAOF4bKH87BTjhCh5XYOr2K7lbsqGFbFII0CLBu044hLacgdFkaq1By-XPqsHLbdF3_n1FobrEprIyzXdMSdapWAWbjM2_UOLGULtbM9mEZWv5qridIqnrUoPHXJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
ترامپ:
ایران خواستار غرامت خسارات درگیری نظامی ۵ ماهه است و من هم از آنها غرامت می‌خواهم
چون سربازان امریکایی را کشته اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103278" target="_blank">📅 20:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103277">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfyvTqOR3rS5ofhycTWhWbdQ4mcFb9E4wvOYujAcYjxxcRWSGZoo7NZv92ghbVobuSTPTu44toW0LF2zBj-A-1nkRSOXN9KkiH4LX1meBfGY-k2G6W0aRmnzuIkkdO3uSaPkOQJlovPFgFAXRacoMS033pOll1G0QQ1djk61H9wyvukTJnUhYOUStHnOOa3rlpIhVgLgbJ2nNaA9MxSOsw7z0AaEfM_jxesleebajrp2QnlkNxE5ACC0AngS1-UWAKxNrOjZncnXVHmtQ_SRRGm3z61_TJbS67To_krQ99RvrDcxYwCw5VHuZVHaF9TKKaOQHU8da5gnr1Q26DwknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از داوید ایبانز:
🔺
🔻
لاوتارو مارتینز پلن B  بارسلونا در صورت شکست انتقال خولیان آلوارز است. هانسی فلیک و دکو از او خوششان می‌آید و این مهاجم آرژانتینی را زیر نظر دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103277" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103276">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSvCLk13EK-Nq8x9R5fINvjlGp0Op_nN6BG7vad1mj5i8wsfovPkXcIw-ET44R-1T9kt2t934KyvHy-6uTW8YKHduQWDMKM0s5cMCrT3H8W64j4cP9jcrzI_Px70Tp60jVxWGY8pS0xoGk1Wxumg4kxP5nRXh7lj4RL-Nrw-CQIwKDOfj8fCV2ubj6b59UQdxk_j6dk9Hx_mYy0N3XHyZTz89gt_hLFwyMBOfDdhzob1bVMD5RClvuYpwSCzvSYdLbRnDojeBTm00jQqlrlsC-XsmEfmJrSQACDckIM-xRLzBuOA9QgMg8z7UCNqC5hdVDii-fyjD6TFo5QPNfhKNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریمیرلیگ در این تابستان بیشتر از مجموع چهار لیگ اصلی دیگر اروپا هزینه کرده است!
🇬🇧
پریمیرلیگ:
۲.۰۵ میلیارد یورو هزینه شده است.
🇫🇷
🇪🇸
🇮🇹
🇩🇪
لیگ 1 + لالیگا + سری آ + بوندسلیگا 2.047 میلیارد یورو خرج شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103276" target="_blank">📅 19:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103275">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbdb454k3Y6hRxw9qfdOYK5x1-dGB6dhplrKsjLwigmao3r8AKGsdEM07eg34WjM_XbVZCutE4AwvjWrIxw9vwjMhwmQKfpZJ0KZv_MT8j5sPwBmii6oxw-18f6PV39r0iCR7RwYVfL2xQ7QihPYUNkOka7dT8aqbUV-72F6Zl0bx_YCng9rrpLpwawdV3UVPXSmkKgh6IKoHL2iB_eru7iMhyOcv1FL6vX6jUhcSx0pff9caH1rUmJWSeyDF61S4Bg9VmdQUiF7KMOfJO-jdX4OlX6NBKXH7TAD3pFs-7BfxajWFscPepwgdIpaphsS7wOI_fl_TySFBeW8Bnw-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین بازیش برای PSG تو فینال سوپرجام اروپا مقابل تیم سابقش استون ویلا خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103275" target="_blank">📅 19:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103274">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8023c35480.mp4?token=Gb6-NBjbcW5sxHZ0wH4WFAOjpMQyylrjQOqsROm1o3xsmHW18NLaS2Rve2pSlCvcwviQvVERyuva7xofwgoWbBQHFcFNgvjyJMhftJrKC7dl_U2c_zB0O84HcZolgA_JXuLwRt8HuZAa8hyjeM8dtmF-bVtciLlSVzLp1QPjbKDdZbpHwARqKPfsFChY3xcmBqcUKFjMqHi8SWjTfjxERgPo4gvkPOB6HjynHcLt0Q4gmrQ4CPC8Vfds4oDmdheX7w4gDgLYbrKOjgpxj5OFybXolUrGnwkj_Rjy1H4cvrgsh0ulRNNvLgVJqBqWNUVDtY_qg6wyChS2gxTSnrnC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8023c35480.mp4?token=Gb6-NBjbcW5sxHZ0wH4WFAOjpMQyylrjQOqsROm1o3xsmHW18NLaS2Rve2pSlCvcwviQvVERyuva7xofwgoWbBQHFcFNgvjyJMhftJrKC7dl_U2c_zB0O84HcZolgA_JXuLwRt8HuZAa8hyjeM8dtmF-bVtciLlSVzLp1QPjbKDdZbpHwARqKPfsFChY3xcmBqcUKFjMqHi8SWjTfjxERgPo4gvkPOB6HjynHcLt0Q4gmrQ4CPC8Vfds4oDmdheX7w4gDgLYbrKOjgpxj5OFybXolUrGnwkj_Rjy1H4cvrgsh0ulRNNvLgVJqBqWNUVDtY_qg6wyChS2gxTSnrnC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار دوست پسر استر اکسپوزیتو تو اولین تمرینش با مورینیو
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103274" target="_blank">📅 19:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103273">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5629191c63.mp4?token=Hskl6n4Asfk5cjAc2ygqzY5dD_Cv42sj-R95Lsr0_uU4aEeG3Injg-zX8N_e53_6whOSRO4NH_e3iyCvWjhTWSmi5_wI1sKF3SMUHTIndFwTh00ldV4GzAVoPOyVvUK48En-d1BYxQ_qLaJVB2FCjuX9_vJzQBuht0EuNL2jIw7hskDwJ5I-HiOwY1X68XttCg88QFewBuJySgDvzO7xK7s0nOf5i6aT_1InZDQhOdxLuyliXI2TapJIUqXmKgbbYSgldmx3TPmWGhkFAjYpd-8tXGs3wUtXuJPuPu3FBebfITN9_Tiojd1hXcMMiTRWel_Z4gAM3vUoorbaduXb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5629191c63.mp4?token=Hskl6n4Asfk5cjAc2ygqzY5dD_Cv42sj-R95Lsr0_uU4aEeG3Injg-zX8N_e53_6whOSRO4NH_e3iyCvWjhTWSmi5_wI1sKF3SMUHTIndFwTh00ldV4GzAVoPOyVvUK48En-d1BYxQ_qLaJVB2FCjuX9_vJzQBuht0EuNL2jIw7hskDwJ5I-HiOwY1X68XttCg88QFewBuJySgDvzO7xK7s0nOf5i6aT_1InZDQhOdxLuyliXI2TapJIUqXmKgbbYSgldmx3TPmWGhkFAjYpd-8tXGs3wUtXuJPuPu3FBebfITN9_Tiojd1hXcMMiTRWel_Z4gAM3vUoorbaduXb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسی قصد داره از تمام خبرگزاری های آرژانتین به دلیل رعایت نکردن حریم خصوصی (تصاویر از مراسم پدرش) شکایت کنهو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103273" target="_blank">📅 19:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps_zI2c8kTDfObPE_jSlvNNbC1_IPDz9pRu_KF6f67SVFgWxNEjb7u_fo3htf_EnyczGDRwZygiFMyaRaXqPL2MA3ARnlrWsaxurRRu7WEMgCR_2uuf2CxU02AzkmCWluDpJ9OYL5lNS8TJ_YjK9Tyt-zhdBO8TqVN6myReJ4NiacnEFlhkgQRh53NeOVea9YVc6wvmEfSX82nbrYLyPP0sMW1r-88HegZE56sQBux07Kc10sS9ymQ28Ulh2d55slkEIwqlVF5RAZbC1F6pIx3aNEov0WXbfnGSRx9KuWOjfXpfb8xtjwyrLa30KyfqZLO_L0tEVoBX2mDiug5Fn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
علیرضا جهانبخش با عقد قراردادی به اکسلسیور هلند پیوست. باشگاه اکسلسیور فصل گذشته در رتبه سیزدهم لیگ هلند قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103272" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29f11cd214.mp4?token=WXIvnCArD9tz5Wc_jy7w4-V4owwfzwVlL2UH7Nw2Yit8ClZ4cmwLpiO0Twz6FAvNhvSrc-oUY2cVxJ4rabicXEqTjXfMRTT4cftJ48LLc2sT1UJIijTKK8OXSdCKj0fMyj1FwoF0K9mfzyGvptmkqVrP8KcZbhN1AmboluFcGg6-ibAZoL_Lr-OYYGvdJMoc2C3GFKpyCsKBRjFjstD-J5y6XK_POwLDfX2Ub4ejRFTmeXm2Ljpcz1v170Ev5qnPOnp_Eod1Xcjq-pD_7xsPJiEC6hbpLpoljblkHVAptD8LEwhHG9Xrr0M7pnOnS2hjkIVrYbtTv9lz6mcN9k8ckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29f11cd214.mp4?token=WXIvnCArD9tz5Wc_jy7w4-V4owwfzwVlL2UH7Nw2Yit8ClZ4cmwLpiO0Twz6FAvNhvSrc-oUY2cVxJ4rabicXEqTjXfMRTT4cftJ48LLc2sT1UJIijTKK8OXSdCKj0fMyj1FwoF0K9mfzyGvptmkqVrP8KcZbhN1AmboluFcGg6-ibAZoL_Lr-OYYGvdJMoc2C3GFKpyCsKBRjFjstD-J5y6XK_POwLDfX2Ub4ejRFTmeXm2Ljpcz1v170Ev5qnPOnp_Eod1Xcjq-pD_7xsPJiEC6hbpLpoljblkHVAptD8LEwhHG9Xrr0M7pnOnS2hjkIVrYbtTv9lz6mcN9k8ckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
یجوری پنالتی زد که فقط اینجوری میتونست جمعش کنه..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103271" target="_blank">📅 19:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103270">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c6dda8f2.mp4?token=RNPBvLvJqeUY4CY1U715j1wOsZ48sOvpJlQkv3MOrNRJnMQi-nY1u68V6yMjOigXlx1haJRewT-ujp9nrUr6bOX9CxkA_ER7fAJPaA1yuukZhL7Lap41-B3xPRs0g2qTUfZ1VFsi9IlFOzzW1w4-M5a5ZCWBShcOsFwoHgJv2qtkuHAqFQjDRBHBwIjihxoMaAkkZJPIybSx94B5VrfMver-ejzZQFjqpmTq1EEDPJFCCK_S9v2VJe_5F-VTICncF4Dx9kF_a7eVbQo_P8o8OKrk_kSitwDm-LAeDJ531M_tcPIIOS25t_0XRToeyjUpzJm428KUOC6TaPgZHkJCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c6dda8f2.mp4?token=RNPBvLvJqeUY4CY1U715j1wOsZ48sOvpJlQkv3MOrNRJnMQi-nY1u68V6yMjOigXlx1haJRewT-ujp9nrUr6bOX9CxkA_ER7fAJPaA1yuukZhL7Lap41-B3xPRs0g2qTUfZ1VFsi9IlFOzzW1w4-M5a5ZCWBShcOsFwoHgJv2qtkuHAqFQjDRBHBwIjihxoMaAkkZJPIybSx94B5VrfMver-ejzZQFjqpmTq1EEDPJFCCK_S9v2VJe_5F-VTICncF4Dx9kF_a7eVbQo_P8o8OKrk_kSitwDm-LAeDJ531M_tcPIIOS25t_0XRToeyjUpzJm428KUOC6TaPgZHkJCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کی باورش میشه رئال در 9 سال گذشته 300+ میلیون یورو هزینه کرده تا برای ایشون جانشین پیدا کنه ولی هنوز موفق نشده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103270" target="_blank">📅 18:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103269">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMMSeY31QiV70_kah95PnX7v9BCO1nJWLPPVicdCuKMG2cdXH269Bn7QHD5Z_u432ICW7waPU2r9ZVRi5D4ww6iROr0qXBCfeI55E0VAoqGJ7__WiXPaxjFI96Tx196M3py9v4mCDWUVqbVT-GtzNyCnZl45cLWTg2Ieu5C2-YMUCDj9LuixTEgv1trJtfzughGos9GfOXvwpDSOGnSweOk3kTkMj7IjrE6MuyBOycu8gISThwTlkKSnWBw-ZMQ5xvEneyGZtxpXGNJRcZX3Rk8pr7goX5W14DUHbeTF5XTjgG1SSlw3EhAi0ymwqjrO3pH0ilvw_e-NW9-7BNdhJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇧
باشگاه‌های پریمیر لیگ که بیشترین حقوق رو به سرمربیان خودشون میدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103269" target="_blank">📅 18:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103268">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi3y7zv9TfXYcp_femcIhCvrWoSMeIKTMv4lWrDKdSBYk0TMIRU2vi3bS6vnrvleT5Zu4g0GSnluxCnshM-BpaDno6NTdYF-euvfaJp15zJzrFAJimadUUYF5qdJyz8471SWfKMugilZu_ToWl2mdLRkyceexuO8QfcTynLerLrbHHrLO6e-E_D9XOgLi0gwP75Xs1dURTGQ8HO4E5tYsiyV-WlvCc2-NxNgxO0TPJNgJTXOEki-pHhSUsyP4okvqCphHTa44Yym_ys5Q8pXVKsQLCTT_oSQe1UWUvH3oq8M5Lj26pEL-tSbQKyt_G-Bc9IXFfqJKkcIBimjm715tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
فقط یه فوتبالیِ واقعی میتونه هویت هر 6 تا کله کچل رو حدس بزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/103268" target="_blank">📅 18:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103267">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb1ladMD6vx3FvBocIDRt-xYkpCQuGV_5wc8rYZajA3hLFWZOkivtVpGBzIIdVG5Id-eASiqjI6HAre5OjR45dGD8L-R-EfJIZ_alLkY2T4KFN3Akg8cptjgRw3J3F4t_gOIIHUE3FQJKZ8q242SeMb9d_UoPMrMsxHJPRIrbPMGJom_f5HK1vjPcHwsRuTwF4R0knV8HXCHomrah_LL2UwlcIt5RK-sfqdCezpYFgUrIeZP3g87jBe_eoVqs1OL3wAoV5rv62laH2CZdhDjbMQF-ndDpELmRvkPEG2P4-YXT0Cb-i4T31yAxnvT8y0o90db7wWvxrMtJxR7GEQFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس کلی پول خرج کرده روی صورتش که نهایتا شبیه کینگ اومتیتی بشه :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103267" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103266">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad5bakeJRG0vdgeFld3ePhCtBpGgZ5kCO-8PycamtwGmGY_3DIO6blz0UpqErnGvTvTSpgENEwZdJjHmhBraBJfR63EK6VYrZSLzm1SGP6yMcg08xVOz96ReOEzLYW_6nrYwffODTNRTfZmt1-_ARtRsHgrURQ_nInes7Udhu7jpAvyWIenI1RDUg_zZMFL8xR6W395CxrVBL4cYwfACN03f4RMMsb3DDzJdZNDcjmbJoAgFo1sZS1Lq6RfYQJVI47egiAJaDKgd6Pei5OkgKNpdcfDYDtMowo8SRjv_d6EUiJd6s94Uf8aLsbDfPS19yAUy9m3Jbdk4CYDVxRa2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
علیرضا جهانبخش با عقد قراردادی به اکسلسیور هلند پیوست. باشگاه اکسلسیور فصل گذشته در رتبه سیزدهم لیگ هلند قرار گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103266" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103265">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103265" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103265" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103264">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4A095Rrg12Trlge16LWGypGodoBVQk6bLSwlgyG5SHv1SXG4SbEEuGQ0pBdPb6Ymctulhq7IP1VEAnXM_MyGkiJL5I83cyUyzBeL4bY_AoVliWUBkp1bPyLAqi3m3LGqQr29AN6m9dEBzdUo9jdcAPu24Z-IOqO7UYUpVnj3IdGMkQcriARy_e1zBplnz1ahBUaLaYXRIPU7NsZpugIn5IPKzIVI4sBo_oEt4iNQ0-5i7GNPWYnaVqlFm6zvtTYffIoXd6fVXHcfII-ietuuCFJ60jTijViAeHFP0WXgX_4nrjo1IPT-ez04WGOsFImXstwApXTT5SydqMDju12WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103264" target="_blank">📅 18:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103262">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dikhEfWGcNBQKK15Ljy8mOBuFtf_PWTtL0HabWdZF0yp2jiVrZIJh-vVYvgR393_XqKtUl2KKYJuy67AldW7YzYu2aUqqTfT0CpMKgrQX9RNBTA7uMF46ayZdsK6jGBV-035dMOXuFcN86aZCEtOZx5un2FZCzn0hPEGOGIJcK08KQjbSLhPQjKje517gvcFXwmLcszGICRIwYDFB2mzTZF77gsSiA1TJah6c--vOKDzHjUBOsVhhbCt_4Sm1fxiaPNS5MyK9Hkl-giOj5UWvQR1PiwXX2YA_xoHV9vdbOSi5zQk0PVWFNnJTVEVpFyK6qkqYN07jWq1zbNyvVN4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/naF0kF_3kt7bLmkP4I1npCBTGCMnixGV-yRKrVqESbAqcDZFxbRM40JSDyL_YnPdKEOaQlwYH2IoDaV-j-mVY4PYkWGBbohts_QcmN3Ezooxv2X3q_SueoLiUgrpfuFRgs2Zvp3md1yL6XZ_LRrClZ-XwAa1KDvugs2SAfmxG7kNLCQI-Imex0NeMkCwN19rRHqWzUSbaLZeQWGVA3M0Jn-z-5JJ10dsDaBOQE6MYJcjdMb90zyE5IWYRa6iTNS79yN5bwHNrngJY-2UZXaccxt0JZQ_oOhDNF4zj7eCC9wW82OxzaOm-qeJNXEN8zono6PcsNO4HAzbh--w5SlqOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚪️
رونالدو تو آخرین قرارداد خودش با رئال مادرید، سالانه ۲۲ میلیون یورو خالص درآمد داشت. رونالدو ۳۰ میلیون یورو درخواست کرد، اما فلورنتینو پرز از ۲۵ میلیون یورو فراتر نرفت و رونالدو در نهایت جدا شد. وینیسیوس جونیور ۲۵ میلیون یورو درآمد داشت و پس از تهدید به ترک باشگاه، قراردادی ۳۱ میلیون یورویی امضا کرد. پرز بزرگترین بازیکن تاریخ رئال مادرید رو رد کرد، اما برای وینی جونیور استثنا قائل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103262" target="_blank">📅 17:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p94hdlgbH3wN7TMs6LjuaOfDjwp9cJguloqvSa9ZqQuzkWHJ8xzsSTVU6c3zOqR2geMeC8LrCE0ic0Q5hn4qJ09kOQxt0Ru_ixD14rTAvO7gMe9ZNTj2o5WjTLLpKei1udM_5T6lDHBtfrxZF_RQAjZZ-lvTn_bZ65zrQWBmhHBORUAVJBCH7Pwh-gNOYk9kxWGJ298n3XVyeJCkXIbL-YczwD6JA57DLQxoKKwzmvFd9Ewi-xllUfrCrN9zjN5J1LNh-fYCNuBN4inlKWvsWlB1_HMXXsEofsAEDp9KncfReJGtXRjcJwpYGzHIdLQi-l4y6WR2rrF-5ZJ0m-a_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTa8CNS1zIPI9QJ8vIEMhNYhrqB6EHigLRyCmIZsOJ5Nft8Uxc98oLEAGPyBeIakwCmHG3bzGIqQGN4icn29SOUboDy_EYlBAFV903BrdrqphBS5orz92gn-qEHFwZV1RDeO2G8xslfMWScgYfGE5QlcvUrbsn_bNAtslyfBDt-cFAazQCiM75Zq7ULezSE4-8JtlqBZqSCE_osgMEEjmh31HeGnj_uDJTS1ibcjma1d4Aw4mey6Iq4pCA4ZzbwiK9LY-uznONzkq-2OOituA_VSTZRHB6l10b-eEfdvQxTyvYxA5ecOPnb2Y1s-MvHg9A8hV2VEaMx3osY7UJKVaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c6e02cf3.mp4?token=GBaoLPg-M6YKakj3L9Bom5Sva1JY5WDO6hy4L9ObZaWRUJVID2uQIGnLiw3JcfhnZ6vHRt8XGya6BVkArwm3RHXjH7acw3l_jy5r7OH_EXWrfO6U8jvirWPIu5Hp23VJpOhLESrmN-3u4LE9YA963R5as6t-7p1rx1EWkb9AwIKzhosKgwWUaSPB_16a39P3XY5Yh55lpkqAlcYyDM31B1IBF3k3Y3IZCAz4abm2sobuwrrC2EsACgTR9l4quEwhpUU0TpF4JeXhS2yGPqjfkwkSkC4MQbXK-YS-54RJbdpEXXsbBJy6V1Ea02WqX2zMNMkswQ2x4gdvGhl_7AJigg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c6e02cf3.mp4?token=GBaoLPg-M6YKakj3L9Bom5Sva1JY5WDO6hy4L9ObZaWRUJVID2uQIGnLiw3JcfhnZ6vHRt8XGya6BVkArwm3RHXjH7acw3l_jy5r7OH_EXWrfO6U8jvirWPIu5Hp23VJpOhLESrmN-3u4LE9YA963R5as6t-7p1rx1EWkb9AwIKzhosKgwWUaSPB_16a39P3XY5Yh55lpkqAlcYyDM31B1IBF3k3Y3IZCAz4abm2sobuwrrC2EsACgTR9l4quEwhpUU0TpF4JeXhS2yGPqjfkwkSkC4MQbXK-YS-54RJbdpEXXsbBJy6V1Ea02WqX2zMNMkswQ2x4gdvGhl_7AJigg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید بانو جورجینا
🍑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103259" target="_blank">📅 17:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103258">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZv37qQHlO6BJ0QWTyAKeuMGobjyZnCGn_r9MmGTfAuVgbW3ZPYPCLpzv9qbGM59HsDPK5ooJaL9jbGdYmDp5T_XNvRQ82fOnLBbCYEKjgSSD69p2uah9cOfX-fjJxb93H9OHDl2oH6xBuPqUIeZlEISKPl6qBl3sxc8LzfEHVemtQ3-GVYNw9GheO6-ZfSLNl56TPMWhPqtl61SobbeWaG2nU1yJ_fkqR7drZQj2Ztu1Mx88GVSNCVCQceYSpRkoTG2vK5ICvvZ9iXPn1LvMw1RbyrqndtKFcTg6T_GheJXWaJCSjkVA4YVRvcwdkY5wBQ6Jv7UExBI5Azmlwyl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
🇪🇸
رونی‌بردغجی بازیکن بارسلونا در تمرینات امروز دچار پارگی رباط صلیبی شده و فصل‌جدید را به طور کامل از دست می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103258" target="_blank">📅 17:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9099fd2879.mp4?token=QrB7-6hK6jZ8i5IkmrUxnOSYNQhma6hbZVL8nfGbmUHELs-rHPnn8UQRhcPHv4CbvYlbDi8NtIqX2uxLiPVRLlb3NYoOxF87bH8zQfhImZkeUJnziBKB14cOPfB1_DQik-z0GOHeh3K75E971z-n_nd3gej1jTSHP5bIhGW1jV3vkTly6iQrb_xDjEL_9u27bxuzNAzrO6-7ZfSAaetvWqdckd-JZN-m6A88pQNG6pSuAvxVog5caKLVRhvb7p45kmLZFYjAg4aon_EhQ9PK9O3HCSfc_1yew_r1ZdRtDbnPnnOAV9_88ivghNrOktba8iFhqnh0VmXEEj0sk-8RFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9099fd2879.mp4?token=QrB7-6hK6jZ8i5IkmrUxnOSYNQhma6hbZVL8nfGbmUHELs-rHPnn8UQRhcPHv4CbvYlbDi8NtIqX2uxLiPVRLlb3NYoOxF87bH8zQfhImZkeUJnziBKB14cOPfB1_DQik-z0GOHeh3K75E971z-n_nd3gej1jTSHP5bIhGW1jV3vkTly6iQrb_xDjEL_9u27bxuzNAzrO6-7ZfSAaetvWqdckd-JZN-m6A88pQNG6pSuAvxVog5caKLVRhvb7p45kmLZFYjAg4aon_EhQ9PK9O3HCSfc_1yew_r1ZdRtDbnPnnOAV9_88ivghNrOktba8iFhqnh0VmXEEj0sk-8RFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
واکنش خبرنگار صداوسیما اژدهایی به کنایه‌های اخیری که عادل فردوسی‌پور به‌وی زده بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103257" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujd4YgIQ49WvHsIDgmwN6jKkqW_O4J8Na6hjF3jbOLYRdYy1PZmd2JKS1hHkY7oHCMDQHjbGCzqt7k5AVSNy9cRzwjsNMX3ANs96DzilqwzXtqtj47Tf0veqUonFj0uN77eByza9y92GtTMvAMFbenDpYcTsjBi0OBu0Uf50KTbUP1PLI6G9lazaUyhcqwT0PbUQXMoG4Us17z_zoMgaNUYxQvQzPqhBmIZd4IdUFUahyUZw13G8eFgEP35N44nzxDT1DJ583liYKn2ouD_BfotuxgpFXRJ1U9FD90dQzq7EHK_aq0I1M4nsSwo9GeShtds3DQNkaELa7cpdAYTtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسکای نیوز:
جف بزوس در آستانه خریدبخش زیادی از سهام لیورپول قرار داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103256" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e349ee52.mp4?token=MDJqdGibwnP1jC8eMDUowMXpagneGa_C4qFTnnTvtYQGsK2P7g8BdbN371-EO07dmk4o9jUi8aVCV-TFnmHJ-EVwFxpVl0paooUcunUH8XkvIPVxgN_8c4iBuaEeYiBKu7Ii9Ic7g5IGgx8LVVXhRDOVTeR2hdfU5bW_7NhGSEPs4-Xld9e6F-XdSao77OBdfuF-Hkl5aSw8g_0bZ0MxcpRQ3U_S7tErvb7-8zmvne75im3wgcQC3LsEkR192sr7X9pSEugnpWaagEm-eWVK2IvJZPK14hdbflQgHZlhqLtk-ZTeOG6OqJVfz_nmnxtwJ1zPkgBkDWscA0nsl8-9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e349ee52.mp4?token=MDJqdGibwnP1jC8eMDUowMXpagneGa_C4qFTnnTvtYQGsK2P7g8BdbN371-EO07dmk4o9jUi8aVCV-TFnmHJ-EVwFxpVl0paooUcunUH8XkvIPVxgN_8c4iBuaEeYiBKu7Ii9Ic7g5IGgx8LVVXhRDOVTeR2hdfU5bW_7NhGSEPs4-Xld9e6F-XdSao77OBdfuF-Hkl5aSw8g_0bZ0MxcpRQ3U_S7tErvb7-8zmvne75im3wgcQC3LsEkR192sr7X9pSEugnpWaagEm-eWVK2IvJZPK14hdbflQgHZlhqLtk-ZTeOG6OqJVfz_nmnxtwJ1zPkgBkDWscA0nsl8-9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار به نکونام: زیاد تعریف نمی‌کنم شاید فردا مجبور باشم بکوبمت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103255" target="_blank">📅 16:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103254">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇪🇸
Xavi and Iniesta
🆚
Italy
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103254" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103253">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a709379c25.mp4?token=V3Fe51frv7DMPoCqc5Lsbi8waB6N8RLe7GRewYuGaIbIxSq9azlaNIUDaLvfpkXF-4Rh7FCLvotPpTEOavwOWK4Shsr94PfRHWq70s2LroOgAuCkpdr2VyRamt-Eq27Uaqw9sYYxLQ1o0Vhv5STb03KJDZxd8AXdi9SS3uAix7qJovyd-4eVhq77ALiJjIRkUZb0H8JbCM7D2i-5dfYcATRICoXdqrqwaKMnfbqv0PJtpmQYWrQgnOTm9MiMHatKcWjbgSoiJ6PhKU7vYrcZRI2MLNYgI35n8UwAs9pFDQxgl-C30XefignLltXdiQ6fFZHGByOANvOlWytVZbXG6EvjWJ5u6MPIYDAbhFfMTLKImgH950mJsEpnBIue1tCjwEqcaimdllE3691or8YC25hPHV2ypkNKtYhd7giMkWCeBZxnGJ8dpg2azQMtTkYWMaND7UuGz8QHH7DYUHdwVZ4EEQOXFZrw4QSDCfv42YtuSlTYDR1j4SL-1PAbtqQes4AiU0ZalXkmSolSexzh2FH-1L9muRyvOKltiIZg75jg1TtbK0YzbF7kKiZlEiSqbKIbIGMKpBRP8W_kz4I6h5ucUIHyoUbZO7NmfjzF4_pwTkM-ZzRXH-Hf-MaD_zGNxeqEaXV1UkXCmm6qSRurOKZjDeGaj5zsy0UMuD85614" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمه‌نهایی UCL2012 و بازی جذاب بارسا - چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103253" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fbe5b387a.mp4?token=jgoWL3GUAHU-Bs9E0F4O-KOBEAsv2UD3uEmx4McvCG_bai0BAL8erdTPJGt1XChn8f-lxsFcebONqs8i1zfulqB6hySNMBGnWS8vk2ZCymoHz_mSX-8gjlYk1LExx4ksUQ9b3cyFSQegUBCnpMwO88HONOJfcpcopu3e-uku9cZ6NcsOfNVWk6bFFbWkNAvjdXkgwObPn_OxA0KOQh7Bir77_xvpZskgnswIJXEfLaKvt2pV14HOUa1uIvSbJh5QjdYlUTL4lnsT4MkOPd-JVZviasGmg1jdJVKdummoyCuTxRohecmsNXGQ74yckJSoJtP4cKew7ES2H92I3C4FEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ادعای خنده‌دار وزیر ارتباطات: به اپراتورها هشدار دادم که هیچگونه ضریبی روی بسته‌های اینترنت قرار ندن و باهاشون برخورد میشه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103252" target="_blank">📅 15:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8870e38c3.mp4?token=DMxdd2iNKehJAlRfIrfQ5VtClWvcCwsb9WNo5jIDwnWC0-80YuSDQru6f2KvugCFgFpdSxplNU3px5BiAo9R_KcOZl6QIOsRyrIcXe5Lq9XOuEa1-RAEm8DhmEMhg6xX1c7qjeI18KRgV36uLgbUtZ9JHRrZWyKzgwkaHCSmLogTvAootPOKZFkIJH7eRUmSi8JTiJr9It-qbHQiB8uEsWAOZZAB1cBM8_227EpQcgXUMQmYRIQ_tHKcE_tsNCaBk-tnMVSYajlIFh8rAyksc5kkXZPdGvi2nJ48YL3MRL-_cZTkYe2h6ZbyQF1XQm83DbrRnz1aeM9YJR_q41w20w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
امباپه، گولر، مورینیو! این مثلث رو قبلا جایی ندیده بودیم؟
👀
🤔
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103251" target="_blank">📅 14:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsDMaGuhulaJpVe8x3c-Ehm0DDaJbJAPpD7wuTBKYfoJJNUj25-rr0QmW-MaW2on0TRwLmGjr4FYatqP8JZgzJhsNYYPD2Dz0JYE3eBkpRqMfDZZEZe0IKrMG7ttDs5Z3bkRTngBr0drd9dd_3dRiSY4HRAGwj7B8WgqNk3A5oA19JZU3ugKSKwZgS9g02V-pbBroJeZFeknkd2FUsC69YwNTYrdQOeYAl-oYCqKaD7JKu7UpNJlGpxUNmLjFElmX7ECYrby-fGjovNaW46scz5_44TQEXfYetjo72QTFUh3Q3LkaFsXlqlpKSmvXHfJKN0b4uNkOcIutrBpGTNWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
پس از تشکیل تیم ماهیگیری باشگاه استقلال، تیم دوچرخه‌سواری استقلال نیز افتتاح شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103250" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hrzau2RriuNtXxUEB_tsPFt9hn8uN_mXJM1GTJ99iJ6xKksn_h07ImIKrv-GQgyz1qtyBu5rO_asEj08cnJKt0Ozy6NfZaOP1tVzL9deLOIj5gIzzqVVjxOx_PIaZ2unlUULNXDEDlOR0tUILuuw8RUhuZHw_4-PssJOSNOZjbKCGD3MKGFRyhvEwChHZ6_fhyHqD6vTnJhYnAz-Dis_qUhr4pjL5xzhtZmGtzagfpNOrScJZ3Ynoz2tZkvV6qvSXDJ4cJtvKLhhyy7my8J3M8E4QQNuu-K9Vyi1FlW6YVgm8ENBVAj9OtNiBBwoj6PY4N7GjZ4F3s0ZiWbOP3UmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇫🇷
#فوووووری
از متئو مورتو: بارسا و پاریس برای فران‌تورس بر سر مبلغ ۵۰ میلیون یورو به توافق رسیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103249" target="_blank">📅 14:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103248" target="_blank">📅 14:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b442857f8c.mp4?token=FoEQtjiIsZQFXCj4kdj9E-D0kG1ZLg4AH8KLI1SuNn7ZHOL4UOklk0mAPJ3jEXFJhKnt5zWvOokWilbSRPHY2lSWqXUpcZ5RPsvltRGiInHHnETpbwac-HZ5r3e8fmyeg1RmgrI75HjSeLMU6-u5I23UaYktGqK7JdaCkEFAcsZYVIKsMiZCeMAfyOh5JSa2EF4LMDloQ2ORjvTMUfowFfQNhScLOUThPQOvrxA64ifh5xxpravkq9sNbKp5Tps9UMiBgfpaMC_YocTPW54ohgh8pJ-I-M_By5zowZpxzsnd-Qin8k-SlzQrkjhQv0vIb6bL2CcQLbvSaYFl4u7fnHBVVO96jhuOvVroM7T08Yp_le4TU35hBj2D9pEmaHQXss2_d0EMfRr0pGjUGD9Il4ZY9lRrb9HSkAtHaxUC2Y_oWrE1bz6xm6B8NyaJbdW3KoSF1wJSY2aibRhY3J60lA0lIsLjsoayV51o0NOkbQF64YJAF8JoMRy-674FaOe04nBzJIkJmsaFn2DfrUpWc5nj3lE3LocFrpI2HorPdtcmI6Ie2iDImqR_ZTaMuE_en5W_PjmzyKxQFq8hPL3wKuMfvjzfR0mSBrEblnGXhwcJrBsgSEeimHgtSIoAZlbnceBfenuC86ieszCc_1-6gkllRjOL_SE54Jbw3vETLao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🐐
برخی از گل‌های کاشته تماشایی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103247" target="_blank">📅 14:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103245">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMUsRe6Ic5A_7YdWA5ukDllkeHokK2qZMrWcmvv-KjuncbJvQsxFvJT3XFeuxoOZ7S0lxvpkPQDRmx4K_UqDFplZPLb3fbU4-hMLrSUP69_axvnFhjRmpL_wohMkbtJ7VqgiYT7jJ0vSBifN7Kxof97_cmUzEAZFWBgWXIymo7YPPKjOY7o6XyStQoZ3XrRPefgxHJU9uDmM8v8ESMR9vS_HIVq65OV9Fi-3ZUgrv04s_6RbwjDC7JzkSNdXNqXmjNyPEtFebdYiSfDvMrWGL4MhX0RbgyMVWEZcR8GD-T-pUjDZ8lxlTNA_Zp1j3xD8kHUWRiL1XVXILP5qz9pExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkoK-Y6cWbpHwDwtCAnw5lkcvvxpzksRhtfiVoJl5h1obAFkRU55pm6KP0wgGcutswl5EWM791g-CtaXru2U-q3sov3blAAnmsFTrVOQbq5uokf-kDu2At-LZU-jQrd9dTwfesGL3LC-rb97OekonavzarFAkztNlgaDlGnfr4ld-ZTVjOjr0XJT5GLSIIA4_aSDY56fc9z2PIhaKyWIXtdO0uIzwLNI-6c4ZcmC8wGn5Q6ZV8CajLga_w5o_SGCEkvcfLrtm2E2Q6w4Yo9_ndhbTI7YYyP7SQdnhGmhKkbVDElDBjMQndqQ0qSirw9Ee7XbT8JxM-hihu7kDCQ-4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
⚪️
تمرینات امروز رئال مادرید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103245" target="_blank">📅 13:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103244">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e730d0e84.mp4?token=KRhk3QuRth3dhVTrDrinJ06y34GAyNL3HqAXXDPXrTMZZw2Why7cVmDTp7CQjgLzw2PJ5za9x7AdIVlnZRgvk9ENH9Op37muUCwWaD9xK_Gb7py60NfPIw1JUrW5aeL-Oay4f2ooErXfI5w-2Nl-msoxh9J3nZvP132lBa3evYZkPQcMjED63-yga7l9uuzAQJwjMx3lhhT4nBDeq7-ASZ49S53Gnz6sdBbEa6YQOGP5lflJAbFJNX4Xgj3LhKHLSiDGpjFr9zBCkOg0Dsw3VRZ2mi8j1yad-dqwjRmuwzgK3YhYYGN81qS-ELouTg2hcs1yrS9hAUDolxAXrcRdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
با موسیالا هر غیرممکنی به راحتی ممکن میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103244" target="_blank">📅 13:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f008e3e11.mp4?token=k9AHxA4EiwqeIaN0q1kUbnpSNI1FkGeiXMKytEpzWxQUu2rnVbimKqbyKhpKw33FQ6bdErreJ3sUjKZSWfDW5EUw2Xonxk0oiC8XYkGumWAWsQjudF2JALxRsI1lHRkkTKVG39L8nisNSHGlR2G5VyikpZKC05oO6j-j-WNZv0uvPbdT6r8euePBpREKD4Nlh8GTvg8S2ca5WF8Q7c3AtssLb_74nkvyuiNavqdGePus0UWU6l-8WzOSD2sgU2cMdwQBxtocfWQhJS3dINqp-WOBbRFY0ulLJJ2cVEeaO4fqMy3OXLERlRl7LAZ42dc3ToavTp0RjV3TSy9tSVn9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
وقتی گواردیولا به جای بازی پاریس-بایرن، دسته سوم انگلیس رو نگاه کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103243" target="_blank">📅 13:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa14f9fec.mp4?token=VOWbcLBpUBW3wfD-3uFPapkO3g2qAWr1N248pfjnAzqRnuWRToNxWLLOmAXkYqPL0ILRaeEfeVkUHp-dTOEXUgZthIZ92M2sFGkbxu3ZUincPg6V9RVSp7ZNgX_2oQohh5TVVJY1cwxndTc0BtUW5DCbLJ1fc1ZWjIAXRQlMOXnvkNZ5gWkiAG0-InvltQz_hz-XZpAUdihCzpXOeuHzUch85euMs5yGKTqiCOlLRp3mdEDoMyB_MP4b8X5NB4lC6DS2f8ZHvjFculyWq1tc3okT_ahQj_KsBDHH7uhDOQSdd615NdtTLIekHG5F7bkUqnDaM6KCqNGrfpT0df_TClFr-WYBGIenV73DIrrZZNq8tRvHcFPpUOUxYjpf7RUxBTNKIEOm8m8TvHWTiB5KsnrWqzgMud17rRZHTrl1wRnI7jk8iiYkSVA3TVScG9xcJJ5o-dU576yesM6MTamrJ-S0yRqcP3o7q0zQbLh6WWgnp3KLwjID5N2BYeZd8hutPd-q3AiqvUYguTT04BMHwL7wiSrrvvSW0RnQ35dsE1Ogh9brYvb-HchXPR50jviaeuS8BhAjrn9ioKF2fHcU8qc4FguZdrq4kyCW_QaNJxgFGAancEUZf5m52Sm-7-JsVcW7wUNt-XS4L-sGUN3lVXgt8zwmKacJ3IpYYd20Jwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
برخی از سریع ترین گل های تاریخ فوتبال
⚽
🙌🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103242" target="_blank">📅 12:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ullyv4QXWUyfFa3N2kI0QHz5bqEXDc5yn-hNNplb_Xg2X1Q92gGY8NU0QMkyoNoaahj2wQEbgMvbjzvr_g-w3MlScGreHffFcwYEwkG4dgoR-ovElpym1j3X2wkwk761FWeyBCCMvu-ivrmjX08Sdy2kI3afKKJI-pIBkm15Zk97vq_M6yx7I0kCjQYoYhhLXWCi8RQZcjPxlvNX5IftYA67eX8QofZ7CYYAai170rI_vjyzoDGm-cPnzJo_cv5_KuZmB4DvWqVzqVBDjEuvpD_Hz4sreRd3j_9jXBVpaIw42IQQdBCiG9WBil1zLqmPZezCf-PiBqCTrQAksYGu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THhX7w6C0IjrubHycIgtdJYZ7q788K5-FKVV4NIrWxdRaPT0zLKtm9nMDqftareYjXpB7wRtFNdNF9AL99lFhiPoa2dFY1WlXkUjWfPACUSCRcocyk70GWQaG-D14xQ4rSAxJ0bKtqWuNq_s9D9B1PnG9GyglPxfZtkSu0NPDFUk3ppAIWXrDXfgwk2RNUKsYHq9XJvp266rp-EVCbQnli3f1bAPeklfNWfT3gOwC3ceQIYO8j1IIClNnMH7KqcFq7xpxSQNfZ3tQ1BehHoCmy1b7FXfsuJZia_FotDBP8mPwrTNCrUgQLHrEkNP453yQ_mEsJcjKCr5R6gOqrU3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WAZk6WEXLpVMlO6vb-FRP-kPmNkm6HW16GDFOMybvRtu8NXXyUKhKpf33mdzR56KvABg_7EWL0z4USp2y7aMixxRpm7fOOLyiEzwnf1sfUtN5edwzEwxbTLgbtNoea1aToGS-olQnv-6CRMawtjXgL6HZ2QrhKUqyEL6k9IEVK7aOybOHtZ-b-WTPn2fMBl2O_zOhlJ3emGZrFFRAWwq1dzJ64GgwvuDv_zwhQHFP4AWKTRk3RZT9s5Bt6zIo5EutIHwTEPL7wKa2vl9y3HIwFkNjLs6M9rSxoyu7HjWe6oukGbsPOJJCuA2QHe9SAKitA1yH2hszzgwgIWM-orXMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امباپه ، کوناته و کوکوریا بعد از پشت سر گذاشتن تعطیلات تو تست پزشکی رئال شرکت کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/103239" target="_blank">📅 12:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f4861e800.mp4?token=M7bIZFWV6Z6zSkBEWjQkzlTrl4M3K5s-d9Hm6NFw14-rH2GaWNgqvtjzenEWj4U75ra2qlCCjV-liAToDRCtTuWqOf2YBd4UHAXTt5bEMwMkjPH80wOZxAPvKanHCpfwuWFrdOrrUSic0MNNpfaUeZQbOSeYTkuFnzc3eC8BeVSLpJIpsmVUt0oOH5cIa60mjiO9KIpolsNjOWAwmrhqnW6XS8PLVY66aA-nMS-gywj690Jl4lbpzr2U8Y3PpTQXG9iWvuLuoEK19mA6gsS-HoxQaQD_FQKJa-EmZhqawOcP4vtjpW4YNLwn-h53oyKoPKMOlnebx6tUtoAxeKB-Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
علی‌فتح‌الله‌زاده: مسی بهم گفته منیرالحدادی بهترین بازیکنی است که با او همبازی بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103238" target="_blank">📅 12:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccEVuyVkBw2sqUZRLUOTifU7EAlLE6CWmALI07_nKwRRvxyIIG-GACsSxbY6UCNP5cQSq_TfEvT9YqtFJ4tBWLWRRRnUGYGX0L5RiMcCggW3bPQo_tT6Jm424j0khk6yVWdw4JeDIL_AE99AaLhFvWqoyeu4zwEs-gQnn0V930W0ATYenViI009G3mtrwUikWeQmWSGmSs4zdiuZwOkFGU5zha2whNBLPQgxG1cusTK399VE5cEdpNNAK1fDFbqJF48IjbCwvF_lmnwBycoJN4CBTmg5ZoTUtJi18oIH9Q8Jwd1TBBz0jhaUi6Rq04c85yY1vdL2BmNgcnnyTITWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
بن جیکوبز | یوفا، کونکاکاف و ای‌اف‌سی نامه‌ای مشترک به فیفا ارسال کردن و خواستار یک بازبینی مستقل دربارهٔ FIFA Forward Enterprise یا همون برنامه اینفانتینو برای فروش سهام جام جهانی شدن.
نامه که توسط چفرین، شیخ سلمان و مونتاگلیانی امضا شده تاکید میکنه که اعتماد به‌واسطهٔ فریب از بین رفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103237" target="_blank">📅 11:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82a19a1124.mp4?token=H7y7dmJuKNpMwTxe3PqJy22BqL5RIVOwsExTBA0H0N4N3HRxecm1czrmJ2ss02stxLKWK1BEn83hkitIa_nx2tC_qrYLDun5wDJ0sx2LLf6mW3siK7MKG_uSxroGj53wTyMIMeshRhDfcLrU-H2n1dNZ1NXtCmuNB94sp-KKSPNggic8EDKDSx0BwIHNBjR5Sao71YgAnBqbQfzXmWmQnt5elkcxaX-CTVHBSK0UvfMAxAVoGHOYSP9ORdb_aszPMwW22UJ6U32kvAdvm79DjNWkhSM3OwW-E3E4RgxvttRiOPcbH-knr1pBb-bOcmnbdtbO7g1FxGUzAYnTxrAI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
محبوبیت‌ دیدنی لئاندرو پاردس در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103236" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=A0TVrYE1vaC9LO5DWJuJYCexWggzceBd1wC5-yCJ98rndZzy-grrCkFBtikzMF6d9FLMNrF94PjqKwOsPgx-jIPQyy3fQ5u57SG7d08lE8Ze1B3aSlWi-vWRyuFv-KkL0d1hKEqwu9jvMf8XRQ1FBQcRi3ap0-hr_739UQcK2eStk8qqUZpFs-NLR65IaghB6BMkWVhPqlnzLaLjunWEvfNERwTFqs_2x9pskC-Y0QjnG5RI7KhDnyO9MkiZtbs-3AxngwwbKvrSkq-b_nNX4NI-8vNqe8ByIpZBnuzoNB0Lt7iaSkA5ESWbsEuu3qSbTH3FfDkgQTyziGwj2ogtdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e57eb2f58.mp4?token=A0TVrYE1vaC9LO5DWJuJYCexWggzceBd1wC5-yCJ98rndZzy-grrCkFBtikzMF6d9FLMNrF94PjqKwOsPgx-jIPQyy3fQ5u57SG7d08lE8Ze1B3aSlWi-vWRyuFv-KkL0d1hKEqwu9jvMf8XRQ1FBQcRi3ap0-hr_739UQcK2eStk8qqUZpFs-NLR65IaghB6BMkWVhPqlnzLaLjunWEvfNERwTFqs_2x9pskC-Y0QjnG5RI7KhDnyO9MkiZtbs-3AxngwwbKvrSkq-b_nNX4NI-8vNqe8ByIpZBnuzoNB0Lt7iaSkA5ESWbsEuu3qSbTH3FfDkgQTyziGwj2ogtdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
🎙
داریوش: شجاعیان: شفر قبل دربی گفت اگر پنالتی شد فرشید بزند. رحمتی به منشا گفت بیرانوند تو را می‌شناسد و نذاشت پنالتی بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103235" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103234">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=KY0gErJNkuKW9iQCPSvcvKAlsVzaHqDnP8Y9WPFg4uXaVxkAp6PZ1iq3VhtJtHP3lHSqUXg9NXaWL7fjpT-JDs8jEt2Nj95sKuIinVRZdhwxe-4m2EmWnShOI71J3FdyHq4uiaI39Jrsb-5jq7Nc3IFDkYr9-qTNyLgdkE2VRKNq8fbeDSlSWZw4k0wj-jKLPLDT6CpeI-1UPdEgqLTQAfE5_C-gB-4sCCkQQKo64YH5Wb-AhZDmazeFOmzNMd9XYhZTSeGF1OpsGFK7SAIHbmhYwuUl-RFV5hz6qF6EpGz6dMjvYccRul2LT11YHHAusdQO-JlwpdnT_Re3TPT5Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7df2b7b9.mp4?token=KY0gErJNkuKW9iQCPSvcvKAlsVzaHqDnP8Y9WPFg4uXaVxkAp6PZ1iq3VhtJtHP3lHSqUXg9NXaWL7fjpT-JDs8jEt2Nj95sKuIinVRZdhwxe-4m2EmWnShOI71J3FdyHq4uiaI39Jrsb-5jq7Nc3IFDkYr9-qTNyLgdkE2VRKNq8fbeDSlSWZw4k0wj-jKLPLDT6CpeI-1UPdEgqLTQAfE5_C-gB-4sCCkQQKo64YH5Wb-AhZDmazeFOmzNMd9XYhZTSeGF1OpsGFK7SAIHbmhYwuUl-RFV5hz6qF6EpGz6dMjvYccRul2LT11YHHAusdQO-JlwpdnT_Re3TPT5Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دومین‌بازی ضعیف دومفریس در‌ رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103234" target="_blank">📅 11:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103233">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK1dhlDqL5S6CVcCiQzVsMJEWMvm1c-xNO-F0XHkyVfEOZwjKTndzvmN5HbchGyt9D8c_mgjTK00eydD3DV_MelVUBPjVK5cPQZWpqxrZuwd7nu2C3qdUmpRuz8tjFP6qlRD_cd38639xnXzeTZ1wMV_yv3g166oYeeA4Do2GHrqX-Uy2VFqeou38ivIAI2z2fw5vXncw9fu_d5F0Ng-izSxq6hZKA-8fp-thZxlO4-10xMk2hohZEp8OHXo-Yzlf8zItXKibmq8vSoZMBB6OWQeazASiAXXyoOE_iM6ZVuY67UnnRKgpjGjsl1Y0uX_EaSwjmvpRZpu53QJCvpqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
5 سال پیش در چنین روزی؛ لیونل مسی اسطوره فوتبال در انتقالی پشم ریزون به PSG پیوست..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103233" target="_blank">📅 11:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103232">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llLMBoVpaWIPQBYSCoGwQLbmmWPqBSVH2KgNyeurGLAQgdTaSw5R9QXhbCZreqw8gSezIk-AkVqDK3XuMXmpvsV-0JchwCx_KJuGM1IT2F0czAocEg-s14VdPQp82vCwed7cGyu1YiH86anMT2O2CQRxMNDZa27-CLyU6_ZRO06BM_S5dRGlN2_iinZw_K0c2vwxyTyix8OhtlTaZ6FBzYlqMO0_slf2gCz3I4Z6MuKJctDCF-tOByvpNzdcaEaVk1IVdXml9sa-NRirb439MSmwPmfNqAVUbswEHw1M4OCF0OYiATOwOSlYvQVRqD_HfvAxgod2LHsjnw1ngi-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
😳
جرارد رومرو خبرنگار بارسایی امروز کسخل شده سر صبح داره دوربین‌های سطح شهر مادرید رو بررسی میکنه تا ببینه آلوارز کی رد میشه و کجا قراره بره
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103232" target="_blank">📅 10:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103231">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9jNGQJN6Af28ID1FvtvliUKwa-xAWjy-wXRxMJfQvYSJ-Xg4464nQDmP-TI_KawGX-BYVHsKZIwY0QThpKStOfcI7pybxvKy9NNnbdKJK__gxfBG4xmEgE7NrCZhoOhuZnUCXJmdy-zl0CkDKtlQHDaAmB5JB52MPA4EMiKG5E5NONGYdKvU388eTN4jiLpuz92JAdlup6Ix4to6AvFSEguAvCZ26DD2nwEbd3WYnKOXWy1259uchhoMOe8zCdRfYhqQHSVh0epxSqK4za-RDipnYrs44ShG21YE5C1joBIO09uF6wxuS9zKV5JOaDi6G9ImkRgaxz4vT0GYWzsTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: ایوب‌بوعدی ستاره تیم‌ملی مراکش با منچسترسیتی به توافق شخصی رسیده و مذاکرات با باشگاه لیل‌ در جریانه. بوعدی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103231" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103230">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=BHRMYlLBPRYKGyWs1Iogb87ohKU3UMIsKMejSytqTaC-VHRaLpe6pAISkoaP3eCVDTrD07de0A0Ut3a0zkCVyEO779SLqQy1I4bqqdybzzeBIqiD6uoNVDTPFY-tdsiUYeDHJkaUsDFagXjq6agMatDht1Q76z761mlMJ-zvRCtGOXvPylLUHELXj3pdoCu_fy8yRWCIbVKwbobSxaETG5eADjuzXSoVYzrpploDBXrSJFQwg2f_zlxbGpmEwBOpR0xJ1XJTMA7umRwMs8BTMGRsAnZvd44UjctprKgeGongWdkHM1ibL1FcWhUdnMUfsi5LiSWhz8IsjXq6zKU5BTi8DTPkzoQXzSxHByawkSAzY6ZTjxKs22HS-6NkgfN_YqvTSdlmmews4B0MiFY9NH-Jm23xcIyAthOs2bNv1_gMqxtsVZVqKBXC5aYuROwX1AXVHCa0AoD2HtYfxWkc_21Fn8S25qHafDOUutSpSKK0CtXBpGkksoaUdyT8im7o_SGCypBYih7x_HlkEYRjZ2FSJg_rmBHAKRP2JUkhkEEzzoMGWXbMU7vJG7TAiQT-GBeNww7ag6IGL_PEPUBJBKJ2yQT_MMHsHoTMoT-d50mLc8MyUNiqIEBZ-aT7_cNDLlLO3i6bnXReG7Y2D9k6gkUkm0hHyKJ_WhQEZ1VqisE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8c797d10.mp4?token=BHRMYlLBPRYKGyWs1Iogb87ohKU3UMIsKMejSytqTaC-VHRaLpe6pAISkoaP3eCVDTrD07de0A0Ut3a0zkCVyEO779SLqQy1I4bqqdybzzeBIqiD6uoNVDTPFY-tdsiUYeDHJkaUsDFagXjq6agMatDht1Q76z761mlMJ-zvRCtGOXvPylLUHELXj3pdoCu_fy8yRWCIbVKwbobSxaETG5eADjuzXSoVYzrpploDBXrSJFQwg2f_zlxbGpmEwBOpR0xJ1XJTMA7umRwMs8BTMGRsAnZvd44UjctprKgeGongWdkHM1ibL1FcWhUdnMUfsi5LiSWhz8IsjXq6zKU5BTi8DTPkzoQXzSxHByawkSAzY6ZTjxKs22HS-6NkgfN_YqvTSdlmmews4B0MiFY9NH-Jm23xcIyAthOs2bNv1_gMqxtsVZVqKBXC5aYuROwX1AXVHCa0AoD2HtYfxWkc_21Fn8S25qHafDOUutSpSKK0CtXBpGkksoaUdyT8im7o_SGCypBYih7x_HlkEYRjZ2FSJg_rmBHAKRP2JUkhkEEzzoMGWXbMU7vJG7TAiQT-GBeNww7ag6IGL_PEPUBJBKJ2yQT_MMHsHoTMoT-d50mLc8MyUNiqIEBZ-aT7_cNDLlLO3i6bnXReG7Y2D9k6gkUkm0hHyKJ_WhQEZ1VqisE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🏟️
آخرین وضعیت استادیوم آزادی تهران
✅
قرار است به‌جای دروازه‌هایی که به‌ صورت ثابت در دل چمن نصب می‌شدند، از تیر دروازه‌های سوکتی استفاده شود تا در مواقع لازم ؛ امکان نصب، تعویض سریع یا جمع‌آوری آن‌ها فراهم باشد. عمق محل نصب سوکت‌ها، بسته به مدل ، معمولاً حدود ۴۰ تا ۵۰ سانتی‌متر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103230" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103229">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC6PrQfdLfeiMXcFwxIlpxMhq3i6hlMKTouecq0aH2lM-zJYyK7B6HJaKt_P_m4_4E9FCPNZZbpM-YFSYg_BNt-XRQGJWw8d4A71YuKPc2Rpgs2mmcAKNge0mExPgg6tgqMFydrEgqp3y6RufCjDp_LbnzAmtYIYqmCDYr6qv-kPU_wtWm3xyRtdrKjU-QJVCf5quFVlwLaR3vU8q061n0XhHx94H6uq5thzCgSyUjCNpB3jGUYPwLOrcWYPT6LRDEFGuczRFj1Xpi_Co0VnV_bu1sOHiEHzIMpAYN1PDDtbS6ayj7fDPjTgKofn1SCU7-t-Sj86BhM2xE-Co7Fm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔻
آرسنال برای فروش زوبیمندی خواستار دریافت رقم ۹۰ میلیون یورو شده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103229" target="_blank">📅 10:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103228">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=ur4TLzVBpPFRYtL8qwFFeFTR3bnEfhpj_Pn_YtTkwZ5U2n1yzcDvGLtzEtfhs0ltuutCUdUqIZeMIzzvxpHJp9XuMKxKeK1oU7ajYep49_C2CdNJ2tIkCj3UaSIEZ5kvuu4YADRplhB5gTZOANUbWvLH7R0a5BSX00Xc8I79cXo4EE4-Nx6JewL0Bkk7gpSrBKTFQNJ3lmoMeURzrPzXSib_aIfDw9o3IPcvgtwogKPIoPLqsLcABO_s90zPlj2cSl87e5KF-Rs4z9qVqFoHqAzsz2aJ3VmbXT3TM2LGZmEiznpX-aNa6MZvL90520gLGjwB72s_tV-cWZlNxtQ5mi31WFq9F30xv9LFBixz-1IyjjNQ3LcWKXBds4l1VLO3LEXVOiNLEquYZAZz8SvNMSE_Hf8WjIzgEKHEczWdkMcDYaSMLZ5uSeJxDnBvhn4CkBqTFVk1QuyEHMr3Duh7v1598fSsCbayVljiEZJL7R9L963YELEo26VxBd-hIzWfIw_POs8Ed7Q2gSE8GrH8-txTh3Ln9j8UqsrmOJomQynkWjxgKQ_bnegbVuvHLmXE_yttNsWzUiGe_VeGDeVno9w-AqDCrHJfQwPi8CdtxEeelZkCfv-6aeQlZ3o5KjKqtqR5gzdi4nCthK26SSiVy2twRqL76TDYcb2N2WExSYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8748509dd.mp4?token=ur4TLzVBpPFRYtL8qwFFeFTR3bnEfhpj_Pn_YtTkwZ5U2n1yzcDvGLtzEtfhs0ltuutCUdUqIZeMIzzvxpHJp9XuMKxKeK1oU7ajYep49_C2CdNJ2tIkCj3UaSIEZ5kvuu4YADRplhB5gTZOANUbWvLH7R0a5BSX00Xc8I79cXo4EE4-Nx6JewL0Bkk7gpSrBKTFQNJ3lmoMeURzrPzXSib_aIfDw9o3IPcvgtwogKPIoPLqsLcABO_s90zPlj2cSl87e5KF-Rs4z9qVqFoHqAzsz2aJ3VmbXT3TM2LGZmEiznpX-aNa6MZvL90520gLGjwB72s_tV-cWZlNxtQ5mi31WFq9F30xv9LFBixz-1IyjjNQ3LcWKXBds4l1VLO3LEXVOiNLEquYZAZz8SvNMSE_Hf8WjIzgEKHEczWdkMcDYaSMLZ5uSeJxDnBvhn4CkBqTFVk1QuyEHMr3Duh7v1598fSsCbayVljiEZJL7R9L963YELEo26VxBd-hIzWfIw_POs8Ed7Q2gSE8GrH8-txTh3Ln9j8UqsrmOJomQynkWjxgKQ_bnegbVuvHLmXE_yttNsWzUiGe_VeGDeVno9w-AqDCrHJfQwPi8CdtxEeelZkCfv-6aeQlZ3o5KjKqtqR5gzdi4nCthK26SSiVy2twRqL76TDYcb2N2WExSYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
شلیک‌های سهمگین سوبوسلای ستاره لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103228" target="_blank">📅 10:08 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
