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
<img src="https://cdn4.telesco.pe/file/P51VLA4qgQyjtRxaVuHC1fmxf2ysBx0m8tIDEcC9uGD0Q_-4blU9TISMfK7KT54DfBTshgea86UDJlh0RNEdZw8WAz0KS7ibSc7MJwiWhpjnm8mQQp7whHO5AGRvX7MlrV_UEi76NoxO7P-DGFF3PjGSu2i3-C-j5gWCyybGBkYZU2YBP_VpZzrvgDYSkwSbfkSK27OU03COijcI-9asCbFtF26Jp64N5uakODyptAwBzX52wHm5iVDfkaLdzWuu230H6IOeIdxh5CqlrLVETzjYcIhR4szb3WRSrQBlPDmssYL8GH_Bw3FfJP1L1EmxZ2ZLWwSOYtDGnOa5pgQSkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 963K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 10:56:22</div>
<hr>

<div class="tg-post" id="msg-148146">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: ترامپ در سخنرانی خود در سازمان ملل، به موضوع جلوگیری از دستیابی ایران به سلاح هسته‌ای می‌پردازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/148146" target="_blank">📅 10:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGESPDTBcuOjsdstBNh1gbg83_EvLLiUiubd1_CCJn0iprnwmUSuD5byMMofp_4JFAsHiz1yW9It3ZJnUdElH7RUJ2Syp7D_QzR6-tGXSMrHydXCZZzy79c3rCrWkQsPi9er1OYtHdmO-rA98UOibT9fzBWB2G5XUT8IxhmX7FfmgsX7_BGaRlqpKisQimYB8EqR2VQdZ9usJLcFoJozcphu5Q3zv1mMHhF-4QIrDRzBaILW2JtJr10zdj6rFAaqtgXVrNeA4BpcS1dfL5Sxn76W3TUWFfdI2xuhjITWWMf6d-qHkaDzMSVAlTrxOzyNdTnF_xZLPw5s5n_NY8NJCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e84c2629.mp4?token=DVd9zzWhyswJsHDprG98W0p7d-FtalenYOXEkL3PaTy9riZv-NPXnlIDDAvDecoiuFyIohzmYd-fqLDvDhPH7Dyt0IVsIKgWnU4f3msVTV7z4e1U1ffGM_SrQ8vc7m8ulOtJhW5QsJDe1wiMbwq23MwjgqKQsQreUmYvFtoYhLJ7HkMShi6UJLLNbsOJWrNvbh2S6zgzCzuoEE4L72VK_oSG65D3rP72BLmkutLKY0nPlIyXCWLmvIoyuaZM-5QDfKu4zJqRB4Eyqs3seCz5KX90R88AAGrLb3_YRzL6cNwlkWhPr9K_SLUU3_yM06bGjereP2EoDlIOkn5VWCroXnfzs1lrg7SL6XhQ-4a_isNQirTc7k14UdNVy2TZQvKSmagD7iXMUY_T_oLyhgz7nwTBlB8m0Bboug60DjmtzVaKo8SgOOh3AWOB-k_N_n05QQA24V194OkLftv_4w3_Q88ff8HjS5wfGs0Yn59g8SvdLZoI7T2q_tjrUU3IK0kRPSJVNql2EakOa5pbxT6nJ3qHF6F5oV9oLosQWaUC6lbCKjieQLHpP1uReJ3DndYTxRt4vFiH_vbZbxy3Y9SYIednxojc0yVhXoataqV-J44deuSr2tPzUhuMqE1HyB_B_FrNC81T-HmZZLc336YRST2a9HmAkAqPs6JFc6j1tEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e84c2629.mp4?token=DVd9zzWhyswJsHDprG98W0p7d-FtalenYOXEkL3PaTy9riZv-NPXnlIDDAvDecoiuFyIohzmYd-fqLDvDhPH7Dyt0IVsIKgWnU4f3msVTV7z4e1U1ffGM_SrQ8vc7m8ulOtJhW5QsJDe1wiMbwq23MwjgqKQsQreUmYvFtoYhLJ7HkMShi6UJLLNbsOJWrNvbh2S6zgzCzuoEE4L72VK_oSG65D3rP72BLmkutLKY0nPlIyXCWLmvIoyuaZM-5QDfKu4zJqRB4Eyqs3seCz5KX90R88AAGrLb3_YRzL6cNwlkWhPr9K_SLUU3_yM06bGjereP2EoDlIOkn5VWCroXnfzs1lrg7SL6XhQ-4a_isNQirTc7k14UdNVy2TZQvKSmagD7iXMUY_T_oLyhgz7nwTBlB8m0Bboug60DjmtzVaKo8SgOOh3AWOB-k_N_n05QQA24V194OkLftv_4w3_Q88ff8HjS5wfGs0Yn59g8SvdLZoI7T2q_tjrUU3IK0kRPSJVNql2EakOa5pbxT6nJ3qHF6F5oV9oLosQWaUC6lbCKjieQLHpP1uReJ3DndYTxRt4vFiH_vbZbxy3Y9SYIednxojc0yVhXoataqV-J44deuSr2tPzUhuMqE1HyB_B_FrNC81T-HmZZLc336YRST2a9HmAkAqPs6JFc6j1tEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از روز گذشته ظاهرا حملات نیروهای تحت‌الحمایه عربستان با پهپادهای سری نقم و عیبان (معادل شاهد-۱۳۶ ایرانی) به اهدافی در اطراف صنعا آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/148144" target="_blank">📅 10:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مولوی عبدالحمید: اگه حکومت حرف مردمو گوش میداد شرایط اینجوری نمیشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/148143" target="_blank">📅 10:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مقامات ارشد دولت ترامپ می‌گویند که رئیس‌جمهور در جریان نشست مجمع عمومی سازمان ملل در نیویورک، با بنیامین نتانیاهو، دیدار نخواهد کرد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/148142" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
عضو دفتر سیاسی جنبش انصارالله: ملت یمن با هرگونه آتش‌بس یا کاهش تنش، تا زمانی که عربستان محاصره یمن را رفع نکند، موافقت نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/148141" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
الجزیره: نهاد ناظر بانک‌های ترکیه، مجوز فعالیت شعبه «بانک ملت ایران» در استانبول را لغو کرد
🔴
بر اساس اطلاعیه‌ای که در روزنامه رسمی منتشر شد، نهاد تنظیم‌گر و ناظر بانک‌های ترکیه، مجوز فعالیت شعبه بانک ملت ایران در استانبول را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/148140" target="_blank">📅 09:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: توافق با دانمارک و گرینلند «تاریخی» است و بر اساس آن، منافع امنیتی ما در قطب شمال به طور دائمی و بدون هیچ هزینه‌ای تضمین می‌شود
🔴
مارکو روبیو، وزیر امور خارجه آمریکا در مورد توافق با دانمارک و گریلند گفت: این توافق تاریخی، یک پیروزی بزرگ برای ایالات متحده و مردم آمریکا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/148139" target="_blank">📅 09:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3cc6058d.mp4?token=PoVDuKLF3pcvR_qWK2eSMDcWkC0UMXkgY_ImVQeijutX0EYAXDhfezhPCIvW9vw10ONMk5S7HhhdjroY8hI7oBwApn9wgPKo8bk6ARmI6RtXQPvG7_nz1DDmu5IsGOJOAkkqtJ-426PXl0cuiVCy-dw-zORcVKxopFmoERvB6VSih42On6CEF0wfyOR_TzyS0WAQFDhFlvPl3-P7uD1gULisK6sOFf0hOCM0NH7tMSQuUz7lLajZ2QfNHprEPzh__2PDcajPoDJGho88EXhXdi9NhwXkqt7j3ZnrK6JBBkM5aTXuQWkVuBFsc9xX9IDPWr0qfy_4FDMUpWf2M6MkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3cc6058d.mp4?token=PoVDuKLF3pcvR_qWK2eSMDcWkC0UMXkgY_ImVQeijutX0EYAXDhfezhPCIvW9vw10ONMk5S7HhhdjroY8hI7oBwApn9wgPKo8bk6ARmI6RtXQPvG7_nz1DDmu5IsGOJOAkkqtJ-426PXl0cuiVCy-dw-zORcVKxopFmoERvB6VSih42On6CEF0wfyOR_TzyS0WAQFDhFlvPl3-P7uD1gULisK6sOFf0hOCM0NH7tMSQuUz7lLajZ2QfNHprEPzh__2PDcajPoDJGho88EXhXdi9NhwXkqt7j3ZnrK6JBBkM5aTXuQWkVuBFsc9xX9IDPWr0qfy_4FDMUpWf2M6MkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: هفته آینده در سازمان ملل سخنرانی می‌کنید. پیام شما چیست؟
🔴
ترامپ: خب، سال گذشته اپراتور تله‌پرامپتر من را از ورود به سالن منع کردند. بنابراین من بدون تله‌پرامپتر آنجا ایستاده بودم. جالب نیست؟
🔴
خبرنگار : پیام شما چیست؟
🔴
ترامپ: یادتان هست؟ آن‌ها پله‌برقی را خاموش کردند.
🔴
خوشبختانه بانوی اول من خیلی محکم بود و من توانستم پشت او یا بخش دیگری از بدنش را بگیرم. در واقع، دستم کمی پایین‌تر از پشت او قرار گرفت و محکم گرفتمش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148138" target="_blank">📅 09:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
هزینه یک دست لاستیک ایرانی تا بیش از ۳۵ میلیون تومان رسید
🔴
آوش در گزارشی نوشته قیمت شش سایز پرمصرف لاستیک ایرانی اکنون بین ۴.۵ میلیون تا ۸ میلیون و ۷۵۰ هزار تومان برای هر حلقه قرار دارد.
🔴
بر این اساس، خرید یک دست چهارحلقه‌ای لاستیک برای بسیاری از خودروهای داخلی بین ۱۸ میلیون تا بیش از ۳۵ میلیون تومان هزینه دارد.
🔴
رقمی که نشان می‌دهد تعویض لاستیک، برای بخش بزرگی از رانندگان دیگر یک هزینه عادی نگهداری خودرو نیست و می‌تواند فشار قابل‌توجهی به بودجه خانوار وارد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/148137" target="_blank">📅 09:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWlwYjQC_swj1GkypFmvWZIUQHZp2swz8IMcHN_koSfCkT5ZsWG7OR5iNaacjMNBuvPVNUV4nWLmI-FYZjREiieprdHXIXNA_-dxl7rHeoOxMd5pdPe6_MsC3-2Wby3DGJxDhBPtBLwfx-hFzeJpPGzuN-xcd6-ejegUXZR63LIvmIb7eg7yUZn_EnXYpWrvygM931ocW-3K_AUBP9UgAJcHizIft1XxPVhkjUCgIYbTjIVKrdCBptyQOwysddLu3eCpXS7_1WwwN_KdKkyh_ZAEihCU9oV0-YGNmuSbgGgW6QbzEj9jPrSEt4WKCJTmcqg1hrqhVyBWf93K9t22nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZv8pJG3uG6oak9kYpc_nsoy1ZUBkYMW8T8M3BKy9DR9yQfzPWHqL32PwjmWK1EcQTdWtxQvseblUrWllAwEk1s0mITTjJbdEwIOHhOqv8hc6YVf6z5_hmG1pzEKJyxYV0Yr-NAgmKIxYl09oCmUnLCzqoaPWb5E3h7z3dJqLmea1MaPgNEy-A3niK0MF9exJQ7NC6ddQPdEGe44q1sWD62B_qv57xW6i-6Ov9gz5sHFuwwIMTDKDW_SWbhfgoXkZsOhPGraZ7ScH0ensAP8TgjnZyY5kpaDHgJDBxSkCfNm2EM_mseLRrQd6j2oklU-TsLhdZtLlWXduAG6fjur2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا،
فهرست «
۲۵ دستاورد برتر ترامپ در دوره سوم
» را در شبکه اجتماعی
Truth Social
منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/148135" target="_blank">📅 09:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پروازهای هوایی در ریاض به دلیل موشک‌ها و پهپادهای حوثی ها متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/148134" target="_blank">📅 09:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bB8MTteiJ7v-sLhZbGf3INWB-pQ-MT2hjb0o-_gtF9PNjSOuc5mf4PPSAsD9BXPzEwsutFMr9Ow0XeaPAkYzX2Ivx_YOKPhDFk8vJHvSmIzr4-sLhJggdpCOQ5Fp_ItPLC-tUTDoKN27eDxH057ooB0_cndju6wySLl8n3YWhTCG9Knkj76dOYeQmNzJlnxEhiP9q_EhTihPdxnemrWzuJTd561lNLIgP0jbw56eKlN923M5TpySoNOmtddcof8YJ1vSeaPCx1LCcQi-1nG0bWta12grQenRuSoBNAkqHxR-jhLW5O6ZNaTu-Wncb4-8VI_k3qobJz9vhMs1aK-4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر من، هدف حمله موشک بالستیک انصارالله به ریاض، احتمالاً پایگاه هوایی ملک سلمان در جنوب ریاض بوده است
🔴
اگر هدف پایگاه هوایی شاهزاده سلطان بود، احتمالاً هشدارهای اولیه برای ریاض صادر نمی‌شد؛ زیرا این پایگاه در فاصله حدود ۸۰ کیلومتری ریاض قرار دارد. همچنین در حمله ایران به پایگاه هوایی شاهزاده سلطان در اوایل سال جاری، معمولاً هشدارهای اولیه در ریاض فعال نمی‌شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/148133" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
انتظار می‌رود شی جین پینگ، رئیس جمهور چین، هفته آینده در واشینگتن با دونالد ترامپ درباره آتش‌بس تجاری رو به پایان، معافیت میلیاردی تعرفه‌ها و هوش مصنوعی گفت‌وگو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/148132" target="_blank">📅 08:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
پنتاگون در تازه‌ترین برآورد خود اعتراف کرد جنگ با ایران تاکنون ۴۳.۶ میلیارد دلار برای آمریکا هزینه داشته است؛ رقمی که هنوز خسارت‌های واردشده به تأسیسات نظامی آمریکا در ۸ کشور غرب آسیا را شامل نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/148131" target="_blank">📅 08:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxhPn8N7Etvf8ddc6GjPYJ9Vr5zP3Cnz3oVH9V91qYdaa9onWNaVdZq6JPeC3eLOLEHABRB-4Y1QgcG9EQOs21QxMsuvP6je3o3Q69ShDVZHZE51acsFhtgNBYskItBsatI23gf4spCGU1MDSkZmoZaWvyDqFhA7U1NIIBjQGz0B208KC894OV1uSh7-SvnCv1xvwhqz2985U5go50skN-RY0eur9yuoTvWHY6YvZJ8Bp7rUB6lTc2T7iKEryDcWaSAH4y5m9FhGkuNUOTEaIAhxBMj1Euc12rLJCFyfctRE1JtLwUm5H69bLjcsPr1Sgpe1lRxdREWcvlkI2HfSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا: شرم بر واشنگتن پست. این اطلاعات جعلی و دروغ است. آنها از رسانه دولتی ایران بدتر هستند.
‏
🔴
واشنگتن پست: بر ادعای خود باقی میمانیم. ۶ کشته بیش از آنچه اعلام کردید وجود دارد. واشنگتن پست اعلام کرده که تعداد کشته شدگان نظامی آمریکا در جنگ علیه ایران بیشتر از اعلام پنتاگون است
‏
🔴
به گفته ۶ مقام آمریکایی آشنا با داده‌های حسابداری تلفات داخلی وزارت جنگ، شمار نظامیان آمریکایی که در جنگ علیه ایران در کشته شده‌اند، بیشتر از آن است که پنتاگون اعلام کرده است.
‏
🔴
این مقامات تعداد کشته شدگان را دستکم  ۲۲ تا ۲۳ نفر اعلام کردند، پنتاگون در حال حاضر ۱۸ کشته را فهرست کرده است..
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/148130" target="_blank">📅 08:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: با دانمارک و گرینلند به توافقی دست یافته‌ایم که به آمریکا کنترل دائمی بر امنیت و نیازهای دیگر در گرینلند را می‌دهد
🔴
این توافق کاملا به همه نگرانی‌های متعدد واشنگتن رسیدگی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/148129" target="_blank">📅 08:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148128">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZwCQtCNdziiyV9eJt9DlJea4mR-14b5RjoCqcmUS7eaQNAVjR5HsZ7s1RIYAwuscZyaccT7LVQwIjCVCosy5FYriR3qgfR7R6MqVOalkxIAvBUI2o6jrhTxZmlSE--7ZerR0ewowrvTlOVE1SsdocTmxIZFKQBOu7ev__e_kH1bhvpBS-55PyCrWVaF9zt-Q9YBcIBqfYiExYADanWKSH1vVqtiYI5Ye3Hodgy6uRpKbi4zRrWRIrbQwNQrLkIUz7MePBvrSuEi9l5_vqhpDziP2Gxg18I-JSR4J_4p9Tve2O14JFQpBCa70z-KNyFdsKbCdUIKLx7n8g26AoswoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه مجوز فعالیت شعبه بانک ملت در استانبول را لغو کرد!
🔴
نهاد ناظر بانکی ترکیه مجوز فعالیت شعبه استانبول بانک ملت، بانک کاملاً دولتی ایران، را لغو کرد
🔴
این نهاد دلیل تصمیم خود را «تهدید علیه ثبات نظام مالی» اعلام کرده است
🔴
شعبه بانک ملت از سال ۱۹۸۲ در ترکیه فعال بود، اما پس از تحریم‌های آمریکا عملاً از سوئیفت و سامانه انتقال بانکی EFT ترکیه کنار گذاشته شده بود.
🔴
لغو مجوز، پایان رسمی فعالیت این شعبه در ترکیه محسوب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/148128" target="_blank">📅 08:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148127">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) از کشته شدن ژنرال فرق العصار، فرمانده تیپ اول کماندویی، در نتیجه حمله هوایی عربستان سعودی در جبهه کهبوب در نزدیکی تنگه باب المندب خبر دادند.
🔴
گزارش‌ها حاکی از آن است که شش نفر از محافظان العصار نیز در این حمله کشته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/alonews/148127" target="_blank">📅 08:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148126">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFdztp5eOCsLlyOF5srjZslis8gT6e7uoB9cFmbacLEAVda7F_0n63rLNFCXhoxb1ImTOiHyHaQP65KMtreS2qEZpe_bSITs1Z5XFqMBDAWtmNQadTawbgKu8yl8s4-Cw1uBaf85q7_GCqV46yCxZxXSZ8beeN7iuj4ljB_FF5tdpZzbYGsN5fS_BhDtsQ76xiwIQfqvOJa3kCgtsPt2HzG0dj50Y5RcIkuRQOeuIzzEwZQf3J81RFEhXY_aWpzme0Ccx9_HvZ1PMxSGuHX2UoF0w0Itv_LxXLEf_a8viuspbXw_D1N5GNUtiNa6ZNhQdehMt2cqaY-HZHJ4_RATHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای نظامی آمریکا به ABC News گفته‌اند که بیشتر پایگاه‌های نظامی آمریکا در خاورمیانه به‌طور غیرقابل‌جبرانی آسیب دیده‌اند و ترمیم آن‌ها ممکن است دهه‌ها طول بکشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/148126" target="_blank">📅 01:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148125">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶ را امضا و آن را به قانون تبدیل کرد.
🔴
بر اساس این قانون، تحریم‌های قانونی، تعرفه‌ها و محدودیت‌های اعمال‌شده علیه روسیه گسترش می‌یابد و تحریم‌های موجود علیه ایران نیز…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/148125" target="_blank">📅 01:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148124">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtaMiAs4PzxievIzAtx7KhAcOcyVElggB0Cf1dDu_O7PAeG-Cf-gYGhx2OkCz0ytfHIBxtGd8d3qliZHdMjvESaHdcvx6e-iMS8Sy_1IXtulHLvbUg8DXGHo_yo0lkrk9Gp_oZZDEnMs5pqRe5cv7zne82atDNqGdycMnV4PsnQf3ljKDE77ZF9VZlG0_ZJvv5jRf3PG1m6kLkEoLUHWvrvhf8Bn2X_usfx-hZOHDvQ3jmRVK_AN5-QQczLYjYSCCPifUPbSKTdXFlLig_hqWd-jyNJoPCfgar82vBhNpTFUS-uNv8RIGkoGYTy89tZoiENQFP6JscDzpLabQ7FFLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا،
قانون «تحریم روسیه و ایران، لیندسی او. گراهام» در سال ۲۰۲۶
را امضا و آن را به قانون تبدیل کرد.
🔴
بر اساس این قانون،
تحریم‌های قانونی، تعرفه‌ها و محدودیت‌های اعمال‌شده علیه روسیه گسترش می‌یابد
و
تحریم‌های موجود علیه ایران نیز تمدید می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/148124" target="_blank">📅 01:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148123">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f1eeaeb95.mp4?token=QmhfcKdf_97E17OnolTd4xiUnnMMNE-BSM10uNPKRW2J6GhrmreLtPW8Z9r_BP769v2fjWX759VexqdRH3Un8OQ4aJzwNJlnNcBzrZ8fbDEIoQ2PWgwj0Rlm4LfDX5B8FkGQxqbNBZZ8InAvH82dsRjRe-SYaAcEgJD9EGIoXBUJGEtpaUThewKnaIR1wc1r336DwFuJIWwlr6y9-6bIg41-m6HE3J4TC_FBS_d3xQCvfPRVBd49GNjRCV4mtJbCSra4Qw8GxnlLjvQBlwKnz7m5LmjlGYp4HaIOxbVGU5Ol5TwM98yhkzSfYgS3DzOQlkbzvyi5uem2Ub35lswyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f1eeaeb95.mp4?token=QmhfcKdf_97E17OnolTd4xiUnnMMNE-BSM10uNPKRW2J6GhrmreLtPW8Z9r_BP769v2fjWX759VexqdRH3Un8OQ4aJzwNJlnNcBzrZ8fbDEIoQ2PWgwj0Rlm4LfDX5B8FkGQxqbNBZZ8InAvH82dsRjRe-SYaAcEgJD9EGIoXBUJGEtpaUThewKnaIR1wc1r336DwFuJIWwlr6y9-6bIg41-m6HE3J4TC_FBS_d3xQCvfPRVBd49GNjRCV4mtJbCSra4Qw8GxnlLjvQBlwKnz7m5LmjlGYp4HaIOxbVGU5Ol5TwM98yhkzSfYgS3DzOQlkbzvyi5uem2Ub35lswyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست:
«تنها رسانه‌ای که بهتر از ایران پروپاگاندای جعلی تولید می‌کند، رسانه‌های دچار جنون ترامپ در کشور خودمان هستند.
🔴
جدی می‌گویم. واقعاً تأسف‌بار است.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/148123" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148122">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پیت هگست : خسارات و تخریب‌هایی که ارتش ما به جمهوری اسلامی وارد کرده، بی‌سابقه بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/148122" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148121">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ میگوید سازمان ملل متحد عمداً دستگاه پله برقی و دستگاه نمایش متن مورد استفاده او را در سخنرانی‌اش در مجمع عمومی سازمان ملل سال گذشته، از کار انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/148121" target="_blank">📅 00:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148120">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYtaKYMdTicT0_kU4mF9oqWdEyznZwRZRR8MbX7wvh3SoN3NCXRJisQ2ZOrfQ4n3TxE0kKHBwBAdyCRKEicCS75H7L-dik2oK3Wsn9gUxmSBE3_SsxbeZv5g-HQXXKQcHQLotqTzRgWrR0mj5P2Uza24fqhRryke5Bk4QNsTT72ObA4B1P643mkqmID4e29hlzMTNP6xVG7Dq3PfPADJBGBtFSqzlsfZ-gRTcO71rLQlXQUfMc4czqME1us0bZZyrMVlWBaXF9-hVprjcSoZfHOfn2RF_M0r94UuOEUt5GQiB9i2dCdpAALJ283HGxJ81di6bt0NT1TPEp9p1Gj5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: ریشه تمام مشکلات بی حجابیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/148120" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148119">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ : روزنامه نیویورک تایمز بسیار دروغگو است.
🔴
واشنگتن پست بسیار زننده است. من می‌گویم، آن‌ها زننده هستند.
🔴
من نمی‌فهمم. چرا باید این‌گونه باشند؟ ما بسیار خوب پیش می‌رویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/148119" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148118">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
هشدار های در غرب عربستان سعودی دوباره فعال شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/148118" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148117">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری /  هشدارها در جیزان، جنوب غربی عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/148117" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148116">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ : شبکه فاکس بدترین نظرسنجی‌ها را در کل این صنعت دارد. به نظر من، آن‌ها سال‌ها پیش باید کارشناسان نظرسنجی خود را اخراج می‌کردند.
🔴
آن‌ها به مدت ۱۰ سال، پیش‌بینی‌های نادرستی درباره من داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/148116" target="_blank">📅 23:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148115">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
🔴
ترامپ: ممنونم که این را به من یادآوری کردید.
🔴
خبرنگار: آیا شما در تلاش هستید تا با اعمال فشار، رسانه‌ها را از انجام وظیفه‌شان باز دارید؟
🔴
ترامپ: نه، نه، نه. من از رسانه‌هایی که دروغ می‌گویند،…</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/148115" target="_blank">📅 23:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148114">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
🔴
ترامپ: ممنونم که این را به من یادآوری کردید.
🔴
خبرنگار: آیا شما در تلاش هستید تا با اعمال فشار، رسانه‌ها را از انجام وظیفه‌شان باز دارید؟
🔴
ترامپ: نه، نه، نه. من از رسانه‌هایی که دروغ می‌گویند، مثل شما، خوشم نمی‌آید. من فکر می‌کنم شماها خیلی بد هستید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/148114" target="_blank">📅 23:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148113">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63f668795.mp4?token=j_9h--7-mHDwFW4a2XiOw-_V0_LP2R_zoxr-R8djaFCPw1vPAd5rjPXyY7wdKVbTQFQ-AHIUX0Dc3V4YZEQiZdfeQLA3URUoI_C6AtlaGjlVVHlM3pQoI8n-KtVg8rimUA3B3uyEcf1mwjiD5fJa5dpPUsiyDt3JUgONmSaeikUzBSTguAeXMSC5_C5jEsENl0xz8p5xN5U_THKZ25LWNZwp2yMbMG63HmrxgUlO6Zs2SbGzVJ7_C5CQW7uHY7gfXmLsWGvtKmYsoko9E-M6Zl8Jo68VZfWoM4m0sPdS7nvoWWTb4bGge7h6fkKc7tFxlOZzOfFUq3qA_VfULYX1IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63f668795.mp4?token=j_9h--7-mHDwFW4a2XiOw-_V0_LP2R_zoxr-R8djaFCPw1vPAd5rjPXyY7wdKVbTQFQ-AHIUX0Dc3V4YZEQiZdfeQLA3URUoI_C6AtlaGjlVVHlM3pQoI8n-KtVg8rimUA3B3uyEcf1mwjiD5fJa5dpPUsiyDt3JUgONmSaeikUzBSTguAeXMSC5_C5jEsENl0xz8p5xN5U_THKZ25LWNZwp2yMbMG63HmrxgUlO6Zs2SbGzVJ7_C5CQW7uHY7gfXmLsWGvtKmYsoko9E-M6Zl8Jo68VZfWoM4m0sPdS7nvoWWTb4bGge7h6fkKc7tFxlOZzOfFUq3qA_VfULYX1IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره اروپا: روسیه از قبل به متحدان اوکراین حمله کرده است. این کشور حدود پنج سال است که به متحدان اوکراین حمله می‌کند.
🔴
به نظر من، همه با این موضوع موافق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148113" target="_blank">📅 23:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148112">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2567a538.mp4?token=O0nw2TmDWbmKi1VrkoXy8P0NmaZwdSyuJjxg-t4eIDbOGJc9fAGUrXcWhg9u5vS1HAqloI6NFkWzP4TofX8Nw58BOFd7rf0-vnbymtMGR1Xo9hAWzV7oKwhACTDPND9jOz3vpsdgWLte1tDV_jqnGKFMF4RHjHKLCYdEWZOfmdgLddtS0Y46h6tfGQNlw-MANYZjGHONoQagb3kxeXKvgQSnn-LOF1LqmXQkdsZZboC-gTn_PnW0GAUvMAHPshgtpRGjQ9IkPo1B2prQcLUqmzsmeuU_JQ9SUxUAtHuiukUdIG6TA9Nfc2jaTt9O32zW-61m32MBpiePKxRwdrmeTY4rmyHa7nm5bs4FzqmHdpsyv8LaCBJHAsAePl5hVwDNcZfq8fnZ8Dl9HOeXdEBCyZdke822EGm5XdA5DcjCrdIiRXjxXxCKhN-e8XWsBnNzqW7-XWc1HuwdIw_dQ3ekYgxR3Lf-NroD41nIDTVNMoiEpb9QKL8wIytyNkUsUwII02pqSk3cwrUgOcCmtPkI3xy6SCCtPAWg2Z-FlNhkYJVmZkN5cXYiHQGWWtPf4sckVLep371rrhiOojRNyoTQ3Xaw83DoJdPpgRh7Jw_galRd2Tv2G2vKcIHdveztNaEQn9yYkZSi7TEXD1MuWct3wXgAttu5ABM6KP6a7YZG6Po" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2567a538.mp4?token=O0nw2TmDWbmKi1VrkoXy8P0NmaZwdSyuJjxg-t4eIDbOGJc9fAGUrXcWhg9u5vS1HAqloI6NFkWzP4TofX8Nw58BOFd7rf0-vnbymtMGR1Xo9hAWzV7oKwhACTDPND9jOz3vpsdgWLte1tDV_jqnGKFMF4RHjHKLCYdEWZOfmdgLddtS0Y46h6tfGQNlw-MANYZjGHONoQagb3kxeXKvgQSnn-LOF1LqmXQkdsZZboC-gTn_PnW0GAUvMAHPshgtpRGjQ9IkPo1B2prQcLUqmzsmeuU_JQ9SUxUAtHuiukUdIG6TA9Nfc2jaTt9O32zW-61m32MBpiePKxRwdrmeTY4rmyHa7nm5bs4FzqmHdpsyv8LaCBJHAsAePl5hVwDNcZfq8fnZ8Dl9HOeXdEBCyZdke822EGm5XdA5DcjCrdIiRXjxXxCKhN-e8XWsBnNzqW7-XWc1HuwdIw_dQ3ekYgxR3Lf-NroD41nIDTVNMoiEpb9QKL8wIytyNkUsUwII02pqSk3cwrUgOcCmtPkI3xy6SCCtPAWg2Z-FlNhkYJVmZkN5cXYiHQGWWtPf4sckVLep371rrhiOojRNyoTQ3Xaw83DoJdPpgRh7Jw_galRd2Tv2G2vKcIHdveztNaEQn9yYkZSi7TEXD1MuWct3wXgAttu5ABM6KP6a7YZG6Po" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در دنیایی که بر پایه منطق استوار است، غیرممکن است که فردی که یهودی است یا فردی که سیاهپوست است، برای یک دموکرات رای دهد.
🔴
اظهارت شگفت‌انگیزی که آن‌ها درباره گروه‌های مختلف مردم کرده‌اند، باورنکردنی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/148112" target="_blank">📅 23:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148111">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9633a2e0.mp4?token=hz4t4kPP06ZS6WlgBKojII-JxA5pHHm_1wtGkzDcp-57cYb8gv2P7pxsNmCXRf-CpKLcCCdC_89Au9hCnIlnqXt_HGhH5p09rgllr4q2wk74yNKLQuSDQHtw9dcYTsPQ1TxRXoBxjx_sk7ih-te4LmiP70Cx2xTV61gpW7gIunnTB65-CGPfDwj6q2fJEbbD2sqE3wpG6Cz97zdoITgek-hKkVcCo8a783QXfo00l94Y6K0l3mxpvLDGiNBRyQITdIQX5ZmSjUseWJWKpLp934nP-CMSScSw3cYvBZ1P8bkKWsySoeLT1zUN6dGBWMey02_1pR7l8ZMseSRo_wu7VaeE6z72QQtW86puykEVJrnpm4Pvcwwek4j9hlk9sku0Al3XT6v5Ajd47mUeWqYs_os60fCdRG5QWnuH7REoHcL59zYsjy-qQ-JnMq-0FDFbwexcWR8uDXwQ253HSR48CYNL_utG-vnQwQ-W5lgFz52PTOWLS8pb1VOt07KwjW65_Q1nsyiO52Nz_CGZYIF-h6jkcbj4guWyxMIiis-FxYsppVSkQggCwdju7mP4I9DpfSSqarpzriEMQD81qR_j2WQOH1-WSiP8ibOfClMZ-CSQbRoFK1WsyQ_RWdLaU62Z6utSpEUxmlI8FzJNjULLxqqjGrTgV-T3ZkYzwal0pDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9633a2e0.mp4?token=hz4t4kPP06ZS6WlgBKojII-JxA5pHHm_1wtGkzDcp-57cYb8gv2P7pxsNmCXRf-CpKLcCCdC_89Au9hCnIlnqXt_HGhH5p09rgllr4q2wk74yNKLQuSDQHtw9dcYTsPQ1TxRXoBxjx_sk7ih-te4LmiP70Cx2xTV61gpW7gIunnTB65-CGPfDwj6q2fJEbbD2sqE3wpG6Cz97zdoITgek-hKkVcCo8a783QXfo00l94Y6K0l3mxpvLDGiNBRyQITdIQX5ZmSjUseWJWKpLp934nP-CMSScSw3cYvBZ1P8bkKWsySoeLT1zUN6dGBWMey02_1pR7l8ZMseSRo_wu7VaeE6z72QQtW86puykEVJrnpm4Pvcwwek4j9hlk9sku0Al3XT6v5Ajd47mUeWqYs_os60fCdRG5QWnuH7REoHcL59zYsjy-qQ-JnMq-0FDFbwexcWR8uDXwQ253HSR48CYNL_utG-vnQwQ-W5lgFz52PTOWLS8pb1VOt07KwjW65_Q1nsyiO52Nz_CGZYIF-h6jkcbj4guWyxMIiis-FxYsppVSkQggCwdju7mP4I9DpfSSqarpzriEMQD81qR_j2WQOH1-WSiP8ibOfClMZ-CSQbRoFK1WsyQ_RWdLaU62Z6utSpEUxmlI8FzJNjULLxqqjGrTgV-T3ZkYzwal0pDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حسن پیکر: به نظر من، او یک ضرر بزرگ برای حزب دموکرات است.
🔴
او یک کمونیست است - و در این مورد هیچ شکی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/148111" target="_blank">📅 23:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148110">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری / شنیده شدن چندین انفجار در عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/148110" target="_blank">📅 23:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148109">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c79171cb8.mp4?token=jPjfo87ME4BXSprpqKg8s5tdyfezt9p5mbIy2pKULh5aTWsvwWePAdLJsZ92QkfHRCE8FZ-sED2hiDRG1zhiR6VuzB1sQTIkl_YcEaHWiWLYinOQzgFzRDnuJ3lryjnVFWf8ZWpQSYlzwwVtc2Xt-qPpUmIh5EX-KNksqX0EcKmoKH0dthDLMA-I0kPL0LqebXZHZL1Xr806ydfhVeGJ_O63EpJ3Fkt0511-fBHdgLju_p0iU3A54LB6KpS4WUZwHYi85NLizcALbO4q1gaPqO81EszirYjtyCyk1R8xkr4TaOw57l2N6k2EHcskRnX1VGFewGFtMCUY9pVyuOhcwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c79171cb8.mp4?token=jPjfo87ME4BXSprpqKg8s5tdyfezt9p5mbIy2pKULh5aTWsvwWePAdLJsZ92QkfHRCE8FZ-sED2hiDRG1zhiR6VuzB1sQTIkl_YcEaHWiWLYinOQzgFzRDnuJ3lryjnVFWf8ZWpQSYlzwwVtc2Xt-qPpUmIh5EX-KNksqX0EcKmoKH0dthDLMA-I0kPL0LqebXZHZL1Xr806ydfhVeGJ_O63EpJ3Fkt0511-fBHdgLju_p0iU3A54LB6KpS4WUZwHYi85NLizcALbO4q1gaPqO81EszirYjtyCyk1R8xkr4TaOw57l2N6k2EHcskRnX1VGFewGFtMCUY9pVyuOhcwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به نظر من، اگر مردم می‌توانستند در مورد کاهش قیمت بنزین یا اجازه دادن به ایران برای داشتن سلاح هسته‌ای رأی دهند، نتیجه به شدت به نفع گزینه اول خواهد بود.
🔴
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/148109" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097ecbb4d7.mp4?token=SS0fMI-4X0fNMBC2b1S2Mtuhh2IgQjcsC1qfN45NPcszJuC-5S9vrmNiJ126AY9f2UK0jJYkmA4XWCbioorJzkX5k61TtGL9j11Mk_iSgwkT49tk8ypVDpxanrhS5yqEktbGHBxF6arlLctLjKN9XGybzknE-LmjbG29Cacu4Xjn9GWgrCf48F6JVg2lTYwOhPbS5AFFyW157bfkIGI8t3Eqfz5AD0zQsKrOxOvs-pwsBqCP2wv7XKNdh4c5vpt7e0k7xmUyv7I9o2oFDgP0Mlhl-k-lWETfCuSYtBzC_dIUp0jm-_RcDcZR3bjUIyi1fbYx9w1w9wTpm7PAWVvEBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097ecbb4d7.mp4?token=SS0fMI-4X0fNMBC2b1S2Mtuhh2IgQjcsC1qfN45NPcszJuC-5S9vrmNiJ126AY9f2UK0jJYkmA4XWCbioorJzkX5k61TtGL9j11Mk_iSgwkT49tk8ypVDpxanrhS5yqEktbGHBxF6arlLctLjKN9XGybzknE-LmjbG29Cacu4Xjn9GWgrCf48F6JVg2lTYwOhPbS5AFFyW157bfkIGI8t3Eqfz5AD0zQsKrOxOvs-pwsBqCP2wv7XKNdh4c5vpt7e0k7xmUyv7I9o2oFDgP0Mlhl-k-lWETfCuSYtBzC_dIUp0jm-_RcDcZR3bjUIyi1fbYx9w1w9wTpm7PAWVvEBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: جنگ به زودی به پایان خواهد رسید و وقتی این اتفاق بیفتد، قیمت بنزین شما به سطحی که قبل از آن داشت، کاهش خواهد یافت، شاید حتی کمتر از آن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/148108" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: جنگ با ایران به‌زودی پایان می‌یابد؛ قیمت بنزین کاهش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/148107" target="_blank">📅 23:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148106">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_6AfcMTaZRoGk6ja2m6cJAl1HTwIebYJpRILVOcwL2rA4Bj_yvMpLTvEfJudDZk7RPo2OuRcz3micEz74O0AM2Ug6z3EMIRBEIsWGddEif1Uy2mX8NGDGjbmPL0FyeyDdtAvnbBnN9AjTek7pSkpPhYevunMvNWPmCItJUApfARqaXyD5YHqr_iZLvalR2LEE669WCnB4-FW0w3PfxHmbt7ttgNMxqm2R3hhevnfsqmCyfLcSKQ6zeeeMI3gpCTTU4x3lrsnMKuDrM3w4nQB_ulQtcCHi5GGkyMZnXcdWMro1J2kOh1wV63vPd8Sy6amt9ySjVhNgUKLCvk3qeslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه برق کشور کوبا تحت تاثیر تحریم و محاصره آمریکا دچار فروپاشی کامل و سراسری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148106" target="_blank">📅 23:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIZWfLh3e3umFySjg0Hf9TnMWfDkSVD08RZ4adzzGxVsytZPDvDEnXZe_H3uY0IL0OXgojbSru1cqILtKr8O1mqHEQ16T3PUHHPs1H962egL8YO3xloZxj8lRDSWCyJKbupHerN1DABTI5L8SGSx7yee_yrJC_71aBtWu6tefaj7BEVAdTS6XHhn4G_OI8mj7PevAe0jMR26vOgzkzKQiLvkEqnsGXA2PiFmTwrb6OFS16mJO4zVWIuIMW_sIPEKx_ymIrwLbisjXHsupWEkqvpZQ_4RmNxifwemWhnsioNSlM8kk4877u8oVFqe-LoAte1fxalE0oF6dx4EMYUGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ایالات متحده به متحدان خود درباره تأخیر در تحویل موشک‌های رهگیر هشدار داده است؛ تأخیرهایی که ممکن است تا پنج سال طول بکشد، زیرا واشنگتن پس از مصرف گسترده تسلیحات در جنگ ایران، در حال بازسازی ذخایر تسلیحاتی خود است.
🔴
آلمان و کشورهای اروپای شرقی با تأخیر در دریافت تسلیحات مواجه هستند و درخواست‌های اوکراین برای دریافت سامانه‌های پاتریوت نیز تحت تأثیر تلاش آمریکا برای بازسازی ذخایر داخلی خود قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/148105" target="_blank">📅 23:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB8sCCRpC--6h1AwNYcl0IAWswAvP2gRYHxfyhA0vIMdNJbfZtjpm_38lg-Jhi4v0RM3ccXU8WaR07Bj8q7QtbiE-TNHRNARMSiz9-wiTablCek5-KMPv0SOEUJi0sPhGpqt-Agg8EvSwfgkXpl8CsdO1zXEdE7CXooSzRvIYx_3K4Dh99RQO53NXIEWSRi167aW9vl2FSAJWd5hApKkY2c6Tgb6q79YaXO9-pnjMdy_LfTqaeFlgU6i6xN9nhb6Y2nYaJ0Eu72oKODZXr3Sb5Mxc_aNqFCkPHC2Pm7sa62Znu_DiZMKqbyvKH3MVq8FdryILRtBypve_7yb0An11w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمایت خبرگزاری فارس از پورن استار حامی حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/148104" target="_blank">📅 23:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
️نشریهٔ پولیتیکو: این تابستان، قطعات حساس هواپیمای جنگندهٔ F-35 به‌طور غیرمنتظره‌ای به هنگ‌کنگ منتقل شدند؛ درحالی‌که قرار بود از استرالیا به ایالات متحده برای تعمیرات ارسال شوند.
‏
🔴
این موضوع باعث ایجاد تحقیقاتی در کنگره شد؛ زیرا نگرانی‌هایی وجود داشت که ممکن است فناوری‌های طبقه‌بندی‌شده در اختیار چین قرار گرفته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/148103" target="_blank">📅 23:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148102">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040b6f8928.mp4?token=U5l_K2Kg9Z39RqAk-6G8kAVzwRod6iyiCPvpP7LmHKqV4K_rk9l_61upfThAXtAEEuAMYbLycXxEQDnXpkxpoOrQMzx0xhci_ly1MtBwIUoZIDXDylHbgwR12Cl5iKAOmE-QiB9RJQ0wkUhlhQA9Vqs71ByMx0bjQQsouNb7pLNUjJEEGBNlyMjEAobIop03nzoMT6xHm601hPS1k_fJ0pEl-goOrpKKK5CMl1gI589VPOi8tSYPGM8rrPHregtzq-L2MT4h4a4EM4lxuNax0G-d-TYaEKIzwPN2KVvg_ThT7_gl3yTY06EenlYUn6tSGtbrikqSuNIxeowP2AZKyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040b6f8928.mp4?token=U5l_K2Kg9Z39RqAk-6G8kAVzwRod6iyiCPvpP7LmHKqV4K_rk9l_61upfThAXtAEEuAMYbLycXxEQDnXpkxpoOrQMzx0xhci_ly1MtBwIUoZIDXDylHbgwR12Cl5iKAOmE-QiB9RJQ0wkUhlhQA9Vqs71ByMx0bjQQsouNb7pLNUjJEEGBNlyMjEAobIop03nzoMT6xHm601hPS1k_fJ0pEl-goOrpKKK5CMl1gI589VPOi8tSYPGM8rrPHregtzq-L2MT4h4a4EM4lxuNax0G-d-TYaEKIzwPN2KVvg_ThT7_gl3yTY06EenlYUn6tSGtbrikqSuNIxeowP2AZKyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در جنگ با ایران، به طور قابل توجهی پیروز می‌شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/148102" target="_blank">📅 23:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148101">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
رویترز: داده‌ها نشان می‌دهند که حجم حمل‌ونقل از طریق تنگه هرمز همچنان کمتر از میانگین ۱۰ روز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148101" target="_blank">📅 23:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148100">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deace85529.mp4?token=atlBjgA8D2Sv4jgBJnPNCUgdoGvheVVCCSvi2nCAJD9mha4gh-Uxa9FgpRjXjn3P1OR_TxgZ-3n5hugcJ52KRbY7EXhmQJOc3_vj-4Lc5zSD0tq8E9sDRtsYeAY7X2s2ANEVRc5oEXLJwSnqGrYYarerVHV5sCePblp5jd5xq29Kb53_uqmgidQGGoKHv34lJ7lECAv90x36lBQmIGhF7yClGXvA8TLu5BqU_aJPTaOjOkvFDNUPF2uaP0E4QW1HkI9ONmgCufjz_NPHhDMgU8FKmAznbyLC6RNYknMH-P4MhZG87tkounnnOOjhgubuV8vAlT2lJWb60TgGPNP9nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deace85529.mp4?token=atlBjgA8D2Sv4jgBJnPNCUgdoGvheVVCCSvi2nCAJD9mha4gh-Uxa9FgpRjXjn3P1OR_TxgZ-3n5hugcJ52KRbY7EXhmQJOc3_vj-4Lc5zSD0tq8E9sDRtsYeAY7X2s2ANEVRc5oEXLJwSnqGrYYarerVHV5sCePblp5jd5xq29Kb53_uqmgidQGGoKHv34lJ7lECAv90x36lBQmIGhF7yClGXvA8TLu5BqU_aJPTaOjOkvFDNUPF2uaP0E4QW1HkI9ONmgCufjz_NPHhDMgU8FKmAznbyLC6RNYknMH-P4MhZG87tkounnnOOjhgubuV8vAlT2lJWb60TgGPNP9nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دعای عجیب روحانی عربستانی: خدایا به حساب دو شاخ شیطان برس، اسرائیل و ایران!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/148100" target="_blank">📅 23:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148099">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رویترز: ایالات متحده و ایران همچنان در مورد مسائل اصلی اختلاف نظر دارند، اما هر دو طرف گزارش‌هایی مبنی بر پیشرفت‌هایی را منتشر کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148099" target="_blank">📅 22:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148098">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlKic8XFgqg_QEZex0ACIDKojoatL1of-g3QATGDKZtr3NH_iOzDPvUmJvwYn7sSZB8wCBpvyWTGmNfHooC8Oj4OgT4sWSgi8W0bWLG3RsWdq4KCr1sSVlmsokvaQDHVc4eyTTsQw_NwkRDQDe5lRobG8lNubCyudI-M8Sy0ebM6_2hUXV90Evj3blm2z8Ibia5YawQfO85iHC0Nj3PfPFfmV4wmLwatX2zVik2BGaBtfZYmMS_o3c8vdht7v5CNutBnYkuMW9juX11xDFAFcCtdGSIkFsLiZcqAhjjw1hLZMzMj-Pn1K8BTMb3CMA4TuIaecIy3A6ApH-rvop-_zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ اعلام کرد که کانال‌های CNN، MSNBC و نشریه Politico از این لحظه به بعد از ورود به کاخ سفید منع می‌شوند. او این رسانه‌ها را به انتشار مکرر "اخبار دروغ" متهم کرد.
🔴
او گفت که سازمان‌های رسانه‌ای نباید بتوانند به طور مکرر آنچه را که او "خرافات و دروغ" درباره دولت خود یا ایالات متحده می‌داند، منتشر کنند، و هشدار داد که "سایر رسانه‌های خبری منتشرکننده اخبار دروغ" نیز ممکن است با اقدامات مشابهی روبرو شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/148098" target="_blank">📅 22:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/148097" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148096">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfgaE7mahcRXp7EUZvLy4fB248d6Ncpf_XaYXO_j1mwHzHtHgpAx2N-KlCY_lY3ZI5tIYqSQJr1nbXY7IDk6SEhHc6uq8aP0lwNDz0jmW5BhQL_U-lSl7j1j55d9PvRmWpV1x5E92uOW_ZnEweW2IEELmUeK414_UDnag3PPVvtP-r6qjGNJi7o75kB4pEzvPzMLezroc72u0umhec-u4ppiasapl71Hi1z9FpBtXoUsMQ9A8gberlW9sXxEy8YGr0fITGoh-mxbV41SIQiyJNhFJ3Ezos2Pq-e7i1lOPuPQAYeUXAIZ3TyFpsHFpTfD9EWF_G2OVMVqK5wcZYl6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حدود ۳۰ دقیقه پیش، دست‌کم چهار موشک کروز ضدکشتی از منطقه سیریک در جنوب ایران شلیک شد.
‏
🔴
صدای چندین انفجار از سمت تنگه هرمز شنیده شد؛ جایی که پیش‌تر در همین روز، دو نفتکش هدف قرار گرفته بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/148096" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148095">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پوتین: روسیه هیچ برنامه تهاجمی علیه اروپا ندارد و آماده همکاری و احیای روابط با همسایگان اروپایی خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/148095" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148094">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOi5DfuYlEvjsxkoqU4URnUg5BTQXpK3RiAbqtole0JuAEYwfpOAUfFK5ELB6vPLo6TN9CNcCViM273d6F0TlWyTM0zPnNzrgWuQNDbggNGPvxplHRpZ570KPN6-wpsCpdyIeKieI-fYWIILutgC3D5b-t2A-ea79_xLuO5wHmnFpieystKw3XRW5LglPYwD-HvPs-CZTTho96zX7E67ng0HrvAMUZNOo2UXT7TgZJQhSWYVAsck67mevCyYxAInnPJQ0_r05yDSKM35t8oRvkqW3qPgM6oq3zTKZotS3xy16XSdj7fVPmnMBena4sywYwuhJU_9XTipmnisLpbzIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: تعداد پرسنل نظامی آمریکایی که در جریان درگیری جاری با ایران در خاورمیانه کشته شده‌اند، بیشتر از آن چیزی است که وزارت دفاع اذعان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/148094" target="_blank">📅 22:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148093">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کارشناس صداوسیما: الحمدالله وضع مردم ما از مردم آمریکا خیلی بهتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/148093" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148092">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نخست وزیر لهستان: روسیه ممکن است به زودی به لهستان حمله موشکی و پهپادی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/148092" target="_blank">📅 22:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148091">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a967d061c9.mp4?token=B8KtDIRoY1Qr93hEWZzG9JXTS24qzUi_NrY5YaqW9Z9t-FyreDtyQYe0IriDnjZhPtUZkdFXDBqB5Du9rL_IQhelkWg0gMhAsN34pwE0EQfnuV1fxrqvCiCbtNhzWIPZtttPq5UqYJyM4bdEiO06Na4TGqM5HJJIlAr1Nj5tSk2nFf21f3nT740PZuYnYIvBD6rvY2mzdct-0KQpRod670h_bDYPYufCBiEA5LG0VR4KqhaEtzSq5ObK9QdaaMWeOMhpZLUoC_X4iFT3AAGlHvppyxdSLaOX6b8bwtqmDWJWCtSK3b4GQMXkmZ4i8VxhQZQ0q6jVwfK5C8jXTNMIlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a967d061c9.mp4?token=B8KtDIRoY1Qr93hEWZzG9JXTS24qzUi_NrY5YaqW9Z9t-FyreDtyQYe0IriDnjZhPtUZkdFXDBqB5Du9rL_IQhelkWg0gMhAsN34pwE0EQfnuV1fxrqvCiCbtNhzWIPZtttPq5UqYJyM4bdEiO06Na4TGqM5HJJIlAr1Nj5tSk2nFf21f3nT740PZuYnYIvBD6rvY2mzdct-0KQpRod670h_bDYPYufCBiEA5LG0VR4KqhaEtzSq5ObK9QdaaMWeOMhpZLUoC_X4iFT3AAGlHvppyxdSLaOX6b8bwtqmDWJWCtSK3b4GQMXkmZ4i8VxhQZQ0q6jVwfK5C8jXTNMIlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستاد اطلاع‌رسانی نیروهای مسلح یمن جمعه 27 شهریور، صحنه‌هایی ویدیویی از حملات پهپادی انجام شده به تجمعات شبه‌نظامیان حوثی در جبهه شمال استان مأرب منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/148091" target="_blank">📅 22:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148090">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که جنگنده‌های اف-۱۵ عربستان سعودی از پایگاه هوایی خمیس مشیت، در ۲۴ ساعت گذشته، ۲۶ حمله هوایی به استان تعز انجام داده‌اند.
🔴
آنها همچنین مدعی شدند که نیروهای سعودی در طول هفته گذشته، ۳۰۰ حمله هوایی انجام داده‌اند که در آن از جنگنده‌های اف-۱۵ و تایفون مستقر در پایگاه‌های خمیس مشیت و طائف استفاده شده و اهداف این حملات، استان‌های تعز، حجه، مأرب، الجوف، البیضا، عمران، الحدیده و صعدا بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/148090" target="_blank">📅 21:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148089">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFSC5ZTjVBhGatL_Is6KNGrekPViRix00IKbatwyp1x6K0cZgA5X-N733Zwryro7k0INrSf208tIKv2Hj1v4oeDhhzS9eJgBKW7_QCzBDL0cp-71O5I5DqLhpFWGmvZLF3rrAARXW4vVDNIILBTGoMrc9G3a5P5AHwrrpw8xbpI3n7UqvZXq56tofZW523rS-5S4rDKhBEh9egP8TN6O0EDo-S2S_kfzsPNPIX2z8HgQ8Y0PtKa0wBrs389XobhxAnOWMMA0SwN5L2VuZjXrYmATQFC0kVDHoftVrtd8xCkCtunspldUzcZhrN_TJ3p0fai9mrMmhHdTu7DBnZa7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
روند محبوبیت ترامپ در حزب جمهوری‌خواه اکنون به ۹۵٪ رسیده است، که یک رکورد محسوب می‌شود.
🔴
رتبه‌ی دوم، رونالد ریگان با نرخ محبوبیت ۸۶٪ است. از شما سپاسگزارم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/148089" target="_blank">📅 21:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148088">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
احمد الشرع،رئيس جمهور سوریه درخواست عربستان سعودی برای اعزام جنگجویان سوری به یمن برای جنگ علیه انصارالله را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/148088" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148087">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148087" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148086">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی وزارت خزانه‌داری آمریکا در گفت‌وگو با الجزیره: ما اقدامات سختگیرانه‌ای را علیه بانک‌هایی در امارات و ترکیه که از ماهان‌ایر ایران حمایت می‌کنند، آغاز کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148086" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148084">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REFZobirEb3zJn7V4mv5t0v4KC75fm1eUyZEeOpEpjq0fyHRrCdT4A_5ojqhJQcYgs2AmYXB2BfACwmgzvCSnbBPczQFjKosDrjxTW1yhAlrGIwcM5IJ3kQ5_E7Zgc8O8gTLQmHX1GMzl5is0wrqwve31IzJFJnmzfLgVAJu1G_tbtjHfwdFhUMkoRkEhGbKOO1rIY_vqAqj49SHpoZaAoL7Wk5oIJbT_upRj2JI6yes3IMeMPwrn3Cbh1wInk_Df_zzaKuzsR89Hzk8Pys5AKfG3vNv5a87vbfJf5uEI3AAx4RG3RIy1vJhkuLFjPszsGKO5fq15NIgcLeNL2NlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUPFGCCn74G7GanGJ4ZBGbQqGIDw-oUUyyEMwP2Qt2gPuMpxAJf8ZlXY9f123ADzQGS935qHeEShaJkfdl5XvgjVrzpSkAZDkT_zWRfHXn_TewSQf7-dKkhG5DwqVTnmQtHnl4sBpQbtaWf5lop-knDtPcZV81s2mya29P3X6rMULDs-apX9WVOsX0H55X6p21lYvw1r9kSFigiFUNklaDQXS_CuMyi9Uw5w-vIhdtKbzNap-TZ3tPh0-FT1XzcoxXvlcbal0PcbYl1sMle0-FtLXGAH-fpV1dGRhlce0_jdN8tA2DFEHeYofl4mat3q4vx3rY5kk7vs0w6RNvgktQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، با جیک پل در وزارت خزانه‌داری در واشنگتن دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148084" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148083">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2f66737e.mp4?token=feLkEjl1pKBj5H3ru0JyeRyvxPmAjqRWjljUAu1dFbwLMLxqvxU3mzqtTpDoNgrCHX91stHZB3_nbwuIo8GomU0iyJIsDzVlI_ELpDiQHljDCWR3dg1q1th9e-aTwwTrgmLYmyTK90yO34TidOz5BgWvqTSZ6LcZFayCGrerAQP7zj_zHU0JzdjU8Kolwr8W2k8RQ7Cfn_26y1sMRM0JXTu7xrrzU1JUdqASNrgpW9OBR1kfV7TkYHDf-Uw-EqvZjSIfiW_m-2SnA_pNxcMuNt1-ywNi7R9ZTbGD23LsCYLYStOHtUJ1CSwLs2a8f-9ZxhhX6uO0Rt6ao6N8bpO53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2f66737e.mp4?token=feLkEjl1pKBj5H3ru0JyeRyvxPmAjqRWjljUAu1dFbwLMLxqvxU3mzqtTpDoNgrCHX91stHZB3_nbwuIo8GomU0iyJIsDzVlI_ELpDiQHljDCWR3dg1q1th9e-aTwwTrgmLYmyTK90yO34TidOz5BgWvqTSZ6LcZFayCGrerAQP7zj_zHU0JzdjU8Kolwr8W2k8RQ7Cfn_26y1sMRM0JXTu7xrrzU1JUdqASNrgpW9OBR1kfV7TkYHDf-Uw-EqvZjSIfiW_m-2SnA_pNxcMuNt1-ywNi7R9ZTbGD23LsCYLYStOHtUJ1CSwLs2a8f-9ZxhhX6uO0Rt6ao6N8bpO53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف طولانی تو چین برای خرید ایفون ۱۸
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/148083" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148082">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
المانیتور به نقل از یکی از منابع ارشد اطلاعاتی اسرائیل: نهاد‌های امنیتی اسرائیل با هرگونه حمله پیش‌دستانه علیه حوثی‌ها مخالف هستند
🔴
حوثی‌ها می‌توانند سعودی‌ها و متحدانشان را به اسرائیل نزدیک‌تر کنند و آنها را به تکیه بر قابلیت‌ها و اطلاعات اسرائیل سوق دهند
🔴
در حال حاضر، هیچ‌کس بر حوثی‌ها بازدارندگی ندارد؛ نه آمریکایی‌ها، نه ما و قطعاً نه سعودی‌ها، آنها آن اسب تیره‌ای هستند که هیچ‌کس انتظارش را نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/148082" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148081">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55aca14f0a.mp4?token=Ltp_0PQi0Y7D2GqpNWVs0o44WMOWmJl-cxb_aw-VeCH2BYgNBYpo2SFlcvNsRB90d5cjL5KHuueP1naHyj3cf0DJ1C49oBqdXYIp4vr9eIz7rDClwnr-j5bt7IUweqoFqwLUz3jcI3p_D2PlHSvght2L8prMx9djuGMmBwI0lRvv93yXw7bojRpYzHTrgcRxPEWm5JSX5v4_5s_QJirW63_FbwmuwLfCs9skCqGFR47_AQNnfyrkn9KIyNJWUYdAZ6CgI_if00rasUaeB_mMXxCm8Q8jhcz3arXwMUbI45WgSAOxRb0yAqlmaD4NdkUfCfln9krm4ntaBf4Karewzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55aca14f0a.mp4?token=Ltp_0PQi0Y7D2GqpNWVs0o44WMOWmJl-cxb_aw-VeCH2BYgNBYpo2SFlcvNsRB90d5cjL5KHuueP1naHyj3cf0DJ1C49oBqdXYIp4vr9eIz7rDClwnr-j5bt7IUweqoFqwLUz3jcI3p_D2PlHSvght2L8prMx9djuGMmBwI0lRvv93yXw7bojRpYzHTrgcRxPEWm5JSX5v4_5s_QJirW63_FbwmuwLfCs9skCqGFR47_AQNnfyrkn9KIyNJWUYdAZ6CgI_if00rasUaeB_mMXxCm8Q8jhcz3arXwMUbI45WgSAOxRb0yAqlmaD4NdkUfCfln9krm4ntaBf4Karewzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا امروز همزمان با دورهمی جانفداها به صرف انواع خوراکی، یه دوی ماراتن ۱۰ کیلومتری مخصوص دخترا تو بوستان ولایت تهران برگزار شده.
[
@AloTweet
]|</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148081" target="_blank">📅 21:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148079">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWF7-Dny6cuLyTbDAMzcQKaylz8NLn7U3w9JIpd9QWb2ERQUEQ6t_4iWBLSIpN0emVVad7bvYnAuyniS-ZUxiqf-pp7SwnbhPbZpJwK1bPrrb7dRuA75S2UtQJMCwV4rVforlJUAGO-v5CiXMr4kbPAR30Fv1hl92vt8vdK5OwtXfsebWsACJsbw2BiJn6ShoT4eyPg9YNt-KJ6Ja97Bc1g3-gFXBOlUhx9cj_D23wT2jEX_SbbLwof92mwxyKMSHKrOykSgCh2gxLbY58YPzFYoE8eJzq54P9jor1d7h7Wx23ltDRqrKIOpPPxYjeQSVbvGX7Usd4ULVRwfX6QoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاليباف
:
دوره‌ای که در آن F-35ها و F-15های شما شکار می‌شوند و مجبورید گزارش دهید که آسیب دیده‌اند
🤏
از قبل آغاز شده است.
🔴
آنچه زمانی سوخت خالص کابوس بود، اکنون واقعیت روزانه است. با آن زندگی کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/148079" target="_blank">📅 21:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148078">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الاخبار: عربستان آمادگی خود را برای لغو محاصره یمن مشروط بر موافقت یمن با اتش‌بس، اعلام کرده اما بعید است یمن از این پیشنهاد استقبال کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/148078" target="_blank">📅 21:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148077">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPN7WKiME3P-ySsotR0QPeJkvJDVztD31-qUDe_sHi6mkhmfXqq5HywPg5YF20AIQSu-OdMOEUxWMpyDLiSmmwdjH1XRlglLeHDB0MglGaXCbyI-DB57iwPLpmpQ3zlKTML6pGTu5qQxHWMvNkXnZEYz72UQh3vhzeCoHeOA7S2HuFDW3GvwFbVSpK_DInRMSu8TShDXukPLRl8q1aLiobocFzIXRu1FaUawlEHLkj_C4QhKPaT7zuta9ZOSj-pbevSrCJ289CAcJ0rco8QSzE0Fd4yL_FZGy9Vy9noW2bcuwwZ-L9CsaFa6gumPoilCh56BiK1hNjZekZqAWg1_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور چند داف در دورهمی جانفداها
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148077" target="_blank">📅 20:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148076">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
صداوسیما: دلاورمردان پویش جانفدا بعد از گذراندن دوره های آموزشی، آماده دفاع از مرز های کشور میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/148076" target="_blank">📅 20:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یک منبع مطلع آمریکایی به الجزیره: ۶۰ میلیون بشکه نفت ایران، یا نفت مشکوک به ایرانی بودن، روی کشتی‌های تحت تحریم سرگردان است.
🔴
کشتی‌های حامل نفت در خارج از محدوده محاصره در معرض رهگیری قرار دارند و محموله‌های خود را با سرعت رو به کاهشی تخلیه می‌کنند.
🔴
واردات نفت چین از ایران، یا نفتی که احتمال می‌رود ایرانی باشد، به ۴۴۰ هزار بشکه در روز کاهش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/148075" target="_blank">📅 20:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی، به عنوان بخشی از محاصره اعمال شده بر بنادر ایران، مسیر حرکت 105 کشتی تجاری را تغییر داده‌اند.
🔴
این تعداد 2 کشتی بیشتر از آمار منتشر شده روز سه‌شنبه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/148074" target="_blank">📅 20:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خزانه‌داری آمریکا: علیه بانک‌های حامی ماهان‌ایر در امارات و ترکیه اقدام کرده‌ایم
🔴
سخنگوی وزارت خزانه‌داری آمریکا به الجزیره گفته واشینگتن اقدامات سختگیرانه‌ای را علیه بانک‌هایی در امارات و ترکیه که به گفته این وزارتخانه از شرکت هواپیمایی ماهان‌ایر ایران حمایت می‌کنند، آغاز کرده است.
🔴
جزئیات بیشتری درباره نام بانک‌ها، نوع محدودیت‌ها یا زمان اجرای کامل این اقدامات در این اظهارات اعلام نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/148073" target="_blank">📅 20:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / ترامپ: "باید ببینیم" که آیا ایران نابود خواهد شد یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/148072" target="_blank">📅 20:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عربستان: ائتلاف دریایی دفاعی با مشارکت ۴۱ کشور عملیاتی شد
🔴
وزارت دفاع عربستان از عملیاتی شدن ائتلاف دریایی دفاعی با مشارکت نمایندگان ۴۱ کشور خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/148071" target="_blank">📅 20:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری /گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/148070" target="_blank">📅 20:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ در پاسخ به سئوالی درمورد گزارش روز پنجشنبهِ اکسیوس درباره «تصمیم بزرگ» او: «آنها حالا می‌خواهند به توافق برسند. اگر این توافق، توافقِ درستی نباشد، حتی به آن فکر هم نمی‌کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/148069" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ به شبکه نیوز‌نیشن: با حوثی‌ها در حال گفتگو  هستیم. حوثی‌ها نیز تمایل دارند به توافقی برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/148068" target="_blank">📅 20:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/148067" target="_blank">📅 20:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148066">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7ZosxuXmBakGNcICbpBO0GjffI5uO3ir83ft9L6AN0Uj-Yi3_GhARm7b4ohrxsf5y6t4c6mNUxx6wGyWJ6cu7S9q6sbiHwR_ZknfrZC1dI3KEyBw-sFE5shR1Y87do-Z5o9u8uZtESkgwURJDvsbe0GOP9Bo6xaK0YjYaXlyrGsJR893cNICDxTdzx8iIXv0QKi-FF4gTPAvnBnf2Y3c9jlXKQ_Vw0WKh1kCnngZJTDXddatKCn8JOd_AbxJLNpSCRbuc8XnyKsvUHOT2Ilcd5lXC4EHLCPsy8Usy9FUfkQ8LC9gCcylyiVU_zHzicQtLbV8yXfgcrPxZBaqhZanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148066" target="_blank">📅 20:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148065">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مشاور ارشد رئیس‌جمهور آمریکا: ترامپ مصمم است جنگ ایران را به‌زودی پایان دهد
🔴
شرکای او در منطقه نیز همین‌طور هستند؛ هیچ‌کس جنگ نمی‌خواهد
🔴
او به مذاکرات و گفت‌و‌گو‌ها فرصت می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/148065" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148064">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX2ZnWcCRAQEUqaZ0wVbx0j4ZigA4jVy2PdpUW5x6xbHGLZHrP-epceIWIJqlR6ggMoRykd20m6NicuBwWIFdb-JTSx7L3Wbz0IuHXzYG4Np1CK77ptiFsaJHaEkAIPs4f-Jv1D4dR2LozvNKUNeUxR5dkd7qd4zntaZ9KYUgMxoC0KZGvw4rDrEr3STP-qbZhdo-4W2nqixf0w8QPRmYsSReQQDOckm054yjOEN70ebG0cBQkUeRkgSaZ1j8lvjK6O1FH_BXMOFFmKnO79q2vJmRR0XYaJmXOh3J5CBT-AJnYuzG8pm5JuIzmVLN0FUnzmwAsY2NaOBubmXsMrBhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زین واکر، بازیگر معروف ایرانی هالیوود و برنده جایزه نخل طلایی اعلام کرد بزودی به ایران خواهد آمد تا از خاک کشور دفاع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/148064" target="_blank">📅 19:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148063">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فرمانده سپاه: آماده‌ایم به هرگونه محاسبه اشتباه دشمن با قدرت پاسخ بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/148063" target="_blank">📅 19:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h2MDOlHQmo4D5a7oo0tMME_pzKp_SGo7eqptJBmb9sTgNEN4VofmZWUagQXABrFKxhBQkW9-lZx2DW2T4RdK3ywyaj-htMdCUj-egY17T-jHus7HMpH23EozSheeTlKwDkh9WAKZ2xAvfrueQ443Q2Cj-j1rgDtNdB2aKCL7dEV2UIltylDSMfMQjUVd_0uRKme62bEst8ZAF3d_v_qcAEWNRIUc_CIz_dZJ3QNS-RGwAIysvyI9I5cOa0sR0JdSRGVcmwzfiwLtyZ3GMcE7TA5PTj2PJYG7udi7ezzFglSVkRuDuBkwl6zd2jH1K7PLeaZEzQKjc-WsQlxXq2vSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش از این، نیروهای ارتش اسرائیل (IDF) حملاتی با استفاده از توپ‌های حامل فسفر سفید را در منطقه القنطره، در جنوب لبنان، انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/148062" target="_blank">📅 19:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148061">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ce71b6256.mp4?token=gCV9i9mQydkp5SOQdORg0nbh2jQpau9TKSUtOvEGAOugw6YW-WY5n0D3dlxz-EZ43YeDtLvrlarQD2nQlOyPIMpg5uZdJX1gQFo_5pEriq0q2M8VJIShw2HBQzY2TsTcjjHvrmfuulpqOXa9EEJkKBFzHFRDzIBpYIb3lhH_q_tL0Wn8RlxMEpAfwbc0GTWXQR4JKwIkT5313q_lH_qt8cL8TQqvdqvJJq7kopldJwbjZLxocACQe2qkOAVIdFs6MIeOT_aqnoDhg0iqB83pIQZoxuccrhmukVcS1VrT1QzHCoG3IFM-wm5hrbQXT7Lct5O9Lnln6-rrEnJIVeS2_2Ftcrw5q5U-853f5OlRsPOJ1VGo7NQaF6l-OTPtMKfDgtoJArJkrVEzpwoFnWb9vTfINkhPXue0Lm2dnknuUtyQuHoy-oEKz8OJB9ioWgL1gT2MKSzx8sVLDkOBAaTSqtZ3uxodDt2qxtZtVkeK9Fi5nyQfftesGHOBZmWlmCN3MlR_rIEMK6pNY1YWkKguaNoaMKVxMLcwnt9nPZtQ6Wsc6iNsb5ukDRO0A068YmLxO_Ynpt2dhack3abPYGtbkMhEjKdjkEiX-bGpWFd4J1OD3Wm2ETaUF2KapRvGbPZHdn14XnIRfVgspIHsD3sd7SrHMbe6M6k1IEXFRspZUvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ce71b6256.mp4?token=gCV9i9mQydkp5SOQdORg0nbh2jQpau9TKSUtOvEGAOugw6YW-WY5n0D3dlxz-EZ43YeDtLvrlarQD2nQlOyPIMpg5uZdJX1gQFo_5pEriq0q2M8VJIShw2HBQzY2TsTcjjHvrmfuulpqOXa9EEJkKBFzHFRDzIBpYIb3lhH_q_tL0Wn8RlxMEpAfwbc0GTWXQR4JKwIkT5313q_lH_qt8cL8TQqvdqvJJq7kopldJwbjZLxocACQe2qkOAVIdFs6MIeOT_aqnoDhg0iqB83pIQZoxuccrhmukVcS1VrT1QzHCoG3IFM-wm5hrbQXT7Lct5O9Lnln6-rrEnJIVeS2_2Ftcrw5q5U-853f5OlRsPOJ1VGo7NQaF6l-OTPtMKfDgtoJArJkrVEzpwoFnWb9vTfINkhPXue0Lm2dnknuUtyQuHoy-oEKz8OJB9ioWgL1gT2MKSzx8sVLDkOBAaTSqtZ3uxodDt2qxtZtVkeK9Fi5nyQfftesGHOBZmWlmCN3MlR_rIEMK6pNY1YWkKguaNoaMKVxMLcwnt9nPZtQ6Wsc6iNsb5ukDRO0A068YmLxO_Ynpt2dhack3abPYGtbkMhEjKdjkEiX-bGpWFd4J1OD3Wm2ETaUF2KapRvGbPZHdn14XnIRfVgspIHsD3sd7SrHMbe6M6k1IEXFRspZUvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد کشتی گارد ساحلی چین با شناور فیلیپین
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/148061" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148060">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/148060" target="_blank">📅 19:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148059">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر کشور پاکستان طی ساعات آینده دوباره به تهران می‌‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/148059" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دبیرکل شورای همکاری خلیج فارس:
ما تجاوزات مداوم ایران علیه کشورهای همسایه و تشدید و هرج و مرجی که دامن می‌زند را محکوم می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/148058" target="_blank">📅 19:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=M4YbYrbd6eYSyKO_SDgChf55ARKfk1BT3egw8qaugtJlNYIIF-mRGXC_KYtI3FWwRVuuDmXseIiv21tehvlIFF8i9Z6r73dXC1mkolusZ8FD5FvWoRpVOxVRa0s7snkjTStXYlo6x5an6eRPzX96eDocYYmlG30IMuyvPGbbgh_TZuUOxl37blQW_YxNghtBoNWKLrVIryl_KGC7VyZWzK0sPubjRbtqfFlfQMM8RegdxPNvjQ2r4vFr2t5onzkQtpyAN6miO5oe8MLIazsm-Rqkc3A-T-lMZxEI6Z1UNyCCU8fyT1o0ZU-Yh5SNwV9XoUmRx0s9UmlpVsRWr5L67g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=M4YbYrbd6eYSyKO_SDgChf55ARKfk1BT3egw8qaugtJlNYIIF-mRGXC_KYtI3FWwRVuuDmXseIiv21tehvlIFF8i9Z6r73dXC1mkolusZ8FD5FvWoRpVOxVRa0s7snkjTStXYlo6x5an6eRPzX96eDocYYmlG30IMuyvPGbbgh_TZuUOxl37blQW_YxNghtBoNWKLrVIryl_KGC7VyZWzK0sPubjRbtqfFlfQMM8RegdxPNvjQ2r4vFr2t5onzkQtpyAN6miO5oe8MLIazsm-Rqkc3A-T-lMZxEI6Z1UNyCCU8fyT1o0ZU-Yh5SNwV9XoUmRx0s9UmlpVsRWr5L67g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/148057" target="_blank">📅 19:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148053">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZayEpOLb4WM1dHpk6gfLtO-C-LpPpbt9QUetMaAhbry8YT9WtGsxQDcIgbGEih4udQaNw5EqGkrrZfbFjsF0ValZlXqnTLOl4VC8cnnu8HIL2vce9xC61M4LwN5cXuowWb4XnxihmYhfPbdj73yr-0gq3xhA0vzbN7Q5zPZg5O1TrTv7vVQAg15_urSMaddEBeJa9vOODakTB0QR536hujjOQd-xW1exbpa578i8FqwdmBYZn-MNjlxbBTgpCe6PoOq5luxa8LragJ7SpVEW1xRdWFzJDNFkvV-lEcrKpzYN5ou-oCERp7gAnWCeUxvX-wsM9HxII2xgV6EptFmTNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9ixOaaR4FIuOSZ50PEuiyTFDFPbgweFyCZgUPWzLLH2dQhuPuMLMfB314c5biJc3BO7dq1RGXB3NS9cunFyMTHxbwmOQs0ezVCK5DamrAyH9u8-ssowTXzBf7NqvKFeHmgFW6e1uBgjohO75RpyylUoiA3-nO5sziUY2zG2gFJUaxU2WMuJW_D1jT2v75h1K_4pg349oL4fJPyIC6vRoDzthFKbiCNp3VViDAbrb8BHWZ-6xWqtIq7lG1RRAwCGoV8iLtNLO48XnB5ud4YxmSGXc89jOWOMovr_pxYJo-Z8-NvMeDuK2cDX6VyrO_Ph84pIqzD9iBGVl9INhctKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrjDVZQj3J4R_Wg4KS6cKvA7GfP20TyZmYi_Mb-d-ReygC7-T4-G0uvikXikBYa8IpEnXYHF03V2EakXI6Yc6Okm_MWj5gvU-HKd7BO8FV2QXNtY1IGgSopZX5JiFnU1tt2s1iUu32t5cI69mkmRBrWoH_W0KHhfXJwjkp7rMO3IESy5v4WeXUCiyV6ROUeDCY2RJMIZq6CH62Mi8lMKyK4o5BfHDj2dSWr-fGvuCQ5Vyy8IIu6im_kaahYymrAd-0Ws-Ac92fcVuVg1f7p1-4Hmgkxo_pEcptcrrOhAFpcy1udtD90k2QNlm6gphpMl9keg0O_9KkU6b2k-N82KUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlaMj7z-SfrE-klI87yJsWi5G2SRPl1lDpa4XXNwYEgTJ0GFXpbYuysFMi0x5Yc8duLTtogxh_BpjFhlTCVxufu7ozwDu8M9Mcq2-Hv5HY-2_xxRQz9gCCE8WETjQCzsKVgYPmO3TrRNvu2UEOCW-1-gaDs3lXryaw_9q-aXnJpgApJh173KwLwWBm-5K-eiVAeyUX9T4o3UH8UAHQ-V8qNKLLyYL-azhPIq1kcmWo_YzcHCxcjQb_ujBYTiR3qxgTKQpILqfkAQ-yj68AxDbyPxpiWBQhFpNqqgf1uCLjCjbRvGPGNBgT6meqjaszHVodws6PaZqGQrIbNoxn8R0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یاشار سلطانی این ۴ شخص رو اعلام کرد که حدود ۸۰میلیون بشکه نفت رو بالا کشیدن
🔴
۱٬۹۳۲٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰٬۰۰۰تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/148053" target="_blank">📅 19:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=kf0KLSYbLTIIGQoo7ZrO_Sq--V2cyiuw_V5u8dhM4m7q9wOkXNUjgWmLrcjt0BqAmwMiSHrtykT1LA1EuK8o-_G5_ZAqtYdHflL09ykpki9zBlyHMcN5gzT1Y_4NDrgWOc3toZ__FIZ-p5YAXA3cYdOmP69hXzUMxVrL_rJGaEEpKSlRm-MqoZGdUxDqqQUEifP2lks8kIXszUFEOMODMRGVqpXbxHmfz1NpSYZ2SdC1qo6VXuL0hth8OyKr1I-9dRJDc24byHVxeURh8-QolGIReZe5WcR91HnyNEuuR6_ChHIx1r71lXAdwNVi0kzkPEsjv_JcgJk-9g75-Lou4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=kf0KLSYbLTIIGQoo7ZrO_Sq--V2cyiuw_V5u8dhM4m7q9wOkXNUjgWmLrcjt0BqAmwMiSHrtykT1LA1EuK8o-_G5_ZAqtYdHflL09ykpki9zBlyHMcN5gzT1Y_4NDrgWOc3toZ__FIZ-p5YAXA3cYdOmP69hXzUMxVrL_rJGaEEpKSlRm-MqoZGdUxDqqQUEifP2lks8kIXszUFEOMODMRGVqpXbxHmfz1NpSYZ2SdC1qo6VXuL0hth8OyKr1I-9dRJDc24byHVxeURh8-QolGIReZe5WcR91HnyNEuuR6_ChHIx1r71lXAdwNVi0kzkPEsjv_JcgJk-9g75-Lou4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی، خبرنگار:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/148051" target="_blank">📅 18:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
منابع العربیه: محسن نقوی، وزیر کشور پاکستان در ساعات آینده به ایران سفر خواهد کرد و در تهران تشدید تنش حوثی‌ها در یمن و پیامدهای آن بر امنیت منطقه را مورد بحث قرار خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/148050" target="_blank">📅 18:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdWW2UH69HO1R4ZisgXX78KJQx1RyxUOn2avwabXNH3yembNq5wNCgF1V94s2DnoGgA7L4FQKmH2FweBzFbiyE8lS-43GVHDUt2Z0dNbc5EpVzRHlRF3V7x_ljd9sodugGXpZ8A_jhpiGwdQqcOsZq5JxnxvGTAXYqhFSMqrdKGGuoCXxKEaIqa5P_AUpyH0YmTKKmX5rgtXyuAy75xdNOk5r75y6q210C4AwPLncVWkNrNMCCTQMhaj0JK4_FgYi9o3sfMMgFHU6w8EdunY2klerAmtpqLDS5xIXVroS-p57-WWhsQFglX_n4Ae1qv8_Vx1vH5fQ9wIAc1lZWKJsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: دولت و شهرداری هماهنگ شدند تا از ۵ مهر قیمت برخی اقلام اساسی کاهش ‌یابد و تا ۶ ماه ثابت بماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/148049" target="_blank">📅 18:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فیلد مارشال مخالف صد در صدی مذاکره و توافق و صلح بود و تقریبا معلوم شد چرا و به چه دلیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/148048" target="_blank">📅 18:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOCnuNdUR2OR-S4g2ZVN5vGJbsueBmgB5MCxnEY-mDk1Ax5QpIMioroc7ifgFDk7iTTTNZEVd8CCF-4KxdG3OlP3IA-kmotuOr4NCUD8Ug28IpBvDsVgacTo9T7Pb1y1rJSc2GMi6wlseLSeb4Q9Ug0ga3UqaKpJK8SOHLqbcOLlQhkm7jbL1zfkF815m_oSBqMBryuYo5ZntPBI6pEGXOt911FxmNS65rsx6yut1IF8nCFXJ3mNKhMtCkMnRyCUtKZQfekyUDRLNc1BtIH0NEPPdb-5s8ya8AS8Jxyb6oE_bHbe3mRPJFtC8x9W83FDd6ap2eM2VUKdnMbEIY5exQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/148047" target="_blank">📅 18:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148046" target="_blank">📅 18:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
👈
یاشار سلطانی: ۱۰۰ میلیون بشکه نفت گم شده و نمیدونیم این حجم عظیم نفت کجاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/148045" target="_blank">📅 18:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac59fbf2fd.mp4?token=Cw8kPFpN0MGf9FhUuzrtifESpMmUsG4sLn_kL2IdvNOWG68q0xjSc1AC0k3_V-l_9XB07d4dCq03P5Zz0KYZPFoecVThJAkwLCb19AT6fQI26JiKDBcOX4KENlufQiTmEaVVn23PFvrdt_zIFn3uMRIInlyo0_CzaCe3FotBiAL5xfyeDcP2-fh3haLqRtdAPChV2gz72p5_5_Mksg-GkHhIEnROx3jEhqZ2g9lxFg46xPQyY_4Hto3AkKnSv57pz8u1Tba1-i9NGdikbV_JOimfT4LJCfAU3vHAPBFNBNieEWZHxlAJHOfOcwh00qAzl8kSS-mf8e647TXiDENzXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac59fbf2fd.mp4?token=Cw8kPFpN0MGf9FhUuzrtifESpMmUsG4sLn_kL2IdvNOWG68q0xjSc1AC0k3_V-l_9XB07d4dCq03P5Zz0KYZPFoecVThJAkwLCb19AT6fQI26JiKDBcOX4KENlufQiTmEaVVn23PFvrdt_zIFn3uMRIInlyo0_CzaCe3FotBiAL5xfyeDcP2-fh3haLqRtdAPChV2gz72p5_5_Mksg-GkHhIEnROx3jEhqZ2g9lxFg46xPQyY_4Hto3AkKnSv57pz8u1Tba1-i9NGdikbV_JOimfT4LJCfAU3vHAPBFNBNieEWZHxlAJHOfOcwh00qAzl8kSS-mf8e647TXiDENzXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لباس فرماندهان ترور شده در رزمایش امروز جانفدا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/148044" target="_blank">📅 17:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر وقوع انفجارهای متعدد در تنگه هرمز منتشر شده است و این گزارش‌ها حاکی از آن است که ۴ موشک کروز به سمت کشتی‌های موجود در این تنگه شلیک شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/148043" target="_blank">📅 17:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=eY70QWcaWP4v4TYg9re9X7b7-YjCQlLuN47DiTR5deX-NRiJu3gg_esxjdfhitMFq-WrkGQ_N65fJcVPrKpyhpgECoq8idF94_4IaCgzRY9GCBVbK7iUvfzWo5wVZPH0W4Oh0mPV0P9pljO4cG6QSjKfxGvEY3g4sWCXiEU2bbDgFbuuMrX66HoXHHqpBGwkxZrnlgiuZcjpL7JguFDqmQ2u5DOnE8F0lPte2m27iJOCd6KeDZP-rCKiL6B_R9GCBDJBu8ot1H4vLlxBFS6JEteOJgAvMSuIX5E_wKxpzO76a2X4xcq1vXP_BeJnGJRyoh9Bluqu1i3BNEMSjbOniw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=eY70QWcaWP4v4TYg9re9X7b7-YjCQlLuN47DiTR5deX-NRiJu3gg_esxjdfhitMFq-WrkGQ_N65fJcVPrKpyhpgECoq8idF94_4IaCgzRY9GCBVbK7iUvfzWo5wVZPH0W4Oh0mPV0P9pljO4cG6QSjKfxGvEY3g4sWCXiEU2bbDgFbuuMrX66HoXHHqpBGwkxZrnlgiuZcjpL7JguFDqmQ2u5DOnE8F0lPte2m27iJOCd6KeDZP-rCKiL6B_R9GCBDJBu8ot1H4vLlxBFS6JEteOJgAvMSuIX5E_wKxpzO76a2X4xcq1vXP_BeJnGJRyoh9Bluqu1i3BNEMSjbOniw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت صداوسیما با 65 میلیون بیننده روز به روز داره عجیب‌تر میشه؛ یه آخونده رو ورداشتن آوردن توی پخش زنده تا این صحبتا رو بگه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/148042" target="_blank">📅 17:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صداوسیما: تا الان بیش از 600 هزار نفر برای شرکت تو دوره‌های آموزش نظامی جانفدایان ثبت‌نام کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/148041" target="_blank">📅 17:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeK8kugRj42MWS5mv9m8VY5Gpmgd9VsZqIOvVxilolw6l2sbHQPJUE1FT-2j8mkGHN9bSqgXLGXDmUud2gdYvU43P_jqoLeAHGYGmYoAZ110507L8Rty-KBWU5kt1QdGOJzRPRS47j7x36irG0od5gg0C3_uXV0xlRxWrVirRxH6HY4qcFwwdeuNHexyK10m035cF_D2sPm0vxVJyJwVsTgOTeHr_AzRIBerKSxvLB-s7KQtKF_gh3pToV3nObT26pbFMqPIOgk5RXvYIfv6T6e0U9upAPA9uCkFApl5K1av7d5qKyN7xxE8JfbdT13z2soQBjHpQjIDnIlu5gWO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انبار مهمات در منطقه "ایاش"، واقع در بخش غربی شهرستان دیرالزور، سوریه، امروز صبح منفجر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/148040" target="_blank">📅 16:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148039" target="_blank">📅 16:52 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
