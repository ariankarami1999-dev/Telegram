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
<img src="https://cdn4.telesco.pe/file/J8vVpPyR41eYPnO-i8wts9AEHrQLWq7a9SYaqqNuprZnaFUiMrBFuZS0Qx9UHVuYumyMJuKMYO6QUqvEfKjJnwDCNrqi6V2g0AgC7rlyCpbsWTjSssnLCj6Ch8Dj2-gm96ZO7gBqDnOVX9QmBpd961EKqsdkSzXU7bmYnl6b0_DBC3PC7SZY_MflMkTondqF_YEUXRTNS95LuezNZaIoH9zJ9xv7z5fBU3S3QcbNdnL4o4GZikRd-u__VFJ7lEzYxLBIxJnW_PEvrRihBQB19HVC6QJ8wJ3Oc7MOI0EH9P3fk_bRZ6ChAAe8r3nNNbrFl43qMQsn6kjQJ-fIEr51dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 513K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 23:22:57</div>
<hr>

<div class="tg-post" id="msg-29768">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=DjXczo3gLtwCG779alvnMlO5_2Gr0Md2I6ixVWUhTwhwZqVm7mhhgkeWrlgCzsY_MS_ETAgDA8B7vtw0bguI-hn45SyvIdr04u5RCTF4S1cpKWbCOSt4w0hefYftFTwgg7YoHV7tHb5eQje5BG3xEXoBLBSovNfBRu5NdIaOrwSPImS3_HsapPdxYyoNJc8CYC3z23vpH2dp4UP2GE_W1lTis9jexECzTiij3uSyuIRueQ4no11Ljbx9NAiC_j0nY0FxYBMO51ibD5NJvvOAv9OABc3TcFQyTipnAnbjTSK_tQbjxawmn2TsEO9Re6ATxe_ySa9IarbtlLuk-a95R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=DjXczo3gLtwCG779alvnMlO5_2Gr0Md2I6ixVWUhTwhwZqVm7mhhgkeWrlgCzsY_MS_ETAgDA8B7vtw0bguI-hn45SyvIdr04u5RCTF4S1cpKWbCOSt4w0hefYftFTwgg7YoHV7tHb5eQje5BG3xEXoBLBSovNfBRu5NdIaOrwSPImS3_HsapPdxYyoNJc8CYC3z23vpH2dp4UP2GE_W1lTis9jexECzTiij3uSyuIRueQ4no11Ljbx9NAiC_j0nY0FxYBMO51ibD5NJvvOAv9OABc3TcFQyTipnAnbjTSK_tQbjxawmn2TsEO9Re6ATxe_ySa9IarbtlLuk-a95R4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
روی‌سماجت‌کاپیتان‌‌آبی‌ها؛گل‌دوم استقلال به السد توسط سحر خیزان روی پاس آسانی دقیقه 47
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/29768" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29767">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=GklPqMKHyUorhvo1Np4eRXUEF8c174pCTiuOfoWwcGo_Jl12yZr0O1zL-f6VDDCilxdjnXxepOYeNcyksiE-tKOoLd-pk7eksy0vIWUuPl6qnDto74ulefh_e2OAYYGzXneWRvC4cxrFROwt9uThRLJ5ckOGbHji2orDququO4rXPLJWUdzPI1CebJbV3dGtG3HAAaYY0Y-OJsTP-EanAQNhkLS3mMHl6YbyWmAx12W8BnI7FNMeDQ41Ap_13bAk7uagxGbvYuGCkJEGEfcpEtkWKS2Rumv9L2Nd0MnsDqo1-ppO9jgfJC8YMXUk96zBpOb7oI_Ivn7KYPEiwwMUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=GklPqMKHyUorhvo1Np4eRXUEF8c174pCTiuOfoWwcGo_Jl12yZr0O1zL-f6VDDCilxdjnXxepOYeNcyksiE-tKOoLd-pk7eksy0vIWUuPl6qnDto74ulefh_e2OAYYGzXneWRvC4cxrFROwt9uThRLJ5ckOGbHji2orDququO4rXPLJWUdzPI1CebJbV3dGtG3HAAaYY0Y-OJsTP-EanAQNhkLS3mMHl6YbyWmAx12W8BnI7FNMeDQ41Ap_13bAk7uagxGbvYuGCkJEGEfcpEtkWKS2Rumv9L2Nd0MnsDqo1-ppO9jgfJC8YMXUk96zBpOb7oI_Ivn7KYPEiwwMUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/29767" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29766">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlJRhqfccgotI6JFpSSYIUfWWmKD96HiouHitcdniZQQrHjDsUsNIyd7d9ndsg3mHf_EEGCSVSP8n6TVha3BQCujxDsBjd4P55JTmA0Qxss2yFigyi8QIC7iTQT705tYNnbslfdLW0TM2ophshBivWABmej4BwOxTlpY5RCTyfwCvRuOie0wLzuvlU1gwbf6i_YyrR6g3nCq1i1Ntr8_efJ6FFrKre7TWzVBMBwrwyK_fhnHK8g9QtsIIqPIrAnpozStF86qMXzqVUDovBDGJ4RwvB-otvigyX5BjUWBjxyHaZXi4IbG_w00QM88O3R7At7RbzaBXDpdRzAvH0GQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/29766" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29765">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC_cSJrCfz6NzaE4gFNxez_rwoyGDLkig8-97W4EI46yGQbakmPqwV6NjNBCOCzvjtPpd-4VIGWMfhYUYFbvx0ulLZdVYVV_Xusi69JCdRinBWtpMeRM-c5uqNvtWhBJvCVlz6UAKLCrcCrkQDoAba8yYE9qZcF8T-3Jwuw6oZRbv280Yktmdg6xbsK2gNuuGYA04fW0MA1LLrDVnsTJFsQAYAolXtSezityELe7ivt-DfZGL8MLAniwahxBXwnObSCMds2Ym5_4JnwyM5Hr57LLQ40FcgEHp8Buco_iWHmkvgsGObv4PG1ZPED0eU6mmmM5pAA5ubHhPCEHU-9M4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/29765" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29764">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=Mo6zX1XgDG3us5Z9OM9giAWHBLC5bUqBOgyjeNEzmRqmsBCa_MbHg9ZHZxY6pif_bx56a1cDUxlaxv0Zl7zLP6tEElGViL5TT1VcHMDYX2KwYp34f1J1oJHF1aN1K1ey02TerPLdHI6kz2_8anLQ5XlaC4NKRQfonc-p-sDvl-qdDZXtz6Eq6V0mbNXVoxz3vV7EHAH78ztgZ1BgNbWMRjmy8RTX5WHWji2iUSx9oqkhdWIxnWKzoUs0OAL5GH9XBPAPhuDY41uZ1IzaL9Ec09IFjNOwmP3l_yEUGvHXF1OsVrHkJw7hIEX2WxWp4H0GKVSG-usjCbZswlW92QXAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=Mo6zX1XgDG3us5Z9OM9giAWHBLC5bUqBOgyjeNEzmRqmsBCa_MbHg9ZHZxY6pif_bx56a1cDUxlaxv0Zl7zLP6tEElGViL5TT1VcHMDYX2KwYp34f1J1oJHF1aN1K1ey02TerPLdHI6kz2_8anLQ5XlaC4NKRQfonc-p-sDvl-qdDZXtz6Eq6V0mbNXVoxz3vV7EHAH78ztgZ1BgNbWMRjmy8RTX5WHWji2iUSx9oqkhdWIxnWKzoUs0OAL5GH9XBPAPhuDY41uZ1IzaL9Ec09IFjNOwmP3l_yEUGvHXF1OsVrHkJw7hIEX2WxWp4H0GKVSG-usjCbZswlW92QXAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم السد قطر در هفته اول لیگ نخبگان اسیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/29764" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29763">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3YT42qZ9c4rqAY9X5t9kPs1uu9NKpfciYflMObK_j3_j5OwOW7dLtdWVQ1QVqV64TeT9zvjR6f1C96wYjomQmZWOCsCx9EJMR3u_7azqNHYqtECftkHmUejvXfS6bd3yzBosdyoVfHK1RdWg6nrA6bXX9FjQFWIszkbg8Nd4iKqCpOex2roUxwRTvNyy_N7XBF3e-CNa1jH9iyg0R2OREVhn713Q5EEibqMCvoQ9-cYXQDfK7A78E6rC6dIqb2p4HPPxYxG3kvPPcGdjpNxx_Ezm8Nm544NhHLRHxSyO_Cvef3PtPkQLXkC4fP6a85Iv-u2mgWac_SG2LP3ASdozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل اول شباب الاهلی به تراکتور توسط یوری سزار در دقیقه 22 روی پاس زیرکانه سردار آزمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/29763" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29762">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=s7YRiFsEZ94XwJ-Aa4clo_JhCvDpTUJpbMKmQX9pbz9ycE7Cm30qOdkZenyTb0I_T9YKEOJ8YMXzu9nr7gOS68bGgco_JORVxbiZeddRXqM70k-sug9GNMX2GtUyUQhIsr0C4nlIXdTaaK1K066_lCOO3Atz9_68Xwt-irbbA1J8OxtfAmIhIKKjoyNIC2hdGjLhvkKPEPl1hwpbcFWEJR8VZGnuyALRM5aKDsfrgFUcYSW9-uCb3tu_yhmOhNI7z4vzTkJbD7vEZrKtjg9WOD-ag6T333Am-kuno-qs3vZacRWET0TCRuHK1gP7o92CuU67uuUF2JMK0J3c1KuPdGceXScJpMIIoReRZ19cI9Wzh9hP_zKOOhI0JjGksTp1Wmx3Hv0UIjoZmQ-yltC0LSXj7GSAxdYIAyLKZvjcUuNjBnoFEvII1QUlIfeReWv3uR9jPcDkDol8O10IheisoJA-JrjFXw01W4VoF4TBby--pp5KAbAoS_T3kB4QRuPqDjctIw7PWLJlWtjmbUxWRxPihf5S5s4n11hXwM1F8V-9qz55dMWR99US0cwC4N-0_rMxSjGHkhL0Qsbt9IjP6rJEuTItGk_3FQ4RC0wMtNw7jsOC_moKDs6vnPguXTflCb2Ifezb14W6ikSa46_WuU4tvWYlo586Nz_bSNeyzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=s7YRiFsEZ94XwJ-Aa4clo_JhCvDpTUJpbMKmQX9pbz9ycE7Cm30qOdkZenyTb0I_T9YKEOJ8YMXzu9nr7gOS68bGgco_JORVxbiZeddRXqM70k-sug9GNMX2GtUyUQhIsr0C4nlIXdTaaK1K066_lCOO3Atz9_68Xwt-irbbA1J8OxtfAmIhIKKjoyNIC2hdGjLhvkKPEPl1hwpbcFWEJR8VZGnuyALRM5aKDsfrgFUcYSW9-uCb3tu_yhmOhNI7z4vzTkJbD7vEZrKtjg9WOD-ag6T333Am-kuno-qs3vZacRWET0TCRuHK1gP7o92CuU67uuUF2JMK0J3c1KuPdGceXScJpMIIoReRZ19cI9Wzh9hP_zKOOhI0JjGksTp1Wmx3Hv0UIjoZmQ-yltC0LSXj7GSAxdYIAyLKZvjcUuNjBnoFEvII1QUlIfeReWv3uR9jPcDkDol8O10IheisoJA-JrjFXw01W4VoF4TBby--pp5KAbAoS_T3kB4QRuPqDjctIw7PWLJlWtjmbUxWRxPihf5S5s4n11hXwM1F8V-9qz55dMWR99US0cwC4N-0_rMxSjGHkhL0Qsbt9IjP6rJEuTItGk_3FQ4RC0wMtNw7jsOC_moKDs6vnPguXTflCb2Ifezb14W6ikSa46_WuU4tvWYlo586Nz_bSNeyzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه دورتموند با انتشار سوپرگل دیدنی و فوق العاده فیلکس کلو اِنمکا در بازی این هفته با پادربورن مدعی شده باید جایزه پوشکاش 2026 به او برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29762" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29761">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svf4qHJpGw6oy2u_ewa6afwha_xdHKVnAjYvBUp44waXYklZPVtO9CDirrorpnXU0goLgLnp6rAnO3eM6_n6FXCquQcl918w-qdf8LqGqjD5gB5R4eMvikrDRafJfdk81-dn1QwqYPK55XymgYK63iO-NE7fiAL1fxNs3EIQshyzHVTpGr7vezLOURiuMy5RhrUzswWvdOkZg5KvM35yY1nzkkKdx6zrZzRNgn3LJraHymkQX7zhmaFl92ZcDMdxPXV-HWYRRT81v5UfrVF1Ky8DvGizQrUQpNN8PbJdQS2a2WYKr7MkZZwhF9OE3pInjnwM-zpGMTOG7o1XbR3-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/29761" target="_blank">📅 20:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29760">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtYAZcBUW8aXFgsgM833eNalN34tPqQr7jODRR4jD33BbjWzuOXsHJrOFI_xrMhs_qkonhEtVlYVMI_dlHfxyNZ-2hDyDO83egc6gkpLCBihcDt8JSEM2N_WY9qOhLaPrplLy_s75jQnlZZd1IYwMLi-VQzYpdVkpvxGr9ZgrSwdzQJhDhACvzuC-5bGAcR316EfvDtiEBVc_scj8iDT19ME3grBJClYm0OE1QDxHz4pDtqdrIKBD6Ny7m-BM9xLmYS1eUABGD1kgRP_fuBwOmlljCd4n4GZHlNazvkjlVE9RDceECx-vIujzv9bjYqMZVUWwZiIV3DfSaTtkGAifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29760" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7cbHE_XuLG2MoCBARnm5A41ckuQZPCLtNksKH8_ZNXgwYp5zP7M6_3o2Sw1WTRnVA_Ebw6nXp1m8UwBZkrdRgpjBV0CpfqXe4kiI8BtilZoGQuE_K1fn6_nJraK7UAZRE0F5IX4-a0DpXuywd2v9S3YJBoeFfWaEtPj9xnLKCGw-8GZsm2lGzDKnVNEWHgAtcJ1aap8bSKBkt9UJxHCSL5-takzS-0u3xuohurWRaU68rzjV8Jlya2pgsWpJqtDtHQGa51hqjBUKzAIiqRiTfbIYmCb3ubQqIAroC4zDkWqheMP29y8RH5NFFvZ2vLMSOukEoeQJm1wKosU-xETwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل السد قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/29759" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29758">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKXWlEuS8n-bU_ljFkz2Wxg5HQJzhA3uW-CT8n5yayxXroFxsAW2dvA0h23X69y1kDTfADn8Q8w6lwqUaEjiKNd71GEm_a_Cf7d7icSWVHXqYjKGRrzylWBcVelpkIAMYHgqOoQO0VQiZF2Mdtj4As-odpnT2wCuu1V6v9wtFs4HlwSBkVgRs2K5p5wWbqr0YcIKWX4_FAf6UbIdrTzjy0lb2B7xbY0ytEP6uJ6bwU-zc8rmDPZtXCS7sfv3iUUg-pZe6_WaRFkyKnf5Oce4jT4YHl3JCeGQT1vsOfmOYd0JKgQB0RwOK7h3jPopJoaRrHXtx9mIj2wl8aV5tg7-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سوال خبرنگار از بلینگهام:
هنوز هم گواهینامه رانندگی نداری‌نه؟ جود بلینگهام: نه ولی به کسی نگی ها. من هنوز راننده‌شخصی میگیرم، الانم کسیو ندارم باید ببینم همیلتون بعد فرمول یک چیکارست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/29758" target="_blank">📅 20:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29757">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=lBt5wVjmIWlQj-BpWUheop49tA7roBTyIupKxFvOSGUsdNRnalwkga5PdxKdmMyp3fYhusx9ags5P0jVIT3aeMXYfcGTaqmOuJXpSLAQFRY2WnvjCGlfPgWTRRTNJcOAv1vaAp3G1sIt4mPyn1x0MY-isWyWtgTChHia3cdKwWv1u-kQqQJv_ajsUIXtm3NRYZg9tvXUg0dshnMes1cOLaGyhlmrYahtGkGIbFwvP_LEWuOR8hOnYLgMySn3b0klQJSsVafmd21MIxddyvDkAj38yamdI2AOqsQtVh_VAuRl1j4bJGqUCuu1g1svjUZ1kOYh5H_WGCmutC90k13N3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=lBt5wVjmIWlQj-BpWUheop49tA7roBTyIupKxFvOSGUsdNRnalwkga5PdxKdmMyp3fYhusx9ags5P0jVIT3aeMXYfcGTaqmOuJXpSLAQFRY2WnvjCGlfPgWTRRTNJcOAv1vaAp3G1sIt4mPyn1x0MY-isWyWtgTChHia3cdKwWv1u-kQqQJv_ajsUIXtm3NRYZg9tvXUg0dshnMes1cOLaGyhlmrYahtGkGIbFwvP_LEWuOR8hOnYLgMySn3b0klQJSsVafmd21MIxddyvDkAj38yamdI2AOqsQtVh_VAuRl1j4bJGqUCuu1g1svjUZ1kOYh5H_WGCmutC90k13N3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ضربه‌سرمحکم‌سردار آزمون‌در دقیقه 7 مسابقه که وارد دروازه تراکتورشد اماآفساید بدرستی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29757" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29756">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90deefc883.mp4?token=ubBj7lP5i8Ud_6iRwMmqMjv67tEKrXmuJsm4x8jg-hp0cPcMPHuZIsyPtZxZzTyc3uW3rFAFO7auwXsVlM7QjDmgb0A49ZbOPgswuTJDf26Q0ekN8PZMK79_dTPS5SK3DzCn3YHq0kXqzwmSWYi2vDXTrzFILjEzzl7Mpfwmwl9syfRbo0BtAfM77SdvyCs9yEPv0f-VKZIgIiIUj79EhlYP8eRCXnlsTJlpXnd__yZc8OmeH7fxzwECsNTuTGzIV5tetKNG7Zy_rKe2GGGemzi3P51EqtebIypWUf7q1rs6YoZWX7IvdZNmgkxh_yzepIhwYNecdFpZCxaelVUwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90deefc883.mp4?token=ubBj7lP5i8Ud_6iRwMmqMjv67tEKrXmuJsm4x8jg-hp0cPcMPHuZIsyPtZxZzTyc3uW3rFAFO7auwXsVlM7QjDmgb0A49ZbOPgswuTJDf26Q0ekN8PZMK79_dTPS5SK3DzCn3YHq0kXqzwmSWYi2vDXTrzFILjEzzl7Mpfwmwl9syfRbo0BtAfM77SdvyCs9yEPv0f-VKZIgIiIUj79EhlYP8eRCXnlsTJlpXnd__yZc8OmeH7fxzwECsNTuTGzIV5tetKNG7Zy_rKe2GGGemzi3P51EqtebIypWUf7q1rs6YoZWX7IvdZNmgkxh_yzepIhwYNecdFpZCxaelVUwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ایشون خبرنگار باشگاه شباب‌الاهلی هستن که پیش از مسابقه امروز با سردار مصاحبه کرده و بهش گفته مطمئن هستم امشب دو گل به تراکتور میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/29756" target="_blank">📅 19:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29755">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owr7DgnhZWzEihXDkONREjlNX5BfEviamhFIhm_czX25TcsfVGqaqoW4igKLSpNzIfo0WiwG61xKQUat7bzu2fg3Y2CZXrOOD2kxzk4xOmOw9iCkhzwpBqWij0_V5JrtZnKVHKCNlIPGc42Odu3-sAYI6dSc-FnZc5JlVsAjIC007EbSXyp8JE0rMvBPrCuZlO-2-QXio8d18PnBN2bP08NLtlF9sXsYZwruNIOPnov-uocBY3nOXENB7yd2DJOzp2WyjXEvF5Z2a-tq0YgQ_HDZ__Gx2ia3uJS2cvXkZ-UWmxId4bDd0UQ-IAcNqtEuVpImyukQxuI5moDC4yQvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/29755" target="_blank">📅 19:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29754">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZnU8zvAkAx8RtsmHmZsk1ryyiETESwKcH4UvX86his0jr_ztIw08DJJ54yRdRtPz90Ip0sFx-8pRQLRjCIkLCZu2yXb46SA5QJSxyyCw_igMAkEMSl7_1ao3SLX9zO-jFwRo7OCuoxmKEOWiClYTXPjhTzmtvPma6WURyLUuySAu6gyuZkWy5CnFX4Z7cX9PU35XBdmQoPRGusq090owe3XH8ck6LA8aGAZIgcZXwbzwVe9njDmVpiPfIE4waC6tWm4BxXNmH2IxC0cBvjQHIshECAepn1sZWOhOF3DQdxbgLlRjjGnbitfa751ITcvvSgfBBqSaHznwKLgiEX5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فلیپ کوتینیو فوق‌ستاره‌برزیلی سابق لیورپول و بارسا با عقد قراردادی دو ساله به سانتوس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/29754" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29753">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmDrcGZe57GsdMURXmqTCfzPeRTjV6ZH6ewIv2RuFfQW3odvohv-uppZSW49OQtUgsGwVka6yPA3HJCHXfuNFrgcb4n_w188iwpY-vgBuOeAExxe1yCR60iTVpC9_m7YDeqxeWmDWj6fCNB43jTSLykYk55sx7koh-mcGYhraCMdWMAsTzAmgaWla-Y8LlZ7VfclTXv5tSKoFbR8db820y3VJvxs6MRSGMmhqHryDqnh47nbMwBORLMTqvd8LX14Yw3sfVjGz78I_x8yM4A0wcDHQW5WOxZrpjBXhm5iuZYq66SXHa_25FyummOI6-RfxDVqcqkIUjhpYRxfSTbvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛
مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/29753" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29752">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWgK72HEI4DgqNtwKe0_ZAn50KKhxRnzOnFXUcKd-JXPVmcpVLlzo_2Cr6_IwKstSbyUWd0dgGl-eknq5oncX0TmrElnimfxOHAVI5XhRd-9CZ5lLuoVrTBPt66A-VAgyLC53_JEF3XgGqrmGcM2kGOr1ynhZ1gUaFtdl_2xMEE6xqZomomBA3iO3fX9IZH1U6jnqMysXpIH0er90kJhCgc30sMDU47609Ih9YiHhY1MfoACCCBF4teQ-KJxTfINWMgHpKybpyiUX9acyBTY-_JjWV7pdEvCw5bhXkrqTBrY4KCb7BKrtTcHNZgq-m85MvwPtOjr-2loGfwEznh4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/29752" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29751">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpKJdsUusS8LLMx9CzrhrrM0oP1XKrWljJmttlU52WrStWSoArUQi6v1yMxUfzCN4GZE2Q_2ebE9sXSua8coTQwwEgJMKOoiSlAHZE0qAsKSWvd5LQ5yozargVGuC8gxM4A0YBSWMt8Rn_TQAjDBMh8mspo39KmjEs9x0ZIsR163NzIX3bBYpZiserctzk7bb5WX4_K83xUPVXT4shiYDJ26aZO43YB226d5DDDY7zqA4cHG3LahyYb07Dzoi5TZpVG506R-o3V5mAG2jMTjBInPEeYhYqJ0i-bxIMB0frR_U1d0KgYeEaVv0tiyVBpw-bgqcuuV2o0zilkoVjbb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤝
دوستان خود را به پین باهیس دعوت کنید و
🤩
🤩
🤩
واریزی دوست دعوت شده پاداش بکیرید
🤩
برای دعوت دوستان خود در پین باهیس بعد از واریزی دوست دعوت شده به پشتیبانی وصل شوید و همزمان با دوست دعوت شده و برای  واریزی شخص دعوت شده پاداش  بکیرید
🤩
برای آزاد سازی فری بت دریافتی میباست یک بار فری بت را با ضریب 2 به بالا کردش دربیاورید و سود حاصل از فری بت را برداشت نمایید
💬
برای اطلاعات بیشتر با پشتیبانی زنده سایت در ارتباط باشید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g23
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/29751" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29750">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5yrBAVebsO32ndMFe80tCYWXCGPc2U6BC0kChJD6QTCqcYEByJs4uni5BocKZ8pO6Vk0kzoMuOhRCabeBB5YmwJ5AenqsjceTZQJ5wsRNh_98ueT8wqguYfLO1VIhFDoaVQocuHZ1UJHQkUhw2PgaD02j8kLxcHgGgJ60ij6xtLK6qYkTJNoTiUfLe66m0j863ChnMyEcOzEvDHyOzOOP360Ui21oFsBYQKMa5UB5pJm0bFCW5K3W8P5ViKGiZun_2OHoiKMDGlfZfPnrPXf39pychnQQf6ecgan-ZDuO5as7NWs8bNe-WpO8N7l7rRrGOlx9H2JmtJvlaHKKMclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/29750" target="_blank">📅 18:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29748">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yc6dRh31Y3krsF5MQO-9Mgfch0JJYNxbciCeyKW8m-HsqLDDOWULOSaGQupA0PikmhwDw6aSInTSQfNwThQRlfdX2npgVmqIEaUHosDDZYp-xsha3hj-LXY3KEEpq56bG3xPbjNrWMFEjW47xPb5ifqbGwC8rBI3EjG2WVF1QxbNp7f1IerfdKth1dcZS6KW6UhykdCvLgzt6-492y_XThik3ORee8lQwTwkM5QyL3DUCcA5IqEctgpiHv3InzdxJcjZif7OsUyX-KtoD-XVMxhx9Qc0PQiF8KBvnVnW96NFQqtoGH6uzXjJMKu2hE6PhbdOnl4-q27UpY17RLPkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTh_WuCPbBU31XY9iu0FGbTlZa0as6fxKELsH637mYlrSciXBgtDyaBJFdSlAoMmDq5MzMvMdNGjzLaLdVELepFfwtYjMqbMrKSlvEyL_VhJfkG4E-cJavHiFD_dwZUcm-PSCT5W9Ae3N56VnyrOkL8081ZNaFisZCaY3N36zd6g5kTybRoSunDjlBSYxrWxFballURpiSsoHqc9UTX3ipmYNbqxwKOF-SOm9ib6rg-UZ5qCzhjXz99l7NBd-S2RTEmHiInO_OfekugGcdc7A1lQbXOCcnbXrx9lmCRWWvPS5oRsN2fDV45pfrcThOD3fcX0Ejj5ZZtq0AejBL8mdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا
؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/29748" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29747">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab3DKu2_WuxLe5wPgjZrDDuWemer4Xn2J96xdfAqwgyFdUxowpXd_IRFCDtAfM2wMnKZiUbHmQA98GFDJKugAoxXkb6lsJelQG8OlxTJZICJJXY0aqR8pNhPnTYY2ZhwW7i_D-m_aa-nHgzOy9__KyCFo5RVoB85EmMGUa_nrVwObUjP1Z_agIuRoqj69pvDwvSeYmWm5gSg0Il3fC4bwQ57cdBqjtSM-SHsmyV4F7kw5kYsYCDMyIj0dnU1wg65ZqORg8pjf3UNUkQb4rGsVGrpaHzQ6UDlLLb7g6hKZyzD_twNibq0lYgFjOyZTO7aZtbZGQqks7iugW1I8Z-7Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از زمانیکه
؛نامزد ویکتور بونیفیس قبل از مراسم عروسی‌وقتی‌‌فهمیدبازیکن تمام اموالش را به نام مادرش‌زده سریعا تصمیم به جدایی از بازیکن گرفت. دختره این امید رو داشت که بعداز ازدواج و باطلاق از او ۵۰ درصد از دارایی او رو صاحب شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/29747" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae707100.mp4?token=JojwUJWAM3snKmSJ-N-uGw2zideIY_y7bxaqSIHxzZ8dLaHGON0s_jnXa0vhacj8uVMYYRrDWsypCnQl8s3BJVLF4LmnpXBCoruGUr98-Lgu8wBXsRW3husGzW-7BJPXa6vAHPuHb3aRofmZZN58SgD1bYU4OUvmrI75xaIOCLmQACaB1JmcMXI2UckAYcVe7CpQaz6AroBqaYfXw7zTbCGDcmVwexNTOto4l-uLhjq6s0eFAmzG58Lle8FkYG6gEBfdvTmEtcd3x9e9XNybvPHjHlNiA8z5jKB4VEBeh9aZOfY8G6qyhZNwfUhOwlSWQqIKDdXyZU3Q8x4aOMrduQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae707100.mp4?token=JojwUJWAM3snKmSJ-N-uGw2zideIY_y7bxaqSIHxzZ8dLaHGON0s_jnXa0vhacj8uVMYYRrDWsypCnQl8s3BJVLF4LmnpXBCoruGUr98-Lgu8wBXsRW3husGzW-7BJPXa6vAHPuHb3aRofmZZN58SgD1bYU4OUvmrI75xaIOCLmQACaB1JmcMXI2UckAYcVe7CpQaz6AroBqaYfXw7zTbCGDcmVwexNTOto4l-uLhjq6s0eFAmzG58Lle8FkYG6gEBfdvTmEtcd3x9e9XNybvPHjHlNiA8z5jKB4VEBeh9aZOfY8G6qyhZNwfUhOwlSWQqIKDdXyZU3Q8x4aOMrduQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله‌ تند و عجیب یک‌آخوند روی آنتن زنده صدا و سیمای‌ جمهوری‌ اسلامی خطاب به لاله مرزبان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29745" target="_blank">📅 17:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtBsziVIpbddCG-RhIikNfKTNoG7Ss9qi3txe_CheoMefJ234vzPIzoQUzN4KYVJ0cR8T-3ldBNT7EqYGwxp52v--cbVl_QuK7zmP41AnrVQl8aqexv2v6x9DZ4cvJX3rC9MFSF6Qim8rbKHVCHU5U-0LcYh0O00NRRZjBhM_0x9yF-j3sG90ncnhVeBo9vzmZAvjkg6z7GT6JczpMMnkY4T_heD2f-QZf2WPCH9DF3iL8ukncYgWZHfe-XujSWGEHf9m0AE2wAcWZDUjOMVzzTI5tCN32exGEz_tIpUIrZTE-yMhVEj4fGxyicNffKque-HD0iO8euFv5G2UcG1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29744" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29742">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuaJNy3nGi_5sfJV5IJs1Rop-PHj00GgDIjf3PoAlZS8gSO3-1VXMIb96TlrApv70D9keJPeODDf5EjfcwpRyGhvZBFJ1qRZ9wmM1-vQw_wWYlXQXgiL3djJf_xbnpYpFljCrf4fgWl0V7Nrb5ck06Rn6Aq_MNK8Tg2hcxjXRFMVLaBnj1zJstdgyROX5MO8YGYlvfxsP6CcWCmAt8k4n6hBjSOg97YHASopfJ00KigQjtlrBDjb5rb78-OsuebT2hS1MS_Hoq6c1Qerp1DC8l8g7eWttHOCF5Y9muFpNzOfCQL5GHslQu6vEhs5HjXk6-BXzyjqeghHNV7TcTKnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگارباشگاه فنرباغچه هستن که معتقده کارتال باید درفنرباغچه‌بمونه و باید به او فرصت داد. باشگاه اون‌فردیکه بطری زده بود تو سر کارتال شناسایی کرد و از حضور در استادیوم در فصل جاری محروم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29742" target="_blank">📅 17:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29741">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2qRnSYRxSVZXFQMzVQHxdeYmq142mnRZZq1CRnMmDFAi14qBp0FM2f6J304ub6S6Jm8b4g_3yk4nVC_cjeEAnzf6-sBiMVqNJqE1iai31ENEQlJ4UptKKxPCrIrtziONYoRuyuFT7NOivrMYwfW3yF6zZKS1U5EjMzz1Bb3KVP5scYIVpcDtrPwQs8Hr3yF_xJFAR_L4thFed2x0kjI8-d2ktQ2au9B9EgDUkySqe1lew21dJC0e6ujcZQybskUzQsA59qvELENRJfpE8NJQZgJEPyCCxZz94csaMvlV6B0XXxPujahrRZpeHMWE7qjt6_8eL1rkhpSTUnzYYzBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29741" target="_blank">📅 16:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29740">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyrB8gMmetn_ee61WmZgv_AnyRnb4oEbDLEoRRJBc7vE0V4dCUYziyV6SyYvfmdNRMo8uDeGKpvyrE8YBnFJJ_kOlVtYIrrsHsrG7vDAD6Akrt-5edzDsSKgQXXYQM8PmtV4YpNuum-2IkCEGmULoAwsfpm9XB-MKNgNj6tRs3mxzbr2r3e9Dm9WmH1ZvHheb4GbVJo77syT9renT-3X5kktdCoC8SyYWi2-rWENhjiJhXzEsoAiU7PEBr6EbzAePNHOEvp7aRC1HscuTgNkhFFhcGFPxvQMVZBiP5O_uPxLwbzefOjHWnqQZ-n7WEAUwY_qJM3Mu4LpYscH50f_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29740" target="_blank">📅 16:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29739">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAhuIENG1ln2aMFbKP319l6tnPUl66_bTY54U9oitt9Bx1B66F-sGnpxAWmcssLnMatp0DBocMLg2Htbta6gWucoMietW-cg91tBBO5MlrQ_tThjbmNrIgQCDP29VBYGAwevbLLxER7q9ZtmNzaL-PajQAXyRQKG6K8DX2KOFRb93-DG9dl-Oihw76xs_OgCwPNEu39iW4zs0VhDN1fYoLabYTxDYWz9xcuDtZYpIitPDRu4MatJ0-eFuT_HTbrdhnXKZsSfEX43XB-aIqgeQOJZ_tCDBTdzc4wfIDBvuCGjU_ddXnL3sjFKDwa_BLBAJ7u4wYWKW7nZZ30Tu7bpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29739" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29738">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU2esBlBTIHKXpzCv9hBnIYa8Z54PND27oYwI8_ZE18_5FjCKJxur9scZRo0P7IA8EaEXG64vq-tW3CJuykPhFPtO5SlPaoFCLVv3N1JFtGsYPAwbEL9PqpCemW7J04SDq9kOqpX06rd-Zv-D0g1krXuea4vTMeW3ZIwYQ0mtgm1jqrRxPu1l4AJqN-qkZy6Ux-jdwwiqppUai-G9_RJxDr6YsQDS7p9sP1Wa6KJwz384cJoXqBbUJ4LyfOVCmef0PUrDCMaCT9e7PfOX7fVH77qEmj5NhXTL8TNjjDZGFSvr5jmJR4vZ8agYGU1vUBMpzPxHBDAN05DySpYWXaofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردلامین‌یامال و رافینیادیاز باعملکرد کیلیان امباپه و وینیسوس جونیور در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29738" target="_blank">📅 15:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29737">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vwOV3nnG8mguZWqhPBahLA-JltydjmLxaH1fC4XfmvoE6pNvgTGJDCDzH-lJVGY_Q1yZJL8Y4f0LjVgZl25E7UWxCyZ_EiPFZ5NCzF-HYd1S7eZ_12I20LCiQpjviaM2uj4Hx51kfAwVFQsVtvEVLDhOzWVbqcqnoe9MgB7mzvwcMcAu_ZY_t2WnHochz-r8V2vxc5qODOK9KEYTJLzJ8RMJG8a2aeFlqsU9cfBln4DPNH0qREebPvCL-Rhsq5iSDDubkfPEI7MpDn8EC6OUB7Wc5q_R3WxH5jAC_AX_J5lV-u1wTkUq69H45JVyB42yTxL8iFaDcCYMykOqj9wyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2999a059e0.mp4?token=vwOV3nnG8mguZWqhPBahLA-JltydjmLxaH1fC4XfmvoE6pNvgTGJDCDzH-lJVGY_Q1yZJL8Y4f0LjVgZl25E7UWxCyZ_EiPFZ5NCzF-HYd1S7eZ_12I20LCiQpjviaM2uj4Hx51kfAwVFQsVtvEVLDhOzWVbqcqnoe9MgB7mzvwcMcAu_ZY_t2WnHochz-r8V2vxc5qODOK9KEYTJLzJ8RMJG8a2aeFlqsU9cfBln4DPNH0qREebPvCL-Rhsq5iSDDubkfPEI7MpDn8EC6OUB7Wc5q_R3WxH5jAC_AX_J5lV-u1wTkUq69H45JVyB42yTxL8iFaDcCYMykOqj9wyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛ تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29737" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29736">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcVTwp-QvkooRv_qRz_c75xohHt89mrWNZxp6D6uzY3mqetFJzGJ-xXuNIn21Pn9rLja451TYkiBEWfe8f3ydi0l7VKqB9NET2oFMuux5xph6XbV31if7-eZYULpkn2Hrts9J_9X_orcdbUxCI2gWuS5KDjVJR93qz0IA25a8vj09RZ4A18xlajo_aUhSASfM4YGtCfZreZwP99F-gQAAVcnMFKn5aXMyCGqLwjtGXbVnTZ054eG7QU0d_sZWiQwvQeX6neQ8I3ITNVeSDYwSi_LwQ12sR18OHZtGaJiSX91fsSvFVHCS4NFt_Yf08AEBPwMPLuYAT0udtCxQI0hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان نیم فصل و قهرمانان فصل لیگ برتر خلیج‌فارس در 10 دوره گذشته این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29736" target="_blank">📅 14:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29735">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHttzSDEhM_UTtP03Af9pIjN3uUuGe6s2gBKHjgfOedbv96woZO0oaCw2sOWYdEUAoj4tcHO0MPp8hiERFHaBdElw4C1yi3d5GFYGdCIWAc7NSYGhyZBpZDM7zY1Qkv1qlORZptpd93os3cgWTS0Sfc5733nmsFqSu7aoeIMTEQ5dyZ7ksTqj9e8wq6_WKE6pO07jxAm4ZphBf3IrCewm_XebRCgV1SG9q77T4QIkytlScFugV7Pd8_LkcaO1DDuJo6vtTRC1wdZEm2qVI8uVWYVQtSPhPLXqvugn7QLm1fCPbIQdKOBP8wo2eV6BrnqGxhNBQ2WGuf3PAZC-3ag4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29735" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29734">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2SzVBp9PY3BESHMenSn54dma39fxnIXG2bdDHDsVk2Rv0wLhSmPQSMazS2MXr9B_MNeb1FFnlvJQws8jvGPADmf4ALaOD6Wmtz7Lc--yK39FXig_c65e2rvBUJYe3DLOsLMKnYaaSPzidgzSAl1anQiO99pmDdxIBct7zE4j6jdehZo7wmo4ZZZbWHCaJJygfu_3KqeidXbinbx0TXs-x8Z8aSY5KnOenKtAkN_wbI6DU6LHuBgFzN95-eaIKbfswMQ9DAUZ5ve2nN9mVOHB_8fEFZSy15v6awxcAk9peHURc1TTUcepRlLPJcNrvISrTaCtuEGG9FQFt3TQP7aisYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3be0ab7dd.mp4?token=aBPTyaK8CjZ5-zE-WjV5ma4DLoKAK-y8ycAuSFCt9DRRFbRP5roXl4Cw8p9abL0EpBb43Oamo-ucQK0z3WN0yOHlq7y41MaPkw4KBv2Bmz9L0yeKvtm0fW-eJSuZB1NSQuwHGL4CaLXzq4cnjBLxVIjYO4MXyhs709FSWgvVV-P3G3y8_0D44dD51St5QZo6B_RszzwjwILbuRlyHA5nI0A83E8Fh2-3YAGlOQR8iEiGHJuV5eEC9DQdDcZXPxezCiZKADWvkXdCEofOSYDKJNnuXru5TvCxUEPAZLetf8FuQib1ikHNq4ROlav39INokoojZkMDBs7zyz-6is2b2SzVBp9PY3BESHMenSn54dma39fxnIXG2bdDHDsVk2Rv0wLhSmPQSMazS2MXr9B_MNeb1FFnlvJQws8jvGPADmf4ALaOD6Wmtz7Lc--yK39FXig_c65e2rvBUJYe3DLOsLMKnYaaSPzidgzSAl1anQiO99pmDdxIBct7zE4j6jdehZo7wmo4ZZZbWHCaJJygfu_3KqeidXbinbx0TXs-x8Z8aSY5KnOenKtAkN_wbI6DU6LHuBgFzN95-eaIKbfswMQ9DAUZ5ve2nN9mVOHB_8fEFZSy15v6awxcAk9peHURc1TTUcepRlLPJcNrvISrTaCtuEGG9FQFt3TQP7aisYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایوان تونی مهاجم انگلیسی الاهلی عربستان:
من‌ عاشق این هستم که موقع پنالتی زدن دروازه‌بان حریف رو تحقیر کنم برای همینه اکثرا چیپ میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29734" target="_blank">📅 13:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29733">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0PkYjjsHHtQDGv2xiqr2XFYvwvUe7E2umcCPqa9GzX0mW7pmR4GT7qjWPVKVQ_TfSmeJKdjfkAgPkS56shZKVLWQw8dRpWI4O_SWQUJwGAeF-DVW_F5HydMC-g13YGWfuUz3tBOdWJbYoZcLybM68vBm0awP_YNAfjLGiVocDArDarxh2a0H1QODeonu6VqJHs3_1M89Z1knXA0i0vqTJysCLg-U9rMBoOl7u19oXKo0ufSRnc5De0JXeChwSbd4O-grEDnzrX6EVIGNI0wGXoKMKxBpR7CR7EjQ-Xs3C6K5P5ClRR3Z5g6fLv0iIO2XMKPm4WlQFZYVCXrs0dlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خوزه مورینیو خطاب به‌خبرنگاران در نشست خبری پیش‌از دیدار فرداشب با الچه: در فاصله 3 روز من باید 6  بار بیام جلوی شما بشینم، خدایی خودتون خسته‌نشدین؟ اصلا سوالی مونده ازم بپرسین؟ واقعا خسته‌کننده‌ست. بلند شیم همگی بریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29733" target="_blank">📅 13:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29732">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrQ3m4kLsBNyuNFocs5tBATjmEBQMzd3xmMike1uSL3TOEeX1910ExIODGPMFB5JfxtPTrK7Mf3wY0eKjdDoQaI24Ddmws1VC0tq3KaxFSwcYXjr8YOvROYd_5Qe0mvXTFIBuIRJRHPoyrLOJ2x-YyWlf8bUYlJNVoihPaFHubYsFGgyYRdii-tBSJlGO7UvgwJ74sEt-x9aiwnnAJ48eEADbr5ZVery7ofRUdBfvkberH2SpZ-qioEKefNxNDv0u1HI7Z3N15-yC2Vrz9wD9TlnMqziAIGM3qAicrhSQSbA-iiOh6vHAMMD8RvR-5-Zfkcck-tkejgdTJgNYBUs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیره‌کننده رافینیا و لامین یامال زیر نظر هانسی فلیک دربارسا؛ یادتون باشه قبل اومدن فلیک سران‌بارساداشتن‌رافینیا رو میفروختن‌که فلیک اومد و با رفتن رافینیا مخالفت‌کرد و گفت احیاش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29732" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29731">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak69mADGr9jUnbJXx0LuO1m-WUA55ieYiyuyeHqlx2keExqRx-RKIRPuHeK5TefTUrBXG0aUWNFO4GMJ5GQxet1ffEI1WjASIyU-0ybNvbfxo29VqnLlJiPG365Ibzr0_CXxD2NTcVhgPyJMimcWF5RT83UxXKxtvOq0ecVhIyenjTZkSDFeCwGJMMBXvG1vBL1I6fKosneoiYYWBl_bw9G10xNBw8nPB-ZWKuTTdGq0QS7yOeWG0gjY8Etvhk30qmi7Fbsnf8Oxq67-9J84FY7vh3bW3OS6bytpJSYWGDmhlx6U4SsTcQBb8GUipZ5nXGg7oIn8Osfgnntul0UD-qPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d6c3c639.mp4?token=oVYhlg2z9fQBaJjhVpDUyLZ7vBM3bIfIi2u0CxYdr_cY2IK6SXGXcOtOvGDz0-EOTX9lYkvxD93kp__Q0ChGYiNvENph7690GCYx1AuTHCBr3N1YsEHYI_6iBubqx1KldgYkPJMFAJ_FyeJG-NNbTIuWs-sgwwfgSRWD9eff2zAMDf942x-152Jg5Y4WKIA7ktq-YIQvtEbc8K7x49cSpsymRoluJsNHWBridxt8GSqBkUAn5m0wSSl4cg5wIeVte4InaGUUDTHXrve2Rfx0L8R9_9h5AcRDSzhuje2X73fXR3HaXWs-6FhkKQp_6xZXejhdCIGglSvGGvGxpK6ak69mADGr9jUnbJXx0LuO1m-WUA55ieYiyuyeHqlx2keExqRx-RKIRPuHeK5TefTUrBXG0aUWNFO4GMJ5GQxet1ffEI1WjASIyU-0ybNvbfxo29VqnLlJiPG365Ibzr0_CXxD2NTcVhgPyJMimcWF5RT83UxXKxtvOq0ecVhIyenjTZkSDFeCwGJMMBXvG1vBL1I6fKosneoiYYWBl_bw9G10xNBw8nPB-ZWKuTTdGq0QS7yOeWG0gjY8Etvhk30qmi7Fbsnf8Oxq67-9J84FY7vh3bW3OS6bytpJSYWGDmhlx6U4SsTcQBb8GUipZ5nXGg7oIn8Osfgnntul0UD-qPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ بااعلام‌مدیرعامل‌فجرسپاسی؛ علیرضا بیرانوند دروازه‌‌بان‌تراکتور درنیم‌فصل‌با عقد قراردادی تاپایان‌خدمت‌سربازی به این‌تیم خواهد پیوست. بدین ترتیب بیرو تا نیم‌فصل بدون تیم خواهندماند و راهی لیگ آزادگان نخواهدشد. بااین‌شرایط باید ببینیم بیرو درجام ملت…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29731" target="_blank">📅 12:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29730">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsB9zN_5jt9nfSTRUhMFuLploxZ7XMIRO3ypYAYNrgweY2xA1QomzNdd4wGo1T_97YWUkKmI1SO0jcy12Re2u24lA3GvlaC2pDk57svU-83Ctqd3gujkA5QD0Cxr5uITQic3lMAmqFBU6nw8VgHJjHdB-jCowNOHV3pWtZAHbFcS4qtWMOatEb73wpqqco998ZWNT2Uk8RcA4ddroByAvrFJGB-QkTn8VPUaZUqg6-DUD5kTAe-cYs78ARelm3oL1CS5XQMfXCEoMq5QonuPl45ehcItLEmTId7IzG7jMBQIm0RgIIxt9Hh9fe7YAx8wjldceIkE-87z_efJrkN6Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده یاسر آسانی ستاره آلبانیایی استقلال در لیگ‌قهرمانان آسیا: 10 مسابقه، 9 گل زده، 1 پاس گل، کسب میانگین نمره 9.1 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29730" target="_blank">📅 12:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29729">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=LPXDFCmhWGD8g3S3YFfM9CTR2lcdcti9rEpMlefy4NBQCp1jaHDF4OSsmNrj3GGOtbhsX8EiGc_QHiAEuA0yRz988YViXtgzI505ldlvrNCN-10tJI_ZlTh-5YiYxrjJKifZXVMEgIPMbK4mU2jUmc-ENUt9jNNtm3GeyYftT9a_qlyuQaMJQaaQyjSAuMJX1QfDGPFz1y6qgNAgl_7grP5a-q6p_IBWpAdpoTIJ5HHg-jNy5kHLfzWz6dkf4o1sQ5LRXP0shb9NjHIMgMJTKh2foc9u-lQT_4AzNy2dgb0G7Vf7m_wd5wrVhfBhJ9ebkLLu_2tmmKsgPGpq4rsQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b04b36d02.mp4?token=LPXDFCmhWGD8g3S3YFfM9CTR2lcdcti9rEpMlefy4NBQCp1jaHDF4OSsmNrj3GGOtbhsX8EiGc_QHiAEuA0yRz988YViXtgzI505ldlvrNCN-10tJI_ZlTh-5YiYxrjJKifZXVMEgIPMbK4mU2jUmc-ENUt9jNNtm3GeyYftT9a_qlyuQaMJQaaQyjSAuMJX1QfDGPFz1y6qgNAgl_7grP5a-q6p_IBWpAdpoTIJ5HHg-jNy5kHLfzWz6dkf4o1sQ5LRXP0shb9NjHIMgMJTKh2foc9u-lQT_4AzNy2dgb0G7Vf7m_wd5wrVhfBhJ9ebkLLu_2tmmKsgPGpq4rsQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇫🇷
عثمان‌دمبله درباره توپ‌طلا گفته که؛
تو کل دوران فوتبالیم یه‌بارهم‌درباره توپ طلا حرف نزدم و نمیزنم. فقط‌میخوام‌تلاش‌کنم و سخت‌کار کنم. دمبله درواقع‌به‌مصاحبه دیروز یامال تیکه انداخت که گفته بود من و امباپه با اختلاف بهترین بازیکن جهانیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29729" target="_blank">📅 12:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29728">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdnldCEQknoU2SJxor5HRL0ebrC-m4n9aywmQsPAngHeXmSiG572mojjHMP-syMOx_sZe-xz3Z71wZSDdgS795XzBzWBghE5XMn5CdqkdrzRNs8tgeBiBY-i837JyjsEDLbe-ivi05AFVcfSnCZzWsxipGrL0ioBJDe24p7ZnZ2l-JjTDIjXNwXLAvjBZ4ubjcz1JZOApHNRk-lH73SwOJFJPx1K97u3eLOa57kPfVkwcECh-gBatE527YarGVvmYMTnz1n7qWklOYYDznKmj_lqGK_84UZs371qhI0sI078bPV2pvYuzTRm5tJAzj9cg3oaJmqgBFMLM5t9WFtDMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29728" target="_blank">📅 11:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29727">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnr9-O2hlSsSWfdroKoD3_mvuJF0TO-S0VqE2i78gLggUd83FICp0mIKWtZb-XHZGmWgKP5I6AfHscYUfFKSqDvhLqBbdxn8nN-T3f5IADIVKIACqVBf4cMnjgx_akE3F85TPLUWSbuNl8lkSCZl0IbndTKo8LcWA4kBEmBqvYjYHkMll_gJwII4siqTJ4AEk4WCEPzu1iggLWks6SmUp7J82rb_4WUGL9iU8ONZozTI6YSxj36zGxxE1rYi5lSySmMXwLb015UxUQRZFH-CubPBAXIXWQu7o7AXJiPzhHS2oX3V_kocDG6Nqs-JNgQwpJ7qg4ZMCCLht5aJh1SjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29727" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29726">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e641fb1ca5.mp4?token=GupRxr5ov5uS38Ixht22XTHN4hohh-McjFm7g8tVCF_ERa89dYbPuYN4ElkG9eQMMMf_WnQr29ulyiKs0tRI7DAM8ehNNBWc7ZSbndQEhoSa3Xp4Xl9wwh2qUTrUapDnHkKKW4dmQ9Dd6WSuAV3ZzILlhF5zChcfD7wQwt87OgxpMMzW53u79WEnQfZCbfphWwbTfQZhawmP4dY0DfTHQMyHMTF_OvPJNZf4oC2txsCMJzSFgj22zhFenF4sod6cMo58Dte4y5uS-uFAdjE09YtySRhPCLT8ndhVg0g-_J-KjcqQBWyReh2xpIE2FjwL3QieG1KnrsE1tv73qKeo6Wq_mzNoJazmgKTvMxgPBhjd0lAYb8tAyzsG3ZiIJD-wvR7wd-iPTuyddk4gVBTvj_9QzofPHz9E56zqOrPLrZ_GcJE_ckxxBkPl4M8ENFeuBAqkJwkiN2wrewZfTSJHz51xWSwoqUDMmm6xqNgfvM4xgCWMgNf33NPTWVDw3eXAzASKfknlzejcPpqius3DR6NSve7Ki_z1ZwdeJgUpwIwH40AD1Qe4KranHZa0HdPSvUg0WrUMc9m_frc8TXai8jmBBAYE0KDG7_mdXWHNo2dYCQnf6YcFXd7nW9ZTOA9vrzq51lYSmDcnau4v5K8Vbq_6cQscpv0DOr5IbSCssNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29726" target="_blank">📅 11:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29724">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdAPVHFYmTqqVwa8dCQuFSFl-qgJdBCM8wqd1JuF9WDZ936QDBoVPCZD49H0i7ZRG1gnd5A613lqm9JKwjbC7StD68pVSIsL26tJ43pFJg-e0fe6-G_kAAIpi3vdZEPzduWegUeKzsm8ONZL9lUkitd0MZ1V9YVHPyhe6wXFCmlWdlqh2IiYN_rXLjJ8HVjAqGKjndSVmrSdYoecVY4ThEwgumP6M6NPLKyx08-OMhx15X2h4iDvm8-Ob5L1AnUNUtTxqkYCckFi6dNcK-LHJFAoKqejo1-5wQUWjENPQAt-0z42mFHaq_STzUz44J0q48zbxgPrh3CxfpugSCUWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رسمی سازمان لیگ چهار دیدار ذوب آهن با سپاهان، پرسپولیس با خیبر، ملوان با خیبر و فجر سپاسی با آلومینیوم درهفته هفتم لیگ‌برتر به تعویق افتاد. این درحالیه‌که باشگاه پرسپولیس دقایقی قبل اعلام کرد هیچ مشکلی برای دیدار با خیبر ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29724" target="_blank">📅 11:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29723">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cf41ef0f.mp4?token=XOeWVq3xOMlxx5IbTIRrl8SB12LaD3-Wdc5bvKSoVgFAkQamHkFdpTFlYewJtuA4TzQO9nbvzmCVnFFx24aFwntxx9Bnc0Qx0vLWhO2YnWRVMBdcQsfVNpI3GKeI9sgmP9DOtiFQ4R_tfdGtw9PtgUmHo3_EMWjrC4NwtcaOMBhy-IGJR9f-Q-s8jIcxKOXF_rUHIGbMPMEvcO-_JJn7pT6_AwHA-GCz73Ixp0Y2BvRwIL9XBfPjVERbEViryD6JM6G2PwA4ugKuUSzc2Ikdh2hJXmf0acIQzOU691x8UQdCsyT24duaXGN8mGRFq8wzaDWftXhwZng74Q89nko4kYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کل‌کل‌های وحید هاشمیان سرمربی سابق تیم پرسپولیس با پیمان حدادی مدیر عاملی این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29723" target="_blank">📅 10:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29722">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKUgiXHybGzrMaEyZouJMiSW5adAJN1KICpF25-2tfWbxJaMX2cVY6DO0DbEH-MpIAYeKf96Ul6XrBgiekP2XcjPmlqMON4nqF1Vz6X6ZvO6MaYZG2ae41Z5WyUBQmy3SjN-ZOKXt7EziqYcl4U_jeNzwuoWH4ZcTqsyyPE6GY81-bEhPLwK7pijsOQKAGj17-UCEEA7xnBEu5mBZL6274CY_9hQy39UWX91w2DPQEW9zMOSswiy1AY01QcXuxggapW4nGr-fxcugsdkqc2k5LwxbxwQEzjL8vxJxm6EH9IFFvQnbgGmEWNcSy2398G-Jk67BLRDrx4ZqQXEYVt0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند دفترچه خدمت سربازی را ارسال کرد. دروازه بان تراکتور از اول آبان‌ماه ۱۴۰۵ دوران خدمت سربازی خود را به‌صورت رسمی آغاز خواهد کرد و به مدت ۱۸ ماه در یکی از تیم‌های نظامی خدمت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29722" target="_blank">📅 10:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29721">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-hE3TFVAgLgZycnY8_u5ylWPkZjXX2a2QpSGc4YrUMks3jJ_GKt1pPx44JfK3dcHKDCM7J5Of8xQIolIWQn0IcmJBsY23Hnl0YNuZ3a76OSmO2qmM-fPPqRNqoR6SMzfof7zYa-0JNONFV4GyLfDsXB-JzpkHv5X0YrkNQpq5HmfQl05vI8Tu6TJwbbyaJ0NgCgEfAIBi267YQI4vkSHpDO-N7_fag8-j6X3LzrtHV0YRHRMPLqwpUttpdiAEJctAs6M4CuImI4SE4hal9a3pMp7Gyr2W7CYKEZ4IzEMNsrDiMG9NQUJVirjW5yEn_iJ8a8SE57YQpg9YIzsEhhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کمک‌ داور رقابت‌های این‌ فصل‌ سری‌آ هستن که در بازی اخیر فروزینونه
🆚
فیورنتینا حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29721" target="_blank">📅 10:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1TD_UFGE1-VF-HKwZmVx2f-y7CCl2xPpzSY5lDPoXb4dpyboV9skdgU-QFG2r7VxH4nQTkO4u7__2f7pUvjwohTTD-bCcXsYhDp_ZyIxZGUmHn-nqa81kV7nSDtKVfa77jz0X8MBQPzahoIBaRzdTajUVRhEWAMxOFtoors34ob4CGYgJ7T6e_ODfIjfaE2Pvc2uoqcJ0UgP0hfb1c81R1U2YHEXmNjApEMBg9QWW4zuy0rm_Bxbi62X0M1p_w5NmY7HRaZ5Xff0J_x9v3onlRcgpLmBtwMfZVZEFB88nK4XHOByCiDk-Cai90x-rXH4VSjbdpDK7b6XaOteH9nuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
در هفته‌چهارم لوشامپیونه؛ PSG با درخشش و گلزنی تورس اولین پیروزی فصلش رو بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29720" target="_blank">📅 10:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUzkp4IgeDC84p1mEOk-PqXrhfZh14PK9CJWAHOJUGdEYYXSUH_qVotjowEDzxOCr728YvPhnm2h-NkYydQS9Wln7qCVxCs1Linh-kRyAGeTEmFf7avbs-Ug5BO0N2jGAuvVQDtOu1PpDa6_5k-cZJoDjMKmJI1gqyge2D-DBtAejctp40coSVCYDoYaU86i5pFd-lCjLEyNxl6Rlsmb3dTAQgpBnUZbA9sZcoAh3OLMC-N4bqdgeuKtCxZVLJpNrfq6sxtXz50wDu-tA--gBq_PsAE8HrnkFBwIJJXN8qJRA7AWfsq66wIQytjtxQPRgiw-o1t-6h7KUVhcrOdvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌لالیگا درپایان‌دیدارهای‌هفته‌پنجم؛ عملکرد خیره کننده بارسلونا هانسی فلیک درفصل جدید: پنج مسابقه، پنج پیروزی، 27 گل زده. 5 گل خورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29719" target="_blank">📅 09:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-1_WOkhm_ZnRsj-g0cjshLhmUjntFBRI8iLedUBK1EO3sHfJPmca2DNzpoAKa1wStMo0P-DEyqcDlG_T8NpuXdEpbV_yurrK1zGTm4FV9AC3qUP64mFgx0fOrnB6l-FmncMUO2fO8JE-Ra7mezNVi1s9khcKTEmwnmkisRByD46DotI8ldfTBoi3NIThae50u7A0pwkGknT1NQiitPFCQREJls7auUug0lBOj7L6iYMw5RoDdxTeIxaZGqgrxH24weYjzdB831AtzSg0xzYxb1XUmvZTwWacYkbo1Utkayh5E7tDj10gNgGlnAMDbty9MEWDasXoVyt4JtcQxtMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
۱۰ سال‌از شبی که قلب پرسپولیس ایستاد، گذشت؛ واکنش امید عالیشاه به سال‌روز فوت هادی نوروزی کاپیتان‌ابدی‌ سرخ‌ها: از آن روز تاکنون هربار دقیقه ۲۴ نامت از سکوها بلند می‌شود، انگار دوباره برمی‌گردی به زمین، به قلب‌ها، به جان هوادار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29718" target="_blank">📅 01:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJqUNQ3Rhw9ph0mOI0MTpUOusneQjuNe4qmcnGcFWp-2JwMeOPY6Lxnr8BCixpdcIRb0Izd_9DALkVLSpyYbsibVYeN0Jsu5Q7HT1l0qfi8W4j9QjjGi3d5_SIdVtjSiicbgmpF_ippPWo3Iz1NL1QvfwHjBj9jY6m-a0n41xwKdVe3EGPQmYCD1ADz6ItHY58vF1fUyQccgONUWbuoBU5gp6f4Tmpug8Ljmv3BTPAuX5lmLBo2NL9iaGETu9ufpjPtSHSz1f2sIHtuRGOrmJ9sWPgXXAgvjeqTRS-G93aIO0dLoPlR9_DU_iRAzfZT4bBqsVWw50Rnr71BYQM8cLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ا ازآغاز فصل جدید رقابت های لیگ‌نخبگان‌آسیا با جدال مجدد یاران آزمون برابر تراکتور تا تقابل استقلال
🆚
السد قطر در عراق!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29716" target="_blank">📅 01:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkOv5ER58yq5uJNTcvGA0EEVPsbRJ1rjIYM39ZFEt_uczIWMaK7UkCvytsEdURTyliYUAONSOFAHBQOlJ_IpWOz5nMe4rZ_y32XN5VlotXf72yqZHa_k68YkA33GG06cLWtZi0xu9446X3J6GTj7WAE9oNSxw3cpt6rACI8Tp1bpEcLz7H8s2rB2Ikxid-N2VnEeJ1Cress0VTFYWDQNxrO69J2BEyqJJYmdXY1C8CosureRxaxHoR47qZX-XNd-nrtocwzfowZDR6XIlNismg5u0lFHbBmO97oQkykbxTQ7JOadi1ie1EFBjyH8twNs2mRHsXBZ8Ctojd7E0scASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌سخت و پر حرف و حدیث سیتیزن‌ها در دربی شهر منچستر تا پیروزی بارسلونا در ادامه درخشش‌ های یامال و رافینیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29715" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29714">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXgoNE4s6aILmWohGZuNTAe9PyHCE0KtaIDZFq9hTLwFxMJiroKizTsRl9KIlv7CPep33BQs3thkSpqK1BoW7lDuh4HSwq4I9XSA6iGSzsYU07yo0MbDiMkQVA4UgI8u6Q_0ctXVXEwtsKQEtRXkkb0Zdeog7WwyZ-ys4PjY08CEea0hatPRgrq9QlYy1t5AfJVd7LIIZ0L-R1BB6UOl5_zaHm5-kCwhYedQPF54Aqsnp7S_ZZLsWehAiGrl9Zk4vCT0WdRx5NtAGNt-r4mc9w3YiFWK8u9KDq6Js_eVfGXaZaKNXUY5zfSfNty_dPLR_IjQKU75mV2ZHRoBJ9utBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل تقابل‌های استقلال
🆚
السد در رقابت های آسیایی به‌مناسبت‌بازی‌فرداشب دو تیم در ACL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29714" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Er3F91rYz98hBXqtf8ytaDBbcNi5l0JQcJvYOUA9Ej1Ad_9npMKT9ravkzs1LSlbNS6RXNmyXsBD21CnOvSKiddMWGFlmtr6PXVoYsSoLDfm5-mDgY1S4v9TPAca_jFhMv_-pksm9OY1owshGALxZ78Q3NRutIEIwQ6lGngZAV4Axroqu6hzoWpMzglGhUnpowtXIB_U6jzL5cl9d4xTVeOwtkqs8sQnLM85U1samhgtrjFFU0e0omkY286-7ZFEDbfabmJrO6ekdedZHyckBOMeJOqdGtrMq7MWj0HJOatyDw32_yGIB60WD_7NE2A25aVT3EBsdgIAqO-W7_O3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام مدیرسامانه هوشمند سوخت؛ خودروهای صفر "نو" بالای یه‌میلیاردتومان فقط میتونن از بنزین 10 هزارتومانی‌استفاده‌کنند و سهمیه بنزین 1500 و 3000 تومانی براشون حذف شده. حالا سوال اینجا ماشین صفر زیر یک تومن چی مونده اصلا؟!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29713" target="_blank">📅 01:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29710">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF-1cxWhVugUpH6Cvl_TKAWd0P9Z1OI1CCnArck7Eww920OL054CmpH99n5dPQ1BLYjPIgATaBvggLc_6EtxYp9-BlYgGsY58E5WotO10_GibyQQGXQvXS98-bwa3c672GmmAbvF9oF2Sy3dJjdQc8jcT4cObi90B73gB27ngVvqmBofxRofOoHo2xS4FmR9wxAVLoDcpZBxQuPLb9JEVMi4R7fQ424UTuOaNmXuorOxcDv01wBjmJpJ1o2mjAkVbLH8VIPYTRMJc4zXjusr8_MLleWq7WgIieclgAMPTScX0pl-YPtqjerqX1nNnKG7sFrnedwXIfgtpyf-mt_3oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29710" target="_blank">📅 00:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-tk4o3fTZOA3qeq3XgXe1hycvIpY3Ijb9pMaTUFRThbLXTSiM2BKSKjVYnIW16mLh9P5A0JYxS3f_g_fx6tnSt3uW5g9OKPHVCaYpaVEPFaALdNFSAKMaFBqnTp45YaQy-4q2fCmJhvtmrdDFyIChVenUv-9Qj0NmzMchvMcFTXdak4RzR7bVwKBj-McKQD2aKla9lYmfnOdpZhsVLbeuiUtanOlT2zUyNHkFR6t4g-W4RPQRLM0y6Ho9b4f8Z7JNZnlr6H0O8wICKpIH23HCcPXF5la9vSYKLVkTL1WwGFeCWJ-Y1-jnJXUkJRscZneqJ04p0xJRr82IkXGKTCkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29709" target="_blank">📅 00:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCXaUYh4YYiidswSZcqrXivRE6Dw5J6QvQkIROW54JXHP_oz4xuHhWXvOsZE5-wViJkKo_CFTxHSbsGz8BMd8GAn5fF33nnlKfXYwO2qxlxhN6F4UUh2oT4kieAXK9orP0xERO6HjqnG6eJRQiEZOyFhPS7jIfv6q_RmgMrsGawHkBV_g4t8Y3CLkNeF71L7W-TpeGDUwuZBKsHa3U-Qh-IBvnICA1iAj-bYGGs-Dm4SCa_KItrL2scJqDbFnPkBk_K6-Q_TVeSzdhXwWn3KvYShqc1V-V6HCh-plfkjpMS2AR5OVNxYkA1gdqlgtfZ0In-yarYouYHEYowjO37bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29708" target="_blank">📅 00:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyqSRM677olpPoCZ64wVwbM1kn3p5ZJoVNDRJR9wJw11zjnPnSYo3ormSU4rhY9ME-6siPKgAOyYjX-EXhlXHrk7W0Q412brMmxTiEe1ErFSnQ42NOlhxdtmL-LIJS4sl1Q7A7hBsQP1zkNe-A-5So4KGN874hfDj-dhOpgleD5gysAhq0ZFzJ3_MTch7Vg7lmbPaDq8rrWhD7L-m2HpUnt4EWgCOku3noX7-umDKTGEmnLBTUE5E3MMZwVdY-L0QWdl5GYGWVwA-lq860zIEBmVY_bRaJMt2950XgZT_8RQb6eqWqPELTPZuZICd-PMo9D4PH2gXYKL8yz1EBR8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هفته‌هفتم‌لیگ‌عراق
؛ امشب هم تیم علیمنصوریان دو بر صفر بازی دو واگذارکرد هم تیم دهوک که تحت هدایت یحیی گلمحمدی سه بر دو شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29707" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29705">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r92JeLT3fWfiRZMGfHAHPyaNBlVIDdUC2sLzqV9_xZwSwOSCmUJ96TwO42bHkIg6bc1nB3I4s0nNJWQRn_dsQQWNhKX_NMeAMmLI8gUmrZIfagk1vGFVbehu6hzA6WtXUQzwkyK2qytxGCCGj9bII5XNeAWMUeEla1d344zeGw4BuGgQYRTfDUL0zOyTxakc96i5ZEvyNNVZotG80Y5-TVXFQIG6cggBASXFbGNI13Jcx-uqraZ-vUeq5Hq-2cuM2STn8FzBinFwnTNndQNyBzzXMvRkhoHoKdKT9gRkkoC28cWvUPltYlpVELz087i2INM2ZRWJ1NcyzdB_TftC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p4YDPorsnxTu4XtZCB4FpQjL3yW4ggYOA_6JjKPyG5oliOkmWqTPd9Ry5O3bIDk8GujL91XvDyUPuYYIU5h84MDqXwGZf_BguIlcvap7tOibuiTBJOcCG34KR1fhMIF7O8WfUyp7dGiBIG-m1aGKgXlIH5-lOCqQOydpGhJlgVV6SsTvzTinKw3yd-wCxd0h9T0h0UJyn2Re2anMpQXh8mx_aMoJVQycrSceCQYJ7VsOEB5Fp5dZL12gj2g3rvA_FG_H8LLZgyADRQo4T3fecrAvOmstgk_LIY6OELk1GeEWgGgyuWFMguqEV45tJ4OKQZa8fRKv_JHkYsA0vBWw7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29705" target="_blank">📅 23:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29704">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp7vBLg3jJ2zgl3cc0A1dBISt1UMK0OSTFKBs5Q82TOdC7Tb-nae7tsgD4RFj7HLgLBpwdnnnzrk9lAag_1MNzcntWOVFm9U5GQLNioFzepmY4JBak0hqZdjQW3mmXbvwoEAwo4Q28SJbtjC8SLN6s6n_Rr0qu0feu4O7M90MN3H3uQus_QLt2xGqt3_1H7jEfGJ6pu4rxDal62qR9ZmzMHLhuiJ6XYvbjmT8EmCNZg0dlbNRqyyzXMROx5p8JCwSeLCvSa46Fqy4O3d1fUGglQuaRwF_UfZnW7Rho9HaGfilKZdl3Sujdtzh30zFHeFeX9MgaoFnf3whha9LVfSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌ چهارم لیگ جزیزه؛ آرسنال میکل آرتتا با دوگل دیدنی گیمارش و ساکاساندرلند رو شکست داد و باچهارپیروزی‌پیاپی صدرنشینی‌اش رو تثبیت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29704" target="_blank">📅 23:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29703">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmPTl3u6lnMrD6yPr_bPuFzmG22GiMMxwkhp_CS04n1s-Blk0Y7aJkWSI0RL_FaBkvjcjiTzmYioSKcpPkCq8gONUX1NTE7a9mN107RxnQ2zHZLu-VuS2qQQ5Ds9FGuNsuAO9HBUKoExQuW0ApaB1uAtDHjxdPc74yOPThJNpQlDZE6vcWRzBTd12GLKU-6N9aB9Vmze48glGpyOkvF3AERo0PHfkI_3Ql3ejFgeAeVPvr4WPMX5BhFEqB0mDH20jD_WrY699NXmimTuJXvt10I-3q0Vmq41iC86Pb8G_R8aUkUYZDiFuN7RL5czYT3BKX549spb83NZNOhvzu8CGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29703" target="_blank">📅 23:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29702">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DkM7GYEy7Sx8E07L0n_6y-VUccbcpAMDY1vhLxAIu-jlnuwucvIWC5BHgauNoU1axkQ4CGl5cIxEkxzScGJxm0Wuh-k49JZ-JV4jwzWqIus7MtZuIkMcuzqg2fKHzCD3HAOf4_XRvsvPY7vSBWkWTzzw8hVlCKWD0SusJHzf3Ok7CWF32mpF-uHPcNdKUikthFLiMDI5sNzr1f4hrotac38cfIDmSgEyqC6JF-tNATuhgvkZSx2Hi9XbiSQiWcynBuLTr53_8wdblQkmXYCA4iQxcc03BUTV-FQqObgwP0ho2r53T6OVEsROpupIwUt3-PJpo55kLccUuztPgCRYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780ec53923.mp4?token=DkM7GYEy7Sx8E07L0n_6y-VUccbcpAMDY1vhLxAIu-jlnuwucvIWC5BHgauNoU1axkQ4CGl5cIxEkxzScGJxm0Wuh-k49JZ-JV4jwzWqIus7MtZuIkMcuzqg2fKHzCD3HAOf4_XRvsvPY7vSBWkWTzzw8hVlCKWD0SusJHzf3Ok7CWF32mpF-uHPcNdKUikthFLiMDI5sNzr1f4hrotac38cfIDmSgEyqC6JF-tNATuhgvkZSx2Hi9XbiSQiWcynBuLTr53_8wdblQkmXYCA4iQxcc03BUTV-FQqObgwP0ho2r53T6OVEsROpupIwUt3-PJpo55kLccUuztPgCRYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29702" target="_blank">📅 22:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29701">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeBpkdP8_EQnPYdv9JdURzgRRIjov4MfTzcbYzmEX5vmsdD_8SPXaVOTxKpJd6UAEX9r_ycPLEj4Ni443I-7Tw6MaH9rwEpgC2UVwmiOa6g7-y6kYuKj02CWhbHbT7PuSDvrRlf6N90nQAInOO49lN2pi--SWTBxU1McIt5JnLFYW8qPHWWJmHmsoZgU3MdOlXhsCP3cwEcK0QdEObebXnF_YlDYBcJ2g0b0G7SMt2yOYydFUNGXpqqmZS1ADWhXliDivGShFD5W-thDn_Df4422LUEXC6k560DGYTPv_g4xT1oPuz0zDGaQz4Pptq84FlsI3osCyCmPVHfVcjuEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امروز عکاس‌ها دوتا شات جنجالی از لئونور ملکه آینده کشور اسپانیا درکنار شش پسر منتشر کردند که جنجال‌زیادی دررسانه‌های اسپانیایی به‌پا کرده است. عکسا یخورده مثبت 18 بودن تو کانال دو گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29701" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29700">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=c6mhuXgcwGR2YSGpvd0SJ9Rwq9CSBzQuD_3hycYfOgUAGvgBwQ-oiCoUITDd2XWk_gdH-dkFSuaTRx_Vvi677kkzb4zThWKi23O4YbHhecKGWiyZp4_xme28XscJIWFxLLyCDHmFVVJlH48dagtNYeI1Hgf5h9FiaOxZmJAtzDlDX9n2Vh0GdTRf7v3Zr9ma3sMPNdpGQYFLCWgYzR5pQx_RCH4VIdtxW4cpPVg5UirOt102_MtgyyWbSE7YbPig-Rh5fnutX0_x72kcUMnh9f_xgDyxdgoRQvHvS1bSlaUKQQt6pWXzlC8zzeO4xBXSQdSvpM7XSCXMyG-nPfe8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eb0365ee.mp4?token=c6mhuXgcwGR2YSGpvd0SJ9Rwq9CSBzQuD_3hycYfOgUAGvgBwQ-oiCoUITDd2XWk_gdH-dkFSuaTRx_Vvi677kkzb4zThWKi23O4YbHhecKGWiyZp4_xme28XscJIWFxLLyCDHmFVVJlH48dagtNYeI1Hgf5h9FiaOxZmJAtzDlDX9n2Vh0GdTRf7v3Zr9ma3sMPNdpGQYFLCWgYzR5pQx_RCH4VIdtxW4cpPVg5UirOt102_MtgyyWbSE7YbPig-Rh5fnutX0_x72kcUMnh9f_xgDyxdgoRQvHvS1bSlaUKQQt6pWXzlC8zzeO4xBXSQdSvpM7XSCXMyG-nPfe8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29700" target="_blank">📅 21:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29699">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfmQVfDoSB7igDndzKebOEKJ_qhu5IEFmWFkf8HDdG4UD6Eh0ibNyOhvE8asgtSbQOaDnGOQldmFehU8OduAQxJ7B9jGIBaAyuxpCGNQUjDOENs7rwyup7ZNdLE0UncI5p8fp85P3JNPo1eAyeMiPmYBUnucNL9cVleoehO_MFq1p9eev-iF-9P9btcACUdsnIJlTgarV1jkk_ijefWK2lZcrihs64fqjbLY83FDRUZ5MhKq9j2mQBUbLA9PS5R-_zfqArZYKH8kc-Cp9JRcwCpyV2uBRxOTGsKCyBsnEY5H6UH9eO7Ab9_ZOOMwqrgEz-ydNWjHytcTAGdR1w_ZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29699" target="_blank">📅 21:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29698">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcgfS8nP-TO5wj3zp1YGiEFVGwz_KFZVqmhO1IoUW9DiwqSrVBwCklDZRXZp0QFWW_jodXx-pBLrkX-0SlEYtLLgkYsWP1FchzkyuAEztAaMZ1G_nICDV4CVJOw5fdZkipdy3KuxM3IEIt-7A8Q2HZIUGrk-7cbVw0ky1HyFgCkDc11yyKtj7Amy5WzTNO--chgWU69y88OjvdOfX89omYHcqEhfxqn3O_p7YoWpnyCIX-_UWNgDLKFyajGk1OdIWB5Ex1xXfnpNh6XhQIB96ZqrrC5_XcxKlqCmbuPzYY75UVud2OHIsXymgNXpJexvHlLodkKYGBPmKAIVi0ZlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی به توپ طلا نزدیک شده.
📊
عملکرد پشم ریزون هری کین در بایرن مونیخ:
98 مسابقه، 100 گل‌زده، 22 پاس گل، نمره 9.5.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29698" target="_blank">📅 21:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29696">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxwqJZTl_BPOERumW1ZaD9UyyXjwIj2ZTMgppHfGJJ78mcIYjEBvbSHtzr4_IAA8SBzVy34EapZVLtFnZ5yUtq7jnsA4PKRiwCcftfnCtKPl-nBLMx_3kfRExT2VyQkvR0Pukhlbe2wqnoJhPfHhcxdhkP9T7QdVwkS5rqHlI5Z3gdT3xpC9xvEyUnGbxMOSlePtEWk9euLFz_NwaGDiVpV_ldvfZ6YOYNfuhg_2IdecOBFmTdCK7ZprdRKnCJOpsbwJfvXxl9-7VLmWVtid4UR4nAsgwA95WA9ggDZyUgzkkwlcx1HubOpWO8_mIRa4PSfqi6TW2nOig3V2N8SzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29696" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29695">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=I8gOFk5DS44kYR2mSpVo1VyQ3eUGsbI8FVGCEzBSGTwNcmqiJPsxrf6ZCwJ_8ag268ZXm7WvDl5e6l5D81e0XgLxpwyfl3x1atr9uGdtAgg3kTUxE5v_by0tyBpLdbkVUU3CJWwNDzLHX41gXcAlbGPBJR3Lwyh7UYei6vV34xqZ-soLJj7w5J6sha6QnP3h0SnOZvaGao8zge5adY5OE1ypikQS7kSQcFLFSknnTFelp40KXsNhAl0MtxpHjtJLrlx_ukMqi9Uh7h1JFZJPbRbTYYtpZtrMzc1byQ3k61VA5f-Z0URWYgFoZXUHctJTdnuCSNdWDFmJ6RCZoSqx0aYaZeGGlSxCbbhib_x80xie4hspCt3okpp0wBnq5JeEf7nKwXCiYajSVU7Vx-_Zn9m5jqNn6pTLa5h-17kr0fFbAVkdbEmyKikR619bfaErm8P9iOVdSSj2TdmtU2c-RHzZ2yfmcnxibmwPxte8t_U-VWsCF21Zcq0BdAW_fOif7EeioRQvW1srb5IKYuptPJTL2KIslMEeVlWmAwTZuZxfGeWad9ltvsTnBibkseIwSZ4FixmZ3YbHMs_fCdXFHqXjZUWKIFinOdvcWio_QM4Bh9IboYWFei6ngCb8IRWgZMUW1P05wYOyN_jaxVBRSMtB9PLXIMWYP7dOL9R5RU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f40791fb.mp4?token=I8gOFk5DS44kYR2mSpVo1VyQ3eUGsbI8FVGCEzBSGTwNcmqiJPsxrf6ZCwJ_8ag268ZXm7WvDl5e6l5D81e0XgLxpwyfl3x1atr9uGdtAgg3kTUxE5v_by0tyBpLdbkVUU3CJWwNDzLHX41gXcAlbGPBJR3Lwyh7UYei6vV34xqZ-soLJj7w5J6sha6QnP3h0SnOZvaGao8zge5adY5OE1ypikQS7kSQcFLFSknnTFelp40KXsNhAl0MtxpHjtJLrlx_ukMqi9Uh7h1JFZJPbRbTYYtpZtrMzc1byQ3k61VA5f-Z0URWYgFoZXUHctJTdnuCSNdWDFmJ6RCZoSqx0aYaZeGGlSxCbbhib_x80xie4hspCt3okpp0wBnq5JeEf7nKwXCiYajSVU7Vx-_Zn9m5jqNn6pTLa5h-17kr0fFbAVkdbEmyKikR619bfaErm8P9iOVdSSj2TdmtU2c-RHzZ2yfmcnxibmwPxte8t_U-VWsCF21Zcq0BdAW_fOif7EeioRQvW1srb5IKYuptPJTL2KIslMEeVlWmAwTZuZxfGeWad9ltvsTnBibkseIwSZ4FixmZ3YbHMs_fCdXFHqXjZUWKIFinOdvcWio_QM4Bh9IboYWFei6ngCb8IRWgZMUW1P05wYOyN_jaxVBRSMtB9PLXIMWYP7dOL9R5RU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29695" target="_blank">📅 20:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29694">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAfvpitj7HE0FU3y61cR8v1vm_2nu6rp-snQF642G-hEZ11zlF6FgGHfkDOCfFNcrwxcrENOGZO0gU3prsVA2PQk2APxNW4jbvQhdIiObmJrUGIqzxoU7q5F13xo0lDePUZZ7umaL1lnjY2DBfbPXrokHCsqfLYTjXSSYZgJ3gJtiI73LhsZpUMgfWTuLW67yRAG3DUqmv8Qt2f6eibEsBkaOyoBmFJGihV3yvJZXqi9CAef5MZ8IRSiH5P18oKKfb9-fvwoQNHezpR9E8ZCZjSKySKNT4YE6ua6iwbxT6HaOASSCZYbK3QwAp_Gd_SR9-2n1ypNkmmapEaPlBhAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29694" target="_blank">📅 20:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29693">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haGGTzpdzqyf58gu0sZCyyDAEeZ5TY8yHD6SES81eGQiqWFoCVRkFDwvHhJ29ydaISV1A4JCAsfIhu0B1s7oEd_F1CF7czIhXhfY75fn8HMDU9NJflHswHLYlDgCjkvcwvlxmxWT8-nxCD3XbKpPs7tJPobi3HmTqVnjBTJBooQJZkCAyotnTt8GJJPcWBlCzanzF7FB0_OfiFAoFF3dyTNlku8TQYNvr3iWV84jzvshbgJ9dehH7suw4mfC71cQGavPERZ2Lijz5STNAxTJKIR13c3tahxs7TUaVOOP8_YyHpq0T6F3X_E4RsKZOq_OLCfxzdHbGPSwWcwUUpT7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی و عجیب اتحادیه موبایل ایران: مردم به‌هیچ‌عنوان‌برای‌خریدموبایل عجله نکنن چون قراره خیلی قیمت موبایل بیاد پایین. صبوری کنید!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29693" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29692">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=o19EsJQsYpO02JdaYnuq3Ows13entNW5L5rIgBGYkLpJUsMkNRczbAuZJ8oQrC7sWPyvYSrTm6QBOX2O_6MeMQe1byvQ_uLsbvMunwp8JMS3HcIGfTMgQdFyaWiAor8IdT6etelm21pNuMyoABBEt3GaVGkAxwMBUMm6xSGVMrbU2brMfuruZIwQOhsn374ZrsVG5FnrgdhVOPruVQDG8LwcfVAAJfq19EuLsYJsaO9TkYjbxG5Milixne3rfnc6HFLCIVlnXk1-TY7qbHLwbsiixJiBiNXbbIYmPpxjfTSpdYVrhgO6amVjrFuIYoJ_znqW_n7LoZdqrTuLNQ9a9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ad168b5f.mp4?token=o19EsJQsYpO02JdaYnuq3Ows13entNW5L5rIgBGYkLpJUsMkNRczbAuZJ8oQrC7sWPyvYSrTm6QBOX2O_6MeMQe1byvQ_uLsbvMunwp8JMS3HcIGfTMgQdFyaWiAor8IdT6etelm21pNuMyoABBEt3GaVGkAxwMBUMm6xSGVMrbU2brMfuruZIwQOhsn374ZrsVG5FnrgdhVOPruVQDG8LwcfVAAJfq19EuLsYJsaO9TkYjbxG5Milixne3rfnc6HFLCIVlnXk1-TY7qbHLwbsiixJiBiNXbbIYmPpxjfTSpdYVrhgO6amVjrFuIYoJ_znqW_n7LoZdqrTuLNQ9a9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29692" target="_blank">📅 20:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29690">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAHUfIdiwnhn67Ke1YqBCc62JAQxL7wzgPdXEWsGBY_izXxdVcnoHypdgajfJbG-fvrnf5fiAjhSobmX9kfsTir70PXkWV6Nl_Pvp1rPOa_ZpcISxihhE8JYMOaaw7uJW53LVPyK6-vh09icPeSNkMtJd_BlrK7nmuA36Sf6_YglLXwCAm1nn46_qUjdVa45y_J6x83liwvLevOtA_nCkq4LR4A9kAzNQglfVba4FxUnNwyYlIEinZLsMHhcb7_wPbCvR440sS9VkUeMahDlScrSqVl0UnXKZbCrx6JPlmiuZ7onR9DoAKnUNHhUFpZNgkcqD4M0GbL42n7baWjhrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
🇪🇸
نشریه ال‌ناسیونال:
فابیان رویز ستاره اسپانیایی30ساله پاریسن‌ژرمن درخط هافبک تبدیل به اصلی ترین و مهم ترین هدف سران تیم بارسلونا در پنجره بعدی‌شده. رویز از یونایتد و چلسی‌نیز افر دریافت‌کرده اماباتوجه به‌رفاقت‌نزدیکی‌که با پدری و رودری داره به احتمال زیاد بارسا رو انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29690" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29689">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8rMKRgP3Ycm7qBr26gI39KrRM1vd22I4bbjlUSEXwYbAEcplwI1nb-R_mcssuAC9-8dIrHuCzqtSie4NYrmCwRkYpjRdhf00WDR8hm7m7uzaKndkPHSxw-mBqsOOqcEi_j2sdZ-lL0PEDpOvWa7oaFeyeigiDRXRQyOau3R3RQNneyTULFeMWxYWh9rN2Tcmu_XgJI1P7a5FxJ9C_PVePxiLX7dRoT6CAoAbMrJvyONoGruWNgaHoqd6oV9C9Cpl0iKhuEsASdTCpqPOElLb_FlOaC3Xs1RNWwiFFlQBD07ELkwqjFn0sNX8XiebvkqueShF89KliAh6pxCM1swEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
در هفته پنجم لالیگا؛ شاگردان فلیک در دیداری خارج از خانه به‌پیروزی‌مهم‌چهار بر دو مقابل لوانته رسید و باپنج‌پیروزی پیاپی در صدر جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29689" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29688">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWsKyLXK-iaZFEM06yOzxdU-bMTBRSHzWwdF1Lk0_U8T8_NNvgh45M3oMV4PXeIb061ljdSI9Ep4vH_GeldKS0fhpnfURuDF7a8wZcKB1klRF37cd7HDhqlIGBNNDJmjDxIKyEGs3LmePyf4CR2RWZrIm2xGn-cT4D8oQFdXCitXaVriUy1iad6779PJL8H68e2ex9Gb9aVg9N5AZiqDS_YTb7KNm_QO1HzZLA-AMP0sOyle6-aSVrzZcZ8zPx61hb5l3pHRJaFVlzOSM9CVH5ZD15aocexyeGbtAx-qIV5MDUkexyBs6ah-R1Yl9QFSb99kGJuXgxFIq_7YfgxEfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29688" target="_blank">📅 19:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29687">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLPs0ADUBEgopMTFFxkcaSFLG55yqDJdLfirgFTs7hRiBiAf9TPgEgCNJfIzFF_Z7MtwvtYFs-wzBuxy5DgetmHYuuRtM05VtcprgmQdRCLA--Rp_BVbhG1sNw_HNvG5tD6rOgG32YiYA7AfuU_JyuQFgUFoBt-V_WRpwOqcfABFZEsNlQKzARpveiL3mhHWQLpCSu1Yfqzcv1vd76bKuN3OwskRxTYBtBNsJscbWg8Z2JCB_DH_O79j7_0d4y1gzQRlq04aQkAv-TkuyYcXbVGXaaAgtzQtTEIfAcMZMF-i3TJMkdCfGeP5VGCB2Jv_kTzlN44YYeScRjMe6wLk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29687" target="_blank">📅 19:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29686">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZQ7ZYvebdk3tUVB3pNEwQ5HplR_8DueOpHl6j3HnA81BevmlH1DoTVZsVKiO0yLBZLCL1xozoD7RXxFFumISH9tV0RK6apecpU3LxPof4YYfNXKgKqM_A9NYfPtOu3VRvIAd5TlrBfqugo8HScgHZFbBmVxKuA74yRqqaGd7GhvNx-23DrZlXmUMnGASoVBGE67cp0iU2Jlgo0xiepy--IufCWs5YijavszJ4K5IlKlJSsYtj4528YG1xwxAyHP5FrF92U4rByHmknmA6U4HCAs17VhbB3wo3ZH3juyA_uXUgRVaUoUKsBuPSp58ENG7-bRe_BI6EQPQ1TG9P2a7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونمایی از کیت استقلال برای رقابت‌های آسیایی و دیدار فرداشب‌برابر السد در هفته اول لیگ نخبگان؛ این‌مسابقه راس ساعت 21:45 برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29686" target="_blank">📅 19:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29685">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhlvbZzkZxml1T9mC8kFnfgpdXLYvhDkfCjpcMrpnINcpCJLjS1D64iiu2a8u1lV2mhLnChbRyLDzuxuRdnYIKZ33m7-KfYj39PwXHFuYiBmYT8w2OJ2EosYhanwlbUztYcFTMt2hwR-WCJCtEk6odJUFbDqqEp95aMqdkkHX4YHxP8OA6eBcuyYONBJcYM2tYmj7SUW9p5KNZrU8IzUy6LUWT0CI2-lBmc7bWZjB3d9NTw0xEG0jcWqQkUov-mI1wyEW8fDghA90iHrbgxFlxCOFndkv58XsvmSGu0OI-0NbRzK8HXUHjb2AKiCd_hht5dviIyt0HvXIRAz3M-KYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29685" target="_blank">📅 19:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29684">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2nHZvkJQmcJdmozXHjStveBpE6kCK-O4cfmCct_6wvIbMP7e-erIL8RE682aOqlaOGouk-MYQ7tORygFVOpWzq0sbdsaPK2Fu-XljswGdYjrDVQ9vgY-Ek9FHudyJtyODHri1QFZCxU2TlWZNt5xbxGaW4Sgqqb_EM58vhJaFQaBUM2YDYSeTfFx7zd1qdNG-E8HFlUbZdfp9v5U5xHgj4loyebVFVkMHhtheW0rgv7PYOvR0GagVVEz2SMM-Ga35a0eo2y4N-YCHFIkea9UnhCCVwRQQiaGh9P9zq-odw1MGMw3uETwZhP8lS5ZxmdOOHgHvcdjCvVKJeHHKcZv8wI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f29263824.mp4?token=ZODIJNPF1IZ_Am6rhMIzQ9Za41fJIFX8X_2rHcReO6L6ytuekdPmQOhN_L5M1KFC3vyuzxeyfhHBPu97FyZZ-oapEDrZpe_pL2C787P3q3M_p2gn9gtDK_b6c6vPxVE0pJiBLf2WyUCrUfVrJr41krF_Y1sGkcTuZv70oE8ocg3m-a4KgCzpkBQrwXpbP2VUy_ewkFaA36QJwWwqV8RWgi0KvFmKDapDFF-bu7X0fUdcVNf6mN27C0-u1SaIdGoGZWETBK1e0QcPci1un4G6wUVirKOjv2ywb7GZ_ybxRTuTLEy_z8KFg6RRkxpuzNZZA3TRzlSSMUR5ZoXdUT7m2nHZvkJQmcJdmozXHjStveBpE6kCK-O4cfmCct_6wvIbMP7e-erIL8RE682aOqlaOGouk-MYQ7tORygFVOpWzq0sbdsaPK2Fu-XljswGdYjrDVQ9vgY-Ek9FHudyJtyODHri1QFZCxU2TlWZNt5xbxGaW4Sgqqb_EM58vhJaFQaBUM2YDYSeTfFx7zd1qdNG-E8HFlUbZdfp9v5U5xHgj4loyebVFVkMHhtheW0rgv7PYOvR0GagVVEz2SMM-Ga35a0eo2y4N-YCHFIkea9UnhCCVwRQQiaGh9P9zq-odw1MGMw3uETwZhP8lS5ZxmdOOHgHvcdjCvVKJeHHKcZv8wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو آنالیز دقیق عملکرد شاگردان سهراب بختیاری زاده دربازی هفته اخیر آبی‌ها مقابل پیکان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29684" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29683">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=dOA5Mw1JHGoNjnt4dGg4Q_01bNYzQ1mf6TZraFfhazC3JKvM3Sc1HTkQnUup_V8laf3Cu25UOvUmgt9R9xAfMZousNCpOZ7qua1TyCYTSETvQopI0l7C5xO6OohKZZLrG4uc0Dhn1EN_-mJRsNgeOksJDsNEzrvDf7wmgsqtOcYSqkjHb4CXCovW4fpPJINg-E4i67QX85KIFkaFKtRiffdrFXzTg7JRs50MEkxaqLeQDppSRfeNnJbXYyPa7KpQNorwfeN8MsJuWAuxw2d3vb19-9rMloArTbYUm58hl70O6S4M3qagdRt7xgplVbsyo1TDKBqHMJl9oavLZdl57A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961ce8dd07.mp4?token=dOA5Mw1JHGoNjnt4dGg4Q_01bNYzQ1mf6TZraFfhazC3JKvM3Sc1HTkQnUup_V8laf3Cu25UOvUmgt9R9xAfMZousNCpOZ7qua1TyCYTSETvQopI0l7C5xO6OohKZZLrG4uc0Dhn1EN_-mJRsNgeOksJDsNEzrvDf7wmgsqtOcYSqkjHb4CXCovW4fpPJINg-E4i67QX85KIFkaFKtRiffdrFXzTg7JRs50MEkxaqLeQDppSRfeNnJbXYyPa7KpQNorwfeN8MsJuWAuxw2d3vb19-9rMloArTbYUm58hl70O6S4M3qagdRt7xgplVbsyo1TDKBqHMJl9oavLZdl57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته چهارم لیگ جزیزه؛ شماتیک ترکیب دو تیم منچستریونایتد
🆚
منچسترسیتی؛ 19:00.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29683" target="_blank">📅 18:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29682">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9HHSII3O9jDelkkS4-zECvZW8qMxhn6PjJUQHsENyBB4BG3t5ktQ-8SXRC_XfMrIrdzYubNyObEwTctseNMpWlwtvErI6y2HCT9jVFFAQ_2cvtrTZ5JmgKxWf3mv_7G6nDbEYepyOfum0fQRhkjQfYP7ZKJWQORT16DcraBhBmg__8LK-L6wJzrrgef0rDukape4FIrVAwUFX_Fo8TletAhn175mIufLg78rzlY9CTkUPcOcbm9MaPlri0k6Ofl2Mdn6yUcgkbWsxml8z235mjSe9aV3F-oTe9Qt35IyUNGAWe7EfwM9KxmnNdo8aifmWrMbxSq0M9IMC3iwsf_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم
؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29682" target="_blank">📅 18:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29680">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lL09cw481lRa8zJZIiGa8-undSnAi9OQjbofMz8uI7ImFiuUbwezkBc6RqiyMJP6kZEIV0wnjGHq2Hw4ifVd8MaizDldKHQxAAjE7g7dOUlkYJe6YRzG04d1sX9rbRCACFSlPZhkYdjiiaaAgDb8EHoObWs6W8pNqg6qB0JarbxAa7g2dUhyyccBA1PkEBMxtYr1B0I4I8uzA021iXl2oPbcYpb7dUOWVXlD-o30-m3JTgawJPQMLyhagOvQsNiVhOpelhipeSZ7MTXtmNyDvz19uMtrGWz3sCKG4FwPpVi9u6iKhwBjjfCEpOO-d0HF_BDjycZ6VbuExo6IHz3N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgThDm3ZY5j9w_61TmLuINBkxKdUsfjTJn4X_Ek_q34h7NPfvoXHJrIV7ZM6MynpicRfhUvL5F0XzDtOsSRPy8JUGuztcn3swwSl9rmZCu54RvOKHMCTNECowlsPoaLVf-zmCFc-DzRAV2_6F8ZhK4BysvOOsbhrn0mNSCoScmj5MnJ8wTPVI82pc-eDiSX34_rmJleYSxSiHY6zm9JtAxiUVIV-HZFVJXJyTwnujwLOneS6-58pfkcnVndLa572xmES0-JuHzTypASiHWCWoUpA-l8FCiRpdnMUkETHOuYvtF0FuHI8nZVoNy1pP5xvKG2Nqp0iXpW8FSQZRRS9Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به بهانه بازی حساس امشب دربی شهر منچستر؛ نگاهی بیندازیم‌به‌افتخارات من یونایتد و من سیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29680" target="_blank">📅 17:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29679">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUgw_57YI3DMKV9fHiM4x0jTUqsNRjoGAGtqFgpKRsU7tm7ab2Qryp91_Y4YKI642YYAU8_rpsyfAlXJz-gJL_xXJTqdpdtYsfsKr5PyLbTWLgtnXDfSVe29kgEzkJ3yBrWft8v3Nk76DtnMWq0EKakfv-8AeGInSORdLXL0pEkkW3BBN29c8FQwOjQh9hHTs8aNyGfUj3QS2OxYvOWX6iewyNa_sTaw9pQ3VCuTBuGkuAzi5zSDvkV83X76yvsy0c_mwmD0EOPhOI5M4BXarg8g_ul3oWnZmcje91Wq9N2C_ibCkzc5ky-UaK8PZfFK2baqL_MmjySZP9QW4tVMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رادان: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29679" target="_blank">📅 17:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29678">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=kbYVr0bZpz2O1jM3_EIgKuvM5XEgURY2iVLOv16yssp62g2orQ0_rYcbi-5sb-9-XsGeugw3X0l38-_RRXLhQo7g35yY-7DRP1lZ_Pv4KxCP77zvIJJag2VZdLCl23tqN1CzvY_UNzAbIU0lTrH3JOR7c7KJw2wnl3OUo91N8ORUIgG6W4LNi0mtHVlAcbhN0imZ9qwj9cL32Ugagk9r_0mD_KcC-g4ezwNr-y_iCuY1V80-1ONv2F3ktulLEQX2Y93Lr7IbjeAekeacurgO13j5txdfLnW7oHpuQJfJvbsc4jp9opSo_1QoTjSuh0WxNUj8kFhKgMTOinsAtDBOMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=kbYVr0bZpz2O1jM3_EIgKuvM5XEgURY2iVLOv16yssp62g2orQ0_rYcbi-5sb-9-XsGeugw3X0l38-_RRXLhQo7g35yY-7DRP1lZ_Pv4KxCP77zvIJJag2VZdLCl23tqN1CzvY_UNzAbIU0lTrH3JOR7c7KJw2wnl3OUo91N8ORUIgG6W4LNi0mtHVlAcbhN0imZ9qwj9cL32Ugagk9r_0mD_KcC-g4ezwNr-y_iCuY1V80-1ONv2F3ktulLEQX2Y93Lr7IbjeAekeacurgO13j5txdfLnW7oHpuQJfJvbsc4jp9opSo_1QoTjSuh0WxNUj8kFhKgMTOinsAtDBOMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رادان
: بیرانوند شامل‌قانون‌سربازقهرمان نمیشود. دروازه‌بان‌تراکتور ازاول‌مهر سرباز است و باید یکی از تیمای ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29678" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29677">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=VZU1usg9D2PdO7JFzb4UObmSdcFVq2n9l304XnP50WfhUNEwNrEhK0_Z3e1H70UCiY7Qblg8LybOZ55Ky4d2PWe_aTK9fanpPimVqu0-8I-bRcBKbzxzhqxZzymsg_zqHRvgHDjjat3MTSnzYasLPYRQDoJKWXY8tCtLW_fiVhJO0CARhnWxIdr_VT7I2a187gwO6Xqaj0woiZzQ8VS4Cn-mfOMNEKiUxC7zdSusUzF3c62qZLq9pVtoTFgkCswP0TKpmbgxv7ReFaCm34G8Qx_k39lotYbgPPOwZETjsliCMnQgpoyPPM0-Oh4m6q1rKFEhCHRpu0iNtb2mu4Abqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=VZU1usg9D2PdO7JFzb4UObmSdcFVq2n9l304XnP50WfhUNEwNrEhK0_Z3e1H70UCiY7Qblg8LybOZ55Ky4d2PWe_aTK9fanpPimVqu0-8I-bRcBKbzxzhqxZzymsg_zqHRvgHDjjat3MTSnzYasLPYRQDoJKWXY8tCtLW_fiVhJO0CARhnWxIdr_VT7I2a187gwO6Xqaj0woiZzQ8VS4Cn-mfOMNEKiUxC7zdSusUzF3c62qZLq9pVtoTFgkCswP0TKpmbgxv7ReFaCm34G8Qx_k39lotYbgPPOwZETjsliCMnQgpoyPPM0-Oh4m6q1rKFEhCHRpu0iNtb2mu4Abqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29677" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29676">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOkp1qsVVmDSk5iboIWIb1qnaDsWQO5UjWLwGE4NggN3PUdv3rnjPsYrHTTcR4Nsp4OzD4NwahPaC_s2Rk9cqyj5ANaY34IMgEI598qhBi9GlzDK8QwQHz1VORfaC3wsnYMtECfimnDgvbFyietCWqS5E_U7ZicGHxh9P1G3nTX8g7ZxFVj14Nl_pvTUdfICtNBVTqQmCTvK3DmLUm65HQF1EqKfCqW3TczKq0IhguJpbxgQVT0nIo4Z0po1KcIfE5CrYl-9MOB88_2x81kBd_z6QPzyPvtBrnSgXekJswadn_HM0P8m-k0fM5ilaKmZcqLktdJWsICeoZda_Gdakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29676" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29675">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
برنده شدن جایزه 15 هزار دلاری یک مسابقه در امریکا توسط این دخترورزشگاه؛ یه مدت صداوسیما هم کپی همین برنامه ساخته بود که بازخورد نگرفت. هیجان مسابقه بالا بود حتما ببینید از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29675" target="_blank">📅 17:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29673">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-qyqCK3seKEiq3KFNVm9UQnuoGS4af0nuR-lIZuFM1FiOJAaRyftLVb_94LXTpIdcQxcLuXhZldPRanCJLie2gLh-y6lZFwiYUoO7bAeWFZFfl4_trAKZPdPe2FwiO0lPv83EoIWlz5GNvPbFKVFVvrIglIZnZtFXNxhOx0SODEFdRSH2Daw_RwXyJPZQ38ITYaak68c3c6SAq1C9rZRUqXZbBi1bADuaEKsxCYiRjixTfbF0lGUIqFJ1ng1zcnSZIp9_t8NTNQxEL_0ukdENmGSSVIpTBRcvJ7E_RccahmuZfxU1dVZJlQ_G3hDXy3EvTKk3ix0OKENJoeceQXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب بارسلونا برای دیدار مقابل لوانته؛ ساعت 17:45 از شبکه پرشیانا.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29673" target="_blank">📅 16:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29672">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjuBWMm-4rl-Locp-EwbhOQGIOsi_HUmI2_z6h7inB5LUQE1DIropgX7YTyn-9UHHlpPqJv-kD6guxR6H1clv1g_pAdOwf9FEXAEAyxaxbaKIt93EBN7l-16MoyoYk7VHvcb-z8IpJrkcXpJ7lz9TgKx8UWMWzxJze2aEKw1CBfZXUme85R3aNVveWpppYdp8AaJcaSxOZX-8krQj4vaQPY0ZBndyID8GSb84UWJFIJf5btxc7MK3LhPRaCkoqgL2nWDIBoy_-Pu-93LP4zUhlL9astTb_jkAlhThsJFp47OhcTKSy58RHvz6GpICpw_scCxuo5ly4HA9vSJjk4cLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت بازی فردا استقلال مقابل السد؛ نگاهی به تقابل‌های آبی‌های پایتخت مقابل نمایندگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29672" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29671">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570942af95.mp4?token=rh_w9JrogPLbiMK2kNNy5iioOy3ITur2DVGzKeMOkbiqLOWKfVEBmGIeE2ccJNbco5nYoSjHRU4zKQpPFaosoaQRLn83I_YDJvJ_Zhg4fz7LzVyx2vfGwgasWb_KaDXQdKUGWushbvmcztYpQ2bCQNZ3oDcz9-0M58k5zl6DzAvbpaETh3THMxc1a7J-vjVr5yBWq7c16-x5uvvNk4TbF7S1n0Zs7Z_49M3ZZUAJ7blfry-gP4PIGH85GIDZt2TgaMjJYm_SatQ1F9KR3jt1Z7H-y6OXO7icUbgpAE9RKU_zyv2ghvuaM81iJNfuDx3Zs2KdKkdAUnJg8K97Gi-s_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570942af95.mp4?token=rh_w9JrogPLbiMK2kNNy5iioOy3ITur2DVGzKeMOkbiqLOWKfVEBmGIeE2ccJNbco5nYoSjHRU4zKQpPFaosoaQRLn83I_YDJvJ_Zhg4fz7LzVyx2vfGwgasWb_KaDXQdKUGWushbvmcztYpQ2bCQNZ3oDcz9-0M58k5zl6DzAvbpaETh3THMxc1a7J-vjVr5yBWq7c16-x5uvvNk4TbF7S1n0Zs7Z_49M3ZZUAJ7blfry-gP4PIGH85GIDZt2TgaMjJYm_SatQ1F9KR3jt1Z7H-y6OXO7icUbgpAE9RKU_zyv2ghvuaM81iJNfuDx3Zs2KdKkdAUnJg8K97Gi-s_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گفته میشود قیمت پلی استیشن شش که درابتدای‌سال2027میلادی رونمایی خواهدشد یه چیزی بین 1400 الی 1600 هزار دلار خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29671" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29670">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov_L7eeFuWs7kllG1By83fueTcXvmlw_shV4bO8xS-xrlFMxb_q7U8O2uGzrBRT9wVMF71xGaSvXaKTz6SKhrquViXyI6E_rfjNhNxTrQcM0BuJIBQh6uDcxgav2w0ylIxMnhEUYS1eDCCMCc561q2eOLYcHARZdXsOzZFrkDV8khREnr__dyz8n4_kflRDS9wzRJC-85EYM0Ap6-O00lAioXa95XGIVqjH-8XqSREJuCrMP7l1t9YGa7mADKUEopgaU0VaBvVIGwa-Yyk6jOAkb5ivmuqzyzAB5fsuJhiYMnavotFKQDMydbBJSda2P91XI0k-ggcxZDd6sndVQdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌قهرمانی‌آسیا؛ شاگردان روبرتو پیاتزا سه بر صفر از ژاپن شکست خوردند و قهرمانی ارزشمند این رقابت‌هارو و کسب سهمیه المپیک رو از دست دادند. یه زمانی همین ژاپن آرزوش بود یه ست از ما ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29670" target="_blank">📅 15:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29669">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doMwlJwcWRFTy2ZVsW59lq0KUdbZFmRp3_FD3GqZTPIpBZaudrQKTAgwj3mibWogcZHswIujelhMrNgDHjKMtbhe4NrgHqrni_9aqKE-W6pdMZmDQcPUJnaf98n2qxFbzOjDBG-xP5ueg4bta3x7ETAs8NcK9nxFFEtHeYtXRqa0sCOU5xakFzaLmUWoQPtjyKzilFxzvW-4NGMSwGL3FPNjXzjIZa7GdjR5zxOS8--2ftpVUjYex0OW6FkWmxUc8G5oixSHm3oTt2qZEjuAkssY5ikyax0pV1NetlV_51XebaprIY13b2UVzy8GDjMyEvDaY9gFKyNvAuBBix_vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های منچستر یونایتد
🆚
منچستر سیتی درلیگ‌جزیره؛ شیاطین سرخ با اختلاف برترند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29669" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29668">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Jofd-XgchBjcvVpjYLp2QSz6px7P2HSQpXtAeibYdiREcJHjbtgHlRJnSFHeAFgXAr1mBRVDU1-qVzVHRQSUNFFx0h3YcGBgeSoPe5ZwKpuU31xY1YYxRPRKNZWlVtzZU_iaW0j2mTUug8Pq8K43getxEGE9bQYj7ADt6aN8gsf1xxPzFNxB3weciqbjXT7cILPEjIOUsuuIRkcmUSFeYL1WkosCSCR5rF5o5nWbDoHG_F0nUQCGDkTZVMNWcCDMUXSTGiD2Gjx-Cqih_dyaD0I23XWnBmnaNZfj8IifjFIhK1bJ8Bvh3MIZAa4qLYbW0ZbWGdRi-Sw9fSV8KXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمتراز یساعت‌تاشروع دیدار فوق‌العاده حساس دو تیم ملی والیبال ایران و ژاپن در فینال جام‌ ملت های آسیا 2027؛ نتایج تقابل‌های دو تیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29668" target="_blank">📅 15:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29667">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=b3mF0lHxd4rAye5i4SImIUiRdiV68nWVEFHPfS_uTQzCqeoGN5YokJLSyjb2g0RMdjUJuX1S8Yr_9GdMzE0BlRe9naMTQ3uNuSFaYFrSZxDL1Ai3PmW84rqB2mtkKCHWwKlbYpal4Ulr232eli6fF3CKBVKodjsQcNno0yygYGXZeh41WQCXfFiuWoPHuujBiSFdXd5uumOv6kFp3cH5eFHuguKX-AnNYOC0ju7rl8csTW4YAWtiFq8xwu_2iR2nv2kmA_UwkbBID-XfezXBsGTtGOKA5wWoob2utVRrAphEunKu1qiPlUh1ZIj2x1SK4QXMEOn-SQRkGR2vIQNHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f478bf5a4.mp4?token=b3mF0lHxd4rAye5i4SImIUiRdiV68nWVEFHPfS_uTQzCqeoGN5YokJLSyjb2g0RMdjUJuX1S8Yr_9GdMzE0BlRe9naMTQ3uNuSFaYFrSZxDL1Ai3PmW84rqB2mtkKCHWwKlbYpal4Ulr232eli6fF3CKBVKodjsQcNno0yygYGXZeh41WQCXfFiuWoPHuujBiSFdXd5uumOv6kFp3cH5eFHuguKX-AnNYOC0ju7rl8csTW4YAWtiFq8xwu_2iR2nv2kmA_UwkbBID-XfezXBsGTtGOKA5wWoob2utVRrAphEunKu1qiPlUh1ZIj2x1SK4QXMEOn-SQRkGR2vIQNHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعداز کامنت‌های‌پرشماری‌که زیر پیج السد درباره غیرقانونی‌بودن یاسر آسانی در ترکیب استقلال زدند این باشگاه کامنت‌های اکثر پست‌هاش رو بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29667" target="_blank">📅 15:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29665">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=dAUTIuOJ4H52ZJKtgxFOD1DU6sA8zJgR_JuJKdl8-tx3Ay5zKbgqfKMTyWbHV3-BZlZeAXMvEsUWypVl1ojfoq0JpuZfcLF5lA14ex4GG-PK2KjplTQggCJTpmZcjuIbtyMbPAtaBacObsDJkeYstGGuAHl4yKyTA3OLSGwyKib7kMcujcysJxN5MfLpjoKVWYCPZyekrlnXVoBn_y_D40Lc2YPBmN6on0smEWv_w_0LFNX43tqPoCMvH-m5YtP6DPaC0FzBHEYjffio053l4Lx3d98ubyWLUaLyhq6gR24vuVGxSt8EW-nX9es8xXcctMCa9bCJV-dE9NsYmPWoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2b549c3d.mp4?token=dAUTIuOJ4H52ZJKtgxFOD1DU6sA8zJgR_JuJKdl8-tx3Ay5zKbgqfKMTyWbHV3-BZlZeAXMvEsUWypVl1ojfoq0JpuZfcLF5lA14ex4GG-PK2KjplTQggCJTpmZcjuIbtyMbPAtaBacObsDJkeYstGGuAHl4yKyTA3OLSGwyKib7kMcujcysJxN5MfLpjoKVWYCPZyekrlnXVoBn_y_D40Lc2YPBmN6on0smEWv_w_0LFNX43tqPoCMvH-m5YtP6DPaC0FzBHEYjffio053l4Lx3d98ubyWLUaLyhq6gR24vuVGxSt8EW-nX9es8xXcctMCa9bCJV-dE9NsYmPWoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو با این حرکت که میبینید داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29665" target="_blank">📅 14:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29664">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmUZX-Lwljh2oHSuTqfS3J7tq6euto-pUJQUII4VavI_1dWhke7F2eOACnEFvASaE6kdKuzaoQVmBh82omfO-D1WngrDFUWW2hA6mCwue5lr5vv1yiKh33FPipu--DPgYWjO_TqfWpMjju0F9GEEd8CoT95_1OUEzO3csT2QesqbzsDmbNMGO20Ka7iGKIYR_mIhHW9wQZyxEAWwEBI3iXLC7NbW1QFKyo_zIf6RfwBVawjm5MGx9ZjndvM62cEJpwV11h8-IBWGSJvJ1Oa4VKXl0cNcniDj7MbNKL-T8MgnYp9HRT3hGsYR7kcDV8kuNTdnBaEC3gnZcFFpVnR2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب گویا صداوسیما بهش برخورده که مسعود پزشکیان گفته بود تلویزیون دیگه ارزش نگاه کردن نداره و قراره‌که‌از فرداشب‌مجموعه جدید و جذاب امپراطور دریا هرشب‌ساعت 19:00 از شبکه تماشا پخش کنه. بعدش هم قراره جومونگ پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29664" target="_blank">📅 14:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29663">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUfllqQNMD81BHR9Vm5N3ZcA1kx-XQp9X6m37GLdYrzfUYTgcFhe_Q3PFBWmHMA4tR68HgWioctVeeQrqo0tCnQ_R1cv-Rh5kcN0fRXa7s7C5THPswItEvb6Ns0H07WNyfDuyfRB_e8TXu90bTcskFV4kxYybwCiQ3-gS_MDLOTvq70tRWVW_d2v90MWDcCui4B9SbtQUZ52pIrLNzAoetMdYfBfBY6qm1iY3pbNBa15XCOTHN5SiJpOS5EzeLWNdJry0RoCZ3Arx4oL7u6WMhlfcyi_Xn08NFdmIe0vGwphzxWyH5MLIBPAIB8HTlTQ-AW4iRwvbMLQLdzv3Iu6VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برای خرید آیفون 18 پرومکس در هر کشور چند ساعت کار لازمه؟! خودتون لیست‌رو میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29663" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29662">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdCMcS0WUsq5iakcQrcAY6LOe3c5am7ywXqsdZaKuvbnMmK8__giSM8tZPtLGqYsX3h-xp6wDbQrkYFH_hMkeMoE-JGvCA2uDxCNNmXINOnHzPD-yu1uOSk2INPKZ1BApCmcf_mm-NRu9Jhfvx80m-_J44RAg4aFXheQbjoRRt30LyZ3Pq4OtNJGaXjqaMxrY2DuF8ALGKBpnoMUpz5Sg4oK7j4SAfGCiymzCPGiHOyglXoz87YkeCJqmBS7X5muZTbm9TqhaHglLM8MVAUP-7hFdbf7vSD1Jr6s5r4z1MA8a6X6c8Mowdd-ANYZN0feyrhMVMkH1L_8ZrPSz3IsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعد از توافق برای تمدید قرارداد آردا گولر؛ باشگاه رئال طی‌روزهای‌آینده‌برای تمدید قرارداد جود بلینگهام تاسال 2032 با او و نماینده‌اش جلسه برگزار میکنه و به‌احتمال‌زیاد توافق نهایی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29662" target="_blank">📅 13:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29661">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A47a4QHCHZ4XgmfikQahcK_J3bMLthr7Cd8sEGCcr0K8S6wEZtnu71XILk9hcFgZjPj8BV6OepKj3kIkezfKxfbjjgdW84IJQ3UKm4yEREYu3Ri06ztRt3HLMai9IdMBXVEpTU_JbJKWUpHeL-iYNvn7ONxOQxlWwcxrR4ni90QSvBsmYt-U1Bq6mbHLIl8nPvBlt9DKIBbxXGhUGp-v5xTNlVuBJzdekGkRQE9D_R0CZBsDN8nkCQq2Yg6hDkV_JPh503YDXfXUe5Vdj4dIZjUyWZrw1WqwyX3vo-Xr0WPlzL_fJZuLYlW_VGHfwzpy2Ov2suVJcDH2oqU_qn7K8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخورد ناخواسته و عجبب و غریب علی حاجی‌ پور بایکی‌از تماشاگران ژاپنی حاضر در سالن در بازی امروز ایران با استرالیا که بعدش‌ فدراسیون والیبال بیانیه داد و از هوادار ژاپنی عذر خواهی کرد.
🇯🇵
ضمن اینکه تیم‌ملی‌والیبال ژاپن دقایقی قبل سه بر صفر کره‌جنوبی رو شکست…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29661" target="_blank">📅 13:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29660">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAXtF53lVVTtXontkzNnoLEn2B7lVeCPE9WlYknPkdX-WA-tKDk6ypy4o8C4TCr8W60GAG4_MfFGce3VkqDzM41DeSWvyzl5MZLw4Qao6WGNY4ZY9h8YAaOIvBfBMCX12paNIwq7U4UUES_WDuyVCyjqqgajuJlNqCzqQjeBlJSqn7mede9OThos_K7_mWWUfZrlWembxQ0idSVHGQcoRLYmeiyh5siC7oL_dI1EnCax8P78MW9a50DqfAV2wt4Xzm-EApI7guejlZdVRuF6Dx0NZFjtluhaLmicBLPd1_L7g3KfutjWajLEDWkHdcu3_Ot1bUi52Xtj4J8sssyYWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29660" target="_blank">📅 13:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29659">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=qNlVrBWHbAB0ZtqPZYnHfSDLupFFf20Ea2x0LKRWBukdMqpRSFUggAbStrIEGNixNgi0XkkaSImJFCBYccwqg5cFzzImNRHZthsjO4O1z8m1UjVV9EUOdxxppN8IQ2bvz9xGN2kAXT8qVAJkPoPKfQgX92q6ttgXnMEYvW4PcOjHA6Wpa24zRfQF5V0A-tSkAHOf_tecXI9karRc4l5pitE2GovODUFVHUdYfBBpn4tVUzwM6TwrrY2yvg8WVHjZahDfTUrbbzo3yEF3wZwtK3t892ST55MwZtrYGEU7qvvTFYs_D4bwd0_TUNZiZBuw9fOTcmjvXLPO-vAPXv1G4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eab57eaae.mp4?token=qNlVrBWHbAB0ZtqPZYnHfSDLupFFf20Ea2x0LKRWBukdMqpRSFUggAbStrIEGNixNgi0XkkaSImJFCBYccwqg5cFzzImNRHZthsjO4O1z8m1UjVV9EUOdxxppN8IQ2bvz9xGN2kAXT8qVAJkPoPKfQgX92q6ttgXnMEYvW4PcOjHA6Wpa24zRfQF5V0A-tSkAHOf_tecXI9karRc4l5pitE2GovODUFVHUdYfBBpn4tVUzwM6TwrrY2yvg8WVHjZahDfTUrbbzo3yEF3wZwtK3t892ST55MwZtrYGEU7qvvTFYs_D4bwd0_TUNZiZBuw9fOTcmjvXLPO-vAPXv1G4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
هایلایتی‌از عملکرد درخشان عارف آقاسی مدافع 29 ساله استقلال در بازی هفته اخیر آبی‌ها با پیکان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29659" target="_blank">📅 12:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29658">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVzaswr0QvXCU0oeg2F1OSR9dRoO024QrhbihLg6RBWcKFyOoBRx7UNJJD98t8YSg_k98vMaNr4b0wEkqATLV-XkF_JALv47uGYGAsfyThARzT0U3DJ_JCYw1_A4Ayf-oIVNp7BbvEfAMkVdUa5RNaVp5aGe9oDsqIxX6SIjFWeoJFGg8Fjjul9FWX8bduf3pwzwtDcrZobIZ0ptt7mnXUCW07aPC4vm6DBYDQ6ty5eu7FeHNPOEeipoWOHyYem12SIpTMWZxQ9gmWT-OqCNa1cZdrcdAFpVlDYqleIWPa0p9zlztokZKO2p9RiqMjWdneHAmQs1OyB0bvQoF-CVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29658" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29657">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=ifm7_GuuKdTNhyhz6Z1-U6-NmPVwi5OVddjYxRuH1kljm_Sdy_ZjQMHf_Z73uYwxT-MFMs25W3xzW632GX7KGjG2lqg4vA43ouGncBQTyxxCYKheh96xWgHQ2a0pWwn7zaPY62z8csyZAf6Bd5ZPb4VTPM8YtFHKZXGQ8_U7CgRXDVr9zeY2QZzRWS2evDK3VyEQ24PG7KhMZUZCpA6c7fMRYKnWS0hmdqoU8Qn-fFCLtld2c9fa0aQHiKulm-JhSL9EyR-N-piuCsbqWoR1GwwbyvdvIdv1R8S4-DzfKGk9jPJfHTqftL1vCp4G9KQM9thHJPV09K7jSPsWjv4sVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b08e88d1.mp4?token=ifm7_GuuKdTNhyhz6Z1-U6-NmPVwi5OVddjYxRuH1kljm_Sdy_ZjQMHf_Z73uYwxT-MFMs25W3xzW632GX7KGjG2lqg4vA43ouGncBQTyxxCYKheh96xWgHQ2a0pWwn7zaPY62z8csyZAf6Bd5ZPb4VTPM8YtFHKZXGQ8_U7CgRXDVr9zeY2QZzRWS2evDK3VyEQ24PG7KhMZUZCpA6c7fMRYKnWS0hmdqoU8Qn-fFCLtld2c9fa0aQHiKulm-JhSL9EyR-N-piuCsbqWoR1GwwbyvdvIdv1R8S4-DzfKGk9jPJfHTqftL1vCp4G9KQM9thHJPV09K7jSPsWjv4sVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2018 در چنین روزی؛
ممفیس دپای ستاره هلندی لیون این سوپرگل تماشایی رو به PSG زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29657" target="_blank">📅 12:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29655">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoxc7vOZQw3M8yxLftVyXqNHykq5D9vlNaxbVS92WdduLH7p3qcNkzt-3luT27kgnA-OAu2hrvL3urml1BjVQTRtMOu0InQe_KDe8Z7qi0VwMYtowD8GSEh8rf_VHdfQq-tuVp1HPxMG4A4etFaP7jY0dRLgD5wydnwJau9IfVWG7KS4JqhuufkQVRrA6rHf-h7vywAefgrwSPJi5wtRZcxU7j_5kzPEUru971WrspsZZoy6GQjDYaLZwjQ7Iq9EXrU-2Hxo8O7l6AToSDUGCs-cgAhMVo-3CTSlkTLdV-yYwI1PS382oehWHDcoTzHKO9YMPqJaeVZ7CG4JNgd0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29655" target="_blank">📅 12:05 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
