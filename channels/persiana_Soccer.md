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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 00:42:14</div>
<hr>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlrHjr9DTZ8KlkRuk6JU3-Njfua6UQvDJHZ8a0zP4cbNZkomR6_0F3lkvoz2YGLYuYySoiPyCzhwXtYnpPIXBZkTLhErovFGGMmvkgo_usEnyV3btTrxzFcE6VUxk0N9-7t_YVReqUwXmgeyMBdKdySRvI8SO5l2a36g2IrJ-g5a8ypN78M23kCyVcD2bh1mvgy3rG2y3q3Cy4Z2VyorUOYEoa6mRQGMZArlHi2IxCFeNg6vZj-IW6e8zDkEQbALPCwp-z7G7k-Z_ClL7_IRk31cH-K_RXaLma3nvvwqbR8pk9-TxL_zRVItDU0OxvUrROld1whN-p-CP-fqwcfNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxegBBMuFxmnc4yaHLJgbFi2Az4EuLpZlQLgt3U7yCWtNZpde6sQOMozeVl02VlYuvSSdqDOZne9xwjeEeZaajBj58sMsMJfrBE2fI8LE9i1J22s1KaiTY9sK1z49Eu64ZTyBoT5pIzTwrpnR_8RXRwFGPX8YqPjWRFZf_AeH2FybeJ_LD92ERzG4PgEHbNk0FUxbJ5dZ8LSfMnOjB_AGWF6Vuw1eXDp4cL7_arfvP9d0Y2FChG-O3Is8wU_OPfitXZy3-DayMRM316htlpbPMkWtNdcgETuKBCW2ue8tSvqXYg1dwqVi4NkDlYjT_iE5ya_pEkvoyHGKKBDSS_oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qaqd0ggb5bnqYE6HEVE5oWfsAtF-C7oD49gTvHt_lmxvDTSmdid39VNH1eUef4JRNqbVZzyAyrPDXDZ-t6oMrP3D3NfKqqN_zMJN7XCl-UhVNGGfyo6m_8vSZKBfDldAcihlxo1YYaAmkdVjw2swrT6og6gcDBIOSgSpGeYKahoD11BoUmPPUt7co3DBqJNxQ570JYLqiSGIFLyW0i3WJhaxGSjMiWOeNwAzgq6PBOs98uGBHLnnAPZH-jPVwGNtPpy-3wJtk0vE7SPkqenw4XtTgAwR0Ximwl4P3o8n4rKQkZZ1-riIs948Sj7PvlHeBZjm-Npnugic2xTQIFdLmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fqp78ikRzeorITIwnCNmkSzAy2tv1mI7lV-FkfTpBwTlN7PEutStUv-eDWF9r_U5DYIWLvYFE8KxH8igtvSQnsvnFhcZjZyFIfvnGkz5Y1jfiXb0920jxsyeio8h_vrUKgVXjeYXlgfvC0pXoVk4MMcIlaAjiXl9LaKrhkpbji6z8qxrTsa1Xr7rmEBW241c7OwFgwhyRM2leIBJT8N4n2DzEQ0i2MOgRWkQMzqhSJ7eupDdNFxBb_J0FH4CyVE-b4_8KDd8T0rjL6681rpbzXsFFc1TPD241fsfzsdQlWsuozakXX1_PAZQwtijY9etYY95ShwulPsix7XBvLNrog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0hKJ33PYq6JW0iHjPCb9qy-Y0BRjF-6Pv9hinZYhX2Gw9G08iqqHBYGNJRsdhvSHsT7yShfxW8aO8GDyQAVc0Ts36ZYqL5pzICeucB1Jllg5CG4-bEebW-tTPes20GF98htj2jgk7biVknz2C3QjrQBfwuTRv-72UYUiG2Oj7NDmhFhGWMiGVSvDZ1tZk9uTH35Y6J8M_ue382e89JmTD9AxIjYH_4s2xBWhUdeSwsBXVias_W59Z0pYJwLv0fEXdyuNIgF00bpCJOPCwf9FqEdaaTNQSxRQWrdZ59Oq3eMRwy6JMSI5Ff1vjxe7Twf1r3VnaSevjmxaUMIfVCxcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwz038Tj-Rbn-aJYkzYvfuhY1rkps1K9EW_uDTecphzHafEWap3iEthHNgSsG2WfNm93CNGgvh9P6EdcMRzB2FQh84bzQBGtQz0S9AnIgFDKiKy7-chwA-HsdLb7g3A8AGq2ycb_TSRXEWdmpdpo2GTGVfo6uqXyJ7yUSipTsr2VQFypCpW4Q0lCSV8Cgwx5DiTiRErknG252_VIVx_wGbpVG382ygbryHnSLcrH6i3f0eleN9y8beiaoZMN4Xx661YUDAZIYgPasl1_Mq8I5fFmymMuV2x424b1LaGeu0o0BGLFnivx8bcW6ycXP1KuRLsa8BL8dlEOfI-AmRVPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDDE6CiP9JTujxKJivbsLM7Zg8PA005yKapFfSloRGnBn7OW5r4qywsUas4tEtJE-18aCbSU2z5U6YBvyczP36XjN9NW8XSgFWBxxQmlbmnJGyJzxwcRih3SbKe_WU3B0dekbQqaQp5CS42rE15vWD7MCjQ-zm4Rap1cbUvJkYXF2JlccQqQ6t86MymqPaI7ooHSgVQfNAWlhLl40bX9n1JnJCCbf-tuEVv0De-b2vN3fB61qciyRsh_t-6AOlx0wOFkB3t_oGLPOGmaE97Fwd9LiESoVtWI4nEfMAu85b2AGX5awAawj8iyyk7qvM_pu82FB2NzavnTlc6ub-QTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKZHTsvPcJbVSAOUZduvsX8-aqHqsC_zVggOQzcTofnJR5qoUeuZRYGL7UioeSsfQZkDTOAihXV3gTFzs8YicZxNliC9eIXoXk9crhKO0XRjRj0f09uP_myltklu41G3bQ0tzl-4s-L6qM4TCUayKWQEEVJNQJBX9W7z-BOHhZnQKFiNhM4K5M69YJoUC5oNVtB0CG1P6Rl8Q_j28MbU143YbvvcPyU4B0lw3U6n2Z1BpIyvLR5zpKFdSJdhGCLJzN-Qt6D0o8t63qY5pZwtN9OMYnNm9hNQ4XKPBFm5_mesbTzNOm8XLlp9VZdwV0yz1O-Efe69JOAKgvL0VN9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVCuPFe0zPQgy8VRFbnrNX2lMrdIMQQ9OlcHE5yegvoCigNhED482OT3g6S62KtQZBQlnNJtAk3GXhs-GRrigmAsX76ovd1hSkCTg8OZ1o3Oq0GqpgjY_lh22Echict0NyF6QvBD77Sa8PJ6qRiKxRW3Aci2Q0cJ-4Z0lKmPl98snGlGBHkFvJ_GXieZaeSp9qCkvR0lNMQ3j1Thk_JUA2kl90eL_u53nEOzBlcTxlHCSBon9V0DzurNHK6iV1X_0mVV8dLNPzRzozrxWcTWuotTaDZV6dU4CxYVwhtrbr2FOI_lGWev19FLimAvEYqmh3Kcms9V6kqL9Ni0q5vUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGoEOhUoJSpSME0D2rdedMVqW87dMz7QwoFdsNUMY2U56RXVwkJMnXupD4dD1FvNx7RSGhqAVUzegooSl6r9FBW7p6H3UDR5cxbfsAndEelwvJPmSZxsD29NRqJvCh_QDOz2QhwMfR3LfN1kvnM8uc6iQ4b0N-vrzPZdzkPLXdoy9mvkFDLtxnDcjcFar3kwmynMTGTmQETBhOyTr8USH_MOunqwNTDSZsihooMkSTlGBNQClj7tFR2tG13zYE-h8UiLIUODi2Jw32ctYAbVh_KMLrD5B6PgDsCGGBStXm_NgHi6lkS5N1JczqSD4Aa1KsHP1LQMJNc31W5SAslYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQxExJs_l7fvykYjTNCGkFga7I-p5HeXWPA7XTgmVy_Loq3z6EkZ6SbDrIWaNpH_20KVz9xEZPqB7xVsfkmX7xPY5wRrjmXW3YggkhRS86mYIHF5CnkoeDmCf4C3cnk7DWly78e1UdM75zoLMJ_1dsYDCRh0ipXYn1CsiwfDa8t67qFfyHeQyDMc-UI4pzxxLorYfV8CBrkN1rCpxUOuH0EiQaE72331jrdfw1UjZelzew3La-zIwfRzmnFzAm2r6gIRRYpXVE3GUCP-He_6gMouzqKYSE51A3VODMWND5aNH5e9d3Oq9IO48UyCIAiPits5OukNQ4pdjTHEsvienw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjmVbf8daZaPvG53aAWDKG4SjApJTHYBkcRlJKxno9iw5YcpS-RyscHTDyUuOzhENeN1VIB4lGc5vYPdW0QeTyitlBAPEBvZ0g2xwdd9mHF8WrKHHJkYl-d8Ax-Xc1rPCGw4J78mmaXCAdT6ilDuy1eNnD093oNZgwyp-hnbNT_yDxKSe0me1FU1gaUR0H0xQxT1cpDWdQ058iUtFT6be4qv4v-2tnJYOJ5ceZCxk7_5W_8KT8Pf6TWlFUtsfJVEPFkpopYRXtIZe-EPPKzA_w5YmNng6LkItWOQPbFYcf5heO9E1O3KAzqQT6478SV3ve_fFwAjTWcZuUj98jScWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnNForisJUhOT97zrMCx6oG6s2PkkmV6yWW0Y-7Klo7_boEoJbY1g3KmiYnAUzlw4X0qfWcb2V_zsBVi_Ec44921A0i-ak5sdp0jJy1NN2lhXq3mJPc2z382O9GEHtZY8tk3eAnSDFfGU5s7Z_NPiaqQDAWqSL0w5lsU7D_CJXfhyUl_8eW2-pdyRPk2wBJNnPXjykJvNf7fEdIusw-kUj2LXAVHQEj0JuF9HRRR_C_hhegtOf0CYPGJf8_Jc0IThQ7whjUGhieJvMV-LfwZsQFowsc18wxJhdhfBfe3uIIy3Tx5oORL_wC2PT6gMKj9hZaHxImiz-IysKU1LkLk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG_CfQZZdGhQRrRAko_KQhxGfnz5T8hj3lRWy0gtcpTAEKaKSJPaZUEd9PPVtZ3BUVqbDGioA39QoSoZZ5_nrTR_4U_llnYOuHGz-c13YCVTxMXPy4wa2nEfadqUWnJLnbRJ6_l3ntg58kzCy-zihC-Ga3MJcrbm1EUWBktxz1oVMUdS92TpVhI461aQrX4nRIXfF8r1yJQg9zIL_5lYbKwouB7WwzZ3R0PBuTeZh26JPvxJH6ooqf31BztRckzgr1ff-nLtmHTCHI1icz2SfPFTv5cxIYljtXG4jCQOu8VF5ko514Yebp9iwjrN22HBblxutIgDS85DQYdT0c_3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_QZM0YhUjDdVkpJWBLJNO_3VDNpfQtN-fAHdGvpF2QgIMYfeK9Kw_qs5DK7QuLFdc_fgaSz-0jD0lVKGhZfhG7PHk26qh1tbzDUTub2bqY_1-Wm0g4s7SzlqPXGIz46ML3SHKcfPTVWXYAqSdZelNmNd8cU9GCOK9m8mqPBsYKux1ZDn5WI3AWtWHd8EcR9PrsrbmS8M3FqFLIV9NzWg5VB2NQDNfFerA9sIe8GU3RT2trDzMpOWNsPv98ZMxYXeuFcwtFeskL-XkqWMBN9Y5IwDYMR1qn41JZ2JsDqOdxe7OgO1qgYHv_Usn-V5u4h9JGAeHW8LR_kWmUHKEgzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMVZdFKdARi07w1A9uHepQRT-JjXq_HwJXYajhSbWRv8xkHii8Pdwfngj9unaUzx7aqah5OpgHo4rXCpBaL7-uA3-S-sV9lig1cMw_BhvXQgraTU2Mu0QXsx2w5gTDsTXgmnWjZwtENis0NSMjpR18Vc1gaNV13N15WfM3_GNpUDzoMULcV8EfkIoev0i2JMAhPzEBmLVn79mQhuLeC9_om26C54ACVKNdCK3DaVYYyAtWjsPzkk4aR1F_K1JByxGslnG70Ye6C3V6822dDyRz5atdK5pRrJDu-1weghGX3792Vjx-AHCqlBxJ40JyUQAQG8GMP4fx-gVy__qVB51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlhteimBIhnON3duFv-NsFXpAwlgOHUBmpIPGCmgB8Y9qDRcZI9Ycg067BPUEzcO2T7fciJ_J2dodyHZB8rX8kJYLXKBIWsLP4KS-A4yKvN72fppMDWmss5hybI6RbOx7FZblHNZsFHX1oagkLDiN8CkZx29d8UWwkxb5zXOrQUOQNZLdYMtX0VUfpsqN0Vl_viU1vAMps6TOtvavVrbQVLUGQWnDkGXyjZ4htcwjGVHNHQ6RFRcvynm4CUhCliQVFGYbVXr-UZnXa5Ek9VLO2QDE1a02oNd3dwTQHxy6TEenf0h_YaK-M44MxyaD9Q2U-eN6brIr11m5ttu8fjguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26073">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFlit5GmicNI0LXSf1MNSG79SETdHdzF-vqtz1JbO-tDliuN8QshNi62FE4o_iImbdaJf2dbqcTqv1e-ckFGS4rhlGV01N_TKgD9tLJ9ZaECRsDA2F4HObCuPQQ0oKYMWVuk0G0uBwl1MDbLqRkDFc1GCGNJpOiBoAMt-L6pEH3Higec08IfaYxNW_2VdN2iyUTIDC0U53ypWVE1Km6Mt4Adje_fcQa43iKzCtJMrYzXp2dbWgwRKtWS7s8y8kcxuo3UsfLZ3PxQ7CAIMeU03Pqo-VojBvm3zU89k1JzvooFKK7J0O-wgzbz9mJaWNHvR88HKq1cbPc7uSHGpgsGNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/26073" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIJ_A7nIS7z_iyNiiGfV-zEPYijwYD9G0jImazrNbHLzPclkc0yGaHfoKZ3meiqhwCAT7csg0KloGXZT4wn0ISjzP_FPdW1aN4qkNFa4H6i3JgEh7mrYRwgDRg9IAGPrbK4k-9LMd1UQQPHE83AnyqOM6Ey65TNXW8NAhtksWY5NWmV1HgKPKGJeKgNdRvkGUukAR5-3_9HjzTAc7Hn0b9PQg2-Xfg8i411kvkc2WKZMOEm1UZfI4NolWchJAXDnu49Z3UO-QBUC43EgiH0ngQg4LRbF2z1tTUwd-vgAAmk9jNfaJWc78RjeHA28VH0OFYpSB-sgOrYuYdb_xvDJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiShKAuVHvPnloWd7Qbc8XTLgt5qONMWoX_az4N44VTXOe4N5Y4el3OUf5kcSmE_w9BEMQ0-t8tcsDjj-7kVUiFU0mJ-aH_F29xnqYUlw4cjIcpFS3TqNqCJKjGMdnMM-X8Nk7-Z7t7HO37FOXt9k4dl4wAVGOQV96CS-fMhMq5LQBSTUP96hsSix7eu-iN8abErO4Zy1mhHzDkLcLt_qdgbkwfZuoX8p9PvNbXUk8jXyrkj4Q8ek6l_cIy6rt2naXlWPBE26LO8l9kCvIAW5U5mLh4HeT76IjaD3XSI9FaBotKv_nDIRgoESl4Q7vkzVH5RR6Zxa71U3S4VNws4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=XjgLeiBNg7QMFDZijG84OWZL_pyVR7F3JfVnykLM2K4fuDGPLL4QmCWHeBrygQDxwrscHxd2TnJtzkZfawZp8xN3iX9iBoeH6JXG2GVsKJEEUgR3TTMlMqVYyuUHhjCQdUSUGsx-CLudsWY8xjm-FEobckUr8TrvGJDs8So9tXSwLloye5xbFDEfc7lmJxL-ilB2_OhmyqzxT9EhiuY-QjwC_UEYjrjJ0MxBAPfx-BPnl60l8HysmNkZYWAmiaqw7uKDQCbfEA9GAyqp8YO85DyDj6nW8eNdFj3NA61-8D1oOwkMROJZgHjku_aAc2sQLVzssKT4wPWX1Xjr0HkDFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=XjgLeiBNg7QMFDZijG84OWZL_pyVR7F3JfVnykLM2K4fuDGPLL4QmCWHeBrygQDxwrscHxd2TnJtzkZfawZp8xN3iX9iBoeH6JXG2GVsKJEEUgR3TTMlMqVYyuUHhjCQdUSUGsx-CLudsWY8xjm-FEobckUr8TrvGJDs8So9tXSwLloye5xbFDEfc7lmJxL-ilB2_OhmyqzxT9EhiuY-QjwC_UEYjrjJ0MxBAPfx-BPnl60l8HysmNkZYWAmiaqw7uKDQCbfEA9GAyqp8YO85DyDj6nW8eNdFj3NA61-8D1oOwkMROJZgHjku_aAc2sQLVzssKT4wPWX1Xjr0HkDFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvyaANO9l_YlD7ax2Xol4fBvh-Kf78kxKZHI72c_bMjAERmCBroH9CoHvF5cBH2ns21TbpaF2dBEUnkgOuOPB_TxPyOzkLdXPu6FQcaEpX7w49i23jMST9B4F-Nexh2WHytgBsfF0awy8HQR2EtNVDLaD4imzcS0LoIHSLv3DyCth2ELQvIpjBBwQFMfrxfkR5HOEJcmiJicALh0QDgGpBDnEx7fKswXkbzvjpW82HjiDS3nVu4Tj6v4rXkARfZbJrkAQ7gFDICw4bWQGnd5yDeDO6BgOD2wnJpILV2Vdp0EqxqVnOyHT1u-E10Y9TvZNDCwkjxwH4FHH82Sufoo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsydjyRrEn_yIAZJvAmvneztY4liKv2cwALTg60oOQyk_Gv0yF8bz69Ic5a598WfTGjbAi45c3LREKPyEjvPt3kSP9gZnxYv1JqNvI2_mQAkNG5lrkcahBzn34qkmmemRkJjYXhZ72JwD7H5vPGNgY00uifNk9hiEacxmZnD8unAN4dxre4GGUfoqfA0xiBGMnmfa1A_HCnS3u0SDfXBFWfIDkoz2O0mJvI3msydd9HcoZaAOJZZG0BGQ0kZJVjvCyDBQGLh4Oz1tvdij-qdIW7S0bv5-SbrKMwsBtXmtUDaHQv8fCi_-7sAG0LzYk7nE7uHlnu9CPlMpjfJFFYipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7G54lNvPKACe2_uTWnLtGKcst4NW1eKPhSnSKrzf0S9ZoVES61_pDVcfxtlGPXlUJRruwUx78o1168sO0OACkzoSwKcczgv5TF31f7kGfm3kmu7tGlwzQgYCVFmmhQ7-U7i8f523tXXHtA10N-G-mVRXvmXdh_DMB3pSNGptKS3p2QKnqP6EYJ4qS9rr5ZOXPVwOK5ca1LkC8FT_XKrAbLxF8qkS_9SftvpFIW13umhNx7mIHCpwUJNmo7SZxpT8PMHEqHzUPgzplT1kUZlHNh509cUH3w3ignVbUOevxW_oUEBZeqwcgnamlPf4RqbguYVETKoQdbmbAsNwRzZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saNzXnbGmNQ1_FYjqjtJ0BqrujAO9h0E9P6obtW7Tuxmr9Y_93oJBqjBYIZqi5NYs4hukGzCVXDG7xyYXpBfJRvABknDaazsm7_FIdTc0vee6NMhPIZecGHC_Zhv_hZaGBb_wn-801WYfujSWoyn_JJ2gKRLtUSogXra0iPWbM5cJIifrIhJO1NYw4rnEty8m9FkBcHVCgVAP9tcnZuGZglsNCI7Ja_riVYR1UxxVDIkUISTpxzMLVD9CwBKxw8z-AxG6DX8r_ksKkAtLg9Qwb8g3qNDKTei-VnsKSmWLY8C0Iksx0RMb0bsXuiQkahdw3KJXKIDNyogcbHF6cIltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbXs2GOh2ibErFv4_YS6Gykk5srqRZ9JMbdhVh-0Oh6l84R5Z3n-F7R2hfsUhsNnd418scIaSAAt4JWZZq4am2V13-ygX-fzBnF6XauTlPbcyEyCXRHcFf60vOJRjeYYP_YuKwETVfHovpXEPeLYswuoG0nUX9iDBvPLJpsF6CFsCJBcFAhLYuBijzQykF3rlisXBKxHxUogMA9w3UoyMyZlePgfcnKXTkZ6O-_dz8dL7rMHpJmD99Ar7zLP5sI5VDlkZ19niet1AWjX-jsYB378gQ7lwd0hDGAsc7bTBt3XfOSToathMAayzY8m56wczDD3eNc6sygu1EeDmY8lqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBPVkw31S_J18a8Caj4jal6VRc_krjCjDby2HLeQHiUgY16RvBdwM8iSmY_Gg2farZ3KH6irP69mbQOmcFs3pauzkrfUmr9oPpL_VRCa7RrlblJdYtsUwUkbx8CcbxNWirWrSpob-1SB7NrCr-ev7KqCx3d4mbUdHI4Y_2bcOnZo93hcIOfHAzKrSG0JKe1anfuL9T409a5QBcZhiX8xAT7VcHAHSw2JDOJXEWV35iCU-1vbMXXGnGUud3hH7jRW--2fI8kx_F7FgSgqjoxeni67AfabhWXhJwhxOLDxVrp5Cea9f-qk3IZSV82cnxyP_CnwblHX-CEoOTq3W1TzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVad5Z_WeYnMQaLn4zvEE13xYJt8pFaTUBOPQw6CEIMSfK9PArRyYjGdCjISHAou9lfF7HlVXfpubt6xxaRljMUbrVUC12CcXfFDkhQ2zNxoo-jO95ZCCXL7b-TFo9O_dkB3O4c--n_qZXCQFji1-FBj19sWC4wGjkT9PkKqB17AQXrYB4CAGYvp7Fvls7PEHL7E3ZxC1pMYgiDt4KrR3AWIhi0Z6wqyv6ew61p5HzqTsZDIx5XzTvsBS7F0L8Y54vFteWRcS6_7MfX0NpY1yiRWhdTzHNqzqo_BnwjnV_kgGSLrdRQUfbQoFTd9uF0SXg-ZeKcYzPdAwoSmXI1ujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsg4vBLwJ5e6BSn_QnbOQVUXyyvFSzsuEde9fMWhVvishV0AE7fSUpY0NGBBLH__uXVfKDSvQJ5rnYoQlZk-w0r2euyFNucx4fqdQ4l3hlvbpHnyOP05yG9cOvYOtI4u5F8JAFWvOeTRAXL8A1iSDE9zSJF43riJaAhRYO0WlQ3VRdH9irULGin_teD9SofD47iQWPiT9dtdhK6QAGiZ4jZRijEsc7vA-lS7qCLG4xOJEBiwV_yuL-WCKgBSNTs9DA45kIsjBcaOTyEx2AlRMsNuMGOope6xCE6KXPLuici7QpN1ynQyjEdFmuaXI6UYnCeHS7nx0XVBfzXMu_NuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ99USyvGhOYA53cANt1qJDNkOFRmNL2Ot-xEQiFVlnzuUXeSZvH5MJlOwU2-zTZFvUgldlznWJ2nbMldCizAzvuOuucaLVe8RBc5KmOOHi34jdK1vXKiWu27pdLeQ-LLeN6lEp2irA6IMQZ4utzqT7DvV8G1jXMTaM8pWbTGLbjs8eV_-NbeE7KP-wKwGac0aZC2eDXiSKyDgQBKPsyjrwWEVdqpUMNlQw0uDNEUlKPa1w_r3oThUmsxFtShR2qX06WynxsHSS9He8ubtPitcjAutPtE7hDiByeEzTYwupH7jUVcxJrN9Fz3dXU_0Kui0KMwK7Nf6z7lIFU8Tf3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKJxFdbnyJ6dupTscX09lgsmAFZEkA1_uD-_Z9x9jjQEdC7b_kZmSYz4eH4-3e7mcdxsfuBAeQKEzzxtk0SwULlZVOpX0K82IPwlrL1hkCZn45CaKp0Iofb12-xdLUjKGekom3KVSlI90c9DK065Mzcqxn6ze2ecE-Wctg4SFmV-9kMEJBFkzvxFbYbmqkpMajhoVfcWQNBAhErB011nRHzPcjP2uQP7H6VT_IW8C-D9-XDHf_xvOOS5029jawh7nsxvcrC82h7iITZ0Nw0n9b1fzqgMljt1H-DIS4-_d9dS5-ccAFDN-rEeWCAoBZfWThgSig0HiMDBTpKWh1elfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSvU9_f7j-XSaEso_a6Lw2QIu1ksAm4AIIc3E13AEQ3QUWMA7sIavj_NvwYZPm9AnwlZ5yavOhjrL3FEVoacRCtGnnb6Ib-ikXzlP-EIOeXCnhpVn__fcgFWfU8pqBWskiembmExN4V98a4zm9nqvbcZwQCpqURgeWbPsuYCWtc_H_0suLIhCHPcCcdlRa3TcDAnaiv-aW6blESvKU6Usw6InwNSL0Koeoiy2mVz7T94xJOV8k-kND1LwU32Vd7ZZvlhVZQxx-nqSTR0xwu-yuChx-YvmHP_tlQlGMuQOL5eiA7T4xNbMvq7lnOMpfpEqHAn6yw0DrIB_4S4DUDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq38ZDOVgkN3f8VwVkE8rOZX01pajxaN53NJ0tNwkwY3EMKu7eQPpSXQDNyMfHLCc8PtFK2WeiJhMBJMh5LrsjwhwMRtCJDGEimyQTqamNTGVvf7XLuQoAHw4yKjuGxhIveAg_i3qUwsQmBvmfznKc74f38iKyoeQwZT60X5YjEZZk6IFtJAhYrYEXIBSRX9_nLfVlicL-QLvaJnXQYWaZ641K2MIXa4s4kOWfrc3LyN8CUhEImRkJPG_z1VAyjrXtR3OaujuyGxsShCjCCQovQPrO1JomNyT3HhVOGJXzGzY8JOYEhL1zZlXgqnYTn8y0ivadxnYVYedwhuUCdknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpNbmGRMPp9tbNVKh8MpMqJqKs0Rk1VE30SaHFIx_FqjpCrVQ_rYbI-gZG3WOjqKff7CUYKuxRSCRZ3-D9TyimMzULDBPVsPApxhRjFLxNt7a0yC1dMgMfiUqCq7PcqiVkuTaUiJ6ZF1EhAH4TcNmoVOkFUjT8LwVMHVIE1jetLemMuyGt9u2okDkU3WQN6qZaHp6vb77foKD_HUp99cu6mU8bus8MYQsr8ReXG5GKXMFlrWs3w2xUTso3-MAax3XybtTxmoYGv6O4w7fV7JnRYRpKdARpveL2X5_IEvBRI2SQuWdXJ3qu1_qYqf30049eg_VqiiVhMJ4dv5kTfDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwB29TmiLX5uvyVLK-QwKSpLlNdnaBbu1VI8I4HTI7zUCu8yw8w5Vqm3nyLzuibja99by4ZyUcaXDevhyEqPqfiMOIF5YGd5Sl8_BT0Dnn65qEZH6nToOmvX7mji0qFEFPDe7FwjyBkqmrltJXR86e5Dr2RGdVW0c2un7i-CHUbseXhIm6AZ4qET5MBx8yb4-ET9wT-P0M_EuUDys98bRQJ1xY8UizMacj6mfQ40Pbda2ghd6BXdhgZdwtJGcjiRUkS5FBW2ZZHaBmS4otttZUZpPdL9jiYoqzAC5Ev-SDkqqwosWZkMpv4WLaWs6JeMR4WtXjhZbR3NrWSoeuQHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2h1Tzb1kgSK72MLoVWFIpLMQ81uPwLRWsyx7lCUu3ka2urr8WCmoOH8dWVtlFFSTcyUdriwisLZT5wxY5Dyo1smPPteUGqmrJdGqiYQjp1FKYAdfbGAuFjYV_WV2zkPmUvPsQrCYOHE0OOBDIA3pMYmO3LYjcs2r5gopZas_VocuZgblwFW7Br2EdMTazRr5ncjbEH2fIQNEiiSAcm5Jh6Az-WleKOMNavxa7s0q1a2mytlgHMDMifjluJ5_MBB0OyZgoGg_Byt0SZ31eULY5shuN1PWRuMgaGbbl0N8brj_PHFLQtemilPFk4WL0FEA3yVbMUIomm-qOD5nOoKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrUmBL0OI08C6JYdLdjE1p2ZTzItOdFZ68CHa0glmIuRsh0EewschSOAhk5Miv0aKTX9ZLlIt32ojsmpmzBgthXZygXzAQweeoFcSeeN3K-51FhP6IZd6TwngBT-UNHVtHhuEvO9vi3EYrS93hxBdOv7REConUjZZqOOt0voSqI4dr_Ba6zm8eUEbj_knWZVzRlvIgjMrR4g507vTlMv_SwwT4wKCYpVQgpWA--H9xEKtlY9Gxmj80MReg7lyyGCAZmlnv5ceIsX6S9q9XPJ0_7ozwmkNPPgvTPCRoGIqWBMLFvGMrm8koxl4RUvRYT2xafNcta2aT6FoAwLBIBusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQvz_R-7ZfOHd98lF8bgzrmg8panqiKoq41TgiK1SF8VjXDpcsBrT2qXDx7_c5rcjM1wbjL1VHDdEFu7pesZAbGExzg1i1iCoepg84aGQHpTchCv0Rp7zjk9gRv9EIxxYFdWtrMceU9C1hsUPNBulrm7hxOs3cSi_isIAg23Y2Rq1Zn-qgExONNXhCOczCMFcMU-WYslisyS3xqYm9MqHYnLOmXqG3jObuvOZkYg-gtQLGf9VrWC149i96IJG_V7FmyMZ8wFw90GsuBVgE8YQ9i8iFyXIUXX0wAagKfetVW8UhJ2Tkac6VET8lNYT1HaVfQebfpTsgpKSV2k39-sng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNoVGU2_YBIlp7PBA8RLt8p1lE26kXSsLAcywSRjA0luwxfprcjuWNM_-oCkqHN5LHiIvFMYLHyPjuA_uuHYTL6NCYQXZ_B7WTTjX_m7TIDcrBDW2bgUfFaPpyg5rDN_JZEeb_E1UMzhbyKyWDh4rDMIIno2VTEM971aOpDf4fdC8VWGhbivZbZEFmltNtjMabfoWSXF_3vaRc6HYL-CFRLxqVRw5wbQd0jvE83LD_rcidsXytUFV0zamTarnPq9Gh6PXYZ7E2uF3RZPekS6NN7KFYBXX-4RbbZUH5sZH5lf5pcUbnwKYCK98FEF15yVemaBrWXt-z9O1MzcO9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgFaoQX9ImNhn9TSi1O-GFrLWQK5hSqwSbOjps3a_J5aVUIE4tyq9SMrWQtHFDKUOA8E-L7NNAf75AA2TMNRcJZtrEL5KJIiFot8zS8LUQnoHzLlMrC0E5B2ei8A_obUpsce-kbdzXpkzgoR2jehYyIpcivKMYjSkRRpGOijoufasTxZXn27w21oQdigqDQMKy1WyhRmJ0mtP20of1wXWwB_PFTt52cfAi57i0X6OtlU_2Me4JOCelWl16ip87-7aM0LQmLpTgtR6MxhZ9nRhMOO5fcBB-dpTOGAIaNyWHX2Bq7atXw2xNVT_EOPcsg8n0tStSWNpWi5EaeOJlB89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=NyidLaUVnLePbPltjqZY4bfyeBzsUN75dGQzy9myiOYxdpdEZVA1GcVXfDE8jrk89A5XBgFNFXA_1W0kNAZwC-TO1jLSi5Cqqsl71UNWC0asxZplXWNU11kiYVpDIWQV4igcFQn9VGqtwPUmQVz_X4Qcp24fLZeaYw1gYMFqA9zTJhMEQRc7oxkxQ2KzD6zaNUWxJw1dANDtrLVKWR2YUW099sh3o5pgfy4v8etlLjh1CInxjr4T_LgzdFZaH1cGk7KOUMHPaqI_DcnFHnyradmsMKXnrAx97hU9Y3I6R0A8FcvlHtyPISjLhXa0JalByDLzxwhQrDt_YkOZdaqYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=NyidLaUVnLePbPltjqZY4bfyeBzsUN75dGQzy9myiOYxdpdEZVA1GcVXfDE8jrk89A5XBgFNFXA_1W0kNAZwC-TO1jLSi5Cqqsl71UNWC0asxZplXWNU11kiYVpDIWQV4igcFQn9VGqtwPUmQVz_X4Qcp24fLZeaYw1gYMFqA9zTJhMEQRc7oxkxQ2KzD6zaNUWxJw1dANDtrLVKWR2YUW099sh3o5pgfy4v8etlLjh1CInxjr4T_LgzdFZaH1cGk7KOUMHPaqI_DcnFHnyradmsMKXnrAx97hU9Y3I6R0A8FcvlHtyPISjLhXa0JalByDLzxwhQrDt_YkOZdaqYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVxzpmbEY6mITACJAKa9qjIk_hVZVBmbbDMuxOTgVyugreOb8Fzrx6-wGQ7IrtwpR_kENLRbdg40JcNCLh6-tNyLtVgDUozGdVzKmHebP7wQ-HP3AtUcsT7QXDSO0l7lxpZuzns5Ilh6HhZSs67lZSakB9Jv_BUUuNJb1B-WIuAAzz8SZuCGiqa5iFu0gL3FShKHur7frnFPdHW34SLajFccUUO10jEv9l4wqhVvLdgwRxvIH2Ri3FuP5r_eAqFuFpCL1KlrRXne11tgiTkjVCOV7YHZHbcmtLdccIbkR1iyi8Ye3jAHkOk4CiTV2NKUGroVLDsm5U1_YtDSpcRDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNdrBDbm0Myt2ESeMUowGqqf6X92OFz1FUvAyLpot6yHthRC-qYjnaFx5qMcQgDkpbLByELA-wtFHUwdPhBTJ2ug_2TmjEN7KTj_JbMXIhCKtnTsKIYcMWeIHsTmiDwXzzxMdmSWAIoMXUOA_SONcEcyt9yiIJ_1qVmv_M2i4z4aVoR9w5cDZv0HZgAmcOlKpQL_lSJgN5y6iGd-QkEpJ4vg5Tc7VdKlmvNGt89WVxti1kdDpDPMrnB3IfG7TcSHJCBvxKtGgUUKDUNBl8yMD_ogDzbD3dBGaVH4oQ4axg2N_K4TkCZHuHJVfoLwHU5Ant5_Tvx9dMzUHAliS52nsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_nbbiGqZYrEcdE7bJlEnKF5MYvf0M5JBAM2wqzJm7RUiKrjEjQOh38xzztieGJDhZ1AYAH8sKMEDwo4mzzBCtWpSmD-PXhlLjVHGVcJ2mm8ud-RVY3Ko4N7GYJhAEHvTEBOCI1rrMRcI5Ln5kPz-soFLot0ykb_9HklH9UXpoTaNi71aE-b_PWTBut4Wl2fqMUbWxy02VNvdfqYm2fw3ao5cNv8Y6cGZ4G9DGK1FER7mHOGMu3_GJuM-5MRHzf2db6ju9cP2CzxweJuNRhIF3qXMwD93u7fWqrL6YuSYbHGNAXR97bMCVFPyDlZ2-iapdNIRfGjc270fRv91FoIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=QLoA9QcPfw7-CLt4iGOlCdieXD4NhGG3MKJVt_BV7NIq5UXReOJOTM05fUONZxyNnsM2h539VqcuN5kvgvxapup3qX3hnRKMKlgHHe4FXhheHRbespgY5i044oyfr7c-di0zc2nYR8PHokki3fLPK_JKi_O9xdLcq-vY3y5Gm8WXD8LbDqFX1IGWAlTm4BjLY0Koxjn6y-w-B3fUl50pV1xet_ezHAK56KowU2pke1ujFciwFf9GnXPMGz-KES5bY3tQJrHUqF3cn1snpKNu161p8re5OgpJValfNyK5gioiv-pICL3fX7jqlNXUHVI1uNUNfPsoNAAkYSP7zJgwADnnqLzmJttuX_RkFMoG2eTQYacOX77D57wQwjqXZ58-kTXKY-e9wpXmr6EUd7g5tEizkdopsUufmNhUpGjf4UWs7c23g4bnjQUcQseF1ZaM4-m4VIYXmYDVsv45AK7bkHGVh0m0HBdfVno1HQ_8QmVY52JOYmmXDayII9A2o-4jHwdg1v2twI80uaLBkfDAGhqf36hlE-pOJZV6t4_vmMrMyIjlBYYTMplkkOIG5q1QZI9KuJ4s_pRR1vCT3iStGI1eyZ05jZTQwU90rvo6o9gdq_y1CRjbhhheik7yvXZQHN74QjNDjC7ODGxbelDgHjgSTpHeulmVbgmrjdxcXY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=QLoA9QcPfw7-CLt4iGOlCdieXD4NhGG3MKJVt_BV7NIq5UXReOJOTM05fUONZxyNnsM2h539VqcuN5kvgvxapup3qX3hnRKMKlgHHe4FXhheHRbespgY5i044oyfr7c-di0zc2nYR8PHokki3fLPK_JKi_O9xdLcq-vY3y5Gm8WXD8LbDqFX1IGWAlTm4BjLY0Koxjn6y-w-B3fUl50pV1xet_ezHAK56KowU2pke1ujFciwFf9GnXPMGz-KES5bY3tQJrHUqF3cn1snpKNu161p8re5OgpJValfNyK5gioiv-pICL3fX7jqlNXUHVI1uNUNfPsoNAAkYSP7zJgwADnnqLzmJttuX_RkFMoG2eTQYacOX77D57wQwjqXZ58-kTXKY-e9wpXmr6EUd7g5tEizkdopsUufmNhUpGjf4UWs7c23g4bnjQUcQseF1ZaM4-m4VIYXmYDVsv45AK7bkHGVh0m0HBdfVno1HQ_8QmVY52JOYmmXDayII9A2o-4jHwdg1v2twI80uaLBkfDAGhqf36hlE-pOJZV6t4_vmMrMyIjlBYYTMplkkOIG5q1QZI9KuJ4s_pRR1vCT3iStGI1eyZ05jZTQwU90rvo6o9gdq_y1CRjbhhheik7yvXZQHN74QjNDjC7ODGxbelDgHjgSTpHeulmVbgmrjdxcXY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=t12S_AS61xIntmgS2Dkci5asdtDtz9o7n6WFpkpkWzF_sO4shoo5-lfBNwNP8FZMODVJmcHL3wOfzU-7H9W0MYgqQ4y9l8gcRHUuUsAbBDKgUjr63E6RBlfgiaI9PIcBkD2ctJRhYlK-6AQOjEKHnFCA7ZnDGl8yXwl3C70Xpe16nLivxR4p6o2Nz6o6-24LAnqsLvR4qskhpWu-vGAzqriM8WRi2yQrs7BoaR35-Dy35rM9zcAsNDDCSWhQW8VTLx7mGqtoEUbY3wFkd51mhLB4FlK4lXCtFw2n3SHGilBNj1OKoNs2zexOqEaVk5ACPu6hUalsP2rdGIphrHFejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=t12S_AS61xIntmgS2Dkci5asdtDtz9o7n6WFpkpkWzF_sO4shoo5-lfBNwNP8FZMODVJmcHL3wOfzU-7H9W0MYgqQ4y9l8gcRHUuUsAbBDKgUjr63E6RBlfgiaI9PIcBkD2ctJRhYlK-6AQOjEKHnFCA7ZnDGl8yXwl3C70Xpe16nLivxR4p6o2Nz6o6-24LAnqsLvR4qskhpWu-vGAzqriM8WRi2yQrs7BoaR35-Dy35rM9zcAsNDDCSWhQW8VTLx7mGqtoEUbY3wFkd51mhLB4FlK4lXCtFw2n3SHGilBNj1OKoNs2zexOqEaVk5ACPu6hUalsP2rdGIphrHFejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ-c2SfthYcQ-oIXRigOHrnlS-UsUgX5QtnXagrkZryK7ftdkH2gxR3yRW-pxbH43AUgq-Cf3luqnSAUOgYJSGZjmiEEuqpmcxGRa5OJwbP4mLGYcfoHh8pAArX_xq9T2DTZVATYwuCBzkLe9F-2k-f6eogdhQZpj9wDcZBmq4a1W98VeOSpPKq26GWVU6FppRxm2ZXlqfc6ioLYrAZnUAXwxNiBpcR_QrKuNe0HA6dTzL8j5wBxWbbUlpZd-Cm-j4CsFV0y2E6-ezUs8H9lyJHfPmo0aR9eJNjBVOAFj-wwotmYh_TTLt2DbpN04yyggk59MSdSj1Zqc4GpzJ4pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=UBIA_C1WUCCx1AhQxuO6Rs2sA7UJIfMQRVa5a6YmZzBpti-U7tgPG55H1akt61_X05cp-sn1oMffqcOZB81I4yYH3oQSRK7RLZ4FCd35d1DItR4cMWVGLW2f0uPFqSWaGU-lenWmZSXuWhh45ivcxI9EqukIXYAtcMRvxYpbJchIjVp2AJzwmgTAKYn49mRRnglfq768zioAVuKVhjHR0jh65HLA8Q1lg0g2UVu572KiOz7QIUI6jb6_v-sO3xMaI3IJGoQ5TAh6ZFVoJqZcniXYrOxGU21cPTuOgX7ZbWtEjk_OkN4sSvAIZ_6iOKa1hZXgHvgHBxC33a-gkzn9Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=UBIA_C1WUCCx1AhQxuO6Rs2sA7UJIfMQRVa5a6YmZzBpti-U7tgPG55H1akt61_X05cp-sn1oMffqcOZB81I4yYH3oQSRK7RLZ4FCd35d1DItR4cMWVGLW2f0uPFqSWaGU-lenWmZSXuWhh45ivcxI9EqukIXYAtcMRvxYpbJchIjVp2AJzwmgTAKYn49mRRnglfq768zioAVuKVhjHR0jh65HLA8Q1lg0g2UVu572KiOz7QIUI6jb6_v-sO3xMaI3IJGoQ5TAh6ZFVoJqZcniXYrOxGU21cPTuOgX7ZbWtEjk_OkN4sSvAIZ_6iOKa1hZXgHvgHBxC33a-gkzn9Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soPirOMbp0t6KFp5nOF7l3_-ooqOn7IaQnSMFSMJcS7uVS8UfdW5lpeDQk_xWGijWYxkuBj8anNjtXtBjt6738oSy3cG4fmQ-_9z0hneEP6lAB2r5DciFY3kBJ7RoJcS1w9_K-yuRcRfjfy36eGdYPvMmh88h0mMbfQErdD968T4LgqZJ9hu9ZlxxAYgOT8214fgqo62oQyAI9EhnABRfDz-JqgrW37jNRicgINSBqUij1_PX6qPErprdIFF__B_NOLRYw3Wv1094NReOik544fgumpA0ouvRDf0eme0M2v0m55cb7SjuVkJ5Jfvzq1OwLcJDakcxC33P0huL2THMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr-oMyRoApEeRPllUUyvVLVYAZq28dCvqxzu5gFTGwOqO4hKe1ZaG33sF_VwM4UV5EVzeDt0kwHn0mpkA2-W0d20_cbZI9Ea-KV_rVBtvF4Yap2IXG_Qu8sdNycUyNNSqfolW5g5ma8F80quynvwlVIY0CiaM0xOANsrpDSI1eBxxTKA6M4lCJGCNZh-x8X_OsiZBqCPapstV_zib9KQEPi1OY15LOGeW2xBvqpgQqfykHHISLWjxR7rKIakJbM6DnjP3aSla_mtzmfIU7nuRv88bE-He067oMYmC0gEw9kuwTip4xKtasuxpE5Bjy_LDDVlnDhI7Sq-c3iDtOPqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLiZ1VR-Tfv3Tw8m2Ga8C4JyHvmugC5dlS2PUVlRY6A8e9rFDts6DBldXStz2PL7xOgjLy6ec_BoChGx_Jumv7S4BEETWIJ09mY8EItjx339XpBYBs_IooIzb4VR9AEJF9yuz2UQqkTgwzKgQBN8U0pqtZEYpgflMNuYOVFzw7jeyAcUpIipPu7lbMpJeCI5PO8SmL_Ybukrhg7wI95G81Z7FKKcbWVgZpwjW0xQAgoUaWBXlc9gxFsW3s5V-0bVDo9sG73MNRJeq2sbbYdf3J3FW2y-eWVjgOPTd7uXdmdOsnhxzBLtPk5rSAhf6k4cBEDB-6YaHUTBFzI_NXXltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=G4GHa0lZjRb1Lh42kYHJZLFWMGpk4vipBX2ZVZJsbEB20LVn4RGuhNvJKeo146NewLAApVgr1Hwkf5JtGTXrWBoiqk14XA_nU8ABLDcEcMXZUY44d2c9Q3d_l4TwKgCcR_LszLjQer_a1UzDoKyMId-aqNRantFv3PQVefQV5WDFSGTyM5jzq9sVqbXUeyQrJPl1E_yCPaQs8r7RV8aGPDrF5uk3XF_2eX6o4PMPhj7GvPZeVtym6eGk-FXRXV41ZVSIPgI5GnHT4v2arppvfnO2LKE2Kwx8WuKTR4HoaMyXcLvglev8IXnNnXxE4HXkAiV4Os3civCyz81zfFDlLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=G4GHa0lZjRb1Lh42kYHJZLFWMGpk4vipBX2ZVZJsbEB20LVn4RGuhNvJKeo146NewLAApVgr1Hwkf5JtGTXrWBoiqk14XA_nU8ABLDcEcMXZUY44d2c9Q3d_l4TwKgCcR_LszLjQer_a1UzDoKyMId-aqNRantFv3PQVefQV5WDFSGTyM5jzq9sVqbXUeyQrJPl1E_yCPaQs8r7RV8aGPDrF5uk3XF_2eX6o4PMPhj7GvPZeVtym6eGk-FXRXV41ZVSIPgI5GnHT4v2arppvfnO2LKE2Kwx8WuKTR4HoaMyXcLvglev8IXnNnXxE4HXkAiV4Os3civCyz81zfFDlLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=YV_iJE22RFQnqOYZIsIU_AMu-lV6q0trKuZ06-uiEyzVGnt_O1r_1Nki4LRnQuuSEuLy3XTGkjTWW_l5swDZS4xxBcYV5SOli4taKTk4bxMTIzm_npQlRMeCgBAdWvc3vKG3f255JRYosVJimlQRsWFI3uq2HPF746Bab8-5Er0IaHLxZFtr7ilsp3If1lWmpaZfABHC-GNpR0ADQt5Z9AHttm-3aXVDarevUap2pGxNHWKy6l9qW6S11cFdeAl0m4jLITDQ1tC5KBD2qcnFzatnNFtoDIHGhWKmTbzdI4PiT2oJSte9_WeHh_uUi1ogI_0nDjz7yHhn99GVjaHIsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=YV_iJE22RFQnqOYZIsIU_AMu-lV6q0trKuZ06-uiEyzVGnt_O1r_1Nki4LRnQuuSEuLy3XTGkjTWW_l5swDZS4xxBcYV5SOli4taKTk4bxMTIzm_npQlRMeCgBAdWvc3vKG3f255JRYosVJimlQRsWFI3uq2HPF746Bab8-5Er0IaHLxZFtr7ilsp3If1lWmpaZfABHC-GNpR0ADQt5Z9AHttm-3aXVDarevUap2pGxNHWKy6l9qW6S11cFdeAl0m4jLITDQ1tC5KBD2qcnFzatnNFtoDIHGhWKmTbzdI4PiT2oJSte9_WeHh_uUi1ogI_0nDjz7yHhn99GVjaHIsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6tu2EsoPBOM8nEoVDHJWvNs9jnQfViJupr4VLAutCmgKTcQsiUhdm0e9RK5XBuUB29DEp5Yr3KGF5Lsfvex4XAuiPuEJ0oM_-lBYCmlTTEvZ3O9mONdFVgOZwcXDhAaHKU8tsrGUYORK2Gpb0gkk6unGLQIbeK11JCeUUARyNkZnn5fPVwLQHpC_xfWH9N1Gc1nf2enFTZ0ogVj0Lov2naCai777DYsFlTXPvxlhK-J5FuoVUY_SWUkdtV2yw5r8yzsvmdqjbd155lyHq-D0vbo1zZU-kfJfcU_O_HkONkGbXYOKVbhbLaEHFY5A_ewpMVJLp98rhauO5BrUSzKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrHM0L3jtCjI85NDkepTAZCgzky2Xhc3QGjPHsU7uAgh8Fv0YFPcSdX2KYeMGxj-Wqb89SBCIQnFQdGyFJFPQ0WvEtRLRx5CYKfoXzYqKRjC-FdSsW5DE-3ghm17q_fdZ0sS6JU0bw13cdF8KxamE_9isUKV6cRfsgKDItFu0EJOb8rdrNuAc6Xnsvv8AXdHBGBb2qDrcspiFhA5hnvLm-1UZJJAvjCG8RDmL_tc9NF0DCjjklkwWikfX3xTzGg3WwjRmB93LndCkp9a1HWAqkBZ5165HTE6XkmMTUrxwjTffeLUwLZUe7X1tIRtdb_RVueSnv9Dj-liQqBauF1zNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdtkMz8GIrk8M9k2vS4IZITPWzXTH_x1ocI4e23cp62Cd1gqP3Opb4K-3tOhUP7IRBuncrRDsX27PeNdsQKFl0-cS0sUoFmOSlGVtFjc7Vmkg9njdHupD0DJCb5qqxJZKtJHhmOuR-vI7nFFRUEPug-aFUZpt8jf5yhtRtdyyibNf1zshPVvAv2yqqakHO2Tm7hvuVZfV3u76iITVMlrOhEGQKZ9JqTRkwGxoA9nYFzdYTjfCcSr0-HrfNUjSBmYISDxI8Yn0dKeHRvhdndmgulMsiKosxoiKE4WGB2ANDrmk1QcjhyVz17Iol0sNdAd7N6a0-K-CFvkv7URKzGlHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvl11DPGVsVNpcyN8z0fMIrDQN68JNWeX6f2j7QguWg3LEw-uevKgiGWhTcCBBIyPtIyaMbhYnS2wwIi7oRXUyfBWYjJ0B0YYrFiw-PrEj626ZgcYtLoBM1bXCcqfAkDZYJYXOZAL4afH1kopdOG-Hq-wxd0XW_XR10jHl-3qVrivD3n6r-PTV1rE-nAC3jl1RvDyl1nK7P1QgBRdaW0zKi7ArAb1QY_9UYZOHI5n-CF4g4xtUCN6-ZWnkV7IR4fKrbPhCxMHTyYwqCOvakmXkmiMb1mgISo-UCSwr1H_eFdMAaEu1EOieyy8Ajf7yXyRaTtIMj-pTkVgfnAcnXe9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGrmZfquLpe-E8WB7Tsc8O4aoLOkh7F2UTn5HPtvthWJbzp9P46mHoK8b133v1Tz37fp11YbrLuxYFaBecrHQ9H2u6rAdhMbqV5mXaIGhglhkL5-7N-U84hZXfFVZTXya9eGdDNtOZtF1C7GmiJ1LnTV02L4xNZEz65hmdtn77L4DqD8YbgrnXUEJCI3Pn4uRFAp14gLgkVMEzas6yP9anZJbEo0zLXdAlj-pmhq-IS4SdgXy6T5phqxiit3-WBUtZGBAjChNIQplU3ejazzADllOpQWtzjIDLODQe39zlkhEbNKACN9Eq8uOo9-9io3vtgFrUeBVaB-Ov2WVOhNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qN4yQfIsXWwLvEhyKAQKn7_JDMV-qjrdHSUvsUUMEzv1tcHhydqGgLb2krlg4YkNq2z_T9_9lRzZOTfmuIPaoR4dOXfgugBVpwbkpk1_eXZQ4fU_HgcsW-cgqz_1pK6RtASmteX6i7svDL97wql1_nKW2GDx481KkCQFQ6NSg0nhDlRTVk2Us5KA-fA88iMa6zQBlL_YS82ZYEHE0IGVObYDqVFMzQraRpyYG0Ikk94h9RAFK-rmn5tTKdGKaKaylcyiKfqUo8FY8MxRl5A_iJqI8c8x7gdpTgZRYG-UBKlg1CMIDq_v7t0VjexgACrCid5tEm0TSjdkNGPE_dra1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI0ZFaf9nf4xKH0o96wEq4SR3foNBftsnFvsAoZiYf7NS5p_2TGd-J9KZVD-Pv0yq4Amu5_uY5jpzxvjFVJK0wgiYF2irETRm8IMVi931FfdbS32XVdBpP1lIXZ5Ix9GJrFW32Mb1wSCWDRLUI1X_ygnU87w1xSQJOedxnxAcVo3c--ZTZztLYFu8ztwYsj-Kwz1tZGrvdxuPlBwmgzUG7hf9zBa7p4wlJar9g5x1TCH4sQjkxA_32C_kRiIYZ6RXKeciUU5vs4tE8DEtBqqGDJvQ5zb850x4P7YcntMaMjq7I35jEfxizpeRTluelwHcTzV9OMlI2Zqzclo4rgn2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFjdgwDIdiPFHfsMSrg3ddV1AecceIitRbzGb4_DiSEtX6kp_UXMZLY3YKSzlTyWGZHxt8RzrZBECBV7szp4SdvWhc75c17q8QcalQJwNE6gUelpWV6EbBIRFmpIA1211o_kkCmPVsI7C15U9fKDfvj1Ek8QeiOVLMhwWGPnsthf82A83P3ewVOnXWp0dhFTjyM_g-1k8JweslrqglkdaLKedPsTFOTe2K25JhTp_LyFMvdDH_fXLhpdhzZmxStnwLU0YdpXhVEKD7R9xKJGuho-aQSp-rL_7tbum4zuGUZZY6hQ5muTIiPAAE_ig9-dRKD7K9vqepNBvqKv8NxiHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUxDAzr_QAOWCdV8ipzsfNe087weOndDOiwr2kjAxYnUj1Ok4ExIuul99R2veIbJJuucHoW2_dSnhuAvJPLMS_dv5Zm7Su1-cmskl32uXgF1ZzSyW4KhFDlXRajDjD6nPYKfxWsY76MUkG8NvbBpYZkUDvmeJZdFHiqNoe5RHJ9b0UlxfRpLe-Om7v7SrFZyJ-WUxkrP6Al9Gg1JhM3H7IKOiABpsYHpScxPinTqv76TaLAjT17q_uj44oDLPxevpRgPyPCzQvqdUbe07Le41Acvd7k6qeCDMFR1GOHDMBlIPzr4eaeUjZ3w8jUH0HbXqVZR7l7RGcoIUpjAF9k3tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mb6BwqKlT1S44OUMttFN1WTA8KnrYbLmcTI-VgFhymWt362cPr_zLa7REVjFjTbDcz-ATZSfrPFfegX7nAVg59W_SN9c6Hf27aqkpgVf4S7P_mE-qY_v6gMynGEf9xju7GyDEnjDQe_1UMyIvvglaVuR97QObwlBOZdcMKjM62z1aZl-FoRnA_5tl8CbFZNDXWERRebzbQfLCk_97ahfP843d6M5JfYiHpA9AtAoSA9QmW1RhPWe1_WXsupsLRftghpGy1rBhxUfX4ruyPYrkJ9NabvMO7L0ABLiTw-I3seu4h7M0moamWj66ViX339JIxoeHBwTzj4qYEu6k9aSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4rmOk-TC_x46LGhrnQSf8CuIlPpb01yrEEKQR4bhgsnwqhdiaR-OCiDK3Q1EN3yJ11rDNUFq0bLfqLePpDUQoSYdrwygoius6plbblmwRPReIcT3KXLfeEj7l_qyGNsAS_xWMtzMxWe140_OxoARxE2T0s_ZNbHYGC9P77Q8ad8SUtGHssEWrT4CMJRu9YKUnGY5Ixu44i7i0Y60uLy738uUa536TkE3fnpROnoOsx0anIousOxvxMdQPiAnkcXzAjV3s7kqXLAfUbuiJR2NLrjK78n6p7FqBljBDgKcOuveneJ7fIEAfQANn7HfskyR4RnwW5C-z0eqZm_ah15aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVnffYtldIDClr6Qu13xoHRc1npJNM0qy44QWJDvsci_D0yEUF_2cEzFbpHxvbCkHH1_iEqubciAgh0TTWDPuOhOii1eMc3ztDXtBNc1ItxLGNBRQn-c_a3aGJ7VsMIgWZxYUGkUNNVKhn4V0s5ez-UPS8_9OQxtt-PrvRinw9n6LgjsrBjLW0PxYZnoRzfAF2K83fxtPpLXG0jVtD48-goJIy8-KD_w0UUXkWzfjRakSCqS-FDuQ_5y2lSJEM9a_wiL3431xmiS5EBp4U0Hp-O-_7qYVWW9dONHLN3zAhcKxtwiK_BNkfyQxTTlnP-hFzxCXt2IghnkHX1xoA-RYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfkAXlgEE6QAEMPN0w5qOwcAljMg91DExraMkTeRmZyboy97ForoYncSp9Hz6KWUR5DHwAoNy4UeLlVrRBQMUqD2JUBidBTolvUz0w1dDwWPVScpBt5KaVwmDjrvYRw0jp6FSR81VaFwjpwaVFKPT-CyclGdy_uLu0j89ZjJEF0ekpfLaSJ0V5Dc6nGOvzZnySLeOZIHEUZHY73StbrE_QuATRM0PhG1i0--9hp-DB9xlJA4wX8hWk4a0vHCCMFLlAmdAbzeVrYnfuLhyI4AtXYMpgR-hjQwZ4msHs_6TjuUDCWfzCrIrQkeXQUXfee2PzosZSfJvC8tarzA9r3tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxa5SRqb7Nrv-3tviGCYoR5sJSPgAg3xpPFd8amabJDt51KLmfdjP4QQ1JH8DdhN5zOQQBP7H-A7yihwT7Ge6k__V6JwArBn_sHoE2r-goM7iurS8T3fbnGkpxIJ8PKe5hUmy2GmetqWKY5OQErmYqd69nW_PRuVLUhJkLKP48bcfZYRTmZoDf1Pf2UOklfU6OFzwmvMTVM9Vke5qJODj5pdE9OOa484c9UnrvbyvhrGqIU51kGGyIO-zvFe3j4zml89FKKoOZ04wG7IMW0I5FZST-qJv-yzsILSNEQ4bihkvvURCZfZuXE03L4SnQQIbfHhjIP14fQoZr55pwP1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxf0NgG2sfivszl-5ULvxkufQ7uDyFUkixxHrQY6MeMh2n6VEk8fqa34vNiEOuf4qNWeZfL4pTh4a1RG7iuooUy-hSB_uzwBuJNzx7rJgpFTXtP8KiALvWL62EK0YI7PNa6JY6QSA49e7AVD3_f8TIYPXehmeG6hEys_CdLzGJttb6sw5Bn4u1CKXN5YGjKQTmV7Pxoh4bNcemabIklwEqOozzGgNX3tiy4inYrdfDkMPJJKbfUU-YacorOPnwQrcAAVVN0KblGni3PXpyR6A6ccaNgWbXnqGUskaB-cbM9Qv0XFlsFJEhKuaSDcDEZt__UCLsra1ym7qTdgBMZcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=HoOwBy8g7her-Qu5zdG8mUERIs82QCpWN7U-_D_sLZBVtD4iUg9exo-GlQkYRmOySkCgreowFK6TNa5jV8xTrcH5Zy0KUCxHfnu6paw7gWPKtTnjvFrTlnanNR1BhgkFUEloQP-bCxEwU27r1HkEBdBpRM54CVU1lh0DqbWLNo8oM2EUJPc2CAsy_L6tfm45SSjF7FdhxfnHFyTUAhNYBijOQ4HN8l1hwCvrWVJ5mXz6eCdf9SLjjeXAWtoooglpcv17eJmk-LiMQYR694LFoHynWByH9hsg1Fh8qhrXIYugv37aUScOTlEVhe12yuI5A2j8ErssjKQcz6OTB_bidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=HoOwBy8g7her-Qu5zdG8mUERIs82QCpWN7U-_D_sLZBVtD4iUg9exo-GlQkYRmOySkCgreowFK6TNa5jV8xTrcH5Zy0KUCxHfnu6paw7gWPKtTnjvFrTlnanNR1BhgkFUEloQP-bCxEwU27r1HkEBdBpRM54CVU1lh0DqbWLNo8oM2EUJPc2CAsy_L6tfm45SSjF7FdhxfnHFyTUAhNYBijOQ4HN8l1hwCvrWVJ5mXz6eCdf9SLjjeXAWtoooglpcv17eJmk-LiMQYR694LFoHynWByH9hsg1Fh8qhrXIYugv37aUScOTlEVhe12yuI5A2j8ErssjKQcz6OTB_bidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbj93Qxt9FopolC3zuiwEbDaKbLL4qh51d3b2A_198BjVOg19tTtCam4JFlSVKD_twy5xoW9UA6U32pnLKxmKsfjbKor_Gy4jkUBwWK2OgJIVRB9Xp-xBxdRWRZHWe55d7vApjJxXvXwLig9D0jF4iUrgkJRhlOLIW8SFc_9t8_cPN8yI6PIv4ZkeHOPpoKXwklYDNd-oArKaAfWt5g_0bUAQomlolJr_Lrk9gtktCleHYz8VIwa9AKsomcxK_B3lqxW_wtkSaLAfqyzUWVHN_yVlvUmcUwBv7cTbzk2QU9fWfivjAfIfAmYtSnRpGez_e7W2GMRc7wbvVFKlJYEGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyRQY5wHGDyf6pU8s9kYJy3jG_6XVU-5QXKbAL2jrsTbfQLn8MyoduHyI_fOV3mAxb1dmnKeozeDM5i2x1lgrZQs0nqFGqkp2ytwvqeNmyzSN2cMFxv43r46GqaRfAoTf_wsCiXc4_n09XJDLE_e6LbH9F1jsgu4UIXfFGmOzMGdIJL9RZsvvid6zdOHKI5C4clHzzJPWN8e_WjFV26klZfZniLFD88l3NOom0I-mY_dNYnnWu15DvJMf7qbPpC4uTCOYhUB5a5NxpPyldRnHNrh-JzVr_XlJ4tG1A_rv0XBtA9aCJKHX4DIUtQGMDRoUhBhyoY1tsdoBjQdOOEfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeYM_bzv3k_QC2RQPg6sc-BMcI1ukZuxdCNBgk-zsCh7rT_WMdhCzr1r7HRBgB5NOHBsWxF2iZTLVkV05Jm7gq-xpNeuiXmWvgu4K9GOti9QlZXJZJr1zi-kAibdWpdCEfyO05C04nwyiq2Uk9WgLqxr7hr5UZluzn3jQdh6awyuYzM2CYKsOVaCHKmvtwRPrHwbhTucejnGsrpR06_K5aHs28OZZqGE4TkW4MjgSzWlnJMcCMG5uQYsR3-rm0mwUHvagJFRlKUcviLdtCz4mpFZPOGS8c3PPxzO7QpBdqdFES2qW-0otzHjR74fnnvvPcB8innyJLUpg9q7WFSAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me7Dqi4XKnklhcyuBLcT6dHzoXDvEJbhJIlvpHO2nfw-_CVjYzqKpGfIiHpJklDnBR4JK1QGBCd38qQ63wsPVnQQW1Og8IwvQDIYYGh4jTHArq-WH63OeNWz6e7MgmelI3Zy6MZf0AHAAWa382I5ovrZLDuI0QordEnqdpUQbNVMhVzaK1jp-m675vEAixJyYROnnRLbWgFUD9QNTFShoI6zY9SOb0-OXuA0gtSDOPvtqM__txj898TNKgOyd6JRDaSPjiaUMX7keZ5TIvuGTPBYBX5uOkwypsXyL2OC0TQGlV8ZaQ4ItovFobDir79Z_BN8myrjNbPtCM3YWF6PfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKLd_BwD_1JEbALyLkNEONIxl8dKfy_g38omKnsLvuqElpWba8Jc6pudSpUIvfkBt3WOM_6HelKrvAJUVLZ6N5CUjKPhsf4rieKGahrIbyKqrqlJY5PJ1UBl9vhsDSAiNRCzkV1VGOtKYZ4aFn6oReci0xQrTXB1kutYhuh8zVKQGo8LTLYSWWEbSX1RZaBduXFbtmlwJnPv6K68QhTX_I2FdzS4tmokGAzG37NCq39kp6AO9uTO7bwZ8MJ2TftMjzJNZzgFfW7sfzewmUIkCqgcHmzHqh1axruc8LhXORI77xEc_RG9FYwGTylWhNBKzuxBWRiTNH6NkG_f8NqQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=pIqixkx9QLYtJ5xUuOQXPEd8cuv7_RF3WDIv0vqShz0A7zO6ksVUg-Ia58S9EmvyVGBQYCb0cHEliZzlYwLXzkDyAF0M4-J0hkO59eABEwmqhArTQf0oCaqSLGSqo4hitLCNxNTreLm8NXHrw4IWxqUL-iqUsc6pglfxePB-jY2PZVFC1ID5YMAMb32VfCwlNLzExIvr_GmRM0FRh4plsYDLnbL2NO_2SiDXizioPf6iIkqiikVpI1t0EbQvTQ2nQFvyMWGJ2AJnOL-tURyeCCKi9ZA1CwpAj1cKELaKuH6ja6f-955MI90kb5larVmr-LCFQxeVoeReQy2Rj6Y9CacMQ52MH1NBG2tXMLY8EfStzWhTb7xvJ8d8kYqnGl-eiGf4mrpNHRKQFXR9lo6_-1IkcNW6VcQTQKHqMDfdSKwXpGdUb9PduEuO8rUKO-9QpKNgkdAggV22Cvtob_tfg7yjkl7W3_er-vMny6ZHtJXhs_qoZ6Z0xrSxUCi6brMf4gydO10Fsu0FMfu7R1txtusLRb_EY5WVOq2tm0LNjg5boNqyisXCTOh-E3vrQUL9_HvmRUawbtIH_fSr9iU2T-ur9_rMOjKtbm6PCrO6wBLHuV6Xfo719lUdi7BO60c3QoU9y8DIyC9GrOM7Nf63PJFNiHsbT-WzPelVGDEAvx8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=pIqixkx9QLYtJ5xUuOQXPEd8cuv7_RF3WDIv0vqShz0A7zO6ksVUg-Ia58S9EmvyVGBQYCb0cHEliZzlYwLXzkDyAF0M4-J0hkO59eABEwmqhArTQf0oCaqSLGSqo4hitLCNxNTreLm8NXHrw4IWxqUL-iqUsc6pglfxePB-jY2PZVFC1ID5YMAMb32VfCwlNLzExIvr_GmRM0FRh4plsYDLnbL2NO_2SiDXizioPf6iIkqiikVpI1t0EbQvTQ2nQFvyMWGJ2AJnOL-tURyeCCKi9ZA1CwpAj1cKELaKuH6ja6f-955MI90kb5larVmr-LCFQxeVoeReQy2Rj6Y9CacMQ52MH1NBG2tXMLY8EfStzWhTb7xvJ8d8kYqnGl-eiGf4mrpNHRKQFXR9lo6_-1IkcNW6VcQTQKHqMDfdSKwXpGdUb9PduEuO8rUKO-9QpKNgkdAggV22Cvtob_tfg7yjkl7W3_er-vMny6ZHtJXhs_qoZ6Z0xrSxUCi6brMf4gydO10Fsu0FMfu7R1txtusLRb_EY5WVOq2tm0LNjg5boNqyisXCTOh-E3vrQUL9_HvmRUawbtIH_fSr9iU2T-ur9_rMOjKtbm6PCrO6wBLHuV6Xfo719lUdi7BO60c3QoU9y8DIyC9GrOM7Nf63PJFNiHsbT-WzPelVGDEAvx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=f0TpEnnFOudVyBZOA2K5Rnm07EGcxLOLETOrmG1jn4JozFnSqXtl2yP5GmCCxMNuZ55QAVMBB_9v1hXZZvF7KioG4jwoIGaRdd3hVFOM9fvnTVAFq5kbQLjMgNYi3N4Pcup4yW4fC5mUOXdVgOhwU4Z3OMzGz6qgcE8Q1PT1AaNrhijewihzSnwlwyl7GAYzu1XtGkc7LqBcnY7AnUvsmrkmckj7k-lGoZbTpWycg8XvHNqeg3h5MO6eHJtOmWhun5MhX9gt4v2cweGTxJVeFe5h3-68YWlAqxiIprumo2jIW1mUKiczDpjlfpBQj-UdYqkvcUr60vdqeM78qhuol00D-6rev-37SX4l-zvMy12-I23kCtYedXu_B8sWbibo8j66XUfu-cjcFp23L8vWvd6u6t1DiCGzdMIazz-ckOXCo2iluyiSyAanhM4HZ3ZT_VAZ-zs_9hkdNf1w6L075aRqEsMNN1mjc9S-UP4JSVN4zmxxtVVTflFNMZKrHuh_q5VfpFv0kRxkLahBHrnNtTNle-3MjMFFRHsLl7oOAFzLwH0qy3jgt8zP_9TnVlMaFbqv1dIHb9296efLWSvF5UNvGc3uKrTwCBW6hCRqGraHtubjZTk_2uy0G0wUA9rBD2ZfHY9nIvg1MiJxnUkUfK1cQammKQblSfUaR0KIDZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=f0TpEnnFOudVyBZOA2K5Rnm07EGcxLOLETOrmG1jn4JozFnSqXtl2yP5GmCCxMNuZ55QAVMBB_9v1hXZZvF7KioG4jwoIGaRdd3hVFOM9fvnTVAFq5kbQLjMgNYi3N4Pcup4yW4fC5mUOXdVgOhwU4Z3OMzGz6qgcE8Q1PT1AaNrhijewihzSnwlwyl7GAYzu1XtGkc7LqBcnY7AnUvsmrkmckj7k-lGoZbTpWycg8XvHNqeg3h5MO6eHJtOmWhun5MhX9gt4v2cweGTxJVeFe5h3-68YWlAqxiIprumo2jIW1mUKiczDpjlfpBQj-UdYqkvcUr60vdqeM78qhuol00D-6rev-37SX4l-zvMy12-I23kCtYedXu_B8sWbibo8j66XUfu-cjcFp23L8vWvd6u6t1DiCGzdMIazz-ckOXCo2iluyiSyAanhM4HZ3ZT_VAZ-zs_9hkdNf1w6L075aRqEsMNN1mjc9S-UP4JSVN4zmxxtVVTflFNMZKrHuh_q5VfpFv0kRxkLahBHrnNtTNle-3MjMFFRHsLl7oOAFzLwH0qy3jgt8zP_9TnVlMaFbqv1dIHb9296efLWSvF5UNvGc3uKrTwCBW6hCRqGraHtubjZTk_2uy0G0wUA9rBD2ZfHY9nIvg1MiJxnUkUfK1cQammKQblSfUaR0KIDZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/shhb-g68iMXPHzq3bllIHhVMe9zBGZGFx1tLKpmUkHaUd-_BVP1Y11H9UDuNoya14hbIuwnNhXfD8-OIlfFmWUmpMLdAEGuyMcJVEyLJFVhSvj9t1rEMqWcOMWH3GcydWws95n3CmkilZ_5juRp8CcM5NPsepJ9rWNTbTlEDMbuM7CRZw0xGgKQ-1NoVhDXB1aWYRCAobNTCQigJVUBwiWdeOHy9NS1EJoXjIIj5yDzwzgN550EDLQ6q0dM6JlkQOaDtSgAXkFPoquhgSW8b1mY0rpWmW78kUyI-VLbvsfKBXL0RUbbOfeSeRR1QNb90vpXKoe2MvjYdxCVpmY2PKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrujnzZtj1L3AOrLGGEtYsQf_SrjBP62eIJj2fcIWpY8JnfTVeS0lFyZn-OCnYdbvo4eU437qz3zXlh8NsyjrAtwNyBZIUwAxm0n9xDKWYHizCuUfDWgr2G3OC9TcIRqk0LvxwFm3jt3o6AfAEHaEYqRSoJhFH59Ejm3ycMwRu77vq9j080qLgdSdh8ciaaAtsaxMamRYMyE90J3AdnLKZmyoz8RPeHxrEjhaqFnaxg263a-QjMhZL-IFKAJ6iB_xNKYcb72Zgwc9c3vMu0SNC41suSVShFFiYqzSOfUgnmT8NFnt0eymaPfnxqeVTPUAtmrAtGvaP4byxnVsR3PDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amXgJ6SjTjP4fSC1XmL8nrqzlJels-vnE0ADsZkoubl3dXrR_w7kFQcSpKRMIHiHZRd07grReFmNVyUjiN_orVeLt8xcWlx8wElqIn5JxGiQlm83LXqk_wpKzBDZTex9rUKDN2CTlZwAmMvOXXFBN30HzXlQ8wNQs8IyfPlACZevKGsZu6cfQqb-OuaGBsHySPaFwxpKFvT-xb1TBpROJm8K7O6WLEc7OrsGC7MmcVh93U0kkDMrPaZk7UZAQ7Bb0fVeh7yNivnjLhPbutYqkfu3b-lBiP-tjlqPzfVUtV32JrzScaMIpuwdC3oDrHAQGvQX_Sc_ss48TEd6k8g81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMeD667AhChM9Un6yrpOcm3pGha83aUgV7ILfsqogr9BFjoQPNp5j40hqJ2_7RkCecRmAoXpqtEEZY-s-_rIBxDONv6JJi3FD8_IXtHUUKkl6KHHn7dpEGm-gBfbS-mmxxXyo-SZntLGs8xS_RRR1KpcSZg8Ov4BPdO27QS5HICVv5GrcJq7-sO1-lazt-A5nx85z53gggMufUVd48AkqMSke9tem-kZmcYQXLvJBUG8mPvQM-VHlxyPQSYK5R6pdcjCzdSbHylJ3ntqP6i5zvGSmZl8yKDIZ__vPptGXExeoiGAV2bf8njs8flynWnEv9t1SQVUrS-cmEicy_IZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYG92_yQ8ETy1TOI_KxQ1kqRToG2DZO_EcU-fzsiJC2_Qdsh0piQGTJ_wbnkya67g9FAHqFskdwpfz02XGHxGOV1jMhaspNV3QxPQC5D9CbfjaY27qjIqMqKYiZZWSxNkm8AfD6LsDcV-zlFknYNHUF_oozWH8wIXvBB2mOPIpwne8F59jXCeIjHxvU4jdHBxjGNtvmimjq70xoK7D34H0H0bKBNDKeUD7QaQbiXdNZ8O3iPeX8MTNGJokJ9LrXKdyB4atRv6r56_CJwqSJg_anO7mRFPuO20lUqFGRznq1Tw8ci1CIeegpe-UpYhWOdcDWIMu9sqJVzkYhoLCC0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFF9WliKykIl8YgAz1amVVlcPYv1njFKFUW37N2fg0Uw7huNBOd3louba6zDsoDnmi5GkKkST30jEPQKdmd8_a9XWGXf6j6nZ5wyuJgudBAlM7jhDRBTNFq_AVqteswWEo9WHPZjyaVwVYZ1zhnb_9tDwiV8x1Sv-XadtiTDwz5sxn86ieAuukE8khffXt0ThJLmMQwPN6WPZoFW14xRtpe3hGpPz5n61VDaCdYcUaPKgJPnxcCC-K1phQcWTthG-VHRnEDfIlgNFC0vtT-Hne1lVP0CgflA4wODBNNoOS2eBX0_rz63GUZYOz1HpocVXfoZ63A7j_Ceph9kf3lwKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
