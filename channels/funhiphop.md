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
<img src="https://cdn4.telesco.pe/file/WxkMwH4Wynf7v8bfeNmKzh-p2fU2LJMO0ct9R-aLug8GfIBQajCrVzMtxyiME6yhEmpgpOmski340-P_nQetJvMODXO3WqDf7-rtys6-0zNnOYa1ydL0-K8adnd1luUIIl0v4qf_tckcFNPaCDomytjWzb1iAhWHI3jBfAReLUIsOoG43lFRI3paL5vptBTQcNN1HXeUnLnSKsZqu1K0tMdht9hFZCCDUd2L8JBd8MkhXvZmCub_iqrLqkPJDOKdgfhvxZCE6RP5SjwlXdGXinLt7-qGrOrSdD3q1-_JyUgEPoqemikohS9rJSSiKxg_QbMjGULPIZ-aEvf4ez9_Pw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1SETWi-_aUK7FoR2lWShapkQfcgOl_ii3E2vZl2ZwO2IBPU1W4EV4X6sl8JojyvKBcl9t6PJLwnkhPeAGV28OGXfG_95XIedjZo2ExeZADk44BH9BB9XeYiIR7tWaWcYhy2HPYg8BWmM0gIr52EzIuLJP6FSGap8BqB7TnaNMYhTEGg9ToLfFFauas2gZB9CP-RjtPfwT5uYJvoLVkkopibGS5XaBVdFNYZTaH7hIuluVoPvZDNlyrvhsS_Mzp31y81D4BVS4i0B3-QVmtvMlLF3QLtdssVT1uwvGFh_WuepDiGjLva1KFh_fEiKwsGtrSzAsbmJTVijXy5uE4PtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=vO5ULkzATK_5YjK-CZqsCjCtbYUBQpH8zE27N_vmUGX2zTSDHKFhJ8XkUyyKnjC5OmgnibYx0MZyty_bnXqFZyuwRAl2AWnRCCx1Pz68Hxdtc2MK466M7rjrfcpTm6QwYM5C-jA_K1R8rJ9BorqpI3gq9RLg46tdhRaBh8kjGGPOfycSDcoJmxLZi-lh3gtoR5v-C94RHtPFoWClJ0a0jZ9t8c1ynhVU_4NpkMcTLoVn16Ez49TmDIjaWlXvavYTEeMKjzvO2Bn_fQGPGgVK-T6YWsE9o0XMH1gwOELf0GExnxUGVWwZj8hIT1dPQA7CzZaJtIlO1lWgfuH3HJYbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=vO5ULkzATK_5YjK-CZqsCjCtbYUBQpH8zE27N_vmUGX2zTSDHKFhJ8XkUyyKnjC5OmgnibYx0MZyty_bnXqFZyuwRAl2AWnRCCx1Pz68Hxdtc2MK466M7rjrfcpTm6QwYM5C-jA_K1R8rJ9BorqpI3gq9RLg46tdhRaBh8kjGGPOfycSDcoJmxLZi-lh3gtoR5v-C94RHtPFoWClJ0a0jZ9t8c1ynhVU_4NpkMcTLoVn16Ez49TmDIjaWlXvavYTEeMKjzvO2Bn_fQGPGgVK-T6YWsE9o0XMH1gwOELf0GExnxUGVWwZj8hIT1dPQA7CzZaJtIlO1lWgfuH3HJYbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسمی شد بچه‌ها، آه از دل‌های شکسته و حسرت‌های ما
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/funhiphop/82971" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82970">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miYzaydBUFbJjNtdiHJNsrDhVeT8IwLcqhA1uIvt9wJLQn3GCw4wa3vKsW0bSDtCAzAmRWa_BxzE0p0xvAfMGIVTFVJcjGE99u2Q1hd9KQT4YpUBLCNJbPzaWI57-ZMODjxMYqhVoxLOUbpVOv7Ds2nhh101RPd2Tq1kXUNfN2bn4lAMzFIOu8Wqru4HhTPcsTA3aJkG58NJcfymcBDbQ7_l-0mhK7Q_M10iZ1Tc9-ZILg47XS7T5QV8mYmCfOEGn0dXw-HWK8497Cs8YSHizE0KdNdB6ec5NJVhmSi2gR_PqXqmdX_RPeSshzGuq44mKu9EIuAjGs7uQ1t76R3tZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته سوم لیگ برتر انگلیس
💯
⏩
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های نفس‌گیر هفته سوم لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/PL3
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/funhiphop/82970" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82967" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=uB4imfOkCIN_3qAOc7LUAgZ0zp-ysi_hL_eg-JPukrj5hF68ryEdlZhB-t8hWkO_J_ybnR8smEdusJGDjVgy2gj93CU4XW0g-ZMm0_a6waQAg_BWZWYHfGX995aHv-ZShKXKcFJD9cUS9B4djRFgvWh36PmwpFRieDORLStYs04AEspNmPmlD5B7Goo1DmjGIr91ljWZf-HO04DteGi9p6IV6yxao8MydJ_yW0rt2JBEN2ryheN8bS9HMQismcxvZk0RRgaK4YNNLBAu1tyd9gizwvgFCelAnu70y3r-D2TbngxctfrAnJ3KDEGtCNvvTwVL0ubxCoZMRcBe-2JU3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=uB4imfOkCIN_3qAOc7LUAgZ0zp-ysi_hL_eg-JPukrj5hF68ryEdlZhB-t8hWkO_J_ybnR8smEdusJGDjVgy2gj93CU4XW0g-ZMm0_a6waQAg_BWZWYHfGX995aHv-ZShKXKcFJD9cUS9B4djRFgvWh36PmwpFRieDORLStYs04AEspNmPmlD5B7Goo1DmjGIr91ljWZf-HO04DteGi9p6IV6yxao8MydJ_yW0rt2JBEN2ryheN8bS9HMQismcxvZk0RRgaK4YNNLBAu1tyd9gizwvgFCelAnu70y3r-D2TbngxctfrAnJ3KDEGtCNvvTwVL0ubxCoZMRcBe-2JU3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/82966" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=lXyi6Hv_MX1Bi-nTi1g44HQ2iUycqEC44klNkFsc4TBTYoAhDJgVt8VpLzWyNqpf4CAmV-Z_rpNqR3AZyKknET0w7OxN9L7zyr7DKPlbbkj-PvRb_iLVxuvBoI3MJs3V2SK6x0o6xwBgAlX3IRLz1dRfhKHtvUoB14qjUN8oQzfvZH8KKVid6N-_sHeoLR1MoZed2nz3oFhs-0gMO5rHzFYf6K3ys5u3vrg8e8kTwWZSv3_wEtDbtDFVFMvtYbPNKCEoNWcRLFCWdYZWCAHGNSDZXZc5eNvSgEwEgNoLrgv1D3DqCo4KvcfvsYwpVncldQqZ-hZEBA6WGk5yuwWMlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=lXyi6Hv_MX1Bi-nTi1g44HQ2iUycqEC44klNkFsc4TBTYoAhDJgVt8VpLzWyNqpf4CAmV-Z_rpNqR3AZyKknET0w7OxN9L7zyr7DKPlbbkj-PvRb_iLVxuvBoI3MJs3V2SK6x0o6xwBgAlX3IRLz1dRfhKHtvUoB14qjUN8oQzfvZH8KKVid6N-_sHeoLR1MoZed2nz3oFhs-0gMO5rHzFYf6K3ys5u3vrg8e8kTwWZSv3_wEtDbtDFVFMvtYbPNKCEoNWcRLFCWdYZWCAHGNSDZXZc5eNvSgEwEgNoLrgv1D3DqCo4KvcfvsYwpVncldQqZ-hZEBA6WGk5yuwWMlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از صفحه رسمی فدراسیون تکواندو ایران منتشر شده به مناسبت گرندپری کره جنوبی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82965" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🦁
سرعت و کیفیت را با قیمت مناسب تهیه کنید
🦁
💫
چرا دژنت وان ؟
⭐️
پشتیبانی قوی
⭐️
امکان خرید آنی در هر ساعت با سیستم تایید خودکار
⭐️
کیفیت در سرعت و پایداری
⭐️
قیمت مناسب + تست رایگان
⭐️
اتصال پایدار حتی در صورت قطعی اینترت                               …</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82964" target="_blank">📅 23:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM3ycYChQ1IGPkDIFDuE4FJpWW_akdTvkaerQyc8_NRmn2O6tbeXyOX-W9IKgfn4qqOoFpJyg3dfDvry1-SJQwJmcq59Q9q1fiR2-ICvDuKkljEAgig4ntl6n-ALcVeQhuqMok5wYxUGTOuratAdgD8fqL4wg1y_QXDy_Nm8F7WFX9sY7Hzmudg7LMTPwgvKEwzQKKVgW8YjN0WYli8j63w2Jg9Bgi_l1tDeGHazh_aSPt8iAlhW6UwM66JRJys0HPNuf0zv5mqFhl6X-WQ9zt9wlqvz29KXHfCb0zy52hJz83rSwVlWXeQ7jLjoBc4VXfza7epygzn6oqkKEvSFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
سرعت و کیفیت را با قیمت مناسب تهیه کنید
🦁
💫
چرا
دژنت وان
؟
⭐️
پشتیبانی قوی
⭐️
امکان خرید آنی در هر ساعت با سیستم تایید خودکار
⭐️
کیفیت در سرعت و پایداری
⭐️
قیمت مناسب + تست رایگان
⭐️
اتصال پایدار حتی در صورت قطعی اینترت
◀
️
ربات
🤖
|
◀
️
کانال
💙</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82962" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اون قسمت از جنوب لبنان که میگفتن اسرائیل حمله کنه میزنیمش
کنترلش دست اسرائیله دیگه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82961" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82959">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmnOH0OuF624BxU1FQC8m5sibQ9OJ3n8fncOyOptkWREXX9w0BNOdejOHt1Hyrsy3eSzLa3t6LhUqJ57Tr2fVkmBafZKF-vYJXsbBgl82bwHUPqNDxH29XW4_5MUD_RK5CDOsN0TYMG-W-XLOwS_sUH2JhL9koORWZI8VZPVD4JialfPBOEhOg5Su8G6nMewVeJn3yQTEygevJPaTd3oYT0uxGcf55BUg6R60B9sOa8Q0qpgueskId1ZhhgQipshsB0HMUF7nA_Pa4u9IY2VgoZm1gm26EKZOEr67jU74Q6SDyNAGWMNKlfK-MZ4Oc1sKCbeyRJ7WXaKDM6VqMhTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکوندی شاه عالی بودی شاه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82959" target="_blank">📅 22:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82958">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=G7jbzJ4eHPgBlkzGyMbdVERTj5OSUbW3GAorlujhWCLOosdSkR2SnzMbOaJN_UtRx9Rsh4f0I0fRczFQZsMslT-koCoeMk-Jzsp9DZSNJrcfo5pAACrrzwviykhTkce8Au6NcBYuo4Nv8gNCG_r5X22ku-o0PsZrz0FdBAFqady1AuLbNAaK9YF3_0lLs1Wd9YnCsXoGksAlrs1wRGg9lLVbEy59qIhm909Ead4M1WbwD0Ke7GApGJtXzh67AYLIaDATaj0qZda1WiqT33jIfZ9PCoFWVdN00e2KHLwmgIit5joszYG9vSKBO_OxNEyTqpaWeIZmEBt5YZJaxAZCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=G7jbzJ4eHPgBlkzGyMbdVERTj5OSUbW3GAorlujhWCLOosdSkR2SnzMbOaJN_UtRx9Rsh4f0I0fRczFQZsMslT-koCoeMk-Jzsp9DZSNJrcfo5pAACrrzwviykhTkce8Au6NcBYuo4Nv8gNCG_r5X22ku-o0PsZrz0FdBAFqady1AuLbNAaK9YF3_0lLs1Wd9YnCsXoGksAlrs1wRGg9lLVbEy59qIhm909Ead4M1WbwD0Ke7GApGJtXzh67AYLIaDATaj0qZda1WiqT33jIfZ9PCoFWVdN00e2KHLwmgIit5joszYG9vSKBO_OxNEyTqpaWeIZmEBt5YZJaxAZCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کافه ها هم مثل طلافروشی ها و صرافی ها جای منو مانیتور گذاشتن که هی بتونن قیمتو عوض کنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82958" target="_blank">📅 21:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8uf9nbfQ3ehDTjCHZvUdZq1iz53XY4nCxmQrnveenS6c_85jpySQtyiTVnBs3HJohTwZJf7Vg14mvw0CsUIZ2Zy4OksM7_5JitIlaXGM3bMXI1kBeKrzZLCxanKe-RKhnpzieaV_Rab3xeqMbKFNQ3F7rjs6LvTZ5U3_Zzbz8JifGxuQTqxsadAgMs1I5RxpRq0SSXyu8dka4Jq4Bl-YguramKZZHAe7OyP5gJ5LUQSlkeAfpMct3_EFYshaSwJlllK4CPs1_9iTVrUWy7FvZKVOV5gowh1SSJ1SNMOdKPJKvrZPs7-gcR-zmFwVAWtE7dXdo9sCaf6jYxRt9q3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال و پیدار به نام "Bipolar" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82956" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsaFMqlAZAbOM1bytnwDu8N3dxgKdeAwcnOkUxP-VcMNClrs7WP7fjCT7XiypKFkFMIbieicTsmom0EgVTKkVsn5mpVfG2jXuDjpuPfod_tbyNPDju_GPrWzSK7-ziQHF_65SBeA1hEdlVFcB3cFyGsICknMU4HvsxpzLpezURrgwpeE4jf7FR9JHOYNc2kzcL2LGYFifuiAIJFxWCwvgiex9krAE_EuKfqE7jA7LRIcTpoOrW5HkT0WKyFQJg_eUVGoqW0koOqr_Bdflb6GRegZa-ddChJtHjErESfPiOKE1Xkda6IujumSb5Rzwlof76JfUUV9Me7H243DRRXL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین بد سلیقه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82955" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvmdanzqfawDSf7JACFaPy0AzpIQ26jhXA8VA3ds4ITWBO5C6yORuuwN8bNDTyMWUWWbmoSf7CkijDCEPlMOdWB0q5VA1pcSP3mWzkUX8yZvovPsQaUUE1-Udy3Oa6iwwxO1cOYQ8GQorcOhZfFdDVFRBihWFoh7ZeLZuQQtRCCtKIWtIFDRCAWo7771Xd0RHwRe94QmAKhvgB9fHe7GW-h971Z9wfuhJQZKWGe_3KUB5-e0_Rk5V1hdHw3jb_GbYZpXyHDkp1SfkaKkQNY56uBAFvzHR3GypLg98HlhfxHX0OmUnnkt_gfWbV1fER58v6ql_oxwTe_RefR9g2RNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی و پسرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82954" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2_Qta5WrNr9J3TkoNO2gLjXCZ3uRujjXEPUDA5c0K2SewNX9mRhTC_Vh5M6cGznhp3lhMh2ENlfJDw_2wcT63FHo5G5T-qR5_y7BGmNtpZiz71sdVUClJTvhe_EbpV6SIC4LWaWEG5l6vxipBUU8X9prZfQlM29dfRzCaJsV69PkiV3XSdj3g29rdUP4q5saaxQmX_5v-2WuUT4i-jgb6SsvGTf67hesf4eZfAchdBNI-gc4q85-VSI258Xy7-atWJtu8rmtf7-F956ODb3TX9WcaIZ4CtadbIiWsHh0hyau8m7vFGneRYP-WDm7gYDfqKcde_4uax_dDwLascYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=FVtyBFW57KpZV4MBSFjTDbqToUc4PhuvjHri8yn_N4Q59OmJ4GMC7qTZkYtz4o8iF77zMpbsaM0OBzVTVEGJc8jMpkxHCZawHDaavDDnipY3Xh-a1Lu5Sacw1jZoQBne1V5-UJEzfiEfZtyFaWrVJ4r2QfkeGQKQy95HhTpYiydlkUbbkmKff-SWkfOzieGF2T8gP7zyoaxKGk45x4GXNTrnuxdLUsK2v3ojE1gC1Dn7JOkkoxg4fpeucCqK2bsJrLwunQhRx4NRt9jmu3q7VJCQa_rThZoF4kYB6h3xqy0jKSVD7qBQgeOxkEpqcInH5tpE5mNHMustdVnQwo8rhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=FVtyBFW57KpZV4MBSFjTDbqToUc4PhuvjHri8yn_N4Q59OmJ4GMC7qTZkYtz4o8iF77zMpbsaM0OBzVTVEGJc8jMpkxHCZawHDaavDDnipY3Xh-a1Lu5Sacw1jZoQBne1V5-UJEzfiEfZtyFaWrVJ4r2QfkeGQKQy95HhTpYiydlkUbbkmKff-SWkfOzieGF2T8gP7zyoaxKGk45x4GXNTrnuxdLUsK2v3ojE1gC1Dn7JOkkoxg4fpeucCqK2bsJrLwunQhRx4NRt9jmu3q7VJCQa_rThZoF4kYB6h3xqy0jKSVD7qBQgeOxkEpqcInH5tpE5mNHMustdVnQwo8rhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شات های جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82951" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82950">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9EIIxeM94dkvsY6WyH0PUsBGfAlZUDLxhQpdC68m2CPXF_AiNc77rj_INJYJhbyncLla25EVI936Hp4NUiVoCLlVi5Esc7pz5ylLfpnvniD8qf4d3ZQj8SBekxaGMSp1IXLH1q-iWFdC2SgWGL2bHiOyDsqk-c4IeQh5BMVsIRg1J1158yRr761Oidy20Gf7GSts6UDnyB_Dk_-E__JIAp6jGkFQ2Amagd_OxS0fnAe_qGP_06HvMTfBNbpjaZkDI9LTuz45FRvyuGyXH32-6kwGUy5Hy3xM9lQ_sykSsmYF_fdxYE5XCIObXAG2lu2vQGOTgplDCeYuWX7HhlwYn14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9EIIxeM94dkvsY6WyH0PUsBGfAlZUDLxhQpdC68m2CPXF_AiNc77rj_INJYJhbyncLla25EVI936Hp4NUiVoCLlVi5Esc7pz5ylLfpnvniD8qf4d3ZQj8SBekxaGMSp1IXLH1q-iWFdC2SgWGL2bHiOyDsqk-c4IeQh5BMVsIRg1J1158yRr761Oidy20Gf7GSts6UDnyB_Dk_-E__JIAp6jGkFQ2Amagd_OxS0fnAe_qGP_06HvMTfBNbpjaZkDI9LTuz45FRvyuGyXH32-6kwGUy5Hy3xM9lQ_sykSsmYF_fdxYE5XCIObXAG2lu2vQGOTgplDCeYuWX7HhlwYn14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
بازی Chicky Choice، هر قدم، یک تصمیم تازه
🐔
⏩
در بازی هیجان‌انگیز Chicky Choice در بت‌فوروارد، مبلغ موردنظر خود را ثبت کنید، بازی را آغاز کنید و مرغ را با دقت از میان ترافیک و موانع عبور دهید.
🦊
در طول مسیر، مراقب ماشین‌ها و روباه‌ها باشید و با هر بار عبور موفق از خیابان، ضرایب بالاتری را کسب کنید.
⚡️
واریز و برداشت سریع
🎁
بونوس‌های ویژه روزانه
💬
پشتیبانی ۲۴ ساعته
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g12
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82950" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmt-FwDE-WneAjzK7ynKP1vLuCgocw8-CPbEfYF5gisUZa-dbfuhyk5pR8vmxMYgys1XtGvqgW_7Jcc2Rhbl4UfxLVOzE-PYoRJRj-1jY_bOU6ZTQ-6EAMcKtLrqyHCzHWJ9uz_3bUKBmIPh-P44CpUQlKJT70Xqq1Ot7Iae0Z66odHkBwC_J-dgYg8EYl04i80fKZNMZjUOodWR-eah2ju6QnfL15sk96XFTeNa8UCq4RlcdVTqEJN7AuSuPpdPLrOCYnohpajjd3XgX88yNmaoio61Ftbr8_crbbPEneRBKd2Ya6mv2h6taiVUTwzpmKURRXnM2F0iDzEPzpWiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام “منو میشناسی” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82949" target="_blank">📅 17:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خلاصه بگم کونمون پارس
ترامپ میخواد پایان جنگ رو اعلام کنه و بزاره بره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82948" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcvTSJZzJncmUxCtBCXU9Lm9anG6Z5GvPQ6Yfj1A1cw-KzjrWpbASuBTWZ0cEATteKPMudjVvc4CXHVvVxr9bstmxWRFV_6H2jt7LAkQtCNCch7P876ASgFIlxzBr8odyx9KpjJjViTJ3WXX_wGvb4LhrRaiSxnaUbRl-pSQgs3i6E54qfTdmWiC2RzLm0uaEOcrQ4t1MN0dIWuUpxyJiFJmRSwVf8azLbGI_CSDlzr0J7v4lO5E8BVVebx6Wnq_FjfkzSm3RXkNZA-qCfnAx1of8gN5j3bWvhmzJwTcK7FWc89IXBhNegXflOls05vK6JH_2LbL-3i0NQs9SZ7Kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل دوم این شاهکار اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82947" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=AuVEFnNZ9Yn8NqqO_oquM7m4LwzSTGUW7TiT7VYZmmwPvERulcOH3T7KvEAtUp14tbnUFRCYPMuy6AXBAVRe1IpaF_rHWEHTOdXGg210dwHKJ37p9UaXMySzG22ycs1H2hFtbOLCfhdeCO0nu3PLanRjuyGu_g5lYkaBwVM6ogzgOi4GJKN51XiEBYsHYRKGxhBIv_BvDkZXppU2bz3AURB21m7-PxJcV9m76iAAS3fJE7jHYXwz1eatHrAIimFiXTscZ8CIZqsmQJllo-ug8PYnT8CqBeW1t-kFwTrps-yHkJSf21C5Vz3RDwWr9EbnwuzGE2ZtGFI5cz3yYOrLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=AuVEFnNZ9Yn8NqqO_oquM7m4LwzSTGUW7TiT7VYZmmwPvERulcOH3T7KvEAtUp14tbnUFRCYPMuy6AXBAVRe1IpaF_rHWEHTOdXGg210dwHKJ37p9UaXMySzG22ycs1H2hFtbOLCfhdeCO0nu3PLanRjuyGu_g5lYkaBwVM6ogzgOi4GJKN51XiEBYsHYRKGxhBIv_BvDkZXppU2bz3AURB21m7-PxJcV9m76iAAS3fJE7jHYXwz1eatHrAIimFiXTscZ8CIZqsmQJllo-ug8PYnT8CqBeW1t-kFwTrps-yHkJSf21C5Vz3RDwWr9EbnwuzGE2ZtGFI5cz3yYOrLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82946" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJBmFbSEERjdmtdCv5ws-rp8fYA6T8Uejcqu2rT1icfug3mc5N-bAuIHBDxl1HQcM7YfWZjML6nODKODdlyjTNqKjqQehvX5TH6w4JivlmtPl-rNpd_XLGGYZOJPr3AtkNj650sxtit75sE84N1IFacRlZBq5fZYC8S-bedMjcBKoYCcT9fYhyvMKVrcQ7XUruQSVdWwV72KvmC-O4E-3sj9nd68OSqdEqyyC9wQy8SbwJoFbraHZ_iRhwzM13q7x4w5eifVQdZ2iS4gs1gvch0bNpGmzglLOvIbYcyVHiYON7tPMh3sTDl8ItJ-m5CF5V7xVYiYYgOpQgbBaDHj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت تلگرام تو توییتر: امروز احساس میکنم خیلی کیوت شدم، شاید بعداً عکسای نودمو براتون بزارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82945" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHmF5j6M3f6z5idsZi--VfeBsZFZAmnXSeb1wo_-14GGRREQd-ttuD2m6kadtFvcZOOTVljvjMouBA4OD6vHkw7nifHKDErvuIrjrz52i5Z9Bb8zdf0-96jN5WLhz6mJV05g781Uo6k4FHPfQAFzAJvDv_PXqXPbNZtJeQcBxx1WZMt7aMkPHjZwS6rptnh1ME_-z11m2vKfvvSdG9738ehDfdxTAIyDiTla59djfjZy_h5XDlQiZGdlC8wOlQMBXwW6S3bhHkjMj2NMufiGyjsUSrsn0x0EDUZk59pTFAeJbn9PNhQh_9GCgF-UBUUMlK0Hd3sC3Vb0jdTfqG0f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد توافق ونس رو دعوت کنید برا تحصیل بیاد حوزه علمیه قم حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82944" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=OwX1qFM621bZXKhphUoR8BVd53nNYmAUGWDykVO2d7ioRhBY84ocjZJ2FX_ydCmdODREIMiaLCmqTUH6K43mn9kat6570gZG9mm9fS32R7yC7l-lIXVNr7_02dXitMD-PR-n02u23xUm4_cIjNOgO5flr16BwFpeQfkjFCTlZh1huaAFkBNzbdYY-9F23jlzMWik_18cdzfLbr8UoUzCYc8i2xxDGxF24Uhda7sw2vvquunKMp998XLRpT7408sH8RvYxwqP1bzNGeTKxCo1gHrn5k-NHfZDs_Mtubgk4lcwHM59FaN4AHbZNRR9BeI9MMEgGYdQ7lNp3RhYjBuP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=OwX1qFM621bZXKhphUoR8BVd53nNYmAUGWDykVO2d7ioRhBY84ocjZJ2FX_ydCmdODREIMiaLCmqTUH6K43mn9kat6570gZG9mm9fS32R7yC7l-lIXVNr7_02dXitMD-PR-n02u23xUm4_cIjNOgO5flr16BwFpeQfkjFCTlZh1huaAFkBNzbdYY-9F23jlzMWik_18cdzfLbr8UoUzCYc8i2xxDGxF24Uhda7sw2vvquunKMp998XLRpT7408sH8RvYxwqP1bzNGeTKxCo1gHrn5k-NHfZDs_Mtubgk4lcwHM59FaN4AHbZNRR9BeI9MMEgGYdQ7lNp3RhYjBuP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بهت میگن اگه ناراحت باشی عامل خود فروخته دشمنی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82943" target="_blank">📅 14:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حاجی دوران شهید رئیسی، یادش بخیر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82941" target="_blank">📅 14:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2N40tyGc9xubw-Xm4vIJGRBojjwj6qdJVpsWDbMGQFwhg1cHIFOClns7TyHfOOe72o2DK9cHomfJBB5CAyLcx4kO_NLuGX177LtFLccsvUQeBV62HUT6R6BVXHI6DW4Q37EQxrEwU-k41zjDe4dEnZaPgaNqcDos7qP13MPyhJslZ1gbqHYHRQ2av2fUFt_y31eOGC63M7x-v-YVSFhByCPcZhqY0qjGO3reughsP8jP5mbopRyhqeVdhTENFPCnGAhVG-SmoQqmM_Ub2evELLdGyDz0hhVrJj-R84sUqcrveZVUKLfM7kk0ZiidHF1fsna3LKvnhjGw3fS8qfNCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی از سنت خجالت بکش این ایموجیا چیه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82940" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه گدای ایرانی تو ترکیه با  ۵۸ هزار لیر (۲۷۰ میلیون تومن)  پول نقد گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82939" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyHkbwTrKEzVoze_i-hE3NgYO4BX3yY249Y_WdwrfXow1L5yIrVtBCGWcd5aGqbDyc7UQIaC6EkZ1UEzMnPBNHs9a_PMqP4xFLWjJm60TOlvtDzjiXnV6D2f3qNnVAwp4pZ713bsR0xmNeQdEeS4w0v607bI2kKJuqLP_tuKrXfuFrpXOm5P7aANC2c-QqlFtNkqW8SOfldc0eE0OxXVEqWoIhwAfDIuxX1CEOgxnJ41u_msb4cvAWnFjWpWZRWdR1KnU2qXYGLfSEOq9jjbx9UUCvCnxFM_rnHy3yf-cZMYcs3dZkOZX3Ay3Ho_EAGTamkVCEKv0TqPxZNctNvAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=evSmKE-Nxhi1En1TkCqg8o--7W1uco8GRGmmY5YniiH0ZAzhsLBenTNa8aZD7DIeUJgwwHzYTiPNf2FXaSZJJAM175JDjCTPdeN4zHdoTpzzKMZ3AaSe1RCE0s3EkOmsJ8Hj_DXYd4We1LXoTxNxrk9IAPNLX95zb-_sMq8Asd0jSPoaOxuptBKRkh2Y1NDgnhqrt20Up4vraPsflegbqxfNzkdX98KRgh64ctiTYXMT2Qw84W0l4I8JmqV0Vs63_XEePMJnHITF3DT-ZNuKD70G007m-f_unxiybzUE8L-6PnGi3Rc9eh3r_7iZCIbIgsw3WVcEJh30C5mW-JR0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=evSmKE-Nxhi1En1TkCqg8o--7W1uco8GRGmmY5YniiH0ZAzhsLBenTNa8aZD7DIeUJgwwHzYTiPNf2FXaSZJJAM175JDjCTPdeN4zHdoTpzzKMZ3AaSe1RCE0s3EkOmsJ8Hj_DXYd4We1LXoTxNxrk9IAPNLX95zb-_sMq8Asd0jSPoaOxuptBKRkh2Y1NDgnhqrt20Up4vraPsflegbqxfNzkdX98KRgh64ctiTYXMT2Qw84W0l4I8JmqV0Vs63_XEePMJnHITF3DT-ZNuKD70G007m-f_unxiybzUE8L-6PnGi3Rc9eh3r_7iZCIbIgsw3WVcEJh30C5mW-JR0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مسی که قبول کرده GOAT خودشه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82937" target="_blank">📅 11:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6YQARkg0MRbW0mURjxmD1h5j6Pt9YAKIhkXG3ph4q3rNO4U4yuiCoiAWiV0SDJwCKDkXUdDglvXj5dn_hSTWHg2O2_fFbGezcrZ2JfBi3QtTbHU6dewBYxdCXHi7OXWDqH4wdqX737-G8ZhYuD7YD6g-Tux8gU1FatVxm6t4m8kcqu3RuGos19042Enm4czjGh_T2YcfXjL9GOlIf_Oh5N-saQoPYqbRj4csfba6fhW2nnWOhUw3gLqATb1_NcDblWRK3zInarD9BPlzv0cDQyNQOvi5DqIq52eOX-7SYkoKoWIjIGeZ6-0qv-EjSHZnhfo92rSdH0wQ27Y7IRnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام اینو توی باغچه خودش پرورش داده و به زنش کادوش داد، ایشالا که خیره
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82936" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82935">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrNOl-uUyDz5Gw3RqVB1Ibc--ESaxz0XEIxgeojq8mgg4wUWbciCcH3AiiqmLdQuHKVwvgWL14IXkPJktKL0AIJeoryCL0lNOurBLQyESVaG8toT7iO8MY23AMIXHlUOqUorQDR1Y-xOfr8SZ5V8Y6SP6ugRTMluZqli6w1D2ATdj6OEvZ5EkkkwK-0-l0VxDsq8XvhNOeEfO-PdAlLcyNLTo4eP-BMAbzQf80WW6gvjChcRdbFWXrQALduaX0lM_mpPyAYPyfDiOU9W7xDO9ZkdMJx9llUXVE1OaG0NGxfQHzFCd0ESZdA0WD2a15cP7XoZilojX2BMhRCunk0Rx9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrNOl-uUyDz5Gw3RqVB1Ibc--ESaxz0XEIxgeojq8mgg4wUWbciCcH3AiiqmLdQuHKVwvgWL14IXkPJktKL0AIJeoryCL0lNOurBLQyESVaG8toT7iO8MY23AMIXHlUOqUorQDR1Y-xOfr8SZ5V8Y6SP6ugRTMluZqli6w1D2ATdj6OEvZ5EkkkwK-0-l0VxDsq8XvhNOeEfO-PdAlLcyNLTo4eP-BMAbzQf80WW6gvjChcRdbFWXrQALduaX0lM_mpPyAYPyfDiOU9W7xDO9ZkdMJx9llUXVE1OaG0NGxfQHzFCd0ESZdA0WD2a15cP7XoZilojX2BMhRCunk0Rx9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
بازی Chicky Choice، هر قدم، یک تصمیم تازه
🐔
⏩
در بازی هیجان‌انگیز Chicky Choice در بت‌فوروارد، مبلغ موردنظر خود را ثبت کنید، بازی را آغاز کنید و مرغ را با دقت از میان ترافیک و موانع عبور دهید.
🦊
در طول مسیر، مراقب ماشین‌ها و روباه‌ها باشید و با هر بار عبور موفق از خیابان، ضرایب بالاتری را کسب کنید.
⚡️
واریز و برداشت سریع
🎁
بونوس‌های ویژه روزانه
💬
پشتیبانی ۲۴ ساعته
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r12
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82935" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g68Lw6nEzDo0uPGMf_0LzFoPet7ZR5F2dc1_foxkedhR8RHNULg_7EULGqE3trxIKt3zUKtUpIJxGFHzzjSl7IWpyAiV1vBh74kHQ7IkFWPNkpiyw7Td3X_W6zE7laegXROgXoREf6MFgnUpXbzFC1hzIMvcL_nHV36Pyj4M-_dldhLzG6Xvv9yhYRDE0Tv_0Um0LTpYhVf9bOfKD6EaR8z8bf58Q9B94_NhRzKBGh5Yk4bjH6zvgAzps7L7TdWtrdCLb19uAj7ByCTK_1TUq9IgU7Ftf_Mi2NwuwHZHRaBXajUbmmTtZeOruB71EKHxPRLAyG_5EnLFbIM6WHmFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرسی نکن پسر تو تازه ازدواج کردی
😐
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82934" target="_blank">📅 06:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82933">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=DVyOVWjBzb5P2xVgTQre3hO08IB4pZWRBAYz7vmVgaJ19G26VxLHEFZa0Nkx7_McuwKPqXHsLbewBm82bOLw9kk4oBE0e7F0ZAF__Ua9qjOE8F6nsHmAW23IyktQY2GpBJ9hrygqa8I9J4GK1gsGVeH8gui2EYgdqXGziP3a0eO6X6CIC8xDyRep1SrHez44EEfkApC_NPKgd5JNehJfNqmUdF2v0zTFXcMu07_mTav_bmCzGJYcza8e-f2V2avIobB1StlWOzWOgRvWJ2FExJQg5vsZa62VBLguovBFvjfiXmZiwdoG28Xmz1PQHFqaK7jH-e3GKSLhkqzvcudoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=DVyOVWjBzb5P2xVgTQre3hO08IB4pZWRBAYz7vmVgaJ19G26VxLHEFZa0Nkx7_McuwKPqXHsLbewBm82bOLw9kk4oBE0e7F0ZAF__Ua9qjOE8F6nsHmAW23IyktQY2GpBJ9hrygqa8I9J4GK1gsGVeH8gui2EYgdqXGziP3a0eO6X6CIC8xDyRep1SrHez44EEfkApC_NPKgd5JNehJfNqmUdF2v0zTFXcMu07_mTav_bmCzGJYcza8e-f2V2avIobB1StlWOzWOgRvWJ2FExJQg5vsZa62VBLguovBFvjfiXmZiwdoG28Xmz1PQHFqaK7jH-e3GKSLhkqzvcudoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش میخوای کلیپ غمگین درست کنی درست، ولی خب مشتی از وقتی یادمونه این بازی مساوی میشه خب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82933" target="_blank">📅 01:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgbXhu4pHQTMosKv1ZIpKAvCWnZpaKIHKbZROrClzwPflOk7kBA5rFQrYCQYzGSiCLwe6MzdLhZGRNlie-uZLajZgmLds-li3WijW5YWSxal84rcb8kvH60MnPyENKTzb0y3rvvU1BDZ_61bQ6UHnIE_0X4gjQxSRK0XmYEezh7Ue60oBK-PVHrfLt5lPkx3DYSkEP1-vM4X1pq8WMpa9K5iIbT3nUQU-rL7MA575RmaDrtFgpSuh_cJuUacC1hvkq62sh1VrVHn4jCfQ6LrI53Nj-oOFHx1C-bP6Acw_Mt0XIJozCU5p2xuFdZhyXvSEByQ-9IOS6dcjzAVbB8-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش بی‌خیالش شو نصف شبی بگیر بخواب، اون بی‌لیاقت بود تقصیر تو نیست که، لیاقت تو خیلی بیشتر از بودن با اون بود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82932" target="_blank">📅 00:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OngZYvSns3POk1GgSThoUpuUFJww2vCcqMP6KS0TNdL95jd0ud31y6qbWPt6wSGwSqnwfV2mWyA19REGXUVqEtOdS6XnDI__3LEAONUXXA3V4PzKbSy1Ei56I6zpBPocJiOyuvoBFtGie-IL9-fTwE8KEBrwbpDEpihb5MgbuxwzTD2HtoxLuq3Hbz_gflHHXB72k6aJ0Cu10URTg_ukTDFqFdggtRGXCz8_QxOgfh943aFcc0X0SmSvjIynSbsy1zQFJu3pZ3fpLZgE9W9PZmfqektaBNaaj4zvPgoWzY3mQj57WEW36KlAMb7eLX8WFRJq-v9iX9rMzZSppFY5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۰۳ سپتامبر ۲۶
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82931" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf4r_mKQpkKrxvLskUYNVp96HCWkSTFu1KjpjhVAsBFq6yn20QAQc736hjYSZ1VzI2rcSItjwR3FuWYr52c2G092MyZgs4TPmcz8DRfK3aDa03knkH_nnFrwcw_OHNlH7-k5zAF5ptC8FflTAp13U9CFAtF_Z--6VqsyNn2kV0pQEsvIPyJKgnOx2Qtm0UiSjsyQZdy6TpaAxVyRQCV0y1ijqIZ4NLup2LJeFzoHsA8rUr_933JZ4VDNbpxZTCGIDHAaqPfDcvugdSNSKfO2U3OEUlb0hrBcx9gRb25JRmxOFyg-5oyCNkVUfcZ9K0RuPNLmkSAH-Nsbcqr1M3gaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82930" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود:
عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82929" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0ZO79EdjwmRiyIOvhEDOuvnaPnGphZxkVDnvuoFVG6OXky_MSO7wapY9CJpsui3yKM4_OYX3Iqk4ielzx_yb0swr8cl4u2PlTswI18-2ojeIKUbVReI2wdDHfuYztP0INCbIHaznrSNC6tJ8iJmwksBaMDiGCCiGVgEtY3pM8pCAePneWYK9P9wLOq0rvYgjpNbcCqE82FsvwhbwPJoD7ILs03VQzU7YxoIkACkVsG8S3-O248SgUSir6KqdnFsGdhJsoTknPFHblO7zjuNu0kLrkky-jCxIwfl23q7Mnbi-yzGclfjhNE-jB546nQ2ypuFJViesjq44xqo9dUQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این پزشکیان بگه یه زمانی همین روسیه نقش آمریکای الان رو داشت اندازه دو تا اصفهان از ایران خاک غصب کرد</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82928" target="_blank">📅 23:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پزشکیان خطاب به پوتین :  قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن. حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82926" target="_blank">📅 23:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82925" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لطفا موقع بازی های حساس دنیای فوتبال، شو های مهم و حاشیه های بولد قیمت دلار رو ۵۰هزار تومن تصور کنید، تا کیر نکنید تو مغز جوون ایرانی ای که تنها دلخوشی هاش همین کصشراس اونم چون دلار گرونه نبینه، نکنه، نگه و...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82924" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سیگارا وینستون جدیدا بوی پهن گوسفند میدن</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82923" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ4shZfqbWD0xUDHM5s5GmQ9szD2rrsJE6aIDaKCafqEHMhE9vFnjCCS-q9RZYuJcYx2tSHGcnX5PiKeR2KAF1yCEf4evq-osdRTDTDTDAe7IetFjkpfx8oHJEVBpxHnisjIWjBJv9YuKFuJBgGwKpx_DAxTVYSNhZne6PxPw4FgwAAJyOwNOw3IywNIP6xLr_L2l2h2nTyVdjxxFjN9kPwnLC6nkHfbZEP7ixG2vW2eE0n3wI5YnaoQQ1VN9rItxMb9ERdTgBcGzWWwdEfWWbO2faRd2wJJvRX_ABHy37rhF6WJg-L3PVI0zeIrFICDW68oxUfj51bAjzSJgUP0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUUmHemxe9lO2YCx05-JXbKxoMIc3TIOJ6TUCvyIA9kSPcRWclnqkbgXuvdYb3k7hIJxRY-P6LB2nItdSOit7c0tbw_cZSPJ-A6NgRqOV22qmq1c-QykxSOimJqV8jwguiqX2bFKEHC_HLNKlJym4uTKwakkd70B9Y-vbosgMRt9JPw9B7Imd5cXitrSrJXKI4kmu6qcuaeC9k6LJvv8xkMG18zITk20Q52JzylgN_tD7y6mleWqGhQ8wFTYiPEvP5R9MF7mHk0ASgrzPC31iukzU93LZ3fgsiWEKUyn57M55nwqpn-BSZPd00gO6Op8k-FdoZi8oMsX6E4LzBi_wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید لنا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82921" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خلاصه‌ی صحبت‌های امشب دونالد ترامپ، رئیس جمهور آمریکا درمورد ایران:
تقریباً سه ماه پیش، گزارش‌هایی وجود داشت مبنی بر اینکه ۵۲۰۰۰ معترض کشته شده‌اند. و اکنون می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر نیز به این تعداد اضافه شده‌اند.
به نظر می‌رسد نزدیک به ۶۵۰۰۰ معترض کشته شده‌اند. تنها توضیح این است که آن‌ها مورد اصابت گلوله قرار گرفته‌اند.
این رژیم روز به روز ضعیف‌تر می‌شود و به زودی به مرحله‌ای خواهیم رسید که دیگر نتوانند به راحتی مردم را به قتل برسانند، زیرا فکر می‌کنم مردم دیگر این وضعیت را تحمل نخواهند کرد.
اکثر حکومت‌ها نمی‌توانند این‌گونه با مردم خود رفتار کنند.
در اکثر حکومت‌ها، مردم تلاش می‌کنند، استدلال می‌کنند، صحبت می‌کنند و سپس ممکن است یک تغییر سیاسی و انقلاب و کودتا رخ دهد.
اما در ایران، آن‌ها مردم را می‌کشند. وقتی مردم برای اعتراض به خیابان‌ها می‌روند، آن‌ها را می‌کشند. آن‌ها با مسلسل و سلاح جنگی، درست به چشمان و سر مردم خودشان شلیک می‌کنند.
خبرنگار: اگر می‌خواهید مردم ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم در این مورد حرف بزنم. دلیلی ندارد چیزی را افشا کنم.
یه سری کصشعرم درمورد حملات محدود و تنگه هرمز گفت که اونا ارزشش پوشش ندارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82920" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">چقد غیرقابل پیش‌بینی</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82919" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">0.000000000001 ثانیه فرض کن لیگ ایران ببینی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82918" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این دربی با اختلاف بهترین دربی ۴ سال اخیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82917" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چه موشکی ول داد یاسر آسانی</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82916" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82915">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82915" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwlGXP4sGveqtSlM2ZGOIMODsU7lxXdER0fb_p1JzG8Z6q7FPenY27gCKifUI5rvXBdeOq7M_kXJKyIBovDyplIATyNgWC8hYGXZ3ExoqEfWhy00tZRMXblBU55TttQXiFHKVXuW85EkuxazGPzZR85ijWwp9mfZrl4k4olUoJCavFgVfy8oCBc_HL4POY8iJhE2CTzDpK-JhUSD_0D74ONrkrjgHiF7mdWjn7sxIFPpAZ8kU0VP7ZXidBAnIGKuLr18Iim1hmR_Oa1wc9woxWmq60xrvCV0D9mtYXLyQTjkrDC7vwOnIawTEkkm8tspW9QVTnfcBvgAjCzOrBnb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82914" target="_blank">📅 20:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb-JEqB-uXCOnbKYdnr-4Mo8G33surbSMAh7C4dO08dE69jcPi-8TTtUqRkFKzzCkLa2LbpJ7ej5SsEltONZcMkbpusqxi3cmo50Zij4ADZT-0dXnYyiRMIlGlRzxrU19rCfd3C-wbSp3oERdbys9uXzem1Dox_RhRXLiouSQa-HKJLIvm10nFxJ-btQRUOvxmPmrqiGgF1d2S3RkXEzrnbH7y9tXEaq-n_xBsoSxlT2_21EmAgY1iXiuO0uThYULcfuO-kWNvkm_3I0rsu_PU9ChBnBLPKnd2KamnLTeyGbJHCCKFu2r9sUZOGNDk5BqTDl_H6N5TtoPE-CKyXvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکو ها جذاب تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82913" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqcFnlj1jGdIzepqYjHg70n1z5Af8LIN-OvpjWVuBTRqVAm8d9e0TXn_0Ed0kq7cx6Y4ud-3fxmuod2GrfAEAdWfy0sI9af3CLBakP17UV62BOURn2FifkhrR1IMv4p1C4P_Xsi5HGpXFARtwJchO0_G__zzVKJpNTyGv3ddeUwsog0fXa9THbPx6xv2N3-XSkpU5f6JgIEcLPXlxuO2pctxSmjc9QywJG0N-AAwFNdtwoQXEQsTeMuoN_zuaAfq2kwQf2bkTBWuNHBF8hiYhWSgqzqDo5Ai6JMKnvPRBCmov15YMv3zZvMpZfrrCfHtzZsfdaqdeVkQ31SfqQmipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت استقلالیا از دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82912" target="_blank">📅 20:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پرسپولیس از کون آورد که نیمه اول مساوی تموم شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82911" target="_blank">📅 20:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیرانوند کص ننت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82910" target="_blank">📅 20:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خلاصه دربی تا الان: آقاسی به علیپور میگه بیا گل بزن علیپور میگه گوه نخور
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82909" target="_blank">📅 19:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">علی پور
😂
😂
😂</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82908" target="_blank">📅 19:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">موقعی که پزشکیان زنگ زده گفته دربی باید مساوی شه صالح و آسانی دستشویی بودن فک کنم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82907" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5OmzIeyiC6axBxWNCdWukONXqxnXN7lOWXTFG8Bs6hHiEmujCQkCnUmrNWSZ8gF4PQ7JlqzJ24Drwnc0b8AhYy-2ZwGo0cdi3NHDInwqnbrLpNUKA4Y4rA19vXnRp65czfpKpQYvLNT6cOczx2vsETqjD5XoPAVUqD6lXUA4TWYKkttHSX6N9X-ElF8jjLwit97SOl8Mpig_EsgoUQx4A_hn2MRACXB2szW9lR-8xpwEsPtwc0AvgWV5vUy24YjXjDBMDCAUbzl3hWmUGpYgkoHuKxjDlggdXq0EafEu6u32pKpRz3YwInf23wSvmJjpla9_nJGDEEV2giNDO_clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا مناطق خاورمیانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82906" target="_blank">📅 19:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82905">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد    YouTube  Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82905" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS00zIju2hyVlcrQCXqJAoLBcS0KeU8zO-DGBsQqaN6liaLo5lkpHe6Jk4ZgIteN75Vix2bH97XKpUC3YzBfB7YMqnCqSQcxzmEt6q803Ypkzw3I5HBS4BbAcek1ZqZqhFz2zTOazhvu8_1IfoFv7XJkg4jf74P4rV1XS-XP40_mw-ZvQT99PWiKNrVo5KaLx-1aLvUyS3GkPAMjwcvhk6cw8SngDTnggVXi7D3_KPaPhCrfWTrbddD6IDTMLonZiHl9UNd5RnI5nDKhXEybo0sSegFJPolJYJMYO8-UoX85cdM_Fhybr3QdMRq9CFBAyZSb7BQPOcDMkTmPWfNXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد
YouTube
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82904" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آرون جزو معدود دلایلیه که رپفارسی رو دنبال میکنم هنوز</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82903" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82902">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82902" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWVtLLIrI0P_KOiYCUHzmEEezCQW62Lf2CYntdfUdu-rKR4iA2l5Fsf9sZwBSXI-klkNz6fhaFGWKfpD0j7uHc0nWVVu7VxLOTzpx70PqfFfFwlMjmAwQnzofbTL_REwQ1bn1lbxxRDBIjDd929epkS3Mv1vG-pLB-1kQtb26wKwFfAU6SBE4Rm9PnlLfYfoiiyCX0xYU8Z0q3NxSku7hssC78BvhC1jijW9KGp8Jw8qkD4Uurerdx8hQG25SAlgHh-TWQq1owJkV3cbBKgaZimEuVeObpGYOwQSKPzTwtdlWRErzDOWUKy-W37sDhjwEktBjQ4nVoAwlV9CczRrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5Z-M2mdE9BqH9me83nnpej2osBs5N5CI2hsL4Xij_Aig-YIgSFwgQ9U1lrJBCFIgPN2AT0L0kJs_lwThlgpQnSmDQFrSZkn_y_--26n_OHvVa_ULGfeuSbJcIk4ticzYVnUrtu-8YW8a9wX2zZXuVab-INXuErGQSH__wPbr2WfNQqIXLFCpzw16z5SKejNLqNQmxXcuUT9_sSPkUYvsWMpoZYo9DqepJ1-8LrhgldO4CGnuNmT6G7GlnWV4SHDt5YA2CdikyyTjIvYhVhtLuGKia8aOYZgTSTR_ESNdGwnFEfDDxv4bfExVzv22LN6_rUSZMd2bkBMU0jDxr8GoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82900" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82898">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جدی نمیدونم تا وقتی رافینیا هست انسان ها چطوری میتونن فن بازیکن دیگه ای بشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82898" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82897">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0W4ALJc08SX9oMFe9bT_l4Cf-OlJh1VnjPeiu7DF8JDMSf7wNi8pQsx0nwQPdJp52PGYKx3OBhxiJeWYovl_ZM2oEuGG61aYgStUIwHI2PoimYa2JX2aF7-U8-3p3SwChiEtUW7wBrixlCBgvbP9v78QHmNtZhRBvQfTWy5byy-81u0YYHiT4iU9WnQ9NyHohUcYDTSUgJOcl8YIKGzgrzi7XsaHA_uUkuLcrGDJnEYpDnBvm11n53FpwRWA45wqfEO_klfi5fIKw2d6HfVWM5g_t0PcVv1_oxwdEgxJo-1MH_pQlWdaZm_ETWIt420MfrDF3p0PrR8dIMDYhLG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82897" target="_blank">📅 17:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82896">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دربی ساعت چنده بچه ها</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82896" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82895">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">خدایی چطور هنوز فوتبال ایرانو دنبال میکنید</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82895" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82894">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82894" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82893">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شب هالووین امسال آلمان قراره یکی از ترسناک ترین شب های تاریخ خودش رو تجربه کنه.
کنسرت مشترک عرفان، ریری، هیپهاپولوژیست و ایمانمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82893" target="_blank">📅 15:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دلار هر 10هزار تومن که گرون میشه ویلسون 10تا ویس میگیره میگه "شما رپرای اونور آب اصلا چی میگید چاقالا"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82892" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امروز در کنار دربی تهران، دربی شمال هم بین نساجی و ملوان برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82891" target="_blank">📅 15:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82890" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itCP0ta-N564ymxcwMcA_WvVpw0ktZF76QJpN5CI_t_RW_hs9hkeFyuCgdxPCdtoy-X5kpi84VV0tr_2h6gMUjFYFWR9jrQKx_rAK3o19w48yTTAAv3_7YzP2WBkzD3vpdhOmQuAC_pzFupZtWrljnSicVAI7Mc8pe2Jl3cUjRrvIZ9TwE-Ec8N3gnyNiRB47mdlkfD4-N2srASzCEk0ZJt_wc9PrECf83oWVecWaeqCmf2DaQqzNzYqXtjagZAziPu59PTYUjsimqNbOkb33lWSmnkTvQ23lWbC5wbVMdrP2adv7jXFYVOAmf-Q1MSJ3hGHby8Mv6GlRc-mCWGJIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82889" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82888">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فان هیپ هاپ بابت تشدید تنش ها در خاورمیانه ابراز نگرانی کرد و خواهان توقف حملات نظامی شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82888" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاید باورتون نشه ولی زمان اعتراضات 401 دلار ی چیزی حدود سی هزار تومن بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82887" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5-e_m9Aa3_9V3FYqLOgrgQnIi96VTpjZdHEhkEhoprSXb40pf8XiQipL6Qj4Ui6H7I9NXm1xLmjzhNU3IzVOEFPTxw3k98JW5Mj2C6AWCejrR52haFV1F9njsn3DKwY9GYY34WhbnPH6t3GUSf1KWZ3ddnf7PjC8qmdJgtrlVW_1w-VC2r1oyAhM_me2TX3cb0mV2b0kIF_xtQKKA7ape8bFMuCfmuReMJMNMlCnoWrFGNRDD-OB_kyZPfe_QQ0Su5qjr5KTJH-UCdDHl9eys_nFIu4XdFOP7Pm4FMh1ksRABuDAtKVxCGLNwvATkXuaVmnEKUCujJY2kHKUh7jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مال دیروزه امیدوارم الان گرون تر نشده باشه
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82886" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnbalF5gLpFqYT45Csn-UJbmtpF9tJun9ExUzERcJS90Bl31uN5Loh-V2fT8Wuha1KoZ5x-uQV2PODFqST7hs1B9SsG_412MMb-lvgggHs3nILpwyZyNEGPIxmYj7GHdd_1m2MlqO7SHkj3WHynx1U8qJgeSHQg4rlaJq1E2yLDS55iKulzRMHILmdMDlN8WHprggLfIX92PiqHiN-arE2y_fP-NBmE832xtInfpCIQy24yAiAo3Q0QUXdIm1uEpf1-CiQTDsPsr3c6MdMvceuCVbNQ3pJlVBHwzlyLYEZdvfWbjzTPpAUn-rYO6P7lFgaDunmctvDUAn9IeNoRj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان حاج‌رسولی‌ها و آرتا میرحسینی به نام "مست سر صبح" ریلیز شد.
SoundCloud
YouTube
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82883" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دلار 222</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82882" target="_blank">📅 12:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_j3UmyAlbhaT28dqBD48hyBPAj-1lbmmt9yRYbw_jStrqIwWvFu9z_R-R9G6VP5cMfwS_s6F1l-VkjKdYB8v7Cts2GgzGMGT5cURwOtzNBYGnxNC0XrVzj6QlM2YBlxkQk_EgDWYVxSFWVjc7jFeDs19LTHUBNJ0uD_9WzPa5OVGQGUh_HLEK4-05bG9QZm_MAv-QZT1vTWyZL3Oh74USjtdxctLTK0TeCD-XYh3pYedsXxBnBRXBJp6jxn1qQGv_t_dibCit8Vj2el9uYhSiyTXCL4yFP9QQq4ZCJkPvZvmLGxb_tkUKw70BS-WpiSLuyb2ABpXE39CDpZQSv0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیب ندارە قهرمان، تو همین ایران خودمون تو مسابقات مسترخایەمالیا شرکت کن،با ترابی و بیرانوند و خلیل زادە و علی اکبری رقابت کن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82876" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tl_0Rc4_IgjVp2-3jq0G_BshtkhD5A5hzPFXP-kjWXWrNT0TUG6Li-6E1GDWI9Qe7Xpo0K6HniOWZ66sj4-tmkad-Bn8xDgRtITRo0X3SI_IcwLdcval9G6Bwmpa0i-KEWmSpRt4bZ2ZEqKwh-EqdbTWFC3U5EcyROj2pkIj0kduW5_lx4caH1JjRyqblnl1cfv-lj_Yp8Bk0u51yP5ItISz_F7m0mlim0lqPQ4hdi8lICvpor5ap8opaA748NR1FHRxRsjRFf9k4y8tk4L-ugGh8JDP4hcd-QrNh-ZuBClY82n4tn7HmLnWgqKvgQNM9t-tzrR4kmBFve02LobhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر خیلی خوبه
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82875" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82874">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my2aOOsh7QyUL7U4w7lZ4B4MWydUkl4GPVKNrFinKRXWy2L-21mx8jBue47BEYtJDviAN4Xc4T_nL9qCZjyxYhaQXoaBMeReQI0lD5Ysll9L-aBzqbF0jpCW8P8TYjBFXLv_WlrQ05k7cCu9T_WZYhuzPAkj0lwwjo0AFu3oGagxTf3nv0LsLR0gQkE2ZuT789CDx6pE_KmKeQKOQKHVRXFaYO0YYUfzh8jHr6iLdmJs1tUlWE5_4-RBwOM3rzX6rFEeWiDiGC5FeHO3Bo3yUmfjfOLCkzaizNj93RzCtbBlzojsRz6CIfVdToD-To_FU4_p81V_tXCYeqQwRr4aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کاوریه گوسفند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82874" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجار در عسلویه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82873" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجار در عسلویه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82872" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فرودگاه جیرفتو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82871" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=uLCmhboubVMBTZ6lDVRZA34m7m68atV1CF4lbABixWTHxGHOWJnH_vvfflpZF1HeE9NHnTEurTK1HHT1lo7EflUB-W1lM90umbImTDeGDi-deyELlZKAMde9k3RoyU8-_OUovZL1q2G8QaPBeTdsGEcAv5mvv7aeCpWg2udR5gclqpytU9b1lRedVzzwk4nbX6z5W9p0PekKBQQPz_Kxc_-JBCVwZMEsX5nBVfED4OuC_Vg3ihYuox9P7cQd3ul4C5kfW-x-m4wFaz3BxrV3DBMW5Ngb7pdAJRCaZGKv_UlF_TypP8ZQbmsVAleyuK9YzGtyZo8dRnUhcpRG-xdZ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=uLCmhboubVMBTZ6lDVRZA34m7m68atV1CF4lbABixWTHxGHOWJnH_vvfflpZF1HeE9NHnTEurTK1HHT1lo7EflUB-W1lM90umbImTDeGDi-deyELlZKAMde9k3RoyU8-_OUovZL1q2G8QaPBeTdsGEcAv5mvv7aeCpWg2udR5gclqpytU9b1lRedVzzwk4nbX6z5W9p0PekKBQQPz_Kxc_-JBCVwZMEsX5nBVfED4OuC_Vg3ihYuox9P7cQd3ul4C5kfW-x-m4wFaz3BxrV3DBMW5Ngb7pdAJRCaZGKv_UlF_TypP8ZQbmsVAleyuK9YzGtyZo8dRnUhcpRG-xdZ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82870" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82869" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.   Soundcould  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82868" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWg8NwkdR4QIC-W_kDMGznJ8isT8QGsVAPKfTj7PhzvRUjn1jcgepHXgG5dbo6VlhWk3WMzW88mR2k6OWF6KmKQdzXteiAn6hgMSEDudxV6AWmeXtp4uPXErQV3Sh5CcDkytX8MetvgmZA9ZfIOV3CVSYBJAH7uueftxhxUPGjKGwwcud8vHO7CE45OrE4C8PY4odwhn6LIff25Jv3XKP1KXXEvUNF0JIV2hiysLpI7FnGZDgP1F2kqpepGq_MetLSYwjbGVaHrKeqWTMlgqjbFChJeCOf5oWZ_OTZz-au__yFksOqisnViH8uL7TzItcupcvcZhx0lf6H97o1APow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82867" target="_blank">📅 20:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بندرعباس صدای انفجار اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82866" target="_blank">📅 19:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فکر کنم اعضای وانتونز رو یا ایلومناتی کلون کرده یا پیشرو جن زده کرده، لاشیا همزمان تو همه پلتفرم های سوشال مدیا دارن پشت سر هم پست و استوری میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82865" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNLoVyNUABsCi_blaGEOyx3q9xXkji5LP1izN_eC7k7v0izvW10zvUC-IFGU0ywD90abZuR7L3mkVZnhk7DBpEA0d5E-K2DRiwTR3OaeztbJHwYwaTYejjDUqYhryELRUeIsh0ATaiJFm8BPaYU8BYHbU__c1VtAWkI9YJIfL9o25WRwdiba39PwDdwJ4pR0xHILGUPyrCdR-uAkuUyamQzVM7gN5g3rF0sYR0uiSidKDFyHpTPbZkq6ep5ZDFFtV4pyi8-3EBsi5nGyzuKZ4oEkpY4XG_H85INEdoY7fp0O8Jq_JP5mGPJe65jHEbZPFXYSckjOOWjN2LkiKiiWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگید چرا دیگه به سجاد شاهی فحش نمیدی، دلیلش:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82864" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3Gu2ZqSfbpQ-jHHYb58sWD7ekx9qggongny1CQSbwPfm26nq-Mo0sXwp3rLVl-hhP75tXNBMAlRbBqZ32kjLCsLy80W2YeoOr8kxHNYn8QtQx__06nl_5HrnJUqPwYpPqQNvH-hGZYAfxqjyA_TvXiAKtA9jM0uRrVWbc3gsM63qo8yxxKfx56Z-SrfxQwLH5YWQclyhQMUaWB11mlMfavKvTSnWsl37gc4TvrzCnPcn46ZfAX-NKC6wVpvT3JWT1ubZ3-5TKGTtAcIBybCGJvNTSIyLebj1eEJjyZApDQycOLsadZUOLFj5I-UmCK_KWqiqQjCV3NZMJ07ypagmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر کاری که دارید می‌کنید رو همین الان متوقف کنید و سریع برید از بهترین تخفیف ثبت شده تو تاریخ بشریت استفاده کنید چون کلا ۶ ساعت ازش مونده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82862" target="_blank">📅 18:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPXCVFoWmaTClccJg_oAnk-oDChv-Kcw9I2FXjqbbMPcl_L94JgbJCHCp-hCNsOsfmn5LUs605bGPI1nJDcZNI1P75B58CL5_T54Pg4DNdhDxZxGMECnT9dH7-W8cSIFIsj_5cW83f4MnqY42TZslr6SkTv1NfY0MgUAQthG8uaq-NMcY0ChPs1gFcUB90ImC-LylAERk9_dyTxHZguGIfMDoOJv67DYMdhH_3Vtchym4Aoaxjp3JBNq8Cg6fcgLDI9IbMHx5o2xksiHriLuX43UzgPIobB4kNrwyyjELCfEev72G4Ptish_OykXHT2MD4mAZgI6DSjTJHMuIugLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فان‌هیپ‌هاپ هم فانه داداش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82861" target="_blank">📅 18:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_h4YMlodvJBxXszOqIiHzykUmXJSMQXoMu_NU9q5Lzx1_1XIKHy9WcqNRUG1q-Tv3sI3mPuf9T2rb76QprZ6wiU7LT5JiYrnDPAGrxN768Lq2Fkd7vNVvik_Ej5MKWAzpdaMgomU-Qz_kM55m3J1BJI4mlJc-dV_-amhSnH9Fq0_NkED8SKFJ-nHo_3ZDodti8a_S67i7gkmux0wcHZgubk_6vcWOwlIbCCkG4ZUI3R2s6I9L8Wy0DHV5Gz_9R-F5M90jC1oID_K2x9FRFNAJoMzpsEsVs9RRUbC1BmYiAthsmPYBN1PB15IXqGSaczVq53kYueqCd10TXeFLIEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82860" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82859" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82858" target="_blank">📅 17:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسکات بسنت:
ایران تلاش می‌کند از تنگه هرمز به عنوان یک گلوگاه استراتژیک استفاده کند.
-این تنگه برای ایالات متحده یک گلوگاه نیست، اما برای بسیاری از کشورهای دیگر این‌گونه است.
-این وضعیت در عرض ۲ سال تغییر خواهد کرد. در ۲ سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82857" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82856">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان چون این روزا قمیت دلار لحظه‌ای میره بالا و شما هم که دیگه براتون مهم نیست چون سِر شدید، هر ۱۰ هزار تومن افزایش اعلام قیمت جدید میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82856" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
