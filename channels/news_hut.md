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
<img src="https://cdn4.telesco.pe/file/DxSU6E9HUcUqWpvmeQCIIoCr22lB5gWepJ-Qvv55nSrsZi7Qibr3ry9WESECa1sEvb6_V1k3QSdnwfJZCTc8xL3IqeZdFF-pza3K4GuNUoVOZLfRd87cTub7n_-Kh2Uf0odeyKSryt9-vKnRP8weIFVRQkAngD_akDUbbB8OqlnJoKr5gn9C9cMq92hyHdBvdeo7aQYEhVfFxK1NAl31NnKovbRTR-oGrY5Qikjtr49s66cyM3mbB95pB7buMEh00YCQYYSpYx4SP6C1DKUJewMIuWjomS1E14jugsqO2XYlFN4886tr2ZssP3OIMFaSUpMs6hyCT5pQXrPz1SkkEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 145K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPBLePufAL-uLBfwCt2dSCHyrdue-5VoGQ2rooCcJuQ6u9nM2ABKWW12HF1o4BTZrYpkzsE_I759a_KqKV7CkcSQ4ZenAiFJcBw6ah0VSefEmqdF86lSxn0pYbKxWAvEssy5nfDwS6DZqpB5x9CFAT8qjZf_sldXpD-q6UsqNBjnBnGHfmZLG2NdKIDUjlGqTdKYfbgfgzMKvDdK7JCIdf2gtRJiY7eaz4yPp66yd6CzWr7uuNNe-6Hl-kp_9BM52BC524WnpmRaSSolvTL5lmm2dfligjqsWtKcnl5u36uL0w0G0LyLWVKdhmjUfPyaNA3y892DfGgYqhAfu9_0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0e7TY39qUxSg1bpkG39JX-ELps6sXz0sKCD4rMqDwVnGaGU6AwH88TLFr9WJS7lUlJYueEVk3c9Yn_g_9NaiL2gsIf99XVLD9GfVH2akTpcARtbxjYX91S7fPE6wc9mVPRNo8eV9LoxJ6jc6FEvMS7rLfiNMJWFhelJKid906YmMheCU46lXBmSR1ysKekqwAQ9wwac7wZWa3Wz8de7BCwA4dDR0a7WT68vWR0JdTnP1nqj7x0EircPLAiGdR0Hkf-aloj4PK3JnAWd7xAfEbh-xSKVg5C9pNLBkKv7DEP--e0dt1RTTLw3v20oDf4MvYS7inlE03KsRAE2KUW4ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d_Ii_awOWTsfVZpeodVE9vm88Ha3NMPHkAlpjaRmAsGuCFRXfkfVhllazTeRNw0RFZAWk5qNT5gWLNASrwYoCuCcscPUUiBUmtjG8NVw7HKfq98syx-kaQVD_kQqEulVqKYx-Ae_oV_ui0GVYvwg_vYesP5EXJ7BWMwUhgGwjFtdHTARoNCGZ8Paq_r18MRLIbjQPqa5U9IH-YLd7qAgfFASdypKgsmsqZgldRX91O09zeh3f3ma9z7QK29yQ0jR9SdAkRjPXboMuymmxKDpBxE1t6-Digmwh3Vx3m7eMGGbhh7dU-lL5khdUcTrT_25iuYL_H3FyikhCS8oeJ6ILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KvW4UgxXR9lMSGmQEVbJGWklOpsbXWyxJcicQ8ayMzaXihfBXezm9KEUwhWNfDUOFNMnDln-u_QviaoIGFuo3L0iGj5UuiiemRx9ROSRVSRDtW22pRzA30yHc3GKo7OxD6Czm364LaSPczyk9dLPHNUvNlAeINK0aV-2WF8yfWBEQQnMtNp0bNka4ZfRPaGAXU_pfoOQalaQOuZsSYNv7Bcqqs1fjRKfMi7vB1iolWFxgj-olXafeH0KsQatuuP-s3AyVIv2kpzlIwrSe2cA93HzcrtPjc89b_RHIlDLR5ZZR2DMwUNimDEzm2qg94OmSU0DvFpA5efmxEERr9rz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ph5go0P8twqx3GDZKFPjDJuSwhWAdUZa-mNflZaPr9xJvf0tmbGtpJgGPYMpA1liW-TSEGBGMRIg0aIlFj8Ki1-Jx0MoBT3jDdA-aGyFlo57zlnAZIjCD9WLj5OGaqNN1lJ6aG_j1orICaQtyyHWZK3BAuYE8jXto-BIO8dHXhSixFlT3AgtKFPB5VkzslKP1MGiVq4PfMuVM0RH4vwJYPAFNHBOAIaoZEb4DBuEJ1VsjxV474K9uRR5k-brsZIfs0caveFclSCKASYCb4S0qMbX6VSyKylPzMD7RrrclU4FUeTjU9BPdzU44LkrwhUbunGrNevQ1-Rn8gjPwzVrXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d4U-YTM-BRw_2-VJ3gwKkYMhbAIY-K3tuGiGT07njfj5qCtZIJiKzUIYSwCTnZoj4KUJWYHMmWybNISYbxnURG1FBeEOQavp_XR0bxYRgaI1UmiYY3X0DBJupz0coMjmCU31WcU49f-UfCGTJYjn1nKdUcZi_tIAXn3DcxnYgY9v61qLI2L3ujn1TOBKIIkov2S8obhd8kAmPOYH7_OHScWO57o1xFXSzdUGcv4aJ5ryRPDVYr2M5VH8Tjs83Q9X2eNhgrFTFKxXDxbSOrWlFbkm9lesL0M6m7QXgBpC8N3yqUmgQ-zFuCRNomim_JF0MMBmrlrXw2TzKshnfL4VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eMhJihqDvGC3OuFkTccJl05N6sBPJs63QGPsDo63pWE4E8DYgMx7t-eevackNl5f1k7Zg9QfJsauo5Bf2uUp3olgjcjqArzutw1D-VTnDRVvO2qU3LbXyhSLXAO4OmgriXmjYuX7Mkc_oqG6sAevGPJYM-Mn_zCrnbTrF8j-t2XhIs4awpyCpU_NZGjTwLy0w0tBERZMWdnY8LnzqtWusdikaWizMaspqxvSUbe-7i1WQv8GSAF9DPVBqRZ6dVl1HDOZT1CsZI1CnRhueRA_8mOvSJTHChQ0iPZm-_5GEx2Z_OR3sHLXL8BAhDKQ8mdOJVqM0-kBviwj0vthEfayBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UdRUzIF7L1MfRvQXNboMUYKpJSeEaHTF4yyjC2i20U6j4VYovNzCWtJFyKDORT_V8yIKo153EiT2YsAM4mjqXNosfccaPhP_mk7VIFdZRriAmDOXDwAdmbE89icFK_7fnEBecbz0v6W52P24jZ4B8v_jXigOGikbAS8R-2vbbxjB7Tl6CvYGHHAlW9-rLcVPHkGGFO-nqVdp2brukT7M9-ed4K-Xb9NX0VJ9L0l8zTFS8v8DNJdwKBhdmz67xS_orl7qOMp_CRUykTTy1mL5QqMsQlSIcnxTt7EsPGMhzTtckTWJg9gBo44mf51EWdlKNbzmmCP5CJkK3UJina5UnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WnbuOnCuU97LrQxIYg5RM6wE_aP4HBT-0T-UE07dMspoyADCaHwH1FGkTktavsZJxeVWZTxFmxyg_mQeFWKYNKIUGfFpTCL1eDgMYpd94uGIa6KYwiCBcqKCAXhuoExAwU6ayLb8lITQWuOxqhpAcuIflzESiyHy70D4lDhmM2vfrRDQcAL32wy5kkwRvg3GggBl7FDjn3nRY1gCVAzHDmog_lXwFXDMTq3oDjRpKlhG3TyfErOViHnqErdnmkD0LQHg2sPbxHYEbaXL9AZtgj2EhqAmYAGIoC9KEW8TmgmXhkwrq3PRRYkGm6q3ju9U6--bYjmt_572BpNHnXSM3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
پست های دیشب ترامپ دلقک که با هوش مصنوعی ساخته.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmu58epFkcfCr_UGg4fWuuwjLqfTKt-nqYataDaKirAb-zDmyf9NN19aOe65JGiNR7mkc1JEEL00-4iiELZ1IYcAjm97-xj_FymFTbEn4QNdTuzhJbMBGFd4_oe3hCH7cMywHEcIKP54eIQJaSjfBsXy4YHFMsY7weeWuInrjto9d7bck_8LVAFmeFMkRQqnQ1flvYLXQtuth7-qViVYHPCKFTptq5QL725GeqBh4LiDfs6WTdQmx0hQHV0qPmPmVMdoC_qpm45oeIecR42ayLXPOAQ7JyhMHg5NGGTvKleq-odfYo7SjkWy1lyWOAbW6V9QRgfPCVXbApks7QtmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ILHEoGMota1M1K_sg6OLRf9SL3EwI3I8iY5oKNQ58LxmlMNzYtDlBnkw4Qz0aaaMMyy-ZZaWVvATqBFcTUGYMNX26YL9SIekjDrs_wJ7Ec8TVVaTo92GeSNAZsYHnLkvBi-S4SpioSqBQrbLXfCPrKM2Q18ZPwdanpZuvQ2RpF3lpgi9z5ab6ilGy3LkZuDmrWpoCQ1BJT2LqZ3WfeGIpn4jUN-K1aoWgaShvHButlK1i1jF7PaQTWR98ySkrTKcEsbXvuWixoWw417-1Scox3KLtjIVRJtmDH3ohS_0_U2k_DVXecxCViuzKpWZkdBGh5DyFz7CZPtD5yPTNdOchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WygTXJgii73NZYpc0PQgx7Jk7eWFap_C3GMcZm-iJ4FJ_hWS7aCkwuM-J8yB8OHF8sux0Dccg4OCHyAnuBSLcmKrMOd7fbn1vb6g5AV_X1mdbsgFsTjosdN0DJx1lpurJWEuTWahgh1UwCzQBzV-UbfxI3eR9gbc20BuTxh7jPgBc6DNsGqqXiffZi4Dh-0qBaOjHlM6uokXvcyOkz_vHcPHU0b2EJ3QbBFvFkNCh2bjxInLJgsAW0NLKvXYcmoZcN-X4pFMFZ_L3JO6GJQaEq7oQGHk0OV1YjVxSIv1_1p3y34qOiwcTaDpoctPj8lGsegfWduyh9FpsEQOYYcylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=RhrYEOcHGvhb0c42xD0UKEwAcJZvEy7mNSazXPCvqixBgH3bLsAw0TK8Fzt7gA0kEO3NAYK5MeX9vnEGkfd2ReRaiAF6t9znS9wRfYCYLf7FURUFwcIN9tIPBFvEtUe3VQ1GieXR86uksfWs1EaTLZXIpXClOa_kq6NQV3BVMStUEm2av77oh13_DZib5cLlgHS8RYq-m1N-87fOoUrX7uSI0D8u91hDSfRLqE9dlpGhGhQUZiRLfyKfORPNg-ziAWqqHkgYHT5p4yebNbHYGqXGKyZNLeqlGdkNgKcXDXEDjeYIjnSFSP8GAmmN0xzaeouKpr8ZPVK1cw-gu3D93g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=RhrYEOcHGvhb0c42xD0UKEwAcJZvEy7mNSazXPCvqixBgH3bLsAw0TK8Fzt7gA0kEO3NAYK5MeX9vnEGkfd2ReRaiAF6t9znS9wRfYCYLf7FURUFwcIN9tIPBFvEtUe3VQ1GieXR86uksfWs1EaTLZXIpXClOa_kq6NQV3BVMStUEm2av77oh13_DZib5cLlgHS8RYq-m1N-87fOoUrX7uSI0D8u91hDSfRLqE9dlpGhGhQUZiRLfyKfORPNg-ziAWqqHkgYHT5p4yebNbHYGqXGKyZNLeqlGdkNgKcXDXEDjeYIjnSFSP8GAmmN0xzaeouKpr8ZPVK1cw-gu3D93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=jUSyDLNh_Aq8O1m-CmTKTAx8ROnVdUwB_KL_Ne-NTlovIW1BqOAIZ0GxEEZSKcrFj30x1K-d1SiZQBQOIyd2FBTmeZNwKHRgzwORtoyEZUnV9L4fxvsFedNy3Wet98tNv7Z8U78nnnAZDxRYe32W0KEiaWZvACPLykucgLYBycORy6naNASBlU_V1P08_8NaM4Wxqxd0VFsId3RDdKI_AoAMFqQGfLpUnOjQ9ybiKI9ZI_kluPEiZtI-HCtx6XH6IXFXehgZhlZGsQLVSJ3Dc-SB57O5Zi5QlQVAYSVVZ2fnp4-wQ4uyHdYbpPlDF9HaFsfjteu7JEXJGzltHm7cqA" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/fee67a1237.mp4?token=jUSyDLNh_Aq8O1m-CmTKTAx8ROnVdUwB_KL_Ne-NTlovIW1BqOAIZ0GxEEZSKcrFj30x1K-d1SiZQBQOIyd2FBTmeZNwKHRgzwORtoyEZUnV9L4fxvsFedNy3Wet98tNv7Z8U78nnnAZDxRYe32W0KEiaWZvACPLykucgLYBycORy6naNASBlU_V1P08_8NaM4Wxqxd0VFsId3RDdKI_AoAMFqQGfLpUnOjQ9ybiKI9ZI_kluPEiZtI-HCtx6XH6IXFXehgZhlZGsQLVSJ3Dc-SB57O5Zi5QlQVAYSVVZ2fnp4-wQ4uyHdYbpPlDF9HaFsfjteu7JEXJGzltHm7cqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
‏
حدادعادل: والا من خودم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/guw7xdKKGHun7SMwDrmn-sm2DDfOY3rJjsPbHA5yu4i9Ye3eSS9pSBXZ-pbizK99BJovXSkpDMj0Um8sg61QYPuQ0iqt1XPhfQA9NMytmyUnjxurQVmPqh2f0GVCajNcBra2RbXP8VZl0SEm7HxF-jhn7eYweGHKrpJpeVJq1niipfdMhLjzrcO21H026wLKuHJEoo888FN3hcXWsLc1H_y0ob2j0mvjWfPNniZPHo_hpAV-MhTDc15BsJwwiJeMFgEHCX5waaoEZNOBmRFbHNYNdF5r9zH3aB4-inDbaxiWvzMK-uDultRLRsQ1rnM4RSkop9rmkYF9d7oYTEEZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmlIRrwFAo5ptWA8DAMvSLrXmNbcO0bibbO5-gBuIRH26p0bBBE1Of57qgW4iDsWv5hiufl4OIeEHFT6uUOR2OsTOcMdIPhJTvAi1fsBDCPWiZihW4wiEHm0dHANLKp-n2LpItRYSj9kMYdy95pzng2fSwOXHe_3055UJfXWmm012QAHLzTCLh2lQk-zHngqDlzhU_dr9OB8TCW4wezRkDXnXBLG3Y6i1D3ym1B-WLAJdd-kYCQwmR_Lm3iylhN4GyB-nK0YlSQ4wvvz-qDimIavNC5FEYlTzJRXJrB4pmsgkKRg05QboSFr86IRjNA_wY4s6Gvw5Ei4_j2dBJhC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A6cLkXG6GB46h1OGGu0xxlpPH88ma_D-Y7CD_cFrvGadjKYirh3p6eliTtgynw4Fj6CnPfO7DYut0sqQw4X94BvvKYORJb3YRIoSQ_0J2TOubjej7mkcaXFETH36s-9pWhTI_2mUFTJxRDKiCdWiCS7y11afEptfurZ-2h_7hGLzOss8w1v4EanWRi1Pzr5wvqq_KHHf-r_G4M3SLA0FB2EieUzHgwSJgYAV2yFDGy64JxjnaXNrXR80cKjUaPY82uJNPwB_P4Nf93aN34HIcDNp3S3U0-tfLUMKuqkvKTqCtiS5txsCkRAdO7_UM618sjbMneHWBAFcN7wohkZEEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=GCNCoipks399EClKEPkU7hNXY_6W89vlH_QAxjx9zo7zMjDPM4CCNF3tS2kVKjC0di0VRcrudVPXz4D84aX8YXShZNX7Z1ayTb09Yq7Zh-yRs3f1ADRqOP9l0kdCIViN9JFPOvjvX5wQSHi8vOGe9EVAOJur__w72ZSLFq0WgPfeo-BjkLeuKcyAncPLIk53zCTPgnhLyYsPvSOPoNUw550djj3oHVg8uFoTuVEjnTO85XMxOEStY1mE-M0lXUSGQZuKHT-MA3PkHCYBa9Hpjx6F5v-7Tc_RaHWIAHk9vV9xBjRITYf1bOBXnliZbZsHDwNZ-3OAa4V_-Nxbym2DHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=GCNCoipks399EClKEPkU7hNXY_6W89vlH_QAxjx9zo7zMjDPM4CCNF3tS2kVKjC0di0VRcrudVPXz4D84aX8YXShZNX7Z1ayTb09Yq7Zh-yRs3f1ADRqOP9l0kdCIViN9JFPOvjvX5wQSHi8vOGe9EVAOJur__w72ZSLFq0WgPfeo-BjkLeuKcyAncPLIk53zCTPgnhLyYsPvSOPoNUw550djj3oHVg8uFoTuVEjnTO85XMxOEStY1mE-M0lXUSGQZuKHT-MA3PkHCYBa9Hpjx6F5v-7Tc_RaHWIAHk9vV9xBjRITYf1bOBXnliZbZsHDwNZ-3OAa4V_-Nxbym2DHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJruJ9OgPFk4VDLwDc3IVWA_zSHBiyrRQn8BZzUNG3aE0Lx_HmSuw_xjB0bBPylb_z3xTJJ6MNDEt56HMylii57e3QZOx5HAwttd_eMCXe1xrtohTrm-8IHjr--7CG7cJP8hywKn7sB6G6zWSCCnujwCcVoZ68He4c5D-PJRcKEEIYOuLVjMoUJEFfSmqFxwMUqGxzZAYDzDkiE9TmYHVcetsrIChLRiJE7H2IQOuqdVvFBsLram5pRZDM957hAcFYfqVQDlI-55rzhj89z9pLgaMGO0IFtKcxn60O0nZkNXimQrAiVQWtcGMSX8M9IZD9brRLh5L0WLohzg4y-p-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔥
🔥
آفر انفجاری امن‌نت
🔥
🔥
💥
گیگی ۱۷۵ تومن
🎁
۳۰٪ تخفیف خرید اول
کد:
AmnNet30
⏳
فقط تا پایان امشب
❗️
ظرفیت محدود
⚡️
اتصال پایدار | تحویل فوری
👇
برای خرید سریع کلیک کن
🤖
@Amnnet_admin_bot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWMyItYYOI77DnlOLWvTUriFFB9ZkeHEtx0Rh1K-MlrLq3igoSyV6qiLiqtPqxclXSIP9Epo8f0VP98dXOQFcsrTuyJZt_Cs29W-XZ3bqtXWpTVqvvBgl87sHvMTO5yG5E3YTToSkevCuKVbyL4IMOTyNkgujCTL2B38uPCmuwuNse5_CaXA61XkH98-6h_8_8Kp3yJfr68ty-4EHvuYUuRAHaK5cwHt5gXmnDTlpeg328_k2W5SS6KV9j5a3TPObcL4LhhxKevLyELhTAiIhQpOSzTYt9SNVHyU68fb_b6p75FJNcvFiY9pBi2IlkwGiAbqGDFwnTErVF-2QLUpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rt4G2WBmv-TypJC-zma8r1y86pHc9PJqyEnTOrBLG68MLlcGFMQRsJC_05p_rPJwsNY7_gyDJY06_iCfxvbYBTZS303BaI6kpXDXxR7JNbgEByMvm4GbJhJ8WbIF_4UWPh0sUrSVTWeqkrwbvWqPtn523D8nt8Da0jb2QWc9_OQ0qt2VsogMXzeWsjfVy2R9uGbi2RsJP4tsrYlZJdCuL1TJ1b1oeXrXR2VkDRsaVtGq0RjkXDe8kI_18Wp9vDKXIwdf28VaW-guk89jizGxH8DVIX3evOokFvFwi3DR7iU2qA4OMPWqcK3uccbLqIQ5HcBytFVQdTZVG9dQIhsIkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGcj1rAPRjLpt9h5-YOC6punkprFgUHqXcTXIV3nsF_ZjUg5GVm0ELbJl9XG5P9q0S1GdJz_8c2r1OAfxZrABylqBuX6AviU2Hpvtn0H7AWnJ63yQ2x6jH5yRFuiOE2Bu7tPCd0xOzF06etoLXesezXlvCf0I-F5QS0XcNWDDsMz84Ka912DbO_nR2rlIihzypJFFsHYBujBCcUZSXORC7rtY7cOFmlDkbwH3PPpy-avrVcAPzT6OZeHCoMcKL32r_rKsshEgCeh0DbPV-V3pAjUVXXkb9U6ysHlv5NtojpXbAdojXDy0jm7HckAZC5LLRVm_SG05WeQwuFDSY0y1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=bWydo1Oge41LnnDf_Z5dIWoyGkguyzcrnDnsg3AcEnaBdk1ft3OdxsX4VdA__a--aYUZYYKN3PljboIhAubEz6SmKqjNPQ2ZF4fBx88p7kDyuMmJjyhAJcpybWIkv3zykCLtMkN6NcRgn_KyCLeOrRFS6CUca7dnLxsIEFbeMQdhZV14vApp5xbhnfpfEOObtxJeeZccAv2SUSYx_GZXhmd1hfDBPxFwb-ubZuP5zRhcKBRhTsXf4xH_TkYFaYhYFMnoimDRzJEzqgaPzvn96Y_W4QB8juA35yEXM3ZSwE97uxsCOsLLVgTlXzjj1aXgIV5KcK6UcexEmLMdoBHKtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=bWydo1Oge41LnnDf_Z5dIWoyGkguyzcrnDnsg3AcEnaBdk1ft3OdxsX4VdA__a--aYUZYYKN3PljboIhAubEz6SmKqjNPQ2ZF4fBx88p7kDyuMmJjyhAJcpybWIkv3zykCLtMkN6NcRgn_KyCLeOrRFS6CUca7dnLxsIEFbeMQdhZV14vApp5xbhnfpfEOObtxJeeZccAv2SUSYx_GZXhmd1hfDBPxFwb-ubZuP5zRhcKBRhTsXf4xH_TkYFaYhYFMnoimDRzJEzqgaPzvn96Y_W4QB8juA35yEXM3ZSwE97uxsCOsLLVgTlXzjj1aXgIV5KcK6UcexEmLMdoBHKtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار
: آیا آخرین پیشنهاد ایران را رد کرده‌اید؟
🇺🇸
ترامپ:
نگاهش کردم، و اگر جمله اولش را دوست نداشته باشم، کلش را دور می‌اندازم.
🎙
خبرنگار
: جمله اول چه بود؟
🇺🇸
ترامپ:
یک جمله غیرقابل‌قبول. اگر آن‌ها بخواهند هر نوع برنامه هسته‌ای، به هر شکلی، داشته باشند، بقیه‌اش را اصلاً نمی‌خوانم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyJa0-vZ04yOOUVq-1O4gzHWmhtg3sQZ2sM5GGOwTL8gq8gN2XKGKnu_ionNyCnH3s4etCdijZagYvakL5KMJah2U1JByEWXoHtkk80cvbY9ZjlFMGebCOYygM01Z9eVK_IxU8HZgHT0YKN78r5E234rtrojk7wxpZ-yx9tFKHNmOeV_eQCXB3SVoiciFtLUwHlsgSoeGZL0VyCHrzyohRwaTu9WNodXh7XTyV3aCt9elUZ54vfIWRTowwxIBENh4H7vkj9uGH7N8v2SZ5Cr52KRAfzM5mAML4OgO4Rn1vFYsvM4aeD075DUjfaO8b1JhCsmHyAzLksQI8MtOkUO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IVcXQhYFp6Tdqs40feukMkHw6ObsiNxdKbir0MGVKnx4uykeq8G5Rks1R3pqyJGEqdh5R3amV0gf58AB8F89StvToQMYM1l7IelotTuQlZoGOiXA0buD_5660t-_10gznCSGExVHTbfIs23DEDDZOzI1PPHsx7lNHndyVKzs3VRBuA02oJZTwLyH_jQUT45yMVLt_6sjPpIE3E__VkSbCA_lD4huANEjorZALzizj_pY1ahxRp7xyAtMKP4xNWc7u3nDXzh9hUTMVQLzjQ8xwbycXV-lFrguO2GcyA16XC05jKsjUSoVzUAohX48ufbQxo3gV0N0VY_rsBhSkgW_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGQBOfOwS3mj_5rk_vIOfMmV_ev0CT_Sh6E3dRoRDmT5YW5UhR58FmwWOio8Jn4KCpIfAzmnIAzbXeBPoHuzduiao4fr2HQ3rpiGMdlCPcbSLXNM08LxztXzwXz8GLUCBGdGf6BYXswlN6mBCCt_rTrAQpaEQ0WpLQwQMI0jymjVkYhpEHoupPZPP96rIaBxdnVDIXIo_xlba9CPpcLdcVy41WbdQjXsc2cIHQ0Yc5oC0Qg-ECsVVy8wqCSUQYdJ2oAyz-M5nmg_Uaeuf7tltm59aBKEF-9Z-IGayA_5Dq2U5oY6rFDn0duR8gqC_5Ey8y-PoOA9fpEovKRAGRI4sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nF-UhPHkwOtgzCpjdxFMjrzUb4ke__9VDlVQaF4ID1xJ0lwopBS2veDp-x4Bp50fWH5gSP-r3MllUSheRZJkz315E44WXBYSJmE7EColCAVXantPxcSSof_DsKjUVl9fJFoI_bJTgb9F8xsPlTf65QxRAlLYEMMH3EUCVj79AMzFOLoNVYX8MzcX8HIjUQL2P2H2vIGKMu9heh3Cz_PQR9-NfKarMq1Foz_TX__5qCohRH5CsC4wG3IZ-i78HWaOJQOG7rJgPWoG34u-aCW6YfWDz0z9OgqI4_Qjrjn3nfWdlqF48L_31tZRpt8hvoLH0dTZqKj1blpD5TrbDPos1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14@HotVpnPlus.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/news_hut/64917" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoU3sQtK5KYIhMDdY01pTyMMlo4JGUP95_78uD6v0VvysMCMJOL34bvxEF45cv4uN7L0q9chMQ571QuyKxUtDAMHhyspErUssFEAW7VMj99wvxj2bqaFLyLcqTvvDWRQ8nENNc5efR08UJonCaFUWR5m0iu1qYzzlmA-IQ4rUzAU4l_smdPAxz4W5mXtxk_hnQMD1tyomodw7s1G0lHpdy29SQpGo6iIGkr406qzNaGyNa54BSvs7VK3PDtw3LFXG9KY-7tjYB4zBtu0Mn8Grq_7WXqEWSXG4MGcR5RwZmizIwAM1KZJA8hzq_YgPcBY0NPs_2nqvtTPE9uXw90Y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👑
یکی از فیلترشکن هایی که گزارش اتصال خیلی بالایی از اون میاد، فیلترشکن غیررسمی سایفون بنام شیر و خورشید هست، دقت کنید این یک ورژن غیررسمی هست که تعداد زیادی از کاربران تونستند با این روش به اینترنت بین‌الملل درستی پیدا کنند! در آخر پست لینک دانلود این اپلیکیشن قرار می‌گیره
👑
‌ ‌ ‌ وارد فیلترشکن شیر و خورشید شوید
[دانلود فایل در پایین همین پست]
1️⃣
‌ ‌ ‌ بعد از اینکه نصبش کردین و وارد شدین، از نوار بالا برید تو قسمت OPTIONS
2️⃣
‌ ‌ ‌ تو مرحله دوم وارد قسمت آخر یعنی More Options بشین
3️⃣
‌ ‌ ‌ تو این مرحله برید پایین تا گزیه Connection Protocol رو پیدا کنید یبار بزنید روش تا با صفحه جدید روبرو شید
4️⃣
‌ ‌ ‌ تو منوی باز شده گزینه CDN Fronting رو بزنید و برگردین عقب، دقت کنید برا بعضیا تا همینجای کار رو انجام دادن و برگشتن به صفحه یک استارت رو زدن وصل شده و برا عده باید باید آی‌پی هم وارد کنه که در ادامه می‌گیم
5️⃣
‌ ‌ ‌ تو مرحله بعد باید یه قسمت برگردین عقب و وارد بخش CDN edge IPs بشید
6️⃣
‌ ‌ ‌ تو صفحه‌ی باز شده باید آی‌پی های زیر رو وارد کنید، دقت کنید آی‌پی ها مدام آپدیت می‌شن و آپدیت های جدید در داخل کانال قرار داده می‌شه، تو این بخش کافیه یه آی‌پی وارد کنید و OK رو بزنید، حالا برگردین به قسمت تصویر شماره
1️⃣
‌ ‌ ‌  و روی استارت کلیک کنید تا وصل شین، دقت کنید بعضی از آی‌پی‌ها hostname دارن که بدون هیچ مشکلی تو شکل شماره پنجم، host رو تو قسمت دوم (پایین فلش) وارد می‌کنید
🌟
آی‌پی هایی که فعلا موجود هستند
:
CDN SNI Hostname:
python.org
151.101.64.223
151.101.0.223
151.101.128.223
151.101.192.223
92.122.123.128
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
2.19.204.19
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
2.19.204.211
2.19.204.217
2.19.204.218
2.19.204.225
2.19.204.232
2.19.204.234
2.19.204.240
2.19.204.249
2.19.204.250
2.19.204.251
2.19.205.8
2.19.205.9
2.19.205.11
2.19.205.27
2.19.205.33
2.19.205.34
2.19.205.40
2.19.205.41
2.19.205.42
2.19.205.49
2.19.205.50
2.19.205.58
2.19.205.59
2.19.205.64
2.19.205.65
2.19.205.82
2.19.205.83
2.19.205.88
2.19.205.97
2.19.205.98
2.19.205.105
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
50.7.5.83
63.141.252.203
65.109.34.234
92.122.123.128
94.130.13.19
94.130.33.41
94.130.50.12
94.130.70.160
95.216.69.37
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
104.124.148.191
104.124.148.203
138.201.54.122
142.54.178.211
144.76.1.88
184.26.163.12
184.26.163.24
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
23.48.23.186
⚠️
‌ ‌‌ ‌ دقت کنید با یکبار لمس همه کپی می‌شن فقط اول ip هارو رو از حالت خلاصه به حالت گسترده تبدیل کنید تا همه قابل نمایش باشن، و داخل فیلترشکن باید تک‌تک بزنید
👑
‌ ‌ ‌
لینک دانلود جدیدترین فایل فیلترشکن شیر و خورشید
https://t.me/hotVPNplus/9
@HotVpnPlus
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Lu21RPQ11W2t6_IXblgwusgl9Qmf_AyH7BWB55SluacrPtSh8kN1QbK0e3ka76w0Ugb4NT9IWBOMk_1WBp5iEfHpuHo5CJHbjrTTTjvJ3jbtG1C7CHuXUajiBzpY-_B0k59IqyYiGXgokjl33g0EJGmSW4tOH1df7QztJq8eqliAggrp1TIhK2XjsjON24TIk2k5uLsvFhZGVjCnRtItiwOGIM9AHARNdr7Tp542upTmNMMca1XEi0SXmZB44nut_YWl_wdLAyMBswlSu7fIjGIBsNlxxi1bKCpk_AphL0rJftIbYTw0R1g1xVEUaHz0p7QV_lZsR6TQVnW6mcvp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Lu21RPQ11W2t6_IXblgwusgl9Qmf_AyH7BWB55SluacrPtSh8kN1QbK0e3ka76w0Ugb4NT9IWBOMk_1WBp5iEfHpuHo5CJHbjrTTTjvJ3jbtG1C7CHuXUajiBzpY-_B0k59IqyYiGXgokjl33g0EJGmSW4tOH1df7QztJq8eqliAggrp1TIhK2XjsjON24TIk2k5uLsvFhZGVjCnRtItiwOGIM9AHARNdr7Tp542upTmNMMca1XEi0SXmZB44nut_YWl_wdLAyMBswlSu7fIjGIBsNlxxi1bKCpk_AphL0rJftIbYTw0R1g1xVEUaHz0p7QV_lZsR6TQVnW6mcvp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند.
می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت.
هر کاری که در چهار هفته گذشته انجام داده‌اند، در یک روز از بین خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64915" target="_blank">📅 10:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64914">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SjT-7nYlorOw3N8pOqgGhn9w9-c39FwySDlgqx5HzDo6wR1LgnfPelQtsVwnooa1iP-pmQgHYOEy4QHpadTzD6DgxrG_418iuUL7guu3w8wv1bmaIA_t_d7aXunFR9ndAHI1RLXi34cY0Ur05hsbmWkeOwpcUNO_l41VC7VKrcDokQCt_-9eI7CGQiDuAQZV9tXZfcl_mmORoNAOFb0iVrMMPr-bLm6b2jnjt-NdiiRmYG9w29WtavXcYR6l4uERW3ZypsGa6H5Br86LnBggrbr0KBPa7l7neciD_nYRHbBbl4mSvif_-HNf9g3HM7UAx2d2iq8DAtGcSEoccx8cGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6dnDpFukngccbhQPn0NGjgXwReHSCxhq7YNhhNO0UX4sKg2mDu1sMfQzn-FWKDIa2SKECLSiIZ3bN-qtBjjqCe1XCSWzD-oBoxGfmBkjAM9nBPantY0K8A-lKnbcHvBMPGQajUQUvprUhKNk-af2LjoUHcK-5qujWvcdkEPjjTsgvH88IMnBnrOU8PIbNUkCaILxnnN92m0sHiL-1zSeTDVo2jbUXHzr-MOTg33_VJgP70yvpv9tlVj3h8fMVofmQ1MUkYsC1jNFOl_fYKws2_UgTuEHP3swCEsVkvdAh_KWXJ89LWKiaJcwxL2TBAY0qCKTP2wuWIq3nkCSDyjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=FCaM_8NDymrl5WGlffVj1HeYJTOfAFJJUWoyqRJ7QqfJwx_jWgwPcBGKgfmIiIXdzyT2X-Hy-Oi39451kuuW5ccx9JkhX17eV0GBCEh745vykgDwFhyl6jCtzbacRBNwPxcBj51_crro391eayEJgmqIycnj4wnZjsw5uapNpP8ojAyT4qQh4-1EfmIfUhgpWORhwM1VafnLmdravEds3Xx1-BmsPFZP560rUuDZDTZ-_0W0eDj2dQKQwIvASFVsDyNIXZbwy4m4ZZuDIU2zjOJYmsUdf3Q1NLRl0lzeWHNmceNbD5x5z4V_BK34QT1utF41GkCUY77T1sJRn6kHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=FCaM_8NDymrl5WGlffVj1HeYJTOfAFJJUWoyqRJ7QqfJwx_jWgwPcBGKgfmIiIXdzyT2X-Hy-Oi39451kuuW5ccx9JkhX17eV0GBCEh745vykgDwFhyl6jCtzbacRBNwPxcBj51_crro391eayEJgmqIycnj4wnZjsw5uapNpP8ojAyT4qQh4-1EfmIfUhgpWORhwM1VafnLmdravEds3Xx1-BmsPFZP560rUuDZDTZ-_0W0eDj2dQKQwIvASFVsDyNIXZbwy4m4ZZuDIU2zjOJYmsUdf3Q1NLRl0lzeWHNmceNbD5x5z4V_BK34QT1utF41GkCUY77T1sJRn6kHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdTbKsAPfisfjJqYMLOIfCP41uqN81YR-QusyYBlQhH7Kh-GXI-r3dxuVRF1M0QN8NggU2hYtokdpXwwVmjC-2dK808bvZbDByGf-U0I9BgZU50eiPr01CFzZ3gi6bgRY2xn4ZRaroc60jlQbNZ5Fq9GYLvk7qeqXv-eNDOFcy4uCO_d8o-1I09fwGCsCVqmAtskPIfPhDZE325VMtoIl9bb2ye9bZGWHE9eJc2ANjt7HNnP7SMxkpmvu-MDWbxw7kBO_CS6_gXK1OIP8dnexBFlW-tRG-31L1BZ55Pkd4pd1jE6h8ik8xWd1aDdC8StZGGkBRdrxjvhEREqnmlFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1Nxj5oHBuYzLd6dbYcXhOOdPKX-htAuoU4xBOy60roX3REfWWBijF6lIn_FpB0s7Iuva43vA6DcQtW5668w4jLycYTxeyKoQcio__LaXG-fqw5Wrs_11mbM0R5hBqeouYjK8ozZFYoEaycdyHgLaFd7fsbL044SJCWilW7t-ISEsD3qBkkz7Oe9lqaZMq0yy0XUla1rQpiReqBLkqXOrP9lqMnQh9siWpUdiKir5BNHaw0_WpVxxKraaB-bQfBiQept5Qjq-XAaYtjFa6y6yWHuDQsEtRCRbTlI5ulBC5f4GUqEdI25R59tWqgTiZcj0QXTU0B2GC-AmrVdeE4Kdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnre6Mc5m4eDiCkZ8qCQAA5E2xBjfS2R92ph3jRx64DmJBCHlE6G5TdUkpWl5-yiEVxcW7JQNRwZno--5xQZ5Wv7hPGEFJ0aJE_P7YcEKB7O3HJpdZVjGOk61xEobg8cknCl7LRTxB9xTK_ew2yeABZzN4KFicoXPAFuid5kQKy9TiT3aQ_-zPU0H2W-LKzqh8moGrhpiPiT0oiIDcFuu_BlYGZD_JadIDmrHSHJL9XF-Ap3N2qH8gDj2-qNsOaDkCsEVJ6CoRkSp7lPypN_2-6pkDI4nEiK2OFmQ1IzbPxmnYqlDxVzdYagh5ABEZJr5mBiElK-XaXGUvGB2WBuFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=OrCgvwJaZi07zmNp35D_NzD2v5t8ThPgMqhGjPplBiBpG2oIEyZegbXfKc_aLZgI3k5Mw66s3azqk4tQ9VsKULC_nmaLIxtsWEehyX_QBCHTXMzi9CC8PJXcUgm0OgWbhyIQlLFm1uNTFf_XOwrEYeTErMv9Beqw4OxY-oj45Z6k8y5tOoOFQEuFLi4DgIukclYCWLh13dBziy5zk0JRriqou4QHrHuP87VCODd4i3TIuPIPnsF7aYGlt3krVFpea21nBwU2zfHAodC6M-Ditg30pJvenD_KJrPL-yQuAS2nZIWQqnReUXJzQ7LR8wr_gTMKDoEabdbCFWMeNKsdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=OrCgvwJaZi07zmNp35D_NzD2v5t8ThPgMqhGjPplBiBpG2oIEyZegbXfKc_aLZgI3k5Mw66s3azqk4tQ9VsKULC_nmaLIxtsWEehyX_QBCHTXMzi9CC8PJXcUgm0OgWbhyIQlLFm1uNTFf_XOwrEYeTErMv9Beqw4OxY-oj45Z6k8y5tOoOFQEuFLi4DgIukclYCWLh13dBziy5zk0JRriqou4QHrHuP87VCODd4i3TIuPIPnsF7aYGlt3krVFpea21nBwU2zfHAodC6M-Ditg30pJvenD_KJrPL-yQuAS2nZIWQqnReUXJzQ7LR8wr_gTMKDoEabdbCFWMeNKsdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KWktTYsV6maPzu2xUPEIjdAYeGawvoAW2wTTjqzGdpiv1aVOJDkV857SnxbcY4BGOl8z1CmF4b6X_rBARUXI7_1BvB2TGPaSjlyYMz_oZWWPCdGG4s-mX3r8dpRWgOnRfMf7hvuEW27LPGmmOwZIm96b7NwESh6vKTPds9KSnWbi-kBwU197Y9xb1wn6pEbnAwz16__TC4sj167ASi5tbdgkaBD8ryNScn-8wZNdokxS_tUIXlBvXn_6qjb9Wy2SXsZL47KyzfjxJE2WjU2l-HjH-wDpCKXAfmFppTrS-cJRFjy_wsGfraMGh9ubB9CoibQkyEAprAwSuZg7h-WVJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ie0IR-in4sD2qWsI6XWfLhG8hG6feLMjhwXFFwi1dDejNCIshYz6rN2_e3TaJs6QNCu4IaZ2HKxnZoDbe20ZyIVwPQd_PtWeek05OmTIJ29Qo77nQ-IGfH9aVuiFJQgDV1Hypd85A79K1gaseOWpg2iVxUaejg7oPU3dEt3XEIMjFASZMkDMmBT0HtI51ClnjEzGgMP-6_M7mUtZcYh16wGEtDheBysb4XfXG0jhzk-1zhrPQmQoTPeMMC0oAJdOu2qd-nBRy-QXcXYWyTUCLX4BdsUTtRtxl4v7td2iCM_YM6dwKe8TbsuhS_uIw87bh0GtZZqhPU4D-I5HANb3eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRrZ5rzGH0IE6sNsyDSL0agjGStqFyWczg67UJEQb0oWArmb-GXHYit25Qup7d-Snxyoe51jlZ7XJzdDTJ3rrN4HrF2dnkRs1E9Y83DFNQor_WuD3wGHh0fvswgyL7yRH1TNd0yJkCMUSIXJrVuDp49UxcjMM0DDjSsmno-FaTHGwpxN0zmmKq3pywOxOFrHrbBs3gVkIp6mx72aWDBM1pgTtMH3uiQHoPAU-6VwJaoaleeJpBNl8arU3VIQ5qnmZGpPRItA0OeqV0hpi1bP2iNkezZef83wgHFUfqxg5g7BhUW4nLgTZRWiEZgx4gJSyeGawP_h0CwBxNBg_Dp2aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afadb-eOxN-6JUzXif5hVeO9OL8F6emYVgHnPe2mfsgFeucVFkFqdVShWBvObjmfg1hX69iBP9UHy7nxJBsTFn8UKbcqEKjati_V8Wq2Z02H2QEEj3AgaoXDHmxHYO82Kp3EMG3CMtTIQhK40NRWmES1jG2tXJcYHtNcfzQWqsOJPE4F68WG2Egs0gQralSserbKXDUwSmuD5-bN3SlMsIFuFgANl_8FxoaRcxbBEIywLwI7t6BYKBW9EGM69oU-gNy52AzhBTuH7qzt1MDTNEk0HI2NF_v7Di_D4sqM5vkPij6GHEM8dB2yKcbgtY-jiEz2X1fYuVgQwCwhpkmxFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jyrg2Z6eVXQGKR-t0213GSDDeYQqIknqPbAPnh8KCe43APzpHMVKvrdYEEKlmxOecAh4Q1JZNlQw2EXjOFB2RzuaEKFlozcz8W29wNflRJIOWlzK4dpMrONIhaAF6LrpC5H0W2RoM_qr3rvIlkUpzouzPEpMswOb1ZgwAsdrvxj_WPGJdmAs1P4ksk4q3Z7-4D3g97wcyd8gY0vTtD-9e0K9V2tAY_v28V7zWHtq5qFytT12HHgTJVhC3x0RXHQ3TD88gLy5AxTwDqSbbT669aU2o0cPRDvh4zGYnqU3ifoWRrMfkalpXbMRO1x4MW0Qg81JgHvZyKt1wZS7ftbiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Syfcvw1moZvwByJHzrSoVBBOnGmrIxtYIhET3tIb38SzlI_KmTo6c5NBjXapyOAbJMs9HqZ5QnkRVyXrGRQG0umMpLvgz-6O6oY3YMyOmxEJ6WDGl-8Omjyo016A8jo2o9JqtN_sSubZgTKMs1eDtSa5A70tJYjzI8RB0P569FJiq8444m3A3J2ccakBWu_7LGVOHCVT2ctiy-cQ0O59WLbayrZKhm6p-lJGMxkBIZfrOtVn_YHByPWy24AwQaUaO1mQ0lmbSBt7pLjyZ1nEHmpdKim4oNgFMqUULCiGd1xh7qGdPZpYYpHm8Zp77Lh5_64ukuGkRQPtKi4yEW3v2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=oKGXia5CP8vkzS96ZoBPe6Uglqtp_-FM052SFsZ5RnZJ-lekLtp1w8HbQmi43lMGhu0Y9zCm3YzeN_ReexS_n2IKsjYhXSN9qpAxtV0VOy45n5CjTAWvu-fVmtk6vGfobzg_0UX88Kxzxd-jJjUz8XdnPRi5gj-XbSImDqRYYdIKlQFsx1TtDTufcGpOqC5FU3e2veiGU03Ys_tCoehTTL_Ch-iJaxuuqBK9rtn0P5Eu3yyr4C90LgqTC9ru97tbG9NjXAydMP2eNO-R7FpakiVtw-p_P_UtVIlAgUW1L-qu4PLbK4c2gUSP1G5mbtFx-sdeqZFu1JM0OrlIyb4K3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=oKGXia5CP8vkzS96ZoBPe6Uglqtp_-FM052SFsZ5RnZJ-lekLtp1w8HbQmi43lMGhu0Y9zCm3YzeN_ReexS_n2IKsjYhXSN9qpAxtV0VOy45n5CjTAWvu-fVmtk6vGfobzg_0UX88Kxzxd-jJjUz8XdnPRi5gj-XbSImDqRYYdIKlQFsx1TtDTufcGpOqC5FU3e2veiGU03Ys_tCoehTTL_Ch-iJaxuuqBK9rtn0P5Eu3yyr4C90LgqTC9ru97tbG9NjXAydMP2eNO-R7FpakiVtw-p_P_UtVIlAgUW1L-qu4PLbK4c2gUSP1G5mbtFx-sdeqZFu1JM0OrlIyb4K3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flXCW2x9RvAQtajbs3HqViyXcVmAanoIX7Q4JNcC2JGWt2fAnge34DukJHHvifMkQSIfbAh2WDCi-svuJ08uf8NtveRmPXhN35PS_aeRdB7hnASOMUwUfPG4g0OnIqiVlBVD0yOPZU1BfrqZkYfyf0kpITA279T7Jj_JVyj-chXrUVxmzhZthjwh_y5LEKPZRmm0IosJp6hxc5qgPCcWaODauP27ENVG1YGXVmq4cJlbgt_-4YFtfVfIQ03G0_2u6BK9qCOsZMQM5Ch1pHR4JssC4aO4tAXDP5Y9_pPQFIGW6mlvSUlvLW8stKH9xDp6keIRUugSwRZg3CSzfUyG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FU_bh9VFBgnsBEFY1SPTDOkBeR4yrFXnXTmq7HqOyZQximltqFrlc7WpdQP8OSXYUcu9qPa45GsxnqscDv_JevaeqWMmSkNQ8SK_xOz-AqUFPEmp-RatNYWjGvOj7lIjre7bhE6xdSEZTFQihOQGt9VQYROPRefI-2Q5KKKOnWXa-8JVBpDl3_Hzi01jyNFW37OujJ5nptREj2rQPYrDfFjH2MhLtfLgaClyydpEw303XFD8dHg31L1MmMsngc-7c28xO66Ul6LvUWQM5lz7I_CHB21Sfou0Qc5BNLz4G5-JnFR3Tqap2Ix3uVpFOPaikKgO5A35Vp6UAGGPC54nWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awc8EUYc-yqlmChsN07mCPQ5inLL58p8M4imPInvNMJl1T81_6vReruDpHg8KcrSt0RraivrGAaAC7HX4U6LSj7BrLhvi-bdoLde79hxaeOjFmrg4XSetvNk4-OIdP3amJEpXhM1VhBE29--iSLWKBGyR8iTnt9LnivIT2lT2st1CL8oAzJfOMxV2bGjnTXg7riQC323cjg_MMyg5EUBHLzEwVqw8XJ67kjEdILXJFuIwPZ7NZYFQnngGLX84Aes3XLm5Y1XFbAt9bV8jABiUEILD_5NHZDeu29fkNBIMKZQBLt1j5P637elMzFYnnMnKkYbnOPzYjFOcvn2UbHLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=Pu9EAJOs3gwQ-UUNReG5iA6oMYzoD-siyxv1gaQgSr7KrtAOAopwrprRrJ7py33Kbvd-hL6bX2TYGE04CD5mC5fiX_xUei1DyBqpATkyY7VHjTvA2sduSoFsi6ybEjNOMHM183RzEEK2Cs1RxlEq3J6LaNeQ0-cVA--SmVCavmgDHCPZxTgsiQLNMtPr9cfonnzk5ctTkYEHKypxWybPf5dIoLv9J4B5Z6bcfzMLNwbvo2aAnG2Rva-axcVo-V_ZFyvRGJuSz0lOU7jihZjsNFcCuhnO3GVAS4rdoyikZ6pXWILRXeXg0Hvt44Fo0NCNiW-BAXrI7erRbZYdTnl1xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=Pu9EAJOs3gwQ-UUNReG5iA6oMYzoD-siyxv1gaQgSr7KrtAOAopwrprRrJ7py33Kbvd-hL6bX2TYGE04CD5mC5fiX_xUei1DyBqpATkyY7VHjTvA2sduSoFsi6ybEjNOMHM183RzEEK2Cs1RxlEq3J6LaNeQ0-cVA--SmVCavmgDHCPZxTgsiQLNMtPr9cfonnzk5ctTkYEHKypxWybPf5dIoLv9J4B5Z6bcfzMLNwbvo2aAnG2Rva-axcVo-V_ZFyvRGJuSz0lOU7jihZjsNFcCuhnO3GVAS4rdoyikZ6pXWILRXeXg0Hvt44Fo0NCNiW-BAXrI7erRbZYdTnl1xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LDSYfFRgfo8d0Lasi8Qpon84YR33o4IosKLMuViLtBwVCpNrgNIUpxV53qaS2zrwWCsg9tSoU9SlMnzagMDTxtRySA8A9gQvxlNlXvzrw_ZzNxQP6vtD_oIy1zGM8chwymfkMJf0LbCOfIG8zhmY5hZhiaft3I6FlSer-fYvCKVEr8_IBR71wsFg7htZt8mm87fzKBAEBh3XSMEUwzps5CLTe4g4WqcTmFdNNVskBwPrcBD96nmqG5ZaqXarzEhbDGEDY7fEKn6lohqpg_WiSQa7bfK-Te1taAn_LAcqetl8w0JhwNohiocOysxCrNmiz9nq2ANtq5Ha5dW4Aoq8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=LDSYfFRgfo8d0Lasi8Qpon84YR33o4IosKLMuViLtBwVCpNrgNIUpxV53qaS2zrwWCsg9tSoU9SlMnzagMDTxtRySA8A9gQvxlNlXvzrw_ZzNxQP6vtD_oIy1zGM8chwymfkMJf0LbCOfIG8zhmY5hZhiaft3I6FlSer-fYvCKVEr8_IBR71wsFg7htZt8mm87fzKBAEBh3XSMEUwzps5CLTe4g4WqcTmFdNNVskBwPrcBD96nmqG5ZaqXarzEhbDGEDY7fEKn6lohqpg_WiSQa7bfK-Te1taAn_LAcqetl8w0JhwNohiocOysxCrNmiz9nq2ANtq5Ha5dW4Aoq8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEagcXd9GN6ho0_2T6XdEBfQ5kR-dhu42WrgKg0PCSkSI6zWvB52E4swURvKG-RsFUjEuDj70VeUuMs-v8unPAN1DwGDUKy27gvus0I_GUI9oA08QuUmo0DZHBKvFetyJmqHayfKIqGmOVm1ZwSx8OGtlvTctK6ie7Z2fCL6zLdOMjVXgsK2ezBkgqdsGRPDLQLWxGfl3uRPWARq1YltcfN6Y316IfCKGvZeNzo-EO9uaglrfXFbY21iPK7K-_8Rftqe43ia22ssyHkt_7ekrp7b2i38E5_M2dsTi9i7duHioYIGL8R-alzaKDChwPiirAkQi1oxW7mlBy34dle8fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HPMlqmr6gbadWz-fIx1ZjxgC5l3i5ENIhQsmxG6hVe-vUh9B7rzqPwMgyuvWSxR-CgaLW2HMIADL7hXDrbux3FYulsZWiDAWKHFcQhae1eySfh7JG9EnnekeV93bLLz4H79M5eDRVzflIDpztWy6KckQxAGyYTux8I-EZ1GkW4vOeoIWC7StwNSf7evVdMJZUkb3jSEz_i1ZIUS_eHkz4Sp6zs5N0JbR-pGHNYLL6AE0Mnt3-164xixluo1O7rm58yjzi23tnCDs7W5maWgL9m6jGkggAJR2o9wKPi2u8P-JM0iRFOwVT26zLH6L4hOFAVLuVJRkkdAEyDZftk4Frw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdhEbV7uyCQHO5EsjWf5HJGLXCM9_BRs2RJ9eCeprrCqlvxeDn6OQGQwTIlLQZ-JQOBTl-7v8DyF6Ah3BF3AxMTTuet3ILhlsSN3oBTyZcq8ie7lc-n3q72ZBTma_sAa06lqOCdusURtPKG9-bA-_LsxRYAIF0C3m9oRAv5tySk6nDQjcEwUzfKF0VeQv80ItYGTEukFhhM3ielLvwTpMBItIN6BBVNvSRAxkCj2RjQUSFWp8Zju3XPg0APIcM8jKgYiodDX2PdglUWfSosdXjYAKIzr3IMt6WwWWM-shbVT5c9wfxLWn3yWP9KafbZsEExXMkugyZIWyYkpVP4d0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrF7G6ep-fPUQO6isx8hXvsrprmOo8q2n9DGewHQLD0pcTvXMGPs8xPuDhMHuBUcXe_QpoLRh3aOhBkNMqMP8WDBnBK22dF0osSwr1UvaSWRsUK6OgPDhF7bhbzLBW4jAA2RmrNr4piH24KW34GaoLLBASUAFw2HqI3V8bd2iPLKPkGRkDIuASJ66ov6iemX14LIAUnBDO4Us33-yuNSwcwnQkEhcpvFkMjpgKGpKvt_9fVTI0gn6JYQQiOVn7aNuUdfnfmsOr2la6v4z1vTahQF7ckFLkWOkV3PdCdt2GlVP5FlprhF7ICJTUCyFmumRFJIQOs44Ehc3vxl-S2lQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwufz3-edwHcqgugFyPl8LycbKTJMMmiSW0wz3ghUALtGwOQvJlWmBTg5Y-R8XIFJpLLjBjtXvs4ABw76yP6VjeYfOjrxf_oKZz5X5S3zAj-DiyoVDulsp6VWbc5T2iZ5ieAORAVu3MHV5PgUSM5TNdzWgWhqTOcgmNyi7x550YvPc_F1cpwjEw_QrkjN67WfeM-LIjVhEP-PXZLwXtfHioiV-sMMoCUCmwskKSLAhMHHNAtimOBKamqiytzQWwvO8adnRLrfJheVp_zrnsMzAe6tPyk3QZSUQSkzF7C5vNFJl2PqNr1Okeahs2S-T_Xm1TfU1aJwx51HinyqA2AKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=U8qkfnudGDBlRG1oWw6PcCuFVWNGh5DLJn_OKX1wtzwR23PULrNmDE4Y9KUElcMfNz5CRP_UX6Ep2N_W_PBFtJHNJ1C5JgK91J7phjWqbtMjY5WoJTCnDZTAfeGCAp6yX8FgRI2d66H2v1UQjNk4xKOA0DOby9JiEI8Rm4hNW9D5h5d7FrInMsC8FtOcujDDUHA_uNG5hBnxLynqA2sUPZOVH1QSX2Eo3jiZG4HHk_mE_PLU-F2BjLQKD3h1xyIebBwI15jgc_dMo9ApA44TqSntoylD-v5ZUuZzLdZaEvP1naPp_JNeTKMgzn9GtbvSain4WF4jwP44ig-2f1skZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=U8qkfnudGDBlRG1oWw6PcCuFVWNGh5DLJn_OKX1wtzwR23PULrNmDE4Y9KUElcMfNz5CRP_UX6Ep2N_W_PBFtJHNJ1C5JgK91J7phjWqbtMjY5WoJTCnDZTAfeGCAp6yX8FgRI2d66H2v1UQjNk4xKOA0DOby9JiEI8Rm4hNW9D5h5d7FrInMsC8FtOcujDDUHA_uNG5hBnxLynqA2sUPZOVH1QSX2Eo3jiZG4HHk_mE_PLU-F2BjLQKD3h1xyIebBwI15jgc_dMo9ApA44TqSntoylD-v5ZUuZzLdZaEvP1naPp_JNeTKMgzn9GtbvSain4WF4jwP44ig-2f1skZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=tuIkTydfJkq0QdIBEJRMqGGZ87sWdalvgBT-hZgayLHa_IQTK7T1ejYIO57Cekf2whWFWuPyg3gMATYJsHKX2CrsbnW6VcwxzE0jvMt8QYK0DiMOr6xkUCBa_CMnZA5kfA4Zx-90M8Y_40mhdGYdV8xG3u6K3szBUmxhqjOHfBc-ScK-yiklZSlvy5pbGGrv0eS4DeAxiyCPcL733ROAb9ZWIwoDuxb2agqnUPpb4CwoR0AG7tP41YwNzHYchXJKCGqyFowNtIhlbJQJizNRP7Kz6vCUooGg03yjiehc4YclpZ0q6UDqXOrg_QR-k8YlUzcBaPD_yH3KLq45_yMqSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=tuIkTydfJkq0QdIBEJRMqGGZ87sWdalvgBT-hZgayLHa_IQTK7T1ejYIO57Cekf2whWFWuPyg3gMATYJsHKX2CrsbnW6VcwxzE0jvMt8QYK0DiMOr6xkUCBa_CMnZA5kfA4Zx-90M8Y_40mhdGYdV8xG3u6K3szBUmxhqjOHfBc-ScK-yiklZSlvy5pbGGrv0eS4DeAxiyCPcL733ROAb9ZWIwoDuxb2agqnUPpb4CwoR0AG7tP41YwNzHYchXJKCGqyFowNtIhlbJQJizNRP7Kz6vCUooGg03yjiehc4YclpZ0q6UDqXOrg_QR-k8YlUzcBaPD_yH3KLq45_yMqSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OdR6GJCgJ7QsLeNzUMFiJbVzv9OKQ6qU4vov9HlpVQtNLnLDiiYvqw_X1TWSQc_83E57JnziPUAZTVtjQUx5_ongJOHfVEvxFYdLXckIp9ZaiRtU-rFW1TF7G7-9DlSgVj9kCYZ9D2T46UQ4OxkVvLlAZc9iEbS3intjk7zg9DeCLxW4JK0ZCHGQYM2BFbGrG1SllC_ZFYucUpEAoJCTCO7R1kOePnfFB1uCAMh1jOT-tlkPwWuPUPpFpxu52rMpGpYaPQAx6e_KQhDcYIOZfjTC1mTgyjARPIRWbYL_-m379OVCmc8Ws2ONp7UIXq4VGwi5ryxGT-gw54mcgLNLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/J7AcIhNcIZKptwXz5HZ0t72jDUYFPrwpRaoRBwapr8IXb7raNXvOlPi5JNpudTZrzu0ZQCD-DLofv9sqR-oJDfbEd1SX5x2Rn10D7aLaAxz0FsJIbq-3bUl-M6WduqqwayVbB02ixJX9Zi7Rdj6rw3OYQbdEoqRWNXwWZnwyKU7eMF21GhcUXFNdhJKmt2MEcZBE7dyYxIfim3UVUIeV-bR_olWRTL27Xd5kltmPR6QTQLQ_EJ9bYlnMon3E7I-almoBSCmt5tbQQcZqd73xh5c78WqMrUTXvlWWqz0i6GX40NAcVt3ONvT5DGUL-DGCXslx-lgZj3hIpvWAwFltLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leM_vqaJFjG5DzNOXAZVezcBSwrfbN1wYcsyfPqtLrM_GkS9QP4TihNbRuR58mTBexSkH2JKOCdYDOcHqIloRZc_8P1gDoQCrz4jlVH7BrgO3cT7HlFDx3qgsFihe0WkJXjccROArV_q8NZNuITP3C5Wcnggaxrqh-Sq8yYa21BOs7g3GFF7SQIXMGaywbyNKbQbv4-zHMsl3e74xusgSp4JOltUIoVLBOOX14wlQ2vI4a-fD4pK7AadpR5Nv3kJyCmo_kJLhDS6bOJTqeCdKr6votlDzSaFdy2orgbYJMXkZtUC-FEDtC4tuRPGQRO2zAecHJq0ZLthetEnYTEPtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBCu9Z6Z-8yUdsK2ybcUr-546dhpI8ZTAgl5IxLFWLNVndn7N-JFcycWyBiaFvTAMK4XOyxRsgzwE196WfNfmVWZILPb4z6jGH7on_rTLfW406Onj4tZ1M-_r2ys09uEA6qmZUMEAQGYVShXUqPJsc3g5Vu06UB5GKbKBHqWdOgmep7IIt4CXFyvniGO3kUXCz1WpGUB8d-2hcvzsItUz5Ex_6uz97k0eVXzp_cHIXoVgdDrv7pD8YLKhA1g_jbMlY_k4_vQ_DgUAV0OLec42eXQHs5f_ljJbKVW8izF1OwubvHY7vs296c6JIykgmr4R6TDm0FMAsyyg4jjr6TZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=sDfv_zPf08ARqDuCztoi3BNMQqwEXU6TT9gptCt45yHjRbaj3hKeD-g8PQc-F9FufHaCv4SSNR9yMayl4XqO4ZpfhkyqO4qyT5QO4y132O8B7jpxb0CukPsAND8A9yqA9Zbx57Pa2cyNHcNZVRafqgwaSPKQkILkGksNWCbK5Oyen80_EIXTtXK6Wax24F94uvgVZkgoDK0Z66JyY2MxYS_FqjmbPzZnx07dvm8jObxThYo4ekotaxXdrdnyVpX_GpTamE8k8Yszllzo5eAby5plDk7fx2wpmQYOLAwN1VCneTS90P-AhjSRkBXo6upPpqUXQnr1uZL6MBSrcTwClg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=sDfv_zPf08ARqDuCztoi3BNMQqwEXU6TT9gptCt45yHjRbaj3hKeD-g8PQc-F9FufHaCv4SSNR9yMayl4XqO4ZpfhkyqO4qyT5QO4y132O8B7jpxb0CukPsAND8A9yqA9Zbx57Pa2cyNHcNZVRafqgwaSPKQkILkGksNWCbK5Oyen80_EIXTtXK6Wax24F94uvgVZkgoDK0Z66JyY2MxYS_FqjmbPzZnx07dvm8jObxThYo4ekotaxXdrdnyVpX_GpTamE8k8Yszllzo5eAby5plDk7fx2wpmQYOLAwN1VCneTS90P-AhjSRkBXo6upPpqUXQnr1uZL6MBSrcTwClg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzqHWFU2_A3Jj0dOImcrxp1U00Rog5RvaJ0wCww5kh8z5TuISUZ2UxynaxpJ5j9lbh-QVgvTdsuaS9yIHYuvXJLm4k55ZKrd1E8VENnwqXCDifeX45MlIP4orwcMyn8M_MVxhjiX_6XpADtIjDvMfuHLwz8O6QSqPATebUN6yH0XuinSalCzdmWBZWURmR0XT3AY81X8SyJNYLKf6i6LXbg2LvrQ82eZzvAbkG0lJidQzZgRGUsf3JglerDWvVpM7sKgST3lvddZjCMIJroy__LU6tHy5txFLOoFRn0n2aa9pfJCicKC74BvFGSpn2zcAx4DWnS9aaAyjiv4XEbKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QQ-eCPrbapzDWrnYsJq-llCvC-syMTNco3OwVaiZgt-IQ_ARR6mx9WLjaxssUH7N8HY_Mx-7yDCyNo3zZNFYCillxFuAjKLd0ffXFdkCR8mL9aCmt2PkNvs-CyIzbA9pgnw6fgOnuVAIevK2pGR3AqflsyGbTP5xMadrpssZv9SztUPhg9akdc8GGKODY6APz7Ywwd2uC3LHvkGYvk_6BEPLoID6WTWiZkDsQmBrV9fuP2V9p1fIxLJXWka7Nqj2-1eNjvM8-57pEVmoNX_QEO1xHV4mRybpNJW4x52m_QZQ33v17FPx02NYULLZvOx4eE-CleSokjiHcWoZ4thOeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QQ-eCPrbapzDWrnYsJq-llCvC-syMTNco3OwVaiZgt-IQ_ARR6mx9WLjaxssUH7N8HY_Mx-7yDCyNo3zZNFYCillxFuAjKLd0ffXFdkCR8mL9aCmt2PkNvs-CyIzbA9pgnw6fgOnuVAIevK2pGR3AqflsyGbTP5xMadrpssZv9SztUPhg9akdc8GGKODY6APz7Ywwd2uC3LHvkGYvk_6BEPLoID6WTWiZkDsQmBrV9fuP2V9p1fIxLJXWka7Nqj2-1eNjvM8-57pEVmoNX_QEO1xHV4mRybpNJW4x52m_QZQ33v17FPx02NYULLZvOx4eE-CleSokjiHcWoZ4thOeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=BGld1hUOr2KigADEHBeft3kP_Ke5aSzK8tteaCjUv4XE212fwyHu09vhc7Bk73ug-DjaIPkeNaJtVJBrOwsLzDc6yn2RwMMTAr3VXjngMdJHHp2ElU2cfbhNDwfle7-lkgbEOTtPmrF-9QIVTf5CbhouLE0fOMwBe6AyPMgKLJ7UYJmTo___qgrBSLvrY8mzyzkdjXOm33ZCHtmBVMzMa5BBUEHOECwqKTxMd3N85ahzN9qxKpN5TRPvQ3vrZHmmkcODA5i3y0Ke0SQr41001J368dZWDO4bCIQfhqv1o1a-VVaGHkFj9b_q67bQh_pBzNDez3xxc1p_pPVm4R_uMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=BGld1hUOr2KigADEHBeft3kP_Ke5aSzK8tteaCjUv4XE212fwyHu09vhc7Bk73ug-DjaIPkeNaJtVJBrOwsLzDc6yn2RwMMTAr3VXjngMdJHHp2ElU2cfbhNDwfle7-lkgbEOTtPmrF-9QIVTf5CbhouLE0fOMwBe6AyPMgKLJ7UYJmTo___qgrBSLvrY8mzyzkdjXOm33ZCHtmBVMzMa5BBUEHOECwqKTxMd3N85ahzN9qxKpN5TRPvQ3vrZHmmkcODA5i3y0Ke0SQr41001J368dZWDO4bCIQfhqv1o1a-VVaGHkFj9b_q67bQh_pBzNDez3xxc1p_pPVm4R_uMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0YfTicBVofT97wyZk_QLC7a7o02rggIwOwRkHmAShbLDJZrXybDNpI-fz3y-3bC7WUNEDw6jA750QiFvW3aJMdpiLaa2VzQUUgOdxi0JjoKzc9zL4wmyoz_CYKA-c68RLF9MbYtkfwTPFiRJF3sDm4IIMpIhsn3-DjV4qSCcMx1Uk5H3z02IJB5vpDXze27-QsoTK1WcIpSDafs38PgY3SEujYeHcgV8CmsBtCjRNpvXbMtMFhLCoW00oSXcZ0bAmf5qWpPTmNYWLWZv57Q0JUpWHCnjyZkbwcH-9XmTe0FCYnqMRtzbAxcgh9LPhuNssQUQabyXEidG3oo0LkE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iKrb55RWcRDljJ3UhZSuh-aK1zBBnXdmoYWii-yBRfk9PLqcRxcgfBUHXkOX4Un4_fI5E3qSBC2Un1QGMuHE0S0FpjRBSab4BAdXa5TY40g3j8hHYmM7QtzdZWD4fQpfmXBOnEHiCw2_zYS1qAsNTF6GVnkz3QDuZO2F6cqjSNJczeBxE7OzgiuG0_dc1Rx0BhrU2_pC_EbWPUhSyzkuc9BfCWeoVkYmY7WpL-6omL7Gf5nXYTb3vz7hYu2m2cmr1acxucJNEkZe4SI0I8gQJ1ZApVzG2NKPOqZlyq5dBob-MYBC61ogSFI93O0TRfydxne-HHma8jMpuv7HtMHtEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=PwoUSzFJQy57SnZZ-SPWuxPHomwsKyy2bcrVecxp707PX_PA0Sy8-jq5xN-qiH1C_1e0CGLByhkwy0vr9M4HtcfQTd-IFftqBNPtRiNxT1dyRqNwrb4EO7JL1fdhzq8iL_cjbbBteImZFh4tom_CDvPMyeO9fU2YO8ryXx2ah5wzpnLPUVyACIV8Ti67yaCRehFaqJitK5jhncY_rxA7Z_Rgohc2lUCR4dhbIaKolzTkG_oCtCXtowoXU4BZoCtMlfkQHC4tQRmndil2Rt6Vf_NCgsMM8dX4X6ZJqrjrkgcd7P9PoB0G0bFayUDhVs4LSoVvXffdR4l2LTelfJXCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=PwoUSzFJQy57SnZZ-SPWuxPHomwsKyy2bcrVecxp707PX_PA0Sy8-jq5xN-qiH1C_1e0CGLByhkwy0vr9M4HtcfQTd-IFftqBNPtRiNxT1dyRqNwrb4EO7JL1fdhzq8iL_cjbbBteImZFh4tom_CDvPMyeO9fU2YO8ryXx2ah5wzpnLPUVyACIV8Ti67yaCRehFaqJitK5jhncY_rxA7Z_Rgohc2lUCR4dhbIaKolzTkG_oCtCXtowoXU4BZoCtMlfkQHC4tQRmndil2Rt6Vf_NCgsMM8dX4X6ZJqrjrkgcd7P9PoB0G0bFayUDhVs4LSoVvXffdR4l2LTelfJXCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=DC2YkK9YjC6UQiyWsJp1Fx7MvFwjACJ4N2vf7SinRAQrHUpcMIbQqkX2EjPLUYQHzorvviHFIk4YRd9vYyOgcflyOZCVSPU9xRuL6GSfv2n1G4bgv6hs6TgEcsAd2YO-ZkUXHRhfMpZuLfrGE_iStM4NpCc06EMuoPYUAzms7uvR8RCPoKtVRZjguegzEc6X3-hlbHZoRTrTmcTcnGaey6lZe3XY2prxRcLikVR8cTWzHNq5K0nKxOMbbicqKBLLPJANytdzfCQUNJgRTavR6gijPfZFtQZinj4TRKyywnA-qFDMFj48qvTkgOAysIF0zKFw4d0X2-PgYphxH2hmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=DC2YkK9YjC6UQiyWsJp1Fx7MvFwjACJ4N2vf7SinRAQrHUpcMIbQqkX2EjPLUYQHzorvviHFIk4YRd9vYyOgcflyOZCVSPU9xRuL6GSfv2n1G4bgv6hs6TgEcsAd2YO-ZkUXHRhfMpZuLfrGE_iStM4NpCc06EMuoPYUAzms7uvR8RCPoKtVRZjguegzEc6X3-hlbHZoRTrTmcTcnGaey6lZe3XY2prxRcLikVR8cTWzHNq5K0nKxOMbbicqKBLLPJANytdzfCQUNJgRTavR6gijPfZFtQZinj4TRKyywnA-qFDMFj48qvTkgOAysIF0zKFw4d0X2-PgYphxH2hmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSLnmbCTGS2VObpqm7bzKumlD5sX4zK1R69pvkLYsCl8dx_V_jWci6Y5nLwpszU961Gu1wyyJJEh8JoMuXDDq11uh11MtXmUVFlz1CkDEnpxucX7gcdrBFDTaac_XoFvgB3iUSd9RIGMxLOuUm2sUSz3cryjtko45-95RPPP20AdxNXBU1UE2qZ1TSlG0dVeGntGWcHjw5ShE387XyJw8hWTcrjwuJ-xNa1OALun6FmoaO5oS-uogRYB6uoNpL1T3Rv8FFfAyrqtOlRZMzBqHolZP_Ql_FolTZxyL8OKJVwJGRSVfZV1WVxv8ZEl587yMdp0H-fYvihgSPmNnrzeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRGexGRZdnqSwBI06DFQ1H24NeIdf2MuknPDwX-S09vTVyBtYFN4o9MYD1VwXNQPe5-HLjRREtzcBXqOzl352uXjclJ4K7luojVhaYIe48eEQroon4BppkRgXU1tyWMvyq8gYMtRfTGxzzhRTzpt1QcsuQAZX5-vYRyRPO-EMzTIecdF-wtbpeLvSTfAIwQaRLUtmVayZbiZolGUapdHEOUc1qtFHyQp3d4KuUckx7tLJpKRbpSIrOu4pnShQHyPjwEOIK93AKM_stHSvM3mPwdK-gT0kF1-fJE3QKv3K0vSDdh9cbt8ePqqbVD6HpAQKyHNDW3g1D8JpkPJ7H0z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEsWwpzNy4zzhJqjrDP06PB6wWidYFqWe3RNzD2O1beChEM3Ya4R-xlkG8qpNdwxDjXwJPvQIKgEQX52Xmobs_ZsSNz_F14Wb8TQchDJlTuTNszAlsnb7nlUseVoGDi4yNo2j4Ifa6xqmPZkzDsVTQ9m9BG57SSRUipARiSjrhoksCIivm1mWdpkTRB5wSSv44d9tBsEuNUWjMup2cAiq58TCZ3-eUiEYwqvA-kelli1s_d3g_a9Ni7cZfdTOt6ijrTa0MURluHvmxZSXYneIy-eBeaZJnLoNKtS3044o8xA33OJT9CSKPA8x5qf58sy_SLOZO14bP79kf4Cqg0KLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWl5ESx2UscaIU8ijgfGmPJp_vzgtrpEFSUfayzRO3Sn_pHe_dpJY53JDj8SAMxJIZaZ69LUb0th5QdArUtGBJZSzb4KtQb7geqk4vWqYsTfGMQwAZa19ulfwDZfER60_F6euNrHmXdNQJpumuRtKMyRVkSP_q_Ecm1HAfGnQPxeLcGVR62fhA8TxuG_VbAVK0OwzQJ1cV2KihRzm5AcAcjC9UuxcyDP84MVhibr3mih0na-eXwJUJjJ9RPih9OBapV0hHFNZVFoRsptkupS0ToHXBJu4oYKmlKAZxwTk27xfC1PKr01nq7OwLldGVrhvmGGRDFS9OdlPbhl0fR-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=R06Gx5jyBWAqxeYe6XetN0k-COfTe7WAibCsBcfCLTzhmSTk7aHHboXB5Abi5ZFGUaXWe5S-au5ouNNiK4u5nqBgVdAYJDErFN8ih-ZZ4_GYZXCRdTcvASOQ0asI_JNsTsjFVhg-Zyq4Z081XY1AqD4tlFVdILY3wRIxzyJ8v__A0ZwNI5uZ_X1ZzCCg4qS1FcL3AgrbXcYdskIubpU17IGZ8SPCUB8dXkCRYhq6Lm24BRwMLTKrBpZ446Chsh4OvWfk4dXGZFAQEkqEQ9JIRG_nSXiy1Z1xJOMmUZb7ifP_9vFbfOuo9yvfNQ0ljbJnwCwGajjxREX3jEZCMselXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=R06Gx5jyBWAqxeYe6XetN0k-COfTe7WAibCsBcfCLTzhmSTk7aHHboXB5Abi5ZFGUaXWe5S-au5ouNNiK4u5nqBgVdAYJDErFN8ih-ZZ4_GYZXCRdTcvASOQ0asI_JNsTsjFVhg-Zyq4Z081XY1AqD4tlFVdILY3wRIxzyJ8v__A0ZwNI5uZ_X1ZzCCg4qS1FcL3AgrbXcYdskIubpU17IGZ8SPCUB8dXkCRYhq6Lm24BRwMLTKrBpZ446Chsh4OvWfk4dXGZFAQEkqEQ9JIRG_nSXiy1Z1xJOMmUZb7ifP_9vFbfOuo9yvfNQ0ljbJnwCwGajjxREX3jEZCMselXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
