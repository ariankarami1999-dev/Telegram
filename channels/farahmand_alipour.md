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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BujRTDtFq6zHFwha7QuQIrLZ2RyrlnALedCLhpGVXTQrfd-AfZKnNScmgRrcmOPMM84kizAi9bJxcHFbsrLwajM9fXww1Q_Cx7B1f5Mx1wohriqYg9ibw8ISvKfspe2E6UWLlf5DZc3lx82FNEImZ_gny3EcBlY-f5ZOkDbp-JllMBJW-KQU5hb3F3KPJ25DQV2rg0_widHqGi_IRqKZzGxkUS8g2kAM9f3czQ4ZMnrin62HBZ4nGMVT0wT2ssg5dYJaYzk9XtIOKUR-m1wYnd5sca7OjrG3DtwNMyv2L99GqHgL_6EWnogm5wUyoRMMOnVOuNCp9PpnFoPXRqcOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APkb9ldN6y7D9Fv_2damawI5304ZzkJPEQ4tNgfSB7DpdNmuAJb0pkQamqALS29lUhsMjbA34osRf3TtARZNxq3yx8dIaLaJtsNOlEfBv6l2C3M4Cf866uHUYBfYNjWz6u_rkYfOUHhqNBAjHbH6ytwdcDzEgI5E57nVn4gqWZ04qfqQHjzPAZm6uUAA2pkgu867dqhdtzQ53vHZ1pIuXRdP-mUYkrYndVTPTqv6GMEnoq1EGO7tnBKPk7nGaX8tNraHzDoWgOBNFXcUOhc7sCheKhPwXVRxVMqgyGRAXC2kl26SKIN7LtIaR0ehfe4OiFI1fsXAUXvpOvRHOzXRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKErFHuEf6H2ApmbURciMzEgDUKLTPin_5-3ReQXcGfT7l4eBq5PvObOPiuTU-q5owDtS0BzyxWSASqeIdZDRiL59IgIvZqX1lpWexsA39K0ffHd7HzZtleoUXXustn28cfGxoCEZ2hnPUr21Jy8hbgBBZtop_KKNs0Zrlt_b5N6izOthglImJVRYM7RIIoPEKoF-YWmP0ndYg4IkJitcM6_qSwErx-WM1cPaXxKj9YZNsmKidgDUwrCh8sMuqOeyJf19n49jHbUI3HqJnlwjc_CLwkRWySIPw1YPWs0uj_xWPRqgFQL-mCSWw_wOX_mA_y1tvOGnozKtILmyPTefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEhkcn7Jhd7iSoUxGBcDanF_G1Td7pgKaC7OhsD4BbD-LQ_2Jae7Vor92qjaZhM-dKmCQDXcCFW5VHMmyzAS4KHy-9hQAxamO7g6kk_uikU0QhLMVBNl9p_ev4UPHul8zSO1X1TCsg9zqRtRrsq3z27RPeQQaImwFTjzxVLRM2hv0mnWJVlvCcaB3PaaEYcpbjYquuESeLv_VE-Mpk28xPWRpQ__5EcohOY-pw5IAygcN1NW9ggP7kP6bENqkD9xWDL_x-0jBs_Uts3lDZcv8b5m57BYKt6a48dKihhJ-UFFxeBPWChZmR-ngaGfsN3dvO9bA7pCmZa56d0g1XuMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=OIWGfNFlH9dAUY4rnUM5dVqT7CsOq1TPfhABNqVF841JN7qng-ny9jjxIjTmXi6j9rqY86mvtoykhfzO2LQfVE-Iun_e-ZJey4J3LDNuogEuP4fYQ5SUhUNbepFX7AUrLUk0eHtJZYbuiIAyxSHI7-i-BdYAToNOzHK1lL00JQkucYSm9Mis7tUpVGk0cVZBSfF9Sxj3eJtXjCSRHDFN8n1PGWoWKSCOtnhlMki7TLzeudIrpmRuYDZwQDgqUXvqkuvcY8vkkWOt0527PU-w2L7gicNkNX3CsrifiyoOOr3xDHdwLpXAk2Rt6FLcmgsvZP7b9k3Xr0Po592DCC-F3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=OIWGfNFlH9dAUY4rnUM5dVqT7CsOq1TPfhABNqVF841JN7qng-ny9jjxIjTmXi6j9rqY86mvtoykhfzO2LQfVE-Iun_e-ZJey4J3LDNuogEuP4fYQ5SUhUNbepFX7AUrLUk0eHtJZYbuiIAyxSHI7-i-BdYAToNOzHK1lL00JQkucYSm9Mis7tUpVGk0cVZBSfF9Sxj3eJtXjCSRHDFN8n1PGWoWKSCOtnhlMki7TLzeudIrpmRuYDZwQDgqUXvqkuvcY8vkkWOt0527PU-w2L7gicNkNX3CsrifiyoOOr3xDHdwLpXAk2Rt6FLcmgsvZP7b9k3Xr0Po592DCC-F3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KurUdiUQFJDGZqJXu1SBJedos0rvnPIFfCvFY1SOvWVZrZdermD7LLdRFYig2qdIbmOzaf8WEOH9f8-xdYscR08qrSIf9lQonRZyCqkQO2X9G3THwY_MpQlSDKUcWA6TvFDasivDstk3POdATCk2AfD9zYxn0R57vogTSMGwMCHN4fV5Ngj9oSHhUTx6TM6EUlCtRM3ggjFxGP9l2-SjQ7Taw0uOyVdL8xCCHc8KApurfKbKNyj7o3IJrSXx-O9ROj5f7T8s_kc5-YLCBp63QCIjZfhgff-m51OL7ZOZOndW0gXsAV1LpH--EAyi3eJ1AtTRgSuEz2GjOf4u9ORHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Zzu4y7QB3enEN-DVaV0NQ_YlTP3X0tkS7oSPBkxCkHAbIPmGcevN8r3CoN1M_0J4tYSA6iNANiGGrCuzxplLRxVFRBCQS8bUG3S0qDGoMSQ30UxGl1MscrfV1FU0ASQRHJzy6w9bz4-yh7XZXH2Xnu64Q7TuBp52T7RoxDjSTYBIoXcir-FvcZT_bHWst5281nIGcqVDJnnBcZF6jBDWscZkPxnMy21WyJB0s0hzRPW1Ax3PV-27IY_rjTP-5rFvO9MpfoHyQY08dCu5TQCVG8UXJXPY8thL9TEE4VT7SrnN8x-BHejSb5pxBrAKUEDYipSsKYjzTFWQlKOxuo9U4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=Zzu4y7QB3enEN-DVaV0NQ_YlTP3X0tkS7oSPBkxCkHAbIPmGcevN8r3CoN1M_0J4tYSA6iNANiGGrCuzxplLRxVFRBCQS8bUG3S0qDGoMSQ30UxGl1MscrfV1FU0ASQRHJzy6w9bz4-yh7XZXH2Xnu64Q7TuBp52T7RoxDjSTYBIoXcir-FvcZT_bHWst5281nIGcqVDJnnBcZF6jBDWscZkPxnMy21WyJB0s0hzRPW1Ax3PV-27IY_rjTP-5rFvO9MpfoHyQY08dCu5TQCVG8UXJXPY8thL9TEE4VT7SrnN8x-BHejSb5pxBrAKUEDYipSsKYjzTFWQlKOxuo9U4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2iBDKl-qD_N0WFKAQ_iU6vIq7Pf1w5-xVRkNqESU8Vyc2BRLMfmANjJNXArnN9VOEXnOzpG3t_cpvwt8NzZko76mM7cXBbyFx1Gsk1AGSHgCwOuXlHDrG98RY06DoAbNktWueA5O3QGoOLUJsQa8n3ZF4XYglyjiKIldw25nH77wMtref8ojlWYcm5C1vn4gpDw5HY4xqEzc298trGT-gGMhJo5HTtORDEJNqwvlqztqMyJxBr-rwcP_-GzBTaWp25mu8VmniWUlEvIESR0n_EheGgTuxQY_TDmMI9gVVvKYNuOENbj5ap15_nOX0BqcYolOA043aqZyKNu-Y74JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=hfWN8MLJNp5HHpxYf8k5A5C9o-2S5zGQL3UVxZH6LTgMzgzzt7KwxGXIOvUc-uaQq9gEfrUepF_COWNyIHcFMTbgcm4yYaClEBUUS8tyf9VPKAoxMC92JFK26gLUay38ghsBhjWQZblvghW0p5edQ28bTZzUrkGbw7drCjqoQ4psiollFoyFhTUARfk3eUvizU3FDhjlSPNLxJ6qTMsulU0U_bA2xUqoUHFB25yURIzd24DryvCv5eOtC-tk7EwEXmC46Nj-wE8L7Y4hmxartQJdn6yAqjvTBlx-9pYDxAtq9tAoSp7-mjxWThQJy3LG9oahLBycgYgBaY-Z6J3ZkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=hfWN8MLJNp5HHpxYf8k5A5C9o-2S5zGQL3UVxZH6LTgMzgzzt7KwxGXIOvUc-uaQq9gEfrUepF_COWNyIHcFMTbgcm4yYaClEBUUS8tyf9VPKAoxMC92JFK26gLUay38ghsBhjWQZblvghW0p5edQ28bTZzUrkGbw7drCjqoQ4psiollFoyFhTUARfk3eUvizU3FDhjlSPNLxJ6qTMsulU0U_bA2xUqoUHFB25yURIzd24DryvCv5eOtC-tk7EwEXmC46Nj-wE8L7Y4hmxartQJdn6yAqjvTBlx-9pYDxAtq9tAoSp7-mjxWThQJy3LG9oahLBycgYgBaY-Z6J3ZkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=PNsVKjDwDs-g2yKK9fMc1sL3a1sT9dvxm_hLdCrkL7uWqSfnyqrHtuzVs6Dt9WOoGqR33JATW8CRScyhz4qHn6Lj2s_cw1JHSAZbhEioKIbkq5AGEAsvAIlLezYK-dnyRRR6_kDX1Aq6Sx3MRqx8JCEhUiw2mGNaU72rwyX238l5crYN71ObKykOjqaHrDC9zmz31gechqTTabkOrm4PEnAnIV0RyOuGTbBExNhlH-e8XZJCaXhvvpUDhtrRWhQ79pV38jL9DnSHmfCt8MFM-NnBetF9Z7-2-QHxinJHzLaHC-0eMODf0WPKk-9OgkTD7liwNMt1D9GIz3ADNmDtiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=PNsVKjDwDs-g2yKK9fMc1sL3a1sT9dvxm_hLdCrkL7uWqSfnyqrHtuzVs6Dt9WOoGqR33JATW8CRScyhz4qHn6Lj2s_cw1JHSAZbhEioKIbkq5AGEAsvAIlLezYK-dnyRRR6_kDX1Aq6Sx3MRqx8JCEhUiw2mGNaU72rwyX238l5crYN71ObKykOjqaHrDC9zmz31gechqTTabkOrm4PEnAnIV0RyOuGTbBExNhlH-e8XZJCaXhvvpUDhtrRWhQ79pV38jL9DnSHmfCt8MFM-NnBetF9Z7-2-QHxinJHzLaHC-0eMODf0WPKk-9OgkTD7liwNMt1D9GIz3ADNmDtiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=eGxTKupWY4IYUuroi4doOqyv-9aZbW2R31QYKHwM_fRDx1vk22OK9NIdRfukLqX3AWLFDiYPxoTM_muH12orlSGt5zOAkt6_yR8XHwJBvlt-k97R6dPU-iIYy0gfT6BYf-oHS7w3YxKF0uQN9dKjkNUhwcDtz4GEVF4k6YvkrCD-ES5INWp2_mX_rY4IGnXFbgCb_jLr6hDn2xtIWHMZMElPCk57M8119JKfMS06V-OAbFP5oF0x0fz2j8ugnsjw3fnm2LLdIwEXRK7SS6AG91q4HUTlQdhJULARyTMjbYW7vCalYVILHGquh-K7hSOYfnC7CGGOaLUsv61gZQ59jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=eGxTKupWY4IYUuroi4doOqyv-9aZbW2R31QYKHwM_fRDx1vk22OK9NIdRfukLqX3AWLFDiYPxoTM_muH12orlSGt5zOAkt6_yR8XHwJBvlt-k97R6dPU-iIYy0gfT6BYf-oHS7w3YxKF0uQN9dKjkNUhwcDtz4GEVF4k6YvkrCD-ES5INWp2_mX_rY4IGnXFbgCb_jLr6hDn2xtIWHMZMElPCk57M8119JKfMS06V-OAbFP5oF0x0fz2j8ugnsjw3fnm2LLdIwEXRK7SS6AG91q4HUTlQdhJULARyTMjbYW7vCalYVILHGquh-K7hSOYfnC7CGGOaLUsv61gZQ59jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=GJraNB-oE7BJCp291iV4srLak3W9xvE6iXu1TrPPO5866z6OZU3sZXJiaQjFyhlqJbCgq2rJ8a3_1NnHhZxWhQnnr4eYzyiDtJvkWmV93tmkiNyxfoTRmF-Pgz7xP5d7khlHygVed520yUgqcxAGsMALUwI0q0VL64yH5TKSFy9nLeqAonMtWrrsRZROoAF-XQA0D_1qQDYcCelnoD9ZOFUC0UtWBH08w2Q5zt6iZ5iEu7DbaToIcYQVEOFqhPNSkuoDsNH_pyNi8psMlJwITvGfU3oiL2Tk5zFFrnALrRT3tGy4epf_PO73xvAa_X_7yesRa2orL6iLMP4otfJmXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=GJraNB-oE7BJCp291iV4srLak3W9xvE6iXu1TrPPO5866z6OZU3sZXJiaQjFyhlqJbCgq2rJ8a3_1NnHhZxWhQnnr4eYzyiDtJvkWmV93tmkiNyxfoTRmF-Pgz7xP5d7khlHygVed520yUgqcxAGsMALUwI0q0VL64yH5TKSFy9nLeqAonMtWrrsRZROoAF-XQA0D_1qQDYcCelnoD9ZOFUC0UtWBH08w2Q5zt6iZ5iEu7DbaToIcYQVEOFqhPNSkuoDsNH_pyNi8psMlJwITvGfU3oiL2Tk5zFFrnALrRT3tGy4epf_PO73xvAa_X_7yesRa2orL6iLMP4otfJmXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=XKKkwc9Q_-SVRc4_1wbVbMwSRBcZM_PBUk2D_X8F5l5mRVzSOyv8SM-G1JaqD4znaOiZq45exb4JpWEd58sgldbtRM5xWWaXBrRGDlklbuO6KLUicPFJwWGEUe2L6JboHGUZuyFEXKPsSl4RG8F6rOe7OPrQN04rCLkBeXlXfx6UDB9LX5egZm4B3KUcNHEdhnHKBp9ldKchRKpEVnekf395s-X1iyWMy-6j6DommXIrxcjTQIoFlRO4ZFD9N2Z_e0emN0mwQB5Qrm17cEPuiyC8WIYvfbgTsz-Ulj5_xcLKp9tExZJcnmuaZdHMXD-R4fLDUiWanM7gzC-bUORkLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=XKKkwc9Q_-SVRc4_1wbVbMwSRBcZM_PBUk2D_X8F5l5mRVzSOyv8SM-G1JaqD4znaOiZq45exb4JpWEd58sgldbtRM5xWWaXBrRGDlklbuO6KLUicPFJwWGEUe2L6JboHGUZuyFEXKPsSl4RG8F6rOe7OPrQN04rCLkBeXlXfx6UDB9LX5egZm4B3KUcNHEdhnHKBp9ldKchRKpEVnekf395s-X1iyWMy-6j6DommXIrxcjTQIoFlRO4ZFD9N2Z_e0emN0mwQB5Qrm17cEPuiyC8WIYvfbgTsz-Ulj5_xcLKp9tExZJcnmuaZdHMXD-R4fLDUiWanM7gzC-bUORkLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQHT2mrokF07QGPezwKE-vNK8T6aRN5R8qkRpxzazCswodfyRhrLY0_TVqQkAtu4Llxfw-6aewx38iunSYFO5zrDceoB15y5A8Rx_ZCKxLl12ERyJvfLLLpvvPUqCjMYRC8VC71dhiXAiuZ8LH6aijYgcnPm_AYMMmtCporsnMobp1dubf6dTeF8FtkMMilc1Pk7DbWJ7y6p6crUkfR-rOiuDrpcij7l5BwQ3V-eB6Dcm2wsIwCkl3Yc6gGojMlpUyGDM3agcOuyQ7rETwHSd59qKfxf2GRDCYRIHOoGv3_LJ4WHaURiPiHlNftgBkRzGJ_6xueu-q8zM45eDzl_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFMkvazWqPVQs-6aIpjXrdvlQyvbOO7QM38L6XWdKjaoq0VclE-uPChoOLNIs-6oi0op0rBGUWHwRrpfWbMw05o5PEy95rMNykUyLgEN_TK3YRISvVqronNuU1CHWPsmKG_TBe3ZgSwNxnXGhHznAE-gdMkz5dZCQfMCKFt5iWH11koyxw4SWEmHFXegV0U8OnjzuniDbIUqlwQmL5ojSWlJTmH9EoHPiXKXgQezySJ3EaVWlym4i4dALxq47CkdXDOtZUWYT5er848zD3JMn8KM-fYmwu8LdFtOT1smKrJPuGENopdnirv_cKnPTMEYDW5ZRyjU9w1yK54U8m-1kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=cZkIwBBQz5JgI13szPzJxzjvaD1zuVBI-T-nAUr6-JznhHZUKZPEGvfoFbVDricSUoUrXqIPRu2qSZefg6Ga74W9_nttawuSKO49OMIBDTELzy36a-QaP3GuAOYehYwLjfFozneM70Ib0LbnyhK100rU3fkyMrSj-gU-waCNxmod2haz2I1LzNYuPkwr12jPev6h0OYoE6uq8dYs3L_uWFyAnMOXWJ1ModKNTnco1hjKlcFsa4Ko_ErddndTRnxrEBZl9i1jp1MxS1VBM3rapxFfPdjAG5kfbOLorsQ5C9DVkbyoXmQ_OgxU61nL9d2DbFa_UijWF8Z_JdE7LX-OOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=cZkIwBBQz5JgI13szPzJxzjvaD1zuVBI-T-nAUr6-JznhHZUKZPEGvfoFbVDricSUoUrXqIPRu2qSZefg6Ga74W9_nttawuSKO49OMIBDTELzy36a-QaP3GuAOYehYwLjfFozneM70Ib0LbnyhK100rU3fkyMrSj-gU-waCNxmod2haz2I1LzNYuPkwr12jPev6h0OYoE6uq8dYs3L_uWFyAnMOXWJ1ModKNTnco1hjKlcFsa4Ko_ErddndTRnxrEBZl9i1jp1MxS1VBM3rapxFfPdjAG5kfbOLorsQ5C9DVkbyoXmQ_OgxU61nL9d2DbFa_UijWF8Z_JdE7LX-OOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4J2ZMlc2DVA0f6MxWq3VWZ5FkZwcWdCKRso4BDJQWM8Nhc3gROkAd246-WWmDvV5aZkSE5Xgzib3uYkYuIM1g9GpUxG7GykD9BhwdsD_RbCrcuZN1aTqAQKnqhHrshitEm3_lo797h8-QjvQGPfUxIFccBhJyJJBMJ1mOdB3EffmjZF1OPjq86LZablaN2xu1gU9qxahmQ8K86i76u6PvKMhphIbWdj9HJDoJBvY2BXxTd5Lsh796O7iTsmgYxNFyDGthYELyNKh_zQ3P5lG6vSET51OqX-Juw-ZOdMqzbZPT4EvkItCNIvFak6Bx4Sj6Rv_7cV55PHabivrwUKdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdWs7RxAhTCTw25NM41jA-39E9EgotIPUNoysrhxrFbV3tq87ZqASHEyab98coMMRA4l_UeSNafyc-k8AaGxPqQ4JAbi4lx_U4nyXYOCm8RqOXEYN910Wr9c8G8xhlYSt8hznCcpxq455jBl3pfOlpTycKhttFm80tpGMwk_aZ5De8lPs68uCIzP3BzN7F4qVr826DP-nbjkBrCGss6e-4_B0x1NUvs8aax19i7NQ_iewe9oocCmK-q3H4zUk9dCqV4LqmSl_8QRDF-FllB71sqIyR24ldnaA-OaHp4b7u4hazaVGYF5-QHuGdehbUw6ScvUOTqMPmBnxmFfIIGxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=J8F3INSOvn-YqRsMyeDo1xkxJKOiPY3nCokRhgk_0bcxDTRTsfSu3esr_Xfcs9QQyPU2FJHRNS29p2q6DbigQ4pNlijKm6K78jPfcz9CJMVhdiNN0_lERQQ3JraHNvk_GZs_mpjnA3viIOYL7zrnYfaa3Go19wW99oMJG7C5WONL2gqnV3K9NLh5MMIy8tLWLtxmBBhFq4o1FYGcfqH68uihrc6LLXlSRYPiJD70nNWx97MWvX4qDmXczdxl-ECAj_jKvOaimjNSpdSbg7cy2yK5H6PGnSYiXnp7dCquEhwYUxWZCY3aA-GEDGEZcf_vT13hRglZ_5z8hLbf4byk1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=J8F3INSOvn-YqRsMyeDo1xkxJKOiPY3nCokRhgk_0bcxDTRTsfSu3esr_Xfcs9QQyPU2FJHRNS29p2q6DbigQ4pNlijKm6K78jPfcz9CJMVhdiNN0_lERQQ3JraHNvk_GZs_mpjnA3viIOYL7zrnYfaa3Go19wW99oMJG7C5WONL2gqnV3K9NLh5MMIy8tLWLtxmBBhFq4o1FYGcfqH68uihrc6LLXlSRYPiJD70nNWx97MWvX4qDmXczdxl-ECAj_jKvOaimjNSpdSbg7cy2yK5H6PGnSYiXnp7dCquEhwYUxWZCY3aA-GEDGEZcf_vT13hRglZ_5z8hLbf4byk1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=no_LQNd0mAHmHzqcDDCL6eaFBy7NPZZz-vIMK9nwiJlKCIqCZsLBskjK74WKruSUBS3RMMI8kv0Evgr-NEPEnxD_AUubEjNNbBToyokEoBnmhX-0PhYLw_Opo1vyOq7My_tfVmX-R_mSNBEmzrQgoRmARcFGNSuJxyLE9ZGnf5QZzyNlT8q27U6QubPJVstfJzHNIPdVeWj2NW1tCbXaHDmcatN-3secPiHA50D2twmCldVpA738hlWbvGttyJ2cMekjfigUTJidO9jWZgkBSrlc3FfOrrfBXHzTIs71cC_SicG0vNVSCX-dTFSv69nwl41EDk3qZBsTwdmXuVIdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=no_LQNd0mAHmHzqcDDCL6eaFBy7NPZZz-vIMK9nwiJlKCIqCZsLBskjK74WKruSUBS3RMMI8kv0Evgr-NEPEnxD_AUubEjNNbBToyokEoBnmhX-0PhYLw_Opo1vyOq7My_tfVmX-R_mSNBEmzrQgoRmARcFGNSuJxyLE9ZGnf5QZzyNlT8q27U6QubPJVstfJzHNIPdVeWj2NW1tCbXaHDmcatN-3secPiHA50D2twmCldVpA738hlWbvGttyJ2cMekjfigUTJidO9jWZgkBSrlc3FfOrrfBXHzTIs71cC_SicG0vNVSCX-dTFSv69nwl41EDk3qZBsTwdmXuVIdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=bnGjNB1xPPRJjaAuyXiic92Cagr-VDtkXb4g--C-uB4Uqn7KHPnPjc8PAcivUxDe0Od8qtpcsGZj9nHaHqA7hXDxxDzDk2v3WGRVV91Cyqf4r0U07hiiI4eIACPF624aP-M1yXXzXfjNz78GEJ36QObbw7zgbrjfOvLsO6OaX_NJyj0pujOUcJvrUBtAyoSiup3rl_RJYZSGzpyYgtpeoRbqtIwdLQ1RCu9U12MtSRwlH0-Df3YX6xo6z64c6v_kmfLbbLMTqDomFrnNdIJzOlN_6csEvFkDpX2yQjNAH2YofzT9mvaHcR7K6gBn2c69hfyegD_sVfo75uYM3Xo7zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=bnGjNB1xPPRJjaAuyXiic92Cagr-VDtkXb4g--C-uB4Uqn7KHPnPjc8PAcivUxDe0Od8qtpcsGZj9nHaHqA7hXDxxDzDk2v3WGRVV91Cyqf4r0U07hiiI4eIACPF624aP-M1yXXzXfjNz78GEJ36QObbw7zgbrjfOvLsO6OaX_NJyj0pujOUcJvrUBtAyoSiup3rl_RJYZSGzpyYgtpeoRbqtIwdLQ1RCu9U12MtSRwlH0-Df3YX6xo6z64c6v_kmfLbbLMTqDomFrnNdIJzOlN_6csEvFkDpX2yQjNAH2YofzT9mvaHcR7K6gBn2c69hfyegD_sVfo75uYM3Xo7zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYphNHR5lz_Jlndk43RNWTDaCRmIBnm9giHH_5hIqkXlknNHEsiLv2Q5Ffoewm5KFt3CHdyTpm-iun1PZTisf-OgAm3etK3mm6aEh9ZVDNXYxCsTp1G2w1nLk9UHhn3IT4gtzg8l5YoPHCK11E9fSJmNpln8kJ9UmOIJs_BIlZ7nUqbykeKP70fOjdxRtoRxYrdpUJ5ogP4N5nGeiZMsNjKL7YGJ4XMAQlS5ZWnXzPuopTml6VktribvMl2dCVULBIay9c_WfOjoH9nDrpIYtaHVicSerBx6Kjnzd18_4c7yM0AOP8kDaka1D3s4FOc4ITcfCNaLu3-kWmySDgI5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYBlx_bqGIpk0Sbz5q9f_8R-LE2p5HAf5zhfhQ02-oV7oPPoSKJMLvc8X2j1pXOB6NLe0dy4TAwWE5Rl_gLowJW7M-ZpchGxSYkMnWdFGVOfof4uxLIKIQbJ5ddC0CCUzonsDY9icZdQ9vV4m1qi01mJBTCT0EWCQXlHOCrx0N95D3R1BIeQ_2jxr2VhCDWuVoc50dOqmwYtojE9kk5N41Fs4eK1qGj7-ovLRvPALCMcYPo4WkATynrbNcKkt7nrzOJNGhfzTLGdSjG_CkPnXnUjgG29TkP3erLpaj4nmHnfvpHnDUOWmwKlnB0GlzbEyrpP66dcBJTFknuO8tPNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=u3Wpq3Gyw8-qVffCmrQknT-M1nVrv5TRU5JaX9JHIWcMC7c30s8m3gwMj8nvcLv4iHqVOTc2szmhcGMq1e93ChiED82vh51fDPtrylWK4fixj-i1X2tih46MCtYERwTxFHnxyT_pML9M7qzVa7HmozxLfkQ3Q1Gq9SdF9iKouQjtAhO_3ZdBST6kSnLAKSCySSacdnhnsnvveb6EXy2lQdUQdBrvWJQgA_JcjGDbiyA9uPMPEyFbWmB0bJUV2YhhkPIGNGPRTgNk7ODcDuulvMgudXvHFU0P5YEcIsQx4yLbic551WUXTuTp_9M9pmwHFDR3wolexVuejIDbpiuraw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=u3Wpq3Gyw8-qVffCmrQknT-M1nVrv5TRU5JaX9JHIWcMC7c30s8m3gwMj8nvcLv4iHqVOTc2szmhcGMq1e93ChiED82vh51fDPtrylWK4fixj-i1X2tih46MCtYERwTxFHnxyT_pML9M7qzVa7HmozxLfkQ3Q1Gq9SdF9iKouQjtAhO_3ZdBST6kSnLAKSCySSacdnhnsnvveb6EXy2lQdUQdBrvWJQgA_JcjGDbiyA9uPMPEyFbWmB0bJUV2YhhkPIGNGPRTgNk7ODcDuulvMgudXvHFU0P5YEcIsQx4yLbic551WUXTuTp_9M9pmwHFDR3wolexVuejIDbpiuraw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=JsflqKBxs_9Ow9VpOhbzk11nE1BKzzRZtIkqFsQcBGES3v-b4ODcUV8gwpwOPDsRbP4sjZQlQvla_zoWEhfcgLaWNYSBGyvornVPmTK1JWAfHtjlC8eE6GTCDdDAIDlElfO-OJY3ZXXRvTDxcus7t4HkIb6csL-LQM9ZMqZfpdAl5D__k8ALY25lLJ7ImiF3zOHCX0-g0rKIr6hi9qzjem7FBf8RRT2f3h9aqmVxtq_EznayJoUZ68s46jf9QSdrltEfMwn-N9p4vnXNGd3X3EI6IAb_XQpxGKQz8aADbpn0oIKd9fRYjwPnbkR9mVHBlgOo1Vx7u50THyMhWitjXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=JsflqKBxs_9Ow9VpOhbzk11nE1BKzzRZtIkqFsQcBGES3v-b4ODcUV8gwpwOPDsRbP4sjZQlQvla_zoWEhfcgLaWNYSBGyvornVPmTK1JWAfHtjlC8eE6GTCDdDAIDlElfO-OJY3ZXXRvTDxcus7t4HkIb6csL-LQM9ZMqZfpdAl5D__k8ALY25lLJ7ImiF3zOHCX0-g0rKIr6hi9qzjem7FBf8RRT2f3h9aqmVxtq_EznayJoUZ68s46jf9QSdrltEfMwn-N9p4vnXNGd3X3EI6IAb_XQpxGKQz8aADbpn0oIKd9fRYjwPnbkR9mVHBlgOo1Vx7u50THyMhWitjXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivyONaNETgIs3IKg1PON-oqaI8vg3-mcZ2M3LK6fczzF1yec3rg0tl7sfMP3q5qwuiLLNaDeViEgoJoqxG5K3OFqQYC9iHBudo0Xk2eepJFAR1fK7eakaSrDAq3yG-dFEGTTUBXcw9nd6eKAuCK_fcQJCP3CcFIa-QYNbJDahlcX8jpR3gm1n-mTLZankAjOGW-VpQTBmdbjxlLxRPJ8lxn7xsuwIbpLWDrEr_igvzec4qOxzlo7u1ISh3v4UG92lfoQ-Gl647cpWbHxnDSY2K4BvA7qgHLofndMlGNd6DToqOzw2t9fI2nw6ThqX4BAd1CbfKMK98QqHtA1nMjBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TunPyqLw0TYv8bwk6P8E-5Fd1xMAk2PZmZ_6KA3Axuiy3E119EyE8_btOjY_aEB8LuORBWgLqmvdNNVeXU0Bu40v0EUplOFUdaCVtumxYds0pwYw-r4_mjMSQIHcSxF2sCFAyhCvsU2rLahvab3NSuaRfuBGFzcfWf382gVuW1rKbHbheveGxqB6sC3cnmKpmdYJlJ6GThCYHXGP1v9sL9Mc5ahVnXXSxVRufPblUvnADP5Ez-NZ-STae0BX73rXRj9JqflSGw-xaTRt6ni2FGRqpPX-rRMEevcI9XZBxU8abRRdpDCPoTAbX2m7eutVoZWzt2T4nmzQ9w5A-RzGYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBswRP0LWmz37FaSY4yYXvwd5CocOe5QJv9ciVGvXqWwajNPpxM4HXdwFP4ARAUyY4eJ4ZBpTHzIeyh-EEAQtuRAAECez5OCBm2jHu1cVB5eEa1954U0QpWgBFJP_K9KlnvTUzsdu9WfZq_8k3rb0d5G1OV_jaohGBsFwH162_Rx6Nkhtulj1GJ8oVBUK_7AVbcve4p2UlCtd3qQNydgcMG2VuyXH96nFlaVHXbu9qX1aOffBtAEXt55FDBjnZB-07EqL4138Gq_j1I-vn3CqbPGbre4x9b8Zuz2gX6vmDB9NXgwLaY69rs1S04vL0DDVmKuwxwnJCV4DwGmAksKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmzfLme0mBOwB-RwVLCl9YTNWW9W8niWC7joJkufH8s8cRgvj9ahSn5RUNW-IGJX2b4NqX4TMrqx64R44hY-nk4g3TJ0tW-F8sBMrxR8XjrDOPC67r8EfcY-KkRVzK9MyCrrxFT9hOsh36BvhrlKzIvrtSR2bWiKikj-l5S9O7z-jB3NkdrNHLdaf8Dn4UqOIUq8Y4Ei8RwPsHcvYNkcwwm3PnAdeAlHvQmhXfyFP-QT87JvnkBZkIGBfk8tiQ8I5vsdPsetzqizzMJJk8uCmO2a_if5gyyHVVizWlrnDO9IprtYDo3q_zk2GdSTo9II-t-RNgf1tvNugqjAlQ126g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCsSRVjW6tda01SjWIJmTyou26XcYDH1cf4NTHNAR7oyMOPjxDqCgcbcRI5dXqa3Xqk7q5VnLZjq3GBOA_kQgXLsR07G3eSsMEHKk93GekxxcI2LTiLvXkXRzCY0wFW2_RR9-Z6Hyvi_6I6u52SH7-_j_2Qq-WGAaavOhV65pVV_DX8_cH5dvzGNg2ClhOQWd0s_HS4Y0S4HXtGalldZjBIFP6UvaAfp69XtTqObWknyHt9jpm2zxJ2EZeK4MF2B8M9Be3BR8z0mjU5PyJ_8FnXNopA-Rk6QCAeEvl0fdOcue1c1fxsh1fpeCtY1htKmCVTeL3jHbCKTyGzB0PE_Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0edx79c_kcw95okUSRAk3eONuGK7SIrefByLB9qoARULHrIThRcggRmdeqev5aXXYUua0GjxqMz5_R0_0X7cv_UThxuQkm175P5YogZE48rJ2jh1bCIGwAe73JDqSZ8diQFPOxhlKn8GVTZci9mswCWRHQvit41kw8mQ0cqmJQ6j77EdhBM_oh1KdhisswTKxFwTLTgi9aoHyTwbLvUuWt56cHJyrk29jnb_Fkdiyke4WS2ih2yRNj7gYQpukygAtyojTwVOUKDaF7DVuO15Vu6z3NG3-tJvd2koEcFCGhdqIaUbl55V7QFR2uUBVFbPu2Ke42_MrnnYmByjh_6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=ii0BsOC4iOlJOF0g0KR-7LQV07sVtwPkZiNl4pCf5J4Oa8F80eRnuwHD-tHqIngLNXE09WWaSOedQeJF9wiuojq3ui8fMXI3LOTvne9SJG0DwXsZOEGVcnP-1P_SBNVdwkmZhJramNCtrhJWRUA1CKrI9KD2jajEuZpREcamSHV766wrEVuoBTwWm2EYFJ6ir7fzrxjd7IvqiwnJq3ja2pozH1lXlivHoDipBeZCSezTNCsx5pDfpjV57_Mb-IKFZLkMYZRPCwSBUwVRl5AnSq5HXpUIDDzE4SonSr0sFVB5APOFU-ZCGEpAH0ltL2siv0_WDXM19D9FKuIHzRQH_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=ii0BsOC4iOlJOF0g0KR-7LQV07sVtwPkZiNl4pCf5J4Oa8F80eRnuwHD-tHqIngLNXE09WWaSOedQeJF9wiuojq3ui8fMXI3LOTvne9SJG0DwXsZOEGVcnP-1P_SBNVdwkmZhJramNCtrhJWRUA1CKrI9KD2jajEuZpREcamSHV766wrEVuoBTwWm2EYFJ6ir7fzrxjd7IvqiwnJq3ja2pozH1lXlivHoDipBeZCSezTNCsx5pDfpjV57_Mb-IKFZLkMYZRPCwSBUwVRl5AnSq5HXpUIDDzE4SonSr0sFVB5APOFU-ZCGEpAH0ltL2siv0_WDXM19D9FKuIHzRQH_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=GgzwyecIyuTTJpXf6aym7ZoM12cV13IbInUb_abZXg3Nlzur3GbytRsnBzT2vpUx26p5jrpIemysAZgTzJVkDutntQoXMnqKytO-KoXRE-x2hoawQ6rAVxWxGdSOb31GD3OiI3gSd9Y4rhDdzHdBp0Z-zDTAxxEachzFkmJDZEx90WRfbUM-XVQaspBHQMUsQIBx63yzcIb5-5PQ8Aj5ec1CLWP2vWSbjOdY_lukMdit-rtDNJSEXSHfDheml1aEovCp-QRznh1zpLykk5tOGVWK2Hat7SCt9wALXUV1mStUcFV2F8GBgIlmf8WDxCkZcVqmawzKN8z6YKIcVvZ-jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=GgzwyecIyuTTJpXf6aym7ZoM12cV13IbInUb_abZXg3Nlzur3GbytRsnBzT2vpUx26p5jrpIemysAZgTzJVkDutntQoXMnqKytO-KoXRE-x2hoawQ6rAVxWxGdSOb31GD3OiI3gSd9Y4rhDdzHdBp0Z-zDTAxxEachzFkmJDZEx90WRfbUM-XVQaspBHQMUsQIBx63yzcIb5-5PQ8Aj5ec1CLWP2vWSbjOdY_lukMdit-rtDNJSEXSHfDheml1aEovCp-QRznh1zpLykk5tOGVWK2Hat7SCt9wALXUV1mStUcFV2F8GBgIlmf8WDxCkZcVqmawzKN8z6YKIcVvZ-jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=VfSbJuNsuM1FYLSOa-W4583UETJoL_OJCME9zn7v1tZX6VFVnKheIHg4O_rrs7RPdDdQsVEp_UwmdGfOh0Ex2AL8Hun90PFj1UkfhEDGLdyF5w28TsCv3n_M_cHiSQG6TbSfnQQTcDTALsLHGClij1jAKSKr7va3uA6zBAyJjUm1BNMGgknhImt7Xm2p7DMdf9eZQhBJQqNnN0KYkqhGbGxhvbDeqtLP6xCfiEYtf9GfpnzG8xqUUR5Qh3J-EKBF8NA3qbm9uDuhb9MoUAzhDwHITWf3hS7WTb14iqGlfyl0Mjva7opEYFG5DbReg9GRr-tmKgA6AanGbQ_SQvqwAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=VfSbJuNsuM1FYLSOa-W4583UETJoL_OJCME9zn7v1tZX6VFVnKheIHg4O_rrs7RPdDdQsVEp_UwmdGfOh0Ex2AL8Hun90PFj1UkfhEDGLdyF5w28TsCv3n_M_cHiSQG6TbSfnQQTcDTALsLHGClij1jAKSKr7va3uA6zBAyJjUm1BNMGgknhImt7Xm2p7DMdf9eZQhBJQqNnN0KYkqhGbGxhvbDeqtLP6xCfiEYtf9GfpnzG8xqUUR5Qh3J-EKBF8NA3qbm9uDuhb9MoUAzhDwHITWf3hS7WTb14iqGlfyl0Mjva7opEYFG5DbReg9GRr-tmKgA6AanGbQ_SQvqwAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=h93r9GLtzupNRPlPoHYuLDwEKmcLy8ALthnadFCWM3GdelZJzr24jLTgrJiQ2awBe1_E5mwy4X2Gt3kSzg45yQIc2BoFYSf0jucSDpPRxFTP9F_oMvRR0yxpYi6xt0FT68toghsSocVHmqBp2xGg6tqtT7DqugP97RMvYhVaiaorpC_2Q9CQCVEmlji2ajzHuwp6N5smZ_GmNr9jEQQT98xNsJjFRmHLXBd776CcwWWsQ-joxzjNERP24ElIhcrtbGJvSfstrocbvv4kWhhcb1093BVIXoZK97ye6iLOBupQUT-z8r5e0sQDlCh9NxEaWltbvrjtKICOmrzfqgF8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=h93r9GLtzupNRPlPoHYuLDwEKmcLy8ALthnadFCWM3GdelZJzr24jLTgrJiQ2awBe1_E5mwy4X2Gt3kSzg45yQIc2BoFYSf0jucSDpPRxFTP9F_oMvRR0yxpYi6xt0FT68toghsSocVHmqBp2xGg6tqtT7DqugP97RMvYhVaiaorpC_2Q9CQCVEmlji2ajzHuwp6N5smZ_GmNr9jEQQT98xNsJjFRmHLXBd776CcwWWsQ-joxzjNERP24ElIhcrtbGJvSfstrocbvv4kWhhcb1093BVIXoZK97ye6iLOBupQUT-z8r5e0sQDlCh9NxEaWltbvrjtKICOmrzfqgF8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=jAj9YulEvoyH9lp_zPLsauHlOI9JfH_n3itrwKjosDLseGY4Wsw2FHP7uh5If7WbRayU4xRNoOpAHqOv9-yr_NSxQyls4-zh-zQeP2Fs44r6Ku6F-mc5G1v7wmlDI31KnWqf_785-r82BCHBIasDUOerFxny0cil5oQgHZI_OClqfOdRZv8XEGwWHRFRXjnpmOEEddAeHAYJtL5HA2MvxeVUDbfBEshFrmROzUReukD-zN3tFV1G48LkodOsDY67PXKxgJlKclTvKQfgC3fyNQ-_QQJWNt6UJsLaB4qvQLSmkKmBb76CdAhTLkqtCDYDe6-TcpEu4cwDIgOGGbUuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=jAj9YulEvoyH9lp_zPLsauHlOI9JfH_n3itrwKjosDLseGY4Wsw2FHP7uh5If7WbRayU4xRNoOpAHqOv9-yr_NSxQyls4-zh-zQeP2Fs44r6Ku6F-mc5G1v7wmlDI31KnWqf_785-r82BCHBIasDUOerFxny0cil5oQgHZI_OClqfOdRZv8XEGwWHRFRXjnpmOEEddAeHAYJtL5HA2MvxeVUDbfBEshFrmROzUReukD-zN3tFV1G48LkodOsDY67PXKxgJlKclTvKQfgC3fyNQ-_QQJWNt6UJsLaB4qvQLSmkKmBb76CdAhTLkqtCDYDe6-TcpEu4cwDIgOGGbUuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=O_ZLtDL9gFP2-Qap-4laTa9Qy_mFqtrAdxhYzDcC_5vyjvQqHY2RT5XEtrR8Zo1Q-_tubRTIE0GAJUlO-t5lRojNojdZatq4zbUAUyP8Z-CWcz7tjzcO1UJlSpHC6dPuNLcgGCULQ-7JK7CKN3gYjhxHgsY8SZrLjO7VNlvyI2IbG8W81dIjdo9Tixo49-eUG3D4yDi8nsd5x0bTvtYUT_SOyL6_xhHliyBP2oqylQgHacGbxo9sLm94jznlsPDe-luwwxY55jTu3TqmTzS8ZjqRIVNNaOIQVzAgLY9ntXeDeMhYcglh2OYtpRm9vMWJsMT_EuHjC5SKDS8DKkOeMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=O_ZLtDL9gFP2-Qap-4laTa9Qy_mFqtrAdxhYzDcC_5vyjvQqHY2RT5XEtrR8Zo1Q-_tubRTIE0GAJUlO-t5lRojNojdZatq4zbUAUyP8Z-CWcz7tjzcO1UJlSpHC6dPuNLcgGCULQ-7JK7CKN3gYjhxHgsY8SZrLjO7VNlvyI2IbG8W81dIjdo9Tixo49-eUG3D4yDi8nsd5x0bTvtYUT_SOyL6_xhHliyBP2oqylQgHacGbxo9sLm94jznlsPDe-luwwxY55jTu3TqmTzS8ZjqRIVNNaOIQVzAgLY9ntXeDeMhYcglh2OYtpRm9vMWJsMT_EuHjC5SKDS8DKkOeMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSQsISQjWmH-fPB2WTHFSjvICcO-NdBCgK8IVwx-47F3SraMk2FQbvuU0LWWQP2WLDDJVRVTy6bfA0ESFKC7mxp39rYDh9Xujz0q_IxjaYsjdF3E0uYH3cuEEkCgigRpeIg0ooBA3jqwNTV8fQQ7fdrEkWTyQHO6IwmVl8rNhMwXi6F8iWsXojjakhGlUX0kJq06N9eUO-TunzmzL3sY4CpHCUoQzbhJHPpAyLdeVjfxGZDTMob-ALp3bTDHRam-sXRd_qYJLjy56O-CZRUN_RyNqaSX1M-_ytYEaFd9WRTOC5yD9_tl0LQPH4KCPgPszHUoi8z1OysmLfkOa3JFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=TiJy7M7-41M5bpuLB9Eo085fhfPaPYRWdkWUsCtsVpTcs2mbsnT4dV8e6lpJWF3_M6h9JS-yFWi1ihWym9qmkZPsbghIN7Fpm7zoqKfbvVD7UmFn7wqQCjYHShJguS3wa0kEn3e0Snd8HAblUuCeMEactVdeEsMAuNWClDPhMB7NPlnhomG3y-PzHBboJJdicBMz0tAAQ0kJHnllgWmGhykSQFCxgtYRwqClfVllPJOUTzM0J5g6tzHEbBPP1U9A2mU2VGxU4FGX8Xapcz_6LV_oswHLH3ALkQPma-IgLUImDxlG8VfdArO8mk29-uGcQJ2cTJWgPxwsQqSQAYON8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=TiJy7M7-41M5bpuLB9Eo085fhfPaPYRWdkWUsCtsVpTcs2mbsnT4dV8e6lpJWF3_M6h9JS-yFWi1ihWym9qmkZPsbghIN7Fpm7zoqKfbvVD7UmFn7wqQCjYHShJguS3wa0kEn3e0Snd8HAblUuCeMEactVdeEsMAuNWClDPhMB7NPlnhomG3y-PzHBboJJdicBMz0tAAQ0kJHnllgWmGhykSQFCxgtYRwqClfVllPJOUTzM0J5g6tzHEbBPP1U9A2mU2VGxU4FGX8Xapcz_6LV_oswHLH3ALkQPma-IgLUImDxlG8VfdArO8mk29-uGcQJ2cTJWgPxwsQqSQAYON8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=Gp9IZsZqq_3aRz4A9TyhmnbfzeoQULlIyLd4rR4rxOInTjt8yrrOXlyZ9xXYzXGgEC6AG4uWQnx6GObx3XhyYHcHJqxIYHDcdBRPgZDt4er7c2xu0CIKeJdQ-v8cOV9lz1Xi_v4uia2iAQNypUMr_TQ9_aqHBYYjuCWbz2w5T2DwV34X13XhAWgkdrZ0OniTsSTMtKXIostjgo3MMX2lSxnoo0-Jy3NXdQNjZVRIk_wynYVDMGUeX8orsHPeC_iB15ZqaQSmriQKYyM88ElHaukRxbmwuvjRACA0CnZU9ncd5O_sx0DNfMZ4f1uyunJjDX2btyuYX4wDTl1TMRnk8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=Gp9IZsZqq_3aRz4A9TyhmnbfzeoQULlIyLd4rR4rxOInTjt8yrrOXlyZ9xXYzXGgEC6AG4uWQnx6GObx3XhyYHcHJqxIYHDcdBRPgZDt4er7c2xu0CIKeJdQ-v8cOV9lz1Xi_v4uia2iAQNypUMr_TQ9_aqHBYYjuCWbz2w5T2DwV34X13XhAWgkdrZ0OniTsSTMtKXIostjgo3MMX2lSxnoo0-Jy3NXdQNjZVRIk_wynYVDMGUeX8orsHPeC_iB15ZqaQSmriQKYyM88ElHaukRxbmwuvjRACA0CnZU9ncd5O_sx0DNfMZ4f1uyunJjDX2btyuYX4wDTl1TMRnk8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idPriCfpZgkcK-sHjrtnzOybfo67fk1xuWhWrejuM6zpGm1Urfr9TZP50bssbSNbcI0pXwyueOTm1mnRTFbgc-65Lag-UOuWAZ3woMNMu4-qmc8TXAlgVOREGSxmHzmtCZFiz-Nx-EHSFSz3XKAeyaaRgemO3lK6vn958kVUNtiOdTiQrPp-uk8DLYem6pyK-Bmr2D4n4a_Ri3wzIBRmWurA47D-d-BVXQuLC5a43nfWpD5M0-gU7Mc6wQbBuY5I1gIaVeY6CyRzj7iJA0pNaUaJxxZRi47BW0FJn5akHYCKsIvP6ehOcHU99RMaIP27GiHVemKx1YHmt49iWYz5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osnr9iE7J3WK-OsTt_aNFq_qbbEgCPApOyFLlMthdyL-xOMKmQIlIPb8vG1ZePjaajcbqywvOsXlxLW_bHAUimP-b_ioyoUWLkEg7939MVrZytSiHAUJfN3f4-he7Qt2iiPWbORl9FozY5Cb8PjnY4xjOxW0tfcpMEplVKtIxM_RtJ0Rf7ENWuuva5RzxkSi_kp7saF53HgCn0aAgsdUv2eExF2oq2CtKTNmW_GvA0UfjGis129w43wE2w1wDvAzJTPVry4HeTUGz2pl8QPp61gc1QzA-pVTY6vnyzITmQ1voTXiOIR_7iB_MJnMly1KNuDnp1RHUUR_sDjkyxzMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTxX669_H3EIXt3dVAu3ddq1_mAOA0GhwCZawa59_qR_kqdd_92resY3psssskqdrOu5olnG_VWQmjUNsHZJ9JSdMLv6zWjI2vzlErR6sT_nJLaHO40I1rk9uupHepgddC3BRi-s6QA8sI_ZIlOSqnvLpzqTDCABpHzPJexGjvhLepsvm8sTiQWwy271chlmXhDuRvrUYQxH6Dbx09grmAzdUgaqZiiO-WbhUAzLg1f3bwm8-aUd-5gARdRJTq5HYLEEZ7odGte-Wz5zGnnwH6p8hsve4WhMsoOdbThvE4hdcBmyRzmYbdilhcb6EqjbtVqWFzPJfojbOpkCUKbz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0maIYQdVRLRqfDmFP96yY5BpwmPjPRhc5Z83LR9HxV5wzjRbIuMpHTCwX7fwEdjSB1clXBQtLoNawKktIb06JC8JeEAf0LnILROcqSZMVee1iLoA23cOcm7H7NyDGT6aqhOLfuzuUBPokDzHZDdhiWgTamnu3GzG8n9WEJxOnq4x-6JTm2XERaPAPBMXBGIW5GdPsGJ0GOjS4WGcUNSeeePXNOzsQZC8n3YjsdWnmDcntz-MxGQbHqylYAWxqCzsByNgReDhW2axdL8PHYKoexi2KZT6Xz2QMKFBSCNQ_ZXLhY6B4T7JkPi2Wqzn8APtRSjDcrSt1ldFt3M2zAYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dupD30apnpFVZuNA2Ib9m5FHLcnTaR3Mp2LGHejYVON62gf-vLlww80QBqkG0PlPWvFgNgeUisMvo6KryYapmtWt_F4RO9PxFppC0vkc1fVqU79vCIBMoQKMixgfsBusJqRLQK0Etsq0jBPhmonxCaXjbyyMFs9qQEsDLzwoOlJjl7iZDWmTfx2p59bU1GD2AYlszQsrc0y1Q4JxsVKnU_juLvIvshBoVkY52_DX78TF1XPkPzLKTAYnT7h-DcxAV9KQLJoDkkga4cK35hoNuXbWyNJhgjXv2xZzRc4xL7i_fOk3jvqUsVVgihcYL0XbcEiyBcZr_m7FliQq71WgQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyrQ5ljiPAl9Mm9tKFav0S9QNULzIIMU6PcHiv8Y5r3dwApUb7lhOJSxQWzVDPu0qKv0b0IDZIblvzqnymG8Od7EnuQDSknmUo_UL3lAcnFC73W_uYhKP3mjw42rpMrT4dr-VsM4Gs9AtK3i1mbWYVcMiyslfJtjD-FosBRbQE-gkghxk-cvgBfGRnTfadrCVq4Zu6SEeLPWPEpQV_yYwef7naSTOlupaUqZcnOFAtH1kCeHn_UMnYKo6TJDZ88NsuVEuE_nW-6ydGzKmnuZcADVtwY-WnVOzmN33Lf7jol5SI7sJhDzfKE7cHqQw8r4vgDQGwA_5uSE6qyQvzf5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DyF2iHesCq6kuExu1EZ3ailLtPI6URMvXr8y-GPoqrdZHTrVuDA19vTY9MEUyGeyaoR7MwZ3hvYxkWPj39C_1rNlVv59cj_MpHBbeAwhnaA5cvdhnx8OaV7YHDW0wRBaqd-ybyGsMPBmkMNHzi7kZipS2oDevDL43yJxB5FcdV-Ofv3MuGeZMKzWCwfdgBot5feYglk1QSXMQMfOrjmLR_MLtkZwXr8KseNDEsysHZbP0aEkmjmJxJCEPyQu3qXfG4P7OP4EXcOVgqSDjKCiQY-YtF28ayG5iiaGRd58cuKG0I4bRRreXgtFTeL2Q8HiIYYAJcBsArXHJ_xgQII5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVtMxvKvh_x0SckaR_Cr3FlycSj3cQo2686lVQ-NZbx_pf5mVmYqKr7rkksUqSCLHgo7G7fARgSfuvVZ-gtPc-z0x1j4zjX7xndFCVfu3HAaj9EIQhpH96PHheaUtQwnlB_Rdfe3LcO3f44u1m5TX_OeZ507TVJNKT20r4vO_qjvqJuQQcHsvoal557NeFUJ49U73Alsgh5X0iaXCd4gEG1Q8dM-NEah4wVZZ1z9M3cxOiQFRdLBmOGCAErOpuqLh_q_bqPsN8UjdJUo9JzPlIfPbZRDk1ccAnDzji6rhJMTA8f9FEE9DN-uA1xRfU8b4mCqW4hOUnBO2bEfPzKhsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy78wUD7suDVrFZoV-9RmsdzxNCd5EXYKnmAryspiohuSA6ZQm1CXb1gFzTIicu1nJSG30IBkjVn-ZxUuxU_3QOZ5R84qH_EI-zGMNw1P24LUceoU6f85DMv89yFSiosW1zr8d7VUQNFiv10h7PFuQv9IzZZpYc6J7HU_oj77b_dPs7Jv841vdLctZRdfHN9QSLcp4Ol0x8ru2mx7menRbuZcHRGkgD4xXXk7lZQscWcLZ-gtqul8oAC6RFLZ2yKALKdAjb7ULf8jBc3O2xZ-C6OY-0cjSJ3s1HNIFpQwg1gZYrgjA_dxMxSHUTErkngO6r0ei_XOHvKwlj4E1mOMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8ajUp7r80tuo8goLtt1mprSCajx9EcwqaBwqHyBfHhcGI60K7255xtNiOMkZoJkviRTAxLEGFw5i6a7CfzmBGvqkkoRETGvIjx-ArT-gdSFSG_WK-eLiWvA7aljOsec8wLqCSrp7mmluWs8xLm5i32oXYUB2bQahfe7yIyzJkcFZJsMxcVG1EtcnfLNHH4Z5GJ_RdXm3cov2A797smndLLs3HgLTw_F-qrKXps3hme5gEgQkHt5RPOh2JEnRpMzwfMDgb-851WOfTgcx2OfwotLfruE7xRvagQCGv-6QadaB159VPxwADQenip1n1eDfy3n46zTYM_58JD3vXgAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYC4IJQoQzvA7MlYKfFsgjgi7ZjTIxfmRhn3UwUcRshD2R1TynyoaJ5AmGcvpaXg7gMe30JxBKVB--lDa8O0Lzieer21bawHQD4QT8Gg8Z8FZBP1F8i2N6-cbwYX-o-SeTtq0pepHJVnPHcyF1ppuAaEFALQpnkKIIm6JpVu-VMm57YZ6WFQNbCbBTNCHoxcq4R8eGsh7aVHkPtFMOjeDsmOGre4sEtiGzo1L5Xm_dBgc96sOysce-dafK5BribsXHzHolAAayQ4U9pjM--WWpgRUTCwzwqj36inlBv6cPBiSvgU-xHxhI1pKvl_nKN9dIJ6dbhQ-OOn1dWx7lK3hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EguokYsv5T32bZsPgmatHobmQvNUragLhva5bnIICA6tJCrhB2er34QkN2yGMfjPF9o8UKtHKr5gGw47Hl7izHzVum11EFjehSK8p-wakOFBdIbIOgBzNlbWG2WeeeB57_9oSmJMJKMjZRlRQ9mOHCYZS68ACoeG2wLVo7rXnYDU9GNPOVR56FRrU5eGVuhxxOY4K0yuGaAVEj7KOp8hbbyxMF4xxriuDr9SN4038i_g6cRXYN0HogCl_6oV9JK4kGaA8ZmZbauCZ6ZHGvs57s4HkJOxckN0NnuxEYL41lYxktL0GatQVdc_UZqllBDEL2kfnMTaVyxQ1fjDydujig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=pnG0PIdtnDA5fKGUJ7rkGkXpqoG8_S3Y4kU5IUYlWcYU0iTP7NFQUj4FRWLLwlbP1Au--bBUBJmt8Qj_iTmU1dgoB5olhWJbo7EWIX2nftZgtP-1T91XWlt3d2-6CT2SXbIzpkoiIBMTRRC07sIPejveR0NfMYjycnmu3M_GxHacmYofZRc6wDGLLdfyOSxB5zZIh4QjW7hNz6C2monHFUuhZF1UINk2YdTY_xgAuMLpcKtWacl1NTbwgejhlFfFb5sNoibGOtH115tRi3yqF7soy4vUAkKDVP6EvMWUe9KOoLi84i0Qrvbt9m_0UxwMba8VLdHTp2rYGiEfyRRkWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=pnG0PIdtnDA5fKGUJ7rkGkXpqoG8_S3Y4kU5IUYlWcYU0iTP7NFQUj4FRWLLwlbP1Au--bBUBJmt8Qj_iTmU1dgoB5olhWJbo7EWIX2nftZgtP-1T91XWlt3d2-6CT2SXbIzpkoiIBMTRRC07sIPejveR0NfMYjycnmu3M_GxHacmYofZRc6wDGLLdfyOSxB5zZIh4QjW7hNz6C2monHFUuhZF1UINk2YdTY_xgAuMLpcKtWacl1NTbwgejhlFfFb5sNoibGOtH115tRi3yqF7soy4vUAkKDVP6EvMWUe9KOoLi84i0Qrvbt9m_0UxwMba8VLdHTp2rYGiEfyRRkWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=mF38g9A2nOtrr7hDhLIUi2YhRwFJcV0niDRmA0P4W5PskTwwfCWdKQfzEqt0JpAkJnEOuS8nlP4oRBHG84yFdBD5qy0V5RPHHF06PDaY6Rhs5NR87VUYEb_W6cUzw3LSBqe4OaqbJw8CHpWI9QgRlxiY95lBwTMhONRF4gDpTv4W-wwhHwGTS8aJdUpb_dTbOh7AJ-uQhZ7sl-OUlBVHv9eZ3fkCGNHFN50zu6dDdOyiKy0p5R8Y5PCkHJTcdMOrZ1TbiKIqCCMO5NmHFDzLWmovS4OpBoYoIgTYisf4i8gAbolfqeImTW16JO4ySNn5V_VcmKVyLLntn2wa41ewtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=mF38g9A2nOtrr7hDhLIUi2YhRwFJcV0niDRmA0P4W5PskTwwfCWdKQfzEqt0JpAkJnEOuS8nlP4oRBHG84yFdBD5qy0V5RPHHF06PDaY6Rhs5NR87VUYEb_W6cUzw3LSBqe4OaqbJw8CHpWI9QgRlxiY95lBwTMhONRF4gDpTv4W-wwhHwGTS8aJdUpb_dTbOh7AJ-uQhZ7sl-OUlBVHv9eZ3fkCGNHFN50zu6dDdOyiKy0p5R8Y5PCkHJTcdMOrZ1TbiKIqCCMO5NmHFDzLWmovS4OpBoYoIgTYisf4i8gAbolfqeImTW16JO4ySNn5V_VcmKVyLLntn2wa41ewtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=vfhgkF2L7A2E6jOTcalLuQF3CA5qH1MTiKJ2x81QvncGxNzsxHfgftmILyuIbv4c2DygoS1CGZwa6gS-ItJu4nYaiELBahj-gXBvfFyb94tFteyxsKl1KwXjgDXI0-0nkJf-mGJbyJwUZ-RnO3ZjPX2Npet5PebDoLl54WPANKfhqmGVXnlTlNdOqBGCOR3Vp4j-FfessxDDeFmuRddcwmQRwIftZUk44J55V8Pq0_7pKH6a4xIoNtTxdDY-jgn3aC90TA-n-h1xEYCTm2jidVn09T7NVMPRMIE6hrVtdEpq75pNTcFeexjD3oi73PVZHPCwocxqvFUZ_BFpS_dGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=vfhgkF2L7A2E6jOTcalLuQF3CA5qH1MTiKJ2x81QvncGxNzsxHfgftmILyuIbv4c2DygoS1CGZwa6gS-ItJu4nYaiELBahj-gXBvfFyb94tFteyxsKl1KwXjgDXI0-0nkJf-mGJbyJwUZ-RnO3ZjPX2Npet5PebDoLl54WPANKfhqmGVXnlTlNdOqBGCOR3Vp4j-FfessxDDeFmuRddcwmQRwIftZUk44J55V8Pq0_7pKH6a4xIoNtTxdDY-jgn3aC90TA-n-h1xEYCTm2jidVn09T7NVMPRMIE6hrVtdEpq75pNTcFeexjD3oi73PVZHPCwocxqvFUZ_BFpS_dGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Uckoayl6ZvwN7gSXvQYb2QyIYlhEcOx7wawDcTOq1nHA3HtxDlMGr4v7c4ctO_chJFxb5kE70CEj0MbS55sYAN9VbSSCInk4Sr0cskSQSpWb2IA8p3OVAfevzaUXSgj_njT4D7XWUGX8BKsxBlPRsjjNjubghEnFz9x7t_jpIxf5nMu4aeviaDizIXVvCHflWu2y05tMJWXSb_2HqalxMmJ_0xpZOy76yqLCwFc-M4sX4b413jTSIBLtjf30xUFWyDYPjTXf1u8kAZW4_HMhdqqNqqgWbiB8lJD7EF598dgPeN4v1P7bTmxqL9rKYE8Z-81t72l3DAVSRPFF0xhxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Uckoayl6ZvwN7gSXvQYb2QyIYlhEcOx7wawDcTOq1nHA3HtxDlMGr4v7c4ctO_chJFxb5kE70CEj0MbS55sYAN9VbSSCInk4Sr0cskSQSpWb2IA8p3OVAfevzaUXSgj_njT4D7XWUGX8BKsxBlPRsjjNjubghEnFz9x7t_jpIxf5nMu4aeviaDizIXVvCHflWu2y05tMJWXSb_2HqalxMmJ_0xpZOy76yqLCwFc-M4sX4b413jTSIBLtjf30xUFWyDYPjTXf1u8kAZW4_HMhdqqNqqgWbiB8lJD7EF598dgPeN4v1P7bTmxqL9rKYE8Z-81t72l3DAVSRPFF0xhxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Mu9oHYCmPlGaYfSO5vfpm3yOl2Sbhc714XWik_eUhnkSQD0FwZ4xewrQHKjq9ZOJvC7yfIUq-Nl2Kc3VzpTmCMBas-tvC9X77aD_h3ZpckZX6N1hiz2Rc7jHRVmRdmzFV-0GnKwuVccrVLq2p_6PvFThdfII2rQ1mwSVMWetrGlyTf0I4xXqZ0e-UH8pIi3DOpdtq_HJNsSt9_aN39rgC7kSHQQLmAaSXWM8jPNT9PhfktYImokUq5QtW6QXrPvGgvHHx_7XGaYcAxs-U6hvJUw7bu8ELARQIWszBwH8qzA1CB4TQWRQnFOoSLAuGQQhduP5B3nnGo47IjAezpTYwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Mu9oHYCmPlGaYfSO5vfpm3yOl2Sbhc714XWik_eUhnkSQD0FwZ4xewrQHKjq9ZOJvC7yfIUq-Nl2Kc3VzpTmCMBas-tvC9X77aD_h3ZpckZX6N1hiz2Rc7jHRVmRdmzFV-0GnKwuVccrVLq2p_6PvFThdfII2rQ1mwSVMWetrGlyTf0I4xXqZ0e-UH8pIi3DOpdtq_HJNsSt9_aN39rgC7kSHQQLmAaSXWM8jPNT9PhfktYImokUq5QtW6QXrPvGgvHHx_7XGaYcAxs-U6hvJUw7bu8ELARQIWszBwH8qzA1CB4TQWRQnFOoSLAuGQQhduP5B3nnGo47IjAezpTYwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iFsF2_5zvEOMtNEgvnPBcWarZldyrvSHxmKS03GYsZxm-oxf_xJ1r0HDDCtQJkxTtSKUcfWke39_KZC0Ib3bCiUsi6aPv31pcgGEKxuUpDv4Dc3JlS3_g5x1DokD6-mZ5x9_MOUcfsUbJNtPBTC9JXSFKacaEtHQhiH0_IQXOTvKxiFvHzG6bdUC22vn0Vg9DGXzjF171bG8PfJQq110v7gMjILG_7ugdGNhKAhvykW2fCQBg5GhLfFn3iilwyb2VTE-8wOYXsvCen3rF6ncwQz24du-EC3EA2LcwB_XKQM1whnArHIUrLcU0XL-4iUewxIxGs7xdN1WZWLOcs7fqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=iFsF2_5zvEOMtNEgvnPBcWarZldyrvSHxmKS03GYsZxm-oxf_xJ1r0HDDCtQJkxTtSKUcfWke39_KZC0Ib3bCiUsi6aPv31pcgGEKxuUpDv4Dc3JlS3_g5x1DokD6-mZ5x9_MOUcfsUbJNtPBTC9JXSFKacaEtHQhiH0_IQXOTvKxiFvHzG6bdUC22vn0Vg9DGXzjF171bG8PfJQq110v7gMjILG_7ugdGNhKAhvykW2fCQBg5GhLfFn3iilwyb2VTE-8wOYXsvCen3rF6ncwQz24du-EC3EA2LcwB_XKQM1whnArHIUrLcU0XL-4iUewxIxGs7xdN1WZWLOcs7fqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=tTDSEqwPam8hXHm67jfM1efTB4IZiRo179rivn7sBA3nRywQX-ve2jooW46O8cIweJ3jTl2z2RKZiV8yQhcXKMAUVDGATHIt1DVQzYIWGu24BCpv90vT4z-y0heQF9vLK1upLZUuYui0k57OgPQ-hGL_EgxcKMMga5Cnl6f7Ea_UHmLvJMFRRBVXQgrcM_6qVQOQQpGMfwh3eW1TAW7RsQoGcIroOE9TuvNRr--pPqS4RE3-7XTCRTz-CLEyGBHD1a5yqc-HFojyVoULlhVCUHO5olPixNp-FvsXIj9nwqd6NgsehJHWSM8At4vH0kP_KJ7TYEN_EAqOrIc7dkjVZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=tTDSEqwPam8hXHm67jfM1efTB4IZiRo179rivn7sBA3nRywQX-ve2jooW46O8cIweJ3jTl2z2RKZiV8yQhcXKMAUVDGATHIt1DVQzYIWGu24BCpv90vT4z-y0heQF9vLK1upLZUuYui0k57OgPQ-hGL_EgxcKMMga5Cnl6f7Ea_UHmLvJMFRRBVXQgrcM_6qVQOQQpGMfwh3eW1TAW7RsQoGcIroOE9TuvNRr--pPqS4RE3-7XTCRTz-CLEyGBHD1a5yqc-HFojyVoULlhVCUHO5olPixNp-FvsXIj9nwqd6NgsehJHWSM8At4vH0kP_KJ7TYEN_EAqOrIc7dkjVZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qobyZlpQMAzz7vVTzsxYDTRANPjp08v4YZay6MBG2xHv-M3vYsczmZJChLeRJPXtWLTLgE-YI3udf6Q2nh9aN3fh0UqCrpj1fwE2XG8aZsXhCNgzMjEIATOCqNpAkZUC5BrrT9bPIyDnF1THQF5_fRxhA2HWA-JAOHEaz0uMI4gbyhlpksa6ACRmuULxliTLvYtl-VPBslzXOLAbJqxKrsT2zG9COl4HSlKuLerRzjGRy_BgRQ6GTbS9qC5V2hP2leFD8LvjzhiH9soF5Cc17xCt9XYfX7d61gx8DuUlpK6jYB9-wWH3trf3oIYWNCtlgNk-GWFdKzlDaWClzZopkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=o8v7ACWLfy5eNo-UbgXTnFnSiHxm--IrBUfwPqlMg_0cS-Zp-LHVZa170feKgmx5nKZzk5uFTOPpBN3_fUNLUq1pRfK7g2OP4VTRfCKK4taroFTo2Q21A9ECkezWUPgiXSmfSiByb4X82ykiG1aN2vUsUUEIUOf7Mg9fe7eMJrOUlkoY0MY-Z7cRzCrzdyh-3x5x2ViceEkllWL-P-z6u-nPBHixkVHvtZNJ9B7cKBy9nfpjtzVIZmOs9xMsKYwp0ZB-OTBlI9i8-yJopuL3hCG-3oYTKowilPCsb900HTOfTd60J_5wauPtJmnqdhZT5tfmFbb17KAdjFuJaE_FFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=o8v7ACWLfy5eNo-UbgXTnFnSiHxm--IrBUfwPqlMg_0cS-Zp-LHVZa170feKgmx5nKZzk5uFTOPpBN3_fUNLUq1pRfK7g2OP4VTRfCKK4taroFTo2Q21A9ECkezWUPgiXSmfSiByb4X82ykiG1aN2vUsUUEIUOf7Mg9fe7eMJrOUlkoY0MY-Z7cRzCrzdyh-3x5x2ViceEkllWL-P-z6u-nPBHixkVHvtZNJ9B7cKBy9nfpjtzVIZmOs9xMsKYwp0ZB-OTBlI9i8-yJopuL3hCG-3oYTKowilPCsb900HTOfTd60J_5wauPtJmnqdhZT5tfmFbb17KAdjFuJaE_FFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=avLBvfw98pXD3pKkp2-i0HjW1TAXAC6oyh-1T_xxtCS2zvh-NmbBZscpR-HaWzN2t-YVRLOgSvqZxssJOKCdxhNs_OWSCPL817sP5G5aLbw1jcCkIYjWYXxzNATF8Lev_vQD7IQuPwbiLoAvZ-jc0CoFpQyhOKUqEyz4YuDCkUxCU-MXlrwpxdON_nysO8U5Ju4KJ7W5w7xH2hduiOwINun3T6Ia7SC1H2W7q4fcTVW1EeszazGGKns0Ev0y6io-G_rtIDyUET2Z29gMgVU7YWrvoso_wsB16i0bYVCktXP2eyBtXodMI6iznlvEXlDmM4y9S0UKYdyDTMLQqVP9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=avLBvfw98pXD3pKkp2-i0HjW1TAXAC6oyh-1T_xxtCS2zvh-NmbBZscpR-HaWzN2t-YVRLOgSvqZxssJOKCdxhNs_OWSCPL817sP5G5aLbw1jcCkIYjWYXxzNATF8Lev_vQD7IQuPwbiLoAvZ-jc0CoFpQyhOKUqEyz4YuDCkUxCU-MXlrwpxdON_nysO8U5Ju4KJ7W5w7xH2hduiOwINun3T6Ia7SC1H2W7q4fcTVW1EeszazGGKns0Ev0y6io-G_rtIDyUET2Z29gMgVU7YWrvoso_wsB16i0bYVCktXP2eyBtXodMI6iznlvEXlDmM4y9S0UKYdyDTMLQqVP9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=cDjdZ9ezjM-p9MSCJCfLmCHoZITm5lK02vXWhfuQXl4bywY_9lGWG4F4rZSDmgz5TMxtw6GcZIiF-IRr6Vm-lrKGoAIwr6phF_urtj8iXBGwb7t1R-Z_-Net5fdOTWKnZtANdclZ2_dZPiKKlQtHGk9NcWA7pM8gxVxZMWRlKByer7dguprdPDzIih-rHy2hsqTixV5WVBKrsML-fA8aOM0NJNIxgCIJ9dhb9crcfRUAAcm89_XY90j2zOOTb4xQbda-VfjEKlW4VqD3PecwIAY83Ukiok5n9mb3eWpssEQNts-m-0OortTTbpiPhPGAyklt97n4RHQsdOfe_KTfsZ1Z-rvs8RvqTPitHAFoymg3TZRcPzWP5rtrBcA2w-RkFqVpVLJs3lncUcuSVUQGee2EZmEIJCY8UKP7fQ__DeYM5t0S0-euRGFOMpTpPV1NskZ0goxhEW0YjLr7-pu5h7309CjySlERv_6mEC0SmN2V1-Rx8Zf5srydop5-FCKFliEBYMQQO7HgeOnaSkH_Rs60YJEFx_8UOp_tK1LXbFnS9vbkKwhuMvbos2oE55fnoHyToj0PrqG6U9Ea2nvLsGK6spckwiyxtmutNN1f6XvPZGbUU0PSDjAfp3kOxI1z6e-nESpj38sM3F1aJN7zbYG85s_rIWMMv0V5j37KgF0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=cDjdZ9ezjM-p9MSCJCfLmCHoZITm5lK02vXWhfuQXl4bywY_9lGWG4F4rZSDmgz5TMxtw6GcZIiF-IRr6Vm-lrKGoAIwr6phF_urtj8iXBGwb7t1R-Z_-Net5fdOTWKnZtANdclZ2_dZPiKKlQtHGk9NcWA7pM8gxVxZMWRlKByer7dguprdPDzIih-rHy2hsqTixV5WVBKrsML-fA8aOM0NJNIxgCIJ9dhb9crcfRUAAcm89_XY90j2zOOTb4xQbda-VfjEKlW4VqD3PecwIAY83Ukiok5n9mb3eWpssEQNts-m-0OortTTbpiPhPGAyklt97n4RHQsdOfe_KTfsZ1Z-rvs8RvqTPitHAFoymg3TZRcPzWP5rtrBcA2w-RkFqVpVLJs3lncUcuSVUQGee2EZmEIJCY8UKP7fQ__DeYM5t0S0-euRGFOMpTpPV1NskZ0goxhEW0YjLr7-pu5h7309CjySlERv_6mEC0SmN2V1-Rx8Zf5srydop5-FCKFliEBYMQQO7HgeOnaSkH_Rs60YJEFx_8UOp_tK1LXbFnS9vbkKwhuMvbos2oE55fnoHyToj0PrqG6U9Ea2nvLsGK6spckwiyxtmutNN1f6XvPZGbUU0PSDjAfp3kOxI1z6e-nESpj38sM3F1aJN7zbYG85s_rIWMMv0V5j37KgF0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=huUf_VEHi9uvVq3UTS2FT074D-vUaYcBSt5plnAj9NDefGNI3iBT9K4WM7YU5_qFhod4rKmX3k_LGTWsqZcNcUj1CuX3HZdGThP2cIEq-YpVcV60D4jnYWyYYWF-EHChq9E9Q_H19-U_aF_m3ACd5tXqJ5kXupja2WR4B45DuZ8hiFzIiqElCLuSss0cCayTab3yW7n6KidC1Bz_MYt5E_xFz3kzbJh1RLLSE27xA22Xevt3sTRujBy07ti2L5vUyKN_ixnCq2M7gLkGvo0N948NO9xl1CTv0ja1d_60coq6-u5tB692zfszsg6YriNcJh-eABYul3QtPjQNJFwO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=huUf_VEHi9uvVq3UTS2FT074D-vUaYcBSt5plnAj9NDefGNI3iBT9K4WM7YU5_qFhod4rKmX3k_LGTWsqZcNcUj1CuX3HZdGThP2cIEq-YpVcV60D4jnYWyYYWF-EHChq9E9Q_H19-U_aF_m3ACd5tXqJ5kXupja2WR4B45DuZ8hiFzIiqElCLuSss0cCayTab3yW7n6KidC1Bz_MYt5E_xFz3kzbJh1RLLSE27xA22Xevt3sTRujBy07ti2L5vUyKN_ixnCq2M7gLkGvo0N948NO9xl1CTv0ja1d_60coq6-u5tB692zfszsg6YriNcJh-eABYul3QtPjQNJFwO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=CrHka8UzCoZ1iSHXIzTCdkEQ3YY0DK-hNeXzhAe8O6w7eZzHDYA3tPJBJ6LlzonDwqUHbgATEayrPzOTkiulsxs0fUyR_524XMTaxVQPaSg7WO0wkm-gqhqvJxQvczKcgQwJaQVEPMDAxXQnjZmoVUnqFMNXA3aWjdVz9fi5eeBL5eiUaFFqHN3qMGiQzSV8a7Hl5_KyHLAa7oWNvNq3Ye44dLwoyMZE4pfH2O-d6g9NnEpbla6hQK0X1-bImi8W13Yi0T4lVsU6h597O8hLXWFQFv3cdnv-BQImIPQTxHnkYTPajQul47nkxkmS3RS416fM7ikAu2tkTn8Z2zA04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=CrHka8UzCoZ1iSHXIzTCdkEQ3YY0DK-hNeXzhAe8O6w7eZzHDYA3tPJBJ6LlzonDwqUHbgATEayrPzOTkiulsxs0fUyR_524XMTaxVQPaSg7WO0wkm-gqhqvJxQvczKcgQwJaQVEPMDAxXQnjZmoVUnqFMNXA3aWjdVz9fi5eeBL5eiUaFFqHN3qMGiQzSV8a7Hl5_KyHLAa7oWNvNq3Ye44dLwoyMZE4pfH2O-d6g9NnEpbla6hQK0X1-bImi8W13Yi0T4lVsU6h597O8hLXWFQFv3cdnv-BQImIPQTxHnkYTPajQul47nkxkmS3RS416fM7ikAu2tkTn8Z2zA04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EI_Db4RIykI9LA9q4TCx8daWrhXLjVOaYVvXvWcYgC6TRtrjO8O-isJhLp5D6ib0sGIy-FQzWPwiAxNMkKOLmqSdXnzGW4A5JpxqtmqRDi30thK5cGyig9tCNhAxkY6Gy-U1CKRm4TvYlHiThmowgu87apfBeZzVZSuEZ-QaWDRNXiuVj-FIOcwjIoerAb_v1SVwodKRCfnVx3puMs3Cz-85YRbyc6U_ApVPO_30hv0poG8DdIdQWJrHaJNvyDa8e3WLCT3aye9eoemxebckvgY_MgJYIf9A4nE9JJm7-tdN6wi98sdtoED_Z4fTC-XXrkwGqSjOLqWALXNLGO7Psg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIGFcoFZR0UmPlevFUjbGGuNyELQycLPsPymN9ONKF_iqT8ENRcsg5ygquu6uSQH-pxZrLIkd3MLwWky1tJqDsw_awe8y6_wEiIneLfhl-1ydrIxo08y8aY-A-7YlJJ4qtUUAzVlbUNCMgqEcxcTV9vWyt6OIeb7oLbqH-vWVjLe-lePUDXP_x4LR8M1goaKoy9JDU6L11qUZhz11ufFub5NgJFI_21-D461wYu0A3EqS5EgTh9bkD7j0IiOLTuFLC8kgEzhp9ZYdAdkJBy0aY2zHBW2GmMpaehPsEqY7yNs99MrJHv9E-iruQ5PbVN_bsdOeFu31mZJz9ndpkPlww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=Gzou9DK9czpYIN3dHK4IWtuf7GOhw0K5-Y_hRq6N4alYYMnI6JlKYW8D7ghL6X5OahcWOFVCRpQuHP1J3Gx9cm-poEoEaI_8DxUQjuNyboukHLjxRQjtbPcS5DMEvCJf_I4Jsi_esxqLIgyG2zOBAXVadPq0y5-fvpbq2YLaZJUb1d66g3Lb1JZeCXIyo58edokx_W6MfdzA0L41aRe0umIBQ3vrhjLDqnQqk337NzRgp8LyI9yitL5IWtgqXeRR4X0HIeRxtZqmNJahracbRzWoKh092uZ6Z3NkR1DBjH7ufmunqZwyEJLNAKR7gOHUhBeQ8x_d3-xw6eykG7cgRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=Gzou9DK9czpYIN3dHK4IWtuf7GOhw0K5-Y_hRq6N4alYYMnI6JlKYW8D7ghL6X5OahcWOFVCRpQuHP1J3Gx9cm-poEoEaI_8DxUQjuNyboukHLjxRQjtbPcS5DMEvCJf_I4Jsi_esxqLIgyG2zOBAXVadPq0y5-fvpbq2YLaZJUb1d66g3Lb1JZeCXIyo58edokx_W6MfdzA0L41aRe0umIBQ3vrhjLDqnQqk337NzRgp8LyI9yitL5IWtgqXeRR4X0HIeRxtZqmNJahracbRzWoKh092uZ6Z3NkR1DBjH7ufmunqZwyEJLNAKR7gOHUhBeQ8x_d3-xw6eykG7cgRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFy0xVtgbc_FnwTn_Bw3tV9Cwohsi1rz_XMYT07ZxPjnKV6O3_fh9Vuehqh9kKrayp6V3Cqbw9ckC_ctwuRgHUZq47JodvzCEVazHDl6lEVJMmUD2gHN8X-YZqEOfRrzQ7ZqWy5zuwbeuKnb_975EVo0hHz9jTpFmMjPeuGZtW6hEogKIceUuWw4srEJ05dANCnwhY1cYgsV6Tn53papppvOgrVpKlfm8QWVrARxqfg7Ur9EIrpeaCA3vaKAjEGT7pXPLN_n5AS6puK6opxbLh_AgvKjj4I1u6YdyE-t6MVtbxxWzRrAMY9nzbHAeK0LcYX39LnCJBFoFEZFWQKi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hG9ZbIEJLUi7Z1sgPXfaobP_jr_VaeEiNXWR5AkwJ9XD97umO1bcLBpvp75jqQiNn8F6ZPQA0K_rRuT7xI3thgCPGAocuRmap2Acbw-oTekaxaUAV2zUiTCJx99gawnSsnD1irT3Y9p5JB8X8xHaRLS-_phwviUqnQtx1EUa7AuytKpOR7oi48Fbrj4mPZecWBftfXcGgY7uo4yznuGZGVBOlVZp_9qnmr1P_JN5w897tU9Y40wqVxL6qp6AuQOOaKXsu-MHcCnfGNMnVMZUiUtdhcXZiyyMnpAyVe8rxjYf-TispSe-jCq3xzCVGa2CDYWIhkC7FZdtvIbqv4cc_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlArcShLl7hEg-UKpnc8cfp3V0YogKpG58L7eMXmsqVo9Zzn_8dJReoDoGLYYQAjocrTP70xbcS4KVMbdWMKm3Z34lOu8uK9mo45t7h2ee_-C9f3Wur3Xaf5EDSaXflUu_5RnJ6rhuBr0hMPcA6X6nceqrchLRAWd_Wh9PKc-R3w8DFsCdwM9khdMz3rDuuM7J6ycWYyHbi3OWIpxl4LYnKUXlxl0zZgW9aKYZGq0rSpauoy3CPtQ_5i83A0UiSTnlWs0OQy9QicZZIPnWbTp-CwAGMzC7XQwJgmuwubfv7xGd8tTQlpLnQVLMlj592DWp3gPNMWaPn3Kreb8L0WEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAIKPQO8LIJAcAVAzQdCBpdvAWdN4A0telniuPOANGeurDPBd5Ssm34lqud34zeMgQTjaU51vnsiwg-IWvYEEpXc4XOAhjxFGIFtBdUXBZwqgE7e-8spPuKjVz3_pFJPBqCZK_6XB9GzHC7wNg6Mr9i4qrEZAKM5I7iyl4xXGB-BEmzVNTJm_h75SfUQ-R123uiVFoTJsLbtiVpFJzgDH6eutY6wdETPHrJ_f0FkS0gwIWA9gj0aVXsqawNFYww5bhQbK7CC3QO_dFFvQLBbFMKH2K5Xs_VRgSTZiu4mYltvoWPlwh1NLv13uEI75KOJ9jOVcuyF3M8zHVy1Zz1ruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=Uv17Z8woa6j7PvAykD8yFfsZrJ7i3_YzQWSv-MvHT7CdO8Ku__OjXyk4yB5JQNa6jTIATRRd_908L1eAGl86zzYbGfR-0VCWcDs0mBLaWiSc3X7_erLQCoiHHz2BokXqxjmZfx0RhZjnP9NOwUCQ3FsIIlZKu1BxOwGAUnwpxit7yIoojeygTmUugvDimQtrALPRjCoclSUrIyZ3q7bSdB6fPhhtb1BaElBhwa1OhlaBlNsA0YuJoogMNvmiI7AdCzX2pWy0vwvWxHeUQab3509EG4UCeg7eqcIzLj1xaWZ-xhq1UyXUKU-vx5hyjGfH5uG80m5p-grXCrCqB1DtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=Uv17Z8woa6j7PvAykD8yFfsZrJ7i3_YzQWSv-MvHT7CdO8Ku__OjXyk4yB5JQNa6jTIATRRd_908L1eAGl86zzYbGfR-0VCWcDs0mBLaWiSc3X7_erLQCoiHHz2BokXqxjmZfx0RhZjnP9NOwUCQ3FsIIlZKu1BxOwGAUnwpxit7yIoojeygTmUugvDimQtrALPRjCoclSUrIyZ3q7bSdB6fPhhtb1BaElBhwa1OhlaBlNsA0YuJoogMNvmiI7AdCzX2pWy0vwvWxHeUQab3509EG4UCeg7eqcIzLj1xaWZ-xhq1UyXUKU-vx5hyjGfH5uG80m5p-grXCrCqB1DtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=rvFK2rWE-o_ksHFtPk7_2KTd2eDx-G6xvj6SkJdSGCSDgO57xrsWw1t9aAhgXIVIjJ_QPswv8LBLYLV-A8tpkDyJJAqvQ9MmP_GV3vM9MBiqAEmiaN7ELFnyuMJBaCKnKmngh94i_NnDKX-MOeDlxxUhqqENcBU4Z7b2r81Y8NpLCL_I0KpgOXrdrKs4AFHV8YWxxYZudUcQv4oGJw6zbp79zUWAWBsoLi-0uNDqmUHyUjiBIFZvAAo4wyGZ9xZow2brIJG7J5RJ2MKpSdhrlTUHaNEuClv9ShG4bqVgJGtrhRmr3w4hQSwiVUW0ydQZ8S7yuqpBXKSzZCe7t43j9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=rvFK2rWE-o_ksHFtPk7_2KTd2eDx-G6xvj6SkJdSGCSDgO57xrsWw1t9aAhgXIVIjJ_QPswv8LBLYLV-A8tpkDyJJAqvQ9MmP_GV3vM9MBiqAEmiaN7ELFnyuMJBaCKnKmngh94i_NnDKX-MOeDlxxUhqqENcBU4Z7b2r81Y8NpLCL_I0KpgOXrdrKs4AFHV8YWxxYZudUcQv4oGJw6zbp79zUWAWBsoLi-0uNDqmUHyUjiBIFZvAAo4wyGZ9xZow2brIJG7J5RJ2MKpSdhrlTUHaNEuClv9ShG4bqVgJGtrhRmr3w4hQSwiVUW0ydQZ8S7yuqpBXKSzZCe7t43j9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ6ntGWfn_PpKVd3ObLvjhUPe-sv1SQJD4P_XKO7jQnooXeYVXZdXmlriHdwytbheilJFWhOx8q17puqz13Zf1he5UJL7VZ4BFJ7tNrRRvrflzkdBJAM_cd49pwDNYYmmXJTircbzOe4J6AxTWZJA0BYW-RD2A3AX1lYFeeIOPDc1hLosweMmtJx6_Jw_-efcgDrJg6U-gRfXtEUNp8UzA9gxb62b_67cwIY5ImxibUwHVyFVV64ZkDQH9V8qiXG_iT3VY0RZW3JHFequLmktSj2YOpdz6eDImnWrWLzw3i9qSP-lIBo3U02uFgSAZp3Y2cY415vXQuAqXNJ3zVVSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=sTHqgOJtcqNAhldub8Ie8EfhsFnJClYL30z12y2bA9QY5IIDUINb44tgz7d7cVPHKulVsa79sv7hUElfW080onRl_tZPFPxI6S7EdYI4WxFuY3HiJoB1iGVkd_EnCZPVnKqC6mUcYO16iebC-7uZwT-ysZvg9unSsW8WeV4ji_Iq7ReSkDUJrqamp28EtFBOAY3vAFuwdzyhoMPf348cjC-Vy4cGK5MsAvbnxVAzg6v80txHPQtRxalTLeHzWEhd6lcuScaK6QicIVkZtQ7bxV4iRXC32c7cZXVw8xRo0sCzkR_tigbgxl4ORZoEV5Rpyczjy3MdDJkaoK3NvV5S6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=sTHqgOJtcqNAhldub8Ie8EfhsFnJClYL30z12y2bA9QY5IIDUINb44tgz7d7cVPHKulVsa79sv7hUElfW080onRl_tZPFPxI6S7EdYI4WxFuY3HiJoB1iGVkd_EnCZPVnKqC6mUcYO16iebC-7uZwT-ysZvg9unSsW8WeV4ji_Iq7ReSkDUJrqamp28EtFBOAY3vAFuwdzyhoMPf348cjC-Vy4cGK5MsAvbnxVAzg6v80txHPQtRxalTLeHzWEhd6lcuScaK6QicIVkZtQ7bxV4iRXC32c7cZXVw8xRo0sCzkR_tigbgxl4ORZoEV5Rpyczjy3MdDJkaoK3NvV5S6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=WXXNRcf7EGoas5e5_VCTwBzFhx8vvPMXLy4Bv_tHGNegwzR9YFwROh4gbWtVhPOGDOCN-L_D_SacL5YY8p1xV__-b5QmPD_UB8EhgOf9vBNUIx4dlQSYpz8XG3b06SbIulRZSwBKNIEaaDtuacs2y8Jl6z5MS9Sq1OJ0JFVtHKP6Hu6z2RXYXxoDq8TYFuz8lsvtLVWp5bRUj012i5ExEFHZSH5Oh6YEX-OWrTbXLnwAaSnnDd4ysZbFE0_KbiYlHb52sArdWNGEhtOVWfkwX-dseKWwi0xSwyZPGq_3_qcm6EEnsWJTzqhDG7sUANbMRzbEHdVbmBAoWWDkPthrsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=WXXNRcf7EGoas5e5_VCTwBzFhx8vvPMXLy4Bv_tHGNegwzR9YFwROh4gbWtVhPOGDOCN-L_D_SacL5YY8p1xV__-b5QmPD_UB8EhgOf9vBNUIx4dlQSYpz8XG3b06SbIulRZSwBKNIEaaDtuacs2y8Jl6z5MS9Sq1OJ0JFVtHKP6Hu6z2RXYXxoDq8TYFuz8lsvtLVWp5bRUj012i5ExEFHZSH5Oh6YEX-OWrTbXLnwAaSnnDd4ysZbFE0_KbiYlHb52sArdWNGEhtOVWfkwX-dseKWwi0xSwyZPGq_3_qcm6EEnsWJTzqhDG7sUANbMRzbEHdVbmBAoWWDkPthrsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=LNVDkrzl0wt9JFdDhGG7FenWOd--wQE-jYjoyt7HJXdog9uBzJXtxExXqT2SRGmUVqlSqkB4OD3euAfiGmzpDLd_KrRcosmFPIX58NXvIo1qTvXYmTfnHttw6cu7YtICMyvKabpEKhTnnFKqR6LxWnWyWDxFCTcHdGZ31XYFOQ477kkzKwbyGLrnRUni0rR1K6lORPQ6fQdzFlpaEpocpY08tTfqvOr10HZKLMQTJGf1qRQYLCDjj5jbu5-4tqYduN2JE4iRvMeba2pJuhXklfVgeE-L5ANW4XHa3DI9Ah39vIDx6ROPU9-XLroeoE0CM00BY9rkTWC0nY3yfEdwgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=LNVDkrzl0wt9JFdDhGG7FenWOd--wQE-jYjoyt7HJXdog9uBzJXtxExXqT2SRGmUVqlSqkB4OD3euAfiGmzpDLd_KrRcosmFPIX58NXvIo1qTvXYmTfnHttw6cu7YtICMyvKabpEKhTnnFKqR6LxWnWyWDxFCTcHdGZ31XYFOQ477kkzKwbyGLrnRUni0rR1K6lORPQ6fQdzFlpaEpocpY08tTfqvOr10HZKLMQTJGf1qRQYLCDjj5jbu5-4tqYduN2JE4iRvMeba2pJuhXklfVgeE-L5ANW4XHa3DI9Ah39vIDx6ROPU9-XLroeoE0CM00BY9rkTWC0nY3yfEdwgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukwYSmPAN-Sd4RgR6E3CUwJ9HcLTXtZho6SuPiD2MkEzOypJEf4QdHGLmMvOfXhw29R1ai_xQ5YOmbKhSp9R9G292AZLppymAaR55VSfD31knP8XE0QmiML040FOJsjsaCX7VrTSbrUXgmBRehEzQLaTCC0_F-e8dFST9FeJMUj-YFut7uIKouzML35gtapG9TGDwSxndGGYjWS1z51HuraNsZrqwZ5XIVZHH2Bab7KBCuWwU1GElkV16ZdnUrtUm1PEQ4oUlDGku1XBx6g_1z56SgZrtxksQKTAEz1-v_dQFlPVU0V7TKM2XjZ7f5bb9EMO6x5WVYVxG9PlnOQI1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=NgYNrDb2CzdSy381mJ0D0BjCmnwCSHAhIJmgOEC4LLZyv2VR73cqu4VbeJZtPaYpW2Et38m24VP4mJLWQJrpN9MDai3O8AD8aWByvI9dyAh-obaf-4ng-sl-VzJuygrqzIjyHP0PipGuGqUyQrqwe0niIQEDeygu79v2fpOjyXJO3yYUQBOQMp4p5-J6FWFjS6bsAWz7urNaBUtAZTHNrND-ROoWDvzJFV7-xAnjIxpz1BNRJWrERG1mWRbWkh7Fszz6S8FyEg0-V_dK19fAzpTW6yolb8l9a_xkfM7LsdVRgxDp1ibqxxk33sGG_YSfheGl6F5pwgpXO9n3rMJXtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=NgYNrDb2CzdSy381mJ0D0BjCmnwCSHAhIJmgOEC4LLZyv2VR73cqu4VbeJZtPaYpW2Et38m24VP4mJLWQJrpN9MDai3O8AD8aWByvI9dyAh-obaf-4ng-sl-VzJuygrqzIjyHP0PipGuGqUyQrqwe0niIQEDeygu79v2fpOjyXJO3yYUQBOQMp4p5-J6FWFjS6bsAWz7urNaBUtAZTHNrND-ROoWDvzJFV7-xAnjIxpz1BNRJWrERG1mWRbWkh7Fszz6S8FyEg0-V_dK19fAzpTW6yolb8l9a_xkfM7LsdVRgxDp1ibqxxk33sGG_YSfheGl6F5pwgpXO9n3rMJXtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujEzrzzqod0XCBy45iX60_U8BkdLCFV69wu3tGu7aQ_EO8lAqVyv8nZoL5E5jK7Wd4RcmnTeMhjvklvqV5FQP6bodbUDK_AOyImmwVkMdAQz4ThTdgGRV8wmcuTHCSQRm0LguW7T6QcGUliYpatxsjRzCFXQb8_wLmAwM6nZrMgZWSHBBSZt665uqRjW-xB5Soip0vUYsX6OxXGKQP_CQCy26J1sLNDC6nWnn127L7_lAW7W9ZsH2x0cU68zc6kGBxvKxJm19d0-f3BlX7c6iiNyLJu_ksgiBZvTAxAg-6o8BxqBLBnmfq_LwkpYfh1Z8p3CC88rCnnWovxiuIRuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
