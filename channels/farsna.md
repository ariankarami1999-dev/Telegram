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
<img src="https://cdn4.telesco.pe/file/BmCTUcrabdTrpcjKLd0_GrR-Y2ZaWa7NbIXqmXOKND7PTUYW5VVZj_w2fOkGmzFf3v9x78k4QFLdk6xQUf_jUcG0xPqqrH3eHFGhnQCvlR3L2k21QxCQ6rca5-9xBrx-EGMa-GE6uIirPwBGu39ieFmn0PLupRSM7pbxNU3AMlcaJYjF4jfUUzni-lukD5w4HRS0gl-LzRGPMJaJzg1QrknzCgjLkI2oERLxGQphOXp8rYOTbnaiPNKqrhfCdNTdByxP9SvFzj0SGKcj4dOxRWJ4zVlq8L5IkCjSERi0NA25avgrrnqyBA-jNH9c5xvsAXR8lfIIdQfF-wc3tUIvdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-448427">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbf4c36af.mp4?token=QXkx-NG5pe9pCCokckf4J3B26Mh3oXOpqhBtH7ekovPlxePxcIV-WIr3h8KpLkXitFTeQD13eGM6xsO5SDNv29mn1v0vcjRdxHPUzt_JcwVI-k5ofhi41BSNZyiaUdpTsWI3vKetb1Wp9janylbFioxtxGgp-Dm0GVU-Gg4_gqJZKUrOMdbWFQfoPkG_D7FtnJFqxPHrE_Fd4qS6B361Fsfk2iSREO-dg1w45h7wbPPbC5Lv8zvs1K0qhzTsCkx6hHjRa78Zasr7TpYcaum4RL8Q9gMmFrI5xaF43tbcTT_C57M254pauJiMzH4ND6UIx8wYsOvLwDAc6-hhSoEN0gngLE0ufAqpmCld-Z0mPVwqpGYQPDPNq66dW5p5ZQtYiuFQI0kbM4eRwXZSVtPHOAMaQ-hN22WNpAUTCA3X1f2CNFsk8ml6MOzvjGC2i4VB6I-U81nzr7kcWAcsh1otA8vUiAq2U1W0uoYd2oCKPPhXYFT7jo3M_ZWj1MD7Xx08Dj1ypWwow2cG2javI2IAFANuRuwAysfxCelr-k2cAn5I7EAKWppmOL7-NSmrPaNJcBun73ONvP0mCyPP-0-IW_7C3SIRcYva37LeC4iZmc640j7Sq72lql8mcNy4YZcKpCzWtNhtMFmUEp_sSD7kAZhFKFfNnOWlJyelMIqFbps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbf4c36af.mp4?token=QXkx-NG5pe9pCCokckf4J3B26Mh3oXOpqhBtH7ekovPlxePxcIV-WIr3h8KpLkXitFTeQD13eGM6xsO5SDNv29mn1v0vcjRdxHPUzt_JcwVI-k5ofhi41BSNZyiaUdpTsWI3vKetb1Wp9janylbFioxtxGgp-Dm0GVU-Gg4_gqJZKUrOMdbWFQfoPkG_D7FtnJFqxPHrE_Fd4qS6B361Fsfk2iSREO-dg1w45h7wbPPbC5Lv8zvs1K0qhzTsCkx6hHjRa78Zasr7TpYcaum4RL8Q9gMmFrI5xaF43tbcTT_C57M254pauJiMzH4ND6UIx8wYsOvLwDAc6-hhSoEN0gngLE0ufAqpmCld-Z0mPVwqpGYQPDPNq66dW5p5ZQtYiuFQI0kbM4eRwXZSVtPHOAMaQ-hN22WNpAUTCA3X1f2CNFsk8ml6MOzvjGC2i4VB6I-U81nzr7kcWAcsh1otA8vUiAq2U1W0uoYd2oCKPPhXYFT7jo3M_ZWj1MD7Xx08Dj1ypWwow2cG2javI2IAFANuRuwAysfxCelr-k2cAn5I7EAKWppmOL7-NSmrPaNJcBun73ONvP0mCyPP-0-IW_7C3SIRcYva37LeC4iZmc640j7Sq72lql8mcNy4YZcKpCzWtNhtMFmUEp_sSD7kAZhFKFfNnOWlJyelMIqFbps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیام ملت عراق در بدرقهٔ امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/448427" target="_blank">📅 21:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c627a93b.mp4?token=dMPoa_9k_ntnJdoW-UuWWuP9PwTQg_Mb4nT0uddbmUbPxLAL0hxCUV6jWQ0fawDxpIttnTxOgsXTej0ezp3eND7GJ1ldv3ShyMK9SowzpseEq61e6tnowFfhLLdN_WiY7_zwm0kx92zJHhJXN794TvRGXSfwOJy9OTl5ckw904znkuf6TooERpb2qyJXFztzAVXAZ_0l683RIyKv1Tls0dRAzuBi7KeX-Tuabpx2r8YRO9AoxVrQ29rf8h1FC7wBrf1juT3DYR2NPxpugztPJYp_8QnlG7j4QUNJ_LRi_vgZ6MSxxBZtqs2TRBmIebH0bShnKKnUAJ3Q2tVEo_eONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c627a93b.mp4?token=dMPoa_9k_ntnJdoW-UuWWuP9PwTQg_Mb4nT0uddbmUbPxLAL0hxCUV6jWQ0fawDxpIttnTxOgsXTej0ezp3eND7GJ1ldv3ShyMK9SowzpseEq61e6tnowFfhLLdN_WiY7_zwm0kx92zJHhJXN794TvRGXSfwOJy9OTl5ckw904znkuf6TooERpb2qyJXFztzAVXAZ_0l683RIyKv1Tls0dRAzuBi7KeX-Tuabpx2r8YRO9AoxVrQ29rf8h1FC7wBrf1juT3DYR2NPxpugztPJYp_8QnlG7j4QUNJ_LRi_vgZ6MSxxBZtqs2TRBmIebH0bShnKKnUAJ3Q2tVEo_eONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید تنها ۲ کیلومتر تا بین‌الحرمین فاصله دارد
@Farsna</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/448426" target="_blank">📅 21:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d210620e72.mp4?token=he8LUTNhyOrnzQFWnaoCK6LENMQ5mV7dtBQBberMlS-q-lQwZs33eWaARTU0t22oZswJ6T7qVU5JIQ323u2xyfYj5xEqegrLmfBjuMYBGTQR-hJ20DB1zORO1yVV93NL7VK0QjYaerkmY0Cn9MSdFLY6b8x7Cid3mxzsCNiXHkhpEprRRDqyeFrqqg5h7YFUyuarnwOoNmxPruDe69juWjoz8oGXWsRTagODjiSNy_5lx5_vy5Tr0SrS3IioCI_YHfF41sfcZmxfbITj0EehkPxFv34rfuf9q8NcipSeJqOarIUyVDcSXwUW_9ACmwYotiDDneTWP-jsq4ciGem-vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d210620e72.mp4?token=he8LUTNhyOrnzQFWnaoCK6LENMQ5mV7dtBQBberMlS-q-lQwZs33eWaARTU0t22oZswJ6T7qVU5JIQ323u2xyfYj5xEqegrLmfBjuMYBGTQR-hJ20DB1zORO1yVV93NL7VK0QjYaerkmY0Cn9MSdFLY6b8x7Cid3mxzsCNiXHkhpEprRRDqyeFrqqg5h7YFUyuarnwOoNmxPruDe69juWjoz8oGXWsRTagODjiSNy_5lx5_vy5Tr0SrS3IioCI_YHfF41sfcZmxfbITj0EehkPxFv34rfuf9q8NcipSeJqOarIUyVDcSXwUW_9ACmwYotiDDneTWP-jsq4ciGem-vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نجف دریا شد؛ عاشقان رهبر شهید موج زدند
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/448425" target="_blank">📅 21:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448423">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پیکر پاک رهبر شهید انقلاب به عمود ۱۲۷۹ رسید
🔹
مسیر نجف به کربلا ۱۴۵۲ عمود دارد. @FarsNewsInt</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/448423" target="_blank">📅 20:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448421">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLIKouxfJVzFmOhCiBKnjr7UB-hrfuCCHPmPBd7dOMxajTvfFPP_mz2LZtLNhrxfHnXNsTAZic7S41ZZuL7CS_apg2npcAgF40a8miQk9fkHWQUQUef39l-vrUGmn1bQo3AXF2CmfZ014u1WRl0FGQHcgryd-cnEY9yeun17E0A0NFMZsO-uvJupQaNVQe74QpwEkI9lxZ9mzHJu25IF1R3uScCDAvNpkejgXKIIb1GNyjJsy6xDlKzUr2vv8laUxvxzAH9zITVCXrIE7GRE2GBSw3bCGWhqk-zrUJ-eCCgKNDmRYxpEEXnlYRV1rTaohWm4x5PW7adlYZ1UY1Ixiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: ما بی‌ادبی ترامپ را در عمل پاسخ می‌دهیم
🔹
خطاب قرار دادن ملت متمدن و شجاع ایران با زبان تحقیرآمیز، از عظمت آن نمی‌کاهد.
🔹
ایرانیان به‌خاطر تمدن، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند.
🔹
ما ابتذال را با ابتذال پاسخ نمی‌دهیم، بلکه با عمل پاسخ می‌دهیم: بی‌باکانه و با شجاعت فراوان.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/448421" target="_blank">📅 20:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448420">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFzKbLwiW8RoehnAgoB2OTmgcAFZo617WDVULFXh2f31d9IF86A2Dj3HElxdtm9tobIZIEdnj47JP6lpJarJ5pExVmmDBs3AHg2s_GNn6X3NFZsERKzaHzpj3q481cnidAV04CGod7rc9aao9uzG1mzYsFUjSJggDtpLH-Jx-Xahrn2f3htfglJ7WF89QKON4AB8KMciSIRcjw8Dy66IRDAhNs4YHIRi47ilqIRVbs1cLBDuou9lXUCNincy0c1Qx01ZEsP4k9H0N9owKf6wAmiDoY6gULlZBcwq7gCGeujeijFBgH_Y16ZVLif58fLYFvQVO8XMChBqR8iuyrA8yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور سردار قاآنی در نماز مغرب و عشای حرم امام حسین(ع
)
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/448420" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448419">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12cc54c351.mp4?token=qIawvgN92wlzmRJ1zlQ0dqCesEndvEQMJxapbZBPewaj20k9Vhbtz53mqmFg6lGPM0n79G-5VI1-IXqOXF0IycuPsYFm05HU9swN39rZn7AVvrSK1abL5LtwkS61h8VsGx_Yw_Naq7-XU5fNoRoxZQJvyWFK6am1cbLM_ewrbZW_32P07Ze7P4PG9YzFLdac8dSA_-kPoIgfjtQJWISs9QHgguZ_OXREWT9VxbYkyb3YXTspz04jWXrJpGWqF14-eLwYgPpfzT0pvFJRdARfInbwStpAJE5FYv_FcRgpj8ULdlecJG70O7O81siAFwNQiytgUmUmINCruNSa0akHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12cc54c351.mp4?token=qIawvgN92wlzmRJ1zlQ0dqCesEndvEQMJxapbZBPewaj20k9Vhbtz53mqmFg6lGPM0n79G-5VI1-IXqOXF0IycuPsYFm05HU9swN39rZn7AVvrSK1abL5LtwkS61h8VsGx_Yw_Naq7-XU5fNoRoxZQJvyWFK6am1cbLM_ewrbZW_32P07Ze7P4PG9YzFLdac8dSA_-kPoIgfjtQJWISs9QHgguZ_OXREWT9VxbYkyb3YXTspz04jWXrJpGWqF14-eLwYgPpfzT0pvFJRdARfInbwStpAJE5FYv_FcRgpj8ULdlecJG70O7O81siAFwNQiytgUmUmINCruNSa0akHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: من هدف شماره یک ایران هستم.  @Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/448419" target="_blank">📅 20:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448418">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3c01c6a7.mp4?token=EDl3Emxpj682fKQhxnCcvsnjfUhdj8slGljJwr8mx_V7ds-SAF7LIRsdi9O69HbWi0Z5-VpAUVS7IATurBVzroNQEeQZDW1fIEbRXhUrbz_0tqQRERZ3x1gj0qADDe9_VDQFpWQ4ZTau0SvCOx19q_Z0CEEPlvHhfkWS7xt6_k2Jg0G0t_9u_6Fm7cq2NYmB5BQWeSls9ClJzayYIGgS6RZjD4-wwH_naRDq4hR6H3h1lCWWjScrsPcEY577JEQU10RgBev3u6IUuYKzYbIX41U635GZrs8Yne9VUzrD7Gmb5QgoFy_m7z4HZNkF6Lfoe6gN1MdgbG3KMiAotwGjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3c01c6a7.mp4?token=EDl3Emxpj682fKQhxnCcvsnjfUhdj8slGljJwr8mx_V7ds-SAF7LIRsdi9O69HbWi0Z5-VpAUVS7IATurBVzroNQEeQZDW1fIEbRXhUrbz_0tqQRERZ3x1gj0qADDe9_VDQFpWQ4ZTau0SvCOx19q_Z0CEEPlvHhfkWS7xt6_k2Jg0G0t_9u_6Fm7cq2NYmB5BQWeSls9ClJzayYIGgS6RZjD4-wwH_naRDq4hR6H3h1lCWWjScrsPcEY577JEQU10RgBev3u6IUuYKzYbIX41U635GZrs8Yne9VUzrD7Gmb5QgoFy_m7z4HZNkF6Lfoe6gN1MdgbG3KMiAotwGjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۴۸ ساعت گذشته در تنگه چه خبر بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/448418" target="_blank">📅 20:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448417">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ae0700d.mp4?token=YdDvF3rgColjB3uKOR8uOEXiGmozNIAh7MuhkBACt9zEUK6zgQNUw9mBbYzqWiXgiqy9v0bh89-Rplo1O0f9Qu4kn31loKYTNipB6kZElcF--0uH_36JO4MFgL44Rn7kPqfgTzu_fGFoE0vD4rp21BVtSYm35DMOmnd9VmizSvs1dbq3HANLpm5SVik7nFGHAGT4Z1P3n9knkzSOJlhZc8bq-XFqMESQ0AbJmfPox5gg5TJ8y3VXkJ6BLDRafsBlPLjr3fKvXjyoiWLqOq1VJqhHuBmuWpPQPY5e_hwYrit3PJJ_Y-k_l38ZsGHf_w3rFfQbAz0dZcqytiAR4kY9QoFyAlCax2KnvtGxcik0Ii2qC19uWm5Pf_KdLl-Q1SYSRYoYq259SioIP1P91zyxdXCpHvi24izNiZYw8dYr5w6KlUpjCHcjcgN_40j_7_Fr59rL4OZ3x8pvPCmIfj3cPkpjlQO5nlyckNQicKJqkNN9cpoYCyt2WJop7UVdl2t4fdvUwS4Lhf1D36i3T7zQiLn612tijMYtckiS08q2P9ymEf9CuepRobgJOxIW1ZNXuPA9nsTZ_WzR5Oz9WRV0ohiCSqb1z9Mv9OrlbO07mdnx74H-dNVbXWjUAbir0YZ16qyCJwHTDm1zrzqTaKcFpUcYnoi3Kq4tbAUeplj-1zU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ae0700d.mp4?token=YdDvF3rgColjB3uKOR8uOEXiGmozNIAh7MuhkBACt9zEUK6zgQNUw9mBbYzqWiXgiqy9v0bh89-Rplo1O0f9Qu4kn31loKYTNipB6kZElcF--0uH_36JO4MFgL44Rn7kPqfgTzu_fGFoE0vD4rp21BVtSYm35DMOmnd9VmizSvs1dbq3HANLpm5SVik7nFGHAGT4Z1P3n9knkzSOJlhZc8bq-XFqMESQ0AbJmfPox5gg5TJ8y3VXkJ6BLDRafsBlPLjr3fKvXjyoiWLqOq1VJqhHuBmuWpPQPY5e_hwYrit3PJJ_Y-k_l38ZsGHf_w3rFfQbAz0dZcqytiAR4kY9QoFyAlCax2KnvtGxcik0Ii2qC19uWm5Pf_KdLl-Q1SYSRYoYq259SioIP1P91zyxdXCpHvi24izNiZYw8dYr5w6KlUpjCHcjcgN_40j_7_Fr59rL4OZ3x8pvPCmIfj3cPkpjlQO5nlyckNQicKJqkNN9cpoYCyt2WJop7UVdl2t4fdvUwS4Lhf1D36i3T7zQiLn612tijMYtckiS08q2P9ymEf9CuepRobgJOxIW1ZNXuPA9nsTZ_WzR5Oz9WRV0ohiCSqb1z9Mv9OrlbO07mdnx74H-dNVbXWjUAbir0YZ16qyCJwHTDm1zrzqTaKcFpUcYnoi3Kq4tbAUeplj-1zU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای اربعینی امروز نجف
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/448417" target="_blank">📅 20:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448415">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXYy3WE5i_P7rlc06O5QgHajNsRfbYg4jcjQPHCMMVDLQGumgfObccecqrgUrW945qR7VbwUrKxCfjLsHIE18C8dwUR3C3YSY6aqN-oJ85jGqAZd_uZr_oIxQoDv0DXE2yWhjZh3-7J7G-Egtm9SLDoS1JnEKsm-DNE86S4wJhfFLXs6C-CTNWSaUqwY-O2HFZlbCRhIWCkiNBQ1F0xyHag_ueXaTibCYXEmFVEVFK4cz7nTL8B7zFag9Zcg9R1ptQcdPEKwS-x0k6-TzdJ2wQ0L310ocdui-zn05gBEZIunTMdbGbQSkJDwZAml-NmX9UQVbt15qGuq3OmrIew9-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود
🔹
در رویارویی آینده، دشمن با تهاجمی همه‌جانبه و غافلگیرانه از سوی جمهوری اسلامی ایران مواجه خواهد شد.
🔹
گزینه‌های زیادی در اختیار داریم که حتی در جنگ ۴۰ روزه نیز از…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/448415" target="_blank">📅 20:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448414">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e389130ae.mp4?token=jCu5Sf6cSCn0JWeXwoxCw81a4iDAFC7TFg5yUrn1eM4Kycre7dyZOEcZ9duLSEH9QtyfaXBluMt4TBifQy7YtBc2Sy_H81BrkwfbNVj58lsZNUkT64iiwMjDwONFb3b5-SAfJF8xDxRe5p5Gy4afScjMgm2plGpAeZeVNBEs8y83A_klx02i1Zx5rOjcNhx3yI7cO_HmqL9Bc-VQ3drRJriruZI9dEgXvIKUhW-r0NYOxoJViYGDhEsXqXLH2EyA56OVjCqYThIWkijIDuQuPIfv3hKptvT8dppTM1u5uKUTZB3gw6e_zRX9wH3uQV9-fG2T1h5oSRUypo1Q1FvfLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e389130ae.mp4?token=jCu5Sf6cSCn0JWeXwoxCw81a4iDAFC7TFg5yUrn1eM4Kycre7dyZOEcZ9duLSEH9QtyfaXBluMt4TBifQy7YtBc2Sy_H81BrkwfbNVj58lsZNUkT64iiwMjDwONFb3b5-SAfJF8xDxRe5p5Gy4afScjMgm2plGpAeZeVNBEs8y83A_klx02i1Zx5rOjcNhx3yI7cO_HmqL9Bc-VQ3drRJriruZI9dEgXvIKUhW-r0NYOxoJViYGDhEsXqXLH2EyA56OVjCqYThIWkijIDuQuPIfv3hKptvT8dppTM1u5uKUTZB3gw6e_zRX9wH3uQV9-fG2T1h5oSRUypo1Q1FvfLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمود کریمی دوان‌دوان درپی ماشین تشییع پیکر رهبر در عراق
@Farsna</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/448414" target="_blank">📅 20:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
منبع آگاه به پرس‌تی‌وی: در صورت تجاوز مجدد، تنگه هرمز کاملاً بسته می‌شود و ایران  ۲ برابر تجاوزات دشمن را هدف قرار خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/448413" target="_blank">📅 20:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448412">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d591c088b.mp4?token=pjc45IZL9oUBIH9fXQiOzpMTz911Mvj0rqxbv8_USnObOqirD_PGhcW9zOP-QElg5xJ0Bv87ZdbTaZs0ZIj7eEskduw1kIVsnBV7OIvXYv5yPAMq5sf6YEjsrOyB4m-zUEIY72OiDA5E7j9TRHCqwIeImDgiH3zl3ZG77pE5gM7pUq8tPgjdGOxqpvhRSMVC2AnaNc1_p9MZUyfby9Dx71WBV9OSmTx_cgqcxJStbjS9m1A8HzV9tzuaRvaJf87VwbBssUKVYi2qxlyt-w68QvyvgRk2RStAJQqpV7YpcxgWpYzDZSVc2NOeTYHj1h9rooze_W35ZwU3WHsfa6_6Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d591c088b.mp4?token=pjc45IZL9oUBIH9fXQiOzpMTz911Mvj0rqxbv8_USnObOqirD_PGhcW9zOP-QElg5xJ0Bv87ZdbTaZs0ZIj7eEskduw1kIVsnBV7OIvXYv5yPAMq5sf6YEjsrOyB4m-zUEIY72OiDA5E7j9TRHCqwIeImDgiH3zl3ZG77pE5gM7pUq8tPgjdGOxqpvhRSMVC2AnaNc1_p9MZUyfby9Dx71WBV9OSmTx_cgqcxJStbjS9m1A8HzV9tzuaRvaJf87VwbBssUKVYi2qxlyt-w68QvyvgRk2RStAJQqpV7YpcxgWpYzDZSVc2NOeTYHj1h9rooze_W35ZwU3WHsfa6_6Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غروب دلگیر کربلا در روز تشییع رهبر شیعیان جهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/448412" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448411">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
ترامپ: من هدف شماره یک ایران هستم.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448411" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448410">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-CAfkfgYU7FuSysYKOjrqusjrbyh3m-4b4WzM8P-BaFU6abvCex0V6c1WTHLw1d7Pv_O4FLdDS0CsM1Ncye1ueMvUPx1hpqP9cSdBrPHEyy28tgDfLe0L6ZtrP686xvypXQNEF7itrupeomU760sCEPgh1YHwnFbg61n3TM5LZpML0KCioN7ji3R08rzD_CZp74_sR_4j7ilC-k6YGHZVoW6HPEW0asYflaOdJKPQihUrMovK3zhf1swJ2c-_-bfEsMtgivTed-7Lrd1-2pRuR1Bp1ZaxwC3VDh7LEM9Fy1RWLdB6sA-x8VIHJu4WLxWMCN0CGNUxfaj-RywVvG7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکر پاک رهبر شهید انقلاب به عمود ۱۲۷۹ رسید
🔹
مسیر نجف به کربلا ۱۴۵۲ عمود دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/448410" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448409">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc350b6bdd.mp4?token=SzCIrPacYY7zSBRycRzME_5ggq4KJhQqRW8C780KoCAHKcth06nY_rj75mb9TIj_PIXd33zgEKj5sM3I52QhoBe_v5KJS-QPFISRDQmMWHbBfFFH4ACmJVZcY5H8_OFg_XIYTn55SaXjVgQtvlG2vIuHb0UWtTsYGZ_RbbqA9i2fsx6-g6j2Eer-0rj9wszeLuWGEtZJyvQQSz7U52T4mi_QAw6n_-i9EwevVdaxeMQ98kchK9U2XZWqS8l2t-ScRyWEP1Y90eOyNxfP0ZVnmfysxZJuqBOCFV-MeUkv0u5Ykiyda2Ij2mssF8J-4gKAU0ViBUoOvAcdBZZjU9ouVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc350b6bdd.mp4?token=SzCIrPacYY7zSBRycRzME_5ggq4KJhQqRW8C780KoCAHKcth06nY_rj75mb9TIj_PIXd33zgEKj5sM3I52QhoBe_v5KJS-QPFISRDQmMWHbBfFFH4ACmJVZcY5H8_OFg_XIYTn55SaXjVgQtvlG2vIuHb0UWtTsYGZ_RbbqA9i2fsx6-g6j2Eer-0rj9wszeLuWGEtZJyvQQSz7U52T4mi_QAw6n_-i9EwevVdaxeMQ98kchK9U2XZWqS8l2t-ScRyWEP1Y90eOyNxfP0ZVnmfysxZJuqBOCFV-MeUkv0u5Ykiyda2Ij2mssF8J-4gKAU0ViBUoOvAcdBZZjU9ouVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار خطاب به ترامپ: جنگ ایران برای شما به یک بن‌بست استراتژیک تبدیل شده. چرا نمی‌توانید به این جنگ پایان دهید؟
🔹
ترامپ: جنگ ایران یک موفقیت نظامی فوق‌العاده بوده است. ما ایران را خلع سلاح هسته‌ای کرده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448409" target="_blank">📅 20:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448408">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a11ad69b.mp4?token=G33G3wlMH8iWUcozDG_7k053Dq1aR1-ptWB-kpq5EopYqNNmrpuR3g64TlUjHITSeiYJtQNuQ1EQLuVjzGLuH0i6W72Z71XgZeIVNf5fIN69mT8--EL8V89eK42UaibpCPZM82cHqIlWTSpmYzQvtqy1YlIlV4CkBpa9sAbrSpfrNnynwCcmufPli1zYHUnfDu25ZalFGuz8ajqhkten5cC5b65KRXycNHAOKCcb8ySgACciWyUWNs8Zfq3C4OGG7fmP91mFLHrV166GU7efRoJtyle6RtDH2SsL-0taPZYWJ19ijiUZnzHVoc5pK7mavUVXBFiMdOiLu-tNbxrrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a11ad69b.mp4?token=G33G3wlMH8iWUcozDG_7k053Dq1aR1-ptWB-kpq5EopYqNNmrpuR3g64TlUjHITSeiYJtQNuQ1EQLuVjzGLuH0i6W72Z71XgZeIVNf5fIN69mT8--EL8V89eK42UaibpCPZM82cHqIlWTSpmYzQvtqy1YlIlV4CkBpa9sAbrSpfrNnynwCcmufPli1zYHUnfDu25ZalFGuz8ajqhkten5cC5b65KRXycNHAOKCcb8ySgACciWyUWNs8Zfq3C4OGG7fmP91mFLHrV166GU7efRoJtyle6RtDH2SsL-0taPZYWJ19ijiUZnzHVoc5pK7mavUVXBFiMdOiLu-tNbxrrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: وقتی جنگ شروع شد تورم ایران ۵ یا ۶ درصد بود اما الان تورم آن‌ها به ۳۵۰ درصد رسیده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448408" target="_blank">📅 20:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448407">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5254493837.mp4?token=Hl7r3_XC6mjxWf7DNOlZ10CCJ2z9UXKSCjlSC-64OTeroUEc_dBqAi1xPbERcG6EqRdJPtJi1RaQ0fou81sHrx4HCNVLk2PfuOAN_mJtsCIQkSL0IDT3PbsOBV8PRRHeI_PjLzURfpsOF647sIodhgcjNgfbwFT9rLfTyLKk8e4NE1nQ7NqRSlNPmHZyUtDlRGjb7ffDOcWstv6Nze_PM0NiZUTRovfGSMY6mO8QjIjwmOyKaX3xWYXZTvQRV6RTqAGmP8o1MLhibn14wxzNaAe6d_sdSq9HFtw2f8bSQ-nSByGBm1Gbn3oYMdmq2bmH0aVyzofcjtkQd1LcUT3GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5254493837.mp4?token=Hl7r3_XC6mjxWf7DNOlZ10CCJ2z9UXKSCjlSC-64OTeroUEc_dBqAi1xPbERcG6EqRdJPtJi1RaQ0fou81sHrx4HCNVLk2PfuOAN_mJtsCIQkSL0IDT3PbsOBV8PRRHeI_PjLzURfpsOF647sIodhgcjNgfbwFT9rLfTyLKk8e4NE1nQ7NqRSlNPmHZyUtDlRGjb7ffDOcWstv6Nze_PM0NiZUTRovfGSMY6mO8QjIjwmOyKaX3xWYXZTvQRV6RTqAGmP8o1MLhibn14wxzNaAe6d_sdSq9HFtw2f8bSQ-nSByGBm1Gbn3oYMdmq2bmH0aVyzofcjtkQd1LcUT3GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: احتمالاً محاصرهٔ ایران را هم برقرار کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448407" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۸.pdf</div>
  <div class="tg-doc-extra">4 MB</div>
