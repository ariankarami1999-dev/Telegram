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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 536K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 11:14:09</div>
<hr>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=bIBiLS5Qdt8e3Pzb_h1REWM5oRBfULqfb3nRiDMJ9I--ngPEhCcCndh-hQZS2ikfriNvcHg49TqTmvIos4oID_nl3OJiVS29FT4korWoX3qDgJWpf-0Vp-JT1tjITIRtKnWmk5Ybus4k5y15PzJeRzyOKftneBE2_MwSqph7On2XGydWW30UoGPxdMpRrEpCCViALtREw3BGs4GcTjgf9bDsRrqTweovzcGa2EUEBA3l-pDPr9XFDljIWpfFI5dORJS4i05C4eGnvqsw6LaLUx1uBupICVt718uUSHfSJ_De9uYgFgGXWbpJOvXmU4ZpxeHFX5hIbzWHgpOHuY9mnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mh9hyEzZoK6DkU7uHnmPqwZzzAJso8ujWYOCkchSzmfB69heDk3IHzZyglZJGC7iAR3e7TLlWUmTKREou48wqWqhT5QNkBr1-faMi6OtVaThMhRwez-hS4gOvckSQJ-imzFzfaCJGCwZlHR83U7Ku8FFmJvf4Uk2AtK2fyzkH0FzbBXWmQ27E2mwzPVImbFr7VxJxQP7Y-dWyirO1cuLuZa6BWkZbgJu1QBLg9y4113OQQMckKu7KVtv6UtvRozc2z2I92oP0ol0J64CQv5QwGXQo0nEyDJzBNqBgjfqpd5icg-M8O08cKAvLGAoIucaMh3VY7xXtWHxSHQLCDSeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ho8GSJojYmHbaxpDqdpujhSn960MEKzhlXkP8MGApwFpaJj6rHY5U_JsXevMzHO9YRGGI_8o-1qVJ7iEquHxWEVKF0vtQK9CkL-37jvtDphnIDdwqaeE1nHj1nL1yAJO61R9RfJKpBA9Ou_STFqyTH_D0897IDDENxRVCuJwiflwyOJjybjwZYaq0xkihOIYomtNLnCMtCnfuf0iE_kOevfG_XO7vvgHxATn4u0e6OWuV_bZqxtCOJH1aAVoOHc-brPVvrp5UhQ_glt9lETzBtEQp7uUccpj6qG5LfGRg2aj6zon4U_JU-EcT3rx1ph76jo5eT5jmjZ0gRRyOmF34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-lNsM-Adkjw7M_a2P90yrWe8aAa5GFPPW7NP3kn-bN4eiYDGj0RRArpZy_WCHOXTmNWrLH5qXDO7x9EWxbvQC_w7enDvXquxuKeh0t9-wWRSKm1FqRdVVDlS-Z8C6sH3hUyA-irrFadfdoOqlUSpn-OWRL83FqxNyyZ3pRVnt_9aOfosw6ktJTm3yUuSc5HBl-1rNySaGf7UKNMdRvNRUFANhtG6Wjt7KXcDJRBcE0OeMZ6Ig2DFwqnm9O7r-uIXzlVpqCTKlv3xAa6eUSsKL0QuGFFzNYqo6LeoCGos0P3KKE-c9z1-c14YBf_E8XI9S42hiFdBg_ZtaISf30H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJffoNMyL9gwqHSZRp-5EfYkv7Ci4geB_4ser8aXrsJk2MGWY88zcad_9eWx3QtZTu4gb3IRN0jJNW8fSIBi6Zd-l2oGEBRSU-JmEab2H2oEVzLe_WTMRxcbF5B_RPw_dImuK2N4wi9cNRI1j8-MKz_zxOjaqp_mWW_E89Xc6rERWEDby59MW4vDZO0FmMi9yRhz2OEOqwWeG-_NuE0CM7-sLGJ08NxstlEPoqx4yjRU69gaUTk-O2Pg0iSrpnxzZEpJAyLN_zVzq37gFFnmUOaiMgNbozuO4GczIyyV-kGhvLOHMVBrI0hjswnfIHg7JDhi0dlovsgwsyBoh5rqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbiCkPrT29di3jZuclRDvyiwRA0_9CHenN3InJ6uaJAQepUdm_96fxuy-bsag5mdcG5Pc15UpmnZtxmgyAegrJv9PbO3K3gpB1UUnKs6OeoM5DDfmI5CYV1HdNvgZwxsruTHvdMYnsYSz80RAhK7tR58X0jlhcKDNNnPMYFwrbYmxvxtcN4dnklRGvbNmZZXtP9VlX-Mu1f6LFzOI6wc278OwODaTm7DIC7jK6Lu7Jhjacu6dQNp2HFQO4py4azppnqei9uiU_MqOesbpLiNPlIeFUGgM4ySFbKU4jumDHZIStWARaEix7xoFb1W9Z6TlgbYf-Aa62lPt72v5pa7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeTqv4FXr31EsCdi8KcfP_MOaBhZe51Rftq9GLaUD2kdDBpwzV-35YL_DQxlGOWxpmOTrrS0GZ-zhmGDcAhPeify79h9sfllU9okoG7i4iJDhKY0fZ6jDriv9klxxtvQiJYh35k1NrdvzzXAQdZH7gIoPGyJUEZJ_VQrKE2XgV2Kgk2Awo4DMdtGuXF8A7bl1cMrVyrHpLXQxl43vFQX02fkdCMf5P7CZ2eV2afuI9b0PFbpbu9hB0RuzKlQ9_gHPeEopCvsO2RpeK3QMVVmaGZNzv8IKHQKBd23JcmU-Ti3KIiIk00VRDBW_JJIPJWRF5jt2QLJxIGaX0M6hczN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppM2Lnhl3CEtjq8VdrmBzYXigAeCEDzfM7cGakzXO9lX4q92aVE63LPiVs5QclSrkVnqR6NBkwWDIZ6vW58bxEMYasODJ8_NLR9EdJJofDW_2genE13KM7OQdleou8d6k36G5U_SDoxk_IT6olFDU5GOscAUvaKxOYjx2YK61H0MWtUW5pLcDiphoO1AfZw0LHvprzfM1aIot8vyrLcOZBW5r6S_FqD8tJ6yJ0YZPMMga__1YRwl58MgIx0PPqGJeGV-qIJ43qzTZVF0aNhmwP4B3qz1Z1Zu6DZ82-cEli2I9CYjbbCbJSUeReUDB1B7fkL9eaMLs0XU9d9mtFF2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLXiaX1BU7BxXFeqPwbs-Eankxn4fcER_1ASlQOvLZw5Y4j6KvgW81dtuPpM1Fk89tC69Kzesn2LnfMEm3psmsSm87fFURy5YE1Kv3h0hrgHU6rqeL9v71Kf86l6tQto7Zf3KyQRhOkfW_edD0PmgI-ObDm9UGYYKc7htVZGLLeNx5f9YPe7QI_neSo5ZPjSVxIjVMIsuKeV39w_iMHCAycXgd1pc29MZ1SiqYWzMid_e0yXSF0-9lZbdTEwU_pGcniUlAu4ONdGZxQOuYThNtrsndD_RlSBmAnFK7oxnz81c6Z37kkffQQ39ZqneY8z_KZhuXriVKVOu8AW4BujmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=BoUcU450RZ9ViSa7vP8PZskl3j4xpBRaSPAb_IzRzuXR-b46QDKZcgi3vAnsUwhcOZuC2mTxV6fjb8EdDy_VRHbbvnDaM1TFevD_DP2rNV2Y9DyfwDaLOvoHZQR1_zQhNN-bSczes65vY0q7Of-cegAO8jH-KNolmdZgtHk0y0ZYXp-fczRv6PwGvWsGUp_adDmUIR3bYciAfEmehGgvJvPkEa3a74zqCRWnW7SImymGPW00JL-jeIML1snOmykrBwYdUfenc0R8Bk6QVkPY8fPlGwitbnpw-edD2ukX-t-0_8TfKupDOJVmvU-nz-Yy4YlzVf0-egn4EGPFSihYKzV_eJRo9h_BYu9Iybgx1NChwTE9SMptzvPcYw4SvhESjsMEcAiWDOtLde4oZVNafheXtdAI-owUNhW2WUp4b3s1MQaFRAGfEZovevtTjDahsRNGRO1I6Dix0QqJvevDDJZAGuBv1dUNYP6EkOqPieJmChGfkPBbfmRJyzn9ntXdZ1NpMEL0ZEGhdibhpEuTZHt2dhP3m3eHagbI6WZx7LhY3jbOWvO7DPiVEOsyyuxhkcMr7jlNx2leS3l0qj_Flrf5VCAjpRU8Vef3xSghdM6JBe1IVxjJF9lLtwyV5sYcozVnFMwi8Urid2WF8ZcW1e5bEofAtpzXaI6HstnE7ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=BoUcU450RZ9ViSa7vP8PZskl3j4xpBRaSPAb_IzRzuXR-b46QDKZcgi3vAnsUwhcOZuC2mTxV6fjb8EdDy_VRHbbvnDaM1TFevD_DP2rNV2Y9DyfwDaLOvoHZQR1_zQhNN-bSczes65vY0q7Of-cegAO8jH-KNolmdZgtHk0y0ZYXp-fczRv6PwGvWsGUp_adDmUIR3bYciAfEmehGgvJvPkEa3a74zqCRWnW7SImymGPW00JL-jeIML1snOmykrBwYdUfenc0R8Bk6QVkPY8fPlGwitbnpw-edD2ukX-t-0_8TfKupDOJVmvU-nz-Yy4YlzVf0-egn4EGPFSihYKzV_eJRo9h_BYu9Iybgx1NChwTE9SMptzvPcYw4SvhESjsMEcAiWDOtLde4oZVNafheXtdAI-owUNhW2WUp4b3s1MQaFRAGfEZovevtTjDahsRNGRO1I6Dix0QqJvevDDJZAGuBv1dUNYP6EkOqPieJmChGfkPBbfmRJyzn9ntXdZ1NpMEL0ZEGhdibhpEuTZHt2dhP3m3eHagbI6WZx7LhY3jbOWvO7DPiVEOsyyuxhkcMr7jlNx2leS3l0qj_Flrf5VCAjpRU8Vef3xSghdM6JBe1IVxjJF9lLtwyV5sYcozVnFMwi8Urid2WF8ZcW1e5bEofAtpzXaI6HstnE7ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=treEenDYnCkZg790onkH76tT-cdI7FxT-12qh_Rse50Fzv3VIrrPq9MPaDxn6lleAZPk95iWCAB6pXAXkzIXLEFcICL55l98TKuh2QB47eeZ9vcG1Qy1tMdF64BrSo99GmP4uBDTsfwxbPuIVE8wgIDHS8LyTPqS9N_DiCeaQAi7L2ffDhIamd_p-5pygGG1JcG9zbdlmYtwl_N0XQxNv2muGhRc4QsDTxIMlKa5VkauY4BPpjzke1_J11ET-VFQeqKF8S7NJrkBxS1W9zdrgEH1HLijl12H12jhjc4RwhO-bGajJ6cdzx-L9r1CXB1642y0dCc0OI3MNZQopN42kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=treEenDYnCkZg790onkH76tT-cdI7FxT-12qh_Rse50Fzv3VIrrPq9MPaDxn6lleAZPk95iWCAB6pXAXkzIXLEFcICL55l98TKuh2QB47eeZ9vcG1Qy1tMdF64BrSo99GmP4uBDTsfwxbPuIVE8wgIDHS8LyTPqS9N_DiCeaQAi7L2ffDhIamd_p-5pygGG1JcG9zbdlmYtwl_N0XQxNv2muGhRc4QsDTxIMlKa5VkauY4BPpjzke1_J11ET-VFQeqKF8S7NJrkBxS1W9zdrgEH1HLijl12H12jhjc4RwhO-bGajJ6cdzx-L9r1CXB1642y0dCc0OI3MNZQopN42kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=fY3YNoz-0maEvWEK4x4K2l7uOFdRW6Xc0wlvlJ7bRGiCe29JFwScO52TZ8Awd90inlhyP_hi9QQzvOPXfnEEMH0Xpqo8P1pAr50YyeJ3Z14U-G8kPjJxeSmG9NTTmXzVuMmuKeeC1gH-fJmgHIV8WrHZ49P5HN5z9oDbOb1Ujjv1rObrFyEJgIHdM_OMLkhn0HsLe-OIKhm4VQcrePJZkyzwSAVXGWS7DrA8GWREhUnzlF-lTyZ0-TExC2m6T7UM6WBU6ghFF0vqs4cK4uRVQdyutljlBYyUnl76kRGfG9FNpqCktsaMY605g2byOUEioiey6ZSzWGU0-WN0uTGLgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=fY3YNoz-0maEvWEK4x4K2l7uOFdRW6Xc0wlvlJ7bRGiCe29JFwScO52TZ8Awd90inlhyP_hi9QQzvOPXfnEEMH0Xpqo8P1pAr50YyeJ3Z14U-G8kPjJxeSmG9NTTmXzVuMmuKeeC1gH-fJmgHIV8WrHZ49P5HN5z9oDbOb1Ujjv1rObrFyEJgIHdM_OMLkhn0HsLe-OIKhm4VQcrePJZkyzwSAVXGWS7DrA8GWREhUnzlF-lTyZ0-TExC2m6T7UM6WBU6ghFF0vqs4cK4uRVQdyutljlBYyUnl76kRGfG9FNpqCktsaMY605g2byOUEioiey6ZSzWGU0-WN0uTGLgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jp06njN4ceymMnrx4XJyGrac19PfbWuEUzekpn5HX_iXFp24rwmmH4hsmeLy63r1AZrCa72Y-aNZdWmDhsAOWaN8SpUdNThCNPTSfr1my1m9NgYZsQt09zurtsNqJwSLoQNytxOiauK_ewQOAnDNRQ0hVrXUcNuCKKDVta6kEhvbQvdtW_nm2WCdFEljIGKl51MN0PE5pg8I9gdMfa8bOCcRg9OZyNQ6pduwl6eNn-v0utUK84o5QPu_CKmed3cWwWD5hsK3LzDwC8fsouS0El35qqQkMP_wtFHrl7Y_alUqcfGhydQWxVNVhMXMQmvQeKuqyzgygHnWRWXVG1mcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOllJ3kw49Hl9kYOPu0-IscEI_JKhRcmJ5q1cbzPNFFMHdgAr3tYZDHWVCG8alNRXsxJbMzey8Yb8ldYQj__pHOiXtO1dLuqVmge9ta3-pKhgbhzbk-CWd1ZXd0Rd4CULZqHdfUi2skSmsMbB3NT2gxsTMOT9uhEo0pm19H6o7TzcZe11XxDb2ejO6eorRQj6cviW-DqkO2VCYVB0CcAC3TP5RaJTbyO2nMVsWJ_0Ur5uHasZSF0VJTJuIBEu_hhyQTmxj0MyikcYpHPiG-XoUICux4RRqEkxdCotQntkAq0w9Wn0xsECdtYE6NlQzGg6rv9NHBkz7i4OJ0QFIXL1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJCdXqw-DK6kEBx2EAthosXT0Utb9d8TWunSy567rg4YlmqZpDhj6yQawUvBVWiTo8zicKwSnxdxiPV4xp2d6VnOViQ9oFBJ5W7LIsudKeDYB2QzY2DQqW3_rVgbUP6aaZetEkQj2eF0z2EQRMuiMeMuHmHXz3zMM3nCt3yBWaEyKJWTNmdSPvmYcR-sdB6dcJdkwBcmCuUZXm9MuRA4ACTwHckThXz27XOY8q9iiXL20opQckV1NHIyeRFKfo-3SMTRsCKT383gpyZa_ZLLHiRG68bGtnXy6WH_7IzL14_Xigy5v-tFW4679EakJOp6fxm1bDS8x_7sKIBbSEA7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlcvSWecC7JpyvHPedLw-VTnpkO4mm1gNwjCS2mjcguV3S8aIqL1Di2RLX6zyUW1OqHeqdaJ8tuyqLh6SJpao4kiTXn6nZ2u2jGnFX422OTK6L4CcVShJR_4wbVx6T-Mu3EMp8K7qXU25-Y661OsJ6OpkRazIBS6i6yqBZXkfVOfNJk8dokeqWctIj3oo1HZwzOYs-594y0bOR9QGUc-rQOr93eKLwr-2xhUJcVP1S3FjVgeYfrSoaA8jtwTvZCNsdS9MUhaRlbhpg_oG1yh21BELCLkw1mpj2IPxw1qHrcO-jxjWdxy4DxpQOtbCwcPtUQvEgDlhYb0Mm0rHn8o7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEe67Irl96v5ol8hFIBOjT1vTJ2BtQUBmh-UMM17rlH_NNuCx7iLNdwemLy7i-VMPt0rrcUcWQ-NtuOrUUR1aYStT55mAk3rY1siT_Sfkh_IfWfVukdP4Qgpx_Q7oXic8Dr7xQt8PuA9YzT8EnOrlhBQX7XqASEPY5BeCtZoBV8URSJLz7AMZnGbccfx_HDmGGIRdR04sdToYzvnwnHr7TxgddABwwb1m92ZMfBFwTZnWAq8Y21m9z_ycu0F1xMAMPM84UYxCOv-RGLONX0sh6qJS2GgGhAVV2tIZI7yC_NIaWdF64vGy8Gcxg-Xvg9lEc42FANtQigyQMpY9Juz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEica0qraJ5-WaJbKww8nmuphqd1hEPkAoI9AJe83Go4onFXL0iMNJ6vUoDD75AumHOtiSABLnd2np9kmwuz061IGkMHS-_qT_4_R99blqIFXWp99DZzSnC72wZkDR-FPFZqAUkTXgErvP3rvfBgwCR4-nQ0knMMfWruB1FJxgiGQoZxac2lAyMIkAibgdlZXDglisTsmsp8XOL0n3_LNrwsAD-Ywwm0Dlk1wqNWPzX1meY0v-yIdGEVBUaLrYRqeDZh8xiIZQejRIumSU3Auj3Y0FN70utrFq_aZaqyYWfEv5ChRNGA0uiPdSuZbRQ4q5GPtUrSlT6CVjLjXmtAAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEqQcidh5cXrbfFXfk2Wu8k6FSOPx08iRmqw3gnV48_jWa_T43AKzph5o_LbRUFS_TqaqC3adp6Hj8xGd3kghdLk3Ob62bRA89X8kXVwqC2MYR924hmhsUo01mtOL8i8dZyqzRdG40bxw_XreJwQnBT01JHiafHSr1QVVHx-Ou10NbZYHKNUFxwy2tLevBUuN0i7W9U4bVbEV6__DrWgM7Dujh9TnGsFomRqUVhrjpE3hcvsIFiqS3zBxfHUEaT28Jrq5ZqZpI21Bgkl_gsy3ikEzgKIlkquQ8yQQM301CnidJAZNaNvimXbMvn9W1duh7eVWdx3PEMxsCtgIbby9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWwX7iIfEVhH5LglNDnCGmne8aqrzdoH0b05x0jo31ZaZbtzWYd3VKLRAbYTUuir3EIZHnGsgxmbyqrfLiOLKPuGnFmlQO4AOHHdZXSOrf3_CRawNMp3FMGcD5fjVVzPge2CwVvaUBGXJNw40UsXzQ6g69yb2opVWMMQIGfTYuoj_mIaZeOBKXFEg_aklVrNhqOwnD-XafkKA6zkZ9RjbcNJUvPRN8r49_rYOoy6Mxq3jVnR9YtEvCKdRnwYeYNMpp8NachiN33qXbdM-L54MOqd053vheV2tih3ltymbtAPD37jA4rhTSM1N9ePAvdp80oePkCl6tpjN3Tl9oBzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=oaZxctSlt4NGxOrHzMFNTDW1kGxyAGz-YxZcsPwQvaEMRCspNDkgPtErnQ8tKW5na8blJnNWuERNRa3bg7MiD68H97bW46f67vqSgW69pIRqdgvLWzhElBGycIeD0HwE--ppLHyvZziGuSSINPtwnAknZaUfhvrMu8bc11v5do-7XE44Rrtn3a6o21zmYg63KjbqxltEDD-urKvMiWm3Vai9KwBHFKQxX21LsPL08HKj7qFUSz0yHm8QrHhdG6G6z5VE6yfhXFyko8ckVAM8CKFsigNfXizAPKyVQsYc5FkS41e-jW6G3tcpADS9_QA_jEun8m692qcTGHGaq8efQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=oaZxctSlt4NGxOrHzMFNTDW1kGxyAGz-YxZcsPwQvaEMRCspNDkgPtErnQ8tKW5na8blJnNWuERNRa3bg7MiD68H97bW46f67vqSgW69pIRqdgvLWzhElBGycIeD0HwE--ppLHyvZziGuSSINPtwnAknZaUfhvrMu8bc11v5do-7XE44Rrtn3a6o21zmYg63KjbqxltEDD-urKvMiWm3Vai9KwBHFKQxX21LsPL08HKj7qFUSz0yHm8QrHhdG6G6z5VE6yfhXFyko8ckVAM8CKFsigNfXizAPKyVQsYc5FkS41e-jW6G3tcpADS9_QA_jEun8m692qcTGHGaq8efQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=nTVbGYe3zo3qxxJw3tt_VkDrEFevw0CLCqv8eRQtk8RPFu8Lzfy3NHJ4sTqLPDAqtUYZU7IIAbndqZCrQ9INe9slsJ5fOi9IaTc9yuZ4dck6o19yzsmUnumGeaGwEMLdeAZiHPg2_PcfqRpO7M5jg5y9sUHWanzoBfl3iNzWrx6BvW1O5raktQm0Pv7FZ1hXwJ261Bp8siQVU-FMG1C5WiVDvQFR9KU2F6T5gj2FIYpROcONonJvABxM_SNRJeMqDmfqe9LW3c9GWsBPWWvr6cmI3nPi4t112oL3NUrQbUDEyK_fKHti6zP9PJCBzfAjGw7f1q5ERYvNo_d84NgGajXoQ22Ripu9IUCzXKq413cz_9rsdknqsMO1XvqajqezDm5XXwuyA2aQUF4WUrAwUagwHaGSAeyFfgicuCkg6ojskmrCHLdg6P_1Ec0y-f53I292wmhZHC76eoYjXu4xMhHQoVYH-zCQQlBSMUtFuRXJfBxe6itYJ1e1kEg5WwnVYMmS_QEau4irZ4oOET3naRfAjTj8ypBnYpYkbm2e4U-3zM6Vm0mqgI9QZhM9tPQ_5BVF_gnX7jRCzmizOcr1vaiI5p1-k2j1-n8uOQhiK6-rI8ZoiIXt0hTsUUSAhtamqKRRk_dQm_lMkHO99VSsDUUZj6QZYq4i_bcwT-LQ6nk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=nTVbGYe3zo3qxxJw3tt_VkDrEFevw0CLCqv8eRQtk8RPFu8Lzfy3NHJ4sTqLPDAqtUYZU7IIAbndqZCrQ9INe9slsJ5fOi9IaTc9yuZ4dck6o19yzsmUnumGeaGwEMLdeAZiHPg2_PcfqRpO7M5jg5y9sUHWanzoBfl3iNzWrx6BvW1O5raktQm0Pv7FZ1hXwJ261Bp8siQVU-FMG1C5WiVDvQFR9KU2F6T5gj2FIYpROcONonJvABxM_SNRJeMqDmfqe9LW3c9GWsBPWWvr6cmI3nPi4t112oL3NUrQbUDEyK_fKHti6zP9PJCBzfAjGw7f1q5ERYvNo_d84NgGajXoQ22Ripu9IUCzXKq413cz_9rsdknqsMO1XvqajqezDm5XXwuyA2aQUF4WUrAwUagwHaGSAeyFfgicuCkg6ojskmrCHLdg6P_1Ec0y-f53I292wmhZHC76eoYjXu4xMhHQoVYH-zCQQlBSMUtFuRXJfBxe6itYJ1e1kEg5WwnVYMmS_QEau4irZ4oOET3naRfAjTj8ypBnYpYkbm2e4U-3zM6Vm0mqgI9QZhM9tPQ_5BVF_gnX7jRCzmizOcr1vaiI5p1-k2j1-n8uOQhiK6-rI8ZoiIXt0hTsUUSAhtamqKRRk_dQm_lMkHO99VSsDUUZj6QZYq4i_bcwT-LQ6nk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=kOOCEDkFaFmZyp2VFDUCppToN7sgc38BdAYSqJsjehrL2hlCosqYJqIq5onp8qp4Pxh4jVGU2HMP5Ww0zaX3__LLHtyfIPE_jj2iphHZA9-MJF3-df97yLNSivqPLYSJigl_TIN82cYvIPQsN0YYez4FjfvFbnzwlbb4BQ8aVyiO_Ca2KRVkocFL3S9OX3uM-16rcbnLcBeyQhlMq6aDsiDH25B8HIjlH2D0Ol9M1_wU8ZJuzgGdJx2Zn46e5486Q_lSCxqnlvot_dcyxMsI60Azy2aMVDcqK99l7JVI6_v3d7QinU2bJMmc4eT0mJ6_4sUY_PP7jrAggrVHeg9yrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=kOOCEDkFaFmZyp2VFDUCppToN7sgc38BdAYSqJsjehrL2hlCosqYJqIq5onp8qp4Pxh4jVGU2HMP5Ww0zaX3__LLHtyfIPE_jj2iphHZA9-MJF3-df97yLNSivqPLYSJigl_TIN82cYvIPQsN0YYez4FjfvFbnzwlbb4BQ8aVyiO_Ca2KRVkocFL3S9OX3uM-16rcbnLcBeyQhlMq6aDsiDH25B8HIjlH2D0Ol9M1_wU8ZJuzgGdJx2Zn46e5486Q_lSCxqnlvot_dcyxMsI60Azy2aMVDcqK99l7JVI6_v3d7QinU2bJMmc4eT0mJ6_4sUY_PP7jrAggrVHeg9yrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=CocrBtsnVu3aqNDSWDUSJxQyRRS2KSQxLr0E6c9pBDhj2CRIX6N1UYzMcbTyMYo8lEQVSwhKZmk9lzhk2gWSTY4mkcUAM1lIrZK71IUA_-DUp1U8TT8ynGsRshrq-4RN3KcgAHayN0ctZUEIPYaONQxMhezbCsYMt_B1o0UoMqaAQLbRDMsRgmvGV46n_90iT7bpQH-ieXXgdLKf5QErlcaD43mxOgueJY-8631kNdYYd6YI-x9-SrGm9L5XJOUpO5HNtCDExk0cOI7h1WylPiTtbBNEw6r1kZVCbgeJvNlktaN38hNvEAAmfwJzy-mczNOTiViSZO8mfNrp5T1sTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=CocrBtsnVu3aqNDSWDUSJxQyRRS2KSQxLr0E6c9pBDhj2CRIX6N1UYzMcbTyMYo8lEQVSwhKZmk9lzhk2gWSTY4mkcUAM1lIrZK71IUA_-DUp1U8TT8ynGsRshrq-4RN3KcgAHayN0ctZUEIPYaONQxMhezbCsYMt_B1o0UoMqaAQLbRDMsRgmvGV46n_90iT7bpQH-ieXXgdLKf5QErlcaD43mxOgueJY-8631kNdYYd6YI-x9-SrGm9L5XJOUpO5HNtCDExk0cOI7h1WylPiTtbBNEw6r1kZVCbgeJvNlktaN38hNvEAAmfwJzy-mczNOTiViSZO8mfNrp5T1sTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRgc4QTHrCSLBWX7O0ohSluLmDrJex4FBkutOCWEhoQ1DFcfsVyRbIeZimchQPBj98lftfLPmIrKe4VLgHC-_Gbpn7HvbiDrIR7FN8IiWTfb10FVCtZYZFAMJVFq3OAUXhni_GveO1DtwE0ktklqn6o0RVfU5WxB2tMBuYP8O7nwsx4BgTVk-z-AwsQlr-F6YcU_HzbY4LsqsAfscqaSpyXFJzCtD4Xq8kEaZGgFXFPwq4btxxHQKoEFchFJgsijkDvT96AXcHNZ6ZKParOeGKtZfk6t2LdXYD8lIzBxv-xaFmdgJ89hZw-1qs_NS8E1JlV1kwQb7-jRSrf3wu20sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=mELIPJNLeLEnf6PYOz38kTL84F5coZ5gzTYXgA0k2x8NvZaSuHwuJBiAH0wpGTbNW49epcpLHprHctvk6qiIeN7ybTBfoywjP46FZzL2XM1oxOrKkHg5Vts6Fz4_QTzAU4YOtRWn1N4-NM9XHWOr46i59uULw0u9nhzskpqOAYavBTTIpVqemGSGrFAA2HB1g4U3VFCIDQTqSB4xDMkesUy0OHQ9kUhjWF_-8mdQdv7eMt24aB8-qZISgLra83-9FVKKTwgu9blQKLEgZ_uPA8t9Cgsp0IP6QFbFKjG8nY8FyvQ64kSBWjfDS_IyD30585XqMGp8fklvN-n6KZF2Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=mELIPJNLeLEnf6PYOz38kTL84F5coZ5gzTYXgA0k2x8NvZaSuHwuJBiAH0wpGTbNW49epcpLHprHctvk6qiIeN7ybTBfoywjP46FZzL2XM1oxOrKkHg5Vts6Fz4_QTzAU4YOtRWn1N4-NM9XHWOr46i59uULw0u9nhzskpqOAYavBTTIpVqemGSGrFAA2HB1g4U3VFCIDQTqSB4xDMkesUy0OHQ9kUhjWF_-8mdQdv7eMt24aB8-qZISgLra83-9FVKKTwgu9blQKLEgZ_uPA8t9Cgsp0IP6QFbFKjG8nY8FyvQ64kSBWjfDS_IyD30585XqMGp8fklvN-n6KZF2Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE9sgzULPNnNT5L0RKWgmCXR_55LlaI4oq4IE5a5TKR-tQEyED4TJwm48QdqjOSKxqWDm1YYMAbIFRC-jPyBYbyJfw20L047_bY-HF7FTkZ1FE_iXplxUPkCKoi5GJMXo69ieNelq9LbHZ7q05pRWnkqc3UQ4EpfVLowbSZifwYBTFzkgZzIO-J1mNLHBtXFPLFKPslhLwjeoVl-0Y9pisosA0foWfexwIBD7xwggKswQe4teafwqitOFLfNTQ2MCjd2_xb2xTVxxjW3_4cfhlEcInqz3Q2QvNI0JUO0ZfrnZC751eYZHfVKWHbt4GAD_Ob4QZ2KDsdyS08owqEpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWfJ1iYXEvDUYRR23cVk0sQlH4CYGu-D86qZnWJYm7K01cOQNnh7r2FiiARZ8fit_CqXL9KwC8ru4eMLeTPgWjyjyagTLj5-nUafdXhA1DZhsJc3S5-nIKVT_0_dV1Kx50S3KLFDCRmW0riC2VBq40u6mmLxKJim0vynIOdtjZNalQmYRwWcCezZ9b64p_k-ac3vSuC3KTFccetbGr0tw-E98GX3LsFChhD0PjhNgLGqbMH4I0esQ_jKZffDn4BpRK0azL6TFW2V55OBDErfMvkOycbEFw6ezG9m5VnpPxgtrSYX9q_5HXPahd4CZXI1bL-ruAMQmw8CjQt9kU7hxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=a6IbRGRSPETUkUrl6dhgUL_lsegTqjebtbNSf77RJhBYO4a2GrJ93-m8O2mmmQOMvO584AY6sBi1PX_5_wRFs5FmCXLEORMjTiWExllkrDUESjQc3YhJWUKgF9K_LzSqjJNSqyIkLItZMjV13BO9WcUnbglWAmtZqVLuf65fs_QNUeNe1r2-QpRX7QTQ2HoY7K7HvPKWh01nQPpO_Zoqs6qqjLNiz4Wfh7P13CT-aSFUe_8mdS8sUa5e3wp5y6imiML-f2kp_QrvmSD5-A3WgfPdafgEc8BF2IQKRSkZaBOpF4XdzvDG5_3UMoBAZtNT0jHtd7COrWq_U86IFaEI3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=a6IbRGRSPETUkUrl6dhgUL_lsegTqjebtbNSf77RJhBYO4a2GrJ93-m8O2mmmQOMvO584AY6sBi1PX_5_wRFs5FmCXLEORMjTiWExllkrDUESjQc3YhJWUKgF9K_LzSqjJNSqyIkLItZMjV13BO9WcUnbglWAmtZqVLuf65fs_QNUeNe1r2-QpRX7QTQ2HoY7K7HvPKWh01nQPpO_Zoqs6qqjLNiz4Wfh7P13CT-aSFUe_8mdS8sUa5e3wp5y6imiML-f2kp_QrvmSD5-A3WgfPdafgEc8BF2IQKRSkZaBOpF4XdzvDG5_3UMoBAZtNT0jHtd7COrWq_U86IFaEI3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=PLP23K8vul_xJrobCBcq_QPbEfv3NVWYkBy-rbXIa-Mz87xdBX9Xe4fA76ltHn3aEj0U418_Brn7Kxtwn0UGSSplxNgxfdYglkNYyHF9a4UxydkNY4idR1ItAqx_a2JZxjeADBE8CPpUIjUPdBF5VlxJCpRRbQE_v7XYYYcXTYHrVA522cFz782VuXg3ucL9bc1prjpFDPzHA4p4jjDkgpCTUPt5qblPJpO2KfjWMJo75eYjFoT39o37ih1_vuKcr25MH8w83sXhAdLhtpZxxOIb1H64yCiYdUcoirVk2Zq0AcFxoWy32GkTxmKPVC2w3V2Sz9WLu_LCsbeZ_Y0yfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=PLP23K8vul_xJrobCBcq_QPbEfv3NVWYkBy-rbXIa-Mz87xdBX9Xe4fA76ltHn3aEj0U418_Brn7Kxtwn0UGSSplxNgxfdYglkNYyHF9a4UxydkNY4idR1ItAqx_a2JZxjeADBE8CPpUIjUPdBF5VlxJCpRRbQE_v7XYYYcXTYHrVA522cFz782VuXg3ucL9bc1prjpFDPzHA4p4jjDkgpCTUPt5qblPJpO2KfjWMJo75eYjFoT39o37ih1_vuKcr25MH8w83sXhAdLhtpZxxOIb1H64yCiYdUcoirVk2Zq0AcFxoWy32GkTxmKPVC2w3V2Sz9WLu_LCsbeZ_Y0yfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT3mZwSd9rJx2xLMIyoDO1mSsfj6I-RA_SLs2sTSnmw9CluDYSvqOIoIWo9itGA_l6MLCsnGMSITWqxN4cMHqOQO783UL0UxplirWLs7YHNLHfe6CNhUDBHO1UGfJI-OZ51cs_popUhAtUfkn_Ldqw-wSWSxgz4jfriwO3FophdyuKPUy5T5g_lnzZKTdd1UoT28DXEuzCSf0grHbhw6G-7qd2lB3SiEiE1Qs8hOTU04o5OMg7XgnknxZueeUZMog827KjXQ8j5huroCtQJSLkdQ_cVw88x3E6nKwRMyL8d_IOTzyq6UF4EaFp0R36177ky3dCkXyVJR3kGCYW6ujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY0GAX1GE585Ga_-sXNCMRUWO5YoP7Jpg1dV3RDru3BgUUFPfq7XaW9U_F_ZMfyDRFeLhhecO7WR3y-a5J2cKSzxzw0WhBrm7kfJRAQQP48bAsS5pJzaQTFErKkfVehm6PBsjFDB_yo3zA37cMUIAj3uBozPYm0B_JpxAu3NmETm5QKpQP-ZNCOTtZBEe-pSJDXegRBdHqkp7DG_RFgx_tDQUjsQqNVOal7eNN3y34lEUOgdmEQXeOjgJyv4KOY-0qv_hef9qv3eO_JCi9FYZd2HqbC5KVtYz0OlaHpw_-UZlpDlcNwyQ8OUSt3UgxKjNgexexDB6yTqPyIUBRo15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=dPDccm-ZEelcqwtFTv8wVMOAYHiiEvtAcSd29V_IshGTpveBwMf1KHwmFoCiW5m8ud9X9mQg6JtRFM4ZIQ7IzedW_OLd86p13DSj2hm-kOAbrhBvjTaZ0P9843czpIax8XH-jMWj7EmDfTgcJM2MjsKNwqfr9DSg265qRmkXTPtEN2dMRX1J764sFl9xohYjfzbsFt4aaV-h2FjvBfirNb39JQcO03tdsK0L84d1CzCXWrKpdMTX9dX6lasg9A7FkeyXeD1COEZaVuWWDyNht5DGdQwWGTUq9fFxMmlwZ-ETFfxi3xrolUIUREU-4qIv2IWTz8T2XSADJ_57uZW17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=dPDccm-ZEelcqwtFTv8wVMOAYHiiEvtAcSd29V_IshGTpveBwMf1KHwmFoCiW5m8ud9X9mQg6JtRFM4ZIQ7IzedW_OLd86p13DSj2hm-kOAbrhBvjTaZ0P9843czpIax8XH-jMWj7EmDfTgcJM2MjsKNwqfr9DSg265qRmkXTPtEN2dMRX1J764sFl9xohYjfzbsFt4aaV-h2FjvBfirNb39JQcO03tdsK0L84d1CzCXWrKpdMTX9dX6lasg9A7FkeyXeD1COEZaVuWWDyNht5DGdQwWGTUq9fFxMmlwZ-ETFfxi3xrolUIUREU-4qIv2IWTz8T2XSADJ_57uZW17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=Qx51gEOKzRgMTBkIPG5aIp7uZ8ZY9ANmDvJPzD3CMRJzC-BGxFyLShlsWJkwmJF6dxFYY1kRk44HRTmP11xb_VaOCtoWs4929V9LSRgWN_R-VeliaPCRiEY-6DS3jjOk5YhJvkV239y_vVGq27G5RbtRe0dgK3ma5Mu9U9OhQ_pJmQz76VQ2Geh9gxggCXbV4Mq5Vrti-Q-Zd0TOKIklwhHW0LPnVpwaMYXhoici0oRKzjXpZC3_I0WCN3R8SW6CD5iPW7-pcvEao_S_uHQvmvUnGqM_38ViuwV-jJB231gnVZInsGnRNlrxpq38Gu_ePLqIfybtC8a3GlQ2wRsiTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=Qx51gEOKzRgMTBkIPG5aIp7uZ8ZY9ANmDvJPzD3CMRJzC-BGxFyLShlsWJkwmJF6dxFYY1kRk44HRTmP11xb_VaOCtoWs4929V9LSRgWN_R-VeliaPCRiEY-6DS3jjOk5YhJvkV239y_vVGq27G5RbtRe0dgK3ma5Mu9U9OhQ_pJmQz76VQ2Geh9gxggCXbV4Mq5Vrti-Q-Zd0TOKIklwhHW0LPnVpwaMYXhoici0oRKzjXpZC3_I0WCN3R8SW6CD5iPW7-pcvEao_S_uHQvmvUnGqM_38ViuwV-jJB231gnVZInsGnRNlrxpq38Gu_ePLqIfybtC8a3GlQ2wRsiTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utPP0cOMj-24S5810Uw6MuOAAQ2vtldgmNJXjzHWCN6lczYSzLRBuD9QbGW0PpqFY2Ej8u9aHG7XHOkemSmyRpDmWqBitX-9ECIUcH3fEjbVFb7Iyu_gH7Zd8OIwDiidIW-ctCGGXwU_LcwaiHMcRkDjmCOzawxyJyqg7ntRQyfoRc3jm475h9bSvOZRKp1UC-fqBLOlh-YQDTXW8FRalEmNTJ9vcgpN5yxit6UbGGRI5u5LWbc3ztjG0KWO_BGnrstKYgsrenE_7_4k7sExKJLDTT-jzMxurrydx7EUITSKQ2WnKvNPqk_U-42ufBq-3cBMHMmfhqnRqGsYrj2uEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2tRimWTdH1YUTWmFjyw7_wbB-IwpviqrpLd5WRF5WpubB1Hsi0tE_pHV5rasLZ2GF1tcI8GZ8BhicPV99AK0W1euXzbmyFzrpHGkR4QFfvjzZ-WKeqwfSZpr8jrSXPReCyQgFakzxZNl1lf47-8smxzUXELEFeXXBe5du2_miJDu7SzlAA5xUDECfpuYSrlouSRQXFeR7SZtF1CevcDx7SWGrLLXcmzXAnZ2F-kKNJNRlxXB_5t5PTGPAw0nYwpoXj3er7fAUSJ9-qJXn3bugfSLbLOQSfKn35PpFzTTNjKk2UBFINWkLKSvLsxkkPbz8DV7HS2Jbi6WfkYuCROkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH3V7p8ls12R3L2gGM5S0cZiZGeEzPRe7gqBAZ87jZ0G5ehAHKvn_wx_KDh47Qr7zT43YFmgdwvCOPA7Xi5S9RBZtn-prm7Ks8NTyqLIEK2cG3PxRDOC3b5eo-JF7DIiOEOHN-jBXOENwbn32F5oGTx_NkZHg1d7p4Nk6OCyQ-CRQ7R1VYIik4GHGLcm4S1TNsDxmOv01V-8eTAB0-JzSXOXXCr_lKayBY0lFmXprsr_2eCRUmmKzJqCYSSqkEp1yhLUNt8hA46PkICaVn4nw4NKdRr61rvqWP1JxIt98dikVIe0KnkTKIKuGupkZ8my-IeaMkwMcFW_02nBovpEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GRtTNIFyTx33WdclxNlph7cDXA42OoER4khwL2ZUMsi7myizFdnsEca8AprTbmYF-JgxAktYxKYgL743KzPRQO1NkiEAlvsnCOgDOQPCnpqbQ44IVtPxeUFJISPOtG3eWkEORFFtruy79Q0GJoVhXAV_CVubifJfphfFl863RKxf-H1XegUPKwcRiiY5QiMG-FWU8MsYWjxMqktH-aFk9b53hbpvOxysB-q6MCttU4gQFsf8xxFLEQei-CFdugt4KdqOZQcdjJG6FHL5mrpvqp7smrIbWwMOOSAO30Y5Qcdoz68ImqvIUGjTjd0wHGMpDuxebNO8CkoQagOONz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwQiERcKpOA8yxBfXximaddC0TZh4Tqo9ca-Nx04bv5DDqtdcvAMoReNugauWVT76PKkkSzrozCSHLGDJIHTTh9H3K3r87MWlgoI27zhJzfWdKETGPIdxuCAgAY8_K0-040DO9WZqbNnbEWMhQtS6KNhLzsVn_aFZumNk8Obu-ZgJsYdHKb2ZMUyk-WauqBxhL59FocFDw9Yx5R6QzMHPsZ8voPFem62qvm5sfWZKC7fbDOGlXo0SUW-4kDncmnSuLsa-kSZLVeve0KDYj2zyk2KqemOhBJIpeh0P2pqhNcrVP_8cr0EiD2eg1VUyFD6nZ_mHu3l3rrjcFtVwtxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcWXnJpKYRpwT4MkIr3gx40Nc0PFpZ6XPdvWQINqihnu3C2C5LT1BudJXvZb-l39Zwt0mdKcPaMN9Lyv5pE3YDTgPids2JKlJbN421LXMqXdUTHTnAAysZkaxUETAo8uX0bcC7eN44KveduoQsTFfS-mowwnm02RpOdfgCi5KQdRrhOvr4yBgjAv6H_c3iAqAeuvO4dsBqUg_ay59W7LrG0fz2yJ_btnCiIP-Gn7syBOzsA8oOSt_vO8dZqjdDlIsnMyCD-9ssSYWkd0DzkeUbz-9OuyBKNf2M90AhchSvdAdgjpx0j7rQb1BIaOHnUKT1bxEu8PuMTgwdRhyaQjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMKT1E0a0Y3Duj847s1aPi3yVZtsPKFyjw_yVL1aaX4MnqA9q5zXt74SZzOTc3WuUl2b-B43gWKsyl__wt6KTd7sQjg9IkLcQgaLVU99X7dUQF0SfNk_HSI84DEhd06LH3kD4Huz8sgHBwkRcTQRnrSCeYKZ6hfM_ZSVJfEQGT_deh-GRAc2h3EOwJA4-SC4Rw5PvPvdGBt4kSh2Hx4mv43u4VQ9SQiore4fovRHkZxbh5CSOzNlir3CZBKhUIdKSms7UxfgSYSsiYeFYFxV0HVAjLD2zTUKbXTNIkhHrV06I26pTwGeLVXENLHWLNLRZYrLW5mfCdAB5IHXmJBHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHg0s6K5RNVaXy1dubBKUBWZ9ZAxPR1itUcDAiIDU-3ssCVsXz3OkFN_7WrpR-X0J-N4Fcp-hsnLbXmqKnPBYk9KBKLlO5uIuF8H2hem7RuttT-S4a9J59uEasvvLG1ZxUAdo1UYDXVjvxatEewOVLuQ5fCKuVzFLtiLZdBnbDm4_P_uemgNN1zi3p2ndqMmygVRk6X3TO0StiaVDAXiO4ntLB2VlviUr6nN3N_ThMlmorJ-2IIp_fXG7-NRPQic-pMpohX4wauN5i_qG99i-rnMeYL2ufzebXiuLNeLiIFa26V4qj4qeu9V_9fWGRx1hBKC5CbgiSbKQ_4pAKFRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOKXcMKfvwLwTBMUtBUeFDXeDE4mv2gpJdqxr8-LfjsHJyKez9Czexmjcz56kUrVj0h9eloQYIkwruMUFVqtKd7Yc54yKYK63JC6qax0H6xiZKolErnlK2kDWE5q5EIxzJ3LNEXD-RBPqQep_D35Rsow2YRQZOpV2xGITl7jNmtxAKSS9zH5S68LjBWyoipLryKqxW0vL0hW6p_wqmBXyyX5Dt9VnYWCRHXerZ27HSVV1Q0cI518fyMdFkv4bUO1vOfR-cVaTcIhAP2MpZ_9A2qnHj-iadLisp9CkiDhUTA8UOLhIMEX7EbPcUh3fOSnglMup97pqgPD6MTv2xsX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biZxtOpwShWOl0bjJESsqthGHCBBXp0FIYfX1wR7h-a4-rQo7_28eTTLKli0iovODyU0gSNlUCU7d5LCEN-PjyDfLkyUcLiHgEAH5KCI5Ekbnegq8Byfz8S5odYQOU_ZiX9gi7PJ6XJhHJcb6JynMtsuCTZNQ_Bm1IMjvNMHVqsh2Jwze8DmiLCA3tAGu-vlkSYIgq4sG27VhtQuhFj_n3GaZMjdb081SIqhhqrvjUYxhg934xm8xtrKNL07oJem2dsmp2tPseUbUXQRl8dAgC354QxV8IOb_T3jyU3LMrdY5P6EqczemUAPbGXIkruoaNj_6CmkisJ2UA290CYyqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3wd4s4nAsjhVFAS2JS3kQmHmFE_Rfgg-_egwbPKvr2Yvi1wPJTFdfAcVNanMGfPvDbcOUEd9Pv7yWW75cHuZ5-bu6qrvpnMbg7WUWbvv-v4caX8nJBTqiiGiAHEQV0rUk9awcjlSCMMaYPZVoTZ4xFTC6UtVoozOSGdnc9izFxlIEh91eG-mBuilCRTPHCNbj9qMnZKI4WJ8s1w7dKERX5X7FoNpQhxxgKHrEC52fg3h14nBZLwuiBhpJchzdAG8YBZl1a7ocCxno1g8VExFffLyfl4WIbB1a_mfln2A0Bc4EoYav-K6QaPXy-XGiCt0U9TfldhTY8z6NpzDrYB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ9-tqjLnzraQWX6OTQM5d4b6uF0QiUyS22OitZ9sxK9M-LspbgN7X-hL7RIucv4xVzCs0N9HnjbzacC-jCj31mUSGIQ3HBXGCEFVxkgtRPjegttoL0Te7o3n96lIWgF9XEGwh25cXhA1LM6r_rXcZdHv31uww9Lmq2EiBmQBmJdCF3YX-wm4SpZ9q3saMXnLIIpKvkH7LYg9gTiBvbZZcpkhvKqSBzfCOgmPwUCkv1Isji213P_2JNmgG3j4LNTZwP9no7VGdNUcPKgsvKTh-k3utDIVEbNsHow5yu6AuQHL88PHkh7h-F5mw9gQgo_QV6PQhRZzyzjbrgXGO1c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM1UU5RzVARCgNQZDDirfmvhh-_DDfDnVPw7jIxvV9xmckFZ4NuVCUac_gkJT1qmShlADm7lAy3QF5tGmub9Ouw2Dcf9UUA_LF8YjBMQTySzv-SR1-U6l3gMB1ppVAJXJbS5inewWpMQ65ZwHEoEzTHIYdTZutH4iwvxiBHFUl2Zc2Xg_nf032ZvO9BnAEES4Wc74gWWH4Dhnje8fFTeoyCyi2-uTNu0eVkW6pcU8dvByajP_AaMjWoL9Sc8_2whjqi1L2-o7cfVkgdjAAwgk8v6p8OtED_NUulrl4DLHu_i9KaAYf9MgWrSJAaBbYoa2GdfQrCQBI8FOCAXbZASUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=GhoGP0-Pz0VecKxZLQAWG8JZ9ynWtp0LOJamnOsHX1pgqfWLUlR0ZI-htl7t-DzusaU34bjSvdaPubKi4L3XF6BDQmAUnNRrPiBDpAPd3yS2ctueSZPYnIGV06lZElXdcDyw8SHWV8LOOeZmTxbHgKAP3A4EUKb0GxogT8XFA0ds9oUzpUqdEAbhHub6WsyzigJJXFjwhmNp7gfrOQJbk-__Fz8EIZ3PYoMDUQfynhVcTmJlKqthb6cRX4F7cyndXaYEEhvzyUmYfgv6iW0mEjy5N73vHwzUKX3as8JCikLgXP-PbHBnrZomVyx_zmln3wyzH7lNESrmMGFzdyGFGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2JS1pvlAfTi4FSYEZRcJhL6bkQyT_bt8cxBNXcMc7UU6D35jDRSjFVhr1yEK3oKNBnqBXgb0VC4cFTb3KqRD7LRloqKJYwNZVdsNZb5twcTRIO0rw3SAfb1W2Dq1h4-owQohs7JuLxcvBjp7ai5RfKsVzQ38DEHKSavgLgT52D04Ih16Irn9vGpxbNikKs_0KowWDgFiFL8OtZpTGA5eZfF_VGad4pbTUDNRjwwGArV8ZFZ5nMWKg6F40ECPqbCzZlnkwuPNQdWgzAjeDnejs3WwjL4nNk402CKpIokOO6a5mJFdi76epeBFhXBLH3Tv_lwGxvHtaW695LInJMQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8AZBzTilQ7Wdn0bDKRhw4DK-0324OqXQOTyco-ZHk8joypmaffrqEZQkGnzusgmYNVDFHW1NshyIbZcZyGZamhSNFGLSUW9XQd4xVrxepf2jgaRIS8FnCC6uIWmyHPhcHCgUb4p1z_GywDQdihoSSWkSdYRoXdGk0UVGt43b_QK2ayy9TJVhgmBIymdZzcLZNNpKABCw0nEEMOsw56kLee-5I22lNeeRbQCdgNV1Z9M1pXQ8GjedbeuI6exFPOgGL8yAp-2gKEo6d1aoQeV3lJwn62EsmdYe0UbbFprBcGY_jMaTDGwnw7a_Tjk-M2ORJ-Xz_m_tQGIgQm8-oep_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4rsWQMdTDPh2crJjgBkrvaUbM0jtmga0wWmXyFOrsVPaJikeEY9UJD6I4iUL0VRAC9gzQ7wXdCA5-EyDRCY9iSd-zbYOpG_UwZP1MNBOSBFPsFYx2hEIPXxbwoBdCsIFdeP57RNb__mCtCJ9keu4WpC99WG1WKyqUakHQnZj5wJKCd2qW-mrkcNiRL4iJFkcZ-cSNAFPyVPApXf7zrQHz4FmNgRb6vYCuZ__jXffR0h6Bmj48CTsW_WgEMFdGk8rv3Zxwbm88ha_SDKynXnlV820TT1keQoCtpwJacWRFrHt290r2WQxVWuSmhQgwrJtb-jeNpVsXx9DRCdEbjbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF2DKYPU7UOIVyKA9tmz801XxkXMG1NP1DXqOd3tr0JV5zFFdI56QCXb9z1Uys22lapQaCjHzXxRiUZ0KkNyGJgpowKc5J9aBg5vaxhZZ9I93s6t_k17vLfch2E2UuU9alGL0hobL1EK-GLcaMLJrOkbqjqQfqL6RGqZjz3Zjw0pBYtnnC_D1Ykiw39ajOa3XHnHcy79cr7GKSAGwqqRrA5Wcp5NsWEwJDpwMQoLxhqq6X26PeHLj5xhhFTG98CtV_V1WQpGA3hrAFizDugUI1Ww9UfwDVlYy8e-FbpahWO6x2ejvDb_pPkeAdNNCKBTXwy0Z8Oyz3NLNPtNJQDkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5zrh-93QaoOfsjoArYdy1uzzSEU1iftEtDLYl2Mvk3pNw26vpsRvjqfpU-EmIF9k3a2e_xnKd9zgZAhFvp5UWbFAI2DjxKbbnBoZ3X1EOYFuzbk6T8SsSQuEfCkz3r3KnOoCxkVIgF4muLZm9AnsMzIrOFqc9kle1SfhswRnV6asCzQDaA7cvptpDvKyM9DUoI23rAxzq1-YUwd66hDEn8jSYIbZbVAdAjHSigW9UBGO_zaHsfnNdMPHQj8hBFd3cR0KB_YWCO-8vWHz_pWqsP9cum4rdNMjvfHRCi2-ThyLKg-t3404y0pmV40NPeWm6Ej1oQ_FE8eWP1iGgKTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101687">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
فوووری و رسمی؛ تریلر FC 27 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101687" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101686">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEAmRjWaspdOmK7kunyDZ19wz5y_1jSgSZZo4u5w8cVZUgRGLAa4DBRCQYf-3OpaQ0fKTcC1RHvzj3aN2gBu5cxIhQxuIQ_HdQhLSjA7K4pIra1kbv3dvAjC2Bt2MlwC285YlA79uR-yt5tnvjd6B1T73c3bffRbEvAkTuhyJ741jP0XfRbPtxhPm9j7XhAmtIGkn46yn2ISwHO55BQQlcrKjLpJQbaGqPkvEEsV6zN0cuLRhRDwaUOkHam6Xi3cscU263RIWgtc2Rw9WOj4afVmAqmFUqhAyDEDPiJxoRboayDPMoRLSMZ-9gWzqRlW8gmsUi0bEx9wurqrKgWeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101686" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101685">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTeiqp4AmxG_xxm5rCx9tdmuk2D_Rep_1aMq9Jfz-SQ3yiPZo3DrFpLJdiHrVN3xtbXNugz9TRWdayejw_cHA6PxpXILwSKvCimmaAeF-IaRXKQw64CdCBcF9gvYz3TNYEZerSJKsWvt55oPen4hY-q3gRBih5kksUzXPD3CUKRVG-4m9doClApEeZGe41896A-kfVrk6eBO07XeiTiSpc-5SOJZuDzQ73X-fIs5-D8F5hxAgPU6ye1DbNewHT9LdInEVEek5viClDmhM4dqpHRqf6GLOkSkvHWO8Rxbe59hYjZQkVDXIeZ-d2u8UaOTn666QSzDIDyqeDa3RJJ0vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
: الیوت اندرسون ستاره تیم‌ملی انگلیس به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101685" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101684">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2wInQZlJWHqUZHm7eGYuz5JvSjeG01WSmapSUWOIMJWRg8QWq9f8jtkEmRena4uq6gpgae-wXguKTbXxxqoLwQMRrPrExjZgSMc9Kyd_NKrLdl5z-mSDt5ERcOsSJlJX_qVnBYD7ZXTXLU3Bgi-DJYOxHPJpFtcVq36NTpYXvqSjRq3f7IiLJipG-f5VvOlBXBpdKdCByVpW-hdl09--81cJYPMkklWVZdwA-JJ9t2YA5hQnvHyJo05SnHD_F_YU4NGwaJWfmvdZOqmILerSvg48rsWZ8lXiKEB1W02SNOGO8X0xlkp-xIGM3iIKtbuj4qFJ1kAeKms8odbpJl_tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسمیرو رویاهای همتونو داره زندگی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101684" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101683">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp8Q2WMOMg7kqEXm43zLLDtv0jSRuMf0CihpPuIOtuAaRaLvyRbitvUUUUFTCe6ZesUesItTBDDwNc48xwr7rIi0IXUy_d3PjW1HdAUgcOX1PV9SeMFYNmV8l7BzpWafG5yu3jpfEIIe_wbfKfDMrcWDmXi9nbBZ8kNH5OnbhfeAJL6KmXiUYUn2cPAARCOZxAZdBt0xaUS0_EFIMV4UxcKL0aF4YbwY8h3h6nFN2cjmHUEzrxk2p5pSH0PfHiLDfX-w3212B9noY6ZmI7y7Nnz5SSAoE3aa6LBf1FMQ5a9k4rvtWK4YbCgJomjE7pNtJBy-Eki-jVGa9kov1ADnpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمیییییی
: قرارداد لوکا مودریچ با میلان به مدت یک‌فصل دیگر تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101683" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVTOjhTjr3qKipc0YlSgDx2Fx0PhmT93e-LIxHMi8cCnetKaUur_fFa4wXV9RZX0BTQb0KjggRPE1rrltTlL2yRDpdlQGFX_p1Hytmf-dwl1_8WRoCVPMPbPOmuJjvHpz14PRVri2_zYWjepBAkeIqUIEkK5kcAIrlChz7BDzV5xjDu08hZu_XjwSg8255g9w-dLy3_m-5q3L7dKyJiwSH6BP_oQ3b4T2O5ZvSp7D1uDGxlc0JhHXhMny-OiDf1Ix3ercZFfbQCT05S2LChMWWYx4d7u1cuX_BgKAEUNqTDrlqC2ZE_HRp420rUMoB2-XW60IjxOtdXh5xT9ce77Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101682" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=jbf4slB-WE9YnFUtCKkUo5c8j8H-_M5iQly2h_kOrG2n3d2HwnQ2lF3nASGsS-ln96b2rD1SlCO37ElxSjH1zp0EANd4zkis52LTtxV6hrcNgghIf3Oj4mqLp1TmZg44fWneJ4mfoK5X9ow_Ou2QmL1VBcT2IH-rtklvyJhxKl0mjM_WnkqsJXXgkjb9e0U4CYAlD5RQF74X_GNVAbZKXVp4zQsPFaZJ8LK1ODsntf47-jQ9NEiSMJwlD774obevYRVa32thGTb8zuunrrAlus3xHN6ipANGhSLHfQ7kamcpM3HN5lrhOtUmW7MfwURkWZUcbHW_QHUSgemJLZlzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سوال: آیا مسی بهترین بازیکن تاریخ است؟
🇮🇱
نتانیاهو: باید بگویم، در کنار پله. اما در دوران ما و در دهه‌های اخیر قطعا مسی. او چند سال پیش به اسرائیل سفر کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101681" target="_blank">📅 19:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
فوووری ترامپ: من در حال بررسی یک حمله گسترده هستم؛ بزرگ‌تر از هر حمله‌ای که تاکنون انجام داده‌ایم. به تصمیم‌گیری نزدیک شده‌ام. ما برای انجام آن کاملاً آماده هستیم.
اگر از اسرائیل بخواهم، ظرف دو دقیقه به این عملیات ملحق خواهد شد. ایران به اندازه کافی احساس درد نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101680" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae47457bbd.mp4?token=h23o_Rb1wRdOIqY5LzJbYpiivR86hWGCT-xhQk9PPzdSvkkG5tJuV_sxV-J0LwCkqs1_ZJh8EMMi95CkZP1M7K-dqlNRgMndwIN7AWiOsSVYpGZ7It2tK6DB9NgP1T8GhVHlz_m0_YFBtlaZNnbB9zAlNwibEgLdtO7m19LIxWHRZiRZTbX4boGKBXLle1bZS1020AYJF3ap_UNhsD4LQPXK8iotzKRs9qepsRlpTLXHkWr_m7ZGhz_F7do-FWgLJSqzEas9UuvfAYcZofk_swLxYMJBOMpQGhMHmNBQuYK6Jw163zTWQyQ7Zp-blrbvHRC3ECMGetKtnxkLxYgoVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تنها جمله درست گفته شده از صداوسیما در سال جاری خطاب به امیرحسین ثابتی: ‏مگه تنگه هرمز مال ننت بوده که بدیم بره:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101679" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXPVK0t04VUwlQualOU7-F4PpUw02ZXPhFkY0byyg4Plk_QqvsT2iQZB6UPh8ZL3JKOM3axHARW9JxfpPOL5ei1Iy00HN4qRurWoYmWwrwehszVPapmLq9zJEunyG7N7L7WjR-213KhxXDNp15VncTsfghKc7yn40kkq0CJGAJc7TgugNvle35xB48MSQEccZng_qk3E2nJiBS8pN3aPq3qR7ug4lbQchxwfZHdhRVjIEilBHXUGkwhNWwEMqALtO3BwvBagNjA9Hp9os1WnVPZSPM2iYONHWx__HexmgrH3JYQOXww3TwhPBWwGyqtzfkJ5DK768i5zBdP8qE3vkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvt7e6_Sxf8Bwl-AJ0gjNttL-r1ik7h6tNEWzpyrAPBHHXdgq9zsnFMbRwqF5PiWVLGU0Efz5z5Iv7lbZaHU6PvvyJFPfk9A-4TNJNVtFlJ8oPyJJWbBYKkxle1btgfIGHN-vpnwKEb65hFw4c3qNwtECxICcFzzr0hy8nKI0_N67cuFo09HqQrkgYGHqJVPz48YDE2nt0yf0ihhIJefbVxaTtkbNOa5KE83hxtBc_GYSPRBv4shPCsyxup6EiTzEDJxQWStU_hnJWhyehCMIzAIvT0rXdcmAcIFW6DdIvNcuuXZTrhrOofQkssdC1d2m-JrM4TOo5AtwgPjt32CbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تبلیغات جورجینا واسه برند خودش Mimoa
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101677" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101676">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcribwRzK6BjmR2iRux8HmL5954jHAHXu4unEenI7lj6cZJ_A3ujo344GWd4_q2X5Z7k8Gj5KTdTfARvABqSdmhsE3GhG4QaP-8thoK8kcHlEvJsc7CJEHblsR3Ko4yklCMePVaVM234uMw1iQDjnQZIy5HygzBEa1kQTPgDX3C34I1d9fb2fywBQTYbHw63wWwl6hPt2PDnNHHDkFPqpvyJWa_nQSPMuTSPMylBtX-rDayak0BoTM6tdNOCl0gBLUBkfMFGWU5fssqjDZ6hpUBfRSneHmfOBelgsUNq_5xVdxtqASkngzvG5zR5TFcPyVOBV5xZ2txBPgyXx-HTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
منتخب بازیکنان آزاد فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101676" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101675">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Y03aeVYK8bisPTh4U6a3Qanc1YPje7TtbATmzzBljKpdkUF3JYAZoxLtuGRII4mZXBy08tDs_jTgVgLFQ--qZ55FVBvjFM0KVo8UGMr_qehNw0i9-Bm4BMeFsxKBG5psGqsWr96Hl_46Tp_H-NANMSCrY3kw-Uh5r_hN3Jdxzltr_OjkIs_FFU22Je0wlNAg_lisPODD1t05xUVycptks8MVUMU8NWm_ejM1C7pkLXb5NVMGx0UzORg5lWtl8oRz6aju8lFkxJfTNBg4uQk13EZ-uYSEf34XJWF3bj428dUw-gtwHM9U3VqH0zSWPtNiQNnDszyZnjnGKENNzcTr6gipvmBq7Ig4O3FJZiyxWg2qZ5N_3fLJXyRrGaKNk8ebif5wSoLzrfALpkLzAhQt_6uDV9HaFDSd2TkOHU_kZtO7VX_OiUTPhTj2W5NwobW4BswTTvNaA1cXH-3yKDoWbEBl6F1FKDpZyqUFP8dHocqfYXLwUCxBqpfUmFNBfnTRVmUuGt86SKhemwzhCHFZ-B1LKEI2irWIcGwnGQ79pSXbm_4_xOhiC70CnFo9tC-yv0HVAf2YxuVMIeVe2ctYbysWvw7WAe6lW6SP6ag2WP1W6maMQMyLLMGeu_9miaMq5qvJ8rq7JEm82nRTFd-MOAD2vxkQWMAliJCrZOiDz_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d6746099.mp4?token=Y03aeVYK8bisPTh4U6a3Qanc1YPje7TtbATmzzBljKpdkUF3JYAZoxLtuGRII4mZXBy08tDs_jTgVgLFQ--qZ55FVBvjFM0KVo8UGMr_qehNw0i9-Bm4BMeFsxKBG5psGqsWr96Hl_46Tp_H-NANMSCrY3kw-Uh5r_hN3Jdxzltr_OjkIs_FFU22Je0wlNAg_lisPODD1t05xUVycptks8MVUMU8NWm_ejM1C7pkLXb5NVMGx0UzORg5lWtl8oRz6aju8lFkxJfTNBg4uQk13EZ-uYSEf34XJWF3bj428dUw-gtwHM9U3VqH0zSWPtNiQNnDszyZnjnGKENNzcTr6gipvmBq7Ig4O3FJZiyxWg2qZ5N_3fLJXyRrGaKNk8ebif5wSoLzrfALpkLzAhQt_6uDV9HaFDSd2TkOHU_kZtO7VX_OiUTPhTj2W5NwobW4BswTTvNaA1cXH-3yKDoWbEBl6F1FKDpZyqUFP8dHocqfYXLwUCxBqpfUmFNBfnTRVmUuGt86SKhemwzhCHFZ-B1LKEI2irWIcGwnGQ79pSXbm_4_xOhiC70CnFo9tC-yv0HVAf2YxuVMIeVe2ctYbysWvw7WAe6lW6SP6ag2WP1W6maMQMyLLMGeu_9miaMq5qvJ8rq7JEm82nRTFd-MOAD2vxkQWMAliJCrZOiDz_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ویرجیل فن‌دایک مقابل بازیکنان بزرگ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101675" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101674">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e54bda82.mp4?token=YptV7Dgyroy-H10CPSvn7XwKjcQZWJLaiKoQoTBa5VyF-7mH50evgqBumFqZPtCAc1q4YKCeFLqNOZ8-s39TjULjrnaioQ9cB4pXVb9ilyhNDK-pHIcqkl-0uNd3PmiU3aztxVJ983P4Mv0v6PfkQeA4iXPYDm2n31lqiI-i8iFb_zj42dhhN78WP5JZ80TQNv_CQ4k-GvpgCfqD_E9hpHcADgI3yoIJ7NdcvvBlZj_F0GIKYOGG5mfMRVh3nnanaXIKmIwxhc6U3fmElhAU2VdtBS_Y1lwqAK9Grhc0KgHLmLZ02IfgnEzdOF9Hdosio5judoLk69gYJfvRuDFP7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
داستان دختربازی افشین قطبی
😂
😐
محمدرضا مامانی، بازیکن پرسپولیس در دهه ۸۰ با یه دختره دوست بوده، افشین قطبی خبر نداشته از رابطه‌شون، قطبی به دختره شماره میده، دختره به مامانی میگه، بعد نیکبخت کثافت‌کاری میکرده و چاق شده بوده میخواستن بهش گیر بدن، این با آتویی که از قطبی گرفته بوده گروکشی میکنه
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101674" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601e0d1ecd.mp4?token=RKhy0f0ISd0OtKy0awvUedsoAniV-Pt9RbwQq8hgLiT5NIgley7Z9r2hIKpb5-qD0aNmpXCP3oevAK67XnIGs3457jPQYRbo24qc279JPu-_1hSOq0pLsO1MndqYmw1gGdEwDFHwAtHvUcOpSsDB1JqkLVofpoDFo9GyORKHYOYAhj4MZ1yCSTfdnFkhLF81-_YWy2qs_QpGNUFxeGfTjMcY8pkiivOrJ9XAlaj9LxVJN_jJrhU8v7Wb4hlN5TkRK6jPJrqRTxN8qybt1cfuFuojPdpuB3RLyxur_MIQ8NGHAc_JwXcoo1YKKTlypgrcaIB02j92p_HxipGzk3hQ6QPgO2GWp08Nyus1lZHANOUe5vgvF_Fv-dT5kpNe3UtfZSpd1l4dAuZISQOfs5RZcrWvn8i8jW16cbDF8ZwiMLJy3Xz9dkO3fgUZqwv7ylxBUS0LNiRPFYr_F-W8udw8gWQzb-CC7KshCS5E2LujQOKq8XjoBz2QZxgbavSKJuKJvl-2CDXdFmLckwfmIrEElRBrJOziOVyhqm9uEIBYmbZBprnA9u7qBvzLDXh4duk_PqBFHkwpC-_5PXF3p507Mmceqf4mINGPmRlMEVrkYxU6YrH42R3nblyTl_Jl28OIE02iykbAB9GYykG4108qhqjw7cfFWSMIaAjDTzbqA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایت عادل فردوسی پور از الکس فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101673" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101672">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jja-7LlEYvakZDvxjVX5_SRUblqttQI7zuZFqAGE5VL2HKFlEkM8g8WMBjeXp5vvOo5BofTKcGPzhWp6jmo6cMabPMOdskfFCJFwIVtIzK-6o5vjd0EzMxNzDDyFYdroFwH4QwxHIcyrfKkGv9C4aT2fEFumLNh0GC_NS6sP01VkFWFdfpvtWewBXUNujVpBV6gODxrctZxOMcIqlPmwhpkq_N2UVjAGyzMpXRhoIsPv4CCLmoJ4WZmirnJ9ThNwaCCYVqsKAH3Xn1gOjTfGoCGMDLQaEdclQdZ0Xy4aTBmcI2RqAUVr3vA4Qt-Ioa6FIfjrY4OSe6zvnI0AySnztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_فوتبال‌180
؛ باشگاه نساجی مازندران با ارائه پیشنهادی خواستار جذب محمد خلیفه به صورت قرضی به مدت نیم فصل از استقلال شد. این درخواست از سوی مجتبی‌حسینی به شهاب‌زندی مدیرعامل این تیم منتقل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101672" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101671">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815514f088.mp4?token=JUKpCy1f1-OXJyzdAKRNPoI-rLaNDVQa41Pw_f6eVKAW0ohf2p5z4ug3528w_XZIb4ExKT9H10tdpmsc2585_u49L-Cyr0AdUQyBFdzfUQOanhDKmuX7rITD0KkopLbSHolTUJPJnBFs96LKB6uXHTc0gNjgLr-Gu8kN9TeN7_peHf2phAVJYUNr_sa2ymtsouCUd9b8Hk2Y3tbfIO0mz-4mqy-3BEaTEXbVEb43R73CLIbWfDBSHOzfpNg7LKXpJEdKJtpm0PfIo6Ulolj6NadjuinHkd8cdfjd16ZDIAJ486IY0vTk1zsGbjUIQiZYpYxRzhHZl00atYYK8ZvN9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815514f088.mp4?token=JUKpCy1f1-OXJyzdAKRNPoI-rLaNDVQa41Pw_f6eVKAW0ohf2p5z4ug3528w_XZIb4ExKT9H10tdpmsc2585_u49L-Cyr0AdUQyBFdzfUQOanhDKmuX7rITD0KkopLbSHolTUJPJnBFs96LKB6uXHTc0gNjgLr-Gu8kN9TeN7_peHf2phAVJYUNr_sa2ymtsouCUd9b8Hk2Y3tbfIO0mz-4mqy-3BEaTEXbVEb43R73CLIbWfDBSHOzfpNg7LKXpJEdKJtpm0PfIo6Ulolj6NadjuinHkd8cdfjd16ZDIAJ486IY0vTk1zsGbjUIQiZYpYxRzhHZl00atYYK8ZvN9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مارک کوکوریا موهای بلندش را فقط به خاطر استایلش نگه نداشته است. پسر بزرگ او، «ماتئو»، مبتلا به اوتیسم است و در تشخیص چهره‌ها مشکل دارد. کوکوریا می‌گوید موهای بلندش کمک میکند پسرش هنگام تماشای مسابقه بتواند او را راحت‌تر بین ۲۲ بازیکن پیدا کند. به همین دلیل هم قصد ندارد موهایش را کوتاه کند؛ چون برای پسرش فقط یک مدل مو نیست، بلکه نشانه‌ای است که باعث می‌شود پدرش را گم نکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101671" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101668">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljidDuwj-iA2r--kqy-IiERKt9QVCGZhWsu5jSv8izZnxsU3X4m3iWJFcNdlfYTkV0OtPIArv1e0llopXbDymqsl_eDqMK5VWsHpp_37duhKBjVkAr79J84vYiy_HlWDXQfDY5lbbt62D_H0xKup4eoYhmwCnUMo_SnrqlV8IM3c3iqglC9ptSMNBuo6L-mOeksquhKNw-vxaBeSqWuA4iCxxUy8AWF9IZ3Q3aKwD-CwlvV03unP89Y4t9NqiTW3NzvnNvxkfWkA5hzc3z08cIdtY6S9lh8ghRhxx-lxDNzpwQ3ZUsAZ5No0QArJGJr0S5uoklQEDFZjyZsZv8CcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GF4z8iFFczzFUtmM6X7cRKflJDw-nhyyC2H9NNypS4d_mDNXlz3zORMyg9tS987F3CmO6kC4xv7xEU_tD-xi2jK2TW75fviG38w2xO3GCJc5HiGlKYKWZA9Ui-ON_3y3SgvjpX1whMmDMFzl1K70TTcjo3IbnB7iZLoHYgaqJjNFp8GUU_wAAy2st4PzU11lsh6whZPI7KHOdV1WlgN6l-jpuOX4DDfhcOA8I34ZTNawBYKia8_3dymehBViiN8uYvkWDf2x94xgcVOhzMkAHxqPWaNn4ww4mZSGrfedYlnd0Ruk3rAdAUxQNLDgH2DIpfcRQUYEmf_6zewxkrHo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAEHWZCyGGZKKf-JPassc0l9oNVB_yx19z6dlNMm7NZNG6S8uTVBgKJPps1uHljwU1o-PS_4B8SZJWNffFG304ild2t0W1c2YmW2ZD2tx9Vkd3AjRiVifi9BHeLIJ-JZmtm_6BctQW3EUcdYR8uc0OkIQJMICBqGGF-8lBVRYASA7zrzJce2D0vjPoc4R-Ok-eXnMBDWeq0gr7RulNvcwfearD1VV6BFRu09Qohuck3Y9llRJugZwGoxz4-rzZj_wy-Izckph-QsAt8VbXW692on4X40OABreCtm_Y5vCLDtmKO-k1y0aGQGYLd8KgwkavohozeiYPMuM9-y7D2sFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
رونمایی الهلال عربستان از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101668" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101667">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLBlIUd3Rm4LvpSqt9lWTU7l6Y1xG9RLA67zNlV7F0aob-DiU5euKuhKdjYvbq1YdQm1_4_AOucoJMstRs0rf70FAvluwWi5pn4ExKzbrJ_Xz97qy1WA1rpDC8PPtgdCzT0ROm2E4V44mWJgIaGxxGZciA7F2udAYnfaewOTohCoXn4m3nWJxSw9nJKTA-DGOSPD5w3TAu90B93ilJuh5o67EFEdMwT1KA1u2egYfUQ1YIJLoU2W2X1ix2zr7M6Q1TqN0ftMsRSPZ-yvF-CCOMKbqrshT5WCTFgoVS7pwsU-T_-uSKs_OI6gd9sEvZ1SIaDtop0tG4w6-W9YUNQmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
جلد نهایی بازی FC27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101667" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101666">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=FGNg1mfY261YxVqaIIucqnn2NY0LEG9yg9RNSt0y3o1FAEDffPlc1hKy72rDjkzsZNsV113uDbc_05oQfdjCufhzED2y0UsyEQ8cNnBvQHLRcj-QZKKKnHuApRSWFqXekUyNzIJQsjSVOLGD_pNBsv51WCaoebaGgkaINBiqIoGVsoU2kbmsIIH9stVsDLPePC3dYWD7finnQDAuU0qpcuR6GongYw0Bzto27fO9VbP2SNoMubySK4sDIzzuMta4yrLnZBtoRkdvuG7OHkiWpb8JAeKemOGz_ULGi9c7bDlc5JFbgesWS2UiFXcKKOHCk4J9W6rU9UWl4dqQIDdRZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7937bcbd97.mp4?token=FGNg1mfY261YxVqaIIucqnn2NY0LEG9yg9RNSt0y3o1FAEDffPlc1hKy72rDjkzsZNsV113uDbc_05oQfdjCufhzED2y0UsyEQ8cNnBvQHLRcj-QZKKKnHuApRSWFqXekUyNzIJQsjSVOLGD_pNBsv51WCaoebaGgkaINBiqIoGVsoU2kbmsIIH9stVsDLPePC3dYWD7finnQDAuU0qpcuR6GongYw0Bzto27fO9VbP2SNoMubySK4sDIzzuMta4yrLnZBtoRkdvuG7OHkiWpb8JAeKemOGz_ULGi9c7bDlc5JFbgesWS2UiFXcKKOHCk4J9W6rU9UWl4dqQIDdRZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔵
خاطره قایدی از اولین بازی در استقلال: جمله‌ای که بعد چند سال هنوز از ذهن قایدی پاک نشده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101666" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101665">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=B8kdvz4DqjiJNPuAJMJEki9w088HV2Ke0IvapNbJuZLLRoWYbgJDND9oS09LC0PC0a0LMJCbYnSHlrZ_mhJkVx1dAhVqslvigwcnynjrMPTLet9GUVEmQp9ynLFpHaDYVp2wawSHlqKMOCm1SVma7EXmLBubpv_W_fuNgcn13MMWAFJjKW3LNBiRdDPiU5jVGxbeDi1Gd3PAV5cu1e6n34XntH6h07QwZ-_3jQZutrb_dnoeZ0GVDBPh83n7o5P-v15TedUkO3fFoQI7bcgeHT66GHTecAr68_0kTwX3hm60xn0AWT-oGnHsr48p0zdT2SLuBd_zHJhD6WyOYmwa6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f40a1d01f.mp4?token=B8kdvz4DqjiJNPuAJMJEki9w088HV2Ke0IvapNbJuZLLRoWYbgJDND9oS09LC0PC0a0LMJCbYnSHlrZ_mhJkVx1dAhVqslvigwcnynjrMPTLet9GUVEmQp9ynLFpHaDYVp2wawSHlqKMOCm1SVma7EXmLBubpv_W_fuNgcn13MMWAFJjKW3LNBiRdDPiU5jVGxbeDi1Gd3PAV5cu1e6n34XntH6h07QwZ-_3jQZutrb_dnoeZ0GVDBPh83n7o5P-v15TedUkO3fFoQI7bcgeHT66GHTecAr68_0kTwX3hm60xn0AWT-oGnHsr48p0zdT2SLuBd_zHJhD6WyOYmwa6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های چندی‌پیش مهدی‌مهدوی‌کیا اسطوره فوتبال ایران درباره تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101665" target="_blank">📅 17:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101664">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FigJ00Xyagl7CjiMJeAQXV5fKB758ueMYTj_uPwjozefkmMwiwqZ0M9YjdFIuGrL2pFBGoSdcc9pqqIJvGTFAyHYF7j96VMN6lvCb_k6BTFpZnfaA8YDpIli6ms8vA3Xur7V34CdCclidLkxGi3UM8N0pyMvjKnYkqwoSB7-qJNmnpW17m5m750AyOghqvd0KSCMBIMjRH6jUPK3CpSlYoELl2jFtFCxV5uElvPbUtpgRxSbK8_PDFuYI12hy-aoHaFI9vL50cCIGToZEkb4w0rcPWpCAoNTRwdCD2ygk5o8mIS26KmPKRLwdIhfyUTrOlTFeJ0RKBgvxLvvtuh6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گارناچو رسماً به صورت قرضی با بند خرید اجباری به استون ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101664" target="_blank">📅 17:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101663">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv9F23AJObkn1QhP5XtgY3m5znDYJUU-dbkuLmI0l1J1UyuBegTmoeV_OjlEHWvw4g_8L1ez-746JzAG0q05NhtB22fkLi-ADbBJ--6-8OJqy8Nv8ZCaoCdYmcjT-WmGR5n56CRGzU7JN8ldvos5GuSzpQyvRjZZuvJYkTzcfysLEO2aX9UROGeDDvYIrZDNo4xb0lxt4eemzPDxDw3Zt-eWXFKpmWNotativg6Tf6zmLaKBqQfz65Cq0UpSfi6A8O6o9mkCBwMM_-PUN3O9vN1LGSs9PYanx_D1urvJTap3MvHbfaNRe7ybOrJGMuzOGkvhbf8oLT24-C-sXq5a8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
آمار ۶ مهاجم برتر این‌فصل اروپا:
🇫🇷
دمبله ۲۶ گل‌ و ۱۴ پاس‌گل
🇩🇪
هری‌کین ۷۳ گل و ۸ پاس‌گل
🇪🇸
یامال ۲۵ گل‌ و ۲۰ پاس‌گل
🇩🇪
اولیسه ۲۷ گل‌ و ۳۴ پاس‌گل
🇪🇸
امباپه ۵۶ گل‌ و ۱۳ پاس‌گل ‌
🇫🇷
کوارتسخلیا ۲۳ گل‌و ۱۰پاس‌گل‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101663" target="_blank">📅 17:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101662">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=eXo0d5pwIJuKLXoj4af0JRLg9Idq5NJhHTvOxaolXlLqauCrvevGJyPa8cZ4efeKlGV7E5m2f2MLVH2lg9N03GVwKcxbVtLzqlTvbQw6BDOPFuQP3vzcBqmi-ok5yPHfyvNNJ8vxXfcUDFlCJslQeSG1dvj0MlO8vFaFLPlwrD28A_-J0kbFDbykstU-pBBPej3O2eRC0a94UlRi3nEFqQ8RI2C1xDGlQ12pWksxQilLr4ck4KdlAsyeLdodpHWtt0aZbaxquQ7WI5bdcV7FGKCzlFm2zLEEBVcrb-735CZtnz69XZB14VxL2J89RLLI_4afpIPaef795ExX1WLV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb77439ac7.mp4?token=eXo0d5pwIJuKLXoj4af0JRLg9Idq5NJhHTvOxaolXlLqauCrvevGJyPa8cZ4efeKlGV7E5m2f2MLVH2lg9N03GVwKcxbVtLzqlTvbQw6BDOPFuQP3vzcBqmi-ok5yPHfyvNNJ8vxXfcUDFlCJslQeSG1dvj0MlO8vFaFLPlwrD28A_-J0kbFDbykstU-pBBPej3O2eRC0a94UlRi3nEFqQ8RI2C1xDGlQ12pWksxQilLr4ck4KdlAsyeLdodpHWtt0aZbaxquQ7WI5bdcV7FGKCzlFm2zLEEBVcrb-735CZtnz69XZB14VxL2J89RLLI_4afpIPaef795ExX1WLV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمایت سید جلال و قیاسی از علی دایی و کنایه‌شان به بیرانوند: بعضی‌ها اصلا نمیدونن احترام چیه، هیچی دیگه سَر جاش نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101662" target="_blank">📅 16:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101661">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=WD4TTIx2W8x7C1oeG5JfIkhWyJkUflk_XWAztWatVcHMkCaFmUTLBnMJsEQM3HqoTNKcma_ZZBKudByyWAJ1s-4Eg5FCIFcChjIn2Sq_3cGqTvWRVtbsx2omBCEigVhV6j01B10la-MSQ3A0CW-pq9CJsPSp3DzCDWmq_4BqhFLFnI0hs6cdOTl9fGW7opAg9K9tBSixmXg9oRSgmouGzJpK0kkJH_66h0pKr2qJw6nr9wiaxj-zJ6l6A0XAC2dzvFq1cy4iiJHj0XU2nsc_PIt9wcMgD1Vx3S8Uw3LTg7vZXehXXaVdTjit1vWhO5lgZ4AfFYYOxJXUZifbT1L0hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098313b0c4.mp4?token=WD4TTIx2W8x7C1oeG5JfIkhWyJkUflk_XWAztWatVcHMkCaFmUTLBnMJsEQM3HqoTNKcma_ZZBKudByyWAJ1s-4Eg5FCIFcChjIn2Sq_3cGqTvWRVtbsx2omBCEigVhV6j01B10la-MSQ3A0CW-pq9CJsPSp3DzCDWmq_4BqhFLFnI0hs6cdOTl9fGW7opAg9K9tBSixmXg9oRSgmouGzJpK0kkJH_66h0pKr2qJw6nr9wiaxj-zJ6l6A0XAC2dzvFq1cy4iiJHj0XU2nsc_PIt9wcMgD1Vx3S8Uw3LTg7vZXehXXaVdTjit1vWhO5lgZ4AfFYYOxJXUZifbT1L0hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⛔️
نگرش متفاوت دو سرمربی؛ یکی شکست را پذیرفته و با قبول واقعیت به فکر آینده‌ست؛ دیگری زمین و زمان را بابت عدم صعود از گروه در جام‌جهانی ۴٨ تیمی مقصر می‌داند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101661" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101660">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=W9erLtwjhseSj9Se734grFs62Neox63qUK1g5ap2AI8ynVGTWme5ARAJ7QLzTB5VcVe7q3ypxgKgFFATHhAJfAJTAyY5clL_lpWWbd26RANz-mLyld_yzQgzXts4CmrbhFBCPnhvLM1eUTJvD9s6EkqMmltRe9tM_HNnWrVHsxRWNylegIQux5b7_le8e8SKnvrlJtpag8O9unTOXODlQhBF4iHEYOEgyegyWCBHfFluLmppvkk2YxgSFtfgd3Rb83AZf_IM-CjT0MIW1LpyRi7syQgI8P4_kTsxAMCZl-8q1qA1UQ4gLsAyRUqoihxdDHtES-SLJi-Fl_klBWz3pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2eee7743d.mp4?token=W9erLtwjhseSj9Se734grFs62Neox63qUK1g5ap2AI8ynVGTWme5ARAJ7QLzTB5VcVe7q3ypxgKgFFATHhAJfAJTAyY5clL_lpWWbd26RANz-mLyld_yzQgzXts4CmrbhFBCPnhvLM1eUTJvD9s6EkqMmltRe9tM_HNnWrVHsxRWNylegIQux5b7_le8e8SKnvrlJtpag8O9unTOXODlQhBF4iHEYOEgyegyWCBHfFluLmppvkk2YxgSFtfgd3Rb83AZf_IM-CjT0MIW1LpyRi7syQgI8P4_kTsxAMCZl-8q1qA1UQ4gLsAyRUqoihxdDHtES-SLJi-Fl_klBWz3pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
مهدی‌قایدی: حسرت خیلی زیادی دارم که چرا بهم در جام‌جهانی بازی نرسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101660" target="_blank">📅 16:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101659">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101659" target="_blank">📅 15:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101658">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=by-OQ02lpXkMMx0MkbaT21vJd2xaa7oy9N1jIP2g4r2imOXHeR9qOfxq_ab-dQugJiJcf0TCBPAYwDvsh-GYT4lJKaAHDOABjtRat31Z3F8UcCzAqJcHkeckMzaXza0NE7KxQfURrNxK9HJTFzXxwUHc05CitnffM7HfvVwOVBLEeTU_CFfMIVxt-KTZXl4ydW2-PKSlPOnc-TpEZ5JIAvAjVTTIE0O61_xidFEizxDeRGUGBZbHN3IB6WPvbCMey-s30muizBfPE9evZrN-CSGsoVWy_9QJ1nik0b1rHcweTHHHmtfbTGuvUI-_XpoVJLsKeUalL7Pye5JEvRjEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca9e664c4.mp4?token=by-OQ02lpXkMMx0MkbaT21vJd2xaa7oy9N1jIP2g4r2imOXHeR9qOfxq_ab-dQugJiJcf0TCBPAYwDvsh-GYT4lJKaAHDOABjtRat31Z3F8UcCzAqJcHkeckMzaXza0NE7KxQfURrNxK9HJTFzXxwUHc05CitnffM7HfvVwOVBLEeTU_CFfMIVxt-KTZXl4ydW2-PKSlPOnc-TpEZ5JIAvAjVTTIE0O61_xidFEizxDeRGUGBZbHN3IB6WPvbCMey-s30muizBfPE9evZrN-CSGsoVWy_9QJ1nik0b1rHcweTHHHmtfbTGuvUI-_XpoVJLsKeUalL7Pye5JEvRjEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجراى مريم اميرجلالى و حميد لولايى در بين ٢ نيمه جام جهانی‌سمه خالص
🤣
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101658" target="_blank">📅 15:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101657">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
▶️
چند سوپرسیو دروازه‌بان در فصول‌گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101657" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101656">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=dhMdpQE0Q-XzCoiDjbYt7B4E4BcXWI3BTH-qYmgVTgDujeYQAdRF6N47NwaI5SsdERWyyIt648xncD5uLljcAMmZab5mB_31ZdZuGTD_rL5FLk_t8x7P4L7uOC5BXV8G572zlrIwExKOR7dJ6M41jW5t0PLxtOJvO4gseikOM5ad-0CodXANh2E2UQwoZ9LeJOfzbhGiChB3M-EkX0DJtwtRY0c4UmvJEo_E8b_cTziVSL0_x9ftuswH8rUcjz5Jh1yqUn0j4gkMfK3jdAZcoOrK1H0xZ3LzM5b5BbalutLXQyBQd1043ypvwyBX85B2PeVNT6XClF9yI-kkdXi_rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89e53e52e.mp4?token=dhMdpQE0Q-XzCoiDjbYt7B4E4BcXWI3BTH-qYmgVTgDujeYQAdRF6N47NwaI5SsdERWyyIt648xncD5uLljcAMmZab5mB_31ZdZuGTD_rL5FLk_t8x7P4L7uOC5BXV8G572zlrIwExKOR7dJ6M41jW5t0PLxtOJvO4gseikOM5ad-0CodXANh2E2UQwoZ9LeJOfzbhGiChB3M-EkX0DJtwtRY0c4UmvJEo_E8b_cTziVSL0_x9ftuswH8rUcjz5Jh1yqUn0j4gkMfK3jdAZcoOrK1H0xZ3LzM5b5BbalutLXQyBQd1043ypvwyBX85B2PeVNT6XClF9yI-kkdXi_rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❗️
علی‌قلی‌زاده: امیر‌ عابدزاده استعداد بی‌نظیری در نوشتن و رپ داره؛ از او خیلی چیزها یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101656" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101655">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGhVwmc8GgOHgUK-hmzvxcnJYE1yXMmFr3L3fBiKbpTEEbQLHQ4U2Q_C3qqTUUudsCGPI9BV7Yzt9pwTAEEYTgOpHB2_Ys-Ot0E6w7AhCxPub_SFNAk5cCsYJAViMbIEAju9V6FGwDX8ajJH-pzGWKpBz8RwhJRR-1QaRN8KYR_bi2ftkNBudYqWzvg3SGeBdoWIdF0pJ61i-FhPUJhJXIUUcVc9pgVaVp1fV1OwSUW3oSs13GiI0KL3PbFCega78j7NLocy-vUGw1GXzqE8MLGfRWSKE_Jxz-DGlPlnIO52RXGk_mIy-e98USXv-ihMCfyHost6iyXLhbVx3TSJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت گاوی زیر پست یامال
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101655" target="_blank">📅 15:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101654">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=Ey8q4LCU32-YSCf1bki2Ijs7T-JX7oD5QvwCkHts0INZ9pdlUlydffZ3TMbHxZv4uKqXF9NKDQanSNvoBwuaZ0vqwcgIqNld6iAgtsaRrCN7svrgiKP6pPbXSkTuv3P7hFkoLNRNNjX-UJPVQeduDJ8V_2-7yQse-sUgONjmSvkAEKA9VXbwvOu8lt_0lcfibVTCkckpRZSQHzl5HhOxzWGIozdtLiPPHXFC7gxzkDPYgccgmmHJWkSRSLKN8smXjF7n5VUhfHIRlBtxjtAkUYujClX08ievGR3JRTB4hu8iC5HkuveSQSCgygROWXs7w4IJsi191n-Q46KCXw1vNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c5973b07.mp4?token=Ey8q4LCU32-YSCf1bki2Ijs7T-JX7oD5QvwCkHts0INZ9pdlUlydffZ3TMbHxZv4uKqXF9NKDQanSNvoBwuaZ0vqwcgIqNld6iAgtsaRrCN7svrgiKP6pPbXSkTuv3P7hFkoLNRNNjX-UJPVQeduDJ8V_2-7yQse-sUgONjmSvkAEKA9VXbwvOu8lt_0lcfibVTCkckpRZSQHzl5HhOxzWGIozdtLiPPHXFC7gxzkDPYgccgmmHJWkSRSLKN8smXjF7n5VUhfHIRlBtxjtAkUYujClX08ievGR3JRTB4hu8iC5HkuveSQSCgygROWXs7w4IJsi191n-Q46KCXw1vNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ینی چه بلایی سر اون تیم پرانگیزه اومده بود؟! ببینید قبل از بازی با فرانسه همگی بمب انرژی و انگیزه بودن ولی تو فینال امسال انگار همگی از مراسم ختم اومده بودن.
بازیکنان تیم آرژانتین تو بازی انگلیس داشتن به معنای واقعی کلمه میجنگیدن و بعد از بازی مثل دیوونه ها جشن گرفتن اما یهو نمیدونم چی شده بود که اونا از لحظه شروع فینال هیچ تلاشی برای بردن نکردن!
بحث تئوری توطئه نیست و هیچ خدشه ای به قهرمانی شایسته اسپانیا وارد نمیکنم اما مطمئنم تو رختکن یه خبر بد یا یه اتفاق ناگوار برای آرژانتین افتاده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101654" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101653">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=ohqyFge1aYoK60THfIOWTDzIzQViX-SV0nzv576W1JxZ-1cebJ8nAU8ord6IMkmT3aK7T28iIcOegfGB-8rdI2Uvnvakaj0g6LLBoLkvPkSTnoPXSOJ2cohkb4u8T2n8rSQnHQdU85UFiUY305NIssWr4LmalePL8cx39dL5SCEYtdBnYNkmHi8-TH5SZN3ZdLoUVxIDGPvQgkx1vEOZqsBExX0Kqtxryq8M7IcJ5V4OO0defx-nRiwERXqZQw4xtwwUCtCkpHvk95UfpcQ8Uyq8Z31LFCd5c64ytdXKbcrp_1Wu3CeLxYlyEjZ8GPxUSXcJwJ4qg-bUbqU6qCl2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d995b135a.mp4?token=ohqyFge1aYoK60THfIOWTDzIzQViX-SV0nzv576W1JxZ-1cebJ8nAU8ord6IMkmT3aK7T28iIcOegfGB-8rdI2Uvnvakaj0g6LLBoLkvPkSTnoPXSOJ2cohkb4u8T2n8rSQnHQdU85UFiUY305NIssWr4LmalePL8cx39dL5SCEYtdBnYNkmHi8-TH5SZN3ZdLoUVxIDGPvQgkx1vEOZqsBExX0Kqtxryq8M7IcJ5V4OO0defx-nRiwERXqZQw4xtwwUCtCkpHvk95UfpcQ8Uyq8Z31LFCd5c64ytdXKbcrp_1Wu3CeLxYlyEjZ8GPxUSXcJwJ4qg-bUbqU6qCl2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رضا جاودانی در جواب نگرانی عادل فردوسی‌پور، به جای فکر کردن به خودش، با آرامش گفت: «بذار بیکار بشم... مهم نیست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101653" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101652">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=LlqMzGs7gYDn5jQ7eJs-ElUqBdGv9xvFkfK5U3K21qddp8uz1zBSQdilljse36sPfeIz7Y3c-bFxr4jil5G-WTjafsC42E__ysmWibdFNIQ3_Sdo7A2q5hQc7M8aKnb5Spu-FWZ4n3nfDgqqCQu3izI_gBgdBWEy_u2NiKvnbPTF7pno3x21_ODJH8eG-rt2COzkITlP5HIDxWrVOUmBGiIxicNFWtVvDjobocnTC4UXN9Yf68o9mqkrWXNiTILpjR8dsdVVHSuMHeOcqZ0fLNUQQE6ijMTbPVyuVJDi0kFq01bvM87yEoMqvp3MDUjrYjEVDp4BNxFxGAPJOJ3VMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7be59d405.mp4?token=LlqMzGs7gYDn5jQ7eJs-ElUqBdGv9xvFkfK5U3K21qddp8uz1zBSQdilljse36sPfeIz7Y3c-bFxr4jil5G-WTjafsC42E__ysmWibdFNIQ3_Sdo7A2q5hQc7M8aKnb5Spu-FWZ4n3nfDgqqCQu3izI_gBgdBWEy_u2NiKvnbPTF7pno3x21_ODJH8eG-rt2COzkITlP5HIDxWrVOUmBGiIxicNFWtVvDjobocnTC4UXN9Yf68o9mqkrWXNiTILpjR8dsdVVHSuMHeOcqZ0fLNUQQE6ijMTbPVyuVJDi0kFq01bvM87yEoMqvp3MDUjrYjEVDp4BNxFxGAPJOJ3VMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
شیروانی، مافیا ایرانی فوتبال ایتالیا: به اینزاگی گفتم طارمی را جذب کن، اما طارمی در اینتر جواب نداد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101652" target="_blank">📅 14:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101651">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkKbmkdAAjwnhBCi_Jduy-a-HM4x5H5pnW-bJ2YeUohIEC_iNfgiKOYqmxlUp-1SLQ9SljVJ7mfypP7ckbOKdAwMxTXng_6_ntZDg6k4h_tvWCVhSiQaU93FFjDp23X-ozDwEHBdUwL_skv0rm-JlO3u8yi66LZQnf4j1sp3swgIseFEVs6R5HLmq8ev8i31EOXGHzlVtp_GSiK6Rx45EwSDZLJ779t1QrQcOsTBc9dH03kuwH16x02MJ-2oyba52CcvUDCt_dbVCJi4dnyg7E1mVkgB6jJYwjXJ8vFiijtq_DA0ihtj_p6X_4cQvlitzlCTpl4YfBWUd_jiT4rVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101651" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101650">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=eUb2WCsHPlOk-jJHuBnhfOQH0bIUMlIAjan_UjRLRE8lhWi-YTxJiFO5UiIBb6HaCcBvK4uu3jmrPjuL7BIoxkP1Fh8YIQEiigqiQWisTz6FwlCyQiEzVRzeOtcEXp7fxBpkTDxx__4IAiR9NIpI2a0sKFfCLTuOE3lVZqLy0Cn4FufHNeRqF2Ws-2_543QX2-QdgpHqGT-2-wdJLg9kCKM8TTh-FmhaAZdeW26P9su_gG3GSZjvT52dQ_kOumTgBxjDTizw8FeMdKul9HGlrOHCvB63v7g7-A9YBFaqUPosEKyiZmnw5iHZwt113iBTta2trjBZaTxVT0EwHyRNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d13a0e1e37.mp4?token=eUb2WCsHPlOk-jJHuBnhfOQH0bIUMlIAjan_UjRLRE8lhWi-YTxJiFO5UiIBb6HaCcBvK4uu3jmrPjuL7BIoxkP1Fh8YIQEiigqiQWisTz6FwlCyQiEzVRzeOtcEXp7fxBpkTDxx__4IAiR9NIpI2a0sKFfCLTuOE3lVZqLy0Cn4FufHNeRqF2Ws-2_543QX2-QdgpHqGT-2-wdJLg9kCKM8TTh-FmhaAZdeW26P9su_gG3GSZjvT52dQ_kOumTgBxjDTizw8FeMdKul9HGlrOHCvB63v7g7-A9YBFaqUPosEKyiZmnw5iHZwt113iBTta2trjBZaTxVT0EwHyRNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد شیروانی از اعضای ایرانی مافیای فوتبال ایتالیا: با دیگو مارادونا رفیق صمیمی بودم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101650" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCVTs3VY0slp3_j9yEyBjylNkindt01gfrlPg0ngBWTbnkZ_BQJMvdWH6QuoPhfLZVeLkA_wS04Fgs5o7uMcw66CGPNxNKaFqiKOJ0pEEeh_DD1UgY-iKPIXCgh12XBRgJYqzhZwQpi4H8vRZktqq865Dv2C7a4MC7h3HO2Htf9K2KbKk34G4plKZlmsd7N-nLtXPyzFQ_CFaCXM_UGm9tCngsaTIGt_EjEA3CZJ8FX39RgzXFGLJSXTfLGhTyHpq8iBYhM9HKYM5HH6tQXDdGQGvtGyOfVurwQOwcbARwec8KfkkM6ZByPoGzAlg83920CTwSdt-rqCRrzGjbc6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=iWwfzYoupbJpiX5clYK44Bokx_yJpdlJzWSDKg2aMYBclLUxORsfJFMtUCWDOQvDMq8Dz1RkdbcIolLKLnHn5KwiMrOsTE1kqcKbfVIHzSF1QLNylE8yyNEfKcVEws2EdreokU6OOiJIwmIFEQLEfmQys3vGvEVYBx--H-yHCN90cHEo6yVVy1U1Bjq10lVwnXG8cGKYKsRec2wGklq20iU41KTmCbuomvFvJmaKAMwBYpEcwiS86eQm8RRbbAKK9cLg6od5JzeSb2jh3zBO3mOiPXpZZZn4Gna1Y45DevD8Dcy2hX56io4U8ZM2c_DIufVSARTSL0gnQ0OmtrvWpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=iWwfzYoupbJpiX5clYK44Bokx_yJpdlJzWSDKg2aMYBclLUxORsfJFMtUCWDOQvDMq8Dz1RkdbcIolLKLnHn5KwiMrOsTE1kqcKbfVIHzSF1QLNylE8yyNEfKcVEws2EdreokU6OOiJIwmIFEQLEfmQys3vGvEVYBx--H-yHCN90cHEo6yVVy1U1Bjq10lVwnXG8cGKYKsRec2wGklq20iU41KTmCbuomvFvJmaKAMwBYpEcwiS86eQm8RRbbAKK9cLg6od5JzeSb2jh3zBO3mOiPXpZZZn4Gna1Y45DevD8Dcy2hX56io4U8ZM2c_DIufVSARTSL0gnQ0OmtrvWpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=c0svGZYLAIiAgnVM3BDyWZ3TzK71p4JAYxpiLDFluzYAN-7TAVACJbTbCSxIXQIVygM-pNOPrNp8Ym9zXLXNqZN3AXlf3sVz4uOccFk0l62feO-wF2Ia4FT_Pce52UmlnWWESrOdX5KPIIEtgbHGhHbrP5POFG4BT_NaJv7jGvUvYm2tYrvHeaOAgDU8qbrbPQIiNzq-GTLpRudi9Z3YkUJRYPxqiNbdEeTwnNb5NWFrmkS8KnsPSt_83Cymp1e6f6YZK__siunXgGKLINOsQ058U4wCeltwaWNbgh6MkJabFxnZExlONMtVo8YMcpu7CzwztoCa51DfYCSqHU0PmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=c0svGZYLAIiAgnVM3BDyWZ3TzK71p4JAYxpiLDFluzYAN-7TAVACJbTbCSxIXQIVygM-pNOPrNp8Ym9zXLXNqZN3AXlf3sVz4uOccFk0l62feO-wF2Ia4FT_Pce52UmlnWWESrOdX5KPIIEtgbHGhHbrP5POFG4BT_NaJv7jGvUvYm2tYrvHeaOAgDU8qbrbPQIiNzq-GTLpRudi9Z3YkUJRYPxqiNbdEeTwnNb5NWFrmkS8KnsPSt_83Cymp1e6f6YZK__siunXgGKLINOsQ058U4wCeltwaWNbgh6MkJabFxnZExlONMtVo8YMcpu7CzwztoCa51DfYCSqHU0PmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=ak9r9SIrNtCx9kRx-P9Ut5yxd2aVMFJoBLgzmi6OVLqRjQxNNwhNtQp99M7eVYxCD_RNQWiGiW6u2fNh9Tss4DhRwIIiyzbjjb-P3XR9pwZAW2n4qswpED-G9WqAQ0noE2sOjZbhoUjHOukzxNESRiMKpcqqNPnGNBTLyWlrmPo-Tvet1Fcle74JbSjMLym-FFtn5W8s_5-pKvac7ClI8pejbzGs02sJFn9Vlx7emQGHwxQS0PCp7b37jqthpjX7xhII_FMCLw2EUZilLFyEzbEhOrDMSYI_Q9D8e3ohtyFM6OFQkapJ9zaAcWAjuvWMn1CMcfdLjBVx3N_v-y0SFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=ak9r9SIrNtCx9kRx-P9Ut5yxd2aVMFJoBLgzmi6OVLqRjQxNNwhNtQp99M7eVYxCD_RNQWiGiW6u2fNh9Tss4DhRwIIiyzbjjb-P3XR9pwZAW2n4qswpED-G9WqAQ0noE2sOjZbhoUjHOukzxNESRiMKpcqqNPnGNBTLyWlrmPo-Tvet1Fcle74JbSjMLym-FFtn5W8s_5-pKvac7ClI8pejbzGs02sJFn9Vlx7emQGHwxQS0PCp7b37jqthpjX7xhII_FMCLw2EUZilLFyEzbEhOrDMSYI_Q9D8e3ohtyFM6OFQkapJ9zaAcWAjuvWMn1CMcfdLjBVx3N_v-y0SFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSVAghbK60gYh8lmoLkULUKadQNk-silZTOvQAK3Ed5RgJFw7vxjALbliRL2fT5G98fTIF-RBNlzDJhve21PvmghosiOOAOk8UgCTPOXs8_OqIAxspDo0TgdNlm3y6lOZVmu6Db-p4BPtEwHXvnw4XvtELsLmo-29_i0fTvufDJegrQtdbskiXXkPirnkO7jjzWfPSU2f2uzw8PbNolDUV8hmv5uaObGUBSmtNeCaKHoNDErn4RWfqHxYeuM6f6nGO1543UgVpER6IBORicyUV7udr9Ld5vZG5AHchn6Vtz2q5NpEMd5K4yYQ_7dOq4Es0UTBba528xtONaHVYbFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfpOFby0ewWT7LkRjNwOg0f_QdpwY3fF_bXuvteEycUNG978RsnGXw3LF6z6edDZ0EqueRek0kOlJf0zYG23JdKWOwXGrLT1QVkQNshDiMtnIbMSW5yDVOPJHZ0lugFEQM231HJOouGbTSRx4gfPpAcH--6Q_YGYd4_hLoyXHnoFZKgmi-TgKRzEwZ4fJDF4TgOFvcPaWxILlS1dhFQ3VHIvpHlqpkM9atSMtuyzRhevkdyy-ptdez6V1oR-9EwLoemKbI1GLFSJ7F7jDVtjv75_DfyQ9hx9ol0E8ijBkHElqktuzxmsmQILJOvLY4avcEU7lt-DskKF37oDJv267Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMlutFbdggMv4b8cwmsE8kj6HQadlpm7MBcSrXNJCYkAwbFvCeWaorDsXWe91z56h0jW5eRov_pEAFVJAPg9rD2jYPpGxVMR4fG_6AO1bgO9M4aqZCzs4ePiwPWFiyp6Z9x4GyGZfsjBK4KlTbeKIhYAwMNL7xQuGxS-hTqMZsekAO6wRaRkBi0ZehOk-Ptm6r7DaXF31AqCHhEEB5kLdqgjjofEr553Zar94j552UXQifl3DIABxNHjPh3zanIgHHTYTXd8OGLKOhh-hJwrTbM6rlMfoGs5zzdeQOdunc1UV_6FNA-gr7U-ylX2JC1w3dbdHVuqy6v_vx2GBdsw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyA1-nSS17AgSYNVQUcMerFsCR7R8JJ0eyTNvDRZW5Sm9wOxD0IASilUu6M7vxvd4CAad_otXOnYGePcIDPsv9-f-mOavOYS98dDkEvvrLyCAh97H2najXHcRlTlKRlIeueqSrvcPo3SunaahjoQ_WMdLWhcj9rT-j2Tho0YF67_yVrwjyLSsfbEdc7v-aswLjGKkYiQArGpzoQLSCsFsYK3yqNSKkpO5wjptXba9O3g-rhcnB1VwgjkeClhaV2us8Q8uz3BfgFwpIUotdTsBFZuBNh5aedrA0ptaC3vZCrnHVnQrrlt8SF2TVfleThoKZT8JjOwWSJDxezUHyAW5VLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyA1-nSS17AgSYNVQUcMerFsCR7R8JJ0eyTNvDRZW5Sm9wOxD0IASilUu6M7vxvd4CAad_otXOnYGePcIDPsv9-f-mOavOYS98dDkEvvrLyCAh97H2najXHcRlTlKRlIeueqSrvcPo3SunaahjoQ_WMdLWhcj9rT-j2Tho0YF67_yVrwjyLSsfbEdc7v-aswLjGKkYiQArGpzoQLSCsFsYK3yqNSKkpO5wjptXba9O3g-rhcnB1VwgjkeClhaV2us8Q8uz3BfgFwpIUotdTsBFZuBNh5aedrA0ptaC3vZCrnHVnQrrlt8SF2TVfleThoKZT8JjOwWSJDxezUHyAW5VLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCJfHcuki8D5pyDyBWugE93tKXiwZWwcDzPoeYi9A-6DUn6WUTeNsVfnZ87pr9fgjtFEFSIwB7H0BkH3DOePGA6Dv41jYzRAW1b92Ge_itLlLQLpcWQT-0gPmrsIpNEG1OLlOF41v_-agDpxXEzHhkaT0HoOG8S1_N6NXXjY0tlLLHNkUIre2yFOGgGKFv58jRDiUsLo96PMNqajx-MivpdpKgjyEqL6Mo9SzS4l6aN-TcNxi_hLothRHXo4IMJ41NoOFzsA46XIu5Nge1OgKR1OxaF2ENrRs2Hz15IeCu8VDjAVuYyDrS8mi9DofUpLq36JP9R2J_yP-fkkVXH2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YorEnPIh266T28GvQu6mrsvQ0TemXqxi3GT3gUXeSAKyutHZp6VDvUbb6cq13Rx3vnwsvGQ55snbPeoiPoU9AiflT_k2OqS0nMbq_9vKIiNyplOb9nKOOdVr5VZ26LjNEkrkrSr2G7x7gQ2IBqctCSsX62RxeEUOOj57vTpbtrHGMcXh2rCOqzWdvoF9AYYp280Nvatj3mQNfRqsUw0jiKc8wOxUGo8kP9fuWEDCXN-MGVjysojg0GW0q9NJZqYUaqvQJpdfTGz8r7h2EZJbbYxWKLdyZ_3Dc9rzlPUhJBGmMHjWgWJDRuHGl_HXigpqs0_QMn61hJ9rjeqzVgyKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=uqWkFMSDG9zsAUD9Jyf20U9_-q4jFX9mnYR5uEinc5194HejLDWGGBbINBLx2sP0CGmaB_MWwS3ZMbtii8krqJ_JgVBpHWaxalBoPtFPFc-mdDXNfhZFkuP1LlrWIZGUXRdIDyUxaVSTLtf4Wn8vb0_S6XtnEyNqU9TASgZcorptZww-U0wLlyLgCiJJpQXXcUN50wPDnXGcP7KgieE2CBL2ciBsyrpk-UrX7P4RDrrqQ7K2CWYi_qP3W2GQ-Z1svf_ygDVsVS14_yMUSPBXozoa5IgkFy1fMjHWKP3MQumlmfRHXm9558lV8W-nnBBHjx0dTtR_ZS8_gLSi_dkdfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=uqWkFMSDG9zsAUD9Jyf20U9_-q4jFX9mnYR5uEinc5194HejLDWGGBbINBLx2sP0CGmaB_MWwS3ZMbtii8krqJ_JgVBpHWaxalBoPtFPFc-mdDXNfhZFkuP1LlrWIZGUXRdIDyUxaVSTLtf4Wn8vb0_S6XtnEyNqU9TASgZcorptZww-U0wLlyLgCiJJpQXXcUN50wPDnXGcP7KgieE2CBL2ciBsyrpk-UrX7P4RDrrqQ7K2CWYi_qP3W2GQ-Z1svf_ygDVsVS14_yMUSPBXozoa5IgkFy1fMjHWKP3MQumlmfRHXm9558lV8W-nnBBHjx0dTtR_ZS8_gLSi_dkdfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM7IPEIp2ALvPgECFSLXHoc1ef3NymaPTKD1hdMkQZ5xng_4HrxCbEQQLE8iQBbmB2kL63VXXNKlO1DwKlXORs8nm21epDgbyLuHobgf8uneAPWWOgkESsGMHBvZKBDp87kk-GRn0BorvO7QSXUqJl4sjfUwEA0H9_WrmbgAgGw06sww1RfhlKNT3XIi5t8ygEt0INK5RgeO9us1b-APSKlZXWpI4NjHKM2PdgaiFOGj-2kGw_eX16pUP34ua4JelFi0ivqdYKrE4Uz9De4PWcDTmIM5vEXyuJ2Tp9KO4HWEkePZAHQXG0AUKt-_2w3ug2qdvlPq39TNNgVlpAQx1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL3_T9sGt7s0M_2bFuHanc_WLpuIjZBfKwPfEBrNq3VAk__UXWCDw4qaOBYJzDTNhz8Vj7HZ6gGeHDgjJr2X6p4OBrewLKiAKynOTF0vfMGRWcKsjSkdPi5SwC_LSmU0zRpQ2S8vz8yc98L25RsUBo5_2lb9UC57txCBpu93hc8iQJIkYDctdPaFHMex8CSQ4Hz4G1ZP2f_Nqh_Z-e4ZVIrBELgichXdBik2h2HVG1y8-PPArNOqwHRuEMA3mvFr9zpBsO5OR36aijP7ascooXa9BCxHtEEatEZEk-vbjyv4myf0yaZAoHDBPyVMw0cjQmciZ57R8r4rsaRLJ_q9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOcnRaZAJl5AA-mIVo1jHK8xou6_MmH25iUsyer9W5j6B1GmsPxEjVNn8EMTBChCGQwSQkoEB5S2_gYZB_rddWdUIbfNWagN3NZfObNwqSqZFQ_9vl-WVDHion0w4yHRjGhOVvLKIXJ4yG0-sjYKXyUP7unLH8IFKdB8lu2jrVhSv-8LNYg-is-0CE4H4ztP2F7xYUAoQU-5k4wIRf7MpnRIcvoHKAedERCMvg42mghXs6sIQlMM_s9Bz2jmDEZEkSL_pGNzXUSBWbNox30norsDtt0OVwbOp3yhAp-cPLduCadopN1--aEjn6E4B0zKV3RbgZNDAnqmsGLySAxNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H53SQgQfHoRu0K_ZCv1hi2VlQL5zYWGeyXHAnJQanrZWKrNuzaFL24ZL4J0hiakzaTFp9G9WjiMjnzrWKACjRhrBBPxYjb0XGC0CjlZXVccOU0jEVvdhVeApljEsBKw3dotGKDrItwDulyFuot3tVRbgTPjWeVMQOWwl7Bxk4DDpyujjUqP7ssQxsy_B53SZ5nSQApXHiMTSg2PSjVbzaBULzsI-CqB64lU0zstTapEG713kB-FyYWlvs53i72eOIHKMQdyY9-_Jl_rWedHQDEy04UxEUoD0DPUK9o_SqOz9V9TPDjEy9YRpLv8Gi1pJKANNqlgWhZaFbJg4EzMYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlfiXDeavxoE_xoZE5PbWbP5xOMcn6NkM0ohAdzuOa1SW7grvQ2m2OUWVpZ-N_z7z3Zn2KhRwFcutvGE0Xfs2YrmVv6_ErrMbncJLUp-WAyTn7cIUliI26VVFic1OPU3JadBjYBlyLELCnULx3OxCSU51tSRVaLX7b972jO69VKfmT2FHD5WhMse32dXEUZaO25r9CHUSSrd0AdN9tgvORKn99xYrRcU1jGWkdJnwQpR3rBMwxIYMt7oLJZ-Ev2fNuwGyP6_9OcJGWHRRLjTVg629C3jGKnyEvU4IVdDbkgeagOjNHkwW3GlUE5IdAjKjGbS2aDnOHVXg0sv5sAHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dvdizPiATpEHHqmG769OAV5J4SEi6ArjuYrjJ_0lzdZDFnTH95ykaQkaTtSiLeR5K_qz26Be2BGF5d-DN3QcJtDPE2rnpmcKtvt44v9NNIJtxXW-4ZzxpXnQVjYnltOrObRlSmgaipPjzWSWfBaN4ii_zcBooAdMJ66uNcb7aK2AFi0YpO0L854tJEqzn5Ahqiv2g45CSgWcWlAMdmjqMClTMQFZZmAplxmwKu2IWeZJOURnEUQYg4fM8JP87wW40pndPsgmbyrkuoPWogrgySyfm1MdF1lkwJH6pyzNpnbTOMpjeFw_KY5NMvnUb-kU7mb6xc7GPa5GT1z6LP6zSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmGmVIfbepQ1Ef1GedMbbhHAss1EV6GJW8ZrsKYSrObPtAbNeeOMS7KI7_CvVY6lREQiS0a9USe9Y3S8obObDlBd91MMWVKjhnCcl2GX8WrFTKOAM5-qWRxU8uBPRg5XiEGUoH7LFzn7-IM-OQ-3Z5VkTcHeTYGmqza6XpgiqZuC3fPWc_fzMCjc88AZ2XycwtIzHM-3iZJGCIzQdAn_l_HFUUthbaeeuHZfv4nv_s8LSz1AtHg7sfkF2uCO6KNEdlvFt0DiYPK2Oz51tmeCpVSDhqXdX6XHtIrGg-FEVbx42BC2Tug6lyIO8pMATY8F1NPx5TWdeH6ECgQ8A3ftzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkxD2n8bSjQ6cbQGVWwQUmD39DDOWn1Frsr7YzpakqvxZknGo63pUB3fSimfUagCODKB8aNj1DW3fA6OPgljfj6-4BwhscZKKjm30NF6QYMXoAkQh4UQ0OtTD_BmhntW4_IDbymrqmJ86UqkTUaP1zckGHPbnjsQXYWwkEX1o8kCcTQCu-m_oLLX1KuEghnioWfI9n6Gr1vC_G_O5GnvvbSxzaXWjJSLTxkoNJhJDxXKWRpbGPvWXa2yyTQIewfOx_lNwWlpKYsqzCfFrE2e8jspc7pecEG0NhsZ3ZcvblUZWuhwCqYnWQDhiDXFRvO1xL8KTObDnYpGc_b3XWu1Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=NvmrjO1ujwWWv_VvUlo3XMSD9oREgtynPmDGXu5iKPD8usVED4UHb3zjBGRFOcF8IN5WATbcM_Er4gNJ5VrWIU1ZAY5nnVAWBPL_PXPIvBXMBHzdEBE4_fnxxb5AWjOTczJsN3tpm-JGXkSpCdnG7pZR89Uvie-K6v7QZ_pz5Go9VxJNm3SNKI8lkRxSopcfqhU0FHYSs0Gj2YS_Y882pwQOl3AmL3qSXNJo-MAqGSydNA9vjTWSQ3Df8kOX0dYKHnHJ5ByQzi91iE9JtGXTTjxUMQR7mqXhMlu4t217sr8_HFeeOprMG-hEpkQ0bMaiAWfalCLrVFvBXZO2su7MYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=NvmrjO1ujwWWv_VvUlo3XMSD9oREgtynPmDGXu5iKPD8usVED4UHb3zjBGRFOcF8IN5WATbcM_Er4gNJ5VrWIU1ZAY5nnVAWBPL_PXPIvBXMBHzdEBE4_fnxxb5AWjOTczJsN3tpm-JGXkSpCdnG7pZR89Uvie-K6v7QZ_pz5Go9VxJNm3SNKI8lkRxSopcfqhU0FHYSs0Gj2YS_Y882pwQOl3AmL3qSXNJo-MAqGSydNA9vjTWSQ3Df8kOX0dYKHnHJ5ByQzi91iE9JtGXTTjxUMQR7mqXhMlu4t217sr8_HFeeOprMG-hEpkQ0bMaiAWfalCLrVFvBXZO2su7MYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
