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
<img src="https://cdn4.telesco.pe/file/rq5-3qkLmssnMxnIjmiWenjn87Rl2adi__Iu0zSPD_xXUcvtZcOSYoYHcn-Y5SUOOQeA021UW_J1Be2ORqNxf-Fr2UMY5DqHv0XPTQWSXijLan_8uZTFbHL-l05ecNsu2vYMZbs7beatcotFxAI9W0juTsMLYYtlwvr3gdhmDaNyWS65dkMWbXh5evNUtv4uXFyrayGj2cBUmOPQ_5EJ0C76mmoDEhotwh2rQrNh8VdrFRzFeYE_xeonqkN63H7tXORWN1G9a4ZtxXVGiKRKUtZArdnzkJ9rA2h9wsRJ1w9T9rAAV4gyDPZ-0wq_mBPdozy8Ne5gkkbFS3YpZD59VQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 182K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxkl3X3yalzM0C2gLxcgbyEypJ8h3_Ui1ePOp9uzGqYid_FXzSIujjsVFrO-xgyCQwNbxFXQ9wjgF2ttbdpg63uX-P45SzjEk2AswX84OtjbMGvnXzKWdQo8rSgHrNHGzwfQxJq7b5BHuG30iFdcmBvH7T688Fmo4dqxc-YIqORdQrFXTPSH8b-dBJENyAmmXhkOrkthIpftdbVzWrfakknA9UljojZOoyal-lsA7VmjgsMZ6XXh74cYQhKWSIbgCoGg3MpduYUcCBnYeL-l0vHw6tZFv4RfA6FUcK5vSOI7-kvBQqJeFM9W11xtKSEkmGj1EXKXg3N-AnWOuUU3jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین تهی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/funhiphop/79418" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ju9LTBp6GfNwKYnFaAG-RbzM6PdjmP4eHoVhP0Apnvht0EogLEpGf08A1knDziS8e4Q61QnANVn17W79hggapGjghikn1PLojumHlScjvP4VK4eEpVNH0rj5tAElWhDXd5hi_B13K3sK_0GYwSKN_WGZAj07qyNw3bSfyPDoLzGZBw6-oRPZjIxI5WryTx7T3vNghfZqgGTrXY2kdXvAIhzsJitNO3kUBa2Dn3_PTOsBxO0uegQst2Spxqs0bS4PObTnSe0H6R2qky-jRJsyIFiHjqwOxWKVQZqEqQq42XM9HaHc3KDLQ63q67lJKd11xMytH_pLDaAz_AJ3aDTneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3SirhC2y6zMsfiO0puUS-otyQ_joJ1SZkIK7TcICMlAnNTMCnv_w1D-UeV6PrnAz52X2WhnrGh-7SotmwvhFoBxwuXZSlDhNQKC7Iiw0j3tWg9eJcrNeZgvsA4KxDqNSSfQ4EAB9RR8bvTWB8B-6KLT-lWJEuVWps0l8U-HBBltbhT3SOSHUPD0aEFv04zsb7SrPnDyHTr3nimWlWdoX5CMu0_CLzOBNzZMvcAnlY9LZsJUcqIOK_ODpKWdsMs9g5n7wEpcTfxmtG8iC8KLx3dFg8LV4XLElyUnCgApoKikpwlgEUSH7CseWC2ZLfUFW4kKY8fpsL_0u-utfYC4eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت جدید ووزینا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/funhiphop/79416" target="_blank">📅 17:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79415">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndul5fUhOPcnVou85n4LNGb6cWFmMxuQk3_E8qNjxvJLzBtnTTAKSEx9QYxp8Y-mGHgfs8qHdp6L9p8zgeeEh9sf3SXGTsPcQproZcdoQjNllkcTjvvprtxLU0sgT1AgFmWeD4CUhBPL3bAuMal1r02v4ttoCl3yupkxQQWRDbdYqCFMAZbud0XGFlOv2KZQnUA4gfe5SBOvUVi0EeSl-vDX7553b90jEyAn3o8is6gvJNtB7ma_i2aoOsJnV8c2bsskibPCsiGWD4NLuLrUUcl3fVdsxZxd9Ejqzurq356mJymDKTbGRP5xKfk2llz_LFNVme2-pg7KmfEVcG1g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل یا پوچ، حالا به‌صورت زنده در بت‌فوروارد
💥
⏩
یکی از محبوب‌ترین بازی‌های سنتی، اکنون در کازینوی زنده بت‌فوروارد در دسترس شماست. اگر به هیجان این بازی علاقه‌مند هستید، حالا می‌توانید آن را به‌صورت آنلاین و در بت‌فوروارد تجربه کنید.
• با حضور اوستاهای فارسی‌زبان
• محیط کاملا آنلاین و تعاملی
• تجربه‌ای شفاف و هیجان‌انگیز
📲
برای ورود به بازی، از بخش «کازینوی زنده» در بت‌فوروارد، گل یا پوچ را انتخاب کنید.
🎯
همین حالا وارد بت‌فوروارد شوید و هیجان واقعی گل یا پوچ را در یک رقابت آنلاین تجربه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/funhiphop/79415" target="_blank">📅 17:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwDw9fG2iR_zUWIWnBAAgrXm8PLk8XphEviFxEC8_Aqnrv9beoTsAqyPvxj9jHGd7aYSz0a6znt46YwQtD5Vhy_KYM4nub7qv4gp3kkzns2G7UduNBnMozga1fVLbv_LeDOZfMuOIv-_lFmV3TsHShMfDuGjEG-lvZxrV_HAzBgOjUxYwJNgIQyhjwUJcajE0k21Be2chFTGQxBM9OCuUH6ntPlsGVfPS2x5RQ6D-ON2_bTBiUD-fUkEc3oDY47-5nton1ocNBe1oKq_Sx12JVacQWD5AkzvSPClopd4P7kBaeFUV9m_pwSR8n-0Tq9Fp7K8pEJsA8vk4uuKsZbzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینو طارمی گفت مسخرش کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/funhiphop/79414" target="_blank">📅 15:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nymdG7VBgByAzw8n-VfE487x8NbjtojgIYWfW1BKZzeM1Zr3yW9DXRhjR-O1dumSCNGuVf0PjmWJwoESdIKuvEeJfW5qPg6A9UG6Kw6n4Nu8FejWvKeaWW6gouHCPaPb7MuihOOwgr9SGVSzqAg-wyNidbb1Oi-QhvCBe9pHMteJzNKSpg5LogH8mDyIGWQS11V4YInrmd2XkTGN4NIsxxiI6ONagHTm91M2sO8rHv2QmsjqeRWba550MzsGAwxTZ9qb8IqBpymRxPfS4usGNfLGA4prEps5Qp-qS9RfemrWXQ2aeAmj0jC1gcZqCIF0HC-aOF03WATTOYnK_aAOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصکش تو بارسا از اسپاس ۴۰ سال هم جا میموند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/funhiphop/79413" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=OwlhsWMBDCcapt3wyCUFYh0-bJR3oOYb8LV5dgUOfSoQYDzM1s42veJ0Qnnew4WfhVW55aqwrSy-Jzk0gMQMxTbWFIpsx_g15gLI1D3Xl8dqH8LJ1EBkWRolSSjXnHKCi25AxQ1i3M5s08gPKtNTERVSO184e9USBm5Akde79CmOoD8csJ5Kui82Z3km09eoo7WjhR7v9w609W5PqnntUPOoLo7__78F87lnkOgTey2orAXew6bNL2G3LY3p2Y1oYazyIiySfY2ERaUKo9q2zHgk7NZ-C5QI_fmu4Mcf71tOyxz8vC53mFlNW0HrqZwAt3s1btJJ7HyXm_LR9_0pqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=OwlhsWMBDCcapt3wyCUFYh0-bJR3oOYb8LV5dgUOfSoQYDzM1s42veJ0Qnnew4WfhVW55aqwrSy-Jzk0gMQMxTbWFIpsx_g15gLI1D3Xl8dqH8LJ1EBkWRolSSjXnHKCi25AxQ1i3M5s08gPKtNTERVSO184e9USBm5Akde79CmOoD8csJ5Kui82Z3km09eoo7WjhR7v9w609W5PqnntUPOoLo7__78F87lnkOgTey2orAXew6bNL2G3LY3p2Y1oYazyIiySfY2ERaUKo9q2zHgk7NZ-C5QI_fmu4Mcf71tOyxz8vC53mFlNW0HrqZwAt3s1btJJ7HyXm_LR9_0pqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای خاک به سرم این چه کار زشتیه
مراسم ایرانیای کانادا برا رهبر شهیدمون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/79412" target="_blank">📅 14:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اومدم بگم بسه دیگه گاییدین از نسل یک مووآن کنید، نسل جدید گوش بدید، چشمم خورد به این پشیمون شدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/79411" target="_blank">📅 14:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پیشرو و اوج یه داداش دیگه داشتن اسمش امید قدر بود، اون زودتر فهمید تهش چه آبروریزیه از رپ کشید بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/79410" target="_blank">📅 14:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">علی اوج چقد پیر شده پسر</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/79409" target="_blank">📅 14:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تداوم و وفاداری رو از پیشرو یاد بگیرید، ۲۵ سال گذشته از وقتی شروع کرده به موزیک خوندن، هیچوقت از کس دیگه ای جز امینم اسکی نرفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/79408" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1R1GsB_L3bobedn7AFIXXS_F9igaFokKktZywjR7UsTxATWea-0cqW0Jy3Zo7vvON8TAWyhIkHDVv9xTZdC0CTQLmEg2R4AJkT-6inJ5QaB0i_3nUId9_O0GjK2wil-MH9-__StYc10EhT5sxga_3mbEpFrDZl_QhyIeuI4Ncp1sIcVXx72aHhfip6Ox97LUE7_zmfwq3E_EhAItD5PPGpzoEgCDFlOwpSSvg5uo6xkrVQpNQ99QUb1i3GPdrqXNc89-qNh9mHXgwtcGi4Is9LF9K9T-3aqxhaty1XcA5cyfOWOWmEwf8vEy09hG1TZDJk5ivmDLrjdvXDZEWzPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHr20J6mvTpURhyNDXiJNndpfK-dxk30YPBhj7AwcOHQoVeev07H_eqn0plUsXgIxNlSD9SwNmXj79UZTMA-Ztce0U-h1aPdDURhiOiZPT1fP9dQi-_LD235ghJVbQ74kZajdrSuZhYF1FGyE7zoxPKkNhi_S9v7nXw5RcMS_60oRb4BoY3C5-eGDv8nKjS2C3lNLagBk4AU5TEzNdirnTyXlYFBoYHiqTTgMD8MiT9HzTsFBGhTrh21lSnSgef04sEZAHXryPxgpXD64k8K6-CZ5olnkxK3ffhMDEnmtQdaz58RRmpdRIj5LPn3_ZHbuf-bYoS4RnC_6n2_bgDZ3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/79406" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یه لحظه حس کردم با ماشین زمان برگشتم سال ۸۵
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/79402" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/79401" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoKAmW2rw75TEvIes-8LbBcm4QAss52x75rJ2ZmUwBqckP6DNEGawhyUZ_E_6sCwM3GiOdccSTKPwFEifAHi0XJ6SYRdDrtBHK6LG9KBcG5AUbqSr4FfpnB-EpqWSix7eAD1IJ53dK6_DLlru-CapmPUJmyvfoMnW-SKigvykJIfTz-jbPEvl7AVGQVArAGWXS5i3LWMAGnyJ0scoKdLSUU6l4-bhSXzWoG2CluHF1G6wvVvf_mVL4yF8BjMSrMs0kdOgK2ku3KNN7Q4mSYsT247b-mJtuRbvGlAdFy_JdicMUerBP20FcQsgwqtjiau4pHMZVVF5_dB9QquHqc-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/79400" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHAPOYA4j58gYLXMx3HKmus92rlgg99mE_H1y2MbPjQyQJNfaHZxHtiWph7fxdBQgcRYo5oWGSXLUQxCCBpzQ24IzL28c5rC1vE7IYuGNlryaF66QLytfKlQm15vHaIra__x8zWJFYs-JrhRxc1iEhESSMe8FeU96fyN2qW9ICO-1fbtuTWzrp5DpnpYnw5T4bggZPcOyP2jwipK1FLhz4FxKLx2svl2PNzKtD4cq8XucHaOaLQ1nJv3x5DnJ63c2O92U2Lr3rE4N4A-kZqedHT57Cs9-RXBXKXXjnlHPjxOKQRouoUUimVc9-PejlBpyi7JHM4gy2aqHMtjBDJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربرد این اون وسط چیه؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/79399" target="_blank">📅 13:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79398">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4kKy8yVbS4I1mlrp4YqZqhcQI5HH-BQqBFWVgZWLXFmTKAHgaE50KeC8ix3H3S2Pjjq0erkfKjXfhFZvlc4HLld5wYAcJ0IT_ICxNjTxLAgN8AU9CyV-LAYlASk65rr_qcfH9drXdvFFfN9mCBUXDZGDwuAsKOX6FE7HqBlsh17VPiV3Koj_i0hqTRu8sGrTLMwUfMJr85k-TeJ17g0cHeYoO1NStUpaNsZLrsJZggx6iv-MIP4lVS_c8ZTyLg0QZVK-U8INloe3X4TWBEiUxzGeplxGdeNSx3zdIQLScMkeia778DFKryByfbygAOYN34EDMwbF-AeTRerFXhiVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان تصمیم گرفت یه مربی خوب دیگرم بگا بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/79398" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79397">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تارتار سرمربی پرسپولیس شد</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/79397" target="_blank">📅 13:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79396">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3DzMzer84a07V3k1fuJrpJUqCd-zTXh09d2K32ef0hh0YrpJdZwgdy_LU6BDYgky0y_OYlUAUiRbI32e66hrAx3r8I1Z2kfXiLMw0o5MJwRjm69wa4TagsE58O4e9Qow1UR2oK1PMZVZT1NagRf3u-xVY_i_e597hptW4B1QcovAhvx_NYNyFmpsgiVpDsq2yLYTn36a_GbUSLnYLUbDGI8t_AiAfoMbHeB3N8LpR5-2GMt_IkO0L0zZgRozr1eq8F3VgEb9V8MeHKlfXFdkmSyimtjJc5W9hV1WENqJpb8xEjS7mBEdtJ5_7SVT7LbyZ-z7BD80cUUGo6OdE7guQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MEGA BANGER
😊
😄
😜
💋
🙏
🔥
💥
🌈
☀️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/79396" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79395">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTeA887RNk1dcwWxrRJd_C4ptIqFw0TDsuHfgxTG9v5J--GTcl29F4VgwPusrzDpvki0odMvR-2WRv7LwXoqqN30nJ4xoF_Fh9fkeYXrF6VVyr12aOi50_GWV4mib6hv8jZBQXOzP1h1_gsCkYQky7mVDCIJi4XXZSxtyJ1mO6oK1RR9rdshe02RhygDW1POrma4Qp44bRcrrB8Hr1LBIetT6bcLGAlJ417y1veIQ4r6sogEcC5wX0C2LJwazQm3LdCCv4hnfYGQaM9Lv021bTp0tlHXyr7YmPLaqYFGNcD3D4sNADWpgZjVumPlAAv5GMu8HdJEddGZzEPWLwLJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79395" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79394">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انگار بکام میخواد دروازه‌بان کیپ وردو بیاره اینترمیامی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79394" target="_blank">📅 11:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79393">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exhQF23WqsfxJQ5762Nu-GY1FwivNfi9ASkKcQnQDQE2rPjcQYuwzKnqa9Zo9-jvOdFktWThOcy4hlOFWARmskmkh-qXqcCGlHVgt7jDX9zDC-WHaxmbzGd_Ynv8UnBzi1ZwUy5giEBT_3HkF8FbJZhpdKFBeFuubba_oO_yqoFPCw37kgn81yp9_L0e4gLi6QZ6cTRy7efdbVVKV1pts6_-51fy1nP7_j2JLYF-d3touTM010LePugdeWgRlSZmd_BH25UtBo3hQEaOamEYggIbjnk78Tu4qnu93M4mhKixrWdDO_KOM_EkorBGRwO3jJimSxOJYm9NjlxnbxOrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه کصخل اگه ایوب بوعدی رو نگه میداشت حاضر بودم سر زندگیم ببندم که سه دوره پیاپی قهرمان جهان میشدن، تنها نقطه ضعفشون همین هافبک بود که ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79393" target="_blank">📅 11:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2rIbQRo6y-jBVacIYm21YzW2y6msn8iO3jGu0XlcZqhcw8fzsm6NeCOie6MnZUJ_qWbTAk-Y4XsabBRhlk8m4PYcKd5fQaDYwmsXNeZS-yehUQQFgMjTLmveJa7xA4eU2Tjn-iB0sLreeqNwIs_m46llNaEz7OVTuG0U9LHd3-37X4TMrRWfsjoYxSHPu2MakEansLZeq1JpAX0roqUXeD-k18jhZykjdREae0KMW9DUTR13VfUF2teQ3AnCElOp40NHTTYFFCN3wivMqp-7RSJmDmVG9tEaGZHdqMAO7XFcMYMEg24S-7pnjT0Cv4ntg32aDRMF2I7qQ64Pnp3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی هادی چوپان با علی خامنه‌ای.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79392" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79391">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKqfY9wkviPTLZ9tBG6_pMo5_5WBvc3f6pMjvDvOLGeuzpVxZaV-_lOeBj3Z7GDeR90m6eUkhICkB7E81K0Ib0f1J0CP47QIXoBg6GFG35NIwdYtisA1fsbccoa4n-cOcQQh0k3UMvYryL63n0GduldtefhzLplWlE1fYSXRXYvjSGrlBEHAxDKOTQFv5Zyr5ZcDWhJhtp8qs-jIOfYaFzqB17QO3NYxKhW2DQEEd52uQg3X6NzTFCEqm4CmH8IiEchQEC2SF-0uKhvoN_BsDIbILPV0ir7kUBE_w6zzrwfBK3vh_2Oep81-HWUPqMlM12RzcOtV7HiBv-gGwqKPWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل یا پوچ، حالا به‌صورت زنده در بت‌فوروارد
💥
⏩
یکی از محبوب‌ترین بازی‌های سنتی، اکنون در کازینوی زنده بت‌فوروارد در دسترس شماست. اگر به هیجان این بازی علاقه‌مند هستید، حالا می‌توانید آن را به‌صورت آنلاین و در بت‌فوروارد تجربه کنید.
• با حضور اوستاهای فارسی‌زبان
• محیط کاملا آنلاین و تعاملی
• تجربه‌ای شفاف و هیجان‌انگیز
📲
برای ورود به بازی، از بخش «کازینوی زنده» در بت‌فوروارد، گل یا پوچ را انتخاب کنید.
🎯
همین حالا وارد بت‌فوروارد شوید و هیجان واقعی گل یا پوچ را در یک رقابت آنلاین تجربه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79391" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8i_W3crV-mJiF3FuGuk-oOUe9sQgh4nBomJfIHx8NntfF_BtKLLr2q1A0OCmG8O2SEeyHWZ74GD92CHgJjPREq_vqjiyMm7PPiZ5BoZC3ERddpNn6m8RU1gcD7ScFCqbo_Iz0TsvB8Zi1IBRxIqb7Jr3JrjEw_CcfEM4sx5sT_NoLpywiZMLUiyC_nahsJt-XdoCn9Vpex5cHe70w8o5Mm1pJzIRYN4wVJYlnEQgIGEDK_aUCBelo3dtz3Za6bbjoiVYh9WuHAbK0mCVlBHtijvBIq0f6R848pOWCEVhXCW2FweM9Sg8iWrXQm57Ou71XQiLY6d5bpLqSn6JlZgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستا هم داره بامزه میشه ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79390" target="_blank">📅 10:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چی میگههههههه این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79389" target="_blank">📅 10:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79388">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">به جون خودم داور رو صفر کارت پاراگوئه بت زده بود</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79388" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79384">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-cNc7iekKJEy3aWU87eRs_EMjvRuO83ohh1T4U6knooCpzDaIgLkyZmpAOA8Ixq3jyM19x5Yfq89oodJy5in4i0-q2FmYS8iaFT1oYsVd-yqXXS_94VglpINqJDLNsHC3qnfnVj2ow8sfMQ00ywD68gM3rdP7l6JihgG3Qr5yUxjN08m5vsDU2CXAHJjSgW9hHSOA3hJYBsS7_0UQQWuQClThRnvHGoxJYBoHK6fEUCHZe5QDYJxoQyRpQHZd5JQKNOOs1nu1YLzdSXUQ0CVqy26dQrcJNwKewFkuebX2EE8FcF1L6J4LDbAUQhe5nBwL_oU3qPeGRJq1O83GoDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید دوستان یاد مانی هیست افتادم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79384" target="_blank">📅 00:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_XKumpKWKymQg95-XEv67_UR76MY0NuZO9-bxFzhunwSKkHpT5AgfQ9iboYUOwecxXqbU8diOu85LtRHSh_3ltNLN8xKgaOsV7jJm6R0dFaRk9YgZG1aE14Fses9sc9vJZwEj4xuzyNTYNYjaB27MDbcxQTFBypKd6VLxkXk_W4uPlzlbndaQF6XBv5_RNtrz1-cWzKpwmzL8zd6sVRsUDlWH28XW7SJsTKGxajERCY5FiYGwHikHE_i-FGtBP6TyS7IxazbfHodgqC-Mcz31m6A2Q2pegCYS9AHfiUaoe4ZQ1xzY1GXC2a_puX7It5xGBDtUAVy0mZcK1AcebQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی قبل از یه آهنگی که قراره نهایت دو ماه تو ماشین ملت پلی شه و بعدش به خاطرات بپیونده:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79383" target="_blank">📅 23:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEJtgp9eH47rNPlXkSMGddZqqliyuewiS-ydePnVGFKRkXno64sp95CLlq5gOKTuKpHRM4Vy2N3yz29BC2VEiEKIYYkVqR1E1KNZBEsAQGNexjt_gxAYSmOoQzEYulnfRCZxTP8EsQVeCe4nvhigNmuOoRpRK5locNFLYOepDLOdg1fj72d6OFg9_fRR1jAp8YgDMpEhB0-n1lm_jX6P4Q3vampQU35rp0wkTxY2IbG_WermrAbDxt_MbIAkghCyKxx5g90XhNmoBhdQCiMVNSx5O_6hgzxc7Gm06nxjNkWRyUGA2qJfo1rMhIPtgvx42V-5o9MSOFtcear4riUjaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جور و بیداد کند عمر جوانان کوتاه
ای بزرگان وطن بهر خدا داد کنید
گر شد از جور شما خانهٔ موری ویران
خانهٔ خویش محال‌است که آباد کنید</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79382" target="_blank">📅 23:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=jubipaHaqvuzmcnrS5OmUw1-pNnEsUh8rXztgm_li8lKqxPiDBYWW17sX3nsSS3eCvITT1ufcVG-RSxyLMacqKqfQ5zL3HoRC36WvFOdIDoO4Sr1N3p12BKfDq0giaf4qzg18eBCabhl8x8Z-vbYObKJ60J3zKKV24Xf_eivhGbQtNSjJCygP4CGYdLjv4ZPwU7FEFA7RCBYCnc5YmhB1Fkyilg03qSOG1OvQKKU1onph96QN2ihrrcGku2JwvErTqi-qr_9bEMtZMhJQRCoeeJqf8H2VWgPndcxA1c_rk09zIoDk1zSl3K9x9h8tZO96OwqdAJCYDkqES-vBFUsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=jubipaHaqvuzmcnrS5OmUw1-pNnEsUh8rXztgm_li8lKqxPiDBYWW17sX3nsSS3eCvITT1ufcVG-RSxyLMacqKqfQ5zL3HoRC36WvFOdIDoO4Sr1N3p12BKfDq0giaf4qzg18eBCabhl8x8Z-vbYObKJ60J3zKKV24Xf_eivhGbQtNSjJCygP4CGYdLjv4ZPwU7FEFA7RCBYCnc5YmhB1Fkyilg03qSOG1OvQKKU1onph96QN2ihrrcGku2JwvErTqi-qr_9bEMtZMhJQRCoeeJqf8H2VWgPndcxA1c_rk09zIoDk1zSl3K9x9h8tZO96OwqdAJCYDkqES-vBFUsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79381" target="_blank">📅 22:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانادا پاره شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79380" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مراکش با امید گل ۰.۰۹ جلوعه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79379" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه گل فوق العاده زد مراکش
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79378" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvIdJfLV0xYrAQkIZFmmLgtSfE4xLwGEe2uO4NHqp8pnNyiXjPDFBDOr-UY0zxB7Gt1dvkXdpHwoZVVLnsWHOqrk6wDcG-gkSzV9olpJzFvCYEGjN_QPQ-4FoZxy08QzljNIs2YhOdHKcZhkIX6Bg9Dcv_V9GNiE0FD16L6j3p9LXGlc137ZURTesZQbLse2DC8gy6A6zN61cy6KkJUnpNaTL8KsEy0fK4oBwVfKNAyRK45Sfnv84GqOFdca-JTwR2ZYaSil-lk6dKQ6c0xL9OSE_NWo1T55hD8nZWaU0-CUDoZV5Ml5Cd8cY7yYlZCzr8di81r22V_rpEQCzts0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امثال توماج عادت دارند دستی که برای کمک به سمتشون دراز شده رو گاز بگیرند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79377" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_a1lHRSxq_OYCjZ_6HSTLgR_MUKf0HgqT3OFJEarssQFZe0GMQD4D8iFuyRABhYxmGLwGxM850XpqiEeNuWUYEcs103bUuzpF-J1WKPvD_YZoQiw0_RJXpjAsgwdRlqTn94LzfYdei8SOTtOjiZL8RFhLs0BT46MkMf-7FZ7HU0O9v89jCGxKWChfCQmfMj5WwuxYN612oj2lOZEyvWWOmeTDQJyUQe6o5sQECDzA6p5-EskZeGXFrdZVNtkORb6f-dKUovTq848tFDUbNF1WBYTg4UDJ_uk-uutSC49XLLOWU6RSC_pS_nG34JGuBT0haJEm9-qiL64MZyMldWzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79376" target="_blank">📅 20:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79374">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E9EQADhqV6pmpM00uYqsmm4TwKQ33R-dGszNQH90iSPCauwgwEAw6xe2-LSPdcU9rlnuSDTjEcRAGClKi419QZEjOZ4naUOWm2AxPYh5VEVp0TupiUIzdoCy6v5ZU1dg8vaHm07Ta-tYFfhCSvr6MPlMXEmIk1Yq-orHAVkKIYWHU9LUBV6xzER1gN8tarEzGnnyzsbMQCa_Gty54BysYoUst11_0bUSHfw2eRewpm72Lu6p_Sa7UcufFnHuZliX4gNHd_25Ftv13rUw62zy1OwDwQQJ7fkwe59AKcJXUGCTMiH5s3LpckKyvijGQrAzyhSD9kAqtmWbQ-Dm-aunRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
⭕️
سرور "تانل شده" با بالاترین کیفیت!
تخفیفای ویژمون رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 2,500 تومان!
😈
( مهلت خرید تا پایان امشب! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/79374" target="_blank">📅 20:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkCQF5kaH2CIZpWUJ1DkEVuZq8iI-QzbcuNhbQ_H796OHkqAaMAehLRwN397l_OLVD4RC_YSpWGYqpy8GVGl8awIOpkibWGCKfgEBIv_-QQH8ZY6XyiVae2D5OnTmlkPVcKXKutUBVYVZW7s5krW22_tA7h_Vjvan9o5lCxjnf3dwW3Ex0B-JrpQMnjIpCVRKj0FrH9Y_lSeFzhMB7VQcoPatQL8Gv0QerBRJBx9libCKgcAKpBAtjOS2jVWxEP7yMcnWyPOoX_2aGsYvUL7o-fLIwvMWwWhiz5lVOvlhJ_2Csx-Nj9pXZjBONK_qFTcqxzCKeDXUosTn5hmiivFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متین بامرام.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79373" target="_blank">📅 19:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWK5yFnEtcEdkXWesDDA3FHiKefsL75ATXz8PlyH3mMwtElmN1CDTx3ZnZ4Yd9SdoRGP1OX2hsaZfvGs8MA62ZQG5MfmhLb6z4GuFu78T0bRcK84ZnBg-39aMI89ZRliKr9pZQonmT74MMNz5eITXZsOBZYCexi_STV5I3imFxIqn_R6S5RclMsPiPRdo8zdVkH_XvfMYXWOwprMwXLHCXnJQuFOnSw67J7vzpbK-tV_f-kyJKyszcjOYMYB2uMLRRJSA106CpqMqLlrh-sttG8ZzN4ENjpom3wcWMGeTVNRjzLwL-pzVcT29Pdh6UWUUlgQ6O6ga4DMn7BnUSSLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید رضا پهلوی:
به نمایندگان خارجی حاضر در تهران که برای سوگواری بر سر دیکتاتور درگذشته ایران، علی خامنه‌ای، گرد هم آمده‌اید: ایران در حال سوگواری برای او نیست.
ایران برای بیش از ۴۰ هزار پسر و دختر که در تاریخ‌های ۸ و ۹ ژانویه توسط خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به قتل رسیدند، در سوگ است.
این رژیم، مقادیر هنگفتی از ثروت مردم ایران را صرف برگزاری این نمایش تبلیغاتی می‌کند، در حالی که هیچ یک از رهبران دموکرات در آن حضور نداشتند.
آنچه امروز می‌بینید، ملتی نیست که برای حاکم خود در غم و اندوه است. این ملتی است که پر از خشم عادلانه‌ای است، و این خشم و شجاعت قهرمانانه، بقایای این رژیم جنایتکار را سرنگون خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79372" target="_blank">📅 18:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpn_x0jtQqobCJ-fn09kr3WX2uq5vxp6kRK7jd-5Aieou8lnR5D73baZdh2X0bvFnwoIpiRx9H_hecMt7Ns-YHn6YPsQl2N-gVUMLZ9UgSpTVlTBTVIUkUM1lcfSS8yDP-gpEsD8dIJiwjQQMISDWgmI1KNBlIGbuvO_U4faofBVT6E5nlcUhq0hJP5icVFzR3lmnuR-A3xM0KEfKSj-6cXnSXQNAU3CN0Oq2v6ic4Tq5PiglO8hWM3Ecdb_43IKO8RmSMHMLXID67Wa4l8hZYaIj-ayW_wJ3T6_JN_foIjRVVs0ibOZmUZEti_UfOsP_hzmtyDPQMZJ3b8TGXKCzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی اونقدرا که جَو می‌دن باهوش و فهمیده نیست واقعا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79369" target="_blank">📅 18:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الان تو مراسم یهو یه پرده بزرگ و ضخیم اومد جلوی تابوت حضرت آقا، ما شروع به اعتراض کردیم که این چه وضعشه چرا تابوت رو از ما پنهان می‌کنید؟
💔
💔
💔
که مجری برامون توضیح داد به دلیل تابش آفتاب و وضعیت خیلی خاص پیکر حضرت آقا، مجبوریم فقط چند دقیقه تابوت رو به نمایش بذاریم و دوباره شب ساعت ۸ پرده‌ها کنار می‌رن تا دوباره بتونید جلوه‌ی نورانی این تابوت‌ها رو ببینید.
ما هم نگرانیمون برطرف شد و آروم شدیم:)))
🫠
🫠
🫠
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79368" target="_blank">📅 17:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">العربیه الحدث:
دور جدید مذاکرات ایران و آمریکا ۲۰ تیر (یک روز بعد از تدفین رهبر شهیدمان
💔
) بین ویتکاف و کوشنر و باقرشاه و پروفسور عراقچی برگزار خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79367" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم  می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79366" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=mS_bMHj_ZFQ0FQngNct6BuUj6Fa1su1v7WcyVjvG_9bWs_5UBsGJXDK8N6Q9clbJZ3Ho_nr6l9wUsHZYT8YDyce4vqCoBQAwmLjoQ2wrtTbbfx1_JGPJW6Vt2KNoiRub-Ta-7VHIeN2WNU1tARkyTrw5lSvR9WhjrejC3c1gbKoMq-LGrFpZOtBiOrMpnIlM859Xi2UrZv5OWKUOR0Hckb9y8TmYTdgNYwNFL2rrVkPU8aSIoGk-A_LsNkLcXpufS2H8U1kK101S82MYPMzj1qGd-Hu8y2UzvaC7LwlDNR85MRfRETiOz6CtqvflABdMGU8YASUNYbUkJ1RcdX0ZkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=mS_bMHj_ZFQ0FQngNct6BuUj6Fa1su1v7WcyVjvG_9bWs_5UBsGJXDK8N6Q9clbJZ3Ho_nr6l9wUsHZYT8YDyce4vqCoBQAwmLjoQ2wrtTbbfx1_JGPJW6Vt2KNoiRub-Ta-7VHIeN2WNU1tARkyTrw5lSvR9WhjrejC3c1gbKoMq-LGrFpZOtBiOrMpnIlM859Xi2UrZv5OWKUOR0Hckb9y8TmYTdgNYwNFL2rrVkPU8aSIoGk-A_LsNkLcXpufS2H8U1kK101S82MYPMzj1qGd-Hu8y2UzvaC7LwlDNR85MRfRETiOz6CtqvflABdMGU8YASUNYbUkJ1RcdX0ZkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم
می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79365" target="_blank">📅 16:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79364" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XywxtSH7TgIvU0hrRWWLu9aMzhJjH-pGprND2_z62O0i-zexd07Pg67GSCifomoyUd--EcZAQ-d2B0kGn0L9oMKnKQXyjxctkEfW4u-OFzr5oyA7lVWNBC1p32prjHVwzhPHzgpBJsVKtRDbLS6VILbx973PaG7Udp10D9KHslHd1y4jDntIh544EXbtyAEs_F9XEkGbSGGySquPOX9n-9GHiDr4sOye7-ErRHq2DFTeJbMGUbA9htdTqtnRYJujDZ4BNJJ5UMDNGPHt3z014EuBpmrvw7dMW28JhMdzu9r-KtbKZi_FWO-bC7rwxIsJ7CsCP7Je61RpUPfi513Z_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو جنگ ۴۰ روزه سپاه در ازای هر یدونه موشکی که به اسرائیل می‌زد رندوم ۱۲ تا موشک و پهپاد می‌زد تو کردستان عراق.
بعد الان رئیس اقلیم کردستان برا تشییع اومده ایران و چنین شاهکاری رو خلق کرده.
من هر چی بخوام بگم فحش می‌خورم برا همین صرفا به این بسنده می‌کنم که ببینید ترامپ عجب نابغه‌ی درجه یکیه که به اینا کاملا اعتماد کرد اون همه تجهیزات رو راحت داد دستشون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79363" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79362">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-unJZ0lC290pxAapvtE5lRnxOzttuUrNuSwutSUhJqpK6kncwCnxkiZcrsdtcVG5Txb8wMeMYQ7Q6kIw05umR5JayQA1bFELOwxAEacx-qtr9DtiqKtinebSAJO_z4cVerzRPRhQ9_ZOSqV_Svz07yNOaKAgktygP1a3sZ8-LltYMdJAM1kuzntpQPrNNopVnjpSYCbJlDHR_rR6GRIGM284iL_3H4ATID3lxX5MEPfflfLW_BCJ4p5mV99ADv5EV5V30L0acFXnQ94ynSpZztUnkYNDfccDReylWWze20_CHNN6ZYzbcxtUnafbJaw79g7ZM1hCmQHt8RUsArpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تسلیت به پدیده به کون ها
دریک رو صعود مراکش بت زده، کپشن زده که میخواد از نحس بودنش به نفع کانادا استفاده کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79362" target="_blank">📅 15:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۱۴۱۱ هم دکی پول ویناکو پس میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79361" target="_blank">📅 14:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_7pTBlXyCj0XeimcG2q5BUmAluSwUw-f2kYjRDsH7YVkvyjMfwqoYDXV94JafPN8uZiyWADO8bTA348n5XQ4nBaWSxCHPhm_tg8tnsAO3ru62DU3Q2dNyzaePApsoioIomyGbCsZStZC5j1LLJ3gFSb3B5fZsmo8bcLczILpxF3q0x6rCDlbRusxnEIfu6yGFkkEp0pVQzaRwH3hVDEJb3BUPDqNOMEFookTAHaobTNPY6C275ivNh_t_VY3qbqEwyF7j8BLMzDjkDEWaiuDdJ-utbHTYsd1gVCYf0X9ORhGh_tWiCYgJ2btZe1j7XhXuNZduyiu2qOIoq6_4GkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره، سال ۱۴۱۰ هم امام زمان ظهور میکنه رضا پهلوی حکومتو تحویل امام زمان میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79360" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKrFLOJbNuDe0niY58_RENtRumPqCCCOT5joc7T-EhgytZmAKEzuYjKN5tok_HXuLrp20uoXksBmwHcgBq6YiOBA7B6p4Whl_WIi1JIaUVaJSChRZkpsQILQ5P_IuHjuR_UVCgqDlCmNL9TiKd2HcKpDY0ioE5cwbChzk2X_-Eov04_roEVVzII2OFJM_j272qF6wDNuk_kdaED82C9XmGDuptzob5s1j0nj-t1ZDg5lL6vB80GNWBMLmuXbBe_NpNzF6RDMa5PQefDgRCVDaDaJy75F9ooPVDKUhhoF02VEgzf3bv-94IKiuvlgEvybgtJdFXf62QZNSu7pOrgPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلش نمی‌زد فکرم هزار جا میرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79359" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">توماج صالحی از امثال شهبازی هم بیناموس تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79357" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79355">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTBWAskTNMDJdIU0ECCWxHBwFBPLMohXPVjM4ElGiyN0xx-Dyi7PEynlN6gcrTYsyaHi_vyN1gFsNoovtcpkNmyI-AXTxRNoSUUYy6bhdUkyp1KJCwxYydTpaRTiNnvGM-0p_mWoJNrAKc23KRBnLAN47bSqm9n9DDyahR9Mwtji9ExlGQ4r1rePBAX3oMmDQ8Do0j_Mc2xbw6tyhpzVFHUrGIB7wooYKn_-WxS790aDnUqK2XU5KGybzgM1DjNKyanCNcKrLcM8u6UKNkwPQR_cAQx7O-uVfUNadYowwctBW9wetawf_X5_gGkOCy3TR5pVKfhWoX6Xf3DotpaeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2JnGE7N6ExAfrUBikPU3ZMBbJkkz2H7Yudkoc399BtqP50NTAo2zMyMar14QsCNyB7p4rSPCEaDgZ6ny3go8shfQe2gniGH4qNQycOtppolMqLZBQ4_4pgdzEavXrA1lSwiWFSIlsUu8rVCLhl62VHX3uGJczXobGSOBSzZbGMxNFl94pQV8d9MWYzFNdW67wmLp670mru3aRvwDWp3jGWLho3cz_Ee2WkIyIyUewVImMpbw_XSQedAFMIjkjL2IoQEVykCA2TNRA23j378kwCf_FEsKuQFX_ZOAx8-YLZslNTKaur6r95Lof71ZkOu46fCmawVu3UO0C13K2lWzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو ژاپن کاملا قانونیه که خودخواسته کاملا ناپدید بشید و یه سری کمپانی وجود داره که بهتون کمک می‌کنه که هر نشونه‌ای که از خودتون و زندگی قبلیتون رو‌ پاک کنید و با هویت جدید زندگی کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79355" target="_blank">📅 12:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79354">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79354" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79353">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79353" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79350">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مسی چندسال جوون تر بود چه رقابتی میشد رقابت امباپه و مسی</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79350" target="_blank">📅 12:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79349">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ما نخواییم کشورمون ۴ فصل باشه کیو باید ببینیم
پختیم بابا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79349" target="_blank">📅 12:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کی قراره قبول کنید از وقتی تیما ایتالیایی افت کردن کیر رفت تو فوتبال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79348" target="_blank">📅 11:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTY2-cG3DNDrU8jc2v6tjCm1CZNCldOPMAsOJbAeUwrjRlGg6RvumXDXul0xbDdB8GalbVig9yGpIYgtpf4U5EX7IbvXSHOacHlqbQa-_HbVjs4yrSJcxjrvz80grJZE8WCrgyTsZaNUTTWh1Ah_13xmvxROdcnhqg0Tu4Hgf9iR5UUIEwXYOAl_xr5RMN7XdWgHqIq1Od2eFfkqWwyOBGZgdnPe0Gr4OayEMXU7wD0kfiXXGVjyMthSDnTYx4q6tx_77BT9Lsloio7r5cKHh_HD80chnYq2Vm8i-8U2hbymyEcqZliHySAJFv3Ub9KhuRrA8kaWL6MerlOIaplW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب بازی مصر و استرالیا خیلی عجیب بود، یهو استرالیا برا پنالتی گلرشو تعویض کرد، گفتم دیگه هیچی سوپرایزم نمیکنه که چشمم خورد به بازیکنا مصر که داشتن قبل پنالتی هایلایت بازیا رئالو میدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79347" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Byyz24HnLmaLCz3w62VycMIMtdH86ihMJXh5Lk4zOM3WMlDA-G6EEjA8HHqxY_yYLlULQGRitFuyl_8hAPdoqRw_nIhAedoGxrrSTiQZhaw2q1eCgbbEdzwkxVvYnamtjVK5QW5aWak3T_Pr40vYmhj7krw4yqKkYMBYkRCS4Idnmjyhbe6TO7NrJYPAjBXKvoYW7O5BDHVA9S7ulbDS3Adt_Owqz81thLOdd2RoB1INIFLj5nEMR20VbYfP_UKeLqWjyfAunNRJo37oZVb0CwWX79ar6fZJS_z9zVtyFdn8Ub9zBfRtpv9qfaCG68_isniLzp1kh9CUKYz0F1o6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببین حرامز
هم آرژانتین برد و صعود کرد، هم مسی گل زد و هم تیم کشورت یعنی غنا باخت و حذف شد و این یعنی به فاصله چند ساعت سه تا کیر خیلی گنده خوردی.
به نظرم الان وقتشه بری صورتت رو بشوری و یه عنوان آخرین جادوت سعی کنی یه وردی چیزی بخونی که مردم جایی تو خیابون دیدنت فقط یه دور به قیافه‌ت بخندن و دیگه دلقک بازیات و کیر شدنات یادشون نباشه که یه دور دیگه به اونا هم بخندن.
موفق باشی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79344" target="_blank">📅 08:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af167dceef.mp4?token=Aa6YgTIqGg0Y5jhQx_V6J3KFAz6ngl_-kJFtZpyTTf6UGS23ok8IDAlhzjL4y1b2zOrhmxNBYA9ZEApiMkc7PlEoa3Zqid3EDEfIhOl43GJzYOEn6sXdXkWksN4wJdKsl60PZPVRbMoPItOdSjGwXwdN2KV5xLXoxZQOEOTvvXDXDvasLyiW25dZiWHr_kA1rYGWoNhWja_ghJAacsVHItUie_czUH4W93_ji1yuyHZNqj5TZaOHQlnLGC-37v7xjvPTSWYWS9GVhis03G5mRzAJlsOxY2dZMjZj5WKvqCvBV1605qZZAbMy1HhL8xzPc2dMXBlBo_jUPVhFaRs9kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af167dceef.mp4?token=Aa6YgTIqGg0Y5jhQx_V6J3KFAz6ngl_-kJFtZpyTTf6UGS23ok8IDAlhzjL4y1b2zOrhmxNBYA9ZEApiMkc7PlEoa3Zqid3EDEfIhOl43GJzYOEn6sXdXkWksN4wJdKsl60PZPVRbMoPItOdSjGwXwdN2KV5xLXoxZQOEOTvvXDXDvasLyiW25dZiWHr_kA1rYGWoNhWja_ghJAacsVHItUie_czUH4W93_ji1yuyHZNqj5TZaOHQlnLGC-37v7xjvPTSWYWS9GVhis03G5mRzAJlsOxY2dZMjZj5WKvqCvBV1605qZZAbMy1HhL8xzPc2dMXBlBo_jUPVhFaRs9kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 2
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79343" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پروردگار بی همتای فوتبال، حضرت لیونل مسی بهترین بازیکن زمین شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79342" target="_blank">📅 04:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171cc02113.mp4?token=XrqAVwWYG3CJO7SeZoNEueHn1Fc1-x3Je-h7K4UjLZocCOeAMwXNIvxR2kFSAU1FanFvpC0LSoESDnhDOEkXJ0MfIkn0GimHC2L8xSFPAhkbypwlS4KUEWcDfCWTOqiAtL88cAxENllOFeHjD2LbcHXpnydIH0Z2n1W-_yapAmng3XKP6ymRj0sSQ5mmYkUfgXSDDxfCwqR3xnj5yiqfrbClgcmcSRFhp9w4SMFp9V27fe_pf0uRhqGGvL5l4pnmANdd_T8-ayekSAx7AQPY0gx1-qwj6kgyCvTeR9vOpM7Z8HiIZSepxBW8s1azqDiCzAsqVtbgM9-Hdw9TcqcoRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171cc02113.mp4?token=XrqAVwWYG3CJO7SeZoNEueHn1Fc1-x3Je-h7K4UjLZocCOeAMwXNIvxR2kFSAU1FanFvpC0LSoESDnhDOEkXJ0MfIkn0GimHC2L8xSFPAhkbypwlS4KUEWcDfCWTOqiAtL88cAxENllOFeHjD2LbcHXpnydIH0Z2n1W-_yapAmng3XKP6ymRj0sSQ5mmYkUfgXSDDxfCwqR3xnj5yiqfrbClgcmcSRFhp9w4SMFp9V27fe_pf0uRhqGGvL5l4pnmANdd_T8-ayekSAx7AQPY0gx1-qwj6kgyCvTeR9vOpM7Z8HiIZSepxBW8s1azqDiCzAsqVtbgM9-Hdw9TcqcoRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جادگر کصکش من الان اینو چیکار کنم؟
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79341" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تمام ارژانتین صعود کرد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79340" target="_blank">📅 04:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79330">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جادوگر بیناموس چیشد پس</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79330" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79329">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گللل سوم هم میزنه آرژانتین
و پاس گل توسط پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79329" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سیمئونه لاشی از تو تماشاگرا بلند شو بیا بشین رو نیمکت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79326" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ایفانتینو کونی کجایی پس، داریم حذف میشیم کصکش</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79325" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این جام جهانی خیلی شبیه ۲۰۱۸ عه
عملا یک مدعی وجود داره همونم فرانسس
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79324" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79313">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیمه اول با درخشش پروردگار فوتبال جهان به پایان رسید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79313" target="_blank">📅 02:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کاش‌ میتونستم از عمر خودم کم کنم و به عمر فوتبالی حضرت لیونل مسی اضافه کنم
ولی افسوس که نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79312" target="_blank">📅 02:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الله اکبر ازین عظمتی که پروردگار بی بدیل فوتبال جهان داره
ترجیح میدم برم وضو بگیرم تا بیشتر از دیدن بازی لیونل مسی ثواب کنم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79311" target="_blank">📅 02:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرید بیا بمال</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79310" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79309">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاهد حرکات بیرانوندی از گلر کیپ ورد هستیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79309" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79308">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خداوند و نویسنده تاریخ فوتبال نزدیک بود بزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79308" target="_blank">📅 01:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79307">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79307" target="_blank">📅 01:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79306">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79306" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79305">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازی جذاب قهرمان بر حق و تنها تیم بدون باخت جام جهانی با آرژانتین شروع شد.
به امید درخشش جادوگر غنایی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79305" target="_blank">📅 01:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79304">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پادشاه باقر امروز یه جوری تو مراسم خامنه‌ای گریه کرد و خودشو زد که انگار این منم که قاتل حضرت آقا هر شب از طریق واسطه پاکستانی بهم پیام می‌ده ?slm chi tanete
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79304" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79303">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توماج صالحی رپر خوب مملکتمون تو رتبه بندی جهانی مادرجنده ها قرار گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79303" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">استرالیا با حذف مصر رفت به یک هشتم جام جهانی، حریفش برنده بازی ایران ایتالیاست که فردا ساعت سه و نیم صبح مشخص میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79301" target="_blank">📅 00:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79298">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارشگر مادرجنده اسپویل نکن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79298" target="_blank">📅 00:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79296">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYkR99XplYQOPqSxaOrXGcYnfu9yriFfY4XHZ16VS6me8BMcUNz_0qgr6bU1_PY7X8mIjUKY_IdxtFgMtO8kzF5SGfPDBOS8P14p5mzJH_Ynfrt5e7oJbpfrBKyb3297EwMIi-IWI2Sg1y2I43HDWypxiJQVimUJQJO0awAUO0qnwuKAdYtOqU3xJV5mayHFrgAFDw_gwznxhXX1myawmECkrzKX7H5ptrNUjpjO5gGZbT_7ht7sd4sJahdNNchSJy5GrkTL0lQDuYspI6phnLRKDkJKL5Wjj1321mDvPNoSSnT4pfEYI8m1ogE-IdX77Bxc6VRAbk1JunpcPtp_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عجیب اسرائیل به فارسی درمورد مراسم تشییع:
بسیاری از افراد (ما) هم می‌آیند، نه برای سوگواری، بلکه برای اینکه مطمئن شوند او واقعاً فوت کرده است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79296" target="_blank">📅 23:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79295">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7mh0hBmXjONjjqyUoT_Lj1g6VR7_eZeSRmaBxi96wkgeK3H_XoApmaxQzMNBe13P1uvA-snT2hqpkgLBJQGJz-3vH9Lq21xnblxrcGduhlpwc624bEOfxI9EojyjIFHSBqgGqYH2aB7QHdQZ5dRO3-H4iNWOl-yO4BH8h5s25qi646FHdpU-HKJfngAGeZ1pCjmsKcyTm8t6BQT5apesSPv7aQp5DWSiTSMjlO0VpQePXH_Viyh7WjjkKnWLFBBZfANoLCSyoljQO_4pErp2TA9K3np04DZuSH5pDRQsSsw0Wffo_cztTbxXyl1mWh7WS7HPl4jA8p8QlQMarRy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه قالیباف:
ترامپ که کشورش ۴۰ و خورده‌ای میلیون نفر گرسنه و نیازمند کمک غذایی داره حق نداره به ما بگه گرسنه و برامون دل بسوزونه.
پولای بلوکه شده هم مال خودمونه هر جور دلمون بخواد خرج می‌کنیم، آمریکایی‌ها بهتره به فکر آمار سوء تغذیه و گرسنگی تو کشور خودشون باشن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79295" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79294">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79294" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79293">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79293" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79292">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تنها کشوری هستیم که توش
هم مرد ستیز هست
هم زن ستیز هست
هم به پسر تجاوز میشه
هم به دختر تجاوز میشه
هم به خر تجاوز میشه
هم ترنسا رو کتک میزنن هم ترنسا رو میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79292" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79291">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n59oFXwZCXtB2vDCl-Mr8I3b99GPMBUU3cVVLWHe482Kc8Do_47zsspY5G5Jukp9G3NrKl-cAD1Q8Uz2HN0hjTe0Oi48d9Oq3KTUi3tus4SRs8ytDek2Oht7nwE3tCMIRyBFJqlD5VBC8dyWqbFv6vw9LQyZWRa5TFLY2E87DIxcULvTi0zJDf6bX3zu0IqTCC2mE6YB-U4W_K6YwzdIHe15yoDmqCXg-DXS2nqWpsLPth3bEAYw4Tm-vTaQUDnpVaGrLwK_WVlCuJc5YKeH1ZwNtSxbFUDIE_f_CxgD4Y4Lu4kZagPPFXIq1smcvDIAYVrc6p_FVlUt4s7IAXThgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جادوگر غنایی چرا یه جادو نمینویسه یه دکتر زیبایی بیاد صورتشو عمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79291" target="_blank">📅 21:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79290">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeFpevNTpCehI-9lHB7VUFndFUE2-bM92u3J0sYCHc3Devk82ZaX5lzIVhnUwdD86isd90b5t-J_mu5Qt1ECIk44AvAlpEbzWpRzdJOKzA7x8Rbj4iwD9WCvqUovBpX6owlzs9N0CxHR_Pgwd85-WhoC9Kw1FzkWd4_BNU-gzoK-v_FLjLMhH7i59VVyRLmjKFYq2F9XMmVyE_CPsl6BAb4UI_9MAVqGf7uQzEPMHlLMvAp30Uy-wfBqUTqu31b08OZ2MVjFTqNmHBpQeg0PTnMPkjD90M5MWvhXLZ1DMpLlCxPzG8cT1cMTfY1PGkaCuMm-vLYiNxbUtjzwPKovTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کی رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79290" target="_blank">📅 21:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79289">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چندتا سریال تاریخی بگید ببینم بلدید</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79289" target="_blank">📅 21:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79288">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79288" target="_blank">📅 20:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79287">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCjEnSK2YkLqqEe_mk9Op2wgcNqdeJLNPW97ICLterbrSbDpdqNpjIIZQZ8nbUpH5nQcUj_wYzUDrjhCzLaIM-TOhN3gs64kjT-Jbrtip_C58IE19jXCfSvWi0PUCnyvv1yfnH_qwEMR2qlK4IWthMvYzcj0E1ZOccj6WsXVUAKt25UU1pdy_RBNtZ3shMMfmZswCNmZH2VUDF_iZikHN0k5WHr-ktCqP_thLJ5VZ0dIGBMDMinHiBR1bNGChWI4LiBA0XGn6UWjOIsY7lpiL0aLhcWcZXrQVnozGNGLQz9C3Pk_NaahqASSRZ3GYPerJNX82VuUr43o9rK5g3rN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه عباس یه خوارتو گاییدم عجیبی دیده میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79287" target="_blank">📅 20:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79286">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یکی از عجیب ترین چیزایی که تو ترکیه دیدم این بود که تو کلاس دانشگاه نشسته بودیم یهو یکی از دخترا با دستش نماد گرگ رو نشون داد و کل ترکا شروع کردن به زوزه کشیدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79286" target="_blank">📅 20:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-27napeIBOSbK0FL20RY2t5Ir8LjJHgwO_eRLmAUvg9XNpH96HrZYk6GC-kK2GKuIXeM-rPlCWr2LMcn93nWHBKcazOjw3hTYYj2XBtPCjtcBFSUUBtwPdyPtLNOrVEEQXTkijW3ghgTtcD9hmrEHkX2sfVKpLwC8Tz9VxboDYivGO-CEI6q4esZ5FOK5DzogkNM24OrRPmnVB8_wa1lRzue3tiAVBu5JzE7RYEyNiv7mPiFyItvmI3t-jVz_lR0OEXoT4go7FeTwxXqX0GvjVpwLzRwSWR-074rb-fboX2K0hX0yR4c6JJ3Kf6uiUSiv6ftIDCDhqTB27X23vO_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ژنرال مرحله بعدی با چه تیمی بازی داره؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79285" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-lWsTPWRJXdpmCm3yPTdHuUUSoiRljPgeBAXag-gD4cvSeMU7jHyHmH19wM56oR3pFA9z7HRugdBuoalsnmxcj6v5OPf5UryAwzsX0dE_aZYwYH0E4PC0kKAqlQZovL_-ocis2JXRaCHY_ALkUjkVJifa8Pc2SOaNkZzoKlX-7aSlMm3Y0Rfov6k6OS9qhKw8D83wnHgKz_jWHopbA4UJLbsSW0i4Mami8-mpUa4Iqyu82v8dTNk7q_FJfhPf41ozwxAzokMXalHLEwIAqs7ISOSaAMkzno_g4qQKbAOKV4wkU9HlsltvmDiTbpzSW1l4PiwF3qvGNcnLwpCNOvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79283" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOOn-_HR3cMIkCg_1CMnxfYU1wo6inG42hP8eBODr5PwCIdIq4G_BuWCcMcVwVEZgJkVs3fzzo0ciwaq_kFOxPK9x5owmOEB-6r0MsmfV8HQhDufrO6MdCa4rx-wr4ghJKM4_WVs1JgtVvFai3lUGaE2IyDlX-wp2bLIXGOjt_nqBbfMvfviIZkS5qDAYte-KQKnVYAOMsZ10I5F2z8rJ4BGXOsVODDeAm9boN56m28hTZvSlEpOsQBpTyrJsUR8B2Lyqh0l0reU7tPCswZ0eoT-2DiSWKkdZuEgBXePt6dKCIXcpnz2MhpCv4UqSQqL2XvAGwRuaLODgs_q3I9w_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهر حیدری و ارام طلاق گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79282" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjHWd-LmpVoYcl3FvedS3LnmlaIx9Ai0qqU_ATHaEWIQENBdn09GbW2zHh86wr5kq3JrHrLJFB6YD37Ue9zoXUmIiCMk_7Bk9NXVZQpyl_YbigY2O2HVpNE1e-avIXNs_bkkZKVEZz7ZRzAn8cOsvAeNueZr3lpEGYhyjZ2my9z6Wfw0REhFE6pi-yQk-I5CrvAHUEfa6B1s5DD5fYEZwafyALfH4heThAAP6oWDSKKm0T-fIvNzNSV4rYBIx8LUsfoM3rB1RojhtXdZtzqanSC9OWEBlhgVziAb9le28x-B87i80fA5Ci5prttcwFTRXPg1a03eTnszKhoDa69d6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه پاشون لیز میخورد میفتادن چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79280" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0Yj6Brdeo6R2RbKLW6weTFP0iJinjO-dXkX7WqS4_RW0vZT1Gry-ALnjni68M8iwAhcFyHB9Cno_wtbQrNxKYmRTbIrTAgNRzBN9OP9y0y_EeKBNZpArm_HoJU1B_RxkQh2jsc3YuMFcnJVkhvA_06SrVgDxpUvQwQ21rz3WelKzje7lcMVOu_7Lwy1ICAZoCXs3d66IR_-8t_wKoIc9zRMTSMlMt6yXwSW4Ci_PxuMP8tZ3tyHrWJ0SK9VZJrkf2yoG_JSvWiNiapCl5q26qnOLchS94BBm9EZ5ANyO5F89sOrzdLKjIY7B7I3rCfzX7l8kh8wCvHqN4cEHIdRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79279" target="_blank">📅 16:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=PcyhLcyDbZqpJDsx8x0JZchF2lFUaa_JJly4Grx3cd7NIHyjzjvJRHEDdHFR0_8pRfoXwzj51reKNw1jl16w0jXqPFK1iUrl9zyPKNt-Df6wODkF-s2Mtt9G3L86D9t7p8FDa0VwIyRW_F5bueKKgOosE34mOI-2NEw2dKW1badlXVqCXyvXQ0BCKgEaz3xRvPEk0_5kXo57JV8VGgC4mywcYoLehAWthVuwRW0E72SJ4Yv-YaDVhlVBIV2DolTJBHuwmqaOolIoK1F8btMLNI39qnUFIwsezR0cxwGfmEO9rHuG-2IAeWjq-XWSrGBkuCgsZuX8-kF7x4299QZZtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=PcyhLcyDbZqpJDsx8x0JZchF2lFUaa_JJly4Grx3cd7NIHyjzjvJRHEDdHFR0_8pRfoXwzj51reKNw1jl16w0jXqPFK1iUrl9zyPKNt-Df6wODkF-s2Mtt9G3L86D9t7p8FDa0VwIyRW_F5bueKKgOosE34mOI-2NEw2dKW1badlXVqCXyvXQ0BCKgEaz3xRvPEk0_5kXo57JV8VGgC4mywcYoLehAWthVuwRW0E72SJ4Yv-YaDVhlVBIV2DolTJBHuwmqaOolIoK1F8btMLNI39qnUFIwsezR0cxwGfmEO9rHuG-2IAeWjq-XWSrGBkuCgsZuX8-kF7x4299QZZtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کنم دکی پولو زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79278" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینستاگرام مادرجنده من علاقه ای به خداداد افغانی و خیابانی ندارم، دست از سرم بردار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79277" target="_blank">📅 15:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpYzXNn6HTbGiU0P3GS8qzGUw5C83rGDkdVjOGPKLzZmGWfWZmdVgW9eOXbCyUPZjUPrU8JX8f3fL1k2jyVG2iFPpXApdbos3flSHbAXJyEtXfFQl-l8k0mx-GzRRLQxVFG3oSwlGsnnU4t5Iu_TeCxSsIL5eZn6FLDyaKclALD9vnEsByVnF72xmHpLj4gntPQhM72cboaZLa6-twmcHb-zv0O8COFVz3tt1FgSLqW5bjljdCPPI2RNeVUxejQLvcm5JqC5NipRNrUprKaivpDsyCqpKjrgvjiFLKQuHcxwaKVWiQ-eRVavyytaox2P-iPP4qcUoeSpMikgwxW4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا تمام مقامات نظامی و سیاسی امروز تو مراسم بودن به جز اسی کوهن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79276" target="_blank">📅 15:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کاش یه مقدار از پولای بلوکه شده رو اهدا کنیم اروپا کولر بخرن باهاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79275" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
