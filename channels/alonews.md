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
<img src="https://cdn4.telesco.pe/file/SN3MWV-wzQYAq2seln4eToVb3D4kGTvU45xzt3k63VMIPqIGkhsfxSl-eUchaxrsFVeP0PlVM7nPERlEft6S6EKmTAMCUgUPCyCc6oiFvuTcFc7hIczuXMRNfhQ9Jc5_IWX6sMHXTKtHzH6e2zBG-LmurMz41VkTcEACsv-jU9LO8oZhMswM2BC-RXuPj48rRddZYydMjLWzVOn2792ABev6rbk--5PojWwx_9xYDFW2D5Ahk3t1Ddw_NP2NqjBQV9boGe02UK9cpETGBFNoqI4qbUdITPiRyQxILaKDZch6XnAkyn6f6XlVMCmjUb6L4yBBhJCCGF89FZcOBuOt4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-145583">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b6764494.mp4?token=HnKvPLUGk1eM0EtZPpZAtBaf7sn2mbvP8VphmR7v7oGbk_9rSQBdpC9-MyN2Ye5kU4bV-L10OZXrWqbyA3UGU3BGNHCBevw_9VQTJ0QMETgwhBvHKzoIZRXfhDAd5bp00FzzRkbFGdTLudp_mCNF0ciGWXLJIKOp5VGvXs5V4O5aSzt_y3XnbsmdK_7EoDqhm5f7f3USzQW8ADrNzhlFO-p_f78p9RgOeS6b_LWNAuliBRUPnJPwfhoiUNIkNWfgwXxJhO5mHjo6nWKs-hYGFohD81KdnBohM-EyKrhizxBVycgc6msOmKMODNdDXTL64Cu7S-YJ5oSICYUuvVZgAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b6764494.mp4?token=HnKvPLUGk1eM0EtZPpZAtBaf7sn2mbvP8VphmR7v7oGbk_9rSQBdpC9-MyN2Ye5kU4bV-L10OZXrWqbyA3UGU3BGNHCBevw_9VQTJ0QMETgwhBvHKzoIZRXfhDAd5bp00FzzRkbFGdTLudp_mCNF0ciGWXLJIKOp5VGvXs5V4O5aSzt_y3XnbsmdK_7EoDqhm5f7f3USzQW8ADrNzhlFO-p_f78p9RgOeS6b_LWNAuliBRUPnJPwfhoiUNIkNWfgwXxJhO5mHjo6nWKs-hYGFohD81KdnBohM-EyKrhizxBVycgc6msOmKMODNdDXTL64Cu7S-YJ5oSICYUuvVZgAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله توپخانه‌ای اسرائیل  به شهرک «بنی حیان» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/145583" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145582">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
سفیران ویژه آمریکا، ویتکو و کوشنر، به مسکو و کی‌یف سفر می‌کنند تا در مورد پایان جنگ مذاکره کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/145582" target="_blank">📅 16:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PO8rZ59_dxJ9Ul0vkywIewofYSB1FfZeXK9zZJKiwQqQNtimtPVKcHHrwqiZvow2JyCja5S5P_EYKNyx_sL1nYyNAUgJohOFI4ut7e-6aGudUT_-rW1icM7TqvwSjy1I8sTWaPDnxhf_251D1PZR1h1JCIwOLaNtmr2WuWKpHtYn7JLz-zclAq5apQSlwD36m87RESF8hlA8Hwlw0t1yBwApQ5Rv3_DEL4hGUEPQ_mOJBrC6yh3-rKz97QWslvUUR-1dAGdFn0FfL439pLtzP5pkmPoiLUVzK2hyUHBqeEzvd21P1sLJz3uyiKTR_cnpdYeTnLdktsVz2LbfZWgWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل فرمانده حمله به سوفا رو ترور کرد
🔴
ارتش اسرائیل یه فرمانده رو زد که حمله به پایگاه سوفا رو هفتم اکتبر رهبری کرده بود. این فرد تو نگهداری گروگان‌های حماس هم دست داشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/145580" target="_blank">📅 16:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
انجمن اتومبیل آمریکا اعلام کرد: قیمت هر گالن گازوئیل به ۵.۸۵ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/145579" target="_blank">📅 16:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
سپاه هفته قبل: اگه اسرائیل به تپه‌های علی الطاهر حمله کنه با خشم ما روبرو میشه
🔴
اسرائیل دیشب اونجا رو فتح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/145578" target="_blank">📅 16:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145577">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قیمت جهانی انس طلا ناگهان ۱۰۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/145577" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145576">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7wPttF1EX4RMVIKljtaQleIMmoOI0ArGuoAuTQ370jExYcy9UwFLjgdv6yqLLszXevJ9c-3M5fOaQoswRMjlFhsGNmMs5t38QvEyJpQmEicreHnjTQmXhCZkGZljMcH_cWKFtXYAm3fjNqnjQJorqFnBi4-W-imdvGgBULnNTXCuLwUjknK0xnJDaDVWv5SncNhmHYJwIba3Hx8XoCUx3YhbXyK7QpRx6IG-FUq8WlbIoa5mp8_hS90MsX2XjfGI0cas0vfNf_64BNX2kWv__Qb8y6B-kzc-l2_lhFHDiqUDZWFO9o9mS0CGU_T-bQuK2NOMHZZ5nVNSAbVFtpEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی انس طلا ناگهان ۱۰۰ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/145576" target="_blank">📅 16:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145575">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
العربیه:  عباس عراقچی، وزیر امور خارجه ایران، اخیراً با عاصم منیر، فرمانده ارتش پاکستان، گفت‌وگو کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/145575" target="_blank">📅 15:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145574">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
پنتاگون: ۱۲ سرباز در حملات چند روز گذشته ایران به اردن زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/145574" target="_blank">📅 15:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145573">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: اسپانیا به دلیل مهاجرت، نابود خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/145573" target="_blank">📅 15:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145572">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Nw6LXDfO3wQLYtlH3YFKdjdmfxq_PVQMDvc-1gtP6tPPpJfmzv7MgzG3SIP5WQAK5r54UzYr6JgquUu0Tfs9tmKRPVv6xYMWowuD89z3f7F4F4mVWrQDUzDl9kHoWlLDFqSsaYPhoz-w1FnJE5UtEYtq_dkk9kvTL0NIz2pPLBO1xirT_8EJb6UymRNZqFDDwXG5jDA8k0I6i2xWiNj7QsQGiI3fZOvZBQOQkJLnJxAaE2gaKznSD4I5d1K_ieC_Wu_5zZPK1SPt9CsQv412jGgKLHepl5IpnGyFT9sG72hF6zxdJIG9ihd_ozRsCrxBt8ZVK-LLgCKNC6_2NHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین و لهستان در حال بررسی امکان ارائه یک پیشنهاد مشترک برای میزبانی جام جهانی فوتبال مردان هستند. کی‌یف امیدوار است که این همکاری، تکرار موفقیت این دو کشور در میزبانی مسابقات یورو 2012 باشد، طبق گزارش نشریه POLITICO
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/145572" target="_blank">📅 15:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145571">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vySZl7bi5NRLitMjI6VW8vomiveyvL7-d0EcgA5x_JR7DoDhrRbD6bR7jHyALar2IlUSukSv8sWvfX2nDRpubEzWRL6DUbZCHgMoyJJEzK4Z0OzT7disMc3pQe77Uk1OzpYTkrk0aAdbh67isE5kiGPwK2873Is0HlxBM07abM6Fh77-6Pq11Jq3W4NjGFE6m5rmAn9snTcZVMdRbP8CyjK6S8qPGIHg8A54x__Ka5-VGkM9EXzX45btxBMFmi0JlDnUoxFSsuMRz6a7a5Tt5J_Fn9ZPFiMAAojkO4w9OTU5v110-o9JHFnB18INC0Cf93OIbahpfjxauhuxElwFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اد میلیبند، وزیر امور خارجه بریتانیا:
موضع بریتانیا در مورد جزایر فالکلند، قاطع و ثابت است
🔴
این جزایر متعلق به بریتانیا هستند و همچنان به این وضعیت باقی خواهند ماند، زیرا این، نظر غالب ساکنان جزایر است.
🔴
حق تعیین سرنوشت آن‌ها، از اهمیت بالایی برخوردار است و بر اساس قوانین بین‌المللی است، و ما به طور قاطع از آن حمایت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/145571" target="_blank">📅 15:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/17e7eecdbd.mp4?token=ZdrDHo1CqkEM8V2nc4S-OGfW4uLLXqLus0WrMVOLR8JTde6pUoznStvb5Og4mFLLJb9nb4FN18IaBTeEFUWYlFfgxopKzM5TEAwNngdvSq4D5cpqrqEj6U-C-gNfvadHkzVn46YjASjYlssV7xMbcpA4ILZ2esnGflWMdNzXRCfpZwWRPgDbL0DriMEU8F5NxjnNEwTTMjKm4dvyb-e83ssa2qiY9mo8ex3bBdLqCzRp9km8C9Lm1kJAT4dyx1V-4JrSVlPa30ktCGAPwKcZ_jLJgR7XfR5FfdxnkwDFLMdmhot_6fYqP5u4hBXhL93o7B3_puXdYbbnbal6GMSmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/17e7eecdbd.mp4?token=ZdrDHo1CqkEM8V2nc4S-OGfW4uLLXqLus0WrMVOLR8JTde6pUoznStvb5Og4mFLLJb9nb4FN18IaBTeEFUWYlFfgxopKzM5TEAwNngdvSq4D5cpqrqEj6U-C-gNfvadHkzVn46YjASjYlssV7xMbcpA4ILZ2esnGflWMdNzXRCfpZwWRPgDbL0DriMEU8F5NxjnNEwTTMjKm4dvyb-e83ssa2qiY9mo8ex3bBdLqCzRp9km8C9Lm1kJAT4dyx1V-4JrSVlPa30ktCGAPwKcZ_jLJgR7XfR5FfdxnkwDFLMdmhot_6fYqP5u4hBXhL93o7B3_puXdYbbnbal6GMSmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی وحشتناک از خانمی که برای مهریه به دادگاه رفته و توسط شوهرش با ماشین زیر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/145569" target="_blank">📅 15:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145567">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czEWIk9Ysa4GyyHyznU6qcbhTdfCilytdoEFBbUvqOAIKuUGz5iiR9P9Spt0f0GUtOJzxFDb33E0c50hGkCg9vgwIjV1rGMUDYb0oGH4KHLssLX78CK63FZ8UgMReISXZ9Gl5hlAtVxD8M5Z75X0TZFI_HocTFvPsQMRPZRYb1X_HIXKxn-XPcs_34FDUQsu9tXpQP4nAMKpTYBhxpqXpeLm3uvOJ-xnBXO2d27y0acVcXGyhRC5L8jlXkeUZXZyVibJQms60eYjrJ1jlyAuOyN3kMe3KLipg5YYIC9Qa-hFJOO9kUu6eEyANQQDebWPfXmPmlP6rFQikWn4ZdQ92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyPLcWsfW8A4xHaGwYlsVnZAwpjsmd-lfnX9fMW4VBJAD7mzWlg-VgJjwpvDap6_CQG0E2zWyw2yu_uEIlwk0FYrtPZZJ9sIoj5jz-slVDZEWF7FWz6KjRIJSOS8PikyMmRlK7-AhV-KcxDD_SIvsni5BhgNdBgVFqGT-aY7fZBw2Lohr8DWavcfY_DHom_YhgefcwcmYGnxs1XbnrYI8HtGx-3yCw4navGGZ-d8cl0UrfCDFjKYW6jZxG_YJzspIdD4ltxniHmniHUvCBYfWmhWNpt59hi0q05gxRLeXZUCU78gpYUSY-ndugHScHTX0eG8rQ7YZllKOJH5cH61Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هشدار سپاه به کشتی قطری
🔴
دو تانکر حامل مواد شیمیایی و گاز مایع متعلق به قطر، پس از تلاش برای عبور از تنگه هرمز از طریق مسیر جنوبی، به مسیر خود بازگشتند، زیرا از سوی نیروی دریایی وابسته به سپاه پاسداران هشدار دریافت کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/145567" target="_blank">📅 15:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145566">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏
👈
تغییر ساعت کاری ادارات و بانک‌ها از یکشنبه ۱۵ شهریور
🔴
‏ ساعت کاری جدید ادارات و بانک‌ها از روز یکشنبه ۱۵ شهریور ۱۴۰۵ اجرایی می‌شود و بخشنامه مربوط به تغییر ساعات کاری نیز در آستانه پایان اعتبار بخشنامه قبلی ابلاغ خواهد شد؛ این تغییرات با هدف مدیریت مصرف انرژی و استفاده بهینه از منابع کشور انجام می‌شود.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/145566" target="_blank">📅 15:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145565">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هشدار وزارت بهداشت : در فضای بسته ماسک بزنید کرونا برگشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145565" target="_blank">📅 15:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145564">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7970c2d53e.mp4?token=HeepMqkmkL1UZRCO305nGEwdLdItSdkzLLvrZsw0ijJb9EnY3vvFLy1ZCbwrG29SjvsslOUNrafzINCIkAofAPNlnGSquQ5CVMjhcATjD7eJCpZS0wlhkadno8TqKCAEERLjPED7LCbK-0s2LKuWav1lon9nhGCLiU_FOzvrT-Te3zE5xXn6livp-G1GgT3Zg3Y9i0yFCirZocchRvB1Y48LnB7BkbEDbpj09OXysNVBWjYSvKqekQn-ZDBDlHDWi1EdPh5UIuUTCJlcaYyP83yoLviEw5rdjnTBIxsJAdQSFkAXC8Y2GBnl3Db0ZNk4JNOCbMJYVWWtzg8YlORJ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7970c2d53e.mp4?token=HeepMqkmkL1UZRCO305nGEwdLdItSdkzLLvrZsw0ijJb9EnY3vvFLy1ZCbwrG29SjvsslOUNrafzINCIkAofAPNlnGSquQ5CVMjhcATjD7eJCpZS0wlhkadno8TqKCAEERLjPED7LCbK-0s2LKuWav1lon9nhGCLiU_FOzvrT-Te3zE5xXn6livp-G1GgT3Zg3Y9i0yFCirZocchRvB1Y48LnB7BkbEDbpj09OXysNVBWjYSvKqekQn-ZDBDlHDWi1EdPh5UIuUTCJlcaYyP83yoLviEw5rdjnTBIxsJAdQSFkAXC8Y2GBnl3Db0ZNk4JNOCbMJYVWWtzg8YlORJ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی جدید از شرایط تورنتو بعد از بارش باران و طوفان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/145564" target="_blank">📅 15:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145563">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
روس‌نفت: ذخایر نفت چین و روابط مسکو به پکن کمک کرده‌اند از بحران هرمز در امان بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/145563" target="_blank">📅 14:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145562">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
طائب: آمریکا باید سر تعظیم فرو آورد، راهی جز این ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/145562" target="_blank">📅 14:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9JX29fvEZVCBdLD6sdsqy64Ul0mhFLbJp-yuLVee8V8PJHKj1AWRmtGOn3SdC-VNiZ0p-O7cHRjMlCq8N-T3sGZqu76XM6wF-fB6dCwATXE_m4EUG2g_WdbfTKQ062lqSjHIRSbnGns1boySma6ViL-TCLnUVJIz0WvfPZRgTBgyKdK81w4diZK4OeNJ86zyAKiYFqWKNLVRV9T2MZ-kUIFmliBzW-m1f0Ml8XSP6p6r15VgWriq-f6MKETP1I67XJNQZv_qI-2b03Ad-obfCkqdBntWDpp_f3-VR1fHyLxQtHYlJz0rVTBnORrVil9gOVrNNS3pWBFdtXXD4-6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردم هر کشور طبق آمار، تو فضای مجازی چطوری میخندن:
🔴
ایران: خخخخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/145561" target="_blank">📅 14:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
معاون هماهنگ‌کننده پدافند هوایی ارتش: از ۹ اسفند ۳۷۰ هواگرد دشمن را زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/alonews/145560" target="_blank">📅 14:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
آسوشیتدپرس: حجم تردد کشتی‌ها در تنگه هرمز همچنان پایین است، در حالی که قیمت سوخت افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/145559" target="_blank">📅 14:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
امام جمعه قم: آمریکا را با شوک‌های بزرگ مواجه خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/145558" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
همتی: به وقتش با قدرت در بازار ارز و دلار مداخله و ورود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/145557" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نشریه  فارن پالیسی: چین از فشار ترامپ بر ایران هراسی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/145556" target="_blank">📅 14:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اتحادیه اروپا: ما با واشنگتن و شرکای خود در گروه ۷ همکاری می‌کنیم تا بر ایران فشار وارد کنیم و به کاهش تنش و ثبات کمک کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/145555" target="_blank">📅 14:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به شبکه «الحدث»:
پاکستان، قطر و عمان همچنان به تماس‌ها و رایزنی‌های خود با تهران و واشنگتن برای توقف تنش‌ها و جلوگیری از تشدید درگیری‌ها ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/145554" target="_blank">📅 13:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
حمید صفت (رپر )برای بازی در نقش «افراسیاب» در پروژه «آرش» جایگزین نوید محمدزاده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/145553" target="_blank">📅 13:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95a10d48b.mp4?token=tatwETdjIkW5J5XLEVO9pdTgFz4NUzZ_39cRCyyhoLVUGLMDxj2MOTfbZBCJw2LYV2E_HzQ-vf5Gz0OszO59l5ByngxABVfA6HYe2K7sY4Pay67FAMCmmRLRbLVdIpODN3f1hJ-EVqRDfLXnfjqztir9r6O9y_4w-FzCu6GczhiiCXcl6pinwfd-4hDTMJYPDVEK2qoze6611iQo60bAtQNd4i1TQtaF7X6h2Noz33F2OHrsHxHsX0C-qWZt7f6vp5sDCgltKBvKxAmpeJ9YP-FKsiuXlNFbV_vAJleUKcOhzoTvtRLETM0NtSId7psNcRS55Z2s03jFyaUpfXg4jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95a10d48b.mp4?token=tatwETdjIkW5J5XLEVO9pdTgFz4NUzZ_39cRCyyhoLVUGLMDxj2MOTfbZBCJw2LYV2E_HzQ-vf5Gz0OszO59l5ByngxABVfA6HYe2K7sY4Pay67FAMCmmRLRbLVdIpODN3f1hJ-EVqRDfLXnfjqztir9r6O9y_4w-FzCu6GczhiiCXcl6pinwfd-4hDTMJYPDVEK2qoze6611iQo60bAtQNd4i1TQtaF7X6h2Noz33F2OHrsHxHsX0C-qWZt7f6vp5sDCgltKBvKxAmpeJ9YP-FKsiuXlNFbV_vAJleUKcOhzoTvtRLETM0NtSId7psNcRS55Z2s03jFyaUpfXg4jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبتهایی برای سال ۹۹ حسن روحانی وایرال شده است وی می گوید: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم
🔴
کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/145552" target="_blank">📅 13:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
البوسعیدی: عمان از تلاش برای توافق درباره تنگه هرمز عقب‌نشینی نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145551" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
حسن روحانی: باید کاری بکنیم که جنگ، عزتمندانه پایان یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145550" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
امام جمعه تهران: فشار اقتصادی علیه ایران شکست خواهد خورد، هیچ کس در نظام حق ندارد سخنی بگوید که بوی ضعف بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/145549" target="_blank">📅 13:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پنتاگون دستوری برای تغییر نام جنگ علیه ایران را صادر کرد
🔴
طبق این دستور از این به بعد نام «عملیات خشم حماسی» به «عملیات برون‌مرزی در منطقه مسئولیت فرماندهی مرکزی آمریکا» تغییر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145548" target="_blank">📅 13:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دستیار سیاسی قالیباف: ‏اسراییل قبل از تفاهم‌نامه تا آستانه سقوط علی‌الطاهر رفت، اما با امضای تفاهم‌نامه و فشارِ دیپلماتیک جلوی سقوط علی‌الطاهر گرفته شد
🔴
حال که پنجاه روز است تفاهم‌نامه‌ای نیست، اصحاب ناراه‌حل دوقطبی داخلی را کلید زدند تا فرار به جلو کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/145547" target="_blank">📅 13:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بلومبرگ:وزیر دفاع آمریکا، در بحبوحه جنگ با ایران، ارتش را تضعیف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145546" target="_blank">📅 13:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0CWJb-4fZgqio1pVxpLHf_GhrXtMQCTexN4CggORwIJRaOiVH0P_mkbXF7QeYU6fOoovPD3KmgzsebquGYqBe23mDPiltvlzNb6kRSfO5Gjmb9ByqKNHfroQEocINaJST7H7fhbG-WgdsZ-ejEPHo_CV4t3cjK2Vv4mOrexidC_7-IPUJ505IucpKNzUo1wijWfwO74OIDQhs1pP--yOnz2N1bnJ7QriNYT7xiBujBtZrx_vIip5k4eU5kEFgpAnpOqE8Qee_jWsCvAToOWCrITlSkCaxABppLCR4WLhB5ELd6ew3urwK6h6DNmfQL2BxMuUTNn9CGMvv9IYlXY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی ملکی، رئیس فدراسیون بدنسازی: مسعود ذات پرور یه اغتشاشگر بود و نباید ورزشکارها اونو تشویق یا عکسشو تو باشگاه بزارن!
🔴
جوابتون به این شخص کچل چاق چیه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/145545" target="_blank">📅 13:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر نفت:  در زمان رفع محاصره نفت را به آن طرف دریای عمان منتقل کردیم/ در تلاشیم تا محاصره را به طور کامل دور بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145544" target="_blank">📅 13:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر نفت: بیش از ۵۵۰ اصابت به جزیره خارک داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145543" target="_blank">📅 12:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
الجزیره: ایران فهرست سیاه خود را برای کشتی‌ها به بیش از ۵۰ مورد به‌روزرسانی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145542" target="_blank">📅 12:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
تسنیم: تا زمانی که تحریم آمریکا لغو نشود و معافیت نفتی برقرار نشود، تنگه هرمز بازگشایی نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145541" target="_blank">📅 12:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
حاجی بابایی، نایب رئیس مجلس: در مقابل بمباران اقتصادی آمریکا، باید منافع اقتصادی این کشور در منطقه را هدف قرار دهیم و با اقدامات بازدارنده، محاصره را بشکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145540" target="_blank">📅 12:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145537">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRaqQXVIomTBJkAAfZD_32np1SpT6coXvIXFXOsidtzK7FPvhQNNMG2xa7ihAn9c3e7zIu7A3z63IJ7eiS-Vf5vn77yCpwGw6P2RmrOTYrxJMPCnzab7zeeGHTcjP-Fvh__OzQ_bwy7YS5Ah-d-KWtSm5rfCDfwVj1n_P9nSwBFKYxCq4ydY7btsogTP1i324At-JEpC8DkGJ9mBsy5Yg0iZ3P2Cd7K74G55lJ_tQYgsyz0d4huqAE9-FAszseKsiD9WRHdklJI83wnxh6DtKdfCFzUsT2EZxHSxbbxBl3OaIprFX73VW-FCCrhcbLYcm826VmRzMWA4WKhsjm4uoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC2NLZZI5IyD11EeIZzvxb8ruE6jooghSXRKaejKS4oyBfX0Eb806R4U6B0qHy9xzV0DwEmw_hWoXaZ3H3yiF4PcJ9soe3dqg6EmJbQrZ4jbBjNDJQGsakfcQJkqeSyt9MTbb3m-LQJayi9qBZuv4o0O4yDS0UQbR09bpByGRPRz17pk58V9a2fmK3G6Oho2mdcxLToZlHIPnS7rCCFRKVj0D_VMusqdOjeglwS9sPmZi5aRzjSXMtnKB8T9A_Y8Por12VHl1TqmV_rCQJdCOrOUbbEqktc14k2vVGL8_TZuvZynY9rd7iKMT5PFua0xEk-IMmO0yjRxWNCaPje8xw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48943dcb4.mp4?token=vOuhAkbsUVMrBzLGi6Y-HFHoydabFpzTmPGS3f7M0fHPNabnPRQSeBI99l3IZFx5padULNTRVEBuV0yGj1JfUgPLHjA9-zXzPjiIlkRJVQEHwMhTwePZoh5BrYbx8Vl7BpJZDONr84d_sxHRQznas1XnF1UJNeiMj6WIyyUgf06CP4pn1AmTIaH5TXV-W5nPIQRDO17MYB8Eu02-aAs4-8Co8pyDjZ2U4UCn1UiScjH-sr_IwCiUKaTUwF5mJ-BB0kmGXfzIELP-c2VbID43RlD2p1ENz5uXlUzvQMYxUgBDuuwuU1Tk6R0pedMguoT_U39NC-A2IwJ5MeLP_Y9nqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48943dcb4.mp4?token=vOuhAkbsUVMrBzLGi6Y-HFHoydabFpzTmPGS3f7M0fHPNabnPRQSeBI99l3IZFx5padULNTRVEBuV0yGj1JfUgPLHjA9-zXzPjiIlkRJVQEHwMhTwePZoh5BrYbx8Vl7BpJZDONr84d_sxHRQznas1XnF1UJNeiMj6WIyyUgf06CP4pn1AmTIaH5TXV-W5nPIQRDO17MYB8Eu02-aAs4-8Co8pyDjZ2U4UCn1UiScjH-sr_IwCiUKaTUwF5mJ-BB0kmGXfzIELP-c2VbID43RlD2p1ENz5uXlUzvQMYxUgBDuuwuU1Tk6R0pedMguoT_U39NC-A2IwJ5MeLP_Y9nqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای شرکت ایندی‌گو که از نَوی مومبای عازم سرینگر بود، صبح جمعه هنگام پارک در فرودگاه بین‌المللی سرینگر با تیرک سامانه هدایت پارک هواپیما برخورد کرد.
🔴
پرواز ۶E ۲۲۵ حدود ساعت ۹:۰۲ در حال ورود به جایگاه شماره ۶ بود که با این تیرک تماس پیدا کرد و هواپیما دچار آسیب شد. با این حال، همه مسافران و خدمه سالم ماندند و بدون آسیب از هواپیما خارج شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145537" target="_blank">📅 12:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145536">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f37707ac0d.mp4?token=Sxjv67lVca594k5qozY4ZpkgZkZRsbKOFfrNF-jklH2BbxGA_tKyPQQUN6XBxr0CeJ61cxueeLzNrQQiGAsSv8N2tFkDXShHIoxh9-5671_rwOGoFUa8qOSZV4gx0PXJxVV-2kp7eq7EbljJjhJymHY9w-DO27IKm4WDXj9i2ZCREeUOX0CYGO7kUK7aYLiixLSG8StD81xa_FmuKCiVC2MDxjf936rKoYwUTJAtakj74QgqXUs-26b9uEKyY2yIZ31fYsUhuW4spRK7cXv6kJ1UGxxzrh9sfotShXyAS25HezAQusYMnMA6AIMcts5XNjQZA8T5S_zoOaEf55cekA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f37707ac0d.mp4?token=Sxjv67lVca594k5qozY4ZpkgZkZRsbKOFfrNF-jklH2BbxGA_tKyPQQUN6XBxr0CeJ61cxueeLzNrQQiGAsSv8N2tFkDXShHIoxh9-5671_rwOGoFUa8qOSZV4gx0PXJxVV-2kp7eq7EbljJjhJymHY9w-DO27IKm4WDXj9i2ZCREeUOX0CYGO7kUK7aYLiixLSG8StD81xa_FmuKCiVC2MDxjf936rKoYwUTJAtakj74QgqXUs-26b9uEKyY2yIZ31fYsUhuW4spRK7cXv6kJ1UGxxzrh9sfotShXyAS25HezAQusYMnMA6AIMcts5XNjQZA8T5S_zoOaEf55cekA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو ویدیویی با هوش مصنوعی منتشر کرده که در آن شهردار نیویورک، زوران مامدانی، رئیس‌جمهور ترکیه، اردوغان، مجتبی خامنه‌ای از ایران و رئیس‌جمهور فلسطین، محمود عباس، در یک تماس گروهی حضور دارند و درباره اینکه چقدر می‌خواهند نتانیاهو شکست بخورد صحبت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145536" target="_blank">📅 12:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145535">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی ارتش: دشمن بازم تو دستیابی به اهداف خودش در حمله به ایران ناکام موند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/145535" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145534">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
روزنامه عبری یدیعوت اخرونوت : اسرائیل درباره ایران آمادگی ویژه‌ای انجام نداده؛ وزیر جنگ اسرائیل با اظهارات خود قصد دارد توجه‌ها را جلب کرده و در صدر اخبار قرار بگیرد. ایران منافع واقعی در وارد کردن اسرائیل به جنگ ندارد و ترامپ نیز نمی‌خواهد اسرائیل وارد درگیری شود. برآورد ارتش اسرائیل این است که ایران قصد عملی برای اقدام ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145534" target="_blank">📅 12:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145533">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فایننشال‌تایمز تایمز از تلاش میانجیگران عمانی و قطری برای تدوین چارچوبی جدید برای مذاکرات میان ایران و امریکا با هدف مدیریت بحران میان دو کشور خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/145533" target="_blank">📅 12:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145532">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJAS_rb4ydb_8I5uSZSruUpmPzcrKBtlNYp9xbD40Go0JNHtnMSmPEi5CmFkDOsGduUxAKLwACSbLciuWQ72GFrPwsJzwOO--qmYk83GLtPO9QnALKYOc66ULIdAiAS49SMTWPsIvooCovo7yrfrvbjW3CoMfHtn5j9Po7P8G0rFWXzF90w_-3nTfOYc4xuza_NdrXKPG63mNiklSYjAXidQU1Id--PowCw5_aiOORB9K1SObcE5sciHlchw0jljzQaqK7TaxI-ckcVXax1AzKq6Q7hqJrp5wZvJXS9kRCrn1ZhjjWyyTAJMVFp7efHp2T2xdjNUPkVzfwODiVXmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : به نظر وزیر خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔴
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته‌شدن ایرانیان بی‌گناه انجامید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145532" target="_blank">📅 11:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145531">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvMcT3OYN-R2U9juM-iJwHRUqj7Rjlib134uoIszKCAjfZ8fhEUp1HNk1KhNNv2PLxLKOmOUoeNYAMoLIJhVcQ06ueTKq2A6-tT74o06FCzODG4_8u8a9N3oiNfW4RbF1k-y_P4MnNqb-ieCTN4R9dHWqNat6UOEziBrQtFDmUPri8P7SRT2f_r0KjadD24u4fRG-Tf7K90pS8XfQz0Lf1AtuXrpf6iGQMsyxlaxOFq_7VULXwqVzK3B6-uDCZ7y0LnbzzsG08qFdJkP7Pf5l9iMc9DtIUmC7igKsJQQi5uaq3xrQ6o4pUeLVsiHiB01Ot_-JAkkV7QDgv5-AjhNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دستیار قالیباف: اصحاب ناراه‌حل برای فرار از پاسخگویی به تفاهمنامه حمله می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/145531" target="_blank">📅 11:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145530">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مسکو: یک کشتی حامل تسلیحات غربی، یک تأسیسات انتقال سوخت در بندر چورنومورسک و یک کشتی در بندر یوژنی اوکراین را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/145530" target="_blank">📅 11:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پنتاگون: حملات ایران ادامه دارد، اما «خشم حماسی» به پایان رسیده است
🔴
یک ایمیل نیروی هوایی در ماه آگوست به پرسنل دستور داد که از به کار بردن عبارت «عملیات خشم حماسی» برای توصیف فعالیت‌های نظامی جاری آمریکا علیه ایران خودداری کنند. این موضوع سوالاتی را درباره این که واشنگتن چگونه به طور رسمی این عملیات مداوم را طبقه‌بندی می‌کند، ایجاد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145529" target="_blank">📅 11:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pu58nsII2V_Iget6JhHYrPnu3FbEZCSermBIuR68p4_8_uj77tEKqdSb-pd1LbVzHtakCJi4ImS-rlyMMWShAa8_UYL2K4GDvP0Rr87Bfb9L7I1NlZ640hS0q6OeyyKU3Mx6_vWi6fqx4cdP1kojfGZ64NLzT3ML4l8JO7eiCCYy89qeA1ExxLwvtz7ACSkG7P4fnVgh2Cuzl7n1S1pP1exL5Q2CXkWpwc344zcfjgQt9F_e9aqCj5kXZjJ-xRuvsRoUYjNn1fFqGHVGBzqr0cyM4ViKVikPS0VsJN72CyDR489n5O4FD_tEIGZSQX69lDE5_t2Fd64ahqsPLY8t4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت در آستانه 96 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145528" target="_blank">📅 11:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
خاویر میلی: جزایر فالکلند متعلق به آرژانتین است
🔴
اجازه دادن به اجرای پروژه نفتی، انگیزه‌ای برای دولت بریتانیا جهت تعمیق اشغال این جزایر ایجاد خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/145527" target="_blank">📅 11:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
صندوق بین‌المللی پول: اقتصاد امارات وارد مرحله خطر و کسری تجاری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145526" target="_blank">📅 11:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/الجزیره به نقل از وزیر دفاع اسرائیل: کنترل ارتفاعات علی‌الطاهر به معنای تکمیل نهایی منطقه امنیتی در جنوب لبنان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/145525" target="_blank">📅 11:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: مدارس حتی در شدیدترین شرایط حضوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145524" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
مرز، صدراعظم آلمان: ما با یک اختلاف تجاری با آمریکایی‌ها و عدم تعادل‌های قابل توجهی با جمهوری خلق چین مواجه هستیم.
🔴
اگر می‌خواهیم پای خودمان بایستیم، از جمله از نظر فناوری، تنها یک راه وجود دارد: با هم در اروپا و با مدرن‌ترین فناوری‌ها.
🔴
هر کس که مانند حزب AfD بخواهد از بازار واحد خارج شود، از شنگن خارج شود و از اتحادیه اروپا خارج شود، در اصل پروژه‌هایی مانند آنچه اینجا در حال ساخت است را زیر سؤال می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145523" target="_blank">📅 11:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=NJZnvI33K_DiNSdLog5JX1wDftoKwIu_gXo_gDdKJlF9_MBq0fPKtSJW_h3fnp3tDhTxz7U7QvgWiZ5LHwiE67e8qvlDzX_4Ot5EOt-Onq3hYEzgHJGg6lsuLBNszqMavpQl5Yw7gqtsRqbbrYIDE5PIeSYKkbsexNI4XSuM8M9RBzpMDbaqu_RwSPGusRnmNqLbUtrA7nq_8QYCc7_GO5lcsyRMIQjZ_ZgCgkyYCSluzNXGP0eFcPTnuo0P3pIyeFMMI7y_RbB0MBLZ8jLOeDQbhZZf-1zG1ovmB4hL5J98HDuBWmKuMoDP4yt0BT0uQwqiMJ1VfRegwr92uZLUaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=NJZnvI33K_DiNSdLog5JX1wDftoKwIu_gXo_gDdKJlF9_MBq0fPKtSJW_h3fnp3tDhTxz7U7QvgWiZ5LHwiE67e8qvlDzX_4Ot5EOt-Onq3hYEzgHJGg6lsuLBNszqMavpQl5Yw7gqtsRqbbrYIDE5PIeSYKkbsexNI4XSuM8M9RBzpMDbaqu_RwSPGusRnmNqLbUtrA7nq_8QYCc7_GO5lcsyRMIQjZ_ZgCgkyYCSluzNXGP0eFcPTnuo0P3pIyeFMMI7y_RbB0MBLZ8jLOeDQbhZZf-1zG1ovmB4hL5J98HDuBWmKuMoDP4yt0BT0uQwqiMJ1VfRegwr92uZLUaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 23,700,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145522" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
منابع خبری گزارش دادند که بر اثر سقوط یک فروند هواپیمای کوچک در منطقه «هیلزبورو» در ایالت فلوریدای آمریکا، دو نفر جان خود را از دست داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145521" target="_blank">📅 10:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145520">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مسکو: همکاری با ما به پکن کمک کرد از بحران انرژی ناشی از بسته شدن هرمز عبور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145520" target="_blank">📅 10:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
حادثه امنیتی در دریای سیاه
‏
🔴
وزارت دفاع روسیه اعلام کرد که یک کشتی باری را در دریای سیاه هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/145519" target="_blank">📅 10:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کارشناس صداسیما: درسته حزب الله شکست خورد و اسرائیل خیلی از مناطق رو اشغال کرده اما حزب الله در اصل پیروز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145518" target="_blank">📅 10:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145517">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم‌الانبیا: به‌زودی دشمن رو در میدان غافلگیر میکنیم.
🔴
رفتارهایی با دشمن خواهیم داشت که کاملا گیج، مبهوت و شگفت‌زده خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/145517" target="_blank">📅 10:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145516">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پوتین: روسیه در رتبه نخست تأمین نفت و گاز چین قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145516" target="_blank">📅 10:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145515">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d55fc1fc.mp4?token=s1-B1hAUyP3I6ZgJHIwzG8s2NqXPrzBu2W99dQ9VGl5Nu1cK0_x5mP-bP_P_XanSbOayjvUdW7UcD23ATDgISS2WMFtuzvl2XPh1I96D4U-AdPER-KBMVzG2J41TEycgivemhdCecg6l-9AqVBkhky4tCQyePtuSx5Fy9KizcimN2GnPzpv8Bf4P6DxMajYALXj8LZ0cyxGOGLoBpl_W3SMezUBdRfgdTRr_tbbhg1dnTupHulP0cNJjKDtDlsqHgsCfHAy1YQZp5hfwl1wVQiB-hYO5EBDvAPltUA2DUNydtoieSgo2RcK_4-T0qZhf4zbLFcGthHgzCL6GnRPXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d55fc1fc.mp4?token=s1-B1hAUyP3I6ZgJHIwzG8s2NqXPrzBu2W99dQ9VGl5Nu1cK0_x5mP-bP_P_XanSbOayjvUdW7UcD23ATDgISS2WMFtuzvl2XPh1I96D4U-AdPER-KBMVzG2J41TEycgivemhdCecg6l-9AqVBkhky4tCQyePtuSx5Fy9KizcimN2GnPzpv8Bf4P6DxMajYALXj8LZ0cyxGOGLoBpl_W3SMezUBdRfgdTRr_tbbhg1dnTupHulP0cNJjKDtDlsqHgsCfHAy1YQZp5hfwl1wVQiB-hYO5EBDvAPltUA2DUNydtoieSgo2RcK_4-T0qZhf4zbLFcGthHgzCL6GnRPXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم زیر فشار اقتصادی اما زن سوم عراقچی و سایر دیپلمات‌ها در به در دنبال خرید طلای لوکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145515" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145514">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK0VAY99hUliGE2xTqYcudPw4UafXS9IwtKj31aAjxwpUkyuxmoDn5O-aFKLptkF2hlgrEwa5QSVq44wW5ZxoBDVMAuKPUe_QEfKQHt9ffvNUIMRYqCGaBUs86KSYB6_gfyOaPo5h3DyYrWbJlLhgBNhV970mBzij79c6kGCeMvUAzpDFhDf9V2PXvJ0Ut9MqlPdXjTbDfSZapRamM0CIE9dUXnuHP2fVD_YIs21ZWeQ5EiQqUIDZvFl8B1GcZJMtWI0E64UT2aZ3EH_ptwalgDE1mRxinupPricG8Y92k3R2H1TNGXHRIlwaZupybKgWue048Ue1ZavIscjpnR6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه فاکس نیوز اعلام کرد که این احتمال وجود دارد که جنگ ایران تا سال آینده (۲۰۲۷ میلادی) ادامه یابد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/145514" target="_blank">📅 10:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145513">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0G-8JQRZc3kkyymRWAAJ2S3UyQG5H2S8roeeOqZGqMn2yFvRp79rYs8pwYndp03x-5Bc1vgHrKpB1WO_0wgGKZRd00BDInpTQo6qInq8scbkIWlZr5qR_mZAT1ozQmcoWMrp_doz2PtwH3laj7ZjlLuL3z37cVjr0My8EGGrNyajK5sZ07xRVAI92T-doj1RNxdTBlbRYMgpKPpNk3-ew3a2vDFtPiAABuVkmMtncn-QGKtQBdJRehO9XQnhEkKRRNLGDEYidfAGSGOFry5HhnoPFFLR016xsIqvud8aN6q9peweE9Adsil38VppBC_nZoBZ9HS5SH36k_LWA3eLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور اقتصادی قالیباف طی توییتی درخواست افزایش نرخ بنزین را کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145513" target="_blank">📅 10:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd9d65c4d.mp4?token=goalfpN9ojjx8arAyAqkUeaNKdkJK6CmcPv140NrPah-9JcRpALrPeTzySuGzwxoTLTJn93Wi8BtG-BEv32X7mHArQwRvSIwKm0OaFPyJRPqEsOJXXvZ8jrUInAoSY3obADdH5urmY9VIWmpLBhpl4fKncZID68W1SZise5-OcN4wWMr-SenADo-3QUXck0swgZbRjZZ6hDRwbG6IXgJ9SsTTGzSrFtfXfkHE-ASPTXdE1SvOg10sMgk_cQho6GnXIgH4Wobyh9Vk6ereBrBdSKBOWxhrxsanIEkoU9tcv_JHkXf2uL-S8L-dboAmJyfnvm8i4x5Dn7Yfqq0P6vKUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd9d65c4d.mp4?token=goalfpN9ojjx8arAyAqkUeaNKdkJK6CmcPv140NrPah-9JcRpALrPeTzySuGzwxoTLTJn93Wi8BtG-BEv32X7mHArQwRvSIwKm0OaFPyJRPqEsOJXXvZ8jrUInAoSY3obADdH5urmY9VIWmpLBhpl4fKncZID68W1SZise5-OcN4wWMr-SenADo-3QUXck0swgZbRjZZ6hDRwbG6IXgJ9SsTTGzSrFtfXfkHE-ASPTXdE1SvOg10sMgk_cQho6GnXIgH4Wobyh9Vk6ereBrBdSKBOWxhrxsanIEkoU9tcv_JHkXf2uL-S8L-dboAmJyfnvm8i4x5Dn7Yfqq0P6vKUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل عملیات جستجو و تیراندازی توپخانه‌ای مداوم در حومه زوطر شرقی به سمت مایفدون در جنوب لبنان را انجام می‌دهد.
🔴
شلیک مداوم توپخانه منجر به آتش‌سوزی در مناطق هدف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145511" target="_blank">📅 10:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b608c09a87.mp4?token=F-eMkwn1Kx4hnNXmwATypwsJfqAWIk4u4R40l0NFbOrRCmqyooScLwth6l11Zc8FnSFjmqq81gDp7d1UOa39wQIMGSi8I_6-KfFFCTdjMuwfz5ynVGuLDEDMR5paBVfgnAN8Al4xlQyKEqpk580QUl7X1NG6Kj0KZhFTTlG0Mzbc7WiCCoqZRfdJNRL2IaHohmsWaY9A2mC-EWmhGQ_H1A8q203NGT8lkCTSOKipmNE3xcbt5AvGyOvFVLZ5iAosa3KlF1Dvh_GnQEsH_dRiYtQAm3DNXMIhz9qG5do2cdzSGR2AzhsVoBcps05Wp6c58TcsKjnnsODZE5skceTXjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b608c09a87.mp4?token=F-eMkwn1Kx4hnNXmwATypwsJfqAWIk4u4R40l0NFbOrRCmqyooScLwth6l11Zc8FnSFjmqq81gDp7d1UOa39wQIMGSi8I_6-KfFFCTdjMuwfz5ynVGuLDEDMR5paBVfgnAN8Al4xlQyKEqpk580QUl7X1NG6Kj0KZhFTTlG0Mzbc7WiCCoqZRfdJNRL2IaHohmsWaY9A2mC-EWmhGQ_H1A8q203NGT8lkCTSOKipmNE3xcbt5AvGyOvFVLZ5iAosa3KlF1Dvh_GnQEsH_dRiYtQAm3DNXMIhz9qG5do2cdzSGR2AzhsVoBcps05Wp6c58TcsKjnnsODZE5skceTXjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل به زوطر شرقی در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/145509" target="_blank">📅 10:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کره جنوبی: تصمیمی برای اعزام نیرو به هرمز گرفته نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/145508" target="_blank">📅 10:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یدیعوت آحرونوت به نقل از یک منبع مطلع: اسرائیل درباره ایران آمادگی ویژه‌ای انجام نداده؛ وزیر جنگ اسرائیل با اظهارات خود قصد دارد توجه‌ها را جلب کرده و در صدر اخبار قرار بگیرد
🔴
تهران منافع واقعی در وارد کردن اسرائیل به جنگ ندارد و ترامپ نیز نمی‌خواهد اسرائیل وارد درگیری شود
🔴
برآورد ارتش اسرائیل این است که ایران قصد عملی برای اقدام ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145507" target="_blank">📅 09:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از منابع دیپلماتیک:
میانجی‌ها در حال تلاش برای تدوین چارچوبی برای مذاکرات میان تهران و واشنگتن درباره یک توافق جدید احتمالی هستند
🔴
دولت ترامپ به دنبال توافقی جامع‌تر با ایران است که موضوع تنگه هرمز و پرونده هسته‌ای را نیز دربر بگیرد
🔴
واشنگتن به میانجی‌ها اعلام کرده که خواهان باز ماندن تنگه هرمز، صرف‌نظر از توافق احتمالی میان تهران و مسقط است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/145506" target="_blank">📅 09:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f448c460a3.mp4?token=q24q5RSNHHxB436w58Az532ifhNmfKnI5ADInj-TJwT5yce2fCN2e8pkAfh3oc0Zc0mWaT_FJrmmTnmNZp3ixt69fq07qQy1Ie3JET8R2fsQGK62g1629TQI_N8NJBmqIYxqmY0gbODEbT99OSYNHQaF9RDdyjJTW8_2zK770jGqVLG2w8WJsJxLeQNe6jWIKnBuH7O3zxTFGJSqzfC5GclEGavAU3F5ahXF9Lvwiu0RMGqmMJETYaTMY8zUKVtCRIJJwj-icNF_kx1iozgoKAsyuUa2eeXfCz-QXlqM5N59xTrKpwVkl18lCeNElFeWL7x2WAnIS1T-rG28iMzgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f448c460a3.mp4?token=q24q5RSNHHxB436w58Az532ifhNmfKnI5ADInj-TJwT5yce2fCN2e8pkAfh3oc0Zc0mWaT_FJrmmTnmNZp3ixt69fq07qQy1Ie3JET8R2fsQGK62g1629TQI_N8NJBmqIYxqmY0gbODEbT99OSYNHQaF9RDdyjJTW8_2zK770jGqVLG2w8WJsJxLeQNe6jWIKnBuH7O3zxTFGJSqzfC5GclEGavAU3F5ahXF9Lvwiu0RMGqmMJETYaTMY8zUKVtCRIJJwj-icNF_kx1iozgoKAsyuUa2eeXfCz-QXlqM5N59xTrKpwVkl18lCeNElFeWL7x2WAnIS1T-rG28iMzgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی نیروهای روسیه به یک مجتمع انبار در روستای پوغربی در منطقه بروواریِ استان کی‌یف، باعث انفجاری شدید و آتش‌سوزی گسترده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/145505" target="_blank">📅 09:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
هواشناسی: سامانه بارشی یکشنبه وارد کشور می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/145504" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرگزاری صداوسیما: ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید مقامات لبنانی نرسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/145503" target="_blank">📅 09:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV7CpLnaMklEv-okCV1C23-w8mqWMeZXyMx6NuBW6dUSh5DF6IlVUF_jdc5Hs3l4I8Ulzz0sWpemsRjfZ9kPCMdiYTLvSwhUyE-pETY84RvLlef--mxLRtVBZ6qliRU-jucafm85RIXyizLO-okowikQ3VVElyVD-tHJfitZ3zNPxphnxsp8kYBEKsKlozIP8mOLQBhmMHgG6L0QpJDd_J_OsZye99QTd9V5_CXmsfL9C6QxnKRHGvuYhKW0WqPUpGw3vMSxTIJ1-57o0n5n4KDjkwqoJ90VqoyYygFPNnUimxritcggufpP2wVh03B7Rdz3ocyWle5nzc2BnXFhgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: آمریکا در حال بررسی حمله‌ای در ایران است که ممکن است به یک مراسم عروسی اصابت کرده باشد
🔴
مقام‌های آمریکایی می‌گویند این حادثه در دست بررسی است، اما ارتش آمریکا هنوز تأیید نکرده که این حمله توسط نیروهای آمریکایی انجام شده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/145502" target="_blank">📅 09:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر خزانه‌داری ایالات متحده: اتحادیه اروپا رسماً به تحریم‌های اقتصادی علیه ایران پیوست و ما از این موضع قاطع و به‌موقع او قدردانی می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/145501" target="_blank">📅 09:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145500">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ونس: احتمالا به شکل مخفیانه عملیات‌های خرابکارانه در ایران انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/145500" target="_blank">📅 09:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145499">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
الحدث: تنها ۴ نفتکش روز پنجشنبه از تنگه هرمز عبور کردند.
🔴
داده‌های کشتیرانی از کاهش مستمر تردد نفتکش‌ها در هرمز طی ۱۰ روز گذشته خبر می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/145499" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj7RKrzEizMBZR57Ot8RnuDSK9_Z8WMwSS1OTmjKH8Nxw8S4oLGbKox9atfr333IefVWczYynxnE2knDFvLLBkR3EnKyVYlMnaqzZRSTwMA6ZgPUNFxHqAwXkYnj5r9wGhBeZbxjhkanoAseOYqe3ojBbCc9lvffHPlKOwh8XUBLXTmXUgYLJdEClqTOPCk-B3gz0XdmxMU7Q53WOwipU8Vt420yHSXToy9xEXsXwr-Rzp_oH5pjlfCyL4A_Dv31E7U4ZXHQinzeu5vKbcL_fxIfB_91CqaBDrtbl5CJ_cglEIeIkE5BgqN_CQeMfvep31PL-8WN2QDkJ18TM7KA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق جدیدترین تحقیقات نسل Z (متولدین دهه ۷۰ و ۸۰) تنهاترین نسل ایران هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/145497" target="_blank">📅 08:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پاکسازی شهر موشکی حرب الله . خنثی سازی تمامی عملیات های الکترونیک و سایبری توسط ارتش دفاعی اسراییل در رشته کوه علی طاهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/145496" target="_blank">📅 02:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3cfabd42.mp4?token=uJSj_Nfdqyl8_JJjHaMNVYM7ULDbpyzODoX2Qo24B4EshQ3zsxReNETt_VN0zbcDtjdxBna-oS6_fDhZGRsKbzr_Cy0iuPsmeNPbsYBiY-0qJzNpON4XQiThbfc88_vPPHW8_mhB3l3kJCVWf56pvVGtN1Hczkw7BBAcxGmWnaHmNJbu0fjMmtjE_9mYefIrkfkatmVrsFiHMN8FrjEIpBnmpFek_l6Cdik_EkeCpBm4BECxIYZQXGzuWxDZJqimZDkk1KUtwmixZAjFQVF2FFmpZMlc1rLH0hwi_V63tkvcwN21Fo8irAgO-v2AtaG2rB7nsW0oUkpMDOWfC-eiuQlpyc6tDWo3d4gJEDWihasF9k9EyoR6ZCRsXzmZG3T9xA9sRsrzGUPJDKdqeobcGEpJqMV6ti-7NgWLNb4c7J5Cojj_82d5YmRt5HG0rmyDNaF_kuZtEyMSeE-LsB0XUIkJIkCHjFVb2I0dUoRg6lQM_bIn8PugHX_jKHCIfgJ5YYTkmXRQqF5nrem0EZgWndPGEOAEt64JcVLowgNxInh7bvdEgSd_8bnRia2hpGjp-m2UQeQ2ZOH2VGhYRYo1VxQ65oZ9Zyeo3-RshtCQ4SNZyZuRLWACWbDc93S83z8aDVzzCcspWyAs2hkBBnUroisdJxlVmus3-Xly3bg7KYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3cfabd42.mp4?token=uJSj_Nfdqyl8_JJjHaMNVYM7ULDbpyzODoX2Qo24B4EshQ3zsxReNETt_VN0zbcDtjdxBna-oS6_fDhZGRsKbzr_Cy0iuPsmeNPbsYBiY-0qJzNpON4XQiThbfc88_vPPHW8_mhB3l3kJCVWf56pvVGtN1Hczkw7BBAcxGmWnaHmNJbu0fjMmtjE_9mYefIrkfkatmVrsFiHMN8FrjEIpBnmpFek_l6Cdik_EkeCpBm4BECxIYZQXGzuWxDZJqimZDkk1KUtwmixZAjFQVF2FFmpZMlc1rLH0hwi_V63tkvcwN21Fo8irAgO-v2AtaG2rB7nsW0oUkpMDOWfC-eiuQlpyc6tDWo3d4gJEDWihasF9k9EyoR6ZCRsXzmZG3T9xA9sRsrzGUPJDKdqeobcGEpJqMV6ti-7NgWLNb4c7J5Cojj_82d5YmRt5HG0rmyDNaF_kuZtEyMSeE-LsB0XUIkJIkCHjFVb2I0dUoRg6lQM_bIn8PugHX_jKHCIfgJ5YYTkmXRQqF5nrem0EZgWndPGEOAEt64JcVLowgNxInh7bvdEgSd_8bnRia2hpGjp-m2UQeQ2ZOH2VGhYRYo1VxQ65oZ9Zyeo3-RshtCQ4SNZyZuRLWACWbDc93S83z8aDVzzCcspWyAs2hkBBnUroisdJxlVmus3-Xly3bg7KYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکسازی شهر موشکی حرب الله . خنثی سازی تمامی عملیات های الکترونیک و سایبری توسط ارتش دفاعی اسراییل در رشته کوه علی طاهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/145495" target="_blank">📅 02:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145494">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP2QtC3XvMAnvwev-3pjMtMb1iI9occa8m3UkyqpsnaMivLSfNZLZfumzorIXwSYqG3h-mJhgBIXN6wOodhgIcdea4L_ylnivR9NMzkeSUe6K2uvZASQMjdYUS32QRHSkNw6pcdfYdfdQxzJyQdZ_I8fl2gz2f9mp7_c-_mknFFttoenPk6CzPeMj1e-JWQIK9AlhX0v57XM1-FZtpvb3JfZdTONV4DMgtyWdNpYkwkPOm0dWYiH1A6ww7XwOWo-z_dOMrVKii-7L7rBN9uHK23968s-FuIGfxbqo8W-UzRvgom8v5tpG6nBiiZCIaq1AR_rRG6NEo3tIUbZ3rmQHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تکرار مجدد داستانی مشابه داستان الهه حسین نژاد :
ملیکا ۲۲ سابه دانشجوی ترم آخر گرافیک بود و بعد از پایان کارش داشته برمیگشته خونه که متوجه رفتار عجیب راننده میشه .
همون لحظه لایو روکیشن برای دوستاش میفرسته ،
اما بلافاصله بعد از فرستادن لایو لوکیشن با راننده درگیر میشه و راننده اونو به قتل میرسونه و دو روز بعد جسدش توی یه کانال آب پیدانیشه
و طبق آخرین اخبار ، قاتلش هنوز دستگیر نشده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/145494" target="_blank">📅 02:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145493">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
قوه قضاییه: حکم اعدام رضا پهلوی صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/alonews/145493" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145492">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: اگه ایالات متحده همین امروز از جنگ علیه ایران خارج بشه بازسازی این کشور ۴۵ سال طول میکشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/145492" target="_blank">📅 00:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145491">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b9e7185b.mp4?token=WxqMFswM0r16DMxeQW_iZUrhI2EaJ5C38plzdUMU3oWhlE8WjtYsD3HzWRm3-zo_eqjQa_3kjPFyYotVxvLBZIuALEu9TvaIih1bzvaOgBWnfRIyD-Eg7HcM2VGU46ODuk2VvzcNoExVq8yLs64l6zS1lkE7ANmLraqHWRRbjjI77K9vTEcIjA7-yFqJ7_QwR2DVKOo2iWlx_KSSfSqgKddmR41A4XPasSBVsU9FgYSA5HS_Zcy8KSxMsSElDJN53VingrV3UYu-gOxnYgQFlWkOmigYz9tA9rVBW0glc0AuZQAgOnkNRhaa64JmN2Vq-HnO-0_NQ09f65mkACCUmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b9e7185b.mp4?token=WxqMFswM0r16DMxeQW_iZUrhI2EaJ5C38plzdUMU3oWhlE8WjtYsD3HzWRm3-zo_eqjQa_3kjPFyYotVxvLBZIuALEu9TvaIih1bzvaOgBWnfRIyD-Eg7HcM2VGU46ODuk2VvzcNoExVq8yLs64l6zS1lkE7ANmLraqHWRRbjjI77K9vTEcIjA7-yFqJ7_QwR2DVKOo2iWlx_KSSfSqgKddmR41A4XPasSBVsU9FgYSA5HS_Zcy8KSxMsSElDJN53VingrV3UYu-gOxnYgQFlWkOmigYz9tA9rVBW0glc0AuZQAgOnkNRhaa64JmN2Vq-HnO-0_NQ09f65mkACCUmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «من انگلیس را از تهدید ایران نجات می‌دهم. اگر ایران سلاح هسته‌ای داشته باشد، احتمال استفاده از آن در اروپا بیشتر از آمریکا خواهد بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/145491" target="_blank">📅 00:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hxn--2YkfYcCKYjUywpM8VN5530KTx3l8kxb-20GcYaKnRGLSgXkCTLPmy13wjzDR6eQh52026ccpX7szW28q5rerxg55evz7QfO833i-9c3Y_qhUX49lw1rcACe1_1FxV5N_nYjEjs7FsgTMHEamzv9a7dIPIUsDMy9o0IXCoXpueZcNVn9oTDbHGAvQdtA-H4thDWTzTqSrQKWz3A2oGEVidtm-gn9bLohVzubrLoSn68purSQQmgnSh8qcRnhcCTGbO3WVavbInxodO1LGmp6knKoAU-mcogGslGAHNIkyY_h2NJRW8aonu_4UnzGMGWrTT_HHPhmCuz0fbiNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzsFEo5ooNoQwrzGTudpD0OK4yuAYQrGyC12fWu8Vpxy-mmPrsbxrEWSH1IhQkXX1C5MfOqOTw3IFAHXaF9fDty6A57ikIXRPrvxIbm2b_nnrwkAw1raa96MSHXolOuhwWuSvqwSUi-PJxzQglVhPhDx0DAMt59QnEIhnSqwVmN-D1WyMfsnRxlwHpwXqOdyWQC-iqit1dzMmQbaACZTEpb-Qc09JEXydKUfXC5OQCpMMfr1foGhcB-mG0V9yNDHAB_5v4wpEYJAY52gWN7xU_094GiYKQRY0QwSNEMQ2gbQtHTRPxjREx9oo-kQWmdUqKFj41p2XAddkDg4q6sxEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی نفت‌کش "میرکان" متعلق به ترکیه، از تنگه هرمز عبور کرد و از مسیری استفاده نمود که توسط ایران تعیین شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/145489" target="_blank">📅 00:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYBkJkgpXUvvDlAr83w8E_qbOKMLddiEoWNCEvJunrWMy_AiSWldLVOUub3WLZ40li-OL1DvYYoGPT_K4j8_BW9L88IakAPg3edTINWs8OwwEc8UFYj6LbvSuzYiuCyq9awsOWrV_vaIxjO_s541abeXOOmgneRyJLBvezPYfcIb7xT-MAdHUqSQ_1tsYFX-noL3xiv98kto3KtD8TG4tb57vVLvOiMY1q7SIcTX09ieU3To5qo7x0PMK2ag47XaoqGAhjYBsQHO1V7Oo5-erihkQyOzc2m-8YDrgBitbDmu8lhYG5dG-dUoppHPLadF3KF7RYtCrIVt8ZHuN4-B9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی:  احتمالا هماهنگی جدیدی میان نتانیاهو و ترامپ شکل گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/145488" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HnBH0tCKSSuXQnMoRO0ZOKhYYME01_2C5rJ9LBQlp0dKGar9QOv1bVTunLAgDnTVyosdP-UtWT69eGgbplccC_wkbtlj7JxDAq03UhaoKnA2ndzreGDXW_Pk75Ig194oLk1_RSBahe2vagDT_vWVpl0MW7qeFkulYR91rMVDhmYIHA2RZdOl417vShdjhg8fBJcYDmiLsYdOMY4uwewE2ktxLtnPiVzP-S7xcpwy00xvEOb-iYaePNvuSlkh76h3g_axHRe93Mou1PV4iyENU9TGBd0_foyvxYzm6CnSxZ0-IGyr1Up5xdMlsyxDFakO72_ymQHTm7fruBXqdu_BwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دادگستری ایالات متحده آمریکا پاداشی تا سقف ۱۰ میلیون دلار برای اطلاعات مربوط به امیر یاریاب، رئیس فرماندهی سایبری نیروی دریایی سپاه ، تعیین کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/145487" target="_blank">📅 00:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
متکی: آمریکا طرح چهارده بندی را پذیرفت برای این که بنا نداشت بهش عمل کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/145486" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ES1YC_xbrex7_6qo8z62bNwSqmqPah-_ExaucXn_-NeyMIoA_0AtqBFD3yGm23jeh6gg76wrqo60qYHxV9-9rkM8ZLHNYl5-S1TTc0qqB5mVQHs9YYCJIbVn16nEXXBMfYhyZz7rnWYt0CswtoOAPWkKk5ujoV8ylugQ3SGGvae6e_zzX67DcLLZigZg_3VwL2bJvSFb2EE-ZxnO4ZT1z-1G7nvyZVnCSZAGVqTLgxSYvq92c8oRpwc4pSFzeJ246IDmU_1t0VDRRM166nWFY-0dfXy_UY67EOdpgPSaECWI10fwYrjg_GVrCNIgFXQk4VwDLwkIc7DtRrMww6-K8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقایی، سخنگوی وزارت امور خارجه ایران: دولت قطر، در یک سند رسمی که به اتحادیه بین‌المللی مخابرات (ITU) ارائه شده، تأیید کرده است که حملات دفاعی ایران علیه نیروهای آمریکایی مستقر در خاک قطر، "به تأسیسات نظامی آمریکا وارد شده است [...]. هیچ منطقه‌ای مسکونی هدف قرار نگرفته است."
🔴
تنها استثنایی که قطر مطرح کرده، حمله به یک تأسیسات گازی در تاریخ ۱۸ مارس است. با این حال، باید به یاد داشت که تأسیساتی که در آن روز مورد حمله قرار گرفتند، در خدمت تهاجم نظامی آمریکا علیه ایران بودند.
🔴
این موضوع، تضادی آشکار با سابقه طولانی ایالات متحده در حملات عمدی به اهداف غیرنظامی - مانند مدارس، بیمارستان‌ها، محله‌های مسکونی، مراسم عروسی، پل‌ها و غیره - دارد.
🔴
تفاوت بزرگی بین یک ملت متمدن که اهمیت پایبندی به اصول اخلاقی و انسانی را حتی در شرایط دشوارترین شرایط آموخته است، و حاکمان جنگ‌طلب که هیچ قانون یا اخلاقی را در اعمال قدرت خود رعایت نمی‌کنند، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/145485" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979fdd9589.mp4?token=ghIPgwq5f1FHjuxPKVtzs8SBpcVC9dXFxz3pJZ1v0yoxwvKnAbkNU5W2-PfxyhkV_AxxISRNAKs02J4IsBVzVgJlbI5ggyZJeOHGpqb5D_GLC1CAc_EPK3y5popBE80n51tlRhlYF6Cy12m8IEstTiO6ldnL4_2TZ5oCvi3DPURjkeFyJRb-V8sJLnJz7BUSolQ8Szh1ML2YtXhh7-hE5wnZvAPMwtz6I3IYuIfPc8Q7ecL9MGZMECWNxVAT-IzSSVbgbbrVG-1Q4BYtc62H3sawG52utzy-Jz9XNmACmC-HZoge7vil2qqSDMQgQe7pihqBle-pUwpxEvNofSwFIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979fdd9589.mp4?token=ghIPgwq5f1FHjuxPKVtzs8SBpcVC9dXFxz3pJZ1v0yoxwvKnAbkNU5W2-PfxyhkV_AxxISRNAKs02J4IsBVzVgJlbI5ggyZJeOHGpqb5D_GLC1CAc_EPK3y5popBE80n51tlRhlYF6Cy12m8IEstTiO6ldnL4_2TZ5oCvi3DPURjkeFyJRb-V8sJLnJz7BUSolQ8Szh1ML2YtXhh7-hE5wnZvAPMwtz6I3IYuIfPc8Q7ecL9MGZMECWNxVAT-IzSSVbgbbrVG-1Q4BYtc62H3sawG52utzy-Jz9XNmACmC-HZoge7vil2qqSDMQgQe7pihqBle-pUwpxEvNofSwFIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه رستوران اومده قیمت هارو به خاطر نوسانات قیمت به صورت لحظه ای تغییر میده و‌ تابلوی صرافی طور گذاشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/145484" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
تحلیل الجزیره: آمریکا نتوانسته توانمندی‌های نظامی ایران را از بین ببرد
🔴
در حال حاضر، هیچ‌ یک از دو طرف قصد تشدید تنش را ندارند
🔴
این خوش‌بینی وجود دارد که در آینده نزدیک شاهد تشدید عمده تنش‌ها نباشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/145483" target="_blank">📅 23:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل: عملیات پاکسازی دو تونل زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر در جنوب لبنان به پایان رسیده و اکنون در حال خنثی‌سازی این زیرساخت‌ها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/145482" target="_blank">📅 23:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد که نیروهای آمریکایی مسیر ۸۷ فروند کشتی تجاری را تغییر داده‌اند، ۳ فروند را غیرفعال کرده‌اند و ۲ فروند را بازرسی کرده‌اند تا از رعایت مقررات پس از تشدید محاصره بنادر ایران اطمینان حاصل کنند.
🔴
این تعداد شامل یک کشتی بیشتر است که از روز چهارشنبه تغییر مسیر داده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/145481" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گاردین: رئیس سیا در سفر به روسیه از مسکو خواسته حمایت خود از تهران را کاهش دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/145480" target="_blank">📅 23:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
‏ کانال ۱۴ اسرائیل مدعی شد
🔴
پاکستان و قطر طی دو هفته گذشته دو بار از ترامپ خواسته‌اند بخشی از دارایی‌های مسدودشده ایران را برای کمک به کاهش تنش آزاد کند، اما ترامپ هر دو درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/145479" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwo_uROwYe-M3LInc1p2ZItNhk3zf-8Aqx9_KY1brlM13C-TNbx0LvGMotAz6KAR7WyIZU-WGcYznaqee1wznlmO7Bl3x1XEthhzenBbTkMp18DMLXedpcP840gktldV5iM81pre5yr6siEix30UfER9rCr-GJsmYZoquGb3ySwI6-BVUqLeI6ndYxFQkyVFV6cWqGMcVS1TwmUb_sfZdIXPr5lDXdH-UiFhRPDk1onlcQTN6PvbkRuqFNA8sxoM_-h7A_z3CDfiaTUZ7We0qqpMZEJ2tHz5H4mpAX08QMXHJRxm7GXCM6BGfyg53uq3Z8X1Nz4KMsidbAVSAy51ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت نتانیاهو پس از خبر تسلط بر ارتفاعات علی‌الطاهر: با ما درگیر نشوید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/145478" target="_blank">📅 22:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJmhPGZ-Unukg7SKOfKAoenX6-M3G2uTcVehfSHcAcptzUDiX-BVqMxoc8Leg5Ujyy0nh_iHHOoRJQGHqPGkDQycvbSNXum0Nn-V-J5KkMYDO0DhcJmJmRIs84RF4QL_B8HjXWOVRMFk5FUaCoinPipSzjDKB-xtVnYSrlvXGcsnUUPRR5xHtg4xGxLcooz0Qj1secqAHrFZwkB6jg4TgNUXpgz8Rcr7yAGcOWAI3lBp6mmIgg2SueUS0uGJlhMvGqWkwtPAC5F4gPQkRUgFbD7gmoddBlDNCZd1nLYp5ZYk5dGIbyz2aCknXdhgyFvPe6znsJkOsemitNjwwWELKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به روستای المنصوری جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/145477" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq76cFrMHXTs8AvIiksFs9s1BH00qFfWNHIYUZO11vlIN8jyZd38qrN7ZEqJFvKel4fAVl0TiaDKiUfyWgwBrVWs2lQez3rukm1WllVdg8OZXg1uW5sCSYlcU3kACbZiaYGnIcXh-9WnTDitr6WpeVxvaY8y8xiG9BTUB_MQkxPkNe_Rr9hg0ny5IEOR_eT0xrE3a7E3fDFESGIxylvq3dG06YnBy0aYsB8B6KqJ0B9B5vrRm8oNuwR4PK2U-xUaLrQdbf9h1SCpI9ixuShZGqe4dJQa2bu3BiMs8kgDRJ59uYGLyRI8ABzP2eo49pl0aZwhLmV-M3hYBLvIXvmEpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه: امروز من نوه‌ای از راوول کاسترو به نام فیدل ارنستو کاسترو کالیس، بانک بیرونی کوبا (Banco Exterior de Cuba) و چهار نهاد دیگر را که بخشی از شبکه فاسد مالی و اطلاعاتی کاسترو هستند، مشخص کردم.
🔴
دونالد ترامپ و من در تعهد خود مبنی بر اینکه کوبا آزاد خواهد بود، سست‌ناپذیر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/145476" target="_blank">📅 22:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=nEcHC8kTir4GoAb48i6gUfa0xc89xvjf_6gGMGpE955ktxXMAHWx4iLUmRX9Y4CcArLAJCgS71p7mxycGz95yt1VDojPnSVvDTdYZSTFKtNn1bAW8pL0PX5JfHnPbYlevDuBsOzEVHnBW5mKDZdUEVLOviujQNGPtKOptXzZvpVdE_HSzwo1ogZLDJuH9HKVQpy_brsf_ciIpuNXlRm-jHjsVQDgi4pK8GDHHkzV464fWzveQSYG0VJ0ZU0spQdn2e03eMR2p7-L4A8FtSNA9aWhonoV6zJn2c5_4nptzyMNA78L9KLSm7eVcT-YCWrJgbCW3vv8OxGapUGE6nbbNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60eb3a2c.mp4?token=nEcHC8kTir4GoAb48i6gUfa0xc89xvjf_6gGMGpE955ktxXMAHWx4iLUmRX9Y4CcArLAJCgS71p7mxycGz95yt1VDojPnSVvDTdYZSTFKtNn1bAW8pL0PX5JfHnPbYlevDuBsOzEVHnBW5mKDZdUEVLOviujQNGPtKOptXzZvpVdE_HSzwo1ogZLDJuH9HKVQpy_brsf_ciIpuNXlRm-jHjsVQDgi4pK8GDHHkzV464fWzveQSYG0VJ0ZU0spQdn2e03eMR2p7-L4A8FtSNA9aWhonoV6zJn2c5_4nptzyMNA78L9KLSm7eVcT-YCWrJgbCW3vv8OxGapUGE6nbbNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر گرم طلای ۱۸عیار 23,600,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/145475" target="_blank">📅 22:35 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
