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
<img src="https://cdn4.telesco.pe/file/vqNeqp1PZYaEGBUuN1T9TxAN61XYEYIy-kTtLZI6okA7qNo1JNbbUfZd_fRA_W8jnnYl3wTTNuuYRykZK3yREXeDmkg3xweIVurJJKnpi1ZfB__qSNnPhtONemk3xYDTX1RpSBNBuybiQaL3Rlw7vVg1fR8VWqbQP_CDCO_VL1A6suAzfT43VNego_MwYnyk4furXUFqsV4Sha6NorSA2PrTLqvKH1VnCl3WfL9r8esiTacDphK3F4fX_w6g9cByVShI5nO2-G-DKkuMf4qKNkwn8MBBchWdN9mHvjxQelhM6LLvbM2fjr9ysl1HVNnaRb_n1AjAIH5aaeqOq2PS2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 11:58:49</div>
<hr>

<div class="tg-post" id="msg-125232">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سخنگوی سفارت آذربایجان در ایالات متحده در بیانیه‌ای به سی‌ان‌ان گفت: «ما ادعاهای بی‌اساس مبنی بر استفاده از خاک آذربایجان برای عملیات علیه کشورهای ثالث را قاطعانه رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/alonews/125232" target="_blank">📅 11:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125231">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سفرا و نمایندگان دائم، ایران، چین و روسیه در نشستی مشترک با رافائل گروسی، مدیرکل آژانس اتمی، موضوعات مربوط به موارد مطرح در نشست بعدی شورای حکام آژانس بین‌المللی انرژی اتمی را مورد بحث و بررسی قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/125231" target="_blank">📅 11:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7e8e2790.mp4?token=HPmHGiBNZ9caHsqvIa37w1CNyElnBOC0er15zWsieUUVsDyhPaRQKCbIYDfRdacf_aAAMIYetioXbl_drzXX2hxnBhbEWCl6mBmhEIiUVXnQbK5n7AKsB2iihws1LCCn0wbEmsxMsWf8ciEDv5dPkFtRXk7r4eILNDPt8AzfLH5LV--IHf0fgQgYXzePaSk2KHUXio9PSoz5kxT5qfUZ2ru_jQRcEt6m_nFBscu63xx4jtVq7WzPj1wG31TVlclgviFiXo-lrc-oZM7GZQv3GhWQbOBoABy5a2quWCcLUScZSqce2mO6_iLusSkjsjdXFjMnvBgXIg8aHVc0cp5nnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7e8e2790.mp4?token=HPmHGiBNZ9caHsqvIa37w1CNyElnBOC0er15zWsieUUVsDyhPaRQKCbIYDfRdacf_aAAMIYetioXbl_drzXX2hxnBhbEWCl6mBmhEIiUVXnQbK5n7AKsB2iihws1LCCn0wbEmsxMsWf8ciEDv5dPkFtRXk7r4eILNDPt8AzfLH5LV--IHf0fgQgYXzePaSk2KHUXio9PSoz5kxT5qfUZ2ru_jQRcEt6m_nFBscu63xx4jtVq7WzPj1wG31TVlclgviFiXo-lrc-oZM7GZQv3GhWQbOBoABy5a2quWCcLUScZSqce2mO6_iLusSkjsjdXFjMnvBgXIg8aHVc0cp5nnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی مطهرنیا، تحلیلگر: در آستانه ابرتورم هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/alonews/125230" target="_blank">📅 11:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بلومبرگ: مذاکرات ایران و آمریکا همچنان بدون پیشرفت مونده و در حالت توقفه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125229" target="_blank">📅 11:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=YSxBEPrI1kfjODPGJypo6XebTRUVn9v_Hc87AjYQhFE6tjCCVzpikP6kZ1aEZ1-r3VFtXUc7FN6y6JfZk2Pl06qU2j77HtsaQoJ0_q1cNzqWhQMaNlnBqCJWuxpXqAg67PeoQ5YqeywLZkt4uQ6ehK7kb_9jWhu57FRBntZoF9Pp8Zv7yVdFNyl-ptlzQzSYm4lag15SmlqBlVt_rWFnaSoONKGUwljlZFFyUdmSiIEnrnOeIOozPBdoOco8WLyoyyrjdSEpldpQAAesAWhE2P6HsKad2NvLFPV9flaEvuLmOOnBXXD_pGyIJ6e43CDqa-0bF3WUQQpfyaQhcwP3bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bcc23b06e.mp4?token=YSxBEPrI1kfjODPGJypo6XebTRUVn9v_Hc87AjYQhFE6tjCCVzpikP6kZ1aEZ1-r3VFtXUc7FN6y6JfZk2Pl06qU2j77HtsaQoJ0_q1cNzqWhQMaNlnBqCJWuxpXqAg67PeoQ5YqeywLZkt4uQ6ehK7kb_9jWhu57FRBntZoF9Pp8Zv7yVdFNyl-ptlzQzSYm4lag15SmlqBlVt_rWFnaSoONKGUwljlZFFyUdmSiIEnrnOeIOozPBdoOco8WLyoyyrjdSEpldpQAAesAWhE2P6HsKad2NvLFPV9flaEvuLmOOnBXXD_pGyIJ6e43CDqa-0bF3WUQQpfyaQhcwP3bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیک‌ها همه بالا
🍷
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/125228" target="_blank">📅 11:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125227">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/125227" target="_blank">📅 11:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTKtM8bg3REZ07QEZrfjOLi-JcX04XkFUYWdXS2CtgCAOVdW_UOyNujkRnAQsr-AmLZuXSjh4TUXVK_f--Uxn_gm1v3ytOeW704usRrOIbwr_VKtVUVp038KP7O2HTCq0e-3ZWuUdzo_7k8NbzjXYO-JkCVgtH0Qcjqur2DNQ074QRazprz_H9pIQQhBb6b6gEJO8a4rqmmowefUuPeneU4XQGFDfGujpow55OnUu4JG7CibqVfpEQfA7qoaFEKLM3BC0Mi7aw3jJDeFb9479CqQXYbJt_xOXnElhA6VxGDCNGJ6cSg__HB-QWlFQ1jwM7hHA-fvwvKBPtmdIa7NPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آذربایجان چهارمین کشوری است که گزارش شده اجازه داده نیروهای اسرائیلی علیه ایران در قلمرو آن فعالیت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/125226" target="_blank">📅 11:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125225" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125224">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3s8KR6HNBW7unXwOtioDK6WUs3xgDEwfvrIvGkrltLEWkaC9l7L_D9kyjnsorLqLym9UsXYuYG50IRmamspQ_TqY8cju13dQGPSzero-ZbJsbRdOEqBb8LKHJG3CuqvliFdllMFz_vTbTc7NyoU5lbG9lIBzLmBhVyIy1ZpgDWCtEkXT76zx6AqNVOkkuZ4Gn9hyuh3gFWTZAF1vjHVvVmXXZYXEVfp_kDBYaDaaH6B_kBImr2i4QWgx6QTZyPa4S0TvE1zokq3PSab9X7ApZR776ElaOSkZ20vn8yS5QiLfhPdRXz74YjXs3EZWaUatzpyPQNVjUPuWutxyYewvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط 2هزار تومن
😳
😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t
با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه ، سریع اقدام کنید که دیگه قرار نیست هزینه زیاد بابت وی پی ان بدید
👇
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/125224" target="_blank">📅 11:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583002539d.mp4?token=dE9X5sXDpqihvbKUIW1mCbRCaDBelSmg8zvGj9tHfJ1tYrNoB0B7w6sFm6InYRxuM4DfHXF_XhfeQ61o8oFcVNDTiT69BK2XKADzijHRv-s-vKGuNdWqtQTnP8w7DUBTDDD0gV32l08U1VfckHpL5QNwYw9QKgzi28E_aD4XaE2JXmvPxBqBhpYq71_66RQFMPplR3hy-hB-__u4DPOefId-f-fOS4uxjNcwHGjNXxJ4JkzbRwmYyEnjPND-bpy8SrLvpoIFmUN3zxtH82FVeTDY4pyCyeipDKI01fANR551JGgnLe9rsHS1Y_OQ5L5-a8OO-saTjMa1UxIQqrd3w3aOwyPzA9TkAd9IrciH-80nAt7S_oKcuqdvLk3Fpa8L2vXaP9n_6VHop4XdAxXZBkMOIFMZ0VTu_opzvFv1L5jjO_bS_vGT7dIe5-1GGA5wPfeaMI70mfavHf151oZ-cCZxn2dCXFnuWG43f9tvAq_XKOdiRdOM1TnQDtrpP4R6LQJR9_5SOc3qrv2f9nB3xlDVJ0MyEfn0UQ0jrsvQB718T3Nmtu5300ZSGlaUZeLq9-ct4bhVTQOI5et_V1-Vn9q17D0NFnXCX-wL72eMPi4nrX64xCve8oqQkg7lW47CvunxitP0Lf3g_k60MPlmxeF_vNSMzZVodIPOysnL8Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583002539d.mp4?token=dE9X5sXDpqihvbKUIW1mCbRCaDBelSmg8zvGj9tHfJ1tYrNoB0B7w6sFm6InYRxuM4DfHXF_XhfeQ61o8oFcVNDTiT69BK2XKADzijHRv-s-vKGuNdWqtQTnP8w7DUBTDDD0gV32l08U1VfckHpL5QNwYw9QKgzi28E_aD4XaE2JXmvPxBqBhpYq71_66RQFMPplR3hy-hB-__u4DPOefId-f-fOS4uxjNcwHGjNXxJ4JkzbRwmYyEnjPND-bpy8SrLvpoIFmUN3zxtH82FVeTDY4pyCyeipDKI01fANR551JGgnLe9rsHS1Y_OQ5L5-a8OO-saTjMa1UxIQqrd3w3aOwyPzA9TkAd9IrciH-80nAt7S_oKcuqdvLk3Fpa8L2vXaP9n_6VHop4XdAxXZBkMOIFMZ0VTu_opzvFv1L5jjO_bS_vGT7dIe5-1GGA5wPfeaMI70mfavHf151oZ-cCZxn2dCXFnuWG43f9tvAq_XKOdiRdOM1TnQDtrpP4R6LQJR9_5SOc3qrv2f9nB3xlDVJ0MyEfn0UQ0jrsvQB718T3Nmtu5300ZSGlaUZeLq9-ct4bhVTQOI5et_V1-Vn9q17D0NFnXCX-wL72eMPi4nrX64xCve8oqQkg7lW47CvunxitP0Lf3g_k60MPlmxeF_vNSMzZVodIPOysnL8Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خروج اورانیوم از ایران: ایران مثل ونزوئلا نیست که چند دقیقه بمانیم، بعد خارج شویم و آنها برایمان دست تکان بدهند.
🔴
در ایران باید یک تا دو هفته می‌ماندیم، به تجهیزات عظیم نیاز داشتیم و آنجا یک منطقه جنگی واقعی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/125223" target="_blank">📅 11:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHc-AmPBdtPrB_4obTS0WgY2lLkua1fJIOY9g6MlBeuQKmtR6rxaDqhMRgFujfVXbi6u4_UCZfegCRkG9Az0IAePYnKalEbA8JlpR0xrnPCbvjwk_Xr05VWT7genOEmQ0ctMF8K0MA4sHPKopVSiLmy2pl_do4RcCBFU2XMQZj5qJJ5WtwoWlb4Pg4Kh_JYpzQmgeEP_bp1L9SVzCInFlSIWHYIlJr50WhExX7BvpqPZXVeZfMH062GZUlALjGBb2EJPa-Z95Lby7meAiPMDIg3Vdkb4fEzRzBYBn1kWDmtpcbMx61MHCfONIsOgUmc6sX9yujwm-ZTSaWWL-RNxKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظرسنجی جدید ماریو نشان داد که ۶۲٪ از اسرائیلی‌ها با «اجازه دادن به ترامپ برای تعیین عملیات نظامی» اسرائیل مخالف هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/125222" target="_blank">📅 11:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125221">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس پلیس راهور تهران بزرگ: تردد اسکوتر‌های ایستاده و نشسته بدون پلاک در خیابان‌ها و معابر به جز بوستان‌ها و مسیر‌های ویژه ممنوع است.
🔴
هنوز سازوکار قانونی برای ثبت تخلف یا اعمال قانون برای اسکوتر‌ها وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125221" target="_blank">📅 10:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سازمان ملل متحد از اسرائیل خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت ملی این کشور احترام بگذارد.
🔴
سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125220" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
العربیه: وزیر کشور پاکستان برای دومین بار در عرض ۲۴ ساعت با همتای ایرانی خود در بیشکک دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125219" target="_blank">📅 10:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پولیتیکو: احتمال لغو ارسال موشک‌های تاماهاک به آلمان به دلیل کاهش زرادخانه تسلیحاتی آمریکا در درگیری با ایران
🔴
منابع مطلع می‌گویند که آمریکا به دلیل نگرانی از واکنش روسیه، ارسال موشک‌های کروز راهبردی به آلمان را احتمال لغو می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/125218" target="_blank">📅 10:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a6df09fa.mp4?token=unELUu4cSjoD1LZeoTZGFM9jCE_Si1gc-M5c8ebPAiiqxvUaEc5VzARktrKS8tefSzJHk_sy2wn79EN_BW3YxgU46I6_WjzBYTxCyvbMgHk0imbomZfiiq_yMfbx29Iez9PRLRgmoRlAT9Za3sKnIJuLTvrq3HyeZUd3PPqjtdTRI4pHPlnZ9l81E22hEDxOpW5vG8ZzuIAJHZq1RB8c_lR6LhFgn4P7n7dyB_1hHYkNsFaKBvr49Wu-o9wXg3Jzu-gUwQyGQ8Td9_dKmhavqpJW2Fmmts1w3B9SMv_NnlAR4VhhJkvLIyOObNfzJd48Fjgm5CqxPsNqnBOD17r4tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a6df09fa.mp4?token=unELUu4cSjoD1LZeoTZGFM9jCE_Si1gc-M5c8ebPAiiqxvUaEc5VzARktrKS8tefSzJHk_sy2wn79EN_BW3YxgU46I6_WjzBYTxCyvbMgHk0imbomZfiiq_yMfbx29Iez9PRLRgmoRlAT9Za3sKnIJuLTvrq3HyeZUd3PPqjtdTRI4pHPlnZ9l81E22hEDxOpW5vG8ZzuIAJHZq1RB8c_lR6LhFgn4P7n7dyB_1hHYkNsFaKBvr49Wu-o9wXg3Jzu-gUwQyGQ8Td9_dKmhavqpJW2Fmmts1w3B9SMv_NnlAR4VhhJkvLIyOObNfzJd48Fjgm5CqxPsNqnBOD17r4tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی مربوط به اصابت یک فروند پهپاد انتحاری به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/125217" target="_blank">📅 10:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEx7f-fx3fxnwYpNs36uYIjVnrwC_l5dxJdlx1QaQHiWmhnYD9MUe5QRjmzpk1Eh905LxQ_tfzZ_f6IWK8u-mCg9fY6ac8kfUMl4tYl5SE2op1oFNrc-qPklynwBWtx7r8ZbTuqpH8w9nXfBNBPpPTE_0yNTCHrafxPt-43_hFOA_XPQuYivSddbbFackncdieaL8YWdWxqhtTclbsi83eCPo31rwW1AmLseHCVVZt2_R8rP08Uf_-96z7fMjL_fffaiE7mfcTtIeynjzKVgeJ9ZNo1bdO3F8T6wFzRz7c_TkeEr9ESXpU-I89sSJh4V0EenwrTf5SZmsm1qQx-TVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم نقطه به نقطه سالانه برخی اقلام اعلامی مرکز آمار: از ۴۳٠ درصد تا ۱٠٠ درصد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125216" target="_blank">📅 10:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125215">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmAskKS461WIXZXVH4hL98pqhuJrhJPWOwf-wuztUZr79ORa0KoMPo4gzXHw4jJ0AsQSKwo5v6jwK5zqhymjxVm-mgsyDpCaHVkN4gsypwFbh6IT0RS_mtfqoqzTXyYKZD_G0HjwdcdiDuP61vXqOZ5IDg8q_fQNzPVrmXZEdss-CFjRcY7xZCCv7PYUe1ASeDx6pEI93kYzntAxXoIWNV7aTuHJARdWGzzlBoH2zMGvNQ8-6ZmYyDaIx0YpJ4hgJEx7LjnvXm7mXF4WHV-DZeI96udaPqyXrfNFXO6imk1oDr7DsOF0dV1mxWT9JahKpRcQkbHqpJlaYrhwr2RN1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرغون هم رویا شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125215" target="_blank">📅 10:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125214">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اسلام‌آباد درباره دیدار وزرای کشور پاکستان و ایران: دو طرف در مورد کاهش تنش‌ها و همکاری‌های امنیتی گفت‌وگو کردند
🔴
تلاش‌های دیپلماتیک برای دستیابی به صلح پایدار در منطقه ادامه خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125214" target="_blank">📅 10:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125213">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na-nGMnhaxiAynULBOf9zhrffv8C8wKr6HtfeIXG6zepPThISUJaj6T0AOsC_-4JQf_15YjmO9lBwdLUoTGqBcDtIzGhaTB1l-aDt0D9Hp91qS4ejzVTT4AxeiUl2rUHrdg7EUBVWPt4oDsEoOnS4nfbJUSXHZlrD8xhEykDDXabTWUdWeiLqeEY4JRphefwMaRSEkm155OizoLhu1MbwQtguDKy_F7UZFRm-4VbNp9uAtlSVo7uXrwzxp0ttbvJhg107CqG6deltZVvYzunIqZSUtHBQVSQK-LieLerRkn8Iu-Q-jDZxELOOHCVBK-msvgl9MuVfDDAFdXWCDZKkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین رسماً به زیر ۶۲٬۰۰۰ دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125213" target="_blank">📅 10:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125212">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo5I7n4CUwBPkdfUnKzl-320BZVkTQYtzJE_ioevafGwbbv1uaMVW3XEqGF7VuunGDizu47bLXEYokZHj0oCKIT7n7AIBE8ToZdmwD5_3dnyd-JYbt0HkRGvVqbsQZxmBssMTK6JCZH0ccyRh2oWkDV6WsopDXVOyc-NZu5Wd8kWaqSyDgYKHTOAHZdLKPjR-u9kFptEEoOxLtYrvymdvLZeMn9EkZObj7mFkGvHn_kEOM1I9Wixt-TEdNBymnaTYkwyL1m9Bh2NXCCabxlid2_sEt-I9SNlEB93JjydxvfbwZWF6AEJwfhR4gHxi6nY_TxJLYacHf7Tt5HIglpVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خیبرشکن صورتی در میدان انقلاب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125212" target="_blank">📅 10:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125211">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
بلومبرگ: ازسرگیری عملیات در بندر فحل عمان برای صادرات نفت خام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125211" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125210">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpkfdJzMXxtyDa_xOO9h1CDV-MkkSfealCuZ_MaWsQArrHq9aW-R90KUkUiv0lslqVxNCaGSRnxao_aHRkwjOm_L0K2XAM1RvYmpgwIDK8fhPn1QmD23a1ovqQ5H4Ht3P_59QhAw6i2HMkQy3uKubaDV_EQ8YN6OuVs00KGRZNkxKTaS_QVh_6wrQRDHSASEfzJeTaCd5SNToMCJ2cr6ew1dAf4cNOjOxv45zLfklfUuJsMVSdeRBL40Azc9vibUVmIwXQOneDG8ZL9YKLNFlkffDPhg3XG-JzgAV6Cbnyy3JVLKFLsqyRsdvc2RNl0VMl8qg-D8VrDthg8MVzci1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: با دیکتاتورهای منطقه به جرم تامین مالی و نظامی آمریکا برخورد کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125210" target="_blank">📅 09:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125209">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
آژانس اتمی: هیچ اطلاعاتی درمورد ذخایر اورانیوم نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125209" target="_blank">📅 09:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرنگار الجزیره: دو حمله هوایی اسرائیل به حومه شهرهای نبطیه الفوقا و میفدون در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125208" target="_blank">📅 09:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه، پوتین، درباره اینکه آیا روسیه به اروپا حمله خواهد کرد:
چرا؟ چرا روسیه باید این کار را بکند؟
🔴
برای ما چه فایده‌ای دارد؟ دلیل حمله روسیه به اروپا و جنگ با ناتو چیست؟
🔴
این مزخرف است. این یک تحریک عمدی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125207" target="_blank">📅 09:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کابینه امنیتی اسرائیل به پیش‌نویس توافق و آتش‌بس در لبنان رأی نداد
🔴
روزنامه یدیعوت آحارانوت نوشت: کابینه امنیتی دیشب به پیش‌نویس توافق آتش بس در لبنان رأی نداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125206" target="_blank">📅 09:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125205">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f96f6487.mp4?token=OpQpRUncRsKXbj980RKs3BAbNZ6neJIAuYYfss_ng4KpOmTZJ7U5BvBESX7PoXoPeK-wK319pqGAwmQNJ5_9QvsRioWGeKH8v15uDX6ec9TGFCuhtFqQ4Lovz9nfiUF9IH1IwTfYJYXZvdS0uYxuRxHdnKsKSsD5Uf-W1z1B8aSCCSVG8Cku5QerFWe8hMlY1FMSvkao5GTTSHu0CW8GUDSodOOA9ghgo3ip2H_GIodRXxhfkIXEXEhJnG4zzfe0ZTz7S_7sgVDQ8GKlDnxz5zmcpKc1BVjrCVO8-bBDUJWYkoKESrciJc60_BsBhb9b36bEPwP8LTuDWo-4fXTMWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f96f6487.mp4?token=OpQpRUncRsKXbj980RKs3BAbNZ6neJIAuYYfss_ng4KpOmTZJ7U5BvBESX7PoXoPeK-wK319pqGAwmQNJ5_9QvsRioWGeKH8v15uDX6ec9TGFCuhtFqQ4Lovz9nfiUF9IH1IwTfYJYXZvdS0uYxuRxHdnKsKSsD5Uf-W1z1B8aSCCSVG8Cku5QerFWe8hMlY1FMSvkao5GTTSHu0CW8GUDSodOOA9ghgo3ip2H_GIodRXxhfkIXEXEhJnG4zzfe0ZTz7S_7sgVDQ8GKlDnxz5zmcpKc1BVjrCVO8-bBDUJWYkoKESrciJc60_BsBhb9b36bEPwP8LTuDWo-4fXTMWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دیشب هم در کاخ سفید چرت زد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125205" target="_blank">📅 09:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125204">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
با اعلام سفیر ایران در روسیه؛ کار تملک زمین برای احداث راه‌آهن رشت – آستارا به طول ۱۶۲ کیلومتر تمام شده و به زودی برای آغاز پروژه در اختیار روسیه قرار می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125204" target="_blank">📅 09:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125203">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عراقچی: قطر تلاش هایی برای ایفای نقش سازنده در زمینه مسائل مالی داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125203" target="_blank">📅 09:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125202">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
در تهران سد ماملو کمترین و طالقان بیشترین حجم آب را دارند
🔴
موجودی مخزن سد ماملو ۴۰ میلیون متر مکعب بوده و پر شدگی آن به ۱۶ درصد رسیده
🔴
میزان پر شدگی سد طالقان ۵۰ درصد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125202" target="_blank">📅 08:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125201">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
آژانس اتمی: ایران فقط اجازه دسترسی به نیروگاه بوشهر را داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125201" target="_blank">📅 08:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125200">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhb3xybqBEMuZX43UveUFolT1lviaw2yWwFLr0NG_Eb9abFcVOyBJVTEjPwS-30NesIH7XqS-AAwcu3OIz_FpZvXhedzSl3k6zz0at0I_U9N6axTRmCCnnhanQ7LmW8OSPRy0SWk4fd9oZ95RSbxZ8XYI28ucyINR8i9AYFtz1qDFDIkd11iizWJjEHnqErfnjlm_3WRWNxKoTFwSal8Vh14UeDvDosx6_d2EOki-_Bf1CKCxyT_3biIkwoBChd6iODabpmr6edjArSZBwcrbfsytULDYizTXGgB9upgbawkAQacsk8luHmMUvWBT8CvrFsxW49kMWVtuqX4G42NDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه «هیل»: بر پایه یک نظرسنجی تازه، نزدیک به هفت نفر از هر ده آمریکایی می‌خواهند جنگ با ایران «هرچه زودتر» پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125200" target="_blank">📅 08:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125199">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acn-PFUiLkW92nWdfdNKZ5g70PxIhX6H0aFbZ142bX4Z_Jr677LruZlOAqy0DyVB5ebS0VTv5hTWDauLxllFpjTOOZi5Tc_f2EzaJs_ZTTPgSfvMDny_cbMQ_UdgSMcTGlp2HE04AfJ6rF4d1iGeYla7t5LxkODkVAIJ8jnbWEmBwMbDf1VNLpRh5cA3-jD15DFxmoBmqd8yqPDbHP1weh_jSz1apdccTsU_1PPWZDzytsVrJVnf-HrJ3e-JDDezg2pdT8W36jLVWokrR0YgV_mAaD8kGcSrOaj3ZrD-C2QtygiCL5A9qcc87WO3_TNWtUjZvihAc9qUgXnqhi407w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت وحشتناک و باورنکردنی ۴ قلم جهاز منزل
... !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125199" target="_blank">📅 08:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125198">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز: بر اساس اسناد افشا شده پنتاگون، «استارلینک» با کمک دیش‌های قاچاق شده به ایران، ستون فقرات شبکه نظامی آمریکا برای هدایت پهپادهای انتحاری مانند لوکاس در حمله به ایران بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/125198" target="_blank">📅 08:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125197">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
خبرگزاری دولتی چین: شی جین پینگ، رئیس جمهور چین بین 8 تا 9 ژوئن به کره شمالی سفر خواهد کرد. این اولین سفر او به این کشور در 7 سال اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/125197" target="_blank">📅 08:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125196">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
در تازه‌ترین نشانه از عمق تأثیر جنگ بر اقتصاد منطقه، شرکت هواپیمایی امارات مجبور شده نزدیک به نیم‌میلیون صندلی را از برنامۀ پروازی این ماه خود را حذف کند؛ رقمی که معادل ۱۶ درصد ظرفیت پروازی این شرکت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/125196" target="_blank">📅 08:36 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125195">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
رویترز: بارگیری نفت خام در بندر مینا الفحل در عمان پس از انفجاری که گمان می‌رود ناشی از حمله پهپادی باشد، متوقف شد
✅
@AloNews
خبر جناب</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/125195" target="_blank">📅 08:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125193">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nhYTmpk_fZ7n0MeRHmh3HlynNST4NHPxSbLIoP91yhayE-4KoKkhEzVveg2lL4Nf1nOU_sHJVHqEkpoyk1JtC3R_svw4Er7MJ5rGyhKd_bIlqL8UgDDdmvBytK8YylsnmQqNqlgvS8T3q6l33b2E4mpmUvt068nUwSBxabosUxm-hlLxiYJI38t2VaujfUmvCqoBYPJj7A-We3D0Am6R80p7afc45Lg4alhK6Oyf8YnK8BSUnU8YjRuv41QlX4GxNK72JUohOnoIABRC66TnnwlYNOtMb6N0htgsa0LGBsCs4lwnd2pSDuCoB4ULxVpyY9DxBVr61pvMKjlyI0GiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JT5aSoad0vjWp-vzHVxVb8fkAOmfSb1ZKN_ukpIVddoue1_70K1Wnx1m79vO6i7Cbj6XPWmAiiwD5vysngGokRL1yTVng-8LKquVFe4A32ARdQRiT0URfJ9ppUcJrM8eCwpG7Ujlamd26wfdg2XZsWj2bXN865bHZr7vPzQqtz2Jk_udbJQhSxzOC0YiOM1NBiGwsXypSe2_Sskdny2hQs_A_iNYdBbPwUmoKz93dJ4bAJbjqh6lS_2iiVXxMyg-q-WIsecWR_XiJKwmvz196UvGldYkUgbaNMgCBds_zaNlX1xQ5WiH1jOB3bBx-Bx_N9sL0J7ZL7z2f0zh9oTgmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید و اختصاصی CNN خسارت وارده به ناو هواپیمابر USS Gerald R. Ford (CVN-78) پس از یک «آتش‌سوزی در بخش لباسشویی» روی این کشتی را نشان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/125193" target="_blank">📅 07:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
«یادداشت تفاهم در مرحله نهایی خود قرار دارد و در انتظار موضع نهایی، چه مثبت و چه منفی، است.
🔴
تا این لحظه هنوز در تهران تصمیم نهایی اتخاذ نشده و واشنگتن در حال انتظار است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/125192" target="_blank">📅 07:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125191">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UoJF-tSozp0oWP5EIgli1-86jxi-iiMqjXcI5SWLrXSWEPoaUHopHm6Ku8rl7P4OAlMwk4vQUVfh8n2Hfk1J9ZAvdr3nCCrjALBSGgFhocwvBHOPmGuN17NLQcPF6Hv3mOeLfvjQB21J3R4ZIS2XB7SwRXzjMsTYuIG-AEJil1zaNRpWs81m6W5UDptoNKZ5s_A2NIfYcKNxMjXClb479-7XweEMI-fhvUcR-NVDNRrQ1CCPVyD9JhepdbwckeiJONoBVSUeGHy1lZLL5CWpAeVKcrPiD8CtJL0YuKzo7ExoYYDyrKtJwT2xJVOPAlXglOnEo1u8O1ps8bKhpY-KNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/125191" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125190">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
محسن رضایی : یک سیلی دیگر ممکن است بیاید تا اسرائیل و آمریکا را سر جای خودشان بنشاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/125190" target="_blank">📅 01:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125189">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39099454ea.mp4?token=Gc-QEw9gkGSF9RO72H1h0G4tFX5ANUXL-W6zaAA-i4VDJpfiYL4cD8uQCpf5RmEVGWr2-BusWPAvG5yNrQDDLmo3RCPwBgfB6N_G1hYU7zIabr-_k8T5gd1FnAd0Imaupl3oJA7DaBn04g2O8tJ4q4iiYRQGnBOgFtKzKn-ICBf07A9qdomTSgc0PRP3EUcKA2Jc_s0Uhw7qxmnuXdUXPEkw7O1loi5dXbF1m1cwCJaS7STesIlq1wBza6Cjx4Sv6-FSUVNRymQF1Ez9u_N0W0Dy8fPLw6pkCTuwQzcO2fqGrJgEScAUdrsTUBAMP5ZiQNVhopMTn_hCztgCM0DvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39099454ea.mp4?token=Gc-QEw9gkGSF9RO72H1h0G4tFX5ANUXL-W6zaAA-i4VDJpfiYL4cD8uQCpf5RmEVGWr2-BusWPAvG5yNrQDDLmo3RCPwBgfB6N_G1hYU7zIabr-_k8T5gd1FnAd0Imaupl3oJA7DaBn04g2O8tJ4q4iiYRQGnBOgFtKzKn-ICBf07A9qdomTSgc0PRP3EUcKA2Jc_s0Uhw7qxmnuXdUXPEkw7O1loi5dXbF1m1cwCJaS7STesIlq1wBza6Cjx4Sv6-FSUVNRymQF1Ez9u_N0W0Dy8fPLw6pkCTuwQzcO2fqGrJgEScAUdrsTUBAMP5ZiQNVhopMTn_hCztgCM0DvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما:
پولی در قطر نداریم، پول ایران در آلمان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/125189" target="_blank">📅 01:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125188">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hauNn7vxMNxt7pXSpaaeT_bp-PJ-L7lQnMLGeSa4SRwFzxVC9lCFVNbsi_OscNsWx9eK8382qqahQgnMxrL9Wx7CZtLSfOvJdmFQyVyJV4w14B_FlTaHlmlix5fTid1LSYlxQBidcJ3cj7dLpYjfMSI8H5hDaAlB96TskPNArYNcdmyCJnj1QPTaeXjZI-3sc8XTnf-WJiKzo06WZ6SExOTrbGbIHKT0pctDeRS--SSxC2j0ubCMOPunL-eAtaEPxj3M5WhsNduMUUYTETOSb_lEsOcQLuX54o-pmkGSPq902r4b1aReEeCn3YtXqsedBl0RzJAAEz4OUXk6jiVkNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید اتاق جنگ اسرائیل:
⌛️
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/125188" target="_blank">📅 01:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125187">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ ۲۵ بهمن ۱۴۰۴:
میخوام با آیت الله علی خامنه ای دیدار کنم.
🔴
ترامپ ۱۴ خرداد ۱۴۰۵:
میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/125187" target="_blank">📅 00:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125186">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374fcdaf63.mp4?token=jiK6hI360X5LOPokPVDj7JVzLSr6R-7nHYuQzTaMxDpcf5RDUe_5z92LyRLXoxLe-Wsclj-HbYhyu-bkW_TAVlJPYfDt16RWpUHuzdOmdUUl4wmeIQkVKFXigRfuAZnK2-pp-8DRE0KlwQuX8b5IIYvkF9OZkkN9YvYELXZIT_tbkZjmrFuNJ6zwPxhgv3_FpfbTdetzvUJX8tT3SD4QSYHJ5Zix-kjbM_eMjZWrBqHqdUXdQr2y2YGwRNXO-1v0-S71uk8BHV7vZexuZFqHXCr_QzwCTmEMCnJN3iqp5Oio0vkmfZkNRKYQxAxg1BZ9e5PHIjJS4F2pVJIm1gj6mwfbJv6m0UGUSdDtymPlwPdfebTY4MylnA4M5TbK8axEQ04d0MdlxjQa7LrWEYc1DXZywdoZTinbQEfhv0TZSkBpXrAb8J83JG6bzAcdj4_sOIS8buDCLRsxK_clGcaXnJq_37T656yOdioXZZNeswh-7VIpW23iNAG6dwfCuv8gF2xgto6q30Kpp2-30sdveANpN8IjMcEZFE11U041VVK-y5-zYvOJA5MI9QqUFUuwmroZrl6EmaC_M5exQrHfGdfLZvF4CQiTcHH71zzgMiYMXmvUfZl4SNqjM-2hZIR-1C9tNIED0fZkD5Th5g0E4EN6Y5Kgw_X49fmZ3BxVro0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374fcdaf63.mp4?token=jiK6hI360X5LOPokPVDj7JVzLSr6R-7nHYuQzTaMxDpcf5RDUe_5z92LyRLXoxLe-Wsclj-HbYhyu-bkW_TAVlJPYfDt16RWpUHuzdOmdUUl4wmeIQkVKFXigRfuAZnK2-pp-8DRE0KlwQuX8b5IIYvkF9OZkkN9YvYELXZIT_tbkZjmrFuNJ6zwPxhgv3_FpfbTdetzvUJX8tT3SD4QSYHJ5Zix-kjbM_eMjZWrBqHqdUXdQr2y2YGwRNXO-1v0-S71uk8BHV7vZexuZFqHXCr_QzwCTmEMCnJN3iqp5Oio0vkmfZkNRKYQxAxg1BZ9e5PHIjJS4F2pVJIm1gj6mwfbJv6m0UGUSdDtymPlwPdfebTY4MylnA4M5TbK8axEQ04d0MdlxjQa7LrWEYc1DXZywdoZTinbQEfhv0TZSkBpXrAb8J83JG6bzAcdj4_sOIS8buDCLRsxK_clGcaXnJq_37T656yOdioXZZNeswh-7VIpW23iNAG6dwfCuv8gF2xgto6q30Kpp2-30sdveANpN8IjMcEZFE11U041VVK-y5-zYvOJA5MI9QqUFUuwmroZrl6EmaC_M5exQrHfGdfLZvF4CQiTcHH71zzgMiYMXmvUfZl4SNqjM-2hZIR-1C9tNIED0fZkD5Th5g0E4EN6Y5Kgw_X49fmZ3BxVro0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی:  اگر اسرائیل به سمت جنوب بیروت می رفت، موشک باران را شروع می کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/125186" target="_blank">📅 00:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ایالات متحده رئیس‌جمهور کوبا، میگل دیاز-کانل و خانواده‌اش را تحریم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/125185" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThbcSuV0YEfBTTURtPDhmghi44y7wJRzYXGvuEYpCToxxUHV8qd9Aykga6FfGLNVWgGKvtbOglZ5c4KaLQBDDM3Uu7bBKUxunRiJEKea1pvjhnTIgIhMORcePSLREsdmirghtzr7XYXg3p6sCYujUd6DVbz8mHit7kh98OqPcLahlwO_1sQndokQZVSRQT6Xrh4FcIYBdIeAjfPkY70qqML_cblUWcSh_Wd0FETxS8gL90_RxdDX2Xis-Kt9f7EDmCrduivv5ppSFBCxj8EVuU5_H2hjloZNzlAsJSVDIVj97h-E22j_mk1-3oAocPasBXchrFv2LlDvO2BLE15xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه منتشر کرد: عکس وزیر کشور پاکستان محسن نقوی در دیدار با وزیر کشور ایران در تهران، در چارچوب تلاش‌های اسلام‌آباد برای پیشبرد مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/125184" target="_blank">📅 00:26 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: باعث افتخارمه با آیت الله مجتبی خامنه ای دیدار داشته باشم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/125183" target="_blank">📅 00:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKAFZPGBRdELZZkYf22cdvP2lpMa-DY7wQs-YN3gAK-25MDQ9gDr6-5Z3QL1ithf6EMSkwTtklRFwm4WWGi2KmIx72yQOrHcJ9QZemhZCDn7G_rEThbswuOsVZlSpCOkPOC3Uvzpme0tkG8dF2JvQWSccJSLK82NrpuBwn1d4iVGcEF01CDoz40mMTFCq96p1IollvTq853k8Vr2367wOn9vBHyEqf2BXW4xL_vdEdolq7t4HDD1m0eew37L5pg8jk-8tfGZ_ICJhgCwEeNMQ4hcfIz-KUI-eUaVZrdwXgMg5-1mysnpU68AMT1uebaB9iyNQMTrtUcuDJLujGm6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حجم قابل توجهی از ترابری های آمریکا در حال خروج از خاورمیانه و حرکت به سمت اروپا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/125182" target="_blank">📅 00:20 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/125181" target="_blank">📅 00:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3651e966b.mp4?token=M9jBbQMB__wY48ZODt0D6p4oitgfDI5dG9oVcT9pKwGzowZp-sXYv6cR6zJCma_QLaAehMsjYCmkQuu1_7RWlsiNc265DIEKaureQleK4PnJFGSXV2kdgXnkGbotXVfCJGJqK2BLEKvh4jDHZ2q20uNJoqg9fNeQORhd65Cw43Szj_hfTcCYcQur_9FR1IXfjacQqMj3m61T8nzKmso0uxcz0Rngj66FUzsoC0pbcPATPU-HbbYyELTR0HYoQD4cQOgyd3PliRnfs6-s3EdiOvnvSZhpyLrm7NDCURFZfPPYeCtOiqB6jfrya1CAgshdEXxOec2bxOCxmK0HjXd0LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3651e966b.mp4?token=M9jBbQMB__wY48ZODt0D6p4oitgfDI5dG9oVcT9pKwGzowZp-sXYv6cR6zJCma_QLaAehMsjYCmkQuu1_7RWlsiNc265DIEKaureQleK4PnJFGSXV2kdgXnkGbotXVfCJGJqK2BLEKvh4jDHZ2q20uNJoqg9fNeQORhd65Cw43Szj_hfTcCYcQur_9FR1IXfjacQqMj3m61T8nzKmso0uxcz0Rngj66FUzsoC0pbcPATPU-HbbYyELTR0HYoQD4cQOgyd3PliRnfs6-s3EdiOvnvSZhpyLrm7NDCURFZfPPYeCtOiqB6jfrya1CAgshdEXxOec2bxOCxmK0HjXd0LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا تحریم‌های شما علیه کوبا با هدف تسریع فروپاشی این کشور اعمال شده‌اند؟
🔴
دونالد ترامپ: نه. ما فقط می‌خواهیم کوبا کشوری باشد که به‌خوبی اداره شود و بتواند مردمش را تأمین کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/125180" target="_blank">📅 00:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991275c480.mp4?token=Rfxw4s7guAqRvOr9tQ1I2wDTm4pS_vxek0V6jEFlLY0IEZZmzXTSGirwx1tVDOFN0CnM6DQplSIXMx-3Cm6F989UrpGk4AX8cmbYSd9Wlwa-c5ohtoPls8BW0QFgFesXmpZWuNienEvdxYJm7W1pJH2nwPcsuBmRaXtvHkh85bLHHylDR9JrZV_bfxzQR8bw_fWOP3RUiR2rq2s6StoK6vWAOJYwTxlUg86lfwmsrrHsJvZyCFGrJFV6D7uDSJMAge8z_gSApzMAz0xf8aHUtPnFsfph1tBH9gM2gCkKtSRfpfy5fkJuBNjO37uAJJJv5jjW7BTpC9_3ft4qoF_D2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991275c480.mp4?token=Rfxw4s7guAqRvOr9tQ1I2wDTm4pS_vxek0V6jEFlLY0IEZZmzXTSGirwx1tVDOFN0CnM6DQplSIXMx-3Cm6F989UrpGk4AX8cmbYSd9Wlwa-c5ohtoPls8BW0QFgFesXmpZWuNienEvdxYJm7W1pJH2nwPcsuBmRaXtvHkh85bLHHylDR9JrZV_bfxzQR8bw_fWOP3RUiR2rq2s6StoK6vWAOJYwTxlUg86lfwmsrrHsJvZyCFGrJFV6D7uDSJMAge8z_gSApzMAz0xf8aHUtPnFsfph1tBH9gM2gCkKtSRfpfy5fkJuBNjO37uAJJJv5jjW7BTpC9_3ft4qoF_D2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مجتبی خامنه‌ای: او در برخی محافل شهرت بسیار خوبی دارد.
🔴
خیلی‌هاشون درباره من بد می‌گویند. البته این کاملاً نادرست است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/125179" target="_blank">📅 00:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125178">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ درباره کوبا: ما بعد از ایران به کوبا رسیدگی خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/125178" target="_blank">📅 00:10 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: ما در جنگ یا از طریق مذاکره با ایران یا از طریق دیگری پیروز خواهیم شد، اما قطعاً پیروز خواهیم شد.
🔴
مهمترین نکته توافق این است که تنگه هرمز فوراً باز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/125177" target="_blank">📅 00:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ در پاسخ به سؤالی درباره اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران:
🔴
«من نمی‌خواهم جیمی کارتر باشم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/125176" target="_blank">📅 00:03 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سؤال: آیا کشته شدن نیروهای آمریکایی، خط قرمز شما برای پایان دادن به آتش‌بس است؟
🔴
ترامپ: اگر آن‌ها کسی را بکشند؟
🔴
سؤال: نیروهای آمریکایی را.
🔴
ترامپ: منظورتان چیست؟
🔴
سوال: اینکه اگر نیروهای آمریکایی را بکشند، شما جنگ با ایران را از سر خواهید گرفت؟
🔴
ترامپ: خب، این می‌تواند دلیل خوبی باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/125175" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما سایت‌های هسته‌ای ایران را از فضا رصد می‌کنیم و هرکس به آن‌ها نزدیک شود، همانطور که باید با آنها برخورد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/125174" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125173">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=diq3itqFz7JZueNQ-k1WbHgEjR7-k4zNqJ_x1dOkb8FVWm0C-RwG8X4GZgmNcKYsy3O9s4S85L4dl6-1_OlP_5TrF0G0fC3NZ-UYgS0ZYEo2IEgb31DZoDiRD6clYa3a5q6mpz-7MLL-W9DAhIj02V7JLZ6O0_AkKPfHZm4uPXsx6YINHkRIPI27myNBKBoNBEOOuBA41VsgWpV9VLDmHDG498jfp0yjsf9GRilfXDzLwnggCIOrp0mGmVYqkgVMbrCsseZTFAvnWmnXcPpUBFu_WTmgG951sLmgyzeTqEw4rLtFEUCqLBqVnlL2jRHATkffPyMiKn8XNTk-Htp-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b30ed4f9c.mp4?token=diq3itqFz7JZueNQ-k1WbHgEjR7-k4zNqJ_x1dOkb8FVWm0C-RwG8X4GZgmNcKYsy3O9s4S85L4dl6-1_OlP_5TrF0G0fC3NZ-UYgS0ZYEo2IEgb31DZoDiRD6clYa3a5q6mpz-7MLL-W9DAhIj02V7JLZ6O0_AkKPfHZm4uPXsx6YINHkRIPI27myNBKBoNBEOOuBA41VsgWpV9VLDmHDG498jfp0yjsf9GRilfXDzLwnggCIOrp0mGmVYqkgVMbrCsseZTFAvnWmnXcPpUBFu_WTmgG951sLmgyzeTqEw4rLtFEUCqLBqVnlL2jRHATkffPyMiKn8XNTk-Htp-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «من نمی‌خواهم با آیت‌الله ملاقات کنم، اما اگر با او ملاقات می‌کردم، برایم افتخار بود که با او دیدار کنم.
با احترام رفتار می‌کردم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/125173" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125172">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f44b60c6.mp4?token=Dc3pqRB8bvjFqzhtLYUlROD6IXrsQb5kVqWmOTkj3m1oQTn8KWKsi2FfInfMM28LzRlQrfQBpJOBFowu8cjuvy0A1_vwZVPr3AAKm0kmxr37x6GKH12kYrAG-lFKkpaYgSDrJvlhwIgcU72OeE5IEGGl1uU9RID7yyWK-nk0eCQLSWAdSiOJHYxnxAgzZ8rqSYTyHrDS1L-rvH84alIxkZGbKvH0Ct9XmtPJvD-ccXJkY1Bh_esizUue8WfsmT_UDKcdmcL6oI3AYiuGCi-vIZ36MwmymZbKd2WILSCYSBd96S8-zGDdGP-0SjzW3tXqEgjtuNS1P1MnSk0geODDPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f44b60c6.mp4?token=Dc3pqRB8bvjFqzhtLYUlROD6IXrsQb5kVqWmOTkj3m1oQTn8KWKsi2FfInfMM28LzRlQrfQBpJOBFowu8cjuvy0A1_vwZVPr3AAKm0kmxr37x6GKH12kYrAG-lFKkpaYgSDrJvlhwIgcU72OeE5IEGGl1uU9RID7yyWK-nk0eCQLSWAdSiOJHYxnxAgzZ8rqSYTyHrDS1L-rvH84alIxkZGbKvH0Ct9XmtPJvD-ccXJkY1Bh_esizUue8WfsmT_UDKcdmcL6oI3AYiuGCi-vIZ36MwmymZbKd2WILSCYSBd96S8-zGDdGP-0SjzW3tXqEgjtuNS1P1MnSk0geODDPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی ایالات متحده:
سیاست‌های انرژی سبز دموکراتیک، قیمت انرژی را بسیار بیشتر از درگیری در ایران افزایش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/125172" target="_blank">📅 23:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125171">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: بایدن و اوباما ایران را به داشتن سلاح هسته‌ای ترغیب کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/125171" target="_blank">📅 23:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125170">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1215f2431.mp4?token=hF8hTjUqZcSW_wBygtjRZgPkdPhBb0-SO3ZSVAqx5YtFBa3Ao-t3zc01JdIqzzF7hubmRGdA-bIhm7_8ZewfSeXm48FY8ZgLKcRwc5Pn0UIqTqk2rRjq5OuA2xYWF-RHHesK-3SiCn1mUBZle9fFxuqpe5HHMZa5HFRhnVsaZp0SJjZ1OsdQV1kAPX0MKtVn3D5OSfwJrveNL69Y5lhaX4a4Ci1VYo8czqqNVefnU0NbDogYNBv0SrfP4dt53wvRcVxGdzAFdxbEIWMdnmP393HI_7lcI01nD0HQJO90XFjjwSvP33Yfaj4iW1zdCKzWufWjEcLUtK6AwwdwsFJXPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1215f2431.mp4?token=hF8hTjUqZcSW_wBygtjRZgPkdPhBb0-SO3ZSVAqx5YtFBa3Ao-t3zc01JdIqzzF7hubmRGdA-bIhm7_8ZewfSeXm48FY8ZgLKcRwc5Pn0UIqTqk2rRjq5OuA2xYWF-RHHesK-3SiCn1mUBZle9fFxuqpe5HHMZa5HFRhnVsaZp0SJjZ1OsdQV1kAPX0MKtVn3D5OSfwJrveNL69Y5lhaX4a4Ci1VYo8czqqNVefnU0NbDogYNBv0SrfP4dt53wvRcVxGdzAFdxbEIWMdnmP393HI_7lcI01nD0HQJO90XFjjwSvP33Yfaj4iW1zdCKzWufWjEcLUtK6AwwdwsFJXPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  روابط ما با ونزوئلا فوق‌العاده‌ست. کلی نفت، میلیون‌ها بشکه نفت از ونزوئلا خارج کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/125170" target="_blank">📅 23:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125169">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: چند موشک در ایران باقی مانده است، اما بسیار کم.
🔴
مذاکرات با ایران خوب پیش می‌رود.
🔴
مسئله لبنان تا حدودی متفاوت است، اما به ایران مرتبط است.
🔴
آمریکا می‌تواند اورانیوم غنی‌شده ایران را با یا بدون توافق مصادره کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/125169" target="_blank">📅 23:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125168">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=SPCzicfqg3m_fno-KhgbKJOZ8vK0aWRyGN-9nBswftDZHo4oJ_f5nLYAIW_MJ56GlFFtwhdpxIXOB2kHtrgmNoVETqhQJRyFg69zYkSgDRSIGL-Pv6xDCdulVinb_NphAeqt7bC3qSIvR4jodpc2ujLKoGDxsYOCEiv8M84ryxigkzc_jj89_M-RvM7sskfNa3bKxrw8piJNgJ_F1peWw0WULz48wLwBW8eCGTpW9JJLiLSE5NpXOgiDnFNmRk924fEz1E8MWlIHSKEP06QsHdMOwzAe3zx4B--psvt5sT3kffme6MdPLlYDfpyjbADXWC0T4fQWAHPS4SD2uhb7_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433ea342ed.mp4?token=SPCzicfqg3m_fno-KhgbKJOZ8vK0aWRyGN-9nBswftDZHo4oJ_f5nLYAIW_MJ56GlFFtwhdpxIXOB2kHtrgmNoVETqhQJRyFg69zYkSgDRSIGL-Pv6xDCdulVinb_NphAeqt7bC3qSIvR4jodpc2ujLKoGDxsYOCEiv8M84ryxigkzc_jj89_M-RvM7sskfNa3bKxrw8piJNgJ_F1peWw0WULz48wLwBW8eCGTpW9JJLiLSE5NpXOgiDnFNmRk924fEz1E8MWlIHSKEP06QsHdMOwzAe3zx4B--psvt5sT3kffme6MdPLlYDfpyjbADXWC0T4fQWAHPS4SD2uhb7_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
تمام ۱۵۹ کشتی آن‌ها در کف اقیانوس قرار دارند. ما در واقع از آن‌ها در آنجا عکس گرفتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/125168" target="_blank">📅 23:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125167">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=t_6nPEvDV0cy67oMED2pTq9YIGV8QJIwB7kHBEewz4hwSzDClRE8c_2oY-zjboi1OzfW9MIJC9_PM1mFVQeCr0qzQWmjuvQ-pmOJ9sNGmn3Y3N6cnlUqVtaqMvvrGaBstY1IhFy0vPjqeldyg-lqq5tiKRQhWVO6m4ou2np4b4qhM4-AH7YJlo_wbukyM2_mhiqKPHUqVLo7WLNkAiQlIY9JUns8DWSx7heylWLUmb8gB7H-XHyJmBXWePPTwAD8s9RhLLlQ47m1NOhb-7DKif1OfZrcISwDgg8lQErYsgCBHsSzZPl2-SAm_2uL7hBitGw_Ocaciblgb5Dz7R1mZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa40321ec.mp4?token=t_6nPEvDV0cy67oMED2pTq9YIGV8QJIwB7kHBEewz4hwSzDClRE8c_2oY-zjboi1OzfW9MIJC9_PM1mFVQeCr0qzQWmjuvQ-pmOJ9sNGmn3Y3N6cnlUqVtaqMvvrGaBstY1IhFy0vPjqeldyg-lqq5tiKRQhWVO6m4ou2np4b4qhM4-AH7YJlo_wbukyM2_mhiqKPHUqVLo7WLNkAiQlIY9JUns8DWSx7heylWLUmb8gB7H-XHyJmBXWePPTwAD8s9RhLLlQ47m1NOhb-7DKif1OfZrcISwDgg8lQErYsgCBHsSzZPl2-SAm_2uL7hBitGw_Ocaciblgb5Dz7R1mZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: حزب‌الله هیچ چیزی را رد نکرد. آنها با ما تماس گرفتند و گفتند، «چطور است که متوقف شویم؟»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/125167" target="_blank">📅 23:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125166">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ پوتین و زلنسکی را «دو ادم بسیار خوب» نامید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125166" target="_blank">📅 23:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125165">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66e28cd9a1.mp4?token=E_6oMz4904O_SW29hWUhBuQ1xbd_VNsR0fr11BcgDt-6WLVIStpZSKPSTNFASFj-v3-4ctSGs1vT_zL8_Zwk-d5_I4jAwgvhN4NDGA5NPbtD47JHlH1xTgOUU1rYmiJcLY-xPfZijX3zxPc4_IgyOrchCnQMZep4vDV67caxvinM2U5NZZ4jcfJ6Zk3Xwl2sh3JEVjcR_dDXTLcFPtz2at2nyzUCo-Q9bpVHy9EUrrB4NSsJSjciqWv-Rmfx7yK20WggNT8IzOedhpbnRG4KR9pHmMXZeQG7d5kc0GARGygvybWfZPAqXXvA_E-E-qP5APWhVP-U-4oTWoIqrUwT7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66e28cd9a1.mp4?token=E_6oMz4904O_SW29hWUhBuQ1xbd_VNsR0fr11BcgDt-6WLVIStpZSKPSTNFASFj-v3-4ctSGs1vT_zL8_Zwk-d5_I4jAwgvhN4NDGA5NPbtD47JHlH1xTgOUU1rYmiJcLY-xPfZijX3zxPc4_IgyOrchCnQMZep4vDV67caxvinM2U5NZZ4jcfJ6Zk3Xwl2sh3JEVjcR_dDXTLcFPtz2at2nyzUCo-Q9bpVHy9EUrrB4NSsJSjciqWv-Rmfx7yK20WggNT8IzOedhpbnRG4KR9pHmMXZeQG7d5kc0GARGygvybWfZPAqXXvA_E-E-qP5APWhVP-U-4oTWoIqrUwT7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : پوتین گفته اگه اوکراین هم کوتاه بیاد، اونم برای صلح حاضر به مصالحه‌ست. شما دقیقاً چی خواسته بودید؟
🔴
ترامپ : راستش فعلاً نمی‌خوام بگم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/125165" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125164">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=sumLE82HOn5YMjtWDrcoi76f_lQ_yTcRThXR1-BzJk91uMR0tscYw6xJmLwCcnZxJV2ogaVD-EOXsWaVpjRk0t2GabnU3c8TnEnK-wRLJtTm_LDjdvnvuom0f1HgJ8i11I_YaUVCLm27ewvjEktsdg12h4nTUsQH-7LurkrCiJN2DSsExAq76M90ZZYtpz9rvGMkAe9Vt8zN-k_rlKd-3_m5KuzZSzwvy61pFXC41m8vuBu8zNt9LRzbUe4lxhUpEVEtB6e1ppEZBhTLR1w-89zXmlXQa8v-Ub_du_w0FRoyBdgU6uuJvj91T__UHdswo6Kc3TPTOuAMteEkl6CkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eed315e2a.mp4?token=sumLE82HOn5YMjtWDrcoi76f_lQ_yTcRThXR1-BzJk91uMR0tscYw6xJmLwCcnZxJV2ogaVD-EOXsWaVpjRk0t2GabnU3c8TnEnK-wRLJtTm_LDjdvnvuom0f1HgJ8i11I_YaUVCLm27ewvjEktsdg12h4nTUsQH-7LurkrCiJN2DSsExAq76M90ZZYtpz9rvGMkAe9Vt8zN-k_rlKd-3_m5KuzZSzwvy61pFXC41m8vuBu8zNt9LRzbUe4lxhUpEVEtB6e1ppEZBhTLR1w-89zXmlXQa8v-Ub_du_w0FRoyBdgU6uuJvj91T__UHdswo6Kc3TPTOuAMteEkl6CkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من تا الان به هشت جنگ پایان دادم و به‌زودی یه جنگ نهم هم تموم میشه
🔴
شاید حتی بشه دهمین جنگ. فکر نمی‌کنم هیچ رئیس‌جمهوری تا حالا حتی یه جنگ رو هم تموم کرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/125164" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125163">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کاخ کرملین اعلام کرد: نامه زلنسکی به دست پوتین رسیده است.
🔴
اگر زلنسکی می‌خواهد با پوتین ملاقات کند، می‌تواند به مسکو بیاید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125163" target="_blank">📅 23:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125162">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: اگر شمارش صداها صادقانه انجام می‌شد، احتمالاً در هر ۵۰ ایالت پیروز می‌شدم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/125162" target="_blank">📅 23:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DW9VktXN7OCnDgfsdOkcxJ6VimberHL8Ym-s52ydJNTGHLyHtw2UZ7wPFr2GqSvtfACTcJ643KxwoWfppyoR77L96HjYgLFrO4K6b9PFogmEyvoWUV8DXKIHRZ2bYYPiIEKj--G58M-rcoqF9tbuRFZP3P_fNRTIqRw-7g3m-s8yF8hI0YvTipgJDigdrIGRwOCPqSKyPHnW_7rHxfggLqWi_J35bp3e7VSQZulXsxgkasWnTZEbO30lzANNM3PWA_Vc1_fwDl3wtl3qUXV2kJuC1EEFtxnfllXV9T4I-52CXkXSj4Mfa7C5vkLBUmEub-7eiKb66C05hzcrkrzLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t5HukcN2uThT0zu33g0OdWco33QY5v3BiBlRxRBkjd-83cEWsxVOrCZKk7EnRy_x4p6rRt24huZl3vMIYoSA01AbGWcqhlaNBawv7lH8EHS25AEOSlj9rofCCyEd9ZZE47dmiqUWO1fj2WB8zm9SOVDNk7S9Ce3sbRwSSZglVBpMdX2NNj7wf5zAnggxOcGwyWCiAXxolLJKdRvcXdSEIns9AxMqzPbs67Xb6z2z6DLDRxPU5wxGCCg40v-5baHkBxnvyMrb-tQRGJ7201kiZuLAbJyOvvy3zq-rFG4wHgoAdKO6q6Dht7Cj5fxtNTH3hoep8mckAtFR5ESSVfHghQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFBwo3kGokFkNcQb1aaghBILIJnKwVwUGQa2vkpjV-ah4TgLUoXQ-DcjbTzxULL_WcIDmJLjfnQlX27IX2jKeL_dT6Z1D4j14-6kgRT2baWrnRA_z3Yfe4uNWsrV993ht9frEutRjhfh5w_LfKo0igVI9kRGYI-wjGT2W6H2rt5LbL75zzs7diY-rCdlcDow77Hh9Fyz0rMtXwLQ5vwz5DlehSj1zr48Wl0vDakXMzUu263EtktnWKxZ2qp2Gws-D3GL8kusNlDS26Yyg7YWqo3t-1_bC8oIGHnCAcOae1xukew7IDJCMiKIipv_jtTL1kRrwfh4aURHrd1KdzESTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2ba44a48.mp4?token=o4-tYWfPwPEH4TIP96KtHau0lZj_Xwfm6ujJUnHYTNWCR1cBApM2vGjLF0NL1iFUdQM9CnSwwoP2I2xZPLtd438qyZSJgHcQIJVS2UbgevCng0n8seowv2mjBLanTYpshVV_r0_5t_ZvtwwtXHzZlTsfSCXpm5rgP5yqy9o2g-CUWBgx9foVHGb_SkeAXb1gpZ2ADowoaeOC-BLdCVQHoH_0X3U9572ViDfSoAU031yuKviCVJ-Yj1lKlhASPihYpnX6_r5XVJjKUSbrKMv1eSFCx0RRzT_6NKBX-K_BWyMPHj5odSva13kGLZOKycWyOnswcNjLqt2ERJCmJlJQ0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2ba44a48.mp4?token=o4-tYWfPwPEH4TIP96KtHau0lZj_Xwfm6ujJUnHYTNWCR1cBApM2vGjLF0NL1iFUdQM9CnSwwoP2I2xZPLtd438qyZSJgHcQIJVS2UbgevCng0n8seowv2mjBLanTYpshVV_r0_5t_ZvtwwtXHzZlTsfSCXpm5rgP5yqy9o2g-CUWBgx9foVHGb_SkeAXb1gpZ2ADowoaeOC-BLdCVQHoH_0X3U9572ViDfSoAU031yuKviCVJ-Yj1lKlhASPihYpnX6_r5XVJjKUSbrKMv1eSFCx0RRzT_6NKBX-K_BWyMPHj5odSva13kGLZOKycWyOnswcNjLqt2ERJCmJlJQ0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/125158" target="_blank">📅 23:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: باراک حوسِین اوباما، آیا درباره‌ش شنیده‌اید؟ باراک حوسِین اوباما، یکی دیگر. او نیز یک زیبایی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/125157" target="_blank">📅 23:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8Mq24n47lxUf-RmO7An0uBO1f_Sg6aDNbPx5TTTCJOq_DpRqNXibUFruJnT2VMmKN4kTLPie78E2Lz8VJ1c5p_9CumYDc36MJha4CJQvp0fftcS2LSmXmXq_9hPIf7V04nN0GO4eOYdQyf3rtejJLcw3Yyx7M-kz5j-Y3yrKTJvYcsbJflbP8w-h2ag2jjg89zHy1nYxh4yTL6Tp1nbDhq_8n3ju4gs28n7ij-3Zebfq5WJfdIkxp4epWebfwd8E0MDz0fWk3ysFwVFnVPCSE-LQavwiaqRfU1IjyuYduUz2-rzNUrZCOkJ942m3OlOnQIkHodAl8prZVweR5rWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پولتیکو: انتظار می‌رود پنتاگون برنامه‌های خود برای تأمین موشک‌های تامهاوک برای آلمان را لغو کند و به نگرانی‌هایی اشاره کند که روسیه ممکن است این استقرار را به عنوان تشدید درگیری تلقی کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/125156" target="_blank">📅 23:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125155">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VINb-LEqDrU9oGizWFAGST2eoGB-2OM6rG8dv_IYJk76-ARmWTndZ3373V_v26aSxLcoOn7t4pbV816zCZIGVSAz20tlei3p_BuIFgyekvoo3M6ux-SahVIcgGF768FL87nHNmPajAuCQfWmDrQ_SHEd-jgmiz6xV5vk0DYGAtcCIV4nO3QSvNPKrgPvLGxpYPvCcoHnOB2jNzXuUhM0a8nObH37iRfmzqsocdyFzpFPGCJH_ZuCvdQqFbOXioshhdVURHyPsA7riS4iM4z9WiKoiyWPoY4KCGop_dsk4jBWc5e6j1cIQ_-nvN1j8oov_7ZpzetRTvXv2tdLDs2Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/هفت فروند هواپیمای ترابری نیروی هوایی آمریکا در حال ترک منطقه غرب آسیا به سمت اروپا هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125155" target="_blank">📅 23:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / دقایقی قبل وزارت امور خارجه آمریکا هشدار امنیتی برای سفر به امارات متحده عربی، عربستان سعودی، بحرین، عراق، قطر، عمان و اردن صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/125154" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: آن‌ها در حال تقلب در انتخابات کالیفرنیا هستند. شاید نتوانند از این کار فرار کنند.
🔴
این بهترینِ [کار] ترامپ است: بدون جراحی "تخفیف" ترنس‌جندر برای فرزندان ما.
🔴
اگر به چین و بسیاری از کشورهای موفق نگاه کنید، آن‌ها از زغال‌سنگ استفاده می‌کنند.
🔴
اگر به برخی از کشورهای واقعاً شکست‌خورده نگاه کنید، آن‌ها از باد استفاده می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/125153" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bed311657.mp4?token=TDrFgiFx3KIgQzlartg2JR-p23fvigF1q8ptApH3BppOXilRu0RYRYE5bxoDysdHynTi1yUdA3yjFEA-fWHEVZu7rXADyRNu3f2iqxlVSLN-biUQc3I3FZzildNusPArLoULRJuyuzRw0r_gHslEoBLkbwDoCcGeDnqtaFmfWIJzmVD8L7lPeX53Cp0QGKUe80CNLOKfaMdpoHrKksSAcU6KZXkoNrXsqgEkpxF_gy5m1JUpOPX594GjfDR-47rlqpLfis-dlUekk7V8TCqgewuJJbOgv6leCCMv2BVTsWGQIoajcAQjkRLzJBDkKuWL9gg6HlcAwXGHh4KeZxV0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bed311657.mp4?token=TDrFgiFx3KIgQzlartg2JR-p23fvigF1q8ptApH3BppOXilRu0RYRYE5bxoDysdHynTi1yUdA3yjFEA-fWHEVZu7rXADyRNu3f2iqxlVSLN-biUQc3I3FZzildNusPArLoULRJuyuzRw0r_gHslEoBLkbwDoCcGeDnqtaFmfWIJzmVD8L7lPeX53Cp0QGKUe80CNLOKfaMdpoHrKksSAcU6KZXkoNrXsqgEkpxF_gy5m1JUpOPX594GjfDR-47rlqpLfis-dlUekk7V8TCqgewuJJbOgv6leCCMv2BVTsWGQIoajcAQjkRLzJBDkKuWL9gg6HlcAwXGHh4KeZxV0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/125152" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/125151" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6SdA_lTNrx4INmLpSF3DiPhSOS3ZedRS3qZlxMSWiYP6xzuE4sSWlZB9BvLRohNWjfLok19D_oY7wZSumls11yYd6qKQOnXoEjt6fdSsH-aYQbsrPDNZEVbclYEnxYgcbxZ5aSeMLIKtSAcFe25p2FWRgeMZibZwQtb_5Se_ZII4Y6wL609Q0PNrCHiR13q7_DvXe0jmOZddHnNjKUOYJYnQOOe_m3NVsXJC2do62ht2PvZIY7GRiWbjHr9o3xTZjmnVLTzRVvMq5cMaUATsCdmyu5K4KjD0jj0ikUTi77qZ_-CO2RfcXk8WvxceF9RvwvZ4BqBU8xrrBeklqKP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/125150" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125149">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عراقچی: اینکه ۴۰ روز در برابر بزرگ‌ترین قدرت آشکار جهان که مجهز به سلاح هسته‌ای است ایستادگی کنی، شوخی‌بردار نیست
🔴
جهان به میزان قدرت واقعی ملت ایران، دولت ایران و به طور کلی جمهوری اسلامی ایران پی برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/125149" target="_blank">📅 22:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125148">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت و گو با الجزیره مدعی شد: آتش‌بس با ایران برقرار است، اما ما به حفاظت از نیروهای خود و اعمال محاصره بر بنادر آن ادامه خواهیم داد.
🔴
یک مسیر کشتیرانی آزاد از طریق تنگه هرمز وجود دارد، اما این به کشتی‌ها بستگی دارد که تصمیم بگیرند آیا عبور کنند یا خیر.
🔴
از زمان اجرای آتش‌بس با ایران در ۸ آوریل، تقریباً ۱۰۰۰ کشتی از تنگه هرمز عبور کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/125148" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125147">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقامات نظامی آمریکا: مناقشه جاری با ایران همچنان حل نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/alonews/125147" target="_blank">📅 22:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125146">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عراقچی: ما اسناد و مدارک بسیار زیادی داریم که نشان می‌دهد از آسمان کویت به‌طور منظم علیه ایران استفاده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/125146" target="_blank">📅 22:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125145">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1LzUjTLVIywwbm3Rz4KRkGz5TiF6lg2m6EaHdy-TjY2pmQdOdvVUsOeaUMl2CxhHIxxns67fR9_W8oeLvf7TuPFCYzDAinbI8Fodg8E35lYGshkzMcYOadEeYTL2MflhMp71k54_3QcSzcH5TQvOD5FBdRWnip_zHRFF86Bc4ZM7a3TsEIxBtBfSV2sKaK_n05lO3HmDPcXFnX66hKo5p0rTImK7f7K7pE9r1tJkvffmdvDJhgM5dPoEaiBHH9tHll1c7iiCpiKkfggXg_DN15gWK5on297oU4Q0qslKcbtGFK25IdFIibUw9wWyunZj62tVFC-xjTNg8DAnICrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) اعلام کرد که سربازی در لبنان کشته شد: سرهنگ عیتان شمئول لمبرگ، ۲۱ ساله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125145" target="_blank">📅 22:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ادمیرال محسن رضایی:
معنی خروج از NPT میدونید یعنی چی؟
بهتره هرچه زود تر محاصره رو باز کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/125144" target="_blank">📅 22:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJ8V4dLGiW8GT4KWsNjS3-x13qb_lJxS2Kis5-QPPHwExB6rQoEh7q3zR_eNJ-rimodBf1mVGFT6M5jHNPSVBSXHJPPJlzP9_P1-xzZh39__GQYANbplwR2FmtdzIxlVejp0WnOVSY64GJ_VRHU9EG9Tj7EWfEBxhviEZxuIdhP5yP0aTiUp4X5HG3dSjVCJ_gbXYUjjGjlQclErDBgofgyqeVAz4cnxb7fcr1TaM4v__itzn221uLQeSMfYY8pKPGfe44UYpgatJbRnKU-Bw7vjgbRqbw6vVmvMwZeWmEHk1dju60ZS6Mwrih7Nzm9a33-1ah-_s6mHxiAsccbRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاکس نیوز:
حزب‌الله طرح آتش‌بس پیشنهادی بین اسرائیل و لبنان رو رد کرده؛ طرحی که می‌تونست روی مذاکرات گسترده‌تر بین آمریکا، ایران و کل خاورمیانه اثر بذاره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/125143" target="_blank">📅 22:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZlCjn47dfgwRRZ4KVBIjYyJ4wkfP6zmylpjl5iAvwXUIBF9yAK_AdbBtD9R_4nysAmzqIr6vrZysDK2-HFl1B3uTtc-bzQU_7Ki1xjZLfF8YkvICQ8J5z7Yjs8q8o32UNV99V37nBFsMFRhHC8N31_dhdbYSFt64ZFDmGgtGKfe7FYWlMPcWVK--EGYt6_QVbYr_hjgELI_k7vIt6R8JxKFDJisf36ZLFKaXVwxj-NTrxDt6e_2BjJLzdvlqw0nNOBn5j5yR_p0agZ-d59MZrSkionQlliBmUuncvDZqZ6FplOE2HQh88jiqgh8_lNhAFgkCGKtowll1Ey30z7tVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یغما فشخامی، خبرنگار: قضیه تجاوز گروپ به شهبازی بو داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/125142" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
عراقچی: رابطه ما با سلطان نشین عمان بسیار دوستانه و برادرانه است و شما شاهد بوده اید که در جنگ اخیر هیچ آسیبی به آن وارد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/125141" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0bm4x8FRWqYPaJIN_1pdNfl7wGXTO4t2BG7qiwKmn699rx2PLVEchEXqXzMTOI91veNZjp9q_CHAli4axgRnDNV8i9mg47bEN3scbTqSQyQg6v6b9SUrdZK3mc6Taw9Qb4LQtSQTBVwFphJmQXl-cfznV7oeCgx57vkcmpDIzzrhAQmFZWqhToeZ9gVhrp8KpMdTgn4KlC_oqfDVmePPU9-u_yDcRUNR6lHzbQKNISfuh1X5p3Ry38ITAhjjt3CXzKYK6FyLo7yQnhAT7NaHg5jQIIFiJ8pxc9m9Zeci4oZIlWva1L6mcnRHvv0xbmDjWOSPOXi0JvpRrS4tmkihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/125140" target="_blank">📅 22:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پوتین: ایران یک کشور دوست است و کاملاً به ما اعتماد دارد؛ از اورانیوم غنی‌شده پس از کاهش سطح غنی‌سازی، برای انرژی هسته‌ای صلح‌آمیز ایران تحت نظارت آژانس استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/125138" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125136">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5d73a4c4.mp4?token=gIC_NWpRRMXUFy-84JCG_wobSeI9H0kQuRWXF_Cl4-qe8ypuN6qePxM9AmuzXzBhrXbCT5EnyiCfNRn6Knip7Qna83aaI_LW0m-BOJwk4T4KeGOr36HNt6hwYC2FNEt317RSeOqsetMNHhUI6csqNLbj0hRryjhS5gqHoS8wV8TY1YrvX20UNdvcVnYoaFV5dWZOsMgMBTHlbuQOzr1TbHwlSp0th2cEIkj4Clv9AmxsgV-BRCSFvb2p7Hn9vSEYR744HcjjIeAa9z5hilVPoViM5pv7dNOYz-wBYqZtRhtd0Mtcc05kHjMNqn8IesZqLdhcEkX2kF7wP98rR05rIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5d73a4c4.mp4?token=gIC_NWpRRMXUFy-84JCG_wobSeI9H0kQuRWXF_Cl4-qe8ypuN6qePxM9AmuzXzBhrXbCT5EnyiCfNRn6Knip7Qna83aaI_LW0m-BOJwk4T4KeGOr36HNt6hwYC2FNEt317RSeOqsetMNHhUI6csqNLbj0hRryjhS5gqHoS8wV8TY1YrvX20UNdvcVnYoaFV5dWZOsMgMBTHlbuQOzr1TbHwlSp0th2cEIkj4Clv9AmxsgV-BRCSFvb2p7Hn9vSEYR744HcjjIeAa9z5hilVPoViM5pv7dNOYz-wBYqZtRhtd0Mtcc05kHjMNqn8IesZqLdhcEkX2kF7wP98rR05rIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین در مورد اروپا: آن‌ها به سادگی مایل به گفتگو با روسیه به عنوان یک شریک برابر نیستند، اما مجبور خواهند شد که این کار را انجام دهند. ما عجله‌ای نداریم.
🔴
حتی اگر نه زن باردار را با هم بگذارید، نه زن نمی‌توانند در یک ماه به یک کودک زایمان کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125136" target="_blank">📅 22:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125135">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8hb8Q-fZCd3cgGjGWz8WL67iBRD5YvrZpBkX4XqpQuS6yt3UffLXJ9e5XpXFJMYoJITXNDvenu1jOKFQ9P8pQo-Mgq_ck3-XPsrYOJBnOybUS_rrx-XvT32wTX5HzX3Ms4KZt0gBsj8ValI_KjVULZNADwFewsAnjTWspFnSF3pC8CMUq7lw-sCjOhgwaeZnhMO1Rzez5MuDTwJHnWpnlHG6J2j3KZh1ad7MmVZXFRdVsdiM0Q_mdRTlwGDu53-qjCDmiVw4l1gPbcM18kt8vk4jdPpM5dQv7-naaGNi4iAAbwlc8m0xoSXW8SnxKAw3wmm4_Vpi-DnG0n4aj_Ilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایالات متحده در اورشلیم هشدار سفر جدیدی برای اسرائیل منتشر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125135" target="_blank">📅 22:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125132">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XqDAUNlkCsq77_S1kY3XhGiz9g0y7nOHhUchGYL9KTRp03xjpKjRrQcIMOMb1NHFcwcRgeWwYzG7oVjyeOslnXa_8tGGWaxh8OXZD_UbbEfysGh4kVELsHhg4M5vQ7L8ZQfldBaUWY4Ml6fZ0sQCM2rxUGFhmia2JyMlLAPH0kVpFfmviFilRYIdOFRawbAuMwCQij0LzuPNDngHIPQY8kOpOHA9EKhrN7ZS9o7xBuxQyGf-qbnLQk9WvlB7px_uuCt1FqU0ZBTsjwkimp7BvL0NX7BC7Ho1w_9akIuumQ2nk2p8aqpfLrgBGNeBWPv6AkTQslmGtU-bTaRdik8-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5YQSgV2LZ-HqtATi6B_zMioOAPpSkrLxRGCEangZVRoYb09yBviM_wPri_eP4bdl_EQpTh1HEiARM-4DxAuBLzRE6w1ojcSa18e5Q7uz5VbHIUvjkgHBP55tixeHw_6Y9KQ4BNYQl0Er7CeoJdj8KflkWotX6keSuUkTEmMlqt5-NHTc3cIeQSGtB_OqAIgpU_5rWdsvqmYb09Q1qX3tMrxKMg75jQX7cpkBfRXggir4tt5t4CJpOcrreVBJgP__ynBq4Jcw2cZ0JTKdQDHSU-by2pNmdbBP1pvL4Fi396PY3AcUwsGmm7Kh0p8QRVbDK6abllavd-0Ak2fu2tqwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
طبق تصاویر جدید ماهواره ایی، ایران علاوه بر تعمیر پایگاه های فعلیش، داره به طور فعال پایگاه های موشکی جدید حفاری میکنه و قبلی هارو هم گسترش میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/125132" target="_blank">📅 22:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125131">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ_f6jRIss3XnLjfkfH8H2gLpCJHslc1BTF0xRaT36uvYPcObfo45w5VrAd4jhliZmboQ9VJoT4ShXFdTvfV7xsnMsa-fot4qq-ABw3p2YyTQJejPkmJ3svEHFJrBk4HsBPFu4T_pGkRdl8pKmLttNVR3F9qEYvfuzzwwbjeN5ecTyuLY377zKb_KPKqig7Fln2DPRW7isxGy-AizO9Eczl65PDIZKdG9rxJhzasUSO9OB5_HUGFG_2KV_sfFHMIbMKGwoPTH10siTXlVVpssFeAgZ0iB9H3pnAmrm_WLAi8hi3xQThzDafz-lZz-pjfoi4IDfoxVCY4rkIDsSpC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏هواپیمای تهاجمی عمود پرواز AV-8B Harrier II  بعد از نزدیک به 40 سال خدمت از سپاه تفنگداران دریایی آمریکا بازنشسته شد. جایگزین این هواپیما F-35 در مدل B خواهد بود
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/125131" target="_blank">📅 22:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125130">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=ljH2HmVcAL8OiiOC3ihplDod6Yjg1zyxG-QOG269cL0e_Iwoh7hzWde4gVVOx0ue468EWe3RXgCXf8r4vIS7ecVt5__y6mEsr6npLqcI0e73VJ8Eli3Aaz97ckd8Da2oF1IoZ43QTpXe6Qyi4b5S7VRt6Odz_5NC_zxq4IiyXM_hKeNcqtZAZ1HpaDr_KnqnE5cPPa-SLhwBMoFHaI09wvkPu2184Bp_RK9Y9_4Q4HDQ6kGz3Om8DA6PJcXTWGCm55IwtQw8mxpURcfJKlhzsfdWGTQ0fnGXaES0f59ehC1ScEImFbb4haKrozcAu4LpV5z1CvPBsYjU99pPMebRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=ljH2HmVcAL8OiiOC3ihplDod6Yjg1zyxG-QOG269cL0e_Iwoh7hzWde4gVVOx0ue468EWe3RXgCXf8r4vIS7ecVt5__y6mEsr6npLqcI0e73VJ8Eli3Aaz97ckd8Da2oF1IoZ43QTpXe6Qyi4b5S7VRt6Odz_5NC_zxq4IiyXM_hKeNcqtZAZ1HpaDr_KnqnE5cPPa-SLhwBMoFHaI09wvkPu2184Bp_RK9Y9_4Q4HDQ6kGz3Om8DA6PJcXTWGCm55IwtQw8mxpURcfJKlhzsfdWGTQ0fnGXaES0f59ehC1ScEImFbb4haKrozcAu4LpV5z1CvPBsYjU99pPMebRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آب زاینده‌رود به اصفهان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125130" target="_blank">📅 22:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125129">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🔻
بیست سال گذشت و حالا رسیدیم به ششمین و آخرین جام جهانیِ مسی و رونالدو. این آخرین تورنمنت مشترک اوناست.
💔
🫡
🙌
@AloSport</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/125129" target="_blank">📅 22:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125128">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ef0b0142.mp4?token=mbxufohc_CmA0J6JpkbUAUgbIwKCws36U2wPvuwVCHEgaZmAZZUlGaX71WadRTMTH6h391k_PtVieaAgRTFqSveyl0wXBuVa9Dl9eSk8sQS0C92T3Q5JGbvR_cwXT_Mhr_sU0EWxRwcJmI4pBv-SdT0GHKYNpbe7i9J_fuldyHrruwdtz9izx9_sJjTzLaeLrMA6IdNM4R0TJyi1rkBdyY3OdEa7krtZW0IcSUhAn5n2c2ZN6em0mlJcIlCXuYX3L3MppWiQwKaQSo3XOZVaZXyrdBBK8bOUnCKuPCQuc_l2fkx_4duouQc6J4OkV0YQgT_P1vo4trXdO_FYBfc5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ef0b0142.mp4?token=mbxufohc_CmA0J6JpkbUAUgbIwKCws36U2wPvuwVCHEgaZmAZZUlGaX71WadRTMTH6h391k_PtVieaAgRTFqSveyl0wXBuVa9Dl9eSk8sQS0C92T3Q5JGbvR_cwXT_Mhr_sU0EWxRwcJmI4pBv-SdT0GHKYNpbe7i9J_fuldyHrruwdtz9izx9_sJjTzLaeLrMA6IdNM4R0TJyi1rkBdyY3OdEa7krtZW0IcSUhAn5n2c2ZN6em0mlJcIlCXuYX3L3MppWiQwKaQSo3XOZVaZXyrdBBK8bOUnCKuPCQuc_l2fkx_4duouQc6J4OkV0YQgT_P1vo4trXdO_FYBfc5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
جاویدنام علیرضا سلمانی 28ساله
🔴
شامگاه پنج‌شنبه 18 دی‌ماه حوالی ساعت 21، با شلیک مستقیم چهار گلوله توسط حرام زاده های جمهوری تروریستی اسلامی پرپر شد. چه نازنین جوانانی!
🤔
عرزشی حرام زاده، به وقتش مردم شما را پاکسازی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/alonews/125128" target="_blank">📅 22:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125127">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai8iHohtBVIQhPkSd459rXRaPvnWxWls03F5XVEjPT5NUgSDiHZSGAcYQd2uAbCM8f73x1GVHM_uJoXJnNXZNuYrKxWxsGmsMYr_p02FgkDpmgfDgUPYFzTVomdSNKdK5AnFEo0rvC_DeaH5gSt0mwgAg6QS14bWFGC8aNftnqVUdrmMhzDjipapRNCmpU27KIg4j6_71k-A08u1KrR7Z8pge8w8DpynyD4SuEa4E4o5wuu6vKCgg18DNjvV5O8lzwb6-BVf5gWB4LhwXiRlpUQq4DnUGI6NakwHjlPF5zkZJ2zJFF0iLHsm24W5XDmBxLZsnMH7WZ4TUDJDlae8Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال حاج محسن رضایی:
اگر آمریکا غلطی کنه آنچنان تو دهنش میزاریم تا درس عبرت بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/125127" target="_blank">📅 22:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125126">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVeOt0MlM042XTFwHjEJwT73gbfS6d-jnx0Hzg-YinzD8UUjsOr-fu80DOQMAEbbn-VcicOz8VkpyIog9vsQHMDVKhdZWV2AzN8srNoCQbq9ZsgPhtqwdbUGnmG5RTjBJAS36a5EQsdvkkiDFbfxn-IbZDjFpfIeXP29lthESg0lk4kIKj5EsdGBMBsbQR_joAO8uqGaPqxbcOtqoSK88z8cwWbJEYZB-V9l5Y72EaBy9I-yYzHA0qEaVupwn0f1YaHYqQ7jIEMvf36GKKSGLgCCl6xKqYld5IiHvlsf8--bwRweDaIPRRwnUrbfPbrZYas9yHf541YUj1r_ny6EmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
🔴
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
🔴
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/125126" target="_blank">📅 21:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پوتین درباره فلسطین: اکنون باتوجه به رویدادهای جاری در ایران و تنگه هرمز، ما فاجعه فلسطین را فراموش کرده‌ایم، اما این مسئله هنوز وجود دارد.
🔴
روسیه معتقد است که راه‌حل اساسی این موضوع، تأسیس کشور فلسطین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125125" target="_blank">📅 21:46 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
