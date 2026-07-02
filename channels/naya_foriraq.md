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
<img src="https://cdn4.telesco.pe/file/VvIezF4SPOsBFVdjVWcZcVTcl0Zw49RYuX0-nw1MV9OGMC540mEnEJY11p8ZaCiTeNj-hTNdnkyiZIk9B5UuLkfXpTIUF1lhO9EXqCJhFdbVykmWTm3hzI00zHwO6HMHBzCx9M0dpfEY4_RVJe6e6q5JlDRV-NKclSIkWiq1Ui4HXBe0KD7qjjGvXimLh6areh5xlk1ZR-a_EDNag1f7BDVloq5CocAdiAJL--_ON18u1Y5koaYMKMFws77Meogbshbo3I5ywczKTIREXq97Hw0t8fpLvSeiHUaw8PwroWCFtrBZK0ZeIOuL-ofMlAD3JKHWEfQUfQijSHta1o5tcg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامب: «تنفق الولايات المتحدة أموالاً على حلف الناتو أكثر بكثير من أي دولة أخرى لحمايته، دون أن تجني أي فائدة من ذلك: الولايات المتحدة 999 مليار دولار، المملكة المتحدة 90.5 مليار دولار، فرنسا 66.5 مليار دولار، إيطاليا 48.8 مليار دولار، بولندا 44.3 مليار دولار. أما دول أخرى، بما فيها ألمانيا، فتنفق مبالغ أقل بكثير. (2014-2025) أمرٌ سخيف! الرئيس دونالد ترامب»</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/80572" target="_blank">📅 15:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80568">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeLsiygtA_6PXeoErY8CFotcgarBmoNzDxEVXudju4yfGMzZZWSgs5tMuAEpzl9XZYOIkjilxxT2olhvd6Kou1nAE4reoJsEg43Auq47dCQx-xCnDdmrfd06sZLRQqTFaIHF7BKZt4wZWnjPZxzzpz5bdkKqwPXxKdvxxXOy4lmnmoVKPtGr-MWd2hbLvT5SfbFUNml6BQ944FQ-BSyU6_jnFa5bh8F1iClBue7kGuiiMFvM3BNPIjcVvBF153Q3Wg-vS869gSQU8GFoW1aKom5DOLSLZOP-tjuWPu4yvKw3NtsU6aYXvmjwb6HhtzUwnt5ruARJzgJA5RS5tSyOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWWmbVO-YQiWcJ-et2Eb0S1UUaeMWTNQQkEj04OzSqA1GbMfAhI47qJTWzifEtNquU0RTsyoUOtpBVR2V3UOX7fvIl-2YxOD1o6eN5ZGdLNBx6C9xYxQ9gQTFawwnN-9UBtvb4umWNq2gQ-fXYhI6n4vEktZAFrnZlL7yT_AofXMmT6zapv1IWrokxp68HoGPoEZMl5qXuy5X3zB60p0oTAB6yTFOwP2aqqC_fcMTcq45nfVzHboequRsgkSTmJwCye0lQSyYOfVi4Dv8KJjx9Dj8kIIEj0HY0bULutjt8pSa6qsjsHVtgEmF4b3i6Tnp__xBnbqlI9pOlwiFaUCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRbGhoEWpNICAMsiK2t7gq4BM0pVn3Pv4mQ_PJq7b3XOGuV6oYfbNgZLpOcOLoYXwwec55VimdPLHLf6X31sHtO4uaNRKsTZOirLJT3VsE3q0PqoT4ZVP7LaHX70CVE-rJ4qTUsbn1zW9kAxVhyE3eG5BbSIdSx9GGxo3gH_fyELUel6epftfp5mkSnKQ1f6_IkCZwgGPsY4aAVFfHK7Kba2uyDCHOWI86QG7Xgt-8vzVk6ka1Dqh8eWwm0ITKUM_n3N81_1PlOf0YHlyK4wJiK2z5Jo3dL76rfTy1bPOQlqEO2uLRQWNT5qF4BwHfkrqUJBSXmNhvLLd4oTbJz7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWHGpX9T_9rjklB468HOKyJOB3VkwMhEreRN3Af_5ZjkWwUZ9dx0TvxXGHHfPrxfUafmWoSiGGZcdBYrFlb-m8j-vQPeb5Qj5GED_HNPBEaMIFyHGWNat0hq3EHB4VrCICWZsqj-NP_w619TOfhkKdhdGsy__YHLqEwiW0GuqOHDLGeKXnTjujrwSPfXM0SFDk6aPuzdR10WWhbG6oMPlvIblM72FPGowmXWh6ZAJnBAT8BXXY8cFV8zMNfklfZpsY_2Ua19NYHGYAyKFRUVKoa7nWrZ6Hoh1Zt8sFLaRXdnmmkBfcAXfyLGguBwx3qASLF3H29i-hwJOn2x9U9YDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
ضمن استعدادات التشييع..
الحشد الشعبي يواصل استكمال نشر المظاهر العزائية، ونصب الرايات واللافتات في المواقع المحددة</div>
<div class="tg-footer">👁️ 35 · <a href="https://t.me/naya_foriraq/80568" target="_blank">📅 15:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=M8YnHFZXVZvmk-DJTyHyy3lk9VX-UCA4mEHsaHDyg-Tnz0Ga5nlhnRo6BP84vv1hgAFT_T7npAJaRgF-uCqhD-Nf-yfqm_yhDTsbCZhjHYEM-dG-Qwgk9pja60eE8VVUB5RiGL1onjqEmXhi7QfRNEkEbXChLYA0PE12G1I6d9Xi6Le1zcIjHw5R2bYtxzVFTXlx1cZ4x1u1bQvy1mfopx8X0HDpDgt6xyxr1aQtW2pPg_xUZwT-D_U4bn3UFc5IY9LJsBDCuD6lyd_RCYR-m4fEQfvHmI84GsJ0V0E4dmy_c4Ei_FskIG4NcnfpYkdLNSi5_pnqIUgfabzYcObkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=M8YnHFZXVZvmk-DJTyHyy3lk9VX-UCA4mEHsaHDyg-Tnz0Ga5nlhnRo6BP84vv1hgAFT_T7npAJaRgF-uCqhD-Nf-yfqm_yhDTsbCZhjHYEM-dG-Qwgk9pja60eE8VVUB5RiGL1onjqEmXhi7QfRNEkEbXChLYA0PE12G1I6d9Xi6Le1zcIjHw5R2bYtxzVFTXlx1cZ4x1u1bQvy1mfopx8X0HDpDgt6xyxr1aQtW2pPg_xUZwT-D_U4bn3UFc5IY9LJsBDCuD6lyd_RCYR-m4fEQfvHmI84GsJ0V0E4dmy_c4Ei_FskIG4NcnfpYkdLNSi5_pnqIUgfabzYcObkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالات اغماء في صفوف المسافرين على متن احدى طائرات الخطوط الجوية العراقية خلال رحلة بغداد - بيروت بسبب غياب التبريد والاوكسجين طوال الرحلة</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/naya_foriraq/80567" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VJyO0B8CpaE5pwSU6WXFLwnAjspqWG593nYHy8hkk4RIgMc_Xj-E08uH-vnyLxIOFdgD3ky4DhzDBmJqXfBRNiPxyjqsFvbA-VsCpCe-Of5w59fQG7UP9yPa9yRIuPLWS9eYL8qgWKj3gfwpA3yf2iFLV_tPeObIpBbrTMsRbMFdGPzdM_MtsQbD6SIHuidxSFKdyPCvDfxxq7azx8NwTcVG-GCzxfGOq1LBKErtqQS8cCI2OShYrNqc324aI4N66LnjNEf6p85_1UEjdcQ7AdpdrtsAo7BJSyOiEsWZe7yNgQgJcluJx3iWPTsC8vhjqF5uXZY5dHt_mtIK7sLeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VJyO0B8CpaE5pwSU6WXFLwnAjspqWG593nYHy8hkk4RIgMc_Xj-E08uH-vnyLxIOFdgD3ky4DhzDBmJqXfBRNiPxyjqsFvbA-VsCpCe-Of5w59fQG7UP9yPa9yRIuPLWS9eYL8qgWKj3gfwpA3yf2iFLV_tPeObIpBbrTMsRbMFdGPzdM_MtsQbD6SIHuidxSFKdyPCvDfxxq7azx8NwTcVG-GCzxfGOq1LBKErtqQS8cCI2OShYrNqc324aI4N66LnjNEf6p85_1UEjdcQ7AdpdrtsAo7BJSyOiEsWZe7yNgQgJcluJx3iWPTsC8vhjqF5uXZY5dHt_mtIK7sLeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من التعذيب الذي تعرض له الشبان الاكراد على يد جيش الاحتلال التركي</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/naya_foriraq/80566" target="_blank">📅 15:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80560">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BslYbU6IV0gucLOJ4eVc8p-XZZ90DiunhIpEhskOOziU1XfAHLuKiOOhoH6r1C5wYwNsoyOb6Isw_KUtMwzo0HMDRGe-FdG4i8QygK1Gm6-3txfXkMGi6FRWViaA6TdnRS_T6ZlnJ24nT1HMZ20GX23k1zHil9PPCwDy1LSnJMIvtm5TEmICKZqa_Agx8dGNRGJ-q__M4lYJZPndHZfL5rwqTxDeCOZeIVH9-zNmbbPsX76uIVHpalnUqW-DxAqqZkYgPjJiGmhZHwnrFA42s9F0THiHbr-tIxxk_2NFaD_AR-khTYLNzG3idIiOKwdEIiI8QwFVhdzMF86XmN_CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUfR_9vW7dnPwMm8W-BcPGEAj0I9eDUI0ND1UymEJStAatzs5ns3JEQaYKxw03VAnu7kpr7CR8cjTMkYQ1ZJEwFDRB6fpKqbt_ZjJXZP0T40Rn7l1NKZ8hxK1sLuZxYW1m6_XiSMhsCCClTty0nIb2OPEPkPi5nLA_NgRcKT7qP310zMRLjgFlJQcS3vPTTeT_F6K4pSoEQhwMxoAZa8yc0-zFEujSRB9K4Zsd168wp-2ydZtc0E4XFkJvNURUQpN9aG0sf5N23Totr8EViEvAJsnkwOtOEgQU2kuf7ZNlCotra9xU4vrjAI-KZchHuu-q98vEso4bUDOcDsQ5esRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQdo4A7QUWJj1m8WNh4enrUgcSTcBrv5ejXqDXOI7ph_9IjG6qu3X2I-W5CompUbHl-X5BD-fX1OXXwmhc4-3LX2Wu8txgoorfAM5PZD22EDvs41KDav428-jkiMPkj2ALZLcgcRp0HUCQKQKdG5unEr1GEpo51_oXZVExRZH6eUBB7oQ4VsGYBeH_s7_Pumi8hM9UuYEzjkE38mPjGRrIaZ9pH8V-A0VFs4vuHSitb0hDK4ognSPhCAQCDyw4q13ANre9k5WgXsBR-p4TUXDYh13cZhsQ59d6aiJ71TgreY6HZ7ImHGCjTuy59ttzKyoUGUZSNWItaz-kZacT1v-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdwbCO_F2AL5hIokYC83Ype3rsjB6RYU2qTbN1rbzw-vHG_KEyw7x0ghhkRn5O7OWqqlzgx-xZY_RsZUi_IKUeDUwNiEKgmqWMlGY64fOjWArJsNMa6mhkW8Ghib60rQVnjGu7-y1QnGlefYxyvCGHVfx2EqPYdx-CACKUMhVcCEoQv33BpPryQFE_0Yv2UQvtjTDJnjERLgvKb2fLdF6HUAMSNJb0dwMXtMVTOEWSqBRkXUmmNmbjH06b-oCnh-pMz8TiC1IQLSdUeaxIvhz0ZjJXVGJepwUtDwkSXwehkHFWPhjQ6fMpFgjv-sUV-U2KGqvKKzhBKewyoar4F-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUMO0m8g0-X43SNOkGVqxlPYEk-uQkKQaT26OI5WYYxM-vS9mIR7NEMGCzUgPDNkzaBp_K5ybA-a3cVrT0xASwRGGOS9Z1MAd-hkHMWt6DdZ7MLrN9L0AjHtXxiKJVO0_chha1C7noaJNymj3wTbqOQDdQR8aEdeNVdWFvY9H5y3Gime3t513qWu0ZVhX6tDrWFzRuN4ufWuKDIyBNnyQJNPOXyNWa3fE5KfDTu7hx6jy5sOZXZyWbNS5Xp1s0-5eYLjpXWmXj42NikH5WckBq5BlhOfGxDlBb5h5g1IO8eWlcs6ZRrE1q0sXp_tmTvWdOodu3BQxaunkXQg0z8M3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P74J4qZx_TRJjVpaA26Hz1Rskkv543aLJUSFtB02qiq1osDxwDRzU-1CjTJX7zHbUYgRQMahWYF5PmF5UGLBnTELAEtsvHWHs6U3qiiXU0kFLWDWWgE2VBksaU4ki-NxCikrq3-YfZ6QuJEMJc3LDc0D1MBHMWYT0M6wcFqnU2LdYAzkpcfpJlM-ClBLZP9C8n98uKtBKflUrUSWDQphz-7bPgiI8IYDKVCUWHinL6zz18cRUKWS6_v7_sXSVrBtRQnHxo8PaWnf6HydlcIJbbnuVxe6-t3YmIdluTZjWb1OWhjiRe5aWZL9NJU7peoYaATuplC_4ShF3t4lgG3ANA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جيش الاحتلال التركي يلقي القبض على ستة شبان اكراد في قرية شيلادزه ضمن اقليم كردستان العراق ويطلق سراحهم بعد يوم من التعذيب</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/naya_foriraq/80560" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80559">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">توقيف الإعلامي حيدر الحمداني في كربلاء المقدسة بعد شكوى رفعتها العتبة العباسية</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/naya_foriraq/80559" target="_blank">📅 14:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80557">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
أيدينا على الزناد، وأنظارنا مصوّبة نحو العدو، وآذاننا صاغية لأوامر القائد العام؛ فبمجرد صدور الأمر، سنخوض الحرب ضد العدو.
المفاوضات تقع على عاتق المسؤولين السياسيين؛ وهم يؤدون مهامهم.
التفاوض معركة تُخاض في خندق مختلف. ولا نواجه أي مشكلات تتعلق بالأمن.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/naya_foriraq/80557" target="_blank">📅 14:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvZMyi_YRqpLdTh71RF61RDFEzaqSgacGXiMf6CdFp7pL51Lb0YaSHNZ-P_2nesirHVPuIf-Gn293AQ38j28ylFA2saYJ5zlh2GjGbUtFoJuikssIzmDacxgLaqku_p6qh044srF73Op5JHiOhL0IPs6fpeSYWuC2qu_FaDeHaXr8-LGAxEfAFuHQIpN0rN20_jzI71nzY9l3lR2RgkjjlsNcJ055SGJ9b6uewOyXncR5MeKwh519Kk4qAn4YcVrPbF5waxed0_XCGSWrBiNjtuIEvGxpKyr92tEM0qokNzFn0hwZvF8PvtS33Pg032sZrXx3wr5HxVvIPK7inM7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
السلطات المصرية تلقي القبض على الرادود الحسيني العراقي السيد مشتاق الأعرجي إلى جانب نحو 50 شخصًا من جنسيات مختلفة بينهم عراقيون ولبنانيون ومصريون وآخرون أثناء وجودهم بمنطقة السيدة زينب (ع) في القاهرة خلال احيائهم مراسم عاشوراء.</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/naya_foriraq/80556" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufPa0AFIf5J_u46Hkbf4bYSoo9FSARbiIKUA6P6lX1ZBI_K4BB7_dZi332t90jsp3AiB09_i28Ck9Rr4x0QfkTQHqiqvfrpOHjeQL2I4pBzswWLFhjVXvggtCHLDInx0_fkghMpVtmwV585zTyIJKNcv9-QQO2crGCsZnoQUSPwmI6jAdz7PSS6PoXxVRvEBWSAzhMcE_18AxSye24zRrw9h3KAUHlJ-yyfH0yLBcu13p6DQmsVg2zskbmiDPiwqu8sDd1k6LwcZItX5bO3YhQGrudQtwbwbQEuoJqiZWtlMFVeh-I6SlSixEWOZmiDTCnoxVgWLWqn0itTA9frN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
محكمة التمييز العراقية تصادق على حكم الإعدام شنقاً حتى الموت الصادر بحق المدان عجاج أحمد حردان التكريتي بعد إدانته بارتكاب جرائم إبادة جماعية وضد الإنسانية وأغتصاب وجرائم قتل بحق محتجزين من ضحايا عمليات الأنفال.</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/80555" target="_blank">📅 13:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
الجمهورية الإسلامية الإيرانية تعلن تعطيل الدوام الرسمي يوم الثلاثاء 7تموز في جميع أنحاء البلاد</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/80554" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قناة خاصة باللجنة الاعلامية المركزية لتشيع الشهيد الامام السيد الخامنئي "قده" في العراق
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80553" target="_blank">📅 12:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80552" target="_blank">📅 12:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">▫️
سيُعقد مؤتمر صحفي آخر يوم الأحد أو الاثنين، للإعلان عن تفاصيل تنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست نفسه الزكية).
▫️
الاجتماعات مستمرة مع جميع الجهات ذات العلاقة بمراسم تشييع الشهيد القائد السيد علي الخامنئي (قدس)، ونؤكد أن جميع الجهات…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80551" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
سعد معن: التقديرات الأولية تشير إلى مشاركة ملايين الزائرين في مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
أُعِدَّت خطة متكاملة لتنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
نهيب بالمواطنين الكرام التعاون…</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/naya_foriraq/80550" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/80549" target="_blank">📅 12:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z92xlGCjkiVp_HX2AF5kJ4qr8Jak0DCp5Fk9Rpswzv7zJGyymkj2-10GFyVNtWREx7KP9nK2tjiGQhnDByq6JG0GJV-JN4ThwhkRrihU12mkgTFpiJDgbC5qKcEpJMeW4JcqKIn5GuEWtvDjul5xOYs69F-GVvMw389nYF6BLBDnTQ0cPVs2Fkyol-iQ6J1EN3myEEeUo2BvPFnZNQ9O3UTtT331ry2HTYLcI8m2SVksrXmZdCQIrwEfc0I72JcEhU87HI62mTjhF1YEQFnSKGvlugpwaAaTR_bcIxPILGzPZzf_KeNwKK6HWW9W-vpxhlt2YEbNo6bB0WycUoFg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/80548" target="_blank">📅 12:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
الكيان الصهيوني يدعي إلقاء القبض على مواطن أجنبي من طاجيكستان يحمل جواز سفر روسي، بتهمة التجسس لصالح إيرانيين على الأراضي الإسرائيلية.</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/80547" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
ترامب يُفاقم شعوره بجنون العظمة.. حيث نشر مقطع فيديو تم إنشاؤه بواسطة تقنيات الذكاء الاصطناعي قدم نفسه ك طبيب يقدم خطة علاجية لما وصفها ب"متلازمة هوس ترامب"</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/naya_foriraq/80546" target="_blank">📅 11:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7UeoaUU6_BXJf2zRL669rs-vLHKWs4ZOA4wUWwnJ5iTmZ6F58oYmrB9aVTUiyaZCgLsCs4AQ1vBLzxz8JreNgBPSBGVxHEL46DeiGc4Hj2T2f4SheEvqbAr6eBRo-09Ej5NKxYs3iCsV1i66WCyXWSWZqE7vLGaAeL4MmoWYVP5RuvBD7Fb9RZnfm5wcI3A9vG49qfB0mnyCOOMDzJeSETqCwDOPNwXYzUPTrwsCPUAfRwOdUjbhKxV4Ku7PD9XN5Ip8YSE4Y9gctzaReL_0T2Ppz9Y4WdzontX0eywA0YLTzZCynjEcELf5gLRHg9ptvv4WqCO7hj6hFJzSGBdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNGx6ZZMpTSMKDHpgn_fiXn1hs1L-AI-XYFHRE_0Cm8OzxccW5Yag6JfReI634FhPHxwdtFL4hx-hdBXpEkAeh8hMRBsf_bSvqK_QUv8eAfzL6JGnVNeCwmFJg3OcunmcGNn6Io_VeaTs1rGu5caXA9a57LxmXAimz4cfJl5pqRt_pC4ekimPsADqMpQseHTaou8RTHiX0L9MtXjn-oIBMg0eLFXGkc98QE1P81HpR6OyzXewLZJupEjbdC6DBAlqs_1a5PWgppg90oEi_PcMJw5oXqH3BtG4l7isn2Spgl4zaF5KWqQuuil-6e7XnjXrHjq53G1YUQ6Oek1EBcDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ma4sYSpDfHiOzHB5kqRy9TVC8iZM23ItU43YsovXwZEW86lEsGoSXeUQyrH0JWbADquQiLv04cSb6iwZZmdyYI1MyOd85XcaEjpAISR1R1lz-VE-wfBcJCTUYv9KAoSvO1grrJHgZAY0JskLEou9K-oUvdjEOWZeugoB3RCqpdnHF4hKPt5ecbxDOcQE8UfMfrpQ4UrHZGJ8HGHeCaFzYE5--i4AgD3QN36vI7upWxEu2QlVexroidaFl6IBuHeNwXeyk-7O6MI0KJKTh-AN4zu0vtQnTz3US9vmvevbHQ6usrc0li2QZVBny1iY0uc56Kr-Lo3WuGNOSxps8NrRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbPFNWpM2zosJu_imCHoFNW3TsqiMkjTJ2OBn_7MV84muwCDeVmmEIBZXvOBx9xYeWxiXIshrNEhrTtbW9iDKPG8ijlGt7EBLA_GeGB_zR0s_I_KvT3nMAguaa9K_RQOhAdlKbjbRm0q65XbCwc_gOlIC7GLclCAg9l1oZt3aL9BcYTxhS6OeJWCn5En4KU6cTh62LzMHpNAtPiAanIMcDwyIuufhLcaniGt4D_EDWzJ4JV0Bhd0yC3uH7B90PC1fvOfEZlWLhQYx4VhmzTxVWYkic9A6hxnh82LXZrj3Z1X2X9o7ZTPI2GO94Pl8sOKLIgAhw2QjxYT3hR0XQ7kMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد من مراسم وداع المعلمة الشهيدة زهرة حداد عادل، زوجة السيد مجتبى الخامنئي في مدرسة فرهنك بطهران.</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/80537" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80535">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN5KPpI7l-V_LwowglULroqBeobYW_dPa1AyoBM7blTo-1mMfKMmMXbc-a-6f-baj-olLlfxsoHMTOXa19mUaspWFiz1LGoQVR8K8EemanY5ifrsCSk7_qolph546cgiGymqpautSZ9r35mv_iKym_RkGHXfo_e7N9wg2A6buX9F099GiIgwREMCPluIikm2T47Ut40pJuAms3SJoDmjCXR6CwgkA6_bS8D3FhmUCgFRFxH7XM5-1euDUtMrLFW2iL7xHwz6CHGEwRdbXOTsedGm04n29wbomW6IEdtIO6Tx-LFxY81Nz2l9ptWqyS4fLObZ8QHdJ5I0ZOB_EPgvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عصابات الجولاني الإرهابية تطلق قذائف ورمي بالأسلحة الثقيلة والخفيفة في وادي بردى على الحدود السورية اللبنانية بحجة التدريبات العسكرية.</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/naya_foriraq/80535" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
رسالة من قائد المقر المركزي لخاتم الأنبياء بمناسبة مراسم دفن قائد الأمة الشهيد، قداسة آية الله العظمى السيد علي خامنئي:
▫️
ندعو مختلف شرائح الشعب، ولا سيما جيل الشباب وبناة الوطن في المستقبل، إلى إظهار وحدة إيران المقدسة وتضامنها الدائم من خلال حضورٍ مهيبٍ وفريدٍ في مراسم وداع الشهيد العزيز وأفراد أسرته، وتخليد ذكراه ومحبته للمحافظة في التاريخ، والإعلان لروح الإمام الجليل أن أمتنا، بفضل تضحياته الجليلة
▫️
أنا، مع جميع قادة ومقاتلي القوات المسلحة للبلاد، إذ نجدد عهدنا مع الإمام الجليل والإمام الشهيد للثورة والشهداء الأعزاء في الدفاع عن الوطن، نعلن استعدادنا التام لحماية استقلال إيران الإسلامية وأمنها ووحدة أراضيها، ونؤكد على الطاعة المطلقة لتوجيهات خليفته الصالح، صاحب السلطة العظيمة في ولاية القيادة والقيادة العامة للقوات المسلحة، آية الله الإمام السيد مجتبى حسيني الخامنئي.</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/80533" target="_blank">📅 10:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2095ae6f9.mp4?token=lRRTjG1SK3-1rOixoDSVW01nAv49UfRP46B8eQZVXUI8nWTr0ObISO-Mtk4bpqRqYb907W6QCAlEX7BB6lcSwitkHC9pwChU1zbnZrRQilY4CjBXmqyuO_vn3q0hvOww178AyFAx_dr0vq3sILCZrCqTcr8G9MX9-xVV0YpqpWsNcKJPQfC2imTjqZ0Id1bne7MkCvziSwkHwB738L4vr9L_gjuiC5FGd1OCYLcNyEBTIFCp_KGaArNuIXwrI3BtgjQG-SEfi0PSNNYfm5hQCFJTKxvbLTmgh9jzycToF-k86FOMYKFVwqVA0ASLmibRGM55jdwBljPbZLjhyf-OGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2095ae6f9.mp4?token=lRRTjG1SK3-1rOixoDSVW01nAv49UfRP46B8eQZVXUI8nWTr0ObISO-Mtk4bpqRqYb907W6QCAlEX7BB6lcSwitkHC9pwChU1zbnZrRQilY4CjBXmqyuO_vn3q0hvOww178AyFAx_dr0vq3sILCZrCqTcr8G9MX9-xVV0YpqpWsNcKJPQfC2imTjqZ0Id1bne7MkCvziSwkHwB738L4vr9L_gjuiC5FGd1OCYLcNyEBTIFCp_KGaArNuIXwrI3BtgjQG-SEfi0PSNNYfm5hQCFJTKxvbLTmgh9jzycToF-k86FOMYKFVwqVA0ASLmibRGM55jdwBljPbZLjhyf-OGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قائد الحرس الثوري لمحافظة قم:
تغيير مسار جنازة القائد الشهيد في قم ؛ اتُخذ القرار النهائي ببدء المراسم من مرقد السيدة المعصومة عليها السلام والتوجه نحو مسجد جمكران.
▫️
تمّ اعتماد هذا القرار، وبإذن الله، سيُنفّذ صباح يوم الثلاثاء الموافق 7 تموز، وفقًا لظروف ومتطلبات الوقت، وبعد وصول الشهداء والحشود إلى مسجد جمكران، ستُقام الصلاة هناك
▫️
تجهيز قدرة استقبال تصل إلى مليون زائر لتشييع الشهيد السيد علي الخامنئي في محافظة قم وتم توفير جميع الترتيبات اللازمة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80532" target="_blank">📅 09:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في منطقة قازقابان بمدينة بيرانشهر شمال غرب إيران ؛ مقتل 6 إرهابيين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80531" target="_blank">📅 09:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عمدة كييف يتحدث عن انفجارات عنيفة تهز العاصمة الأوكرانية كييف نتيجة هجمات روسية منظمة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80530" target="_blank">📅 02:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTui2LENI3x6TbnaRMe3IiaKU2fyZzVc40dw-ue3LeURDTxygaGbTewqv_VyrW6SXNRuNLxEXv3ZZfuI9A4ewFmM662nfBRvCk4R1O-EHpU-9kblu5t_P-GREurae7AgVVAAX-9WNweRA-0sauEflLbzcqf9pGq1QlITUTMDcAbe7HeT3acrmrI90oAAt9yiEwXHsp0vOGX9CANEhh_jIfYOk2jNo3QOJ0oSNsuA5v3JhozdNi-4LI3Ui0tHc7ER1bBNNGfjXWJ9odIYGs1CY6G9Pw4JCLrAcD3xgldXHNqF5ZjFpcg2QlzSo8E65v8_1eK9TEx2AcpfemlwzZu_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKhslfBjoH6oaoSKPlwrmZZNinkmS9mD1vzH4i9Nri2GdfwTP-yMo2hNTWSVVqPLcSkfHB4Z4AJm8fKF8vKZIkxCGyxnox_5cj5K-J_ztpJ6rPJXG7Sa9lHH0buPbuBU21MPsViUq2lCsHPtucqm5M6xBCUvX9ePRsf9aMQgHTjY3F0HTkaho0u8n50SdffbitXdHeAXKTK40G0luxIPQY7ow2kd20rghfnDDfijK33pmcV3wPJyA7wYQYZHRe16xNLGH1EOUILiRKiYGGM-rp3FI-VVvYeeyYstKWjFy4T39PLhNf4tm1OXPfEYTEhzq4D-yqR_d69w2JqaH6EG-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
وصول قوة أمنية كبيرة إلى محافظة صلاح الدين حيث فرضت طوقًا أمنيًا حول منزل تمهيدًا لاعتقال عدد من الاشخاص.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80528" target="_blank">📅 02:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek_c_hnrhye9GNRmcZ1J2Wj_1DB11vxiR2JpCwGdQSLIldcZcUO85hfokp1ShIJMM9DzMZud23Gmy65aNdzfIDSN3I9NmjrxMGp7CCgDwtoJfmlFV-RZDL3yISWsNMZZAI_zzm3Gl-qPZ-bGZkf2eL-bK_IQtjjUBY6cOzTdXpDhF1YAGZozTLcttLmMQnw_MxeEkb3l0hJ3Rz2V3Vx1j0zrMOO7VOjx8bYZpcge0fPnWSZO2DchAAVLOTB5f2R1WOYKeD8oSFoenibFd-W18SgfwJpAxmBLmNoKb653A3BPUzaiiikDs2nm1uWvW7-kQraWFM5akQCr_KkD9p9Veg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد ختامية قبيل انطلاق مراسم تشييع السيد الولي من موقع المصلى في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80527" target="_blank">📅 01:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80524">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J-xM8gWZoiEohM40wMgHO_6BVsiIQfd2X1sJ_bXfCeY3yOBhx4RuqjeXxCj848FFal6ktp0QQkryuB7Wjv1F2kcH4cSyzkfyvFt95JlIlxZzGK35DWRGDCnXpRBooh--5rF1m1VZgNGwcj72Q7DIjFrOUbmUtniwon4abxD1gWJ9V4LGMK8UOvVrgqOROYe8rIIzXg4x3EByoJoY1sQKi4jJuVjT1-cY2QhQ1Cs8eefJG5oB37SIdTdtzCB_WeF07N1ZUS1z0JWrljEMYyagboZgrRtY3eKba_2MUs9ycTCRBUwQsIutrhejCidenebvVI0puKhpajUNmLJy4CR4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5ddKg0L-5ni-xvm7GOQNYU65xFrv45zVFWLvlklJIWwZ7tKTMSxc2VG0_a9_bjPfL1MpZ_jffQWJyjUOmEgJYTZTwoSNIrK_6tJQVooHxONoYmi1DqNH9gCsEo4ksbURBA7sAn1b4ZmBwl8TeOpfd2nprtmnpGaZ2m4QZjpV0a-j7-ANOWUfRVNIErJIblKlE3C7_BZG4tzwQZQevvKYSfD8yDsXXcMOmWbFEMYODU7CIApjlsBnn99KPxVG0JyA4V1z5E4VwMdFcBfXgz57m67eGYinZEl_yqv8larE7olbcyoEx-eGcn7JLKT2kxm_zC2zpTz59oJ-7jjZwuZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbWGj11bYTDyvt9wTNujW359ZvuuUJXYh2m6JTtJkfGZvXjax78PjEUHrqZKUluiEbKKCj76Nk9jZD6oy7G9MOZczLqtuFTKCbXcHFYeFmbRt2FBgZXKbzvIM7ZCqirl7kw9ihj5iZX-Ap9q8sIj6wR1S25sflD4INxuxQXcaf86MHdByiwns4sRToBFO1Ul88XGBYqPTQCmVnJAqazmCzmF50iMWftLhO3HXG-0WOMcLPwxjXpzjGmJdxfhvla7enfWXJWcyve0XmF_bUVASQEuOVnNxK3npWbEG84Rcs2DK4GGhH7GC0MmV7_xw2K97j-cnpkN2CwAr_8DBMfROg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
سقوط عدد من القتلى في حزب الحرية بمحافظة اربيل بعد استهدافهم بصاروخ باليستي.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80524" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ce18b1c2.mp4?token=Y6OKOjnjBkoHqX93ONgpAv_0i_VBOuVFcHfwoqjD26a7AV96dK80ruxTVXRT7H1QIm6sZXT-gIGT2by93l34WlcaKXiOIE1JbQIHLvQH_Z_p-esKc8Ho21-sYrPHM-CUS3HZoT3UY8T25xubWyroqUUlINo9K_C-1Q4MN0HNhRL3nxU7vv7ZV0Wq55vTPHDrHPEel-t-3fVaj-Ekak0gHqn9amqgkazGreR9tkPJG7X3-9IWmJfPxO_gFg7ES383n7KqJWUOHSACZhI7dE9WbcrlkkSshAJemKTDaRd8rXFIjSt96y2TzRgqudQ-ZbQT9fmMC6CIFGW_JA1SlR5imQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ce18b1c2.mp4?token=Y6OKOjnjBkoHqX93ONgpAv_0i_VBOuVFcHfwoqjD26a7AV96dK80ruxTVXRT7H1QIm6sZXT-gIGT2by93l34WlcaKXiOIE1JbQIHLvQH_Z_p-esKc8Ho21-sYrPHM-CUS3HZoT3UY8T25xubWyroqUUlINo9K_C-1Q4MN0HNhRL3nxU7vv7ZV0Wq55vTPHDrHPEel-t-3fVaj-Ekak0gHqn9amqgkazGreR9tkPJG7X3-9IWmJfPxO_gFg7ES383n7KqJWUOHSACZhI7dE9WbcrlkkSshAJemKTDaRd8rXFIjSt96y2TzRgqudQ-ZbQT9fmMC6CIFGW_JA1SlR5imQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انفجار ثلاث عبوات ناسفة من مخلفات تنظيم داعش الإرهابي في محافظة الأنبار قضاء الفلوجة كانت متروكة داخل بزل، ما أدى إلى إصابة شخص واحد.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80523" target="_blank">📅 01:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629a285c37.mp4?token=qtuOZKQeO-02x5xWSVniT0X0ccfkmWnkE2U85oYhmiz6UUFUmOWL9clEDKntbEkuixDFaKRsoIxRV5gFyVSg6BBqO4DAiYJWvsEOK3fMh0prtTc1KOJb3t3LoJPvRs2KNHQyVlW6_SDHqDy6f7vHZcCP-0aKYsYdBAueEMuajr5zb6V9GKGHH305lxPNnrZuIA37jBkRJvx9VIs3onD1afCM95jvBEvEl_xxZe0WxAKwQubLX-PzUntWls04ydvXwwvbKpu_5-g7YhJFBjazLU-PhEOIO1bs65W9O3OvDUxYYpgniOaA3DabFHuB50PRG4D3esUghAwOPjZp6aIdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629a285c37.mp4?token=qtuOZKQeO-02x5xWSVniT0X0ccfkmWnkE2U85oYhmiz6UUFUmOWL9clEDKntbEkuixDFaKRsoIxRV5gFyVSg6BBqO4DAiYJWvsEOK3fMh0prtTc1KOJb3t3LoJPvRs2KNHQyVlW6_SDHqDy6f7vHZcCP-0aKYsYdBAueEMuajr5zb6V9GKGHH305lxPNnrZuIA37jBkRJvx9VIs3onD1afCM95jvBEvEl_xxZe0WxAKwQubLX-PzUntWls04ydvXwwvbKpu_5-g7YhJFBjazLU-PhEOIO1bs65W9O3OvDUxYYpgniOaA3DabFHuB50PRG4D3esUghAwOPjZp6aIdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اعمدة الدخان ما زالت ترتفع من وسط مقر حزب الحرية الكوردستاني في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80522" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80521">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fa60cf3d.mp4?token=GS2rG3soOwJZw-5pN2hWvKUNNTX1WgxB-foQtTS9WRGjBBdYWNAQZ1N3cLwRvwHktO9PFumQ6D2iHngCQb4Anr0cYoW_TSd9RN_vWjTCXa-xumSXVTydsnn5_ZSLfdquRk7DJJU-1MJ937HPkv2qaPz4s6veXjfq55RB8SmQn5NEq1zfqCWZ52fU680qyszNqLGQqyym6ogjykMk_0Dah1eYdTZ_MvJLgK2Zg8l_7AupB4Qx_98pZ5uJZsKrJUdD65Rw-Jh9Dkhlr5bKyVc-OSTaSy0dIrjZ71yUKke1-LxX3WLABQvgO0hH_wSrIQGOjzYiliwdNxQroH_HRX-AJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fa60cf3d.mp4?token=GS2rG3soOwJZw-5pN2hWvKUNNTX1WgxB-foQtTS9WRGjBBdYWNAQZ1N3cLwRvwHktO9PFumQ6D2iHngCQb4Anr0cYoW_TSd9RN_vWjTCXa-xumSXVTydsnn5_ZSLfdquRk7DJJU-1MJ937HPkv2qaPz4s6veXjfq55RB8SmQn5NEq1zfqCWZ52fU680qyszNqLGQqyym6ogjykMk_0Dah1eYdTZ_MvJLgK2Zg8l_7AupB4Qx_98pZ5uJZsKrJUdD65Rw-Jh9Dkhlr5bKyVc-OSTaSy0dIrjZ71yUKke1-LxX3WLABQvgO0hH_wSrIQGOjzYiliwdNxQroH_HRX-AJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حزب الحرية المعارض لايران: الذي يتخذ من إقليم كوردستان العراق مقرًا له يعلن تعرض مقره في محافظة أربيل لاستهداف بصاروخ باليستي.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80521" target="_blank">📅 00:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef95cce284.mp4?token=GpLWzNoavF4BME2W-8VYvSiCeGyJ7exyjV1d-VHYUKr_7MVqJIKxzBDc-b3ZcZ1TcG5-QSAFK46ACK5B-NbWh9wWt7U65YD1hS-aRaA-DzHiKWvPeLHCCPsxlQBWdxxbJosheaGCXDnWjsKHUyom5osu6_Qn5dWSQAuvDVRDq66UH-vx0W61ujkmSrTWtkhdB_iQfc1MBrQ0EWYJ-NZq9IPNTKRJPTjFXIgljmeT8nW5AGmdLvmo10p7sv9aX4ldzYDY-cnLM184mYpaf4p-p_OwNBWlxYYL7vDsKxzbS92K9oNi-mdj2GvYt6YGpNTl_bIbt5DPq1G3h7JahDfpDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef95cce284.mp4?token=GpLWzNoavF4BME2W-8VYvSiCeGyJ7exyjV1d-VHYUKr_7MVqJIKxzBDc-b3ZcZ1TcG5-QSAFK46ACK5B-NbWh9wWt7U65YD1hS-aRaA-DzHiKWvPeLHCCPsxlQBWdxxbJosheaGCXDnWjsKHUyom5osu6_Qn5dWSQAuvDVRDq66UH-vx0W61ujkmSrTWtkhdB_iQfc1MBrQ0EWYJ-NZq9IPNTKRJPTjFXIgljmeT8nW5AGmdLvmo10p7sv9aX4ldzYDY-cnLM184mYpaf4p-p_OwNBWlxYYL7vDsKxzbS92K9oNi-mdj2GvYt6YGpNTl_bIbt5DPq1G3h7JahDfpDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استهداف مقرٍّ لأحد الأحزاب المعارضة في محافظة أربيل شمالي العراق بطائرتين مسيّرتين.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80520" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8144f7598a.mp4?token=v2S5CYdRuyQW9ccErxdwqYpNbBZCYputNGiahledh25GeuikZf3VtJ0sH-2GoTfA-6FbiDb8_E2AhqBKBtAhAtV4tp_s4_DjTI1Pja6Kx7MXNJDib8mdb7paS0KkidORq64rSLbTyjWK-n4nFMl81mfE5fpqLodTG559XjASRu1MRMWVD761ELLanTJSNlcNAIsYin61MMjTk2p7ZDHamCx_GnSJgiw8zBOxgK04XzFjmatfsfhCbDCB9eQ_1NBppnwniEj8COIf4XQe1LFgTFgBWwLcAeWNNr5eQ6tPnz_Q9QBI2XLClRV_19OEFSP1sQyg5Oc7oLlxxjVDE_8wyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8144f7598a.mp4?token=v2S5CYdRuyQW9ccErxdwqYpNbBZCYputNGiahledh25GeuikZf3VtJ0sH-2GoTfA-6FbiDb8_E2AhqBKBtAhAtV4tp_s4_DjTI1Pja6Kx7MXNJDib8mdb7paS0KkidORq64rSLbTyjWK-n4nFMl81mfE5fpqLodTG559XjASRu1MRMWVD761ELLanTJSNlcNAIsYin61MMjTk2p7ZDHamCx_GnSJgiw8zBOxgK04XzFjmatfsfhCbDCB9eQ_1NBppnwniEj8COIf4XQe1LFgTFgBWwLcAeWNNr5eQ6tPnz_Q9QBI2XLClRV_19OEFSP1sQyg5Oc7oLlxxjVDE_8wyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سماع دوي انفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80519" target="_blank">📅 00:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIfDt2uviIBJkPzNLGhg5AkjMxTbbXPl6iZe7OmmjXb3Kx18gk_5y_1eZQwMxCJrUFz0ZxGsy1tlBkkzqG5jBrpMcgddUu9JJnpcShPZVPRExIOTc7cX6vPXTCJAML8zxLKSQqrJazDQcdhbglVlu5q36C7eoZDb6Y5ba2pSVQ-cAja6xVCqJ-beBVyGGGCb4hekacsntF1RdIv4CWIKGWGrEZnDM7k9Yh-2fANGLTQ4W0fi_x39dQ_nzcPPZk_eVzSYxlPcKO1-F4oHGkaZk67-DDb6nQ1vt1kagX10o-Cv-s_7yytwkbCK57g39gSgM3Bvw2OaoXQGPaabJuBU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
سماع دوي انفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80518" target="_blank">📅 00:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
قالبياف:
تعهدنا بمنح الوكالة الدولية للطاقة الذرية إمكانية تفتيش محطة بوشهر ومفاعل طهران البحثي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80517" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80515">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdbcef6e0.mp4?token=G-3oY99BtilYjPXPSHhbTvBxzumGIOdJbRNBz0-i5uWV5_yXw2gJqcrslm2QVNWv6ZX39uW2GgO8HB-Uq5VAhkUj-3lMGYFtyMv0ZWYLoAMF9RfKGJ15sSW3yIUP2v3j4PpYNtKjO88A2-0JDUNMlTqpSgV0HmLJA6RVS2bFGwq3qgunVwxaBFr2cVutiPV-ohtnm6kKhaFDV_dl_oX-FPMZ7ymo3Q_6AS0GYycurWpEnkPOzzPnoMTTK5amdq6gixCdVDhAsbEXfJO7n1QNVpJeFbxcY8fCixWJeZmvCGkKZc02QocTuCTP1Or8BR1T9MIhFcKbTEr7RkkF4d57SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdbcef6e0.mp4?token=G-3oY99BtilYjPXPSHhbTvBxzumGIOdJbRNBz0-i5uWV5_yXw2gJqcrslm2QVNWv6ZX39uW2GgO8HB-Uq5VAhkUj-3lMGYFtyMv0ZWYLoAMF9RfKGJ15sSW3yIUP2v3j4PpYNtKjO88A2-0JDUNMlTqpSgV0HmLJA6RVS2bFGwq3qgunVwxaBFr2cVutiPV-ohtnm6kKhaFDV_dl_oX-FPMZ7ymo3Q_6AS0GYycurWpEnkPOzzPnoMTTK5amdq6gixCdVDhAsbEXfJO7n1QNVpJeFbxcY8fCixWJeZmvCGkKZc02QocTuCTP1Or8BR1T9MIhFcKbTEr7RkkF4d57SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أرتفاع عدد قتلى الزلزال في فنزويلا إلى 2295.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80515" target="_blank">📅 21:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي تنشر:
بهذا النعش يستريح سيد زمانه، وقائد الشرف وأهله، وزعيمٌ بوزن الجبال، ورجلٌ بحجم الدنيا.
قد يخفّ الوزن الحسابي لهذا النعش، لكن أكتاف بني البشر جميعاً تعجز عن حمل قيمة صاحبه.
قوموا لله، وهبّوا مسرعين إلى استقبال السيد العظيم الذي حلّ زائراً.
هو الزائر بعد فراقٍ دام سبعاً وخمسين سنة.
ألبسوا المدن سواداً عليه وغضباً، فهذه هي الزيارة الأخيرة قبل الوداع الأخير.
ولا تدعوا هذا اليوم التاريخي يفوتكم .</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/80514" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: تقرر استخدام جزء من الـ6 مليارات دولار المجمدة لشراء سلع بناء على احتياجاتنا.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80513" target="_blank">📅 21:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
لو أمر القائد بعدم التفاوض، لامتثلنا للأمر بالتأكيد.
الدفاع عن القوات المسلحة واجبي وسأدعمها بكل ما أوتيت من قوة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/80512" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تقرر استخدام جزء من الـ6 مليارات دولار المجمدة لشراء سلع بناء على احتياجاتنا.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80511" target="_blank">📅 20:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80510">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⭐️
أكسيوس:
تحاول الولايات المتحدة إقناع إيران بالتخلي عن فرض رسوم على مضيق هرمز مع استئناف محادثات الدوحة.
يشارك مفاوضون أمريكيون وإيرانيون في محادثات في الدوحة تركز بشكل أساسي على مضيق هرمز، حيث تجادل واشنطن بأن إيران ستكسب أكثر بكثير من صفقة نووية مقابل فرض رسوم على الشحن.
وقال مسؤول أمريكي: "كانت رسالة الولايات المتحدة إلى إيران هي 'فكر بشكل أكبر'، مشيرًا إلى أن رفع العقوبات بموجب اتفاق أوسع سيكون 'أكثر قيمة بـ100 مرة' من 'استخدام أسلوب العصابات في محاولة فرض رسوم'.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80510" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80509">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236dd9ce6.mp4?token=Z4HpIt02yV_NbFlxeFs3qw6cZxnXCmsTN3JZfQbUHxzHIVeCRaltIm1Ot2pUenLJXmdICUa1hAZhU0840p11c70dNQ-lfzLybyZQG2G_YGb89W65HEBKyG3HjMPDDON4s5445JQnit7fjxHVrMbj-haOKO_-d5knh_uBBz_xSpZf8zl_VBiISm22EuOwDHTC-_0eNGpfulpgrbenPv1js0XB-oRYOM_IS-GKCi9f1U-M9vwI5FeHJh8N0tDCO6jNjZEDKZsWylTZdr9Rgenx3rdujf1YWfsFnLw3tzB5wl3HTX-lZMZsDZE17Mkr6h2JBiMS9Sv1zJoRt7LJ5JTkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236dd9ce6.mp4?token=Z4HpIt02yV_NbFlxeFs3qw6cZxnXCmsTN3JZfQbUHxzHIVeCRaltIm1Ot2pUenLJXmdICUa1hAZhU0840p11c70dNQ-lfzLybyZQG2G_YGb89W65HEBKyG3HjMPDDON4s5445JQnit7fjxHVrMbj-haOKO_-d5knh_uBBz_xSpZf8zl_VBiISm22EuOwDHTC-_0eNGpfulpgrbenPv1js0XB-oRYOM_IS-GKCi9f1U-M9vwI5FeHJh8N0tDCO6jNjZEDKZsWylTZdr9Rgenx3rdujf1YWfsFnLw3tzB5wl3HTX-lZMZsDZE17Mkr6h2JBiMS9Sv1zJoRt7LJ5JTkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
غارة من الطيران المسير الإسرائيلي على بلدة النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80509" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80508">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌟
القوات البحرية الأمريكية: في الأول من يوليو/تموز، الساعة 3:30 صباحًا بتوقيت شرق الولايات المتحدة، هبط طاقم مروحية MH-60S Sea Hawk التابعة لحاملة الطائرات الأمريكية جورج إتش دبليو بوش (CVN 77) اضطراريًا في بحر العرب. ولا توجد أي مؤشرات تدل على أن الحادث ناجم…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80508" target="_blank">📅 20:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80507">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
القوات البحرية الأمريكية:
في الأول من يوليو/تموز، الساعة 3:30 صباحًا بتوقيت شرق الولايات المتحدة، هبط طاقم مروحية MH-60S Sea Hawk التابعة لحاملة الطائرات الأمريكية جورج إتش دبليو بوش (CVN 77) اضطراريًا في بحر العرب. ولا توجد أي مؤشرات تدل على أن الحادث ناجم عن عمل عدائي. وقد تم إنقاذ ثلاثة من أفراد الطاقم الأربعة وهم في حالة مستقرة على متن حاملة الطائرات جورج إتش دبليو بوش. وتواصل وحدات البحرية الأمريكية في المنطقة البحث عن باقي أفراد الطاقم المفقودين. ويجري التحقيق في سبب الحادث.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80507" target="_blank">📅 20:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80506">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9458e9fe.mp4?token=YsdqAd89wONB9JjkrtIi5PEui7_eR3o0rgAE7JTe8Yd8-xHqKFXZdLa6a-P8ulincn-pDS4K_ULx6zPWnMS-9-60tLr9gFLPCu4RP7zwmuttqdAqNxdGwKvn3uwZAaAKwaIPw3u5SNLt0M5q2m0WjQbhNGvGSs4JxEh5s2myTtuuzNtx9TLqj2AyEzlD9Wl8Jimk4twiEcadHTNuHoxr6f8kplvdAbWGm_rk1QeR--R6SUgt_TZyOf4WRAds6_BtC5WKxFF9w0BX5VFQY0v5_aLbxbD4xeZO0LBMDADIY8Q0Y8zILvN19IVlLh0CRBEdvfLRBNLy3zbjsFYNfIDHfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9458e9fe.mp4?token=YsdqAd89wONB9JjkrtIi5PEui7_eR3o0rgAE7JTe8Yd8-xHqKFXZdLa6a-P8ulincn-pDS4K_ULx6zPWnMS-9-60tLr9gFLPCu4RP7zwmuttqdAqNxdGwKvn3uwZAaAKwaIPw3u5SNLt0M5q2m0WjQbhNGvGSs4JxEh5s2myTtuuzNtx9TLqj2AyEzlD9Wl8Jimk4twiEcadHTNuHoxr6f8kplvdAbWGm_rk1QeR--R6SUgt_TZyOf4WRAds6_BtC5WKxFF9w0BX5VFQY0v5_aLbxbD4xeZO0LBMDADIY8Q0Y8zILvN19IVlLh0CRBEdvfLRBNLy3zbjsFYNfIDHfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
عمليات تمشيط وإطلاق نار كثيف من قبل جيش الإحتلال الصهيوني بإتجاه بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80506" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80505">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇦
ليلى عبداللطيف أوكرانيا مجدداً.. زيلينسكي:
هناك معلومات من المخابرات حول استعداد روسيا لشن هجوم جديد.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80505" target="_blank">📅 19:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80504">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17df36d2b.mp4?token=JBZfhC1C7LSnz3SDsJFPC7dezQ1KLCFwHNRS1p4itd0J51K7CmpkTtGMMP3OBLDuoeAXvGzmAP3KoEjqeDUXTDX_pMZkIIAwrwhxd2nLKvJyfLxf-uGoZ637v9xtjyf3MEhnUSXMQQ1L_QaNFtEr5uZz1dqgbpToBrnk1Ii9Ye8ntjC7JWlM8oHybQKKJJ6JTfYde9haavUHj0rFH-MP4M4JyzjbcugiCn63CJBdM5c8ywDcVAAOo3mZ_kf5kw2MmRNvfL5NFwIYEoGPvsNmAIpdoc9xZKe38jPiwVsJ8g9fof5o7nGB9zvdnfCCOivD0kRo23ehyKJtaoxy9H4kEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17df36d2b.mp4?token=JBZfhC1C7LSnz3SDsJFPC7dezQ1KLCFwHNRS1p4itd0J51K7CmpkTtGMMP3OBLDuoeAXvGzmAP3KoEjqeDUXTDX_pMZkIIAwrwhxd2nLKvJyfLxf-uGoZ637v9xtjyf3MEhnUSXMQQ1L_QaNFtEr5uZz1dqgbpToBrnk1Ii9Ye8ntjC7JWlM8oHybQKKJJ6JTfYde9haavUHj0rFH-MP4M4JyzjbcugiCn63CJBdM5c8ywDcVAAOo3mZ_kf5kw2MmRNvfL5NFwIYEoGPvsNmAIpdoc9xZKe38jPiwVsJ8g9fof5o7nGB9zvdnfCCOivD0kRo23ehyKJtaoxy9H4kEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تستكمل هدم منازل الشيعة في قرية المزرعة الشيعية وسط اعتقال وتعذيب عدد كبير من الشباب الرافضين للهدم.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80504" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80503">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
نائب الرئيس الأمريكي دي فانس:
إذا حاولت إيران إعادة بناء برنامج نووي وتهديد جيرانها ودعم الإرهاب فالرئيس ترمب لديه خيارات للتعامل معها.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80503" target="_blank">📅 19:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭐️
بالتزامن مع عملية إعتقال المتهمين بقضايا الفساد..
وسائل إعلام كردية:
وفد من جهاز المخابرات العراقي يصل سراً إلى إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80502" target="_blank">📅 19:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2f2f3651.mp4?token=kVqE_WjHOC5KfP5aJY3aVEjMopCL4vrXR2gqX2ca-HovQTkLQnesJ-3X-yTtgGU9MX3OO1SzsdUVI0K1RZ4tF1vxqmuVjq2NRBzxtjsW__X6VHpDuW8jIoHJO0S0ZUzbEhE01wwmyvWwNtJhIm9zjBofmYXKTFvyI2ckQhen_3pioyX_QRlwHNtwyrPYEwx_GJLDQ8G5ykMYV7N0OMm5PqQYozfk7en_Y3wWwu6Q8rU5EptjI3JlWDnABxBrrE8yUetqCqvjbhSlzHivHB8bjV-5-may_vp_7IsMwswyq9gDqvBBtY1D5EfHLTSSwZngevydLJjAOHHXKRZw3puBaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2f2f3651.mp4?token=kVqE_WjHOC5KfP5aJY3aVEjMopCL4vrXR2gqX2ca-HovQTkLQnesJ-3X-yTtgGU9MX3OO1SzsdUVI0K1RZ4tF1vxqmuVjq2NRBzxtjsW__X6VHpDuW8jIoHJO0S0ZUzbEhE01wwmyvWwNtJhIm9zjBofmYXKTFvyI2ckQhen_3pioyX_QRlwHNtwyrPYEwx_GJLDQ8G5ykMYV7N0OMm5PqQYozfk7en_Y3wWwu6Q8rU5EptjI3JlWDnABxBrrE8yUetqCqvjbhSlzHivHB8bjV-5-may_vp_7IsMwswyq9gDqvBBtY1D5EfHLTSSwZngevydLJjAOHHXKRZw3puBaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
عمليات تمشيط وإطلاق نار كثيف من قبل جيش الإحتلال الصهيوني بإتجاه بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80501" target="_blank">📅 19:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
سيُغلق مطار مهرآباد اعتبارًا من الساعة الخامسة صباحًا يوم الجمعة وستُعلق رحلات طهران بالكامل يوم الاثنين.
▫️
سيستأنف مطار مهرآباد عملياته يوم الثلاثاء بينما سيبقى مطار الإمام الخميني الدولي مغلقًا لنقل جثمان القائد الشهيد إلى العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80500" target="_blank">📅 18:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
بموجب مرسوم صادر عن سماحة قائد الثورة، السيد مجتبى الخامنئي، تم تعيين حجة الإسلام والمسلمين محسني إيجئي رئيساً للسلطة القضائية لولاية أخرى مدتها خمس سنوات.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80499" target="_blank">📅 18:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80498">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcaf83b98.mp4?token=Pjge1F5lUkmfJe12NuVnebqaWoXBjcMgsaMbXSC9T_Sz5z5-LtoLOfzH0BK1JQZBNT0lfgWfmzPuRP8yZqWtRHGzsqjTs14fteeP2znUHcHn7qm3L7YqHSt0qkSzASRs8niVK2--H5HNckotQEdGeCs4EJvG-H5h1QeYwrVowu7txnUUnapmLr5VsSj-PFjlfLxqnayMefA4eGGUHORKwca9jPhQdIWS2IyhzD5US0mP3jRdKH0aZRZLotnld5dETkWL_NKyDra3Zxt04VD5k7Woiwk_qnLEFJiXjntquacdTE9-TtBXsMzvLPndmnLLCWcdViKbk5GPpjrdG6hMDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcaf83b98.mp4?token=Pjge1F5lUkmfJe12NuVnebqaWoXBjcMgsaMbXSC9T_Sz5z5-LtoLOfzH0BK1JQZBNT0lfgWfmzPuRP8yZqWtRHGzsqjTs14fteeP2znUHcHn7qm3L7YqHSt0qkSzASRs8niVK2--H5HNckotQEdGeCs4EJvG-H5h1QeYwrVowu7txnUUnapmLr5VsSj-PFjlfLxqnayMefA4eGGUHORKwca9jPhQdIWS2IyhzD5US0mP3jRdKH0aZRZLotnld5dETkWL_NKyDra3Zxt04VD5k7Woiwk_qnLEFJiXjntquacdTE9-TtBXsMzvLPndmnLLCWcdViKbk5GPpjrdG6hMDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعد أداء بطولي ومشرف..
عودة لاعبي المنتخب الإيراني إلى البلاد وسط إستقبال جماهيري كبير بمطار العاصمة طهران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80498" target="_blank">📅 18:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80497">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
تدعوكم اللجنة الإعلامية الخاصة بتشييع المرجع الشهيدالسيد علي الخامنئي (رض) إلى حضور وتغطية المؤتمر الإعلامي الخاص باللجنة الإعلامية للتشييع، والذي سيتحدث فيه الفريق الدكتور (سعد معن ) عن الاستعدادات والخطة الإعلامية الخاصة بالمناسبة.
الزمان: يوم غداً الخميس، الساعة 11:00 صباحاً
المكان: بغداد / مبنى مديرية الإعلام
للاستعلام: 07712853029</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80497" target="_blank">📅 18:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80496">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇷🇺
🇮🇷
نائب رئيس مجلس الأمن الروسي دميتري مدفيديف سيشارك في مراسم تشييع الجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي في طهران بصفته مبعوثاً خاصاً للرئيس الروسي.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80496" target="_blank">📅 17:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80495">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41542b706d.mp4?token=SabYGCs1w-cubntTIMRMie-IhfqafeiWlz8RkcAIOfFELoXxOZxeumLZNktrgAgyITAcMkyfrjpO94yZTIEsH74JS5xYcAlKb3W-B5kFAjUEhbmkMr6gCZZOpd5UYhfeMRwixoRKqq4RcxRc8lAebKJtnApGHW1BtFaLKdw6c74ktafD9FWQ3-TftM-TjvespDI9GVuiKA4ABSKGwpJFJFsfBnU9WIRYe6XZzBY-WUxbqEhNOXbqdCLtM_gotJ3O_o5iwJ-EifJu8Wqn_Gyrgy4WbAzxGak1j5BA3EXl-XF5G14d5dx0f4sJ1rBThDxA57bfZpQPQmGRanLT2zAJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41542b706d.mp4?token=SabYGCs1w-cubntTIMRMie-IhfqafeiWlz8RkcAIOfFELoXxOZxeumLZNktrgAgyITAcMkyfrjpO94yZTIEsH74JS5xYcAlKb3W-B5kFAjUEhbmkMr6gCZZOpd5UYhfeMRwixoRKqq4RcxRc8lAebKJtnApGHW1BtFaLKdw6c74ktafD9FWQ3-TftM-TjvespDI9GVuiKA4ABSKGwpJFJFsfBnU9WIRYe6XZzBY-WUxbqEhNOXbqdCLtM_gotJ3O_o5iwJ-EifJu8Wqn_Gyrgy4WbAzxGak1j5BA3EXl-XF5G14d5dx0f4sJ1rBThDxA57bfZpQPQmGRanLT2zAJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇺🇸
الكيان الصهيوني يمنح الولايات المتحدة استئجار موقع ما يسمى بـ"السفارة الامريكية في القدس" مقابل دولار واحد ولمدة 99 سنة في حال بقاء الكيان.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80495" target="_blank">📅 17:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80492">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKg3pXJzl1CVNzsYh7x7ORT_mOIDiwzwONUz6bn1vNmhdv7hNCVovsOM4j1g7wJenQtxUJp-u5_seOy-t4Pk93pSHGDnXL2dRBw9knAs-cuEirQvWeXqjuoojho-kL870QD6e2L5QNjJYnhonoN3VHI00JVonEAXBdXPr23cHLJ6FccPmN_fg96bfRvwWkzay3EK6PH7MXRCZ8uKxt7Hksa9DlOtqB3CZC_9zEWycu04fJlJO3dEEkUPe8AoLHaCnm3AGh0ujGDm3uz-oVNobcAORnlNr54MrpiQKEmA9t9cLtQG83Ow9IR4pE7XFNUE6EPHnEHqPp1bIUe3YC3bSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpD0inhHnRMxM7CoKHa-hbo6hGzZR3x3zdzkZiUfSAmDbN2J2sTPWG4L0tmhPgf4WjVt4_roBs55kUyCyDBdTkf6cRlQmpjbjNirsZFbRbnCZU2b_i69tjXTtYpfn9Uj6VGoah-0pDay9wFTZ9c4CeWOvxu4K2cbyFI6IRNOwsJCSgWm7e00Lzc7P90Qo2LN93Aqv3x5Yk6YiI94wzBwDoKccaj3IH8BgHEV6ujL-MZtzlLawcdzSDP0C0IPpVciRWOT1Nk01OrWvP3lFVkWz3ZCoqOc2GMuT3bqRxk-BGpVeI_RjOPdjyVxVc2cGFN8JNHhyLO0ySgskd6c8c6Zzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-Bybrt3DRMaxlC0v9s6GPFv0MCjM_he4-34xfxMX7FLu0CE7I9q-2y7wUlMi23tOmvoM-6vVGUinbcj9wJ6jXot2diSn2Y-obhhnkm0jWQnHCSF1XOkqoNXfdEtI9_FoY74sZAls5qtubE3RLQTkj1vvhPuQ2hKsTweyRZBn0_bsArEZ9onqHENXbxbE5-sVibvEXxKOJNfpO78JgNxmKqXwKbpb-IlvzrUUkPI8I5LneUpG-2QgndiF9nBtS2AeMp5MZ-3xXzwFTLvkdtc53Wcaq3j4Rr53rO3yrST5SyJvgV80suS2sCyjf64XYZ83AdJ4AZ50gvqKsZbzAG8mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#بالوثائق
🌟
سحب يد مدير عام شركة تصنيع الحبوب في وزارة التجارة العراقية بسب وجود مواد غير صالحة للاستهلاك البشري.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80492" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80491">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
المتحدث الرسمي لائتلاف الأعمار والتنمية يتحدث عن استثناء وانتقائية:
سبق لحكومة السيد السوداني أن طرحت تعديلاً وزارياً شمل ستة وزراء ورفض التعديل من قبل الكتل السياسية في حينها، وبنفس الوقت أحالت خمسة وزراء إلى القضاء ، إلا أن ظروفها  لم تكن توفر الغطاء السياسي الكافي لاستكمال مسار الإصلاح.. أما اليوم فإن حكومة السيد الزيدي تمتلك تفويضاً سياسياً أوسع ، ونؤكد في ائتلاف الإعمار والتنمية دعمنا الكامل لاستثمار هذا التفويض بفتح جميع ملفات الفساد دون استثناء أو انتقائية ، وترك الفصل فيها للقضاء العراقي.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80491" target="_blank">📅 17:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80490">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هجوم مسلح على طريق 17 الزراعي في قضاء سفوان ضمن محافظة البصرة جنوبي العراق يسفر عن مقتل طالب جامعي</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80490" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80489">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cec442b3.mp4?token=Z4Y3wBLrRo1FEKFusVCTcOK-YYB_ttXIQIZaLhJUygTVAA59cmKmSVmh94GY5HIX49MZsCjcoGYsS_fKcsf_etL6v_5PFKjUkyvoC5jEaoMB5_ajFMY1xrLBBJdBP2sjZQGU7piJgINck4cgip0Xm3Gdpf6991Z4-lz8BbkZYt9EBbevEJu2Mdwu19H1j79i39S79cvPOCWYiQUI2WisRq3hVOopYbi3WAJ1UXsDHpRQ3AxgltKrCGqleyoRZH5TTVgb_Uh9lX0eypZoIZrYUqdZkI_Dz4ho5Mrn2OoPz852SdStrmOxY1hhJk5L0GiItpbZcgX6tNOEeGjdVDGJYWMIMp9RcIttJDvMa43izuKcOCcM033Jxxm469-qYG69mbWmIf72jl3eqmAXwvrgo4pR8NfVmg_fN7NwWjBnZ_wF-Y_fooTKpqVcpWc4frNJnSBnmpirLcUpv76jGkoSH9bVRwaTQxvyk43jy4ZV5-yYpH4rKAZwLHH5ADBNe3tO7ArISfl0PJfPjBFN9qCw-GwmLjvtEwhe4gdNo5o6TB1frgl3O97PWi4tKbf6Bh7ohHW2CQ_r0KbQjFYqZhMHXa3IV4UGL8yFD_F2txBIOKCA3MjogXbuf7EPQ2vbicGOqZQiJwOjKk97CO8pLY56HuBPSzKPGT0CavcmZCqT9f8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cec442b3.mp4?token=Z4Y3wBLrRo1FEKFusVCTcOK-YYB_ttXIQIZaLhJUygTVAA59cmKmSVmh94GY5HIX49MZsCjcoGYsS_fKcsf_etL6v_5PFKjUkyvoC5jEaoMB5_ajFMY1xrLBBJdBP2sjZQGU7piJgINck4cgip0Xm3Gdpf6991Z4-lz8BbkZYt9EBbevEJu2Mdwu19H1j79i39S79cvPOCWYiQUI2WisRq3hVOopYbi3WAJ1UXsDHpRQ3AxgltKrCGqleyoRZH5TTVgb_Uh9lX0eypZoIZrYUqdZkI_Dz4ho5Mrn2OoPz852SdStrmOxY1hhJk5L0GiItpbZcgX6tNOEeGjdVDGJYWMIMp9RcIttJDvMa43izuKcOCcM033Jxxm469-qYG69mbWmIf72jl3eqmAXwvrgo4pR8NfVmg_fN7NwWjBnZ_wF-Y_fooTKpqVcpWc4frNJnSBnmpirLcUpv76jGkoSH9bVRwaTQxvyk43jy4ZV5-yYpH4rKAZwLHH5ADBNe3tO7ArISfl0PJfPjBFN9qCw-GwmLjvtEwhe4gdNo5o6TB1frgl3O97PWi4tKbf6Bh7ohHW2CQ_r0KbQjFYqZhMHXa3IV4UGL8yFD_F2txBIOKCA3MjogXbuf7EPQ2vbicGOqZQiJwOjKk97CO8pLY56HuBPSzKPGT0CavcmZCqT9f8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: يقول النقاد إنك تستغل منصب الرئاسة لتحقيق مكاسب شخصية
‏ترامب: أنا أربح لأن سوق الأسهم يرتفع. الجميع يربح. أموالي تُدار من قبل صناديق. لا أتحدث مع الأشخاص الذين يديرون أموالي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80489" target="_blank">📅 16:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0a98fb201.mp4?token=ksoqftA4T7a2i2A2g4bk29C3Mknt9HBYIapPzQMB_QNnVCdEPEyKlGQ2wwZfPQsEEpia8BQH1s901b1LCSf_5TMpLcz9Q6qWxVEb4b2S5QWxN1AvxjrsSGMiKZN5hczqFn1cDAm6HmuF_IqWkg5FFf8CvQYlrOtgDaOOH5mHUCNjSrhQHUaOS89iBtGSyQjQ71-Ad13UADr_KcNMcn39HdWJ-4RXxXwT7krlk3ZTgGyK17ewRCdoB-Up0nBt3AZVQ0Wx3EJ3AeHBgII39qZyTywp0J4O-Mie74ts2qzx-_X2zNSoJENvlI9lS2N5ihxqIKTCw0ctwi19Pebj8n_OHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0a98fb201.mp4?token=ksoqftA4T7a2i2A2g4bk29C3Mknt9HBYIapPzQMB_QNnVCdEPEyKlGQ2wwZfPQsEEpia8BQH1s901b1LCSf_5TMpLcz9Q6qWxVEb4b2S5QWxN1AvxjrsSGMiKZN5hczqFn1cDAm6HmuF_IqWkg5FFf8CvQYlrOtgDaOOH5mHUCNjSrhQHUaOS89iBtGSyQjQ71-Ad13UADr_KcNMcn39HdWJ-4RXxXwT7krlk3ZTgGyK17ewRCdoB-Up0nBt3AZVQ0Wx3EJ3AeHBgII39qZyTywp0J4O-Mie74ts2qzx-_X2zNSoJENvlI9lS2N5ihxqIKTCw0ctwi19Pebj8n_OHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الطائرة الفاخرة التي اهدتها قطر له: ‏إنّ البلاد فخورة بها للغاية. يمكنك فعل أمرين -- إما أن تتباهى بها بهدوء، أو أن تُظهرها. وأعتقد أن على البلاد أن تفخر بها للغاية.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80488" target="_blank">📅 16:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe48f538b.mp4?token=CVqEHlzb0LJLMIY1on2JNKUlT8XilMZbEYsvPrGRwIRDZV829F-ZuZkUG4dJ5HSZ_l4xAq4p7ukl9zTIpC_rjxKR5qihBkwKTbb3xvO9DEW-7yKTbb4Dk19iZIG8RfAAk5k_PdW7SvDtbMtmHqxhsNQP07tK6lVMWtwKhdzV3tFB9WR9EybzfZbuj0qZHxRq1sVBsxt-DRmfvCuSLF2QfQmlaxzXkmJIt5ZxohKavkVjVqzpyfwmBUJuPrjjU4STjpJt4GrOpDnjruorj3ciDvek0togs5WfsU5XdMMiOQHXnbRdHR43-hT0JrsgVOzReVF4GlIWWHKxmdaD9tuX0bofjVpCfL3HPZvAjn0bhJVYELlU5okJ59NVW6HRgADC3mcOaJ15O_X45wARnaOUDf67vuda2aYcGR8L41XsomL5uX9wmluNd7RLKJMsWx-hprVORK7wsz34ugwEz-b_OBMUjLwl8Sb2mRx63ksKmkI0IWQqdhMA7CUCYkJrxcpeeM_HvkYan_EpvVRp58VddqNGkQv_s-fNgZMluB4MlYj9MTC3R06njD7CMHsZTdmV-JqJa-TVzwjmdmmMMzRXvfcR0IC3lgvGLYyCWq-HLbWE6TovzMEP8jKnnfjmHhl-MaZxHoW-EtPPF3UcZMZMOVug_T3aOArOg5d4fsnGlbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe48f538b.mp4?token=CVqEHlzb0LJLMIY1on2JNKUlT8XilMZbEYsvPrGRwIRDZV829F-ZuZkUG4dJ5HSZ_l4xAq4p7ukl9zTIpC_rjxKR5qihBkwKTbb3xvO9DEW-7yKTbb4Dk19iZIG8RfAAk5k_PdW7SvDtbMtmHqxhsNQP07tK6lVMWtwKhdzV3tFB9WR9EybzfZbuj0qZHxRq1sVBsxt-DRmfvCuSLF2QfQmlaxzXkmJIt5ZxohKavkVjVqzpyfwmBUJuPrjjU4STjpJt4GrOpDnjruorj3ciDvek0togs5WfsU5XdMMiOQHXnbRdHR43-hT0JrsgVOzReVF4GlIWWHKxmdaD9tuX0bofjVpCfL3HPZvAjn0bhJVYELlU5okJ59NVW6HRgADC3mcOaJ15O_X45wARnaOUDf67vuda2aYcGR8L41XsomL5uX9wmluNd7RLKJMsWx-hprVORK7wsz34ugwEz-b_OBMUjLwl8Sb2mRx63ksKmkI0IWQqdhMA7CUCYkJrxcpeeM_HvkYan_EpvVRp58VddqNGkQv_s-fNgZMluB4MlYj9MTC3R06njD7CMHsZTdmV-JqJa-TVzwjmdmmMMzRXvfcR0IC3lgvGLYyCWq-HLbWE6TovzMEP8jKnnfjmHhl-MaZxHoW-EtPPF3UcZMZMOVug_T3aOArOg5d4fsnGlbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب عن الطائرة الفاخرة التي اهدتها قطر له: ‏إنّ البلاد فخورة بها للغاية. يمكنك فعل أمرين -- إما أن تتباهى بها بهدوء، أو أن تُظهرها. وأعتقد أن على البلاد أن تفخر بها للغاية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80487" target="_blank">📅 16:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbeeea8c.mp4?token=fnoKcpj_9OL6VqHWKRn0It1gZL27N8lbAbDDviDG6lBxDKd08-G1p94naJbUZlmoh_gH-i6wrFMZ4aZHbewOyyQR5Jg4phaA4FM8mMjwiBhs5qXi29adLdos8bwIkW06rwmfCJj9NBWk6QzqL5zL6owvXNKA6K9ShWAqti5ERBQ8pOulJxRWS3xaGYBvLq6vaCQbxngj65UcdFpTYAU2ZPydGDyeeyLSTV9Np9zs_k5VGfsVXs-aJVHQ90MP7vlAQqzWY8247Q7Pl8h2TxCC7hdLoK21j1-HO4AEirX2BlpOz4ypE_HqalEAwqgbHGz5M0TWsdYEGLQp5ao7yCZ7jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbeeea8c.mp4?token=fnoKcpj_9OL6VqHWKRn0It1gZL27N8lbAbDDviDG6lBxDKd08-G1p94naJbUZlmoh_gH-i6wrFMZ4aZHbewOyyQR5Jg4phaA4FM8mMjwiBhs5qXi29adLdos8bwIkW06rwmfCJj9NBWk6QzqL5zL6owvXNKA6K9ShWAqti5ERBQ8pOulJxRWS3xaGYBvLq6vaCQbxngj65UcdFpTYAU2ZPydGDyeeyLSTV9Np9zs_k5VGfsVXs-aJVHQ90MP7vlAQqzWY8247Q7Pl8h2TxCC7hdLoK21j1-HO4AEirX2BlpOz4ypE_HqalEAwqgbHGz5M0TWsdYEGLQp5ao7yCZ7jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير في ياستار شقق حي السلام ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80486" target="_blank">📅 15:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec1bb2f89.mp4?token=eAb7skrcV6Zze-ViRVKGjnQn7q6rJvHhvpccQeD6f5bx05znPRiyfn8C6jIXfRA7vDf19wZcOqVT1FOGmJA9PU8yiADh9GgWghJ7viz6VG9S5pBwBVwNF7_kXndTqpO1ds59FaVq48KTvdQQkwQUSV4d_fmSGfr9RBiPeFKlnv7ynBBRbbR3pBBZSdJlFeHHJrtalhSxHdkBA8FQeeIVxqpMdl6aa6LvAlELmEO4eKSzdu2Yi3qQRzHmaRPWI8L4TUCIvGK6Fka1w302lT9DUHtmJ87__B64XeCJvs4_6a4banzqlFmC4mhu5rUJKNID9dwgs-Qe7B0rk0uxMDL3Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec1bb2f89.mp4?token=eAb7skrcV6Zze-ViRVKGjnQn7q6rJvHhvpccQeD6f5bx05znPRiyfn8C6jIXfRA7vDf19wZcOqVT1FOGmJA9PU8yiADh9GgWghJ7viz6VG9S5pBwBVwNF7_kXndTqpO1ds59FaVq48KTvdQQkwQUSV4d_fmSGfr9RBiPeFKlnv7ynBBRbbR3pBBZSdJlFeHHJrtalhSxHdkBA8FQeeIVxqpMdl6aa6LvAlELmEO4eKSzdu2Yi3qQRzHmaRPWI8L4TUCIvGK6Fka1w302lT9DUHtmJ87__B64XeCJvs4_6a4banzqlFmC4mhu5rUJKNID9dwgs-Qe7B0rk0uxMDL3Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كببر على طريق أربيل-مخمور شمالي العراق</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80485" target="_blank">📅 15:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80484">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇶
الحشد الشعبي:
ضبط 20 ألف حبة كبتاغون في ناحية السجر بقضاء الفلوجة شرقي محافظة الأنبار داخل أحد هياكل البناء في ناحية السجر، كما ضُبطت بندقية كلاشنكوف، وسلاح من نوع M4، ومسدسان، ورمانتان هجوميتان.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80484" target="_blank">📅 15:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴‍☠️
حزب شاس الصهيوني يعلن أنه سيصوت لصالح قانون حظر الأذان.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80483" target="_blank">📅 15:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80481" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حدث امني قرب سواحل اليمن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80480" target="_blank">📅 14:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حدث امني قرب سواحل اليمن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80479" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
هيئة بريطانية: زوارق صغيرة على متنها مسلحون اقتربت من سفينة قبالة اليمن</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80478" target="_blank">📅 14:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1302294625.mp4?token=gm-Zu3o48WLw-2d2jrkW6pcJmwAd54xjd6TWSzWcKq2mkt9TIMtnK3fvJNfkLlGe_zXb52EfOPI2otEy2cSkUq-Q_sW1tmhA3hERBCF0-x-JdG_mstfeDQ9Go8f4V4MAr6gAmjcefX9LIa_Sgnax8UKV1x-2fW0MM-1eEOAEaRvEajoSWcA1N85LkAxrpMY4r0heJpEXaslzP5F4GhZeYIa_FJFVWkVKu07oaCoLa6v3qMhJnqhhIjCx6hAA7_PuLm3jSqTA7P7pLO7GI8INdUxjHKL8TgYQJkuQwsQVpEHdG0xcsn7g-uaCYsWKW3F_iL40mrzZT365QAIwCWQEhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1302294625.mp4?token=gm-Zu3o48WLw-2d2jrkW6pcJmwAd54xjd6TWSzWcKq2mkt9TIMtnK3fvJNfkLlGe_zXb52EfOPI2otEy2cSkUq-Q_sW1tmhA3hERBCF0-x-JdG_mstfeDQ9Go8f4V4MAr6gAmjcefX9LIa_Sgnax8UKV1x-2fW0MM-1eEOAEaRvEajoSWcA1N85LkAxrpMY4r0heJpEXaslzP5F4GhZeYIa_FJFVWkVKu07oaCoLa6v3qMhJnqhhIjCx6hAA7_PuLm3jSqTA7P7pLO7GI8INdUxjHKL8TgYQJkuQwsQVpEHdG0xcsn7g-uaCYsWKW3F_iL40mrzZT365QAIwCWQEhYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتداء مسلح يطال السائقين العراقيين في بانياس السورية من قبل عصابات الجولاني</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80477" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80476">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اعتداء مسلح يطال السائقين العراقيين في بانياس السورية من قبل عصابات الجولاني</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80476" target="_blank">📅 14:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f98398fd.mp4?token=Pi8jRMeGYHzxnuvIZ6ttv2yT86s-uyhGLWfma1a30anCCKYZHmUuiB4nRJn5T3MEAunwbaCXlZ9ZRZGlnu8D_tlFC7Y5dFsXmvHZ1R0CB6WJiawaXCCuXl9kRVDhvkqG6HmitOgpUVyCB298BbVnOCMTFZuQGy6Qzf6DVoWUCTwYkPWm61sdhZUS57S7GFteijYaaQeZv7NN7X8iqv948JSqaOJ3Qona5yeIPyk8bW_AXQGsEzRqMZ2RjwFjgtyn-ZCuqmnl0oOF1M-wxYy3c0-3eoROpZFJXkZywrpJvRdnOFM_VgQBC1zDDpPTOymmFsbpXzFuHUTQMycTmELg_Y28Po7cGJ7nObuSJmW_9Bx3ibONeH7tqgApP4uKGtm2LUbewePDSVzxAHA-2ecRoz2xTVAI6Tnz1VaXxXEWzZePCnlAUp4NcL8OjQec1KscwuQOLmqJVW1fjIv98zoOcOGSvLz50-c0Vjbu1JCxGW9iwcW5K3os3RfDl3s0djth67URhSFSvG4dj5aeuLyJfFJYcZcFaNauBkWqnpjlXbvDJjS8Hvs39tO8JzNMe0YtMuGnQvOXHvjt29vhMi0m4F0xBoQKT9HUKrXtr_4dFNUChfmRBnpyGaW-csh4m1U4c89jzaNnmedT2kS_cyldqwPIQk0Dyc0qh_gwu7W-Rlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f98398fd.mp4?token=Pi8jRMeGYHzxnuvIZ6ttv2yT86s-uyhGLWfma1a30anCCKYZHmUuiB4nRJn5T3MEAunwbaCXlZ9ZRZGlnu8D_tlFC7Y5dFsXmvHZ1R0CB6WJiawaXCCuXl9kRVDhvkqG6HmitOgpUVyCB298BbVnOCMTFZuQGy6Qzf6DVoWUCTwYkPWm61sdhZUS57S7GFteijYaaQeZv7NN7X8iqv948JSqaOJ3Qona5yeIPyk8bW_AXQGsEzRqMZ2RjwFjgtyn-ZCuqmnl0oOF1M-wxYy3c0-3eoROpZFJXkZywrpJvRdnOFM_VgQBC1zDDpPTOymmFsbpXzFuHUTQMycTmELg_Y28Po7cGJ7nObuSJmW_9Bx3ibONeH7tqgApP4uKGtm2LUbewePDSVzxAHA-2ecRoz2xTVAI6Tnz1VaXxXEWzZePCnlAUp4NcL8OjQec1KscwuQOLmqJVW1fjIv98zoOcOGSvLz50-c0Vjbu1JCxGW9iwcW5K3os3RfDl3s0djth67URhSFSvG4dj5aeuLyJfFJYcZcFaNauBkWqnpjlXbvDJjS8Hvs39tO8JzNMe0YtMuGnQvOXHvjt29vhMi0m4F0xBoQKT9HUKrXtr_4dFNUChfmRBnpyGaW-csh4m1U4c89jzaNnmedT2kS_cyldqwPIQk0Dyc0qh_gwu7W-Rlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عمليات إبادة وتنكيل واعتقالات واسعة من قبل عصابات الجولاني الإرهابية تطال أبناء الطائفة الشيعية في قرية المزرعة بريف حمص مع توجيه شتائم للإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80475" target="_blank">📅 14:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رئيس مجلس محافظة كربلاء يوجّه بإبلاغ شيوخ ووجهاء العشائر للاستعداد للمشاركة الفاعلة في مراسم تشييع الشهيد سماحة آية الله العظمى السيد علي الخامنئي المقرر إقامتها في كربلاء المقدسة يوم 8 تموز الجاري.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80474" target="_blank">📅 14:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">القضاء العراقي: السجن 10 سنوات بحق المدير العام الأسبق للهيئة العامة للضرائب وزوجته عن جريمة غسل الأموال حيث أقدم المدانان على حيازة أموال واكتسابها بصورة غير قانونية واستخدامها في شراء عقارات</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80473" target="_blank">📅 14:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
لمعرفة نتائج الصف الثالث المتوسط:
اضغط هنا
الناجح مبروك
والراسب بيك بخت بمحرم النتائج
مواكب المبيت هواي
😄</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80472" target="_blank">📅 14:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VS7DR2PqWJuRu1_IN43OjZxQgYvvcg0dQDrHFmPLUC1BJweuDPxAGweodRV65z5-cSuhNJPdQj7q225Ix6vCP6KNvG4uS_ckLlOKyg8_-Bq_aW36MXHrPLIfa8rqABlLnQtBn6M45lVuOyeZBcI6iOCrYWabLNxE5q5rjTbcWBU5D7zo6ifaVpMVR96nE1dXNHrATtI-rzes-tPwBiOZQHXu44Wi85l2bJZPV5WyYzWuY2Ltj0ryNyZ92AeNFfm1fJqsIsI7IYC-0lX5jGmysiLBGt1TZSM-uutVvAnKeL5eonBTAgjWj2pwfqtOplkIqkVyq8SyZBI2FPde2mEBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير الخارجية الايراني عباس عراقجي:
‌‏مذكرة التفاهم واضحة ومتاحة للجميع وتلزم الرئيس الأمريكي بلجم حلفائه في تل أبيب. وإذا تجاهلوا أوامره، فسوف تؤدبهم إيران. ‏أي تهديد ضد شعبنا وقيادتنا سيواجه رداً فورياً وقوياً.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80471" target="_blank">📅 14:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d63ab9e22.mp4?token=ENqG3OOUOu-VGq4uo5etH2BZJXa7QbViA2C48tQOLcwikBBzTalgIRwfivjJJgJ4hPaPDMUTanzlA4l0OkjcG3CnCtsi0Hc9bNMGbjx4DkgJxrwF6dpIfJ1_YgQptHeBamtTbZGaOmjANbXHag6bQnk0Cy6LfgqblgE_jC7rbL-ZUKIztX1ZDI2Xw3zeI0YZ939J-HBycanI5y3sijz1pMp74mRyQaELPZ6_Aom9_ag582al2RDiWwC1XNWJdBpjSjdvQHpJ7TAfKVCdWxA0e7HMjydF25Z34ujSAEcHf2sBHRzw5SqV3ft4F7be0AC0W3pOTMtq9TsfnIYlLApZ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d63ab9e22.mp4?token=ENqG3OOUOu-VGq4uo5etH2BZJXa7QbViA2C48tQOLcwikBBzTalgIRwfivjJJgJ4hPaPDMUTanzlA4l0OkjcG3CnCtsi0Hc9bNMGbjx4DkgJxrwF6dpIfJ1_YgQptHeBamtTbZGaOmjANbXHag6bQnk0Cy6LfgqblgE_jC7rbL-ZUKIztX1ZDI2Xw3zeI0YZ939J-HBycanI5y3sijz1pMp74mRyQaELPZ6_Aom9_ag582al2RDiWwC1XNWJdBpjSjdvQHpJ7TAfKVCdWxA0e7HMjydF25Z34ujSAEcHf2sBHRzw5SqV3ft4F7be0AC0W3pOTMtq9TsfnIYlLApZ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد اضافية من الحريق المندلع داخل مطار بغداد الدولي لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80470" target="_blank">📅 14:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80469">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyZV0icL3bwgeTeQdSTT5F0FZTIp2CBVuau0evo-zdJBeMWRJGqjPWRUThjGxSI06AsbeERqB-42yk4-OfUONev-pA1ipmQ4-JASaSpTpqq6CfNJYifNfsUSlsJh24n9HnxNWiP16Z84WE6DZf3NSEDUveswR3mPIclnH2-4LMiy9Y1tHzLv9CYpmu0nkc1RDV8pxXm9RjW2DQv07jYEBblPuA_9SXMF3GLMukv4p9_sVCcYte0igdGVHaF3hp4Rr3dbxQjbiTP1iLv4ppmIA7Qqm2d6PTAB5J0JIMWjdeWPgKzFh2dGYBkSkDjxu-NM95CkdKUdbwHJ4-rK05FHBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الحريق داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80469" target="_blank">📅 14:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80468">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80468" target="_blank">📅 14:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80467">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHjjOM7qhSUPPcBRj40cuvnHVKOpT7Q1unYGb5eD1cZRDMB-EQBtnzWQ-kED2Pmdt5sgZ0Fncl1BQcZvsOl1gNxNURHViVEyf5j1LHKW-sMLhkCaB0f5t7gKoM3vbtwe8wN0w4z3v5-plP_wWL8scbnbCgjtapI1ftyV4NpoE8M919Mc9kVOQ8lkCW7GrKQR1dfhqMjBaKi0bQO__y_0Poyl2yWviibRVmd0TgoA-IWn3gKRecnqoy-XjSa5kp0_niiwdN8E0TL3mBHNfbiKP0Gl6EkQjEG372nBUo-APXamE7b8kRfdoDaZr8Fc0fVQNE_AOL6dGoze81B2FZ-cNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندلاع حريق كبير بالقرب من الطائرات الجاثمة والمتوقفة التابعة للخطوط الجوية العراقية داخل مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80467" target="_blank">📅 13:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80466">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزارة الصناعة والمعادن العراقية:
صدور أمر وزاري بتدوير وإعفاء عددٍ من مديري الدوائر والتشكيلات.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80466" target="_blank">📅 13:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80465">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-oEGJRLCpaxQRmRayNfL0VbvJ8y3jSR4BJwP1MyPJV2psqjgxrPRwPxZ-JahhZBB_7bbnWellGg0w5LtBK1xSDNQ0JsX5SNgR73OtPJB6NGGTVpq0TBdtJn8i-fAq3iPFAbGxkBEgZdIkTZwXj-M7qY9O7JZjnjOE_BiXOOUUZLlm7LG__1GzD-ZEAFiu2lw5625AQbTKNQSOdVtqZ10aDI1P1NSHocjbLb9wgUWWIpFIYX7T1Qbm-3RJqfRp7pqT47e-aWTsFnKPClf0U5fxJx1JTQ4avUT6VzcD-USg4j4dcYVze2LXOmnWOJ5Gly2vgeq8mVjQSJHN0rlpqfkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قيادة عمليات حزام بغداد بالحشد الشعبي تعقد اجتماعاً لمناقشة استعدادات تشييع السيد الشهيد الخامنئي ودعوة أبناء الشعب العراقي للنفير العام</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80465" target="_blank">📅 13:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80464">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbjZVEhIdHfp5dyblZfSeE8SkIl77J2RWyHEUbkmYH9Ls1TCi7kyufu2rQBFKW0XxHAKNgHhQX0Zrfn9JGOInTTQIottDNgE82tvZOtE7kYHvv5XuBCTWzytUcBQUjO0SGi3wx3tp84fp3ZiG7vTAyuuF3SFUOX2V3kITNNtBzGy3kvjaTznsAtH5qVtC4zh-a-5C76VqorwYG42o1tk_wkhi4F9jTkLEpw2KGCwlsNduPF72TrsM7fCR3333cJrMhtAF6fwtNNKwhO1MimOQn9mBfEMle6O2xiIMh9F-3xSbxH0n6NHaJ3hoSugsM293_PdHnqiq8zsJZqWXzMOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حدث أمني على بعد 76 ميلا بحريا جنوبي بلحاف في اليمن.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80464" target="_blank">📅 12:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80463">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
حدث أمني على بعد 76 ميلا بحريا جنوبي بلحاف في اليمن.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80463" target="_blank">📅 12:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80462">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالعراق يودّع إمام المستضعفين</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELOw0gq-unVaBX-BW6lQUxda2ugTrrpWCBTJu9Luih-H4mx47OpIwR9EUby2p-jjksiTsiz_OaKQIn83D6q1XZvi3mVMOSlZT45Te20b3dq07s-PXGeER08uaKOPmJ534WjCnc8S3SVDXcoZ93o6WUtyxsc6kz5xP2ds25Z6X77AlF8rzZLCcPzkc87Q8MaTKy2HRfF02KMbzg1vCkDaLjZwsPwU7Xl1vZz0y_xWzW7SpHj4nhPwudt-Q6nBLJ3xNqRaahi8l8mJMiQZWuW4_EE91n5OMlTM3Uiv07x8hHbQQflFm6cdUljMCMgHryXEHNvfvcvcmlU6lAjRXhcvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
يُنشر لأول مرة
|
🔸
المتحدث باسم لجنة تشييع قائد الثورة الإسلامية الشهيد: الجثمان الطاهر لإمامنا الشهيد لم يُوارَ الثرى حتى الآن، ولم يُدفن «وديعة»
إيمان عطار زاده
:
نعلن وللمرة الأولى، أن الجثمان الطاهر لإمامنا الشهيد وأفراد عائلته الشهداء، قد جرى حفظهم حتى الآن في كمال الإجلال والرعاية، ومع مراعاة الضوابط الشرعية والقانونية كافّة؛ فالجثامين لم تُوارَ الثرى ولم تُدفن «وديعة».
▪️
#قوموا_لله
#تشييع_إمام_المستضعفين
➕
t.me/Wadaa_imam_iraq</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80462" target="_blank">📅 12:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80461">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI3QSKjEjf43ljnipnekcTDrdFdTq5dOUKZx8y5owmeyeKprd699WJISBv_-W-ML-gUtncMQCG1HW5Imk78MY25R91OnOWnyfZJ0_kz-vd7zmqqA440tx6S3wnnTu3a1uMZcpUyCd7nfznApgkMwpWlyL_GrUdRlkrZW0HPY-rL8KR5ugvf6bSdLYqTtujckbv2esxm0ZW6z1SVfFspoCISFE-n76nLXR6-sQp1zRcLAH9ACGHvWFcTqlxPJslKaJLF8wh50DLfdTefOLqIN9N7N_wcFC6Kg7_7chvCeuTJcv3tybewCGZ6bYFt5dySi0PMRU5mSajCK_hP_JlBx1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الجيش الأمريكي: تم التعرف على هوية جندي مشاة البحرية الأمريكية الذي فُقد في البحر من متن السفينة USS Anchorage وهو العريف لانس أرماندو أورتيز كانسيكو، البالغ من العمر 21 عامًا، وكان يخدم ضمن قوة مشاة البحرية الاستكشافية الأولى (I Marine Expeditionary Force) في معسكر بندلتون بولاية كاليفورنيا.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80461" target="_blank">📅 12:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
تابعوا إطلاق نتائج مرحلة الثالث المتوسط بعد قليل على الرابط أدناه:
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80460" target="_blank">📅 12:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📰
رويترز: محادثات فنية غير مباشرة بين واشنطن وطهران جارية في الدوحة بوساطة قطر وباكستان</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80459" target="_blank">📅 12:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwW1sz5nHlcFx87j6BQr3er63sQg_qp4wMZfdjWi-c_S3Cvs16_xtk_5imAImh8-g8363NUxG5hxY8P8JNYNsL2pgzEmEaCGmIDDPNT1yhMjkC42r9n_AjhYIQF8owJuKf-iWNabTAfkK6IMCAq_XuQAp9Hf9EUOLVgefXsCET0rZW_3l4sjj5MpWcgroajNXaZMLd3kqocZN1xurU55yEwTLu7XtzRV0qGAAnjSdcns4ANADoO42CNfj0iigoHUjZ3gubtTu7YZbq7w9cITLSFut1zrl7q2xHqx0O3unKgdUypjqln5mmkQZewES4nDuzecT9tjvPnHhKHD6n7mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXqb2uhFVSHd2VBvrZ3txvIW-27L_8we02QCOZLYjLaf6-MWLKHtNvqAqoW5QdpiLl1S2r4mP1CZLvoepihJlhZR537mOt5hVnSGa5l7OpHLEyDXZ2Ms9YKPGRbs4b_47pmQxNptCKbB3eUX-o8UtohOdGvnYkzVN5msZEVRm9PGKQAXuhVFWf2mGzrcEpMWnd06rXRddF3WCb9N5VMyFhRj9IBeFYKyOPTMxiDnViv9lQqF8alKhHJaH92DP2K46XVqm3hdiZsVbfjBm-XR5OZgHZfCR3AFHOrokeAC0swGGOK4DVYUdteL_ok_k3J8Z22zW_Q2vDOWGSf_Kmem8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeZh6lVomtZKbIzpIGSzqiyJOr24A15D_2WLqMZHlZO2s4UdSFDwdZSYG3su8pPANVmO3LkX-HXC0wqnlu04NkYJ2V-QZKZ4Qg24YtdQFjqWc1Gkeej6CaJp9MjTGIKjz80VagDapLixYdpewhA9ONzcUK_SyxsG0qJ4Vzs0VCAhX2vYSweyaEWfl9QeAieESkyS3EVslJc1kb9OAXjqrF7Z0D7uMGEyf-eGscPnUmw1-Se7FyNFIZ7roZgTi37D2cF-3nKztKdP-mJ7bpME-V2SnANWRVyjtVcgkA3bdyOJNaJPaKovi0FvSt4BKQu43mySKBE1Ypu8C5KKIH3XYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
استمرار الانتشار الواسع للقوات الأمنية في شوارع العاصمة بغداد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80456" target="_blank">📅 11:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b2a11221.mp4?token=gb4jKxpkDAQ7utUkPsZjZNUteMi7PttLDcOaOfyey-Xl70T1CBOA-vG9rYcmSXnQczyezH3sOlg-oRQO8c4N8KoYqcTwK_cJ85GdIkN7LbANBEAp0VfvkO1_93wOrmMEX_rkF9GyEMtpniVMJ56Kj0lIpHzTmq1H_03ag2aRVRBnITLpCFIT2mmsBHG7sMhjSxcsw3gTQ_ErwrnGPAyWd5rH6pIKupb-8H2yPqyEY4W7esjjeE_UaT1xGePagNawMFzL0bkfEqklp4TBlxpa8slgZ9sEVG3TECtY1z6770LFf5pmZDaS3amNtx73ebQ-dv3sV3Jr29c2G6UHxofAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b2a11221.mp4?token=gb4jKxpkDAQ7utUkPsZjZNUteMi7PttLDcOaOfyey-Xl70T1CBOA-vG9rYcmSXnQczyezH3sOlg-oRQO8c4N8KoYqcTwK_cJ85GdIkN7LbANBEAp0VfvkO1_93wOrmMEX_rkF9GyEMtpniVMJ56Kj0lIpHzTmq1H_03ag2aRVRBnITLpCFIT2mmsBHG7sMhjSxcsw3gTQ_ErwrnGPAyWd5rH6pIKupb-8H2yPqyEY4W7esjjeE_UaT1xGePagNawMFzL0bkfEqklp4TBlxpa8slgZ9sEVG3TECtY1z6770LFf5pmZDaS3amNtx73ebQ-dv3sV3Jr29c2G6UHxofAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مرقد السيدة المعصومة عليها السلام يستعد لاستقبال الزوار لحضور تشييع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80455" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a10c2fa70.mp4?token=nbhNu9FVAgmMkmdzq1U7-dLjRAx_ZpePHNpmPC9Bzz-avlPNtpaO5_PVkqrUNq4bxwjUeCy5kfQzuPKhi47F7-8oAY1A9JOuEBZ0gq13wCUPde0vQh4eFD2_lhHLRy98LbXijo5AX44qWLN8XfEmbJwqKkE5_FFprg9nUq8cvcpOU65nPy356lu0vzR-koOznMSnTbeHy-7SCVC-MWVR7fwGvsYSCs6zwOK2jXI0ts09iu0Dq6aMo1dH8v-qSoZehCXZ8B6KJX7HIuzM0osyAgp1Ctf_B421LnDSKfWvuloRJ_zoTN18D0g65mVQLgfaheDLZyJ_e2SXzWeZwzZZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a10c2fa70.mp4?token=nbhNu9FVAgmMkmdzq1U7-dLjRAx_ZpePHNpmPC9Bzz-avlPNtpaO5_PVkqrUNq4bxwjUeCy5kfQzuPKhi47F7-8oAY1A9JOuEBZ0gq13wCUPde0vQh4eFD2_lhHLRy98LbXijo5AX44qWLN8XfEmbJwqKkE5_FFprg9nUq8cvcpOU65nPy356lu0vzR-koOznMSnTbeHy-7SCVC-MWVR7fwGvsYSCs6zwOK2jXI0ts09iu0Dq6aMo1dH8v-qSoZehCXZ8B6KJX7HIuzM0osyAgp1Ctf_B421LnDSKfWvuloRJ_zoTN18D0g65mVQLgfaheDLZyJ_e2SXzWeZwzZZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
صهاريج النفط العراقية التي تنقل النفط إلى سوريا تتعرض لحوادث وانفجارات خطيرة في شوارعها بسبب سوء البنى التحتية والإصلاحات الوهمية التي غنّى وتوعد بها الجولاني.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80454" target="_blank">📅 10:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
سيُغلق مطار مهرآباد اعتبارًا من الساعة الخامسة صباحًا يوم الجمعة وستُعلق رحلات طهران بالكامل يوم الاثنين.
▫️
سيستأنف مطار مهرآباد عملياته يوم الثلاثاء بينما سيبقى مطار الإمام الخميني الدولي مغلقًا لنقل جثمان القائد الشهيد إلى العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80453" target="_blank">📅 10:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2JeHmbVFq9hLnYbGw7QJ_R32JYNCWykzL18A5e-29q_Sx0PG9qNRphgILhNAhMMtpiST7ojfazhBdnvSfcPCm7h2PCerobCcwQv-8uYPAMJ8PCRrcUS5E8yDbCkf4h9zaMrZS6-yJrzsGABZxQMk-XlvyUbh_8PWh4G-LcFv7ENwiihKvrhPP7B_AdvQZM--0PaPimyvGJ2wm5G1aG8JSOpzIxDSWmopVORtwBbyR4nbz9g3sHt8hkYJu4t3lv6BofZgTD5JPTMmjeFaWWMvo_GS4l3Nn0eKoBHGmUGQGN9lshG048WnQg1ZvdkYzwFmAiZ5jvGADdJg6KA5_5pew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في أجواء توديع ووداع قائد الثورة الشهيد السيد علي الحسيني الخامنئي (رضوان الله عليه)، تم الكشف عن أحدث جدارية في ميدان ولي عصر (عج) بعنوان الوداع الأخير (آخرین دیدار).</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80452" target="_blank">📅 10:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd7746698.mp4?token=hjkzOtxK3fxvBUu6sGxDybBJZGNl4U_bFPFt34SSKVCnABp4Ff0JnzKirlxz0U2Ar1vsi_t8sWbnv02HCvWorBTd03IgfI_7q0zn_K_fhbiGCNE4Ux5grfe06QQmf6MzceROMEuNihWNC97CrWIyFFNhhvX_6FrdJj59yGWsrmqzzYEfP2VWjX8Qsf0K6_27ZLL_TJjUu5FPXC32Rh0N71SplSBMsYwUaSbcw0aHDvUcwMnkmxl4R0nZA46ajfiKgLEXK7pDUOkTEYY5ZS_wcWnjWAbuh8PVJWlDVeuraOzNwWYWSGGYwNIivPpAH985Y7V9HS90QJqtVQATaaZzQS1qYkupZpl8aJIGMEpRgt5sPLkIT4BNCX8XJqhDiSnNMjXRYgFVamZZfE-2EjmBAo6elCuSR_kxOOnAMp8pKQB9EYhepYwEM4GpPipb9tnc2KpBzkdg9RXWwiA0VOjvRv-OqvO2ZgOIat9XrN08gSX7obSvN75Zgl7sCWj9yzcbMFJkpiinmhLWYEc0lCYT6ZAEupZ5Kr_VYUNWnH3QQtzXqlIHiVliog1iRk95IGGq_4n7U23iJSBZc3YDBMDSFip5qtw691DRw3oT4iYvb6EHXxXEDNSuOq7HEd723f_BNSbW8HX0X9j1weCvtQzZjpj16K_kfT-9PhzTmlalsqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd7746698.mp4?token=hjkzOtxK3fxvBUu6sGxDybBJZGNl4U_bFPFt34SSKVCnABp4Ff0JnzKirlxz0U2Ar1vsi_t8sWbnv02HCvWorBTd03IgfI_7q0zn_K_fhbiGCNE4Ux5grfe06QQmf6MzceROMEuNihWNC97CrWIyFFNhhvX_6FrdJj59yGWsrmqzzYEfP2VWjX8Qsf0K6_27ZLL_TJjUu5FPXC32Rh0N71SplSBMsYwUaSbcw0aHDvUcwMnkmxl4R0nZA46ajfiKgLEXK7pDUOkTEYY5ZS_wcWnjWAbuh8PVJWlDVeuraOzNwWYWSGGYwNIivPpAH985Y7V9HS90QJqtVQATaaZzQS1qYkupZpl8aJIGMEpRgt5sPLkIT4BNCX8XJqhDiSnNMjXRYgFVamZZfE-2EjmBAo6elCuSR_kxOOnAMp8pKQB9EYhepYwEM4GpPipb9tnc2KpBzkdg9RXWwiA0VOjvRv-OqvO2ZgOIat9XrN08gSX7obSvN75Zgl7sCWj9yzcbMFJkpiinmhLWYEc0lCYT6ZAEupZ5Kr_VYUNWnH3QQtzXqlIHiVliog1iRk95IGGq_4n7U23iJSBZc3YDBMDSFip5qtw691DRw3oT4iYvb6EHXxXEDNSuOq7HEd723f_BNSbW8HX0X9j1weCvtQzZjpj16K_kfT-9PhzTmlalsqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم لجنة مراسم تشييع جثمان المرشد الإيراني: جثمان قائد الثورة الشهيد وأفراد عائلته يتم الاحتفاظ بهم حتى الآن بأعلى درجات التكريم، مع الالتزام الكامل بالمعايير الشرعية والقانونية.
▫️
لم يتم إجراء أي عملية دفن أو مواراة للثرى حتى اللحظة.
▫️
الشائعات…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80451" target="_blank">📅 10:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cb98fdc3.mp4?token=bragDsnP6z_y9FqUTxA228qcpcnKhgjw9NgnhKZRl5E090E2Ns5vROMQ3ZRfaPT1NimYqtU_RRqlUBBAaDXYaSZ6pwMbOAZiJWsseudlPR60_1vglHkRZdlUv6YjEbVt0RxTVVKJfd-CtT-ELt7Sja1QvPWEoi4-C_Ywd_Sv54rzOj6GkQN6W5cOSYw543snVLESb8lbNDSgJ0qGaDLziiZRjRIP_RaBykrhDy4nMdgLlxMURO547moHyUn0CAlSQ3j1_uW0fNVZ6nmro7eB_VV5W22kp96G1_9hkgdQXDrqznHqxZxv-AYYvD0tLp0x9NNUL6l5pVDQNmDn3CG-Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cb98fdc3.mp4?token=bragDsnP6z_y9FqUTxA228qcpcnKhgjw9NgnhKZRl5E090E2Ns5vROMQ3ZRfaPT1NimYqtU_RRqlUBBAaDXYaSZ6pwMbOAZiJWsseudlPR60_1vglHkRZdlUv6YjEbVt0RxTVVKJfd-CtT-ELt7Sja1QvPWEoi4-C_Ywd_Sv54rzOj6GkQN6W5cOSYw543snVLESb8lbNDSgJ0qGaDLziiZRjRIP_RaBykrhDy4nMdgLlxMURO547moHyUn0CAlSQ3j1_uW0fNVZ6nmro7eB_VV5W22kp96G1_9hkgdQXDrqznHqxZxv-AYYvD0tLp0x9NNUL6l5pVDQNmDn3CG-Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم لجنة مراسم تشييع جثمان السيد علي الخامنئي: سيحضر مسؤولون ورؤساء ٤٠ دولة في مراسم الوداع والتشييع لقائد الثورة الشهيد.
▫️
سيتم الإعلان قريبًا من قبل مسؤولي وزارة الخارجية عن تفاصيل مستوى الوفود المرسلة، والدول المشاركة، وأسماء الشخصيات الحاضرة</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80450" target="_blank">📅 10:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c0d32e61.mp4?token=UM9yTh1CMEzmqH7R4-B8C5iftJkvBObfseXx7z2op_M0kEV0ub55f2ecOgXecKS1CcWN9G6TvzLXbLWwiofYFPbwJ34HipoLB7-QZ84w08UrTplbILWrqsFLx0NOAjnP_WB9dfQIpX8zS0nd6jY3PTAKabE0JDgKZZMSz_iB4xFMIU3CB3KqIEwr5bDtaHEd_aKfDe9nK-FSQX5Cr6uoBZbEgYeLRqASma9Wcytjxi3tCvhUCC_CU7louqXDHWZ7MYQsKydvvKyFZfuzVNmpKUt874VKbePOeoIE7BalBlPrF-NgszffIoC-Icn8YgCaPb8uVNvW73y2wywdcfLc9po3PSelnJRGZC-csQAs5j24bUZUrGhbolJYD99JiVV7_rfxhMUWWWdU1xDgINxUeu4sR7mBEIlfth46ollMsY8F7FbQcFgFyWPYNNKBx-vl5ce2vFTotkzY9zUeLAXkfEmRO1v55cL6IV7BdXOlMMOi8mvnP_U9DBDWIbwZ7HbgPaP54e6xWJ3McURsPRRcOG0lndYwlHsrB3_S6Ms_X-ygEFU0MjjaSXljWWYYuL4p_l3qmuehQNV301lYzoFOKJpGOcQRIyuW36tRFnUfWF09kyFGMfSc5UGfkUcjykH24tuLahIBQirrRQ-9iJRjh9sPAIbp3kaxzBtvUP070lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c0d32e61.mp4?token=UM9yTh1CMEzmqH7R4-B8C5iftJkvBObfseXx7z2op_M0kEV0ub55f2ecOgXecKS1CcWN9G6TvzLXbLWwiofYFPbwJ34HipoLB7-QZ84w08UrTplbILWrqsFLx0NOAjnP_WB9dfQIpX8zS0nd6jY3PTAKabE0JDgKZZMSz_iB4xFMIU3CB3KqIEwr5bDtaHEd_aKfDe9nK-FSQX5Cr6uoBZbEgYeLRqASma9Wcytjxi3tCvhUCC_CU7louqXDHWZ7MYQsKydvvKyFZfuzVNmpKUt874VKbePOeoIE7BalBlPrF-NgszffIoC-Icn8YgCaPb8uVNvW73y2wywdcfLc9po3PSelnJRGZC-csQAs5j24bUZUrGhbolJYD99JiVV7_rfxhMUWWWdU1xDgINxUeu4sR7mBEIlfth46ollMsY8F7FbQcFgFyWPYNNKBx-vl5ce2vFTotkzY9zUeLAXkfEmRO1v55cL6IV7BdXOlMMOi8mvnP_U9DBDWIbwZ7HbgPaP54e6xWJ3McURsPRRcOG0lndYwlHsrB3_S6Ms_X-ygEFU0MjjaSXljWWYYuL4p_l3qmuehQNV301lYzoFOKJpGOcQRIyuW36tRFnUfWF09kyFGMfSc5UGfkUcjykH24tuLahIBQirrRQ-9iJRjh9sPAIbp3kaxzBtvUP070lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم لجنة مراسم تشييع جثمان السيد علي الخامنئي: سيحضر مسؤولون ورؤساء ٤٠ دولة في مراسم الوداع والتشييع لقائد الثورة الشهيد.
▫️
سيتم الإعلان قريبًا من قبل مسؤولي وزارة الخارجية عن تفاصيل مستوى الوفود المرسلة، والدول المشاركة، وأسماء الشخصيات الحاضرة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/80449" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
الحرس الثوري: أصوات الانفجارات التي سُمعت في بندر عباس من الصباح ناجمة عن تدمير ذخائر متبقية من الحرب</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80448" target="_blank">📅 09:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71a250766.mp4?token=OXILm9UbDwXdNTJxZ9waY8UvQPvPxADNJY0RiXTbI4kTtfycJxK0MMRateaLZwbpHjqAyMXiAytKtrxd_panp0cw2UqF9hByZ3NDBlrFKcpI4W67rQn3dkgWJF_VWpPCIc4ucpZpUdpLbuxZgTX5l12F1IwT5i-34wfDt5jZHVR8n6Fz-WTQGwZkJeNDFCC_3UhqqqWl7ru1H1n0bXY7eS2uwvshiFfGJxPprNh6OfvchlEDCfHQ1I9q-1zwNDYJwHKb_w5Vm02KXalQs0fGmRnyyhgLHLXw_8mVS6Pv8AbxWzCof92OGCR_FLqlhqMZ6CMIDWjmE295QoC528pVBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71a250766.mp4?token=OXILm9UbDwXdNTJxZ9waY8UvQPvPxADNJY0RiXTbI4kTtfycJxK0MMRateaLZwbpHjqAyMXiAytKtrxd_panp0cw2UqF9hByZ3NDBlrFKcpI4W67rQn3dkgWJF_VWpPCIc4ucpZpUdpLbuxZgTX5l12F1IwT5i-34wfDt5jZHVR8n6Fz-WTQGwZkJeNDFCC_3UhqqqWl7ru1H1n0bXY7eS2uwvshiFfGJxPprNh6OfvchlEDCfHQ1I9q-1zwNDYJwHKb_w5Vm02KXalQs0fGmRnyyhgLHLXw_8mVS6Pv8AbxWzCof92OGCR_FLqlhqMZ6CMIDWjmE295QoC528pVBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المتحدث باسم جمعية الهلال الأحمر: سيتم نشر ٢٥ ألف متطوع، و٣٥٨ سيارة إسعاف، و٢٨٠ مركبة إنقاذ، وأربع مروحيات إنقاذ، وأكثر من ٣٠٠٠ دراجة نارية إنقاذ في طهران لإقامة مراسم تشييع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/80447" target="_blank">📅 09:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
الطائرة المسيرة استهدفت منطقة الخضراء ومن الممكن كانت تستطلع سفارة الاحتلال الاميركي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/80446" target="_blank">📅 03:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59de911ab6.mp4?token=vUtHOVuiFM9h6eNWVgfAoUhzEpsnoa5u2ahx-6Zx3JgJkCQXTTg08TPdT9NoWahaiGCasnvWgMFJ2Byn9kRAS68xBQPdXyCiMEJu7KV2zjrL175WzrDgxm2L5WwWPbPTCsYzAhMXk-cLyfnixq9Arj2gsBSeTHAQOeUhNzE92QsnO0Z5wCX-lYlzadXizu-Pr8EfRd84Tr4TiDy9dv_Ho_I7GeAR8SgUxdty7Q69ZdYp5W3xC_B6GPGPbfgA3eHSXuBEqg3bDYFWPHupi75USV-at7ROf4oxNczwAJIw_2eU8KANmUXMfPC3fPCMV5nWgN56vW7OPs-71LC2uhdj4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59de911ab6.mp4?token=vUtHOVuiFM9h6eNWVgfAoUhzEpsnoa5u2ahx-6Zx3JgJkCQXTTg08TPdT9NoWahaiGCasnvWgMFJ2Byn9kRAS68xBQPdXyCiMEJu7KV2zjrL175WzrDgxm2L5WwWPbPTCsYzAhMXk-cLyfnixq9Arj2gsBSeTHAQOeUhNzE92QsnO0Z5wCX-lYlzadXizu-Pr8EfRd84Tr4TiDy9dv_Ho_I7GeAR8SgUxdty7Q69ZdYp5W3xC_B6GPGPbfgA3eHSXuBEqg3bDYFWPHupi75USV-at7ROf4oxNczwAJIw_2eU8KANmUXMfPC3fPCMV5nWgN56vW7OPs-71LC2uhdj4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الطائرة المسيرة استهدفت منطقة الخضراء ومن الممكن كانت تستطلع سفارة الاحتلال الاميركي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/80444" target="_blank">📅 03:08 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
