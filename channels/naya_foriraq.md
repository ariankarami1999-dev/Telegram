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
<img src="https://cdn4.telesco.pe/file/unjV7PusOWgWK5spoVRUnafP5_9I7qjUfcOZtWDT0U5OkdJIx-tRemqZFsDapSd7N1_sB2AQrgJ9nBo-bFsi8BPF0oZ4YRTYQm9OE9U0oAruRVBEJX-1rfd1TznG0UeV_FMpI9i1YHLgg-D5e00EPp-3z6w6RQKKxbkWF5hwTNt62W5A96tuT_0rZJYFYM3JrIsMb7hWUeNu-ypjb0w9LZLZpEu6umt0COGymGUFHMjcjYeSEftmgIuYdOVmlCy5rRs0n5ScwRa1hsBM0MVod-tBhGCUF44ByJcHpyTX9bGbPz5lEiG4NmTDsc-uzHGeVENZXcNE7rSA-jk_clq9hQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 08:40:25</div>
<hr>

<div class="tg-post" id="msg-87177">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2feb1679.mp4?token=uQ_mtVxLV-Kzaxg7y_XhBQNaWAUF70jx_MmFXrkPw0-fAeuFgf6HgrfViMQMnPjtdOb0KapMGfysJManukrMwCfmb5S_x5KUaVPksR6Y0WGThwedHd_tX6LW7gCetiS5manLZ-UDKfi3zbtvo7vENCagmSF2v0qH4ksW3IrinM-kNPAJXxZ-U57cyBSgcvlhIo06GUVyYEK8ALoLGRrwUvf2E3GBv9_z74eyTktQaJTPCLcZXSrMxv56SfptRPfKzEKF1EU1bdO7Yi3nB_ry186cms0MPhoa8jylGlg0Jab-H4-YON_b0sTp2jNTix4T-8JxhaUiXpwGsNHOr2jh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2feb1679.mp4?token=uQ_mtVxLV-Kzaxg7y_XhBQNaWAUF70jx_MmFXrkPw0-fAeuFgf6HgrfViMQMnPjtdOb0KapMGfysJManukrMwCfmb5S_x5KUaVPksR6Y0WGThwedHd_tX6LW7gCetiS5manLZ-UDKfi3zbtvo7vENCagmSF2v0qH4ksW3IrinM-kNPAJXxZ-U57cyBSgcvlhIo06GUVyYEK8ALoLGRrwUvf2E3GBv9_z74eyTktQaJTPCLcZXSrMxv56SfptRPfKzEKF1EU1bdO7Yi3nB_ry186cms0MPhoa8jylGlg0Jab-H4-YON_b0sTp2jNTix4T-8JxhaUiXpwGsNHOr2jh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
حادثة إطلاق نار داخل مدرسة في بانغ كرواي بتايلاند مقتل وإصابة أكثر من 20 شخص.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/naya_foriraq/87177" target="_blank">📅 07:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87176">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275832bc3a.mp4?token=U8-C4ojj9kqy4r4IqjpgAt5cbzSo6N1_zgX1cOfjSfON9XMJyKPFxg7bs_UxiMgTHVbrTt2Cjg9TzWtbql_YM8IhWUugYSsiQnjQMC2w5_8KNZuzqEcICRrFlvO-ZPJkiGA6CSD3agCxi_XKkTfb9GUh64VqVGM5Dy2ZkwG2ynZKr_Ft2Ki_sYH8DvmflsmL4QN4wL-zP9p6DoWbew0cKymilFNqAw-KvPgQAmPxtgif6SXamCiFdExcjafNCgRtHl-k2rw7FmgT1RdqMjiznCU7d5NXP7TweeDqhU_PuhM09XJ-vfqELtypp9jWKBOA0klUx3C25k2l-cJrnu-TQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275832bc3a.mp4?token=U8-C4ojj9kqy4r4IqjpgAt5cbzSo6N1_zgX1cOfjSfON9XMJyKPFxg7bs_UxiMgTHVbrTt2Cjg9TzWtbql_YM8IhWUugYSsiQnjQMC2w5_8KNZuzqEcICRrFlvO-ZPJkiGA6CSD3agCxi_XKkTfb9GUh64VqVGM5Dy2ZkwG2ynZKr_Ft2Ki_sYH8DvmflsmL4QN4wL-zP9p6DoWbew0cKymilFNqAw-KvPgQAmPxtgif6SXamCiFdExcjafNCgRtHl-k2rw7FmgT1RdqMjiznCU7d5NXP7TweeDqhU_PuhM09XJ-vfqELtypp9jWKBOA0klUx3C25k2l-cJrnu-TQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المروحيات تحلق بكثافة أيضاً في سماء محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/naya_foriraq/87176" target="_blank">📅 06:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=S8ACvVe93YhpG1dRL0TxqYqTNabhlTGb8Ty3FJA2UNoteWRFyPYpIcoj2jGQkcPlfqOx7sQhAaHauocRp0ZvY6k2p_gu2y1beue3hwdK3PAtOvw9W33aZc7WnnEJ24M0MOHRFmC7ppjU_OZc1M3eM7GM-B9H5Xu3frIh90DsTyG7GRUj5yx2uEIIukkbmq_TR32DjbA2LT6HeGckIiZdYtGJ1JkItvhlUCgoUTW7i1tF-vqz3H74zHUkWR_hKZMbd6Cb36TtKs211zx6luPFalNZlxR7IuDzs6ZOIUfQGw1NLOxUYvRZeufOYyXwaVJbodRKJul2qZeXi8mYnXkjuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=S8ACvVe93YhpG1dRL0TxqYqTNabhlTGb8Ty3FJA2UNoteWRFyPYpIcoj2jGQkcPlfqOx7sQhAaHauocRp0ZvY6k2p_gu2y1beue3hwdK3PAtOvw9W33aZc7WnnEJ24M0MOHRFmC7ppjU_OZc1M3eM7GM-B9H5Xu3frIh90DsTyG7GRUj5yx2uEIIukkbmq_TR32DjbA2LT6HeGckIiZdYtGJ1JkItvhlUCgoUTW7i1tF-vqz3H74zHUkWR_hKZMbd6Cb36TtKs211zx6luPFalNZlxR7IuDzs6ZOIUfQGw1NLOxUYvRZeufOYyXwaVJbodRKJul2qZeXi8mYnXkjuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من تحليق الطيران المروحي في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/87174" target="_blank">📅 06:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjO9ZhgLf5bm8r0C8ZMk_fNf-vO8VzTdFcGeXroZpUtJuoI65V_tINZoXKcJluCXhtJUuOcgNc9WFRs4pk0_4Ra3Hnr6H-gA8VPmZoQr4kxWX_OvLwLseLMnP5QA3l7Ao0Y0xjcFeCc_VzFAmbnfOUKulWa98tBwtEPlr1_BrqdW7HVNazMbHNDmo2b56X--PUJY5NhpuTzqesVWhXdcsgLEN0yipd6YlCM-RnaGsf2RmsDK0c_6hSTKKOFF5gKQNGboBOWT5LfdhbSv3YAlA_UmBXBXpJrvWO5kPur0NhPO3qgpLaEr1KoeCIUG9OLLowWswXPywvuYZOe25nBYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
طيران مروحي كثيف يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/87173" target="_blank">📅 05:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87172">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302813141c.mp4?token=FtktAFa_dyOWyPynFbQ9TZhVAg3nuEMZF43m0xiGd1sbQdBcx5rJVpNtsCI9vUrOT8V3y7p9qiQ3ScjM_xJHe_ivvOtVygNKFF0Ko5ZEoIwuySsWgG3yHAGw8v3wQY0elVF8tRfYeNBhVO1DznKxkTu58uj36-A_BY8nh-oE1p8tCz91ZXVG5Hg_j-Lwu8ZqFb7myaWUriW6r-x7uNoqOLo6RMMUUOGqsAG2HG5rTxiiR6YhlS016OSzVS7vSr4XSKgAyZC4mhMNf93_-yLU-W_FJ4Wj7QgG8vSvszm02cn-APq8fc20oPbG3MbQrSziJFPdC6lGiAL4SaUilwZgk0i-vlMLHeuqT1kCxsEe8wXfyICzBCcQL2WB3G7AFijMYTdNmdt8FzobqLjy1_l9ksqF_JHLf8uFR5oX37THNiILZk4UGXrqUzWwwzpQ0C_4oR7XFji4E0iWtl8VQE_miSb0zwLTkTtfLPVflh_QSHGxCy01GUVO94gU_fGfl2xJh7A6WhQMg3Mg9GyEQaUnen1mkPIq87FqB8VXy5jGxprVL6h5ZXT00vLAR4i5imf4mQCf6IPuymKlwC_aRIp0B28RXHxDvbp34IbwhySR0SAnMoTZ-T1lBRPPKJaKAFyAWOdrhCCsMAicQxBSiEjOiAN1iH7HNdFJuZt50xxDfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302813141c.mp4?token=FtktAFa_dyOWyPynFbQ9TZhVAg3nuEMZF43m0xiGd1sbQdBcx5rJVpNtsCI9vUrOT8V3y7p9qiQ3ScjM_xJHe_ivvOtVygNKFF0Ko5ZEoIwuySsWgG3yHAGw8v3wQY0elVF8tRfYeNBhVO1DznKxkTu58uj36-A_BY8nh-oE1p8tCz91ZXVG5Hg_j-Lwu8ZqFb7myaWUriW6r-x7uNoqOLo6RMMUUOGqsAG2HG5rTxiiR6YhlS016OSzVS7vSr4XSKgAyZC4mhMNf93_-yLU-W_FJ4Wj7QgG8vSvszm02cn-APq8fc20oPbG3MbQrSziJFPdC6lGiAL4SaUilwZgk0i-vlMLHeuqT1kCxsEe8wXfyICzBCcQL2WB3G7AFijMYTdNmdt8FzobqLjy1_l9ksqF_JHLf8uFR5oX37THNiILZk4UGXrqUzWwwzpQ0C_4oR7XFji4E0iWtl8VQE_miSb0zwLTkTtfLPVflh_QSHGxCy01GUVO94gU_fGfl2xJh7A6WhQMg3Mg9GyEQaUnen1mkPIq87FqB8VXy5jGxprVL6h5ZXT00vLAR4i5imf4mQCf6IPuymKlwC_aRIp0B28RXHxDvbp34IbwhySR0SAnMoTZ-T1lBRPPKJaKAFyAWOdrhCCsMAicQxBSiEjOiAN1iH7HNdFJuZt50xxDfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مروحي كثيف يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/87172" target="_blank">📅 05:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87171">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
هجوم يمني بالطيران المسير على مقرات مرتزقة السعودية في محافظة حضرموت.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87171" target="_blank">📅 05:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87170">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
هجوم يمني بالطيران المسير على مقرات مرتزقة السعودية في محافظة حضرموت.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87170" target="_blank">📅 05:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87169">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfd307190.mp4?token=RnSPVuaZ4dhffSeYX5C3H79acp73jXyqKXjX7SGpFI2Ksc8h8CLo9Ko5PTOPEj-doB_ECP2wGeDMqdpMtxB_iVlQPP3bFlZkaA5EKQU_JuHMBUkJPR1_AO0sUaInk_oiFjEIqMHdbtvKOtvppen0fDwQJnwIxQ_nBt-2QbFk93z0j71OSZSWGmC9dF6tNMMVHYyn66I4OHLcvChDTQXJ8eqzdCcMao6c5yu3eba5_Jxwe8LHHNasGFUocwdplqPaxDomgwDqZP2U2v34QqSK_G2PUypLv3WWT4f8Jocn0aT1rv1rIqjGtbpIuV3EhIabQOepJzSDji0nEWYBIwGP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfd307190.mp4?token=RnSPVuaZ4dhffSeYX5C3H79acp73jXyqKXjX7SGpFI2Ksc8h8CLo9Ko5PTOPEj-doB_ECP2wGeDMqdpMtxB_iVlQPP3bFlZkaA5EKQU_JuHMBUkJPR1_AO0sUaInk_oiFjEIqMHdbtvKOtvppen0fDwQJnwIxQ_nBt-2QbFk93z0j71OSZSWGmC9dF6tNMMVHYyn66I4OHLcvChDTQXJ8eqzdCcMao6c5yu3eba5_Jxwe8LHHNasGFUocwdplqPaxDomgwDqZP2U2v34QqSK_G2PUypLv3WWT4f8Jocn0aT1rv1rIqjGtbpIuV3EhIabQOepJzSDji0nEWYBIwGP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/87169" target="_blank">📅 04:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87168">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff414bfdb.mp4?token=C26gAz4qBvVs_L_ajt4UY1DbeBBszgz5xKp8-BjgBq1T18TSGtglM9HQujHmlfhDJ1zeR0lO8qj0j2MLwoU1CfZraABegkT60QLUZEEZ2GBuey6Qs1Q6WDLED5-4v0I0oNlL7vOcbErdVYv4--b56e4MhTMU5FMJp7JJLo7SPOB8QPy6J8k78TM8EaZ_Y_7uVKHleTbEI-h7CIkuuF9rSctbFYlvvTwvguy8fYqEUNSCE-j5y9-HoWa_vQJlarSFzlgtfbMrsdMu8S2jQVwggCtnd6y3IwD4gHPmWCPrAhWvb4x9IpKT9iXXhn7kIIbZXC4JfPGMOzrrGErZifLM2iUqvZKJkDm5gUK4DNuPKEXGRjhItwjkKmx4ddjQriaOuz0F1oISh5zWgndJq5F-O8iU2yOFYLOVHbJN7CU6IGZ5OxIgZ9lMcgocwhz8H6V5OJQ1GyMgjZ_ncrSEa669TTx0xhhV2H3NkW_f6SJpultLefj5b8eJiUfKyYPQ_i3qt0qBvxDptpxT1-uMqR-MPdgBqNuvgC7Sd9pbLE35p69nwzdBYtrEuffMqapC-WNJAtZYiWTQVPncCtImoUqheRrgCkNHcKaHjuz29WMq7sUhmg92iMA7-_83b7xsty5ZF2oK3oPHjO1GTGW_WHp9Z99qNhSHAZAaSwrzxvJJaGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff414bfdb.mp4?token=C26gAz4qBvVs_L_ajt4UY1DbeBBszgz5xKp8-BjgBq1T18TSGtglM9HQujHmlfhDJ1zeR0lO8qj0j2MLwoU1CfZraABegkT60QLUZEEZ2GBuey6Qs1Q6WDLED5-4v0I0oNlL7vOcbErdVYv4--b56e4MhTMU5FMJp7JJLo7SPOB8QPy6J8k78TM8EaZ_Y_7uVKHleTbEI-h7CIkuuF9rSctbFYlvvTwvguy8fYqEUNSCE-j5y9-HoWa_vQJlarSFzlgtfbMrsdMu8S2jQVwggCtnd6y3IwD4gHPmWCPrAhWvb4x9IpKT9iXXhn7kIIbZXC4JfPGMOzrrGErZifLM2iUqvZKJkDm5gUK4DNuPKEXGRjhItwjkKmx4ddjQriaOuz0F1oISh5zWgndJq5F-O8iU2yOFYLOVHbJN7CU6IGZ5OxIgZ9lMcgocwhz8H6V5OJQ1GyMgjZ_ncrSEa669TTx0xhhV2H3NkW_f6SJpultLefj5b8eJiUfKyYPQ_i3qt0qBvxDptpxT1-uMqR-MPdgBqNuvgC7Sd9pbLE35p69nwzdBYtrEuffMqapC-WNJAtZYiWTQVPncCtImoUqheRrgCkNHcKaHjuz29WMq7sUhmg92iMA7-_83b7xsty5ZF2oK3oPHjO1GTGW_WHp9Z99qNhSHAZAaSwrzxvJJaGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مسير يحلق بإستمرار في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87168" target="_blank">📅 03:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87167">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKskodymInD8j8GeHu8uEEo_x350cPfGe4cXOYmvpbWQ8H3hlGsP2KJ65nNKfFXUV3145q9DGbByxRC5VRPwydJiH49KcgY17HNwyhEorb5McHjrBFhy-wIysQ5LGVsMCJ2aP2iBU-R7jMJCkQqmnNtJTCUzNOWYMeJtVdENk9OLdHeEfrFEGzDmf5tnKj2xCn1egmoEgwUXJ6AdrqTIGhnK2MNba4dkFkobjzZ4Ulb3oBpEbVkuMaYV5q4ZCAwsP7XKEFPOks2JushV9BDygOcEDTXZiD7pv2IBZkT6j-hM4VSc0wkRjeiYG8AtzAg_vyGvfzleLlf1ROPmENHBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إغلاق مطارات أبها الدولي والملك عبدالله بمدينة جازان ومطار نجران الدولي في السعودية وخلو أجوائها من الطيران المدني.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87167" target="_blank">📅 02:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87166">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
عصابات السعودية في اليمن:
مقتل 17 جنديا وضابطا وإصابة آخرين في هجوم المليشيات الحوثية بصواريخ باليستية ومسيرات انتحارية.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87166" target="_blank">📅 02:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87165">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
ترامب اشتكى سرا في الأيام الأخيرة من أن الكشف عن انخفاض مخزون الذخائر الأميركية يجعل واشنطن تبدو ضعيفة.
ترامب كان على دراية تامة بأي مشاكل محتملة تتعلق بالذخيرة منذ أشهر ولم تكن التقارير مفاجئة له.
ترامب كلف وزارة العدل بالعثور على ما وصفه بالأفراد "الخونة" داخل الإدارة الذين يكشفون المعلومات.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/87165" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87164">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/curgJPMk0zIh7lxhhERsIqw6JPukYk1GX3j3_FL11GGVDdNNBGi9f5I_mCLofytOJ7LA1k6HaKQWo2ghdbeyLUE3Zr8Lw-ViolQwkqIo6SaUNHcgKcFZPo9XduCYtOX2pYRMBViFP7pYrHNbXiS9dI8xJbVUpSRmpNi5V09I4zS6O7QlDyy11JvfwyfiZoaQi1oSLmHnw56ZzFklyXOozjvkrFm2UkS1ae9lDKplKlxNxT8qE6ydN9nAucl6vsGev6keb-ihcmzlHwAytG0eS1L06VNw32RO7y1awkC62wW69I9JVxvVsdK7aNjHqjDtqmUgoLx-C2EPJNEPTOnnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/naya_foriraq/87164" target="_blank">📅 00:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87163">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/87163" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87162">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔻
مصدر يمني لنايا: مقتل عدد من الضباط السعوديين واصابة اخرين في المعسكرات التي استهدفها انصار الله.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/naya_foriraq/87162" target="_blank">📅 00:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87161">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8949db271c.mp4?token=mA7lBynqeXJRCbw_GO8RTH6d6BcJESUTjhJrWK6MLdJtufQI4cA9qp5Dc39DLVweQJVOHUQpEA6Iim44JpdkaM8jASAvZ3eXGfvtIlvYbSY1AR6qSOo13dcEs0WeMgPW-fcdedCNnAXHzUCU3zqMhZ15ZkYxrapeJduaj4IHoKUL5Tfm_7Mu3gP21jY-j2PKUnmgh75iqICIp-Pc5hCjLFw8vf-3vXCQD9-Jqj_xOATwA9SKvdXp3LwdWyuxD2H80rwQLp_GvDwryycSkE4vAT5sGSh1FLVMOAqIi_XYDiNMZCrdv1s-cZbjD5QEVEDOvQ-iM7vfM4F7uRgO-9wiCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8949db271c.mp4?token=mA7lBynqeXJRCbw_GO8RTH6d6BcJESUTjhJrWK6MLdJtufQI4cA9qp5Dc39DLVweQJVOHUQpEA6Iim44JpdkaM8jASAvZ3eXGfvtIlvYbSY1AR6qSOo13dcEs0WeMgPW-fcdedCNnAXHzUCU3zqMhZ15ZkYxrapeJduaj4IHoKUL5Tfm_7Mu3gP21jY-j2PKUnmgh75iqICIp-Pc5hCjLFw8vf-3vXCQD9-Jqj_xOATwA9SKvdXp3LwdWyuxD2H80rwQLp_GvDwryycSkE4vAT5sGSh1FLVMOAqIi_XYDiNMZCrdv1s-cZbjD5QEVEDOvQ-iM7vfM4F7uRgO-9wiCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: لقد نشرتم ليلة أمس أن الولايات المتحدة تمتلك مخزوناً هائلاً من الذخائر، ونفيتم وجود أي نقص. هناك طلب إضافي بقيمة 21 مليار دولار لإعادة التموين، فلماذا هذا ضروري؟  ‏ترامب: لأننا نحتاج إلى المزيد باستمرار. لقد قدمنا ​​دعماً هائلاً لأوكرانيا. هذا ما قاله…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/naya_foriraq/87161" target="_blank">📅 00:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87160">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b995216d5d.mp4?token=ixtBN7UOvkgxm6Vbt-D593tv9dYtZQE1ozovbucBAJ3iyl1JRuYmY6aNguOk4ONtCNnIc6HJC85soNyMxbHDyGBZLzARIs1GPNeIwfwwto_J7hj1oINJ42kLafB2gvEs0puWDHPd-OsrNJLQpkuuQggksLX7S3Hww5Zi2UllEUXzaGx1CWPekbx2tcaO0G-7Fu5o5c83ux8N7n7urk5RZqOjYCltLBpogXIbMiyBi5ksmhTosK5c8fdaDhXQmeSUWJMysTlZCqQHBNoq-GAXxfpERNSjgZfrrBLaQPLtz_ICjYqLkOb9-ELoEpzFHv1j5v12CLTB3DXSiiiJ74zcSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b995216d5d.mp4?token=ixtBN7UOvkgxm6Vbt-D593tv9dYtZQE1ozovbucBAJ3iyl1JRuYmY6aNguOk4ONtCNnIc6HJC85soNyMxbHDyGBZLzARIs1GPNeIwfwwto_J7hj1oINJ42kLafB2gvEs0puWDHPd-OsrNJLQpkuuQggksLX7S3Hww5Zi2UllEUXzaGx1CWPekbx2tcaO0G-7Fu5o5c83ux8N7n7urk5RZqOjYCltLBpogXIbMiyBi5ksmhTosK5c8fdaDhXQmeSUWJMysTlZCqQHBNoq-GAXxfpERNSjgZfrrBLaQPLtz_ICjYqLkOb9-ELoEpzFHv1j5v12CLTB3DXSiiiJ74zcSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:  يشعر ترامب بغضبٍ شديدٍ في السرّ إزاء التقارير التي كشفت عن تقلص مخزونات الصواريخ الأمريكية، إذ يعتقد أنها تُظهر الولايات المتحدة بمظهر الضعيفة بينما تُمارس ضغوطًا على إيران للتفاوض.  ويُلقي باللوم على التسريبات - وليس على بيت هيغسيث -…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/naya_foriraq/87160" target="_blank">📅 00:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87159">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19bad4fe07.mp4?token=JIZkmvQCSGirobcU72Ic74EhfTY0VklfVRc5lgHq714lZyVZ5VKwiFaBehtVpgZNDDRoW0Urnv_to3xFWwY3fVxdRp_vt7W-eNsTRVuh2Kf0f2t-TWoqN7QF2c9JkIwiM9v6uiIOKXP7U6pAP5bLE4MTS6XBqbS0M4n6ynsFHjs_xA8nJSAJ-IW6fYaXfbFakShwVh5LczTtCSMLxDdGTS6RmWVkZMiYD2_k2dnEwlqBGERhGHcEI81YXADNy7OYaHfJJ-RkhttxychjXOq6Hi8xNNdWxPJEOzdjvOigpc0qOZVFBJ_McrG48mSfChmUbyagd0TKq8b6v6iwsUVNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19bad4fe07.mp4?token=JIZkmvQCSGirobcU72Ic74EhfTY0VklfVRc5lgHq714lZyVZ5VKwiFaBehtVpgZNDDRoW0Urnv_to3xFWwY3fVxdRp_vt7W-eNsTRVuh2Kf0f2t-TWoqN7QF2c9JkIwiM9v6uiIOKXP7U6pAP5bLE4MTS6XBqbS0M4n6ynsFHjs_xA8nJSAJ-IW6fYaXfbFakShwVh5LczTtCSMLxDdGTS6RmWVkZMiYD2_k2dnEwlqBGERhGHcEI81YXADNy7OYaHfJJ-RkhttxychjXOq6Hi8xNNdWxPJEOzdjvOigpc0qOZVFBJ_McrG48mSfChmUbyagd0TKq8b6v6iwsUVNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اطفأء ابار النفط الكويتية علئ الحدود العراقية تحسبا لاحتمال هجوم قادم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/87159" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87158">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامب بشأن إيران: أعتقد أن الحرب ستنتهي قريبا جدا.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/87158" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87157">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87157" target="_blank">📅 23:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87156">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87156" target="_blank">📅 23:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87155">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قنوات العربية ؛ الحدث حاليا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87155" target="_blank">📅 23:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87154">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgGMHJEr3yhAibSObkJd4c-NUAAEmykwnrZdprRGixb4h08VDcMYnGxCxD_Rtg48OC294k2Jj7HA8EIvuNjgtyUHRA-AJMc7fuyq5dBI8XS7zEz4yor69pW3DBVgNzEB8rNNnejyf0nXHd1_PNLtzsJS30Znhnv7HyLSeNjUvwekWqeIumktGAsxrnw6NVIuNsOVL_Li2n3jGMeyvUN7XpWtuRcnM1k2dbFqO9gAtnqYI3YR2izYybV9BkSwaKk8KphQ2ckwReFS3yfINQaCQQ1ri33zKWSrR5RhS4-akV9EPibimBW_plUYLnlqncPoZbzp6An56Z6EYm3cuaxC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إلى أعزائي، أعضاء مجلس الشيوخ الجمهوريين، أصدقائي "جميعًا"، يرجى العلم أن المرشح الشيوعي الديمقراطي لمجلس الشيوخ من ولاية ميشيغان، عبد الرحمن محمد السيد، يروج، ربما باعتباره أهم نقطة لديه، إلى إلغاء نظام "الاعتراض" (Filibuster).
لقد شاهدت ذلك بالأمس، وهو يتحدث بحماس شديد عن هذا الموضوع.
إذا نجح، سيكسب الديمقراطيون 4 مقاعد في مجلس الشيوخ، و8 مقاعد في الكونجرس، والعديد من الأصوات الانتخابية والشعبية، وسيكون لديهم محكمة عليا تضم 23 قاضيًا، وسأكون، ويا للأسف، على الرغم من العمل الرائع الذي نقوم به، آخر رئيس جمهوري.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87154" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87153">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5UFH1lsvWioLnheBXOpRoHAiNzRPGEj32ZWS7XXyz5gHiGIJ7rVCtvv22ekYGGxeLTlbAIP03XIK_oLz4FlriqVyvTI4jMCKrTLeH7tKjsrpaFriWjmeEXC5kjescMNUS3jwDJOyI5LXySe9r8-3Jq5ErvFzocmHK3U0C_HzBxh_4cdp3J8PG-LyscwpclFsKCR-jnctKAf4qiZt47tgoM6ij5d1nhSz6TBLBbaZFCou7hdODd6LtR5uw7kr9mmP-Dp11Vu3_I-jvh7fXVlMXrmfA6_UfRBv1kw_00g4GJWy9mH3yEKE34WkF6eSv4hBsrsrTOeOpBUyaCDVzoiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
من جديد تعاود اسعار النفط العالمية بالارتفاع مع استمرار غلق مضيق هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87153" target="_blank">📅 23:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87152">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=s98ILs1DJsE-aXGexGNWCjR2Nfd2q3bPseHy97AbXgmRvH3Tgm50c2NCm1Xu0iQ8PkRL-ffS2kb8QuhXonsQDJpeaWbt2ZyN0vEcJp2LWnnDMsCaHcW_ZJugETazcxexeflCR3Z8HNFXPExY0B0b8zBnGBaTOki04fEclqcDWoX5rmP-nr2XTKaZ_akT_MCy7Y6H2h4gt_Nr41i3Y9X6vZCQCuGqJC4BTBKOPPYYCfiDpHUvgtdd1dDphux4sWyewyOReEXPvc7xJBSwCvNj1E1jKyHXZ5xkWQOk0IMxNkha9hx0Fi7IiaWDxAisGRrsPIX2KSd1FRip7i2BJ55l5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=s98ILs1DJsE-aXGexGNWCjR2Nfd2q3bPseHy97AbXgmRvH3Tgm50c2NCm1Xu0iQ8PkRL-ffS2kb8QuhXonsQDJpeaWbt2ZyN0vEcJp2LWnnDMsCaHcW_ZJugETazcxexeflCR3Z8HNFXPExY0B0b8zBnGBaTOki04fEclqcDWoX5rmP-nr2XTKaZ_akT_MCy7Y6H2h4gt_Nr41i3Y9X6vZCQCuGqJC4BTBKOPPYYCfiDpHUvgtdd1dDphux4sWyewyOReEXPvc7xJBSwCvNj1E1jKyHXZ5xkWQOk0IMxNkha9hx0Fi7IiaWDxAisGRrsPIX2KSd1FRip7i2BJ55l5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
الناطق الرسمي باسم القائد العام للقوات المسلحة العراقية:
لن تكون هناك فصائل مسلحة في العراق بعد 30 سبتمبر المقبل.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87152" target="_blank">📅 23:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87151">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سبب الاصوات في مضيق هرمز ناتجة عن اطلاقات من قبل حرس الثوري نحو سفن مخالفة لقوانين عبور مضيق هرمز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87151" target="_blank">📅 22:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87150">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87150" target="_blank">📅 22:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87149">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG_XNHyDl0bFgc6DPSPu69HwJTwtr-gtLizIE-N4-gkis1KKWIyyzn3PpghnYu-FlLXaFZE8thOAXOY8zm2gzK5_c4jox0huXHPDqLHVVG41gn3ySiRivE16ND4MOks_zpiDmOhYgIMclDcP0w_V3Awt2tqfjbZB7OkEpOie0KF4TQfX-5-MAVK6WH6D54AfyPgVMJSxutNNookLrqmSKnsHAD9fwaLSLSBJXp_YWWAmLRu-fSnvpLlm7poHiNmWd6enGvakHgd5YVnF6eGtyFukgIRfFDHOWz-oTCIXWfG5KK8Q-ZVSH8qf-iex8SNfyi6h1mQq3QSPROFLn1Kb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حشدُ الله… حماةُ الأرض.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/87149" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87148">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وقوع انفجارات بالقرب من مطار كابول بافغانستان.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87148" target="_blank">📅 22:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87147">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e086b316fd.mp4?token=O44GAfvm9jcLEVluuPrTDmaGCkSZ03cO4QKTIokTSXIcpnTfc67Y2otSL0lAGX-oVRw2c-joB67j3DQP1BGwqX1OrEGYdB__by3QVg__kX9Pmz8il18N6kvY3-WmiDTyg6ldx8QkCl3ihnogdIsiI8eBNmDUOUzhUQOODOzVIH7dN7KOTAaLk3qvpjyrKVJXJRVQq7XEF86M1_wzAl5Lhm5gfuRk8MVYwuP6m8oD5NfKB6gHCqXtHkambrWRf6FZb5ADQzZTIGPQoHixVcIc0xyeqnUFU3VdaMLwN9i-klnX61qbEWZ_XB2XiDFg0dvhouOtdueDOCrNchJ4QfibBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e086b316fd.mp4?token=O44GAfvm9jcLEVluuPrTDmaGCkSZ03cO4QKTIokTSXIcpnTfc67Y2otSL0lAGX-oVRw2c-joB67j3DQP1BGwqX1OrEGYdB__by3QVg__kX9Pmz8il18N6kvY3-WmiDTyg6ldx8QkCl3ihnogdIsiI8eBNmDUOUzhUQOODOzVIH7dN7KOTAaLk3qvpjyrKVJXJRVQq7XEF86M1_wzAl5Lhm5gfuRk8MVYwuP6m8oD5NfKB6gHCqXtHkambrWRf6FZb5ADQzZTIGPQoHixVcIc0xyeqnUFU3VdaMLwN9i-klnX61qbEWZ_XB2XiDFg0dvhouOtdueDOCrNchJ4QfibBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قنوات العربية ؛ الحدث حاليا</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/87147" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87146">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJgbnk0V2J_51HG5M1GqdDOVcufgyRNbj4zj2fu2702sjYXojvU8Cok-i_d8umK3oN8-_4P5wRJj_ekYuT6_8MohDUmMQ0t7yLwrhVE7qWyW0a9nKjNTykSSPcbRHKMYkOx4pmmIMou_sISweoGpoKaA2uGDwRTDhnWBSy_cLzHmVgB6GKUjWVXI-F3f9v8EH8fDbJh6YIk4xDroMRrO2xULJ8nKyW1p9D2f97LzuRVfQZqCK1iEef2TGmQdaS289Wcpea-syZLaZmC65sWr53LZTEk4IO--HAAArvwy6gK4vq8y9FyGmUq6y0V6jncdGhLaOMvAKEFMQ6ei5xo99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
:
هجوم ضخم قادم... انتظر، لا يهم، إنهم يريدون التفاوض."
‏هذا هو الدبلوماسية المسرحية في حلقة مفرغة.
‏إن استخدام التنمر والوعود الكاذبة والأخبار الكاذبة كوسيلة ضغط هو استراتيجية فاشلة.
‏اعترفوا بالحقائق والتزموا بتعهداتكم. لسنا بحاجة إلى مزيد من المسرحيات.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87146" target="_blank">📅 22:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87143">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvnQDI-XyqcxH69efcVFTg5CNwbcAp2bR3Z4lvbWd2QZRk225KiOb4mph817am6xVpF0_tNt5ax1IRQkscm49KRhzH29_F_-hy00gcxxT34nnW_s2uRtsiP5JqhTo_OBt3z8rjBvg56FGUdzgZM12Ms4VL_SnJj2UqjzfnD3GtaJ6JuIg1tmY147VWHMBvDfWmYhiWj6tLJi63rt71qo0eWiS_xocIHJoNyRv65hlg2qw6pvmdevpMH-N1ohQZKPQJKnSER0Qd0nZ0csY2PFKUCCLP_mmlWj86RYH9OPRVRY0wOeG4-IbrCwEOkD7WTxqU3NnJnSL8h4kWcff9z-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKkPrt9qphvdX59jM1ugdwiQOvSP3V_q_HIirg0ZIh3amAxzQxuIS9TOZu_ZFfwTjrzGxsHQGzETPzOkO4SfH7dM7A5ogGU7MsXDmJgymdD59HUam8AUNCZQteBKX_x45qa4m2E0hscpwpZMs-FgejBfeGurSJqPQU2LDVqFwMmIXNrIJVqodOdzIr2oGHDCWztV_-S-eArFdItajbis9XrbnKwC_qmSzVJgBQGvtxW3Mvu9eEzqqBmuki0WFqlowkDbZryCyiqbw2fKDFIR4ubs2yNOJqryGQs8bfyV4PGEDbYdEr7FZ23O0K9ra4xtILSprSfA7s2XYwabX6M6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBbm1zKKDc2KZGVgnclRI7yg5DABHxG63UpUheyp-u4XMXN7dNXRUrXxpA4zRyD72g96ghD4TwSdLkcyVr_KJg7jWK9vDV2JAAhjnW7SZeqhxip0Mv2hFO7OZKNfoGK58L2pyKJFGt0PvcgpW1bsW70FX7-5FDexvQuQ1IUROwp6Hp1STMth34O2vIr-3xSe4qROC1_ATuAEaQbQLeUwPZkCTRQIHZj5nJfSygTHnw63L8-C6RCDNj8gp0HURk7SK0JMpnCdCHsRiY8r0v6gWPggBUMPRppTB-0EIV9gp96lEhPtphmUUhbUUgpdhhmbm3Y1CwkswSrVHXuEnvQewg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار عناصر من جهاز مكافحة الارهاب بالمنطقة الخضراء وسط بغداد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/87143" target="_blank">📅 21:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87142">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87142" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87141">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXRYIeswxfRXTxWEi1cDC6YPQO2r8pMDQKZuJtqRCd65mxR6qH41cfSxPLdjaL21i887Fp1pr_ajX_qQggHMQOzv-ZuLWAnClr-sBM98b0pl-eBn1ZStEur7tv0Hi_k0aqMwSlJADFC2xHnb3Yb2-E13WiUfjSaF_Afg1S6nff7Cd4xGlB1v-ZiGr8LUUFGBZArKs6FRL-DjbP8cb3HDGKQjU89uuCPWbuB6ASgk-d4l_aan7Ubq_Dh5H-BcymzI5WCXR0-O2ZHq_pHwDhHUlHMqcSeRyZKeMUx5SA_LIefu_DaH1AFXALgNJ8zhdTWZnYSFAKd2lCs8YmSeojQ8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:  يشعر ترامب بغضبٍ شديدٍ في السرّ إزاء التقارير التي كشفت عن تقلص مخزونات الصواريخ الأمريكية، إذ يعتقد أنها تُظهر الولايات المتحدة بمظهر الضعيفة بينما تُمارس ضغوطًا على إيران للتفاوض.  ويُلقي باللوم على التسريبات - وليس على بيت هيغسيث -…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87141" target="_blank">📅 21:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87140">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يشعر ترامب بغضبٍ شديدٍ في السرّ إزاء التقارير التي كشفت عن تقلص مخزونات الصواريخ الأمريكية، إذ يعتقد أنها تُظهر الولايات المتحدة بمظهر الضعيفة بينما تُمارس ضغوطًا على إيران للتفاوض.
ويُلقي باللوم على التسريبات - وليس على بيت هيغسيث - وقد وجّه وزارة العدل لتحديد المسؤولين عنها.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87140" target="_blank">📅 21:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87139">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv3B3XO9a7VFkhUTXUvXwQn-cuSXE3EPUniC9K3o3BIXMrF77lD0UpaAg7sEmCv7AlnXiX_NtPgYOi6fBgerQC3y_neIMX1P2I4VNm7PfhaLgaWRXCnN7ICzpjT0Ons3toL3MW2T2nEHJfQ2IuMO2A5V0BkjwYfRX98n-CjkrC5H7RIWmGPaFF2PD7H9P6vpJR540Aq2RTpzZkNaqCVwLzZmWnJedgunBTtIqS5Oq3OLKrzkgKabAzAwXa6i7Nr28NaAI_l6aUuwEM_NLZ5pQLA5b7-Qviyw_lLd8RJA7Bdv1p_EVZFU32dq1-qfum0l4WZwQA8PKpXW8ZZYb4BNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في اربيل</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/87139" target="_blank">📅 21:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87138">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجارات في اربيل</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87138" target="_blank">📅 21:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87137">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K48J-9JFY1gcnhsAmeQeDDp4Cj2NHh-ymO0qxxJfMRmXYspnrQx8eehHcgewY2YRpF03hwDJ9OH36f8c-WSwCukUbahRk3P8ndVDfBpOhTZLFBy7asjsQI0QshLA6QufvzUKBQUxoRqweZ1u9iNFpHmPtPmCtGxkV73buZ8g6vYDY-okturhQav2pvU3vyjXdqoupdfKdPz3PbV2CwS9qz7UhnU3Ri8RfncCkNt8nWojFlSiHwwJMVpVgOmDGPF6yWo3Bx8F1L1ppTjbI1VetJNHai5jWSa8iwxT7yr1n_y8uOSKRlaNoDXI4KyuPy5Vha1hRp9YcPW4x_7Qla8qoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارين قرب سفينة حاولت عبور مضيق هرمز على بعد 9 أميال بحرية جنوب شرق كومزار، عمان.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87137" target="_blank">📅 21:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87136">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762fd91ecb.mp4?token=YvtJGZVqkmyyaYp92SKoQ5IbipyW7sesbD4Xk4dzAvfpgl5pGr4yqdrE4lXRLAYfewXIlZ3-XOlMrMr-RQHWHzpHM_oAqoRG6Yqu5Av6tEyncUNJdnF8gk6qugZ727j_pPjvJl2EBPfzy8TORrLYwagMMpV7IrDrJthY-2mzR3GJzw0Bs093vpj85ZoWhUw0LlaXdMAgry84N8qh3NfKJdlBWlFCeM7ZTz_3wuo9VoKLOBA2q99tR397X7qxRjJt-v2j9x27TRTMHB-XycjGf9vkCujJL2MNuT_8VVrfg3hccY2kQjEDDv_xKjfqbEdKOp0_wAhT4iVHjtEFgO0OVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762fd91ecb.mp4?token=YvtJGZVqkmyyaYp92SKoQ5IbipyW7sesbD4Xk4dzAvfpgl5pGr4yqdrE4lXRLAYfewXIlZ3-XOlMrMr-RQHWHzpHM_oAqoRG6Yqu5Av6tEyncUNJdnF8gk6qugZ727j_pPjvJl2EBPfzy8TORrLYwagMMpV7IrDrJthY-2mzR3GJzw0Bs093vpj85ZoWhUw0LlaXdMAgry84N8qh3NfKJdlBWlFCeM7ZTz_3wuo9VoKLOBA2q99tR397X7qxRjJt-v2j9x27TRTMHB-XycjGf9vkCujJL2MNuT_8VVrfg3hccY2kQjEDDv_xKjfqbEdKOp0_wAhT4iVHjtEFgO0OVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللحظات الأولية لوقوع الانفجار في مدينة جرمانا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87136" target="_blank">📅 20:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87135">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9GhQfBU3akbH8wFQWOOcQMLwaRMUsQPETKomeEsMyEiL8RgpuRf2MNbiFmtz9ank6_1prdR_5MD47Fhel5k1NlTS90MFV9TltDWyISDOJCuzaaE1XAkeKWzSCfoE_scpbPpmd3pcvWM17OibpKPjX1fKue2vlOHjl59OGbX4SuOtsT_2g4xmHL_XJAk-sNJ9ptWmYzH666m7uYITImPNR8X6rtD8xN5ZdIuqQrl_g1gkGQKWiMx6oGZZwnzn_KNe0SowaU7jnFbYwxGG38DJoWjdQwpiLIu7K4MUr4HTTE4a-0DjuA12IY7-VkgbGADUQv8OUHJmDk22L04sCr88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
صحفي عراقي ؛ قرار إنذار الزيدي للقوات الامنية خوفا من قيام الفصائل باستهداف احد دول الجوار ..</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87135" target="_blank">📅 20:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87134">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfwWWQOoq02FiECnY47LydtjLWtzDSeIIoh2IfvAPZCjSlnjt-nWCiJLekcwhrYr3YS7OepBnXWhngzou58ikvFEUxdeSarYLCtcGfXtG3gQMnxwawbwNEHtTHO-EeeFLveId8uOCwuzmHlEA1WAjeGY1BNaCRQkbscmUPIbe8aN35Y2ouWC2PRVT7OQYtElXh02IHKP3XWt8wGISmsoi-tbyZhF_Cqm8h1hhD9l0H2m2SQcwaYpeDdnvuGkx3RJ1vl34wXhoKIbvdrExZ-1xCnmGCyNpi1uA5_NPfEG7ABPdHG_nd7VblhTjeVs8MrCXit7ZaRq8gTx-D4XcQdzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
تنشر الأخبار المزيفة، كالعادة، شائعات كاذبة ولا أساس لها من الصحة تماما. أنا سعيد للغاية بالعمل الذي يقوم به بيت هيغسيث. كان كل شيء غير عادي، بما في ذلك هجومنا على فنزويلا، حيث تم تحقيق النتيجة في أقل من يوم واحد، مما سمح لنا بتقديم أحد أسوأ المجرمين في أي مكان في العالم، نيكولاس مادورو، إلى العدالة! وبالمثل، فإن إيران، حيث تم دمر البلاد لغرض عدم السماح لها بامتلاك سلاح نووي على الإطلاق، تسير على ما يرام! يحظى بيت باحترام كبير داخل الجيش، وقد حقق تحسينات هائلة، بما في ذلك التخلص من DEI، وزيادة التوظيف إلى المستويات التاريخية. بدأت هذه الشائعات من قبل واشنطن كوم بوست، واحدة من أسوأ وسائل الإعلام في العمل، على الرغم من إخبارهم بقصتهم خاطئة تماما. في الواقع، أعتقد حقا أن "تقاريرهم" المزيفة خيانة! الرئيس دونالد جي. ترامب</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87134" target="_blank">📅 20:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87133">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0dca0aa65.mp4?token=Zx7JBr4KFbqvN1OkqRDEwSMBl27w7QUe2pKv0X6tAXC0T8lAi6hJLHatCj297f9tRoGb-v8unULcOT1QqBEU3uexLhb5fqSA0zqgUU9OpWfM5-4vKh3j6J8_RuEoX3aN4IR7B6OlNcaFFy7ADexkynslQ23FDccEeNI--Vpvk-DizfDpBpU9MZ57koo8IOoL7rGQy8kZCiy-3jCa42elQCalxkTp5Vk2zfKnxx_e5-vfDzsdnGcLtEulnmgxPMsJT1NFg-ApRBMQv6y6Duh_TMM5tJZo0o47ezP6bEAVHHgqs3MO2vncSqzvHBvNWJDLjCOIhUqYOFviQJdlMwvVXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0dca0aa65.mp4?token=Zx7JBr4KFbqvN1OkqRDEwSMBl27w7QUe2pKv0X6tAXC0T8lAi6hJLHatCj297f9tRoGb-v8unULcOT1QqBEU3uexLhb5fqSA0zqgUU9OpWfM5-4vKh3j6J8_RuEoX3aN4IR7B6OlNcaFFy7ADexkynslQ23FDccEeNI--Vpvk-DizfDpBpU9MZ57koo8IOoL7rGQy8kZCiy-3jCa42elQCalxkTp5Vk2zfKnxx_e5-vfDzsdnGcLtEulnmgxPMsJT1NFg-ApRBMQv6y6Duh_TMM5tJZo0o47ezP6bEAVHHgqs3MO2vncSqzvHBvNWJDLjCOIhUqYOFviQJdlMwvVXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محيط موقع الانفجار في جرمانا</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87133" target="_blank">📅 20:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87132">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99fe71b04.mp4?token=kqQ3l_5Fw_SkItDZfqOeQ4yx6igQPAI5r75CR0l67s18Z6rAkm91MphLtByhu9ZtqA_x3jfZyMPwHtmEmIt3YpOJbqWDlczYIwSwkxsP_5F8T5svP2P1_24usLhuUmHbSgK-HajQibrhrNzdbqDKnAURpA76akCbwa_x1kMpRPvep-V1ISD0alOtteUIWJZjFDzTqNyHrwXskcUEoA7tm1c2ec77deW8Vz5Q2h8NLDshFrmpBOcQLj5I5h2YMLp05MkRl_Qd5gRrVArFCVIVn1aEIUUSkLzmeXl1gb_XDOhJtTbL3OiHnq6Gl4sYk6Ef1VRdcIZ8gChQzq4UoHy15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99fe71b04.mp4?token=kqQ3l_5Fw_SkItDZfqOeQ4yx6igQPAI5r75CR0l67s18Z6rAkm91MphLtByhu9ZtqA_x3jfZyMPwHtmEmIt3YpOJbqWDlczYIwSwkxsP_5F8T5svP2P1_24usLhuUmHbSgK-HajQibrhrNzdbqDKnAURpA76akCbwa_x1kMpRPvep-V1ISD0alOtteUIWJZjFDzTqNyHrwXskcUEoA7tm1c2ec77deW8Vz5Q2h8NLDshFrmpBOcQLj5I5h2YMLp05MkRl_Qd5gRrVArFCVIVn1aEIUUSkLzmeXl1gb_XDOhJtTbL3OiHnq6Gl4sYk6Ef1VRdcIZ8gChQzq4UoHy15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار باص مفخخ وعدد كبير من الضحايا والمصابين</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87132" target="_blank">📅 20:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87131">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaTDULB99iauzjvLh69Bhlaha_L5DzSMNjc6aRko6N98oegSVFnTHLAd7vsRG1-OlUKoPwdf1wt4tXZLjt1isyhM2YvdE-5Czx_nYvkQ_AfW40bq4AdoxmBYwar-BGVCXZW8xgkLMp8oem7EE6n-XwXUbX1HNXdMXVaHLsbdCKecIZhziM_HJ7a_MzFW6Rgs1QSbMV9t6pDv4st-dee2tUF21Hrl2bP3K8-Tve_zBu2A-Ghlws986y3RAH8qjA9_ol91QwFcW9Yy5WypPWJqkUg2pABZ8YepEEfzwf0IKGH9UM1FadjJxTqIkATTOzExCobaSGCOwCKbO65DJ5Up4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عجلة مفخخة قرب مفرق الروضة بمدينة جرمانا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/87131" target="_blank">📅 20:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87130">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPs5F4WuYUoNz9fGzzwGAIFGbGb_5NEUzvGYf1oyInEODFTPu3HwzrA6PhTF8xEjl5LN_0DeUUO2EEI_f0me0ewnWxx44sdqePLYr2abPBV6AMBmpeTNgjiY1VYPScN-L5T2NhhYAbRC440fOAmN1hWtd56FBBNwnYVlXXqs8k3X2f9iZf4usJ7OIRtY989otF1VhdRbSL-VfTqUBcvBKsxXY6DIcoisMLEBsBgUTeLGsRKPSOv7067DC57HcC15Gmef86TOWGnFzucePwlVd-R9TX-4a6lFLRwtWQHedJebJW3sRP_MPuKyxc0vI_TReD3hRpZNH7ZC5jJ4Mn2LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عجلة مفخخة قرب مفرق الروضة بمدينة جرمانا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87130" target="_blank">📅 20:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87129">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دوي انفجارات في مدينة جرمانا بالعاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87129" target="_blank">📅 20:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87128">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوي انفجارات في مدينة جرمانا بالعاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87128" target="_blank">📅 20:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87127">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
تفاصيل النص الأولي للخطة الاستراتيجية لإدارة مضيق هرمز
سليمي، عضو رئاسة مجلس الشورى الإسلامي: يخضع النص الأولي لخطة "العمل الاستراتيجي لضمان أمن مضيق هرمز والخليج الفارسي وازدهاره" للمراجعة من قبل لجنة الأمن القومي.
وبحسب هذه الخطة:
يُحظر مرور سفن تابعة للولايات المتحدة، والكيان الصهيوني، وغيرها من الدول المعادية عبر مضيق هرمز.
لا يُسمح للشحنات المتعلقة بالكيان الصهيوني، سواءً كانت عسكرية أو مدنية، بالمرور عبر هذه المنطقة.
كما يشمل الحظر السفن أو الشحنات التي تلعب دورًا في العمليات ضد جبهة المقاومة.
ولن يُسمح للدول والأفراد الذين تسببوا في أضرار لإيران بالمرور عبر مضيق هرمز والخليج الفارسي حتى يتم دفع التعويضات.
يُتوقع فرض غرامات باهظة، تصل إلى 20% من قيمة الشحنة، على المخالفين.
ستُلزم الحكومة، بالتعاون مع القوات المسلحة، بتولي مسؤولياتٍ مثل توجيه الملاحة، ومراقبة حركة السفن، وحماية أمن الخليج الفارسي وبيئته.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87127" target="_blank">📅 19:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87126">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNz9FoxrT0pi6sXVZflcALGPm9Ztrc_9lPfflF3QON0SBzuf3DuoIPjAUUYZKsl9JhfG7DjU-Ere2xfRYWps5mMIttWAKZENCBb2h1Km5eVYRNknJ-EKdOK9QFHCDC6y_hjCv0Cz1fKnpJ32_8oUPn43PXC_XjKaNM4q1Ps0uv-lvKNprLof69L1ntlAOQraXrJshLbvVOn7eOGGFoW6odClHAeP-9nnWcVqOBxN1onWMN2dZTvzc3rekW8QodX2LfgyJ63ucb57KdBZs2xrESPA7fKbyhe-64_BRo620N6su0cE-pNcvvx7jTlQi-BSjFX-KnW8eiY1kzPJQ2Vyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار عناصر من جهاز مكافحة الارهاب بالمنطقة الخضراء وسط بغداد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87126" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87125">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
🇾🇪
مرتزقة السعودية في اليمن يفرون من معسكرات العبر والوديعة الى الصحراء والخط العام بعد تدمير معسكراتهم بمسيرات وصواريخ انصار الله.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87125" target="_blank">📅 18:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87122">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQ013Xz1XlwQNdqf9lbDfrKAhcQwEQ5YVsoaa_X5upTy_UsB-KXKIq1CekCEcfLZjNor04X2fPsjiglQ-rIZzZl4SQOj_cjZyWk4-cmwYvTFu5sq9IM_YDSBftogandRh-bLxSDcwe0vZ5vZenCSx2ug_Q8Ge7oAnmcd8aurdzNxbWKh0MjRoymfR9cWE1vWIyX8QMds73ubKU7i-pIl8v4XYGYYQhR2hd_JRDKEcwuVR4EO_p6f7L-gIOA7eT5rzwz6MZWHMzEJQ1UxE44Af04ZZTwlFo0Pk1IAGikn0sUTec6OKvRxRjzE4meald0I2fh20M58zjXJCHVSS7t6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nA5xXAmgRQsP2DRzrIcEzL-k6kBINduL1m3bI2QSV0aeTInZNbmugth46pK4buuLXisvQVu0RWisFPiKCg-8IvfKJN8svN2D2p5BXrpuMqwgAKBiE0lEvs-MtjT5j2KFQohB8qso6SjdsDPo5Sku_4h0kxoUXIID98Ssu58u4mVvtf3faL7fTIDlsqHx2rpVLb5478OfIOEg-_jpDNoXS18PCNJqf4k46GbdbqmCtuFAm-4imK9Yqt-lETkDIlUeV02bHr8G5bbLbc3yNConwCpIdyNUL3HGmUPbeP1897JU_Uie1xR6aLaHgRT13L6Mcq9Qip9vyH8Ft4P_nhm_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVRaah-9O4gb1QHeYsXqj6QYSIqA6Xesfrv7NoT7AVkuiTUjuR0YO04An8Q6xQ12l5ebJU-IhPmmZWjwWQVxkRIlSvz37h0NwNWw18o_bWV2R3LFURoDY3E9tTuhdH3TwGGN8Bkh8dC5EmKkhET8gwYtTD9Y6DMlHDGQO7zS0obSvT8eieGAAFi77UpqRIN11DMGHCOlgpWtIrv371JuFsRYwF88UUlM2QjurqA6Z9_agEf7b9aW4uTik04K4vgFq0h58KSxc_RqcQlS-IQuPGvZJWRRlUEqkJFgMtZ8y5mtm5yOWHaUticotGapdNlaAAEZ5VOKIbDiL8-O7zfj3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
شرطة محافظة الانبار غربي العراق:
ضبط كدسٍ من الأسلحة كان مخبأً تحت الأرض، وإلقاء القبض على المتهمين (ا.ع.ف.ج)، و(ا.ع.ف.ج)، و(ن.م.ج.ع). وضُبط خلال العملية (5) بنادق كلاشنكوف، و(2) بندقية (RBK)، و(2) رشاشة (BKC)، و(2) بندقية (G.C) عيار (ناتو)، و(7) أشرطة عتاد (BKC)، و(500) إطلاقة (BKC)، إضافةً إلى (250) إطلاقة من عيارات مختلفة.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87122" target="_blank">📅 18:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87121">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اعلام سعودي:
80 مصابا من المرتزقة في مستشفيات مأرب وسيئون بعد هجوم انصار الله.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87121" target="_blank">📅 18:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87120">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07b8e26a8.mp4?token=Fln5hxiNDoNTYCzpGqMWCBwzv0-TrrNQGTZ59f45cgt6IocqgZO3MGcARCGMZ3D8LT5RvmVeC4Os4Z6Ren0aY6snDyFN8jnoeJZVTj3ykSGyg4GHEdlUQu80OUXb2YHrhjLa8An3B8Nykmcj7XFehg2Z2Vp3f3M9ApY37GQZIfy1on_x3TKp8gX3uiAWpOlu3d9pqpLfyChVoBrUERIs5N6uSOcxY679KTdqvmRK6-UpOkAbuqMcRO3Kgwa26qCtELcgZlldIRzVT0rDJm1Du9TvvOYKVKXufM7vcm8Zc-fBx_c95HmU5pnCSXiyMJiy--IO0AYwsOKskvi26PBlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07b8e26a8.mp4?token=Fln5hxiNDoNTYCzpGqMWCBwzv0-TrrNQGTZ59f45cgt6IocqgZO3MGcARCGMZ3D8LT5RvmVeC4Os4Z6Ren0aY6snDyFN8jnoeJZVTj3ykSGyg4GHEdlUQu80OUXb2YHrhjLa8An3B8Nykmcj7XFehg2Z2Vp3f3M9ApY37GQZIfy1on_x3TKp8gX3uiAWpOlu3d9pqpLfyChVoBrUERIs5N6uSOcxY679KTdqvmRK6-UpOkAbuqMcRO3Kgwa26qCtELcgZlldIRzVT0rDJm1Du9TvvOYKVKXufM7vcm8Zc-fBx_c95HmU5pnCSXiyMJiy--IO0AYwsOKskvi26PBlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بيان القوات المسلحة اليمنية سيكون في تمام الساعة 5:30م، بعد قليل</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87120" target="_blank">📅 18:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87119">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
مصدر لنايا:
خروج فرقة مدرعة للجيش العراقي من معسكر التاجي لجهة غير معروفة.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87119" target="_blank">📅 17:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87118">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
البنتاغون يعقد اجتماعاً طارئاً لمعالجة غضب الرئيس ترامب بشأن التقارير التي تتحدث عن نقص الذخيرة الذي يعاني منه الجيش الأمريكي.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87118" target="_blank">📅 17:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87117">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة ونوعية.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87117" target="_blank">📅 17:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87116">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇶
خلية الإعلام الامني
في العراق:
بتوجيه من السيد القائد العام للقوات المسلحة، تقرر رفع مستوى الجاهزية الأمنية والاستعداد القتالي للقوات الأمنية والعسكرية بما يتضمن تنفيذ ممارسات تدريبية وحركة للقطعات وذلك في إطار استمرار ديمومة الجاهزية العالية لجميع تشكيلات القوات الأمنية وتعزيز قدرتها على أداء واجباتها، بما يسهم في ترسيخ الأمن والاستقرار وحماية المواطنين والمصالح العامة.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87116" target="_blank">📅 17:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87115">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed2183872.mp4?token=DZhsbrzbOScuumPR1eri-muLQZCu2UwQFHFYchcQzNo8xa50RRI--fnGBz2yFlxNuajnN1uVsKRo0OZN9V27EKB_9TJCemcq1ugmbdF2r_W6DDA25hHwRzPPVAMyIAKBTqyHj5xA3AB2x0kcecRB45i6vzbZQcvD29cir8iIS1zpYAhfP86l0T7LPYebi6Y8sr_Ja3FtNC9adz3rirubJzi3uHNQjTxZJTvpcbz8L78ypn_Xdn0t8-ZsNTpHx2hGSN4dJ1nkzZ5Vea261Hyzj08TDFVqf0pFaST3NryolCuZ0SBs8Va5EEBpGUJnbyYCfnDdVEpBcaA5vZmI_lmC_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed2183872.mp4?token=DZhsbrzbOScuumPR1eri-muLQZCu2UwQFHFYchcQzNo8xa50RRI--fnGBz2yFlxNuajnN1uVsKRo0OZN9V27EKB_9TJCemcq1ugmbdF2r_W6DDA25hHwRzPPVAMyIAKBTqyHj5xA3AB2x0kcecRB45i6vzbZQcvD29cir8iIS1zpYAhfP86l0T7LPYebi6Y8sr_Ja3FtNC9adz3rirubJzi3uHNQjTxZJTvpcbz8L78ypn_Xdn0t8-ZsNTpHx2hGSN4dJ1nkzZ5Vea261Hyzj08TDFVqf0pFaST3NryolCuZ0SBs8Va5EEBpGUJnbyYCfnDdVEpBcaA5vZmI_lmC_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
وكالة فارس:
رسالة شكر من مقاتلي وحدة الصواريخ التابعة للحرس الثوري الإيراني إلى شعب العراق.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87115" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87114">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89f203653.mp4?token=CdMUfBVvH-SkWrX6AbG4yiv4rNy-Ccg3CbzZdeTfLX3tesu9FC4f1XiVcoaNF0JcSwhI6fLZZg3vmb4Rb0cRLLIfBT4XD0xVhx03LP1autVmTOZ_kZVgk_RfV3IGxWORJpz8ToXF8INZNx-wxTDzexl0-CcJ_VQzo477FaQ6FgD11p5o9Snn2uyVeZMqFZS7CW46ys7flFw1lnlqcRKYkxHqwv8n4im7z51I3cICbdrJ_0lATWFsduAyAP8ISOsYFnQkbgZGNNR5qVv-yuGJnHPQTCCtpeBhHRappLIwVDZ2Ni7_fPTFOtTjITMmaX1R7QUQgdnZDbnNv6X08qJdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89f203653.mp4?token=CdMUfBVvH-SkWrX6AbG4yiv4rNy-Ccg3CbzZdeTfLX3tesu9FC4f1XiVcoaNF0JcSwhI6fLZZg3vmb4Rb0cRLLIfBT4XD0xVhx03LP1autVmTOZ_kZVgk_RfV3IGxWORJpz8ToXF8INZNx-wxTDzexl0-CcJ_VQzo477FaQ6FgD11p5o9Snn2uyVeZMqFZS7CW46ys7flFw1lnlqcRKYkxHqwv8n4im7z51I3cICbdrJ_0lATWFsduAyAP8ISOsYFnQkbgZGNNR5qVv-yuGJnHPQTCCtpeBhHRappLIwVDZ2Ni7_fPTFOtTjITMmaX1R7QUQgdnZDbnNv6X08qJdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر يمني لنايا: مقتل عدد من الضباط السعوديين واصابة اخرين في المعسكرات التي استهدفها انصار الله.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87114" target="_blank">📅 16:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
لحظة استهداف انصار الله لمعسكرات مرتزقة السعودية في حضرموت ومأرب بالصواريخ والمسيرات مما اسفر عن اكثر من 45 قتيل كحصيلة اولية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87113" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هجوم مدفعي ومسير يشنه انصار الله على شمال الضالع استهدف مرتزقة السعودية وتسجيل عدة قتلى وجرحى في صفوفهم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87112" target="_blank">📅 16:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6675bcd19.mp4?token=IGITscJuyaoezYLInIhQudA2KfgJT0HaAtccsTKcxDiGT941OeCTuIOTs-RHiJ6FBGh0DE-lv9tzYzCNY_zFWNiQEPgJah5McZd3k-CznSbbUq8wmky27Kt5s5K0tKKPoKuOQhy60VcVpjonD94F_qEBotcGGFg1-kkiN8MgV3kukAmmCEHkTV8cUaJvCk-fI6ZhuoH_FRs4TTIGe4u8nmkPsHAgJWkgV4uDP_rWQ-51sdZBke8EzwCq_08J4bvP6DhTIYjizRtAXSqTORr98CSGHAEzilon8wHUihPdsYC3_2HfNLxmB0aU_qwEbNyXnxyOwxvInmwNQ68H1ZtpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6675bcd19.mp4?token=IGITscJuyaoezYLInIhQudA2KfgJT0HaAtccsTKcxDiGT941OeCTuIOTs-RHiJ6FBGh0DE-lv9tzYzCNY_zFWNiQEPgJah5McZd3k-CznSbbUq8wmky27Kt5s5K0tKKPoKuOQhy60VcVpjonD94F_qEBotcGGFg1-kkiN8MgV3kukAmmCEHkTV8cUaJvCk-fI6ZhuoH_FRs4TTIGe4u8nmkPsHAgJWkgV4uDP_rWQ-51sdZBke8EzwCq_08J4bvP6DhTIYjizRtAXSqTORr98CSGHAEzilon8wHUihPdsYC3_2HfNLxmB0aU_qwEbNyXnxyOwxvInmwNQ68H1ZtpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رويترز عن مصادر يمنية: 30 قتيلا على الأقل في استهداف حوثي لمواقع مرتزقة السعودية بحضرموت ومأرب</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87111" target="_blank">📅 15:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة ونوعية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87110" target="_blank">📅 15:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون 8 صواريخ بالستية باتجاه معكسرات مرتزقة الفرقة الأولى التابعة للسعودية.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87109" target="_blank">📅 15:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87108">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtbL5-QkU52XDUvM3USNFwPip5d3YVDlrgiqMlbJ3Soef1oxMnOxvD9YByAIMGP0hwe5FgQnLQBGKpGWkQQICk5tM9FQcL1saQaHglGV1ca4f7C2A-nitmzyL35AiRJzmNDCK_oKNkuRAoipzo8ZkCbE45PNlXYFjdnF6LqWoY_AjNJrh4oB0-co7H101Z7yc7beUFP2WxfkmDLwoCcxa-9y2hLJDUl44zgIHITtEVATLWW_D4aA-FFTDODA8-9JEzgTlMgcFN4Nsdn0Ec9EU9ZdHjpNet7EsjNh0pnrPeXKmnlG8lOWOkAc94kM-tlLNzY1-aMOxc4E9EJFar-wXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير النقل العراقي يوجه بإعفاء مدير الشؤون البحرية ومديرة هيئة ميناء الفاو الكبير من منصبيهما في موانئ العراق.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87108" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87107">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">في اول رد كويتي مزلزل
🇰🇼
السلطات الكويتية تلغي ترخيص المدرسة الايرانية في الكويت.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87107" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87106">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7OcZoY2mwIbDZOubfx4fXFQmVEPRvs3zwjJyWsVZ5wBk78zmQZJ2b4FZaEKQbu8mDd8iNCcxGNTWxjalXKTxc2zKGDjDK1T2qy50AdvbedrQGB1dcaXk7V3jbQgpT8O4-kWNZ4g_tJqbe1U6n2m86koD490wFeLALvustNv65r-uzB_7bzfPYVO_BraQZSYnX1jPXJkqe1UOQLOO0eAO3EVmgcqiaQjqOqRfNdkEiztdujHwTyCSB7puTYI9rEIgahNjmgFmManxf4ZQnAeKPAgwfzZL_LYsbb7VBnGjDA6yi-pwnIH3sMUP0WEvwGJ7bUDZxH-XfQummapI1Qshw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
دميتري ميدفيديف:
من العار أن يتم تذكر القصف النووي لهيروشيما وناجازاكي مؤخرًا، ولم يذكر رئيس الوزراء الياباني أو أي مسؤول ياباني آخر ولو مرة واحدة من الذي قام بذلك. اليابان هي تابع للولايات المتحدة، وفي مرحلة ما، ستصبح دولة مارقة.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87106" target="_blank">📅 14:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87105">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">السيناتور الامريكي برني ساندرز:
عندما كنت طفلاً، كانت المعركة ضد حرب فيتنام، التي قتلت 59 ألف أمريكي في الحرب، وأكثر من ذلك عندما عادوا إلى الوطن وناموا في شوارع هذا البلد. كانت تلك الحرب مبنية على كذبة.
الحرب في العراق، التي صوتت ضدها عندما كنت في الكونجرس، كانت مبنية على كذبة.
الحرب في إيران - "أوه، إيران ستمتلك سلاحًا نوويًا غدًا وستهاجم الولايات المتحدة" - مبنية على كذبة.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87105" target="_blank">📅 14:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87104">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
مديرية مخدرات محافظة الأنبار غربي العراق تُفكِّك شبكةً مكوَّنةً من 19 متهماً وتضبط 408 آلاف حبة كبتاجون</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87104" target="_blank">📅 13:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87103">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇹🇷
وزير الخارجية التركي هاكان فيدان:
بإذن الله، ستنتهي المفاوضات بين إيران وأمريكا اليوم بأخبار جيدة. يتم حاليًا مناقشة فترة مدتها 60 يومًا. إذا تم التوصل إلى اتفاق خلال هذه الفترة التي تبلغ 60 يومًا، فيمكن التوصل إلى اتفاق دائم بين الأطراف.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87103" target="_blank">📅 13:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87102">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=sjdqpHnQ_uD9VyPQx85VxhJNATiA08B47rK6lG2y4LfEzd_0yQLFRqkRlJ0eH-a-BfTCqSiffDs5nVXnBKjoiLrrez-KoDDheLrizRtsqq6R2sE7-a5_UFRWt3rsHRO6TcDehKGumWtLh-grcLaOMxKYojo6e1WqLq0kVr1N8F-vPklGxbWu4lhPOE1ZC85tGxKqEOPu_U88ktOfdoyodZuY-3S8CcMqVPwooLTHP1eCcMgX32K2jAZ579QXOGe3enk67g84NCxogz1IVQ3w0C60pVca2cgGDDIeDvv42_vUEdducSOcHoAGb2TTmEUuMUKCqE-I9n4dSaQMfDExVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=sjdqpHnQ_uD9VyPQx85VxhJNATiA08B47rK6lG2y4LfEzd_0yQLFRqkRlJ0eH-a-BfTCqSiffDs5nVXnBKjoiLrrez-KoDDheLrizRtsqq6R2sE7-a5_UFRWt3rsHRO6TcDehKGumWtLh-grcLaOMxKYojo6e1WqLq0kVr1N8F-vPklGxbWu4lhPOE1ZC85tGxKqEOPu_U88ktOfdoyodZuY-3S8CcMqVPwooLTHP1eCcMgX32K2jAZ579QXOGe3enk67g84NCxogz1IVQ3w0C60pVca2cgGDDIeDvv42_vUEdducSOcHoAGb2TTmEUuMUKCqE-I9n4dSaQMfDExVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون 8 صواريخ بالستية باتجاه معكسرات مرتزقة الفرقة الأولى التابعة للسعودية.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87102" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87101">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇸🇾
صحيفة لبنانية: الجولاني لا يريد دخول قوات سوريا إلى لبنان بشكل منفرد ويرى أن أي وجود عسكري أو أمني يجب أن يأتي ضمن إطار عربي  وجود طرف سوري منفرد في لبنان قد يعيد إلى الأذهان مرحلة الوجود السوري السابق، وهو أمر قد يواجه رفضاً من أطراف لبنانية ودولية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87101" target="_blank">📅 12:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87100">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇸🇾
صحيفة لبنانية: الجولاني لا يريد دخول قوات سوريا إلى لبنان بشكل منفرد ويرى أن أي وجود عسكري أو أمني يجب أن يأتي ضمن إطار عربي
وجود طرف سوري منفرد في لبنان قد يعيد إلى الأذهان مرحلة الوجود السوري السابق، وهو أمر قد يواجه رفضاً من أطراف لبنانية ودولية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87100" target="_blank">📅 12:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87098">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇰🇵
🇯🇵
توجيهات صادرة عن مكتب الدفاع الياباني للتعامل مع حادثة إطلاق صاروخ باليستي مشتبه به من قبل جمهورية كوريا الديمقراطية الشعبية</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87098" target="_blank">📅 12:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87097">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXjysYNPzI30jVTRsPSD6A0UJDIxtQdAts4BlYcjTBFSN00f_OC9IA6_7wusQmK5Vv5GnTJUmnxf55PpHPAFWrk69b0vxem_F84zu9T3wo2ymu9IH25cENw2wi4OlYrrzcgnaC3923m6hK5UvHXYYuRmxoaOEnC6oOy7PA4FBMIkz5W_o2lMawCldChHPSZgO9_xderXSDKFLPJ8oZa2KXjBqGcQJzCKVEx3XeiBwigbewj8KJ5xCpC1oWkSt3cVf7x-3YOSnYFin11xx8w_GrfYoITpEs1EP8cYAI9HjM2pGAyltNmhaDTtbvQJiXkI2baaUlgftKfPMdQi3bRLBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇵
🇯🇵
توجيهات صادرة عن مكتب الدفاع الياباني للتعامل مع حادثة إطلاق صاروخ باليستي مشتبه به من قبل جمهورية كوريا الديمقراطية الشعبية</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87097" target="_blank">📅 12:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87096">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">إعلام خليجي:  تفاهم بين طهران ومسقط على الخطوط العريضة لإعادة فتح هرمز.  اتفاق فتح هرمز لا يزال بحاجة لموافقة المجلس الأعلى للأمن القومي الإيراني  الإعلان عن اتفاق إعادة فتح مضيق هرمز قد يتم خلال أيام  السفن الداخلة إلى هرمز ستستخدم الممر الملاحي الأقرب إلى…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87096" target="_blank">📅 12:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87095">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">إعلام خليجي:
تفاهم بين طهران ومسقط على الخطوط العريضة لإعادة فتح هرمز.
اتفاق فتح هرمز لا يزال بحاجة لموافقة المجلس الأعلى للأمن القومي الإيراني
الإعلان عن اتفاق إعادة فتح مضيق هرمز قد يتم خلال أيام
السفن الداخلة إلى هرمز ستستخدم الممر الملاحي الأقرب إلى إيران
‏السفن المغادرة من هرمز ستستخدم الممر الملاحي الأقرب إلى عُمان
‏أطراف إقليمية قد تشارك في إزالة الألغام والإجراءات الفنية اللازمة</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87095" target="_blank">📅 12:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87094">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇱
🇺🇸
أمريكا تبدأ بإخلاء عدد من طائرات التزود بالوقود من مطار "بن غوريون" في الكيان المحتل.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87094" target="_blank">📅 11:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87093">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇱
إعلام العدو: حزب الله يحاول خوض حرب عصابات على الأرض و"الجيش" الإسرائيلي تصرف يوم الأربعاء ببطء وارتباك</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87093" target="_blank">📅 11:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87091">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_cJluozQKZpIOrr3guUG0cb--qRY11SLA8TXhW5iHxdO2WRJcLm6_fGMfuZgLjTX958hSHfh-YY-bNwbyx-Z9lYvxnbkrXmgQHCaQia1RfEVY2dl2piOjGFlkGseKd8UCyv_UoThs2IoGtW-6JkcnnlUeXtTHvIdz1D4sNleWC-3AJtlp_RQT9V4RkhW36yKpgSFOWUHnSCgxyE5TI613F_vp0TpLr8s06lZBZVqAST0mkPX9aII_NlpXAxH5Qw7dgIQZGzZeHeQK3jLUh5Uq-2M_KsSsvbCb88NErAyraAl6lpEAa4zi-3Ol5okM1P7Eu2ij0C5AN07wX96-mF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZgt-rHiZsydya0LYsEtIu0F8Z9i0wh32IXcWmKvreIyUCEZzgIKBlrZhn5OBA8BpKvnSosJIcwdEULVhCzS3OaCbBLkKszJwHvUMstgiaEsIMriiwrSYk_x0OWBSy3oBvA44YW5P4E58XqJNe5Mtqa-Lfv-iODMBYAC3GI2qEWQhLkGNsJQVCKG89Qhkjxt1dc4I_Jws_R8iNjXfWCnN9RVNOIAXxrapxqiFYg-MKtmzHl3NyJ2mKsY-F9NBDZRcg1Qg84PA8vrZMjd38UlQsGyQoNVPy3BHDHkAcySY52L2pT1ZF4ELXzeYgHsEbzTTW6bCDnGKI7p4CLaEr0pww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد أخرى من انطلاق الصواريخ اليمنية نحو أهدافها</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87091" target="_blank">📅 11:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87090">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNz0R1NF5eVe4U_DoD4q7-7AUhQkZ9iY3Th1GqCMfZ6PU8NWsOlyQc-zjPBvtCyegUwPR6_b3Qi8IDDY2UGtz4sFUkClYSEi654CDgj7jTIIS88iGU1ds_FA45UWmUvg5eeQ6d7gCjxdWuiBZgDU18EeoqRLHVwyqBFa4DPPMUnro4kqeZZVlZM3H-D2vhm4ntShPm-BJRF1FkgGEt9fguE6UY6RUCHvokNr9SQt0nZVyKXqQgY0voTl9RkbnE9wUhFD6vjFFgCNMbwoSoBIqpj2mAf_vGD1SA8NwIRaN8sxFLssD5HyYt0F5u2KoshR-Ocgv0BlfoOY3cg4HAy-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري جنوب شرق كومزار في عمان.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87090" target="_blank">📅 11:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87089">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حدث بحري جنوب شرق كومزار في عمان.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87089" target="_blank">📅 11:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZA8-F9c8lS5I0-rqIixPdeNp27NCXPdmtGVMKealBgAnUq9PWn0S-t2UIDPaQ0plJLrxNmfLjflTuxgcWv6WLHRXHbgKX1fjkmqt2t6BjPkUWS4oiQqdOMtJ_G2yzXtS98UxhYuuFwTKhJCcqnBwekGifsJtxKbMxAa3f_by8ys1Zpm1Pa9e_rSOqN0UlfEE0wxpzV79lFtYHn2QdI_JJ9psI2ahg1QPkbiLnK46si2kaW0Vp_mBzRkb55goUN2sdLMijo3qMhhweHqgCKA0JmJLaPpWzvj3JApsYYS3aOJg_AIg1yaGcGaxFU3ahWAIRTpZ4QZv2a55Jutq6kpsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oycabtlM-7j2okk-LAhaeA-oBA-zgJLZCKuL0ki4gH0RYP03G99dldxes7ZpCHpJwHd8gP3KrlutyAt75lofEozhNbEJy4GwC6Vba1HSVJKZPEJ8poiblx_eRiXAjaNffYvk03wSm221a7-1VziUyXzKDIzqLQDm63cjOs522Gu-AG8SuG7rJD99eFY2uof5aMmV9sazz5trxZ3dIiRrEkpCqe_SWFjsEqdZXjO3VWOrChjyjn1O9g6jraqJlsldP89bKAhT_wN86hRVw-Mi9rZUn_YOGtpu4_C_V0CchMX7wLI8obGVFfIumYbqFTsorhSL07szUCXrWxVP_4HNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AFP5F5XAwf9Q1BDLgIcbgvimbx-eS8_-g683ugdbGoD0fVc-MK-knDDrr1N-tyPLGuAlxRQ7B5sUVXgMEy_5fqrtVxhGriT3GboKjOG4iekNo7932eyBtOiBIozVyPjkVspiF-49PMTY4T-M90LOxU62X80qkMH3biB1t31ETpzAn7AT1bKloCKNFunjlcOHWaOg8JF8fTgOUyzMPMpkE7pB78gKG1-JzgARDUfnASURKMZVnGtUks4U-g5TXGRrD4uGySnsRcOzIeTU_gVapniDxZiAKIcxjGCBe1PSmCU3cqDbS1yhGiBtnnTR2I8puy9uLXm9z4nitnaQkTYKIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">إطلاق صاروخي من اليمن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87086" target="_blank">📅 11:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">إطلاق صاروخي من اليمن</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/87085" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87084" target="_blank">📅 11:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
وزارة العدل العراقية تعلن كسب دعوى قضائية أمام المحاكم الأردنية لصالح شركة أدوية وتسديد مبالغ مالية إلى الشركة.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87083" target="_blank">📅 10:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇵🇰
المتحدث باسم الخارجية الباكستانية: لا نزال منخرطين مع الدول الأخرى بشأن الأزمة في الشرق الأوسط والوضع في هرمز</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87082" target="_blank">📅 10:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏ترامب: نقوم ببناء أكبر عدد من مصانع الذخائر في تاريخ الولايات المتحدة
‏سنصدر أحكاما بالسجن بحق مسربي التصريحات "الخائنة"</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87081" target="_blank">📅 08:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇱
حدث أمني في حي بارك تساميريت بتل أبيب</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87080" target="_blank">📅 07:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇱
حدث أمني في حي بارك تساميريت بتل أبيب</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87079" target="_blank">📅 07:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb71ce607.mp4?token=BHjOsO-FXy1M9FrkV9ArxDlnl4pVOr6057Ep9tud-ul3B5ZJJFOgfcMp40aY04S7iD-BFo7OoFi7Gh81VWizEO9pzobe6-WagEtouvuHxiQ7WrYW9b69M6TKAFQUXiIR6m-wBYuRUuwCqGQFh8J39VvwuCJ8Ukd0aHWqcZ8ai2g9A-qVo00Ounx80CQRLyj0QLVqJ7bQkcHQYTTeYw6G9vk99eWioOdWdajIjj5Wn9WIlbmXjDJDDdFOzQ8L_OGFwNyKaagkdpxDW-FYfjj3lommGycEUGw9LxK37UG9NSmNK4yXKzEXraDw-fn9slT8m1K4mEVxC5_qY2716KXX5rDReQQhIKzo469nnB4H1-GfiYsCvNfIXFJRd8VP-fgR-FXY22K9FYpamvc4xz7h2NA5_O_oJRKeefHbPmOWd1ocNfnlgAlHtfkpjpAw5SnXmlW4F0Krod6W9YS1Gz5WjMxSBO4E3OFTQ8UlFOE-nMdJ5PD2jwXA6MVJZNBw1yFJvBOcs8ojibewkMqkOldYU68CjPMnGtVi6n0YkGrTGvsiHa6ENSuTrP2GmFCmHAmdVeYku0B0tKEb0D0KtY7nyrXyY4uzQolnPlrvMENLrEetEKn2-9Avc2KrFpT8ZeYGyvVT1v_pqWyhW7ZqAhLuWCimH9_zCrS6lnM9AVe4Ifw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb71ce607.mp4?token=BHjOsO-FXy1M9FrkV9ArxDlnl4pVOr6057Ep9tud-ul3B5ZJJFOgfcMp40aY04S7iD-BFo7OoFi7Gh81VWizEO9pzobe6-WagEtouvuHxiQ7WrYW9b69M6TKAFQUXiIR6m-wBYuRUuwCqGQFh8J39VvwuCJ8Ukd0aHWqcZ8ai2g9A-qVo00Ounx80CQRLyj0QLVqJ7bQkcHQYTTeYw6G9vk99eWioOdWdajIjj5Wn9WIlbmXjDJDDdFOzQ8L_OGFwNyKaagkdpxDW-FYfjj3lommGycEUGw9LxK37UG9NSmNK4yXKzEXraDw-fn9slT8m1K4mEVxC5_qY2716KXX5rDReQQhIKzo469nnB4H1-GfiYsCvNfIXFJRd8VP-fgR-FXY22K9FYpamvc4xz7h2NA5_O_oJRKeefHbPmOWd1ocNfnlgAlHtfkpjpAw5SnXmlW4F0Krod6W9YS1Gz5WjMxSBO4E3OFTQ8UlFOE-nMdJ5PD2jwXA6MVJZNBw1yFJvBOcs8ojibewkMqkOldYU68CjPMnGtVi6n0YkGrTGvsiHa6ENSuTrP2GmFCmHAmdVeYku0B0tKEb0D0KtY7nyrXyY4uzQolnPlrvMENLrEetEKn2-9Avc2KrFpT8ZeYGyvVT1v_pqWyhW7ZqAhLuWCimH9_zCrS6lnM9AVe4Ifw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇪
رصدت الأقمار الصناعية آثار اسوداد وحريق واسع في منطقة جبل علي عقب انفجارات متتالية شهدتها دبي منذ يومين ؛ حيث أرجعت السلطات الرسمية الحادث لـ "حريق صناعي" وسط تكهنات مستمرة حول الأسباب الحقيقية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87078" target="_blank">📅 07:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d964adb32.mp4?token=a1L56RXfUqyDoWjVNLi9_4dmAOol8-pIC89yz8BDbULt8vH5KDCG7L_e5a3Ff7F1U7teOzXvy3oaf60uH8gf0-F7mKnsMgVMVmpruTMyBpWm5F79XFqbXdwepFZm2C4SyZrM2LAYuz9i4yI13LeoiFYbGt0QiCw3VJZStAIol2en5uELr5RiWP2jXqCAL6gqHgyZnRzZczICmMOA8GCcTMD8_XjFO13cCK6fNuFUp_uAR1bzTIbe2ylcuQDQDNbNLlazwMIRM0O4dXYE288MWeaNpbF6vH8Z7rAZ2hpoUoN7RGSy1-CWlv4LKMc5tnqpsapV2HqEA-C2rUtjpnTvWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d964adb32.mp4?token=a1L56RXfUqyDoWjVNLi9_4dmAOol8-pIC89yz8BDbULt8vH5KDCG7L_e5a3Ff7F1U7teOzXvy3oaf60uH8gf0-F7mKnsMgVMVmpruTMyBpWm5F79XFqbXdwepFZm2C4SyZrM2LAYuz9i4yI13LeoiFYbGt0QiCw3VJZStAIol2en5uELr5RiWP2jXqCAL6gqHgyZnRzZczICmMOA8GCcTMD8_XjFO13cCK6fNuFUp_uAR1bzTIbe2ylcuQDQDNbNLlazwMIRM0O4dXYE288MWeaNpbF6vH8Z7rAZ2hpoUoN7RGSy1-CWlv4LKMc5tnqpsapV2HqEA-C2rUtjpnTvWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: "سعر النفط هو 75 دولارًا. قد نضطر إلى رفعه مرة أخرى. أنتم تعرفون ما الذي يحدث عندما نرفع السعر."</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87077" target="_blank">📅 04:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKzUpQJvhn39zaykDpc6tJxVVwlzquMNzuPG-mbsF3DrDwkyo_BagHuoAUAvUQs6eCbo-295Hz02qS8odUIF3kMdf26v04rekwmO1OOK9doxLvuHV1Wz0KReKkFbHft5yWPlMlzwrYqMkYyOzEA58CEkQ13XVno3DwfAWqnBJJVGqxPlGAAs3R2hp0GKLWCGIaD_N_x9QAPf-F_pBzEbAz4vF35MQmIAlhn3jOtuID-zFiLdBD5_Hg8IgluefJYMdMyadiQiR2n3RYtAbrCGcsts6iTLjCX7yLmndZAgLIBMzB_ZoKKpZaeCIaJPMSfdGs9mNvk3wPOfSib0aKEfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
صور الأقمار الصناعية تظهر اندلاع حريق داخل سفينة بالقرب من مضيق هرمز.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87076" target="_blank">📅 04:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQn1f2KULq7u2fEdh6KikGaOHMnRfWkZSHBoVHq2wxxgzqcEUkGlvxl2kyTCyYSxwlb7io9TRyM_2rZcuBO2XG0sitXxwGZxvm3E1mDjQ0x8ZrWN4b9OUDtym8ts-BKhylODQxneSpgOz2u_kTNNmIzkY30NJkbcneaPMHWaJNzNGjpcLkJ0ATC2fhCoE3INQuhPmVTM15KJ42hpv1ICcoyWUmuJ5tRW0_hj4OwTmfe3jD-BDeZ0Cm2VGkMFGNUgtlWc9gEm5kiH-_nJ0u4h_aqdjA5eHURi4WqXSrCqA29bRrL3AzVZaRtrwgiC-gLC7YGFfWij8UyBHNIGL7nabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
كان مايكل مور، "المحلل" السياسي الفاشل الذي يخسر أمامي منذ سنوات، يصرخ قائلاً: "لقد خسرنا في عام 2024، ولم نعد نطيق ذلك". كلا يا مايكل، فقط تعوّد على المزيد من الخسارة! لقد كنت خاسرًا طوال حياتك، ولن يتغير شيء
لن يتمكن عبدول، رفيقك الشيوعي الجديد، من إنقاذك. إنه يعلم أنك شخص فاشل وحقير، ويريد أن يكمل من حيث توقفت. على مدى آلاف السنين، لم ينجح مفهوم السياسات الشيوعية قط، ولن ينجح الآن، خاصة في ظل النجاح التحويلي الهائل الذي حققته إدارة ترامب، ليراه العالم أجمع ويتبعه: أفضل الأرقام الاقتصادية على الإطلاق، وأفضل أرقام التجارة، وأفضل أرقام الصادرات، وأكبر استثمار في بلدنا، والقائمة تطول. هذا هو العصر الذهبي لأمريكا، ولن تتمكن مجموعة صغيرة من المنبوذين، مثلك يا عبدول وغيرك، من تدميره وتغيير مجرى التاريخ. إنه أكبر من أن يُدمر، وأقوى من أن يُدمر، وأفضل من أن يُدمر. نراكم في ساحة المعركة السياسية. لنجعل أمريكا عظيمة مرة أخرى!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87075" target="_blank">📅 04:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">استهداف سفينة قبالة عمان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87074" target="_blank">📅 03:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/87073" target="_blank">📅 03:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87072" target="_blank">📅 03:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
استياء ترامب من وزير دفاعه تزايد لأن هيغسيث كان من أبرز المؤيدين للعمل العسكري ضد إيران.
هيغسيث أقنع ترامب بأن العمل العسكري ضد إيران سيكون بمثابة انتصار سريع وسهل نسبيا.
هيغسيث دافع عن نفسه أمام ترمب بشأن النقص الحاد في مخزون الأسلحة وألقى باللوم على نائبه.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87071" target="_blank">📅 03:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87070">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇺🇸
نائب الرئيس الأمريكي:
هناك أشخاص في النظام الإيراني يريدون إنهاء الحرب وهناك متطرفون يريدون استمرارها.
الإيرانيون عسيرو المراس والنظام متصدع ومهمتنا تحقيق أفضل النتائج الشعب الأمريكي.
سنستخدم كل الأدوات العسكرية والاقتصادية والدبلوماسية من أجل التوصل لحل مناسب مع إيران.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/87070" target="_blank">📅 03:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87069">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇦
🇷🇺
الإعلام الأوكراني:
هجوم روسي بالصواريخ البالستية يستهدف العاصمة كييف.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/87069" target="_blank">📅 02:06 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
