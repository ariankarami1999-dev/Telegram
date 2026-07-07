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
<img src="https://cdn4.telesco.pe/file/vgx5oraikqM_9-MbJruknH2f-YxSaAUZaL1sKvjkuI64aMtoaGfwEdwARppnsnGlGfPmatTn91jLERqR7hyyuZeMUeLoUCqamu61WqL7UAqr2mF1hmkqyt7DtP4LzSF8Kkt6UASxjdk81UQCgAy4ghMUnf9OTuDvtREU5uEi9SYnT_drcnNTq9PUnFV9TDNiknXFca5-SrRViS1sefJiAt7J2_Gbksrh0J4MDp6VkuetZfpHzFLvhr9nGCegjHhDKurOWYM0tn5UENJ6Fm5AeviuCLDl1ANVwZirGl_al4eg5yRS0MD9xMEFsaJUllTg256rofMwW3OfllSkHdr3Uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZoxNKsDbZjxzKAUi8sNmPus15qFPEvWi1l_nNyA449ajA0ug7oHLmIpX_6tCEc4nw-8-J5cp2Dnp0YZng8TbbxfAyRbVtiKIMeTcPZ4Sq38-LwCLwVDSW77uAKeYk89hnuw2biYFPniATMlzaHVkf-EHmfXaW0eY38HxhBU5qyrxchhGPO0-pflzJCifhsJS5mFEjGQkNOocH2i9kQ7yGGHBnRiP-ii2veyHKujeXvDXADdVPc9XbVRT1ZScGvylCRjrkiaca5fv49ubbOuFmsYCRU_d4mdZoX8pyfN3uWvz_XbzD9MGB3FW5d3UySVuZhE79XWM7pnH_sSVI3TxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APkb9ldN6y7D9Fv_2damawI5304ZzkJPEQ4tNgfSB7DpdNmuAJb0pkQamqALS29lUhsMjbA34osRf3TtARZNxq3yx8dIaLaJtsNOlEfBv6l2C3M4Cf866uHUYBfYNjWz6u_rkYfOUHhqNBAjHbH6ytwdcDzEgI5E57nVn4gqWZ04qfqQHjzPAZm6uUAA2pkgu867dqhdtzQ53vHZ1pIuXRdP-mUYkrYndVTPTqv6GMEnoq1EGO7tnBKPk7nGaX8tNraHzDoWgOBNFXcUOhc7sCheKhPwXVRxVMqgyGRAXC2kl26SKIN7LtIaR0ehfe4OiFI1fsXAUXvpOvRHOzXRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKErFHuEf6H2ApmbURciMzEgDUKLTPin_5-3ReQXcGfT7l4eBq5PvObOPiuTU-q5owDtS0BzyxWSASqeIdZDRiL59IgIvZqX1lpWexsA39K0ffHd7HzZtleoUXXustn28cfGxoCEZ2hnPUr21Jy8hbgBBZtop_KKNs0Zrlt_b5N6izOthglImJVRYM7RIIoPEKoF-YWmP0ndYg4IkJitcM6_qSwErx-WM1cPaXxKj9YZNsmKidgDUwrCh8sMuqOeyJf19n49jHbUI3HqJnlwjc_CLwkRWySIPw1YPWs0uj_xWPRqgFQL-mCSWw_wOX_mA_y1tvOGnozKtILmyPTefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEhkcn7Jhd7iSoUxGBcDanF_G1Td7pgKaC7OhsD4BbD-LQ_2Jae7Vor92qjaZhM-dKmCQDXcCFW5VHMmyzAS4KHy-9hQAxamO7g6kk_uikU0QhLMVBNl9p_ev4UPHul8zSO1X1TCsg9zqRtRrsq3z27RPeQQaImwFTjzxVLRM2hv0mnWJVlvCcaB3PaaEYcpbjYquuESeLv_VE-Mpk28xPWRpQ__5EcohOY-pw5IAygcN1NW9ggP7kP6bENqkD9xWDL_x-0jBs_Uts3lDZcv8b5m57BYKt6a48dKihhJ-UFFxeBPWChZmR-ngaGfsN3dvO9bA7pCmZa56d0g1XuMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDb7J1e17lrbmVAc9Sj3axmZmfJKMQOl7Fk6zadpV01vYhkJUlTaayuIYpPktvBYMZ48ox_lGdE2m1NnhqXa6cZsnEX6ksJLeaB9KDXdRLg_2YMx1G0Sb49ciUeqQfIGUrsoIRwiBPoHbaeQUsZxd8oSTlzbpx0VNR_RWL-2pKNO0ROwdyrzqtqzjXFDhEqWpYLkNptm_2sm1LULa33D-RfD7ReSTumX14wO_nQtXLNp2P85_D8thg_eRKx_RsASDsn9AQSGX2O8KiDWIlE5YLR7G_b79SNVL-6VOmCkqFKnblRblLz5i4x3XSB0-2uQY1yLn2_35PZ2p6U5U1YTPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=rJXQIjeSSBxOoXSSoJIgVsvVgjqXcP0ob1CJpW-IyUBBrZElUAm94EF4n2l-ViziVgbl8OpqSW1Bfg4rbYHG4YeZKbou5pk9FatTGGxPl8SCS1bnqS8sd2umkhPTe_CXxdNzv57f_-NfWI_rc-rCTiNjpLer3KBtsvblLvr_jLSpG47CM5WV16dzMYGQVYVzYlgamp8y9sKQNj9-DG_v07shBFB0Q0Rwq8USu4uQOFDNHqRdsDFJsX_v6jJ7POlN4l8dl0MfK8ZNzxkYqkSLCMjvN1iay0xN_3TNj69Q6VqZ6-o7oOgCkOaAYdlnZF8GZkn9uwlMqcZNeIL2tyNxKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=rJXQIjeSSBxOoXSSoJIgVsvVgjqXcP0ob1CJpW-IyUBBrZElUAm94EF4n2l-ViziVgbl8OpqSW1Bfg4rbYHG4YeZKbou5pk9FatTGGxPl8SCS1bnqS8sd2umkhPTe_CXxdNzv57f_-NfWI_rc-rCTiNjpLer3KBtsvblLvr_jLSpG47CM5WV16dzMYGQVYVzYlgamp8y9sKQNj9-DG_v07shBFB0Q0Rwq8USu4uQOFDNHqRdsDFJsX_v6jJ7POlN4l8dl0MfK8ZNzxkYqkSLCMjvN1iay0xN_3TNj69Q6VqZ6-o7oOgCkOaAYdlnZF8GZkn9uwlMqcZNeIL2tyNxKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=OIWGfNFlH9dAUY4rnUM5dVqT7CsOq1TPfhABNqVF841JN7qng-ny9jjxIjTmXi6j9rqY86mvtoykhfzO2LQfVE-Iun_e-ZJey4J3LDNuogEuP4fYQ5SUhUNbepFX7AUrLUk0eHtJZYbuiIAyxSHI7-i-BdYAToNOzHK1lL00JQkucYSm9Mis7tUpVGk0cVZBSfF9Sxj3eJtXjCSRHDFN8n1PGWoWKSCOtnhlMki7TLzeudIrpmRuYDZwQDgqUXvqkuvcY8vkkWOt0527PU-w2L7gicNkNX3CsrifiyoOOr3xDHdwLpXAk2Rt6FLcmgsvZP7b9k3Xr0Po592DCC-F3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=OIWGfNFlH9dAUY4rnUM5dVqT7CsOq1TPfhABNqVF841JN7qng-ny9jjxIjTmXi6j9rqY86mvtoykhfzO2LQfVE-Iun_e-ZJey4J3LDNuogEuP4fYQ5SUhUNbepFX7AUrLUk0eHtJZYbuiIAyxSHI7-i-BdYAToNOzHK1lL00JQkucYSm9Mis7tUpVGk0cVZBSfF9Sxj3eJtXjCSRHDFN8n1PGWoWKSCOtnhlMki7TLzeudIrpmRuYDZwQDgqUXvqkuvcY8vkkWOt0527PU-w2L7gicNkNX3CsrifiyoOOr3xDHdwLpXAk2Rt6FLcmgsvZP7b9k3Xr0Po592DCC-F3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KurUdiUQFJDGZqJXu1SBJedos0rvnPIFfCvFY1SOvWVZrZdermD7LLdRFYig2qdIbmOzaf8WEOH9f8-xdYscR08qrSIf9lQonRZyCqkQO2X9G3THwY_MpQlSDKUcWA6TvFDasivDstk3POdATCk2AfD9zYxn0R57vogTSMGwMCHN4fV5Ngj9oSHhUTx6TM6EUlCtRM3ggjFxGP9l2-SjQ7Taw0uOyVdL8xCCHc8KApurfKbKNyj7o3IJrSXx-O9ROj5f7T8s_kc5-YLCBp63QCIjZfhgff-m51OL7ZOZOndW0gXsAV1LpH--EAyi3eJ1AtTRgSuEz2GjOf4u9ORHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Zzu4y7QB3enEN-DVaV0NQ_YlTP3X0tkS7oSPBkxCkHAbIPmGcevN8r3CoN1M_0J4tYSA6iNANiGGrCuzxplLRxVFRBCQS8bUG3S0qDGoMSQ30UxGl1MscrfV1FU0ASQRHJzy6w9bz4-yh7XZXH2Xnu64Q7TuBp52T7RoxDjSTYBIoXcir-FvcZT_bHWst5281nIGcqVDJnnBcZF6jBDWscZkPxnMy21WyJB0s0hzRPW1Ax3PV-27IY_rjTP-5rFvO9MpfoHyQY08dCu5TQCVG8UXJXPY8thL9TEE4VT7SrnN8x-BHejSb5pxBrAKUEDYipSsKYjzTFWQlKOxuo9U4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Zzu4y7QB3enEN-DVaV0NQ_YlTP3X0tkS7oSPBkxCkHAbIPmGcevN8r3CoN1M_0J4tYSA6iNANiGGrCuzxplLRxVFRBCQS8bUG3S0qDGoMSQ30UxGl1MscrfV1FU0ASQRHJzy6w9bz4-yh7XZXH2Xnu64Q7TuBp52T7RoxDjSTYBIoXcir-FvcZT_bHWst5281nIGcqVDJnnBcZF6jBDWscZkPxnMy21WyJB0s0hzRPW1Ax3PV-27IY_rjTP-5rFvO9MpfoHyQY08dCu5TQCVG8UXJXPY8thL9TEE4VT7SrnN8x-BHejSb5pxBrAKUEDYipSsKYjzTFWQlKOxuo9U4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2iBDKl-qD_N0WFKAQ_iU6vIq7Pf1w5-xVRkNqESU8Vyc2BRLMfmANjJNXArnN9VOEXnOzpG3t_cpvwt8NzZko76mM7cXBbyFx1Gsk1AGSHgCwOuXlHDrG98RY06DoAbNktWueA5O3QGoOLUJsQa8n3ZF4XYglyjiKIldw25nH77wMtref8ojlWYcm5C1vn4gpDw5HY4xqEzc298trGT-gGMhJo5HTtORDEJNqwvlqztqMyJxBr-rwcP_-GzBTaWp25mu8VmniWUlEvIESR0n_EheGgTuxQY_TDmMI9gVVvKYNuOENbj5ap15_nOX0BqcYolOA043aqZyKNu-Y74JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=eYs5x5BXhvb2rOoTbiqz0exptwqHh05uKm5JmdgblFewI6Tox-bxfGcRYkw4t--nE-aXhvRkQHWHRx9L4ia8YsT4Axz_e0hT8qTO6AtUTgvCRus7UKMZVgAdp7uREBjYqw4lnaTgcSXEKgEr-LBG0bt_Ci6yYp5j-uJUikZKQMe_6l_i6rHLgThgcbCYySL_Wm29i7XDJeHpePbpG5GqQWkAQlfY5SG8tqq79BnTNaUQlBlpmaXWhXWSAOJL1vUGx3ZvWtWw2Qg28mL1H0dd3FMVhkTDkuefxQGfiwGu294jBNjbCwLDb14L8CtBJW31KpuzQjBRllRolVewsxtA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=eYs5x5BXhvb2rOoTbiqz0exptwqHh05uKm5JmdgblFewI6Tox-bxfGcRYkw4t--nE-aXhvRkQHWHRx9L4ia8YsT4Axz_e0hT8qTO6AtUTgvCRus7UKMZVgAdp7uREBjYqw4lnaTgcSXEKgEr-LBG0bt_Ci6yYp5j-uJUikZKQMe_6l_i6rHLgThgcbCYySL_Wm29i7XDJeHpePbpG5GqQWkAQlfY5SG8tqq79BnTNaUQlBlpmaXWhXWSAOJL1vUGx3ZvWtWw2Qg28mL1H0dd3FMVhkTDkuefxQGfiwGu294jBNjbCwLDb14L8CtBJW31KpuzQjBRllRolVewsxtA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=LHH656aXiV45U8Ql5WWK-aazA9WIsJ2i4lf9dgzKlHts7ENCIUrWGk7rBZwN5Eae64iirM2QYDn_wvwF9wTx4RPYqxkdFCzz203-9YuanPyNsluVWTaBkGdGVVocrYadCbEUtdzwNYsGOIFxLqIRPruvUlBJ9ubo6kWfhYyDByDK4nBP8orLbVdbSNCXJ67q0D6HD9ckhwqVUQzfEMUGBGuVz_gfDpMyJeLXIxU2BSdXMgH_1aXtIhvZUKdGStnRK9xT4rDviUlipdQa9PghGp1LqwjGZMUJocDDnwczc7g4FYjb0NEPGoocaOOn5cyBY6VfgI9DEBFII-QCKgzIzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=LHH656aXiV45U8Ql5WWK-aazA9WIsJ2i4lf9dgzKlHts7ENCIUrWGk7rBZwN5Eae64iirM2QYDn_wvwF9wTx4RPYqxkdFCzz203-9YuanPyNsluVWTaBkGdGVVocrYadCbEUtdzwNYsGOIFxLqIRPruvUlBJ9ubo6kWfhYyDByDK4nBP8orLbVdbSNCXJ67q0D6HD9ckhwqVUQzfEMUGBGuVz_gfDpMyJeLXIxU2BSdXMgH_1aXtIhvZUKdGStnRK9xT4rDviUlipdQa9PghGp1LqwjGZMUJocDDnwczc7g4FYjb0NEPGoocaOOn5cyBY6VfgI9DEBFII-QCKgzIzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=TcHfrFlEWNVVotndwa6O8iJUV7lB4fTzTBE5ktZDR4PuTb2LeQyNroOqrkxELvTGGYBQ6ysBZgc6b1SQunPH8gWgDA4l4jqgKnRMPues_pzSq1iz-WhAd0XqFZX3lp8KhH_uJvnVpmk6wV9vcV3FSGv6ou9f-YptRYg5ceT9LSW8Df4-nSKHlBGqvPBMWcYpbbWGCnMigt-5RWmvLrERuEcxGPoMsq8czLVxJtbfwO5KASIESSnfnTwn62Jqxg7QS8ostBEsEOX1IHq4VC-8fAk0wNve_WgTyEmRpzcNRLwMhT0TzU7J3gW63DYs4nnNHtEsa98xqB0Q1y2Q_rd5uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=TcHfrFlEWNVVotndwa6O8iJUV7lB4fTzTBE5ktZDR4PuTb2LeQyNroOqrkxELvTGGYBQ6ysBZgc6b1SQunPH8gWgDA4l4jqgKnRMPues_pzSq1iz-WhAd0XqFZX3lp8KhH_uJvnVpmk6wV9vcV3FSGv6ou9f-YptRYg5ceT9LSW8Df4-nSKHlBGqvPBMWcYpbbWGCnMigt-5RWmvLrERuEcxGPoMsq8czLVxJtbfwO5KASIESSnfnTwn62Jqxg7QS8ostBEsEOX1IHq4VC-8fAk0wNve_WgTyEmRpzcNRLwMhT0TzU7J3gW63DYs4nnNHtEsa98xqB0Q1y2Q_rd5uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=cwrkmiTDo9_4fnAb8cn0AYUhYntzFF06lAe5tQG3uF44kBsg7HKOKDvj5u66v-FoGVNubGHwI2fPmmDP5oREgujdbexlydrvRJISya6dxdFytkQCrsQrZgSoVdFN3n3KmMpZP5btbESjkEszzZMusj9P3YMrb5wqDMb9EzAdd5nXDnMJYZ0jXjVDVaEcj9CsdawhZ6xKbN8ABh9aZUoHSqvdLGYz3WbOuhSulzDcsHII3LtsiEIj88AdAZjkHROu_deUh1ePqcW6cPJ1tROTmueLvYJ-PU-0CkV2WFamSnq5TgF7rEjZ5wtgJHUT27jXgmVU8rtu-9jpdu5nv0cupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=cwrkmiTDo9_4fnAb8cn0AYUhYntzFF06lAe5tQG3uF44kBsg7HKOKDvj5u66v-FoGVNubGHwI2fPmmDP5oREgujdbexlydrvRJISya6dxdFytkQCrsQrZgSoVdFN3n3KmMpZP5btbESjkEszzZMusj9P3YMrb5wqDMb9EzAdd5nXDnMJYZ0jXjVDVaEcj9CsdawhZ6xKbN8ABh9aZUoHSqvdLGYz3WbOuhSulzDcsHII3LtsiEIj88AdAZjkHROu_deUh1ePqcW6cPJ1tROTmueLvYJ-PU-0CkV2WFamSnq5TgF7rEjZ5wtgJHUT27jXgmVU8rtu-9jpdu5nv0cupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=d7DcU-0svSuqsE1QEdd2PzKpswk-4eYMCIyYIRgaHCCYfpuwIhHXrweHARShhzTPkhQAjqbMhGzduftygup9q4bWmP6echaDEh3IK8OAmCet4j6dbfPeJZACjMTdjvZmFKX1IHs4oCfkvoizfsBqISI_jA56QFnqhKbtKWEIGCIBso4O7Vzr0Bu_txYJK5HGfPWlsQwGdAs37PldhYcVTJp-ecx6QMEAla7PfzL-LzFP7083xMvcUNTXs7xYOWC-MX_F5et_4vWBZ5I51hah-Ra3EgyLFF76nSjrHIefoPxligTXPheVVSwTkATvKyULfgyVVeg9fES7_7NOXK4lJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=d7DcU-0svSuqsE1QEdd2PzKpswk-4eYMCIyYIRgaHCCYfpuwIhHXrweHARShhzTPkhQAjqbMhGzduftygup9q4bWmP6echaDEh3IK8OAmCet4j6dbfPeJZACjMTdjvZmFKX1IHs4oCfkvoizfsBqISI_jA56QFnqhKbtKWEIGCIBso4O7Vzr0Bu_txYJK5HGfPWlsQwGdAs37PldhYcVTJp-ecx6QMEAla7PfzL-LzFP7083xMvcUNTXs7xYOWC-MX_F5et_4vWBZ5I51hah-Ra3EgyLFF76nSjrHIefoPxligTXPheVVSwTkATvKyULfgyVVeg9fES7_7NOXK4lJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=k_uzje5LiwMMJiBaXxt7Za9HKR1mrNDKJh1ulngjjVPp4Bnn7YtVdprA-3JhF-eQgapC-KzQezHcbVtiVfJyuvK_FtWnxjhAWxDLZh6Ler-MEVs6lGQE0G-PpjmmGnLfEHr-dUIqpJzbvd77r85AauSXtNo_2Yg1spnMxaF9iuOU2GwJ5_p6gBJRF2eYi9uu_ISob6Ge0lbiaMhaP6vlUH1OnOalJU_0PU6MqLzpFSFCbAkSrT3qx79MUdb3eY-HE8o7sSykYrGKMsrdxFBSYDt59Fp6XFWy4T6nJuZUr_pk8eo7jc5HQVn5IIQj8Z9JwwmFkCmSUy1qjFyXgluFDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=k_uzje5LiwMMJiBaXxt7Za9HKR1mrNDKJh1ulngjjVPp4Bnn7YtVdprA-3JhF-eQgapC-KzQezHcbVtiVfJyuvK_FtWnxjhAWxDLZh6Ler-MEVs6lGQE0G-PpjmmGnLfEHr-dUIqpJzbvd77r85AauSXtNo_2Yg1spnMxaF9iuOU2GwJ5_p6gBJRF2eYi9uu_ISob6Ge0lbiaMhaP6vlUH1OnOalJU_0PU6MqLzpFSFCbAkSrT3qx79MUdb3eY-HE8o7sSykYrGKMsrdxFBSYDt59Fp6XFWy4T6nJuZUr_pk8eo7jc5HQVn5IIQj8Z9JwwmFkCmSUy1qjFyXgluFDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=H_OcXLtrziP8oTW2YsdihHrsPCYi6lQ2zHiKUwcdRAv51M3KybuV_cCzRLdO9WmH56ptzYyacFXPbCoh9N-0NSvDE64gcdDt37v3s4XiCaVT62g6v369yAeAzVWMS23zk9VkdjEwAZXfLWZFiQVp-oZjO7FV4751PalCqWqemeIsAYE8gH8hLla5tzYKny3NIVs8yy8RCRibCrTNDGtc8U3nVQZSbS30SfRUvC5h9z37kcQ35ChTZXDV_TfWHBozKmHiPaSTvfpnUdGpA6ok_aOGXc1wdurINbKRTYImBMk3GTCZN2XVBoxeJehUhpFBSAMCAoblkJCsVULoZQW15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=H_OcXLtrziP8oTW2YsdihHrsPCYi6lQ2zHiKUwcdRAv51M3KybuV_cCzRLdO9WmH56ptzYyacFXPbCoh9N-0NSvDE64gcdDt37v3s4XiCaVT62g6v369yAeAzVWMS23zk9VkdjEwAZXfLWZFiQVp-oZjO7FV4751PalCqWqemeIsAYE8gH8hLla5tzYKny3NIVs8yy8RCRibCrTNDGtc8U3nVQZSbS30SfRUvC5h9z37kcQ35ChTZXDV_TfWHBozKmHiPaSTvfpnUdGpA6ok_aOGXc1wdurINbKRTYImBMk3GTCZN2XVBoxeJehUhpFBSAMCAoblkJCsVULoZQW15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv-bWqQLEMn0zUVhnlRD24CiazSiZ2KtQvVVEw1CyyeW4Jx_XpuWPqmoM5KX3Ek4DkIqqhlESieGDRaOreVPofKXW_YkKCEf8NRzrP2JmkYjuSEWDr0Dj6pg5dsIvazmyrVLhVH2qS9lqvBUfmrgtA_urV2u245tYXZ2FEdYq99Ld-46NljzATlrK2nD4F_MWNkmkJC84R7yT6hcbjgP5rKwvEmQZNy5-a9OwN9QHoi39XFHsVAkmhYzWdpIjOpCjbE2eyPJ0pwiLXXOcnU9RQj_YTVmpGD2Fm3ic_JoJscux_58KMkL4RapAjdpmw7oMO5tVRN03WKI8KBMyOaQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heB88Aq5Rt6yzjbdxZt2C4pHKF0oHLslhznH_iraelKmwRiUuZRRJL7rNyjDuZwqbDhFA1ckFK4oN3iKr85b9xDSeaMQl5dQRRTCIZuwlPAX3H_42VjE6na_7vzKzN0IA_iyiF35pi7t5QX5Gn0vEfgPj94zoS5ULE0fQv3Nj87pPy8XIe1YEtWRcwwlng248WbBzu-vGtSS4NEcVxEDWV4UlSGNvqLT39JLnivIjkOlnG7urt2-R37nW3Wu6piIePu7JVKxnWe-kneBBjJX_5iKLnRFXzwxxa-xovulZmXjXBNqNbFCKzsfFcI_-sdWNT771MVfllUo05Nx4AQf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=ebZp_9k-e7Xu-fQ2GxoqntwuWf95_fSWMK8ga02965-c9bAkJPnTJ6X8grkjfNO5DqVvtuSvaMPzKUGQ0zqBIP2hqQ3KRO8E2pEUt5ZMaSNw_KVUmCjBRYYQODVoHCOwMAde2VyUzOa_8b4bzzV4VlXPPpErT6aOnCn3gSnhHoshnhMwbeoqhWl6Hy1YiDAcxECC3oHWs-M1fhDu35g2jz5in2YHunM92DDd1kzkU3cJOdCi_n9Vx-hXJcofXFMR-I21rTY0odxFc5K6iYpYxg52b8TXqdBytoGNpBQS9U2EoOEVkex78SBeP7-jynrsFTJv-vaSlK8a2PpsrN6iJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=ebZp_9k-e7Xu-fQ2GxoqntwuWf95_fSWMK8ga02965-c9bAkJPnTJ6X8grkjfNO5DqVvtuSvaMPzKUGQ0zqBIP2hqQ3KRO8E2pEUt5ZMaSNw_KVUmCjBRYYQODVoHCOwMAde2VyUzOa_8b4bzzV4VlXPPpErT6aOnCn3gSnhHoshnhMwbeoqhWl6Hy1YiDAcxECC3oHWs-M1fhDu35g2jz5in2YHunM92DDd1kzkU3cJOdCi_n9Vx-hXJcofXFMR-I21rTY0odxFc5K6iYpYxg52b8TXqdBytoGNpBQS9U2EoOEVkex78SBeP7-jynrsFTJv-vaSlK8a2PpsrN6iJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raFeDwLNRmFb2pGHBRXv6-pT5gjJpnsBSXveXDtO-heomek0_32nH1tZw_tia02H8YMjC4vleC93ULRQsFuPcrYvMsxnqQ7I5TaRv4bwt87zIc_VPwWRtnlCCrFuv1UBmrX56QOyorXN1Hc-8SzrgQUexU2Zp01CdNoa-CMecWO_7E5x33m6XfezQOBQj0AA6Fy1VXNZafu_Ttlb7ughZMnG2NYWeKTwVETVtcFlH81KphmCGsqGszEo3HbO-cn090DBquabMMx8m5ik8RyKl-jspdtVDd7-yMZKGScPNwAZ-Sxg7O37woj-p2PKaUCinoiwdofsQs_UQOpaQZW2nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bt8Ig-2uMKs54Y_X483Grv_BJWnzJW7Skq0LRRO77ilijz8mWjk2JmjsEipzugBiYO3lupI1whYTEl9TJLDLxzZWaookvrbgJc-hGmduqZNoSfRIbT4bnUOp0slqhXm59xJCVMo8EHvoaUi-AQYp6ibTF8yzS0qJ4OKBBFhwYJj7o2yuvHFacu1mAa-bOn4qVPqDU7OFsuu1bjySmmdWsnHSztkssaKtyyo-5g9f_pLR241YfbXJ7QXrtrx_h6O7kbsBnFge5PuZD_5jdEzH_0Wrm9tBdf4xnZEkRkoOjmUbH6mAnFhP4MiXKFplW5M6VQsY1YyawlFQXKBjbSKEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=sVyc1tWACY2XGnVYaVm0FJYiiAS6AVaGtc2FKICS3j-jFB-V9fsRYRFFZ5St-Z9o-L9ruKYYsOPaF43uxvExhQQk_5SPkhBwMVz2q-NKF7bMvzmalLweGsPMIHzKSLrQNPE4Y5gZTgHh6is649ZF7Ix_4wDognSj_WKgdX3bkDFk0hMmIu_jwQMRrcD1JDeCbF_6r2Mi1u1XfJ0X1NrG4cYwMXMlz35yMBstc84-aw44w-jq6whI3UCDhZUHiTp8y7ql70-BEiQqKW50RImaH7lkc6kegufCqFXbtwWcfPVSU6TMp2NPiolSSEKVVoBs6PW7ZSHRB0JbOeGkYy-v0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=sVyc1tWACY2XGnVYaVm0FJYiiAS6AVaGtc2FKICS3j-jFB-V9fsRYRFFZ5St-Z9o-L9ruKYYsOPaF43uxvExhQQk_5SPkhBwMVz2q-NKF7bMvzmalLweGsPMIHzKSLrQNPE4Y5gZTgHh6is649ZF7Ix_4wDognSj_WKgdX3bkDFk0hMmIu_jwQMRrcD1JDeCbF_6r2Mi1u1XfJ0X1NrG4cYwMXMlz35yMBstc84-aw44w-jq6whI3UCDhZUHiTp8y7ql70-BEiQqKW50RImaH7lkc6kegufCqFXbtwWcfPVSU6TMp2NPiolSSEKVVoBs6PW7ZSHRB0JbOeGkYy-v0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=AGhmUipY6wXxR38Mw2ZzrPHNp1-o-ikXXZTLn4FbgZk1hB-94kb-KDoKdQEVotxcma_GFbIksIf-67mcxW2LbtOKHR6y1m6OEoAWgNQBm3XkUbfwSBVCIe2DiHUgb4kbrgA-m6ZYOXANLLs4c6G7Z3G5BeOm5JtHY01Hvl1lz1PKQU18MWY_iOFgjPmYF5uYBSyNRrYDGBIr1YVtlhpG3fbYlovQwDwlTiDi6Pa6tpKwwfU6IgFTfKPGTFP8_n6hDh6fjvTwWyg8CRNAXHvBv3Bb4wNmS912IF4Y3nYgDIPOhNuARIDgT4PXgzwwQOuxOl1XqLKkgLZQxW_8WMLdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=AGhmUipY6wXxR38Mw2ZzrPHNp1-o-ikXXZTLn4FbgZk1hB-94kb-KDoKdQEVotxcma_GFbIksIf-67mcxW2LbtOKHR6y1m6OEoAWgNQBm3XkUbfwSBVCIe2DiHUgb4kbrgA-m6ZYOXANLLs4c6G7Z3G5BeOm5JtHY01Hvl1lz1PKQU18MWY_iOFgjPmYF5uYBSyNRrYDGBIr1YVtlhpG3fbYlovQwDwlTiDi6Pa6tpKwwfU6IgFTfKPGTFP8_n6hDh6fjvTwWyg8CRNAXHvBv3Bb4wNmS912IF4Y3nYgDIPOhNuARIDgT4PXgzwwQOuxOl1XqLKkgLZQxW_8WMLdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=iAVKF6HYBQ9gQEuPGjq-Pa1Q3JzTmj4GNzDrUF8hWiMyxo1_Wt9Ju3McoYODbU27_OpGK6zhQh3dKDFto1BETYl8lmHTFmV7dKru98_fFjI_w3mhEAIeDYd13hXFCsDxapQ0G5d7JVio7Vocg-raJ-TOlY9ofXugtEV6HpUTerYpL0ay39rcp3_xNXPzJqGbrdv1OCbBN_1UAQoCWIHNuJcY2mvA3Ggg1A_JgHlNtqQWaKdr_-BlNCka0bNYoWAWeflygagb5e-xXthTc3Bdn2HE0Saq1-R_2-S09d9eGliSM1Lf-wBCFAGlAYJtVabo1I1pTXXuU9N4Y-CBLOC_PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=iAVKF6HYBQ9gQEuPGjq-Pa1Q3JzTmj4GNzDrUF8hWiMyxo1_Wt9Ju3McoYODbU27_OpGK6zhQh3dKDFto1BETYl8lmHTFmV7dKru98_fFjI_w3mhEAIeDYd13hXFCsDxapQ0G5d7JVio7Vocg-raJ-TOlY9ofXugtEV6HpUTerYpL0ay39rcp3_xNXPzJqGbrdv1OCbBN_1UAQoCWIHNuJcY2mvA3Ggg1A_JgHlNtqQWaKdr_-BlNCka0bNYoWAWeflygagb5e-xXthTc3Bdn2HE0Saq1-R_2-S09d9eGliSM1Lf-wBCFAGlAYJtVabo1I1pTXXuU9N4Y-CBLOC_PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9xYE7IoEpFhIxF6igqwfjW4BhTtJ2vOoiIOZigUuG_uwEcjwTjlFIbP4jpQ3zDc5Viz54diuJiC6XBtHG-lPfvwZ7D2XsGCTexofnsc0Y0on-dTVyLZU6lULqckD9ThtjPc_VApyXHqy1--b3W0KoHkFD0V0DExmTuTyoSgnNNs8QjEK3tlA5gXOjMq9tALKJ6DzLKH3lGcTohQ7MPp5-ShyTMru_a2-4w9uL6ouTy-FFDyjVpg-ql400iCB1CAAQFf0dbkz1eU5UQlAkuqR2Gf_C1dR4pttGkDTQYVDrpi1x0Oq2XqmjLUlaI7TkqW_BqhppK4FXs4o5yok2jwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrBLDTNWvHt_YZr8ojErR0t-461G1n0_zgZTyU4ZfoJMLSN-hzX_R51P8WUjjk5e7A5306LYBiWS4TasuFJyyiDXfWH848HLkog-QPqnQQw05VeL47K47ZQx8cmB92xye9h29furdJP8uA7brb1T0XKmhmv-BzCMegydbh0xiFPkFLLQHCTygKYbXbbMUBSbRbeBWgBvt-4LYFFJzaUyKDb8dcMHadQPGx1Jvn3zZCqyA6QPwfXoTDI_8Pff4kiNK45gKQdZ5-XbaQltXrbGiymcgONUkQEhT02qzFKHuW7RDfNdpfAzKbUt8T8-bev8ihI_wQ9vVEqOpZKflftm7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=RaMR9FSt0PvNNXnNX4grO_nJt8JsGsIa2cP9Pp8i_s24TBXhs6yc0bDaoChVxpnJQ--87Kr40qJOInynvXWBAHDxy39m_XWnMPcs7YPiVQDdQcq-Vq7uEcHFf-WShV-WbWz14mACHdhfSTctFAYZpQKVEX8ejPOfp64bG6Dsh199odwBfl0m1hT1I5wPuSWy4Nc-cxiv5D5Rlxzf471mNRKhQieLsE7ybRyGd0VqJwl-_I718t_NKm5Ehc_E5KSVqK1Nsg8HRN0Ejc2hgb3I9BF2jGagYD9vX7FyAoKZjr2IdBjZAHkAWk_NAZjY4vtmtURpubgb1amATqn49JeHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=RaMR9FSt0PvNNXnNX4grO_nJt8JsGsIa2cP9Pp8i_s24TBXhs6yc0bDaoChVxpnJQ--87Kr40qJOInynvXWBAHDxy39m_XWnMPcs7YPiVQDdQcq-Vq7uEcHFf-WShV-WbWz14mACHdhfSTctFAYZpQKVEX8ejPOfp64bG6Dsh199odwBfl0m1hT1I5wPuSWy4Nc-cxiv5D5Rlxzf471mNRKhQieLsE7ybRyGd0VqJwl-_I718t_NKm5Ehc_E5KSVqK1Nsg8HRN0Ejc2hgb3I9BF2jGagYD9vX7FyAoKZjr2IdBjZAHkAWk_NAZjY4vtmtURpubgb1amATqn49JeHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=CaM2tKQV3TbMkAmOz9Ih9lHfULHPemh8kyeDKnv2iRCTr2v93b8Ih_VAo0gFHc5aRKpTZ4YI2iNN-S3ES68s7StutjzNlcZce0vtbhBQ4AaHQsdFOujgzJ_UjMrnQpsuApBOdou0v50TxX24u1HXpytsqboifbBMJLdyLbUBV9p3TrtCSlBxI3mSirZQytNI6mJClMjQOZTBDqXHL1W6RWab8_eLRkKPztxqXAOQUTrM4TrCS91PE3sur5Kd-SeY4N2fGQo2MeRU-8MPHKvzGONmUD5k7iJkNTM7dvYVikmqki0LhxnnuJIr8JLthrSsggtgwtdpzEg2R7IdCIlPPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=CaM2tKQV3TbMkAmOz9Ih9lHfULHPemh8kyeDKnv2iRCTr2v93b8Ih_VAo0gFHc5aRKpTZ4YI2iNN-S3ES68s7StutjzNlcZce0vtbhBQ4AaHQsdFOujgzJ_UjMrnQpsuApBOdou0v50TxX24u1HXpytsqboifbBMJLdyLbUBV9p3TrtCSlBxI3mSirZQytNI6mJClMjQOZTBDqXHL1W6RWab8_eLRkKPztxqXAOQUTrM4TrCS91PE3sur5Kd-SeY4N2fGQo2MeRU-8MPHKvzGONmUD5k7iJkNTM7dvYVikmqki0LhxnnuJIr8JLthrSsggtgwtdpzEg2R7IdCIlPPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxBPLS-N-in5fGn5kgswSun8fSj0eccznl21ovG7s9MSWb6vYRFTp7w1I_GKnB6MIWCU35OcE_w8bzBpLrPKxx9YkSsrxfmW5CA37U1JVP9kDN7eYf36GcrYctMo7wC4T3vcZmwMuiP5qRQQUZhny-28JLl9GEHfn-UIqxSvmHZGfIZVpr9s1mJeok2jccAJFWVNXLraVUS7z_y_LvBbb-FoZV4dkal6OnhzYKw33RBwozHbw2V_RGqT7jvy_LlIagYcD44EYvAYj_rXMGQmENKuL5alVnYmHPQI_pvbottyIa5Rk5_hnaWiKftB5W_wu72w-bkDFafMBKaoddeNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2RvbHwMTpnmxdChNWRbT2UKgHWd6Rgwy7K-H_7Me1yOTE8dQPQhR55FJ9hj7JC6U6D9JY9pRK0N-fIMev0gVh8XIcRlrq5ahNhArAIDs5qBGYIE134SgRUK2TLxNMoLHRG4AAQljcrZvBrsSSsD-YpDcGy3CD9pP1Xycn5JMuZww5P9rjy7XJ43gSDdDeyV8Dpdi4jB8tUUfyuTVfLmUD0PFuP6pBtg68uNzg1k-s_V_Lt_0fctYBs8mzoG7CKKelDD75lGniH5yuVpA9_M0pEHGGkpQS-tRKoiUxynZCcA0i11KlAtVON_uAaK4RRcEKytf9sCxX7bRc3fGtfjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RofDDVAnESCERaSnYI8D1jGHUfyKc7mqVnGgyFggkCAvOqqIcbJ6hfE7X0u_3G6DZ7DhwJYcR3dgItXleFX4t1uYsQXcmlgMG7USkFJkJA_4i7W3slvonc88tw4uUjAS7b3g63rdELFlXtfR6xhlaLerueKaLJboEAMOwXw_B8emDPPM_qv0wslUiltec2W2xqGVV5rt-BtampTBPRJlUMhH3hzaswQjejUzlPDAfio9yebQGuggHnYwhvOM2340oEYSIudzp0SZHNHLVvbyLP-vwFqaweyjSdS8gHykYoHY1ndEXllBVDfAj7pcJH0tNhFCReGIB9PlCjffHGILwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5QnAbGEwEqKFRealCSmaRTADMZXTgRXFSOXR22o196Qnk8oHd0DN66TWootCFeelUe59RCtTA1RmhbFgCbXVen7NflbbfftUKrYzgY-N0uCTPHmN_WjyNHBthy-Zyp9S_Eoyn1hkjTI-kXmY6A0cTiVT3YrIX-jJrZDmy2ifKE4nmcmtXZMpzkPh4YrHN4LFI9Pgbdb-423d5XSW__t5XbYBbJOSfUpL3AI33V-z0uvukLrn7WurSvi_6nRPmlcJysjnWQTJOT7ArbluU0rRGoTCv7RgiujjgPoVcLVwaUQU5T13P25W0UJAuugokdrSJNYpDIWBOKqdkDbm7t3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcXMFec5-gWOQ1mNaDii-yjU5zMfyelqtabycYxogQfESlDztGZAmc_Yu-x4Azm5ERKr04CcBEowIgPuCbqxgyrrTOItZANsESRVbEy0LVOOc6hnnqCyV7_U2PMqe2NelsbpWP2xUDrkY0JjhnWEpQSF0eFqTIOVv23eVXWS7YAOspIebhDcGvzubPQBxqQo7zhc755muz6dhbG59Z9bQ9LRdtOrtjU7P1m-Dqv-E_GcIi4KoH_W8RggBn8qOAh-4tyQnGf-SDaZNVI65LF03r_KuXc9dYQqutGdU1MbGghiECdZzSWWq7kcqAleWshhJ8q35miSG2CMV71dB54EWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPYTlFzsrPWoqnBMIZr9WZDLTmg-3Ut933BqRLmkvKA-tme253TM_KpUTfDscEIuTXR6aLgZrfFv0DvI54DcmLcGOVOsFi_AqMPcO4jomHG6Elsfe1nbatjOSPtdLULOAhh5Iww3PzoU9WT2NthQPV9CrIJaG4RH9noOkPJXCdA-3d-aELeyQmUqxRU5gEe3wttt6y0PLM2ILZ7UpBLK8gWlvKvF9cXjLa90qXSv4lmREZ5HTnPyYjZMJJbPsZ7VF-099NWbBi1Ld6xrTqteWBWayjoTkiW_6wFuqbtolTObLDcCg4xKGVBXezPk62OdHK7Zpa8N1--JkHssVBSenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=Ge5cjTXNVTk1AmLZFy7LcyebqNy0WWocfKjmak92eC7xuJ8aOCDRMDiN1cd7BvGdO4Ebpmk0z9DFFWagryl0G9dMB2NednoqHVxCloj04YmAjzmo9k1KZhaZz9Prr1KQEmOKstP3gVtHMa_raQzC3XcfAPKUFH_4luwYXOZpi3Em7Af8yiJ5bg3V3wHh-9DrgySGLzWS_kBWqLYHNDcxmTug5YiXdELRZjEeoqufkjCWvaGDBNi-xSr8fULchIvtsEgXSdoVQ8eyRzU6_9MiomveatF-G15bQVLoPm_DttCf0TZ76BgXmGMknZV_T2swRgO9UtTpyh0i9QQTT2ySVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=Ge5cjTXNVTk1AmLZFy7LcyebqNy0WWocfKjmak92eC7xuJ8aOCDRMDiN1cd7BvGdO4Ebpmk0z9DFFWagryl0G9dMB2NednoqHVxCloj04YmAjzmo9k1KZhaZz9Prr1KQEmOKstP3gVtHMa_raQzC3XcfAPKUFH_4luwYXOZpi3Em7Af8yiJ5bg3V3wHh-9DrgySGLzWS_kBWqLYHNDcxmTug5YiXdELRZjEeoqufkjCWvaGDBNi-xSr8fULchIvtsEgXSdoVQ8eyRzU6_9MiomveatF-G15bQVLoPm_DttCf0TZ76BgXmGMknZV_T2swRgO9UtTpyh0i9QQTT2ySVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=gyQDEWD1-d9OurySiuJtj3zUHwn3mzoAfWgNOxzGCBT4Ja_scsiRpbjZsETm1iIE5_doct1e9yGa1znORrCDqJWhwSrfJr2fkmM0DyKlpVOXKFaHjsEKFzZBhSUcWOejgjaEZoGf5KQkXygC_D9DFPt8Nt64Uys9tJ7mlG5GwLjmtsv0Atae76NFzQ7cbXGzxI5tQezXqvujhxFVuDjcf604OAu9HQyRuF9RqNAAjpctBeEf900YUa-KHWG2WVpjCBGIZAKFRSGwCLhr7BNiRPWrfrIuSDsZ2gwshvcMSEn3lFqUQtma1kei5ixnW2tv1mCxu0thDrD6a43b0zrXSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=gyQDEWD1-d9OurySiuJtj3zUHwn3mzoAfWgNOxzGCBT4Ja_scsiRpbjZsETm1iIE5_doct1e9yGa1znORrCDqJWhwSrfJr2fkmM0DyKlpVOXKFaHjsEKFzZBhSUcWOejgjaEZoGf5KQkXygC_D9DFPt8Nt64Uys9tJ7mlG5GwLjmtsv0Atae76NFzQ7cbXGzxI5tQezXqvujhxFVuDjcf604OAu9HQyRuF9RqNAAjpctBeEf900YUa-KHWG2WVpjCBGIZAKFRSGwCLhr7BNiRPWrfrIuSDsZ2gwshvcMSEn3lFqUQtma1kei5ixnW2tv1mCxu0thDrD6a43b0zrXSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=XSisYfpNSpct37E3uWWknzVn0HtDTp0F2cDSd64r8xa-H89B02zAFEXI8Qe3sxIqYL5w_6bIQ7wgNQ3_rXRllMsQgnp7QDKXOdX6sRluiwPLWHZWdL8jMhbnTLjDq4OAONTRgRAu7xER2P8Ppx-ATVhTRiyQJzmF_F4Tx8ozbsJQHHzT_A4RixTFlKDznpinViAzBe9Dn0_QihiLNOXE_Zqyj1XmaWn47kA6yCcnWMnyt2M7QJG4gIzwgkwfBMfTbKN6mVV_TE1SAsLZzY6Pw4rgu4v5yxKdebJ_A_mn214N0K3mn1Fw9WoMSfwVt9lE-7Fn11XFLO85siobRIO0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=XSisYfpNSpct37E3uWWknzVn0HtDTp0F2cDSd64r8xa-H89B02zAFEXI8Qe3sxIqYL5w_6bIQ7wgNQ3_rXRllMsQgnp7QDKXOdX6sRluiwPLWHZWdL8jMhbnTLjDq4OAONTRgRAu7xER2P8Ppx-ATVhTRiyQJzmF_F4Tx8ozbsJQHHzT_A4RixTFlKDznpinViAzBe9Dn0_QihiLNOXE_Zqyj1XmaWn47kA6yCcnWMnyt2M7QJG4gIzwgkwfBMfTbKN6mVV_TE1SAsLZzY6Pw4rgu4v5yxKdebJ_A_mn214N0K3mn1Fw9WoMSfwVt9lE-7Fn11XFLO85siobRIO0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=q1He-2uepwrKYZd6o7uKduW4kjpO6LAV2PZYsmS1B9PYdP4DgAseKl5vS8uNfqsle2peskErWSyG-6r4ePORnmB9Af-jRwhFUPkxrKoIm0MddGAV4k5XjSwRwsvubI46TO7RIALb1Xzs63XoWm8KE0Ygg_7U5yzL4tWEns_bO8pRZK3QUI_5PiQYjFHvQWKT_w_jOx2_ihoGiafrXZ5W500KdfeV_8LipJpOMIDbUmMqzEikk-gZb31Db2b5P44Co32qhQm6w7U9fFxY86niT1Lftl2fuJWJwD3aflwQjQI8bc_yFlF99z3UcqkApBG_bFTv6mGMSfmcAxQwG6Zrbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=q1He-2uepwrKYZd6o7uKduW4kjpO6LAV2PZYsmS1B9PYdP4DgAseKl5vS8uNfqsle2peskErWSyG-6r4ePORnmB9Af-jRwhFUPkxrKoIm0MddGAV4k5XjSwRwsvubI46TO7RIALb1Xzs63XoWm8KE0Ygg_7U5yzL4tWEns_bO8pRZK3QUI_5PiQYjFHvQWKT_w_jOx2_ihoGiafrXZ5W500KdfeV_8LipJpOMIDbUmMqzEikk-gZb31Db2b5P44Co32qhQm6w7U9fFxY86niT1Lftl2fuJWJwD3aflwQjQI8bc_yFlF99z3UcqkApBG_bFTv6mGMSfmcAxQwG6Zrbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=vpDycQpArZGJmthjWqqMfSDHsg8U7xrQDXglOhJmzrn_3S3vsxKT7Ms3k3hGg8NfbSo5w8ZR9MzelAFhc0v71yP-QXwXaEuZDQ2Ht4f20H1iRu1HaIvFd-TPLOTs__0R0PnyGvWbkzYbDIdHf-rNhGMEiQiZ0-mqdvMqF0VbhJuMQBOUS2UJoNuQV4COhwqP2YtUJ-28hrmLp9TgcPqHCVcJJ4eod4-QaNMNwtfkjEcIRZ2lUiLgQzE7Myp55EELWgiiAaU7pO-jqMQ3sZCAvXZ3mkH3oM0IXNglWTCvMqn7RmE01g08E6nw2R3CtJck3MI7ZWuhsp3D0ZlCv4kk1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=vpDycQpArZGJmthjWqqMfSDHsg8U7xrQDXglOhJmzrn_3S3vsxKT7Ms3k3hGg8NfbSo5w8ZR9MzelAFhc0v71yP-QXwXaEuZDQ2Ht4f20H1iRu1HaIvFd-TPLOTs__0R0PnyGvWbkzYbDIdHf-rNhGMEiQiZ0-mqdvMqF0VbhJuMQBOUS2UJoNuQV4COhwqP2YtUJ-28hrmLp9TgcPqHCVcJJ4eod4-QaNMNwtfkjEcIRZ2lUiLgQzE7Myp55EELWgiiAaU7pO-jqMQ3sZCAvXZ3mkH3oM0IXNglWTCvMqn7RmE01g08E6nw2R3CtJck3MI7ZWuhsp3D0ZlCv4kk1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=NCEN-FMpFld7WUmhq63y6ba1P4IukDlkeU7yKXew1WwA-7lXI1LpUMFaJuzs5KlVk89DU_1JNlEH8TlAWD56QzDEFwhNlnRpfYgtC91eNVTmdYH5I5fvd5viYHtN-oZVO3HP09GsDpBLJRQJuBvcpocSw0sZhAYpIK7SdmqBXEGOMkdxhLKyT0VM2jMFVW_Xlc6dQx0neH438Dn6DzEq0Qf1GB4fn3DGACsbAXR5f9H0iYu4uZIaCSxEpTWHb6q-1tfTLYMK8tv9TSqWozjIjr6nI4_stULyScywuPu7EdVoseaaM7XS7KBKyX5k_TXvBQ27dIA9Ymr2AZQ4AvHA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=NCEN-FMpFld7WUmhq63y6ba1P4IukDlkeU7yKXew1WwA-7lXI1LpUMFaJuzs5KlVk89DU_1JNlEH8TlAWD56QzDEFwhNlnRpfYgtC91eNVTmdYH5I5fvd5viYHtN-oZVO3HP09GsDpBLJRQJuBvcpocSw0sZhAYpIK7SdmqBXEGOMkdxhLKyT0VM2jMFVW_Xlc6dQx0neH438Dn6DzEq0Qf1GB4fn3DGACsbAXR5f9H0iYu4uZIaCSxEpTWHb6q-1tfTLYMK8tv9TSqWozjIjr6nI4_stULyScywuPu7EdVoseaaM7XS7KBKyX5k_TXvBQ27dIA9Ymr2AZQ4AvHA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKk2qasDu99x-clYUiaCccFIhwB2eQVNBgDdd49O6Ujgk_gHIu48JmiQktsc8CscptIFX07xSD1WYOXOSS1I7L7FXWhHWWwFgpcZo9GpTD9cEvmF7pGzOh51OUguML-iVOfRDg57a_bclDTyd1jJX4McfwKITcZtEW5JpjXdEdvVpKcuq9rcPoZsCOXr_KCBg4enK4twJEFgtvDJlNgQijB7eeOLgZosOlCpKU8dEF39EbHZ_CHZY6SprWzz0FmJAmdzJt3YZ86wr8lLZmWkEfJ-CoucgZDoISvtdIhquEaNc01zHvto6POC_jln8Hu3UwnGWwRJDn54PsHtyCIdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=AdeaoFE7r0EzS0bSoWLRie3huPEDk-Axw6hMZc5Hv3XVi7s9kJUVmim6OlGxLw0DCrUmnQESaMT9XeP97XtwxbD5afNfN0mz3KmfaqaIyPKje_3Zbcb2zxIZOpGy1Xr2wc1fMGAS2ovQIfpPsgBZiUVGqmgtCx7Ze9IOovvQiD2YnIB7qq0RTfVU1UY_RvuF1Ke12tWc2fdFLikwg83xrJu_R4U5sd7XqZTrjc5_IkADRf2vpaqidKbGlAh3x_9EhcFmegUg2MIZAY8FhWS3MDI1aNsp-l9W1GhpSPx0cNuQWPd_PIM6vKt89KBnh43Bh35isCBR9ayURGY4aXi4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=AdeaoFE7r0EzS0bSoWLRie3huPEDk-Axw6hMZc5Hv3XVi7s9kJUVmim6OlGxLw0DCrUmnQESaMT9XeP97XtwxbD5afNfN0mz3KmfaqaIyPKje_3Zbcb2zxIZOpGy1Xr2wc1fMGAS2ovQIfpPsgBZiUVGqmgtCx7Ze9IOovvQiD2YnIB7qq0RTfVU1UY_RvuF1Ke12tWc2fdFLikwg83xrJu_R4U5sd7XqZTrjc5_IkADRf2vpaqidKbGlAh3x_9EhcFmegUg2MIZAY8FhWS3MDI1aNsp-l9W1GhpSPx0cNuQWPd_PIM6vKt89KBnh43Bh35isCBR9ayURGY4aXi4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=WQQB1MKyyoMBFkKv_JLPPC5jP09PHVqq-ygp6FTcwMgITQcw8jU-No42fZqtY7T-pwDEatfCHfeapyMfxAqcqog8NrLmrf5nJruHM5_-J0peQcGwY3_3goYqiP_nBwMsrSfPLaIPojOQrpdxYqMZ8523_cxJbQ7lJtN8lwjIDEgT0DL1cdDlc2M__BlIw6sXaf-_u51bsXhH6qpmbXYppw2xWNoH9yj8ApuwalJmZYlCv4UwA36fLEU2YREvyJo0oEqy0e05JRbvAQ5CMCply_mJHHpuiHzJMp2KTCyT-RrbX8ihJHmeFSdjpfcifHfMdRvQUF9YnAfl9k9nLIfRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=WQQB1MKyyoMBFkKv_JLPPC5jP09PHVqq-ygp6FTcwMgITQcw8jU-No42fZqtY7T-pwDEatfCHfeapyMfxAqcqog8NrLmrf5nJruHM5_-J0peQcGwY3_3goYqiP_nBwMsrSfPLaIPojOQrpdxYqMZ8523_cxJbQ7lJtN8lwjIDEgT0DL1cdDlc2M__BlIw6sXaf-_u51bsXhH6qpmbXYppw2xWNoH9yj8ApuwalJmZYlCv4UwA36fLEU2YREvyJo0oEqy0e05JRbvAQ5CMCply_mJHHpuiHzJMp2KTCyT-RrbX8ihJHmeFSdjpfcifHfMdRvQUF9YnAfl9k9nLIfRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwhhD6yJemc-oMYFZoJs_tzigUn327pFNAG-gzgigPyzz5SdcElj-ji5T0iHZMUmBT0_WKeg6_4NG4uT_yaEMN90PjtDtwrE5lewoH_dIH2_jPdYg-0reiKamsN1UAsMXKtC0U0ZBnK-6A2H7Pjh9kJtGVdFQ-oARnMjA86eTlGsdDdpyU92KezDHUlSNwrxPhzKGOfuKJl5VGX1O-s5uNRma9mdPtM4_3hCByRhIfnl2aYHx7uO1IXjXDimpfHGUX0AD7sGQfZ5zgjmGconT0F-iSzbsdm3y9h1CgV4D_H8V9RgjPCY5CLfKg7dTpoixgHEGmOoChKn0AqX4fPnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZUZMzFhUuQaBg5W0y6N2Ft10j-1HDhhSljT52yCxixXv0STv_WQPg3VNylUudtWodxLBXvwnagIBMso8Enj49mD1zSSHbMyZh3MYTHiDycR1JnMLJgar5Am1C56tXb1382vpvxUH2n23AFM0DikIJO4UPED1XkQimCGzqxTAlw-3heJH8a4kqAGH8t6FmhRnYKxStgoK0SzIKoXYcEyd3BgaEsEVWMbK6KtoNmcXKVBqn43vL4JowBYupDr_8s64sf9SIoU5EBDUMcteAzqq6fvMCaeutL7r5uDpxco5gTVzyA3Xw99m6giqelxNRDEC6VN69UdJfcUdjJw-d3pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLfQsLOdf2Ww86CNkk0L5IWZGfCvYyoeUp-9d96SXimdaWiA6mLn1TVjDxEq111fmTXWHLTaVmvNdSGMFpAlaGGJbITBkn8kXtt3JeTPh9gpZanOXakKLfUnMiiMWFe424lT3azCfVKZc2FEEUZAsTY3Rpgd-y7fIxDkwC5s_ux6hzyPhw3J5eYZuKro_zs-iwuB09bIewLI4d0QLMSQG25TOjqP6ZYNdYpWRcLf3RWS9T3VOUEJTrfyWHAOipc_j2tvKT5cQN9hYCOhHmPK9Ncp9sdrV_d355mdw7EhcEHgRTXXYhqLiIEc8FuiI-qcYpaaDSFbG2qiI61FLz5saQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxDrET735AQ00BHzD1OVGxQuzTG-un3sAImkj3EBfMuCOLkORGGyzyrkknSgrzOwdZbjXlY_6x2a_NUkVe7rYiWYcPfy5vDclBXJ7jc3XNdfWEQdp8EYNM9uoC0n3e7RFXG9SKZtHOwcNhRB7umIDAcUUHbaaBzpJXWPBsApJz7xnpfB5N4mP6xUHM8pE4BYZ6063conrH1OAemme7hsmmR0jLznqZzIaLDP3ApyGVJzB559S_iNSE7CoOQgFHFZDDp9PJcAMGfD4nCRn9f0hSE5SyjXDZzGbniRgn765KMtXdqGjtp1Un9KrrFGiNt5z-jCHWhYDUtx52bVgPE-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtHPWTC1lG3iGnTd8myBHM6ab1S-vNvp-scXTpduHp-BNLtaVBUGZcuhf6Nzk4T0dSXnLoDmFRVGWIAOQtqFdgbIov3VmmI7kaBfQJ5JPopj-pVFb_UipI65KjhuWX5f3STXrh3jAD3T-UZ200TtRVrDM_UvuZg1n61Is0AbMwFQzC3Oo9Oo_I4Ye3RVT6r6kMb0VaAsMJuWLoOVkE3JbUR8e3u84pqV6TpFmDPF9sq9uV0U-hNAUWzlr0dVmixQBtgqd2N3Xm-kE1R9k5I9IyNQjS6sWc0xswoNiWgvN04sOX0Soae4LMFuvrbp2x6HDl2oGw2f33ZZVSlE_0r-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGWGcf3NdfCpT1Ivc7qbXRu5EVJ-3vT1VvAnYxpOeE0EN-LlWPeEy2weX4w44T6mo6mtF4tCRyd1rIbROI6jWjqph6-jwPusTJ9_NEYIq0zBKVckVfp7Sz8da8F_sCL-vbmnXy6IfWTor77LDq0j0oLmS8erl5VqnYbObTzi5ICaFv-ydrBIHBsE0McBMPUOATsooUj2_6wRh1BRt6CW3cgGDnFt-oeXHJ_7ZReG9Sw6H1kc1eph0ZiG_SOh7zRH4LBsboIE4Df-jzcSBhTVIlAWQT9CKGQ9pJ4h7hXfaQxDnTBR5ccps83udfjDvt1C6u92riN2xlbffxMnawnabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyF2iHesCq6kuExu1EZ3ailLtPI6URMvXr8y-GPoqrdZHTrVuDA19vTY9MEUyGeyaoR7MwZ3hvYxkWPj39C_1rNlVv59cj_MpHBbeAwhnaA5cvdhnx8OaV7YHDW0wRBaqd-ybyGsMPBmkMNHzi7kZipS2oDevDL43yJxB5FcdV-Ofv3MuGeZMKzWCwfdgBot5feYglk1QSXMQMfOrjmLR_MLtkZwXr8KseNDEsysHZbP0aEkmjmJxJCEPyQu3qXfG4P7OP4EXcOVgqSDjKCiQY-YtF28ayG5iiaGRd58cuKG0I4bRRreXgtFTeL2Q8HiIYYAJcBsArXHJ_xgQII5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTRsbwL7-iFx3WMSwxyLBde8WwcyJqOHPPNWzxjkycJJxDNfBBgECex1ij-VC1H0l23NP7OA3slH4UcmiSsGCJG5e6D9riBReJH1f1OO-_pFy-O1PBgW7PaGEpoc8qvP8NEErMRllP-k9bqDFbPVL21XV615fjKHlw4yNxTwTuyXhqDVEbXI8_9vuqPDQDEWMts28eNv70Z0GmXmoDtm7rfg85l46Lp9gQDXGG4ppffoJIp2frF1QT0aRTXLFXPuoewDvhd2CokZ9xQrV9Ayy5VrN0WFDjrLtgnrrm7AtpxM5VnqZiFewlXcmKnk_5aXXxhWoXr4sYEvyf-0mqC3sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAgD7Tu9dkBGONakGCD3aUnS-Z1Q5AiuWQWih9Qx21ukw2vGj3k_lDYl_uUpdg29meV0HijAxQSfhsY9yOEhzLceoPHNI88hFKu24x8M8wYz7LxeXk9LbNyzBF_lXWCIX97NX8yWzi2FW12zDpRGB4mF-A8obpiiK4lFEKcdJ6SLx3WInLdU7G23TjWZrU_8_TO1WvkKEeJDQFaqkwsSsbZpQVJ-a9V8OI9Bwcqzm4xV6Y9oBCyVgtE4z7QWYFvS_AdzusCIOq_zTMJfVWSsGWfK_Rn1tHpyI6HG95oFgnqqc3LUmgOVGqDOncUs6iwnSObTtsT7T_iwActeALUmPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl3yTvvXxFARZhg_WE41nSVeTSIWE2O77QynHjCn36Mfop09IBSMQO0RNDqlP37uWllKd85ajweJ0ko-lgvub_KG897ekIZC5pPB2s7rjbZFzJaZJ-mkw54FTK3iEZXbtJqZV8JThwx_470yrAtQdeCqfGFbFvWKaz_x1QYsmhIuQ6gAMk-glM7iqJBtnVe0hkyfIOUJGCEK6aI-oInVNMfp85QGl0lUfnnIRRwg1fhILdnLlaQTQ2yAmr7r52p282MahEAFt2c0XLPkum9G67vZ7YC19zPqgsdSNrsnh1zKHxMpgZF4RlZ4RHAGCu94kNjd224CCtUtMalIzpVo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqSwzlCAVlJASMlojWZNHQCJo3PbV9GYyGS9L30ERCLMKhcra4gUtG3LOnR-SrOt3sBa0SDZm9kia7tZ1SDA0CkrUtSa-bECsCCJkakF8zKqmF8ladLVTJKAxAfW1tf3SPnB6YWF0Qazwxh6rEyHjy_ondFcZqcONJeXAOUqK-0Gst3eoMHL80zJn08WcJ8PR9oClTsuepKpY4U_CQq3H0G0YGhFAHxPenHDfs8iC2U5bSuusDTjqeXrtSKdNM4edqzzvKX6YOb_w4NW24SxtSe2ieNIYTzoFU1beaekL5IeIudPXOjQ9BGBl2a1tDKEOm8KAbfo4_JWSN5WFmG-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2xZDMPdFF6wqvnU8D3-4N_3co-5lUGjY6H-mPFMcFajlsKd4-3OIxkgUX4etgNcS8C-kwE1n1mdQoqoO_4lCplDDcxGiKMm577XG9YvqU6Aa20LFo8jYg_xnrnWPOFz2cNVpMrQQzxkozjNbM0VD6aX6A07qV0VHFWSrYPi2cI0zHVqj-mDvQ4IB1bq2ShZ0qlxprfU10GM56wPhIu_WmJ18_FvwWDBBZz9VhCSSDuU8YKjy0jWa6rDTY3fEFVxfMB9467F3sk3_b6CTak2fCfgYD-361pM43XZCbGbCy-fbROgLIj5Kj2s8wb13_q-L-rKBpbrVkU4Q_TWWYQ7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=FzQUkFHv-aYQwM63fpbLgVpUREHoJsC4HODnd_Jc3B_agIrKGdLwzMumTO-aKCIZijERmz8PxIbq-ajrvtzb1RoLZlp_DDnRDk2SiMvqVP1zYcA5D5DFeA-ckFlyHgdkzUhds-cFevPahwoewLtGx-Kjo4Ez2_bFNyvNHAvzaGgLH2yPQakq5u_hD1auWTq5n-CP99VGI9qy1LR6Wjt8GrlHSMCQYUj5aq3H-4qvRqIO1jmwy6h1vt9zBajIR-C9P9pN_jrvcLDlwbEHfiDElNE1UEavlua6UajcHMpY7TDmnFfo0ksF1klFqCmT-DInAQyqaVwJaQ94PzRuQOwNMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=FzQUkFHv-aYQwM63fpbLgVpUREHoJsC4HODnd_Jc3B_agIrKGdLwzMumTO-aKCIZijERmz8PxIbq-ajrvtzb1RoLZlp_DDnRDk2SiMvqVP1zYcA5D5DFeA-ckFlyHgdkzUhds-cFevPahwoewLtGx-Kjo4Ez2_bFNyvNHAvzaGgLH2yPQakq5u_hD1auWTq5n-CP99VGI9qy1LR6Wjt8GrlHSMCQYUj5aq3H-4qvRqIO1jmwy6h1vt9zBajIR-C9P9pN_jrvcLDlwbEHfiDElNE1UEavlua6UajcHMpY7TDmnFfo0ksF1klFqCmT-DInAQyqaVwJaQ94PzRuQOwNMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Gm-l6BQzRHA5mm4DHBCsIOPhvymS80fyyME7AV5Y9jHJnRb3btqKezjaJjOHVzxOUuRgp1mbapR7vBvYbBRspNYHinlc6Hycu2eaXlVAadhBxUlCfwgaZoBM8xdqaeNwLrI0sBr3fuOvGPw4dOYWOr1o0NXbcTVptl3gbY2_5kbsJ6aF_k0W-z9VhHDORl4jm6KEYfqalNjpOp8ofPHLgjEDPcvtLgy5oMkTh3xpVudokB1Dfr-lxfs1ZbqKZjOhAiui0oiZCNl3b39wgLzSnBxQ4BOt70Ihhn99fH5pZv62NfBAbKIBJ50Q5-gRo8X9m_kvwPxBNWZsXVdVAG2Fvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Gm-l6BQzRHA5mm4DHBCsIOPhvymS80fyyME7AV5Y9jHJnRb3btqKezjaJjOHVzxOUuRgp1mbapR7vBvYbBRspNYHinlc6Hycu2eaXlVAadhBxUlCfwgaZoBM8xdqaeNwLrI0sBr3fuOvGPw4dOYWOr1o0NXbcTVptl3gbY2_5kbsJ6aF_k0W-z9VhHDORl4jm6KEYfqalNjpOp8ofPHLgjEDPcvtLgy5oMkTh3xpVudokB1Dfr-lxfs1ZbqKZjOhAiui0oiZCNl3b39wgLzSnBxQ4BOt70Ihhn99fH5pZv62NfBAbKIBJ50Q5-gRo8X9m_kvwPxBNWZsXVdVAG2Fvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=C1JmpiXd-YEZZRaG-cCD3gDmcUhdbf9DKvSYz1qTv9owmaulCmVVBkywNaPWzSA9K4kETdop2uKM29zBkF2z8-7soOtCZXqlEVvpNiX8HcC_DTItDgtdZhOQW0eBZILE4VKxZZF2Z2lc7hneai4HmfEXguBn6mqJWjd5byVuBQrhABHGNgI2UneyQv9LaaUtV52G4FECl6FG47fSG2wXVC47BSXiPfOrfN_9KpKQRMyT76ypqMCXfhjSC-Achacqq2gGzFLvE7UlDQxE4EX32EqHQjYD-mD_SoMmDxMCO3Za9-hMgNCvm4mrKl_7fm4b3Q3rSHE1FlE7IBEXqViaXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=C1JmpiXd-YEZZRaG-cCD3gDmcUhdbf9DKvSYz1qTv9owmaulCmVVBkywNaPWzSA9K4kETdop2uKM29zBkF2z8-7soOtCZXqlEVvpNiX8HcC_DTItDgtdZhOQW0eBZILE4VKxZZF2Z2lc7hneai4HmfEXguBn6mqJWjd5byVuBQrhABHGNgI2UneyQv9LaaUtV52G4FECl6FG47fSG2wXVC47BSXiPfOrfN_9KpKQRMyT76ypqMCXfhjSC-Achacqq2gGzFLvE7UlDQxE4EX32EqHQjYD-mD_SoMmDxMCO3Za9-hMgNCvm4mrKl_7fm4b3Q3rSHE1FlE7IBEXqViaXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=WrWy10JXI0Q81ejf8GvKIh5dXm2BoPpkZ7vJsCF8O9XlfAPGLoEx3qoAEyIhzJjSQyXs4UsBiv9Vxy0I6ECzG8vDuH0uXk2MK9IkwcwjmBwvcW8mgrB1LVb3YCdSAvwurJgSXODnQ316b6RMzvKERnY2sFBdPPV_FTCzYr6FDReXeWzcpy7gV3m1H1aDaQ97JKFx8MG7EBEZ1qg_NJZ5zL0HLo_mY4pZDWaskGOH9Yz-6Lytd27vNW55W8gXwmDntuoLLmwu0W1hPl7CVTF5BhvPMNwXd27f8UwZkJhEC_EsONVCgBvhh0yZ-0xprlNMlsFuA72LWuM6RIBMIiVKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=WrWy10JXI0Q81ejf8GvKIh5dXm2BoPpkZ7vJsCF8O9XlfAPGLoEx3qoAEyIhzJjSQyXs4UsBiv9Vxy0I6ECzG8vDuH0uXk2MK9IkwcwjmBwvcW8mgrB1LVb3YCdSAvwurJgSXODnQ316b6RMzvKERnY2sFBdPPV_FTCzYr6FDReXeWzcpy7gV3m1H1aDaQ97JKFx8MG7EBEZ1qg_NJZ5zL0HLo_mY4pZDWaskGOH9Yz-6Lytd27vNW55W8gXwmDntuoLLmwu0W1hPl7CVTF5BhvPMNwXd27f8UwZkJhEC_EsONVCgBvhh0yZ-0xprlNMlsFuA72LWuM6RIBMIiVKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FYsiAbDrx6agsaW6akNwm7oGlbozPRlDQ8fht9UVMx0QyFh2KvMw2bDg4MyCRWtub137yGP2Sv_bk5UqQtMXTICyaRc3ScsEnqbNFJzC226SlXAOk7EYrT-DDwl6x15Hr0R2XhZFzq-2hEcrPrmP8jT_wIcArlVzFjoh2UC4TszRIm1lAUw2sZMGf5csOOeavipmVcu4Aj98o95lzlulCo3_mRMyP67ydMP2cONs64uNN7ujfD5M_ARdNEGLqZQhIdjErx3Rp5tbOV4gaNffS30pICUpwMLvXjE2_xjux-SzAch1bLG9ejh67rtcybgUEehPEReaafxLDj2RCYALKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=FYsiAbDrx6agsaW6akNwm7oGlbozPRlDQ8fht9UVMx0QyFh2KvMw2bDg4MyCRWtub137yGP2Sv_bk5UqQtMXTICyaRc3ScsEnqbNFJzC226SlXAOk7EYrT-DDwl6x15Hr0R2XhZFzq-2hEcrPrmP8jT_wIcArlVzFjoh2UC4TszRIm1lAUw2sZMGf5csOOeavipmVcu4Aj98o95lzlulCo3_mRMyP67ydMP2cONs64uNN7ujfD5M_ARdNEGLqZQhIdjErx3Rp5tbOV4gaNffS30pICUpwMLvXjE2_xjux-SzAch1bLG9ejh67rtcybgUEehPEReaafxLDj2RCYALKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=RrqF7yLmb5m7hMBZn4kG1lZrJCmInJTL57vAwOJ2IiiA1PWWQrhCXb5b1XkE6MTHlLtWPsC1kmDqBusPSSUSQsgnqlc2aqVOWiU06Wtj2tCojJaDcCdJOggpx0on0g5gtzhdYZ784FjyxOh0LGmxgu9AHsxn8bK0DQwPCM-KEcO63Zpywio8TjWLwAHsDExDv-Sz2eZ0rurWTKIx1Ly6kj1n2ZI8PKHfc9hHc6maNbfUICrMbevdh4mdzshframvdY3uSXlgA-XfaFuaQhWhlSd78S7GAt1Jd-HZxVZGraNwIuf9OlMFfCiQHyt9h-YSG1oocYR09wsROp7tcfgBOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=RrqF7yLmb5m7hMBZn4kG1lZrJCmInJTL57vAwOJ2IiiA1PWWQrhCXb5b1XkE6MTHlLtWPsC1kmDqBusPSSUSQsgnqlc2aqVOWiU06Wtj2tCojJaDcCdJOggpx0on0g5gtzhdYZ784FjyxOh0LGmxgu9AHsxn8bK0DQwPCM-KEcO63Zpywio8TjWLwAHsDExDv-Sz2eZ0rurWTKIx1Ly6kj1n2ZI8PKHfc9hHc6maNbfUICrMbevdh4mdzshframvdY3uSXlgA-XfaFuaQhWhlSd78S7GAt1Jd-HZxVZGraNwIuf9OlMFfCiQHyt9h-YSG1oocYR09wsROp7tcfgBOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=fg76TYucVVYSf1nb4dj26lpHe7LSmGqwUpmkF9LrTt2pRmHSY1a5Rkyd0ALO7cWFLbdkmhHAJLXuWVBSCj6eYIoedFpabDaFc3QsNXlDjECfEvFrri-r3VEDmqPNSqI6YQBi1BQhJrMvtyg4fkE94IqhKt9aCe0kWbMd0WgnzWrCedOBi3K-tlJr67QHhYpOLirVhpGxhILx9k7n3XuXnHTi2tqFrWQ2xJPjz7hrJ3ME38pEc81PA3JbZhqRgnV0BTspSmQFHMNhBh6Gxhaypyp1VzbR6lvVucj1-D5bz9ZjHWT1_RiWOYzSgmtfxvgJ5Wi2IhWsx0fkqaOCL_DbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=fg76TYucVVYSf1nb4dj26lpHe7LSmGqwUpmkF9LrTt2pRmHSY1a5Rkyd0ALO7cWFLbdkmhHAJLXuWVBSCj6eYIoedFpabDaFc3QsNXlDjECfEvFrri-r3VEDmqPNSqI6YQBi1BQhJrMvtyg4fkE94IqhKt9aCe0kWbMd0WgnzWrCedOBi3K-tlJr67QHhYpOLirVhpGxhILx9k7n3XuXnHTi2tqFrWQ2xJPjz7hrJ3ME38pEc81PA3JbZhqRgnV0BTspSmQFHMNhBh6Gxhaypyp1VzbR6lvVucj1-D5bz9ZjHWT1_RiWOYzSgmtfxvgJ5Wi2IhWsx0fkqaOCL_DbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8wZVeS4xpUtSY7FJve0j6oz3jI2xl4p1vl39LbzmbjzyfPHYLhpKGHMbT4l_puS1xUUh8VOPgXX_AHsxx8ihnRNCJ8sRlW098pJ5tL05X7CyR5bql5_SEtkAjhWIU6wsoK2-mzXo2_L2fCin_7TCqE2_ArNsn-bkIsn7cdGVzmJBv0ajfaBSNH8cK3TWjrIo-r0SpsXJYIXr3t_Gp2DN7rcvwPtcKO2y6dXHE1-j2NbMGDQRR3xFMr_5prNlx-P-41S5oZeDU-_OrlrUqGJhg6-MDkVHtRVQRKHjNP4XRnXu-uc4-ArUzO5MBuILZK0AvIM1TfeqSoF_rMeIO1tHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=RKOz36NYr-tXVfn1TbHHfe_l5Q1qBF5cxVUbmRr5h-CIO4dciDG0VT9fB_7kI1VQfq77_hFeJ47A9PI3fbka0Av3RyDhwWGRX302I0Obmz5G5tGxSIgrIFbrJXDKDaZnxEoX8OrywBH-MFb9aUY2bV9SXD_av7Cjq5f5kaOq3S3apXUt1uI-gGmaO_BYvm0ZRY5PGhO4n-J8Rk8Ar1RxUWVYyw_9cNYD_xjdx7Z6zG0iCt15ENyE6vB-yvpvcfoQhOXiEmCpDENG9ZNpZEuiATQnmhL7rCaAeJZqIu592pgnMHVbdmIqP_peNe8XGjCUSeMiZ4lphI0z6-VPKgWHtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=RKOz36NYr-tXVfn1TbHHfe_l5Q1qBF5cxVUbmRr5h-CIO4dciDG0VT9fB_7kI1VQfq77_hFeJ47A9PI3fbka0Av3RyDhwWGRX302I0Obmz5G5tGxSIgrIFbrJXDKDaZnxEoX8OrywBH-MFb9aUY2bV9SXD_av7Cjq5f5kaOq3S3apXUt1uI-gGmaO_BYvm0ZRY5PGhO4n-J8Rk8Ar1RxUWVYyw_9cNYD_xjdx7Z6zG0iCt15ENyE6vB-yvpvcfoQhOXiEmCpDENG9ZNpZEuiATQnmhL7rCaAeJZqIu592pgnMHVbdmIqP_peNe8XGjCUSeMiZ4lphI0z6-VPKgWHtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=VQ1A5BfZ9QW2mrFQCdFAVeVf93u0auQnpg2TnAlDQEik56R3J4QpyH7_qHqZratotCmNxcMjw8ne6jZ9CLgw_wYLyCX-lyOuSlH9tsAxX0LSSPuvSMoofobVcVgXwPKL9j8lsJKwqgdr1502XnDAKDKwJH1H-cwsZYFMF2hSXku1xXv_jzW8jHBEBzTGBB6nZZR0T4p27gf0J_A1dFGntzFXASjAd_8CLwhqGdx7qDvyfZiQOIMITWXjEpYwfhomOncSiOMRVuYIj8D2pMQ1N9zNzTA-sa2XZxh2hwjz3ksGec1wRYEKIRnCziE_ijwmSvwcw80DzBpfuxsUODXkFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=VQ1A5BfZ9QW2mrFQCdFAVeVf93u0auQnpg2TnAlDQEik56R3J4QpyH7_qHqZratotCmNxcMjw8ne6jZ9CLgw_wYLyCX-lyOuSlH9tsAxX0LSSPuvSMoofobVcVgXwPKL9j8lsJKwqgdr1502XnDAKDKwJH1H-cwsZYFMF2hSXku1xXv_jzW8jHBEBzTGBB6nZZR0T4p27gf0J_A1dFGntzFXASjAd_8CLwhqGdx7qDvyfZiQOIMITWXjEpYwfhomOncSiOMRVuYIj8D2pMQ1N9zNzTA-sa2XZxh2hwjz3ksGec1wRYEKIRnCziE_ijwmSvwcw80DzBpfuxsUODXkFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Oo8lL7ZwDodrWrNyDjsonPq8-7q5OsylIT_3JuFoy4HYlAgAmViwR2cPobuj8rbtYjoZbcgaXGfpx7Wvy-8Tnyw1eTNpmWDeLw7kjkJByqvHf50oCjYbfKXRsy6r-AQZBvTfvyj2UCgDJlFGu4n1_ijM8C7zqrQjt0o6RdDIrTDXLABpV8Gv0kqG8ozT4UT-Vc4aOq02ofdDEIoQiKb0lg417iHqeGgutSFFjH6rxW5mgpm6Gr8Abuc8C2tVSJBKMqWOTXDxKx5FX0la2h-MmCkZA7_IJ6U4NQiAXSaFvrON4Lyat52g3_QtixcLvrri1TIHv9u4PgWC8BEByodPfbNzaO3JGTZ42HiaxaVQ249uRjhML9N_Al1EdChdIc52E8JIsB_J-M4bm_vLASWNMStLMyuq0ROZNY7q4rb3mCi_3QdI0imKyEQrlNXqX0x3UgY732sn4HKlottxjbEiHmhKfCpC-BJ9LilGJ-N-zrMsYEal_Zz4ekzjimXc1kWVDPEPs4A9HHgwiPM71e_VEPO2ElLpmriqBny56qn2gWoLdBUHcTiZ6_4Cre9Uo4c6SCJ4Pc3zgG17O25L3_7Fa62OxZmEOn92cQy6Qe-AZ_NlY1p07UxJNutIxSJ0yrwF-oKyFrqHTVHuQbgGtQn57r4qE8xAxfACmsuknTwbkxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Oo8lL7ZwDodrWrNyDjsonPq8-7q5OsylIT_3JuFoy4HYlAgAmViwR2cPobuj8rbtYjoZbcgaXGfpx7Wvy-8Tnyw1eTNpmWDeLw7kjkJByqvHf50oCjYbfKXRsy6r-AQZBvTfvyj2UCgDJlFGu4n1_ijM8C7zqrQjt0o6RdDIrTDXLABpV8Gv0kqG8ozT4UT-Vc4aOq02ofdDEIoQiKb0lg417iHqeGgutSFFjH6rxW5mgpm6Gr8Abuc8C2tVSJBKMqWOTXDxKx5FX0la2h-MmCkZA7_IJ6U4NQiAXSaFvrON4Lyat52g3_QtixcLvrri1TIHv9u4PgWC8BEByodPfbNzaO3JGTZ42HiaxaVQ249uRjhML9N_Al1EdChdIc52E8JIsB_J-M4bm_vLASWNMStLMyuq0ROZNY7q4rb3mCi_3QdI0imKyEQrlNXqX0x3UgY732sn4HKlottxjbEiHmhKfCpC-BJ9LilGJ-N-zrMsYEal_Zz4ekzjimXc1kWVDPEPs4A9HHgwiPM71e_VEPO2ElLpmriqBny56qn2gWoLdBUHcTiZ6_4Cre9Uo4c6SCJ4Pc3zgG17O25L3_7Fa62OxZmEOn92cQy6Qe-AZ_NlY1p07UxJNutIxSJ0yrwF-oKyFrqHTVHuQbgGtQn57r4qE8xAxfACmsuknTwbkxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=d9UTGSA0AeKIQALyPmjwdU-Lm90cNLcmSlUl_Ub44m12LCMf9s0i3knCruDc2J1tx0OZtGwB49h0grpnsnFAQ-jn-ELL5Y5KvGJlScSp5aN0RAdV2nirPyq4dwZQseIiHmUOhl9wexnq9iZ1tbE6eN3n5IK-l4R_kWQITJCfRT5OxAYveJj2K_p_9lurEMWD4G9Sp0nC5AsQ7hd-WilTjJ0OvnKA7RYLPW10oDkRq42st_h8GgatjgxE-pYAhvM79kDCe5_I2t75oHoNtvtACaYTwzpIt83QOXH48_48EXibpvDUZKkjLOI9BXFoBuicss4oHphqPdntTxHCmvxjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=d9UTGSA0AeKIQALyPmjwdU-Lm90cNLcmSlUl_Ub44m12LCMf9s0i3knCruDc2J1tx0OZtGwB49h0grpnsnFAQ-jn-ELL5Y5KvGJlScSp5aN0RAdV2nirPyq4dwZQseIiHmUOhl9wexnq9iZ1tbE6eN3n5IK-l4R_kWQITJCfRT5OxAYveJj2K_p_9lurEMWD4G9Sp0nC5AsQ7hd-WilTjJ0OvnKA7RYLPW10oDkRq42st_h8GgatjgxE-pYAhvM79kDCe5_I2t75oHoNtvtACaYTwzpIt83QOXH48_48EXibpvDUZKkjLOI9BXFoBuicss4oHphqPdntTxHCmvxjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=inGG9ocvstUJv24SxwVZmG4GdaLoBlEZ7x2lg2uMXON5KfaQAuN1b6oLdc_Raor4vYP-5FqBmOV_W2q-MZ0Lnhm9hhrOMdRR0cilzP-d6QNZUJnYw7IOpl0S-QK7X1mddGoHVInOu_XTjenj4UfyAZZzYSnvd42IcnC38IeqNusjo5TBC5lXw9YzjSILebs-wCDhTPIKiuGhCLIjuftphcGPvee3IWos8XEeLtoDIqmGko6zViD6wzaw87Kj8vK68NQ_icA9V2xjIJ_BqjpbnxDuejnGyHBicFJNOuhLzPjxwBM-ncULPr9j2feQKS9TNbgiBgbc-2b4Ti4o2M7COA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=inGG9ocvstUJv24SxwVZmG4GdaLoBlEZ7x2lg2uMXON5KfaQAuN1b6oLdc_Raor4vYP-5FqBmOV_W2q-MZ0Lnhm9hhrOMdRR0cilzP-d6QNZUJnYw7IOpl0S-QK7X1mddGoHVInOu_XTjenj4UfyAZZzYSnvd42IcnC38IeqNusjo5TBC5lXw9YzjSILebs-wCDhTPIKiuGhCLIjuftphcGPvee3IWos8XEeLtoDIqmGko6zViD6wzaw87Kj8vK68NQ_icA9V2xjIJ_BqjpbnxDuejnGyHBicFJNOuhLzPjxwBM-ncULPr9j2feQKS9TNbgiBgbc-2b4Ti4o2M7COA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qX_NQkqU6s8IEnGXbZPVmUCI5aTVBA-t3N-2dEqdI0T4c_VkCtiLRMlwbN_hpU48lNT102_z6uOgYg8hoAxj2gAyDOf2imMlVuzrc__nJquqg8fK5EF6DjalANik3nJLa9jSV0iXGal-JvJQFFzsiuupreZ9zjlIAVqNPxMmvXdbtW5DgFKAIEIUN1GX2vG-Zouj1cDqAPCcZhgNj8AuCSH-MBpIVkf4xpgV59u4hmpEXqqGj3_lx72WXR60s7uiEdNk8pcjiSbMvbbZBAL97Mx-9-HuOPZImZyY-fakmjbT-31LONNhtKryOn7p-cp8cR9KPMqcoKH8Fz6bMMpY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NO3GPv15tLvKapDg-eowT_wrfG6Ql3bTVQdEPh0-mTzF5xMp-cPxAORpEyMp8KNFHfBpD4uBhtvR6RQWX3s9QlzJuRs-Yv5yuQ8Mxcnx72TiWSh9b1QIrPjk2qo07vECudWEznf7cPYG4Jk4SLUvf68kgU3YpBZ1flpkuGXQq2Z0gXgNaGJ1S7VYts7AfhEk-cmcRzs6WppvkmTwzKwVddine5gSM0RJ0u3I5nEL99K8JVZL9wnWBOULwWSuzPzVfnhKrrGHnIWA4Fnx8HXk7krIlrUIZpiohEBPBZQve7dBpY55uocUARO42tSD43cV5HLRvCYBzHt0lC1yHBDvdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=LzQXbcGNWeIN3mZKgtnx5hkLP6TMUdOZHoUGpAEaFGbzvsJ3f4ddcbZrYhp2kqnfBjGOsvbQQyFWBi0aS_7_9bXp7I5_StIye7tzpWCcb-Mhu3Z7wQvxbVTEJPOOAOQ_XK9uADcZSIVqIndG3qFMaiSNvZ_Tb27GXyt9_SC0HYD--2SUp29dutymdXgVOnArh7tDtP6BdPRID_naNrJu4r5g90Kw3vxy2-1007TeDZbsaKqpoa40cRYlLcvO9LdaMZWxmIxFC7gIbHwouuVSkZU-STw9hLYwEVbpBLZUWsrBA3vJYcCr30ZTtvXX1mXWFq0sixz4y2gqcW_jDf2c2RKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=LzQXbcGNWeIN3mZKgtnx5hkLP6TMUdOZHoUGpAEaFGbzvsJ3f4ddcbZrYhp2kqnfBjGOsvbQQyFWBi0aS_7_9bXp7I5_StIye7tzpWCcb-Mhu3Z7wQvxbVTEJPOOAOQ_XK9uADcZSIVqIndG3qFMaiSNvZ_Tb27GXyt9_SC0HYD--2SUp29dutymdXgVOnArh7tDtP6BdPRID_naNrJu4r5g90Kw3vxy2-1007TeDZbsaKqpoa40cRYlLcvO9LdaMZWxmIxFC7gIbHwouuVSkZU-STw9hLYwEVbpBLZUWsrBA3vJYcCr30ZTtvXX1mXWFq0sixz4y2gqcW_jDf2c2RKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSR94xK3oczeez9C1D0RvPZiFEE0BXXd_jgP5r9hGcW-lTROCEUQR_xp_jpwQqQ9CmQQrZSGLS8lc0fB-yi4NDT8vveoGxCJeSuTsMNz-IM-3OGTnnzJMzq7-EVxLryiERGFb6ekYdBDoMe9KPlVVNuL79OCdqplJhiEvkNn_3bLKG_dZkrpolmgbHpXGOQ622Hka7ZCm7tE5I_lA8CqZmoM4izkNV5EZyDuPhgkbVvePE6RbmLu2xD5VXA-bgXN2xQtaGnUwFMuPyjGjjTOQJL1h7e5e4vlRfJmSmEREH2B3tB8R5BxpLoA9o_tQV41cgaWinAOptqQajDj_W0eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ent4YwPyNUx4RZXfpH92-dEFdje0lkLCnTSHL6lBUj5aJaLrTJXLlc6akG7RUs_yNEt8mXYp96cKdh5hxyKwyE1jc-nuprernRAXjV8yNx4-MWw_kFrDhtaFWeUIgUZMgqF6Zd1QyzEp7n65QKeOPDxlUdq0lyNc4XhfAWMiLgtgmRARAyyO-cDFKsUXWrp-5rvdZNX7meSkcTwDhkCPRiF4O_S88mqmY0TOjf4YuJUwCtOvpH3VJ0-3VC7Ngfo6CLA5f3VrfN4Z11cz_09KoJg9ChKfQW_T02Ku2HuGSN4TljHvtddPOVZN-o1-0u2P6G9SQM8kvSAnn8GLSW__FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFw4ePORum8XiSdgmK2j49atu7PLUNcH82fxqq9o6sjEiremcOTYniXNPL4tDIbxlLnMq18oUPOD5YzH_vIa3JJfPpqEmEWL8EeTaGzIBcf3XK17rd9OUbX8tC6wVlaKDmxyKtapULqnmRj7Ytt6vVV7tKTzeyU0GDJUV6WI9G8T4gYpB5noUKy0g1TL5n8l7-Z8fCkycnKyLvb8ax58noNm8Ukbz_ChqlIH4sDypPYoJkCQrnDB2FUQ2iB8rMr1HmFuC7GiniCko5domWQTE0f77lSqUsG4pRfeS-_YEeSLw3EGYnevqQo0MKbIk9XeCp6PWHdRw-GMy2qn36TTiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoImuR3ox_KB_5w4my-TQ9Q5pBqUEYvLQP3D2FrCJ-qQeEFJi2NEJghFtKL8nkn0edHefSaMa0Dq33ZwarDcNKZf-CU9ANnyDvus22rbyCefNQDMxi9ugnd7T5RPYanriHKMG_7V9zGTPZw7dUS4x4BIIDmtED2IixUMPPShTYHcFUeixD4ak9eE2tw393ND6h7KdoDgfK7CaM9XFLP_mGrfCMD7tfewTei6FBkqTqEFPR9COKHVz3MWjpSDgVVYbl29tZ4QJV02fDxCyk4T1mad6Djmo5WxEu-FQIGVMxvk8bxUXHehcb6FKMA-Ch-KuvNdR_0yWDhs1Aosh0tAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=qAixE0KY1U7WYa8-4FxcmQyaHf4tVxbQK_G9J-7ZsBLSQ0uFDuuafJkRNUxCeBH3ORlKTjqXVjIxI1wO1LF2z1lGLUs3Mr73vVXGCQC9XfiE6prW4VBtOiVf__-1bduEpch2mzRaOODHzEuBo2HGcT_SBKBQ_berFk11DoJLTm_tBPbtUUhAugHasO4Nq4imye7ZRjQyFucy2cBMlPGHoOjug0Fp3eGsKtR6Xij03t-raqaYh_FCZ3wbhqI-No93ozzYhRunCW9TSEJmdFYvsxTwsXGqKyXgWgz0bv-gb6OpM7Id71djb9-Q1bskmekYeyiCI4aFHoRysr5ne-1B0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=qAixE0KY1U7WYa8-4FxcmQyaHf4tVxbQK_G9J-7ZsBLSQ0uFDuuafJkRNUxCeBH3ORlKTjqXVjIxI1wO1LF2z1lGLUs3Mr73vVXGCQC9XfiE6prW4VBtOiVf__-1bduEpch2mzRaOODHzEuBo2HGcT_SBKBQ_berFk11DoJLTm_tBPbtUUhAugHasO4Nq4imye7ZRjQyFucy2cBMlPGHoOjug0Fp3eGsKtR6Xij03t-raqaYh_FCZ3wbhqI-No93ozzYhRunCW9TSEJmdFYvsxTwsXGqKyXgWgz0bv-gb6OpM7Id71djb9-Q1bskmekYeyiCI4aFHoRysr5ne-1B0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=eVLu1JAuzTQ_-ROYFnP33tmgGNB55Sw7LB6gVSKuwbBgIdbieHW3tNsjKW7qcUDcZWdC9sA0AxyJRxA5A3TFbUgZW-giIcUpMmQMMuFXfUmKnM2Z5YpHoB2HwweEDU9AfO9gC5oZFnq0qv4Gv_j_IMAYXusZJZ6z2A0gf2zIi1uXILvP3oa9TCOpNO9_Hkj7oo1UHLdhHMD33VHjb-Df1yuwnz90Z3n0MBwQBVSLHG_nV5VG2dKTm_h7xDDvZUYneuRsnOH-_Sw_ULaX4W2ww5qiqrDOb1K0U2eeYidTrBeaAf0q6T3MV4SnSBDcJcY80LxnS_mZTrBoD1l_1_OK9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=eVLu1JAuzTQ_-ROYFnP33tmgGNB55Sw7LB6gVSKuwbBgIdbieHW3tNsjKW7qcUDcZWdC9sA0AxyJRxA5A3TFbUgZW-giIcUpMmQMMuFXfUmKnM2Z5YpHoB2HwweEDU9AfO9gC5oZFnq0qv4Gv_j_IMAYXusZJZ6z2A0gf2zIi1uXILvP3oa9TCOpNO9_Hkj7oo1UHLdhHMD33VHjb-Df1yuwnz90Z3n0MBwQBVSLHG_nV5VG2dKTm_h7xDDvZUYneuRsnOH-_Sw_ULaX4W2ww5qiqrDOb1K0U2eeYidTrBeaAf0q6T3MV4SnSBDcJcY80LxnS_mZTrBoD1l_1_OK9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaAJav4KHWT0YaK98cKWF7kZE0IA5MjOUxmYy5QXCARtCzOzikL9mEdA0ozeF2TJReO5yi1uEVUJ-GxHcV2UznN_7EtWwCMERS2CIkIyBJHQXfKNGXJ_SMt26CgY9Dcn4-R1ZxXoUXdVHyHQsIxB1ZNMcJfNF3AQS1HfdJD4sBCQ91p2DffVaRFAru6aJVwiWs2FAenaZHpfbUTnrkvKfbR1KJN_0g-YM_KEWcjk7tWI1-JQW9hsPQEmRzl_NXT2ko8yx4ltRVaE7h-grAtWCMv_Yxk1vF8s0-uP-9jlklnvzmoIxe8MWo4Z1raj5pxABLeFPSWP_Yw_sL3SgQNDkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Xp7-oB5lbFDpxpoxs0Qot-n-tEh4q5Utzqzf432dLgiTKkT0decK-nNmhSHH8ccrwec590zvbHIQY4lRAOORncqUTjhd0foTITUZX5xnIPpZOchFqVlDNRsWpE-Cv28PPgTN7A7Oj1WaAyEqGo9zBAWsX3yqNI1Kq1D1b6RmC99pokW92D-9_2NT_yJTOqv2zs8irvNLQl2AC9i-dddHn9Anw8oLBhnSqvZm-mcMp5MtijrNv_zq8XBgXpu31giqhPbzkHLNN8uO8Cp25xyfP5IYoqGWotO8vIH_3p7a5HHvacRBF8-6QjuoNl_mgTWiRarEORgU5_Fa3z4IxtZwTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Xp7-oB5lbFDpxpoxs0Qot-n-tEh4q5Utzqzf432dLgiTKkT0decK-nNmhSHH8ccrwec590zvbHIQY4lRAOORncqUTjhd0foTITUZX5xnIPpZOchFqVlDNRsWpE-Cv28PPgTN7A7Oj1WaAyEqGo9zBAWsX3yqNI1Kq1D1b6RmC99pokW92D-9_2NT_yJTOqv2zs8irvNLQl2AC9i-dddHn9Anw8oLBhnSqvZm-mcMp5MtijrNv_zq8XBgXpu31giqhPbzkHLNN8uO8Cp25xyfP5IYoqGWotO8vIH_3p7a5HHvacRBF8-6QjuoNl_mgTWiRarEORgU5_Fa3z4IxtZwTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=N-wf-ItaOnhvXLVP4JTl4IjgxyaODe7-leImttTwBPeZ1cGY10FMsHAfXA2g8MFyoLbLcj3xPa0K2DiriCeYRsWVEktjAjPmVl2iJLF_mnzHePwlPDrhY7VaJKTYrv6jEBBOQ3uajx49ObDdzpi8BW-_B22xpuyZBF_yf5sV3u8IbRHt32Emf84BbKYbCxWI4EZ-e_Fiy7pPnS2kPXPyZ9oxizToyw7uAzc5knIdmygzibUaPxh9NHISGr0TCZG5He5l2oyv1DI5gmjZccofdTHrq8B_luwTMA5xzdrSMA3cn55aZ3o5bgkvZuvDbtEYWs2qkOYNvVBgeOh-E5TwSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=N-wf-ItaOnhvXLVP4JTl4IjgxyaODe7-leImttTwBPeZ1cGY10FMsHAfXA2g8MFyoLbLcj3xPa0K2DiriCeYRsWVEktjAjPmVl2iJLF_mnzHePwlPDrhY7VaJKTYrv6jEBBOQ3uajx49ObDdzpi8BW-_B22xpuyZBF_yf5sV3u8IbRHt32Emf84BbKYbCxWI4EZ-e_Fiy7pPnS2kPXPyZ9oxizToyw7uAzc5knIdmygzibUaPxh9NHISGr0TCZG5He5l2oyv1DI5gmjZccofdTHrq8B_luwTMA5xzdrSMA3cn55aZ3o5bgkvZuvDbtEYWs2qkOYNvVBgeOh-E5TwSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=U2hHkjFHXNGBcdEFkTqzCmvoRXZ85EB08nzmF0PdugXMj28yg5GLjQFBXJgs2Hx5oZfXaxbVJRgENOwhRJ2lOQeD4PNRQFMzRu2-Zg6hnZjTmWW1autRFatuqmDHApkkne3YxIBqlGUuE6c2AOsWnSEAIVtVq2x44B89PdUE5bf9liBSbKJ_PbR-bLq25dg1lp4OdBdHtBpBdR0oBFceQxhLxasv8HZ7EKv__UvMFifgRkR-U7hx1c6mK0mvJW3dOoFxTqxH_Yby2x-xfH8G8KlAGxr4efkTjSPn4amGns_BNzICFp6IRjEg-9kOEsinuuuA3UI0B3bhrk3h_n0ISg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=U2hHkjFHXNGBcdEFkTqzCmvoRXZ85EB08nzmF0PdugXMj28yg5GLjQFBXJgs2Hx5oZfXaxbVJRgENOwhRJ2lOQeD4PNRQFMzRu2-Zg6hnZjTmWW1autRFatuqmDHApkkne3YxIBqlGUuE6c2AOsWnSEAIVtVq2x44B89PdUE5bf9liBSbKJ_PbR-bLq25dg1lp4OdBdHtBpBdR0oBFceQxhLxasv8HZ7EKv__UvMFifgRkR-U7hx1c6mK0mvJW3dOoFxTqxH_Yby2x-xfH8G8KlAGxr4efkTjSPn4amGns_BNzICFp6IRjEg-9kOEsinuuuA3UI0B3bhrk3h_n0ISg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHPAmag1IFGcaK3IatpufsJEz9SrxCJJ4E-PfMS23kAswXqs2gnWjF30vqsuRKV_jJdIOhxKd0ODxTdYI02XOB2M2sdr-U0hvqSdd1bjBKX6tYDfArv1YwkP-y3y6oCgTeEiNdVx-Ot95vSAY6XaN-2qpaRMXlDVf88AxNydHFS7R428kzHxRztkc48LVaAs_u7x0Wj18Fag4nwt-2DEXcIgfutJo811UaLKsTl7-UlvK0nLSCwahrMovk--7H_tXxsYEvd6l6mnaCZAdcD7c3fNJliFwFwRrZRVVvDacGgu9NgMSXVm0z_-dJ-a70myxNGN-5zXckLX7Ean7kAidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=pKoVEQJJ9QgGgvcZL18sXjYqLwzoLOS_moB19WxERAaN5C1o6QN6xoa7Vya9q60e45Vyc3vRDHwsleqxJKCzgx4fQbms3ektJsOdQ2CO6LhxmBimntueHESDHylejfmeivD-dWr4cjsultQ0MWyc6tsVReLKFdIWd0SfEumqHbsziNujNcdliIiM7o5eBYf78lfspaaoKsCQe8qjH-O9K9smB7Fvm-OJR8-35zsO7XBR5LPe0d_ziv5utXp55wcZp_PUX_P-t-nCZu13-N6iqtDtaRUi9MLgfv1yjz5FwjpEr27228whKqHV20J4KtrZtYkfC1_CPcc4mybJHxyyqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=pKoVEQJJ9QgGgvcZL18sXjYqLwzoLOS_moB19WxERAaN5C1o6QN6xoa7Vya9q60e45Vyc3vRDHwsleqxJKCzgx4fQbms3ektJsOdQ2CO6LhxmBimntueHESDHylejfmeivD-dWr4cjsultQ0MWyc6tsVReLKFdIWd0SfEumqHbsziNujNcdliIiM7o5eBYf78lfspaaoKsCQe8qjH-O9K9smB7Fvm-OJR8-35zsO7XBR5LPe0d_ziv5utXp55wcZp_PUX_P-t-nCZu13-N6iqtDtaRUi9MLgfv1yjz5FwjpEr27228whKqHV20J4KtrZtYkfC1_CPcc4mybJHxyyqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFfaGQyWcVKHYh2llnsLuUTTGMJfUxzTOlrUfdhSMlnsLGNLnirkSw1fZygQ47wwEPavaSJJ2LA-UtDj0MSH_4gjhnkH6V8-SMvUSCvVm5zUomfkqkky4ch6bXMSC-PxuHCZT6FCh-nyUqTV_8S3emGEFxbDeMoc8PO8FRbKIAojybVXk6K949NDegkEyCqgJiHDEs8velwHhi3yIDxgudxLj6VOtM6k3bhAEuTNCHu00vrSxi1Yd2frGnIVL-8yyXaC284rK9Neh13Np1255oqtQu7d2EtKFIZqPQotODBq7nqD9lQCL-tsxRmIAoFXXrI4HPoQq6O8MNHPYg9HPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZvRlGYl5d27Tp9sCor56PkJ9PQiPGG10CP7V5On7sNAyHIlXtcipJfOPB-BW2u0HQ-I9OuHlIumnVHeq3bXdZkJFqh9XNjHv9BzcGYFkLUJVVe5n7Sl7RsfcLztGHICn1fgpCwiX0ehopdOWdsTlv8mGmMMd0em-KBxfBR56r17XkkeDd_1s-epMyE1GpLOfg-iuycERhuNKlOe_fd9v8s5Q9X2tgxcyjdXOWpSPF5Vjq7isBuzdwcUtAwJrupLAiu4ZqQj2S8R7Lb57o874Oe5sNQn-8dHJHJTBXjr57H-qpb7vGeqBsM0Cu477NK1I1Ygg4xv6MZEOf6MmPT7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=JEEYXhCmHsyt3TrfDpLhVjQBN6ll-AsV29m_WBb4BAjWkcJrZ7r2LkbmQdMPtWNDZhS9TIOm2PAeyW2F8dI8d-PSDph9a9XacOd5YIbaBY7-3UoNAGj_7asmefVbVRNi6JK9q0AssJLt6lF39uZA5xpGihKOTSgzxz41ScVDYBtFS3bbPsiynEZixo72sbuaA35I-c7bntF1MvQ3ZF-oobLlRaONpGthbkE1BbuS2q4wHY6TR-t-rieyNu1FWfra7JySioabkSrV4jOy4AQxNH2oAghK4OCzzZrjImkf1FLXSCSkr0zSSGkRwtuVqQTRPNuvSPO0Ic-8k8mZNYhzyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=JEEYXhCmHsyt3TrfDpLhVjQBN6ll-AsV29m_WBb4BAjWkcJrZ7r2LkbmQdMPtWNDZhS9TIOm2PAeyW2F8dI8d-PSDph9a9XacOd5YIbaBY7-3UoNAGj_7asmefVbVRNi6JK9q0AssJLt6lF39uZA5xpGihKOTSgzxz41ScVDYBtFS3bbPsiynEZixo72sbuaA35I-c7bntF1MvQ3ZF-oobLlRaONpGthbkE1BbuS2q4wHY6TR-t-rieyNu1FWfra7JySioabkSrV4jOy4AQxNH2oAghK4OCzzZrjImkf1FLXSCSkr0zSSGkRwtuVqQTRPNuvSPO0Ic-8k8mZNYhzyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lNOT7lJmHdA7oxM137fkzLXeHiuYpl8XA1V6uVHS-dsoNz3ZLeo9Kl6XvcuNRF2PHsg36COAcG-Ro6p8pya2ioqid-Z1_IOMF_Bxk-zd5w65kL2Rzt2bqEFep1IvqQoIvjpTp0_w4eANzFBXo1RaWwXB53WO15_bsnCa3d7m8ZzqznZqAO4izF-kBBCXJPup3lTZhrvbHGTkGv1eOYQwwpfi_FozdYP35a8l6qXE-M5QA2xu44xyPUV_tFaPy4QVwxUnn8WGc41EZsMrVHmyC5WnyZfSGqhT7TPtXBw93L_KS84YrbzcvG_lAWtZ6L8xOLhdMWP2iTUzRFCfSNpc6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lNOT7lJmHdA7oxM137fkzLXeHiuYpl8XA1V6uVHS-dsoNz3ZLeo9Kl6XvcuNRF2PHsg36COAcG-Ro6p8pya2ioqid-Z1_IOMF_Bxk-zd5w65kL2Rzt2bqEFep1IvqQoIvjpTp0_w4eANzFBXo1RaWwXB53WO15_bsnCa3d7m8ZzqznZqAO4izF-kBBCXJPup3lTZhrvbHGTkGv1eOYQwwpfi_FozdYP35a8l6qXE-M5QA2xu44xyPUV_tFaPy4QVwxUnn8WGc41EZsMrVHmyC5WnyZfSGqhT7TPtXBw93L_KS84YrbzcvG_lAWtZ6L8xOLhdMWP2iTUzRFCfSNpc6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
