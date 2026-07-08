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
<img src="https://cdn5.telesco.pe/file/MmVNw1imC60hETuqpU757ZhlgTDiyd4iDODdNCq437amDmWYoU4nYDbrBjItlj9HWvXutnlx_HylkupMIsL0Cy3CFqsDQJK95s4VW9Qt36QbklsNp3-2x2D0JfGFjcCEI00jArdJe6sQ88QUx7YWF1hTeh7K9EmpiQSONaE-JJXVY8_n3lPubkuVXp7CbZwrfjR-aTSrClHUmldCMQmw0F80gHgbC6a934Vfv2nQyxxMtm-eclCunApE4ygWWJ04Njun1JpZMNIFYO4Y8TupHfjshe4qDO-Gf67aK3_fYrwC6Z32M8zlgQ5eZwwrzLkltHofrIzw-EnRtLnltfvD3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 615K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-99008">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=QHdmALx909WJX0FQ4zsngeZk2lXwGmEFasHXcVU8y6JN5gefkpbO2uWyhx3-WGtde5n5ov3IrhQtuXAdzCj4ou5DljRWQtFFnhbIlOGswkP2rx9eUGVhhO1kUU6k4xsNuSlYZWXaw4iKyyxs44d6XMVhpRcVZp0TPN1UKNQheGZ5r9J3Xx1N8Q0q4nqlZ3VsaPnPYglt_Mi0RoXWdAQdmCMcSWRDlRnWxj4CUvwAmztBJQ3oAEFIErIXlJTBvqgLYQWI75qWdP9z712YpCODYv2JeF72IJr61r8wl0YL-rcyvet2ekfEkibjmmSaEqkICnjkUwcZ2WwkRVB6LhwzQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=QHdmALx909WJX0FQ4zsngeZk2lXwGmEFasHXcVU8y6JN5gefkpbO2uWyhx3-WGtde5n5ov3IrhQtuXAdzCj4ou5DljRWQtFFnhbIlOGswkP2rx9eUGVhhO1kUU6k4xsNuSlYZWXaw4iKyyxs44d6XMVhpRcVZp0TPN1UKNQheGZ5r9J3Xx1N8Q0q4nqlZ3VsaPnPYglt_Mi0RoXWdAQdmCMcSWRDlRnWxj4CUvwAmztBJQ3oAEFIErIXlJTBvqgLYQWI75qWdP9z712YpCODYv2JeF72IJr61r8wl0YL-rcyvet2ekfEkibjmmSaEqkICnjkUwcZ2WwkRVB6LhwzQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
تیزر تقابل جذاب انگلیس و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/99008" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYPZa6H7UeYXF0fopgDOwPU-7XT-SYQzAaE0J_qw34-1qHwoxKeyQS-Cr5mtxtKXl9sd-SrmR-H1Y3BdSSZOC4RLn7J0XLGUAqE429ancOVItC_F2TJ5OkvzVNG-Ljr-AUSCVewQKEYKr8v48PWJq7x8tnowgFqj9gyHwyPeGaDfcSmej1oEA2SpKh3pa9Ld0_RawVk29fxAaEnEW-qUw9rQ8QBWEzf4r7OX71uSezjCkCch07YcOkxMxTPa-nPxANuV2boSKk8WagmWQNxWhqoEYH7xeJd00ACClrZsB6PEef-Zum4foJ9mELZLdIOJZdL4BzbGmE2St_umfBioZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
♨️
مونیرالحدادی ستاره استقلال در آستانه عقد قرارداد با اتحاد طنجه مراکش قرار دارد. این بازیکن که با آبی‌پوشان یکسال دیگر قرارداد دارد، به استناد به شرایط جنگی ایران و بارداری همسرش قصدی برای بازگشت ندارد و احتمالا با توجه به تعلل مدیران استقلال بزودی قراردادش با تیم مراکشی را رسمی میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/99007" target="_blank">📅 10:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99006">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/99006" target="_blank">📅 10:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99005">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=t1HjxV0HjxFQFiXHCmAH3RFzRiSx87p0EvFH24NMp_8UZGrrU6usPhjWZnU5zFgpQ98shUm9Lj1oxaKGWF52-XJat9Vn_7LHh1oAmnaPN9QfQQqFSqAq03EELXZ0o4v0fTt3is3IiVtqCYRD1xR3peP08p9qrlZDroIOHs37IN0a6BXAHTHvy3zz_Uh2VaAF1dRAdWlm1ZYFCQ3cGrwIA5Te9e6vLPmsOlz1RlVA2PNWDoXCHLTDihkgEaI3y5VX-EsA1-KK6m-PaU4ymvsKFIpyjHkWXYSXIdGCTxiXHCk8C1o7lkcReYnno11nk8KAAIe1e1b8kNZK0yuYlkdQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=t1HjxV0HjxFQFiXHCmAH3RFzRiSx87p0EvFH24NMp_8UZGrrU6usPhjWZnU5zFgpQ98shUm9Lj1oxaKGWF52-XJat9Vn_7LHh1oAmnaPN9QfQQqFSqAq03EELXZ0o4v0fTt3is3IiVtqCYRD1xR3peP08p9qrlZDroIOHs37IN0a6BXAHTHvy3zz_Uh2VaAF1dRAdWlm1ZYFCQ3cGrwIA5Te9e6vLPmsOlz1RlVA2PNWDoXCHLTDihkgEaI3y5VX-EsA1-KK6m-PaU4ymvsKFIpyjHkWXYSXIdGCTxiXHCk8C1o7lkcReYnno11nk8KAAIe1e1b8kNZK0yuYlkdQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تیزری جذاب از نبرد مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/99005" target="_blank">📅 10:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99004">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVpUuOghCTio3QzCdpka0B71VeVDzb5b7dqeKgiATHh4q_1PCqwYQDq53vXwcb8BSQHpdCpAeHTeMcXPbLdG_DLq2_aeEPmSs-GQHzFb5HTvO_IJGhEdM5lG8Ai0_jgSifaOMfEBAuGhiN9iSyaQWUkJ05J_ovs1xF3L_IAbfbLVkN1GYvNcUClYQ3rDiqn8lQLQ2oUfMzG38AVIkJyn9p-gaBEX8qRVmEjIbN5MhvDWnot513RTdTq122S-4_oBvXRbWmFpwMMD-MtP9axkWNW4mn1SWPAH8A-KFV7henwSjWKauGOEsGnkvJBUtpM4LJCG6wYLpW_IfnYXwhgL3X4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12da15f688.mp4?token=gLAckSkhVdDHL9Ef7beD6hEvDq9geE_xwK53FBsh0nKY6AOt2Ada4GSjrKEvfVHFvYPIQ0C9AcsHmoIB_1AtTm0jLK8UVVfnYvjXh0LCfq3WbotMyyI1UQqbwyfKvKFYvFuyLsKQIVzQUM1hgJSaG2pS2wVdWlP06ssWUK_WNkD9DMVoEAvjUTf1Fbi8QFhHWXUZkbn323xNcGmUYK2nMdiNZHVQk0Mp-lDO9YmigInT_cvWkUZNmQlIbTnKISYzpl4hke4b2YH7e812UViDdDSiV3kLZcH7N32GVKuaygIL0hk_8Q4UhZcgK0a_Oi6v2Apw0ZwGZmL9jnx4xWWNVpUuOghCTio3QzCdpka0B71VeVDzb5b7dqeKgiATHh4q_1PCqwYQDq53vXwcb8BSQHpdCpAeHTeMcXPbLdG_DLq2_aeEPmSs-GQHzFb5HTvO_IJGhEdM5lG8Ai0_jgSifaOMfEBAuGhiN9iSyaQWUkJ05J_ovs1xF3L_IAbfbLVkN1GYvNcUClYQ3rDiqn8lQLQ2oUfMzG38AVIkJyn9p-gaBEX8qRVmEjIbN5MhvDWnot513RTdTq122S-4_oBvXRbWmFpwMMD-MtP9axkWNW4mn1SWPAH8A-KFV7henwSjWKauGOEsGnkvJBUtpM4LJCG6wYLpW_IfnYXwhgL3X4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
لیونل‌مسی ورژن جام‌جهانی ۲۰۱۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/99004" target="_blank">📅 10:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99003">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
❌
با اعلام کمیته جهانی المپیک، تمام تحریم‌های مرتبط با کشور روسیه لغو شد و این کشور میتواند در مسابقات مختلف نماینده داشته باشد. بزودی فیفا هم معافیت‌های مختلفی برای روس‌ها اعمال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99003" target="_blank">📅 10:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99002">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99002" target="_blank">📅 10:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99001">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=AUM8t6Yu4cuDxkcxGWxLwH6fG6lDpkonBsus72VKsJu9rXvcYQdk0G15f-qx34gWvMTz6QoW8OajyGmi7k5fhwk6rDQFvBJmGpxgqYgBbUFuHH4e_fuwq-w4upyZ6iUtNKem2ISMc_XPH36QEjyIrZ0ZrxS-iUOrmQHWJtR-ddzG52ecXy_YZKZZrO71Mx0ON0g_Xzy2MTu713XAzikKadswlrDBHCxU-Zmf-KtPMyEpH5p2hjMu9iPkQi_SyEIgMk1uyThAK21A5K-oOwTyDUxBDgYgPl0mvr9xHAX7cy7sGgfjqhCktvoQ1LCJoSHR83cClQUOVlHBBLuqkymmRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=AUM8t6Yu4cuDxkcxGWxLwH6fG6lDpkonBsus72VKsJu9rXvcYQdk0G15f-qx34gWvMTz6QoW8OajyGmi7k5fhwk6rDQFvBJmGpxgqYgBbUFuHH4e_fuwq-w4upyZ6iUtNKem2ISMc_XPH36QEjyIrZ0ZrxS-iUOrmQHWJtR-ddzG52ecXy_YZKZZrO71Mx0ON0g_Xzy2MTu713XAzikKadswlrDBHCxU-Zmf-KtPMyEpH5p2hjMu9iPkQi_SyEIgMk1uyThAK21A5K-oOwTyDUxBDgYgPl0mvr9xHAX7cy7sGgfjqhCktvoQ1LCJoSHR83cClQUOVlHBBLuqkymmRYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
دیشب هواداران آرژانتین برای فشاری کردن سرمربی مصر با پرچم اسرائیل تو ورزشگاه بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/99001" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liMg6miKno3k0-0uIxAwdu0YKuphHOAMQplrQ6aj20N6gfZfLRAmlsFMwepyIx8PGkEmjW32qHxMycVZwfnw0zFi-ZD2rkIPnpf3abPYCyed8upMs8iDPhmIEOasWMNp1FFmmzZV8rOiV6dNPavDsLN-p5EBLvfBDpNk5vSxaRjth861HMd_39mzynAivgQpKmX1iiQGVZLXu2m1bDknUNHgID9UMSeg2EBW0dfA2MHnfuBaPVbov8wUjJqk9D1BofJZcaJ_c95qPjeVvIQzg9KoSrfFNfVHM769t_EC3WN_hii_RnWpJ9IQHXu3mMkPkUuQry274mqGbNkDKrt6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🏆
🇪🇸
مایکل‌اولیور انگلیسی داور بازی حساس بلژیک و اسپانیا در ¼نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99000" target="_blank">📅 09:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=YOTnI7vOWN0HkyNEuc0AQ0ZZewl8XNfInCKVqirmERt1ychMLdy8cJg-IAThhBwsFHolnEDCt3B3F0QeE3FnKenV2-FBvvjcxT29Rk0PQ4pAMQRPWEMGKFhow8tJVK4y-6UkUmQZo6OBFNQw4Y2LlYuxwzsoaYzStvy5tIU-lQFtZCBVCt_KNdRVStp5qEz-huhubn_BXELmkLox6UGiOapLsY5C475E9jM_L9bgAmt8gpAEx7FwUOzQrNxG53VATgCjHW6yMlIHwP4NVd3qAjvzBWzlJX776vn3FWlmNLP5VZe-zGCBwddb2gtwp9ALbBssgHAPlJ3kPjBZXePWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=YOTnI7vOWN0HkyNEuc0AQ0ZZewl8XNfInCKVqirmERt1ychMLdy8cJg-IAThhBwsFHolnEDCt3B3F0QeE3FnKenV2-FBvvjcxT29Rk0PQ4pAMQRPWEMGKFhow8tJVK4y-6UkUmQZo6OBFNQw4Y2LlYuxwzsoaYzStvy5tIU-lQFtZCBVCt_KNdRVStp5qEz-huhubn_BXELmkLox6UGiOapLsY5C475E9jM_L9bgAmt8gpAEx7FwUOzQrNxG53VATgCjHW6yMlIHwP4NVd3qAjvzBWzlJX776vn3FWlmNLP5VZe-zGCBwddb2gtwp9ALbBssgHAPlJ3kPjBZXePWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتین به یک چهارم نهایی رسید.
🔥
🇦🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98999" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYoXSI__zPEJdeeuZg96-q3Qu8cv4ob4AssPuykjxcpGP7tHxzazeTtS78p1tdjE4-j5aKcQWnnDay3t__60gCH8Fx-lvkO9Gkfsl_WA0hhlcrsMj8QvpOmD1CywGwdazjt_-hwPkhCl2_AyJOIMGDNtAo39mRkq8ndjfMX7x5wBoRlYke6VIRqKls1P0wmXFv_7jzH2To0g5IKdItU025AHCzfKlRb9AqYwWLrYOUCgEoX-eRUpB9hZ4W9ryEJZWuRVFStzGeF5VCoq-KDp5BYuHFIJ6DPlwHnW5auAWmezNQkGx2RpoS_9aeirsusU2WC5ZCyeeThdEbhUZ9lE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
| فابریزیو رومانو: قرارداد کانسلو به احتمال ۹۹.۹٪ با بارسلونا نهایی‌خواهد شد. الهلال و بارسلونا بر سر مبلغ به توافق رسیده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/98998" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO-GlPESKAk2oG3sX-xzVRNI4YY1NbWDDCynVrj4mARlJ9C8dU1rak922Tj4U7Kcrfse6S1LvsZzkbWjsU_ynMhtKID1UPOhmne0DwrFmxPHBkZUctTUO4Yyl58NuYTkiw55vsbjkG6X1Xia4N5OpMy8NlSm16WrCDNQAuEwU7S0PNTlLT9qNC2YtdBNmJLhkV2ImQjCmG9qy00Fjpyl0bDFRGn0qo9XQ2amuBN3HmyCpV7dsUfEaSJLg2ZTSKq5s1QQriS94Uu0XDn1FDqDmFb9Bsed50kK2j0FviMyF7atWGUJZkpANokJGTzzu_MxK6piv-t2cJT_lLL_2qsLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
◀️
تو گروه D جام‌جهانی ۲۰۱۴ یکی‌از عجیب‌ترین اتفاقات تاریخ جام‌جهانی رخ داد، جایی که کاستاریکا از گروهی که ایتالیا، انگلیس و اروگوئه ۳ قهرمان جام‌جهانی توش بودن صدرنشین صعود کرد و تا مرحله یک چهارم نهایی اون جام‌جهانی هم تونست بالا بیاد.
👏
🔹
جالبه بدونید سایت‌های شرط‌بندی شانس صعود کاستاریکا رو 6٪ پیش‌بینی کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98997" target="_blank">📅 08:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=nVW5KHacsYDoq-Runlv-k4nGoUHzCFEm8ej38kokILnGmxX1Y5WzPpoeQDvvG8KRU1KMzFPIdZxKjjKI-W0f8Zwar2v3ZD6GbmHdx750_1vAilkArjVg0vyABquXqwcWuQlHQM5ZRKu_CBD6UZColOn4g7PkGFofCewidxkdKMpCCPZhJ4o9k7L3Bucu2RdvtpmW3JLqXZZNGNL2ubzyMO62KkGPcgEe1kKV4C6MsEuHzmOsOVwEeP9qqHxq2vvYwq4_WW9AqKSaOyc02sPtrVfRrlaWDjPNACEAHsU1dIIiObclnbPrVAuI8po2rA_8caKC5ePSiFve2sF9bKaLhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=nVW5KHacsYDoq-Runlv-k4nGoUHzCFEm8ej38kokILnGmxX1Y5WzPpoeQDvvG8KRU1KMzFPIdZxKjjKI-W0f8Zwar2v3ZD6GbmHdx750_1vAilkArjVg0vyABquXqwcWuQlHQM5ZRKu_CBD6UZColOn4g7PkGFofCewidxkdKMpCCPZhJ4o9k7L3Bucu2RdvtpmW3JLqXZZNGNL2ubzyMO62KkGPcgEe1kKV4C6MsEuHzmOsOVwEeP9qqHxq2vvYwq4_WW9AqKSaOyc02sPtrVfRrlaWDjPNACEAHsU1dIIiObclnbPrVAuI8po2rA_8caKC5ePSiFve2sF9bKaLhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
برای خیلی از پسرها، فوتبال فقط یک بازی ساده با توپ نیست بلکه پناهگاهی است برای فرار از شلوغی‌های زندگی، جایی برای نفس کشیدن و رها شدن از فشارهای روزمره و فرار از دغدغه‌هایی که شاید هیچ‌وقت درباره‌شان حرف نزنند. وقتی بازی شروع می‌شود، برای دقایقی تمام نگرانی‌ها، استرس‌ها و خستگی‌ها رنگ می‌بازند و فقط یک چیز اهمیت دارد، عشق به فوتبال و تیم مورد علاقه.
🔺
فوتبال به آن‌ها یاد می‌دهد بعد از هر شکست دوباره بلند شوند، امیدشان را از دست ندهند و تا آخرین لحظه بجنگند. و در این میان لیونل مسی برای میلیون ها نفر از مردم دنیا شاید بزرگترین تراپیست دنیا باشد. برای خیلی‌ها، تماشای بازی مسی فقط تماشای ساده فوتبال نیست‌ ، تجربه‌ی آرامشی است که در کمتر چیزی می‌توان آن را پیدا کرد.
لذت ببرید از سالهای آخر بازی مسی
🩵
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98996" target="_blank">📅 05:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=seaauUlyBXUe5k2ne8KOrKrh3tHd5gjkGnyVIZHuaN4osjOC_y2azUZS3fY_FSg5JwzMQsWl9V3-PXEpaMkVW81G-ZU_3YioQ66cw4rei65AitJgX2RQ8JJeeNyhD_3BEQa0-9zeqyGx-5l95fwp5Jx0yJV3_TyscDEuaRAFcUvlH7jsIVa1vGsIIJmwANsFKVSDbRltfJvsM5qx5GRYZALaqGk68W-9MuCCtdc96ElioTYLqmXapxVLuQ3nNR75XW0uH1RjqkYemqhebnOTZj1DlnKxj2MisPZtpOGnXn-IWWfbwbvoS5DxhAi0M1wsyRNoCqqwuI7uXN8dfY_EgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=seaauUlyBXUe5k2ne8KOrKrh3tHd5gjkGnyVIZHuaN4osjOC_y2azUZS3fY_FSg5JwzMQsWl9V3-PXEpaMkVW81G-ZU_3YioQ66cw4rei65AitJgX2RQ8JJeeNyhD_3BEQa0-9zeqyGx-5l95fwp5Jx0yJV3_TyscDEuaRAFcUvlH7jsIVa1vGsIIJmwANsFKVSDbRltfJvsM5qx5GRYZALaqGk68W-9MuCCtdc96ElioTYLqmXapxVLuQ3nNR75XW0uH1RjqkYemqhebnOTZj1DlnKxj2MisPZtpOGnXn-IWWfbwbvoS5DxhAi0M1wsyRNoCqqwuI7uXN8dfY_EgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‼️
12 سال پیش در چنین روزی تو جام‌جهانی ٢٠١۴ یکی از تحقیرآمیزترین نتیجه‌های تاریخ جام‌جهانی فوتبال رقم خورد؛ آلمان ٧-١ برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/98995" target="_blank">📅 05:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts_t-3jn8AE77OezH-NUFGBRwDBYUx-H_KBGvmfauHA3M_-9QTGGveChhHmr-3uRh9R4fE43LA2Py7qh8ugMHb0OAbH14XYnPDMbvhxaDD4asAMK2ITq3_Hc1xqmNxfm4ND_tC0CAT17v0AzzltBcYtgdQIAXds2AeGm2T0S5FXrzAN8uRlpC-50ziTzPu6KUldfLs8PpkXUYJn4gJiB4z-c7zAEWK-qkcxlfHIUOYyeBF9MmP0Y0V8rni9_3thtQnc0upEqJ-LxiQYQielzOL5k8JIOLgYKQBFLRFDvK3N7JtEZGIktBJt5zUbrm1AoEXJ9MkjEehleux4JWae8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
💥
لیونل مسی:
«من گریه کردم، چون احساس کردم که هم‌تیمی‌هایم را به خاطر پنالتی که خراب کردم ناامید کردم. اما خدا برای من یک اتفاق ویژه دیگر در پایان این بازی در نظر داشت. من خیلی خیلی خوشحالم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98994" target="_blank">📅 04:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98993">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98993" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98992">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn1z5eXfMKK2ChUj2C2lSCsNO3oDwqlbXg7caO3Rc32ePmij33rwzCczciHjw1nDONO_Iuu3K5bj9zDJGRPdUlpSj2yHFoQCr-1CgqHPS5dYJgFCfP6AAGBYo2w5PoGJiJ8mvGet0yJXh4UcplFjzb-felipU2fJ3RsEtV8LykIw5-fcQYya3xqM_Nn_LfsCx96NKy1frrlnX_EkAl9hjmZKAXSmYF73zhKULLAITbaSVv7aXIYhG4X_uTJ3OavGLcWMyG1UZjmWnEZJzgUIQGsxgPDUuAhTIvFpWtMcj91WEbzZ1xQyUTvd9Z1bxNvKXFQsnWFFAjQ72HJ9T9eRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان جام‌جهانی تا پایان دور‌ ⅛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98992" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WC4S29JAPm5tbH9eQ4nhs01MNq4rMiw96GpM-5maQ0-CmkswXFiSnpFEoYwvu47CUhNMNSYWS843NghNaS6iE34qeQ_3FtjDvA7FR8c76eQsaAlbmYOYhFHEtmKjhkRk0GLDYO2V_CywoB13j1CXffwGlf022GAs7RYf-m44khv5tUZk3obv7TJW7N-5bBcP5Ebp2F-USeOX3gE8cIpyag_5w_Wvtbdaxp4S27eoIMiyH54HFxkbE6RSUKDiOpbgh6-H3YbzOQB6oGqu332tfIz9JLuCsYf4MdhIUnMPjSclRKxku2LeOPpaALe0W63SlFIbpkp_HNc7Djj_ILRPtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ اسطوره آربلوا سرمربی تیم فوتبال فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98991" target="_blank">📅 02:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98989">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRCueTDZ6mhvD71_WPCHlR8y6raQ09lqePIrxFhO7Tx1L_E27UKEXZKW2p0WsiNsS4UxnqXO5B_Jq3K0K5FSAUHsn5zxbMi6QkjeJjUAX7q2hz22_c7mWDOBljbDZ8S4nkOLbpoO3j-V7ySwRr7W7Va57fvAWD-c8FDWwepsCtNphzt_bMwp9je4uD9lAHxUPL8UtRygSOHogBgdo32p2EGR5Avp1xVa6nQyyifV9uLbDCcyFXsraqQqloz-TrJne_CJ4B4toOh9yqw0eiOStkDdcOYOYKUxK9bTOiyh404QjG-sli4zlguQla8i6-U-sKbgq0hTo0zHPVS5A2gDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98989" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98988">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2ezmqXtubYyJSDIu7UnYDih-u7dWHfOUv3qlWls8imJK31TjYdc7xiVNuVUbOZ_ZKkdxBKvxQBlsDEvJVQPyQ-2fdtncWfSaYo7tvtSgZsHxUMOybdg3D5kDsN4inBPV211bFfSjjdy5F-pU7-N_yLKE7_HmEB2dxouVn8TTP7mnIAVGqLn1fLLF1gP7R7eqfWjv2B0WTKc52BfVWfYRBwqrTs6XbF00H0kRWZ5Dqq86gcdgwDBET_KmqFx6yTsCPolvf4ahxyxeSOc2lKBdnD_1tWvBhgtaGKaex0sIRYMStUD3Mi0-G_3E4zJ5heQ17t3IcF2aZPaqOeoBJ2TEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
تیم‌ملی سوئیس با برتری مقابل کلمبیا در ضربات پنالتی راهی مرحله بعد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98988" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98987">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/Futball180TV/98987" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98986">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگلگلگگلگلگل و تمامممممممممم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98986" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98985">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سوئیس بزنه صعود میکنه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98985" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98984">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/Futball180TV/98984" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98983">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگلگگللگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98983" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98982">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">لوئیز  دیاززز اومد</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98982" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98981">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کلمبیا نزنه حذفههههه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98981" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 568 · <a href="https://t.me/Futball180TV/98980" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگگلگلگ سوم سوئیس بالاخره شددد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98979" target="_blank">📅 02:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98978">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 462 · <a href="https://t.me/Futball180TV/98978" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98977">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پنالتی چهارم کلمبیا و گلگلگل سوووم نشددددد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98977" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98976">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/98976" target="_blank">📅 02:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98975">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگلگلل سوم سوئیس نشدددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98975" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98974">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/98974" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98973">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلگلگگلل دوم کلمبیاااا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/98973" target="_blank">📅 02:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98972">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/Futball180TV/98972" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98971">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگگلگل دوم سوئیس</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98971" target="_blank">📅 02:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98970">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/98970" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98969">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگگلگل دوم کلمبیا نشددددد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/98969" target="_blank">📅 02:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98968">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/Futball180TV/98968" target="_blank">📅 02:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98967">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلگگلگل اول سوئیس</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98967" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98966">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
🇨🇭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/98966" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98965">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
گلگلل اول کلمبیا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98965" target="_blank">📅 02:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98964">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/Futball180TV/98964" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98963">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
پایان بازی سوئیس و کلمبیا
بازی راهی ضربات پنالتی شد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/98963" target="_blank">📅 02:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98962">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tw-UYc2wlPHEg0mMJGu037BZElAlApQonTDVTQmuQw3nkNcYra9V5wthMCi9fpLMeTn5b9Hj7TOqwp3CYLB9e-B2SHebmauLQW6cgbzd-N3mtU7TqtBB36JEaKn3JjQ0lTDJaYZj60BgSs7SMlz9fM4BAQSL0b4GL6yi02IogNdq9RxYI7PHtzEfDQYZyKtrkT8_KNZxLYpisvDMPdl9Hdi0LoSqX3N-z5f-Fu1cDpajUqo-bm1n8NQyfFS34qm_u_emGdhCIF-jw9xxegLXGZWVz8TIiJOh5p0PDMmNRMLIjxuKBBuAT1lahV2YL0aMjB--DN5dt0Z2JGd-i8bkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلمبیا چه توپی نزددددد
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98962" target="_blank">📅 02:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98961">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ گزارش‌های محلی از موج جدید حملات آمریکا به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98961" target="_blank">📅 01:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98960">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوووووری
؛ گزارش‌های تایید نشده از آمادگی همه‌جانبه نیروهای سپاه پاسداران برای حمله به کشورهای عربی و پایگاه‌های آمریکایی تا دقایقی‌دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98960" target="_blank">📅 01:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98959">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وقت اضافه اول هم مساوی تموم شد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/98959" target="_blank">📅 01:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98958">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=A7sxW3Qz1nb4BKmqwH5QNoxFEwbvrxTXVdhX98ixuzqpO0XvoKs_Eearf-EtOnrikt7qUkYq__-eksHAVCqK8JvxUs4PFMYup1nGwZQWx5El192UabcF-KzNQhEn2opC2DdLAzdUl7CSSPUs0mSnXqGFNskN7Pj3xUfGNRh2iXzM84FaVnzYx-uOXShyux_ocAYZzecbKZRpfQnzli6J2CJ8sg-VQxXQoyakHylpqh-sQbF3hwRO7eui9GyzDYnYw7f9Op-0WeAve1E8rvHByua_2otK046-COobRS9caLCsn5RHrsDF52bb27nN8ntuGMYiQxWoUO5MicAppg9uf0OzZAhfiAaopIPHd3jC5WG2mt9s6jOYtjhinIBcdH9VuzRheYinem0laId0_jsbbU8aY76tw8WEh3OF0_HVuVKwqtt0qOYhxvFSDrfINwLb1zWD4VkLw8NbxmJFvlbXz19K3IT1kRE8T31uAw3Kfi_IfMXcQfWj8MGi4tB5EgIYRFZEeMvfUL8gZ96jzqNTRkeSZCvnCT2FOhb8-v_yTbEPDExQIWLNYiz18FGD1vP7G7uFIqvecUM3CUNCRXyyJQU-wWyZpjr8jENaMLolXgV13kiN46JNx-NAlPxUUpS5EksOyvxiRtaofNvWZEGeCCtcqCMRn3W6W3iAuACqzjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e61389fce.mp4?token=A7sxW3Qz1nb4BKmqwH5QNoxFEwbvrxTXVdhX98ixuzqpO0XvoKs_Eearf-EtOnrikt7qUkYq__-eksHAVCqK8JvxUs4PFMYup1nGwZQWx5El192UabcF-KzNQhEn2opC2DdLAzdUl7CSSPUs0mSnXqGFNskN7Pj3xUfGNRh2iXzM84FaVnzYx-uOXShyux_ocAYZzecbKZRpfQnzli6J2CJ8sg-VQxXQoyakHylpqh-sQbF3hwRO7eui9GyzDYnYw7f9Op-0WeAve1E8rvHByua_2otK046-COobRS9caLCsn5RHrsDF52bb27nN8ntuGMYiQxWoUO5MicAppg9uf0OzZAhfiAaopIPHd3jC5WG2mt9s6jOYtjhinIBcdH9VuzRheYinem0laId0_jsbbU8aY76tw8WEh3OF0_HVuVKwqtt0qOYhxvFSDrfINwLb1zWD4VkLw8NbxmJFvlbXz19K3IT1kRE8T31uAw3Kfi_IfMXcQfWj8MGi4tB5EgIYRFZEeMvfUL8gZ96jzqNTRkeSZCvnCT2FOhb8-v_yTbEPDExQIWLNYiz18FGD1vP7G7uFIqvecUM3CUNCRXyyJQU-wWyZpjr8jENaMLolXgV13kiN46JNx-NAlPxUUpS5EksOyvxiRtaofNvWZEGeCCtcqCMRn3W6W3iAuACqzjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو دیگر از حملات دقایقی‌پیش آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98958" target="_blank">📅 01:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98957">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=YEgRLWVBPpDsJYV-lIblLONVyIf9KgbVZhceeVf84dLRrydAEjNjJLF-Pol8CFzgnwC58Zixdl5slJH2l2-myb0O0fHwNgddaTulqQxGQRst0EA0-TsxXKCk6lt7CD3MeBEnviEXEDrbP8E1MqLBhQp3pFVj2I9QjGS4uImQp67N70tu5WX5yoYsFH0gBziG9Sa6CNoYcroQltPkA6qoJH2DF4RFykERxpdLk1cc4DgKO3LVRJ05WxyFeCEzNMqVfFPh86SexdPxdzkqhhFhk4fFU6vYcY0aMV2mqYGjcJYi12osK7ujMslXr2NarU-1KuFzMl7kf0Ruct0n-UeRPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d512a0d2d.mp4?token=YEgRLWVBPpDsJYV-lIblLONVyIf9KgbVZhceeVf84dLRrydAEjNjJLF-Pol8CFzgnwC58Zixdl5slJH2l2-myb0O0fHwNgddaTulqQxGQRst0EA0-TsxXKCk6lt7CD3MeBEnviEXEDrbP8E1MqLBhQp3pFVj2I9QjGS4uImQp67N70tu5WX5yoYsFH0gBziG9Sa6CNoYcroQltPkA6qoJH2DF4RFykERxpdLk1cc4DgKO3LVRJ05WxyFeCEzNMqVfFPh86SexdPxdzkqhhFhk4fFU6vYcY0aMV2mqYGjcJYi12osK7ujMslXr2NarU-1KuFzMl7kf0Ruct0n-UeRPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو‌های منتسب به حملات آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98957" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98956">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98956" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98955">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oS9e4KiNZJyk1D_HvsaiFgB56ySXMFvfqvq0_i37lb_33eHi0Hr8xUZNWdBdusJRS4umQ2wfSQ4XcVQ2gqG3EyFNqS5d5F8FW4dPSm-IQd9jWOk8c4H9xPtnNV5oKLjZMZs7c9ufhU56Q8SMH7eX36O94JTUhcrfaaYzauBIuL5hrlWjXexj8YJJtUbV4G-xFFo42-d7K8Htw8XXv0HhBPp3d32JeVy6ClXZlKIBMHgY3xsqVoGpE3gFymkE86iGYjow7OxS3pTYvU_7Aa1nU5qqHdh8yiuUoRffPC1mrTOLlH7RSI1w3-NdLM6aSfIQR8mrQdiI8ABoQbdkH1dXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98955" target="_blank">📅 01:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98954">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/98954" target="_blank">📅 01:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98953">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پایان بازی کلمبیا و سوئیس در ۹۰ دقیقه
باید شاهد ۳۰ دقیقه کیری دیگه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/98953" target="_blank">📅 01:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینقدر بازی اونور کیریه که اخبار جنگ واجب تره پوشش بدم براتون
😐
😐
😐</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/98952" target="_blank">📅 01:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛
سنتکام: در صورت نقض مجدد آتش‌بس از سوی ایران بار دیگر به دستور ترامپ محاصره دریایی ایران را با قدرت فراوان ادامه خواهیم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98951" target="_blank">📅 01:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3b48AAXucW8wOyi1KSmtmTwwdXBfmnPHHSF2Q8jYZi1suoIepktmlqSfX2Mo2M4i7YJo-CLNLw82t5s5zVPwf1EvrJHAzE7ySMWWhJPrsQkK5-tB5sNs9StKM10BdRTi8EkYlhjNeCug13wOJ4cAK-U9WFUgv8jRoeyRYwpSZJTkaqA2pjx0R-S_tXYKoAWoED8_IDENwsYZBX21hVOfoUwFQ_AdxaBuRRu6kkHZgc4h6Qyn3NdN5xgk3O7is-Wr9Jko0Z9HrxppORj2sUbRWgsYXniw5J_f9s3p_hrm52Er6NIueXKWYGcFprsURS2g8eq4xk2YPG6sUfyvYLvxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری از حمله به دکل مخابراتی سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98950" target="_blank">📅 01:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=M4l_UWhGue5owe1_o87rX2LnRvGA3W9kpJC-2wnZ432AKWUB_5jb5SSxph-1v-_I9AIqE1mK9PyWBj-IKnNIW7zFwt93xQEISp-JnGQR3ZaQ_Kldr3Zp4Vd_GRL9p9KXOMf03EedOs-Q8MuRw8PGrx1H1po9NR41aNP7U3pN_g7bDv_t8SjzqEQ1zXK5c-bVp8qRvfaTm0hnOrgCQYvAwYDV-9dLtvtIVtkWoZd6j3xT1DrH8bB7kqCxrdNj2aX9OVZrkX_ECQyH0qoI4mP7pEtmsIzx42FKNCL5NZb05fBlBddooVwj9w1z9Zri2k9HK5WoPj_KUI_cIT2JY7tYCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f434bf30ec.mp4?token=M4l_UWhGue5owe1_o87rX2LnRvGA3W9kpJC-2wnZ432AKWUB_5jb5SSxph-1v-_I9AIqE1mK9PyWBj-IKnNIW7zFwt93xQEISp-JnGQR3ZaQ_Kldr3Zp4Vd_GRL9p9KXOMf03EedOs-Q8MuRw8PGrx1H1po9NR41aNP7U3pN_g7bDv_t8SjzqEQ1zXK5c-bVp8qRvfaTm0hnOrgCQYvAwYDV-9dLtvtIVtkWoZd6j3xT1DrH8bB7kqCxrdNj2aX9OVZrkX_ECQyH0qoI4mP7pEtmsIzx42FKNCL5NZb05fBlBddooVwj9w1z9Zri2k9HK5WoPj_KUI_cIT2JY7tYCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇪🇬
اشک‌های زیکو بازیکن مصر از ناعدالتی داوری در بازی امشب مقابل آرژانتین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98949" target="_blank">📅 01:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNeuiK1OLiS2g65bbkoZhREm6lskhORAzx5HwnE7QDLcY24FmXet3zgEL2-yYQvr9ebOpy9o1NXNibXmsR00VjxSvA7TCvvRBeMYiByIjTWIOoCeVs99ifkoZLftuai09MZxlydI7DPGr_PezhUbKdZ_AcPQxuawc3Eugbi0fJ1CTePVVWUxI37TUWSwznVA0V1gTzsoepgLwCtDTbfo3J94egb9LwOEAMe0pSYqG_3YKSJio5V03VEkKtINXIGYvX26n7Is87GyY550Do9szcuzdGlbSWpTQn4qL2AQ53a8gxKjVCJkN46azzoMmAUvzDWp4D8QGJASfXiI7Vunpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم‌ملی آلمان درحال تماشای بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98948" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98947">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7agG3SADGr3HGEXTRbx1ugdO46QH4gj0TnbT7Cx8Ry4mm96EeoJLn4wl4FSCl20ciqFh4kzyIMblv8jMse6OjzWWI9vV209NhSWz2C82N9d6wXdd15g2ozYUx-9UIxbWi55tkor3mOUZ9td1cbo3VzLQtl7UpFw1VeT-yOF_C9z17aJzVziDLcvNfLX-tgGAQgiUvG8j16a4d68BXFfda6kprFSxNJW1na3HjvB6b-dREi-yypG3qa7g1K6csB_Vb6WraVcglp7ToyEyBoArczjbTxjV2AQ0dQu6bBLFOfvhAMm1GpHtraFt2u94zUEvsXoDeUbqPuuZn4nYxhsTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر منتسب به شناورهای سپاه در سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98947" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98946">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری ادعای سنتکام:  نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.  حملات…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/98946" target="_blank">📅 00:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98945">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8QMWRRh5h2TeLOVMFq5n80cm0ecgCVHuUen3Trf6L1e9eLBMg3NPX0bIbYFZ3QQl9Vhgkpb_H6aHjzpxN_X91D5lGJP2G4lGCRH5I9lnF8xVESF3XR37_XOvEiB2UFZM0DMA3JKWhAwfsln56OJtGF3I8hxx6ROvfM74Pe4bG1p9Q09158lz2sm5VpTuHQuuQY3yGJ1LBOjSl9taGftHzU8K9Tng3oUQhT_mPYrccddUJ3vq3-ytxoR9keybWXAWk6ovof_lzNuviGtQoV8uH_l76slr69sKiuxrxzKY0OV-CzdZeu1X1bY8VMUcJAsev9sxUu3Bz80qPKIAB_OUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوری
ادعای سنتکام
:
نیروهای فرماندهی مرکزی ایالات متحده، مجموعه‌ای از حملات قدرتمند علیه ایران را آغاز کرده‌اند تا هزینه‌های سنگینی را به دلیل هدف قرار دادن و حمله به کشتی‌های تجاری حامل خدمه غیرنظامی بی‌گناه در یک آبراه بین‌المللی تحمیل کنند.
حملات ایالات متحده در پاسخ به حملات ایران به سه کشتی تجاری که در حال عبور از تنگه هرمز بودند، انجام شده است. تجاوز آشکار ایران، بی‌دلیل، خطرناک و نقض آشکار آتش‌بس بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98945" target="_blank">📅 00:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98944">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101717de02.mp4?token=hcmwmai6OdGNKgTbnQw2BiJJq_Op62P01aUcswmGAI4_HevYSicPKjh8CvkAblm-2e9et02mAuujO4fzBjTTi41-cYcItOoDy14-U7RgacQeR-7HyBxXrZgfYweghMmuSFsPgQF4f80B4yNqSmPrK2HodcHthLUICC0CVVcKKjAHr5kMQgUolSvOJdUDujHACernj0qeOjvclEpkONomUB9OcCjBzfaVRBewE9GPgO4SQT6XfAp-0FdP4-ndxUCu-NzL-FqUq_ZUoyc2RifIHAYHFEZcpeC00ZQqhtwNCN_j_uB_PHPwdsDURSlkozt18UsS_5t0zREwKMphDW7QXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101717de02.mp4?token=hcmwmai6OdGNKgTbnQw2BiJJq_Op62P01aUcswmGAI4_HevYSicPKjh8CvkAblm-2e9et02mAuujO4fzBjTTi41-cYcItOoDy14-U7RgacQeR-7HyBxXrZgfYweghMmuSFsPgQF4f80B4yNqSmPrK2HodcHthLUICC0CVVcKKjAHr5kMQgUolSvOJdUDujHACernj0qeOjvclEpkONomUB9OcCjBzfaVRBewE9GPgO4SQT6XfAp-0FdP4-ndxUCu-NzL-FqUq_ZUoyc2RifIHAYHFEZcpeC00ZQqhtwNCN_j_uB_PHPwdsDURSlkozt18UsS_5t0zREwKMphDW7QXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تفاوت توجه بازیکنان آرژانتین و پرتغال به دو اسطوره؛ یکی محبوب و دیگری منفور و مغضوب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98944" target="_blank">📅 00:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98943">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ شنیده شدن صدای انفجار در جزیره هنگام و سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98943" target="_blank">📅 00:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98942">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/98942" target="_blank">📅 00:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98941">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
؛ آغاز عملیات شبانه ارتش آمریکا در جزایر جنوبی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98941" target="_blank">📅 00:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98940">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6OlIWp_tvxre0xFh4fFchgaXIb22ATUZZ9BP45tMap36Ir0iWmCxxMn5aDt1wq0ob2T4BrIt2PyKIfHcNusWGZKNYZ1UjS0ubiUP23N9dGAicD3bUDgEZaKY2ozQ6kNFx3vjVox9QnlCd7Ym5TUjS0HcW3FAd-o9WYR67qtHHLK9W9aWwQe0sX4n9bN1bbXisP1_fKLCskIMnVUNvwXVc7D8pT7OxUIlSGdKaxl8cREx39faXuHzii8DRsTIbfMo_6ATIxxL_mwof7GL1mkcKZ0u4GxIhRz2xba1eVpQiVJCvdWP3MHNye41SitlKZLcFgqK1TTX3PKLYwqdGPZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
آرسن ونگر: «هیچ تیمی نمی‌تواند در این جام جهانی بر فرانسه غلبه کند، فقط اسپانیا می‌تواند آن را شکست دهد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98940" target="_blank">📅 00:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98939">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e80f1162.mp4?token=E2Tsolk1STZgHU9hXS6b7StqsuxrDKssZns_Q3YJ2eZ-hHadJ4Ifk5zF_zhXGDTxBFdEnHFTHeue8kWgcCEi_Skoc9eOYyIzWORXGCT-Lxv3hDyOBkJ1BDwIPAVJpbXWNTu3IxWEUyPAkRzbLuEMEarSp8UZbbTjpjMxbaK8uCbj1LwBcfrGyVuqJ4-nNXvjgC5uCp0i__YM2gM-x_cH1kAq5K1hujDKAHru6XC-uqmavFMRvkKKURBr_mYHRO7xZXB4qzJncye3MGKxaE7qH2zYx-CHXUM4f3EclNMbNuC8zv2poj6XWRXP6sLWi-WpGg9abeOn2zmFTCJj6eVNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e80f1162.mp4?token=E2Tsolk1STZgHU9hXS6b7StqsuxrDKssZns_Q3YJ2eZ-hHadJ4Ifk5zF_zhXGDTxBFdEnHFTHeue8kWgcCEi_Skoc9eOYyIzWORXGCT-Lxv3hDyOBkJ1BDwIPAVJpbXWNTu3IxWEUyPAkRzbLuEMEarSp8UZbbTjpjMxbaK8uCbj1LwBcfrGyVuqJ4-nNXvjgC5uCp0i__YM2gM-x_cH1kAq5K1hujDKAHru6XC-uqmavFMRvkKKURBr_mYHRO7xZXB4qzJncye3MGKxaE7qH2zYx-CHXUM4f3EclNMbNuC8zv2poj6XWRXP6sLWi-WpGg9abeOn2zmFTCJj6eVNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Legend
🐐
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98939" target="_blank">📅 00:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98938">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پایان نیمه‌اول بازی کلمبیا و سوئیس</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98938" target="_blank">📅 00:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98937">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilLpA8ceny5Cs7fY_-m4e_XZ9ysr8NoGy5jc14E1lYnd7RRAHEXYwAzF5rqloc7itGr9lmNR7scEZ9VcCGkG2NE5BlJN0GYFm33wFFj_0ew7HeCoNr1W2lUCXODPtmMwPl7IK3Te_EEfewitdvsloeNdPBhfYej9Ke_8SZT1qh2ElItrV7Wd4aucU2A20cX-aRpUz6Yh3sQI4GEAMd-m9tZ6ZWwFBn1AN0PNkgy1ass_RlTu810ZZIbXP_eX96ZOJOUKIzF4o7ZzK8-Dah0d4CJ1CyC_xeaskCkQD2f1eKur0aZ0XOqvE7-msoLVOxkGaRBDSxfqfe8UAmgInYdNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇬
#فوووووری
؛ جیانی اینفانتینو پرچم مصر را در جریان مسابقه بین تیم‌های کلمبیا و سوئیس به اهتزاز درآورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98937" target="_blank">📅 00:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98936">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3e3abdb3.mp4?token=Pdu6_P50ZzZfSBNIsza8l61FiaytPKM3g8EIeHVKbkN-2Nab0rm2sNblsR_uu38pvvowMFy681rDXTq3QLrEpPeDw7huriUw1UGBKbAeUb9fx3SLRoX-VyseHHrTsCSR1AZZhLEeJVewMN7dNoaiaao97xNba46tNIU4rrnXAJ-Hv75gHR4pC9O00IvPG8NqGVCKYsjq-9JusIlenzzXbZmvZfkHRaNsuhYND-bMGCSsS5c_iJf0rgsponnIiFfdFlX0PptkYLyjFQFGRDzldC0NDgKUhuUHQN7pWcASKa9EllxGiP-DuCVyHfTnwC5LjIB4vWmMFwtjgIlFZ4eR0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3e3abdb3.mp4?token=Pdu6_P50ZzZfSBNIsza8l61FiaytPKM3g8EIeHVKbkN-2Nab0rm2sNblsR_uu38pvvowMFy681rDXTq3QLrEpPeDw7huriUw1UGBKbAeUb9fx3SLRoX-VyseHHrTsCSR1AZZhLEeJVewMN7dNoaiaao97xNba46tNIU4rrnXAJ-Hv75gHR4pC9O00IvPG8NqGVCKYsjq-9JusIlenzzXbZmvZfkHRaNsuhYND-bMGCSsS5c_iJf0rgsponnIiFfdFlX0PptkYLyjFQFGRDzldC0NDgKUhuUHQN7pWcASKa9EllxGiP-DuCVyHfTnwC5LjIB4vWmMFwtjgIlFZ4eR0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
لحظه گل‌دوم آرژانتین و واکنش اسکالونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98936" target="_blank">📅 00:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98935">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a31c10f53a.mp4?token=EiHC5fN6hp-o7XwSMA6LReXvnueU9Ay3cpYBIDoeuVtH-42Ihd1cOIj7d3RyTJUFH2eTDqsKa1gK2QYzFV4KypMRu9LOpMPZ9BPwNTynU0s6paG4xDPMVNVp1ZmWwhtqq--V1fwPKbJnGQ4J7DAlyCmHl4UXQwfCxqMn1A2hxrPVPaO0CqLYGFIdHlWoaBgo5Sw6_W_Xr9Eokq1v4C4y85zCBK8s2bc9ZDn5S1ykPZ3pwp_iuVJDYEAqyLd3Fe4xTZltB6tl4LFsjw64797vDq9Zzbmt-00WSAVX-UiOlpnsL8yts5n9rRSfxdGtVi_3-8VWU0c1jeJY3o3asEfPcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a31c10f53a.mp4?token=EiHC5fN6hp-o7XwSMA6LReXvnueU9Ay3cpYBIDoeuVtH-42Ihd1cOIj7d3RyTJUFH2eTDqsKa1gK2QYzFV4KypMRu9LOpMPZ9BPwNTynU0s6paG4xDPMVNVp1ZmWwhtqq--V1fwPKbJnGQ4J7DAlyCmHl4UXQwfCxqMn1A2hxrPVPaO0CqLYGFIdHlWoaBgo5Sw6_W_Xr9Eokq1v4C4y85zCBK8s2bc9ZDn5S1ykPZ3pwp_iuVJDYEAqyLd3Fe4xTZltB6tl4LFsjw64797vDq9Zzbmt-00WSAVX-UiOlpnsL8yts5n9rRSfxdGtVi_3-8VWU0c1jeJY3o3asEfPcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇦🇷
وضعیت رختکن تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98935" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27ddcab60.mp4?token=ubnBVKNFWhfj5QFMfj0B8pX-ztHycCSBIK7PdrtwKngpqFsaK8KWB_FK8y_KexRErqMPvZ7dhbkAXa9aZxpmO6SZIo16f6iGfudu5P8RloIMQK-GA-xf8nCv9-kLgccsPts8Qi2fhbb0JxxJNKDfEPDdZ0dd3Fsy6MLFLhEYGez5Hrji82kkz32YUMj7cQ5XlPFubBg1i79Knmzf2Rhzc1JP7bBh_2RbrelhkfTURZs-UJcCE_73sr4gRsQhfbtNwZprviJ8nXpgY65BvdUFBLaf4szJEISZf8TMnJXl-gO32Ei3NPCW80wvGpHljl3ipSJ8Rxc_RrQ81GYVAZT3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27ddcab60.mp4?token=ubnBVKNFWhfj5QFMfj0B8pX-ztHycCSBIK7PdrtwKngpqFsaK8KWB_FK8y_KexRErqMPvZ7dhbkAXa9aZxpmO6SZIo16f6iGfudu5P8RloIMQK-GA-xf8nCv9-kLgccsPts8Qi2fhbb0JxxJNKDfEPDdZ0dd3Fsy6MLFLhEYGez5Hrji82kkz32YUMj7cQ5XlPFubBg1i79Knmzf2Rhzc1JP7bBh_2RbrelhkfTURZs-UJcCE_73sr4gRsQhfbtNwZprviJ8nXpgY65BvdUFBLaf4szJEISZf8TMnJXl-gO32Ei3NPCW80wvGpHljl3ipSJ8Rxc_RrQ81GYVAZT3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
🇦🇷
احساساتی شدن لیونل اسکالونی بعد از کامبک معجزه‌آسای آرژانتین مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98934" target="_blank">📅 23:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4uR2SUhssqG_tz1sYMC-wmDjbRXf3lSNTJZ1E-eYkqDV4jsTrz04HtcB37dSqes2BTuNq79tSbqvj6JyPotrDvDjNvPq-C1QWXcGPeyz-dokciqxTHFNesTw6tLVtC2n6CYtdMryIkC1hMVB6x4RZ93CZbKMMthBHg2QV5MQ2mn2frlw_jalK3ILerkbxcwHXPW-W-2U6QU6q-4Ly6QFpQOYLr0OC4O0oO7WYfuc173yUPnG3J8E-o64ebEKCMM6zrdZPaKN9V9wAIfW0fuw9Ox9NRfFkkNTRJFn7wYGqJeIeiC17bhl59HZeCs1y5SO-Jd0n5gA_l9zN0o7GV7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادوم زمینی استراحت نداری تو
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98933" target="_blank">📅 23:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98932">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5jd3xZk0-VuRz9KXipDu_fzDOJixP9SESzQH3MFPl8RE24mMAL42u18FmUm4fPX3PxJKs2dHghdlqpBOr69p57ZnT_lDkOWgkFaSwe6HDDm39WK_rR343oMKscfyLkEU5J6rVH3Zrr6eH6fH3MnUvcmXc5uKipXTvYQRSpNDyZOefWxPKM15nkBjx0ntHoykBaJiC4i4BFvACWt-YA0xvUgpIbiAKGjnfYudo9BPCo6COJMIsA3yki3KAOT5B8lHANF_s1UXFkPDgYi-FYzHcKh9RuE2T4nRkXG6H0HkDZmF-5_BCDibO13kyH9AAcPOPAGET_wTFnhizlgegFTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عشق از چهارتا عشق همچنان داره ادامه میده..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98932" target="_blank">📅 23:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98931">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شروع بازی کلمبیا و سوئیس</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98931" target="_blank">📅 23:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98930">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCK41bKAF5IYP_gMJQoihbPbz20BoL13sI7trcVUnsy5tc7pN3dkVID0hZQQLgZhni_nHS0CPjAE8zJcmih_kIa8mp8TfumUvAeyggW-qmUMJo2_C-t6X1NFeDXF-aUf9vZjLEnQ11Se8B2A09yuCgbgboHvn7u8zJqO5jl28Hxt_rAuBVt8jC411XHXnK0VC3IlR1s2kLYg8sJLTdtA452_HoPnDr11bUsxyVZsOM90InHVuc4nmquNqEU-mmQxVaQZ5VFQQYAwALnSiJBtuE6lss8XL88Vn5T9If3-uMvRYKYFe_wZdf6l1ttkOx1lLxei2pPzUseqJgi8w3QFPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
اسکالونی
: همانطور که لئو در قطر گفت، این تیم ما را ناامید نخواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98930" target="_blank">📅 23:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98929">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ub3fWadTuUpdC_SMCr2Jvd6MshLYqG-pMOiit5lujIHc6X11vQULTV0MhfMWVjObo7EppyVJVAA3Z0bQtmUk3RhjrPpPdmrMB7RkbAuBzdMKm7mXMwFhyIZJ6ASl1WYDzMB3du8t2j-J-vCDyiK_2WzGF6Z3-504ZJvRukBcmROYcEAINyNT5OxL4sCo9MrHJIfzzWtTnh1P8-gjjp7uP6dp5FtPsLejwvVcgBTlZXozrmNN8Vh6YFZqgnw6UmDewXpySfwuxMBRdSQ1KzHC1LNng3BHKfHlKo1moHy3dOZoZT3GJX21Y9rqKj5SY5PV5gZaCHHlxq5CeeWuJIyOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه ESPN از مسی با این عنوان استفاده کرد:
"تنها او می‌توانست این کار را انجام دهد."
فقط او می‌توانست این کار را انجام دهد.
🥶
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98929" target="_blank">📅 22:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98928">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
🚨
🤣
کون آگوئرو بعد گل تساوی:
‏"نمی‌دانم که آیا الان دچار اختلال در ریتم قلب شده‌ام یا نه، اما اگر قرار است این اتفاق بیفتد، بهتر است همین الان اتفاق بیفتد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98928" target="_blank">📅 22:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98927">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwbSsD0EJoVUgeAItNLIEBqj_QECZEnQhHyl0ZGIMqPYvWKkXn5jiajikQSZvUxtTywU3ibZYNCD3tx1KIfbTBePYPW890V8kFbT1HlMMHO_ridFc9KNeq6MEROVl7Bktes9Th5_4iEAECsBQ1Do0wk5RVqMbS-DYAjWFLlJQNVQSY8dojIuqGuFgXt92Y8yfPi8BsdQ7lqtL8iTdP3y1gxjERba4y6zzU9BjUgGRAf2seymmK0tiWoX_3Iqo016fBL2IvGPMv3x4V_qK34eusHfyhUmRKmQE--wzmblKmrxpsKxThAa17wuQicaeafE1ID5nC7PspfMxwjC5t2tPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
گل انزو فرناندز، گل شماره 3000 در تاریخ جام جهانی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/98927" target="_blank">📅 22:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98926">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
🚨
🚨
‼️
حسام حسن، سرمربی مصری:
‏" ما بهتر بودیم، اما فوتبال عادلانه نیست. ممکن است آن‌ها بخواهند قهرمان جهان و مسی همچنان در جام جهانی بمانند، به خاطر مسائل بازاریابی."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98926" target="_blank">📅 22:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98924">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MUMv5pLatrDUI5O5msinRXjdbjaqafHuSueXIReqLGstkuoZ1pdwHwaMvTCORMnNJSF7yZcDiPdbAlQygXuQLFIGQt0FEtcMFCGSrHAtY7ZEClRZtT2N0wP2BkSYL6QTwnirv1WUDTjBgNrXOmH5YIWmniwBaQ1WfJUnJ3ux_FhwuX3wHIM6_k4sWTwfiPjciFjaPWHrl024LQ-Gf4iOZDBzCGx3Fr5tGCHmvkdDOAxLhekzZeJoAGisBL3l8GTU-_LrmrFBzg5G0QvTiJ-ddqaxCclvLsNnDLmL1A2eo_vEdstqOOSRME3NtKTMWUyeDtZSU8ZYICxoj7FD5b_NhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCruZnnePOf8ZlUY8qtKKThxiH9Wr1j9boo0jk3XfO_WcWCS5W45bfBfMFVvma1R0iEevRVlGaTzsr1ObgKjqIZ7Wzz_9zUaJNud7Yz5M5GwpmpUb-bp2BHstEadEfYtJbUhDN6zRTYTV__nPq8X-8kUPW0ER-qWGr0CG7hY5_31yHtuZc6ad76OJLe7xRwyKUlHsGg6u_qML6hZsCwVMfuGDMxwjMZFWf97HCze3FMCGttryS77kFozKjKMTskUqH9q15RWdzG_QqPmpsWqXj8nezgSkPGEPnnKim_w7CUfmUtJRf0Hl2vHOZnDlOrID3-BqRlVNKE7lSSQ0dn5eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇭
🇨🇴
ترکیب سوئیس و کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98924" target="_blank">📅 22:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98923">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxKIxadJS2jxZLI8GKNkzbdd_4GLTcmpq0bCLlhx49A_HQxeGabsd6Hdy7Q1zgqfRCpHcIELNGCYXRDPbRd9IRCpn9miN-CVOSlY9tEt0Wv7U5wmTYw8MkJnc_zIlVNgw6kiCClb8MNQTUn2e3Rhi3LxVcdGDK2zAYWrOzf6Jdsps08sttqO943VA3z5_dAwJmBhb_2TdjbEFZb8Fb17xPDXDEidBvVy5ADuKvTa07yY46gu_x716NdVbeSfHEtf0d7JOG7wHIJMTBVtjH--MyNIbdNBxuWCTHYBqiIe55xjNt2LayA7_3IOt52d97K0zn_VTLaXS3s_s2esDAW65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی با 39 سال سن به مسن ترین بازیکن تاریخ جام جهانی تبدیل شد که در یک بازی حذفی گل زده و پاس گل داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98923" target="_blank">📅 22:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98922">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j44PZ9xKxgam565DXQLcdu9TVMLcfryAnYhXXKuKgufRr-M9ZtmS-4AfPe6q7z51r7vionNtYbVGskMgc1gTXRtCDDQzlTrZbEDMQjolUZDZhUMMOqilPFt82kNXH1UA18b6DkGIqHyHCvCodjjj1Xs8Z2Pwau549tku_NBEIhmSApfhQKI-5RSfCxPgPsxon2HdDyseQtM1IsRnvPshKvR_IsQSMRf67w6Q3RwIir-Z8W--VCbnpXKnJgGcuEKlohWYExT6GzjkrvQbyyj3f-TRsEIVoftkHSlreoeuU1I4JdM2fZLU2-TVIsiOUqTtck_jQomguFNT1T26sCG_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
آرژانتین، اولین تیمی در تاریخ جام جهانی شد که موفق به پیروزی شد، در حالی که تا دقیقه 78 با دو گل یا بیشتر عقب بود (3-2 مقابل مصر).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98922" target="_blank">📅 22:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98921">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ut_JpwBaEL-5eH2-ByjTxbxn9Jqk0TQY7NFypFxsTXZwwwCKdcbcn9iLg83hvCm4_RXudPfUDBjyVLWvKNwYs3EVguVjVnATE-DhiNOtaq4oeULG2hvttM7X3lqSPi6aQjjOTVb9QypGFD8X-p-Agb3n4aRP3ct2x1PNbtJJOowE-loEDk3qAIH-VRALUGPmr9L92TqwV_7hqrYwaDGdHn6Vxo1F0xhzd0OqihwnQQ0sv2AjjVYBH8WW0pdVBZUbb_i5yPJHkhl4pGqXoA_AKk6YiMKMCy01GTd30N9PslCDxrMB7pZjy9VsBK69CgOYLnNxeD2Cq35-ISkJygCRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادتونه مسی رو بخاطر اینکه جام جهانی ۲۰۱۴ رو باخت و گریه کرد مسخرش کردید
یادتونه مسی تو کوپای ۲۰۱۶ پنالتی خودشو خراب کرد و ارژانتین حذف شدو گریه کرد مسخرش کردید؟
یادتونه با ۱۰ چوب در جام جهانی ۲۰۱۸ بازی کرد و مقابل فرانسه که قهرمان شد اون سال حذف شد و گریه کرد مسخرش کردید
یادتونه میگفتید مسی تنها توی بارسلونا میدرخشه و جام ملی نداره مسخرش میکردید؟
اون الان هم گریه میکنه ولی اشکاش اشک شوقه اشک که بخاطر دومین جام جهانیش ریخته میشه اون ۳۹ سالشه ولی هنوزم بهترین بازیکن دنیاس
پس الان شماییکه ۲۰ ساله ازش متنفرین و فقط دربارش کصشعر میگین گریه کنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/98921" target="_blank">📅 22:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98920">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ips384o5ASoEqUVjSeMOPeTMKmiFJhLjc_aq2-RgnUnc1ehXgo2xjAaYZKVTlI1ssRXy1VZdjcxQmXdNAoqHcmmTAM5C-LHUi4Zugc0hgIEuNiRd6bPdxIB7Nk5zY_AmXp-RzaKmyiRs2vPR-uYvhzEvkAG4oQgZ9rMntU6QgyfT4d-jwUHZWbhJsDlbWxRCfvl_XzhVxHEmEZ5BGeNVeEHRgx0UOJTdOTE0YTqz99Q658OwrIUY8WyOtIywikGA8vxn8zi_U1K6HLv3VNt-C9LdQiD-Zhs94Wk7AGRAAiu1mwY0qyMqZ6kpS74Y68fZ_ozuckhhQ84GgDkiruBIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
زلاتان ابراهیموویچ درباره لیونل مسی:
او به یک هیولا تبدیل شده است و هیچکس نمی‌تواند جلوی او را بگیرد. او بدون توقف به پیشروی خود ادامه می‌دهد، و این همان مسی است که من دیده‌ام، همان مسی که ما به دیدن آن عادت کرده‌ایم، و هنوز هم امروز او را می‌بینیم.
به یاد داشته باشید، او از قبل قهرمان جام جهانی شده است، و جام‌های متعددی را به دست آورده، و توپ طلایی را دریافت کرده، و همه چیز را به دست آورده است. می‌توانید به سابقه فعالیت او نگاه کنید، که بی‌نقص است، با این حال، او هنوز هم بیشتر می‌خواهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98920" target="_blank">📅 22:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98919">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_PgNsi8QpTrUpPGVRxZieJ2WZn4w_bHp9EFxyuSvAL6H5fX7bcyfxX895MLSffOKwXFmoOIUGf5UHUfCeMnMEnK_oDb5hxoI_7DdqR_slANc77U0E1Z3dGu_-gEYeuB2kUVNg5iP83dnck4BqGRGKt-tKXRfCd-stTAEmRzitoFw0U6_B8Lz49l5YllAlFSZ3EPDS_YcBF__uUW7I0cgW4y05ky5k5Vo3rooB0HbcXnKbNc9PuXAqULQguJQNu5Jw3DnFafmhACQ3pXdMV_jEi08DzefSO_Y3cvGKvJXjtBXtPvhF1jCKBxMGxAHmLj93paGtaYBCfkVhXMNqRyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
– آرشیو VAR:
• در این صحنه، پنالتی برای مصر وجود ندارد. – یک تماس جزئی از مک آلیستر وجود دارد، اما این تماس ضعیف است و توپ دور بازیکنان بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98919" target="_blank">📅 21:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98914">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk0aOLRV9DQXkydrDf0_tFC4_nypOMPVo3pvx2-4e7GN15nM0fn8985OlatLfivxZ6AGTAEOnBbBsTg_K3KlzgM0DFjJyNpYrvQa626H2oUHP5SOSnSmB3SqPw9JPnIGCXX4CtN3Ha0PpfbxbSl-ct1I8OnbQLtOv479URFQQ79ztc5o3Qf9dLEIj2__1g-ycVBj6ipwIgFqCSkIB4OKNm99OBYq-6JBRjSWVNsCFZqDC0ogPP3qMO0x3wbl7gkt5M4fP5TAGDmmFS-65bOv9nGzM_DYX6KQKNrlVoSr1mobw1A62DWNwa5bzrLL4QgQO0QrJrrGgOaI_2aj6iBgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/skGSt4eWrw3YQ7mouhrvVBW_dHksd5BP60T9gVtT0HR9gsSqwrHp9lxEn9T2X8EFww22ic6aeUaXyhend80pb_KoUYt8dRni_Z4Mhs4GPYI59sd3Sxf0dD_S_uINNjotyT0Hr9VO9edfF_hBAF6ma7UirzBg4F6yEe4F7XOTE10ms_zQ9N8aeyXhvQM94MjOYVQV7XPIMeSUJFZN3sAePm7J1APqnyn_c_P4QxnE3B42toJfn7JDS7aoC6OuIWr681Rmmd5B3cHnLd7cYKY_hHWz5NN8iQH8vP2rXgRJCgUG6BMyWgeq6Gt9CxdI6N3uQIbg-KeBatK8MMdw4Zk_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rju1qeGCC7olvKtT-A-LpmviBNYXvb8gmLi9gVEtdf0vtnBygbV7W-YodgX4no79RTq5ZBa9Y907dZWv2GzNUeGoJ4KdiYTrEMUA20J6o0SvTa3l2LBF6Tl2s7gut9zihC1KTwKRAfmtwsyHXlGMmiiz9vb45v4ynbQbmu98xh86PdKZeGceO8LR01whtdnFP8_EC34s7q0VLw7I3v7FqkB6ifphU4zfuqwaZjfIoWv4rPhHWVv73KTWpKiqk_lPgAHEZhFf3no0wDpeBEr0AnMlrmybeqA62JTtk8vzfZTnO15bXugyc_rDuV6ZMpXod6MAP_gOSwhrdL0cLvpOgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NjLTiIDhnLmYJGgf778K8M6_J7t7UIm1A4juRQZBmWoGkoliRJXINYh28_F8uClzI0xdOekH_8plq1RJDc1j8tGOwY-SLhyrp7jLtfEoXJfKHoqYvPWrBvEGETxKZvbGEgvsfe2qdfJ0YyfBsurX2qJIBP8pyMmZIo9V2ZHApuUU8lFeWC4WitVoftqbKn_dDN_Y3VSNmW_OOOkRCrtb9km5fBiENFIocpRWbd7zK6ukvSjGls0lgcRwpXk0gdkbaqOpAucV_PHFfWpKVRhoArbJnZsXooSYSWqGAe4vhrlz3PNVadWkc0H7n3042E2wM_1zWrJJ9chQHW1Np1QTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSxQPAWWyOhEQjKja9onfVSntr0rMk1PF1ItNzamxdtT7W9MXCO6ZtHAZejtPM9Yvq_T6i94C5pTSHdaeLS2FTTbAE1HvqCKaVABifmkdFXErZ0PibWvV00HhZ8-dckJAnR9Cm0xEtrnatG3Q1NWxEWiZhB3gb-4hZ2oApglXXdH7d6NTjmAAXJJUuBsiAcd7yW1z96MvFX3t3y0XHPRU4VmRfDDGzwkbLN2yLGMTdCoLq9xvWgnDn4OKB0vnjjgBeuKrsJU0S7CRKmVpb_DdcYUfDYgPZK90m01KM8Wnxupojn8H0QDwMJlhTK6spmb1nnvL8YZqdaBqzhLGL4B_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دیگر مخصوص استوری امشب
🤩
🩵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98914" target="_blank">📅 21:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98913">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مصطفی زیکو بازیکن مصر: داور تماما بر علیه ما سوت زد. امیدوارم خدا انتقام مارو بگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98913" target="_blank">📅 21:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98912">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDiXQjORDfK9chMhaXlmr1gS7Rlgc6BmqrgNLMp-lrZ76squyKDmruk6_uHsAvlpI_AiyIUOjvWQuNoOtaDF8GAZfqDU8H4CGUNl9cSWf5UcUXCV6sEbN_iPRIfE4Poj9C7Q88_7J2UBiQozNoAbZBbQXJY-4jUMSFm1A4sOX1ju8kndPf8NnXErpkOz3cP-7uvPysY6wnTPrE7fl9w-6hgxkoS01qikt3N5MYoZ5PjTV2OZACx_NPzhZOTIpGb63wN5yI27mkkOGUHEYX0_8cnoGa8CxtNvfnfhY7dK05PUtzjZosQzRY33KCgZEKX-Doc6Ucbwyewa1UVT-slXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید بعد کامبک
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98912" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
آرژانتین اولین تیم در تاریخ کل جام جهانی است که 3 تیم آفریقایی را در یک دوره شکست داده است.
- مصر
- کیپ ورد
- الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98911" target="_blank">📅 21:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98910">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHcFksALoCOgGAVyXFRVslffSjDcBAp9KFCMTD-bXvKAo2Kqd0U_FY54x5iIY-J8aeuCa-ywmWDYoa7lErSfs-jxEG8OIuVvu3YVrbYccnfLOOHMXZAYZKRqBfQWQKE3UouinF3MtDrus2Y0csK2r3XVSfaNA4O5CoAqJrDzrr2NLxLIcBmkOzA8xECOxSpeb8xB3kUCHE8VVGgA9xmnQo4bKqWT5AlUMou5e43QGxZBzqN21IOdgm8CdttDKx7AEXJfxW2OfYt5j38tIRfhQjgT7-fRHAB8UwSq34KWDbGgmSLGupCWY3IqVVAMX3wFP6mAzqzX73hFgBahbWwegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
اینه فرق احترام به اسطوره‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98910" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98909">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98909" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98908">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vupQv54CUTNLOfnMisQ7Vj_E1iMNEnTlHOQTWn6S4y0tFNkAgI2KN_N1V-ZfYQxxnbh5eVF8J33M4ZFC0EuEpGAEKurr47xGSGU_-YBy4V5NI6eufhmSL5BDp4oE6YXm2vDZopIr-CGGggy-jWOhrNRNAN7E-p3QTel34IsT9IOwPHbdiOneFfiVjYswdlNzG5a9KNIroiCP7g0jf9HwRA4rM0_u7zZtGcrUl2U-VaP3taN_fjVz-Dd3SEwnzeCrxggh89-UGro3Ly95g1pYcocAajbK82vaxQdGfgkJdA_JcN7-3DETN2YgIz7W_dF8tBhIHJim-k4T4cAR-lV96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
✅
تیم‌های راه یافته به مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98908" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98907">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrTX_bKK5WnEqBwtwdPGCtU4icj-kQa8Ih1V5T5haBo1trCqE6kx5HxpOi1OxwI4_fcncc_OlDCaPsD7qv0cGu3gYFNoIEDLAGmum8TYrwX0ty46rSP3Q_CTlb_k3dy-qy_JXS6L5l-9oEtfhWbwOkstBYk6njA7lKUlAErzF6gDDz2qZJgASIfnYYKuhhkFWsMCO7-xmetZz9JXJbwl7RDH3HuFwUaICiGzGXUDWChSlr0ZqBI8sDvQ8z_cua23YdLWLL8Qa7cg-zleHLL3LdL7RzpS53AjqMF-yVEFsTkvSPp934sz3XFZwo4iHVz-UqC-3lRPAS9oTyorVaLQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
‏بازیکنان با بیشترین مشارکت در گل‌ها در تاریخ جام جهانی:
‏30 مشارکت —
🇦🇷
لیونل مسی
🫡
🫡
‏23 مشارکت —
🇫🇷
کیلیان امباپه
‏20 مشارکت —
🇧🇷
ادسون پله
‏19 مشارکت —
🇧🇷
رونالدو (اورجینال)
‏18 مشارکت —
🇩🇪
گرد مولر
‏17 مشارکت —
🇵🇱
لاتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98907" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98906">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmk6AlMIVl-R6tEez_BLWrkXvAELa-TO454N-3miIc5usJp7elIiQd8QMIwLvRQrne-nrUHj5TjMCSCOuiQVM-LC3MRfeZ_91WKsG_3jJTz7tEZXWY2SEQBs8KxXgVFdWMDYYXihyizkNDILKDUQYicUH5i4YtjFugSHg_PDcy8j77_wGA-LgIKwcgrtZgWdAt-plx3LKPlocf0Sb9Rg5YAkRPexiMOJC4d6xtzvs6xeR1cOJKh5DxWTjNaw8gFQ0S58WLK2pm3CcbqaKQkIFs8c7KrIpz62dH20YV6RbHdI2yXiOMmd1yjvtYcqz5piKWearxLLP68GOR_NjaejMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی، اسطوره فوتبال، با کسب این جایزه ۱۵ بار، بیشترین تعداد جایزه بهترین بازیکن زمین را در تاریخ جام جهانی به خود اختصاص داده.
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98906" target="_blank">📅 21:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98905">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJFqO5Eir2NnVOjP2AhOQ2uVIAk9bWtkP7d8qfhurs3TYkDDPvsiPFcbZXxlq4wdClhgvnSuQvn5_r48W_RzSJfcE_1tolPBQqXRBKc1LGUt4M2WSYsx-6Y3o2yBNN-pWJBc1FzvjY_OiAx8h96M4fx_onJMdgdh8TbW3d2widfEDhkQOl9pP36YSiT-aGtvgtuNYZZIyy-vPwizkhFj7_mM_LDFtocTwtfvn4sn0OwscqHrIsbSxrHXN_3dymIpbIUkTluXIlZXF7Ew4CoaPLaKKnMIf0vZiKAuNndwTS4cFsJgi-IPNtPKLEZ0nIi8kAG_rokTPuYzvnfy_mMz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🇦🇷
| ‏اسطوره، لیونل مسی، در 9 بازی اخیر خود در جام جهانی:
‏— 9 بازی
‏— 13 گل
‏— 3 پاس گل
‏16 مشارکت در گلزنی در طول 9 بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98905" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98904">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnrmIvzTu9SpqFDUS3DBtb6apYpBRT0RNPH2Ad28uqStyHgCgEIaIfu6ggjf5K0mk7nojsmngZroJnZQnn_w26OJcRurLUAhwADD_BvPiC3liQDQvJcv6XPeIbOVr-GCh1JnCnIHg4xDpqqk0U1iD_sjb-KHmQc3Eo3TzTAYuFVb4L8hzfRaMRBfge2evB_Xatwf3XVQ6a-rf5rcSnq3bS6SW5Xk6Tuc46qh_5GI6L0ylEKcKTF5x5qfCUJnVcBEvcMPLLI-ZgGRw90uG72QXuOVj79AWtXjD56P0DKQ_w2Vnug_R1R4Q6ij6LnqZFNquAkf7mzBUkHCrF-utfm-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
افسانه لیونل مسی، رکوردهای خود را به عنوان بازیکن با بیشترین مشارکت در گلزنی در تاریخ جام جهانی، افزایش داد!
😳
💙
30 مشارکت در گلزنی در 31 مسابقه
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98904" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98903">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVBqqkO2Ga01ByA6yUg62rLw6dv0uhYDz-65Uz_32WB3SZ85OgDBhgIsdQQVWWDy-yxd9XqhpsyztvGw0cmFPE5JiX9Q62Q2MqkxQzdtqI1seZ3JQ8l5NFp6HNeG4rA92-8DTcipTFTSoerRu61FHphC52W6w7hZAhfvHEaakvBxr2z5qL7U686EcN7PNzL87AZ1G1xb3oF7hHsi4fSWUJhEyOOxFYq92sWMsBqPC8-h7hKJ82qeRpgflu9EpyhGJ2_jsmNT47nKcxFyuUjgL0K2VnXtSEDrR3qC1B8mailctbhhXUw7ZKVoAtI40w1NbIC7gl66lhCGR4EzXqqTeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
خایه‌مال باختی کههههههه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/98903" target="_blank">📅 21:40 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
