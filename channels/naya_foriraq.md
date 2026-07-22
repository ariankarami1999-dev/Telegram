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
<img src="https://cdn4.telesco.pe/file/BZMsyquTd5zaDHo2M1UcXS99CWhVfHLrdjTO8-g5tr8zft14YXCnDUUI-8-nM6emkDmTds9DKNIXmZI7FdBwKNOoefe-c77kh-qMbHh_8RSF4UCJH_ab0G_h6fBFOsWCqLKkQ6AcQmJ4kPdCO-ZoI3dv5hGgmqC-0lxxYfT1UhHjBBfE6BmrXhcrjecMjBhTsvJxiJ65S4F7qz_3HC0Uqx9lnQT0CrYajkhvG-sYepAuBrB-c2bN-fcrTl1eNcoCiYNoz15RcZZWWV1xpiFBo-5cdXIQuVNXhqASN62o4aCh6QNGnceY-emly-OkTxcQbMsd-v1ubvxY0ZzfRXk2yQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 21:16:59</div>
<hr>

<div class="tg-post" id="msg-84896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVQiBvOSSnscZX68UBgK04FMW24Zqs370CLcEfzpvlMklCpfJ_FtN6rdWJxE8jBzykSSO5PvRMXeuCz0ghd2iMCzg4La4T1gCt3bjgaqk6qE58oFTDukGg_7zdanguka1vzwWhxEIKe-DSJynIlggN1I7e6XvSO0iORExTT1pRtHo7bmVLoIz00ff7XEpo8XvmLmivIb47QBOmYBKieDjgBc0RG3eMaL027tIlaTGyKMDtGdo7uL74tUiVQZIt6NxsT_VovMkgifaq4xWKEMU7NGjkoWTAkk-sDDa70d-U9D0paTu5n84smLlbemtOSrsjegH2rl5dwAJAKDsBbQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا قائم الـ محمد</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/naya_foriraq/84896" target="_blank">📅 21:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84895">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة ارضية عند الحدود العراقية الايرانية من جهة الشمال بدرجة ٢،٨.</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/naya_foriraq/84895" target="_blank">📅 21:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84894">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9adb07c10.mp4?token=jqtRUk-Miv3JFUwt7XOFurtuPqWiMEiGkqaEO7YPbrpVEVHhPj2x3rsa0h6gwS9ID8yltd4rQFBrBftjgrR7OwagDrFRcBvlzD1h9ndjwXKRcM2XfX_5pnhe2Vu07aML89CV5qjU7KIDHUOjT1G6dPuPlbBl4pHhw4-tOFEcjn_oZdTo2qrfWZd0sTSSPveynXMXF4AQC5oVFRoNBDTqOpW5w_KoITpnAwh10sn4eNNHjOOOc02FKvd6hqmNBobOIMdzXKd5mZ2t0kNNxe1AV3pN-p2DhkRaCIqdgcdm_aRmKwJyQUFltANptV9p_v4mCBsUFDfr4zH8n57A5IdIbEz99mpa3IgttpJL1fzYbSH0S_kv59VzI_HEUFe9QXAf9f-j-F5lJNjlCWO-jI6W1GKznYbxt3go5wK1Ubw4HpLY4xfqEE_OvRG1MSmXIYMizRPz0_e7p9ZMnPOd4m9V983fzJhhVy5YdBTvn2lL0Gvqb1OhjcJ_3YNRJVOigk2ZqjyprrTPZeqrPYiNl3AN-C5J8CLFCrWS7rhJB7yta3fxLkjfPTKe9ydMxYhhU_TBRB21zk9YbfqITWswW0uTqOo2jmWiO6scPc_H9caVYbz-5Bt16H96hwwdIM3ipehfkK8hGhg8Jf5Rg8WB7ntjVaGc1YtvvQw9NPA7CIQj1xo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9adb07c10.mp4?token=jqtRUk-Miv3JFUwt7XOFurtuPqWiMEiGkqaEO7YPbrpVEVHhPj2x3rsa0h6gwS9ID8yltd4rQFBrBftjgrR7OwagDrFRcBvlzD1h9ndjwXKRcM2XfX_5pnhe2Vu07aML89CV5qjU7KIDHUOjT1G6dPuPlbBl4pHhw4-tOFEcjn_oZdTo2qrfWZd0sTSSPveynXMXF4AQC5oVFRoNBDTqOpW5w_KoITpnAwh10sn4eNNHjOOOc02FKvd6hqmNBobOIMdzXKd5mZ2t0kNNxe1AV3pN-p2DhkRaCIqdgcdm_aRmKwJyQUFltANptV9p_v4mCBsUFDfr4zH8n57A5IdIbEz99mpa3IgttpJL1fzYbSH0S_kv59VzI_HEUFe9QXAf9f-j-F5lJNjlCWO-jI6W1GKznYbxt3go5wK1Ubw4HpLY4xfqEE_OvRG1MSmXIYMizRPz0_e7p9ZMnPOd4m9V983fzJhhVy5YdBTvn2lL0Gvqb1OhjcJ_3YNRJVOigk2ZqjyprrTPZeqrPYiNl3AN-C5J8CLFCrWS7rhJB7yta3fxLkjfPTKe9ydMxYhhU_TBRB21zk9YbfqITWswW0uTqOo2jmWiO6scPc_H9caVYbz-5Bt16H96hwwdIM3ipehfkK8hGhg8Jf5Rg8WB7ntjVaGc1YtvvQw9NPA7CIQj1xo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
وَلَا تَهِنُوا۟ وَلَا تَحْزَنُوا۟ وَأَنتُمُ ٱلْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
@Naya_Press</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/84894" target="_blank">📅 20:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84893">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انباء متداولة عن عمليات اطلاق صواريخ ايرانية نحو الاردن</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/84893" target="_blank">📅 20:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84892">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇱
‏
الاعلام العبري:
التصعيد الأميركي ضد إيران سيؤدي لتدخل إسرائيل إما بطلب من ترمب أو كرد على هجوم إيراني.</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/84892" target="_blank">📅 20:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">واشنطن بوست
تدرس إدارة ترامب خيارات عسكرية في مالي ضد الجماعات الإسلامية المسلحة،</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/84891" target="_blank">📅 20:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84889">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ليلة ساخنة جدا</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/84889" target="_blank">📅 20:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تم إصدار إشعار للملاحين الجويين لمنطقة معلومات الطيران في بغداد لإنشاء مسارات مؤقتة جديدة للوصول والمغادرة من وإلى منطقة معلومات الطيران في طهران، اعتبارًا من 23 يوليو.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84888" target="_blank">📅 20:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c060d1357.mp4?token=XZVnGqFrONhaHd4n3w--m_fqukv-FLN1aSuR3u2CbR5UeEz0p3YyKo1F3SmJ6MmkJ9DDAhva3wIQYzRGHOBZV7CYlVsdTA3pZn0W4hyx3Y95mRtHFnMK7sJT4XBOC3o4M5hFxmd84jaU0b9gNWcYVwuzfjEo-xi0dx2Ibnt6Fqd8wx5BZuypih1bZEqQohBycAO75fkjgqqv4gfonBti7ilv2EjQga5OvhtmLdvAgA0njMDW-ezdnXOuyLeEh4mnYTN0C0d0D61GA7cnNCDmbM1Wf9bEB8ahN8Ta5jbX1VnLHQpmIFRnw2Vv7cgzMNfjXjtWOTRe85CUg19LCPBiuFg3rg8h7Wo3NDHtSWSpyZYmym_r4ReewpAfoGSDR5F2iDZ7BNgZTIYFqAxKwwfb5ralL6O4BvPAaRpurFzvNbASD1BPIEhZ8dRSvgrtvmWfDvbU-tl2RnBSxk8Aa2J3LozM4P6pGJ3b_5r60CJm6pB0WbNX0ONS2UPKXVHRySbN4GPGvAdLolRVOxwHD4KF7JR8wAgf4S3nBnsWX0XfyP8nU0aqj44qpWfk6WLLD6NtqeIwriihpLZiRkgez-WCNee7o8oXVLooq2gX3XALTA92arPyfI86Mz_7-7nYhu2Q3kqaSJMqNHlZhQXsnBizl-T76wmpDaW2ckt1XW55KzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c060d1357.mp4?token=XZVnGqFrONhaHd4n3w--m_fqukv-FLN1aSuR3u2CbR5UeEz0p3YyKo1F3SmJ6MmkJ9DDAhva3wIQYzRGHOBZV7CYlVsdTA3pZn0W4hyx3Y95mRtHFnMK7sJT4XBOC3o4M5hFxmd84jaU0b9gNWcYVwuzfjEo-xi0dx2Ibnt6Fqd8wx5BZuypih1bZEqQohBycAO75fkjgqqv4gfonBti7ilv2EjQga5OvhtmLdvAgA0njMDW-ezdnXOuyLeEh4mnYTN0C0d0D61GA7cnNCDmbM1Wf9bEB8ahN8Ta5jbX1VnLHQpmIFRnw2Vv7cgzMNfjXjtWOTRe85CUg19LCPBiuFg3rg8h7Wo3NDHtSWSpyZYmym_r4ReewpAfoGSDR5F2iDZ7BNgZTIYFqAxKwwfb5ralL6O4BvPAaRpurFzvNbASD1BPIEhZ8dRSvgrtvmWfDvbU-tl2RnBSxk8Aa2J3LozM4P6pGJ3b_5r60CJm6pB0WbNX0ONS2UPKXVHRySbN4GPGvAdLolRVOxwHD4KF7JR8wAgf4S3nBnsWX0XfyP8nU0aqj44qpWfk6WLLD6NtqeIwriihpLZiRkgez-WCNee7o8oXVLooq2gX3XALTA92arPyfI86Mz_7-7nYhu2Q3kqaSJMqNHlZhQXsnBizl-T76wmpDaW2ckt1XW55KzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترمب يشارك في استقبال جثث جنود أمريكيين الذين قتلوا في الأردن والعراق.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84887" target="_blank">📅 20:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84886">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/84886" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84885">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
ترمب يشارك في استقبال جثث جنود أمريكيين الذين قتلوا في الأردن والعراق.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/84885" target="_blank">📅 19:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84884">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
انفجار في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/84884" target="_blank">📅 19:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84883">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:‏
من المتوقع توقيع الاتفاقية الأمريكية السعودية في الساعة 20:30، والتي ستسمح للشركات الأمريكية بتشغيل محطات الطاقة النووية في المملكة العربية السعودية، وليس فقط توريدها.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84883" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇶
انفجار في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/84882" target="_blank">📅 19:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
مصادر ايرانية توضح الاصوات المسموعة في طهران من ليلة امس سببها الدفاعات الجوية .</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/84881" target="_blank">📅 19:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f6e0d88c.mp4?token=P1BPn85hRWoo9Rodo01m0uho78B9XcECfXDhU6-UmDIpD_5Sf7rHIGhGY1SAVn12zJZ8CeG6RruWOEY2FVyDpK113qEdLnx1c2lFpMY-_fCGO7PKVecM-0pEbrnrvEQd4rmDfQuPX99BDPbfFEp1wVYYGdXZh5RXFtAVqKksDLAe4jStLlh0BlcdkvilbMpGpGgMyznMIeS6TnKfv49yqZhJ82wyfD_LhQ1eUC9tnwgnT2_Da07Ob29RLpuYqhF5FEIuf9cWWgOo0Ir3VbLvU7oUdeqT4DZy0IiMhgXxbG6SBsKwIcMQGhqHeg_inNmad-Pco39Ar9Qg9v6aS4Jx8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f6e0d88c.mp4?token=P1BPn85hRWoo9Rodo01m0uho78B9XcECfXDhU6-UmDIpD_5Sf7rHIGhGY1SAVn12zJZ8CeG6RruWOEY2FVyDpK113qEdLnx1c2lFpMY-_fCGO7PKVecM-0pEbrnrvEQd4rmDfQuPX99BDPbfFEp1wVYYGdXZh5RXFtAVqKksDLAe4jStLlh0BlcdkvilbMpGpGgMyznMIeS6TnKfv49yqZhJ82wyfD_LhQ1eUC9tnwgnT2_Da07Ob29RLpuYqhF5FEIuf9cWWgOo0Ir3VbLvU7oUdeqT4DZy0IiMhgXxbG6SBsKwIcMQGhqHeg_inNmad-Pco39Ar9Qg9v6aS4Jx8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
النائب ليو ينتقد مايك والتز بشدة
: "أنت لا تعلم حتى عدد الجنود الأمريكيين الذين أصيبوا في حرب إيران هذه! عار عليك! أنت سفير الولايات المتحدة ولا تعلم حتى عدد الجنود الأمريكيين المصابين! يجب أن تخجل من نفسك! يجب أن تستقيل!"</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/84880" target="_blank">📅 19:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
‏مادورو رئيس فنزويلا الشرعي المختطف في اميركا يصل إلى محكمة نيويورك لحضور جلسة استماع.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/84879" target="_blank">📅 19:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84878">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">▫️
‏
غرفة الشحن الدولية:
الحوثيون في اليمن يوجهون تحذيراً لاسلكياً للسفن.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84878" target="_blank">📅 19:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84877">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjl9dMGqPWUQDbQe8IIKxGZ-88pHEHJQ8nK_VGc0KTZTTWowL4jnEBNCEpqFXoqGStAkkaw_lGH3pByo2RSzC3r3rF48dhm2_gp-TFucXjpU7msBErDXwC7Jy9f5aLHRGOKaVsmi6OeqRb2PTRunI4fUymFImrjMxrfIw9M2qUrPwG_N-L4zalGA9K_y71VA_Z7mNgAfxzguw0B4y0mwdSjF8rdB68OTJt4vk1FpbfHYsjZ2q7nE7_V8Hj0uW3UaoTi1TYA17sxMoOO-lBSiFUOell8EDqdfbR74cDruYmVvyat6fvYRqzLWLUGuTRjC-OpWbGnucLUNjyKIrl0O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
أسعار الغاز الطبيعي الأوروبية تواصل ارتفاعها، لتصل إلى أعلى مستوياتها منذ بدء الحرب.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84877" target="_blank">📅 19:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
مصادر ايرانية تؤكد انه لم يحدث انفجار في بوشهر وما شوهد في الاقمار الصناعية هو لشعلة نارية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84876" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
🇮🇷
مصدر عسكري للتلفزيون الايراني يرد على تهديد ترامب:  - إيران مصممة على ممارسة سيادتها على مضيق هرمز، ولن تسمح بتحويل المضيق مرة أخرى إلى مصدر تهديد ضد إيران."  - إن عبور السفن عبر هذا المضيق سيكون آمنًا إذا تم ذلك بالتنسيق مع إيران ووفقًا للترتيبات الإيرانية.…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84875" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
🇮🇷
مصدر عسكري للتلفزيون الايراني يرد على تهديد ترامب:
- إيران مصممة على ممارسة سيادتها على مضيق هرمز، ولن تسمح بتحويل المضيق مرة أخرى إلى مصدر تهديد ضد إيران."
- إن عبور السفن عبر هذا المضيق سيكون آمنًا إذا تم ذلك بالتنسيق مع إيران ووفقًا للترتيبات الإيرانية. وإلا، فإن إيران لن تتخلى عن إرادتها الحاسمة في السيطرة على هذا المضيق، وتعتبر ذلك جزءًا من ضمان السلامة على المدى الطويل للمضيق
- إذا استهدفت الولايات المتحدة أي جسر أو محطة توليد كهرباء في إيران، فإن إيران سترد باستهداف البنى التحتية والجسور في المنطقة، بما في ذلك مرافق الطاقة التي لها فيها الولايات المتحدة مصالح
- الولايات المتحدة يجب أن تكون قد تأكدت تمامًا خلال الأيام العشرة الماضية من أن إيران ستستهدف أي هدف تختاره. لذلك، فإن مقامرة ترامب المحتملة ستؤدي مرة أخرى إلى فضيحته</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84874" target="_blank">📅 17:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📰
أكسيوس:
ترمب يدرس استئناف العمليات القتالية الكبرى في إيران والتي من المرجح أن تشمل حملة مشتركة مع إسرائيل.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84873" target="_blank">📅 17:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84872">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9424056a04.mp4?token=NKBKzJM8U8tHFfjmmiF2fHoG2bBJr9X40gyU8c3NLGK4y5Maj2Ou6CHixeZHLlCT5rP9NiyKoVlTUlxESqCMA8Jyg8jWz5e7tnti2RHIg1I-iHaJtS7a2mx2wPr4pKsv8dtPVVk9QnTbdAcbpTK7ycY-03UTj7smaKfuVS1FfpT-_hYgYGPCcAJCpsJIP6oiU7ASVD4q24g1Ghh2GyIt-0Npo11wuNm5g7BoK8IWB_RryizctygFxys1oO0hVP_-DrJGvn8gP86x8YVkMhY0eoLLDONer-TLl7oEMix531-XqqiMtLfmmwYngY2-X2DeJYc0A1z55b6KYt9nrDxcAoVni_acF0uKS9hQjyKOKhpMphad4Lf0oeA0xOvu1J2YD4tWqdW6PSbG5dv1fF4A-P_hbu_w2D6UYJOqihKSCTyw-68x055nfAjPhWkzV3zNNxvruF8xuudNxKNutHhWkFrq7onkD4METrO_0g-_LtV4fjMqqBIZXSB_qWf2VFmVCr7N8yG5Ep3aL6LtEW_Pmpp6kxjbRTlnbiX1QiFTHFBVQbxF_nm75WZ5HGs7mcRm7NyMTKStSDwjtKZAHHU34WHDAtvzhWUCfcOom1FBaIzz4UGw4WvOIJ3nQ1J0eoo8HSYB3mc45uutKTRBDAGRaCtoi-h7Ocgq1vjFFetJ660" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9424056a04.mp4?token=NKBKzJM8U8tHFfjmmiF2fHoG2bBJr9X40gyU8c3NLGK4y5Maj2Ou6CHixeZHLlCT5rP9NiyKoVlTUlxESqCMA8Jyg8jWz5e7tnti2RHIg1I-iHaJtS7a2mx2wPr4pKsv8dtPVVk9QnTbdAcbpTK7ycY-03UTj7smaKfuVS1FfpT-_hYgYGPCcAJCpsJIP6oiU7ASVD4q24g1Ghh2GyIt-0Npo11wuNm5g7BoK8IWB_RryizctygFxys1oO0hVP_-DrJGvn8gP86x8YVkMhY0eoLLDONer-TLl7oEMix531-XqqiMtLfmmwYngY2-X2DeJYc0A1z55b6KYt9nrDxcAoVni_acF0uKS9hQjyKOKhpMphad4Lf0oeA0xOvu1J2YD4tWqdW6PSbG5dv1fF4A-P_hbu_w2D6UYJOqihKSCTyw-68x055nfAjPhWkzV3zNNxvruF8xuudNxKNutHhWkFrq7onkD4METrO_0g-_LtV4fjMqqBIZXSB_qWf2VFmVCr7N8yG5Ep3aL6LtEW_Pmpp6kxjbRTlnbiX1QiFTHFBVQbxF_nm75WZ5HGs7mcRm7NyMTKStSDwjtKZAHHU34WHDAtvzhWUCfcOom1FBaIzz4UGw4WvOIJ3nQ1J0eoo8HSYB3mc45uutKTRBDAGRaCtoi-h7Ocgq1vjFFetJ660" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يتجه الى قاعدة دوفر الجوية لاستقبال قتلى الهجمات الايرانية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84872" target="_blank">📅 17:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84871">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
بيان بعض الدول المتجاهلة للحصار الذي يفرضه النظام السعودي على الشعب اليمني صيغت بصيغة موحدة، هل تقبل دول بإغلاق مطاراتها من السعودي وإغلاق موانيها وعدم السماح بدخول أي بضائع إلا بإذن سعودي؟</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84871" target="_blank">📅 17:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رئيس المكتب السياسي لحركة حماس خليل الحية: سنسير على ذات الدرب والخطى</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84870" target="_blank">📅 17:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
استياء واسع يسود الشارع العراقي بعد انقطاع التيار الكهربائي عن عدة مدن ولساعات طويلة بالتزامن مع موجة حر شديدة وارتفاع درجات الحرارة إلى مستويات قياسية ما فاقم معاناة المواطنين وأثار موجة من الغضب والاستياء بسبب تردي خدمات الطاقة في ذروة فصل الصيف.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84869" target="_blank">📅 16:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84868">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامب: في أي وقت تطلق فيه إيران على سفينة في هرمز سنقوم بقصف وتدمير جسر أو محطة طاقة</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84868" target="_blank">📅 16:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84867">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامب: في أي وقت تطلق فيه إيران على سفينة في هرمز سنقوم بقصف وتدمير جسر أو محطة طاقة</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/84867" target="_blank">📅 16:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84866">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoyMd6Q1mWy1DQ9UEA3YL-ml0uVkB4saTOFt6zVXqf6Y1lRbmj4kYUVGSK6UCaBbBp6o8ipv3gb8_f40fGdaWnUCrOAhgb-p0zC7Buz1TOHd6SQYYBOKhOLhhFwVElp2vIBx3vzcoRQLAJWYVNBlmnQq5YxlOcw83DxeCUVP1hse2sNeu_21uofCLItoYFkE-l2KcMMMS1dN1jh9XuUeH_KMPdRDBsgSUu_8o4vlx6e2BVMDfLu4fSyJEBAJpIXwlagTuZCq_I4Fy6YRpzUaWMmPRSHlF3xFX4vlZIXZK5vcJTYl_F52KF0mybDOyRsdXd1A-aURwd1IFauVV_barA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يوجه تهديداً
بشأن عمل عسكري محتمل ضد البنية التحتية الإيرانية.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84866" target="_blank">📅 16:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84865">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Ygn_1TxphU7l0niGqiW34POiD5r48ZWdnzZU47ZcOW3ngOywhndyc2zrCIDCZV9_hrDPg_KglHAXdRltDwAkeYn3yzKE1C9YDyolQvNstcO2A2tt6goky7syrjJ_Y4_Qe-LcXaZNw5Kw0MqZip41y5I_ZFmYj3Ss8EmGHA9IPOvUP_AsHiAjXoJTsxOgKMMzcMh5VZXxgNKvE-0J5y2AnAQb6T5Tb9K86QUCmLHcazTUzr1lPseJjF2b6J4wmYPQRdme9C3qDlq_8mzDzNpNED5W5gBJgxh1EG1XQLFQvNOa_GuwhaK5pBiI-ZnssGVotZN-njvbQj8myGGivvDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يتجه الى قاعدة دوفر الجوية لاستقبال قتلى الهجمات الايرانية</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84865" target="_blank">📅 16:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84864">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9234603b1.mp4?token=MM1KDfkqoafIqMefFgU1HF3WnG0JoGsTRGx2BYEQgl8g0ALoPeD281o7pUa8YKk-QGUWeaUtve1R5Fw0okB0Wqb47i6eoRezFi4kP6WzQ70Nxi7P0-H4dWx3suArmo3YnfRmTEEsBOdHaDlOn041LO-Gq4xiCawp8TMWH5h6LhbqAniVIcjx_NmgBqc5tzqAyOv1jBjPOseVsd9yZtJyA6StROZQ97Mn9fCV2m_xcVWvk94mSY2wJRzIEG4-EOBkF0JweYfbzeG3eakLhN-Q6NIVzDGKPEEVJzpo98zJpl-CyAmmMK7axMi3DyzWMfQiGIc30E_5W9GCeydJlw45og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9234603b1.mp4?token=MM1KDfkqoafIqMefFgU1HF3WnG0JoGsTRGx2BYEQgl8g0ALoPeD281o7pUa8YKk-QGUWeaUtve1R5Fw0okB0Wqb47i6eoRezFi4kP6WzQ70Nxi7P0-H4dWx3suArmo3YnfRmTEEsBOdHaDlOn041LO-Gq4xiCawp8TMWH5h6LhbqAniVIcjx_NmgBqc5tzqAyOv1jBjPOseVsd9yZtJyA6StROZQ97Mn9fCV2m_xcVWvk94mSY2wJRzIEG4-EOBkF0JweYfbzeG3eakLhN-Q6NIVzDGKPEEVJzpo98zJpl-CyAmmMK7axMi3DyzWMfQiGIc30E_5W9GCeydJlw45og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
تصاعد أعمدة الدخان بعد سقوط مباشر لصاروخ إيراني قرب إيلات</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84864" target="_blank">📅 16:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84863">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEcH8Oqef0SaKHNkjF2NtZ3_iYM3bd8AChIdSZ7X67APeOJo_d0b_KtOsRLeNRcepXta50axQ6Gh60oSrLEWT7a3cLYgpW0zEqG_8M_RTTPx5hEInpQp1NA88OQFYrA5zHY8plYKLdIyimRd9X1wg0ycnzAocZ7aH5Z-OcVDiVkRQcDGXXFa8G-cxsFIOSdQ96j_8t_QuaWpQtI4cSM_5FgiOLRadn_PZ9fP9LThw8cxAZHy854tH6n4lZLVySsiwY1_7kczMx2voc551pYqmjI3FZEqyKQlnNOYaTT9fHeNeGl7P7pkNEPneBsv7d3bWYMpXj62pydqc9LdySZXtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇮🇷
مواطنة كويتية تعاني من قيام طائر الببغاء بتقليد صوت صافرات الإنذار نتيجة كثرت الهجمات الإيرانية على الكويت
واسوهم بالتعليقات واتركوا تعليق جميل على الرابط ادناه " يا كويت لا تخافين "
https://x.com/albfatmah/status/2079838707947905163?s=46</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84863" target="_blank">📅 15:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84862">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txA24Q_jZKbiWj1aMej0pYHda_A7QXpCuNxATtpMjuVXikY4UEGSFpKU_8CAt4ZH-sEXSzjaB2WVv5i0Kh_1lsSnaZxCQPxmuZPpU9DGZEfROQ8nkQItd3s5R5Mo7RVf--fyUAXVVmXaAXBdMsMX57mo8fSgbBVQR_t5fKSTIxlEJTdpVXXWfjYQVnxffP_hzR0Mav2kueA_47zHBsWWZ3--Xv8o3JLWw_Du3Kbo3-Hs54eiXuso2dwXy2NNeuJIC8RgZeRhZQxwdnx7Bda8gnMgz2shwMuwWU0q2I05fDddGtHxmDtsi1nKSD8LK5lxDqPN85xZN8NOoAvjWmNCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشاط جوي مكثف لطيران البحرية الأمريكية في سماء الإمارات</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84862" target="_blank">📅 15:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84861">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7a4614820.mp4?token=cDF64zEBC5KwrCNLYAaD7x9h821E1JlPNY0BaDRaFFdYjYRnAHAoXbgVL2FjLNRX0TamBSFsMp58xlj7tGLghqPbPlNtrIVBB1lzz-IYfqKjDdsz0zxzP6nqp1hMVE5GlFFkCJgICvARtjgwQ2TBIAgZm23fKv-uqsBAH5Xs9x-An57vNuPAnNOhva1d9WUBaGshJnwent7IkU2iPwqgs5SDoarTrTyQlMmj74G7eOsegI0Uh4jMzPxi1OOLIv8hZgfJIz4n0ZRM5WqUtUf6u0tAR4BBAoQWRdBKXBuLGkyWudQ-idH2LN7Y8qKr_tVw0hBScKbjTVBnN0F6P3KNebmug6jTcc69g__Syd-8XImrLLC1lZGGe9yzTjWgk6ybsI2vMyqoj7-e9FZilEmXtuTqczIGpMMq7dYmCSk8mT4Q5KWLQgmM760LEzoHkerOZwy33ZoX6wuU7QLsO0M21H0jsYOiwwBsQsUy5D1AdabeP4mxvXEbbftVOnsPaQnGChvA_2KB7pYCPCPK1vJrZH8_lpYC7l-x82HAUqzZX_BP72h9RMjMN54Eo-GTIyi-CZ07m-QMKb6Jf4ZSu4CO_Pp2zdC6HxPEyp5CA1ppAH9jmktFtZuPExAEe91OQXJMIRtz5HKsdvaAoM3YcuOjLD3JID4oCLuVMLMhM5_M7ZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7a4614820.mp4?token=cDF64zEBC5KwrCNLYAaD7x9h821E1JlPNY0BaDRaFFdYjYRnAHAoXbgVL2FjLNRX0TamBSFsMp58xlj7tGLghqPbPlNtrIVBB1lzz-IYfqKjDdsz0zxzP6nqp1hMVE5GlFFkCJgICvARtjgwQ2TBIAgZm23fKv-uqsBAH5Xs9x-An57vNuPAnNOhva1d9WUBaGshJnwent7IkU2iPwqgs5SDoarTrTyQlMmj74G7eOsegI0Uh4jMzPxi1OOLIv8hZgfJIz4n0ZRM5WqUtUf6u0tAR4BBAoQWRdBKXBuLGkyWudQ-idH2LN7Y8qKr_tVw0hBScKbjTVBnN0F6P3KNebmug6jTcc69g__Syd-8XImrLLC1lZGGe9yzTjWgk6ybsI2vMyqoj7-e9FZilEmXtuTqczIGpMMq7dYmCSk8mT4Q5KWLQgmM760LEzoHkerOZwy33ZoX6wuU7QLsO0M21H0jsYOiwwBsQsUy5D1AdabeP4mxvXEbbftVOnsPaQnGChvA_2KB7pYCPCPK1vJrZH8_lpYC7l-x82HAUqzZX_BP72h9RMjMN54Eo-GTIyi-CZ07m-QMKb6Jf4ZSu4CO_Pp2zdC6HxPEyp5CA1ppAH9jmktFtZuPExAEe91OQXJMIRtz5HKsdvaAoM3YcuOjLD3JID4oCLuVMLMhM5_M7ZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المتحدث باسم القوات المسلحة الإيرانية العميد شكارجي: تم تدمير مركز بيانات ضخم للعدو في الإمارات في الحرب المفروضة الثالثة. هذا المركز أُنشئ في الإمارات على مدى 20 عامًا، بمساعدة واستثمارات الأوروبيين، والكيان الصهيوني، والولايات المتحدة، من أجل السيطرة على المنطقة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84861" target="_blank">📅 15:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84860">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
مصدر بالحرس الثوري لنايا
أوامر من من السلطات العليا بالحرس الثوري بتوسيع دائرة الصراع في غرب اسيا وان الضربات سوف تصل لمناطق غير متوقعة بالساعات القادمة ..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84860" target="_blank">📅 15:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84859">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/84859" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/84859" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84858">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpfBu8j8Mn4Tpelcqy929eromkSncO7mt1J_1qK7v1x2e-EOzpODtbPRs32asX7r22xBVm206bDAYNqIcNBtb4B_d9xHtnpSivP8yczNk9qZ6mhf-dT_teM-e76CPy7QCXbeS-5X_UoGe6Vd8_86GXBVD3v2T5OuBHJHEVp7M0IIvjbeJUE1AM7tp9UGQrLSEZWe7XhEqB-O1fpduIIzIGhYvts3NFKwYUJRZXqpsWLUbjGjFNVo-Y5FxjEy8WLGEEsFtC2j2xo2sAJPfIGdhdJh5BgoRyjTQ1_XnE2x5OjoAKyi5_j2gKfaMxWv-QytcE12M1cTqwpNcVRUrjNs-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84858" target="_blank">📅 15:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84857">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoTXu4rTaGXZOUxsoRY8_FgJmvGp4wJTrBuI1lKuDauJ7HJuMdy8UGqwiDDpjNLTtcH7XxNIuZ3OVIx1VSdWiVjtQ2KrUMcmYHNixv-tTQPLlI3q9-8tcDyeppsfe8jTa6gyUctSYzyxsH_RO2mVhgE9FJv-o6V90o8gW65O8mGUABIag0uky2MXR6AYZHTkjeYfTwBiixriCazE8-JdXIDCFFaH_uvHprQiVJcEJZ_FXXHgSaP3Q0uwIbWvdzx7jjF2vQ9oUchA3aVE7PUDZjbZgs8QmkdTTKYv1i_eTMxXtDz_H8Osn9_wrfmxV7yyluBDMtrKZJjYS59UgeX82Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84857" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84856">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84856" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84855">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84855" target="_blank">📅 15:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84854">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84854" target="_blank">📅 15:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">هجوم صاروخي يستهدف القاعدة الامريكية في الدمام</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84853" target="_blank">📅 15:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84852" target="_blank">📅 15:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84851" target="_blank">📅 15:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84850" target="_blank">📅 15:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تسمع في مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84849" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84848" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84847" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇱🇧
رئيس البرلمان اللبناني نبيه بري:
العبرة بعد لقاء ترامب - عون تثبيت وقف النار والانسحابات وهو ما لم يحصل حتى الآن. الانسحاب الذي نفذ من بلدة زوطر الغربية يوم الاثنين بالكاد يعدُّ انسحاباً فالبلدة لم تكن محتلة.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84846" target="_blank">📅 14:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JynHVBPVQGKowuZLkAvrVaKHHaBKdj4whr1xvTiFBqFI_XlD0pe7SJ6hX8IVnu61r5JlyW7AgcRq1hQVEtf1SmaPVI7r2UrLefcKh0KSAjL0EY0jY0VCGexfThpQ9KfIAnrFPsuSvHL9N0EJHEG_xoC6Il3HfCtc44HNN0C_Z1MhYfcUwPG1uFN7WT-ox_eXAiCqPvsPFKRX7Y7OxPAzMNMEzmVCfSkzl_Zz6uyDSkpXVqeVOPyOIM9wTJDGDUY3O6_u6qkntsvcG7NZGlt2r0OoA6QUHAHOE0MO41bdwn7RuyYNqdq517GqJMHmBs0GOU19OcynHJOLbJgjAHaHXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UB3dnxyMIVWTGd9H3U6JK4oE7PJ9KRbtyOJzFOFQUUjPQZC3s8ZBzfWsqVfQqfxL2sJ10ZSG8RrWSf8dOaIlgR_KbtSyF-lIf0pV-pz9SDvv8_eHKpkoj-Kls97gSnEmrr3LGhu9qDPgK1A6O6n_tjMr3uzccDg3uq68s6sGcrgnZMRmiu2Xt-U9LqaNPXr70IgW-e9lYwJ28C1Zkg38b73orQi8Gw-7Es8r6i15MG5tDdwYxaI3vLarizh7LEz_FApJ_l14ET6cvBhcOPmb4BHVWLB5YUexK9nCSpIc07ZlFX4h3uwcuftwuib9LQopatbfEz1e2CEXeccC8lShCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لقطات حصرية وخاصة   تظهر وضع الجنود الأمريكان في قاعدة موفق السلطي وهم يهربون إلى المخابئ نتيجة قصف الحرس الثوري   Thanks a lot 57th we get a lot of information by these videos</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84844" target="_blank">📅 14:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bc0c30806.mp4?token=PfV06jCY6S-x0wWMK1RiMtM_oRa62MZW0O_uLzPgiD7A7CIhCU-uQSYTeYm62lAWcwWMKRNBoPWaC3xQdEb_tqYsxWZjpRBgn8KWg8zTGRMTmYIiMG6_FBDcSWkFW4jMM94mQtThLzq4DSAVs0CKWYkG-gSwdCTQ80EedYWuLaHGZcDKoJW7d8KXB3DySdsaTlhRlv4aBwQtGWKjTGG2hoVsqzCjMhfZQdDUdjyMbpyYA4AH7k_dVsgDW4u02V8s0FQkxRpetn3RBlXDsE5hGjDsSuNX5Ab74wPRmamDpbXKahLdTlLBL8CjuOd6awZBeY5LSZ7bnQFFtAlfSxvd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bc0c30806.mp4?token=PfV06jCY6S-x0wWMK1RiMtM_oRa62MZW0O_uLzPgiD7A7CIhCU-uQSYTeYm62lAWcwWMKRNBoPWaC3xQdEb_tqYsxWZjpRBgn8KWg8zTGRMTmYIiMG6_FBDcSWkFW4jMM94mQtThLzq4DSAVs0CKWYkG-gSwdCTQ80EedYWuLaHGZcDKoJW7d8KXB3DySdsaTlhRlv4aBwQtGWKjTGG2hoVsqzCjMhfZQdDUdjyMbpyYA4AH7k_dVsgDW4u02V8s0FQkxRpetn3RBlXDsE5hGjDsSuNX5Ab74wPRmamDpbXKahLdTlLBL8CjuOd6awZBeY5LSZ7bnQFFtAlfSxvd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇸🇾
محاولات فاشلة للتصدي لطائرة مسيرة ايرانية في سوريا خلال اتجاهها لاحدى القواعد الامريكية في المنطقة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84843" target="_blank">📅 14:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">على الولايات المتحدة الأمريكية ان تستعد جيدا للقادم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84842" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO9SU0FQiGBPpp0vTGV4px1CTme6ousZMeq8U5UycCZzNtDCJ0cmTv-O82agpfmtnBTAh2ofoBlMpDgFikZz06Z4w4D4PNMo995u4SUCbRPmB4ZF0_DBCnuPga7cy3JoRfSfN4Yi-reUAdzJ554Bbng0fnOzA63lSWayIa-XO42uLykewkxjZskWnmcgePaiAcm-rrDe0bqEPruGoau1GVPq2_Qf5RGOzg4ZL78H9LY8F6wNyb231_RyWSKg447EqxGRhIgKfM4H4Czqcl8XKCL5WAalOM0qOv4FmyXucGlULNp-8ClwxvCjmZJ4OzOehXL5xLL7oKoeqj6EtdoyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84841" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/84840" target="_blank">📅 14:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
حرس الثورة الاسلامية:  بالتوكل على الله تعالى، قام مقاتلو القوة الجوفضائية الشجعان في الحرس، ردًا على اعتداءات العدو، في الموجة الـ25 من عملية نصر 2، تحت الشعار المبارك "يا حسن بن علي (ع)" وإهداءً إلى شهداء مدرسة شجرة طيبة في ميناب، بسحق القواعد الأمريكية…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84839" target="_blank">📅 14:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2317f947b0.mp4?token=c9id6riu0I1CeRVA7iQSLpREOm9-E_XeTzhi-k_u-RlPoNXqFa3-CULgWEHf4a3Ty14_u20Jj62rtYOahSfqguA_HyDlcE_h5vWBnpo6xqOD8Oms-H262V_XLoqRhMow3cFUv9WKcvoi0Ae6ezxPLkuYHPyur9FBS9j3F9R0lAxFpVzoGK4QmRGZZuAgLAzM8KHBS-6w3mrr214Yk_Fz0P4TEbc6g6phdcU3oJNEGHixpVvyNMIDDQW_Hpip-oQ9W1yUMXVsAxxfQjnFHZSDqLAtYsWq_bjG_GO6etsofoC_YYdtLTiWvUNJ95phWA6W7CXoPC4jJ9DyG_Y8Lpu0WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2317f947b0.mp4?token=c9id6riu0I1CeRVA7iQSLpREOm9-E_XeTzhi-k_u-RlPoNXqFa3-CULgWEHf4a3Ty14_u20Jj62rtYOahSfqguA_HyDlcE_h5vWBnpo6xqOD8Oms-H262V_XLoqRhMow3cFUv9WKcvoi0Ae6ezxPLkuYHPyur9FBS9j3F9R0lAxFpVzoGK4QmRGZZuAgLAzM8KHBS-6w3mrr214Yk_Fz0P4TEbc6g6phdcU3oJNEGHixpVvyNMIDDQW_Hpip-oQ9W1yUMXVsAxxfQjnFHZSDqLAtYsWq_bjG_GO6etsofoC_YYdtLTiWvUNJ95phWA6W7CXoPC4jJ9DyG_Y8Lpu0WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
شما که میگفتید ایران دیگه سلاح نداره .. چی شد؟
@Naya_Press</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/84838" target="_blank">📅 14:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84837">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
حرس الثورة الاسلامية:
بالتوكل على الله تعالى، قام مقاتلو القوة الجوفضائية الشجعان في الحرس، ردًا على اعتداءات العدو، في الموجة الـ25 من عملية نصر 2، تحت الشعار المبارك "يا حسن بن علي (ع)" وإهداءً إلى شهداء مدرسة شجرة طيبة في ميناب، بسحق القواعد الأمريكية في الأردن مرة أخرى.
في المرحلة الأولى من الرد، وفي الهجوم الصاروخي والمسيّر على قاعدتي الملك فيصل والأمير حسن، تم استهداف حظيرة تجهيز طائرات F-15، كما أنه في الهجوم على حظيرة تجهيز الطائرات المسيّرة، تم تدمير ثماني طائرات مسيّرة من طراز MQ-9 جديدة تمامًا، كما أُلحقت أضرار جسيمة بطائرتين منها كانتا في الساحة.
وفي الهجوم التالي على حظيرة تخزين المروحيات، أُلحقت أضرار كبيرة بمروحيتين أمريكيتين ثقيلتين.
وفي الهجوم على مركز إيواء قوات المعتدين، قُتل وأُصيب عدد منهم.
تستمر عملية معاقبة المعتدي، لأنه إذا لم تتم معاقبة المعتدي ولم يدفع تكلفة باهظة بسبب خرق العهود وانتهاك الاتفاقات، فسيتصور أنه يستطيع، متى شاء، استئناف الحرب، ومتى ما تعرّض للضغط إنهاءها، وتكرار دورة الحرب والمفاوضات ثم الحرب مرة أخرى، وإبقاء ظل الحرب دائمًا فوق رؤوسنا.
الطريق الوحيد لإعادة إحياء الردع وإرساء الأمن المستدام هو تنفيذ أمر القرآن الذي يقول: "وقاتلوهم حتى لا تكون فتنة".
لإبعاد ظل الحرب بشكل دائم عن البلاد، لا يوجد طريق سوى الصمود وفرض تكلفة باهظة على المعتدي. وإذا لم تكن هذه الردود كافية واستمرت الاعتداءات، فإننا نستعد لعملية نادمة ستؤدي إلى إعلان الحداد العام في أمريكا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84837" target="_blank">📅 14:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84836">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📰
وكالة رويترز: ‏سفينة نقل سيارات تغير مسارها في خليج عدن وتبحر بعيدًا بعد أن أشارت سابقًا إلى ميناء جدة السعودي كوجهة لها.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84836" target="_blank">📅 14:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📰
وكالة رويترز:
‏سفينة نقل سيارات تغير مسارها في خليج عدن وتبحر بعيدًا بعد أن أشارت سابقًا إلى ميناء جدة السعودي كوجهة لها.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84835" target="_blank">📅 14:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وكالة سلامة الطيران التابعة للاتحاد الأوروبي: نوصي بعدم الطيران في المجال الجوي الأردني حتى 31 أغسطس 2026.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/84834" target="_blank">📅 14:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">لقطات حصرية وخاصة
تظهر وضع الجنود الأمريكان في قاعدة موفق السلطي وهم يهربون إلى المخابئ نتيجة قصف الحرس الثوري
Thanks a lot 57th we get a lot of information by these videos</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84833" target="_blank">📅 14:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84832" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/84831" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUz0HKCpD5lu3JgtxTCXMtwkDLEXFthflcIk2kbjG7Gqli1SEcIbBncKBnz8X7nQtd6rkODSSDWgHsV9YQKhloNjyTBqJJcCSFyd5aKxfYbTns_Ja1p-huxSnCXFQ54JRWw2Ak4BB858QkC2opePtVJ1uvo1PSzVKv2hWNeqr60yI710RC0dVxmCxtUlKbsXy2_dX0dwDQRT1Zd_Y27psWx71Ykq6cipFjLuvbRIJkCe4XfWJqV0kiRS601oGEHysA7Y3hQ3e5uOs3G39CP6rEvx8eLD2whBmob4ObOda78nMDkgbdbzpqn4LwYzQ69PZE04Xlpcd2tvOGDLU9Hsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
غيث التميمي عتل زنيم منحرف ضال مضل وعميل لاعداء الله ورسوله واهل بيته وللوطن وقد باع دينه بدنياه طلبا للشهرة والمال والشهوة فلا ينبغي التفاعل مع هذا الزنديق وان استضافته في القنوات العراقية يجب ان تكون ممنوعة منعا باتا وعلى عشيرته المحترمة التبرؤ منه حفاظا على سمعة العشيرة ولو كنت مجتهدا لقلت غير ذلك</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84830" target="_blank">📅 13:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تعيين الفريق الركن (محمد قاسم الفهد) قائداً للشرطة الاتحادية العراقية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84829" target="_blank">📅 13:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
🇮🇷
الناطق باسم الحكومة العراقية:
رئيس الوزراء سيجري زيارة رسمية غدا الخميس إلى إيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84828" target="_blank">📅 13:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇶
تعيين (زيد حوشي) رئيس لجهاز مكافحة الارهاب العراقي.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/84827" target="_blank">📅 13:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">روبيو: تهديد الحوثيين بفرض حصار بحري مشكلة وإيران هي التي تثير المشاكل.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84826" target="_blank">📅 13:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iy-pkFT05a_kDx7ZvjcWH5XiGu4uAAHD9XbLWDi4qu72dGPYlsYpoGfop5u8A9pTRqpzaycEdsWjftmIk6pEPTG9RPXjArKKL4ZuU4TGTDY3_ZGcxeJUVODqfwgw2_KWRZ9NgfW2FkI3O-vGmpTu5Seog7G3iV8Ib1wViikgC-QvDK5riROkMJn_AKhDJ5cxVEAu0vWJsXfuNCeQaHtq1nwGvmjD7YFqDosQgskVEH-7u4cTdGPjjz3ZULfh9gcZZyM7HTVlZn-VEV_v40cGLjaCnzdUSKrB7EDTCjhLfdSOg5c69zdPE_Rcmhf6NJblOf7KkAqYKlXwYY6v5hQv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تعيين (زيد حوشي) رئيس لجهاز مكافحة الارهاب العراقي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84825" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏روبيو: إيران أرسلت طائرات إلى اليمن تحمل معدات وأسلحة.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84824" target="_blank">📅 13:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
‏روبيو، وزير الخارجية الامريكي: الصين لم تفعل شيئا يغير مسار الحرب مع إيران.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84823" target="_blank">📅 13:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇺🇸
‏
روبيو، وزير الخارجية الامريكي:
الصين لم تفعل شيئا يغير مسار الحرب مع إيران.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84822" target="_blank">📅 13:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سماع دوي انفجارات في مدينة سيريك</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84821" target="_blank">📅 12:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇷🇺
‏
لافروف، رئيس الخارجية الروسي:
تم الاتفاق على لقاء مع روبيو غداً</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84820" target="_blank">📅 12:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
🇮🇶
الإعلان الرسمي لنتائج امتحانات الصف السادس الاعدادي بفرعيه العلمي والادبي بعد قليل على قناتنا  https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84819" target="_blank">📅 12:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#ترفيهي
🇯🇴
ال‏إعلام الأردني: دوي الانفجارات في العقبة نتيجة اعتراضات صاروخية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84818" target="_blank">📅 12:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84817">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRnvLYlIZBgDvSDCDy2fKAs_YoGKeVlOvHFv525uCJFFM9mMEyTClH0_re7yFJEivLtZ2Cx-Kqk9cm-CvnaVxj0VatpGnUPzqMYeDE7ltBUe1twumfcy7A-QWy7f3MGsM5zFhrsoNtFPjA-iY0Y05YTDe2CZvipjMffkaXDRpm6P6eqOC-YAUxMHpqO54l_gZj2gBr-DaF4TwQ71rtKD1n4tc9lxlWH_uYCETxxGCg47G7oBeBVMxeTTCpifh2mqFwRfoWC5e2dNHBEo2-yoXQ0pZg6vzA_lRdYtEPKGD9iAqOVmFfnOUXRuxCGmH5cZtQrWDI9lOttZunxPPWUT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
النفط يستمر بالتحليق إثر الهجمات الإيرانية على القواعد الأمريكية في المنطقة حيث وصل سعر برميل النفط الواحد إلى مايقارب 95 دولار.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84817" target="_blank">📅 11:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇱
هيئة البث الصهيونية: إسرائيل لم تشارك في عملية اعتراض الصواريخ الإيرانية المتجهة نحو العقبة</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84816" target="_blank">📅 11:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇱
انفجارات تهز إيلات</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84815" target="_blank">📅 11:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#ترفيهي
🇯🇴
ال‏إعلام الأردني: دوي الانفجارات في العقبة نتيجة اعتراضات صاروخية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84814" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
رئيس مجلس الوزراء العراقي:
نصحت ترامب بعدم توجيه ضربة عسكرية لإيران
لا خيار سوى تسليم السلاح
العراق يجب أن يكون نقطة التقاء لا ساحة عداء بين واشنطن وطهران
نرفض تحول العراق إلى دولة فاشلة وحكومتنا ماضية بمكافحة الفساد
نبحث شراكة استثمارية عراقية أمريكية تمتد 30 عاماً بدلاً من الوجود العسكري
الحرب الأخيرة وإغلاق هرمز كبّدا الاقتصاد العراقي خسائر كبيرة والعراق فرصة استثمارية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84812" target="_blank">📅 11:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇯🇴
🇮🇱
أعمدة الدخان تتصاعد من منطقة حدودية بين الأردن وإيلات.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84811" target="_blank">📅 11:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebb7bf717.mp4?token=PpGeGztiPYjsZuJ9tYQkQ_I-3NdMvJJ9SYupttiDDVHg7CGGJyECuF6G-Nv6s0Kgcje7DJ60AA6uHaZoJOuYK1QC-fLVXNugnvooa4WZ8ZzfyPI5HIy0-TC0KVoFvdD53S73IL8G3vkfXv1PUuHwFOmSUchPV-aTTfFqnq9_oAbmw2W7b1EsK8aRDE-1dzISU-qv1D3Qi4sN_tLduOnZB7TI3CXpwead3nS_VIBcCsvjkvi1BqA5vtlo2xW-8N71uC0A23Jlx-gXCAirnUJmDF-jQlVAaux_d3WG7iNRQZgV84k0t2Dy9xOuvl6GwCVbEY9cM76yTsqSmm9fmRTYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebb7bf717.mp4?token=PpGeGztiPYjsZuJ9tYQkQ_I-3NdMvJJ9SYupttiDDVHg7CGGJyECuF6G-Nv6s0Kgcje7DJ60AA6uHaZoJOuYK1QC-fLVXNugnvooa4WZ8ZzfyPI5HIy0-TC0KVoFvdD53S73IL8G3vkfXv1PUuHwFOmSUchPV-aTTfFqnq9_oAbmw2W7b1EsK8aRDE-1dzISU-qv1D3Qi4sN_tLduOnZB7TI3CXpwead3nS_VIBcCsvjkvi1BqA5vtlo2xW-8N71uC0A23Jlx-gXCAirnUJmDF-jQlVAaux_d3WG7iNRQZgV84k0t2Dy9xOuvl6GwCVbEY9cM76yTsqSmm9fmRTYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
انفجارات تهز إيلات</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84810" target="_blank">📅 11:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgInoDmANPLbE1iDttU_jNsDC8gSoWqiVjia8cZA-_RPq47iv3QPIdpuyN9WfEnVPpeN7C9hzOg5CBeopTBBpzKra-2_enpOEAYeIbfLbrrdUDkJ2imQalvAwcy_K1fM82m9uSFyxrhiFVYHxO5fLprxZUZAyK3JOyKQx7ukAA793rFJ-rfMoRhceR-3cSlmQAIvN0_wHLENy439h55jSIt4QuQpWPYDr42vU7FvQxOkMDHxvVdjbjeLStA0alE6LeNKMR4NZWju6HsmQGhD1HLqu85eL_LOKevpIQjvx6HaaEsMXDWaYaHopdOLFg31U4NYrB1rKiqK6jUU2IznfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RL-B03JM2NfkEmWfWA1iqP3GlH7AFTs_OIJRzDmwAqtoOG9GvF3E_TDd9ykTO2K4-rWlN-aCVbQVc3t-bwwjdgt5FU8FDRpSG1g1ePH4GAOIfLljSbauO3ddcFSsGKgvZ_Ol3cPI7xSIIDT9xzdSw2lB3ZpnyTdJo1zeP1t5OsmA4zmwQSpnH0lDS_gymykOXPBsVKs_GfqhuRSFIODZTQ1eaNUdGJOuWsKkSJD3AETrYVmgpjBrOcO8S1Hxf7ytx5_a8je3s1c47QFMPfxzz5lYYY08y13cQe3GwJq2s3Zdm8keDCW98dmw7Q8rFAj6VIDivebB0AU5uM_uxCfXZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
تصاعد أعمدة الدخان بعد سقوط مباشر لصاروخ إيراني قرب إيلات</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/84808" target="_blank">📅 11:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0998be2c31.mp4?token=g-K1bi5GE6nRf0M6USkceb9pAc1l3qpJsoSBuCLJVrtLU0s4UHpLDVcL3ZP_jWJPKvxWN4V4IGQl0GfZJf9tbGaJjnSwVPQKr2sERtla8lGIsPxue0ZmUlK5oyiDE81NQoPEMaz_8b3qvKFALutvrJCSN6hiDR-0tHtlFPMP8FJCxJMRMU_yeednS8dV_xsAI3Lb3aq9tUDujSz47F0W6nYTiDtFTBnu_ySLpF3NuzcgJhY15SVfWLcR-VBYJb_ugR3qnn9kZJNq5P1HFlrwksb_eDvK5qkx5d19a8HjMmlXKbSmz8PyxwaNobq2WO9DnM7EnysHJwiksWxgugYPdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0998be2c31.mp4?token=g-K1bi5GE6nRf0M6USkceb9pAc1l3qpJsoSBuCLJVrtLU0s4UHpLDVcL3ZP_jWJPKvxWN4V4IGQl0GfZJf9tbGaJjnSwVPQKr2sERtla8lGIsPxue0ZmUlK5oyiDE81NQoPEMaz_8b3qvKFALutvrJCSN6hiDR-0tHtlFPMP8FJCxJMRMU_yeednS8dV_xsAI3Lb3aq9tUDujSz47F0W6nYTiDtFTBnu_ySLpF3NuzcgJhY15SVfWLcR-VBYJb_ugR3qnn9kZJNq5P1HFlrwksb_eDvK5qkx5d19a8HjMmlXKbSmz8PyxwaNobq2WO9DnM7EnysHJwiksWxgugYPdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
انفجارات تهز إيلات</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84807" target="_blank">📅 11:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q98zJmg1C0ZUvgVnCGWGEX7aPfQ6ByXlD0dBY_VRKvOIb1xwBDwJwIo635zrWQon9gXI3fRFerLz8sCTjdZ35G_D4yRxLGnLCUE7m6icZ4_T3cdBiiKSG5qSkK9Pm8_vz4g-872wGVTpGuPH3Wq-PR1V4FqFIQdjLJE7bt5nkdvTrDZbXWVj7kFHSfTlBI4Ib9F_hbnvGC9-8_4mrsDbRkpmKpYe_Cmw8k7vgP83HNbi5Hn4T-9bDaZ7VX-dld8Ox0uQUcy499E2w7yAQZE0bq8S-fimSL6c-YGgKCAp8IC_ymZT9d16WAia3QUWHVVG5DWeu9F6Mim5_sA7Kh7tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
إصابة مباشرة قرب إيلات</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/84806" target="_blank">📅 11:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇱
إصابة مباشرة قرب إيلات</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/84805" target="_blank">📅 11:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84804" target="_blank">📅 11:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84803">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇯🇴
انفجارات تهز العقبة الأردنية</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84803" target="_blank">📅 11:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84802">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84802" target="_blank">📅 11:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84801">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbKZshzgISYQnY4mJ_v5IvxxklD05WbXRIqaLpuQcWLdLkKmxhUOfBa6i-nHIlg4x_C2r1_lToWlz0DPaB5vSUU1JbZ_dS07aX1Uu979gnk3B0kgYgs5C06Sm1sEddAkqJ470xdTFHwiAzG9oqExU6INWRbRUf_CgjKrqtCLCcmehZDAUUnNyMuc2Tg1wFlYj57iVqPMtFpYOVB3DbBtHe-OJz98h7mejCm4jMwnTJkS5Il1iJrf0IeVDsS1yYIOMJD0hSiciqd51b_fS-xiBuYpMEBNbN9hQbbegwUJNZvhraVGf75-P_J_k1tnvMpwBQubLl30KXME4YF7UnCLKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الموجة الصاروخية التي انطلقت من إيران تتجه نحو القواعد الأمريكية في غرب آسيا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84801" target="_blank">📅 11:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84800">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvpyyYFrmVh-hApGmvJ06oUm9wo9O6FgE4XlE6MwTbET3J1F-WPQ6VGtX0QDsLM5iOV7qMVUdahsNJaaoo05RPw_ZHEO3N-5c-IjLM_fC9eVJdRg6I5KwsiT1a1JT1vZqQLr99rAos_McbNTGCqh4KbH9QnzBUUezrISrprWN5A8tJquJzdeBpy0FrW9-ly2V0c9depCmhE5u05pYBn90eTtvA3tAejNvh-vn2owDLDXtm_-D2mzwTeJfsoez4JDr8CZ5T7ouRX5EkRQipJWDwhz3o6t0td0t41cVkxb-0zxJNCNau3oCD6pQ5UJwfElZmGpX12ngl0e-bqO2oJkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الموجة الصاروخية التي انطلقت من إيران تتجه نحو القواعد الأمريكية في غرب آسيا</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/84800" target="_blank">📅 11:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84799">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
قيادي في حزب الحرية الإيراني المعارض: 3 مسيرات  استهدفت موقعنا بوادي آلانة في أربيل فجر اليوم</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84799" target="_blank">📅 11:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84798">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8462b1b2e0.mp4?token=XEPFb64OXbrkKxwqreQb4kedyTvQOuwFgWBk3v7UxaYi89dEWQ5YxRdwkE5RtO46lYm9vA-H0s5JrU2sL5utZrj_21xViZYWUmHuD2jYYMMTae9GHP80F4kWfVgaeEKLGFlK5jF42wyV-s7TUO-w_7DOB-Z9DEgQKyJ79UHPkbJjEYt4OZpcb7s8y5GYW-Gt3BA55VsJd_MOjCIgRevUYV9WkV4zwSlD5jSWF8NMGk9tCeYWSWHFyvFS14ojzSH016YYOwBl8gUpBTHZRzc4OixXDRRVxeey843JzMx158JLzALMYYaWwTDENoU0EakqD_HHDpb_bBt--PlVvvXM7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8462b1b2e0.mp4?token=XEPFb64OXbrkKxwqreQb4kedyTvQOuwFgWBk3v7UxaYi89dEWQ5YxRdwkE5RtO46lYm9vA-H0s5JrU2sL5utZrj_21xViZYWUmHuD2jYYMMTae9GHP80F4kWfVgaeEKLGFlK5jF42wyV-s7TUO-w_7DOB-Z9DEgQKyJ79UHPkbJjEYt4OZpcb7s8y5GYW-Gt3BA55VsJd_MOjCIgRevUYV9WkV4zwSlD5jSWF8NMGk9tCeYWSWHFyvFS14ojzSH016YYOwBl8gUpBTHZRzc4OixXDRRVxeey843JzMx158JLzALMYYaWwTDENoU0EakqD_HHDpb_bBt--PlVvvXM7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اشتداد حدة الخلافات بين ميليشيا قسد وعصابات الجولاني لتنتهي بهدم بيوت جميع من ينتمي لحكومة الجولاني وعصاباته من قبل ميليشيا قسد في مدينة الحسكة السورية.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/84798" target="_blank">📅 10:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84797">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d5e7958f.mp4?token=KE95eJUv3w8lI2J2WgAKnWVpuIGecDIIWP4PVo0bNfu6H8VHiypcESQhesa7yhS4ijJn5MsaTOfc8g7z57ZJhGdT9byKoX34SJRnHqPWhokFIKpIp1v2adAJPzay4KtjHUDSNHa1FmufGjh_UgAkfQEvve3KcBEZ9dMlii3zlAfqgWDouDefASX5a08z5oC7DRVLH3uLHsMyrI7US6-AhZS7b1UquwOc6EMzma7RMb2cdkZwL8hReiMn8HQoHsY0cTu07hPpkJBph4y1S4WBgjPYCSoXaKg3-M1tXxB8fmzLNtUUkWf8k-_Wz-DWENXivNBMkaGpyl12jIhNI0PImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d5e7958f.mp4?token=KE95eJUv3w8lI2J2WgAKnWVpuIGecDIIWP4PVo0bNfu6H8VHiypcESQhesa7yhS4ijJn5MsaTOfc8g7z57ZJhGdT9byKoX34SJRnHqPWhokFIKpIp1v2adAJPzay4KtjHUDSNHa1FmufGjh_UgAkfQEvve3KcBEZ9dMlii3zlAfqgWDouDefASX5a08z5oC7DRVLH3uLHsMyrI7US6-AhZS7b1UquwOc6EMzma7RMb2cdkZwL8hReiMn8HQoHsY0cTu07hPpkJBph4y1S4WBgjPYCSoXaKg3-M1tXxB8fmzLNtUUkWf8k-_Wz-DWENXivNBMkaGpyl12jIhNI0PImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هجوم بالمسيرات يستهدف مواقع حزب الحرية الإرهابي في محافظة السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84797" target="_blank">📅 10:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84796">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
🇮🇶
الإعلان الرسمي لنتائج امتحانات الصف السادس الاعدادي بفرعيه العلمي والادبي بعد قليل على قناتنا  https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84796" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84795">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔻
🇮🇶
الإعلان الرسمي لنتائج امتحانات الصف السادس الاعدادي بفرعيه العلمي والادبي بعد قليل على قناتنا
https://t.me/nayaforiraq2</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84795" target="_blank">📅 10:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/84794" target="_blank">📅 10:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84792">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
انفجارات تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84792" target="_blank">📅 10:15 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
