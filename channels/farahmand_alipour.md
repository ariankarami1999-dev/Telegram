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
<img src="https://cdn4.telesco.pe/file/CGkep57lpq0yqahf8SqpF5QE4l_QaXKucTkO1el636RgcSVACl_482EKWZw-Eziyp_eWKA3xavC4juZw-pSSnfLjgWprWYt0nN5sEUfNOXGvr0TB4CqP6EHkDep24elI3W_QwCEQ52xkpZUvBsSIlS37SowaR64mI47vnCUaUuNzSkXLzYnPyaQl36v8beHCjmxC2H9ii1LYN11kynytPU5uXCJ2Fnkx6BWu-W8M9ufG02aQJ-SMRTd85YB2ZW3Zbrd8ZasFfFLfppAH89Dr0AjgPGcr5WtHUbAWcxvmWvatYfBt7CwsbJcaQrZ9miMaBW0-LY3tV82UFJx-gUoQZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 03:11:18</div>
<hr>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHMFFHMh2vfBe1zauUgJI96dfdW_Trwayjr42VE78wd5LnUJ-eVcc04vLwR1H3YoEtInFe-KsNB-agomIb4QEcpiXmn3US0RycVwvW86LSYkMJ6rZTtW-URwnEDAbF05z0S3APEbg0zP4t5j9ctXsqQC4A6GYEgxTpF4B-7g-A05_AIsS5gN53qjsYcaLdDqFhTbUqLvy5gNypxVSuI9EDX2YpZeTe2Avg47UHlWdaE6EeZwLfIWpUJpfj6dIG0fehUF1U98t5VoCuHcx1jfSk8RJAV2_8fPC9XFgKh2mTVQYXVDlHmewaZpH8s-Sbw6Fu92XVgFIERJyuZjzxjEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=tOP_lKKY_Dc4QoHSFRtx2BKrXQt3zVyLL2keswccMQ6wfK7r-nuX2IY1pYAwavdXVMUyDD0Hu_KpM0OydintGQAw4xHPdz61ETqhbtAzCPig_h8FgFUiC_i1jtUoaqs1IJosEuGQhkNQzZeIO0LpQerhp2XS8gz7AHMYzf-2PuGeiz9u-usPIPXxo_cKeGu5nAxApVcTJFr7vymcEN96AdRzXqNnvMTIUwSl7nS64GkIRW675Tzv12azY9dJc4X32JPegr1FqJf5JXWcyWF1UkSwaICrCe22YkEBo-2o42ZWv8ML5E1fJH1IxBxuTQ5VEGPSQR78EBFT-IUxx_Q3kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=tOP_lKKY_Dc4QoHSFRtx2BKrXQt3zVyLL2keswccMQ6wfK7r-nuX2IY1pYAwavdXVMUyDD0Hu_KpM0OydintGQAw4xHPdz61ETqhbtAzCPig_h8FgFUiC_i1jtUoaqs1IJosEuGQhkNQzZeIO0LpQerhp2XS8gz7AHMYzf-2PuGeiz9u-usPIPXxo_cKeGu5nAxApVcTJFr7vymcEN96AdRzXqNnvMTIUwSl7nS64GkIRW675Tzv12azY9dJc4X32JPegr1FqJf5JXWcyWF1UkSwaICrCe22YkEBo-2o42ZWv8ML5E1fJH1IxBxuTQ5VEGPSQR78EBFT-IUxx_Q3kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=dSf1yFdXvLD_tFa6aR03Nl7JgPfM_wdkQg6bib3DixPFDdbULZ3ciBb6iPvYdrbDjfnsE6XHzcJnmcSaZv_Fqp8rC_CiXly4hYfzoWUQIJiQboSU9nx-J1LONT_01z7WVfMZ5JbI0m8X9peXpD9XmyJ2h9zNa4Bszi7deXCeqpeATBDsmRiTldrHYQMR7vZS2dL2ybNvXgi2mATd5tzpvB1tdjVClpsCA215gILneJfeRRYJy3mnF6Sh2PVpHhFCtIiGCOYptVpRslpgIy9q8lUFswRO10clDJtjeFsbDZz8JqPKzJRIGpq9-x0dG6SntnjxKwUYopt--gr4JkOI2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=dSf1yFdXvLD_tFa6aR03Nl7JgPfM_wdkQg6bib3DixPFDdbULZ3ciBb6iPvYdrbDjfnsE6XHzcJnmcSaZv_Fqp8rC_CiXly4hYfzoWUQIJiQboSU9nx-J1LONT_01z7WVfMZ5JbI0m8X9peXpD9XmyJ2h9zNa4Bszi7deXCeqpeATBDsmRiTldrHYQMR7vZS2dL2ybNvXgi2mATd5tzpvB1tdjVClpsCA215gILneJfeRRYJy3mnF6Sh2PVpHhFCtIiGCOYptVpRslpgIy9q8lUFswRO10clDJtjeFsbDZz8JqPKzJRIGpq9-x0dG6SntnjxKwUYopt--gr4JkOI2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHbMBcxiefZCwO9HbFl0b9G9q90je7YkFDoEt7TxrqNgqu9iBNuzJIl2HTjfdCZRfvm9fWPwrN0NKZjB_mc0u3_3uKyw_vfaWG2VuS857K3pfI3LLGlcGupHFw9e_qj2EDC0QUZpqBs9wJf_w_sBCf4wXEAtVhc3vnf56tBlTrOPSSdfOKbUuPKKv2VOGplxdQZE8O2pFzLpnH_067gfd-aOAamkxIZLPTO9aRQaeKZL8HOdk-ocIRW0kHr_IBn04vgut0yIXpaEWx7wYLFH6m0j7MVvQ6PZKwzX2zZplqEZoQNhebGDK1yeYu8fA9lBQFez8DuIMYGrkPn5PC5J5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5XA5xxIvKfKhlWZ4wBvbVvdCbLUvJ-6FLPOw_UtJRS856NIn-lknRl9tmrsh6yTeKzNQFFHlI2w-POl19vy4kiSMvbYcit7VKq2_NKqSLbRg6zOsGCG5recU0cNME8y74RWFowWPSksSKANBp2MW7DXQej8Iyx_g9KWzbqcRvWR1afPuYJ_L0mT-TihxUKurAt_PaNvtDf74Vf179Yg8fU7XFSai4ydW7pytzluj_ySDU4-_TbJ6Lp8nGYG1-2SihpSu5eNMQMQoE_VWQPwqyOOukZ0A2p_pVm7tQeJGts2z1yewvKWDS37xIa-n8bhxJPUw1U_QJlZ_ixyrum7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUjClHVzaH5KUBjo6d6vkLMJdTMjD8mbT18Ch4N3IeQvI3XkFaVIigydKoqP60RTwiZ06XHUeSvphqfrNCEKj3JNGtEqxEbrXQFUQrrSVbTROd44uTwkmUuXWj-2gcbdcJ_EvIq6eFO1bHpWjvLoy4Sf9wJHfK_0581MF7o0vbFsK211ufWWrNtLLY6uWZfweB6LauP7-E9cgwswh2YRk73CJnT-hM3Dvlbg4SuPklcrBViixlD3XNKOTClNgnrBF0TH8N_3AayrzfT_yENeFq9x9ErrH9wKAoV2SmTDT4Oa0vt3Fa6d3SKVKp0sW_Oi0WToD8X1UxZe8wa_rJsVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-LjuxwJENWdD_hooyPi_qgjqJ9feZHxuxEJi2Na4TsGNRnX3OawM1ee6WQ0NDfnaBUaGrLgZybYfa70bKdEeBO8yLBMbwwVTArAa3TUvsFPuMruIKmxSaS43Rx_FplZRZVqQVPnkOTo9FbE1lxhwilfw_tWyUeijC-dTgOccBkgyAAJRcID5Shu7UnDjMwbJwW5FXsZOm5COaPGmIwkI8AYF5LtZCxY6CpDiG8ZlK9FY0Ko8dqdABwaN8buDU0CUzzLp76_3bjKrQeuccnQ9O9Hv4QvAlAVS5IKWNnHu--ZUbg5SHOqDRoWZxfpuLnFp0Xwh2IMc31qS4Lx6qHqnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_0Fj0QL62WE3q-PkAIDk2hGRs2dPmKFsGz3_TPqW19ItMKLdi0pvaP5dd8R6p0MFaRda_AiTVD9tSNqLz1NQawje25wdXlUDNnatJGwi_VeZpAqjw08qBU8aE6BhowrsEQGR74ULcH0KHZRcuI0ou8uFg2gQ44uh6YcaB1Bj6nxSmwt6P3luxkgU0F9z5QKkA0sUWwd66UwpHUd780-B2LS2MeD4kZFuwg9-meZ4iVfnnuHXYzDKJLKBWFTBHzcvpTEzcN-a5jFeYmIc3rPOXyGOfaBrGe5K8qnGdMaXPE_pg_ttAEjAUg1WjABPchiQfG901mZ3FqL8Zz1hjgjmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_M_u0lvhF2WahWSJmHZv9rWEiwRwwPGGSMBkAnL-9BemINtXl79ELmExzzV2Xh5VjTyLS2n7p98TM9Jd3T6qrBKQRZcy7WIJmBucnAQ9D3i96wcMAiMhFizI32hdJo7RswHrKJTkv6lt8f-DlAg43sZ5M8NXiQCu-XLLlvYjYTIxznR1dNvn3StyHKqhFBWby0UIBmJPmRElPFxTsvPBjMXhUXQnT6g0fwlnzNEDE4-tlIIl5OB71hEOST8AtRF1s8ZIm_bdDpo7fyYTPZ7qOjBHkEb_INVf6NgFjsbP38IgWWDmGhLnBuYe5GAJaGxWER8W2Sf1qYw77aF4GQTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v07wCgiZ4-pN1ZLx7Mj5lx23c7bH2jcbgFhOVF1CG3P39a7LVlSOAkGcITA-dDHTqqpDUy4JkGUIbecKAl23ugJQgkow20RFBOujNO8WG6-_PEBdbKeU0qmM9-aQlRpF994IYZiGj6I2IAIyhKKe-rjFD4G5S_mjJoDMFA_Ncias6mkjkbrLZ4ZGMxbneweIyuHKOK8iBRwIHshhQPoDm9-ymX3CHSBYtWT9ULbVZpkQe31_0x-33g1gcT0aVjT4YPKchATvp007bERdnStLS_fmeWZutb4cPJW_wdItKZCDjMk8OLNuzi4hzWEX6dACebpxSkY1QLp0vYpddFW6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=qcQUHYYSIL9-eIHFSDRsQD2faKWm4ohylb1_M45HADSynx34UxMibVCbsxBpi5bqAqcDudI5EK2m00R5ySNX8uuk31YwarKMhM2pFTekURnUXqyyjFT0QxyzYK_6LEejJCVM0SKEmKdJOAih6abYlzbink4y_083sS5o2hK38xeN5Im6N2QZRGO4DDQG_tVWI05F9mgJdnMfkh6Qz5fWKb6GE_xBbPbPbLkAXYL6ioZvmzRwt6ul_IeeFAMLIjuuoAJfxd5Ywu34IedV9PzkBj8vOvxZgooxRgkBkynHtOnjx9iSwl_k-FfrEqI1AuRMcOUPz-SSJMoIm9dDq8CqDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=qcQUHYYSIL9-eIHFSDRsQD2faKWm4ohylb1_M45HADSynx34UxMibVCbsxBpi5bqAqcDudI5EK2m00R5ySNX8uuk31YwarKMhM2pFTekURnUXqyyjFT0QxyzYK_6LEejJCVM0SKEmKdJOAih6abYlzbink4y_083sS5o2hK38xeN5Im6N2QZRGO4DDQG_tVWI05F9mgJdnMfkh6Qz5fWKb6GE_xBbPbPbLkAXYL6ioZvmzRwt6ul_IeeFAMLIjuuoAJfxd5Ywu34IedV9PzkBj8vOvxZgooxRgkBkynHtOnjx9iSwl_k-FfrEqI1AuRMcOUPz-SSJMoIm9dDq8CqDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=cuye6X4qNVzaXbl99AI2VBXxYCutDa57BYp31MEOluy6haWWJZ2FyEHfUxbl7isiL2-eBZoSFXG0lLwfqh0GUofTvtN0a5Nee6mx7MiHUgYXk8MEpuWxal18R6EMMF-v_kZHLunkNVzUMQEElmxr_xCgswauq6Gc_avgkK19TS4CG-2_kQ9d-P7VZsacZYkzQRiTRm-_udsAzJ1S7R4J-avNwpwzkcVlvEboCCPByvrTc2s6vengjJxlBzAc4HaI-jEGO4XoncTVkIXB2kqruXnB0UuJj0kSZi6ZdaattGRHszUUWp8k1XusvAodjsFYezNbGEM5gzZ5V9QsrYM92w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=cuye6X4qNVzaXbl99AI2VBXxYCutDa57BYp31MEOluy6haWWJZ2FyEHfUxbl7isiL2-eBZoSFXG0lLwfqh0GUofTvtN0a5Nee6mx7MiHUgYXk8MEpuWxal18R6EMMF-v_kZHLunkNVzUMQEElmxr_xCgswauq6Gc_avgkK19TS4CG-2_kQ9d-P7VZsacZYkzQRiTRm-_udsAzJ1S7R4J-avNwpwzkcVlvEboCCPByvrTc2s6vengjJxlBzAc4HaI-jEGO4XoncTVkIXB2kqruXnB0UuJj0kSZi6ZdaattGRHszUUWp8k1XusvAodjsFYezNbGEM5gzZ5V9QsrYM92w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=unxpKc_ajmRc-N5azVShCQ1x2gXpAubAveHUa2GX4QcRGrb8lSUH4O3Q7oVhB1Is-CuXZoYhoqWJ5TPsDKbiST9dYv2_1oWonyQ2IxOiG4zoFNfq5wtBJ-nGaZYZZ3uCmrmWEYO2ZNtS3RU8tRv15jxOImoIubdq0wCiQ-ArCpTop3E2en83bK5CXi6mK3cAKDu5TcFk-fw3qpJdWa-Y0lpBJAiOocmupEn54DGfeYfKXXB7l6LQzM2P803vLKxl1Kh36dkj2jY1QrP0eA1z18F0ofiCWfeT4GDDU5E2MHShiKZgiK8fzD5AJyetWdMPTtP4JNfg--Qnbb5nyJXGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=unxpKc_ajmRc-N5azVShCQ1x2gXpAubAveHUa2GX4QcRGrb8lSUH4O3Q7oVhB1Is-CuXZoYhoqWJ5TPsDKbiST9dYv2_1oWonyQ2IxOiG4zoFNfq5wtBJ-nGaZYZZ3uCmrmWEYO2ZNtS3RU8tRv15jxOImoIubdq0wCiQ-ArCpTop3E2en83bK5CXi6mK3cAKDu5TcFk-fw3qpJdWa-Y0lpBJAiOocmupEn54DGfeYfKXXB7l6LQzM2P803vLKxl1Kh36dkj2jY1QrP0eA1z18F0ofiCWfeT4GDDU5E2MHShiKZgiK8fzD5AJyetWdMPTtP4JNfg--Qnbb5nyJXGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=DALzq_UU-7NlBYAQ8mCRQDaKSvuZqkuVUjlXiyD9qxKBE93-XzJZhXR08apH1wySztd4_8u_NI9MNTtJQQ9xEP4deTWphx4tIDspZdub7b63Wqu5NWBCY2VsZsQGDUV_TYhuYaIgG7N693TCRfyUHLGJpgqq0GobHvi1n6ea5D4GHnUovhaCcK1w8aroEKawo7fK3jtR5b7E5dOB6xMlV9MX-UUfsue9kVzw-NC7xrzb8ggP5arL5heTh2fD_iiSLNC8LNs5Ghk8-gGICVKvyUUVolL62ehax603Z-6rw3qm-XbBs7Zd7LufXtbrQHtB2R8XtFCu6s-OVbpGTiRkhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=DALzq_UU-7NlBYAQ8mCRQDaKSvuZqkuVUjlXiyD9qxKBE93-XzJZhXR08apH1wySztd4_8u_NI9MNTtJQQ9xEP4deTWphx4tIDspZdub7b63Wqu5NWBCY2VsZsQGDUV_TYhuYaIgG7N693TCRfyUHLGJpgqq0GobHvi1n6ea5D4GHnUovhaCcK1w8aroEKawo7fK3jtR5b7E5dOB6xMlV9MX-UUfsue9kVzw-NC7xrzb8ggP5arL5heTh2fD_iiSLNC8LNs5Ghk8-gGICVKvyUUVolL62ehax603Z-6rw3qm-XbBs7Zd7LufXtbrQHtB2R8XtFCu6s-OVbpGTiRkhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=m7ATmUvwfDXeyatSWF9XXj_YsP-QTFt3VJZb8Tj4LmJujeRikUljihrehPnylwuwDqeXYbosT-FV8PUFst4h41rzpl4CexHwbvcGK_LaJ0UcNpnWcJ0KX2graHQywgJrdSgUXVAgQIW3blEDMHrLuecPvF9VhagXDoW9RUHlX-Ntg3wNbLeFci3dr3dcl0hbqGLSNstUeqEWE7oMmfSJ26ZtKVFdaQLy5NYPeTIE4c7jO6GlvHz8aD9OZMsyGBs3uauuLGNx_KiUD4Sh3VrxEcliIv6_FlK34QOfg3kIKX_xbXqWgs63pvgcoBxtlaOu9xf0ubfpDmLgaRn8BqunBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=m7ATmUvwfDXeyatSWF9XXj_YsP-QTFt3VJZb8Tj4LmJujeRikUljihrehPnylwuwDqeXYbosT-FV8PUFst4h41rzpl4CexHwbvcGK_LaJ0UcNpnWcJ0KX2graHQywgJrdSgUXVAgQIW3blEDMHrLuecPvF9VhagXDoW9RUHlX-Ntg3wNbLeFci3dr3dcl0hbqGLSNstUeqEWE7oMmfSJ26ZtKVFdaQLy5NYPeTIE4c7jO6GlvHz8aD9OZMsyGBs3uauuLGNx_KiUD4Sh3VrxEcliIv6_FlK34QOfg3kIKX_xbXqWgs63pvgcoBxtlaOu9xf0ubfpDmLgaRn8BqunBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=XtsuIsSnuO3DFN2lW3jYYuikaU-oH4eOSJDvIxw1ETxNflxkIvmfAqHHWXPwp68HLPQmXeNjh1GJsdEMvnr3XWHuGb4_72Sd94kDvSSF1I8WKk49XFZE9nAqpR6x55bt6OnxmzAlZ0s3e2JoVqWmwIpL5NzKGSZ84bsNFqHdSe74wvPzFVr-jKKkd40gdz-Gls2f0cHKtIBu0rk-G2leB4MlE6EBQpmPHxkk7eS0m4tmw6poArt-iMqBfEWJAc_YqgxbCsqyuWKRohqsKCnEkGHTeCmFVr0DN9zwDCR5hhv-EzxfFVn5jRgqzpjSgeLQM7Xo1deGY2SfDSEgm5fsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=XtsuIsSnuO3DFN2lW3jYYuikaU-oH4eOSJDvIxw1ETxNflxkIvmfAqHHWXPwp68HLPQmXeNjh1GJsdEMvnr3XWHuGb4_72Sd94kDvSSF1I8WKk49XFZE9nAqpR6x55bt6OnxmzAlZ0s3e2JoVqWmwIpL5NzKGSZ84bsNFqHdSe74wvPzFVr-jKKkd40gdz-Gls2f0cHKtIBu0rk-G2leB4MlE6EBQpmPHxkk7eS0m4tmw6poArt-iMqBfEWJAc_YqgxbCsqyuWKRohqsKCnEkGHTeCmFVr0DN9zwDCR5hhv-EzxfFVn5jRgqzpjSgeLQM7Xo1deGY2SfDSEgm5fsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=K_-wZK9_dlLWACBi1Lnv5V5vqlRlv2ktF3HfDmXwKfYmui9W0E81WCv-phkNmZAjP3NtJcsE_umw-1HS_dO_jdFnibaapqHBwmfP5QNSNcoEK2VhnKI0btFhw9gEQI3NOiWXQMyjlbMlghps3f5JIWmX4Vz6Go264BE8Sp_oDe52Duprm2AkYgLNIXT1U7-iI7YYS4pOPsNrjiAIhi3O2lcPkdz_dp2DViwaHisKj4l88aECiGBtNk4jwmOwJ9wxU-Rmkpp4LCXAYpY1UTER2LWUQ5jslRKhRM3YBW58UZR2kzmDgVPX-blpIlncygAQ9LUPYDYJSYC1Xvpryb8LWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=K_-wZK9_dlLWACBi1Lnv5V5vqlRlv2ktF3HfDmXwKfYmui9W0E81WCv-phkNmZAjP3NtJcsE_umw-1HS_dO_jdFnibaapqHBwmfP5QNSNcoEK2VhnKI0btFhw9gEQI3NOiWXQMyjlbMlghps3f5JIWmX4Vz6Go264BE8Sp_oDe52Duprm2AkYgLNIXT1U7-iI7YYS4pOPsNrjiAIhi3O2lcPkdz_dp2DViwaHisKj4l88aECiGBtNk4jwmOwJ9wxU-Rmkpp4LCXAYpY1UTER2LWUQ5jslRKhRM3YBW58UZR2kzmDgVPX-blpIlncygAQ9LUPYDYJSYC1Xvpryb8LWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCo4UTujhMTukooAzlWzTPRj7aJlLAmar7_0V3Skz47GhmWy7ok9gFG7-8nDGu4NlHQMJdtMEELmoc1Q8OtkvFUdJeu26ZlNo2ygA6atUXKyyWteLZugsmvZiuoPLLLM7YOoSL8lsTnvgNn7afi7JRyETOtVZxUNIqjdFxMaPNOcDlSicTsPC9bqNTozGo5nBwdzb1b2Mh24K2yATcJaK6__O6-AtmU-4t13VODvJwN9yENObbN07nMrEEeonLl1wb62vo_WSb4aExspx3JhBiuC3Cd56c2s-JU5xqlhMLJ9thItPTUl7hVfjG42JsdmYhC1CeZBsR2-B4e4CR8bpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=T7-6uj-S9iFz7UJbce0BKzD_6hn1nE6QDZuSlsW21oejGBoQaInXfPpcUhnjqQqU-NCBZ_oAkPTkBr4NCxLDbt1s85aIp3Ln7Z-5I3H186A5W2gb5cBO2Y-zSxU-dWZNucwQRkmMeNZpJOvWPl9wU28D3-S4IOtBT7puXI_dE5xBaqbFG8vITdidewKgnOecheCp2DDgW7tNrkXzmo6NQgIH4jm9QnoZKPfhY79RwXhsRpSHkP09EbipF9COUoiBNFZpSfiI07s5xLCqIBgf8KNjeRlSCMszjPVF4g3skj-84qqEAeuFIVuZxDAgKYJkfb92hx1mDxRmGAzygx3wvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=T7-6uj-S9iFz7UJbce0BKzD_6hn1nE6QDZuSlsW21oejGBoQaInXfPpcUhnjqQqU-NCBZ_oAkPTkBr4NCxLDbt1s85aIp3Ln7Z-5I3H186A5W2gb5cBO2Y-zSxU-dWZNucwQRkmMeNZpJOvWPl9wU28D3-S4IOtBT7puXI_dE5xBaqbFG8vITdidewKgnOecheCp2DDgW7tNrkXzmo6NQgIH4jm9QnoZKPfhY79RwXhsRpSHkP09EbipF9COUoiBNFZpSfiI07s5xLCqIBgf8KNjeRlSCMszjPVF4g3skj-84qqEAeuFIVuZxDAgKYJkfb92hx1mDxRmGAzygx3wvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0cEojWTZGfaoqnQbJBrYOF-GnnzIx_gfaEsvEpvK2T5HDYJ4nQeag_jARGDG6OtICdI1gYJ3GSsjMlu7Q-BC9Oi7wAN9AO5BKt1Vp0-GduWUp4l2IwdGF891M1mAIguYfqatvB9BNfVMDP3kF2TfTb_7JNKLlgA6eYvNpieEQk30hhYlWYyX5hG_YAxCrYfRECD75vUsuPJ8Bnkvn4apgaDINYt-gIpYylmSh7mnoIBM4S5klzG7tSmlUO3ATw5_OoIa3UfIkF_OM2pEO5qPqegnNDgxs8qt-uMRHCwc1qDz5nv0UQbNYcvUYBH78fTfjgovuYN5_yUBnlVdidwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ElvvvWVqrqszIbl9ZZ2ZFNmdfJR9-FMHm6w5L0GANEzGEHQKF3ggwzqx1JKOQ6alxXafajfHWg_b5v0A7deg-i5bq_Y8FOIjcxCg7qPGRTvPGUkGHaksauj4k1ydSaeVddGN8QaO3jRSaCRLvB3PKVXh3Gm6xY5iZor9pv7tO8SIfWBuUfCt83pH-48Zr1onHIBzdIK3zlwIQ8N17tLcFgEbgAVv6Px7kkBqsu08YxzzAPIrCgQregy3DmWqZ1rFdBhy0iDISzQviLrCQGNZ2_IVKqrHmqGnokl8VxtZZP0BAMJ-cXpdpM71CWW0yF0hkbexps4tZ-qWUqzgiTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sK90uVBlDw5j-Z-NuprmxVSyFbRPbuqFihkm2aRXCXgDhw6orWCx-0-gf9ktIZnRSC2ptMBlCRdybE6kWGH7y2lywHgJtikYYr-KprCNMpIbEi2qiXsrZuchpSwvew0YYvVhW37PoC2eauneaY17HHTZO2W3AOhfg7YhIGkhxffTZswq_0eZdz5f-X1MRnEC7Yx1aExqCYt1t9rRx269J0ZDSK_aeoXFVMt-iS7v9RnHz1XNscIfF0UqQz0uZO9wP3kxlcpIrFge5MtMlUAI32LAvh8kRL35VTww8Lprytuk1A6TlM9nInPNs5882bf47JzaYuRH4SEiFYkpvR36pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZvQ_dLDyP1YaLZ5Qmymndrb606rurx65xDwTu91cYH0a_gCF88L19JZ4PQSThauq82i-1VNuNb7J3JsLPIdDGjVqr-h4p-pCI1qnEcBFY5ge3x8aYdWGfeWzS3ZXWrMHpm4JcmwF0aM4g1AzyafmhB_o9KkGsyQ8gsR-9S36WWTepoksNSinQZLD7vhV6TTu2vmcYZG6JVvM5AmqNox_ZV9QuemxMCwP1OO2CJHfxak7dRlsMjbm-if-_R7_Hml0vv1XVkOmFqHiWGHlCuP5bFw5m72wkCyq3VOZOSG8nwZU_ioa-dIaBFuE-exfJonkCsk4h-3W7ixGS5Uv5AWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=Ri4VNQoFNl0YZ2xoYrjxvdpCHmoISNeO6nY16tsBkvdP1zcsGL0lf8jFo0cfxN0XLPOzqDaQjiwo30BC_ysB5FlzkuhTzz927XHgSnTsqZdspZgAtZ4miNiuvmPTvLmbdGqTCeh6-hgvBZ1Cd8TD5ZEqRiXxkjuxLPr6Q_EgxJoStxPaeKOPdg_9eVA3baQhw771qO4iRf9gjunbfHJ1LP2nZRG0ZZ_X5ULKiEcKSa-FDouWY7hEz9qLhyukWKldvWXJq1T8YHhLQvQIfZ6NQEtf0bGXsiPNbkdO5iK8PDVgMuReimcPkNHqNPO9YaIEl0XSpgZLydLG5Gr8SodPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=Ri4VNQoFNl0YZ2xoYrjxvdpCHmoISNeO6nY16tsBkvdP1zcsGL0lf8jFo0cfxN0XLPOzqDaQjiwo30BC_ysB5FlzkuhTzz927XHgSnTsqZdspZgAtZ4miNiuvmPTvLmbdGqTCeh6-hgvBZ1Cd8TD5ZEqRiXxkjuxLPr6Q_EgxJoStxPaeKOPdg_9eVA3baQhw771qO4iRf9gjunbfHJ1LP2nZRG0ZZ_X5ULKiEcKSa-FDouWY7hEz9qLhyukWKldvWXJq1T8YHhLQvQIfZ6NQEtf0bGXsiPNbkdO5iK8PDVgMuReimcPkNHqNPO9YaIEl0XSpgZLydLG5Gr8SodPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxJcEd1Og-9OD_aNBfrHXFyJ7WMaVxX4SwfWjike3iEBXVOsHH5BM3qliS9-BJX8yIZMrTjtPIDUYFtvYa_bCw7rSEsvKtsIFpbcSG1C_ZbCQCujsJsJVU27-ucl1XKqlWGea6HjFNIWyL4T_3Utow1ZbIh_nEQztPD9SEdbhM0obDKzxH_-p2RlsO3TUXSe5UcFIb84Is86zbAJkcB-N1GoSnIWGolp3xLRrL538qK8uAW6O_GlwoXYnGJpioUX10phOrdAf4y-ZskQuTtrIv-O3pLkvTY-LRCmTAUcoWsr44sWdI5etpCQUxm3WckNzL0jnK-CYoRXGA6fptkJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=lQPuyMK634fVRKNGiAqyRzJuBCWis94lWoInKtjcrqqy9eCTtPFkiaOHLHAs-ZUpdewoa2wy9uBf8uGbBOnsV_9v9lL4pssXrt-VWVDi0F_cOaYYBTjLwFes38XrsOBN1gXBMhaFad5Yj-vIVvv7k6-sKNB6dnaN1XBLXzEuXAwg_sxokjUq4D7nqIVsdkIWmvIKHC9wy2OBX5UocqwQ4LVFy0ZQDjHntpKG9odighaOGmYOBidvxlO8ON5sDFPpmJLt6mGIzWABnMd6TthB9w_6eGUA-eZBUZ4vwxPGSosiCqLQEqvCUERbFeoeBwB7_cBxPEsXBesG3FylKK_fNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=lQPuyMK634fVRKNGiAqyRzJuBCWis94lWoInKtjcrqqy9eCTtPFkiaOHLHAs-ZUpdewoa2wy9uBf8uGbBOnsV_9v9lL4pssXrt-VWVDi0F_cOaYYBTjLwFes38XrsOBN1gXBMhaFad5Yj-vIVvv7k6-sKNB6dnaN1XBLXzEuXAwg_sxokjUq4D7nqIVsdkIWmvIKHC9wy2OBX5UocqwQ4LVFy0ZQDjHntpKG9odighaOGmYOBidvxlO8ON5sDFPpmJLt6mGIzWABnMd6TthB9w_6eGUA-eZBUZ4vwxPGSosiCqLQEqvCUERbFeoeBwB7_cBxPEsXBesG3FylKK_fNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=JgtUWM3mXR5mLJWWGHPkOWqadb26ZsEcDCWyjj_7IcPEYmM3P4PaTwg1--2jR7UJfcF-e-_gPT5cGVGdIMtbIVDJk_v2S6nD8FzeTpyW-Vq2p4fx7DNt50F6FeVweWCnIy_4ja0jEcWyqdekKiJOsjra2KVsPowqJtoyAMoX4vwzewqN_zu6C0wFxPYvJWGPDk8sKybFDpikynRRfcSw3lpnbOsmM_AmOs_GPrXgSUWZTTnZou353TySuNh1zK94ayVHD_CblARX-6sk9BIXsIrPaYGgfw50iPnLLvSMZ81Wqso8afqubHzUQtSgbCG-qlzv8xVu2uQoJjvQFifAEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=JgtUWM3mXR5mLJWWGHPkOWqadb26ZsEcDCWyjj_7IcPEYmM3P4PaTwg1--2jR7UJfcF-e-_gPT5cGVGdIMtbIVDJk_v2S6nD8FzeTpyW-Vq2p4fx7DNt50F6FeVweWCnIy_4ja0jEcWyqdekKiJOsjra2KVsPowqJtoyAMoX4vwzewqN_zu6C0wFxPYvJWGPDk8sKybFDpikynRRfcSw3lpnbOsmM_AmOs_GPrXgSUWZTTnZou353TySuNh1zK94ayVHD_CblARX-6sk9BIXsIrPaYGgfw50iPnLLvSMZ81Wqso8afqubHzUQtSgbCG-qlzv8xVu2uQoJjvQFifAEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOBNAZfYJClJ0nZKkWdD4rbe5lYzDdh13iCljncAzJ5YluCPjycoXjlrv53zXMwI4EtBpEz6bqPSd-f8g_YO3iYgmlzs_XtF6cEXHV6ZiD7l4GRoJbus9GbFSeTOVw0KdmO2IBiY-MnA4LTt_-2b77fNhASkjaLf07KlG0wC-5qp8CPYLIWyOjDD9tVzLiISC9bY7HAteezl-arQpq_XrtNETZx0fuWcBsSepQ3PmnpO8kcOzG1fcm8_Zk6W-e-sgphIqttizp-aH3JeFPWFBTJ7fN-OWTy5CFExof4IbbcXTpHlCNmkTjTrm71eT8u4C5ePgUV3nTQ-qH_QednL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdelqNblcIUQcS4Qb5Iot93hRh7wF8JJhIB3nhrh4Pd2-V94k25ymIL-T7XyxFFlZeXBP70Rdp7MW-nQVimAqj60wwkOdGxnATFEDS3eJTXGb0fpAMkxhdK1Hy5pwnH5q6oEy7CMB0vMJWTQ5a5hCHBGvsK2rl9SIZwlaNg2TF8G8VbADeodIUAKRHUMny_klqLEgGFrI-HGfUy6vjqEtZx_ra56zM_LpkElxEIvsFzSa3lI_82M-VFWnM6uC5ih3igp9tyvKoA68DRewvXpy4V_F0j2atRYK7rWUOBIMfVgrxJw4Qg4GbtXBLh39SCzA6HEdPYK4iYiK0ERhuZNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQVgJAa0zGOSpvVZ3mw36PrpmOCml98YcYvIVBALxAdY3X5TEEeHBwfliRTDx_M4PKQlFmPxyCXiN6ooqxVK9UTfxtyfjtAP7xhaHjRsjMLUe6XN2mwmgebaWWf6bQLboQ-1hxLvMGmCuMEFVT-rS0VnHQnMhubfufuEUToTqaNLvtd22C5Fj_zbs5P-fsIOFptGYm-zIjf8ewy6HJWBXY0Dv5PGYRRrQBGzGwMDbDwGsSgvN3EqiD_zDuV0rUcSPNAnasPzo252cpPj5HfI8JxtPZyE6Y-Tx6S7bV1eFsoR9skfHFRnz71fEyCOoYBU0mGgM8svEIm7MVvlFeMzzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=dGyqyxat-544sH8L9LMjeL6gD9kJFshPUCfck_f_Oyj6YNJKsj_mSUgH5FD4bsaOyjg0weTMCmErzfH1WNhk2SOsanL29hwV9Csz_Txn02qmoKh4hikXIgh8rYQ_jqQ1EjlLfB2wFGstEGslKGhipBp8tep_OhQZM-MYO2KSgjVYY8NQq2ySc7jOxAgeEkb4GrTiYXYn1_M3WbrRmOS8W3ZWPhAaP78Z6Vs82JmhAF_9QW7sf_ZEqxXOOtJCP8hzi8yCNh6vsm93DxmeszWCG9VQBLQtANxUrSOGKbV9G_E9P4TgIJNOwGV9ehJLsZleMeKroGkEp_Gba9HPvp4WZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=dGyqyxat-544sH8L9LMjeL6gD9kJFshPUCfck_f_Oyj6YNJKsj_mSUgH5FD4bsaOyjg0weTMCmErzfH1WNhk2SOsanL29hwV9Csz_Txn02qmoKh4hikXIgh8rYQ_jqQ1EjlLfB2wFGstEGslKGhipBp8tep_OhQZM-MYO2KSgjVYY8NQq2ySc7jOxAgeEkb4GrTiYXYn1_M3WbrRmOS8W3ZWPhAaP78Z6Vs82JmhAF_9QW7sf_ZEqxXOOtJCP8hzi8yCNh6vsm93DxmeszWCG9VQBLQtANxUrSOGKbV9G_E9P4TgIJNOwGV9ehJLsZleMeKroGkEp_Gba9HPvp4WZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=VvtZQ9PuqWaoyepN02Nm2jHcq_mEf3P6j6R11iWHY4AXsWSbwWB-eB34sQNiTqpaUwztXCv01YGKdaenHitEKMT6PBrn36CmLc8sbcOECnd9RPzx3C9fpoYy6Xmax4wyzF9P2qIMj8Da3ouNbKeoik1dfsUN110RHOuwY4CFE8GoA7G1tq--L5TEGrr43L7UaBB2se16WnQG1O2UAlzyCLdxtYoY85FvuRRNdO2-IHrtB4fTkuMjOwtMIqalG4TvlUpmKhFc3pLfC83OpQm-0dghZtFvupBAJvlL2zdkvtgJMym321eiNt0Akku2UNo-eDRhLsdRLrroG-Pd5qz6yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=VvtZQ9PuqWaoyepN02Nm2jHcq_mEf3P6j6R11iWHY4AXsWSbwWB-eB34sQNiTqpaUwztXCv01YGKdaenHitEKMT6PBrn36CmLc8sbcOECnd9RPzx3C9fpoYy6Xmax4wyzF9P2qIMj8Da3ouNbKeoik1dfsUN110RHOuwY4CFE8GoA7G1tq--L5TEGrr43L7UaBB2se16WnQG1O2UAlzyCLdxtYoY85FvuRRNdO2-IHrtB4fTkuMjOwtMIqalG4TvlUpmKhFc3pLfC83OpQm-0dghZtFvupBAJvlL2zdkvtgJMym321eiNt0Akku2UNo-eDRhLsdRLrroG-Pd5qz6yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2zR3u-Go8ViUG2GvlttoXOMobFd4ov2qa5gpFIcCnd67WOEFDXo2pwsRyL6MkEXgj0_8K33wjhDTZyjKMb6ELeE0HsH_4J40dMsLfNcnlCVQ2VjIRt_GCyeiOZ1YXjnyJWW0EkVn_2qWAe0W2ZwGp1dEiOR6wM4Zc1VMQ2h1P76GRp190R_Mjwc7_vxqxvSQlEjV-N7pLkm8oWbRHbw5nn41yTmtEerbG5dU8IMIZo6jv3vFuASMqtFi9Qpj_idVYh8X7GZUHADcxqZu0LALhN2aw9ii2kpbVsdKIm-xU0tOlOLRcTMxlBAqFsI7zTXNNhyejPCcFYYkXDAzJv2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcPaRIOXdI7_QKJpCWoMpjgnNzBswtbao-6EsOAsr_5Fp0SpNRTCFQtaWlhLFMOh2d6dfaZToyXrfOuPRMoh5qlvgei7Yx68EoAbNb18bcilPCjumken6n0W56PHe6feza5UFHjnO9FCF0rZWKgTtiat2SK6vxMw5qrrerJWnJxof2ZPdHMfoTOdWpwkYBXyk69FKDs97hltiSBdotKCSh2i5qEhTHY5xvOSB8FXZl972Nati5UBWb51cRBHARe2AQTa-7POQU9Y7Hvfzi0a9RV5JPDHKwQHJ_wlCJTij7MTqSymNFD1ObzJoEh-Wjz5j6EwNGBNoczcYhLojX5suA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_BZIgOaN6eZHYCo0EZxKLr52GQShG2KeNuHCdTzew_8Pd4RctqXe1ekHFrRAkVvZnQyxWG910bCK0xtC5R6mQH18gGtsk7VO-TR6Jqi2IoblNTwUTQDnnI_jOqmvtjPbWKzgbr_wFIwJHAr2pK0WXe8M5v8cwhkYOd-FrBA5CgH0nnXTv8Hsby1GER5subq_1DaZ_fIR5x2cMfeIbMXalrrYzRJF8UPn3kimuIDfErkM6kX_7NOWKAMXHRrilmpc3yblHhJlUJI90qpmk2euumFPfV9Hvx9oJUZ-4HT16vW0VWl62MNhrjZPEtpwzqsAtLzq3GkpFSczZ_MCEEQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkikR6kRg0o6_fR4Cfa_g__q3b5VXL1i2sFZLQ1rwJyq20kYFDJeoOdnNtCJ373s0QwGXgG3B10n3Cz0YenRsZH4UirSnvBX6Xj17b9eLWnXHTSt4GdP-LFEgAVk_QVqwR97DzM933fF5SPbdEVyZ2coRsR8uIlZ5nas-9b-uiqEoeHS9RwV2g9HOrgctmQKhlCO6ZQEzMOgN3q4RZkk3jAjhlEEjMZGcfHfqEaOh92VV__S3bfWSo8uotuZrJWlxvcYFWLUjBuy88C_9BgKZSacTTzeK7MePhEdsMTO5heLsD6DfQv9dFY7TBcUidFrP9DtuAqgTDsiWcYkflYLhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jywtGZAMYXa9gL2v5_gdbiSOW1AUgGPoI1F766q2kWPMegLc1BeCDx2NV-R-pmTwxm9UUiNS0-9D1zVoIhSQzPr0_qFZfbIW7Wx5oEiSmig0JaKMtooDEvBL2t0atvZfyTxU1HMj2dFjlnbpE636cxwSRYk0bB4-k5wJ5xCKnyjcL__aWpLUhwPWbAlap6l3_k6bHCxVK-U6DmDuPDdr8Q9JaTdWGaWrf51uYRVMM3Fu0qGAkiT0jTYRmFJ20IQ4vg7e7FHtpqcNjQTBpApWIqlUdIOUBO0-w3Izn9FQZKVmKEN2-8-dwveA0Wcl0F89rRcNaG4Xu8QIRIeiDbRXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCEltRU17BuopDsz3AEShsdf5MoZk46e1R7FQnQ0hPELPusdQ_pS6Nvo0MN23g9wp9Pw0ulbVGi2QL7zytjUADfFPVkSjAtZj5T1vWWIujQIpUgAqf6GEOBvR2rpkba75FEXWdGeGJytAUArRZzNOxZr7Njojo8x-oOsaUyl4gSxzUoNEOD7PXEwwMum7VdYdzraaXVsmAhQT2wqoJEmRD5CosW8TSQXV52vLvDeqcySp0c0gTbpd6tKn6UTERazgu3YLsLv66Bw3Bqb7oiTW8aVVbT9qh_2uB40EKWHViYqpVkxkejSDpIvN16ykDvGODohepWZK6Kuk9iLaa3ksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMRa0JkUbwxnkuYwX_pDV1dcazJUwtt7RCeHmOF0mkKL0Vs_cCYmHcIWNEUjch0Yo8dGQTUTa0AuHRGpktkRaNLQV2b0Q5mQ1mk7fEoWw4wfSZc7Si4S4-jlJw5fhXOx4sFbLCDwz4y9aIB5EcmqPVFrEGCqL38iv4SO6b2WLGpntRSuw2VdfDiTIvzBAf-kvmDg01xYnWg3VpwpyD8uXxW1E7n3ucQXO_OvvlFNNUZ95gYztveSfKGLX5PmKaoJ0WQay8YNcFU7i9HNbOj4EtA2b3Bgr8uvi_QUodunu7J2iUzzGCllE7CUcGE7fYAnScDHS8zjosKejceUWiyqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFbC6lDsLX1ZLpNiJgmPuplRveDBod2GgoADoG1BDqAepm2cCoKjDIhcQ_63qmycyOFvJvBCS-4icySLI8OftNlB1ii7QtHUwJmpc_G2uttkjdrsZ-cN5-YSwqhh97o_HkQtJb9iryjcGeR2Sz66Asi9I83kRC1ObUuEm5Usxo1BT1c2OeKsDy7_M-0ASsX--hMT9p89mn1xRmSVsUe2pzUioYIBV87ctYpNTmhECWAFwL_Ryv3HV5Nk1hJSeTHJo2G_7jaONM142wA5mBemGGvZY5g6cBVjMMzyX2tA2WwH8zeKzMoclPlMJBwlbJAydb2JWHhNCUJ1oArC8HFt5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk7DDdHFNUOP0HFGg1Px_9AhZ3CdFl-dFTcWep5Ewurqwc5yhIP1WkX0L1Pe6mR0c3Ue6E_3xUERRf9IPJURaEHPJjwC5soTlgNitS3MA9OXJ7wYn-8Hg_hqULpN379JWumaKraXE8gqQgpRtLnArgp1mwZ9e1xCTQU5mLs-SDHMkEXeg_Fub1gCwQPrHWwXrczCbJqitl0EdKuTt7ySA0Y2IjpgwldJHDF2sWT4qPs6Ve89jYnmZtjc__2WJBveEYbnQg5Bk2SUfMriiWasxvsumCAg5zLigHkY9SL2MMn6gaxrMplMSpJ_UjjK6U6IaD7norgETAx-xDbWOKtw0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=JjZ5piy0dRDYvj4OMRGnrblpaKybPDldjPsVu2mIeHtKKX05Oj1NnDaGAjsdb-8yK9wXqYYZ8k4RKsgtI90Wl9Ynr1p8TDjP1OR4bzhsjNz3wurjroO7gOss1e1zrCaqL3nrVZ1FL-36mqXKQz-AZRBR3SZFW8zKwTkpxSWrpihYlKVrkhtBLsJYVj_1xOU4ykPktfKlK11Do_v-r9kJWoVFsFkwaOVOyG_8T-57nzcs5W1uVjSy2tFwIIcuaqHqwnTC_zn2B2gEKbTkjoCQkpKqeBvABrx13JRntBTcavwkgD_VqDJEPU_a1YP_lGISedk9nciaawjEg-P41vLID4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=JjZ5piy0dRDYvj4OMRGnrblpaKybPDldjPsVu2mIeHtKKX05Oj1NnDaGAjsdb-8yK9wXqYYZ8k4RKsgtI90Wl9Ynr1p8TDjP1OR4bzhsjNz3wurjroO7gOss1e1zrCaqL3nrVZ1FL-36mqXKQz-AZRBR3SZFW8zKwTkpxSWrpihYlKVrkhtBLsJYVj_1xOU4ykPktfKlK11Do_v-r9kJWoVFsFkwaOVOyG_8T-57nzcs5W1uVjSy2tFwIIcuaqHqwnTC_zn2B2gEKbTkjoCQkpKqeBvABrx13JRntBTcavwkgD_VqDJEPU_a1YP_lGISedk9nciaawjEg-P41vLID4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ44Cs_325VPrHy0K081fDpRI6Q2dof6eq51Um49IVSlC-8Qx40DXLr7CauKhpDqebbM6uIjW8Nz6ET3agB7-ll88GR8tH33Zx1qMer4KNmR1sCN7B04jhm0hNNE1uFR_CxOsg-5TWJ_zCi3OuvMkRQjiQE0tD5lQgDHPyF9-7LU81dnABkaj2TW5ZZdjmbA2DTGBray7f1tFvePBqLFGT6GavXYw82as63XiTxV9OY2-hCmqik8NxAyOcdqC2TBpajIS_dFWfp0P1U6KMDogonsMwOxOKVuOGEd1kQcYZ0EIqAKOG9XY0yAJyAyTIeH5G9viu7Dot0Xt0-YbwQH1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imHQG3jko4fFnAyjiKDSTFXwu5tLanZwOB1-bdVgxTtgwTr3RDRBznEK4elsURGBrlwdLMmrtGi4XecOsMmujKln3WpDUAf0A53tUvf6fs8a1uZ3i01HgNIJWEzzPIwtum_PYxKlF_uaZAk3plUf5-x60HhvAcrz1yXu3a58IaXMhpieoXT_x26gUvRmCQtdREJts63DTRXu_owf6x-_AUISlUbnfZrjL-czZmVUGj4Khn1zpIr1Ztj1uWRD_WaGE8NyMFc40RuIM2oGtH4gY6KnZypDlnR-BUsyfBkNt5CGyQX04Ck5hXreivKh1E6BPQweSxL6XzN-xoS9fmK-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oARlkX9PYNoI8IMHrnWsYH1XYcvqcjUX3PbUI1-1HCIDTFBu3spbcGl5ejSdMPdFOr0wHJTNmoYEfn_FXQi53Pey41eUshNi2DafpCyaiwtYMdPZpBKxoxUN74N4UB3eeFYNVMc1RAgxUmxkc8rwOUw7Id3W65Dd7cdXzgz69LAEkRenvqd9smDKHqFNUwuywuC1YfO6dUVzPQ7PfEopQkM8C_0fhL8QQ9kh9BxVIY2gDQ6IxpLkC5iGwtTFRIdXDPJoea7tuRCl4SkM-asTJXB_YpfNuEz297DKxCIFQLs-0AqJRLOoDSX-DyFCGDD6dKxHo_1x67Jl2o1XVvbk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGCmzqIyVIRf39Nsv3fbWXZ3WaJLqpA9R0GJWM9LcYZB0o_BjTp6KlXNPJSaLU3hsmVNkmL722-WeHSrChs_KBbtdkhXy5nz_5-kWOQIvzTBvEayMKAS5f675r7P-p2F1tshWMTIPlQsm_eaD2yCHNpYzrxyrfBLphE-sd0vo-NfBn0XESewR85D4kL184vcZymT4Hz1AqbOhEy0rPEikl3Axofy0SD5ayN_vJF3QiGHvB8_992ugA2Q7E8DkEbLcxQH8KJPB1keM5RVvztasT6GxCOdJ4CRrUH3CzOokkf-SOLm5IiP9sBWhB-x-ucKlbsLWTVnZiTaH33ohi7K9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceN-XkiOfnOumHAdm5pTcSFS6-FUa5mN3FdqrBiuROuW1qh3UjDW1hLRIlMj9g-eZjS89UAQcXRH6XlGA-TYVioRmisYgeRCGQrfvVm0ZhKAkt2IjGLQRpndwFhuhHt5PFLD75_-ce25IQOR-vV_AuWB1GqKrE-vkUaxU77J7qcFSgwLYgSQ5nKcxWR2U0CMiIH7ni0LQ5HHYSJRXOjfF0BqcsTtlyiyIEnX9IN_fMvUvGuSAIjuO-KRtxRnsv8EHxBfIeAagsV9so-D0eZwyyvpsMMXH1OVXom2Tvkwekf9LSZ41Qb3ugJpYezJHvWtZU_fKrUuLr7mlU1Q8kikVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ayBAL_tMJQ_6-dAKinuEcbOWULvEjYShqL6JH3hv6OqJbZLv3qfYCNF0BnczQJZrARxdNRPMZ8oCg6gJLGSx_-a0-ensqi1KPY2pOn6XyjRwCI5VObQ7FLeJ6CfTg33FONlmNsDgbGRSafBYrK3IGFEoT5qpN1OaOkXsm8rQCyOvjD_rTFdm4h4LppCTNOvn5h1c12ZrpsVQ8-o3rjHXiyGqIuYqEd0Az1pAurpPVlkSl2f0AoxZH4mVRWkJx4xZtEaEYZo8Cxq3lFlOWDSY5tYoUkppCQU6Vk9Ywp42LcrVZLpQ7J-t4efTCp2r2VPE_Jp3KeiP0_Dcwl0uYn7eeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjAFaJ1_tBxdqMaPBn9zK_tj1Li5xPzHU-lMC1AP0qDg8hJklaywrPiBV4nrvCN4GrBbuUtN7ee1juMO43HoY1AfYPaQ02_kPX2OOaSmRl8qNPyIrmBWh1-hsEDGt9fOO9MndwswfNrpEeKxiIuLDsrInIHuPbiJ2b9n5uKZJKdjqYPBHKHQaSzS5LKZMz5igcuyM3nCEgb15F_efe2ojH57Yp42P0Bx2v5H3K5kOWE_Tz_aMCE8VMXJcSUjaWM3su37CprPBdDto63Eox3EiM_Sr8kjUaGo4yJGy7-Fp4nKPI6GhfCmq2tBPJ8dDB9G4LSgOg8VrtPtrhCqHQ9Rrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=GAePzaVtmGG-9CeyfRHE2EL5phlmU3E_4FMYhrUBywr_-6hSBsloKP7ew8vWyD5KGFleTVVh3C1vpEA05ZipZEZPqppyoplH_dShcUsDMuveqSUDtg8L0jei-xQ8Ve4C8eW29Q25Gx7xN5CWm2b20BhiiOfZZWD1jAyXjx_U5DOLeUorxteFS2knBBjrpevztFdYr5i5znwCRqndT5GdZoU10NpO36eyXInycsqaakeKdOWTT6eanTEydNDs8cylZZYZwcmaouGz4tJiJLhqeevjrtVoXPYzKd1WWfQcXvPs9tPAuudIrP7cTQQ8DjOT60YQQ35vNzmkEGWR0cSD4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=GAePzaVtmGG-9CeyfRHE2EL5phlmU3E_4FMYhrUBywr_-6hSBsloKP7ew8vWyD5KGFleTVVh3C1vpEA05ZipZEZPqppyoplH_dShcUsDMuveqSUDtg8L0jei-xQ8Ve4C8eW29Q25Gx7xN5CWm2b20BhiiOfZZWD1jAyXjx_U5DOLeUorxteFS2knBBjrpevztFdYr5i5znwCRqndT5GdZoU10NpO36eyXInycsqaakeKdOWTT6eanTEydNDs8cylZZYZwcmaouGz4tJiJLhqeevjrtVoXPYzKd1WWfQcXvPs9tPAuudIrP7cTQQ8DjOT60YQQ35vNzmkEGWR0cSD4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=IsylpUOXCvpI3uz9jnNeVkGofqYBqnliH9Jz9o1pbMJ6Nx2tG7dLKmUjhfCmXWmtpkUnVVbhKfSmNetN5XmDgXa2UyxE1ipwM19Fq5pgs-v8zUXj970uDWmrhXEiT9XpFmVbUU73L5p-o9DamdXtyvDRGu_jTwZsH7HEhnuoRlvoPPeu93TnK6ReTPrCuoHcLsnqGY8vvEoqxNomBo1yZPIuLyaPkbs1zodrIIcM1SBGRyAp_WYJu7SJ1kjEbT-iDKT8ZW0APSbVrQ3265rleZa1pPcEDyGtGltAEfm8Opd9kUCts7PKWDPzMidJWOvZ8XsMXjNE9eevk5uxzYXEwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=IsylpUOXCvpI3uz9jnNeVkGofqYBqnliH9Jz9o1pbMJ6Nx2tG7dLKmUjhfCmXWmtpkUnVVbhKfSmNetN5XmDgXa2UyxE1ipwM19Fq5pgs-v8zUXj970uDWmrhXEiT9XpFmVbUU73L5p-o9DamdXtyvDRGu_jTwZsH7HEhnuoRlvoPPeu93TnK6ReTPrCuoHcLsnqGY8vvEoqxNomBo1yZPIuLyaPkbs1zodrIIcM1SBGRyAp_WYJu7SJ1kjEbT-iDKT8ZW0APSbVrQ3265rleZa1pPcEDyGtGltAEfm8Opd9kUCts7PKWDPzMidJWOvZ8XsMXjNE9eevk5uxzYXEwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umHNcXOzUkGe7yf5uBwgcO3Uq6DfuWU9oUnf3VIN4WFureIc--3ZD-1EwJchbNB38DISaQP-UO0bmNKld7mbLQnGDMJD82T8Q3t9MxSITXTgEz4_UyZQQxk5MzI6ZYNI1tL1lmgFxbeK57zD64BY3qo2cY2KDkeuwiVFjJzwYKcm1dJyKhTOR-9uUGGwss_LcTvN52ao1YH2JOM2MnMhn6qEVPHR04Xz0QH1TY-xvJq4n7t_r-oHPVrus8Q0w6crznppp4B7dHyE03OHCpxYF3Nt9sfljBauK6oDDb8r2HvbsIb6mXRiPpDz992b-b7vw8pkaCynZB_lwa5IsDQlwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRwYdkylA3ZrJu1rKUAZrf94BEu-wGsz4DnwAX6UIri-hmy_zGgFB6gmx5TxDpEczX-a22mMmZL6lsh5Oi-z6XO4hEzhuW9T7VRrJGpXhOb-0CRqRCIG5AzjKfeaoeDDogqougwAuVZcnPeXE2-rh60BZORSEx8ItOIb-G2Q1FAewzz2rGfxJ6FPGDQ38BKb6TqobS621SsKAn-_qGK9QL1KSYZq0VjmmliTfzBo_ZoooMj7UwdrhfpWEVrHUg9JAiCP9Ctw4sS6iTZALdjK4e9h_wY7OhMv-jpWcqNq9hfLqafCuDlhrWMNv2iTY11uIfJ5lLkAeXEM4QvPYSc6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=LNqIL6hkvnG8DlJBuKcsBpm7ILn2koo4okLNyJjaljcB8dfEk9meHs7ScAogdoKi2PwpQPIBvwu1vUxGLJfol9664gN7c5pkJgKk0X2MsWbdu1nUCy5nY7KpvM4d8rLf3qrQw2mgi3MJ9Jk-yU8f_PDJTgQIx9s7j8MWELO_6jWCemVFQnE7ICgGPu5ZvQ69rknuU5YVqyEDp1XE_K7Nnk6QAmj-A3TodST_hJ2CEYJ5gOZ9AkzsMKWWZNRVYutoJBxNxPHXTXrxwqXKbOzaUobpE99aYArJDpToVbl6qLanrQn4OgbKsgyu0EB3qUXeazdlzhxb3q_41GG2ahz_cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=LNqIL6hkvnG8DlJBuKcsBpm7ILn2koo4okLNyJjaljcB8dfEk9meHs7ScAogdoKi2PwpQPIBvwu1vUxGLJfol9664gN7c5pkJgKk0X2MsWbdu1nUCy5nY7KpvM4d8rLf3qrQw2mgi3MJ9Jk-yU8f_PDJTgQIx9s7j8MWELO_6jWCemVFQnE7ICgGPu5ZvQ69rknuU5YVqyEDp1XE_K7Nnk6QAmj-A3TodST_hJ2CEYJ5gOZ9AkzsMKWWZNRVYutoJBxNxPHXTXrxwqXKbOzaUobpE99aYArJDpToVbl6qLanrQn4OgbKsgyu0EB3qUXeazdlzhxb3q_41GG2ahz_cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvGCIc_fAOy4zsoZ1d_hl27ExAqKq7EBHyUa194ss4AnMsLgyKyEnYMN2MOEvL6RhwtQWGJajFtWuPwFaRzSNHMHgcZnjmB9GR6PLalOv7KUKYy__UG7YwKiKGaAaGVRGTwPFpkLnWWK_E6J72AlYM74OOSXTZTOsIV1tJn3YaH2VlJJPoLDdu76fAVyuH_9t49h0vOQTl37TwgBee-BHN-KyfXAKg-LIkn2zzO0rrqCnR3VVKVlI-Bfh-X2i6IS1JYkQ4ICpS_3el8YZXo9reYh16RBGvbwxBiBVhkR-iPah8HtG9duvy30DfDW99Yiafyqo2UZaIOzXGhtlBla7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUds0FCn71ZpfqGDWXtsJNLoVNETQQwB5DhCap1CufdwHTa2n5MhCwXxUWd99xfD9GaAYhgJCUZD2xCOytDxPI4cOXUDTmrssjL-IMV78iJPZcR6YaRPCBlpXIDE2hs_wgOhfMOQY_zERGqzu2jiT3uqPLKrsY0kGW_DlN6_qgiTpaM8pzoKIVEHR9uSn7s_EiIeUcddTLqi1Ns0YcVuzGGd0D2AZf_2abpiKU6c0KHJxXPqsThDAOwpba7iVPetDbbv6U3qWyK8rP-KugN-uVlLdQCY_ohCKg6yRzIE6GjZ-NNa0doorIJgs2_YrjaCsx9Frzu7kyETN8q9J-X4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=rSvwADS7MdQ22fXFrZbMqO0RMAfGU6TaOrtm03ANP6Yvzu8FVuO446-19cjYfpg5qOM-abqOV6PIw3TpGW7d4mpgAA2yglqSi99tz6cPsEJsyQq7UfoSieKVdfnA6r3-mknnTXzLrA9_SLJ-l-FofJyHOv-u199CeFW9cYJpP5hiHRRsa7U9B6pRtd8Rx-c1nHrWUovj_QOrxXcAlnZmiF1J1pfgo01c6uPi7WOUOEuElF07ZDK6-Xv2xczt-gZI79ntm0rFrFTA0Hj2aA6GAaLb6t1AGHJWU3QnRqeaSo29rh2kWQT34ugj7ApGabG00-5kqzeu9ZCvUVDnFrgOfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=rSvwADS7MdQ22fXFrZbMqO0RMAfGU6TaOrtm03ANP6Yvzu8FVuO446-19cjYfpg5qOM-abqOV6PIw3TpGW7d4mpgAA2yglqSi99tz6cPsEJsyQq7UfoSieKVdfnA6r3-mknnTXzLrA9_SLJ-l-FofJyHOv-u199CeFW9cYJpP5hiHRRsa7U9B6pRtd8Rx-c1nHrWUovj_QOrxXcAlnZmiF1J1pfgo01c6uPi7WOUOEuElF07ZDK6-Xv2xczt-gZI79ntm0rFrFTA0Hj2aA6GAaLb6t1AGHJWU3QnRqeaSo29rh2kWQT34ugj7ApGabG00-5kqzeu9ZCvUVDnFrgOfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=uNzNz163bdyJntt74I-26Og0J0sp_xQNy4BM5ijHPwgZpeN_1-M75J94mhrjTZNRGvPCqEVH4RyPBKFOeX7yHdtBRt_lc--JwwMtp4Y_O5Aiyx9o0tzo4Q5gJvXV017Y2dioh9UCHzr1vSxRRaWGWhKfTB2DzD75CrjwVNOQlt5rEHaqKuykTKXLfumeINlRX-09bKeUYNV2cNLfaQfmTPx_CiSd5XncEsmC8Smar1QOrpJxLjdi8HyyojY7CZolxukVW458qn6DyE0jNZwoJf2QYr-wS8TEz7pyNb684-oO2x1mrl3jmQS8PgW3Jhh5bmBfLddm6G_2UHIZsEbqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=uNzNz163bdyJntt74I-26Og0J0sp_xQNy4BM5ijHPwgZpeN_1-M75J94mhrjTZNRGvPCqEVH4RyPBKFOeX7yHdtBRt_lc--JwwMtp4Y_O5Aiyx9o0tzo4Q5gJvXV017Y2dioh9UCHzr1vSxRRaWGWhKfTB2DzD75CrjwVNOQlt5rEHaqKuykTKXLfumeINlRX-09bKeUYNV2cNLfaQfmTPx_CiSd5XncEsmC8Smar1QOrpJxLjdi8HyyojY7CZolxukVW458qn6DyE0jNZwoJf2QYr-wS8TEz7pyNb684-oO2x1mrl3jmQS8PgW3Jhh5bmBfLddm6G_2UHIZsEbqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=AXrEg8UCumCwAn4PUDcVtdF7u5ys-Rp4vpJ74n5655hWFK-CX7tljxTnM1YvSQsGHbKyX17XgpE-XrHm2qY1MUe7FkmvetWYd9UAaaNp02AVPY5ovGKY9QEMEbSoq22q5fJWnVUJ1rQhhlou9s-v3aIp83VfGLCmICIe6wVabPP8w9dKgxYrtNujFyg00REOYhYsQYA-ypuiE1nhjyIDRue3XmjeZBvryhtGEodvUO_jGwsd1fmvH81CJEmcdlV1a5pik5s3CbKcclw-1ZuJmoM7ZWfAWY6KF4JlNeP94jbpLIYYfJ4Vr0PoKUwi94OIXrfwTo_H3dwXsWITQ9xQsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=AXrEg8UCumCwAn4PUDcVtdF7u5ys-Rp4vpJ74n5655hWFK-CX7tljxTnM1YvSQsGHbKyX17XgpE-XrHm2qY1MUe7FkmvetWYd9UAaaNp02AVPY5ovGKY9QEMEbSoq22q5fJWnVUJ1rQhhlou9s-v3aIp83VfGLCmICIe6wVabPP8w9dKgxYrtNujFyg00REOYhYsQYA-ypuiE1nhjyIDRue3XmjeZBvryhtGEodvUO_jGwsd1fmvH81CJEmcdlV1a5pik5s3CbKcclw-1ZuJmoM7ZWfAWY6KF4JlNeP94jbpLIYYfJ4Vr0PoKUwi94OIXrfwTo_H3dwXsWITQ9xQsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNAiSOeNFw1p2qIrfhnn8RfiTuSo7liQ7XcSOAbvcWLwNlJdA2sxzI4VL5JIYAR6rHwqJ3uB_vg_O3zpe3cptXokEdM6UXSNR8HBIxdsIPgjO1F5dmz2k5fIdtQE53iJVhxbQ2d9dGBrnZb50fRuBIeC0OY8sCRZW_tqFymlbQ3o4cX8ZZDr_8FOOkLJ0LSD50aBvZuJMn4WgICi-mGUEbiRxdiK_7FCOkfnPE7wGk3U6WdpM65l98unghTgALB3iiiQQPVtEaAgnh3mPJLVY4pR61ecjo5xK3E9gibUcKQXDfWQt1DE3UKFpTMT-ZpSoaTn3JgJWbzSJS-sHi_Cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rza8_k88s-znxj-OQxdcGOjHBHUcr-08CfIhhL_CxcjhHaWb52XJze_za6S5hYeYHb0wAlhI8IwaO43jkq2Emhpzwko9rHG0iZQ3SYpIKiIBCDb14X3zBdKRWZbXXCuWXqQ4crrCJsvdFNG1DRGdUsn_yadJi5oTAQ7G7LKD737P81IjqN6cry3k8p5DEJZSFFSjverxNtshvvm6J_Go4VH3hzC1YZhU03KPzz05WtnoqBb14hN_huTEJPnN6g5fN6giL0zI-UAUYJ4qwHfeRF4sVnLIOBDDadX1eXsh9Wh-2p_ZgRrBnYWGYZ7pMoO0iBs_6sLPCrwI-L95Gm2LIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaL5EW6hfDQ7917RQmAnP_qbEUjhZGIPc73p-M8iOVMti_-giyd3Cm2xlVLMEcGPWL_AWTA5vkFzeXjblRz6heQmkeMs6HSUsGYdIFtdkjGC0TJ2N8MWhnnzdLctagX0npB4zze0lTXRam-1JRf-DdUCRz2xc8APBaKYHHiiCr6Xr5naYScOwvDwPw-8aPrLjD793jP8PIVSiqHrDg9_2h3LhW6xdTfBs80QywLliV_Iy2Hf9CDT6o7MBOq0UorKqtxMewyQhBdDQR4uCMTC1rfv7HIKeLKeviIbywDnyn1duoCuXI-dlsmu1uL6xW13WqgG3H3kB-mkSK6GMji7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=lQBGRTnPD2pZWaO19yw85mJDkRMP24eN3H73Cx_L8UN7QhuoDykmKhGs9bVxBtIFc9N0ewDHZ3fcCjWdTjwneKGbKF7gCB2BJqlhpdj3_ckF28skH2KKtNcaX0_XzzjL42K8YfMQZuIsbBmN5JkDNLtiRNpgQdSjm7auHBO22AnDdHTwbRbZRFS7BYAoXfvC3T5RtAL0cZ3iSQo9MjfFVclQZ1XBZi6v0A_Jmf6KvxZdJB_uKA96lo62IY4u_xOtzTxy633o9kKFat-36qAXBVfoFiEY4b5bmFTinKEPxPs1Y0NdMvXWqBlj_kDlWQO79MxnVPMgZ3avDUIpjjcjAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=lQBGRTnPD2pZWaO19yw85mJDkRMP24eN3H73Cx_L8UN7QhuoDykmKhGs9bVxBtIFc9N0ewDHZ3fcCjWdTjwneKGbKF7gCB2BJqlhpdj3_ckF28skH2KKtNcaX0_XzzjL42K8YfMQZuIsbBmN5JkDNLtiRNpgQdSjm7auHBO22AnDdHTwbRbZRFS7BYAoXfvC3T5RtAL0cZ3iSQo9MjfFVclQZ1XBZi6v0A_Jmf6KvxZdJB_uKA96lo62IY4u_xOtzTxy633o9kKFat-36qAXBVfoFiEY4b5bmFTinKEPxPs1Y0NdMvXWqBlj_kDlWQO79MxnVPMgZ3avDUIpjjcjAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=HcRGjFefPacuQcuZKrtH6NgyrE59dsnc3FGnckD4v_mFsjSV6-VhNgUXU6zLM603u3yeDP5p2NrwPVtmGdddH5lmWuXSME4JFgt0bXje9FOAjcRYT_wVEQlZq74AampER3vFgbwVx7bioYcHKbtwqoIpV3DCiOIuoad5XTL0c3i2X8YYhtu_8GeGcBobqUwpNT6qqGr1YXnqjbax2_DqQmtawhqMHjLfEQq5G_kPivCL6Q-H8bl_hVyvTljXKw6WaG7OYBn4ugV9WfkARr_VhzOlRj0RHn4vkR4Eq-Rloxw-mj2LDIKlXqhhiIOsK2gLm3rcNLYmNJp-GTWqOAP_pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=HcRGjFefPacuQcuZKrtH6NgyrE59dsnc3FGnckD4v_mFsjSV6-VhNgUXU6zLM603u3yeDP5p2NrwPVtmGdddH5lmWuXSME4JFgt0bXje9FOAjcRYT_wVEQlZq74AampER3vFgbwVx7bioYcHKbtwqoIpV3DCiOIuoad5XTL0c3i2X8YYhtu_8GeGcBobqUwpNT6qqGr1YXnqjbax2_DqQmtawhqMHjLfEQq5G_kPivCL6Q-H8bl_hVyvTljXKw6WaG7OYBn4ugV9WfkARr_VhzOlRj0RHn4vkR4Eq-Rloxw-mj2LDIKlXqhhiIOsK2gLm3rcNLYmNJp-GTWqOAP_pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=mez3pcuZcwqkUyg5ZLaLHrkhDvoctW0v--ccydhy1e80TSU2aA7LoqKJmsXTJ4S3v_VxtLG2krkPC_slx_tuvMslLOMot36nqQcZLjfjQQUEUi0Ow8t1XfiKg-FrnPrqV2Ao1NTUlg8318VsZS6R9C0k-ZCMoBdmesCo_G4romt-NhDAXp4tcUz3Po7lmtGu8bW8ilzVSXM0P43VzeP_Cd_kX49-ORTGVKtwLw_NLTLbxsm17X1H0cOp6MC3b0clsvJSN92DHQ0PS8juEZJVfMOVSUNYhuOLLhrBJ0i-aGYnAGPN3olteMMiCxplMA0vfBMMrRI1ZTEVRl4DeL47hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=mez3pcuZcwqkUyg5ZLaLHrkhDvoctW0v--ccydhy1e80TSU2aA7LoqKJmsXTJ4S3v_VxtLG2krkPC_slx_tuvMslLOMot36nqQcZLjfjQQUEUi0Ow8t1XfiKg-FrnPrqV2Ao1NTUlg8318VsZS6R9C0k-ZCMoBdmesCo_G4romt-NhDAXp4tcUz3Po7lmtGu8bW8ilzVSXM0P43VzeP_Cd_kX49-ORTGVKtwLw_NLTLbxsm17X1H0cOp6MC3b0clsvJSN92DHQ0PS8juEZJVfMOVSUNYhuOLLhrBJ0i-aGYnAGPN3olteMMiCxplMA0vfBMMrRI1ZTEVRl4DeL47hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=IP60jdqGtbgLT6_ecJZvVtBlP8DO3S5SeYupHJnI_Uwcb3-isdUOEVLoNDq5reluZV5g2CBwmaK56GMsVEkeE9lsOtc-MXYHskLBfGeUrK__gYLim9Vlusmbsh595AWNZv_TUSHuWJrN1C0FmQ-LU52O5oKOck3-TxtKAtkaTD1oUr1tNYSRPaJYnuihUolqRo3Yya4mAfoc-LmmCQHs-H5vqQ4m5S6xVcjxZcaGqJBTk7gctraQ4RUSVSrgRBE2aYLRJ-jaRO3Jcy-7XI1SIAqeowRdsSFyQGKSTSMyZIfslICBGBF3i6xTnRumZShWc8allzORmAbTIJ_sEgBJNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=IP60jdqGtbgLT6_ecJZvVtBlP8DO3S5SeYupHJnI_Uwcb3-isdUOEVLoNDq5reluZV5g2CBwmaK56GMsVEkeE9lsOtc-MXYHskLBfGeUrK__gYLim9Vlusmbsh595AWNZv_TUSHuWJrN1C0FmQ-LU52O5oKOck3-TxtKAtkaTD1oUr1tNYSRPaJYnuihUolqRo3Yya4mAfoc-LmmCQHs-H5vqQ4m5S6xVcjxZcaGqJBTk7gctraQ4RUSVSrgRBE2aYLRJ-jaRO3Jcy-7XI1SIAqeowRdsSFyQGKSTSMyZIfslICBGBF3i6xTnRumZShWc8allzORmAbTIJ_sEgBJNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWWujYD0ePnPMffGEnioT4kM41gtVHIqId49hEL0ma8ELqXBdiFUohg1KMW-3Jsz6rWNEDAsIUEtF5fvy_WCEJmftTohHgEYEUnrzxg-hbhFS3LqhP30bTLD13An6TcSS7wLSKoNHaa6uED4g-HT4i_uZQKFF3u1_QlRJbVkQkYIqs5hnC5O69lNNbupok5MB6L2OlEFwPhIzkcXWCZumUq2E5CkZL7ApWEStBu2lJRIgDKWM0zhjELZvBbfH0mB6ys1BjLUxQZdvYchz9bM_doEk41G7cvRHsUoovUCi2jNzu4bfOy6a6QxbzfGWbDQsIwYxFeZzafJhlK-oUxq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoPhs3kgMW1haPqNfEYSiO2Y5aS9A_YaCpvHvlsQDrtooOazVH44LvJ9MKo0WcHEcQcxFxRsJZKYX-3cwBQXJcLqtepRAiFaLXvZoY5miBw0zBTjH37muQ8crB0mdRf5Oc5Chs4L3rHsG5kZ44npk4FIitJdl_pF4C1CQYIUz0nAwe0-UtXUpNGOal-rNJSPyqQ4kYFatYEdfhEULgZ2Mu1ACEvm1ryT1slnH1NDnqCFp-d2ys7L50UJo4ywEhsKO9-kptGY0T30DPXPNfyqb1Nu43tL7OXHO1VI1apHF5CKaebhf7DiLITVPOXYD3K_0J_Y8kUQvLx8t-WPYwW9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zg8xi1HkkilVB3laYVORsUEWtjvhRHTlc9fCLErtDqo6u-h3M0cCZ0xCdBTiddckwvuUAk6xf0ddTIkNvHrHKz2axeLUkbUbqMho_m22H2FLIOexBXFkas_p7KDWZ0eLmrR2CfLHSfMGObWqyFyayQBwQdTYhSjJOlWkm1Z7aL45QCwk-9uoWqmh_8aApwJ9CXXRUSprO4JLroIgwsSVjGT5FmhNuR4v7MrpjnE2sAjWcGxu8NsEh95vnf4rGY3qmQT7SGHaWH7XN08RQMeM_Ck2aKUhqRBewk-5ShWJI69w5gQ_h5VXlYI8-98_MyqcEb7ree5QBzXvKCeVHWi2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JYDbeArkh6UZQm66YX4O8UA8v58lVDRhHv28u7w2-HWOhnb76B4gbqHwdlSz6AClrdB7yu0g0upecG_LCBNw1HcroXXs1ZnFFYZvNOW2onB4pbhMYvMYyCbbQ_jbkAXWobeMhuYuxo1pu1AccXtBvI4x-4medSb35hk8S4TVk1V3MC4nKndqzKmnJmkFxRdSAgcJS25DFzCdcJePmh_wSqAHZDMvmjzGZAfNeVY8VgnvDUFhXKHwuttR7WQzJVQAQ90ZhU2DM9YQOVPTOdepwlS7n8kqjd6_V6tnBCK4l_azGd34lONdOOmmjuPnV09F3MaZKMkItJLVSYctMGbodw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFH-5OOZNjHMFSFzZKEbL2Q4ikMp9vgBqc7kLTsKTSav5O7wdLAo9cuY2C31A28tV6OV1Jv4zABKUkewIVD6JN-PfMJuLbIwGwMFONG1lxW8xyMZHw4ypk-MbMCLeODytsRI49VYaW4AR2XRmWWj8kVcnlIgzCyQ-CiG0hk9lj_XROiQJA-fLhfpJ4IZEC5eksWwvv5VGyhnNkYVEYuynKg3lzslFtXa5XzxiBW-8Qtn1ZbSdgw3rpwwhAI0nXRxaCOMZPYcP0tE0-S13j43Q7_YfQELJ7L4ROO74bXk7pvvNA-SBN5Ha8N87vXX5C3-s5TNjQ9Wg_h7sS5xCZ_z3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvri5JMnX_rF8hZ4boT9yENfc6_lgiDRFEuU6_mKxN4_qKdtYMHxjWY_sCzNaQch1pW2G0AZEt9VHLFJoNSyHf5znuDJSkWguzxI9pwNb5ooEHBZdRU0SaOMYfnxqtMcxz_Dhg7Gj6txJEoy-VMdMDoAevZ8tVn_cdT1lFpBNZm5yaQNg3javvgea99qCTMRg8j-NhPN3A6U6p3op2sz1dUi09TYbPT9VDNaxHZK683a-HqPKbJ33p8K8B2ojOrWOVEy1ivLkHUT0WgOHcbUby9ka_kSLN3nPqv33ph0TKwCvq3zzZxbxLQNWCTVcfwSjoOkjO2z0siXj5aT8SnAyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW44-7ExJjfvFdVkgsEqCQbUMjMbsKepWy-CMo9lsHGRs4i1Vr4bGIb1fz8z27WZvpiAYx0XL7RppYVG0phli0kLq0SgTYTfY4DesOSjwlY9Sy1msU0Aycy35toKJ3RyKFGeU4xBCPHB1tdj1nOAv5PIT9hNJZDcK-bs8QLXQss7HDO_domdvYeJKaDVLot--bcJQtNkMdWRaVzYCNr6I-EFAkDPx0eCVs1D3kajiOjdigyhQKiP3fK87EGg9O8FszPRPFzHkiJP3XLsiMInxG-Uwqm9Yoba2pCxSnqKggRGilAdUPRlHqCnaLozDi7VZzGSrFWJJDy421LH0kF0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ug3-CD_y1_AQG3CjCdQhbKaZde3s-FGcCDyMZmLyRdvR7rIZS5fCemVFVpkLzNcR-Sr-CGPcFEwXpMqPRnjZsYzWND-2Fr3E5QEpiUUOrorB6LdYi-pY6UrkypQrL3LOhUZBW7ELdHLxyHveUnXKGue4eG9FbAJmucllet_3SSND1LyP_7oXKVVoVJ1xZpo2kg-47hZXjVg_A2akM7x9tphr15hdkWo1bBNH2PG5-YJd9BMRMt2gO2m9ubuG9YA55fxtvRrC7_Ho5RJcPAVlguyMYZfcJ6AtMUPIF1PSZsYTKO0sM8Q-PC2u3pPdTIoBohyjc6ng3UoAKg48cgbNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZWN2yWRZkG7UfYqbUpoyCeLNxQ-i_vLfxNbNP067kBwiRPl9ccTbLivi32xqME3gon15Hmx_aW5S2T-KZgY4xsk9YF54Tsk0LkCAi8d_IY4mL3MBXnJHojohoKTZLU9dO6g45QkhoYPNYAw91NGdiu4IEHBnOrnJeU8pB4r3wSaNH5jX4-M4JTN2ow1bZAukc8U84zQtlnt8VdHFYhxhJ1RgV-A1dLDacsunytMxw3JPOrnHuYL07xuxPHHAN2YqK1v6NLnyqieiHLDqCjj79i3DTNcfy37ypMHTlQc5IHMfCylT33AUHIPQk0c-1Eysb4gIbTFbHEh6ODmkMLFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSpau29IuQM0U2o1HskvKEekPjORuFha7VY4icQuq_OvOMHGnFSNHVon_naoxl9VZSLdi9oQN0mGy9pNNoXgg6V52RPxM8llI-CKO3_aTxYtlR1JKNg4rAlzz1TC-6CVZ7gyJkXxIq1EOWUIUf22nGOkuO5CajsLRtt9lKPfR03aR185yccUmHDUJjiEOG06jS9xl6NDDXQIiGResbt1uYzY7eWkE3L1ccPMRUjkmpRDvZuKHcha5k0_GnPEHFHsz_4qV93bQK7D9Ot6QhznGUHn35Yx83I1Hv0jCSHjNET_nAkGGt54BrpcNiCRJmY0J_YQxEw4NEKZN45unEKPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hx4ih01lA5cb3sA-JSHyRaE_69LSBRYq-cgqlWOv4lrFS1NZBw0Ln_K2c5clFr7q2QUPoeBcJu8h9KzgC35tq-gzUuwdboptqV4fGRFLxux8GIsFOCvSiHP-qlyMq2ZDi6ByRm6nSJVTxqRiGeRlJvLsiYL_ZxytbZJ-6TtO-MTq6GPN3szRm9FZkSI7L8YtraJ5aXchCWfTNJrkYOmjHrSmf-dq1N45hU7YvhpXi-G6F2iLZNxW1zSyoc1E_K9cX6sfq3LplS1QcaIchA8bDQmYxJXwmevDKSe9NXxGaG2u4wN3iZ3qPmHjZNpVTANS8E9M19G9oEPzNhYwOhHzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVXdx-50P7DNmCepPWbihj6tXuLNxHBLPeNE-GAhde0GPFbJ-Vzd4V2KoC3PGFQuL3kIuI_ixG1vDKIZwvPvwB2BSIHz5IhftyflLT9clEk23RTHiTYMyaLzs-lWurIdgxwHiB0f6RUG5fe1dtvW821H7N7rxDoM6-xSWUFEi0VLlZhB7hHpg12MK6sm2btW9VR50TP7wU4sPzRb5hVJ6NAfOqY7DCUkl6W74ARGDDHxl8F63B1HVOMZaJAtqOsyhOchdq8L5PRWs_dUqPi7J53AmN4ne78CLxZ9XzonnTRGFd-YXoxX8EUJ_WCvdTNHo2JI4rqgMdSYlznNqVMegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7w_IPJA6FBbIa6ZBAKWHWHy4rkbNxvMwqr7acQ_HkphkkjpLn_IVH22LeMC2YE0l96wznolEuhmSR67-nsvxYIW0Ud_CmZwhDeaTVxVSca6NbRnvrLo_d1GXrpTvarw0p9sbLqmX1QbnkN9Ut8ks4_5VSZMlW1oOi08-1S48v6tQmCV6b8mC6-eUtfyVAMvZRNYMkFGSiVniDRYCarT45OVvLN0i7p0_5OEZdC58SeGM46kkG2UQM_T1uUZ35xXbqq3oj218jRJeFfAwGxluLQV4qtnvPRb8b5iDcQlKPG0buK2eHlt2bYqkA1E6U9FA5PMN5jxwMxP8bV3hO73ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUzbQ9yGuqHMB7aNQJumAmbTXh_B8SvaIE-v8rqCnExt4QoN-TMtvDv1VTAFO5i1Ps4X8W2VoMFHIxtqpaWbDMtfLvM5j3oSNk0uYy1UqNeaOgDwzpKAyStNuIFIHJvysz2uBHOri-Sg55huceXDf5l8OChdaiDc5j86MEeF5x9yNluXqmPqyCvh3tGni8Qr9Q1lyi11-sSUg6hqEwA39vltswfYeTCTmNgHK8KwRpzdYAJYyhRZWmzZHvlukNFNZ_6HLe1peB9BUv-99DPYaXZURfYfRsbrJ31rczy7y0eohhs9VW9qA9wfrK3Xny2M6S-6bDho8fgjS1JlKoSsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=mv1PDlkvZcZ5s19zNrrqSDJ-QF1ezJDMNBtAYu3srSkh27kAnpj0JkCZZ8JujAmmnSdI5evwBw8QhI9F-_3QyPE9AICmKd5nmoRUp8jZFdR35FfB--i2rmSLCehoyDTokuaXbdhDKgXog9knE5vIswiTYsooByaicDJQKPwzonE5QsIj_ZpAEFQ5TGL-tERL7r3lBDhlubgWTWYhskf1QaiwBVt25wYvRsOooEBdRzN4XN3ZkJLnAMZwnv088lvlEDRgww0QNDmnVcUunySeAPcTHZwfzl7c5er2jWnPzHsmE7kTjzGnuzg5dIBC5_JHsTuYr-pa02ehPPiF4dZw3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=mv1PDlkvZcZ5s19zNrrqSDJ-QF1ezJDMNBtAYu3srSkh27kAnpj0JkCZZ8JujAmmnSdI5evwBw8QhI9F-_3QyPE9AICmKd5nmoRUp8jZFdR35FfB--i2rmSLCehoyDTokuaXbdhDKgXog9knE5vIswiTYsooByaicDJQKPwzonE5QsIj_ZpAEFQ5TGL-tERL7r3lBDhlubgWTWYhskf1QaiwBVt25wYvRsOooEBdRzN4XN3ZkJLnAMZwnv088lvlEDRgww0QNDmnVcUunySeAPcTHZwfzl7c5er2jWnPzHsmE7kTjzGnuzg5dIBC5_JHsTuYr-pa02ehPPiF4dZw3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYEyFdANqKD6QytXuDnwYyUeQhjdiu1sdbHQCoZPqknpq0YcmwrQzb00lFa6uCNvtPYdlKn67ZgUp7hVqfv0AxZCfw1wC1N4Ibf11eCIIYv21mvuqatm0NfE5PVY6n2QOmKn-YYnnz-ETq17bm2x2Q5_m9g3CJ_GsEp9RMUBML7EpEZteZ56y719WSOY1ohbDSNb-WuYPbrUsXACZNlCoyZ38GwpQbktjllvfpJcrqaoZT1pk4qmvSALOyjPlIyzres8-T7ymAKguz3uvkWo1e2bypb7jtAwMUtojU9Szj05Qx0hDu9wmAAMtnD06kaLBih-5we92TqDVDYR42hBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSlj0LxomSZmM8x-nOSO5eZUars8pzB347jj0lLw-fhVjn_-mfpK6X5e60SNySLu-91CZnFLEfDL3c-4gxuuUBYWSt47rY4Qdc-WzA_QYVhFi4vA3923Mbf1Suqs6mVlnrkr9UntieFMI9YaWaKS_Mz6tEGAiGsASxW5OGBcbCXjX4mTkgaCvVQZmVSE8jNXySBDUd2g3DvhzfHEa-5V6k5pVtsdoDBqgMBTF1V3dg3eywITHBo1X8nfwvlH2aXFtQrECLjb2qLoy1uDal59tVZXlGxC1904KdoxFqAdT7GexjRq7mv1haGi-RRTBXqTwVU5mQwXB45zg84wDGhoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpF5aHodO1m0gPcpKHWnuVwUbznRZtUNrAV4evdondWCsOmf_y6sMk0jJjCpY-KzFADWMeGXH71S-O28Qqns9QAeC2-f8IVUfkTNTy-9IyoAgu_iRzN-sCzSN7N9POfsUUD1gCYrBQvKrgxEIj6_fXHRP6aeMh5luwjCKBMpUHDw6audtG3xNgJI-gKcFhYuF52YYuOIi1s31w8-zyqtEvizs8RLnwOPqmIfXjJFBI8MwUD6llGCrGTkYb_1IjytBHvrACg0FMz769zjY9DbjeWh6ybwOwPMyhItd-XKqoCigpwsKzF7yU1zSpJUqt5zHClSz8_MD7pXaee0UX2saA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODbcJvuQdIe9hDl0KtEKnitOUe0gGzKCHEXiiAGzq3ZiJpsQ1MYTmskwNNFkSlNT772mNkeUuqDp1fIxUzxMqI_UChAyy0PDB47kOkxBAW73wjBM2mNQvKZPVsEEoQwKOhAzJ7on-uThJJuUhcKULX0z5DbBEfswmK2qwyZqkqlB54C2-s9N-7CWnprWyWKvqie2nohTnBHGwXdZtSki6TNH3vg9IBMgsIpAz2Y3DpIqJeE05uOS9A5y6L27wTXj7blQSF-4B25ojE1byROnhNfFJOfR_DQXYUsqBmzr9KSYUQsXHx1i83O_RiQpJLgczg6avvOJJxaVSrhrDSpZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdx1Qb52dbnA2NF9TaB8ScfOAxbcyV18BE1h0wbKCG-Xt0izrIByCUOQkifnMhfuEWmaK6975VEoIExS1oWUPgmNgATNVAcx5u_N48311CWgiZDj9RRBcyi7iBlsLhEQtb0_spiTPB5n3GpxIWOlRx9Gx3a6DF-z2XdXhrdHzO4lokuto2TL0ZDrm--kDc2jPQLsh6yO17FynOhaRsNXwd-bcw2OC5gL8c5YN0rrI5LspkpJFpg_V4IJc4iXs3v5EA7NA0P8Zt_ZjUB4gljUjKlzLrOwtmkj5B_HKKYd6tF7sReETd3Ky0qbei7y-AqRnEo_p4fYP-yyjTNPGvZl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
