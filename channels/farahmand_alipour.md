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
<img src="https://cdn4.telesco.pe/file/r3LpllfWVpwHykhgQ7_c-vmXeO-NEVKYHUcQb3Z4cxQ6BKZkxd6p8nqQjA5EuQZx-bQXmwq6cEyjW8J91TE8L3SE69QvUwofW4-qwymJWE4_DRQvTGyDSEcvXsgJs_WU9p5qlzxpaa-tbWWAJev-NJEmA9hMJ9YKB4qg9XtMV627tu4wNao6mR_RLxfddtopoIIa-m-516oZ2R5Xx0p99fPmqjx2Lf5khQfH4wFQgs8busQJPjsbOani6rA5y1_JwlwLy6WfQtduvZ4N3rPiYNHggnHaH9gnjm6uZNs-WpF5j9kuwLWZdp-At0Q8rmLFILTW0hZyWU9GBgI_A6RVIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 20:29:25</div>
<hr>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgq5-bj90lOJ3EZOrEqyh25aVxF6nFKyIg7DJh9WYa3gNmh3eBkTa6jhQrq3mXJOHJMkx9st-q0sfnPwC0MigaeGEcMI6zj4Tz53rCOASxLXSCdFpK9KRUo9m6Ux-71fWfSGe34nvy5ZAXATURUiScrGPXFX54TA5_q3D4sEL6EjR3-1CnjB2HCAVx07zqfVQaajNFHXXNB-wjYuztOAokw-V0XswRrNCxkdJN1tpwZKmtsDzwbmoYjrJskysJtDcCrC-thGD8d2_wpzQDBalA2CHK-NZjpBM48wA-5uacfNbdcTeMYfnBRumXpNSSrdvg3sIeNlwUYndp3mmQSWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفته بودند مذاکره برای حل مشکل :)
در حالی که تا جمهوری اسلامی جمهوری اسلامی است، مشکلی حل نمیشه.</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farahmand_alipour/5679" target="_blank">📅 19:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OOB1Dn50w4GsobTpwCHE_bV0u3Xn6-UGNBEFLqHotj5Lyeps9OiP__nJaHlb4hjhwnphRcdHonRXdL6R9weeHE-sjjRSjjGb8oEKRBysdUf5Uvrlo6T5wGBLy6Q394hyKgfq2ta9TqcakqrXPTrQsgxDnRxy6xDZ-v6jB9_JYaHd0NPnpueUs0vx_s2Q6cNjv680_oWY0ya8wm0mlVv-fP6PUhTAwWnMiYGJJqmF3b2mQn0k_ObgBdNAV2Pc0g3QdF4SF_z2rgZ3VS7qEeNIlJvbyvUFAptc99zv9X_owPCWoKYd5HqSQ_9sUpqobFSGFDZx354gWG2teC8V6nBfew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd078eea01.mp4?token=OOB1Dn50w4GsobTpwCHE_bV0u3Xn6-UGNBEFLqHotj5Lyeps9OiP__nJaHlb4hjhwnphRcdHonRXdL6R9weeHE-sjjRSjjGb8oEKRBysdUf5Uvrlo6T5wGBLy6Q394hyKgfq2ta9TqcakqrXPTrQsgxDnRxy6xDZ-v6jB9_JYaHd0NPnpueUs0vx_s2Q6cNjv680_oWY0ya8wm0mlVv-fP6PUhTAwWnMiYGJJqmF3b2mQn0k_ObgBdNAV2Pc0g3QdF4SF_z2rgZ3VS7qEeNIlJvbyvUFAptc99zv9X_owPCWoKYd5HqSQ_9sUpqobFSGFDZx354gWG2teC8V6nBfew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معاون رئیس جمهور  آمریکا،
نخست وزیر پاکستان و نخست وزیر قطر،
و خبرنگارها داخل سالن نشسته بودن، قالیباف و عراقچی گفته بودن
اول خبرنگارها رو بیرون کنید تا بعد ما بریم
کنار آمریکایی‌ها بشینیم!
مگه آمریکا چه نمایشی میخواست سرتون بیاره که گفتید اول خبرنگارها برن بیرون بعد سرمون بیارن؟؟</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farahmand_alipour/5678" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=N55dWWRotSbpoEjWX6mYCd2gSjmSSqBdAt3kDW-XyjPyQfgSoJERTouzuwnLO0gDZigppBzalz3hcbyDYCHmdb9mu09X0BSq8rmwUZGw7EwZoCBEzsWGAQAamBBrexQnxjPI2xtT1Xa-By5Ju7h56sGFJQG9ifUMPhP4LcG0v-tSeTha5rZVyyImh_BVCe7dLE3vdtgDBENEPf3EN3GUmtLrWKAgaPAlUvAgChqH_PqScVSltq6As84gMxqdX188KhL0aYw7RPVuQ_Uj7nDTlYFBi43wtdyeEwrak-k8mIY-kEyfQyxnp1CGZzecD8w2O2BFcL-fUfCy9_1yzWrD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2464c582e.mp4?token=N55dWWRotSbpoEjWX6mYCd2gSjmSSqBdAt3kDW-XyjPyQfgSoJERTouzuwnLO0gDZigppBzalz3hcbyDYCHmdb9mu09X0BSq8rmwUZGw7EwZoCBEzsWGAQAamBBrexQnxjPI2xtT1Xa-By5Ju7h56sGFJQG9ifUMPhP4LcG0v-tSeTha5rZVyyImh_BVCe7dLE3vdtgDBENEPf3EN3GUmtLrWKAgaPAlUvAgChqH_PqScVSltq6As84gMxqdX188KhL0aYw7RPVuQ_Uj7nDTlYFBi43wtdyeEwrak-k8mIY-kEyfQyxnp1CGZzecD8w2O2BFcL-fUfCy9_1yzWrD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دور اول مذاکرات به پایان رسید
شهباز شریف نخست وزیر پاکستان یه میز برای کنفرانس خبری و نشست آماده کرده بود که ج‌ا، آمریکا، پاکستان و قطر اونجا باشن،
وبی عراقچی گفت نمی‌تونیم اینجا باشیم!
و ننشست و رفت!</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farahmand_alipour/5677" target="_blank">📅 18:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z14DqUyzcDLMh8ROn6n-yBOv8MaR1Se43nWVZ8FhzWfOtRLwGP8APzHGIazEDHKlqOY-flR4SbKb9l8gJ9EE-756Y9135rGhYPtvvOjgW3lhYUr1lxieB0pZaSCpojDX6SAUr2lKV_MW2zEO2VS6MD0B3weX9LzBq0iTFHmW3WblJa-kviI2tciKRisr4mEd8kTbvztC9_M6RDgh99nXZnR0olbwkw0E3VOTl0bsqTO4BPdWRsBN5EeS2TvuYM2snjUIv6OvJDjzNWeTcJvFyA1_sDDtOFExCH_njdde27USsc1BgPECfXm4PIBixP2h7z1_hGOkBCScSTozgPYZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5676" target="_blank">📅 17:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b14c3d6d.mp4?token=nTQ6X7_GjFCnizdx8V8F6mj3N07uha1B7benIhZ0wWwY5Rk3DTHcckpbx2EmNBWdv3KA959uigciTguWGS-OIdV6cyGSnDtI2J-THoS7yISivHCcK38D_4M45cLfLGwLvs2ieV88ZwfUOrLR777xt74lmCE9OIE7K-cYTA_qPnXuThoxXSxxM0BTGhWEdrQI2mh5lSsxcwhMBRZKH0Q1y7j3-NvE-kd67zl0_DezR1q6BTUTWyYlcdr1QtaceorqmICmcQkPqU5LCVyQcse2MEEp_fIXeSnSIgc2-OQTQJUo2UTSiswlBcQIk9JZ6UxiRkw70rMaY6vOXNeK5pM1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنایت‌های جمهوری اسلامی علیه مردم ایران</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5675" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adRz3-2w6mQiiUOo08V7YSgkVAHlQHYiLZ4VNw0VGEPyi31OxK4m_NegFPGCor1mhENBjjDhhpkK1m1FEI-ujToZnz0LWIJ3uheyOH_FtMzt4vw25vtPr9JfO6IOnyYalOqakQ1IM9IZfYPhZev5nbhSvfDg7YCT6w3phHifqnFEDKfdBtqOCN3ajD-vdH0NZhy2hspPI_s1u42UDJWsWBU8sFotrZaNlh-xmCMtEEYylenVUwok4LCao1S-p_Vxv7PJyapHjRlto-WfyWzfJ1pJGJM9y9xd1SbJmH1HqGBHJdAVKdXVgvgt3h6q4WboVkT2L-PKk4n-wvxoW-xAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپِ کیسه دوز به فاکس‌نیوز:
«آمریکا می‌تونه به فرشته نگهبان تنگه هرمز تبدیل بشه و ۲۰ درصد از نفت عبوری رو برداره!!
اگه لازم باشه، ممکنه کنترل تنگه رو به دست بگیریم. آن‌ها رو به‌شدت بمباران و نابود می‌کنم.
اگه توافق نکنن، از کشتی‌های عبوری عوارض می‌گیریم.»</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5674" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTiHHa-YXTxQSSorFKHxNGavcGKzlqJfvcr5zRlQz5KMYU9NsAC1rRDHqhx3lmpa67xR_uRLyFMp9vy8FoMXM38-KdBguvomctElUwmqtsGuXs435GJvlfHyqaaJxuhxlYbGTWwk_xNeu0erW9TtNAXrAYdeN1wE0Q4XsPMEploQIiJI7lZDAa4PysDUGBpSpi68uhuSGnz-ICmx5BdMIaoa-fd1dZcdy9uwe0ssTB9LrsmEg7pxV67v9GA3c6ovWLWqETqYdlqXelblB7uZUj4e1mWW6pByHn1giDEn-dcu_2oRbjaQ0VKa68npnrgk_f5mHq2MHY_awa64no48Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2VchZg_KIe1nUsEPl5XuMt5ion6kWkkZ6STBX2cTHaRUPPQA2m7ZWHdrg40e-uuFSiUdCiFNKQbxxlXp6SHOURkCEHlS9HSCeCzA_1wtTfrcsAYcZ7b8PZbGNYfA09NMnsZrL838Yi65hVzvTzLK0xSaovujQD48G2LDtEPRB81eMmHW1nz1DAgofZZPbwps6XFWCC2q9d2Sub1tnnP2SHKUkg1ojn8ZKfO2ivTiYZnz6W7k5sfJCXtXXNU4raoOINQeRrOzvjaQU3mqu0LIN6Omtyb9MYjh6sZFM2DCaaR20tspfroRyQsOHAjvGkyWALy1JU1eU3OX22jobNVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2XT7SAcOvHN2TvfAOhQ7qlCmXZzgjSL-gz66ArLCsA4wu0PB9tDX0NlocguSyc-qr35uAflE4-NFZkbIoyJoGYc7PO0OrWbHrIgoMeQKPL1wUU5P2oT3nzUfweFrpmXFXqv2hNX8KsWMNqIK9-nxV5gK40VNxws7U53ILclFUGqW50RFdRIWFisjMmT8fGDpLXnvLkWRaS_BvfquHdmjPzdAr06Xx6Fi_DOwdavAijfeFoXaelp1reHD6x9TZUSQZsrQq93WT_AOk3cuz36zIQevya4mms2DFvqPSzWHvEJJxLqH615TTbhqSRZ63Ta5xRoxvIF3mRNPLTZemU2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsdBrk39VUkaHgUUDD1WoOmMQmDMorD3dhmQvAO7we9CoD6EHJ8_PsYOX_BGSktm-NENl7KEAXE616KH2zV5sCqbG36qPbbQ-xmkgpvTf99pllSTU9IPdA0_IMSxk1qG6Xqlt8CW38BZ02J-SBY4PnWVk0fv-Bj3mVVWrVf0bhCro15YMeXEGtQK0iG-HN8ww2hE3GAqONoMk5CqEU8JXbhAMOeFuD6BWgw45hNNWLTgBu2GNYpDPj4KIK9kXC2PN5wdOLzXxxVSGGySY0vz7gyocrGk-pVFptS6iZecRscGil-JSr1MYurFryI-32rCSFuTSgayzzviY_LJBOsNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwtPyXg7KhlbBMbxqa_RCdMGC3E4o7mM0ehXNAwxJIvS-nat5C8Eh9wGMxMF-Ul0ZlgGb8i-HOnF21Mx8011disWXDrHylyx70KRCKKt1W_waOJCCKPYVydQYKhbnxmQ3_keQlVtttHrp1t8tzE762Jq1I5nhrwqjyJ6kSln14cQ-3Gqb61m7QZus9hQin1BDN4WVJrBwLh5IKUp3AWYrog4Gv5_mZ2KeZOLd8-Q9Y7D4gtQZaukReX6Senu7w3TswIh_Arf6BFbKi7XTchHlz6QoyCK7ziK52dcB1x2vnDIcBV_Bkrr7PYSEb5Gh1N6VjrxyXpO2wvE6SJzDFgS_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzKE6uSMbU7sZeWbgnKfm19mNP_SuTxESzX7tjBIzcNrhaGWEAMY_snjqqgdiEZpwWcBZvQHJKn3CewzCmq3a90MRwQpMUEpQdl8qc6Q3u9CDOcWO3FAr92cMt4ckedyhPSyARKtTj7by_YrlUOtZ_mTZDnGXE2IhEPmZmxYCu--cznmh1hLv7GP2xvnqTTfmiODgEqwdMPkUcW36cAfBJM-Yl82PCdrbJeLSg5QTDhomeZQFtic9ztiuEj77gbxK4MH7T81DLwI-kp60O8WPmdOXpLg7jmoXa0UjNt-ceFLL5AJNZJ8Lv8jbp2zo7xzpVlt2u899xDMt_M5GvpA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CkR7AB7gqgTIhXt8dx0ZN7Uqy1LXtzYw_YClOBmE1DjVE7rDxmtXcB6Zmw9fwfkMRUQ5AIZEwlJOVBg9Ql7XGi2PjtteDh_rlDj302bf01hfIZAAm_07AIFsTc9RtcKMVxOhQrpiav0ZhInUhkn42ySRuu3rfvyge3LeVvx8mrGoMGDUsI5bjbQ_og1q6gi9skWp7UTZxywTtzCwWkoHKbBzXh2ZVn2QxSo1DZQuOS-iA-nOmkXtg4bdYPcJhfpeebZ-rLeyfV0XRs5y3sL9SMLCUICO0Ld9YoVw1q47G8Sm69IZ3wAHsGAE1cxqSDCK2fagaA5AZqsID1SjxCvPuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=CkR7AB7gqgTIhXt8dx0ZN7Uqy1LXtzYw_YClOBmE1DjVE7rDxmtXcB6Zmw9fwfkMRUQ5AIZEwlJOVBg9Ql7XGi2PjtteDh_rlDj302bf01hfIZAAm_07AIFsTc9RtcKMVxOhQrpiav0ZhInUhkn42ySRuu3rfvyge3LeVvx8mrGoMGDUsI5bjbQ_og1q6gi9skWp7UTZxywTtzCwWkoHKbBzXh2ZVn2QxSo1DZQuOS-iA-nOmkXtg4bdYPcJhfpeebZ-rLeyfV0XRs5y3sL9SMLCUICO0Ld9YoVw1q47G8Sm69IZ3wAHsGAE1cxqSDCK2fagaA5AZqsID1SjxCvPuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=WDZqEGOBlkKvqHLWEL_e0sQTRul-SENYOBKwCHuz5kib63XX_hdNsqX7hcEInJKmA_D4ve8mziS176JFCpjcTabu2KSQSVrU09Edp4Gc1FGJvsw9Kr15Qo6sNczO8biKziPilgMSZe4NMf4NpPTZ7O0JIikfmNkRmajhu5ZUVOz7uENumMMKkJTHFWUlIiaMl4zB0NNzf8-8QyhDFiCEq4gZ5HuJNvV7dD6quiH66Ul_Gx9sgpoi4dBIMMtdTS32QgVuL-M29rvfCdgdgZbBnwSQm_mgUxnLfAvdP1kYITVT28HBFjHG5xocy0mMQgx5C6az9INv3VLFkBMMWi86xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=WDZqEGOBlkKvqHLWEL_e0sQTRul-SENYOBKwCHuz5kib63XX_hdNsqX7hcEInJKmA_D4ve8mziS176JFCpjcTabu2KSQSVrU09Edp4Gc1FGJvsw9Kr15Qo6sNczO8biKziPilgMSZe4NMf4NpPTZ7O0JIikfmNkRmajhu5ZUVOz7uENumMMKkJTHFWUlIiaMl4zB0NNzf8-8QyhDFiCEq4gZ5HuJNvV7dD6quiH66Ul_Gx9sgpoi4dBIMMtdTS32QgVuL-M29rvfCdgdgZbBnwSQm_mgUxnLfAvdP1kYITVT28HBFjHG5xocy0mMQgx5C6az9INv3VLFkBMMWi86xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=tOKHPahwHA62qv_YOtRTyNvTu6A99Jm8gWgJG8KtVflVvdCIn_ZStjhB_GsytPBovgYM2gSRSsnlhwG9P3fT0-BdZLCr82yPCeex1QOMgINuqXf-ufhLQZyk2S3THgnogU3-o0RaQ0-F0uh8qq7Bti5A-7LF24DeZKb26YQAzA4hroIRzznIWlIS67OIFnt51qBEHBm7t3fov9KDhL0XhKY1ffpSs_KUvJdR4Kicc15IviltVvDk5MsmZEZlndHiowb7g-Vc7Sqi6V2KMl8QONISJLAHOK57TMcVlHDdcwfl6rsPZ7CgJEawO6-mFa3Qp2xS2PtRYaaLZcgwmQNU5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=tOKHPahwHA62qv_YOtRTyNvTu6A99Jm8gWgJG8KtVflVvdCIn_ZStjhB_GsytPBovgYM2gSRSsnlhwG9P3fT0-BdZLCr82yPCeex1QOMgINuqXf-ufhLQZyk2S3THgnogU3-o0RaQ0-F0uh8qq7Bti5A-7LF24DeZKb26YQAzA4hroIRzznIWlIS67OIFnt51qBEHBm7t3fov9KDhL0XhKY1ffpSs_KUvJdR4Kicc15IviltVvDk5MsmZEZlndHiowb7g-Vc7Sqi6V2KMl8QONISJLAHOK57TMcVlHDdcwfl6rsPZ7CgJEawO6-mFa3Qp2xS2PtRYaaLZcgwmQNU5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WleLbUb4cIxwDo9TBu5ZxHDnPFZcDdKM1F6c-7Q1dZPeY0FwFQvEL3G5voZYoGSKkrXypaNP7txQKhaS21t4mbeEcX3WccOqr2cbtLKv-qdtOtjRCImd3-MsZbyVGeUF23jZ1jln6R_5VIcriNl63CuSMSr1Byu9yKEKjOw68gfNJIl93DcU8Gr5IuAnNTVTp6xDfI5vxIO6tDpv7pQjPpLY8EbhWBH_ZN2bi48q6rkPwYryWfPRPtiv92wrP48fp1jV2KuLcny4EF-1VlvRjGI43gA7wswMh8jBuFXSaFq71WcKsIocKUnw6GLer6j500-byfoSq_85rnJUNs5SXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=KCDbmqeuIFA3KC_dQxdHJYbEVcTQTeeMIGf6WivlfjYojgteI6XmifoQ60RhO5tjVvh7h2LJCrDQBBY5dhUj_embxxAphanziT_I84WTbRy2r2q8p1oXcSKcS-e0DfUYtVv7YsUi6hLNFOMJbZAbsWJ53sMDXXzyZQ20nMohg67BqU9w_uF1TpmhetXNFhErO3d3QOLWTgdKcD4_GcTyxmHoBN0jHWG7UrlGi5qhlcHjfYXHB7zb-T9AH4UrHdQEg6ZTJ0EYHzzk6jdup3BDehKu1xvU2y96OiT4V247wxps3lYqD6lcLuAxqbvts3a5sdC6fkxzRBYqaLmJETFsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=KCDbmqeuIFA3KC_dQxdHJYbEVcTQTeeMIGf6WivlfjYojgteI6XmifoQ60RhO5tjVvh7h2LJCrDQBBY5dhUj_embxxAphanziT_I84WTbRy2r2q8p1oXcSKcS-e0DfUYtVv7YsUi6hLNFOMJbZAbsWJ53sMDXXzyZQ20nMohg67BqU9w_uF1TpmhetXNFhErO3d3QOLWTgdKcD4_GcTyxmHoBN0jHWG7UrlGi5qhlcHjfYXHB7zb-T9AH4UrHdQEg6ZTJ0EYHzzk6jdup3BDehKu1xvU2y96OiT4V247wxps3lYqD6lcLuAxqbvts3a5sdC6fkxzRBYqaLmJETFsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ikHU-tMozsNS_cNx2HKMKsgZb4bqDGungIM1gsDjlkLKQ6fp4W6_pO54lnV7gJT6vJiGyxWsdhDaXMFoCsMWP7UpFXKz33f7xKKh07IKpGibJlofC17mWGZRIrNdzlFCtAILhVu9loIvPB92OTKr2PxKjiP5m6mVtlzVU4yjt33e5PF5ae3eIjV6Z7AFR4KE1AHkB9gT1v3W_PD3_8jAbmjduMKKK51YjkQilpd6_5KKjaghDOpkPVwFG_ekQebq9VJdJpDd2KSnBw_6hLQ3Zdggg6YB6RQpmA0YjmQNL3_PnBRixGeySm2HO4ka_koXEIO5-2EOVyCuwE35gE1Vig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=ikHU-tMozsNS_cNx2HKMKsgZb4bqDGungIM1gsDjlkLKQ6fp4W6_pO54lnV7gJT6vJiGyxWsdhDaXMFoCsMWP7UpFXKz33f7xKKh07IKpGibJlofC17mWGZRIrNdzlFCtAILhVu9loIvPB92OTKr2PxKjiP5m6mVtlzVU4yjt33e5PF5ae3eIjV6Z7AFR4KE1AHkB9gT1v3W_PD3_8jAbmjduMKKK51YjkQilpd6_5KKjaghDOpkPVwFG_ekQebq9VJdJpDd2KSnBw_6hLQ3Zdggg6YB6RQpmA0YjmQNL3_PnBRixGeySm2HO4ka_koXEIO5-2EOVyCuwE35gE1Vig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=C5Y2UkP-h10pNUJlTv_GPA7SjV9kXcTzIaa0fX6OnL-ad_pM5ji1FNFDA9tqyDRFbylnz3SN8UmA4GJ2GKolAmtzyVXv5GFNaGetxLoki0i6QcbMbsPp9IudIQxoCyFAw6Vj5U-X407C9smR_vHsfk-pMfHh3v1B68TtYRg-4E1UwvTjPEeREUGksVFELDm5qt9-w4C8_HnTGY1M3toTS7g32kypY6gn81_WvSoa5iMh6pPkznkVz2s-c93XxzyJyWJY7LM1St-EwmCw4np2b17wu6Ajba2B3Hco1tMC4j5wMVXe9dXkEt8laUXGYw6QeaxoliVccE1WydaL835emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=C5Y2UkP-h10pNUJlTv_GPA7SjV9kXcTzIaa0fX6OnL-ad_pM5ji1FNFDA9tqyDRFbylnz3SN8UmA4GJ2GKolAmtzyVXv5GFNaGetxLoki0i6QcbMbsPp9IudIQxoCyFAw6Vj5U-X407C9smR_vHsfk-pMfHh3v1B68TtYRg-4E1UwvTjPEeREUGksVFELDm5qt9-w4C8_HnTGY1M3toTS7g32kypY6gn81_WvSoa5iMh6pPkznkVz2s-c93XxzyJyWJY7LM1St-EwmCw4np2b17wu6Ajba2B3Hco1tMC4j5wMVXe9dXkEt8laUXGYw6QeaxoliVccE1WydaL835emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3nVVPF61OgkiATNO-bOBoxhWNO1N68f1riCT8MmeYZRO0O36ipTlLPEdnoA6JPD74y5gxhqnqkI-fQqOyAsaXfuFiEN8b858-42yDYL9jHsxpRVTvABkbOGobyOMCyWdwOOK8kxGmrDTmMNVossa8e91BuxdiKwG6qgBDBbUubfcgp6ndPjqzv8jNmhwOE0pzT5zlntZhPPOFKMaYDg04Vqd67JnBWhEHUgr4KyesJDty0x88RG2R9tfHbNkkeuZNYTEc9pnZt1Aphk6A83vuUrhL2bShiWaqLSbOLG-zqJ9psVzZMxgWQf5VmKyZSOwkAbWIXIPLrzp4YB5NQDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ll1rCknwnJvMkFTIy5vmij2aJpveuYh6Vu9ZAoQQoaVy7FOT9dtcdt5WlUz_UjvUkqvW0_N3JsSr1ESR_VbFFKIXlRRMoEfgnqIP4N-epgkr-VAAxZxNl7LfELtpHRAw25oNBHtC2V9UId_CCm98R8Ra9qsS5OB_ai94iu8_ogJQ43hAlRWIjfQ2wMAmOkOuL9BGItHTEwWUmnIXbEcNGxgo0Q0njcju0d_zIsW39t7I2_2K6RGZMi4lnn5q1LHmEj-A45TEKaw0NSWYidLdmYz6sYtj05Eht2CXNYDlrEi_2lnkN4jCoy5BY35OdMnkrQvUeMm8UNwI1zCqWD_VaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=ll1rCknwnJvMkFTIy5vmij2aJpveuYh6Vu9ZAoQQoaVy7FOT9dtcdt5WlUz_UjvUkqvW0_N3JsSr1ESR_VbFFKIXlRRMoEfgnqIP4N-epgkr-VAAxZxNl7LfELtpHRAw25oNBHtC2V9UId_CCm98R8Ra9qsS5OB_ai94iu8_ogJQ43hAlRWIjfQ2wMAmOkOuL9BGItHTEwWUmnIXbEcNGxgo0Q0njcju0d_zIsW39t7I2_2K6RGZMi4lnn5q1LHmEj-A45TEKaw0NSWYidLdmYz6sYtj05Eht2CXNYDlrEi_2lnkN4jCoy5BY35OdMnkrQvUeMm8UNwI1zCqWD_VaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj7_4_wFOUWH1WyvsRDGsySO4ETfvjb-rAgFDMp6cIuq1lB992oLui_Ue8qSyxtF9pivBkge1w4c3CuSAUjJV0eTL1k5YGtUIPy4d_cl8vduT_eblVfxkTTqsS86Z7PvY1T-SznG4SEx3ur1VxsGkzO7O23RBdUVqcZk6LeGvOSptaldcW1Gcvwt6hcQXFAyV6r-6os_UdzrIyj-csubcdJXjZ4EcdYf3fGA13jiv75UGefEuuVjPm0YLdcjM1ngAmFw3ktwCNl6vTjFooY_tPpeLT2YKLmDXTP5mBCyg7sauacdBOqmL-Xw-kK2ImTkAnj38AAfu65vUSwi0uo6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=keanTfmQkkYyBfgkvQRrWRibhIWHY6FbiU4HAx4L-U9oE21iv5Ycmet1bn9G_vHq3QCB_-tyAMmBKjKp9xbFe9KGScqkIA80Q9XqA4v-xhtbbDWo4r6VMNVQwN7Iv8HDvTjWsFh5ZMU7pvAXuiD3vc0A1Hmoq-mo77LcYHTKms8APIrohBqdw1i56s0_nt2TrHHswRNFAQXzbjOwlCiI7fBlSWIA9nhYMitX3RAZ-TxsQh5ooVA9gL9WkkH84W1EET4GFYRDSIQ08kj58JYbvJFvmgjmi3FWRRqBFnKUYJz5zABtX5PlZgK6lF-RINu6Pj8wxPnbI-sMITCcVNdTfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=keanTfmQkkYyBfgkvQRrWRibhIWHY6FbiU4HAx4L-U9oE21iv5Ycmet1bn9G_vHq3QCB_-tyAMmBKjKp9xbFe9KGScqkIA80Q9XqA4v-xhtbbDWo4r6VMNVQwN7Iv8HDvTjWsFh5ZMU7pvAXuiD3vc0A1Hmoq-mo77LcYHTKms8APIrohBqdw1i56s0_nt2TrHHswRNFAQXzbjOwlCiI7fBlSWIA9nhYMitX3RAZ-TxsQh5ooVA9gL9WkkH84W1EET4GFYRDSIQ08kj58JYbvJFvmgjmi3FWRRqBFnKUYJz5zABtX5PlZgK6lF-RINu6Pj8wxPnbI-sMITCcVNdTfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK_V8DhIw81KA2dMkL1d5GNxNo2oeZVd_lCEdzz5zV-Y4GBlWrYYpCG9G-qIUPNHUCNiI79xcJ6uwVk8CmZpzjijYM9HXxOqgyu-9QCe02NI69hwVUczVGgKFBox_XKJDtXUqzOFA1MhLItR0a0STnc7q5iH75Dnfr_jWdlOe8nyow6_opJGpll1NiBnVeWsX4rGYBRNkQN3tPbXezoLgXEbMYOAgJKHi15776cPdJI1jlfk00vB_EIjDeosc7cf2oE0EfEEjVmlfL9WAqRKQHZQOIWMGxq3x6h0v1AqR1XX05OeNzls1NkRG3AF3WO0jqyztPaEqWmBPdZZY1M4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Z825m2rksLlDcQsWT2Bo350cSmgyMjWatelXdfVWGxVbjmKckC4Swro32rN2dt1T0YoyLZjkLk04sWg2a7vqkwL2OhXeXNcQF1tvUmatvP9RUAkvCiLmHyziti48ElEFsjT7dY_NPeIZH5w37Vag-OSVBMcYJb1TDimlKs2NtO4Hsaypy8vQFBmSny_CpFHZ_b8-TCiGcWs0EpDEdvJEFufRnE1fIDF0Sbtt-xjOPCHZPNTf0D0eE0FoQBc1Eb3-B1pq3PnqMMEdnveJsvPipGLBa9GaRHHy-Ctewn9-2uZLuoxnq7IQckcCSaGpPGIFDlQxAhGNrqk9IVNyBaZSew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=Z825m2rksLlDcQsWT2Bo350cSmgyMjWatelXdfVWGxVbjmKckC4Swro32rN2dt1T0YoyLZjkLk04sWg2a7vqkwL2OhXeXNcQF1tvUmatvP9RUAkvCiLmHyziti48ElEFsjT7dY_NPeIZH5w37Vag-OSVBMcYJb1TDimlKs2NtO4Hsaypy8vQFBmSny_CpFHZ_b8-TCiGcWs0EpDEdvJEFufRnE1fIDF0Sbtt-xjOPCHZPNTf0D0eE0FoQBc1Eb3-B1pq3PnqMMEdnveJsvPipGLBa9GaRHHy-Ctewn9-2uZLuoxnq7IQckcCSaGpPGIFDlQxAhGNrqk9IVNyBaZSew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3IKQERhsG7VdC6ftJzmLlf2h10hxmo_eh0ioru2N9AE0C8ctziDJkAsQFdtqqI-c659QBnfUJcOV2X45-SdKWqhgNvt4FfdDH0t4Mt9guR5VEquJQNhTruwrGsB3qIYRfWJB6L7xwXD65ygW-kVovpj8RkjjXPwxC1x4ZHgej1itJ8vt3VyxyZznCnLYXe11FeeS0rTcrSLYz4I6BRG8P-EjIomGrAmJzQ7ljo2gQ9TBT65_zCQpzS27nCxBHOQk4Z17DemLbmqctmw5DuIuxzwbyLdF0lNH0d92LWxotrBo5IWLhOBAYLwgrQLYMp_Pvg1qN5oVtkZo66N1lHWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVYXugFtvMzfIPUwtxZQo25zoBl_DAKZocekRgQ237JTPGTNs4sjmBl6CGnM5OEYJYjssfKP2Xk6zx1ZIdT46H73UDf2GCf7DpijthVXpJ72ShPq_773VPfXHwetqGtmHTSyErN9dcivHVf60OkK0ZHqcAZUCKc6DSIzjmWXxO6D0FpHBmBKtLrRorX7TieWyyhg-oz1ebspbvx2OU9FHPP9uX4-tAPSIm0fyfi7pnaSqUXyiHotWzLrxku_dTfO1NARKgjCyS59RVu_r84C9R9IirESRzuYtUyXrtShmgKk9SdEjYBs5NQLAWhQ_ZAIpZoC0mYxS-GbQiAC2ompVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=rpz_JH0tmpNp4HLZHF5mBcyGwlQezZCfHVpL8CThSTdwzT1rV07NZsyNrm4fewNYR-MtLcMPMAvKQdfY43w8h4DTS3158Mi_RmPXyGvAkNmTmOzCsdIBiFQdtO2w5PpR6_jrwqOiKEi0bCL2qR5CxTnGA5NzVvBBUS3RsJn9S4kX_7noExrccU2HD8OFybtRgzxuss1ntv7cE3hHzbu10d1Qbm39zUWSMyN8_PD2BRAn1Z-0ifU9YisZmVmga_qyeRPPSjeQtK19taChNscHn-hg9Pa7mqXzZKy949gIGDTsWsx-GNo1A22g6gkjFwUqqrfaDXCdiJ6GrDw9AtgSBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=rpz_JH0tmpNp4HLZHF5mBcyGwlQezZCfHVpL8CThSTdwzT1rV07NZsyNrm4fewNYR-MtLcMPMAvKQdfY43w8h4DTS3158Mi_RmPXyGvAkNmTmOzCsdIBiFQdtO2w5PpR6_jrwqOiKEi0bCL2qR5CxTnGA5NzVvBBUS3RsJn9S4kX_7noExrccU2HD8OFybtRgzxuss1ntv7cE3hHzbu10d1Qbm39zUWSMyN8_PD2BRAn1Z-0ifU9YisZmVmga_qyeRPPSjeQtK19taChNscHn-hg9Pa7mqXzZKy949gIGDTsWsx-GNo1A22g6gkjFwUqqrfaDXCdiJ6GrDw9AtgSBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrXHKdiqJHu9igPCZ4vuqt17U6RUAy5X5YvuqxeEm6mtugMG2crSRe6B3Yke87OV2UQBQNKI5EpYqA1b7JbdQOzgZaJjf1eHDAjisHMnH5sbA13_X2qjfwyMoFO7Mv7I7shFT43lEHAftwMCxiqEKWITrOVsq6vzCT2jUuXLHaTz-2UiZK62eF8d9ixo_sD3nTW4oPVRRIyrAX5u17ZMGOZqXIAvQYV9yckmmbFN5S5LjARwyRGvUDcbyNN-6UOIlg6BZWZLyHBAH9pg7MTwyl1l8KX61AG4cfApKSlLnhGPV1GEAhZNYN-T_-d2mGNmhdOOgLhDQIuVT_kassYEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp0a5WGjzl_ZrdiMzt4Nevuceuxjy298ccOkJ_9YTEr26NT5-Sv_cbKfFUAY4CY25cz4ZBmmM0_lHmwAWVCU15ajYyzl-u7TsXjR1RvYcbTtve7L8zjGPquKnFW2elMmqYDubGBZUtTyvh-sC59KCXwxc3uw479wYjkqAaU5SAiHzkfzr_7je_IqfugDw9tyPghi1owxvLvXWrNfZuk9mNyBp5FTpY_1Y0C-wY3Ji6n07wGgXqEqKZGzB6j3aG8vtTH4uo0Ru9fY_hdp036BP65vKY0_yG7lioG9valedo3wnzcB4aCTVmMsTc_XiyaF2JM0jiiojd0Rp56NrhkdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKcgyjrpiAHGWhOBwZ4xAYUNUGHa4LdWRKbPjStQQ7OLkCWd6zhCHuHK_z6eDSIwQXy1eNvaHxOSvocsLs2aVcYa8jLZwjDlN0a-D7tm3JVipggaRqwedTNtGVaQVgCBLSk5u7LQCN6orvSyrX8VYkDUOEzIgLY_SplruTkILzZtne0UWPBD1SgZ8B_c9LwNxKOSzW3hhHH3w0kqiW2z2FnBI2fzt44b9fpDqCMa81B0rAJL_TJtDQwY3SREcBm9tUjLCT8Qvfqvcy9vXRzdbsl6LIaKOiTDK4O9wHNhZapbC_Sx64fLHW3Ezu7HNBnkxQXngSwUtHqmrcjdmYs1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5P93ufSJf1imrjw_-_CC0Wrg4SjnOeo0TQa93abdyaq7-7yLTyo0PmsIhMwknTSMZOup-U9quGiTgtSoS5OVpU8LbPNb-kohNky4Ojq0_i1Qe2L-81UGbLy0Tq2zW7kUawmBBa3OBMvLrJOWO1W77Jl5vd7bXhDoxLcL8PdzQAJq_VAZdRFzypUzNEbQHyLdzCmwlY8DO1y_HJTWHp0VMu99ZgvIP6do0zWtaY5_O27-xFbUyvr1d3wweAi78DVPjaoBdcUbJ78rpO047xCCcsolO2pR2QwinKq13uInT9ksnYypsczgJD1vrVrKM1BdWe5YW69lsPztPcUdh-KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lftGtp0a-Z9DqqPNsPrG_0khdd9uwWZ6P-YYYPC279QJ-L9pY_SuCjek1dDEoc9c5gLUjreYipiMby8I9sD-GROIArXm_1jLjwKUTBtbDHzbNxOq1sxkOYiSxrQkRcmovzhYtPFRfJs_R-wpQ6Dq-Jz0iJKRlPd1tw6Gl-JxopgZjF2gLgdZs4QnO8v32iuNQs9b8NwpSJDLwqAXRyd7rPuGh6Hihn79rjEldHWxlAFm_tQu5Z_AJrb_BBUndNf_rDOpcjXXW93hwQusTkvOi8HXMlhixqVZwYH5uNHkf_XsPdcIzXa8lh4Pqogoug891wZlhR51RcgAL5tYC2NzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=DcKBPgd5YOOOBOEzibPPFS_ig7A9QRrOzu7LUYBFwe60u5PoxZKOA-D-aJ2d4nG8c4qVo5XK9ZHDCG3MiLN5V8PPD_c5ltEKnwqV5x2HyPt-b7gdB0XW15wzhxRzBHJGR1wY2lT_d2WD4y3UtX1oEcwF9ywp9TFL9R6XE_Zcvhe7o2H1_HRooElrTrXge1w99CwihZKzg3sahcj6vc_3VSzua-85YLBMpWLIFF07-q1O-R0Z9MLNxEbOiSeCBqOFevtk7uUiID8hFAN6gpSlCyDAEpQ_L3u--HOfxvg9NER0vDboYu6Ctzc-gFHJqsKODySYkANsAiOQLsA4hml2Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=DcKBPgd5YOOOBOEzibPPFS_ig7A9QRrOzu7LUYBFwe60u5PoxZKOA-D-aJ2d4nG8c4qVo5XK9ZHDCG3MiLN5V8PPD_c5ltEKnwqV5x2HyPt-b7gdB0XW15wzhxRzBHJGR1wY2lT_d2WD4y3UtX1oEcwF9ywp9TFL9R6XE_Zcvhe7o2H1_HRooElrTrXge1w99CwihZKzg3sahcj6vc_3VSzua-85YLBMpWLIFF07-q1O-R0Z9MLNxEbOiSeCBqOFevtk7uUiID8hFAN6gpSlCyDAEpQ_L3u--HOfxvg9NER0vDboYu6Ctzc-gFHJqsKODySYkANsAiOQLsA4hml2Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ozim1CdjFR_TUyOzmf3db6pFdYaU-MIVPhsLvhpjzi0byMjP7eFYVnNg5zDqp_m3oudVBgXMe9Mev-617X76iv1Fc-52soz-BM3-xOO5T-vSYLwBYypGH1GSAAgE_xSOEurip0p7RHyZT0ZbO6RyX2N_WVex_tkij7LzkTW3MIHngbhuSTyDzrYh3OADV6zrgLhEmoTdVcziIaIzVQTl2YB8rjPK-fTLF4_0UXOeePpkvgEN1XBNaWnPMPuAEWWAQBJw3B2RIu6WYYdNAw-iSQDLInW0gkNYR128KAXtCppsGgATKvTZB-TZS2uBbqw6d6RmivCq7dS-P8CYRMHJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=Ozim1CdjFR_TUyOzmf3db6pFdYaU-MIVPhsLvhpjzi0byMjP7eFYVnNg5zDqp_m3oudVBgXMe9Mev-617X76iv1Fc-52soz-BM3-xOO5T-vSYLwBYypGH1GSAAgE_xSOEurip0p7RHyZT0ZbO6RyX2N_WVex_tkij7LzkTW3MIHngbhuSTyDzrYh3OADV6zrgLhEmoTdVcziIaIzVQTl2YB8rjPK-fTLF4_0UXOeePpkvgEN1XBNaWnPMPuAEWWAQBJw3B2RIu6WYYdNAw-iSQDLInW0gkNYR128KAXtCppsGgATKvTZB-TZS2uBbqw6d6RmivCq7dS-P8CYRMHJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=CS8FnFxQ4jCBEfr7f_g2bN9uq8DYE8bOYDOBgBZEvWrTGpQtfpWUCDwQlzB8uVfoNqQiw8JqqgLrkr9F4-3VVkugGpPJEm-a8FOwJ0pwR2EiVI1ThhTCb86Ak78N9-Nm9Py9IfKRiT-tEmiXNVpQfs7AmlzQva_H0V7hTGmj8Z2Ps9CbggCpG1au2YK9aHuYzy3yetJn_pGmGyPZP5YvDn_t09DdFD-uWI9bon7SvnGDi21dai1jY9TVGQduh7gHuP7Q_0qqd527y3kNxm-gKgo20f-10WECttLEkBgakAPFgPt8c4YRqERmNQAjk2JBnFH2P4P_HrjVHf7rGsujgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=CS8FnFxQ4jCBEfr7f_g2bN9uq8DYE8bOYDOBgBZEvWrTGpQtfpWUCDwQlzB8uVfoNqQiw8JqqgLrkr9F4-3VVkugGpPJEm-a8FOwJ0pwR2EiVI1ThhTCb86Ak78N9-Nm9Py9IfKRiT-tEmiXNVpQfs7AmlzQva_H0V7hTGmj8Z2Ps9CbggCpG1au2YK9aHuYzy3yetJn_pGmGyPZP5YvDn_t09DdFD-uWI9bon7SvnGDi21dai1jY9TVGQduh7gHuP7Q_0qqd527y3kNxm-gKgo20f-10WECttLEkBgakAPFgPt8c4YRqERmNQAjk2JBnFH2P4P_HrjVHf7rGsujgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=UPQSlQch0xS6baieGXWPbco5vCPeVPhr8mZMndCkS2_yY4hyB-3glETcT1Ng43ZhWIP3_rI_uA4d0hcjvVNmbw7_1TsgDoj_AL67tbfG9QlEYdq6deDpFjwyJUdU8DUVOGHOdM7uwLNouCJgzF4Vvq-zeM5RChev7ZizXptPCEdyDG2ISoy48kPzQwnfOM1RtSM_lCMgNIPBSAUBGq8NYCGYHmldI1VtIkA4p0VJI0PNpABOlIr-UZ7lPEn9ppWrG-xDU617y9Eemw1RtpgLTzXAQQMV9wc7ahoxiPQpeWMsmEhPs-2HqCFQEBGdxywGfJz5c4pTdAE05XWiB0K3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=UPQSlQch0xS6baieGXWPbco5vCPeVPhr8mZMndCkS2_yY4hyB-3glETcT1Ng43ZhWIP3_rI_uA4d0hcjvVNmbw7_1TsgDoj_AL67tbfG9QlEYdq6deDpFjwyJUdU8DUVOGHOdM7uwLNouCJgzF4Vvq-zeM5RChev7ZizXptPCEdyDG2ISoy48kPzQwnfOM1RtSM_lCMgNIPBSAUBGq8NYCGYHmldI1VtIkA4p0VJI0PNpABOlIr-UZ7lPEn9ppWrG-xDU617y9Eemw1RtpgLTzXAQQMV9wc7ahoxiPQpeWMsmEhPs-2HqCFQEBGdxywGfJz5c4pTdAE05XWiB0K3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ3Qbf8e3H57JTstPHNAy4IDnZsvKH3NdetRq90PaNe_e7x4S9tOMWZA6rbN_XF9anFFc8FFNtS4gqcrGYHb6gnfS3U8tvDCUbu-RpmMoKXFhupMnLmOaIBd0IqotwQetGO0XYEGHtBXw3258PMQYYlF8gqKp8pmLtHTGvWapIKF6CVD78YjqeK9M6NQdTIq1bSSlkHz9_KSLRVuP-OHSpY_jUF1yR0qDpJgfYXPaMu9y_ApY-VN3f2GaOObagNRdmsLY8aN1LwwoJ1JN5Zk63rI7QeDecHzy4SDTenzkINayqNPOHyDxdKc-dbqfzDHH5xU21Q4FheDtL_dyjAVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnGac9ofGLK9bVSu5QcfYtngJYh2jTvWMTPtD4ErnWRrEMJ6SWjxZRjQW0zfn05mvsRRzTZ1ykPgufgLMGCE5KcEIwnnFcZmMwPvZTnfmQXq_LifihUg9IaX5yzJrguDgTQW31lYodULXkL5G4vpksGTI5Fl_hvrscpjgmHf2djSds8lcUPOkNcVcubKkoo4kKY6T5yVvbibEfomVH9-H4i_dONYW2WUtrH-isd5rqTtYxE2ifNGEIOApCWIUOcVBErjyVjFnyGU9DCrHAr1nSfTPM4P1PVD2kEGccF5OySSGy6BjuFgqk-wDRCEc1fd2LMw6HBpNWkOdicPYkorgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Fywf1andvyEwppMbXjAcXOp3txHronpvS4m973lDNwqcbiP8BriUNBvwk_CevZ8EPmvfZgXfx2EEdPXNEAQBPJy6LjkRHPOjegyPbcTOCCX8K7H12pQllaW3WcJwCsKbN5AhJDMO9LRcjmUKgkvPshLrq93fKKy4yDmRoMkgBagEp24nHLwHlQJRkeusTNM-STX1NF52q03Zf9JAP7LPbWg789yGNFnve0ZvaKBSeAsNV5B3GRX9H2X2Q_LPz7lV2x3vB6grxesSmGWMqBkdYS13ZP7OLJV2-bhf-Icq0eQ7UxT7hdQe0p2Q0E0Frt3O7PNV4xt9Deoil9TSx2N7uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=Fywf1andvyEwppMbXjAcXOp3txHronpvS4m973lDNwqcbiP8BriUNBvwk_CevZ8EPmvfZgXfx2EEdPXNEAQBPJy6LjkRHPOjegyPbcTOCCX8K7H12pQllaW3WcJwCsKbN5AhJDMO9LRcjmUKgkvPshLrq93fKKy4yDmRoMkgBagEp24nHLwHlQJRkeusTNM-STX1NF52q03Zf9JAP7LPbWg789yGNFnve0ZvaKBSeAsNV5B3GRX9H2X2Q_LPz7lV2x3vB6grxesSmGWMqBkdYS13ZP7OLJV2-bhf-Icq0eQ7UxT7hdQe0p2Q0E0Frt3O7PNV4xt9Deoil9TSx2N7uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCDbLRJzwEIEy2iF84-72LdW5oA_68f1xxtUJycGJTSIJLdymCzmbbW51mvpe003k1R-qtVift9ANZYUOV8DeGHYH20HVHnmSFgRm8WYPxuyQcabEiyqQtsceDlzm6RXZ7tZk7qqljcNVQkOyrX5LK3Cnlwn0caC_TqiCUby1u3U4P-5rAAD7s97gvChTPU10Dgjsh6VXm2tFpvA5hj3oSHeMmyDolINPM0UhuqCn8VzQnfCDKNu8uqnB7inaDr_99G3HavD3CiNTX6k6aYHS4spDe6hyrX0XTm0VtZJYlBz7ktrryIUX-NN1CAfVWw871FIT59f2x8CNnxI-PVIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=HdHj977Wpha2UOieaOYU-eP8Z80fV7u9VIOzFLU86Ps1VO9E6qDdABf5uZJazRgIsvVpKyQsTqyeXPS-HTW_F5DiD9F2vgHD4WmRUxZ9GebIKg7HpbjVPp4idYHFexerYVd59d22CN3diAIK5m_eXAGXKSBVsSyb7Y-brinIfe4qBtmHSvok9Lj_C4pexmtODV7YFT5S7TaewRBXqiE4HSByhjqazBGjziPwZU2LQbIbxyJSllDBXAKnA8nYdW0TmKYCt2sEQUm1EeTDTR5suchCHOsTFQrvwy2ap48GFNN1HTo-6bxcaG7zijiMhKks-Hfg3bHa5m4OsLeEPVltSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=HdHj977Wpha2UOieaOYU-eP8Z80fV7u9VIOzFLU86Ps1VO9E6qDdABf5uZJazRgIsvVpKyQsTqyeXPS-HTW_F5DiD9F2vgHD4WmRUxZ9GebIKg7HpbjVPp4idYHFexerYVd59d22CN3diAIK5m_eXAGXKSBVsSyb7Y-brinIfe4qBtmHSvok9Lj_C4pexmtODV7YFT5S7TaewRBXqiE4HSByhjqazBGjziPwZU2LQbIbxyJSllDBXAKnA8nYdW0TmKYCt2sEQUm1EeTDTR5suchCHOsTFQrvwy2ap48GFNN1HTo-6bxcaG7zijiMhKks-Hfg3bHa5m4OsLeEPVltSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeWSKsR_QqwmeDKcoNObzCS6Jn9NBwWeY4q_Mo6ph_Nz9_ii-nhUaethE4afp4wFuiTuAQFdyEJpEe-E4lYSscE6HYGoJSMGL-3fd21hboD92nlmBdA8x9jRkoTrJlFNrbpXsguW_fizaPFc44TNsn1o0PwulhIWzWZF7RMM_ei-ZMl0ZknJhSj5VmvwrTTcDs5FmjrxEBNkwvtS25TMBVzO28cwRf0srzUp9OD8_2inY0rrFA3Puq4goPv5BvAxMpQ3bdbpeT1MW5Rct9Pij9We20PrN-lgWL04TFAr8si1RYAmY0XGU8ksRabUTXp1CZOrvFzXFSaATPahHcFgyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxyfNgmSjcxqexSthTL35KIscAqtoNI4_tP8kxScitXrjGPRdU541_mc9DBwAnAOMPqhsKjznDvpYG6tgB_gLb9DFF6uryQ0De-B2ctEyje4SxSI-nrcSjaZW3KyQUJi3njB3Ub3me0cwAyxo1LHXldo5opIuJL9XJ7p53wvsSIqI2RJ-Tlt3hR-qr2wdIaPoUAj6qeI8eET2AJpHmNKvOoeWn6tvsCz6-IlOfdpucPLwKAQC-cQkR4AWixpLFoLyQgdTLALKnG6sSR-sMGnekmNq_QblTxfm0g5JHwiU5zgoF3G8XPqaZpXb7KRFWz1K1a2VcJ9iBscNNHLVWkW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=HPiZO822fJGeSqf65Qw1v86oCpioO45fvIcQdktkz-OV99BKYSG-lS4yIorWNmP2nqIyT7HZ9moR0k1qlegfpEs_cZ2D_KmJoCtQNu-nuLefEUlEhEx19lEKTLluQqi92AUWKiU1AM7xTp-ORLzLZ_yTClshvkZrkwWJAieIRyMo5O6h3trF98w7xnYWZkoa25zZLDl8vjV4wEvXDo9FkAh90n8S_YdNxu8bZp-udfEL9RURCbnOpkyjQHF90wNAgIfJsHUmVwoV2U8ljOvhHY29-7zFDzGqh4AcSNsmHsFHzdKIXuI2d5qGv7cn0iORda36-PQ7sAIJsFi59-oZZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=HPiZO822fJGeSqf65Qw1v86oCpioO45fvIcQdktkz-OV99BKYSG-lS4yIorWNmP2nqIyT7HZ9moR0k1qlegfpEs_cZ2D_KmJoCtQNu-nuLefEUlEhEx19lEKTLluQqi92AUWKiU1AM7xTp-ORLzLZ_yTClshvkZrkwWJAieIRyMo5O6h3trF98w7xnYWZkoa25zZLDl8vjV4wEvXDo9FkAh90n8S_YdNxu8bZp-udfEL9RURCbnOpkyjQHF90wNAgIfJsHUmVwoV2U8ljOvhHY29-7zFDzGqh4AcSNsmHsFHzdKIXuI2d5qGv7cn0iORda36-PQ7sAIJsFi59-oZZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=b3BA5mz2NdF1_psbqtMhY9gDycwnM-4zytCN3L7EDYbBTGV0-TtU4ge6Ifu3acJ2dGteHT0L4Qu4liMIYAw7nwvcpaZXvxj6kNfIjmuVgQVhYyJDaHZgpeZFBwHuUxQruKtXD0OVlNIZoeBmzYrcfoT7g15a6VyvwBVA8Te6K9-7ACI-ElwMxiqL0U9PGPHc68_T1cS0bOOMm0LobAABn6YyvoofrNXz7RaAPy2av1_qV2RoqeW8c0V26hxo_806achre-2V77l6omJgZLdOg4l8_Qdpm6nMJ3QiWn_WdEeReM4kseOiXcbGMPrbb1nk7O6hWXDhfpYP30cwT97VYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=b3BA5mz2NdF1_psbqtMhY9gDycwnM-4zytCN3L7EDYbBTGV0-TtU4ge6Ifu3acJ2dGteHT0L4Qu4liMIYAw7nwvcpaZXvxj6kNfIjmuVgQVhYyJDaHZgpeZFBwHuUxQruKtXD0OVlNIZoeBmzYrcfoT7g15a6VyvwBVA8Te6K9-7ACI-ElwMxiqL0U9PGPHc68_T1cS0bOOMm0LobAABn6YyvoofrNXz7RaAPy2av1_qV2RoqeW8c0V26hxo_806achre-2V77l6omJgZLdOg4l8_Qdpm6nMJ3QiWn_WdEeReM4kseOiXcbGMPrbb1nk7O6hWXDhfpYP30cwT97VYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpOaoC19o3XNw2GcKuL1GO512UvPgXpECjWvQT5NsiubZN7CL6dDsmLYjp_sPCxFOBhSK0NQr7weAp-mgFGZ-bD4U73lzJsJcZL56bVFhusrrnI0Umtc6VJ4mt02fmjtk3ab-PfVRqRDMjt9HmdYHvoWur6RO1_RbDH8icIZkHPV2gXLAvBzO_19q-5nNVUg3g0bL-kS0HQp5oz5L2Rh65j0CJf3QZ7gEt3ag5-dqRvVB6DQNo59IlqTe_3dlYl0eoAEoFbdw3wYLDlEHx9nfCtl4a1FPwTBM9Iegrb669RSeIWs51trS3En4sVoOUqoiVu2cGYr6HMlA3K7Dtwqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxupCHvpMp4dHFrn_DqgCrssEb6V7vMqjnQHSN3snsscCp7lM1-21LJ-vm62v37Yt-LVPreCEOORDXbaxwxYJru1_hC2liVzaFjy4zUlWfqZG6sclFiTbYvLqiSSxILUZuQ95sXQO571mD1VabBEruoOuQviXkusKmymhPknKhz2e9rDO8Cwdwtln-2qkeSS0OKJaNsNd3KblR_y3i0hxqOu-2TqlXKy4_3THBBf9vOz1tFyIU-XzIA8cA3_RBKucOU75UiuPeysU9-i4RYZOhfL_XqFeF16M3vcLMVIwqM0A1A_iuP6y-zK6fd7Nqe-eCcjNmwihbcTi9mzTKgsUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANAtx5QpW1FzA2MknC8AggqO4-nq7P03VNZYhE2y1h4W8TThA3dm9_yqCT22I1fB8pK0QeGTWl7m5asZAygrn5N-_4Oy_sBUi6DPiCjNCrU18RB_F4LcLlNlZ7clVQcDdxcaBb1rOwAwmKzl_hQYJIVr7dsbzUzDFAIMQeJmwaJhbePyfH2bWs0RaIOjhz0L0ZLXApot6fstf6CpayAtTC3fvjfYaV7Ry3GeO0tUTSo1qR44HJEQ618HGfgWuTaQmtQeTsZUMWRXAexlRskX3t-GYdxd23MelFL_LLtHyM1-frzki2V7VrGvN97QVFRZ6CFQZoCN6gGQ8yQEIVo1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=pQvm9wP3t-kAAofpoaEmu26kJiFk7HWPliaSTHrX6zW0vgD5paJTyIVforIf4feq0tl-fUVO-IabUs_sUJExLxspag_M4P1QGljhOt_wPwhfQPdPTvbe1vRaKhvd_f0wFquxfhppAr8NS9S6xGbJCD9e-R1wrW-p4x5IPsmg7DU69GQ7FFKu6jxiQ5PQtobQ5MggKfKRxcE_JzJ6mtU14jD1z3Bh7swXeiS33Ud7PKFE916aXPtmiWgaCOxR-E37kY8yYjtfUV4VDgdBOVgNrE047n9mAzq9bz3fPcxQpvBg47DcIlcaFxdA9CqA9UTIv3KtgQRlDTfmBNjP0Ba4fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=pQvm9wP3t-kAAofpoaEmu26kJiFk7HWPliaSTHrX6zW0vgD5paJTyIVforIf4feq0tl-fUVO-IabUs_sUJExLxspag_M4P1QGljhOt_wPwhfQPdPTvbe1vRaKhvd_f0wFquxfhppAr8NS9S6xGbJCD9e-R1wrW-p4x5IPsmg7DU69GQ7FFKu6jxiQ5PQtobQ5MggKfKRxcE_JzJ6mtU14jD1z3Bh7swXeiS33Ud7PKFE916aXPtmiWgaCOxR-E37kY8yYjtfUV4VDgdBOVgNrE047n9mAzq9bz3fPcxQpvBg47DcIlcaFxdA9CqA9UTIv3KtgQRlDTfmBNjP0Ba4fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olj5eO5FCzsfbsHasShdJkWbeMHdyljW2j01Noy_YYbQPY4gaE6qg6mpfZs8xL8tVEEoco27p8tlgSuS4XbHiAcbgmdLAdbTN3PvWwxbvkpG8yqaupodlRqdubGoKDRP64kgSybIAUTJPHBaM9nnHnYtTcaLcJknkboLMkrsIW5U_zyWj3h8akaC9bOXUiTy7dIqrVO5ISuD5ksBGojqYg1iQbN5S9xuWaZtHnvbCKW2ocvLRmD-k8lrMTGm4ldU2XlMxd7NWUPm8n4nHmj0J3JABGsM1CQM2h5hQhibqRIlGYJRHzqhiam-rF_3p9eMYbvNfIK46b5I3wg7l56-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qi-AVkmQTns7JatIp77uBEfCy2t4x25oTbv2BQHKQn1SVqHKEkCXZQ3-hTW1udt9nyZjFmccO9ZK756Y9E8surWhaqlnWKSe4eMiJhugoCJo_MgfZN_x5CmKalV6SR9l7Cg4ZsekXgFvMz_-k8ab7sOHbRl0EPDF4v8ZSDoTfIFMPr5wEyUja6fhFcE14iFnGS5NKICKp5Boj9e0bi37KwepkeLSjhwBJlvLPBXvxYV5mkSslsQ4Fu7qwOB2kbKfj0ONmCD5mwxtd5CEvxmQgyq308hwyQBAkTgil-44hMedxI5YQIkx8QT9VztzkKyWiYqLlIr3YfBEfzR1Hya9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeOG46bnL8LAwAFm2ClTFv-Hga_c1zjJSYxHq7GRCl4x-ViSlaOt3gjEECVJHOOOosXaRIbt74ayum-7EQcpYDzBpNGGOJVr_M_1aDV0Q0mVuDZHp4UT3UlLsWPO2pncMiA_K0z8mi5UojbV7sgKrjspiSlUoX_Oma_xdYuu_czPPRqbp7gOuH5TQ-UXyhREQ51o4VxIBxuO6IWL0YRBDYAHRyj-WT2ibO7NEfkGWTY2H3HA6OoCCuLvT8wuVW0-O1hSCO_Ch08QpKRqqFwcztjeOTSpnaCGYu6iHNfHS88H2zCVGWg6y3n7aWARxbsuYaKaHlntJgHIGC_64F-fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETGk6Y3Z0aPXJscVkhPWp0ZCYw1aXICDPsV3YQwaswA8N0K32U7L4yU6SDfTZaNLAQN19scCrJ3i-u5u7bKCD2dM0zd7DJ3XdqDt0NEJuH3KoEcBy6DGtKzMuP2yUMUIMNW9X2pAlmFiCuoxQ9ZfHcMbNqbAZCg3MNFs1IhFpBMZYlXJd8fRYZXRFC3heLcoELI4-0EXG4RFV2OgihnlD0JS6FlrhF30oVrpoH5A1Rz2KDmsZjrTIkBfYiP6jqDRUcJ6pcZa8gb0i_4slOxK8RPDSn6PXEiVw0s8F0g6JjOdaJglVgHNu-DCyOdICwwDUi2SGVZydD6hWPmOPPQzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=aPdHQm4ck-pxiP-lEhLeruUAqdR7evDX2AGsnhX_cFtqfSsCQNwZBee_4AOns-BRxz5Kw6-y5Zqo1pFlGaMe2lMPqNRmIEYE8MjRvo9Ecz72MngkXF0mOluSF8636SlWRYRG7jHNJbGuOEZma8lI-z2-5TAdGgw4-Dvqkad1IvTobRu-nkCymmjbERvtaEtU-jLWWCfSQ5XQXEazU_l5phlIoxdVO0_MG_NxPldo6I0BetSsyF4dHFR-4k6VMinTbulLF9gedKX87bEfJDy8mptXNF8JC0Ob7KT9Fx4c3QLZKuZ2vyb4H3VXLa6cUq4ck-pbE6lhHgtX8lLK7Ai9AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=aPdHQm4ck-pxiP-lEhLeruUAqdR7evDX2AGsnhX_cFtqfSsCQNwZBee_4AOns-BRxz5Kw6-y5Zqo1pFlGaMe2lMPqNRmIEYE8MjRvo9Ecz72MngkXF0mOluSF8636SlWRYRG7jHNJbGuOEZma8lI-z2-5TAdGgw4-Dvqkad1IvTobRu-nkCymmjbERvtaEtU-jLWWCfSQ5XQXEazU_l5phlIoxdVO0_MG_NxPldo6I0BetSsyF4dHFR-4k6VMinTbulLF9gedKX87bEfJDy8mptXNF8JC0Ob7KT9Fx4c3QLZKuZ2vyb4H3VXLa6cUq4ck-pbE6lhHgtX8lLK7Ai9AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5zbeRDKK1aazUdTOKrbupsKCwNIq_CvuOwnaum7RD-gRwjnvmodY6WRylnWJHy4w2efxbRTe-Z_RSVHBnciIP8AEzEr0gg4gybV_IS4mP1uTInjFUzNm6OCmRJu9u4v-tIqIy1a-t-zXtaObJieAeUpFsc5g-xfGNBUQCl2nGvF0tsWpFAc1MOliHtaFwTdGPNzifcSgd3TsErrQ5rPs2WVBBzk2Yixj4KETT-7Ee6q6f71fzxqwEBwxx0qRP92BAk4nhNy-jFNm9WLOGC7IXr6HYF6xZaWTxyt-YsCiK5I91nM_E_a9DymK1g8Zf8Z5gIck--NK_dfrLSVxLX4WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=CmWqHrpS6pWBn08MiciW6eEDlvJAgtDe1cbq-76o1pMj85iL5BI3NvEbfKY3MlciKZOAoQDpx9oYCPkuAoZYNXLXzjPy-Z34o57vXNpzc6eEoiB1ZIKlnPbX7HgvMUicvheXBIg4whv003EhIpnLnZUl6_4USjgAonGuK8UUsN2juW0u_x1fmldr3UjcaYg6hS7n17aIUztwJ_sjpcNgmPpSY8KtmF2MbeimhQTjKsyPAMHFZMVmGdemOgpZMRktoGpPMRQns36fliUM2gwcDnQfUbEalSJ_21UDxFgwOR864sd0HG0xzfE0cwH_sBl1UssFhSm3nfqnqMjCeSaqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=CmWqHrpS6pWBn08MiciW6eEDlvJAgtDe1cbq-76o1pMj85iL5BI3NvEbfKY3MlciKZOAoQDpx9oYCPkuAoZYNXLXzjPy-Z34o57vXNpzc6eEoiB1ZIKlnPbX7HgvMUicvheXBIg4whv003EhIpnLnZUl6_4USjgAonGuK8UUsN2juW0u_x1fmldr3UjcaYg6hS7n17aIUztwJ_sjpcNgmPpSY8KtmF2MbeimhQTjKsyPAMHFZMVmGdemOgpZMRktoGpPMRQns36fliUM2gwcDnQfUbEalSJ_21UDxFgwOR864sd0HG0xzfE0cwH_sBl1UssFhSm3nfqnqMjCeSaqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=YQAcC5zGW5TurVrp6qpcIkyf6igh6P3-OAEll9psQqAJpTo6jJ_OQTCKq1rmaczjbGAOi3neXlw5uuxjRt2n9Y9W-PLCsS_c-dNC7-BcPELz-Xhwek6LKRyoNnB1tMnLtFyCqMQx-Sz_dwyhR9NArb-94ezSXy2shgYBHn8WKUbA3ywFp3Qxf7CFZ1xIcS7cS2bFbztH9aLZqux_YzMG4jmPwek4ELLeSohyCTodHvruE5pEX3RT0arDE5wEHN2QAhorueoIiOX4ihfxqVUNbo9Llstpq9djYxNY7Y8z_esrtRZ55tJua1uUXuSl5moaOnNVAw6y3Dd4BxTaPjBe-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=YQAcC5zGW5TurVrp6qpcIkyf6igh6P3-OAEll9psQqAJpTo6jJ_OQTCKq1rmaczjbGAOi3neXlw5uuxjRt2n9Y9W-PLCsS_c-dNC7-BcPELz-Xhwek6LKRyoNnB1tMnLtFyCqMQx-Sz_dwyhR9NArb-94ezSXy2shgYBHn8WKUbA3ywFp3Qxf7CFZ1xIcS7cS2bFbztH9aLZqux_YzMG4jmPwek4ELLeSohyCTodHvruE5pEX3RT0arDE5wEHN2QAhorueoIiOX4ihfxqVUNbo9Llstpq9djYxNY7Y8z_esrtRZ55tJua1uUXuSl5moaOnNVAw6y3Dd4BxTaPjBe-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob2qAy_vQPGFItLQLG99qyrYw78qtuD5Hkb1dxMIxa3ExFUrXjAHrbs0BNhPpz2DMoFCY_m-lsg0mXc_7CI6eY95J4kIJ3nuCS2Z28jibHbFSn_Ggk6OIVCfPzsq9yHwsr90ywRcJwI76esnvUgw_s4fBdBf7tYXINQDjtgFUuRjUB41v63c9YkjkmujYT1wBJrfy2qbkLBa1hfWwmQo60ehP8MeCJRfSELrf0qmTPOtFpM-uqyAcuFlzpHDFZHFx1NcnQFPgAVhAAEqHspXOBHOiDgyo6RxYl6ah9VF4Wh124G9RSKevSTfIb4ahH0Nvvg0uGePXt7cJr9c4Kp90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=vfjs9-Jg9h7JxRFd5nyQIJLsaRUju3o9yXAn7B2Rum5piunJEjBTxPzOl_MgJWRdpYULN9xSPl3pCtAlK1Oe1Z0CYRLrFiHTEIU252hUAPW4r6pFFh0_NWarVQfBUxWxpiCVTsYh8kIkg_rst646dLuwmNl69h8ad6xeV9Untgl4D3slQZcyZ_zp7SbP9m4qlIjnqHt5iMZZp4npxtfAde5D4ZHPJvgE9CPDfPkpPWfjUzHpFRErSdebY5E85CHcdJPDdCeCWvVxsRE-KuLPYd0WLwT1-ugKEk6Aen1EX_y-8wQrzq4BMweOEFZfSU58CLGDwLCAoqAO90rt3ihFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=vfjs9-Jg9h7JxRFd5nyQIJLsaRUju3o9yXAn7B2Rum5piunJEjBTxPzOl_MgJWRdpYULN9xSPl3pCtAlK1Oe1Z0CYRLrFiHTEIU252hUAPW4r6pFFh0_NWarVQfBUxWxpiCVTsYh8kIkg_rst646dLuwmNl69h8ad6xeV9Untgl4D3slQZcyZ_zp7SbP9m4qlIjnqHt5iMZZp4npxtfAde5D4ZHPJvgE9CPDfPkpPWfjUzHpFRErSdebY5E85CHcdJPDdCeCWvVxsRE-KuLPYd0WLwT1-ugKEk6Aen1EX_y-8wQrzq4BMweOEFZfSU58CLGDwLCAoqAO90rt3ihFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Sb3fPAJtNrmIMivJAnBI12eoJklXKicfw9rJxrXK6L4NoveWQWSnq6dDQfJIw4ZlJ-aqVH-TivJNmK15lCl_DzhS_QjTXvQK15NawNbEoluKrToaXY2ShkfWP3PUcLOQOm5SMtbGnX9OADCAJbDClvx1XB21vfOuimL7nltIa8TtWNRRECR-Z1uGZEeiRMpJB_4HUjcxxJxGqtb4a7ZbVNha25QdMtIMmq9S6s1JdAH7Wup7_d_4Nads9i15Yk7_ZjqObZlUQw7RC-mi1rcH7TWmbDUBbUkaig3_mS8j_SwRHclPGYOmfGYle7EPQVR4OQ1_Q3fbkaZOOKOEyuiBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Sb3fPAJtNrmIMivJAnBI12eoJklXKicfw9rJxrXK6L4NoveWQWSnq6dDQfJIw4ZlJ-aqVH-TivJNmK15lCl_DzhS_QjTXvQK15NawNbEoluKrToaXY2ShkfWP3PUcLOQOm5SMtbGnX9OADCAJbDClvx1XB21vfOuimL7nltIa8TtWNRRECR-Z1uGZEeiRMpJB_4HUjcxxJxGqtb4a7ZbVNha25QdMtIMmq9S6s1JdAH7Wup7_d_4Nads9i15Yk7_ZjqObZlUQw7RC-mi1rcH7TWmbDUBbUkaig3_mS8j_SwRHclPGYOmfGYle7EPQVR4OQ1_Q3fbkaZOOKOEyuiBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLNqKur-5rWFotvSyDuuuUvZGH_7jYjuV8pA8A7CRkuoixKkCB1_Cpw-LFDJYZZYVSDDY5pjsKZuqE4ieiyEfO4Uuz1F0_Fsr_a94Qf8YG5FUSyG7OZUNS0nODHdlM3nxR3iFJIq6nkckvPEUTjt0MfTXSTKo6ZeJr2iOg2lTg7Zk6crD7fSPma5HJw8AlwuL3fVXErL9S2FMakWlOAp_bz4K_QfIjrjxtnSTjNwziFKtkWuqhka8E1CSWIm6vNi5A8ccbbE-ibGbSHDRHYYt57EgnXJtsrpbSiT4Yzpvuk6ZorNLuGGW6Ss2iTgC_u5Xix0PdnmwAkjJgPIcCkHPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZafkC9JgGyGlIL831Ou5688-dKbkxZiYK98CopR3APlHHEUpICauO2VTmGlc9q-7otrZ3wOcMXPtdaebhmDPXW9cVmUVjGDDW3KL02qSrXjiSNoCX9ZeF5B3IUkGEULKWUFpdM0r91wosyaW_q1wRrwzEom_Bp3gdZdIW0a3RHoQtIeyG6z49O_WkHbbCJ2LYCSMGU2HpUW-uQH7P_lEOuyNZFOwdV6Rzi4tTNzVXwh650-olrXP87BfQ5u0j0IIzgJFcaILP_xW1r08eMK3N5hBUfuMWaRK8VzOwtSgRcvGjZXd3PnRQyUWV1STDqCvP_fLr9VqXLR_JzL76sTtDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsl4M_bGBVzZ4fxoJ8n5mIvCLc5dRFSQqfofJGQ56yx1lSMHCdB17S10igyqeFOSE4NGWwMh-c3wBCldCei4tj0xER7WTSI7Bv9_PKQ-i5x1KqXkyfWz2mveLiZa5mV1TZmsyHvc8jra6uTLZOowbDPLVzdiLgHvqcZXSB7f1PzgxOon7fc3hDXYwlbJvqDNUNQjsyai3nYKae1hPA3ouwieaPKuA0Ifhbhv6TX7HvW7jObj_CZJQyARlThK82nSrVJ1cKD1A9BqW9t1Pf_sAsx_yHd-mcae3HRYv8mrPqqIE1Ch4rg3AmzTSKCtyIdzeSR0VyhFgAm_7ncZsT_TWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDZ-k7iIrbCzcClhX37u67JnKMlE5oKqVcBwaCEIRa_GJcJ8copAQWzx8lB8SiZ57SJeG_dXSQ7P6NaF_iRhD4fEiFC6X6_3JlQ1MriopHkauTsyZDIm3cB7qqHmDYHWBuIzXdOKM7q4XhC8KX2kKCDnmLEYhvzSx8NMBB0m3A6KJ6_vyOFFeeqv86MRhWicPecJaq4MLbhlzWcaYQwBwRjx7_j6eY1hlOcb8d0JQvpY_Cmg6su39IgAbykaudPPaQSkePnPliIPdPW9Qf9DiCB_TqlHyidMwtFlFmVTwUR-ousphWe4KZpP66paL9UvWcJ7VAi62O9-hJ-T-7NcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=Z7NeBZHenz6nYOOnRKWkevv7VVNHvDNEYmT7kMarYhKza5-m7dEB6__Gi8kGouYHRb-cY5t4WVvDhVuAlDs5EXu1iENw8Rwz4UQGQ3lsLPOv40yDMH8UzuAN3Ma_jeQpLZ7aZMuFFsyJcl4FoErOZxuCmVviJE0o_c7PjIJT1uxmplQzt8bNkXqDLpJDtbx2kuCsWa8i6jgfxCSYv0cHpTstxddCZme5qOOKFAh_bf0uiKZ-Iek4ckNLP_yTEcXld7XcvymydQy_1nMt8_-Ph3izjQHvJ0p53BYHofbA7nsLV-S9LvU5L-QYmbVeZzuCDhg9oS2T4TOz9TQ6WPoj1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=Z7NeBZHenz6nYOOnRKWkevv7VVNHvDNEYmT7kMarYhKza5-m7dEB6__Gi8kGouYHRb-cY5t4WVvDhVuAlDs5EXu1iENw8Rwz4UQGQ3lsLPOv40yDMH8UzuAN3Ma_jeQpLZ7aZMuFFsyJcl4FoErOZxuCmVviJE0o_c7PjIJT1uxmplQzt8bNkXqDLpJDtbx2kuCsWa8i6jgfxCSYv0cHpTstxddCZme5qOOKFAh_bf0uiKZ-Iek4ckNLP_yTEcXld7XcvymydQy_1nMt8_-Ph3izjQHvJ0p53BYHofbA7nsLV-S9LvU5L-QYmbVeZzuCDhg9oS2T4TOz9TQ6WPoj1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftSRh_OVlzq9PE32c0pzyhPKpvZNGs_JlQnk_tm8-4Ae9Pd0jWvl6R7hENQ7TIiGwK7OqMObqnbP5ilirr4J-fzI5apZ3_A5cGyC2J2Gucts0X2deiG5cU7O9U8bZVbbyn_jIljSdsvHjKnayKYYbo0g6Mfp4sJXis1nw2eAoBpB3x2LQyPmOVXdiBWQ7Y_R0Kn0va42DKNBxpKVSxOnWcSKBs01h7Ah9SNFbhnBG5e_c2nS0HOJUSyYsL_Zxwggq2chFAU8u9tp7I2pV-YTA-j-g5iEmprN10D5mmps6zo922l7l1_qqgLiS8BRb1nXdZSjzU9-2pLrLHjjsgOst95I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftSRh_OVlzq9PE32c0pzyhPKpvZNGs_JlQnk_tm8-4Ae9Pd0jWvl6R7hENQ7TIiGwK7OqMObqnbP5ilirr4J-fzI5apZ3_A5cGyC2J2Gucts0X2deiG5cU7O9U8bZVbbyn_jIljSdsvHjKnayKYYbo0g6Mfp4sJXis1nw2eAoBpB3x2LQyPmOVXdiBWQ7Y_R0Kn0va42DKNBxpKVSxOnWcSKBs01h7Ah9SNFbhnBG5e_c2nS0HOJUSyYsL_Zxwggq2chFAU8u9tp7I2pV-YTA-j-g5iEmprN10D5mmps6zo922l7l1_qqgLiS8BRb1nXdZSjzU9-2pLrLHjjsgOst95I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-ALVwZxfsNSBsouWeSDJiTcuPG0rYVRUATwu3opWkQHI4DOJjeqwTxqotdyz57GaV7UvRt2hMK4Fe482Ww2OhRcb1WpO6aGDQoLvvf1KLFthcOY9iPP1SWaG_geETiqX5Jl5F6KR8TgS4jwU8Fazg-r1FsUg6-KKwNG6ENsSOTEAi0teaxwSJH_e8RhE-mifXD7Nc18x_J81qZnqGLuyslfIO43PYgnx0Pxbeg-AIVfdZjpeythC0MUB5IviS_asNm1EnkWkGkgpXwQCMtP0YehXhGPQFmVrp263qTzAIHyYVlJXGJDXDwC9DVEDHInvcfTewMAWDL6TSns-ejytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlPyDAuRryfddlH1ESnnrffN3k8eS-ElEWpt-NDhw_H-vK0SbunIqbgx3JX7AsTe2v56miwMfPP9-ESdwsn9yVm61TU4FxPeze981Y2XdFngNGS9GW0yZDJqWrYZ62M1_u6gypdQvd56ADx6YtBxmDKo3qb_12lNRUHJvX5mQBbCs4GcU0lQS0n4RWJ84Bv8Hz7FXgfnqnD8DrIYmxUKnmMLtyzWENoOpWxUHderqR8HSx7b3aDLhxHrf1R_aYrR-V1YrlONPfD8L8CJgOEd_Kki1L5Th3KhWY1TXr7AdGsWSn7SIcNg-MpsBoaeGmm3KPJIQfJ9DvqQLb7MFM5QWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmQO0R3ozyBzYwNg-5ybN5k1UgZ0X7Q6B46WMMkvaLAMzf_8cMdMUMgT3lIUEMCFSO8xuKQeDnz4J2hNpydxdxYy17K2hEa_bS0rB4EMO2h90avyy-zOAEQofKkLTDu3r0Z2y6su8Xly8DVqGx5DylSRlqL365Ck3yqUfwuvlP-7gNNQae7olVKa67mk7MeESeEf8QalmmTaRVnx4ivHjHcPxaPgEtqTRALcSwPsCiBgvJFNrGvAt1f2zwgs7IPv3w4cf044QTVQ70aH6iDnlshCsuNtzkYaDwWjcOWg5gFabyX75q3mDMNk73FOLU52pv8452dq6bBhGPmq2vHMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNmao74q2WqGl2owoycMam57gqBQ-Nw2QPZKb5b_zmIVY2Aode9Kx1gAQHwHZFDOWu2iY872dakNMyv_pqHIKua67j5F_Lk6HPkuExKcK52Vy_DwVtYfRlM3nG_1DBK6CO38bSE0zgf6qw7-ukYlwHYOFUDaEz_Rr0WEs3jq4BEvCNwGsuY_sHlQlxppQ2VaZPDdoPZF3fLZ94zSffLVBDEZfmE7eNZ76DiF8Asxj_UdpYCo4g4L7OYAcN3m4s3RYMQUeg60fPcihlsM5epIwDpJ3EFk4b6RiE0oPtyM3C00T5JvwOJJp6D-bdM8b-JXqgHBysM-l3qvSD78pJ26Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXznkU0VLetaaieaZNiYKaqk_qL1mYofiEANMVDM9B5_0F4_cG6avhGpo9xPSAoR3ZJfKPmgkpQsUcWUI4MZn0077H8QY0dwI28Rljbt0Dnr1exmML9A6IZQB5Fqdy4y1tLuiFNEFErTFzqX1zhCWFe9LORH4kgRqLgMFXsFbSd6xYE9GKPrYKSK_Y8xTc7y2s97qB6j1wdBbRUnzOJKW8Xfi658-lK736wDTSR7wB4wZmx-BuezCXFQAZtUcZTx0JZOfsk8aOtPY3_qjFc766Uwfs3az4C9A_zg-nKv_G5DhKg1DaX0832IHIBpf8ggpLFXXkxUXDUVhliaTKCIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=u_RGq6szeOr9B7uELckE1E3blf3BFCffYJCw-xAzqOqd4WhbSbGg2DRTgdTRabVSdM21y5iKdycbg2723_zZ0zxVAeDmx72dYsq5Nzyjk6gMO-m_N4o-WXrAjaBpr37LDby24m8WUh446ydMlgbXdDSAYzs6bguVRdkSsQxSF5hPpaopzEfjxEpjaK-SByLJAPaWZ1cvPybICPujx8Ud3EUFys0-_IFpLLM2QljWZB9QH9FJ8Qf3TgqD7Ir-LEAEyfV94I856heyVE5DVq3cbO8TpsdAoGjAKs3-bD0_kgjGC0kP65qftAx0SBt_ZkoqhVu23qpeO3Tjb4j8e0XZBjWK4aQ2uBgnASm2y3bNoiKu6ehWRntKeZFv_VoEeL7DubQ5T151AK6eRBsEWyAXuM0KE6JvwQYJxVYvh6eNtO3XXpy98uHq9TR9VAdHpOB9DuEUD0Hl2rYHJ52ERbCAJn0E352SWwYuvlIlgIRn07NkbJX1fcJqH2YF390uwRK-COcvk5vnXlfchmGToPdvjpS-od8HGpwwo6xMc0wxKXTh5b76_GRPjL0vuh-Ldr-aezR9oi27ZknmXf2fN0ukuiKu8MMS_feTeZ_tN20sieRN_bSkhtE1XSwPEvNUrGOGdR0kGSeyM6eBlNlqKPGtjgOKHSFi8DFTdOXrB-uyqOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=u_RGq6szeOr9B7uELckE1E3blf3BFCffYJCw-xAzqOqd4WhbSbGg2DRTgdTRabVSdM21y5iKdycbg2723_zZ0zxVAeDmx72dYsq5Nzyjk6gMO-m_N4o-WXrAjaBpr37LDby24m8WUh446ydMlgbXdDSAYzs6bguVRdkSsQxSF5hPpaopzEfjxEpjaK-SByLJAPaWZ1cvPybICPujx8Ud3EUFys0-_IFpLLM2QljWZB9QH9FJ8Qf3TgqD7Ir-LEAEyfV94I856heyVE5DVq3cbO8TpsdAoGjAKs3-bD0_kgjGC0kP65qftAx0SBt_ZkoqhVu23qpeO3Tjb4j8e0XZBjWK4aQ2uBgnASm2y3bNoiKu6ehWRntKeZFv_VoEeL7DubQ5T151AK6eRBsEWyAXuM0KE6JvwQYJxVYvh6eNtO3XXpy98uHq9TR9VAdHpOB9DuEUD0Hl2rYHJ52ERbCAJn0E352SWwYuvlIlgIRn07NkbJX1fcJqH2YF390uwRK-COcvk5vnXlfchmGToPdvjpS-od8HGpwwo6xMc0wxKXTh5b76_GRPjL0vuh-Ldr-aezR9oi27ZknmXf2fN0ukuiKu8MMS_feTeZ_tN20sieRN_bSkhtE1XSwPEvNUrGOGdR0kGSeyM6eBlNlqKPGtjgOKHSFi8DFTdOXrB-uyqOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY6Vv2Vy5mldu1_IZuhnyEhyCU0DLPEP1r7Z63xi90DsSFJJsS6ddA9V2paBwdmYiNsNwGMpzBLKr4qc1EzqHukpV5WAoB9tttCblEeUMPSCZdVSG1bFGt5zl3xCywo8qnUZHGMmDFu8vnY-HptyDkgpxdFkvkFw--JPSpNs6bCso_75U6IMsn4Sv_bMXjBPNzFSETifL7pymfWOiUKYMFw3v5J4hJhMrbuT4yq3bPiMvQsB8020VG92UNWLlury0HhaY3EbQZVvhLdIW-tFQunxBW2cX5yj7Q5YH5d8DAqZ8j3pfifCCxHm-0uK4Uwp3Z2h92age9ZPk8G9d21Alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=ouCxW_cwSA73t-DV6ATFu8zJoEAS5OEtCblkUEBdy2BjN1zS5MfsOjpPd2fBRmRny7kiQeVkKkIwH9QXQQrs1aHAvrvz0FnhfBTlNuHO0w-yx0QQh_IeaAX0ZVpmX703qPozdTF125Vml7Ax2Xn93BxDxXTuf8B26waSyZ6r6lQoeJRoU46M1dEg2k0Bt0bSd8Y5EV3pr-e45xr7Pj9fXe3T8lE5F7TUjgoCdThQXuCHmyCaHa4G2Zf3goxBLed7YLclICZK8_BsMIfx6JNjaW9OgXmhSHUxB9rKkR1km-ZNvTuocFFH3FVMzLDeWLwHkqVvBdJCkrOD9jxeCzoxMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=ouCxW_cwSA73t-DV6ATFu8zJoEAS5OEtCblkUEBdy2BjN1zS5MfsOjpPd2fBRmRny7kiQeVkKkIwH9QXQQrs1aHAvrvz0FnhfBTlNuHO0w-yx0QQh_IeaAX0ZVpmX703qPozdTF125Vml7Ax2Xn93BxDxXTuf8B26waSyZ6r6lQoeJRoU46M1dEg2k0Bt0bSd8Y5EV3pr-e45xr7Pj9fXe3T8lE5F7TUjgoCdThQXuCHmyCaHa4G2Zf3goxBLed7YLclICZK8_BsMIfx6JNjaW9OgXmhSHUxB9rKkR1km-ZNvTuocFFH3FVMzLDeWLwHkqVvBdJCkrOD9jxeCzoxMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=qNGuW5EUPLXo-N-zsltmdBpkrPAdzu1Jzk8oEzh2edmDXlMKV2FkR48gM-V99SuHXf1DSlUWqvAzBLUYO8-5ERbokXeVERCWi9aODXg6mwHCFZZ8hzO6kQ48KThWidv1hEgdKdsnzYS_BKvklB5AHGX7CKNJkjQbcrMh4PSBwcGp6_nkVZ6Kv3QDM3oRTzfN4ZhXRj3gWdI7LsD3JEeAJXSmgAJXl7ZCa2TEwEpwJLvkmIUUVooczcO8sG3ju887sz9meiL4PaV1rRUJJosp_mjI-vDTP57mRjGCZG_b0UlOyNZJiNXdqvZAluQ7bIuA1tcgKCJtDwaRFuysrMl_hqYwpC7H9YlS0Ko3RI6OlI2i9KlgOKT718QLuxkO5SZv2T8elVeKM6kaxuyYn9wZ29jd45oPS4kEOb6s9cW2mgGJP3JLrkcJh7v4gGUOVfVEZnvePNUwYlLvpRAics_52DT8If4erZy6B8Hr1W2jpiCW-38CMUDgN2FokU1qD7Wh4hBoHGJxuYnrUm1QLu7IHdYWShaAaZA6n7nvbLiOT-5vwyONmQhoH-pGkvnFz8Uki0EWsyBVlOdxdTzWhCg03s89ZDxIxeRWFTU10M4R0vW9jpSmI1cJXaM7BHJko_HtgdSjFYveKWi66qHnUFHA_SMGuxYJtMXPRqKdkhJMGek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=qNGuW5EUPLXo-N-zsltmdBpkrPAdzu1Jzk8oEzh2edmDXlMKV2FkR48gM-V99SuHXf1DSlUWqvAzBLUYO8-5ERbokXeVERCWi9aODXg6mwHCFZZ8hzO6kQ48KThWidv1hEgdKdsnzYS_BKvklB5AHGX7CKNJkjQbcrMh4PSBwcGp6_nkVZ6Kv3QDM3oRTzfN4ZhXRj3gWdI7LsD3JEeAJXSmgAJXl7ZCa2TEwEpwJLvkmIUUVooczcO8sG3ju887sz9meiL4PaV1rRUJJosp_mjI-vDTP57mRjGCZG_b0UlOyNZJiNXdqvZAluQ7bIuA1tcgKCJtDwaRFuysrMl_hqYwpC7H9YlS0Ko3RI6OlI2i9KlgOKT718QLuxkO5SZv2T8elVeKM6kaxuyYn9wZ29jd45oPS4kEOb6s9cW2mgGJP3JLrkcJh7v4gGUOVfVEZnvePNUwYlLvpRAics_52DT8If4erZy6B8Hr1W2jpiCW-38CMUDgN2FokU1qD7Wh4hBoHGJxuYnrUm1QLu7IHdYWShaAaZA6n7nvbLiOT-5vwyONmQhoH-pGkvnFz8Uki0EWsyBVlOdxdTzWhCg03s89ZDxIxeRWFTU10M4R0vW9jpSmI1cJXaM7BHJko_HtgdSjFYveKWi66qHnUFHA_SMGuxYJtMXPRqKdkhJMGek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
