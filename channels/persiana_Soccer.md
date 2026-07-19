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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 520K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrhJ5-y2OvPAdtWM8s16q3qPm2_291WqGmebs82no7WaHBXyPNt9qIgXVuvQq9p0XzeEfIYVChIE94Wmzl9t7qaqX3fq8iAQf2GiyVtg8g7ZdhbAAKo1J89p28CowDh7l-4ziNeJLhlZmmoAT-u8I8HU2Ber4-Pev4QnsB6Ar88MvTlIkVSczUepoKI44b1xaIiKV3JGB_aCbqejIAVf0dQCyCGH5KAILqY-x1Vs4W_cHkhTrPYTImQxZ_tSnZRz2a0y63RzKCbALtBaq5VHTpkBtG9dlR6XCSRCFosshIhIZBBu6h-qRr67_-5UTe9oig6kxtamwLzqtmAJ5MSQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10 · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrBnz7Pbv3eKw0u7chpHY8yPzmsKvVMbwS2ecA4kFTki2JnNAdddSs_vvpC1Yf6JNmRbFDDpwDJLOF2o_VIXdJh_sXG5uly3iOjFb1OYN9d7KHA3XoPmPl58K930N_-UNHHwU-sJBmQkFFFU8zCQ-SReyusaxC18sqQQC4h5-6gqVvmPaYpueygmlTeBxsvMfPSSVFbvp78PPGTbSQFvesrsxfBSCsFcn89pjjNgZlyrTJNecLUapgaaeIWnwGrfdAFdTxm4CbYEt8H0Vl6oknNuAv_UVKZsweZ7WmHV_udUmaOYBS3zRv0te4NH5OHiiOUSVhZuKlBwyqpng95nWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuHMt4U9y2RKoxbC05HfRrf0_bIBgtL4mEybkSnW7x2jZR5k6NqlUhN9FyH1_qI2K_O_9Dpeey5SDG7Vn4PpdJUdH0Qku41RZFZ47V5nUNRl3Zqk96bzWRXGYU77mSO2rN1ZC9yK2fmpo-hbPaltrepgRy4_2PyDcr-B1Me6xkb59zA6qAkBlJZzk5JINwsAdzRJ1Gg49bc1n2gL2JG4NXH_O5GGFjjqi6OPOsLl0H-RNNW2YBw9xzgCBfleBzftmF4-kiHCpqzyPJ2uVeid7x49wAtom9tlOihEB4Ca7JMiuERahNNPN9LbeXV9YjQ4pwA_QcagPGnYsr7jTl3XFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=c1g49SJsgipNbHKZUJAfIh2AxZVbwhiAZPrppyuZ9qjtJQrWHPIULc6xPoDMooPJJAMPOeHEabL6m-ceEV8H1mDqHdrWzGS0g84RwawHjLJzuuHHF_78ertufH_UAHLxBjsVy97-UpqUPHaDfMGyKX9Q5CjiuCDwvWFgb92r6Pa2wrmMKLWT6RZTDPzB3IpwWAqZRPOBpI20wbsdHzsXjHaXNJ9bLuouMr5tVTJOFXeAHYnLScePNgHKHARpA3e_-j-9tWsxXTt1GgB0YXnXdIPjPRYWMIZSZi9a2JtvjjjoAoOW-HvR5gPLG6GIr2D322-DYl0wnuOfbufPlmovQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=c1g49SJsgipNbHKZUJAfIh2AxZVbwhiAZPrppyuZ9qjtJQrWHPIULc6xPoDMooPJJAMPOeHEabL6m-ceEV8H1mDqHdrWzGS0g84RwawHjLJzuuHHF_78ertufH_UAHLxBjsVy97-UpqUPHaDfMGyKX9Q5CjiuCDwvWFgb92r6Pa2wrmMKLWT6RZTDPzB3IpwWAqZRPOBpI20wbsdHzsXjHaXNJ9bLuouMr5tVTJOFXeAHYnLScePNgHKHARpA3e_-j-9tWsxXTt1GgB0YXnXdIPjPRYWMIZSZi9a2JtvjjjoAoOW-HvR5gPLG6GIr2D322-DYl0wnuOfbufPlmovQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlrHjr9DTZ8KlkRuk6JU3-Njfua6UQvDJHZ8a0zP4cbNZkomR6_0F3lkvoz2YGLYuYySoiPyCzhwXtYnpPIXBZkTLhErovFGGMmvkgo_usEnyV3btTrxzFcE6VUxk0N9-7t_YVReqUwXmgeyMBdKdySRvI8SO5l2a36g2IrJ-g5a8ypN78M23kCyVcD2bh1mvgy3rG2y3q3Cy4Z2VyorUOYEoa6mRQGMZArlHi2IxCFeNg6vZj-IW6e8zDkEQbALPCwp-z7G7k-Z_ClL7_IRk31cH-K_RXaLma3nvvwqbR8pk9-TxL_zRVItDU0OxvUrROld1whN-p-CP-fqwcfNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxegBBMuFxmnc4yaHLJgbFi2Az4EuLpZlQLgt3U7yCWtNZpde6sQOMozeVl02VlYuvSSdqDOZne9xwjeEeZaajBj58sMsMJfrBE2fI8LE9i1J22s1KaiTY9sK1z49Eu64ZTyBoT5pIzTwrpnR_8RXRwFGPX8YqPjWRFZf_AeH2FybeJ_LD92ERzG4PgEHbNk0FUxbJ5dZ8LSfMnOjB_AGWF6Vuw1eXDp4cL7_arfvP9d0Y2FChG-O3Is8wU_OPfitXZy3-DayMRM316htlpbPMkWtNdcgETuKBCW2ue8tSvqXYg1dwqVi4NkDlYjT_iE5ya_pEkvoyHGKKBDSS_oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qaqd0ggb5bnqYE6HEVE5oWfsAtF-C7oD49gTvHt_lmxvDTSmdid39VNH1eUef4JRNqbVZzyAyrPDXDZ-t6oMrP3D3NfKqqN_zMJN7XCl-UhVNGGfyo6m_8vSZKBfDldAcihlxo1YYaAmkdVjw2swrT6og6gcDBIOSgSpGeYKahoD11BoUmPPUt7co3DBqJNxQ570JYLqiSGIFLyW0i3WJhaxGSjMiWOeNwAzgq6PBOs98uGBHLnnAPZH-jPVwGNtPpy-3wJtk0vE7SPkqenw4XtTgAwR0Ximwl4P3o8n4rKQkZZ1-riIs948Sj7PvlHeBZjm-Npnugic2xTQIFdLmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fqp78ikRzeorITIwnCNmkSzAy2tv1mI7lV-FkfTpBwTlN7PEutStUv-eDWF9r_U5DYIWLvYFE8KxH8igtvSQnsvnFhcZjZyFIfvnGkz5Y1jfiXb0920jxsyeio8h_vrUKgVXjeYXlgfvC0pXoVk4MMcIlaAjiXl9LaKrhkpbji6z8qxrTsa1Xr7rmEBW241c7OwFgwhyRM2leIBJT8N4n2DzEQ0i2MOgRWkQMzqhSJ7eupDdNFxBb_J0FH4CyVE-b4_8KDd8T0rjL6681rpbzXsFFc1TPD241fsfzsdQlWsuozakXX1_PAZQwtijY9etYY95ShwulPsix7XBvLNrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0hKJ33PYq6JW0iHjPCb9qy-Y0BRjF-6Pv9hinZYhX2Gw9G08iqqHBYGNJRsdhvSHsT7yShfxW8aO8GDyQAVc0Ts36ZYqL5pzICeucB1Jllg5CG4-bEebW-tTPes20GF98htj2jgk7biVknz2C3QjrQBfwuTRv-72UYUiG2Oj7NDmhFhGWMiGVSvDZ1tZk9uTH35Y6J8M_ue382e89JmTD9AxIjYH_4s2xBWhUdeSwsBXVias_W59Z0pYJwLv0fEXdyuNIgF00bpCJOPCwf9FqEdaaTNQSxRQWrdZ59Oq3eMRwy6JMSI5Ff1vjxe7Twf1r3VnaSevjmxaUMIfVCxcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeA0dQRinmbwkE1nH2dhB28ITr_FS9KCfuxjXFtMr4UDJkRIhQobCMnfHcYqW_8N3h754rCZmXtDqALhp6lOLnuckvpzhGQh3OfmEwL12JsnA1Woh5WbLLzE_ekL7wQhixBa4Ks6mQshkdLwEE5wq9OIQYOv2HrLLl9wr9QysqsvAi7PI4wlghIrB6rTw59jloqrTIApw6cJ_1raJZKeijH9g2-1qEFCdNRCLVxPj5YBA7FJDkQjp7HegOazyrRa38RaE2LmTDGuhHAilnfpbhYKkay0bTgXWj6TIhfM6ax4bwq_Wmqc7BUnH0EDJz-BLfh273bE9W-iYXfnJ-BJPbYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=Yz1ctfjtYNexzaBNGxog0-zCdEzGocLnbi08JNqzztA_PSlYyjPdEPyHYMfuUUOYEZ6IfuAI35BvF3gOZSHisoVhyn-XK1lbGNrY9CyimSIQFZ-Fi9Jgib0ux_4c-HBLIJarU7eGEuYrk6O7tp0nAImoxGPln1Ij_9gsTIDX68at1XNyTG281SfGfn4F5YHHRevB2XYF8WUTO-dVm5h9qwPF8Or2KZ7ityDEF-JgKEyXYC1ZXsRuxztWttfShrN_PkE_uIa6KwX3IHYFyc0OCTN9OGjkjCk3uWhTunGEqygqQ0CNFCBrjET2uSOPWh4PU8iBt2r9zLeuZKyv-RHKeA0dQRinmbwkE1nH2dhB28ITr_FS9KCfuxjXFtMr4UDJkRIhQobCMnfHcYqW_8N3h754rCZmXtDqALhp6lOLnuckvpzhGQh3OfmEwL12JsnA1Woh5WbLLzE_ekL7wQhixBa4Ks6mQshkdLwEE5wq9OIQYOv2HrLLl9wr9QysqsvAi7PI4wlghIrB6rTw59jloqrTIApw6cJ_1raJZKeijH9g2-1qEFCdNRCLVxPj5YBA7FJDkQjp7HegOazyrRa38RaE2LmTDGuhHAilnfpbhYKkay0bTgXWj6TIhfM6ax4bwq_Wmqc7BUnH0EDJz-BLfh273bE9W-iYXfnJ-BJPbYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=TLAbjhs7f9R3CKy_4sAtquvrqH4KxBPo2g4zJqZ0KnFz-NoIjEH6LwwjVzO8loCpbzkjAsjBvnG81UcUIibM1oG7qv9E7dND5ir7r4-Vx2qKRMZkyR_OjftjOAqhJvJK4P9pXutkU42uVPi6i4bHTxgx7WJSfPc3yaoXMd5Ives-rBa7BS2TnuMZfNngNpQSGRXO6B6AzlB89C9xzQ2E7ff3XegVyzvibJ7zk0AiY8s07n1MdgMgvuip-X5auFGdNDLI7LrI0634Q-N7HHmHo6jrWBURWK6HVNWGDQf3NJpQk1J12PAJnhKkTLYOtxfbEmC9FmETzoU7S9gXt-LfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=TLAbjhs7f9R3CKy_4sAtquvrqH4KxBPo2g4zJqZ0KnFz-NoIjEH6LwwjVzO8loCpbzkjAsjBvnG81UcUIibM1oG7qv9E7dND5ir7r4-Vx2qKRMZkyR_OjftjOAqhJvJK4P9pXutkU42uVPi6i4bHTxgx7WJSfPc3yaoXMd5Ives-rBa7BS2TnuMZfNngNpQSGRXO6B6AzlB89C9xzQ2E7ff3XegVyzvibJ7zk0AiY8s07n1MdgMgvuip-X5auFGdNDLI7LrI0634Q-N7HHmHo6jrWBURWK6HVNWGDQf3NJpQk1J12PAJnhKkTLYOtxfbEmC9FmETzoU7S9gXt-LfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwz038Tj-Rbn-aJYkzYvfuhY1rkps1K9EW_uDTecphzHafEWap3iEthHNgSsG2WfNm93CNGgvh9P6EdcMRzB2FQh84bzQBGtQz0S9AnIgFDKiKy7-chwA-HsdLb7g3A8AGq2ycb_TSRXEWdmpdpo2GTGVfo6uqXyJ7yUSipTsr2VQFypCpW4Q0lCSV8Cgwx5DiTiRErknG252_VIVx_wGbpVG382ygbryHnSLcrH6i3f0eleN9y8beiaoZMN4Xx661YUDAZIYgPasl1_Mq8I5fFmymMuV2x424b1LaGeu0o0BGLFnivx8bcW6ycXP1KuRLsa8BL8dlEOfI-AmRVPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=ozcduTiBMS4Cxf9SEy6V1GtVcrNgGjwndbr6uSc2apOTaUnNSd2PxVRQKTuXgJbhWsyb7T4cV5Q7Qfine7dwutwNJ4Xn8pIPnw86XShb-b6q04lYl2KFVz8G4e4ewoQgtetlCvFT9jaGRdn-H7cYmOkhttZd72hIdsX8NvN_rjMb-dapcHZTVSIl5YGYooFIhL8SQLR3Wa52DkSWAAn2HcOFzkNxpjrYeAt3ub2TfdwRvfynhD_bXiZUS0bu3Zm26EnMbla_UVK-eImZVY7Bz8QIsD-3WY7STW_G8Gaxu3qeuzu-wuN4TmrHrHybNTBVZFDZRX19aD9SbkD7eCxCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDDE6CiP9JTujxKJivbsLM7Zg8PA005yKapFfSloRGnBn7OW5r4qywsUas4tEtJE-18aCbSU2z5U6YBvyczP36XjN9NW8XSgFWBxxQmlbmnJGyJzxwcRih3SbKe_WU3B0dekbQqaQp5CS42rE15vWD7MCjQ-zm4Rap1cbUvJkYXF2JlccQqQ6t86MymqPaI7ooHSgVQfNAWlhLl40bX9n1JnJCCbf-tuEVv0De-b2vN3fB61qciyRsh_t-6AOlx0wOFkB3t_oGLPOGmaE97Fwd9LiESoVtWI4nEfMAu85b2AGX5awAawj8iyyk7qvM_pu82FB2NzavnTlc6ub-QTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKZHTsvPcJbVSAOUZduvsX8-aqHqsC_zVggOQzcTofnJR5qoUeuZRYGL7UioeSsfQZkDTOAihXV3gTFzs8YicZxNliC9eIXoXk9crhKO0XRjRj0f09uP_myltklu41G3bQ0tzl-4s-L6qM4TCUayKWQEEVJNQJBX9W7z-BOHhZnQKFiNhM4K5M69YJoUC5oNVtB0CG1P6Rl8Q_j28MbU143YbvvcPyU4B0lw3U6n2Z1BpIyvLR5zpKFdSJdhGCLJzN-Qt6D0o8t63qY5pZwtN9OMYnNm9hNQ4XKPBFm5_mesbTzNOm8XLlp9VZdwV0yz1O-Efe69JOAKgvL0VN9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=puGFCwoxgcptT7vSd-HQffCyBqZYfjbczoyntti9WfufV41xhIzjfp6Q8QhKkcXNIbsHixDWdUCE0uRlERDf77GyzLsPVlbmADCA_Vkod6AFMxLEc-q4O3Crcg53K9Kwm2KK-klgntfnrxcRTPHiRfHJDb8mvaYfRsgBCZf7EyEtR27CAK8_j4GSszyz6s58QE_4lc3A-22w2c4jl-iH99VruXCq1MToEqpNa4DiAVrOq1eSigtkCcKZ9769c5JNCF3oI1fNBlukBsArsCInuBvQZzFMNwl4Zh54TJDZHStPbENAwUnY4LXzZsTjYK8mo5oSNM2dhU3NOyoQomaklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVCuPFe0zPQgy8VRFbnrNX2lMrdIMQQ9OlcHE5yegvoCigNhED482OT3g6S62KtQZBQlnNJtAk3GXhs-GRrigmAsX76ovd1hSkCTg8OZ1o3Oq0GqpgjY_lh22Echict0NyF6QvBD77Sa8PJ6qRiKxRW3Aci2Q0cJ-4Z0lKmPl98snGlGBHkFvJ_GXieZaeSp9qCkvR0lNMQ3j1Thk_JUA2kl90eL_u53nEOzBlcTxlHCSBon9V0DzurNHK6iV1X_0mVV8dLNPzRzozrxWcTWuotTaDZV6dU4CxYVwhtrbr2FOI_lGWev19FLimAvEYqmh3Kcms9V6kqL9Ni0q5vUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TF1TUtCqoJMsPsvoONmayMNmfzF4A3OPHP03I8xuUqrW4eDXvktXWiOVtim-RWlQfS49i4LKqtrU3Z6bWakIw879Hs43RRRw3tZJB8-T8I_IspGRMoGkmkdhLM9WMAM3emKjYL3YjhmJ5kigdFLP-sw8W7EdK7E7jRT7ZMlpg81xg2k29fYB8Nt-RQ28zgJOc0snCIFo4Ng5XQ9bPTI-T2_cZ-AOmf3MmpJEt03ng6OYdLi6cxP_MfXohwQL_rPZxwGq-4DxD5L2TbHZgu3Ava2ZmzK0lA51003Igql8qtkKLYGao5dqiKB_IXov0yeSxq3Qn-zpLYeD7EG0eu86XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=LQYCf03pAMARLl1Ay9gxKFTw-QO34qstMIjQCXqndHKxdLg5uWh-VEKy6TdSfo7oJf6pcOENjZ-s4C7Ftrsuo5P1Qrevsfs1271ZPQ4mA9p76Dkaphe4_d5WNBfc6O6DTjtTqao5_F9NuKUT6G2L8oYGZ2liHtyQkd1iGQiI_1i5Sayrycad7clfPdU8O-QIBtPx3tv1D-lfE9iiWPMPBxUQPh5FGp2u5AX74SsT5NzFlIDxH63sTQG8aqPmSpfNEZL_uSBEyJOMKU_TgBPRQQ_nZQVjLGbAjM-AlLgbKmh8iknDMaEmyp_FA39cCArL6AeqraqNjM7ymocWKW-X_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=LQYCf03pAMARLl1Ay9gxKFTw-QO34qstMIjQCXqndHKxdLg5uWh-VEKy6TdSfo7oJf6pcOENjZ-s4C7Ftrsuo5P1Qrevsfs1271ZPQ4mA9p76Dkaphe4_d5WNBfc6O6DTjtTqao5_F9NuKUT6G2L8oYGZ2liHtyQkd1iGQiI_1i5Sayrycad7clfPdU8O-QIBtPx3tv1D-lfE9iiWPMPBxUQPh5FGp2u5AX74SsT5NzFlIDxH63sTQG8aqPmSpfNEZL_uSBEyJOMKU_TgBPRQQ_nZQVjLGbAjM-AlLgbKmh8iknDMaEmyp_FA39cCArL6AeqraqNjM7ymocWKW-X_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGoEOhUoJSpSME0D2rdedMVqW87dMz7QwoFdsNUMY2U56RXVwkJMnXupD4dD1FvNx7RSGhqAVUzegooSl6r9FBW7p6H3UDR5cxbfsAndEelwvJPmSZxsD29NRqJvCh_QDOz2QhwMfR3LfN1kvnM8uc6iQ4b0N-vrzPZdzkPLXdoy9mvkFDLtxnDcjcFar3kwmynMTGTmQETBhOyTr8USH_MOunqwNTDSZsihooMkSTlGBNQClj7tFR2tG13zYE-h8UiLIUODi2Jw32ctYAbVh_KMLrD5B6PgDsCGGBStXm_NgHi6lkS5N1JczqSD4Aa1KsHP1LQMJNc31W5SAslYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h49jT9xuB8DGKMNioELL0JJSOt9xIBnDbv1NBh9YhJCY9eudPXDRcW3asszJDHhsrlPN-H5xyk_v_akiFDrFCSvBR5fm1XrJ9bJgmzSArdyTIcn40IPdP2ylecsWlCjrrTYDHSdZc_DFlfR06944ZWAJ9dsYA84GVIjvLfL0WwuXUeaNerehLHsZlQxkv81qWePjliRnGNNjoOQz3_B9yeSMzcAwJdNAmZHfWOd45h38D5cSR-abP-kFr_BMukXlhiHtnAslKy4fWxRYvHAR7OmBXfeENG747eENVqPy2SLFutd1myhOB6Utgakgs7zeGFFKw3DcJAiAl2vQ2pg7dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnAzAcYqJqAh7rRTYAQ9_rmRo-zUxyAjLtZLlhhcOA63kuqTFAl3_kgYovx5jzIZMusG1l_11VkLVp0wRTGd0jnIWVmfYofKBB48R2z20_W7_AEz4iCY9Alf1c4xyUKR72x0Xa0XHolYpcSxl_1ZUzhYQTC6ILrbTudwHQHhenlw36tVdbR5ORzBG7zIhawctAZPpIt8YBN5waxpmwj6QlAyb_RqPBzXLKrUdikgZEcRBRgXXJVc7v-yVRBDQuDnu5lYbgNphGRzs7LToD-FqEwdqyNbcpWrRn4jpZ3YRqd2diok57PsGFYYKUJE5-Nd9KGNHtasyCen9IcrRQ0Zsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2vHndmCWqC9J8nZxlV1p5piHbH42SZ6paXRXwjp4yF2D_KYDBu-qol1Bi-MeWIWCJMseYqcvmztmwpb_IS3XPyZHJCh_087xNLDi8YusuWw7zbvwsLyX3ryHa7hHNVWOwmixludoJ48Nqq6lY18lXu8AQn1cQqdkVh_G3mbK5ttTyMp7lNmfEwl2Z0o7z_0owFnVgHYPFDm19eAy2g7fWq2qoVNr4lTPwvOCYGSd58YzZhgUbGeuslNRcu__00PD9Dfh4PBYOcMrUqzoJnINM1pPfxe-JraeEa3sf_QaKPf1StKXOqjp2Uoca4ncZ3iNF6fczckV8gu6Qa5jpvnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfk_4hOWaN1U68Hc2lJla3KoddooD_uARivMRiM0Qg2RaqOtrtWezZ1D6I4uMzO7gW3Q2TCLS2r7tal6vTIUrkvnV8oNpkbHfSWqBrbDkFwxvWc0ttq4mN35U7_yspchhUojkwZ5jv7INhQHMH7TgE2gYgZxbdpxN3Ay_W3JuZVZXPPEs7qhnx6snUrP9R5f5lFlNjMrHxiHL1Xz4IJwvJ1bLlI95lu5tTEP5Q8ledz5B8Ssq6Zkk_tQb6nqX0EJwVhLdtQqX91GNQ4024Uc3YBvm7341uCOcvDHCIWhyQgqwpsjZxD7C0vN6ACfznROAHuuy0uGXZywRHQHW-eN4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1eaJD_dpYKdZfobp6j6jxBPko8M1DUXMXtDoNqozfMDEldojDphW8CJbZ2JrTlSpMrLi56GM1wBG2ib2es9gRA_0FYlgdZBG5MSNHkLA_CxlUV2DrVgDsBsgY7m_-IevQ8CXtcZ406YpDyyEG7yFLQgbkahPoT0IuOr_UD5L6SlfdeVBkm2yIEgMIJvGrTQNtN4Fmmq6MJ2hHU6aqOlwaDaYmUpHLTOggue8YM-G9MDV8ZGgGiy7phMwqxXQSDQJgWllrzcrKIXn4OBtKxbimSIhoSSN1ZYDzzoElG9subAXXodVfiD0ekQH3_4CAC_25G0OKXskWZ5xtxZmFwCiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5EpI843qQlY1RJA7oQFViJ2K49wDTjyBBmfoEVGSJ9cDAzPuwZxOgpXrjG0_xGf7b2PWlroppMxaZPPMr6sjgURkwR1xLWNbYutx8MmmAAhk7Ntd5VK_dAJGqXueucW7TAb7ES-ob0HyW9gJyVi4yHCxw6jQjCOwtbeuXm3DRfoZkgqsSstHJxPA-PCdMtnZJrt3we8RCvevLs1jH-zkj_WipXHxPbyTENNlB8v35j6wdVJiRTEYYGQ7feN9--ndK7CfcPtuNh0JRObNCg9wE1wUcm4khQsSWh01BAh1vkOnUs_hRUoCohFoe_HqWWvxV9uEXVnMJ4ymf7A0InMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6qqLk61_JrH69W72nFz_dDHsHNzqdPpW2kkB7i0GHWT1K0sG3azEklcVXYNu0xA-nf03WK7kj3h3Uk1TX-CJRq5eg1K8cCQDlFLh0XHR4-h87754XCrmWWGxIMO1AmKThFaJ9CUWYTWXNisa4ZiFE74nMZk_AsADxgU6CVB-0AG-_Au2QIRfkXrQtUWhIRM_7Q34CQ7jXaqMgq7qx-5YJtbSgCgSKlKC12cNrPPN29gNPnVNM01l2R3mLs80ocF9BjAG3arpmMJOg6kODYnWo9F8l1eTDzk4Y5NHAA1Dmlx7pRWxir__YBRb_ie5zdYQfzmjssDYAfJxhEJpC-qmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TS1BbBNQq0_K6jfTbtvY-c7ZvBjTaVMvX0S-eZ9Jzz8l6KV1S0x2hbwNbxV5MZ9bKT9pn93hxtInkfIRqXr95mEQhOKTFDBpFq0qtmplKcLLytyuhGHuWlY7OzIfMBFDMRZYwltcmSrqr13hLEGqS6hXgIL1Sh0WNaRt06BF_bS5t7asrxoIpKX8gfI4ZLhGVxzXu7AUMhqCheRfBJucCAoI_paC3KlXslzGNddRggDbKRZa9G_vhbBGf72Zc1QtaUWBWZ_WEeU52N4f3vjFdz5XkeV8jRoA2IJfRz0I4Lx1zkA-XZ3UaajC_LMPDONBSoj_-Z0bfpRPkfRYsOD65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین
🆚
🇪🇸
اسپانیا
📅
یکشنبه ۲۸ تیر ۱۴۰۵
🕥
ساعت ۲۲:۳۰
🎁
۷۰۰ دلار جایزه
به صورت
FreeBet
بین برندگان واجد شرایط تقسیم می‌شود.
📶
علاوه بر آن،
۱ گیگ اینترنت یک‌ماهه
نیز به برندگان واجد شرایط تعلق می‌گیرد.
✨
همین حالا پیش‌بینی خودت را ثبت کن و شانس خودت را برای کسب جایزه امتحان کن
https://t.me/betegram_bot?start=p10_r4EF37DCE</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/26073" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHw2FdZg68nlZmhQ1ihFoXY0mPK941ilfzTXqI-gbrRokZ6NrYzcnMTA1mQzX5Siwr76Mc3ZhZqjom389lD6N49u429E-c3NLE8CXuoyMN6IBv2Qd-TvrapHj1CIEIEuoaxRouhZ4bTFjxztsu508XDsFgi_6b5s1gQyt2pQ5d5md8XjupkteE3esaPku3rk6BeNnciZJjw2_7CtWCKyhjr9EmWhB3d_dN0ISLRfK6sC40IsVzJBGKbdjjms7GRLOzVL6Cnv1MNjykSry7RZtOg4Ty7x8Ftp71ZVNDneRpTB-Dn-1QUqwBE1IBoLRrp_LRS1zMCFvk7UNAl040bwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiShKAuVHvPnloWd7Qbc8XTLgt5qONMWoX_az4N44VTXOe4N5Y4el3OUf5kcSmE_w9BEMQ0-t8tcsDjj-7kVUiFU0mJ-aH_F29xnqYUlw4cjIcpFS3TqNqCJKjGMdnMM-X8Nk7-Z7t7HO37FOXt9k4dl4wAVGOQV96CS-fMhMq5LQBSTUP96hsSix7eu-iN8abErO4Zy1mhHzDkLcLt_qdgbkwfZuoX8p9PvNbXUk8jXyrkj4Q8ek6l_cIy6rt2naXlWPBE26LO8l9kCvIAW5U5mLh4HeT76IjaD3XSI9FaBotKv_nDIRgoESl4Q7vkzVH5RR6Zxa71U3S4VNws4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=rcoFTCLakiWNsmlgbIRJz05AkMLCFg4zjvgqMW1uAztLV-df3g-VNw2QlEnCan9z9zGkL-h6R2O9aNREu8zxzHa0KliXJDhkNIgNLDxC2AZaP9t60CoFVbRrgiar-hGEsahjaQbRaLEvsezn4BZXfngt1wDp3prXZ4cv0napvZeA2iVX3315pQAl2hxWT0a7stPm96bh94olgCnIWuJzLe1CYPXbOPnDOwzOhAPuZLF69ZLNsT3yE3mSydH5D4Ol0IF7CsAeP43rGSHrCx7mVfmdbxNK_1P9130indGdMmUuuTyhzcikChkUrlMfBkAfJT5tGjnHNFZXcwZiv5gRRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=rcoFTCLakiWNsmlgbIRJz05AkMLCFg4zjvgqMW1uAztLV-df3g-VNw2QlEnCan9z9zGkL-h6R2O9aNREu8zxzHa0KliXJDhkNIgNLDxC2AZaP9t60CoFVbRrgiar-hGEsahjaQbRaLEvsezn4BZXfngt1wDp3prXZ4cv0napvZeA2iVX3315pQAl2hxWT0a7stPm96bh94olgCnIWuJzLe1CYPXbOPnDOwzOhAPuZLF69ZLNsT3yE3mSydH5D4Ol0IF7CsAeP43rGSHrCx7mVfmdbxNK_1P9130indGdMmUuuTyhzcikChkUrlMfBkAfJT5tGjnHNFZXcwZiv5gRRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX4ewok8PZeIWBpi68LjMDGgFyAtR8JiDfT-JcDTcgTWOhKQhoQKnwKn9XzoqPFvWJbmIHUZ1PRgnj9-WxHbwyo1k9226ql1-eDRPWFASrGaeDacW46NFcBEWl0NbAG3V8I-t66TTkdeCfM1Sghbs5M5SW-8G_I5ptU-ubWqdbrUounW0SkZx44likMvQ-GwALWbaGRls0NkHs_dpzkl3Zir6Ie0RMiaEH_ZW66BaxuUgXZONfTEdFW6j_mWzAARbCitc4GRrEVXkEu7qGC1Ek12XIeNSJAc8KLgR6nlJQFY8j_A0JHrCXZeIn3O-rJBDOpTBjLbRwP7sDyvpl1JOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQcAzmlFtUvCkNg0mz3eDd3ZYrB9QFxzZfo9JWSeFW2JDUAaOoJBeNztxq9zkNywaQZmoSFzo4p5s5hBaV2ydIfBm2qk6H3Hp4df2jHM76IuGx9kfHU0UB2eF2W6aY7sJ-_l9dP0v-IvJXBAbEbZpqFwyQKJkGg1DDozsqkGigdFBXCWc9tapIyyt_li6cZc4gDQOq96KGB0D_I_Bt1CV7d9ktx9nXkjsFO6aDsteHPfYNI2Dhn-jruYdRmU6oUSeJ0R1refnsbhOyvZk1SppI27JiQo2G8A_jcOzbH74JnqoC3n742y-N_O8kHyu3K0Nqjuf21Cd4NC0iakmEgAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlhrT3SPLBPlhjFPQ-Uc1hLskqduaoSUUa9aIZEkQ62RGGJARHdLKbwMLAaQpZWU_cXaDmlWBTRJIET1lcf9BlFFOHzbZgOgy_BtaXEy5OLTdy_z45PDUVyGnMGnC-j1KWvbz9Af1uat03SvZKftGNqdBHsu3RDOEm00PKg27wLhs3-4vhN2JDRkxGNQhyjiXRWJ7etp9ZLPaHfLGFNG-RNUPqb8iZhdLch_fRtyrgaVfhdYJkjKoZDU3JFKNJpjUWjg8uDI9s8i4Jl1aZYDLf9dHNSlUyzuWHGIALDx10eHZtVg2laH_ezybyPmgsnKB1L3Czk2g-p--F3VQ3dxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=mRyBN10dhfB_c9LKzNurJ4Rb80lD6MUMM0MBrLSNYrIkI_B5G6zTzOwRwfL1F8OfHM1hJJKcnCct_M86h03MCVnhCxcTQAZQuadNIHTFqLorsYg-iQTvbqH7tAFif8e4vaaq5uskbB7NdvG8NELjJqeeFA8-1uiyDU5IC9zbE0C4U6Me2qpx9GAVH1Ac_SgRuABbcz66Sz-lQdX9BUM7PWHDrrMqH_4Jcq7gywxUbYkMMQJv2tPLAzRTScSKn5AzCbRmT41-0t8LLZnVIfgO2Ix7APTXS0MxD-R-64tHjtvv-FBbuvWO8e2f-69E7j2ywbSikWsfqEtd0RzDFOp6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=mRyBN10dhfB_c9LKzNurJ4Rb80lD6MUMM0MBrLSNYrIkI_B5G6zTzOwRwfL1F8OfHM1hJJKcnCct_M86h03MCVnhCxcTQAZQuadNIHTFqLorsYg-iQTvbqH7tAFif8e4vaaq5uskbB7NdvG8NELjJqeeFA8-1uiyDU5IC9zbE0C4U6Me2qpx9GAVH1Ac_SgRuABbcz66Sz-lQdX9BUM7PWHDrrMqH_4Jcq7gywxUbYkMMQJv2tPLAzRTScSKn5AzCbRmT41-0t8LLZnVIfgO2Ix7APTXS0MxD-R-64tHjtvv-FBbuvWO8e2f-69E7j2ywbSikWsfqEtd0RzDFOp6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZOYdOwlYVXZ5NV6lb00k09NM3tXXF_svKxyXbQ0JfuOGhT5Et9CpSKGpV-HTOyVWbOnHn1rYGgTOKuTA3pLfK9gtl2AeCQpNiHhkNyG-CP2kkcuKvRqSxXVmjJDd4nh9SR511UYrIumvQHIxD3gBHPvhE1UTmBn8UGzXd3dIYSIEexQRVYpdGoTkRTqOPA4UolNcbmnLSEN3Myh9pwl2FlQ0D3_2Sl7WxbWnZoJRw94O-ukaocTdMVmBARXFN_fwXDSnaTotr2QLIMaQ66jT1PfqzhgLlqoN7Igz9zNaDEo2xJXsQ9EqdkJgTbYNBvz7gfG0l3l9d196PoQ_SsOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltSBajRbrcv1y7QApbqV6qpmXjsR6r1Wq6QdWmPdGhf2l0ICPR2xbqrxDtggEjTAcsqonIpSE82kJTIKMGuZrlxfLwCMIW7dsdHRGGr_fYtGiQFhtxIa0p5P5To7k_fP_OHCs3_UAX5S16WWv51Mb3zBONyY_6EaEWtZLonW4ejaTmJ7Y89SgCNGvHU8FgDuGbkjYHAEy7e03-v5dzkWSC9RhMl29jUMpwXfR6x6Y-BR21pZIWXeQuSn2z7LUmB5tcgGHET0ExXGUkfXSKWgr8MmBo4-QV6sygdyi2UzzkEUktSsfEN9WSaiJbAyoPukhkkDQSbHzyZpL-xJT5Y97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIxMh8FOkd2Uw0U6LjRnFChNyXmdHfKFC9sjrWfMUA5gT-Fq4TJX7Ct0S1WY95G7lCEEthkmg2P5JGnijPd6GB3ytlWb-TOptJyG2d0SXT57qyhMxNupZI1HIgbo-5J298DuEab5E2JM8xC0yTR7HgWOdN-OhJ3224wtloFQ2NHe6XNfpkflHPFsAm1LvAvqW8bnYXwyx_IYnk3aaHFymLNtBIv94DeHS48_-yxD_sH7Dr_xtxhOq6LuCm5XGQmINJ-GQ5uJ3TkB0_83uyXhL7GflO4ilKJ9um1T6_TqVFoRKSMRtHi-l2rRHeUj9n7jPNqWE97Dv9_T5gGrur8EBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZUpWesZPo6oMAvzFREGClSP2LhwxXsh-9WiTD0KY9RWwC76GMtTykX2quvBtzcde8hx5mo_GUCZnes9vhd5mL4Nly-xbdGHVgr-0yGkbeovi8-1_L5_AuV6JI2sRUAEaSOrI907X9Kz_oPFynWa8YrjunZGzghd9_93L2_4oUFglliNZpD27YX76TDbFJSYKS1XnFqqhcahN3Jc_tgMdM9zSPWl4dvfwFeDsX8Vl-F-tHdBAZGHLEsJ2vSPGhyLYltlM_FbAdI8FoJjibqePXdU59eoTkwKJYmzwFMMjmWQnegwLQL0XyjtHq7wp-eVOpdMuPWFIjrkX4Zn05s9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=OQ5_BO_ta6g_F4WSEsJW8yV8GqVeirJFzPF_lHU6hLSmxMOPOQY-oJFg8_QuJ6i2-QHGViiRc2Wr7GWg3yqyDhvZYvDtoeLizqYKDNr2zbYDqXhdyG5W-VJKvoyfXukqE-PF3i8srJ9-HAI0y46qTkBeUBi2v_B-kBE6GX3Q2V6kXem5cGJc96D2S8Gs4LmHG3IP3kOsin0CucXJ0kvrRh135GyR7cIpDBsi03TXU8GxpFJ1D6hStxvxJpwzH4rxIrsY9DgpF8pxiw1uVC4AYpOXeRXMQoRi_vCN0XhnX0sPdm2hBlQm4OReFkrZsjrqfNbx7buclj7EQ31ruBai4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=OQ5_BO_ta6g_F4WSEsJW8yV8GqVeirJFzPF_lHU6hLSmxMOPOQY-oJFg8_QuJ6i2-QHGViiRc2Wr7GWg3yqyDhvZYvDtoeLizqYKDNr2zbYDqXhdyG5W-VJKvoyfXukqE-PF3i8srJ9-HAI0y46qTkBeUBi2v_B-kBE6GX3Q2V6kXem5cGJc96D2S8Gs4LmHG3IP3kOsin0CucXJ0kvrRh135GyR7cIpDBsi03TXU8GxpFJ1D6hStxvxJpwzH4rxIrsY9DgpF8pxiw1uVC4AYpOXeRXMQoRi_vCN0XhnX0sPdm2hBlQm4OReFkrZsjrqfNbx7buclj7EQ31ruBai4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzeR8ijwNXGv5RucEXGFz2UIQT0iYwP29XS0cZjSz5bLABbNPVuQIGc8ttCnrzZgoPWIVY4EE0b0FeOugTQ-2Kjkf3v9XpiJs2zcRxd6fsAIJwRnlYNMOqsu8VDYwSUIiTQbpYtKwqmh_jnBu45oLqs3Y_5kbnzkqTPpwpGZNxqFDDAoJW9XNAuLG4wYZtF0neaQDwzOKBNq1zjQiLFlXTDK0xCFcDRDP0LUTLq53NtwuERrvgoqTzwFQLs7Rkg_VhYJ_wJUwZmDAdaAJwj7Ts8XnLylIh10lP5aTM8T5gv7E2m65r4ZtMJCsAVbzIIGyr5MsvNBzKY7rfjf5Ba2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8HJ6X3TWUUkJlvOeCOdI4xvdzWTbv27KPHSoLOAAZtaj-cN9YGahl4Y4hv9ocBw0tkgvhZtX9Uf3Exhr1Ofb0_Dqtqt2w0Y4vF46ZGfhOVGok_5kz5O8Y8FpteIvmsXOCexqbnezDoIH2gLOVH6X-rWUcyWETxGly2_pwPwGmBb26MS_zKdlhr5R3Tt7vBRzXxF4Xhnoey63GVvoBjRenx80GYtGTCY_NBWty8TQiEN37mm7we-YcoOgAj4bUbFfP8xbnx6aRQxcqvStGuCkE8253HWnRbKKneVTDkjHVH4viDWfZMpM60SNRLfUhKIy8uyooPygKlk_z0SSWO4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=ag1IVV2pSTZD9cjU0znuxb8XqiuWKIFxFWmc7dXuFGC74TacCGiXB_AtxS62QJjR9vb-oG1nTLE08gUxFKWcYjUAEqBs45JW3m6Pa14_L_XAWNLMzgixwBmiF5J69icjC7gRNpLasptjv_yQcR0yP_jN6kGqcnVjSXcHudLmWXq_permaAG2S7dz99Q9l0XNAiGPP776eL9TtOVPyzJKLIzrdhP8p5Le-xKNo8bEMlTjMdJ3TtWSixB90e4SR2LMU6tRvrxLpQ5qhSbDJ9-0DmoVI0ePU6NJry_jky0XHMDk0y5pQ3gZ6QrMUywk92J4KQNegHeHdo1ujkuVOjrreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=ag1IVV2pSTZD9cjU0znuxb8XqiuWKIFxFWmc7dXuFGC74TacCGiXB_AtxS62QJjR9vb-oG1nTLE08gUxFKWcYjUAEqBs45JW3m6Pa14_L_XAWNLMzgixwBmiF5J69icjC7gRNpLasptjv_yQcR0yP_jN6kGqcnVjSXcHudLmWXq_permaAG2S7dz99Q9l0XNAiGPP776eL9TtOVPyzJKLIzrdhP8p5Le-xKNo8bEMlTjMdJ3TtWSixB90e4SR2LMU6tRvrxLpQ5qhSbDJ9-0DmoVI0ePU6NJry_jky0XHMDk0y5pQ3gZ6QrMUywk92J4KQNegHeHdo1ujkuVOjrreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=YSJytoT-VWAZF88AAj5XF8TMIrI1qjF4ORqB5EnHmlT87DhFFq2hJBc4hCTsw8LQ4IVeQOI9KFwh21RKTYklzvGD2pg7mWfQiCfq927FpKSYIOYeE5kIzW2FdNJgfDBErU5lRxjjJSrZDgjJz2J2zqriVu7hsY7BQcYUgVMUKY4mVTD4oxZ_LEWdEt8uHYAgoLYA4aiKc9u8Z6i_pCFzokIN1C3s7JfrWv4A9LociPzdWGnykrIpzXuLaUi2SYAM62j8u_N4lW8VmUifWsaaC6ofP05gRI4yf9mKHAhQj_7tPvh5GvMeaqzj5tcWowhWjLiTlBDtJYoPU-Hry-qVAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=YSJytoT-VWAZF88AAj5XF8TMIrI1qjF4ORqB5EnHmlT87DhFFq2hJBc4hCTsw8LQ4IVeQOI9KFwh21RKTYklzvGD2pg7mWfQiCfq927FpKSYIOYeE5kIzW2FdNJgfDBErU5lRxjjJSrZDgjJz2J2zqriVu7hsY7BQcYUgVMUKY4mVTD4oxZ_LEWdEt8uHYAgoLYA4aiKc9u8Z6i_pCFzokIN1C3s7JfrWv4A9LociPzdWGnykrIpzXuLaUi2SYAM62j8u_N4lW8VmUifWsaaC6ofP05gRI4yf9mKHAhQj_7tPvh5GvMeaqzj5tcWowhWjLiTlBDtJYoPU-Hry-qVAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRPPAwxqK6XVSn35TrVTBKreDxRu09AgrmmDuHA9vtjFvy2nlktqj9wDW3CJfAvypP1DGyreBWMKlBE7CQ02BC650x9jntSqCETDWCJcZsd9wMWnnS6WIj2oIaqloW9U8NktXFQ1DO7SYzgLyv_6QYa7voed-iMlxSwZBUSztsu2n08Cm-fi-0P30EVm2KabnicITC3bE7yMwmRR9vWGVtn5NAvm0OKtXnA0rlNHk7JUNkdmQCvxB23GfUKjWKxxcm94FEoe7Sr5ZkF50rncFPtB-e3hsxZzEFm8vDqqtXQFnxskBMUOOCIaesWLX_HlJ3eBPzbfuSPgQ7-Ed_9zpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8HD6KNh06pGnR7Vd6UAiWE0HvbwiJzGWYHDeHAeKHA92NyK8PUCEmjxIvLqH0ynABcn6K1ha05P01yRHMS8i_2wfJrthm6jsjgNuMyEtJSs1juUR2Gebw0y5n4Amye5r-_Dx2ae7gQD5fL01zgmzbNLtcoYdfg_Rsg8rlWVqo2Aesu5qQd-iuPx1fV-ZWkO2WDpB51AKARLWbvTxXlYjxDGfDZWZOYgblsUlIKBL_PZJ_W3LBXJLCO6XofUahO6qji-PgK8BNqVdfe-1IIEzKfm1f3qYSwYQqHorTEgRlZcJ0wfUBuvBbREGSwfZ_lXQIGTbG9PzZ9FPh18EJJigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVg-yNKb1MQkaIWceKHkNcN9d8EWLknaBsAwQKyqhTSgsGr-X9l1PWvgoNKxUz5CXSadIqIVLg03dlPDAFtUbN23DLv3vOLIbuks-MQH6fN6knI_1CQY8-PhNfCaMr9j-CVDPZL7iSwPLbJlAnV19vqIaaNv6FyXIqIfictSqP_Rxqy1BVk-NyOuidRGbGG_pay8Tyibi-BOBrGf8G0utfFRSVjwAzm11YFAK1IEKl63vy8dpQVJWRwHXqoi_oUigCYi4gylTY84oS_YL9CsKzRjaLVpcXi_kq8PFUaY-mJsTI2xDO2FK_-nc3vtAwnawLsj7IxuRuRoWzgk9gw1Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWBFjjmGRlZ404ZBiqKgbbRaOpo335Z-piCb9woZu8PlNDarvJIDzOWfyOwGh3_Xm8obhBB82CW0JSL9KbldQV-SaHFive_iNLTYM8IgMXYu-wphPz7b8Zhh61z1UUKKsqtfkrwnn2c7mFdvZ-ZagvvGABwOBX4qEJzE-7j6UramARp3bkiEuCNot0nCrHhpyWd8Bl7On044gEzM2vi8AbphxYFp1bKajD03mj7zHIiA4JLJ3BdtIfp8ENjVPtuzv46CJRV6G9WHC3cCuZmtbJzWmaAkVSbCnmhyZnxF-x956MLixF7Y076hT2Q2PDbW7vpmPwZn6jWFLN1Bd1MNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiar51BXqCaAE0qo6nznpGrALHYhhI7A3ITk7Psn-KA_-i03G-wENB-4y9W6yFA8bWWgVT55t6daEZ5b02REPUTe4cUN7lZPLavgGxzeIGzbbHJV0PgeuAupybmGLbMxl0f0D2NRIPcFuFXEskppUQuBAcwMiPsFyAm0tzSIYQWM__bgQ4c87CbPSjCNzuwAw7npgV_b0aIykDdDb1OmEEIXn3I7OZSoT1Y1l9GgMidi05Bp6e9R8EM65dgyz-h910XcDx7_5M-_1jafiiMfpW0TTLIms9-bDABxsrJ8BjHS06Aqjz8tEk3v_KxtJeRRtyflANSLQKUTCO6g_9VGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2h1Tzb1kgSK72MLoVWFIpLMQ81uPwLRWsyx7lCUu3ka2urr8WCmoOH8dWVtlFFSTcyUdriwisLZT5wxY5Dyo1smPPteUGqmrJdGqiYQjp1FKYAdfbGAuFjYV_WV2zkPmUvPsQrCYOHE0OOBDIA3pMYmO3LYjcs2r5gopZas_VocuZgblwFW7Br2EdMTazRr5ncjbEH2fIQNEiiSAcm5Jh6Az-WleKOMNavxa7s0q1a2mytlgHMDMifjluJ5_MBB0OyZgoGg_Byt0SZ31eULY5shuN1PWRuMgaGbbl0N8brj_PHFLQtemilPFk4WL0FEA3yVbMUIomm-qOD5nOoKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unHCdeeS35_WVeNQut83jG35IWwl6Q8fzQ1XYVjuiSjAsvll-Q_Fo5uIQDzCrDt1hzvMD6iZ681o4Derz5TCgAWNkNWOS_oFvo4oZqZWFYmG_uoMB3uiGqrcJRZFGiJ9Vskod7iVmjvrXvn7dtiHwy8TVtflAo90Az8bq1ywqzgDzNpLn2xs-AtoSss6il9ZHstFMZkqrfNm_duqCdV0BCDUXz4qjmkGKiwBxGR4ViGVRH_6o91rvxZwHvsr--4fWdjDxDkBCYaKQ7cNxgXW4EsSGzlb5Lr9e-SAqyVmy7PCZJRFuiPNDQxPC3dgVXhGbUKD8hBMRF2Dygj1Dr-fAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmm9toPmM6Wal5XMA_UnxdqchQUf-pMst3PjC4OHsRYTftpyVTMcHOVHY-hSnieQL24dcsIXXy3Z9l4ldUKFv9remVS5tyJ6Lv5oddp6_5F3pAdD6IAhuZzzBeSTEaglKkTB2QI7cz9c0IAUqE3aTOCLTDU1pZ9rdOgKG2wqnHwuRTfmos3KtvQaCZwypZPp0bHGjPgHmoEVabKOtEqDEpGvZmb6FSoV6E6Ld8ioZZ6ok70KFo3voMWRoBvyGvsNDh85RL1kMqb_IegHxwy_4dcx-iLnfG-X-7b5vYZcT5yeaOb6blz4K2yEyRl6ukUBiVpt_duKcFtLSu6WXJ06Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caGYCPqqZxoNFPqmzdw9uYjM5fhFWLh9jWxQaujzFa25c3-vMES_iQTX9UP-Ejvr00axxiO_1uwdzhxwuy-CZ5ccPLGMqQY_2ZtbdqSa5JW8mR4CQAZy34NLhYCaeJQyB5-gN79B5tqStSoPbTfrOrFyBzIKecqYZ5eO9lzXk4c2cAE-kao_coxXi2K95PSHCIlbkFy7ZvDtOwJjC0WiP0eOOqsOg1Coc4fBgYgtzzDPZdLR6SbkevhLdQvX7QcXF1zjC_t6skL1JnPWkIENlKybN4kO1FeRanTT625Mec1Xn5-JZEFs4fnXG1rS6g8ISXrXwswTGLEHYcO_tLeBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZipO1FS5iqk4x9ib4j23A08t0q5G4-pGxnNDvLzOPSIUhyxm6Y4jVfGYyHPHQIEK0rWPf5xz6gGSJr6_5kt4EiGNyRcDNTnUWHySVOFNnT2bcAJMfHm53GXHdWFIoYKyJ_iOAnGnUvJBUtRdlRIdVEpH7n0HZ7GMowpDA18hyXMZyhB90ZDDgTlZxKZN6ZfpKHrN2rLvKZoSCknVGzTRp110YRzXgSSYGM220x3LWR12lfxRF2u7jywpVglCqTvfCrDsrpYQ_ULAzDk6jA64Q4WhK-pGQDcrMhlC1q62Awv78oJpC4YqI7qRLngtYO4jkULeyYkLiM3wtXghEfcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=KnmGtIIhd25502-VwO9_fCXW4_VrMlvtWbraieXkqdv0MdRzInEZjAip61DRVpxWt8g9KBc1KNa2iw-Mlc_Ym-WWMMIj1hCu5lqx8ERb1MBJI4eWH6Mup7Qo-oF_r4l4pWZMT7nCGIM5_aYoEOlMROvGCxyUKYQVYU5X9iRBpgTf84IKtAL4cQ-RElBT1x-KX5Z7qt8U556X4D_j1WE18gJy6T_IFtyI5PJ1_vLC-3c7VYzNt-M0tcErLOU-SjfjAsGVTKQroMbRybibBmJ2BrfieQFblAeqxPtu5ewxcQr82nYmo6G4OutRxYvZPOPW5pJhfYGq07onKjU5RAqOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=KnmGtIIhd25502-VwO9_fCXW4_VrMlvtWbraieXkqdv0MdRzInEZjAip61DRVpxWt8g9KBc1KNa2iw-Mlc_Ym-WWMMIj1hCu5lqx8ERb1MBJI4eWH6Mup7Qo-oF_r4l4pWZMT7nCGIM5_aYoEOlMROvGCxyUKYQVYU5X9iRBpgTf84IKtAL4cQ-RElBT1x-KX5Z7qt8U556X4D_j1WE18gJy6T_IFtyI5PJ1_vLC-3c7VYzNt-M0tcErLOU-SjfjAsGVTKQroMbRybibBmJ2BrfieQFblAeqxPtu5ewxcQr82nYmo6G4OutRxYvZPOPW5pJhfYGq07onKjU5RAqOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=UU3q0wtSqFx6E4Z0Guw4QZMFIVS6X-3vLHqPvCJbgzu4L0_xup6IkL9jxW0hfqqHo3XN3Q88HinMLdo9oDc9PJAH4Wk3XCp50DJVQ0CIDrvifvbg4kgZ0GAN81jVOTiOJQzG38p6uth8o-zYTcav6OxTgynV9i773-Gjr7XKfquU2T9uMUWxzXeqIXNY0HcFd34H-wgoDy47pS36lIzsp-g3A-FxG_B56NWv3Z_y0plAVleCvS0afr0yZazUndhjidh7yyLyQgXYmvTjW8Hc5m0YiUU-mwn1-rUHPbierXQw9tlDQay4fzPj5oRTDazHdDZ3oQbagXEaJiaq-NPwBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=UU3q0wtSqFx6E4Z0Guw4QZMFIVS6X-3vLHqPvCJbgzu4L0_xup6IkL9jxW0hfqqHo3XN3Q88HinMLdo9oDc9PJAH4Wk3XCp50DJVQ0CIDrvifvbg4kgZ0GAN81jVOTiOJQzG38p6uth8o-zYTcav6OxTgynV9i773-Gjr7XKfquU2T9uMUWxzXeqIXNY0HcFd34H-wgoDy47pS36lIzsp-g3A-FxG_B56NWv3Z_y0plAVleCvS0afr0yZazUndhjidh7yyLyQgXYmvTjW8Hc5m0YiUU-mwn1-rUHPbierXQw9tlDQay4fzPj5oRTDazHdDZ3oQbagXEaJiaq-NPwBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MT3XvZSlqpYQDqJgnIA8uJsAHL2GBHjRhIoZ9ykNPGI4kXEQKgBqwfvG03QchmPAu11bExEFpUgr-hogSPX2Uq5gcrge9AL81i2yKNE_n6HZVVYN-cx84pifAjrDjvoF0xhx_IRxrFDj9pu1JfE9PQHYcIgs9Yhyn5ySCYHTCDTjLe2jVPvqiL2Kne5cfMK40gJGFsSxm2pgoKxZoOyoxrUSETxFEsDz1EGu_ttgNF29T53GMAYzvuxgARZaPx57_kdBgNTKG8imL4qf6Ih4H0y1adGxqWZRl9dvQizkePKGqUZwwAkv7He7M8MrUUQVTPbZyh7Jwc2qeL8xVIHWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSEiXREaItoAslqdTiTBAosZ2FxUbnIOtF8sTi1VjfdBrU_8PupFgsuAcloqncUnEugcso9Rsboz50QpjYaLwTTs7oabw7sIJa6m_FatZU2412V8Q-AxK-odl-d2jT0dqpf1Mi2QNY5PpoiQnwc_fMxz7pW506M1cp8UeC3bUeAdWyAgRYGSn9r5OTd45RKZvrguDiUCA2IJawDobzRi6sFypMJkJLwNoF8-p4_t35ulphfb1c6nEHtQt1PRUq5xOfd3VmsQFPuGYS5KZH5NMM1R_8TEqXKtIPW-i69SLGdw-pEm60yB5z1PHyft_btqD9XFzA4V7cpduMFdy9GqgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyLTpo1-rOH4oPB44S3v6KW4BsKktS_ENKbGuA7BAgENv_Z6uUihSQVMldIgh05u2n_gKhSYswKfdaKeeHudO_EFkWU816x6bWEf4zjLZL-Nq0L8LAMdyM7nsA0Z2bvtSk--E3JkAVuI5TVyziHm-AAoaF81HeQnX7lwyBJ7jVEdQama4f-AsU2DW5ndBP7FJj79P5QXfo9Y4dniMzdSE0fqkIyn0mESCtur7aWsRtCtFhEeotKeIhM9Q9Hv4Ue2TwTDVB9vUf2C9-jHe4VthgTJkUAtR-BCpD7buqQ3XC5rCmJrjzxSUA4vGVowOTGIEoViUj5y3_kpQLyxtfUeWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=bDoLUD28Yy7PRNfxNq_48-s7IeHe_ASa1KWOlIzZyuR2XN3WQ3HeUGAp8_pup1Js_g4WkPJwzyaOXl2v5hmKGb_CS7g8jLBu_aHJZZu-XcyfsP53nXBwcLYLIaQHryLgiIEmRISn_4avaPCnHzNyCA84n4uEmoQDuI15Q4rzpwqS7h6YVP2Gnn2biZJ9og1yUw7rTZXeUDtNqKo946QPZlBZEwnpSVE0IC6icTqTcFjotY2OnkAwtph4P2EKdASr01j02tI6Krg1Xw-PK1NSxbv6KouLP95t5CyAX3dE7wA33pzdRUqrGS-X78P1wXV--chRoadLfVyxkO85LagOgr-y7ghBc3i7M3YcUUY0MGelPZiv7LHgkCrN7dTfx-waNTC7S96ozREy962Z43lCQX1zZ_qGWQaQatbz1F1mw6XSOCSluZchwlSEGVXHJ3S7Is9bzzLTsdg-HRTzmGbTdHEhEF_5WNaKaQ_8XEnjOkNB_AB8MDF374MLw3ZA4K0XW6SlahrX1r8HZfpolHkx4Jqs28l2roZpsA7NsZThm6rJXfjKlhEOfhDSrRO4bz-jhzA2zXqZXMV6RFv0hFey3hy3H4dk0ApCwROCxIksnEZRT3PqsgZC2yy6YA2N5prrWaBBCdljhh_S0HlE_8mHVt7eJW8W2YTtCP7FeNPMEDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=bDoLUD28Yy7PRNfxNq_48-s7IeHe_ASa1KWOlIzZyuR2XN3WQ3HeUGAp8_pup1Js_g4WkPJwzyaOXl2v5hmKGb_CS7g8jLBu_aHJZZu-XcyfsP53nXBwcLYLIaQHryLgiIEmRISn_4avaPCnHzNyCA84n4uEmoQDuI15Q4rzpwqS7h6YVP2Gnn2biZJ9og1yUw7rTZXeUDtNqKo946QPZlBZEwnpSVE0IC6icTqTcFjotY2OnkAwtph4P2EKdASr01j02tI6Krg1Xw-PK1NSxbv6KouLP95t5CyAX3dE7wA33pzdRUqrGS-X78P1wXV--chRoadLfVyxkO85LagOgr-y7ghBc3i7M3YcUUY0MGelPZiv7LHgkCrN7dTfx-waNTC7S96ozREy962Z43lCQX1zZ_qGWQaQatbz1F1mw6XSOCSluZchwlSEGVXHJ3S7Is9bzzLTsdg-HRTzmGbTdHEhEF_5WNaKaQ_8XEnjOkNB_AB8MDF374MLw3ZA4K0XW6SlahrX1r8HZfpolHkx4Jqs28l2roZpsA7NsZThm6rJXfjKlhEOfhDSrRO4bz-jhzA2zXqZXMV6RFv0hFey3hy3H4dk0ApCwROCxIksnEZRT3PqsgZC2yy6YA2N5prrWaBBCdljhh_S0HlE_8mHVt7eJW8W2YTtCP7FeNPMEDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=ORf3OfL2g9nUWu-CCETDitUk6eGst8vcvidlE-y_kwyEs2pkuD9GPyA95-a21zFUHN4-gpfBnjnrgF8d0kpX3EE9GhXEs8d9IvZPW2gU2TRht0Z4igwsRfVuwzowOguP3Q-tTCfRKtnzsPQCeGszZ5ox3SZ1RcRCFUuxZx4CCuBJGT6SVVjp7rRXe8iwcZw_LeehWGOU2GDkve076Pn8XKCpOGh3K2anoAHi0jj1NNCZhh9RdP7SL1O4Op53RYJaLgsPu1IzHP8a051JcOuOLiMXg2vHQ9pQ9E0blE8a3_8IQxnilooQxIr3wsnbl5UVrfIjsZ_LqiQ28QizflDm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=ORf3OfL2g9nUWu-CCETDitUk6eGst8vcvidlE-y_kwyEs2pkuD9GPyA95-a21zFUHN4-gpfBnjnrgF8d0kpX3EE9GhXEs8d9IvZPW2gU2TRht0Z4igwsRfVuwzowOguP3Q-tTCfRKtnzsPQCeGszZ5ox3SZ1RcRCFUuxZx4CCuBJGT6SVVjp7rRXe8iwcZw_LeehWGOU2GDkve076Pn8XKCpOGh3K2anoAHi0jj1NNCZhh9RdP7SL1O4Op53RYJaLgsPu1IzHP8a051JcOuOLiMXg2vHQ9pQ9E0blE8a3_8IQxnilooQxIr3wsnbl5UVrfIjsZ_LqiQ28QizflDm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=lGjw1GRpNj1iBNBOm_1GNVSGdXbRd4Sxua6D6sOXF6jLifudsPSt0GvdQgHSj5-hCSHxKVvFf8GPk4t4qcLalAC41SwqITTkMSZz6aQ-DXDv-8C8eSZXuP0mNt3zg3hqJ4EkT7grh0ohShOdTpAvUrpVd51V5YIhkkJtBbbRnW7utMmGRXYfLmpdATfrCqIsXSWnXrXolVo-C_3vkGnLkgaaA4rwTMvk8Zpl_9RM82efQbeLS5dpNX7h62nDh0FNMXpD2vp_mzLKZhZ4idH2AvGTqXQKmETfecYsx84xgvJCLbNdpf6z1yibAiu3cb6ZN5fn8BGzNvW-8__cmYfACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=lGjw1GRpNj1iBNBOm_1GNVSGdXbRd4Sxua6D6sOXF6jLifudsPSt0GvdQgHSj5-hCSHxKVvFf8GPk4t4qcLalAC41SwqITTkMSZz6aQ-DXDv-8C8eSZXuP0mNt3zg3hqJ4EkT7grh0ohShOdTpAvUrpVd51V5YIhkkJtBbbRnW7utMmGRXYfLmpdATfrCqIsXSWnXrXolVo-C_3vkGnLkgaaA4rwTMvk8Zpl_9RM82efQbeLS5dpNX7h62nDh0FNMXpD2vp_mzLKZhZ4idH2AvGTqXQKmETfecYsx84xgvJCLbNdpf6z1yibAiu3cb6ZN5fn8BGzNvW-8__cmYfACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooEfvpbasaywyftOnl7CVecW2aBYWiaXc0_Imo3VgDLMzZGWKr5rpnqOY0MY5KgVcFZrqOwu2P26Ivj5s-eCBev-airuZzajsydhUZVz9JJhTtuYV5H-jfjogcfn1mLs5Kz5EVB9qYMj3pofx1hSOCtTrozGX8LL0skwi3BDEJlLyrtBRyjZTYDtolNJWxGHWxjECubc3HT5BskU9PtBhEoqSsqtwbeZFFBAhkUnLwxa3h6wP-2BH5QtdHvb3B9NJccwV_8rV43KpD0QOZybrfNgVOVkU3H-XN8qty4XQ69D1Bb0_Sv87hiz3o8efGQeXYz9WTeriLn1ccMIGXVW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=O9kTbPyNUl6nd0dEiYP7Qm0GLjZrHZg78F7UN5LbxTuUtRFbRpR8pjYeotO1G6_bsS65AWBxPNrGztgbaVcZpfan208AY1RGC8ej2k_XAABvFJtYeCIBY7TVDi5_dNDRNL6oyzP55BZRgbh8AkLkcVjhWpbdxKglxzUx-NTATVxWTNztOF6MqVXApjY8GodtHEtdJ5BjetM6otexikwsNG7-sFruTfKi16A3BUYxm4z8Zn-Tv1GhrK6oG-Eqh-xamkuYlkvOj86z8uYMCliPZnhn5W_Ppu-ElJnz3v7BocWibnnfzUeoeLbTLsg4kVtqDCmlTkZmiUUceiNLsrFBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=O9kTbPyNUl6nd0dEiYP7Qm0GLjZrHZg78F7UN5LbxTuUtRFbRpR8pjYeotO1G6_bsS65AWBxPNrGztgbaVcZpfan208AY1RGC8ej2k_XAABvFJtYeCIBY7TVDi5_dNDRNL6oyzP55BZRgbh8AkLkcVjhWpbdxKglxzUx-NTATVxWTNztOF6MqVXApjY8GodtHEtdJ5BjetM6otexikwsNG7-sFruTfKi16A3BUYxm4z8Zn-Tv1GhrK6oG-Eqh-xamkuYlkvOj86z8uYMCliPZnhn5W_Ppu-ElJnz3v7BocWibnnfzUeoeLbTLsg4kVtqDCmlTkZmiUUceiNLsrFBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soPirOMbp0t6KFp5nOF7l3_-ooqOn7IaQnSMFSMJcS7uVS8UfdW5lpeDQk_xWGijWYxkuBj8anNjtXtBjt6738oSy3cG4fmQ-_9z0hneEP6lAB2r5DciFY3kBJ7RoJcS1w9_K-yuRcRfjfy36eGdYPvMmh88h0mMbfQErdD968T4LgqZJ9hu9ZlxxAYgOT8214fgqo62oQyAI9EhnABRfDz-JqgrW37jNRicgINSBqUij1_PX6qPErprdIFF__B_NOLRYw3Wv1094NReOik544fgumpA0ouvRDf0eme0M2v0m55cb7SjuVkJ5Jfvzq1OwLcJDakcxC33P0huL2THMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ15ZeI96xXKXs9owVNfGRl-Ku2_gQGj4KpFki7gwHRDNZCCfoZTsWZUajWcu9Nx-WLZfju132JnBMTANro7U0lS6unfB1n7e22K9XmvQzTFI_-4ev6uNGQSUT9SgdvlrgIpwvHNMf3-4289FSuZTcOF8jtFw2cHBUV5qAhW8fIqNZD0Hvs7jLZhVqRFSMjh7-ICFgKp3LmswRVMXQfIAfvRWNmS9RF8swW3h75XC26z-WJY26VCnjd4H_m8tWOCsT0OT37NFbnHjaGPNd6YBj_qq0xjWFMx3XCByHVdhPD13t-RIgA86UtaUMyjOUSn5OYNhZrSX6gPOLplkKfrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqRYdKKO_-r60aLi9Nu1BviQA2DMPVi_MNplIqMcMvyaits3NcOBeoAP6WYNBHs3sg7Fr8790lOhC4IbD9XCe3UQzT2B1TX27B8l6K2lKX000iyD5MTECP5vZNAbYI61IZ2F5LxQW6ZGK5LRs7D41wFhEj6QbODo2vvv5bHn39s6mwn0JB1XMz6GHN4j5nJ09Y4FWMvy07QF5oJjUb2PixWo6D91V6-VoDd4d7HJx_uMrPdm3eMKRSM9H7slbsTLyer4bnraGIqlDahWWFCoTkmLZYGfo2wnYXbbPAlO4TvPK6_fivXsG0CIu0jA3bMoZh9AohEtBdOWaD6JPwy14w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=qmcGGttuenrS3tQSH_WXCLrGLVf2CxDEMwsErV-KHve3kIp7VEqFzxfOAZq-UEOMQTRG0UyAOrmoA0Vk4c-xES4HfH3iYN_yslEXm3WQvTwJqiXxxTqVBaYAJEeow_rIRomn8PKabkAQAQfdYcs7OUFw1MC1DcxocV0A-WErbEsExgiDw8n0aM_8-Bgl5d6ioMEUSYyK8A-sFbf7B5KSi9zSQlzmkg8cmmZYSf1Jk4ZYYiMgCGHJ9UzfJGpHglf9GAs6IQ6o7R67NRmYGV45r7S_olOTT0EKrD7NwgAvNlOSBGVhua2fxhzGmb2nxYUPdcW6aBLwBHwGlWkVrS5snw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=qmcGGttuenrS3tQSH_WXCLrGLVf2CxDEMwsErV-KHve3kIp7VEqFzxfOAZq-UEOMQTRG0UyAOrmoA0Vk4c-xES4HfH3iYN_yslEXm3WQvTwJqiXxxTqVBaYAJEeow_rIRomn8PKabkAQAQfdYcs7OUFw1MC1DcxocV0A-WErbEsExgiDw8n0aM_8-Bgl5d6ioMEUSYyK8A-sFbf7B5KSi9zSQlzmkg8cmmZYSf1Jk4ZYYiMgCGHJ9UzfJGpHglf9GAs6IQ6o7R67NRmYGV45r7S_olOTT0EKrD7NwgAvNlOSBGVhua2fxhzGmb2nxYUPdcW6aBLwBHwGlWkVrS5snw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=PEPJr_VjeoJgWaoWO27Xxl9nu0zNPDCUQnsALcfL85mC4rBjszjtqpgoVrjxO4t_6IeDRllxjkcVopPfDhw7ibWwT-MDwWPECW3mCTtCdBEj_vyRujmKqaNCZ2FbcFISGPyyZCvO-QfTDHRVK9AFKq0_aw2YhgFRXUCcaTQVoCCnnAjIenaI8pBLn-dh8AcnaSMmPF-sc1_AfUIA4LdF1WVwgjKypYnKqw1-DaoRCQ9dPnsLKU8ame4u4whxF5GJO1kCKcTCZhfQjftB5EBY_OMA1X47-L83ep_kPiC8P8og1XMXgINbt9FEPcB6MG2x0CeeGBSOAme1MRppqMW8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=PEPJr_VjeoJgWaoWO27Xxl9nu0zNPDCUQnsALcfL85mC4rBjszjtqpgoVrjxO4t_6IeDRllxjkcVopPfDhw7ibWwT-MDwWPECW3mCTtCdBEj_vyRujmKqaNCZ2FbcFISGPyyZCvO-QfTDHRVK9AFKq0_aw2YhgFRXUCcaTQVoCCnnAjIenaI8pBLn-dh8AcnaSMmPF-sc1_AfUIA4LdF1WVwgjKypYnKqw1-DaoRCQ9dPnsLKU8ame4u4whxF5GJO1kCKcTCZhfQjftB5EBY_OMA1X47-L83ep_kPiC8P8og1XMXgINbt9FEPcB6MG2x0CeeGBSOAme1MRppqMW8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6tu2EsoPBOM8nEoVDHJWvNs9jnQfViJupr4VLAutCmgKTcQsiUhdm0e9RK5XBuUB29DEp5Yr3KGF5Lsfvex4XAuiPuEJ0oM_-lBYCmlTTEvZ3O9mONdFVgOZwcXDhAaHKU8tsrGUYORK2Gpb0gkk6unGLQIbeK11JCeUUARyNkZnn5fPVwLQHpC_xfWH9N1Gc1nf2enFTZ0ogVj0Lov2naCai777DYsFlTXPvxlhK-J5FuoVUY_SWUkdtV2yw5r8yzsvmdqjbd155lyHq-D0vbo1zZU-kfJfcU_O_HkONkGbXYOKVbhbLaEHFY5A_ewpMVJLp98rhauO5BrUSzKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tmz3UYZb2Vn_8qETI3uTiqpAGdkeKTzBbdz6gZDBnhdz9DQ3mV4aF7aVwIcguTpHfLgWqPi6cDsgpAWtP9YQTLHZa6uzAigNuds9SmJfvUyY-wyBWt_5k7C_p2KQl61Fl8UOCndZAKXzd-u21Om2MMxnlSzte9IqRQ-pguZz2KrcLx9xl7DfLiOhZQefG51iu4ZHbaey1qor3Wp3i-Sgz87siv37v3ZUYz6JnRfo4DrjyKfq-ogBPmD3jzL8SvJSBiSbUzJ-ZG2Gcd_S98OjQ8gLyxhbNY9u8yQ6cvi-bVbq95dsb5uJ0w9moIjy-xpxvfu1yAoumzi5XegMgeei0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLs36QQxLetC7hE6FcCjqWIBKfKv3wCQMLAIaW0loUTkWQL-ZhvtKvE7tCX09BDyr0hEYw0V3uQ0-0Pa7gPgkzGQCWwarHH4MzJFo6qBm40aC2Zz7F9geTqtHmfVt8RdE_2XLJgf8F_4tGtEJTppC2u_qb2Wv34qAFMANohLYZhiEhRdtGHM9ahJRsTkL9AnK92ojiCbis8onSiTpU8HnXVADyjWEHwTvPoLmkx8UN0pi8TP0yMMT_CtlAXFsYHLBJkUk10TKJT2DB8f0pgDft8eLVMEVjODUS71PbNFQKysb-7mX5Wxo-lm4_x0bxT9owQ-__wvGYgL0ts6jW9XPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUB3uKu1V_Ras9IfkYt8t9d9GbY77V_YZbTsIeC03_eN4eO8bcRVVfyKif9sxNGDhGqZg9nOPmwo9znfJNuZ3CU6t9fxU1IhnBXreW0Wb33L_bckE1r7uHbdTpC5IYQFiKGUigz7vm2BRAqVTS9qWtXqdNDDrnILQbe6kaDBddHLPxqnvKUWLrfYgUkA_RTT45aViKk25FABcGCp424rI4QtcFbHIn7Ok_7cELjzpK4xvEQiyThP5dag3fGrxzsw4_rcsH250TCsjYHX9_zU7kQrqks_X3Rlok8Iy-IJf4hw-1mjNz9vS7Jz9vDgbsCmfJOnrovbdphQjh8YOilQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B78poEuY-tos4E8LXF3ULd8UT8LlXpF18-M9Or_2FosCMsMiWigKKE87DsxNCscvphSs1AUWWy0X1LU0kGnJdlTPaupgK3vsOe8SXLZ1JNkKDjWtkXDnQrBzLBxJ4xLY2qaPQPcJ2zOi7Mlnrvl2nZ-sjBiIcrOSCcDwTN13SQZL43rpuet6U9p1j5Ymhq9e_YbznKTXApfIjdUi7-fVLXRFuLP0-IaZR4lyQBMZaZhynXW3ui1VtOWLOBO4aw44iRpNukgM-4IVtMQHaG1OT62gOASuiV80e18l8Jc3N65EPJuiHeh4QxWYvm5Q-8M98SUYfxtcSsA-fEOOD8DIng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9RdHZYh9TrTD5iOrzEd9juke77lSnU_4y8RlGbafM6t7A_8Kt6otmp-gIkkJsvwGmrC_pcDZov9skyijPxIHXR7iamI_zbuFjdSF4pGaV0PWoaP6fXvZh7lqJRzwppFzmv4zTSOBZ1Y3JdgZslbU3IivR-B3X1RUh8YCu_ulAqcvtL_Hc_Hj1Jhe5tpLlQbzP7GnuJBl7JsggCcIx-dFKbBffrsA0GLTr_cyCtedFrvigG1UTcBxiLCihNWAIGXENaUVbK_cZE9AYjDTjPlSZAaff5wUUxXQfAvBpi9lzJgIdpwx5kMHioQ85-xJcmavwt2f6dkUTVA50x2qZOarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI0ZFaf9nf4xKH0o96wEq4SR3foNBftsnFvsAoZiYf7NS5p_2TGd-J9KZVD-Pv0yq4Amu5_uY5jpzxvjFVJK0wgiYF2irETRm8IMVi931FfdbS32XVdBpP1lIXZ5Ix9GJrFW32Mb1wSCWDRLUI1X_ygnU87w1xSQJOedxnxAcVo3c--ZTZztLYFu8ztwYsj-Kwz1tZGrvdxuPlBwmgzUG7hf9zBa7p4wlJar9g5x1TCH4sQjkxA_32C_kRiIYZ6RXKeciUU5vs4tE8DEtBqqGDJvQ5zb850x4P7YcntMaMjq7I35jEfxizpeRTluelwHcTzV9OMlI2Zqzclo4rgn2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=Ub4uaKu8LROnrxnAtaRNGEk7rBoBd7ZRk3V4Qm83DveB5YkWQ-ToQWE2jXRRhiD1AzwiJottml00e867G8x7SW7HFpd11_wY_ucPpAaLix7ws_3B1fOJGIChP0Xve_JD-_jbVhhuiVSvIJNfL9hynBwCRTUQZC-IbWzoxQCKgSPD2JMjDIARVlKWj-dzMxQ4wmpf4gAge8T4p34viL37opNAOXK8geJFOVsxPN18zZrRCa_mnchWHYAL2TRNIN6D1_-SLI4T575qMhai7FCseY1EedPM-OVcmuTQ2CHVYnSJC_EJNcC7u0w0mDo_7LlZAJXQ-rfAEA1yLEg3tsl_WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=Ub4uaKu8LROnrxnAtaRNGEk7rBoBd7ZRk3V4Qm83DveB5YkWQ-ToQWE2jXRRhiD1AzwiJottml00e867G8x7SW7HFpd11_wY_ucPpAaLix7ws_3B1fOJGIChP0Xve_JD-_jbVhhuiVSvIJNfL9hynBwCRTUQZC-IbWzoxQCKgSPD2JMjDIARVlKWj-dzMxQ4wmpf4gAge8T4p34viL37opNAOXK8geJFOVsxPN18zZrRCa_mnchWHYAL2TRNIN6D1_-SLI4T575qMhai7FCseY1EedPM-OVcmuTQ2CHVYnSJC_EJNcC7u0w0mDo_7LlZAJXQ-rfAEA1yLEg3tsl_WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFjdgwDIdiPFHfsMSrg3ddV1AecceIitRbzGb4_DiSEtX6kp_UXMZLY3YKSzlTyWGZHxt8RzrZBECBV7szp4SdvWhc75c17q8QcalQJwNE6gUelpWV6EbBIRFmpIA1211o_kkCmPVsI7C15U9fKDfvj1Ek8QeiOVLMhwWGPnsthf82A83P3ewVOnXWp0dhFTjyM_g-1k8JweslrqglkdaLKedPsTFOTe2K25JhTp_LyFMvdDH_fXLhpdhzZmxStnwLU0YdpXhVEKD7R9xKJGuho-aQSp-rL_7tbum4zuGUZZY6hQ5muTIiPAAE_ig9-dRKD7K9vqepNBvqKv8NxiHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH4Me67FDpTsRrewJoq1MvqH7qMo6WSGtt_50M-JN1KnPOUsjB33z3RpGXMc4enTqX0L58F5HZc1AxsxANYT6IAxSG7JeMh84izdyaNhv0tR0DDl4GxCyB97Z8BauoEPkOJKXukSEq8N0pU9W47eg_RtIdfQ9Vf2_0RS_jaY0Us_kVLpLxeCyihIX-i9JIeYrs0k2BWKyHeIqczo76evA9gUUcrOSS2YzqLwP7RBmcOFhYYG6L_xF1DlY5LqNtdba-2m1qhW2vYDJhEHaFxgsApbldY-dimpKUAwUpPuvdTpgWC9wI2WeKOpwmY07rLFZleQF1PqyaQ6-yAIwGgHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbv8nelrd0BSuFPCHTadA1xX5D_VrFTOxIZ-e7HMA95oFYdepmbU5ezfKM4gEdqnkhzYWRfzwmlGw7HWghKALHkruel1x53Bebwfin8Kad-a-6dsPokwc_sqjIVxtQ51Nw-MSOpMxUs309DSQP1h9mJg3RP4U0cW_ZIdcAe2v-LYrZRbxzrngI6ZUJGkabEIgA89R7hhXbPpqJ49W4hzC0SlLa8e-dQY1G9DGYhaQPVEd6PF_c-IzvLfbGL8KWxavZ92MS2sg5UwekfK5_BmJrZ3O_T3Naoma26vvnoNksnoCJqWj-1cR-Bw--Z1FFduNnu7pwcmLw0q6BTSpAjWSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzqTA0M6N8q1HK5SaWePmGpk3PAjWCfmHw10OUOrnerBD0DHwaV_OFwSoxhJWr3XQn6boZHaJ-sgJYqgoJr7JYO7Psiz-Uf-lIDmIR2MaD7T4yzK8UcCFXjBe_oS2f_nvcq_qA6sldWHwuX1kUqzObcLy_Ks5bZhe5CfFG7lI_Fiu62QOQTo93ww6bS5b1wa3hU6bgl1WjspeY5qOEaC31fBWWQhbud1W9dYTGsOiA3PkDSSjzspSmkTcsIVedQxmY8ebv_0p9_iPmjM0-wmeq5Aq0EPFPRzcmpzLGl9kWhH6mKUq4dtznbFZybmfizlQobveNt27hp-RFQSTG1yag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=oJXR8Fv9FckKb-R01KJK_59UpikD3uxcckcCfRdCVTSEC4ljM_ZYVxLoAJ0lZSme1MYqLd_QqBwZmWGWaWgjedbwygLMNyOgSoAoZ42UONKjkXbO3Q6hQtHiMIWgb-DMQKxkfHd-G6G_WghwJZmfp60mO6SoP7YoBqKU0KH1gWZgC43TEDg2GupI4mn7HLYPSUr0J6z6CjIr6VyPsX0JCpRGDIM6joLWwz_J7UBxPVBfNJUaWAJtApFJUK-bQuv7hz-oZgxcMTZEnxz0VAuzeW9oRfHWzq9vVM-gv1Pzzp3okSvu7eiaD-9Y208t1a_pyV4VT2hlDltWEHXK6FAcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=oJXR8Fv9FckKb-R01KJK_59UpikD3uxcckcCfRdCVTSEC4ljM_ZYVxLoAJ0lZSme1MYqLd_QqBwZmWGWaWgjedbwygLMNyOgSoAoZ42UONKjkXbO3Q6hQtHiMIWgb-DMQKxkfHd-G6G_WghwJZmfp60mO6SoP7YoBqKU0KH1gWZgC43TEDg2GupI4mn7HLYPSUr0J6z6CjIr6VyPsX0JCpRGDIM6joLWwz_J7UBxPVBfNJUaWAJtApFJUK-bQuv7hz-oZgxcMTZEnxz0VAuzeW9oRfHWzq9vVM-gv1Pzzp3okSvu7eiaD-9Y208t1a_pyV4VT2hlDltWEHXK6FAcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWm_LNn8zGGe-FlGUP4ArPRlszP4PItbiwKtv5QXoYLVqBO41gryTFKW0VXJrwoiaCJVoaxFVM9RdWCyCCOzv7gMO1WvYBEWaMqoVZVsJXEs0Qk5a0BBa8vciAynwyuoiS0tkv8Q-5z4jW7hsHTDpjPoQkNa4tS_Qj-C_VzUx5ax1YEzInTnd80FrwBwqJhbI62liZinQyeET096_o6NvSvpl2irovPK5gHGp6pkFJU0RvD3DRLhb1Rr8z7U6uYlrD4advGOvtwTfI2K7ttqkQ-UCFfHzFX0D2YrO6wmyZfqSNavsOX9ry_PusfvPtZx_zG1p1wMjfw8abHXbwyTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJCK8c4H_SxKujfy65UPH9G8CEbfhaCrGGFRYDhDSKvl5iZZibDx4t__fbcHFoOc011d0Zk5QipFYXhBy3sWQd9tStbzyVLkFPae2KrA2wxdFuZYiZlF60PW6M0WcN8zwXEO3OCe9FIM9g49rmWSecRyDUlrVNQnViWxA6m3nSHo2ANLXIRVcqB8RYhMz2M0Og8ZSR_hAjSDb4eu1J86M8Rn3DCqywcUeVgxhpu3tp0DHKb4ecGI-CKZvwRost52ixk0sWQFuoDv1sYB6_8-89l_VLn2EylcCpdlBAc2zPo0jHhHjgeGotdnGcoGGZW9RqLgjdKbTdO5C0AUUQeing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB66TWy7rG_NbCg7IihW4UFNZpaQBJJ1bF5-HMWmZEfwjP69YnHCaH8nJD3WGS7UxSoErMQM4Bz1ia_d1-h-hFwTBisHYdlzyNnFfXaG36AlUxTjaGOPZUxwdm0mBar9gKQyLgofUVbRXiwkw1IcPm8tO712H-kELnt8ftkoRazhCc9f-ye5-xU9EiznCAvM-5osbP9DVl65hGJkASQ7heiguZlX3zVtU11AZ5i3ZllH9YOT58DL2RfpySBmlWCLb1otTL6yoUmVbAZjbKFzr4Z0IQKmiEmx1vl9z9-pnYnVYEZQvOZUuCLur_DtoJME8jSpXf1etoQysQ_bAMUqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsD4aUbHCniwd5rxaPb0YDeYk-7urc8OQZ5V3UiE4-B8GwznkBx1c5_2eDooPlGLb_mpw-gd6EXO0eHc9QXbu8X_7KKuPpaaVHssFtKLFHiyY3JVXlFRu8XASOV3zEL8g5zn5HYOlpaoEm_XLscPZry-I-qSupQDVt8PZfTb6-UZic-YdN3JJwHt8wzGpGxOQZ43bysXnAhsIg1YDpNUrx7ENAlCpr_cJprcLVMJsihgntq7bNMjTFYkJd5Y5jTvy-hYBPHAoxhmaOeMS4I7CMdglxkAS6mw-v5BtGxFKoxBXLARK3g__TZX8tGXwoyfKWwBLc2HEFi5KlDCf2evmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=MW-H-8cpu4rs1luBVTG8JcReqf-LLHtKsG0ofc7jfoIEd1weaiN6D2bxKrNjrBZyJw403w1hV5CL9kHcvaPOGP21C48TNSZQYUhdS0IBx08frDX2V_v-Jlzt3tnhOeoUiqmnr4pO2ITKMXHr2qki-QgwuA4zGa6UfEHa5Nj3D_-Ihc9uvfbveYXJOLCQobkmoAmZPmIUFUuj7bYWQLxsD1SKxqLEJqSor6cpPBE2RFqjAK-QSoNrL-RiS2cf4Y5ersYktYZwDB1YppTyshBcWGBKnmdgsC1vVMrhgT3sCMmMbx64ghcDUMF7rqYMeRPAm3szAkhd2oGzLcsqPvrrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=MW-H-8cpu4rs1luBVTG8JcReqf-LLHtKsG0ofc7jfoIEd1weaiN6D2bxKrNjrBZyJw403w1hV5CL9kHcvaPOGP21C48TNSZQYUhdS0IBx08frDX2V_v-Jlzt3tnhOeoUiqmnr4pO2ITKMXHr2qki-QgwuA4zGa6UfEHa5Nj3D_-Ihc9uvfbveYXJOLCQobkmoAmZPmIUFUuj7bYWQLxsD1SKxqLEJqSor6cpPBE2RFqjAK-QSoNrL-RiS2cf4Y5ersYktYZwDB1YppTyshBcWGBKnmdgsC1vVMrhgT3sCMmMbx64ghcDUMF7rqYMeRPAm3szAkhd2oGzLcsqPvrrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFWLJQfI4-Vt6kUidqEDx5HryI9WnOXA0daT0owKI55ACJnA-kns0lFtB7XrhBVxwGKKTQaci54bjwCFdmm9mPj_kGTnzXVSJwp-SPC5SQDeuOPRtBWvoqi3N3RZ66MQ97dcnngcvartnO5L3zq3wNCWDmsD2gWgh6mtyxssjl0QXJrQ46Nl40Qsj7fLDrg-ks0BMlYUb0UsTA4DRf7hON-2VLJhVTWttdrIjSbzZLikxJtXYz5I1Z0AsKqP6Z21bl5cwSLbUu-8FsSUhlM5bB1DKyGG1RhwnoLjCjaijvjSHDDN1U6XffCIcCB8IAvSTPzvq1ikTcJJWPI0imKuRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9XZYAEnPzijP1kIYQOWD_H-2UPBxwiIj5A-Um8z-i5iq5UX0g2WG-7wUJTUT9qCW4B6zHYb9r12ZMuXxUgYdgGrMKuW6C2cijFSKceiaxUnA_mI4l365lS5wY-hIFW-jczD50RFMpdxHsaLbDnwIkSfgRkQh3x1V6KmBlvz83no9Yyo_-gQR5We5B99Y2jfshq7SKYj92yDtmEg2DBCiyEg9_HOxXkA-VEglx8s12RiunZsOZ4SuaU5w9GpDxrDkT36hLehVrNkiPaJeqb5viDNl04cBxJYJbmJ-e43iUMeFs0Mbun_sF9euH4Mn1OpO3H1vv8YCo2fvHWro1TgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeYM_bzv3k_QC2RQPg6sc-BMcI1ukZuxdCNBgk-zsCh7rT_WMdhCzr1r7HRBgB5NOHBsWxF2iZTLVkV05Jm7gq-xpNeuiXmWvgu4K9GOti9QlZXJZJr1zi-kAibdWpdCEfyO05C04nwyiq2Uk9WgLqxr7hr5UZluzn3jQdh6awyuYzM2CYKsOVaCHKmvtwRPrHwbhTucejnGsrpR06_K5aHs28OZZqGE4TkW4MjgSzWlnJMcCMG5uQYsR3-rm0mwUHvagJFRlKUcviLdtCz4mpFZPOGS8c3PPxzO7QpBdqdFES2qW-0otzHjR74fnnvvPcB8innyJLUpg9q7WFSAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me7Dqi4XKnklhcyuBLcT6dHzoXDvEJbhJIlvpHO2nfw-_CVjYzqKpGfIiHpJklDnBR4JK1QGBCd38qQ63wsPVnQQW1Og8IwvQDIYYGh4jTHArq-WH63OeNWz6e7MgmelI3Zy6MZf0AHAAWa382I5ovrZLDuI0QordEnqdpUQbNVMhVzaK1jp-m675vEAixJyYROnnRLbWgFUD9QNTFShoI6zY9SOb0-OXuA0gtSDOPvtqM__txj898TNKgOyd6JRDaSPjiaUMX7keZ5TIvuGTPBYBX5uOkwypsXyL2OC0TQGlV8ZaQ4ItovFobDir79Z_BN8myrjNbPtCM3YWF6PfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8ZLkEgIkz9V3VS0_f223sqOL6lZTvSNsUzYL68S6r_sksL6-X5qPbGSCuWR8xgvkLcaxx5GoPtf-nWIhb4Y8xuKzNILM6m9b79Vfqgb0zy4jyVwSMGPRcNqWpRtfuXfj6ETuhyeCpZ5vVkHtbe7DuojFhkKORXNpgerN_kAKOHpawNwMbKUjTzoQkWpKLCiD4BKVbL_fW9gRv1kCf-mmIR91snCRuX3PxIinJrz07cy9PIo36dGWB9lhe1UMwNiTfy3lRniswZegNYaho4nuQ0HwK6CQp1zwudxSCFluZjJi9FrXlK0088ffUlIR0tzg4ys8kKomEuX-uIoct1FMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt62Wbof02mS7qQu1HbqXUAZnJ073i-7fMxhnUV8rgu5rp6HQpHmDdfH0c8feSK7vevUNo0BOaNIP1IHF_BLb0xquEsSe08I00XJDvKc--fAnOkcR7azSH9UpsjzpPahef2RvPA_Zjfg8ZbP_0ptFqspAcD2n-frzs326liGoOaRRYktrDfIx1p_vryGYDuyPqazO6CdK4lNjg-hEigl5YRrKcTBSUyQ1hQjI_NFtjMZVJkTP8KX5DUJxmdqrtxk2z_7PINnQk5B4tw4_eJBPPfz_wFVEpPr5KxeWd8_B5BgNmKNW-ITkr3GLWXEdqIM5PX2F0Q_duEi_glXZ0McK-ys" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=NDK0ZX5okAPWrOWgmczl_vd68cikb5i2f0PB4QYL_ZcOSEm0q-pcSjZbS7TsM73PRR-S0S2X-_QHI13XMqJz-_o3TKD9AVEH7KmilS6CDagf0jpPkCp3pEQqbz4eVV-HJd8x6Y7sBA2XkhXZqr_kb0eF3cqnOUD0h7h0tpBQw6fbTHZaV3WVMaELr4jmUlnSR3bC5HGtlwTy_phyFfraQ8AMaJi94_G9iHDV2mUneheg-xn-liApsBYUmmyaqgeRBHDOGNiMFH--KSJojrEmKEspgjQ3EfW2xV-hgu22BvJbSqL0EDQ62f6m1zwfNCWlsQ46AWLYkoRgD7OW0GEHt62Wbof02mS7qQu1HbqXUAZnJ073i-7fMxhnUV8rgu5rp6HQpHmDdfH0c8feSK7vevUNo0BOaNIP1IHF_BLb0xquEsSe08I00XJDvKc--fAnOkcR7azSH9UpsjzpPahef2RvPA_Zjfg8ZbP_0ptFqspAcD2n-frzs326liGoOaRRYktrDfIx1p_vryGYDuyPqazO6CdK4lNjg-hEigl5YRrKcTBSUyQ1hQjI_NFtjMZVJkTP8KX5DUJxmdqrtxk2z_7PINnQk5B4tw4_eJBPPfz_wFVEpPr5KxeWd8_B5BgNmKNW-ITkr3GLWXEdqIM5PX2F0Q_duEi_glXZ0McK-ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=Hl8lHPBsittbfmDipr0u8Y6Vmgy6otfudx73rI_eX5HWy9NdaqY5kOO2iX3799fDVv_QO5iQsEdHOuLYGjB-1mRR68tDzHPBYb27EpXk7Fl5p6KPAmTVQlYgGqy6ay7t5Q1risLkjhFMVZMzM3GInTCJrstcNmlmbDQr9RYLKsWDpgy4yXRf_1qqA6eIHAsa14Seon_dw2peJl8p-jhjKY2wAaWSfNWZd-g4fPHR48cooEG2sawEOCmjvCK1vmR6M00AsxFs2tBwBaMgamhKCI5wmfw5XWgjj_iX2X-qCe06SFCrUfOx1DE5CX3mj-9Dq7h8C_p39BQ3tWHVqBByVoCljiAZVHtnlNffORBq1JdalrcI0KbxMhs0rGgW0Lb60a8TbvGHcMaFhhXXfmzXBIckuCmTeQ1bvICZp1-tUsj9DXhNpbVCnLphAmTrRHl3sKe_p8gGslnlb5iYtVDGeqY9opk02NlytEPMSp2dunDRwCo7ZINIwpiTbYIX1APO6uso_sFbPslmarHo3U82ak94IFN1Cj87gFWrNi69Y5zNicZmlwrNV0vD83dbwWfRoMlwZsNYMFSKTxyEYsR_u6UInMJv1jnOq2kAZZBQfwTeMsBjF6ivb5JX3EVfU5xhvf9wwOSTBphkVHnL4R6X2i582gpAXUtOLuYCBe9fSfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=Hl8lHPBsittbfmDipr0u8Y6Vmgy6otfudx73rI_eX5HWy9NdaqY5kOO2iX3799fDVv_QO5iQsEdHOuLYGjB-1mRR68tDzHPBYb27EpXk7Fl5p6KPAmTVQlYgGqy6ay7t5Q1risLkjhFMVZMzM3GInTCJrstcNmlmbDQr9RYLKsWDpgy4yXRf_1qqA6eIHAsa14Seon_dw2peJl8p-jhjKY2wAaWSfNWZd-g4fPHR48cooEG2sawEOCmjvCK1vmR6M00AsxFs2tBwBaMgamhKCI5wmfw5XWgjj_iX2X-qCe06SFCrUfOx1DE5CX3mj-9Dq7h8C_p39BQ3tWHVqBByVoCljiAZVHtnlNffORBq1JdalrcI0KbxMhs0rGgW0Lb60a8TbvGHcMaFhhXXfmzXBIckuCmTeQ1bvICZp1-tUsj9DXhNpbVCnLphAmTrRHl3sKe_p8gGslnlb5iYtVDGeqY9opk02NlytEPMSp2dunDRwCo7ZINIwpiTbYIX1APO6uso_sFbPslmarHo3U82ak94IFN1Cj87gFWrNi69Y5zNicZmlwrNV0vD83dbwWfRoMlwZsNYMFSKTxyEYsR_u6UInMJv1jnOq2kAZZBQfwTeMsBjF6ivb5JX3EVfU5xhvf9wwOSTBphkVHnL4R6X2i582gpAXUtOLuYCBe9fSfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shhb-g68iMXPHzq3bllIHhVMe9zBGZGFx1tLKpmUkHaUd-_BVP1Y11H9UDuNoya14hbIuwnNhXfD8-OIlfFmWUmpMLdAEGuyMcJVEyLJFVhSvj9t1rEMqWcOMWH3GcydWws95n3CmkilZ_5juRp8CcM5NPsepJ9rWNTbTlEDMbuM7CRZw0xGgKQ-1NoVhDXB1aWYRCAobNTCQigJVUBwiWdeOHy9NS1EJoXjIIj5yDzwzgN550EDLQ6q0dM6JlkQOaDtSgAXkFPoquhgSW8b1mY0rpWmW78kUyI-VLbvsfKBXL0RUbbOfeSeRR1QNb90vpXKoe2MvjYdxCVpmY2PKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf0A6Md6Vg2uRpqefXiDnFYKGa85nzfzsXhRsKfMrQ6fL7LZfn0Ia21R3w-PXBrq-4bBDtIWEeDeqAmE0s-Ax-mlSW07QjbDAysuuMxdoXpkttlxxevvpFT2vh_VQEU-LW5k1QwZbSsjpv6Q6HEjWpti501yGtNOIiuM-zwh5tRlor-Bh5rvS4omxOJiJHWmQ3PZGfW9gw4G-ML0FcGXmpKSgFNqinH5tTG_W6x5I_ii1278vH7aA7SAX3YM2s489zK-KAx9Vcg5Q1vTSo11O5bKSTWF6QOMCUHZ_SczTiEupHGQJwHM0To4KpcAvq7mlV3DBJjODdE70sb-cELUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
