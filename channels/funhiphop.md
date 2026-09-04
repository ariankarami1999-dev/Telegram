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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 03:42:57</div>
<hr>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/funhiphop/82967" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/82966" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/funhiphop/82965" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82964">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/funhiphop/82964" target="_blank">📅 23:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82962">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/82962" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اون قسمت از جنوب لبنان که میگفتن اسرائیل حمله کنه میزنیمش
کنترلش دست اسرائیله دیگه</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/82961" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmnOH0OuF624BxU1FQC8m5sibQ9OJ3n8fncOyOptkWREXX9w0BNOdejOHt1Hyrsy3eSzLa3t6LhUqJ57Tr2fVkmBafZKF-vYJXsbBgl82bwHUPqNDxH29XW4_5MUD_RK5CDOsN0TYMG-W-XLOwS_sUH2JhL9koORWZI8VZPVD4JialfPBOEhOg5Su8G6nMewVeJn3yQTEygevJPaTd3oYT0uxGcf55BUg6R60B9sOa8Q0qpgueskId1ZhhgQipshsB0HMUF7nA_Pa4u9IY2VgoZm1gm26EKZOEr67jU74Q6SDyNAGWMNKlfK-MZ4Oc1sKCbeyRJ7WXaKDM6VqMhTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکوندی شاه عالی بودی شاه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/82959" target="_blank">📅 22:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82958">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82958" target="_blank">📅 21:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8uf9nbfQ3ehDTjCHZvUdZq1iz53XY4nCxmQrnveenS6c_85jpySQtyiTVnBs3HJohTwZJf7Vg14mvw0CsUIZ2Zy4OksM7_5JitIlaXGM3bMXI1kBeKrzZLCxanKe-RKhnpzieaV_Rab3xeqMbKFNQ3F7rjs6LvTZ5U3_Zzbz8JifGxuQTqxsadAgMs1I5RxpRq0SSXyu8dka4Jq4Bl-YguramKZZHAe7OyP5gJ5LUQSlkeAfpMct3_EFYshaSwJlllK4CPs1_9iTVrUWy7FvZKVOV5gowh1SSJ1SNMOdKPJKvrZPs7-gcR-zmFwVAWtE7dXdo9sCaf6jYxRt9q3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال و پیدار به نام "Bipolar" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82956" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsaFMqlAZAbOM1bytnwDu8N3dxgKdeAwcnOkUxP-VcMNClrs7WP7fjCT7XiypKFkFMIbieicTsmom0EgVTKkVsn5mpVfG2jXuDjpuPfod_tbyNPDju_GPrWzSK7-ziQHF_65SBeA1hEdlVFcB3cFyGsICknMU4HvsxpzLpezURrgwpeE4jf7FR9JHOYNc2kzcL2LGYFifuiAIJFxWCwvgiex9krAE_EuKfqE7jA7LRIcTpoOrW5HkT0WKyFQJg_eUVGoqW0koOqr_Bdflb6GRegZa-ddChJtHjErESfPiOKE1Xkda6IujumSb5Rzwlof76JfUUV9Me7H243DRRXL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین بد سلیقه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82955" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvmdanzqfawDSf7JACFaPy0AzpIQ26jhXA8VA3ds4ITWBO5C6yORuuwN8bNDTyMWUWWbmoSf7CkijDCEPlMOdWB0q5VA1pcSP3mWzkUX8yZvovPsQaUUE1-Udy3Oa6iwwxO1cOYQ8GQorcOhZfFdDVFRBihWFoh7ZeLZuQQtRCCtKIWtIFDRCAWo7771Xd0RHwRe94QmAKhvgB9fHe7GW-h971Z9wfuhJQZKWGe_3KUB5-e0_Rk5V1hdHw3jb_GbYZpXyHDkp1SfkaKkQNY56uBAFvzHR3GypLg98HlhfxHX0OmUnnkt_gfWbV1fER58v6ql_oxwTe_RefR9g2RNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی و پسرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82954" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82951" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82950">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82950" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zmt-FwDE-WneAjzK7ynKP1vLuCgocw8-CPbEfYF5gisUZa-dbfuhyk5pR8vmxMYgys1XtGvqgW_7Jcc2Rhbl4UfxLVOzE-PYoRJRj-1jY_bOU6ZTQ-6EAMcKtLrqyHCzHWJ9uz_3bUKBmIPh-P44CpUQlKJT70Xqq1Ot7Iae0Z66odHkBwC_J-dgYg8EYl04i80fKZNMZjUOodWR-eah2ju6QnfL15sk96XFTeNa8UCq4RlcdVTqEJN7AuSuPpdPLrOCYnohpajjd3XgX88yNmaoio61Ftbr8_crbbPEneRBKd2Ya6mv2h6taiVUTwzpmKURRXnM2F0iDzEPzpWiPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام “منو میشناسی” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/82949" target="_blank">📅 17:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خلاصه بگم کونمون پارس
ترامپ میخواد پایان جنگ رو اعلام کنه و بزاره بره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82948" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcvTSJZzJncmUxCtBCXU9Lm9anG6Z5GvPQ6Yfj1A1cw-KzjrWpbASuBTWZ0cEATteKPMudjVvc4CXHVvVxr9bstmxWRFV_6H2jt7LAkQtCNCch7P876ASgFIlxzBr8odyx9KpjJjViTJ3WXX_wGvb4LhrRaiSxnaUbRl-pSQgs3i6E54qfTdmWiC2RzLm0uaEOcrQ4t1MN0dIWuUpxyJiFJmRSwVf8azLbGI_CSDlzr0J7v4lO5E8BVVebx6Wnq_FjfkzSm3RXkNZA-qCfnAx1of8gN5j3bWvhmzJwTcK7FWc89IXBhNegXflOls05vK6JH_2LbL-3i0NQs9SZ7Kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل دوم این شاهکار اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82947" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=AuVEFnNZ9Yn8NqqO_oquM7m4LwzSTGUW7TiT7VYZmmwPvERulcOH3T7KvEAtUp14tbnUFRCYPMuy6AXBAVRe1IpaF_rHWEHTOdXGg210dwHKJ37p9UaXMySzG22ycs1H2hFtbOLCfhdeCO0nu3PLanRjuyGu_g5lYkaBwVM6ogzgOi4GJKN51XiEBYsHYRKGxhBIv_BvDkZXppU2bz3AURB21m7-PxJcV9m76iAAS3fJE7jHYXwz1eatHrAIimFiXTscZ8CIZqsmQJllo-ug8PYnT8CqBeW1t-kFwTrps-yHkJSf21C5Vz3RDwWr9EbnwuzGE2ZtGFI5cz3yYOrLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=AuVEFnNZ9Yn8NqqO_oquM7m4LwzSTGUW7TiT7VYZmmwPvERulcOH3T7KvEAtUp14tbnUFRCYPMuy6AXBAVRe1IpaF_rHWEHTOdXGg210dwHKJ37p9UaXMySzG22ycs1H2hFtbOLCfhdeCO0nu3PLanRjuyGu_g5lYkaBwVM6ogzgOi4GJKN51XiEBYsHYRKGxhBIv_BvDkZXppU2bz3AURB21m7-PxJcV9m76iAAS3fJE7jHYXwz1eatHrAIimFiXTscZ8CIZqsmQJllo-ug8PYnT8CqBeW1t-kFwTrps-yHkJSf21C5Vz3RDwWr9EbnwuzGE2ZtGFI5cz3yYOrLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82946" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJBmFbSEERjdmtdCv5ws-rp8fYA6T8Uejcqu2rT1icfug3mc5N-bAuIHBDxl1HQcM7YfWZjML6nODKODdlyjTNqKjqQehvX5TH6w4JivlmtPl-rNpd_XLGGYZOJPr3AtkNj650sxtit75sE84N1IFacRlZBq5fZYC8S-bedMjcBKoYCcT9fYhyvMKVrcQ7XUruQSVdWwV72KvmC-O4E-3sj9nd68OSqdEqyyC9wQy8SbwJoFbraHZ_iRhwzM13q7x4w5eifVQdZ2iS4gs1gvch0bNpGmzglLOvIbYcyVHiYON7tPMh3sTDl8ItJ-m5CF5V7xVYiYYgOpQgbBaDHj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت تلگرام تو توییتر: امروز احساس میکنم خیلی کیوت شدم، شاید بعداً عکسای نودمو براتون بزارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82945" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHmF5j6M3f6z5idsZi--VfeBsZFZAmnXSeb1wo_-14GGRREQd-ttuD2m6kadtFvcZOOTVljvjMouBA4OD6vHkw7nifHKDErvuIrjrz52i5Z9Bb8zdf0-96jN5WLhz6mJV05g781Uo6k4FHPfQAFzAJvDv_PXqXPbNZtJeQcBxx1WZMt7aMkPHjZwS6rptnh1ME_-z11m2vKfvvSdG9738ehDfdxTAIyDiTla59djfjZy_h5XDlQiZGdlC8wOlQMBXwW6S3bhHkjMj2NMufiGyjsUSrsn0x0EDUZk59pTFAeJbn9PNhQh_9GCgF-UBUUMlK0Hd3sC3Vb0jdTfqG0f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد توافق ونس رو دعوت کنید برا تحصیل بیاد حوزه علمیه قم حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82944" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82943" target="_blank">📅 14:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حاجی دوران شهید رئیسی، یادش بخیر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82941" target="_blank">📅 14:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2N40tyGc9xubw-Xm4vIJGRBojjwj6qdJVpsWDbMGQFwhg1cHIFOClns7TyHfOOe72o2DK9cHomfJBB5CAyLcx4kO_NLuGX177LtFLccsvUQeBV62HUT6R6BVXHI6DW4Q37EQxrEwU-k41zjDe4dEnZaPgaNqcDos7qP13MPyhJslZ1gbqHYHRQ2av2fUFt_y31eOGC63M7x-v-YVSFhByCPcZhqY0qjGO3reughsP8jP5mbopRyhqeVdhTENFPCnGAhVG-SmoQqmM_Ub2evELLdGyDz0hhVrJj-R84sUqcrveZVUKLfM7kk0ZiidHF1fsna3LKvnhjGw3fS8qfNCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی از سنت خجالت بکش این ایموجیا چیه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82940" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یه گدای ایرانی تو ترکیه با  ۵۸ هزار لیر (۲۷۰ میلیون تومن)  پول نقد گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82939" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ2ocz8HYYIIaSYsioPbDALynrxTlzPA7wDrfPV7hYRJjUWAbVgZDshNAvYmAnBBl48zVX3fhTmUjpy7wPm-Jn2znbv4mVE4X0A-KvvuPV_HehiTJRKALLIvHANd483P8QoA3CZGYle9rcpxF-J6vS3FDR16KK_5K-8u5V7iUVm9HYrd3ftQSqIF1SXjWl9Uy4pTs5X8Z6477VkQoHljtXzrESdPfXbZvNjGU9WXHTuPvKW89Ivi2Q7W38SY9rFPQ_yX1lNkT4ejWhUTu2ogouhdlQow6_45bfQLuyOTwNEzLGHaI0qKPEziLnSmlCcHNJY_STzBYJQJmnTHojx_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=t7AIx0uKns3jMahKPLThh8i5Pnu4tD-2SsXg2TK-DiOOgTVXJQngu93-dI8Uy8UiG83olr0CjYq1E0soa5w2DRVm-1oGUU094N6Kd4Q9MxuFIk01j5JgAusWu4Rz4LGgodsUnyjLAVg9LkTri3qQbE0rhBYdb4KZPqpngjBjcJs0n07lBsNhMcXXqOWy9nTXmrIhVy1QkrEV4I8LgWXiZKJjmYvdvBHbePwRqJQjVAaw37XaaZXyR84fl3-5Bxfi7MvGl4SdqhIqtecgSCB5di_d7QJ0Gclmb8M_XbOh5kNrA93TT-cgpqpxARGPRQMuKq8wtbuC6A8ltnfIjL3K-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=t7AIx0uKns3jMahKPLThh8i5Pnu4tD-2SsXg2TK-DiOOgTVXJQngu93-dI8Uy8UiG83olr0CjYq1E0soa5w2DRVm-1oGUU094N6Kd4Q9MxuFIk01j5JgAusWu4Rz4LGgodsUnyjLAVg9LkTri3qQbE0rhBYdb4KZPqpngjBjcJs0n07lBsNhMcXXqOWy9nTXmrIhVy1QkrEV4I8LgWXiZKJjmYvdvBHbePwRqJQjVAaw37XaaZXyR84fl3-5Bxfi7MvGl4SdqhIqtecgSCB5di_d7QJ0Gclmb8M_XbOh5kNrA93TT-cgpqpxARGPRQMuKq8wtbuC6A8ltnfIjL3K-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مسی که قبول کرده GOAT خودشه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82937" target="_blank">📅 11:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw0ejteOcedTZg98ClYVKTgaOEZ4HGEl_YF-LquxpCg6uzhgrj5OJWi1dmOLOP-Zev-yFlP8G7SvftsWsI9geLuaplauRwSFL-Iu8dP2j2OmLlJsHgXPGqfMsrRyfMlvOAy_pmadn4TAHl9JoHExeiVaz1R_Wpn3G-vPfNM0ZcEZwOb5jWgV9_eid3TQKmGhUTBvJisKtAgpzhOFvQqfrX119zhRfM0cwONcSRYlhxR2fK55-HjYYTRIjcY9_cKRKpB7Jz6LhUtz0_rE_pxY_agyiXDCP_PtixNAr-V3drwhq5giYsyRf5UgP1SiZLktK6ik-m0u2jrfc4J2bFvZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام اینو توی باغچه خودش پرورش داده و به زنش کادوش داد، ایشالا که خیره
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82936" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9K4yFkS3Ba993IxIigrVyaVEbmHBD9r_tSqTALLqk6scS7JOkuRUHKM70UazhM8ErCIEufAmYM2Q8xV1N59o9ttZ17aUdQEQ7hZ3mcLj8rXT8hfB1lkXZ8R3yQMOkNuoq3MCxWGP36o0AY1R8knRywISUR4fa6jCjVX_RJ044PqLbtDG_RLTtlMNqA2dUbEOMEeFmHhSJ1tpnrFWfaQfjpnzPNzYo8tFVGfZ_E-bKeFDwYnzvivMUc8LC9sJQnyCe86Kncm1TDO5v05vjc2WGiYwgzG6DveLf0lxxYbas3XldaLozw-B-ktfEXct5F59MfT8bNIOIe8McBj3jluu5mY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9K4yFkS3Ba993IxIigrVyaVEbmHBD9r_tSqTALLqk6scS7JOkuRUHKM70UazhM8ErCIEufAmYM2Q8xV1N59o9ttZ17aUdQEQ7hZ3mcLj8rXT8hfB1lkXZ8R3yQMOkNuoq3MCxWGP36o0AY1R8knRywISUR4fa6jCjVX_RJ044PqLbtDG_RLTtlMNqA2dUbEOMEeFmHhSJ1tpnrFWfaQfjpnzPNzYo8tFVGfZ_E-bKeFDwYnzvivMUc8LC9sJQnyCe86Kncm1TDO5v05vjc2WGiYwgzG6DveLf0lxxYbas3XldaLozw-B-ktfEXct5F59MfT8bNIOIe8McBj3jluu5mY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82935" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQI7rWtUEC3fEwwytSp3MD8_0AWe1be5CgYhlco3U-rGjeVv6ixwL874ugbW56CVbn82fRGtO5iYbf_6zx0FQNp2UfLzVF_a1lJd9hiQ-HfF7Od--xqCS2Ta_V184XwXVBQvXBZXPhY-ILY6I1NayCQxSjzoiNC-xgHnwhLUiUnDExl9cZW8ffuyxndWYKkdWxvG6uQqAt8CpEbRg4KBgwH0mnJwEC5UD8-kAlZh-GIf6fGcnnm-_02BmZSMlw-1GbN4_ZG6hRb1DKUdFvgVAh4sCuIxGRDG1VGwoxkrZBI0M9CXajQbGli3OzBwS2RQ-SaViGtGSEkUdYpxO5oFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرسی نکن پسر تو تازه ازدواج کردی
😐
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82934" target="_blank">📅 06:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82933">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82933" target="_blank">📅 01:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgbXhu4pHQTMosKv1ZIpKAvCWnZpaKIHKbZROrClzwPflOk7kBA5rFQrYCQYzGSiCLwe6MzdLhZGRNlie-uZLajZgmLds-li3WijW5YWSxal84rcb8kvH60MnPyENKTzb0y3rvvU1BDZ_61bQ6UHnIE_0X4gjQxSRK0XmYEezh7Ue60oBK-PVHrfLt5lPkx3DYSkEP1-vM4X1pq8WMpa9K5iIbT3nUQU-rL7MA575RmaDrtFgpSuh_cJuUacC1hvkq62sh1VrVHn4jCfQ6LrI53Nj-oOFHx1C-bP6Acw_Mt0XIJozCU5p2xuFdZhyXvSEByQ-9IOS6dcjzAVbB8-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش بی‌خیالش شو نصف شبی بگیر بخواب، اون بی‌لیاقت بود تقصیر تو نیست که، لیاقت تو خیلی بیشتر از بودن با اون بود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82932" target="_blank">📅 00:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OngZYvSns3POk1GgSThoUpuUFJww2vCcqMP6KS0TNdL95jd0ud31y6qbWPt6wSGwSqnwfV2mWyA19REGXUVqEtOdS6XnDI__3LEAONUXXA3V4PzKbSy1Ei56I6zpBPocJiOyuvoBFtGie-IL9-fTwE8KEBrwbpDEpihb5MgbuxwzTD2HtoxLuq3Hbz_gflHHXB72k6aJ0Cu10URTg_ukTDFqFdggtRGXCz8_QxOgfh943aFcc0X0SmSvjIynSbsy1zQFJu3pZ3fpLZgE9W9PZmfqektaBNaaj4zvPgoWzY3mQj57WEW36KlAMb7eLX8WFRJq-v9iX9rMzZSppFY5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۰۳ سپتامبر ۲۶
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82931" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf4r_mKQpkKrxvLskUYNVp96HCWkSTFu1KjpjhVAsBFq6yn20QAQc736hjYSZ1VzI2rcSItjwR3FuWYr52c2G092MyZgs4TPmcz8DRfK3aDa03knkH_nnFrwcw_OHNlH7-k5zAF5ptC8FflTAp13U9CFAtF_Z--6VqsyNn2kV0pQEsvIPyJKgnOx2Qtm0UiSjsyQZdy6TpaAxVyRQCV0y1ijqIZ4NLup2LJeFzoHsA8rUr_933JZ4VDNbpxZTCGIDHAaqPfDcvugdSNSKfO2U3OEUlb0hrBcx9gRb25JRmxOFyg-5oyCNkVUfcZ9K0RuPNLmkSAH-Nsbcqr1M3gaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82930" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود:
عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82929" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0ZO79EdjwmRiyIOvhEDOuvnaPnGphZxkVDnvuoFVG6OXky_MSO7wapY9CJpsui3yKM4_OYX3Iqk4ielzx_yb0swr8cl4u2PlTswI18-2ojeIKUbVReI2wdDHfuYztP0INCbIHaznrSNC6tJ8iJmwksBaMDiGCCiGVgEtY3pM8pCAePneWYK9P9wLOq0rvYgjpNbcCqE82FsvwhbwPJoD7ILs03VQzU7YxoIkACkVsG8S3-O248SgUSir6KqdnFsGdhJsoTknPFHblO7zjuNu0kLrkky-jCxIwfl23q7Mnbi-yzGclfjhNE-jB546nQ2ypuFJViesjq44xqo9dUQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این پزشکیان بگه یه زمانی همین روسیه نقش آمریکای الان رو داشت اندازه دو تا اصفهان از ایران خاک غصب کرد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82928" target="_blank">📅 23:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پزشکیان خطاب به پوتین :  قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن. حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82926" target="_blank">📅 23:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82925" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">لطفا موقع بازی های حساس دنیای فوتبال، شو های مهم و حاشیه های بولد قیمت دلار رو ۵۰هزار تومن تصور کنید، تا کیر نکنید تو مغز جوون ایرانی ای که تنها دلخوشی هاش همین کصشراس اونم چون دلار گرونه نبینه، نکنه، نگه و...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82924" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سیگارا وینستون جدیدا بوی پهن گوسفند میدن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82923" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ4shZfqbWD0xUDHM5s5GmQ9szD2rrsJE6aIDaKCafqEHMhE9vFnjCCS-q9RZYuJcYx2tSHGcnX5PiKeR2KAF1yCEf4evq-osdRTDTDTDAe7IetFjkpfx8oHJEVBpxHnisjIWjBJv9YuKFuJBgGwKpx_DAxTVYSNhZne6PxPw4FgwAAJyOwNOw3IywNIP6xLr_L2l2h2nTyVdjxxFjN9kPwnLC6nkHfbZEP7ixG2vW2eE0n3wI5YnaoQQ1VN9rItxMb9ERdTgBcGzWWwdEfWWbO2faRd2wJJvRX_ABHy37rhF6WJg-L3PVI0zeIrFICDW68oxUfj51bAjzSJgUP0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUUmHemxe9lO2YCx05-JXbKxoMIc3TIOJ6TUCvyIA9kSPcRWclnqkbgXuvdYb3k7hIJxRY-P6LB2nItdSOit7c0tbw_cZSPJ-A6NgRqOV22qmq1c-QykxSOimJqV8jwguiqX2bFKEHC_HLNKlJym4uTKwakkd70B9Y-vbosgMRt9JPw9B7Imd5cXitrSrJXKI4kmu6qcuaeC9k6LJvv8xkMG18zITk20Q52JzylgN_tD7y6mleWqGhQ8wFTYiPEvP5R9MF7mHk0ASgrzPC31iukzU93LZ3fgsiWEKUyn57M55nwqpn-BSZPd00gO6Op8k-FdoZi8oMsX6E4LzBi_wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید لنا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82921" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82920" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">چقد غیرقابل پیش‌بینی</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82919" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">0.000000000001 ثانیه فرض کن لیگ ایران ببینی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82918" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این دربی با اختلاف بهترین دربی ۴ سال اخیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82917" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چه موشکی ول داد یاسر آسانی</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82916" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82915">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82915" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnKgMwqxNTf6ZYEazAxD-MVDH6IqOMfnSimmBeJXNr2b2aCwRycBx4Nd4gx2SCUU1QmX5nKCqDkzIEKP0rX3q55wMn8fMRzpdxSj_KeC5QG1_VBY8xTs2Og5qlbfrDVLrktPlsl-FnsTyoW9b2wfWzDFyPG0F93OO-ptgGYKRp94Vbl3pTyEs-czhhqbFRWbdIY0TL9YVUTdgbWeFMi6CZtb7rroQVcqJjzvh1qB8xQi6zJwhdZ4i8-NQVx0Bh6gKOWfqHGR7YcPHqTBPjhT-Ewgnv0IFubN5rkBxuq954ktkSiHMyfy6aPX8pIPPkfADYNYqheGbSTLwOLQ624bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82914" target="_blank">📅 20:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb-JEqB-uXCOnbKYdnr-4Mo8G33surbSMAh7C4dO08dE69jcPi-8TTtUqRkFKzzCkLa2LbpJ7ej5SsEltONZcMkbpusqxi3cmo50Zij4ADZT-0dXnYyiRMIlGlRzxrU19rCfd3C-wbSp3oERdbys9uXzem1Dox_RhRXLiouSQa-HKJLIvm10nFxJ-btQRUOvxmPmrqiGgF1d2S3RkXEzrnbH7y9tXEaq-n_xBsoSxlT2_21EmAgY1iXiuO0uThYULcfuO-kWNvkm_3I0rsu_PU9ChBnBLPKnd2KamnLTeyGbJHCCKFu2r9sUZOGNDk5BqTDl_H6N5TtoPE-CKyXvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکو ها جذاب تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82913" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqcFnlj1jGdIzepqYjHg70n1z5Af8LIN-OvpjWVuBTRqVAm8d9e0TXn_0Ed0kq7cx6Y4ud-3fxmuod2GrfAEAdWfy0sI9af3CLBakP17UV62BOURn2FifkhrR1IMv4p1C4P_Xsi5HGpXFARtwJchO0_G__zzVKJpNTyGv3ddeUwsog0fXa9THbPx6xv2N3-XSkpU5f6JgIEcLPXlxuO2pctxSmjc9QywJG0N-AAwFNdtwoQXEQsTeMuoN_zuaAfq2kwQf2bkTBWuNHBF8hiYhWSgqzqDo5Ai6JMKnvPRBCmov15YMv3zZvMpZfrrCfHtzZsfdaqdeVkQ31SfqQmipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت استقلالیا از دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82912" target="_blank">📅 20:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پرسپولیس از کون آورد که نیمه اول مساوی تموم شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82911" target="_blank">📅 20:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیرانوند کص ننت</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82910" target="_blank">📅 20:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خلاصه دربی تا الان: آقاسی به علیپور میگه بیا گل بزن علیپور میگه گوه نخور
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82909" target="_blank">📅 19:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">علی پور
😂
😂
😂</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82908" target="_blank">📅 19:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">موقعی که پزشکیان زنگ زده گفته دربی باید مساوی شه صالح و آسانی دستشویی بودن فک کنم</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82907" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS6gGjS2upJ5IwXrOj_ZdNdgQ_mbZAQ3fZbhEjP2jAqTLg-dM0eN8OaxdpinHZzORE381DiaTjxI4KgWNjnukg4Yg0Bt-pPR7A5Bz-65dZ1WkAALcRY8EOItuOAH0oEMC3S0iym4gS_vAlHb466Owg5qpKo-D_5cMTuBLMDzf3eJuzjuKaYhEWdaw13fHvSnBDG1Y0qDwr0tdbpGMFr_lzeiFvmUfoTgMLlGgbExwc5uYQqf4Yq2P3Ekj8Ks9VB2zP465pETo8YFBYOryfOI3HDc-U9sH8MG69N_u553JsChp3_mHb9xBLTl9C49Hx7KmcmvkryP0D8BSW96ckzdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا مناطق خاورمیانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82906" target="_blank">📅 19:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82905">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد    YouTube  Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82905" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82904">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS00zIju2hyVlcrQCXqJAoLBcS0KeU8zO-DGBsQqaN6liaLo5lkpHe6Jk4ZgIteN75Vix2bH97XKpUC3YzBfB7YMqnCqSQcxzmEt6q803Ypkzw3I5HBS4BbAcek1ZqZqhFz2zTOazhvu8_1IfoFv7XJkg4jf74P4rV1XS-XP40_mw-ZvQT99PWiKNrVo5KaLx-1aLvUyS3GkPAMjwcvhk6cw8SngDTnggVXi7D3_KPaPhCrfWTrbddD6IDTMLonZiHl9UNd5RnI5nDKhXEybo0sSegFJPolJYJMYO8-UoX85cdM_Fhybr3QdMRq9CFBAyZSb7BQPOcDMkTmPWfNXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد
YouTube
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82904" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82903">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آرون جزو معدود دلایلیه که رپفارسی رو دنبال میکنم هنوز</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82903" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82902">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82902" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82900">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aBY9_-EV98voj06QM63nw5iW_sJ1__TvcE6RJZAvuwY3OwyfwS05Q1Zb8ZASr1FpzdzQayAfSl634z6eikzzOYjvl6T3SH1e0JTAnCrMDdufnxTUprWV_jmwY-V4CIGgptCMjyFc7xvCTrhtnTv0KJ5O4iLCdYpqtgD_CT_WM8_tYRbS-Am0BrHih6GyBuG0aRp8jQEmiOlD-UBVHb9bSiW9ZxzsWv6hJFXGaKL9ybr0ruHpZZV413IF2XBAqwx7ANw61qBgK2-Qm-hSSV2BDV_-A-70U7hjeSP3KSb5GM4faVoGoMsec-2NeWgGWTI7J2qjRgiR1IKBDXAIk5hHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5Z-M2mdE9BqH9me83nnpej2osBs5N5CI2hsL4Xij_Aig-YIgSFwgQ9U1lrJBCFIgPN2AT0L0kJs_lwThlgpQnSmDQFrSZkn_y_--26n_OHvVa_ULGfeuSbJcIk4ticzYVnUrtu-8YW8a9wX2zZXuVab-INXuErGQSH__wPbr2WfNQqIXLFCpzw16z5SKejNLqNQmxXcuUT9_sSPkUYvsWMpoZYo9DqepJ1-8LrhgldO4CGnuNmT6G7GlnWV4SHDt5YA2CdikyyTjIvYhVhtLuGKia8aOYZgTSTR_ESNdGwnFEfDDxv4bfExVzv22LN6_rUSZMd2bkBMU0jDxr8GoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82900" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82899">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEAorJWLu2IYRSXOmbgPKwXBhI15yg6Q0XOgE0p05H1hqPsOlmTUuMKgns707qC6B-EGFUdHKbDKPc54UapFabk9_-AOmSECM4mvmKsCI8HFNV-wq-IA1SKuoMGGvXRmbZaN5Vje4zDp3jxC-TTKVippUWGggSwghf32A3mg50L8wQtjFTaeGoLu7Hw5JMa7pFFesS8A4ZQmFBTh5Rn6g1xf71WGNecBZJTRo48kpvSfUE_CgY4-Qq29F6BGdnmAcqeoyQ259KWzzoX7xcca6KIqU8p-lKw94mPnYESsw6jcl1knaTVCkQ-3qLk1DL7Z4kY8blTVbRYUbhxx9qsKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استقلال
🔵
-
🔴
پرسپولیس
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
چهارشنبه ساعت ۱۹:۳۰
📍
ورزشگاه نقش جهان
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
استقلال
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
پرسپولیس
:
۴ برد، ۱ تساوی و ۵ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر استقلال: ۲.۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر پرسپولیس: ۲.۶ گل در هر بازی.
🧠
برنده واقعی کسی است که بر هیجان خود غلبه کند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g11
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82899" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82898">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جدی نمیدونم تا وقتی رافینیا هست انسان ها چطوری میتونن فن بازیکن دیگه ای بشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82898" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82897">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPPlhEIZlupnAkKzwKKpkEYeOHWjKXJNd-4ZD3_8jr2ajMl7zp-MglFr5f26bOCE15a_qt--s6b3IHTddEs1MoKqOMIKjgtQJ2qZcYpLyM6Wl9Sz3NS1ugbS60IIA9lArs8XsKXwpkKNZbi3seG6zTIbzz92MDiHYBEggtOKtsV2stBZd2ZaN9tf8D3KGZql6dzalz0RwNfz0ypbxdzA2WGuN0_pxaUOfgxcLuz9zCey0lfFa3nwL5ByKmCNDJZo_PHOaerz0PRNw4BC5JB-pDkuUR1Ej7RsjWrdrpZii76owWMjvqt-CPVpaubD1i5AIqZv4ca5RYuRGHndjPzdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82897" target="_blank">📅 17:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دربی ساعت چنده بچه ها</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82896" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82895">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خدایی چطور هنوز فوتبال ایرانو دنبال میکنید</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82895" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82894">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82894" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82893">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شب هالووین امسال آلمان قراره یکی از ترسناک ترین شب های تاریخ خودش رو تجربه کنه.
کنسرت مشترک عرفان، ریری، هیپهاپولوژیست و ایمانمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82893" target="_blank">📅 15:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دلار هر 10هزار تومن که گرون میشه ویلسون 10تا ویس میگیره میگه "شما رپرای اونور آب اصلا چی میگید چاقالا"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82892" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امروز در کنار دربی تهران، دربی شمال هم بین نساجی و ملوان برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82891" target="_blank">📅 15:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82890" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itCP0ta-N564ymxcwMcA_WvVpw0ktZF76QJpN5CI_t_RW_hs9hkeFyuCgdxPCdtoy-X5kpi84VV0tr_2h6gMUjFYFWR9jrQKx_rAK3o19w48yTTAAv3_7YzP2WBkzD3vpdhOmQuAC_pzFupZtWrljnSicVAI7Mc8pe2Jl3cUjRrvIZ9TwE-Ec8N3gnyNiRB47mdlkfD4-N2srASzCEk0ZJt_wc9PrECf83oWVecWaeqCmf2DaQqzNzYqXtjagZAziPu59PTYUjsimqNbOkb33lWSmnkTvQ23lWbC5wbVMdrP2adv7jXFYVOAmf-Q1MSJ3hGHby8Mv6GlRc-mCWGJIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82889" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82888">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فان هیپ هاپ بابت تشدید تنش ها در خاورمیانه ابراز نگرانی کرد و خواهان توقف حملات نظامی شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82888" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شاید باورتون نشه ولی زمان اعتراضات 401 دلار ی چیزی حدود سی هزار تومن بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82887" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5-e_m9Aa3_9V3FYqLOgrgQnIi96VTpjZdHEhkEhoprSXb40pf8XiQipL6Qj4Ui6H7I9NXm1xLmjzhNU3IzVOEFPTxw3k98JW5Mj2C6AWCejrR52haFV1F9njsn3DKwY9GYY34WhbnPH6t3GUSf1KWZ3ddnf7PjC8qmdJgtrlVW_1w-VC2r1oyAhM_me2TX3cb0mV2b0kIF_xtQKKA7ape8bFMuCfmuReMJMNMlCnoWrFGNRDD-OB_kyZPfe_QQ0Su5qjr5KTJH-UCdDHl9eys_nFIu4XdFOP7Pm4FMh1ksRABuDAtKVxCGLNwvATkXuaVmnEKUCujJY2kHKUh7jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مال دیروزه امیدوارم الان گرون تر نشده باشه
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82886" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNDi59Nm4AlVi0rqgCElqPfrXATwaI5j9uYqcQMxSAmeWXqrkzdzqRjtwm08zk7lzekPznrQxaCq1GOJIotuJ_1nthI8WhQtt81e0yRFmi_m4an68SaXHMRExMbmk6SlPb3PS-LMmg_3Av07Gs1DzASaQAG96sw9U3PC4-YBsuJ3yH9I3No7AfInBjLd6x6hkGW7vakaiFHbJV8N5ZpeZoBNqszQEgR3FEkcw2mTgvugcOLT18d-BD5NOGdQI92VfBX-y8by_-1oOmOCWG61P6JQ1lvHukehWvKHcefwp0jX1M4l9d452bipZlaVAufOpeIBP0_1wW5gp01-AARsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استقلال
🔵
-
🔴
پرسپولیس
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
چهارشنبه ساعت ۱۹:۳۰
📍
ورزشگاه نقش جهان
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
استقلال
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
پرسپولیس
:
۴ برد، ۱ تساوی و ۵ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر استقلال: ۲.۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر پرسپولیس: ۲.۶ گل در هر بازی.
🧠
برنده واقعی کسی است که بر هیجان خود غلبه کند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82884" target="_blank">📅 13:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oibkTnt7dmank_QI_7RoTGlni9w_UEBJpqqkpfV8Cd7ERJr-B-2jbbxRDA_eleHLVeJtHdkNL1xh6S4lFtx_BIkNb_nC_sCtR73QtCbhK_6NCB0kSvwiP8FkTt6PUyQUfO695fBfgqsHw4H285iczwK8zZzsJCDE-mepZsbKO88nfkzVcSoeVzTVzVawIX9Di543X8KcWkuIQRiPqHik0DERRXmsXrTaVNGtj5QKRChAVLJAK3W3hydDzQf4xfbOIAEDMOYuCrPsYnwKl_XOJl-0cbr3vFp-9OC6385ZJASgr_dtGhB0GzMtSmP7fNnY_DmuoI1tK7u5dutYiFr8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان حاج‌رسولی‌ها و آرتا میرحسینی به نام "مست سر صبح" ریلیز شد.
SoundCloud
YouTube
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82883" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دلار 222</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82882" target="_blank">📅 12:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_j3UmyAlbhaT28dqBD48hyBPAj-1lbmmt9yRYbw_jStrqIwWvFu9z_R-R9G6VP5cMfwS_s6F1l-VkjKdYB8v7Cts2GgzGMGT5cURwOtzNBYGnxNC0XrVzj6QlM2YBlxkQk_EgDWYVxSFWVjc7jFeDs19LTHUBNJ0uD_9WzPa5OVGQGUh_HLEK4-05bG9QZm_MAv-QZT1vTWyZL3Oh74USjtdxctLTK0TeCD-XYh3pYedsXxBnBRXBJp6jxn1qQGv_t_dibCit8Vj2el9uYhSiyTXCL4yFP9QQq4ZCJkPvZvmLGxb_tkUKw70BS-WpiSLuyb2ABpXE39CDpZQSv0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیب ندارە قهرمان، تو همین ایران خودمون تو مسابقات مسترخایەمالیا شرکت کن،با ترابی و بیرانوند و خلیل زادە و علی اکبری رقابت کن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/82876" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdkYDFNOTJ2O63E4z8lcjV24dkdm5kImP9-_gug83Q6SuY3JNQUgweQvAS4N9KMW_O7CDI_SdswyA2l8qqmLgSYB6l1_8sR7UIW1s0kTWTCNJrALTL3dmOVyvye0WNwAgGn46sNHvE87GNB-NhSd3u7-iKuK-pT4HxNToi_v2zgJ4dRb5eInzVmeKth1n_mjaKYzM97rswn69wt0cdU_4De1YHGC6ZXpBMEQH0giNt6fiqlz8UiDaOaLSl-hbZFi_GtR1V3_NcKIudmEU0yzXxZiHobRZx065QKzySAwVKGEiKjgjY4H4KWOxUOCWVogTF_uSPCsnNw7T3VuGIRYKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82873" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82871" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82870" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82869" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.   Soundcould  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82868" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82864" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo7S-0HpK1AHu4ERdH-Juq9n_xhmsyTgpsR0gaBKrhAuH0kXeu8mcsTbcDNlWPs0f1LWlFiwM6jiKnOhbS6NekoChtukIQhWKVQfVRfj31LmhvxShbDiyukgRkvP3sthCj8SKL-yO5U--DZrRKE636OB5jxOjNYq2JJi7mi7XZHDAA8VMda1Eixs6PRxWzRRsGHoep2wn-zVXB9gNHfGmF9MyHgk69rOZR4lLRDSMGfs4rtdlt-1VL6dz39qCTDZwDzmm-UGyOsyqbC07chfmm6Rj8Lp1VIT8pM9WSHiTEUsHrummVfRiOJA5FV-HbMFXvCFLARiTamFBE1MgYHw9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82863" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3Gu2ZqSfbpQ-jHHYb58sWD7ekx9qggongny1CQSbwPfm26nq-Mo0sXwp3rLVl-hhP75tXNBMAlRbBqZ32kjLCsLy80W2YeoOr8kxHNYn8QtQx__06nl_5HrnJUqPwYpPqQNvH-hGZYAfxqjyA_TvXiAKtA9jM0uRrVWbc3gsM63qo8yxxKfx56Z-SrfxQwLH5YWQclyhQMUaWB11mlMfavKvTSnWsl37gc4TvrzCnPcn46ZfAX-NKC6wVpvT3JWT1ubZ3-5TKGTtAcIBybCGJvNTSIyLebj1eEJjyZApDQycOLsadZUOLFj5I-UmCK_KWqiqQjCV3NZMJ07ypagmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر کاری که دارید می‌کنید رو همین الان متوقف کنید و سریع برید از بهترین تخفیف ثبت شده تو تاریخ بشریت استفاده کنید چون کلا ۶ ساعت ازش مونده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82862" target="_blank">📅 18:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPXCVFoWmaTClccJg_oAnk-oDChv-Kcw9I2FXjqbbMPcl_L94JgbJCHCp-hCNsOsfmn5LUs605bGPI1nJDcZNI1P75B58CL5_T54Pg4DNdhDxZxGMECnT9dH7-W8cSIFIsj_5cW83f4MnqY42TZslr6SkTv1NfY0MgUAQthG8uaq-NMcY0ChPs1gFcUB90ImC-LylAERk9_dyTxHZguGIfMDoOJv67DYMdhH_3Vtchym4Aoaxjp3JBNq8Cg6fcgLDI9IbMHx5o2xksiHriLuX43UzgPIobB4kNrwyyjELCfEev72G4Ptish_OykXHT2MD4mAZgI6DSjTJHMuIugLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فان‌هیپ‌هاپ هم فانه داداش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82861" target="_blank">📅 18:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_h4YMlodvJBxXszOqIiHzykUmXJSMQXoMu_NU9q5Lzx1_1XIKHy9WcqNRUG1q-Tv3sI3mPuf9T2rb76QprZ6wiU7LT5JiYrnDPAGrxN768Lq2Fkd7vNVvik_Ej5MKWAzpdaMgomU-Qz_kM55m3J1BJI4mlJc-dV_-amhSnH9Fq0_NkED8SKFJ-nHo_3ZDodti8a_S67i7gkmux0wcHZgubk_6vcWOwlIbCCkG4ZUI3R2s6I9L8Wy0DHV5Gz_9R-F5M90jC1oID_K2x9FRFNAJoMzpsEsVs9RRUbC1BmYiAthsmPYBN1PB15IXqGSaczVq53kYueqCd10TXeFLIEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82860" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82859" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82858" target="_blank">📅 17:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسکات بسنت:
ایران تلاش می‌کند از تنگه هرمز به عنوان یک گلوگاه استراتژیک استفاده کند.
-این تنگه برای ایالات متحده یک گلوگاه نیست، اما برای بسیاری از کشورهای دیگر این‌گونه است.
-این وضعیت در عرض ۲ سال تغییر خواهد کرد. در ۲ سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82857" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
