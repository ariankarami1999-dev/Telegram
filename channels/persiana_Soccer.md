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
<img src="https://cdn4.telesco.pe/file/GBIFt5_l3E5RvyyurTKJXJqGSAxjUXZ4GtnuSkx76JLzPmlA7xjEdc551rw_WB5mWZSBIliwPzZuql9725tHLiqDL1dMvC0W4d8VeOVZ3vtqym1J35OId01CDRp9odD1MZcqGe8GXK249aiEHnVIjcH8hbHgXxkP6ga1A05gxv2usVDQcsmJzuVmuGGHbJIRAe9dq3-bjscYe5KewdUkuelfl2NqiuwmJzV-JuJQ4WmYHTtUctm1mv9VulBt2R4GPAOosvH1SaSD3IPbFkUVbaR2UNOraSHeOyyfq1GzRHU1x0u4nFqYU3gw8Z8LTYlc2eDAWIUVkf4fVjw2-QjY4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 630K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 11:06:32</div>
<hr>

<div class="tg-post" id="msg-27191">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV0073ht0namwyTEvIUWzJiz_c5HO5oT2YkYd_ya_S8OZAFTL-vnrgrfTYDZaP8cQYKHejjKZXCExhUm9OsK7pIF06TMQQRtgtPEQXSV6ngj-eOBJqdcKTROnTus6Eqy2WAqNDpAhuZNYemAasuhKh-SVqlwXdr20GIdke99AEv58e9FeLhxD21VmD1c-hvmSiHRmiLv0d20MyOKimTgqDyP1-G-6vWzL2RkmJyeSGVTrI764s3qg1NjcdmM_PUKdLx3gB2FX-KNnRJrcnM_IluroKuXHPEslKHo1goxkEUk2dE0gbt4_aHiBR8lNAA-5A5t5FiFVFBW7vkWOY7oBfdKobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ محمد صلاح فوق ستاره مصری تبدیل به سومین بازیکن‌بزرگی‌شدکه‌به‌ترابزون اسپور پیوسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/persiana_Soccer/27191" target="_blank">📅 10:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27190">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeYhb2jmQ6INLVbaXKEJrYf9NZ_YHpfWEJyHkNALJ1mu8V2Tex5XCMUW9EXIJMhcRFgA-YNcYFdaeyKtn7_-yKjp1BW1ezkhJYs7iS-7URtjkQBLuIA-lM3zz9o7-I4P6czWjeeaeTPn4sq5Smugo-QM4VMNDRJWhRFVvxcfT8NoTlBF3lG13QyB-W6MmsPVu9gTjS3oJdfukNq8ePCWNgS1AYppuIuWucDmKNygPx6Gp0FbBYE23ELLiS2__uCLDcEeS6RC4hozPYZC9c9KGYKi2sbgTuYhOAx4vr6ws1FdEQ2uuhM7vvGDwYd0Uof2_OhwioxdxhAqYoQqtNJHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/27190" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27189">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=po6VOI04kE1ZcndFRNZfGr71-zrg3KdVTsPj3y3VaFRbKUbr1-Du5r-yZAjHrlt0sRt9Df70M_sDL-zPs64GZpokDFxvWulOlnakiguWvc4rj4OGftecUSzyUFUj7GlnQtDaOyZk1O2GCR8XCvh2BMG_kPNNICk8vDsuGmd_LNPG2QoMwK2W9OEzJuE4zBI5s1Psd1SRi0saUsMm8HZsIg5iQZI4HH4N2KuPjHGC1FC_4oO5c_8ssRF6dNgelQlMksykY_5zl3Hk--ivLoZtyXUVaGeIJo3yb4bdB_NHnNocskmh6JGA0diRW8fThkT5X6sQ-T9BSzY52eNeKNClNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بغل کردن جواد عزتی توسط یک دختر در اگران عمومی و تذکر حراست سالن به این هوادار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/27189" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27188">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a3912563.mp4?token=Qz5LSCP02F0Mvj_MppijvdyWBayp9nJDM8VoNs08_aZds9WXdVquhJMQdqHOabEYxjQBM3Dij8NxJR6JjH31MUP8oZiJV-rOIIeGW0ogP-c-LCUb0Bo09lDr6XruZckNQuq1HnrFu4n7BjBFHPDtV4weaIYEV3dKdcHBOTrEWStF3_b5FPPVcecy0_09PHlsMIAoKMsLXeGo5fZs9iiAGIOkClGTp1R1wN9Z5363AJPxgi1ecVbtGY7ANbDR_b6SVtCA_kEHeMazW_Jzaaybf00HXKmu6zyO2TLoW6-_pqCgCfPfRbFaHyQyBix7ZzNVLtlE7O_MdsIkLSqjJrPUww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛
بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/27188" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27187">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چرا
3️⃣
2️⃣
1️⃣
انتخاب درستی برای شرطبندی هست؟
🔢
امنیت و اعتبار بالا
→ چون ایرانی نیست، مثل خیلی از سایت‌های داخلی آینده مبهمی نداره.
🔢
سقف برداشت
→ در ریتزوبت سقف برداشت معنی نداره و شما میتونید بدون محدودیت شرطبندی کنید.
🔢
بونوس‌های فوق‌العاده
→ اولین شارژت 100% بونوس داره، و یکشنبه‌ها هم هر مقدار شارژ کنی همونقدر جایزه می‌گیری!
🔢
فعالیت بین‌المللی
→ در کشورهای بزرگی مثل برزیل
🇧🇷
، هند
🇮🇳
ترکیه
🇹🇷
و بنگلادش
🇧🇩
فعال هست.
🔢
اپلیکیشن اختصاصی
→ با اپ اندروید سریع ‌تر شرط‌بندی کن بدون نیاز به فیلترشکن .
➖
➖
➖
➖
➖
➖
➖
➖
🚀
لینک و اپ رو همینجا براتون می‌ذارم . برای
جام جهانی
هوشمندانه انتخاب کنید
✅
⚡️
اپلیکیشن اندروید ریتزوبت
👇
🌐
RitzoBet App
⚡️
لینک سایت معتبر ریتزوبت
👇
🌐
RitzoBetLink</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/27187" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27186">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX7dUGvM5uErBXi84-fq8uVoJyh7166VCmhHrXFaSrwWuuezpEU4EqPk4ZgoOqHvjJfeKy3XwStUxvDPSBh76AzN-bzL3R1F9E2l7NM1vGU-tQo_Bf_K1xJYvR37-2gGGKn0-iXoYFiXa-f5oi1mXO17qSSTPpNQn9IlJQnVAW-rgDruXLjBxhAtjORYHm89pdDTxYQjVzMIqNxPrf2nHepxIwnlS-7Z-z66mikSUmZnlT68_vbrYI_l72iHhvUReDwVCDeMtE-rfcWYB-zmjsj4I2P-aDjLsGJybkdtmbYeOVQs5eWNoV8reJGyQ15Y9heuaKCO0Bfeu7p8Hoz2Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
نزدیکان دانیال ایری از توافق‌شخصی دانیال ایری باباشگاه‌پرسپولیس خبرمیدهند و بانک شهر این باربه‌مدیریت‌نساجی قول‌داده که بزودی رقم رضایت نامه این بازیکن رو به مازندرانی‌ها پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/27186" target="_blank">📅 09:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27185">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeR5mv4BHqSPZQ97stYlcrb9Y1Nq4lqkFUP8QQmV28ZucPPqY0HHDIgbb8Cf_hsoGFPOb_TlLD4O-SWT-5qk6KJZ2Cgg5FCul58eivrGK0eZjM7IfYG5DCkg5ur7vXRyJRlYIwXO-F5Wp-VKB1k1MCa0gbO6TvQytICyZS7vpuvseIyRoNJ2nSv5zS3nEbIgrqnOGnARcseS8qyUDQWCieRjeuPzVeKk5ADgyxv1B2nAqsmbHIsGtGG4jgm13AIPXaoDFt9aVm5kqX4k_wGBMGwwdWvjUzqLWy7xp4d9yuFLrbvTORg0eFVb7FrH1WpEHj77_F94Uy0iDvMSmlfoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو آدان گلر سابق استقلال: هیییچ صحبتی با باشگاه برای بازگشت به استقلال نداشته ام. باشگاه استقلال به‌من‌بی‌احترامی کرد. دوبارنوتیس فرستادم اما مدیران‌باشگاه به من‌پاسخی ندادند. بر خلاف میل باطنی‌ام مجبورم از باشگاه استقلال شکایت کنم. اگر جنگ نمیشد استقلال…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/27185" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27184">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT5VCI-SrcZGqpIy_yinBUHBztA79P0FbGuFGM2Gd1oOggfOv6tflbKaWZJZhFAxDUjlDRKIijYayYQgQw_SgfKxKRzRIqWnJzHFqE3wWRL5mmiEzHwrTSPiRee5afhgKuPQUrC_xOXpg1rbJGzi49uM79qFgPpcN_GFyNyC7cgNQwmdlejOYsbNdjUhjQTE5_C4zNWe15h31JwcUgmjcQmD99eRmAt5p6A4oYu4kId7hWfr1L9imHSZ_CRiHrMy-dwfa5q3H0ZdiMV9Gn3gT7yWKtTimE55wSQReqD7fEbo6vh9DBpmzK36XYLSbhFikzEg0s1KyiLAycvm1fdABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل لیونل مسی در اولین بازی‌ بعد از جام‌جهانی که از ابتدا در ترکیب اصلی قرار گرفته؛ همچنین لئو یه پاس گل هم از روی نقطه کرنر به ثبت رسوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/27184" target="_blank">📅 09:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kN54es1U3C8dGcHeiUoxVMAa_5MhOi3mhGX9lAzX4ZVW6jgPjZhzaHk1HtuJX0JAC6tLmDymLnm3CCloe6A3aSaJpU1gKdri1YJ21Ddv2C45A53qJzZq0P63mPPr7ildObfb0Vth1gQcZb9DBBa1jywyzCkWfUt89FLUVQ1_PYt48hg9AGSweO4oh3qdQ9LJX6bsSWMrrgv8IoI0zgCx7ceMaEPw5cc3cNYrAj1On8yI8LQXlcO-v8DxJDuatDA9LakyCnfXrc7CWPEisD-IQY9OrQtlPP3q9MfC96RdurMi7D8cne5CRaO704dR5uWAUM64smD7YBlB-y90F6BZyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آفر مالی رئال‌مادرید پایین‌تر از ارسنال بود اما وینیسیوس بعد از مشورت با نزدیکان خود از جمله نیمار تصمیم به موندن در رئال مادرید گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/27183" target="_blank">📅 09:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBzcqlvXJuNnhvFb3QNAyTAnuXZ9uUqWFZEJLLiJi8Ei4TAaC1Y87XKyCRDSDCaxZhm0U7mzuSba_mFPHxUBQqz3MhUxCei7QnHIyOat-oToHqPYBu9erL7OWygrzgaXKLtOM0UrugaG0PnC_s976Wej0Zt2rdyoLhwXN_2ehoWyhEgUH8p0eRdEDVJfYvH3BpCzLqtN-VrJV7vvYSofA6AocpuDRf0JGVXmfyohysWvAQU_yRRf0l9iaJz8OiqSKsvHlzfnI9LK9JbCM94b43Z4ulCnVxTtYaB1LjkvWWpGpBLayn7vzoQwzv0gJFgI7b4pv5-eeK71pCkJAJMYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=Nm3rLF8TW4dK1HubfFlbVOSkX4QW6ULqo9ed3meHwHRnOs-bTb64clHvtz9QxzrD4QymVyFKv1NTKL02S1y96CwY97YbUsIEQ2_KN8xP5x9CVUg3QXI7UfjR57kJgxh37wh5UzTv92MvsfIob8vj2dEhV3k8RRakXOHWQaZIfNw2Nw2lXJ_pI0S-3rmWmeZUMZ2FZbZkf9euohgUEBUGll3Bnzj7F2dnTNxdyjsDeRP_gS-HchlRoZtxPA2o2eO55uQOUjJQCcVu7wrKmxrrq-w5cL0fD-bjEDoGkUy1-lAZx5775XM26golY9vhOCR8kq3JbOX3AK9q2ClCCBsvIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/27181" target="_blank">📅 02:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27179">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhEheoWubFcQAnkzUCH0O6iKO-dwRBi1UUZFJtK0BTK-5ZM2eOd6E_Y1wonQdCvMPgBkqvxTEpgDllq0yZtsRuFATEh47A8KgRhTSYhMzTwFmfHXAIuYq-JxBkicznn_4YAMO4eAu81nL15PWGyXVoLgu5EpFT36sgVHiU3R0c88GeNzvA6iqiY7PLFZRbANr7RuPPxQxPkZDnovsaFv-ESvqvQPza3d3fjBziVMEQw-KKZvHC_rTSxh47d4EAA-XKIsAhMbolSofFFdf-vX_V0Kdq5wTWd1QMx_NeHNe0SVSoRcgbGMdVOPWbzHnrEL-cUeJR09poCLVuY1GGUSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27179" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27178">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از گل‌ های دیدنی در مستطیل سبز روی شوت‌های فوق‌سنگین‌بازیکنان؛ عالی‌بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27178" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=cznt0si3fuTDzAwoTsqWfgZFzgpCDT377fkrnIECu3VVvoamzrIUMP4ScC5AuWI2F_uaSRP-ouYZ6XUwi_uVTtSZ_iqq1revKjzxcg3knx4u7Talrv6-kEDdTSAtaYw8QiP65-xT1jBYAriZiOqE3weG2XOHJ0vkCREwjR10cfhpu3KVtngNHTgLcNb4z3IdcWwza1pePwukiunQfahmARUD0MXVGAc44ACQcjy1iZXW4ztQ1U_u_pSK4w7lKAI19bF8pdNKPvRjx9uE-UhyVLnuxI25wdv-J5qybGyZ2WIigqXWbkdUpoM8Nss2O3596aZgWWGSmlPUmWl5IEL23g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=cznt0si3fuTDzAwoTsqWfgZFzgpCDT377fkrnIECu3VVvoamzrIUMP4ScC5AuWI2F_uaSRP-ouYZ6XUwi_uVTtSZ_iqq1revKjzxcg3knx4u7Talrv6-kEDdTSAtaYw8QiP65-xT1jBYAriZiOqE3weG2XOHJ0vkCREwjR10cfhpu3KVtngNHTgLcNb4z3IdcWwza1pePwukiunQfahmARUD0MXVGAc44ACQcjy1iZXW4ztQ1U_u_pSK4w7lKAI19bF8pdNKPvRjx9uE-UhyVLnuxI25wdv-J5qybGyZ2WIigqXWbkdUpoM8Nss2O3596aZgWWGSmlPUmWl5IEL23g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27176" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mkK8TGGTTgMDa2ngVskWUmw2ND8k9j28PI-pkiomUpV2BzgYFw0-kJ4OopuNvCzIL5wWF63bslLufhV2MnYmTf43Scm3i6qHSJvePOZXVV-KLKkV5BzxYyVoehrzgaHX0-a301wzxZGAAa0xlCYIGLPCUWqZwCyQaQAXEu6dThdsdEM48AR10L3QML-m9F-QBfHtkZfllsfEA3tL-G2n-YdoDbjlqxTSWRXieav9ATf_OkFinzVyOq3-rUDt2g8Jd2pxXsXGhmpen1jv2cbGOFTFtxxnIzvZfJWWkuL97r5JU0jbom6oetAv4FL0SkPqbn4TEKyZCoBCUB3y0bow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌‌دیدار ها‌ی ‌‌‌امروز؛
بازی یاران اللهیار صیاد منش در دور سوم پلی‌اف فصل آینده لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27175" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp44nDugGDQN7WGqw1eCesFdZwcPf26-d5ZOoofuF7CUyNLmSZ4Qdb5ue_4_RYTd7t7Od9IPugKxJWTZslrXZeN8fMNNlb9rnpjtfEKBUmqNv_xsTq9tV4FcPLq-QV3_LsFGtrtK6ty-2nFMkMGTqJri9SXf9mzeTRNqQA3ukXfMbyMBPABHoZUYA__cn99_LyS8OoMTbhhP_VnhnNdV4wcquKGA_VmcK91tUDXoSw_UrOXf1sJbYxGZ1hZPMrlOZR50ZM-I908dqh2JwBnPFNfIzRT1xP4AlTATwGH9EWf3Sjmw91rXzYkqOPT54uHPCmP1CR2VBHTsBrlGWz7S9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
تساوی در دربی میلان و برتری شاگردان اسپالتی در جدال دوستانه با چلسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27174" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd26SkgujW-vnz6cab2PZGloAXjQC-87oozRL31oJwQ9LLOPn8Q7y2N6nG-Eo0QwYpa4f_sAdFianBeV2tSGpLxX4jAmOoxxUFEKgsgWV7P1-82ZHnG_PTlJ9wU5Q5H0NFyg2IBy8-4KNDcleRcHrG-4xpatlPEn-SPcFVOHTgoTQ6nXGlyp77ewVyt_NCdisP22yMyIDpXq3LaF1kQa4ufGtSp_te4uHpWw42QoJBBzbvPxhPpO5fDj7RTa0NdtED5nzh2-bsHW_qyMXB_Vd825x7N9mB57WA-9wJewOhCNSp15kQkSJDOBJdn9x_KhunHV9E-uTrQriE3RORC0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛بیانیه‌جدید باشگاه استقلال: تموم کارهای‌اداری‌مربوط‌به‌بازگشت داکنز نازون انجام داده ایم و منتظر بازگشت این بازیکن به ایران هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27173" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeJHsvkdfHZtnWZ5F4eBzLxtk8DdKa4eG5a-yhB26NW1jr8ltRkkPPOJzoHban9zFc8WV81FdNE6fzoK2fngSqyFE9T2LVsKS4jqO9QGAOtHpa5JleSATLMdnonM8wSIK5NWe9phxHvSu_ijiXTVOoAIg7ZfcLdE_Uwa4rllC37RamHlDlgL6QQc2cRMKJ_keeurUoELNDb5QRPKvIlKwM3Kgjz-lz2_vBuLQjera9HJX6FYmpT4T8A8YjR4todUqltBucl0rlqNkij3WIgCtE_xs-c2XtVoYjI5sRTkdFzJqRzrUwNt6t2fn9CWnmLFbPKL5KanV20SWnQmz7rRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/27172" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4oXaCtkdQ9_f6towDPJTJBiopjDybnplYAd1tmKTTOkuM9ZGo8EdoG0kUNnnKCBGM5Lao40RVe1-U9qaaqely8UjQ0cy0G3DVwPfNwouhMnlK4y-nuDRBnYgRhDLtS46Tjk8_H0Q-SrgrbySeDG3yWQNwr563OApB_GkYQcZVRJit1khbEKF0UDb559u1ESoFJ82pQcWW2H4ywbhs8G-A7AHZ3E_8mp4qXzMriwrBoP3FZf1TgLAVNmYgueMDhxORSshEV5eP19MBfpo1y_syJ3g6f2tg--qB6EiXH9R8a-rhADKTLS6T3w-LCKGk4_b4maVHduJDYXxsgKVeSBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرو خبرچند روزپیشی‌که دادیم؛ باشگاه نساجی به احتمال زیاد به‌وعده‌اش عمل خواهد کرد و دانیال ایری رو پیش از شروع فصل خواهد فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/persiana_Soccer/27171" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPJEHP84WYf4xSs3RKYyI6DZ-mNkq6k_71yiOnM05yFpEdtBLsG81NxkrdkNCjf-GhCqfXD7MkPHBMIsfOuWvwKTeY5pwMiOsmyp--dIKzthSpk6FVYA6e77_BvW4w6zxD78x3LBN_3OfHP3ofOqBUjPHYmfTiC8VzDbEIx4T_At8gqUIVMPk5J5P781bwWNx1IUQihDJGZHkVTQuL3Ddzkl1Bvv7B6yqKwc3IM9w6h6bZonAqVIpvpEG8A2DpDsEd-CEH5X4yjUltKa7IHgOanqatepludIj3hVF881wiTPffQCYcHUH5vrEqPIKpFnDiatuZ67D1WSr8haF5ynNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/persiana_Soccer/27170" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2pO6GPux1Hf9Wc9nIgR6LItBJrQ166HxsmPb7e9g91hx5sMH4xFLc_DX-eXeLah5EqVHjqIgRZqrUD9_H8LuO17r_LvDKgg1LykDt3W_ePpNslJK50XcdNlZw3Lg9eM5n5TMHRvjn1SEJkzwAGZ8zLxt5FbVRvIttANGesaQaOvkDfJmL5adCYriVmV5hKoFYgZoo9vNOisyr7UWX10AzeWx3QyrasocYRg0iGE6ph3OBVoI2Bt1QgJVLzKzorkX9ZI4Fkyn9VzOytPogcwIZXwlirymOzkPDZhXoMrRepRoGteNtwUhdhVmnfoc8sqBW1fIlB37ZdFCbhiZq7FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
توییت‌جدید علی تاجرنیا رئیس هیات مدیره استقلال که غیرمستقیم‌اعلام‌کرد که رای دادگاه عالی ورزش اعلام شد و پنجره تا نیم فصل باز نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27169" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqaqFZb5FULcpD_WcQkzkAQaksXERYmh7tzVNuBVPfIdMr3kJ3KzWyvvNl6AfLjzS7hFWMMYKWHKpG_emVE3sZTvVdwzZOSaynf7mW52tbUibnzSRV3HDQIOs6xSg6ei83nkigUEVxdPTTukI2p_Q-R7v_ofF7UzFN-wK66Nk8LbyIEhXL-vRICqetNQYUYROhfg47kdUlh3iRvgGlpaH76g4l5xVBRMGFc09QDBpxqkOtDnQ317deFyH30D0MBm_19PX3JUMnHg9yksx-6EhW16EhZHXAh0RtvUoxP6QAfWGW2Hfbqny94e57NkwxdBMSGHAbZBImv3sy71Pe3sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=K8j6nXIUadHX5_Yy0kE_SppnQCAymZyk9b1Au26obIjA2suV4UljMg3yQlwnqumbhkjQQUb9aBwpyyIvIXzY1ofvUrz0QvumB6upl5iUeR3XVnBq_Zozb10fW39wSeji7NKLLCIrXwRQgxvlOfoDpSLuCXroMM_RrnoU5HJpyfgWXZtT1wM8LCQYPbzJY4Vs8Wmrx3YYlVlAG5wumxTnAy8oi2Zu0pZvEEhHjAl6Ld_cekiERykGmKiP1GeOERa0jAs2aHeSAP0FQPrVKkVfDgBbOzIl9_zbr8R3VVH55CooTMFthXxKMHq2NyzDrvo-rOl-_rfm1wRK2fbncBq2dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=K8j6nXIUadHX5_Yy0kE_SppnQCAymZyk9b1Au26obIjA2suV4UljMg3yQlwnqumbhkjQQUb9aBwpyyIvIXzY1ofvUrz0QvumB6upl5iUeR3XVnBq_Zozb10fW39wSeji7NKLLCIrXwRQgxvlOfoDpSLuCXroMM_RrnoU5HJpyfgWXZtT1wM8LCQYPbzJY4Vs8Wmrx3YYlVlAG5wumxTnAy8oi2Zu0pZvEEhHjAl6Ld_cekiERykGmKiP1GeOERa0jAs2aHeSAP0FQPrVKkVfDgBbOzIl9_zbr8R3VVH55CooTMFthXxKMHq2NyzDrvo-rOl-_rfm1wRK2fbncBq2dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAAK_qC1tKOj0092CNCwlbkhnMKNtmeWDubr-n_Z90gQn-WwsNwkDFEqauEuFRRTXV5gnhqn5KLTtD-eyx8vGWqqJu59i-N8Yg1J4sh2-s_RD1Y9znV_G8OgdWBf15p5bFxqG2-UqHZTm4wBvSrjyWF10bBMYYirRDXOxVRLdGkQ3A2QD9nEmegIzkgT5VRsK_zRMgCILBDsWlVNNSrZLGzqIv8w776fwS78PPGmus4vdPNVlT21gZDvoy1hWSiHlLUFTk3TkXWnEwdAX2J02D0LKW6hz7Ladk8_fYbrgGhy6qMYqhfGIlVnlhK0D3ycmFTocw4kj8Mc-kf5d3n_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neDrS1C3c18Kjly-0oRjQ29fP16IvJSSgxq3HSfY3BcCPtWPv79qCcsyicB8KFVQ_jiJvljW6n0dgbjhKItaTflWvwqJKePqlD7sMyHkpRFK1537IZU91wlQjhsVL6RkDUGv8IE2wo0-CoWrKISZU9JfgmjrT1zdftOAC8vSDGVEM2j8OFEXqPNUGi_BwQEqo1M4yQ7t83rVGHCtvJPNXi27ZqSWFSRi9fesoJf_-1Kw2Pdv1mvgcWI2ubySCOmynRFMVhgn9OhJh_V4BM-ihhf5w3Jt1DhJXvx3132RE7GLxTehg4PHj7J2amUpDK_jnsOViusZ6m7XrsB7y9uAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR8SaDeMmnWeGgR9o41eqZ1DorBPgo07-YhSs8nYgScDH-CAMkd-5g_DucUGVbsMnW_jXV410vKG5-DzO5shgAODX3xfK4qp5eqxAQbrTI-I-AIuXWaE-d0H4Udg70ZG4szWSpBuQjIM1p4RyqJmeD_l6MUaniVAxq2dxRmhpIul7e9nGdcQq5tbzgozBCkPHoDIpsoXw7nAHHiJy__XQwY1uVeJwUiho8aNWVdplU_wWCs6VMNuJPXEj3bUMSJz6sndOp1hm7TwxEJ014UfXeZ8LGL9zoC8j-3PN6u_dQJ76BfO8pQnbDPZGxlXpi0FZFaAlE3WDtktfntBO8-PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_BgRkJfEGcYG9Ax3MVXEihMWBShcZMW3mr_B0X-kdlKOxKf5KOUZ8-7jp9fF5pkgP9ScBhC2LZcv7oel9CIxGIdDYuuML11fSDKh7K4j8RWSJFObkksPngEhr0S1_5P_05NzejLK5fUg3xJz2NUoi2TczqF9sKwbprINwArcpG59swfsGObGcQJPqC6pnGqKtG3LSjpG0WBehxKyr7vuA6-sSKwkIFpFWgXM1F_OkMkAPhus2Yzle2rattXsuEZ6waJFkQMOidJQRierACEz4JaYFFxMvDtiXrNInqLPesfFEHPlEvQjHpqsYEbiJ1krqS2UuitBUDQXwjIqSr7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIpOLT2ahILg9rSSXbipqE1bwwn0WvujzZJzJeKFZocIw2q-IpwsqRmPk8Q72ETRaYCUfeqHj6v5ktZ_sKF1AOKp-nELxgHrrVo1tgPklEs_FLeAI_t6gzPyDcfXDMsVK6N5bADcicZ0PvoB6B_ICR1fZ1T1DqctTfpXfg1bJAOTQuhL9RBLO57FvYT_pyFZhYy1OoETIyOtPWvm8bvE3cOZTO0yfRxQOHuhFsxYCMnITY-g2EyRoW_LbKfUKqorSZdxy-MGhay4PYa5hcHsLnrIb88pw_EeXagjN2_oXbcX6MLvhEcGw1kq70HbSdUDNQ9Ad2tQPQPSjwe5iAidXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVnIJAE7q69t9BnV-dkLcEzlaG2-fa3AuIFRAr85d7S2Y4EK7pPhd18Rsj43nK_7fazXZxwmqwQRNDL15shExSTY61Wfo7eB2mvDfrCnq48ybNd3js2YPMdLo7QG5RzF5NB2JJuj_57CytgdoFJBV-_4I83Pr3PsAFQBkTZOlOI95okCMvna4PFHuMUhrIWeeInenOPJTD1UvoVd2HykRrgX7G_V2_os7a1noxv84X8dM1-lpwO5VCyE6D--04fjbsaCLs_JrF7zddG3a2B5AW2v1pjHdRR3ggNpoVLYAIRZtHhYa5F81oozrDIoXJ2K5hg7oEhsugch6udV_-N42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALR-zXRd-jImnhoRyur_-cfzyl-E3E1HPSKbLsSwrIl-lZVTLucqR3lR_JcpUrKfKRnvhrDQz9LgvlPloezpL2vXG8so2eZarga8sv3rj4wr-u_cfm1JzCWrICVoR9UivHJuYZgFxX8RwDAJNQP0Z8bRiTq-NNZ2B2wSGn1tOjIJQy1SO1IZrMLERav-A3FSiuwg2CrZMrApBDSQGNgUoGtFwXYmmavBtCMB1YDNqIHy_Lcp_kOyKed9CTiEBIwZdf00WfOd-JXYEpGTQXRbLId1DNFQC65CDvCSqhIOMOIdcuD_8KzDjdCCPdKJW4V9om-ZqSpVxYBJwnfle-9hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mylT040P_f6prCXpJX3P99zTYiQCT3klEDgQwV4akUhnxaluWuXrsj85-bQ8Cn14mX1IFR3YdbNn4Lb49Aq9au-USERRIgRSFLqIzdsjbPy0Jisnz3n5ZfxnFs6MNS022IPIJ8K-SakLpjiB5ooCIawL5weV_ggHiOvb3jzP6UOtiX1WqiLQr-IaUgsbhSiEAlN1tPQMswpNgScKCFCx7vGo-Csy77ma6T9CRnuzbrIqSDylWOunvtcHBVdLxS_9yN-i-fUNhYD9W6jbhWRVEOaYA4Pk9VMh5xnZV4fE1XhSryZzls9S_D5UcexwPNneXkZK1N9KrFoQfm1jJQKMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFP031Ikh_m7KSQGopUT0FBO68R-tDwBXK9Dfo6tB913h6zX78zuaq_iF7OBSjjIgcbFfovE-4audo22XxrGc6mKsJYJvfVviY887gtWgpMyDsY4cknJX6vC95RVaE7KQN8rIIxUCnyyyIDW38JQyz7NDIXQukFEOfYGh3jSEdjfTzzyx0zfozQzI4LE1pF_tSwtAqIKheflS-MvwnK6EJKGRt6hrq2eKoWI2GsdHB14qz9AVkX5agPLnFBFs2xJJrchhIQeSTmtWN9Iu0cOCimRKCOoQ7TLi-POtJN1OGuAuHf6beGJxbVT-x1RjtWUvSSFIMzM2MwmXG-C1B90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT9RLvw1mF5so-ypUsbGHFP5GmDz5GlI8b6TmLVYDbDH2mNyWN7aoxWXz1XLHMsxGdnHVMx4E86CvBfc0A-hk-Q3sbcVIECQcScdpfKoSUj0g03aVoWJVgDVptPrGf1IAPD5XwWuLOP5tKTeuqAgX1qeluO0hbdOszRRG8aEQV6vF24iujXDX_lJ60RYKaWlIS35IUtROCgQ0jSyY5JPUwH2rWAztg4yRCrYlc880GLq6bBs1sV4LKOrXGSJEZLJdDDomvaYNbthRVMX1MTMtnISeCtdf7Cq_76Cw3xMnq3GZrTaj4bQMKhiyDk5kh5XBYk9B73culuVAgH9sffc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIdgSaGO1gqq9EbTeO1_7qeK5WRLttW99lipv5HnRD03VY4jQN8-FrqPGKqX4vs9XZ-0SGz-AIBOlTRJi1qni5HLZQwxLVTtLuaDEVoapikSWXe4TMpMbp5xo1ZtE3pZKlKJpqGpyYz7yf1NQg8sy2iSKzRPs_ZKK-UUDqFG6pyPNXhihtnAs_LPWQ-LcO1ZO8_imiM0ndbyfhgWYv47ot3WtEpqGp24v65jyP-KVBHsWrMXQlEN7Ts3Iz28xGrMeRF1tqS9TrDY9OfJYik2MR9jyTx5QauGeEIOoJmhnnKp4ec1VzPGXQnnLPp5VquTqGO_jjkC515-F0FF2nFI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4LFu_JNrj-L4auhMasA-YKIS6XROGekPkT5vuetmUua-X6qqXPA798MhSykBoA4qgfrsQGrkJDuvOnRac8NkqmEP_7hOfAXr3kTHn9dLnMuKhYV6-ryQCcOYd95xpLGA2LdanGZYez2CzPqUbmOBkpy63qMJW-EAioJF0A1R0xLItyeEEurIODzxiRF9uQ7VkQuyGTVveog_EQPMAz2KDdoy5gVL5k8k6YosOfQtfEuK40A7oYjmfVEUxcpAHoegs-O7ca5yIdNyvnNcVulLjHcrJZP0QfDj-rFZKNEHqUuLAOujb0B9kuRr3S4HEm0aFtw2QzUumvbgVTXOh7vsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs4W0y1Q2XkgcCWujiwjapIAskiKC49QMX7I9GNuTEiRHbYaT0x8PO2EHrp2F0KrBTsd6vEOJl8uvHYCnXoUKeW4sj2j6cwpJQ0XQ58CtTmW-X2GkFzX9J9mVp_k_Vw4VGhzWD80gnWjVuQYC1x0kUiiJVv_deKYWJl5HBJWMljVoc7x2pKiDZhBK_wO6cqqan8qGgwJAadZk6wRJDv2NBBA44Mh9Ul3hFp6qP7ZGwivYP81vqsfXzb-RMpXDTvj4kZKV--qtUJn4n0_5MWN0xvEr9dgpUYlo9DUMzigDwfV6Tx0ZB6ne0la-igMHqovQedVuyKAhFuCwn7YdtB49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6UYbGC5aYcIgfjwGZA1078-Vs_gqioUcWfchMaugKRP69ziWnYPks-HieWuoxAHm9CDgSI8mTbmVKcD5kWEbc-YyxcEnCwUu8xh2iiCwMiLnrG_JrQfOAL71nA_gbkSLYCYbVxtwdE4PdmJxe-D_StSbTDsypQjsfkc-GLUp0QDuYEk4UoCiTn4MaUmBY06fj6hGMbscXFaZrJYRS6LOxTkqnzjD_vb_SaQDUMqgQEthRDkCNHXjjwTQ4db1CFoHczQh6tLXeUEPPv8liEW_Zy1cAZQFnEx2xx9Y3JeQ7WBJs2LvhLxhlcQzYmrdp6QJWUst13g23AhQFjc9HAlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=tSI8uk1FPbiY0eNn_rE6zz7OwgUiyjM7b1Vc0oLhEwVzPQ5TXLY6ARhAWGFjUM_jPKJQghLi6eywlVnmvXDHd6v11u7LYQcKIQzrKRog_o-TkhjVpb0H-7WnjrlkNOHYlO1PDCT6xPj4oWvRY8NcKpK1YplSIQOVK5U2WcmOi9dd6KxEF0x_dSkEcUEBCT9xo909QqjNtKyzxdmpvbQZb7q2kyeX07deIWn9L65KG3poFQu9VbFPBoPXKyteNcGcyo_ALedlB2DuHKQyzLSL9n3Rp71-T_P0fcSDz6qJ_zetDvCEDSjgXFhF3_rpo3Zc2mz5CHMywFsqsL_rG8j2AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=tSI8uk1FPbiY0eNn_rE6zz7OwgUiyjM7b1Vc0oLhEwVzPQ5TXLY6ARhAWGFjUM_jPKJQghLi6eywlVnmvXDHd6v11u7LYQcKIQzrKRog_o-TkhjVpb0H-7WnjrlkNOHYlO1PDCT6xPj4oWvRY8NcKpK1YplSIQOVK5U2WcmOi9dd6KxEF0x_dSkEcUEBCT9xo909QqjNtKyzxdmpvbQZb7q2kyeX07deIWn9L65KG3poFQu9VbFPBoPXKyteNcGcyo_ALedlB2DuHKQyzLSL9n3Rp71-T_P0fcSDz6qJ_zetDvCEDSjgXFhF3_rpo3Zc2mz5CHMywFsqsL_rG8j2AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sve9nRhjqYllKCS8UK_QQnDviBqYnDR2mQmDAiMeDKBS9VsQsucLfa24w-2FbrGZjOAFJ_6KyKF9wu6UZsr9Lc4mcBCk3pNDbY05KMGAA5681Da4oDtdqr-J0gv4p9zooMkNd0qQjKN9CGTMYfcKfCv5-nHszZqS9JirG99GclZLFU36SKMi-iZfcuPZxRDIQhTuHWT9C-DaE5TrkVyxemupKhbYWI9iko__45e5ANBN6bAaoGeMOVFsrE5psKqQ9OtuQNXf6uV786uVJfbcr1L7nqOF2B7YRR_qpuLcgZ5SYEp6rBAeQjXkme91C5TUPVk33w1wFV0OOitFrCEt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=diaMzu7TaIsWBTaa7PKJSp4RxNtxtF9c-Z3iEh60ayA960QBU9YHBt6hoIwDO4do2cRZaXeXpOu__LEe7eJh0KiCHy1pfyZEf0B28fqJBk7LawRkYgihQJqED5yUmaQpM6iQN5epAq4W_4GPbI0XfdAZ7F6_BQLl5zsXX4DJqOimonUMmFZ7n7ZaRvV5YeJzBuS1u6IDd17YfMKJVkPD9NrEZG1TvMe_JJoUTVdM0caEOuZ47vFvsV6qEgkoMZlhuWT1zPnnOEP2qvMhIBvgPVd3e2_d8JIK42LXJosz-3v3K_keWU9F5LeNkDyEL-aDJcSFgJWeoH57I_qoIhxkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=diaMzu7TaIsWBTaa7PKJSp4RxNtxtF9c-Z3iEh60ayA960QBU9YHBt6hoIwDO4do2cRZaXeXpOu__LEe7eJh0KiCHy1pfyZEf0B28fqJBk7LawRkYgihQJqED5yUmaQpM6iQN5epAq4W_4GPbI0XfdAZ7F6_BQLl5zsXX4DJqOimonUMmFZ7n7ZaRvV5YeJzBuS1u6IDd17YfMKJVkPD9NrEZG1TvMe_JJoUTVdM0caEOuZ47vFvsV6qEgkoMZlhuWT1zPnnOEP2qvMhIBvgPVd3e2_d8JIK42LXJosz-3v3K_keWU9F5LeNkDyEL-aDJcSFgJWeoH57I_qoIhxkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=RuQ8-CdjjoC9d7PuHhxoFqjlH_xtp6g2ko27llUhpV8qQPcKOGkoyP_wSUzgEkPDvIcVThk1jsitpC8ZqZxjbco8dHjcdE4u-wZ8z4jy4-9JPQQ2sMpGJ7IpSmqBjUE7LGzVNwag4suMoR1EdjhHSp3crwzErCDrFRA-awpi1j-JHi11G73qITeDSv84KjSk_lZexE6uUUDyz3-TuvilNo69PBDLkId4Q5TSL8K_b7vu2nppRrzF-69EFhIc6V0xXpG3kroKsXvXhlFpIc00WmzOvdLHiMP_IDRYc1zN37C-y8RcKy1QgzZFP5UeKRB3m4egd7X-OjH6SphiMthyog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=RuQ8-CdjjoC9d7PuHhxoFqjlH_xtp6g2ko27llUhpV8qQPcKOGkoyP_wSUzgEkPDvIcVThk1jsitpC8ZqZxjbco8dHjcdE4u-wZ8z4jy4-9JPQQ2sMpGJ7IpSmqBjUE7LGzVNwag4suMoR1EdjhHSp3crwzErCDrFRA-awpi1j-JHi11G73qITeDSv84KjSk_lZexE6uUUDyz3-TuvilNo69PBDLkId4Q5TSL8K_b7vu2nppRrzF-69EFhIc6V0xXpG3kroKsXvXhlFpIc00WmzOvdLHiMP_IDRYc1zN37C-y8RcKy1QgzZFP5UeKRB3m4egd7X-OjH6SphiMthyog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXsEFp6vSrYgwqJEua7GLndI6VnuCYZZx7Pb1Udd5ASz-PZa66nZ7KqUeHKoq0aaRxMhs1K_9yKXARzRdXFdegAlyDciTrpgQPOvvZun7hlMDZswBVC5kgQ3husROCuDlE_h8y6vtmDc1ftLiUsHtCsZVH54ldEZKg6MHpP81Yzkrr25XvYGsM8p0pBDtFvuY9sDqdsd_4BNqGgyasLhvudRAiTkLZNnZUgpxAQU7QqbvcZFGK9VouwwHKtf0pwOKou8OQEh5_QMSoWumUvDEsfPO7V7zzpjY6Ji6cdEeVhkEGOOz-bTke1jrjXSpb0_BOXd04oWR2mZrKTIu_m9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecuqyyPv2hQYjZcW7juavWWcKJyCATqMo2MH5hx8Cu6cALs43x3B3-piPaS0ImaL0xJjtE_A9-ucixxis-Qab21YYe_RvofabU2GAICE0mzvWb_EWWRDXZkbkc7OMruFgO93xoJT-58ZhLISoYMmxum4fHxs7pTcNjoSi-5gftm-cU7MV3cSC9KVqosSG9KVJ8XSrJBUigWmtWwJ_lKSED-tE6l4vpRS6Vd2-FHctq1-n4539EmpC3tXvueWlnj7UiATDk6oOS2886RkXk8tw08zm2UfEF8rVmdTgqvdmVgmEwZFbKK01i3YEGrmT00ARENwOrDlH3FF-GqFxM44-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6nQOPdZM_wn-WPPyb_WlmIyxLALu6WH5egDP9MwuMogIwOFSktSSwHe4KMDt3xwDcgKhej4h4sSGNjtmOYB-Iy2N-g7X6xXHc2lzYq-pH_eD804O4MV2OEsDsZMC1MYOiaQxw2-XBgiW59rFDaIhQXJke19e9aFz59UowzEUD2x87yLfhvQ0T2hyFEVwlR2O3cJr7MhFEDcH2iOAPZapVFB_v9oMxSz6Tv_Tuh3OGZRHyczY9oFHjdbXtmyZ4673PKLFvwzfAI7k9aQCNQngySGTJ3Zr-Vw0UJDHHz4BhdrLjUQcJGqxkJ4S4YPEkz_lGsviVs7-YOvmH24F87yjio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6nQOPdZM_wn-WPPyb_WlmIyxLALu6WH5egDP9MwuMogIwOFSktSSwHe4KMDt3xwDcgKhej4h4sSGNjtmOYB-Iy2N-g7X6xXHc2lzYq-pH_eD804O4MV2OEsDsZMC1MYOiaQxw2-XBgiW59rFDaIhQXJke19e9aFz59UowzEUD2x87yLfhvQ0T2hyFEVwlR2O3cJr7MhFEDcH2iOAPZapVFB_v9oMxSz6Tv_Tuh3OGZRHyczY9oFHjdbXtmyZ4673PKLFvwzfAI7k9aQCNQngySGTJ3Zr-Vw0UJDHHz4BhdrLjUQcJGqxkJ4S4YPEkz_lGsviVs7-YOvmH24F87yjio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA90E9gBXB-01-XUeq9XPkK-FqwVCfQlJEgpfb6Gt_AjgAn5-INu_xbTR86AFMEMmOZRx1JIl8fGhjF-ViPmFP1w6FJVmcn51r_f4umSTxu4fWxKfuWX1LwV-sdZc8iTbnV35GQ98V2VwW-TmDrPSMDDlBCH67dwp1Q8QDxDW0WYRWXFdCQDfXHUlYU1tbd9cXIDABSj2sm39E6ekzB1rlswS7OA5ADYE34KMh4snvX2Ffqb95QIeVXZOMb85DakxmjTEf3Yf6knQMS7A-XVjaRzHFuXxNaEFQNjMCdRaUiTKecJjelivzWDG7iIZZ09Ne-pqLqcIjas7VQ5ZsulLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=hb3_En3uqRiAg--_2aUZPqrE9oGyAcyxVdo_IubcmEnUCudOIjuQGyhAbPABOdMV87W0hKoInUsXyuwFRpT4teBajDnFdIvMUIHVI18Is-HrCq6pQtQyBM9WdW3HOO1o_maSrsskEYpWP7_0fLT_3gpHcS0rFVvDwBCrylEWDdURbsDVQD5HYasZ5KfsEP1fDu_cyRGQ3r8dfJTeDnTMQ3h1k4og1BihYFKEJ6L0jSl-_vJl4SdEeUGw_GdI-OMOJGusbs0r6Zk6PPIizg6iab-NvOvOuFp9cYxkiUmMFjoxkDYkH4WqBrf-o9x1oh8sx53ExDKEl_nDF1OETzTYOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=hb3_En3uqRiAg--_2aUZPqrE9oGyAcyxVdo_IubcmEnUCudOIjuQGyhAbPABOdMV87W0hKoInUsXyuwFRpT4teBajDnFdIvMUIHVI18Is-HrCq6pQtQyBM9WdW3HOO1o_maSrsskEYpWP7_0fLT_3gpHcS0rFVvDwBCrylEWDdURbsDVQD5HYasZ5KfsEP1fDu_cyRGQ3r8dfJTeDnTMQ3h1k4og1BihYFKEJ6L0jSl-_vJl4SdEeUGw_GdI-OMOJGusbs0r6Zk6PPIizg6iab-NvOvOuFp9cYxkiUmMFjoxkDYkH4WqBrf-o9x1oh8sx53ExDKEl_nDF1OETzTYOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSIVNabpHsK1Z1-MXkF1L1HKKSQjrtl_pcRkAr7EyEv-KbxOnEDo1WGfTPhTGGBMbiDIfxCY4JpWcw1KARJDEOa99u9XzFMXMpgoWa2GJpbhipo_1dQiK8-0_rqGhWF18jkJ-9VrxDl0vUm6jdJPusACt5nej0s5j5Dq3NP62JcGmqSlLkUG27xryOWWZP-od_AZWW2ssXVKce5zJtUVbKOcqvP3r2rZpKKBR5mZ1r9_qDDKRFM7DBDm2qimmXiJRyEPX8Ka2Yb4HQNm2ZWRLVyulGXFKKPIU-dgcQNgQqTSX5AbhKLow0nJ1fK_6u8TkQ_rAwzUeSW6eEL0g5e3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI9SNGrmTjwpN_BZhMHRahQ1LNFCj_HBZroPOhxP4_rV4-WXKN2ZuivKIeshcOpWLPHp13kTLwpBUkGDV4qoXE1LVd7w5-WZaVQEosbWHCHEK7uT1ATIFxfdgeBKmKSkPidzPoAjJvCscOsQJelBYQSfsujVU7tc6C_7mT07P-kQksYXZ2se9O9T7iBhQM-muVjaGa99ozq7N9e4nVmEJ9qPXojDaG21hy95jaQcBLM0xv15HqYn-qNbh-kcUdm7msnOMbSLV_MdRDI3m1ExQazUkytpqsnEGiSdfBpXpSmxqMtorzRHSByDXt_H1i339dXkoK00UwY7N4fCKEhwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNWWy0SATzYBYexkkdcuLGeC7jtm2eC2Ai8US4pKIJKu_p_JFxgkmWcREXPWSRzS3QOZhnZRdkGBJ73ZqhbazhhK1wCYWVnQGToVVgBsOanBjyb_IXyMble1BF9bSOExSyC1jlLdS-gO7FluwpERiY4kGd3CL6nenKpwXqCgQF2hMBKumq-5BRbKGDPqy8bYQzbKl6Crj1cbqJwMD3KmOLdEV6pNR9hhToxjem-BG1TEb-6B-Yv3CfQKfFRXNjY4M5Yw3JpOLYOkXU3WmAc22pjtABbdHDE8YOTrzF18YPE_eDrfX93GUG4HtfZqaz8MwW2caGA9y_tYcb5NXGJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xd8K7G3H1Ix1vMUGu5e3Llcekp6-df-ffc1BR4We-w-mbkVaaSQ80xJAHp5q0k0yneo6S5uyFO6xXKhyocaRSRMxQExiKUaKmQiqrCPnsEhTjpAWPiviwW0eixGtTxiZ5ujAHKITdxiWGcSIPq5cRmkGJqsMcMdhq69CrrTr_LYBBRif2ILV1RDpsMulf9Zc3EezAQaRxC95mWmTynwJr8Sj1_oDM-LSSpoJCZOPnpeqyV8i_kmKfKU8kxmuKsDEcapTCYB3kWC9PfaxpS4AHBF0vf47Lvt3uZkn4W6Xpy9l9OMy1ERJG-hZAcjtsWpCabaIsMCMeBdkbhc4Ix-I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xd8K7G3H1Ix1vMUGu5e3Llcekp6-df-ffc1BR4We-w-mbkVaaSQ80xJAHp5q0k0yneo6S5uyFO6xXKhyocaRSRMxQExiKUaKmQiqrCPnsEhTjpAWPiviwW0eixGtTxiZ5ujAHKITdxiWGcSIPq5cRmkGJqsMcMdhq69CrrTr_LYBBRif2ILV1RDpsMulf9Zc3EezAQaRxC95mWmTynwJr8Sj1_oDM-LSSpoJCZOPnpeqyV8i_kmKfKU8kxmuKsDEcapTCYB3kWC9PfaxpS4AHBF0vf47Lvt3uZkn4W6Xpy9l9OMy1ERJG-hZAcjtsWpCabaIsMCMeBdkbhc4Ix-I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=fZpQaK8YO60CD5ZvBXzIiwfqO7sKoIu8Ur2KznCLuH4RgT8G3sqiXJ0sl-h7h_V1nvWaokBZe1ePDcjt2sziRgjlID09utq2pcIJc-Rg3lOcRxSkK-KvTSwLyWGotFOtQxkilVSQn1TOEE4wvBMvKrrRduMJgN-4L9j2inSrdymzmlm2salVAJYdDer_BjcJp96FZ8eISZ2zUL5cceP1rWFaxWGwy8TgFX26X9twN7FixXjJOW17EsQdrbyBuRBaM5Zk1E0BzS1u1UC_cVCtcHA-NFcR2qnsr777sE1Zy-b2GgpYo2eckosSX22HTq6XxlJO9ooEHOBV01ZS_Ki3DDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=fZpQaK8YO60CD5ZvBXzIiwfqO7sKoIu8Ur2KznCLuH4RgT8G3sqiXJ0sl-h7h_V1nvWaokBZe1ePDcjt2sziRgjlID09utq2pcIJc-Rg3lOcRxSkK-KvTSwLyWGotFOtQxkilVSQn1TOEE4wvBMvKrrRduMJgN-4L9j2inSrdymzmlm2salVAJYdDer_BjcJp96FZ8eISZ2zUL5cceP1rWFaxWGwy8TgFX26X9twN7FixXjJOW17EsQdrbyBuRBaM5Zk1E0BzS1u1UC_cVCtcHA-NFcR2qnsr777sE1Zy-b2GgpYo2eckosSX22HTq6XxlJO9ooEHOBV01ZS_Ki3DDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGLGnPJsjgILNOvEWOANvx1lwEwD1XnWzK0mf8jPTv4rWipQWB3i1tH9o5h7KImN5-2M_dV6JFoqarkkdTvS0K84y4VMJXZZibbrGWLu6WiOqMsH5VW0kIhD2MROApfgAsHWb-mOW-6ne7GueSHO4WlSiRY5rkxxGnuaGC5viQXaVtQNM1H8RWlxl97GTzw-Eb-5X_8-31AfnhFdyWK9vYwGXqlvDp653G1iKvd6P83fYXqN_UX8lQ8K_wx2OmBNTaVrUVXKgrzvOk5fs_IvjKZh8uwTHRryQ2R8e7aLn6DbY09wmMetzvOAn2tbXnpHj0kIozuCMTVKENNFSctK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=EEiqmYuMJzUCQ_-3RRT9JyxAdCPBQjky5OTSThapb9spBthYirQkSA_jEjs6Duv0w_npUNzy8Nyied6ZHCkvj_9yZ6anFh7FP4bFBDIrCDsVQxBdbSWaZOuklGa_tR4vAKJdX2BCzpPeC-zOaRsJ3d8ZzsIE-ldQZXBwhemSQdpOczpS6S1SnELKm5Is1vUMZ5qwdnUfskXcHlRf8hfFu4WlLuPGag9vEbpZIgv_xqwT8WQJRywsvGAhFpJ3-OFESn2arNSueCny7J3_IgX2XdbSs7NNoS0SK9RGZFXXQueZDHpuSg6AT5d9hi2cvMJNNFpoLTCyD-LQNJR3Mn4Yfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=EEiqmYuMJzUCQ_-3RRT9JyxAdCPBQjky5OTSThapb9spBthYirQkSA_jEjs6Duv0w_npUNzy8Nyied6ZHCkvj_9yZ6anFh7FP4bFBDIrCDsVQxBdbSWaZOuklGa_tR4vAKJdX2BCzpPeC-zOaRsJ3d8ZzsIE-ldQZXBwhemSQdpOczpS6S1SnELKm5Is1vUMZ5qwdnUfskXcHlRf8hfFu4WlLuPGag9vEbpZIgv_xqwT8WQJRywsvGAhFpJ3-OFESn2arNSueCny7J3_IgX2XdbSs7NNoS0SK9RGZFXXQueZDHpuSg6AT5d9hi2cvMJNNFpoLTCyD-LQNJR3Mn4Yfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FanKG87UmUHKD-Av0rPyKuRWafvtY_O0mII8CJAelNplmtMiEaoIzCQ4OzX4_4dr9hd-P4T_W0NSZh0K1dWR15uUfmzPAlSGEcDktO-iott9hjsH_KlhQPLi6oN9rAKggU0Q5UutHLB6xYtJDKtWhIYRC9kZEmFHnePTKkMVb4kX79Kb9t-TS_VNkJLIwg4r3WcBvX2A1uHo8iJRjW0tjV3gYrvlCWgExIegrtrzqhjmbDcMRsGIPa9HU2NxwlDzEQIW2z67wp5og574hcDquxILSLxUohHT7rR9UBiW8JfO5Et99YZYxVC4MG9UEKv4HXBXnd-FrOlY_HLu6MX3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax9ZeuN-UsYpAcq-b40840Lj2rnlSum-r65jVgfRBHC1xOinSlrPNSEDnRID6nEfVI9FyGPykELUXbG4-iyGHAnBdqA0YvgVhmb6KI9MX6rJdB2Ig02LNkDh15oBc8uhEuLtwp4ZABADvGSJmQDB541f0TMYNmA7C7mWhI6UpeRNMMGM7chSXDoszDwVYAzIbjHcvV00Hxorvi6IbGL09-RLadw5ee76QAVtZNS9hJ3qc6AgorCoXkb_Z2aYbEc5k6GmLAgY2QZcwAgQbLpP__pbSrUuVhfcK6vI50TEQCMmncNwx4BFIuO0tTYPJQHuIjO5U8QGT_PmVizt0kVBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsbF6QW-wToEdGUsczpx7lARMfCsQQe0R8pTbKoBmIpO9yWb0MooCvST8LjnzmSYGRX3wIN9XxTrsQ7jJUqx88YgumXeWfvrxCgjulayAr2zIa47p8P7avjZjIPm9-YB6vkwVTxx6lm8uHfbgGmhq3Zf3uKxY4z4aHcTrt8w6igCaACz4o4oDSPxS67n6IxAjkVWx5MeUh54ZCIPkFkgmuEs4G0xyL6uCGxkvgZrqLO8aX1wgCOESrdAYAKTvzMTasGBSGZGKhzsunYgAlo9r2xKkQwH2UwK2chYIuLN2VTIuPbiB89hxGPdpRkIe9PcM__GuboBMuY8Qv1VGe1eVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWU731k6XDUIJodQBwuvyhROXZr5u3M4c2AlmJIopM-lNKO7slv8ER4MBPH7o5fNt4E129zpk0lpZ2q4Cd4_isygBSGrkYm68r59XUCtDvAgRUw69zZpd19z-xRa1gefbav38Rj4bFAsrbufA1qpvH0adPLxROKVvt3qEsoQylig2XahWPSjhuTsaoIujdQ4-gaSSnkXhP1mPxEB8fUP457ZMHWkfRkVbPxBMEO1lgAfE4G6x6TJY4YHdSzwsicQpBpT6Jft9-0zVEb9zUIopElfJNn8MT34PU_KRJwCfiUrBn_JMF-0eNDCRNzogP3S25Wc4NEdlLwhhYDA_aFmJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soaPa8rMmK8kL0Nof6PuEI3wMgamRq5oQTGiDr5zi_--dAvubybJ22WmZTnAE1SAQ30GIqC4ufOybj5i0h0NSODoOmUzZbo90jg5V3JOtkOzNEGjD2sDZ2T6_SNT77-8J7YWuY6Sif46eWR44VNd7HrIp7wgZ7IGIES8sAAE6nXl00ix0DzXXNykoFxnYLkxfCiNGTfD7Q1yr6R5HWFyVxQRqtQu-3gQVPuHoBn7-89LzE7Y-WjFWPz5pDURctizpCDjDrobDzq2PQZHsYiSUfCbtBhuIr2qfucewEMZ16QaTbpm5hAsjfkKHRiBykqqyX6q3RA1nAE-6ER0BVZ5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7uP8Q8CxLs1DUBviGPmJRIu3vUyTJ0NHHkOgbcGhN9z7OYKdmdMAM8DNcxXlKqz6iCHP2ICCgDd7RiS4AttbS7mKf00MInkXVnUN_15jvjYhRyJgBYrGe-_jQEe3J86dirhqmGtcmwH2xS6ooZu_wDC9VPZ3XaqZSWmEEpiTOEJgtaROEUiC479koETVEJlwkvblPr9MDg8kOkxBz7R7rbt_7oU5MlkDMlvbW71pAFVbdRXyQiuByj6Un8k6WwqoGZb0vkHrh7nGJWmw1t7CII2Hog1_QjgGROpxu1cl67Vjyf1bgyUKPYw3UkgoFppgfu5kAJwzJ2KInnrAbm6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwfPnQAiTYLWODoMwg9Nd-Xfm1rsqAbkGM_WgwJOeDXrrFurdsxVCgh0YaDqkNijjt2MgEQBvVZZC5NlmLsNhSA1U077VoVImZog4vvcmEqS_VWdrN3D6fF4Glmykq2tZCAO7iqpEmcyTDK_9eSUMA7heIe5h7UQfoweL-exB1Riwker_d6VzBcoyAujfTpnlaNC76XIPdu1TIDuUEklfMbfoEANul9ax1lxeGm9iIY60dXkpsVoimNEIf3WMi0Qnm5int4d84L939r2PAMSNXuaGfBmtXnWSjmvxIBxRv1p4WN51Pdm6rpIvMCMDn0ryY_Hu8ZEuNQva3Qxa-fNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXvKuq4bdnEbUObVKVwem46FLNypvQK68y9OrZkX44AKkCN1CnC_lQ5zmgEWeTIcbP3BIOJjBQ37kr_SRXvVyQn_aU06Dys-_miuqySK_CJ4gDxICLCAjuTUWG7ccoqhyxIh8hln--hldH9lEh7Ml7OpWj-OK4Tda1t-eXH9ZoURmWj5H4ecFGvATWKMuJXY4BPUFzdMn1zs8eBYoxdangwzzSKB16zl8APlGjUccEHHVKDu8JBeM1zZG1O9WM2trnJg0QubdPJ1KVhZG7oHLC4fAzB2NzLUEj4Mzj12SUT5p7GsNqLjQoFPogjk5hZkIHaZSjG9kIXcxXOI9JQeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN9ge1IsHEtNqPzxeJBCVYsKoYXocCo-iPjlHerpdole2dZE6-nAXZeY51Zdc1bJixj-NJo5cWTEPyL6v7oEn_N44ajyibskqVmnFwK8G7NlNPTnUSAZglYTXwBWzRt7XggDJNgFKyjbhbd0d8B02cKrM3ER1adTW22WlZiK_mVoWdS_bRVZMSyuRrM6BUz2vS330cnokyWV8ONmYv8jzlRLRZt3YS06bFxhwLtEyZ7jTZHxAEA2noKVD8UJNkyJCtfR0XW9ZyU8Q5FTVRvU0JVMLLeDkx_YDxOsZtklNyDIPMjkHD5BouprHqc7v679ADRHN4aWziEF7E8ShLbT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBNySZQMCE3NG-tVfwegyjTmtL1RcJUVIDWmqw3Fwn11C_S67nIi9V9idYzKqmQNvGcQSoTmRp2IvXJ7JM1O3143HPrvE1jNjCdnD-6hQiYq7kXQgGLHys-igusx2IVPCuQdVGWCPYMx7WCea-lcIxdTH5C-Nry1SH3MKV_3YQzg3WLSZPNrnaMCIr5F_OIgWUYWSi8qKda9eAlBEAf7nqv99BX577RyWf1z6SiHzm8Wov-k9O8JCaQIalTjM012mLgDSAwzKVFtH4B92p08aiJbkH5Z52Ws5Gr3zz4xdavXZhXb9RPsnbP_nFPEk7y60I4xY3x6Ukt___ySaw297w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LySM06ZMoPNV1EUP7Gp78YewRRtflB92T_N51NFYIjomP0oAGw48OrT7YXCDVoaLxSM1-ippSx9N635Iu__KVclJCChalQHu1URdazySdbIEkHnW051iNAB8gOrMj1pqKMhDQHyDMV2k7l3b8mQ1lEuwiqX0ymC0GE4_daEeo34p2nRSEo7_NW2t_cpFygG2lNphY27gEUw-xPAOusUuY5JlhhIdHr6LpRWSIuflIrjwIO4UzvOTluGO4R4jcvb1YXRcTNHGZtdBdCARKjAbPJ1fULbcYFPsqYzY6_3BPhOwKJNz6YZP6T3T5N8duJVJ1PU7uxmLZO6JXw4-ksEUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=HGMYKzdDIDEqzPtFI9M9OJ6pL4Z4rTL3S1XoI0XD5zEMpfEAvXdqR8s4EqMIOOy4_4I2Y_Q9eKzEM2-7mZZ-9gThKB0bwezgEm6N2UfFZO-irLBMV5cyeuQXtW_Gtb3Im_EwZu7uNdEw7gKApZ_DPVWX__H2U6zha_kGWRm-HYg0zy4GU3YN2dECCrNmQCW2647cfLmTdM_VTAO0PVgWcsd8t2EIOW2m6EaqlOn8Mqlfl2puTr1ZC8c1r0l9oLIcEfTq99n__CTWLwSEKUo_fjU9NwtuyRY35fw3uClBiIKgdkZvFCj6RskQ7I5boWqMVBmRnkpItFo8fZuESYVu7WT5CCBRBf21V6i2TrjYH9SrQwUWBkNa417ZIzSjQ2gZk_Y68mk5pBBv2gLVaZt9noTSXXG3YTziX15e2ORntyH1eJwSNJ0BMj9goX5tjDajkZbwWQjzyAuileSwvyc4TsqnYDWzBVlMkOSR1KIVzVcmHsNJH6Tx--xqaQ1ILjxxeCwt7fiyIWGcb4HQukhiyfvo3e1Jqzgr-bqlTgxOtrjknDe2dh0MZD6DX-CUFGME8-RdcqqEJVuI1mAgoPsZtdYfQrvWepv2HQ7rdyfHUwFHrWzkdSrUyBTh2u0o1S6eDh0homQOLbuUMmbulMcDdDNv7gGQgn17WXUVrF58hYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=HGMYKzdDIDEqzPtFI9M9OJ6pL4Z4rTL3S1XoI0XD5zEMpfEAvXdqR8s4EqMIOOy4_4I2Y_Q9eKzEM2-7mZZ-9gThKB0bwezgEm6N2UfFZO-irLBMV5cyeuQXtW_Gtb3Im_EwZu7uNdEw7gKApZ_DPVWX__H2U6zha_kGWRm-HYg0zy4GU3YN2dECCrNmQCW2647cfLmTdM_VTAO0PVgWcsd8t2EIOW2m6EaqlOn8Mqlfl2puTr1ZC8c1r0l9oLIcEfTq99n__CTWLwSEKUo_fjU9NwtuyRY35fw3uClBiIKgdkZvFCj6RskQ7I5boWqMVBmRnkpItFo8fZuESYVu7WT5CCBRBf21V6i2TrjYH9SrQwUWBkNa417ZIzSjQ2gZk_Y68mk5pBBv2gLVaZt9noTSXXG3YTziX15e2ORntyH1eJwSNJ0BMj9goX5tjDajkZbwWQjzyAuileSwvyc4TsqnYDWzBVlMkOSR1KIVzVcmHsNJH6Tx--xqaQ1ILjxxeCwt7fiyIWGcb4HQukhiyfvo3e1Jqzgr-bqlTgxOtrjknDe2dh0MZD6DX-CUFGME8-RdcqqEJVuI1mAgoPsZtdYfQrvWepv2HQ7rdyfHUwFHrWzkdSrUyBTh2u0o1S6eDh0homQOLbuUMmbulMcDdDNv7gGQgn17WXUVrF58hYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5xqsgTfvG78-NphGPVI7M7XlUiYmikfTGsdRPnLrsnO5gYtxwEZaZVoyIsVOh0TNyE7hmMZo3-xcTJYE4_sDxgzofyXeFy-MCWVzZKwFua6dou7vP51-tZ_s6K8oM6WF9TR4LOXV1gaD57kNMV_8f0is7U-0eD0cXyCFuXyHZRp-TX9ZK5_nKVvb7pxeBpRDDnAGlipsG0JfEBOAapOUk4DAmxNBjimkbly7lXxabIDpTN5TXg8gjQ_hCpgd2FDyoOHqo9I8I1YltjHdq86HIpqJEPy5bshiKbubc2QxNuxk6wj9_vSQA0Va0nl6FOIDUQE7tQ6cL9noCKKq8SUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBtdyRi82lW4F23IHS31wL3LvR6wgi8VXgDvX5tugyF1UHiK3M50yx2WFLGHM88yPW_wkxT4ob8ZWw8t0YPCVJjQB1DQPc1dK3C0x_z6hSAPLFytrl0AgsekBe_TpXojWMdujyiZGw9gYde7GjOyr56JEzyH5kt7BBQ8VlPrQQeUO7tlILVEnUl2HILTz0NTo8QuLEmaeV4tWxB_zYQT6ZBi2WZKXlhYDEH4snQmKoMuKJgAaDU8KvSSxpt6plqKwI0ASu-cXC3HObIpENQ8lRUDLouIs1FEbJfoh6VyR7_ulfFgzPrDNmO5F-WfT-qusOgy7D_UCbulj2wMhdkbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=HlefqiePnzUpDDRNPoZHgocDz-7EwW6D87H5qBKS2S089GsMGrNjdpdGmdy5_r3E4YVjM7udfrSpCdCGWbO-ff3pxtaN8VvxykXw32b1Ln70xGSKlDohq_CHDBlv_4RSnYvaSXAu15e8ec78su1IbuZy_XTRnGYEo7AOIKf_D5wQc_4IHPpQPhTSK3Gj-RA9eV9PHzTEK2ZVhbjBWDVFXCv6FH-85ZyepGtbgYjgPxtAAbfSMg1aG4pnkOS4nJB-tOE9Pb9gupCxjmEMym6fpzacyQq7FI9a7xFjCiosX6x5wXKXSSwJmb4EhZN1-CL7SYpnHrdNTG7KlevZCigsmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=HlefqiePnzUpDDRNPoZHgocDz-7EwW6D87H5qBKS2S089GsMGrNjdpdGmdy5_r3E4YVjM7udfrSpCdCGWbO-ff3pxtaN8VvxykXw32b1Ln70xGSKlDohq_CHDBlv_4RSnYvaSXAu15e8ec78su1IbuZy_XTRnGYEo7AOIKf_D5wQc_4IHPpQPhTSK3Gj-RA9eV9PHzTEK2ZVhbjBWDVFXCv6FH-85ZyepGtbgYjgPxtAAbfSMg1aG4pnkOS4nJB-tOE9Pb9gupCxjmEMym6fpzacyQq7FI9a7xFjCiosX6x5wXKXSSwJmb4EhZN1-CL7SYpnHrdNTG7KlevZCigsmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foeaVYWuzeSgDS_del6eD_a6w20dJbQo4MJOZ039YgY59UrBIWmjWsUGd_ng99T7TYWEr9mL6P3fiA5PRSbYgswEdz8CocnRNl59zKrAfJpLZbnlgWFCh5O2Ycgol2qu_asLHxGsxE4xZCYuS2emSj6Y6kvsaU0dWO4JvwhIYZKPZc9YIzYCk-DOx7-XQHHJGyofYyBgtFmjvSjsJlcSNPoO0V0lSxDZgV7LhcVwf7LMPp9cVNPk0ewkDjOUl-XWT5qKpjuY_hPhC4BvwZApe7h9DUerZPttZniI-meq1CeQ0jmdKxe_rR3VFlAQEPRPPzMXUL5nh0CZ4COaTwt9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RW1H9XkRuR8JeuhSYsicQHJ8zARxIGvBEmoHmhe4e61mhVyVqFI4ZY9Y0pN4TkEUTXLUyzaVEHX4QpjRcvizTm0lyeX4YWCGS97A3Jnv2brqVVNVs7T2MM51I0ulsl2RZDbjxKhzSEG7yocK0X0-dbo-NgQwfFZsh0UZgJVkhcVMZo443rCPgvUR-tVXNOhriyIh3tCUHoWcuoWHovIwvMQZatteuyh7h7MlIoVXgzDCZT5OKTjNt3mcxvohRtQ09aFxZMNJbWZTywHKz2CUaVgEPG-ISxP4b8-gzMEjfrO_3PdmloGcGW4Ta0lVc9QGiGMkqxRWboTytpAqxTqiKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm1aPzSxuq4ASSZMK20c72s_Kn_ShaaDa9_9eCqSArIQGj0c9CFhYe259Ez4gAlz-NMIBCJqtrRdNXsUXS8GVBpcq29MDKYuWGpgffGJ5iRJvkhtrbhp3ueZLpksaezBQqjzTf8gJpSon4wXhZg6jONspJYe7v6n6GmJwoVo-Riq_pkeFzWk-QF5wcxzAcIUsyl_V0ZydS5neMbiWnbJ8SwGg7lUhBLZ3W0TSncvAuwykiWmDsU6k_TxKS44y6oQpJOwmxD5dmUynkw1QRlluyfCrwLHKy0FckcgswRpV6fH3HX5pCG7_eiLCAEuBNC3MeY1T5xllxo3evhv_TLf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMsqDQ8aNZ9ebtRS95BYqYvvq2R_TPC_sj7K2XvcBla0W5Qmpa45S4pzDODIxLAa3RAdDFvEc0ixp6y-4-XoBIsufxWf3DjKheYHYZztzImX7vvRI4w5dpdDEQreLyH3pNlCxT_hXYVSweoJFP5jAo2AswgracTnFfFBh2WsTO0jApTuke4Bb-wtsHzItkLs8rtd95Yp_rkp-TbcsYLECNHbfldb6vyzU951mgYt5K_M_vuZk2mZEqLFi_bwkrWWE7HHT1diLjRbnKg0xKtvj4nPMI1w-8xcsXuPN01mZGasjRt3hpXOkZcfIuzuek7WOAzVqlJA4gejjIwckBWBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kddBI6t33BVSzw4yiTX7-q87fpgsfKVjAQpJrKUuRq7sDPF0FDihIfye65tpKC6HGwtMqL7-j7-NPv7RlpyYqwr1UA1Yil11loYY5RJM8HA4kjksHhXOMk3YEQWfn1mpMB2g0CRbpL6Fpfa5Re3A1xRCCQ3fKHk-8vocNLVICE4jSB1LR6j-RHCnchPJ1HjOKPwIHHpFIJJVRJ3QG4AxEZldkNeL4xRWgG4DokQI0h5kaItdqwBEaQwy3GVVwd9MVRGuaXAhPF1_rr-TBup5ghR3ZAKmbVJoZg3OOZ_UEA4zmF_CQHGOX7frkxoeY2zK44ktbkH7uBBoSLAjsquhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gig7R9kV6PmXJiErCwEF0ims6LgxY7YlJ05LwNDd1RyKTprWvXNN77z5wubjq2kTBuIdwOSF1MgsD3FUC8ngTHI72FNo3zvNsDq7kZnrVgp8lelieDigxHLtvsoh_Xu-bKGrLK4KoIao9WMUYM8ofGkIRh_Nc64Fr2dcF8UQNp5953o6E33Z3fxI57JSLZNaV4EHayfG0CfDXWNqldldD3XicqB6H2m1UNLhZLPTw6YsU1bqrRlOZ1TVQPyOOM79bOUUmDYb7vFfwQixX3jiK_i1lEqUotNmunz6ZXYXSL7115vk4azJd8F3o5VsxOzy6Ch5UwRoXwJKGBr1ZJll9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLvE6lJlVzPZFo-WbQEHa7HrdO4Uj_PUM-7cW-SLboju5qLCwUWIhZwC4_j1duwP9Ks8wFhxy8YBYwBDjyCsb7lKf3DZuhNOmPUIUlR_ryMvYbbah2rYGazHVQ8vpVVT0TUDoA2PUi210SlS5DRLKkomlWwLlpdBK_U2pYKEfVjXzZirxtZUZCvZIZuaaRhwDbq_OycUiJXrD3sz8QaQewIwneT8cFsL6FG2jpqFyH3Tr-ubnLovpeKdSmtoOFIsPU8gv_gJUF04o4SXFeZwyQI_s29PUQ_kJvbfoi51SrrufXvXh9cfmooSVUHWypk1O61O_T1GkNbegcRUG13L4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU2cc9Ltzx-vSe3g0Yvt0gQWSUIRQwJegVDXpaOmY5y6EAFKEnhw3nUWGjZ3gckFdye2RBwpk3lB7ke-VJqkFQnvQIkn5HMBuSJfnL3SF4RRwr8TMP6t6nGLUYHh4QVkOZ44gwuJJolZ-1h0kLA616e54QQL-ka9tc0_PakHVRf3x-6VrGnQ8OnoaAf2HCKDlF36urrlL9ZwitlZs6KgBwgq2WAGuG9L_bv2p5sE7xa-c01fq9ZcT94XSXH9v4BRCWD8tRAWYk1Rpm63dvRCmx1J0r3p9ZObJTXBXe4VNOL2TCxPbvEsODiXvQ3GFhKf0lijSyqn8j9WUIoVO1xZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=Ip93q_c5x6Oqrp3GvT7gy6J2pWZ5Lqshtowyt_dJWT7QHpmEGEm1El_FopNp6AqtYXxJEz0Nesnwr6NcR6Ygo29OGCb2WT_2g_Xn1y_K2fpc74NB5M8RQlX7ShxMqc1UbIw2vwEe_a-3UVKTu4pMQyvkatgoY0tuIS9FMfypSZh7wvV_A0V-UjFD575D9_iKkg6_IHbX4_RJlXKEzAMGyI1QRhHywkX-y3eW2K7E3i1ImJ6qaZrqbxoCnagFHBksSnDl6ICLtT7tPbRsWX1VX_Kkk-x70EgsRoUI-ve4TAaD2zPoODaqIdxe9jIDY6DYIga9evdspLdWaEIRDF1ETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=Ip93q_c5x6Oqrp3GvT7gy6J2pWZ5Lqshtowyt_dJWT7QHpmEGEm1El_FopNp6AqtYXxJEz0Nesnwr6NcR6Ygo29OGCb2WT_2g_Xn1y_K2fpc74NB5M8RQlX7ShxMqc1UbIw2vwEe_a-3UVKTu4pMQyvkatgoY0tuIS9FMfypSZh7wvV_A0V-UjFD575D9_iKkg6_IHbX4_RJlXKEzAMGyI1QRhHywkX-y3eW2K7E3i1ImJ6qaZrqbxoCnagFHBksSnDl6ICLtT7tPbRsWX1VX_Kkk-x70EgsRoUI-ve4TAaD2zPoODaqIdxe9jIDY6DYIga9evdspLdWaEIRDF1ETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpzIz6sgxlDmkhgi9hvZHfUUKpvzjhndt23dIDNw6DkH4Egn5SIOZztlsRrcEGCixB2_Tncqr6mKcSbUKaNgw7Xq8zZxktVM55KMs3RtDDpK5Aa6lfQVd4PjyLEX9krWseaOfQexSCOfdAQicnMg6N_luzwQCCRwjhfVhzTJQ4DENUhGXOhnGACnCaomR7BoaSiF32nuKy2fajaSr9mPayzIKzpE8ItYRJjGu4IAEUYBroK5kHmWGgn7NLRcVTLdsGeo4IvIjnCFsq3dvUGOtB9uq3CZPGKJpZcys37rqSNDaEjort6_XOwAosHnplcWPI00JfIpp8RpBG-dB_aE3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=Oo5jusbSW0RKyqDbbbq-G4flnnnX7rZzrdXaX2y-aw788rtKcZt10UUWeOxeDozlqaKbc_FbkRIhM5J86zuqqQ68O95Epl0Z7Jcks6vvLadDFBJlqVRzFJlSexsnSVIncFCfaoxO2KxVVpHPW7wUvHTujmTMfrHMsoqsvfF8HfyywawEefjEFaqJAI_mVpcvIlvnIyjn2yHAnRxSPC8LAyWh745hxBfMizWx8CF6-wSzD3Ty3wYXA9alnpmvk4aWL_KHhEtvV_7DyffmfxD5V15lYkiiiujFi6Oatcw3ohdH1x6_ZSSyGhm8iVxO_kmL4L4sbsKcwJbqj7-sbIT9jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=Oo5jusbSW0RKyqDbbbq-G4flnnnX7rZzrdXaX2y-aw788rtKcZt10UUWeOxeDozlqaKbc_FbkRIhM5J86zuqqQ68O95Epl0Z7Jcks6vvLadDFBJlqVRzFJlSexsnSVIncFCfaoxO2KxVVpHPW7wUvHTujmTMfrHMsoqsvfF8HfyywawEefjEFaqJAI_mVpcvIlvnIyjn2yHAnRxSPC8LAyWh745hxBfMizWx8CF6-wSzD3Ty3wYXA9alnpmvk4aWL_KHhEtvV_7DyffmfxD5V15lYkiiiujFi6Oatcw3ohdH1x6_ZSSyGhm8iVxO_kmL4L4sbsKcwJbqj7-sbIT9jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pPD52bYorwJv6TRNO0dithD4ywficFe90UHN3qE3Y8LlJICQ6XoOH7sfIjsjT05HpYjcswKY0HhliThvbJRYTPt-IM6vevfzdfPZ-bKVcDobN4LBDauRAbwByESSLap3vdIe7bt66EbeFoNG8thMXSRFhtAGOBjDPbAzf6VG281_iQUtBf7ZaH0782tyHAlFLpuEBw1cNbDBj7QFQlb7JhjespqgNvobTqBWqIc1sjY3jj65y9rHJQ4SVThU65mDqhzhkx2qgo81wPIWYNBXGRDyua4xyxTzEGHbrWFNUhTbDWuO2BJA03vJKnhrzbyLMpLtbuNA_sY-T2Rj32EFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pPD52bYorwJv6TRNO0dithD4ywficFe90UHN3qE3Y8LlJICQ6XoOH7sfIjsjT05HpYjcswKY0HhliThvbJRYTPt-IM6vevfzdfPZ-bKVcDobN4LBDauRAbwByESSLap3vdIe7bt66EbeFoNG8thMXSRFhtAGOBjDPbAzf6VG281_iQUtBf7ZaH0782tyHAlFLpuEBw1cNbDBj7QFQlb7JhjespqgNvobTqBWqIc1sjY3jj65y9rHJQ4SVThU65mDqhzhkx2qgo81wPIWYNBXGRDyua4xyxTzEGHbrWFNUhTbDWuO2BJA03vJKnhrzbyLMpLtbuNA_sY-T2Rj32EFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USQQaFrieBD_MBCjJFJscgQ0XI1NBem7dJJT1JJc98qEcA8ppJ_Rzix3XrKqLw8fEZ2Mmf57B4t_8wy8k3tMcZFcoXGGrXW7XkPszfI-Fyt1KfmcA68k_BTgms-dC8GReRELyUGkyJKcdueTkeBk-uY5Q72b_46HcPLEIS89nio8jslNfvZNShVFra0Dxd8stcQFLnbTbeeErSq-gv1Yy3LSY2ek3LPap0FksmLVyoYO_h8kXB6grGJf10n92o32dOdIHcNM_d6qB5vrWeeY6_Y1NqI7-AFiIsanwmDYZZgHfSRscejaJSPBYt1sLxjXgTy_gMmjLRBg_CoCSkau1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=iGTjoDJSoAhOUoN-bAMGDFoGYXmJ9_NFZDQy6BfRy6kFZN0ObpXfGRVekm1JQZ_cWbi3BtpM1vPewjgA9J7re1ISoiQ3dC0aPmjjQtUuiavWnjfL7x_yEU4sU3e9Jph8c6q0cDQTLbiu4fVZt4B_3OfNP07AO75hMfLbHpQyMnaJuOyF0_bOuRBrpPqp272pplArx2nCdZ-NwZT-RrPcln4utW8j8dRufZRgME2aNCZNc3X3FKGyPwCHcV98_b_hfXGSrl4TcrmIW_5k7cO-32hfwUEnxABW7jn1eBzq_a01hhJ982NBJ5v1wnAgJSRJyJd8MZNShQuU8RoyWHQngg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=iGTjoDJSoAhOUoN-bAMGDFoGYXmJ9_NFZDQy6BfRy6kFZN0ObpXfGRVekm1JQZ_cWbi3BtpM1vPewjgA9J7re1ISoiQ3dC0aPmjjQtUuiavWnjfL7x_yEU4sU3e9Jph8c6q0cDQTLbiu4fVZt4B_3OfNP07AO75hMfLbHpQyMnaJuOyF0_bOuRBrpPqp272pplArx2nCdZ-NwZT-RrPcln4utW8j8dRufZRgME2aNCZNc3X3FKGyPwCHcV98_b_hfXGSrl4TcrmIW_5k7cO-32hfwUEnxABW7jn1eBzq_a01hhJ982NBJ5v1wnAgJSRJyJd8MZNShQuU8RoyWHQngg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piFB4yCseDmO-zj7N1ZZZSURFAe524m31RBT3RXT6xrcHjMnJIoXBSEl3WIKx31TKf1JItA2FE2VLZr5J1xiLrM_S0fdLwt_dfS60r_iJt43LJYAhsJBinhmDYNlzD-1gxEL0zHMwd9vEjlABZ2Qc47OKP3wupZTM5iMWXhcUgUNAcqOYvPMgC9mZ4XNdjabGRGMeRxFSu17fR6ujGpHjOuUxB-WEnT95r7cprk8RpeoGzNuKlxWTxN17MMjQ5DjYrpUllDqmABYs76N4LQkqtGFL8j65FKcGCr-WCSv1_k3svKLfnVqI8vdR-C7AItf7UC92yGB0b5EnApjhdTTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQmEaKTCsQRWfzFY2mkjwzVxsYoTnSQOuF_VeCE84jmnhgI9Y2Wi45tZZLFazpDQdXrsTiXV2whYnVYsZbtu7etRRTW-9KVnW6QgVUh1GlAwqM5srhct3oswss00VNGtuGTiVok1WqQWa3yVz79zsGxiFUOu8v-MaXkoq2HXZV2MQYORNOZ6V10IU6Ja4-L1aOLkdvXUF8HR1OIYw9kkVn_Wp4oxmlGEhTOru22UnPIMr3qjnKGav8rvjHzAtbSH4eOOgvVXB2k7lqtvBtTQ7ak3Or6MQ2_h3HDD61H9MxK_sfeK73X-RxzrW_RWyRPWn_jGKj9jxl0XqVdNz4B2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlEFgfbiges_9ng8RRDC-u8ZVqD28hH-2yAQ3luZmnimnLAtgvaW0Hfbbts-y7B5haS0t9U3zw-SKkzVXkX9uD94ZKzDnXYJELgMHbva3-epkqUQvNiLn2NQXp0PxZlWZ-5HQPewB0Dkn1wQEoi_Lcj4piH6LXmk42PxHGtDNZs5NosvVjnWLESrPD4K6qlgkvB-pgu1jFQxhVtfXIOYotzolgun32HEIu1s_9bViP8ZYu1GcNJzItYVEdPf_H9EEl99Xf8Ds0cki3XA4vlqQKFAtExwaEysETtDjt25T2XTfucJLXRKyFqWLSmOUPr5NLJRw8zT57FgRtUetf2kXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvXOuY-tc7MwC8Rv_-_L3q1rL4cVPmslRia25NnIpD6bUOqOFw0jRwDVnp9VYW77zsRF6JHge0s_-yrLRry_OpWucPFuacw9FoxyipXXY5uBvEYzEKMLIWuDetUW-tpKCW0GphktXrpkXtVu8_hGZXy2KguIFCpcT6lzAe8f3RaOCrvYnUen7p8lb-IAwTG7GOoV9h4xc9OLD5ne3I0Wj40H0EzJPg3Z359_3SvuSrVgA0dGyC0RrvRBSWdIva7VUH_1YHKWjvrF0fxsuHN3WCky3Uc0jjrRZCeZYDBSinONY_lzCgqS5bW4JgsZOCAWewL-fW_LlR_Ru-0g9zxHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjGSOh_Q5Ey-S_ODU2_tl7dygqrGrgo2p5Z3uwU2sbYbAlGaxApJ2IWNTGPSY0wm67CvGn_pC4qtwHXCdKDhcQscMCIK2xtxdJDQ-cW4AnCksOtW_wDThKc5gb2hAOUNm5LEhNiTx2CaUUimUWrzM_Pq-tvSS1kMEg39OXOkeV98WsurL4HNPvI4w3lpMCo9_6f0zutu6lm8VuuB-KfeHk7y9xkoyj187PxrtSG8Y9D40SYksfdVlgY_b7D8JQgH251pTcGd0_lOsWZE5kshZCFdhwvfz_FTC1VfUY8-dpdInPMXZGBL3yF9-aDqQxAe22EUk47sxCuoNUAx5UQYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwwg9VGbV-hL0MkHd7-umD70VaFQnG9DQQT5zRi7a5YN8ryfdtuR6E-a59yZbEjvh_PSpUxqrH9DjX6bT78YXNaDJgClVhRYew2maFqsXzQH_v5zkhPGPipuhQUPBjwWH62XffD_cZFZfB5XLzAr5ZhfsvH22fbjZn24dDqGGwajG6rbbSkskW0uCvjIMfWv9fVPmxGPYwQNDxf1Jk8DnqBMfgmshpgrMtcG7-xRyNiadSEaaaxYyU8TZsHrKqFayue-MeMXt8Wy4K9Mdu0emQGtYKgXQg0djJNwRphvO55S7iaqnaBD65lh0rscuD-NSZsiD1E-pAnS9ZOnw7BRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stSxu_ahye2JRP7xbKRS_H7GimD7GEjawppPihYRRD2VTIttjksNUO9KGWVhLNh-EGVebkrGofFqba7Cz63j7uXe10HJiM8nvU5R-MONhUVX-Iou5SqFz-QZA329IkclIa2jDXDtVxA00U1E_VcIumDg7gey40Rp2MEpYEsC091jzS9r_G3FCH_GexuSuUzFVvpbI8zA5Yi8Pdw42gv0-dpebAl7jLSFBtacAYP3N59_VJm8jgic3_BF5Se_uIFT5NPLkUASL_0CSixEpySncpcYaD-lC8NG1JqIw5ygAj47neeakc8znKfx3IoBBa7cw0Mso92vMFIlE6JU3c28Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiKeluE1aGESy44nBpqGl4vA4bl6bkKVJqNxWdu6o9h7Lo1rOsTvPmEmqSQ2eb0-txSiHBQkuWAk71wOHw0AK_MP_wJsXDNAEMTlqP8IHs73NaPsnjaSyFrwtHS_sDJ55OA0_C8NfX7hXLHzO-XbUnE2D62pPhQ8OtDpQd7f_3yDiE8HNyKXElsCltlDr-TM2oPpPplYV61qWfnv6IItCQvNe2umb8n5LZTioty7i7PVA4IdQVkfcaESP0LzPCuwVTmMoK71S4Jx5i35GjLOJszaB3hsefKRUiJT7hj-6J9QmKeAORuOgEoT0iG275a9hIciusDVzruQV2KYM7vfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=MH2Hh2WU3O6MgyFj3do8pVGo4zj5I1LOrVqchepW4cgAnzpjjW4W20t2L9tC8yNYJLaP7sdxnhftTM-urz7XbToGaQymNoEHBuKUB2X4mqk3kAPIOc-b6N9zb-CnlieUqe2ybEIQIgC0hZ0McoFfPkvZN8Edc97YwMgS9XZNvjplfvGEaBxsSi1G122TF3cPa1C8L1dRYbdn3nJx1BjA2AGN6qZfxY1KCgqJ7vj5ZuNKJiZXQ_qebTyJYIFxu8BFLvTjzBtPOeCJp18df9yvrsLtA4t6HbYdRHRo2FI1kUfRESMBJivJ50pWF5_cqtf3EiIpIGG9fpOYUZa0UwmGzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=MH2Hh2WU3O6MgyFj3do8pVGo4zj5I1LOrVqchepW4cgAnzpjjW4W20t2L9tC8yNYJLaP7sdxnhftTM-urz7XbToGaQymNoEHBuKUB2X4mqk3kAPIOc-b6N9zb-CnlieUqe2ybEIQIgC0hZ0McoFfPkvZN8Edc97YwMgS9XZNvjplfvGEaBxsSi1G122TF3cPa1C8L1dRYbdn3nJx1BjA2AGN6qZfxY1KCgqJ7vj5ZuNKJiZXQ_qebTyJYIFxu8BFLvTjzBtPOeCJp18df9yvrsLtA4t6HbYdRHRo2FI1kUfRESMBJivJ50pWF5_cqtf3EiIpIGG9fpOYUZa0UwmGzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=kyErGZ8ct_se0UgGiSPGKskr9-ewmbqmRy-3UtdtPPHRuCL8IKdZnTaBtHrCZ_5S5qU1wdpZ9-yEQ3Bao27asbPGEGfgNAO0zXJApbIPBbU7WivmkdRqN50Jivx2tEDZ4zqrE2jKcAWtcVebH7S67ESc5BYZDxx0ekQMASGc1kyYSkuNHeehbzc5svgZ5cK2JV77Jjwe45Fr3gCupAtopOHp65kydD3GtUl0WU505g9KTWyqcBunalMpNNSiHwk50cBL8eOwI3VObRHjrQQWAG4OpBfHjud8HVKrk-KHXxeyeSsP9doJmC_SDppE2e4ubVrmW77fbOZHaaWUoK9Iog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=kyErGZ8ct_se0UgGiSPGKskr9-ewmbqmRy-3UtdtPPHRuCL8IKdZnTaBtHrCZ_5S5qU1wdpZ9-yEQ3Bao27asbPGEGfgNAO0zXJApbIPBbU7WivmkdRqN50Jivx2tEDZ4zqrE2jKcAWtcVebH7S67ESc5BYZDxx0ekQMASGc1kyYSkuNHeehbzc5svgZ5cK2JV77Jjwe45Fr3gCupAtopOHp65kydD3GtUl0WU505g9KTWyqcBunalMpNNSiHwk50cBL8eOwI3VObRHjrQQWAG4OpBfHjud8HVKrk-KHXxeyeSsP9doJmC_SDppE2e4ubVrmW77fbOZHaaWUoK9Iog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-rRJWBodoVbWAhBNMYpUNBwpeNauQujiHluPTVXd-lwA8urp8l5V8nMKiyHY8YopRpYv4lh_Q3DxAP7ZX2ITnoNF4scs8lhOgFXug0jwHX4F1CvU9F3o4CA9Yucr2Kn1MJjUlNwjn-uzBeyeHURjVQPwOcjjiLNN0XvS518dEukaMK11Fs4X6-hAs8Olt7SYOG_MMK6jKxGWGLTE7JG6DCHpuJmVYraYYIwACiLOR08KLoYgGekY1D5r1iTJWxfX5xndea2sYv7XTtcR9vhXw6a79wv8Q0X0tze1pjBZFgUQZ10dCInKiU6ljo4oSdIA47YDSxwypkgMnJ5Uxo2khQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-rRJWBodoVbWAhBNMYpUNBwpeNauQujiHluPTVXd-lwA8urp8l5V8nMKiyHY8YopRpYv4lh_Q3DxAP7ZX2ITnoNF4scs8lhOgFXug0jwHX4F1CvU9F3o4CA9Yucr2Kn1MJjUlNwjn-uzBeyeHURjVQPwOcjjiLNN0XvS518dEukaMK11Fs4X6-hAs8Olt7SYOG_MMK6jKxGWGLTE7JG6DCHpuJmVYraYYIwACiLOR08KLoYgGekY1D5r1iTJWxfX5xndea2sYv7XTtcR9vhXw6a79wv8Q0X0tze1pjBZFgUQZ10dCInKiU6ljo4oSdIA47YDSxwypkgMnJ5Uxo2khQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIyzNg2Beag8oJnEs_VJmrFx4S8wVNh-VZV0qq_RtIzgYOki9supsYyatUrBiLjOJKUSit-W9FNJOmG9aYDWz_mnPP_gImrPKAFbDIF9T5FFluWgLuL0V5GbBN2Ft0YYbeLN57erbo_MPxThsgOU6tZoqVqRf7onoCtiOqIfBlaPMeyJuG_JPtBtH8Ap-kEATTe3kIOxpJLPTrOvc9i1wM8E-Pq42WvufahAaZbK-t9-v2_ZcdNvDPsxGpV34d2LggYgwk5GsQ7Q_A1K3iFhQ5cIVIpCJa_JX_W1J30bMy34fEPuKEVh-k8ArLT0YiHcfNvLPcL3xhQr-XA81UwNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shZRmE5nK1iM6Vp7KtknKFWcrlRda2x5X3rKw0E3E7hXpL_Q_5UHYI3injYoG8IJ9YwBlja0w7p1NmpjS03q2Mt6b41DSc3j2IS0LvLiKeIou6U_JZEfAXi-8CzWAU4fNnAoU9LFAGhigI7gptUmzDUGRNQ_fZDqDMOtlksj2-ry9VbfKs8y-yCspVrfhviLCicRcS9SVkRbem9u3eB2Mzetw5D9n_CHrsqzaD-b7-JCfLtAvGq5nFDv0NPw3pHkqai1CZj1HVTnrXeY8VrkaXINmvSxKNWl4dbPhwtqRmQXm9sM2MPMxQ78pAjgsIsurjVYtcmbWiojsJXrK7SOwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaMzwWn8FWH_yDRGVUknN5pli6rksEqvdv4I--haLXzFZ6YpscYSkKXdmsEIEgN6CuvoukKYqV1pNm-Ih0-oo-uN1fXCmGmJrXibjARoE8bM8v1fTzfbPnhFMxqAepvBjqBeQcbZnxbiYkDpCNIEz66KcwTTizF8kFzKjgOLE6eqlEF4tJo7m-Su4VgHAz5w5JvoA6BBhxAJ3WQcGDp-GbXH6LXurDViB8Jio-01yC2qGe6mRzJQlVHszyNSHyzzMNpaDg0sCohsUC6wB5j5tFMaRnooGjtxMmdAZsxI8AlNq-5HKDez74V8MvNWpd3F7ZvQAYHHCbvIFlBHZY5VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
