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
<img src="https://cdn5.telesco.pe/file/hUEp8XfCtW9Z6zlJulYiyVgtsTiHF-ATVrStROt45Au4lncQBrxpxkxE7MvsHaoE6Zzypv5CecIUaIn9aYTa55D7qhKNd2Vngcow0IOj6Umwcwd4b-edKrosf-w1w425pidIkYSQV3Qdb7y4ZL2MrwEUyVKmuPjcVKW111328VUdbsaei5kQxiNrTjUSLn4JeCOXsUqvsKrI9lzosuOI6nBw6JBlGS3gM_Sz6SXo0_e2SKkn-e25XQe4MakN7q-C4pq7pVTW1eKe_F5Az6keGmkQ58VWRcVod2aEOO1fLVT-udjXUOk75JkbwNwi3UguNq6Que5AjQA_57XW3YpmiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 648K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 22:33:56</div>
<hr>

<div class="tg-post" id="msg-97917">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRs6kMBEPMEHj5MnDLQ8ZVoU5BUoapWV5IB9dYgqIrweOPxXqPs8YjeuvCeUlSVcf2UrLitZHsQI7kSQjAud0fD8M2OzfhVutQNkHWGvviZ7_5sMqCuuRISeiiJg3jdSTcm2b3t9xaJbk5LhDgiRPm6s844uUS2dO0qrg4ztA5Su_OyB7iV1FR4BXEApZy78W4KeJwPaK-uHBP1HC2u3Lvz2mkD_TL9o9w9lnttlo3PDnQrGmJFaQvDSugLhv9Z1ettKB6zvFEBZq7Gfv1WdJR_bdKte9nWkNMH3MuJtC51fKFrkVej_u4sl5d18GiyprjszrwZX1z-nsRh58ZO5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
امام عاشور پس از محمد صلاح (3) و عبدالرحمن فوزی (2) سومین بازیکنی است که برای تیم ملی مصر در جام جهانی دو گل به ثمر رسانده است.
🔹
او پس از محمد صلاح دومین بازیکنی است که در دو بازی مختلف در جام جهانی گلزنی می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/97917" target="_blank">📅 22:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97916">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پایان نیمه اول
🇪🇬
مصر 1 -
🇳🇿
استرالیا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/97916" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97915">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYKzugFDGalxJBSILInjWsoJYVQoa9tCIUUXhyAqRHZnvQduyraCdpp-f47KIiKTbA_QR6CNeSa6nj8FWXUBnWnMg3YBghFWuyB-8SZuz3j1n0eps_AX3qrmgDjstoj01d5vdO-cRq0PhnUpo5PkTXUVXDod81wOptKxb2Pn-BDrMbcB_TsKjsHCU_f6E09dvnmVclYVJnnxxtSDf2pUZpoR9qZBbMn8U5MiYaSkupUYE7oO9MMe32l3Du129TCJBK-vlHW4uYYrcWMZTgiepPLiQ_DCjuAMfXJ_0M_7wUQfMKpG4E8LHcu8iQBy-r6sE_l9Z4Nux9BuC-fa-O7gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی اسپانیا برای بازی با پرتغال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/97915" target="_blank">📅 22:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97914">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbfbd3G2qmlgplhQQGr7dljO2EBwD4DgiX73h5g-1EP5cH02s1zKAVWig5UBUJboYmYH-ri76brH8Ps-MmP4bjmSNuGimltuznu91L_36eSa5t1rTwz6o42sppFJdx1y3A1Jd-0xIC22LiX6dyo-p7ALmcMD9TTvLJGhzM2C4zOLJ7XkQucaa28oN1iujNTa7-TEi3sN-iYIe8khkCk1RxknYQypq_U4BggXgmcyYgCEktWKXeyQwOUY8nu-nBFErjD2vvX8q18tQ6pomkCbT0efsky4pa0iB1wvkNJ9cbKR-A_QnGM7AlLKOmUysoOqf_rALxY1Isr8VRiMmZPQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سرمربی کره جنوبی به دلیل تهدید شدن به مرگ از کره فرار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97914" target="_blank">📅 21:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97912">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zd0iHZcZWWt4wMzSFJVyW7ZkZzZgP-VmbcW2y10uuf9WL5vsuaCfykeTFG4cOPyjwWverRD9eoq3qB0hLMWiNp6pupgKJr7faWcjZz1eZT5Qtb3zaX9lFCrMrOdYiyCZIpiS7j6NxJ_7f2P0COQPfvEtqZrBu-TEAS92xpAT5F_iVT8Y9o6nIJ7pdgYL7IMNN_jD88dOrAT3MN08Kptl9QViO23VyT6GwkxNexwU2K6HvUspSOIrao_6fMxfYbxMd-9b33NE5qix9VrwMHoZd1F7BBqCdA0hfMpIXsh2lF4d_GPOQKSbZptAoppkE4kWx_DRQc5S-yfB_OvsnmKJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4c7wigYxVOjgxIPfquli-YOsc_qF6fcorT53dqCtKrjvWLmj2v30sR5bBx8ZMsUgyB5CszqTExHv5y7uStMBg6Na0YMBjAYsdIRGCEQzRCCuaunBCLLTiyXtWaY78Y5MtrZh5qixJY1UGCGxdwxXZ6SBsnK_oYds-m75nL2NBzV3CZaaYoL4ZLcjucP76z-cpE6yPUaKEgm_6SUR-Tzlj7bCENdSryMizaaer8UdZlmliBFddLdFHkte8WxGeE_30Arqu4WWKBLJXhwvk7GIvmO1D0wqkKOmLOJqsVg8KR9hDKJmp684vT1dL_52pKFunU9SugLdVdzOETLPIGr-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🆚
🇨🇻
🗓️
۱۳ تیر
⏰
۰۱:۳۰
آرژانتین
🆚
کیپ‌ورد
📌
آرژانتین یا شگفتی تاریخی کیپ‌ورد؟
⚽
🔥
مدافع عنوان قهرمانی برای ادامه مسیر به میدان می‌آید، اما کیپ‌وردِ شگفتی‌ساز بدون هیچ ترسی به دنبال رقم زدن یکی از بزرگ‌ترین غافلگیری‌های جام است.
👀
⚡️
آیا مسی و یارانش صعود می‌کنند یا تاریخ دوباره نوشته می‌شود؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/97912" target="_blank">📅 21:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97911">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2fa6b65337.mp4?token=nOWqkQOnzmLpx0lOrpHev6mPo-rzauDB8NORPQxX7nutEL_DCcgheCHW12Lk-sL8e6KYYJmajC3us-21ROKvOsF-51RYZwDxuYL-UFnPj8M2nWtq3ic4R77r-Q23vV5-12n6AH9rOW3NNJNKRnGruzFD-uROQ0TO3oQYfqO3N0EpdkZa5OwFOuP5hxz6DSQ0WAzYQUKA6dH5x7yjr8GpFrfsXkjqGzfJIbdO9Xa89hTn1rizLaUr6apY7KX8VEZYFF3lBM7p23AjJ4JcrFys-zjPt7KayL0vYHX1vamSf065c42O_ALkXm1wTlTonzSBnyPkHypOUhmUPFtJ9HIl367uYOjW6HJMDBXVtQYwitspowIw2tYwzTvadkl-R71NYlimylWEj6xEXa9ouqblCAA_1u9NZxmzjNmU_xqmbbZRZJRHWkUk5aCymV9_MkFEkj4kTyD2LRZOfeSpEZxRA1TUhKmrW7g_AbO_-lZbcrA6IHqUbfzlOYwEwGURJnaZAU8KhVtp5KsxoL6LQawZTlNZv5vEpj5Zz8KXFQhsCdFZBgMC5LXGOYw5NLHkefZyAki1ou0OvF9_hQCn-eSHxaSv2EZ9pMlFeWOFGGhmQOoo3n_WyVJDUgueRW2q2uq9gHKNif8F4X5XcrcBEiyKfcAn3OiY5UHRqLn-VKW2BCY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2fa6b65337.mp4?token=nOWqkQOnzmLpx0lOrpHev6mPo-rzauDB8NORPQxX7nutEL_DCcgheCHW12Lk-sL8e6KYYJmajC3us-21ROKvOsF-51RYZwDxuYL-UFnPj8M2nWtq3ic4R77r-Q23vV5-12n6AH9rOW3NNJNKRnGruzFD-uROQ0TO3oQYfqO3N0EpdkZa5OwFOuP5hxz6DSQ0WAzYQUKA6dH5x7yjr8GpFrfsXkjqGzfJIbdO9Xa89hTn1rizLaUr6apY7KX8VEZYFF3lBM7p23AjJ4JcrFys-zjPt7KayL0vYHX1vamSf065c42O_ALkXm1wTlTonzSBnyPkHypOUhmUPFtJ9HIl367uYOjW6HJMDBXVtQYwitspowIw2tYwzTvadkl-R71NYlimylWEj6xEXa9ouqblCAA_1u9NZxmzjNmU_xqmbbZRZJRHWkUk5aCymV9_MkFEkj4kTyD2LRZOfeSpEZxRA1TUhKmrW7g_AbO_-lZbcrA6IHqUbfzlOYwEwGURJnaZAU8KhVtp5KsxoL6LQawZTlNZv5vEpj5Zz8KXFQhsCdFZBgMC5LXGOYw5NLHkefZyAki1ou0OvF9_hQCn-eSHxaSv2EZ9pMlFeWOFGGhmQOoo3n_WyVJDUgueRW2q2uq9gHKNif8F4X5XcrcBEiyKfcAn3OiY5UHRqLn-VKW2BCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مصر به استرالیا توسط امام عاشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/97911" target="_blank">📅 21:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97910">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مصر اولی رو زددد</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/97910" target="_blank">📅 21:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97909">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/97909" target="_blank">📅 21:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97907">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGRJnivT6ZPouTYkEfdxUvtmMoPJm7SLblfAgFyjYbRRJwLGF7yF2WmHxCUK2hcx_9jxpPdUaj5vHR1vFblaNhlP4zcL0lFIcCcUolc-su2lVynfe5cN5wFUdAOQoItsCq-hJ4PXXEMi0BahZ15vSEVx4VcebAlhDlS9cb3PEvfOexcvFz8uRo4vGI8eXs6Bl-a_nH_6jWcU9mg8KkxXyRI4fQR6dKQ1ovd_efrask03h1nFnpXa_JQy0xg7mtyaOQDOTZgkjI8-cXxu1oG1c1ZTwR4QiqaGiWGnlzbH5toWY7VKJKDgeelAWprVKZuut6vCw-9jRp9h7TZlViN7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVnWL_K_pENGHqYk9_6AeatSrzLGh9zxAGRamvpla16mmXlz3unzC3JAHNsUEQAK2X-9PUVhhVbvZuitDxl6LZryfhXauVOBmh2q605S6SqIgjL4gD5e_bUG3lJ2oPtt0__V52cKP5OhA0Lm8Ah-F9ZhzWz9WfVFzrzy5IRJL9gg4oaMioy7Wm-0iSq8L9qHJWjgJKbnG5SR3c2TzbEYW-v9C4hyNTsdaH8kyeDAntYtI_1yG87405AXZbRZB_lsB7IxyaIWBzV6sJwuWKT9-w49X0sCeVpnjuFJ_0bNQqaVMl-1oDQSXTcG-xb7TGC06oVHbNzyigTE0HEerA_Jmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری - روزنامه "ذا صن" بریتانیایی:
به بازیکنان تیم ملی انگلیس اجازه داده شده تا از داروی "ویاگرا" برای کمک به مقابله با اثرات ارتفاع زیاد در شهر مکزیکو استفاده کنند. این دارو توسط آژانس جهانی مبارزه با دوپینگ ممنوع نشده است و به بهبود جریان خون در ریه‌ها کمک می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/97907" target="_blank">📅 21:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97906">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQE30nwc3RseaQrbzde1aXupSNbcygbjGgMmvcwe1GVDC6x3Pqj7wsI6y7hNQBTCCofMZIm6dvnWXLbf0e05BitsOpWVDnPpPFSteAhE0-S9D8IM0hnRVfoNT7nv6cVY_HgG7kpW5uwvU1UzMwzQL2U5rJvxCgG7Xk1bp3ZDYfuN17j8K12DdCzmmI5dknKMg7BiAi4kO887dIY9Jvhq0CTmroDA7Lhb5bNX_M7__7KK76gPouniUDgyhYUTdNEJCdkgGYEQv8opdtMy5AXjJfuYul9rPFO1NPUecBtkBP5DEB7ZtoMt0emZQXCdQ5spMUJCQp5zSk21O08NHgv1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇷
بازگشت رافینیا به تمرینات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97906" target="_blank">📅 20:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97905">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3dfc9e63.mp4?token=pH_eQ7-srJxAsl2bYwWfmfUbudYrNdb7dDF_C16IEckkaEQmiW39fox3ROI196ZRPTvGM2TDswILhf_qTIm13h5f__DghY-MMNBDlNI876ZQTORqi1erChexNiNpII2pF1HzNYyPY2WgCkkHfZsoveI_vYlj7lZdfQs8pH9thYybRLoOlxb1IslIupN6h-RT_STb8dgcci6tH3FxeHWZZ_3SVj9xNhkSdUNVmyMB6kFrH6j13F21FIRsh9UUsITbzlCsSBwpXx03cZjsdXT2RBVFUtUDZhNac1QVua64aHuZ6sITKU-TJMwIPgE8xKDS2tYpy8_OwBO9FimtGko_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3dfc9e63.mp4?token=pH_eQ7-srJxAsl2bYwWfmfUbudYrNdb7dDF_C16IEckkaEQmiW39fox3ROI196ZRPTvGM2TDswILhf_qTIm13h5f__DghY-MMNBDlNI876ZQTORqi1erChexNiNpII2pF1HzNYyPY2WgCkkHfZsoveI_vYlj7lZdfQs8pH9thYybRLoOlxb1IslIupN6h-RT_STb8dgcci6tH3FxeHWZZ_3SVj9xNhkSdUNVmyMB6kFrH6j13F21FIRsh9UUsITbzlCsSBwpXx03cZjsdXT2RBVFUtUDZhNac1QVua64aHuZ6sITKU-TJMwIPgE8xKDS2tYpy8_OwBO9FimtGko_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
تتوی " کایزن " اولیسه که راجبش گفته: «این موضوع از یک صحبت در زمین تمرین در کریستال پالاس شروع شد. یکی از مربیان درباره مفهوم کایزن صحبت می‌کرد. بعد از آن خودم درباره‌ اش تحقیق کردم. ایده‌ی بهتر شدن هر روز حتی به‌صورت کوچک تا زمانی که به سطح مشخصی برسی. من با این فلسفه ارتباط می‌گیرم.»
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97905" target="_blank">📅 20:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97904">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdDcjBvlqDdZ7fqT_VhluQKyFyeOnuuZmB2elxHEut-0h84lbcX-DCVh9uQQogOvobX3LfWlkqdRNbS_LdKYyaJgUmSTTkJ1Zq6xXub50jQMiBR2eJ59o4oBO9y3h-bRGKmMkfmjNJ3cPhNPSsGLkjmJurDp2q8-i8Bw1h5y2VP8VWz9zan_blyjHv05j7rUMrvQ9ZWinhb1Dp_dHRdSn9UnG066dfjibfGsb2pSCl2Bdw2aRSSnYmtOyM69KGaPw31S-agy8op2sp_auUzDyC2i3yB2jT01p1KKtOwXAv5vQxsaPBw8M5Ye5mT_KGT4HU5o2kxf3a7Sf7yx7lQDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇽
🏴󠁧󠁢󠁥󠁮󠁧󠁿
علیرضا فغانی داور بازی انگلیس و مکزیک در مرحله ⅛نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97904" target="_blank">📅 20:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97903">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOqKMac-LY1aSJlxQ3yWH5iKS3tR_QPdZllbysh5OhyPZq3YbpImsjk9vlck1VSeLyiMu-v6aKQWviAKFXNd5NhRVGi3tQjOeRfKILwhorg1LoNtZODUGE1-widwRtO9DQXcHFBtA4EAesropfke9ciaRAiHkxhokCDO9O8AjBMy65WyABvrhPBdv9MWOdZM_JSQrLiZ-qjJ_vP3iLktm800F9XrxLhB4s-8YX-rihN-WTSr8dCfn9QCLwvqZwdYsSYqQCBb-OsDZsdBzTKb9artOE3yyD6g5ouSn5_oNFS3eW0fMJGjH6ks7jrfd2NaAJB3HLDcjIkQP7IAaqzRHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#رسمیییییی؛ آنژ پوستکوغلو سرمربی سابق تاتنهام هدایت النصر عربستان را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97903" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97902">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-EqB2ud86gfw-3-abbxel5zjM6Y681ZrKMUXrUtkVuyGuOOeaTHqJ0isZawEsEQxUHuNV63ApwARVG96gpAeZc37pRsFys30BCZEHYAV7SPswC6LkFHIQROtOb3i53OiztNh74xM9dOcmfTytEteljeWvJ5yYkG_Rrc6X6PE5WASD8gSMVE5M526apl41dGYfsIBYoS9wr615qLAUl6q7G4r0fSiHuVIa7lTiaP8HpR_TJbL8I21GOCS5DhsNvi6XKBOl8RgjhHHo4G0aSQ1aDfTQ2PsVpsy5baSQP5yV0Vo0iCJgzCJThV6qCq11MyD_b5yTb6ebwdfPWoVJ_Ypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها افتخار الجزایر تو جام‌جهانی حذف تیم قلعه نویی و حضور ویژه ایشون بوده.
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97902" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97900">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCsTzhBqcek5zqvjwPytxYoTS227ONOF1vphuMwwGeTz-49-o86QdvzpANrlmzGrHhI89-Lti76O4PDjVKoUQzPL31oNh8reB_YqUkZppTz31KkW77MmstziUIdRiwR9KEu-Vs4jsnyUplwVkci54jJkCOMRZn-eTELM2bX-yfvDdiJy9gVQJLuY43TcYyr3RHoBq0mvV8YAhKtuUDK_mQRgTtg1YMtrYsLU9vRRXkRHcs6YrQ5cftZflknivGZG6ANl4lvSIwLXmaPdBLWT9K6I0LvbEdIylea7FrTWOTnINRFFANZESvZC_OpEswf7WcmWo7h7F6AkgaIBRCMpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtzOhTnmBvhv9KpVxm38lSALIpZcB89nDCcDkqRMfNEM0Osu2_RTkYjqLfULxGaACYXh4iTh_FZ_GqgiSbEMc5NNunpOHl526Fx1EvBtgYMcVMEodebmGAnDpSxGAQzJNMP6lGwXFqrWLYAMUMoGeDH_fDTv3Wys47qvaVsSUDVrZOBjSvCc6_3a1zGm7sR2Yoo66xdYJnmhG8ilPdd50aNr6ffouv91Ph6tHYo3JQKQkG_IGsFg70SUWtm9EqcQ-LgJk0xV40V7pWuSbA_DAPTg0oMzpiYpRt7Npr4LUrHQ7vo6DYVJF8xlDlpvdLyJQmlc-T18EQOaLXsuNvW6kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
🇦🇺
ترکیب رسمی مصر
⚽️
استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97900" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97899">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97899" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97898">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gqR-rQ4Td6345M9ZA3ld7EuC4v6NH7tCdgs8xnCFq4w0ygNr63MwzpQoQb5DrmvFyiZcd49QCZh73QNLWJDCCoHyjRI5e9WS4eHBx26Fo9L3wgKut07umX32tTgh6zAdBec2rWLZuC-Ai0bRa2ptiGJ_2NqXfQPSQYOtsy8_tNJD--yudjaCF6Plp3o16IaiQx03234JOeRZIR8pAZk_ol3W-i_kT4mlEV8EB1Iz6_7QkC7sZ4W-UKC56J191j0kot6ib4KlxcWEIXDmJACqHYo-uah99qcouOhLr0NUEggOq_NS1u-GvqX1lYZbxu7DNqAg7lBVmyuDouZ1UQbw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97898" target="_blank">📅 20:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97897">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ2jqOOpepdZlir7xiKge0ecUA1mIt1goWFR4L_So22RKfLdBPt6X1xvpQx2JbtYOrW8nDXWBVw5n_3eOp7-7y9qUNVf2d8Qc1AvgJ639PQTncWsmeu5kbtG6W0ylCLWRggmWmInnSrM6JC2BLaJ7ocrAE6V2WaTFfNlcHjUzjo_AtidOOcmBpv7h0KF6LoFelg6gsYc9pJSiNVtTWFBSGf4KAAsyUdHFxaHGGGVxCS3EYwGbupVaEwGFBCGUZJdSxlO3KgPt5dDnOW1Y-jI4IR0P85A4dwTPEHHRFChDJ9AbQWTUoFRd3m8_aEODauccITV89gO9CaDeTVH9tBuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#رسمیییییی
؛ آنژ پوستکوغلو سرمربی سابق تاتنهام هدایت النصر عربستان را برعهده گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97897" target="_blank">📅 20:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97896">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUvO39HpiYU5mZMKeYBPJ0_1gj2nGFhxAXjOZMZoTOuKY_HMqToKdPSbrn-MOHw2j1-ZysMHDeUcgcEDLIpIuRP1WAaQrHcB6cCnACMEIa4R7opQk4WSSfIUFSAm3j1vaa7aaPl0-Zd_YPemJEeAx6HA0raOq6Q3lno6MF1tbCtVLxPvpujPa1SwkcSEolToOlWtWm5hEXBZhyq7sc8aBBqkhU3m0s3gR6fdivsOrRyMh-xcDZ4h6XR8hdn67KDoE_UYMLGxBUifJ8JAPavNeOmCW5VVPetb4C4H8_S5lmjUgn7jwSB5831p5gSw_F1VaNWX3hqIEVNvcn6dyLn7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با انتقال تونالی به تاتنهام، نیوکاسل که ۱۷۵ میلیون پوند حدوداً برای این سه بازیکن خرج کرده بود موفق شد حدود ۳۰۰ میلیون پوند بفروشتشون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97896" target="_blank">📅 19:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97895">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOYko7SWrRejLrBMVoAWllfyzisjbOoJOZmx5HpPSZyFLKpBkgtwQWYUyiMBtAtlT0PJeF2pJ0iTpYI_K6GrRl_RUBWrYYj8Bm50lJwKD4cTSLQSqCNLWweEUxhw_fyFvDQbnFKjsog0O1Pe2HKcoqU03XauBtYZWDymvyiiKoAf9HnHqAHt3SYtHRjOlFs17-q4uAw7fMRQPpLiRLqWHcWkomwSRvu1OrL9es2l-1g1QoiIzOPM1JBfddAKhGMhtDFxQEf86v0N0OHMILsMGSs74P4hiqkKulBoFofahB3H4zUud2RfnJFGHFZMLMDxvmcbJq_X2xV7oscva8_R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از بن‌جیکوبز:
یورگن کلوپ تمایلشو به مربیگری تیم ملی آلمان اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97895" target="_blank">📅 19:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97894">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61eb94b3b4.mp4?token=bM3_AUZqb9oJLiVoHUT-7HqV9ggMZslf7MA8_PbXPb7b5bpJ24A83vom26u8mBi7540DmNMTz_YmRdaHpuVVaMYWCJIZlcCy3GfLoBiIIVSDg1zm3iXGEodPy8PV81sdchn2WWPH6yn6W0RImpVj-XEmPiskR46AraPCpmuaMyZTKFDzMvO9zrqegqIswh1Z9VSWxBqF6ms7jN9kckiGHgHZICaJgatw_Lf8OH1w1yxexSUjmIUHPO36NKHGsfdlSraMz6i1yHPE88rPc9kCqjLytDLOdaVi1NfyoVW0-24dhbN-k-l9SyVvvO8BDr5h-KH2ogDUNlsB3yYqgCQhfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61eb94b3b4.mp4?token=bM3_AUZqb9oJLiVoHUT-7HqV9ggMZslf7MA8_PbXPb7b5bpJ24A83vom26u8mBi7540DmNMTz_YmRdaHpuVVaMYWCJIZlcCy3GfLoBiIIVSDg1zm3iXGEodPy8PV81sdchn2WWPH6yn6W0RImpVj-XEmPiskR46AraPCpmuaMyZTKFDzMvO9zrqegqIswh1Z9VSWxBqF6ms7jN9kckiGHgHZICaJgatw_Lf8OH1w1yxexSUjmIUHPO36NKHGsfdlSraMz6i1yHPE88rPc9kCqjLytDLOdaVi1NfyoVW0-24dhbN-k-l9SyVvvO8BDr5h-KH2ogDUNlsB3yYqgCQhfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند تو ملیت های مختلف
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97894" target="_blank">📅 19:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97893">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbf79b99b.mp4?token=q9Ar2rpY6cM6nIAEDrIzpizsNk87rw1o17D1sxb-bRvRHOZras82RrGn2SgCmglQXOYkLGyNLqF-MGLzIUJo8f7b0b2BfpPnUAW8HqqycxFTcljFAKwqQX45npBVaULMxMxbCYNVM3iQ0f2p69HSv4Nx0c_uY2UpTfdNn4u9VxNhUFcQAu6bUJPp4gxMj42QF-Zh5Ozy61ycsJMCLg-u3RUAN7GvME9TGJDWDOnQDKFCBQeC2rZ9krvQnK4-YJLLN3bECXuY8Xbur03ntdafjTxaN4NHC3pQLj8ADTHnVPtsvh-tpXFcJ3-r65Lnh9Vn2lChVsu2H6s96hb3N_jV1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbf79b99b.mp4?token=q9Ar2rpY6cM6nIAEDrIzpizsNk87rw1o17D1sxb-bRvRHOZras82RrGn2SgCmglQXOYkLGyNLqF-MGLzIUJo8f7b0b2BfpPnUAW8HqqycxFTcljFAKwqQX45npBVaULMxMxbCYNVM3iQ0f2p69HSv4Nx0c_uY2UpTfdNn4u9VxNhUFcQAu6bUJPp4gxMj42QF-Zh5Ozy61ycsJMCLg-u3RUAN7GvME9TGJDWDOnQDKFCBQeC2rZ9krvQnK4-YJLLN3bECXuY8Xbur03ntdafjTxaN4NHC3pQLj8ADTHnVPtsvh-tpXFcJ3-r65Lnh9Vn2lChVsu2H6s96hb3N_jV1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیای نصف شب جام‌جهانی هم دردسری شده
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97893" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97891">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">😏
😏
😏
انتظاری که مردم از بازی امشب آرژانتین و کیپ ورد دارن بعد پیش‌بینی جادوگر غنایی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97891" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97890">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5205517f12.mp4?token=aZT2OpatCPYTNas4h9fa5-vizrJv95NMo3t39LB6ozYvrqlmMWxp6c-cZCOkyFLOR3-AsjQ4ocY1K1HQ7g4rcceLLpgFsyxd0xwOH8jLjUWP0BamYenaLYjLKm63LNpA-mTtdisPreTISkGBPXEJfHBlTPfiV_WFVp7NKpy8RlZ76D4NoPFG0eQJmwE3wz2XPFk2RA5MD5q6A50mCTZiwlsPUUsOAvf9YhnLNjmjqIZSyX63Orv7w2rbTbOhukJ2e2dJJQAMEBvVPwM0RVenvZiiSqf8wu-lzev2LcABR6tIiS2oG4bZVMdxADCmmkdZoZ41xQwTuQtdEmDnsJRniw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5205517f12.mp4?token=aZT2OpatCPYTNas4h9fa5-vizrJv95NMo3t39LB6ozYvrqlmMWxp6c-cZCOkyFLOR3-AsjQ4ocY1K1HQ7g4rcceLLpgFsyxd0xwOH8jLjUWP0BamYenaLYjLKm63LNpA-mTtdisPreTISkGBPXEJfHBlTPfiV_WFVp7NKpy8RlZ76D4NoPFG0eQJmwE3wz2XPFk2RA5MD5q6A50mCTZiwlsPUUsOAvf9YhnLNjmjqIZSyX63Orv7w2rbTbOhukJ2e2dJJQAMEBvVPwM0RVenvZiiSqf8wu-lzev2LcABR6tIiS2oG4bZVMdxADCmmkdZoZ41xQwTuQtdEmDnsJRniw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
اتفاقات امشب بازی آرژانتین
🆚
کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97890" target="_blank">📅 18:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97889">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwrAN8EhZbtjHFRD51mbtTw1z4RB4D-W4JmVqPvUtNgQzB9kT8lzkaD3MerS6h5IZlpWO77RzfBNvDvC-hXCU4CB3TYm9Ogg4Enug1O0J9KW5tT09zIbAn4KpUrYQd6OYhhqKrr9K1ks0R6-966oF3-DdbXSY8BQ5Td9cJdS7fm9jgtDypZweHoLSrfeQf2mhBCnoDzzZQV8lNclNrOC8v36m8hCs3ZzDWrb0vkokr5ahWRbzPfg1k0lYBDdEyhHO4YExtI_qn4gBBd7AD-CAPjyVrAMZbI1XnZL1sUWPHaVkOEGTc4moscMgBl8o9k4LIEylKfZZUKSw4AS6cphiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#رسمیییییی
؛ ناتان آکه مدافع هلندی تیم فوتبال منچسترسیتی به فنرباغچه ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97889" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97888">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94c7d6c007.mp4?token=C7JHqVfrhNFCuXrtjdcayDYt6qh_EPXgPQteZIbYoPZgKuYVGbvFgcMdWtkKCLfvP8OcM3ultpS0eStVIbXuc_N0m2PqaWMpHyC_dd92cwfdQ2BNnQDLFowSjL-dGzMsUxgbN6--zLj_H7huIlj0-rekfqtXo7oUGE7S4YicXKHo-AfNYEbKblb44PbKaLgjPfAkZluSGO5iSOZNpFF4NiiMhhD5Zsie83Dc1xFTQgpz01hxcyMBYSnNm2t8w3KsBy_AuQ4GfF_-TXF0j8vNM_mueWuAg3K1My50ttgH3hLQXla27UxlARrKRfsGz-LVIDttUWTbYM1eyVoXWDgqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94c7d6c007.mp4?token=C7JHqVfrhNFCuXrtjdcayDYt6qh_EPXgPQteZIbYoPZgKuYVGbvFgcMdWtkKCLfvP8OcM3ultpS0eStVIbXuc_N0m2PqaWMpHyC_dd92cwfdQ2BNnQDLFowSjL-dGzMsUxgbN6--zLj_H7huIlj0-rekfqtXo7oUGE7S4YicXKHo-AfNYEbKblb44PbKaLgjPfAkZluSGO5iSOZNpFF4NiiMhhD5Zsie83Dc1xFTQgpz01hxcyMBYSnNm2t8w3KsBy_AuQ4GfF_-TXF0j8vNM_mueWuAg3K1My50ttgH3hLQXla27UxlARrKRfsGz-LVIDttUWTbYM1eyVoXWDgqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
پست صفحه رونالدو از جمعیت فوق‌العاده مردم کانادا بعد از بازی و برد مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97888" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97887">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGkf5BHYXHVAsuF2YaoQDkklEy0A1z-1yVzcebWiOVXQZraxAMKOFDcs53_ZWe-MmHrqMGhPdRfl82AMx39hT-0Dr3q2QX5J7dyd21LSPKtZO8zDaLb5tetw29DWO4ECcXRgNz6Y4ONGdHocu7aDRPrRuu4wiqALT6J46F0mIpaAFQ-NzKh1SZaZywNjUtJs5vZdK4Q62Kl4Wzmi3BKeNEyanl-X4yrP-R27QKehrcsbyG3cie_TsOFlkuaHWNOl5vi9iSETV2lRVr4CK1r0H8F0aOjuJta4ZIUVB9BQCkArnJ1_1AC4zXaeLKUYkUqzh8Sjenp0_m-BHhpFzKHGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
اسطوره مسی در اولین بازی حذفی از هر دوره از مسابقات جام جهانی:
🇲🇽
‏2006 | به عنوان بازیکن جایگزین در برابر مکزیک بازی کرد و هیچ تاثیری نداشت
❌
🇲🇽
‏2010 | به عنوان بازیکن اصلی در برابر مکزیک بازی کرد و یک گل ساخت
✅
🇨🇭
‏2014 | به عنوان بازیکن اصلی در برابر سوئیس بازی کرد و یک گل ساخت
✅
🇫🇷
‏2018 | به عنوان بازیکن اصلی در برابر فرانسه بازی کرد و دو گل ساخت
✅
🇦🇺
‏2022 | به عنوان بازیکن اصلی در برابر استرالیا بازی کرد و یک گل زد
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97887" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97885">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHHmJaFh_i6k-tkhlSi8Eojla8mc4oVGfynfT2Duth5B8E5zh8BJ-JT90k_pLOTbDO5BBPb6h9xA_6FESFswtXqyBw2IofPykDcd_1rUxjuSyRCLhar0b7JExi63aXkz4N2eZuN2UokwORbRhrq_vR4ey461rX163Wg54Uu0jq818_XC7ch3oT5_D6q6QSPnxjkSoFlM231VuD23k3wlRhS6a5MLda3YNbarzgGGpKZSoC9nmkFhrXF8-fWsp1Mt6J7vejnZhewq65BdLRAn_UoHSzdqnU8pd1aBtWBdxyaQF24RfXZ1SaiSXJ2kqj_QNlKp2Zt8_7pNJ2bgpK2aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPy9EEB_3AQunj1TvUapQrFi9oN_sbOyJP0x9wosenA2Bm4fQGo_JVWHhJjdhov7J2qPbQpN6TZIXmffmwt160gSqj8HBLJKMeztAONtgQep09NXBwiFywN5brAW4F4UeE6beqdeaTNAh9hdnHa88TZB5zvKDlVflBrGsb1xPxs9W0T4CuJZ91dPXX2PF4weOK50uyxgQHwNpBoR0O3JzyhPl6j_rrSJ05AmtdtFqBCpFUjgK2jLcMmA1OposYR3KvzxTaxT5c2Zgo8D_BTpnQv8DvjbViInJESoXyHFGt0ExTbD0k2Ysu5pOklYFQor--ZdGD-Big7AekX50cfKxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🏆
#فکت
؛ تیم ملی کیپ ورد 22 موقعیت گلزنی ایجاد کرده است، که بیشتر از تیم ملی آرژانتین (19) در جام جهانی تا به امروز است.
🤯
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97885" target="_blank">📅 18:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97884">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT60MVy0P_JuTcY1S7Ze6oym-0fEvLfZT2BgBSyoo0ptlr5A2iLLJ03LpIN8XyC_aPXUI57hk275smysBRRG9RY15wzfX7YcjhBASfiKmThWP5cMgW0tyaWgJEgo9CLnkn2jPjwAV91zRksonFZ_E-W1hynUbFg6xFkeDCYB-701XmGhNKZUWjAKK5th-chI6mkdcLcqrh7_jnbXcduq-SScObpraBlUMpvfkhHEn6rgeZyUrdKmd7ztB2lsEM4095kRCHvH-vMJJDjqNEmQzVEvpoeSYSSK2spkcOIkUgntdSg1gBsN7xaMvpUYFI3btlnqMC9Ep-nZ-IAH6eZXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇦🇷
🏆
اسطوره مسی در بازی‌های مراحل حذفی مسابقات جام جهانی:
‏• 12 مسابقه (11 مسابقه به عنوان بازیکن اصلی)
👕
‏• 5 گل
⚽️
‏• 6 پاس گل
🅰️
‏• 11 مشارکت (گل و پاس گل)
⚽️
🅰️
‏مسی، به همراه امباپه و پله، از جمله بازیکنانی است که بیشترین مشارکت در گلزنی را در تاریخ بازی‌های حذفی جام جهانی داشته‌اند.
🐐
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97884" target="_blank">📅 17:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97883">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d6124f5f.mp4?token=bYJ5dE6HYZQFZTq14j6RTnQ3oOUYTJ3dv8oEiT23Nm923rHyLSEpxcfN_L4oGAYWT8lQj7j_oWiXQYw3mBPdj_R9SnLGj-b18LlNkq15BBNwa0mXPGLIUxuwS2HYIw_y_us8G2dcTGGKCbZRFDRbjNGIg-SBl47GTAmMANJ6vWk4q5Wlk-pBUxQOOjBVzfySnQgj0W7PRrVje2QoHwZGRnu6hRxIMKo-mpOITTBRWJMdVm7ZZnFs41KC4mLft5hK2f83vMXcYODTx19pM_C0oiN8jUPW8cs1xLuC7mLoAgXt1wvtJeu8kydW7LF9vumMA_CaAgN8oKAwpa88PUgUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d6124f5f.mp4?token=bYJ5dE6HYZQFZTq14j6RTnQ3oOUYTJ3dv8oEiT23Nm923rHyLSEpxcfN_L4oGAYWT8lQj7j_oWiXQYw3mBPdj_R9SnLGj-b18LlNkq15BBNwa0mXPGLIUxuwS2HYIw_y_us8G2dcTGGKCbZRFDRbjNGIg-SBl47GTAmMANJ6vWk4q5Wlk-pBUxQOOjBVzfySnQgj0W7PRrVje2QoHwZGRnu6hRxIMKo-mpOITTBRWJMdVm7ZZnFs41KC4mLft5hK2f83vMXcYODTx19pM_C0oiN8jUPW8cs1xLuC7mLoAgXt1wvtJeu8kydW7LF9vumMA_CaAgN8oKAwpa88PUgUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بفرست برا اون رفیق فوتبالیت
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97883" target="_blank">📅 17:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ1DOwVQ32FGpbtjsRY87XUBwNgX9bNCY8OqG6IwAF3vIfTJLf7HUR2ORyPFLuNah4L3WSUpG2dAmvodFnCzi0p4JztU5xw5-gizDScoOzpZabClX9m_J5GjQG0oXT16kpjLZpoMFLpsnv56glxJ97GrYNBPvvgEwpkkJbIkT2i5v7RJX3uaMlxcH-D7uTBs2KwgMoxUE2UlnC1y7sswECBqnJwF3efMKSJqRH-I2ZO0ls31m7_S5YwDyGO18UAG245wZjvEJ3ayjieR8xPVP9g4ggHkf76GNYrw8mQYw9VxY6KcEtT7Bt7CrSpqRF7vpPW0XOpkuuiWlGV3CXwWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
اسکای‌اسپورت: فدراسیون فوتبال آلمان درحال بررسی ارائه پیشنهاد به یورگن‌کلوپ برای جانشینی ناگلزمن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97882" target="_blank">📅 17:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtiNSnNPId3PXf7G9CVgcuZoKotImmKMB05LGV03hvDSq2ivaEFJNc6tYUSsPqoLUGC3D5OKvjKddfo86MZjG4RWmyEUx7P97zSrMm-HNihn4j8Z8iUOvNS5jFlvnJgN6LoR8Uvmv-jDjOWwB1iC-F5FvP7tgVRY3WfETfDukeU2SfhOl7AW3uAWzss-9n_nlDMhFoIvv2eTrQJxbZ6fZpv_S2W0wNjMN3OOPGyrh8ccPnJLLJluT-xnh4hQXsqTptdP_qgEIjxcpKnpPtOM9xE_iMQ_9I7RgWOgf2uYOqya7_G-UXA0s8C2vba5NsOitrruQZiZCLAYdUYpvj-giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاقی که برای داوران در جام‌جهانی دوره‌های بعد قراره برخ بده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/97881" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/497eedaf5a.mp4?token=ZWgZo_vKF9HrRM55B_dsYx7I_E8QQ5yCoNiTve9bdNVGg7gjEk68lbylzF7hU0aZlyZ2ghKDwBG5IfDLhIYMQP-SxvywdnzawYAD-rW3IQOSVD1ujfSBrtgqkYb_pv6O3VR1UQTvtXGd45W58lQ5l6vL9AShV81wkb0N7UjDxGkTqe5jR81SvGGF_20e26etFgVPu9sTLV0DdI799o05VO6syaT-Q4sxcNJWiQhtbpJvHcZt2M4lHi3D8gKVffnN-a06pRtTPnskYJHaH9EpoRl9wZARWG-3fNgUc9KMBRYVwW-D0VXlFWpbELkZf27MQQsn1CeBhZdBuxWRD_kVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/497eedaf5a.mp4?token=ZWgZo_vKF9HrRM55B_dsYx7I_E8QQ5yCoNiTve9bdNVGg7gjEk68lbylzF7hU0aZlyZ2ghKDwBG5IfDLhIYMQP-SxvywdnzawYAD-rW3IQOSVD1ujfSBrtgqkYb_pv6O3VR1UQTvtXGd45W58lQ5l6vL9AShV81wkb0N7UjDxGkTqe5jR81SvGGF_20e26etFgVPu9sTLV0DdI799o05VO6syaT-Q4sxcNJWiQhtbpJvHcZt2M4lHi3D8gKVffnN-a06pRtTPnskYJHaH9EpoRl9wZARWG-3fNgUc9KMBRYVwW-D0VXlFWpbELkZf27MQQsn1CeBhZdBuxWRD_kVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه سیاوش خیرابی راجب حضور در برزیل برای تماشای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97880" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlMn_M7XvP1dv6i3xQ_TxbisXuxYEuZBGB9b9GEE_nfaunsQQ_2g8onehSPtSuOkGPoPZskppu-XIaeP9HQL-fBgrvy3lxZXpdgTbR_HG849ItuwCbkjC9MQH91fOjz4dhi9OBy5bPN4wGIVfp5Cgr7wE_bmMCBH3HmdcnTg_Aasohk1JeAFEYixeRd0HEf389_g7ceWK3EgixU_yP3bVghdsu-HjNpDtIisQmX0WdUGX7DOnIQhkn9xE3ra7RhKWtLi4AGuVMjjjeRNdZPQdHNr12ZkRLn4SyUT1V-LqI9uKT4zq10zldMikI-lwbFwK3WPlgC19C4sq4mqbMYdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🏆
🇹🇳
#فوری
؛ فیفا پس انجام آزمایش از بازیکنان تیم تونس در‌ جام‌جهانی متوجه شده که ماده ممنوعه "کلنبوتیرول" در آزمایشات دیده شده اما این ماده بر اثر کیفیت پایین غذایی در مکزیک بوده نه مصرف مواد خاص! در نتیجه هیچ محرومیتی شامل فدراسیون فوتبال تونس و بازیکنان این کشور نخواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97879" target="_blank">📅 16:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx5Fc14wqqZ_KgFe25-mkJQth3Vhk2ee6f6SDrDQ0kZe9CQdXkA1GDHgwrv0h6Mz1owbGlLa2UCCZfiCOfFZUiSwJfZ3GdaXYUNmWASNOmRVY1kIuQ94w1b4v3IUF43gk-Byv2myTbfVGhzrAJ58e_wdrxAQ5FE88ARwwIvIVaikzOHcLkBuUWDeDZfVKSQx7fLcBaNMF-uMOILez6G-Q1K1Ja8SVwT0oX2Fi5jSEt3cq_gaHvm8ncWusqtC0Q4XSZVRs-ZqcuGP7J7_z60a7YKrBbX9ygGVLR8E5QTM3abMZbfMYgeKf58tcRXNQf0diS2VF70-yfHS618sXbEFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سپهر حیدری اعلام کرد از همسر پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97878" target="_blank">📅 16:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYdwXXkR8ZbeJyzdx8pmZ0oKDVapEa3cxavl2W-uNncQyTvU6zLQs1TmdWJjNVTaqOVkdTHMPvSBLbpjLYF1AhcwdVPKZnkqpC48vEZTMsjQuQLdxTYGwVhWsUDyYEy-B41mu2VXDN2bSXSv8np99CjmR_UOefStFnblWLS8vEn0OgFDOssG9WAQ8ej5WmGdVO1BKa6ocFzi4AYsYYln3GiXlH6dDBP8MHTf9EnNoIsFIHkfBcn_8cVFENMGsaeHuXQdMYVlC-M3hsLGlBJfXLEG_VlqkySSTVfObvrOFDJRBPP8Oubnmw1fl5OLnxw80yvBk6q8qtLHgvOd_xaUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارلمان انگلیس قصد داره به پاس درخشش و تقدیر از هری‌کین، لقب و نشان "سِر" رو به ستاره فوتبال کشورشون اعطا کنه
💥
سِر هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97877" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97876">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50819de74.mp4?token=IEK5oS1LJU_vk1Rm4fBe4D8BvlFC8A1A632zfx5Fx3Ih_MK4zEThQLTbFjuosSxqC5NmUebW5rUcDoXdeetDgVNk9AvshQweXknqee5EeiAlQeLZTieZ6c-eZ0SaXuehVi_5MkF8BoTcobLpppcipm3Zh4O9TI0ZIIsEvlPef5HhLUWR0Y5M5v9oh_AktbY26x_mceqBeulkeBhM_rCjTTxYj6uoMrEbPsUsME0949Gy1EjiaDUNLVZspoqpm5e0htLDzmtmbRarCiO8sBxIapAKZiP7X9xSXBn8kBVx50MbQD0ZK4e-pUsxR0ai6Vk1tWQS_lBmFNQiapUO8_pNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50819de74.mp4?token=IEK5oS1LJU_vk1Rm4fBe4D8BvlFC8A1A632zfx5Fx3Ih_MK4zEThQLTbFjuosSxqC5NmUebW5rUcDoXdeetDgVNk9AvshQweXknqee5EeiAlQeLZTieZ6c-eZ0SaXuehVi_5MkF8BoTcobLpppcipm3Zh4O9TI0ZIIsEvlPef5HhLUWR0Y5M5v9oh_AktbY26x_mceqBeulkeBhM_rCjTTxYj6uoMrEbPsUsME0949Gy1EjiaDUNLVZspoqpm5e0htLDzmtmbRarCiO8sBxIapAKZiP7X9xSXBn8kBVx50MbQD0ZK4e-pUsxR0ai6Vk1tWQS_lBmFNQiapUO8_pNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
خداداد عزیزی Core:⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97876" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97875">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgJaeMWUYce7-Ua6o1gUEGHSJ1fUxFlNBoKuJEGb2Q3I7jGhLTkWVANrmjG9uLO-R65ZdGImcj-MFgnDUGLjv6MCigfSgcufzHl7WRsUnt5itzHkVRRNtclIyKXyPaaxLmCMqFBDRlnAmjI5m-fvTF857RCebX5Y3lUZWGESl2_l3F2CkQYA119rOERfYxKlRJE3De2j65yHoN6obmv3rC_v8V_fwYuz4At-pQtY_fhq9MMM0k7i1ewQQxMKhuFbob0FxEe8kCCEhsk-vm6FoxcVthMv2lHFW1045ExjmObvoAfWKFrHuDa2cw_a6bGPWsys0lNmhxWq83IpDqLtMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
⚪️
فوری از ماریو کورتیگانا:
انزو فرناندز و رودری از لیست اهداف رئال مادرید کنار گذاشته شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97875" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97874" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97873">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97873" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97872">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b016be396.mp4?token=snil3OWwK8u3ZXneLCnGTG6z-qGBhaQ5wDnoaHWEUt1sJGwhZvuL5Ay-CXYsxjSnDeuqVFRP-_P9fm3Nhzi7Ic6GW48ylOdvus3BYqjN7k_LJz6iTkdgLti2SgZKJJt_UzXrndod9NStKk-htz3V2Ghqhb8jCFjs36n7wcs6L0fT1XoOjaiiXBjMV_YBnvnBNroZAvW1TLj0cI7SCy9AR-DjdTFOEfc8tj-gT-hIVlDKyhgsM3Mfru8eM2Bw3F92kLzXJ62Nf_bARg4gVhli3rUavMonLTIl4ACi7cuHEIrQFl10Qu_18mnuK43C8YiOfeRNUHa5g31LewtM8NqCtZemHL1FovJj7654Qcs3o-PkiL60C4ubWZyrPOi_pOeHbHOW-ngJfPXEcLsy91hWyWKTDUvfFTYnkgwbFm8BtdUD6TMhw-Xk6SZTL0wTvq9aK85CxRoUspW44lPQ7r7tPefLxh4XpAETaecPV2s9jM-uu8VcWQcOgCFUVOPDRRBfiVD8l42I2t0ua7nkAOpl_PB2FRc4ZVRLzFocIfFGAI_WVMq0FfpX64Ylc0YR4jGlgzWGbvFAX8pPlkzP6Ieh8joHMZ8nAK3kr6sv2nVwqliIIO1Iid2egnJqmiwKxySWqvNErSY3r1oHWydbrRHMpErO0JmgpiPpXAXjbiCxOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b016be396.mp4?token=snil3OWwK8u3ZXneLCnGTG6z-qGBhaQ5wDnoaHWEUt1sJGwhZvuL5Ay-CXYsxjSnDeuqVFRP-_P9fm3Nhzi7Ic6GW48ylOdvus3BYqjN7k_LJz6iTkdgLti2SgZKJJt_UzXrndod9NStKk-htz3V2Ghqhb8jCFjs36n7wcs6L0fT1XoOjaiiXBjMV_YBnvnBNroZAvW1TLj0cI7SCy9AR-DjdTFOEfc8tj-gT-hIVlDKyhgsM3Mfru8eM2Bw3F92kLzXJ62Nf_bARg4gVhli3rUavMonLTIl4ACi7cuHEIrQFl10Qu_18mnuK43C8YiOfeRNUHa5g31LewtM8NqCtZemHL1FovJj7654Qcs3o-PkiL60C4ubWZyrPOi_pOeHbHOW-ngJfPXEcLsy91hWyWKTDUvfFTYnkgwbFm8BtdUD6TMhw-Xk6SZTL0wTvq9aK85CxRoUspW44lPQ7r7tPefLxh4XpAETaecPV2s9jM-uu8VcWQcOgCFUVOPDRRBfiVD8l42I2t0ua7nkAOpl_PB2FRc4ZVRLzFocIfFGAI_WVMq0FfpX64Ylc0YR4jGlgzWGbvFAX8pPlkzP6Ieh8joHMZ8nAK3kr6sv2nVwqliIIO1Iid2egnJqmiwKxySWqvNErSY3r1oHWydbrRHMpErO0JmgpiPpXAXjbiCxOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
پشمامممم ریخت چجوری این جیمی‌جامپ بازی پرتغال بین اینهمه مامور از رو سکو پرید وسط زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97872" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374849cbee.mp4?token=nT4nYOvuQoYhznqDxaUhPgzQJKD-J777D3Hs1V-mek1HJnrdwI8oX7NYtP7N39Z1SWayeeyCu-sIY6hVQ9hke0QYyzGao7vGtvIWpjO6KtIPNiR7CQaW8Ewb_lm3sZQo159KCUyc1c9IJXmOltPcKxG1hNw8uJHQDeDJMXZbMXpbt2_mStUgXEGKuW6ZhM9ZKN6EEpKnwZUw12WhRGbuIv6qtN61pXK0vEBjlVxAGA6-sz-XYaiIbN5TomJ9sa4WaNpw_pxwMrggpdGj98wI8Mp6yrvDvlCDBXP4MK9uP_ZiIcdZBw8sRrgLq3Qc3wtNMByF4cPY3-QWiU7IucyNSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374849cbee.mp4?token=nT4nYOvuQoYhznqDxaUhPgzQJKD-J777D3Hs1V-mek1HJnrdwI8oX7NYtP7N39Z1SWayeeyCu-sIY6hVQ9hke0QYyzGao7vGtvIWpjO6KtIPNiR7CQaW8Ewb_lm3sZQo159KCUyc1c9IJXmOltPcKxG1hNw8uJHQDeDJMXZbMXpbt2_mStUgXEGKuW6ZhM9ZKN6EEpKnwZUw12WhRGbuIv6qtN61pXK0vEBjlVxAGA6-sz-XYaiIbN5TomJ9sa4WaNpw_pxwMrggpdGj98wI8Mp6yrvDvlCDBXP4MK9uP_ZiIcdZBw8sRrgLq3Qc3wtNMByF4cPY3-QWiU7IucyNSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
چرا فوتبال شبیه به زندگیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97871" target="_blank">📅 16:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b751ec19e0.mp4?token=Y8EXUDoqPq1SY6qrkCQKWRvTLyleRGtpml_wSAbeUm0fEtcEyfGhK5Eivn1TqpA1Q7P8iWhuucOEtnM3iX9Xtlz5JtkxnwTnW5jLIZ4vD_rMU-FavUYbzPKWeu2J7EVVP2rRC2xXt7dcvAXOpzYZDEvjEpHpw1uuWv1RDPoN2VuRN3Gp2FVbrOQi8vDQglbaXcHnMSbl_kJDzf_84i6vwPrAxrHtnfFhrd3t0uc-hIUZy1pGI2TEKu9O3IOGIPrK8G6e94AZakWCO-4EsgYAQaSXoU4AXhAhZNp7nwZGkG9P3J7RuuGpo_2m8nyskRjQkA7ACNMvUZv08Dj5LzWSvYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b751ec19e0.mp4?token=Y8EXUDoqPq1SY6qrkCQKWRvTLyleRGtpml_wSAbeUm0fEtcEyfGhK5Eivn1TqpA1Q7P8iWhuucOEtnM3iX9Xtlz5JtkxnwTnW5jLIZ4vD_rMU-FavUYbzPKWeu2J7EVVP2rRC2xXt7dcvAXOpzYZDEvjEpHpw1uuWv1RDPoN2VuRN3Gp2FVbrOQi8vDQglbaXcHnMSbl_kJDzf_84i6vwPrAxrHtnfFhrd3t0uc-hIUZy1pGI2TEKu9O3IOGIPrK8G6e94AZakWCO-4EsgYAQaSXoU4AXhAhZNp7nwZGkG9P3J7RuuGpo_2m8nyskRjQkA7ACNMvUZv08Dj5LzWSvYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
وقتی رامین رضاییان، تصمیم گرفت بدون کم‌وکاست به تک‌تک آرزوهای پدر برای خودش جامه عمل بپوشاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97870" target="_blank">📅 15:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97869">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e7bb3043.mp4?token=ezeG4UIMQ28SpifNh4HTMEUHlwFAQVjsdzw9lBHbbq3Haq1adclxbk8iKVf7eidmp6N4ZyBUa4bSHIKw9ROXXgoECvKTJBz0wTI4jZE2Zio1M8HfYlrB_9wJlFYOW4NBajpMElXAaPJWdH1ytFOSzT1o5dmiEPIVhGMXxnMrLLqGDgAdHEEqIkQ7oJK4O6QmhOPtj81ibcA7Be13HNIuB1qt20Nc2oB-xzpA0tJP8JejwX8iK8cOANDEUN0kqtEWmxgxOU7CpWlSMG8FEghphwxL_aZC1NDhy7Fc_WS_jH6TCMomKK1yBSKZ4aSNDRVWkpUiGkQbQj-3OC3-8Y6dGnX5RiAHdSTQlqLDItbP5nrBmsa6TZlXmdDF47sdFt5MLgvTvQq0NQYAN_vzOyFAv5RSQzxKU3pKodhTKklpdGZRhepKCqgM380hbgNiyH5fkKvse8OTgU0W4fAMzSIl0hQYKijt-jn7QnbvGgPZ-mO-bgZPihD_R_oJDXCBs0er2RVq5tVvugNhrNZH3DwJxFoNtgZigjoyqRUsJR-rWnpIHujkoiEgFvNvhi9weyOB655O4axKNrM7FLedYABGFca7dDo8YmjFfi1bqqxCJd6gDL3LqHTGNLTojs2TlldpZfCLrnyYc5RQ1QI2aapgrqAGQZa3TpzIo0fK9xTT4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e7bb3043.mp4?token=ezeG4UIMQ28SpifNh4HTMEUHlwFAQVjsdzw9lBHbbq3Haq1adclxbk8iKVf7eidmp6N4ZyBUa4bSHIKw9ROXXgoECvKTJBz0wTI4jZE2Zio1M8HfYlrB_9wJlFYOW4NBajpMElXAaPJWdH1ytFOSzT1o5dmiEPIVhGMXxnMrLLqGDgAdHEEqIkQ7oJK4O6QmhOPtj81ibcA7Be13HNIuB1qt20Nc2oB-xzpA0tJP8JejwX8iK8cOANDEUN0kqtEWmxgxOU7CpWlSMG8FEghphwxL_aZC1NDhy7Fc_WS_jH6TCMomKK1yBSKZ4aSNDRVWkpUiGkQbQj-3OC3-8Y6dGnX5RiAHdSTQlqLDItbP5nrBmsa6TZlXmdDF47sdFt5MLgvTvQq0NQYAN_vzOyFAv5RSQzxKU3pKodhTKklpdGZRhepKCqgM380hbgNiyH5fkKvse8OTgU0W4fAMzSIl0hQYKijt-jn7QnbvGgPZ-mO-bgZPihD_R_oJDXCBs0er2RVq5tVvugNhrNZH3DwJxFoNtgZigjoyqRUsJR-rWnpIHujkoiEgFvNvhi9weyOB655O4axKNrM7FLedYABGFca7dDo8YmjFfi1bqqxCJd6gDL3LqHTGNLTojs2TlldpZfCLrnyYc5RQ1QI2aapgrqAGQZa3TpzIo0fK9xTT4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کنایه‌های تند عادل فردوسی‌پور به قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97869" target="_blank">📅 15:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3bZrQ58sMkamQVJNPkDPWjdGKRS3Ubsm0XRPq9n9-TRfpEW23YcmZIprBsvwfKTlwXrrGg3WzEmpWGZQbSSRlQg1rbJ_euFVgxf4KzYmg_tm6ulM-gPI2Org2L6i7rSpobfKdNlesJMPnwCH3_mHdkxX1qtYiauqpRLd8_RcO2mVoocKu2WgIdRqvyTlS__G6o-mzjq55A1d_RrI6GE5nySFAqia5H5LBs_YPxQcblkVYcThD783MJVpvsybzLvTQygOxRPYGtu3lJxHq6UUVzku7E2SdsJkOkfaZkyS2eTjeNv0nfEpSv94k0IQkSkE-UL6i4W0cTn_PNSqi6yNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3eb4669c8.mp4?token=HK-oGPn3KoDISMkhwWq7HbhYyFjeq5T-KP_Z2QhOh9VVmZSJR3lCatH5L8w53XWVm95mvx0Zm1k1m_5LFvY9FCAnvQzyLJN7SF1wS8cvXxvijrxMU-SezrAlU2IwlxtZvwihHs7Fc0XOG8UrKvr37NGL_dWu4dpT7y10IT5wyYiT8v0vyY7rRzkXsU14jwOHgDCFFhBfDmZL7iG8vANzUPjyUvNUyuq6KDu4L3sI-lmbhh7-vR2GnNK_jfHHP8Sv0PgFlChEjqh4SNcaznYMV-TrfjfrGFh-aNXfc3Jq_2lnzrf-DVwsfofFt81x0vf2ikBSqlAplW2bUTfN_hjLYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3eb4669c8.mp4?token=HK-oGPn3KoDISMkhwWq7HbhYyFjeq5T-KP_Z2QhOh9VVmZSJR3lCatH5L8w53XWVm95mvx0Zm1k1m_5LFvY9FCAnvQzyLJN7SF1wS8cvXxvijrxMU-SezrAlU2IwlxtZvwihHs7Fc0XOG8UrKvr37NGL_dWu4dpT7y10IT5wyYiT8v0vyY7rRzkXsU14jwOHgDCFFhBfDmZL7iG8vANzUPjyUvNUyuq6KDu4L3sI-lmbhh7-vR2GnNK_jfHHP8Sv0PgFlChEjqh4SNcaznYMV-TrfjfrGFh-aNXfc3Jq_2lnzrf-DVwsfofFt81x0vf2ikBSqlAplW2bUTfN_hjLYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هالند تو اینستاگرام این کلیپو لایک کرده و برای وینیسیوس کامنت گذاشته:
🇳🇴
هالند: وینی باید این صحنه رو بازسازی کنیم.
🇧🇷
وینیسیوس: خخخخخخخخخ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97867" target="_blank">📅 15:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDtBFCDOAxYO3C9bbAjujrgIk5JxRJthr3BZaIsNPIIX4lU18mfqDcGiRyZVA0qUBDBghwUT4Y0CoHcUHRjUhHM13xN26jkcWwrc0VtT64-bu1LEsI4sBwHnnZvm9MNPbtiKx5S7Q7i90ofZltfYTTyihA2mPdkczrcCoAYHOqeNIyeupVdKAQvkTcL0-9ighY7vBVfJdvRMTFyCoh9IbINllNOHcxYXzFTfsI6wFe4jyiujiw9Dra4hYQOss7bI6_WLyvtjMJroKi6hFwsRNOLJg1oHtfN_QJBnRmcYoEqrucnuswBNWVh9VL5EZ6dUnLXr18h2VAl6RuWQYbFigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کل افتخارات روبرتو مارتینز:
صعود به لیگ برتر انگلیس با سوانزی سیتی
قهرمانی جام حذفی انگلیس با ویگان اتلتیک
سرمربی اورتون با صفر جام
و کسب مقام سومی جام جهانی با بلژیکی که ولش میکردی اونسال خودش قهرمان میشد.
تاکتیک که نداره، ذهنیت برنده که نداره، تفکری ام نداره و الکی فقط تعویض میکنه.
نه سبک خاصی داره نه فوتبال قشنگی ارائه میده.
کرواسی با چندتا پیرمرد برات مشکل ساز شد
جلوی اسپانیا میخوای چیکار کنی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97866" target="_blank">📅 15:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خب دیگه بالاخره از بالا دستور رسید امیر قلعه‌نویی و مهدی تاج برکنار بشن
🤡
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97865" target="_blank">📅 15:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d611a1c585.mp4?token=Ww4VPS6AdSU5uWaT4Q4Z-X3CKEeJ9dWs7Vi5oS2YzYRjyySmXomSyCr2U9mlc0-xnvkrddYfe-Heh88G8O9S9IlzDgdfxeM8NlCtZexpBqhzGZ_ymlLpmqibiw8yQC0XXUBSwoHLXiNbtFN5sr4pBbLErUkrS16vxPfAkBNjWXTf9qohi93Ea8xJfumGwAjg08126PcQWk0CMAFBUvufe9ZG60G4d8wO3N0UbrmKgZiDzY5vaL58aI5NZMwwNo01YJuTjMZjr4Mf3ajT1LRB08kI_Hskmxv4QOaLoiJy0T2MZH30qKpcc5DIG_rJH4nt9qtGQ6yGejW2hg4BqFTtZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d611a1c585.mp4?token=Ww4VPS6AdSU5uWaT4Q4Z-X3CKEeJ9dWs7Vi5oS2YzYRjyySmXomSyCr2U9mlc0-xnvkrddYfe-Heh88G8O9S9IlzDgdfxeM8NlCtZexpBqhzGZ_ymlLpmqibiw8yQC0XXUBSwoHLXiNbtFN5sr4pBbLErUkrS16vxPfAkBNjWXTf9qohi93Ea8xJfumGwAjg08126PcQWk0CMAFBUvufe9ZG60G4d8wO3N0UbrmKgZiDzY5vaL58aI5NZMwwNo01YJuTjMZjr4Mf3ajT1LRB08kI_Hskmxv4QOaLoiJy0T2MZH30qKpcc5DIG_rJH4nt9qtGQ6yGejW2hg4BqFTtZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇭🇹
🇧🇷
Ronaldinho vs Haiti.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97864" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97863">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42e2e0f70.mp4?token=eBY-aoscHp0nbsjqD7g2tKduo8VqTW1ZOnBWXUJQNzJYiQL_e5Tw4Tusg5nXAOtwfupxp7zL3AqTWI4NI3nwgkslnUqZzkMpa9pAKimMlmZJRogrzUWFOvBPcigD-FBm7rj-Iyz_-vUWGLV2Ee7GOyb5D6w3swJO3k_psDRWEcjItcMZbvuy8LLeoLt5Wxw1zOPOikFHHvnxJhbtG5Sglx7CwqUCnCIY5XUsvu7Nfi7wlVs3P7ddafhR5q4URuG386FoEYOCO8fVYheFvoZ977AHveRpBHWYeeLzR3HLpOaUl7XRjlV4a8FjQNKs8qwBXpeKfeULUAVgyvLm51Eahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42e2e0f70.mp4?token=eBY-aoscHp0nbsjqD7g2tKduo8VqTW1ZOnBWXUJQNzJYiQL_e5Tw4Tusg5nXAOtwfupxp7zL3AqTWI4NI3nwgkslnUqZzkMpa9pAKimMlmZJRogrzUWFOvBPcigD-FBm7rj-Iyz_-vUWGLV2Ee7GOyb5D6w3swJO3k_psDRWEcjItcMZbvuy8LLeoLt5Wxw1zOPOikFHHvnxJhbtG5Sglx7CwqUCnCIY5XUsvu7Nfi7wlVs3P7ddafhR5q4URuG386FoEYOCO8fVYheFvoZ977AHveRpBHWYeeLzR3HLpOaUl7XRjlV4a8FjQNKs8qwBXpeKfeULUAVgyvLm51Eahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدل ارلینگ‌هالند رو داشته باشید. خیلی باحاله ناموسا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97863" target="_blank">📅 14:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97862">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f9d77bef.mp4?token=r4n_iYxUq17sZzTbVOTBl-z7ZhnHi6RAALEwZFSe8pxDfynoZbtHjkgHdKgzVzxgF8Zd0lKjYJjYXdtDkc1cc6dEnEt2Rcbzzg1urgMD0RJyUw5rRMI7nBz9qREr8suYTjeWsJB8VcBfqWrddecZiZzCFutZNJOUu2UTDQNF1dDG6UEKXD8L-gL-ldAEJKzK4jgBgyQlUe4ncGmQ2_QU5fLGGja3IWSBjXSxPSULWBUbjYNGUJcz5HLBJ5S1L9LZ6YsmlQmgSO_nV6QC16sesZDg_2BNqd8omvLohwKRol5yB650iC6DlJ8QUFgzEGIiuuJlGsDWFpLQi8viCFpgQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f9d77bef.mp4?token=r4n_iYxUq17sZzTbVOTBl-z7ZhnHi6RAALEwZFSe8pxDfynoZbtHjkgHdKgzVzxgF8Zd0lKjYJjYXdtDkc1cc6dEnEt2Rcbzzg1urgMD0RJyUw5rRMI7nBz9qREr8suYTjeWsJB8VcBfqWrddecZiZzCFutZNJOUu2UTDQNF1dDG6UEKXD8L-gL-ldAEJKzK4jgBgyQlUe4ncGmQ2_QU5fLGGja3IWSBjXSxPSULWBUbjYNGUJcz5HLBJ5S1L9LZ6YsmlQmgSO_nV6QC16sesZDg_2BNqd8omvLohwKRol5yB650iC6DlJ8QUFgzEGIiuuJlGsDWFpLQi8viCFpgQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به همین‌راحتی مدح و ستایش فیک برای امیر قلعه‌نویی و تیم‌منتخب ایران برملا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97862" target="_blank">📅 14:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad396b4fa.mp4?token=jQz3UJi9zu-1_X7ofwIpqes3xWRTEB2AydQFab6HqetFXgl5G3O-PgDxh2_YMQI7Iq7jas2JjPzbovmnsAjrgI-m_2CJ5KXZD7nE6L_8fA29eohtv-wtFim6LyJ38TrgjPoAu09sZWTniX6REwf3chfXw-xMCLdvjgm1KfzZ1Xxx_xf9ZK1KALSRb78_Bw-y8EJKtMd1z1qnlC_cRsojTnDQZVjOIP35bpKJgKqK5-4c2Xxns5l_phYgph7lMn--l6ibqWTOoXNdn0rlXGIj0H3jqVoIKLK8f31nJKsSX2tfv2VaGR5MDihZAyNU0agwM0AclTq8RlQRgEbVISJJSDnlZ6EAL0vjbXlSIysxtkU0ksVDFN8vARA9G_doSfDaOvGDzGYQ_s7GUEIf6pigVpZ4y1k8qrbNdLg7xSaMFayAbWoRlWqLDdVuTWWewIGYgTTw6Y-R8VV-HOyFc22Z18h6NjdR7YEvObleCopFNpqiq39RzT2Zp7QVEjEF9DZNRoxGOl_1dXG09oxF9DjDaQDzhpC80AP6Az8mgiYBSjbxvdDxH2-Su8ZbVv1uqPd_0DvT97mPSk9QMAgJUSBUCYPZtbvcodifxxvzA-TGF15q4ixLJ5DlaMo_AefXlevIOR4mf1i_XcsuJD6AVF9ivNy2-P87VK-8YEPGA4biH7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad396b4fa.mp4?token=jQz3UJi9zu-1_X7ofwIpqes3xWRTEB2AydQFab6HqetFXgl5G3O-PgDxh2_YMQI7Iq7jas2JjPzbovmnsAjrgI-m_2CJ5KXZD7nE6L_8fA29eohtv-wtFim6LyJ38TrgjPoAu09sZWTniX6REwf3chfXw-xMCLdvjgm1KfzZ1Xxx_xf9ZK1KALSRb78_Bw-y8EJKtMd1z1qnlC_cRsojTnDQZVjOIP35bpKJgKqK5-4c2Xxns5l_phYgph7lMn--l6ibqWTOoXNdn0rlXGIj0H3jqVoIKLK8f31nJKsSX2tfv2VaGR5MDihZAyNU0agwM0AclTq8RlQRgEbVISJJSDnlZ6EAL0vjbXlSIysxtkU0ksVDFN8vARA9G_doSfDaOvGDzGYQ_s7GUEIf6pigVpZ4y1k8qrbNdLg7xSaMFayAbWoRlWqLDdVuTWWewIGYgTTw6Y-R8VV-HOyFc22Z18h6NjdR7YEvObleCopFNpqiq39RzT2Zp7QVEjEF9DZNRoxGOl_1dXG09oxF9DjDaQDzhpC80AP6Az8mgiYBSjbxvdDxH2-Su8ZbVv1uqPd_0DvT97mPSk9QMAgJUSBUCYPZtbvcodifxxvzA-TGF15q4ixLJ5DlaMo_AefXlevIOR4mf1i_XcsuJD6AVF9ivNy2-P87VK-8YEPGA4biH7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😛
برخی از کنایه‌های افراد مختلف به میثاقی یا همان مجری معروف‌صندلی دزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97861" target="_blank">📅 13:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNwpGCwvcX8KPlf1oUbBRTFv9DN98kI98Bf767CVSzZ39CSjZW9PrBEJCVq3IOJ6-wL5w_NCAgaUn_L0c9iHLvrTV6vrFyV9wsxfvOTtA5rO8uGfgf2joZxJq1qAIH9XIr6GfpkVJsbCbif7899KgWp5_onb6hpiP8WnFCHKXqmORFYTJsDBpg3q5u_vybBiTUCIgAVpzNqxxJ_xQW2t4x2SbYIERSglG97RgBhguUkB1U1B9bVwwPqxxmHkK3vCqKNGU3HBaWoKcMq4nW4HBHjGnMahX2X9zkal-8XNtfN4yrZGC-hdobx_mCMokxi5iWBRVkXxs3t0md572xCVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فدراسیون فوتبال آلمان رسما اعلام کرد یورگن کلوپ تمایل خود را برای هدایت تیم ملی آلمان ابراز کرده است و مذاکرات به زودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97860" target="_blank">📅 13:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdkedykHg6Avmr4QxUiZwPXnvwQoh_T8Y8Y75qPTYVLZS11sNsrddHWk56Uv7gZQo2iqr0G-quJvrLb7t5qyTdzSdrENUnWTl19zp9ha-urigFrmL3JXJ5BVW59O7a1UZXL1ZwJ9CEd1O5KAKX2T5_O9c6wDLMr0PTPqDaqpgSh1r8aiLDKzIe_wGv6jRXT-0SvNIq_HjEizt_mZYn1aS1rysS7Oo6fp3LWXekrpIDwI_LuCQBkOOkMhsMQywFCivCOrpsKVh3JjvfmTEB1aoD0qRA1FQ0W8aOpYo4GuktPCyR6JYrD_OnJt6xpf8aFvEymDl9lzdDSwuqY1yWM6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
ترشتگن قرضی به آژاکس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97859" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df46960b2.mp4?token=MLM8XJdJ9G1Xo6WqYF8OUDY6J1deAXV1mBPHW8dfcveGips0MYJnVJpqXYEC-I2o0Ww4o4dXa_TGkGcyC9synmvd1lHUE9JX0ka3EAyKEkqQXvTkAJWgXIP25IQSPfdRLlhSWhS5Ds20CyWg70qMA-LTm5TegyEjd81em8BncQZP_s7sOHxl7lN3DO27J3IMjMl-uYAIN4LpaO89KPC5ZL9SiZa8r4kcJKllKqXXWFiMfEQqsm91SkWRx44ogn9ErmEMiMqm4Wqc22PFkxk5-xQDRuuDkayjM-9LPKVoCIkoQ4vFV-dQdvEpGiJBn-a07T-9sPw6_kj1PL0RewO30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df46960b2.mp4?token=MLM8XJdJ9G1Xo6WqYF8OUDY6J1deAXV1mBPHW8dfcveGips0MYJnVJpqXYEC-I2o0Ww4o4dXa_TGkGcyC9synmvd1lHUE9JX0ka3EAyKEkqQXvTkAJWgXIP25IQSPfdRLlhSWhS5Ds20CyWg70qMA-LTm5TegyEjd81em8BncQZP_s7sOHxl7lN3DO27J3IMjMl-uYAIN4LpaO89KPC5ZL9SiZa8r4kcJKllKqXXWFiMfEQqsm91SkWRx44ogn9ErmEMiMqm4Wqc22PFkxk5-xQDRuuDkayjM-9LPKVoCIkoQ4vFV-dQdvEpGiJBn-a07T-9sPw6_kj1PL0RewO30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره مشخص شد که چرا سالار عقیلی در رختکن نساجی ترانه «ای ایران» خواند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97858" target="_blank">📅 13:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrTgQ9LsP3BHwzrAFXXKNU2eOFMuZXN1P4jP0xgG8hNlx3d4-zmLvfPSJL9hHZtQy6bAVudRrOM9U8Ncmzx-9BiNog_7vCoCflfKlK3SmipTe0Obv1HuYPcT5SgZrZuy4ESoeKV6Td6DKweqWa2ShlE3pva0Wyc-WvzHtlzvzFv1kRu-JJ-YZ_r7-6weCQtEsHnApcQLRub7EqbCU5v6dQ726plUNVA4zhr16xYpmYCuiSB5EE3eJbBWH0_50XCZsocsVDUL4jseBpmW3thB-q1FZdEuyLCZ_WnGZcu6f0LNAifVOmsrtoy4YSw7WKohamYJz_5eH2vw8cidS8lQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرمی مونگا با ۱۰ میلیون پوند از لسترسیتی به منچسترسیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/97857" target="_blank">📅 13:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=P028efF_K51BOsROKrJPBl6TNHKNrU77EMgbGRId-fWH2BlUVJduvw2Z4vFtdDGpf3tadnPdLdertBYzidpIlacSCCrr-9MD037BaDKn1eAS5wGsmrtTcnB6uy8-LWJ8UItB9J_TmiJ3GsEFvL-MrhtuqoFCqIbuL2LiovjIVcEybsYZiapwi4lM3V7BiGJQ1-gbPJNsH4a9Guqj6JazxYyo-TwUAgT9EGYLbD_EK-bIbw_SV0ZbiAXdPZaYQy9L6lc93h8EJtNA_0j1K7oxSZ_NHPHNly13t6YICyFmsFn3_K2uziwzmeA3PUphjAJ1mmm8SKNVCJsv5SYd6IU0qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=P028efF_K51BOsROKrJPBl6TNHKNrU77EMgbGRId-fWH2BlUVJduvw2Z4vFtdDGpf3tadnPdLdertBYzidpIlacSCCrr-9MD037BaDKn1eAS5wGsmrtTcnB6uy8-LWJ8UItB9J_TmiJ3GsEFvL-MrhtuqoFCqIbuL2LiovjIVcEybsYZiapwi4lM3V7BiGJQ1-gbPJNsH4a9Guqj6JazxYyo-TwUAgT9EGYLbD_EK-bIbw_SV0ZbiAXdPZaYQy9L6lc93h8EJtNA_0j1K7oxSZ_NHPHNly13t6YICyFmsFn3_K2uziwzmeA3PUphjAJ1mmm8SKNVCJsv5SYd6IU0qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تلفظ نام مسی اگر در کشور دیگر متولد میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97856" target="_blank">📅 13:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97855">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51882d6736.mp4?token=YKXa7fkKaaOcK4nKKLYavwl32GIy3m2T8T66w2VrbY9cfjbdkp2oakbtFvLWIwfoDSS7LpMfqQqXWDMj9cwTI878FYjDUcnAvcqDVkt8ogzpGSNseZloGyEEnGQZcPrzSwb39zGBJGLXSiXEwgEix2JukUhQOr-shRTqCy_Fg2NXDqtO9t5fMR4uQu9bFa5v6Ask6_VYUXvdc13RtzG7fB66netSPlDDudsJRYd2r97SHgZ2h60JrbsX5deYsQwYCaRiyks8lLB_oaddW6UAvJ5G-u-70okAeVhVX5ZRzhX9R6f-9PgdSfU6xUA0LOhRA4cRU0gCL8a_oJmAPy78jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51882d6736.mp4?token=YKXa7fkKaaOcK4nKKLYavwl32GIy3m2T8T66w2VrbY9cfjbdkp2oakbtFvLWIwfoDSS7LpMfqQqXWDMj9cwTI878FYjDUcnAvcqDVkt8ogzpGSNseZloGyEEnGQZcPrzSwb39zGBJGLXSiXEwgEix2JukUhQOr-shRTqCy_Fg2NXDqtO9t5fMR4uQu9bFa5v6Ask6_VYUXvdc13RtzG7fB66netSPlDDudsJRYd2r97SHgZ2h60JrbsX5deYsQwYCaRiyks8lLB_oaddW6UAvJ5G-u-70okAeVhVX5ZRzhX9R6f-9PgdSfU6xUA0LOhRA4cRU0gCL8a_oJmAPy78jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود پرتغال به ⅛ نهایی جام‌جهانی 2026.
🔥
🇵🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97855" target="_blank">📅 12:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97854">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OGuuIPmvj7HBk_ZV5HdCPSRyvafd0m3iTgX1lY4m83R21DEFOh4xuxugKFXJD4ITwhiWGn79hVVwdPNC0-DVUjz-2c8bPBj-WpOzmAcijU0fZkRfZRjxCqFLIyP2v_03PvelFpfDHz0XSczgGMXL9oYfLP3Kpty43lZ3Y5xM1eP6XxCXdKixnyZdadpUA-wbS2RNqo1qyZirtQVFqwANLYFaiKMCvGfWN0diQIwVSoH7aXMlgxwVzOCiv6_7VPjeoE-jJskRW2Rp1v3GiQH-RE2g2jljx2jBwC7EjsAtez3dRkVx9hFVK9qFQFeY6rxl0q0cejnJWJujLwKn6U6HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه لیورپول اعلام کرد که یک بنای یادبود دائمی در کنار استادیوم آنفیلد برای بزرگداشت دیوگو ژوتا احداث خواهد کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97854" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idcMA0J3p_pDGgRQ1gpvy3jPFJEPp7EnQVecLlENelMALumVPm3ayiu5r7C_G40DRe-vbOzozt6rBBDuCMpMfg4xuvDz8T8YZJ_qMxfB4M1V7dcTcQxoclGU_01DXbEXwA0RCw3oapKQpk59NbVxDXpirBrIuX9b0XmckLhBB9UjfJiWhvnONtOcOfwqQVaxGxwpKTCa5shrcU-zyxGUuVFT-LG57kMOT4iS-CcU2ukb8fiU0gn0NjKduOOPWkjrP4GJlL2xmJmN_rf164PPnFJjenj0I5eI-znPIwgegsCuJrb23HSAqU_aDWMrBDgScvH7mtYshUq4JXxSvTwCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
👀
صرفاجهت‌اطلاع:
🇫🇷
فرانسه در سال 1998، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇫🇷
فرانسه در سال 2018، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇦🇷
آرژانتین در سال 2022، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇵🇹
پرتغال در سال 2026، کرواسی را از مسابقات حذف کرد.
🤔
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97853" target="_blank">📅 12:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-QE0dWvT-HXtsLa7xlcdLWmi37pMgt9r0LE4JKA-72wnPDL-64UYpmSzWjlhbBt8q8w9UPPETzPn-_kPzkjKvG0AXf5U_jMt_-0iA-pVEvyTQiDozvCWABqqG1VGk4ioGyjTaVk7TjwaavVHDyaAjAu2yckruQ7bXSBNw7rTkAheQGIJOUD44Wdjp4pNRuHEPvqoNOb2mn8TWXs1eAcH101h4fI1iXyB2eIzk6FHBlBPC8-ziQU8Ov_y3451eg7R3BdB1llYfY1g9gmGPmuj5j-sunLanve2mDJuaJ63jgaTJr2Hk72GccN0HpiLQG3hgD0UDCEs2G8fOSo4MSReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جادوگر غنایی بعد اینکه‌پیش‌بینی کرده بود کنگو و ساحل‌عاج حذف میشن، حالا گفته که امشب نسخه آرژانتین هم پیچیده و مسی باید با گریه از جام‌جهانی خداحافظی کنه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/97852" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97851">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmClY_qqrqv-BAEBCwJl_Y4_CN4McPqjXYNAN5SxxaipKJ2xrEF63dYNlC8E5IkFELzSWHwkvxvGAY2-pbZ2Y6IVg2WgDeB7HIq5rwFKrCneMIwP_cveExamCwaU2TytbMUlL7D0U1OWKMBMji-nd0qpTLXZMMRhYzohFQw9Dhb0fLxpnSQyr-tR4rGoCCLmKycdpPg_ZacozXSZrdh7FMN_611tJ6nElXCPnT5H-McpxSr6mdSohyWfXuBhJT7A00OAe6CJa4BwkFCTF-oR3rHXoDZH0YBTWUHS70Tft-2dy5r11oxNkNf1QRELUppZO41kVULLzfVIigThp19lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97851" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97850">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-ubG_JqxE1pqQMKxOrnsypQpEl8isS24pyypsfhk66cmg-wsowPejq9FZzQYqrDk60XcsUCqxVRzJEfpFxGSLSoUpHCSGq7T4PhonKkU__fo4MjJ08TfYdHWqhjuRHGKaujaR2nYQCOVVaiTIaH4onV-z4iTykx2rgFut-SWJTjNT7fg2CWV-rub5d2tZwr_4qwKzMi8aGeHXzRaPZmPQFgskwdFjoQAOpuO_EHlqsI7QZn0c0PQe6IbstuyCe-4Rb_Ppu71x9tShmiuBTKx6VbJgaHftNaH9eDcy_zxYASCiwsVl5kdbjWfR7ZsVLhSTz27MRRws4VKdJ-ZYvHGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بازیکنانی که بیشترین بار جایزه بهترین بازیکن مسابقه را در جام جهانی کسب کرده‌اند:
🤩
لیونل مسی — 13 مسابقه.
🇵🇹
کریستیانو رونالدو — 9 مسابقه.
🇫🇷
کیلیان امباپه — 7 مسابقه.
🇳🇱
آرین روبن — 6 مسابقه.
🇭🇷
لوکا مودریچ — 5 مسابقه.
🇺🇾
لوئیس سوارز — 5 مسابقه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/97850" target="_blank">📅 11:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97849">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy8q4qqjEidTLHjiXqXDPZn6iS5Iasf542_Tn_7NYPkbcxFpURb1pC3SJSbTDAjTqJJHgXoz_M0wq9J0LN1uGVMNx1N84XF8dYdL2_qynWwfKMF6Uva-R-k4dMXIOu4SY_0ZdbaTGH4dmVs_AR336R9UzYTAot1OGFx42HA00HM3VeaYfuKN6zUrl6Qrt0gCUK7YB14oOLwKbErN6g2qxGTXHNBYnERjDBQSN5bAKVxDbaH_DmuHyEbX0mepbi8PW53gqTRnnkXIimeKJMlxGmO3Nr2QpBmw_e65VEGFkgCyyBsAa_dbjGWSPZF1APudLbWpwu3lhc0HCsHnUtcc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇵🇹
برای اولین بار از سال 1966، پرتغال موفق شد بازی که عقب افتاده است را در مرحله حذفی جام جهانی (در برابر کرواسی) به پیروزی برسد.
لحظه تاریخی قبلی، یک اتفاق افسانه‌ای بود: پیروزی با نتیجه 5-3 مقابل کره شمالی در مرحله یک‌چهارم نهایی سال 1966، زمانی که اوزیبیو با برتری، نتیجه 0-3 را تغییر داد.
و پس از 60 سال، "بازگشت معجزه‌آسا" دوباره تکرار شد.
🔥
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97849" target="_blank">📅 11:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmT4g0PBHo6NyyJhcmhhEwSEU7hl6QFeyh1O2Z4kgWkcYGnAuv-_Mj0grhJS88Tcsf9g9FFdNEpk02smaBhGlYZSw2wTIhvbYVxaS5eKzHQv3Y5IUEzbrTXbvFXHe-aPgrXlE6P7L5YB_BL7sGfu_ToMRpVBeQjV9IH-cpoHKVCfiltRj-CwCILIzM0040N_WxFL2bjfaurE2Kq2ZJGIbAI6ge5zDUHXGgT6PxJXTlkOBur2DMAhJ02aqHRDncffyJqoJllSw95taUlJk_Q3lKwSeAlOdD6MUaQlFPsl9MrETNrNqiuSW0R1efZ08XT2zKxaYm_1Xp3V1lpp31bwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97847" target="_blank">📅 11:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc9-ZqsCusBHy25U1CgDvVpywCm_aMmQ8t0IlIp5Ze8lr8crv715VK5v3KKx9aFPJgjmJkX3PYvbL8lt-hvRg3porTTVa_8JHyIni_96g9jD2HhV4yp50gZpwIt25JMhWXlv0Hm_pmmPnaZAMJNPKo_3Lx3TNkCprotyJiuTOO5fD9AYM31z2QSne2qRS8QBnoNvfSaSFVXZiHJ0WqEGZMjmPbeLJgDxCTB5mEfRprh0c2QuqxZsW17T23sc00am5e2jvrKCdZ4Z6dWAhQVhMKHj0NdEedTgA-Oq7SvQJNLLZAwOjhsQkgsn_UPoeghGmo2mSyqfJ4dGhelky120GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید علاقه خود به انزو فرناندز را تکذیب کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97846" target="_blank">📅 11:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f386995eff.mp4?token=tZmpGWZi_aUNrrXtrZ7q-7j479_a85xeGUk7dtN_i_KyeRu_gmo2d4KiAdLFzcVVwqexl7K5hhWygFXF9UTI7uDfPvyPLW0OpZDnZuQxeosMZDOJOAw_42V_GxialLNSxtZ7WAHwtqgPuyT0-qz8YkTE_ZFlypaxJxmYd6dx3TuGumD_o6qJnB4ew2E9V1quz33OrJp2xRH9kZNIRitTcsjudG1Qb9ACEClv6S_bBJRbRVEDezLQOYk1UZ0I68C6OFnPbuffAN2KUC9OmohR21B6Lqk2PtmYTO8UojqvcGG63r8bxnJIB3s5ED-R6VNsUlHu__pszndyhNihHi7CFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f386995eff.mp4?token=tZmpGWZi_aUNrrXtrZ7q-7j479_a85xeGUk7dtN_i_KyeRu_gmo2d4KiAdLFzcVVwqexl7K5hhWygFXF9UTI7uDfPvyPLW0OpZDnZuQxeosMZDOJOAw_42V_GxialLNSxtZ7WAHwtqgPuyT0-qz8YkTE_ZFlypaxJxmYd6dx3TuGumD_o6qJnB4ew2E9V1quz33OrJp2xRH9kZNIRitTcsjudG1Qb9ACEClv6S_bBJRbRVEDezLQOYk1UZ0I68C6OFnPbuffAN2KUC9OmohR21B6Lqk2PtmYTO8UojqvcGG63r8bxnJIB3s5ED-R6VNsUlHu__pszndyhNihHi7CFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
🏆
🇦🇹
ایستادگی برابر قسمت و سرنوشت
دوران فوتبال عجیب ساشا کالایجیچ، مهاجم اتریش مهاجمی که تا ۲۸ سالگی، ۳ مصدومیت ACL را از سر گذرانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97845" target="_blank">📅 11:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwIRQGDfH_Nw8iXWrMUQ2FvkVcIt1Mm6fqY-B-42-3iEkmJkNOVRY_qiHydNECICCE1HA_9KnUayGvFZveK6AgFXMZw7rowy28I9wvlqmXCYIO_iYsUEc3k5ro9n189Xmsy2lJ0CH3qf7CJekO7rOK6yKXoL9NIxLxdeaWQtvvVsi_a8I7HmGDDtb2C1x39HpcZn1MBny3BXV__LePHY0P8cfBUSYkCTUQPU1y6LbXLA4fyBj3MYJqOtH1N6qOpQb5MdTHw_1Y6_VcMRyNla7Hk0V5t-BQ_kssdKuFojQ4Z7WIIhlYv1dh4TgECSywYbHxGD6CV6kG29ac8i9b0WHC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwIRQGDfH_Nw8iXWrMUQ2FvkVcIt1Mm6fqY-B-42-3iEkmJkNOVRY_qiHydNECICCE1HA_9KnUayGvFZveK6AgFXMZw7rowy28I9wvlqmXCYIO_iYsUEc3k5ro9n189Xmsy2lJ0CH3qf7CJekO7rOK6yKXoL9NIxLxdeaWQtvvVsi_a8I7HmGDDtb2C1x39HpcZn1MBny3BXV__LePHY0P8cfBUSYkCTUQPU1y6LbXLA4fyBj3MYJqOtH1N6qOpQb5MdTHw_1Y6_VcMRyNla7Hk0V5t-BQ_kssdKuFojQ4Z7WIIhlYv1dh4TgECSywYbHxGD6CV6kG29ac8i9b0WHC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ریکشن‌های اسپید در بازی کرواسی و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97844" target="_blank">📅 11:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdNnDo0KJtX8Ip8fiM58F71kx75NmtCyafCRa1elY71Ec0bSwl-T9FQGvQ4jo9pHeBAbz5MinvCHqIdcDsGc_cKZ8F8fhBd8YGMSYWgcanDhDZJOVOcwNimdlafNbgGRlhIjRpzrrZwpQvu2Jqi0rcJgeM_ZShAWYGhBNbvSAtH3aq8Pk-ahUu2oHhdyqV-j8KgapFhezBIZ2HJnlFiFL4I04Y6pbYej29uoNDl6oyI8y3DMuxDUhrvMTqf6gbHzWU8qz-y1iWPm1fWPWdosbmDzT22BPzcaYqWezSbdaeMM3hYyt8KS3phhlTKGSv2PBVA8ixkqT3UdPxbMA3roqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارک کوکوریا اولین بازیکن اسپانیایی تاریخ است که در یک بازی حذفی جام جهانی دو پاس گل داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97843" target="_blank">📅 10:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=Iyql-GyI8cQ6088fqWAu5ALa1SliXFL8Xb-SQLcnbKgRwpSGvzUnuDTE9oHknpACPuFPsQUS2NRsaAjvNND_V5-Trfa0hWJAEjrrpUNtU8ukGj6hPhpUQ_E2ws_EgUWGUGnDkvZHjEb1U4ALgQDSm5AqaTaKMqcWhZq_Uh52Mec3ROu4z_qtOcJAunD4_Zjb1GXLMALemkf75n0_kcOwlBlTymKzCltQiferqm0UVwCrMFz6H3DcIzyOnMX4ciHowla2mted73zYEOY2t_mtrXABiWl4N3mZjzR0Cvr8XC6O7sI2EsnksAr4MnG_q__KHRqI9QZ76If9aZ5y-i2slw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=Iyql-GyI8cQ6088fqWAu5ALa1SliXFL8Xb-SQLcnbKgRwpSGvzUnuDTE9oHknpACPuFPsQUS2NRsaAjvNND_V5-Trfa0hWJAEjrrpUNtU8ukGj6hPhpUQ_E2ws_EgUWGUGnDkvZHjEb1U4ALgQDSm5AqaTaKMqcWhZq_Uh52Mec3ROu4z_qtOcJAunD4_Zjb1GXLMALemkf75n0_kcOwlBlTymKzCltQiferqm0UVwCrMFz6H3DcIzyOnMX4ciHowla2mted73zYEOY2t_mtrXABiWl4N3mZjzR0Cvr8XC6O7sI2EsnksAr4MnG_q__KHRqI9QZ76If9aZ5y-i2slw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇵🇹
شادی رونالدو در هتل اقامت‌شان پس از شکست دادن کرواسی و صعود به مرحله بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97842" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97841">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1EZzdjwddsx1V4nB_ReVzyJWhvuRR723mpQOeI_fOW6XDM7lTP_n7SAwyXKkJfNgC_r2_YHNOIDUK_OrcwZwbGvOC5zl3CZsULLYZFKJtpN1CdC1PaEUDLAaquGK3qxJxIIrc1qWtmZg-m8bds2mjgeDgTsQdYg0GDe0Qm-vC933wZj9ZAGQG__PkqoWdcMaXhvrF1gufBgC44m3L9myyUqV85YLjqQ8VWgH7tcMajD2dwTBUrnATaQglk5uq7QMY23bOFn5CqxkMAJhboYlZ2HcsUIjEToA4Lto_jVI8wAgqUDuwu7uHNqX1C14ihDVGe64TISSTWd-ZhPP0XRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97841" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97840">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=mfhyes7y6WNO33lJlVliG5FVO4UK2pJJUZB0U6NjRHTdfygJXn-wl5-BWT73E6iNTLuEhogGhOtS7taw5oVk3PFK4kmx3WpQ8ZqbUBcIVKnzvsg-oT0F-sSQ3osQPzPcYLITDA5sK3DG6N--ubtOwZsGWwFMWM5LCXf7PJpD1ql9dmXtX9Hj3TV7Xr8LZK0WPuM0MimbqPYjr1kljAMHhs8t__xH81gSetCGAvqmaL-ToMKYnlz-LaOe5TdG5A_rUSMxH3wetP1trRLDW5pEpG9Z280JB8Jg0J8MCjzGLgPon2CW_X_DQ-Qsnf5k_kM9wBKHmv9Ln1runqBJsLtzIr4MzqQAtH46_KAFTXSaDorxeR1HbTCmTuac1J2kU2X9y5LvAuGmu7HVz5TyFyRez_k0HNRNx2JZVjOH6fQ0tKbduLBxc20q9rk7DSM4s4-PQS5AfJ7XV0nfaSwtGKo2XFaP0Dk0XDlWNdTNbZ6DnxG56ejmXNim0SctJoIccZoJ-Ik53cpgl-K27IQ0txppUFNcIottEJ0VlbJGCCVChQtNtmA9koOfV5b_3zgtKj3q5PwQsJnh4VCj7i1ZaUkl2JklwLLO9UJCxKOz7tPpIPcyWiOVwkUwtdzl0w6Mo0cl4CnSZTi7WQxi56Krb4wnLIY2j4F9aJMJYZ1SPa7ey88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=mfhyes7y6WNO33lJlVliG5FVO4UK2pJJUZB0U6NjRHTdfygJXn-wl5-BWT73E6iNTLuEhogGhOtS7taw5oVk3PFK4kmx3WpQ8ZqbUBcIVKnzvsg-oT0F-sSQ3osQPzPcYLITDA5sK3DG6N--ubtOwZsGWwFMWM5LCXf7PJpD1ql9dmXtX9Hj3TV7Xr8LZK0WPuM0MimbqPYjr1kljAMHhs8t__xH81gSetCGAvqmaL-ToMKYnlz-LaOe5TdG5A_rUSMxH3wetP1trRLDW5pEpG9Z280JB8Jg0J8MCjzGLgPon2CW_X_DQ-Qsnf5k_kM9wBKHmv9Ln1runqBJsLtzIr4MzqQAtH46_KAFTXSaDorxeR1HbTCmTuac1J2kU2X9y5LvAuGmu7HVz5TyFyRez_k0HNRNx2JZVjOH6fQ0tKbduLBxc20q9rk7DSM4s4-PQS5AfJ7XV0nfaSwtGKo2XFaP0Dk0XDlWNdTNbZ6DnxG56ejmXNim0SctJoIccZoJ-Ik53cpgl-K27IQ0txppUFNcIottEJ0VlbJGCCVChQtNtmA9koOfV5b_3zgtKj3q5PwQsJnh4VCj7i1ZaUkl2JklwLLO9UJCxKOz7tPpIPcyWiOVwkUwtdzl0w6Mo0cl4CnSZTi7WQxi56Krb4wnLIY2j4F9aJMJYZ1SPa7ey88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇪🇬
مدیر تیم‌ملی مصر تو هتل محل اقامت این تیم پیش از بازی امشب با استرالیا با یک مامور پلیس شدیدا درگیر شد که شانس آورد پلیس کوتاه اومد وگرنه حکم بازداشت صادر میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97840" target="_blank">📅 10:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97839">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=YrhJ_hB6Vcf0hKZIgQcT4PcsYl_2hnSPqnxXwAqw9EkInlDnbwocvGYVYe5IVThGKYJpeoRbhyGOlgMfBZxwDNotieYgfReyQXoxN113pInsVbMOBVvqBD_HdbyUYi7RHIPZ9RabxwOt4yqGe1lTKtI7XHzPvk2dFJoACo1jrhNghSZ9ClmZtZOnMQsGn7_FbQOTDUFw4bTXbUwNmHjxZP-ZqbZ21Gi4TZRDpbf8aGknTG3QDnxpYLWBFz-Uh0pFmyBF9sKU7G6EdmBDpy8jkTcK7126sQVBbz3KrxtYvW4aHm22vluwYr9fSGwyU3m5Bh8vhCf_LND3KNwFpeuXrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=YrhJ_hB6Vcf0hKZIgQcT4PcsYl_2hnSPqnxXwAqw9EkInlDnbwocvGYVYe5IVThGKYJpeoRbhyGOlgMfBZxwDNotieYgfReyQXoxN113pInsVbMOBVvqBD_HdbyUYi7RHIPZ9RabxwOt4yqGe1lTKtI7XHzPvk2dFJoACo1jrhNghSZ9ClmZtZOnMQsGn7_FbQOTDUFw4bTXbUwNmHjxZP-ZqbZ21Gi4TZRDpbf8aGknTG3QDnxpYLWBFz-Uh0pFmyBF9sKU7G6EdmBDpy8jkTcK7126sQVBbz3KrxtYvW4aHm22vluwYr9fSGwyU3m5Bh8vhCf_LND3KNwFpeuXrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بامداد امروز شوت رونالدو به جایی برخورد کرد که شبکه سه مجبور به سانسور شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97839" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97838">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=JIUMCvE7sBlWqWcn82O_iEKNPMVx0SwsW1Lcx6jC6dODgMC3WiZsWcBAO7kPREGzhz0jFsdapYhoXUo95Dwru1boIXugU2PLQ5wfFbAGrzB48xeRbGssKLFn7VQIGh8f4MOvaG4hOTPUwZqEJFYnMCAN1otWZLznOi-TLQG8KL5ggSGCKpOvHGB8j93R3DZuz_0JQnRVA7olyqLAVitwhJoCTIGZWQDmTTw09PVqVFuD5H9bsV0oBq20TMOUyPli4MFVGsVIYwARiZmKEqJ9s5BG2b_JElMk9GvzYKvnvRGBXXUXrIIME1hW4fpcX28Afu3wgNriRqYM7MuT39vcWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=JIUMCvE7sBlWqWcn82O_iEKNPMVx0SwsW1Lcx6jC6dODgMC3WiZsWcBAO7kPREGzhz0jFsdapYhoXUo95Dwru1boIXugU2PLQ5wfFbAGrzB48xeRbGssKLFn7VQIGh8f4MOvaG4hOTPUwZqEJFYnMCAN1otWZLznOi-TLQG8KL5ggSGCKpOvHGB8j93R3DZuz_0JQnRVA7olyqLAVitwhJoCTIGZWQDmTTw09PVqVFuD5H9bsV0oBq20TMOUyPli4MFVGsVIYwARiZmKEqJ9s5BG2b_JElMk9GvzYKvnvRGBXXUXrIIME1hW4fpcX28Afu3wgNriRqYM7MuT39vcWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇭🇷
🇵🇹
جیمی‌جامپ بازی دیشب پرتغال و کرواسی که با سرعت نور داشت سمت رونالدو میرفت ولی در نهایت پلیس به سرعت بازداشتش کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/97838" target="_blank">📅 09:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=WQr80_qYwbVGi5lpgqzNl-9EfRai1sySc1oOAvrTontvcQXPJ4GrE4geH7pR0LTKxh2wOgqkIelLuIcvhRpYK04pVvUgoiI_QnSx1YZzrZeutpAWbxUMaVLkfMyfz6uRfA58yCE6xycs-bhaJFbSYDO48RNuIRrNuo2y-KnKMhGn3_W6APmO4TQ6pAs_qBXHpBa_veFBhNu9tnavNT8yJWNlqKkjxcFh3UihQuM8-LDOWmWRtb-US8KCuQu6kgyHfEVPkBBJhGp7mEuYMXK85nWVT7wmc-gdecvz3dhYFGIlhzOHk_EwLChguRsCZAWuEKEy2pskwyJZo-T8F051vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=WQr80_qYwbVGi5lpgqzNl-9EfRai1sySc1oOAvrTontvcQXPJ4GrE4geH7pR0LTKxh2wOgqkIelLuIcvhRpYK04pVvUgoiI_QnSx1YZzrZeutpAWbxUMaVLkfMyfz6uRfA58yCE6xycs-bhaJFbSYDO48RNuIRrNuo2y-KnKMhGn3_W6APmO4TQ6pAs_qBXHpBa_veFBhNu9tnavNT8yJWNlqKkjxcFh3UihQuM8-LDOWmWRtb-US8KCuQu6kgyHfEVPkBBJhGp7mEuYMXK85nWVT7wmc-gdecvz3dhYFGIlhzOHk_EwLChguRsCZAWuEKEy2pskwyJZo-T8F051vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
🚨
🇸🇳
سکته‌هوادار سنگال بعد گل‌سوم مقابل بلژیک که در نهایت فوت شد و به دیار باقی رفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/97837" target="_blank">📅 09:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇲🇦
تو اردوی مراکش یه شعبده‌باز آوردن جلو یاسین بونو که از لیوان آب مار می‌سازه و گلر مراکش میرینه به خودش
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/97836" target="_blank">📅 09:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🤣
داستان جام‌جهانی و پارتنر بالای سی‌سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/97835" target="_blank">📅 09:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzBgFX_SkxK2ZhyaT_1glm9pNOf1BSyDIvaR-NbGXRJp9Dc32IsFvyfUbgKq2N0iakwBad29pL2bgp4FkdDeEUKLt_jDmvV0_QZynyWxpJQdkaVoAxnHPgKfkPFvPiYuRWeYLaKpOWckJDTFAEhHIMggZxtoZ1OOOW5x-pI8fxmav4bnP9nCksRjN2qV5WcwCZncXQeFWEDq2MrHKh7fIcox9jJcd7rvmSN5uoVPdo0AetxT6bYrCepNM_EHakEbDj86UjqC0e2yyu6EKccg_hvUsWBkqkwZwqO3RgVMdjrU0_nIWIDoigb_wqXubfI95H4VOZyadsmd-hQZuxvyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری
؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/97834" target="_blank">📅 08:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🏆
مسابقه الجزایر و سوئیس، آخرین مسابقه‌ای است که ساعت 06:30 صبح در جام جهانی برگزار شد.
❌
❌
در دور بعدی مسابقات، فقط دو مسابقه در ساعت 03:30 صبح برگزار خواهند شد: مکزیک در برابر انگلیس و آمریکا در برابر بلژیک.
بقیه مسابقات در زمان‌های مناسب برای خاورمیانه برگزار می‌شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/97833" target="_blank">📅 08:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icrI_KNe0Q9t_3CRGCTlOmGBuLZpS5FzkjPr1bj6Rdz9XsDke1GjYSsaCEtBtaBpveovPOmeQCy0-c4XYeEqP0DaNpJD5SFVH88BYqu-tVovNEp-AJvDtHDMJiIiAa9aCN4lQFjV4NT29eGuVc1pcJmKxMjqVmg5yOovDe3RTwyGTze2BFsO4J-3LQozpGBWxSzofgIylnzRZG3UbK21ZJfwV0HGfdLclYj0SdVANKdWt1iXmTtKFoOUDgODYLbWq9ZvgKfC1XBSvCn2pjxGvCjQW6cm5ZVJTEMNcQjfRBWxEd6Nlfb7-hJfVfF5gXDPsAieJz1UvVD4BZDpbRl0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇩🇿
با شکست مقابل سوئیس، ریاض محرز ستاره الجزایر از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/97832" target="_blank">📅 08:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBnwswAgOlcS9zV40KjgdvWE4ukiTP1KRrjBOawmpsB9dJPqxl1CWIToS0rDJr3nrO7-FzpUdAzl8pyJDK0lOD9bA1dhJUe4usbebhWuglaN3G8MHIQnhRCAeoLte4NgUxariGC8bktnDLBgXdKUcBt6w59bEA9Iwg_93vUqLRZP_E872ZmWIKC-yYWika5iXvNSSK6Qefi7QK3uZCaUIMMMejryNFgah82Zvm7oUrp7bW3lLhIgbqeC0nWAW79nINpbwO38J3j3KMmnnuDZOOQg448Qc-RZPUUam2M5gNOmpHe5iVushjUFYiFPBryWomBczFUjm3JY2jKcR58EDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آخرین آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97831" target="_blank">📅 08:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgrLgZ4CF-5zCSeuzpQh0PurvhXqaWtsqzP0j5yagn0Mn_nZoUfPyPd5Neu2n5c_MyAUQ4-pCo031vUlZ-0_z5hsbhGGqA5swVC4O7Exl_aTpI8weeoKx7C11tvpclkYd8sSWJUDqXN3BwOQUpUD_Ps0-_9EOtoHFMujsew2Vkoq-q_PbV1XWEqeSr5vfn_AHhi4DegdNquUJ0HrOlw3ROlPSzTF5qK-sCIk9q2KvARh1cJtQEnbMAmTAdUUATjiHBI0DUA_hA7QKvcoTwBXh3X5rthy6pZ5LBk6JwpLxxJmW_1JYY_dibFViLYRH7CAMToZVgYb772XtNKNIvbXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهاجم سوئیس چجوری اینو گل نکرد؟
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97830" target="_blank">📅 08:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الجزایر این همه زور زد که گل بخوره به اسپانیا نخوره که اینجوری جلو سوئیس تگری بزنه؟</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97829" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d083e293.mp4?token=D6HPJwIz7QOoCDGDkreAiBeEg8QXvfGoVW61JDlmCSiMunNWRn4UCLX4IIq1MosLvpQrIgkdKK0h_RhecDTiqJpRKCUjPVSaHa3KrFhvCbGcpmoIhb119lhjRz4YXBaDmuASZhLHkmaPMo_-_IQ4a30plbp1Vi14u2DrArBDbRKmpC9CLjntkhZ-FZoZDV6LmhbveN_DHCubZJ7snr94fXzPTDTBQQHCZfaYDeTK6JZgIXG87BwUZhj9F83IINQHo4sLNbJt_FqNeyDoh1lnAUqOovquJORkdb936aY45j8bM2wZ4HDcGVv9CH9T0ItZLVoFqVsaPXlIZRThD59feQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d083e293.mp4?token=D6HPJwIz7QOoCDGDkreAiBeEg8QXvfGoVW61JDlmCSiMunNWRn4UCLX4IIq1MosLvpQrIgkdKK0h_RhecDTiqJpRKCUjPVSaHa3KrFhvCbGcpmoIhb119lhjRz4YXBaDmuASZhLHkmaPMo_-_IQ4a30plbp1Vi14u2DrArBDbRKmpC9CLjntkhZ-FZoZDV6LmhbveN_DHCubZJ7snr94fXzPTDTBQQHCZfaYDeTK6JZgIXG87BwUZhj9F83IINQHo4sLNbJt_FqNeyDoh1lnAUqOovquJORkdb936aY45j8bM2wZ4HDcGVv9CH9T0ItZLVoFqVsaPXlIZRThD59feQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/97828" target="_blank">📅 07:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شروع نشده سوئیس زد</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/97827" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97826">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گللللللل دوم سوئیس</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97826" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97825">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/97825" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97824">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVd30IO6LR7d9AbkMDXrar8jBmOt6RdMbggj1ABSvp2a6smzviGPAe7K3S-mkdqznX7d8ZEn9oi9sRJhM8yAMGDBegZm-LWypzIBe9ilJw8bzhibhUWVvB4OuY4Gfa4eim6Z-uRZNWmedM7jXfcaWsMU1rPD-2gTix0UfreGHtG2XoXP4lwC8XCyRU_5p0JkhLIbXA3ihYyK6HpGtvWL_t4lOx2hH6MTsroD_21nFDr9nM0E3sRZM-Fs8HzmyPi0WEExdx6zwC7oToVMT-ujY-pZ310MTskl1vEIBm8nbJKacCaILVBgSqykB5MxHhWrZW_2IDXJvlSPKAFCCiwgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
یوهان مانزامبی هستن پدیده 20 ساله جدید جام جهانی:
⚽️
3 گل
👟
2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/97824" target="_blank">📅 07:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97823">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=WYiz-nhFJWHOaux_9xbf4S6HRjBZ4aIfFsCsd9THJQ4BqwNE6_M_tuoo7mqN4KlfQTfcZmFtToR6t8shv_ncOw9yZBCVIabU35mQZkZRJZ2kL3z87IHCZBncbrjNls2jG3GU6j7l5ddTxasoj0uD4BMeiTo5Q2cDvTOur7bpPdQXeTsjqn_wueJ4rOi3VPV7FBJu41NsH-5cpEKvX8F-thAFkOoUBwfah1wwA3j3fIkt6w6i-38dQBturQ18MAeAs68Nw5ykKtDKa6_loxxkDQxYCgkFrIRTWYNgunh4_oB0RjQY8L62bjMWJFAeRMGUtSoP1sGk-_xxzTYoLBtNlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=WYiz-nhFJWHOaux_9xbf4S6HRjBZ4aIfFsCsd9THJQ4BqwNE6_M_tuoo7mqN4KlfQTfcZmFtToR6t8shv_ncOw9yZBCVIabU35mQZkZRJZ2kL3z87IHCZBncbrjNls2jG3GU6j7l5ddTxasoj0uD4BMeiTo5Q2cDvTOur7bpPdQXeTsjqn_wueJ4rOi3VPV7FBJu41NsH-5cpEKvX8F-thAFkOoUBwfah1wwA3j3fIkt6w6i-38dQBturQ18MAeAs68Nw5ykKtDKa6_loxxkDQxYCgkFrIRTWYNgunh4_oB0RjQY8L62bjMWJFAeRMGUtSoP1sGk-_xxzTYoLBtNlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل امبولو به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97823" target="_blank">📅 06:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97822">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امبولو</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97822" target="_blank">📅 06:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گللللللللللللللللللل سوئیس</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97820" target="_blank">📅 06:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بریم برا بازی الجزایر - سوئیس</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97819" target="_blank">📅 06:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=rwG5mpWs39UsmFa3quLh777NV5Y0QaZl0V_HsGId9rflszQQKgyjjxor9nwWDIbhfLFwooxFe3r_KguuSaSf_DplxJVQVKpwEZoQbwT--cxCnZo5Lq5zfWpUAx8_n1psVKO8qS2oOP0UMg4dJCWUn1FFKnGnWAjZCF9P-_b7D8xYS_7DHz_3gdBEWUG76vahk0bDyQLNdGtZJxIjQvhq5_Y9Xphi6IjLkx8cZuz-dGM5sLcqyQFJxwC_mMBFoyKY2wJNfwcAcVaqRgqx6Cj3V0BSe0QqSIKe0WhwUoALCi6pWYvYhnrIY6eZ2VZfw8n8jfuZ4jP-oOHFjPUaeBirNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=rwG5mpWs39UsmFa3quLh777NV5Y0QaZl0V_HsGId9rflszQQKgyjjxor9nwWDIbhfLFwooxFe3r_KguuSaSf_DplxJVQVKpwEZoQbwT--cxCnZo5Lq5zfWpUAx8_n1psVKO8qS2oOP0UMg4dJCWUn1FFKnGnWAjZCF9P-_b7D8xYS_7DHz_3gdBEWUG76vahk0bDyQLNdGtZJxIjQvhq5_Y9Xphi6IjLkx8cZuz-dGM5sLcqyQFJxwC_mMBFoyKY2wJNfwcAcVaqRgqx6Cj3V0BSe0QqSIKe0WhwUoALCi6pWYvYhnrIY6eZ2VZfw8n8jfuZ4jP-oOHFjPUaeBirNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیدی ژائو نوس رو کاری ندارم ولی قطعا ترکیب استاد باقری و علی یاسینی یکی از دلایل صعود پرتغال به مرحله بعد بود
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97818" target="_blank">📅 06:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thwBt46qEm1OrOAP4tcyG4xiQFjwIzpW_CyJvWushjoR066K-Zz1tzR1rcbtP8pVT3-0XG_vo3zbDI5Fw6mC2HpVeA0zaGkoF8JbXLXxWoDtHJ42D13N--AG-ueBdULRicTxFRwEcGCIdX3eCbt4N9pCmKU7rRo7n3UsE0wGiLAJ1GdyxBAM367lnbiShenhxgI5F0CO8Xg5jHm2HODzv03UGwTrXAL54ePdr1PsH-i98wSP5QiEC1MAjSXcladfASJr0r1V3OT0ZwSRsZsmqh-vegOu8D0s8_zUHzSuQ61KaU_J0Qyd1BeJNDoq5iID_AlYFHOWXFS-x9dzmDrFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"حواست باشه بعد بازی کامنتای اینستات رو ببندی"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97817" target="_blank">📅 06:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97814">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g3jQKj_TYtSOBpMfMHwUhyfpq94ZEARUeUkVIUFPEHlNyGPC0_yqIYZikqdrkuVncQNRrwj_av_E_f8C15Y5g2mKlfVm2SaIFZGAStk_NyyR1f7hKMUWGXYxCVStNGs7B-ELMpirsKhYE8rPMBFL2Mr4H7v5YRSvXLxpdTERj9riFzdkXbmDcRU6xBoHIngTyXDX09z3DGabxDmMCUyWVTp-EUVsDgZmmyoLpGbDMtWd_zLfW1NXZsJSLK6i-fwIi4aw_yD-Z--JYTKRGjWTT4byfTzX6OqAhIOeFyImDqLgWnwIUrPfLrfFlw0IqNkhyP94-Y86cMJ3EIcxrkjG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CoeTP_24NmrGiQcb45s_rLUC36F_bH8xMCbZ7f3fxw5RFGBFsThX4GBKHmLprTswPS1NX6j7Nouq2-Jpls32fbbFnvYxjHxvygzJ62pAkB4JkHQbpbuepRJA__cE3afMZcebyDVgN7oioy-GpspfrAa9YeJl45v2FkOqcJsOBQlZh6tepC8UQEnH1nS09bFuwX7I9KRwBWnO1b2XxzO_tU8M-eX72sGoSVZT5DfzLtECuOyqPxchCYOGQeIx8_hCX66iYtBMN-GuMe5yE301epGgr6EI6L9bwYrIctQanakbaSFg6Hvibh33h-TmKLMRxXBAswYD_sMgLKOI1ohmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZR9xPHGQmYzqiQhiJ4Q7zCW1-UaVaVVafzRoCiniQA8L1P6yk3n3HBDTclFRRdtJUJl4n8NEhDs6EPQMhi-Bo2mTVSN3H6O3S-DbmhP4GtBRXRGgzraCabB3aK2EV8iKTeim1y1AKc5hx83dRjlZfpgKCin1KmAzuVUAHL5WU3jZTka7NAcnlaXk7RFyIKG5fuLuvQRtlthz8-qDgr29dKLDvg9xbrpXIwlzboeuZ5sbohBdwDwAVkWX1a-Yb7Yt7mLm5JRJXcsp4wJ3BETI8sQr7jxLukThYhJB0EsyqylOamZFDavpY1eH0v-n3eiL0q_EAXlPFFobaNhVQmdbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
از دلایل صعود پرتغال در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97814" target="_blank">📅 05:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97813">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckS038l8zXDoi4dvk3OK-mih6R2i6aOhbjZt4fI1cTPLSnNl4ldSl4FjI6v1Eb1aESOMKn2Ffo3CWmhq0aK6kBAjmLxS6lv0DjTCPXKZ1Pg1kVg39LItEITVb6qD0KFjOchg4ho8f28dBtL8Jy3j7YW6Skx9g8mGo39Y_-iD6pncKulD-uM9E5FZOFSmA_YcHXMqLfz5feVXI9QYkkHjf9jA-8eCMV2CWiIQf0EAV2oL6fV_J19cv_HI4fFUpGw3OFfISepUJzis8Lh_-uJFy6avd0-skxm8-qcI2CVaZKm_-4hRSv6xweDga1tEkWS9CoxgY_8n8EhWPwGy12L6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97813" target="_blank">📅 05:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97812">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ7p4vKc_jyZcr0DgzLVhcaJSpKs_QwgwiBg9Fv_3DI5wabAfavDGxyxz6UKOrTYYy9eZYMXz4wDVwkzcmu5oXBeS-6Vs6oSGqYHvXTVnXd_kZOtRtB9re4cB8Jqf73NmHCSSL_bWcW9bmIV7IpJiqLJqw2A-wPKCalQ0U9-GWHKW8vWumAbEGgOgWIGgLdLtgT6ptVwQqi9L_XHOyY9occ94NE2S0QxTYbvCUFgv_E-i9GsKYP0IsKQSILWrLWEokP07ChFthZgmn-PMOlSmL4xUi2O6KcZMV5o9GGpYTRsAJIPlR4e_Y70IaOi5cNrdn3eRuNGeP2oJ_8QnGkstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
قیافه لیائو قبل از پاس گلش به راموس:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97812" target="_blank">📅 05:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97811">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWEjVCDpzwgTa8OFXD1Qz8plyx7xdT0l0Z6t19DXHV86i9F6iCnjX4yy_3KkiO2zHM7gl7MCDZDMMknXVwqUzhCKND2qP22TwODCNZOeQEbjyjPvr0LydCg_psrZvwP50k3hPmmFsGyXB9AX2niUdud3zi26SejKSBiKjuA4PwM4vfobEeuU24VJYgvoqA44pTAQeGR0wDa8Z91pEznJoHExBQBvj8NbRbtb0xzAu_EXLPAaQR65Pz4xIYaQmrjzdsv8j9tk8YkvPtUQx5KrW1OU9PPi_UavDaUWiTW0dBfYlJFmxmYr-7eyIEuJPHjHNQMZ-N5B174gu-4MtEtBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد برونو فرناندز در مقابل کرواسی:
❌
0 گل
❌
0 پاس گل
❌
0 خلق موقعیت
❌
از دست دادن 2 فرصت مسلم گلزنی
❌
0 دریبل موفق
❌
10 بار از دست دادن توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97811" target="_blank">📅 05:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97810">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhmdHoKlSI60Vg9obTO5Y1uHopz4yX6CnyJGjYC9aQ2GomoEY6e09ZScB_nXpYQC1GEn9XFCIFAuzSSSL1AvTLmlI9oSpqU3SuuWl8On9y08Br3gHkjC0gMmAVzTxcl35oYGY_FWlnN1Dhb3EJoCkQ8WqwunxjnrHtOh4NMMZjSs8trj9jW5I0KK7x1PcdauC7UX861dTiixYbo32KJU7JtsWU3_U0xtfEEQvgZXe_xyf8hWwW3VxLvALdwHAPsaMdcbNagSvQTCkhaywI76pSFpo0SGJ1ejtqfAlO2tcb9l_mLJaNlHDOsPwd6M5tI0jA0j-H-r8hkBji6iZ0DqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کریستیانو رونالدو مسن‌ترین بازیکنی است که در مراحل حذفی جام جهانی گلزنی کرده است.
🔴
کریستیانو رونالدو: ۴۱ سال و ۱۴۷ روز
🔴
په‌په: ۳۹ سال و ۲۸۳ روز
🔴
روژه میلا: ۳۸ سال و ۳۴ روز
🔴
گونار گرن: ۳۷ سال و ۲۳۶ روز
🔴
ایوان پریشیچ: ۳۷ سال و ۱۵۰ روز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97810" target="_blank">📅 05:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97809">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97809" target="_blank">📅 05:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKKwWKQy9RkqdjebzGUNgt2tlRmyXC5xwVk-noiFrjYlTuZGNBl8dsADvW8HGXc3rIdQ1UnYSlKWbmt5qvgwi7_ndMAzbN1mHJNFXjTu30ionbtCaMq_cM4_B3jqo_xthIW8CkQV7aPCy4jSz5u-WBoO_UflNTaxCxVt_XdyJ0IfSFYk-GIe9CKUJW50vj_K_eibkeSWpu1_fJqqhAKGaZR3SHQVPg1BaqAx0EZO_1ZcZ-ExIRewMbPWcTo3vEI6GrQIXuQppUQ9AspW7hnxF6nPb5YbxXx9FBVUzl1wARhpdk4yuyw0np7MMhxX51YuU3xQAAYdgSNVgAhqN5lVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خواهر رونالدو: رونالدو بعد جام جهانی از تیم ملی پرتغال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97808" target="_blank">📅 05:15 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
