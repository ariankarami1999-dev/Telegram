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
<img src="https://cdn4.telesco.pe/file/l_rNjXhrYZbu5XOE3gIhsPhAWeNltRfwC4ZOsisHc6xyeJchykqrEq0RoMpTEmoizxaDx1CQ-_u3nVtlMssVInApA5HAnWeoK0fQHGtJstIowpZdbbPtGnhfWg3ahC6ISF2045S0ZKvMIqA30qZXXbZLhfkZprxaJCWiV8di6Bi9dBkkEHbg2xFACtbWvJZi_K1L7gGAoj1mtBvvnpHFqVJjvzOuw5gAI6ZyBufZjNo-SJIWsFU2RBeL3v5D4kD1URonARqWARbxy_Kxs1BKM7YHkAIvnHHsyfMGDe2IR6jPZqnvE9lFOA7HB1INXm46HZIg4H2Zfu7WtMieah9l5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 22:25:00</div>
<hr>

<div class="tg-post" id="msg-449015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhs5EunX7oJ12BhR_mOqi7oLIJoZWLcVvfGU447CmhRaZ0EjKhSA9kmn7ENjLQRhTs5G28sz_4N1FIu_fcbnfVsQBk2rLugz8srBacdnKG-u0KnRGs94lIGIVCwczWmohWkfOxMkWpv4nAqLWFS2Poi2oA3Ox0-NDFNTxUybMn_CP4aD-aVCygvApeuxgjz9pvMwkkLOu0FYQ-Zw9RAybKMOy509dDAL5O54wOyMuYfVrJtvOIKNia2ElpLzgjbAVVfnJfcrxSvmn7iEN6bPz_d61gxNqYZ4nJzo4a5BfahnHG-rWBQyD2FkGI490V8nY60nWb5mK6J-FL2FV6Qvzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازهم در جهان موازی درخواست ایران برای مذاکره را پذیرفت!
🔹
رئیس‌جمهور آمریکا مدعی شد که ایران از دولت او خواسته مذاکرات ادامه پیدا کند.
🔹
او مدعی شد: «ما با مذاکره با ایران موافقت کردیم اما به صراحت اعلام کردیم که آتش‌بس پایان یافته است». @Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/449015" target="_blank">📅 22:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc24d831.mp4?token=ZVLA2Mm72_MNyYhlZh4f6MeXcwqlo3D3J_4VcIK3qnNSyuoFKEseHRDgfZkY-Ok0DRRmRqpt0KIPHe6EF6sjfK_s9pjq02sU7cfNQkD5KbAX-KY140lz2L2pEK2WHnnWMyetQTPQo-c3SSXaN_drih0Z49xqi9w7UfMVa1BoJbrjWXd-UpBoePUP9dxXIlqim8yR1KnG8XEwNl_WBaOvlxhdza0sc03mGPM0kQF34RJfvOB13wiyq_t5Sj7x15p0iPkZ_jONIb2FnHPxlDdfK369SCbGqK68SSEVPCneafKgGQl1-K1jL5qYGmBNTf3WvfHDQMBPSOkBZIC4lANCOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc24d831.mp4?token=ZVLA2Mm72_MNyYhlZh4f6MeXcwqlo3D3J_4VcIK3qnNSyuoFKEseHRDgfZkY-Ok0DRRmRqpt0KIPHe6EF6sjfK_s9pjq02sU7cfNQkD5KbAX-KY140lz2L2pEK2WHnnWMyetQTPQo-c3SSXaN_drih0Z49xqi9w7UfMVa1BoJbrjWXd-UpBoePUP9dxXIlqim8yR1KnG8XEwNl_WBaOvlxhdza0sc03mGPM0kQF34RJfvOB13wiyq_t5Sj7x15p0iPkZ_jONIb2FnHPxlDdfK369SCbGqK68SSEVPCneafKgGQl1-K1jL5qYGmBNTf3WvfHDQMBPSOkBZIC4lANCOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای منتظرانت، صدای خونخواهی‌ است...
@Farsna</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/farsna/449014" target="_blank">📅 22:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58dcb9d425.mp4?token=OX7taRwoDSq06vs1zLzpEBKF0kPBCjTKU1_v2nOttK5RLENxyeRAxg5BT2YkLWr73xTG5Xf482383Ol-fu0qU-ZAnWRYouynfElv9UnRSYgXNlMwCEYlz90jo0muaTvLPSDj-Qqgd23lnTFL6xx_u7Ow6g6BM4bcqfylFyeU4o-m1p6bOMoA7W1a2Ug4Z9IGQhsE6H4g_xvt_ihakGcXftnn-8MMCuKSQ8s7XBJtt9OZ_hGnmNTe345yl62dt6rtM2OFqc_S4PjoMrFWfCVz_dgcQDK8j-i9wXHj7i_N-BJlJeCJop64aWU_ZbrR3ip-ocHxTBHFA2GIqkSEAL5XMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58dcb9d425.mp4?token=OX7taRwoDSq06vs1zLzpEBKF0kPBCjTKU1_v2nOttK5RLENxyeRAxg5BT2YkLWr73xTG5Xf482383Ol-fu0qU-ZAnWRYouynfElv9UnRSYgXNlMwCEYlz90jo0muaTvLPSDj-Qqgd23lnTFL6xx_u7Ow6g6BM4bcqfylFyeU4o-m1p6bOMoA7W1a2Ug4Z9IGQhsE6H4g_xvt_ihakGcXftnn-8MMCuKSQ8s7XBJtt9OZ_hGnmNTe345yl62dt6rtM2OFqc_S4PjoMrFWfCVz_dgcQDK8j-i9wXHj7i_N-BJlJeCJop64aWU_ZbrR3ip-ocHxTBHFA2GIqkSEAL5XMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: تا وقتی که رهبری معظم انقلاب در مورد پایان تجمعات چیزی نگویند، تجمعات خیابانی ادامه خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/449013" target="_blank">📅 22:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1eb35161a.mp4?token=aSp1D8XNZHgE1CHbULxPevIxeHaJxINlTFCfvuLVJZ4LknfbiJmEqjSn5tVLdlOBxZeCLDXu9yldsduMtxA5ZlhW8pf4uLEa6D0gHrPpY06zwkayPx7Eh7FWkvPrKmDUKzQfBlrxK46o4kUbd-hr5P7P2lOVqKgddaw2w0wRfLHSHQ0bkgFG8FJjo2Nx-OUYrb9xc3zfv4IUv20WL-pN4obACENyCpk0SjJvDRjs80fjlk_RlK6sO_rs9Ej2-K-NHCCDI_gHo3sha2ZZDLw1vhZo9FTO-eAprhlNRth3wNZxAW-bWbHQXrnJactUUm3BxN-QkKRsDYwcNZEdrxMppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1eb35161a.mp4?token=aSp1D8XNZHgE1CHbULxPevIxeHaJxINlTFCfvuLVJZ4LknfbiJmEqjSn5tVLdlOBxZeCLDXu9yldsduMtxA5ZlhW8pf4uLEa6D0gHrPpY06zwkayPx7Eh7FWkvPrKmDUKzQfBlrxK46o4kUbd-hr5P7P2lOVqKgddaw2w0wRfLHSHQ0bkgFG8FJjo2Nx-OUYrb9xc3zfv4IUv20WL-pN4obACENyCpk0SjJvDRjs80fjlk_RlK6sO_rs9Ej2-K-NHCCDI_gHo3sha2ZZDLw1vhZo9FTO-eAprhlNRth3wNZxAW-bWbHQXrnJactUUm3BxN-QkKRsDYwcNZEdrxMppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت دست‌نوشته عاشقانه رهبر شهید انقلاب در وصف امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/farsna/449012" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20077aff3.mp4?token=Yb-AyW-83jZ3-xTFHka8qG6mfavwgd9b7Ir7R5_JV6o68bpMv4mJ8WZT24V28dH_nY_NX-c6ueBJZKIqZ20wqb-7ZoliK9K6Y4zjx--HR-F_BUnzcecCvib_fFqc-QRhYCfupP4h8YA0Adh6_lwjZp7EmO9WgX28LQ3WQxPvWzCEAqr9_PS3Nfaz2ALTDaSeJdHBsOS6cqSbvRg22NSFXXnz0IMJ34fzC342zb24esms_f-PaBFJCgTAADs7Di-MUDb8z66ZtxFYQtV97BJPjFhnnYemk6-9XcdMrgSwDcgD2rI3IrEztQAeVA5bYkk_dQImAXCeZVANz-8qdldamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20077aff3.mp4?token=Yb-AyW-83jZ3-xTFHka8qG6mfavwgd9b7Ir7R5_JV6o68bpMv4mJ8WZT24V28dH_nY_NX-c6ueBJZKIqZ20wqb-7ZoliK9K6Y4zjx--HR-F_BUnzcecCvib_fFqc-QRhYCfupP4h8YA0Adh6_lwjZp7EmO9WgX28LQ3WQxPvWzCEAqr9_PS3Nfaz2ALTDaSeJdHBsOS6cqSbvRg22NSFXXnz0IMJ34fzC342zb24esms_f-PaBFJCgTAADs7Di-MUDb8z66ZtxFYQtV97BJPjFhnnYemk6-9XcdMrgSwDcgD2rI3IrEztQAeVA5bYkk_dQImAXCeZVANz-8qdldamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: مشکل ما با آمریکا از زمان کودتای ۲۸ مرداد آغاز شد و الان ما با آمریکا پدرکشتگی پیدا کرده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/449011" target="_blank">📅 22:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b1283110.mp4?token=TXpugDeMq0_3TLRk0fuKW23VUMXCHGgUQoIuyXOZSQMD1_bJ9jkxR56EbnITNc2fhat7GES5K9RKQnTeMSAipEW-IZUlG6xhzzuYeRFe3gU22JGjfFClYowINX9o34f5goEwleLfQq2m8sFAfi_1qfgklzGqFwxDoQAYnPn95aqed0TF1kUnpgzpryrfrrIpxLp8m-_IKCei2vzDYem2Zlevs75XY2J9lwGLMm_TcWacKRn_GRFmF1s53MhOZMoU8s4rrQqXGZFlMTjWtf-oLPmtv7Lexuivpb5yh__rP4sR1eoqYvKLv6btgaU2P6H69uFy8KuDUifNqECUeiwIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b1283110.mp4?token=TXpugDeMq0_3TLRk0fuKW23VUMXCHGgUQoIuyXOZSQMD1_bJ9jkxR56EbnITNc2fhat7GES5K9RKQnTeMSAipEW-IZUlG6xhzzuYeRFe3gU22JGjfFClYowINX9o34f5goEwleLfQq2m8sFAfi_1qfgklzGqFwxDoQAYnPn95aqed0TF1kUnpgzpryrfrrIpxLp8m-_IKCei2vzDYem2Zlevs75XY2J9lwGLMm_TcWacKRn_GRFmF1s53MhOZMoU8s4rrQqXGZFlMTjWtf-oLPmtv7Lexuivpb5yh__rP4sR1eoqYvKLv6btgaU2P6H69uFy8KuDUifNqECUeiwIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: هرکس بخواهد مذاکره کند برای اینکه با آمریکا به صلح برسد او خائن است
🔹
هرکس پیام دوستی به آمریکا بفرستد دهانش خبیث و نجس است. @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/449010" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">آمریکا تحریم‌های جدیدی علیه ایران اعمال کرد
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا اعلام کرد اسامی ۸ فرد و ۶ شرکت را در فهرست تحریم‌های مرتبط با ایران قرار داده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/449009" target="_blank">📅 22:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9575683bac.mp4?token=dxeWTA8RVfRT0AtKW-iW9asomIyTkwE5RPd8hPvz3C3XLIay2MSQapGohKQ0k5YCDBLBwB1gZy04ld_FgvPoZ9bdbPy5zlegKmoQiz8R2ysWZTBDJU-HG0uXTjo-EYFk9625kkJD8GInyWwZy6pOF1gmEbVA4gJZWkhKiagdCjhhbJeH5fZE3_5N7hFw0M5fPb5TCXXU2Bi2mXmetROH_b8L_6kvQz0AoXMZpJ25gIHjdBI8CDlbHtpW3lUMtSqfYobABuevAg9dOsU-SgLqgJSM8PHhYsEqTvM72OO_cJ6Lpa-Er8xOofymtJcMA38flc59p4x7juR2Vv27blunqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9575683bac.mp4?token=dxeWTA8RVfRT0AtKW-iW9asomIyTkwE5RPd8hPvz3C3XLIay2MSQapGohKQ0k5YCDBLBwB1gZy04ld_FgvPoZ9bdbPy5zlegKmoQiz8R2ysWZTBDJU-HG0uXTjo-EYFk9625kkJD8GInyWwZy6pOF1gmEbVA4gJZWkhKiagdCjhhbJeH5fZE3_5N7hFw0M5fPb5TCXXU2Bi2mXmetROH_b8L_6kvQz0AoXMZpJ25gIHjdBI8CDlbHtpW3lUMtSqfYobABuevAg9dOsU-SgLqgJSM8PHhYsEqTvM72OO_cJ6Lpa-Er8xOofymtJcMA38flc59p4x7juR2Vv27blunqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: برخی می‌گویند جنگ را ادامه دهید که جمهوری‌خواهان در انتخابات شکست بخورند
🔹
یعنی ما برای اینکه یک سگ زرد برود و شغال بیاید بجنگیم؟ ترامپ برود که چه کسی بیاید جایش؟ ما هم به دموکرات‌ها می‌گوییم مرگ و هم به جمهوری‌خواهان.
🔹
مگر می‌شود که امام…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/449008" target="_blank">📅 22:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16ec0d64f.mp4?token=PFw-a2FZNLMFg4cHKxiblUhCy9GvO4FIO8_uqfvm3lEsZge30wK7xBWCAJpZPQZP9-RW1zQ35Psr9NVILbVGDQs7eupoqUsWa9iGJrmrKpftRCEKipw2lpP9Wp61_EGHLwv7ovrhBT3bb7eMLjSGT9iCdtLnEZV0l5uEnbsFNWAMmYDWxfa171BYpRRMYzDAJ3KhV89xyqm3NO4hV7Bds2-PMvRfd4vIK4mVAGPdfDfznaAZxkPXpxifJTg3edwZDW80vgyFakDv_NUhFPcN1F1aYbkRC9mG64ByJXnyWsooiiGtmy3ELa1XDBkBT6nufa_qpd5EgPBG7vJYwK04oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16ec0d64f.mp4?token=PFw-a2FZNLMFg4cHKxiblUhCy9GvO4FIO8_uqfvm3lEsZge30wK7xBWCAJpZPQZP9-RW1zQ35Psr9NVILbVGDQs7eupoqUsWa9iGJrmrKpftRCEKipw2lpP9Wp61_EGHLwv7ovrhBT3bb7eMLjSGT9iCdtLnEZV0l5uEnbsFNWAMmYDWxfa171BYpRRMYzDAJ3KhV89xyqm3NO4hV7Bds2-PMvRfd4vIK4mVAGPdfDfznaAZxkPXpxifJTg3edwZDW80vgyFakDv_NUhFPcN1F1aYbkRC9mG64ByJXnyWsooiiGtmy3ELa1XDBkBT6nufa_qpd5EgPBG7vJYwK04oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: کسانی‌که از جنگ می‌ترسیدند فهمیدند که جنگ هزینه و مشکل دارد اما ترس ندارد؛ ترس از جنگ بدتر از خود جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/449007" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ادعای رویترز: تیم مذاکره‌کننده قطر در تهران حضور دارد
🔹
رویترز به‌نقل از یک منبع آگاه مدعی شد هیئت مذاکره‌کننده قطر در تهران با مقامات ایرانی دیدار کرده است.
🔹
به ادعای این منبع، هدف این سفر کاهش تنش‌ها و فراهم‌کردن زمینه ازسرگیری مذاکرات ایران و آمریکا با…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/449006" target="_blank">📅 21:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1cb9a4ea.mp4?token=SbOn3ec4f3V8jYe2shRLJJLAhBketdwAYZ95qsDrH1s3PU--tRqsIFmO5Yn_aBk6GyBQ0OZNzXrM3roamAvUOdNJ0SHPENsXA5tDiQ7JEwz5WFhnLieRummh6U87WUE4LzXxCu4MPd_lFj02ceVc2qESXM9kBAEqcwtJex06Pr4auHdh23czqzkQ5MDED5NBIeHkZGi8UU3ImnoIUJMRZOb9Cf-bOwFejzGNxOEmOAwEdd9k-1_qtjFoyj6EWTjcI71nBk4EffSKzXVWnrjawUC7J9-SVHBOBKpXb36WxyZO7blQQKoC-jxmLvbrxs1tliYPdses4VmnmpQOOFp0Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1cb9a4ea.mp4?token=SbOn3ec4f3V8jYe2shRLJJLAhBketdwAYZ95qsDrH1s3PU--tRqsIFmO5Yn_aBk6GyBQ0OZNzXrM3roamAvUOdNJ0SHPENsXA5tDiQ7JEwz5WFhnLieRummh6U87WUE4LzXxCu4MPd_lFj02ceVc2qESXM9kBAEqcwtJex06Pr4auHdh23czqzkQ5MDED5NBIeHkZGi8UU3ImnoIUJMRZOb9Cf-bOwFejzGNxOEmOAwEdd9k-1_qtjFoyj6EWTjcI71nBk4EffSKzXVWnrjawUC7J9-SVHBOBKpXb36WxyZO7blQQKoC-jxmLvbrxs1tliYPdses4VmnmpQOOFp0Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: گفتنِ احمق به ترامپ، فحش نیست؛ این صفت اوست.  @Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/449005" target="_blank">📅 21:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f81f965a.mp4?token=Xqdzpk0WDszHo7gdpyH60ReGNm0aF-ieU4xbzScpzs8EnZLQVmEKRR84yUQHW4GjfROeZH1lCEzqW7mToXrPPmCkh9ZkNTi55I9KL-X5g7tBwOeO5wcj8clxBCnxXGt12-Q2eZgiFYUwjo7NWZ792e25-bgV57qeR3_plr9VTiDvHscMmRXj0g_W7jGRKc7CWB_6RJxsBJWEFC9H8Dd36P_IrgWLKRQTt9DrtO1TRkB9otuBATdq5KqJHlBHRNLc9ivPIn_cmQByteDJ4C49ip6n4WvUUtmKgaH85hVCcnW1lZe3Z5Bma2YqXgSqfmDZraPnAXAVSEjD3hltzvK9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f81f965a.mp4?token=Xqdzpk0WDszHo7gdpyH60ReGNm0aF-ieU4xbzScpzs8EnZLQVmEKRR84yUQHW4GjfROeZH1lCEzqW7mToXrPPmCkh9ZkNTi55I9KL-X5g7tBwOeO5wcj8clxBCnxXGt12-Q2eZgiFYUwjo7NWZ792e25-bgV57qeR3_plr9VTiDvHscMmRXj0g_W7jGRKc7CWB_6RJxsBJWEFC9H8Dd36P_IrgWLKRQTt9DrtO1TRkB9otuBATdq5KqJHlBHRNLc9ivPIn_cmQByteDJ4C49ip6n4WvUUtmKgaH85hVCcnW1lZe3Z5Bma2YqXgSqfmDZraPnAXAVSEjD3hltzvK9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند.  @Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/449004" target="_blank">📅 21:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=upXKhJ1PN99BRvSc-wMjv4og9Mk9ZHFW5gO8gUnYtvY2FvutBjuXa96fJF8l7FPNfF1PrlwdcLTtMtGlkfgK8XQh3VKKYQ3MHBa3fId-LA1smlqkBYzV8t20OCCX4WL4xh7hdkhJUG3lvQyWNzMQvxMwuAL658e1nf6i9YdLSvbbFTi8QYVRqTz7drmz4se7z4DwxJaCTGAk-S8I7Sf1Hx9_Ps-EoEUlX1Mv9XKxdEyVTNzOa_9FL-imzwWghpXeGSXG0HdNW83CVJJy8q1dfI-c_nc-oapWgY2Hrni_fefJ2PNgHDsw_NZGwnymBihFnjS-XxhCm_bOI-vW-z5cmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14cfb7b2f7.mp4?token=upXKhJ1PN99BRvSc-wMjv4og9Mk9ZHFW5gO8gUnYtvY2FvutBjuXa96fJF8l7FPNfF1PrlwdcLTtMtGlkfgK8XQh3VKKYQ3MHBa3fId-LA1smlqkBYzV8t20OCCX4WL4xh7hdkhJUG3lvQyWNzMQvxMwuAL658e1nf6i9YdLSvbbFTi8QYVRqTz7drmz4se7z4DwxJaCTGAk-S8I7Sf1Hx9_Ps-EoEUlX1Mv9XKxdEyVTNzOa_9FL-imzwWghpXeGSXG0HdNW83CVJJy8q1dfI-c_nc-oapWgY2Hrni_fefJ2PNgHDsw_NZGwnymBihFnjS-XxhCm_bOI-vW-z5cmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سید علی خمینی: آن مسئولی که بخوابد و در فکر انتقام رهبر شهید نباشد، باید به وجدان خودش شک کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449003" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0jPB1z0YPMGu7veKKOLJVqVz-jwMG-Kg9IE8HMbxYJBkSxwELxTJgY_-an_ZWuVkN_LqxSYVXU42Qcq3YEGcNH_-Qw4v-XHzDvCFiXYR5msRoEmjoCalDKXQZfMHjHlBxR025SyfOm_0zjDHA0zJfiZLVRjsnaR6E8r3I0CD9Gi00GQowpPh9vWa4s5IMJ3NBF3HBFWpJSXUrLME_goFYCwu9W_F3_cKujtsOuYHLvlR9cf8wyMwII7B-a-_wNEr86RheM6x6bIfEvH6mcetcYmV_9vkeSZ6ZA1LZ2KFQnZaTk0y1IGtk0lJ2zalHxx2J0vaJpWcea-LVJ2JuCWkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آثار فرزندان سیدحسن نصرالله برای رهبر شهید
🔹
گروهی از هنرمندان لبنانی برای شرکت در مراسم تشییع رهبر شهید و خلق آثاری با محوریت ایشان، مدتی را در ایران سپری کردند و آثار متعددی نیز تولید کردند.
🔹
این گروه با عنوان «پسران حسین» ابتدا راهی تهران و سپس مشهد شدند تا در مراسم تشییع و تدفین پیکر مطهر رهبر شهید نیز حضور داشته باشند.
🔹
اکنون علی نجدی، یکی از اعضای این گروه که در مقطع جنگ رمضان با آثار هنری خود درباره ترامپ در فضای هنری ایران شناخته و مطرح شد، تعدادی از آثار تولیدشده خود و دیگر اعضای گروه را برای خبرگزاری فارس ارسال کرده است؛ آثاری از تمارا فحص، احمد الحاج و علی الرز که در ادامه
اینجا
مشاهده می‌کنید.
@Farsnart</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/449002" target="_blank">📅 21:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قالیباف: درگیری با آمریکا هرگز با تسلیم ایران تمام نمی‌شود
🔹
از دید من کسانی می‌توانند با آمریکا مذاکره کنند که آماده جنگ باشند.
🔹
در مذاکرات به معاون رئیس‌جمهور آمریکا تفهیم کردم که ما هیچ اعتمادی به شما نداریم
🔹
ما هرگز دست از آمادگی برای دفاع از کشورمان برنداشتیم و هرلحظه آمریکایی‌ها به تفاهم خیانت کنند ما آماده دفاع تمام عیار هستیم و قاطعانه مقابل آن‌ها می ایستیم و حق ملت ایران را می‌گیریم.
🔹
آن‌ها طعم قدرت و آمادگی نظامی ایران را چشیده‌اند و می‌دانند که ما یقه آمریکا را رها نمی کنیم.
🔹
پایان جنگ برای کشورهای دنیا اولویت است اما همه باید بدانند که این درگیری هرگز با تسلیم ایران پایان نخواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/449001" target="_blank">📅 21:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdYKAhOvlE1sdLa2_X1oIEcmdOIKKNx9p7Ml-uR0goLSgZSDKKJNiuQ__yBRkX3hitm8DZlR6xRDNv4XbxhtMvZoSEn0pqP-AbC5Xsfbo9QgY9nRaWrYdr7LwNMDEbqZicqKNwUVQv2DpmiMBIVFzH0maK6R9LOsuTV5jyilh2G0Ag7a9eBJCNXqb8T-JryX9sg0WWg5W74obEqxfWy0iDa-IhMbLy0u5ubkxKiPKSljilkp0WhhK9IxjSdBL8drcCHMbv3F4tBw2bbrhEUOEoMfgUwYMh9ulywpJLMGStTsHaGgZWANE4u5iZ23O2LYy7_hPuSNzJWxoUFRj3v9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtdqYuB88TrCTLZ1mxaYNcFWdOJ3ePj5Skhd9WkdQwbFTUoqg3EnatCjZZuXWjl7Xht4E_1_tE0RuSQcu1ItmbIR0I_pMU9K2LgWsmrc1JX9-rXBvAK4PAP5ZzAq3gtefp6DTRx5dshNK0RJNAOhZXJm1_zjzdgwA1MCVXyIokN0ZLl0ceqB8V6oZmdHbF4RMoqHyt7rLtU7jQ0XGPo3XK0lCc0HnUx-Hm3TpcqhvMJckIvjMvuLAZZQQAP9QSs0HeZ85i4fdHpIlKZnvFg0psLZAU7K8BU9uYYsuiQZDsm8nAGIDNR-s1lMbM2TLFZ_5TMElOSrJkCfevZV7-4w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9MbLr6Dh1nKmENokxOk8Nz2_WyjNz43cDxNFl4NZtsjBoca2_zq2SEwdFCedtAjjlMH3GInATGHf1wSDvb9HjUYYZAY46HbTK-jdQNiO7fHDMyHj8yMZ-wuQohETIAKxDAtU_7wRjCFH1aYULP6WnyMJxtVRQuTQjQS-evMG5Xj3b4gyCc5xdq0u4n7MWhKaNYVfLI04wd5DD__AuTj_cznl6leTGHtxAYDi2562YUBR4IrUQPCvRZmbD2BgeKuF62q24UIgMJkUjkNk8OFqECNmt05WuQwmH5diIFaZ1WLXlvy39ZkLUWVmZsJIIolzkLvs0ZMz6GT9kUECgJWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JR9z7DK2_uQKEB4q0920h5C-3sxD2z58i_WygopF75fpJt_Tc163RVHWS7-tF-BJV9nz78oLI1x9aT3tTUUWxSPyEAc54KhLUBX_2koVGf0klRx_D6p_9Dg3ryIdiiGrUVsptS0JPVNiKkhUH-igff3jIzPw5LJoUDaM7WUtWPTNc6fq36O1fXJyfUUtAAL2Tlzo6IyyiOU2sMzWbQ4e3yxKKrBWhCeuFr29Dcy8B-gVQh-pBl2rbRH2VY8IJaHqKewUEGi1I-hP859rC9RMwYv3-JfKRcPmxqh2oRaOM5FcIWjvFXgFJ2wnMJ11-7YAkfM1jV_QT4Cg5VwjZF7Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCGNQbHqGn-VK6Fy0m58Skpcr5jc8la3h_mgfx_e_kEj8Rem60gYlQfx-UB6HG30wXGPKdukuAhR_kaAapwR83Q_k1Br6gVF_P2cAwUCwxRK5DQpAmvriqBrR0zpecmJxVnBYePFudNN3xjeXOMThaCHpRcC9Hqe-eadE4-n9Z-AnZcg3HahsYPX1RIjqKzTpudEeDw8ZxAx7wJuMkgyv2BioJQP2jZ_yEBAThGKvCvlLieMAEda5pz3y1_OQqTK8xXvPjkSX0eHVI8_aKJ8tZE0UADiZ3IAosmEXoTgLHNqWmNl2rdY-wewt93W8k6Zy5NmzgYTk18av2FYGGgCoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r5QdCHeIF3oUyaTNNr0Ll024cB0FY5yBmV0Rm7gVZzKAyY1N0WxEDwXHhF17zPISyHV-EqyseZJnZ8I_YRrYli0pLIMambLVol4W3KVcAcuPUSdn1SGBmEG0kB_SpvCoKNRtjrZxbMETvqpsLJ3s89bT2Q-pE3ITIpwsm4ABbM2enaNqr3SjRjby2lcXBafuMCXkMD82AceByZQJZyI2dtI-m_A8U_0YMkuTeJJKqlx0FlRmeQk2RCyadtKAM7LBNsXDcWwDRw5xxtec9wZfgy4j4dFvEeckrtF8N6KHAj4M3VQriHmXnyyof7fqlFNwHT-MluSUZWXldSFf9t-ebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diLq9PvSASKy7_98i3G9MtGET4JM8rgdodvnx1fKxo04QCcQUZxzaoQIj2IMjPmmWqenhYfiFhl11L4mvD_33g8S40SpFgxQv4IyFq8iWdaLRfcG75S3q3wHbX2h3eISfH6BvRZnOEdbdypSHERECB3hdUzUzEAPoKCCFHRvqYAez_t6rgPZzYw6XdVfeMQoFYK1c_KvqWhIh_LlVQCoCSjA3wuHDVJhKXIZFdf-HKmlZfhAFJn2vMH4Ror78ATyBelumOXbD47IQEjk5Jvj0TmLNaF8VCfQJGCgfYlnxLxiPs5Vyj0I14u8phahxkzl6qqYdWL2uOdbl0VT0rsVrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزار رهبر شهید میزبان حضور مردم شد
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448994" target="_blank">📅 20:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448993">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5222c635.mp4?token=GLRLS2xCgs7mccmmAb9isZ1TYbI9dpg3vec7JlLZg0Yy96TlMtNRl6R0vuzhSbpaR85uJcaE5tK4FapcS29o6e7mEp2PTBp7NMXOS1zJ6bvbzqgtKr_FxxGF5FbR2Kff-9xGSB-L5T5xOvUzABvKTBnMvFdk1jGSvOFjpAoQQAulgBPVyMXHR4gNH4iR4ymY3_CmDoeUJsU_3iRWZ-uBCYCtg6pCSPYPCqxNxH-yrrBSaLftjtkPFyymQsyL6bVK4vfxf2p0qxv-T87WHfnh3zr6gZuIOfEHhL4sHDJ1GjoVphRldEMRYVi0ti7kauqiDqDLCoWuQPizrxOA_h9YvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5222c635.mp4?token=GLRLS2xCgs7mccmmAb9isZ1TYbI9dpg3vec7JlLZg0Yy96TlMtNRl6R0vuzhSbpaR85uJcaE5tK4FapcS29o6e7mEp2PTBp7NMXOS1zJ6bvbzqgtKr_FxxGF5FbR2Kff-9xGSB-L5T5xOvUzABvKTBnMvFdk1jGSvOFjpAoQQAulgBPVyMXHR4gNH4iR4ymY3_CmDoeUJsU_3iRWZ-uBCYCtg6pCSPYPCqxNxH-yrrBSaLftjtkPFyymQsyL6bVK4vfxf2p0qxv-T87WHfnh3zr6gZuIOfEHhL4sHDJ1GjoVphRldEMRYVi0ti7kauqiDqDLCoWuQPizrxOA_h9YvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت زیارت امین‌الله در اولین شب پس از تدفین رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448993" target="_blank">📅 20:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448992">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiA63DaSts2dXYnYJiae8Cu4ciDyT0DF8tYhFlFqJQ1VYlF_GonEtLaWKLxHnC511Jrvfstqu1ubhVTYmKSedp7E4g35M0-hRf7fRFgSwVrjCLqu58LQ3i7YQ4y8YusyrZD49Amyjhm1b-9_pxML677UC5Tjc9QqrBtyfJsGxZkrGZ3oA1zgNXFug__m344k1FZZHD6XRYQ0IBYFYPqlBpJooM4c0LzjUPC2jgS7jNSjMSWz66OgWfo9R-1OmCS7Y6zEXgbC28RsdJp2_uAix6_MwDPcH86NSSPy1X4iZqqNu61DKGJk3fl_WQP9bA4M3jEKPmc5rRHbmbAMoyz_Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448992" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448991">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/448991" target="_blank">📅 20:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=XpMXlEd0mQFOgQXYsCrOG8X06vu1RhyD4SjVY4M8UzR5tUciHTvvhf0t69Blz0BraRvwSQ3ddiDsxXXY2CYPTWKTEZAYGDBz6W2w4cRnItllbyUiBjicKyI6g786wfyvu0bo4Qctpyk9MvQNUVH7Nk2VN2FVlpnpi7_8HilM7rC7bxhI0vnNWEoxnR9Qyd4tkJfH82IDt9X53CmBZyvVY-LFKVKskzNmApxX2UyZVUhBHvnYJciYpI4JbFjkwFiQXog9c9fOg8Y1K04nqPnS6b70ercLnyV4vFkV6s-6j5qwmpQcMcXdZMm94He6af3yjtDaK_SYq0TtwDe9KqapSx15bXXwEYYYThrVsDaaDpiGwROrUve4_9yllfvcVb6BfLu8X-bgKSN6cK9E0YzitSvuMcceWKUtomA2yi7GQM56mKI-hBNFMT_Ya6keI6-Y0p0gEdbhidk07kkDGMrbxK2gNK_Vovdv5NN93vIC0AbSy0O2hRpXffqb4g1yHDOfjLnsczedEFKvXx_wDo4R1Dd0cG527gl_Lie0ZXMxBE7x-oAU47tJY2Fy0kl0LifUIh0HrQwLwW70gbfw1S83QG7x_i1NV85CuHDbk0_9qZNABgS9tnN3jniUUolOUk2d2ywQJeuDj4ftPWaHj505Uv07iDSuMGeul1V0RAbzUEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ddc860633.mp4?token=XpMXlEd0mQFOgQXYsCrOG8X06vu1RhyD4SjVY4M8UzR5tUciHTvvhf0t69Blz0BraRvwSQ3ddiDsxXXY2CYPTWKTEZAYGDBz6W2w4cRnItllbyUiBjicKyI6g786wfyvu0bo4Qctpyk9MvQNUVH7Nk2VN2FVlpnpi7_8HilM7rC7bxhI0vnNWEoxnR9Qyd4tkJfH82IDt9X53CmBZyvVY-LFKVKskzNmApxX2UyZVUhBHvnYJciYpI4JbFjkwFiQXog9c9fOg8Y1K04nqPnS6b70ercLnyV4vFkV6s-6j5qwmpQcMcXdZMm94He6af3yjtDaK_SYq0TtwDe9KqapSx15bXXwEYYYThrVsDaaDpiGwROrUve4_9yllfvcVb6BfLu8X-bgKSN6cK9E0YzitSvuMcceWKUtomA2yi7GQM56mKI-hBNFMT_Ya6keI6-Y0p0gEdbhidk07kkDGMrbxK2gNK_Vovdv5NN93vIC0AbSy0O2hRpXffqb4g1yHDOfjLnsczedEFKvXx_wDo4R1Dd0cG527gl_Lie0ZXMxBE7x-oAU47tJY2Fy0kl0LifUIh0HrQwLwW70gbfw1S83QG7x_i1NV85CuHDbk0_9qZNABgS9tnN3jniUUolOUk2d2ywQJeuDj4ftPWaHj505Uv07iDSuMGeul1V0RAbzUEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما را به سخت‌جانی خود این گمان نبود...
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448990" target="_blank">📅 20:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/263f294669.mp4?token=LGTGhgNHTIxw-6fXoMv1rMzvIMjipd_wv0JCARbD7t925dNtmPqMiA9S47FaEnegTmQRm1KuRm6DbKBgylcjynJ8J36d7H-kYq3uQoll52QwymJM0y-lMaXB4EVKVwviAniJ4p0oNfvDUI_eHL_E6i0jE-yZtm6mqlPDqGpoBp0W0MyQE_yDp4jrgRK7lvNtR2QRC6XXjPCEKHGqPZDc-3oa8Ktph85zeJmgr7cBbJZ0BC9QtIk7W5sl7J8T7xJLODvfARnWEKp7xVgI_zejKCaibiKsfBLVsy5oAK7qRZgEdUfayl5u42ZPP7ymJ27BZHBN3CYV0o9u2XO9-Yz5-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/263f294669.mp4?token=LGTGhgNHTIxw-6fXoMv1rMzvIMjipd_wv0JCARbD7t925dNtmPqMiA9S47FaEnegTmQRm1KuRm6DbKBgylcjynJ8J36d7H-kYq3uQoll52QwymJM0y-lMaXB4EVKVwviAniJ4p0oNfvDUI_eHL_E6i0jE-yZtm6mqlPDqGpoBp0W0MyQE_yDp4jrgRK7lvNtR2QRC6XXjPCEKHGqPZDc-3oa8Ktph85zeJmgr7cBbJZ0BC9QtIk7W5sl7J8T7xJLODvfARnWEKp7xVgI_zejKCaibiKsfBLVsy5oAK7qRZgEdUfayl5u42ZPP7ymJ27BZHBN3CYV0o9u2XO9-Yz5-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاوت آیاتی از کلام‌الله مجید در مراسم بزرگداشت رهبر شهید انقلاب در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/448989" target="_blank">📅 20:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e24b27639.mp4?token=FRXgUqCj6YzyA2ZeO4TIb0BLxmgQGHZ8r_6FzKbpEPnlxhFtoSk_RvLR3-W2j9GmGC5paeDFr6JSjvBWKEmxqwIcFLtSqCeKjpB4voLkrDH2uBlIylBTnhdmHr_o3VcuDF5lkrOCj4u9NL_5EDdPYn7to1GsR-2kfEonvVhnj3ZQdm70mA6Lvg4U9pAlCohmWYFnjgjRDFshoM3ane5_4bdL_-yfjNcT-26O1xl4fGqM0iQHs9s_yscWzbT3cWQKU-Ed__PKwepW-IhpO6Wc2-ESlunMXhiBnuHzdcSfrjOmyTNto09NEYqfvkrkjpTW3vPJuVu4lO63pHkb0vvj_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e24b27639.mp4?token=FRXgUqCj6YzyA2ZeO4TIb0BLxmgQGHZ8r_6FzKbpEPnlxhFtoSk_RvLR3-W2j9GmGC5paeDFr6JSjvBWKEmxqwIcFLtSqCeKjpB4voLkrDH2uBlIylBTnhdmHr_o3VcuDF5lkrOCj4u9NL_5EDdPYn7to1GsR-2kfEonvVhnj3ZQdm70mA6Lvg4U9pAlCohmWYFnjgjRDFshoM3ane5_4bdL_-yfjNcT-26O1xl4fGqM0iQHs9s_yscWzbT3cWQKU-Ed__PKwepW-IhpO6Wc2-ESlunMXhiBnuHzdcSfrjOmyTNto09NEYqfvkrkjpTW3vPJuVu4lO63pHkb0vvj_4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ اقامه دسته‌جمعی نماز لیلة‌الدفن برای رهبر شهید انقلاب در حرم مطهر رضوی.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448988" target="_blank">📅 20:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448986">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تکذیب ادعای العربیه و فاکس‌نیوز درباره مذاکرات هفته آینده ایران و آمریکا
🔹
درپی انتشار اخباری از سوی العربیه و فاکس‌نیوز درباره برگزاری دور جدید مذاکرات ایران و آمریکا در هفته آینده، پیگیری‌های خبرنگار فارس از یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی بیانگر این است که این ادعاها صحت ندارد.
🔹
این منبع آگاه در گفت‌وگو با خبرنگار فارس، اخبار منتشرشده درباره نهایی شدن مقدمات مذاکرات در اسلام‌آباد و همچنین ادعای ادامه گفت‌وگوهای فنی در هفته آینده را تکذیب کرد و گفت: این اخبار کذب بوده و هیچ مبنای واقعی ندارد.
🔹
وی تأکید کرد: اخبار مربوط به روند مذاکرات، در صورت وجود هرگونه تحول، صرفاً از مسیرهای رسمی جمهوری اسلامی ایران اطلاع‌رسانی خواهد شد و ادعاهای منتشرشده از سوی برخی رسانه‌های خارجی قابل استناد نیست.
🔹
گفتنی است، شبکه العربیه در ماه‌های اخیر نیز چندین بار اخباری درباره روند مذاکرات ایران و آمریکا منتشر کرده بود که پس از تکذیب از سوی منابع ایرانی، نادرستی آنها آشکار شد.
🔹
این ادعاها در حالی از سوی العربیه و فاکس‌نیوز منتشر شده که ترامپ روز گذشته در واکنش به برگزاری مراسم تشییع رهبر شهید، عصبانی شده و با فحاشی از پایان تفاهم سخن گفته بود.
🔹
با این حال، کمتر از یک روز بعد، برخی رسانه‌های وابسته به آمریکا از ادامه مسیر مذاکرات و گفت‌وگوهای فنی خبر دادند؛ تغییری که از نگاه برخی ناظران، نشان‌دهنده تناقض در مواضع اعلامی دولت آمریکا درباره روند تفاهم با ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448986" target="_blank">📅 19:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f20a3c0d.mp4?token=hEQJmJ6zkeJqosky0WmFhgJkaOEAPaL3tuBFfaDMjoeaua4unNs0gJPb4GzzBwu_MnEFMAIN0G70teq5_NCMGMsRPl9cph02PHvDjWnCjbzenKFiHqCFFOT9Hcct2eHZU2t441XqbZlcbddm_p3cELH6hPY_qNXTm6RbUumAHm95urE6pMfmEw8alKlulJqxLiw6SB4SAXD2_3299qJB7l1yRauo5k8grsuz1_t6i2VB1qa5kWb946TyEfyWwxIah5BJcX6lQtAT40zvH9bf1pgy4d2gwMlyo778quy8xXG2Rl2jwKIbF_gcXQpa82CnSLA2Qq6f_Eg3wiOGqFkqNrSET7N1En4bI-ZUbmwrOsdWHOEdngmndt9T3NfZwdf0gpDZ-lC70JobzCEQYeLX7IlKeKYQKdTyouNETV0Gm1vSc_uYbBdCNlf21YuJX2JafCWXVIdwEPT24PDCRf04FbmYGuNtMncoB6Ro3FSYNaFqwDpq0DgpjolvNyRjIiCoiteQ6eRQ9ZRKVJsdSexfAk1p_B4IRkzJyh_7yL7fi2UwuU0384peuWa1MOkbw428bzV478pcfWwEzf3Ttm0jdpLlZEJe2ambDeAROy_yoTgVrReGTGzGg7OyndfuR1DrmzpzkTKGOgqDiZcDkdGaqfW4kYou2cG_ewLOlnJT6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f20a3c0d.mp4?token=hEQJmJ6zkeJqosky0WmFhgJkaOEAPaL3tuBFfaDMjoeaua4unNs0gJPb4GzzBwu_MnEFMAIN0G70teq5_NCMGMsRPl9cph02PHvDjWnCjbzenKFiHqCFFOT9Hcct2eHZU2t441XqbZlcbddm_p3cELH6hPY_qNXTm6RbUumAHm95urE6pMfmEw8alKlulJqxLiw6SB4SAXD2_3299qJB7l1yRauo5k8grsuz1_t6i2VB1qa5kWb946TyEfyWwxIah5BJcX6lQtAT40zvH9bf1pgy4d2gwMlyo778quy8xXG2Rl2jwKIbF_gcXQpa82CnSLA2Qq6f_Eg3wiOGqFkqNrSET7N1En4bI-ZUbmwrOsdWHOEdngmndt9T3NfZwdf0gpDZ-lC70JobzCEQYeLX7IlKeKYQKdTyouNETV0Gm1vSc_uYbBdCNlf21YuJX2JafCWXVIdwEPT24PDCRf04FbmYGuNtMncoB6Ro3FSYNaFqwDpq0DgpjolvNyRjIiCoiteQ6eRQ9ZRKVJsdSexfAk1p_B4IRkzJyh_7yL7fi2UwuU0384peuWa1MOkbw428bzV478pcfWwEzf3Ttm0jdpLlZEJe2ambDeAROy_yoTgVrReGTGzGg7OyndfuR1DrmzpzkTKGOgqDiZcDkdGaqfW4kYou2cG_ewLOlnJT6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عضو ارشد انصارالله یمن در برنامه پرچمدار: آمریکا و اسرائیل تاوان به‌شهادت‌رساندن آیت‌الله خامنه‌ای را خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448985" target="_blank">📅 19:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ce956558.mp4?token=diyZQyzxIGkaJmmEkkDjRJoCP1hdXUG0-vX73Sp72jhtcRqOHpRgEuU-WOjUWi8_UFcx_Mnoi_f_pnjXuDNfpbHql73GGmR_uf0c0bsbfTtBwCCRTBXHUZ-d7NtRQ-MwNXy-30i1X01kqkcW3Wm_g--afY4eqQyr3fHaSMVnS6wsUZb_TWxCMMCHhlhN_9PqB7qUpKHMm5w_sE0wNfmMnR1HKA1vfzUQz55vZGeXcaXk3elC4vG2cgQGoFQYNJ_bgR5tB39BHr2d8Z1UUNscm7YJglAMILyoRv3-osjr4y1DaCHsm32KsTZVEVU2HgYIJkxEu1aPs6QtRH3NRCHDKFznebM9EHfbxbpORvgXicyoy0NDkW5fnvbESqN6AAkA7BI2kZeS5anLwFNvuCDSr1_kqN7ykeB_1Chyne1E2OB06wiE7WtHuqyyy5-LV2S6PZIQ8WphzyUisk8YGrOGgz9QpJnAvWXeuE-DCmSDXyndsstPANp4CRvnKNIjP_xA8l6ReMR3JXDJpv1il1pDhstlRF6tKNlm1MFCO4lQRb6UdGQtdraV_u59agznJa5SbZvMIqSpEQetxOGxjkhAmAMNyYRSA9s17Btn9Pb3xKcE9gabsfCnvz-LKY7qE0KmHe2IJTiHejxbyXuDP7-RPjTLg6R1aaEwgxLrvoKROEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ce956558.mp4?token=diyZQyzxIGkaJmmEkkDjRJoCP1hdXUG0-vX73Sp72jhtcRqOHpRgEuU-WOjUWi8_UFcx_Mnoi_f_pnjXuDNfpbHql73GGmR_uf0c0bsbfTtBwCCRTBXHUZ-d7NtRQ-MwNXy-30i1X01kqkcW3Wm_g--afY4eqQyr3fHaSMVnS6wsUZb_TWxCMMCHhlhN_9PqB7qUpKHMm5w_sE0wNfmMnR1HKA1vfzUQz55vZGeXcaXk3elC4vG2cgQGoFQYNJ_bgR5tB39BHr2d8Z1UUNscm7YJglAMILyoRv3-osjr4y1DaCHsm32KsTZVEVU2HgYIJkxEu1aPs6QtRH3NRCHDKFznebM9EHfbxbpORvgXicyoy0NDkW5fnvbESqN6AAkA7BI2kZeS5anLwFNvuCDSr1_kqN7ykeB_1Chyne1E2OB06wiE7WtHuqyyy5-LV2S6PZIQ8WphzyUisk8YGrOGgz9QpJnAvWXeuE-DCmSDXyndsstPANp4CRvnKNIjP_xA8l6ReMR3JXDJpv1il1pDhstlRF6tKNlm1MFCO4lQRb6UdGQtdraV_u59agznJa5SbZvMIqSpEQetxOGxjkhAmAMNyYRSA9s17Btn9Pb3xKcE9gabsfCnvz-LKY7qE0KmHe2IJTiHejxbyXuDP7-RPjTLg6R1aaEwgxLrvoKROEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوهٔ خردسال رهبر شهید انقلاب، شهید زهرا محمدی گلپایگانی همراه پدربزرگ خود، حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای در یک مزار به خاک سپرده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448984" target="_blank">📅 19:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448983">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس افغانستان</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4d3fe5d7.mp4?token=jaSCLZb_jwbodsUHIMPvyMl60rUqYBN9BJtVc4YbsGt2AsXCPDpTxJswfFgs1gEVAvWmxHeae5cQ6bHvupTMxA4Lkrs4hZFUivRamGrHCaZdrQ5Dj3oPlvyO7HrrMBmGhUv2dicNvuHC7rHu0yDwnaZ4k3Pq6Y9PD_6NL8CNP7UMzilOsZVeivTKZSUKrZ-bo1GYzbe8syybWVPF6ix736Kj3nvjC9Hw8kO0T7FRkDCjB5-uJsbRmsgCOgReL7We-2eV_onRBF-dt9C8cpDYBetShG77qVha9IpA-8HMD3NTuYrGWae7SS0G8mqSnjIXs63pOM7cSt7fh48GND1GwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4d3fe5d7.mp4?token=jaSCLZb_jwbodsUHIMPvyMl60rUqYBN9BJtVc4YbsGt2AsXCPDpTxJswfFgs1gEVAvWmxHeae5cQ6bHvupTMxA4Lkrs4hZFUivRamGrHCaZdrQ5Dj3oPlvyO7HrrMBmGhUv2dicNvuHC7rHu0yDwnaZ4k3Pq6Y9PD_6NL8CNP7UMzilOsZVeivTKZSUKrZ-bo1GYzbe8syybWVPF6ix736Kj3nvjC9Hw8kO0T7FRkDCjB5-uJsbRmsgCOgReL7We-2eV_onRBF-dt9C8cpDYBetShG77qVha9IpA-8HMD3NTuYrGWae7SS0G8mqSnjIXs63pOM7cSt7fh48GND1GwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
گوشه‌ای از محبت افغانستانی‌ها به آقای شهیدان ایران
@Farsnews_af</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448983" target="_blank">📅 19:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448982">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEg-33N8dYD1-lOfg40xyU7w2wk_67idXZmZSjcA80iOu7A5pJ5sgiQRR54X-aWpORTuZRL2Ig7x2J0a14E1JJItmSgNPRGTf2tkToaQpmeDAxTqDuEhxCOCNnv5mPHpPMDGK-eOqhIaPF3SUjjkqmc1HgjxWfCh_vV5tCnm13uYTCwOpYKgF46i1pM0IwhXJxnR7EsEcQbhC3BL7YwKDVBD3QDMnqeDid1fSqKuJRaoCu5X43AudEWjnwlte6hYHMEdeqfI121qC7Q8V626gI4p5_83k4jG0RoJrmeOBFG7siy89W7EySSR4vivfPVtH5gf6mlEEiP9pEqdwuBmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدرالحسینی: تشییع ۴۰ میلیونی، منبع جدید قدرت ایران و جبهه مقاومت است
🔹
کارشناس مسائل بین‌الملل: حضور بیش از ۴۰ میلیون نفر در مراسم تشییع رهبر شهید سرمایه‌ای راهبردی برای جمهوری اسلامی و جبهه مقاومت است.
🔹
این حضور، قدرت بازدارندگی و نفوذ نرم ایران را تقویت کرده و در صورت بهره‌برداری صحیح، می‌تواند معادلات سیاسی و امنیتی منطقه را به نفع ایران تغییر دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448982" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448980">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2afac4232b.mp4?token=lHbV1bs0CVoAot_Evh2p6Li33Av25v1V5UfHjhWAXJOyUEXpcgbBIXtGN-JANcoDYjPCIrsBgxw-7-3Ffo8CdRk7nt5QFYamGSsBQ6HIULF5qKurAG1Qn3MQNYV-21DK-J19RMBclejE_h9VOxeKbMir8pdFiGuCyPtwEepGuZCeIxmXIWN6_S-QByRpDt6U9TPMRSmpda19ys6E8i2224JWBiwfazynhlLDBimXgzXJkv_pWrX0xHJKBK4GDKT56RKQ6isKzfoZOXAzpzdRdG7ZXAKqW7nBGkk5q4st74WXdZYPgChnPMGajEP0-hXVyHFFVdCZouco6nC7P_zSrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2afac4232b.mp4?token=lHbV1bs0CVoAot_Evh2p6Li33Av25v1V5UfHjhWAXJOyUEXpcgbBIXtGN-JANcoDYjPCIrsBgxw-7-3Ffo8CdRk7nt5QFYamGSsBQ6HIULF5qKurAG1Qn3MQNYV-21DK-J19RMBclejE_h9VOxeKbMir8pdFiGuCyPtwEepGuZCeIxmXIWN6_S-QByRpDt6U9TPMRSmpda19ys6E8i2224JWBiwfazynhlLDBimXgzXJkv_pWrX0xHJKBK4GDKT56RKQ6isKzfoZOXAzpzdRdG7ZXAKqW7nBGkk5q4st74WXdZYPgChnPMGajEP0-hXVyHFFVdCZouco6nC7P_zSrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌اکنون؛ تشرف زائران عزادار به رواق دارالذکر برای زیارت مزار مطهر رهبر شهید انقلاب اسلامی  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448980" target="_blank">📅 19:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448979">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12dee16225.mp4?token=GZOn7pE3cOdUfvdWGQEhuvDjPr_FRrrVIp2KqFWp2U9cRlOnDrY17jrTl4Eq9gtB7pvgTeBMgNpoy5FQz1qhNF-4-YcNnOLBcVwy2cGQAAq2-mXqvc8CMWRBu_7yLxq630Q_Cpsygzpfo0WO0IhmfvzNjnk2s8OiYapoEGmz20xj0aVhInw_4vSF4UtBeKExXD4bJ-BDn3SUwkW8GZaeTdZG6ncgbXvSAtePGcn_JV7XYZbOKXHcnTLrc0wvf8bJ5etDRI1gKn81LrAuBOG6a6_VF218uiLQ3FPuYi3_vS6ioZkEwt4qZ-c45qW5xuW9vN5gS9h96LQidyFecwQ1LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12dee16225.mp4?token=GZOn7pE3cOdUfvdWGQEhuvDjPr_FRrrVIp2KqFWp2U9cRlOnDrY17jrTl4Eq9gtB7pvgTeBMgNpoy5FQz1qhNF-4-YcNnOLBcVwy2cGQAAq2-mXqvc8CMWRBu_7yLxq630Q_Cpsygzpfo0WO0IhmfvzNjnk2s8OiYapoEGmz20xj0aVhInw_4vSF4UtBeKExXD4bJ-BDn3SUwkW8GZaeTdZG6ncgbXvSAtePGcn_JV7XYZbOKXHcnTLrc0wvf8bJ5etDRI1gKn81LrAuBOG6a6_VF218uiLQ3FPuYi3_vS6ioZkEwt4qZ-c45qW5xuW9vN5gS9h96LQidyFecwQ1LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ازدحام زائران حرم رضوی و انتظار برای زیارت مزار رهبر شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448979" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOaVS2klrthZkmpiXvGBHNzqpP7IG1DygJiD7un1IWRGt0RErtlQkbtvSdurn9snOX5XIyWSwecPlrWg8QTNzoVwtK21XNS4mQtcrBUSU-ymjooDK49A1wiJTHMNgxRJBR6DCpiPKjc3zsmdL9rLZxRYuYEN_AmoegNgv1LaMBrZeQqfC6xeKgy6me7VNqGgn-HY0x-OWYwuRmqxcWTEOrN5JMFSiO5SxU2g8J0HKM1iIkEsSKCTWO2_HJP4OY7g0fVe8tG5m4lXFUAv9bs33vbVx38sLNfr4ocw6TBzQVpizNIhoSqkypotNZTnwuHow_iCOkcxcM-LpXedXbyp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkPhY63ylP83P12H48Yw49u5zlMpxvfiIBHCqW9VqiPyKVcwdXAmxsT5SKKjkf_EgFJYtrHe1W-qO9P9XYykYW6hTKk0xOCEn2F5dCoWzsD5ipL1IfdM-h5Kg8_hnewGaVGoUSBgvrnqSisin6Jr5lxazZI_Fa9FrRgQw2n2B_2Xg3Uh33_Ca-9BS0Lpta77RHOzyW41ID8w-MMVHF5S8YozvaepysHppBjph4SJ0l82gFdyjPKRL2Q3IleKJtBBdY5O7Jb2mWMR8YSti1f47deylYfbefzQ_XasQ27mzs5w7uB7-vpBfe8e-iObBYXrbomtyBctl-F101ImV9L-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2IHxpNS5U7xWdmXWG6r4zOzvPsxEVCCefrGGlt1aFJMXIQCOPIEGkqJvr3-8gYkL3QceknL16xlcRibq01Hab_8M5riALsVdUUp8FeXvUB5ic_VNz1dL39Okd1_kPcq3jHmFhOIjdwytbXBT50V_c-sFt2S40BrrvFCUy2A9yetLmoAVtgyHtOG0JOHktNxDCf8gDNSrx7eVt06k437SRtPfrzUsFvw6a1vQ9mMSec0HWtyDHugzvOfD1DqxNusv4pZN1-6WrZ4MfMKHpcO7Ru19F8mr4wqOJlR4xGDTTDQlTchOayGeQCJpZB1zGS2DU0eQ1XsjyjEtLfFIV6b9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
البخیتی، عضو ارشد انصارالله: یمن ملت ایران را تنها نخواهد گذاشت؛ ما دشمن دشمنان شما و دوست دوستان شما خواهیم بود.   @Farsna - Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448976" target="_blank">📅 18:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448975">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLBoHSpaJDV6uyVrhb9lxZATzYYhp8ym43qmGBRogAyodnIXi5YX7CFflHJWd6lkZWeoeKA0IrToAsUyncNEVt_bgalvEfYUvmw847-08WpNMujp_DlaXOjR3yQgCswO_zySCYCg5PfMityP4C4eNJId_dyW-PDp38VeFJTTZ1-ZZXH4dKrY-oHQ7JRhNZSUHEoH4mH1zNCqYZ8KAHaUtgy9TXg1glpGiXMz76JLzREHETbgi6UaCymPF_rMNP8nWT189PxfS9WODmqPTSmtRWlDvc2vkG56eOCv3T8d466R-F9ZWY9Fp6fMH-beRcRW9mJulAZfQTivKCiDzVtiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر هواپیمای ترامپ از ترس ایران
🔹
روزنامه نیویورک‌تایمز به‌نقل از منابع آگاه گزارش داد همزمان با تشدید تنش آمریکا با ایران، سرویس مخفی آمریکا به ترامپ توصیه کرده بود هنگام ترک ترکیه، به‌جای استفاده از هواپیمای جدید ریاست‌جمهوری، با هواپیمای قدیمی «ایرفورس…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448975" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448974">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bac2dfc17f.mp4?token=UIj_bQiNcMWfdLf_qN2W7bsJX0mOm6BznEzWBwTj6B7OpYoRrIBDZWe3YCV9y09FI4ljlUcP3Fm8UyPBwSGHCXkX8GcWApbUU-9Vpu9JYtgNipeXuoVgILOeSQRj9JKqPJa4qjzGVbjctChq_5_C0XY_Fr7RJTRV_aBO4kQhcnAmr6vKRZ4rxw9OTBj4DBa1K1dmNaBuQdXI1ncrSA7HsQdz07z7QYnk_obS0CpmxPm4d6ayexoGtNgAQyENjRjXPkqj_pkMKlw9FxXf2k57k3kGEtc81nfZmBnLZo9e5IerU1EgVpBQfwtsHPSQCVmLDnSIB5mNoJdxuFwxlf2ZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bac2dfc17f.mp4?token=UIj_bQiNcMWfdLf_qN2W7bsJX0mOm6BznEzWBwTj6B7OpYoRrIBDZWe3YCV9y09FI4ljlUcP3Fm8UyPBwSGHCXkX8GcWApbUU-9Vpu9JYtgNipeXuoVgILOeSQRj9JKqPJa4qjzGVbjctChq_5_C0XY_Fr7RJTRV_aBO4kQhcnAmr6vKRZ4rxw9OTBj4DBa1K1dmNaBuQdXI1ncrSA7HsQdz07z7QYnk_obS0CpmxPm4d6ayexoGtNgAQyENjRjXPkqj_pkMKlw9FxXf2k57k3kGEtc81nfZmBnLZo9e5IerU1EgVpBQfwtsHPSQCVmLDnSIB5mNoJdxuFwxlf2ZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با آقای شهید ایران از نگاه دوربین فارس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/448974" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448973">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823afc570e.mp4?token=INGHVjOa6avRo-wlzT7HvB_8Xe7RxNbWzHPUphJpXP5acXxjkV5ryGXQLJ9zs6STGZVKGf-2j_UNmznz6wR0Fdmfy9Ahj2yHmHWjXgtj4GilR6enbiMeoQ4nX2aFCfeiuVZIykzTO0Tmg0-pgq0EMlMB7IRqOHDGQXXrNXw3FjICWvVGHMC0d_mw3BoSkZMYprjmIpnywTGpWkz28JRt1IU0hB1gbRzLzNXJ_dSdLYzYwF9cIR6XspScx4UsAnYH6i2zvAeE4ZlOLB2FKsG1zT6JVnzHOkjlliVqKK5C-TUVF0UMuBOc0HXEtzRSOVfjaidIG4HiwEQEaf_WTu9tH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823afc570e.mp4?token=INGHVjOa6avRo-wlzT7HvB_8Xe7RxNbWzHPUphJpXP5acXxjkV5ryGXQLJ9zs6STGZVKGf-2j_UNmznz6wR0Fdmfy9Ahj2yHmHWjXgtj4GilR6enbiMeoQ4nX2aFCfeiuVZIykzTO0Tmg0-pgq0EMlMB7IRqOHDGQXXrNXw3FjICWvVGHMC0d_mw3BoSkZMYprjmIpnywTGpWkz28JRt1IU0hB1gbRzLzNXJ_dSdLYzYwF9cIR6XspScx4UsAnYH6i2zvAeE4ZlOLB2FKsG1zT6JVnzHOkjlliVqKK5C-TUVF0UMuBOc0HXEtzRSOVfjaidIG4HiwEQEaf_WTu9tH4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چشم انتظار زیارت مزار اقای شهید ایران هستند  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448973" target="_blank">📅 18:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448972">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbmL7AJ74a3hYpAOiSx7tH-4jrcED6Bxo4H6ymA3zRFVpqc-iDCy4B3PeXf91MR-OT5LAusybBdCjVNSpv7lOpJQFGMDfiLFLh5NwctuHNp2GVkfpfgkINkQXRojJHKl_1gjrxhCmN2rU7HwV2WS0pvn6UEs5EKb-WUnmk_vYPe9zicYTjNzxvhkZ0GIWYAyNzjBpPhuGb7zDeW39Qklog3857YtvJmLtF1QLkNilx8Uc22un0lZUhSy0EYmNmZzcViOkRD5g8HCQwREnLfmPx6qkjQXz_ILt6vQJ0wtBIByuikead_WPKDCpbPOdafcQ3E5Q095c0LqFWp5QmMg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بازهم در جهان موازی درخواست ایران برای مذاکره را پذیرفت!
🔹
رئیس‌جمهور آمریکا مدعی شد که ایران از دولت او خواسته مذاکرات ادامه پیدا کند.
🔹
او مدعی شد: «ما با مذاکره با ایران موافقت کردیم اما به صراحت اعلام کردیم که آتش‌بس پایان یافته است».
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/448972" target="_blank">📅 18:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448971">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac1cb4c3a.mp4?token=C7p1fLgHt904SadTKIFctVlXyrHFPHnqZJM6aH66G62rmwHbAiIl1C9IVX55AhSyqodLdA44TYLA_4o5OJreCTkZsJ29xQZPNyEqXkGxqgJT4bm19tiwBXUDowIKy8sYj_wSbwYWvrKJxxmFceT0kJjQj_ZrOnDArVxgyO7fdCyJPrd1RtOvWaV9s3ekkx0VYIyfAXN1k_q3vMGNAkeGAc582u61GAkwHSFmexmp9vSa3wnO5EyOvfLtHYbZInsiRH391_KSftNLDar_KDkGYE3wVOvzYf-ojvDZXIFNM5_kF0j97u-Hk63iD73oMHpMaKi92AaqQreA0aFLzaJS0xw3cman0NNa5Dt2IvN2rUJrpd4nrHSBs9o7mE6h7yAvYze9uB5XYyLqv_wdVHdoseCuo6emShfBcW2xP5oCtiZYeDo5-h0h92zB6hosIlo7U2AeqUfKucTwWWPAZCG0BMeBQBC9kBVQCZswWQfXSF9Lk9eJOuzhpxaqzQYyOU9ENr2VCK_ekj6EedSxWpsrzxIuCHMmHEG2gWVsacH09c3NZt2g-wCsMRwbFw6R6EXXm1z93Go4Yu4OC5PJ9M1ZsIJXDnafOo5OcHfXF83szYwOu3-h93smQDUHK7e6rJhlw0gBpWO_wIlunLgE9AupxJzbYuoTEMFAWW06IlJHzdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac1cb4c3a.mp4?token=C7p1fLgHt904SadTKIFctVlXyrHFPHnqZJM6aH66G62rmwHbAiIl1C9IVX55AhSyqodLdA44TYLA_4o5OJreCTkZsJ29xQZPNyEqXkGxqgJT4bm19tiwBXUDowIKy8sYj_wSbwYWvrKJxxmFceT0kJjQj_ZrOnDArVxgyO7fdCyJPrd1RtOvWaV9s3ekkx0VYIyfAXN1k_q3vMGNAkeGAc582u61GAkwHSFmexmp9vSa3wnO5EyOvfLtHYbZInsiRH391_KSftNLDar_KDkGYE3wVOvzYf-ojvDZXIFNM5_kF0j97u-Hk63iD73oMHpMaKi92AaqQreA0aFLzaJS0xw3cman0NNa5Dt2IvN2rUJrpd4nrHSBs9o7mE6h7yAvYze9uB5XYyLqv_wdVHdoseCuo6emShfBcW2xP5oCtiZYeDo5-h0h92zB6hosIlo7U2AeqUfKucTwWWPAZCG0BMeBQBC9kBVQCZswWQfXSF9Lk9eJOuzhpxaqzQYyOU9ENr2VCK_ekj6EedSxWpsrzxIuCHMmHEG2gWVsacH09c3NZt2g-wCsMRwbFw6R6EXXm1z93Go4Yu4OC5PJ9M1ZsIJXDnafOo5OcHfXF83szYwOu3-h93smQDUHK7e6rJhlw0gBpWO_wIlunLgE9AupxJzbYuoTEMFAWW06IlJHzdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوت‌و‌کوری مسیر جنوبی تنگه هرمز
🔹
پایش ماهواره‌ای کپلر نشان می‌دهد که دیروز پنجشنبه ۲۲ تردد در تنگه هرمز ثبت شده که فقط یکی از مسیر تحت حمایت آمریکا بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448971" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25fb41b7d9.mp4?token=k0Ap2REGghx3YGW8NBk77eB8Vfn9mpUfP0oED8fEn2BrkN5ahP2TaUoOt48gNgDhbhPMdniSnQul_bHp7kQauxzNE5cp2bmxwt6TXTjuTeGLDqT6V2mLX4rCdP65cAPCASTRPZ2PCodRxCMwfjaqXm3hKBX-ffjkTuIAWVlW_EavEFnxd4W5BE39ycJPTUN8V4Gdoeu_4KjZ4YMV2yEFtj6Mt_dhVdnDEc1L7xVzcNRIpRwLOEOJmy-JOoXzNikyeHK_v7HePISul2pOJEFdZsgaPKOJbliUpfWNiInHMVuDAFgspR_4Q5v0PaDe2QeEESxwN32Jr6SJ9s5mzpaGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25fb41b7d9.mp4?token=k0Ap2REGghx3YGW8NBk77eB8Vfn9mpUfP0oED8fEn2BrkN5ahP2TaUoOt48gNgDhbhPMdniSnQul_bHp7kQauxzNE5cp2bmxwt6TXTjuTeGLDqT6V2mLX4rCdP65cAPCASTRPZ2PCodRxCMwfjaqXm3hKBX-ffjkTuIAWVlW_EavEFnxd4W5BE39ycJPTUN8V4Gdoeu_4KjZ4YMV2yEFtj6Mt_dhVdnDEc1L7xVzcNRIpRwLOEOJmy-JOoXzNikyeHK_v7HePISul2pOJEFdZsgaPKOJbliUpfWNiInHMVuDAFgspR_4Q5v0PaDe2QeEESxwN32Jr6SJ9s5mzpaGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران قهرمان مسابقات بین‌المللی ریاضی چین شد
🔹
تیم ملی المپیاد ریاضی ایران در مسابقات بین‌المللی ریاضی چین با کسب ۴ مدال طلا و ۲ مدال نقره، عنوان قهرمانی را از آن خود کرد و بالاتر از لهستان و برزیل ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448970" target="_blank">📅 18:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448969">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۹.pdf</div>
  <div class="tg-doc-extra">3.8 MB</div>
