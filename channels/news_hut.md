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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 20:13:28</div>
<hr>

<div class="tg-post" id="msg-64961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgmrUZ1Yre1M4d9ZPIctvlD2Z83yu-FUYYEiE5PitQ3cP9nowFzhYr5WACOaDOaFkJZw6rgA1NHnceskOXQAz7Q066Dxc-CeaVcad38w72wENVkTGmIkMYcULrcTeSUxVumd89RmJrFT0a6evpqbxpJqs4rhbhsDP7VlQmHsc1Otaah8DIPAhr8EODApPEoNAGXnNGFLd4bMzIfHW86c8mdlMT0fPPQ116T60bLec5qnAVgfuhnF7mDewx4e-Ij7vqatxC2HWNbtpjDWL691VBPgIRuabhzEgHlDqv35CRxLUN8p_2TprxjHGoQwqxw48T0TfU2-aKg_4t6Y1faEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
«اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم» در حالی که پرچم سفید نماینده را به شدت تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌شان همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی بزرگ و باشکوه ایالات متحده آمریکا بپذیرند، روزنامه‌های در حال سقوط نیویورک تایمز، وال استریت ژورنال چین (WSJ!)، سی‌ان‌ان فاسد و اکنون بی‌اهمیت، و همه اعضای دیگر رسانه‌های خبری جعلی، تیتر خواهند زد که ایران پیروزی استادانه و درخشانی بر ایالات متحده آمریکا داشته است، حتی نزدیک هم نبود. دموکرات‌ها و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آنها کاملاً دیوانه شده‌اند!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/news_hut/64961" target="_blank">📅 18:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPBLePufAL-uLBfwCt2dSCHyrdue-5VoGQ2rooCcJuQ6u9nM2ABKWW12HF1o4BTZrYpkzsE_I759a_KqKV7CkcSQ4ZenAiFJcBw6ah0VSefEmqdF86lSxn0pYbKxWAvEssy5nfDwS6DZqpB5x9CFAT8qjZf_sldXpD-q6UsqNBjnBnGHfmZLG2NdKIDUjlGqTdKYfbgfgzMKvDdK7JCIdf2gtRJiY7eaz4yPp66yd6CzWr7uuNNe-6Hl-kp_9BM52BC524WnpmRaSSolvTL5lmm2dfligjqsWtKcnl5u36uL0w0G0LyLWVKdhmjUfPyaNA3y892DfGgYqhAfu9_0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0e7TY39qUxSg1bpkG39JX-ELps6sXz0sKCD4rMqDwVnGaGU6AwH88TLFr9WJS7lUlJYueEVk3c9Yn_g_9NaiL2gsIf99XVLD9GfVH2akTpcARtbxjYX91S7fPE6wc9mVPRNo8eV9LoxJ6jc6FEvMS7rLfiNMJWFhelJKid906YmMheCU46lXBmSR1ysKekqwAQ9wwac7wZWa3Wz8de7BCwA4dDR0a7WT68vWR0JdTnP1nqj7x0EircPLAiGdR0Hkf-aloj4PK3JnAWd7xAfEbh-xSKVg5C9pNLBkKv7DEP--e0dt1RTTLw3v20oDf4MvYS7inlE03KsRAE2KUW4ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت خودرو ، ۲۸ اردیبهشت‌ماه ۱۴۰۵
@News_Hut</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/news_hut/64959" target="_blank">📅 14:37 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/64952" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmu58epFkcfCr_UGg4fWuuwjLqfTKt-nqYataDaKirAb-zDmyf9NN19aOe65JGiNR7mkc1JEEL00-4iiELZ1IYcAjm97-xj_FymFTbEn4QNdTuzhJbMBGFd4_oe3hCH7cMywHEcIKP54eIQJaSjfBsXy4YHFMsY7weeWuInrjto9d7bck_8LVAFmeFMkRQqnQ1flvYLXQtuth7-qViVYHPCKFTptq5QL725GeqBh4LiDfs6WTdQmx0hQHV0qPmPmVMdoC_qpm45oeIecR42ayLXPOAQ7JyhMHg5NGGTvKleq-odfYo7SjkWy1lyWOAbW6V9QRgfPCVXbApks7QtmqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست عجیب حسین دهباشی سازنده ویدئو تبلیغاتی حسن روحانی تو انتخابات ۱۳۹۶:
حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/64951" target="_blank">📅 10:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ILHEoGMota1M1K_sg6OLRf9SL3EwI3I8iY5oKNQ58LxmlMNzYtDlBnkw4Qz0aaaMMyy-ZZaWVvATqBFcTUGYMNX26YL9SIekjDrs_wJ7Ec8TVVaTo92GeSNAZsYHnLkvBi-S4SpioSqBQrbLXfCPrKM2Q18ZPwdanpZuvQ2RpF3lpgi9z5ab6ilGy3LkZuDmrWpoCQ1BJT2LqZ3WfeGIpn4jUN-K1aoWgaShvHButlK1i1jF7PaQTWR98ySkrTKcEsbXvuWixoWw417-1Scox3KLtjIVRJtmDH3ohS_0_U2k_DVXecxCViuzKpWZkdBGh5DyFz7CZPtD5yPTNdOchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در شبکه اجتماعی که فیلتر شده
روز ارتباطاتی که قطع شده رو تبریک گفت
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64950" target="_blank">📅 21:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64949">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64949" target="_blank">📅 21:06 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64948" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64947">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یک سری کانفیگ فروش طی یک حرکت بی‌شرفانه برا سرور هاشون ضریب گذاشتن، یعنی شما ۱۰۰ مگابیت مصرف می‌کنید ولی حجم مصرفی ضربدر یک عدد می‌شه، حالا ۲ یا ۳ یا هر عدد دیگه‌ای  اگه این حرکت کصشرتونو جمع نکنید تک تک اسم می‌برم تا نه آبرویی بمونه نه مشتری‌ای @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64947" target="_blank">📅 19:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64946">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تسنیم: ممباقر گذاشتیم نماینده ویژه جمهوری اسلامی تو امور چین
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64946" target="_blank">📅 12:44 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64945" target="_blank">📅 10:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/guw7xdKKGHun7SMwDrmn-sm2DDfOY3rJjsPbHA5yu4i9Ye3eSS9pSBXZ-pbizK99BJovXSkpDMj0Um8sg61QYPuQ0iqt1XPhfQA9NMytmyUnjxurQVmPqh2f0GVCajNcBra2RbXP8VZl0SEm7HxF-jhn7eYweGHKrpJpeVJq1niipfdMhLjzrcO21H026wLKuHJEoo888FN3hcXWsLc1H_y0ob2j0mvjWfPNniZPHo_hpAV-MhTDc15BsJwwiJeMFgEHCX5waaoEZNOBmRFbHNYNdF5r9zH3aB4-inDbaxiWvzMK-uDultRLRsQ1rnM4RSkop9rmkYF9d7oYTEEZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیلی‌میل: کیر میخواد از نخست‌وزیری انگلیس استعفا بده
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64944" target="_blank">📅 07:55 · 27 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64942" target="_blank">📅 20:31 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64940" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64936" target="_blank">📅 10:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64935">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل گزارش داد که در اسرائیل برآورد می‌شود دونالد ترامپ در ۲۴ ساعت آینده درباره اقدام نظامی علیه جمهوری اسلامی تصمیم بگیرد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64935" target="_blank">📅 10:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64934">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عه امروز واقعاً روز پسره؟ روزمون مبارک
🕺
#hjAly
‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64934" target="_blank">📅 10:33 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64932" target="_blank">📅 20:56 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64931" target="_blank">📅 19:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64929">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همه‌ی اعضاء هیأت آمریکایی قبل از اینکه سوار «ایر فورس وان» بشن و پکن رو ترک کنن، هر چی که از میزبان‌های چینی گرفته بودن [هدیه و یادگاری]، همش رو همون‌جا انداختن تو سطل زباله.
دلیل این کار احتمال جاسوسی بوده
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/64929" target="_blank">📅 17:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64928">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne6DhGJydiz4yJAjBLRyR6NKYxcs1Wsq-xjX2u6D0cV72taXWXBuk4FvVMakAOVTonahxGU45jJHNz2QWyT0Y2MD2zNbEeQu059RhFBSL1mZLjaJZec7VbbNQzmkDjTBOmLNNBNmMT5V377sEPWsKSqNGQJsnBTBWJ_08Zo0DGV71zJ1q2DxNgIw7O11jKkvLdy8jPeHpmSoU48yCAc7fDYiekolZjhue8quP88UgTR9XZLLGSfC06rkUjDR86udanABs9D-mJeNB6Tn8S1jxRLylQx45VDmjJyLhMvhnMhq8JZyPrTDJ4jeBZaj2w9By_POgXqWXMQg3LOk7RYL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64928" target="_blank">📅 14:47 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/64921" target="_blank">📅 13:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo8yOIVtpQ9GkGYylbCFKp06h8UUJtqTZ6pxsgNd7i32SMDKRqSgvI4yqzZMCO9uYxJIL9r5iIR2jPhtFadFGEpg4xirV_GV7LeUKQ5hB7SwgRfvAqG3jLz9d27S_VKxfqpdgnCOY6s1Eu6vGJILaDLKsOxj-7MefVLEFFYbGZV2_2t2FEb0ZeJUJ1CgmzYPQFrOjJIqT8yP2hLvK3VP6YtYrwZbx6OIBJBqmWGb5WPbg6-U7Hd08Xa4AV5vCAnfRoWPkXpmFTowaqKzFDzqCHRRFbbrwa6QnlBzQRV5AywGVpo-Sl7wzCEHMXUB-s2Pu8Og9HnIG83l8AZ6mFD_sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/64918" target="_blank">📅 12:45 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upZHQIGJT8EhAaO1aC8BX0mmbmL27erdp44qjdNiC2SAIoPrKkvcsoIcnoGK5lZCAoYfYuGEMaomNyIfXzU-0R37a4WXX3cgZzrSV-kyt7Gv5HhZbEHmyIO8P-6CM1P0Sw3kBSeZUNFev8Q_rukp56SKgfIPfDoYfdSZ22fzjcmyHVODXNjfRcAnqe2bacUof1x51HXl7CVuk9jks_t9Va59KX3y79XvGLnbZjwyNIgIfjCaHS41iBc5TS9PgZs8VEt8WHfnv2a3EY7_jgpVp4xScgjlo1jmcWiPdN1czX339a7xqUmQ1wdifJ4XBWvT2jsWtewA3u5UM-lqdQvdWA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Y9nuQo2M7L045sutY9cIc2r3r6Hoj3ckD1yMiHclBvNHY08ZPaixPxtDo0C3zIW-SJrPxesbJPGEAgtKvpQdSBH4LrgaoSTpcvn8OS9p4MzCUzTG2ldBkYtTEwn7eOGfOW-UPH2GZ6I68arazydBF5NwSnyiUZKfyE70t6Vw4O1urWqHuPWhA_t7L2_rSmj39S9sTE8JPhXLWRHxsy1dWY0_QY5Ms4FFLaIr6NN4z6jwnefbeWEoQqizAoEeX7IHss2rsD2rgZKBvAwkSmfwncdDCIXbPsW5MC0YrBlPKe3cU23DJsh2KuQCtW37AaAW-jMKV0R5B8h7w7CNr-kNyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61dd932f8a.mp4?token=Y9nuQo2M7L045sutY9cIc2r3r6Hoj3ckD1yMiHclBvNHY08ZPaixPxtDo0C3zIW-SJrPxesbJPGEAgtKvpQdSBH4LrgaoSTpcvn8OS9p4MzCUzTG2ldBkYtTEwn7eOGfOW-UPH2GZ6I68arazydBF5NwSnyiUZKfyE70t6Vw4O1urWqHuPWhA_t7L2_rSmj39S9sTE8JPhXLWRHxsy1dWY0_QY5Ms4FFLaIr6NN4z6jwnefbeWEoQqizAoEeX7IHss2rsD2rgZKBvAwkSmfwncdDCIXbPsW5MC0YrBlPKe3cU23DJsh2KuQCtW37AaAW-jMKV0R5B8h7w7CNr-kNyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/EiiLNSjIChWhzWiC5zDpUox1Q2E9z3ibi-CZJnQ5ahp71zQdYaQFP8PvH8Fgj7GWKWYFzIRLIIyowXu1_KsJseObBy-SMoCGIQFlgQ51yf0ozQXHuRoJdCNwP7x5PYCTTDHKlVoXUNcYPbMfny6ziB4Eamd7Anfsl-Xbp7gvZr2a3MAQUjqhxrm2NXMHIXBAEeAn4reSiKILHv1dyBxU2KLSSUSHjCQazeu4fwumuFX_dza4dxszBEFgvVyxWNHaUiYoZFXgCVN12U0Ms_463K6oAB2MWOIEoTvb_rMcWmD4XiRgbFmLrBX88wQrWLsfC1ReeZlBtmZ7miFA_z7KMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/news_hut/64913" target="_blank">📅 03:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kde9nTStnMfIQjGZ82IhbNHKQkullIftM548WtVw0aHaAozx1Cys6KdOJwHI5QHCiMeY-iUDRhLrFYEHag6gQ9rH15YyrTMuKAxyNYc8xenhDBXf9UGCWQaNN03RMqy0iIrhys16tZWQpqsOfv6nMfePViX879PnkWiayAz4gAq_VkVAMgklOpvJNIE3G2i09xYffMFfQUV8-5GIoX2ZNPBBSufSWAhi2l_k7j62WNGdBGYCx1WKeBj0a-BXZtVJX8r3cZ6vuR5vzdb3NA_nhnRsLOykpKp7uSuFu81RYO0wQ0b17jwcMagJWZbZZEVyRLYnDD4VC0Nhz_6kUlTo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=QaoNH8TLHL_svDAOY08ct-bhGBi1UEKQ9Zu54gMc48Gv5mhDcLxXlhnu2ta8HdiJy5ueLeytrtEvXkoGjcGB5EdcQnPFXHowiN_Rd8RGSLJI_TtBPePsp-nxtTST57FjL2FTOOro65D5aLUbj0V7RYFzoL47paTMdgbGs_VeO_e1rXZLDNrI5SrVj-uevAJPwuiO5fWskZjYRih3j40E_EUjjX7YXsenwWQlYdwN65rBonR2MCoCLt6crDponmMeJr-v2dYRO5z4fKI3lhdzERC1ZzHA5KXmVwrPsJ_31tLhIPTVLki8ZbU6a-GZ2ZA7YiWAbWDT2mJEBVRZNg_Mmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=QaoNH8TLHL_svDAOY08ct-bhGBi1UEKQ9Zu54gMc48Gv5mhDcLxXlhnu2ta8HdiJy5ueLeytrtEvXkoGjcGB5EdcQnPFXHowiN_Rd8RGSLJI_TtBPePsp-nxtTST57FjL2FTOOro65D5aLUbj0V7RYFzoL47paTMdgbGs_VeO_e1rXZLDNrI5SrVj-uevAJPwuiO5fWskZjYRih3j40E_EUjjX7YXsenwWQlYdwN65rBonR2MCoCLt6crDponmMeJr-v2dYRO5z4fKI3lhdzERC1ZzHA5KXmVwrPsJ_31tLhIPTVLki8ZbU6a-GZ2ZA7YiWAbWDT2mJEBVRZNg_Mmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thUmUvUNwLtIUR2Kt_bEXRl5sS2iSE26TX72jCaUbE5PdzOfrvScfwIKKfgq3GI7n6Q9oKR_C_1X9UT_pHz4NQQVS42efLl072g3BmiT267Hjf-FAtsXUVk1Mdi60aDsuOgsk1pVc2HN87a6ney333WSpUs6ltu3n9tmCY_FiYbvrfQyGltjRJoeArL4XafkzFzZaVGPvVEW5wCq-UoBYtxK3eTX2S2H0D5AKyxFN0qpedI-blzF-tZ4e4dOc0va-n4YdKXWA56JApxyhu7riQoXPGVdRxMubn6ZZyEwewb6Lj-haNkihwPqS-rDIDc8w-VY6AyRygn52wAuxUmggw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfIKiYBH70MWxmLf5_Iaruzgpx27SfQE7WlkBQ0qEEZot4ASybmfE3Lt8NbWKjKZ5JQ6oqXH6oqv6N95NxFnvPdrLQeyWWiu9M9IKrFBy1YmWvj4k-2zU2N3WtKZHr1l6r8ONmIg0LJKUFbx0xrTPP_w_Nioixh29D3tUU0VI5GXCOL4JrktkSCS3LwngFD8RL2UCcvcY_lDoFJk_ZadBX3XCvoCmPkJh98h4tZ0jFFOMXhYRwhTu4qT02rWcfT8oLAgGmod4Dp9MruOND9oPaLidWwd2Nzs41M-CXGFxKxMqoNR_OVI2HYG17ZEelp9Ddw-abmbvFYGGM9VG6VXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtyVjIS11MVSiw57C_eTo737K3WN8XtUR5ZLW0o_atsyUp4gmS3zSeX_AUN3EpB3Gbjto2FtjuU7WB17wlm_54UwPrcljo8ObTGFVEyHUwDsdFvzfDjv3INv8UClnEjyqZM0KpvYtB2xuwKz8dY__MBmOG7fjsoETpshEll2snxCNwIu8lT5qg9oVc0P6tVfnQVEN-BGUEF_Qr_R_slQDFWWa_rlhVrW7DBbEtHaNibfGZGg3AcHX8x-HEvsrUHbCNvPzWALsy8drTIOLQSaGe1MDVFzISRVk6ZVAQnk4PjPJroSpqMV1DadQDgmmdTArMe-UENxBFnN-Q1PzbjyDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=BK1Nfn8pdgFJwHKy3woxI8qReAAxjOhS3A5uX0nc9VI0OAer6YjAEoiutTp9vesLVGbn0w6IZduREv7hkJF1TzDb4ut8QVEpvV8CbaxOylYkgSxhbbGP5ST5cERusz2s6_R6UKsbOO6SxzcVa1ZBqBdA2hbJCxZ5D82HFoh11jh7X56LR7_TOJntf0YltBXDbU-Lz0bqnNja92y3ASGowRKLBpAO0NG2XGt-CFe340KXT_XNtB9cHEV-p7jMChe2aGGnce5uLO8lzJsiy4G3TkMW6Yw_zFZ2z9Q9NAP9hL8oraNNW8m0w66XMwA7uqiqL1FCdtwl_J9ylgDNIbfMHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=BK1Nfn8pdgFJwHKy3woxI8qReAAxjOhS3A5uX0nc9VI0OAer6YjAEoiutTp9vesLVGbn0w6IZduREv7hkJF1TzDb4ut8QVEpvV8CbaxOylYkgSxhbbGP5ST5cERusz2s6_R6UKsbOO6SxzcVa1ZBqBdA2hbJCxZ5D82HFoh11jh7X56LR7_TOJntf0YltBXDbU-Lz0bqnNja92y3ASGowRKLBpAO0NG2XGt-CFe340KXT_XNtB9cHEV-p7jMChe2aGGnce5uLO8lzJsiy4G3TkMW6Yw_zFZ2z9Q9NAP9hL8oraNNW8m0w66XMwA7uqiqL1FCdtwl_J9ylgDNIbfMHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QbGPr9NbF9xDipgGwngvGilMHGRVS5YinbVRk6QJo0IwRwZ26SBbAwrxPh2L2P0Xer993Kinc1BTmTCUFsxD31a_gyV6oSUpzhMuBw2r3OfqcvRjz5e1JNnJg0S8hXAmdkfSlHNSOFPW1pKEysRwfGdAigSAJzTZD8U5tER6B9oGWWc71gktWSrO_V_oIQcZzx64WmhH2xKOEt7rbTMgGugZRUXVU5goDEaUhmdu17jnm9me3E5wP94PGIpTQdvkZJGTz-jmNsdKWQjyn_o3teicZIsuaDdu4zOAmvdXiUkcRb140ibmHGvOtQupTVDTRMvpJPAmYfWtQu_yjfJhUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tliX8SHMv3s7Ndl7xNrqI4ZIWa1TQYqFvMVlyLR0Iyp9g23Vy4S0_pkd3lSP9jbaQOeqrTez5sJk1rzaPNJ2ODlQhOFutmib-hcNZGSGcgDxanNA34yKLl7yehQ3S_TDcyN1jen1YQjDDnkO28UeHmGCyon9HLxjsylnpGfzpNsGICgexgrh578vOnUQN2Me9awXvQZDq0-Bcxc52xV8fc7I6J1-NPMLGRFdNI7-SsW6ARkIUUTdpuwfhyqXqiHOe1b8fy3SAJ0TumtdhBfDo4jg9GRzGjem27qkI49yHVA2MjhnmLE6iR_h8e9gEZAq41IzhdRBxYaYUFFXG_y5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afadb-eOxN-6JUzXif5hVeO9OL8F6emYVgHnPe2mfsgFeucVFkFqdVShWBvObjmfg1hX69iBP9UHy7nxJBsTFn8UKbcqEKjati_V8Wq2Z02H2QEEj3AgaoXDHmxHYO82Kp3EMG3CMtTIQhK40NRWmES1jG2tXJcYHtNcfzQWqsOJPE4F68WG2Egs0gQralSserbKXDUwSmuD5-bN3SlMsIFuFgANl_8FxoaRcxbBEIywLwI7t6BYKBW9EGM69oU-gNy52AzhBTuH7qzt1MDTNEk0HI2NF_v7Di_D4sqM5vkPij6GHEM8dB2yKcbgtY-jiEz2X1fYuVgQwCwhpkmxFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X-Hk-oKxq-YquB8z5yN9PwcDfeYP6i6cQmf2dCILbLfs1FEdjyYg-KH_HCXoNZVB9slhc4-KrMOjr9SWw3VuE_-Rm5PW2xXGAA-4eCYISFBEK9xKBnBvDw2Mn427Q8L26Qyj_gs-IxZivSEc5D6JLulq7onhfJYJbA-Ca2-zlsUniZ33mkJnOsK6ZtyeCJZwUKKz3uCKekHh20yiiyEG8j2wJAusnN6UganvZBwE7I_-u_AjU3Bpp4bz0uofhuyst-Fe3lJyl6i2BV5JVX2ndBVxwIXo3JRYbtz_0i2LT3jXkLfdFv2cJJnf3yifoDFbUpxKA5TlhWienJGiG-AwLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STtnF2DfJM6azm4w3pF-pWCPOwd3awRc6XbzGgrjTVK4VR-D_aluOBRzmKLvG_7MZC8oSmKAFEx0fiAjTZ691gXnsuzCjhOGGHzgO6-lOUlvO6tumyO8l4kXZdJI8AWMsEFIwwXJyvgeRjNche55g1xte8jURHtXU1bjDYEzg46mVND5zoq6wPmyYx4Cob_5yKJNyzyUh1Tt6Eyb-9ZTQI1LYA-jXzDhUxNvVBFxhiDqOJwkjTNT358yV2AnmQXCHlit1RHvQ8JwfV7w-mdb6mpbKL5iqEp3Ns6lwLFjjMeT5FPq_W5CzXB4x79CNbEfjSomdU2kb1ueRjQmtd-Xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=dbK3DOQSEjYavpTj-dwl12inuXjNgZC6TC7XIorjnysobrj91wd7rCp6SU1U_ea_MmURkcxW-zjheCul5FFPriU4j4r75D63J3QPvhFRfIN8NENpbR-aNgvy36yuWSNVnACKDCSdA-VppRxkwLc_406zcNfEIgy70Wpty-MAZjauXE_u9t3-_XhkFZmm8CaWA68tfhrng1OdmB9XVCLWLE2roglk209Qgb20joycu97Gt6dAmDa9r3dgqK3eI_Q6_d9lkCJsBq5iZZd__G8x_TrztF-aLjMf1KwieMcfkH3sPalm-JZiQSXwDCYFBd3qJMuwoN012mq82PYB50R7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=dbK3DOQSEjYavpTj-dwl12inuXjNgZC6TC7XIorjnysobrj91wd7rCp6SU1U_ea_MmURkcxW-zjheCul5FFPriU4j4r75D63J3QPvhFRfIN8NENpbR-aNgvy36yuWSNVnACKDCSdA-VppRxkwLc_406zcNfEIgy70Wpty-MAZjauXE_u9t3-_XhkFZmm8CaWA68tfhrng1OdmB9XVCLWLE2roglk209Qgb20joycu97Gt6dAmDa9r3dgqK3eI_Q6_d9lkCJsBq5iZZd__G8x_TrztF-aLjMf1KwieMcfkH3sPalm-JZiQSXwDCYFBd3qJMuwoN012mq82PYB50R7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FQWpYad7uFM5VoJHzluBLSC_6wIO-NO3Scd-CP7aXdibcnKn0yr_WIpHIrDz-bOmsYffRf_RxSPB-RgPbnb8sHik8ngglv_BcZwKZA50cnlvvZaE8UAZ3ND0Kj29VpS4L2Ea5_fdFIvlzhTMyvs8OU9dH00jnlwKXlqleuomunBIrpG72pRcHJvxzGZUDGMDJ8-Zvn-QKQ59pphqk3qrrH-8GToG2keqxZL4Ds-yE8dVXVJqzWpGaGW11XCLYY3gmaUrIHwkKysNWFGE1vhUC84UqgzknEyn_2wEE-68KtEts8gxF9Y076vtsrA7OHZelxYw9IgB_7j2-0H61hV8Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrgEQSFJ34oVfcRXDzAdWhPzHebL4t7mb1n8fWdYHBWRXywVe0SvBPhmR0y0rBMmoHR0KIl9FIVTI4W1f4dYmIVFg2NQJfIVhYzZBVEAe-Z6mMaJz9rffYoaMvMExNCDywBQ_BUD3dqEGToPoI6FpeSNTufQ6g-UiyJ5kdl4iujpcr5bBV_z7s_Hoqmm6jIrh6kQMrB1_yU8P8nN82BeGeONxhZEGEZqWnIPQUGZa55Iz0pk56pO4CMlTRkzCrLXZKNTZ3bvZkNPVqwe9hrg4VHzJq26eUOr5pGKROLGGGnPtraErgFz5sJmeaSMwTMi5YZzybPKxyOgpg95z2mUIA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=uMVwZrzp4PAuSFef7eoFpGW4Boi6vFUaNs8_K-TOt7v0GV2k2HsRxOykm9G9UazDmauHcmSAY0PGQ7bLgF-p8aj5VpbPWgSWX2z4m709V-TMg8770dkX8poor8qlXgpfduLrMhTxybx3GXbN7elfV1TtU3b645gkr8U20ng-FS8CMVr79PAAXuYd7X1_UV0bH7BEbobl8yTVzsAw42Z6AuIuNVY4GQNECPDNQ2lzwqFZnCcJv9ef88ePl7buYwSj_Hru1GvUY_3cq6jxUU1FuOqrVizYTVxuvgPpWWZHrkSNSzqoaP8kpbBXX9-7FPfI4J8H9QTwCQdEfoxPlItrVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=uMVwZrzp4PAuSFef7eoFpGW4Boi6vFUaNs8_K-TOt7v0GV2k2HsRxOykm9G9UazDmauHcmSAY0PGQ7bLgF-p8aj5VpbPWgSWX2z4m709V-TMg8770dkX8poor8qlXgpfduLrMhTxybx3GXbN7elfV1TtU3b645gkr8U20ng-FS8CMVr79PAAXuYd7X1_UV0bH7BEbobl8yTVzsAw42Z6AuIuNVY4GQNECPDNQ2lzwqFZnCcJv9ef88ePl7buYwSj_Hru1GvUY_3cq6jxUU1FuOqrVizYTVxuvgPpWWZHrkSNSzqoaP8kpbBXX9-7FPfI4J8H9QTwCQdEfoxPlItrVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPNf9T7NL22y-lqA1o5DKGdS5QUu1QbvXGxjgJOgyT4QLPoWQ9PhQuMMDZecSYgPYie3KjFTnaM7zjzcZH2gaFeEHXJnfjdFVlSsQHrjQXFeGIiY3rUXRycsyNrMNTM2CmbUJQcVuV4i81S0Xc0buPgKostfaiYF1q5T2tbPD2yJPoCsbqEe4f7QdLwuVJVEjxdXDoHeHjJ1Kvvh24-FhXoJTB9aT2law3fCgCtYQgTTgcLkwewt3HjWU-9tdoNvt1GSeBdtYZEUPa_RL0kds_VLDaRXrRAlm89Ef0yNsBMbrW-gO_rvXWIun_0B8mycx2lD5OlbkwnXS969sqp-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/T3GvJ9MzAfQZWdpIxLLA8RBZHguBxKpXiIjQhhVrKEvb2O0onv6rf8jNf8FaIqmFqeJ11I-lNSaxFX-Dje8vkxpb7THvJAPJD3O0AHKrITzshRLotmmHuEBUg0_d63NLR4tKmzzPxKwt02X4VQar_E-aXNCvv5L9PbPOrwxWSQy53ziQ2FmHuSrckgBEd8Aip6AMNuWl08nffFj0XaXn7EsJR36TkW_abigOI62JET4m_bRo2TtX786irPIkg7rWP219jWIg27xeV8xE88g7xt7kNKwNfLcpVTAVH1eCVXAmacH93x5bCB-p6DH5K4vnjZImqpiQDrFhi0G5QE0wCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud-M9i-w2E_XEsG7OEd8HXjVTaaPIiVBwINIMJMzvdHsZejGo66j7UkVqCShzDlS4-rwckI9_EvCRQXiDIKdrzQmdPF8CWv4n6ywc7XGfjXn-xa7__6P6Vb0cOWs0mH3bPUceV9wNUR6Uue1nuFBx1r9rqvuVIoLoUKaguvpnAzJqivK6y15x9NcMp2-TXtnjVrkt6yDhvNrsnXgw5r31hKq8QsZmykJaoL1y0K5Cl0BEj0Dwk3n9biN-ZmoDu_XL-p7S_akQ7nfX4k_huCFip0eMDHPQKUyn7uvRuUo2nES-Y7TVxzMHCl3ZazQrjOXCLtiIOePyGvHcPCePaslrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIjX6gaIIua8RnZeq7PL868Qd0PIhKNHtDTlj3CyyTw5CiblQvNdVbbl3kVluWWOLRIzbyyBmtaXfzlphv-6rdA1K2gLL2ZP9QK6DE2bFGKjHe6gBv0DZiJ6x_L2x5RaZCxVHh8zE9dswwM2yrM9mWvvCnNimW7HSxT7FzOoea2GLbBaOxvN5s8567KgAoz9X1E7PwGR0jBoNUkxVoIT0D25qPHf9tP2xMAsDX_20sclzfZ-TssNU5M-5pSuoP1ZSVvYHF4LLPPwDascJu_GQbDkG0XzJm4-dyravCev_oXkm2LVRbOyOcdi9i0pxIJeg75Od3UNge2c_qgngh89Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=TO5dktf-44vtB1JROnJjXKSOm_JvK0KklvEeaQxrMVpRGb_1qGF_GsUNqD5664a0kCOjrG_OTia7eaH3nuc0xP9y9o4u6nH6HADAFYv6nctJ9BjsQwKlE-Nnj4D0yb_u27C16__5ijNDRRE0m_jHe78MqaCNBnrYYzBnd3hdU0NUXhO32E4dNmQaX5--zBIUhjmJLDvrph7dDin7vB-j4NPX6tff61g5pSXECg5SxKQng3C0hjZOgn0B4Di2eGjiDRdWvbK1rfEM3szsmIc8ygvlukSrw9K6oPxQkfJcZO0Ojv3K4WMBrLmuUaHvVnFrQmDZHvzN-Oo6RQU0K34hPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=TO5dktf-44vtB1JROnJjXKSOm_JvK0KklvEeaQxrMVpRGb_1qGF_GsUNqD5664a0kCOjrG_OTia7eaH3nuc0xP9y9o4u6nH6HADAFYv6nctJ9BjsQwKlE-Nnj4D0yb_u27C16__5ijNDRRE0m_jHe78MqaCNBnrYYzBnd3hdU0NUXhO32E4dNmQaX5--zBIUhjmJLDvrph7dDin7vB-j4NPX6tff61g5pSXECg5SxKQng3C0hjZOgn0B4Di2eGjiDRdWvbK1rfEM3szsmIc8ygvlukSrw9K6oPxQkfJcZO0Ojv3K4WMBrLmuUaHvVnFrQmDZHvzN-Oo6RQU0K34hPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G_Pc9FMOjEP3i_4Y02tRkeDUYQnc0ycKWrXCVp3zfOXkLpUIbKhYkswwRtUjku6IHE7561XkBKiE4oeT0-eBUtQXPHoDskehZ4ptYeDFB2N0WY08pHdu7MMmxT4YUxjsCZZ3O_Sed39uEvj_s9sa1hKX4_Gaccgr50BKLXYrdsdovG7TGj3b7Brbau5BKXOT_Pbj5wVgLmCcSZoXavkShtORPEmVHa00mn6GlPU9cXB44I7yy1SDSdBZh4_Whj9kR8d3J0KAYuWNIe--VRRLCYxOlwF09s5JSCVND11TbzxC6tLpBCL4qp9HRrvDlfDvZxeB2DBfq9EXA_tr76mLJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8A8CishwYdE7L_ldRiYz2-DMXRdkqZ3cny9y9QrS53e5BFc4Gy27_dtuJtKtmO-osNSsU05t3m7It1ahF9JYYfiF4PSc9vfYlEAe569O_WlUsMpKhuJH8PmPQ99hfrVXqWjQEHOQIN282a61cNaxvnUxxsuQlgipewjIhyauE9TF6stZ6n5j6bsEibidb2_K14NupCnKHDapT2XrcgFDNgbf9sxGP1RzmSD20mg0PRJsBMBuBUfa2pnA1FAGaetmr1UeBe941fDzle04sXDy6iwpLUpyGtyZo8eWo5PgMQrfCSJX7k0JkyRff1GOI9UwLu_5nxOseu9Ra74dyQ9dg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=AKc7n1SaTWGpvRtyMsF5eOZhBZDrO_dW7Zk0WIvtI90AKg67Nccx4gWZdEVmfzTLExJC3vrvLEQJVMnGJZtv_Csb7kiy7wT0BoaoXh7VdIigvYachQPLsjqqVre5zcaWg-lorop5qNdOIDT4YpFd2Pk1XOUKVIKfnkCmR8bYOHqXaYZoPQj3jbXCZPmmVAktkZ-FXahgHWP_TRJremajX0u9XZa281n1zTrekbjyAoN69-9NXABfTqAMSuukrceO2iPW-Jr7iY8RS4ebXEV3A4CqC57ndu-a7pNsUrG8ch-yr3HQJ836a2ojgDp-4qBlWfYZUZ5u9GQ0ldthTiJ6QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=AKc7n1SaTWGpvRtyMsF5eOZhBZDrO_dW7Zk0WIvtI90AKg67Nccx4gWZdEVmfzTLExJC3vrvLEQJVMnGJZtv_Csb7kiy7wT0BoaoXh7VdIigvYachQPLsjqqVre5zcaWg-lorop5qNdOIDT4YpFd2Pk1XOUKVIKfnkCmR8bYOHqXaYZoPQj3jbXCZPmmVAktkZ-FXahgHWP_TRJremajX0u9XZa281n1zTrekbjyAoN69-9NXABfTqAMSuukrceO2iPW-Jr7iY8RS4ebXEV3A4CqC57ndu-a7pNsUrG8ch-yr3HQJ836a2ojgDp-4qBlWfYZUZ5u9GQ0ldthTiJ6QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBcEnWk278nr2n5roDpkqb29DHfAlIT05E3hS1qj9HLi-xOEpcfJ0qNC576JvEvKG5Pi_HxGzuxZIAp_log6ksuwgONO2HthbcBRx-b_ecPdxE6tTC3Tq1jItN4PaTCUplgAJVutdKoiAIamBnUPZUNTPwtMgBTyKKcpazVHHKi-Jd1sbtH6y1xMBctNSSTWT9WI5s3StHBuNrLb-NH76XMrSphM1aSIyB8pNK-L1S-bPr6QvnTqo9OnH0-1pww7XBmxm4mUvrJVdYxPU8eOXKnYRfxKJhG5wxFA9DhKX_j_PEgEXUGars1cAjHgsSt_zufpqTisBXjAPzho7x-C5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=Tm3YniPjvyuf2xFQu3Wwj0llifQwiTmtE_mVt0TVP8PUjyHCTbQZLL5z2JUomWMO_bxP2omdJ9VeLoQ8H_c80mMI9dqY0RnsCB33H3POHwxIfM3S_KKFbUHUsOC4EhmcGNapKJKwGNYBFnT2GtQc76GphP-Jat9LLVfjU3zKe71Z91Y2swlSK2ehY15K1iKfculsvHYb08--nWZYLB1Ri5nMErsiAE5yeYqtL0X_1QYgB9ef99oyGhsen7lI5LHlX7YPrbdkJr0h3SlI--gvY0dwVHsMU1KZs6m1gSC3_gHNL3yBEbLyNpQ6VEZLAWnWLuQXhEiBgfz646Xr4nzEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=Tm3YniPjvyuf2xFQu3Wwj0llifQwiTmtE_mVt0TVP8PUjyHCTbQZLL5z2JUomWMO_bxP2omdJ9VeLoQ8H_c80mMI9dqY0RnsCB33H3POHwxIfM3S_KKFbUHUsOC4EhmcGNapKJKwGNYBFnT2GtQc76GphP-Jat9LLVfjU3zKe71Z91Y2swlSK2ehY15K1iKfculsvHYb08--nWZYLB1Ri5nMErsiAE5yeYqtL0X_1QYgB9ef99oyGhsen7lI5LHlX7YPrbdkJr0h3SlI--gvY0dwVHsMU1KZs6m1gSC3_gHNL3yBEbLyNpQ6VEZLAWnWLuQXhEiBgfz646Xr4nzEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=bsrDij2_A3zZZxCcP_j2Z6xzws0dN620Q8Wh11hKtzXUPlZJAh4lAesyam6TwNygHmh9dYzE3TVPoVcpytZvPheIO9Q5Y-gqJ2vY9JBPXLn7Uy7xMXHJOCTbkJPhP-ZW_sXi8ve8iEtGdpnBTVHhTE6hrCQGija5G3X7p01QHkFGKva2lTifgpEYypTMGf1EEbcK707P8z5-KuLQ-N9DcM299lw3EC8OCsvm4SWIPnx9bNr4BzTlkIWhZ6wlsyAKmyeKpVyy0q-JO9m8eojy5FM4LMOjKeShsaAFqWyPDeamJmNW5KkYlvdLDYOBwQ6leKvUXb9MP19A4uZTdG1Xfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=bsrDij2_A3zZZxCcP_j2Z6xzws0dN620Q8Wh11hKtzXUPlZJAh4lAesyam6TwNygHmh9dYzE3TVPoVcpytZvPheIO9Q5Y-gqJ2vY9JBPXLn7Uy7xMXHJOCTbkJPhP-ZW_sXi8ve8iEtGdpnBTVHhTE6hrCQGija5G3X7p01QHkFGKva2lTifgpEYypTMGf1EEbcK707P8z5-KuLQ-N9DcM299lw3EC8OCsvm4SWIPnx9bNr4BzTlkIWhZ6wlsyAKmyeKpVyy0q-JO9m8eojy5FM4LMOjKeShsaAFqWyPDeamJmNW5KkYlvdLDYOBwQ6leKvUXb9MP19A4uZTdG1Xfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMC8NZql3Lpbvbs686ZvGA8N-MN-WQPkMh6IatfisnyWkzPyx67y1DtCAZ9fnA9upwPIgFESeTnJhtzK1TdKEqcd3wvaGnS-z_0E8dVubPPsxaxryv9aVWdzvDpJiOXYpJ6ndJjMZArQ-X3f0N_HXG79yFdJ_SPe5OoAUkCURIOZ5TqyzxHnVrQ43_A_opEmfsWveN26dsNZ3Ol_8_tPK23dzimXYtsqCgWKy3pEm7QlTNzFiOWOqpCiYvYJSAHupbm5SlnOlJxezXIjZhPa3jB5JpQoHcNluQwrJyKb-9ID_yMJ0CjuJ3FIoYN2svWCbjGHypjiWjtluPBOfw8QbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/seBvL9ScCEUz6A_vQDw6t0u-jlvXbkn985Oj8HraOe09kg2XNGRFuTR26Ah9F5n3cwzQ_hSJXca1wSV-JdBnAtKYQeqz8Nbs8A0k7WmbQUjsQaRe7hVZ5zwrFcrBKiMz6xLkJR8JRCmtuf95tn4TF_cBxSZvAk3Bewy6KC1O_oQcpUhd5YK3Hjbhob9nldYbg0nFvfYjRx1GpZ3VoNEAcg4ASG7RSUbj8xgRD-4F4mrsb0cVNonhnneKzog42uKoybOF9nvbAMix84tNvJ0DK0hFktkknhMWpHHyBKtgImW35ppEDeZzssQ8LCGiCa1kcTwVwPkZIqrp1iXHy0M6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=E6eplrdYOyQ3KO6OQMIo8QKRrUEMGHjl1FUafbcxYqCV7EJqqYm-Buyj6PLupVNEXA-dnYMd3aLQ5WjnlKA_L14HEG8gBP6ja1_H8rrld9hPIUYRWX5bxq5mKeDb9fQez0Vnk3E4OqRTk7qu15GBqHI_zr39DD9He69q5wwpXlMo_RS14vRVbGSbwOOcoY5v1deelU7Ab-4C36DAn0lJcfFrxK6v79h20vGU4WezacAoEKt4WGqdBciYteOKMisdT0D-1owRwn0Y76HsXWD3qcG_Vsd4nuw_0RsdTZDgpI5c2zdfOzSSYZ24kf3p8bfFIPozfDxYsUSbrzx-1rqFCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=E6eplrdYOyQ3KO6OQMIo8QKRrUEMGHjl1FUafbcxYqCV7EJqqYm-Buyj6PLupVNEXA-dnYMd3aLQ5WjnlKA_L14HEG8gBP6ja1_H8rrld9hPIUYRWX5bxq5mKeDb9fQez0Vnk3E4OqRTk7qu15GBqHI_zr39DD9He69q5wwpXlMo_RS14vRVbGSbwOOcoY5v1deelU7Ab-4C36DAn0lJcfFrxK6v79h20vGU4WezacAoEKt4WGqdBciYteOKMisdT0D-1owRwn0Y76HsXWD3qcG_Vsd4nuw_0RsdTZDgpI5c2zdfOzSSYZ24kf3p8bfFIPozfDxYsUSbrzx-1rqFCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KriUTYAaQ3ZjrTmYatY4DDBOgKflBret5PUHA3LQjiVtWYedWjZNCybqDU4dxZ_wCGA5eJdj5m-iZI_u3dmLjtLlbmypUteniBlpvqQn0zxuChPV5y2SXxoQgDiBlqGRhRnpdCmXgsbhoK4FbpOlT5Q2CWGKDoys5n5jekKKrTG1O42Frw-ofCTyPR5t1ta0mkqYQEDwKfYe7XqgOriPH0OMboAKfLiKUp8ZAbFT0HAyhqsiHbTXvC-FlcUzJOf83g95mtz4CPzcg8i1sEvyvWGDAudZBbPGKVdk04dkWFPqmh5EQEE4iTVwv5Q3jJzGol-T9HM8DlRtpq4Fgnilaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZRGexGRZdnqSwBI06DFQ1H24NeIdf2MuknPDwX-S09vTVyBtYFN4o9MYD1VwXNQPe5-HLjRREtzcBXqOzl352uXjclJ4K7luojVhaYIe48eEQroon4BppkRgXU1tyWMvyq8gYMtRfTGxzzhRTzpt1QcsuQAZX5-vYRyRPO-EMzTIecdF-wtbpeLvSTfAIwQaRLUtmVayZbiZolGUapdHEOUc1qtFHyQp3d4KuUckx7tLJpKRbpSIrOu4pnShQHyPjwEOIK93AKM_stHSvM3mPwdK-gT0kF1-fJE3QKv3K0vSDdh9cbt8ePqqbVD6HpAQKyHNDW3g1D8JpkPJ7H0z4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOOeImBEfGRZJLCRwMmJ8fN9hpHiGbLMy6bz7Jw-6dZw8JkBJxW5TEuBSDkoTZhNfad56IyTq28qIWqkijfayDAl11xlsSqVS91-7O9iihBZE3mG_CU5z3JmVBmA26ED71T2QByIYipzJoE4vfbbsmcXLDjzCk8-2P09hId48Xj3BaySC1i1v_B4N3lfXsHqUkLD1s_ntNxk30eC-u7AR-twX4zGrN6KRxr-NNPe5ow-UGym7n-Yq9mN_KjYLXZxuWB7FBdAvx0FZuiHxmIDGQyEaSO0v1pbmi7Z7JngAwPDjZ8yxIu4HqKedGnsAZkVInfT6XAAHZNKMgFF4CiE1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFR8LLu1GDi0PEPxzWmLmpztd9JN0Vbqhii0TF-7439QGk7M52M3e4tQvl_3mVwcTgGwUCDkBPLfawCIhBTS1SdM_YBjYBVenwAwUO9Sux6zGs1A2bY5Q1_CMBbpPhKFlbUbS7HHxSapoN5WftA1uOrMMnRUC2FPPvj4bW-yJ3TAc6ctz4eRe5308qBvy4lUC0wP53iW4OAOhysDFJJV0ezzShXmxWCnNs585VjE11Dn6uiL3WCHbao91sA5rmtMv3J1qQl3wm_tMTeoczOn1YqJm-J1KoVr2i2U4lEKN2mw_Ejil3FgALtdJCae7jzVjDPQKb7PoJMjq2OcwbjHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=fLSkicE4Wy8jA7uVQXiJunaNFUxBbQ6mwWmU8ivQMwZVgbcipTQEJp4mlKM8MQ_FwPMftGmgttqpKlz-j9p0ubtv5qzYVCZ-tIzHGafSJ1mEVMuFtGJdrs9JOl7cFBWcDOGgMyYiX4rm5fIZmPUMhlFzjabWV1YAcw3Ofyb1yRgL2hVrTtoNgwqJVWl9ZWEyRzx_cA84LBkkJ0dcVNPm1FWEHbrjAAZgjP3E_JGhUh01holiOOygTIPhdZwOe84ZRv3XFmJOa9x0pLlxiKeBNUKnEB-vfVLKv2xCar-fk9-69fX8SZn-6Sejvp3wykbnUB_MRylN4SxfxYN9B9whOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=fLSkicE4Wy8jA7uVQXiJunaNFUxBbQ6mwWmU8ivQMwZVgbcipTQEJp4mlKM8MQ_FwPMftGmgttqpKlz-j9p0ubtv5qzYVCZ-tIzHGafSJ1mEVMuFtGJdrs9JOl7cFBWcDOGgMyYiX4rm5fIZmPUMhlFzjabWV1YAcw3Ofyb1yRgL2hVrTtoNgwqJVWl9ZWEyRzx_cA84LBkkJ0dcVNPm1FWEHbrjAAZgjP3E_JGhUh01holiOOygTIPhdZwOe84ZRv3XFmJOa9x0pLlxiKeBNUKnEB-vfVLKv2xCar-fk9-69fX8SZn-6Sejvp3wykbnUB_MRylN4SxfxYN9B9whOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
