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
<img src="https://cdn4.telesco.pe/file/N4ARMjTvPSJ_uKgvLx1nkySQF9pTAHRU59lMqOi_eED1HRegE_aw4_fwxR5FfRWVabv23mCmB5VBTKwiSxLIEKfyAYn-fX3D01xJLzOSbecP4ms9Ax3xJ6uQ9dxfYdSl4O2zD21NQ0sK02ed5QDd90pDfN7HpV9hKrzkWsr4zV8AUQKWreWHOSF6yUs3zMyNLcc3rRco8eDSdxFdjif3s2dkYmJGJ4iqDLOO7-agT5tCez0N3sy6x6v5TLnK-3d3XTya4gn_uRGBqO4aBgHRW9Dk8J0ajwo7ixO3Psa52ZphEiPkjIyX2yiRwreqTKFNZvbfAlsttOVgvY__GAX3Gg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 04:37:41</div>
<hr>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c0b0a4f.mp4?token=CEvlbsfnlPEwI83pr-2Q-U3b4PtTgjy-SBzb_2A4_Uirx1aQaArx2VlCBFTLd3ydpQyjIaU_T8FEIJh_wtwSekXqm1W10nPOHFLSdOt7Bbz7wYQbUL-BgZmmj9QKpC1oa57vqSw4940cAyICFxuKWcszIhAJZrmrFmOcflmANX83mw3QP4WuNipBy0_Xw4VhpazCKtpA6mTRhkQj2aTXf-ZuoWtgyNwtfnHdVJYK1tSww6rKGFJoudm5I9WGPRufaHOBcCT5zsEeVwcjLh4J6gOPvso9j-ylsfvT3EZsdeMfKsfLICm7yCaWX3WXC8U2Owpsc6dq8FHuzYJYs4UJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله و برج اسکله بهشتی در چابهار</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693dd42141.mp4?token=C0rYXg4AGESmbiarrpUjDZhCkUwUbhCjnwg6Jkxm-pFbASKNBBNND5s4X-6Ed9PdA4p5vuxUiW4TTGYpImVW33lHQfcP0m-7SFZNqzCW1lGCiN3_7_WjeCdnMi0uVYJ6rInyXa3D5-UG-yaXE5Ew2RVbtb96_6BgFgMDNwGQBe0EIYzcoZZeWha8rzl6jBhr48BoxR-_9JL9kjM8K-PMT6RX47sRTbOREpX-s4pjTikOYZHPJUhv-fbXlC3DwC5VcxvKQc6FWQ_AvrkIXfR1P5EeZiQu3xbtKwQP0C8SlCB8XVT2KaHNxAA39DHTenev0kiqX0LFezcES3o4MmdaqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693dd42141.mp4?token=C0rYXg4AGESmbiarrpUjDZhCkUwUbhCjnwg6Jkxm-pFbASKNBBNND5s4X-6Ed9PdA4p5vuxUiW4TTGYpImVW33lHQfcP0m-7SFZNqzCW1lGCiN3_7_WjeCdnMi0uVYJ6rInyXa3D5-UG-yaXE5Ew2RVbtb96_6BgFgMDNwGQBe0EIYzcoZZeWha8rzl6jBhr48BoxR-_9JL9kjM8K-PMT6RX47sRTbOREpX-s4pjTikOYZHPJUhv-fbXlC3DwC5VcxvKQc6FWQ_AvrkIXfR1P5EeZiQu3xbtKwQP0C8SlCB8XVT2KaHNxAA39DHTenev0kiqX0LFezcES3o4MmdaqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش سوزی گسترده در بوشهر
🚨
کشیده شدن دامنه حملات به جاسک و ابوموسی
🚨
گزارشی از فعالیت پدافند بر فراز آسمان اصفهان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQbr2QQISjVSia5hYpUZ8i9fYCdVLkSDje6yu5sne8rOE7svuV4afU3gQ-vIYkZ1LCPriPDcIPjLBQf6jP-rX1gvroTzLceNsmGaW9cyYvG7W3CNxGO6GHpL_zn1VMQ8xsLHtTeunRwcMvAW_B8ssGdpuMDRBhR8KFgNwT8pAdBRXJcXmTPNXMe6l_xg7OeyLg6M0FMNfGmiaZ5SrXzwAY0D783h2D0dfiUdar57sRIbVgVBvLFJ9_buGsu35IcbDRB6Cl0gJmVjduyLcB0XOoFL5xpZvpcAhXjNRAc7TW4AvzLZJ-k4x5y_5k1KX5ULDQUri7V1Ag1XInH93CvuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=OpX6kknpm8Iya1C5V_GxOT6drTYayt8Wstx5lDoLeF22SZtQb2lCWU9eczABtMOw3LWnprG76ZtNXpDjLnbGLqd_45Mj_4ixLjT3EkQxSl2j-BaYit4zT3_U6DPtSuEblTlIfXPBkMHnGNVltkqVy6xlaNOpWLCs22cU2UG235DCFVbMWAE97XROUDMDmVEr2v8BU_ovYR7XbjAs9cGpxapVErCsNpckehCiGfPebAHvQq4KqqU0Hs2AVeOEVmg3NCwM1tXmJeZcqaKnRv2h06vi8pg4wLN7KfO7FWUXG0svtYfOx4B--TSgbht6YR2vQFN84kqYzHcab7Sfqg3zRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ae34ead.mp4?token=OpX6kknpm8Iya1C5V_GxOT6drTYayt8Wstx5lDoLeF22SZtQb2lCWU9eczABtMOw3LWnprG76ZtNXpDjLnbGLqd_45Mj_4ixLjT3EkQxSl2j-BaYit4zT3_U6DPtSuEblTlIfXPBkMHnGNVltkqVy6xlaNOpWLCs22cU2UG235DCFVbMWAE97XROUDMDmVEr2v8BU_ovYR7XbjAs9cGpxapVErCsNpckehCiGfPebAHvQq4KqqU0Hs2AVeOEVmg3NCwM1tXmJeZcqaKnRv2h06vi8pg4wLN7KfO7FWUXG0svtYfOx4B--TSgbht6YR2vQFN84kqYzHcab7Sfqg3zRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب - چابهار - حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQE3Cq2IarY8X-_Ou6fz_-qdBGWOOAVF32SgEn3wpQ7GxdTW9gJJMpVsTqkxf4WfRWLsiIC47_6L4dqaTawOmQ0EA_R6CvyqrgXe_0V6178I_-cWEtPwoPZ2qb3Do0qZ0xwmnFgG74TyLte6p3amF0VGUX5xff88KckCTAZwVwIdr6bNlBDONk98nNenh5ynX8fDU_RH5_5JMtLMGqjZX7znw2kWW5mnExr9dycuYTt3lEgX5PL0EbeUFsQ2o4oMmC_JI8rZ8Jv_5cWTImMpBaEelpQa28fYWLWiOKmpk_YpBh7lwD1kAwiWoq0BQeWL0lwESN2nkNvTWwPSIX__Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=rJF7EeTRC4n8QscbBSwyywBYgLGNt_bxCZ0ukHDzFEOaFdoWqCR3janNRcHjRNXdMn0tW6WPCzJ0aRdJyp5JNdS6r7UmFfyWL8Q2Vllol5CaQzACk3YVplRsOtgd4WmgQgjBikTIEf2L_6CtcW1K5DojKXIWfBXuUPt9hT3kR8YW5jF8ymuY95iVZ_fmJVj-36bt1q3_NSVcxbTDuSSsWKMyyJNhB7bJFPzL6bSEB4DwDfQ5dfmzo5U6pUVPfAW_tYeta4dbewV5HPCtJkXi1slJ4GVjWneuhz8Dufq9715gD8tLdOSsy2gOxIUqT3O-HzNdeKucU7zgKpYknGNO-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030961c3b.mp4?token=rJF7EeTRC4n8QscbBSwyywBYgLGNt_bxCZ0ukHDzFEOaFdoWqCR3janNRcHjRNXdMn0tW6WPCzJ0aRdJyp5JNdS6r7UmFfyWL8Q2Vllol5CaQzACk3YVplRsOtgd4WmgQgjBikTIEf2L_6CtcW1K5DojKXIWfBXuUPt9hT3kR8YW5jF8ymuY95iVZ_fmJVj-36bt1q3_NSVcxbTDuSSsWKMyyJNhB7bJFPzL6bSEB4DwDfQ5dfmzo5U6pUVPfAW_tYeta4dbewV5HPCtJkXi1slJ4GVjWneuhz8Dufq9715gD8tLdOSsy2gOxIUqT3O-HzNdeKucU7zgKpYknGNO-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات امشب آمریکا به چابهار</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxKSWjSmIZRGZCkiIdztiiXPmw7MI6TsWnzLxX_AJEyaXn6s1X9kzMjbMn30_ayUlpX43jgOi2hKsaylIDAERPdR9wiSz5wIZY5ruhOBz29lqEnvQ8OJA3QE3xoOOn07hJ7aPaXAstfulhyboeoyMGoOar8LOWvMcfcxoR66Axqafd-J0EBZkLg8Tgqglw7jCnAyFzoOgDi0j_ZqkFDps8E3JXU0zNqWCiK4fh1l6htJhQKhgNfpm6bWuusQnRQwpD1aIG4rIAakmimFuyal57AGRH7BjzW98Pm2p6etv_0cHru_OKew9GdlilnK61ISD1nMQic1SZi4rPobpk4Usw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=XkP7L4x5NF0tgJ3bBOG_ttkCSOfc8NZlLmIZi_yHMb1x-K1UP5Fj986yGJA4-b4YBkiOmNvVbFePkNVQOVESvOwm4k8JERhQyN0PQfsXGscCUCs9fkzn9cOFXT0KhYkfIweJ2k75JUdrHrnRiR6u23Uliwgx9daZOXexFZKIQSjANIkXnpkkGesRc5cXO6-jHdW4Ylb8DeLvJ1YSF-1yRwhqDF6U5XBXIXofuQ6969Y72MzG26lVmWyt35jVxPGt__wnv5MKKqShr0bnwCY8HyaQeVkOfDVtXd3IhmgEjPTCFl_zrqEeCgjyNFvJDIvYt8MlSe7xkf9AUWrP_Shwfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3530f756.mp4?token=XkP7L4x5NF0tgJ3bBOG_ttkCSOfc8NZlLmIZi_yHMb1x-K1UP5Fj986yGJA4-b4YBkiOmNvVbFePkNVQOVESvOwm4k8JERhQyN0PQfsXGscCUCs9fkzn9cOFXT0KhYkfIweJ2k75JUdrHrnRiR6u23Uliwgx9daZOXexFZKIQSjANIkXnpkkGesRc5cXO6-jHdW4Ylb8DeLvJ1YSF-1yRwhqDF6U5XBXIXofuQ6969Y72MzG26lVmWyt35jVxPGt__wnv5MKKqShr0bnwCY8HyaQeVkOfDVtXd3IhmgEjPTCFl_zrqEeCgjyNFvJDIvYt8MlSe7xkf9AUWrP_Shwfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگفتی سران فعلی ج‌ا آدم‌های باهوش
و منطقی هستن، چی شد امروز گفتی
که یه مشت بیمار روانی هستن؟
ترامپ : شناختمشون!
و لبخند رضایت مارکو روبیو
[معروف بود که روبیو ج‌ا رو می‌شناسه
و ونس اینها رو نمی‌شناسه،
ترامپ امور رو داده بود دست ونس،
که الان ظاهرا دوباره برگشته به مواضع روبیو]</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqio4D2q-qLws74KDCaiR09ijMCVB2Vp2Uc7zcICaOuSNA5BcjexN4v9UZiHU_dx8wzwOWvsYSuiQE6ktFNXMYdFMz2OyntzK7F0kX-OJpEs-H_qn-k3MKowsCgbbBrLFsy9OJsBpQtDlzf0wdgdTxuNtN1wophjMMMRAPf0lcWu9mGP_Ki1bv_vc_5ZUIWb3HUFaSX56m0msqIcvQ1Xg7Olu-vQSWdowYqiFgw_ejwD4Gl9F3POgo_N7ZZCDw21J2_4vck3seC8s3B5-uZVX8m-BeSRavHECVhE5e6SbkkQsdo_Bx5hZJ4gsN8Iqg-9v0P2sH1GDsuMxxa2E5oOOpg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5d27edac.mp4?token=HAxQoXabwVa_RO4wkNJLG3e7rEOlQyjbcIchLsdWbLKBh4JfIL87wqmhynp8wjjqe3Nzw7oM4soQZRQTnWBFPaIukYvDwF7H2xD_CkycP696zo_1ELlUglD7aPfjFaU35hiUUKBEv_Qts62kOaFuWQdHtp9K3EAN4trW-s4GAj7-0Zb81EoFW3IsGz7wJnjNGNa7FEbyWr0PZfbNGUm_0ysWzoN33VCy7xdOsUx7PznCN9pO6sawSG6JGXlDJWUP2h33jdYSHymr5cpOmIxJpqeZXyYvTkpxzBMjl5Il-YBaVqxWY6Ht9mtnUXBBOsBTNKV-w1I6mWQ9G7TeM3Zqqio4D2q-qLws74KDCaiR09ijMCVB2Vp2Uc7zcICaOuSNA5BcjexN4v9UZiHU_dx8wzwOWvsYSuiQE6ktFNXMYdFMz2OyntzK7F0kX-OJpEs-H_qn-k3MKowsCgbbBrLFsy9OJsBpQtDlzf0wdgdTxuNtN1wophjMMMRAPf0lcWu9mGP_Ki1bv_vc_5ZUIWb3HUFaSX56m0msqIcvQ1Xg7Olu-vQSWdowYqiFgw_ejwD4Gl9F3POgo_N7ZZCDw21J2_4vck3seC8s3B5-uZVX8m-BeSRavHECVhE5e6SbkkQsdo_Bx5hZJ4gsN8Iqg-9v0P2sH1GDsuMxxa2E5oOOpg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برگزاری مراسم رو
انگار غزه است! با بسیج کردن اینهمه ستاد و پول و ارگان‌ها و…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzzSsDYa8IXl7mXx7DOeEqP46ZcQdnBRUD64sU3JIY19s2RCYYLb_q3aDDtFOYzPCzNOncjWjzLGLfgb_Dqhqr989KFz42vbUMnRgQIeFX5NvkQp1L1eiQ3il-Gc4CiKOAprVvy_9OCHOLDWmGanGu4QRl_WYl9UdsRFepC6MSfeNnL-VtmrhDZE2IeX07dtUkvSA35ZHCwt-RbjEXs9oYxHaln930TAMkLQYmUJUc9SPfZOWe4We_oIGHg1EXT_yR4pn8exr_ZrpoukBvVRjI8rZ7rRQaIXvfuboDHX9MzWM0EygwAUgFF285h70DH_k1-CO2_lB9z3HkZpqh0XYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c23cc7c.mp4?token=Ki1alEeNcLwnOfBYCsOQxnFOSW-36GAObsluWfWob-aO9J9OQRJDHnsXNLD52g3OD4dXPUMdRFyapNPrHhpXswFdPruwvn3cR2Cl3-RX9zq5lUnXw6PXBkd2WjmWR0Rk77WGJN96trcxD4VhK7RnMLD3mJ9EnQFaSVr9XGR61Mx6XxLRnA43ZzWRrRR4N5K_2AU1ffSFMIqyDyXSiw7CK199XL6_Vi6PDSzr_ZCyjhm_LK_kbQTzgnborVhB6NEk6wabwt31vaBur3cqZ_gRGvgYZUxVH67J5VON-ZfCjhlf4ZLiB-HMH2tdubae9yJ-AwxXK_gTvplDSuYdc4HvhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - اسکله بندر عباس
زیر حملات ارتش آمریکا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd51af5b9.mp4?token=PsPYqlvxWn3WNiH_ZG1O3erxgZxRHjSt91ypfNNq9AAYIU0OmOOIPcnWt3kbrQp4Z89aq5gXw1_nZVqhTW8TsTsjBRGn8ttzK2oXcB-BHksY4Af0JfW2LJAXH5SzH-qc1ceylOL60l4biafWTHu6SQmMIYjtbtUzOhthKcehJzXylkhcd7sIPPSPVTheYG61zqdZLe9tloc4gdW2bT6Pb4uOTj0_9QC912mMaq6kg0vItDXhu9Y-pmM7hChpm4PSoTI3zNqRX3VSryiYRxGcOC1aBVOH9kicLCDJnhHiGxmBlE3htlHIQENljTKNOyXSi_JMR_MkyUNMksqEiUoR4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مراسم برگزار کردن … ستاد برگزاری ، هزینه هنگفت، ده‌ها ارگان و ستاد زیر نظرشون.
بعد کارهاشون رو ببینید!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIre10lVu3bv6n95sdd_v8I4n6IN-Yuw_7LKmlVCtqoJ_dxwLl4nuNEvxvjwTfwm2fWEjIx1p3ZRL5gNQut4T45kYNHLZY0CqTVZMjsKTVU3ZS6OvKoTiVXPr1QWApvOrz_Wlt4hjUrmjMpokiOmyVw_fU08KQcOpXPj6x1VgqCfARO22d-OpgMfF93uArlZvssw8DoYmRhvPQ9LsktneWqjC4h4KvlXP5c-VJw0pJH5kFS0wRmEB6426DiFR7pRMQec2lH0m0wCyvN_QeEs1YzwefGlaGvUgoE5YZYfDItfbo509lsk2jIsgyijMsjZiJlWZ-BUHDjvG6KiWG62-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=sgBpgPTuL5SI7o3j5-kbNVYJvSJDcDRs-PHyJ8kIDTXVc0GTEnV16m-asEfr67V_do_F5EhkgBYPDthVK6AuPR4aKeLrRV3mL9Mui958tnob_uDk_Fec0o7AR-Hf-i3AaMigXyF5_Vd7k9QYuSdqvJ8VlSy6R9MT78iLTk_VGJ-Q3LMwdVI1yYFKQfHkACZNdMXariUx7tx1Nfyu-HA_XW1-jKv0uPyV_uvie5VhH39aGuCvE-M8vK_0AQg3Zd_do_WTP-o08X3BtZQpzeUD2rfvs8EcZz-2uUDKuCD6C6tqZSrWcZY6HFIa1uR82Lelv_M2yMtqptCsMlgq7wN_9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=sgBpgPTuL5SI7o3j5-kbNVYJvSJDcDRs-PHyJ8kIDTXVc0GTEnV16m-asEfr67V_do_F5EhkgBYPDthVK6AuPR4aKeLrRV3mL9Mui958tnob_uDk_Fec0o7AR-Hf-i3AaMigXyF5_Vd7k9QYuSdqvJ8VlSy6R9MT78iLTk_VGJ-Q3LMwdVI1yYFKQfHkACZNdMXariUx7tx1Nfyu-HA_XW1-jKv0uPyV_uvie5VhH39aGuCvE-M8vK_0AQg3Zd_do_WTP-o08X3BtZQpzeUD2rfvs8EcZz-2uUDKuCD6C6tqZSrWcZY6HFIa1uR82Lelv_M2yMtqptCsMlgq7wN_9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/046bf7600e.mp4?token=lWSldFXcULycTu3WFD_3dNN4pS0Q4lmhUd8itfcvOwsG22UJGIy-W6A-vue_bANKACOxUlkdjMS6YcY1Dq5H4aMoyj3KVsk787lFKQLuBTk5eYUPyX5TvQab0xBUXhppvxpAGVwylJz1t0ye_18BQ-zPJIJ07SRIh9f54NbKBBTKwXuJpxbjKFwIGmnCOsw5qjhDcd9VnfXLdkcnYjgRwZNCmb-rlYgG8_knlCBJyo0WD07ihodMjys1LD8veB8BGQdxAMnpNVzlXA2Z0rgRvuzqDTracBD6ESaYpIG8MssrCmZmjh8UU1EUDyao2kt-DbK2fGYJ4VHOEKgIgziKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هگست وزیر جنگ آمریکا : همونطور که ترامپ گفت امشب احتمالا اونها رو عمیق‌تر و محکم‌تر می‌زنیم.
ترامپ : محاصره دریایی رو هم احتمالا دوباره علیه ج‌ا برقرار کنیم.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=S1NYPEvGu8_TOua43cyVDKBo35-xphmZueGbV1BLIxNolGtqqof6rzLhC8bMe3_8aBQOvIyghUlD_SlLvorI1SoAQU7MRHvxn8PWex0dqDz-TJyoDjgxqM2hV0Z8SfBlwMkT15SNdroTDIkbOJC551bbQGv0XuzwZC-4uV9PFqgZnctquHhAhmOZ_ooJ-JvxmGW4r5Y_JBObe7YRrc_mJCMhQf_HQ5kIKMrsVezF_a1S78GhVYKmBnwkteqCxH2P3Gsm5JC4ptjPrP0of32jpdUHoarL3T9cNXjch1Hvucogzd4zlJZSJSs8kvb-AEDhV0IY8xFK1Uvsaqh1iUpMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=S1NYPEvGu8_TOua43cyVDKBo35-xphmZueGbV1BLIxNolGtqqof6rzLhC8bMe3_8aBQOvIyghUlD_SlLvorI1SoAQU7MRHvxn8PWex0dqDz-TJyoDjgxqM2hV0Z8SfBlwMkT15SNdroTDIkbOJC551bbQGv0XuzwZC-4uV9PFqgZnctquHhAhmOZ_ooJ-JvxmGW4r5Y_JBObe7YRrc_mJCMhQf_HQ5kIKMrsVezF_a1S78GhVYKmBnwkteqCxH2P3Gsm5JC4ptjPrP0of32jpdUHoarL3T9cNXjch1Hvucogzd4zlJZSJSs8kvb-AEDhV0IY8xFK1Uvsaqh1iUpMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=Ly3TA9UodZ1QP0B9BnZA56f8ExXxoS-bv3lMKQrJu7tdj09scwX2seqrJHUvEkk1OLt8zsSfXxfcf_CTTwE4TXNMmWoasX-5JnSaZVvCpYqdLhDR0VHjxBkhm5ajPl82fd67O5LrUvU-lcVNHdCkkOrBOeC9JfrQB6nIG179kjRqTPSmWyjGBHsme7xkLQ9xjwhVxLiGl_3uqNO4RVNc0Lw_8IoNF-hATgMKT95R5zv3eqV7UNHFKzZGK0S36TwSMvNDoN02jUpY6dZNkPWgtwRljh0t6oPeh41wf-8K7SPCkVHI2NJZgOzZ7AaP0VzxsYxXV6pEz2u4vc5W7S_lDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=Ly3TA9UodZ1QP0B9BnZA56f8ExXxoS-bv3lMKQrJu7tdj09scwX2seqrJHUvEkk1OLt8zsSfXxfcf_CTTwE4TXNMmWoasX-5JnSaZVvCpYqdLhDR0VHjxBkhm5ajPl82fd67O5LrUvU-lcVNHdCkkOrBOeC9JfrQB6nIG179kjRqTPSmWyjGBHsme7xkLQ9xjwhVxLiGl_3uqNO4RVNc0Lw_8IoNF-hATgMKT95R5zv3eqV7UNHFKzZGK0S36TwSMvNDoN02jUpY6dZNkPWgtwRljh0t6oPeh41wf-8K7SPCkVHI2NJZgOzZ7AaP0VzxsYxXV6pEz2u4vc5W7S_lDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sRJkaVDw2MN8WuVd8vt4pvaLgl42m2BOtUOs65D93ND7bxhbvv3jzL_gn8YBFlFmxhGDD0dS-Fzvl2sro7IIK69darVk8WFACa0ku0-Keh0oZMYS6bO8ICpgQbhqiW2zggOua7t6pjD3c5Jj2TX2B5NHM8JRNvMeTc9LI6PmRD_VSVlpN8PtfR9Mcy8iovDNWtYiompG5lPcgxiL6g6k0bGLeV-sRUa6giltpJEw694Q4BEVmwpO6VzG2kLZib0Si9XXrRWa1Lood3FVkftIodoqiFe_Js1YCvt0f5UTrLmMWhIHHn2-KAZOydaqpU4oTm9Sl7p2jp0f3nrsMN-Jgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sRJkaVDw2MN8WuVd8vt4pvaLgl42m2BOtUOs65D93ND7bxhbvv3jzL_gn8YBFlFmxhGDD0dS-Fzvl2sro7IIK69darVk8WFACa0ku0-Keh0oZMYS6bO8ICpgQbhqiW2zggOua7t6pjD3c5Jj2TX2B5NHM8JRNvMeTc9LI6PmRD_VSVlpN8PtfR9Mcy8iovDNWtYiompG5lPcgxiL6g6k0bGLeV-sRUa6giltpJEw694Q4BEVmwpO6VzG2kLZib0Si9XXrRWa1Lood3FVkftIodoqiFe_Js1YCvt0f5UTrLmMWhIHHn2-KAZOydaqpU4oTm9Sl7p2jp0f3nrsMN-Jgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هزاران نفر که اومده بودن توی خیابون‌ها رو کشتن!
صدها نفر رو اعدام کردن، هزاران نفر رو زندانی کردن. اومدن با وقاحت میگن ما اومدیم توی خیابون! طعنه هم میزنن!
شماها با وعده امنیت کامل رفتید
با پذیرایی و امکانات. حتی خیابون رو تخریب کردن برای تجمع‌تون، کولر گذاشتن براتون!
خود گدا گشنه صفت‌تون رو با جوانان شجاع ایرانی که جون شون رو گذاشتن دستشون
یکی می‌کنید؟؟ طعنه هم میزنید!
شما هنوز نه این یکی رو خاک کردید!!
نه اون یکی رو می‌دونید زنده است یا مرده!!
هست یا نیست! توی چند سوراخ قایم شده!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC4j14uXLSQ4VhXLvoTIacocMtj7UwBHzR0fIXydb3JMxu0sHUYKoLCCrKJZ5ZUdwkfq0SGnGRlcWcvDHr-MWh8Nw1iAdqijvF_llpWcLJZS6uaPrdUYlaSrgjJcoX4hrkB_BPTUTIP5KG7T1qYyqCRg4ZczwixtoWXVyTr_8DgG4WcthndaHMtM8Vgq-efcwxrVQNXoVGYUMPVspfWT4NJYWoMuU3AiDA_5MSOmvl8XrUGEI7ZhRMqX8ibjTV0UYd4p1Cjy4IFskN1iv9LY9Lq6cRSQhJc_MkzV9t9sAwydf5RASfwpfJlA4crvHVZLwcOdD9l8_5rs7QXpEWQPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : «آتش بس با جمهوری اسلامی پایان یافت. مقام‌های جمهوری اسلامی شرور، بیمار و فریبکار هستند.
آنها مشتی آشغال هستند.
به آنها یک هفته فرصت دادیم برای مراسم خاکسپاری، ولی در عوض دیروز به ۳ کشتی  حمله کردند.
آمریکا زیاد از حد وقت خود را با اینها تلف کرده است. اینها شبیه به یک غده سرطانی هستند. غده سرطانی را باید سریعا جراحی کرد و دور انداخت. »</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYmDlFzSMUtZ0q7VqtN6N5mBYphS1KvNml3y0nifqulPedH7OWT3-57OqYzNWzGCtoE41MKI2LYcf1LQOPyakg6becrFYCxE50rmMauT61TS5YY5wAV91umupGHJedo4qaEEiXfPn4QB8JTiSnA8QkOydoagX6jqHf8GHZN25aR9pA2XMphfDC10Z3Tdp7mMiVUWBV4ayu75MCaHhHVtNvqZV4aVrh0rkHWN376NvnGMg9ePR3VsESJ6FmNxSZsvHd9ZLtosgwxPWY8JzrrGpiW81M_V-TzXq2wbYIDgB2Lw25z3vAZRJiOteOjnFDat-Mmpia20wZg2nU_BiY6CgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugxyLkHE99GbQnZNozeHcp7xYvHTESmwybGjxccbbJ_dz5GlVuWLXgfZ3PMNXFlQJVn74zZZJUkQalicKsyuUuSOdO2gjcaz0lY6-KjCIL3TzKm8RWuaf2f8W68QF_n_iQx47UlgLh7fLj2pg6PiU7faIgU_6RKx2HdlROC11MtCeXHKS7jlP89yzefNfDe-fWl2b0OlE0RxUsudtvtFcw0bgG2H3gyhP8RVlr2ZueyQXd1EOhMxcSr1-Jk9jeQaYW9UZvjz1Oh5pPQv1NAJhQI32DuAB2HkarK4EhPL6ix29qu76vpkcZmC44uVmrpbgkmKPtK7Zs3RrK6QETupkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=QLDunqQ4ZqwYYd8wmFqcqKXx8CsM26_E-65mXDrsFxmKBByLWZ21GMcadzDGq3K2rLxxUEYwwKDOnxIte_Am5TwtnfzEsqDMUMDom6Nw6b7hitqnAFBao6n3Y2_I4ImU651pwJq4zRkH5mxxqyS3mIzQn49twQAVdnvnzu8xQ8T4eHtUx467jXISXei05hsJr2bvsf_q2LcxyM5_V6Clobk-HsRudgQ6amDhXgm5m8UQOFIC15tRNEQCaGQnk09yw9TvCTYfwLta39ZiGAtk_Y9NAubxPUVY4ljQ3Dd4KVDgmdLtytS89wnGXHpK1r2hSjb1hSYvnKInezjxFN9Uiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=QLDunqQ4ZqwYYd8wmFqcqKXx8CsM26_E-65mXDrsFxmKBByLWZ21GMcadzDGq3K2rLxxUEYwwKDOnxIte_Am5TwtnfzEsqDMUMDom6Nw6b7hitqnAFBao6n3Y2_I4ImU651pwJq4zRkH5mxxqyS3mIzQn49twQAVdnvnzu8xQ8T4eHtUx467jXISXei05hsJr2bvsf_q2LcxyM5_V6Clobk-HsRudgQ6amDhXgm5m8UQOFIC15tRNEQCaGQnk09yw9TvCTYfwLta39ZiGAtk_Y9NAubxPUVY4ljQ3Dd4KVDgmdLtytS89wnGXHpK1r2hSjb1hSYvnKInezjxFN9Uiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8W8G830dLJBdkC2DWMS29NjQRSVVZQNldvsOx8fUEjUHAMql2NWbz1QmiwPOU_xv4jvEDyu1-eduIjiJiroeZZH59YGtXQFe4skoUPhziRvV9GqRjnzuEH8REWwnshM5nM7h3zCTTDBLwNMh0ImhwCB3Eh9mNFKUsZoSrSdZIHVNVME0rJ6rD-rGaoQiRfxdq55lE2pnLNA_WjzX-PFFDlRFuy1ESuTaBY243y_PgUpWh2SmCN2TfrIlcQUrq4ZwuCkIrDL6roCNopuSDFrONA7MWgv4MVDvvbH3Js6mcPuSGGMHObZ_crhD-DsxqtzQDOMytA3FuXRZmHU8mGS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=s1evf6PPer1Z-bAKuAhuj1-gNO3cojh4zHbmkt7xJ2B8pl_aGShQ0sjhwGiPuTBXWE6EnDw-AouS50IULT4eq47ymKbIqi8kqXjI1QFkGWqLcmhuqBNDBVgWSxYPrmg8TcwZocQpaub1wtdl1p6PN0jzhw-ogngTnVepD9LqJxl7j4Pcifxkx_gQ-wCxJbRJ5oxnNla2TwRp3LQc2VmOQI0mj5c5YzLyi2nXI9GrI_E6UDt-b53UAG128VgfJOP61uT4BVqkYs8LVbDWe5QhwcqeAFG5fo1rCXOuD1GiHjG_GC1o2u-7H8lDgYNXYjFxRyqro52u_jkokLwsa6uL7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=s1evf6PPer1Z-bAKuAhuj1-gNO3cojh4zHbmkt7xJ2B8pl_aGShQ0sjhwGiPuTBXWE6EnDw-AouS50IULT4eq47ymKbIqi8kqXjI1QFkGWqLcmhuqBNDBVgWSxYPrmg8TcwZocQpaub1wtdl1p6PN0jzhw-ogngTnVepD9LqJxl7j4Pcifxkx_gQ-wCxJbRJ5oxnNla2TwRp3LQc2VmOQI0mj5c5YzLyi2nXI9GrI_E6UDt-b53UAG128VgfJOP61uT4BVqkYs8LVbDWe5QhwcqeAFG5fo1rCXOuD1GiHjG_GC1o2u-7H8lDgYNXYjFxRyqro52u_jkokLwsa6uL7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7aB9Ms9FFNkx4e46q9L7qbe-T97hxiUgzJ8Qwew8FqJBAra6qLp8v2fciy2wSkY1yIOsLqFtMO_hwDwu-e4_OmW9S62LqT4ssEQapmYUVXvmf2W6YZ4fWBKGOjBCvUs1xR1Ri36PPzBZThQZ-SX3TXTSJ9vd3Hg65Ge53ffZPoIX8pit2VadSwa_smc9syqdU-OPIuJG7rA4t0gKdMKJuMJ2QwOy7zYShuvQ91E7e_4R7nYMy_SGgt4dh0gkOurVTXHe6QkPEfsRDDBDBXf6s0EEw01lGjaW3G9YigLwDEhgNW7NITFlVD4yz13Wz2Y9eWlB1aW0OIYU_8Z6aSYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hfh2q4DOURgAPaDavfGLtcQ-tbcsH3jxVWLDpBx7dNrrEf9mNU8ICbfumKZVMpXA55lCa0zE_hUx7KjU701pmJusp0-Yfe4RgPBOO38vDeQDochmdMwPBmOKtPMj9ZvtuOvgK2_jV_QhMuc5499Je5FLhfc9RN9cDw6uZVwiNh4fxH_M72lvc8xA8Nn1Vv5-IJ7Cr8va0BMFJnuoqBCGIbbhIE8vdZR_k2QIZVfO8E58-ZKSrIrGbxPKVGAzNxgbKFEVt8wC4okTS4wGGy-B9xl8M0e34wj9Y6Ng0JB4sjrVExLgdgkCmwG8ii4WudUH7PksMHxNiGcxSrWTabyYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=qVxitjWQ0KzaeVqRbTtMNHQ8rnIYGtit7s6OMb5ApHsOI9Hb_AialreRC99YcocUxiAljum1E3hMUlJkcy1mHmT2Giq7CK3kJQlHkc7Ncj3_f2PBTja1uwJ4CV8wlSa7QxuT29YWhJGyFjtTc_Z4kRQtkzLJwPiARtq3kcrkCdKBjrqIN2nQ25LlEreRDo6WsrnmnbmOn_OPOqp2bnI9_uy3YuENRTiaTk2CMahvSma4HGz44cNBwP13tcDKo2D18qp5PfXnaqMIOmZOcQwKNOclH1rqBf3ldtIHRxbgAGKYVWJNi91sF5sf_lLFPSrzK0g9MAJR0nKIONId2pwe-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=qVxitjWQ0KzaeVqRbTtMNHQ8rnIYGtit7s6OMb5ApHsOI9Hb_AialreRC99YcocUxiAljum1E3hMUlJkcy1mHmT2Giq7CK3kJQlHkc7Ncj3_f2PBTja1uwJ4CV8wlSa7QxuT29YWhJGyFjtTc_Z4kRQtkzLJwPiARtq3kcrkCdKBjrqIN2nQ25LlEreRDo6WsrnmnbmOn_OPOqp2bnI9_uy3YuENRTiaTk2CMahvSma4HGz44cNBwP13tcDKo2D18qp5PfXnaqMIOmZOcQwKNOclH1rqBf3ldtIHRxbgAGKYVWJNi91sF5sf_lLFPSrzK0g9MAJR0nKIONId2pwe-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5914">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فرهمند عليپور Farahmand Alipour
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/farahmand_alipour/5914" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)
دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIDoEo7gzcbtBxG6_iikJ-FFvx9OmHTj_pSqQSvUhx3YjHMeksHamc_u10b3WK1ijpkbKUb_9y7dhxanIM3ZQwuXYVC8wzfldqmpd9fRFwSpvvbO6uVwnqxpAOAt0O1zt4LyP-YIyTg_yYo7C57P_urncGQgxr0tg0eYz5z6BKnsPE6SrFotBxqN9MKBcCQI_WumhUMmJNSjBYE5CPv9agqTHzYL_NS3ZiK0zV8lOhgg_qeRVqObwsgWyU5X8BQjQG6QJ9v5o9mQsPd7pr6BDhRRkTuZ64clTwl1Taox92nfawjauA1YHB_yPjTlOev8cGw_h47T9JEhKLJUnRW77w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEWL6gxDcIwbNtzfeImNapUuBLljpBnjG-G6PODdViwAEid0vtHII9kMELXD9otnMU82pmtUKcx3DKCUrLcLypNc8X931OkjFGQpfHuwNvST5Q7jdR-Q-xWoM3Tc_Z2NONKMDrVTxsKEq_UEMKYHfB3C9uYLPgkKIDBPYh-tb6D9lPPJJwflmVQcJcXheJ-5bQHhMeAlMIuH5OzFXXJlCWwPs6KToB1e3A0EBs4uL5iqMvnqq00Kx8TDVLUPjkp1pxUwdrXmukPY6xPfiKgB5vk-tkXDhGUzlvZWRYtrAr1E2D4OrhOrFWwBK70PmUQC7S9dvbx0YWQ6v_uNvYzm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSOoA_tJK4sq0wW_ro8bjc8OrioF_QrwE_5rJKQlL8f4axWx2fgP4-uMCaLDpoAOVjYgqhV74KhBJmb1jbLUiBam2zI0JbHmuaiDPS41NeCj5t81eb419gikDhU69qMlsxp2eyyBBrqfFT0c85kHYu8-HY2Ye4LcNuAUWoZ_SN6sEZ3M1KoYPzQug7PFBWUv1uo3IADKdyeuocs3XVwubcpK9_XdjdSkWjDjLiMZHkAQpx2WRQFBxUuc0pVBcT-sNfd9qs-2EnI6sQAa4_BuJq4extwCN9bm7DLntfTYHOwgHtmXxJHiBSYdw2FefYfvXWvtuC5bqZwE1unW93ku-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5DS1M_knCBsRwOEbmd7NX8oMguiTdIh7yu-HeEEusEZZfcbo7UEO0TW6Aih8Mq9HW6zDUTqNxB8TJ3TppGf51NeooYJl5p7ywEUTj0lOWW2ZN7h94icuPmn32sZns83ldbTNdBOzRDulPxTQfSdGZJUmPmpusZMlo9IaYDOyr_5WxYusAuVY2-b2NbWBSjdCOIpoaPsRIitHiOkofLdAjOYxiPxG7alf338FBdAwmR4KLqWLNT9Bcg-Orm_-FLS-1cnzLe6L0-cTn7ixa3KgopZGEQYOumBYBEmWh_psEgQ4o2Gwc9pNrCLFwAtlRPFZU70pvh7bJDJhLfZwrIlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LERyCq5lUmA21UTlEXAJVt6eq6FL8A89NBMTzWto0hYba18Tgs0Cy7lkdExmSaTX79jqFCX719mZdJ6zpBdsTPp4nyijXC2rsKVGMFciLDbXgPCG3Qbj2Hrtxk-7N4AN_UXs67C8fSx3TVxUeZRzHL49Ew7A29ItDqKovdzWDycPd65p05ehcXNtyyFXax8VGn61JZA0ClWIiugVwA4w1anXT3Law0IVcf6YqGF20IkKBJKQbYsd066ANMlHhDeyLaqRyHfzPvk41fKRrF_1dpV5Dt4lofy58LsqhFUmW7q7oS7cSkpLHgnC0wNLIxxtMat3LTs_Oug8XyUVnfKq6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9MstWK45w7GXgQZgGPccDKlcJSbKSfaABE66PNNHottUMISzzAPh_PChL8HTCeo9sv59qm9Zej9no4cG7KVgQGVemqb26gdNHwSgTrSnRSPd5qVuO-9OEXc05J8mWQgyeaD91KJFyEEbFuHSKZa-FJjOvIBwAfiksSJXuf5QkscgaWAexPEvtjPZ0I7ahvnr4QJeRdaXVCGmhhEkAWwAPNAuRYtx8UH9QSegsEjQINQOfTOjq0gTN7sssxsmg92CtcAU96_TCBe-9sX9bn-ebzZyOeE7abB59GYEgRyheD2ZIX6hgl-z-LzYm_OUf0C-LVmSlnI2BlOxMUbfVOtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=gW-JjedtVPnmsUkxa9xKdfHW1NfXGUsk03HTjzTUfTYXrG2HwsT5L6Dx4LEJ2XlMw32IbJx1mLV-vBEHSYXvXU2sVB7dxohNsYtAO-niA0Fp5tenhQ_RWhL-9L3J0f5MbPE3ep6oIhWeA6aT0Uab31yrX0pGyDqC79SdsN50r2vw2GMLNHUtbjd1Unm4Myhdqv2DMGm5OyCYSzNKxodRHNs4lLHR2grxaPjkHeCXwR5kN5YbxI0EiFJAXtIeak4t4cYdtbYzc-fEmT-TS_WH-h4JNz4d5s4YV26ifyiN8KzfkRGq85LG4cpQHd9I7uv2d49jH1n--VSoswOYoIbx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=gW-JjedtVPnmsUkxa9xKdfHW1NfXGUsk03HTjzTUfTYXrG2HwsT5L6Dx4LEJ2XlMw32IbJx1mLV-vBEHSYXvXU2sVB7dxohNsYtAO-niA0Fp5tenhQ_RWhL-9L3J0f5MbPE3ep6oIhWeA6aT0Uab31yrX0pGyDqC79SdsN50r2vw2GMLNHUtbjd1Unm4Myhdqv2DMGm5OyCYSzNKxodRHNs4lLHR2grxaPjkHeCXwR5kN5YbxI0EiFJAXtIeak4t4cYdtbYzc-fEmT-TS_WH-h4JNz4d5s4YV26ifyiN8KzfkRGq85LG4cpQHd9I7uv2d49jH1n--VSoswOYoIbx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB5U9d-mRJnKPoe8p8Sk14ls6XBxKmo9AlTsEmDbHPYY56V2Ev38NH65ByIYtW4CLPeRtlT99gaoiH9-M7a7gzsjROrbqC8athgVudIvt10GzeIy8f7UcO52ESo12K1ryBYFKqaPTyhlSzsg6EG1kroiC46UU61SSxeKJZN7sBta5kgCXZmmFbo-SdhlsVXW5sRY2_SJtuNwmOnGUGqShDpLs9o8IAtZkA72GyvIU92QoneLJRUWqyigztViFKpI9W9-n3pam8f4PVvto4tu4qN8yI4ZvheSIoMYt1cUhW36WPCZbpJPaBT6d5M9kdZQpUck-wLXKqSe6FLSEzwe0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=fBIWOvrrOsQdsnKJ9bhWGIW-1eu0mO0tWihxj2Vm4MQ1f7w4NBPMS6Hyz1PdhxYbE4jQI3Wz-t-9Q34cg2c3PgiZbgmcr7n0Moig6jjnOJ69Xh_zrsvs7ZstkMH7eJMmv3U_kGCSBWOt87CTGJ3Rybo4m6UoJYAiSFVI5OBTLcvDgMRIsXV6NwBzRgUpuXX9qK4mnS6p6Nm3KKli6q4-OK-Ysu0XCFM_6k4vofEydLBg6aaQw8Y9tqjGCfDaOp5acoAa7qjYxuq2vwGHizWlxfXTQWML-O9YBorkGPIYPuDU5TaAUmWlzJOI_Esnq907GBmEcOSq6efOL3B2VQ-4lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=fBIWOvrrOsQdsnKJ9bhWGIW-1eu0mO0tWihxj2Vm4MQ1f7w4NBPMS6Hyz1PdhxYbE4jQI3Wz-t-9Q34cg2c3PgiZbgmcr7n0Moig6jjnOJ69Xh_zrsvs7ZstkMH7eJMmv3U_kGCSBWOt87CTGJ3Rybo4m6UoJYAiSFVI5OBTLcvDgMRIsXV6NwBzRgUpuXX9qK4mnS6p6Nm3KKli6q4-OK-Ysu0XCFM_6k4vofEydLBg6aaQw8Y9tqjGCfDaOp5acoAa7qjYxuq2vwGHizWlxfXTQWML-O9YBorkGPIYPuDU5TaAUmWlzJOI_Esnq907GBmEcOSq6efOL3B2VQ-4lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=XY-Ueg1-cYgnuSvgV6YOAsK8Eyb2Grq5Uh6nBOR7oFwR9z9x3bj4zYSvXtlHY58udjD9BdN6H5K7YZl95bK4gPECckbWWLSYkeG8NyuUlP71QCUqB1ZGR5I5HTdUEhZ1ZnJ40fo3NiIxRVvKKf67tLo1-90CeVp5JH9_MXD06uFurukb1XY4zLx6ZTQaS1f4dnFeXpW7RAyaL77UgqTqJZpdr67gumNE28oQi50_6anFzb4z8WhIaSPGM2bS2JayspFftQKObXakKq1utm-eciLCVNPOmAGJYUNCvY-5XGwgo-KOqhqiibxcwbWg6r21dCMpZOF31gfdpXCnya0_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=XY-Ueg1-cYgnuSvgV6YOAsK8Eyb2Grq5Uh6nBOR7oFwR9z9x3bj4zYSvXtlHY58udjD9BdN6H5K7YZl95bK4gPECckbWWLSYkeG8NyuUlP71QCUqB1ZGR5I5HTdUEhZ1ZnJ40fo3NiIxRVvKKf67tLo1-90CeVp5JH9_MXD06uFurukb1XY4zLx6ZTQaS1f4dnFeXpW7RAyaL77UgqTqJZpdr67gumNE28oQi50_6anFzb4z8WhIaSPGM2bS2JayspFftQKObXakKq1utm-eciLCVNPOmAGJYUNCvY-5XGwgo-KOqhqiibxcwbWg6r21dCMpZOF31gfdpXCnya0_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaztX_BuvAeWlm4NNvtLj78kfeQa4pPhAPhJxpG7ckdHVX7dEZQID7-WuqJYoVVZn9AN9EEI13nsg1yCuEk9LuScSLc77Ai0sQrPYqbA9lyvBzO00mfyGXR2a_h4rC8sC7t8sm8Q-WsnNcdcdV6MzUIxU38rvB7KB2p81UgcswZgvOHIVIQrE1AW-XvEhAdgQ2VTPq1-8gqgpCZ_OPdN1qLi8znakLbEe4_Tv20O7hSnPiRZast-jk8FIaTV4zn6CMnbrryDOh7GzpJjaTMEWYOsvxV6vyqEbigg0s4RtsvzPutCVZb65wlJoAWS1QrKDpX_nEw42e9gam3-_Lsy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=YexksrF5YY6VJB8hJ6xYF1Enc0YvOgd2tz29gQ9p2nnzIa2VYg6q8_HuuuQ-kquuzIR5H0XfcShSmEunrDjcOrpoZLiWP9KOKd6gnhKXfCuBaSOF5Yc5fMzPPyOv-AFLZvBxuCichFozu44XFNTVKxSx0a1V0cR7j9jCFs2HU3FaqTefic6V1662Q1yWBzNtut1liPwiA5JEP9erUcr69CCFaoISmTaUspZaxcfYm29zR79Gk13j3dfvtKWUWKJIuNSfNXl8jt0bMFVxsvBcdPFY4mzrYj13qaPoAp4yggYtDquAAxCQMA1lpZwLeucyfBZKtjOm0PK5xK4ZRY69Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=YexksrF5YY6VJB8hJ6xYF1Enc0YvOgd2tz29gQ9p2nnzIa2VYg6q8_HuuuQ-kquuzIR5H0XfcShSmEunrDjcOrpoZLiWP9KOKd6gnhKXfCuBaSOF5Yc5fMzPPyOv-AFLZvBxuCichFozu44XFNTVKxSx0a1V0cR7j9jCFs2HU3FaqTefic6V1662Q1yWBzNtut1liPwiA5JEP9erUcr69CCFaoISmTaUspZaxcfYm29zR79Gk13j3dfvtKWUWKJIuNSfNXl8jt0bMFVxsvBcdPFY4mzrYj13qaPoAp4yggYtDquAAxCQMA1lpZwLeucyfBZKtjOm0PK5xK4ZRY69Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHndmPhGt7xunLpztZ6Pf2U0SV3iK8arBtKfU_1MPk_a2vqp_xFRiCBNvB-WVhLcYM7Ka_ktvTy4AoQ20afKqtfLlbme2yR9klu1g3v8qap8QzE9Qt78p-4dRUSkb_VEc55hnRutWVI8Hhde2w_9qNFYkEU0XFDqRUiNoBmn4h6g1OnpgIDOkdCpdOh8RGSZJSh1THLKAtGcvsWer33N_-Btgp3FyJOOLR5_g2OgM7WE7zMnpmSAmGmv23fQ2CtHEfXuE7mnAxlv6_2ZYscgc1k6ho_RCLR6JGgpumj0a25KmA40lAAmLeg76ok09uZ5Kv3PfDNAmfWPSwyAJWCoTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fasI4_zOccDt-OzO6UbP8-kFbsJhx66H26bD6d4r1j_9YPv4v_MLoWu7Eri7Hozt8iu2FQ3Y8vYcUA_2ncvpJJO22E-2FHmy-qycnXC-BwlVa7_zQllodpjCt28ULacsmcRKvPIrWH0IqD4XW5ZReA6P5iTADV_0BtG9V68LP4hs2HzDMQfTkSCFEAMWdrIMC9ZqNaCZzJ83PYjhuP9R6HlrqX6y6iwPo0j9jlhEcGzN0zLv8CYw-PCa294KHm8COmWI54C_dvXVZYYGlCTPZndknI76N5iMqZjMWI13QTbYazg8YAIjURsKQoSF9Z0MXSwjaGC_zJBgymiitEGLxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqvjOL6GlVCJw0Qun5JFGKUJZXiryPfUxth0wTwc-que0sJylyh0TmbN_w3BfepNgPe_HHGbDUwcGjptu-eTXnb6CDuOAlanJASaDVFXITk9YyG-LFS2iRXb_gIxLGDtJf1XA4pqQi1jCg6s2S7tkTA0MNjfdLtuI6efajWJNLKYo7lXxg-azYlixs8jRfC6Q1f8HkcJWoMYgtdipa6ZfVv63QcjyZWOcwHmQ--cxDaCP9ZgyGdXKd9kxvEACLl2gJUK6SRYTxb1JZ7HIUgBwZmYlbimhc612_l9UVPlsszNeRkceZvgtfjACjBntM9vpdkdMqyiaz1-RrEiOeXtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXVHomcsX3TzRYGSKx8ll_9FjFJ8tNEpLNLzt7Dqw2BIswcONd-5tcnXUByh3cCo98-4z1UzPvyH8zavs-bwiRAy6T9C9D4rn8vAmZVwM4c97EcpPH60Jh0NAn-mDWs0dMZ_rKbKzuxXD3gaOaIBKU1JFG1Mxz-OGXMyYC7xgP9-L2ixgFIRTXBCeXsU_1kN0bOKVXxWLM8tuxpkMXVqyLXlHWzYqHPY_Udjg3yJab3qLLQ29B_QOQ08p9ioc2Lu0e587_WR8KLlCA6vLn8SwhFYdr0NDXySy86_W1s8HxZ-JWN6vNOFfA6estPtuG4Er0tittvLi1MV_4kPM1opng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWgfX6vSBpC3Tg8TsOeQ41UccGpSLyNJzVxgshCKPhRn2bWDrInqzcawher7UV5HHIhkcCcZcE7jFXC9xalbCH6up_CFxgQEmFpJqe-V9_1QtqKDKmo1wwsnjuj2l53KSaQRkzFL2iI3plgDM_wQT_7FdVh8lLjAofGB9hT2WIg3v1N1oPnFNLiGK9eKLuTb2Z6tuWGEaE_qWpe4puR2R9iZNvcCeLHydNnbfcA1QFWTL5QqYq0L35yJBRAQe6vT6_0VmyB3BZifO5NFepzj_tuRbLKEFvprmo1fUucNw6zh-g9_QT93bWDYuzEkse4hmEJ1bmyGuIQMEAeMLSrtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fznowDSr_QQ_WzCn2jq0W61yNMwJRPrjpYMoKqqR9IFkhg_e1Z8HK-M1IC5eEmPB8cMMP_AzraTBXYmbY3GDyseZJYa6Dc30-HgWuw2xqRzTPFkbo9xK-8ZzaIuoJw9uf1SFdzgB4OCDvYz-PPFe2SXU8vNu5o8FTs10L1yMhvPM-IMakKnRbwfuwDBDDJExFM4-tEFurXie2OwkDP_7JJuVnMNu6FDtmfn48M-ZnendMXqdPMTvA5ZBS-5y68d1owNhj21Wwqq75M7ox9dv6f9Nn6EmPnMCxa6q7myt354oUHpUy7Lp-XnAXqD6lOB7gOeoTktBa8-rnqT17CbpHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=S4ArNLxGPQUEGcvM4IskP3z3OvP2EHCCSpW2e5M5VK3kV16TY2gjUVq6pS1iOC7GGTdiodc0mbu6-DiuWZ-M8PN5j_GJbWtyx7FHbMuLIEnsg3KVSmBUiGmAfg9S-y_bAN1XqczRyozYlBEoJA0NKql--BnyoC65eI-g9DH6uWkyJKWboH6EkukzMFF--dAz4wkwN1ufu_SmNPiosO0ucv7F7kfLfj8yfpLdyf0BWq20-UR9YdlwcBnOjdTJqk76iY07fMQV834cHLe2l09oUi95-gplfP_0R0-4PZV0eK3gSs8xw_MX-2PQAhVlDM1c5blLRr-atFEs1O4mEP1Rsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=S4ArNLxGPQUEGcvM4IskP3z3OvP2EHCCSpW2e5M5VK3kV16TY2gjUVq6pS1iOC7GGTdiodc0mbu6-DiuWZ-M8PN5j_GJbWtyx7FHbMuLIEnsg3KVSmBUiGmAfg9S-y_bAN1XqczRyozYlBEoJA0NKql--BnyoC65eI-g9DH6uWkyJKWboH6EkukzMFF--dAz4wkwN1ufu_SmNPiosO0ucv7F7kfLfj8yfpLdyf0BWq20-UR9YdlwcBnOjdTJqk76iY07fMQV834cHLe2l09oUi95-gplfP_0R0-4PZV0eK3gSs8xw_MX-2PQAhVlDM1c5blLRr-atFEs1O4mEP1Rsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=FiDyRORLn1KCRdwjHR1638hwboNfnNqAa2HqvqE0ijMpXPoARITtig84fB_MpoIJDbzZp79IsS95VDe9M0MOhlMETHeZUFWCBJURSHKap2slIprMeNWEatmPPjBV7AtuJ8JU0X13Bl05DAcXM6_8VpnjPRk7yshWbG450Thbze2iJ9BV7OvRGsi7-2fS7C9DYQRoSNlVGObR1_kpscvOlLKOv8GYMppkz0oFGYkTKGhNOHD7UCMdzyfsAuX9ro3aBtARQ5rUZY9QDiZXxtYVKPAg7Ofw-Veb2jXmEUy4YEjoGOD9bVxmBRqK85eVJYGfAEYhtimrj9so8Me16HiHTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=FiDyRORLn1KCRdwjHR1638hwboNfnNqAa2HqvqE0ijMpXPoARITtig84fB_MpoIJDbzZp79IsS95VDe9M0MOhlMETHeZUFWCBJURSHKap2slIprMeNWEatmPPjBV7AtuJ8JU0X13Bl05DAcXM6_8VpnjPRk7yshWbG450Thbze2iJ9BV7OvRGsi7-2fS7C9DYQRoSNlVGObR1_kpscvOlLKOv8GYMppkz0oFGYkTKGhNOHD7UCMdzyfsAuX9ro3aBtARQ5rUZY9QDiZXxtYVKPAg7Ofw-Veb2jXmEUy4YEjoGOD9bVxmBRqK85eVJYGfAEYhtimrj9so8Me16HiHTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=J72lebi-j3XV7zZ4AqNhlOwE4kOvWG5OGHzUbzkItr4LT38pxv2UAfDwFpDmh44t7mDKK9y1fkixPSDU2m6H-i_bsxtIhcsgj6g-wd6JrB6k7dVVyaHDVxDsmRvKGzfZ0CSL6TC8_fhlxPHXcd_CVKxySd01h_FnRQriQB8NAutWDnHmLbSCN0DUbMAbNnQ8lhGy22Mn4EhcbTz8eprsUcNtxqcO-QFp6pAxdINORPlAx54oYRPPJKSWlnSPC8z5_7LOfFYf8rDiH1mH8-25Iaxzdir7MwiS62iMToGedHrFAgfhGA_-J3tz2OhYDtIvSeZfQDIFjhatZtnpFVUiNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=J72lebi-j3XV7zZ4AqNhlOwE4kOvWG5OGHzUbzkItr4LT38pxv2UAfDwFpDmh44t7mDKK9y1fkixPSDU2m6H-i_bsxtIhcsgj6g-wd6JrB6k7dVVyaHDVxDsmRvKGzfZ0CSL6TC8_fhlxPHXcd_CVKxySd01h_FnRQriQB8NAutWDnHmLbSCN0DUbMAbNnQ8lhGy22Mn4EhcbTz8eprsUcNtxqcO-QFp6pAxdINORPlAx54oYRPPJKSWlnSPC8z5_7LOfFYf8rDiH1mH8-25Iaxzdir7MwiS62iMToGedHrFAgfhGA_-J3tz2OhYDtIvSeZfQDIFjhatZtnpFVUiNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=q_IMbqVHRGKEkINjw7zz-xmyeXj_uznDnKUWDVwHqmzTgTcNCryGOyXmyThQfZvtXHaAFMdZDuC2V2XzbPQJVhCZ56vtYuq3VBV_KaOTQY1hrOTVb9KeqBJOuGcAZ3-s53ESulStrCP1sVaBSx4bxkN0pDAf3qMHg3EqHjOtI-J7bNEWsJLS1Y00KKEU1CpEr4SqMdkgHopRrISMyD2bHaxlMYRNfnDMyeW8ksSYicG_kaXyRs6c9QRRvzGLrVmee0_GMJ2foP-sq_zfcz7POI3ppXJYzzrfdSUX-v2snYrBb0CwCXVTDQeKQyKAEq9-FMpXufLo8F8rO4aZP595Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=q_IMbqVHRGKEkINjw7zz-xmyeXj_uznDnKUWDVwHqmzTgTcNCryGOyXmyThQfZvtXHaAFMdZDuC2V2XzbPQJVhCZ56vtYuq3VBV_KaOTQY1hrOTVb9KeqBJOuGcAZ3-s53ESulStrCP1sVaBSx4bxkN0pDAf3qMHg3EqHjOtI-J7bNEWsJLS1Y00KKEU1CpEr4SqMdkgHopRrISMyD2bHaxlMYRNfnDMyeW8ksSYicG_kaXyRs6c9QRRvzGLrVmee0_GMJ2foP-sq_zfcz7POI3ppXJYzzrfdSUX-v2snYrBb0CwCXVTDQeKQyKAEq9-FMpXufLo8F8rO4aZP595Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0HPmcIjFJpuwCH2jRWFC7caVhT1W9JNGugxjaSYySfq1BMyieq-m3NU6kjKHRYRbPd1nde7QQF2RMHaOsdP4Fwjo2gkOThsjn9DvrB_CW3PuxG4-0muF6UHX9P4uZrqWLyv_-vjVduUKPyDBlY5gCR8LEOdkluv-iRVNHZp5ytLQEcokJD68EU82o5VecykZ0VghyGKyuuum1VHlWno2HjQEtchKgsXAnAzenA-kyiDPIBN1dHF3OeJdyOznfVQantx_Nod57gsJv3A2VwdxLm-hxErG2OWYxc0z0Qehe4iV6jtHEfG-wjHivFADS74El5-_JE93FOed2H8T7yyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=U7wAb2Dg6I9X87ntwiCv3_3MvWkJyyd4ZvMnFVThhKqrkmjMP3Gq3p0ThHdTbmBjjHQ-qph5yFZqy7uA0izmI7gtHMaUyBWj5lJ53q4og3qDp0cra-fxqUK7DuSiOPs8EDlCfqqBmK1lE4JC8bLSYPCHyd9s-Gw8vJQrNUn8mC4rU7iKjxcl_8gs_YTE6ZbtIW_yNfBPwAcDzFG6pbcZcF9VxTG4f9ATAO0RJ671NKesArpg1dcKmB28yrA92tXZmnGmX4y5mgHgxzEatujFDi26WgeuGMCgRXHa7OJny1LLQfojO8eauNOtXVZ_bPdggblvLzlnY3kSrJ5tCvFywA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=U7wAb2Dg6I9X87ntwiCv3_3MvWkJyyd4ZvMnFVThhKqrkmjMP3Gq3p0ThHdTbmBjjHQ-qph5yFZqy7uA0izmI7gtHMaUyBWj5lJ53q4og3qDp0cra-fxqUK7DuSiOPs8EDlCfqqBmK1lE4JC8bLSYPCHyd9s-Gw8vJQrNUn8mC4rU7iKjxcl_8gs_YTE6ZbtIW_yNfBPwAcDzFG6pbcZcF9VxTG4f9ATAO0RJ671NKesArpg1dcKmB28yrA92tXZmnGmX4y5mgHgxzEatujFDi26WgeuGMCgRXHa7OJny1LLQfojO8eauNOtXVZ_bPdggblvLzlnY3kSrJ5tCvFywA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBD3V_yqMwiOgyh6802eAR6vC9oebI_sk9SDDx49yxMs4l5qyBcszRRFYptDBdzRTmLyfetUamzUmJCPJuKrHgVJCFbSgB54vuWSRZLK4_U8N67n2O5HumAFKnjSVpiU2Y2jw-yD0gXI6aJDhZ6zWOHGcmljRDg_CryJZhbn-GC32U3MCLRmcYwEMKo_E5AswiLI5PQHN1-lRludHiK9m_PVTY2j1KSqjjcZYYNcyDBVirHpXsX43f4owigo72NZADveG6QmCrTBVv0BYF4vejTczoP_IfowEHXaIlDyWk1QiIYNkgm9mnKBFj1sYRx9OOBgd0YNY5qhD48N3JVmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=FuGbxNgrtensosb8lLRi65PH3r1rI4f2hXB-o1K3XMycWED7791BofxGqoovABq3L-t4KrW2slD58heKEXCjow6PtA-mR63gAkYrEiQNv-2dXLOqnkLJcgNPmD5Lbf-RzUfxfLA4s9mEZifvR7ONbVBoNfGo3DPrdfMwA1GjuP9jH5GY0OWpfFmcIHrBRxt7nqVRWhTcjLkMJ3fQEE_9EmucOcgamoSO8neR31R-ry3_57ajy_-POQyDDEyVLDWzuy-8GGYmITi3HJ9zjZu6pKcL2KjM1a63-fSgvoiUm8QRkba-DLlpQpKyIwtahikzoDnEJUFsGsMfhzdtoxEs_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=FuGbxNgrtensosb8lLRi65PH3r1rI4f2hXB-o1K3XMycWED7791BofxGqoovABq3L-t4KrW2slD58heKEXCjow6PtA-mR63gAkYrEiQNv-2dXLOqnkLJcgNPmD5Lbf-RzUfxfLA4s9mEZifvR7ONbVBoNfGo3DPrdfMwA1GjuP9jH5GY0OWpfFmcIHrBRxt7nqVRWhTcjLkMJ3fQEE_9EmucOcgamoSO8neR31R-ry3_57ajy_-POQyDDEyVLDWzuy-8GGYmITi3HJ9zjZu6pKcL2KjM1a63-fSgvoiUm8QRkba-DLlpQpKyIwtahikzoDnEJUFsGsMfhzdtoxEs_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=F0AdnUBpB3K1osLjxoUkvDjp93auSi0R8VznbFNcrqz0TqKRtADge04m1NjIbA4Lmt6TZ1xdkZTQo6ylZLuSPlO9sa6NnQdBNr_YurG0tZOBy3yYaOFtjxo8v6s3nCeMC4wFx4-skKVdltpeV7_jOpmsLuIHJHkDh5sknmbs9cCk6NQN8udoiKvg1rZafATosAbwZCdQwMjc0eVVcRGID-7-UZZyWt6n2rOyKih3WgxZlaYEZpEDDqZEdg_prcd8N-manDO4Wq3RkZKPYybta_XoPkdq_7GiQShPVVNSKluhoRojDBPVfKashsHLVdjUli0zFQPV3upXX6F-BHNXhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=F0AdnUBpB3K1osLjxoUkvDjp93auSi0R8VznbFNcrqz0TqKRtADge04m1NjIbA4Lmt6TZ1xdkZTQo6ylZLuSPlO9sa6NnQdBNr_YurG0tZOBy3yYaOFtjxo8v6s3nCeMC4wFx4-skKVdltpeV7_jOpmsLuIHJHkDh5sknmbs9cCk6NQN8udoiKvg1rZafATosAbwZCdQwMjc0eVVcRGID-7-UZZyWt6n2rOyKih3WgxZlaYEZpEDDqZEdg_prcd8N-manDO4Wq3RkZKPYybta_XoPkdq_7GiQShPVVNSKluhoRojDBPVfKashsHLVdjUli0zFQPV3upXX6F-BHNXhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=Nir478SyLYQjh9DnwSrCRjWUF_csnQhQ0XODtN_xO1pGXCYFicilgWQsmRO0FcHjUURM5FSSl80rBjh-KuNv1oJkN1cXwf-7KNObSNby0zhwmkVqqv6OLylA7PXHHxmT3o9YAZFU7g2v85Rxcdyb1doTA8oy0BjhjBhBp7WUrIUoFaSka3TAfEXHhq19OkSH1Si6vsK_3rG5hST6914v-jpWGv4rxH9bhApAVDbhH6Q6qkw71c3I9tdq_C6pDyw1-5g-gK_d75XlERBTyt-37EyMPPQScIOYaXTRXVZqUPZkIKRrjWQs3CenzX5Pz1tMWnc1g3vvf8VDwJnlf_8a6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=Nir478SyLYQjh9DnwSrCRjWUF_csnQhQ0XODtN_xO1pGXCYFicilgWQsmRO0FcHjUURM5FSSl80rBjh-KuNv1oJkN1cXwf-7KNObSNby0zhwmkVqqv6OLylA7PXHHxmT3o9YAZFU7g2v85Rxcdyb1doTA8oy0BjhjBhBp7WUrIUoFaSka3TAfEXHhq19OkSH1Si6vsK_3rG5hST6914v-jpWGv4rxH9bhApAVDbhH6Q6qkw71c3I9tdq_C6pDyw1-5g-gK_d75XlERBTyt-37EyMPPQScIOYaXTRXVZqUPZkIKRrjWQs3CenzX5Pz1tMWnc1g3vvf8VDwJnlf_8a6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=usjxnT6gGAMQnircQAsEmVuys9wAcQB9PsLbO_YyhOTBgyT4p3bmDjvE_Izz81slkSV8o8MAO7Ij1GqoBT9t9rUPJioZRBC1oXjn4y5ObHc_MpH0bFabe_XgBiPEnhG3I4pGEbXwsa_ibVGMQz_XXv5e-1FscA1HA1P4Rvy-FoUTtgIdnWjzdam4v0v-MMkpY1C74xVuvYqJvjJgbSRaMRSlTXpzswizIgxkK0Z_ebNNEgfvuBJLVV3JfDPeeyJvYsvehVcKwD-5yk6WXShlzkjyFt4ULZvxjpm1OMSfv2TS9tHyiX9dJCzAz2sRory_FjOMa4SKoiqMzZ1lko4iQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=usjxnT6gGAMQnircQAsEmVuys9wAcQB9PsLbO_YyhOTBgyT4p3bmDjvE_Izz81slkSV8o8MAO7Ij1GqoBT9t9rUPJioZRBC1oXjn4y5ObHc_MpH0bFabe_XgBiPEnhG3I4pGEbXwsa_ibVGMQz_XXv5e-1FscA1HA1P4Rvy-FoUTtgIdnWjzdam4v0v-MMkpY1C74xVuvYqJvjJgbSRaMRSlTXpzswizIgxkK0Z_ebNNEgfvuBJLVV3JfDPeeyJvYsvehVcKwD-5yk6WXShlzkjyFt4ULZvxjpm1OMSfv2TS9tHyiX9dJCzAz2sRory_FjOMa4SKoiqMzZ1lko4iQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=qQA7ZjslkhREf-TXiItr3JFiGzp8ykfov2Whtib2k-Dg2lY1Q_LwADXDWHK79iqObnM1ucGZWhtv2cYsoWhVTuMdLNSdpE9-VFTPYvNWJCb-5X8VnpkAQfQ7EQI3IusVLE8JI2SIafqRBXx30DCRGG-fXK9cURxddIOZpQ37mTsHEyLCRxrHvpm-5eyYJUlY_owazYqVb8cvDTH6DBoPPktnkB6FRpqknDSIng03S1gMMBNa9RVkV-cPBFSLKWtRgjT3LHA4JsrrIbVTyeWeGMtFeySdcVBcpWT8CyPfr-8DXgPYXMbUggBfRcISTEOBEEhxaMC1GLF9RQZabJcx1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=qQA7ZjslkhREf-TXiItr3JFiGzp8ykfov2Whtib2k-Dg2lY1Q_LwADXDWHK79iqObnM1ucGZWhtv2cYsoWhVTuMdLNSdpE9-VFTPYvNWJCb-5X8VnpkAQfQ7EQI3IusVLE8JI2SIafqRBXx30DCRGG-fXK9cURxddIOZpQ37mTsHEyLCRxrHvpm-5eyYJUlY_owazYqVb8cvDTH6DBoPPktnkB6FRpqknDSIng03S1gMMBNa9RVkV-cPBFSLKWtRgjT3LHA4JsrrIbVTyeWeGMtFeySdcVBcpWT8CyPfr-8DXgPYXMbUggBfRcISTEOBEEhxaMC1GLF9RQZabJcx1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=CzSHZqpX7iYUXh-MqN3R7VkyIcoXu65vhtBakrL9N2atNGzDs8cMY6wXjuAEf7OzWg3uJiFGccLAmE98uahqLGW_qcXxl6MDd2cwTH1Qi9tMLw5rYP82BYckyF2lpR8DRPkTvwv93rdInCkr2epJpnrbji0ITWH48Ob0LNtc-Mi3XtZAafXWh2_uuJT5toykzilyW95JTCZYV5GYdMedukbzuqYdpyGObtE3ciCi_Z3ldydVqg4uGYSg6e0qSsBaQo_wH1oPa4MHeA7k-7XyXYu8MHTC25fsmOuS-9k65mAVCPrlDRfKBZ7gSoRR_2aVah_TQJlIb8XYm4wJ37zHiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=CzSHZqpX7iYUXh-MqN3R7VkyIcoXu65vhtBakrL9N2atNGzDs8cMY6wXjuAEf7OzWg3uJiFGccLAmE98uahqLGW_qcXxl6MDd2cwTH1Qi9tMLw5rYP82BYckyF2lpR8DRPkTvwv93rdInCkr2epJpnrbji0ITWH48Ob0LNtc-Mi3XtZAafXWh2_uuJT5toykzilyW95JTCZYV5GYdMedukbzuqYdpyGObtE3ciCi_Z3ldydVqg4uGYSg6e0qSsBaQo_wH1oPa4MHeA7k-7XyXYu8MHTC25fsmOuS-9k65mAVCPrlDRfKBZ7gSoRR_2aVah_TQJlIb8XYm4wJ37zHiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=S_oWTiSiak-B0cFiYLJfft2mOlhWWOmcMtQutDMXmSShXZ2eMtZFK7Sf-gwkzho0CblmfW94HhjFDQYpouKDRjz_QJw_Jav2Pyt3u81RJWqgdDPcbURrZ6tb_TFKr4Eh0TrRNFgAvGGiFGeXhmc0NVVAeIHgD8cbyxIIFPMcNT_J7ElIyp0WMsprVzqqJp1_HMZfrbWjJ3KT845fCgDMdUSCQbCLKpwvmbUTRas_J5SmMEjx6b9PF-EDhBwOe-THf9Z6nnXQw_gn0I0iECSxehu-_egsZJBZivmffSM55pUlsh-UYkW5jcNHHV7sqTJdfOzdx-GoepRj22mU_pUP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=S_oWTiSiak-B0cFiYLJfft2mOlhWWOmcMtQutDMXmSShXZ2eMtZFK7Sf-gwkzho0CblmfW94HhjFDQYpouKDRjz_QJw_Jav2Pyt3u81RJWqgdDPcbURrZ6tb_TFKr4Eh0TrRNFgAvGGiFGeXhmc0NVVAeIHgD8cbyxIIFPMcNT_J7ElIyp0WMsprVzqqJp1_HMZfrbWjJ3KT845fCgDMdUSCQbCLKpwvmbUTRas_J5SmMEjx6b9PF-EDhBwOe-THf9Z6nnXQw_gn0I0iECSxehu-_egsZJBZivmffSM55pUlsh-UYkW5jcNHHV7sqTJdfOzdx-GoepRj22mU_pUP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7iG-bhNgOYDHrcXrY4SqEKaf7ZEmsJdzJ_uVl5W94Ns8q-1Cjk2mr0VEEwgOajtlSO5Cnz2sZiBzW-oge3jRc88SnZ50l7lSfjCMNIbaQ7WIx2hGlxedvzPcJIrVA1WLSH4ZaZdSwV-gKwKSgg2sZcUe70s86nKWD5t5zesDfsqzde2PeCH4snRkcZ00waozSRw65RRfMFrZI-RL_SmML1zfczdbAS1mZfwPmAn_sDryg9gKPJWyLXKsdhe6PlJllPin19JeOj12zQa-hR4RfBd_QSSzvhR9klCjeO8q_ZQMFx6hZKTsF5FLNtX3PY9faZMI1YxhQX_JRNkFRHYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpQvjQPEbZVa45JsqzJLhgvOoYZS7EjA1zP-z6BolDk4GXhP9h-mTq6q_XcUaYRIbi8QBhDvSH2Cs3tCg-Wa4JpM97-5DPVgKZeDDOe2NIM_AFMgWmiw0XMH3z_K_j0uwPCHkw1S6yss65nkD848Y-SQfDJb0Viud2nA5cHYNxpf4jEpi0F1jzOhBOKsODh5Om1DnL2hJsbtJBwQ2voG2retUPW_-u-wf4rOFMmGal9B9hpOQNkzHp3N573SBmqN2OdiwO-QoJd4ZTA_Y62EQEaH7NtZdsnBI0gw3vsapdntYhTKhUy2G46T869Mcs9gGxdxUYtBpXStDNQBDouIEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=AoZHX1FIdzw7CVHADGdpGY6XNhiZzq8Me_IbukvDC0wYHLKoNuGNxefFcxI7Bo64GqQyWWqlU6GlpZDcFEdSperO9Rt_RmRB9RsUypNvCepJUre_rz0p6vNa5U96279ZH2wJsBdRdkJGyMkNvOyDO0QYD1OE5kA-o4mHbgi1krrSBhPYa2Z6I5pQbGx8sWj0uVsxESJMx3MnWTF40RNRDGKSqzdiaZo7TyUOjyyPMJbhBpQCb6Ep2Csi_cQ-KDhWPW7GvE-asakC7hAecZ8RVWNdavPQTlOgg4mkCu977cX_SrXTWKZRHGowRnD6Npi-nQi0i37_LmbsHFO-cMKPig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=AoZHX1FIdzw7CVHADGdpGY6XNhiZzq8Me_IbukvDC0wYHLKoNuGNxefFcxI7Bo64GqQyWWqlU6GlpZDcFEdSperO9Rt_RmRB9RsUypNvCepJUre_rz0p6vNa5U96279ZH2wJsBdRdkJGyMkNvOyDO0QYD1OE5kA-o4mHbgi1krrSBhPYa2Z6I5pQbGx8sWj0uVsxESJMx3MnWTF40RNRDGKSqzdiaZo7TyUOjyyPMJbhBpQCb6Ep2Csi_cQ-KDhWPW7GvE-asakC7hAecZ8RVWNdavPQTlOgg4mkCu977cX_SrXTWKZRHGowRnD6Npi-nQi0i37_LmbsHFO-cMKPig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRcM7EFtzoLPe195s1wZumNyH9hF4j4Y5i2HTHA2GKWnqOctBge5JMJNs29aNFSwMUNUGlvwvsIGCBFcWA31ZDi5RKhbcwkHwYZ0QOxiXaff8Si-tjwmQDjZBmQZQeN8UeaD0BGHW_trn5ru6a64DJeya8qPzMCuH1IwjTiA93IOuN0TNnbfFseNgANfeFLyv8AMcpHKsgcnUd3wId4Uj6rvHj_E3FTcY6ZOhiAMKnnG_9wqAt62JsKtKaXW5eVR5pWJnqQ69WZRRvO3fNtkqjokwBvjSpy_TMpGo--27vuVD8frKVJkfif8GnEPi3EVurA3rBag9ApHhRzcHx6I0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlPGo9uRx1MTCAIMSLhEgL1ZkOELicplOc0UekWHtFfwdJwyhDDXud052AR3VfZ59BvwOuLnxD8gQg-wL1vnkkiDbtS9M_glaG_0stBNykaZRKIjXtRFV933tDPl1AGqiyyN3M7A0QV8CJ9S80qF2DIzM5fhO4x6cegYdfFYqZPTVarNfpJnj27k4JG1sfIGifnWGd93JGtURBEpEjIzN7cQMSjTwNAJJyO8YglfXV0bingqmGc5GaFPoe4TEuWOojlCM87hB3qiml0-Nh0zpjTKohOUMGvO-1f0wlEdu7u2bIOZjHCWQqbDm0gEm9sXhpBZs76EVVUPqIC1m62pPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=leaHy95z4dqk2_RFxESHckyoIHA9RexT74eCHV5NJ0XKz5Adtq6gDxOCCyYJgNUS7G4C4ElMu0adwF8uUR5d-_ZLDKs14n2V8ORmTbW5VTiNbHqnqUX2UzIa34GrSe_x4PNkMQ8dXgi-g2hxA-DHiaYBeKfxOCgLgPLN8McRW4jD22Le__0J-COwj71cfGu0ZL9yejvFn9vNsaq2KzlTQNcW9PuGMh2TOhK1tfSy-rZ5Tb4d3SqbGkvntm_JYZBYyaKX4kG3UMt47mbXo738JfoiPCncePkXYHjMqfyhoLN_3pua31U2ixJ7hSFEU5vyQDc-VSrmXLVWqDk7dNg2MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=leaHy95z4dqk2_RFxESHckyoIHA9RexT74eCHV5NJ0XKz5Adtq6gDxOCCyYJgNUS7G4C4ElMu0adwF8uUR5d-_ZLDKs14n2V8ORmTbW5VTiNbHqnqUX2UzIa34GrSe_x4PNkMQ8dXgi-g2hxA-DHiaYBeKfxOCgLgPLN8McRW4jD22Le__0J-COwj71cfGu0ZL9yejvFn9vNsaq2KzlTQNcW9PuGMh2TOhK1tfSy-rZ5Tb4d3SqbGkvntm_JYZBYyaKX4kG3UMt47mbXo738JfoiPCncePkXYHjMqfyhoLN_3pua31U2ixJ7hSFEU5vyQDc-VSrmXLVWqDk7dNg2MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=eRm0hbQZPbH9ior9Ga51c1JZAyh4PSkGDqFxEik84bU9Z67_8xzEiOsSc7inN9IH0xwgO-Xk0qY2I_phPBVUeWQj_H81TxkXOIG92qZXYLkK2onsRtX--qv1NPn-YgbBivF5hyvE3qfu4AXcgnmSNHIo1WD37T2tbGkp1PjkH8XSkhRqvehabRoOWPfcB7Iyh2rufdfexlSOe_9QVZJU6oT-kD7W2bhC1N-vZyvEeaip0Tq8q9Pdao23ax6v_q3zObiShip7ICvPPqluK-tvZmTI0Rg8N8zMKWqyPZSJfN1HK7dvMor1zyWfXZ15TfOySW9NwQw_FB5YrIms8y_5bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=eRm0hbQZPbH9ior9Ga51c1JZAyh4PSkGDqFxEik84bU9Z67_8xzEiOsSc7inN9IH0xwgO-Xk0qY2I_phPBVUeWQj_H81TxkXOIG92qZXYLkK2onsRtX--qv1NPn-YgbBivF5hyvE3qfu4AXcgnmSNHIo1WD37T2tbGkp1PjkH8XSkhRqvehabRoOWPfcB7Iyh2rufdfexlSOe_9QVZJU6oT-kD7W2bhC1N-vZyvEeaip0Tq8q9Pdao23ax6v_q3zObiShip7ICvPPqluK-tvZmTI0Rg8N8zMKWqyPZSJfN1HK7dvMor1zyWfXZ15TfOySW9NwQw_FB5YrIms8y_5bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=s2Bkftw0JsP0jx-1PYkbkzACPqR_S398QVnLW2d12B7IikD3rkb5VswMaPqI4hJ5ryFjsbpL9au_klNfY3U_1Sn1cu9ORg8QeF4a0HXiQnOP8nQ8iPi4S7qnFme3L2Qo212cYrVdgEjbGC_MuKTeFmcmK81o5uK2O-8mNid6ypzoBaFdfbep7aC309F3jiOyLmdI4jDPZLjCPBv4ZX9tPz-vUAn8UcKa0oX64NSU_Vu4chBVwqvKuOVFinVwKloKgkdD1Q83g0fGO7TQ-yYJl7HYfXfJEVvaQbsooqSPakZc1NGkF7mn0XChZjhrdhnN-dabGgIrAHfM1N92fsJ1WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=s2Bkftw0JsP0jx-1PYkbkzACPqR_S398QVnLW2d12B7IikD3rkb5VswMaPqI4hJ5ryFjsbpL9au_klNfY3U_1Sn1cu9ORg8QeF4a0HXiQnOP8nQ8iPi4S7qnFme3L2Qo212cYrVdgEjbGC_MuKTeFmcmK81o5uK2O-8mNid6ypzoBaFdfbep7aC309F3jiOyLmdI4jDPZLjCPBv4ZX9tPz-vUAn8UcKa0oX64NSU_Vu4chBVwqvKuOVFinVwKloKgkdD1Q83g0fGO7TQ-yYJl7HYfXfJEVvaQbsooqSPakZc1NGkF7mn0XChZjhrdhnN-dabGgIrAHfM1N92fsJ1WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2mHICmPdzc6-13vYAdKB1-x2PF7p1o23aaj5MvnKvK9WAYiAkOY5tIb9oaCOdE_fM2h_eClnVOAvMnAw5KASq2BoUC82sJZ9tiSZbdsqXB1S2lGQR62a_KVxMAZlFYB9J5mCJfHEhhSIOHZr_CPD0FzvO8ieAGRoYkjE_Wlz4OSf0hFwBWBVbspGMvIL4aUy_kTG1BFOoo0HdauiPwrLA2U53wnwqs0oKpHNRVbF90DwaBTitGFRjujQZleQEUdjsX6b68LCiL2pxythFzDy-skVq3KeIacY5Gt9U4CvzMNsiZb0064Gm2nytT_6sGgvneT64ux46uUvGr329dBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ec82v3oDpZpn_TTSGQRoVA4aG6yelicmIAESNPZceGU7FGKlLENDyeGR0G8pgGN8JCE1UfMgAtF7RzIZjRiaFV46gej1Bm4d6HXXxIEg3OSfBDs9K_rQmlXaBg2g5CTyqg2GHZWS_YRlFpSJoBpvby3yZqF0jeEcftn-qgqRNByX9s-rL8869z4I-XsTQx35NM9KR6sa6Kcv4rG9pN6wsK1cjwrfkemJWhYIUqKtyH__2nWxi6NRBb8M-1NQyIImLJinaehKOW6CXppBJOgfSV2OoIuIgMZrx28uFoi1EeLvEaHPziXWUKqVjNDQebOjAMyxu5BEsSFuXAc0FkLJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=mlEvi8YKhDwyNVVid9eRangTXOJAQ_dSlZu93m8coK-gyx_XGfhXX-GGpHRkI-dRMmW_eQ7CgIagBjfP6Ac9JLxqbX12uleoA8FtydtocGIzDDn9gzIGro0P3i3fNfFlUpFsLj6WtqxvAu8C_AdUst3xAmo5wBLefXCEhheDCjdIrKBVlNqsfKpgV0gjYUO6ST2rdce2bjwzWI2dag9uHeTw72oXw5SwgvbeIzRJw7J2DYbOj2y8yFU5HHvbHWWMHwvphiv32AjeHAw-DTe67YwttfJlHGzV2k4ZbwT6YDPtJjWbLAQJV9r3Rpmsz83Xcj98uGNtIOv8fJilGiH_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=mlEvi8YKhDwyNVVid9eRangTXOJAQ_dSlZu93m8coK-gyx_XGfhXX-GGpHRkI-dRMmW_eQ7CgIagBjfP6Ac9JLxqbX12uleoA8FtydtocGIzDDn9gzIGro0P3i3fNfFlUpFsLj6WtqxvAu8C_AdUst3xAmo5wBLefXCEhheDCjdIrKBVlNqsfKpgV0gjYUO6ST2rdce2bjwzWI2dag9uHeTw72oXw5SwgvbeIzRJw7J2DYbOj2y8yFU5HHvbHWWMHwvphiv32AjeHAw-DTe67YwttfJlHGzV2k4ZbwT6YDPtJjWbLAQJV9r3Rpmsz83Xcj98uGNtIOv8fJilGiH_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=DcfNDd32z5Dgcma5iMvHtjhvMWCRRHV7STMY-svxUrhAjALEyIvUj-eJatGbFdQODNcecirGHCzSP42L9yiE08_FWK4Xlun5-2KNB270ycQxBklDFZQ9KyQjG4xVLhPcdj6UrE8je2lZISdzlXxHbyPK3ICkLqfoFkd3pcg_vqJtH1lT_bODXe9Btj9fJOnOz0ygjftvzjGYW3J0s5Gb3n5JqVqa96Z-6NNvHCxdS_wlxTiMUEmq8Hfib2RRzcMdb_1uIhxWJAEHZvXSIB6Wj1dRK01mMswzUJt6Ferpdy7eajM8IMqk0qLbqO2HxOR1lNB8HfrKP409SkQQ1lHxoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=DcfNDd32z5Dgcma5iMvHtjhvMWCRRHV7STMY-svxUrhAjALEyIvUj-eJatGbFdQODNcecirGHCzSP42L9yiE08_FWK4Xlun5-2KNB270ycQxBklDFZQ9KyQjG4xVLhPcdj6UrE8je2lZISdzlXxHbyPK3ICkLqfoFkd3pcg_vqJtH1lT_bODXe9Btj9fJOnOz0ygjftvzjGYW3J0s5Gb3n5JqVqa96Z-6NNvHCxdS_wlxTiMUEmq8Hfib2RRzcMdb_1uIhxWJAEHZvXSIB6Wj1dRK01mMswzUJt6Ferpdy7eajM8IMqk0qLbqO2HxOR1lNB8HfrKP409SkQQ1lHxoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
