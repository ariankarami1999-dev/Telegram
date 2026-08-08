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
<img src="https://cdn5.telesco.pe/file/tqoMP-1cN6sKFKE8UDgwcbpSOXklCWtoCaa1nzb2dcMx2BoGSfOmZGWQmVj_Hd7TBB6YIjNPF1cwY9r1R2pz_TMEMLbPl_gtBqJJsZrU7sGBHHfubZonRmizFbs4JIhptf-YtztRxci_lEfRGFfLJWYNshxZvjc3f9MetYRYBXrBBiD5FguQqtuXxDinCneC6lLHqt22hkxeUQ336Q60MgcZVNO3JCVLMtYK1GIUgKHJY-pk6Zbn2Kmhlv8N9goHOqTbPeuCzxEQiRQBTMoaDUZwe2DO3t7VuPUavAlyb3QYjhQ940CQMK046GKhH3e5ccdzgPgwY3E6kBrRZ3-fUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 485K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 16:56:40</div>
<hr>

<div class="tg-post" id="msg-103075">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsuj25SzA-uSfBwdVcSAe0rfp1g-hJSS-ckQbQvRxXdIsGbLE4zW402Vvwl_vpQeUPW0S-ZFG6gcLNNwIIHkLkzXGo1XQzPg8DTqwqQBIoe9YgHXaojai-eMcPNLKDLNJQaDsamH3qv7SeVv4e4mT3-I1QcDIz7pg1Za_YCMyUxV_0oH2cIT670ujWME0bzKye1nIJzaYUxhIXgLAQtgkllnuqfx2PkEWpmC_zNydtxxE0egg-BMG9vED66qNynGBRuyz7XmPPrnXHYsd_MoRaZyZENe4QFgxF_MygqfM0P4dUs2kj1-aYdlNwdjgW4Ns5c48nAM2zb7qqdYBH0Ihga1tc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsuj25SzA-uSfBwdVcSAe0rfp1g-hJSS-ckQbQvRxXdIsGbLE4zW402Vvwl_vpQeUPW0S-ZFG6gcLNNwIIHkLkzXGo1XQzPg8DTqwqQBIoe9YgHXaojai-eMcPNLKDLNJQaDsamH3qv7SeVv4e4mT3-I1QcDIz7pg1Za_YCMyUxV_0oH2cIT670ujWME0bzKye1nIJzaYUxhIXgLAQtgkllnuqfx2PkEWpmC_zNydtxxE0egg-BMG9vED66qNynGBRuyz7XmPPrnXHYsd_MoRaZyZENe4QFgxF_MygqfM0P4dUs2kj1-aYdlNwdjgW4Ns5c48nAM2zb7qqdYBH0Ihga1tc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تمرینات میلان 2002/03
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 617 · <a href="https://t.me/Futball180TV/103075" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103074">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5i7t0fjUxPE9LtIi-fP_EObH1Z12caCKFAaI1xY1FHObBh7BS9s610el7AGrjvvkdU1xHBC66usqxf1iJPPG8ggsi4MQE3FhY8XQS2vNBl8dT7jLdV3OxSH8FXt6I45CmTy90Gwt-bsqPmJGWThHWXQ5GZ91wfgF3C4-e6jg0HZLQ5UPbz2RT4A5l-ulJCsLaqlx5LfZWV1_iJmSzNlXih2z_dlE7a69MSPVlrbGisFNFCB82Ca4N44Xo5bJn5os1_6fPCMW5CTNxpvcA7kUNo2MYBOs1Vm22Wz1jhpXyd5bQCQ8buC3pu2QaeOBVOhgqntGCKVPYzbjksmO1Fs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از ویکتور ناوارو: بارسلونا در حال بررسی شرایط جذب لاپورت به جای آرائوخو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/Futball180TV/103074" target="_blank">📅 16:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103073">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=MdoZCPuFxWcuN7iU62ctahZTQhAotkVtuLyGrJI9bcP5SPipwMeegni4VbOXY80S8MsQEJZqcNKCfQFd5f1fHwpTT4yaf29xTjovhf8FO28IMqpa2VDUdr_wtprM7AvqYy7FkTqyQ7OfiseoTFC0ifZSHdsGMwtovlGOfMbaWNIC_7M8dRHFb0a4CkDa5Ne3W5OtdDZvE1iYjbD933fnYhJ-qpTd5bXyNwEEshGw_XPqh10WUiNPn4RICVwiV3upyWReI-a6kQ0yn2SSuD8ox8D0kHW9HyM5hcz9zm8dY4t4Vpxe7GN-Psvkru_HvXijwoKNA9RoCMsfjTZK05lcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=MdoZCPuFxWcuN7iU62ctahZTQhAotkVtuLyGrJI9bcP5SPipwMeegni4VbOXY80S8MsQEJZqcNKCfQFd5f1fHwpTT4yaf29xTjovhf8FO28IMqpa2VDUdr_wtprM7AvqYy7FkTqyQ7OfiseoTFC0ifZSHdsGMwtovlGOfMbaWNIC_7M8dRHFb0a4CkDa5Ne3W5OtdDZvE1iYjbD933fnYhJ-qpTd5bXyNwEEshGw_XPqh10WUiNPn4RICVwiV3upyWReI-a6kQ0yn2SSuD8ox8D0kHW9HyM5hcz9zm8dY4t4Vpxe7GN-Psvkru_HvXijwoKNA9RoCMsfjTZK05lcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب بهروز رهبری‌فرد از قمه‌کشی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/103073" target="_blank">📅 16:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103072">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=ExwFDH2G1eg4o2IbQ8eE0V96T6mD2BCWUFaEOgjodrd2VLomrVfdZX8-12v6JBrzVqRwNoS4Swfnknk6skucUpqlMUJJUYdR7XLpG0mJ4NIhYGCQlXq5Fxi2Z3zEQj-9BODWp_uV16g2AF88_6OO1KXyKJFHJL1_8BhN6Gg1esxX-FDytNPVWHFCc7k_gnaolQ1VJg-zrb78NvDzr9ltUcn6_XAwMEuVQ9u4dB_z0L75WXL6o8KpBW5d194-HVyLDDQsp1OK-0GMYIhwYR9qtmFE61pPYDSL_AsSaB5fbOQtvBphyQhAk-Liq1wD6hLY8dIg2hX_UkM32ZC3Sm8nSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=ExwFDH2G1eg4o2IbQ8eE0V96T6mD2BCWUFaEOgjodrd2VLomrVfdZX8-12v6JBrzVqRwNoS4Swfnknk6skucUpqlMUJJUYdR7XLpG0mJ4NIhYGCQlXq5Fxi2Z3zEQj-9BODWp_uV16g2AF88_6OO1KXyKJFHJL1_8BhN6Gg1esxX-FDytNPVWHFCc7k_gnaolQ1VJg-zrb78NvDzr9ltUcn6_XAwMEuVQ9u4dB_z0L75WXL6o8KpBW5d194-HVyLDDQsp1OK-0GMYIhwYR9qtmFE61pPYDSL_AsSaB5fbOQtvBphyQhAk-Liq1wD6hLY8dIg2hX_UkM32ZC3Sm8nSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
این کلیپ رو چندبار ببینید و برای آدمایی که تو طبیعت همه چیز رو می‌کَنن و میخورن بفرستید تا بدونن یه قارچ چقدر راحت می‌تونه آدم بکشه! اونم مرگ با درد زیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/Futball180TV/103072" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103071">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=Sr1-A0_RCzzQdTRwaYtA0BvheH0H06lRwhAoV1MV5bTaxDVUx7xgxyXk8JApnWWBW5gP0i0PAu2MU6M0Hf3Eja0Qqzj8jM3pxwxqG3o4tN4FqEgkbXaq__f5D1LgAZjXSHW33tanQZDR78_4hGHShh4uAIe6nt1pxf-RKEnDtq9lMcVj2FFDoNU-g5F79mn5dB38aEuQpyfIoA71tbtJdqH0f6PQwSl8xOziny6gZdVU2tgSlRa5JzqLFnpw1ar7cywquVt_fGedFjPZF8lb1L8RL_BWHlInJsmgAfuVJatbrsJF18f_jccLjqRxFl19sW-o-pOA2LvfbqFmp77bBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=Sr1-A0_RCzzQdTRwaYtA0BvheH0H06lRwhAoV1MV5bTaxDVUx7xgxyXk8JApnWWBW5gP0i0PAu2MU6M0Hf3Eja0Qqzj8jM3pxwxqG3o4tN4FqEgkbXaq__f5D1LgAZjXSHW33tanQZDR78_4hGHShh4uAIe6nt1pxf-RKEnDtq9lMcVj2FFDoNU-g5F79mn5dB38aEuQpyfIoA71tbtJdqH0f6PQwSl8xOziny6gZdVU2tgSlRa5JzqLFnpw1ar7cywquVt_fGedFjPZF8lb1L8RL_BWHlInJsmgAfuVJatbrsJF18f_jccLjqRxFl19sW-o-pOA2LvfbqFmp77bBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
روایت‌جالب‌پپ‌از معرفی نیمار به بازیکنان بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/103071" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103070">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be22201896.mp4?token=t2I2jOIsvAva-Bvr65iDtmyh12j743Mf8nm3GJTRlMyqUO2WcZOLZNtnzqbK8fjPxhelobz2YO7RMxuepham7j2qafvALnVnpjjbP2rOwCGxbb5pwFG5aKqkPqychJh0ZlgbcEKieVU-cn92sZ0TDk8EIjTY2P0XInsNja_UWQyi-K82WvXqd1v7lMuCEPcgTelaS1yr4GQC5GwOcokWzrB98qlWWANyuygRBF8qYIqLJyQndvctrevqHpDwecoR0tIEtzGTwXCJFQRLvwqY2UWQuTgKUDq-Ro--Kc3RZYOSZLvQDnG1cmGyvZYpVBbRE8fHdhKhH4P2TiOx4lMCJDAgNOcCVKXL_DtvHptczIyxrxxhnxgqz1AxJzrB_t-6WHaa-_9jGIiOTtvxjSUGi2E_0-GuoHASLqOy99HXs_JxXlzHC8xho0nkrSOHEl8w8j6C1Cc4sj8T_9kBxpadWN23JvCu5wrJ1HBRvktTjs9QvuTUd5shqYzIgkVWg0OF5TbuZZtVHsqJt_FLBLhKOq5CKNKx59tuznPSvV4kBU8QGqe3DofvEGjljIGp_pMfGo6dNk6ZsDhjzZKVvd2YQlMEku93srq8PZ4WaJjBCJjjvobR5kSDF5OdsVOU2v0fAHp4cIBZxbHHaln5-J6ClW3cqllFYDQo36ZEcB0IuFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be22201896.mp4?token=t2I2jOIsvAva-Bvr65iDtmyh12j743Mf8nm3GJTRlMyqUO2WcZOLZNtnzqbK8fjPxhelobz2YO7RMxuepham7j2qafvALnVnpjjbP2rOwCGxbb5pwFG5aKqkPqychJh0ZlgbcEKieVU-cn92sZ0TDk8EIjTY2P0XInsNja_UWQyi-K82WvXqd1v7lMuCEPcgTelaS1yr4GQC5GwOcokWzrB98qlWWANyuygRBF8qYIqLJyQndvctrevqHpDwecoR0tIEtzGTwXCJFQRLvwqY2UWQuTgKUDq-Ro--Kc3RZYOSZLvQDnG1cmGyvZYpVBbRE8fHdhKhH4P2TiOx4lMCJDAgNOcCVKXL_DtvHptczIyxrxxhnxgqz1AxJzrB_t-6WHaa-_9jGIiOTtvxjSUGi2E_0-GuoHASLqOy99HXs_JxXlzHC8xho0nkrSOHEl8w8j6C1Cc4sj8T_9kBxpadWN23JvCu5wrJ1HBRvktTjs9QvuTUd5shqYzIgkVWg0OF5TbuZZtVHsqJt_FLBLhKOq5CKNKx59tuznPSvV4kBU8QGqe3DofvEGjljIGp_pMfGo6dNk6ZsDhjzZKVvd2YQlMEku93srq8PZ4WaJjBCJjjvobR5kSDF5OdsVOU2v0fAHp4cIBZxbHHaln5-J6ClW3cqllFYDQo36ZEcB0IuFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
روایت احساسی خوزه از ساعات پس از فینال UCL و قهرمانی با اینتر و تصمیم برای سرمربیگری رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/103070" target="_blank">📅 15:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103069">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=fOt1LAzhtzKYWoK5vkS-Rw3jiRbcNQYqW0mAzSI_s_XZlJVUqfDPkolH60Z89bkn6XHV1nbhumE8fuY7fBy2eUGU8juGjKILrOJ6tT9hhn94lNfSEDbcyLhczij30dEE9OwMi_MOfNSR8iOTuxUU5fujVOEq0QDKC7Ri65OVFkJSyZH4IJs5i9p0VV_zkCz7A6zMKArpSF4TssjEQHCvLcRTP3viExziIcyq9L_2bYffAr0-4ZBEfxdIIf-2d9uHf1qdFs88Haw3pIEyYvp-9BUrThN0GGluAJRfWpfh8uLtkBkCaJ9-knle2V9zpks4VAfJQn_hr9r10d8qFJVymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=fOt1LAzhtzKYWoK5vkS-Rw3jiRbcNQYqW0mAzSI_s_XZlJVUqfDPkolH60Z89bkn6XHV1nbhumE8fuY7fBy2eUGU8juGjKILrOJ6tT9hhn94lNfSEDbcyLhczij30dEE9OwMi_MOfNSR8iOTuxUU5fujVOEq0QDKC7Ri65OVFkJSyZH4IJs5i9p0VV_zkCz7A6zMKArpSF4TssjEQHCvLcRTP3viExziIcyq9L_2bYffAr0-4ZBEfxdIIf-2d9uHf1qdFs88Haw3pIEyYvp-9BUrThN0GGluAJRfWpfh8uLtkBkCaJ9-knle2V9zpks4VAfJQn_hr9r10d8qFJVymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید چقدرضربه محکم بود که یارو با این هیکل پهن شد کف زمین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/103069" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103068">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmXQL6se3NEukU3Fb7st_GDBLR86_zsNqod_x8mVKRmuxglCMZF2n8C1pZaOX6V2TFjPh2DGu8Qd4Nrg00sG_kMrdUXcFbReiQg8rbbW9nlM29D94oX_2L9lxknJmLXiPeXEOwDsAfBHzq8XCYM4ItPpI3MrXXwSX_rVjwvWH1NZ9HXecg1A8GIZ15bWGPrbQTXf-KJ1h8cMq_ZCH9XtwHgaUvpPmdHzevVSIy6ZUdwRVw_SWx0I7q1tACc0_4x5vo-0EWU0KPqbmKfyThsH3ByL12aw1WRM13DQU3D1-rQROV1T8L_YUXeKSjg0e_u0VH3U-lWUebJZp1NYWGEyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
نگاهی به آمار گلزنی لئو مسی در بارسا به مناسبت پنجمین سالروز خداحافظی او از جمع کاتالان‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103068" target="_blank">📅 14:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcCIJbIgW4KmPtu3ojVGK96r_8wwqMEEbyiaHkwnAVwnjZoNGKdDyX0ovArZHdHebMjDG9HmAtZNmePhiqfMG9NROXb33bvTI_kC3UAb5CJ_JkH9I4LGtADvOcWvA7GFKd_4hKGYYdnzLBvAUhQYQNW2QtNE2TUux3nAXMytuaNtApayhTN-i8ff_ktQqG_gJc6t3WctIGb459xbdGPX4VSEOcuL-pySV1qnqbp9qWEAuiXiGp4CFjDqUJtw5jDIHiSmXQueVhdFQdN0OXk7UweGetyOPXd4SHw5234TKI1vsp2wkE7TV2eiTfkY12BbLnxEyRDPVjC6CUy2QltTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خورخه مسی، پدر لیونل مسی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103067" target="_blank">📅 14:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=l--T2GIfXSPCZfcizOIJH9JRvg7sQixRza0Ees5Q_b65yPIZcLUIiG2vvFdutafgl9OXMUNQJyJoNaoJ4DF_ML-ijTw1ZvQrnhIl-hWYYfBXI4SWv99PEumkPcfuMLmcibxANC6CdrOTN31PIo6CofNs9MB7LlPTRnJ6xLOty5U9vz1G6uCs90VuAuOTjOy2sMiDVHIm-cy3iDNTWlhyy_q8CJ1mJ-lSg0HjSCtsqesFdX2FTw3Nod4x-XzHtSgKxZxUVL1bsEvEkfS1uUju0i21RGzL5pXTgV6IJVNVydSR_ZT3W6RTr31K6NF8xSqpwBxu8V4CdV8uwQ8gl5aESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=l--T2GIfXSPCZfcizOIJH9JRvg7sQixRza0Ees5Q_b65yPIZcLUIiG2vvFdutafgl9OXMUNQJyJoNaoJ4DF_ML-ijTw1ZvQrnhIl-hWYYfBXI4SWv99PEumkPcfuMLmcibxANC6CdrOTN31PIo6CofNs9MB7LlPTRnJ6xLOty5U9vz1G6uCs90VuAuOTjOy2sMiDVHIm-cy3iDNTWlhyy_q8CJ1mJ-lSg0HjSCtsqesFdX2FTw3Nod4x-XzHtSgKxZxUVL1bsEvEkfS1uUju0i21RGzL5pXTgV6IJVNVydSR_ZT3W6RTr31K6NF8xSqpwBxu8V4CdV8uwQ8gl5aESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
سطح‌تمرینات تیم‌های باشگاهی آفریقا رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103066" target="_blank">📅 14:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhP_SA-6wZvR6M1otmOBzueWHbP8cHKtvAr8gePhWc1iR08rh-myDLETh8bTjLjrvcVv62XxOg9CqdYBR7k525QmqtBQ1eEJcvD-_oM5BzUyy4Q1mL1Y25Tt9iJd7qz-kJH96WLbyfSlOPF4wIIyariCjHsTMkwlemmRMUL83KwHyzOfLvYEopjwJXf-woxZjjlb7WcR2xoegKPohRrVNG7FQvn__zCKo4ak7ED61ouz00qkVpaTPeDyM89mzJU7gvJzQwgA_2PhzMulRfspjtFvTcfEOGbKVXJFq6IvA6BqWaW-gNiyMj2sgnd1MoQVC2FWFaWbOq1pTPGH531CBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
🇹🇷
علی‌ناجی خبرنگار ترکیه‌ای: پیشنهاد ۱۲۰ میلیون یورویی اتلتیکومادرید برای جذب ویکتور اوسیمن توسط گالاتاسرای رد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103065" target="_blank">📅 13:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103064">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103064" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103063">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=Rxjri4SIfz0h1EMLz1pwuyO5pbaFAkxdYZDPvRhcsG7N9xxOz_eEcg43lNvCtu2E_9S_mTA970PULXRnc6NCz4k6e-fwq0rPr5N5xPAk53raU8vMTyNpx5sF6PbcwnI0m9BHCgb9T0pSD6hYEY4AdYzPnqE0uy8VBblYFf8jg1U3rDNxUSaOyEDg_smfwFchZVfXY1MIKVwwWVPHFOiWy66FxaM79gmWZTB2In80T5BNx6UqeJib-qtFl-GxguO42xPYvlP2lgT47OnRK4dgmKxStLwE_4RRXf8nZGKhmNGkwkfmUxCNzt2ZvcsTv5Y53lhrhxMtFVhgEEicWylP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=Rxjri4SIfz0h1EMLz1pwuyO5pbaFAkxdYZDPvRhcsG7N9xxOz_eEcg43lNvCtu2E_9S_mTA970PULXRnc6NCz4k6e-fwq0rPr5N5xPAk53raU8vMTyNpx5sF6PbcwnI0m9BHCgb9T0pSD6hYEY4AdYzPnqE0uy8VBblYFf8jg1U3rDNxUSaOyEDg_smfwFchZVfXY1MIKVwwWVPHFOiWy66FxaM79gmWZTB2In80T5BNx6UqeJib-qtFl-GxguO42xPYvlP2lgT47OnRK4dgmKxStLwE_4RRXf8nZGKhmNGkwkfmUxCNzt2ZvcsTv5Y53lhrhxMtFVhgEEicWylP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
یامال این‌روزها تو کلمبیا نقش دیجی‌ بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103063" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103062">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDKmJFAIHqReYH6iMdRFvmp5VtmsVcLplRk9jFxCJprW4a1IzyoLNdIPiOp8IbLNefQzJiB773tvDc4Yw1DBjbrYl41c28cPtkquiw8px7UW1rhzJIqmzk6XnsB1DBH_KLqf4H47rIKN_irUQhb5nJLw0PWj56SYpuOApgZ-Nk6BLtOy-qiMJ9Rz6Ao5AUuWsKUNI_9QdyW1WyLUGnSeTSNPcD7D5rBvjl1znrI9p4S_c3qQbIHAktNb6pOm4p0CoR3ESkBa5VlTEkk3GXct4fPHcCZsIDsBd2Xq9Y_7HdHZCQRqAzH8EskyZspXR6NyEyjEbmJ9pfiOAAfLFLdZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📰
افشاگری‌عجیب فرهیختگان: موسی جنپو فصل‌گذشته به ازای هرماه حدود ۱۴۰ هزار یورو از استقلال دستمزد می‌گرفته که در تیم جدیدش در یونان این رقم به ۲۰ هزار یورو در ماه میرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103062" target="_blank">📅 13:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPmSS-iK1q41szkhuA0ODsDd8_uJTLwe5M0XQDqz0qZd1gZjJz1_RWsxTZEOEuB_3YMZlz1rAy-8aPZLVH9eQzu2YVnvxdqoUhHMWysMMH65s_aigCGNvn1xJ9YwYDMUvi56sBwfF9hekmYm19gFULdfPFGrb1Zc9QC4SFrqZHMvta6emhUC1GH67-pLB7Ae-5XVRwFUw37QGy9XCDy30qX2SG9yCgCka__qlZ31HmHuWn1fc77NEfQlPU9OjBJHUeCIFDKdMw9v2BXnBk77W7X0kHLpGR0d4SoWyENq0ec_BzpySo9EJ2E8NnE4ztIKStDkXiekelcDAjJ1H3Bkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🤯
#فوووووری
و پشم‌ریزون از مارکا: توطئه‌ای برای ترور لیونل مسی در جریان جام جهانی فاش شده
😐
🇺🇸
طبق گزارش پلیس آمریکا، لیونل مسی بازیکنی بوده که در طول جام جهانی ۲۰۲۶ بیشترین تهدیدها علیه او مطرح شده؛ از جمله یک تهدید ادعایی درباره حمله انتحاری.
❗️
پیش از دیدار آرژانتین مقابل اردن در مرحله گروهی، ظاهرا فردی با فرودگاه دالاس تماس گرفته و تهدید کرده که به همراه دو نفر دیگر، با سلاح و مواد منفجره دست‌ساز وارد ورزشگاه خواهد شد و مشخصا مسی را هدف قرار خواهد داد.
⚠️
تهدیدهای مشابهی پیش از دیدار آرژانتین مقابل مصر در مرحله یک‌هشتم نهایی نیز مطرح شد. پلیس همچنین یک تهدید بمب‌گذاری جداگانه دریافت کرد که در آن ادعا شده بود مواد منفجره داخل سطل‌های زباله ورزشگاه کار گذاشته شده است. نیروهای امنیتی با کمک سگ‌های مواد منفجره ورزشگاه را جست‌وجو کردند، اما هیچ بمبی پیدا نشد و مشخص شد این تهدید نیز کاذب بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103061" target="_blank">📅 12:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNSRvwjAHxKcShsDUApb3DZF03GaFYSNumSIrkJHHty01Fb2gbZ1ZWY__naBSMg7SJXL59HNUEy3mW1kXCCmOyYUnzxiBieAsr4VeIbk4Gk5NXB6ueV4gj--aitsK7RM7gOdFx0GwpwF7mMS2O3tHzzKd9esSM64qwJoLpn5o6-3DuKVWjlFFwqZE_XHVnDOB87-vanCTDcQrKc-2vThRhkkvY8ZdBoeJUqIUak26rCc6LCRsjR0LvTg_uepdsBuZ4rLFa_spPFoR5EBK5wF8C9Gi-1Nnl8fjLgaMPjC4hMCKm4_qZGL0OraxpVAtprzGOb1xjHEX5zwZ6BAs_rsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از لوئیس روخو :
✅
فران تورس پاریس سن‌ژرمن را انتخاب کرد
🔼
مدیر برنامه‌های او این تصمیم را به اطلاع باشگاه بارسلونا رسانده
🤝
هم‌اکنون مذاکرات میان دو باشگاه در جریان بوده و تا نهایی شدن توافق فاصله‌ای باقی نمانده
💸
پاریس سن‌ژرمن مبلغی در حدود ۵۰ میلیون یورو پرداخت خواهد کرد
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103059" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU_aoUenKQAp-koAq7CZhshJknqWmh1K53fnlZ7zXgTTYH6RcmksHWwowNc4X6W-5O6T9ZxWILlzZtph8DKzxfCQE3zwFvdaDE9Df3jA0c4sJT8ZNCn_gi7hHn5zNFAB9XiKKsvUgkx4H6cCGDdP4Kx9W7XB0HIJWllp-DbgorIpRynJHhAyk9LLKIncWq04Sy4H0kKoAlOyNYBmHSccCbHdIckMyi6dj7GONpJwNVF_I1YWEjYOBcEd9HXjOGHqLlJgSkWRy8lgySCR2mPv2OhNoaFj-Mw0zKll6Y2avs0lBRF4tNOiu8wRG--rSScfJEu-wf9tvRAoBYwq5QQobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری
دیه‌گو سیمئونه :
🔻
وضعیت کاملاً روشنه. باشگاه تصمیمی گرفته که میگل آنخل اون رو خیلی خوب توضیح داده. از نظر ورزشی ما از داشتن بازیکنی مثل جولیان بسیار خرسندیم و بهش کمک می‌کنیم تا به رشد و پیشرفت خودش ادامه بده.
🔻
قبلاً هم شرایط مشابهی رو تجربه کردیم و دیدیم که چه اتفاقی برای گریزمان افتاد. از نظر ورزشی هیچ راه دیگه‌ای جز ادامه کار نمی‌بینم؛ این وظیفه‌ایه که نقشمون به ما دیکته می‌کنه و تمام تلاشمون رو می‌کنیم تا مثل دو سال گذشته بهش کمک کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103058" target="_blank">📅 12:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103057">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCIFRoxnjyRycF4DHGmn90YIliMBx3hGpylHuTOVygQJB2MMn7VLhjmIN5fHVyrigINYhDUKKF3EAx-ulEFsTVDc5rSB6765-fX2CUyvz_ZCvCNsLlTNvJ2igKGl_o1807MF-_X-gl71nrSyITWy0W1QTgpoXziEBSEJ-7IxKsXbeZPcJqTyc8xUNUooxdF7c4MR6e6u1ZA5sJjURVNInQCYl1YVhCNcCLos8rsfxOQP2IaKW-ReT2wmas7clnzzbN-LmE4LQdzORfbGUI1TMCqFCr__1oqcsqH8fnGjtzuvyu0Q6bd4oKt5avsW2BsVMwJMVIRG0QdYXpGLzsKRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو:
الهلال برای جذب کاسادو با بارسلونا تماس گرفت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103057" target="_blank">📅 12:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trbSM0LsKvQVygQuU8D5uv6sksdN5uOINwwwbexb84vSH8TD4R0XVjX6WG7qqW9sPjl4pIwzePwAEHe7DHZsY8PWgIInRFQnJBGWWJDtZhduiUbu35jLE4j6-j_T2mp2DFd1lkgDH1BGdiBBS9jfVu75Tj17mJ6Wn34oPwn6k0yTllBQdjXPfTi_XgeC2Np0jP3LIt94TdmCd_dsO4GxBjz2Uld05JnfTzIfjp215dcrVEzEn3-geICgvjXTbFv5miatCGxgkfvpTQ0PpORY-Jw9GYvrwO7SVvs5reHK-I2ZQVBivXltUDye-ET_1APaa1jCXd9Ls7rZvv-cy7cVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست PSG برای بازی با منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103056" target="_blank">📅 11:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgV5gkUHy7b2-aRgUY7O1WHxtuzBLy5bBqbPESGwYx4jS0farjQxitBWa_2yw_8KJayjnwYVXiVwKIN8kczpLKEiWQnj2AADcF1-V_q9y9x8_s4Nzl1ebkA4cAmMvf8WtDTOWXEfJsspbHZCRdLv1xdci9RddB0ZwMMH_KsmhpC4UO84STTcFf8-7b8v53mOLghAXhdSKpD219gZ5WUqJeWB6ecn696eTAlE2QGvBVDabRIuGpYVfmERHVnk-FUQnP7h-N_8hrUp37BwXwpJZydvXDyTBwGWiFWsj9Izh1M6XRayM89u5h4Gc3aPSKRJSxhe4mTVezVdw9YwEIhG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
بارسلونا روز ۱۶ آگوست در سومین بازی دوستانه پیش‌فصل به مصاف بازل سوئیس میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103055" target="_blank">📅 11:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103054">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff922b433.mp4?token=viJh8LbH-kxGbfGJ8-OHBNsuIfZjqISzAb7gdED9EYwnAO4nOZEKiB5-DTFf3uEcrKk3RhK9ByYAj0FcGmSAOf3r0_yfXDyoIgaAVjO0_bdNs9jW-cRZ4Dk-Q6WJ-Cue3q0itJjJ8qvMYbCduuxjwBUCadLK1Y6IsnwE5366fOcwO26eqWJwW6nCkDcKFCQR44kzvia6Xs9msHlcbm7WMJksv1TP_Xaw_d7ErFWWF8X7jXcRE1bZ88Pj5vysSu9GKYoPJNplg5qWTdc5iRtftO1wox4gJjKPEduEOTY7hGZQxTYkYcm8wxnB_gpcLlHKVBvhRZy1ZpBoYo7CBker2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff922b433.mp4?token=viJh8LbH-kxGbfGJ8-OHBNsuIfZjqISzAb7gdED9EYwnAO4nOZEKiB5-DTFf3uEcrKk3RhK9ByYAj0FcGmSAOf3r0_yfXDyoIgaAVjO0_bdNs9jW-cRZ4Dk-Q6WJ-Cue3q0itJjJ8qvMYbCduuxjwBUCadLK1Y6IsnwE5366fOcwO26eqWJwW6nCkDcKFCQR44kzvia6Xs9msHlcbm7WMJksv1TP_Xaw_d7ErFWWF8X7jXcRE1bZ88Pj5vysSu9GKYoPJNplg5qWTdc5iRtftO1wox4gJjKPEduEOTY7hGZQxTYkYcm8wxnB_gpcLlHKVBvhRZy1ZpBoYo7CBker2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترابوزان‌اسپور ترکیه درحال یادگیری زبان عربی بعد حضور محمد صلاح در تیمشون
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103054" target="_blank">📅 11:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103053">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d7174722.mp4?token=fWKbCIU7d0vTpKKQjP5WirpHBeVexBN3g7lD5np78VWcDeQGltiLfhbzTLB0yvDAhex8iBLvncmsrIyjJekLJnDtlJFI0o-WpdZFl6HEX88hozL-1hWDy-1xe7O5EEc6SKxVmlGuf2SgjDA3sVeoDNrrJEziMkZh5CDrcVeOSUgE2gpnTl6sDd7OOEsZgdOm4geDf_Ki3kPcbdEHSYYI22mrNPa28jDJpeKl7QJ_jaR5ZUk97UwBdLq0fX5sHsyQdsD8RGr_rGKa_7jUkp_AAuSD05g5WhJjGZZWDa6flKFH_c9zCPF8NtZRss22343aBjoxSbdmRkkp2LoQgumiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d7174722.mp4?token=fWKbCIU7d0vTpKKQjP5WirpHBeVexBN3g7lD5np78VWcDeQGltiLfhbzTLB0yvDAhex8iBLvncmsrIyjJekLJnDtlJFI0o-WpdZFl6HEX88hozL-1hWDy-1xe7O5EEc6SKxVmlGuf2SgjDA3sVeoDNrrJEziMkZh5CDrcVeOSUgE2gpnTl6sDd7OOEsZgdOm4geDf_Ki3kPcbdEHSYYI22mrNPa28jDJpeKl7QJ_jaR5ZUk97UwBdLq0fX5sHsyQdsD8RGr_rGKa_7jUkp_AAuSD05g5WhJjGZZWDa6flKFH_c9zCPF8NtZRss22343aBjoxSbdmRkkp2LoQgumiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
از عجایب مملکت؛ امام جمعه ماکو رو بردن که سالن آرایش زنونه رو افتتاح کنه
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103053" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103052">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103052" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103052" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103051">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=E95VDFrHxQI3Z9pZCriAtqOgn86sTmc9M3laec1Ml_6UJkFqxwb5ZDMNftRucd2uNksWEO4Td9JlNfIJlhMP9saRJjtyJ8Jjo6Rwhte2pHD-s0uB69lNZaYSNGTHiK6T9yf2GOM5b7MKvbqP3_THbpO7c5mmN8LKIDJ0_HgdinqEepS7JSTOBl6qM1uDbjOGcpZkNSjXgkZMmSkypN9KsxOD3Csf_iB59xHV_ZlivlIo8VEk3JlTwBwednRtKf7wauq9gDQcxz3C-OOmbC3voKSdyxaV1rgD-1NuzoFgTOHG69WdYtV5ARC5AHBmWa38DcbngrqUJ5KZOI_AjlMheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=E95VDFrHxQI3Z9pZCriAtqOgn86sTmc9M3laec1Ml_6UJkFqxwb5ZDMNftRucd2uNksWEO4Td9JlNfIJlhMP9saRJjtyJ8Jjo6Rwhte2pHD-s0uB69lNZaYSNGTHiK6T9yf2GOM5b7MKvbqP3_THbpO7c5mmN8LKIDJ0_HgdinqEepS7JSTOBl6qM1uDbjOGcpZkNSjXgkZMmSkypN9KsxOD3Csf_iB59xHV_ZlivlIo8VEk3JlTwBwednRtKf7wauq9gDQcxz3C-OOmbC3voKSdyxaV1rgD-1NuzoFgTOHG69WdYtV5ARC5AHBmWa38DcbngrqUJ5KZOI_AjlMheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r17
@betinjabet</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103051" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103050">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f294785d1.mp4?token=O7nLSf_VFZLgyYCQFV4iCpHirDnWUNs-8cX-_qSMGHe8KfiTwUYFs1-OnJYZtb7EBQqy5AvGZjFR2FawXJ22wTtVZ48AxkaxJvZfo4RW3tJnm75hj-re0yy_nyPllH51KwbZ9ku1nD-O8GsPfywbiR1E3RgK3Q7TRJbl1oHPpKFgou-Vls9OY5sZ-w4Jbbue6m2r8c4DJN6CAZ3IhZfNAcGCP7_lulJ4rVsbUPOY789fUNKJr8sbEaRlvAve6NxCc-6XLh1Xrg5FG3T-VR7gqjtqDN7Mb_B5NTOEnxS2e-0_NGfr2YSDdzvimu0OLgGwVU7HiXshWcKx4_eox0otP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f294785d1.mp4?token=O7nLSf_VFZLgyYCQFV4iCpHirDnWUNs-8cX-_qSMGHe8KfiTwUYFs1-OnJYZtb7EBQqy5AvGZjFR2FawXJ22wTtVZ48AxkaxJvZfo4RW3tJnm75hj-re0yy_nyPllH51KwbZ9ku1nD-O8GsPfywbiR1E3RgK3Q7TRJbl1oHPpKFgou-Vls9OY5sZ-w4Jbbue6m2r8c4DJN6CAZ3IhZfNAcGCP7_lulJ4rVsbUPOY789fUNKJr8sbEaRlvAve6NxCc-6XLh1Xrg5FG3T-VR7gqjtqDN7Mb_B5NTOEnxS2e-0_NGfr2YSDdzvimu0OLgGwVU7HiXshWcKx4_eox0otP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚽️
مثلث‌رویایی کریستال‌پالاس با حضور ازه، اولیسه و ماتتا که شکار تیم‌های بزرگ شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103050" target="_blank">📅 11:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsB5b_fsz5ZdGgMfopNmEzNX426bDOFQ3ch3MJXR4OB-CKeXe1YCP6FKFS_coyeO2FHH8l-C0t7wNVXZouD5sKteQKu0vdRU5tq7HkNBI1VRCe6nnZWne1DQcmTB5_hcndoOrGX3Cm1OajN9fS2D_wTsPlGaDKfdozW_s4j2pcMCVuDweXGmPSxchZUnvnF1SvhDspNN5SIjsI9xX34Q_Zuyg6TVczxQP4y12RFu0stIudFQUIWECflVRQUTLJAyphBByMaVwT7mqMiy_-aWKk27qQytdOxpLJ6Iif79ZkF4OE4UdiNZ7uj-jSBVy-kEoSoYQxFPtgvM7Cri0a6j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تلگراف:
اینفانتینو که متاهله و 4 تا بچه هم داره در زمان تصدی پست دبیرکلی اتحادیه یوفا با یه زن کارمند یوفا ریختن رو هم و باهم رابطه داشتن! اینفانتینو هزینه‌های زندگی این زن رو پرداخت میکرده و کلی پول خرجش کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103049" target="_blank">📅 10:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3239f9b4b3.mp4?token=XZttmbKz32nPTBzBpm8ZhKQRSi1zy2mX1X1OV6uZAFqNE4qJ_pRE8MzN0tISX_8CvTp7WnGk5txpMauOxez2s4BQx_Vn_pzyIaFYQnI7ipW_ca82EAYYttI7o7FltI33mEzIMOYydj58LGpdu7_a10CV8hprHWVNY83_hcLslbOhlVKPXLB7CW5DgqrDDaVWKo20UWtk7fkcIw19dNO5Yw7hCnstEaciUbkfRsXMQmPQVFdN15msNb9ZCeZG3bnhOFzYclOWMkOiAlTDoiI3T0Bk_nOlPN37yaL2f7dPXiSuzcIe-wz2rp405ICvrcxB1LzZidJcJVg9btLVU5Y4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3239f9b4b3.mp4?token=XZttmbKz32nPTBzBpm8ZhKQRSi1zy2mX1X1OV6uZAFqNE4qJ_pRE8MzN0tISX_8CvTp7WnGk5txpMauOxez2s4BQx_Vn_pzyIaFYQnI7ipW_ca82EAYYttI7o7FltI33mEzIMOYydj58LGpdu7_a10CV8hprHWVNY83_hcLslbOhlVKPXLB7CW5DgqrDDaVWKo20UWtk7fkcIw19dNO5Yw7hCnstEaciUbkfRsXMQmPQVFdN15msNb9ZCeZG3bnhOFzYclOWMkOiAlTDoiI3T0Bk_nOlPN37yaL2f7dPXiSuzcIe-wz2rp405ICvrcxB1LzZidJcJVg9btLVU5Y4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تعطیلی باشگاه و واکنش صاحب باشگاه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103048" target="_blank">📅 10:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103047">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🙂
👀
واکنش جالب پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابوزان اسپور
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103047" target="_blank">📅 10:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103046">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563a2467b.mp4?token=jC5yQHFNDV-ma51WmvknATxESXBut7KjkjogngyFoZqbB4cpoTxIeNepmPulwxP_hFqZ3Zr1ObViNNVGAJhjlcj5u-dEJ-hroRj80pQtkI5048PxKd1pmhe_IQhkmwBoIgnBcwtZT0LulT_bvPTO0IiRm8Yj9-QrrKxxSFNGtQwHhhzg7n72bgHKY39sk-IpuMQvqs6sN9K7Zm5t7gahTrS4VQ2deHW9ZviSUTpQKt6XVP30wpiIIVUhH9Ls_Gl3wnYy3e3bTmsR2kZ8qTRBrE7JphNk8Zab-wV5FMKonARgbZ2AKV7IKX8U5BKINnimZjLWUpjmFa3UZsIkCZaopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563a2467b.mp4?token=jC5yQHFNDV-ma51WmvknATxESXBut7KjkjogngyFoZqbB4cpoTxIeNepmPulwxP_hFqZ3Zr1ObViNNVGAJhjlcj5u-dEJ-hroRj80pQtkI5048PxKd1pmhe_IQhkmwBoIgnBcwtZT0LulT_bvPTO0IiRm8Yj9-QrrKxxSFNGtQwHhhzg7n72bgHKY39sk-IpuMQvqs6sN9K7Zm5t7gahTrS4VQ2deHW9ZviSUTpQKt6XVP30wpiIIVUhH9Ls_Gl3wnYy3e3bTmsR2kZ8qTRBrE7JphNk8Zab-wV5FMKonARgbZ2AKV7IKX8U5BKINnimZjLWUpjmFa3UZsIkCZaopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
هنوز فصل‌شروع نشده لوئیز دیاز گلای سکسی خودشو برا بایرن‌مونیخ شروع کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103046" target="_blank">📅 09:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114a435ca1.mp4?token=D9WWrFEeNTttweeGIKa8WPESzw1Uih3I3Om1fIR-8Yhs1kql7hjNpbJvLIm4xzlEdfycy5X42fkNHZVIQUVX5xWza15UhVeRuZAB51PBsqQ0ZY7QS9TQE8sEbLmGSsqvlyboaX12yA21Acffjw4GlTsQ__wJ8lfubF0yacAWgJI8YCXvXfEneteN2somMyDIohqZxjuLJHk1qV41JgegMgAiVhxVs_G6Js9AhcD-diXbPIaoIS5JdcvNMkY_Q0Lli5PCyvwa9mEGaubNNNZeSXO0ATZgM6fSMKNT8Qo-9cNsGWc2Z8neFsch-CSqUwYWTp3-FB3kAsktKD4dM_z4MpcwLqTERP2UwyELkarXKshCKSEwyTua6YbmAz8vAREpjpfGc_kBjKCohIA44xGGOrtIFn6pKSHVAt1z1jrRwg68250tROc59qLyjHuUIvqUzEzgYMWoErwGBo7iDxpaIyokZ8D783aiM8ftXou6W-FS6g5jxv6_tMGgTtDtKgUAHPyBQ_27LDmkbeu0go4dNuPPV3ArWE_YH9XI3fmx5qCh5Q7yBB2UzXCr2evUNskvABbuKWbWpsE0tpkFvbJ0lsx3_FWaO565acQnVTJLUEcOUfSDThe9HhlY1kgmWmm7odpNN1ChIUuFgRJIncpHwrL3fHfV1vDo3nVzqGBYYss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114a435ca1.mp4?token=D9WWrFEeNTttweeGIKa8WPESzw1Uih3I3Om1fIR-8Yhs1kql7hjNpbJvLIm4xzlEdfycy5X42fkNHZVIQUVX5xWza15UhVeRuZAB51PBsqQ0ZY7QS9TQE8sEbLmGSsqvlyboaX12yA21Acffjw4GlTsQ__wJ8lfubF0yacAWgJI8YCXvXfEneteN2somMyDIohqZxjuLJHk1qV41JgegMgAiVhxVs_G6Js9AhcD-diXbPIaoIS5JdcvNMkY_Q0Lli5PCyvwa9mEGaubNNNZeSXO0ATZgM6fSMKNT8Qo-9cNsGWc2Z8neFsch-CSqUwYWTp3-FB3kAsktKD4dM_z4MpcwLqTERP2UwyELkarXKshCKSEwyTua6YbmAz8vAREpjpfGc_kBjKCohIA44xGGOrtIFn6pKSHVAt1z1jrRwg68250tROc59qLyjHuUIvqUzEzgYMWoErwGBo7iDxpaIyokZ8D783aiM8ftXou6W-FS6g5jxv6_tMGgTtDtKgUAHPyBQ_27LDmkbeu0go4dNuPPV3ArWE_YH9XI3fmx5qCh5Q7yBB2UzXCr2evUNskvABbuKWbWpsE0tpkFvbJ0lsx3_FWaO565acQnVTJLUEcOUfSDThe9HhlY1kgmWmm7odpNN1ChIUuFgRJIncpHwrL3fHfV1vDo3nVzqGBYYss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
✅
استوری وریا غفوری: تقدیم به همه جان های عزیزی که برایِ ایران فدا شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103045" target="_blank">📅 09:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbaa91a27.mp4?token=erseHJIKJl2AmJpOGZim-HlAmnCvVixC2fcNRyopaJRnJNVJbNq6WltFA7PtZlOf4xorYNbq14f-TjQnBowKJtqIqLf-U-dJLwmfjD8I_7PKkWWrZvWnhLuS4e1onGPm6EXVLfUXIKMsS_SGkLZRN88teFyldhJicq2QgrYot6EJA4oYrrbHNYW9n5mRJsVEuBZ7OFjCoZYBr5OPv5-7VDy0PX2xr7ZWihV5ilaE3ovWdxUaNz17kMy6iwSR1zTi9o1w1zxtrNeh5JoISLCrtKyx1QgvyImOnDwqV-zKh17p0wsJJlv_zarDCaqp2sPDtMRyoCE8humr89TKtHvkeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbaa91a27.mp4?token=erseHJIKJl2AmJpOGZim-HlAmnCvVixC2fcNRyopaJRnJNVJbNq6WltFA7PtZlOf4xorYNbq14f-TjQnBowKJtqIqLf-U-dJLwmfjD8I_7PKkWWrZvWnhLuS4e1onGPm6EXVLfUXIKMsS_SGkLZRN88teFyldhJicq2QgrYot6EJA4oYrrbHNYW9n5mRJsVEuBZ7OFjCoZYBr5OPv5-7VDy0PX2xr7ZWihV5ilaE3ovWdxUaNz17kMy6iwSR1zTi9o1w1zxtrNeh5JoISLCrtKyx1QgvyImOnDwqV-zKh17p0wsJJlv_zarDCaqp2sPDtMRyoCE8humr89TKtHvkeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✅
رودری که بارها مقابل مسی و کریستیانو بازی کرده، بدون تردید لئو را بهترین بازیکن تاریخ می‌داند.
🔺
او می‌گوید تفاوت اصلی این بود که کریستیانو در محوطه جریمه مرگبار بود، اما مسی در هر نقطه‌ای از زمین می‌توانست بازی را تغییر دهد؛ تا جایی که فقط با رسیدن توپ به او، حس خطر به همه منتقل می‌شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103044" target="_blank">📅 09:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/103043" target="_blank">📅 02:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=ETGWnZn63DZ0a0AbK6RPywqK1KiRxSYt4Tqna6ZSxOnw6trNvZBAkXQ4Wnbjgut7kpoY-BtiKWGx06muo9KKhgg4_8zwJWbERqkfdZhyeKN8RtUSQPAfqP_Hklcmv3hAv0H5redQ76xr4o8HH3pu8c8Rywe1Fb77NG5MGXzwFD-PjO9iby_BsbVcjHLzMBu415e9tE8rruv2v4XvzUru3MJUQAXjAuI0vGeImD2KbMN8g-iW3vsAR3I_PjcSTC87kddHG8cbMK0tJNhsDSgdlPrvjm4crHSM5o_K29XdayPltBDjowBGkncVXPp-JSqNg8ca7fbruhgId9H1QQEMZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=ETGWnZn63DZ0a0AbK6RPywqK1KiRxSYt4Tqna6ZSxOnw6trNvZBAkXQ4Wnbjgut7kpoY-BtiKWGx06muo9KKhgg4_8zwJWbERqkfdZhyeKN8RtUSQPAfqP_Hklcmv3hAv0H5redQ76xr4o8HH3pu8c8Rywe1Fb77NG5MGXzwFD-PjO9iby_BsbVcjHLzMBu415e9tE8rruv2v4XvzUru3MJUQAXjAuI0vGeImD2KbMN8g-iW3vsAR3I_PjcSTC87kddHG8cbMK0tJNhsDSgdlPrvjm4crHSM5o_K29XdayPltBDjowBGkncVXPp-JSqNg8ca7fbruhgId9H1QQEMZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❗️
ریدم حاجی اینجارو داشته باشید
🔻
حسین کلهر مجری سابق صداوسیما مصاحبه کرده گفته که یه شب تو خونه حشری شده بعد زنگ زده وزارت اطلاعات که براش یه پرستو بفرستن تا چنتا اعتراف داشته باشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/103042" target="_blank">📅 01:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9yqnQbmCjLC8AfdXFuboSp-kEJwMVnCSz9IcDturHUERKcQIT03nw2HEkHvOgYXdYWmbcE0YL88jCgec2zutSwkyeRhFJrwsiCNcoYW1K4KT6HQAZf-DMuMzXg8Xsg8YOY4vJ8k4FmrB6pycqHkfm78oJDpeAkxlYhiK3H-p9GzSwC_VKHV4Gw-MOzEbGn1k7mSJXWO5VOYNKtMlzmSWctcSUKaw239aT6XdblPzMAuizdPGpSROBp_cPNjo2JBhFytwvfvTdkdxVkGExNAks9OWz4IW5hc1mceHy9GeviFVoSJW8YmtNhi1Han99Q8K8H5FENc8S6IuiTQrpVolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
🇪🇸
بنظر فصل‌آینده عقب زمین بارسا قراره حسابی تیمشونو شوهر بده؛ مگه اینکه دکو کنار این سه نفر یه مدافع باتجربه اضافه کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103041" target="_blank">📅 01:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geO7JYq7pbYufsHvHOLhXM4hdnQFdzyQUFJPF74hPjM-4fU6I_yrkvpvYVUNkDGTOkoYfUIfh_WZUn2R4mV06sSz1MLINYl48ecVJTkAjezi6MxoxR5VW1zcX-Ktzzxx88m6_eI4WLfZBbRYa_X-I3VcG03iBcbYYat83-8nmdKWR5L0J3K-tY3tvNz49ouviuA2T4q2uibSCTTRDMvW-V2XSeuGb2O2jEoQhgDov0k_Tz5wJrH6Jfwl_BjslgaoiljRWQ9IV80mCpzYyrg2lTuOTrtxTOMuIaO5gmg-OYl8Qk_aQCf9GOFSadeAxaQnrRxrbS1zIpia8h8OruZRmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
لیورپول تمام حقوق آرائوخو رو پرداخت میکنه. همچنین بند خرید اختیاری داره و با پایان فصل‌آینده در صورت نیاز قابلیت فعال‌سازی داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/103040" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103039" target="_blank">📅 01:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103038">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0fpaHTeIvoiAXfI9wBm7KoJrI5cf9kKCztjZrcFNEwggbL2cUbI8zJuFWTqtTYSxTTxTCrg-Oty8gSu1EB93up90zKoFQZ2D90z_R-O7nyqbKH0oIK55nSxOzjUr3v1Tr73Lu2X9hvDNv-ya9q4_OVOpkhmwLzR7N5iGesR9oyC4U6qWVTgCG4hmmzEHVvRAZP4bj7EFB60CmO8XsXFVaIr8B3mE_lEIyxct7tf9g1M-37DEGhA6Qd1jO01LKoSDn7upaeKgrNEKR8uU2g8pWz4iiT-Mno0u9OZD5MOoP-ofijHUX88bCznyuQyY4K3oHwbwqj9JHcTbVIwSvWB0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🇪🇸
بگایی‌هایی که اسطوره آرائوخو در سالیان اخیر برای بارسلونا به همراه خودش داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/103038" target="_blank">📅 01:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103037">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU3Ii9bGbpMwrAM_-JoJj2GO6EedoZMdLJb60FSjuIEFZwxTwP-ubf8GtBPNd_y5OW94PidfJcJ_Rew0pxnCJjTOxHJ8-NFOTszVhCyScaIzr8Wgnl4hG-mEKrtl0S2ohW4NpVXY5xPP0S0sRX8nhPZiNNBeuRWtnOvtcd1IIWAJacfSV1Ya1oeBRjYMUzgcTnozaOQkprD8HyWYD9t6T-4eTR_2XwFCUSCzGHvMDTZImCrlc67jqavSqIp7VVyibqBcC00Eh8P-ZyGt-dmxmYrpAqyHMB0gwlZvbq_ZWxA3H7YDcEgpbi_TuhQJzkGFL2r3xugsfk0clSuPtZUlBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/103037" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103036" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#گل_با_پوچ
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103036" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=Iia147b9xFq1rVQrG6--X1ufiUg476tDXHaKQrhVZVVMLdenFQvCKd0lIBhBeM-mHeU2Xw5UrfYlMHsSEHutkFu9-CN-cV7LZd-NLQfFb3bS1J1LlX89wEnCubHSkZ7V_PwyA05Ordqz_QjziSLVtpkCupKtf0YAIkAj2_yFu3x-orYLAb7ph-NnXAo5C3DEkqv7AFPIF2Qd04OUIxRAhMWl56m2rQjaPpltlzpfE4QLlnedWlndqKT9j9M_Un5TYUlL4dmWazWYe262nLPDIHRsYLlmFxnUd2C7Lp-LAMA29wDbnpmNtc7yPQuUkcnYkaRtRpo5RCNiMTlhpMcj9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=Iia147b9xFq1rVQrG6--X1ufiUg476tDXHaKQrhVZVVMLdenFQvCKd0lIBhBeM-mHeU2Xw5UrfYlMHsSEHutkFu9-CN-cV7LZd-NLQfFb3bS1J1LlX89wEnCubHSkZ7V_PwyA05Ordqz_QjziSLVtpkCupKtf0YAIkAj2_yFu3x-orYLAb7ph-NnXAo5C3DEkqv7AFPIF2Qd04OUIxRAhMWl56m2rQjaPpltlzpfE4QLlnedWlndqKT9j9M_Un5TYUlL4dmWazWYe262nLPDIHRsYLlmFxnUd2C7Lp-LAMA29wDbnpmNtc7yPQuUkcnYkaRtRpo5RCNiMTlhpMcj9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
#آموزش
گل یا پوچ آنلاین با افراد واقعی
🟢
حتما وبدیو آموزشی رو‌تا انتها ببنید راحتتربن بازی پولساز بدون ریسک و بدون پول گل یا پوچ بازی کن
با هر شارژ
2️⃣
1️⃣
🔣
موجودی خالص میگیری و با موجودی اضافیت میتونی کلی پول دربیاری
🔥
💻
آدرس سایت مورد
#‌اعتماد
ما:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a16
@betinjabet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103035" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoeVft7QeZfJ966c2p0gHdk8nEHWBI4OkinOIEgxr9zZ-7Ah55EuqDYJkj-Gy53i8WbLyZ8gJNSCgmPw4SjMWSHu2gcC2nzZmqG5161qrybRagYWMYF_lcStpYvGq65aoxHucfj47B_C9a1-gORwf_OmRzPKf4fedFVDLubdrlMWIHAMzIujAuSW9JAovn7huOZATmoCSKaWj-y7qMxvHZciryhaqRTuUm4Pc4TzC8HXQCdozjItTTa7_pI9kIx65N_XRwaS7-lrpikvXXXbOFRSlqOcAro4XJDn3n7PVGjeIlnEOBkXzUIYDIoeD0NFqq9AQ6BmoevmVZS9EboL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🤯
مهاجمای پریمیرلیگ خایه کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103034" target="_blank">📅 01:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G83-X4zbP6OqAjXx_ADnjZB23jKY0vPp2hAOHIaFtdjvQlNsULB_Y2BKx9h_w7JfSFxMgDz5OByYLGcYjqvjoW_HQ41D9WxQMpCT3tEvTlwx-N8AkOaglSdHdkOAUIxRe9CboLpVeVb0YaL0oVjM9A6o02fc9muS42Ic5hBHyXKTF2whGv8OX5APKJZtNeEww8PcCHYo6RKW6dhXoHdHRuJ7ttZBFJEOswcs7jimFBliI6LTgoIIzCOpp-oiDydg-3MIxu08cASlpEgJbKyfCawGAmgWf2Mbbw3o6x97ggpcxqeSpwQPMdgx3zOsykUE7y4kgvH4hKWHOT2q7WVMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤣
🤣
🤣
دکووووووو بیشرف داره چیکار میکنه تو نقل‌وانتقالات امسال با بارسااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103033" target="_blank">📅 01:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/103032" target="_blank">📅 01:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejSsc8GdZB9p_JX2rQPFnSiJS4twBRexiryLK8D2G67NDXJ2gV03BbmwavGGINq_x7zf4HfgGk7q0BhX6dArPcs-IQgxn6wZuvn1mVdjacKHZXT-xQpOfzSXTLJfJ260pdIfmO0euRueRnexyVzHUOcrhjvs84mNfr4IJmPA6cOjjEJStJApVxkC44VpirZOl88gxgTWJiC49BkXO4pC3BKJdEykYL7Ety_qJ2AYfKueSLNgoB0OIPP4hLrdyi5U7cQGlBAtbHzHmRn4ORH27kE9qUhaBOgbDP2QUJ8K2cC-phO2esiGIVIfcMJwjF4giQFFSq6CHfgXU2iFzjErWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری
و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103031" target="_blank">📅 00:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103030">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103030" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103029">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k04J5wiQWbe-OdHLgrJREUuHijHqJw_KDIJBXUZl9mM_zBBlaO5wyYE7CeGiOxqa7MidRSKVH4bf11VRogG4RYAiWz9bLbMW6-S65ndPlYUDKDxWvkdr8uvTfOsvLjsYI69t58CVQm8rizCAJ8xc6Tmg4s3YLMYZax1UAvBMIq_YJf4mW7NrSxumxiRIvzHLpEn3MW68iNOePZcXY50sy-m-YcYev-lNvjvIlMsPTS-iHR6J9ojQHdsngdiGop12ChN4ND6REx8wqj7Zjc_bZt4EmC38yewEgadTpKqjTl6DY1G8lJ53wGbGeJeT0lHHZo5KTcQZ4rO5tViuExk0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشتون راموس عجب بدن حقی ساخته
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/103029" target="_blank">📅 00:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103028">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZiXv2pwHbFl1tjm0IOOxLCPx4q0bNR5sKs59aoNpRXAZZR0FqKZMgDOcOvmm7xZSV49UJZYkf-oiYqvVF7fZF1mUbUWsGrNy0UXD__LebvvqA7A0xZaOZuczj_Xm4D-7EnDUVoAa5OBQCVSw0qUGiE5aJkoLUE3UPU2jM8I95ojN5ZEHyBZPhpfjUHLc1XQS70f1nWVzMGGXPMOlwRvdsdYh1ze3Lwk9LM45wRg5aFSn9C0F-Gbe_imRahJYJ6AvMctOa3kvniav7dEBVfeDFFC7AItXkgtee1zGKQCSUJPgkpkYYPlcrhIT-KxUy_XPF2M-8S_llvjK4GT2tQ_YfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
آاس
: برخلاف شایعات، درحال حاضر شهر میامی آمریکا شانس‌اصلی میزبانی از سوپرجام اسپانیا در سال ۲۰۲۷ است. شانس استانبول و ریاض کم است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103028" target="_blank">📅 23:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bRdFqo9DrDFkuET0QawFzkBTxxe9FNrw_4s-YUfvnLn8WDqRKJ7KPlrfcWpCcq_x4Eqrd-d8ZzCYoPv8JFASOmbu6caMg4sb7xd1JlA3cb6SnGVg1iUl-KYbPJPvdAIjJlqUqsiravu7mIz-JVSZX4oT40rAc2Z7u11spygW3-37pdSISW38D-Jsx1uAhCAX6AqilZK2C6YHDufa0C7yd6PLZ2AOGaxK3Gds48osdUe5KoHKXZFMOIe4d0zbZyhGoPSGAubVlqx0LLxqryG0VC0HQTCo5Wmb9q41lUOuD4AxJHZDExKi1Xkzji6U2IXD36GpfpCYc-zZssPkVLsWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APuAL5r_a6kjv6jZbZ0lPJ4Z3stJZL6CaW8e8HwHWZOAmYcJdtpzK36IWmn0Gf1Y66hDe1vVY4sFBM4DbYnD6VvIfarF17Nw1LF-bGZcS5aKqgg3YALYs6tPYxytNbIYWIyt0GnRcEey6VMuxyAZZHTptjp2v8A4JD7lAyQiImobwxZ19ntnSrWEE6yDXKNa4fpy8DgmJB2EhImArE-bzQCPif4XEUxAlXVnAHWjhi4QNiXsQ_uLFeY3r5qs29S-P8M9xc5QtIN-vwS9xO4cWtiUAS3o9LfUc_IciYODdQCNzNbUaOtlEQuMzTNig63Utl9wEvSnZR1D4h6fHjJsVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔵
ادعا شده کول پالمر هنگام جلسه تاکتیکی مشغول تماشای ویدیوهای سوفی رین روی گوشیش بوده و ژابی آلونسو هم بعد از دیدن این موضوع، اونو از تمرین اخراج کرده و گفته فعلا برو چشمم بهت نیوفته تا ببینیم چی میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103026" target="_blank">📅 23:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103024">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnlkZ10BJ9pH2fcv3xghaDQradFVWkAqDrkSy7cL4wh5YTvkrfwa7STTV7IMoI6T1qnWtIPwRrlOvVI76Dy0Cpm7c_f5EuGaRQE7Jh0ZCxEQmrLGRo3g5LFMfq2l0mr3c2hAQOUjRBRK95SCzAagoSwgRNRztnSWkjhJsNCRhj_ACrx3v_DT9nq5HWrnL8BzbV2ivtxMP2CG0zlranHk1kATUK-w91Mt2uO6o06ahLH8_BYo6WC8eC8FXfGJtB_iQl-Twu_9crA1Bqpzm0-pW8LzBdzZrGYOelOOrvSdY4LZOM_ZbTovw1-n5hyellu1Vr8c2_WOdsQABqp6Z5RWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vl0gM2MA29GKWc8ODjpWS9RzZ4lRoBlMow6e56UIIJQTnNqUIm32_tZlnMfvmfIiTi-xsG0Iq2fYbJmI87Tl3_qEAjcndPToHjmanBPIjlx_JV14JC1WdY19k661beBmMvQDa0mR1uOaokOxipoJp85qKRPV-1-y7QwhQF1u5lum8Zmpy4Q6CcDKPf_Z_7YRndYW6BCNfThsWUZC7jxSuKkCKnc0OXOjSG_zKMOg8zIH9Ckfm1QnZ4X43szFpj5FCIYlhxsFkG1V30ut3fuG94Lpzd5ufaVX-0OfsWeD3LjpJFstdpe7flE8CEdkGXt_aVw2rVSf-GpaNAC_H1TTng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بازیکن مورد علاقه‌م تو رئال مادرید؟
🎙
یان دیومانده:
قطعا کریستیانو رونالدو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/103024" target="_blank">📅 23:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnmaXMFGfXyZgZ_8fTFpwBKBBUhtUT52AWn3MAw6WYopxH84gpJZm3ikGA_EPmWOe8ISBwbUWJXAAUh7YLEme6KKuSlGautRXCGB8UFYU9XZuoT3hjKKnvSFVAcIVZrjR6bbbNu6hXt4ueTLl-7v9_GBRXwGG_33tNeOuh1n_f1PNadVlGneiQuscgyiAg7secLOeeX3Q7BRNypvseG8Fp8yfDdYtqEWxbJIDt9g0W04ghI2OeCZwnmuCo5sLDp0LL2la9S_U5TCs9RMv7VprlecE1NU45wpRqEe_60QU1zmiXDc4DORzbsNzoSEZDlY4IcnveHG1kswk28O3sBb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شات خوشگل از مسی امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103023" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdg9_HXIf9pgkXSh0kABCrtzlzH3S3pVXUsw1cJmqrFe65w7lMoYpco_IQB_73wa-C1dRKh_bbrsFL_wPGlcdm-Oj6yorqTpa-NWqUxADNUELJALXOJhiKXy3mC5mqkB849X323Q1oQixeICLUzRwaRd2B_DUeA1Z0Q9LkE-HfWKK086gWixqdwjUoq6VUAm_jgQgdsSsL7bKppTzRhTENDosKuFdkP4dy2hb6z4y3V_IalZwEqDV0c9PEpMyhtwzCXSBB93jdYoQN6cjDv_8alXRGVI7MtIdw1R58_UC-0OnU-abukqv_JXpCwkucCHdIanpwemhpSqx4oRO6PQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جیدون سانچو تو انتقالی عجیب به الریان قطر پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103022" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ea6e382f.mp4?token=BYKPFLKzgdOLWDD8wPAs7JZoyRL2G3dZ1iklXnV7UooxkvywJuNSnhksYaJ81RbrJCydbmA4euGVlSt614-UR1k_MmAoyX0tNkFrXLYi2_wxXsLEy1U0PT7-0jou9Ov-ktE42T7MpUakfWIAhpNVr-Ahkr0Atabg_aaLPsotr-k08ZO-4xEYCBxFwXTwgWy41tcw1LoxK3kqoybuoeX2xiXCYXLDCz1J6TSjZj1C2tTflpQN4-Ygvi6dLY0-cDKYXFjL5_4EeKlrHMsUnDi7357p-emMYqGk-eBklC1pX2ZpuvrFHUDjeH-4Gma_J7aOc-hkk0KGeiLYZ_XJmW0AJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ea6e382f.mp4?token=BYKPFLKzgdOLWDD8wPAs7JZoyRL2G3dZ1iklXnV7UooxkvywJuNSnhksYaJ81RbrJCydbmA4euGVlSt614-UR1k_MmAoyX0tNkFrXLYi2_wxXsLEy1U0PT7-0jou9Ov-ktE42T7MpUakfWIAhpNVr-Ahkr0Atabg_aaLPsotr-k08ZO-4xEYCBxFwXTwgWy41tcw1LoxK3kqoybuoeX2xiXCYXLDCz1J6TSjZj1C2tTflpQN4-Ygvi6dLY0-cDKYXFjL5_4EeKlrHMsUnDi7357p-emMYqGk-eBklC1pX2ZpuvrFHUDjeH-4Gma_J7aOc-hkk0KGeiLYZ_XJmW0AJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چیچاریتو: من کریستیانو رونالدو رو آدم مغروری نمی‌بینم. اون فقط روحیه رقابت‌طلبی داره و همیشه تلاش می‌کنه بهترین باشه. وقتی هم به موفقیتی می‌رسه و ازش درباره اون موفقیت می‌پرسن، میگه: «آره، من به این موفقیت رسیدم.» اما جامعه تحمل اینکه یه نفر از خودش خوب بگه رو نداره و اینو غرور می‌دونه. ولی از نظر من، غرور وقتیه که چیزی رو بگی که حقیقت نداره؛ یعنی بگی بهترینم، در حالی که هنوز نتونستی ثابتش کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103021" target="_blank">📅 23:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRM7LSLrRvUMbL9el3mhrRXmLrE_bIp4QuGQ4j8La61HGs5QQjzYmTAA5GfvMRZxDLkE5z3KYlgByxhI1P-G_mcZ9BKPayyw4V6QAcvKHitDBKpMTLIhuT8KlQbo7edX6ko3Hc_ajjpu4r-DWEBVbfZdDYe91QBYvjWAFJtniBl4TxIYoWCbPn93DfmhYRt_bDjiXUEezQGUZAFYgPyY3j671FAOkPesoAc2NarHHmrQ41mVBWpK8Jhduergad2xVbcBHTlZ3qVg1zLjbTxkoYaa0_VUhqT3URNcdFHv_xIkEUbzf4VIwM5Vj97rxdE2o9McJfjbY171817g9y2gbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
بازگشت تیبو کورتوا به تمرینات رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/103020" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
جلل‌الخالق؛ اختراع جالب دهه نودی رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103019" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم  آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16 https://t.me/+5fvta-uF4QA3ZDY0 https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103018" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103017">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ncp17sQ89n-bK_jqVTXn9gSlmGkrz3HmHfv2MfyAZn-xaVU6W3G1Oi0XjPUAlBr2B554RmXKd8sf4ymcNNdC_dImEyysoIB-V1ngpWnrsj7EA4nJcISXYSoGvCnkABRe7lRuB8PCQy6Ftb2xgeplt9-UaCCv2Xg5dYsFH02OoVy8pp2eneKrHxONpViHiE0f7SglDt15oq1TxvVWuOguiY67Qg72SDVfTjo5TM3rIBi6pUxU1GiA_63cudhctJ-6CK_xrFsnIzmnRpGKPsIeiInyp4OnTPbFVpJ6K_gWwFXiJEZpK4sm_1CA2EmyMC4ExNmQWSPpfw05D5FlEALJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم
آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16
https://t.me/+5fvta-uF4QA3ZDY0
https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103017" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103016">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0EqRYZqqwzOoqPr5Ci6lW-otxcneqF7oU-u3jwh9sIJxO6y7IJvUmlUZiYCKCBBN_2sXtYFQTBUHhLP07nRDCxFpGnW2Ov9RO8BNTdPcFX2QlJQuAZLeX-__fRFyFFpbyjzePlMnuF3kscof4JJkBsKnIfZ9bnQj2hwByw4Z-A4HOHOsi-dYPkAWuVpXy6mXQBrk5MYpFvNpA3RaCgJxFIBSKYLv5AFH6kq6KlGoU8eW8yTOfYW29iz8zFfDe9-twZeRcypP-cvXTxL7z7V6Tg1zR4FyMB6Ne6lQakrwWe1GTEuzh415PNo_D4WSSmWETAkLY6dQZ1z-xGfYRP5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوپینگ با ما چه کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103016" target="_blank">📅 22:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103013">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nndNR2eOhx610itFlYMZXkHreP46eHIGRSyx0U7pwQ6ZJH4l_uXxqXdO7yUC9xcs5-eIa_13UGZ60S9zGzYv8ksLfG_kL5kacfxgrk1Nb-5CS2CtKndO_84Y1a-y4SqctFav7Jy69-ukdz8ifBtd5IFvHUwmnb2L0vWOlJ0AoabY9PBkHGZrPeBDc3hzZ9CTjFusjKAodsUSHF3ddUsk3VZHGiWfrc80TBzMRDC6FGl4oiqqrm-GydWU4veGawWmXxTQHe-kxawKkeo5KK15DRNvYuTC0-7QcK_z0du6_dh1hF5CtHZLxXH4v4aTKap_pFNTaVeX9Mk8wl64pn8b7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utMP8LXUuHuKi1T5Tp58JOMet8Bz8nLHRI-hsW5pHbY8M0WxBe3BQJXV1eDkiS-r3pyww2E9_NSgK2hfqQx3dBl3QwTgdgxtdqBJh6gOItQqWQ6wDzwpPCo-MP7B4yyzaPtXo6O1zADuP1HGbeJa_E9rH0sZzYDNNBRJwoybBSfQ5kCA_c3Ld5YkdQIqc6_qYH1ST1oyoNIOr0KN3XtEBAaWAmLgfBqc0j8z4IMXfBHBWDSZv5-Hi2fRpeZZ592SdeuwoytG5QA5vGs2ocXiq_sJaGDUPDAzZJFmSUBQmp3inVP4EQAYzBUN4l9SddpqCpqmelxmAsgGtlF1MXCBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzF-NA8ynDHNJ3nKSh98tatDT57mvgI1njE64JabyJnpjZBE7id3Wc48eQnAgD0SIPjaTuEMxs4qKzk58rfQ6yC89B9lvxwPS6kXyI1AAGLdgHlnxCAn5Rfgm22XG5WSN7IoIrXiMjiU628T-ASx3nmZ-GauxissE7OLhxm-OIxQAoKL2Op9WD-UOk5byrzQuxkxKaF6Q5YPPEHT-_2NgJcFu2RbT1-os16cpulCbRp0qu6_0PN26AHxdhcgV34gl-do63pua9mUMaAbP53pw3VO9lBn-bJUc3Casuw6L-_5-dHcSisO6nyqG6Y3xrze_C9ticUCU8InG2HGS9ZPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
اولین حضور دیومانده تو تمرینات رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/103013" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103012">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcuxpmzIfjOp6lvbP7ARaPV0ZLvrpXaxzKVK7O7QeIw7oVXgFI_3OdhhN2KAFLKqfsIGN3dhIS1J0Kc79eF3mLwCDcqml0gYJBkRT-6b9efCQjDpGUay1doc1sNE67E2GcLuHJuQO8b7lYHWLLqKiA9TO07_sioOyk7SuwMtqDy7d6dIyIWpVF-lj2KJEHeBAvr2pYR9UNMoPqbEbBkSzYoXf7lmcbScC59m2sF8uSyPBEEumkXForzDdbdZiDPEtNULNurhYK8IB7T7JrcoozIb9NBW5Gy-j6NXMwNfGsn3YDILzooMLiqvXkzRb1KMATCjWC_g0q8bjNGOt_kqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: رولی گلر مارسی با عقد قراردادی دو ساله به سیتی‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/103012" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103011">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQoIpY9ThSgFgkv4v5rNjIP1jP3OM28mmiZGEYIO0dB5nOEZlfcFgFQ5RH5i_VCYrjEvN-U0UWIXeMpb-pTDoXaDA-LNDhqikeIjRiRIVcHOwsq0O7SIqKqIVKAITZNLA0VPsiEPXnmmlb1z8VYPnckkgKQwIaha-9RRcBi9WhNIKyu67dhPqk8gxzyKB2zRiovJnfnTIKdXUGoVGSYFPuuArKFte9InUOHA0fYpCTMr1AqMjDS-zoGJK0YMlUQKMKpQfsZ55Vwil5b1RnsHn_JOgg1rLrQUwTn7MWHUmsyKJVNBkQUt9_Tls6NSFAgyIxvRYjWCtDesyZltb13_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
ژائو کانسلو در تمرینات الهلال؛ مذاکرات با بارسا جهت انتقال دائمی به کاتالان‌ها ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/103011" target="_blank">📅 20:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103010">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVx_E5uaAOpbMPfzQegfvt-cgC4_GA8LZH61amkvPRliG2atGD-uhzTmckXLZW-iOw8B743oMPJUxOVFdQuUzqrOBK-Fa74KhOhEfwIa4xO4-ktbLTsdwWAyMpXdeYYhgA1hfxiqQoUbi6m08xLlPXZvUC425t20vj_0KvwxEXMwTrU1-kQ6fXEBvmn9y2DnOo0hFIqltUC2v9HYpQYqcgHORNLS2ESVzITEgh-i5_8If7mazXxFqGOBeKkosX9LsnqWeODmUFQ6tx1Vani3FCcej7xnd5wZgGokWoBlGnmA2U4UPfDoVVz8I2pBdDIzx6ruLw-6v5zNe6Z7O_BEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جناب مالدینی بهتره یه تست DNA از پسرت بگیری:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103010" target="_blank">📅 20:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103009">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwQ32IpzeT6ta27DDOMe1ijUYjJicRA5hoptJ5SE44cLZcsP9Crcs-D01eYDru58aMe-REoxUeMUpO08nLc7j1jKGsbx1mEtnXZpd524cfijg-z_sFQZ_2EUaetFy6xD3sK5e4Cs3rsRRHy_7cMJSYInfIQXAbvJa2dfedqOCvcOKadGgAYcrHxCPgdTegazyM-dLzuePE7q-42rLzmHDD5FhSk4Pp2BRQYtRWTl3-gpqn1VrNAyJaHnbTazrHn1S16I7gIrtRWTSbhw2_fjIaOeR37HAGSznSZw4r_niHC-Zjfap1mDcEYKTh-tdnUIYI9f853Nx6wBUosFu-WJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🔵
سهراب بختیاری‌زاده فاز گواردیولا گرفته و تو شرایط کمبود بازیکنی که داره، گفته که اندونگ رو هیچ‌جوره نمیخوام چون جو تیم رو بهم میریزه! از طرفی گفته آدان ۴۰ ساله رو برای نیمکت‌نشینی میخوام و تا نیم‌فصل که پنجره نقل‌وانتقالات بسته‌هست، باید برگرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/103009" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103008">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=ET8qXqQmFfEDqw3_dTi6MT_6p8bb7yejT_3aTntiHjoiED5BKGh3bEDrImO0yQF3pAEH4kDT9KpCeTQQnsbfZG0D_9QUV7EkeI7lHiNSCmOnMz8nDH_wrdxruOnENXOG4WHnQMZ5wjdYdAGYnDSMzCU-OPfdpHA0HMoZuTC8jlbEPSomrQX5ZfOFbj-En81rcJSqxa0-NNQjgP3J6_0OgCGer873gsVyegOk-JACSYoLD2aLUb6PewUL0jIOImIOdmIwO0k27QBiIOm3okP3soG6OY2-UIIRvAlejLNdqvmq4guq9dAaC1-f9xGYP79Hi_jtGv3QGwtdU7Ch736TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=ET8qXqQmFfEDqw3_dTi6MT_6p8bb7yejT_3aTntiHjoiED5BKGh3bEDrImO0yQF3pAEH4kDT9KpCeTQQnsbfZG0D_9QUV7EkeI7lHiNSCmOnMz8nDH_wrdxruOnENXOG4WHnQMZ5wjdYdAGYnDSMzCU-OPfdpHA0HMoZuTC8jlbEPSomrQX5ZfOFbj-En81rcJSqxa0-NNQjgP3J6_0OgCGer873gsVyegOk-JACSYoLD2aLUb6PewUL0jIOImIOdmIwO0k27QBiIOm3okP3soG6OY2-UIIRvAlejLNdqvmq4guq9dAaC1-f9xGYP79Hi_jtGv3QGwtdU7Ch736TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پیشنهاد اولیه بارسا برای خرید رودری بسیار پایین از حد انتظار بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103008" target="_blank">📅 19:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103007">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=EZeIvsRKwWIdCVOMQ6-MnX52yxXn_OLs_vKnaF86uJJkgEZloVvopeYdOh3YkZNLYYl8MIHx8aAYxm2eIlW72ikuH7wkpkSchGFZK3fMOsLH_QOTQyF4QSxhLa2rhvNDYHfl9c2EA22ab9bLhihXkNyYpet4HekQ7qMoyLjjFmP3UYGqpSSUQQQsqx_xy2rBUZx6C6uW7krh-XX1mcZqL88ns7nhLfbFpKbj8N5YnbCKGL4cFxbQee2mWC69zeO00WYeSUpJvD69Q9fFELX87JOmV_vmEWUK_WkHb8S27DvQwR_uGNOTExHPden8NDhVbe5e7yZ0rb_qtkUEwBuLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=EZeIvsRKwWIdCVOMQ6-MnX52yxXn_OLs_vKnaF86uJJkgEZloVvopeYdOh3YkZNLYYl8MIHx8aAYxm2eIlW72ikuH7wkpkSchGFZK3fMOsLH_QOTQyF4QSxhLa2rhvNDYHfl9c2EA22ab9bLhihXkNyYpet4HekQ7qMoyLjjFmP3UYGqpSSUQQQsqx_xy2rBUZx6C6uW7krh-XX1mcZqL88ns7nhLfbFpKbj8N5YnbCKGL4cFxbQee2mWC69zeO00WYeSUpJvD69Q9fFELX87JOmV_vmEWUK_WkHb8S27DvQwR_uGNOTExHPden8NDhVbe5e7yZ0rb_qtkUEwBuLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق‌و‌نوش لامین‌یامال در ایام تعطیلات در کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103007" target="_blank">📅 19:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103006">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSS3CU6yaXOwhHamKAcASjy-r8Rr1iYc0Q5kVY8sV4qWYWdfz7-XvNs3zGXRyNWfrj7q_GRbgtfoLjFCRPtms8lGzFrcijILO33sRB_STXrUX-OEY_ms-MWUlX-1JpmIBcYf4st55Z6WlXR6ttdtU8A9e7Mo-hc6Ri28Gx096DWyCz8L3k0sUPUBQULDQBi2XCere8fVJNlJttl1qoF7IM5SZE7c8pkJMX-EdIUVDLDFWGMRRcRZ-k_Yujw4ADcO6bu0yETVGCJRQHzo_WoA8MX4SirMghovHrzH60Ok_nG25KiL86PN0GD_DFuLiBI30eANH-1h37sYBuj1XbTrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
دقایقی‌پیش سه‌کشور عربستان، پاکستان و ترکیه پیمان دفاعی سه‌جانبه امضا کردند که شکلی که هر کشوری مورد حمله قرار بگیرد، دو کشور دیگر حق دخالت و حمایت مستقیم را دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103006" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103005">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpecby5haGTOuMEBnsXdI2oEqPn7utEUgETM8XlTML5TEv5DuHFnTx92s2k3-ozL03uA1lMEYhKeLEtq9fSUMA1CdPRFt2hEVafPsi6YGCFnvClHVZaQXx3MypB36lfnXmo005pmMxK2WSKmvF47m2UTqYxDgVpBWTx3w7CN6VmvyvgZ-45r6_OQ7AQUYrN5VSkZPqqdewUrtMgLbkYDWB8GZqb4Nz3VZl3e5E94lL6N2PglqfHHeG8c-zOezhvpUIEesIKRMb4K7H5fJae84tNgHmNiG5SVYr5Kg_QjGVh5gKWoyLajuOqJWNz3RMrQQwES9_rv5L1z2mCJ2ZKFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین دریبل ثبت‌شده در فصل‌گذشته اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103005" target="_blank">📅 19:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103004">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsK72Y-NXfT8ChQ1vfmzrqgAxfg09r9Nh1BVP2BzG_VhHoswGTQcGhtuqhVMzIkXTRxGY2N-Jf9XseyaIXCiDWKpxmsvaYbMWuFksyPZgKm_5LvodNassimLIfVSXa5KwfcgfzrEdUVoLQ1CPO-0N4dLsnEGREMaaaCnyFIKo_txfnycz_Ahn_dXHkmcazb933_ynPL9aFsHKw4KQB4klcAXgBJkqEzrXlXUK4vZBoxPnAhK1R58VV-bkDP9uuGSaFHpAlZhoN-0ER8kJ07tyzxiDNH3k6InxINg-9qRVZo9PFIQtJkqO82H-5qMHjhWfGvk8elC6zboR36ZbsPfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
خوشحالی بعد از اولین گلت چجوریه ؟
🎙
دیومانده:
به این شکل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103004" target="_blank">📅 19:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=biRpzamYN_Xtrn6AoOwv79uIUDXK1rWiV8Hj4EsZF4tSspgNBJYpEchEa6M-15ar75411_JcKVXhmbUJysFdM3-APbZ93tX_BfnlwXASyvU3ogKmMY9C-TvoNGV9-9taAvt3Ol0hrZAH6Ud4XSakzX3XsJmBPl0QiIbphmQLPhAXt3ozN0sDrKcCLdzW9xPmwbcRbZm_PfvLNGn04Z7KhuoxS7_m_5LR78N9MHOQUmzk3NxsnW5HHxGK4ioeqsff07XYys7FgchQA5_03sKBspQ7L14xHM2jUx-xz_shWGGuVDBg_Ggn2hMfC8X5JssgrXwo-E2DhFADGL5o0zv3wQTE2zEo2hsWtdKcQ8uoN5xlYKNHOvxmvzkTKYIxgYTc9KxAy8t5p0hoK4L7LulpoQD7vj-d0Itgjm7LFxUexnYsFvzQiSYHVVozIYJobXU_MWPMeIvZ0ljlllRveiv2PeFiz8f8iPnIN0NWzyCmItn0PGv29KyOTlbzrX0ar-5G9gGi1xxAamcn5k6z2QqF5RNH3PJqnZzGLuWYt8-PxGSclnL1K-JP3xGCJVD-hNYoei2AdX6Y90DjYem1KqPl8v9rcMDSmww9TohvFmPbqQxECl1fCYdvFhmeTYezP52O2T2NoN_0uKUIs6lMaA8ZSqDrtY1_rhdSZHasBfGqGxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=biRpzamYN_Xtrn6AoOwv79uIUDXK1rWiV8Hj4EsZF4tSspgNBJYpEchEa6M-15ar75411_JcKVXhmbUJysFdM3-APbZ93tX_BfnlwXASyvU3ogKmMY9C-TvoNGV9-9taAvt3Ol0hrZAH6Ud4XSakzX3XsJmBPl0QiIbphmQLPhAXt3ozN0sDrKcCLdzW9xPmwbcRbZm_PfvLNGn04Z7KhuoxS7_m_5LR78N9MHOQUmzk3NxsnW5HHxGK4ioeqsff07XYys7FgchQA5_03sKBspQ7L14xHM2jUx-xz_shWGGuVDBg_Ggn2hMfC8X5JssgrXwo-E2DhFADGL5o0zv3wQTE2zEo2hsWtdKcQ8uoN5xlYKNHOvxmvzkTKYIxgYTc9KxAy8t5p0hoK4L7LulpoQD7vj-d0Itgjm7LFxUexnYsFvzQiSYHVVozIYJobXU_MWPMeIvZ0ljlllRveiv2PeFiz8f8iPnIN0NWzyCmItn0PGv29KyOTlbzrX0ar-5G9gGi1xxAamcn5k6z2QqF5RNH3PJqnZzGLuWYt8-PxGSclnL1K-JP3xGCJVD-hNYoei2AdX6Y90DjYem1KqPl8v9rcMDSmww9TohvFmPbqQxECl1fCYdvFhmeTYezP52O2T2NoN_0uKUIs6lMaA8ZSqDrtY1_rhdSZHasBfGqGxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
صحبت‌های روز گذشته پدر زنده‌یاد مسعود ذات‌پرور بر سر مزار این قهرمان و اسطوره ملی و میهنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103003" target="_blank">📅 18:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=Y_d2ls-InIgCKj6D2Zptc62h4qoPyPFzzSLJWNVpoQMmIFu0IEJAxuxs_nlwEbFMj56N1tAEyce0g_nQ8XGAIWNxTfPtZJMCdsYpJ-ir_iVQy4twG5TPo7vy-Q7_dZOceIxoF52yF4gjhg2UjL9npp0C69agrtOS4NeMthUk4Y2BtqfilKksXuw-iAzwYjAfkjhsZb93-l73LSaDq2MTbwGSpfSEHcL95XAgGda-_4GkgB3tbsPKr0lqVLwtULNAlGIWkx4LYooZFxmIoSX8TTZ7H7O7qEfDpPl0UBbUTGeXFI3a1fopmh0C1vge9DFAohzPEIDeYTwrA0Sybbf5xCbFl9yyGo0N7IcXxZut6xrWwCMwa4WLj-i7vNPDGjlnvfM7J9sA4fYVYp_7_sh3Pdsf2AGJz8CttOJz4-u7cXP80g71ZPg2D3p5b814J6u2u-mGoF1Lt5bEAu2R1rwQXu8Wodwc0S3DVqkX17-dk3hKKxSlla_atM9OLSnfNsB7tqQnB4pbVseGPFAFj9tK6xH-f6XDiK1-v0dzgknZZZ-H2HelxhkffscNCg8qROkwpqBVZFxX8VrZ94bbP3_zbYqSgIN7YfgBgYeIpxCwhi-ZGoOtu5MKZHVKXPMDH-FznizEkW6DyKg328N_0Vx06R-QovUjgGc-QWL28T6vTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=Y_d2ls-InIgCKj6D2Zptc62h4qoPyPFzzSLJWNVpoQMmIFu0IEJAxuxs_nlwEbFMj56N1tAEyce0g_nQ8XGAIWNxTfPtZJMCdsYpJ-ir_iVQy4twG5TPo7vy-Q7_dZOceIxoF52yF4gjhg2UjL9npp0C69agrtOS4NeMthUk4Y2BtqfilKksXuw-iAzwYjAfkjhsZb93-l73LSaDq2MTbwGSpfSEHcL95XAgGda-_4GkgB3tbsPKr0lqVLwtULNAlGIWkx4LYooZFxmIoSX8TTZ7H7O7qEfDpPl0UBbUTGeXFI3a1fopmh0C1vge9DFAohzPEIDeYTwrA0Sybbf5xCbFl9yyGo0N7IcXxZut6xrWwCMwa4WLj-i7vNPDGjlnvfM7J9sA4fYVYp_7_sh3Pdsf2AGJz8CttOJz4-u7cXP80g71ZPg2D3p5b814J6u2u-mGoF1Lt5bEAu2R1rwQXu8Wodwc0S3DVqkX17-dk3hKKxSlla_atM9OLSnfNsB7tqQnB4pbVseGPFAFj9tK6xH-f6XDiK1-v0dzgknZZZ-H2HelxhkffscNCg8qROkwpqBVZFxX8VrZ94bbP3_zbYqSgIN7YfgBgYeIpxCwhi-ZGoOtu5MKZHVKXPMDH-FznizEkW6DyKg328N_0Vx06R-QovUjgGc-QWL28T6vTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تو مسابقه مردان آهنین دیشب نزدیک بود دوتا بازیکن با همدیگه سر یه چیز کسشر دعواشون بشه که بخیر گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103002" target="_blank">📅 18:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102999">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL0Hd3gOoXxIp3ZKnA2YB1nYPufECzG5KkJOMkT77AyAnbt2LKUYKNz-RiKQaNXhWJTPBJPOqNjojeEwZTMmvSfKjnMYnRhiRP2vE6d2UWmBVdizGKbg-xgKkbJMdgrOHRt2KGLTE52FYQ6t_v-RntBqpihogr1b_MS7nBFl05RA386306Ze-h0UHZv8OvYqJFWPXLMDqKEKatt1cx2XZn3NVKcVVs8fLme9CUnOp7jtWDM9eRGIX7qah44DEVHzIOS2VMwgwcYhSlZlFFZuKVOYTlZ_P-Ylo-ljhkvyMbKHtByLVJrQmXdbal7LtjneGyPnGSJAd4SjRYS8fpjjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWSe-wPZ6xXjy6P0wuKKaYiCdanBA0IAFkwB0QeliMTcIMDYHvxrz6yTDtac3gB6akI6Hs3KXLQzt7ZUQVoOT4eQBybuGnDcxf4YRJRUvp1uMjD0JS1WZEA_Z8WZdQmd7LbUqZYf-Y6OFQcmODxUH_AP_2SiIFOybYLSexnaWJUrGwx7sjr9wdKRf0yYeT_Tt0rOmyPMe20e9mddg5-Ft57cw2T6nu_FQ1XgZd_mucP9pyNQfbTPfxI7Irck4RM9vZNNjInkCLS9ckMAaGNBUYXIItTgep8Wt5W0fWYsb2ytWRq-HtjBt23ts542x_ziWLDDL3b3kUDJC3i9JPu7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMB3KisPyQu8xYIlf0mMKRyY8kR0fytcyAZiF8wdMgzB-_EeFdod2Hd8QSJLymwLSiHwEou7vrRnfQEaQtghitaUM10b8GIceOBp47IQOdd7SquimSEpoXvtJRikAOg1NFB0-fyJ53KmuD4oAm24pjCH8IwhnPB_3SC1TVC0PJ_XD264S-sttYREa5EPyvJsVYzL_72ZLZd3HxDyjhtR8L-NQghOKpbb3q-4uP6grfOkIG3XHK6-y-DZ8BdsNa8UTYLwtFVVOHynFkuPLoKoYRoxWx02OPbIxCnzMuzKdZDEwi4GX4nYojXw53sdpPxIMysIGSWZQmRqWPVB7RWVoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102999" target="_blank">📅 18:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102996">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBgapaOaGtG1eM8UOKUMmaZFINBXxnuV3c7ipx0u5oVHFHIFriD_J4XaOgt2CX3d0O3RJ-9hW0FNbAX3h9I3dOqvjCUadE5pivtOQrBFNr3GtauUG4eXmziIHW6lvavtGmF6wPGjHPLOhioOIik9ZgUd7kvEswSLhXzigybDXBIoHrIi4r-VxpJOZtrgIT984zHYtsRKQq23h3WT57LfPUdyoocD7871FkN2r3NPX2pUIzBn57CUNGZLTC2bZFvthv_FiuKY3dKkG0A3ktMyRaXCEIFHXrBGHu2VCdNYT8QGzYTSGBighL0KjFYjGBCS8y1NtFlAVcKFIUjQjeaPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byG-6E_DjEx782N_P4gxbgRpNpPQelw4-KNo-HJ8qYS4dG1u5tmsCZkS0bqJCvCiNZBjvWEoNYb7xnN0iRuzyzPWXqpd0R26SpSl72eRcHxKzpqZwd2eTSTJB6kmfpSMNb3sWDS40rFHyu4Fux4dVcsp0QjL890Ne81Yq4fUdj7eVykzPafcPfXYyKyjQEooJYjCgiqlO2pZRXdFxa9zJR4EEuMskZFfrp7GHRTNYMQDImaC1PONZQLkUbZF2tupHMhlA1J12cMVC2kBQlerUW0eIWvnzYxJ4ieJLO3NyHrN1WakkGIQOfIeD43wz5emMeNEYP-T_EbSYUpxQ1SVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvKSyds0qk3afQchL5rG7EUTZ0CTC1YT7Fb9jTTrb6fG3JZaSb4SHaOsFwlmi6rhJkbnh4AoxqGNLIE6bbNZA5j1ovxbRxCyLGnS4UILHWb9uuMUhs9JVJT_GAsxGuzsAewDi885wcTd225G38E_j73i65ZHfkFiZ_KKoEwyaVo1HYnIFZ7T3RR4JKCdIPpnIW8A3PgtBAs9k6KvvO-byqF1FJyzxEB2PJ1uTu5g1RohY9hRKqBQhfN909V4Bm3poxZ3Uw9iX65Xw0TCjUxSfPGbqK2LOzZnCUfmMVSxnDeGfxUy5klMpU7iqXIvxwKtbyppl3M37aD7Rs8F9aAkow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102996" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102995">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3QFHfBb23W3o_29-pcBnN1XEOnGSUDqU2Gfbzp1nsaOBteN3NLhNj-oREUOLt-WeTbcF-yMaz0yPPRhw4Pt3GwCGGJRFGhh-a6zX6nOXXUtvOTwWUW4B3QyzZfPYRrVD56b_R7OgVJm2paIA5IERTulnVOrcJfuFJ_JkjZZ_aEQyr0Jf89R9oJF4M_UY70HDiiJaqObZsEQYaJSDM_9f0O4ASIsI9DEl2ThaVTPtxJhgOQ5XZhDUq2eHPjtWnhF2WBlGjHNA4pQ8PyCucDNYmjszYbYSggxNcdSOZ0gFzKsLXQ552YfhIS0iyK_Fsa7cnTmTeWLpw8H5B4D1HTJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیومانده در تست های پزشکی رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102995" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102994">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
❌
#فوووووری
از رومانو: رونی باردغجی‌ بازیکن جوان بارسلونا که در فصل‌گذشته معمولا ذخیره لامین‌یامال بود، به صورت قرضی از کاتالان‌ها جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102994" target="_blank">📅 17:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOwpflDIYXSiIAczLWOqj0V3lUrYDpnIeLdT_0E2m-7BG5gVPd4_YOy0A2evpK_Rdw2fxtI-uOZXi69wWbCRN1qw2LeL6oj4Xr8AUlU-LB60Kv4CVuJ7nOzUV2gpNr6jyAKt4g3uxd0B41iMVR87MvQa1hXdYUf3bTpdsnGfHr18jkNZPbWQgYOTuTszCDC9hblg8SQBSY0T2bqtbGuJPiIYH0EJgxan5aCEKhUr94dEwWbXtzM4BkYTzKFLCmyazlj0P8KNd61LBCbohnSL3ZbVonUtfkFw8IbwAos21Y_6SQzR5Phgp1h5LzH5GsHCpOfUc2aI2Gp0gECB8qpU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
🔥
🔥
✅
بنظر باید تا اواخر امشب شاهد خبر HERE WE GO رودری باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102993" target="_blank">📅 17:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102992">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txei8WbWxE2RDmmzJ7UfdIKj60PdyzicHmXVPs1pzYIAhBJGtS2eQcYA9yglA7WUlvfM0nosk3y9itIO31L_fGqr7XJSZKDaMInWq3sgVHlBZHb6Gu5q_4BvkiV2PXQr25mG7z6aSxos2m7tYW5DaoiQyfzBcglFVRMVL534DSo-MmqEL5grq2xmp_icsJGVsH2KwQYGeVYLxt3dQm0UJXAfaVbzK6qTtFkB42i7yvzceMh60mQeHIe-zBavrk6WQbk3tCcisDS2qfHTk8499wvPe0QpBX2anVEO9xPPTzCZeZZ9rXLvvAXm2g4sJZO0rHrtq-83Ul7uNMkU66WadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
#فوووووری
#تکمیلی
از RAC1:
🔻
رودری روز ۱۲ آگوست(چهارشنبه) زیر نظر هانسی‌فلیک تمرین خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102992" target="_blank">📅 17:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102991">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از RAC1: رودری با مبلغ ۵۰ میلیون یورو به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102991" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102990">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=k_NPgWEjrIyVb7leHviwiR5l5wnsXcxCghNyhf1e62YtuiaY3-8yJ3RW8a4arzhQKvgsq2pPxM8HjC5pOxqMFygCuU6BJLavv0yU3srr9FbYAg04UMawGyoX_Z7CmkGo6tGFYhf0G4Gl17xDndwZ5njBg3_3JG7qrnEPINzbpl5kdaQJXfrr-L5Ji9E5PLPiFIrVXOIyl6KfkEbeguMj7BpEGzj-wyExap-JWrEZKsPSW9SLHeQI2hUWnDeZNjFvxbR44m9z9uFxi3zAnif80j9uJDX4QpX5umNuUQtEXJTKRoa0xYaiy4KF_TkSlLicd78HuoD9t92tjseB_DGGDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=k_NPgWEjrIyVb7leHviwiR5l5wnsXcxCghNyhf1e62YtuiaY3-8yJ3RW8a4arzhQKvgsq2pPxM8HjC5pOxqMFygCuU6BJLavv0yU3srr9FbYAg04UMawGyoX_Z7CmkGo6tGFYhf0G4Gl17xDndwZ5njBg3_3JG7qrnEPINzbpl5kdaQJXfrr-L5Ji9E5PLPiFIrVXOIyl6KfkEbeguMj7BpEGzj-wyExap-JWrEZKsPSW9SLHeQI2hUWnDeZNjFvxbR44m9z9uFxi3zAnif80j9uJDX4QpX5umNuUQtEXJTKRoa0xYaiy4KF_TkSlLicd78HuoD9t92tjseB_DGGDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای رئال: اون دو هفته ای که ما با رودری به توافق رسیده بودیم و وینی هم تو راه آرسنال بود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102990" target="_blank">📅 17:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102989">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=jSumUgipvAtA3njLdI3murKirOY1SuEcUvvvmteSUXYOBOiLWaRA25tdVsweUaNzCEm6iYyc0LuZnnAWqCOoBOekJqOkP_5OCMvu4i_3ynP_Mx4J8evX-r7yO8VHC2iAZtQSvGPYQZ2H3H777MqMRpRsZ9FNp-QiQxHjLrp31Hmf64S95J10-k3E31KxWJe1u4jmjdZdaBOiND26Dxk5CRhrMqUKP0uAAHOMNhBkNqi6nub89iOOaqvX8HyXwwaM4Rz2h-XPwVwxMY76HA1cFbJUU21Mk0AkNtnhjC1BDmbL3R1ImYS56jvzAq3UpSGh3epV4LWEjPKjelbJT5Jw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=jSumUgipvAtA3njLdI3murKirOY1SuEcUvvvmteSUXYOBOiLWaRA25tdVsweUaNzCEm6iYyc0LuZnnAWqCOoBOekJqOkP_5OCMvu4i_3ynP_Mx4J8evX-r7yO8VHC2iAZtQSvGPYQZ2H3H777MqMRpRsZ9FNp-QiQxHjLrp31Hmf64S95J10-k3E31KxWJe1u4jmjdZdaBOiND26Dxk5CRhrMqUKP0uAAHOMNhBkNqi6nub89iOOaqvX8HyXwwaM4Rz2h-XPwVwxMY76HA1cFbJUU21Mk0AkNtnhjC1BDmbL3R1ImYS56jvzAq3UpSGh3epV4LWEjPKjelbJT5Jw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مسابقه مردان آهنین و فرامرز خودنگاه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102989" target="_blank">📅 17:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102988">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQy6QBThB5Dt94-xM3GYGr6gYJicdxAqsHuYEX4pJCzlfvks_T799nvmu7A63B9DlAaKgVayd0PYVAlLiVCbp6Q5mKrceMcTCFAK2Z4PKLdBRJbZ7_WmlHwVbf_FMuwFAtYovIkANr0R-JSlnxn64FLYwamShfNKeZpbAHuAnnHGfWMtaRToz7Jt451VL5RJ6_2adK7wCdVPIDrODz2h86P9A3b-eV1kH0e4149e0Fn2JnF-i-Thx2TKrwB51V-0GnsqqPixH-tlW_xZ7Bbgyf55R4qNUbKHsYmIjZb9Czd0QZYoXtFFCMDCU784xbyfZ7oUKqz4n-92LnJw56A5eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
اورنشتین: بارسا پیشنهاد ۴۵ میلیون یورویی برای خرید رودری ارائه داده؛ درخواست سیتی برای رودری ۸۰ میلیون یوروئه.
📰
رومانو: بارسا حاضر به بیشتر کردن مبلغ پیشنهادی خودشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102988" target="_blank">📅 16:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102987">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=SMbVjTIHmkT6bbwLLvKzP3zx1UCMRa6VVzHtX4VBCDjMSl1SDqIfV83EZLwLZh_LcImL7qWFbv38qQnFpymQ8Mzprdly81H61os3nP360KiNuILdI8pGl_rAwhk_Gu-sNEHyWU3ao0OmksuUUwpqFevrfrKaH6tNT4efJR-5jgPpUO4qnBsw1htFHtaApt9_O38PNShpum_osH67aLxTnYuOT-LMmdZ-YAU8dtlNvSilTVf4HXoQVG2OA6z3wUmnNLsAUmu2JJ67XYP9I_C6pscqSBQqM-jHqBxzfV1syKpnY6YapqBP48ZvB9Rya_RiYOepsfO2I62gmv4_uR6jxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=SMbVjTIHmkT6bbwLLvKzP3zx1UCMRa6VVzHtX4VBCDjMSl1SDqIfV83EZLwLZh_LcImL7qWFbv38qQnFpymQ8Mzprdly81H61os3nP360KiNuILdI8pGl_rAwhk_Gu-sNEHyWU3ao0OmksuUUwpqFevrfrKaH6tNT4efJR-5jgPpUO4qnBsw1htFHtaApt9_O38PNShpum_osH67aLxTnYuOT-LMmdZ-YAU8dtlNvSilTVf4HXoQVG2OA6z3wUmnNLsAUmu2JJ67XYP9I_C6pscqSBQqM-jHqBxzfV1syKpnY6YapqBP48ZvB9Rya_RiYOepsfO2I62gmv4_uR6jxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات گرما روی رفتار مردم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102987" target="_blank">📅 16:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=Use_ISepckCJY5uxwUv_9cVSvMjgFAWSTU1-k0ksgV5tIE_WSg7PYITvlNh39sarXpD73z7YXYuidfUaoSOVspbyWmNXnLxUpi9NRKeZTAtFVqjpsiDi_wyJGe3eey5fMw5QALNkHPOYc5g1l07jYbdYYCmL-2Tn2pQFo3jWdfwcUKCmiJ7fu3YnPZt-ontu6A-CX0S3b4nVXqp_OTNjx7PLq6VLX9iJasyP1sm3Rorz1XZzAyebZymkglGipWfV_Lnu6QJwNY0L2rHpDnm2rAxvjAVD7ESXt1VjCcJmDpVZrdhlAgEwsyw16ZCi4tBBghfkthsvIJWMztPp3nNJpyk0GXicaCr1gqu5ScJ-vDEikObJpwAGJ8y8GcH0VXiEZ15-fb-o15exQ8tNtmnXU9yvKF-eHpnG9uEplERRV4yoVA3QAhgp04EqJb6vXDPmaYr3FLU1gKEEdHKml7Z2E_v6U1is-dwTed0tymGQk_Smxhugky0s1Df-BQvJMFPq1FPaCDLnHLDDWtIudoVR56-11HmeX4cvseJZdBH6SDtWhBvq6bJoFxRKcRbrgoCQD3-srB_HvEW3DZVmnwU40MXuvNyH-nXw7E2g4nCqcbWJWvfsqrzrurD8Rj0y-n2kfTKitEl0SgAFiszSgIoSDQkwavXQQbpBCsQJdYFsxo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=Use_ISepckCJY5uxwUv_9cVSvMjgFAWSTU1-k0ksgV5tIE_WSg7PYITvlNh39sarXpD73z7YXYuidfUaoSOVspbyWmNXnLxUpi9NRKeZTAtFVqjpsiDi_wyJGe3eey5fMw5QALNkHPOYc5g1l07jYbdYYCmL-2Tn2pQFo3jWdfwcUKCmiJ7fu3YnPZt-ontu6A-CX0S3b4nVXqp_OTNjx7PLq6VLX9iJasyP1sm3Rorz1XZzAyebZymkglGipWfV_Lnu6QJwNY0L2rHpDnm2rAxvjAVD7ESXt1VjCcJmDpVZrdhlAgEwsyw16ZCi4tBBghfkthsvIJWMztPp3nNJpyk0GXicaCr1gqu5ScJ-vDEikObJpwAGJ8y8GcH0VXiEZ15-fb-o15exQ8tNtmnXU9yvKF-eHpnG9uEplERRV4yoVA3QAhgp04EqJb6vXDPmaYr3FLU1gKEEdHKml7Z2E_v6U1is-dwTed0tymGQk_Smxhugky0s1Df-BQvJMFPq1FPaCDLnHLDDWtIudoVR56-11HmeX4cvseJZdBH6SDtWhBvq6bJoFxRKcRbrgoCQD3-srB_HvEW3DZVmnwU40MXuvNyH-nXw7E2g4nCqcbWJWvfsqrzrurD8Rj0y-n2kfTKitEl0SgAFiszSgIoSDQkwavXQQbpBCsQJdYFsxo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وقتی صحبت از خایه میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102986" target="_blank">📅 16:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=nCOeQqvJX0EK2Mxn106NjF6g3orc8BFX_eXiSWJybjQG3usWqOD8LPsDqOxUqAj7NhYwPhzEONt_qlHeW2ufZ5BD8S2KU5w0W21EpYzfsb4gDD_y2WC8VxaDUNGJ7QLZEMu2QGIs7o-m0Y8BJVT_ipoJ8o8_DIa1YJYWUWKypliPULEChWlBqT-99q2FSpMIdHC06HCQcH4x49LRBFOZr1HhU4ZEgGFXrfsG6nG6SBfG7YjUAmUA4IRID7IyhQucdMpYs9tdbiKvGoD9HZEEftf3l3Yvnis75dhRmziJu2oMFXD_cUzUTIJx2nK1nEoA7UGYrMTSdDw-W9yZCV5Aag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=nCOeQqvJX0EK2Mxn106NjF6g3orc8BFX_eXiSWJybjQG3usWqOD8LPsDqOxUqAj7NhYwPhzEONt_qlHeW2ufZ5BD8S2KU5w0W21EpYzfsb4gDD_y2WC8VxaDUNGJ7QLZEMu2QGIs7o-m0Y8BJVT_ipoJ8o8_DIa1YJYWUWKypliPULEChWlBqT-99q2FSpMIdHC06HCQcH4x49LRBFOZr1HhU4ZEgGFXrfsG6nG6SBfG7YjUAmUA4IRID7IyhQucdMpYs9tdbiKvGoD9HZEEftf3l3Yvnis75dhRmziJu2oMFXD_cUzUTIJx2nK1nEoA7UGYrMTSdDw-W9yZCV5Aag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گذاشت همه چیو رونالدو انتخاب کنه
#احترام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102985" target="_blank">📅 16:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi1o7c7UOd4wESqNhDwFfdCkZO-rRh7yOdcWIEFnGdZj7_SzzEW-lJpu7gkMe3_upf5anJvoS0y4xdFRkHwkmuOUYYSnjfeHNrPVMyX8460vRqRzW_Ab5qLGLKxcPaVcgdLJtgwUK8Djg9_SGtCejjCg8csieveZuM2GGteGblbdc6C22gXWCSIkMz__IraapX5y-0_5iELd6YoRX0PcZ7wg5BbdeaYMrkU2rTm1eYBuBsQQ6RILOYeej0jCGKfwlzCLIfd_UJ20NZNdJhB3ido9EIQOlJj5KYcU3OfNpxN_v0vo23vj2Oo8oy_2Y-vRKVq3F2Ls19NeeWATAS856w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
منچسترسیتی به توافق با لیل بر سر ایوب بوعدی نزدیک شده است.
این معامله در حال نهایی شدن است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102984" target="_blank">📅 15:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102983">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=hUMJ7MF5uMnAw8GTfewduWjbBMyZH0oR0ir0poDSEoc6O89J3uBZBe9J3YyN3j3D10EPiolLrU-EB3B_Y7QCmCXYY2V4_P0Nxi69x7OlJknCuAmSi5q-HSY_cJkYmsr45DD_vJ_aOGx6TFq2lRdLHVPBdVFas2t-mAoP2-4oNT5Ov7m3LvU7SFKm-_XFClXv0HTTribkb9dBBjF1OZ6QICo9vw21Gm-fvUGohkJaGgbLRqSg16IPrGD_v_WShm_fjHi26nxtVTrhaXWL1mggJAhrhMZBrLZk9CeVKxs0BLOjMvvycZGR7KDNug6QhJgpi2TkreiasBjJN6C1rwJqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=hUMJ7MF5uMnAw8GTfewduWjbBMyZH0oR0ir0poDSEoc6O89J3uBZBe9J3YyN3j3D10EPiolLrU-EB3B_Y7QCmCXYY2V4_P0Nxi69x7OlJknCuAmSi5q-HSY_cJkYmsr45DD_vJ_aOGx6TFq2lRdLHVPBdVFas2t-mAoP2-4oNT5Ov7m3LvU7SFKm-_XFClXv0HTTribkb9dBBjF1OZ6QICo9vw21Gm-fvUGohkJaGgbLRqSg16IPrGD_v_WShm_fjHi26nxtVTrhaXWL1mggJAhrhMZBrLZk9CeVKxs0BLOjMvvycZGR7KDNug6QhJgpi2TkreiasBjJN6C1rwJqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسابقات جذاب دو امدادی المپیک ۲۰۱۲ با قهرمانی کشور جامائیکا و رهبری اوسین‌بولت افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102983" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102982">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=LTPq7Y49bz8YrHYW9HDXatcE8jbVD27YQzs96cy0FUrtCzmRuW2T-3RvhYxS2Ys0V4e-jYuPEdfUomsfjQv379pVTrtPPQmBdoDl6SWDgT6jAgiigyb2cqby3Cs7-VqQbHmh98a1Q2k2YP344AAOEr9ZlEV-p6h3kAg7R39quFeWx7VaVoKV7phPvtD651FQ6cU3YgnGC9Ha9TVKkzjwe-GxJgImuCwCtkxXbqh8iVYK2_OhUMafBke98wD4jkdwJ3xaM_u8qu1J3eFfCha4DGCaCI53E7UNAVbf0y-StkLUcj3nHDdhqbezGDsqD5o_e8T-7CLI_uOuut5LoIgPbrBtGev4_Yo7_ieeShvjx2fPDb9FLTfJo0XAPIxPhqxLpRtni-fL-u5X3fHv_se7XHOpvRKhjLMRP78hjYlo5VWh19EeGdrBwxRg_r0RuBhRYRgcB2FjYt1VpInSa9rWqoj9SfdXhgIWYJTpoNEq7Zm5jj2KvPDlNKhbKaa383FNzgTn0T01eE7l8FknawBZPnu0owiXfO8pdSpKEiyYorytZr7yo39ZzZwjwg51a1CdSp3JSgx6LUpxnA8x7bRKrP5OBy8pOT04N9_x2KViAMXwPgfrbeE0f4xdCKaMhHT3Sca_AZywa8BkrrPWeCKbjl3VdF-PChZaBvNuG161Pjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=LTPq7Y49bz8YrHYW9HDXatcE8jbVD27YQzs96cy0FUrtCzmRuW2T-3RvhYxS2Ys0V4e-jYuPEdfUomsfjQv379pVTrtPPQmBdoDl6SWDgT6jAgiigyb2cqby3Cs7-VqQbHmh98a1Q2k2YP344AAOEr9ZlEV-p6h3kAg7R39quFeWx7VaVoKV7phPvtD651FQ6cU3YgnGC9Ha9TVKkzjwe-GxJgImuCwCtkxXbqh8iVYK2_OhUMafBke98wD4jkdwJ3xaM_u8qu1J3eFfCha4DGCaCI53E7UNAVbf0y-StkLUcj3nHDdhqbezGDsqD5o_e8T-7CLI_uOuut5LoIgPbrBtGev4_Yo7_ieeShvjx2fPDb9FLTfJo0XAPIxPhqxLpRtni-fL-u5X3fHv_se7XHOpvRKhjLMRP78hjYlo5VWh19EeGdrBwxRg_r0RuBhRYRgcB2FjYt1VpInSa9rWqoj9SfdXhgIWYJTpoNEq7Zm5jj2KvPDlNKhbKaa383FNzgTn0T01eE7l8FknawBZPnu0owiXfO8pdSpKEiyYorytZr7yo39ZzZwjwg51a1CdSp3JSgx6LUpxnA8x7bRKrP5OBy8pOT04N9_x2KViAMXwPgfrbeE0f4xdCKaMhHT3Sca_AZywa8BkrrPWeCKbjl3VdF-PChZaBvNuG161Pjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
روایت سبزی‌فروش اوکراینی از حمله پهپاد روسی که جون سالم به در برده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102982" target="_blank">📅 15:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a246a820de.mp4?token=EUmBPsNR1NRj1d3g4ZtOcrywdB22jbc3UkXo32yIaDtwdHeaIadxf4sDKlq7DqgsSXj1G9p17HKZg3QPDh9wi3xizYlxIilVr9-sTlhbBSXzU7XN93MQLu93BtdNZA3Tes3DsDznUAuWJ7bH609tSlJHWGM8HL-IjS9AGiEvxP0w5ZqwLe5tHIuKfLZifnFBBsxst1u1-WlfGZNzq2sj9zM9V9E2cWciR_GtmJnI1kfwRhHVVoOZKuQNMMCA-C924hVAYyIoetNzoGB2vm6zgZUcS-mCMLb9DdP0rjK8xm_UyTBuYWz9aDL1SRSYP3tMw94quSHA3YbYorScteZ68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a246a820de.mp4?token=EUmBPsNR1NRj1d3g4ZtOcrywdB22jbc3UkXo32yIaDtwdHeaIadxf4sDKlq7DqgsSXj1G9p17HKZg3QPDh9wi3xizYlxIilVr9-sTlhbBSXzU7XN93MQLu93BtdNZA3Tes3DsDznUAuWJ7bH609tSlJHWGM8HL-IjS9AGiEvxP0w5ZqwLe5tHIuKfLZifnFBBsxst1u1-WlfGZNzq2sj9zM9V9E2cWciR_GtmJnI1kfwRhHVVoOZKuQNMMCA-C924hVAYyIoetNzoGB2vm6zgZUcS-mCMLb9DdP0rjK8xm_UyTBuYWz9aDL1SRSYP3tMw94quSHA3YbYorScteZ68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇹🇷
جو پشم‌ریزون در مراسم معارفه محمد صلاح در ترکیه؛ کشور‌های همسایه ما دارن تو آرزوهای ایرانی زندگی میکنن...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102981" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102980">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892883543d.mp4?token=MSl_Gz1vqZ6G7T_KIJkxvMA6CwxPx0YDyL-Qag-SjPTz-bEcoynztz_HRgzF6uAsSFKKb3H3aC_Wj67SDh_9YM3fQU1xUQDBf9Pw5fgz9WToUV-cONK-mDVpb1Tgc9aihYHo7jjknwy2XENAYbJy0aVc2VLmdxSMqSWpxmfyrFOb1fyU6bcNxXgB8cXOWLlsN2t1brCJ7VOkr7KpHPHki4r6lrWqkQeF8mRHNs1nPwHLijyN_a7oyOJoKdBod5piXfXIUShwGdRXgVgO4bjUW2dhW0O02OrwkbACppb4M4U0tJk7DfPQqotHBw8fe4qt_Q7kr5gRMYg56CvSp3rNojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892883543d.mp4?token=MSl_Gz1vqZ6G7T_KIJkxvMA6CwxPx0YDyL-Qag-SjPTz-bEcoynztz_HRgzF6uAsSFKKb3H3aC_Wj67SDh_9YM3fQU1xUQDBf9Pw5fgz9WToUV-cONK-mDVpb1Tgc9aihYHo7jjknwy2XENAYbJy0aVc2VLmdxSMqSWpxmfyrFOb1fyU6bcNxXgB8cXOWLlsN2t1brCJ7VOkr7KpHPHki4r6lrWqkQeF8mRHNs1nPwHLijyN_a7oyOJoKdBod5piXfXIUShwGdRXgVgO4bjUW2dhW0O02OrwkbACppb4M4U0tJk7DfPQqotHBw8fe4qt_Q7kr5gRMYg56CvSp3rNojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
سرخیو راموس: فراتر از یک مدافع.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102980" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102979">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kLdA3bPFYsRDZl0HZPewNHwuiV5H21O5Uv1f4pJPSUCTsibveg99mN2gHfJNiMmQawvpXzUWAoTVTnwjNwNTOkMFYDh-5p_4PIeCFnUOcmnM3LTJu7VFAzd84Exs601rOq9wThb1razZOz9RB6i1kTMOKQy5ZlJhFHqrfNYm127A-Yw9oLh_W0APQXh-82lLC_Wf0AhTXa5viOP95ksCZqTKGvvZN9tW6fPcAJ5UuR3MAI7uAx_NBtcgiPeAwMzDAh01R9pK2l_VWdgBZbfDHzIdH_6zJOU9kHd9VSwiUSG7pR516gP4HtiOlCFCLyknXJ1kbnzc3UVOWmIxB2XZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: روز دوشنبه قراره یه خبر بمب راجب خولیان آلوارز بگم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102979" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102978">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvsHaZ8ycd1UAACpTfA62JsEU5VNon5Qk6NnGoNiLSdol-P0KAT-f0x7eKiM5L1R13mKRXFA8zPvSsZOoX-bdIboDgXuh0udHlFQOxJkfmpSeeQjnqaaZ0BVO267-dhP7Pfqkhy5fuZRxsEqyvBlbtlaTY5LbEVZwV5nhbqbRnlVC80rPcwQpAkL_Ah2zJ74ByqoQHoi5xDG-gF_wNjsyFA_iFDbg5z017zdigyn2sE_0VtH-KoWs_jarE5kWFmRcuL7EhIKBJnz6V9tGQ-C8fU1N0297COC2OcNHPzvq_wc0ukSlARk3Lw1710BGTS8IL8I_A1vYK533GuINdQ0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
نقل و انتقالات تابستانی رئال به پایان رسید و رئال مادرید معتقده که ترکیب تیم ۹۵ درصد تکمیل شده. تنها استثنا، پیشنهاد بسیار نجومی برای یکی از بازیکناست در لحظات پایانی تغییراتی ایجاد کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102978" target="_blank">📅 14:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102977">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZhq2NUGCqvyLg20nGsBQYkWpeJ05ZBwprjoY57FYaCx96xOt2qzX3NFw9C_lIeondpgYp-Bo72-vlUKxGOIFRGMIOODQtWu_80p2mSoiiQqZF_k6t5RNF3GGEe8Zs0KryZ2zsKSee1fyUi0z0ahtYsIGGDV8DMLGLKy4yGE5HW4JRUH19qwVK82anKNNbl53g-Ku3WpN_p26wRMm4cNZST10emtdsg5GIsVVGKryiw_seRFzv1aIBKX-ZsKsf0udkFmzlz8YwbTfWLVhHuFJU8mfFwqnOA1niSLlRB_CVqX1be2xOF_cxJc9rJQJyT6PEuQSJpa1CkswmUPGKfQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رومین مولینا:
آرژانتین، جیبوتی و مکزیک از جمله فدراسیون‌های فوتبالی هستن که از جیانی اینفانتینو حمایت میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102977" target="_blank">📅 14:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102976">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uzy-gO40cFu8o3SRIWUPAAEvcXR-1XzEPKzocxe05xN22cx2x07LA2MRQ4cbL-Aoej4NRE9lrQDxq6-cR9GfdImeteYGJ6GoHCGgb5KRGayxfXxHTu4q8_mDc0OLqV2gUrvw4H-4OIU_rxrX58CR9S403Kp3sMqnV-W53R97dDx27JebI2GfQ_vLyv5L9MB_NsAnMvi71niEE-9wi6BewLeahk9llNLJqG3LzSQo9vYyAInANk2fbKVK-3-qmuscYAXMWZp9bG49RJ3_DZdx2aviQvtsyzC1Q-GITZafWiWX-0IEJDOYtiUQpFrsB-T2TH35h5ZWfi0h4MsmoqriMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
برخی از ستارگان فصل‌آینده سوپرلیگ ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102976" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102975">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra7l9KNQnIaVRCu0wI2xaVeGvKH3MFtWQvVedHo_Y5kolAA8iTqqFARQtYDEQAh3cagVEMX-zRZfCNHobIwS-ZRcGh7Yte-32l2sQQFSfw9xy9Re59Xm-PCcGe-VlPFZRbwha0sugleb1gbM3kEktkQUnx6HBTWLEtoXoqguf9_qD7YoNOo8ZKtra2qjk-7gijexfFrSzbNH9619ovXKznaU5tVGP26rkWFPtKmjy-S8PNwQXB6jjZEZIp-wo8ExJ9Rczr6RdIxEdIJdmEgLh1zqZuo28D3Tv35IA6L_jJdKZJbcgR1UhCnKu-pQJIYSF4H1NRvzEbGjuyuEFPcbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسطوره موسی جنپو، وینگر فصل گذشته استقلال به پانتولیکوس، تیم یازدهم سوپرلیگ یونان در فصل گذشته پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102975" target="_blank">📅 13:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102974">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itHNz3zXW5y920Df_EiWgDCtYwiMOMLawtzfJ5EvWbRmZzhnDhYyYO8e0a6EDy53kSPZMco1bnxZMtQFj2Upqe6JRSADNEw_Caj2eLSnkrj2trvUiOwT498EBR8PZRcRzPRRuJ9Mpwu57F_m8CVpt2uEGs1mGK_NMmcifuKGMdl-Wa-OzD5v1vtjE6dsFc0FsVrzjx6NJytWFNKLCMZHO1m4sely7L5136u9xOiAhrBYdAkRyPpu3TwI3fNN1MoBRa4UXL04grnHwfobtl9aThgRutJGzIeofexAO_3F768aYML-gljH2nWukCrhAMpfO1uol7qQjVIhCWF_4WYJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول برای جذب بردلی بارکولا به توافق اولیه دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102974" target="_blank">📅 13:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102973">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=tZsfSTm4W4_ZbK3p55K0qB-J1XqkaajDnk5EC9W4YwcD72PK1yqtUifbdiTq1gurjA7UiEnyZcoERNor2s-kRSHT93_xH_y87sEX9ovA2EiG7uHo-F0d1suyGulfsBTxjJjohw-x1HyfJ1-n7MGXJGIzZ8PYJ0m3_xdMG45tIz9ED55dPD0FzTXATbFAWnFdd14Si38FOqnYBN6vPY2Il2ko3pF7-_LStLTKF9lVTD46xwSMg83fMOydr70ddlVMDE2Iw_N2YZHscVJNvTxfVCmw_FrOAI1i-0Gxs_kQTcl2aGWby1Janr-YbDdSd7SQNIaC0L7brIvZAYXJhsf7rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=tZsfSTm4W4_ZbK3p55K0qB-J1XqkaajDnk5EC9W4YwcD72PK1yqtUifbdiTq1gurjA7UiEnyZcoERNor2s-kRSHT93_xH_y87sEX9ovA2EiG7uHo-F0d1suyGulfsBTxjJjohw-x1HyfJ1-n7MGXJGIzZ8PYJ0m3_xdMG45tIz9ED55dPD0FzTXATbFAWnFdd14Si38FOqnYBN6vPY2Il2ko3pF7-_LStLTKF9lVTD46xwSMg83fMOydr70ddlVMDE2Iw_N2YZHscVJNvTxfVCmw_FrOAI1i-0Gxs_kQTcl2aGWby1Janr-YbDdSd7SQNIaC0L7brIvZAYXJhsf7rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
این شما و این گرونترین خرید تاریخ باشگاه رئال مادرید: یان دیومانده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102973" target="_blank">📅 13:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102972">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOcPxg-xxtDVDeJJ0JLF1bDoe9uxhwpkfC3nKSOYt_PZoq5qzTDUZldxvghAGdgLCspTrKmW7PED7L9-ULrZ_2G9w3DkAn7ycl-wtPEKkBarivfueP_lvjPhebt1ZwpaUexSvptM0RBMBFWOh9Q6yBrCuHCDKLpFFSnmoBYgFdVkrkVn068ys3cjWYuCDv3hTaMZBEeawA-R7jbhxAZScivDRB-iP_-xFLlyLXxVckEsJHMtsp0yHI1Y1a9BBNCi8MrgtBPpZzSZBm5JsfCG7mA0pUp9_d6LzSO_tLKucZTK_nEdnKGiHHQhAshp8ChAutbnNDi5hCqoB8HGtRGMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
تتوی گابریل ماگالایش از جام پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102972" target="_blank">📅 13:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102971">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8NGrSm6w5dG0_EbYvrUwtBeMjtfRTDxtGohwX6o5EB_ZhNL1L5FEkVOkLcHs0gbT550B1OYWnIdL0bexPZ11tHvusfwmm649jtrG02PDcOyjHgUWbnFRSDxPFtT8fUxKJYkCkOJSJaFvNFGGNAfexsvlYQpEJvlIl3SajrKbzY4jwNBuHbCKgH2jiP0_LtfucsO4gbYdZkGbpHZkQjhQycn2DhJkG_KJ3D9-k59aR7hmXpGWKVsiJZ0DdRIbZABNqipwB4AJKoxsX9_PamLrwWQy-AxsutHmpYwRL2w6Bq05dcZz_ezGs9KItDtVy7i6cljrzb1z5c0Tz3T1oAENg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔵
دی‌مارتزیو:
اولین انتخاب مارسکا برای پر کردن جای رودری، انزو فرناندزه. سرمربی سیتی میخواد دوباره با هافبک آرژانتینی چلسی کار کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102971" target="_blank">📅 13:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102970">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rn-6_9XSMffXBG81GSo2lKISFOep6HuomUVF1Rc_MqE48883xYKcGe-UiNXoevHlK0PRkDIbySN3eY_SMFUF2E9JT8Vdnr8OZVGZN0Mzm2560fZkkq-2Hj0SM7IouijMHphAZM30GXJdvHU6S9cRgdlj-tjrhx0SIzZg-xnlGfSQ8hRkWJvAmoK1Lk5_E-PUpHebkSnZlyPc8-3Epuc1ZKItSZYCyJcDEcOiGHlHhTj0PRFy3WV8XOHDLCKLZ5VB5bEFMd69hfjWjE-_PmoDI6baYVaphOKXqpdsAk7bOlFMI2tp7eRz20WhvE8zPYuhac5Kn25oHFYVjNJNLfQRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
بایندر سنگربان منچستریونایتد با عقد قراردادی قرضی راهی سلتاویگو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102970" target="_blank">📅 13:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102969">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4e-6xOWiWVE02ZmsCZTQKwlYpactRLSrUWMEwcA-aIA12ck5FBTrq4pmO5R1XcN-KbZM3xfC8L4uJoSzfltHd413Z-Lu8y6634eZO3BiiSIiDcNzoO4cyhPAw8SLZxkeGVQszcg6JTaxitxN7XXVJMnPpf9TaYlD2JJMK4Y8I14jFd017pTwSoDxS4WySnjod2BzKSn_MOQESk1xWhnNB4NFRyOSURW7JKEnEpRJEVLcHmCGK8UUDz8A4OCo4lTNo6MU6SN-jEKpfPEA87MRaUg13JXD5YL4-Na669nmhwg2V78k_kNjx8hRuABs2qjXZzVKtPKRdRzQM-wWSxbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇹🇷
🇪🇸
#فوووووری
از آلفردو مارتینز: مسابقات سوپرکاپ اسپانیا در هفته اول فوریه ۲۰۲۷ به میزبانی استانبول برگزار میشه و برخلاف دوره‌های قبل، این‌بار خبری از برگزاری مسابقات در عربستان نخواهد بود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102969" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102968">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/102968" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102967">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXCABVl7AevEw_kZZMQyDFGWM-zF9Ka8pPn7W6L7v4-J_jbmCuJFkcODLaocUGNaRnVcPc_iNHDiTwH1vPntUhd6bLsv3b6lZLrEH-613jiHJM-TElWY5zMOuARBRS1XchGLAWTeeD-QCD1RvyUHcB691xicFDD84WrLYAXgzoT9Y01jDhk7VGo9Uun9oeIhAdBW2_grK-0LueD55NBSYliWfFoMEy0uiru5jCC2X46epr8ak3qwdJuWVTdfO2HzBSMnyqOxlevzGmso1W9apWeLWT6uOg6_zjgye5DJPEVU9kxPIthCdOqEbVokPn3SCWilG1kg82uPPg397TkwfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102967" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
