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
<img src="https://cdn4.telesco.pe/file/SiN9eppKdy9R1kn8dBFFCnM8_cvFJs8HQu-8gEu3qkDx-yCd-lG79BXgGKubec4y05PqcldMyA-n4hXF1KmzpJX_BtSKPNe1XIg9FUxTWdinNI2Io8goKbbJBTPExYwYe_BtW813Yqn1xxs04jSLE626k2GR-sQ9ktsHSkh6yeKGdIHlr00kVGAaZa6Fk99g0HmQ19GcZA8WY8b0_Nt53TTwZjOIjhe2WrMIzt2W-8pHKbJZBrxuX4vratI0b2R-C7ZeD8mfWrziI_JXXCMx-DHzvL4WyQTJiGE2O2gvfpF0-Ikr-b2jwOKMs8XW3_lew2YgakyGvziXKnFCSmms1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 221K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 10:56:56</div>
<hr>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxume8HH2NNDee5-mJYJRAFdz5U4f8Y6oguPqhqwKZvxbzrJK4NSY8oGBVTxSMgiv2ToE1GYUnIH3bW-uScpfWB1vaz28lXMdKvYncDjrmvMRPEdiNJR7b1Fc1-tfsSpI3MIp0eVVCP8R8OBPI5H4ES6-aorSIKdDP8SsQzLfoEVPa10-3f5bQP2PLgL1JJ7nv6W4bee-8YOXB2TMwA2TlAzySAqL3dNV2Ipref9zDvpLtYf_U6je_W0evaDbJsyKrKqccig-1JWaPCFhJ_-hwYjfvXsmud2U4iqQ9Y3fSp6n-HNrJBSAgwSV43jroyJikCzunMm2nKZFnk3QzSgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q3oZaR4IoC_eTCmLJQ8eL4COrulmtxfhhkrSt-ue9dHhipCxJguObXCt-p9jgNyseTV-Nx4Hr8AgLEHfwqhWpjoqDttWpE3JWfDxh7-y56dWuUX2FP6i8hMZT-dufDc58BBYRvHHdS2X0HwHEtg3LcHgsPDEvyQQWHYzeSE4LpcmyKst184e8yruE2KLSS5ZIsNKs1pZ9OQ8jJdScnz5IacJycbD6_UEdnmYGqNtqT6ohCV1HCzISVK1iTacf2oEq9QVR8JfpVNRYLy9V5C8nN11mN_mMQ6iesECwRldOsCb3ahaCJz2wFFMshnRKx1TJuZX0EBHtCApYarG0DVrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K22jwwDldbwtS0slQbKl3JK7R-HKhOMBITUppR8GIb4N6FjPq6LA0QrvL2PwsBthKouqgjfC0bV1v8h0jNzux4d2wjpMFl-4bkrIA5lW94QegcCYcexfzRrEGnQbZHVzX0JpkT-5nQs9H3VHvRhBEVXAURgdFctnJzqthIW2e0p4brXBaUA2gtit8x9xJmBCzbbAzxtwgp1VkgkkDCfBpRvEY1fNnl3TFYgF3TINY8N5wdauP1QcHl-8R55M-d5c4GZ0ianioa3EQZ_fyDxi2M5LA3aUex6UM7A9r4-iZ4m9lDhjyaah0CBdymJNNtBbHjpz4GKOe_wS7wONcJHXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=l8KoUBG-1rZskEZnoPvOCnKZY2Yf9i31bjGY71V4IBFAWyOpLfj2fxJpMdT87_oY04ew4COBPy2tI231kbv4FOa7H6EFLEocivhDgU3S4i1nlD3czQlzVco7IYnmj73eIJVAvOlb3Km6m9DDOJ9ohciVbC6CkIuaF91jTlcprryvH83RLLXpCpqoBdBDVe9iOzxd4C_p7wrSza-ysuaTPdv-YzgjRTIXwhBMZGN_BTVT6P20jiQQ98P1-H0iAYNCVvrNPK6Ji5J2-qntcWfvfcKw9l-ChnJIFyCRfr7gR59-n0OhcLIRbPhgC-_VocOTczxc9pNjTTSdyhDJZ6SIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDvExEj6VyEL5MQn1yCKVV6x1fr744oWSmzzRmKISzQWR25outQK05LGQKSsmt06C8LtvzJQVNY321hlCZvss6NicRHTlF7H9TiS2znZ_v_MFWuT7J9oZZn2YNhqyRgLaFkHiZzJaDLi25tJLC82uwiC-jUqOaIwBHtqRnQ8oAo5JsLIkUXWJNW9nCKrh5sA2EUMjTlYTt8wNqQEW8mdmUJ5YoRmXGSBi27PwBhnzpg5cEPijD8QacO1zQIGq8OhLZP8BBi-fgUMlVuZLcQcGb6sVc3FEkARxqx4M-6ZTEIx7QiBahuWvWdcJ5RqQImmOilyQsmEBK1qC-Bzm5Z9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=d-tvcjSb541OjzLWNl_Wq9yv2oSG5SnFUsJDwZKl0vSWw5fS0vFhYt1ZsehRHVCuRuGkzrrAMSNq2FUJOOyqYDtfNrK7WTRR2SQd3SBqpXjoDkiVv3NW1uiYSwdVukIwvKtZpR-cIamz_ka1oFrvOegrrBCFCIcoQ68DrYFzOdmUWQuKtMPq3gqoQgzEOEm-LMxFjdLd3EWRf2iJk3fcFk9Tdgr8zziTLH4JAJeq8FSiWBHmkgsRMEk8M5Fjq6KP1WFAyvz6s6qhVu2YGGwn7iBDLZNH2zA8mJhOVaLluUjIIMfYgWqrmHZpfTOhvaT1utRjWN8KYorteJyA9WXPJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=YsJNtsijSH5HsjAAX-vphUBD_zABDgOHlEghH6fJsx3uUZs5Nf_kcQuIBD0dDADFXos65cx1FYdTcrwOK32eYO-P_Diby5479BKkuSDbZDH4twB9fMaYWzhFWXeRhutxJ7jy1LtcTM7p1YdMambz0rXaSIc8bM1e6tXx0oq_6fDUNEgNcYeQNZcyI7AoJlLlRNA97FFLlRyE_vOyd8-larRf7ohfHZSojYexi3H-xcW3-qFo1WTyXV_a2PbfFbHuxqzrefDOXsZwufaGaRi76-NUw3mTGD_Wh1ReiRU4LR5cq3L1RWnItugAVJ1YQobARNMu9hV1zx_gavpVIYqYew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=pWauUwj663Q4TR7N8Jb6V31XaaAjt1DFZ6z0PLWy77S1DJdo0JCL6gcJyBi1FpEAKipa7L3uDqSG1EI7L1wmtqRzWKER2uyghqKWJT8X3Z0N6QdJkZxGPl_pYJDTj28IOhHWCMMJYlJkdCV7Mj351e5YwOhjIq-4jrWyuKeAvM771Jiz1oET4jVOFb5pXKQPFvQvvuWmElcZynMkW3p3P01f5ROmmcaD3BydLmzxr2hO0ggp6b__h61XCFKQY8sF03xxJNXc29h46aGAef4FqLLfjrZ_dLLmsYP22oqaXn8cDka7HuWD4jS7Q-5Flwv8nIqdJKtPn8iB4Co8EiybSnpa98KyGB-cmBn0jxxy-fnpLHLABBScCSL0A9NKbhh21EJPmCqgkPpd7g9tmnNW0d5lgBpVSUcbMYVYs2ZWWkB-Cs8mFBWBbmiRfqQm4uXLkb8O9Jlaoq8XMqDVlR8Lxb1vEZLz9rvuSGTTAtpX33ya8ktP6Vhw5JX5H0W3_1QqsLq_QF2ekbXWbhEstSH8phpsRMYjs-dz5cVSP5KGm9k7jUDpFbgSs3MIJVt8Yh13Jtm_M8oIjHi04jVzlYD3X30eC819GbOk0gVlco9KN9GVVR7tT3kELXxZz-zCtc-wfXTsYBHS1wYO3K9OY1P_lSojfyIcTH0mL-UUrnnm5xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=CePrtrtQgtLbPQdtMA9QZHK6VW2rbdznqX6I4F6vWYkovoNXlE2SFven_kOgrCr9oyPUcO2yj3VL5Elso7Uhum4NycGcRMmHa39CGqQgfyjjw0jvLRZlNc6mGHtV6eP73yMuJJ-XY2sjg4lxYOBWlvGTFpl_CbtW4N2JzPqAN2NAEw-k1ZD8QgaONjKA82xsJRYXCwPMHXC43VaafZVPGhv4jzY7xfV-Nont8sJ9tyr2F3WfmVMfDvF4lBdtrA4bZg47LDDPH8DV2XnWigOBWvyQdxbEJGnQjiMGFLcn6Q3laGk237nCaBTOE97QTC7-jCJQzNFkCAXh80AE3DJ-ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAlqS6TVlzidGu31QOSJ4Ef151VC2lwZHfyHM6ueoraJ0bdQD2jXTIW7Zo9W8d442JEWmSm6yagfgZ2begJmQgQG5qbJQOpwD5S-8QrVATWBJNV_N5_eXWELLKbmqkHzqpzgQgVwGsoma_7MQzIVj03jIF2nUHEYstEseYVP27t1hll66aBH6rAQfVzad6tF-kyoXQ_xuQOB_b-19590ef-OpB20DJwzkUinkDwi05QRNvvJ9AVZSyZkMaKJEyEXKtHEi3hJjUJoG9P4YseFQoBJfr1h-JZtaQ1glnCxb2o4klYkSP5XpU_wjF2BTcqSGV5_5opWaaELQKQMNkGE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=cv1a6MCfHZIdY99mrp_z7HdIkhKoV1iSSJzRw37KGCHluv0-1b5fR4kfAwppZZBgICzbnY0F8xktWjQf9vkod0i2j8-t5GnxgfePqYUv24hXzNnsVhIMekKn8UqFVWnucBbNzjMLg1yAL6GSvMVKwhNju3ldsYcfuTyjH9FerzdCJ5-CGdd_f8NR6J1CwKmd9dcBMMCY9Q-vFxYcfF03Q2wnpcW-NUFbe3IE6ePjbA6qh1e2qFlUlCxE5Zt98W2t7pbAxq7XZuHI0bs9gspdLAX57dJCfp1A5HJpHPCaqfkgCgL_DsDpaI7uA8zClmXvqluk_QIRb68PSw2UwlvZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyKxEQTSRYbRNnvfSPps8nUzMOVLTgfDH9QRrzV-1ELTQSgP3dJ3SC471N4ZVL6RASEUMYi_7LPJr85cs5IjYUAyATKq4YGjf5SEfTB6eOfD116iToUqDGk4KSr4athBYwkEFP75TCpCS75wWrt4gtbWvBPMmK-LSrCapql9e0ajxBlB_3oWb-L8skjqIbqWWTFFWzqrvnBzFjhdkD8qCgyO2iStMFb379CU7DxjgS0suQuzxECxYWpTn8-ifO5-pgAaZETQr5ZO9DnCd8gs8WX7MtZH7iglZ5R3mMrkSEaEEtS7GS-8VIVqZh7v_jGovsuM5xcJWn3E_aAW4tlBIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx2UAvyY0mxAROgLu6cO3upEUYkjNQyQXjQQYnFxICr1txAzDhz4FTBIV8DcxzYGzjDluXNK4-fu9fN3C4bIaxmYoU0P8vmwNKqPx4zt9ngpcbDi9wUATIHI0HjRRo7XyFkJO7RAVXiCpZ1s5QQBJaNIruAe5f-1u7DWA4u02IQx-FuefoIG3RW4Pn8wrVv2Cz_9ru7WdFZH4KRBe7TDI65QjrWlOelqIenHEDF-SY4gAu-kOG5PfQi-lywdIXTPRJEt72ddWDckFmbepsr6oJOwi9gEJAcb6sc1_kBsHK606n8xH1sI17RN0BH8fLqdJk_fR8Auv0eIDlx-qTKaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrpLqEEJh2oVGr0GkF9T2GfgbIGgC9ehXVqwKvHPgyqwOP8cAtyqDRkcel5OFNGGdfPkpvmEoDLEHzSgG_FxDmr-fooXqR-R8uZPT7VDBLfqFVvE3depg6rSrGfC68ADtMgUX6pC4pg3E14U3Q50fH7iU6U3e6Rpgvgcfos18OO4Zj8TZxM_LhPlYlURPm_Iap2mnErX59GMpHEHUK2Xk_SkX4DYxT9dwxnqP5rVSlytIVzAeeUD-dIU9gE-TDka9q1gpOPoPEkNODd1nPd3pM9jiSBg2llAitbrbdvF7SNujHE3Gb3lXGY37enHV2ft3fIQZ7DoVDuFx_F4l9bQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=VOl-GvfoibaEE_Njmu9NFXwmOcCXSx7i0QPE0Sx0SSInNF068Cv1Oe98mNY_zSwmvsgsmL_qQfLcnXRKLagdEztXMMviX_lfyz03gWiezbstvH1om0IR64sMRDzZReY9lBVBshjWLj33oKJzoUJxDXJzrOiwiXpEve0ihVL3KlCMgejaPQr52DNse7W79RTltHA5tvBlF2OKsbve7NuXFeUYxaUxCGKUnH-_QJ5P821qFHgo0QVHs-po6yqYNo7QfFn9YLLvR8cOuG6g3L7rsvRmFOUj5fcDP_emCE2RJ3JyVokIvtakS-IuRYqhfeFZ5v4g8XIZwcZipa314b92Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=VOl-GvfoibaEE_Njmu9NFXwmOcCXSx7i0QPE0Sx0SSInNF068Cv1Oe98mNY_zSwmvsgsmL_qQfLcnXRKLagdEztXMMviX_lfyz03gWiezbstvH1om0IR64sMRDzZReY9lBVBshjWLj33oKJzoUJxDXJzrOiwiXpEve0ihVL3KlCMgejaPQr52DNse7W79RTltHA5tvBlF2OKsbve7NuXFeUYxaUxCGKUnH-_QJ5P821qFHgo0QVHs-po6yqYNo7QfFn9YLLvR8cOuG6g3L7rsvRmFOUj5fcDP_emCE2RJ3JyVokIvtakS-IuRYqhfeFZ5v4g8XIZwcZipa314b92Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB7ELjcqDxXK1CnVtX-OkMBsxpzt40Gasgj2J-d0DNQtVGeQEPUrpTK661JDz5-Y-hjthsWd_QfeDJvd5Srw6foSWbfQE_lup1s_6JUbggOf3oKfxAnPhn2rASisDkho74nXnhyPMPY9NXekBrQmHSEmfqNvAJPdf1Jw-ZJASo48HJLV_BnTjr3l3CYdlHhtUjEF-2ciWMdRFzWzHKpDzitTycN8TUR9DmyIG6Z1UDFP6X4dW0Z2e_9YLO7Chqbt9k3CxgWGxe5sevtz-N9czNJbRI3lvGMON74Cw060HJ0dxVW2gthkKkfmSjWUX03rMAdl3Tg3nI2rXyEQOL1juw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUGVl9CLfy37So5sqBBMYbxXLuD9sCzFw6LinaXl-7w3ouprur9EyLxezhCtXSUdbfg2oUjplZ_X0oHAvAtz1UzvIPu9WAmjRLpr3If-1vgdT3-E_4zWN36eSe3jfMstchkkL8s9XV7U0cjWFdnAAM1UhsnFRJ6zPfF6Shy97y5dznAhdujuoQ8Lu3WgE5-8sFyI-JwjQ4CirCk1_OhiMJbEHRmYUIaZ0DDT-qs2V-W7zMeZ8HPlQF0FM8xPoRQnyHYw7q6qwa3qMmYFe_drpJ4nP7UnMvqFvfzHsXY_jRqLs7N2JS1gEdv6msV0803FjUb91Q_PZx-eJJCM9k9lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDsTo0FJ0Yci8VQyCiPWwwfyNyX6VRWeYL4zYDoLo7pwhLcPxOCcvnSKBGKktdlGr8_ta_2UG7GCgKU6zMJqxuc51TzPmFMQE7_pTtvSW2ulKX4YJwWGBwATFdGnIh4cQpKDuMNmfgpUrRHkLIdfPFSVXcUIDOIHXjZGPVFTN7btfq4oM8dAXPL9EUVyT1UyYcgYzjojHfHMjTBCjQEcxvlDuQ7Br9e2kW8BQLIQ97-aqbsaHnrjDrJvplKMpe7lBoOdjXprhjbFBFMBRvRMpsJTPwjJ2Slm4HUXzyzH1pqs-dzsMDDQ3mS0G6L5CNg9Xg2beG27tx0ERSdLCq0o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=C6GYF2mFf8rGM7bb-t-_F9Ooe2zhlua9pBWf6bsV5dVgI5MwKn5rdAbx8t8ye8NtKxejel1tKQrz8WT5Z295nvBPx8FAm1JdXqKPqwX45PmWJ7323waOKaozMnbn3RuI7GaxVj3OdaMz61bdk91gP7xDzxqEy7jriDtvMePTl9HQypQ5PulGwKit9qxXeeq7WJlVM_BgTSqBL4MzVSCpbqsgwhpUCZM0oxQGtxoRT0zCdbyFjQEh8_h5I1I3SoWoIjtTVTTD9D2QPW0KodQMzCxOsHLDNPYz8g2oL3PLVwQvO7RG4HOTc9CJGq72o8Cg5YIVUGVTutnBKUnZyOFcvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=MHuwGwesvod8eYRhdPvRDLXpHYIqINtztpuyq5oJn6Z1pfDFp1G_KZpKB6TXMRbyLgZgZHBarRdH2NcCkv3otWzS4-xJ8rkjesrFZxXS25O62zYH_s9KMXRjnIJrmsc0RAS65MQWUltTloX2zTIt_pBydZutqSRwU_eyLcAKVXZ5KXCl5iJVJ6ZumFBuNS21dBikchVamGhQMFQG3VSCdhWL5id8GVuwvhYXYAvwYhOhRIPhTOulaphyO-VDoA0m--BD7qm9R-i-zJ6s2qfew6qF65mNNeWBe4BmcF5oIy_PwtDkNfYTqdrAHokzH9ZL0qk_h_VNj0Kn_-j3a4tyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=MHuwGwesvod8eYRhdPvRDLXpHYIqINtztpuyq5oJn6Z1pfDFp1G_KZpKB6TXMRbyLgZgZHBarRdH2NcCkv3otWzS4-xJ8rkjesrFZxXS25O62zYH_s9KMXRjnIJrmsc0RAS65MQWUltTloX2zTIt_pBydZutqSRwU_eyLcAKVXZ5KXCl5iJVJ6ZumFBuNS21dBikchVamGhQMFQG3VSCdhWL5id8GVuwvhYXYAvwYhOhRIPhTOulaphyO-VDoA0m--BD7qm9R-i-zJ6s2qfew6qF65mNNeWBe4BmcF5oIy_PwtDkNfYTqdrAHokzH9ZL0qk_h_VNj0Kn_-j3a4tyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=H_CyeK2xd-mK7pOlufVNUFkqlYJ-JD6c2XU4h1XqA1gkRNhP9d4152RDMMr_UsNWYLXdcQ8SJsDtCFLdNvGnA9J49hf3wxcJFt6o3OHrXs7WndcS7WpVzVECmhDhrk-vfcMEjh50wCKZrWt4-BNDSGt7XUBuLAuMpEZISYjFeRbu8ORpRbK47SGRA-RvhfMnSIX-ywIu-ZeBP9Irumq81rgi7Qah68oAqXw37ZHAdSDuw6_1kZm4z3BCNvS85unBgMDmR1uz5ZsiqHtBViaTk4KZ2LevK1u8DPWPNxFAyvcjgXq0aFNlmslZYT0m5n2F458gflXr0VQYD0pFbPAtuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=UelRZB1X05LpP_7C0iLp1TUHO_c7r_pip3y12ukVx4Av9qhEQp70KI4xPnOWjWzy_oAfSVNsblKpWetoMtOpIjzfaf1PJ-ElAn8LDNHZzP_fGZBMdYm-ij2I_C5F2ATByylQ82Yrd4iw0gryPX8LXBIXvrYBy6EvM3KoKjjLrIfPPqROtDMZw6bS0xbBUeTOqryGlwUQPYEhFvY8QPvWGxC5DZwhEjQO-3tpTpSqo0I5Aa4Yq3Q8F99jYSmSa9Tdr891KKeA19EbvBIShrd4wA6PpRbMdTJmWm4QhYiFb-5Pa7e8A4a83lHHSLvLiDAKUNQ4x4tiXitN1Buz4OGlaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQTaIZOPaPW-Cc23mEpBBo25n8haZzNjwiAuxHUE1-2XQ7w6CwNPWNBqvLb7_20TI3dusAT0v7h8P-qxn9kBEsnWppJH_5YROKXGtDWVt8G3esArOtkfJAOh3jWmZf9nMMc8craPOhql0vNF7qnM0mcuxbzFimJtGNs_d0pV7c0Cnr8g3xlMPdVxn1uSwS03OA3_lDHeyUy4H-KXMQ-hufsjlM3JkIwNsBruaNDE84TVZqyPFeseUncqAGolX6iQMJU5VXi-cW6A79AiURO3Zcg7u2Ouw7xXo1r7q7zEl_8tQ3IB60V8QQYQ7mr-5Nz2TnbMR7ZSMUAZTCBpNZCucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqE1hsMgYG6dAtyg7rWwAHcXcpkikMWU3zBdmygJqe8Dy2bCTkHOCNleEGgTX-4OIHxs8ZL4fP6zVgOKucbMJNCcV3Bom2plld2Toffcnl8lXFHGMNndZAkz3AWuDxjzrpW7LZP38NI7sxnIkZ39d443sH_att2CgtNt2rFWelM43qYj4xmYtjZzvKhA_3HB4MXyIV4y0VYCF8vHnYHE3yh8QT6ibqsyXYRuc3DmjRl_VdyrcSCYLMFmIzu7pZzTnA8Vq6Xk1QWlJohlO5mEx69Kltg822gfRsqd9GtJ2Q6F4BmcGSr7vYp1jnUJ-OZO7im_u8BAqBG74QXX8B19Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAoXDoXpbZS4L2afoCCIC4JwO_u3-Ydtezoe4jOSG_8LT1Vlw6QxwSsFxHYeTm-n97nUK5HRtT3GHPIryu8qe3RqEmokUR5cFXhPM_1XtyI9nR1FflOfkilXJ78xEDulfdRhb6KnEwpQyI3tW-w3HmIDBd-RdDMT768QY5hfK9sknaadfKW3rFCl5okcsbiNxDha_aozmgFPTKG_Yk4rNqhIFy6RBrpvD6umPPSTJ9QIuP0cn_drblg9jfdg99kJoCjQgc9I6UVo2LijlYlNt0MoNWgD7WB82RQPclr0wTCb4W2r9CmR_4HyZBRXfDEJ0Nl7hadgtn30I4tJ57_CrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vde8opNORzgrRfa5iXYmzQNc-H5RYPyT_fGmBA_tqARk5A_M-ThjOxSYMCGfnV0pi5aRM8oy6rHXJH3o3go89OS5kanHJqqvbX7YBql4EIihNMVXedlMHAq_KBKmIq08cLh5eLW717uAdJ7vZrJ4IpSPDGWJwiEGSRdcc0axcpgwT2XrtzxYFcePZeuzRBTBx4902XfQq-934ADRPddoi0AEY6IHgtIBBzpG8nzmtG1YPKZgK2gHvydOcfOgD1ZQ5O12e6ZxmvqDSaDgSPaH12wxFakg-sxVpF_O6Wr3uchsnrYtUlq78xj1EHFbdQzpv2EBxHg0wqZUR55GEOczrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM5wCrmu-x5naWSH2MwZKC43jwzcxZ3hVZ-bEaptLgM-ynw0yHrFAWx6GPIljoqCgkhvbqXxguMScG0NMIpRa5R9e2zB58hd--qm4O6NBVypRPSb58hcmD2GI5oyyb58EYw97-9-xOXsV9FGkBHxTQF0-GCjTpCkisVYguCeeHS7PdIDilX7fO17va2RHUEhkuBf0lvnzJKaJzG8kfXKRa80tFQgYil2Xug0HR5jE4awrgCSGnZ-Wq-z7sJjbn1Wl_EjUK2FBTZ3pk1dAug_xL5MSIPD3vDFFQshU7NS2-e38fRvkdOedcQ2fPjolMrB45TKdvNH3GnmZTLbeiiF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur7sSoJJoOjC9xyXV91sA7S47VXYfxVjyVZoxoOjCbEnOLep890bPNkAh8C1sZSuQw6rbx9fe3Fp068xtMBcoUf_wowtATNhq9r3nztj7tvK5zFy-6x8W2mqZ0T8HFKVweAtFPkE2Cwr8SBzjsuRUyodKRLzycxfwXbRF4LiYSKxKfrIKwOglozLYfS6egbGr8l1RsS7_Nxy0cJhay7dVgrG09y7eIo6E6UXXQPAbFKHLmhcu0bj8cZHoTkwlOXupY19boidAWfw1lWizcnqAxhdbOOfd5XoEzWDKeQDn6lTdeafaIrD19wGJC9bKb7u2EGCAasHm6in2HK9OjEMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqXXOdPMe45invCul4WYOKpVm8Ixul8MLO2pyg8Fm0OKKaj9u1qTMfP1B7YPuoIKH6vH0gr7Ezod5T2blulK8-ajQUYxtC5JdgR9GT7QzpiuZZaKDXbMG_yainFpIP0rwoe_XDqVnbx3Hgam-vzH8z9E7G_E9kjbDCvWK9Hc0gdWDIYaWz0VlGRiwbCpL24YraLSFhElBllH57kWHbsgU41YocPPf1bmkla8_CppZ63VQUPSKyaOnjxzn-jRk4vyNwtaquuIpks9RVNwNSqUWka5gxDboFGaFXK9y2jcWoyNqVkEvQmFXCAkndC1wYNmglUoVc4uuisCruP5X5pj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=Al9B37x-Y3e4c4hkMJfAUkM38BHZUPnYU_9U_6eFcRIfBboyojLf1egMRkh3gu9hybeHs5OtFWhmBAnqSpvC1NnpA6vMNHb57kFFkLuUKaw1fEeVF6vaclm-tb75_jX6lCYMPMOWHv3gVBK65sgUqvrFJvJ7NOW_pkrlYY5ZFph3aKdgeMA7hpg4JXrolf9T26JHgUI1OU8cUH2FxlD_EGIGqXvG2w2vNXTMkdnwe_G72daZtffNIHJ4GxLiAs3pGygifYFBseok_1f2G7gA6d-iaIl7HdbLy2-vcGU5pKrhoqcwjA-Tx8E15HT_Q49oJPJ_wyG1n_T2oJqR7IsIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=Al9B37x-Y3e4c4hkMJfAUkM38BHZUPnYU_9U_6eFcRIfBboyojLf1egMRkh3gu9hybeHs5OtFWhmBAnqSpvC1NnpA6vMNHb57kFFkLuUKaw1fEeVF6vaclm-tb75_jX6lCYMPMOWHv3gVBK65sgUqvrFJvJ7NOW_pkrlYY5ZFph3aKdgeMA7hpg4JXrolf9T26JHgUI1OU8cUH2FxlD_EGIGqXvG2w2vNXTMkdnwe_G72daZtffNIHJ4GxLiAs3pGygifYFBseok_1f2G7gA6d-iaIl7HdbLy2-vcGU5pKrhoqcwjA-Tx8E15HT_Q49oJPJ_wyG1n_T2oJqR7IsIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=h3HDSUm6h9ybns9sGQp7wJK6EelalyZI4IxpDQtW16aoV1R1RjEHrrkQrEj14jyptam9h300RIYyj19oCByziarQlr2OdvE5mqp_vm2nRRmE4egzA8vwNLP8xLwDp_SRvyM8WF5Cszfd6u0hODCZPQ5AYsCao-tEpm8xkOa_GmoNhuvhmkJQmdWyA2m6Q1RjnKiYRNmap-4KQzmUaPa29BeJyYQsFEoqGvvx7jU--oyPmdsiKAGhIFSIjKyafUlDmT92hLqyGFJ2jIfHGFKwJbMC5KgDDKxc2XfSfIuzn0O4yaragOVbS4U1nMkb8xW9Qr3QJPCVXkKx0u5kL5mvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=h3HDSUm6h9ybns9sGQp7wJK6EelalyZI4IxpDQtW16aoV1R1RjEHrrkQrEj14jyptam9h300RIYyj19oCByziarQlr2OdvE5mqp_vm2nRRmE4egzA8vwNLP8xLwDp_SRvyM8WF5Cszfd6u0hODCZPQ5AYsCao-tEpm8xkOa_GmoNhuvhmkJQmdWyA2m6Q1RjnKiYRNmap-4KQzmUaPa29BeJyYQsFEoqGvvx7jU--oyPmdsiKAGhIFSIjKyafUlDmT92hLqyGFJ2jIfHGFKwJbMC5KgDDKxc2XfSfIuzn0O4yaragOVbS4U1nMkb8xW9Qr3QJPCVXkKx0u5kL5mvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=M4BSWiLto23d_CGKo8IZK38irnA-fXZT-mVLHmAbBgdOJSsmEBwUNl5lfmBbjP14zAM93JN52npgBMvgz-_sk6gyoK2HaRSOVZ6JHKL-OuLMLLQza8gXKj7_M1LctesGs7wE-C74vYcdv8YM4JMS-vMJuHKSW8x0ibe8PYIsQampuAppRhuRQ1lz536rZ7zlZI-eMxzkfR5oBXPuz54CSBV7vUWp7Ux8ffCJTlCZ3KsdF2GZ8hZK3H2kmnwlRadT0vnFJcG1lN1dE44mu0wAbYowZB1Ns8HGPgNEUzd496MaeigVIIGRbwG-Ik5q0RnmOa1Exlaloz24DIxG1STn5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=M4BSWiLto23d_CGKo8IZK38irnA-fXZT-mVLHmAbBgdOJSsmEBwUNl5lfmBbjP14zAM93JN52npgBMvgz-_sk6gyoK2HaRSOVZ6JHKL-OuLMLLQza8gXKj7_M1LctesGs7wE-C74vYcdv8YM4JMS-vMJuHKSW8x0ibe8PYIsQampuAppRhuRQ1lz536rZ7zlZI-eMxzkfR5oBXPuz54CSBV7vUWp7Ux8ffCJTlCZ3KsdF2GZ8hZK3H2kmnwlRadT0vnFJcG1lN1dE44mu0wAbYowZB1Ns8HGPgNEUzd496MaeigVIIGRbwG-Ik5q0RnmOa1Exlaloz24DIxG1STn5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=lh9GvN8kUB8Eerb8OvkQ6-YwQpuRGUASxZyz3pK_tmKVH2PQXnN0knvCvCIe1jvj6or0PCc8YxxMMjNgyPbClqw1FxK3-w2Jjss9yyqDzzj0FkbZWd70z58q6qwmJHC-klVn4Ag0vcsYCOKKzT33lLNapzeXtBX6C5DRoidWxZ6kz8lTunutH_4JC9asMtbe1sBnBRGCubHq7vE54WqVEFlJnvaOWskNAuZuzB3z_6U6vzcW9jMNlLxyREeJ0rn__AHnaUvMc01zVmIm8hEIAQF70U4RBPpKrul-_2lg9V7XwgyubyPGAyAHpNL2dSlAL35oVmCJ7YXj_d7LJwAnTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=lh9GvN8kUB8Eerb8OvkQ6-YwQpuRGUASxZyz3pK_tmKVH2PQXnN0knvCvCIe1jvj6or0PCc8YxxMMjNgyPbClqw1FxK3-w2Jjss9yyqDzzj0FkbZWd70z58q6qwmJHC-klVn4Ag0vcsYCOKKzT33lLNapzeXtBX6C5DRoidWxZ6kz8lTunutH_4JC9asMtbe1sBnBRGCubHq7vE54WqVEFlJnvaOWskNAuZuzB3z_6U6vzcW9jMNlLxyREeJ0rn__AHnaUvMc01zVmIm8hEIAQF70U4RBPpKrul-_2lg9V7XwgyubyPGAyAHpNL2dSlAL35oVmCJ7YXj_d7LJwAnTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=hmVERvYjVaOsfOIZFZiw63z17hsttUkyrRxno6UhiYTBLkkm8foQXzLMl-NbjoTPko5IIGTRUiN-gpGKl6yq7F9kFdXMpsicRVXgxZTW6fsdDbNZ_u8oHF8K17LEiy2OuvE_Ey5LvKjiJXzLfQoehQy7R4QhMY0jnlToqNdCN3-XmqWAeo_VUB2Z3mRxbNTNKX1939pMp00CvF9avNHLKKICIZFNK5oMQfwroV4OEAF1el75k05r5EtMF7ImMTNPXVY9UatYkWfsIcN-oJcQVbebhxNKBhbDK4PcmeSQp3m7QY0pxR1UlowdjBt8tegXWlYNst1K3D5HAcytzdEr_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=hmVERvYjVaOsfOIZFZiw63z17hsttUkyrRxno6UhiYTBLkkm8foQXzLMl-NbjoTPko5IIGTRUiN-gpGKl6yq7F9kFdXMpsicRVXgxZTW6fsdDbNZ_u8oHF8K17LEiy2OuvE_Ey5LvKjiJXzLfQoehQy7R4QhMY0jnlToqNdCN3-XmqWAeo_VUB2Z3mRxbNTNKX1939pMp00CvF9avNHLKKICIZFNK5oMQfwroV4OEAF1el75k05r5EtMF7ImMTNPXVY9UatYkWfsIcN-oJcQVbebhxNKBhbDK4PcmeSQp3m7QY0pxR1UlowdjBt8tegXWlYNst1K3D5HAcytzdEr_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=H1hJi97tT3dOV90cR5di5kywDy4-A2O_bux9zbUsPiMWfRgYYkEd-mbnl0WJJDb2uT79OVzSuOWLsTia9r4v14gjS9TEkXFlSVZfpnsY8A4fYVsEB9bOjfZBFNISOuLM8dApoIX7KjGKq1LZPTZ8PrOMUfQ3NawjF8G0ReBoR1BffIy9ADDnghbaiy60BR78fQh6Z1kNP508zF670DBdw7uLb3a683CN7OyEuUYEZHj20ikQ8gXrqZIYLDId8c_1pp0bJRmDbOW8NBL8hpb2s_8vGW_Pa_oc3pgTO4scbtaeSRktvQUtp6ESb1VrtSM3byw8-hLO8xh84v2A-qVLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=H1hJi97tT3dOV90cR5di5kywDy4-A2O_bux9zbUsPiMWfRgYYkEd-mbnl0WJJDb2uT79OVzSuOWLsTia9r4v14gjS9TEkXFlSVZfpnsY8A4fYVsEB9bOjfZBFNISOuLM8dApoIX7KjGKq1LZPTZ8PrOMUfQ3NawjF8G0ReBoR1BffIy9ADDnghbaiy60BR78fQh6Z1kNP508zF670DBdw7uLb3a683CN7OyEuUYEZHj20ikQ8gXrqZIYLDId8c_1pp0bJRmDbOW8NBL8hpb2s_8vGW_Pa_oc3pgTO4scbtaeSRktvQUtp6ESb1VrtSM3byw8-hLO8xh84v2A-qVLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=dKKH45VLHT9WWt-xw4P20akSnWoL_d-B5xh2QOJhYZT-uVdd1Qe8XA0npb9labswZAEx2wAl3_6LZ_-S5UGBdL0Ai-8Fgp_uR2Am8yWT9lYge5NS3jLJdWkM0EdqQgpwGTngiDDhBBwgsHm20pch8C7syCWDouYllr3p0Z8xAxtxM7qVfiWzzq2rdwUG5HTesW7kpMMLJsKa636gp_K40Cd4LNyx-t-zvxQT35HBQnO-NHgliWXteurD7BGnlQ2OvIdfkIEC3K5zyCD-AL_w-rM0xpFK4f92KGxIaT6EV6J9-k9v4uhb9z82Yp6b9OM7Fov82Ex33NvX3xw3AfGCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=dKKH45VLHT9WWt-xw4P20akSnWoL_d-B5xh2QOJhYZT-uVdd1Qe8XA0npb9labswZAEx2wAl3_6LZ_-S5UGBdL0Ai-8Fgp_uR2Am8yWT9lYge5NS3jLJdWkM0EdqQgpwGTngiDDhBBwgsHm20pch8C7syCWDouYllr3p0Z8xAxtxM7qVfiWzzq2rdwUG5HTesW7kpMMLJsKa636gp_K40Cd4LNyx-t-zvxQT35HBQnO-NHgliWXteurD7BGnlQ2OvIdfkIEC3K5zyCD-AL_w-rM0xpFK4f92KGxIaT6EV6J9-k9v4uhb9z82Yp6b9OM7Fov82Ex33NvX3xw3AfGCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL6XQ3pOu4JAqrUYX_Tmc732TPl-qdBwnv1CYoI-ehV7hK-rs9E5hr-tg72_piTCziQAm3KBIRAjS6i8KF6ZQXODrLnTtGq28b0_lKaIOOl2_ezxKNS4YTpQ04F8t413Sjh8soQe1np-fTCBI1gpzLT5u_0gu_u_K4HxESMUFchCtjbsyaWWx4TBmI7ZVv3gBNYP6SXMbwYs7wbfYUjHqexepiRRG5R5S7b_uogxZS4a5HAyo0_fR9kRFb0CqjMrat2UorguCPQ2i2Qv1aq1CkOcdcwe3J6fDTaS2MhVloelShcF5APmYgF0u3s2yKHO5nYtxoiMHDD8tGh5CQEzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=vgSYiew8wlrnWqJcUNN8yQAyQpLPuXIH5R9bF0XyA12paUmsrvR7oI96p4_1mSGH-ZUNUWEGYe6J1AKoYdWQNjd4mQs7qePVAQryrwKSdyZfHEslD3vga9d0fDOiD0uxizZNHU_HeAkFDhJjrHvuKCsKgrtHa8QRw36Adj3vbo4SWcTuiCt9ZxKZX82A_9aa37-A47q4CR0XKtQyu84Cky1uxWcXBcOw-CheSq-5gCS4OJMkDKqrAmsGuO2kpmffmtX7uFSRcZDhG_lUFqJrS44gk9MsEXdTJmYzPK54y2Ynuy_jEHlG0tutBOww030fPiEOdRPs5xuWMNTRZ2mWgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=vgSYiew8wlrnWqJcUNN8yQAyQpLPuXIH5R9bF0XyA12paUmsrvR7oI96p4_1mSGH-ZUNUWEGYe6J1AKoYdWQNjd4mQs7qePVAQryrwKSdyZfHEslD3vga9d0fDOiD0uxizZNHU_HeAkFDhJjrHvuKCsKgrtHa8QRw36Adj3vbo4SWcTuiCt9ZxKZX82A_9aa37-A47q4CR0XKtQyu84Cky1uxWcXBcOw-CheSq-5gCS4OJMkDKqrAmsGuO2kpmffmtX7uFSRcZDhG_lUFqJrS44gk9MsEXdTJmYzPK54y2Ynuy_jEHlG0tutBOww030fPiEOdRPs5xuWMNTRZ2mWgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=LzViEJhDDNtwMESHh_sSOg1apCYWqrMjm-F03yY_hu1Uq_QbulHu6Biq1iuU7CaGkSjilvySRVKqhYD7YptNBU3uuDBwq0klWQhdSiyRCTWiIaEy3ADmEP-jwcDLTpNN50Qc0LXc9FtVNSQggZBAnGYjsSkkopCxhjUw3RrOHS4fqOYqaowcdoiwTFhXVjdYt5z-TF52_IDab0_fPafsjBbo9uwJy7BALv19zZc_UGyJyVn8joBZIDE9CRwuYan6ky4iaodiB097fXVKOH5SbY4id1SZFn3qGvLTXkND49jkeCEHOBQwx07EuR6iLxbzBjVO9PrkSyJG8f7yTRlnQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=LzViEJhDDNtwMESHh_sSOg1apCYWqrMjm-F03yY_hu1Uq_QbulHu6Biq1iuU7CaGkSjilvySRVKqhYD7YptNBU3uuDBwq0klWQhdSiyRCTWiIaEy3ADmEP-jwcDLTpNN50Qc0LXc9FtVNSQggZBAnGYjsSkkopCxhjUw3RrOHS4fqOYqaowcdoiwTFhXVjdYt5z-TF52_IDab0_fPafsjBbo9uwJy7BALv19zZc_UGyJyVn8joBZIDE9CRwuYan6ky4iaodiB097fXVKOH5SbY4id1SZFn3qGvLTXkND49jkeCEHOBQwx07EuR6iLxbzBjVO9PrkSyJG8f7yTRlnQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=QvNaxUywHAuq48PY9Hi3jUb2amyoz3FE2eheZauQIuQeN3D8SW3SFRMQZMwm2oqK7K5D16c0IxNvbjZIWyzBXmKpImB8jA3Ei-EDgkpmhy_bBYrQTnw3QhjrMfa1lZ9MztYhDqYftwwG-5BN1ut-1BYrvfV_3s2u9IJGYYgVIKW7jxm5VOkQZdCzEYCKrD20lgeK48_p0tFt_7a8np1aMMuw8lnaCHsu2T4t-TCfhZAKnTrumeXhZSDE5ZV02QrNphOmss_FRY0fLZ9B-_hAaxmIBjvJrwcL0fL9CeB1X3aPQnT6HVyqrvPU3zhE060zmG7lqCpaRByRvo9tcwSuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=QvNaxUywHAuq48PY9Hi3jUb2amyoz3FE2eheZauQIuQeN3D8SW3SFRMQZMwm2oqK7K5D16c0IxNvbjZIWyzBXmKpImB8jA3Ei-EDgkpmhy_bBYrQTnw3QhjrMfa1lZ9MztYhDqYftwwG-5BN1ut-1BYrvfV_3s2u9IJGYYgVIKW7jxm5VOkQZdCzEYCKrD20lgeK48_p0tFt_7a8np1aMMuw8lnaCHsu2T4t-TCfhZAKnTrumeXhZSDE5ZV02QrNphOmss_FRY0fLZ9B-_hAaxmIBjvJrwcL0fL9CeB1X3aPQnT6HVyqrvPU3zhE060zmG7lqCpaRByRvo9tcwSuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=Bq-D0ez3pYhyLYV3KLB6CQ1PDuHMgDSz9VASE-2mcc7wnNBTXCDmhDRaI-Ddox8H32gfiW_gzn12ZI691v8jj4Jb2iJlO69NIJHezxT6Eeqlaps84ex2uj_SCnTKyBBzm7ESu8RvL6OihBY-BNjY8Vn0bby_ug1Il7Mkc3-GWI-2mTQ3CarijCLuKeLtrni8vk3JTJXTloPdeK3TrkptEFAQhmH0Vd2mfsIAKJbcGYEmMxxqKewnzP418xNTwZa8JZ1OXdyQNX7kfEJfajdM1AUOPN-S2-MADnS30rfUbw_lGEJMfO9qbw4tMXnUVlSCoJgQn4oG9TuWuMYmnJW-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=Bq-D0ez3pYhyLYV3KLB6CQ1PDuHMgDSz9VASE-2mcc7wnNBTXCDmhDRaI-Ddox8H32gfiW_gzn12ZI691v8jj4Jb2iJlO69NIJHezxT6Eeqlaps84ex2uj_SCnTKyBBzm7ESu8RvL6OihBY-BNjY8Vn0bby_ug1Il7Mkc3-GWI-2mTQ3CarijCLuKeLtrni8vk3JTJXTloPdeK3TrkptEFAQhmH0Vd2mfsIAKJbcGYEmMxxqKewnzP418xNTwZa8JZ1OXdyQNX7kfEJfajdM1AUOPN-S2-MADnS30rfUbw_lGEJMfO9qbw4tMXnUVlSCoJgQn4oG9TuWuMYmnJW-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=KSyeMUvhNnYBApdUPL4DvzhE4araXc7NVHkXMz8gSEFrZIUcG6M5O_7b5sutzcpUkzZV5t-Dj8a532RDCnggQkqa8L3fu1yYV3G4rWz_6fgrEGBPtq3Ay6gFOX_EuUTgrLiw9l0KBqrLIfzLA5de519FqC5fzQHQ-PGmpQxNMHfooMxd8Hixr09IDHDlxQRa2XOsUXT5KwOLPWTSRT3ljfbY_x4w5wne335ttkMkcJ3XzbMcqCvwyZTvJ8CN6ojaux130p2gUZgtKYBWybiwI8qdSPPe2PmQI0adtfW5av5EbC6-IGhVTh6dP6RTIvcm62_P9BtBZUsZWDbUzzOf4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=KSyeMUvhNnYBApdUPL4DvzhE4araXc7NVHkXMz8gSEFrZIUcG6M5O_7b5sutzcpUkzZV5t-Dj8a532RDCnggQkqa8L3fu1yYV3G4rWz_6fgrEGBPtq3Ay6gFOX_EuUTgrLiw9l0KBqrLIfzLA5de519FqC5fzQHQ-PGmpQxNMHfooMxd8Hixr09IDHDlxQRa2XOsUXT5KwOLPWTSRT3ljfbY_x4w5wne335ttkMkcJ3XzbMcqCvwyZTvJ8CN6ojaux130p2gUZgtKYBWybiwI8qdSPPe2PmQI0adtfW5av5EbC6-IGhVTh6dP6RTIvcm62_P9BtBZUsZWDbUzzOf4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=jGJmmBpaRHDzf6tSK75VUDUZDw9rtrevUYCPNWaetakWYtaGsE11lLGW5KQdFqXCV7MkgTA8n3grOBAPoqNiDqo63m2LwrI23hquhtMsDz3ojJ4SqlrEzzgUKsX_ZZb-ZFPtIS5PxMl350U1CdQzJTLsUoGnz12cZZDian2gQYyhXs2wwzaEJXkTO0GhDnD89-a6rnTnhUembNB0eBMZ9PjGCfnvP9QU2EDszrEri7JM9c8YTD4Ei2pITf8HmqKv-t8N68D5JvqdwN9dmFFAyobhBLekItdwe0WwfNn2TDenpwsXzRwEyBTcicfaJs8UG-nUh4oacXJXGBHgEPo92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=jGJmmBpaRHDzf6tSK75VUDUZDw9rtrevUYCPNWaetakWYtaGsE11lLGW5KQdFqXCV7MkgTA8n3grOBAPoqNiDqo63m2LwrI23hquhtMsDz3ojJ4SqlrEzzgUKsX_ZZb-ZFPtIS5PxMl350U1CdQzJTLsUoGnz12cZZDian2gQYyhXs2wwzaEJXkTO0GhDnD89-a6rnTnhUembNB0eBMZ9PjGCfnvP9QU2EDszrEri7JM9c8YTD4Ei2pITf8HmqKv-t8N68D5JvqdwN9dmFFAyobhBLekItdwe0WwfNn2TDenpwsXzRwEyBTcicfaJs8UG-nUh4oacXJXGBHgEPo92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=SJCB5K03on2XbAuJiCa94frPo1txJiuJaMQ7Lg4AmHueDECGjELBIU1Odr6VutIvdSc3as7kM5YzQF9tWLF1PcQshMYY-aYbKFcUyycBi3MaYlkjTDxYZDBB-uXsms02uOuyhIIOzW_VxbHNjzX53G2ASz3gGLlFX9uqlFNj1KW5m3D-w7aQ4oc7pT38eD3hduDZr_KZnyg4xAdjU7W0bM7rgS5RrFG7-i7Z4bruIBTigJIAo0Q9P7QUmVtOyUk51RLw2s10LyJO_Q1A10eb2jVrUzkOGq3iirYv0Lum8XyQqJBfF1aYAAQMcU8SNXwcIktiKW_098TjTJMoHnJ90w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=SJCB5K03on2XbAuJiCa94frPo1txJiuJaMQ7Lg4AmHueDECGjELBIU1Odr6VutIvdSc3as7kM5YzQF9tWLF1PcQshMYY-aYbKFcUyycBi3MaYlkjTDxYZDBB-uXsms02uOuyhIIOzW_VxbHNjzX53G2ASz3gGLlFX9uqlFNj1KW5m3D-w7aQ4oc7pT38eD3hduDZr_KZnyg4xAdjU7W0bM7rgS5RrFG7-i7Z4bruIBTigJIAo0Q9P7QUmVtOyUk51RLw2s10LyJO_Q1A10eb2jVrUzkOGq3iirYv0Lum8XyQqJBfF1aYAAQMcU8SNXwcIktiKW_098TjTJMoHnJ90w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66525">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=NK4vZWTyen0TocNmtn1RnsgZF3ppKwNrjfVUomZuOTkFSLmtjioi79fpnk39GPvMOnC0FjD8ramUPy7v2FCZksaATSTMBPQCT7J9y3Rg8TUxsLUBxfleJ2NIsDuNWpGpJNAMnREy65asqVfP4XNgMgK1qVRSlW8dBR3mNu5lijhQklcQXKUFivU6yy4GNuYgLFKUGxT8qRDw853GFUZYmmjpxUpic0_7331PjsMYnhq3YdpiYBuf2COLFDIIhTggzJXQegQBHZPXzfgbTGRLWaIR8-GXmWzTtkqrlSeiwaqSB-4XeYYUhy1imyNFDmCB11vkRydmA1e_8M1lZliAYC7ubU7pLkhLfmh4_JCQw_GiERFOhwsjm30EGduE2IRNWl2yx9UWE6TDrdcJR2PE6z0uzAXlbkSOCoXcDo0PcWD-51eDWM6ENjX8JX759YrW9SyBOOSWXutmL8lzDz5PmkR_YGJZM-CGdI2XgY8JXlmDNfBsvk3X2Vk6KPw8angTxIUB97eA1vMZJPXeXniC-pr8VeN0clvzI0pB_QENEyBX8MSIVn7r73obkrE-5I-DJINDiyHDnvoDECjtFDWWIj9ITB08z5ZTYD5xv3qYgwWN5Tty6mYNI_Zh6mnHR1g_yonTVATzuIOBasTpn7ugU56a-xJz7ufG3GOyRe7WNWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5016d97e5.mp4?token=NK4vZWTyen0TocNmtn1RnsgZF3ppKwNrjfVUomZuOTkFSLmtjioi79fpnk39GPvMOnC0FjD8ramUPy7v2FCZksaATSTMBPQCT7J9y3Rg8TUxsLUBxfleJ2NIsDuNWpGpJNAMnREy65asqVfP4XNgMgK1qVRSlW8dBR3mNu5lijhQklcQXKUFivU6yy4GNuYgLFKUGxT8qRDw853GFUZYmmjpxUpic0_7331PjsMYnhq3YdpiYBuf2COLFDIIhTggzJXQegQBHZPXzfgbTGRLWaIR8-GXmWzTtkqrlSeiwaqSB-4XeYYUhy1imyNFDmCB11vkRydmA1e_8M1lZliAYC7ubU7pLkhLfmh4_JCQw_GiERFOhwsjm30EGduE2IRNWl2yx9UWE6TDrdcJR2PE6z0uzAXlbkSOCoXcDo0PcWD-51eDWM6ENjX8JX759YrW9SyBOOSWXutmL8lzDz5PmkR_YGJZM-CGdI2XgY8JXlmDNfBsvk3X2Vk6KPw8angTxIUB97eA1vMZJPXeXniC-pr8VeN0clvzI0pB_QENEyBX8MSIVn7r73obkrE-5I-DJINDiyHDnvoDECjtFDWWIj9ITB08z5ZTYD5xv3qYgwWN5Tty6mYNI_Zh6mnHR1g_yonTVATzuIOBasTpn7ugU56a-xJz7ufG3GOyRe7WNWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره مجتبی خامنه‌ای:
من آیت الله را کشتم و متأسفانه آیت الله دیگر را آزار دادم.
من او را ملاقات نکردم. من با او صحبت نکردم، اما مردم از او صحبت می کردند.
اما او شجاعت خاصی دارد زیرا به شدت مجروح شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66525" target="_blank">📅 22:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66524">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=lgjxyQ-GbBTtCa0PvbKYCnlPv2aB9Ip6RXQK99e2Oh3D-bCHp7UK_2lYLlBYuKElR_xlDtwVMNUbkU30YvPNFmibbhnSjHUmEkpodvLXMtx-syiWwPOGfuWsMo2Iz1qi7eiUhZ08Y_08nsFlmWTy0sZxM-IveVW3HUHznjOrLsbA569ZVCqWda6nUaaGMqf1Q2Cvzstru-0RX5xOWhF52IZqDwO0zt1t871HaAlny3QgZXaSNxYbSIhbwSn1KoPodf-en2WffMmiJCcHzVI8VS8IPIrYd3saJeDEIEE4r0GGe_xkHTD5xrmEkZgSBN5g03RX9_2mUunW8molj7_vnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb514f4019.mp4?token=lgjxyQ-GbBTtCa0PvbKYCnlPv2aB9Ip6RXQK99e2Oh3D-bCHp7UK_2lYLlBYuKElR_xlDtwVMNUbkU30YvPNFmibbhnSjHUmEkpodvLXMtx-syiWwPOGfuWsMo2Iz1qi7eiUhZ08Y_08nsFlmWTy0sZxM-IveVW3HUHznjOrLsbA569ZVCqWda6nUaaGMqf1Q2Cvzstru-0RX5xOWhF52IZqDwO0zt1t871HaAlny3QgZXaSNxYbSIhbwSn1KoPodf-en2WffMmiJCcHzVI8VS8IPIrYd3saJeDEIEE4r0GGe_xkHTD5xrmEkZgSBN5g03RX9_2mUunW8molj7_vnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره ایران:
این ایده که اماراتی‌ها قرار است یک میلیارد دلار برای ساخت نیروگاه در ایران سرمایه‌گذاری کنند، اگر ایرانی‌ها رفتار خود را تغییر نداده باشند، پوچ است.
آنها این کار را نخواهند کرد. ما اجازه این کار را نخواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66524" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66523">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=HJcdh8pobSW1ca2gDxAegH4akTHIwsZcak4cjlffd0584z6oGw81lDeveviuu8tJPCEDLo2YBhbvUEsct1IeB9cLsQly-GeJ4O80BlwEiTkGFVloTAuful4rlinwaD4SA8tfLBLKvr1njKM3zjzdRGfE7yLk9fQCCWjtTzsz6gIHfEWcCkIDMSjU0xnvr5PlXwkWiEJznBSGQkJxPO2N2ZZSsTMJQ4BQVnSG58-qhBHjZK4hlOa0iV3__S7wo4DHskyxLMj1Uwm_tDPKybK9SqXzhb3J8MjBUbT_btaNHaAOZDKIJJyfxvNR54KM0EQIA_6B-B5BABa9rAFdENsw0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9895e96f.mp4?token=HJcdh8pobSW1ca2gDxAegH4akTHIwsZcak4cjlffd0584z6oGw81lDeveviuu8tJPCEDLo2YBhbvUEsct1IeB9cLsQly-GeJ4O80BlwEiTkGFVloTAuful4rlinwaD4SA8tfLBLKvr1njKM3zjzdRGfE7yLk9fQCCWjtTzsz6gIHfEWcCkIDMSjU0xnvr5PlXwkWiEJznBSGQkJxPO2N2ZZSsTMJQ4BQVnSG58-qhBHjZK4hlOa0iV3__S7wo4DHskyxLMj1Uwm_tDPKybK9SqXzhb3J8MjBUbT_btaNHaAOZDKIJJyfxvNR54KM0EQIA_6B-B5BABa9rAFdENsw0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏پیشنهاد جی‌دی‌ونس به ایران:
گزینه الف این است که شما همچنان مانند یک رژیم تروریستی رفتار کنید، که در این صورت به معنای واقعی کلمه هیچ چیزی به دست نمی‌آورید.
گزینه ب این است که شما مانند یک رژیم عادی رفتار کنید، و ایالات متحده، به عنوان مثال، اگر قطری‌ها یا اماراتی‌ها می‌خواستند در کشور شما سرمایه‌گذاری کنند، در واقع به آنها اجازه می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66523" target="_blank">📅 22:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66522">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f005383e.mp4?token=L2ctniy6iRHMk8YgOv8bjmp2BnkNzhkVdtewMS2KQQrYSvkazdEbPjWlL8eM-j_K-W-8n5r5zyufFJQAAVCvwu0At3hijf9dAVu0EY1jjCubHDRLHI7uco5FxqVXceoeCdpaDgJfF73qKI2g3CFEBM6mRbTx9MY_YfX9xaLaYiFYJ7dTj9ZFiIKIFzLLLKPlncDt6e510DewinqIhMNQtLgbDdtm-hvoJ4s_31if_lDGrMi0E9Upd539CoN_ZT1UHPLMD3fOT8_u37fH8iBbevrdGCSuJAf5befPMXLcboAVlp_pToDRWXlYuPpzDCA00ST1W9rjMmyQPRiO1LuF3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f005383e.mp4?token=L2ctniy6iRHMk8YgOv8bjmp2BnkNzhkVdtewMS2KQQrYSvkazdEbPjWlL8eM-j_K-W-8n5r5zyufFJQAAVCvwu0At3hijf9dAVu0EY1jjCubHDRLHI7uco5FxqVXceoeCdpaDgJfF73qKI2g3CFEBM6mRbTx9MY_YfX9xaLaYiFYJ7dTj9ZFiIKIFzLLLKPlncDt6e510DewinqIhMNQtLgbDdtm-hvoJ4s_31if_lDGrMi0E9Upd539CoN_ZT1UHPLMD3fOT8_u37fH8iBbevrdGCSuJAf5befPMXLcboAVlp_pToDRWXlYuPpzDCA00ST1W9rjMmyQPRiO1LuF3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره اسرائیل:
من از تصمیم ترامپ برای پایان دادن به توافق ایران دفاع کرده‌ام و اغلب متوجه شده‌ام که استدلال‌ها این است که «اسرائیل فکر نمی‌کند این خوب است، بنابراین بد است.»
واکنش من این است: نظرات اسرائیل مهم است، اما اساساً آنها از هم جدا هستند
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66522" target="_blank">📅 21:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66521">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=h29usDHxSQv79hWbnnDAfC6kKRctUN1G3mTlDMruVio5wHxVVACbSPlPOK7VoRwgEtcEaMI_esI589j2NMsH-d7IzWI-MmYVmR1QME4VeJHwxj1okcaqtVpXJfwwbp8vFSCJJiqARyPVUtfLE_wWS1doIfRzvKvNgZRF8VsFzAX32hms30tteQNN8wMBO62YFO46-WGfMY-evpDUtkNelPm3csxg4rry7L-ccJxR4Lw9UMe73ZF5nI_7NnQmlmzDzqKQ8ewoqK6C3Q-XG1y6JISGyjDKYzIgSVrFk1SX7H_suIsDIDgALi3VKUagKWQEtcW9PJDmrKLCl-r6N7xHuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ebdd0a4c.mp4?token=h29usDHxSQv79hWbnnDAfC6kKRctUN1G3mTlDMruVio5wHxVVACbSPlPOK7VoRwgEtcEaMI_esI589j2NMsH-d7IzWI-MmYVmR1QME4VeJHwxj1okcaqtVpXJfwwbp8vFSCJJiqARyPVUtfLE_wWS1doIfRzvKvNgZRF8VsFzAX32hms30tteQNN8wMBO62YFO46-WGfMY-evpDUtkNelPm3csxg4rry7L-ccJxR4Lw9UMe73ZF5nI_7NnQmlmzDzqKQ8ewoqK6C3Q-XG1y6JISGyjDKYzIgSVrFk1SX7H_suIsDIDgALi3VKUagKWQEtcW9PJDmrKLCl-r6N7xHuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره اسرائیل:
اسرائیل شریک خوبی است، همانطور که بریتانیا یا فرانسه شرکای خوبی هستند.
این بدان معنا نیست که ما همیشه منافع همسو خواهیم داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66521" target="_blank">📅 21:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66520">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=RNx7nEQNue1Apf66STaavCHPddlavnGJvw7Vp76cHro-KS3Av1GGgVEn5yQZsyeJFi28lRhGIZXYDjzAdsQzn62T2edW5Qomw2yeE9MY2qnX-9wNxWlCadZ5WYCfxtGTUg4K5d7lf1kuFJmqVZTA3yasxwLAbRxFIGoHLrGx8apoE9Ck2zhl-ViPz9GXFCYvsz5CEqdcK_3EnhywyE02w7n52PV0xxXRaU4vvKz8ULCMc8NCAYROzq2Ng_AJX5iY2BueAmModxKDPkzCZSjC_9MVMuNNVGcIfb3gQr02FCADYNQ2_4uqE_Ony-TUz6WF-NJw-LdprEC5ypeD_zMAGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3443a503.mp4?token=RNx7nEQNue1Apf66STaavCHPddlavnGJvw7Vp76cHro-KS3Av1GGgVEn5yQZsyeJFi28lRhGIZXYDjzAdsQzn62T2edW5Qomw2yeE9MY2qnX-9wNxWlCadZ5WYCfxtGTUg4K5d7lf1kuFJmqVZTA3yasxwLAbRxFIGoHLrGx8apoE9Ck2zhl-ViPz9GXFCYvsz5CEqdcK_3EnhywyE02w7n52PV0xxXRaU4vvKz8ULCMc8NCAYROzq2Ng_AJX5iY2BueAmModxKDPkzCZSjC_9MVMuNNVGcIfb3gQr02FCADYNQ2_4uqE_Ony-TUz6WF-NJw-LdprEC5ypeD_zMAGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی ونس درباره ایران:
باز کردن تنگه هرمز دلیل کاهش قیمت نفت از اوج ۱۲۶ دلار به حدود ۷۵ دلار در امروز است.
و همچنین به همین دلیل است که قیمت بنزین، اکنون که ما صحبت می‌کنیم، برای اولین بار از ماه مارس، با وجود افزایش به میانگین حدود ۴.۶۰ دلار، به زیر ۴ دلار رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66520" target="_blank">📅 21:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66519">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOPHbuAOkn_FUJnMeuhoqwtpmjvoWtS9oHM4Vo6FCDuXbKHVuL_4pLu6VZdCZ-GMvXlE753tA2jqzglopTZ9lNp4ikcdONf3P2wMcv_-5LfraNQhFk_76qw-XEheXwqHdbCKQFZolgMGTYlEqgn6uxk6ZAzqY4qZK6XdQj9SY3xHwp7sEZV4IpMoRFfXw0Q0SUUeRhfeVqqDz_6wVjuc89VqWsoCwutvOMPHsq9VBLgjMEdXNFsdqU---Gq_peABuVhI8p-vJyccHYyIMoyl8fo5CRTrDgus8dRYO43y_HAG1dWMCl_f1NvJKDwrXUQsEsH0ugZ2T1gUm_-FATReaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هیئت قطری رفته سوئیس ولی ایران و آمریکا نرفتن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66519" target="_blank">📅 21:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66518">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUs_ZtPw0lcYVVLIDL9drA8VlmhPWlLeaZGB43svCoY8Pg08PLVqeh12Dc28iUcY5qvnZfxSbMysQN2b2jdlx0VFS09Z29NMIDpTdeNnQPShIRQldz-xabLBaSH1VpMsUd5oxnPtYRFmM6IToiRUVO90fmNoCS4S-kfTR19_Bj33-hRuGOZ4DxxQm_QSu4yeuRI_7rrC8OSI0-FT-LUyItparwPCSf70dakbOwI3BXHc_wShfuv1JMdKH20GhsUnZc6nlJaGkGUH5dRYnE-MQxTzShED2CN6vK8Dt2if48jfaIXyBMbds9TbF4NF_HWcHhbicXZIdZ_qRWbdWtaCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌پست:
آمریکا ادعای «مزخرف» مبنی بر اینکه امارات متحده عربی - یا هر کشور دیگری - دارایی‌های مسدود شده ایران را آزاد کرده است، رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66518" target="_blank">📅 21:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66517">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eokV7t7VmJyC5jJC1Spy5Z2yT5wBXHUNqEIjTjt-yGGMUhKMZgWVce5pwHs2ZFksBP85UfVm9yEM9ssE9__HT6M0qiQTxZ3x0ZDkbHgc1cYqdXzEil_4kpoJhDLLJg3mNwruWZpVhyyJRCpOq7VT3ZX8DbmHfEF0lC2k7CJJQYx3aKdhjzjj2qsImjr0iNERSS39vWL2UuyyNOtv6FIVmNd42irJbYQKSv4nXZBRJUoKzYAS1ag_6iDphiTdUYgcn56sHtev-J2ROZ6UHn-aNDPIrxug0BOi3FXlx7MLnPyhZCyhvW75FjnwuFRs5ONfp3qqXoMhvkEmcudailcA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌های اطلاعاتی ایالات متحده به دولت ترامپ هشدار دادند که نتانیاهو احتمالاً اقداماتی انجام خواهد داد که می‌تواند توافق صلح جدید ایالات متحده و ایران را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66517" target="_blank">📅 20:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66516">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=GWx6h-i0pEuxGwE_aOgCBmS96AbuiDJGsW6ZT-HCvNHb9ndRJiIcwm0Rp1HbmRKSyQobb4pHnvwaxfeXd6v7zg4elTVRSNBtF5IO6pm2ii9yUFVmIlNpi_VXihtlGBZIxFhPtWI0UBWq85WFkwpjYUat7QWXk58f3y1gZcuaz5GpHb5L-F0Q-nZ2DxCbf8Kcjp183tAEr4-UjDeMZjt0Lo3B0EcQBJXmeAv8XDQmvphCHRpAWsosBRLY7yUAznUIhw7CIJfmVetrD2waI2-_QKhQkI46fjwZsBDT3Ru--VHm1LosqIjxV7LJ54RoW17PkSpqGUcQ26mfFHYNr6pjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700e55c3c3.mp4?token=GWx6h-i0pEuxGwE_aOgCBmS96AbuiDJGsW6ZT-HCvNHb9ndRJiIcwm0Rp1HbmRKSyQobb4pHnvwaxfeXd6v7zg4elTVRSNBtF5IO6pm2ii9yUFVmIlNpi_VXihtlGBZIxFhPtWI0UBWq85WFkwpjYUat7QWXk58f3y1gZcuaz5GpHb5L-F0Q-nZ2DxCbf8Kcjp183tAEr4-UjDeMZjt0Lo3B0EcQBJXmeAv8XDQmvphCHRpAWsosBRLY7yUAznUIhw7CIJfmVetrD2waI2-_QKhQkI46fjwZsBDT3Ru--VHm1LosqIjxV7LJ54RoW17PkSpqGUcQ26mfFHYNr6pjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم، دبیر کل حزب‌الله:
امروز در لبنان، ما با خطرناک‌ترین مرحله تاریخ خود و بزرگترین توطئه مشترک آمریکایی، اسرائیلی و بین‌المللی روبرو هستیم که آینده کشور و فرزندانمان را تهدید می‌کند.
هدف اصلی این طرح، ریشه‌کن کردن و حذف کامل مقاومت و پایگاه مردمی آن در لبنان است.
دشمنان برای دستیابی به این هدف، ابتدا جنگی جنایتکارانه و بی‌حد و حصر را آغاز کردند و با کشتار غیرنظامیان و تخریب گسترده، مقاومت را به زانو درآوردند.
در گام بعدی، ایالات متحده و رژیم صهیونیستی پس از مشاهده تغییرات در معادلات منطقه‌ای پس از تحولات سوریه، توافقات قبلی را نقض کردند تا موازنه قدرت را به نفع خود تغییر دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66516" target="_blank">📅 20:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66515">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=B_jGG-Ppd312vlS9pDTTL8_QGBn75-fxQr4tk8dLSN79ZO9GkQiHZd8geNLfc8-kCUdEFvjtq5jmaQwN5WjU3Ta81N3IsSUI6T-QDpTz15_0U4v6-D8bzwCDobO32g2fx0UpknTvS6Df3Z-FfkuJpjWvhxx8QHAyBF0DU0PPrrD7F6xdEZznQvt-JVaWmvtz2TX-pJwFIGrVCkLhXWoR5LlDs-R-ORls-ifZLR52KRT8CfcnD-GDkI20tLkoBykHOOX05unx7P23P1ZZ_H3mGpdv0kKtLOpcpUFt-USvMLTXhmiZn9MdTfbuF4IRwBoV3oIPy0AlNf0VAC3JjZu-lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f332c84e.mp4?token=B_jGG-Ppd312vlS9pDTTL8_QGBn75-fxQr4tk8dLSN79ZO9GkQiHZd8geNLfc8-kCUdEFvjtq5jmaQwN5WjU3Ta81N3IsSUI6T-QDpTz15_0U4v6-D8bzwCDobO32g2fx0UpknTvS6Df3Z-FfkuJpjWvhxx8QHAyBF0DU0PPrrD7F6xdEZznQvt-JVaWmvtz2TX-pJwFIGrVCkLhXWoR5LlDs-R-ORls-ifZLR52KRT8CfcnD-GDkI20tLkoBykHOOX05unx7P23P1ZZ_H3mGpdv0kKtLOpcpUFt-USvMLTXhmiZn9MdTfbuF4IRwBoV3oIPy0AlNf0VAC3JjZu-lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
پروژه نابودی حزب‌الله شکست خورده است، نقشه‌های اسرائیل به بن‌بست رسیده است و پیروزی نهایی، یعنی اخراج کامل و قطعی اشغالگران از هر وجب از خاک لبنان اجتناب‌ناپذیر است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66515" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66514">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66514" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66514" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66513">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66513" target="_blank">📅 20:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66512">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
نعیم قاسم، دبیرکل حزب‌الله لبنان:«تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
حزب‌الله خلع سلاح نخواهد شد. این سلاح‌ها برای مقابله با اسرائیل هستند.ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
«ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66512" target="_blank">📅 19:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66511">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7mGL6Drv0dTOHsjjPIAnyAT2gu3jrOGiI4a8bk6riMslyZa_QWg05GG2g6hyWHfLoXzbbLUJZXlG1_ywaEGmCPrmgpKzAdSqVfDXmThf_NSwYe2fayMYFWK3MiMmE0-0fVoi1oP-7zIrxXrOBiLC-5g_gw59rl3iRSzgQHw-YLhcqr98hejE8eL1zB16E1I5ZNGnmZo8isX942XZ3Im-H9SDeoY3FSl_7Q6keCj1XfScYjrYmMUYqrkUjKjKQbAzL2HJGqO6w8dJ3ENHdCaoKlTGppd4tyIa1D8kkkZKoifpjeystCOQ25wyE8zOdY86P-w6TgzOYA1FsP-YTRGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اتاق جنگ اسرائیل:
رژیم تروریستی ایران از نیروی نیابتی خود، حزب‌الله، برای حمله به اسرائیل استفاده می‌کند، به این امید که بتواند وقتی اسرائیل پاسخ می‌دهد، اسرائیل را به خاطر از مسیر خارج کردن مذاکرات سرزنش کند.
ایالات متحده باید به حمایت از حق اسرائیل برای دفاع از خود در برابر رژیم نسل‌کش ایران و نیروهای نیابتی آن ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66511" target="_blank">📅 19:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66510">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=p9BWLibB5Gcpu74VmojHHdCHKaKtdk3NV1w1q63xt3cIfFxsrqXh7YRT5fg3s4XSwQ5Xb7y_uiJSFiQvZLiU0XnX7fdaUgt2OTupLWWrGOpaHBTTk4jOBwLn5TMXKa6QeAEyXNJVCbSPD3B2GdcfNopEX9VlA27Bi_p79tRqhdHiUToeEiecdPC4XXEa3T5NjmSp69zWb83zDgMMkp8-PrgqSe4nwotFwUHK9p77QuLfBz9qL34SowOQ7z4VU0uCPTmnBJBg8rolm3dFntjPQOvOFzSMARgWlr1mXQ2-Ot2t_AdDuGC56UNgbTL5T2ee1OPFbWelYELs2J4HEMY4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0ea7af18.mp4?token=p9BWLibB5Gcpu74VmojHHdCHKaKtdk3NV1w1q63xt3cIfFxsrqXh7YRT5fg3s4XSwQ5Xb7y_uiJSFiQvZLiU0XnX7fdaUgt2OTupLWWrGOpaHBTTk4jOBwLn5TMXKa6QeAEyXNJVCbSPD3B2GdcfNopEX9VlA27Bi_p79tRqhdHiUToeEiecdPC4XXEa3T5NjmSp69zWb83zDgMMkp8-PrgqSe4nwotFwUHK9p77QuLfBz9qL34SowOQ7z4VU0uCPTmnBJBg8rolm3dFntjPQOvOFzSMARgWlr1mXQ2-Ot2t_AdDuGC56UNgbTL5T2ee1OPFbWelYELs2J4HEMY4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
«هر مشکلی در خاورمیانه مستقیماً به ایران برمی‌گردد. حزب‌الله؟ ایران. شبه‌نظامیان شیعه که عراق را نابود و تهدید می‌کنند؟ ایران. حماس؟ ایران. حوثی‌ها؟ ایران. اسد که در سوریه مردم را قتل عام می‌کند؟ ایران. این رژیم هزاران هزار نفر را کشته است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66510" target="_blank">📅 19:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66509">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6rCyzYnF8UwTpJ8_AdIck0Er6iJdNBbKCD1ecbgqaouEo22_t3AqiEsD1xc2-zVlTLMGXAimiB6S6HASg110zsUlfOQv6Yl2P5fthb1pMKM9vLc8gNwcSJlgEYgmRDEI6HGLB_lT0z6XC23a4EkONTz64jr8QzHjfcD70BVjX0IefaYpLo4NEMX8bmmHad9eGx3Y7ANI4_Hoh2JszRGD8XvsqUjZowtAogHcz6VftwEplDK9Uv2vT8NffRJSM5yuwrSBQIpp5szM6l0if21cd1KKRSNwwDzU1b1hajvazpKm2UKjqTMv17fP00wZdRNreInJsesIWn24nFMwjH84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اسرائیل هیوم به ترامپ:
می‌تونستی بزرگ‌ترین رئیس‌جمهور تاریخ باشی، اما شکست خوردی
شما به منافع جهان متمدن ضربه زدی و ممکنه به‌عنوان رئیس‌جمهوری در یادها بمانی که باعث تحقیر آمریکا شد
به اسرائیل خیانت کردی و حالا تمام تحقیرهایی که قبلا باهاش روبه‌رو بودی، کاملا موجه به نظر می‌رسد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66509" target="_blank">📅 18:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66508">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ:
ما از روی استیصال پای میز مذاکره نرفته ایم.این ایران بود که از سر استیصال آمد. کارشان تمام شده است!
ما این دوره ۶۰ روزه را تا آخر پیش می‌بریم. آن‌ها هیچ پولی دریافت نخواهند کرد؛ حتی یک سنت هم نه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66508" target="_blank">📅 18:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66507">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=KMqxNyYz8NGxuZK5bLOPeek1iyS3ojo8MAzjvNOP_PkdNgzKhYCfJvRDn79eZ6B1P9PqtW2znVF9BDiFKgGWdA4u_TPt0ruVrdo7FZlfpROFQIwXz0WsZ-keIcRxVaXybhUFApNvEv2pQKRt4duhXQbWSmjlKxXt8hr9KdFAvJOfv8xqN0ZEpGUcgI_glzN7mYWTtmfTMtcrBzN_g9d578em1FpE0oX20RdGK0oVcQTNHXkx6IUieYuiwpjd9LtWTctYj8LUzIoHIFQfrNgeq104LS5_cuiEaJaqliNQPqkxU5JIuqquxv1cge5kzGsd7J7vwSx98P5y79AqMGIchA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c09804d09.mp4?token=KMqxNyYz8NGxuZK5bLOPeek1iyS3ojo8MAzjvNOP_PkdNgzKhYCfJvRDn79eZ6B1P9PqtW2znVF9BDiFKgGWdA4u_TPt0ruVrdo7FZlfpROFQIwXz0WsZ-keIcRxVaXybhUFApNvEv2pQKRt4duhXQbWSmjlKxXt8hr9KdFAvJOfv8xqN0ZEpGUcgI_glzN7mYWTtmfTMtcrBzN_g9d578em1FpE0oX20RdGK0oVcQTNHXkx6IUieYuiwpjd9LtWTctYj8LUzIoHIFQfrNgeq104LS5_cuiEaJaqliNQPqkxU5JIuqquxv1cge5kzGsd7J7vwSx98P5y79AqMGIchA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
همانطور که دستور دادم، ارتش اسرائیل با قدرت به ۱۵۰ هدف حزب‌الله در لبنان حمله کرد و ده‌ها تروریست را از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66507" target="_blank">📅 18:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66506">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66506" target="_blank">📅 18:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66505">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=n4DLdC43PtyauUwN15eesAk_m2apXkq7DJC3jHqWCLK0I8fsOuH8VpDU43ZyZVqo_E6dILPNKZaz1CwLj7Ged9UbJjUYHYUpkYb5DAszKM0vGcVL2h9tc7HsZsnFylafMbaKYLN5HZGHm7bKD9h-1jV-DMFvbLKhYb1fkm8_VJklu_siVB3FNRXtU0LJBlf4_kNQdRcmDyFuYwg-BGShqvIm8m6rg6N-i5xxzMPNx2P6uMWnmdkYMbhrHB4VZK6YodW89YCTAwvL0sm92Nr-T7cfw4yIa0Rv9G3zjvhm_RhdkC0RSnvHghuwUr9n1f9v7qJD-YYijOsmHJx7AWtGRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa1be6643.mp4?token=n4DLdC43PtyauUwN15eesAk_m2apXkq7DJC3jHqWCLK0I8fsOuH8VpDU43ZyZVqo_E6dILPNKZaz1CwLj7Ged9UbJjUYHYUpkYb5DAszKM0vGcVL2h9tc7HsZsnFylafMbaKYLN5HZGHm7bKD9h-1jV-DMFvbLKhYb1fkm8_VJklu_siVB3FNRXtU0LJBlf4_kNQdRcmDyFuYwg-BGShqvIm8m6rg6N-i5xxzMPNx2P6uMWnmdkYMbhrHB4VZK6YodW89YCTAwvL0sm92Nr-T7cfw4yIa0Rv9G3zjvhm_RhdkC0RSnvHghuwUr9n1f9v7qJD-YYijOsmHJx7AWtGRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محکم تر بززززن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66505" target="_blank">📅 18:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=ecwvnVsn4u_oq1yKRRgoCH20BCMe1uS1T0aO8wB3Kj6H3V4UowyodH7lD1sJJNWF8cULGduple-2hU3LxBS0Ioqiat5khcDjwDVjrcFy24xCmMGQoI0DYMBGiT8EUMypwodNnVZVsHi6elAHSOk7YottAYtfd14B9z_2yh4kKFw4GcqTNSd0UHnYL23eRjLw-L0OOoAsRBLfFi7JKI20KrAOuxxDpyTbSVb9ijIc8nrkX1Byo2ayWKYs_DCCnCfP5qXdt1ij8zWZzrwrVehu8nX60PfKs7ZVTLs04DcNgNCDZze98_hrbsrNEYJG7v53EuGstjjLSkpCuULLUZal0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b87f1a5b.mp4?token=ecwvnVsn4u_oq1yKRRgoCH20BCMe1uS1T0aO8wB3Kj6H3V4UowyodH7lD1sJJNWF8cULGduple-2hU3LxBS0Ioqiat5khcDjwDVjrcFy24xCmMGQoI0DYMBGiT8EUMypwodNnVZVsHi6elAHSOk7YottAYtfd14B9z_2yh4kKFw4GcqTNSd0UHnYL23eRjLw-L0OOoAsRBLfFi7JKI20KrAOuxxDpyTbSVb9ijIc8nrkX1Byo2ayWKYs_DCCnCfP5qXdt1ij8zWZzrwrVehu8nX60PfKs7ZVTLs04DcNgNCDZze98_hrbsrNEYJG7v53EuGstjjLSkpCuULLUZal0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از لحظه سوخت‌گیری جت های جنگنده F16در حین انجام عملیات گشت زنی بر فراز خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66504" target="_blank">📅 17:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=enHo7_5C95e7zIRKSSLZvFBM8Q-IQK1fGEqYuY_UPkC_ANjbZQlAMqxDgxrSYxE9_iQKz8YddZZTTF-_-q9EXFCOm0lRoqzITQ-F4OUw5X8QdD41CapSzXXI5UY34mazwcYFqv8gBk5yZX7uHq95_C4YkzKe47XPiEtz34Z3gjgwxjNLwBmgKREBKiyjPnjChNGxofGCyuc4VCPpB844nqJ0w2vqqZcyEgCo7Uzq7geqgB9HvOCEwQl3S6O55S_jlrLBC-rlc0AQz4wzSqwLixfvCzNe8s6Q8LgEKrH1SBqGOYZ2M2x2JFkLj1WxJrnaupuCOL5VI7K085Z_g091IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3273d3f5c.mp4?token=enHo7_5C95e7zIRKSSLZvFBM8Q-IQK1fGEqYuY_UPkC_ANjbZQlAMqxDgxrSYxE9_iQKz8YddZZTTF-_-q9EXFCOm0lRoqzITQ-F4OUw5X8QdD41CapSzXXI5UY34mazwcYFqv8gBk5yZX7uHq95_C4YkzKe47XPiEtz34Z3gjgwxjNLwBmgKREBKiyjPnjChNGxofGCyuc4VCPpB844nqJ0w2vqqZcyEgCo7Uzq7geqgB9HvOCEwQl3S6O55S_jlrLBC-rlc0AQz4wzSqwLixfvCzNe8s6Q8LgEKrH1SBqGOYZ2M2x2JFkLj1WxJrnaupuCOL5VI7K085Z_g091IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ بعد از نشست G7 پشت سر جرجیا ملونی نخست وزیر ایتالیا گفته:
این زن همش التماس میکرد باهاش عکس بگیرم. حالا جرجیا در جوابش گفته:دروغه، شوکه شده‌‌م. نمی‌دونم چرا ترامپ با متحدانش این‌طور رفتار می‌کنه؟
ولی یک چیز رو به خاطر داشته باش: من و ایتالیا هرگز التماس نمی‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66503" target="_blank">📅 17:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66502">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
منطقه امنیتی در جنوب لبنان ۱۰ کیلومتر امتداد دارد و ما به تقویت نیروهای خود در آنجا ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66501">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbR5ZD66RZaBnv954oOMvA9f9mPnRCEnPyRyknnvh0_uIjsFMidWl8-Rhyt4wr36oLvZXDNdIMe-wygsEJcwG2r5olL6eLF6WIo9ZAc4jd9316ldWe1nC-pq2_Sh4weD2verfj0oGW09-qKQNR3KcNMOwEIOkEjWGzxixiN2REQmBqle1XAlrtS9yR5yG74O0l4irnydv9cKtpqoakRAzCNi1BcjMHCgULbS2eW-G58ZPBq0xw7O6Jh2NvNVCQcx3Zv-rkLbie68SvXY5LYt5dHqqi8B6-rwdUbjI-WZN1McY_jjAYvK6HN6QH9dsYKmhzC8cDOto3ztAZG12BELgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و حزب‌الله به توافق آتش‌بس جدیدی دست یافته‌اند. حزب‌الله از توقف بمباران اسرائیل و پایبندی به توافق‌های آتش‌بس قبلی خودداری کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66501" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO-zNL4wQoLf3selQ3gimy7yD-XquglnOhhYMyl9cfGIp-eRuNLnRd4Cc5l1rpFnMe-8CG81Ctbtg1Gf2581_d7iKImWiIC403KwLxBuY4tojKAvFLxd4RjdRVDNCNVntFcjLQGm0CgPR0Z-mKpORGAEMGPLsQ7_GogXNxOVeMpDcpxcBa9LtP-QQj3KM33GYYd6Hd-hB_5iBhVVRzpS6WgqBnpkNmegU3X9th7_IZEz4t4hXcTv5eDsjeCZJc4OT6_TJFv6rEWRAEZsGrpkJgO_UTmTYa7JNY2CZXiGbjT3A3cM0xRKoJGjde3xKIXxQPRh6AJao-OInIn-bCdztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:
یک مقام ارشد آمریکایی به من گفت: اسرائیل و حزب‌الله بر سر آتش‌بس مجدد از ساعت ۴ بعد از ظهر به وقت اسرائیل توافق کرده‌اند. این توافق جدید با میانجیگری آمریکا و قطر پس از مذاکرات با اسرائیل و ایران حاصل شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66500" target="_blank">📅 16:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66499">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN10jcOYzL_U5YhQfuB6p7P8zOY4dptDatzwSuA7l9EhXsk1eHgMM5iQRvAZSu7Wqbo3_PWz1OkafNhv04l-6fbYPVTYJrvJsehUF9mwCdk0GNlwbPsSzxDvDvMn5QYTdJPb9tge7fsEkXbK9z6AbvQEsb1OX27qyQDZdZaf6MOSUP-V8RZLwT980lv7scv7lnMDQ9PbcHJfJBMT5FOqYct3p1XeyJxKCX3ZSYl1ZL1ZSFdvfvVmrsWsdarh53XO5TYvbU64S5-wkHMdqB1PtXjtsEsoIeZ4gs5YD0Wrhub9i0tQzLKc4MIPScq_S1RonCAp099cgTbIlBTgiLxOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما از روی ناچاری ملاقات نکردیم، ایران این کار را کرد. آنها کارشان تمام است! ما 60 روز را بازی خواهیم کرد. آنها نه پولی می‌گیرند، نه ده سنت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66499" target="_blank">📅 16:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66498">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzwlYHcOc-lgIqDUqZ-Hpjm4_ntEoHm8yT56qNKFR9enTvRjRakYimyTb20NcywYlvgD6Jul7H93cxAFlc_he-30UAR8XkElBVSWyrkKwQSaoa1XJ7Jm661sY_h6Q_jjiICJ5HgP32_CdNFSWrG16gO__bQnEvjXFURTFQf1Zf83bXasL0zTbKZLh3v1OjyrRnCriAmRMNUSxrI0pltGK-X9Eci2S2YfRC0UgPhklSFazLmVzK11UAaVy5eECz1n7_HdHw9b8LJqxxVk6FehvxmfKXZSOSpe-Ig0llP2d0d_D7ZKLLe-C8ztjHn7eViTt4VaGW_4HQgB52a026hkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
این جنگ ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات پدافند هوایی، نه رادار، و تقریباً هیچ چیز دیگری. با این حال، دموکرات‌ها می‌گویند ایران اکنون نسبت به چهار ماه پیش وضعیت بهتری دارد.
می‌توانید تصور کنید که کسی چنین حرفی بزند و از آن جان سالم به در ببرد؟ بعضی‌ها واقعاً تا چه حد می‌توانند احمق باشند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66498" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
‏اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا مسئول حملات اسرائیل به لبنان است. جمهوری اسلامی همه تدابیر لازم را برای صیانت از منافع، امنیت و حقوق خود و متحدانش اتخاذ می‌کند
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66497" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66496">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGeCmH3l01yftGi832iFzecpkVqztOXi-SbWc9bsixQRXHNds2TwdeipjD2dcyptAUylOp636AGIn8ep79xAmmzEc1-J4i2IQ5s-td8xoPMIy4DF0kmJ3GRfENVsKI1KTyImrr3DLNqD33ViXNJuVwjEJDDhUYcItIQjCtlQENKC48V744Lg5qg4bpJ0smRYYp6TIHglSY72DpLf1u26fuXaY1MPNsZTn3F8eSQegaNfDGXX62AowKclVTYv5g9CKZLpdzgrOrTNvQs4cTHF1EMj29ukW2Yg13E2FjDIkc7JFbVgu0y0Ul24WSLI8xAyRF7Md3Co0uhE0SszQyCIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66496" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66495">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=oTkW_Qatdll-6oVDC6GmGsYbNTdE-5Xu63LdfhIQDpKF8KxK1bw-fbmnXQ6ITgiun2-D-FomNs1JRGun0SNf_UzDhpcrYBQPl5uOc0bptsVAKUF3dAa2N7axKiw2X9u29N-RxbwVi9CMxNfZGuKzBAB4sA6QGURo7iosQTw34t0ZtiHAWlnNxVHeRIUmnYafVzCOS0GLzmEqtZ9Um4KrVo4cges413EN7wo2kxLu9jsX_kxjqfUsmsAJM3fDMJdiQTQ9gox5juK00iSxcpKA4smOEXaMdz3cnNChdvvSh0NaZ3uD8jVRFyMbQo52BnR-g8FBIf6kZKlLVnGUzm7LkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec2c7bdfe.mp4?token=oTkW_Qatdll-6oVDC6GmGsYbNTdE-5Xu63LdfhIQDpKF8KxK1bw-fbmnXQ6ITgiun2-D-FomNs1JRGun0SNf_UzDhpcrYBQPl5uOc0bptsVAKUF3dAa2N7axKiw2X9u29N-RxbwVi9CMxNfZGuKzBAB4sA6QGURo7iosQTw34t0ZtiHAWlnNxVHeRIUmnYafVzCOS0GLzmEqtZ9Um4KrVo4cges413EN7wo2kxLu9jsX_kxjqfUsmsAJM3fDMJdiQTQ9gox5juK00iSxcpKA4smOEXaMdz3cnNChdvvSh0NaZ3uD8jVRFyMbQo52BnR-g8FBIf6kZKlLVnGUzm7LkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66495" target="_blank">📅 15:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66494">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=BO7ZHYiScf1qEMrfg42xhBdfuKA97P4fIDRbzR6RF_rpEOVf0wWGNnEYC3La2pgeZKY4SWsDN7PtIRJLnYMNiwYhJXSt9jh03_VlexvAiwVAVUqGjPtTSjtTuA-9ih_uUCEa08s9epAeluorhGBl9j2jU9ls1NRkO78hF4-QFCq06jh_ei2-ovtZV547X4MpqxDh9vc-t0Sd3iaZkLdaVH5hQ-O6QfbgFJHzHYgT1GLUZR3NDx3U_k-rEGqmCLrW7ptmz1AuOZCokadQuZbydIY90heGbW5xe_zFwBpIr3yvIv2Th2QPn-Kfpj98Ea-cvm0KO5QuFrg1ynkTlrSfrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f017f858a.mp4?token=BO7ZHYiScf1qEMrfg42xhBdfuKA97P4fIDRbzR6RF_rpEOVf0wWGNnEYC3La2pgeZKY4SWsDN7PtIRJLnYMNiwYhJXSt9jh03_VlexvAiwVAVUqGjPtTSjtTuA-9ih_uUCEa08s9epAeluorhGBl9j2jU9ls1NRkO78hF4-QFCq06jh_ei2-ovtZV547X4MpqxDh9vc-t0Sd3iaZkLdaVH5hQ-O6QfbgFJHzHYgT1GLUZR3NDx3U_k-rEGqmCLrW7ptmz1AuOZCokadQuZbydIY90heGbW5xe_zFwBpIr3yvIv2Th2QPn-Kfpj98Ea-cvm0KO5QuFrg1ynkTlrSfrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیا می‌توانید جلوی حملهٔ اسرائیل به لبنان را بگیرید؟
ترامپ: «بله. آن‌ها احترام زیادی برای من قائل هستند و هر چه بگویم انجام می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66494" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66493">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66493" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66493" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66492">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQsxB2VDAB6UQwEhyIqdgOxOB_sYv72lbEP78b0tgr2o1Dj-xHNTFOZjNBbRLRnDfNjdr9vKPLcV7evTshXa6VkDo7S4Q3heMFaiEWDBsvDCN1-BgJ1WBxRXR1bjQz7AJKombqIGSBVVih58HXMUkgmUrJTJlMuzxPnDlzM4NUJn7j6t0OWy_M7RWwrIX-hn7h53VvXR5YM3aVZVF5sqa-gz_GdY9hlKHXRlG_lOkGE_W7--mZNlcXTFHiftOHBFE-IQDqZ4CCGkA4hxiYJWlZ1p1JuGwl1BqYBLnW4mxEBlxk6evrOTXFC1bEkD9k8D34DQ8LQU8tI18oc3gt-chA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66492" target="_blank">📅 15:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66491">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GB_w8Gzf48sNP8ZlWCudv2izdjAshi_JCiZ9ZYglj_z8Stc5i5OyMIVBQgjFZPWlR_5Lk13n1sNC16YMv6FJRtt_8nmWlHibdJUI6xDwpjKxdBo8dCjBQ-cXCYSXp4yLz56Iah7fPFhwpSIJHz-cvMb88j6S4OCfnEeau8OhmlA_hjvn3Bit13rlzOblJ_6hqp6pQUKdUDvsMB6YO8vR0EjhFRx0HK-4X2Rg4DaOuJh72XS1WQzlHvzrM70Rong9qKcXoXv1eejUecc89LYTL-Mns042GcLApfNJE2DyGQR8G9SRiQ_VT97H6WkpXJNxXreTlBbDr6kqj6fqUJ5j4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به فارسی؛نخست وزیر نتانیاهو:
پس از حمله جنایتکارانه حزب‌الله که نقض آشکار آتش‌بس است، دیشب به ارتش اسرائیل دستور دادم که با قدرت به حزب‌الله حمله کند.
ارتش اسرائیل به بیش از ۸۰ هدف تروریستی حمله کرد و ده‌ها تروریست را از بین برد. متعاقباً، ارتش اسرائیل امروز صبح به مقر حزب‌الله در بقاع حمله کرد.
امروز صبح با وزیر دفاع و رئیس ستاد کل، ارزیابی وضعیت را انجام دادم.
دستور من واضح است: اسرائیل حمله به سربازان یا خاک ما را تحمل نخواهد کرد و بهای بسیار سنگینی را برای این حملات از حزب‌الله خواهد گرفت.
ارتش اسرائیل برای خنثی کردن هرگونه تهدیدی علیه نیروها و خاک ما اقدام خواهد کرد.
همانطور که به صراحت تاکید کردم: اسرائیل تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهد ماند تا از شهرهای شمالی محافظت کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66491" target="_blank">📅 15:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66490">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=UHg-T6nHJYem_-LHGaROUCQAtL5YcMJLsMJy8Hs68tYqLfTRZk6-rJ0nQ7O6h2eJdq0nfvcSYgJnGGe-jDg3k2u5CHXofBBzw72xmON-6s6Jof8rzvEKQb_9odmxVIg6UgPkpMh35aSl694jOrykjaLwNp0F_tLB3vJMDdJTLMvVa5mI5f_gDJPEuWC3wenUgIMgSp-8pl1Ai_UiRVy6tXwGm6o3KqzoNS0Mcpph_f3ylGf83OI8cQpq8oSmtDA4gx7JI7ufFESF4XUNFp0CujASu9tpt_B5y6lXxrtRbvW15ObP8_Kt_IwPaT6Ce8paSHippO1ewyZ3O6LkecVjnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc6524eaa.mp4?token=UHg-T6nHJYem_-LHGaROUCQAtL5YcMJLsMJy8Hs68tYqLfTRZk6-rJ0nQ7O6h2eJdq0nfvcSYgJnGGe-jDg3k2u5CHXofBBzw72xmON-6s6Jof8rzvEKQb_9odmxVIg6UgPkpMh35aSl694jOrykjaLwNp0F_tLB3vJMDdJTLMvVa5mI5f_gDJPEuWC3wenUgIMgSp-8pl1Ai_UiRVy6tXwGm6o3KqzoNS0Mcpph_f3ylGf83OI8cQpq8oSmtDA4gx7JI7ufFESF4XUNFp0CujASu9tpt_B5y6lXxrtRbvW15ObP8_Kt_IwPaT6Ce8paSHippO1ewyZ3O6LkecVjnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66490" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
