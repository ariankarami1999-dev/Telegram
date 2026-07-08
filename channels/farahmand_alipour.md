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
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 01:29:01</div>
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
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farahmand_alipour/5958" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
گزارشی از قطع برق در مناطق گسترده‌ای از بندرعباس، بوشهر و چابهار</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5957" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5956" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQbr2QQISjVSia5hYpUZ8i9fYCdVLkSDje6yu5sne8rOE7svuV4afU3gQ-vIYkZ1LCPriPDcIPjLBQf6jP-rX1gvroTzLceNsmGaW9cyYvG7W3CNxGO6GHpL_zn1VMQ8xsLHtTeunRwcMvAW_B8ssGdpuMDRBhR8KFgNwT8pAdBRXJcXmTPNXMe6l_xg7OeyLg6M0FMNfGmiaZ5SrXzwAY0D783h2D0dfiUdar57sRIbVgVBvLFJ9_buGsu35IcbDRB6Cl0gJmVjduyLcB0XOoFL5xpZvpcAhXjNRAc7TW4AvzLZJ-k4x5y_5k1KX5ULDQUri7V1Ag1XInH93CvuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت مجید موسوی، فرمانده موشکی سپاه</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5955" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
گزارشی از حمله به یک پایگاه بسیج در بوشهر</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5954" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5953" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQE3Cq2IarY8X-_Ou6fz_-qdBGWOOAVF32SgEn3wpQ7GxdTW9gJJMpVsTqkxf4WfRWLsiIC47_6L4dqaTawOmQ0EA_R6CvyqrgXe_0V6178I_-cWEtPwoPZ2qb3Do0qZ0xwmnFgG74TyLte6p3amF0VGUX5xff88KckCTAZwVwIdr6bNlBDONk98nNenh5ynX8fDU_RH5_5JMtLMGqjZX7znw2kWW5mnExr9dycuYTt3lEgX5PL0EbeUFsQ2o4oMmC_JI8rZ8Jv_5cWTImMpBaEelpQa28fYWLWiOKmpk_YpBh7lwD1kAwiWoq0BQeWL0lwESN2nkNvTWwPSIX__Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله به یک سیستم راداری ضد هوایی در بوشهر.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5952" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حملات به قشم و بوشهر نیز کشیده شد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/5951" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5950">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏ایرنا: صدای حدود ۱۰ انفجار در چابهار و کنارک و قطع برق قسمتی از شهر چابهار</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/5950" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5949" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxKSWjSmIZRGZCkiIdztiiXPmw7MI6TsWnzLxX_AJEyaXn6s1X9kzMjbMn30_ayUlpX43jgOi2hKsaylIDAERPdR9wiSz5wIZY5ruhOBz29lqEnvQ8OJA3QE3xoOOn07hJ7aPaXAstfulhyboeoyMGoOar8LOWvMcfcxoR66Axqafd-J0EBZkLg8Tgqglw7jCnAyFzoOgDi0j_ZqkFDps8E3JXU0zNqWCiK4fh1l6htJhQKhgNfpm6bWuusQnRQwpD1aIG4rIAakmimFuyal57AGRH7BjzW98Pm2p6etv_0cHru_OKew9GdlilnK61ISD1nMQic1SZi4rPobpk4Usw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به اسرائیل اطلاع داده است که قرار است امشب حملات گسترده‌ای به ایران انجام دهد.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5948" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5947" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5946">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
گزارش‌هایی از شروع حملات آمریکا در جنوب، حمله به مقرهای سپاه در سیریک و بندرعباس.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5946" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جی‌دی ونس که طرفدار مذاکره با ج‌ا بود:
قرار بود ما محاصره دریایی رو‌ برداریم و اونها هم‌ دست از حمله به کشتی‌ها بردارند. برای یک هفته خوب بودن ولی در ۲۴ ساعت اخیر شروع کردن به حمله به کشتی‌ها.
بهشون گفته بودیم اگه
حمله کنید به کشتی‌ها باهاتون محکم برخورد می‌کنیم. نمیخوام بگم امشب قراره باهاشون چی کار کنیم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5945" target="_blank">📅 22:33 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5944" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5943" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzzSsDYa8IXl7mXx7DOeEqP46ZcQdnBRUD64sU3JIY19s2RCYYLb_q3aDDtFOYzPCzNOncjWjzLGLfgb_Dqhqr989KFz42vbUMnRgQIeFX5NvkQp1L1eiQ3il-Gc4CiKOAprVvy_9OCHOLDWmGanGu4QRl_WYl9UdsRFepC6MSfeNnL-VtmrhDZE2IeX07dtUkvSA35ZHCwt-RbjEXs9oYxHaln930TAMkLQYmUJUc9SPfZOWe4We_oIGHg1EXT_yR4pn8exr_ZrpoukBvVRjI8rZ7rRQaIXvfuboDHX9MzWM0EygwAUgFF285h70DH_k1-CO2_lB9z3HkZpqh0XYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: درباره جمهوری اسلامی کارهایی انجام می‌دهیم که باید ۴۷ سال پیش انجام میشد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5942" target="_blank">📅 20:03 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5941" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5940" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdUfZQkUbZn4PdoxFTVxLLC1_uh0pk_Svk5640gLN8azH07lx77hJEtleV78CRvp6Z_JKpk1-_8KmjB9UTsUSLYeoWcpCE5957aqSyJMQ_5BIqDmp-TH0m7ZDyf-FrXDdMCUqeIy2m3c-VmwCzD_GNxilrk1N9IF9d71qsK81cGd-WyPe0LehJS9HHy2h9vLs9Fjl8n88UE1EwFXrG3ONQkjmhXvPpZ9zoYiM7cynGUk5udht09N7zSMOMtnXavVqK5S6Dh_15r7eA7W9ZrkkdZ7eSfmgYwRD-IWBI4zZdX7GyzYebxleNPkr72Cx3_TmJCjbEjuip8uzyiy2xlHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کشته شدن ۸ نیروی ارتشی
در جریان حملات دیشب و صبح امروز آمریکا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5939" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: اومدن خواهش کردن زمان تشییع جنازه ما رو نکش. بعد وسط این مراسم حمله کردن به سه تا کشتی.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5938" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a4f35953.mp4?token=UM-4jBsmM2fSPhhatd6bMlVbQu4DH39d-uUUvsrbWXmPL1j8yncc3jOQDYeGue1N87B2hEiHhyL4oM3rWKpx-CgWwAlxzKywwK5Z_1be9mC3wCeU7nbbIN5vKVoc9DZkXrAtmCFWxMAjHe8AJQ_Fu6CyzcOEJgLpd0o_dwVYAhs_Z_Q7GT7fU3QAuReRn2V3pxRf1R8BLAvF183QLkyWPd1LrL-2qNHcAQpoH6o7HO2Wb9xp_qhkcb-h9TlM9bjj-Fvy7_Oh9VM2cTRZdJf51Y2Z1RoNHLdo2KX09BT1U77iW8SmwwoRqP7EMDSCSeXpgi_5lSN8ceiT2mEQXrtsmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دشمن هیچ غلطی نمی‌تونه بکنه
مجری : خو اومد خود گوینده این سخن رو زد!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5937" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5936" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aff1f3384.mp4?token=UOC4u3SGDeIPTJ-MzM5_IDOjqkVIdeQ3Oc7A6uIAkmrPuvtwZ0_QJGbYJa7HGGBjDTCR7DJyWt8ZdMBBYQ6D7gsm81q7aVMSHRQfWE0GTUQunRqIBulQrSp8NsBTLYSSpiHZFNJ5zpFrZsgqwW2C3rRyg5TDVT1EDb85KQGuBbeyf-_8cXNfGvyruxEomCRSt778bVBGrT26G4la6CKTNU7sG2d-1t7x5IjdYen9rLArwh4LOwT52tnn9R5J6XnQdXtiHlM9nIpSThFXieN2MbFVV7mLZqoxTBWGakFrFvWn-tND_oGZceWsn3qEs7c-IQe_ND61wslWqTBP7gEk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : اونها تحت یک توافق هرگز به سلاح هسته‌ای نخواهد رسید، اما شاید بدون دستیابی به یک توافق هم به این هدف برسیم، اصلا شاید راحت‌تر هم باشه، چون اونها دروغگو و‌ شیادن.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5935" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=mC23x16Mi3PzHAfd-idEYYSpqEnP-DQmUm2mYwHdl-sTpVz3OxgAEpgJH9g1v2b1izJPEOLAF-wr__jXR4LiCiI4fBA7L2OpjHp2gqnl8sGtWWIlpYXZzbxe-g20lnC3ANT-wl0edA1At24kmT7GR3WFQCQ7w4ZZvnmYmoTWCveeZMIog9jtiKe-t4n_MG17cPuF769CWEwo8M4gz4Hq7kLuGoqa9-g1JaoBQoq8J49rj3vconIqPc-9fNj-QRPyYYqlB-7bV9fK5kpqJh-NbCmCLJtHLJnpGAsxTwa3uOU9bZ5o8V2-7W6mwFrnw8nxmoC4yVjEogI7MKo6qShQIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5484fca6.mp4?token=mC23x16Mi3PzHAfd-idEYYSpqEnP-DQmUm2mYwHdl-sTpVz3OxgAEpgJH9g1v2b1izJPEOLAF-wr__jXR4LiCiI4fBA7L2OpjHp2gqnl8sGtWWIlpYXZzbxe-g20lnC3ANT-wl0edA1At24kmT7GR3WFQCQ7w4ZZvnmYmoTWCveeZMIog9jtiKe-t4n_MG17cPuF769CWEwo8M4gz4Hq7kLuGoqa9-g1JaoBQoq8J49rj3vconIqPc-9fNj-QRPyYYqlB-7bV9fK5kpqJh-NbCmCLJtHLJnpGAsxTwa3uOU9bZ5o8V2-7W6mwFrnw8nxmoC4yVjEogI7MKo6qShQIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ساختمون همون جایی است که خامنه‌ای حامیانش رو جمع می‌کرد براشون می گفت :« کشتن بد است، اما فتنه بدتر است.» (پس معترضین رو راحت بکشید)
و اونها هم براش «حیدر حیدر کنان» می‌خوندن : لب تر کند امروز سحر قدس شریفیم!
ولی داستان یه جور دیگه شد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5934" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c41654d4.mp4?token=sIUCHYlduPx_HM4WvFX7f39c4BBRRln8kcipfwvCUJbe8HiGZ7vFsOs4ndas1ld7T1kgxs8lDmStQgFNYhsHwIN2aIxtxs4HEHq17V-gIMSWP6_oDxpLMhaV_qPGX9gxEEJjWTLWRE1CZFCIhRbnOS6dhbpmRXuGZp2N6dfExWgg4L9pjwoCQYkPabQlknjKTUtuB0nfgi3woWZgV6EUgH_JuJJrf208to4CSzyB2gU0Lvyoy_1scQUuuDd3ANlm709eF6xrwtImlEIb6D5ngSM9fQW3dQJ8TRso1LzSdYIoXQ8oUiORlzJo1P0Wn1rbD_3aEjTViE1VUcInC5Qc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : احتمالا امشب هم اونها رو به سختی بزنیم. فقط دارم یه هشدار کوچک بهشون میدم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5933" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5931" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am6u4Rrgu8xe47049HkbEe2GoLeGK-hOZx1km_XKP_cO5A_miICtDx6qpu8fTBH8KRnTnQu8UfsRbhd25HZTKsKBFMIA-CblIRkYcYhypdXrIDISH-w1l5s9QY563aUY4DThQUI2O1Dchy6cAVnvWz7rHw5CLFc34suckFckq1NkwD7U1y_E143cZCr5H-b-7TJxQksbK78-PiXS2vykxRns5SzXys-oSm9lPZFjXd_nH6oLKvyvcR89r3SjU04-M4-nqwYVCwwt-JOgqMHlJ5EPQ74vwNSdr-fYCXW6ztPtm1FQoYt3Vz-7cAhbq9GQnC7ZrdMeSGdcF6SyIY-eSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه کیهان زیر نظر خامنه‌ای در دو مطلب خواستار کشتن ترامپ شد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5930" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5929" target="_blank">📅 15:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7ovzrxVJ-I8dU0bHTsxaUMHAD9037YNq27Or5C6n6uHtLKXZA4tOfZOFO6RVEJYiKlh26CFYqkUf386ktr3AkL8mFXwCAwk31gZJHYl1hIUchBwk_mp6pbLnFfsQGHLXQxkVyIxQNGoRNJQTAQaeMVAp4_XLd2_KjsYWAAV635Fy3Xwsvq85AsoKMib1VxzOJ7QxQSvO-krfSpZbi9Av6321v_a6qyuq9UpEjQ0JpKXWxHzjjsdu2FSc_2sei0gVqQp5iUm3d-hEmmA5RoB8r0Wu9uiNMog_8NrotCtEyqGT4yjx164VMZtPhp--x5P0CMSZi9FnISzm37ofUkLEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوش دولت چپگراش رو چنان بکش
که درس عبرتی بشه برای بقیه اروپا!
برو جلو! دعای خیر ما پشت سرته!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5928" target="_blank">📅 13:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5927">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">محمد اکبرزاده، ‏ معاون سیاسی نیروی دریایی سپاه، ‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.   او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.   جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5927" target="_blank">📅 11:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
دبیرکل ناتو : حملات آمریکا به جمهوری اسلامی کاملا ضروری بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5926" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLTAkiyyGNWlhbVQ2nrqLIjN41U5ZvJZezsHRVicPJ5GjQacvQQa6zPRnyeEK24wU3Yv_V7a_w24YLDPnu5FBhCa4Dz3tiMiLt4cUVEXH15-N_Y6046KzKMGd0Aj9xZGRFwwQ6q2aH8nSolXrxWUf9m7l5waP8kG5t1DELeo--EFCgs2XaV-GXasMDv_ngG-71hjJujQw912CoTZKZvsaXemWZ1vpqoghzVriFQeJ3Tw05cTNPHjHmdZIZGj_8nwtmad7LMNk1N3oZN9z2Xa2QTyq2Aa3GJIgQDXVBHKIVVr6TZOP0c57QQ7S8z6pKi5enBgDUi5SM-_y0NC0BG4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندرعباس - پس از حمله آمریکا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5925" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پذیرایی گرم از عراقچی این بار در عراق</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5924" target="_blank">📅 08:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
سپاه : به ۸۵ هدف مرتبط با آمریکا حمله کردیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5923" target="_blank">📅 07:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aada56b9e2.mp4?token=Rn_8WCUJbJutyPrrsbMZMeVklr871nCBWKrfT0m9f_uqL8UzQqnbVchV9RocoskvFLnM1rzw4iiNr0iISQPQR9vyPozccctXPIFjwtTBjK63QOoM0xPtuCCyWD7wMVHUZJen9tEGNBIqI5P4WKregQ06eb_O08JDarZZvevzknG8qaIZacMCgnxUytnh63z2c1e43687SiVbEblFIgNPsECUmc0QIPVUjmzLrPyV3VklTcdOIoyzEdiyPpzP_H-WCr_ob5AgrmEJxeZLp4Nxu6hP3pQWEyUH1XnuOMe_pJ6KaMwmc7a7UF-0SKvjokXa1aR1-T6SzIg0VfeBmUEEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس - امش</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5922" target="_blank">📅 04:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZc_Vwhxfkh47zUVQhoGuIfSV38s0LjAnnkjB4zJqeEnRphn1r0OWGdkYplpgpObbgZ-IafyVuC90iMrDb_Jl810J9ku1FSRBxwWcDMmr7eB2eWp-nyKSUtLywniQmMKtYiVN7Zh7B5tCeEyqDFI00F52R4MY3Sro3IgipTEaZ9JvQOhLcAx6XhF0ilOnvgoQZfqY6dhDtr8PN1Zgteh-mi9SV6fM0UlWtUZg8qDv7oRdWLNsQ_9W3heaUiJSV5Dl3dR0j65Uy3RN9Dk6wcqYKh9zXovpGwjKH0ZPKmHIZQZaf4I6dejBLxKRs-bAc5i-pHjTwNpLj8gn0GXj41EWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش ها از شنیده شدن حداقل ۳ انفجار در بندر عباس
تصویری که گفته می‌شود آتش گرفتن یکی از قایق های تندرو سپاه است</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5921" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
ارتش آمریکا: نیروهای ما آغاز یک رشته حملات قدرتمند علیه ایران را آغاز کرده‌اند.
‏حملات آمریکا در واکنش به حملات ایران علیه سه کشتی تجاری است که در حال عبور از تنگه هرمز بودند.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5920" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در حوالی قشم و سیریک!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5919" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5918">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=Hlq_2rB51YY97hX9EPrjWSPGhShdz7n0QFoaOQeuaQbdFACBgrGym2bLn1l2xSeS2VqnFFDYimahJHtQcug7UBN0FJz8v0CjaHl2avEUeb2hXbOvW1OsJKVqRyqN5w4DROQRznRsGfv7v1gnzjtPf_-UqcKQX_dHElADTNSfc4cpeDJ0JQOpXHIG6kEdPZ5C3bwJW8qAezFsAkjCFd6uG37jpNolvb55YLfYjtIlVohPSe3ZYaBhu0X3KC8T5FM9iVWo3OClCl3W-9WtmcNVEzumugxEHvue6Lb9G-g3kclf_TIAhljs4oTS-osmDJ_yfrHU4KlmGv0YkbbOQFLq-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f02faf66.mp4?token=Hlq_2rB51YY97hX9EPrjWSPGhShdz7n0QFoaOQeuaQbdFACBgrGym2bLn1l2xSeS2VqnFFDYimahJHtQcug7UBN0FJz8v0CjaHl2avEUeb2hXbOvW1OsJKVqRyqN5w4DROQRznRsGfv7v1gnzjtPf_-UqcKQX_dHElADTNSfc4cpeDJ0JQOpXHIG6kEdPZ5C3bwJW8qAezFsAkjCFd6uG37jpNolvb55YLfYjtIlVohPSe3ZYaBhu0X3KC8T5FM9iVWo3OClCl3W-9WtmcNVEzumugxEHvue6Lb9G-g3kclf_TIAhljs4oTS-osmDJ_yfrHU4KlmGv0YkbbOQFLq-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی این ویدئو دقت کردید یه نفر رو به کامیون جنازه خامنه‌ای وصل کردن؟ :)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5918" target="_blank">📅 00:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYlWE-T9ee_SQawtgsguqRyjRdTF0b7U5rT308SZm0BKvJTK5UNj7I3NuHu0CMwNGLwGFMV4zTqL1FOdIpIdm7jb4e-QLI40f8Z1DI_yQik6nUJON73BL7z27VlOTXZ2ukQVXueGg6lNWuGpcXE4XaszGOMB_q4BvXDesaYoHcvnc1sAK-gyRQWCqHoNeKh7LJwnE6IFZ6kvwSgqHZ340EEu28GCiHoKCaPPditL-I-RsUDAfICOyHtzshaw0ifWr8xvydG2EmzI78S3oVoStwgdrgKzPTQQbaJf1VDBFuaK9Gbe83t3nbijiZPTfRQZXdcfPZ9pSZuTkH226ZTkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو حقیقتا یک سکانس تاریخیه، مدلی که دارند خودروی تابوت خامنه‌ای رو اسکورت میکنن :)  دارند جنازه خامنه‌ای رو‌ از جلوی خونه‌اش رد می‌کنن، از همین هم‌ پیروزی ساخته و‌ میگه چقدر قشنگه آقا خودش اومده به دیدن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5917" target="_blank">📅 00:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5916">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiw6TmoaV9yUoG4DQZiuSIaq4x-Wy20hVxFelCw1JSRImoQNVZGUT4NEC87iTB18x206iQMX1__TvuL1AhqDu6m7VSjxRGr3DsvbSgY-g7lLjwB7lc1bYWUJ5nMwd4gbt16kff8SH8DHDoIDHk68Db0rvDU0IHehb-7HrUxg2qSahL32N2i6W_8E2DYe-ZEye0tKZFQ6fTm5AKGUFWHjZJx5L2etmMsU3WZ2m7rZhDFVH9nxrcG73QOpFKO__PCAOFxkjMIGMrJNBKC0M3GykQ4ssxdtyQf5SsFJBS-5RezT2E0aGqTCWFKgcXEphPPy7fWFYcz-VS8sjuFHBTAawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما موشک میزنیم بر اساس حسن همجواریه
شما بیانیه بدید اعتراض کنید
مغایر با حسن همجواریه!
کشورهای همسایه هم تازه دارن می‌فهمن
مردم ایران از دست اینها چی میکشن</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5916" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=b4aYLMx3El45MyNBTqpPsd70Y2qDU4IYGMJxYJKkJrnJ_A_nZ3x62c6FCaLsXjrsYDNwMtIBqD8TDBruRUimVBVxK1lSpyoh1hZP_Hu9ngSIAHU85JrQxO7cQJ385osVjvA-sswKDtdJmZl8Pb5StZTFQt42xLf3etyOE6v5Nv00D76ggJ8A6HHj_6lvcUTX6fqdNAoNjrs-_p2w4mxd3NoL48viTVlrWyR9RqxFZr24Sx1QFZtID8IkQ28cIjCPjR6Zq5ljfynsn5cWOXnx7eb86Icj-0X_75gfhttxwgDwc1KQ--oo5Spt-6a1si4_VGJw6Dbnq_6Y0pM0U9Aiyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e58e9ca73.mp4?token=b4aYLMx3El45MyNBTqpPsd70Y2qDU4IYGMJxYJKkJrnJ_A_nZ3x62c6FCaLsXjrsYDNwMtIBqD8TDBruRUimVBVxK1lSpyoh1hZP_Hu9ngSIAHU85JrQxO7cQJ385osVjvA-sswKDtdJmZl8Pb5StZTFQt42xLf3etyOE6v5Nv00D76ggJ8A6HHj_6lvcUTX6fqdNAoNjrs-_p2w4mxd3NoL48viTVlrWyR9RqxFZr24Sx1QFZtID8IkQ28cIjCPjR6Zq5ljfynsn5cWOXnx7eb86Icj-0X_75gfhttxwgDwc1KQ--oo5Spt-6a1si4_VGJw6Dbnq_6Y0pM0U9Aiyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه حمل جنازه خامنه‌ای</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5915" target="_blank">📅 23:26 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5913" target="_blank">📅 23:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhJ97e9GYOupwsBQkWMp77mnkZev_yMZZ_osA9CBdNJqKZ-nkPTEI9iqbgLabrUx4WnlIF2Nr5I-iAacMF40ZYDXTM90lp55XV0nuHwRmqintjUrf9KCcMNlpSK3nOtleiTB20cje0TqSXcFtg0L7bo41wMGXuNv7D2OVACdIHOLN6wdkzdRJCREYivQikJ6VPrqiEY7JE5Y0gMthzvJTWPoma1ePmeeGftdWdigpkH3fW-SP1rWRArMtRIx_LERLu5_0T4tk_3E1EoOZswyNRtsVVyxQ6PeZwxBvdwXZMUrTikY8mZoNni7JhxdbPEaehtiP_xsvf_8HT8ffdVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط امروز به سه تا کشتی حمله کردن
بهشون که واکنش نشون میدن میشه نقض!
جای ترامپ بودم یه توییت میزدم خطاب
به نخست وزیر عراق،
هلی‌کوپتر از وسط راه برگرده قم!
بیاد دستشون!
برای آمریکا خرجش یک «توییت» زدنه!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5912" target="_blank">📅 22:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFXgntI9SIgdPmWpNH7O8b7f_F3isFHpCbHP3ndOzPf80mVNex5UxZ4y6ngcqPRAWhwjnu4Ge_fS36oW03-sSOqOzcoMzRqhjawQ9PiIwNM7_3nOQaRcMBJq61jWTzID2ba7LgLUu2acOzypDki5G_ZEuZGgzbOCpKv8tluh6UtZQxvGN9zvMKX6PnYZwjLGVT3N3mNDQYXMiXtomNFfqGMjjjq2Cn4RboBEdFUSwYNoMNzeuMjS5hTf81GPHAHwJwT5wBsoSPRTcz5yA0-1E7cpr9vliVBg--xkdeZFT1fEV2SltK21CTyPQ9wc_eZIsu76pSCB6oLMzirtjMpMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمریکا مجوز فروش نفت ایران را لغو کرد!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5911" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRRSVoUhOGMW633mDLhMIy9ntJUVteuk5t0PIz6gIWm0JGXSnrI0zsmBPPtlIHPxB3u8apL6jdh1btpFxd3qBndCK2CSkdi9AVVvXCNSUlSu_gE56X3jnApp4iMjZYhb6mosKle0RhOz1Oi5qxzOJVlG1BZSTJO96zS8rHpw0LMXYWvBjfY5t4UU46mVOd_Fy5xnbuKKpLNgU9JeSZWC7Y7lOVdoW0GCS532gUWMZZ74Y4LD7y8TmJOLjtg-4q58wxO6vC0mo8uF5ANtB0ieor-3g3NTTMxc_MJ-n5b1Kb-uQnH84sfSLGn9UQksPT4sCEX6eh5IWJjcasgrKPIejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد حمید  رسایی :)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5910" target="_blank">📅 22:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک مقام آمریکایی: واشنگتن مجوزی را که فروش نفت ایران را اجازه می‌داد لغو می‌کند.
‏یک مقام آمریکایی اعلام کرد که ایالات متحده در حال لغو یک مجوز عمومی (General License) است که فروش نفت ایران را مجاز می‌کرد.
‏ این مقام آمریکایی هشدار داد که اقدامات ایران در تنگه هرمز «کاملاً غیرقابل قبول» است و «با پیامدهایی روبه‌رو خواهد شد»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5909" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dj8tnrS6KXUFA7AhAdJHBh7j9Dvk7cl9bM7D48jSVETAd6jtA5L-MxGWLXKbBKIOVw_ZZm5g6aMDxwdtLsTfLbamfUOYJ4zuK4BlYqZKOdf1lopqRXCmnufOmdGJVc7V7h0OCfNZri95ERLc39U5ycw2Yi9JssElS1Z0C6gut6d-k4SEST7Cq4M_o5_zSywzD1Cv_YcNG9sFwVbr82WI_pe3sweq09gJ724m8SamUBucWsmadRtXr_DlXuK30WZS9gDSWwkNgoJJY_Dqyn5MwAFD1Yyg4cw2jZa37YEi8qwkwrbN8uNkDuX2wwiLv-ZItGcN-R1alRQJE4o-VjRYvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjeZoV2uGMVrt1QltubRoLFCm0uEtBV-C8loA_fz6wcbYVnkafEjkuKsXC5RPHuwRPuCPTAGWvJp2iuLZjHkcTw9YNTcnYm2A3bJ-AFv7EHQXzg9hln29YIlhHWylTfdPexb7_UP9jp16zHi_9xBJtxMay5gAQ5kf0yuQ-GUb2Pgw-sLeLpme6ODWvtLLFGtTIzqlwvxrbqK7dp24_eEtYowC1oimIwZUeMeY7YIis3eihtUKYWWcIN485IicPHWKGtpdSQcvS7IYreXlQyc8o_PVIuU2Nz60ujwizWUGwTO2_2h6DoiFSloSKrWMCuENk3nmq05ex6U6n-UAMEgTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=LTQUU9wBzzYNj3OSofZmzM8XazDVllB_K8wpFd95eMCpN6WSeFF7eZZhZuTu45UD3zB_QSgGOqDLtwTzOpMRr5y4iOa2IMZhgsLusTeYzblEB_nQli4v_lRdCMQyx_0Be6vqdcRSguq9UjRZdZWx80t-aOkfNCLPNbRisa0OGhAA_d6W5N3ifvL4W6n0qPzPvnJcBoR2pCCFizZLtbT9XIYi5xkFbD91IOugychMBAmlE3OoYoqM-7cmejutmWSet6EeUBlyNeiJ08KhbzeQBDtE_IR8YDWULgQxlSAQrXyGQtipLuOuGfbnvkxRz8K_vh1MbKZIUnOdCI3ejy5GwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=LTQUU9wBzzYNj3OSofZmzM8XazDVllB_K8wpFd95eMCpN6WSeFF7eZZhZuTu45UD3zB_QSgGOqDLtwTzOpMRr5y4iOa2IMZhgsLusTeYzblEB_nQli4v_lRdCMQyx_0Be6vqdcRSguq9UjRZdZWx80t-aOkfNCLPNbRisa0OGhAA_d6W5N3ifvL4W6n0qPzPvnJcBoR2pCCFizZLtbT9XIYi5xkFbD91IOugychMBAmlE3OoYoqM-7cmejutmWSet6EeUBlyNeiJ08KhbzeQBDtE_IR8YDWULgQxlSAQrXyGQtipLuOuGfbnvkxRz8K_vh1MbKZIUnOdCI3ejy5GwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDo2Aj5NtMjYevyuu0HBbJEWjdab28aAzCMD22ZFUjizeC9YhYTfTAemJyJBxiHgpv9nfgtigef2uJgXFirWYTuASx1D9iiop6VZK0bY2xMpseegwUXRZFVQrRoufYmNWlYih2dBG1VC4dXGMxmz7by0iClRtlUsqVd61g09NGToDj-yvmZo7FZVpK3MK3CSFFh0-Zyb0uxUrw8wWl3zOxs2MO1q55BHXJeSI6pzYQiTKuyghqf2g6lHOKjp7YvFGKEO4vQpIHJzpKYm1OK06e11vS5fLbhKTzgd3-U6ik_P58J4243y7qV7qnJJ_fydQfR2c0_XQE_XDlDsvr9y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=f7ik2sGcquygBOQyD54OoTWePWElC20m2Pi1mxnr8oBxWI-W-PyU_gcjiDBDFtEQdqM0p8sGXJWSpaUOa3zo8MjMUM68Mmg_ESIdZPvwCVpSl-TqeYsdvsmqHm_L33xYrpcTdzDd866UgZ9TTZoE8G1_xLXSkBrzyMD_RyHYAthYUE9xV_ZHtD4fLTwcNT_Tkw5WfKB_x_NQDfwUcYosjq5o5qIF-iaXUWowUTUFegkNiWSHnB9bBBiu-LKdBoxjRR9UK3e8zvP_dJ3bZCruipnWBexsQB4WsmCYceP6wyhajucUsR3LnG_UAwgfF3J8vsfduejaIjgaFLA5odgJJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=f7ik2sGcquygBOQyD54OoTWePWElC20m2Pi1mxnr8oBxWI-W-PyU_gcjiDBDFtEQdqM0p8sGXJWSpaUOa3zo8MjMUM68Mmg_ESIdZPvwCVpSl-TqeYsdvsmqHm_L33xYrpcTdzDd866UgZ9TTZoE8G1_xLXSkBrzyMD_RyHYAthYUE9xV_ZHtD4fLTwcNT_Tkw5WfKB_x_NQDfwUcYosjq5o5qIF-iaXUWowUTUFegkNiWSHnB9bBBiu-LKdBoxjRR9UK3e8zvP_dJ3bZCruipnWBexsQB4WsmCYceP6wyhajucUsR3LnG_UAwgfF3J8vsfduejaIjgaFLA5odgJJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOZdKKEqkb4-lK6PgnTPeqIWIKToYHPXLHTIkdwCIy_CwzEYDoqBAVQIt_flaIfD4n4O6B_727BQCnEaGkOjkq-3kdmDR0iCwr3nS4naJJkGaf_INmVqTed2RY2lv4A8lRSyalsLMzMj_GWukMfxrnptncJXlCkdf1pLszcQ4uEZ1xDyYCEfwaAL709oNYIPJHepRfGcXamqsjp6KIGzmwInpDS7S1Y6YEHq6fJBDxO44akrr6zeqJC5n11a-cUypQ2a8qx5EfKQiPeXBvy3v0nWoMZG6IoQFYV0bG2V63QFcxilkisHyoIekDoR9WdSXmeQ2emBPFYmickz7hUb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=DpZUTzTSV34Zr_nvJBVhXeJvyK0grWRapMV-uRcYpZtRbgc6EmpVV3hBO9LIKY009yJcJ1ERZi7HmwFkdMlSFcPhaTZJXhrpyEetMsSnhoTkyslrMEqdcuefN-87HTBBSIu-UYEFlD2is2BscWXGXWu2FhSQxpKBBjKHsEuhQkHBj03r0LlxXlxO5eT1nHgki96O2CFRttiptq8ufO3wIeJ8UsQea1yno6sHYU-DLYqLiwCr7r4ZEXSfqodJoHslqn-nugXjcvX7k1eV9b9fj6qcfY7EQwbJi003U8FMo6J3zuycx_QJ3p_OJR2_rQdA29NHUYzASit3-TSPrXT5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=DpZUTzTSV34Zr_nvJBVhXeJvyK0grWRapMV-uRcYpZtRbgc6EmpVV3hBO9LIKY009yJcJ1ERZi7HmwFkdMlSFcPhaTZJXhrpyEetMsSnhoTkyslrMEqdcuefN-87HTBBSIu-UYEFlD2is2BscWXGXWu2FhSQxpKBBjKHsEuhQkHBj03r0LlxXlxO5eT1nHgki96O2CFRttiptq8ufO3wIeJ8UsQea1yno6sHYU-DLYqLiwCr7r4ZEXSfqodJoHslqn-nugXjcvX7k1eV9b9fj6qcfY7EQwbJi003U8FMo6J3zuycx_QJ3p_OJR2_rQdA29NHUYzASit3-TSPrXT5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llhsacVq2yx3zx54dpv3JP32qhQwCl9-d5rH0Vqu5-kGlKfONw0XZr_Siu6dl2zxbMWrzU4kAlaoFjsc2G88yYaCrzcC6ZOMhrK7wJLMcdxU3eGvTzaFjzSOBm8NUrj2HTIpqnaS59Ws-Da9dXiL7anCi5FkZNr0fXbfZWnjbaDcF6F2E4LnyGJvHxbyXCD99iHWWEBPhDC64T_np7MZDFN3QLRv13y6DczlaRd8xWIwkdmqZzRoyk9ZUoOuJtOpyqMMfih2H9mkDHMtFP3w7kqc8IndxwYo9zl4xTpCZTS_0KptP4212FOhf9jBLuVj1BSCdIFPuwWpupmDIK7iJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chAFwobohSBoCkAH334bn3qCpVQma4IIzn3_XYIES3Hc8L_or6CBnf1aMwr-1LKQK4IHngaDNULsM09MISH6myG3VxMtoKO5Aw4KNABZBKxKZwLNOWLgYzm4J6tITww24OLM5pS7mDdNKuPz7xVxLdhawc8tZnc5C9wPNWom-C0ZbWSPmrCWGNVxc3w29FlQvakyqOavtiVgGurn4931kdUH5WVeMjQdgEffE3-_Ju7KHFyftZuZCfZBPg0W8a5Fd48nnHght0q-eps8DwVi-ECZyjuX2brEy1SL4ELFT0n5bbmmFIKcH52hqusu6U_AZ063QcaCwDbjFKuds-Pg7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSouzOQNgESG0dMF2kwlYcgDyWJqQws85rFU9J4J3S7RM5FvX67de9eNu9S7mof-FMNNRKxN1gKy3w-L-z8z6uPHK7A7Wde3_J3MnpSQe9oGMDKEyC51w6AVgJrHHnQNc6CvbJYnjq0bY4hNNmFaxGQDH0tokTEDB4HST0PO45sL9aGxt2DX9R-uGVXfh29Al0JjvfM6RUP9yuvt45FC92XD34vG7zkfvdHy7Bg2FywejxIn_ADUr4eMTzBpha8lXFeXcJ38UF05vyIpX8wu9zSHocqMv7hVYlz7hdUsm8uq9QrXqHCcoAvEtJ1rZzLUPicuUhVPeZlHHQbqZWa_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV-SRi_ls-motkfe9LQlrpDfv6t8NO7BsoYl4PeWpNqXgyLioH8c79SYS6xXq6egocsoMOGbFdYnPw7CyAItzwbr7GkFni8Oo-FPatGkUjrHotAaaiPMeo81W3xfJY2Vh5uljvCZ3D2uQt2QOaPHyKWz71Vwm6QWCTT47d5mPXm52OedSx3BTaxIJXjLcfOy76hnf2sgASqEAZF5E0XiowLaV4fMC2bh-OjZmi5mb2ScBPtpVVr2mYtd8K-K4LtrPS0zIj0tHLamazE4FX5NKYDfrcvUZ1-xnsuwzitKPlN4BZ8hCkN5LCjeWyB33LR2ie6W53NhGSiU-AfEPu850w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghhkT5JL8Ul5RB-IN-7kj1bw7gxJPqXtFRUgx49c6fJF2Wnn1CFpN0bSGII5eR6ecTAhppR14sttKQSt6Ov2T6vQNsgS154y98S-zoOnwBTPqvkzH_DeoNeZdiQMHTFYkHmg2ddwn7g-xRDunYXN7yIsoMeiRen4-hk0rH3Unh6AWD7_oLEP2Rc7KA3b_qwM-aZWR0V70smi-XmISFzsmZxdfjYm-5vTdlNYArA35S37Xgm3AkuUKHD99nIgZnlNF32dnW9ZSmYMWtemxYKKcEue-aoP4ITtVbECuzBAIEBEjI-8pOevOxnwy22fS6qVtXok1rgdeuTNagWeeuXPaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=YcSvAkVXCNTud576IbUEQJvsaQuzusYIvt80lOKTjFSvSfA3Wh49hgPkrc-e3mN6kGSbMVt5WFEYL6qmxVeH7jTEmJVCKjeSY1DSxJeA7hZED9HJwQIBdbmv9b0bKX3SYh6YBpcWK-SsjANdaW0-H5OTKVjpKI8EHFka0STJgNTBcp-6IDm2QgKJAHm4d1jjDhKihve1KnHveVshQfgi6gMhsYSfcS9M19ZgnwzRYoz99Uh-Vettc5PYINepuRwGImO4x30W1busrOviZVJxbrIb8lSMt7ZbHeUA4pJ7Sy86NO7XIMIxjYmoBtnzCnhJQlE0AbYqoATPiU4HWLSzvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=YcSvAkVXCNTud576IbUEQJvsaQuzusYIvt80lOKTjFSvSfA3Wh49hgPkrc-e3mN6kGSbMVt5WFEYL6qmxVeH7jTEmJVCKjeSY1DSxJeA7hZED9HJwQIBdbmv9b0bKX3SYh6YBpcWK-SsjANdaW0-H5OTKVjpKI8EHFka0STJgNTBcp-6IDm2QgKJAHm4d1jjDhKihve1KnHveVshQfgi6gMhsYSfcS9M19ZgnwzRYoz99Uh-Vettc5PYINepuRwGImO4x30W1busrOviZVJxbrIb8lSMt7ZbHeUA4pJ7Sy86NO7XIMIxjYmoBtnzCnhJQlE0AbYqoATPiU4HWLSzvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=NseRdb3dOEAuRyL1w5t4kemtGHM-3tIwiiC7ayj-cyvGIMpO6HUdLwUrt2GG5QVIMU33z4zwM4XHlm4Nk_rRBUNf3GeEJM_CFugkAh5Xi2plV7r90bPcxZboNeLpUtTtCLz0tvv9Q0ka4TUt5_tmej8pmLNvt8pq96POGeXFvsgVtRCJISHWaZibwAnVlUub3OBlQT5x_MwpmAlUREZJA083fwaKCJCtcAnGSd1-Of5BP2NMTbPMOSi5hE3O2t9Ix7pc1dD1YhnnyFnteX-0UiNaBMC6WXWbs53oNOjuSnMXtICQ_fyOpH5HdPAu6KuXT0aNbs3cAnx41hI_e4USHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=NseRdb3dOEAuRyL1w5t4kemtGHM-3tIwiiC7ayj-cyvGIMpO6HUdLwUrt2GG5QVIMU33z4zwM4XHlm4Nk_rRBUNf3GeEJM_CFugkAh5Xi2plV7r90bPcxZboNeLpUtTtCLz0tvv9Q0ka4TUt5_tmej8pmLNvt8pq96POGeXFvsgVtRCJISHWaZibwAnVlUub3OBlQT5x_MwpmAlUREZJA083fwaKCJCtcAnGSd1-Of5BP2NMTbPMOSi5hE3O2t9Ix7pc1dD1YhnnyFnteX-0UiNaBMC6WXWbs53oNOjuSnMXtICQ_fyOpH5HdPAu6KuXT0aNbs3cAnx41hI_e4USHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=c0T3vZZNQTYdAy9Y1f7MkhMzYNR7F18HQykXVkxqDUGGTmEIC2WO2-IipmDqJW1xenYlC6iiaqY0OE6cxqeTKn3tZoICheUM4jDub4YGa6fRkz8s2Xd297OmOhp7ZHO-2XYztIZg_9KXlJk7soBi5vymO13yIQHhXe5jd5FYTDkMUBbroZzyjlh9q0ZZeET2wxqZ6rca8Vp3vvMXiBwVuLWXTBTaWgrdyNH6eMYnQtqt2m7dHLPiJuWazrMXgtTuO6TY7zm59GQfHRBxJgbT_4MThnrod3VtlR4SQjef9Q2F68QDgcdkt6pysmnaivLOB62Pkl_o_fVoh3JXEc5aGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=c0T3vZZNQTYdAy9Y1f7MkhMzYNR7F18HQykXVkxqDUGGTmEIC2WO2-IipmDqJW1xenYlC6iiaqY0OE6cxqeTKn3tZoICheUM4jDub4YGa6fRkz8s2Xd297OmOhp7ZHO-2XYztIZg_9KXlJk7soBi5vymO13yIQHhXe5jd5FYTDkMUBbroZzyjlh9q0ZZeET2wxqZ6rca8Vp3vvMXiBwVuLWXTBTaWgrdyNH6eMYnQtqt2m7dHLPiJuWazrMXgtTuO6TY7zm59GQfHRBxJgbT_4MThnrod3VtlR4SQjef9Q2F68QDgcdkt6pysmnaivLOB62Pkl_o_fVoh3JXEc5aGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=BB6V6vODO_GJz00wCvBDEawW2ioBTZboD0-jNnGKpPeftf9OYHP2EeyT2Pb25tBNllOiiHvkcnw0K4ZWjkT4UgJY3uYo3kkIBWkUxVX2ZlN7eX9rANbhMLFTiQg1nAB3cz5FyUPUNUti3uc6dbp_j2J096YHMUzTfzSnlxUqW5EQ-bPZ1jvAAcT_C2sWCtEj5iNTo7luhyS4zFxepbFdbbPvtHk1E2-3Vopcl-c7bswfhYriA1Nkbyn4un_TijCp8n379zpEiha4_enFou2__zc70gCDHx3BKtM_asKMZujznlBqNFy6usTzTkxBLiqVVs12LptM2g0hq0-lp8wysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=BB6V6vODO_GJz00wCvBDEawW2ioBTZboD0-jNnGKpPeftf9OYHP2EeyT2Pb25tBNllOiiHvkcnw0K4ZWjkT4UgJY3uYo3kkIBWkUxVX2ZlN7eX9rANbhMLFTiQg1nAB3cz5FyUPUNUti3uc6dbp_j2J096YHMUzTfzSnlxUqW5EQ-bPZ1jvAAcT_C2sWCtEj5iNTo7luhyS4zFxepbFdbbPvtHk1E2-3Vopcl-c7bswfhYriA1Nkbyn4un_TijCp8n379zpEiha4_enFou2__zc70gCDHx3BKtM_asKMZujznlBqNFy6usTzTkxBLiqVVs12LptM2g0hq0-lp8wysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5X-yAWQxHL-yJhOq7bdCumExYCX2SuKI6IlQRhcOH26MOiJgEo5Hq9H5JcEblJcfCxCEBbHOGWrQUf70L4JxOG1FUySISuB1QkfSw2BT4BzTA67GqpDWN4pJnLreDz4bnaS3ytkYxSemtYMGpOACfpZZXxJHmgM2hKRZUtU09Dpx7exb1kiKjEgc1gNHMFQ9S-3IuoQMPj4SJIQqY_g3QG5Z-1pBjKc9VpgBEw3DV6XPpebMhAtRQArr81npVe9PrZ-tOzoK8Nm0Iskrm3xBcibt2AJLWqAyun7eIlE0mw0G35ae_YgQyKZ9vD2R_ZHWmAf7JasfrlsT_SYkTdoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=RVT8Ib9oz7WDY1beI1riD_onq0bFfpvgbMOi0fCBdDqVUJie5VnQO5mAByPUaCPYOZ9jbNva38N2b2PnBL-i7BL7P4ftCsDH3CzxOV2U6ARUy78JNrl0Mhzdu6MtX_nB6GakzVZI_7IUgHou_6_Mr7S0ILXib-ejB2tga991BLtGsdkHgj8VJ9qu3xT8WV3x6t-xEFVN-P8-bNVFVz_wU04yoYTkVZ-JrhNlTCBHZDdbdNDxfx-TM_hnqUK5A3FOo9YFBOyeo1DFlyRXIbCAj0egN4tXVOjhdi4OSlHUGfNLiGgfJyja2FiNZ3N1DoXxk3BdVY1WjJINmVcsfF6XjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=RVT8Ib9oz7WDY1beI1riD_onq0bFfpvgbMOi0fCBdDqVUJie5VnQO5mAByPUaCPYOZ9jbNva38N2b2PnBL-i7BL7P4ftCsDH3CzxOV2U6ARUy78JNrl0Mhzdu6MtX_nB6GakzVZI_7IUgHou_6_Mr7S0ILXib-ejB2tga991BLtGsdkHgj8VJ9qu3xT8WV3x6t-xEFVN-P8-bNVFVz_wU04yoYTkVZ-JrhNlTCBHZDdbdNDxfx-TM_hnqUK5A3FOo9YFBOyeo1DFlyRXIbCAj0egN4tXVOjhdi4OSlHUGfNLiGgfJyja2FiNZ3N1DoXxk3BdVY1WjJINmVcsfF6XjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpP6nqmuy1w051vsdAS24sje4PaV-sRpwpMLagSEVIHgKDleB_lv5x1MbVthUt57du_XT6x1qrWBMKwd4IAlHZn7EKB0xk7GVPLXMC-0pN3QvkCXTvVsruhurx8qh4CM9P0nlpuF0SETjra18SO2hyOtrYMGa7CFV7oc2_3_bkgEeCkXi81f48LWto_ojHkMfkjEvNuX8QAAcp2uFZdKA3mCTptuYLMToiG0PzYuPHLBAdM6nSjuTDBhY2_8b3PAZcL7OTuVbUfxgFm0bK9V3N8FIp3vJIx-KC9XzmqvZQxfOpxLY1erDYFqpiLtcZr1HRGRMviuwHOpZ2qgP7-Xmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=O2Qg_BPhEbt4Q6jdtQavCQaS5unsox6qZIrhK2DCGFev26ACVgMLwq2ePCziBhpvEUzffZovATSFWkHTf3URHbq-My6MB-NOD878k-22B8zJPCSqRsQOlC9YQjxgAUB0gLdmWkXL82tZQVbA01VMsiTZ5a8kTb16aqPNAanm2DbIlOCA6Ilvsc_TH3Z0O_UgslrHpmaoXjU0NYzLMofwKf4u7_BWjRWYFp_eUXRGRhscomkyjsd3bVIRtXEHPrlxSrJpjqjoAg6l4u_r4X5lI5ieqz_1AjBR4onZfiV-OBO_F4SDmi2cFvJHI-0dhwYUkC1L0MO0T5-pU9Kftrt2lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=O2Qg_BPhEbt4Q6jdtQavCQaS5unsox6qZIrhK2DCGFev26ACVgMLwq2ePCziBhpvEUzffZovATSFWkHTf3URHbq-My6MB-NOD878k-22B8zJPCSqRsQOlC9YQjxgAUB0gLdmWkXL82tZQVbA01VMsiTZ5a8kTb16aqPNAanm2DbIlOCA6Ilvsc_TH3Z0O_UgslrHpmaoXjU0NYzLMofwKf4u7_BWjRWYFp_eUXRGRhscomkyjsd3bVIRtXEHPrlxSrJpjqjoAg6l4u_r4X5lI5ieqz_1AjBR4onZfiV-OBO_F4SDmi2cFvJHI-0dhwYUkC1L0MO0T5-pU9Kftrt2lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=Qx9P-Q7gwkU5gzimm2sHcfY5blKuD7KM0efysyGWi9OJSsiSODmr5udBQW3nN3y2eaf89UccZnO4zHtdCs6n2NIz8ULncbh-1nQp21xkQJeEuTNXgrfxzRLbi9HCoRWRjaWsT8BuyxxAoB87sRM2GkS00_rii9Ja6ZsiqnxF4CpBiUvc_qMPjITNDAeTAKPLyG4OTsHFTGEW1nas_lr7lfa1LWjikl_UNXssOzb1HdMPT9h1_bOer7cWSUqDtMD34u2d8wVAGdErcdgPu_bhtRJ9aGl3ZXeFNsmQ2qdjG2DMM7wEsHcQRTBVjD0y53EikcVlacZb0ah8pamRwWbnSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=Qx9P-Q7gwkU5gzimm2sHcfY5blKuD7KM0efysyGWi9OJSsiSODmr5udBQW3nN3y2eaf89UccZnO4zHtdCs6n2NIz8ULncbh-1nQp21xkQJeEuTNXgrfxzRLbi9HCoRWRjaWsT8BuyxxAoB87sRM2GkS00_rii9Ja6ZsiqnxF4CpBiUvc_qMPjITNDAeTAKPLyG4OTsHFTGEW1nas_lr7lfa1LWjikl_UNXssOzb1HdMPT9h1_bOer7cWSUqDtMD34u2d8wVAGdErcdgPu_bhtRJ9aGl3ZXeFNsmQ2qdjG2DMM7wEsHcQRTBVjD0y53EikcVlacZb0ah8pamRwWbnSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=b2fEahconVuB-bVNyhq-fS03k4NdxGXseZbnqNWsacjKlY_ypGPVN9ICXcCw70VG3utog3XUf5FiaAnlgQk4f_le29sgPbX72afw3TbAwrBQyD8wPou0h3lZzkt0fZU4isBLd005yYOi1n3L1btCOBNNg4-CswRS1jIxv3nk3J9OI2eLlw81Ib20cl5GhOM2DlOtI7ebj8yof_Grs6SoSRO85nkT5hqeMBUmph56GyaGIDJrXE3OjspQ_0D0gV2_z0mz9h50RmFmi5nWOpKrex2LoicAyUBzpbdTFq_stn5f0IlQwEOnlxjQ8kojLP3Xu2qdPwp71B6CwVnzmAglIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=b2fEahconVuB-bVNyhq-fS03k4NdxGXseZbnqNWsacjKlY_ypGPVN9ICXcCw70VG3utog3XUf5FiaAnlgQk4f_le29sgPbX72afw3TbAwrBQyD8wPou0h3lZzkt0fZU4isBLd005yYOi1n3L1btCOBNNg4-CswRS1jIxv3nk3J9OI2eLlw81Ib20cl5GhOM2DlOtI7ebj8yof_Grs6SoSRO85nkT5hqeMBUmph56GyaGIDJrXE3OjspQ_0D0gV2_z0mz9h50RmFmi5nWOpKrex2LoicAyUBzpbdTFq_stn5f0IlQwEOnlxjQ8kojLP3Xu2qdPwp71B6CwVnzmAglIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=S8CEKt8bFqXOO-qyhgv3m2vsZ-DZy_F4iJm1rHVOjtseSFS6O43bXXmMwHqAoziMtpAomQKNEL4abpfg8K6xNB2QA4hnZh6kAA8gtCgkpfPKQR13weFLafiOfDNy38Zsge0-U6qHewBj92cCeuSsJias1PpZouhDDRAoBDxLPOMjKorhKTCHX-zPYai3WWRJJL51w0an0ewsfVjPgsoDTiwyoH5Pl4abW-f_S5ESiB_3RLHxWx1TTS2p99SMCJL3SUAwHM8PiAfAIOT8kK0nbIO0bdc6phYbap-gOV7pHs7pjo2aehDdUZ2h0UK8zEC64kbHeSLk6MZQIVSzdPERVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=S8CEKt8bFqXOO-qyhgv3m2vsZ-DZy_F4iJm1rHVOjtseSFS6O43bXXmMwHqAoziMtpAomQKNEL4abpfg8K6xNB2QA4hnZh6kAA8gtCgkpfPKQR13weFLafiOfDNy38Zsge0-U6qHewBj92cCeuSsJias1PpZouhDDRAoBDxLPOMjKorhKTCHX-zPYai3WWRJJL51w0an0ewsfVjPgsoDTiwyoH5Pl4abW-f_S5ESiB_3RLHxWx1TTS2p99SMCJL3SUAwHM8PiAfAIOT8kK0nbIO0bdc6phYbap-gOV7pHs7pjo2aehDdUZ2h0UK8zEC64kbHeSLk6MZQIVSzdPERVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=Vg61BGA0MDwfnnHkAKRGuAUpNaJabZZiw9ApEQSAghgZvj8c2pqZgc663eO5yz3gn9WIFAODYS9JlTaEx45BejySBEHXdKP2u4WlRAiABC3HbvTDmdoumNH_akh4P3PdMp93j8qoXbkUNy5ONAz5Egy9gOabEcI5-DZxd3xH2R8Frc6UeB5jI1v2mKnscMMr71P4J46glMyvK0Xf3Xfn-GFHc6L8XBvvMwcCM8LZ9uDg3qnhPvrVfT0FcS1KPazYRG7huRo_AFCr9A7l_cG8rmDs9Dt04dYkZwJ9CCQSABLvmW7r-YEw0CfPYhriHkktx1DM5AvwaCgGDMegHhmUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=Vg61BGA0MDwfnnHkAKRGuAUpNaJabZZiw9ApEQSAghgZvj8c2pqZgc663eO5yz3gn9WIFAODYS9JlTaEx45BejySBEHXdKP2u4WlRAiABC3HbvTDmdoumNH_akh4P3PdMp93j8qoXbkUNy5ONAz5Egy9gOabEcI5-DZxd3xH2R8Frc6UeB5jI1v2mKnscMMr71P4J46glMyvK0Xf3Xfn-GFHc6L8XBvvMwcCM8LZ9uDg3qnhPvrVfT0FcS1KPazYRG7huRo_AFCr9A7l_cG8rmDs9Dt04dYkZwJ9CCQSABLvmW7r-YEw0CfPYhriHkktx1DM5AvwaCgGDMegHhmUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=m_6J0Q6AQD9oAFNWvrLetTN29-xiTBFgajJ0wyh10uXHKTWz8zqsaDHx4hGvK8gHP-KxVFUfou1OJzXsBHEfqep4p3LFRU8qr_KiPZF8S8zLogErAG2f8h13B2RIgrtVS7T2ZQe5I7mQA_tkSV1IjQYRUA-jU6G-Vd27X2WJLp5hURJ9xTqUByPyBnMUNui-wgCyMW0VbQ3zD9Sc_1Y4JicKCWCYWXnpBlrrrMuMcTnF2XA7I9a7Ko2Q2DQg03VgdqA0dHhABJFAiqFdEciTlD-LRtQaZDaGbo_J57GEd-xYyJysWWraJtbua9F673EuLIEB08i_RdAfpmrXLeD3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=m_6J0Q6AQD9oAFNWvrLetTN29-xiTBFgajJ0wyh10uXHKTWz8zqsaDHx4hGvK8gHP-KxVFUfou1OJzXsBHEfqep4p3LFRU8qr_KiPZF8S8zLogErAG2f8h13B2RIgrtVS7T2ZQe5I7mQA_tkSV1IjQYRUA-jU6G-Vd27X2WJLp5hURJ9xTqUByPyBnMUNui-wgCyMW0VbQ3zD9Sc_1Y4JicKCWCYWXnpBlrrrMuMcTnF2XA7I9a7Ko2Q2DQg03VgdqA0dHhABJFAiqFdEciTlD-LRtQaZDaGbo_J57GEd-xYyJysWWraJtbua9F673EuLIEB08i_RdAfpmrXLeD3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=T81kybq6ODXFTEs5tu09qf_xynU7uz0M8gaUhe40vRjFOCC6XJ-xQuseyCY2PcZZ44jCeNhl8hNg9U_O_5mDGRjaY2-BF5IkkViLpqYkhwvBxFP-xrgPmURAxM0NChflzq4TMWNI_-NAZX7zY1IfiyBJ-vpax2_o9mE_42RRXVXh3pSVHdHnW3jpeV8hYThAKmFLhoTVYRWqc1hJGvNZjNdU-CSKQDmrPbUvrNahrYJRrdkrGBpLh3b06pCkFRnLri6mgQd3ylLOoiTPuj5RV5tMWDV1AdbEtxtwsOogs4SZyE09JhjS3VqTl7WZoFuKAgRjWc5f2NDW8kZP3uqePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=T81kybq6ODXFTEs5tu09qf_xynU7uz0M8gaUhe40vRjFOCC6XJ-xQuseyCY2PcZZ44jCeNhl8hNg9U_O_5mDGRjaY2-BF5IkkViLpqYkhwvBxFP-xrgPmURAxM0NChflzq4TMWNI_-NAZX7zY1IfiyBJ-vpax2_o9mE_42RRXVXh3pSVHdHnW3jpeV8hYThAKmFLhoTVYRWqc1hJGvNZjNdU-CSKQDmrPbUvrNahrYJRrdkrGBpLh3b06pCkFRnLri6mgQd3ylLOoiTPuj5RV5tMWDV1AdbEtxtwsOogs4SZyE09JhjS3VqTl7WZoFuKAgRjWc5f2NDW8kZP3uqePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGlBp-j2rhv1OBhFCOWk8i04JqQlyK2gO4enhSNYKXjphKtk2qPd5OtrZlQegGBK111aTwxzETR8jSOO3BXLqJf1r8tK53PW6Hgg36WuE9Yq9EAjkpMhxd3I9OVOR3og6H_4-TdsXrKVwxPm5D6FAdKoTZM-i6BlyVyZN5rRzEXlG0UX3tWYgc2M_HISxC1-H_aMn10xNuD43bsNdUivpEnmt27OYQ4gOYJjwZ5jBJtwfngcAkVrCYsOBSXRl2HlJ0KdnhehYZgHzSpqpiJIFCcyev-JXadCOc0oH8M_SpmL89F-mOjOJT87sV1sh7FqWF3B4F-uZZJohHiHTk4-Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpRGbqgIDF-3rR0TTC4HE0zbGDobuX-bJvlQCkCp61s2iuduZKzl-p-WT8VThlquo6caC8GErSCqj8Pp_8Jq4Itz8yMFGw1ghsGa6ikzj2ww-rX31T579me7uzRd9i2_nV5GlTG14dHujP91vlHVq8xtKUf0m3l-FGufbEtHk2as8qXSDt845mhRWc0K1E-RwjnhAvbGY-dibg_mGL3GksmvmKr7z6EQo96_0_JU0Gbh4PCAEIzQl6iQp8UtDNK6vHQaDi8zaE5lw2ANvY-0I9189JHPlIKC10Th4OMfH9eSD2NSFh5NAvNjHtgeL9-8yeCjYsrHU0RE1xeAu0C4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=DBaQwufxmbIbJsogMiG8synt4t5QzQup0Yck6z5vXSVbJi8YqwFQk4wh0tAnkuykm9t6EB8thlaulGex7BbxzkoNgW5mmP35DZWpJ6e7ttgFzDd2YGb1X1bBZ-kyG7RGqKEBox_mc1EdJbDj35GgIdEezR4SMd37tKCg90olwOc-xkDsfh1OcELax649yyO1Elg2heXcsN0UPNJ9XY_FAadudMRmMpiuot1kTjuerg72osa_DPorabMwXeWX-5TjwgU3bGLdM5pGLbDoTE52DKVsQinWg2vejcZqoPCcWuQEwR_iqWz36-MGWluqpSaal0-oCwo2Uk4nv87Y8rQt3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=DBaQwufxmbIbJsogMiG8synt4t5QzQup0Yck6z5vXSVbJi8YqwFQk4wh0tAnkuykm9t6EB8thlaulGex7BbxzkoNgW5mmP35DZWpJ6e7ttgFzDd2YGb1X1bBZ-kyG7RGqKEBox_mc1EdJbDj35GgIdEezR4SMd37tKCg90olwOc-xkDsfh1OcELax649yyO1Elg2heXcsN0UPNJ9XY_FAadudMRmMpiuot1kTjuerg72osa_DPorabMwXeWX-5TjwgU3bGLdM5pGLbDoTE52DKVsQinWg2vejcZqoPCcWuQEwR_iqWz36-MGWluqpSaal0-oCwo2Uk4nv87Y8rQt3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuvIA4xQD4Sorqoquag6gTHILnch47CmvHKg8bJX5QJsLsxFPW5oiQgdP2wSZmVf22AJafvWTp4IdtfB68rNIg2A5g7Abx3AOdFn6eNuE_38YHXZ03266K4kk1PqTri0cZCB0A8L0qxPQqfBVgv5JtM524Gz4zDD8qa7g4olRFivc-qWXkEFE3EOqhEb30FwwX3_s3-wgWTrzV9qgOox_zbubooz5sj5Jvdju5gVpn4S0_V3mT08jDYFs4U_D6w1IC4IUjgMB4cmHHgKm-x8v5j1Ow-p7DybZuYh9qVmgSUhc73AO94cttf4_APKMOLh7k78qr4KDzsiGdZeNAZhug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkstKj6ltYsPcxNYiihbj_rRW-AXgTCQuiXDXhlrmgPeHo_Zia3KR0fyXZMtFf2c_MHQDfoCmh-8L3qOYYqOcB6mC1tiUrOiRnBYOqYLpZs94krL19_Tl5Mlo3Fi3hrBxYFngwEqrtuhcUbtCIygKwdJrSEm7YV_mHuSHsxZYgXQEQmVA-kFRz3Hm6WzyWHeRyM6RvU70r-pvdgaW9N6vSDZyZ3tdKje7DQQG7Y-2M8ISj0hZg8jROYB9TmifjKIqUtOYwdKEC_P5slU4aLoiP9xzuoJmgaEn9jMo38Xl3dBdoaFGqAjfq1UPcQI-U3ZooiuF-ZrdXvXYW6IkRU0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=enwALm44JEcEKUPmo8EriOHy77KYEOZxhAB_-RpHXHylNYvIfp4vhylgOfeDnBZe42J9qIPO2w0g-0zZXwIVQAYlVM1yZRj2BNovWqH5xCpKGH_uZ41dNU9xhED2Af4n3GvKAaHE4GR-FZQeCfPe9Gjtd7G0J32Xe9YUwNj-XNb7_LyvEqf7j9KjC6Wp8Vjrv33iN_mthNEf7XRcVa8wEiUlRhoFVvHyjKR0jjBwIAqiG3ieXh5VXKvldC0CkJ49GOPg88pGizqk6vENw_CyJaHFYhtGoG06b5lXlXsahmx-RPT2SgHOO2-hgM8Y2tcootiU9GhZzOrPDx-xkviKfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=enwALm44JEcEKUPmo8EriOHy77KYEOZxhAB_-RpHXHylNYvIfp4vhylgOfeDnBZe42J9qIPO2w0g-0zZXwIVQAYlVM1yZRj2BNovWqH5xCpKGH_uZ41dNU9xhED2Af4n3GvKAaHE4GR-FZQeCfPe9Gjtd7G0J32Xe9YUwNj-XNb7_LyvEqf7j9KjC6Wp8Vjrv33iN_mthNEf7XRcVa8wEiUlRhoFVvHyjKR0jjBwIAqiG3ieXh5VXKvldC0CkJ49GOPg88pGizqk6vENw_CyJaHFYhtGoG06b5lXlXsahmx-RPT2SgHOO2-hgM8Y2tcootiU9GhZzOrPDx-xkviKfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=acO5I8pXkhaIN7xkjun8lheg1JTv6E_ajvktsvcJxtsWdputunx_b6-b1esqkn814_FNXl3xtY7ReisgwBiWE-raVX9g7DmyIKyGXTRN25XvG6XOw-n1cGv7bANunDutQfYEwzTs5hJTVZlyocdNBXfHYBpmLC_G_4Uhr1c1k7Ynldrq3inO-UBfDosZHFajqpR2ioPy0hvBWmMHurIi25ropFeDHcIpE7behQir5709V-4jXUr26FGtxSIOWlLevPktBy0FYRCSq3npxdAEq7sXYVBkejJeUMLuXXpGnZdjzkEQ9tnl8lq44cfH68XmmgKUzSRxQuRnDQcVnQWUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=acO5I8pXkhaIN7xkjun8lheg1JTv6E_ajvktsvcJxtsWdputunx_b6-b1esqkn814_FNXl3xtY7ReisgwBiWE-raVX9g7DmyIKyGXTRN25XvG6XOw-n1cGv7bANunDutQfYEwzTs5hJTVZlyocdNBXfHYBpmLC_G_4Uhr1c1k7Ynldrq3inO-UBfDosZHFajqpR2ioPy0hvBWmMHurIi25ropFeDHcIpE7behQir5709V-4jXUr26FGtxSIOWlLevPktBy0FYRCSq3npxdAEq7sXYVBkejJeUMLuXXpGnZdjzkEQ9tnl8lq44cfH68XmmgKUzSRxQuRnDQcVnQWUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=UG5x22rpi-sDjsDwaffI_3th4PMcQIb7otLvXsWa13EWr5szAwWnViZulX36JUJxPWRbW9b5KZ632hQ5CKrD-9ZKUx0qQnefS_252maUTV3ANcJapbIUNuqIyLTYT9GnQ9CAKgike3kQPiALeoqf4W6_gHWyvd2N_QyuIKJT0bC8VzRI2wIV6_EQMEv4SKbr7TaBxYTSJAi3PEdDh1Zyy4lgBW4tEJMtDrbdoGMsaz3ZyPbCv7f8mBGy0Y9MlXkcyM30mh5nzqitVfNghNjyLD_Az3JQOk08b4sEsmiwFktrVdlfyDWG92ZcwXwtgubaWBCsUpp_MFpZujVfsIwzoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=UG5x22rpi-sDjsDwaffI_3th4PMcQIb7otLvXsWa13EWr5szAwWnViZulX36JUJxPWRbW9b5KZ632hQ5CKrD-9ZKUx0qQnefS_252maUTV3ANcJapbIUNuqIyLTYT9GnQ9CAKgike3kQPiALeoqf4W6_gHWyvd2N_QyuIKJT0bC8VzRI2wIV6_EQMEv4SKbr7TaBxYTSJAi3PEdDh1Zyy4lgBW4tEJMtDrbdoGMsaz3ZyPbCv7f8mBGy0Y9MlXkcyM30mh5nzqitVfNghNjyLD_Az3JQOk08b4sEsmiwFktrVdlfyDWG92ZcwXwtgubaWBCsUpp_MFpZujVfsIwzoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nS7XGY4Akkt45ZC2LWfH5uo7xqw-kwRQbAyJRtBe2v5b1gdwCGAYKxTWpV7NVtsHrrBK2CI0VNYm7ApMjCtpLlXapVS8x4Vnm0aWS6mXoaZXT3UJVJMj5WgW1YMhDzTgoVpeF52V_vZKM2NQqqNQdc3HxT6GAZtWQVARkNFMgw_53d8dUIypgayASbJGyNt3TWjCQody_O4Dj3GsI0HNk0FkV6haqkksI1plD9rmRo3lk2PZf-PKiK1SXZQa-s60q6iociRAQfw8R-FLxVBBwDPZGXl2yIibpPx52slBVUs0iv_rB2qffWGbao3tIeskN7ZoC6GYbm5mgJQeVYzaTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq_MzHqY10R2YcX2h3vYKtKceLx783YeQPDzDM5nXCWtLAYt-XiQd5bXxDNfCiDV7fk3c5mxVH1OLnZ34XtwvkBK0gJMjcJ9uYFK1rS9O2TezELCrxPVz3yoGWMifpjbYNd8m0XzzQsprbJZ9uDEOs6AVkEsEpW7ak4z9iJZzloAdKTECwfiFWt15G61k7pMNoeI7-2v-hrCq3aMEWIV3apfMdpAWIrMQrV_Gh3c5RPF8hgS8P_mvpDbUd_QLdfssMIvwRPgc_ZdfYp16KUAm1do3khDoXcXt21Ph1DuWmASxeukvd_WM54smOIrbiHfaq-PjLJLtV0ej8nU8n4FDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=WX79CpGhWs4z_KS-7sknUNq9SpRzNz3P5SLBXj9emrdRZ1C555mZjY_FM-i98NJgOXazKilNwMutIgyXRM0iFyuJlMlykJCuY-GFNs_RdG6dk5VFH7VRHLurcxLkrUhkz89CYgjRV77zQnZZa-t8w4i5R7mGrvhQ1Dua4t5P40OIQ28VUc1nEYioLBkP5CRhGjeoEkAvy3PufaDpebkql7wyJoskZ2jRSGcC3fjs99ASMr6K85ng3-n8CG3X5f7cMFRcNJAlel2Ny1rFC2n28n98p90KSYO9I8k3kkHCIWEtGVGlJxc-bscKjusj_BWE5_ApQyYaOiZbdUlGkhO7DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=WX79CpGhWs4z_KS-7sknUNq9SpRzNz3P5SLBXj9emrdRZ1C555mZjY_FM-i98NJgOXazKilNwMutIgyXRM0iFyuJlMlykJCuY-GFNs_RdG6dk5VFH7VRHLurcxLkrUhkz89CYgjRV77zQnZZa-t8w4i5R7mGrvhQ1Dua4t5P40OIQ28VUc1nEYioLBkP5CRhGjeoEkAvy3PufaDpebkql7wyJoskZ2jRSGcC3fjs99ASMr6K85ng3-n8CG3X5f7cMFRcNJAlel2Ny1rFC2n28n98p90KSYO9I8k3kkHCIWEtGVGlJxc-bscKjusj_BWE5_ApQyYaOiZbdUlGkhO7DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=OtK1sy8cLIW6WR7FQ5CnfX7t0-WlwWvW7sifHabWNKXuCFP1dEzLJZmY8s3rE2QgqVHWh89uAZMFHxEahdN9aXSZUUy2VybCb_O0BbTUSabE1XEegbLwIvSDdMKm7mY6wLKX4mMv5vhBjJCzVmFxLdEsa1tn0nQFKWcTsOjX88VYXzPrC3Y4K_N84tJOWhMx1YuhxuL0Q9YhltHwi9Q5kJ3gcGiu92BGeLlZ2Qieweko5zCnnx-rcXZPUszDpyxuRXkz1RJ-weGBrUoNZG0qDR7b-i6eMQOVPHJdTEVJdgZy7SqZ4xJI5sKyyBCHmW9mO3rkP0_TjhIwis_SIdLNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=OtK1sy8cLIW6WR7FQ5CnfX7t0-WlwWvW7sifHabWNKXuCFP1dEzLJZmY8s3rE2QgqVHWh89uAZMFHxEahdN9aXSZUUy2VybCb_O0BbTUSabE1XEegbLwIvSDdMKm7mY6wLKX4mMv5vhBjJCzVmFxLdEsa1tn0nQFKWcTsOjX88VYXzPrC3Y4K_N84tJOWhMx1YuhxuL0Q9YhltHwi9Q5kJ3gcGiu92BGeLlZ2Qieweko5zCnnx-rcXZPUszDpyxuRXkz1RJ-weGBrUoNZG0qDR7b-i6eMQOVPHJdTEVJdgZy7SqZ4xJI5sKyyBCHmW9mO3rkP0_TjhIwis_SIdLNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
