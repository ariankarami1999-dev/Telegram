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
<img src="https://cdn4.telesco.pe/file/RphuTCfrxuxxe6lK-0EJ-_tqfcS_xT4QZ6cnUajj8RB4WSj2cLqX2mlmeFTMYkzS2Qisd8bmt1_IeHlbcGrLxjigrfNEvuaYQpdGvP3TNpwK7Gpbit6vnQjQNmMqNOwmblgTt3e7RqnTtgBovIbDkjXjdnSVaZ3G1-ND6_d5_jz-bIwtEOwwgVKjFPsXQLRrM-D5M-S6kLOInxOhWSXRblQEHu8ipkd_xzLRv0p-Vg5wv3cbHD2Ar6yJ60yjKUqLKAmkoF-G8exAyIZdl1UqZr-VEJzq6K9zk3npqgsY-zuXhlFMZ03ud4ywOwXnvUzpbYvrUPe0nWmMgqXpXqCaLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 04:34:58</div>
<hr>

<div class="tg-post" id="msg-446534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد @Farsna</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/farsna/446534" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7833e3d388.mp4?token=AZWDPkTGL3YxCxc6Ktf0a5qO6FivJO80SfaI76F_M_pspInsdSLuD0xLolxm197PHuk45v9-hgbqdD4wY6WGGnhe8i7cxKJPQTn8MnJmF8I3dqU3V3YW6oObIhP_LE8W4Wum8kaY8aRwEUNZ_BLZ5oOV3bmjPEMXKoY-mYtdNwX-lA-unJeXCI8p55WUohAdAYEoqv84tuixwY2VmfNKa3wgChDojTCazK1VCZcGHnjIlXPsoaN8uVafSP402xD5Xw620Gzxb8pLeBRFI5Eso_wzEnS8rGiFkegM98nKWghw0uJAxP-IjgmtEcz8nZg4IvLpvdX6_BiYkULvj-S2YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7833e3d388.mp4?token=AZWDPkTGL3YxCxc6Ktf0a5qO6FivJO80SfaI76F_M_pspInsdSLuD0xLolxm197PHuk45v9-hgbqdD4wY6WGGnhe8i7cxKJPQTn8MnJmF8I3dqU3V3YW6oObIhP_LE8W4Wum8kaY8aRwEUNZ_BLZ5oOV3bmjPEMXKoY-mYtdNwX-lA-unJeXCI8p55WUohAdAYEoqv84tuixwY2VmfNKa3wgChDojTCazK1VCZcGHnjIlXPsoaN8uVafSP402xD5Xw620Gzxb8pLeBRFI5Eso_wzEnS8rGiFkegM98nKWghw0uJAxP-IjgmtEcz8nZg4IvLpvdX6_BiYkULvj-S2YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوای دعای عهد در مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/farsna/446533" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446532">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78bc76f0c.mp4?token=YKpOLWnLshjAroJikDGrHaOiVg876BG0Ztqfy84RfLN0jo69NisBeNsSQRRbqP39SCs4OcXROyc-BWnLSFmMwu5YPEOyoy4z0M2J5BNMwntvem0lGipJY7EmZzq8xWch3iCikWvvVH7teU__YzZ5I9wwNwFLqubk2cYej7xIPW1NlRPBie4VpcCMCqcvm6tqaHkID7Uskb6WG3mvIM4nC5ufwouwIXpX9vhCjqCCqzyKA_TKpkETfeG4oZvoEY82-OvaFjEEfRrcCtrBuryY8Rk0N2Albs2zE1GsEZH8oJZGuMpio5mbcqEhbB7TBFzb8Xse_NJo0Atst5rQCqVMDaXkgoRQbA9-aPBB-wPNmI5jtg6Fyq2KdXuAurwA_htw50GDlmzeBPObff0Fp8gFqWcB2qUMywFJQLpc9VXsQx3Cj1lwxrPxQ4ryPj3147ONpNxv4dFjF0XOh60RazUkzdfMMnoGHMb5yfGrY6G__dAMC6RVKWJRKlDyaZFniT4ZyDta1f4NAhXd7k9NLXh9vkbPzlmieVQ2wz1zq9-nbLYFqFV3TAc1lnI6d_HSJyhSkSROV1S38pG47hXEUSEaL0Mc_T6SI14EPB_TVQ6vLoWbZyD_mcayfm6JA4ON8_jvJoDt7qNBNSex5VY6CinobO2fWkj66CL2Qikf-jXqmqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78bc76f0c.mp4?token=YKpOLWnLshjAroJikDGrHaOiVg876BG0Ztqfy84RfLN0jo69NisBeNsSQRRbqP39SCs4OcXROyc-BWnLSFmMwu5YPEOyoy4z0M2J5BNMwntvem0lGipJY7EmZzq8xWch3iCikWvvVH7teU__YzZ5I9wwNwFLqubk2cYej7xIPW1NlRPBie4VpcCMCqcvm6tqaHkID7Uskb6WG3mvIM4nC5ufwouwIXpX9vhCjqCCqzyKA_TKpkETfeG4oZvoEY82-OvaFjEEfRrcCtrBuryY8Rk0N2Albs2zE1GsEZH8oJZGuMpio5mbcqEhbB7TBFzb8Xse_NJo0Atst5rQCqVMDaXkgoRQbA9-aPBB-wPNmI5jtg6Fyq2KdXuAurwA_htw50GDlmzeBPObff0Fp8gFqWcB2qUMywFJQLpc9VXsQx3Cj1lwxrPxQ4ryPj3147ONpNxv4dFjF0XOh60RazUkzdfMMnoGHMb5yfGrY6G__dAMC6RVKWJRKlDyaZFniT4ZyDta1f4NAhXd7k9NLXh9vkbPzlmieVQ2wz1zq9-nbLYFqFV3TAc1lnI6d_HSJyhSkSROV1S38pG47hXEUSEaL0Mc_T6SI14EPB_TVQ6vLoWbZyD_mcayfm6JA4ON8_jvJoDt7qNBNSex5VY6CinobO2fWkj66CL2Qikf-jXqmqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد @Farsna</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/farsna/446532" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446531">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93cc5c358c.mp4?token=vnmid6sS00lxB9yoP_iigdL35zlUBfTZFMgkplzBNc-4wGjzyyxcNsCzJH9huISRQC2nYNRmOgh_2moD6ATm-MwNQU5FNviDrSr1MNnN7XSZI66fYL68hSgj59qe-mYYCdN-h8yq5ctudXO9LyKp4tR6-fnfCGc-38aFoKF_NPhZf5uKpjBShYTEPJ2q5KD29b3816v4eoappDDSF66VLNaFzFaWpYxQiJ4d-0yzkGB_aw3vOmtGQEZupl_MGiYltPXkP18bXc6jo0RYE5gE0uZ-IC7If-OJ45rVGUP1B1GLXpOpWJmKoU_DyynFBflzrq8Yy1KxL_2HZVDCH9U-BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93cc5c358c.mp4?token=vnmid6sS00lxB9yoP_iigdL35zlUBfTZFMgkplzBNc-4wGjzyyxcNsCzJH9huISRQC2nYNRmOgh_2moD6ATm-MwNQU5FNviDrSr1MNnN7XSZI66fYL68hSgj59qe-mYYCdN-h8yq5ctudXO9LyKp4tR6-fnfCGc-38aFoKF_NPhZf5uKpjBShYTEPJ2q5KD29b3816v4eoappDDSF66VLNaFzFaWpYxQiJ4d-0yzkGB_aw3vOmtGQEZupl_MGiYltPXkP18bXc6jo0RYE5gE0uZ-IC7If-OJ45rVGUP1B1GLXpOpWJmKoU_DyynFBflzrq8Yy1KxL_2HZVDCH9U-BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمدیم حسرت دیدار به دلمان نماند؛ روایت حضور نیمه‌شب مردم در مراسم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/farsna/446531" target="_blank">📅 04:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446530">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ed610c9b.mp4?token=FvFEssudv6eBv0Yopg61v1tntH_680FgO7T_lVU7HWB5Roy0rbPSkISsnCS6qfms_JMwwFKS_HlSXGTPjJ6pm6S2GwA5bvU8UQ2U2xeVuSyfpF_pcQd6rvfzr4YrQG0dPyA6D5V38thh5SjQplyGnIwHOnAhH7WSYze1wBSPYD9buVQ-P9OFi1O6f-dtgBV40riQkO1czCQwnMcbwbhC9PiZjcncYeLZYGhv8DB2opzhnNifVMXR_jP5lrGpTFC4q_lB2dBhSacEb6eyyXR6GbYBoxDAidMzr25Uuw-VtvgZgXfhE38JDbpx9UklYSaNVKAw24HNVQ2IPEKa72itvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ed610c9b.mp4?token=FvFEssudv6eBv0Yopg61v1tntH_680FgO7T_lVU7HWB5Roy0rbPSkISsnCS6qfms_JMwwFKS_HlSXGTPjJ6pm6S2GwA5bvU8UQ2U2xeVuSyfpF_pcQd6rvfzr4YrQG0dPyA6D5V38thh5SjQplyGnIwHOnAhH7WSYze1wBSPYD9buVQ-P9OFi1O6f-dtgBV40riQkO1czCQwnMcbwbhC9PiZjcncYeLZYGhv8DB2opzhnNifVMXR_jP5lrGpTFC4q_lB2dBhSacEb6eyyXR6GbYBoxDAidMzr25Uuw-VtvgZgXfhE38JDbpx9UklYSaNVKAw24HNVQ2IPEKa72itvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارت عاشورای آخرین دیدار با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/446530" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de68dbe7b.mp4?token=of5DiwHLY_ASqsPHMmV02KKEgxfzjAoL4sxavd2OPKgJqbn_hj9PDK9WmofaMOKXmp_4hS2gvUyzTytuzlM6BUzX5o5_JY_T3UBxoSBZl46to64XOKDe8jkKf-d6hwDd6WFu5WrPw862rxyiuhwjfL69pWbuOzDbjsN4Sma0OMK1mRBgbLlzbgRsdReWI_ryOncGUon1QBFKJdljJOeKw8oiGiF-Z31nAnBhwv98msNoUwVwKn9ihcVWRC3wbmT2EEBaZAcEL_62YCeBQ0mn9YB5FjKjMKrE6tndjqnvKE7D3hN49ojKv3VxvX6_2c8BmE8-Z5JCay1EOJU6nC4fng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de68dbe7b.mp4?token=of5DiwHLY_ASqsPHMmV02KKEgxfzjAoL4sxavd2OPKgJqbn_hj9PDK9WmofaMOKXmp_4hS2gvUyzTytuzlM6BUzX5o5_JY_T3UBxoSBZl46to64XOKDe8jkKf-d6hwDd6WFu5WrPw862rxyiuhwjfL69pWbuOzDbjsN4Sma0OMK1mRBgbLlzbgRsdReWI_ryOncGUon1QBFKJdljJOeKw8oiGiF-Z31nAnBhwv98msNoUwVwKn9ihcVWRC3wbmT2EEBaZAcEL_62YCeBQ0mn9YB5FjKjMKrE6tndjqnvKE7D3hN49ojKv3VxvX6_2c8BmE8-Z5JCay1EOJU6nC4fng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای سحرگاهی مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/farsna/446529" target="_blank">📅 03:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49247b4ea.mp4?token=M-cogXWVEisTjGaDNOCWxJf6DzMXUGxWPR81Cg-3OGo0QPd3-cEMWGBHv4uz9Xbh46Lf3zHy2RFC2PNiXQ-JlFbBDykAqUZN-CFcUelTHjDa8nMkBdc7O960Fob-5Ag1T8jniyRHg2iQgB1blXrpaBKBkEFb9HMld-yLPAkaRwN1PyShDAmwb_KhiL3irqLyMT9U0s2lLALiJkrW354w8XQcVOhTLq0p9AunXFvbOKNICRZ-dwFJUFBmYuefsVCu5gsWFFUUMSsQdTPZ5h8fV8nG1fZ2yH2pRogGxhPqrjvx6mbbZFR0heZOjSldEX8bdI99BCBaqiY8eZ5-SkujjDzJ4CVprxBRhXVvE_Zx0th8M50PiOjbNkRJrZy-jzfDupvSrJAyBBxECQlTCfuPExVArOyFpvMowo8r5EI8ITUO6wZB3vrHeHvMpzqCM00Rw4-KABUt3sfjqN_83ajJEzr-Y1pnHBwH9pN00HDkNWfLUFX2CvdAjzMqIBwOzZjXt1gBYy3bpvNKwZ230WonBVXmDw7ShAA_EGSkseVmvvqWDSiALU0JOa8WorbhIFMMIvhDYObYbX0m1aNqJXgGdt3Fkx6TQbIf7xj17QIUFTfiQMpD6VpYpPgustaISpA7m1GservbL9OzWw4z4AkIcXzRd0hSj1hRLbHPYWhKklw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49247b4ea.mp4?token=M-cogXWVEisTjGaDNOCWxJf6DzMXUGxWPR81Cg-3OGo0QPd3-cEMWGBHv4uz9Xbh46Lf3zHy2RFC2PNiXQ-JlFbBDykAqUZN-CFcUelTHjDa8nMkBdc7O960Fob-5Ag1T8jniyRHg2iQgB1blXrpaBKBkEFb9HMld-yLPAkaRwN1PyShDAmwb_KhiL3irqLyMT9U0s2lLALiJkrW354w8XQcVOhTLq0p9AunXFvbOKNICRZ-dwFJUFBmYuefsVCu5gsWFFUUMSsQdTPZ5h8fV8nG1fZ2yH2pRogGxhPqrjvx6mbbZFR0heZOjSldEX8bdI99BCBaqiY8eZ5-SkujjDzJ4CVprxBRhXVvE_Zx0th8M50PiOjbNkRJrZy-jzfDupvSrJAyBBxECQlTCfuPExVArOyFpvMowo8r5EI8ITUO6wZB3vrHeHvMpzqCM00Rw4-KABUt3sfjqN_83ajJEzr-Y1pnHBwH9pN00HDkNWfLUFX2CvdAjzMqIBwOzZjXt1gBYy3bpvNKwZ230WonBVXmDw7ShAA_EGSkseVmvvqWDSiALU0JOa8WorbhIFMMIvhDYObYbX0m1aNqJXgGdt3Fkx6TQbIf7xj17QIUFTfiQMpD6VpYpPgustaISpA7m1GservbL9OzWw4z4AkIcXzRd0hSj1hRLbHPYWhKklw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران، امروز تاسیانه!
◾️
امروز مصلای بزرگ تهران مثل همیشه نیست، اینجا، امروز غم و دلتنگی بزرگی سایه انداخته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/farsna/446528" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f926fd7cb3.mp4?token=rmbOkNiHgwKi3vNHf7FgRXJTcGzXA4xMO7_sn9JI0FE-Bn8watkKc9kKrbCQb0BUCuwbECKqUsFUsCDmauIXOLIz-pb9MiOVReqhJuIoP4P4wCnxN6V2UzB1GZthvyXHY1pmo1XfUDFWmiq5_w_AulO20VxhRq0Q4q5gWic6-H1q6NJAYGoNI9kIOyZ-Jn7IdHiFsN7wrHhUirDO6qmdQBiFD1rv308wQqNUEvdogzLmiFdh9437cU9oVwXYySbrpFAwXmDfAvIfpmlYRtHPdwdWixAAWYMDxvK_hVwrqHMcXURoYpl29d4N981nI4kYqhYUhQPwo6dx0cXsrUqAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f926fd7cb3.mp4?token=rmbOkNiHgwKi3vNHf7FgRXJTcGzXA4xMO7_sn9JI0FE-Bn8watkKc9kKrbCQb0BUCuwbECKqUsFUsCDmauIXOLIz-pb9MiOVReqhJuIoP4P4wCnxN6V2UzB1GZthvyXHY1pmo1XfUDFWmiq5_w_AulO20VxhRq0Q4q5gWic6-H1q6NJAYGoNI9kIOyZ-Jn7IdHiFsN7wrHhUirDO6qmdQBiFD1rv308wQqNUEvdogzLmiFdh9437cU9oVwXYySbrpFAwXmDfAvIfpmlYRtHPdwdWixAAWYMDxvK_hVwrqHMcXURoYpl29d4N981nI4kYqhYUhQPwo6dx0cXsrUqAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورودی‌های ۶ و ۸ مصلای تهران در سمت شرقی به‌روی زائران باز شد
@Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/446527" target="_blank">📅 03:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86a42811f.mp4?token=vF8RN5Yg6aN58Rr8b2pbDwwpj0hzT7yFmhd-2Motp2dtsDBd67EekIHxalVWsS_E0DcKLwLYuRchYtFlpLAtkRtdNkn7yFps2ZR-9nxk5BLE9z-UJBe_fjiyYuZKnt1Iyk6h2I9B3K2-6gnI9XUBRU-fZnlamGRTBRi9SVaHyyFNKf0-pQjG1Vs96Um1CyjHX6A8zLtb1fhpILOEBYlW6TCG2axLZOXy7keYw7IL7QCOEmgx7jKF8lc7yPfG6SA4BDDoydb3ZBxg8r0IwDpW7oFtHq4bTSK2gJasoF4Ctu9-HWK-BLmWn_Stn2AG-4eaXcuSFFiRJtvE6y8nKmhgqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86a42811f.mp4?token=vF8RN5Yg6aN58Rr8b2pbDwwpj0hzT7yFmhd-2Motp2dtsDBd67EekIHxalVWsS_E0DcKLwLYuRchYtFlpLAtkRtdNkn7yFps2ZR-9nxk5BLE9z-UJBe_fjiyYuZKnt1Iyk6h2I9B3K2-6gnI9XUBRU-fZnlamGRTBRi9SVaHyyFNKf0-pQjG1Vs96Um1CyjHX6A8zLtb1fhpILOEBYlW6TCG2axLZOXy7keYw7IL7QCOEmgx7jKF8lc7yPfG6SA4BDDoydb3ZBxg8r0IwDpW7oFtHq4bTSK2gJasoF4Ctu9-HWK-BLmWn_Stn2AG-4eaXcuSFFiRJtvE6y8nKmhgqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان صبح به افق مصلای امام خمینی(ره)  @Farsna</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/446526" target="_blank">📅 03:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1Pw5Ea_aAlu8pzJrLcqYWo4Tl9eiHIb2_HScoX2Zlkq_PiYg2hObktwWi_fSyrlmH_G0pQrui5HXoxXuXej1ABj7p_OF6tVJ7NejOGVichZe6mERRISi4SCk2wxc7UQx4-zpVpq-LuoPLD2YENXf1WCw80o5bJpYRbuZg-vkGxzVsBdqZT2MwyZdfkP7aucvgMFdiVJr4JpO-JcCc6Ee1arupepVDcmlPDDeFLr-QtN_b00fHLmktfaI-wVMbU1Iegd-HNJvOjvlYZtV-usFBWsaNX2lwjvTf9Ts9QaykRBJVqNwoSj4jpRXp9pAz3fofPLhVuSg4FOsXWXq1Rz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
آماده‌سازی محل قرارگرفتن پیکر آقای شهید در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/446525" target="_blank">📅 03:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=WFYZBftXIe6K8W9-zQrp418MVdPVxNw0uUb1iuOpnbFHoko44iCxuBI5tassMXyPNMepUOCCnVq5EHTCI9brsfllw-CR08GcBVTLRnd62NkUumVMweolU8Lt31rOj6zRFXyQfoZvWeSMOSU1ugQ9YXDiF-jtr9A01CC7ee9wq8B-bx3d-uYddteentYN2lyZ-C0Kxyr4UijlgFRr2PKLgzbD3qvZ0TXRsFiWkGvbNRpOZF8wknEmD0n6jWk5WZMY21wgLm7FjlOI1FZWLFNyM4BLFUZP004eMMNHSzNyzBhePSjqE6HOxQwt6o0Iess2pHZ-Xsr_jZxjmHaGaAxYGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baa9424d9.mp4?token=WFYZBftXIe6K8W9-zQrp418MVdPVxNw0uUb1iuOpnbFHoko44iCxuBI5tassMXyPNMepUOCCnVq5EHTCI9brsfllw-CR08GcBVTLRnd62NkUumVMweolU8Lt31rOj6zRFXyQfoZvWeSMOSU1ugQ9YXDiF-jtr9A01CC7ee9wq8B-bx3d-uYddteentYN2lyZ-C0Kxyr4UijlgFRr2PKLgzbD3qvZ0TXRsFiWkGvbNRpOZF8wknEmD0n6jWk5WZMY21wgLm7FjlOI1FZWLFNyM4BLFUZP004eMMNHSzNyzBhePSjqE6HOxQwt6o0Iess2pHZ-Xsr_jZxjmHaGaAxYGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی نریمان پناهی در حیاط مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/446524" target="_blank">📅 03:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939fdd058e.mp4?token=POVcXhJZc18jBeIcpbx_g4M6PBIhcAXiuxuQ4CHDDG6wEO5S9BCatFlu-cYRcl_Plke8RuL8OQETblGKCVTgr7zShsrf6vt9HlYIvQecV9-opCUeyIi7y_x5K697dJ-Xs22qagd9HRbI-FRpW_DU9SUD7YPpTLJ2ZZo9vLaT_87p40MnI86qkuTK0Ed3zqR_Ghx0TiOnXflVGiZ5OqNPv1wRXAOHaSmy169UQGgOX1L0w7wI6kMyXWCo9j6yR12-o9w2TmwEPmOwKUKVBz0797jTvYF2EhW5CKbc1Adea1sd0IhuCTEEXgEMfN6RvEUVpXAS1B70FNBXv7KVU4WGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939fdd058e.mp4?token=POVcXhJZc18jBeIcpbx_g4M6PBIhcAXiuxuQ4CHDDG6wEO5S9BCatFlu-cYRcl_Plke8RuL8OQETblGKCVTgr7zShsrf6vt9HlYIvQecV9-opCUeyIi7y_x5K697dJ-Xs22qagd9HRbI-FRpW_DU9SUD7YPpTLJ2ZZo9vLaT_87p40MnI86qkuTK0Ed3zqR_Ghx0TiOnXflVGiZ5OqNPv1wRXAOHaSmy169UQGgOX1L0w7wI6kMyXWCo9j6yR12-o9w2TmwEPmOwKUKVBz0797jTvYF2EhW5CKbc1Adea1sd0IhuCTEEXgEMfN6RvEUVpXAS1B70FNBXv7KVU4WGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جایگاهی که اشک همه را در میاورد...
@Farsna</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/446523" target="_blank">📅 03:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de0fa71ef6.mp4?token=OBfWNfUvt4Lk4cvEk_LvqSKcT9G_Pl-Ts42y_BY9oHY5IaQFFA6bVOq2qW4oEIFbmfY3vfQyMwJG2HrKWHJXSlGKc5cIzCCT18IkN8jPgMDvIZFrXTvKiefAr-pJ5UwSnNT5oVyHnpCMcxHP7xjx_sdrikaSYsoTX8DREAdehvYBoebk1vwGgJsyhPXQh2Z3ldDLuk5qZVqWcDDWA5_UxWqwNWhQjUqWhk7P-IUOL-Z5fdIKgIz47hNKeo4OTV4YaOEPRBOnjWM1-fRp5leTDVgyFTP2zSxfJePd_iHgsptjFCwsSOl0TMC-tLOnW1ErL_xIC6xjidMSEPd3_clPLJw89L6LhpjEW--Wwc2FwmAZHiSQH4qDf22ItQ6NX_H1DnxUVUbar1Oy7GsecYvTPpxqPSbq9ITTFNnAqVdbivM5p3jjMofFw7TLLYi6WqN5kSEVPcmQ4K7RcgtzjQVYXa2wKUTtezJrhHotJJqMNSYYd9Ox1ULmeSiF6xvkrxZzj0G2OCn4S7q9DcFA0T0slytH8Ly_S3ZmUeSrxvlKjruj-eALWe6u9COiwwZQ6mQzW0t4GDpix_iFDHCqX8pn8KTLu6oj8ZdfWNkAFxIWlOZK4geJXAWVfpLSzOCgZ7XlsYv0VK3l7yEY-K1nKYyJaIamNc2OrYi4kMpM-yQExHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de0fa71ef6.mp4?token=OBfWNfUvt4Lk4cvEk_LvqSKcT9G_Pl-Ts42y_BY9oHY5IaQFFA6bVOq2qW4oEIFbmfY3vfQyMwJG2HrKWHJXSlGKc5cIzCCT18IkN8jPgMDvIZFrXTvKiefAr-pJ5UwSnNT5oVyHnpCMcxHP7xjx_sdrikaSYsoTX8DREAdehvYBoebk1vwGgJsyhPXQh2Z3ldDLuk5qZVqWcDDWA5_UxWqwNWhQjUqWhk7P-IUOL-Z5fdIKgIz47hNKeo4OTV4YaOEPRBOnjWM1-fRp5leTDVgyFTP2zSxfJePd_iHgsptjFCwsSOl0TMC-tLOnW1ErL_xIC6xjidMSEPd3_clPLJw89L6LhpjEW--Wwc2FwmAZHiSQH4qDf22ItQ6NX_H1DnxUVUbar1Oy7GsecYvTPpxqPSbq9ITTFNnAqVdbivM5p3jjMofFw7TLLYi6WqN5kSEVPcmQ4K7RcgtzjQVYXa2wKUTtezJrhHotJJqMNSYYd9Ox1ULmeSiF6xvkrxZzj0G2OCn4S7q9DcFA0T0slytH8Ly_S3ZmUeSrxvlKjruj-eALWe6u9COiwwZQ6mQzW0t4GDpix_iFDHCqX8pn8KTLu6oj8ZdfWNkAFxIWlOZK4geJXAWVfpLSzOCgZ7XlsYv0VK3l7yEY-K1nKYyJaIamNc2OrYi4kMpM-yQExHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اذان صبح به افق مصلای امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/446522" target="_blank">📅 03:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb0e215210.mp4?token=V8jwnSU0sdIF1DjtBeT1a6D41yJYKZo1wqnNEM1ZjGZ9FqyZHy4QkQBO_R_b-t3ahyyLEisCq72OaWNEALOUQX9ctJ1H2bXTJSjK1Kx6sOk5JY-9xnqiGbeoFC3sc_KGTRTjahxCg-j4PfKlCXf4eD93vEYmo1aeo7DJ2OgM5ZaOx4_MZCyAJNktM0YGix1HtheBXCoag2ukQygR70kW_zLicnX8llT1Lp5eJATNlZulw3cgMRCLvtV20eeHP5uFfqGJpquW0bWSWa13Gx86OypYl0dmF7b2z4s9iKb8BM79YFzuLcShMDiXEvHDnMRV08goKHWDRZ8M91rneC0R6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb0e215210.mp4?token=V8jwnSU0sdIF1DjtBeT1a6D41yJYKZo1wqnNEM1ZjGZ9FqyZHy4QkQBO_R_b-t3ahyyLEisCq72OaWNEALOUQX9ctJ1H2bXTJSjK1Kx6sOk5JY-9xnqiGbeoFC3sc_KGTRTjahxCg-j4PfKlCXf4eD93vEYmo1aeo7DJ2OgM5ZaOx4_MZCyAJNktM0YGix1HtheBXCoag2ukQygR70kW_zLicnX8llT1Lp5eJATNlZulw3cgMRCLvtV20eeHP5uFfqGJpquW0bWSWa13Gx86OypYl0dmF7b2z4s9iKb8BM79YFzuLcShMDiXEvHDnMRV08goKHWDRZ8M91rneC0R6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین ساعات انتظار این شکلی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/446521" target="_blank">📅 03:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
«عشق دل‌افروز» پرواز همای، برای رهبر شهید
🔹
نماهنگ «عشق دل‌افروز» ساعاتی مانده به آغاز برگزاری مراسم وداع با رهبر شهید ایران، با صدای پرواز همای و شعری از قائد شهید امت منتشر شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/446519" target="_blank">📅 03:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bd38c9b2.mp4?token=dTU3jO_38SZBY5TIgdI5hoUGAtxMkAAML0LxIC0BbTm4jkuzzcLns1tNbncfUsyA9XycW_clWMDjQpo-h-CplkzjhkHhjjh9eWx7NgXrpTIekj2BLga6BavIWMSuTLV-YlEWRH5zn7wC0fJkQ5-U63BOjsXRb2R-kEvIBfCrTKAArXO2YjYAA4psBf1ou-CtwSMungSVI7KQVTIsFsrhPYP6tVD99KJ7SGYgRAdhhZcRxjZJUJUzm-KTc67zAbo7NJmfKhDuwCZ9to4KaFOWP4glOmlOCWMf0M1-DzU7sZq5OTnYLgGn9lbf0iVk9lVWnOVneT2bLAfF_vPdlBz2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bd38c9b2.mp4?token=dTU3jO_38SZBY5TIgdI5hoUGAtxMkAAML0LxIC0BbTm4jkuzzcLns1tNbncfUsyA9XycW_clWMDjQpo-h-CplkzjhkHhjjh9eWx7NgXrpTIekj2BLga6BavIWMSuTLV-YlEWRH5zn7wC0fJkQ5-U63BOjsXRb2R-kEvIBfCrTKAArXO2YjYAA4psBf1ou-CtwSMungSVI7KQVTIsFsrhPYP6tVD99KJ7SGYgRAdhhZcRxjZJUJUzm-KTc67zAbo7NJmfKhDuwCZ9to4KaFOWP4glOmlOCWMf0M1-DzU7sZq5OTnYLgGn9lbf0iVk9lVWnOVneT2bLAfF_vPdlBz2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اندک اندک جمع مستان می‌رسد...
@Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/446518" target="_blank">📅 02:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ecc44ada.mp4?token=In8bc5u96037rF-wC-In98OAYFUx8D_YfkCUVomP1d7zBdq_oScX6SVC25JyHqH9rD29140psJsCZQph_wfely3zoaXDIgXwmIEHOzbXGCzV9E-Mv1Rne933kNf59jeh7mjeU8z-leBvE6W-wke3bQfsj6wEhWbMGN_pnrWANwalBfdbWJsAVURUto6sJurzO5qqBZ2EZdkYQDwbszSr_Ouywtv68QPjF4j4srFPJwiIphJkf3NmxtJynLZR_bwMIRxgCGgFHBykzRoeIHIHPNacF5a678vMdTjmHADpmeKx3KBNpZaDNmHisFmrEObmrAJ46gfbFZb5BROqQiQeKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ecc44ada.mp4?token=In8bc5u96037rF-wC-In98OAYFUx8D_YfkCUVomP1d7zBdq_oScX6SVC25JyHqH9rD29140psJsCZQph_wfely3zoaXDIgXwmIEHOzbXGCzV9E-Mv1Rne933kNf59jeh7mjeU8z-leBvE6W-wke3bQfsj6wEhWbMGN_pnrWANwalBfdbWJsAVURUto6sJurzO5qqBZ2EZdkYQDwbszSr_Ouywtv68QPjF4j4srFPJwiIphJkf3NmxtJynLZR_bwMIRxgCGgFHBykzRoeIHIHPNacF5a678vMdTjmHADpmeKx3KBNpZaDNmHisFmrEObmrAJ46gfbFZb5BROqQiQeKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چشم‌انتظاری مردم پشت درهای مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/446517" target="_blank">📅 02:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446516">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae50a122db.mp4?token=VSbfuB_0Nwfl_4WT3LU-n96daIWxmQJ2numSpCPk5N4whd5o8GfAnVOmGT1cYkTRld_OuCXKQiltV2WnausLRRTGyY_EsnOIrRxawvIEI6uSafcqomn6zm1-4sASAQK95GUf58kMWvYNYv3ReAFGcNG8brzZXRPtNHbfAaDqMOl4xOKAS9fongEgVohESNESMrh786albUbTuXYX01-0e8v_wh6TyR4H5JcsdyvEzXVi3hM9SrqezDB7LZC8nWAvw8gdeC5bjgauoJAxGbnotSTx63JTLffCdOpn6mvYZjZedmD_W2w7LTOcEFJqwWKd04AitBSFyE71oneKhOGxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae50a122db.mp4?token=VSbfuB_0Nwfl_4WT3LU-n96daIWxmQJ2numSpCPk5N4whd5o8GfAnVOmGT1cYkTRld_OuCXKQiltV2WnausLRRTGyY_EsnOIrRxawvIEI6uSafcqomn6zm1-4sASAQK95GUf58kMWvYNYv3ReAFGcNG8brzZXRPtNHbfAaDqMOl4xOKAS9fongEgVohESNESMrh786albUbTuXYX01-0e8v_wh6TyR4H5JcsdyvEzXVi3hM9SrqezDB7LZC8nWAvw8gdeC5bjgauoJAxGbnotSTx63JTLffCdOpn6mvYZjZedmD_W2w7LTOcEFJqwWKd04AitBSFyE71oneKhOGxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی عبدالرضا هلالی درکنار پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/446516" target="_blank">📅 02:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446515">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ed90b67f.mp4?token=WH1q2woTP_ypdy2qz_8uQP_ALce8xqm9JHUdwIJZ5ndBRnhEldu8jMZDVyMzGVugjZx4gVjcSTvfKyznG472GeoOchz0OgCFZan0rCyXoAKbZt9VOC4Tp5wTc3aXXznEXwC4dxdW8aNWpFHkuM3G-Yqq95bA8Yu65qxviBS2zqlG0x-DVQ1pe7w2TmrAnrmUGgWW1y-20S7vnt-CSaDTNlPve5bosJ9tzBG7Y-abJBMfKErw9FHafVpf88ph-fBO8OsiNEJ-aSAA6NepVxdlfMQy_Ae-OmqCiHu8g3V7RDZHwuIbx9e0dLGcxOKx_Rrg4IwuB5wypc_XBfdtKWWmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ed90b67f.mp4?token=WH1q2woTP_ypdy2qz_8uQP_ALce8xqm9JHUdwIJZ5ndBRnhEldu8jMZDVyMzGVugjZx4gVjcSTvfKyznG472GeoOchz0OgCFZan0rCyXoAKbZt9VOC4Tp5wTc3aXXznEXwC4dxdW8aNWpFHkuM3G-Yqq95bA8Yu65qxviBS2zqlG0x-DVQ1pe7w2TmrAnrmUGgWW1y-20S7vnt-CSaDTNlPve5bosJ9tzBG7Y-abJBMfKErw9FHafVpf88ph-fBO8OsiNEJ-aSAA6NepVxdlfMQy_Ae-OmqCiHu8g3V7RDZHwuIbx9e0dLGcxOKx_Rrg4IwuB5wypc_XBfdtKWWmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بی‌تاب آخرین دیدار
◾️
بغض و حسرت مردم در مصلای تهران، ساعاتی پیش از آغاز آیین وداع با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/446515" target="_blank">📅 02:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446514">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
۱۴۰۰ خودرو‌ی آتش‌نشانی در خدمت زوار امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/446514" target="_blank">📅 02:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446513">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
ادامۀ حملات اسرائیل به غزه
🔹
منابع خبری از حملات هوایی و توپخانه‌ای ارتش رژیم صهیونیستی به مناطقی در شرق و جنوب غزه خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/446513" target="_blank">📅 02:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446512">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f977b04afe.mp4?token=WyPppCtEhwANaV7rcCLs5WSdZ94wYrNvFz2aoBlojWkkhJGRu1ZsaGnVNSY_2aCzwyFl1UR4OuHSM9bKA3y1UAUh0kD5SwKmrlBK3oVIlwNjndmYF5vHoSt41BNxfOzLg34afwS1BqnjSnPTBAcIDPU6v8fpOWCzQZJMjwXwtIvmA28LohMku4xhEBtKOjXYEK-4LT93S2BwsbRZIw-iAHUbyXrLjPgPWnzu1lAbSN8floG6QdX4jzsJOH84Bi-kTzdgaYMr7X2QB5daRRTNgnIFSdJua73Hf_4PJ5y7bw-RBdKNkZWzweTYYLL5UwgV0qyFku2uceCHUrpl_Y5_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f977b04afe.mp4?token=WyPppCtEhwANaV7rcCLs5WSdZ94wYrNvFz2aoBlojWkkhJGRu1ZsaGnVNSY_2aCzwyFl1UR4OuHSM9bKA3y1UAUh0kD5SwKmrlBK3oVIlwNjndmYF5vHoSt41BNxfOzLg34afwS1BqnjSnPTBAcIDPU6v8fpOWCzQZJMjwXwtIvmA28LohMku4xhEBtKOjXYEK-4LT93S2BwsbRZIw-iAHUbyXrLjPgPWnzu1lAbSN8floG6QdX4jzsJOH84Bi-kTzdgaYMr7X2QB5daRRTNgnIFSdJua73Hf_4PJ5y7bw-RBdKNkZWzweTYYLL5UwgV0qyFku2uceCHUrpl_Y5_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
الا ای بزرگان، بزرگ جهان رفت
◾️
سران را بگو، سرور سروران رفت
🎥
قابی از پیکر مطهر رهبر شهید انقلاب در مصلای تهران، در مراسم ادای احترام نمایندگان کشورهای خارجی
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/446512" target="_blank">📅 02:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446509">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSQR7L7B5jjrHxYDdhxzqONWMZoVLBiCzO6wy0e5EZ3DyXGioFvCoNJRhAgLVi_TG_wRdsYH59bC1SJMqLIC5mjGcnDWE2c2t44BKBfGIda28Nb3WrWqU1DklUonr5POW8h5gwuA9YHkzhSneIsA_ON8K6LvitP0gzyC3SnIaljyhveg2uqIX21HcBLqTz_Wzz9u8JcOgob14x6L63U3NN58aSVVcQhhPGJIHxH8VPJdsBU_MHf2DVT_RgKbqRzmj9v5tfjNRNsQJbptio0DPauLPTq_FqYf-TU-TC4_NnYStkhcLjgqOPBGaYt2kcDmunWdwfBQ7RiYiKH6PSSgWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GB-EzK5qGSI4hRDCnu4XO8NuFd7tExuQ7sy7wbx489pOMGYWZGilHr6TAPSAxKtFn0Zn8Gw5osoE59JZMkMR779bwJEBkuaawOjrAn3NXVibggbyOx7-XXFDyS3lbCh3u-HUAwf_xl8FyHyuKJF7C-iZ055t-bsRTpgabLhn8QxB2khDWgORYm6veLue1Uk8GnBKyaWO4a_UqWpnbAqdY6OzSuwBHb1URC3hufxSpiC-OHCZ_hb1k5sDSuIfLY6Nr9MU21unwt4U3357M8xhL8FVD9hjkAZNF-QsTqQSJQ4HlU5VYRPWkXsAOpvjc1YguX-ralHnUedtCSWjdg3Q7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuYzbTXNTxZulWSR7ElPpE_tA1bubyjDrn1a9CAFAhd_YD4uY9Q63FgiUV7AhH1rsPczx_22I76ODJSyyZ2XW6nkwU8w8bQV43LZdpEo8pktnBxwDcaSG70_IGYw829jAcnjWnY1p_Po_bFBlpGHFTG3N4dWCsy30ZFqHvYWgx0aI95d8lBj5N9co7oRJKaEiqFHmBDNeMIDrParuOKsoC5lNxQZTfZ0PO3ux_KEKL9m5ay4zpaoznXYSOkjlhSKC2bLxnF0m556-1UVDpxi-50SHlL_cdYobv5j60h12XK_hlOn7oBP_WpZndzC0v2ti05BufVDXykIyiX2njx0PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زاگرس‌نشینان با سیاه‌چادر به بدرقۀ رهبر شهید آمدند
🔹
هنوز سیاه‌چادر برافراشته نشده، اما چکش‌ها بی‌وقفه بر میخ‌ها فرود می‌آیند و مردانی از دامنه‌های زاگرس، در گرمای تهران، مشغول ساختن سقفی هستند که قرار است مأمن عزاداران مراسم تشییع رهبر شهید باشد.
🔹
از بچه‌های مسجد و بسیج تا کسانی که روزگاری اینترنشنال‌بین بودند، امروز در یک صف ایستاده‌اند تا به گفته خودشان، وحدت و ولایت‌مداری مردم بختیاری و زاگرس‌نشین را به نمایش بگذارند.
🔗
روایت شنیدنی بختیاری‌ها و حضورشان در تهران برای بدرقۀ رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/446509" target="_blank">📅 02:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446508">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
سردار معروفی: دشمن نمی‌تواند محاسبه ملت ایران را تغییر دهد
🔹
ملت ایران با حضور در آیین‌های وداع، نماز و تشییع، هوشمندانه پای ولایت و ایران اسلامی خواهد ایستاد و به دنیا استمرار انقلاب اسلامی، استمرار ولایت، بیعت با ولایت و یکپارچگی ایران اسلامی را نشان خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/446508" target="_blank">📅 02:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446507">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b7271e4e.mp4?token=HMwdYsOwj_ZAfWAY8Rj535_w9ljHe5xWrGbuK4H9INm8FqmN_FHBirm_GYxQsalSxRyJydGbGqd8AbTEtS0m1UENfAraUrm7t4L9wTlmJMfgmACqrVmdCRAkEqY2-HTMNQDi1o-ij9sydLMhIdY0TAlvSM3h0QsvrRKZt1aaqxoJTHvW58uxGl3cNDgOzG84ao_lZyDSsK9v_fse5tO4wMEOPjMW8lE0NYcKrxg0uyFCJAQ0bh7SM23XG_1DyJlL-eidM3TGppbmZ5UTPb2RwkJvFOkkUmrx3YVYKqIKoBy2-2MRgCvWJ1aJrWuBV9RDbhrN4pQe0zvWSvbv2D1XhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b7271e4e.mp4?token=HMwdYsOwj_ZAfWAY8Rj535_w9ljHe5xWrGbuK4H9INm8FqmN_FHBirm_GYxQsalSxRyJydGbGqd8AbTEtS0m1UENfAraUrm7t4L9wTlmJMfgmACqrVmdCRAkEqY2-HTMNQDi1o-ij9sydLMhIdY0TAlvSM3h0QsvrRKZt1aaqxoJTHvW58uxGl3cNDgOzG84ao_lZyDSsK9v_fse5tO4wMEOPjMW8lE0NYcKrxg0uyFCJAQ0bh7SM23XG_1DyJlL-eidM3TGppbmZ5UTPb2RwkJvFOkkUmrx3YVYKqIKoBy2-2MRgCvWJ1aJrWuBV9RDbhrN4pQe0zvWSvbv2D1XhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلای تهران، ساعاتی پیش از آغاز آیین وداع با قائد امت  @Farsna</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/446507" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700fb5cced.mp4?token=Ya4d8Z-etqU0_QqAlxsC0mh0gOeP2bwuTtXTKbbcaorClVVNHsbe8VwdG3lvHgjebggLOtxSgX3wh-HtZuJSDHgtUkMa63Tp2IGO3n9AsxwXLa7d2gxPZGt9CkDh5tJCJ0CZCm9P8D-t6_koC5XuLSCVfqwvbyRFBRCwGM5fKEYZ14uJyAEE90zluaZiRf4G3aRTaZuAtDPKDEtEGWG3LVOLtNYCvVPmzTwSLcvMj4DtCtMbBpwgCMpI2xk_3wCb8NWtKsdytUr8Y6-QbzSX5mF71rJyZ48RuptTcFxsEILjqIpzaA0Htv6U-6YKNf5zzJlnVtZG2GKVIlRMYcGe0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700fb5cced.mp4?token=Ya4d8Z-etqU0_QqAlxsC0mh0gOeP2bwuTtXTKbbcaorClVVNHsbe8VwdG3lvHgjebggLOtxSgX3wh-HtZuJSDHgtUkMa63Tp2IGO3n9AsxwXLa7d2gxPZGt9CkDh5tJCJ0CZCm9P8D-t6_koC5XuLSCVfqwvbyRFBRCwGM5fKEYZ14uJyAEE90zluaZiRf4G3aRTaZuAtDPKDEtEGWG3LVOLtNYCvVPmzTwSLcvMj4DtCtMbBpwgCMpI2xk_3wCb8NWtKsdytUr8Y6-QbzSX5mF71rJyZ48RuptTcFxsEILjqIpzaA0Htv6U-6YKNf5zzJlnVtZG2GKVIlRMYcGe0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسی در دقیقۀ ۲۹ دروازۀ حریف را باز کرد
⚽️
آرژانتین ۱ - ۰ کیپ‌ورد
@Farsna</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farsna/446505" target="_blank">📅 02:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43fb37209.mp4?token=TzlRhDhYuCn26bRqmp0f_NKPicb3R_ifZSY8ySnFLmbuC9I0cNjx-JPwQ5g5crtBnEoQ5GGtEfUrbHD1xMPRk4IP-K8W3ykVTTYuqIty0LICh-A2ZAUcO1ovM9Mscz2i_6vGa-oMVk6FdLowR_oVOESwhGbY-Q86QrHUW9h1KjR14jgHA4fdPC3op4lAF9PkZSnmAHj0SwfTXR0ffDeNP2zD3UOalqSwdLlJqIfLZ3_PRFN_Z5UVOS1lvwgjbs8lZC8lKgg5B6D5Lfdi7VBSdx56gPE5jIJJpO8IwD4PNnTTeVwTpx3YovWWBPDVy7DSh_HdzaDSTkrAz2jYTHXcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43fb37209.mp4?token=TzlRhDhYuCn26bRqmp0f_NKPicb3R_ifZSY8ySnFLmbuC9I0cNjx-JPwQ5g5crtBnEoQ5GGtEfUrbHD1xMPRk4IP-K8W3ykVTTYuqIty0LICh-A2ZAUcO1ovM9Mscz2i_6vGa-oMVk6FdLowR_oVOESwhGbY-Q86QrHUW9h1KjR14jgHA4fdPC3op4lAF9PkZSnmAHj0SwfTXR0ffDeNP2zD3UOalqSwdLlJqIfLZ3_PRFN_Z5UVOS1lvwgjbs8lZC8lKgg5B6D5Lfdi7VBSdx56gPE5jIJJpO8IwD4PNnTTeVwTpx3YovWWBPDVy7DSh_HdzaDSTkrAz2jYTHXcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات محدودیت‌های ترافیکی در محدودۀ مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/446504" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cefab0f6.mp4?token=HOkCVuNY-f24ILz-V9p00mZhgHRpurWcSC4YJc7cHvu1Y9F2Xige6GCEViLBWtIrlHOsJysABLrjfrl4-GvvNVPWy9c3z92_dfWbTJ7S0-GQrE8kmQBA3Ct8EBdW4vRyeMfPtIhXL55tZzwU6T_RPuHrTq8-uqsuEcATcboRiMwHKxqImbaitHSrZUDfSyRWKMWbQxLufIGueXbGKkZO6NBhJCoRB-OGa_b-rExKZKICtR4T6jwSBFHzkCEctFIS-Lo890DjbxfInkExFFB2Vdj06MYzkn0cm5J9is4OOUInaHQHCaI301jOHNRquYDXMbBlxRzhKAsJT6xrAcA6cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cefab0f6.mp4?token=HOkCVuNY-f24ILz-V9p00mZhgHRpurWcSC4YJc7cHvu1Y9F2Xige6GCEViLBWtIrlHOsJysABLrjfrl4-GvvNVPWy9c3z92_dfWbTJ7S0-GQrE8kmQBA3Ct8EBdW4vRyeMfPtIhXL55tZzwU6T_RPuHrTq8-uqsuEcATcboRiMwHKxqImbaitHSrZUDfSyRWKMWbQxLufIGueXbGKkZO6NBhJCoRB-OGa_b-rExKZKICtR4T6jwSBFHzkCEctFIS-Lo890DjbxfInkExFFB2Vdj06MYzkn0cm5J9is4OOUInaHQHCaI301jOHNRquYDXMbBlxRzhKAsJT6xrAcA6cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم منتظر در خیابان، از بدرقۀ آقا می‌گویند؛ نمی‌توانم با آقا خداحافظی کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/446503" target="_blank">📅 01:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde79d832b.mp4?token=tlEWgkmE8zDl8T50Vw0-YZ1T36fgPEBehsYXuSGm2s6FO9CQtZm2HhoBdVIpBnZ8dLFPuRt1Guy-vmUeZvaOnioV3qn6QTgYMm1tOY_up_5_rAPxiPqcBXzMgmmjGNRgW3mfCGDg-sdpRRrgElrQDIL64YDccd3Q5GbSjA-lCqo3Kvl2SroJpxeFK9p9yN7XWETh6KSh9U4hcIbizrT0CeDMh5rjQgh2FsgJZXOD1zenS3hxW1gauwDNHrd-Q1Y1OvCm0TsJKqjyDuI2mtJm3hCwTkyJwPfF0cuBG_cQijVfupiry_IS3T1nuSOWukpzMi77IM7Fy0JT0I76oO1zNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde79d832b.mp4?token=tlEWgkmE8zDl8T50Vw0-YZ1T36fgPEBehsYXuSGm2s6FO9CQtZm2HhoBdVIpBnZ8dLFPuRt1Guy-vmUeZvaOnioV3qn6QTgYMm1tOY_up_5_rAPxiPqcBXzMgmmjGNRgW3mfCGDg-sdpRRrgElrQDIL64YDccd3Q5GbSjA-lCqo3Kvl2SroJpxeFK9p9yN7XWETh6KSh9U4hcIbizrT0CeDMh5rjQgh2FsgJZXOD1zenS3hxW1gauwDNHrd-Q1Y1OvCm0TsJKqjyDuI2mtJm3hCwTkyJwPfF0cuBG_cQijVfupiry_IS3T1nuSOWukpzMi77IM7Fy0JT0I76oO1zNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای نزدیک از جایگاه پیکر رهبر شهید در مصلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/446502" target="_blank">📅 01:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446501">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6b30cc11.mp4?token=HddEpSYPrfOp8j54crFFpD_XVPQoEpj_m5Mtptz8E5VhY2IugoO4gQ8varFi53PFB_wZAn1Two2zLcCIMbbIzUkoiQ6-uJ_7O8WInYWhpDrgd73zcoNrSMjTD9auSHklQjBn41jW6-1ViTZ6_2X5kfBqDjHHLF8mE_ICDwCsxN0stC8LUEuifYZbfuDA_AB6kIZYngLJfB1ELbyZpTlVoknXGIUiCmaIxwd1ERGEH8wcf7DAoEsZIR_HlI7FugECK7EUVXKBCigiJzL7aQRt26-dpPa07KJc9qBGjmZE5woNcIzM7ovCkK5keuFEk512fcjaQAMhgzr9NPqZcJx4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6b30cc11.mp4?token=HddEpSYPrfOp8j54crFFpD_XVPQoEpj_m5Mtptz8E5VhY2IugoO4gQ8varFi53PFB_wZAn1Two2zLcCIMbbIzUkoiQ6-uJ_7O8WInYWhpDrgd73zcoNrSMjTD9auSHklQjBn41jW6-1ViTZ6_2X5kfBqDjHHLF8mE_ICDwCsxN0stC8LUEuifYZbfuDA_AB6kIZYngLJfB1ELbyZpTlVoknXGIUiCmaIxwd1ERGEH8wcf7DAoEsZIR_HlI7FugECK7EUVXKBCigiJzL7aQRt26-dpPa07KJc9qBGjmZE5woNcIzM7ovCkK5keuFEk512fcjaQAMhgzr9NPqZcJx4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میهمانان خارجی حاضر در مراسم وداع، از رهبر شهید می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/446501" target="_blank">📅 01:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446500">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG4mAErDJNmpnPDtY_xOVIVVRjZk2HtgHuKucJoRnG1vafDmB61Wh1794iY9pgF12Pu60Cj2WQjoAuT4Z6z75F1QsCP39RDpCuM0-hwhw8Y8rHr_GDiJildPCBRUhcHQ-RjeDkaH-y0GoL28okqvtOnMllwNeXrwEMllN8XbAJJuVgts5vP5acXACsLtNCex9398P7HjaNVaUYJKCJP5h8aB2j41F-9Z3_KkdztYTBt0UvcYfeg_nOlqzklqRmQP3L5AkFG4nHMGWQP6r8PMj2jQgCu7o2An48_rDBP0JAHk1XsBAO9gmAiWlgtVDgIvv-TTLByetZo7A963TgTZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخت‌ترین شب زندگی حسین طاهری
🔹
«سخت‌تر از امشب توی زندگیم ندیدم!» همین جمله‌اش کافی بود تا بغض‌ چنبره زده بیخ گلویِ بیشتر آدم‌هایی که ساعت‌ها روی پا ایستاده بودند، دیگر طاقت نیاورد و بشکند.
🔹
«امشب وقتی وارد بیت شدم یک پرچم بزرگ دیدم که نوشته بود اتحاد مقدس؛ کلمه‌ای که آقای ما برای آن خیلی زحمت کشیدند و بعد از شهادت آقا، ما باید حواسمان به این اتحاد مقدس باشد. آقای ما فرمودند به مسئولان جمهوری اسلامی اعتماد کنید. اما از آنها مطالبهٔ مؤدبانه کنید که خطای محاسباتی برای آنها اتفاق نیفتد.»
🔗
صحبت های حسین طاهری از حال‌وهوای اولین شب وداع با رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/446500" target="_blank">📅 01:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f486aa29.mp4?token=ESxqDpGPg2P52aSUPTbACmp40ER-m97ENYovKHlFm_TaM_f00gjmRBiPHttVQGdwh3mQkOQf-6iy4cIJn0to_xMiO_jJ8pyU0k-OL45emBDm7-2xyFQ3J0NWp1dS50z2qUcBVtXx5wAkxZfexCDwLAxp26R8_TgEZsAsB7Y46IC3q52W39y6IuHA0JRvYQ26Q5SrxZSp-4EeiltboqRm02shYL3lZVe5-YwLCWXU5hviGHDiTNDLpXN7DwAXRl2bYXu_AljkiO5Gu8SFHxkx8UPCZ2ozyKDO-gq_VTBYqjAEL4RrSO3V1qaMn_gPyXrqvwQz8oGPPy1uEN3TCwoeJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f486aa29.mp4?token=ESxqDpGPg2P52aSUPTbACmp40ER-m97ENYovKHlFm_TaM_f00gjmRBiPHttVQGdwh3mQkOQf-6iy4cIJn0to_xMiO_jJ8pyU0k-OL45emBDm7-2xyFQ3J0NWp1dS50z2qUcBVtXx5wAkxZfexCDwLAxp26R8_TgEZsAsB7Y46IC3q52W39y6IuHA0JRvYQ26Q5SrxZSp-4EeiltboqRm02shYL3lZVe5-YwLCWXU5hviGHDiTNDLpXN7DwAXRl2bYXu_AljkiO5Gu8SFHxkx8UPCZ2ozyKDO-gq_VTBYqjAEL4RrSO3V1qaMn_gPyXrqvwQz8oGPPy1uEN3TCwoeJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مصلای تهران، ساعاتی پیش از آغاز آیین وداع با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/446499" target="_blank">📅 01:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446498">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a87dc475.mp4?token=KdxPwsYOpBHzB92cL6kTpyAkMmx3hL7EqXIMKLZJCLPpD0AKe3at_RWno9MGI0ljfWyT1r7A97ZmMO_HC5QmfAchbaaW65c9Fdhn3qjSM3DJhT9eg3ZHVMHrM1-SBkU0phGprlgylapyiBFXV00MAWQ9qftCtRCgbqqpbpkgAXQDz_Szg6RLntGDcBApNOPLbQyzaWqWKZDX-QYs6oWEKw6RGfG9MwoUx0uavNl4WFFIYHfYQr5o6pwW-zsL2Ef4tG8ryyX-bFxjISIOADXwJAi-x4G09C62cqCu7-zZ3raG5hd937ERQHQAp6O98cJQaEtE61qhckF4LM8LKgfz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a87dc475.mp4?token=KdxPwsYOpBHzB92cL6kTpyAkMmx3hL7EqXIMKLZJCLPpD0AKe3at_RWno9MGI0ljfWyT1r7A97ZmMO_HC5QmfAchbaaW65c9Fdhn3qjSM3DJhT9eg3ZHVMHrM1-SBkU0phGprlgylapyiBFXV00MAWQ9qftCtRCgbqqpbpkgAXQDz_Szg6RLntGDcBApNOPLbQyzaWqWKZDX-QYs6oWEKw6RGfG9MwoUx0uavNl4WFFIYHfYQr5o6pwW-zsL2Ef4tG8ryyX-bFxjISIOADXwJAi-x4G09C62cqCu7-zZ3raG5hd937ERQHQAp6O98cJQaEtE61qhckF4LM8LKgfz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه‌چیز دربارۀ مراسم و محل وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/446498" target="_blank">📅 01:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446497">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495961d30c.mp4?token=RC16BRedv1VBRU0LqJQ5fP7KWPNf6pFlisRi3sIUjUf3dn-nQVgb1AEWVjdAWZ5vqLpc5nq9pf8z4am4TvupeBKfyKEk-17lRjx-ZUap81c4Xm_E6GqGvBFIV8sTSu0fQJqir7YjJrKKEC_88feij551qWjOwOVTb7SxeWh5Jur_R9QKeNLjsIpieSAFhhpiaVZ72m3Dt6VpkXAM6iJ1sl3kESnTgcMHszLEKVqiHFL5xFDRyek00lBRrEtxXs5bfg6JlwkybunLk4ShTXDjUeLHjQFEstowDcFOrDA8FzTt--PcvhLpDDr3iX60XzYBG3I_4OhsDh5fyJjU2u6-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495961d30c.mp4?token=RC16BRedv1VBRU0LqJQ5fP7KWPNf6pFlisRi3sIUjUf3dn-nQVgb1AEWVjdAWZ5vqLpc5nq9pf8z4am4TvupeBKfyKEk-17lRjx-ZUap81c4Xm_E6GqGvBFIV8sTSu0fQJqir7YjJrKKEC_88feij551qWjOwOVTb7SxeWh5Jur_R9QKeNLjsIpieSAFhhpiaVZ72m3Dt6VpkXAM6iJ1sl3kESnTgcMHszLEKVqiHFL5xFDRyek00lBRrEtxXs5bfg6JlwkybunLk4ShTXDjUeLHjQFEstowDcFOrDA8FzTt--PcvhLpDDr3iX60XzYBG3I_4OhsDh5fyJjU2u6-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سنج و دمام‌زنی زائران وداع با آقای شهید ایران، در خیابان‌های اطراف مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/446497" target="_blank">📅 01:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌  یک استان دیگر عراق هم برای تشییع رهبر انقلاب تعطیل شد
🔹
استاندار استان واسط عراق نیز برای حضور عزادارن در تشییع رهبر شهید انقلاب، چهارشنبه آینده را تعطیل اعلام کرد.
🔸
کوت و العزیزیه مهم‌ترین شهرهای استان واسط در نزدیکی نجف اشرف قرار دارند. @Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/446496" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiamunR03TZJ1Tb9L2dpYRccFhibuLrYHVFAfkM_8pkyeO7YCgJby2XPqZdikJmLKcBf77KKQ2vsm-oUXRi4sSdcSVo3PHTAucfzb_LRdc-jhsYOQuRof0GMUe887wpazJnl0tpPtyw0-mZWBTm4sN0M2FtzSZOhPe8WqvOGNJRFWFqFs5W_JlN1_584_BnOdIn1Spa1h4G6RMskOMmyjgLQ94Dl1zh_N710Xkb7WwfwEU8bxzEdi95njWM2Jy6QHoB4kfvUqH3onykGTaHxYcCSq1m8azegmq87r9VdMh5wFgWu2ptDtuTvuyFGrUtfuCo69p_w9of13Ys7oXbbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجباء عراق: ارزش شرکت در مراسم تشییع رهبر شهید، کمتر از مبارزه با صهیونیست‌ها نیست
🔹
دبیرکل نجباء: میلیون‌ها شرکت‌کننده، خاری در چشم دشمن ظالم خواهد بود و فریاد مرگ‌بر آمریکا و مرگ‌بر اسرائیل تیرهایی هستند که توطئه‌ها، دروغ‌ها و جنایات آن‌ها را نشانه می‌گیرند؛ پس کوتاهی نکنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/446495" target="_blank">📅 01:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMVavkjyoTSiEhNdudPPuU9JknkuX3i4tVX_jK4eTtKcZvZPGqBc6RQdt6rWmhY95FVIckVMWp82rPztjtgNhcaGF5p6wf54twidmbrAiv7ZGjfr3zv6XGZelPvAnNHb9l6akbWU9gSpNutR_bpNJo_NUFaRC1ROibrbOG0-QfLDUmq7mdRisRY-V9cLW-dGDcgLbZRqa8A8VXWi4CczebrNmzEDuNLRK8uoTT6fHBcZRx2tjam9eK2wVM4Ey9jOEXF6ahkTVcmNk73-cFKdnQrToa4eCgl3vLqAsfns13rRMOdqORFuVRlxPMMN6EOzzreag_zBGI9pHUeyug9MsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی مصر: این برد را به مردم مصر و فلسطین تقدیم می‌کنم
.
@Sportfars</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/446494" target="_blank">📅 01:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lopExvGw7Wzii-Sk0ipaAeXh2ZzO1dnpXi33U7AKWMHk_2yIttBe42KgCNxYHd5F0pYvhxhSBzKa3HZzmAyaVSo7HrkhRvBI_6L9xGZ268auklPtYGhlM1AXx1YXW50GIGJy_A39lUEFFFuryZ8sumA8dsQVP7EFvNqvN4e-b4eAFrLb4zLygcDykztBXk04v-jp-3a70p3-HLW46708B1NA5eJ1OvLQKdolb_XV9xkcub3pJynVvKvF2ELDPc2MTsP-r0CPwYtNcfJqA-N3tM5sHylCpwTKof04y0yLFQITIpQu2nHOMz-nG--hDrfzAjHLckIVICLC0XV9abdUaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ مسدودی خیابان‌های منتهی به مصلای تهران   @Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/446493" target="_blank">📅 00:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cn7FOv1klRj7fSfBfC5ReYLQpQnlJab2MB5qOcfrVxNInXgLSKqJu-j7cwkWQRss7i7EQ5-pQhZisTMxvFp8dBcgd0tYRaRRmOrifGfCiG_9WWM45BsQjTzGh00XfqNg1NlpxBklKIdCQ_Pf7hnNqx1EVQWUrLkRQAsxOGcjj3G-MtQ8aX1AvpA5KlEvLXmVDyK-2Ai5WI7V45o3JmyG8u7M7VZHkV-6O6E6VRjkdC8OB0L1Rck6BY69tFFwJTgMEsMAOG4fc92E-D5lilq1SCP-8kO2PXP79KYH05ieBtwyACBmy_m910q7HjTxRcSPw2cyQeD-Yoa2imiLWhS_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وداعی به وسعت کل عراق
🔹
طرح حشدالشعبی جهت فراخوان مردم عراق برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/446492" target="_blank">📅 00:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU8uiE_qXWbW0f_FVoDP1gO8CBIy6z0KpPO40E63asbm0fjbf_ZqKzO-q9267eBs2I2VKMSkQrV7Jg3MMFX6K2CB52TMJizQIufx_0vaKzlQWu3pTS8tTBv5srO4KtLy03gSfD3gyQ36BmSnQUNNQv9BVdHL0CvX_riPG8VFYzJtyH55Z4NQjcnjHAtawL1MdWKFDEFDQc0OmJoc-lx3zObEG2WTxWAjOe0nd6De_unupZNV3_94PLlBYvEAT0T6B_YMskz8tSc5TOJh8KvtWLQu0RjqfUayIWSvJH3g6BG7_lFwfZ5CgZbs3YeyK0Of-EJI-G77EyxfhrrrfyGGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نقشۀ مسدودی خیابان‌های منتهی به مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/446491" target="_blank">📅 00:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEvf_mpxujgYRVVmcYl1naamgSMK-fRdlTKQAakqpmnDFF1qABac37aISX3LxC7gTol6TEaTVKPcD9DVFLUNiqA1x4awTHfBVtbfAbTeBgocmr_JTGvqhX3vnjKXfjsy9vf0O-loSSOxThmoHEAXapfastEk0tuMh3_yR7pq3iYU6kiIEkwEdWu0FsE412ifBjqPxUBdlIPXL7IOzidWFJOR3aaa1Wqrg5qJ8ZUvSapeEXrw8DRi6rt7XHkxfZE5iSMAznGu0s3VD4CylEJqDX40MXjdxzSOguUh48fswJI91w2RbwfHQEsy4M9HMsjKcNyCx0W9M6WOlUwCU2ZEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازدید سردار وحیدی از بیمارستان موقت مصلی تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/446490" target="_blank">📅 00:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d77ec6308.mp4?token=LyRA7qtOEwlKBGqHxgroxp_1Q5_ToOtaptGlbpw3ODovMm4cNK-_8RxnZSxy1164kM0x-IOX03f9n6CnF31jBQgBoLLc-otPjrS0MUrj96KDYkkIunG86vvCexr8q-fhc0VmKHtZVqRRRSyMG61D9smkx8rhHLKwajmBnJ9E9PKnpOOgxWv7IT77wfxNi6-EXrUECs0NaSrRdyjfLuyXJK2yyOlopIaJN22xY-Bm_o4IWcYATEfspnIr5Pi-ZKGtZ4f_sRdlUNTkHqRSbRmYdBPzPrrAnUDt7bpjEc2qfSCyaL--U2bbCJB4mX9xjvx8-2m8Yv7DdQQ5ofkhgqLsU2Uy5TNaxCtrZzEXuzj0XVfzMZ9kN9RRQwp8iPfYr8jSMFEPmkkFwVaK5RHrEsazwFLrevA31nLdM-71rocr5ovy0yGEEWC740s7MvtnOI9qvIoKgijt87wOzNMm4L-UpUcdVLvtyD7nlSFSj5IjlFWS53xihCE3iNgFxMVWk8WHxcyC5eHCeV2lbDc9JmuMvF7pWdgdoSr4BZOjucd6yp58QppHfQX6WG_rfVHjX-9yYco67sb-aXOVP04J0Bhty5TFkl_W9ybDhwGB_gApdmUP3_Op55P7onpyhZzImQxHvb2hYyvfQ6OcKuKGwWzo0q8uYK5s3MUB0QFUo5ms-Ac" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d77ec6308.mp4?token=LyRA7qtOEwlKBGqHxgroxp_1Q5_ToOtaptGlbpw3ODovMm4cNK-_8RxnZSxy1164kM0x-IOX03f9n6CnF31jBQgBoLLc-otPjrS0MUrj96KDYkkIunG86vvCexr8q-fhc0VmKHtZVqRRRSyMG61D9smkx8rhHLKwajmBnJ9E9PKnpOOgxWv7IT77wfxNi6-EXrUECs0NaSrRdyjfLuyXJK2yyOlopIaJN22xY-Bm_o4IWcYATEfspnIr5Pi-ZKGtZ4f_sRdlUNTkHqRSbRmYdBPzPrrAnUDt7bpjEc2qfSCyaL--U2bbCJB4mX9xjvx8-2m8Yv7DdQQ5ofkhgqLsU2Uy5TNaxCtrZzEXuzj0XVfzMZ9kN9RRQwp8iPfYr8jSMFEPmkkFwVaK5RHrEsazwFLrevA31nLdM-71rocr5ovy0yGEEWC740s7MvtnOI9qvIoKgijt87wOzNMm4L-UpUcdVLvtyD7nlSFSj5IjlFWS53xihCE3iNgFxMVWk8WHxcyC5eHCeV2lbDc9JmuMvF7pWdgdoSr4BZOjucd6yp58QppHfQX6WG_rfVHjX-9yYco67sb-aXOVP04J0Bhty5TFkl_W9ybDhwGB_gApdmUP3_Op55P7onpyhZzImQxHvb2hYyvfQ6OcKuKGwWzo0q8uYK5s3MUB0QFUo5ms-Ac" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظ آقای عزیز ایران
...
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/446489" target="_blank">📅 00:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRl2vFZ0_E55tQjF7fRTRflKTuayOiRcHKygmXuyqJ2jdyhsHfFIy0EUaTJA58ZoA8QfXDtlD313Aj1bzHEZ1zzz3g646dhhdSzdd5Un5aaTRT23rro9qvUQqRcOVV3HTZSZguZ_ufmnA_yLDEeIPvTvCrwZYSwKOdGy_sN4jI0jIb0D67gYktT3DQfwv4UFC9qQWe1ZhjlMMpqPSQgGV1ZjVBbirEaFzM-9IGnVrVpAuE5Kn12TLL5KsQzchKyj3fAP_Y7-CtoNpnjDxx8e2h4nRfbgLqTUsta-Ovx9F1e2DYEg2u266KCrVSR108Gm350NAPbnfaU3Ny7v2I8Ufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIokOk5Z_t9ofjgrqqIJbOCiYvRrpIQewhAUJs7Mexx9owPbpVdn7AeaNrLXW6Dl9KTrtqviPcQtbowSSnCTbJjAMTR47sGqW7pRywIDLpe1tdZnrF23_KNcSirrkBuX-8wdFzBn6_lIlWxiocP1h0J633a0txLKFIIJu6_OYYXxGrZhic0i6nj8GdRtx3_7mPukB1EdU_SI6Vd7AXP8plXmnZ_AtklC0VGLwTC0cjKoh8-tfy5ZuyVb4JTj89h6R0naipmTTQG4xAeA7i3SnT7zgjQSlGySGJXi-fJ42eHhP3Xa76x_kEX5eixBALJBzyK-b-diczBwJcsTIE-G-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuowRq080G-HkIGU-bu8O_Wkb6ec0Jx7t4mHwbIBIpJ4vcNu5t3VJZvyUTPK-3SAR8g04uCO16R1vcmVCiJaJNBn2Mw_eRA5IPLkN1am7iKYDf8dgIbeQAMLUZq67xELO1YPKKHmjfDhtSazdE1RE7q4R7OkOflgyRQzZBs8zUTmI4-qf7azRkWdpqvjEj-NZ-8b25AoVBH-SK2TX_-L6R-lClPNNaVhATwm64kJnYZMptWOQ7NLuGmNQstaufU3qqyIQgDpWxCIciJCN6uU_GSXUy3dP2P6p4aR3rgcBo_Sm72a1vraZmWT7y2JnHPPRh8wgIjl02lrYwGAKWiLFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۱۳ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/446486" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzS7wLlq0KUQGjm90eDAVIlaxTlqj0PG571ObKHjf4bjZ4lVn8YkB2BRKFO86YatL85c-rxFMt3_FYQUM4DNvgEraVc-aIZmCXmdCPkErltrE4H8oE7lJ2sXtnniCoAzm0dshTOy7-bPFn1L9kiEsJkKSVsX79hvTtUlLZ-g5xbZM6I4HoioSQu-RXMvwAXFI0LiBYRxMYl4DtsNszNFi0nAGc5j_vyy2UhYYWaJ7GvbAOWWkJ_TgiL4ALuNf7JCeTiWyPpjRS4rpC8LrUQgkFpg1XwAISq1CItwJir5FHWnbBm7lJ_quC2S7djOJiW1s9yC2Pul9TOJtgb340UR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSUGxGhF4XPnPUtrJfn_magjruNPRmCECnOnlfML9gXGAYLRM7KikRhyNlx40KZWSTPKmSyuJK9d-64g_hh7m39MoPYsIZoYCG7Lxi_IWgRXhcxy8ieZqksFGVtMSUch1vAHEJUeiYhkG5ovvZ9IMSxetjGthKMBJ0mvuSTO2lScLo1d_fV8u8VNJlobnQ_dasdA7xbSzctYn_aGYmOaxR2hlD90voIftx89mcY8By3eMa3Gyj837pZmYKJ_aVtM99_ne3AS4qwvofKsOr4zQqESc5cXvzNiubUp4dKxY1ZgAt5-0dO7iqdlAIyruGWB4cv2_ACZPSx-vXzaWsGfFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvAxuwmtGPs9XzCmxL05ur6AN3YiKfpBQiabzYyLMD-QPlLZ-BhMI2_esf9lJdsiowU2p_Gihd-fO5oTgB4JICQMAj5hPxc2Xtau1767ZpUEfOckPA8P_O1_l-4QWI0aqYbGE9ZoGhoxK6Ee13VPYWtc6cXEgjzv_cCwoGaP5plyFsa84KZoPVlKvrMbmTWzjR14_bvYQpJAaWviV_xeomKD80AHzK8GEivX0bicw-sN5WNdm_sx2kVAVMp-CVoYcyI6iUCfmiu9XL_kq8OPw2mOTsXXqbm-ITayWKpVGavGLJbyHENAaP7me_RjC1Xb2yQ1-JsEkYyWJZDwkEm5Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTA4xGB8eA-5hHB0sm--x4SFjVNsbIC-TQnMuUDvuFnNecHUMJyDHPXSaG3XdEmEMZveuEsbzGUzhl_f3YfxkIhw0juJH68Xis1LJ_CKrjXLOQ__p6Pehkvtz8LUyxab971-BuxW3GC261Q5_LcXsl2Fnueat8WcGdZsQZ9ehvOXa1w7BHW4j0TXod33IGnVw9ye3lgjowsDKntCO93XjBHm8u91UAOKJyUH2KcRZSSUJeDnuuB8paaYZNqbNoPuFg-oHxXCF_qju6QALpqSEAq5zVoAnz6zp343dZM2IWWJp50oxdqWn8mlXX7a5zfcAUQQQq3yze9C5s3p6jiXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_-LhLSRq0FSO-hBMtFH7BFPgw6dog-9ybR1yTUCLiQHv_OirlQtxhBgPLMD5b0tLbaOGvwhvOMWo3ZEOpXtLN2oDWPdk9gK3d3TAQrfjRlXkZnJBU9fGTFRg1eQNCj9x6D66yoD7CBhfsCZP5UaY-2FqbFB1IjPKb2KTy1iVw5q5kTnPU8nlY2kIYly57VyfuEO87LxAknFd6BSFFhPxdmojVGyPC72O0XkteIv8Se6hpAKV9HTONhjz7Xu2_DqkZplFYhRivjplHYjJ3dblcXmqCBsrjgSCTiqV_JIwxRxP4DV6LRIYIFpHys8CeCUcJEaRqOCNZ_cVhwl_NhgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWj34PPYITlMriNxIU-m1UoWs6_F21txdv13cr8j9abOAnaoDiG43YJI-KGAkowEwPB-4cURKfz6PINooRg84Bi1vmfXyrPpLO4c_X8NQO6EKQCWrN5wt-OEW3FWCM4BTyzcm0FqNrYESq_BcdPjudnaypQWLRcv-R46U_AFCsyuVPPdBtg3ItencHNLjGPzQlIRyfxqNir2jI5bj_6SK_cYVyUbH7E4favU3f1Sh0DMd3y9nZ9vscfgzBg0LY5LePrEkik4ejG-Y0dJThnJrIh5MLmghFjBnR4EGmC1xZU_EbOPIDIXOIDUDllvEEbDsA1702aZ8QK3jg4Uoy97pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ll48fmFfo6E11uFkB4Zng5gD6xOGPN_VCdWZML_lyOWdMMNDtXt7f8DSVtZQGY6CJw7w6xK6_ZyU5l9YymnweWzE3NZTuzmbfF5NLC4Y_-WQW_RkNocJ73YAA1KfkJkx3l-RvNQLAI1_heWMszx2P1w1sfMTemFgqVPC4F55wcRgajCT2YN5btxwAIr5RXpBlvNIyw4n8o-spbbr1lMA-PtQ3D2Vxz7dXG-mO98dMNTDhQoDinmqHgzHmrcRloZsOCp6gPVjQ4hegzMLx7pyiT2akHoDKTXX1tCFB2QyBz3oUgznlgP8WzdZxe8_uLrJrzrUhaySyWvNr4pMKeBNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iapDBioGGr8uPn9UAQwfRKV2rEGbP8eB3Z25ID_aTWm7Az29xVLpW4topsteR1e7dSp7aoIQlXzrTzfYYSp_zWhIU2H9FxISemfbPtgOxI-xS9wkvmcQrrAO3j95CFp8la_Og6XKdJJcUgrJRcYrobwWjEeeAV-8x7PmLOiRbucdkIrFP0F82H69Xts7ypemJaUetk1XKcLyT0cfynKKpQVN2XoL_0U2Dlfe_z__QnN2CfJrN7q_0Zu80ZTtCuTdBhZLOU3l_uL3OFjeWV8O2rzkQoqNRMH-z_LHcloEL4KaBNpt_CHerJHkwpGT2mCiaOkIKg9JhFLcJcHqTXDsmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqUQY2gPDtWulAhy4N2SAjHMXWTBkJjGvfw4AhKU3PLPN08G4Yis2NOdRiArEo45BPZvWpUuhruojNSIkTuQM9D6HAKgTiJoSRdTTLC5fPPX74TG5XgOEpjLTb1CSK6xyWfcJhMVzMkEUaeg4t4NoghtgGnYWNBAv17qawkZ_kl6feySd-r_13OScvW9NNCASICl6CqShDNWbm8U7RRXvPhRQtcAfyd6cvFLqMgJiBcm-SZBMdQwUZjgRQ1BxTybLw4ekAsXBztyJHjanrM3Vm9mbCdvOB2Ao4rlVfTOjyR2KRWCkqJ1eg0ElBpm0vhzJq8ggodwjHIDf4nOxy3R9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LF8x3pGrZrQbjnLBJTfkqjjNp2atJE1IFFYKuk7CjlDAmfbWTicXaiRE1Cv93s3qsIujR92PJs6VEKCzbGtD1Kf2hxJT-yiRtGrGKL6MaxlXatGWYukTkPD45yqqzdnCsogTIbgfDU-UhIM-dumfb1vazeelQnjSs5VjHOHaY6r2znNym3r--EpRHEznKBRtsO_fIgheLtvnrOWGZddQePEDZ0CtO1yM26WP_a_oNEAKYySdIPGzuS6C3jrBYYCKd3Q0fZySjMLa8fp5Hg8n6EHdbfj_-6W_Y8pl8DHlMtN4iTTs--tvFQCd_byX3jv4oykYRJhF_ru3TmJd1K35mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/446476" target="_blank">📅 00:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogv6INb1M5LdPSsbS6iJXfZ7yry5JmWmI9ThDS-uMVyNSFHf3zjz7koCShSXf-GkHgvPdaKHa0WfCAUA7vuaiCz3KJqb6nxPbi2pjJRqTFUI7-dSWZPX3tK0F1OTbxVLW98oYpOdymEwNbVMnbCsynmnP8PzbIzl6CxHW1dcqVjJ6XDPMnnKZrZ8DU-2FKUCcRLLrv_UmxSHv-j_AJ4lT37QXMO97WEwUKxUZnMP_VnyoHKFW_jnS1eiyksH4YTQj7JM4YvZuHEDp54HDSmsocyQrUgPnhnaQim16_NZQ6dIsXeQj5VutPfycgkD5Se3xkjGSZysix0tMZSAVTnIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صعود فراعنه به مرحله یک‌هشتم با حذف کانگوروها
⚽️
نتیجۀ ضربات پنالتی: مصر ۴ - ۲ استرالیا
@Farsna</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/446475" target="_blank">📅 00:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwikcbWnViwkJ6n2CJ9SoBqAsBxtXz1EN-byiohG8HKF6tPEo7MH44xCEMkv48jRVloVYERhB_n-FG3ZXi8Y3MNtitmrA1t5A91B6GJP2h7kMQRf51scrZHtS0DJwYZG6g9SiK-x_aCE_LlxNzN_O-DWqhkKuwTOY3unnYX7xbpXZtXh2sbaZqY5K7NQ_fMY36NIWW59N-3vUCes01gy-OPCaRaF1gf-af2tfzPyx-yt0EKPRA9V7tUVpiL040MfkjKudj0HS-qs-fMyMxVnlBM78PkkGi4vEmRR6FZkpRB2uHAOBlOZzW3DcSLK5L111MgQeQUSILDtchpob4GYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویری از شهید مصباح‌الهدی باقری‌کنی داماد رهبر شهید انقلاب، به‌همراه همسر و فرزندانش در کنار آبمیوه فروشی خیابان کارگر
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446474" target="_blank">📅 00:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446470">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqBuQtuquAiTHm4qt6ws9QcMpikeAZfZzTTpcLrXoeG3tpH0uxJuVyN1oSBLLERTZy9gcm6mOfcuR1WkMGwy_-dYNcVaLHiGcWZIdfaSXEOD4qSwg0Yd31GOyWJZ1Z-K6AP38zx3UG0mE3OQy3lLT7wHXFDR9LMCWK68PABPTbJY4YNkZC3VR-cZm_vCjRIf1iDuAR7Vn1zVsHV6A410vpPQeMgSKESEeUGHCpBjaKUmQ9kkmfZi4CuK5xx80yUnQT0dm_9CX1tho6kW3oSneD0XSOaIUFxFxsJ3vNuQb1WoNpGtMEVZBYscajNe2FrO4pQqJzmC5LIgHkImIp6xhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjHtTn38MU2Q9M77z1MOoRq-1Sa5O1t8Nk6Vbb4eT3tE67eMn6bhbT1xLYIWouoQKgUm6UAUoYH7ELXgBgEwRWCYmcZ9DPaD2JPPMHgW6Zx36qbkAvykKgZDtTqfIFN8qSAUhdql0x0Hi85NabHsGWg2yanYNyApur_slHKY8iTxlmcUR60OncbFVACzUunyopP_mU0BGEIuUksUfiO2RTGJIx9OJG6ldOl7AY7dWgrvPggOJoZ8XX_nGpY_B1remymFpT4m-2RiCgaWf9uQp6ie9iIpPNrWr9GNAtmf8FlBmNduIqyW1xsFrE8omY5vLf0cn2vMHUlX4Ny38WT0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHdf_czb6jqqBpZfHlGcCJCTm1bfh9c5_U1LGcsstdX-6-HEEecMoshRAw1gL8NzjPXxx22QphMujF6Lv7j2yjaqDV72iGyLHj0LuVbHYTIFRAbYWmZLc3JUCedYbHoi9gERUbGyu57g37UoPnQrYW_9l1piTagiHfY0LeyboYXqDgTr9PhLo1eY5N_xzUesP2VhlFfc4RZIi_JUPbCm9bZdKrjtjN145p8k3imzTd7fJ-k_AcXD9_ZciYL66JvI0Xrw8e9latUcspJAIliCXrh2DVkS-qt6JaIuZ0RFDL2pX0Njwt0yI7XsdOUaaszRWWPXSTFnFkI19l5yJHjg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR9gGxDtjZ23sYU_qy5QKpMJsIGW1eQpKusQil3l0wo6Y1sPBHbu__zLlvFcdSLjg3NlUzi6_0M7Uhui4G9ZUK5b5UzV7mGnulN6KZanhFrOcGo2YNDwyZyZyGkVsrnkFwCXtFQs2I9i0OnomDIXmrp3ae4qSr10mcFCZX9_QkrmRudjYp3KB-qP0GvutrKlybLF22F9TKPGlxelBW1K4GCvZLlFJGDknTmPVdkE9sNHG3b39oZbu8oLhdbvXuCFt_9yWsszib-mTYDhbKZm1QHp1PG7myqdzGK_VRbEZjTrsxhxWEBkuRttUDtRu1mLNJqeZp_U2aC4BluIjiqbMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انتظار مردم برای ورود به مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/446470" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446469">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuM2jXl1NB8e4emNYnbSdFHG00tmsFX3VKEShbWdpnPiAoRcxSdn7lVKIhf4quenhT3BwpAWXne-KkJpIhLR6LqEMcE9CudFXTEi4XIcfSdw3edfm9otYnZqPjcGzvX_lTsBLiJp0_ApT8Tq5-wVuQAjXTqRbIhFxYxW_DDEmkamnTv9bHdLPiTN5psbNJzdmkeYBTHB64CryAlczOS_ETgB6JV2pTo-2vaZIeC_nc1cdLUpTyxi79GjWWbvKBwX4UtRMWeR3VerrI2m_6k8Us7gBGpmLHTeNGXMdoZwSELhQftZx_3bEJLtrpqGDGikJIdOkdMge8FNlJdKPBruOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخت خرما
🔹
روزی امام علی(ع) درحالی‌که باری از هسته‌های خرما همراه داشتند و در مسیر با یکی از مسلمانان مواجه شدند.
🔹
آن شخص از امام پرسید: «ای ابالحسن، این چیست که با خود می‌بری؟»
🔹
امام علی(ع) فرمودند: «ان‌شاءالله، درخت خرما!»
🔹
آن مرد در آن لحظه از این پاسخ تعجب کرد.
🔹
مدتی گذشت و زمانه سپری شد. روزی آن شخص از همان مسیر عبور کرد و چشمانش به نخلستانی بزرگ و پربار افتاد. در همان لحظه یاد آن گفت‌وگو و کلام امام علی(ع) افتاد و تازه فهمید که منظور امام چه بوده است.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/446469" target="_blank">📅 00:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446468">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ada85a1d3.mp4?token=bisy9gNpFAp7QHREpr4BigOwS4ikfcpSDQ1_csWftzWf1SC78Y1dm0_voN4yUCiGw0uBT4kQ9IWXmRXfVX3e7wJZ8ByHngAYIx_XerSEks5v_bbIs6_l8kuEenmwCIwbYZUif6Vv7M9vtw7Bf8xLEE-ouYCi1CXf3FUwMZ9Q9mSiWhllXAdGgwmTpYsynP_gwiP0nCaXj44h02S-R2tf9wVB_I3cS9x1GMKgBkMz37O_fGg8khbE-60uvNTSKByUbrwrl6NHMYeLuLSXEc0F59z8vyIOefTwv_N-SSmA0CvTCjU7ExYHkgKF16DVoYoZE4z4r0Kg1JtyZYuqB2vbtT1SRDW136WSfAO5VfYLV-bSfybPRhYXegafg5O3v17eFPngwbBhKtvMFcCu7qNGdJXoigALyKFIVC7GUwwuOkNKvpPg6yhBRW-MPFSyySQ_sUh3fXhgtTkQZaSjoTahyJ7J2rXkIS3rwSXZN_U07OAhBThsM1aaHb3ssEp53TqLvtslhJz116sGyV-DK3scTubu88EORGeWmgnYO4jg6K1nd4--RiJ5NK10pj03_6OVX6cUGFtehrCinWMMbdJHCLzLS90q2Qz5SXYXLOnoF0mCzOTGcwb1lP0RBnoGbsxqoWwN1wO-jS3VHetg3z0FT_jnBM2J_YlmVLVHviMr06o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ada85a1d3.mp4?token=bisy9gNpFAp7QHREpr4BigOwS4ikfcpSDQ1_csWftzWf1SC78Y1dm0_voN4yUCiGw0uBT4kQ9IWXmRXfVX3e7wJZ8ByHngAYIx_XerSEks5v_bbIs6_l8kuEenmwCIwbYZUif6Vv7M9vtw7Bf8xLEE-ouYCi1CXf3FUwMZ9Q9mSiWhllXAdGgwmTpYsynP_gwiP0nCaXj44h02S-R2tf9wVB_I3cS9x1GMKgBkMz37O_fGg8khbE-60uvNTSKByUbrwrl6NHMYeLuLSXEc0F59z8vyIOefTwv_N-SSmA0CvTCjU7ExYHkgKF16DVoYoZE4z4r0Kg1JtyZYuqB2vbtT1SRDW136WSfAO5VfYLV-bSfybPRhYXegafg5O3v17eFPngwbBhKtvMFcCu7qNGdJXoigALyKFIVC7GUwwuOkNKvpPg6yhBRW-MPFSyySQ_sUh3fXhgtTkQZaSjoTahyJ7J2rXkIS3rwSXZN_U07OAhBThsM1aaHb3ssEp53TqLvtslhJz116sGyV-DK3scTubu88EORGeWmgnYO4jg6K1nd4--RiJ5NK10pj03_6OVX6cUGFtehrCinWMMbdJHCLzLS90q2Qz5SXYXLOnoF0mCzOTGcwb1lP0RBnoGbsxqoWwN1wO-jS3VHetg3z0FT_jnBM2J_YlmVLVHviMr06o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل عاشقان آقای شهید ایران پشت درهای مصلای تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/446468" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446467">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjwOIURE7aLdG0JiAWNtYFxC67XBPS6kKZ3APif7xmHZpcnendQGPXjz3F5z4q0q28psT-2Wsx5sbpUXSvUbIyk7apC3wycSaB639NZOeHVMsObKsONXW2rDBUQDaxcnSIlH11v0vCfaZLVvzXlkuaKDkh7Rm3ayoDdmCrbIXIOD1h7R3NU4Ji8PJjiGRPoxbkT0AxFd_ywq2lDPjiphW81XZU4Vg54GsOk_AvXskV6GWjHhhzZsSvLj2ltN1VB270ZY0ijX751P4Yp1MUiaKXulIZuUONdt__cPzITMRRLzwLgyNlhERNmMV-iBz4Kq7WjSIg6Hr18DzDnR6W0Wxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| شنبه ۱۳ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/446467" target="_blank">📅 00:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446466">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC4-eEELaJkN45kKOYOHF5Vn3KLPGpVOVooDStsTBOHWiHoAS8ji9ur1SPc5ZCwl5-zeDRcwhOsDkCzHQWwR2Of1dL94nfnY1n9p6Ss7N5qsYtt4kCVwoTeoWjZmfyxoP1yFU4lZUjHNSKOikH1qYQsSur3CYLOlHP8cpu6nypZsIyagQNE05MgyXluVGlmGZFEX6sFgX4okrYWmydmFSq0s_YaYxUbZXgio4vQYORzkHA0Wsb-lR-NdxEiKfadFnQ7DT78mgltPcDlu9bYhr8dtpQQVekQwSExYDQ60l3O_Sd57gRnVTxJQ9gJ2XXwjEwqWj8ycL1ErsKdFEHveNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاه رسانه‌های جهان به حضور مردم در بدرقۀ آقای شهید ایران
🔹
تقریباً تمامی رسانه‌های معتبر و مکتوب بین‌المللی اخبار مراسم وداع با حضرت آیت‌الله خامنه‌ای رهبر شهید انقلاب اسلامی را پوشش داده‌اند.
شبکه سی‌ان‌ان
🔸
گزارشگر ما فردریک پلیتگن از مرکز تهران گزارش می‌دهد که انتظار می‌رود میلیون‌ها نفر در شهر پایتخت روانه خیابان‌ها شوند تا برای رهبر سابقشان سوگواری کنند.
شبکه الجزیره
🔹
مراسم تشییع آیت‌الله خامنه‌ای قرار است به نمایش وحدت ایرانی‌ها تبدیل شود. آنچه آمریکا و اسرائیل در جنگ علیه ایران انجام دادند نتیجه معکوس داد زیرا حکومت نه تنها سقوط نکرد بلکه قوی‌تر شد.
یورونیوز
🔸
در صورتی که برآوردها مبنی بر حضور بین ۱۵ تا ۲۰ میلیون نفر در مراسم تشییع رهبر عالی ایران محقق شود این بزرگترین مراسم تشییع در تاریخ ایران خواهد بود.
ایندیپندنت
🔹
مراسمی که قرار است برای تشییع و تدفین آیت‌الله خامنه‌ای برگزار شود از لحاظ میزان بزرگی و اهمیت آن در تاریخ نمونه‌های اندکی دارد.
آسوشیتدپرس
🔸
آیت‌الله خامنه‌ای به خاک سپرده می‌شود. او در بیش از سه دهه رهبری خود ایران را بازسازی کرد و این کشور را به یک قدرت منطقه‌ای تبدیل کرد.
الجزیره
🔹
پیکر آیت‌الله خامنه‌ای سرانجام در شهر مشهد که به دلیل میزبانی از حرم امام رضا مقدس‌ترین شهر ایران است به خاک سپرده خواهد شد.
🔹
خاکسپاری در نزدیکی یکی از مورد احترام‌ترین شخصیت‌های مذهب شیعه، افتخاری بزرگ محسوب شده و بازتاب‌دهنده نقش آیت‌الله خامنه‌ای به عنوان رهبر سیاسی عالی ایران و بالاترین مرجع مذهبی آن است.
خبرگزاری فرانسه
🔸
انتظار می‌رود این مراسم بین ۱۵ تا ۲۰ میلیون عزادار را به خود جذب کند که آن را به بزرگترین مراسم تشییع در تاریخ کشور تبدیل خواهد کرد؛ قالیباف این رویداد را «یکی از مهم‌ترین لحظات» در تاریخ ایران خواند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/446466" target="_blank">📅 23:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446465">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=HFkJmGvYyt-mIULvsolAu52RR9PfwUxJRMByfIYpa9uICLuQ-MD3ZTRgRl811ihqNvpI8upeWuuGZcbJcwhOLIxC2FAznTbWO3cB-YY-XWpRkOzEPv-Mh_vb4bN8dPvGEKG8Hkb7SCkTyHaCJWNNVYvp4ez4R516AFstV1JbJMy4x1sMQd3Yu_wB75Aq8Hb9vK-VP33MT9SAvjw7LZi22u74mcRHVZkxol0NdIeEmFh44zOozorJAz75w0vPJuS4KFr6KDxoEKrrsIVSRMcTBL7M8S9oSrbZbC_nYdk_x5rwcT3N5EZig_1OvNu1cJwBLkkN4MXxRBl8m66q7jvD71F2pBPiVOQPMqbZALC-yXgGgOnF5xzKSGGH_X5lC3hbJVtwT9e6RbWwAIYeCUDSuCizDvoRb6qqzncB-Oni37Ie8K7k1cCQNGpssGnOptDeEv3JybRICty3PWR_Y0TEzVV2oaycL_QcPAwPsQvBTYLXhaK_OOkMDupBq0zrGjohKx9OHD7ePVB-0-akdJe8TRFVBITtxFAGlhC5kaKhc9iX8RVwC3rC1cYJ64-cTJ4Y38F8O2y2EO9uNX3pKlnXL7CAHe2ocJ-4nwl7PRYAaIfE4KXu_uIYL6KqqqAlzao3_I83XdaED1gbTFWU5LMQSlqpwpA2dAM2_NZRvqXZxuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a79a851cf.mp4?token=HFkJmGvYyt-mIULvsolAu52RR9PfwUxJRMByfIYpa9uICLuQ-MD3ZTRgRl811ihqNvpI8upeWuuGZcbJcwhOLIxC2FAznTbWO3cB-YY-XWpRkOzEPv-Mh_vb4bN8dPvGEKG8Hkb7SCkTyHaCJWNNVYvp4ez4R516AFstV1JbJMy4x1sMQd3Yu_wB75Aq8Hb9vK-VP33MT9SAvjw7LZi22u74mcRHVZkxol0NdIeEmFh44zOozorJAz75w0vPJuS4KFr6KDxoEKrrsIVSRMcTBL7M8S9oSrbZbC_nYdk_x5rwcT3N5EZig_1OvNu1cJwBLkkN4MXxRBl8m66q7jvD71F2pBPiVOQPMqbZALC-yXgGgOnF5xzKSGGH_X5lC3hbJVtwT9e6RbWwAIYeCUDSuCizDvoRb6qqzncB-Oni37Ie8K7k1cCQNGpssGnOptDeEv3JybRICty3PWR_Y0TEzVV2oaycL_QcPAwPsQvBTYLXhaK_OOkMDupBq0zrGjohKx9OHD7ePVB-0-akdJe8TRFVBITtxFAGlhC5kaKhc9iX8RVwC3rC1cYJ64-cTJ4Y38F8O2y2EO9uNX3pKlnXL7CAHe2ocJ-4nwl7PRYAaIfE4KXu_uIYL6KqqqAlzao3_I83XdaED1gbTFWU5LMQSlqpwpA2dAM2_NZRvqXZxuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوتید برای «سلام آخر»
◾️
از ۶ صبح فردا تا اذان مغرب روز یک‌شنبه
◾️
مصلی امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/446465" target="_blank">📅 23:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446464">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
آیت‌الله بوشهری: شخصیت علمی رهبر شهید، منتقدان را به مدافعان ایشان تبدیل کرد
@Farspolitics
ـ
link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/446464" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446463">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌ بغداد هم برای تشییع رهبر انقلاب تعطیل می‌شود
🔹
با اعلام استاندار بغداد، پایتخت عراق روز چهارشنبه برای تشییع رهبر شهید انقلاب اسلامی ایران تعطیل خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446463" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446462">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAZ9MTChmuUmI6cXEEYd857dmts23c9fj-YkJl7XPYq23Uc1qg3dSn5wh5S0O5y_kiHlQhpu2qTstql0MfYaFHjAS8PG0BMQ1_woLbMuk-z8ZtPQvuOZecV0RzpMkmhQcC_dB9F836ohbG6xHLitpWgd7qWyXmrMbW_nRUrkmx5d1Q_8C8HDaBZu2ocwSz1BFprttDQWFBjzY3c8v38Vchy4vvOAWVuyFHmdyM--35x2fKkmZoSBEQWZlipNHtrovV1GdPM-gInT3N6dj0yIIj2BqqfdwvV9u5K3TnCBDqEl3TK-SX8mzXrvBSiHOMg_WJSV_Mx2kAXgt1BZ-Q1muA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شعار نوشته‌شده روی موشک عماد با سرجنگی شدیدالانفجار
🔹
رزمندگان هوافضای سپاه در آماده‌باش کامل عملیاتی حس حضور در مراسم بدرقه رهبر شهید را به شهرهای موشکی آوردند و شعار
#باید_برخاست
را بر روی موشک‌های آماده روی لانچر نوشتند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/446462" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446461">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a350193e58.mp4?token=hJmTfo1I_WA_7PphnkaFtJ1daW8W3ijAgZ32KT8MnbFCUyvVPCN8JCA2vlPrSXVNcWtjgY4Lzx5CfvKxf0zG20BImkDkgf3YBYjPsF3ms-QSgYU5sKuQK3H7zDpeR8b2FHt8nTmHdgh95JB7Z_j3xNDRBIF_yKhi6YFeRCJDN9gpMWxjymSnkitg_6hOk-3q6lrhh5qjzaHBG4ckJBQGsbGL8rpDptx3VHzCtfjWIfq3Oo5nqt0mzoVIM4BPv8OnWymCg51gWiAn_EsThuD47HlSntEIvcN0P8G9JnZkzWNPyvmYKWtDgNmV6jLl_MyBkFkyfcu6QC3oYxWLY5GSLHUg59WSE2wi76NtG7tttZoEgPEhVhLZKXTcqmgP4hea3Fkt_0EdjJrWTqtvG9p-lKxqA1WbUCy9Cj1ljfs-LZC59GVVOzGGrMBdN4ixF07Pi8HYXBAHlt03ATEUW0cpF6F7fzj8GxwAb6gGe3H_FRTkB-ITCRYpMoOZl8hFjIOrcYCn1OWEmv2nfM06RvzWnZoVIMH6-Cl6oeIH0MhCJp0b0_v5YQr_rFkot9bO75h8HF1P1Jx34a2FRYqZF3B2D8FNx9pbIu_QYRUvXU0jas3DmZcNW7uvOCW_Fp-MxSDrQYA3LpcLkmCR5aQ_gcoFo-_YX4GLhM3YDbb9qwP1Rcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a350193e58.mp4?token=hJmTfo1I_WA_7PphnkaFtJ1daW8W3ijAgZ32KT8MnbFCUyvVPCN8JCA2vlPrSXVNcWtjgY4Lzx5CfvKxf0zG20BImkDkgf3YBYjPsF3ms-QSgYU5sKuQK3H7zDpeR8b2FHt8nTmHdgh95JB7Z_j3xNDRBIF_yKhi6YFeRCJDN9gpMWxjymSnkitg_6hOk-3q6lrhh5qjzaHBG4ckJBQGsbGL8rpDptx3VHzCtfjWIfq3Oo5nqt0mzoVIM4BPv8OnWymCg51gWiAn_EsThuD47HlSntEIvcN0P8G9JnZkzWNPyvmYKWtDgNmV6jLl_MyBkFkyfcu6QC3oYxWLY5GSLHUg59WSE2wi76NtG7tttZoEgPEhVhLZKXTcqmgP4hea3Fkt_0EdjJrWTqtvG9p-lKxqA1WbUCy9Cj1ljfs-LZC59GVVOzGGrMBdN4ixF07Pi8HYXBAHlt03ATEUW0cpF6F7fzj8GxwAb6gGe3H_FRTkB-ITCRYpMoOZl8hFjIOrcYCn1OWEmv2nfM06RvzWnZoVIMH6-Cl6oeIH0MhCJp0b0_v5YQr_rFkot9bO75h8HF1P1Jx34a2FRYqZF3B2D8FNx9pbIu_QYRUvXU0jas3DmZcNW7uvOCW_Fp-MxSDrQYA3LpcLkmCR5aQ_gcoFo-_YX4GLhM3YDbb9qwP1Rcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزا و ماتم مردم بروجرد برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446461" target="_blank">📅 23:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446460">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e008d976a.mp4?token=UzyUrEfR3YK1AMPf5goJmYW8TLj4bZLyEspKnT6Fo7NywgbtTtB4q05A5V3ht6s3JkxVdfnDYYnpHiJaG4KKKDxGg6-YsSFqHUGGSnTP7v1FmGBS1IfyOgo6BoC3VV3v1R5K1LfwRINaohDpeG2WVvWkaGGNEdNhB_aP3MbNER4hNDmy1HNJZNM3WE2-ZTYQ2vxnYE3yvGp3dFEqPQeCIBzlV1zPh94JCCa3P3NOivjKwExOqr61yhcGD2fP_pF0HQ8zKuq3cGa5Kt-_VBMgxMl8BdZwszAPXdcmpOlUzdyUghLZje5vbla1qIwxo510ISWS9RSdBNJ0rnRx18J61g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e008d976a.mp4?token=UzyUrEfR3YK1AMPf5goJmYW8TLj4bZLyEspKnT6Fo7NywgbtTtB4q05A5V3ht6s3JkxVdfnDYYnpHiJaG4KKKDxGg6-YsSFqHUGGSnTP7v1FmGBS1IfyOgo6BoC3VV3v1R5K1LfwRINaohDpeG2WVvWkaGGNEdNhB_aP3MbNER4hNDmy1HNJZNM3WE2-ZTYQ2vxnYE3yvGp3dFEqPQeCIBzlV1zPh94JCCa3P3NOivjKwExOqr61yhcGD2fP_pF0HQ8zKuq3cGa5Kt-_VBMgxMl8BdZwszAPXdcmpOlUzdyUghLZje5vbla1qIwxo510ISWS9RSdBNJ0rnRx18J61g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بدرقه رهبر شهید انقلاب: اقشار مختلف عراق مدت‌ها پیگیری کردند تا بتوانند میزبان پیکر رهبر شهید ایران باشند
🔹
روز چهارشنبه بر پیکر مطهر رهبر شهید در حرم امیرالمومنین(ع) و احتمالا در حرم امام حسین(ع) نماز اقامه خواهد شد.
🔹
رهبر شهید پس‌از ۶۹ سال…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446460" target="_blank">📅 23:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446459">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎥
گفت‌وگو با مردمی که از همه‌جای ایران زودتر از موعد برای وداع آمده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446459" target="_blank">📅 23:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446458">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8776d64d2c.mp4?token=B5Qs2XwSauX_4K9_BXb3u5cbBpl7v5bpUGp5BnR8ytyjeQuMDiL2qcQsM7S0-DENGHMeB4-B6noe0zdF9JdmUbhveaQR2nj3JRuMqYIsScHHfmevvDawUa1TcUiAatqX389Qcodv_uBj1BfjIBk99S8It-n9IB8hSrB5ZVlpDKrohx037jL0uEp_WkfF32-K_qGozKSLGYNSPm19DM4JpMfbluWxtfnxjn8on74HLHYKqchuOq3XggwACGmWvAd1AeHFQFMlXCK9wq4eYVUwSCa8l8yY6ndQAr89gZw5FwrZ-fY2phq1ejfcM0hAjSFWVq-t5Be7czuPOv504ZmvcIG2Ve9e84ho-gz5cfCX8S13kJL9LZd9-ptEPRjMY_KojHflX2bU2gEK5TN8j1ljrGmQR47X8VIzasIjFafvhBCct8kxHjPzCSfoUr8LptAlml-JpqxiEUcmi9F745s2cap7jZYdpH9nCkE8KzbsS5SuU1Ug4PJn-VETSPVr6jHok_7pR_q7nHXcwiXCCZVVaF915arktYt2L1RdHapbWpl6JhZju0iPAbqfrx_yU77YgRt1434kKpZ9bOjX3-jtHUQjUuq_AU8vdkJ7nkEjJqzsLy6K384vDA0i-NxqG5ZsqkOXgIv2pbrda5-b56iXoieOIgbyOCfjg4stQ7Jb_7c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8776d64d2c.mp4?token=B5Qs2XwSauX_4K9_BXb3u5cbBpl7v5bpUGp5BnR8ytyjeQuMDiL2qcQsM7S0-DENGHMeB4-B6noe0zdF9JdmUbhveaQR2nj3JRuMqYIsScHHfmevvDawUa1TcUiAatqX389Qcodv_uBj1BfjIBk99S8It-n9IB8hSrB5ZVlpDKrohx037jL0uEp_WkfF32-K_qGozKSLGYNSPm19DM4JpMfbluWxtfnxjn8on74HLHYKqchuOq3XggwACGmWvAd1AeHFQFMlXCK9wq4eYVUwSCa8l8yY6ndQAr89gZw5FwrZ-fY2phq1ejfcM0hAjSFWVq-t5Be7czuPOv504ZmvcIG2Ve9e84ho-gz5cfCX8S13kJL9LZd9-ptEPRjMY_KojHflX2bU2gEK5TN8j1ljrGmQR47X8VIzasIjFafvhBCct8kxHjPzCSfoUr8LptAlml-JpqxiEUcmi9F745s2cap7jZYdpH9nCkE8KzbsS5SuU1Ug4PJn-VETSPVr6jHok_7pR_q7nHXcwiXCCZVVaF915arktYt2L1RdHapbWpl6JhZju0iPAbqfrx_yU77YgRt1434kKpZ9bOjX3-jtHUQjUuq_AU8vdkJ7nkEjJqzsLy6K384vDA0i-NxqG5ZsqkOXgIv2pbrda5-b56iXoieOIgbyOCfjg4stQ7Jb_7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد بدرقه رهبر شهید انقلاب: اقشار مختلف عراق مدت‌ها پیگیری کردند تا بتوانند میزبان پیکر رهبر شهید ایران باشند
🔹
روز چهارشنبه بر پیکر مطهر رهبر شهید در حرم امیرالمومنین(ع) و احتمالا در حرم امام حسین(ع) نماز اقامه خواهد شد.
🔹
رهبر شهید پس‌از ۶۹ سال حالا با شهادت به عتبات نجف و کربلا مشرف می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446458" target="_blank">📅 23:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3E03-lra2e6mSQKxh8ZES829fDzWR5hgByF7EGVowtYgeYuePfXPl9npSt4jBYoKvQteDBkmmIMnFNuZPNTkglujwtvss-braWgNxZBpePvNb-dvK_oAzH1_G_35Xsguj6xMfSa3rEmVT6W00RbtIUgCuZnhVxtrwe7WnKlKgKZZpEkrNDKfmJriD1Eg8Ura0i5rcs1GpW_AExOSR7Mz3l48TERxSczsRSXgCwos-izS9pTguWDoKVA1gXJERZDEwx64P0xHpgVja_d9uMdOqK6QU7D7odisdPtTimmyqpGE30lJ6KbI36pHce9PFtDg3MREK2Wom6OGhPPCEz6SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Db4Ye5pyYw-6NCAJ_TU5isHH3B-eap8LtzqQn4Ox-kgMKw4qe0rUOw0EdUk9pskiP9XjfqgPHRBeOE9E94Q0_MY06FW7d-26uBVlUHcBwDzmCEKFpMdsVNl7jQ6wuicPL3nks7_-8lhzW92yoHn4-Zw6N2-Ajahcv5xY25ZIcAWnEpSISfUvE9mWZaH-VBceIZlVILlmlfodpiPteU2dvcH37Cj90l6G0KqSXRudQSEiFTjGNFnMYgYpYopeLmI3CwdlDCfWP-VzxIFr-o5DlWdyT1qZ2q-lOrgWbxi9Y9AbGMBhXYYS7oJNx5rI8rVpOtYsekxyDvOkO0_X8cs8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMX1nxdvFb60vFhmCvwKHem1wzdZja5kfXvpi7AfuhCuJsMxvt__awsedyKaj8SomOAzZuVeG7dP7ZZuxKHrVrvQJpCBpv9lL0_soomYDLYsyISSiKDp0oFuZ6Cn6oaGRnrCKyeHw3D9ip2URcSWAxbBO-BKQ9v2k0oaegklNsmddUu0Rru2RafxNkeSGctZt3xxRa3ZuTegdN6x5BuRw6T43pI0NRdBBQ0MJeGy4uWeDlxvcHrGq7iHPy-2ZbUOPWvc0JqHwOanHK8A08e0hml97pmH98QGSk85vsvVERSGW7mLMlVX22BjJR_OjHEvTbAdv128QN3ktSqnFC9D3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCHIvRkqUFlsPeqWVS8cWnjO7L0Jqo2ClK7RhT365LD22rZrE7u5uLZ-aljt01kimRKWznD_8_XIJICwIyAFOAL5jpC74-1pBalodqOidHwgfza9O9GhNyvZzwm-7HLaVu_piGlAe4tlhhxxbYLxbfaJJMpaeq6lNiCRCSAYQFD0sJgsKtL_j2M_UGgbDFqoF9zinXs-Ga_iok0H8_SHFkuZ3rRATpJ3Nk1f-lLhSSlOg4yLrZIo7Z9rjvEG9v1aLCLs6p8bFvDHppuIS3WDyBy_7OwO6MbToflQaVxPB2Ev3PhU_H5Hwhk0UnXDBksLp0idDkeo4v3gFeJOeFuBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9AHq5AhUFQQvLVhXvOvRa2X8Kz0w2F9i0I7BZFUfbnTPvUSzZuYgqospdQuDHZvRJpB4KUqToWlUBpTDp2ZpFVb13bwLfNT-UoChKSpgvF0DAlo24CBCWiS2JqrWrfPhFWmnE-ZjjLweDaQ5JuXLtm1ka_QWwytDSxqVAYh3pnBTKfopMMYE0b17xYJXoCndX9UnLEzNjXwGigtf1g3RK3QzeIZVorezAF0i1rvZVycbUTmYC3iwC23zsKet-b3GK6sBR4N9ihzrmXzG4X43glo9we38qykq1hteqSogpqsyR91id-K3272BgAyc11Bm7aj2TnF2dMZCAveUBuOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCfU3uKzaTfmH2YgrtWMx6oe70rD3EkbJwzylLtHfkA-Xt53S78kqNu1dDJ0UTu3BDxaLCeHh5uFI6pu2pmBSEOfXp3XhTvqmbwymTUP8biOEIxjbEdHW0-mXkRWh-2du_6ijPqgadxS5NiVmcO7hyACgHJNKscrByuUUhfAE2QlwpffPMDpxmB1qPQNVkVzvlNb3LhJTzbQvx3r451g3T25N4ZTxUyRfZDKzVlbX3TQuSYiPsSOEOJrwA-2tP42WLx3SJRGcQOEpAls9cfSOox8NavoeJzYg6hyt4ajW8W0bA5PUTn6IiPGg7vNNtemnDZ07r34iO581JK83mUQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C_i22rWAJkSw7Sly_9YXYItmx6UtzdIfvwMvZDNwo3RL1_2ZTVJYmVQ18_inxMQ6nhNq8_SU5HUdZOWt-y1X47UcLipqLWOJmMF59G38WAq3l2A0Ed6Ynv7OFeDDcmlDS1Ttx-K768vtHAp6uHYVMR5cB9N8CINnddyCelK5w4kFNJUiPjz6RROxVH8vJiTPTZVyBPItD4E4zy8eS5EidfTlnc1e76Qwai7YTMXM1TcAe5ggwdcsY2naB-bIYupSh4jR2AVCfgTe3K4hG_BJzd8Ku4Psdnqgjf6diCWTdaeuDcf7p-1KNrJK6eeLHvO1z6UlWGwPEEQ7xlfOqyT8cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
۱۲۲ روز تلاش برای یافتن تکه‌ای از پیکر شهدای مدرسۀ میناب
عکس:
مرتضی استادزاده
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446451" target="_blank">📅 23:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950e330a0b.mp4?token=XTipvKgzPrt8JDdaWVX5b4eAq18oyMxuxSDiERIZ0ZxYuxwdvxzENCF0_rjynB4OppD-9_Taar2TQyV7PNbfWC7PVNllRCYG8UGqVZlksUixh3tX_TCDe-RoOWcbc5eRwIDisr9rcZMQrXba0KrsJfkCN8sYWLdgiVAIWMwLF1wttlrb_l4vK1xFtI75RY4oRADy0JPe8hMRU0Z1J7Wp26ZZ4aKRfqHsjcbVOTQvYfaUbD6H6vvj9Oql1wB4JRQwE-l4cCNH9jQQxb99DhdCqhUUuWyXAA03hxcLT25r-rbQfVIl1onls3Spuybtq9dVrrTqfJe2g-05un_8PFl9LRYBsiSmMKMz6KyJDCYLPPHcvGYk5dLjISy8JDExWTnopSftbR0qkiCwCMkUfGz_MztnspngMrynwdqQzF054UH5wEpsA5mef08IvA863UpJ00m3RKB10Bq21wXMhXSBHnC3Up1uTgw6uPxIjf91VohQNbIbfqAcF4BT8QoD1jcmsz_cP9QlaMRrGUIGUwWk4FbuoOr3Nkmu71Ur3Wyoiujs-nZvbONRtfuNLfmUTpp3Rq2FGGf6GR8YZe-jngzXn1ytqxiLH_BpRLGr1NZem1sWkI5pb_k1M_SqAC3Pbb_UhRJM44rVsLdTFJ72xzbnnn2TGEeLitCNIuyTDAC_UwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950e330a0b.mp4?token=XTipvKgzPrt8JDdaWVX5b4eAq18oyMxuxSDiERIZ0ZxYuxwdvxzENCF0_rjynB4OppD-9_Taar2TQyV7PNbfWC7PVNllRCYG8UGqVZlksUixh3tX_TCDe-RoOWcbc5eRwIDisr9rcZMQrXba0KrsJfkCN8sYWLdgiVAIWMwLF1wttlrb_l4vK1xFtI75RY4oRADy0JPe8hMRU0Z1J7Wp26ZZ4aKRfqHsjcbVOTQvYfaUbD6H6vvj9Oql1wB4JRQwE-l4cCNH9jQQxb99DhdCqhUUuWyXAA03hxcLT25r-rbQfVIl1onls3Spuybtq9dVrrTqfJe2g-05un_8PFl9LRYBsiSmMKMz6KyJDCYLPPHcvGYk5dLjISy8JDExWTnopSftbR0qkiCwCMkUfGz_MztnspngMrynwdqQzF054UH5wEpsA5mef08IvA863UpJ00m3RKB10Bq21wXMhXSBHnC3Up1uTgw6uPxIjf91VohQNbIbfqAcF4BT8QoD1jcmsz_cP9QlaMRrGUIGUwWk4FbuoOr3Nkmu71Ur3Wyoiujs-nZvbONRtfuNLfmUTpp3Rq2FGGf6GR8YZe-jngzXn1ytqxiLH_BpRLGr1NZem1sWkI5pb_k1M_SqAC3Pbb_UhRJM44rVsLdTFJ72xzbnnn2TGEeLitCNIuyTDAC_UwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرثیۀ تاریخی شاعر برجستۀ جهان عرب برای امام شهید امت
🔹
تمیم البرغوثی شاعر فلسطینی با بیان‌ ابعاد شخصیتی و الهی آیت‌الله العظمی خامنه‌ای قصیده‌ای در رثای رهبر شهید انقلاب سروده‌است.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446443" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=oYkfEe21M1gqRFH1X6Ry2JoJcmQVoXsffMNOV9Yp44LBSb9-A4jS2YBAOmC3f7oMNo6-U-1i4RcQ6JoESYpgDKpnZ9PO1j2wGC72gCRsa2Wg2eHw1ALf2sjPqv9ozwfbuR5ODZYE9sYyiLp8-ELYye0VVTRCfdXZBeyMF7JnCeXvSuz9hts2d_ezvq_tcQhLsCVHvS_VjpjYHkwkDCpNprP2pIviC9faVinOxaW_PRnQzp3ztVOFkQZFP_gtqtmKf-Xro_cEqJgo3KI1HpA-Wpw41zdwE2CLJb_KZhcGNijddkTkAB7sQNnGFJHVjHPDwaIyEF__beRuwmruzVjBCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d1b34e56.mp4?token=oYkfEe21M1gqRFH1X6Ry2JoJcmQVoXsffMNOV9Yp44LBSb9-A4jS2YBAOmC3f7oMNo6-U-1i4RcQ6JoESYpgDKpnZ9PO1j2wGC72gCRsa2Wg2eHw1ALf2sjPqv9ozwfbuR5ODZYE9sYyiLp8-ELYye0VVTRCfdXZBeyMF7JnCeXvSuz9hts2d_ezvq_tcQhLsCVHvS_VjpjYHkwkDCpNprP2pIviC9faVinOxaW_PRnQzp3ztVOFkQZFP_gtqtmKf-Xro_cEqJgo3KI1HpA-Wpw41zdwE2CLJb_KZhcGNijddkTkAB7sQNnGFJHVjHPDwaIyEF__beRuwmruzVjBCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور رهبر شهید انقلاب در حرم امام رضا(ع) در سال ۱۳۶۴  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446442" target="_blank">📅 22:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446441">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0d65fa4fa.mp4?token=B_3d9sWbRbH3sSVtcqzro78dcqtd0fPBmqjnKs5T5QdOa2j7q77SebkvUr5WOMCGhxrZPXIHaWz959D4ZcUrtGxxXSknkFGFI-6GCI8hwaUlQpA6W9Ysy12PntNQ3tHkART_jupYUFiUbXKcDfvh9SP0NPo2255ehWflJn-qjhutVVJEdhQEIKDrXMj6zMZ2ytWZLs50c4F-g0Y8vxVT8SZjqcCRJzplgrN33Z7brOnG3DP1Mp8iZaHMatUWRRpBKDVBub7gkjpSTtWni130sd3Ip28wCOPzIzl1XAzUXUZTEPQfx4KErpexJ80BVGHo0M2MUVS2kMlCbplG-ZU1kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0d65fa4fa.mp4?token=B_3d9sWbRbH3sSVtcqzro78dcqtd0fPBmqjnKs5T5QdOa2j7q77SebkvUr5WOMCGhxrZPXIHaWz959D4ZcUrtGxxXSknkFGFI-6GCI8hwaUlQpA6W9Ysy12PntNQ3tHkART_jupYUFiUbXKcDfvh9SP0NPo2255ehWflJn-qjhutVVJEdhQEIKDrXMj6zMZ2ytWZLs50c4F-g0Y8vxVT8SZjqcCRJzplgrN33Z7brOnG3DP1Mp8iZaHMatUWRRpBKDVBub7gkjpSTtWni130sd3Ip28wCOPzIzl1XAzUXUZTEPQfx4KErpexJ80BVGHo0M2MUVS2kMlCbplG-ZU1kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446441" target="_blank">📅 22:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446440">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b0c4b111.mp4?token=ID8PE5RnzWnVRLa1AZYKjT0pDgnt3aHIwWbTj5FDbmXJHjFZ0oGTU9FLLZPpdwd1okbJPub13lGsU3RH3wV-CnSKVjOfA9914KlXGmULXm46uxqugGTMIQEQQToO3b29dhmOgLuUAKogJRoXzpsJ0hRS9OXIZcJOkdG8y11NVvY317Ea_Qbns58OAC3r1MYcW77-4nFFiRynrK3CyHSXXCB0aEpzQ3up63HWG5POJLyiIcVtyZBsY4hz3eBRUHUZQs7CpDz4kHyLBTYUi_QyXM7iVvJlrs82G30wF0gdEKVwkOWka1eovvL1g7cMaIPK9XOADUsRq_GF2Z0zlFk6Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b0c4b111.mp4?token=ID8PE5RnzWnVRLa1AZYKjT0pDgnt3aHIwWbTj5FDbmXJHjFZ0oGTU9FLLZPpdwd1okbJPub13lGsU3RH3wV-CnSKVjOfA9914KlXGmULXm46uxqugGTMIQEQQToO3b29dhmOgLuUAKogJRoXzpsJ0hRS9OXIZcJOkdG8y11NVvY317Ea_Qbns58OAC3r1MYcW77-4nFFiRynrK3CyHSXXCB0aEpzQ3up63HWG5POJLyiIcVtyZBsY4hz3eBRUHUZQs7CpDz4kHyLBTYUi_QyXM7iVvJlrs82G30wF0gdEKVwkOWka1eovvL1g7cMaIPK9XOADUsRq_GF2Z0zlFk6Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت مصلی تهران پیش از آغاز وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446440" target="_blank">📅 22:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446439">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b9646a94.mp4?token=eRQpHWMjCjNFmvbF9MPDX2-h1H8Dj3gIxrUEniC22AUEie30m41YxqUZQDs_FB-9BFA79zKrVy4nRRGgkkCaAqsdqv3xOzG9SQwSfOYJuUFuvdjqLzCMmcIiiBiQL8Ns6CoAyswcQfW0SngDgadkmBd9jmp6ArgQyOOkOtKsogE-j2An1WSahgT7NN2YdFpiqEQgRnvd0wHJUiZmzQvLXuFxuCE_-Sz2egKgaJb07-L5WpWP5yS8xi3T2f239vlH5e8tbxiNekNMZjH2Wik5hJquhj2QiyvIRmj2zvyQlfyvJbsEcpKDseOStZiNmQPWw5xe7AgYDIqgv5z4-BZfuEYW5uu7YgaelhvoN8m4XBgEEA0UqaoGAJzoga4Vc3-keVWRBjfhlM8LOd1gzVjieeH0tPl_Hpq2KPu-cjFZzKrsoFukIxZgDr-UXQe4TvvaTvYOzHqc1ZgJ_iLRXihxFtgvv2RXHx-wjnwN2FM1WW-LQY33iy2DMVJ00j4xFGsbTRZ6ddLf7OhIZSdnCYxyOt1uXTASpyk_3czrutOj1EXPKBSLtwl7zb-71U8Kxn6iS-uLriRnISpnl1xtMG4s2S0qNRCXXkET7Gx1_v0b8q79wBDgRO_0-2vzzlkrY3YpqNBxKFO08ST3N3DH4VDLovllkUNGXJNyelIg0z2Ki8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b9646a94.mp4?token=eRQpHWMjCjNFmvbF9MPDX2-h1H8Dj3gIxrUEniC22AUEie30m41YxqUZQDs_FB-9BFA79zKrVy4nRRGgkkCaAqsdqv3xOzG9SQwSfOYJuUFuvdjqLzCMmcIiiBiQL8Ns6CoAyswcQfW0SngDgadkmBd9jmp6ArgQyOOkOtKsogE-j2An1WSahgT7NN2YdFpiqEQgRnvd0wHJUiZmzQvLXuFxuCE_-Sz2egKgaJb07-L5WpWP5yS8xi3T2f239vlH5e8tbxiNekNMZjH2Wik5hJquhj2QiyvIRmj2zvyQlfyvJbsEcpKDseOStZiNmQPWw5xe7AgYDIqgv5z4-BZfuEYW5uu7YgaelhvoN8m4XBgEEA0UqaoGAJzoga4Vc3-keVWRBjfhlM8LOd1gzVjieeH0tPl_Hpq2KPu-cjFZzKrsoFukIxZgDr-UXQe4TvvaTvYOzHqc1ZgJ_iLRXihxFtgvv2RXHx-wjnwN2FM1WW-LQY33iy2DMVJ00j4xFGsbTRZ6ddLf7OhIZSdnCYxyOt1uXTASpyk_3czrutOj1EXPKBSLtwl7zb-71U8Kxn6iS-uLriRnISpnl1xtMG4s2S0qNRCXXkET7Gx1_v0b8q79wBDgRO_0-2vzzlkrY3YpqNBxKFO08ST3N3DH4VDLovllkUNGXJNyelIg0z2Ki8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی رزمندگان نیروی زمینی سپاه برای دشمن در مرزهای غرب ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/446439" target="_blank">📅 22:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446438">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3acc934c23.mp4?token=VeReUjOp6E8usZdnbZRh5Ni8Tg7YZeNNfprHAtTiahdNMQtCvvUaFkyLCliIMyNC0RIeClrkkbKvgLM6l7rkR5X1vpKY-8EabVaZV4oAAZOebax6-ij6sxVRqu-vWwGahmOw9DuN6ms95CuF7bZqb6RK85JIdNZeUTf71MHMCZ0M4ydpuqiru8hB5vby6UtuD_E1NShmdUI1DWBRxnkeJxnV_vloBuFsDQLkBBjqy2vLkPPpshU3bN9Dmq_79ZhZmrCXhNKdvnttD5qwAALc6om1ogGq67NxEvd5LviP2BLmZBVcIS4HstrtSwq4TNF0tqNLGVoA9iGZ_S_pkUGphA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3acc934c23.mp4?token=VeReUjOp6E8usZdnbZRh5Ni8Tg7YZeNNfprHAtTiahdNMQtCvvUaFkyLCliIMyNC0RIeClrkkbKvgLM6l7rkR5X1vpKY-8EabVaZV4oAAZOebax6-ij6sxVRqu-vWwGahmOw9DuN6ms95CuF7bZqb6RK85JIdNZeUTf71MHMCZ0M4ydpuqiru8hB5vby6UtuD_E1NShmdUI1DWBRxnkeJxnV_vloBuFsDQLkBBjqy2vLkPPpshU3bN9Dmq_79ZhZmrCXhNKdvnttD5qwAALc6om1ogGq67NxEvd5LviP2BLmZBVcIS4HstrtSwq4TNF0tqNLGVoA9iGZ_S_pkUGphA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار تهران: راس ساعت ۶ صبح فردا درهای مصلای تهران باز می‌شود؛ قبل از ۶ [خبری از بازگشایی] نیست
🔹
مردم طوری برنامه‌ریزی کنند که از این ساعت به بعد به مصلی بیایند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/446438" target="_blank">📅 22:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446437">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌ اعلام تعطیلی رسمی در استان ‌«ذی‌قار» عراق برای تشییع رهبر شهید انقلاب
🔹
شورای استانداری ذی‌قار عراق از تعطیلات رسمی در این استان در روز چهارشنبه آینده به مناسبت تشییع پیکر مطهر رهبر شهید انقلاب که در شهرهای نجف و کربلا برگزار می‌شود، خبر داد. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/446437" target="_blank">📅 22:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446436">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc0642946c.mp4?token=PHkh3ZsnTX3-uGI6uU7F3yfoXK4QKlE0dm5lTCbi8Fk-6z-sFv49Is0jGDB7_sziu6F0OI8K9GiOgVPGvQ_DNfAGqFObOhQCbPCLsbFQ9DrGeVjHybNgIDASh6s00qxtzaOi6tq9soCu_rYIDNFnOXs-EelIYGBy7Cnp7OMq36WuttGpzzg3bWrA8Girdx6GO9fhieGrXKPx4m7yjIOVAyukon-uofHsaLJrPPrL-Fl-57a3OuzUfHNqVPvVXZELlCZrgpB7eWHCjo-s7rg9jus0P0an7PpXLBvT_dpDWK-ox02T-bO69tSAjTxSbgHwrneE7tFp5S3eyXATRCf6LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc0642946c.mp4?token=PHkh3ZsnTX3-uGI6uU7F3yfoXK4QKlE0dm5lTCbi8Fk-6z-sFv49Is0jGDB7_sziu6F0OI8K9GiOgVPGvQ_DNfAGqFObOhQCbPCLsbFQ9DrGeVjHybNgIDASh6s00qxtzaOi6tq9soCu_rYIDNFnOXs-EelIYGBy7Cnp7OMq36WuttGpzzg3bWrA8Girdx6GO9fhieGrXKPx4m7yjIOVAyukon-uofHsaLJrPPrL-Fl-57a3OuzUfHNqVPvVXZELlCZrgpB7eWHCjo-s7rg9jus0P0an7PpXLBvT_dpDWK-ox02T-bO69tSAjTxSbgHwrneE7tFp5S3eyXATRCf6LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سؤال خبرنگار صداوسیما از رئیس دفتر رهبر شهید انقلاب: نمی‌شد آقا در تهران دفن شوند؟
@
Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/446436" target="_blank">📅 22:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446435">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e176fcf876.mp4?token=WB9g8qJSaEkpCxAn_cYdrk4cLYCm5_u86ouNPnHJjQ9KoGnyjghWgId81_WHdk24OUpgV_b5spc8ie4cp1PtT0aBbLhzMfmCn3jr4fF1TXC2dh4qexZix9N5cPG6t4270_4BLvRSMNn2lZDqAOzFEMKMGDESztIU2cSsByWuUKLypgHIH0nLkQilQxAJnldjTE9PvBPGvD4WzObi5DJpzk4fES2YQVRIb-BFg4TC5-4W0yjYB8SgIJD7lk5_9yYz8HVS8i1AgYYJUE1ql-809fnZ37KjhRT8DgzMiVYu4t8lBmvVVszjbrrNxNml-kUQAznkDLHyW8J3__YPgkigKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e176fcf876.mp4?token=WB9g8qJSaEkpCxAn_cYdrk4cLYCm5_u86ouNPnHJjQ9KoGnyjghWgId81_WHdk24OUpgV_b5spc8ie4cp1PtT0aBbLhzMfmCn3jr4fF1TXC2dh4qexZix9N5cPG6t4270_4BLvRSMNn2lZDqAOzFEMKMGDESztIU2cSsByWuUKLypgHIH0nLkQilQxAJnldjTE9PvBPGvD4WzObi5DJpzk4fES2YQVRIb-BFg4TC5-4W0yjYB8SgIJD7lk5_9yYz8HVS8i1AgYYJUE1ql-809fnZ37KjhRT8DgzMiVYu4t8lBmvVVszjbrrNxNml-kUQAznkDLHyW8J3__YPgkigKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصویری از وداع سردار سید مجید موسوی، فرمانده هوافضای سپاه با رهبر شهید   @rahbari_plus</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446435" target="_blank">📅 22:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446434">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsnOrlZAyBwITkfqsIT4LLZBccbOrbrgHN6mwLHMkVnMwTpJMiQ_Mnt7RUF2cfTUk9stRxbwbPdpZy1GZKVY2oK30NC5AwEWeDqmw5PIeLo1Auz8Qr0e4AuNWhX4JmT_YKUWW-85HQ50inaa1WHfRWjbpFlNSjbFm7-SkJhHHe94V3_HxBHXfDm2Kc1ORRANi_c1JqGz8LDbI-5s-8-HomsQy6c70XPLKtNGRMthMHEUyl8NpUjdaq9b6cRCh31BBBWw0PXgpMU75UUaviPrvWZTcX140ZhZ-9Qp1FpyuBdZrAqic8xi17k3HOuR0cjAu7PAhmIGz-hI1z8mlUnZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش قالیباف به گزافه‌گویی ترامپ علیه مردم ایران: به فکر سوءتغذیه ۴۰ میلیون نفر در آمریکا باش
🔹
تصور کنید بیش از چهل میلیون از شهروندان خودتان وابسته به کوپن غذا (برنامه کمک غذایی دولت) باشند، اما همزمان یک کشور دیگر را «گرسنه» خطاب کنید.
🔹
این حرف، یک اعلام یا ادعای ساده نیست؛ این یک فرافکنی است. یعنی مشکلات خودتان را به دیگران نسبت می‌دهید.
🔹
نصیحت‌ها و توصیه‌هایتان درباره برنامه SNAP (برنامه کمک غذایی آمریکا) را برای خودتان نگه دارید.
🔹
ما خودمان درباره دارایی‌هایمان تصمیم‌ میگیریم شما فکر نرخ سوء تغذیه در کشور خودتان باشید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/446434" target="_blank">📅 22:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446433">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123fcf84dc.mp4?token=T1mmYvfrOwGuotV1zklRQotOXORBIpktpIcKgih-5HDuOP_q3Hm7W8Bq1Xqnrd_3qbtbgIQyP1EB-0B1E2Oh-3Cf6gu-bxtCoerpv4j2stz2iFLhOb1TfLFSnXNkGDZhDCerOdI4N4B7_mR8rG8vK6iUGnIAV2r6u-6DulIzTR9cNOo08jnRnfa03tLoP89rir-ebt334c6I3tvVJlgRZWVbQmUxEJz6BTKsEwIo7erJCCngHqyeRg6iIUc5uC22RqjETLnvzcAK8rzgpVaJ9CYYd0oLXyKIIh27rdsSX10KG6n4r-mQJ0UP99V0SSkyfDxnW8Ob0rxPcqefn5ODMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123fcf84dc.mp4?token=T1mmYvfrOwGuotV1zklRQotOXORBIpktpIcKgih-5HDuOP_q3Hm7W8Bq1Xqnrd_3qbtbgIQyP1EB-0B1E2Oh-3Cf6gu-bxtCoerpv4j2stz2iFLhOb1TfLFSnXNkGDZhDCerOdI4N4B7_mR8rG8vK6iUGnIAV2r6u-6DulIzTR9cNOo08jnRnfa03tLoP89rir-ebt334c6I3tvVJlgRZWVbQmUxEJz6BTKsEwIo7erJCCngHqyeRg6iIUc5uC22RqjETLnvzcAK8rzgpVaJ9CYYd0oLXyKIIh27rdsSX10KG6n4r-mQJ0UP99V0SSkyfDxnW8Ob0rxPcqefn5ODMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ای عشق دل‌افروز؛ دل من به تو گرم است...
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446433" target="_blank">📅 22:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446432">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c5c84c5a.mp4?token=VU6cISYjoGpHShBiu0pGRYyQmvZL9t1t8Gperp0n35Y755HFpeD7qWw3pnmDtCbviSlil2JTpZcWyefBWHIMHLwf-VF-RbQdbxTJh7Zt5TK5zBsJXEfEDBQrwLnm0OuehSBXhS2GLQlwMIpcawFdXR9gOLudJq-FNacfDBB81jLZbMBX3tcYJHRmM15i8GspVql7O5w2aN1PlCbShDtIrTmgzLpWhUb1xZCllKHib9-5vXiXakRPV4NQOvL775D9oRRw3_WHz8wSMq09v1zWkg5W0Vi8qnY5yBPw7wPGnWGMKp8PlO4T2PKGCDSRFo00nr2GmnTTHoKdIKxpjunpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c5c84c5a.mp4?token=VU6cISYjoGpHShBiu0pGRYyQmvZL9t1t8Gperp0n35Y755HFpeD7qWw3pnmDtCbviSlil2JTpZcWyefBWHIMHLwf-VF-RbQdbxTJh7Zt5TK5zBsJXEfEDBQrwLnm0OuehSBXhS2GLQlwMIpcawFdXR9gOLudJq-FNacfDBB81jLZbMBX3tcYJHRmM15i8GspVql7O5w2aN1PlCbShDtIrTmgzLpWhUb1xZCllKHib9-5vXiXakRPV4NQOvL775D9oRRw3_WHz8wSMq09v1zWkg5W0Vi8qnY5yBPw7wPGnWGMKp8PlO4T2PKGCDSRFo00nr2GmnTTHoKdIKxpjunpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همونی که براش نمردیم آخرسر فدای ما شد...
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/446432" target="_blank">📅 21:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtgm7jvkWThL8Djajc1kmg9qerrL409BrZ4bIAVKCloDzDjogmY1kiFRmRYCJI9O07qh69P9QeOftaUferj6Yl23C7lIN5EDwa3KqsEbP_ffxKvkZOCZGgCP0RdgnJrkoBVVZYYECRL_6iJxU15KnkGSk-ETGXn0A-VQIJtQqF_94ANBYgu_yMJc8-rJtKyFtxWlLwgqObsokmQK_hIGIY1AFgB_Cmthvga-8jqWUsEGtDuh433ZDt0mYGNKh1Kqeu4rhUtGNUB9Jqf2XP0WrFpvOKKEFQ-XMdVSYczvGVFXuoplL3kndZ-a7rtbyAg8x6W4U4Ae1s3KKmseHvpxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUF0Hz3wBbq6zjAEvTdsg1eBqFlj4RiXx7pJlzV_KqZq0_NClwNX88ZuaI5Gksu2bQpz3k2shA5S7GMpDNJbwbXHPhFkSa3DSSaSeT5FwaVF7UNqjefBiFZaCcmiABrmD6P9WN_rmFL-CEkrT0F3R-FAOED70b9RtKXZ4GoMXqS8eobpIcyvBnbl0XH-_5hMZNNdFE9H_ngR9uIYBed4hBLjvaKpkjs8TZPCdktFef_oiFjhlV4RCXi9-DuBEBz_4uzI4bg5D2a9jlOKskJFGrbA_AYdrG-2xzNkMnzaumGprIkBj9I1L6tcjL4n1NEIfvkRyTxXrgD_X61kl_SiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DS62LAaN9LTNEuPkkcmXCmGkc5kNzl0Gw6MPvkkkkY3QkurIcXwjnMeYLLH8KfUm_GBcvaeVd-D7-GIvhj-ROcj8jmnfhbqaH7hRwte5mxVfQ-KLK9_psCxvXajyizgTyO6LMTuGK_Kcpvew6qZriKS2HbtIBFqwnoxgJZnETLdhFJYsumCvOjx97WTq7PeJG3fQFqET2wyvdmmdzzaw_Q7PbADeIiFGFK4bShk2Yx-vroTWY5CaIeufXG7RnJgZ0X1ZOjb9ad--DprrAuPuVY-XImjuhtCJMt7ecKgueKHIWLIxle1eb9VWh57MhLEII6ZBUFBFD6esvakNN1AvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF6Ib1Ai7tWVK107glJMHYHIbkSab04H9nUyHF8Q_S_VTrJ4TUesglfULVIj736n9Xv12KEWPkO_ALY4BL8CwFbbGGlPhH5M09U8cYkRN1kYI_kDX8EaMR8K3DWhtWjrYNEWuBfQNQNCegNSLYdrf-3vCrlgiL_eCM5jn3M5vpAiR1xtgJ1CA57IQpYEbx3BelMWlaGDOrvQar5yo6c6BYhA3Q8IkqBI5DXPkwMYOv7beYv6-X8rZkkyQkC6A3H_4U9lyp3TV0CdSARyqh-nb6WO2RPvsoflnyGz_BsRjQgMZY_tCFSwvTERG0Ay7oHyiCjNfJ31xmnwkXmuUIvWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7kU-4C85wiUIePTptFMwUi6pRjNx0yorD2oqtIqy5jyqKjt-eecbCziMPEBYwyid3kYxIPkSeCIKWnHJxbYv8K7L6LERaoBJhS_fhsttqABZr8RS9a2n5JZevzgVakRi1JmI6H7EIYo8ao40c1JFK2QwZ5dgUEsRsdN91iCqjbiMScq4AULCYUNojFFu6TlSwU33VCGeYkY1Nz7g_xEZOuX3wknvj9dNy4RbhSrkOYlDPzJ4XB2B7dfz7hsQU0fd8emoCDNPmCrtKZ6mKlZbOilYd52beabPePYE_gYRMbhvhSl7a_914t2Kxt1kv6sl7hjv42hkq_1rTwg2JPrlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfId_Fs_0mnKWW8ZcoZ5Z-e5stUngf2eJlBcynVYWXuTeV2Y4m3eLi_pzpAtcPH_Mm3WOypvLtGRdCQxB-M15pC09j4im_iOGzezd0EEdt5pEuDtiyJ_rw0TyBjhdQiKsvH6mBg58KmliaXosfjFOu4q1CA8bXF4h7kU0ATEWgDqd4GV5TNQ6sfqfVgG4_lfAnze9gLuYbz4Hxq7ywm4SvXNRVweoN59KEn0A4Bs1DNioo1_ryDVTAtsxYGMAX1duC-cGiawOi_eUdRcBhZ-48L1L0JAroRr0mDYWQVFafHaq8eXRt5DeTwTBKT-86BfYLBuCVcG2kPY5xIXGMmi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IPbLI5-Ay37HMicJuzZPfSqgXOcngRjMgeWT-P5aFOVkrknR9dqn05zMxrUPzKpESKeMVJBMrUJnpTjSxED3puEGh7cYW9yoEBCLGH0vgwA8fZlI2es7yNIgtJjRkLNFcWRUOPuj7HxRylq7VNuHFXzXbpz5HKEOLzWsVyOo_NVAbMXdhTG_Aea6lqZ12lQFC3CRR07ujvWlH37-eSLd9oC_9MjVvrotQqI_LGXbU1w0DGOxKwUgkCsnA4LVAES14w4APDYlG-gIx4BTW2zBD2hdSu0ddgU6_sbWgPRz8opA7ulNh9v6FJXaPverQ5B6s3E_eRteBoN6S9d2yKr-fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تشییع پیکر شهید مصباح الهدی باقری
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/446425" target="_blank">📅 21:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=XvLwdhOjasNuA1nedqFo7_lGfN3F9N50exUBB2cQLVez9bU-l6tm-Rwiu4TsXqGIAedZCFavyj0OxaREb2vwJUV7w53HhtdNowJmFrp1ETuiqfACen-fa-wH7kU-5jZqAUNcy7fpMQLPI7eQH8IMice63RmxNnQ4h-Aw-NUVjoCSAizDarPrpqs0CAWd_X768g572xRDdKnjUhnfvBHULO-AsMQgMiud8SBUQ54cmz1yKgUyp8DECcrX7XcU-gpZ2T7KNPtcneRgTH4GuNTlEcNvP-wGlYbGfuL2BvftyUv5mUqIz1cBpJncYe5jIMcO__eoHi_9cYtp-LgKttz5Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9efa1991e.mp4?token=XvLwdhOjasNuA1nedqFo7_lGfN3F9N50exUBB2cQLVez9bU-l6tm-Rwiu4TsXqGIAedZCFavyj0OxaREb2vwJUV7w53HhtdNowJmFrp1ETuiqfACen-fa-wH7kU-5jZqAUNcy7fpMQLPI7eQH8IMice63RmxNnQ4h-Aw-NUVjoCSAizDarPrpqs0CAWd_X768g572xRDdKnjUhnfvBHULO-AsMQgMiud8SBUQ54cmz1yKgUyp8DECcrX7XcU-gpZ2T7KNPtcneRgTH4GuNTlEcNvP-wGlYbGfuL2BvftyUv5mUqIz1cBpJncYe5jIMcO__eoHi_9cYtp-LgKttz5Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیرکل جهاد اسلامی فلسطین: خون رهبر شهید مسیر آزادی قدس را قوت می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446424" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR244XM_s18T-p82iOILm_j7mYlxAuQ8N_1jrysDg4rPXrF4JXUUUrnVmJH7wS4CpLDqNypoYNnckyOrt7y_ZhnVMt_w_YQfYZVgYwT3T42iPvacLmFoJVafWbkLW0dm6IXu3TfFOYEDRMmUmwHICqN0H5Fgs1sIoivVvGxa7o6-_c4JY-VSNkQayEISmeyF9VMnChBCqZq6MBkDnjk5ZRTuSqynEjZib37O5rdJMG0-fOzsSh-b-D-NHbRRiTqMP2cCuiEtNO1afSKqnMPSYxGI-lOlzreo7BY96RWv6w4r45oXn1n95kPZ6MRnPsd84rtr0iTRRrOB09HI5gGrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار معاون رئیس شورای امنیت روسیه با پزشکیان
🔹
پزشکیان: از مواضع حمایتی و همدردی دولت و ملت روسیه قدردانی می‌کنیم. باید از ظرفیت‌های شانگهای، بریکس و اوراسیا برای توسعه همکاری‌ها بهره گرفت.
🔸
مدودف: حمایت شایستۀ تحسین مردم ایران از نظام ضامن حفظ ثبات و اقتدار کشور بود. مصمم به اجرای پیمان مشارکت راهبردی با ایران هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/446423" target="_blank">📅 21:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea23085be.mp4?token=BDEkDHmY_f_OfoCkflQ-cJjAqNeRcbsxc8TjqptQc5k-EmC876RMd2oivnW_AHMqg4MsnrDTo7ELdkpTyOX3Lc-ZW32ohrv8AL1Hzvt7AhtFp-ocywlIcpezVivvjMcwVg4iqfePU_EKqElNnsj-Cim4xq1KWey5EsuBNA9uAjVHOwfokn7XIk4CSTWYTEbXNbMeJ-uNqssNPddp65bCAz152V-jY0lGwXr2KFoe1UQ-npG-pgm7ohmdVl1EPhOoHlCIzThm47c-8fcd07MU_cDf_1lJQem2A2ye6FeLOy6DYdNodXg-w5vKnW6EE_nkdfKmWU9hdkYHQb0RcJv80Y7hAuWBQiGuMfh-tllEGzdEGM-AkzmVcfUIJ75ykjn5knKpHEIWrarpBNeuDbJD8GUP6jNemJUcqY790knk4oEu9zO7oM2g1AdU6_mD3rsQOF7S_WyEZqk1kl_XWPXXvtxAAipn_-LbEUcPxtWd_XBJDeYf7ERzSeZGp8QmyFOtmvYh1PT33YTZM9Vk4kBOR2lLA7nBVeVf6IPPbkATbUo2ukVA1P9yxpWx-wAqBHK6YY3_m862iRGQ7hRv5aNlXsfJPZgDEmz2t4m4CarGnYVaoPL8VGC91wxwIOdPGT8FVgbib7j5Od-iEqHlmwKJ1Ybgs_KTr8rai4RQoI1YN7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea23085be.mp4?token=BDEkDHmY_f_OfoCkflQ-cJjAqNeRcbsxc8TjqptQc5k-EmC876RMd2oivnW_AHMqg4MsnrDTo7ELdkpTyOX3Lc-ZW32ohrv8AL1Hzvt7AhtFp-ocywlIcpezVivvjMcwVg4iqfePU_EKqElNnsj-Cim4xq1KWey5EsuBNA9uAjVHOwfokn7XIk4CSTWYTEbXNbMeJ-uNqssNPddp65bCAz152V-jY0lGwXr2KFoe1UQ-npG-pgm7ohmdVl1EPhOoHlCIzThm47c-8fcd07MU_cDf_1lJQem2A2ye6FeLOy6DYdNodXg-w5vKnW6EE_nkdfKmWU9hdkYHQb0RcJv80Y7hAuWBQiGuMfh-tllEGzdEGM-AkzmVcfUIJ75ykjn5knKpHEIWrarpBNeuDbJD8GUP6jNemJUcqY790knk4oEu9zO7oM2g1AdU6_mD3rsQOF7S_WyEZqk1kl_XWPXXvtxAAipn_-LbEUcPxtWd_XBJDeYf7ERzSeZGp8QmyFOtmvYh1PT33YTZM9Vk4kBOR2lLA7nBVeVf6IPPbkATbUo2ukVA1P9yxpWx-wAqBHK6YY3_m862iRGQ7hRv5aNlXsfJPZgDEmz2t4m4CarGnYVaoPL8VGC91wxwIOdPGT8FVgbib7j5Od-iEqHlmwKJ1Ybgs_KTr8rai4RQoI1YN7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم از حالا پشت درهای مصلی برای وداع با رهبر شهید صف کشیده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446422" target="_blank">📅 21:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6fb908b86.mp4?token=rTRmgC_EGCuC5zbaEv4ictLnK8YaQg8tBKO_mIYhGTgjc5Z5yyamHVtPEVHwAmRmM4cuvKzJDxsSz-Gq8fczD54Vf27-dJ3fRu3G-8ogpVghBsywFyVbU9Vvj7YxFd1E7_0VwRwQhLvh7_oSndVVRzfrAtxUsfhIUjbcUZj8M_mA7zj1Wbtf5ITNQ8qpKVq4BqQkAh9cOExZQe0PdnXCYHhKA1na7uxyv7IRojrvT6cVNV8CKaeQsrL3A7XbhkVir3ANn8xZJEjhInBUqFK6oi_IzuUe-9i-YN6AXmbnmKCZCRdd9Jawr71rYV5g3cGHyrOSyu6GLsNpIcC6fBGeCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6fb908b86.mp4?token=rTRmgC_EGCuC5zbaEv4ictLnK8YaQg8tBKO_mIYhGTgjc5Z5yyamHVtPEVHwAmRmM4cuvKzJDxsSz-Gq8fczD54Vf27-dJ3fRu3G-8ogpVghBsywFyVbU9Vvj7YxFd1E7_0VwRwQhLvh7_oSndVVRzfrAtxUsfhIUjbcUZj8M_mA7zj1Wbtf5ITNQ8qpKVq4BqQkAh9cOExZQe0PdnXCYHhKA1na7uxyv7IRojrvT6cVNV8CKaeQsrL3A7XbhkVir3ANn8xZJEjhInBUqFK6oi_IzuUe-9i-YN6AXmbnmKCZCRdd9Jawr71rYV5g3cGHyrOSyu6GLsNpIcC6fBGeCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس اقلیم کردستان عراق: جمهوری اسلامی با حمایتی که از مردم در این جنگ دریافت کرد وارد مرحلۀ متفاوتی شده است
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446421" target="_blank">📅 21:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446419">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZWGIyO8uB4JwWGSMraFJzOz-ETKdrqznhf4b_atbFIRRHcKReGD_M2AxPqJXJskThu0VJKBQgo8Q6qAFvPxkBQnkm0Ogev11gLqSOofhKdIHbZWh1QWpD_17QIJofQi7VfMJAKLvjCaCvyPSebO6Vmx_ZEJKtaivN-Y3c58nHb6ML8Hg4jlApTT3tm8C7Fh7JMsEfZtSmx_PRB7WR3UN549jEC0rGdCKCcF7-C3ddld9d8cCdjNS5rjd4-nCrAJ4j96yxGy1MZczYV3buLcXjgof1k-fx462NOgwG1lusVThP37R7nWJCIF1Uc3BpYjx44o7rF56Ax0fugXqsidEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پورجمشیدیان: ۱۷ تیر پیکرهای مطهر به عراق منتقل خواهد شد
🔹
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: در یکی از دو فرودگاه بغداد یا نجف مراسم استقبال رسمی با حضور سران این کشور از جمله جناب نخست‌وزیر برگزار خواهد شد. در ادامه، تشییع و طواف در کربلا و نجف…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/446419" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446418">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPMPjp8_4U5KtIvk48F06TNAKcGnGLBq8kCoZ9PzieLEfWuYubz9CaCKJhpfwObRZxLWm8eLjB_HhzVm1M2YZGvL_ZeNWZJ1yYMB7s--9ipNkfDdDjKfXr4Hv7CeVD4_fouT-sIUwc8QCgjuOebqtOH4AMF3McC0J_Gwj-PI_yRPtjbjkiaN5v7SbgpA30VuO6Rc5TpmSY0j6P6dOmq-LSmiffu4j1LpE5KuPnYGi0oFo7yE61hIFwxqBBqaaphQecmV9E_2RQV6g5FaumHPB25CMZ8Jw_IL2VQ5d1dEmrOIv0Mvo5jiCygIq0hzhy0ocRY8L-r-wPFLg99_2Qv4Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویری از وداع سردار سید مجید موسوی، فرمانده هوافضای سپاه با رهبر شهید
@rahbari_plus</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446418" target="_blank">📅 21:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446417">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5075a6dd50.mp4?token=WH240uKr6R9po-Nb1iF4mjzbOGGRUlBea94tAoFmmsMo4YhucrQ_WoJ2WIfdBFN5Woa9E5CTPoKwSx8I0qxAqjWczmKKi0KHf25VV5XmnZUgZLGYNsibx2EjPr-5PIAq1x9ZRFVE-jqcgZE4fPG9zvZFF0MyxzzH6UNqvdNnVOmJsm44wGVgp1lrluzWrOGUTCjvhtqtojAlwP4vqqgfGAMGi47eqtnUWO6joy-B3pmR5W9yt06vE8faIc0uKB9SCAxsbUliWZsqaGVLU-fpPzu_sSu-OqYw7EeZ6H9Hs_o01ksrufw0m0_KMdDYGupYZ6XN0Uh0XdR_AjOPESZFIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5075a6dd50.mp4?token=WH240uKr6R9po-Nb1iF4mjzbOGGRUlBea94tAoFmmsMo4YhucrQ_WoJ2WIfdBFN5Woa9E5CTPoKwSx8I0qxAqjWczmKKi0KHf25VV5XmnZUgZLGYNsibx2EjPr-5PIAq1x9ZRFVE-jqcgZE4fPG9zvZFF0MyxzzH6UNqvdNnVOmJsm44wGVgp1lrluzWrOGUTCjvhtqtojAlwP4vqqgfGAMGi47eqtnUWO6joy-B3pmR5W9yt06vE8faIc0uKB9SCAxsbUliWZsqaGVLU-fpPzu_sSu-OqYw7EeZ6H9Hs_o01ksrufw0m0_KMdDYGupYZ6XN0Uh0XdR_AjOPESZFIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رهبر عزیز ما در مقابل تمام قدرت‌ها با قدرت ایستاد و از استقلال و آزادی ایران و مسلمانان دفاع کرد
🔹
تقریبا در دنیا کشوری نیست که بتواند در برابر تحکیم آمریکا بایستد اما رهبر ما این کار را انجام داد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446417" target="_blank">📅 21:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446416">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=dGVL2c3ItlpOwoo_vYWaTVVQlY38k7ADERIwgeF_8D1v_8gZZ_cdBWy6odB_scI8nWVyN-tTYrk3BlDBeBhmck-Jx_uC5_yIWqz_X_UkMGGyRQUFrKkGI1DteKZj0Gdt3Xo7RF5tdldYNXCyr1RPfnWyywDc-eMYrR8P0Xwl7Q47uJjYbe0n5AerbcfEyv5ilhhe0lSxTf3fmYQ71pfLdbMnhTItucidi79w8A0ttlqT4NkyZwvrWH9L-iVGbOjIPhGRF4O9qEI415TKRJVs-xFMiSgNkyncyx8yQeVG-a61OjVVAI3yLCDUJjmGOpNF_KpSuz4ccv_SNmDoanLypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a20753a44.mp4?token=dGVL2c3ItlpOwoo_vYWaTVVQlY38k7ADERIwgeF_8D1v_8gZZ_cdBWy6odB_scI8nWVyN-tTYrk3BlDBeBhmck-Jx_uC5_yIWqz_X_UkMGGyRQUFrKkGI1DteKZj0Gdt3Xo7RF5tdldYNXCyr1RPfnWyywDc-eMYrR8P0Xwl7Q47uJjYbe0n5AerbcfEyv5ilhhe0lSxTf3fmYQ71pfLdbMnhTItucidi79w8A0ttlqT4NkyZwvrWH9L-iVGbOjIPhGRF4O9qEI415TKRJVs-xFMiSgNkyncyx8yQeVG-a61OjVVAI3yLCDUJjmGOpNF_KpSuz4ccv_SNmDoanLypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسعود ده‌نمکی: در تمام سلسله‌های گذشته، خاک ایران از دست رفت و کوچک شد ولی این مردم اجازه ندادند در جمهوری اسلامی یک وجب خاک ایران از دست برود.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446416" target="_blank">📅 21:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446415">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe1d1a188.mp4?token=BdRzCtswJdT4KUKSS8TXMpWWsCIAl-4D_wJp9oE-SZzIzWxrzZod60CGAouSZTSD1ilfOe3g4mPvkG3wk_LucSspKDnGLpFYUMqEBLTqn9WVbdRsFyd0O_V3-YeyrFPe3SjEBSzxO2JTmtsy2zrOEHbN5aBN9utRlXglDqUaDqd4HWUB75qZrcMLFLKQu_4h42BNzx4FYmaxb-QvtPPtQjrDIRg8pinl4KIo0PMY4blpEcDcQ0oBuFBd4y77UkwQe5_-PFU6gVfalJG6ZFAld38W2n0biOWLhg4PabSTqKCtJmyO01oinXzOZoAdKikVCo9YslZb7PB7J7U9KsdBVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe1d1a188.mp4?token=BdRzCtswJdT4KUKSS8TXMpWWsCIAl-4D_wJp9oE-SZzIzWxrzZod60CGAouSZTSD1ilfOe3g4mPvkG3wk_LucSspKDnGLpFYUMqEBLTqn9WVbdRsFyd0O_V3-YeyrFPe3SjEBSzxO2JTmtsy2zrOEHbN5aBN9utRlXglDqUaDqd4HWUB75qZrcMLFLKQu_4h42BNzx4FYmaxb-QvtPPtQjrDIRg8pinl4KIo0PMY4blpEcDcQ0oBuFBd4y77UkwQe5_-PFU6gVfalJG6ZFAld38W2n0biOWLhg4PabSTqKCtJmyO01oinXzOZoAdKikVCo9YslZb7PB7J7U9KsdBVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: رهبر شهید انقلاب همواره ایران و ایرانی را عزیز و سربلند می‌خواستند
🔹
۳ اصل عزت، حکمت و مصلحت با تدبیر ایشان در وزارت خارجه شکل گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/446415" target="_blank">📅 21:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446404">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=A6-FXA8L6D_v0Xhf9N1-PSCwEVALzauHg0LttqB5jBshkH9ULC04KFIsSLi9S3u_rhUo_aiYQi0CsH0HYQF5WhWR_FwoSdnyiCky0u-S1Se6INWlQt8QteytVw6_B0Ksuk3K6JdJu8PLUNW2a2wO92wx5zkP-eZ62zbwxOyuGR73w2i29J3nPYQOtwLqkzcRnj49NwuQuMg-Yicxs-9qFXf02MXQSKhD2Vbt1wFWSc4lR6dmY-jowBR55iRH6SyKuODdpOm3pMUyb56Mka3HxnIAxU61gIJ3q7L6kAJTirgCnekdBv591mUMnolvEdcKYiGgeAbHphxwYybbkWZE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c187e9edbb.mp4?token=A6-FXA8L6D_v0Xhf9N1-PSCwEVALzauHg0LttqB5jBshkH9ULC04KFIsSLi9S3u_rhUo_aiYQi0CsH0HYQF5WhWR_FwoSdnyiCky0u-S1Se6INWlQt8QteytVw6_B0Ksuk3K6JdJu8PLUNW2a2wO92wx5zkP-eZ62zbwxOyuGR73w2i29J3nPYQOtwLqkzcRnj49NwuQuMg-Yicxs-9qFXf02MXQSKhD2Vbt1wFWSc4lR6dmY-jowBR55iRH6SyKuODdpOm3pMUyb56Mka3HxnIAxU61gIJ3q7L6kAJTirgCnekdBv591mUMnolvEdcKYiGgeAbHphxwYybbkWZE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عباس موزون برای اولین‌بار راز گلیم‌های آبی بیت‌رهبری را فاش کرد
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446404" target="_blank">📅 21:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446394">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HunfiGdDVSIV9Yg5aFU0Awd3iSgx3JNwJqXY3EvL7XhfNt-O2QJPENnDxF4ueqcRi73WE-yY_oUZuRj2Fm18js6nTDmYQf0qM6KkqF3NVyI5fU9HEoT0EfmXTdNYapc_BHliYYlg2p4Fz7p0Rt5ec9pIu6p2dgXIA2IjD8YRPje8RKIqAvCNI8sJUiJZ4TGXRa1dMTaY_7p2tQTtVKn_uolL6LXNBkFgDLFU-O55_pX-fmR2p_QAxRWqB4boUZFN6C_DzDtJH9ZZAYLETh4Zm_FmkJRzwAVJUyuCV4K4uxJmjfW6r-AzNlefwswXdKPMukHP4tkSRWLlWlBNIahRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtJLLxdFLmum1wfzwbikOZkDA695_YXh8Ske2460sQsjlQabZANNxigRm6R99U9InpXf1AWw5ao6Snimgyk87VYdgJVjcAs5BGenhJsELbberVBZjYFRr5ftZqToH9-YpHWdlosHY5_lNQ5KbCRqR6mE73rnsvtlbYXc8s_Pw0m6E4khg-qPiXvDrK8aqwy48AMjHFo0mn2CBvHzAqbmiLOP7tDxzHzm4zPIcoPnhY3XvGChPUaoG0IA1mgrlP97GH0VKFR_8qkTKaSWN7N12RBSFdNhEsVNOKShIZKlFXNZh4-v9AkvFSlLV04_Hv1BgKrYBpAtHy9x_N_gwVMU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxJg8roUpM1SaesmNI8ALK6qtJnGzB3G_0NfvgicVwR-7kWuf34X08JYzGg6gTjetcI_w6DRLUBiOrPWfDXRuXgJ4L0Xc-sXnilvQgZHqSDmeTByY7kuGDYS2hI5nsRuKq79UdbwsmOMbBtp9aHAzUJhWPv2fp1wS309OQkcm1zPkj1RXzMLNNp9FanNciS5hTj3DHkgiHcoGeQyXv0dF61puDncwzfTCyCVkgrc0T9sgdiKizBgCMeSXVpfl-5QAihZQ8gQEbshbB1Gkq8ZHZ5IlieHBLYP0zOEW9pHseSQ-2aLKPdolqtzRhXiybvPJtJcpMMrr00uSkWD8jIs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juXNcE5odA71O8-2XvZrxsxSy1FqvBFK6YVDZYD7msfQs07IyobD6-nVre0MUon73pBUbkBBG8pMKK-NDLdZyKJd47UjhCe2-xpnOoY1PQsPUnzwNJQNKBAIcek7ZHYmKDYUkI8mlZE6JRugmLCByUVnK_81cPC3rKbgpyLKfOU_M3GtUCAYkipVH2prHJM7DpK3HvERlska3PKQHwDJSo__mYlJeEyorwtXl1L03DsmCVX8fjBaNEEb9jZPJjHi4nvRuKcPPJTr2W0lM3tXZ9F90vMVz10Rv1o9vX9zIo-pWpnybFi17_fmg1vfXPQcXST-1yYI2xXJYR2yds6Bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdwSswt9ISwlepzppCwLldCJwPK5mf9QG1eJeSClvIMjJ3OJSFaTzPmlTL4zgCemMLJPO-0gE0U0SStJ4B2nxKWFXfGzB50F181lDqxOIuM0qMK6aVGkA4lSmULoglKbxlDbdRP1BrtpMJB-lg-ib4MfA9xQR9zjsvZ4N-h2KXW97DFL2TjFvAJ6-nOEtIIOtpmsF4fZqyVN3C8_rAh_puPn8z4UYrHaQ2uYpbZigYIN2IXJq3jlALtq27AwPXBFMrRIWcGpXDH1n2vEnyHNZZdcnELNwpFc76XicVEsZN5oROK0_vB66B-GQ-IqPXxxu83JpdAMrMOIBesw8CEcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwj90iZu-sPv_0Bz0GEp2UuueSpEIpPtUeNkdLvHdYDEAmNZ0aYQ7F9Zv36fK7jzxrUtgwM8_jOSXIYfWCeuUI6hYXiPk-NcVZaUxUggRK2f3VdCQKfKp8Q-HxuIqFA1HpIpM0ESYAn2uZGkp_DUxWAuytlsla7sbU8RKNb8sxk_nK1uKzs30Kt_c8MS0EqHee1vEaxTky5HZRVUce8kfIZB2iP1AdsMssi1--T-a0bKQGGDHisRPdDd2Z69fAHJWznhP-0LNpxk0JHS2ZoO0aqlFxqCOrlsv7P0ovahf9Ord3dY_VtdcC96QYIDJwxCSJ1ojpkjafO6Hj_wi1HiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rL500rdf_aL_mmeStcgkROIFYN2HXCoo4u9v32rpcnJZdKWFk0tmuwM9mb86znf4KNrKL14ezNfhUzqln9iNVVU_jlNuQ40GpNJzDM5psncKAoAyMsLBQ_MYEry1VFza5oP1qe8lIxqcBC5qc_aTkQtVS6YKkfECs78IX3-KUazZJTdoJDym45Y_eUSKAGm2SwsNLUwha_KIqCF601Ld8X_TpnMh_fDQvLkIpkOFD53q_cSPTMbSIw7Qc5bqSSef1ebBbClwkUvWOk1XPcmN9wsUqwdda5BuwH_t9eNnzf5R4WjCyqfPI8U7QIkn23G3JLt7XiANBgC2T5bTmBY8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/av0qHstAzph8vf7Tjs6gaPQDkGJO6lAFEEzVSUnbC5ePIsMzpg3ZJ2q1lXUGd9SKcTpsq_si_-Xx3J0ycnHcr0ZMk973ueUYfyEv-y3VQ_u97gmlM5JkBRgpVijUWIxhzxNoBtCl8zDQIhkThZgb9jZVlLCTuPkQ4RRLs5XilVF0EA9_2JIJaJRqZhF3YXKgA1U6-RDG50yBFQfnzwJ2PtZuNSAocrLetdM1bvEukLNFR10Yx9dnDs6LYhugtXTqJESEsjkpNYdzR6IU4RAeaiIlhsdlZpkznVA-Q5dbSN-6nKMMnvFXoWl7i_9Hb7vgIFC_bafncOvN6ZrAkBANgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYydXeXMnqhM6kI_j4fw6S7vi5AAdXV3t3Y4ru9kKP2Dq-N8Gplggh8NriAc1Ok4yY21Z51QF0mB3sne-SCz0QOJ9n7xNK7W7lhsgiD8ePmnCJhvzSFVk05CoGtRv7SEdJuyKgqHiFkNkhJ-V_Yu-YDvUGMK9JSrZeu_XEe55zSkbMAm1j530llp9NARYXJ_ov5STb72UErydau1uFVklKqIdxkIY9BfHTpgc8A_YPQhZFAW8m5Dw43Z-5dk_l_DRCCBdckDYPsiNzxIU7NbfPp9BjnrJlG3NHnCJ6qR9ePWyBZFQ4gaWbG651H1SU0oM_QmhSILEGEH3CdU8aYzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTVbMsSbxDu2JvW143j1_NZ986hC_UhlfegYx63rEobTAImiWPdq8rdT2hCiRr7vKtOav-jEMisW6DYwnu7qx-2bDorfeAGUHgr9Pmy3z8SOPcD8b5uyIga_0boV7OdXtp5IoMpYuK7RJ3YY1XLFGdQCyinwK9xE4PtvcVJx9Y4ibMB7QVKGBVTHWfoyXEV012_dH_mD73rMMhAN6C3a4F0vj-fpPP2eKKAEuuZ7s6rAfpECCISv1eFrWl0dGrLRbq1z7N5AFhwVml_z-zXWKRuzj7EuQe71wkaDZmkvFj-u5CxgfPwRATCEXeQQIclv15gYiFbb7omct2Raj_GtNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
سرودۀ شاعران در رثای رهبر شهید انقلاب رضوان‌الله‌علیه
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446394" target="_blank">📅 21:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446393">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca41dc09d7.mp4?token=lIOrnveIf1sfOnpo_EXTAsANvfTti33tkDRolMchgA96Y4n-FwC88c3sOAZeSPKfu3KxjDZEh4cEvAOqgT9s84pcx4s1cts37peCOiBHW5Ynqz3YUNZa__QisiILT8y_TaGrURXOHPvnkuaZtgYd57rUo0c9ec2K_m4iB4KRAk0-DlLu7dUCRQHoRzF73Cw3Og_eB7CQpoB-d6oNmz82rXR9ROuAXGO4I54G_h2bb2uzkGz1E3fmeWnCUNZtEepmgON_DeAexOCzVnMwxSIvzMApMLtPObK8WbloJyfJY3CeSlCboubJGSvzhLfik4CHx1aW_7UduLs-1JSNK86xaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca41dc09d7.mp4?token=lIOrnveIf1sfOnpo_EXTAsANvfTti33tkDRolMchgA96Y4n-FwC88c3sOAZeSPKfu3KxjDZEh4cEvAOqgT9s84pcx4s1cts37peCOiBHW5Ynqz3YUNZa__QisiILT8y_TaGrURXOHPvnkuaZtgYd57rUo0c9ec2K_m4iB4KRAk0-DlLu7dUCRQHoRzF73Cw3Og_eB7CQpoB-d6oNmz82rXR9ROuAXGO4I54G_h2bb2uzkGz1E3fmeWnCUNZtEepmgON_DeAexOCzVnMwxSIvzMApMLtPObK8WbloJyfJY3CeSlCboubJGSvzhLfik4CHx1aW_7UduLs-1JSNK86xaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تو رفتی و بغض، سنگین‌ترین میراثِ ما از این رفتن شد…
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446393" target="_blank">📅 20:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96758e532.mp4?token=FM0ItB7AxdTSwc-okLqcuPQkm8a0HuBtvXYpaPF2sGIYFQKHShIUCuu1zpzP3VuinMXPxFbCQpQsRLnARi-49OaIjFsIAmJN1TwrUSYLG2WAqKjkq4ly649x_EJC94NNgLIeT82_YfsnvdFX3D3FLMwPvt3B81G3Kz5ewbGl92A1xa4fAIOZBhCyGuu8UOJnoA9Uj2RPPjKyGQ2IFTn4tRvN4JyF-0KAmzoVzMIGnMcuQFgmviQ-fC6NI_G-Vfq5mUwBgc1hTB4nM6F4OVbJnZK1ha18x3TLcS61hoCxS6ihjlk8KFEQ2qQPbpgvPIqNU0pt0BWjtqqE69dP7iC4Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96758e532.mp4?token=FM0ItB7AxdTSwc-okLqcuPQkm8a0HuBtvXYpaPF2sGIYFQKHShIUCuu1zpzP3VuinMXPxFbCQpQsRLnARi-49OaIjFsIAmJN1TwrUSYLG2WAqKjkq4ly649x_EJC94NNgLIeT82_YfsnvdFX3D3FLMwPvt3B81G3Kz5ewbGl92A1xa4fAIOZBhCyGuu8UOJnoA9Uj2RPPjKyGQ2IFTn4tRvN4JyF-0KAmzoVzMIGnMcuQFgmviQ-fC6NI_G-Vfq5mUwBgc1hTB4nM6F4OVbJnZK1ha18x3TLcS61hoCxS6ihjlk8KFEQ2qQPbpgvPIqNU0pt0BWjtqqE69dP7iC4Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار میهمانان خارجی مراسم تشییع رهبر شهید انقلاب با رئیس مجلس
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446392" target="_blank">📅 20:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgDBLDwUbFIGrC9_e4Ut8YguY-f6jX2utvuLsZ2x0XRLbrGYMEWT5YzqqwLHA5kro7hezG5_MTLlwb4eDTeNvaextLo8W5r7GhavypD-X8XbUit5zjesrHYUMmmRunjJwgGURL-zuKXbIBLy8GJaZY-KmSgZyBLscg8U2Cp5RrEGEOAZLh2RCYvpaSoSuFmxyH5qnVWrj7CchTDnWCONGMi1HvWzdeNlmid7WiHUKOfudbmWcgyMId3bFhPy6FhKIxWBndgMazdde4AZVPADpW_5uyjNMbAWyQfEo_x9NMXM9rbfCYJoq7HRUOLYF3wK4VbxopeTNM9QoB9M7X-U8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
کدام مناطق بدون محدودیت هستند؟
این مناطق یا محدودیت در آن وجود ندارد یا کاملا وابسته به شرایط لحظه‌ای پلیس است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446391" target="_blank">📅 20:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44caeda318.mp4?token=ccRU8QvSEa-S31ZQAYzTHvRGD7Lm8xlAoUsQKPzlQs8yZtp9hXPDEyIcoj96dMXIcb951xDJULn1H96apUbZJqn_q2roW3EOSFiphxYwbDKH6UjaOKeYlTgMKeajcsUKw1PoO3rtKJjohHZg52bSjIzyRKzagMfYsawvoa7NgkfAaCJmLgShOFzJwqjC4XYOVkazQ2m_yPpMuv1ewhterh-fR8eQEhURaDFWnKiLNU5iBsYc3PGyLSJspElEkPUkabuz39ScBjexItuaRAcKP_eg_5UJzY36j1cA3sR8aN-UP73sPP622ichWp0WfwEa-r6tjVBlJIFuskwmeyTebg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44caeda318.mp4?token=ccRU8QvSEa-S31ZQAYzTHvRGD7Lm8xlAoUsQKPzlQs8yZtp9hXPDEyIcoj96dMXIcb951xDJULn1H96apUbZJqn_q2roW3EOSFiphxYwbDKH6UjaOKeYlTgMKeajcsUKw1PoO3rtKJjohHZg52bSjIzyRKzagMfYsawvoa7NgkfAaCJmLgShOFzJwqjC4XYOVkazQ2m_yPpMuv1ewhterh-fR8eQEhURaDFWnKiLNU5iBsYc3PGyLSJspElEkPUkabuz39ScBjexItuaRAcKP_eg_5UJzY36j1cA3sR8aN-UP73sPP622ichWp0WfwEa-r6tjVBlJIFuskwmeyTebg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانه‌های کوچکی که دل صاحبان‌شان بزرگ است
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446390" target="_blank">📅 20:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446389">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280e9a8a2e.mp4?token=m5e3VaRb87f7w4F1C2GtHVRfWZvDRbneT2_f_BeFTvSeC_hmIDUh1bpnD6kcB-eyrMZo0WxVvEPFLPNaAZ6OJAgEZ9oov4v1tOkj9JGht4usbo2qTDldw4qWpOdcYu1ukFhJWeV6ntmDdbO7lh4M5Ufa4qR3znHP1Q-KWQ8oSepOlOuPyN-yNuFkSxQpzVvfEWgrcW1xixxrludgp5TyDLnDzMvY12W2gcDO0knGjxaYaKd_3g3BPJdty8FxFv8meUouYTPd2upln83gXiAhhC1R81Yt8LairAsMMrN8AEX2xpGNeKc1Ec1LLL9mz66iQeiIyOZpjE8e48ByGDG5Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280e9a8a2e.mp4?token=m5e3VaRb87f7w4F1C2GtHVRfWZvDRbneT2_f_BeFTvSeC_hmIDUh1bpnD6kcB-eyrMZo0WxVvEPFLPNaAZ6OJAgEZ9oov4v1tOkj9JGht4usbo2qTDldw4qWpOdcYu1ukFhJWeV6ntmDdbO7lh4M5Ufa4qR3znHP1Q-KWQ8oSepOlOuPyN-yNuFkSxQpzVvfEWgrcW1xixxrludgp5TyDLnDzMvY12W2gcDO0knGjxaYaKd_3g3BPJdty8FxFv8meUouYTPd2upln83gXiAhhC1R81Yt8LairAsMMrN8AEX2xpGNeKc1Ec1LLL9mz66iQeiIyOZpjE8e48ByGDG5Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشور پاکستان: رهبر شهید در یکی از دیدارها دست سید عاصم منیر، فرمانده ارتش پاکستان را به گرمی فشردند و به او گفتند فرزندان حضرت علی(ع) هرگز سر خم نخواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446389" target="_blank">📅 20:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446387">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmoS48fvRula-2tCQ7ou62UOy5bWlZJQvFeSdHnn0LMD9Uz_QY20GEuNRCcoub-EJmquK2HWkqhnT-wVBRZQ9k03jAnquO3LBpSK29eamz6c1xuiAdiASO_gtEiTajn0R4fPUFwR9xK8VMipk7F3bw-Ycjc3elDIy1PK0EOtdlDicI1VhjHKQjCpjYJV_9D1z792Kzixfbu6v9narjNGo0Ok0NWMpvXznOn42nGF7Spzx694Hmm2yNVQxjzB7mUpMo7Et5-UrGbO_e9jjznmW8e4u7_b3Hb1Aj7xqKSeFXvn5jnP8Sy9Tzb7OAkkT3hT7hckp8eZUV7N5kEZQiKf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ادای احترام مدودف، نمایندۀ ویژۀ رئیس‌جمهور روسیه، به رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446387" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446386">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=T69rcohYP1mPWXO_ozV7DPPzmw3cGgET1MTJih3dr8rm3GKqzJ31MZz3R-CLSDC5MKOs-uWGZuHooVFHTqm8lUY1fm7g2ahEf1Rgpv5mgHS9VIpmm-nAOFkCtKd2SUGNYsWFVUD5IYNWmWRnx19lh8mrJq5X9DMfpd-eM0089oaB5OLCP9JZGa8vleQ95GiHx7H7iTBj5j2nYjXAj4HTXhUkUn6CFB8-zIAgrDLkqzEP0VnIYqgBz825aGP0Pge9dUp8elwPiv_7jMqJCCo21x3FcsOh9EV5lHUaR9BuO4ih7Nz0Eb0eWRfWNqiTJC92BwLLhsVWwCZYsqofOvYMIa1LZpcsRNFFwBRtpmY3jn1kBD323aSvAYLPIPHd75wSCQ9wqUFuUC7asoQ1-nNYmfU4P6MGeVOjgE3ZuprHjXWDyNbytjGQE98UoMsgEPW1j_5M1S6XPEsBu6B4SviwmiHMFYXoqRzVI2Pk4kvVwunK8PMChLbUzDvxMrb04_l2U6lx-KsTh8EPOBnpNJl9zHAHU1bbMLTLzjU4mWBs-BQmA_NYo4NLC8SeJYayXEBX9WuK43gcKZAR3bcWEvcPXo8I1yZgL4VF-Z_91Rlb0FjFQseMNjQnEziwtZTj_9QHpwrgSLLJsPXTIli-9jEfe7pGxpMClmjArtMRb_Ol6uc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58817a5d50.mp4?token=T69rcohYP1mPWXO_ozV7DPPzmw3cGgET1MTJih3dr8rm3GKqzJ31MZz3R-CLSDC5MKOs-uWGZuHooVFHTqm8lUY1fm7g2ahEf1Rgpv5mgHS9VIpmm-nAOFkCtKd2SUGNYsWFVUD5IYNWmWRnx19lh8mrJq5X9DMfpd-eM0089oaB5OLCP9JZGa8vleQ95GiHx7H7iTBj5j2nYjXAj4HTXhUkUn6CFB8-zIAgrDLkqzEP0VnIYqgBz825aGP0Pge9dUp8elwPiv_7jMqJCCo21x3FcsOh9EV5lHUaR9BuO4ih7Nz0Eb0eWRfWNqiTJC92BwLLhsVWwCZYsqofOvYMIa1LZpcsRNFFwBRtpmY3jn1kBD323aSvAYLPIPHd75wSCQ9wqUFuUC7asoQ1-nNYmfU4P6MGeVOjgE3ZuprHjXWDyNbytjGQE98UoMsgEPW1j_5M1S6XPEsBu6B4SviwmiHMFYXoqRzVI2Pk4kvVwunK8PMChLbUzDvxMrb04_l2U6lx-KsTh8EPOBnpNJl9zHAHU1bbMLTLzjU4mWBs-BQmA_NYo4NLC8SeJYayXEBX9WuK43gcKZAR3bcWEvcPXo8I1yZgL4VF-Z_91Rlb0FjFQseMNjQnEziwtZTj_9QHpwrgSLLJsPXTIli-9jEfe7pGxpMClmjArtMRb_Ol6uc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: این وداع آغاز ورود ما به مأموریت جدید در مسیر تمدنی و رهبری سوم انقلاب است  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446386" target="_blank">📅 20:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=BVKs9IYN2mV_14eejJiA0Cm0O1ICkqt27T-2PrmpdW7aHeF8z_8Gcj_f1zhau1abip9wRgOGox2YYSYK2WK3Qp0cqVUhGZSSsXLeS3B8UjFCoDrH6RGpY4HdFkKKyW3ac8YVOiVpLxwb7smnwzyQsMWgA43eZC1anrkPyB2P_cYG09DA6BeLwJsAuXE7qbqlOj0oSosEsUriJFcgMjxal2QUdj_wp1-m1HfLLsKlBFKIr9JFNTwH8D_SkfPK8gyADMaIMpWfcAw6ureI5MtdI7wvWUlKTWDWDh9wO6w7JVLLK-V-AxhxaFkSZiRPgOGmXNb5yZgG-39ugrhRp0m1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d118f99fc.mp4?token=BVKs9IYN2mV_14eejJiA0Cm0O1ICkqt27T-2PrmpdW7aHeF8z_8Gcj_f1zhau1abip9wRgOGox2YYSYK2WK3Qp0cqVUhGZSSsXLeS3B8UjFCoDrH6RGpY4HdFkKKyW3ac8YVOiVpLxwb7smnwzyQsMWgA43eZC1anrkPyB2P_cYG09DA6BeLwJsAuXE7qbqlOj0oSosEsUriJFcgMjxal2QUdj_wp1-m1HfLLsKlBFKIr9JFNTwH8D_SkfPK8gyADMaIMpWfcAw6ureI5MtdI7wvWUlKTWDWDh9wO6w7JVLLK-V-AxhxaFkSZiRPgOGmXNb5yZgG-39ugrhRp0m1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: نسل به میدان آمده بدانند نباید از خون شهدای انقلاب گذشت و باید آماده اطاعت از آیت‌الله سید مجتبی خامنه‌ای باشیم  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446385" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=v8AXhU_QvLnD83Izi_TwBd8dSgRUcDm0LtL1_Cu7vhKQeKJFYVuvYZW0UigkBc7pOlVq1bPP-0gQxZPZSDLa2u3GLDqdc--fuBt__O4S3hbY2FwatPgBLsgdsWRVjtXzwvIg7gSspvsPN-dmNB1SyHQQ6sOZkCrt8o_-fr7TqafzuYg-axHiN3Z0vNiuNdnlhvbGpjnGBdxY3RMhimW56lr6xqxUQ7z7uXp1sF_ZzD5-TD7yUptKA6JM5TAJAO_l38vfN4_6amjviIpOReSkRMsoKHPmQ6TjHT4q6N0NxvrjWJGNlZXYzyXHIjjhexT1rNnxCyiE27gu0qARbXG7gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec73618ea5.mp4?token=v8AXhU_QvLnD83Izi_TwBd8dSgRUcDm0LtL1_Cu7vhKQeKJFYVuvYZW0UigkBc7pOlVq1bPP-0gQxZPZSDLa2u3GLDqdc--fuBt__O4S3hbY2FwatPgBLsgdsWRVjtXzwvIg7gSspvsPN-dmNB1SyHQQ6sOZkCrt8o_-fr7TqafzuYg-axHiN3Z0vNiuNdnlhvbGpjnGBdxY3RMhimW56lr6xqxUQ7z7uXp1sF_ZzD5-TD7yUptKA6JM5TAJAO_l38vfN4_6amjviIpOReSkRMsoKHPmQ6TjHT4q6N0NxvrjWJGNlZXYzyXHIjjhexT1rNnxCyiE27gu0qARbXG7gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: نسل به میدان آمده بدانند نباید از خون شهدای انقلاب گذشت و باید آماده اطاعت از آیت‌الله سید مجتبی خامنه‌ای باشیم
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446384" target="_blank">📅 20:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu_17sljRJMxiAqagH4nCwq7rDA7iCls9CQTcN0HZaxIrcQkuqyAcGlkoRJkngbHfTjsKyVV1BUsj_vhZjP-397NfOevNM3Er2BCrcJtc344tuxeAo0x6iCq6kTqr-nlfi-nJM1VQCaxV3mw2NSLvldAXJ4gHm3Vq4vCfXoZzQkKwP-67bO6O-vD35ZSdNeI9ZA5j4rTIKlm4KnPOHN8-lJd9KPYokSghPnBKWSCE9pxLVk2zfdsYfceJnoDA_BPxZAsjdqGVaic9r_kqzJcysdU5OHjud3_0czqDUY7g0EQh2i-WaA_a7sW_y5O9vHQIZ9DKx660T4Wf7A8On1VDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان در جایگاه مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446383" target="_blank">📅 20:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d2988441.mp4?token=BSnHHoQHTaF1_MnCbexC3JcohB7UjLzyo92X-QFoY7UcFklIKK7US3FlxK3USFI7EFaawgrz3xYmLZaK2sd1jOuG6wG808_e1WHVLKPSTqvJryf1dqQaC5sQm0V9sWy-ge0iWvkws_diBtoO7IG8EZw-hYK80D5SKHIbluxhbyaja30e0TTuruQiU6LBZKj9qu5MrWkNFs6yN_M9mp5XmBgYRZPWceyMSfqlUuD83pecQTh3QVlB1N5lw4ssKzcMhEKdy_hvvC-cb6oWRzT3a7EYYU2PiWgMScyUnbDZ2g-XmgEL_p890Jo9VGpM2kHCyo0NdSADoUHx44rag_dPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d2988441.mp4?token=BSnHHoQHTaF1_MnCbexC3JcohB7UjLzyo92X-QFoY7UcFklIKK7US3FlxK3USFI7EFaawgrz3xYmLZaK2sd1jOuG6wG808_e1WHVLKPSTqvJryf1dqQaC5sQm0V9sWy-ge0iWvkws_diBtoO7IG8EZw-hYK80D5SKHIbluxhbyaja30e0TTuruQiU6LBZKj9qu5MrWkNFs6yN_M9mp5XmBgYRZPWceyMSfqlUuD83pecQTh3QVlB1N5lw4ssKzcMhEKdy_hvvC-cb6oWRzT3a7EYYU2PiWgMScyUnbDZ2g-XmgEL_p890Jo9VGpM2kHCyo0NdSADoUHx44rag_dPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد تشییع و وداع با رهبر شهید انقلاب: درهای مصلای تهران فردا از ساعت ۶ صبح به روی مردم باز خواهد شد
🔹
در صورت فراهم‌شدن امکان بازگشایی درهای مصلی از امشب، اطلاع‌رسانی لازم در این مورد انجام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446382" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2abe920c.mp4?token=jpzBDlSnRlp43lp0JacE_6JBjpmGBUyZq4EGpuyjbbKcTrd3qFQZer62wiBQ2KDs7TXil5JEqdovw85IlP37qYBUro5MiujuP_fb6XQKOdVmcFEl8pS_JCK9QCNsBN75RbbdBkfcBeF9xOzW1r0sCOlM03QO7HE9R0FZDmj2gHzWGwNaxNEptTGo_b3bzF7YOYzzO1-Cs1UbO9oaty4SlygmlR9FIhl_YwO2y7GtbZ5UX236fWZimGhiwj6PL6ydILE8IFPSWFDlSaiFTmV-2NosqJHvailzYVB6VIQJRRaggCc4Q-xAlTL1olV1Fp7WDz0MWU2TNK3pKfC5O-FIeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2abe920c.mp4?token=jpzBDlSnRlp43lp0JacE_6JBjpmGBUyZq4EGpuyjbbKcTrd3qFQZer62wiBQ2KDs7TXil5JEqdovw85IlP37qYBUro5MiujuP_fb6XQKOdVmcFEl8pS_JCK9QCNsBN75RbbdBkfcBeF9xOzW1r0sCOlM03QO7HE9R0FZDmj2gHzWGwNaxNEptTGo_b3bzF7YOYzzO1-Cs1UbO9oaty4SlygmlR9FIhl_YwO2y7GtbZ5UX236fWZimGhiwj6PL6ydILE8IFPSWFDlSaiFTmV-2NosqJHvailzYVB6VIQJRRaggCc4Q-xAlTL1olV1Fp7WDz0MWU2TNK3pKfC5O-FIeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جای آقای امام رضایی در گوشه‌ گوشۀ حرم خالی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446381" target="_blank">📅 19:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۴.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/farsna/446379" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۳.pdf</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446379" target="_blank">📅 19:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzIFuT8-CNTnGMp8LdqRmyf6rF36Ib3sRzWoSygpt1U_ErcUAJtmK43kPdjQeOIMOqNVztPVqZ2Ss03zn13DWu7fW77BIgKkGo_EGxEh_1NGf9150Kel1Vlpa4PbsNx-22fwbNSo_SojvSzbGH_SFdUH6ckYot87eNwEqv8CASSFTZXMZ6Du_ZX1f1RszDZcph0YZMpJD8GQa7YFaRCqqOd27CYjJCzGbJQvIeH8AYsApQ5dyEiFmlo6hoV3XWnfhkBrIHrTAbeqVtGFByHPmeQgSlDOMKql12PjSO-yWhMVQyWkdv-elQMVd5CTBNuf3VdEByfMJx_gORZCorgwgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوت از عراقچی برای شرکت در نشست آتی سازمان همکاری شانگهای
🔹
دبیرکل سازمان همکاری‌ شانگهای در دیدار با عراقچی در تهران از وزیر امور خارجه ایران برای شرکت در نشست آتی وزرای خارجۀ این سازمان دعوت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446378" target="_blank">📅 19:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پلیس فتا: فریب اخبار جعلی دربارۀ مراسم تشییع را نخورید
🔹
رئیس پلیس فتا: دشمن با انتشار اخبار جعلی به نام برخی مسئولان و رسانه‌های معتبر خارجی، در تلاش است فضای مراسم را ناامن جلوه دهد و آرامش روانی مردم را برهم بزند.
🔹
از مردم می‌خواهیم به پیام‌های ناشناس، اخبار غیرموثق و محتواهای مشکوک در شبکه‌های اجتماعی اعتماد نکنند و از بازنشر آن‌ها خودداری کنند.
🔹
تنها مراجع معتبر برای اطلاع از مسیرها، زمان‌بندی و اطلاعیه‌های مراسم، رسانه ملی و خبرگزاری‌های رسمی هستند.
🔹
مردم در صورت مشاهدۀ اخبار جعلی یا محتوای مشکوک، موضوع را از طریق شمارۀ ۰۹۶۳۸۰ یا وب‌سایت رسمی پلیس فتا گزارش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/446377" target="_blank">📅 19:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4820db050.mp4?token=aXd4mRiFnTOgmxxYElZthuU7lv_fjvno_-oRr8SurmXepc-NVVU0gxiHAq39OLw1eF4j6OA9aOwe8ujhIaWf5o4k_ofTPMBpD7a07dNcTMVXmnVxUfHE4YUZUQuPxpAaR2_s-Vh7Y-9H0ujby48eT2EDmL1xre2-tptG95oiKYE8wCBqjqEobJ_NAKtmFne11_r6knO6LmJFrVL0dcQ_bLmGfjHbqtso_mzNKdsEDfY-VJoDiSZrrH5kwew0lINLhbYsPZAmyIgkyl8bVdcgTyp5ZIVZ694srJ0j2Fk1mE02OMEw8J3SCSqyELGL1lork8xITWWTaqIpwrT5eDusd0FLsSmnByfj9FMwjSZqzpQYPPTvhRny71Z5ZZ37TMqtcVhjy7ydMazYzoOy9rPcnfh2ujU0u5anYnykKlyplrvR-nuzBRpiZcMPRZBfp8Ie0qEA8_BiqM-nlinnqvmbYJhZGuENUSqKmn52cse8T7WnXE5PXAOKLBcTfhc9KcwRJYtVA0FsxDhhUNoY17dhE-gdj3kK-2oJYGDwUfAaT2R6PPld928cittsWJWyMvTzttL9FMqTZv5u4xAt1VBeEJfYeU1tFXHWPzg2xCcxaLmpmPHp8k7_slctn9CR7SbQ0YYqkYmlIHQs_c1XejVNj6HhtcdbyCsQPqrBhnT_svA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4820db050.mp4?token=aXd4mRiFnTOgmxxYElZthuU7lv_fjvno_-oRr8SurmXepc-NVVU0gxiHAq39OLw1eF4j6OA9aOwe8ujhIaWf5o4k_ofTPMBpD7a07dNcTMVXmnVxUfHE4YUZUQuPxpAaR2_s-Vh7Y-9H0ujby48eT2EDmL1xre2-tptG95oiKYE8wCBqjqEobJ_NAKtmFne11_r6knO6LmJFrVL0dcQ_bLmGfjHbqtso_mzNKdsEDfY-VJoDiSZrrH5kwew0lINLhbYsPZAmyIgkyl8bVdcgTyp5ZIVZ694srJ0j2Fk1mE02OMEw8J3SCSqyELGL1lork8xITWWTaqIpwrT5eDusd0FLsSmnByfj9FMwjSZqzpQYPPTvhRny71Z5ZZ37TMqtcVhjy7ydMazYzoOy9rPcnfh2ujU0u5anYnykKlyplrvR-nuzBRpiZcMPRZBfp8Ie0qEA8_BiqM-nlinnqvmbYJhZGuENUSqKmn52cse8T7WnXE5PXAOKLBcTfhc9KcwRJYtVA0FsxDhhUNoY17dhE-gdj3kK-2oJYGDwUfAaT2R6PPld928cittsWJWyMvTzttL9FMqTZv5u4xAt1VBeEJfYeU1tFXHWPzg2xCcxaLmpmPHp8k7_slctn9CR7SbQ0YYqkYmlIHQs_c1XejVNj6HhtcdbyCsQPqrBhnT_svA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با پیکر شهید مصباح الهدی باقری کنی داماد رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446376" target="_blank">📅 19:44 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
