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
<p>@news_hut • 👥 144K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 21:57:14</div>
<hr>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgmrUZ1Yre1M4d9ZPIctvlD2Z83yu-FUYYEiE5PitQ3cP9nowFzhYr5WACOaDOaFkJZw6rgA1NHnceskOXQAz7Q066Dxc-CeaVcad38w72wENVkTGmIkMYcULrcTeSUxVumd89RmJrFT0a6evpqbxpJqs4rhbhsDP7VlQmHsc1Otaah8DIPAhr8EODApPEoNAGXnNGFLd4bMzIfHW86c8mdlMT0fPPQ116T60bLec5qnAVgfuhnF7mDewx4e-Ij7vqatxC2HWNbtpjDWL691VBPgIRuabhzEgHlDqv35CRxLUN8p_2TprxjHGoQwqxw48T0TfU2-aKg_4t6Y1faEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPBLePufAL-uLBfwCt2dSCHyrdue-5VoGQ2rooCcJuQ6u9nM2ABKWW12HF1o4BTZrYpkzsE_I759a_KqKV7CkcSQ4ZenAiFJcBw6ah0VSefEmqdF86lSxn0pYbKxWAvEssy5nfDwS6DZqpB5x9CFAT8qjZf_sldXpD-q6UsqNBjnBnGHfmZLG2NdKIDUjlGqTdKYfbgfgzMKvDdK7JCIdf2gtRJiY7eaz4yPp66yd6CzWr7uuNNe-6Hl-kp_9BM52BC524WnpmRaSSolvTL5lmm2dfligjqsWtKcnl5u36uL0w0G0LyLWVKdhmjUfPyaNA3y892DfGgYqhAfu9_0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0e7TY39qUxSg1bpkG39JX-ELps6sXz0sKCD4rMqDwVnGaGU6AwH88TLFr9WJS7lUlJYueEVk3c9Yn_g_9NaiL2gsIf99XVLD9GfVH2akTpcARtbxjYX91S7fPE6wc9mVPRNo8eV9LoxJ6jc6FEvMS7rLfiNMJWFhelJKid906YmMheCU46lXBmSR1ysKekqwAQ9wwac7wZWa3Wz8de7BCwA4dDR0a7WT68vWR0JdTnP1nqj7x0EircPLAiGdR0Hkf-aloj4PK3JnAWd7xAfEbh-xSKVg5C9pNLBkKv7DEP--e0dt1RTTLw3v20oDf4MvYS7inlE03KsRAE2KUW4ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64952">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmu58epFkcfCr_UGg4fWuuwjLqfTKt-nqYataDaKirAb-zDmyf9NN19aOe65JGiNR7mkc1JEEL00-4iiELZ1IYcAjm97-xj_FymFTbEn4QNdTuzhJbMBGFd4_oe3hCH7cMywHEcIKP54eIQJaSjfBsXy4YHFMsY7weeWuInrjto9d7bck_8LVAFmeFMkRQqnQ1flvYLXQtuth7-qViVYHPCKFTptq5QL725GeqBh4LiDfs6WTdQmx0hQHV0qPmPmVMdoC_qpm45oeIecR42ayLXPOAQ7JyhMHg5NGGTvKleq-odfYo7SjkWy1lyWOAbW6V9QRgfPCVXbApks7QtmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VbmlOV6y7DVyNi2Tbfid02Zi4A38jQIoMtfqxKnangRQusGW690jbGA7_jExgJ3LWvxUFVkDInBY_Ue6FOIb9XmNflnlIiqn8enHfbHZLvOPUa6LcrFDhFo7cUyDjuAqgy8ijgwJalV5IdmiZXe5gkKDNdQJRhshO4ScH6Q_V7OCvRFY1x2jipr1miThYVKGrndZHHrnD9k2yZZLFt9uH8k4F2u_d896VFWlkuSUCVEtoQO9eNraE3W0DYxntFH5dZaTdekbCYvVxp1KTEjj4tGottbPgo6cM2eECfnLJwV2cWS-NfP6DZ5zaA74Hvh_0ox4eCeFPqopVh_UreQ6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAtaJutOjt4YEtFis2-H8u7RJYZi0eYaubygoiSKORN5J0JJZjxzUAa4ML6iNnqiCXkvZGVx3PCrZ2St4tHQ5N7R2YKrDMOjUNBdD5zvtPboC-AEgEcQX4JKFjASwAlzeING4f_jRhru2CsTZLLEp__72vV8JxnuZUojCiI-GCIZu1Bq8iTY_uogdcbBfdEfc6zSz0N44j-AiB2fxZETfZd4aYRmkhnMIhgQnYkki6tJN51vuP2yKzRXK98yS7uxnc5L4n5hPeSTSV9GrYR8BPEbN7EEWi_NS1_ffjwSPC1BCvv-RT0pJg4KXn0dGktknObb9mtSXVAf3pd1z-yhtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=rW3C1ejYoh0yF1I2vKTXCNHE-Q13tnjTqbCIn2pUY70WKsuLvm6eUceBJSlbuG3bzS-J_Vp7T7bdLvepJISL7g3RpztWzq2W8Po0yqucfalaUSZ3cbbMMxL2rtkOp9hKXWTqNQ8xTGylv-vYaGGLd01NbSPtY3F1-3i-DpEO7ZEidkHwlx57I2MYrx1l2p18EEyrRxSH7MuXM7YKWwuDqjTp8oO5lA6IzfP4ov1RNVLb9faGn-ichtzwQagVo1JKMH-_gieS1mdClpBy9qlBHmL4fXKDaoscB6jEi-jsdLGp72ueMzO4f-svvi4ug800pbIBzE44Fjs6nXtpLWW2Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632a1eba8a.mp4?token=rW3C1ejYoh0yF1I2vKTXCNHE-Q13tnjTqbCIn2pUY70WKsuLvm6eUceBJSlbuG3bzS-J_Vp7T7bdLvepJISL7g3RpztWzq2W8Po0yqucfalaUSZ3cbbMMxL2rtkOp9hKXWTqNQ8xTGylv-vYaGGLd01NbSPtY3F1-3i-DpEO7ZEidkHwlx57I2MYrx1l2p18EEyrRxSH7MuXM7YKWwuDqjTp8oO5lA6IzfP4ov1RNVLb9faGn-ichtzwQagVo1JKMH-_gieS1mdClpBy9qlBHmL4fXKDaoscB6jEi-jsdLGp72ueMzO4f-svvi4ug800pbIBzE44Fjs6nXtpLWW2Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
بر اساس تحلیل من، هیچ چیزی نشان نمی‌دهد که افرادی که اکنون در قدرت هستند با قبل متفاوت باشند
آنها هنوز هم می‌خواهند جهان را ترور کنند، اسرائیل را نابود کنند و به ما حمله کنند.
هر قیمتی که لازم باشد بپردازیم، خواهیم پرداخت.
چرچیل چه گفت؟ «هر قیمتی که لازم باشد برای شکست هیتلر بپردازیم، خواهیم پرداخت.»
همین موضوع درباره ایران هم صدق می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64945">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/guw7xdKKGHun7SMwDrmn-sm2DDfOY3rJjsPbHA5yu4i9Ye3eSS9pSBXZ-pbizK99BJovXSkpDMj0Um8sg61QYPuQ0iqt1XPhfQA9NMytmyUnjxurQVmPqh2f0GVCajNcBra2RbXP8VZl0SEm7HxF-jhn7eYweGHKrpJpeVJq1niipfdMhLjzrcO21H026wLKuHJEoo888FN3hcXWsLc1H_y0ob2j0mvjWfPNniZPHo_hpAV-MhTDc15BsJwwiJeMFgEHCX5waaoEZNOBmRFbHNYNdF5r9zH3aB4-inDbaxiWvzMK-uDultRLRsQ1rnM4RSkop9rmkYF9d7oYTEEZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64943">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmlIRrwFAo5ptWA8DAMvSLrXmNbcO0bibbO5-gBuIRH26p0bBBE1Of57qgW4iDsWv5hiufl4OIeEHFT6uUOR2OsTOcMdIPhJTvAi1fsBDCPWiZihW4wiEHm0dHANLKp-n2LpItRYSj9kMYdy95pzng2fSwOXHe_3055UJfXWmm012QAHLzTCLh2lQk-zHngqDlzhU_dr9OB8TCW4wezRkDXnXBLG3Y6i1D3ym1B-WLAJdd-kYCQwmR_Lm3iylhN4GyB-nK0YlSQ4wvvz-qDimIavNC5FEYlTzJRXJrB4pmsgkKRg05QboSFr86IRjNA_wY4s6Gvw5Ei4_j2dBJhC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در سوشال تروث: «این آرامشِ پیش از طوفان بود»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64943" target="_blank">📅 00:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مثل اینکه شمال کشور زلزله‌ی نسبتاً شدیدی اومده، مراقب پس‌لرزه هاش باشید
❤️
‌
#hjAly</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64940">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjNPVwmIFpmEGL3vjOciXOHRaK_r-POPtEVbOcpr98c9rkOaIfzAAeVCsKE-wwIc73w7jAY3Oj7TFHDOPLcNK5_OYcv8CR4Dw4-AMO7ntCgSBRd89IkDVvG3ClepG41WWZtg0hR203rXzoZJZ2FwjvprxFx2pd2TjdHGsPyPe6LinmuqvyceIR6ttDxfmtbIF02GTBVktDlT8Z0EFkkQfyjM2_LUZpsmB2ihaErK04AsdXwibhzZ7LG81nagtLMvJCpnYHUmCdksdyquzLuMtgPOwKOIa_q8MjyFaKX-7JZ3wwlW57HmQ27kPU4iuCi-Ozaqb4OY2KtugZ25xBRS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=jma-NmpQABFOzMCodIz3S-Z-AlM4SajKwwdxzg8kVV3wqCjALD7R_N4fzd2QueKrQ7XgdWyyLQJScqbTfgDkqzwE4V06xT-7Gc0806tzjDlTxljnKbO9jyYsR5Mw4ujiDvHoQW0Vrugd5ZST1FohChpY-ROr9GWph4OMPuiCMT9XG2Kq-y7tdMWVHGc_gAGPYPRK5S_PJlhfFoNg0zUYEfIJwzzFGUYmLGrg61687KVMgf280s2LYA55q5-0su26hS2J6TrOo_EJuhD6ScisVY8qnyQ7H5nqZCle4xJoLU6TJ5Itg3bhukTcLYJ6lKfJo0x4M35XapOZMVK9LJjfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0ac308ebe.mp4?token=jma-NmpQABFOzMCodIz3S-Z-AlM4SajKwwdxzg8kVV3wqCjALD7R_N4fzd2QueKrQ7XgdWyyLQJScqbTfgDkqzwE4V06xT-7Gc0806tzjDlTxljnKbO9jyYsR5Mw4ujiDvHoQW0Vrugd5ZST1FohChpY-ROr9GWph4OMPuiCMT9XG2Kq-y7tdMWVHGc_gAGPYPRK5S_PJlhfFoNg0zUYEfIJwzzFGUYmLGrg61687KVMgf280s2LYA55q5-0su26hS2J6TrOo_EJuhD6ScisVY8qnyQ7H5nqZCle4xJoLU6TJ5Itg3bhukTcLYJ6lKfJo0x4M35XapOZMVK9LJjfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند طرفدار فلسطین از برج ایفل بالا رفتند و پرچم فلسطین را از طبقه اول آن آویزان کردند
شش نفر از این افراد توسط پلیس دستگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64939">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDABFqERv2STIR50Hy0-b25J8qa8dAexOdJP6VicdPw1pNwgWULpudwakx6I7lcQH2cOu8yM4QzwWeNYo3V80lqZWM206cVDaQodBHEBCBfXPDtC3rVOI-F19aN9x7NHfzMD5sSNfq8jjDSWt1yFH2x5bqd9o1hVpwrG_d4TlhpmiGRDnTBM56QJ17VG9uOyNGA1-wG_45xg4wCeWX6TN1svONimu3cqSgNGrF9_hvvWoywGbYWcXNMHVeAxb5dIkDTQcS03nGWO03hHEziEZeybvLLeTO379u0-0dfHDnyP5rZXYSgUkQ3G3ojUuyysthmFVdLtdNtObxst-H7XIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پست ترامپ در تروث‌سوشال:
بازی نداریم! تماشا کن قراره بعدش تو موضع مورد علاقت چه اتفاقی رخ میده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64939" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64938">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64938" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64936">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWMyItYYOI77DnlOLWvTUriFFB9ZkeHEtx0Rh1K-MlrLq3igoSyV6qiLiqtPqxclXSIP9Epo8f0VP98dXOQFcsrTuyJZt_Cs29W-XZ3bqtXWpTVqvvBgl87sHvMTO5yG5E3YTToSkevCuKVbyL4IMOTyNkgujCTL2B38uPCmuwuNse5_CaXA61XkH98-6h_8_8Kp3yJfr68ty-4EHvuYUuRAHaK5cwHt5gXmnDTlpeg328_k2W5SS6KV9j5a3TPObcL4LhhxKevLyELhTAiIhQpOSzTYt9SNVHyU68fb_b6p75FJNcvFiY9pBi2IlkwGiAbqGDFwnTErVF-2QLUpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLj1IjTUrfx39Z08CHnhw45Jn0NN0FydAFVWl7XghZOMBv8qd1Voks2ka5VovD9UgZ04wNQb1JjJRLEm_Yb9wJx2f7V7rFo07p3-1bCkcDHOKbSvKWtl_f2GbSrMmxkzMhGN2cJ4o17hANuM05jdesokaKOYWpEwde6yx_YhUGZ1xispWnku543WJruCr3T_0MuReRIUO0kgItAcpFCfgWqAxsCWOwTeBcX1UXaPAoM4rhbO1t_nHos2znbBES3eFb_uM8apZXnPrOUcEUl9TkvGl4iQoatQJ44JxRl2ji1oOqFIDw1Ai-MpE9y0U1Dc2rW9yt3THD6k5d3fHhMFEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیکتاتور‌ها مثل هم رفتار می‌کنند
دیکتاتور ها مثل هم سقوط می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64933">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKcdVd3pEDilt3FWjotwdhlKsAQJBCw1NtFStHN8IabxW3E5BetPAuCV0OrgfUVIxxMQUO9eW27f-Be1B-TwDV5YXeB3seA82JK0fOJ1JHBzMaq1wxrm_7KVLK-3-kF_AmNCkkW7Q9Jk0Zl2U8d3QfCFzlfrl-Ee1IJa5QjM7pHcQeSDqFMGXgo8q_jYjPRsflyW2UkvhhFMYL_zb_qNamlag-j9R9amoQ72crFwRNQHk5aXqyMhe-EWPTjEc0_eqEljOgr1nuV_HFgjkoIOq3C897LI2G-OMt3sUIpTcyqZWdH9JlzdB-sd6feCMyr8MCpQhfNMl3RXZp56lP-LHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزالدین حداد، رئیس شاخه نظامی حماس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64933" target="_blank">📅 22:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64932">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=nn_WlHMOLvgcVVnSp39ECUVpHSXDuwjflI6XM9dDlhsLzYtqJFmw9omKQfaCYloE8lqwm1-V42bUNe4W-Y6SZ89oReE0OgOVNOp0N_ahq5eiTmOanXmeNs3_xyh2Shsrg3_eq6k8LM0-e6SON7iXzULlC9nfI555xSAG-iGE7CxMXROtm023eHwQCzxLesM9SZDYQkhZQbd05-dAm-fM9Mjw-h9jPgO4E5zACd2psCM8SFKwoTbQVSF7b0keSzT7Dr19Fh0NLW1hmOaugxk-k2Gj77IwU0NEYbyaO7dbHAKA6eKI39keUkl4iQvRgRBSsiGufioDlJVfVrst_x0ePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39ff7f49a4.mp4?token=nn_WlHMOLvgcVVnSp39ECUVpHSXDuwjflI6XM9dDlhsLzYtqJFmw9omKQfaCYloE8lqwm1-V42bUNe4W-Y6SZ89oReE0OgOVNOp0N_ahq5eiTmOanXmeNs3_xyh2Shsrg3_eq6k8LM0-e6SON7iXzULlC9nfI555xSAG-iGE7CxMXROtm023eHwQCzxLesM9SZDYQkhZQbd05-dAm-fM9Mjw-h9jPgO4E5zACd2psCM8SFKwoTbQVSF7b0keSzT7Dr19Fh0NLW1hmOaugxk-k2Gj77IwU0NEYbyaO7dbHAKA6eKI39keUkl4iQvRgRBSsiGufioDlJVfVrst_x0ePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64931">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
📱
👑
آی‌پی های جدید برای فیلترشکن شیر و خورشید
🛜
‌ ‌ ‌ همراه اول
2.22.250.149
23.58.193.140</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne6DhGJydiz4yJAjBLRyR6NKYxcs1Wsq-xjX2u6D0cV72taXWXBuk4FvVMakAOVTonahxGU45jJHNz2QWyT0Y2MD2zNbEeQu059RhFBSL1mZLjaJZec7VbbNQzmkDjTBOmLNNBNmMT5V377sEPWsKSqNGQJsnBTBWJ_08Zo0DGV71zJ1q2DxNgIw7O11jKkvLdy8jPeHpmSoU48yCAc7fDYiekolZjhue8quP88UgTR9XZLLGSfC06rkUjDR86udanABs9D-mJeNB6Tn8S1jxRLylQx45VDmjJyLhMvhnMhq8JZyPrTDJ4jeBZaj2w9By_POgXqWXMQg3LOk7RYL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64927">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: تعلیق ۲۰ ساله‌ی غنی‌سازی باید یک تعهد واقعی باشد  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64927" target="_blank">📅 14:39 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64926">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64926" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64925">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#مهم
؛ ترامپ: با تعلیق ۲۰ ساله‌ی برنامه هسته‌ای ایران موافقم
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64925" target="_blank">📅 14:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64924">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تنها هدف حاکمیت فعلی، رسیدن به اولین شرط هست و بقیه شرط بیشتر نمایشی هستند برای بستن دهان طرفداران، چون به خوبی ‌می‌دونند که ترامپ، اوباما نیست و تا زمان انجام توافق، قرار نیست تحریمی لغو شه یا اموال بلوک شده آزاد شه!  منتها ترامپ به خوبی برنامه‌ی جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64924" target="_blank">📅 14:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64923">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
ایران از چند روز پیش منتظر پاسخ آمریکا به این پیشنهاد پنج‌بندی بوده، طراحان این پنج‌بند فرماندهان سپاه از جمله جعفر عزیزی با مدیریت احمد وحیدی و تایید مجتبی خامنه‌ای بودند، طبق گزارش خبرنگار ارشد الجزیره، تمامی این پنج بند توسط آمریکا رد شده!  جزئیات پیشنهاد…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64923" target="_blank">📅 13:40 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64921">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHtvZIhJmeRn6-J5X8cKmRjMHoLbxezDdOwyLs5GqNK6PWc_Z6llluw2AlsQpfsxDRSVFrsBpdgcTAkSzle7kMs_nwroi7BEP0ER73uZY0hupWQsHZgU0AoB3SvcnXKpYIWvHIT2rAb0Eo4CRKJlZpY3vcXlzIlh2OGllWFDGQEwQH8vArkE4YjkhehSJ7bN588rViCeJQ7MU2p1QBqSzjDQq306YgJQ3_NIzryFr-HFjEgwdUtk2q0IUfxKqPrbXplUSO5AyjRtepI293K570RQUnp85Hj1TCIGUhI2gvZGWD1mUhNyBTagkFgKFEX136uOZZuA46syTBlUeKiEMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IgmPCjHKifW4pMLeWfx0dLbOqRI4LZ3k07S5oj5ICY_VfYh1pGZ1wKRyGBo0IrtOdqPUc9rhUEjANeNcdrNuF3d2_PLAvuuXVvRTtznKNbVLphAvsjf5JriDpzL5irPx1fn_TJGcsSpnZwEUjt_fyg5OfwLFY7lWFvCBIoGc6qp0y6NUGC__oyvA-i_Ti7tX1Djfvn_NBxRnQ0t-UGOJ_8yUt9sZM-AqnHJc0ptwKDKe5jqmq_BYOVh4iLs5YOHlaNQGTDrgcbFMaSXj5DEvfUeryMrqVtawdngYWzeE0O8axy8_0e1TUlFfkFnNZka9z8JFej1AgLmZ6HIEDv3VIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ الجزیره: پنج بند ایرانی ها توسط ترامپ بطور کامل رد شده‌اند، مجتبی خامنه‌ای دستور داده بود در صورت رد این پنج بند، دیگر وارد مذاکرات نشوند  @News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8JUbAvdhR0pbFibvWV-p1hbS5B0soB9GkuQsdFPxVUIKeU8iDF4tiB_93w2MW3ALFuzyyPiE7Uj6wgKq3v_KNWuDY9b7yZK9X48LslS7J12OnHwWxtvjU0PaFIlfoEjkkHMeKMKbqRqwUL-hxNkqiWi3PWW7UPAZwFzh63WfdF50J2JJB8yXnTPhO1bh7xyf4GdOBpJMToeXCmJZvQkF67aygZ9pwD6pPoUvhbp_7Ng0ZqThrhEoC1_MB9PeiJj2sAwsyOm8QzkXsvmoJ-ax8FvhLc8ubvRSi1xZWEAtGYfGxuwArOUhkNcY_acsmNQdAroUfAkfgSggI4bUI-9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#فوری؛ علی‌هاشم خبرنگار ارشد الجزیره: یک منبع آگاه ایرانی به من گفت که تهران رسماً پاسخ آمریکا به پیشنهاد ایران را دریافت کرده است و واشنگتن شرایط ایران را به طور کامل رد کرده است  تیم مذاکره‌کننده ایران پنج شرط را که باید قبل از ورود به مذاکرات در مورد…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64920" target="_blank">📅 13:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64919">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
ترامپ:  امیدوارم ایران در حال تماشا باشد. ما دقیقاً می‌دانیم چه چیزی را به نمایش گذاشته‌اند. می‌دانید، آنها کمی استراحت داشتند، بنابراین سعی می‌کنند چند چیز را جمع کنند. آنها چند موشک را از زیر زمین برداشته‌اند. همه آن‌ها در یک روز از بین خواهد رفت. هر کاری…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/64919" target="_blank">📅 12:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64918">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇮🇷
عراقچی: پیام‌های متناقض آمریکایی‌ها مهم‌ترین مشکل است، هیچ راه‌حل نظامی‌ای وجود ندارد و فکر می‌کنم ایالات متحده باید این واقعیت را درک کند. آن‌ها دست‌کم دو بار ما را آزموده‌اند و اکنون به این نتیجه رسیده‌اند که راه‌حل نظامی وجود ندارد!
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64917">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/64917" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭 𝐕𝐏𝐍 ]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xmd-lSzY7Opcu_-AMcAFBqAQZeoPY5vdFlIfNixr7kO1CwGx0mtIN0MeWTeXQdcGHMDTm2gDTYG3kQrv4I-kv12SEMigTmihVRyru49fxodNG2RAcXcWZvg9RuXF5V1WQCKdur0ziNPz0Kgs2mhlH9Xz-X_To1eJ6A-v1Cu7TUsirW9fbvTo4_k__TYwDGza5L6xc28po2qZ-0PxnV4THEjGB_PY2u-Zg1l-NiwSWf92yojsBABPvqa0ZHhsWap3ziJSQkDW8YRoKh6MstBQXMW20BKHHOl22X047ydChMoWA0tbpggMIuaTHn0mOpsd_tYsLFT54aAGsMxf4W_i7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/64916" target="_blank">📅 12:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=OjOqs7IbXCrIp8pnBheCE5L7SaUViCMX5Rro8b9ynlyxvpZsJFZPcOiVnq-tSOnXVpc5-fpZXRqp7Xw88jjvzeRVsYqNQoPMFhgkKvK4-pvwbWppMNo53MMRtx-kjPdbjpz91OcwGDkBH-9tcZF6VPVPqYe1jVkaAh0JbS_sU0D8Pwb53iI01nKFklDGvNY7MSp_rBj3A6_hZsfIT85xuuMp4TI-s3w789Mz1Fvo9PZOsfGygsxntwyAAfI03il1D6hPKMK7TQlTi_IiC5MbTWUnEwdlPMTrcDk7Fb0I785A5RTjIkUZ4A97lPHd8TzmohaIHUQwfpm6i1YgpTSvqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=OjOqs7IbXCrIp8pnBheCE5L7SaUViCMX5Rro8b9ynlyxvpZsJFZPcOiVnq-tSOnXVpc5-fpZXRqp7Xw88jjvzeRVsYqNQoPMFhgkKvK4-pvwbWppMNo53MMRtx-kjPdbjpz91OcwGDkBH-9tcZF6VPVPqYe1jVkaAh0JbS_sU0D8Pwb53iI01nKFklDGvNY7MSp_rBj3A6_hZsfIT85xuuMp4TI-s3w789Mz1Fvo9PZOsfGygsxntwyAAfI03il1D6hPKMK7TQlTi_IiC5MbTWUnEwdlPMTrcDk7Fb0I785A5RTjIkUZ4A97lPHd8TzmohaIHUQwfpm6i1YgpTSvqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
📰
کان نیوز:اسرائیل معتقد است که ترامپ پس از بازگشت از سفر چین برای از سرگیری عملیات نظامی علیه ایران تصمیم خواهد گرفت.  مقامات ارشد ارتش اسرائیل و فرماندهی مرکزی آمریکا (CENTCOM) در هفته گذشته درباره احتمال از سرگیری عملیات علیه ایران گفتگو کرده‌اند. بحث‌ها…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64914" target="_blank">📅 10:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64913">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A7FtUSs9mBsK_9j8hKXMgY2Y-MrlMdEdV8Zty4c0kdgXnz27J-Qb9PMV4rIL-VJoUxIQBYJqTLCLwxeyp_k3t4cB5zlHHBJSkCthKHgIw0_hSCAuaHqMrUoqnP2DM2lqL-cYdGeyp6x99Aoxh0bGzQ2IbzMyYh4qz7puiII822XKqWx0XyqqRf5L471j5zbWuYjVwHBkAr17bGot9PIV5sByI8pZcSF45HxJ74JbdB4EZEK0xk_KpvOFmLojNjtMQC2npTn79UVspnB5_gUoXk0AkL4rtrCkS4KVYzz3xpYrVvKEAaJt3v3Z3JLKPXXx6huTU_xC8wx3XFHimxG7Nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB0n12NIcgRFWMkFmiKL29L-zxxax1JN84uG8_GRvgMbhgoYQ3LCEb10DG_Pbmu3r1g-6_t7HThhGvbTVO_uBV04Nv687c7MebklN2XR4fS_R4Y5HIHAanvXd3nHiE--m45PIiCOmZUwrawz5fYL69BHMuOnMD01c0vddmLU9BIIr73Zk4jSqWBd5JktEYZ5TO6KYoh_QsRJnUU0JARSdTpttxMG-eGiRdX3qMMxqy1ziUPvQlWTGeOo2-KJKdI60ixUu4lKggMkbtvOsLI4mdM6-_T3OOqF9dAqREowmvBhcFFu_xbwRxIOsCT7z8GPvu8bhn5DhEDo7is992v-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=AVo8CyYXlI_bFD7n4yTIuUSytMyBzaEfkFgWZ6OdyMPbmao0jbxCWL4RlTpuV9MlnbYAh1UXyjD64t3PmB2mlMA8ywQdmOh8YI2wBESyubvuEajceDao9PWk0ei_gaHdjrtBxjx1Lafnj11gAUdToV6HOburUu2lfvy8WrwvqaEu2p0oEGs_AnPsMhzc2LbpIEVCJQBFnmI-0snkqXI0U_kQ20qOfVGUtNYXaI-sbPLONs0M3o53j2ecGE9t9PJkgsU-bdIoBMzYeDHGqoAcdQ82hgVCFRYkqiJ71Ia6JZHs5zFHPs6kWZxWCa16VtOJa1mpzc67S2DXmikPFWld5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=AVo8CyYXlI_bFD7n4yTIuUSytMyBzaEfkFgWZ6OdyMPbmao0jbxCWL4RlTpuV9MlnbYAh1UXyjD64t3PmB2mlMA8ywQdmOh8YI2wBESyubvuEajceDao9PWk0ei_gaHdjrtBxjx1Lafnj11gAUdToV6HOburUu2lfvy8WrwvqaEu2p0oEGs_AnPsMhzc2LbpIEVCJQBFnmI-0snkqXI0U_kQ20qOfVGUtNYXaI-sbPLONs0M3o53j2ecGE9t9PJkgsU-bdIoBMzYeDHGqoAcdQ82hgVCFRYkqiJ71Ia6JZHs5zFHPs6kWZxWCa16VtOJa1mpzc67S2DXmikPFWld5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRJMGDehRexrA36F9l2xxkQlN2BQirDs5krMjC-kOYr2cZTmKoyjcGoWWl0s4TyT3_nR3NlTj_GCssS9Ty9mDWxT_LvswdxP4-RowAmbppWbfORzq_r1ZCJk247IILUFa919f2lTeOe5ub_UJrXGKTSG2qM3VukgEx06C2pyVNpjCYLjksDsv7FqddCb5kZPaH04pZysF2Ii3AuYE-FU4UKu-KhDS7YJc7kLsl2D1BIO5LBlrteQ6iiJ_WcMquFySdypyBoqKzisvvytQOdvRWEZNdhclwMicAceS-TDJiPI0Xxp5bnMFeCr70Ye11DgKCNZ0I3C7H4BwSBhekKUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bB9HklDxlhyLRz7Ogbt2svOkICBjgr0fxqeXs0kAnQGGgZklJZfYF5t2U8aqWN-WEGL54UMEgZR8R8pI4tUggh5Xjq7oOx2hTASHHMosLlCcfkTTQt9A20N53fvKKryI8PM_R1uZgG_SmbHY-rJe4GksxFBuHu44BM5T4cglV2gu2FuO-FElo_wu0wcavtbtznr0fHStZfc1TjG1UNedqb4GbnKo3wmJ-82WwC2Bt0rbPkxeIRBJY_RTCQi05xUBc6BJdEaZE4ycjHq_-93gE6l5YkhikuCp7nWUxBzMNADAiv8VAF1OnH5SD0Kg7mvUCfH8bCpgeWCOE8CWGv1vSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPq27j_UeM6cb5XCaG-MNPI7x8_mPS5p3b6ZrJTW7KRp_KeLdhsT0_bE24mSejkcqmZzuG16ZMdOsbo3-f7LVvLKxZMPNWkp43VFmLRuwaSoL5JJZn_u1xU00Zlby7luuUwZND_JVC9VXONWjHbKm9f02j2dU95Gg71jd0IcbeEt61bxy5rw8wBTLiEM-1OgbQKPQp_FVCQB-cResZ6EjUyHubnqqNRk4D5zRbYO_V3-flnZAOjsPsWgGJWQDggxB_4OSMWN8cVyD967rcIRrYruYTVpQ1dn84sCVTqTB2vSYCdhnypFwA8rCYPe6O4aHTINeWx2zBN1CRKuICkLZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=WN_g6y5YrTYNMMwPE9-PlkY5clY4wo4SIV1UWEXZc-Lk0e-71TgOOIJVsydxsf-NafVbixapJl2lEeqtnAUQQXuLt6w7Ux-d1ZhFKXKqFVUNjtHFtRI_eyV67IBOGzRSXBCs7qYNASy9KdST1L5Xwl5zL9lmKrEpkLl4pYQBYJAoqQjshtXLrwUGdouzJeO7jUfkJNSHrIe8kwZXPDqHKSfaEktU-9Vuib7UABRpgOSWwmY4luRazcXzaQNaiQn8p-ins4W3n5fCm_m6leFczFO9I8LC21nuE_EOGr_HT9hm2UbUnP36E96YdfZ8IDVEfD0h1O6omyVMy2bOK187ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=WN_g6y5YrTYNMMwPE9-PlkY5clY4wo4SIV1UWEXZc-Lk0e-71TgOOIJVsydxsf-NafVbixapJl2lEeqtnAUQQXuLt6w7Ux-d1ZhFKXKqFVUNjtHFtRI_eyV67IBOGzRSXBCs7qYNASy9KdST1L5Xwl5zL9lmKrEpkLl4pYQBYJAoqQjshtXLrwUGdouzJeO7jUfkJNSHrIe8kwZXPDqHKSfaEktU-9Vuib7UABRpgOSWwmY4luRazcXzaQNaiQn8p-ins4W3n5fCm_m6leFczFO9I8LC21nuE_EOGr_HT9hm2UbUnP36E96YdfZ8IDVEfD0h1O6omyVMy2bOK187ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gCT2--HEK549_VwKc3JSGtj6a6ykdBo5Bl_7npIGO7W8WB3NMHpMb7dvLelcn_8XEuk3EoAfOJvjfl6ulfhMnKzGjXkBVQV62jVsZUq-a2qwi4pRX4fvvMzeToTuQsIP-CdNTzCfxuT0p8J9C-W8CihskwyJE4s8AX-zRihu0kxx8yxt_LZ3nOHUpC0pF4S9-45RU8ILqrwZmVOkiB00wU9LmKBMHA4GwvUpIN3PNYjak_3cGMQ5yGE6oInwj2DspIc_0qlgHquAXybq06A8yov9WFZCrg3dRDE6cJjsFxa9iB4i__3hrZS-disFt9Q0D-EwnwOM_FJNfAbvQcbU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ie0IR-in4sD2qWsI6XWfLhG8hG6feLMjhwXFFwi1dDejNCIshYz6rN2_e3TaJs6QNCu4IaZ2HKxnZoDbe20ZyIVwPQd_PtWeek05OmTIJ29Qo77nQ-IGfH9aVuiFJQgDV1Hypd85A79K1gaseOWpg2iVxUaejg7oPU3dEt3XEIMjFASZMkDMmBT0HtI51ClnjEzGgMP-6_M7mUtZcYh16wGEtDheBysb4XfXG0jhzk-1zhrPQmQoTPeMMC0oAJdOu2qd-nBRy-QXcXYWyTUCLX4BdsUTtRtxl4v7td2iCM_YM6dwKe8TbsuhS_uIw87bh0GtZZqhPU4D-I5HANb3eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjl3ekIxwb4ITIk7e8c5pEvdoRAo3rRInfyesKET00Sqi2GChaYeANnT9pjb0cDNKAnhXwmSRsWkVzltFZNn4IBGdYAJA9GWjktrzESVlypQBpneDc-pfV0Y4eD9uWVrEvW3TfZ8p6JRPAV99cr3gQ2u4RwMYkmnTgjKbtLZIfeh8fQiZkR56WUMljXVpGrZi9-zmM_ednppJbIUuTT04iVHmNajLkUJUpy0l9VRE5VOZlQDKUEvPx91Boc6u2pDs80SBvuvDHnb4iXihFnpXDYgMiER26mK4EMLEn4jmSw8Mmgs6yiK_QKXcGbNKwt4r0PeQd1Kszq-U_bub0GNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afadb-eOxN-6JUzXif5hVeO9OL8F6emYVgHnPe2mfsgFeucVFkFqdVShWBvObjmfg1hX69iBP9UHy7nxJBsTFn8UKbcqEKjati_V8Wq2Z02H2QEEj3AgaoXDHmxHYO82Kp3EMG3CMtTIQhK40NRWmES1jG2tXJcYHtNcfzQWqsOJPE4F68WG2Egs0gQralSserbKXDUwSmuD5-bN3SlMsIFuFgANl_8FxoaRcxbBEIywLwI7t6BYKBW9EGM69oU-gNy52AzhBTuH7qzt1MDTNEk0HI2NF_v7Di_D4sqM5vkPij6GHEM8dB2yKcbgtY-jiEz2X1fYuVgQwCwhpkmxFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pW-duvONIUMjEidu_S1Dq_Cm7NlpUjR-aEi9gy0WqxZnsWRarYdJpZDK8HwaxtGujA5118k7czRTq5BiFH_Zrv0ohggWVVxV2sZ6IWPBbO1Pa_ltLn1PKhwiY63xgdN7u1e_ORYg6ZsmZD4Pvc0-PvT_zYB3Ejc9V2NdWA7vy6OhYAaRVdZDHjqSOzQGYPnUi1nHjG5avxrCFxzmM7jOYHf101hvOiIhWSYCeaR4sCrooUpoL6XPtvj6OrmC2ZtD1XXaE9wVI_W4Am9hy5daADNa3wcrMlHCS6fnj0UjQL8O8-Jm4tlIR85n3gzpH3sLlSJBYedNCx2wGnd3ZhdsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ItgjTtpIKd8LqgkI6OeaY6Yb1nNULgMn_Jk22PKRGoKUFXQVNWLlqyW0zE_SO2hgxuFqGj_rW5I66_2EnufoUfWPWvW8K6vADQb6WyyrjeZMgmWR3rMaHpv6nn24vzAR4gRmL7O4Q6CKbLmYd4HWh4sYtJnBHQiA9qyLalXTO9nsaahdBEKy9VzF44drYj2wfOn4EWq2dy66U6tk-A7FJxGnoLh-h2DN2ETew2uBobYaVJdl_6AwP7MY8XbiqoomqDUWkhYFLkQ2peGNf25ljqcHkwQhwHI_Vw3jKR8Q2fay3AWl8gOe_j_9SvKd8_MDd62H5J2eTjMfmgc0eoi2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=K1uAikLdxXMdVSOAmZ6FMRdYi5wHWVaSoMOTFy6GjvdKLYsUf3_0yNcj83Zhy5-jC0S0onjeCyxgR08qlbaq1A28yAgO1iQ97CKgtGXgaF9HFN0qo8rSvPxLmNeIbmOfzGwxjp6cyN-j4E5t7IAlce7l4ZPurdkdEoM21K5uAgsD4pJfYEPAxNTDXrIE2zpALk3TCr35RXuh7CXezBcLCWYnQW5FE9MvqtW5hBaxTClRHBs8KSZHuNIG0THwDyiMEJtzPF8ICmj2mVE_lztH5lSOiMwfnhh1RD4ItKRwSUSDjV4GCOmPVDgBqRMfelZBGvNT2Y-e77m8bK-Dt4VCuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=K1uAikLdxXMdVSOAmZ6FMRdYi5wHWVaSoMOTFy6GjvdKLYsUf3_0yNcj83Zhy5-jC0S0onjeCyxgR08qlbaq1A28yAgO1iQ97CKgtGXgaF9HFN0qo8rSvPxLmNeIbmOfzGwxjp6cyN-j4E5t7IAlce7l4ZPurdkdEoM21K5uAgsD4pJfYEPAxNTDXrIE2zpALk3TCr35RXuh7CXezBcLCWYnQW5FE9MvqtW5hBaxTClRHBs8KSZHuNIG0THwDyiMEJtzPF8ICmj2mVE_lztH5lSOiMwfnhh1RD4ItKRwSUSDjV4GCOmPVDgBqRMfelZBGvNT2Y-e77m8bK-Dt4VCuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBTr4BNCXen3H_BoWrX17qOqmNFMpB7aWK5ViA0f4mTE9yZi4Gg26FrYbq8G3qK6idDf9TboGRCXXs1XylOYVgREOZP6aP0Go6Oaug_Wbp7OoFBA2JI_9jVENV9Hpa1RIX-yhtKVAc4rfGeu5d1DgEJ4-5U6CkjeRl9h8f4dKALKhdR6FgMsXQjMZyL_v917gZfIoriDEQnnWsbBY1TnN8IGMbw5XbLz53_qzV11tZKqScthqblJFkupVL34YBrV0jn3jv6S3sYHWR6eLfHHv2pRGM0m261-RyeMoglS3zK_x1HYaiFqoRTMquFrJSgJD-x31-v10I9Jrd4Ubf6Bog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_m1pEqB904FxGVhzT1pgOMzNgbnJkINXxkfLUsWCq_1sZTxAJNYOigG195pmbiLgtvXFnCA4wUaZ88OfSVDRXSxDt7aG86F7u5sm3WBM2UVU-RXkPI2hB_so5kbnUFbaEz1F3iFAcrBHHOH3KfhPEqkTmAwyRPw32TrE6j4ff4Gt2_moO603aQQiJkUJDRAtUlPTcPXbOVq5DVnMeHvhKg85-ZHdM9g0TQQzTozqxCD-4VZKsrg4kJLhGPwpbTor3slgcD7ie4L_0cw8lTvzRb7k7wZ-fGNvttedo05zmXMVyxx_DDghglpPLOi85lbk7Kxuy05BzVLLUd54CwDfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awc8EUYc-yqlmChsN07mCPQ5inLL58p8M4imPInvNMJl1T81_6vReruDpHg8KcrSt0RraivrGAaAC7HX4U6LSj7BrLhvi-bdoLde79hxaeOjFmrg4XSetvNk4-OIdP3amJEpXhM1VhBE29--iSLWKBGyR8iTnt9LnivIT2lT2st1CL8oAzJfOMxV2bGjnTXg7riQC323cjg_MMyg5EUBHLzEwVqw8XJ67kjEdILXJFuIwPZ7NZYFQnngGLX84Aes3XLm5Y1XFbAt9bV8jABiUEILD_5NHZDeu29fkNBIMKZQBLt1j5P637elMzFYnnMnKkYbnOPzYjFOcvn2UbHLgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=TQKirmrLuKSYT00S3pEAmKp2qwhKIda68OjMOjr9rjbEFDL_1BboDOiqppD7E17OrMS-oSjZ_TlY7CJeWTOB4r6GI3-v5APjsLo8E9_cUcdebce86e4B9vGH2jek0Qkltv9DJqYUxW9HCXIBBvp6nbipyovrrSxjGCOvitQZmE99-dr5bBfI4ebwyRlklYSbt6JG8cFUp3cztjULK5hRs8_A6rB1cbSfsxlU8Ehvq9aldOJc5pDhBH6WmgbAjI5IX_qF3RAz3J_O94ElugwmRxAUm4F2xxs8ZoZuRvhOuMGOfbfL1b4Gl1JUyZwJPycZXvXBj7uYVG0ZGoCdz3Ez3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=TQKirmrLuKSYT00S3pEAmKp2qwhKIda68OjMOjr9rjbEFDL_1BboDOiqppD7E17OrMS-oSjZ_TlY7CJeWTOB4r6GI3-v5APjsLo8E9_cUcdebce86e4B9vGH2jek0Qkltv9DJqYUxW9HCXIBBvp6nbipyovrrSxjGCOvitQZmE99-dr5bBfI4ebwyRlklYSbt6JG8cFUp3cztjULK5hRs8_A6rB1cbSfsxlU8Ehvq9aldOJc5pDhBH6WmgbAjI5IX_qF3RAz3J_O94ElugwmRxAUm4F2xxs8ZoZuRvhOuMGOfbfL1b4Gl1JUyZwJPycZXvXBj7uYVG0ZGoCdz3Ez3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoEKYvUQO9Nr83yTKVCZmyxLW3DXmLBjXIMpjLUL_9xNYSMr3H-RmlZ9HZ5qyGexZV95wOBi2Oo7Q2KLYeiZAcknm53W0LkefVzEbX4eidOJlD_Lv1a4bvHfFLaHi5CQf_MrD8zvMjeEvqSSrjygN-7UkSN7XhYftdcIx6xuH240cy1ycKOLxWx1x5fsgy7U95pr4oYFC10a3dWP2USN6aXqQmeL-MIvnXipYa8zC2tp_IoYbbZry7FjPab2LYSkjmLet7Oh-xn0sci284LAdYyLjk0h3cclOJtlH_fgMq9Gf3gaCxkfhyKHArdAp1FqbUvkaL_tcO1Ztc_Xf4FNtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/FO0cm8V_NaZrpQtiHwJY6z_DEnr0wrhDFlDbBUW9ukWDR1wLKyjr5CKHUYOhmdurYr1U2DeyPYH5BKNjybbW2Sw7YsbD88nkLK-VRKzh-vuzm-2dgq38E7Gr6hKUBMCFMLsieX6m6Cq2MBLLypSXwpl8x-PUPq10cvgnjc9wlFZ3NJGktPxhR5-GvIYlS1oSbuFPgGHdHHmwXV9B6Px6TyoGDQMzKItwTW3Sxpysw8NpTrJ79iV8QZFR72EFBYmA2Xyy9kUbqv40K9l5KLFB5CGo-biGuw0jXkHy_L0X-cNFwuMNfhv57AD856OsAlJ1-VN66H70-bZcFF5agBqoCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPLmCBO857RXeYnuug5tJA94tg3CxBzwIy4S9UssTOFmatesskkApuSpu6y_ygFUAbWQbeTETj0FG7GZQ06SabG4HEisykA_RQIm2ankCrGfYnBhqrwNyLuV1k0gmRtE-NdqtmHN989gY0s5KxsRGBYjzNbx16hwHYquf634oAbxjzipggnzDiFS4N3LA_5DsuZLkXhvetZZEXeP1UJExQhoxGwRV0XSZKBKl9ZQ7EO_ppdMPPC5sVXxsqAZ4LM4S8-Exb61tg5HHiQOHSAF7wSImUZlExF-x52PI0GhJTTd7OCZcYUhuqIY69GfMEbFKfxujRhWA4uh3Ojr2eeqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd0vSrFw8GxLhzBV--mtUTHFIvOGcLsei20_cNpaayFopT6I2H1Lb_8jbyUQwhCB1K5x6ZejxsEDNuKRHoUaH1suaHEwhg_vWacklEDIQsMHkArrLzeUE89ZfUXj85htPxNegFxgy6TkFCt4ck2sliabW6uFjj9IGyDYavhwUCdFLmnEB8B31Rj2gD2_Tx7qXMKZbqmw7hSpwWFZZxc1UypkcXwMQyKTjFnoB-tJK844SAvRpb71gs2_nTOnCCe2UOyfsOOn_w4x7fTcnxNsW6Tn4I87knnvyKil5HIpTCCjhRZkyjVyPvZvcKhq52vnb8oHulK93ZRJWsrYjE0JYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM5RDqehFHnFJfzmuvz29CYEeiiVteXTZ7ybtomNA0YMlUB6I6MzY4ldYcv-0LqBrlOg_Rw_Qmus_3fb8ByBbKA2HpTh2H4F00gGtuR_tnB6x2tLWEPnavSIDVtK3othi64uRGKrEoA8SsiCiAOfYlpi4135DdlRUejmRguJA4abkOks1cjAMnT17LCCjLIoKGC5E0G-lZuZEc_piRB1Svjvk88iSLnw8GzCKx5eWFS3uNb9o3pwKkkop70UJ6AAb7xmnNcnuFbaZulnSBFK3d7RiX9eoDahTlQxRUJ0jEdv60hHVXhllTlEO_HuBchMtgN9UEXzD3_LNS-mGFf0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=sTIPZ7XDzTTZq21dBOu6bJ9e6TIBBaGBq-FdNn5iY_oe162lnALQFj2jCStyU0qt__jdMbZa_pmUmmJxX-Mv6ngs-XJZha_Tjzd9FD9Uink0KzCvE_sr_fkq9A3z52wj4PgN4TqQCTfq-aW61oVvWanMbU5VOHApmGBBDSnfop_9JH6toHdYqzfaFKBEZRE1m970rZkArIPNafDyYJ6bi3UQsZNig5SpvoIpoakBTb9NXi-OUhqaSo_8FT2HbjAt_ArrXZ0tbvkrJyFY1OFDR2cyCXuLsGpnvnorF11ZU_uJuQoB8FFePBtR4OTiw4r0dTQhjo7M-W2EIQtwq1xUBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=sTIPZ7XDzTTZq21dBOu6bJ9e6TIBBaGBq-FdNn5iY_oe162lnALQFj2jCStyU0qt__jdMbZa_pmUmmJxX-Mv6ngs-XJZha_Tjzd9FD9Uink0KzCvE_sr_fkq9A3z52wj4PgN4TqQCTfq-aW61oVvWanMbU5VOHApmGBBDSnfop_9JH6toHdYqzfaFKBEZRE1m970rZkArIPNafDyYJ6bi3UQsZNig5SpvoIpoakBTb9NXi-OUhqaSo_8FT2HbjAt_ArrXZ0tbvkrJyFY1OFDR2cyCXuLsGpnvnorF11ZU_uJuQoB8FFePBtR4OTiw4r0dTQhjo7M-W2EIQtwq1xUBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=G_wNqulb8ypVQ4_PhzKcPTvcdsn6-t7OY5a2eBJEvlh0eGyQKpSHIx3k37SEdV3VoGoZmYg8qHs-IdzK9_l6LMnhXo--Mqn6fRcsZ3I1xZXzVAxq6d3quprJHk8vjS8BoZVHYIr7CEZP4LZ2tGNw5kG_FdtiCkX8_wpq0k-62d6BSz6J2wqlTUCJBfami1cc4ogL7VqqkAGbgKkB0dRgXxOGKnfc87ifi9n_8rPFzER4e9bBcBDRdm4R_EX6UpmmBIegC2SVk9rJtt7fHihEgKXJymY1oI1R8FmsLapqqVR9RkSeszDs-idKufIwRCTfrzYofGagiOHrq84vKQZLvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=G_wNqulb8ypVQ4_PhzKcPTvcdsn6-t7OY5a2eBJEvlh0eGyQKpSHIx3k37SEdV3VoGoZmYg8qHs-IdzK9_l6LMnhXo--Mqn6fRcsZ3I1xZXzVAxq6d3quprJHk8vjS8BoZVHYIr7CEZP4LZ2tGNw5kG_FdtiCkX8_wpq0k-62d6BSz6J2wqlTUCJBfami1cc4ogL7VqqkAGbgKkB0dRgXxOGKnfc87ifi9n_8rPFzER4e9bBcBDRdm4R_EX6UpmmBIegC2SVk9rJtt7fHihEgKXJymY1oI1R8FmsLapqqVR9RkSeszDs-idKufIwRCTfrzYofGagiOHrq84vKQZLvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QoBK4umEZiMYkVrybXb5tQUV4CtGsZF58ExjOUphhdij2qiIoHrWxIXI4SohXzzazoLYlUPJ2wseBHlTo_0W3VTMGY-fNKyp9ewPFKdRHCXew-RyZSRSr5cApn6Nz1ZxPmfuT_oHIQ4TjhxDrnQLglG8osB8VFYO7E69aTkxpZD8cr7Aemx9zTnmy39Iwii53aVW8lb7Ea73dDKgmnrls9Za2_YVbh3kbJetJhb-UuWdeLVxa8QvWwU6Ts25-POx_xA4W5eKClEFqW80kJ1qpqiDZpl45RhgzKSyY6tPhPgHQt7z0Dn49OLQRJ85hkhsCgufsiL4fBIhE7ieUTMn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIJj2BCgwYoAfPahdWhFJymGbJJSnmq5F2opYEbAyTznjb4hoh_BbkxODmyknHlsRwyQEK6zxgRm4xFY6JGlE0GaN03E6JcHFbURRsQxcaIe1Lu89i6mT4KGHJW6RvOrLoNgZpdczcScd9kO8lxNYnTxkI-LHiGm1TZph-2pKbtR8pHhmDoZqkfHTYTCgNTd5WKn-O-bRHFHzjhj7Pf-CTIbQTTl_bhDpblH69ic48MH7pOMawjHncCRBWkazhxwqkyGyvomqlqV8CaP8TDP6DPmkCcBX9wPkVE22ik16rNI13QQGpv7irFaeCwdR9vCikt1aCJLXLnhGLjylVKD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBCu9Z6Z-8yUdsK2ybcUr-546dhpI8ZTAgl5IxLFWLNVndn7N-JFcycWyBiaFvTAMK4XOyxRsgzwE196WfNfmVWZILPb4z6jGH7on_rTLfW406Onj4tZ1M-_r2ys09uEA6qmZUMEAQGYVShXUqPJsc3g5Vu06UB5GKbKBHqWdOgmep7IIt4CXFyvniGO3kUXCz1WpGUB8d-2hcvzsItUz5Ex_6uz97k0eVXzp_cHIXoVgdDrv7pD8YLKhA1g_jbMlY_k4_vQ_DgUAV0OLec42eXQHs5f_ljJbKVW8izF1OwubvHY7vs296c6JIykgmr4R6TDm0FMAsyyg4jjr6TZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=M0HX6l0WJvbfccemZYlT0Awp1vg-sIE9thTVb3weDG0ZwRDo-Pjdxqz_v8pvsZIwyl15bU9tAxeX9btv2qmfsWG6fbfczOOasMWB9ZxGq1H4eosmAuwrgTMOJcvbCshuLAHjtieEAheS1G9Q7SPFAtrWxTHMPLFJu-vqvrJkEoCqM4b0U-Bkec_vzxE2xVRoIzqtw_nrdWV8D7Ny3SZCdf3JOa-IfVnDuh_KAdD0esaelVFJz8dAFPeYGscrsAtTtqzC6ePnKuMeVAuLHoh4zUbquGQCnzGSjy5mOPac1AN-hrSysbZDuFbx8RDwW16j4TVsLSr5S41xNoHuvu8Z8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=M0HX6l0WJvbfccemZYlT0Awp1vg-sIE9thTVb3weDG0ZwRDo-Pjdxqz_v8pvsZIwyl15bU9tAxeX9btv2qmfsWG6fbfczOOasMWB9ZxGq1H4eosmAuwrgTMOJcvbCshuLAHjtieEAheS1G9Q7SPFAtrWxTHMPLFJu-vqvrJkEoCqM4b0U-Bkec_vzxE2xVRoIzqtw_nrdWV8D7Ny3SZCdf3JOa-IfVnDuh_KAdD0esaelVFJz8dAFPeYGscrsAtTtqzC6ePnKuMeVAuLHoh4zUbquGQCnzGSjy5mOPac1AN-hrSysbZDuFbx8RDwW16j4TVsLSr5S41xNoHuvu8Z8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHsqIH0HIjGAjpa3jF8zh6anVhgBKD8dX_B6kYReUQWHXQ4uV7be1JCa8gHo7YOCl0nd_odwoGEPOWNQX_pgVcQMyXSjyVtLd6vASmxYN_7eDboqGX-hdoQ3ObFAoW238cyas8f7lkDn19NmA24fAAvok_PMg_5ihMNVeEC5WW7ygia9Y5_qi4QJzboz9XaZpUjEgz4KR3NMG2UnYZG22eChlZlgfdH-tgDS6on2nctrW972cQjjQIOW5810FmY7tuwEGGgEV9rwA0EOwCAq_f0wCzPPuOa4MzS4tOeew_Yi7oqTCEPUtBqCqgCitd9nsTUB9qkQA9LyQvVMnQCK8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=A4JwjA6W6cF6RR-dVrm2N1boLW2Twkp-RPfdDmmS2-XRFwES7Eb85GwyEOTSEN8GjlomNYilx-FgdKBzti6tjMheLRbWNqmOTg2HgfGm3cDA6jIuZGMzO0SRn1z_VizEtJR915GbZlEl5Vj_Hu9tQDCbgVDQpzGTwvcwrcxg_eIcJiPuDNScN-i8gz87ExsKdA8_LZljBn2JjgH4DRdEwuWwynzrCXq-am8ne6MBv5NLnhwqMJYjkizcJ4-j8Frz0V7oeTfWPm9mpO2wdx4qZbteIjttl6n0Po31_5FZuJ8vKxK1XffijBkkvKpnBDpokvIxefXIIxhmoc4r8_OsmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=A4JwjA6W6cF6RR-dVrm2N1boLW2Twkp-RPfdDmmS2-XRFwES7Eb85GwyEOTSEN8GjlomNYilx-FgdKBzti6tjMheLRbWNqmOTg2HgfGm3cDA6jIuZGMzO0SRn1z_VizEtJR915GbZlEl5Vj_Hu9tQDCbgVDQpzGTwvcwrcxg_eIcJiPuDNScN-i8gz87ExsKdA8_LZljBn2JjgH4DRdEwuWwynzrCXq-am8ne6MBv5NLnhwqMJYjkizcJ4-j8Frz0V7oeTfWPm9mpO2wdx4qZbteIjttl6n0Po31_5FZuJ8vKxK1XffijBkkvKpnBDpokvIxefXIIxhmoc4r8_OsmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=K2rh9L2GT7Mg4Rbgf8q2YRVhAvUEvbzgpkIE9yeIfp940T_nR3d-zL3RHrnBvYnr0irFCwdhhnNJrUtp4TmnWEr--UsLErDIX3N9u4rbz59Zi9nuFWpgbHANabF4K0_FfS5hMka-s0KUyK0bJDV8vL1s2daZ187NnyMWpVTeON6Iy3U0vIAiIut7nGqjh45dCwrg-dH-U1QlJ6y63YRW3PKHMcBeVTmytad5cgeU7UnrOI_tqGepNfz3KPZCWZbHWafAJeshs9Vg9LBy--LNSrlOpe9E3drNEO0Im2zN0pwjq7sWhLCPjVYzAIdON5By8lRxx9ecDNZjB2rifFDUbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=K2rh9L2GT7Mg4Rbgf8q2YRVhAvUEvbzgpkIE9yeIfp940T_nR3d-zL3RHrnBvYnr0irFCwdhhnNJrUtp4TmnWEr--UsLErDIX3N9u4rbz59Zi9nuFWpgbHANabF4K0_FfS5hMka-s0KUyK0bJDV8vL1s2daZ187NnyMWpVTeON6Iy3U0vIAiIut7nGqjh45dCwrg-dH-U1QlJ6y63YRW3PKHMcBeVTmytad5cgeU7UnrOI_tqGepNfz3KPZCWZbHWafAJeshs9Vg9LBy--LNSrlOpe9E3drNEO0Im2zN0pwjq7sWhLCPjVYzAIdON5By8lRxx9ecDNZjB2rifFDUbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfFidSJh9YCczXSzgENEoa2u2__i_dxaWC3yyVQOnA7VDtFUygyJSF1-c4gaUPVj76Pow8uYC0AvCmlMVcaOOPZ2dJB9LEsgoXUSTyYUjuC8shgP6DS_PvfQ1KDo8pRck01gOWpG2PYwMiMxOHZPTpxS616IGgYPQuZHH2b4O89Znwr1Q5hgA0eFrLGIK3DV8uJ9teaeqj0b9WXsczBXMaIYBKTtMJt_9aqxmjxDZPP1E_KW_oHlFauY1b462vvvg3byexwnn9VxtkuK1DsCFmPC6EX6H9XDQajMC621UkqV0rRYMP_kciz7WJrY6KKuF7yg_moaCbrHnkTO4ki6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VVWpXp9BOC55ay2qHyjFaoavjfdFGamaJ_CmuRiWuyWv3NRDHeIMQ8jq-NeMHe6YLZJF4nKGhYt38v_AHN4rHvznLo860H78IsjAVNYho26aeegX2-x1Nw9Vo_afFUai1xORaNlUURM0kenffVFdO1CtEsTG9NCtgNRtz7QXfj8iay3P0T5hGVOqSSNMFqbR8QRFXBm1GPwi0jEx4ByRNK0BwMfUCkjsKvkNfYcF8EzvszWtIZrNeSluRWAVfecoNQR-tE6u32jG-3dizlWV-WIJ2Z6ULr0xqYStnRjItHqq0R1LZGo0jQUqg8lfCW8RFKh1m4j6QvfEGRok_2RTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=SkeAvm8vmIy8FeMGeB2hFMgF1E8L8RnYaoZMu_XCYisFSofn69_ea4yK7u4J8pNx_f-QAID_LKUSlZgWHUVH83nnZ_4YsRFlp8PVJ-C1_aepmiSaLg88ycPpee5GqJMjnQxxjdSoynQLUKif_ghNXBdno4LYfDgHY9a480EZTSbwzCzp0C4m-lSwAgZDt1BiJZiGTnAaphlJbJi41x6FQHRKLNl3PmYAkKnyL1mX-8r9pp6lCnRxLyKyTGZmAFJf-E_qiXIhC2FjTJMR_xYkm9Qz-w6S8ScIkYsgY6ay7yAloGSQQM7y0pKqkvB0QxAnhkYupUaaaZsm3K5vkkMSWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=SkeAvm8vmIy8FeMGeB2hFMgF1E8L8RnYaoZMu_XCYisFSofn69_ea4yK7u4J8pNx_f-QAID_LKUSlZgWHUVH83nnZ_4YsRFlp8PVJ-C1_aepmiSaLg88ycPpee5GqJMjnQxxjdSoynQLUKif_ghNXBdno4LYfDgHY9a480EZTSbwzCzp0C4m-lSwAgZDt1BiJZiGTnAaphlJbJi41x6FQHRKLNl3PmYAkKnyL1mX-8r9pp6lCnRxLyKyTGZmAFJf-E_qiXIhC2FjTJMR_xYkm9Qz-w6S8ScIkYsgY6ay7yAloGSQQM7y0pKqkvB0QxAnhkYupUaaaZsm3K5vkkMSWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afhvTCdrnDaTwbmL09pug96wFpDfri0SbN19DBP0AsDJyZVSs5qZIH2OxcwgjfIZm6VcDoJe12kHt_Xaom24cdnLPj80YAJKXRj2SMuarre6q4REvz4rhaV6REEg1vaUB5SfwykX3vya7t4UlLN4TExlxXdd2jhU5n-pe3StaA12tLT3VemSCb7syGmx14WZM9d-E_dGRRFq5ziCsAPgUyOGMWlu32tl7tIAp0YWBuZyzIk9lYRm1u0U1IW3ukywHjTDfYu8N4zVYfsRIjS15QEcyE2KnV0Y4yPVFIiz5C_E19ry56ihmGKd77_lEJkFzikfqGvDimloMMnM5eaPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRGexGRZdnqSwBI06DFQ1H24NeIdf2MuknPDwX-S09vTVyBtYFN4o9MYD1VwXNQPe5-HLjRREtzcBXqOzl352uXjclJ4K7luojVhaYIe48eEQroon4BppkRgXU1tyWMvyq8gYMtRfTGxzzhRTzpt1QcsuQAZX5-vYRyRPO-EMzTIecdF-wtbpeLvSTfAIwQaRLUtmVayZbiZolGUapdHEOUc1qtFHyQp3d4KuUckx7tLJpKRbpSIrOu4pnShQHyPjwEOIK93AKM_stHSvM3mPwdK-gT0kF1-fJE3QKv3K0vSDdh9cbt8ePqqbVD6HpAQKyHNDW3g1D8JpkPJ7H0z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxUFry4UloSHDlLhpjg9kLYLFv_L6n2RvtAJhuzVG_EQT4Cf6QSiZBKTJX8yJ8BrkuWW_-a5koTikRxIUdJ1p3lKOZ4IcR5RGJidgDcwl70Rmv2GE_b2afz4HiuZbZByZ3Q6JMKG6Z_s9ktcdxl5HiptwZBpxSe0H2j2PsJrc_PqFEx9_-3zypI4t1n282wM3eXumY2exrOoX2BUeIJr97EJWYZDWu6aIPr9J6ULZMbcGDcOjwzWV_kkjKPT6YspyfjtKmOAqF8D93ezT__dTgdAg0hc0GxO88C6XlNQ6ZJQv2ezrdJNw4ixJtA2cARb_SQkoqVQdoqVQP5BcuzHlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCKx-61UYNIBDj5HYcvjvGNSZaEBpR_olrOMLUG6wf97QsnuzQrOP7UAw_dXxJpbulexcJ9VIxnVztuChJgMR-N6AM4F65mxFrBEclIjrGh7of20jsv2jbvw4i8t9erhaw-fg9QwPigTHjr5Ydm3jnw1Ont9EmPZo6x_BEH4NiVcmeLX6Bm2GX5VrxEWvaKahZGqs4rOfiBEsZu3rcWoERx_vBD4tWT_iA5HusVuuhoWi1p3Pxsq0pCi4lUSMsc8kV68MJqfYjpQBfGARIk6qGt1hM1E5R_077Zvge6NE-FKHb2UwWgRABZ1dxYs-W3p11YvMfOLH3ZDEQHTq__CKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=AQL2aT2EDg56SMu2DCLjPSCylqyrcRf7orqKDY19b2Et0XkyIZfWQK7RczIPqJbXAhDVuEzIP6vNNgFLFgLxX2Nq_nE8qr5xMwaTr22Hu8AIGLjmTujls-irN59m20Dr3LBwt1hjIhACkMD1Kaf3W8o1MypqL4UJPH2V7kKeyvvB-SFAAtheQTDl8O51wrrHG08BcZd-HXsNJSNRwmHUXYSWfMGDz0YhdnHpN5lRn7TDco5q4xtkSWlTy8B0CPtREfcX-zykZwttqLSMZIIMW8uABq921OvRxuWhlBZhNjpoSfx2iluztqZr_-z0-o9ninmT9EDrMzX-xxF8gYX6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=AQL2aT2EDg56SMu2DCLjPSCylqyrcRf7orqKDY19b2Et0XkyIZfWQK7RczIPqJbXAhDVuEzIP6vNNgFLFgLxX2Nq_nE8qr5xMwaTr22Hu8AIGLjmTujls-irN59m20Dr3LBwt1hjIhACkMD1Kaf3W8o1MypqL4UJPH2V7kKeyvvB-SFAAtheQTDl8O51wrrHG08BcZd-HXsNJSNRwmHUXYSWfMGDz0YhdnHpN5lRn7TDco5q4xtkSWlTy8B0CPtREfcX-zykZwttqLSMZIIMW8uABq921OvRxuWhlBZhNjpoSfx2iluztqZr_-z0-o9ninmT9EDrMzX-xxF8gYX6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
