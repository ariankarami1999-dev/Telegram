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
<img src="https://cdn4.telesco.pe/file/jlemP-NkJMeld-NrjcZ2hpCIXiVA0hYpupmLE_Ekvk2_dDYlNKEQ4hfwXNm4p6PGp45AG6stlAOY6Efg3HXkMLXdmbrJPsK5DoQjYwpDpkisPttTCCeBq8PxVxhhUqCXUUKc9zkglhruVM3N9gq8UZPHaeuNFs8VjPAJOeR-NDU0GYt4x_qX_GixzgbEOq2bTMjDaGnzL9TAfQAuZ-xF5QtLHiaLRYkaccLJcSDIOokOBlDDkUvL2vQPMzaVaxFmeBk8WEmimr3o2IlXc9pPPGu1XEX6kKiPbdJwpowFy3kUOWVJfobTFW0hA0Wx2oWeMRYo02kLJo5M0wlEiUN83w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 197K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 23:52:11</div>
<hr>

<div class="tg-post" id="msg-79650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">زیر این پست آهنگای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/funhiphop/79650" target="_blank">📅 23:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79649">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز سپاه 4 تا کشتی رو زد امریکا هم معافیت تحریم نفتیو لغو کرد و یکی از مقاماش گفت که بزودی چند تا سایت نظامیشونو مورد حمله قرار میدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/79649" target="_blank">📅 22:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeI4Zes6zDcRPP5k3wM6XzKrY7Qt3tZb8Gpwuw1Isr19Mf-P7aE0neeXj9uaP9s6wPTpNg1Jf0a_FteA6yMnu42WP3_noWDHe7GQ2Y_t2VTYfVHjxA1EiLd6ACfKsG3HVJV85LZWUjeKZQebVLo_5_iZlPf3CWwkw_sftUqH40EkMPsSvu7sppDs9XOjSKhFQDTUnwB0gfq0nHL4CIUls5ioz-lUx5EQKq1A7k2Edvm383-fO6kF4obYuAPvmr3_UFfrMIO_kU-SytjAx3_eH3DiPSLou7l9aD3n3iQ51TAeyDqDkOsNCRDI-JXvN2ht9la7YBCLyhLYPiwZvBOYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFge03K_SjoIN03O_JiVIBbWuOSZabQrEcsU2oLy0vJkCae01rEgCFkRZa1E6vwP7y1y0lpf6UDrl-ADibQHHobk1lta6zpQUZJPX1RyD3GX5kospD4ITH1vbS6o8DAroonWiwM9ZjDaIpcDp9KRwXJ8s6vAz8GCZxB2xejchF_5TuUzdwsYLHjUpH7nrNNe_jJWt9lxH2kQWQVUzt8ZH2lT0Qcy3Qeu5y1Kusn8Nkng44YJ-L3vFE1att6p6GjM-h-lVp9lJhDHW31wMiFtoshH6Ti6axKKb3L_vVqn58kMfEc1X-iFImZVFQjqTUXpAi5t6hJZbYmsNzIhvl4dVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این صحنه چندتا فحش به برونو و نوس تو ذهنتون پلی میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/79647" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حالا به رونالدو فنا ربطی نداره ولی بنظرم آرژانتین یا یک چهارم یا نیمه نهایی حذف میشه، خیلی کیرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/funhiphop/79646" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79645">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس رفع محدودیت و کاهش پینگ</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8STiHdsdaAjU_K2uPGSghg_dKczX7LE-umyAJzQ1BKrJghs1SVDmKqJFjS9w859nBaUpH_au4hP8fY1ciz2x1PoTZTlFbuWSCLzbsTovGkusCpTbZsV61KWkWzDV91qW-2fcH3fVDQw2EUCXNh0TEtCHyhjhsf00wZDV8YYfEyGUAUsK860JBivhVXo4gpfIejGAl9O-6h6Izh_SzF9FM5bMKPTljVLp8eDlKbCwbIG5uQEBSu0tOh3nY-tEc8OzYENEu1cvErKuk9rVOrgWZ5OmVcz4ZmCipQIXCfZF6xz9kRj7yADLziYOyOn10sjcVfEwIRiX9Yt0N2EdkCZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
یه اینترنت پایدار، تفاوتش رو از همون دقیقه اول حس می‌کنی
😎
✅
سرعت بالا
🌎
سرورهای متنوع
🎮
سرورهای Gaming
🛡
اتصال پایدار و امن
🚀
اگر هنوز از هاب شل اشتراک تهیه نکردی، وقتشه تفاوتش رو تجربه کنی.
🤖
خرید آنی از طریق
ربات
🧑‍💻
پشتیبانی تلگرام
@HUBSHELL</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/79645" target="_blank">📅 22:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79644">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اسنپ چت هالند و چک کنید ببینید خایمالی مسیو نکرده</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/funhiphop/79644" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79643">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝒉𝒔𝒂𝒏</strong></div>
<div class="tg-text">ایران چی میگه؟
😂
سوئیس</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/79643" target="_blank">📅 22:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79642">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حریف ارژانتین امشب تو بازی کلمبیا ایران مشخص میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/79642" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79641">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQliqBlyqFuXBrGu1aI1bVGDmo2WpkezRotfWEKKUtHQhIaanOKdJrNg-W9MhfJwHSFXvDAldaqNFE1LcqlfJP7r66dFNA2n-Vxdl8szWTK-6QdGRiSzQGDOSnB3HUHmgKJixuqq89S_dd9IiSKE1BVPXKsHugtoet6KCmY2u1JSoEe4yRlvp1PtZ-NYqeNXPh6n3_zFosotGuVUS5YTbdR0mj6Ocv0VwyBGCkJzzaqyB2C3X8r8kKJvNUwVBUgSDcl8wusiNswlDCxCUh56FZLvaSokczZBj7vd8P82F_9WE-1V6KhBpTvgNMcjA7C6MMQ5x7fxMvn9KFW-Wh99_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی روزگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79641" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ولی دیگه مثل قدیما استرس بازیا مسی رو ندارم، فینال ۲۰۲۲ تا نزدیک سکته رفتم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/79640" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79639">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آره دوستان، مسی منتظر نمیمونه پاس بدن، خودش پاس میده گل بزنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79639" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79638">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfea1eTiYDReNf6uRwuvpPG6G9bJsTniDRGGyyrGwKcSZ-TquNrVAaaBt5UNm9a14Fv4ZFsawEw4C1TXJFBxpJ8OIt2rJXbLO9_dZ5GrydWN_6yLk0Kzaowc_DgZcTjaKvqQ6vGXlwuC9cprnMJF6hwM-v7cs_ZXDVlwyCpg3yuW20PzVmEc0NW9TjLLYnySDU6pQ7Gk40JVe2T1296UjyL--j9_BJjBjcK0LDQd0n0bqVS7XwSXXRj1j44WiieVuYgXvI2b-BjyP-j2kguE7jXfUU8AwP9tc5MkrJEDdYRUxYW18HzT6uBupKbkhi92ivnVhuBBoHAQcQ6t2x7eSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79638" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79637">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پروردگارم
💙
🤍
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/79637" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79636">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTHNNdL4sfk7bs8fvfGrFvleilIPk1eL73LurS4WI_DRdkB3bete4uQWKHVu9g_lbEZIfA_CK6EUjDZjX28-vrOIuDOL_tvIRZ-uy4eAkv44rv3qI2Y2nDIJ0n_hOQZeOXh9Gi2jqNa_qEojoqvAFNVK5ecFwAN1j8rfbydL4BZtCPur7OSwICs5IIOF-QPyA2eNDsHpIH5ySOxEBhMGxgbS-rJYkkco2-9uEfiEc0ihWP7oSQ7WBssh-5YW3mPFgqRj3TzLCu9mJDNTpQaf69JMiUV-S8DvouCoVadGaIdsD4syIJuIuXfNLnZgj1fidClOLmyompYQTNn0Y5CJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی فنای رونالدو رو نا امید نکرد، داره گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79636" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-ws33urv4E3PBPZMo1aFaYPKNo2JziJCnUF0cU7sd3E3X9baOFlTU2wLoCgf_F57bDoVQ-qU7q-xEgmvHx10V9LrDQPBQWzBq7shEKLDkBPrFcd1DnOOT7tW7ScxzD9rNO1nYeDqsbpjfWWzVklEgPqg7SVuJNVWy9rOrN3J_nOjdeDa4HGOQ4z9ZH-9aqjAlEMTwM0f4DKTClyT46E2RpGSogLYdoGWkiyy8Lwa0KzUM_jvz1mB16YWGKsvpKgKeQON6mdIPplPb4RQbTnXA-oZlj8jVu6e3aJ4FthBkb0YPU0qec-ZoE9JBUII5joM8ZlTStUhRLrbaRDeUVeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79625" target="_blank">📅 21:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79622">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عجب کیری خوردی
😂
😂</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79622" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79621">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=GRaF56ifvE2HqNX14qIzokmivepJpGwIGqGjqJWC29cog603b3-ETn-FWnT1MBZmKDX55VRYZa2cjr86BdIpEGXXEA4M7OTyccbWRLWDBTiboQ2WrKkV3vHPfh7qmi9AY0z1u7kE6AnvM32jHzO5PAzNphycimOXcO4foqPcCbkmfUF0lHegVATae_IsAag-F6msUKGyJZegZ3qgHbyBAZ47_8WIY-R2Hw2MpxnUIRm4T0vddlTkaUPaQvbuHEpZfaF52IN0gbfeUiAo97KnanzTuPL_01TNdesSnhBxN1WcgRQEm0p5eyXMxXeOoNSp98nbfg9-NMd31XgtfE5aLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9531c4e029.mp4?token=GRaF56ifvE2HqNX14qIzokmivepJpGwIGqGjqJWC29cog603b3-ETn-FWnT1MBZmKDX55VRYZa2cjr86BdIpEGXXEA4M7OTyccbWRLWDBTiboQ2WrKkV3vHPfh7qmi9AY0z1u7kE6AnvM32jHzO5PAzNphycimOXcO4foqPcCbkmfUF0lHegVATae_IsAag-F6msUKGyJZegZ3qgHbyBAZ47_8WIY-R2Hw2MpxnUIRm4T0vddlTkaUPaQvbuHEpZfaF52IN0gbfeUiAo97KnanzTuPL_01TNdesSnhBxN1WcgRQEm0p5eyXMxXeOoNSp98nbfg9-NMd31XgtfE5aLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79621" target="_blank">📅 21:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79618">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79618" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79617">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه گل یه پاس گل</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79617" target="_blank">📅 21:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مسیییی</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79611" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79610" target="_blank">📅 21:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لاشی
امام
حافظ
زیکو
چیزی نیس اسم بازیکنای مصره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79607" target="_blank">📅 21:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مصر آورده میگه ببر، صد بار گفتم فقط کیپ ورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79606" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آرژانتین بخواد اینطوری بازی کنه قطعا حذف میشه</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79602" target="_blank">📅 21:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOqaGHM1jFe7eE-PcaDSL9SKZBQ3PpNrX2q8c9z6ncnYdP3RJ9fNW3WBHqkFepyQ-RPIbkf7DegdfA2zRtQmWXsvxHShRUKhGOHBqLgzeUlEBbG2vbHV7vSt9PKFtb7IYLYRq6emO5X3JeQhblQJPkXEb0cLxKVLamdgBBeSGr-WYqUpzkodL0eLSX5D58Va1r1hhVrc611Mhi60p5I5KNFCiHmYNQxT0ndW5w4I4u4BpmSIuN2pqQE8mPrr6-o9DIxRTn3uj75OFlaWdZ7FJR_bicrT2O2EOW8QpG2NpS6HDerHKG7Jyr4k1uvUOrFQR_1OtrHLUecBlrQQFnS5vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی تو ادوار جام جهانی 8 تا پنالتی زده که 4 تا رو گل کرده و 4 تا رو خراب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79598" target="_blank">📅 20:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd042</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79597" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شما چرا از حذف رونالدو خوشحال بودید؟
😔</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79596" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یجوری خوشحالید انگار مسی حذف شه جام جهانی قبلی رو هم پس میگیرن</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79595" target="_blank">📅 20:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COI6lSAFM73lyjcUB_b0lgOh4n7oZC-ovU67BKQyd3UsyXxggYb4GzBic0XPlvtK4rd2PaAM6kMatoimpWWARqXvd2nduqAXFF-pnrL-EaiTBpRmn3_u_c32g412_bmJ3VAM0CvqoFNgEWh7eNrH2PoNQMFG46KtnhHWGyuy7fUCjHMUm7_nen8BZdTgplvauubCAdbuIMbBI6qogp1tOP0SkP5YutP9S7BDeD3ERB1pStaVlgplxiH77KG22OprxBWshg3V3bh1c8myTiPoMyYM22_RZ9jj0x7ihwVa_Xy6BFw7dsWlckPRI1Mo_mwrSARNO6kflpqijaNBScGUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل عکس مسی بعد از بازی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79594" target="_blank">📅 20:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این دومین پنالتیه که دروازه بان مصر تو این جام جهانی گرفته</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79593" target="_blank">📅 19:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79592">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">این دومین پنالتیه که دروازه بان مصر تو این جام جهانی گرفته</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79592" target="_blank">📅 19:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79587">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به گزارش بابک تقوایی نویسنده و خبرنگار حوزه نظامی: متاسفانه چند کماندوی تیپ 65 هوابرد نوهد ارتش که از اعتراضات حمایت کرده بودند بازداشت و در خطر اعدام به جرم قیام مسلحانه و کودتا هستند. نام دو شخص از این کماندوها: سرهنگ حمیدرضا خلیلی و سرگرد حسین مجیدی است. این عزیزان از حق تماس با خانواده های خود نیز محروم شده اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79587" target="_blank">📅 19:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79586">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTaumfgjFAHwpc7KHhURTkLopAr9JhhiDkkiq3RFOathWUiUD6L85qYC-k0Wi9MRY2e7vxPsOYB2a6aSTzSoceBqZYaFqeFJOdGH1lBIYF1n-R3SVDiMQG18otGkIDmrwMF4WQKHGTcRnRx80KwRzMSrpwyCrXuEAeVx0MAV2azyioR-4BRFyIGBDjrH_6H5PvYfEtGfRWGilU7V6g1qBRSOUjKwvucPZ6CrxJCYWdF88D_nPMrmwxF_74vJ4GlqvRO3yDjF3GY5QkHKUHdaduvX1kwLjePw_YIJI9RQ6bkVbyxCsyGn2WN1NonZh2epqoJ3uc5sZgzoUgKlXuyNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط مخصوص نابینایان پیاده روی شهرداری که مستقیم میره تو تیربرق.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79586" target="_blank">📅 19:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79585">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw5Ne6GvVrjDz35aWYqOEnNx6Prz6a5NfXuxmdULD4hQz1wRwezjxQ-6CahXO3CLWW_R3vGC9morq0j9NFjxp5ZVna4jd86rOkGXHDmdXfY6MknzxjywNPCJKFAf9kWyis9_HYigTPmEod2jH9zAOkBnAUIqGBtDwaC0QvruMKcr9mNOmdw668A9Nz31yroivHnPcIrcoiVFeEZNAhQGDlz8_G2qOfvlKzclGqPt5Wgssa6vfPmfm2ItqTKRykyedanLILgRFUuKj0EVkN90M5HYrkhn60PXGWUB2-j06aolWEBS7gFOJDPrJj7ABy37Z3n7QwcO26JRtxTBTaoziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پیدار به نام “بریدم” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79585" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79584">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgH1OGSZZEub8WcoHQ-mgGUtA6ABaDh_wfmHdkmrG5VLDzUZ4zCJfjSvM7m6RqmKyGxgIE8wTd765-DKS-CvKYC0PzcHZDphdcWQar54CQIx0dLl_GSBKVZdeiGiW5xoylFTPHkxIMj7D5jYGedGw1qwgWXat-9sdk6Q7IOU1jZMZAtOhTECtEI9JtBXNzYq9LWFs2YLcrZh8dwKMZxI-EKvqKu5gNI2cmYovXB_-dIkYzdyzgTWZMA_fnFA3EaCD3rLpSXiBGlKYgbiICSNKCFCgiPEmJvU5tny6kvwysWMcRKcDZfDYfuuYIKds97elD3CH1WaVkOFZa-nPjy4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار: بغل لامین یامال؟
کریستیانو رونالدو: چیز خاصی نبود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79584" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-m_pA8_D1UndlRvKk5L-gevBslHM-MS-wUqT7gsBgmF0TlhlotoAFwQJ16ApGaAzAbylj8ZHAnIM_lZOCAt7FiwGzYcRfVfTpAslaEEcIBTiculkpQ8bU_FOdibkXLVY4GJC5k6SorO2R9n2lM8De5WKXNJvt-PSuM_rwrNZ4S02MOH92clfuNCzvoa5T9kxVpt9isscugw88Y0mJt67Ar5oe5GPBM8eUFPK8QmQlXJle3Wl6Y5oOec3dZyWyZFEH5sE3v_b1ipuKnOkLzl-JOS4dg4LYJfz1FbO_8Me9uSWB-4eprIvQKlbQG0p0mabajKAMTVyslO4EL64yHMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا رونالدو کاپیتان تیمه موقع باختا اول خودش گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79583" target="_blank">📅 18:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79582" target="_blank">📅 18:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=vaNqDLwS3JXa1hFp2xPQgDoDXTn4b57lPZNegQfSXBKYIi-UMEz8_B2n0b-mp_dfM72xwibUBy7FmnZkIteCNN1G-noOr-j4XpFrWk-v-1oEloBFFFLlLtLdgeRHTDWhD7xFRFFqgPGquB8QGY4-EZCN1dFJss7HpWRkuiMBrJvdHbTO7yq0z59uNanFnz0MfDDPe18rzSymqVbhAvxdop7nc8YIEmA9POLsSvb1BTnBoQTRdDKE2F1ss0dlXPgpyQ8RknD4AVJmfEq8vg_XiFAwc5FO2IKFznouAYpnUjJqlLAuZfMHdCjiWhw_nVqs-CoGrAXQS8bLKgDnmer_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0addb56dc0.mp4?token=vaNqDLwS3JXa1hFp2xPQgDoDXTn4b57lPZNegQfSXBKYIi-UMEz8_B2n0b-mp_dfM72xwibUBy7FmnZkIteCNN1G-noOr-j4XpFrWk-v-1oEloBFFFLlLtLdgeRHTDWhD7xFRFFqgPGquB8QGY4-EZCN1dFJss7HpWRkuiMBrJvdHbTO7yq0z59uNanFnz0MfDDPe18rzSymqVbhAvxdop7nc8YIEmA9POLsSvb1BTnBoQTRdDKE2F1ss0dlXPgpyQ8RknD4AVJmfEq8vg_XiFAwc5FO2IKFznouAYpnUjJqlLAuZfMHdCjiWhw_nVqs-CoGrAXQS8bLKgDnmer_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌ی عده‌ای اغتشاشگر و آشوبگر با سنگ و کلمات زشت به دکتر سید عباس عراقچی.
تقاضای برخورد با این اعمال زشت و تخریبگران اموال عمومی را داریم.
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_الان_بحث_بحث_سویا_و_ذرته
#منم_به_این_مذاکرات_اعتراض_دارم_ولی_به_این_مدل_اغتشاش_هم_انتقاد_دارم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79581" target="_blank">📅 16:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8hgdi215uTnrAjOBS5uO726TE_XMII0h6qV30MAuarlxlOJgb5aPXPRNzVH-UhQR8fMzjEzbfdl0f3QILv75DC3Y0PK_gQBx3f_ERnA7feNkiOUFHVMjuSYSckkZuFXKw_huG3nWxN0h_5DFo-Y3ViQ49nHL8ggbfPWgXpHOXoFRST9FfOWtRTtqBWlwu8LXO7tnf1T411D9Mf2chOp09nvJjGAfRpaDYapR2m7rV-hdZLF0DLOFuSGgo9nkK9R2GTZaogSU4F466x2OIF7IF2rEtEGUXbz9kZtPRw1lcM2NaG8t5at_Qw7ImBR6b3NpORa64Cvuum87WgKUjOkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79580" target="_blank">📅 16:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeK4Ytxp9A8e0e4y754jo4CZJWdJ3wAx4hjVHC0owSr-xKbvibJla_R-LXZLsVrmvMPprWAeIdN1eE8_yuWOQS72WV1KvyMq3J7jGzpOS57stKvmHOqQOuOemLl4psmFYwu0lHoJvza-BavyH1_eu45mhwvlhFoAS0C97D_TjiVNTjZtraEG5HKum_PmlJSuOgz9ebhMDS80STZtnBTwqSNg-zyo4JFVpH1hr1DsxyJ0xXab0hwOSCthjOnPp_6ifiSjg33eGLyDhrM02RU7q5abQTPx8EuQecqieEtyR9YdhZqMCF7ZMv3to5wCijE01m4KdrmW1TstrxDRpmscmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ازدحام پشممم ریزون جمعیت در تشییع جنازه خامنه ای
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79579" target="_blank">📅 16:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یادش بخیر ی زمان هر چی میخواستیم هلدینگ میخریدش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79578" target="_blank">📅 14:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79576">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOHdwQZqJWeoZtzmuXkgpC3B65c1rzwMQzvXeRaQgsGfIoRWw-XvwLwICc49xfq2g44xAaVtuxr41DyF81VX3Q3IfkVAqPl0H2frvDjJAOpclb9VA8bc2Y6w2lsHqBqKf-mXahtMS85jXhtr6rGEq5h-QVEJpW2U2Fsl6gyWHa1M3HqHqm7SyLdgGx56RoyA3SS5JbyEJvy_RSiaAXT2Xs0mK3pyngO16rTb7XFU2VKbPP3bjTx_qNNGO0-diO7Ov-2rqEq7eCNuj60iGOfZZc2fD5bXhkRRnmmS911Ur0eEwaLxVeFbhWjH-ppUy9MUOtLaf7X8_dE6CqJqFK9wIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BblbHHBK9K-5du3sk3x1K6SJiLv4viId_in8fpobuJIO-0aPsX9XPPOsPxBRyU6wyOdqPrt5PmsMSbSaQHRpi-TSH4pPI_zCIWbSrK5nTCNLYqTEsnbbgHrSwN3UTj9twHNDdnafSgPe69xxDPweWR1JmSUZPdQV7fb7cOsRWMWgVKUnyrIlIPd9mfmfdAADcqVOPNtBTEGeY6pMKmRBVrjPtySkuO9UnTUmssjxn0dax8yEWyTlPfsa5-SG2oubnC5ahNsNGLryc1Twa46din_hyujxhgBPpaNHrtKHvlYVNsIssHJohoMWzZGvEmpC-O2s06myA957Ves06gnLtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیوید کیس مشاور نخست وزیر پیشین اسراییل و از افراد نزدیک به موساد:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79576" target="_blank">📅 14:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79575" target="_blank">📅 14:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O87moylNzYldv4tEhn4cxtmlxlB6R0YOAGpwwAWOtxzJT0Z8MGe7QJzwDzasMbLTk_GnWa9eFAIIMjDUzPjWQAWvbGTM-txUHEY6aUeGNitU-QAJYwI8dOybpdyA-zHDA_lrrYka1ICvZK0IgxOXAnP4ceQScXWRe2ixEA2fSwVY_MLTnNeIvwC8eRWC2s_KYzKAYuIB-g5zGPNCsMhjxtl_OOYVG8Iv1Ar3NZwJmRzF1xC3l_myzIFvcsm9rP2wcEs-BEQYD8N01gJpmj1GHynGvX4tPC91sbgRTzEwbSBMQ5ErGxacTqbmxxdgYXjmjOvF4gyW_pnf1yUTN4KD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی میتونی با کلاهبرداری از ۱۰۰ هزار نفر که ۲۰ دلار دارن ۲ میلیون دلار در بیاری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79574" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هیپهاپولوژیست ی فوت فتیش دزده که بعضی وقتام آهنگ میخونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79573" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه دکی لباسا و کارت صدا عمرانم برداشته نمیده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79572" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBhyhuP9O1-xAZD5UuVuMGcy3ffuEE4D4peReudOS9y0MGu6EvGWN4RBCcyevaHzzQC8cEtC-6J_HvCsg4OQdGmnZWq3AgZn8FA_JcdZGocSISqJh-6tmNXPvvPRMh_Y1wtoZ7cALskxsFsi5y0hZ5k3bw8piCKLNBHXVMn4PMDHGmovJHXbJjbLuvi3F4fOORMANV5DQPAXrMz4swn4BnSasmID8tfpeuZFPYIwf5JAtuE4yvlwsDDhdgF2GNewW-LIOATY3N589TTeHDrQuc5s_aWltoy7qhP5O74yaMlQ7G_rHSdxtjAhTfg5PUqI4Z9wW4hza_LwDoaaA8EIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه
دکی لباسا و کارت صدا عمرانم برداشته نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79571" target="_blank">📅 13:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQUW1HPWtcxHwuFhIOH3Ry_hvZ7DmVqoev1jLN6QNSlcSkgGL8Sv8uqqSS_lztH-AkpwyBB__fWHMfsBiTd26J77uQRAW1QKgbuVPMFRyvte1V8SEZWR-8pyC4gRTXsE7rYgHK9aVPFltlcDovaotAkjLOB9T18ELB0SafdmdpG71deRb8ZzhD9jMmiGkCaeCz_MFOYiPxYFcjrC7JEh0-cxv24_L4qnKH0Xd2UOv9C-6LsLcGmO2sz0WsP-U_nXtust2aMGL0hy9hPaB2lyUZ-3oOSOLexwdXVIegn7SBIjirYzI6S4p3gMJzaumJgzwi05NtwR1KgrIlb4g81Ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق این نقشه باز هم میشه نتیجه گرفت که سمنان چیزی جز یک تئوری توطئه که ساخته دست دولت ها برای کنترل انسان هاست، نیست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79569" target="_blank">📅 13:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">امشب سیریکو میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79568" target="_blank">📅 13:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv_yaMIG3nHJpVorqMEuXH1JRqPM-7KlUO5r4k-a8CdeqLdDF5OyHk28nQseAtNQR801ToNSaQW0x0168-BUoGd5YU0CK8GZyw-rhlhBA49Qv-aGToqb2az8EvEjOUeWoEfRD5Yfbq8XPn-VRR9s3ow7Y0ui-c328VoFjOoPp7oP8qsRsWiGuzIUZHgYk582x2i2jJv6ee5gvQbLLGgebQ0e7lUpO9_00Xo3pKy_aHoM3wOKslyXU9LtY1OGmbPaHxsX-DQXQZRAz5jSqRDZRMH7t_pXP2xrR4Q-mKabmTjq1ZsNDZhNqjn-BkTQRiez3JDvrSXFyl9AAdsbFPMxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که میدونم مارتینز مادرجنده از قصد باخت ولی نمیتونم ثابت کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79567" target="_blank">📅 12:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">امروز تا اینجا اتفاقات زیاد هیجان‌انگیزی تو خاورمیانه نیفتاده متاسفانه.
فقط یه سری آدم ناشناس سعی کردن با ترکوندن چند تا ماشین روبه‌روی هتل محل اقامت مکرون تو سوریه، مکرون رو ترور کنن و سوریه رو به دوران اوجش برگردونن ولی ضریب هوشی‌شون اونقدرا زیاد نبوده که بفهمن برا ترور رئیس جمهور یه کشور دیگه، علاوه بر تروریست بازی به نقشه و برنامه‌ریزی و اینجور چیزا هم نیازه و متاسفانه موقع انفجار، مکرون اصلا تو هتل نبوده که بخواد آسیب ببینه.
فرمانده‌های سپاه هم دیدن حواس باقرشاه به مراسم تشییع پرته برا همین دستشون خورده دوتا کشتی رو تو تنگه‌ی هرمز فرستادن هوا که ضمن تبریک این پیروزی بزرگ، متاسفانه باید بگم که اونقدرا هیجان‌انگیز و خاص نیست.
به امید اتفاقات هیجان‌انگیزتر در ادامه‌ی روز.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79566" target="_blank">📅 12:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULQmKuKiO_bLeCJBNlWd7jCquUF1tetCC4dLmeoVdDUq8HE71UAWXuejJz_khg6OiGfYRwND2gjhaPoSmhfAPUd0biZTLDK9ld4Pv-LznsGYllWXz2RLWQ2mQaAdWPk2qivLHSXbOLqJo_aUjAnd1FzFluUrNwfvJM8wVBuxmHB_PVCEJGQFu1FMpNKoxgLHl8e6vlLKOaCJYiHyVQUC_jvsLuli2gp062Ild8x3iSFB5bY4z0za6iB3TnAs77MQ-I-1fdxkoNFgeZspyHuYg1tTPLaUvfJPf1Z3RiHYoJ4tPYEvUnyg30u-qy6eznoDFUKJRRu8agfnoK08lAFdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79565" target="_blank">📅 12:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اینهمه به یامال فحش دادید گفتید بزرگتر کوچیکتر سرش نمیشه، تهشم همین یامال بیشتر از هم تیمیای رونالدو به فکرش بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79564" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ببین تلخون چه موجودیه که برا اولین بار حس کردم ادرویت کارش خوبه و بهتر از کسی بود که باهاش فیت داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79563" target="_blank">📅 10:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6fyzChlfYJW3_lk8vJlYR9R5uDQaMlHXIHlraCBZzVBNIVTZXbmzShqLUqj4BQbqzgj30ILQ2vEwOOBmvDYNWXsZt482VjqsS95g_iwkxsYszxd_l1uczAzRsfs9iJpztNl9sI165yB4d3WIKV1GEyd1CClLGcK_wbKsliR-Do4uD0yzaUc13RvLFvXRrzmWPLv4Bb0bnMYFvl6PNok3AD7vypCScg1aUO3qWfzyWjrhcXy43tni86Wh2OKqT9vSr8f5UId35bIODT1HiWc5gASAvv8h4XfSJ3natKaN1xLjju2GXDcnIvTTzZB1V7HsOJo9BDFDGMvBa5u2mNp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این رفتار لیدر طلبی برونو فرناندز که حتما باید خودش همکاره تیم باشه بعید میدونم منچستر هم گوهی بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79562" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79561" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عجب یک چهارم جذابی شد ولی</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79560" target="_blank">📅 09:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بلژیک ورژن فوق تخمیشو برا قلعه نویی گذاشته بود
از بعد اون بازی همه رو درو کردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79559" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سلام دوستان صبحتون بخیر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79558" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPVfgr3eHFlrprZL3iebyBOBA8nfdqFeuUK-N_OXavfA-7l7LM0VnEDxpksR05fKeiP-AG1qWDq1vxwyp5gy2UjZFrfa6F20ofHFpwnTJ46qPCbO98OTTqGDx6vtyXCDSZpd5BL8Bm-vAAH9Ej4I8ASVuINLEP8VEhbgagezg__rf-Upt6XONel8PO9lMCWN0UsxUNuwKE1jYqn5vJlAn7oqkb-uzibEYQrs0l69x9A6HxvEUHZnx3C_KRPkJZlY6T3yiUTEodsysRwR6I3UupmVGxcIVOcnHK3fGTF67DMxT4rKrLy3cePjB7Ym6NDSom0BX4qyt7N6ig-b8h38YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ذره حرفات به قدت میومد هم باحال بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/79557" target="_blank">📅 02:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EnK2ww8W4TmfNb7Owek985TdGcMNswjLAAmuTV0WXv2ZEWRkyQARMlC3FO_1mioA2OJMv3Kfx6FEiXugPVh-QqunP2NbaMClQHxR6bP8QHFEAuQ_YjrjXzQRi83M5nferI4YeK3Q6X668BBz4zwty7Tby_hFiQXUD927Qu3BEredRJIJcjBc6mfM1ewck1Are7Q38fEC97umXjEb5L2Oc8MkYkP0SQOMjXxgeO085x4JI4jgjP11DUyVHRq_Cw5773njrI24lJwDVfv4qmHFxsZBMz0VsJPCqoTAYO4wSg28iHwP31jAUxb5vYR22i1UJdBi4FJ87PRzXEe54MbBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfiv8rhi8IuAplyxVgIWZtxTKSTklIcg6ZuWWtlhWXEfLmHNDNhtI_fHMgwau-zpOmTM04POuCiWw--10wiRJj3Bi7QkFFY-Glj-I4-tdsV_UiP8wE94wl-pt_bWsPNtXHa7qylEEJG_wIRWPESjJ5DsEqMlFN51q7GTBovHnbMEIYCf7UX5JPVa8w_wEZ1KPOoNatrO-vbZXk-FqDaalSYZhMr15Pcn5u-mmVEhQz5lXOSBVvrV2gr29qwJAH3dteU49jyZiC4xg5qFdfOufR7WfN72QNMI5-JyVHG9n5i5icdBcFCTqduQWuT7w6uP8ZZzaN2qoD15Kd5V3rn7Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فک کنم دعای خیر زید یامال بود که بردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79555" target="_blank">📅 02:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن  https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79553" target="_blank">📅 02:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79552" target="_blank">📅 02:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79550">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=S_XdX944yH4Li-m2-sdEwJbdUgDIi-Tq7okMqLjbtO2-fiX6FKjGQcrCKcY2kXf9mECA2g-5DXMfPyav-_YTQHU8kQT8CWXC8Uk3ktMmff4S9HADIOZxAEzGB43KlqPCExzF36yjOmbb3eZnM270QZjBO4aMx16xlChRnsuSoQcKcipH97ZqcrdMucps9f6CriMPPAdKCPveAxdRTvmAKLVfFSbj5xoLUSAzvjkVW2Dre-fQRTrdo3Atw4t-xqr8qY_5SENrWRYlEHNfAR6D_r5wQo5u1-WdYLZ0MHZJ-uwWehhBca5o2CfW3wjK5LGiVTiF5d1sZEeZV_rwUXqQ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=S_XdX944yH4Li-m2-sdEwJbdUgDIi-Tq7okMqLjbtO2-fiX6FKjGQcrCKcY2kXf9mECA2g-5DXMfPyav-_YTQHU8kQT8CWXC8Uk3ktMmff4S9HADIOZxAEzGB43KlqPCExzF36yjOmbb3eZnM270QZjBO4aMx16xlChRnsuSoQcKcipH97ZqcrdMucps9f6CriMPPAdKCPveAxdRTvmAKLVfFSbj5xoLUSAzvjkVW2Dre-fQRTrdo3Atw4t-xqr8qY_5SENrWRYlEHNfAR6D_r5wQo5u1-WdYLZ0MHZJ-uwWehhBca5o2CfW3wjK5LGiVTiF5d1sZEeZV_rwUXqQ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب بخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/79550" target="_blank">📅 02:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79549">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEliAS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o74dLXtbOGFlprqMMOg-xldK8Hnb567TLAqezt_Bys0R1-CCxVWilUvMLJR9kwaHpUrvrwpBsismkVwqyLbLW60m7bTEAK_gnB9Bq55NfWELu60dJDPqsd75qnv_PiixrhoMatRoz3I4omFXTCvxtPLl-Xw8XNQ7CvKNz9Q6PvwAKIo5aTvdAv_e3hPRB9Xio29Fuzg-Qp-mR3fN7WmyksAmSQP-H6yLoz6jyAlmRNN48fY_A-3h2NTPSvNYKv035yB1I3cHr1mXf-4SbrhCnfHcykpjUBMPada8EgQpxsIbFRXvFqRClfMdbTUOvpiXLeff4gz-a3hKZFlvLY9x1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعصابم از تیم تخمی پرتغال کیریه پاشم برم فیلم ببینم:</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79549" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79548">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوستان رونالدو فن نظرتون با خواب چیه؟</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79548" target="_blank">📅 02:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79547" target="_blank">📅 02:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHadi(idk version)</strong></div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/79545" target="_blank">📅 01:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79544">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlhwSZXK7VDGtZFOo5nLn-SfkVHGHVD0zbGQJtrcWgx_oeOLnNnTRcXc0Qm7_cUPVaboHTehq4sQkZERmDkuFKvowj1V37c6ab_dhF5q5F7V-adOJa0yKFOPYTehF59Cwtf57xmA9qpINGU0RUOPjfzXURGEaru_m8ZEYYE5dsVQNmqHY6yRvFWSxv27hGpKf2m61hxij_nMHjmuSER-W5TsipvnF5rB2GqrshxajgOGL7NMc7VlreEKhdYbZUGZs6hm5C34-MhEv2AmWB2n1LKb3iYxeTTMeUwzFt6Ii3Q5kD1Ad8sUx_-EQ4CAAySmd_8ynZtipNTsM9B7e83sDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79544" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79543">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79543" target="_blank">📅 01:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79541">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aylktyUTVtbRwmrugHu0sCZ4_SXeLG0YFRwfBSmU0Kvfefege5g76vMD_USrdtnOMjzRx0-1br3TTVqVVuDANeGj-DxIZyhDl0rexxgMw6DCnlibwBuPtupL8TtfbufQWWw-kBw0aq_zT_Kknmveb6kb4pucCYTlnH7YtgEhU03-W7bJWY-b9mLGge3alfwqwmFcE_SqqldnmGdPbcBzTWA8IAiS2LlDDGguZEJu5DLSivNHEFi_L57qps2vEIU1t46s2pEHy07ylD2K0lk5seFxUlLy1Noze5A8D-YXfV8hDXTOwAAdLuRRV2QO7RDSuTUisGDg_MmbqVqorqpY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیاد گرونم نیستا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/79541" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79539">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شما یادتون نیست(منم یادم نیست) ولی اسپانیا ۲۰۱۰ هم همینطوری بود، خوب دفاع می‌کرد تهش یه گل میزد صعود میکرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79539" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کاربر Mmd به ائتلاف تحریم پرتقال پیوست
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79537" target="_blank">📅 01:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaZRIzqSOquqNH7Pse4qDCI4s6_VnU1exScf4K-clZMRAF8taH3kpuGrDbP0Bm9LArNtjzeUJMJwg2NJ7koyqMdURiyemkFUTj5xX_kHukJcK4q2cDprScQIUwksrzd4t-RCBEk_IeYSaENKEE3GVo3gSQe4MUzxKxhM3qVCm5EnhQqKXr6hRyu67OIP8PnwKL7grKGgD09pjaJgLS15_pmqT_s6GLHMFYTMER42_88tvs6lGndUTrHXQzpftO_t053OfBc8SplFcLSOCmq85IXlvBUVQkpBVL9JWZvZNDtzl4BHCVtPF88R9DTcwxANdwZjbAz0O8w3CpD6TH9dWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا داره مارو میکنه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/79536" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رونالدو بعنوان سرمربی جام جهانی میگیره
بماند به یادگار 405/4/16
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79535" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u11wjBsOcDGWsSHQQqLXiCdOHQPXHa3donEDE0_MvJ1ouPHg-uQvw7JtfzEP1qx3HxjddUrIzGl3CB-xPkuJi4YsZX8ci_w0kwEOjKWpqLHL-z7Hq-2qj-roimVLQB00fxujozxesfq0SYKxwSm2KeddnlVdPQfc_4PYvjVluklkGUlQrxacVg76pMQ31--7LCiao4gsbMObYJw7e6KiMIMpgBfKwEyiZ50bKqX1sdRwSzh8Mit6tn-sE8-hb4krkiKLVpdQar2r7b9V-0V7YKiN3kHaumFg5MAjsY2kprfP7jhMNZTcw-0qRWh1PBEH5A2x3aL7-Vq1U0Pu4VbgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا ۵ تا بازی تو جام جهانی انجام داده یدونه گلم نخورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79534" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دوستان بالا برید پایین بیایید مسی و رونالدو ۲۰ سال تو یه سطح باهم رقابت کردن و الان دیگه داره تموم میشه، با کوبیدن طرف مقابل شخصی که فنشید نمیتونید کارایی که اون یارو برا فوتبال کرده رو نابود کنید، پس شل کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79533" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عزرائیل فوتبالیستا داره در خونه تک تک اسطوره های کودکیمون رو میزنه، نیمار، رونالدو و به احتمال زیاد مسی هم بعدیش(
فقط رامین رضاییان مونده
)
جدی جدی دوران طلایی فوتبال تموم شد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/79532" target="_blank">📅 00:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6lbtjmL91ZI_1OGusPM3uKKAcRo0H49j-BK2Gt5I1phaG3V-5Z1ANZZDkqIvbPUStsjqSoxoTc7gbU_BLrV4xLoLdvXeDZefeCKA8AK7-6EjsepFP6X1_dcv5tUNYeIwWNZ3iOAXACR9aj70Q2Qfrj6Abp4Eq3L_vVABcRoUbTpsJHxeJBoSF_ynKEGzJlFSC6az1hRoY9u2lx6AnVJeUiOqH8ugdcG49xQoTWKfTsrBgdqF-uPMU1jQxDbotmgLebPr-qtKgT_Ls6pCP-vco0r1Y2Pa1KoH2J7rzi1bewTq6Qd1onVu_YXB4zvy5NFaTVXn89Qocp4WCv1X9ADKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79531" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9F_8h8QoIHFo8rrFfbKCNsqLjnAnoHvPuaRlir7Wc98_PM7hPLkCgUYJ2m7sOa4Hl24a-ZTPNLTAGURpj01irTQGgefnfUfPNw3D4P8mxi46vmAqxhWW6fXyuTiOHOA37C26nY-1fZyHzzsr872jiAITE3nf464EI8u3DNuxjBKskGJxSVXLrDyBdgHC1cU6S2d-KO_egyrwwqGPw5z6l7e1654ySNueQlf4RajZ5CiAldJF39qAwINpnDoxsk6cNzM7pBuDEmYPYWooIGKcXj2BU_dXna47kHN7DA6ldQ13EUIAtQg43WqY3yLe5uf3H4aucUJdf2yNLH3JUf2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای تمام شوخی ها و کری ها، پایان ۲۰ سال سلطنت، ممنون برای همچیز و خداحافظ برای همیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79530" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79522">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=ev0O0Jk-9TjWo0nmEuJ6Xp5o7jxRNWff23ThpkFoautXiJFPA06EB-oN0acllAopb4qUtv44Id_0T0UPZvBhSwWUxSiHvtw0Io1nzDPodfy1bbGb0a574WHkDqIM5B4ER2oHD-xwt-VZeJotQhKG3jF_5xZ5mmfaxO6NaIWg25lM-0UwtzDhPn7SrFBvzowSNoXg0HmUr_4-P6wbfr1flB74WpPe3l-iT8Ur4wYdXQZ323U7msWoSb-l7EupcG9tffIITsLxYENLqiH3ID30icsUbHZkDrvB85gUJaKoYrGAJDNqI4CK9wbfRkuqDJGfYiHVBX8X6LtKyrwHNAVtNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=ev0O0Jk-9TjWo0nmEuJ6Xp5o7jxRNWff23ThpkFoautXiJFPA06EB-oN0acllAopb4qUtv44Id_0T0UPZvBhSwWUxSiHvtw0Io1nzDPodfy1bbGb0a574WHkDqIM5B4ER2oHD-xwt-VZeJotQhKG3jF_5xZ5mmfaxO6NaIWg25lM-0UwtzDhPn7SrFBvzowSNoXg0HmUr_4-P6wbfr1flB74WpPe3l-iT8Ur4wYdXQZ323U7msWoSb-l7EupcG9tffIITsLxYENLqiH3ID30icsUbHZkDrvB85gUJaKoYrGAJDNqI4CK9wbfRkuqDJGfYiHVBX8X6LtKyrwHNAVtNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79522" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79520">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79520" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79518">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMqUzVMko704SV4oDx9-IFZsDfwJjjaZCJOm5tDcvU5SUS_7dFIp0BL2wUfTEu4FzwawGxA7x2SsRRrY8iT8-0Yun3PLzWxdjvsdFPI6wpxRSmCZ7GcgyV8SIbJR_iUOeckJz1GRoevlGHeneOuMbMg-Glbn-ll5gEvKe8fBP9EkW44862TB-cNnigWGuHCjpabz42V8awitnrUze7on5kFuf2OKsGhamVJdLzN3-YCGaUs-fHD0ALxk_TKeUpKEMSimvbiWrnG83Bue_7DKCosei0FDf5dUQ0wEwGSXkE4Xez73GfE3V-xHzKH9AsJD05k0lJ0L1uqttnZNNgB9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع علی خامنه‌ای توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79518" target="_blank">📅 00:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79516">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یامال داره گرم میکنه بیاد تو زمین</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79516" target="_blank">📅 23:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79515">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بابای یامال مصدوم شد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79515" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79509">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6traFSA6Eqr7uNsW7cfMzjrn525ZN6tLWqALn7dqodwjaHEKcgCTgPrsAEt0gtUvbY6yIBOTwNNZD11QXSKv-KNrM0SaJNK37Gd4m-kHXb1iFlC9Qw3p3o9n0w-5ZPLIo4kf9kRumrXsvs7Qr4b1In0-DSuRjmlcNGOIhejuISN24Of77e6FbTeTXA4djc8DYS1ve35Ilo7Pf4klOCGXK_kbMfvtUOsEDOO8jWwy-qGh0bVFDGnlGAFl3GFuT4XQ2KpeLWPDirOg_qkHFaRqfEhrfNFwi_zO7zZRw7qlrQiCRnkIBHLX1jBH-FiIKS4Iwi1yu-F4DsEPo1URiBpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzu3MJFvMkcjrRG8Gwweh6DdL3_mT7HNn8M4pWiB5tOtwKEUoBPN45KMynvcFgmMHWee3kBI9YYL9ii5rc9oxrf21JiwD4PttBzg8XHSlGaa9j7mpvCmDCQiS04nYWtHuBvXHueVS0IR66M8DmlyvqBtKRiJ6Y7b0QTuMrPbbhvf0SSGQN230Q7jpWZMOZ9zvIUEaKHt4CjRDg6oi3R-0MKCl4iSaCfk90N0fDBvwGZvhD_XySMVs9oihltUXSt_XhbMkVK9HhpOMSN-rD9p7OIjTvS7_jltRt74_cTzWslBbo667xPc0NEEGVhyKsa_NbZO0swhhZNwvCkh9vQ0FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلیفه سوم سلسله عباسیان هم امشب داره بازی رو تماشا میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/79509" target="_blank">📅 23:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79496">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امشب حتما ی تیم صعود میکنه و بازی صد در صد ی برنده داره و ی بازنده و احتمال خیلی زیاد هم بازی گل داره.
بماند به یادگار
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79496" target="_blank">📅 22:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUXVc0m7Cl4wmdgBuzB8LNo89vqrfdYQ-wx3OTPALuSFHeaTF2LKM2Q0LpBYmIRu7rjVN2wX5qUq5Z1pnp_JL69SSDDA3Pr25-XBRIygJGOvN_jnyuInVenIc1PgzuVVTN5DK578Hqe9-oeaHdseEfLJFKFejqBVY63aPdv7bQaEGdLYwGwOtcHhhiz1GTbt8Lv4e0wetaqFpAyzxB8OQoavz3VMgJQ7EVQciYd8OasR6lnqgT_nsnG5MBoX94vCgzh1c4jsTgqq7Ff5CSMiLHawaXgWVosZxE8j2nKeQrXyZYF0eIzZx6fmZ4bc-upPjOeRHdhtoI5a4kaDe0AAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکشی نکنی کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79495" target="_blank">📅 22:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79494">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0iWXIsnNnBohoqRRXr7cctOwJnHk1_Ep1bfYBWo5Q4sBQNi6YOARK7BGeL32sMYvUJgugolW19hZNiwIqFyYuUle3NNo-kp5VkPfMLhFrekfD9s_S95U9lcuzB7-wInvjtWoTenVrnm68L5J6y3SSmBQydAfzD27xKABE61eks4j1NQCfA0vBFQrftbhvnE5bOuWVFIa4gEybZM1ycRfaOi-oJnhuOGMx1xjR7cHmKB3TGt_mjANOHFM1x6YPZ7kSHnhWeRuLqGFjW0-tvf7RX8Vb2EX7jAuCqMBy0zFamnHNDHi42JR2H12zUztT-N6uOq3YnCV19ZDmlCajfBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79494" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79493">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSMMX2POEgLAeg5hLM2PjYWkSYrf6U7ntGVR8FGB8-3g7s6dpNPqx9fvRlZ6BQHYcaMexQi_NA2pUpg4Jd4WaEAZGQKtibHID6WvRRPjMHHVkSGiOikuyDDybtAcJzdO-ML_Ok1q7RwB8u1xGIwSZLiP2S0u-g5TDnWPIrFPAfGqIrv2FhaY9BUq1w_C56mI_yXYAUvdwFkfYaDLM8ynASejLE4m9FAYWPYwPM0H53klcZMcWVbns-lnmdvExUj6tt6YNT3BPxh0Cb1iCwjJVczpbsWJloZVqCO9f2wtPZsbnY6GWoNZitEL9xlUnvNhLtOuheUG264Xc3M2xCnRqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79493" target="_blank">📅 22:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79492">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط 40 تومن
🚀
20 گیگ --->
❗
فقط 79 تومن
🚀
30 گیگ --->
❗
فقط 118…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79492" target="_blank">📅 22:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79491">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط
40 تومن
🚀
20 گیگ --->
❗
فقط
79 تومن
🚀
30 گیگ --->
❗
فقط
118 تومن
🚀
50 گیگ --->
❗
فقط
198 تومن
🚀
100 گیگ --->
❗
فقط
388 تومن
🚀
150 گیگ --->
❗
فقط
578 تومن
🚀
200 گیگ  --->
❗
فقط
768 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79491" target="_blank">📅 21:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79490">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ژائو نوس امشب برای رونالدو بازی نکنی مادرتو میگام.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79490" target="_blank">📅 21:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79489">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFsEvqdmpQc7AkpPvIqr75lCK16ogBJOTuyFZQ8dGpMXGk0UfW56eEURWZmhOev0RYYBv-Dgiy053MyxpZettVVoeDqDnyvouLJhKxuub_kASYQDNmNKjUWLxTHtQp-If8angOMp90UszgR3k_SLB2N5UAqjDhedtwpRA5cz9mpY4TzmoAIHvbAVmzJIxgY43RDUDo9mQw78bfVZPQuqU_036_2xJo6aAy449Ec0PgP1wuFHOclpiKqoaL-uHBrBVTmF2ghXwB3JKyX7FrKzMI0nBjFP2wv6g_PBdUVG_uz9BJZR3i4wMNpcePn19KdZ2uo0jPiFwsC-hXZYhk-s7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماغ بیرانوند تو گلوی کینگ گیر کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79489" target="_blank">📅 21:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79488">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhSBy0zNzZhQAdTTB9P8GAezLEnt13EVv8wVCZg4nAZ0tEBwbD40T5NMnSFYNW-txUjtxF_s8wTX324-nKcJHTVrBoJwwiJ9ndxaEuFU2jd90kFtRzgjCRo2WyAlkqbspB9uq5_2gDEpCdAqEJH8FHDTAUlgG5t5NclqjI0K2qyyX3QIaHMm6oK-DkzETLZWYJgXLGKG3dGv8EwkraLl7AOzSJ3IUlDgwPdoT9DhyC9NHA6FmORZKWIEXz1gpayVgUzUJu-HIeKa1H1PXlvDrLtbW7dZ4X7Y_AKRNbsm76w_IMeztVmiZcQgbROYJX27EsjYTSEMT50hgyQSiJx05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب اصلی پرتغال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79488" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انگار این ترکیبه فیکه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79486" target="_blank">📅 21:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79484">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlPW6FRYw77T-k6CxpHrE5bSAXvjJl3afx7HLBerTMDJmQXOuARsZ98t83dotGlOCI0ohseyk6_YS1bMj40S8KNhN4aA7fzjIsTJS96JNIRPgEeNumttSPyam3P4ed6swo64-Jcuwf3zGa4A0igN2RrR2YWj07L6-BJQi1731Nbj_9RM1TIonf4b0dPkxd7mctggKMu5WrfLqVu8ekIpEL-O8-LIzPriAr29CNBe2Vj3lWznpNak65NvMs2WyNaK13jjnZ6VzFSHbAl7FcyTRURM0clnGc5b21S46twQ9nHuifn5ZV_eprL69UVMQtMSLydn7Euqw_B6Ir6t8TLndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNwiW-XFjLCN2GmbBzSi3ygx27AzuKbn2ATQlmcyF-QHxrvkNwfTzQD7sPkmdEo_5SUkFqzzIq3tDx8zjagtgMJb_4Yx_SmVWgrya0RtPvikEhlj6RyB0bsZ7Fsdig5eF5hq9Lz1UgXnTOIvd-8l9PFa_Qyxgr0kaislpUJlGns0ZLhMWXU4n2BxZ0SkusZIBaXb7Ls3uHpyS7KIyDLM7e1_HQWtGw4TKZAUw2vsZxjP9T259kRUyER1MNon2QcaA02nLVTjqjI4QqBAGG0pW7fNlZVf_-a7xGHZaMAWk8t4YjcVkS45Z90-Ti_z_6XkNILmhoDBTpQ8OiinS2_gqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوس بدبخت چرا نیمکت نشین شده جاش روبن نوس پیر سگو گذاشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79484" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مبارک رونالدو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79483" target="_blank">📅 19:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79482">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3t2EPKsoq4XB8NR8nSqU5mxnR8GZKqr-XwCbkEhKxFax_QkfHLchk6FjTpr2HfyZuDAeLZhokF9D5rvqI3BbiZdQzqQWPd7lJ64WscYM6Wa9EDqT3Hx4IFoI4c3pLuR9vqyctN0O9xZgRqgQYisKcFl-ePy8w8PvJE3elmn52SZCmvLOSXTMR__JsBrXOHiUTjJ_mnlgXRc93pc4WEDpB8CE68JvT7clr2eTWCpo0A9Qzby7rmqRbTiZqdEAKHOwev1IENbjdTw0v5HbGdttfXf-WmEaSuN7zSd1QmVSAdmp_mZPgMdLB3UJMrcxw7sKFgm3xVWom_1C8zFxFQJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبارک رونالدو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79482" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTMTP0IYqWWnRU2cbCbVmbrEkRBjSHOansNV2oboooary9_ReVDkgAyqR_DyiunrJ06tkwFYNY_k4ln0EVw3L3oP_H2pukhhOVImw-OAw1jQ4XRh5fjPLG3G-qHSqIvPwCVz3q1jYOnWjTzQDltg-qYFhuwnWKzR0NM_Tq7Q3JOERtRc_l3uEBwQrqQRoO2En07WRcJSMI-Y0xQsZjOkZqV6TB14AbRykuELT7Pws20kko25xWZOES-nSSxTaKC4em1bUQZ_Wm9wOVaz5ueZ9kmz7jTZEYlPX_7Bv8SI2Du9WmM2Nv6KT_4iJaoHrcGBaGdoh01mWHYwTq-aNbP73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79481" target="_blank">📅 19:16 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
