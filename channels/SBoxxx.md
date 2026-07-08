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
<img src="https://cdn4.telesco.pe/file/Q5bQerLrruWcGnfcM4v_BY8UMdOi70z9JWx__wsBi80nM3yiHVvOT3lgG9jgki6p7RCn5vznReU25PHUM_lvD-rMvj4Y7EaiLb1afDicLOc0dD3RYE6hKA4GsJqP8hC1Sm1UeScdswNAhsHFsPtp-S-x6R15YiMKz-CVnBna9QqwnLxySnb_0KHxDWjNUHmk4MRx14HMylMIxH36qE7S7sXQIfMknenwz5qMTAYuUPmaFMOfOobYb7uuD3aG3HafYwibTiG5p26N9KZrhrX0olPQiNwqG-iPC50-vESL9zm6ep3CrxDtrDgXnveMhtr5hELgfawoNxeiw7h0_KvVIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 08:43:32</div>
<hr>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">CNN:
وزیر دفاع ایالات متحده پیتر هگستت‌ در روز سه شنبه سفر اول خود را به اسرائیل انجام خواهدداد.</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/18322" target="_blank">📅 02:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6ocxoA3sbA9aux7qCLirIjyIMoqeUBOqLiiCpLrOoaaBK9XT0-P4MV-8sK0BO9o_FeBYaYmS7NVH23kRM8Xg9PvsubyrQ5Kb2gpVd3fKOAxkRbTPiR_OYwMWW-6ye7f_na8-5tP0tBT5RG2rMd4nT8ZFOWBwbZoXeUjJ8N4DYI7cwbFqvcQEPqMkDb1FynBaYiq_XZ39n_2Nj5LYdy9jz7QeTluEEeoMuHi0v9XrR2oDWVqs0w3bRiMoGtL3MpJaxzbPYpbzgflkeRlJFZcJGW2hOh7LHaSyBU4FELbuirUXo6pw5iM82-fV-yhRyLGQGtNA9bdGMQCLQyDzC6UxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!  ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SBoxxx/18321" target="_blank">📅 01:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18320">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حملات ناوهای جنگی آمریکا در ایران، اهدافی مانند سامانه‌های پدافند هوایی، سیستم‌های نظارتی ساحلی، موشک‌های زمین به هوا، موشک‌های کروز ضدکشتی و محل‌های پرتاب پهپادها را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/18320" target="_blank">📅 01:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مقام آمریکایی به CNN :
حملات به ایران برای تنبیه‌ست!
نه مقابله‌به‌مثل؛ و این حملات فعلاً ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/18319" target="_blank">📅 01:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18318">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8C21jrtvcbPzOQ9ehwk842sB66AWWOT1iNWzzS2ZwY7q3XX-pvfYBdyxUL-dAtpcN1Hu1jNAVedheSBYq8X0IrnMU2C8Af_sAz7wN7q8cBQr-t4LDbBO0t_dfozcqjGudlKRkm8qoKomNoKqY7Yfk01vFZtRlOxcp0LcfRF0akAHvm7zxp8rUILc307FS7dxpnQJ-GuvXvAhFMk0BPhMZ-sHajBa3ABZYO1HQmnQpLZ0kh_is11KZdikAi25beQzO3orOkVIuBKfdldcxbrr6pImgKdDoavV9OPq2RfGzPl9HEY-BhBN5ddA4_ChNU4ak2_k5JBP_bCd7cW3fwlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/18318" target="_blank">📅 01:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18317">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=GUU7Lv-yiJISpm-TPb_8VJdALp_RL0cPL0BCtxOu3Pz9Lbx8QlWyOVh22DLvW926bjOcn_0b7mODhjmVquPjFRpd2cnZdNAWsoV5iZqsK_lZ5kzEtsjytwQD2S2ABmMUxGO3U-J0P-BDAOigFOsuAum4rCFOJiCAjaibZ-Re5KlwtC5QW02m_Vafp2j4nsZbdKjt18eatqKPFAFlPbsn_8vitwGl_joYJPmHS8eE-c0avDZe_eSoWWUhcE8Vdtb47ik8toB43aCGrrtl5VOTxsJ-36RSAhzZYUfAwVm0ux1vzGxXTXMJFoIP2AtVlAFqo6EsqcLxleS7uVR4FFnWEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/782b3ef401.mp4?token=GUU7Lv-yiJISpm-TPb_8VJdALp_RL0cPL0BCtxOu3Pz9Lbx8QlWyOVh22DLvW926bjOcn_0b7mODhjmVquPjFRpd2cnZdNAWsoV5iZqsK_lZ5kzEtsjytwQD2S2ABmMUxGO3U-J0P-BDAOigFOsuAum4rCFOJiCAjaibZ-Re5KlwtC5QW02m_Vafp2j4nsZbdKjt18eatqKPFAFlPbsn_8vitwGl_joYJPmHS8eE-c0avDZe_eSoWWUhcE8Vdtb47ik8toB43aCGrrtl5VOTxsJ-36RSAhzZYUfAwVm0ux1vzGxXTXMJFoIP2AtVlAFqo6EsqcLxleS7uVR4FFnWEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی انفجارات پیاپی در بندرعباس!</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/18317" target="_blank">📅 01:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18316">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نفت را بای داریم پدرسگ ها</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/18316" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/18315" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18314">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مقام آمریکایی به PBS: «ایران به‌وضوح نشان داده که به هشدارها توجهی نمی‌کند. ما در حال افزایش شدت واکنش و فشار خود هستیم.»</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/18314" target="_blank">📅 01:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18312">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#باید_برخاست</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/18312" target="_blank">📅 01:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18311">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رسایی گفته بود حالا که ترامپ در ترکیه است او را ترور کنیم! ترامپ هم از همان ترکیه دستور حملات را صادر کرد!
ایشان را بیدار کنید خودش برود دکل سیریک را نگه دارد.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/18311" target="_blank">📅 01:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18310">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_8A71ov-GE8D3TSs67Wjok8iUmfIseI_3tbro4NYCeOb8D5NQlJwJqsMgRJGnnMCFM5aufIrCTgGIM2DuGax6HYwD4llPV8tmswlvonejX5AN40eEVPOkq5f4rAo7lD44g4vN3x0vEGx3lxsWpxFAsbs-o-stFH70hc0PvVC4Ud8eyY1gvc3z-UTplg4ZXyErEtO7WP00lIUuTa01gAKHulylKCac9QGNQzxLA657jafI3mVt9yiTeRp7CAKvbcNdaxGsTFEYIBJKX_yF3S1p99lu961Fn_7dB-mO-v5Cx9eYTnHUMrmCcJK5aCT87KAisRJtwEzgJo2vDeZV_9Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه دکل سگ جانی است خدا میداند</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/18310" target="_blank">📅 01:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18309">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPVq0mg9-f5-hOGy1s5kY-hQehf-3EBV2PHl0sgAlngmxJ04EQ3qD1br9OqRhDYsjv7psP6_AUV01HZQeuuczLeH07kLW1uWIJdx2m8CBiRxI4CTgMJKWZtqjAZ7gEZq-DKP9WIz2EkGZQo7xJ4a5aqeyw7iItPAkxNzgj9dGEJlvM5iNsKxWNc7mgnQBHnCSsLnXnjycKkNsgzUot8ZLpLwRTpHUWDYx6CuaL_5GlUwz3ZiIBQv6vh2VwvYmw6-ZGvLRKkwQANOKH-zSyNJF8eMUAyOePFV8HeFcq-iPE2bWmoHRbpEN2NlsXSVWqVJMkeasEJL6_WPWpr4czwESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویری از انفجار در پایگاه دریایی سپاه</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SBoxxx/18309" target="_blank">📅 01:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!  بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/18308" target="_blank">📅 01:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">باز  هم اشتباه محاسباتی منتهی باز هم از طرف ما!
بارها دیده اند ترامپ اساساً اهل محاسبات نرمال و عرف پذیرفته شده و اجماع-محور نیست باز خریت او را تست می کنند.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/18307" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اژدهای بندر را بیاورید ببینیم منشا صدا کجاست</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SBoxxx/18306" target="_blank">📅 00:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گویا ارتش آمریکا اشتباهی یک هواپیمای پاکستان را زده و سقوط کرده است</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/18305" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سنتکام می‌گوید ایالات متحده پس از حمله ایران به سه کشتی تجاری در تنگه هرمز، حملات گسترده‌ای را علیه ایران انجام داد.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/18304" target="_blank">📅 00:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">منابع محلی گزارش دادند که آمریکا به یک دکل مخابراتی در محدوده سیریک حمله کرده است</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/18303" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/18302" target="_blank">📅 00:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسراییل هم شرایط را مناسب دیده و شروع به پیشروی با زرهی در جنوب لبنان زیر پوشش آتش هوایی کرده</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/18301" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.  فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.  سپاس</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/18300" target="_blank">📅 00:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18299">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به نظرم این منجر به جنگ نمی‌شود.
فقط از کنار دکل های سیریک و اربیل فاصله بگیرید.
سپاس</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/18299" target="_blank">📅 00:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آن 2 بند اول هم که از هنوز از تنبان توافق گشوده نشده صرفاً در برابر بازگشایی تنگه هرمز بوده.   به زبان ساده تر، یعنی ایران تنگه هرمز را بست که از کله زرد امتیاز بگیرد، اما او یک محاصره دریایی در پاسخ اجرا کرد. حالا ایران امتیازاتی را که می خواست نگرفته اما…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/18298" target="_blank">📅 23:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18297">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دکتر محسن رضایی:   کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/18297" target="_blank">📅 23:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18296">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دکتر محسن رضایی:
کاملا مشخص است که آمریکا مذاکرات را با شکست مواجه خواهد کرد</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/18296" target="_blank">📅 23:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18295">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر خارجه ایران:   کشتی‌های تجاری که مسیرهای هماهنگ‌نشده‌ای با ایران دارند یا دستکاری ردیابی کشتی را انجام می‌دهند، با خطرات مواجه شده و تلاش‌های ایران برای تسهیل عبور ایمن از تنگه هرمز را مختل می‌کنند.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/18295" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18294">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یکی از این تعهدات  این است که کشتی هایی را که از مسیر عمان میگذرند میزنیم تا بفهمند مسیر جنوبی ناامن است و از سمت ما رد شوند</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18294" target="_blank">📅 23:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18293">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزیر خارجه ایران: ایران در حال انجام تعهدات خود بر اساس تفاهم‌نامه در مورد اقدامات لازم برای مدیریت تنگه هرمز است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/18293" target="_blank">📅 22:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18292">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/18292" target="_blank">📅 22:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18291">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/18291" target="_blank">📅 22:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18290">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ایالات متحده مجوز فروش نفت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/18290" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18289">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRed Lion Corps(M)</strong></div>
<div class="tg-text">بازی فوتبال تیم مصر و آرژانتین، چیزی تو مایه های جنگ یوم کیپور برای مصری ها شد. کمی اولش داشت خوش می‌گذشت بهشان که زمین و زمان بهم ریخت</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18289" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18288">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بح بح!
موشهای نیل به دامان طبیعت برگشتند</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18288" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرنگار سی‌ان‌ان:
«ترامپ در حال بررسی دادن اف-۳۵ به ترکیه است».
نتانیاهو
:
«این تعادل قدرت در خاورمیانه را نابود می‌کند. من این کار را نمی‌کردم».</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18287" target="_blank">📅 21:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/18286" target="_blank">📅 20:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امروز پوتین با لباس نظامی با رسانه ها گفتگو کرده و عملاً می خواهد از اعتبار و جایگاه خود دفاع کند.  حس خوبی ندارم....</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18285" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=fRV6UwAFSB80lxOpVybSCHPQMSONIkDOD89HI4Of6kIuaKGNWAyHzPjXSoastAA6kUEOUtl0Ppw20AA5yg7YKZhYlKuBFUNYrMGpRZuspZvj2PBHtu_lmDfhEXCFjwnnyHQ8o6hEPbIHkuey222u94EelNlWrirTZAgSWKaoQ29nAiGKob7K0wdOwozhwBPotfcbdbumv4Yv5lyESXzmKCPwoeMFjam3gZ-60A5v_AVahcr2a98v7-el5oWrlbOmu4Sg6fkWS18MoaZW_gc9nDlcrqbzh_Y8sM1vN2HBYi71qTb77GboYnPW9rK9CFvzwuu5rhHC2UGf7qUuvO8exg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb88acd05.mp4?token=fRV6UwAFSB80lxOpVybSCHPQMSONIkDOD89HI4Of6kIuaKGNWAyHzPjXSoastAA6kUEOUtl0Ppw20AA5yg7YKZhYlKuBFUNYrMGpRZuspZvj2PBHtu_lmDfhEXCFjwnnyHQ8o6hEPbIHkuey222u94EelNlWrirTZAgSWKaoQ29nAiGKob7K0wdOwozhwBPotfcbdbumv4Yv5lyESXzmKCPwoeMFjam3gZ-60A5v_AVahcr2a98v7-el5oWrlbOmu4Sg6fkWS18MoaZW_gc9nDlcrqbzh_Y8sM1vN2HBYi71qTb77GboYnPW9rK9CFvzwuu5rhHC2UGf7qUuvO8exg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک تروریست و یک شیفته تروریست در حال امردبازی</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/18284" target="_blank">📅 20:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دبیرکل ناتو در مورد ترامپ:  من از این مرد خوشم می‌آید.  به نظرم کاری که او برای ناتو انجام می‌دهد خبری عالی است زیرا، بله، یک تهدید روسی وجود دارد، اوکراین وجود دارد، بنابراین ما در هر صورت مجبور بودیم در اروپا گامی برداریم.  اما او چیزی بود که برای ایجاد…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/18283" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روته، نماینده ناتو در آنکارا:  ما روز سه‌شنبه در مجمع صنایع دفاعی، ده‌ها میلیارد دلار قرارداد جدید را اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/18282" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2UMvV4WBDJhoUxHZy7OApN0mWa_cT6m3ygjuYfkf_WnlLzPtBC2Dzgz6ShstQJxyB3l4qxNXvKmX-cgwmr6CREGNPHo945cJ4cruQ9UZ2EwEk7GMxoJZjj1oTtGlBMqVwcQy_i-opMds5Jw05eHqGTzaz592YhSpCIAQHZlBozUGMbBz39Fo9At_YuICPaMq8SHd1iMczM6lnr6UzO7qRVyJzCTvYuArf4GDF2Az7MG59eUfOq-40Bb5fmjvucNIFXJehlQDEWFbDcj21pXHH8EKsEoCzSEZ1z2XmpLensbLqwsQRXNhPfOy5W8wjS8N2yAJMOncmPco7pUtdmKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه کشتی بعدی را هم در هرمز زد و نفت صعودی شد</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/18281" target="_blank">📅 18:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ9yfGWhWP8OAixoQln9SiCkSL4sd_e2tW_Gq4zXhndgFFuLKjHVrIJvnp_Ap0ROuBjFXGAXn79x-g-zvtGKtjDEIVSnAev32IMu2-uvyTquclS3gxF8C65HUoc5DGheVldXgnDkCcpSzbEO3vHwdvU-D5V2V-rE-UoiS0Tz9wQQdQ_xPxMriDFQoDDHZIzgtZ-p4PjKG7zTyN266vvrHp9ebU3OXBywOYp6obNh13LpAM_rHrEdjWBoJh138w3cX0yH0_wU0tM0iRIBEi9rjVXW3IROe9VZCHVAzGshY0SXjei4x4hdg5RInieUTc38rqknzJfco0G3cu9VfVLCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">90 درصد این دولت ها را زردپوست هایی تشکیل دادند که از دید چهره و ریختار هیچ شباهتی به این دلقک های اردوغان نداشته اند.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/18280" target="_blank">📅 18:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سیرک جدید اردوغان!  لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/18279" target="_blank">📅 15:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDjBsm4GB8GNxM9AHYJRYOJKdI6_rSb66MBBz14DEsavjr8BK8ixngIvlVKgnSieoki6fRnQaOqdW72qlfcvFYji8JOuVCHOWPOsEKK2n_MXvsvQbRWx2jIJjSXVt_WiV4YtYI5XXIGxrbhuk51IpM6xYJrSKsTAeiNGaT-mTGbz9zdGCx3Y1cFpkEvg-BRSsv4SyN2BWCttaDM0InK9lJjLdE8w4ADp8X4sOeLWmFErbyrgh3cA_rvZl72E36y1tDjsILOXJI8HCkdyfA7oEy8tK247pXC0gJ-309sLBE9-3d7iWJkWp6u5PyKFgSw525svo1oVziPiOHMSvQZlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GX28ame0Prkw7-GqLBXCPqkg6Lo-n-31xHfLIRxLpqftWKlN8Wh-dEKdInSNRf3W0DM55WI1FWQS-bSzWVB3lqnDgkamE7wfx8fj0vXfWVqv6uxorhIjs87pUISe0H7-Rg6-FotRkH-GrmVf2DVtfWykBIxg2lYfcgeMcrNyfIsTeVJRtdD8geyO8FLqO4F30xWkPJqnYfMCQQ-hjJl0Xe3CeujpPPM6bbJIZgDixtURriMl6Xu_DjtPI2BWxcnJC9mHj8QmZEINcMsRStdbSpeYQodIwtdiExWVrjk70f82bRDKCeWZ0QOod5SbQh_PMDTNNzsaCv7DUbYm0qsexg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جدید اردوغان!
لباس‌های تشریفاتی که نمادی از ۱۶ دولت بزرگ ترک در طول تاریخ هستند، در محوطه ریاست جمهوری مشاهده شدند و در صف ایستاده بودند تا از رئیس‌جمهور ایالات متحده، ترامپ، استقبال کنند.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/18277" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/18276" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/18275" target="_blank">📅 14:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حماس رسما انحلال دولت خود را اعلام کرد.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/18274" target="_blank">📅 14:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXcd5GosBboViCawhhWhbMk49MDRtF3n0ga315fDpEEq2fNcvvEC0AJscNvwv-ssN0aUP0ePqGTN3lN9QMIozjIgqhZ3f9toyVmNSrk1XAjpid6aEmgizNeoVyzy82qzWOmPCncAdXzAVr1jHUZY7hSKw3cgJzm46x6DpQB0JlW0k75mCjPAgk2KB9PuX7th3qCN3e4vAZfN-gAbGD7vC4yEAAHVTg-T7XCWsf3wZ7PBbWBjrsbLOwcRvDU335t6bsjB9jv3Hw9ULnLhEcOoLr2e4IKd-pCjzUiF8pxwXYrAjcwPJjTM6ngxBAE3z8A7f0XmkbPCUsqRCra7niF5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایه کشتارهای قومی بر اتحادهای ضدروسی
تنش‌های اخیر میان لهستان و اوکراین نشان می‌دهد که حتی نزدیک‌ترین متحدان نیز نمی‌توانند از سایه تاریخ بگریزند. در حالی که دو کشور از زمان آغاز تهاجم گسترده روسیه به اوکراین در سال ۲۰۲۲ همکاری‌های نظامی، امنیتی و سیاسی بی‌سابقه‌ای را تجربه کرده‌اند، اختلافات مربوط به حافظه تاریخی بار دیگر به سطح روابط دوجانبه بازگشته است. مصاحبه اخیر کیریلو بودانوف، رئیس اطلاعات نظامی اوکراین، با شبکه RBC-Ukraine نیز بازتاب همین واقعیت بود. بودانوف در واکنش به آنچه «اقدامات نابالغانه» لهستان خواند، تأکید کرد که کی‌یف نباید با واکنش‌های شتاب‌زده تنش را تشدید کند و امیدوار است پس از دوره‌ای از افزایش تنش، دو کشور به سمت کاهش تنش حرکت کنند.
زمینه این اظهارات به مجموعه‌ای از تحولات اخیر بازمی‌گردد. در آستانه یازدهم ژوئیه، سالگرد
کشتار ولین
، فضای سیاسی لهستان بار دیگر تحت تأثیر مطالبات مربوط به بازخوانی گذشته قرار گرفته است. هم‌زمان، اقدام اوکراین در نام‌گذاری یکی از یگان‌های نظامی خود به نام ارتش شورشی اوکراین (UPA)  واکنش‌های تندی را در ورشو برانگیخت. برای بخش بزرگی از جامعه لهستان، UPA  نه نماد استقلال‌خواهی، بلکه مسئول یکی از خونبارترین فجایع تاریخ معاصر این کشور است. در مقابل، بخش قابل توجهی از جامعه اوکراین این سازمان را نماد مبارزه برای استقلال در برابر سلطه شوروی می‌داند. همین تفاوت بنیادین در برداشت از تاریخ، بار دیگر شکافی عمیق میان دو متحد ایجاد کرده است.
ریشه این اختلاف به سال‌های جنگ جهانی دوم بازمی‌گردد. ارتش شورشی اوکراین (UPA) در سال ۱۹۴۲ به عنوان شاخه نظامی سازمان ملی‌گرایان اوکراین شکل گرفت. هدف اصلی این نیرو ایجاد یک دولت مستقل اوکراینی بود؛ دولتی که نه تحت سلطه آلمان نازی باشد و نه اتحاد جماهیر شوروی. اما در کنار مبارزه با این قدرت‌ها، UPA  وارد درگیری خونینی با جمعیت لهستانی ساکن مناطق ولین و گالیسیا نیز شد.
در سال‌های ۱۹۴۳ و ۱۹۴۴، نیروهای UPA مجموعه‌ای از حملات گسترده را علیه روستاهای لهستانی آغاز کردند. بسیاری از مورخان معتقدند هدف این عملیات‌ها حذف جمعیت لهستانی از مناطقی بود که ملی‌گرایان اوکراینی آن‌ها را بخشی از سرزمین آینده اوکراین می‌دانستند. اوج این خشونت‌ها در ۱۱ ژوئیه ۱۹۴۳، موسوم به «یکشنبه خونین»، رخ داد؛ روزی که ده‌ها روستای لهستانی به طور هم‌زمان هدف حمله قرار گرفتند. برآوردها نشان می‌دهد بین ۵۰ تا ۶۰ هزار لهستانی در منطقه ولین و در مجموع تا حدود ۱۰۰ هزار نفر در ولین و گالیسیا شرقی جان خود را از دست دادند. در مقابل، عملیات‌های تلافی‌جویانه نیروهای لهستانی نیز به کشته شدن چند هزار غیرنظامی اوکراینی انجامید، هرچند از نظر ابعاد و سازمان‌یافتگی، بیشتر پژوهشگران معتقدند خشونت علیه غیرنظامیان لهستانی بسیار گسترده‌تر بوده است.
همین گذشته، امروز نیز منشأ اختلاف است. پارلمان لهستان این کشتار را رسماً «نسل‌کشی» توصیف کرده و خواهان پذیرش کامل مسئولیت تاریخی از سوی اوکراین است. اما در اوکراین، اگرچه بسیاری از پژوهشگران وقوع جنایات گسترده علیه غیرنظامیان را می‌پذیرند، بخش مهمی از جامعه سیاسی همچنان UPA را نماد مقاومت ملی در برابر سلطه خارجی می‌داند و با اطلاق عنوان «نسل‌کشی» به این رویداد موافق نیست. این دو روایت متفاوت از گذشته، امکان دستیابی به یک حافظه تاریخی مشترک را بسیار دشوار کرده است.
با وجود این اختلافات، بعید است تنش‌های کنونی به فروپاشی همکاری راهبردی دو کشور منجر شود. لهستان همچنان یکی از مهم‌ترین مسیرهای انتقال کمک‌های نظامی غرب به اوکراین است و امنیت دو کشور به طور مستقیم با نتیجه جنگ روسیه و اوکراین گره خورده است. از سوی دیگر، ورشو نیز به خوبی می‌داند که تضعیف اوکراین، فشار امنیتی روسیه بر جناح شرقی ناتو را افزایش خواهد داد.
با این حال، تداوم این اختلافات می‌تواند پیامدهای ژئوپولیتیکی قابل توجهی داشته باشد. نخست، شکاف‌های تاریخی میان دو کشور می‌تواند انسجام سیاسی جبهه حامی اوکراین را تضعیف کند و روند تصمیم‌گیری در اتحادیه اروپا و ناتو را پیچیده‌تر سازد. دوم، روسیه همواره تلاش کرده است از اختلافات تاریخی میان کشورهای اروپای شرقی برای ایجاد بی‌اعتمادی و کاهش هماهنگی میان آن‌ها بهره‌برداری کند و چنین تنش‌هایی فرصت مناسبی برای عملیات اطلاعاتی و تبلیغاتی مسکو فراهم می‌آورد. در نهایت، اگر ورشو و کی‌یف نتوانند میان ضرورت‌های امنیتی امروز و اختلافات تاریخی دیروز تعادل برقرار کنند، یکی از مهم‌ترین شراکت‌های راهبردی اروپا ممکن است با چالش‌های فزاینده‌ای روبه‌رو شود؛ شراکتی که حفظ آن نه تنها برای دو کشور، بلکه برای معماری امنیتی کل قاره اروپا اهمیت اساسی دارد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/18273" target="_blank">📅 13:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/18272" target="_blank">📅 12:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟   هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز…</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/18271" target="_blank">📅 12:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEYN9rfdk04j4gG7ReoqyJ9UaY9_aONY6AXZITaCm6nTi7QAH3JTWMhf_guaCbO9Cg-3jIGVmcAlohcQuOtoGsAdn0CpYnmls3sEbariVAOd7HL6bro710lS5WikJabLBUupNG_1FBwzbFxD65ANN7nkBw1RvePPyTn7DcglvCzfNsjApzEEAXWzcnGqUcE09ubS49FVGw_0ip7En199psM8293hALbgL60OVX1lOMsZg_7V1ygxlf4tn3uaYEk6ZmiHZ-k37_Pv8M4jxbVE1aA9y7iLMflhjYQjALX9ZWI0ffOlaEDKUnUBjS8P6rZVL3gJAysAoGqq-b6CH18Gow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقلاب هوش مصنوعی و گلوگاه جدید آن؛ آیا آینده رایانش به مغز انسان وابسته خواهد شد؟
هوش مصنوعی در سال‌های اخیر، رایانش را از یک فناوری پشتیبان به یکی از مهم‌ترین منابع راهبردی جهان تبدیل کرده است. هر نسل جدید از مدل‌های هوش مصنوعی به توان پردازشی بیشتری نیاز دارد و میلیون‌ها درخواست روزانه کاربران، فشار بی‌سابقه‌ای بر مراکز داده وارد می‌کند. نتیجه این روند، رشد سریع مراکز داده و افزایش چشمگیر مصرف برق آن‌ها در سراسر جهان است.
این تحول باعث شده است که انرژی از یک عامل جانبی به یکی از مهم‌ترین چالش‌های توسعه هوش مصنوعی تبدیل شود. در بسیاری از کشورها، شبکه‌های برق برای تأمین نیاز مراکز داده جدید با محدودیت مواجه هستند و شرکت‌های بزرگ فناوری سرمایه‌گذاری‌های گسترده‌ای در نیروگاه‌های هسته‌ای، انرژی‌های تجدیدپذیر، سامانه‌های خنک‌سازی پیشرفته و طراحی پردازنده‌های کم‌مصرف انجام داده‌اند. امروزه دیگر تنها پرسش این نیست که چگونه پردازنده‌های سریع‌تر ساخته شوند، بلکه این است که چگونه می‌توان انرژی لازم برای به‌کارگیری آن‌ها را فراهم کرد.
در چنین شرایطی، توان محاسباتی به یکی از مهم‌ترین منابع راهبردی جهان تبدیل شده است؛ منبعی که می‌تواند بر رشد اقتصادی، پیشرفت علمی، توان نظامی و رقابت میان قدرت‌های بزرگ تأثیر تعیین‌کننده‌ای داشته باشد. از این منظر، رقابت آینده تنها بر سر منابع انرژی نخواهد بود، بلکه بر سر تولید توان پردازشی نیز خواهد بود.
همین مسئله موجب شده است که پژوهشگران به دنبال الگوهای کاملاً جدیدی برای رایانش باشند؛ الگوهایی که بتوانند با مصرف انرژی بسیار کمتر، توان پردازشی بالایی ارائه دهند. یکی از جذاب‌ترین این مسیرها، رایانش زیستی یا Biological Computing است.
مغز انسان نمونه‌ای شگفت‌انگیز از یک سامانه پردازشی بسیار کارآمد محسوب می‌شود. این اندام تنها با مصرف حدود ۲۰ وات انرژی، وظایفی بسیار پیچیده مانند یادگیری، تشخیص الگو، تصمیم‌گیری و پردازش هم‌زمان حجم عظیمی از اطلاعات را انجام می‌دهد. در مقابل، آموزش یک مدل پیشرفته هوش مصنوعی ممکن است به هزاران پردازنده گرافیکی نیاز داشته باشد که هفته‌ها یا حتی ماه‌ها به‌صورت مداوم کار می‌کنند و انرژی بسیار زیادی مصرف می‌کنند.
همین تفاوت چشمگیر باعث شده است که برخی مراکز تحقیقاتی، امکان استفاده از نورون‌های زنده، بافت‌های عصبی و اندام‌واره‌های مغزی را برای انجام برخی وظایف محاسباتی بررسی کنند. هدف این تحقیقات، ساخت سامانه‌هایی است که بتوانند از ویژگی‌هایی مانند پردازش موازی، یادگیری تطبیقی و بهره‌وری فوق‌العاده انرژی در سامانه‌های زیستی بهره ببرند.
البته این فناوری هنوز در مراحل ابتدایی قرار دارد و فاصله زیادی تا کاربرد عملی و جایگزینی رایانه‌های مبتنی بر سیلیکون دارد. افزون بر این، مسیرهای دیگری مانند رایانش فوتونی، تراشه‌های نورومورفیک، شتاب‌دهنده‌های اختصاصی هوش مصنوعی و رایانش کوانتومی نیز با سرعت در حال توسعه هستند و هر یک می‌توانند بخشی از نیازهای آینده را برطرف کنند.
با این حال، یک واقعیت بیش از پیش آشکار می‌شود: در عصر هوش مصنوعی، توان محاسباتی در حال تبدیل شدن به یکی از ارزشمندترین منابع راهبردی جهان است؛ همان‌گونه که نفت در قرن بیستم نقشی تعیین‌کننده در اقتصاد و سیاست جهانی داشت، ظرفیت پردازش اطلاعات نیز می‌تواند به یکی از عوامل اصلی قدرت در قرن بیست‌ویکم تبدیل شود.
اگر روند رشد هوش مصنوعی با همین شتاب ادامه یابد و محدودیت‌های انرژی به یکی از موانع اصلی توسعه تبدیل شود، احتمال دارد پژوهش درباره معماری‌های نوین، از جمله رایانش زیستی، از یک حوزه صرفاً دانشگاهی به یکی از مهم‌ترین عرصه‌های رقابت فناوری تبدیل شود. هنوز مشخص نیست که آینده رایانش بر پایه سیلیکون، فوتون، سامانه‌های کوانتومی، نورون‌های زنده یا ترکیبی از آن‌ها خواهد بود؛ اما آنچه روشن به نظر می‌رسد، این است که رقابت برای دستیابی به توان پردازشی بیشتر با مصرف انرژی کمتر، یکی از مهم‌ترین رقابت‌های علمی و فناورانه دهه‌های آینده خواهد بود.</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/18270" target="_blank">📅 12:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gx-eQ9-EQrxE67qEQ1SA3THOHwAGdgf69cE-dYhqTv5Jetk1U_KpBoVgY3zqEOGarcgfJr1rZBc-bS13Z7grP2syyZO4hM-seW9oQG0GwEO_f1kP3M2XQGDhuyF5hZZPvJZBrMYK1VngcxOXYXfOsmSDrtHTciKwLKeHkpiqap9Ap919K3gOeFc7pZ-QXPSpdy5RFkOUwvCZuA7t16BCE5zKUY2CUDhoxl7G9AlIO8zNmLcMkiGPasBtq_9hCctvWCpO5bRgz7eqAWiRFKvqFNRw5oGxse7VQGKdcInEIxNWgCqNq-AsVuYYV2_xk-cvC_Xwl5yOliMnZvu3iIlBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارهای پرشمار در دمشق نزدیک محل اقامت شیفته صبیه رفیق بهزاد.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/18269" target="_blank">📅 12:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHvPPiHWXIQEiIGofspaUtBVij3MkRiKqnuAyi4djwiONh_760Bl3p6K_DIvwB3hz525Ac2DOWLfMO9axn3xfKMba9rtenrb-BV-d_m-s8Os_4iDIezVlZvwpFR0rNVGjxzEZzWjA83R57ZQNDaCftmg9jUnkDqZJCstrkDQdRhVzcnNuDrJRAGhsSlIGtEnOyzbzo2UE-HILETSJ4KzAXSgn0XOB8QouR0bOos8TXwUISCn5nsbaYGE1OS5TDB6WxsVz8DKuUWV9d-gGnWY_rJKwvF_HOQfaWNj06SdtufhodtkitaGEDMNJCRzUqfbJyCw0_fdJ4j1DTF3BHtDnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهید لاریجانی اصرار داشت با مال دیگران داماد نشوید ولی خب.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/18268" target="_blank">📅 11:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">راه‌حل شاید ملانیا باشد!   تهدیدهای تکراری ترامپ در مورد تخریب ساختارهای اقتصادی و زیربنایی ایران در صورت شکست مذاکرات، تنها کارکردش این است که جمعیت اصطلاحاً خاموش کشور را به حمایت از جمهوری‌اسلامی و بیزاری و نگرانی از آمریکا و اپوزیسیون وابسته به آن، ترغیب…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/18267" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این زیدآبادی دستکم ۲ تخته اش کم است!</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/18266" target="_blank">📅 11:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18265">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در سوریه، ایران و اسراییل مشترکا از گروه های ضدجولانی حمایت کرده و او را یک قاتل داعشی کت شلواری میدانند!</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/18265" target="_blank">📅 11:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QovitG34Rqj9oCpnNmo6a1LCo5TszQDSx2RUILL1grTe7kMR38Cvmtf5TkK7tZy9tmx7Ja7yNGVnoJfhZCRV_q6P6HoSNHhJGk3gnxwpFeN1-4obzP4Pt4AParYl7IFPOTc58L_KMVlaOLVzvGZVVZV-ySOjXvENGTo4XsovDnGLo0uu_DOH5_KgEP1NTYv0CDxxVzc0yk8zoX-lMuELNKhOuOFMr_QNkwFtWy8uUBMSpvNQRA4jiP0j4I-BCOUMCT86fyOq1jPweRG65Ck8eFvh-x59tX6RiuScXqlTyWud_vW5b6g7_2yUouZbRe1EEH2LySrSN5eMk2SQOkKKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایین قرار دارد و ادامه شرایط نرمال پیش بینی می شود.</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/18264" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/18263" target="_blank">📅 10:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت . اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند . این حجم از اختلافی که…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/18262" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromParvaz dar oj</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3ay_BPUCvep1PC_abVJsCEW-K-WeVc2jGNzT1LfX0nbaXSycKyPRsf28QB1l9PS72quzWW0uzoEgeZHxRbqB0Nb5MX80BQ-h2Y1qQGnl4KZ31VHGPq-XsXUWz4GQQklAFqKxP0EsKm3FxCO61SpXAfxkkFvbyvXL9dSEgw2Bdy38fBzXK3ZWmUj8_6Zb9iY8HVgJEkZ05YS44B3YmxDecS60I4Pe4QEQMps3GSpb70HdT13zpvE0n24rZcS2aOKs90F1KRFMr8498xvnfe0985mkMnDm9PkalcB_sJR7Ipc_2hglfEqupLtqbXz2WZurLD0C-eszon2rnN2I4e3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◆ روزگاری وقتی اف 14 فول تراتل روی دریاچه ارومیه پرواز میکرد ،نعره موتور تی اف 30 تا اتاق خواب مادر الهام علی‌ اف میرفت .
اما امروز تاندر تحویل گرفتند و با وضعیت فعلی آسمان ایران،می‌توانند تا تهران بیایند سلفی در کابین بگیرند برگردند .
این حجم از اختلافی که افتاد واقعا خرابکاری نیست،شاهکار است!!!
@PARVAZDAROJ
| 𝐀.𝐑.𝐀</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/18261" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست     معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/18260" target="_blank">📅 10:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جمهوری باکو به برنامه اوکراین در زمینه پهپادها پیوست
معاون دبیر شورای امنیت ملی و دفاعی اوکراین، دیوید آلوویان، در مصاحبه با گاردین اعلام کرد که در ماه‌های اخیر، کی‌اف توافق‌نامه‌هایی در چارچوب برنامه Drone Deal با شش کشور امضا کرده است و به گفته او جمهوری باکو نیز در میان این کشورها قرار دارد.  این برنامه شامل توسعه مشترک، تولید و صادرات پهپادهای اوکراینی و همچنین تبادل تجربه جنگی بین کشورهای شرکت‌کننده است.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/18259" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18258">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/18258" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUuKY-JHHBBhjPkSgTVH1s7cnQ0osiZA2oTArGe_ATUQGZfYqsDWin6TP-UR2D5Sm2dCAarUID_h5F78_3jlwBu8-f7tpmGr1lbgQGS3AmXaxRo88QS1tNK5szwCrW0oUc2tp-Olsyt43HGhirIQPyKn1YwTBxKVXnHKmo8DT0bqhdDAkPdpqgWekY2KAgvuO886bFWk8MfsrbTVGhjIceAi1eYNVPjutbc_NncBKPTZyg-ZqkdCBT-xWWvB9GPhM63_bp2alcg-AOiggijf05Okr_x8sOs-8_8wVznnaJoGjJPDWPpALw-PWLhz-jJIIjOLdY8MxKOxLAwGna0dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ دبیر شورای عالی امنیت ملی به ترامپ</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/18257" target="_blank">📅 09:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/18256" target="_blank">📅 09:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مسئول آمریکایی به اکسیوس:
بیبی وعده‌های زیادی درباره جنگ با ایران داد که محقق نشدند.
اما چه کاری از دستمان برمی‌آید؟ او خواهد آمد. او وعده‌هایش را می‌دهد و سپس ما مجبور خواهیم شد همه چیز را بررسی کنیم.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/18255" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خیلی جالب است؛  از 6 کشوری که شدیدترین بحران های انرژی را تجربه می کنند، 4 کشور در منطقه ددخیز خواهرمیانه هستند و 3 تایشان (سودان، سوریه و یمن) در ژنده پارچه ای که به عنوان پرچم رسمی معرفی کرده اند، رنگ های نجس و نحس پان عربیسم (سیاه، سفید و سرخ) دارند</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18254" target="_blank">📅 20:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqtPkhdg_6V9Bj7moef6ZyVOnvC3hxao7VKr1_KdGwHhx3hStBi_bWnRvF59arpAQqJtKyltI8cyv77kNH9MwNSW_dBvCPcP3fHkKPpbHfLSIcOSh3UWJx758cqGmb4kilB32gG0nnVLr6e4dmdSJi6ab9KncGGogaif3aC_nvZ-eNc7kIIP9b03M_yDYHUBRO37rFYlwfkv3t7SbuX720eq8_UKn8t4oAGii7SFSQTPeyTi_r9zkxmQONaG3AjJb9Hh1yj4Ju8c-qmVwd39sm7mWbVzU8Wd5ecrFC7Huyv7ag8RxKNkmFxgeKirNmVW0PZdwuUP2OEFx7zRCQxLbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما در کل این سیاره خاکی بگردید هر جا کمبود برق و انرژی باشد احتمالاً یا کمونیست هستند یا دوست دارند شبیه کمونیست ها باشند و با شکم گرسنه و خشتکی پاره مرگ بر آمریکا و مرگ بر سرمایه داری سر بدهند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/18253" target="_blank">📅 20:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شبکه ملی برق کوبا روز دوشنبه دچار قطعی شد و حدود 10 میلیون نفر را بدون برق گذاشت.  مقامات اعلام کردند که علت این قطعی همچنان در حال بررسی است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/18252" target="_blank">📅 20:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گویا آمریکا می خواهد در این مدت آتش بس موقت با ایران، تکلیف کوبا را یکسره کند.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/18251" target="_blank">📅 20:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز  افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/18250" target="_blank">📅 19:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ در مورد جنگ اوکراین:
به نظرم ما بسیار نزدیک‌تر از آنچه مردم تصور می‌کنند (به آتش بس) نزدیک هستیم.
پوتین می‌خواهد که این جنگ پایان یابد. من این را به شما به شدت می‌گویم. ما یک تماس خوب داشتیم.
زلنسکی در واقع می‌خواهد که این جنگ همین حالا پایان یابد.
ما می‌خواهیم به ناتو برویم و می‌خواهیم در مورد آن صحبت کنیم. و من فکر می‌کنیم که می‌خواهیم آن را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18249" target="_blank">📅 18:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
بمب خبری ... اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران  https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/18247" target="_blank">📅 15:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan Movahedian Channel</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=ohTdeYQqFk9xsoRDiv7fpeFFX6coPuY0DlM_RfAhPxsaoqfvqtPOc-4cHlONusrIzmf0v3peOqmaEkObrsoMCI0G3kJPiBDnlb6vdg52zZT3GIaaafg8KwBpgSOduk7SAeckpyLTry2wYwb7vraiK2V7wWnMevKNnx6f5U4_q2UzlQDknAXQxNziBzuD7hGgoRT_0NMOA4fjka5AJhwvBdry30S2BLncQW7PCrrVyVUoMuAVN0Z3jz19vDpnzV8dr7C2KpaZSM8h8QyKUXnMOcO2yxnrOMIkykxtSAEJXUSVosstaHuU-71MMRtu3qUwzx8r_d1KaXDGYofM6HoNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a018aa532.mp4?token=ohTdeYQqFk9xsoRDiv7fpeFFX6coPuY0DlM_RfAhPxsaoqfvqtPOc-4cHlONusrIzmf0v3peOqmaEkObrsoMCI0G3kJPiBDnlb6vdg52zZT3GIaaafg8KwBpgSOduk7SAeckpyLTry2wYwb7vraiK2V7wWnMevKNnx6f5U4_q2UzlQDknAXQxNziBzuD7hGgoRT_0NMOA4fjka5AJhwvBdry30S2BLncQW7PCrrVyVUoMuAVN0Z3jz19vDpnzV8dr7C2KpaZSM8h8QyKUXnMOcO2yxnrOMIkykxtSAEJXUSVosstaHuU-71MMRtu3qUwzx8r_d1KaXDGYofM6HoNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بمب خبری ...
اولین حضور رهبر معظم انقلاب آقای مجتبی خامنه‌ای در تشییع و نماز برای پدرشان در مصلای تهران
https://t.me/+SV6YYFA0zX1kOGZk</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18246" target="_blank">📅 15:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18245">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ونس: ظرفیت تهاجمی روسیه نزدیک به صفر رسیده است   در مصاحبه‌ای با تایمز بریتانیا، جی‌دی ونس، معاون رئیس‌جمهور ایالات متحده، وضعیت نظامی روسیه را ناپایدار ارزیابی کرد.   ارزیابی او: توانایی روسیه برای عملیات‌های تهاجمی بیشتر «ناچیز و تقریباً صفر» است. این می‌تواند…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/18245" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18244">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 2  دوشنبه 6 جولای 2026</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/18244" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18243">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMK8yYEETA9sK6FuFP6wxMitnmE3l-mRq23kxwdbt1YPx5WZ6wQcZisk6bGW55V-0edt-kJyIYw_P3EgmZe50GF0l9hBMoXVkTSq1neZKWE9qh5s_GI_EwWalJZnob9uH9W8bj1_mBMuecP1rxo3uIc4pJTJOhVXUtxuWZAn1b6pcc9Ga6WiyhczRbTUGZKFsEand0dzjSi3B12TTOl7YaZpDWC59vMl1J8kCJQQCAe4GEx3Vir0Jj9qMPbhlFmKJWsHZ9CpW55g8x0pN5xbF67XCzH63HX9Cujc56c6X6Pu6fc9XgNd2A-9HREoXe7SwyGw6U8lFx5VqakgdlOr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/18243" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18242">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/18242" target="_blank">📅 12:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18241">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نشست ناتو و 3 پویه اقتصاد دفاعی روز
افزایش هزینه‌های دفاعی در کشورهای عضو ناتو در حال تبدیل شدن به یک روند ساختاری و نه صرفاً واکنشی به تنش‌های مقطعی است. هرچند در ظاهر، این افزایش می‌تواند به‌عنوان یک محرک کوتاه‌مدت برای رشد اقتصادی تعبیر شود، اما واقعیت اقتصادی پیچیده‌تر از این برداشت خطی است. هزینه‌های دفاعی معمولاً با تأخیر وارد چرخه تولید و تقاضا می‌شوند و اثر آن‌ها به‌صورت تدریجی در اقتصاد پخش می‌شود. تجربه‌های تاریخی، مانند بازسازی ذخایر تسلیحاتی آمریکا پس از جنگ خلیج فارس که چندین سال به طول انجامید، نشان می‌دهد که این نوع هزینه‌ها به‌جای ایجاد شوک‌های فوری، بیشتر اثرات میان‌مدت و بلندمدت دارند.
در سطح ساختاری، ماهیت خریدهای نظامی نیز در حال تغییر است. جنگ اوکراین و استفاده گسترده از پهپادها در عملیات علیه روسیه و کریمه، نشان داده که فناوری‌های کم‌هزینه‌تر و غیرمتقارن در حال بازتعریف اولویت‌های نظامی هستند. این تحول به‌طور مستقیم بر زنجیره تأمین دفاعی اثر می‌گذارد و تقاضا را از سامانه‌های سنگین سنتی به سمت فناوری‌های سبک‌تر، هوشمندتر و مبتنی بر داده سوق می‌دهد.
از منظر ژئو‌اقتصادی، یکی از روندهای مهم، بازتنظیم روابط تأمین‌کنندگان تسلیحات است. اروپا به‌تدریج در حال کاهش وابستگی به تجهیزات نظامی آمریکاست و به سمت توسعه ظرفیت‌های داخلی یا تنوع‌بخشی به شرکای خود حرکت می‌کند. این تغییر می‌تواند در بلندمدت ساختار صنعت دفاعی غرب را دگرگون کند.
در این میان، خاورمیانه نیز به‌عنوان یکی از بزرگ‌ترین واردکنندگان تسلیحات، نقش تعیین‌کننده‌ای در جهت‌دهی به جریان سرمایه و فناوری نظامی دارد. این که بودجه‌های دفاعی کشورهای منطقه به چه نوع فناوری و از چه کشورهایی تخصیص یابد، می‌تواند بر رقابت جهانی صنایع دفاعی اثر قابل توجهی بگذارد. در مجموع، آنچه امروز مشاهده می‌شود نه صرفاً افزایش هزینه، بلکه بازآرایی عمیق در معماری اقتصاد دفاعی جهانی است.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/18241" target="_blank">📅 11:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18240">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odh3jbFXlqbvAfbD_s-UXudVWBuxHitjF7KDE0qNiQOEF4JNdstWxbxItHhhL80Qf89BpMddjhEfAMEb2X522PxU4OHjL558Hp3jJD-YoZiPqhhkGl5KVCgmOUt8JWg36TepKNFVHghz6MPskxI3k1iHrtHs5Udyp9_g8cY4TjH7pjdS2Zf1pNmmWXzOPhTAeXNtTVDNl_YD85pZeKOW11DRCt8oZRYdD3OfzX4XpGpDjUJmuXFivq-ZCsut4VMEIvba7ihuieo32s8iWeyj1nNASYJmBdWSuSGSjlTFNnPXaGaG4toLOBZAwh2A9mq9lOxO4q8tyCCnLMUcuGG0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتک برای امروز در سطح میانه پایین قرار دارد و ریسک پذیری بسیار ملایم پیش بینی می شود.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/18240" target="_blank">📅 11:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18239">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/18239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets  شماره — 1  جمعه 3 جولای 2026</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18239" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18238">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شبکه ۱۴ اسرائیل:
سپاه قدس واحد جدیدی به نام « یگان مختار » تشکیل داده است که با شهروندان مکزیکی و آمریکایی و همچنین ایرانیان خارج از کشور برای ترور ترامپ و ژنرال های آمریکایی همکاری می‌ کنند.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/18238" target="_blank">📅 10:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18237">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/18237" target="_blank">📅 10:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18236">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twgbUANThFQlUr_JvxHn4nFX7dp3Kd2OmHzG6_ofOVnUjaH9smHxzlP114rmdIpTpfj-UoFmQ7vtEwxRuWpu7RbtdS95vNRy383-QpjTl4SfIhafzBKI9Hd8gpAdHQkSfkt-KOkgU6rKHIiWaajOU4tpOtFuRaQ8i4jkk6bv_xaxZoC1JYxS_wk5bZpLfltVrJ1cYQmeUkIwq_ucWuqRqoQC_ruEzjx_ANfvPXacxURmBrfqW8J65Wb4PfC8wQgccsTzm4DizAmey9M7k2ZqypAUl2Sdu8A63REyg_eBxXFPRiSQfuDGtUTqGYZSGeJYm_7ZIUr3Lq12fXgho4_9Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گویا واقعاً زنگ زده اینفانتینیو و گفته یا بازیکن اخراجی ما را می بخشید یا بازی خراب!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18236" target="_blank">📅 09:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18235">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/18235" target="_blank">📅 22:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18234">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGQYnmpFhxfrZDZ_eaXJXNdG0anqFru4_HTXCkJlD1DsVuiTcVBxxac9YpxnxJYQXSMIlj5zih4CftmHFCDjFueTvSv0iSkqSOFA09gkO-u2m9Ey7wt17IV9x5gRQ44wPoLUUViQLcQ1B2usZm_uNFWd9fHhklQPawZ_lrwdNsoNxv_B9GSB5qJPI542hDUaEfRMz_rMcrvSl0oiF2bH5a-mIY_NsCgW60jOfQ_dZBGBS-H_agyDmQbdnDShic1xLt2QP5K1v_1vRQt-Jwc-cFYgS6ECcf1obaYyhrrAtLaWxxkhuFj5VF_9CMhL2tcXF1n3mOqQ0yy_apPaT7zzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
استقرار بالن نظارتی (الکترواپتیکی)  در آسمان تهران</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/18234" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18233">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نتانیاهو:
«برخی روستاهای مسیحی‌نشین لبنان در واقع درخواست الحاق به اسرائیل را داده‌اند، زیرا ما از آنها در برابر حزب‌الله محافظت می‌کنیم.»</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/18233" target="_blank">📅 21:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18232">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایران می‌گوید از آتش‌بس با ایالات متحده برای تقویت آمادگی رزمی خود استفاده می‌کند.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/18232" target="_blank">📅 20:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دو نکته:  — از این میان ما سومی (J-20) را داریم. (البته ماکت ش)  — آخری (جنگنده کان یا خان ترکیه) فقط یک مشکل کوچک دارد و آن اینکه موتورش هنوز پیدا نشده که انشالله این هم حل می شود.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/18231" target="_blank">📅 17:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18230">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.  @MonazeratChannel</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/18230" target="_blank">📅 16:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18229">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمناظره‌ها</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=D9AJS4F701zsyHnG50ccb5NLhabw0-lFz-CXnT6ozw3lw7R2i58wX-sn1RqcKFdnIfR39ia7OPn-W1IDCNEvtg_msnX-fGIip8GO67eRubv8L99G7KdD8pBSufzX2D3n84Zjnt3GfSlIXzsGnmSfTj1xhlAwjA067a7aNUss6hAifSlYGBzXxMGTenNQo-LRGCH-pS1ptBRFKjd6EyjewJJk0uzIvSuLJ-yYGe4Su0gMu8oN7V7cxv6F7fPaZ2g-NZAyYd6QdtbXN5HE72XtS5v3M-aHngNg2Q7OGKwOw4ToVStUXvfE9fzmspUPhEvMVhVXS1Z4qXFjWtgcs-2gNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f11f469c.mp4?token=D9AJS4F701zsyHnG50ccb5NLhabw0-lFz-CXnT6ozw3lw7R2i58wX-sn1RqcKFdnIfR39ia7OPn-W1IDCNEvtg_msnX-fGIip8GO67eRubv8L99G7KdD8pBSufzX2D3n84Zjnt3GfSlIXzsGnmSfTj1xhlAwjA067a7aNUss6hAifSlYGBzXxMGTenNQo-LRGCH-pS1ptBRFKjd6EyjewJJk0uzIvSuLJ-yYGe4Su0gMu8oN7V7cxv6F7fPaZ2g-NZAyYd6QdtbXN5HE72XtS5v3M-aHngNg2Q7OGKwOw4ToVStUXvfE9fzmspUPhEvMVhVXS1Z4qXFjWtgcs-2gNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چرا نتوانستیم از صدام حسین غرامت بگیریم؟  حمزه رحیم صفوی.
@MonazeratChannel</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18229" target="_blank">📅 16:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18228">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/18228" target="_blank">📅 15:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18227">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مسؤولان آمریکایی نگران بودند که اسرائیل ممکن است در طول مذاکرات صلح حساس در بهار امسال، از جمله وزیر امور خارجه عباس عراقچی و رئیس مجلس محمدباقر قالیباف، رهبران مذاکره‌کننده ایران را ترور کند.  با نگرانی از اینکه چنین حمله‌ای مذاکرات را متوقف کرده و جنگ را…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/18227" target="_blank">📅 15:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18226">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/18226" target="_blank">📅 15:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18225">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">قالیباف، در مراسم تشییع رهبر سابق ایران:  «ثمره خون خامنه‌ای آزادی بیت المقدس خواهد بود».</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/18225" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18224">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/18224" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18223">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کلا خاطره خوبی از محاسبه خسارات و جمع آوری شواهد نداریم.
بار پیش
هم که جناب عراقچی داشتند خسارات اشتباه محاسباتی اسراییل در جنگ ۱۲-روزه را محاسبه می‌کردند که اشتباه محاسباتی بعدی روی داد و اصلا محاسبات ما به هم ریخت.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/18223" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18222">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:  "ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/18222" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18221">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سخنگوی دولت ایران، فاطمه مهاجرانی:
"ما در حال پیگیری قانونی شکایت مربوط به ترور رهبر سابق هستیم که با جمع‌آوری شواهد آغاز شده است".</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/18221" target="_blank">📅 12:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18220">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Trump Accounts
سرمایه‌گذاری بر نسل آینده یا
پروژه‌ای سیاسی؟
دولت دونالد ترامپ با معرفی طرح «Trump Accounts» تلاش کرده است ایده‌ای را به اجرا بگذارد که در ظاهر، حمایت از آینده مالی کودکان آمریکایی را هدف قرار داده است. بر اساس این برنامه، برای هر کودک واجد شرایط، حسابی سرمایه‌گذاری ایجاد می‌شود و دولت برای نوزادان متولدشده در بازه زمانی تعیین‌شده، مبلغ اولیه‌ای را به این حساب واریز می‌کند. دارایی این حساب‌ها نیز در صندوق‌های شاخص کم‌هزینه سرمایه‌گذاری می‌شود تا در بلندمدت از رشد بازار سهام بهره‌مند شود.
طرفداران این طرح معتقدند که ایجاد سرمایه از ابتدای زندگی می‌تواند فرهنگ پس‌انداز و سرمایه‌گذاری را در جامعه آمریکا تقویت کند. از نگاه آنان، حتی یک سرمایه اولیه نسبتاً کوچک نیز در صورت رشد مستمر بازار، می‌تواند هنگام ورود فرد به بزرگسالی به منبعی برای تأمین هزینه تحصیل، خرید نخستین مسکن یا آغاز یک کسب‌وکار تبدیل شود. این رویکرد همچنین می‌تواند وابستگی شهروندان به کمک‌های مستقیم دولت را کاهش داده و مشارکت آنان در اقتصاد و بازار سرمایه را افزایش دهد.
در مقابل، منتقدان بر این باورند که اثر واقعی این برنامه به توانایی خانواده‌ها برای واریز مبالغ بیشتر به حساب فرزندانشان بستگی دارد. از این منظر، خانواده‌های پردرآمد بیش از دیگران از مزایای رشد سرمایه برخوردار خواهند شد و در نتیجه، شکاف ثروت میان طبقات مختلف جامعه ممکن است کاهش نیابد و حتی در بلندمدت افزایش پیدا کند. همچنین برخی ناظران، انتخاب نام «Trump Accounts» را اقدامی با رنگ‌وبوی سیاسی می‌دانند که می‌تواند این برنامه را به بخشی از میراث سیاسی رئیس‌جمهور تبدیل کند.
در مجموع، موفقیت یا شکست «Trump Accounts» به عملکرد بازارهای مالی، میزان مشارکت خانواده‌ها و نحوه اجرای مقررات آن وابسته خواهد بود. اگرچه این طرح می‌تواند گامی در جهت گسترش سرمایه‌گذاری عمومی باشد، اما قضاوت نهایی درباره آثار اقتصادی و اجتماعی آن تنها پس از گذشت چند سال و مشاهده نتایج عملی امکان‌پذیر خواهد بود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/18220" target="_blank">📅 11:15 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