</div>
<a href="https://t.me/farsna/448404" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448404" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368b999813.mp4?token=kjFpsscl7grUMMJT_y67Y_sdsLZvIThrxzvVL58dS4p63DCymJhOFaBmNNBrtVXosQ5BbvXyXllUaEUlYMWnvo2ttKCIroWcq9DnyTQSQyY3eorM_2Vz4-w6rFnux9_TFBsaGepR84Nrz5f0SZnxh3y7a_vknnQg9Rq0fUEn1JVEKOL2keOzxYZJfX20BxWf-docgUgBugXYNGclUVJSfXN3t41d4jiaimRoo25zpsLCG0xoy7SHqF0qYwJpMzEB2GbH5BGb193fmuZaGDgbkqKapVyobHhqYIpcSu3K75Iv9WJyHzIAZq7bIpAyDpKh5PCFDjiaHpcXWYSvhtFPBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368b999813.mp4?token=kjFpsscl7grUMMJT_y67Y_sdsLZvIThrxzvVL58dS4p63DCymJhOFaBmNNBrtVXosQ5BbvXyXllUaEUlYMWnvo2ttKCIroWcq9DnyTQSQyY3eorM_2Vz4-w6rFnux9_TFBsaGepR84Nrz5f0SZnxh3y7a_vknnQg9Rq0fUEn1JVEKOL2keOzxYZJfX20BxWf-docgUgBugXYNGclUVJSfXN3t41d4jiaimRoo25zpsLCG0xoy7SHqF0qYwJpMzEB2GbH5BGb193fmuZaGDgbkqKapVyobHhqYIpcSu3K75Iv9WJyHzIAZq7bIpAyDpKh5PCFDjiaHpcXWYSvhtFPBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهد، لحظه‌به‌لحظه به بدرقهٔ آقای شهید نزدیک‌تر می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/448403" target="_blank">📅 19:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c89662c3.mp4?token=QsmOYvv5xbAdBpcxe1BlIfKYbp6lcrVmPzF29ACMox5se701qhJsQ9FGb86ObgJs7CzbrXLsIa7ZnXDdJpVo9gTSWrK2PDikt-m3VbhLMrUteYIPb8FQyxcLMvnH8Dlh09_KPe-QEUmlTqQdbSmKg39d7fcFLg0n7KReN7QhK8aN-4zm6_LKOh1D7FdcY4ImM4_RIaTYLkvXtXxVstKFmB9ms_fCtnskOQTM0szgDNz2ylbbR6nLxW-qyXmrgl0xQ38Wo50GKmD0GdoxMtxcIhI_rIuva8I12ST1Nk6bLfqv9wg9uO8wlNQCAwMnoZ-h8PMbLWkPfdCZxVJeSEaTyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c89662c3.mp4?token=QsmOYvv5xbAdBpcxe1BlIfKYbp6lcrVmPzF29ACMox5se701qhJsQ9FGb86ObgJs7CzbrXLsIa7ZnXDdJpVo9gTSWrK2PDikt-m3VbhLMrUteYIPb8FQyxcLMvnH8Dlh09_KPe-QEUmlTqQdbSmKg39d7fcFLg0n7KReN7QhK8aN-4zm6_LKOh1D7FdcY4ImM4_RIaTYLkvXtXxVstKFmB9ms_fCtnskOQTM0szgDNz2ylbbR6nLxW-qyXmrgl0xQ38Wo50GKmD0GdoxMtxcIhI_rIuva8I12ST1Nk6bLfqv9wg9uO8wlNQCAwMnoZ-h8PMbLWkPfdCZxVJeSEaTyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم سیدالشهدا(ع) مهیای استقبال از رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/448402" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxSS2AH1YM-ryIgwAlNFeWfuy1vExdqI8g4c7mjIi0XZ-lAT-8a8sjIA2jmFFQDHp5A2NeB2wlzE4cmZ43wvZBxlCtdWEBzFAv0jeN1Kds7zrcOYl8SYnP4-aIXYxzGZWUfng4n7QbkXANhc-DYygNi6UsKHJZm2_OYxlskIWajKtNMggh1NhgrMisevJdqvSpNascM-N_kBveAp-8ygXHWNz3T8kOCLOTZP2rls79jtKIRcoqMFMP9l6-_u1DTMJ6TDYxHz5k89j8P7WgBhC54Lr2PU0c7pCFJs1KSgx9c0Wn43dNx5sBkoGrHiepHcdcYFLzCU3VI414-pFx2A7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌گهر از حضور در لیگ قهرمانان آسیا انصراف داد
🔹
باشگاه گل‌گهر سیرجان با ارسال نامه‌ای به فدراسیون انصراف خود را از لیگ‌قهرمانان آسیا اعلام کرد تا بدین ترتیب چادرملو نماینده ایران در لیگ سطح ۲ آسیا باشد.
🔹
در نامۀ مدیرعامل گل‌گهر آمده: این تصمیم واکنشی به فرآیندی است که طی آن ابهاماتی پیرامون حقوق این باشگاه شکل گرفت که امروز حتی اعاده احتمالی سهمیه نیز نمی‌تواند آن را جبران کند.
@Sportfars</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/448401" target="_blank">📅 19:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb8ef0ea.mp4?token=K31TNoJ0AQ7i8OYuPICTHDDJa-Z498ezxT5Nh7-hRozPLn4w7s_t14cMmdWlAA-6tIX8MG9-ct4UmZZIlYqo1HBcXcRLKTbGrCA7g_2pR5QarzdOLIErn5AaVTroYkBYUnOc-DoXXqZAWc03d3X6hs12LUQ3xXLr_QaxKKc-TDA5ejseUrZCzJJmCZBxVut5fVlZqEu5ffVdz3HqYEVhH8i8bWT-J5vOl09gwnSckRWZmABVFkeQEs-79ynYxiDST4fyY6Afs58FKcjGudX8_31sAZ8vfLHQCnaE9yYk0uv4-m0VVGNpAGyDi0k61sSUmpHHE4KBvZQ1n2cECnABfLzpOFnTA3XgWo1Tl6Vf3ommKepYsxIy3riBEchGLRSw7D34rJ_VM6HxpaVuLZlKCgCWkMc6a9u0QjhgjeOjrS0qfoWcKUQOJJrbMEVJ54DwHXrJbnXrqSgvIa_zLuN5vpNXK07SPbwA_scwQ6aCUJ5i9M3oEjIxIkH-eE1edOU-f1hjRgI0fXLwRABft1az2G_0dHro6oQo3Kr68LBdRuaNeLcDavy7GI-wH7VA7ze0SVnEIG8v8bsHZj71JfFaZLj9dBuRkxdSw2NE0H_1NIOekBf4BlL8K40a0s7aN1BGhie_qrckWCxKrSWXh7c56BeWwPSe8NPA4iS-ylx7PSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb8ef0ea.mp4?token=K31TNoJ0AQ7i8OYuPICTHDDJa-Z498ezxT5Nh7-hRozPLn4w7s_t14cMmdWlAA-6tIX8MG9-ct4UmZZIlYqo1HBcXcRLKTbGrCA7g_2pR5QarzdOLIErn5AaVTroYkBYUnOc-DoXXqZAWc03d3X6hs12LUQ3xXLr_QaxKKc-TDA5ejseUrZCzJJmCZBxVut5fVlZqEu5ffVdz3HqYEVhH8i8bWT-J5vOl09gwnSckRWZmABVFkeQEs-79ynYxiDST4fyY6Afs58FKcjGudX8_31sAZ8vfLHQCnaE9yYk0uv4-m0VVGNpAGyDi0k61sSUmpHHE4KBvZQ1n2cECnABfLzpOFnTA3XgWo1Tl6Vf3ommKepYsxIy3riBEchGLRSw7D34rJ_VM6HxpaVuLZlKCgCWkMc6a9u0QjhgjeOjrS0qfoWcKUQOJJrbMEVJ54DwHXrJbnXrqSgvIa_zLuN5vpNXK07SPbwA_scwQ6aCUJ5i9M3oEjIxIkH-eE1edOU-f1hjRgI0fXLwRABft1az2G_0dHro6oQo3Kr68LBdRuaNeLcDavy7GI-wH7VA7ze0SVnEIG8v8bsHZj71JfFaZLj9dBuRkxdSw2NE0H_1NIOekBf4BlL8K40a0s7aN1BGhie_qrckWCxKrSWXh7c56BeWwPSe8NPA4iS-ylx7PSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحدت شیعه و سنی در مسیر عشق به رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/448400" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846e3e4aaa.mp4?token=thviacvo3wtE4Kt9NFFUwWWa73d57Njc8wZcy58MmLmrIhlk4gkWxWX1LGhBJ6fHKXw-AOtISniStNabai9VgdFPxf5Y0VizZrNDwHZIQnuA1JNNrYC04LKDm75XvCIKvP8a_XMN-D2RFq4HeSzG3oyAqQ9gfS7tQvha2LpkeryM52iXRABf_arwZjAumZyYbfrjy_vdZqiB1jJncb5JOUxcnyZNpGuvq8B4lEaOJrvQzMPKcmibxnCyzDOBQCBCv-7EPJeUNsCaewGGpm-nCfq_N0E1_bKbRXomqcJp2F41KZxSyICdF-3z35J1EBN6LWsg8qUUXsH8LDVvr9Qe9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846e3e4aaa.mp4?token=thviacvo3wtE4Kt9NFFUwWWa73d57Njc8wZcy58MmLmrIhlk4gkWxWX1LGhBJ6fHKXw-AOtISniStNabai9VgdFPxf5Y0VizZrNDwHZIQnuA1JNNrYC04LKDm75XvCIKvP8a_XMN-D2RFq4HeSzG3oyAqQ9gfS7tQvha2LpkeryM52iXRABf_arwZjAumZyYbfrjy_vdZqiB1jJncb5JOUxcnyZNpGuvq8B4lEaOJrvQzMPKcmibxnCyzDOBQCBCv-7EPJeUNsCaewGGpm-nCfq_N0E1_bKbRXomqcJp2F41KZxSyICdF-3z35J1EBN6LWsg8qUUXsH8LDVvr9Qe9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشایر کربلا: خون‌خواهی رهبر شهید را فراموش نمی‌کنیم و آمریکا را رها نخواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/448399" target="_blank">📅 19:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a747ffd1.mp4?token=XYCae7Os-ebJLL6-u-87Y6CYFrlhV4mNGMXVPb88kVdAqf3Bv08KSsXfH7jt_Sv_TB5WOeXGTOTZXKTyxQnghpVBysrLpz1l2OECstQngOztGOkFGUFta_yKUwsTt2ChJoIcnGIQoAWpU2y-Yx4vQAb8QskYRp7BulD7oMwj5Hunz3loW56rvcnHHOLdmAvKU8ZBDc40tU7YDgZwyW5fmkjNgGQcrM6FnXvB1R65QxcbUwGL4R68fM6shefeGGZe58VoKFv-XdNO51hxOehk102C34CxidQkZq_KoMe19H43O3vKlaf7_tNtdWtNsIq3cidlalH2gOYjyJRzNqiPmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a747ffd1.mp4?token=XYCae7Os-ebJLL6-u-87Y6CYFrlhV4mNGMXVPb88kVdAqf3Bv08KSsXfH7jt_Sv_TB5WOeXGTOTZXKTyxQnghpVBysrLpz1l2OECstQngOztGOkFGUFta_yKUwsTt2ChJoIcnGIQoAWpU2y-Yx4vQAb8QskYRp7BulD7oMwj5Hunz3loW56rvcnHHOLdmAvKU8ZBDc40tU7YDgZwyW5fmkjNgGQcrM6FnXvB1R65QxcbUwGL4R68fM6shefeGGZe58VoKFv-XdNO51hxOehk102C34CxidQkZq_KoMe19H43O3vKlaf7_tNtdWtNsIq3cidlalH2gOYjyJRzNqiPmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر چین در ایران: همکاری‌های ما با ایران تحت تاثیر طرف ثالث قرار نمی‌گیرد
🔹
چین به‌عنوان شریک جامع راهبردی ایران کماکان از ایران حمایت می‌کند تا از حاکمیت و امنیت و کرامت ملی خود دفاع کند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448398" target="_blank">📅 19:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448396">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c54bed844.mp4?token=KeTtv3yXE_Ry46z5lldbVN7LPawkKP_wLKuejTi_xKTGxSSdl4AjTxLcgEh7fsYdZrt37WtJbxPEI6SXVCA0ACuJSNcEyupgdeWOb77XKeap5llE03RTrU20ivvv6k7WLDBYoVP-8iu8pbY_NFOifQJiqMIu03C-_1DIl9QvqpWfVopshBNcvNBxyvzsWhRZmeFKkKZB2W03I59CBfcWH7yHQmY6-eym-1z_Rn0qm1V1POY0yv5Okbh6xSAWS22SGjWTEb7GDjINvyJZtqKZ-9LtSVQVYi6kLcfO_I9kkx3-G10Oxwxo3QnNmANQ_3Z6S15uL6heO4BhBC4pMJu3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c54bed844.mp4?token=KeTtv3yXE_Ry46z5lldbVN7LPawkKP_wLKuejTi_xKTGxSSdl4AjTxLcgEh7fsYdZrt37WtJbxPEI6SXVCA0ACuJSNcEyupgdeWOb77XKeap5llE03RTrU20ivvv6k7WLDBYoVP-8iu8pbY_NFOifQJiqMIu03C-_1DIl9QvqpWfVopshBNcvNBxyvzsWhRZmeFKkKZB2W03I59CBfcWH7yHQmY6-eym-1z_Rn0qm1V1POY0yv5Okbh6xSAWS22SGjWTEb7GDjINvyJZtqKZ-9LtSVQVYi6kLcfO_I9kkx3-G10Oxwxo3QnNmANQ_3Z6S15uL6heO4BhBC4pMJu3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش زلنسکی به اینکه ترامپ او را «رئیس‌جمهور پوتین» خطاب کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448396" target="_blank">📅 19:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448395">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6553b9097e.mp4?token=tiC87oBpUp-ToNieKIOTIHNXZfSyGdfvyjcGkxzk4ajbKFJgR6DW-igaEeYcx-6zT0p-hudXzSakCqtCHt4mrozn87Dgotf7yjYa190npe5sDqEFNYO0iokU-vgbOJgQ_l8Vq-S-lv1WrgGHkF1SVnlyrToeh3TO_rqj_VkQpEvtQskeTbl3XJ5w5xygf2rWfywpBre6KWcyY5MO8zBf35oxULVUZSmr2G31yCEEfxq_9p5pnV6x3SQ2SmofqOdoeNo952x9sl1Mznosd5FHGeThnB9_yfkqp_jaeHZB6V9hULNpSMyXs2hwMx04EkvBw_08U4tFSwWdPPgx9OpNHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6553b9097e.mp4?token=tiC87oBpUp-ToNieKIOTIHNXZfSyGdfvyjcGkxzk4ajbKFJgR6DW-igaEeYcx-6zT0p-hudXzSakCqtCHt4mrozn87Dgotf7yjYa190npe5sDqEFNYO0iokU-vgbOJgQ_l8Vq-S-lv1WrgGHkF1SVnlyrToeh3TO_rqj_VkQpEvtQskeTbl3XJ5w5xygf2rWfywpBre6KWcyY5MO8zBf35oxULVUZSmr2G31yCEEfxq_9p5pnV6x3SQ2SmofqOdoeNo952x9sl1Mznosd5FHGeThnB9_yfkqp_jaeHZB6V9hULNpSMyXs2hwMx04EkvBw_08U4tFSwWdPPgx9OpNHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: پیکر مطهر رهبر شهید نزدیک بین‌الحرمین است و به‌زودی وارد این مکان مقدس می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448395" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448394">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f255e148.mp4?token=hP8igXXZAhPm-ADwKLsWsk0Meda9DQrM5Meg2ET0aHyWlx0m7CdaCW3pG-j4N_kmcObHjN3cy7Ozly28s7p_KNrmjm43kx3218aJrR5slMpvwpkFbm0BbK2xaHxwi-Hjit2KZzWvhAJ8jFwsPIxdp9VWUGZcO63ms8YpIU7M_mqyr7HGrq4s5N2Gmd54h2ntApatm6fLPSD22Wa7ge45Z0ySY7Etj0TcPsSygITnHuu8xEIZLS0XKSWhBK4qDAEgxmRayeNuyf7_I1r1CFHh4cBagNIG92foxhCv4oCg9isI8w86sPJHJ6Nz6wQQNYxNbbYeLEnVdmgQYlb4fpv_PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f255e148.mp4?token=hP8igXXZAhPm-ADwKLsWsk0Meda9DQrM5Meg2ET0aHyWlx0m7CdaCW3pG-j4N_kmcObHjN3cy7Ozly28s7p_KNrmjm43kx3218aJrR5slMpvwpkFbm0BbK2xaHxwi-Hjit2KZzWvhAJ8jFwsPIxdp9VWUGZcO63ms8YpIU7M_mqyr7HGrq4s5N2Gmd54h2ntApatm6fLPSD22Wa7ge45Z0ySY7Etj0TcPsSygITnHuu8xEIZLS0XKSWhBK4qDAEgxmRayeNuyf7_I1r1CFHh4cBagNIG92foxhCv4oCg9isI8w86sPJHJ6Nz6wQQNYxNbbYeLEnVdmgQYlb4fpv_PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر اختصاصی شبکه افق از حرکت سخت خودرو حامل قائد شهید امت در عمود ۴۶۱ به‌خاطر ازدحام جمعیت عشایر عراقی  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448394" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e7bfb4ad5.mp4?token=c0Z6W9_NjL-mk566pGiQjH5s1e7PQt7hsngSXfmM3NJ_l2n4btZt1CJgyAFIkLD-Y5TmKo4jmIcZVKNAzMk936TvOxDNqXABijXyDK_6lmp8FrRmKSR-SAQA5bL7XcfnJh6SRNzplpZ-lqoj5I0LVtZZlKRAEZIOICf76nyFF5znGizmMwuiFOS-TRYOhlO2TzW0GlOHeQr32lY_JGE5BYOomepm6-5LeNb9TdWP7BA2jPiq8I9USl_JbhLT6AOH1kI22PLRyUSX2WXPiyzNc56ajV3LfZR5y2Gke0NPB-9F5cvTDslaZAhLGIEam8pEEsYjV60DWb4TudV9bfHzeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e7bfb4ad5.mp4?token=c0Z6W9_NjL-mk566pGiQjH5s1e7PQt7hsngSXfmM3NJ_l2n4btZt1CJgyAFIkLD-Y5TmKo4jmIcZVKNAzMk936TvOxDNqXABijXyDK_6lmp8FrRmKSR-SAQA5bL7XcfnJh6SRNzplpZ-lqoj5I0LVtZZlKRAEZIOICf76nyFF5znGizmMwuiFOS-TRYOhlO2TzW0GlOHeQr32lY_JGE5BYOomepm6-5LeNb9TdWP7BA2jPiq8I9USl_JbhLT6AOH1kI22PLRyUSX2WXPiyzNc56ajV3LfZR5y2Gke0NPB-9F5cvTDslaZAhLGIEam8pEEsYjV60DWb4TudV9bfHzeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر اختصاصی شبکه افق از حضور پرتعداد عشایر عراقی در مسیر مشایه، حرکت خودرو حامل پیکر رهبر شهید را متوقف کرده است  @Farsna</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/448393" target="_blank">📅 19:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24537cb428.mp4?token=dye-wjF2CZzaVWHuevq_i2Hr2luouYXBj0RhIAKHAjQ81qEAjGjb_6rX7zPdfnClUluEVFVKbOmdxXRdssMo2QwWLxdc_OKNtTkKHYFn-VLo1U2ltFfgIel0ZrYlDHCaFfbIzlAJIIYX6po1lrGAU3hcpHVxSAxxbO4yxYrNj78ehThREVG7s4tP6ilnyHSBS_V3HWaU_LMZgqzh1PT3mqCTlBuqxoIcDFmLVKdwVD1t-3QN5iQ0J47_2BJgE4mycQ3a_7WDTZwNGxslqKKJb9fQeDprXkoM--HZrOQhE-1z0rNAJMzVVIuSZIbxKyQN0DhJkE2_e_GTbdpR261Irw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24537cb428.mp4?token=dye-wjF2CZzaVWHuevq_i2Hr2luouYXBj0RhIAKHAjQ81qEAjGjb_6rX7zPdfnClUluEVFVKbOmdxXRdssMo2QwWLxdc_OKNtTkKHYFn-VLo1U2ltFfgIel0ZrYlDHCaFfbIzlAJIIYX6po1lrGAU3hcpHVxSAxxbO4yxYrNj78ehThREVG7s4tP6ilnyHSBS_V3HWaU_LMZgqzh1PT3mqCTlBuqxoIcDFmLVKdwVD1t-3QN5iQ0J47_2BJgE4mycQ3a_7WDTZwNGxslqKKJb9fQeDprXkoM--HZrOQhE-1z0rNAJMzVVIuSZIbxKyQN0DhJkE2_e_GTbdpR261Irw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر اختصاصی شبکه افق از حضور پرتعداد عشایر عراقی در مسیر مشایه، حرکت خودرو حامل پیکر رهبر شهید را متوقف کرده است
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/448392" target="_blank">📅 19:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=aB_pLM6sQ5Cxjkny7ErWiieukRkDMBo7z4KXSce01trlmBUuhS3A-0EnGcig6DO3SWARooYyI0WnpTUx8bTDuGsSHSqTnbKUx5l1obSUx9c6eUTHwgo3e2Iyle9JzMyRmHRI8F-ChT2cSGHowwHVPzNdbOVAeI32kTtZSf1jF2KStDSn7p8A7gG2U-qroJvOD_s1eJyEUFuP3xsotBEeD4DX9_kbsQIFbqkGnNd2peIJNaTN7njgH4zzZ7GvpiUhx_RwWZxNV8RSwjkj-bw8d6XcIei2pgFMmJ72adb2pwMXgAe9HXOXCf73RB6TaZkfe7eFjGGdZP0dEBxOj7GGRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=aB_pLM6sQ5Cxjkny7ErWiieukRkDMBo7z4KXSce01trlmBUuhS3A-0EnGcig6DO3SWARooYyI0WnpTUx8bTDuGsSHSqTnbKUx5l1obSUx9c6eUTHwgo3e2Iyle9JzMyRmHRI8F-ChT2cSGHowwHVPzNdbOVAeI32kTtZSf1jF2KStDSn7p8A7gG2U-qroJvOD_s1eJyEUFuP3xsotBEeD4DX9_kbsQIFbqkGnNd2peIJNaTN7njgH4zzZ7GvpiUhx_RwWZxNV8RSwjkj-bw8d6XcIei2pgFMmJ72adb2pwMXgAe9HXOXCf73RB6TaZkfe7eFjGGdZP0dEBxOj7GGRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مرجع تقلید شیعیان کربلا در مراسم تشییع پیکر رهبر شهید انقلاب
🔹
حضرت آیت‌الله سید تقی المدرسی، از مراجع تقلید شیعیان در کربلا به حرم امام حسین برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب رفتند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448391" target="_blank">📅 19:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BewOJpupXww7mOsXYggmWOaeNlm2-mFBVG25RG79d4ikEgHYuQUgfbOCTcGXfEm32BCQ0Hl-ZNdCWF_Ez2zW0_tBmIw3mB_PKXiJCd6RVUQjXjuJDubA2_hIBCT0yyaoFPLpjM6aZH0cP1SZEQd-EftD_9mcVK0sXXT2h7t0C46U6Ng3Fcs02vB88cywrefDNiyBwEbzCoIDX4CRyV8SHuK8lJbYv2nfqcx9-04vf5l5tedXaxIbuznzA1O3ropQ4B17FKf7DigXckV-qhG4mD1ZrcatTxO5PbOiXjREhYUvdd09NU0cu0RnT8ZDdgRJQ6o1wC92xiGIz3no6QliMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸ قهرمان ارتش به شهادت رسیدند
🔹
روابط عمومی ارتش: به دنبال تجاوز جنایتکارانه ارتش تروریستی آمریکا به مناطقی از جنوب ایران اسلامی در بامداد امروز، ۸ نفر از دلاورمردان  نیروهای هوایی و دریایی ارتش جمهوری اسلامی ایران در بندرعباس و بوشهر، حین دفاع از میهن اسلامی، بر اثر اصابت پرتابه‌های دشمن به شهادت رسیدند.
🔹
سروان علی معینی از پایگاه شهید یاسینی بوشهر، ستوانیکم علی مهدی‌زاده، ستوانسوم حامددورای، استواردوم امیرحسین قاسمی، استواردوم علیرضا زارعی ثانی و استواردوم علیرضا بالیده از پایگاه شهید عبدالکریمی بندرعباس و ناواستواردوم شهاب امیدی بزی و ناوی محمدجواد روانفر از منطقه یکم نیروی دریایی ارتش، در این حملات، به مقام شامخ شهادت نائل آمدند.
🔹
ارتش جمهوری اسلامی ایران با تاکید بر ایستادگی تا آخرین نفس مقابل دشمنان، اعلام کرد که انتقام خون شهدای میهن اسلامی را از دشمنان این آب و خاک، خواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448390" target="_blank">📅 19:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود
🔹
در رویارویی آینده، دشمن با تهاجمی همه‌جانبه و غافلگیرانه از سوی جمهوری اسلامی ایران مواجه خواهد شد.
🔹
گزینه‌های زیادی در اختیار داریم که حتی در جنگ ۴۰ روزه نیز از آن‌ها استفاده نکردیم.
🔹
گزینه‌هایی مانند خروج از NPT، تغییر دکترین هسته‌ای و بستن تنگۀ باب‌المندب در کنار تنگۀ هرمز قابل بررسی خواهد بود.
🔹
طرح خروج از NPT نیز در مجلس آمادۀ بررسی است و اگر ایران با تهدید موجودیتی روبه‌رو شود، تغییر دکترین هسته‌ای نیز می‌تواند در دستورکار قرار گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448389" target="_blank">📅 19:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89016597b.mp4?token=YIUBcd_Vif87mpB751uyqNXUm-rzw9xUYcXjpJlmROyatGCR70YIBTi_4TUjVRSglSjUH1oKWgr8nD0_cIiocAMR85GUS00e476b-R-zrBoaSUfklfKq7TUY45tuPpPdOAsuLDwKO-47k5QA78m1LtcrR37x5U4jNZ9RH8QKa6F9yKdarbDUySh_JvBgkan1mwKInkJIi3JutQTPSQ-xPqg3aKUqRewFpW3xZUJORGDZrzT2X_jEaLEM_3QirOnXSxwfM6_5zWGniumr9PUeFU3Uaj4UsfQzYsVMQHMyR43OH30fQshYacO0q06uLwMIid2jf5I4Fop0TMLVKsSINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89016597b.mp4?token=YIUBcd_Vif87mpB751uyqNXUm-rzw9xUYcXjpJlmROyatGCR70YIBTi_4TUjVRSglSjUH1oKWgr8nD0_cIiocAMR85GUS00e476b-R-zrBoaSUfklfKq7TUY45tuPpPdOAsuLDwKO-47k5QA78m1LtcrR37x5U4jNZ9RH8QKa6F9yKdarbDUySh_JvBgkan1mwKInkJIi3JutQTPSQ-xPqg3aKUqRewFpW3xZUJORGDZrzT2X_jEaLEM_3QirOnXSxwfM6_5zWGniumr9PUeFU3Uaj4UsfQzYsVMQHMyR43OH30fQshYacO0q06uLwMIid2jf5I4Fop0TMLVKsSINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر چین در ایران: همکاری‌های ما با ایران تحت تاثیر طرف ثالث قرار نمی‌گیرد
🔹
چین به‌عنوان شریک جامع راهبردی ایران کماکان از ایران حمایت می‌کند تا از حاکمیت و امنیت و کرامت ملی خود دفاع کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448388" target="_blank">📅 18:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895864774a.mp4?token=Vygv7_marGdPqLKidP6fx_A10wfRMYsB8x4WnrGoazaNjjqhTrMocYKO1DtBxpVTx0hDmswIjpxZugxKy807xHVECETc4pGFrEZRHleqMkUW9FXjCHdhMQdKqJbhXwTA8oaDVdEPpdHm9ULedneycYl-8l4Z_FlYrw3Xa8icpOPBZ9DbsF7sPr_TCb8vXIiQPOBXKRRkL-ougS-aMbDZuFMRYgYNpReTusIyqhWFIvtyVdz1BXNpYuFKgEwjPQxtAYQ2PgkCr_YrV-l3XKPrKXDq8J1AKnJrhc8InqzV9pJ6aznFWEb_wiesvVUkZq3aX3r69ab7Xi7PWub8E-zKCUU2ixVFHnvlFuDd6QlnAv19gt-8JiyRpoV_iSrH1nOsxUJCU9d7b7thAu7sJcfNwLntKduyBcOQOXxP7MvDp0YcNCOFrw6WUOxZ0hUkJvG3O7tzy3Gkei-klYpzNTn_0eEyY_jxCvWhAg5qLcGi_YrTkpTrkPk4XYv3ybIGXQtitzkgPi064uOjoVSrgnYu7bITqQwpzv2mbagfYQY50YCzoedFoPXdBCgpo9dGqk8i5Xt9OfjrweAsZOnELmuYacSaG9lgncqwza_kzuJRfL8M7mg4gMlg1bRdO52mZzCjbvJx82WW0dX501wd6XjAhwGd6GvC-bJ2hxxozOFcW4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895864774a.mp4?token=Vygv7_marGdPqLKidP6fx_A10wfRMYsB8x4WnrGoazaNjjqhTrMocYKO1DtBxpVTx0hDmswIjpxZugxKy807xHVECETc4pGFrEZRHleqMkUW9FXjCHdhMQdKqJbhXwTA8oaDVdEPpdHm9ULedneycYl-8l4Z_FlYrw3Xa8icpOPBZ9DbsF7sPr_TCb8vXIiQPOBXKRRkL-ougS-aMbDZuFMRYgYNpReTusIyqhWFIvtyVdz1BXNpYuFKgEwjPQxtAYQ2PgkCr_YrV-l3XKPrKXDq8J1AKnJrhc8InqzV9pJ6aznFWEb_wiesvVUkZq3aX3r69ab7Xi7PWub8E-zKCUU2ixVFHnvlFuDd6QlnAv19gt-8JiyRpoV_iSrH1nOsxUJCU9d7b7thAu7sJcfNwLntKduyBcOQOXxP7MvDp0YcNCOFrw6WUOxZ0hUkJvG3O7tzy3Gkei-klYpzNTn_0eEyY_jxCvWhAg5qLcGi_YrTkpTrkPk4XYv3ybIGXQtitzkgPi064uOjoVSrgnYu7bITqQwpzv2mbagfYQY50YCzoedFoPXdBCgpo9dGqk8i5Xt9OfjrweAsZOnELmuYacSaG9lgncqwza_kzuJRfL8M7mg4gMlg1bRdO52mZzCjbvJx82WW0dX501wd6XjAhwGd6GvC-bJ2hxxozOFcW4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فدای جان پاکی که جان‌فدای ما شد...
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/448387" target="_blank">📅 18:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0kTC_mvBt2b8gPOQ0eu1Sx5FbvGbZkOWQx01xtm3yUEkPwnDVVfgV4Ksh0I1ZGagryo9T_AtUqwBr0GToTh6WEtLDuQwF0T7rVCOUy6qfi_LtXqTVWs2Ieh7e0RtWWxxtLqd_Pfvc30bw6CoGUkHYGV9hsjkOf0ZEwoowctdxgdGgnRQuktyGfSsn2YQjOFM4xLEe-IzIpmLo746A9BRWuFtwiggijHLzsbcHqy1Yt4tq06_J9mQoEc5D6tTg07ecy6wIua-kAmJ6UywCh_WfF5DRagL9Ctbo3LaZpRQRMt43kZHq65Hf5XwsoIPs4pBd_6NiSwrbJB98P-rFjeBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
فرزند ارشد رهبر شهید انقلاب به همراه ۲ فرزند آیت‌الله‌سیستانی در انتظار پیکر امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448386" target="_blank">📅 18:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b179b4651.mp4?token=hYzC6Pd6PM2bTykyIW9Z67vJRwqg2EyPMjlg91L6XgVYdvYAeFqYs4G6Ip4nPcWHdRsXEECHdsCLNWArVmsD1IcIG84Rkn1bE1PkSTTlotQW8HJ2S4h4M85n5m43alHJQ9m_ncfamwzl77ZtKEpVDPZxf9AUgMErmEvNS65STXu8w7dtb_moTnUmqOwfr9ZDC7CMWleePqsX-7xucY3XdiGMuwHcH_cbNP49s_khn78WGNvk9Gd0Ywxv4lbwbuPfgU_yUVsOiNkg1_qWKD0Y9NaXzGanQ680HzCPa_JGmitAnx43O_27p0rrt76JZh0VB_E4QSgrMbcEJrciIJpx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b179b4651.mp4?token=hYzC6Pd6PM2bTykyIW9Z67vJRwqg2EyPMjlg91L6XgVYdvYAeFqYs4G6Ip4nPcWHdRsXEECHdsCLNWArVmsD1IcIG84Rkn1bE1PkSTTlotQW8HJ2S4h4M85n5m43alHJQ9m_ncfamwzl77ZtKEpVDPZxf9AUgMErmEvNS65STXu8w7dtb_moTnUmqOwfr9ZDC7CMWleePqsX-7xucY3XdiGMuwHcH_cbNP49s_khn78WGNvk9Gd0Ywxv4lbwbuPfgU_yUVsOiNkg1_qWKD0Y9NaXzGanQ680HzCPa_JGmitAnx43O_27p0rrt76JZh0VB_E4QSgrMbcEJrciIJpx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارتی که سال‌ها در دل بود، به وصال رسید
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448385" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6318b53b.mp4?token=huRSY54pzBgrtaOlGZ9AVhK2vOZ5wyD3Unf95FgN1JZYS0_Pa677W8R8s4b8i5CmfcFfvN_VbeIbjlizGHjme9Y8gztEfSNGUjLiwqrpf_aHET3626gkj73ClzrvfuCPhXAGo0iKEiZ7NIdehq3t0rdWw1MZGI9J7j7IZigX8YFXWQt6jc0pp4NtsTMh55ty4a2F6Yu9Vgr6sjN61xkbHUriYanqaXklYAzu7eB4-GjQJwPGQ92uHuf-kCDGbt8cQc3NpbIMbURvrQgkfvVpjLcU8f6MoENLNXw19aMrhhI4Z-5SX7dV_c_CdX_DHwH3E4cWH_0KBMxPp55gOIp-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6318b53b.mp4?token=huRSY54pzBgrtaOlGZ9AVhK2vOZ5wyD3Unf95FgN1JZYS0_Pa677W8R8s4b8i5CmfcFfvN_VbeIbjlizGHjme9Y8gztEfSNGUjLiwqrpf_aHET3626gkj73ClzrvfuCPhXAGo0iKEiZ7NIdehq3t0rdWw1MZGI9J7j7IZigX8YFXWQt6jc0pp4NtsTMh55ty4a2F6Yu9Vgr6sjN61xkbHUriYanqaXklYAzu7eB4-GjQJwPGQ92uHuf-kCDGbt8cQc3NpbIMbURvrQgkfvVpjLcU8f6MoENLNXw19aMrhhI4Z-5SX7dV_c_CdX_DHwH3E4cWH_0KBMxPp55gOIp-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال جوانان عراقی از پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/448384" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca2b8c1e5.mp4?token=loXb2sh6XmoI8PBNP0kHXgfOVduxzUDd5RE583dRcESg0Q772ky9TxKnwxl-EKfvXaJLSRYXbyJZEohhmwgqntZ0MYVenwYDB7bGjAeI4zBFTTsbx0gMDPhtQuyJfzfjkmnkqLfXDzrBNQ5FXydhB1weIdL9WEkd7UlkCE9_xWv6emocdBXxCBCX9GrHKXiXmyARx0q5IEwfgCsKZlRWNNfJgFlM4AEFrAJ-LHk-iU-glNzpGYWwvFEQYPJwxAGehFZYEV4VTBNu6ezr8evDON3-4xNq_rFqZDhgs_wH2xbJ60lIwcPMC0MRkktds7M3Z1V5GGxqpbNnnUyBYMWFwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca2b8c1e5.mp4?token=loXb2sh6XmoI8PBNP0kHXgfOVduxzUDd5RE583dRcESg0Q772ky9TxKnwxl-EKfvXaJLSRYXbyJZEohhmwgqntZ0MYVenwYDB7bGjAeI4zBFTTsbx0gMDPhtQuyJfzfjkmnkqLfXDzrBNQ5FXydhB1weIdL9WEkd7UlkCE9_xWv6emocdBXxCBCX9GrHKXiXmyARx0q5IEwfgCsKZlRWNNfJgFlM4AEFrAJ-LHk-iU-glNzpGYWwvFEQYPJwxAGehFZYEV4VTBNu6ezr8evDON3-4xNq_rFqZDhgs_wH2xbJ60lIwcPMC0MRkktds7M3Z1V5GGxqpbNnnUyBYMWFwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عشایر عراق در حال تشییع پیکر رهبر شهید امت در عمود ۶۰۰ طریق نجف به کربلا
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448382" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a09d41ff.mp4?token=VZXHTL7dCx6iiO6Ap19F0rcaU3LAjP25zKZpSph1m84GpONS6GOWkpJ9goBx11HlEvSZx4G4T7aZh6KiW6T6tXZK60Xyj6TVIERxyo58AQ7n0i3wlWgMQpZj8WSYvL7KO8eQZsQ9NkFgE4MkE8STgaz-JfgezSJOnigmBKmztGT2EiTLv6KGMP53BQoo1VAvp8wI1lKF88EgIM_3Pa9A5ouI_tVcbFJrZrQ6luBhVdm9yNetvHP8krocojOzwKjMqqzw8L8FHioEp1jAMk1QGtbhGPBMJ9ewq0TOnK4eAaBWSIHRpDlHtXwbmqIWnJS26FOOVUYZX4OUgFA85SmteQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a09d41ff.mp4?token=VZXHTL7dCx6iiO6Ap19F0rcaU3LAjP25zKZpSph1m84GpONS6GOWkpJ9goBx11HlEvSZx4G4T7aZh6KiW6T6tXZK60Xyj6TVIERxyo58AQ7n0i3wlWgMQpZj8WSYvL7KO8eQZsQ9NkFgE4MkE8STgaz-JfgezSJOnigmBKmztGT2EiTLv6KGMP53BQoo1VAvp8wI1lKF88EgIM_3Pa9A5ouI_tVcbFJrZrQ6luBhVdm9yNetvHP8krocojOzwKjMqqzw8L8FHioEp1jAMk1QGtbhGPBMJ9ewq0TOnK4eAaBWSIHRpDlHtXwbmqIWnJS26FOOVUYZX4OUgFA85SmteQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطره‌ای از اقیانوس حضور مردم تهران در مراسم تشییع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/448381" target="_blank">📅 18:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc90bc8181.mp4?token=esb06ZRENcIl_EXtBz2M79UPwMWw_AGujZUIFMX0wLuhQfNEPmIPio_-9ZpL7BQcCDiCBNMDZHOkKF7au5xJvqX6MwJR-wzGc82o9ZR61kOnps9q50WyrXRQqaroqH-9GtkorQM2tnACzgOHbUazf_DlaFnLZHfl7-g4pxquOnGJ6bLHWGyY6urpwEKr7ZwQP6OQBVUWh51C1vYkZbNp0OX3QrMko6yvBKAG3YLF4rF-GgEj0VSGCAWyDuY626SkMVw1oSScr7mf6x9nnmk8SxO4xuyizsv2RlVUpJRrMwhdJYubiesNtlRuJH0CHSwy3W0F1_nVcFOXP59qrLH9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc90bc8181.mp4?token=esb06ZRENcIl_EXtBz2M79UPwMWw_AGujZUIFMX0wLuhQfNEPmIPio_-9ZpL7BQcCDiCBNMDZHOkKF7au5xJvqX6MwJR-wzGc82o9ZR61kOnps9q50WyrXRQqaroqH-9GtkorQM2tnACzgOHbUazf_DlaFnLZHfl7-g4pxquOnGJ6bLHWGyY6urpwEKr7ZwQP6OQBVUWh51C1vYkZbNp0OX3QrMko6yvBKAG3YLF4rF-GgEj0VSGCAWyDuY626SkMVw1oSScr7mf6x9nnmk8SxO4xuyizsv2RlVUpJRrMwhdJYubiesNtlRuJH0CHSwy3W0F1_nVcFOXP59qrLH9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای شهید در مسیر پیاده‌روی اربعین
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448380" target="_blank">📅 18:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFGhniPfqmcGUFEz6V5uh0wVkMX_r3NMelbVXEVDHe9Gl6uuD3hNKjTRYZMHdHIaSr0Y-f3xF__giAMeRVp5K0V2MK9aCBHdcpjcCVqOmfmwzHi6FQcL8lPfqaHGxqhrfe29IYL4cXWUkawCysKvHQbGbZID7iOVhb7zMbkAl1WrJKemroSRCznjUVr15HYy920JTqGCHHEiyb3cLcsc2TOaWSXen9qeUa7CGFbb_f_CKunEbWEPTCcRaeKax7bMHJT3bC2I3YfQOrtQgJGnaeyQqWXrqj3mveLNiSJ9yb4Nb-tPGNcKWQPc17oaD8hm74CWnEKZQQQjn0pBNsgOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سقوط مشکوک هواپیمای پاکستانی در دریای عمان
🔹
ادارۀ فرودگاه‌های پاکستان از سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان خبر داد.
🔹
طبق این گزارش، این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448379" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnG5Y4ONa-4j6IB1mOYJJi_DKc0lzwdvwvnkpOt5BHS1uhFlxTJllIi5goDTrRBdtBaxUyuVFplsrPOS_LqHy90V1vmmwGidz3IftKj5HXOQxwfRCfdLynMBRI3Q6W5nfbZZ_sOmxu8FeiEFwYYOOtRAdrzYOvP4-F9QMxSGGl00ozd0JbOyXNikOlcfNg_xyVFcooIN2-YDQlIXHOUd-R2jKWfnUigGQ2c3dEPCAyhT60Ra595_NWaoMHdqYHBUvcXVp1u1BnkSIGSZoauRQUsh5rSDntgSfBpL7ph-h5xjEriMCrOdf-7NksomzgG9A7yZ_RKv3rbjFFlPvZOPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه شماره ۳ آستان قدس برای مراسم تشییع رهبر شهید انقلاب در حرم رضوی
🔹
آستان قدس رضوی به منظور میزبانی شایسته از زائران شرکت کننده در مراسم تشییع و خاکسپاری رهبر شهید انقلاب اسلامی و دیگر شهدای گران‌قدر از خانواده معظم ایشان، مجموعه‌ای از خدمات ویژه را…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448378" target="_blank">📅 18:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d505f40d.mp4?token=bzLhW62gQvfU1XQd0nEUU9DjNsWOyqeZ2_d8TORHQmIJwMRGUIpTMj_BiboHJZX4gh38VDRE3pxfE0i4eg9Bz2Re3seMhbZqt1L3LT966o3YjMbR5TcrN_MJ5uEFAcnIqE3k8yPpETU15QHhflW_HSun7NJR3K3rLzi7Xp_p00Qy2w5jcBicJrKC7Aifr5HJ0lJZp8esePIKJgWjdqDZLjwTB2Z75poCVI6N3Lza1Db9ZdabOLcB4jrQeWi_tHuPqD6a-4RfkzmbUvrFhbew6SDHxffsi9LrGSPgWOiWlg-E3DzBtg8uXNaB6QqT0rOZplLu2MM-JPUXk5N-xu0-nHs5bSUPNfuiDAdlKaQZD1Bb9gYucBVgP-bj-7e1Ii95bX6a8eZc7RtBLLvHjD_xeYtMUpHspHLxQKB-3ci6FKJpvJaYoDpuMz0PLQZgmyEOOJGqP5pmVBZFeNV9EO9jXL34ja1qgQT4klSRS-Hx_GHlDKa1klJ1HmfpavSx5e7foVGSSF7jX3mg0bezycqS6op4-qOdgBcJZTc_u-TYEJsk3ilQ-1O4_orYFGfP2wigHZ7nZVIL0sjMMtIdg3vvbYZnBGTO2aTz5dyR1bQ_A9UfQaWfzrSsO_8tw3q02Kc9HU8G1BNUHqggC6Zs-MyJ1t69x-uNiG12wpj2k7JXxHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d505f40d.mp4?token=bzLhW62gQvfU1XQd0nEUU9DjNsWOyqeZ2_d8TORHQmIJwMRGUIpTMj_BiboHJZX4gh38VDRE3pxfE0i4eg9Bz2Re3seMhbZqt1L3LT966o3YjMbR5TcrN_MJ5uEFAcnIqE3k8yPpETU15QHhflW_HSun7NJR3K3rLzi7Xp_p00Qy2w5jcBicJrKC7Aifr5HJ0lJZp8esePIKJgWjdqDZLjwTB2Z75poCVI6N3Lza1Db9ZdabOLcB4jrQeWi_tHuPqD6a-4RfkzmbUvrFhbew6SDHxffsi9LrGSPgWOiWlg-E3DzBtg8uXNaB6QqT0rOZplLu2MM-JPUXk5N-xu0-nHs5bSUPNfuiDAdlKaQZD1Bb9gYucBVgP-bj-7e1Ii95bX6a8eZc7RtBLLvHjD_xeYtMUpHspHLxQKB-3ci6FKJpvJaYoDpuMz0PLQZgmyEOOJGqP5pmVBZFeNV9EO9jXL34ja1qgQT4klSRS-Hx_GHlDKa1klJ1HmfpavSx5e7foVGSSF7jX3mg0bezycqS6op4-qOdgBcJZTc_u-TYEJsk3ilQ-1O4_orYFGfP2wigHZ7nZVIL0sjMMtIdg3vvbYZnBGTO2aTz5dyR1bQ_A9UfQaWfzrSsO_8tw3q02Kc9HU8G1BNUHqggC6Zs-MyJ1t69x-uNiG12wpj2k7JXxHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری مردم عراق مقابل ماشین حمل پیکر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/448377" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4855ecd8.mp4?token=DuTWZlpYfYFNnZ_Naj4vgoG-vL1aXO6BSTBUXPKhYS-Yffz8bMPDHGCV8P8ntHjcP46wx9a9hAhrbDC2gf9VjKhGQgTXl2FFFODbJAChchSwgHY6UrnnTdbOsR9bJAKph-qAtsDib1I3_AbONUy8e-o8R5VnNJi5yX_VBUDvYLoj3j3cp_bHDv9duItjSaUdSobx8GITVDcay-HVOBvXc3V9RJg3w84QA429sGEzUMz_tMh2di6q9dqwz6lWn0j0JC7lnqacGlrTv501pNENrxO664d6_d4MKUTNk4RIilF2IkKwamdetm6LhG2s4zKFsgkF7YfU7EwR1dJ47xSKow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4855ecd8.mp4?token=DuTWZlpYfYFNnZ_Naj4vgoG-vL1aXO6BSTBUXPKhYS-Yffz8bMPDHGCV8P8ntHjcP46wx9a9hAhrbDC2gf9VjKhGQgTXl2FFFODbJAChchSwgHY6UrnnTdbOsR9bJAKph-qAtsDib1I3_AbONUy8e-o8R5VnNJi5yX_VBUDvYLoj3j3cp_bHDv9duItjSaUdSobx8GITVDcay-HVOBvXc3V9RJg3w84QA429sGEzUMz_tMh2di6q9dqwz6lWn0j0JC7lnqacGlrTv501pNENrxO664d6_d4MKUTNk4RIilF2IkKwamdetm6LhG2s4zKFsgkF7YfU7EwR1dJ47xSKow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای انتقام، ‌قدرت تو را می‌خواهیم یا مولا؛ خون در برابر خون
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448376" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d6b642ee.mp4?token=gerGHxoENnv6pN1WsvI54MKrB6-T0YFK5Em7ZgE1XjDj0A1vVL1Z_CYf0lokkxlO_Z5K92CIXt0sG7Srsrx3tXbdsSwcvp6MHFwEba5qpt-FtcBg9iEEBx_1wPvFIGUvkJsOBjpZAbZ0BNRgALAnmc9V4tMFOyotuUGBvKNQb6VAuAUdHj53JKdlbdw23vVL860nCueGSgNJsFbntC08o3hLVc8Dz1EN3ULuXj4Rtzy7L0OLS5W2I3m6dzaGHC2AD7B9AEJxZGQGbYO8RAk-BWhzo9TdDkt-QSr1OsYSOxZTL9Uwz3Y54umb0FHJOgqpDkg98YaQ6tDYVR4qHGZYMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d6b642ee.mp4?token=gerGHxoENnv6pN1WsvI54MKrB6-T0YFK5Em7ZgE1XjDj0A1vVL1Z_CYf0lokkxlO_Z5K92CIXt0sG7Srsrx3tXbdsSwcvp6MHFwEba5qpt-FtcBg9iEEBx_1wPvFIGUvkJsOBjpZAbZ0BNRgALAnmc9V4tMFOyotuUGBvKNQb6VAuAUdHj53JKdlbdw23vVL860nCueGSgNJsFbntC08o3hLVc8Dz1EN3ULuXj4Rtzy7L0OLS5W2I3m6dzaGHC2AD7B9AEJxZGQGbYO8RAk-BWhzo9TdDkt-QSr1OsYSOxZTL9Uwz3Y54umb0FHJOgqpDkg98YaQ6tDYVR4qHGZYMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار عراقی‌ها: یاحسین(ع) پسرت سر خم نکرد
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/448375" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8152564799.mp4?token=Vxffk6CsTsI9AB01vPFgLOtp8m-2z8N6VXcXRJE_frLfE0-rH_WaEyG-MHOa1-153Rw1ZGyC1ul36xDePGCabjRs8OXKxXzZLiljwots3xkWl1iXgPBUOWPXeUXV236qawEZzz3mdx5nWWOnkgU8vVNfMN4exVDUAJZtCEVGG_Eu_0uTvkU6hx4SfjgT9E8nryqsz6BrWPvfzqvBJbuWjwopMGLNBzpu7YNs3Mv23w14HbxcDyQsOjUiFVE-cc-U4aRIKjrpI4BC94jxR8tgojKXd5YEXiFYc6hC3TUo6KLwaUISa7e_KHQ3zdB6CI3sxxIRzKsSp0a3lwkS5rjzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8152564799.mp4?token=Vxffk6CsTsI9AB01vPFgLOtp8m-2z8N6VXcXRJE_frLfE0-rH_WaEyG-MHOa1-153Rw1ZGyC1ul36xDePGCabjRs8OXKxXzZLiljwots3xkWl1iXgPBUOWPXeUXV236qawEZzz3mdx5nWWOnkgU8vVNfMN4exVDUAJZtCEVGG_Eu_0uTvkU6hx4SfjgT9E8nryqsz6BrWPvfzqvBJbuWjwopMGLNBzpu7YNs3Mv23w14HbxcDyQsOjUiFVE-cc-U4aRIKjrpI4BC94jxR8tgojKXd5YEXiFYc6hC3TUo6KLwaUISa7e_KHQ3zdB6CI3sxxIRzKsSp0a3lwkS5rjzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
و خداوند دعایت را اجابت کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/448374" target="_blank">📅 18:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864d75da4.mp4?token=nkY-wKSQ--aSLUPNEODx6YFy-BXFL3xW-YcCVlgJcgxlbXgqG7bCgJEZcPyknqOQr3ewV1Hykt7BqypcEniUSNsPei-gO30zdMad_3dPbdwurMSWlAuLHQCqBgTTM2S_n2oLtol-qWCCbiMh7MOW2Nv6gAeSfasFxrPOcYgo_CU_hiIjYsB7U-it16LU5uQfGCgEAjc0KOJIf3yr7qFVjWxBvHHn1k5mDLK6bvuPJp2A5sRSoe4UfUufVSYzOwIrjuqZaJfaJqZ323UvOBcwTBPvhwxNe9tif0cT_PFSTrEoDap8AhyttAdGDSqTZbpPKL4lTzh8XR4yx0VT6wop7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864d75da4.mp4?token=nkY-wKSQ--aSLUPNEODx6YFy-BXFL3xW-YcCVlgJcgxlbXgqG7bCgJEZcPyknqOQr3ewV1Hykt7BqypcEniUSNsPei-gO30zdMad_3dPbdwurMSWlAuLHQCqBgTTM2S_n2oLtol-qWCCbiMh7MOW2Nv6gAeSfasFxrPOcYgo_CU_hiIjYsB7U-it16LU5uQfGCgEAjc0KOJIf3yr7qFVjWxBvHHn1k5mDLK6bvuPJp2A5sRSoe4UfUufVSYzOwIrjuqZaJfaJqZ323UvOBcwTBPvhwxNe9tif0cT_PFSTrEoDap8AhyttAdGDSqTZbpPKL4lTzh8XR4yx0VT6wop7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بین‌الحرمین قبل رسیدن پیکر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/448373" target="_blank">📅 18:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npNkNmtZxueIx3eo3W0ARnH62B4zdjAgH3n-UIl0ewBn3ZaTnbR3jlokbzYHInaylJhPLpkSSsGYFvsn5g-F44CmdcP6ShnPtoHHITPntQRQZS7NmuuKEQ6HR7pGwpbR-LUJedDwEPvjHKEvXdH-XZZhNt6UXD6Uri7hvQWc4NGvjXRb5bMo3xKsAhJfRr_E7_TzhIq7U7YXSTHViz3UB3yP0ktLuzxYQY1ht-SV4AvA19aXTqSW8UftV9zSG56mMgbKUprxFZjUpre9bTa9FWjAhjot1Cim1e5aJ8sqTKtayBu_oif0Sq2s7_PYPp85HREqDjGhU7HtPcQjN_yJyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر رهبر شیعیان جهان در دست نظامیان عراقی‌
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/448372" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-text">🎥
حال و هوای عراقی‌ها وقتی متوجه می‌شوند آقا ۷۰ سال کربلا نرفته بود
@Fars_plus</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/448371" target="_blank">📅 17:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=iqWZ1ICNX1MqBs1Nif1CzfWaHl7da85U-RXo713yc5gW1KZvtRyd819cjVu_m34grzfroyVTlzpvDXbt1Jp3RNBPW-wGLaIXM42IAaTmfJJxRmlvcEI_d48qDDrfCVud5jnWHfpB-vrAB3HgXm-3do5y6URCWUjd0ZRqSlxlSouEa-HX6ifjJ9zReHXOm9fnTlCzSWaKURdK-qHJGmknv6MY3i9inwDXxc8_wi29-qUas4R1LI2s6NRmRJxM_UuK-_F5ihMRiuHutaZJ7uRCYGSDAiSNOPOb-y447u5_kD42d-H8TUnw_rw4YmJvBPaH8iGXokRDZqDofUCZNORL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=iqWZ1ICNX1MqBs1Nif1CzfWaHl7da85U-RXo713yc5gW1KZvtRyd819cjVu_m34grzfroyVTlzpvDXbt1Jp3RNBPW-wGLaIXM42IAaTmfJJxRmlvcEI_d48qDDrfCVud5jnWHfpB-vrAB3HgXm-3do5y6URCWUjd0ZRqSlxlSouEa-HX6ifjJ9zReHXOm9fnTlCzSWaKURdK-qHJGmknv6MY3i9inwDXxc8_wi29-qUas4R1LI2s6NRmRJxM_UuK-_F5ihMRiuHutaZJ7uRCYGSDAiSNOPOb-y447u5_kD42d-H8TUnw_rw4YmJvBPaH8iGXokRDZqDofUCZNORL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر شهید لاریجانی در دست عراقی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/448370" target="_blank">📅 17:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58433e38f.mp4?token=TdJVJMuFGswhh0z7Hzyv7Z1uG6P1zzsRkRUfAzvd3kerGsx-MpN_-bmvcCLGpDX0rGMH263lKdlSigpxgJy1VTnRDrChv-VjwA1-amTzDlUY_4bC6PczLLuXrsqJwKD_9Hxm5867CeFd1TtjhoSAAlh1aHVOA4_Y10DaOwBeAc8lyCGiObXtKa1W-gteJ26dDhJHZq7vsUuA18gzEVSd8c0EdKb1Sva2qnM1F6B7qEShfGJdoyoCZvYAhhcn3Ak8LxljLl2-74IJwcwj9rRtlNBKjwDsvjWTOBL_MdFJzssZH-oFZ_ks1vreqRYWSPeglyOtK1JNDCexBQCBJgGiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58433e38f.mp4?token=TdJVJMuFGswhh0z7Hzyv7Z1uG6P1zzsRkRUfAzvd3kerGsx-MpN_-bmvcCLGpDX0rGMH263lKdlSigpxgJy1VTnRDrChv-VjwA1-amTzDlUY_4bC6PczLLuXrsqJwKD_9Hxm5867CeFd1TtjhoSAAlh1aHVOA4_Y10DaOwBeAc8lyCGiObXtKa1W-gteJ26dDhJHZq7vsUuA18gzEVSd8c0EdKb1Sva2qnM1F6B7qEShfGJdoyoCZvYAhhcn3Ak8LxljLl2-74IJwcwj9rRtlNBKjwDsvjWTOBL_MdFJzssZH-oFZ_ks1vreqRYWSPeglyOtK1JNDCexBQCBJgGiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احترام نظامی پلیس عراق به ماشین حمل پیکر رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/448368" target="_blank">📅 17:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448367">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=XXo-_8iKqfC9nkhxxqae2mYJLN2ghlcG44X1iagm1xlvU0llarlB9LGF719hB_g826rShamErXG88wZpJ_LtCQ3eN-g_Lz6jFwIgo-3esTeASjc9mqwnl8dw2J-IIYkrJgEfHFGW-hC6P6YfuWFwoEOpG30qFJJyrdwUsZ9NAyyKMUj8nX5VvFM5EptGg1ayx7H2DRS59GNMO9GJrkkkeOoqe0AFlALH-47lb5QlBeBFJD8ycaBFGmlTBUihQqV2Va3NGRGDuBqzY2Jq5eCKimbST57h8-orb9NjiRzO0R2Ue45_oOP-sIuHR6cwgROGr6Rok-OEbANM8CENZZmEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=XXo-_8iKqfC9nkhxxqae2mYJLN2ghlcG44X1iagm1xlvU0llarlB9LGF719hB_g826rShamErXG88wZpJ_LtCQ3eN-g_Lz6jFwIgo-3esTeASjc9mqwnl8dw2J-IIYkrJgEfHFGW-hC6P6YfuWFwoEOpG30qFJJyrdwUsZ9NAyyKMUj8nX5VvFM5EptGg1ayx7H2DRS59GNMO9GJrkkkeOoqe0AFlALH-47lb5QlBeBFJD8ycaBFGmlTBUihQqV2Va3NGRGDuBqzY2Jq5eCKimbST57h8-orb9NjiRzO0R2Ue45_oOP-sIuHR6cwgROGr6Rok-OEbANM8CENZZmEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برافراشته‌شدن پرچم «یا لثارات الخامنه‌ای» در خیابان حرم امام حسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448367" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc919fb2a.mp4?token=sz56g_7Vouc59BPZatNslg3c6tEBdGYpcWsw8G8ulZz5ip4IzIdIkEqH8eQXgNnfHjlPlhkmr24O4bI8f73SXHXlAn35p1zeKPSLLqGnH0VKE3M1sdxnAMU3j_0IoJaPUy2UXNa6zb0Q-qVG6WceQkSv0UQptPACTf3Q7XWKKhZTFVr6d7LdboBOO8X6AkmO6FeURD6fcIp2jeWajRKxYlnBRPg_hlCFkVMKX4SD1R6pFNZ67WDRH75wjAfXOUGG-EnAo0VzshnSm6wnGESr8qAYtZMV5Pq2_XFXeLDBC0H4nvV0lsOMLw7yQwAvTgYs2Bb51MeODmKu5mwfQXCpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc919fb2a.mp4?token=sz56g_7Vouc59BPZatNslg3c6tEBdGYpcWsw8G8ulZz5ip4IzIdIkEqH8eQXgNnfHjlPlhkmr24O4bI8f73SXHXlAn35p1zeKPSLLqGnH0VKE3M1sdxnAMU3j_0IoJaPUy2UXNa6zb0Q-qVG6WceQkSv0UQptPACTf3Q7XWKKhZTFVr6d7LdboBOO8X6AkmO6FeURD6fcIp2jeWajRKxYlnBRPg_hlCFkVMKX4SD1R6pFNZ67WDRH75wjAfXOUGG-EnAo0VzshnSm6wnGESr8qAYtZMV5Pq2_XFXeLDBC0H4nvV0lsOMLw7yQwAvTgYs2Bb51MeODmKu5mwfQXCpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جمعیت حاضر در بین‌الحرمین در آستانه مراسم تشییع پیکر مطهر رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/448366" target="_blank">📅 17:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448365">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e9748c01.mp4?token=IAtAVznRfMzO5WOZKDlsmGqXDtUVBe2Sdk73PxIsh0EZZ7RPLH5jFEzabDe9q2By9AwSJDCHnawh_HoWGBNr0zL4phOCokERj3-wcWSejZHSE7B7dbLfxJ63bUl-9JZzzRu6aHTu5WMMg1slECcYb4Um3ZktdNreXHsVzTVdf4EiRXo036jyVeH3jmoWu_2g6_wJSUrUPGEFhgvjNdydSiyCPmkJNAntv51zkhWMU8WIfdWARVMrz1dLzfk2M-1oKhiWclfagi88wToEStlTN-gX7DEFM06Hirk5TrbNaqA5UhuxE84Z7aKNITeZWc7TISrXxEcQHmj7zwbS_EqZLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e9748c01.mp4?token=IAtAVznRfMzO5WOZKDlsmGqXDtUVBe2Sdk73PxIsh0EZZ7RPLH5jFEzabDe9q2By9AwSJDCHnawh_HoWGBNr0zL4phOCokERj3-wcWSejZHSE7B7dbLfxJ63bUl-9JZzzRu6aHTu5WMMg1slECcYb4Um3ZktdNreXHsVzTVdf4EiRXo036jyVeH3jmoWu_2g6_wJSUrUPGEFhgvjNdydSiyCPmkJNAntv51zkhWMU8WIfdWARVMrz1dLzfk2M-1oKhiWclfagi88wToEStlTN-gX7DEFM06Hirk5TrbNaqA5UhuxE84Z7aKNITeZWc7TISrXxEcQHmj7zwbS_EqZLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیون و زاری زنان عراقی برای زهرای ۱۴ ماهه شهید جنایت ترامپ قاتل؛ هنگامی که پیکر او وارد حرم سیدالشهدا(ع) می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/448365" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448364">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVJ-cuoTMwdahAfZm3snku6mP7ahj4l4CvsbAuCSS8eI0zRG3_Wt7DICVria7ItEANY66aSR_7p1FY39IaVRY4upsBhqISWgnU0bvLNOjU7z8bYdkQfrbaZ_xXin3PA1MfPv4UxFdcGZhcsd9tpb-OCdeqRa2D-T6alK-NMjYHdTZRtWnSAFDibMmvAoicTiRWCx9OQ1SgHxsUcPMmgLKO4g14xlpChredQg5qIEKrE-92Mt9ICku1ARbYJrgLDBb5OKZKFHG9PSJYZkUJFRlANOQJIGY_uvre1N9AGNYQuW6zCPb_0IFddeCLEAmDsL51odpNGSTXDUckqBjl9rcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس یادگاری با تصویر حضرت آقا در بین‌الحرمین
🔹
هر جا عکسی از حضرت آقا می‌بینند، جلو می‌آیند. با احترام، با لبخند و گاهی با چشمانی خیس می‌گویند: ممكن الصورة؟
🔹
در تمام سال‌هایی که خدمت به مردم، فرصت زیارت را از او گرفت. بارها آرزو کرده بود به زیارت برسد، اما نشد تا رسید به امشب، به سلام و وداعی با شکوه در میان مردم عراق...
🔗
حال‌وهوای عجیب مردم کربلا در وداع با رهبر انقلاب را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448364" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448363">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
گریه‌های فرمانده ارشد عراقی در مراسم تشییع پیکر رهبر شهید انقلاب
🔹
ابو حسام السهلاني، فرمانده عملیات شمال و شرق دجله در مراسم تشییع پیکر رهبر شهید انقلاب در نجف در کنار جمعیت میلیونی مردم عراق به عزاداری پرداخت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/448363" target="_blank">📅 17:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448362">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afb212fb7d.mp4?token=WEXu629SdGAvDy1_G5s5-78GkEuvlFcMN3HQA3pnrwvAMMWk5KPugKtM2op7dJbVNLB7AhOFv05ck4cGWxpCAM3JJdeR6NqMfaUtmYos2x1uasUOKQoZkcsNOPUMX_NvrY4YrC6cbUIsCmLkHemYf0uGosbDCBNNTf9HyFPJilyyn_0FlwbaJofOi2l1EnjDfHXr9WAO47PtQJRVTbqn620UTcCy-poCjWigUTPiSw_YdDlaN9tXh-9AOAJc7r6E10Q3f4dfoM9-3nZY2tqdNmqROvyevU5_Je7BL0voBrGO6xQtx-PHUH3DmULigzTgd01N3rEM1HWgnNHkZ4g8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afb212fb7d.mp4?token=WEXu629SdGAvDy1_G5s5-78GkEuvlFcMN3HQA3pnrwvAMMWk5KPugKtM2op7dJbVNLB7AhOFv05ck4cGWxpCAM3JJdeR6NqMfaUtmYos2x1uasUOKQoZkcsNOPUMX_NvrY4YrC6cbUIsCmLkHemYf0uGosbDCBNNTf9HyFPJilyyn_0FlwbaJofOi2l1EnjDfHXr9WAO47PtQJRVTbqn620UTcCy-poCjWigUTPiSw_YdDlaN9tXh-9AOAJc7r6E10Q3f4dfoM9-3nZY2tqdNmqROvyevU5_Je7BL0voBrGO6xQtx-PHUH3DmULigzTgd01N3rEM1HWgnNHkZ4g8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب ۲۸ تا قایق [ایران] را منهدم کردیم؛ احتمالا امشب هم همین کار را بکنیم.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448362" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448361">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf84b71fd9.mp4?token=ankYa13ODMqaAM1PWKCyo8dekhQPorSRYK3F5f5PialsE2dZ33eOFL3cWH0pOPXenvwbWqAYshPz02CanmDE8loihuVMNoNnHjqXFV3ghY7mhngzb2OUuxeBLjv232prO4dgDVvjLU4Av0v0sfqt1VqAoGXmfADopgiC82WHaT3kxGaTLHhubihB6LD4GltotOLCC5agkDS-y1CuS9f5Qy1Rpm5rJFDoqtzyrYFKMmGNj5C1x0tRC6OMX4QS15logDvHqf5EDkm1-XEEbk4nOKVZbigGDtnBTbJRQJJDl18NMgU1r6O9gQKHHFn6XsvR46ShVN6u83Zax_u7gkt15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf84b71fd9.mp4?token=ankYa13ODMqaAM1PWKCyo8dekhQPorSRYK3F5f5PialsE2dZ33eOFL3cWH0pOPXenvwbWqAYshPz02CanmDE8loihuVMNoNnHjqXFV3ghY7mhngzb2OUuxeBLjv232prO4dgDVvjLU4Av0v0sfqt1VqAoGXmfADopgiC82WHaT3kxGaTLHhubihB6LD4GltotOLCC5agkDS-y1CuS9f5Qy1Rpm5rJFDoqtzyrYFKMmGNj5C1x0tRC6OMX4QS15logDvHqf5EDkm1-XEEbk4nOKVZbigGDtnBTbJRQJJDl18NMgU1r6O9gQKHHFn6XsvR46ShVN6u83Zax_u7gkt15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ دستی دلِ رها کردن پیکر آقای شهید را نداشت
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448361" target="_blank">📅 17:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448360">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f0abf71a9.mp4?token=agUG7fBRKkR6mUdJzkfCcTuvF3PYCMBAQVrgXNShL9twFLYDDkCbs1iuQHHeT0xwdic8qxRuYFGXnAbMVXatLswqOgo03M__y0g3DMost35DBdCmbvrciE6PEQMJWR_HBHAY1apL8UKFMoeeo22FACj4Mjc0QAk2VIag1PatqUXiNkjmpLNTbNw299CF6SjVhobLk4J-gGZq-zQgOQLoMVMlOYF8fYe2kDHitSFGVptyaSPHhGrmSxajjR9TAXNeE94vfnaWbuxIGDH6HWkdpKh55FvfmVKvrIWvYkf5FP6swZWQUKGIsd5Cmsr46RDdKfDeDuZQRiM7UGiYQYmfEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f0abf71a9.mp4?token=agUG7fBRKkR6mUdJzkfCcTuvF3PYCMBAQVrgXNShL9twFLYDDkCbs1iuQHHeT0xwdic8qxRuYFGXnAbMVXatLswqOgo03M__y0g3DMost35DBdCmbvrciE6PEQMJWR_HBHAY1apL8UKFMoeeo22FACj4Mjc0QAk2VIag1PatqUXiNkjmpLNTbNw299CF6SjVhobLk4J-gGZq-zQgOQLoMVMlOYF8fYe2kDHitSFGVptyaSPHhGrmSxajjR9TAXNeE94vfnaWbuxIGDH6HWkdpKh55FvfmVKvrIWvYkf5FP6swZWQUKGIsd5Cmsr46RDdKfDeDuZQRiM7UGiYQYmfEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلام به بقیه‌الله(عج)
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448360" target="_blank">📅 17:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448358">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a78dd2ba.mp4?token=FJWn_i8fPqzFgwCQ7sCwJfe80Ny3_maaiC3g87FGeFqSyd50pGqKARufZB6UWy1N7KEJ5A9Z5-_IEVvqzP_TbKVEgvlIO1zi89OKBI8f13ggZcq5lSsJPA8pbF6SpaaAxGSZwzn58tl3t5ACGEYLCYTuS85mLnuTrMYTTiWnhaJDQ9arNhpo9juOFRRXApQ7ZwAdW_lNddNfumr0mtOtEaPoeTgQ2kuwbV30VFUOfxKC7Xzl1uP-I0kugClTLubxZg9lL6b0g6KAKH9wfKUgE9z3Kp4Vr8Am_qD7PaXYVao8WLCy3vym-pRGnVCA8390whOlSr_82BSqqQladv1a9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a78dd2ba.mp4?token=FJWn_i8fPqzFgwCQ7sCwJfe80Ny3_maaiC3g87FGeFqSyd50pGqKARufZB6UWy1N7KEJ5A9Z5-_IEVvqzP_TbKVEgvlIO1zi89OKBI8f13ggZcq5lSsJPA8pbF6SpaaAxGSZwzn58tl3t5ACGEYLCYTuS85mLnuTrMYTTiWnhaJDQ9arNhpo9juOFRRXApQ7ZwAdW_lNddNfumr0mtOtEaPoeTgQ2kuwbV30VFUOfxKC7Xzl1uP-I0kugClTLubxZg9lL6b0g6KAKH9wfKUgE9z3Kp4Vr8Am_qD7PaXYVao8WLCy3vym-pRGnVCA8390whOlSr_82BSqqQladv1a9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: شاید جزیرهٔ خارگ را تصاحب کنیم؛ [ایرانی‌ها] هیچ کاری نمی‌توانند در برابرش انجام دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448358" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448357">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Fsfu4X28ur8U3p9f08S-c9T9fiWUnAo_dAuYTKvoudsleooAJVeQjwCmhiLfuE0-oBXarcWmf-Mkp744Iv01ePBlREe4mAMRHq4tzQ91L2aBANcfwoh3hLrMwgg0hPs0kqQ_sPlBq-fchtePEYdxfXG0v9ji2kcTqi1icK8puf7fv4U_ntevwgnCgWQ6fPpIqPGfLF9l78MRDeqDmUggr05g5MZcD7yiDzYF_Zam_HXPWXJvmLXzbj9tK38Sa2mTyZN8L9kjeOlzilY6Hntuq2mTMrRLdLst0DKEHiwGHhNykZzStqgpuUU8iP3kCYdJRt62fOTK6Si3Y_X_HwNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده‌ای که از لندن برای تشییع آقا آمدند
🔹
آقای جوانی به‌زحمت می‌خواهد از میان جمعیت رد شود. بدون مقدمه می‌پرسم: از کجا آمدید؟ جوابش در ثانیه میخکوبم می‌کند: از لندن. برای اینکه مطمئن شوم درست شنیده‌ام، تکرار می‌کنم: از لندن؟!!!
🔹
اکثر خارجی‌ها شاید شناخت زیادی نسبت به ایشان نداشته باشند ولی به‌خاطر جنایات اسرائیل که در سال‌های اخیر مرتکب شده، هر کسی که مقابل اسرائیل بایستد برایشان مقدس است.
🔗
حرف‌های شنیدنی مهمانان لندنی رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448357" target="_blank">📅 17:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448351">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nXkfcd9Fbj4HtCk_CNaMom4gRkd8MkkckOHAaJhcITDErs5qddL7sooyfsm9qu3mXTH_prlT_itZs6RLsC9m0xCLAZugOvkSwKr1rSKUyo7JOwxfNUGKqIAygpU1_1XvmhmL80bxz5w90Tf67LGOAr4nqtix5Ma052qxp_5hL0Vm7SL8Rua8iQpxCV2jZGiKjLS4jH5pTbPJq1VFdE9-CCJS84G_0y1LuP5CWOh6Il7qVLaprr0A8O8ONfGUadn_TLe4hpfGRA0zODjmbs2FY-fIFBjjso5_yGZ7cplcsMxYbm-fbKH91W5UJudAIItZRBDiJM9AvtWtyJVNOMJr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3CLGE3rQJVIOhYGkEmNe309iroMTjfMBN7IrbaNcg1xg5PF3boFwI5wuJF_OOMWDz9sp_c84DFalISTDVmtysmGn3tvePYR51OSTEhn0LzIWaQMh9b9VQbCXYDnD9wW69IppJQvUw9NuJLtZFkeFeJWFllFUeuvD2bK9tUp4d1p_ePkceDMNkrYhSkfvy-rUcEjwfarAe5nEskGRlJylJ6VyWBQvHBqJQTYAZ1s9ogay-lT_yOWQdPUAG3r4WUAgIVzh14oSwrt-Bi5p2_9r2fzDYcKLYYh2Icz5CUPTXPLYIEgAIsQfMayKuzlyxxYFKTmxaQBqaxlJx2EjHZ1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvSsrAORZSFErXNPtzYUc77g-rh0FFGN0nkAc8oWO-uijfI5fktz0dFiVj-g_lhnzvPJd8BPRR2YLzfoZuZOiVkCiwGqjwY6Kuepm3sAkFu9qWukdFNRHUq1sX43GuhjPz_3uJM6dMkgm_RCiKgDnqjUYR4qvyBETksVJPop5Bb_QURrWNRem09zhn-zoNEDZbMkbhtqtN5aqNzG8WY4f8F6SJFqy2yvLLFpvikhgAlmo3pckXx6LX3UESnzkrf-Pv76BEUAyBqh2ZnUsARvkbaOb0rHTYmpdd_OArT1rPY8KE8KwzT4smX5mOLm0qEYsV6eenjGJCRHkbU7A-P8cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZ7WK4SpqtvBGgwEnXlpuD7xghT6kjFGxEJuJFWzLDnkAk5vWPNK5G2TGXX2xbyAe7_Dcpf0RBNiA9qtEkiObNO-lnKoZih8UN9sFwarJGq60TrUBcWHy31ccxD6RWEMiEgNwBB8IWHKhDD4ReWQVnhuXr-_1AL30nun5O1UXG1Sc_GjUJA9y21CEw4XyrYZYqqO-SSXphwkUG3yJi4emyqgMWhxyUrSDs9Bs1JzkI8oyjBhb4aZwz6leYnTEpCHOM2DPHRYzSKHiWE6OosE5Im0YzZmRlrotKfeBIJT4Fl6AMp9PhwxdrUkmBHoLhpFgbpCsU4KHRFJsMyeLC4V0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JozfG4-pnjovl1nuiNVbQQSHz8LyXxFm7BXQATrM5Lk0SBpV_9bbGJkOZzBoH_BBlhCUwWdKzpaiXi4c5nRXzbgX-_FNmz8zFvu2oC0d_r32U-Jp7PJcQYryJkuLBIp9TCK6t4qv2fXSO22MzHdQCKjWiOfKXSJEILVOh3ecOU654KIjHgomsZzoqn_wgIXHxsHOL5QLpqmRH7H_d4HbkU9EXupSoKG8uqjQoiSSMim1NrqPuVotYO_3BWn8oQShNdibOLkb2tEbVg5jqPL51Yerlp3TMW-hAtvyGu5AdBaf8z-PReCBjIdlIotUyxdBIJBwl8KLgE1orX85N857IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7lsQzaUSe0gYwqSRxrYtORSFkFgJ5WR0iiVP1XTd2819vzuy2F2LkU_ac2o9C5G2xbA_2L_2H9-qAznBUbx1Tt45tVR-Ohzt_XBS58g--1rJo9svDkD0nwjus2kp3CJiuhThidylIHYeTzpmWym9zkzu4YpEWS050zgxvWL6rPCaeUYMwus-aUGUDBaa9iO0eX17NnrYItGwzAMN4h9go5ngrgHfC--S49mKxCKTBnL-swIUG2bjCoSUNMi1GfgHFWCrsWp_DLGZEDZ4Qhf_CBQwEE9XcWt7GmDag24V4P-wO6BVpelFuQ-HO4wN73tvqo3ysYSYQD3knTt3X9DdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین قاب از زیارت رهبر شهید در حرم امیرالمؤمنین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448351" target="_blank">📅 17:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c9309d46.mov?token=PKQL3HiDCEwCE2QYOfOALs8NmX1aO0mVpKqc9zhO4geA8gx2eNglHcyOAkXYtnTO30XAc5QQCXZHPBgo2iAMRi6qzvgJateBGJyGQ_IbQvADF74IX6kHASzvLKEGLQPrFUcKTuPL5WnlDSW_W_2weXmLoWYVohRRAQfjFZl279Njx0FxTZFpWT7ETYNXmsQd2DbWS4AbwCwkaT0n4gNvIkaD_ydG3vB_cxSYN9hWl-DVg3JCfXhjBybbByLZGasBNzpML3qu-mcF9bUkLdwqqR9nne3_wDGdmMFS8mna-9v7tb_OlhI1lNKfylWYqAmTgzULZt97xZosjBKyKk2DoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c9309d46.mov?token=PKQL3HiDCEwCE2QYOfOALs8NmX1aO0mVpKqc9zhO4geA8gx2eNglHcyOAkXYtnTO30XAc5QQCXZHPBgo2iAMRi6qzvgJateBGJyGQ_IbQvADF74IX6kHASzvLKEGLQPrFUcKTuPL5WnlDSW_W_2weXmLoWYVohRRAQfjFZl279Njx0FxTZFpWT7ETYNXmsQd2DbWS4AbwCwkaT0n4gNvIkaD_ydG3vB_cxSYN9hWl-DVg3JCfXhjBybbByLZGasBNzpML3qu-mcF9bUkLdwqqR9nne3_wDGdmMFS8mna-9v7tb_OlhI1lNKfylWYqAmTgzULZt97xZosjBKyKk2DoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر رهبر شهید انقلاب از طریق الحسین و مواکب مشایه وارد کربلای معلی شد
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/448350" target="_blank">📅 17:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448349">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=cB7lrK3Vd59HQzz1tWyh7Nre65St7V8b10BlijKMs5f8_FHl7Ky34_ZDWEBPPpfQ1UxKLxFFsYyO2pZ8qCNf2RWh-UESiUjn2U1wr_sz0ECAymKJosNZy860XBrV9KzD4Df8rhAwLnbD9B83te7VOWb8SoVYDr6xGIAg4Q6GvYE824euhdAivH_A_c1Vt1Pk19YQ3IB9ecx2CAWvfw8w3YrEsZdc62C2zgkYxGmnFGpiA6FqmRTyVZZWMXz4w6jNIg6MTQ7WBMrEQVnTt3Pq9d2tjc5_-gXKG3F4pShkD1GPknx-xtoCUyUMpajejHlB_GxkfJmB_uKBPnGbmG0Sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=cB7lrK3Vd59HQzz1tWyh7Nre65St7V8b10BlijKMs5f8_FHl7Ky34_ZDWEBPPpfQ1UxKLxFFsYyO2pZ8qCNf2RWh-UESiUjn2U1wr_sz0ECAymKJosNZy860XBrV9KzD4Df8rhAwLnbD9B83te7VOWb8SoVYDr6xGIAg4Q6GvYE824euhdAivH_A_c1Vt1Pk19YQ3IB9ecx2CAWvfw8w3YrEsZdc62C2zgkYxGmnFGpiA6FqmRTyVZZWMXz4w6jNIg6MTQ7WBMrEQVnTt3Pq9d2tjc5_-gXKG3F4pShkD1GPknx-xtoCUyUMpajejHlB_GxkfJmB_uKBPnGbmG0Sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ ایران را جمهوری اسلامی ژاپن خواند!
🔹
رئیس‌جمهور آمریکا: جمهوری اسلامی ژاپن ۱۱۱ تا موشک شلیک کرد. این موشک‌ها به سمت ناو هواپیمابر ما شلیک شده بودند. @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/448349" target="_blank">📅 17:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448348">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73992baf6.mp4?token=nDbYJHF_cGuc1kCMbOXDFKSu0DVo6m7H-SF7gjrCcEo04CP4xxWJZByrtjtiWm4r0Z1MpOS_1rdmIRbVNbSJS0Ogc7ROLRYw8CWlZHQT2VUx8t97hwDaU3yHvVa-vSwTPZjOV9NW1n19JYY3cOiSNAFAPzg2XYOvjAncKImxf4Xeq2gwe-sDsz_apQzcNUtonI29Y69dHSOImilurWraQZExCf-Ew0AS7rdEa5aSPSZLhbtEDdKwIFa8gWj9JQ9Yyq3P6QBEw4JVlazLkNvP4I4DDlEsGD_8AUMVjYnZR1YCebfyQY9gVA-QOwuezF4DYo-Ot6Kn-0Xq7kYuYoy7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73992baf6.mp4?token=nDbYJHF_cGuc1kCMbOXDFKSu0DVo6m7H-SF7gjrCcEo04CP4xxWJZByrtjtiWm4r0Z1MpOS_1rdmIRbVNbSJS0Ogc7ROLRYw8CWlZHQT2VUx8t97hwDaU3yHvVa-vSwTPZjOV9NW1n19JYY3cOiSNAFAPzg2XYOvjAncKImxf4Xeq2gwe-sDsz_apQzcNUtonI29Y69dHSOImilurWraQZExCf-Ew0AS7rdEa5aSPSZLhbtEDdKwIFa8gWj9JQ9Yyq3P6QBEw4JVlazLkNvP4I4DDlEsGD_8AUMVjYnZR1YCebfyQY9gVA-QOwuezF4DYo-Ot6Kn-0Xq7kYuYoy7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف‌های دههٔ نودی‌ها با آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/448348" target="_blank">📅 16:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448347">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoBDkzwglaWk9zZUxD2yvrWopOK5F62lP3xxQVkpn_sLVJxO5bEB-sIxeTYidc8tCmHS5qzLPS3-0v4ndJzwIWBXjxn3Ei6Zn2svBByd4suuZPBaIO-sBIQXGIFEwezVfmea3_U7E3T1xP0DjRpfZ4zE6If9oZNh7_YcmjTRBDAqXjvoKyUG2JEr8HeZtpYbn2URSd0GaJPGO2Mo_l1cz5sZqUUZRaqv4hq74KQusGgHQm87TYPVtIapUVs7lrt2dzidj2mUPygmqFp-gphwNTwe3zun7ZbPWbJQWIk2_RMRyukEFrSu6ucG5gM5EHNLNNmsQvaUIGxwaT1gq3BBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: به ماجراجویی‌ها پاسخ فوری داده می‌شود
🔹
مشاور رهبر انقلاب: پیش‌تر هشدار داده بودیم «منطقه، محل قمار سیاسی کشورهای خرد نیست» و بارها ثابت کردیم که ماجراجویی‌ها پاسخ فوری داده می‌شود.
🔹
اما مسئولیت تنش آفرینی‌های تازه واعتراف زبانی به لغو تفاهمنامه توسط سیاست باز راهزن و بدنام اپستینی که بارها مورد نقض عملی قرار گرفته بود، بار دیگر منطقه رابه سمت آتش سوق می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448347" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448346">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea2c45dca.mp4?token=Ut1BdPLjHIwng9r0Rxx0lcOs8SeSNa5wHGwSH7DVVITviPTuJc1GFMqktqm49xsTy86VNapm9CvIDLY9kgtUNWnAlNirgOFH2YbcJB6TrIxOsiKyedOZbTjT7n_qJeL4CGmuQcNmXIh-ohnYxsRhkpVW4Y-j3buRffHE0PoLZZ61piPzoTF1P27-4U8uxowxrAlKCzY5xyMAwbifuHob6WN4H35fPrVg8v8aBiNGHKgUUYU_MCLWUtWX-Hr2d9NOXf6xUg7J5AINKKro-DrU6gA7vD7cMSGZsqqo13BdUFv4C_Fz3CRB0HIASjHvIVvf9V0q8v_t2fQILexW412evQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea2c45dca.mp4?token=Ut1BdPLjHIwng9r0Rxx0lcOs8SeSNa5wHGwSH7DVVITviPTuJc1GFMqktqm49xsTy86VNapm9CvIDLY9kgtUNWnAlNirgOFH2YbcJB6TrIxOsiKyedOZbTjT7n_qJeL4CGmuQcNmXIh-ohnYxsRhkpVW4Y-j3buRffHE0PoLZZ61piPzoTF1P27-4U8uxowxrAlKCzY5xyMAwbifuHob6WN4H35fPrVg8v8aBiNGHKgUUYU_MCLWUtWX-Hr2d9NOXf6xUg7J5AINKKro-DrU6gA7vD7cMSGZsqqo13BdUFv4C_Fz3CRB0HIASjHvIVvf9V0q8v_t2fQILexW412evQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرد عراقی با پرچم قرمز: برای رهبر شهید خون‌خواهی می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448346" target="_blank">📅 16:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448345">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=RgHNLsi-FM91BE8U5p6qYRiTJ5Nk2NHc_UpmHAcXra6ukKB0jH_6Hxyn3zh49Ob_hPP7k1B1S_CDMBu1MWuCtxu8uTgVZh3d66bkx_-YQdINQia0xtqDAcXxURG2cWjvwFawMHR8S8oFm-b5K9S1YdfEqW2DYIIXEFVXliwvqT9GrakbuXn3ucqSFGVgYY5g5n0lKK0GN6XXx3dZxxBbKAYGHF07aWCHdRc-0OgrqAKrsov1jlbfeAHlFydQGfA-9LHdEgxEGJqkmbr6tEqH45-hCiRllc34bwE18RTY0aElhcFtFb8gkf-sig72VmKp8GWnogjiz3hutH2O7Scu2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=RgHNLsi-FM91BE8U5p6qYRiTJ5Nk2NHc_UpmHAcXra6ukKB0jH_6Hxyn3zh49Ob_hPP7k1B1S_CDMBu1MWuCtxu8uTgVZh3d66bkx_-YQdINQia0xtqDAcXxURG2cWjvwFawMHR8S8oFm-b5K9S1YdfEqW2DYIIXEFVXliwvqT9GrakbuXn3ucqSFGVgYY5g5n0lKK0GN6XXx3dZxxBbKAYGHF07aWCHdRc-0OgrqAKrsov1jlbfeAHlFydQGfA-9LHdEgxEGJqkmbr6tEqH45-hCiRllc34bwE18RTY0aElhcFtFb8gkf-sig72VmKp8GWnogjiz3hutH2O7Scu2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب ضربهٔ بسیار سختی به ایران زدیم و احتمالاً امشب نیز دوباره ضربهٔ محکمی به آن‌ها خواهیم زد.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448345" target="_blank">📅 16:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448344">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bdb6b181a.mp4?token=ggsmkyF3nBEe49yR_SdgsF301tKixNJK7U5d6yl5EjMKgNs1cVyT08FlQoH-wMloQwAGwQoQLjKNyW9Ir_Bh4yNe6FkO2mMumI6h06HJnf3OfW4_aXu8RHwZPcSDkSTv9mYHDxK8i-betY7rTC9mE5wZI-5NUxNSkEbdX5HbRmroTk9oborNYIBVGV6sYieEdLHJVUDgWzPZTWr8qV1OGLLLd-LEGdTuD1AFMgL3DdrU3hT2yj-f-oc85YIBaYegenqv3FMUwxNY9-khmYAC3m0_LEPqVzdnEdUfMVxGV8w1Dhsywutg7AA4DJIzkCqxKHjtIvOz1mfHXJ22qIjwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bdb6b181a.mp4?token=ggsmkyF3nBEe49yR_SdgsF301tKixNJK7U5d6yl5EjMKgNs1cVyT08FlQoH-wMloQwAGwQoQLjKNyW9Ir_Bh4yNe6FkO2mMumI6h06HJnf3OfW4_aXu8RHwZPcSDkSTv9mYHDxK8i-betY7rTC9mE5wZI-5NUxNSkEbdX5HbRmroTk9oborNYIBVGV6sYieEdLHJVUDgWzPZTWr8qV1OGLLLd-LEGdTuD1AFMgL3DdrU3hT2yj-f-oc85YIBaYegenqv3FMUwxNY9-khmYAC3m0_LEPqVzdnEdUfMVxGV8w1Dhsywutg7AA4DJIzkCqxKHjtIvOz1mfHXJ22qIjwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عراق (واع): پیکر مطهر رهبر شهید به کربلای معلی رسید @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448344" target="_blank">📅 16:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448343">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0f4bec21.mp4?token=k7wWXeBwoCg3PpP2xgoq0S5M3TkSITmJOMEm2Vscb2OMO-vLrmuR9l5vZ1hXw_rgSBnSlnt4LRZJRCdzGaCK083mNNFinJOPcJSN7peJK3dNV1lD1kvmBkqvv2fY9zV0mV4xHVf0iFX7pe1Dp0xWIuxlrEegkNkoyMkJzmMSUus9csFD0RUR3cu9p-ytFnOkajx-pUgdbghl_rkrWKW6tz3Dz4OyXc03WxOgz-_9NeW4wLVUF7p9hqu24mnhYYJceSXvWbP7vMyBZnpAHd60BVQXl5BzgWgU6qLAUaO7qEi5NT2EHfJ53r05E06ia9AJvgeqZTcZ_-bbPDGnY96slw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0f4bec21.mp4?token=k7wWXeBwoCg3PpP2xgoq0S5M3TkSITmJOMEm2Vscb2OMO-vLrmuR9l5vZ1hXw_rgSBnSlnt4LRZJRCdzGaCK083mNNFinJOPcJSN7peJK3dNV1lD1kvmBkqvv2fY9zV0mV4xHVf0iFX7pe1Dp0xWIuxlrEegkNkoyMkJzmMSUus9csFD0RUR3cu9p-ytFnOkajx-pUgdbghl_rkrWKW6tz3Dz4OyXc03WxOgz-_9NeW4wLVUF7p9hqu24mnhYYJceSXvWbP7vMyBZnpAHd60BVQXl5BzgWgU6qLAUaO7qEi5NT2EHfJ53r05E06ia9AJvgeqZTcZ_-bbPDGnY96slw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
خبرگزاری رسمی عراق (واع): پیکر مطهر رهبر شهید به کربلای معلی رسید @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/448343" target="_blank">📅 16:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448342">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎥
بین‌الحرمین، مملو از عاشقان چشم‌به‌راه امام شهید  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448342" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448341">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f378af4596.mp4?token=Q_M2PVEymK7SmefDpynRA3asR9W003cugd3cMvIPl48EvIjXkdcsjEaKiEx9wbQQwgHlHK-qYYkjHIsJuCBgcL65V3pSf5UWe7VxYx_pomou4V6q6-TMmj82A14lBYOfaA9BE1_0N7IT0rTk8rjsyJ8NBnR6nOixIRRVddJ1I_maMrvWBCOvK1sBQ5lHwReRwoIn5VliOUMFkSLBdtDlsDEhOB7WXIopoqPngIPCeuJmS8wUQoslgREGT1_eKR-1AV5MvkJtuD-58uU8TPJW45j6WdAd8RkYHFtakDhW-gfgj3Kkg_nkcmp_oa5vgLnZ_82xIaNph6wT_JCcLE2XPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f378af4596.mp4?token=Q_M2PVEymK7SmefDpynRA3asR9W003cugd3cMvIPl48EvIjXkdcsjEaKiEx9wbQQwgHlHK-qYYkjHIsJuCBgcL65V3pSf5UWe7VxYx_pomou4V6q6-TMmj82A14lBYOfaA9BE1_0N7IT0rTk8rjsyJ8NBnR6nOixIRRVddJ1I_maMrvWBCOvK1sBQ5lHwReRwoIn5VliOUMFkSLBdtDlsDEhOB7WXIopoqPngIPCeuJmS8wUQoslgREGT1_eKR-1AV5MvkJtuD-58uU8TPJW45j6WdAd8RkYHFtakDhW-gfgj3Kkg_nkcmp_oa5vgLnZ_82xIaNph6wT_JCcLE2XPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورودی باب‌القبلهٔ حرم امام حسین(ع) مهیای ورود پیکر شهدا می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448341" target="_blank">📅 16:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448340">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy6Ve-iYgCza9l_BRYKON5qtgESjtLg8OKA2GJRr7Ncod4Awh9sGJOwGdn1B-Ja48MBIEUklj3uvDGToWqqaaOereHxn31rv3Yd6o473_2oEojnlBxuPcvGTg_hs5eVujR-WoSSp_geZpnDrX7zrXNO0ek0DaiLtHIomHyDr8eQufKf2R-G8OfIKNbnpr5qGugGYkPzJXOERyyXcReVFDRYRa_1SHYqhgjnfFX3Yu0bk2E43y6d9Y8r6e-Hgq1Q0Xgyay8X0-vX9t_VYkpjIKFwgPtLDfgqlSoVRqyydhgCufWjQJzofthuQfYS0-bCYfsKzUj1Omg1FDl9HfGoZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینۀ حمل بار دریایی در تنگۀ هرمز چند برابر شد
🔹
سازمان بین‌المللی دریانوردی اعلام کرد با تحولات اخیر در تنگۀ هرمز، حق‌بیمۀ کشتی‌ها که چندی پیش اندکی کاهش یافته بود، بار دیگر به‌شدت افزایش یافته و هزینه حمل بار دریایی جهش کرده است.
🔹
حق ‌بیمۀ کشتی‌ها که در شرایط عادی حدود ۰.۱ درصد بود، پس از تحولات اخیر به ۳ تا ۸ درصد رسیده است؛ به این معنا که هزینه حمل بار دریایی اکنون ۳۰ تا ۸۰ برابر افزایش یافته و بیمۀ عبور هر نفتکش بزرگ بین ۳ تا ۸ میلیون دلار برآورد می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448340" target="_blank">📅 16:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448339">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff04b626eb.mp4?token=F3l6-xpP3kZiDeBCZ9BzffNycIxtFzjQPiZQTQUzUZoTlbcNU_grXQrv-GBhTjNOxYzIrXFOgWCei63iR3UeEPn-MuIWeMofg84bvgKM0eJ2uSalWjdM1izE1EJO3TjoMuOpnzfWOzS210kSlEwUs4Pi1XG5e4b8aPwo9vZeS1iigU8rZrldu9hgntXWVpekTaHOY95SjVnyPXrO-9ehroaXTpNfsBw4cHcPcY1o4Cskkgu5saS18m8BCuLWl6QKemLc5fp8skMgx1dwzH0Sz1P-zSVNQHW4DF4fMuNlEKcx8CrTRKoC1Bv1z7ubPk_nxuOHrcktY3EdU1ztcAGLOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff04b626eb.mp4?token=F3l6-xpP3kZiDeBCZ9BzffNycIxtFzjQPiZQTQUzUZoTlbcNU_grXQrv-GBhTjNOxYzIrXFOgWCei63iR3UeEPn-MuIWeMofg84bvgKM0eJ2uSalWjdM1izE1EJO3TjoMuOpnzfWOzS210kSlEwUs4Pi1XG5e4b8aPwo9vZeS1iigU8rZrldu9hgntXWVpekTaHOY95SjVnyPXrO-9ehroaXTpNfsBw4cHcPcY1o4Cskkgu5saS18m8BCuLWl6QKemLc5fp8skMgx1dwzH0Sz1P-zSVNQHW4DF4fMuNlEKcx8CrTRKoC1Bv1z7ubPk_nxuOHrcktY3EdU1ztcAGLOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دیشب ضربهٔ بسیار سختی به ایران زدیم و احتمالاً امشب نیز دوباره ضربهٔ محکمی به آن‌ها خواهیم زد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/448339" target="_blank">📅 16:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448338">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45df1cc3a0.mp4?token=fD8asLJdmH0CQk4Oh0bqL-XatmeInSs8gE8nhIwwkyzMi30kyTakeknyWy-0YtTwSfxcil91cknY792cmkYrX6rk3PGdJRVrSmRSQfM3sSk8lk6eP7pIvJRgd8SU93gORsSegcsM5FRoFuDXt75QDud_wGXz9W2DwJlxC9cHnkgzQY2MBVVO3Vm1lIkoskTimNocb_PxEqtju8rOPwW3brHdl56WkOcPUrmTvZxBDYVgLub3QFO-KhwejCOKpfA78AW6tgYlEemj3dL0Cn3rydRgurnRzGLHTtD_zgRp-MXghjHVswkxmdsYT0dB71Z_2zAEl4W9FeajVMcKg5NjBnUum3h33Zj8zVrVcYJIc9CDW1ffZ-TzDbUyXUkp6z55CHJpVuYCIcha3BZJThFIEHhJOA7VknY5_JnQsSqPS9lki3pXczr0qbPzss8mQg5MBVRYlI5RHtm4hrGjH7dbAry-bfARUupkx0VL1MLoqc8PaMx_j45PbbiMjb5kx39V-O1YxhlBI56awtHr4L8SximchIKJOxHh0OLA5rrDWZPkRdn1_gPMSPav2grhawWmjSG32aM2FHyVFByRM71x9Ezu-tfNKfXjollXufoh2y7YZILb5oIpiCN7NN_Zj7wbe_ulSFqVE7N5NHC0niCOhVn9mDkhwfulBTeMFddh8jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45df1cc3a0.mp4?token=fD8asLJdmH0CQk4Oh0bqL-XatmeInSs8gE8nhIwwkyzMi30kyTakeknyWy-0YtTwSfxcil91cknY792cmkYrX6rk3PGdJRVrSmRSQfM3sSk8lk6eP7pIvJRgd8SU93gORsSegcsM5FRoFuDXt75QDud_wGXz9W2DwJlxC9cHnkgzQY2MBVVO3Vm1lIkoskTimNocb_PxEqtju8rOPwW3brHdl56WkOcPUrmTvZxBDYVgLub3QFO-KhwejCOKpfA78AW6tgYlEemj3dL0Cn3rydRgurnRzGLHTtD_zgRp-MXghjHVswkxmdsYT0dB71Z_2zAEl4W9FeajVMcKg5NjBnUum3h33Zj8zVrVcYJIc9CDW1ffZ-TzDbUyXUkp6z55CHJpVuYCIcha3BZJThFIEHhJOA7VknY5_JnQsSqPS9lki3pXczr0qbPzss8mQg5MBVRYlI5RHtm4hrGjH7dbAry-bfARUupkx0VL1MLoqc8PaMx_j45PbbiMjb5kx39V-O1YxhlBI56awtHr4L8SximchIKJOxHh0OLA5rrDWZPkRdn1_gPMSPav2grhawWmjSG32aM2FHyVFByRM71x9Ezu-tfNKfXjollXufoh2y7YZILb5oIpiCN7NN_Zj7wbe_ulSFqVE7N5NHC0niCOhVn9mDkhwfulBTeMFddh8jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیش‌از ۳ هزار خبرنگار راوی مراسم تشییع رهبر شهید در کربلا
هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/448338" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448337">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=WYwMjX6Lwts4yWoUrrVMG2E_lzf-ou7VrEgbjGfGaKpXqmtbchwg7SxGpy4KM2qpLM7sXdnxPVgN5B4-HQoxMkNur4IM-a8SGc58yPB2auExhe5K3ymL5h3eLAfMXTbzir61CnhlACnWgLZW7kVVaoD_21yLMa-8_66N8mMA3DTxK-xP9ZD752diLZDko4Q0gPgNof2mQ8jXY86rszIGKBTR2JEr3Bsg4V5KyeNlL1gSdHr6GdFXEq16WZ40BoCxdl-rt0IrJrZBzmGcinewaXqPIXNL_kOPftBId59ke3zKjBd0i7MT0zCmnFcapWZpS4_qlQF6jjBGzGs6v72S8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=WYwMjX6Lwts4yWoUrrVMG2E_lzf-ou7VrEgbjGfGaKpXqmtbchwg7SxGpy4KM2qpLM7sXdnxPVgN5B4-HQoxMkNur4IM-a8SGc58yPB2auExhe5K3ymL5h3eLAfMXTbzir61CnhlACnWgLZW7kVVaoD_21yLMa-8_66N8mMA3DTxK-xP9ZD752diLZDko4Q0gPgNof2mQ8jXY86rszIGKBTR2JEr3Bsg4V5KyeNlL1gSdHr6GdFXEq16WZ40BoCxdl-rt0IrJrZBzmGcinewaXqPIXNL_kOPftBId59ke3zKjBd0i7MT0zCmnFcapWZpS4_qlQF6jjBGzGs6v72S8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بین‌الحرمین، مملو از عاشقان چشم‌به‌راه امام شهید
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/448337" target="_blank">📅 16:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448336">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8caca61e3.mp4?token=DfLo85FTsbxTVYdTeigJUrz4DNp9B3Re4fYOd8Aiyow7ie58dU1B6JyBs4Z28p3WutIMPsc-vOjU50qRcn7TMYgni5XSIKVdQTQQneUJPq11QRF4oLyV-khVpTU2FKtIX9HDq4zaQG12ImsbVICrZsh7wvqNGLnzx7UOIdimASU8Cv6eAB4kFxquzpZrsv_aqpsPaJDiiu96DhqZOXSSnwPtTVhpciy7gGTC_WwwIPm9gt9P4DxNAIdQ7pjPGAzQskH3EXiZVLMzaT4ivTV5KCEfnuizubnuDAYxBGFqkmop_6dabfsmz1yZ_wB2TZ9vK-5QXv5XNycOIy7JcqDq-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8caca61e3.mp4?token=DfLo85FTsbxTVYdTeigJUrz4DNp9B3Re4fYOd8Aiyow7ie58dU1B6JyBs4Z28p3WutIMPsc-vOjU50qRcn7TMYgni5XSIKVdQTQQneUJPq11QRF4oLyV-khVpTU2FKtIX9HDq4zaQG12ImsbVICrZsh7wvqNGLnzx7UOIdimASU8Cv6eAB4kFxquzpZrsv_aqpsPaJDiiu96DhqZOXSSnwPtTVhpciy7gGTC_WwwIPm9gt9P4DxNAIdQ7pjPGAzQskH3EXiZVLMzaT4ivTV5KCEfnuizubnuDAYxBGFqkmop_6dabfsmz1yZ_wB2TZ9vK-5QXv5XNycOIy7JcqDq-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در کربلا با پرچم خون‌خواهی و تصاویر رهبر شهید شیعیان به سوی مراسم تشییع می‌روند
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/448336" target="_blank">📅 16:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448335">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71ed0fd55.mp4?token=tjpxa9ibqHLzwVSRjcmI8fmXIqbBG5hMzV38w5FAwqTFW2RdfNm1BfGUf7KrJadA5W5ww3iljTEnaOi0qhRG9ztO9JZJKCNPt7z6XlgZioBSFQ8V5O_3r7wqDAktcEDn7am_X7GuD_fGMBSQhMIhUaExNxXfW5X9j7EoSy-FIWtmu3FdBO7WJV9bMkL2Y8eqO1bwgwZGoOPIuOueT9ecrCDTvu5s2SZEYsOMdfhwav6PxPg7hg-TJbK_tLPOi-p0-SccS4ntrVIWbqF1LnBtLqSEkfsZZa_yEuBystUablJ9f4BAHV3E4srfIO6tIpeg3u-d1vn5PxbagLI5jd1y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71ed0fd55.mp4?token=tjpxa9ibqHLzwVSRjcmI8fmXIqbBG5hMzV38w5FAwqTFW2RdfNm1BfGUf7KrJadA5W5ww3iljTEnaOi0qhRG9ztO9JZJKCNPt7z6XlgZioBSFQ8V5O_3r7wqDAktcEDn7am_X7GuD_fGMBSQhMIhUaExNxXfW5X9j7EoSy-FIWtmu3FdBO7WJV9bMkL2Y8eqO1bwgwZGoOPIuOueT9ecrCDTvu5s2SZEYsOMdfhwav6PxPg7hg-TJbK_tLPOi-p0-SccS4ntrVIWbqF1LnBtLqSEkfsZZa_yEuBystUablJ9f4BAHV3E4srfIO6tIpeg3u-d1vn5PxbagLI5jd1y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع نمادین رهبر شهید و خانوادهٔ شهیدشان توسط شیعیان نیجریه
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448335" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448334">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912f4c8046.mp4?token=X3WHlQpEsJy0al3ww7sI3OdmhILVlDNcLtf0s9VLLJcRaDAexIw0Dgy8FVjoL_4Wz96DBDec5oZSEhu4TWRibUrTmq2KzawAgvcQll-IyoNWQ1rhh99UDyZ8SzL3UDCFhvyZXtYae-8KJ0i2tlnbSecBa5ERwYxjGjLHFL4bb0iWjSCuAVsVzZBtexVKErwVs6RTKEcbLwi8a4Gyl421y0ueO4hW8W5sFlXg8-ve1hCvwYavZFwcYJ1XyyrZ8YZOacbh5PHrExmHFCaJs-zqjS10PF7xjYWlJN5VKAB4u6YttBlf4ybI4o404yA50sXQ3t7TD07KnbulLI4KWpVqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912f4c8046.mp4?token=X3WHlQpEsJy0al3ww7sI3OdmhILVlDNcLtf0s9VLLJcRaDAexIw0Dgy8FVjoL_4Wz96DBDec5oZSEhu4TWRibUrTmq2KzawAgvcQll-IyoNWQ1rhh99UDyZ8SzL3UDCFhvyZXtYae-8KJ0i2tlnbSecBa5ERwYxjGjLHFL4bb0iWjSCuAVsVzZBtexVKErwVs6RTKEcbLwi8a4Gyl421y0ueO4hW8W5sFlXg8-ve1hCvwYavZFwcYJ1XyyrZ8YZOacbh5PHrExmHFCaJs-zqjS10PF7xjYWlJN5VKAB4u6YttBlf4ybI4o404yA50sXQ3t7TD07KnbulLI4KWpVqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون‌خواهی به سبک بچه‌های سیدعلی؛ محاله بگذریم
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/448334" target="_blank">📅 16:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448333">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر خارجۀ آلمان : برای پاکسازی مین‌ها از تنگه هرمز به توافق با ایران و عمان نیاز داریم
🔹
قیمت انرژی در حال افزایش است و این موضوع بار سنگینی بر دوش تمام جهان گذاشته.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448333" target="_blank">📅 16:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448331">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73768f58ca.mp4?token=OFh3zlDhSTBPe80d1d0Qn4cKHoIzdU9yTmAqf2MBrwm8E-7gGipiVkvrjTyKIqIdsXWKJfMn9-i5uR3aeDHNYWSFWEHvSpDy-jtDf1Hs36yOl4JVfyZYj3FXe0uE1H5jeIe4QcbH2g7asxe75S6NJiPn7H2ZbdMWH7keAA9PSRHRe2PrxV2mJGW572AFVzyEH-M7qX0XdKiZWfMGyYAA_09385AltInSMKDdu7DaX8MCPyyQLX_V888mMFTE_Pwmmj2ZBIE7AJrC4WJz3eb7F26nIzmC7uU53HwFfwOKHCgswL_NBsT5-N_6jt4Ad3IBT_wEZ5Xs7YTsqFbFkKyAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73768f58ca.mp4?token=OFh3zlDhSTBPe80d1d0Qn4cKHoIzdU9yTmAqf2MBrwm8E-7gGipiVkvrjTyKIqIdsXWKJfMn9-i5uR3aeDHNYWSFWEHvSpDy-jtDf1Hs36yOl4JVfyZYj3FXe0uE1H5jeIe4QcbH2g7asxe75S6NJiPn7H2ZbdMWH7keAA9PSRHRe2PrxV2mJGW572AFVzyEH-M7qX0XdKiZWfMGyYAA_09385AltInSMKDdu7DaX8MCPyyQLX_V888mMFTE_Pwmmj2ZBIE7AJrC4WJz3eb7F26nIzmC7uU53HwFfwOKHCgswL_NBsT5-N_6jt4Ad3IBT_wEZ5Xs7YTsqFbFkKyAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلهٔ عراقی‌ها در مسیرهای منتهی به مراسم تشییع آقای شهید در کربلا  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448331" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448330">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Q-VuyI6iZWLGnP9k8ISWxsf0bHiJ_HhCO2xJIWaeC8VJY8fvon-jT08r-oDGM1OzgaxXyGzj2qwYDKJ4kbTcgad9ahqI4NA3CBYuXE5qbA_MLjC8gbnp7Ghnni5VR9ldUFbRbZrxcwJsvgFTNtk2IZluLC4xvxT8P8cOiLZTKZA3EDbptKj743ZrneO1C0OEZlyVHoQnUMm17YisZXyWS59kIqokR_r7SEWOpyZd0PRK45KwlVTG1MxMDvy32yXVvFx5wx9DYVBOrBqXIIvb5uSL95kBiJ4lJTy34VZWSfCx0WxNjShzbFz9LjVIjDRTbmo8zZJG_Gev5P7RfnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سامانه‌های دانشگاه آزاد از دسترس خارج شد
🔹
سامانه‌های دانشگاه آزاد اسلامی از ساعتی پیش از دسترس خارج شده است. برخی منابع از احتمال وقوع حملۀ سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا تکذیب نکرده و اطلاعات کافی برای اظهارنظر قطعی دراین‌باره وجود ندارد.
📝
پیگیری خبرنگار فارس دربارۀ علت این اختلال و زمان اتصال مجدد سامانه‌های دانشجویی ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/448330" target="_blank">📅 16:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzkI1TZc4VPo_s311hWMmuk7z8ECBJPpQqZVld4vmqJZIdK8cqJPgCi3uC-Lt8MPXY7Gclx_1HDGOEBLVmWHS5XETHLORBg9oR6Sq26Mp0EgajXPNfsff2UoJkP9lSkuSg0pNS4615Ty3zvlIEw8lkY-8JBejBDo__MYAXQXAtKEa46SvuWweqiaEjbcdxt2ChTOSe4ulm2Ed49zPLnZ47qF6HKnCy1_ApWgWB-zbJKwrmhk_7-fZAd06DxhNHkn6HVMGmjRWYCGwzRbpkXRpQ28zhX6onE_9S7XOLr00H8wZ-VqEnW-m89gBfueYGw4hGkFkW6Q8j0JCQqtTbqojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obpMEB3-l9dggZyhmHlqgW0851lvlBLbH7gfd453CvWPWLC2AnFV5eqpx6x3OjLJbxfaqsl4a5dVXrhs4_Lkh6OtiKREp2BYu8qJHZTUZAJOicYg0bcEx7q3txvofdTC5EEn03QMMvVUdSBgvRv35pKCpEcd0l2-k584uoE6Azv6Pfp_SCoVEKa0w2uNm78N5toWQT4bL4LdkxZNVfvJ7-4F9GBzyTee_IQolKFlvyLzvC5xDMnxy7M-3E33offWIMBfaXHWU-EbNaNu72KmMxe4h4rjeBSG4npDjXiawhx3JuDwrSW3E8bB9wbACDSAyZMKxN-ulkQf6TqFjRg1LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAg52b-Eiv5OXwwaSs4jIXwZb9nlohWGhhd5TnhzbXlAVokk36GAiV45ExtbXZaUfBIRfRaVWlzwlqO2YCkHKvngQU8HvWOBJ2oeAnuvaUvzZ62f2z8z-43FQX_eUUeg2EmsiYzS-VuDD0ZEC1L61bIc_4iZkczQ9Up5jde722ZAYyuHeJC0_pgiX-BZ8MsXR-iGWktp6xuLdvTYv3JMNjynbXTJqw1zAcF71av7kODc99i0cm956UY8j3zTny9NdFLFV5aGXKA9d_K61Yj8dHTnz7klXirDJNEcTog0MER1PZ8ReOdpnKi6vuVXmR-_EfeJq46CGrirOPB44ki12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzXk4Oo34mA1Qg_V4tUvOtBZQfBa-oizzyCexdPfx2tAVfOi2enQkC7GjEyB0RhNHZMeZS4z4E3WQ7pPszlufIdCLsJrocw5wbRhCxGJ_b5i08QCjEBUm0EoCH4HtDVDPI7d6LQInQrtwxEbIbDWo8UuPacWHkGuz6Zs7_gFJJEZ9Uv0HP0GgJ2EkdnzC-H0XUgAnlngDfllm9Wa9rnkGtq6TmdIZ-pbTr0T6jFB6TLn6gqOObefT02HYWzDtyo-NuH_9E4SrfrHkBh29eUsLlRKhX97BFn7W_Ltbg0RSVThEedIXk1jJBnCuVOtdsBb0S2X8cyJwdl1RQupUaKXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MsnFEBbB30SB5aOblFoN-ZgG_4SGsbj4FVXiuVSkHa5SBwpKROsHwMjcpzlibCEl2h3M6EpEfTx2lPmlLp6op2uPEtdawcuxlFrRFHFjTYTitcO_WqxHoNfvhRO_hoyHsEA-LJGGbjZRIKcWV9b7greb15jx_bBs7i30-WAZop26tDvh0Wiq2jQW3BmmuvfeCL-Bopex6KgwvY3u5rN8L96mCbz6wOG0uPttzqIdf3nuZG1FjEgp6sSEjgq8NgBenoaQv40hilIv2rOVeBGDAP5iRhq3rrE4ywXn0vOE9Oi1Pfs10oBAjrLfrm05GwQcmnFXLrdylF9hkgoG0Eem5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hFDLnKqmGccMKoVVSBHRxjFJfrPyUs-5VjBgA0ZDKDotE9PLvp21jO4R4bl3XmfKN6aP5m6Wzb2Qb1ePEnAKDsTYdr_b1YXR54u2AAFOB9ilPIAn-PAFlo0Assfknsqf6S3TQ7raPEULJe0ymLE746BzMGV5bFoybZkqCvGHcbtJqljSm6YH0SjBkVgJfnAbkH52HfIeYwv2hr8N0y6Q0Nt1jkKrhx6TsW8VCl5lqnrScDBXqwPXh2rPD8Gio-FPg7m0KlJnBB8MI4uF9h2MZZ3js_vViB2ZoG1trP0qVHnI9_MS-HCBiuxq-wx5a04AEEPJhd6aOKMBq7amhZMbDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نویسه‌نگاری‌هایی از آخرین دیدار
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448324" target="_blank">📅 16:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfhOsfWa5XF_Wpn3YKGx1_TI9BDAQCZVaFD533jXpziXV6P_4p4tveqRjV53AJRtkyWqTyfmnxC4rj1GzaEewNRNscHF3vh2aiv6dg68qM_e7A1VLtZlwP2-DcukA8qT80OiBZZrvqdWqhjboJeh7fTjXAi2_7ZfpKHGFlxLpT7FLIPUBI1CZ3PGUTyUdtAO5TB_Pw-yrji3ECC9AYveatBNwjZ6P0F9BDxy2pcllBR7ucj8PoH8wDpYqKhEqPnaI2o2diK3DvXElsk1jtzChlAkKZMTEhEt1LWnDdDBOP58l9aH1tcl2_LP50pD6MoyPW9V1jO2I_8-wNKToq19Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجز خادم دههٔ نودی برای آمریکا؛ بند کفش ایرانی‌ها هم نیستید!
🔹
«باید خدمت ترامپ عرض کنم که شما بند کفش ایرانی‌ها هم نمی‌شوید و اگر ایران بخواهد، می‌تواند نابودتان کند…»
🔹
یک‌ آن، زمان می‌ایستد. فقط سکوت و نگاه مبهوت! حال مهدی دگرگون شده؛ انگار زبانش بند آمده و چنددقیقه‌ای طول می‌کشد تا خودش را پیدا کند.می‌گوید: « احساس کردم آقا اینجاست…»
👈
حال‌وهوای عجیب این نوجوان دههٔ نودی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448323" target="_blank">📅 15:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448322">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37af1d5cfc.mp4?token=YdyI0FOjqqnryALleSehLuxTF_DhxVeAamOae0zPkc5MEDyNf_bURjrFZMhBP7vEVo67g5AytZaCTAmy9asQ4wuTap7GeDFVEvPv0WcAo62apzHYxtNOfjPfjvlku1z2BaJnjBFGBHC0oDHhwx9qgBFlN9SgWhu3Qc90uKr-I6MvmdzmCxn6_tEJ2wV0HkJcawV1GDFhAH8qUGA2Lb891ExA4zZGkDymHpFVZISKd1T51ZXA_rbekJ4CvKBdZgTk3vFnvHTtyV2ByF6-joiVtH-J_Y9nOEek8kOQ51UBRTdMo-fUbZs3-DhYi0fjmdbDc01jnjQkstm4GWyJD4CpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37af1d5cfc.mp4?token=YdyI0FOjqqnryALleSehLuxTF_DhxVeAamOae0zPkc5MEDyNf_bURjrFZMhBP7vEVo67g5AytZaCTAmy9asQ4wuTap7GeDFVEvPv0WcAo62apzHYxtNOfjPfjvlku1z2BaJnjBFGBHC0oDHhwx9qgBFlN9SgWhu3Qc90uKr-I6MvmdzmCxn6_tEJ2wV0HkJcawV1GDFhAH8qUGA2Lb891ExA4zZGkDymHpFVZISKd1T51ZXA_rbekJ4CvKBdZgTk3vFnvHTtyV2ByF6-joiVtH-J_Y9nOEek8kOQ51UBRTdMo-fUbZs3-DhYi0fjmdbDc01jnjQkstm4GWyJD4CpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یزلهٔ عراقی‌ها در مسیرهای منتهی به مراسم تشییع آقای شهید در کربلا
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/448322" target="_blank">📅 15:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448315">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIgQ8A3xfTXxyFHC-g6eNrOvRqnBD08TxsKgN9S5ETOmocEmC4ixii-y7yUeWUNUF0Juqh5GYxcpil6nDZyCgy6lnY9Q50PR-MOnMHGvghW1uAee8dgQZ4P-3b-4xVlMe9m3z-RHAjOx3lSedPdtoFTrF1OdXmXHT-ppYPbUJu87DYQdxrmdqnjndpqYuzgZB0o8qu6B7Q1nzkf9lHSoFAPLRx_Q_2d0OjP2KpGs74d07M71Zcq60C80sEznpFm1xJH_ifJORjiV2mjmz7wtIFnTcd_Q3wgSF7M3a-qgdqsUI5BIqjFCBBH2EzBCiH0A_CBVladutxvoucjSKg-tHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIal9u0clg01ee3v4iEZrDe0Kw15QJF0sxpXV9Y6YwGrZO3hwbsV9Z3F5FhbJuPfAbQjAGFtHNZnQKerNIJJDbE44g4tPohfh9qNPUKJV4uq8k90SDrFEtL1XvXnHzxy-BPgM38jOaK4lr5gEyNAJ_XOaMO1MfENDF136W3hDWUKu23VLxANUcVkOZNOEyqs4f1BJdnI8YHO0hHw0-XGJiO96V4wG2eU-yHLMZTquNOu_cJUZTnQbnFEHW0m3XxtGlMKrLgOJXc-XtsmBJD-QBpjEdW29Ee79U3d4hrQEa54BzXHg23JSt7Hpo2vUNEjTddTygMLdB2OmnrAbqytbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3wG78r9-_MUpkT-aF5TPTKpTvbyFfAQuyTPfRXRVVw1Jb7pD968LJCv3deWk8NRoxxDFZix3iB6GXGTiDM3zNk9QTgtA6bpWFGlcHjLzD5q_pIRrQPLWe5zVpaysWSBMAlpQrcXdSns3tIAY2n0oIpqU0jJk3px8yAHkkgk-r0SPVyIgJmQBqI1EqO5k9lgA2slhrHW_uoyBaphNvlCMudlKxB1yKXgTgHKarlLwh5QwxYP5pLj55yoHyZn0i8tOdjn36C6QNxJpnPXbferaLSoeb1PaRx7SpKpGi6VN4xW097y9B1pfAoAlPp76XZReb1_BbiacNT2Gl4pbz3s2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TzHHRWwrahClYQQraCArqtbE7mjaVl422F49HHNrXvn4RLRiPz1QzfoCplg6dRmIJNLw69y3AHiq5QyOFirs7v7PylJvWsZ-Dabwp5r93oJAOG-wPznLDomT4XUFG6fcvVNlLGFf2q8b3QiELZ5z8SB4hbIMcakcJ_g8M-p0o_rfor6Z2Od8h2e1uuFnNZKX46n9IZhHIYD5fOfcQxcMdMElhkDKqNEE5RDdE88I1tvqxtH89iHUVDqXJGcc4Lh--XoeRNCO8svviILOL5udhHGjXLw1QOHkQqbELFx53-yvgn_sWOxW_YsuezvHmQYwO1b5XEbEriKcQxiNuLW8Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKqYhji7KlekGppJ5yYy2DfNqZLjEsRaQmQA62emsTdrUf6A6bWeSfFo5TyzFQThM3GuhU0uXhUjOhAkKdPtvNSmpMWTo3EdAazKKzgElg51lBpJitCp2acMP1UMAaPsJcKoAEm0vSdIQ52XMVNzMdV6dwqyYcUv0XQYN7AaUTkg-2NePmFXgdwEtiusSFmPj9488tqIUzwCaY_spyyq54CXco4ztbBGz9kA1C4bLQ3pDc-1rfJIm12xF1yQz7OXuBBgEfct_sBTlzOLwCSPZtO0kA_30IyfTQvGvDKLmxjg8AAdHATaN2BvkDMZa8sR2x9aCTTuTvYQcwxHvRqGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fsywQqIl82sp7mqu5hRG-W-Sz3yL1UHEiWxI-sCccOSWYaP8HIcLDHApFnPomBP7sSjXe8EvVbgT2wcpD1PKGZ7UKznLcMxqIlfMJb_4kwzbWf7s0kTNcoS-gApFOw4-06zyPadAPGUo2ZzzPMEvYWotYssIGD_y8jtbDNJmmrWsEXcRrWBgsCM1gULCTxfIr2Ub0YdpcXpHXCnLR-AOQclH_Rdo8xBV_7DCoxuSKyzfEe_zROLLr0-abfyD7ZrPgeorO2oPp7naq3L_cogQQBXg4LfhdgVoIkX6Hnn2Pa6GFXneKIXud_Gcz_3ycAbJD2WY7EE3NM4_bPiA-QoWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RPfrHLS0E5M7RQCJkBVEpWUkgcA0eSADeWB1T4BC0A8rZVebc4gUqw4j0T6YI6Tvu3L13-hvVNtMZP5zuA7hixAJf7VxcBrxM-oRhKA_Ic-TCtkXRjerqm4vlb7seNckMJFZqF0OZVcgvPQrlASR9uL7b6nhImF37CKpGj1OuYui3yvGuNhIYu7NfQDciHIxrkZGzGLBZe2uhBChPtCFv_dixJLGCb8yqnocLHpRtADo70Bj_e3hKQxyH3zu9ae-9aAiQW4Qual-6xbh5h_A0aVEwbLUreCNPvf_IxKMBACKMI_1tOzbDhnw0Wh_SVSHDPepFHGPHgHvnvz7siRsWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر رهبر انقلاب و پرچم‌های ایران، عراق و انتقام در دست مردم عراق هنگام تشییع رهبر شهید انقلاب در نجف
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/448315" target="_blank">📅 15:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448314">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59348358a.mp4?token=aX3veZeJl5Hg0BNPJB5EQ6TJrImAHfGuQkxd5zONdD82Iue72U6xUCztIOc0Lnf8H0NKbE62PZDu2ANk_O-chwxocZXQbIGOcUWE4Jh9vmVGrwwDu-cBTMm1L4uxTkh4IhoUGNSxYzDyqnOi5TX-4hKsWUmSiz89N4ahczUxbgiNpMCnLIH8K-K6ba2UZ_FRzTczQDuJjHz_AQ6ex3xxfbYp2McIcL8kRR3m5cMUygzy0p9GEBxmHTjzqHPgiEv6R3o78wh1q-_Anuerv8JoB_rndSCVU90hAbcJTmieUX29cAdbDM6mP55yB4_UQDnAV6QdhWiAp39NsCXNbLDbvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59348358a.mp4?token=aX3veZeJl5Hg0BNPJB5EQ6TJrImAHfGuQkxd5zONdD82Iue72U6xUCztIOc0Lnf8H0NKbE62PZDu2ANk_O-chwxocZXQbIGOcUWE4Jh9vmVGrwwDu-cBTMm1L4uxTkh4IhoUGNSxYzDyqnOi5TX-4hKsWUmSiz89N4ahczUxbgiNpMCnLIH8K-K6ba2UZ_FRzTczQDuJjHz_AQ6ex3xxfbYp2McIcL8kRR3m5cMUygzy0p9GEBxmHTjzqHPgiEv6R3o78wh1q-_Anuerv8JoB_rndSCVU90hAbcJTmieUX29cAdbDM6mP55yB4_UQDnAV6QdhWiAp39NsCXNbLDbvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش ویدئویی از تشییع و بدرقهٔ آقای شهید در شهر قم
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/448314" target="_blank">📅 15:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448313">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYJLSOmHJCS-3ZB2NhlEBXT5vkTcOLvaNoUZxS806AlA44VwI8-yhFWsEhz14C4Egq_eVU80xICMWjkZSRYFyq3qcW631WheSwmGFgAAZEG_OQwik91QAXBFKCfpoKFCQyNKSZ7vzweDTouXfVi31DEo0RibiPaacBx9vG_Vgy1p8oD-V-zj340T3w7l8qD8CUV75ur9FPaEvnrr0unr9b9syHk9ouoi_3n1oLhW2EFqt5dPdF9YL78fp6CUh_l6kAWlqyk0D9oZmnkvkkbegy0yl1SzjpcIOmH-ieHZzpp1wkJK5rRegsRTEk-1fKzGiVsRzzDmwSti_-OeMg8z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک‌های عامل فروش ارز اربعین معرفی شدند
🔹
بانک مرکزی اعلام کرد بانک‌های ملی ایران، سپه، ملت، شهر و گردشگری برای فروش ارز اربعین به زائران آماده هستند.
🔹
جزئیات مربوط به فهرست شعب فعال، ساعات کاری و نحوۀ فروش ارز از طریق درگاه‌های رسمی این بانک‌ها اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448313" target="_blank">📅 15:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448312">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57aab4ca1.mp4?token=pwirxfZ9xI55JcJdjgb38okq8jTE51VW3B7jJMC9Gyw_EkRZTga4ccxfzvwkjnTr-Mig08x3bbXfMySVBPq0lNay4h4n4SDe6rWwABIhtnt_oqJI6ZB_Pero2x2ZtCYn7NplsXGgcTLUvITi-sAZv1sdDWMql9c7ij59nO4MUiyZBhQcgJQfsd1LmnDRwyo50Yqt8m7rMvsD9-E2qXb0RyPTB-lp5U_psRvN31aZuM5wlXPDELWB3jQ4-piNUTwpIb2gX0QoWS6AzKHzkki_yBIkmuySdBbX6qUBIKRLwysWTCtlmcrZTTlYPnG8YJsBtGU8EWPJbjcMtetxFBTf8q3obXTgoknygYsBpl3EK9Eumx_Y1Q-1WjcwnuZr6BLh8C0wDP7jw8_mezQCh7f5SFr5d-nwcx02TwWgxUqw1ehxEmF5kOScurbdOy4-KWRlrns5pA7iW7FalHPustVII5YIk989s2_e2xdNQjO3bvBjc9hBPQwafJ6TQZ_nVawbzVJGogGJWpuXYIizL0xX7dHyAbt7PZ3LKXoAEnTMCi-bKUS39UlDubMpePq7jzY7qda0t7HGX5fJU4sh4x3DgAu2z5Ddguw6Sm_9ASBO09EEILQ9obwjQxzAMlTl6Umg2SsTwV5rJP29iKezAykALd9__1PTLuvHMGM1v8jcxDU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57aab4ca1.mp4?token=pwirxfZ9xI55JcJdjgb38okq8jTE51VW3B7jJMC9Gyw_EkRZTga4ccxfzvwkjnTr-Mig08x3bbXfMySVBPq0lNay4h4n4SDe6rWwABIhtnt_oqJI6ZB_Pero2x2ZtCYn7NplsXGgcTLUvITi-sAZv1sdDWMql9c7ij59nO4MUiyZBhQcgJQfsd1LmnDRwyo50Yqt8m7rMvsD9-E2qXb0RyPTB-lp5U_psRvN31aZuM5wlXPDELWB3jQ4-piNUTwpIb2gX0QoWS6AzKHzkki_yBIkmuySdBbX6qUBIKRLwysWTCtlmcrZTTlYPnG8YJsBtGU8EWPJbjcMtetxFBTf8q3obXTgoknygYsBpl3EK9Eumx_Y1Q-1WjcwnuZr6BLh8C0wDP7jw8_mezQCh7f5SFr5d-nwcx02TwWgxUqw1ehxEmF5kOScurbdOy4-KWRlrns5pA7iW7FalHPustVII5YIk989s2_e2xdNQjO3bvBjc9hBPQwafJ6TQZ_nVawbzVJGogGJWpuXYIizL0xX7dHyAbt7PZ3LKXoAEnTMCi-bKUS39UlDubMpePq7jzY7qda0t7HGX5fJU4sh4x3DgAu2z5Ddguw6Sm_9ASBO09EEILQ9obwjQxzAMlTl6Umg2SsTwV5rJP29iKezAykALd9__1PTLuvHMGM1v8jcxDU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین جمله‌ای که امام‌حسین(ع) امروز به رهبر شهید میگه چیه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448312" target="_blank">📅 15:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448311">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd340a6da9.mp4?token=KBv1iqRfGI_CVOC3eiHWoGwallWiTga-iHKWY8zuh_VUmIlJWwD1mifgYMCmOGQLyXsLdh0e0jeiSjWbfu9nwC7F-9kTRNAiGMiz6dDB_V-3p58AmnYJi8H7N2tc-h3VWiRyTWzPjEnRoS3TAvGT_HZ0MRXBlGMHAvcYdUi9HazyEHulLQWM-5lqzhfEBmw97E-jYcodKibsJrfoymMRql1KeKVAU-yBlekCOABN7v_PtwFcb6iz3_3bbQM7u5d2Qf9W108A7FPICyjoRrq2PEouUgEdP6OajxQuE1Tljz582qZcOASDz-gtWJPY2NzeZesRVpf44dsqokmlvjnf5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd340a6da9.mp4?token=KBv1iqRfGI_CVOC3eiHWoGwallWiTga-iHKWY8zuh_VUmIlJWwD1mifgYMCmOGQLyXsLdh0e0jeiSjWbfu9nwC7F-9kTRNAiGMiz6dDB_V-3p58AmnYJi8H7N2tc-h3VWiRyTWzPjEnRoS3TAvGT_HZ0MRXBlGMHAvcYdUi9HazyEHulLQWM-5lqzhfEBmw97E-jYcodKibsJrfoymMRql1KeKVAU-yBlekCOABN7v_PtwFcb6iz3_3bbQM7u5d2Qf9W108A7FPICyjoRrq2PEouUgEdP6OajxQuE1Tljz582qZcOASDz-gtWJPY2NzeZesRVpf44dsqokmlvjnf5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر شهید امت تا ساعاتی دیگر وارد کربلا می‌شود
🔹
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر رهبر شهید در کربلا از خیابان ابومهدی المهندس تا حرم امام حسین (ع) تشییع می‌شود.
🔹
پیکر مطهر آقای شهید از اولین ساعات فردا در مشهد تشییع و به خاک سپرده می‌شود.…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448311" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448310">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc79e99234.mp4?token=Zz4sEkOrVIMplMp5VwnC41UVAt0C2YdFMwuiHRXuduRDyvy-rvktJ1--RDpYxflFomXRmA3JrhgAdTQh-moJpAicJWO4QyJBfiunsMn6gRAEWZj7n4nn_qb2YcfXtB8Hby_sYq1MBmnMBCYmkY87hlt3l5upyZZ0d7zT2eGu9T9XDK9zjXVmxnL0auYIttZtRkJKFtXpvGgKgC9Ne9-5CtLCkCYuft6PrJuVGZ-qBy2_0l7YnUAXUlF-DrWOU3s5E05VcZAmoCQx7zHupIO34zkaXccGCCsg98WKp7ZRBR2ytpZ55jqAptqa7bFrqkAQ00kPxggHGJ-Nq_AfsnmEWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc79e99234.mp4?token=Zz4sEkOrVIMplMp5VwnC41UVAt0C2YdFMwuiHRXuduRDyvy-rvktJ1--RDpYxflFomXRmA3JrhgAdTQh-moJpAicJWO4QyJBfiunsMn6gRAEWZj7n4nn_qb2YcfXtB8Hby_sYq1MBmnMBCYmkY87hlt3l5upyZZ0d7zT2eGu9T9XDK9zjXVmxnL0auYIttZtRkJKFtXpvGgKgC9Ne9-5CtLCkCYuft6PrJuVGZ-qBy2_0l7YnUAXUlF-DrWOU3s5E05VcZAmoCQx7zHupIO34zkaXccGCCsg98WKp7ZRBR2ytpZ55jqAptqa7bFrqkAQ00kPxggHGJ-Nq_AfsnmEWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تابوتِ پدر می‌رود از دستِ یتیمان؛ تا در بغلِ شاهِ نجف، سر شود هجران...
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/448310" target="_blank">📅 15:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448309">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad06aa37c.mp4?token=KvBhKXBru2mrYuviDA_DDb7FzC82-emdJw20W4HKuvKnzsrrdSCMLbSRBFumzNkSxLKa7DI2fIzFai7nkCMSZbJD5o-XzyplupExC5XwGQXvcK1XLIVFjnrzQxvbF9BSNBCohbqpQLeUsi_33dQVrJSraf-0ngFbD1BsHd3fApOx16maJs9e-xV_4kE9i0VEFRD9nygoUtrPrvmaLGYEDrXchy-8Byo0X64-y5ozsosZO8X6OGxzxqrNwBeUSdgrwcEnMaoTAj5h9OCwV0xdYF6qrcXpipmFB2GvLcmM7Krh7ZMHvFoiazMa64NIFYlgFLwKxebhHCF5XdHIOxZL2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad06aa37c.mp4?token=KvBhKXBru2mrYuviDA_DDb7FzC82-emdJw20W4HKuvKnzsrrdSCMLbSRBFumzNkSxLKa7DI2fIzFai7nkCMSZbJD5o-XzyplupExC5XwGQXvcK1XLIVFjnrzQxvbF9BSNBCohbqpQLeUsi_33dQVrJSraf-0ngFbD1BsHd3fApOx16maJs9e-xV_4kE9i0VEFRD9nygoUtrPrvmaLGYEDrXchy-8Byo0X64-y5ozsosZO8X6OGxzxqrNwBeUSdgrwcEnMaoTAj5h9OCwV0xdYF6qrcXpipmFB2GvLcmM7Krh7ZMHvFoiazMa64NIFYlgFLwKxebhHCF5XdHIOxZL2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حملات ناجوانمردانهٔ آمریکا به حسینیهٔ امام خمینی(ره)
🔹
روایتی از سرگذشت ۳۷ ساله‌ی حسینیه‌ی امام خمینی رحمه‌الله در دوران رهبری حضرت آیت‌الله العظمی شهید خامنه‌ای رضوان‌الله علیه، به همراه تصاویری از حملات ناجوانمردانه آمریکا به حسینیه امام خمینی(ره)…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/448309" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448308">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
تصاویر حملات سحرگاه امروز نیروهای دریایی و هوافضای سپاه در پاسخ به تجاوز و عهدشکنی ارتش تروریستی آمریکا  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/448308" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448307">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae82bf5111.mp4?token=tDSDzPopaXZCpVdBrJKZLKaHGYFQwspVJ9neZOrH9N_AkFMdVJW9NCOoHDbz_FH_1tgjLVKU9sgTC0K93ED3JKo8B6gOfSzefp1HdeI6bXZSYc-LSf8RH0fbXRx5ArNgXQiBG1HC8CVBlFfO5bBCawoi10LHtm8ciJyZw_Z3Vpdf0ZyA2fjVsu4QGw3E_BAitKuiGP0fSBBJAeJY2sOTHY1rVrRdO_BFiH8xSY4S4lfc1YcJ5oLTi1Ad9OGJ9wqpKX4S-Z6uKxGZ3iIMIGdsdcY5ILHTu6JNjxb5jdrP5t7GVLi_S7gjSZr1eotzz8ZCyaF8Wi2a7q_VkBMoKW315A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae82bf5111.mp4?token=tDSDzPopaXZCpVdBrJKZLKaHGYFQwspVJ9neZOrH9N_AkFMdVJW9NCOoHDbz_FH_1tgjLVKU9sgTC0K93ED3JKo8B6gOfSzefp1HdeI6bXZSYc-LSf8RH0fbXRx5ArNgXQiBG1HC8CVBlFfO5bBCawoi10LHtm8ciJyZw_Z3Vpdf0ZyA2fjVsu4QGw3E_BAitKuiGP0fSBBJAeJY2sOTHY1rVrRdO_BFiH8xSY4S4lfc1YcJ5oLTi1Ad9OGJ9wqpKX4S-Z6uKxGZ3iIMIGdsdcY5ILHTu6JNjxb5jdrP5t7GVLi_S7gjSZr1eotzz8ZCyaF8Wi2a7q_VkBMoKW315A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر شهید امت تا ساعاتی دیگر وارد کربلا می‌شود
🔹
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر رهبر شهید در کربلا از خیابان ابومهدی المهندس تا حرم امام حسین (ع) تشییع می‌شود.
🔹
پیکر مطهر آقای شهید از اولین ساعات فردا در مشهد تشییع و به خاک سپرده می‌شود.…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/448307" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448306">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1A6-jh32xZzERt9P1x_q2HYXkRrorS3wobAshJd1zJ9SiCIUENsOcF6ItrHYDOYaxcZDLXA3PeZhyGp3X_F1p-mJVzEGKRVXNN35c4hZcXNBVyuOG4tGtk47sodHwWWBIQeisTSxjbHjW2tQEPSd7447EasegRUdkshuKoW7SEcTJXWxgyjOC-DrkC0LqMN6w2tNQBju68Ir4mvsNWCxFPtjRNql_XxHALOqSLSRDSc91Dos6c-g6fpEK0AQ3it53ExbYyTMUYgCUVwSxPav0yOYqXsOHdgaxpKs2QTUyCZQIFFFs1owEVxPYXuKPsOLikVlawRC8jSxWcU6rMe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید بیش از 563 هزار تن فولاد در چادرملو تا پایان خرداد ماه/ رشد 18 درصدی فروش
بررسی آمارهای منتشره سامانه کدال حاکی از تولید 563 هزار و 27 تن فولاد در شرکت چادرملو از ابتدای سال مالی (اول دی‌ماه 1404) تا پایان خرداد ماه 1405 است.
بررسی آمارهای سامانه کدال حاکی است از ابتدای سال مالی این شرکت تا پایان خرداد ماه 1405 در مجموع 4 میلیون و 368 هزار و 576 تن کنسانتره آهن (خشک)، 668 هزار و 436 تن آهن اسفنجی و یک میلیون و 747 هزار و 812 تن گندله در چادرملو تولید شد.
این گزارش می‌افزاید: مجموع فروش چادرملو در این مدت 505 هزار و 187 میلیارد و 283 میلیون ریال بود که در همسنجی با رشد 18 درصدی نشان می دهد.
5524 میلیارد و 838 میلیون ریال از فروش این شرکت از محل صادرات بوده است.
سال مالی این شرکت منتهی به 30 آذر ماه 1405 است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/448306" target="_blank">📅 15:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448305">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBM7EWXe7waE3JiDdc3YE5f0IdrkrIq-3wdXXpJIj_3KoMrB_FJU30nVj0x659-a26YkJUxzky5a-B6Xe2K8dnG0r-My7GTTXPMkv9zOAleij9dYIxVVp2dOmE5cv6AJlsJax1fLwfzCH5hGrfviQ17PBsHpDz6JpbKPEM4rXammXqCEwqtBLZW8juFAq08NqbpZms1e7FVlNAiVCJqUp8kYoWSarZf--_Ck7JWN5zUw32V8ENgHyn6cyokkjerZkzgi2H2NhQx5h9l0zwfPkI3SCgEhK0pRxwjPFJ5me3RFYL-5MFjtkld-fjI_TyLyDCpnD9AvctjwN59x6nvqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/448305" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448304">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/448304" target="_blank">📅 15:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448303">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🎥
تصاویری از حملات ناجوانمردانهٔ آمریکا به حسینیهٔ امام خمینی(ره)
🔹
روایتی از سرگذشت ۳۷ ساله‌ی حسینیه‌ی امام خمینی رحمه‌الله در دوران رهبری حضرت آیت‌الله العظمی شهید خامنه‌ای رضوان‌الله علیه، به همراه تصاویری از حملات ناجوانمردانه آمریکا به حسینیه امام خمینی(ره) که برای نخستین بار و همزمان با سفر رهبر شهید انقلاب به کربلای حسینی منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/448303" target="_blank">📅 15:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-448302">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6e6f7d8e2.mp4?token=bP9PBACEMtiwP77wFKJ5hZcRZSiPf6wq3EElbrWKNhUszHqBGiNYxXughEYC5AkTTrK_kQrgF3KOMdpcYEnJrWGpI2IDTBPNhg4hRzPhR8JHXx7L2LolKneReTXCjy8vqu5KiGXbeqNl9wQrECnJnFVOGfU2Cided7eky0vZ3NmNs4FShBH7EJul9LK0A5H2V7AF325xMWozG6gv2i9fpJwUKN7wUr8XgiEjfTeBXv9026vr4iI8iDNzYedqxDQJBNFq25M0VQouckzA8p-nRuADczy7iObHATOXxw2lfUETymwIr40YQVqzgeHFkfBJ7PynJAXRVK73DnjMoJCsuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6e6f7d8e2.mp4?token=bP9PBACEMtiwP77wFKJ5hZcRZSiPf6wq3EElbrWKNhUszHqBGiNYxXughEYC5AkTTrK_kQrgF3KOMdpcYEnJrWGpI2IDTBPNhg4hRzPhR8JHXx7L2LolKneReTXCjy8vqu5KiGXbeqNl9wQrECnJnFVOGfU2Cided7eky0vZ3NmNs4FShBH7EJul9LK0A5H2V7AF325xMWozG6gv2i9fpJwUKN7wUr8XgiEjfTeBXv9026vr4iI8iDNzYedqxDQJBNFq25M0VQouckzA8p-nRuADczy7iObHATOXxw2lfUETymwIr40YQVqzgeHFkfBJ7PynJAXRVK73DnjMoJCsuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران باید پایان رسمی تفاهم را اعلام کند؟
🔹
از لحظه اعلام آتش‌بس تا امضای تفاهم اولیه و مذاکراتِ پس از آن، مقامات ایرانی در سطوح مختلف بر یک نکته اساسی تأکید داشتند: به آمریکا بی‌اعتماد هستیم.
🔹
پس از امضای تفاهم تاکنون، آمریکا بارها و به روش‌های مختلف،…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/448302" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