</div>
<a href="https://t.me/farsna/448969" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۷.pdf</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448969" target="_blank">📅 18:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c464275300.mp4?token=C4D8x9QH0s55nDMw8C19Xbe6fRR7maCpKUxCeaztIcTDDZ9AhI_SUShO-1Gim8GOvJQ20JEZdp_XMrcE6V0IdeCqQRzEPqTLrg3VENvkpekrxETeJAxZpmTXJe9KQvG7YgCtOSIo5vWnBPvwXALeSwZzTldjnx4vmr69nSUvQRFYM9VHus4yIIaMBhZR7ZQgokoP3EMlO4cbGEMykkSxJK3KdGiOQyp-GmcZXeQn-3y75_Z_lMcdQ0jYy_qnwB1A1fEEn5928MsItuNuj0fJAl4xtBdsCzddDUfuFwJuukf7tQU59Q9TOUSve2QXNpepzgzlAkUQ0mAbiZ-W-a7_HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c464275300.mp4?token=C4D8x9QH0s55nDMw8C19Xbe6fRR7maCpKUxCeaztIcTDDZ9AhI_SUShO-1Gim8GOvJQ20JEZdp_XMrcE6V0IdeCqQRzEPqTLrg3VENvkpekrxETeJAxZpmTXJe9KQvG7YgCtOSIo5vWnBPvwXALeSwZzTldjnx4vmr69nSUvQRFYM9VHus4yIIaMBhZR7ZQgokoP3EMlO4cbGEMykkSxJK3KdGiOQyp-GmcZXeQn-3y75_Z_lMcdQ0jYy_qnwB1A1fEEn5928MsItuNuj0fJAl4xtBdsCzddDUfuFwJuukf7tQU59Q9TOUSve2QXNpepzgzlAkUQ0mAbiZ-W-a7_HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم چشم انتظار زیارت مزار اقای شهید ایران هستند  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448968" target="_blank">📅 17:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRM-7JfIkmbS-_NI5aV6pqyCKzqaRRzS4Gkes4mVDN9kNtl5msqtqOxCsHPV0n_nMTuZNxwLNM0LQ4BXuPC2ukeNXFDNF_4xkzSfzbX2-D2XetTz8fFPdRnMbmejdiUi4BxbrWn55mULIJiva0XOBnAezrfyjFXfrCzszxSOXRW6PotUuMd__fod7nTmigPgU2gcEj6xpjt709PHWJuiqwSBDf-76Eg6RsD1Nnr7OLID2qQlRWMyEG8ljOQ79wY98rBGqQj2aPczuO4jnzdlpdK-WTY3AP2F_zDT_XQDUzc60RKTjXqyZ7TwN4QQZjuCA4xHZLB_Q3eoXAQDd_IkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاطره نایب‌رئیس مجلس از توصیه مقام عراقی به آمریکایی‌ها
🔹
نیکزاد: در عراق از نزدیک شاهد بودم که نخست‌وزیر فعلی عراق، نخست‌وزیران سابق، رؤسای فعلی و سابق مجلس، وزرای فعلی و اسبق و مسئولان عالی‌رتبه این کشور در مراسم تشییع رهبر شهید حضور داشتند.
🔹
در آن‌جا یکی از مقامات عراق به من گفت که به آمریکایی‌ها گفته در مذهب شیعه، هرکس در برابر شیعیان با تکبر رفتار کند، شیعیان متکبرتر و مقاوم‌تر می‌شوند و هر کس با تواضع رفتار کند، آنان نیز متواضع‌تر خواهند بود.
🔹
او به آمریکایی‌ها توصیه کرده بود که از غرور و تکبر در برابر ایران دست بردارند و با احترام و تواضع رفتار کنند تا پاسخ متناسب دریافت کنند.
🔹
بیش از ۴۳ میلیون در مراسم تشییع و‌داع با رهبر شهید انقلاب حضور داشتند. آحاد ۹۰ میلیون ایرانی خود را در این مراسم شریک می‌دانستند و اگر شرایط برایشان فراهم بود، در مراسم حضور پیدا می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/448967" target="_blank">📅 17:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojkeLQWl0NMcQjpPiNXlt1cmLe9yqz3JzJDoza4Ww168rp2brbfluNRORdjAm4uplNqLmKUHg0VBD0Fco4dAh48nocR2Ln61nPLdkoRv-YVvFugBsz6BMJI575cMmU93h7U5jm8OX8foz93J4CG0cBa95z2e1p_PeavSNQMZb1S6w6zb8BCqqeMijIHFGamtNuCF0rfCegjiWu7Qy1YJexa830tnidN9sqOg5GSyjHe2QKR8iZTKxz8Sw9xOh7Ah9dbMevXfMjH2tfsrwCY9fYB6YXVBo2HS_8TX19_rY41U9e6qmjrBqsqn95kToyPwVB5gO-y9NcIeCbd9UQzzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیلی: تشییع ۴۰ میلیونی رهبر شهید سرمایه اجتماعی جبهه مقاومت را به رخ کشید
🔹
وزیر سابق ارشاد: این حضور کم‌نظیر، پیام‌ها و دستاوردهای راهبردی مهمی در عرصه‌های داخلی، منطقه‌ای و بین‌المللی به همراه داشت.
🔹
مشارکت بی‌سابقه مردم، شکست پروژه چندساله جنگ شناختی دشمن را آشکار ساخت.
🔹
دشمن طی سال‌های گذشته با بهره‌گیری از عملیات رسانه‌ای و روانی تلاش داشت میان ملت و نظام فاصله ایجاد کرده و به‌ویژه نسل جوان را از آرمان‌های انقلاب اسلامی جدا کند، اما حضور بیش از ۴۰ میلیونی مردم نشان داد این پروژه با شکست مواجه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448966" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448965">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb345674e.mp4?token=R02Gref30biOBxisp1fbvTiAHANzUAevHhIbkCqNr-QmDZzHfxaFLyLStwteo-E1dkm5DV3_mfDsdjumk84cXMcz_hv9vWiU-cPN9goE9--gChGVbHTwiAGMvROAoiipctKRL-wIUN8bZ9UfqtSysd-X9XJF8z1QlF50ZtG6joXsx0fG5WhJYVuDSAZ9f7dBO32Ja-yXruYuhlEP8KG9KLThTCsXnXc9uinPL-SFmkbE3RQEzHc7_8MDh4RBQ7KL1hfPcgPFKl9INrGOpgJzTyZaBy7pTxDaXuUon_bE5szF28h0zNISBQMwsUrMHP35DPXuRt-HM-mB4YMpp12pLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb345674e.mp4?token=R02Gref30biOBxisp1fbvTiAHANzUAevHhIbkCqNr-QmDZzHfxaFLyLStwteo-E1dkm5DV3_mfDsdjumk84cXMcz_hv9vWiU-cPN9goE9--gChGVbHTwiAGMvROAoiipctKRL-wIUN8bZ9UfqtSysd-X9XJF8z1QlF50ZtG6joXsx0fG5WhJYVuDSAZ9f7dBO32Ja-yXruYuhlEP8KG9KLThTCsXnXc9uinPL-SFmkbE3RQEzHc7_8MDh4RBQ7KL1hfPcgPFKl9INrGOpgJzTyZaBy7pTxDaXuUon_bE5szF28h0zNISBQMwsUrMHP35DPXuRt-HM-mB4YMpp12pLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب ماندگار از مزار مطهر رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/448965" target="_blank">📅 17:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448964">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbwapkuvzoPMFmeYx6-BPTW-Q42m46JQ4dKHDg_UHb_u7_e22dSLaCqyqa3mLHVV6y0TvALC0GPDzurduj9WymzsR5jxXNR_hiaLAtF4weaRnpo2VpTniS6FE2K3dQQm1zfc4Bq4pw4KJabIDFJTZbbQf_P0WPSvku8E7S2ETRVzH9nWMOF0EAIPfrroN-98eNUfQRBbXhi2mFxh7ch4CezPs2ox1D8j-ZkKQLMu-iqM-VOGrde38J8rXGX009HoJHWDNmb8EkEcQQoRaFPnryM6LPFEZJLezeVes7xzzG01z8NuTQrZn2s569fanputZZAbHFXYhYQVOvs1fPcjJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مزار مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان در رواق دارالذکر حرم امام رضا(ع).  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448964" target="_blank">📅 16:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI3aYLysvylXti3LPrcSVNhuZtCaCzup_1PsnAWy6mnpoZ8USP-3iNLoaqXEHfDD-a3dhK9tYfhB2vKHXmYfMcH0xYY2VON1XzCIbjVmZImQM0IoYkgHPfXjQZqgn-WCY2KnBPG9GvCD0MvQIgmZe2o5HCfXIl5Pmsea2YtmFNkh3WkDUiz098-4g8Nj1prTj-owXDX2GSljDomNRfoCMFQVBkbmRRFBfUUI97bC2jL-MUzcFX9uUrULuYYWzEOMDmJv2QzDuJSGoHzx_lENi-UrT0xxkr5ryrBpLgbvhZH1oQhlDlHVrevXK0-fHhrhWr7FyS_kGmCyfCZ0s4TyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه دفتر رهبر شهید انقلاب درباره اعمال مستحبی مربوط به شب اول دفن
🔹
با توجه به اینکه پیکر مطهر رهبر شهید، حضرت آیت‌الله العظمی سید علی خامنه‌ای اعلی‌الله‌مقامه‌الشریف، و شهدای خانواده ایشان سحرگاه جمعه ۱۹ تیرماه دفن شده‌اند، مؤمنین می‌توانند اعمال مستحبی مربوط به شب اول دفن از قبیل صدقه و نماز لیلةالدفن را به امید ثواب پس از اذان مغرب روز جمعه (شب شنبه) هم به‌جا آورند.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/448962" target="_blank">📅 16:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448961">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUP2EgqNWcaWH1ZvqLd_B4Myi_AVFgvw7J63hcf_f_l5DKDD1_s041aTcEGnINurcims80SYan9jM7F1NzT-Riq_5k5ySWvf_dmyKpqzMJHKuc2dt-Qhn9SSa05kfZ_vMb4wfTp5M8tObayv1vh7q-EPOBSLhqnAJB5fK91yKLOOLAACqdh15nd93u6CsDchH_UKSfk0_O9Vl4Nt3H9_mr61hepDMwdrjj_UJABDDc50gGz54Ji9yrysRGnJnI60WZ5skO5Tswqmq18gUXIEeTPCKWUPtSNc8EIH7WNCMZ-DQOR82vFiyyVPcddOYLneeJLqGm2opkEnwWRDQvyteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: تشییع ده‌ها میلیونی رهبر شهید معادلات بین‌المللی را دگرگون کرد
🔹
این حضور، معادلات بین‌المللی را دگرگون کرد و نگاه جهان به ایران را که پس از جنگ ارتقا یافته بود، بیش‌ازپیش تقویت کرد.
🔹
حضور مردم نشان‌دهنده حمایت از انقلاب، ایستادگی در برابر آمریکا و بیعت با رهبر جدید است و پشتوانه‌ای مستحکم برای جمهوری اسلامی به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448961" target="_blank">📅 16:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448960">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFBAPQYgBWYqEyF1jE5WfDqH9nbmUH5aMRrcbfzefPkbkR29Q3sWT3cfra75p8kCfQPtY1g5VMwdFLP5lX1kSo-_krWlcANIT-3uIRVYX4Xc9KZHy1kEnRNdh2CKIia3sq2wRdHXammRLCm0ZOOl8LTdU821RwCdMsLHVXi5AxAVPrxdLTBD44IdKqSLY-thn_mfR4aAmEYORWyg-mflmRdbMCsiJYLBoOJJ5MGRfjXwUWD9M9bcb4IPCWp22f020oJVgA-KzN5jgUuTWOxSW53iCVNV3LX7LBM7bf_JMTqZ2sTZqj-mgWfscQC5ouPpw53xlf2bnqJW5bbXLYqynw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم بزرگداشت رهبر شهید  انقلاب در میادین سطح شهر تهران برگزار می‌شود
🔸
۱۹،۲۰،۲۱ تیرماه از ساعت ۲۱
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/448960" target="_blank">📅 16:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448959">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXX5JCz36jgrFM684kOsxLdjZQTSyplKfoHWrigGb_NB8VBBHVXb1T4pUmOMA9OZsPFfU0fZNwO3VeCngTwV-fn4ioIuY-Fb7P1w53TGAZuWE8NMZt2QNK03JNd7wlpy8dlBNQR73PCG3bENVtPYzv0sm4RTMoG4mIvmVsM14pi_vLqa27gEM1wgqxevkgU-b00XD4ebxPIq9omfRIqqyiyrY7X8GN-s2h4YUZi0UGoZDhcKVtHCB7d0Efb9YZztZf--grMwBMkLj3Wq7lvUSIjN_GebCtCWEAwCoqiiitoCMQE91yqNjlsoK_pIA6vy4BOABpr1s-D1mY_ajnViVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استوری مهران غفوریان برای آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448959" target="_blank">📅 16:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448958">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd85be99fe.mp4?token=T6udk8TYqLjqHi62CwG8vUHxU64rB5zM1dY0EGwU48K34grJ7uZO_HgyDg0jhexlcHzRPyCCwGD4QdPEZ4aP41opH-kLkcimKJ3fLQpt6DxhBSnhFbzWkZzPcEI5QVEGR_gBhRCpq4fTmsYuK2f3iCQ4T714WX82n_eFeiyPrpVUVbmKuaJEAhalDAmg4a1874-hpYJynUv6mBki1pq8sTxB-3gkgFan16PhqywIv6RwDmcz3KURvYJ3EM5cRfmuAe6ej9elXYj8VpKZW76yB1DBRJn--zpXeBdtvjRmRR9x32Q3tRkY_R87KTxa8DPoicZMWOH1Sk0v1nd7wVlr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd85be99fe.mp4?token=T6udk8TYqLjqHi62CwG8vUHxU64rB5zM1dY0EGwU48K34grJ7uZO_HgyDg0jhexlcHzRPyCCwGD4QdPEZ4aP41opH-kLkcimKJ3fLQpt6DxhBSnhFbzWkZzPcEI5QVEGR_gBhRCpq4fTmsYuK2f3iCQ4T714WX82n_eFeiyPrpVUVbmKuaJEAhalDAmg4a1874-hpYJynUv6mBki1pq8sTxB-3gkgFan16PhqywIv6RwDmcz3KURvYJ3EM5cRfmuAe6ej9elXYj8VpKZW76yB1DBRJn--zpXeBdtvjRmRR9x32Q3tRkY_R87KTxa8DPoicZMWOH1Sk0v1nd7wVlr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم پشت در رواق دارالذکر، محل تدفین رهبر شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448958" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448957">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNrj-aCoAjblkXnxcWIe28AVOBmg9FmzhjeTdwxfdVUm4o_ahlvmmTyyA057V9DW3eYUIpUJTw0UVEJ41Ye1cg4htGbpLtUi6N1w_7wcY6Km-fQp9BbbQ9tfiAqITIXOXQEPvXc4PTyty9XL7vzd2XTW-yHcZ3Vg5rBSt2GkM0THCrJmSy-OQ-8mpjGek9hX33KF8qgZaB67qzVMleIsweJtvzq211D8RtGEzwuge4HUZuEoCCjxtjoZJRbYMwxZgWfJcA372H5wHk1hPXSQgVQ72EYMO7hUjBcOR0_mpZ0ljQPFK3DnwkRUmeGV8LppslBThLQDFwKjIYpUdCJuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینی: تشییع ۱۰ میلیونی در عراق، ترامپ را عصبانی کرد
🔹
معاون پارلمانی دولت شهید رئیسی: عراق سال‌ها تحت اشغال و نفوذ آمریکا بوده است. حضور گسترده مردم در نجف و کربلا، ترامپ را عصبانی کرد و نشان داد نفوذ معنوی رهبر شهید انقلاب فراتر از مرزهای ایران است.
🔹
این مراسم، محاسبات دشمنان را تغییر داد و واکنش مقام‌های آمریکایی نشان‌دهنده تأثیر گسترده این حماسه بر افکار عمومی جهان بود.
🔹
حضور میلیون‌ها نفر در ایران و حدود ۱۰ میلیون نفر در نجف و کربلا، روایت رسانه‌های غربی درباره فاصله مردم با جمهوری اسلامی را با شکست مواجه کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/448957" target="_blank">📅 16:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448956">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای رویترز: تیم مذاکره‌کننده قطر در تهران حضور دارد
🔹
رویترز به‌نقل از یک منبع آگاه مدعی شد هیئت مذاکره‌کننده قطر در تهران با مقامات ایرانی دیدار کرده است.
🔹
به ادعای این منبع، هدف این سفر کاهش تنش‌ها و فراهم‌کردن زمینه ازسرگیری مذاکرات ایران و آمریکا با هماهنگی واشنگتن است.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/448956" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448955">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWagyu4yjkYJuhymSare2j-hTMv7wrHNg1tc8E-_E8_rJ4cCBU2Jyvs6PjrBcCY34K7gj9Tdp7GCtFK9VnGCqY-fGsZb_23SnXBa78-lCUlDUVtsytFnoinqgECSKHaI2g2Yd-91FC0QD6QAMau9KDDJ8KZ6VhFaX1KF3HUT-xjW_7AlqiJnxGDCwcss0ZUQwXZo3sUvNLLEZpj2pOdIunByet6T6mK0_RhB4uocmr5fkSd4BgCGm_AB9J9Qh4DGgPYbj9fsUOpD0m42qDLf5rG-NvgQCAHUgUprdtWJjPDc6A389KYSj8m8sT0FEIacflPEPx5tBCJrTPwliX9woQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ: من هدف شماره یک ایران هستم.  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448955" target="_blank">📅 16:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448954">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3dcf56223.mp4?token=NqSfQXjURZtp1jRoiq8NwtsWGNb_xC46Ucn-cetA-wlv82xJavia_u4yEaRzemiDy82YUn5lY_U1air11vLLithFklmCzFM1jRfRwQoy5zh7Wb2_1noLiLFmJU9k8Q2j_Q52gcmxb2h_xOefIYFIJqXIUeg6sA7B_Dvz5E4c4EFOPU0jcEMBuuQg_ZkIkBIUSJd9DnMxAJ3SABuqZIMvQvo9-fg2s8-aDohP7ybvenHFsumUyluOyxcrp9f1MsGCIS1PeAHjAWemLPdaCDwnhOnnTkY4MRwjmkHX1LpMsTmrlcZDDem2h7rWSe_HwuDDdFh7Zn9faRQE8lHFuKiojw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3dcf56223.mp4?token=NqSfQXjURZtp1jRoiq8NwtsWGNb_xC46Ucn-cetA-wlv82xJavia_u4yEaRzemiDy82YUn5lY_U1air11vLLithFklmCzFM1jRfRwQoy5zh7Wb2_1noLiLFmJU9k8Q2j_Q52gcmxb2h_xOefIYFIJqXIUeg6sA7B_Dvz5E4c4EFOPU0jcEMBuuQg_ZkIkBIUSJd9DnMxAJ3SABuqZIMvQvo9-fg2s8-aDohP7ybvenHFsumUyluOyxcrp9f1MsGCIS1PeAHjAWemLPdaCDwnhOnnTkY4MRwjmkHX1LpMsTmrlcZDDem2h7rWSe_HwuDDdFh7Zn9faRQE8lHFuKiojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعان، کارشناس مسائل بین‌الملل: باید کاری کنیم که بازدارندگی به‌وجود بیاد و امام‌کُشی در ایران رایج نشود.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448954" target="_blank">📅 16:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247c2a33c9.mp4?token=hq-ti7cKXSP2Sy3d9GgDcCsKav2RDv5Y0xCYRQDFTfM34m6OtPaSjIYLPTcwSlS_xBk3wrf30y8QhV4N6L6_kSGMYWQBUCCUa2KXe69_CAWqEUc6dBY5Rz1d8_TLeKG-BO_CXbqQ89Cb84CnHZ_DYgRhkDSjlrpghVE1glUGUqC1AWOB_-WL5AfreW231IONQBdfHhcDKyWjsHNHKMAuq3V5Etxmq5SmeRIEDQ_ps7qQeC7eE_-BHGX0lNG_D4SECrAIZaPBCkorozniD-mmugkW4ke06wX5_maHOa4p7VcDIF6EqM-zVuJ2vkZeamo3CAFvx8NDOXYYO5fKCarvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247c2a33c9.mp4?token=hq-ti7cKXSP2Sy3d9GgDcCsKav2RDv5Y0xCYRQDFTfM34m6OtPaSjIYLPTcwSlS_xBk3wrf30y8QhV4N6L6_kSGMYWQBUCCUa2KXe69_CAWqEUc6dBY5Rz1d8_TLeKG-BO_CXbqQ89Cb84CnHZ_DYgRhkDSjlrpghVE1glUGUqC1AWOB_-WL5AfreW231IONQBdfHhcDKyWjsHNHKMAuq3V5Etxmq5SmeRIEDQ_ps7qQeC7eE_-BHGX0lNG_D4SECrAIZaPBCkorozniD-mmugkW4ke06wX5_maHOa4p7VcDIF6EqM-zVuJ2vkZeamo3CAFvx8NDOXYYO5fKCarvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمادهٔ روزهای داغ باشید
🔹
هواشناسی: از جمعه ۱۹ تیر تا پنجشنبه ۲۵ تیر ۱۴۰۵، با استقرار الگوی تابستانه، افزایش دما و تداوم هوای گرم در بخش‌های گسترده‌ای از کشور پیش‌بینی می‌شود.    کدام استان‌ها تحت تاثیرند؟
🔸
سمنان، تهران، قم، مرکزی، یزد، البرز، قزوین، لرستان،…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448953" target="_blank">📅 15:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0yNOkZTywr7bNOdUoAw_OvBEXaR8rv0qf-xkFHChShaHs1nfyD3cH-rpG_ZDGrzz9e4tXTG_KiQh5EmhOPyZ1qH8tBqWVD4gxyED_nnoAAM4xEWfCzsPTQKj7_BfQ0tuS_h24ScVt3fPZanY1ElzMoL21PdwyPqgqzH01FAm0NlUN44S55trtlOR8vt-rzrgNU-j35KbFe_IaVEbDlR11v-IhldgFXORaXDzfg0zvXTh-w35zDML-LYY2RCEXW7J-MnVTLjOJ1CHpQf0x233B4ZdXTwL16PgUj-HoM_L4_V08Eu-l57FPYigJCRvBot-BzTSstcX-yfO6P8QLEF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_wYwuNCWU3r9rWWDVaJZFMdVIWwpwNq2nsgWLsMOpMpUiwBhvjd_8drUMKtLKGbSNNkhXQhJWqydeXjW-F3McV2Vs619VV6C8tG7ixUa1XXn4tMC40N94HvLXq1DZtnQA19Qye_YMnM6Peo8xcQ9QWtvBhAUGTBE0X9SWQZZsArK73bV6mVoUQeigYHK55DS74t0j84JOzt4YtrXIPbNVHu3oeY2x1Zyk-VJEjzvwQKAFwh9uCuJhOYCpTSrbtK3wuFW-36B1jAFjwwuc3Cp298n6Mn9jYd_D1b7F7hJxMNFuiZNdJWs5Sc653D88JT3ZNmtCGG0yTQabixyK-ecA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72d7495a5d.mp4?token=i5_3-KKd8j70koynd5nD42n4aVx-j6WLiukRW7z_fXZXbvx7tYCTXX5lC1vASWnXakpY3tlnBkhLAbo6P-D9gSsZRgBmOeEbA7aupitFqod7do2TKeY_cfXT4Q3auqcpYBNI-Rsw6I8gayoZZ-w0wS5RCmGUjjdHh_Jkz6Qy1eRuP4wtA4wOMwQ24_e11kn5Xuxp842Wy2wRVpx3C0_vemma02PD-M6xv1YCVeMrGcw3zwoMaXOLEtz1ibAKaYR1oa7qL2lPxrnApzavCIR930cdAqhNbd5JZCbMibVCDWWslwrmXV2OjYssiiaCk8lg3NaMw7kDEiuiV5ZL1KkKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72d7495a5d.mp4?token=i5_3-KKd8j70koynd5nD42n4aVx-j6WLiukRW7z_fXZXbvx7tYCTXX5lC1vASWnXakpY3tlnBkhLAbo6P-D9gSsZRgBmOeEbA7aupitFqod7do2TKeY_cfXT4Q3auqcpYBNI-Rsw6I8gayoZZ-w0wS5RCmGUjjdHh_Jkz6Qy1eRuP4wtA4wOMwQ24_e11kn5Xuxp842Wy2wRVpx3C0_vemma02PD-M6xv1YCVeMrGcw3zwoMaXOLEtz1ibAKaYR1oa7qL2lPxrnApzavCIR930cdAqhNbd5JZCbMibVCDWWslwrmXV2OjYssiiaCk8lg3NaMw7kDEiuiV5ZL1KkKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حمله پهپادی رژیم صهیونیستی به یک خودرو در جنوب لبنان
🔹
شبکه الجزیره از حمله پهپادی ارتش اسرائیل به یک خودرو در نزدیکی شهرک کفررمان در منطقه نبطیه در جنوب لبنان خبر داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/448950" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5a0f0c0d.mp4?token=DcPtlzqtLwoWRmi0XLraOk8HCgzVMR3epCke6AGocpXopm4DO3rMZz4XMkvqB1TD51eNEUhwv2YxUYdiStYQyQYCihnKCxt0pGnMoAM4HFzouPd_6Xmw114-kwcPAWQ3sXMxsA6sCEiIXLzWS4qpbrzoeAmqw-vTkJhljBuCAAho88GRzpTQ-OMjdhjO0ZQADQo632_Od_9wj5vOBnPiAduYjnNjWC2nMUYoTGS_ykuyWKbmzLkxElGvuWDmWTj5OFVQFMcuPjEm_prpGxRS9QeR_Rjl6BF_FPHANKcZyhwrnhB1Xp9Z0zLMyQOO6WPUEdJwlAfLz6pCFDoPYsMRMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5a0f0c0d.mp4?token=DcPtlzqtLwoWRmi0XLraOk8HCgzVMR3epCke6AGocpXopm4DO3rMZz4XMkvqB1TD51eNEUhwv2YxUYdiStYQyQYCihnKCxt0pGnMoAM4HFzouPd_6Xmw114-kwcPAWQ3sXMxsA6sCEiIXLzWS4qpbrzoeAmqw-vTkJhljBuCAAho88GRzpTQ-OMjdhjO0ZQADQo632_Od_9wj5vOBnPiAduYjnNjWC2nMUYoTGS_ykuyWKbmzLkxElGvuWDmWTj5OFVQFMcuPjEm_prpGxRS9QeR_Rjl6BF_FPHANKcZyhwrnhB1Xp9Z0zLMyQOO6WPUEdJwlAfLz6pCFDoPYsMRMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آستان قدس: تا ساعاتی دیگر مردم می‌توانند به محل دفن پیکر رهبر شهید انقلاب بروند.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/448949" target="_blank">📅 15:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌ مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی(ره) حرم حضرت معصومه(س) برگزار خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/448948" target="_blank">📅 15:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448947">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bf9b3888.mp4?token=aW30tdy5TdMrocFqanRR29Wkc8l5uRRuFgsz0UmeoiUtq8JS3TMwdFMbkY5hPYCyWTCT-YLvVn9nWk36RZHkOIIlLUXr-XasuR7g4IHcGPWKGTbM05aJ_8fvwbn4sPxXTcmzQ65O7UiAFBQM3Sw1nD7Vsi-be1bSn_elEGAWJttjc3fG6p0JYTCkgnovbaMaRV_kO5dKi7MnVeAKHC5CUHqJS_L92SwBTwyhRFZeM_WSxfNcMqz0F-9BMHjQcbEBUGXU8YU47bZuc2LODYC95E1X4D_-QJXuftTZDegg98AgQhV8hlNFFAIAAcxG5bRPdUhL3Bmo2j49ec3CKN2Ssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bf9b3888.mp4?token=aW30tdy5TdMrocFqanRR29Wkc8l5uRRuFgsz0UmeoiUtq8JS3TMwdFMbkY5hPYCyWTCT-YLvVn9nWk36RZHkOIIlLUXr-XasuR7g4IHcGPWKGTbM05aJ_8fvwbn4sPxXTcmzQ65O7UiAFBQM3Sw1nD7Vsi-be1bSn_elEGAWJttjc3fG6p0JYTCkgnovbaMaRV_kO5dKi7MnVeAKHC5CUHqJS_L92SwBTwyhRFZeM_WSxfNcMqz0F-9BMHjQcbEBUGXU8YU47bZuc2LODYC95E1X4D_-QJXuftTZDegg98AgQhV8hlNFFAIAAcxG5bRPdUhL3Bmo2j49ec3CKN2Ssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل راه‌آهن: تمام اراضی واقع در مسیر خط‌آهن رشت-آستارا خریداری شد
🔹
درحال حاضر بخش اعظم این اراضی در اختیار شرکت متولی احداث راه‌آهن قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/448947" target="_blank">📅 15:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe53a547a.mp4?token=Sd-01QG0Psf65ViCeIyij01oz5acNIL1giOyd8tcBd_EhR5WnRip9hTIbgyh9DDzvw2A8xCIxxt6TUKSVarKsFzBN_C2Z_AT06e3vvAWPv-zlySwVt1xaRSNctzNGc5ADTpvbz69NUvd-vrmutjT45Kg5JwOJbuCNls5VbrSQULkzNa1OJWt4-6MUR2_gM81tMGr1k6SdAEerr19BPX1rV0XA8vQe2gbxG1FbJAedz43Flr9tReK_puBPFGZCmhUnHjTw76d1NxoJjY1Y6eaD3DPGnTkSrnK4JG3OBo5qyk79vr-2BU7OiwIbmY4Bhtcoi6vHK_5XUTM76sluXe_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe53a547a.mp4?token=Sd-01QG0Psf65ViCeIyij01oz5acNIL1giOyd8tcBd_EhR5WnRip9hTIbgyh9DDzvw2A8xCIxxt6TUKSVarKsFzBN_C2Z_AT06e3vvAWPv-zlySwVt1xaRSNctzNGc5ADTpvbz69NUvd-vrmutjT45Kg5JwOJbuCNls5VbrSQULkzNa1OJWt4-6MUR2_gM81tMGr1k6SdAEerr19BPX1rV0XA8vQe2gbxG1FbJAedz43Flr9tReK_puBPFGZCmhUnHjTw76d1NxoJjY1Y6eaD3DPGnTkSrnK4JG3OBo5qyk79vr-2BU7OiwIbmY4Bhtcoi6vHK_5XUTM76sluXe_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آستان قدس: تا ساعاتی دیگر مردم می‌توانند به محل دفن پیکر رهبر شهید انقلاب بروند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/448946" target="_blank">📅 15:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNL0GyZcpFao4SlY2IJyqIv-qMk5dEDzAlGAIXSMVyjfD4s_g6xNFSl_Z7f7SV4NkxcsEETbPtOAVvMoTmJIRXKtxCjDe03_tNUDmfZTOS0aOcpzwH6V99noRhfZwyXT27rfpUPWfdTbTxK2gyEZEZcmapIEhec2BjBohD7Wm4pdyHhSk-StQ3_i4qveBSa3HoRcbHf8wTDfb90WIIWY8qYro8w2OS0lQ5dIGMeNu-vs8w1hZdQmXSTYrueeiN13AuVA4KEY_hmJHozwitXMO8KVFheV038yluVk7XhVU5v73D7LIbzQt0nZ4ql63J-rDRLgNddGVH87PMUfdrha-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دبیر شورای‌عالی امنیت ملی: با حمله به زیرساخت‌ها مقابله‌به‌مثل خواهد شد و رژیم تبهکار صهیونی هم از پاسخ رزمندگان در امان نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/448945" target="_blank">📅 14:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f38d90462.mp4?token=uL7cxqjdd2Z4V6URIxoPdHt3WQW18c9drjCYJ2qoG9oonwu3ZG0UN5SeZYBa7BssvG5XsPWWtEIvB5sOAhfABhuBfodcqSrrppHY2aSb3jIUshT7qRHyBetMAcE7YM-S7fSObZzbWu-xmK_2vLEkXK-qygOLJNiUu1nTm6xCLnvGsllVO6IKPq5pomXtOeq8A80KAENen5ISNy-g83jegJxThHCyR6CXywKqnoGG7NwygvMhGMcBafbHue8GjvTmzbbVEA2OGAL0q6NyKRQsO5SskN-3NqetV2DdoLIDkvxB5soPMndxzHDURQ-1GqSsjDETSyPqEJkFIX-8BRIIkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f38d90462.mp4?token=uL7cxqjdd2Z4V6URIxoPdHt3WQW18c9drjCYJ2qoG9oonwu3ZG0UN5SeZYBa7BssvG5XsPWWtEIvB5sOAhfABhuBfodcqSrrppHY2aSb3jIUshT7qRHyBetMAcE7YM-S7fSObZzbWu-xmK_2vLEkXK-qygOLJNiUu1nTm6xCLnvGsllVO6IKPq5pomXtOeq8A80KAENen5ISNy-g83jegJxThHCyR6CXywKqnoGG7NwygvMhGMcBafbHue8GjvTmzbbVEA2OGAL0q6NyKRQsO5SskN-3NqetV2DdoLIDkvxB5soPMndxzHDURQ-1GqSsjDETSyPqEJkFIX-8BRIIkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد ۲ پرتابه دشمن به اسکلهٔ صیادی بنود عسلویه
🔹
فرماندار عسلویه: ۲ پرتابهٔ دشمن به اسکلهٔ صیادی روستای بنود در ساعت ۹:۱۰ صبح اصابت کرد.
🔹
درپی این حادثه، ۱۰ قایق صیادی مردمی دچار آتش‌سوزی شد که با حضور به‌موقع نیروهای آتش‌نشانی شهرداری چاه‌مبارک، آتش مهار…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448944" target="_blank">📅 14:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02b60bfa8.mp4?token=IlHvCQ2U943-2-FOTTtWSKSwBa9AIrANHgdsD3R1ejhPNyjyjdEmMtrtmt0Cb-O1_WvTbEor-oXup-JGgixSg7WDwDEyzFUdLEiuzOun23R-EEaBzwosmwFg50NI6xhVuOBP8uJ_ATDOFp3RCqocD4UOqmeH-Ravan5NNTDjhyuqrEb6aUCSoxeGr4QfzupO6ogIxZddEzaxW1NUZ125z0YAdOdFjxO2MsGTVWK1zZaChSpcCUCmdY4D0PfSrXLeHFzOSXlAsYVfnD69o4217kB800mgjHaPegkCzPs7fvYKGaxT5ZwvbU0R42twDDTHgja1zHnvseLW4KvArdcnXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02b60bfa8.mp4?token=IlHvCQ2U943-2-FOTTtWSKSwBa9AIrANHgdsD3R1ejhPNyjyjdEmMtrtmt0Cb-O1_WvTbEor-oXup-JGgixSg7WDwDEyzFUdLEiuzOun23R-EEaBzwosmwFg50NI6xhVuOBP8uJ_ATDOFp3RCqocD4UOqmeH-Ravan5NNTDjhyuqrEb6aUCSoxeGr4QfzupO6ogIxZddEzaxW1NUZ125z0YAdOdFjxO2MsGTVWK1zZaChSpcCUCmdY4D0PfSrXLeHFzOSXlAsYVfnD69o4217kB800mgjHaPegkCzPs7fvYKGaxT5ZwvbU0R42twDDTHgja1zHnvseLW4KvArdcnXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین پیکر رهبر شهید در پاکستان، تایلند، بحرین و نیجریه
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/448943" target="_blank">📅 14:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9Q3dds1lKCWyzjRGhi70Xs4uC6ie1iK3tN-Cb4kL9ralt7oBBWpQpysfq1svx9I84VShht_ZwavNOYqmLwju81cNjQFWRjKV-rInBFYeSJh0cUhCBkdrljfxm3NR2vh_AJVsSD1mlG_O9R2HdB8bFoXer4w5GmwFYJR_kPuaHyOfx4qeTDKcv1xoMP25oS9wgQhAA5C_TyVJJ1NCg8OiC-66ZS1h9ULSFcsSHC_-O_dZUrrK7QSgaOfsvGevI1kLYgzdcDuOeohHFLfWIMyvtpGI3zaggecvEQCO1s4AOSjwa4uAZDJ9x_dT35IRgaA9p8ezdW55EvG-cRUI5wF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاغی جدید فوتبال ایران؛ جلالی پرسپولیسی شد
🔹
با اعلام باشگاه پرسپولیس ابوالفضل جلالی، مدافع چپ پای تیم ملی و چند فصل اخیر استقلال، با عقد قراردادی به مدت ۲ سال به این تیم پیوست.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/448942" target="_blank">📅 14:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmPsqrtVvTzYi0RKdjA2SnYUtsxZz-Emk5PlF2cimEv5GIAZuJ2ThAYFvNcnJ4Kafw7EonNkkrg56Bi88vjAIeZ2aqkRXlFU2We87CbbFGqGoIzMuueKpGeinrmSQsE7w98BOLLKVvo-iaEOwZ_ovQV77OcURXaYD-47HJLCtLUr3JbrPHAC3NKfY6t-mZmxArjN0zyWpjc_uO51nvgxQnetpXqFPacrIyAfxiywsr35mxX4TFsSO0TuiUbWqWWcIpZs4GcD5AvUxGYMmsyRjxCMwL-u2ZO53fX2cF5xXdZ45VjrUzgEQSnme16Voe7QKZQ9QeC-VbSMlCY4L6y43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت!
🔹
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/448940" target="_blank">📅 14:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b35dd7c4.mp4?token=kwMXUaUIN_ISmKLy_Ll_K_9UwUQ79lyz3P_Xk8mzzFy7SvviLlklrIgBbpCRXWmiPb8R3zog8FGp_nYo2YoUrgmeaNFC0DSXeBbRpDVnmpwMMAcn-tEzd7zIB8pMNULHWiJXLcaKEmvtlAMnGZcYtzlmcOLf1zVU6tpPH-BXDRKE58TCJ-vdAsnoMUFxWxvy3I3sIfoEV9qO4zl5aQ8d05mlsT0PFATBnghXtDeolxbifJN0jiPUu2W-WNcGJR0Yjn1Cw32Kv5u0RNwcOboJkLeV1nCiK3etjTsVPWTpQj2PukOn4c47lfQU6u1rq7meCGP8tQFvix3gGsHxxlr2sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b35dd7c4.mp4?token=kwMXUaUIN_ISmKLy_Ll_K_9UwUQ79lyz3P_Xk8mzzFy7SvviLlklrIgBbpCRXWmiPb8R3zog8FGp_nYo2YoUrgmeaNFC0DSXeBbRpDVnmpwMMAcn-tEzd7zIB8pMNULHWiJXLcaKEmvtlAMnGZcYtzlmcOLf1zVU6tpPH-BXDRKE58TCJ-vdAsnoMUFxWxvy3I3sIfoEV9qO4zl5aQ8d05mlsT0PFATBnghXtDeolxbifJN0jiPUu2W-WNcGJR0Yjn1Cw32Kv5u0RNwcOboJkLeV1nCiK3etjTsVPWTpQj2PukOn4c47lfQU6u1rq7meCGP8tQFvix3gGsHxxlr2sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حالا ما شما را نمی‌بینیم و دوستتان داریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448939" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjqh9EBuLFt8-qtQEbUE0sWSIHTgbS9AZ34T3Jp9EyFhaBdcdpF19Xa6lBWEr0YK9F8iT8IHYtECSNDopdKqvnhvI-09272MpRqK3GJjrAA6uaSkoEHfZm1vCo2ZU0aCcRxeIlcY0zhQdBk6PK1nuXNAljJIvf8bM4RyMIY_7J4qIk23ue7bYiEMko95wsq84cNZIxlV6WI9dhUGPWm4PusVxJKM6CgBHbQ0RcY8dAY93dR6yQmu9kVKyfrA9Tw95O6_LF86RYCNHEU455NnJw0IszusHSCahoXg2UQhiKlvyi-Kaikomg5b5dSUfziI9rfig0BLzhIwlWKxDV95iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر خارجه، رئیس مجلس و شماری از علمای اندونزی برای ادای احترام به رهبر شهید انقلاب وارد مشهد شدند.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/448938" target="_blank">📅 13:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57cc189e49.mp4?token=opA2LIWRhYiNgbqPpZrz7tiOmzUR3hlXurWVvQ57q1VzVd2iGahjMDoVtF8ZmPtj9hzsPLbnFBV3EAyFvbxDNGYuu9hLxCpt7TdQoo_pF7nIvK7KFNSaVrYIVoH4CWqS9cmlwWSx4oEhvw0aayQ3t1L0v0kX4MYRgDiJra1PVRj3iY6N8Go7rAa6g0xli_kymCfawuSViulicjRYxdUCWwLzps6l8ZhVt41PwxIa_wgdyb-dJPAUdJetTawsUJIk2rhukUdtuOEbt5IBB7lNRX-RQ568A_2FY_mZ4OxfIEdxIOA7ty38izoyEXSEryltyavWYGlQAupfLzL0NFbAYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57cc189e49.mp4?token=opA2LIWRhYiNgbqPpZrz7tiOmzUR3hlXurWVvQ57q1VzVd2iGahjMDoVtF8ZmPtj9hzsPLbnFBV3EAyFvbxDNGYuu9hLxCpt7TdQoo_pF7nIvK7KFNSaVrYIVoH4CWqS9cmlwWSx4oEhvw0aayQ3t1L0v0kX4MYRgDiJra1PVRj3iY6N8Go7rAa6g0xli_kymCfawuSViulicjRYxdUCWwLzps6l8ZhVt41PwxIa_wgdyb-dJPAUdJetTawsUJIk2rhukUdtuOEbt5IBB7lNRX-RQ568A_2FY_mZ4OxfIEdxIOA7ty38izoyEXSEryltyavWYGlQAupfLzL0NFbAYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین رهبر شهید در کارگیل هند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/448937" target="_blank">📅 13:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c410869c1.mp4?token=d8s_SWd_aTTzEDT4loXd66D2zitGO0R3URHU2jVyRycU9sihA4F_4ElGNjlcQ-qymptCopEXtXbVVvaTk7VdRHdX8MYh-nLPtCye4y3qj2v2mdG6viZHbk0O8W5jbHzDrc3I42xCU3YQUswz0Hp3ykN5IRCRnfCdjgFv4694O4TnplQfwa4UgwYd59dUqnHYAumdwnAeLo5VKMnlmDk316O9GYloLwVPBZOlvnFC5RWaDyu_1ammXhTSrN8AMpDzAGp5WLsTwc6vN6dgi2_4ZhNgR2a6zx1pO5WdumTZCNWKibHDtGmCeZbmaNRszCckTfjItvwkLt5OqvjWJSeYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c410869c1.mp4?token=d8s_SWd_aTTzEDT4loXd66D2zitGO0R3URHU2jVyRycU9sihA4F_4ElGNjlcQ-qymptCopEXtXbVVvaTk7VdRHdX8MYh-nLPtCye4y3qj2v2mdG6viZHbk0O8W5jbHzDrc3I42xCU3YQUswz0Hp3ykN5IRCRnfCdjgFv4694O4TnplQfwa4UgwYd59dUqnHYAumdwnAeLo5VKMnlmDk316O9GYloLwVPBZOlvnFC5RWaDyu_1ammXhTSrN8AMpDzAGp5WLsTwc6vN6dgi2_4ZhNgR2a6zx1pO5WdumTZCNWKibHDtGmCeZbmaNRszCckTfjItvwkLt5OqvjWJSeYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جلیلی: انتقام از دشمنان، حق ملت و وظیفه مسئولان است
🔹
ما در مقطعی حساس هستیم که آنچه فرجام این رویارویی را رقم می‌زند، میزان تاب‌آوری جبهه حق در این جنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/448936" target="_blank">📅 13:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209e6e3e83.mp4?token=YpurOzgbOccEAjWQGlokyMgocraYmShYJ1ELfooc7yuadY__p_MAUCb1MmfDA6X-p04gHDSv6FA7HsJ4hboyytbnTiTEh4T1TBCbJQCe-dfvGTYaz2vKzKdqC1Ps5QCVbIQoGSiPnwy7cx0GkcttiuHRqJOEP48RJecC3I6foFADCflkckPE8N4wXElJ8kUvJ0JL94dgY7cconJxeBSk2bLRPDcNr5BZ2Frz-v1-QjG398za4FiSExf1R7ind-tsjL8jv_bOceNFj3OlCHhXIW1IID45XE-MLcDkyZs6z5jRTW1yHUfAJS_Ltp34WLLEk_WtV9C0j-hwyV5Sw4EBbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209e6e3e83.mp4?token=YpurOzgbOccEAjWQGlokyMgocraYmShYJ1ELfooc7yuadY__p_MAUCb1MmfDA6X-p04gHDSv6FA7HsJ4hboyytbnTiTEh4T1TBCbJQCe-dfvGTYaz2vKzKdqC1Ps5QCVbIQoGSiPnwy7cx0GkcttiuHRqJOEP48RJecC3I6foFADCflkckPE8N4wXElJ8kUvJ0JL94dgY7cconJxeBSk2bLRPDcNr5BZ2Frz-v1-QjG398za4FiSExf1R7ind-tsjL8jv_bOceNFj3OlCHhXIW1IID45XE-MLcDkyZs6z5jRTW1yHUfAJS_Ltp34WLLEk_WtV9C0j-hwyV5Sw4EBbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای این دقایق روضه منوره و حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/448935" target="_blank">📅 13:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlocdPjLXZqld18CvTavrRWCCUNrOGB8RWtjLFshyQEhfuHZPlqiNfn9Ptdyb1r5vH8OSPHyKDddcimOwaxOvsrLbHXlTfv33AIFcMvstYTZS492E3t43Wrio85i5tFE924322J8R1BgJ8TYF1hdT4LIEqF5CcDZ-Dscea-jafk-NNA-v9RdrX2P-hbkP3E-jY6I7oikGkV4afSz8N8NAfO6O9B_Un5W2AnVHmdxpZRV5OgYdtxgZqHQ74VBlWhl29FDNdFMvaR3OJxcb4xGzZpQYKhpt3P_QgxOlHwMf_Ioo2yDvkaxUpO-wfhOPPlTbdNjZyT2uXsi0IPs2_r1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوترابی‌فرد: تشییع رهبر شهید نماد «صبر جمعی» ملت ایران و عراق بود
🔹
امام جمعه موقت تهران: اجتماع و همبستگی مردم، قدرت‌آفرین است و اقتداری که امروز جهان اسلام از آن برخوردار است، با گذشته متفاوت است. این اقتدار، دستاورد صبر و ایستادگی جمعی ملت‌هاست.
🔹
دشمنان اسلام، به‌ویژه آمریکا، سال‌هاست با زیاده‌خواهی و سیاست‌های استعماری، ملت‌های منطقه را تحت فشار قرار داده‌اند. اگر ملت‌ها می‌خواهند از یوغ استعمار رهایی یابند، باید استقامت آنان بیش از دشمن باشد.
🔹
حضور گسترده مردم در تشییع رهبر شهید نمادی از صبر جمعی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/448934" target="_blank">📅 13:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f74d80bb.mp4?token=RzsPn552KnKBCsXEYZV_Jpgblqk_7mpkZvtnOpXellNZeFWuLnUs6jxqQ5CLwxhdMGFbIU7yxg6Ic1LPARJWI17Rt7f67C6dOmr0be3SjzeQaL8EWx8KTQxsQYSdWGy1N7e19CKC_J0svgGKjD23KexAMNWv4-OeOARnO90NUT4D6KN16_F7d8zjh7RJ6mVKtWp8FaQynpbHts8_mFt3k3aEwX35sOUXFmvqzCrqaC1YXcptnc2L506dUQtfBRhy18aSTtLC-ylZdtYX2wK2b6I61mR7ZVhDbJSbmMtUaX42o_ZKacLZUWHBz8Xost7Ly1dTJgs4A3ftAGXP6MQA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f74d80bb.mp4?token=RzsPn552KnKBCsXEYZV_Jpgblqk_7mpkZvtnOpXellNZeFWuLnUs6jxqQ5CLwxhdMGFbIU7yxg6Ic1LPARJWI17Rt7f67C6dOmr0be3SjzeQaL8EWx8KTQxsQYSdWGy1N7e19CKC_J0svgGKjD23KexAMNWv4-OeOARnO90NUT4D6KN16_F7d8zjh7RJ6mVKtWp8FaQynpbHts8_mFt3k3aEwX35sOUXFmvqzCrqaC1YXcptnc2L506dUQtfBRhy18aSTtLC-ylZdtYX2wK2b6I61mR7ZVhDbJSbmMtUaX42o_ZKacLZUWHBz8Xost7Ly1dTJgs4A3ftAGXP6MQA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت مردم از ماندگارترین سخنان رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/448933" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaaa-sbE3-aajWx_MeKeclhQIGkpyXzxziJ5eKx8_bZjnTGfxkEF8UeAY7qK_hNue9sKBoDOw-yd4vzZC2b0kkUjOXujnCtJEvCQCbl4qpx1c5ajFOFLZKPW9t6RSbLg6TSQea6AreKMCIbBvkL4ur2XAvMAyMmMdwdE-8R6lyJdflq8C2MCx76pPH9UqnIq1g5fqru_tY7al5hQytAGfCyBch8Nxk7AmYdLtF9GyrSvodvb3SsfV3aJpyHbTkiVj8FSPrbdZWQdVwWBGAQGog7Hw2OHNLdHq28XPkM8_bOt8eIcxoUNR95QhS9mZYTYdFs60QQdIrtTOr0PVJIt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز‌های فرودگاه مشهد از سر گرفته شد
🔹
بعد از محدودیت پرواز روز گذشته در فرودگاه مشهد همزمان با تشییع پیکر رهبر شهید، درحال حاضر پرواز‌ها به‌حالت عادی برگشته و درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/448932" target="_blank">📅 12:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448929">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mj9ZPe7qvxJqKOnorfSLHawyKu9d2M84syOwUKLuAXkZ4NmoJXbYXrq_zfkXuoNlJBeshKzuaLSz_WfUYQcfaLU6TIE8arb1lPlPV7wpRSeVWZTXhx8Fjfc2e4fRKirBFwSBsgZtHuTE5_w3cZ4eJrtsmJ_7iRFKayZ6PISWBRqE2XWR59VOeUdPIuRyuBFfH2kvkUe_8y5rEE6nJ_8fB5n434IQ7EKwUTRizKtWdj-eFLY1l3O43_3VEZ66AKvDpEqR4W58g4pYpy3q-mraL1_OP2TsqLRdC-wwxr2yW3NcJ8arr-E9SKx2usXuSAUUmx54mdYLdqxrS8Mcf8kykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pafNMtrS5vVa59Qo-2HU_gOE-bYI3sGP-OpYlGHFWfJrCrC1X6YVM7B-_KDhX4TIfkT3M_4hIycRVvQdA4kr-ThGKW3ldNEZCUgVYV1JH5zccTt0vi5ClTEvkyRgXFGmpplvd51vEim_Loel2aAdobvADgzpQDT5uEqfPXmIx0dUTHdtPvNRg8c4WUoM6rkf6MPPecekVHKLhdvXLhMBJa4h8hAKIwQPMVMtnoEro_buPhDrCsLO7QObHq1LX5bD-h1E7lM24pTjyw6oJ8-0Nsn7LH-lr3nKFXjEcPVr2UOpPm_yCT1cyoRgL9zso9iQL7MVgPW3eMyYrds27EM5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3-njY6d3YzbVymKrt3EB19TLWwqUZoeYTm6YcXu4I_qUbv3B932jKKR-92B51GVlm2usyFBdzQ5JnZXfB4QZGTSncyUHHTE_XhVbZOlzPqnO-m1Lx0YH9laWknO0kAUEpdTiq7hyivUSWewCgPpyH1hUWaB9IeHMV8u8dAumbBKvqnaTdMCUmnUrkmRGZBpIa3VEy_C65JKNcGYd_rKlWxqUoI66fYawzinzKdWE95FgvJrXeqSxguSm2avkbTBefjdVqmY4aALbRyHQ2W86FylqQZyoD9CrvaXQ2AP1_ASobcLy5znp3Eg3_FJ3tQCiSic0DoLo0Tw1ZNe4UlIIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
کودکی که به زیارت زهرای ۱۴ ماهه رفت
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/448929" target="_blank">📅 12:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448928">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4926d659c.mp4?token=lNuJqSZ72mgUs62qZ3Cr08yrz5qzlbJT6SZiR00JVhofhWjz8EdrU3SSnRUXaoQI_MQVJe34INLSGN1iEsxjaYE76M_AQsYX6Li114kkY0j31rXO53M8JUEaYnsChW9FIlDTt60HFZafypbKx8z-K5Euj15lPD4z_KlwSYVkXccePv6kIqBHZF29zKKZEK1kdvS98LgDtvPZnrt00RCHxzt6HupKOdgwWi3V2XbvJU0WnLdvEBkcNABLEfmJAQXYsHHRXzVMajAqtr6vD_EfZq9MV1CCAZHtCccxVls5PA9DdYXZBm-5w2-JDFhMyxhi9rB5_3yuHutwfE0_4gFsPjtpmoVEMxjOJqyvxv7ikE85l48Gg8Eng6zA7NR-nM2NGeyZKvDTPWCSNnOPz9YvuZx5W3wF4E63LGZOuebheAh1zxJwMHQEYRGaukKl2VhwRqBeaG8EBG8J4k_68sXUstlho3ckMI2enOOhaISpkIAna2RMICcwXS036o-HLtB8hpgudOP7Q5CA4lVwB56Axfzp85QU6b-Aji6cfFiRx1l41XfUVUuKA7H4HUkEnWEMAydaN9pLDaiJ77oKfE4hqSIF22Agy_DkNAMTJIb9CIV7e7bYtWasG348FORHYtQCf7pbO2KpRlgv8xlQ5lqQ6tQAFAop3BzEhh6r7rLG7WU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4926d659c.mp4?token=lNuJqSZ72mgUs62qZ3Cr08yrz5qzlbJT6SZiR00JVhofhWjz8EdrU3SSnRUXaoQI_MQVJe34INLSGN1iEsxjaYE76M_AQsYX6Li114kkY0j31rXO53M8JUEaYnsChW9FIlDTt60HFZafypbKx8z-K5Euj15lPD4z_KlwSYVkXccePv6kIqBHZF29zKKZEK1kdvS98LgDtvPZnrt00RCHxzt6HupKOdgwWi3V2XbvJU0WnLdvEBkcNABLEfmJAQXYsHHRXzVMajAqtr6vD_EfZq9MV1CCAZHtCccxVls5PA9DdYXZBm-5w2-JDFhMyxhi9rB5_3yuHutwfE0_4gFsPjtpmoVEMxjOJqyvxv7ikE85l48Gg8Eng6zA7NR-nM2NGeyZKvDTPWCSNnOPz9YvuZx5W3wF4E63LGZOuebheAh1zxJwMHQEYRGaukKl2VhwRqBeaG8EBG8J4k_68sXUstlho3ckMI2enOOhaISpkIAna2RMICcwXS036o-HLtB8hpgudOP7Q5CA4lVwB56Axfzp85QU6b-Aji6cfFiRx1l41XfUVUuKA7H4HUkEnWEMAydaN9pLDaiJ77oKfE4hqSIF22Agy_DkNAMTJIb9CIV7e7bYtWasG348FORHYtQCf7pbO2KpRlgv8xlQ5lqQ6tQAFAop3BzEhh6r7rLG7WU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت آیت‌الله علم الهدی از ویژگی منحصربه‌فردی که رهبر انقلاب دارند
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/448928" target="_blank">📅 12:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448927">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2fa10f04.mp4?token=Xa6IHbq9NmKMKDx8CcQICYCTLPBOSN8VtHFvVRcjwMz5Dn2dtGlxSvstr0NOuLYZrugFv-YykeiU6x7llK_kK9meiRbkhTc3j-Y7mipnpEZXs6yUpvN7JUVW3QiMZQXykHbIhgEJ6xI-SgfpeT0VaRMzxZ1fk-ZtxCYgKD3jlpY9Ld8zUYuVJJeF06JdT_QAOl2eBoyhVYnV5fOb0hXJWzx30H2GBfeSyT2rShmlP5IS1TUJGJYHz-zyj81UxUQbOugAziYpFMayh2txL0874WqGgrSp0JKYFrtI25DA3Ne4uUiTWAi4jHvJg472cMaBcKL6fH9iFZnqumJLAtGJjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2fa10f04.mp4?token=Xa6IHbq9NmKMKDx8CcQICYCTLPBOSN8VtHFvVRcjwMz5Dn2dtGlxSvstr0NOuLYZrugFv-YykeiU6x7llK_kK9meiRbkhTc3j-Y7mipnpEZXs6yUpvN7JUVW3QiMZQXykHbIhgEJ6xI-SgfpeT0VaRMzxZ1fk-ZtxCYgKD3jlpY9Ld8zUYuVJJeF06JdT_QAOl2eBoyhVYnV5fOb0hXJWzx30H2GBfeSyT2rShmlP5IS1TUJGJYHz-zyj81UxUQbOugAziYpFMayh2txL0874WqGgrSp0JKYFrtI25DA3Ne4uUiTWAi4jHvJg472cMaBcKL6fH9iFZnqumJLAtGJjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
البخیتی، عضو ارشد انصارالله: یمن ملت ایران را تنها نخواهد گذاشت؛ ما دشمن دشمنان شما و دوست دوستان شما خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/448927" target="_blank">📅 11:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448926">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI5iqxzFZjbxVs5XksxPrnoxnoBSDf5BIgPTCb6HKvCpZqoaH8dOoZ9vF0wivjPOnQxFWd6BiYZ2k700oT3UhnYqGOacYGdbOi73HA8HYIbcQaAmnMfe5nlM3I-WWnq0Q8cb-BKzI5fB_PWyHRam5J3bA9sLUJHd-L_Efdu7-z8PxPbf3sYkkyjLSyxsBMquVMpIHefALx4o70mEyLmLWxMbb-hSThyo7xPjMyovQSsWY054WIwA5Z3i2J5Eabd88OgkEOuCfXjA-YRSST_oRKLd3gGva_nxcUDVmSm0HWou3IBQg2Xz2GinnbPyL_c1Y6qhEmB7_pHxlDCdj0jGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه اس-۴۰۰های روسیه را به کشورهای خلیج فارس فروخت!
🔹
یک روزنامه نزدیک به دولت ترکیه گزارش داده که آنکارا سامانه‌های پدافند هوایی اس-۴۰۰ خریداری‌شده از روسیه را به یکی از کشورهای حاشیه خلیج فارس واگذار کرده تا راه را برای دریافت جنگنده‌های اف-۳۵ از آمریکا هموار کند.
🔹
عبدالقادر سلوی، نویسنده روزنامه حریت ترکیه، افزود که امارات متحده عربی و قطر از جمله گزینه‌های مطرح به‌عنوان خریدار این سامانه‌ها هستند، اما تأکید کرد که باید منتظر اعلام رسمی ماند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/448926" target="_blank">📅 11:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448925">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbPcpP4JZvKr1jsEVIhYpu2SxT4000Q4dSDMAhTVmXB3CmxTDE2WiPUgrWxOJnZPqsDW18HULZqZOZ4CWlEN_PB2K-CUh8ujakeym_w1jfw5o-xQGnEbQpw-MhMSAqzrC6CN3J7Gtol1dp86ehDWxfZ2u8Cy6WLJOCT-j5tPCe3aRMDVe3rkXGo8EnTvMltq0fK4gOsbegOhsP2UrjH4CaSWPxl_jomnYZGDWu3RwYbOq0FzPbHEnPPNpDdYYosFlXegL7u-ZmKn0hxefDXOKPRH7lOv_jguXgi0dJddPWwWNYlBn4oKAmfrq1lRAbhnT8q4aPmjEl8j2js86l_lvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پیش‌ثبت‌نام حج آینده رایگان شد
🔹
پیش‌ثبت‌نام حج سال آینده ۱۲ روز دیگر آغاز می‌شود و امسال ایران ثبت‌نام اولیه را رایگان کرده است.
🔸
پارسال متقاضیان حین ثبت‌نام اولیه ۲۰۰ میلیون تومان علی‌الحساب واریز می‌کردند و هزینهٔ نهایی ۳۸۰ میلیون تومان بود. @Farsna…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/448925" target="_blank">📅 11:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448924">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فرمانده کل سپاه: خون‌خواهی رهبر شهید فراموش‌ناشدنی است
🔹
سران جنایتکار آمریکا و همه دشمنان انقلاب اسلامی و جبهه مقاومت باید بدانند که با ترور ناجوانمردانه این رهبر الهی، هرگز نخواهند توانست نور الهی را خاموش، اراده ملت‌های مؤمن را سست و پرچم مقاومت را بر زمین افکنند.
🔹
خون پاک قائد شهید امت، عهدی جاودانه بر دوش همه آزادگان جهان نهاده است و خون‌خواهی شهیدان و مجازات عاملان، آمران و حامیان این جنایت، مطالبه‌ای قطعی، مشروع و فراموش‌ناشدنی خواهد ماند.
🔹
این مطالبه، تا تحقق کامل عدالت و پاسخ درخور به جنایتکاران به‌ویژه ارتش کودک‌کش آمریکا، از حافظه تاریخی امت اسلامی و جبهه مقاومت زدوده نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/448924" target="_blank">📅 10:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448923">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hev6S6L7Mh36R_faKV1PYAHiqBiQQ2RVWTJzq_d7c8faGgGz2p2dVzQ1pNON3j7bBw9zMcSUcGdGWo_Xt7oLVk3apaOtAkmEiIuwpgdmpxwFBn2geDHBW1Ww8dVUUzAd_l1bYPRMroi0FQZDWPcq02Wo8-Hb0LnlVr-dTQFb9V1AlYEQUOGXymxVdfmyzjNyzNkLP7avYDQsRKFNB2yNtsLZB_1m_Ux989LEB8PT9yCHGCILq7QOAQDUBMbtFJFsVRhBPl4xpwheoLzC7S9fRXxl5RjqVMeU4FksvxP93YnNir-o-XX_Oz569KXwGNs6hoIWS4xFves5pzdxWJs16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام بیش از ۳۰۰ هزار نفر در سامانه سماح
🔹
معاون عتبات عالیات سازمان حج و زیارت: بیش از ۳۰۰ هزار نفر تاکنون برای حضور در راهپیمایی اربعین در سامانه سماح ثبت‌نام کرده‌اند.
🔹
بیشترین متقاضیان از استان‌های تهران، خوزستان و خراسان‌رضوی هستند.
@Farsna
- ‌
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/448923" target="_blank">📅 10:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448922">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRZcUthf58vBCuBEGACdwdyTh72Jazm7XVtQM5EN-V8sii_OB1OwtCOp_-qkba7_HpWBjxD173LLgwL-_ahXYWcS77awWBpnl5qFQPZcbgmP-pcW1ZFn_pjC32ZFUBwp2ehcS4R_MCkRU2DdGcWF89-ahlILqfvENit7bu-9lqU_9otSOLcdZdC3qm-pMS_RfHRA6g6Zot9BJ6Q75Gucn1p6m7M0LKnaVc1vVe5E89GNhKsVVUtlKkUub4V3_cyOjNruE9J1xgwcDkuOyQiS4gLuAShvYadmshzb7MGR4AufgN6YSXXxpUp68lROeZQovB4vDEkCcP28574bzSIrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر پاکستان: گروه‌های تروریستی از افغانستان وارد پاکستان می‌شوند
🔹
هند به این تروریست‌ها پول و سلاح می‌دهد. برخی دست‌های خارجی دیگر نیز وجود دارد که نمی‌خواهم درباره آن‌ها بیشتر صحبت کنم.
@Farsna
- ‌
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/448922" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/574b047b5e.mp4?token=P1dIjEtaRpvXvdkDwlBLY-dznTQAl8hAMV9MbD3qMzQbhIJgqA-W8wq2pz1TmvS1Dnq64Erybs3AyHM3Y61h7qL4n5I5KT2uqB0eab4bgO8ULu9cbz-zcNyg_irLBn9otmdcnE8sb_6DqVIaHBx0hBGZkKm14Qln3DNIEVtWKmt9EKNpa7j-LToSR6vJdUh0RNhw4vFEU21f4fczuv_uJ9lQ9-2iZqoviYvb13NtleDJOTnnClc1B44LB52fnJlquvlCP4nlkFs9vMo6IRLRlOIiC1G3KKKJ6I4foOTiVg90AvGPF7CeKMXoTmSXJDd4mDI3y90f5SnyA9JwWJZq6XIepK7-NaAyAbSAJRlcoB4l2WaAqpHfFlKs4NpfDAelj5Hq-wm5O3IIn6gdZpFJAKANBgO2WfdLJwBoL4wVutRsrcs1NvSoIAXi4VkmB9fxSEtvq5jRDzVrabGOEFAS_Pn_vyoDazt0wSRihaYJ_7yfkGVbEmsEN6fxehorufnBz7Wljp5SWpc0SjWzE6hXquc5_95Olhbrkg7f-xDqEneSEQZugrXRMM1nRIZ7qIPHRB9peAghUWEqZCH-VJzu2giTyMgk5VFN7cQvXE4vAww3S1m7fKf1v33FDzqgFPSOCBXPu47q1QIypF0SvPQjfCRcqONhsBywCDCbcbizGNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/574b047b5e.mp4?token=P1dIjEtaRpvXvdkDwlBLY-dznTQAl8hAMV9MbD3qMzQbhIJgqA-W8wq2pz1TmvS1Dnq64Erybs3AyHM3Y61h7qL4n5I5KT2uqB0eab4bgO8ULu9cbz-zcNyg_irLBn9otmdcnE8sb_6DqVIaHBx0hBGZkKm14Qln3DNIEVtWKmt9EKNpa7j-LToSR6vJdUh0RNhw4vFEU21f4fczuv_uJ9lQ9-2iZqoviYvb13NtleDJOTnnClc1B44LB52fnJlquvlCP4nlkFs9vMo6IRLRlOIiC1G3KKKJ6I4foOTiVg90AvGPF7CeKMXoTmSXJDd4mDI3y90f5SnyA9JwWJZq6XIepK7-NaAyAbSAJRlcoB4l2WaAqpHfFlKs4NpfDAelj5Hq-wm5O3IIn6gdZpFJAKANBgO2WfdLJwBoL4wVutRsrcs1NvSoIAXi4VkmB9fxSEtvq5jRDzVrabGOEFAS_Pn_vyoDazt0wSRihaYJ_7yfkGVbEmsEN6fxehorufnBz7Wljp5SWpc0SjWzE6hXquc5_95Olhbrkg7f-xDqEneSEQZugrXRMM1nRIZ7qIPHRB9peAghUWEqZCH-VJzu2giTyMgk5VFN7cQvXE4vAww3S1m7fKf1v33FDzqgFPSOCBXPu47q1QIypF0SvPQjfCRcqONhsBywCDCbcbizGNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
با حمایت نظامیان رژیم اشغالگر، شهرک‌نشینان صهیونیست به زنان در در جنوب الخلیل در کرانه باختری حمله کردند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/448921" target="_blank">📅 10:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI7dGI2YFdOuyGZLeoH2gdduISs3G4GUS05gMfXszA2vGhU1Il1gXwDPWot_lKIB5kjHZd2ZfLTkXFEoQND5RJtk6LS0zr6ge_1u4V99eqwF-IiCiSIUun-WSOQtIHuW7TMwuFPYB6SAAg25cVr5Xj2zg1NCYKvvcVktjQHMf2VdqHIqNlIWUAvDRrfj87DX7rVsn_250fMkD9fiPzqycsY-cQF-0kUN6rpeDzjvaKlGxVoOiqOXzv4Ns_buuUAF7ntqXwJBhAHkFOnybRJyMRerM_3DkR6BTcFywqYPqe1dK1dVC5fPGcvnRetfJtzldtmVmFMC_pPdOoCnjuBVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختران ملی پوش ایران قهرمان آفریقا را شکست دادند
تیم‌ملی والیبال نشسته بانوان در نخستین روز از رقابت‌های قهرمانی جهان، در اولین دیدار خود به مصاف تیم روآندا قهرمان آفریقا رفت و در ست‌های اول، دوم و سوم با نتیجه ۲۵ بر ۱۱ برابر قهرمان آفریقا پیروز شد.
@Sportfars</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/448920" target="_blank">📅 10:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448910">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZUVCFibP8mdHUcBpV02XqerJXWlEYXKbQbG-XiJbc5-Bb8N81im76LRqcBiu5GT5gL1Ng9UcyBh0P5Eg9FT7uWG_jDhkn0ZdU2hMDH6qUFKATINA9zKBiERJJQuCFzyi5uXfBxKd3XN60K7EMc0_oz-1Qx9P6eRzpf8gG42vnlSatymLNk4xHU4VWJ7edKwf4-A5QWIhS7x9ojy_9QBxkO02R0AKEuTp9a1YvkIKUesU5CYAowiRTd7_AN6AViSHKCqowsoGPap9awuMSwDtPo7AqIO4OGT3dmth0JRqxZdgHdX_PS4nDGVrnj1wVu0P5NaSB6bUV4-HTHP0lngxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GSTm1y00ACkFyhrxhKuxP-hmDCTqazBe6d5S-tuzapWIA0beHTB8d6BUSckbQx0rlr0-J7a8qLl__oF98lBJGESHicrM8-eadzQQSTjgzPN3szJUDG9rfVVNzDz6BSDgdlN9hQMNpijXlvx5LhfAJI6CGq6w9pe7Ez5wk97v7NFKHAF3T6uMNioQxSMTOEK8ZKwNzfnyeiVPIDt2TclFYk3F-nKgpCgnq7V0kzc0hgalbxplVM29hjcvCE4Gmd_7WVkwG08IDmWFOL13g78JrWsEzOLJGuw9blYTqvbz_2ZbJIkbA-0BgopMmwrYJkCG72eEuYCMQctaSpttuCaBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_7X4yymGvHwppyP7-sTkaeObh1t3q0BzLhvmDipkwA9YyxNUzneFhX2c22lYR2SZAUJkdhnCn5Mcfp6XF4X0lvdhHeCWgj-sIt3bnzu9dIuSRrZz7OQirNMVJjrOoKyJD0_XKx3tSKaj1ejKxvKObbBnETi82Q6aIxluDPMkzcJ3TbIWNW0kCuz9sv1zi79WvTXQSlNBOlbrfs8ZJbJyL4vbkslU0AbYdbQFwuiWjxkUhYOw8cOZvOs82BMqhK1EkT3pvldsbYa8Sfjng3UuAJNHkSKF5TAr-ei49hLH-fVCkd6boejgqcytwRbycenAedGZXdx6Jo3KMgaqA3KBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7LNrvVr_FHL4hwGDw7a0GSTYF6TdSJNCxGyKhtfAY8SSr3ludfCQh4cCECxJpNtBt-5qqgwIFwBKFuK_R2aOY0tsBTKiouGaa7wNiwARlf4-kW-uDGcPJlLN4XZ2Eks_cvPJwNDztFLphjvB3MoA_eO7rRY0dYvEmDt2TwJmNZcW3agNJXOswK7Q7QAKTUxm7KPAwrW6XbYMLAiac3Gs9iBvwvGp9rDNQNmIP3sD23DBasaP5am10ee9bZrNoUaZgHjR9XqIJ9vKREJ0-uk0wRES5mqJkYnFHBVeO690sTJzdPR09DTmNjDu_BPfziyJiy-A818XVh46roGEnVxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r8Zrcgh8eSwxVH8-buQPUHX7z8NJ_fVQ_ULfJNww_NObgrqUoU8J1e6A214hf2W3FP4WaTVZrzjgucfXMI1MRXRdIY-kcxEl4YriwK7K1hHQktWwQtIl2fy1AawWPtRz-qyQzAvTbOx3TiGtBvMTsk-sBRPN0n43TlnUpZX3enyT0_NSEfnIFdNrVxxLAfLZG_FKFJP0oYTIjxUaGs2lj9mEDVq1FQa-TCVc9Xmj7AEGR3HtSTMJrkVGxexerExFLbASiMtaP4fMOnnwZPry7XxxFEpVkzPuotjhqG_f-h6eRpef9j0zH7nfewOY0iC9_vH-kMs4Y2jtK3U04AkOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/paSrHQZpbJZqMMPYhqnHxGx4cLrJKqwyLO_G__lpUfm0zBmiuBmjUgN38LxGUquTNNTUogQaXqHuuokejFU5YGzaltLlb_qVNPgKiHgGoRsIw_j8ycU3Yn8lQr0Vp-KDbEU_7Y8cDnpYKPjYArjfHuF0JJRMLAnfc38L1FTcLeOzBpQe2EsYSSvYI846_J2Ej3VnoS-An6Sav0ZAY-O2xv2vVqAkoSZd9PtjQ9WLJpgR7mP3ndHG2JInz3kPkgtPoW-aoODfsizYI96zwrpwhx5wowWJAgYQtTSmDdin6mcLyUxZ721Ehc049NZ79stdDi80xWmnRx0A2bSmOxOFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln91VBCHpycL8k07GnIyVCSiwbniP4WFDIvNQQYd9zmrKMJE57EdqrR98caJkI4YOhHV1TuN7Q6ROWQYNYMBQ4OqplvI144sqdqYphmqv2t3iJArY64255oOswbSmvbgYMBAVhFl_vNUsr6obkGqaRWmp1wgq4CtAh0BiF9f0stu-0y5Y_34TZqXwkOjM45rYghgvwNmyk2F9-xeB7jT2HLKHRPAl67Z6NqSu1H65tu6ZxM_L6hewsCMJjVcskHcglUnBwAf0PbeNKgGzc5A4VJ3quFAk074bchMUb72fH0xiBkhX-Uk6JUP17xzLZL5Hw5nIx7iO-2F-rKyVZlujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kHxMaUkeYe9D05dkm8YVAYfXZuhATrtb93k2HeA41lQ3_EAdyKAGEjAko0kStU5kV0KPaKV8HwK9AFedibfkLs7QLd3LapJphF_B90MWWQRv6t2xtv2x_Fst7YVVPNRmN1C3eUnXSXfyWMM8FvRAMkLwH1fS5qgKxrajuljAmRR9O_xQfvv72ikgG_n4KjTTkgyKrg93QYDXITkzIKlJ3gAPmA83uMuwlc4TO0TshmnbMXdnd5ZxZBuf5ndDjvQYeYjumAEuAINDwotpQy64qcBSCZAS8dGiUpHTYaPibW37ygQSEFAytvWiwNWF8rb4fygGSuFO8mVvCfaJIjYF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLmtbMBJDE_7uMiwi2Rg9zXhFIMlOJjODqt4UkWDihwlzVbxA4OrDgrGcS6kueS-CEfwJiDShTDvgzj2LrNS2W7vEsw7vFV5l7pPOw_NFFMeq6KAku8LshjtGzHXfxUBVo2ZnmEul3lTkiZGwXsMbg2q7ZRxLk4_AnVlzL2dbPFJlRouVc8y4TFR54ycSDvQwzxvrLMLE7jyRUe08_0AY8GcQv3VmxU4l-q7k9bsbzOx5zjtehedCqY8UN5eoRvzRPNHZHQxsXn_5W2DqIzYhPvYaeTpGQQfcjgvEqTNKj4-KMIqrfTbp7IvQWT0WZMGUr4zX4yZcu6FOQdBKLGR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNxBAttFkHz259NkOTXvMcCzG6xGTW_5m8V-zb7QR6PLRaKqcP_TFxMmQ1jThqQbZSSc9vOBD5d16LOEkW2M-hDfdjlAwWokboW2nyhFotGNhvQavlNYDLnxdPr-eoYH5kf8ze0NRQ8cEr_7D2aVw6sn_Ws3U5dc2Ks4D_U6vDF04SbFXvcq-_3PfYddJVpu8KM1Awqf09oRy_eCy25hfMIVnRnlOd9NVj3DrJ4usGBxEMb8Y30gIs69dp1K25bAPCdjxFiDZEfx28qkyLjBqsVNnO-yZOQJ0BYWfe-lwS0qGIkyA5eTPAjPkFxj-D3L_HQL3OLNA8crFfdGuvtm3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از تشییع تاریخی رهبر شهید انقلاب در مشهد
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/448910" target="_blank">📅 10:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448909">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آموزش‌وپرورش: زمان‌بندی امتحانات نهایی تغییر نمی‌کند
🔹
رئیس روابط‌عمومی آموزش‌و‌پرورش: هیچ‌گونه تعویق یا تغییری در زمان‌بندی امتحانات نهایی وجود ندارد و آزمون‌ها مطابق برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
🔹
تنها امتحان درس «دین و زندگی» پایه یازدهم که قرار بود ۲۰ تیر برگزار شود، به‌دلیل برگزاری آیین تشییع و تدفین امام شهید ایران، به ۵ مرداد موکول شده است.
🔹
دانش‌آموزان می‌توانند کارت ورود به جلسه خود را از طریق سامانه‌های
my.medu.ir
و
my.sanjesh.org
دریافت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/448909" target="_blank">📅 09:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIhYMwoKaeJ9VgSHSBCFENEmrzwCajKWNtnCCjJ8NWCheOzsFoWizfKcTW7caBxBbFJujdPPhz3-gB84qVU2EhCsOkiJE8jlEqIjUYqbI5BmZTURYMnaNXgXNGpVOCL1TPW0CKFWR4B_GL2vV-PtnCM8a-WnhvWaX83KnCB9v-lhW7vJd6nSqMZVLMdNA5Fg2d4Jwq1w1svcJXeo5RCssnb-4CWcFZijTbDSz5awawIStuPuEEoHS3WpZ2Vd5mIngOk21sXDH80qivdMxCxDk1V0XLOxcCY2f7707ZgDCBePbGRbds-q415WokV2h8_nDLVQ68xP6Fgu1Iz9ZKgNFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمادهٔ روزهای داغ باشید
🔹
هواشناسی: از جمعه ۱۹ تیر تا پنجشنبه ۲۵ تیر ۱۴۰۵، با استقرار الگوی تابستانه، افزایش دما و تداوم هوای گرم در بخش‌های گسترده‌ای از کشور پیش‌بینی می‌شود.
کدام استان‌ها تحت تاثیرند؟
🔸
سمنان، تهران، قم، مرکزی، یزد، البرز، قزوین، لرستان، زنجان، همدان، کرمانشاه، فارس، اصفهان
🔸
کردستان، آذربایجان‌شرقی، آذربایجان‌غربی، بوشهر، خوزستان، هرمزگان، خراسان‌شمالی، خراسان‌رضوی، خراسان‌جنوبی، ایلام و سیستان‌وبلوچستان.
این افزایش دما چه خطراتی دارد؟
🔹
افزایش مصرف برق و سایر حامل‌های انرژی
🔹
احتمال گرمازدگی، به‌ویژه برای سالمندان، کودکان و بیماران
🔹
افزایش خطر آتش‌سوزی در مراتع و جنگل‌ها
🔹
احتمال آسیب به محصولات کشاورزی
🔹
تنش دمایی در سالن‌های پرورش دام و طیور
چه باید کرد؟
🔸
در مصرف برق و آب صرفه‌جویی کنید.
🔸
گروه‌های حساس از حضور در فضای باز، به‌ویژه در ساعات گرم روز، خودداری کنند.
🔸
از روشن‌کردن آتش در طبیعت پرهیز شود.
🔸
دما و رطوبت سالن‌های پرورشی به‌طور مستمر کنترل و برق اضطراری آماده بهره‌برداری باشد.
@Farsna</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/448908" target="_blank">📅 09:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjLmiuLgMn-HvEcOjqxoJMa5cpDDD0hubbzWwuCLw7d8SvM_wJXB5LwwLMx23A9iJF_6rJ_VmDMfZGF7xqxJD0Bg0DbPjcxyG8BMyWtx5RzessbqEbwvFvvzfnFZtW8Vw1J5Frtb2YPocLBHfCvP9PHC0ZuMXZ1FG1t1Kgjg-yVYoPwh_CJyONpQ2sNjlHNe58ogZBlCi2_cCoGQjuPiyVSc_X0S4I-nfU6D-llIq3B8QfLbsc9GvVaRTWtk-glAusGVaU2I2vAWL0kGmCrSC8bWmms279svedTpzlwb0KjYyp6mp-ZoH8ihDo0WHMlHZElIiFY1VS3dyuF5iHRHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باتری هسته‌ای با عمر هزاران سال ساخته شد
🔹
پژوهشگران چینی از نسل جدید یک باتری هسته‌ای رونمایی کردند که به‌دلیل استفاده از ایزوتوپ کربن-۱۴، از نظر تئوری می‌تواند هزاران سال برق تولید کند.
🔹
ابعاد این باتری تنها ۱۶.۸ سانتی‌متر مکعب است و با فناوری «بتاولتائیک» مستقیماً انرژی ذرات بتا را به برق تبدیل می‌کند؛ روشی که عملکردی شبیه پنل خورشیدی دارد، اما به‌جای نور از تابش هسته‌ای استفاده می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farsna/448907" target="_blank">📅 09:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlVsksP_WMSXz5qwruvWOAmP-4mEUonbHP3sULCfQ2EhKlyp8oW2Eahy6JTSyFylfZ2DXrrbLcL2HP1f_Kr1ZPx3k4met7YFv7LZS-0FYnnzFDfacfA85EKEV3hJ47Z6UFmONWXzXzQk2g1Hfxmyvs7qLPqZmzPr5-IJ_NdgO7ox-iJHeF7s5QFgjvm9z-wrSuEhoitmx7EQQMkb_J4f4SLGvC4tMpiZH4UhDu90k_fUqAIt5U3cHlFUcdgwBF1B590z1ujbT10BzhQ0Ixdu9cMkXeqL4ZTYQYZcI1HmfiWPRsdC7BjEKFyQfJpw8o-C3XLTDU1HahUVjXa24sOCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست جدید آلمان برای اخراج مهاجران افغان
🔹
دولت آلمان برای نخستین‌بار در حال آماده‌سازی اخراج شماری از پناهجویان افغانستان است که نه پیشینۀ کیفری دارند و نه از نظر امنیتی تهدید به‌شمار می‌روند.
🔹
وزیر کشور آلمان می‌گوید که اخیراً به توافقی با طالبان برای اخراج مهاجران دست یافته، و در مقابل با ورود شمار بیشتری از دیپلمات‌های طالبان به آلمان موافقت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/448906" target="_blank">📅 08:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448905">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebQKW8sWtAbuFrt7OT4yb05_8guEYaVr2czLw35VMZUa-jRv7VXiFyarWI1rCchkBZCD3mU6Wyckzl5dnVTv_zL22Ploi9VvTtr8-g0fH8jOF3RWWjqApE6q39Kak8eYUh8BD_Sq-BBnhUV7TJgixjgeJHox-93HgvpqQR1fWrR_ooeOxLzkjN0xIuNXRJudBVI-tBLpilFrbWrp56SI9thF8HODF1pkWLcP1E6msRrjeSAaPQy-rybLpDpajEOv1cKYngRET2aMws0hZaYZOmiWNw_I17bsWitKj2Xe8MvlAJGHcex8vDeVNC6RBji2FNLbJw_VXHInw2BhMYmL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی گسترده در اسپانیا
🔹
منابع خبری از کشته‌شدن دست‌کم ۱۲ نفر براثر آتش‌سوزی جنگلی در آلمریا در جنوب اسپانیا گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/448905" target="_blank">📅 07:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0K-tcK9r_x6CXbjFlFvZrW6m5hPvH76NobRvNc4WxlJDxBweyH7FxAus16U4iKg_m4QYtkTJHv8cbY7yw12ecDSJr_wdvsQKQJtOBnG4Fv5vGILw3Jzxy6fSyPiJOpA8nL3N-yD7OzwEKyeEsxrj26iCsW_s6Tn3VSLUb7GOiNmqF3wSILuubpc5MwiKUbG5Na30Wq66BpLTB3j1fi3zzZZJBlaxE4QyUrHGBbkH8ps7Tv0UbWJtr_iLc-MCwG7Fk9AA6FUkjpGxz-6bq2T8SFQp0ruCuaEf7uCjFZA391C9GjT-8ZpFOwIWrRsfRQkdNrfj9XiNKmcvCARIxsdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردپای عربستان، امارات و قطر در حملات اخیر به زیرساخت‌های ایران
🔹
داده‌های وبسایت‌های اوسینت و مراکز هوانوردی از حمایت‌های متعدد جنگنده‌های آمریکایی توسط پایگاه‌هایی در کشورهای امارات، قطر و عربستان خبر می‌دهند.
🔹
برخی منابع خبری  مدعی شدند سوخت‌رسان‌های اماراتی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farsna/448904" target="_blank">📅 06:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLZiqUk_2CSYe3e-YglyC7UWbzxWSEsyO99rx7tQPG3EjveLW2JJt714WpZi4W7VV_k9TZEs8C08NQge4lOi7vLi43iLmlEJwedA20aw0GUc5h_gD4Ib1epmhqbYs-mWO79Y5b8iiS8s2YQW8f4nkxwsHt_pUu2wtaZ4zp75fdwvtxqRWpH1SAhJM629FGyuLSWpl_Nz2jIqd9Au4NQhh77zxV70_5sY9X8NzekTAriqJZVeXlEe6-RfIHguowBuBGYs0ZsiTjeM56urS2KCfv493Jvd7z-DV1-DHeUzE-zHc59Bs2iE2_mL63ulhDyZ4EZ9yJvh3UdrrsM62EyCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور رئیس کرۀشمالی برای تقویت برنامۀ هسته‌ای
🔹
رسانه‌های کره شمالی گزارش دادند که دولت این کشور تصمیم گرفته نیروگاه‌های هسته‌ای خود را از نظر «کمی و کیفی» تقویت کند.
🔹
این تصمیم در پی دستور کیم‌جونگ اون رئیس کرۀ شمالی، برای مدرن‌سازی ارتش این کشور صورت گرفته است.
🔹
کیم‌جونگ اون تاکید کرده است که امنیت کرۀ شمالی و صلح واقعی تنها از طریق ساختن یک ارتش قدرتمند که توانایی مهار و کنترل تمامی تهدیدها را داشته باشد، تضمین خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/448903" target="_blank">📅 05:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448902">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
با آقای شهید وداع نمی‌کنم
@Farspolitics</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farsna/448902" target="_blank">📅 05:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448896">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WI4re2g29qHhsvb7x0-wm5cd6Iv5H7b-uOr3IoX8aY4YSiz-YCWtYYzklmntgs5BXg7SGhYgCQP5Z1mJDsBzEW9X3qU5Dn8W4rPS_3beMqu3EVEEBpunKRPZox_kc-WcmbbJO_Gsioc3Q9BLuKAEUW0uBXpx8TqMwvcpzO6BIJHzSp_BjvxuS9zEbd4qHEteVSc-KwObAO8BpcCSL1NtWV60F6vqoQr2JSoVSaXh5HfWi1_NRF79-IWy1gJGVOho6HgZjBZzaLy85RKaniWFZyKnmkNuDBwzP-kWq8TcLYV9l27zU9Zvh5oQ97NKRqx9ff9Mf1CVybP4otOVQSvCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjGpzyftTnc-CdR1CwTZLsFXwtx36e63RrUQJ6guxKoV2pgfHnsI33O4vspo5zTZcDDFHOoDL21OiTQIcUGx6PSfXiJo6iNgfsKud0zjCgJuwKtrlx2QDmHC7KwkvpcEuwPpw13XSzmzc_WA3XVEWP4hkGNlvUWpe9iSSv6AXvY1k63Aa_M2S1KNgT-TAbj4IvMGtQjJYfHo7DthGLYkZ3CYbNh9gzaPK6TozYR8_xlmReAgf7Epvhd3o5jq9ENH8kU257b45y_azLO-ZHYuQlujwMQ540K_peJWqnkUhKo2sxxmvbpMroMB0PFvkRUTz4BxQozjnvo73BrurthpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rO6S-ZcvfOK6g-9znbb7_WtCgaeF2z8Tr0DMfOnbOEuhcwQs04f9X8kY6WlDbVxcp6srUGYmphvXURIsSH0FuDbSxOpfZDuYS4eClclaqC61N7JLpZJraldIh1sNrkfmuteAX0IZOHJtfYopvRccZJkWcIaFv-9VqI7tdL8HBPpGVttIPbmP7KALp8Z7qnKBS8jZWge-IIuaC426MDiLdpd4OU4vRCsv2_HCZ7oNzNUMVYrjPxSQCXqZ1GdbHXXI7PSUfnYW5b9R22QkEdOIQf4UYDKYIeYnMX2YWm_DQ0raW55VGALI6apivmQyI8BK4rV6HIYsqVswheUqC71EGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOhXdJ1k88qz51-JulRLQ5NPZWEXyElhKOBRLNQjosrS0AHFS0bAP7wo0egphcHKa-9IurzpP1eEsazhrtQi-nxv59JK5H0ExQBe2Um_xZHrF-9IKPDiyJvJ-nHX5Q7UUVJpwQ4tY3OxyAmDVvxRCE439UuAsIkYlxMrCB30_J4ixSs6t2wIcz8_0PmSWE8dklhFx-BQHsMCtEs9a6_-SDkIfDh3o2_DJUGUvzVJ5DhzDoTuPEmLrDoxRZQoTU0HA61Ka9GqLc39h7M-1mLVripDZptu_dE9Rw1qa4kC8vi0n72AwrOTHdfN8lQnVKAq0KgQP45AkvsFXn0c0buwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SshJJGK8o5oDHxnfu1TXe3csxDfbJUbnpDZVYeDqH04Jalu3rWVB7wzpbdTQhqEUdcuCkbl8mnaKh-CTQhpmo7pgtZkkKBQ3YG-ZMHFDynUCPM8Xmz2wwm2az7WxnarD6OBZywsdfYJNbTNL2hm5-3Ozk48ZsN1DLTreUwlxZVFdUxf4iJK5z8bk9UdQmyderMaNeGMNnajWfztphhy3u96H8EX47nYuu17MFwAm_ocZRsQ2MLcT830dmecrz38ybIw5DAo6EsiWc5GnmSAOJvGXUiqM_z8zpcu4MLoO41KTlZxYLIY_ZiQbjuge2QMF-XbJzGn45t78BG1iCrHGgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCL0iGQAQ_vfSyThjS08Ev611t0ptTEXIJ0EA8fiZGwjwjm-qcOSjjlXu2xUqBBAf_mSyilBBf9O5iD1H279C2d0nO2NrjBon4s8o-Vv_3DSN5CVgg5rNZ3VpMfdD_Yw_Azb5glyWytndJBiTTWyMXiKgC_lYcg4i3RMhnso0Wf8ZCZ-pfmQdhLv9zJU1KojHKxrTvdMTZpfaVWdQwReUVIE9MHweHFo1DfiTynXkCgJrByB6iQQWKGHyX9ugyiqPC2SRAWkFnXrGJ51eZ2n2x041B-eWowi5yMiBG0L35wmXrVjawM5q4lmgaANs7BqCOPY65YlCO_7RU1DUiEspg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری عشایر آذربایجان در سوگ آقای شهید ایران
عکاس:
مهدی ایمانی
@Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/448896" target="_blank">📅 04:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448895">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZfKB48_ubJUeFXi7rR2j48mR_el5aBU23OXCuI7LgllixNTJ4MoQHgMzYdMugrczoCIi4dklBV_sFBZ984O9dpEHEinvvEgSMvE4GzJNZQt4Wt02a4l-EVc6g0oJilMiFHAZFk90-bpB7qO-776RMzKaJYiPmahUNM6V0Owt1u7azwubjgerM91Fw7AH_5Jx0mvSAwoySpMHwzwd4EgCCSj9pSpHnx0zydOL-jZQ61Z7ZJEGVDOBbGI9z-sPG8fLyUYvHLfURFAYCGxtAVv4g7tettTGTheCvRRBn2-IeOkOo1OiqT5wI1A6maFDoVRgSyg-mH2mifxnB4tK80XTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر نتانیاهو نام خانوادگی‌اش را تغییر داد
🔹
یائیر نتانیاهو، پسر ارشد نخست‌وزیر اسرائیل نام خودش را به «یوناتان هان» تغییر داده و اسم او در نهادهای رسمی رژیم با این عنوان ثبت شده است.
🔹
این اقدام پس از موج محکومیت‌های بین‌المللی علیه جنایات و نسل‌کشی خانواده نتانیاهو صورت گرفته است.
🔹
روزنامۀ صهیونیستی هاآرتص گزارش داد که این تغییرنام از طریق اسناد سازمان امور مالیاتی اسرائیل کشف شده است؛ جایی که نام جدید در کنار شمارۀ ملی او ثبت شده است.
@Farsna</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/448895" target="_blank">📅 04:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448890">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dr77jFDr5Td10GQSHZamvuR1Kc1rFy3GvG7nz9PrIFcAKRnzZ8qIV4lT4_sbpPunpa31VSQPpcOuf_iKG0GwFKaBAzd_Qthzm1KpBhxEfghzoucuCNBDzMXbdVpVpTxfvfq_qIwvzWooX5I_YgR6Cb8pTiaIHS7_FNnkJKcedbK-zj4dFeELRsTTcUtrlbSCK9obZmbOuZ1Z8JqAbmtQ2ZsKXHz3IJSV_fTAoB-VicJ7xwq8nfi3yziqS-sahFgVG0fA6lKXWxvD4xVC_CrX-gAQ1gdr4tGZ7gIpHp9nDiqQWdCmLUyUboiknkh10Y4DfBQyhhpqhNuJpDRQxyDdRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLcg7TusQ6H8IUCyGMuRWXjgyEpvQK91JFiUzUu2JSr0K-L6u8aqIH3jCs6qIAI7k1FiCaYSyVIT4IHZP3NgLl62IVcPYIt7vCYfhDdMxhul6Nx3DcNDsUfGMuI79LtJBWbV5ccZw4MdGjn7Nae8jkeeisAbWlgJLPIJVJml3Me24YyPc4XZ3qxD2KoklCTXF7JNlyfdiDqcj0H-emIYNhB0rhQlvngOAWoMV-YEBd7KbgTouyfRmdbix_K0BVv59kqmzIbxdWzV3yK4HWbBL9rOU8h1aW3RBYUYD1mViOBCPVRmhJYOvfrrnBq8i4DXUSIula5LX3IeS-sYR0eWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPcTRvQ5KXtiOkikaXPjoS2sonsWSGOf0oWN_xm0F0ae8w6MPeXVB1SV2PtGOBaW4hrPp-_vaNgH1E-6L90rzco29dZvV5bBJp5D3RssApELlN60co89URrIcm9ZntjIg-56WGXhrZV1qrrrrw1-lFqgFyGoJIpGPb3ln4Iq-Bc6G1M1Cn3JdUyIkKQREW20w8ctlb0E8QbA7Uwhhcc4ACqCIcBETB-fAjSqckZHDtHj4r6hO-HcH8fYKmL_z-oU81kx7Jw8xF-41HMs_Tu4Xm0CnhgHnEjkMnccJhUicqw_HAe0J21DHWXK8WcbRiJD0tsVTBCgSwBKaOrO1aOP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H8M1elHglXRtoAub8mKEX4irmX4ZN8mWu3JlHTqcnK9QjcMrlsWa3Afna0GGyryZGoXnVj1jH0QhMSZC00FrerCxrKLLfPeEJX1MvnQajH9tinNA8uSix0TZuM28g-mSOqX0OX_dIxtrbZYwL7Uh-0B2VXsNx9nwRq8HH1M9U9U6-mlipUia4SzJLzn2TKxOvAZA77QTR7_M--QpYT3EII92RTW3neqYeHfCeH9qNIGqN49a8OzJigl78PZpO79nV3tCE4gU9SNwPOg7jJjdUZlNP_9Np2-hU83C1lV60u6Ada_dXgLIYuXkZYYl5k5Td_JmLDIAj2HVw78x0AoKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1lENenM3PO4zb3oN4rlbDO9Z-Hvmmhakwvx1XHsNxQQhK5-UGz1yjU0K5Sk6NcBuyKHMbNyL2zahJGa3G-hg82RnPPbvVB7ex3359JVFJ_bc1A2DSU_tOpjNIJg2WJ_24OrWffhrpMoeSH7HOcg7uj3Bx5US-9bwKwyEEbyTSX5Om6KzGCfNjX8d9N_j4ejcplsaJXZRJr1g0tXyz6hBHt43dIYpceTyb8sHO1SHrttHF7SV-EbGrTsNxTYHHd92bHt9AriQnDgJdLNKV96NW7lOsMA1EiasROcZQcaP4ZXiNt_cbLsoLqPJNMrIsTlP197vhZQpZ7pBsIlGD8aUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دستۀ عزاداری خون‌خواهی امام شهید در زنجان
عکس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farsna/448890" target="_blank">📅 03:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448889">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عبور از کریدور پیشنهادی آمریکا در تنگۀ هرمز به صفر رسید
🔹
بخش انگلیسی‌زبان شبکۀ خبری بی‌بی‌سی گزارش داده پس از تنش‌های اخیر میان ایران و آمریکا عبور کشتی‌ها از مسیر پیشنهادی آمریکا در جنوب تنگۀ هرمز موسوم به کریدور عمانی به صفر رسیده است.
🔹
داده‌های شرکت رصد اطلاعات دریایی «کپلر» نشان می‌دهد که در روز ۲۵ ژوئن حدود ۲۸ فروند از کریدور عمانی برای تردد استفاده کرده بودند اما این رقم از روز چهارشنبه هفتۀ جاری به صفر رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/448889" target="_blank">📅 03:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448881">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2UyVSeq1Lu2cuF0BsdM0p0iDS6yCN5EyJ4PPslcvh_ca5TUCzL0cdqH32KBj3c9wsgoOwa_PrdXV-Ofi5LN6pqsQ8urk2Pdtiiag13nI9RUd6ZlTLJT-Drx-a8dAKQ95pw1t0mI5q0RseWcBMOIGnetKMfLdWlOflOiL9YNuI6wARwaWQsFFiJOBvMddz0DleLXy6sPa4CktIgDBjzWnqdjpgOCU_iv1qJxWVKiAPb6LWpLoXNZobA6Vp0ObA4VJCW6GJQyK3ud50qdoCLofxGYqQmFR-_zoaz3kQt4RKE1ADd5sj9WgzIwAF0tcJ9EA172yQ16Q_CiIBmftjdkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzuuDGs5Ykf03JGBiIYtnfN5VHmmubbhSUQ_YJA0SGhxBnqGF1TBibbepVw_i-MWBriLg68RBPN2_J6Mz7JS0WtPXfXsZbOaSRJ-a0IU9NFJ2f-BlYGSxpW6dwmkQOPectcwvG3-x6mxAh0NkpRwIcUlaBrMAUu34NxNiBdl8eG-dCV_EqEsYvkbX-KgQ9NLcYqKp4ukY-Tzxeg_KQ9uihhbw1atQ-aCHYHEGnufhkAu_hm2lmZiZOZ1dhToPiLDKdvGq96ruRJwzWs_G9kDyJ0o3I83-ulfXrLMizhYfCzU3OYMUUU7bqRVsolLbFkMRdIgBpsJ0irU--i261jgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fLeJd3BjnT5s7_ivt8UnhH8MaeTSJMv_SndRkH6A99jLlP0O7-UVbMg9m2Shsy3hN1rXRMDWdXWY5yCFrCCDLeELWxMXR6JQBNMIngZwa3n3W_DsUcYswGuZNi0hxpsSVwOW8lLqYN0HQJ1jMXUdK8LgEHaDzMxOoyEas0dnJsvB9fmzCkp5-yXj0cAHyGNHGAo_ish-pJXOUXfLaKwkds965AJaRAfB0nFPurIGbiGjtEDhUvfqsfK2TB2fFbbbfo7JB15OoFvrU9sVh83cfAcElHWF2_prAfXXn8qHLhKoSbL_RdRvKlc0wW9pw4TSORxaCWqN8MzjHMkdSNCf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INIEJXucK3sDAYmcI19X33LBGoHWDyUjcPaM5SDgYmmNLFyYgDQWN40s1YC0JwLjNzAoIgHLNH6lMiX4RdWHVcty0wiDBDLhsbS5lm8sARer8XqEku37NdddXlB8MBeeaK4JcdpjqvOz9kTmP3Nk0XmGyASE3wNdXFpmu-O4vI7S5X3lmGy6YNE5jYwEvjqlmUJEEyOXz4B7LR2OldiUeLMJ-BZpbCgtfC7q06YynVNDSYpWwZ3MKWegC61w-IezTLEKS21CxoaJcUfsuyw9tqbG5J5BT8jNYFisur0JNvM1Rb2mCVye0y7uvd8wvlw-fBK3qJY7TF9nB4sSwI4p5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fd-uvhAGroNv3hi-eQi-3i_m0GV3OIqqTxkD0oVFSJLUxx3-D-UemTIxu1gpeguCB9uWhqNACTDmKegn3ChkXBY96OKu4El67DI65vqjUhVeaAVwmwBdycnXmzHCTjMzXUWUmUJQC2Jkp9YLUpGp90x0-p4RKaTD-zV_F7TR2aybZfBwqTjGTNCRhjf5E9VphMwdaW00q_thAavX37DnhSMQIoX5fh74nW2oA_BSmdTjm_gAGp23vhLbYMaNL096Dgy1VKHq_75X0uml4W_I4pVCHm8p9K6PEF50QjMWqBnBgiOGB1zozHQNVn8wwjPR2LJqPDuhWac4rUrYN4jsEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ljj6eVtFJhwskMBB6wLM5RlqjZLsRYxxzwq5gqWYRDVX1XRzBjnz0_4Y6B9Li9J2ySWIE1_ffxbWh1H6gAAGR0SsI38xwESb1E_jpMyE9_L3aib3ebCD7UPfWBaMe8qGn4cdnSqPQNBNGu887c6t2uDAcgudodtKIH0Zj5zC0D7Cb6JBIkopx0UHSWkz1560847GLbKWmRGHKWFO6neFFMI-uABjZXkE-SRk3QX7FihR8PoAoxgqeh_AMxiyTctwYjt0-ni5DsVLWOOybfwLzLfbBbZ303CJyVh_7qtpJy10ZNiqoGT6_GQ6AXOddcLUt6-4a16xjuW0RUfQGoV2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDOxXcjck19Y5bv1SY3Hp7XLy4D6L4B1Q1Uzcj9dx9JJ64v-22zD3eLjRQJ-VhLdwkccv0FEWarbYfC_vnbE9Iv7D6LO1tWDv3AcduCVPNNtw_hlF62-_QLSd9fR61gzlHzna64OwRyP9rLUT7gGr77Z4JswmmnAWt4rG_Z6o5JaGNEUDDMBqRWaRkuW2nfgTsb5KbtRQY84-um164bbN6N8ACOkgeFoViYNtIA8xTQITdnQqGQw8rAaZHa0M4fjnkM_SeBMnJMZ4C54_uXGTE4s59R0uqPLRbXOOLyud3dt3xuzLqPwQl4IiFTg3eLzmxGQpObMZuDnyFVYUjRpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHZyTeowwxa9DT3DojlEMXvllv09kHinHbGX6Hyovg6EMJfy4z4Mp0LTLfBn49zyXkZge8iBeQGbsHMC6q-FRZrSfpP6ywP1iq_sbOyM-c6BWH4bebQPIzDqGmGnze_SZ48dZIGTWld1M6lCauViqlAN0wJwGK75VO-LNko8C0CLG_wCKaGiojVD4TXQGqGduGZn_pO63MhkzBQnCegLA-Jyrm15FWSZqYPFMztDr_9fHp-gJ-S-mjNWoLY1diT7B0jSdYjTv1JxRAQ0-5QkGSsGsm5H9j3phnO4bwtemVJWj3YuO7qnPfPfgPOh-xDixAXK9BQhp2nc3r387pDDug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شام‌غریبان آقای شهید ایران در کرمان
عکس:
مهدی امین زاده
@Farsna</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farsna/448881" target="_blank">📅 03:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448880">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMAv59K5vdnX8MxEH5tG4bDlXfs4vmwx7MLb2zc5UInxqTTCaVJVSjLGsmNPrUoif1yKHzvJ-JJjjnCbew0GhJWVyJ5z8hyc5gvgFVyBxfdMgKrkYfHoOyatgKXKcBbB_3k-pVAxWW5tg197S_9wMXyaufLknIUzOzcWGay7GC1TXidH2nBuQ38O9q30pEBuI4OQ9o9Iz0UiyBrFN9cMm0rKJKkjD_6VZDnKIKgL7TNU65vOlRX37Q4V552GG7KYiQVGs8jxvDBSwLQSo8vsvG3nyjietzCxLFHsDwfdQbXmAauHArU7q6ylpFHJnzBQ0dPY1dk1i4Nll74HLZ-KSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب برای آقای شهیدمان نماز لیلةالدفن بخوانیم
🔹
روش خواندن نماز لیلة‌الدفن به این صورت است که در رکعت اول سوره حمد و آية‌الکرسی و در رکعت دوم سوره حمد و ده مرتبه سوره قدر می‌خواند و بعد از نماز می‌گويد:
🔹
«اَللّهُمَّ صَلِّ عَلی مُحَمَّدٍ وَ آلِ مُحَمَّدٍ وَ ابْعَثْ ثَوابَها إلی قَبرِ فُلانِ بنِ فُلانْ»
🔸
(به‌جای «فلان بن فلان» اسم هر شهید و پدر ایشان گفته شود)
اسامی شهدا به همراه نام پدر:
◾️
حضرت آیت‌الله العظمی شهید سید علی حسینی خامنه‌ای، نام پدر: سید جواد
◾️
شهید مصباح الهدی باقری کنی، نام پدر: محمدباقر
◾️
شهید زهرا حداد عادل، نام پدر: غلامعلی
◾️
شهید سیده بشری حسینی خامنه‌ای، نام پدر: سید علی
◾️
شهید زهرا محمدی گلپایگانی، نام پدر: محمدجواد
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/448880" target="_blank">📅 02:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448879">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37457a636.mp4?token=nbFGZdXSdHE4XZ5LbEl55K_uXrGljlppZPb8DfBZi8KTRWnyrYPTpq6O00MCxulHupIy7SWx7SxRAjk8-u2dUTWK711_8Va94Sof7wQlPyXl_-HKxXTEIm8F2bM_bBwD0WeZQPmEahJtA42trNPHw4xN2sH7Xq-PeihqHDebb594dvsNBB5XSsR_hfLGSuiF7XWisFQimPkALzH_f_h3fqRed0-9cqpQkEoY9rV2Xle1qX9NfPKY25e3W4HuWGgvbz8NV4McPMAfVNPMlh62VQm-7sbCp3bXv5f-rAnIOyo3wlYl9253sKwqU-0OaQ71YQOWMgP5Eg5aAE37dC9G0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37457a636.mp4?token=nbFGZdXSdHE4XZ5LbEl55K_uXrGljlppZPb8DfBZi8KTRWnyrYPTpq6O00MCxulHupIy7SWx7SxRAjk8-u2dUTWK711_8Va94Sof7wQlPyXl_-HKxXTEIm8F2bM_bBwD0WeZQPmEahJtA42trNPHw4xN2sH7Xq-PeihqHDebb594dvsNBB5XSsR_hfLGSuiF7XWisFQimPkALzH_f_h3fqRed0-9cqpQkEoY9rV2Xle1qX9NfPKY25e3W4HuWGgvbz8NV4McPMAfVNPMlh62VQm-7sbCp3bXv5f-rAnIOyo3wlYl9253sKwqU-0OaQ71YQOWMgP5Eg5aAE37dC9G0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش صدای خواندن تلقین بر پیکر آقای شهید ایران در حرم مطهر امام رضا علیه‌السلام  @Farsna - Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farsna/448879" target="_blank">📅 02:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448878">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیکر مطهر رهبر شهید انقلاب اسلامی در دارالذکر حرم امام رضا(ع) به خاک سپرده شد
◾️
پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی سید علی حسینی خامنه‌ای قدس‌الله‌نفسه‌الزکیه بامداد جمعه ۱۹ تیرماه ۱۴۰۵ در دارالذکر حرم نورانی حضرت ثامن‌الحجج امام رضا علیه‌السلام…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farsna/448878" target="_blank">📅 02:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448877">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaYp7TIUPOuVUS0ohV8lWCLfHjyaLO-ZS8XcpQKuXAWa2UNajRdQNmrVNeUNtaxH_Jb_PV6xEmej-YK7uA2Vf2A9dJPBNPKbP7wj9MCKEHSjTIocYxfqR647NOf7PG4SWJQ39e3J2EEAG8X5ZpSJgnuXM5-8tGrrJ8Ll6_9t3WDj3tX6OSCtk3c4n1lHvKHnyFcTtlIPYPleimGoEm6UxkOodTJS0ZjwHyUoxWwZDVDec8tG0ePqoCx47rNq8lWElP43KHHpqDPNOTWHDsLPxcIpoLfjDU8CZhHqXDaHQnMYdvHX3jBTGL48OSv8xk4LEGH_RTFt-7bDspu_KVcnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر مطهر رهبر شهید انقلاب اسلامی در دارالذکر حرم امام رضا(ع) به خاک سپرده شد
◾️
پیکر مطهر رهبر شهید انقلاب اسلامی حضرت آیت‌الله العظمی سید علی حسینی خامنه‌ای قدس‌الله‌نفسه‌الزکیه بامداد جمعه ۱۹ تیرماه ۱۴۰۵ در دارالذکر حرم نورانی حضرت ثامن‌الحجج امام رضا علیه‌السلام به خاک سپرده شد.
@Farsna</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farsna/448877" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448876">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2631b20bf0.mp4?token=bRX9LtokoXkOWKgF5FDOpKHwILRabyOG4EYyb13KEfzc38Zw01fZyH3WfS91tGuD4_OpQVZbeMYCO656avVL2qcCk4shPcWSJnEkeytnI8Ts829fP-GLAQQduZVW1QebQbqSD5mMxyyiSYTFRReNlCzyQ9t9-bBimDvLFF8-mDuG8IWWnYJ8e-8hwnfathnpyUxAASWS3MBbvXTXLPI2ZjcDIMA0YtDuwfXXCzXTAxER_B9BnxYwcCYDTeKP0h4wxdKwgXvdm0U8qWb62XUI4eGDffIJx2N-9rln4z027LzsRh7E2HUpGFVQhj1qynS_lfNRqr22XCTXXCWZD_PqVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2631b20bf0.mp4?token=bRX9LtokoXkOWKgF5FDOpKHwILRabyOG4EYyb13KEfzc38Zw01fZyH3WfS91tGuD4_OpQVZbeMYCO656avVL2qcCk4shPcWSJnEkeytnI8Ts829fP-GLAQQduZVW1QebQbqSD5mMxyyiSYTFRReNlCzyQ9t9-bBimDvLFF8-mDuG8IWWnYJ8e-8hwnfathnpyUxAASWS3MBbvXTXLPI2ZjcDIMA0YtDuwfXXCzXTAxER_B9BnxYwcCYDTeKP0h4wxdKwgXvdm0U8qWb62XUI4eGDffIJx2N-9rln4z027LzsRh7E2HUpGFVQhj1qynS_lfNRqr22XCTXXCWZD_PqVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش صدای خواندن تلقین بر پیکر آقای شهید ایران در حرم مطهر امام رضا علیه‌السلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farsna/448876" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448875">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxLJSS1EIPR5pgypuo1XSZHBexYUgWwehA-fuNXazxpDg7Jdd56mevJRV8J2pNGqsVBBUooBpJlocB1vZIEttati625daRHrpahPlVOxmgtNVwo6-r7O3FpcU0bmjZClHFxwRkB3tfmDpHnuQ0FHmHqRTiqJSZ1tbTTPUv6UqDoUqr6nxenCBLoQLSdv8Wid0y7EQRrNH3x9xWV_qnbSEI7XbjQtF63FxGptTtC-PiNizxVlRZRI4hi54Lh5rgowLTK5eH280xRW4a0FJBNiTrjz1JtfOZZ9fGlrMama_Iv1D2UjUx-aMKYgzuiFuMG0PUNGfdDCVJShCIshzGwhCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و امام شهید ما در آغوش امام‌رضا(ع) آرام گرفت...
@Farsna</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farsna/448875" target="_blank">📅 02:29 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
