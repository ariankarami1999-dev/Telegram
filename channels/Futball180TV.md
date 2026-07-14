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
<img src="https://cdn5.telesco.pe/file/vbDUPXRmE4AEGMmclH3iI-z3NYy4UU8ToIOq0ntwZy7gCrB49NE9oF1HjSe0ChxWbaFi_Jn4gVQIO4R8SebIFVFYv358Gpk66OD1FNyAsbLFTXQZlmMclvZQGKMRKbCUvpIPb8OXYwOldAZ-w_1eXE9vx3hmASntZOYCgOLSlEaZSc20v8aoFpTSEzvL7GhdevVxzhkk2rWrjwoQCOXuxz5XTGqpLNrDuNZGV_-Ra54ydJ_UZiZDUsDKEntIlYCtis_Y4-W8opPPnYzNAPmcPZZWLK-TjfyCbDHr6Dwtwibio0t45JVYgJy6w0ClQMG7QLy34yKTzkJbcPPp7-cwEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 579K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-100054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed789cb4eb.mp4?token=UnrtCsob_gXWTSpOcAIKFdSqo63naEJ5s6GOtBYVNIx500xtjvWDPRSnR87o7QeOq2Tal5zj9-tXJ83y-xw-uHrRwSEBflLmY8DbLnshkuVp1WGE7zvZ9BFU3A85O6xLGlHCpBHqebPXXi51wQYMJ2reJmHWRWKO1eowLdbEwmhNorOZPOpE0QNQaT8NgY6JxTVRps8x3DNFvIMp54GcjM4vvJJZy_SMkWQX9E4ClU9pDAm3JkVY9EHDeOgm14blbFNaeEvRgqgS4Twj_i9mUHL1Wxuvt_MIcrvZOtBLk2BG3UZXDpE1yMuFCXHyL3BtkqI8XyNz36eZYz71BfDVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed789cb4eb.mp4?token=UnrtCsob_gXWTSpOcAIKFdSqo63naEJ5s6GOtBYVNIx500xtjvWDPRSnR87o7QeOq2Tal5zj9-tXJ83y-xw-uHrRwSEBflLmY8DbLnshkuVp1WGE7zvZ9BFU3A85O6xLGlHCpBHqebPXXi51wQYMJ2reJmHWRWKO1eowLdbEwmhNorOZPOpE0QNQaT8NgY6JxTVRps8x3DNFvIMp54GcjM4vvJJZy_SMkWQX9E4ClU9pDAm3JkVY9EHDeOgm14blbFNaeEvRgqgS4Twj_i9mUHL1Wxuvt_MIcrvZOtBLk2BG3UZXDpE1yMuFCXHyL3BtkqI8XyNz36eZYz71BfDVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
همچنان از احترام مردم روزاریو به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://telegram.me/Futball180TV/100054" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d6661353.mp4?token=UbvQl2r91pjYV8pP8tpTdvXbQ9530XCZntUmH7a-PQDLbYzc9blPeV_U1Wj42ayqLfjQvwasvW1CQjN0d1MDZyQT0LZMHvsSnMa58qjMwoqly7E3ZjliTKPHXkJR1uvUrkxITwJyrCQw048i7LACD6mcNoTuK-JhTot7i9Mzg9Vi6CFfQLu-vbVapau84eg3SKfLfWzX2aR7IkFe5ro-0Fov3ePtYg4-8buC-qZL1hGAwYWWT3F4JzQipungS3u4l88cdnYaKjAhoFbU8KtTv8GMp6FE6zLI24bti0NoyfYl6lWwV-W071JCJXQ_ZieLoHFf2s1qOGvU_8pxm8Rj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d6661353.mp4?token=UbvQl2r91pjYV8pP8tpTdvXbQ9530XCZntUmH7a-PQDLbYzc9blPeV_U1Wj42ayqLfjQvwasvW1CQjN0d1MDZyQT0LZMHvsSnMa58qjMwoqly7E3ZjliTKPHXkJR1uvUrkxITwJyrCQw048i7LACD6mcNoTuK-JhTot7i9Mzg9Vi6CFfQLu-vbVapau84eg3SKfLfWzX2aR7IkFe5ro-0Fov3ePtYg4-8buC-qZL1hGAwYWWT3F4JzQipungS3u4l88cdnYaKjAhoFbU8KtTv8GMp6FE6zLI24bti0NoyfYl6lWwV-W071JCJXQ_ZieLoHFf2s1qOGvU_8pxm8Rj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وسط مصاحبه عادل فردوسی‌پور با هاجر دباغ یه لحظه روسریش میفته عادل پشماش میریزه
😂
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://telegram.me/Futball180TV/100053" target="_blank">📅 15:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100052">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bfb6b282.mp4?token=Yj3WNcjvwk-wyEDaRP58r1yKwlyK4anWwWsgQY0T2_YzJoTAMI1f2PozY97xeZw2VKVOMIiFaSLUEuCVkzMrihHNndshSklBdqOxagz_kzPFYDYlBrp4inM9iZMBS-aN-w4ImhespeL_Xuo2hv635IWVIm0TQEnR8M7C5Smu_z_GV_roUd6TQlEb92EtTKVvt7-YyLpCswCh3o0QV3wTJGuDq4QI78dNRqob-dJCd18UTrG-X65MTPJZ4IwOiwYnnUy31_mFP9HyJ3lqjjor1mKoBeBiBvGuuFv1ossaR6koJVlUa-ahuKgwFVWb_hOph9IfArxDXPX_GVip2DElZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bfb6b282.mp4?token=Yj3WNcjvwk-wyEDaRP58r1yKwlyK4anWwWsgQY0T2_YzJoTAMI1f2PozY97xeZw2VKVOMIiFaSLUEuCVkzMrihHNndshSklBdqOxagz_kzPFYDYlBrp4inM9iZMBS-aN-w4ImhespeL_Xuo2hv635IWVIm0TQEnR8M7C5Smu_z_GV_roUd6TQlEb92EtTKVvt7-YyLpCswCh3o0QV3wTJGuDq4QI78dNRqob-dJCd18UTrG-X65MTPJZ4IwOiwYnnUy31_mFP9HyJ3lqjjor1mKoBeBiBvGuuFv1ossaR6koJVlUa-ahuKgwFVWb_hOph9IfArxDXPX_GVip2DElZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
در انتخابِ دوس دختر خیلی دقت کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://telegram.me/Futball180TV/100052" target="_blank">📅 15:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100051">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxcgB8nsPxxFx01At-T-qbPaWbyEVEIJDvP_svPi4wil1GfaLnuWQCO7xIGQQye0bkfQvJQF023KI6XyL4jTcNrmz_Fpiav0dUEb_QmHEvWz3zLKGFYskHONcriUIwnziqkW58NB-i3yQ_U6FTuh7mAdBgIGJq0gf0rXEb1IlNH-zbwnen10mtacdbxasA69WffdJNtAbqevyBRfMH210k6gfQxZD0c--WMpDZ9c-5qeKUMAx8cu8a2Udoujj4-VcGGx0y6S800AudCKXVp8RzeVmlABYR7XsdfPOfsApNf8tsPXBsBmanUY8rq3QDoTza5BR60V9sFaUz2fuwYlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
یامال در این فصل، در تمامی مسابقات، 55 بازی رسمی را به انجام رسانده است و در مجموع 25 گل به ثمر رسانده و 18 پاس گل داده است (در مجموع 43 مشارکت مستقیم در گلزنی) و 3711 دقیقه بازی کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://telegram.me/Futball180TV/100051" target="_blank">📅 15:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50041dee62.mp4?token=cyCqGPggZf_zcI10dwaPbKPVBEL1U4uRFIg9NlBZCN1YPwegbVfun_SEJb5sdisUE8F_RaigOS9r49OnMxE4UKNn1koSyFcQJSXBJHkTjyQIj9SU85CmL5zz6_pu5IbZ-VEJH0QXPfC2LIdi4sGJm8XKtSadlEzg9dAi_eS0TgE1S1U38wAmRyqez6Qqhjg2oZQ4tSLKOYFDWLKHC_z5w-zi4ZkhFc3ATbDiToDJDKSWUyzF02qbYup-6oSJZt_fNmCOfCho_66t0GR_5JI97mBITIuOhRZyjiy-kiNjM3TGVNzbaFVljbKbpTKs6kZpslooHrWc5QwpsTqY-a9QYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50041dee62.mp4?token=cyCqGPggZf_zcI10dwaPbKPVBEL1U4uRFIg9NlBZCN1YPwegbVfun_SEJb5sdisUE8F_RaigOS9r49OnMxE4UKNn1koSyFcQJSXBJHkTjyQIj9SU85CmL5zz6_pu5IbZ-VEJH0QXPfC2LIdi4sGJm8XKtSadlEzg9dAi_eS0TgE1S1U38wAmRyqez6Qqhjg2oZQ4tSLKOYFDWLKHC_z5w-zi4ZkhFc3ATbDiToDJDKSWUyzF02qbYup-6oSJZt_fNmCOfCho_66t0GR_5JI97mBITIuOhRZyjiy-kiNjM3TGVNzbaFVljbKbpTKs6kZpslooHrWc5QwpsTqY-a9QYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
جو فوق‌العاده تختی انزلی از زبان مریم ایراندوست؛ جایی که زنان هم در بهترین جای ورزشگاه، فوتبال می‌بینند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://telegram.me/Futball180TV/100050" target="_blank">📅 15:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693e2b7cf3.mp4?token=BDXA-RlzIy56PuH0JRQ6IFO_p65qOVBxFczeBq2ZdO0gNmQHD93N59F2lzBSfdBtWx-Ky_64YlGY6cO3V_o0QRqXNwGfHnaC7w5fNLlvZIOBmxKNzHvztrV67ur1SIuq4Sb_gi2FSJgplfWc5X4gRAy-kx3pY_x7qwk_qpxv3caOv2m-7x4Cv99PIA0sZzUEeBoE-gaPHuYobKA3WLjdRhJQGUA3qsB-gVXNRsHw9-98YNmElW1NgeowOr5XvOAiY1yp43R6Lklxr22tSnv6W1183YvS9IF8krN6NCuTTXw-jo8EDE7xnBXmdTyYrLOOU51cDn9FYbnrBQakpZBEXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693e2b7cf3.mp4?token=BDXA-RlzIy56PuH0JRQ6IFO_p65qOVBxFczeBq2ZdO0gNmQHD93N59F2lzBSfdBtWx-Ky_64YlGY6cO3V_o0QRqXNwGfHnaC7w5fNLlvZIOBmxKNzHvztrV67ur1SIuq4Sb_gi2FSJgplfWc5X4gRAy-kx3pY_x7qwk_qpxv3caOv2m-7x4Cv99PIA0sZzUEeBoE-gaPHuYobKA3WLjdRhJQGUA3qsB-gVXNRsHw9-98YNmElW1NgeowOr5XvOAiY1yp43R6Lklxr22tSnv6W1183YvS9IF8krN6NCuTTXw-jo8EDE7xnBXmdTyYrLOOU51cDn9FYbnrBQakpZBEXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تنها سوغاتی ارلینگ‌هالند از آمریکا
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://telegram.me/Futball180TV/100049" target="_blank">📅 14:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKD7GZjGhHwWccrU2Xh8Vif6Sf6ZQ8rjYtrZ5dC1zvRfP66ix4Qml5aRxL09Oe6CdL5qOgrZzrDwWfDmqZL-RySHXBaYE838vEO_CeGR9JmZyDr3fuaXcO_SeGE-ftZ0f3Ck-jS0ihFXp8bO9QNi-TkOYJ8KUzrQ6nzuvQjxJyUAwzqgFrkq_aQ0WMm-D03wnhj-NbzcDNfH2WBPKD9x6sBvlMv50p4lZcua2n3LnMZUcZxT6hbhlE1iMyTuoypBA_YTnN9pnxggOOu6iLqWA5awSjrRepA3tQ8fsyGk_CvJb39z19vPOqU6ZwQq8dBEXjBVXi3O3VSblH0aEuJkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
فرانسه برای دومین بار در تاریخ، در جام جهانی با اسپانیا روبرو خواهد شد. اولین بار این اتفاق در مرحله یک‌هشتم نهایی جام جهانی 2006 رخ داد و فرانسه با نتیجه 3 بر 1 به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://telegram.me/Futball180TV/100048" target="_blank">📅 14:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t95N5IBBt39kLy21sztBfaeXCezWhcRa9BfBCxDranTa60VsPhlWgOYScVY-0IDxsvjFRYyZvki70Gxu5ioKNM1-OUECL7ClRuDw_5LO5tX-GG1sPk1pPERFrhcQyJityfOCEB16AOffGJmIWhgs1d8RulmbSNhWHrTxnV6DRgQXAjIBeLKw4DL_oxPbyN6sFyn3fJog0FICORDLSM_G7aL7BQIrjGUh27f-6zk8mujDMwaoyC-hiybXJNShUQetHS8nj4BCYwsITJzzB4iNYJKuHwGtW6gq3EGBvaxEH3o7SE4tp87RKIt2J8ayKSw-V43F8q9pnsMGrRQR4UV2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۲ و فعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://telegram.me/Futball180TV/100047" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100046">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBlrru3acpDuA3ZKUt0KJg2tIIBd0pmVVrch-b5NdMvmSsAJxYNvjiqRVg3RADHWQrLWCGEyOpzNgvfoolULfLmQVR3PqPAy_ecv3o79f7VAvTWegQmiXtTwqnLP0Q4LdTpanJJiBhvJ4ZKIOdtlI7ySBGckCATiY9tWl642k9YNXSUSp2dU-KUbtpbzOyL-wkFRaGCAmSfef9mVD5LnVQkeMzj8gu-ML8E90mLkTko4hfgFO5I3mQrBdcg5ub3OwPxglo1GgmsPfhdZBeCouZtjutpQt0UEGIJGQtaV8z8Ek0ArMOAJQXsusO96NMkAclIUoBr-IOdor65UjFKcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسپورت:
خولیان آلوارز با وجود پیشنهاداتی از پریمرلیگ انگلیس، علاقه‌ای به رفتن به این لیگ نداره، خولیان فقط بارسا رو میخواد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://telegram.me/Futball180TV/100046" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100045">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD8YF3XU9cRtVEhXvMmSoh-mLzlGRu63R30rhymlBqGeAeUp8qCic2PAyv0VeC9cqA4aMmRpy-T7gnVs-vo6_fC0X5NmkHVWvqDMUh-pBaytplbXQ7QbOpze1IKVPIlFu39hYOJOvc9bNdvXGAYvKqIAbz88-NeiWRaqTex32eEV5BSyYULr-yRDOkwSTmwRc9RjNNZF5P81PEoURxMHg0ERjzz4eIpFx9hvN-8nFH1H8c4DQNibYfCa5lpyf3Dbb1TZKrWoUnNmP6nZndl0uklTmLhij9Clh2KtVfKDlXXY2xctHWfpAis7e8O0PDrKQPlx5tTcOhGvtkiiJ99iag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ساشا تاولری:
الهلال برای جذب سامرویل وارد رقابت شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://telegram.me/Futball180TV/100045" target="_blank">📅 14:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100044">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3edea28603.mp4?token=AUwqoyq48FkOa5lOAdghuii4WYbtVDOqCDGRmBmSGo-O3PFwtnLsWDWzP8UhflpXWSjjXC02FTXTUAvIhyAod8zNLCZTYkXpBPpWnqOEHP-t_3U2fOq7Tpg9We9iEzhHjMSn2x_6iz0OO3TrgaWw2ivXO9IYU2BOYn1xsRARsuQXykDFv9NXMSt0dFFA2Ry2Bc9PtrE6uA018-gtlXTqrKu650XbTUcbNFsO595SRqUj_XbkAWLooGvDBD57UyUe7QOX_cOGvRvXzARzzWxKJ6kk6S9Nuctv2tw05xHz2XQsd9jE15XK0Dd_7_f-KbJXEJ9S936Iw_UaMLrBTLVy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3edea28603.mp4?token=AUwqoyq48FkOa5lOAdghuii4WYbtVDOqCDGRmBmSGo-O3PFwtnLsWDWzP8UhflpXWSjjXC02FTXTUAvIhyAod8zNLCZTYkXpBPpWnqOEHP-t_3U2fOq7Tpg9We9iEzhHjMSn2x_6iz0OO3TrgaWw2ivXO9IYU2BOYn1xsRARsuQXykDFv9NXMSt0dFFA2Ry2Bc9PtrE6uA018-gtlXTqrKu650XbTUcbNFsO595SRqUj_XbkAWLooGvDBD57UyUe7QOX_cOGvRvXzARzzWxKJ6kk6S9Nuctv2tw05xHz2XQsd9jE15XK0Dd_7_f-KbJXEJ9S936Iw_UaMLrBTLVy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
نظر فابیو جانواریو ستاره سابق لیگ‌برتر ایران درباره عملکرد امیر قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://telegram.me/Futball180TV/100044" target="_blank">📅 14:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100043">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2OkSvZkN3nsnJPrLgPlibOXBQ5l4zhFhmG5umljwUx65qARX0tCAnF2NnlwkNgwAi-2OwPfM8D_2CthL3jmA7j15j8QW-pSyNvqShHWdAOV5DM_b51xBqvQJNwcVgpMVUN9AFb2cM53Mr-pcOur-KF3UGwFMdL49lunIwTadv_2weQ7oe9e0hw0PmapSEcu1jjHReL4-w1n4-W3jf3QVS6DZxVqF5wtiArmlfPvAKeqF7p5zv4MaxTcRVcwIpBCWepVgz6wpozV6V4u96zH_UQw6VM1f-DYJqoIZgASKqGnzek47xDhi_FIgr4UrTU12TUXs8xWNsTVlQGgQnFYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
ترکیب احتمالی تیم‌های ملی اسپانیا و فرانسه برای بازی با یکدیگر، طبق گزارش مارکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://telegram.me/Futball180TV/100043" target="_blank">📅 13:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100042">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af31abf33.mp4?token=toE9u5s7M_chwBxkSTWlH8ehnkLmZDA18OD04mChpD7QkiAH1pnLLMJc8y4O0Xm7TsR-YZS4BJZYhzRN5VIUena85UiiBwQSn0kmZlk5X-76tDlAoab0ii6IoM5IJ9OGz-lck7UqYbkZR-LVcVs5NymrfSy7nkeonecmztwwbpTydaZp7vR4TsCX2OP0o5mr92IJ_QBHyEB6fkp4BcTmSmmfwnkViVaYofUwwV3CtVPrvsk-THMqTzU9a2wDQUDmwckgaPuYkW1bhkr9mtxDQ5zKW_rERtbMbttHJRoJGyILdfADJ8D3IJfMw-EHxh5w845zGEKp2VIB6WkBnIaN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af31abf33.mp4?token=toE9u5s7M_chwBxkSTWlH8ehnkLmZDA18OD04mChpD7QkiAH1pnLLMJc8y4O0Xm7TsR-YZS4BJZYhzRN5VIUena85UiiBwQSn0kmZlk5X-76tDlAoab0ii6IoM5IJ9OGz-lck7UqYbkZR-LVcVs5NymrfSy7nkeonecmztwwbpTydaZp7vR4TsCX2OP0o5mr92IJ_QBHyEB6fkp4BcTmSmmfwnkViVaYofUwwV3CtVPrvsk-THMqTzU9a2wDQUDmwckgaPuYkW1bhkr9mtxDQ5zKW_rERtbMbttHJRoJGyILdfADJ8D3IJfMw-EHxh5w845zGEKp2VIB6WkBnIaN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تماشای فوتبال در کافه‌ای وسط استادیوم؛ دیدن بازی فرانسه - مراکش در یک کافه که نزدیک‌ترین تجربه به حضور واقعی در ورزشگاه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://telegram.me/Futball180TV/100042" target="_blank">📅 13:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100041">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff64783daa.mp4?token=HxRRaPzFsg731n-t-tFU-DZ8wXOVae95_DesjnxDrdqYOycRl2DRzQcBTSMd-NRE5zPVh3itmErvnD_fSCawqiSId5P2EseqA_LkDqNtFcmb8O9y_cRzLa2yV3Mls6OftXQ_MA_TsnnQzjJ9IPhqtX3g1WgSMj1VVxVNeM89vOC0Z2Bbte_SSnJiIFaFdITR37H1HwdG7ZWw8-ljVvAJEJ0eBTTWz0SALo4rbmUKALWhKA-Jh-pXGLEVZbK6CvhEDPZug34I9vWwph-bZchhoe3vdRhfh7Pz_zQYunTVfW0dCpKLXJpYNToVOdrTFL_ZC1rkH_QwRhzGrHu_7KEw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff64783daa.mp4?token=HxRRaPzFsg731n-t-tFU-DZ8wXOVae95_DesjnxDrdqYOycRl2DRzQcBTSMd-NRE5zPVh3itmErvnD_fSCawqiSId5P2EseqA_LkDqNtFcmb8O9y_cRzLa2yV3Mls6OftXQ_MA_TsnnQzjJ9IPhqtX3g1WgSMj1VVxVNeM89vOC0Z2Bbte_SSnJiIFaFdITR37H1HwdG7ZWw8-ljVvAJEJ0eBTTWz0SALo4rbmUKALWhKA-Jh-pXGLEVZbK6CvhEDPZug34I9vWwph-bZchhoe3vdRhfh7Pz_zQYunTVfW0dCpKLXJpYNToVOdrTFL_ZC1rkH_QwRhzGrHu_7KEw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
موزیکی‌که بیژن‌مرتضوی بین دو نیمه فینال جام‌جهانی قراره برامون بخونه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://telegram.me/Futball180TV/100041" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100040">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3cb94583.mp4?token=ayZxxVxAdGKEZoqIbXrtNyUTSPkJED5F1U5Jn7bZff9jtcsG-MP_vcxqMsxqAno5rxD7hnrEBZ_Sc8S7sNg5bIGOYNgenZjOO1ACBlkQ9aK1EYm4aorF2md3lZHCBUM-5o9FqvHCvQNjOlrdr-Zife6Ak11BzFdIa-lqWK8_hO4rMANSiv7fy8s6yMoHjpmKMI0wr-EUBrmGWkY64GfWp0sYRQV80FAb20mc1K1IuY98PXpAJPeLR92Ilom0YqSbMQZOhs2ni8lsvgSmriNBiWYlHR-uHyVqC1OvjssNEPL8gL0cHM0kbtcrZJs-Ti3J-bz89kWY1Vi_FB2YK_uopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3cb94583.mp4?token=ayZxxVxAdGKEZoqIbXrtNyUTSPkJED5F1U5Jn7bZff9jtcsG-MP_vcxqMsxqAno5rxD7hnrEBZ_Sc8S7sNg5bIGOYNgenZjOO1ACBlkQ9aK1EYm4aorF2md3lZHCBUM-5o9FqvHCvQNjOlrdr-Zife6Ak11BzFdIa-lqWK8_hO4rMANSiv7fy8s6yMoHjpmKMI0wr-EUBrmGWkY64GfWp0sYRQV80FAb20mc1K1IuY98PXpAJPeLR92Ilom0YqSbMQZOhs2ni8lsvgSmriNBiWYlHR-uHyVqC1OvjssNEPL8gL0cHM0kbtcrZJs-Ti3J-bz89kWY1Vi_FB2YK_uopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پیش‌بینی قهرمان جام‌جهانی توسط گابریل کالدرون سرمربی سابق پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://telegram.me/Futball180TV/100040" target="_blank">📅 13:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100039">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8026afaf.mp4?token=WKTa-e5GsmXs01dBOvD3JEnUEMtW9B39l7oe2mWOe96bt4mVuXzn2Lz57wND-2sgBFOgqG74yg5z3rmKvzu4BQTFT4oI9dKjMWCAOF73u-l1bspjp48TKC-S_YvgIQTo3tQsDFLhJxhl5FdH_R7JtPvjwd_v8vUUN3kQyrN5a_pJ9W7PupzwZkmg9b6hdTvRwl6oi9KD6k0MQuxYCqu3qcr2eot2kDOeebTiLvkg4CtoY7fLk6vh0mChG6nHmOfIncsWK-GsU-GEKZg7b3k-mYzjPg8unW9DOaZj2JdZHpWuL2L-N57oDw7ifsMNwnm3s20CnyoZOuZI8t4sB2vMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8026afaf.mp4?token=WKTa-e5GsmXs01dBOvD3JEnUEMtW9B39l7oe2mWOe96bt4mVuXzn2Lz57wND-2sgBFOgqG74yg5z3rmKvzu4BQTFT4oI9dKjMWCAOF73u-l1bspjp48TKC-S_YvgIQTo3tQsDFLhJxhl5FdH_R7JtPvjwd_v8vUUN3kQyrN5a_pJ9W7PupzwZkmg9b6hdTvRwl6oi9KD6k0MQuxYCqu3qcr2eot2kDOeebTiLvkg4CtoY7fLk6vh0mChG6nHmOfIncsWK-GsU-GEKZg7b3k-mYzjPg8unW9DOaZj2JdZHpWuL2L-N57oDw7ifsMNwnm3s20CnyoZOuZI8t4sB2vMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای مردم مظلوم جنوب ایران
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://telegram.me/Futball180TV/100039" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100038">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIF4HJp7B7ig0nQdpHEnmADMtypaVLJ6yS8yaH5ffYautWbUXHRctES4gegaoYFFZN-YcdIsyOBRrQjXNSxyahR2qBd7HVR2Kh8ogywR9TdPrOpPwhprYDnfMo3C58u44x-tR6ghUsDHaty2CVJHor2m24rCBS4SdDI4ox3GeQbiGOtVQgNL6W_6gX00wphTCB6gqLGOeHQN0ZO-Oq-rF__WWl-b-7PTYsXsjbVxMKY8DFJsQY4mqYZTunNhopzWhEtrYjVJd1gI1bl42gbQBEFtVe79Psc1Qv2iHWQEoyNvy8zRWrUbcJlQNUAQyazcjkDZLr0i5PfV-bC5uNPjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
قرارداد امید نورافکن با سپاهان تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://telegram.me/Futball180TV/100038" target="_blank">📅 12:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100037">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7a16d712.mp4?token=uMA6J066LTIliZ-EGkmtZJO4ICmAJtBKwGT27yCCr9h1ZLK9vilYuwu_HrcvlouOZfGQBWOjV4P7umPaRG1q86mNJ2bu-3-V2ZMcUMVcO0WA_2zi3RtqxuoN9XVyWUi9Y6otPGDem80MvOWXk_RbstXdm49MSfdXkXapjv904X_RL88Szye9Gy0-PUz0dl-A8O_JEYOUVBilVHcdz3fhmEy2RP2VMWvIf3N9O_W2UhLbNfeEtNO2ABPgsq8GTRnfucCShT3bkoapRy9ScP_yRBVgPHoDme6GKeMwt38bGzJnc1sqejC08UM8qONAxS672fTSQ6j8m1Lnpd_2MKmHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7a16d712.mp4?token=uMA6J066LTIliZ-EGkmtZJO4ICmAJtBKwGT27yCCr9h1ZLK9vilYuwu_HrcvlouOZfGQBWOjV4P7umPaRG1q86mNJ2bu-3-V2ZMcUMVcO0WA_2zi3RtqxuoN9XVyWUi9Y6otPGDem80MvOWXk_RbstXdm49MSfdXkXapjv904X_RL88Szye9Gy0-PUz0dl-A8O_JEYOUVBilVHcdz3fhmEy2RP2VMWvIf3N9O_W2UhLbNfeEtNO2ABPgsq8GTRnfucCShT3bkoapRy9ScP_yRBVgPHoDme6GKeMwt38bGzJnc1sqejC08UM8qONAxS672fTSQ6j8m1Lnpd_2MKmHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
برای درک‌صحیح خط‌حمله تیم‌ملی فرانسه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://telegram.me/Futball180TV/100037" target="_blank">📅 12:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100036">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm-upj4bm-d_c4OF2UFaPmDMXNnMx_D0826Ik0YQ4zSQvqydT4pu8xRqywIz0kJ59XrNBuvV39KK0yyshTis08Sws31nAOAhWet67aUH_Em9stxoZ0dqpP6JN3iyJXdt0gnXflk6NwegerYImAh19nvmc24Ue4rTvR8lrtTTSPht7yg98pQfbeo4Mt5gbHNF-AeK75mb7TEPYanwNh70f9AaqhCV8gssHtnRipBav0MpgJ4p9gApuInNzC1uGO2WWt5WUU07rO09Y7o9ScLI6CW40Sw6z7xTE3KL-mmQlMp7KsLi90MnDhIm2f6GEjkX0y9_DCm2tszedv-P3mL5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
قرارداد فابیان‌رویز با پاری‌سن‌ژرمن پس از جام‌جهانی به مدت یک‌فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://telegram.me/Futball180TV/100036" target="_blank">📅 12:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100035">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZANI70LVUjDCqNmso27XTOW-UeGn4PzhfjvXzdcu3-D9B5HvPBo8NYsRwQs_ZJT6S6HQcYyTx9qtSe9TIWfPleUPSnEHYXnTjnZSloHIAQkUvkKyTrU2fx6vfvGFs0xxxGeloRnvrugjHH-sMrIalrk9VADTDF0nAnZXsQSW1XFKd5cVE1X3q_ehbtYFvfbJlt3vcP1L2-UjKW9a_kZQGO6Si35kYULE1JxlgonfXs8B6v5vqIE8u6R37GLLV8AXv8rbOVeLaUmk9AviVltHjRwh0DyGoggWuUittfXnxngEsnCRy_RjvPTnO722i90HUzjtMKzuzGTTqffA6ijiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://telegram.me/Futball180TV/100035" target="_blank">📅 12:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100034">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mssrCEQrmsle3mItVnvGiBPLbzP7ViqR0mqOcjkOveYNY1aYf9lWh78MiAB_mowa3RbofobH89KkKb7hxpW9pUoPlBBos_lz3_P0oC1mqRIzof1rCYOEqlAimEUC02i1l87xaheyMPH3VQCC1T5oEqocmK1nmlfI1_tH3PEQ9E3BRddru7XfGgv43nCHVJNxzjbQIKVi8QUUwCLJeSg2IUO-T7QelSo3FbpC6NztuzUVGBVXcb6Ip2ioOdvM5L2D6Y2wLo_V8trY0ugdpta5dTkQk9-p8BAzKVjbCRBp0X_QAgjlhHYmv7xMJXVbkB4WAtX4mU0iaxByVq-_vmrGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: باشگاه منچسترسیتی بدنبال عقد قرارداد با ایوب بوعدی ستاره جوان مراکش و باشگاه لیل هست. این بازیکن ۱۸ساله ترجیح میده یه فصل دیگه در لیل بمونه اما پیشنهاد ۱۰۰ میلیون یورویی سیتیزن‌ها ظاهرا لیل رو وسوسه کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://telegram.me/Futball180TV/100034" target="_blank">📅 12:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100033">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
🏆
🇦🇷
ویدیو جالب و جذاب از نمره‌گرفتن لیونل‌ مسی در بازی اخیر مقابل تیم‌ملی سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://telegram.me/Futball180TV/100033" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100032">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc8dc3115.mp4?token=r8ZFjQX976y98_7AZbz8sprGOWZal4IoOR86ev9bZhZoATRKpfZ-rnmv5eH0wTUBoRVTAGjGtVZ0h049NCoks0g1BV1S9jmod5sVW40FkcUcgo7ffMxS3_Lb9LXRLsYhFivaLHrHcTzQP1pUe0YU5-9ly9OpFHSb5oMGWuAJgFf7Bnnv7564zv6dxn0lOLPvT1T4PYOplPM8vLkZkvRJs-isT7OWR-jJ9WKXxAn6UbasLqaYhmkvTY7ZtV5_LLXKmAO2Q5S4K2wErldVzSW9q9fdMddsa00wuET_dB4U7p7nunPsH2MhLGjhxuSrwxOooEW1J_NZ-aro9hQ4Sr-aI4SB6yIzVhLRcO0vVQIhaFhIWxLWdvZAUjzDE0IrN3m44z1YCCbXtra17OOxek3-P8DCj4WvmvxG0HUz0V7ShMRokJMPsdaD2rldPu1rhQpTn0l5tCfTDw3XXZezGaSyoUEbuGwuyvNR7pOlRJRAo2axBPEea0ZDPz1QRS1KiFnWFOc0Y4v9WkCCgMsPARpP6p7iTpsJgqnOQ2Elz4YHXdKzNBglEdkZR7p_KDodwvexrCYRSKkDiUcxzd8RRkMiwvbsfWKtVCzUmp5nEskcZr8j0hbHt4J_qUSXVTqEIY0a5N8NXLa3iCKJ332PnOJJ5lR-47_ynk-hA4iBteO4iTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc8dc3115.mp4?token=r8ZFjQX976y98_7AZbz8sprGOWZal4IoOR86ev9bZhZoATRKpfZ-rnmv5eH0wTUBoRVTAGjGtVZ0h049NCoks0g1BV1S9jmod5sVW40FkcUcgo7ffMxS3_Lb9LXRLsYhFivaLHrHcTzQP1pUe0YU5-9ly9OpFHSb5oMGWuAJgFf7Bnnv7564zv6dxn0lOLPvT1T4PYOplPM8vLkZkvRJs-isT7OWR-jJ9WKXxAn6UbasLqaYhmkvTY7ZtV5_LLXKmAO2Q5S4K2wErldVzSW9q9fdMddsa00wuET_dB4U7p7nunPsH2MhLGjhxuSrwxOooEW1J_NZ-aro9hQ4Sr-aI4SB6yIzVhLRcO0vVQIhaFhIWxLWdvZAUjzDE0IrN3m44z1YCCbXtra17OOxek3-P8DCj4WvmvxG0HUz0V7ShMRokJMPsdaD2rldPu1rhQpTn0l5tCfTDw3XXZezGaSyoUEbuGwuyvNR7pOlRJRAo2axBPEea0ZDPz1QRS1KiFnWFOc0Y4v9WkCCgMsPARpP6p7iTpsJgqnOQ2Elz4YHXdKzNBglEdkZR7p_KDodwvexrCYRSKkDiUcxzd8RRkMiwvbsfWKtVCzUmp5nEskcZr8j0hbHt4J_qUSXVTqEIY0a5N8NXLa3iCKJ332PnOJJ5lR-47_ynk-hA4iBteO4iTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیش و مات شدن استاد کسب‌و‌کار مقابل ابوطالب
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://telegram.me/Futball180TV/100032" target="_blank">📅 11:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100031">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601b5e5990.mp4?token=WtAx_w0tOxphklPh6wykhFuyJ1u9VpzoGmot_o6ir5EJEYdCQU2LpDsab-aTHh31R-3CYy4uDi17k6LNTAhGErL4eLjOefBVGgzg8AEC8a9oTb4mSjUid8Rx-56CWS_znsMewJ0VQwJg3kuz1Z2DCM35r0ZqtZwFMOwAaKyqKdLy1ORmFx8aQEJ2NZFwuBYwJkcs6iMCzMpjEJ1H03ItpFrhphXa0pSWoF3NG4hiM0ipEVo78jt0zglH3JExihwb4Lo9-8rIDWsUmAGd_lKsdTVgdb3vne2ywRh1vM1OVUdT7FsDvOjpbnmYjxDJ5AT81d4RTOF7pXD1veqvDIzrCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601b5e5990.mp4?token=WtAx_w0tOxphklPh6wykhFuyJ1u9VpzoGmot_o6ir5EJEYdCQU2LpDsab-aTHh31R-3CYy4uDi17k6LNTAhGErL4eLjOefBVGgzg8AEC8a9oTb4mSjUid8Rx-56CWS_znsMewJ0VQwJg3kuz1Z2DCM35r0ZqtZwFMOwAaKyqKdLy1ORmFx8aQEJ2NZFwuBYwJkcs6iMCzMpjEJ1H03ItpFrhphXa0pSWoF3NG4hiM0ipEVo78jt0zglH3JExihwb4Lo9-8rIDWsUmAGd_lKsdTVgdb3vne2ywRh1vM1OVUdT7FsDvOjpbnmYjxDJ5AT81d4RTOF7pXD1veqvDIzrCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تیزر جذاب از بازی فرداشب انگلیس و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://telegram.me/Futball180TV/100031" target="_blank">📅 11:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100030">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8d222e07.mp4?token=PMgqZGsFEOTB_Cj4VTSfc8zLhmchjvLi6bdBaGwGW56aAetmEtJFeBJlzu8oO9cdaU4qmz_GxrCgstqVvO35eEx3p3YYHXGXvwLWbadrDFkKQ8elxaR1NDwkc8c49CUI9_p1F2wni8yaz-VxzSc9Q-V1lsy_eSG8wOGmLSOcfZ9MxCfC58kp9-vSW5EFMNk09ncz1YWbq93cVq39Z_TU2ADmhYmknOBFyDkCZPPZ2XId_5iZgDGYg6Ro3Noafy_XKZ6RyyouvtZVRwBTQr7XYooUH-nm03Po4875EAMzYRi4dB5devLGy3TZgmHV0b-Ruqnu2p31keDeXXE55zDIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8d222e07.mp4?token=PMgqZGsFEOTB_Cj4VTSfc8zLhmchjvLi6bdBaGwGW56aAetmEtJFeBJlzu8oO9cdaU4qmz_GxrCgstqVvO35eEx3p3YYHXGXvwLWbadrDFkKQ8elxaR1NDwkc8c49CUI9_p1F2wni8yaz-VxzSc9Q-V1lsy_eSG8wOGmLSOcfZ9MxCfC58kp9-vSW5EFMNk09ncz1YWbq93cVq39Z_TU2ADmhYmknOBFyDkCZPPZ2XId_5iZgDGYg6Ro3Noafy_XKZ6RyyouvtZVRwBTQr7XYooUH-nm03Po4875EAMzYRi4dB5devLGy3TZgmHV0b-Ruqnu2p31keDeXXE55zDIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🙂
تفاوت پنالتی زدن در زمان فعلی و گذشته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://telegram.me/Futball180TV/100030" target="_blank">📅 10:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100029">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxuh9feT9LfTlleklj0wF6-pXVioA1G3UY_sOCcjF-xT1GH0vgsuMS4Kn8q6XoQ_QRiUAedNy7TCN9Ab8icKCb2A1oX1FsYRI_C_EPsH7_LE1tZLN2vv3CyB4llr1e0hAlFIaDJYs8kB7dGlm9jDA79BOb97Sef1omKNkheHOKHkKX67n65ahjSn1vA9y7IkLL37wEke8uBtotiSevB0rZ8ONR9BVv2urpE7oz3cdJkDe8vUW5IAIuECOqqy5iEUiKV7hFmqlevKnel4_3IhLrn55cKKBE7hxnY7pBhsqf5-Enws040xKIw5Untpr4xP5XUduLxRIf6cH_-OIgs0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسماعیل‌الفتح آمریکایی داور بازی آرژانتین و انگلیس در نیمه‌نهایی شد. ماریانی از شانس‌های اصلی فینال هم داور VAR این بازی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://telegram.me/Futball180TV/100029" target="_blank">📅 10:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100028">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e78e4370.mp4?token=YEFvs7R_cZs8I17nKUsFihQqwWeMMA40RUF926bkNPnscDctRdxUBQcFBYEo1g2sD6Q8cllcO16BW8T-trBkiVjPh2UxKWq4QjgSE14oPLmnFFh_9D_43GoSfDlr_-UqkYvm7_ZEMtHi3p6j861pYw_xmHrrSjvtYNE_wOfPVH81yUJ1QLr7YefcssBymfVxfWnKY-NhOBnRCr8u4Nw8wOtsXZnzPuInVzUyI0P1Mt3j25aKTaoqaXeVg1Ysbe1XQHG2cRloWPd7P4FGwmeZcPjpT3FsoB7lvs2FYn72rweuIjrN3VNOPnm7qyBUQ2UDHM_p4EWchVMzi2IPPBmBsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e78e4370.mp4?token=YEFvs7R_cZs8I17nKUsFihQqwWeMMA40RUF926bkNPnscDctRdxUBQcFBYEo1g2sD6Q8cllcO16BW8T-trBkiVjPh2UxKWq4QjgSE14oPLmnFFh_9D_43GoSfDlr_-UqkYvm7_ZEMtHi3p6j861pYw_xmHrrSjvtYNE_wOfPVH81yUJ1QLr7YefcssBymfVxfWnKY-NhOBnRCr8u4Nw8wOtsXZnzPuInVzUyI0P1Mt3j25aKTaoqaXeVg1Ysbe1XQHG2cRloWPd7P4FGwmeZcPjpT3FsoB7lvs2FYn72rweuIjrN3VNOPnm7qyBUQ2UDHM_p4EWchVMzi2IPPBmBsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
وقتی عمو رشید میخواد سرمربی باشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://telegram.me/Futball180TV/100028" target="_blank">📅 10:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100027">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5hEUCpyfsLGV70DL9ZCNHOmmF5SEHFk5vo9T44ve8CnJ6o2aJ_sYvF0jkZzI1Maa3eCAqguD1TX_4afoavPCikSF2PWSdMXRf_LOyNHMGB-4xttnvIRXuDh2Ehf1e4hG75Y-HKl7tzSOP_qv_KsuSdtGj2c-W3pIrHyMgfEV34G5FQW6KDxJGoB74T6rVf4oP4g6NcUOjc9dOnvoAfpstN_lQV4inMdA3okgyHjhFPDj5fTC9a6awaD33n4yelKpvQLHsReunJOq0GjqN_GFlrb8RncZmNzsE4OaZwvuXjcwIcxFzRluvDe8MqGj6YgI5X2TXVbADvWyR9wEA2pCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://telegram.me/Futball180TV/100027" target="_blank">📅 10:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100026">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f9569b8.mp4?token=BeZ_WA23hYs38oZ32DXQvi0Lt0f_9QOh6gYuz1h8aJ12SBi0f5g_JYxKdycJz0HBgOnA9jj2h30uT-23iPvnwHxyqvflt_A612JU09bFwrPffHK2zFQE-2HWaG6yK7lhh8LtskpwisguErk79FqPJn2QFVvCm2iB3bUu_7JMsyZY5ofZdBvUY3we_34G5PBfwsXAD9D3W7pq4NPb_pPlH6sLJ0LwKcIUAmIulgaKUeS1PhqXHHACSgd8r8RHUKSeJMf3C2pr7PvLIcdrfkNV5AFFeEUnVYNn61j7QRnBXebwczNrNlKz-TFK4AFNJY8iAbdYb08tNgoGK203J4b2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f9569b8.mp4?token=BeZ_WA23hYs38oZ32DXQvi0Lt0f_9QOh6gYuz1h8aJ12SBi0f5g_JYxKdycJz0HBgOnA9jj2h30uT-23iPvnwHxyqvflt_A612JU09bFwrPffHK2zFQE-2HWaG6yK7lhh8LtskpwisguErk79FqPJn2QFVvCm2iB3bUu_7JMsyZY5ofZdBvUY3we_34G5PBfwsXAD9D3W7pq4NPb_pPlH6sLJ0LwKcIUAmIulgaKUeS1PhqXHHACSgd8r8RHUKSeJMf3C2pr7PvLIcdrfkNV5AFFeEUnVYNn61j7QRnBXebwczNrNlKz-TFK4AFNJY8iAbdYb08tNgoGK203J4b2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طوری که رسانه‌ها از داوری فیفا برای آرژانتین میگن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://telegram.me/Futball180TV/100026" target="_blank">📅 10:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100025">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk6UK4t4ZPIvOpQb8Y9Hqqo93kFzsfCKkjrbbB-X1_fBZV_9xeHXbiDNfAqXWs0vsaKNPbb1fdFxx89sDDuDeymr5cWa5ab9MKwPfSHqgh2tS5_OUM0vM8KDHdanE-VFufEQy8-n20XBZ2A4Ej4Xf7Vso41pFpYRKj9GpISlIg2rXOyKWrsSxWDczKB1m-Nba5Ep0mJDAy7ZYkz9thgeMI5l0DdPlmVTH6TkugtuyNpLT7VjUmAbe9IFMQXBbD0PD6f2ji-u6P8OLIN2baOREP0ZgwkLdAsuDGNTIUP6iJ7mQLMWLzfajOv0b2nz-JW55nALoUnD6FHe1WlITm3Tzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عزیزم ولی این نیمه نهایی جام جهانیه من که نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://telegram.me/Futball180TV/100025" target="_blank">📅 09:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100024">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd1d85494.mp4?token=Q4xPI7a0f_P0SZZOih_mKhb8qaWUiaywV7wGKpvT91hKhi5EFri8YsgjscCWPyz2S2L5-k3YzKPgcTmMcZLHTLHJgyQXc6VVgMtVW6z-xjYzPk8khjrLZe_Mqb5VRlkFoTZEhPuNdQQJEFsezJEjvknJFOy_5bbWVJm02N__n0zGBrWKje5walQoCZ287ChieEiVUdTVK4l8s3cpnqeWh2E-hTDpIH3XbrBDzeBYGMVd6pYolSXcJ5Qfm0xFKoBO12zlkfkWT_kNqQjDT5F5E2SgrllWO_jZFskfEnWFKErCRetf4b-aLmDQTMKHIaUDvMGC5YwlRn_tmbFZveYnq533W8UotLWFYFQCvmJCNQyuwWU0bJNlMoTbCgaLwvhoQnCDa00CYxhp7POBLB0VFhrkNkh3_h7CzvjJCS4D-SKHkrivJzar6TwU1etXi-rJ_kB-_oiPoIXXUtlTQisOV_olG4rOquKkMRdgTStgVBIkMw_e-Jq4wQ9MT_7In8LmnecR9hQ2dc3bxH0o-ydrEE3kj0jcdjH78Y4r9jW3mWlzKU3JSHGIUI1MM5lGiq9FHlYs-SNUFhkEyxba4sVOidhy8RE52oZgEssuetFLmdG-0sBTPDw4Eudd8vM4Wvq6Z_kRq0TsAXo6z-v6fJBtCOXJfDAs3WuJi3849R5cjVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd1d85494.mp4?token=Q4xPI7a0f_P0SZZOih_mKhb8qaWUiaywV7wGKpvT91hKhi5EFri8YsgjscCWPyz2S2L5-k3YzKPgcTmMcZLHTLHJgyQXc6VVgMtVW6z-xjYzPk8khjrLZe_Mqb5VRlkFoTZEhPuNdQQJEFsezJEjvknJFOy_5bbWVJm02N__n0zGBrWKje5walQoCZ287ChieEiVUdTVK4l8s3cpnqeWh2E-hTDpIH3XbrBDzeBYGMVd6pYolSXcJ5Qfm0xFKoBO12zlkfkWT_kNqQjDT5F5E2SgrllWO_jZFskfEnWFKErCRetf4b-aLmDQTMKHIaUDvMGC5YwlRn_tmbFZveYnq533W8UotLWFYFQCvmJCNQyuwWU0bJNlMoTbCgaLwvhoQnCDa00CYxhp7POBLB0VFhrkNkh3_h7CzvjJCS4D-SKHkrivJzar6TwU1etXi-rJ_kB-_oiPoIXXUtlTQisOV_olG4rOquKkMRdgTStgVBIkMw_e-Jq4wQ9MT_7In8LmnecR9hQ2dc3bxH0o-ydrEE3kj0jcdjH78Y4r9jW3mWlzKU3JSHGIUI1MM5lGiq9FHlYs-SNUFhkEyxba4sVOidhy8RE52oZgEssuetFLmdG-0sBTPDw4Eudd8vM4Wvq6Z_kRq0TsAXo6z-v6fJBtCOXJfDAs3WuJi3849R5cjVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده نروژ دیروز در مراسم استقبال از هالند و رفقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://telegram.me/Futball180TV/100024" target="_blank">📅 09:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100023">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f18097782.mp4?token=k4RJ-pBsIdQ7Ay8Qm4o7HAHb3ycxL54VMEBhf55FssPFv2A_anCokHOBA8BT0R2AEm71iNWRMIzmQWFILeBX3rdACxdTMQffOm8rMYyAA1wTDiR9qahNuS83P2G7dzhnSLeCQH_14cXsY_IuYHFMe42NreHvyJa71vjTJCkXyoNjXZC90Y3HfUHZg3U3IsNu1eBQR_7nrPAZ-4vd9KNpHIZeirfSs0hhmcvqVrea4JGjvlQthvk-QtRBuwmv9l1KHyHoRITEPUafmC1tA94C4JzIuOC0TUirsc4r4hRViVTSRAIZV-L7FqPoWHQp22Foumsf-XogLkxeLy5qefvHUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f18097782.mp4?token=k4RJ-pBsIdQ7Ay8Qm4o7HAHb3ycxL54VMEBhf55FssPFv2A_anCokHOBA8BT0R2AEm71iNWRMIzmQWFILeBX3rdACxdTMQffOm8rMYyAA1wTDiR9qahNuS83P2G7dzhnSLeCQH_14cXsY_IuYHFMe42NreHvyJa71vjTJCkXyoNjXZC90Y3HfUHZg3U3IsNu1eBQR_7nrPAZ-4vd9KNpHIZeirfSs0hhmcvqVrea4JGjvlQthvk-QtRBuwmv9l1KHyHoRITEPUafmC1tA94C4JzIuOC0TUirsc4r4hRViVTSRAIZV-L7FqPoWHQp22Foumsf-XogLkxeLy5qefvHUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
عذرخواهی دختر علیرضا بیرانوند به زبان انگلیسی از رونالدو بابت پنالتی‌ای که پدرش مهار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://telegram.me/Futball180TV/100023" target="_blank">📅 09:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100022">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇫🇷
🏆
🇪🇸
تیزر فوق‌العاده از تقابل حساس و دیدنی امشب میان فرانسه
🆚
اسپانیا
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://telegram.me/Futball180TV/100022" target="_blank">📅 09:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100021">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9dRFI-Y5e1efwygxH_701XAOmkfYLD80itrS2UJEs9NpnBidloWwf2RBpct-KdZ-fnOqmUpW7A_J9en-7gY5Q-1eKpoperh4PhxMhku7kdUysanL7xMCw0YmK0ymbD_HL-25tJnQiM_iD-v85oTyi5FNogeN_ksnAq6hx9uOnUbvKChZdQo0c3Wb7r1EmVBIUKa6nYloYXy3--HnJ7PDsg_K2PRfwT4qK-JZa1N-ceiRcsHUdtb1krJ5NEgwCjeXQXzCk1g8Zd2bXlozYYwXVlHgug-SkZG65AxHEpcRTA632Fl-DVy250mBrbQ-JRorkouV4g-0jZ3kIFz39mbvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://telegram.me/Futball180TV/100021" target="_blank">📅 05:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100020">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141052eae9.mp4?token=lS7s43x2RTNQeXphXddV39GM9i3YOZNDl02QLnYyyJZ7N2zBntw5bVQGQqvJBtRqoyRKBii9fDzSu1xiE7weKaXwy8QhvRlWi3HHZfFXkyeAB20nBmtQJEoqD8Wmkmjj0RLAKQwgOYIuzggsqi5Pv51AY5OoDDOPwtw3JoymVm9RL5R1Ukgiyr77EBUFcFQoRzbFR75mSMBWkbPjDdsyIpGiKReWIk8fEDgIRK9OMvSi5ILl_Lr1Vi84_gA_aOO1q5mUzqZiCCrpUrbZS_jmLZBd0RKO4ZJciCv0UTZUml9klPnnbtguaO0OYTNY6j47oABYDSnCEdARHMKJ9OQPUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141052eae9.mp4?token=lS7s43x2RTNQeXphXddV39GM9i3YOZNDl02QLnYyyJZ7N2zBntw5bVQGQqvJBtRqoyRKBii9fDzSu1xiE7weKaXwy8QhvRlWi3HHZfFXkyeAB20nBmtQJEoqD8Wmkmjj0RLAKQwgOYIuzggsqi5Pv51AY5OoDDOPwtw3JoymVm9RL5R1Ukgiyr77EBUFcFQoRzbFR75mSMBWkbPjDdsyIpGiKReWIk8fEDgIRK9OMvSi5ILl_Lr1Vi84_gA_aOO1q5mUzqZiCCrpUrbZS_jmLZBd0RKO4ZJciCv0UTZUml9klPnnbtguaO0OYTNY6j47oABYDSnCEdARHMKJ9OQPUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال گرم‌مردم نروژ از بازیکنان کشورشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://telegram.me/Futball180TV/100020" target="_blank">📅 04:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100019">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ad2f40e7.mp4?token=RQo-UWDEI4WT5kjg9LmtyBsOYu2vA8BwFhVjm3a13vErgNQ0LvYMOWsMVd15MarH8i4DQymrtQmVuNciwY3S7wVrPNZVn1BF-GgcqGTyCOQpB99wrxzzipcg-NDpfVjfFEkmuIR_B8BxPGcEnLJR0kOvhgcyQGafiOGOV2sWJ1ZkBNASDJREoeL7g-h8IuFy32dS9H0U2hxBOx_CfPV6POYlK2V-IjCRbZe1nyQ2fDAgA6MmzYOA78H7NUox_61G4oCbGB6Mt46Rx9bepMu2B680RclGYLsfNFtIv-TbjvjLunpRfHW8MoLzCyYUXj3G7MbZ26FGZTSgiNE7A2HU1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ad2f40e7.mp4?token=RQo-UWDEI4WT5kjg9LmtyBsOYu2vA8BwFhVjm3a13vErgNQ0LvYMOWsMVd15MarH8i4DQymrtQmVuNciwY3S7wVrPNZVn1BF-GgcqGTyCOQpB99wrxzzipcg-NDpfVjfFEkmuIR_B8BxPGcEnLJR0kOvhgcyQGafiOGOV2sWJ1ZkBNASDJREoeL7g-h8IuFy32dS9H0U2hxBOx_CfPV6POYlK2V-IjCRbZe1nyQ2fDAgA6MmzYOA78H7NUox_61G4oCbGB6Mt46Rx9bepMu2B680RclGYLsfNFtIv-TbjvjLunpRfHW8MoLzCyYUXj3G7MbZ26FGZTSgiNE7A2HU1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تولد لامین‌یامال در‌ اردوی تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://telegram.me/Futball180TV/100019" target="_blank">📅 03:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100018">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cd6224c4.mp4?token=Joxsp_OfFKPxugbaQToeFtQQHGWcUp23V_1nwob5fZ8Evzx5WG5axvib--FqeXKtQe_IOUolckNacFi7T6QMnHm4CCZ5np-7AOiXTBBIEalpS7s0NVcmhg4t6SQhAS39AFaKtBAnq7A0OJgJVJzg_rA2iON0om_RfCCU_3gg56aPkjXI5sZaON9tn9xJjFOI6NXInA7ZRi_ghsocx7brFgNLsDx61P3sbDB9A35mzJA_Da5yp26fuDGEaMby1G6Tq0JrEERsKJNW_gJhedqp2KoakAWe8RR94eovyvBfHINnU8KXtOTjLKqAfqIzvYSTmq-KayWf2pQ0Ccube5wPeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cd6224c4.mp4?token=Joxsp_OfFKPxugbaQToeFtQQHGWcUp23V_1nwob5fZ8Evzx5WG5axvib--FqeXKtQe_IOUolckNacFi7T6QMnHm4CCZ5np-7AOiXTBBIEalpS7s0NVcmhg4t6SQhAS39AFaKtBAnq7A0OJgJVJzg_rA2iON0om_RfCCU_3gg56aPkjXI5sZaON9tn9xJjFOI6NXInA7ZRi_ghsocx7brFgNLsDx61P3sbDB9A35mzJA_Da5yp26fuDGEaMby1G6Tq0JrEERsKJNW_gJhedqp2KoakAWe8RR94eovyvBfHINnU8KXtOTjLKqAfqIzvYSTmq-KayWf2pQ0Ccube5wPeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوب براش خوردی علیرضا جان
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/Futball180TV/100018" target="_blank">📅 03:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDGXxSIZOk_AiJKuP5bKXYbbmwxUlBCKKsiMQ3lZEXESLvl78g7ChozvQQArriTtOU__zbojNcTAPtiK0BpSbW2ZLBK2O-yXJ0PTWhhqlcwM1rELfAlHronrsJutT1mDezo1vcJ_d8aruvvQfOsOsrjPWnytfh-kdOvISvpremct2CobXSkYrUaXLJJsRn3QuOiXhn0LW9AS666N8DEN3uQNOkY6HSCo5GPmj6Ie_CG8r_XQC4crXDM3LWJ_dsM3fFe9YoLb15JYFiVWm3TWTUgfO3v7a75_6e-vBhNaMvkSnhmeHdZtAn6O8Q2Uj6H8B5sR0qqQCCBwkNZqfeaGSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
لامین‌یامال: ما قهرمان اروپا هستیم و طبیعتا تیمی که باید بترسد اسپانیا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://telegram.me/Futball180TV/100017" target="_blank">📅 02:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRhspfsgUkBSZi4BGOfADb9g_7uNeBbYbMexdiVkPtZ5UmdwF6TmcfOSQ7xIvI-El6o0nh6fFguXID3R72PU1h22SjrGSe3PzWzQ9M14Ps-qpUa0QN2zahG36c7ka93p686auu46AgzPNBFh4W2L7qL5IFpCmguxy5gsAA0pFXhk9Y1zGJJKb2IDqE0qz9AGZzZnYXplsmKWr-qHBWHhR-e6HH4nEi8UM5aY1s2kVYvE2PTnYXhS6rCjwA4swk3hfL83N7KldaaZ-P5zZ1Si0Ju6XXsI9XQzl5l3ZmfpCI1UrZqb45rYNqOQXSKx4j_-lVD15ZoFI0TJa1mztsRBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇪🇸
دلافوئنته سرمربی اسپانیا: لامین‌ یامال ۱۹ سالشه و بهش اجازه بدید خودشو نشون بده. مطمئنم فردا روز شگفت‌انگیزی ازش خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://telegram.me/Futball180TV/100016" target="_blank">📅 02:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKXMyAzD_3teLF9YLMlD_x04wiI-fF47pU6YE6bGStdcNXTjnXhnfEccWPL2IMAB98wbfgr0tRWKjPanICSanE-u2zsMpnoZpZy3xBQOZISce55Nxo4OpnLKbGwjAiym9z25In_ZhZw5MveGwzvmH6a4EBWgposhbXHDAPF3TUNIvW3JP0ikhQAeWj7Yajout0-tbaXkCU-KxnvoKwg4MP5_ywInJdWWYOWEHxsXnUCAGRLzgMglaV1DPSGzUk6zFKpBdFeuFZLFuWOSXxLgDw4nW44sN6iPqiiG3l-Np-9zYnO-F0yuqFTGPVLLvnsJpTy1G1u9GVgMp7RQ_668vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
داوران منتخب باقیمانده برای بازی فینال:
علیرضا فغانی، ایوان بارتون، اسماعیل الفتح، اسپن اسکاس، جلال جید، اَدهم مخادمه، سیمون مارسینیاک، مائوریتزیو ماریانی، گلن نایبرگ، ژائو پینهِیرو، ویلتون سامپایو، خسوس والنزوئلا، اسلاوکو وینچیچ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://telegram.me/Futball180TV/100015" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9b623292.mp4?token=coqnrAt0cOTSVqFH6wfgP12nQI0kbozt05AbtCsWkdNGfPqWtXKNqMDpc0-Dgw75VYk_wzWwiQdvIh1umSpI8MWCRjPe7rf9_njXOMUAUT6_2N_KxSrdmOdsQqJiNoYPCNILY-EqaR1yc2YW7pZ4MkyUer8ORej7oqGBw0ogkh73N-g1HFUYR2WZ1L6y1i5jt0dDp0HiVBoER1sz-e1q3rcW67IpHq4BCO9LittbD5id1_-yvn1dr0fXEcCtxBG32iZTP44lYYW1VGPiv2jQ04ymBXWmoB137SzvkbZVt_huy9Uqo7HtSKLPE9c173FOE5B1sFKxN_-o0lkxSaF7b4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9b623292.mp4?token=coqnrAt0cOTSVqFH6wfgP12nQI0kbozt05AbtCsWkdNGfPqWtXKNqMDpc0-Dgw75VYk_wzWwiQdvIh1umSpI8MWCRjPe7rf9_njXOMUAUT6_2N_KxSrdmOdsQqJiNoYPCNILY-EqaR1yc2YW7pZ4MkyUer8ORej7oqGBw0ogkh73N-g1HFUYR2WZ1L6y1i5jt0dDp0HiVBoER1sz-e1q3rcW67IpHq4BCO9LittbD5id1_-yvn1dr0fXEcCtxBG32iZTP44lYYW1VGPiv2jQ04ymBXWmoB137SzvkbZVt_huy9Uqo7HtSKLPE9c173FOE5B1sFKxN_-o0lkxSaF7b4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇳🇴
استقبال فوق‌العاده از وایکینگ‌ها شگفتی‌ساز جام‌جهانی در بدو ورود به نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://telegram.me/Futball180TV/100014" target="_blank">📅 01:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SZ0WPmy7__DBOz8N4_rZU6SnG1FtBaC8_Y0njxrG4KqMCjX0Mk894Asl7guXdB144lptrkuNI4i33VgIXdc3_-udD9lKwN4fAKpelt9x9Oz-30U68puvhhP0CG2xfub4PE-Vx0UqSPk4IW_DY4kqyrSC_q2WHoVKMjoDxuRDtqZmsLlq1zc3UwZ-lFh9VgsOuOykhC8AJhzQggzWSAwmlUYgJ8jQ-pmmg9PknUVw743uMBanmnNVzyaPjqUQZFLAnH0G4qpxzOKa6dh3LkcdqMGeInGT9Jj1CLMOVqBVZSuUPLMagJ6d9PzX6ikUPR9nhNkjf4Zwmk-ZcasDv9_W-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خستم کی تموم میشه این دنیا
💔
حق ما این نبود واقعا</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://telegram.me/Futball180TV/100013" target="_blank">📅 01:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
ترامپ: هدف ما از موج جدید حملات ویرانگر به ایران، تضعیف توان عملیاتی آنها د‌ر تنگه هرمز خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/Futball180TV/100012" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
ترامپ: هدف ما از موج جدید حملات ویرانگر به ایران، تضعیف توان عملیاتی آنها د‌ر تنگه هرمز خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://telegram.me/Futball180TV/100011" target="_blank">📅 01:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
دیدیه‌دشان: کیلیان امباپه صدردصد آماده هست و فرداشب بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://telegram.me/Futball180TV/100010" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKXfzLSqJfsSb-rifOIiPKzlze1jm--HkleH38hipjBAHpLL094BXKEgvkIOkfMT8cUqpzPrRBTfDYi8_w9VEvUI8alC6LC83IfgTwj3tStBFyOoQc7yf2may49Al61pLC8LwOB6KXG5GNtsSIpOCtHkEGeS2C9I8o08fZp-FLn3jtSlPi1AjsZ4DysP1klGLgBFL6MKRq0fzr3QoDDAg4s0w-rnTvD08oCbbUdRGlHrl0LTjYstPC4Ir7--E3aZjhbqnsZpyrpHfxefjRqsbaTYHeBiK_vZ7o1_-7G1XqoMgfNpdXFOuI0o6RWw_ZklwY9WOJVJjpKa38otZKnjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
‼️
گزارش جنجالی روزنامه نیویورک تایمز:
موساد در برنامه‌ای چندساله تلاش کرد تا احمدی‌نژاد را بعنوان عامل اطلاعاتی جذب کند. هدف این طرح، انتصاب او در رأس هرم سیاسی کشور پس از سرنگونی جمهوری اسلامی بود. مأموران موساد در سفرهای خارجی با احمدی‌نژاد دیدار کردند و هزینه‌های او را پوشش دادند. دیوید بارنیا رئیس وقت موساد شخصا برای ملاقات با او به بوداپست نیز سفر کرد! در پی حمله اسرائیل به محل اقامت احمدی‌نژاد در ۹ اسفند، یک مأمور موساد او را از صحنه نجات داد و به خانه امن در ایران منتقل کرد. با این حال، این همکاری در نهایت به دلیل نارضایتی احمدی‌نژاد و دلسردی او از برنامه‌های اسرائیل ناکام ماند. وی سرانجام خانه امن را ترک کرد و برای مدتی طولانی ناپدید شد. احمدی‌نژاد پس از غیبت طولانی، هفته گذشته تحت تدابیر شدید امنیتی در مراسم تشییع خامنه‌ای ظاهر شد. به گفته چهار مقام ارشد ایرانی، وی اکنون به دلیل کشف بخش عمده‌ای از ارتباطاتش با اسرائیل توسط نهادهای امنیتی ایران، در بازداشت به سر می‌برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://telegram.me/Futball180TV/100009" target="_blank">📅 01:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100007">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇫🇷
دیدیه‌دشان درباره لامین‌یامال: اون مهمترین بازیکن اسپانیا هست که بلده در دقایق حساس چجوری تفاوت ایجاد کنه. حتما مراقبش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://telegram.me/Futball180TV/100007" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100006">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇫🇷
دیدیه‌دشان درباره لامین‌یامال: اون مهمترین بازیکن اسپانیا هست که بلده در دقایق حساس چجوری تفاوت ایجاد کنه. حتما مراقبش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/Futball180TV/100006" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100005">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nix0T36m9POkcKJaITk9kTp-CQuyewo4RdII0qTO35Qa7shEHTwGrgsHKzCMEVSF6xoHM3FuqSPiJcdCbJMEJSuGlzQCrCWmeK77GJN0aK7UA7NJ1gzsYeOAi77r1XwUDgED8AO6AJnn9pyy_h7Vdp6Asxa-GqDQqjReZnP6j3QjK_aChm9uPVmmMuAPJyUyzWfG6y7d9KZ3Wak7BTqRoUF8npnq2B8paPx03bKdSLDqscXTMsTNSWNxaq5jO77TBplyetXIWnvH2YPWD0A3p6WfefQYvJcUtCOGj22PTvGLbSySMURFvSud0-T_VTjOUifZWZopEwwXc5X5PpyPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇫🇷
امری بازیکن فرانسه قبل از تقابل با اسپانیا: راجب صحبت‌های یامال حرفی نمی‌زنم. فوتبال با فضای مجازی فرق داره و فرداشب بهشون نشون میدیم که کت تن کیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://telegram.me/Futball180TV/100005" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100004">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2oEBjHN8ZIt1QvmMzSeuvfHC_yyO8yLhNZoTcCjcowhoedZlnKGh-p6c3U_ssfrFvffUwyILrWCQSrWGIKx80k3SVmFFq9LI2XBMMgqWeT-07qX0yII7J-hsPFYXMuSqnK31DkNVsFL2QhDJz6YXozDe8B-mEU07qDEoFkyhd62SYIWKyzcCfJQJRegMnUs9MoB0NfsQtf-pmj6X0wi6adY90PfBylkb6KKdxBTsdlR-WLC_L1QIXgzUQtBtQ9yON-SXQ4pWyrX060r65QRF_3XxTKgjhvAs8AbY5EqplyQ4by2Vb_mUuHoJ5ZfE8-H9aaORWKUlGD-Fuo5p5sDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://telegram.me/Futball180TV/100004" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100003">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بخدا خستم کی تموم میشه این دنیا
💔
حق ما این نبود واقعا</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://telegram.me/Futball180TV/100003" target="_blank">📅 01:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
⭕️
شلیک‌موشک‌های سپاه و ارتش به سمت ناوهای آمریکایی در تنگه‌هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/Futball180TV/100002" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100001">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
⭕️
فارس: پرواز جنگنده‌ها بر فراز تهران برای تامین امنیت صورت گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://telegram.me/Futball180TV/100001" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100000">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-_-rxvMHtPbqyfHc_Wp3Q9-3JozIBO8PAn9fW7J11Ob3CHgXqMSk293HN0jOVPJD3bMqp6GBrtzzHohPe2_8kJ3XsBgJDPUnEZNO2260DJLc5d-Oca6koET67ZsrSYfS9PCWZ5wJaEsIQjt8n-mHPH1E2qmivKTypOKAhAHXyOcSFNZvXo6ufqeU95Hwk9xrCJKcFNxZQSPNSXLPHaExuYItvlYVYvHjK64ZR0zGXYxMFqdVlfheAZJjSEQ2d0OWjQZgTyS_S06rFf-ZKFbOmCjWAvrEVXA617l8xCBrZ4tlt0emATNKv2RywgcDOOLG96I9L2GH77XPd0sdlbocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: مایکل‌اولیسه گزینه این فصل رئال‌مادرید نیست و اگه موفق به جذبش نشن، در فصول آینده برای جذبش اقدام میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/Futball180TV/100000" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99999">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHmiKWZD1Q1klwcPH3QizQ7Fz6Wn6FkgSK2HS5CCjMJNbACbhtnhH4DG_4ZOZoOtBF6u6iGnPK_jUigw1iXx97HW2ITcoD6ONVof7_LqAuKyICfEDA79wXLcsHke9r9ZAo1gqcj09ywoVvrY7ShTcXrSG3ddTHf2gqj6IvPxBFwP2_sZiRRjt_5zWtQ-MMqcB2VCmyBye341o1PiGKr8wxFQlp2oKZkQIs461Vx98-vN0kThkGnJ3z_fFY8necb5lIcExKUeETygdx4iciRTT0k2RRMnAmVA9CvoDwlo4TlOn0TxCaeIpu9BU_C8RccfJJ7bQL53Z6h-9g1L6aSLdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دی‌ماریزیو: باشگاه آاس‌رم با ارائه پیشنهادی بدنبال قرض‌گرفتن گارناچو از چلسی هست. چلسی البته خواهان فروش قطعی این بازیکن شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://telegram.me/Futball180TV/99999" target="_blank">📅 00:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99998">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=CR0qBTdsGzBehYwauFYZdQKTFKemN7Bwc50cmcOJMaYIesfkk8U_7PNRyPjC1jdQ5hu018S5blSJBxhHCsK-WlARlqw2mVp0P-NYGQ7eag1HBRTeb13BFyeOJ7QEtE4GyItl-dsgV0x8IYHZG1I6vRIGYnQtPo-9VVh-iT7akfJ5Y4M09Atedd6P9UoFBic1NhZMbYnWzFRcjtjLy80HVi1pJMtAk6bKeGtfADregduUoJ6uNkYyW8mhe7GBNiyuEvwo86Kt2tcsi0o5sakd6AbUnsirLGdMhUhd7ADiHLmDqUaCOnajBFw3WYRk1wMF9NApsiZmJh2bqoOL-_b0BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=CR0qBTdsGzBehYwauFYZdQKTFKemN7Bwc50cmcOJMaYIesfkk8U_7PNRyPjC1jdQ5hu018S5blSJBxhHCsK-WlARlqw2mVp0P-NYGQ7eag1HBRTeb13BFyeOJ7QEtE4GyItl-dsgV0x8IYHZG1I6vRIGYnQtPo-9VVh-iT7akfJ5Y4M09Atedd6P9UoFBic1NhZMbYnWzFRcjtjLy80HVi1pJMtAk6bKeGtfADregduUoJ6uNkYyW8mhe7GBNiyuEvwo86Kt2tcsi0o5sakd6AbUnsirLGdMhUhd7ADiHLmDqUaCOnajBFw3WYRk1wMF9NApsiZmJh2bqoOL-_b0BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو منتشر شده از حمله به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://telegram.me/Futball180TV/99998" target="_blank">📅 00:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99996">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
شنیده شدن صدای انفجارهای متعدد در کیش، بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://telegram.me/Futball180TV/99996" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGvB1Thyeipx4RSTVB_IpXJAzwOV-JwRHgsRIT9FHRtN8I5hCXrCi1Bd6jNfQKhiDk9CBV7mtmWZ0FeitCbFadk_zZy4gt139QyXscNS8_y25P035MGV8EeeafoQueBjc9p5ZEiS4fgn2uU184sewqg2Hy1Dt1SzCqY-hA12-8JkycXEii94uux7Rco3HoP1Sj-BftbOZ9-zEzeSrH9kbymjVn_cSeo24OXJLR75GLvjq4cSwJ7Uh1egB1dVgmds0VU-WrlLjWpesVOuFSzHusjBZSEG35B-oKmJWPcn6BiWhLzM-g2MURv37c4fg19bs9Is-9VxKvAlFT5zi2jVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: میسون گرینوود ستاره مارسی به فنرباغچه ترکیه Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://telegram.me/Futball180TV/99995" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8kagzzLLcAjCRLAs_7TUvexGyYaopx5SyxN_UR5U7UV9yIfKGE6OlziNJa0UJ_TCB-x3NvkCQcn69dk0KjoIuBj0A5N4HqiDr8EiOHQa3YkExh3fw4Eoxp-hLLZ1JrMIYPiQoMJW74UdRu89lSCRcSOVGOzrbpnrk74JerThsX-vjhYiYLG4jRj6HkmqBvGD2qA8BdJ9mOVPz7rZLG93_y7l6n7QX2I_YEmH5FratdhHJ8cJVYZ-icd0R7JEsXlmbkuNk52taMH2-xjg22Qh25_8N6vPvstuKkHx-vTPvnwI0hzcGzAqmJ_TG6JDGByDbIxCnmlO6pw0AXkXJmmAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام مربیان فصل جدید پرمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://telegram.me/Futball180TV/99994" target="_blank">📅 00:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99993">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
ترامپ: ایران نباید به سلاح هسته‌ای دست پیدا کند. ایران می‌تواند تعدادی از موشک‌های خود را، مانند سایر کشورها، حفظ کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://telegram.me/Futball180TV/99993" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99992">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
ترامپ: عملیات نظامی علیه ایران ممکن است بین دو هفته تا سه هفته ادامه داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://telegram.me/Futball180TV/99992" target="_blank">📅 23:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99991">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
ترامپ: امشب و فردا به ایران حمله سختی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://telegram.me/Futball180TV/99991" target="_blank">📅 23:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99990">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
ترامپ: امشب و فردا به ایران حمله سختی خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://telegram.me/Futball180TV/99990" target="_blank">📅 23:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99989">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKEL_b-Vg1Mb8fRfhVy24zfHyspEQs-jaMQKPzJx6eYDGDN9gc8MGaFE4yPXUTWVkkTceDYDRBiiHVJd5apH_WD3D6yeZbu-bgvhTUeNTTpCAsK3upDOPLi_O2YeBYkrso-YbiCB3XZSU25nez_QepSZRAxCUYGeK6_D35kwJSXauoYb0LNchGfqp88OBN3Ybun4277OMSWcWcvoHGBMyE9EpoLIAnM6qaHTtRR0ObxVZ5-H4LJtp8vkAsRnH0SHXKlUkzEToHYHj0qoH9ZwPsLnYtqNrhkf3RLbbWc0dZUieeUVYYJuKE0pJ1-ESRW_jq1Tytvmj5moB69PJ3jC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین روز کاری ایرائولا سرمربی جدید لیورپول.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://telegram.me/Futball180TV/99989" target="_blank">📅 23:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99988">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇪🇸
🇸🇦
#فوووووری
؛ فرناندو پولو: چندین باشگاه سعودی، از جمله الهلال، پیشنهادات رسمی به بارسلونا برای جذب کاسادو ارائه داده‌اند؛ لاپورتا قیمت را بین 30 تا 40 میلیون یورو تعیین کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://telegram.me/Futball180TV/99988" target="_blank">📅 23:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99987">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6JXafytiKU9o7CefAEGX-mP9j6axdCATcYw9Wxy3kKWAcjirgwU6BJZWZFk_e_TPTAgUOnzu9T-5j5HLqOOxdIJagCJdVdwAzFZJeH5IRyFkwEItcfmMKvnLOZKGE3dgZWz-mer1hntVOzAJTSSP9bKQaBrTmqRFg4Yw__-8cXPmau8k3Xq9T62sTn9DmHYXIDqoVJqYOsoTYpINwt7KjKDlHivaWjKBXg4y1CB6_YhetnwZlJa3wHH1UU67Cp4MI0twGecZSbkxsS7O0CdC9NVubCIFr93YCUsAuWoxw-9FqbRhcYccHBUpqXMSUYEGNRcc92wqli4TRp1HYZt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومفریز تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://telegram.me/Futball180TV/99987" target="_blank">📅 23:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99986">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_Z9f0lER1R9uSmmmC0QVazGVuMD7zTlt-FsyAx0hbyfOKNbMVjBtqmCFNS49LXysKk6lsOecKwBx8cmEoLVGGLXAeDIIEAHdA25jAMRPwgqMbJQ98kmh5Wp1I2HDAUAvr4aYA737ZfUugjHPZ1Bt3uzcBsDLouzYUfX3HsefygHHaacF_RwNv2Vo3NGveCpcazVE1SHihhxs62ZdC00ObqHE1rMB4yBeDzBYipkaVGzx1IHrVYDOUDLSLDOwlLr0PaAxfvWf9QMDbB80lRfIYHwhO2nODEcAFMQ3Mu1CTOcNfiyEpv6VWtH5UrebKOVwR-FwWryDcTrx2a1o-PZmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بین دو نیمه فینال جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://telegram.me/Futball180TV/99986" target="_blank">📅 22:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99985">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFMAbTZze5YBGMiorgVQgCjY2PbEtFmSHyrjbVdQrEHpu2VhYSBPDf85xh5uTQYNPIjruxpTsfcKf6C9hJ4xyZJ7rCWrfCU7iZZZWbHmbZHFqM-bGJMLGq4oAfPSyViPpqRzMlLOWG7oJbjoYQoR1smetcitKkRRDHQLugBMaEPw9lvDN1Yrj0FkLyeDuWVibOq7WieqUYSKO5lAnNu_DYiB5CD3AYGCN4HOYYj0DYnFabB6FyKwU5ZWFYljRB5DuMHL7iaTBz-UnW79CDssYLvNc77ils-HLK3Y-AErVYx8ZBeW971jk6yZ3R-tzT9eXvM9mMEwCos9vZOzPUYh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیراز و اصفهان هم خبرش اومد
اونجا هم دارن اعلامیه پخش می‌کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://telegram.me/Futball180TV/99985" target="_blank">📅 22:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99984">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUrt-yjvdAjIlcJ1OsRHIKkgaTIwU8JO4k4zi_MWIITs-7GbXd4Y5fXyFpuh0bAdD8DNY5BAPMc3oBnhezlR31oykARqrS-u1apQCtwvp_jOjFDtkVHMGbVvmAvWcwr-qBCtLGry1Fo0fLLkXwkQPNU2KMSg-9JFkm6NRYxD9-uQDyZUypM9seJlVARY7AyQdwJg9L182u0nuim20M_3ORtrA-DoQaOgkPIxbpvjA12WZei1G43VtBJH-oQ4x4cfpuiM_inHEk5VF8ELMrmQYl6YXdHn7On_pcLr8k1xaWftTsfpuD0yXgFez2vDx718-U0Jo6af7C9Tf1nVq4_Uug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمه نهایی جام جهانی
❌
الکلاسیکوی بارسلونا - رئال مادرید
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/Futball180TV/99984" target="_blank">📅 22:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99983">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6407669b7.mp4?token=EnZjXkqk9zUEjSWAD0LSv5F0ubox39BSpSnp7qw3NSD3vasG1CJK3LtsjAHuXkBXmFB5SCYnwUakkWX3-Ejn37armV9mRfZrwD8OblzQ3wMU526Hor2O2Zw-stsm-tzyQuZDxTNjegl3pOd-W2c7T76Y4q0hviuldZ7M_Ey3RgX_abWXaHkbOgUHCzOAbfDGPdJQUAjUE3C5hm20Rlz5VQP-TWqTejPm5SCZw-_8nP4MQaQFGk3YRIFVHeE14MBaT_1DJumt7HhG1wJi15d6i2JwihsbBS-rxQi_-TIkCNjlpgMaVSoI-AGWcqiYh9Y54WfQ5_iIl3N_zHEctx7TOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6407669b7.mp4?token=EnZjXkqk9zUEjSWAD0LSv5F0ubox39BSpSnp7qw3NSD3vasG1CJK3LtsjAHuXkBXmFB5SCYnwUakkWX3-Ejn37armV9mRfZrwD8OblzQ3wMU526Hor2O2Zw-stsm-tzyQuZDxTNjegl3pOd-W2c7T76Y4q0hviuldZ7M_Ey3RgX_abWXaHkbOgUHCzOAbfDGPdJQUAjUE3C5hm20Rlz5VQP-TWqTejPm5SCZw-_8nP4MQaQFGk3YRIFVHeE14MBaT_1DJumt7HhG1wJi15d6i2JwihsbBS-rxQi_-TIkCNjlpgMaVSoI-AGWcqiYh9Y54WfQ5_iIl3N_zHEctx7TOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
بازیکنای فرانسه اگه تو تیم‌ملی اجدادیشون بازی میکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://telegram.me/Futball180TV/99983" target="_blank">📅 22:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99982">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZTwPoTMNoYDww9ZixmSzEC7HVkb7O6CgRQDqD-YiDlkGB-NktUdZMeKQvG0VHXy6uSpoGFSVp2aIdCRm6MJ754rqIuUNrMLxfPDyNGywJUAP8LsjRvKelAm2RiNo1OMA6Ar20F_q78XhN9kmIH8zBWJjxQP52Z2PE9aPxUXVXEkEJfoks5LfB79XWdaJSau2LIHO8CI0ErQKB7ghraFCofawrnOTAD2QQfZNToOfSaG4FTxl_6Kd2uHlTHUjowSaTtcuExdmkw9ICTvUuPAQWY2H47okC_LzERA8Pxfo3kgwUe7pdGWC_ZmQ194hXcOlEfLZqZiq6U43JVF7PvnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
کیم‌مین‌جائه مدافع کره‌ای بایرن‌مونیخ فصل‌آینده نیز در جمع باواریایی‌ها خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://telegram.me/Futball180TV/99982" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99981">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38664c7a49.mp4?token=tTdBIKHqoiES-QQp2Ap1BduAT2wmN60NkxpsnQwRUyqfDewSlBUuEnWqSa7fAQBx8AfmDfoSYu0c4u7l0yvWUzHMOA9P1G95lbvTGo4vs9px-dhWKfR4qrTvs6v-9pcAR1MRuD_sHmL0Hr4-ZFTeoFPgg9-O8FYXDxkkULeFdeBKIDC4ER4sW9kKXAYiozS7Hi-6MBJ1JtIjw8bTJZ1ag_aFj9hHm-tMVcGpbNbE3LyyVbLXsUjhSf4GSY3oSlvJr9D2L86rgkjH8o5ii3uYJNfwx22rzVExabCi4-gj5QAxAPJnTd2lZgKGoNWRAjhp0lBSZZJax8Y4iTx8vjf0Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38664c7a49.mp4?token=tTdBIKHqoiES-QQp2Ap1BduAT2wmN60NkxpsnQwRUyqfDewSlBUuEnWqSa7fAQBx8AfmDfoSYu0c4u7l0yvWUzHMOA9P1G95lbvTGo4vs9px-dhWKfR4qrTvs6v-9pcAR1MRuD_sHmL0Hr4-ZFTeoFPgg9-O8FYXDxkkULeFdeBKIDC4ER4sW9kKXAYiozS7Hi-6MBJ1JtIjw8bTJZ1ag_aFj9hHm-tMVcGpbNbE3LyyVbLXsUjhSf4GSY3oSlvJr9D2L86rgkjH8o5ii3uYJNfwx22rzVExabCi4-gj5QAxAPJnTd2lZgKGoNWRAjhp0lBSZZJax8Y4iTx8vjf0Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
مقایسه آرژانتین با دوره قبلی از نگاه گابریل کالدرون سرمربی سابق پرسپولیس که اعتقاد دارد در مرحله حذفی، هیچ حریفی آسان نیست
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://telegram.me/Futball180TV/99981" target="_blank">📅 21:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99980">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYnVd7thjRUTKecKTFqsrHYuYheComGKPz4XRr3vq9own-ZqAXLfzQxcyDo_KwbYhLxd412D3LZLR_EpfynkLVFd-hrgCAZVrHsSP9VLYcUjS888VAkNZbaEY4hbCAYIAESZJmnMGNxJf8S_XiI_Wcrn4Xhbkv0cAWRmplyBAkQRA8E81ezRty5u0pmW5evBnEoCDnOnJbgJ8bDbtEowuXJ3xlGxICcWgm8D1J69QulhsQiJO5F5j20nE2-lhADTuNF0u1XPMWwA7cTJ3GEoDU5wvTQu32xg4E-yiVBFm3iUY8NLtzIWxDirZt56u-3stVwqJGRYt9X577FYKUp5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تب پیش‌بینی جام جهانی بالا گرفت
مشارکت ۵.۵ میلیون کاربر در جام «همراه من»
🔹
تب جام جهانی بالا گرفته و لیگ پیش‌بینی جام جهانی «همراه من» به میدان اصلی رقابت‌ها تبدیل شده است. تا پایان مرحله یک‌چهارم نهایی، بیش از ۵.۵ میلیون کاربر وارد این لیگ شدند تا شانس خود را برای حدس زدن نتایج امتحان کنند.
🔹
اعداد مشارکت خیره‌کننده است؛ کاربران تا اینجا نتایج ۹۸ مسابقه را پیش‌بینی کرده‌اند. فقط در ۳۰ روز نخست کمپین، بیش از ۹۰ میلیون پیش‌بینی ثبت شده که نشان‌دهنده فعالیت بی‌وقفه شرکت کننده‌هاست.
🔹
حالا با رسیدن به مراحل نیمه‌نهایی و فینال، این آمار باز هم قرار هست جابه‌جا شود.
پویش «همراه من
» دیگر فقط یک بخش جانبی نیست؛ کانون اصلی هیجان برای هواداران است که پا‌به‌پای بازی‌ها، در فضای دیجیتال به رقابت با یکدیگر می‌پردازند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://telegram.me/Futball180TV/99980" target="_blank">📅 21:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99979">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/183d4ae8ef.mp4?token=aDTW2SUhs9TVnsyGZ8Igxog6SwfVhYq_UeCcoj4JjvUF608hNOHsbJYQpJwiOrrFwmxfkzBDhUnCKtOpXSmq8d1pwxg8l4cc4H93PzV9zNwAE6FHTjyWmQGWR9NKxe9VSerx8iJ9nwknw0Kbe-OD6Bb0J6ItJrvCrBhPv98J7NAl6A_YeR2iMqPkrIXTp-hvWBPjix1kGHHLJg8u0jPLLjwqSNn-7pUT970iLA7j9X8YLj4GEmc-FhmVA799C99tzC2je9yUYYKAfZtdlJBm7nC8FqcSNL2tAIj_TGzila850hQ2TUAetiZ6SkOEdCjLUtrwu9v2hzjfNwiQMShNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/183d4ae8ef.mp4?token=aDTW2SUhs9TVnsyGZ8Igxog6SwfVhYq_UeCcoj4JjvUF608hNOHsbJYQpJwiOrrFwmxfkzBDhUnCKtOpXSmq8d1pwxg8l4cc4H93PzV9zNwAE6FHTjyWmQGWR9NKxe9VSerx8iJ9nwknw0Kbe-OD6Bb0J6ItJrvCrBhPv98J7NAl6A_YeR2iMqPkrIXTp-hvWBPjix1kGHHLJg8u0jPLLjwqSNn-7pUT970iLA7j9X8YLj4GEmc-FhmVA799C99tzC2je9yUYYKAfZtdlJBm7nC8FqcSNL2tAIj_TGzila850hQ2TUAetiZ6SkOEdCjLUtrwu9v2hzjfNwiQMShNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آدیداس برای 19 سالگی یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://telegram.me/Futball180TV/99979" target="_blank">📅 21:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99978">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://telegram.me/Futball180TV/99978" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://telegram.me/Futball180TV/99978" target="_blank">📅 21:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99977">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/moyfOtGqEcc2o4lbxjKpD-H3knHmwlZ5xewfzY64GKmsnnFQ-pJYBfaZ5eBngVTcnTVZ3jhi1v1Xvpgs6r-uDSwbObYNeB7-Okbpj7RpS5qzKXtMQdQGz-_3t0ib1MV-GEzRUEfs3FU0U06QtUP6TYV8BrF1r-evg-DOhVsAQrQx0FiAYL0ruUayrx6VvsrJSRwPJlHVdBru3UVYfXQI0aw_xmx6kG8qiyukrWaKBI3sWZiEk8gI26Qmp1u7ImImbLzw9puLI__NRQ0XwYL_hYG1Vs-Of6xECA7XBDhR8JWsUYMGRWC3Shy5wSZIXfYozmaq5t9SA0Vs72Y5LL0b3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎆
تورنومنت بزرگ
POpOK
Gamin
💥
فرصت ویژه برای علاقه‌مندان به بازی‌های کازینویی
🆒
📈
رقابت کن، امتیاز جمع کن و سهمت را از جوایز میلیادری بگیر
💰
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری همراه با انواع هدایای نقدی روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet1.space</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://telegram.me/Futball180TV/99977" target="_blank">📅 21:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99976">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvyHVr0NcdGw06Y7sRcSjhXGaIQKtBFnBB1idSEDRPglnlQL9fI3pKiwkeOTF9dFj0Dhd7BGG8XeIaLDDqOjvXvSAmug57ef8AoeQE1izmsRHsR3K8Llnk137SGWZMRqkSzwWSvUDRi440ie5YaHc6pBDvGk4idkkt5nn7oHtRsgDVI2ccHTuMY3OA0LZ2aEO78QRhs7FWnhT19to9dKjuwZjO4YkF0l8n3UGvnpF8zXYGKXeVniBjRbv72MiJz4x0reerGl5OUCYOt48mVdnDUSHgkOzwVE2_KIaTPsLDZ59wLVMbFzUaHXYFpjw-Pl_tgZ2Ael620wqAJ0dNyvBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ رسما کنگره رو از آغاز مجدد جنگ علیه ایران مطلع کرد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://telegram.me/Futball180TV/99976" target="_blank">📅 21:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99975">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS0gaHNPtkXOyR5hQra4AptdefWABgMVkkC-Me3cI2T72GP7o-tfAMOSPr3NyA36A26Q-9EUA1uGcoAGk9KfrWFYl9SZO-lDWUlVB5ezKHB_vJkTr0617NXQf_iZYWcK8ZraVDzVVmYEa3vcW-l3fPAn4UkdDzIOp90uAkQBzhxP3yL_PC8M7t4oThNs907TnO63XXKua_Yx-Xc89z-mXko-iImZv3j-zbCluyQru5deD9NAHve5yoCHQDuDI6LevFzL2j6OEC_dk9m7TJDDFVIQQn1is-Y2D8CH0zZYqarza9IPU2HpoY8xW1KvN-J2mxcHJn9h_yyWzbYNsMVQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست مشترک زلاتان و هالند : قدرت در مو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://telegram.me/Futball180TV/99975" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99974">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCpbCSY7jc9t71XMN-6qGtyhRyyMtUpXRN3iC2iHYDu8XHt_B748vyaJwMYogCsFSLflmWxbZJrSgVwfZ_tlRN8BZDdBBw6pJepDEgZgltk9-SqnB9DzvbyBw7cnUhD8a1hrgrxseWrDDK9AsXOhnHxQNWpCBb9Jm3q6p78jGefAd93pC1byv4L35SnDjS9cgBrNgoCpfnxrNQoLRp5xo2o4DV3UKDwUh-0BDJUGKqlYw3rhwd_ZJLjI731-zwvOD3ee4-XcL-4QQxGCAQjMPZWOt6n0gvA0UN9kOCXHmP_w2VUNg4hpb3ogimhYG5M5K1sVAuNFtz-25h1aUPd-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
همه مربیان پریمیرلیگ در فصل آینده در یک قاب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://telegram.me/Futball180TV/99974" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99973">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LajTqh0R4nxfcEiVdfUml3OjPBiA43TvOGDojc0zhjva1iyxCmeEV_Dy9uDf0eX_pGg6HtGy_QtvdBoPjDGSTDABQ-5feG_UbeOs3aOeMuogKwnP4K4nTSiXVcJNE0JcNRXJtOzXWswGFGTi5jJU6Fx78tCYIFztd8RN2HlnUeHZ_PlwnzFulYVRAsxNH3PL18Xgm2Eaw__1bMmyFvCEFE5BQGOj8jSk7boIKTToPntIkooJ-XIcr4BVKYfcE-XKN-CyMcaF09YhsvI5I5AzwW0RTbe7GTOnPoTmKRnJOesyL_2oG3ODrQSNlB9JkP40mTGYZ1bNTHUNX_SOK8aM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
کوکوریا:
وقتی لیگ شروع می‌شود، جنگ با بازیکنان بارسلونا آغاز می‌شود. بعد از آن، بارها در دوره‌های فیفادی با هم دیدار خواهیم کرد و در آن زمان، آتش‌بس خواهیم کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://telegram.me/Futball180TV/99973" target="_blank">📅 21:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99972">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB1HRTVjt3X8ycXe6EyhT0owYHxJ4ozI2QUqmyP0HtEbQSmMWx2Gzj4XpAsSYcpTowPEvUM1By8NdVJFB-XFNy6-S_jvzD4F6i3Gqcb96W2pYGqvh6uT0IkmPiGsso726i8lILytKe8VLdcqiQIyCjFFUzhjjBxKY8NPXvTdFq9Q-4KY9_sNflkjLLzKI-IT0cn8wvFbdVU1Z5KN9Vf5Wn8wXAYacIFAqSLJzwsSX4zCqKv1iMpyuxtQ9-gJwl9TwlxSPb6_Bg5Oc9bJIwrAWw8xLOpdepOVXykO3UGErC-knnQR9Jdea3kwzqyiXFv_fGL3P2Cozv9KsfoHS8wDuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17K · <a href="https://telegram.me/Futball180TV/99972" target="_blank">📅 21:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99971">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jk-x3fSYIkTIpRty41WJBGrbi4AotedNcUu4SW7VbpOsM9VL8J-gSf4wG-dIJilcqTo1KCg68gYbRqEiTIRLEm2SraE4KLVjoI4D8YjBlVOPy8rs4rzIQ1AIB9CSJjHgtOoEoaqJlaI5XA8TpwvL6035yvDE_32h8Q6oj83PeXNioavlntOhOeo2WmIsye2bVNzxi3EiLPH3R7Fy-44Q7BJCBnJ2WlsnJJci2UCg1GyHLD5cxs6VGeiF9de0HkIIP0mfb4VKlDutYnLnuxTzJ0V4FsfClaso61ft5ZvprU5y8JIaUXGiWrOWSBMh12Ga2ehgevalUCOLCJcxzAwJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
طبق اعلام رسانه‌های ایتالیایی، پپ گواردیولا اصلی ترین گزینه سرمربی‌گری تیم ملی ایتالیاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://telegram.me/Futball180TV/99971" target="_blank">📅 21:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99970">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NccSPk-ve9sTtVt4hMFY3HRhNAWWD2yoH5tOGm5_XD1ZnsIbB6EC9CPDKehhDgSYWKC_xjX1RVuCM-UhCT-pDVanGvwnbcszE-DWRZmxHKnLWAhjpAeqwquKurdfafy9501jkNPOU0_E0xC2I-7nivjpjM8AkNfOjEQhExOC8dlMBmUARcwXYGfo9A4jjq1mlTbhfW8ZgZfekQHA_SpsxrzfcRh20ptzJxDolAR2SNVt_Mpqc93zDS2faEfSvzqYYCOyMl9uIa-SvAZ8aoCBjiYQncyldss7wWoCR42IJxVFQVrJ1mhXcqlxt2QvIH59G4Hx61wcxYrbjqa_gAt2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری - مارکا:
تیبو کورتوا دچار آسیب‌دیدگی نشده است. این بازیکن امروز معاینات پزشکی را انجام داد و همه چیز به خوبی پیش رفت.
🇪🇸
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://telegram.me/Futball180TV/99970" target="_blank">📅 21:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99969">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cbd524bc.mp4?token=SP15YvkFSaht71cAaghyk2ekaNN5msNKf1Ood3682C_P5zbG_NzMCoZUBgqgJ3B3PIrURIX9kqXKwi6-ox0EfcnaiIWxLgAmVDhy-LsPC2v5dSr-R7hlORi6L56uyBhzae2soO6ISF-qvawLLwwNIbIgttFbUlY3zvVXiZ2XCfCR9QeLFUh863Q06EMLqkNjEp8L4QpNFWqKxgICYT5TzQBY2rIuFJvKTFAlF_YPr0981CLIwE10D3f71OFoFBzCftVMK_Ox_8SCRGVrX0FgK93QEGE_iik_lsN_r3qOlOlLnP5lt27xtTTF3Q5napDXjEOVXExn_LX0sY2Y6C-rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cbd524bc.mp4?token=SP15YvkFSaht71cAaghyk2ekaNN5msNKf1Ood3682C_P5zbG_NzMCoZUBgqgJ3B3PIrURIX9kqXKwi6-ox0EfcnaiIWxLgAmVDhy-LsPC2v5dSr-R7hlORi6L56uyBhzae2soO6ISF-qvawLLwwNIbIgttFbUlY3zvVXiZ2XCfCR9QeLFUh863Q06EMLqkNjEp8L4QpNFWqKxgICYT5TzQBY2rIuFJvKTFAlF_YPr0981CLIwE10D3f71OFoFBzCftVMK_Ox_8SCRGVrX0FgK93QEGE_iik_lsN_r3qOlOlLnP5lt27xtTTF3Q5napDXjEOVXExn_LX0sY2Y6C-rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرق ارزونترین تا گرونترین صندلی های جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://telegram.me/Futball180TV/99969" target="_blank">📅 20:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99968">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e7fbe2f2.mp4?token=YKWv7JA62QcI712jP4_fZL6hrlM-G2TTjDc_I-HRGPaMJk3mbcGmkMV1RuPfdEcF_3cd4H1xpyW6N7OlnpWkd1suDm16MYoepitWAt0WPeIBAlA1FnduuiXIVtMubOFiepCiGCMaR7-x52emP9euS3sQcZ76AhZtIsvySRFxm_aHhMvbi1zFyXX9tNwWH11Ws_edw01C3a8ie4lHxt60HqyZ91fao3adWwJKxRo-6GHCz0ZYdqpVQfWk_DXrYQNhZEpFW3NGZaTylelfvfd3Ecl0FabWodT2uM-0Qah9Y3UbbJrdBu5Duff7UkwlMaKgvFnNnpzl_gv6sRS7QptJMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e7fbe2f2.mp4?token=YKWv7JA62QcI712jP4_fZL6hrlM-G2TTjDc_I-HRGPaMJk3mbcGmkMV1RuPfdEcF_3cd4H1xpyW6N7OlnpWkd1suDm16MYoepitWAt0WPeIBAlA1FnduuiXIVtMubOFiepCiGCMaR7-x52emP9euS3sQcZ76AhZtIsvySRFxm_aHhMvbi1zFyXX9tNwWH11Ws_edw01C3a8ie4lHxt60HqyZ91fao3adWwJKxRo-6GHCz0ZYdqpVQfWk_DXrYQNhZEpFW3NGZaTylelfvfd3Ecl0FabWodT2uM-0Qah9Y3UbbJrdBu5Duff7UkwlMaKgvFnNnpzl_gv6sRS7QptJMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا جان تبریک میگم که بالاخره استعدادت رو کشف کردی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://telegram.me/Futball180TV/99968" target="_blank">📅 20:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99967">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR-iUbI28Qo1NJr3hnNieb0Gvqv2lyPwI9-g79z4Ts-sHWxjMLOEb0eB6X6F4GSlQbl0wD-jqDUA5V2RJeHi1-HW864amCws7HBWBlSzddd3LYLX695g3r-Ci4SdXmpD3Y9jVmYqDyVCfc7_UOyDIvB7UAj05edGWlqMzl09P8c4MfNVAiwzBxNsv2ApEj9MhbPCoujfLTHf7tgM8KDtq_IJNLmHSkl2MIGbrwIww7CcePsGreucXDWIaUYt-z-nUP-qxHB3VWvHdZQNF-_GUyEbQfD3e4iTO-rLcd1iFJcAM7D1atUZIOT_G782d6AAD7Pz30ii57iDrKugeW75pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://telegram.me/Futball180TV/99967" target="_blank">📅 20:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99966">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIK0i3dsd7XVpPUH6txJl5jPIY4vgwdXRl2gnbAqplqPBhe4Ijm_NFEMDQHz2xAv9sLisRagxtm80Y2n6Tbdp7jkgpDaZzj8WL-Nn6-rWPS-050Bn5r2BxrZwDqjxhR1jUOjGFMLPmfjYHzTVZHTJQi-B8erIc6da3TYekcmOonCC-13oCsTxEJ60cbXL2nG56D0pQ7ZvuMcJDIgklLfGPQ4QISnHHPTgohcjnvcXeVOSYCKkOeAcR16qGhTLqMT8fAFZYNIJ8YSwjTVFBRpElIgZ9nOtXvJvcK4LlCuEIaEnDUwGF1TreggiKwB60OJUO5UQrzqZVtmf_QZeqAO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
🇳🇱
روب دبی‌رینک داور ۳۸ ساله هلندی به قتل رسید. این داور گزینه حضور در جام‌جهانی بوده که در نهایت توسط فیفا از فهرست نهایی خط خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://telegram.me/Futball180TV/99966" target="_blank">📅 20:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99965">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4c44829d.mp4?token=QShnqpw83VhDf3iiOiZXrROAjbLC1gCOCMJmneq1YTixYg5P9rfn6VXstlXL6NIqLA_QcP2Kbb7Btue4Q5qEz9GzfgjVCa0wu_iODdZ6Ih6lZojpuoKr5S_3IHwfeLwx2TbGN_72_KoA6RTQJdqK3gkHUM_d3muEzVBuwhTVsFRYlbpg8CwXZnGUua23odJhqE5bR0WRdYo-JczFHYaMXJZsB-gxL7uS5WvllcobbFjnrrg8UdP9-I-FebMPOcZnCPLt5T0IHJ7GAUuVC1r1_w2q9lJ9aDurasCLyW07U-MV6p_oISbsVtpCw4PJCjGhuM1ddq25GRw0pH0zNkGyMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4c44829d.mp4?token=QShnqpw83VhDf3iiOiZXrROAjbLC1gCOCMJmneq1YTixYg5P9rfn6VXstlXL6NIqLA_QcP2Kbb7Btue4Q5qEz9GzfgjVCa0wu_iODdZ6Ih6lZojpuoKr5S_3IHwfeLwx2TbGN_72_KoA6RTQJdqK3gkHUM_d3muEzVBuwhTVsFRYlbpg8CwXZnGUua23odJhqE5bR0WRdYo-JczFHYaMXJZsB-gxL7uS5WvllcobbFjnrrg8UdP9-I-FebMPOcZnCPLt5T0IHJ7GAUuVC1r1_w2q9lJ9aDurasCLyW07U-MV6p_oISbsVtpCw4PJCjGhuM1ddq25GRw0pH0zNkGyMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🎙
بیرانوند: اینقدر تو آمریکا وقت کم داشتیم و باید سریع میرفتیم که شورتمون رو یادمون میرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://telegram.me/Futball180TV/99965" target="_blank">📅 20:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99964">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
هفته بعدی تاجرنیا مصاحبه میکنه که زن یاسر آسانی مخالف برگشتش به ایران بوده و ما تمام تلاش خودمون رو کردیم
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://telegram.me/Futball180TV/99964" target="_blank">📅 19:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99963">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e8095565.mp4?token=CpD0E3abrCyZDrgZ5Oevn_RArjfadvUZ3J9PlU5CcmMbj7HUMNr6_EEXN0t0Hl9Hx28ni7Dx0Iz4ZkUtnI2CkQeW738LHp19Qm57A_nUc5uNr5MvkHrO1l6pvsKHfS1TKB7aRbOhng48E1cn13p7cH8KOotFyQH4Q5_vVaESxPM4N0xbmn4lLqYlxcWJ2j-x_58OOrxg1dKUVL3wpwqNT4PrECIDq6astLy6jMhzudOF8ZAj92Og3Kabtwc-JZgNhRpwcDY-xQqErqfDTFPTxM6m7X8w7qQfzguAB8cg-RMDLZ99ZOJh-0aL_gPzGaZRBFc43qUQZrqTkVdmBmAZwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e8095565.mp4?token=CpD0E3abrCyZDrgZ5Oevn_RArjfadvUZ3J9PlU5CcmMbj7HUMNr6_EEXN0t0Hl9Hx28ni7Dx0Iz4ZkUtnI2CkQeW738LHp19Qm57A_nUc5uNr5MvkHrO1l6pvsKHfS1TKB7aRbOhng48E1cn13p7cH8KOotFyQH4Q5_vVaESxPM4N0xbmn4lLqYlxcWJ2j-x_58OOrxg1dKUVL3wpwqNT4PrECIDq6astLy6jMhzudOF8ZAj92Og3Kabtwc-JZgNhRpwcDY-xQqErqfDTFPTxM6m7X8w7qQfzguAB8cg-RMDLZ99ZOJh-0aL_gPzGaZRBFc43qUQZrqTkVdmBmAZwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
پیش‌بینی سه‌هفته پیش نوسترآداموس زمان یعنی مجید جلالی از تیم‌های برتر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://telegram.me/Futball180TV/99963" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99962">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=u6CnjM4DeTGyOVfXUDn82kI09OyF5xY0z29tabf9dH3lJPxz4S49QxSmJeaNXQdr--UHWYdx9kf56yrBBAttx1CmD9FHLykCvP0unzLIuW_mKgOxmdP34sfD-azsKROEIr63cZalOeC0t5V2_BBIydzcWDzqItKPuNKD7fg6RFjX8QY_A5uL6A3sXTkjOYSx8oZqBxey8hqceeqpXWRc0WbK3GjQkquRpc6IG6Ku65xaySd5cUwkGVDBIYGFuSH4d2RXiqRDCv-oRD7bYSlcszsVRMzCgfgmv6W3-hPYmFCzTCeqDvKA1pY_tizzAmqljmZDVOm757cgvwn9EhA7xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4532025b1.mp4?token=u6CnjM4DeTGyOVfXUDn82kI09OyF5xY0z29tabf9dH3lJPxz4S49QxSmJeaNXQdr--UHWYdx9kf56yrBBAttx1CmD9FHLykCvP0unzLIuW_mKgOxmdP34sfD-azsKROEIr63cZalOeC0t5V2_BBIydzcWDzqItKPuNKD7fg6RFjX8QY_A5uL6A3sXTkjOYSx8oZqBxey8hqceeqpXWRc0WbK3GjQkquRpc6IG6Ku65xaySd5cUwkGVDBIYGFuSH4d2RXiqRDCv-oRD7bYSlcszsVRMzCgfgmv6W3-hPYmFCzTCeqDvKA1pY_tizzAmqljmZDVOm757cgvwn9EhA7xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل خودت رو بزن!!!
🔹
با افتتاح حساب غیرحضوري در باران بانک کشاورزی، از برندگان
۹۳میلیون‌تومن
اعتبار خرید باش!
🔹
۹۳
سال قدمت
۹۳
برنده در هر روز.
🔹
برای شرکت در ‌قرعه‌کشی
اینجا
رو کلیک کن.
شرکت در ‌قرعه‌کشی
🎁
اسامی برندگان تا این لحظه
https://www.bki.ir/fifa2026lottery
⚽️
فقط تا پایان بازی‌های جام جهانی فرصت دارید
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://telegram.me/Futball180TV/99962" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99961">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🔵
#فوووووری بیانیه مشکوک باشگاه استقلال: یاسر‌آسانی که توافقات مثبتی برای تمدید قرارداد داشت، بدلیل دیدار با خانواده‌خود در میانه مذاکرات ایران را ترک کرد و بزودی برای تکمیل مذاکرات به تهران برمی‌گردد
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://telegram.me/Futball180TV/99961" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99960">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
‼️
یاسر‌آسانی امروز در تست‌های پزشکی باشگاه استقلال در ایفمارک حاضر بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://telegram.me/Futball180TV/99960" target="_blank">📅 19:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99959">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrxfamCFLiR_GPid0R-gW0DLfuqv1dPZVF1HjXCadG1Q37ngfgXudedYElMCFwv7SETigPxLbRETBQ3-QZP8aNFa7eG8Knt8kP_SCFhxtOUxN24U8Y1suO4Bxkj2oXEWmdRCgL11xV8ZgWkZ2bzusZChv2JFtwQj38oCEOdRJGYb5s96Ry5TD7-z2clRr0Nj7wdkOiQ_W_UqDYGxBZsdRB1sL82w-2MWg3n2KnsLRAXGwNfH1uSL8zHl04Hp2kbPQpVJIqgWynfXZP-E8wyz6FG6Jsc942iT9BrqxCtYBNTuvtDhmDp7ig4lh4rh7WGSySKUKswOe80_ZOstEaLJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری ادعای رسانه‌های داخلی: تاجرنیا موفق به جلب رضایت یاسر آسانی نشد و این بازیکن ساعاتی‌پیش ایران رو ترک کرده!
❌
باید تا تایید یا تکذیب خبر منتظر واکنش باشگاه استقلال باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://telegram.me/Futball180TV/99959" target="_blank">📅 19:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99958">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🔵
#فوری
ادعای رسانه‌های داخلی: تاجرنیا موفق به جلب رضایت یاسر آسانی نشد و این بازیکن ساعاتی‌پیش ایران رو ترک کرده!
❌
باید تا تایید یا تکذیب خبر منتظر واکنش باشگاه استقلال باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://telegram.me/Futball180TV/99958" target="_blank">📅 19:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99957">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8b173980.mp4?token=g--5shWigfbNkcwapS0VxPwMBd_tDc8mTrb5Vr5wHc3lyychewI3UFFukyGboDUIIrO5Z2rQYGeiCaWLZk1ho4E7-RHlljr9RNjYKpM6pX2CSw7yNTCHpVgAA0eoJa3KKhEJD-XQD6jOs6WozzM52ukt-c6_nhGErR4GemyegyE77vgw3Q4cN9EsEdujCBdktiuOSLZ-fuv73K_JJ9VmflMxwg1qW8Ztnsyu6fjnozjhwVnzof9cxehWweG9eiJ0a6peC3w2EO76Gzc9pWE3TO_rBikxxmjK8XT68Sp4tXsjo-8GSSAaFmWpeIkJEkxpfVGYp4nPaj91Nw7nsQZdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8b173980.mp4?token=g--5shWigfbNkcwapS0VxPwMBd_tDc8mTrb5Vr5wHc3lyychewI3UFFukyGboDUIIrO5Z2rQYGeiCaWLZk1ho4E7-RHlljr9RNjYKpM6pX2CSw7yNTCHpVgAA0eoJa3KKhEJD-XQD6jOs6WozzM52ukt-c6_nhGErR4GemyegyE77vgw3Q4cN9EsEdujCBdktiuOSLZ-fuv73K_JJ9VmflMxwg1qW8Ztnsyu6fjnozjhwVnzof9cxehWweG9eiJ0a6peC3w2EO76Gzc9pWE3TO_rBikxxmjK8XT68Sp4tXsjo-8GSSAaFmWpeIkJEkxpfVGYp4nPaj91Nw7nsQZdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی گل منشوری عمو رشید
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://telegram.me/Futball180TV/99957" target="_blank">📅 19:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99956">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2vAByejWAwstaJIjE_rSUgw_fIEFreTaLfcUmzeTSQIHCujsKu34HIo5QxoYETOChAAIr67xhrClZGrAs55Yaa8pPOVKsxv2ZeVN3dRdbuzDwmCkZIDBZXnjyAEcgeOVkC1kxDvakYziGmfJ9d3zVTIUDDUB1oxOlSYpZAKzkf9PjvuYAQzxzlo6NVASiFBSbbzO8-Zw_-MxV3zYT6_mJMspM66JYQDYzEGypN_p8RkNbDmH4kdd-GJZHlzsb1woZnh3YAGjbKaYVyZ32oR4Q6mrx-mk2fiFraGVsruGZUazsBSTaASEeVfjHRzVBxNlxZahLbLZk1_xX0TWagGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
لیونل مسی و کیلیان امباپه تنها بازیکنانی هستند که تا کنون در جام جهانی 2026، 30 شوت یا بیشتر داشته‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://telegram.me/Futball180TV/99956" target="_blank">📅 19:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99955">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC9OcVZOhOAeFhIi_HcjhVhYGjWby9JPAqG4YVq2Y-fd72-EYQ2r4hmw3u1g5WZ2QW0IPWI6Wefautm_NWTeZWVRywnbbz_o_AQqqMYzWFaY0MkPiNe64xfBGyFT4cGwvLT2GRUIAqM8VnMN77U4IniCua009bUzzLimJqaG_aWu_T5u5NndhAwC4WAG9bMCNQv7FPKi5ylsSw9c5Q5qumXtL72IyIv2eELNXuO6ztDR91zEekWQUSKhNXYVQJiTIRs60iiDOXa1JB63s-B2A8MjP4kgEhY11HqpsPZR0k73B3WjGYIw_S_u1ceMu0aLnQ4x7g2znX04J4hwzvsb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چلسی طبق معمول اسپرم خرید؛ هریسون پی‌تونی، هافبک 18 ساله انگلیسی، از باشگاه ویگان به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://telegram.me/Futball180TV/99955" target="_blank">📅 19:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99954">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asQBb9gjUm1J9RDduVsrpje9i6suSdIuPvMzaHd1c2I4xmRM3OKPLHlSOKnOXZKuVHNGTWPk0UoqphXXhigeF1x-MrVVIoUzZiOYRaUs1zq8R0-72nWVYpBJ8ODMLKWtZ31kA-Hi-_GXuGKpRtPiIF6Sm6GhZYxPuDjE8DejnP7M3a4ovW37BI1LRP0e2SjGzKeM5t08D5XhsnbTNaABnrLYQJuRuBXAAMFwJfPas0HiwVkQZrGkqn-fQDndjDcnAsPJQ_Rmzvro6mwMC781YcP5G-YX8LmaGbNGTv032gzdMhZ4_YT-Xrtt-6tw2hjpv6KlUqrEMwQV7ziinTCEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇪🇸
ترکیب تیم‌ملی بارسلونا در نیمه‌نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://telegram.me/Futball180TV/99954" target="_blank">📅 19:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99953">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a785f38a0c.mp4?token=vBEl-NK7mGktbDY_WbHlmwe_JNPz2nfHp8xX4-5x6MDWnAd0tEJuKShtPxr89b0-Lvn9xUAbZE3mxrj26DFSenxHFaDdqfRhQFRjtZgUdfDOzXNP5nRobB3xVnLeTvwem0G1nu34ZTUVH76-nVTAixzq7Z9cpE199AGjPRh97kGBGM69DdB2JeBplCD6Upqsjfy96VUkJOEFLOtpsh80gaKOZjdkPO8xaXiEQ3COPJEvqzA6aipwGWsl9S-KaZ2adxIMpZbmoV22sG-eh4BuGrou40NB_kEpYbanIonRNeUSq9uUxtuSrV53r-xKBbi8cMNhzNKTI3bOK1irYVTrXCyLLYqNXh6SP55S69P6cNHMnO-mJgMM52tJTUNnkJii6EUXbvbTG7_lPYfBwO6UEeS0XtOc0J6FKtYgTC4WZ7CB0PfJIwgWSQ9cXZgJ233dQ0F6ujDXms92EOI0TJL8oT_dLGhjQKtJj4q3Yfwxn24iVdD5fbcYYF0zQZgd086Z-iFH8Yr6hUaU9GxUtqbUc3945yZNnhG84CDqSqAshbtmJGKzqeDbbGx57iVQgLlCiDOxJuQFNiEmk7G1RLWqjuQJxC2pIspe0DTQ1RpACLQyi-LXRS7wVaDw2IwD40SgfDRE2m8FYAeZDYNLZP50K3iM-6WO0JMYWFqk50eG8Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a785f38a0c.mp4?token=vBEl-NK7mGktbDY_WbHlmwe_JNPz2nfHp8xX4-5x6MDWnAd0tEJuKShtPxr89b0-Lvn9xUAbZE3mxrj26DFSenxHFaDdqfRhQFRjtZgUdfDOzXNP5nRobB3xVnLeTvwem0G1nu34ZTUVH76-nVTAixzq7Z9cpE199AGjPRh97kGBGM69DdB2JeBplCD6Upqsjfy96VUkJOEFLOtpsh80gaKOZjdkPO8xaXiEQ3COPJEvqzA6aipwGWsl9S-KaZ2adxIMpZbmoV22sG-eh4BuGrou40NB_kEpYbanIonRNeUSq9uUxtuSrV53r-xKBbi8cMNhzNKTI3bOK1irYVTrXCyLLYqNXh6SP55S69P6cNHMnO-mJgMM52tJTUNnkJii6EUXbvbTG7_lPYfBwO6UEeS0XtOc0J6FKtYgTC4WZ7CB0PfJIwgWSQ9cXZgJ233dQ0F6ujDXms92EOI0TJL8oT_dLGhjQKtJj4q3Yfwxn24iVdD5fbcYYF0zQZgd086Z-iFH8Yr6hUaU9GxUtqbUc3945yZNnhG84CDqSqAshbtmJGKzqeDbbGx57iVQgLlCiDOxJuQFNiEmk7G1RLWqjuQJxC2pIspe0DTQ1RpACLQyi-LXRS7wVaDw2IwD40SgfDRE2m8FYAeZDYNLZP50K3iM-6WO0JMYWFqk50eG8Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
ابراز نگرانی عادل فردوسی‌پور: با توجه به جو سازی انگلیسی‌‌ها فکر می‌کنم علیرضا فغانی داور فینال نباشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://telegram.me/Futball180TV/99953" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
