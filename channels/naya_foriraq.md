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
<img src="https://cdn4.telesco.pe/file/P7nTMMYZW1uopl_LxhZtKZgHZpDaQ6rLs8PMneULNQ5ZkNWAMBJyePT2jv6Vx8xuFN3xTdc98P-GWwnWwmCzS2CugbgpEVkt9CUztCa0AWA1SooBI96HMX2MwS4I3WxHzuHkAUeas98vWhLiyHEb5GQAk4PMNF4QHQTU62TEerC53U_9sJq3rD0CbGgbYdUQ0VjjeDs9r_5qMF-wLKnk1SxVl-TAC0zBdVToHklHNpmuZauCXT63mQa0f0uZjx4ipF90BOtzxgDQ_zW1boo2ZVPPbCSXMT9IIC6gq_srQWqmx_nsvhpW-w0yxTvKHv9-Okdbtp6ppLRfsGeqH7-nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 18:07:48</div>
<hr>

<div class="tg-post" id="msg-80828">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=hoo9hUzueq5xxRQa0SgEL0_hQ_rx6hi8kLJCE3ws-oe_6ZrMnjKRAmCpvRvRq-66lyp3ZhM3jAD71UIXH8fArmxi0gNTtwoKkZiHXTtQjKnET36jMOxtkQD_reN3ln8OUImtS2wDQl_CiX-upWWVmXISvjnSQz6CmuGvuDn0aAbh_qdjHsWC2xqwPCslMBCfdOh6-YTltC1b3p1shd7H8DlbYwDl0FwQllWhicp8Dj6WB0eoYyeorMNe5HuCOMqsG9kTP0Q76Rw-W5CjxLqHyio_JBBTIjZ0UOGgtKBy3OL1SjroQ3DRZEpXbusAWS0M5rMvbU9_-OH8cQvJAlD1Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7bbd75691.mp4?token=hoo9hUzueq5xxRQa0SgEL0_hQ_rx6hi8kLJCE3ws-oe_6ZrMnjKRAmCpvRvRq-66lyp3ZhM3jAD71UIXH8fArmxi0gNTtwoKkZiHXTtQjKnET36jMOxtkQD_reN3ln8OUImtS2wDQl_CiX-upWWVmXISvjnSQz6CmuGvuDn0aAbh_qdjHsWC2xqwPCslMBCfdOh6-YTltC1b3p1shd7H8DlbYwDl0FwQllWhicp8Dj6WB0eoYyeorMNe5HuCOMqsG9kTP0Q76Rw-W5CjxLqHyio_JBBTIjZ0UOGgtKBy3OL1SjroQ3DRZEpXbusAWS0M5rMvbU9_-OH8cQvJAlD1Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الهندي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/naya_foriraq/80828" target="_blank">📅 17:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80827">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=Neahk8GmPFHdL_RCsXWvMdbDpyB7nL6sfX71-pWOwM07Wz1T3uicw6vfgmN4POKwpcF6LjSka5qQ8K7FGzNi7sR5Md-DtXJ4sLLa7eDVPyrT_HKHjcejDwSqmJN99eG-pqFd28FwNvp-XW7N8jhVE9cg9Gvy6m_WtqHmliA90nMlZCHdprRFPK3lRCs-tb38hEJCOw9LvPUHGf97EAg2tAwprUWuh2u15vn_m6LUlX-e0FdgTpbUAcfDBIiME87N_JrQNgrg8gJdLqvnzuvUMoLh3FYSxXyic7Sc3gO1wCkMHiNIKBxwqqZW3gEYPYAHoq0cO1QGeTkMlN7QG0THYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb7b7d98a.mp4?token=Neahk8GmPFHdL_RCsXWvMdbDpyB7nL6sfX71-pWOwM07Wz1T3uicw6vfgmN4POKwpcF6LjSka5qQ8K7FGzNi7sR5Md-DtXJ4sLLa7eDVPyrT_HKHjcejDwSqmJN99eG-pqFd28FwNvp-XW7N8jhVE9cg9Gvy6m_WtqHmliA90nMlZCHdprRFPK3lRCs-tb38hEJCOw9LvPUHGf97EAg2tAwprUWuh2u15vn_m6LUlX-e0FdgTpbUAcfDBIiME87N_JrQNgrg8gJdLqvnzuvUMoLh3FYSxXyic7Sc3gO1wCkMHiNIKBxwqqZW3gEYPYAHoq0cO1QGeTkMlN7QG0THYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد التونسي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/naya_foriraq/80827" target="_blank">📅 17:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80826">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية عند الـ6:00 مساء بعد قليل
.</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/naya_foriraq/80826" target="_blank">📅 17:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80825">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=mE0jLJqlsmjEmDVHTiuKQbLDl2ZfKRIfp0fJDg7TpwIzb-U3JuwsZSx9ma3kWTCJv6ZZXHZG_uTJTrU-gZqiTY4l35Q-pGacmibHNf92L4pZsUBsKtw08WTuL1cEdj_Y-ePKeex7XZv0zl8eMm8tQp1Btsh57SuF2CeLBvf_38Xq-IiXZPO6n2EhvUSwVI0sJU8nbwQJDOyYjzTGAgscNTAAfm9GkWoNQyZD924c_d1LjCyUBxqS2gJCKyUtlpgnglYfKAfV4sLGkzh7HUPMTnMOfINYEPLrHU-UrKe9A4Qg2D2-x70oi7JjcKH2811r5GNHV38EScRZrlJ8HF3NVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299dd37dc4.mp4?token=mE0jLJqlsmjEmDVHTiuKQbLDl2ZfKRIfp0fJDg7TpwIzb-U3JuwsZSx9ma3kWTCJv6ZZXHZG_uTJTrU-gZqiTY4l35Q-pGacmibHNf92L4pZsUBsKtw08WTuL1cEdj_Y-ePKeex7XZv0zl8eMm8tQp1Btsh57SuF2CeLBvf_38Xq-IiXZPO6n2EhvUSwVI0sJU8nbwQJDOyYjzTGAgscNTAAfm9GkWoNQyZD924c_d1LjCyUBxqS2gJCKyUtlpgnglYfKAfV4sLGkzh7HUPMTnMOfINYEPLrHU-UrKe9A4Qg2D2-x70oi7JjcKH2811r5GNHV38EScRZrlJ8HF3NVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الماليزي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/naya_foriraq/80825" target="_blank">📅 17:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80824">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=QEHN3N6ZeYqZq98YuGRUbBRy5SYb6Ubz9lfhDrMMy-ZY0t5XfK7xRiOKNoWR3bHCzd2V438364OXuaC88TeUJx99TlYrFQtzVhEQ1K1OiJApcI4l-mDciYXlLd46FGYo6UoCaGYPE9lAQIdZubNQIfBC3Xeu9pvSFN-KkjTBSPQFZMx0ltdo7yZAptRI8k5QnAdgNyCH_qUqBcmhAXD5jhhliEHwigW51Z8CXP5mLeTgC0BAKBfuzR42pT0qXtPPc_bKLr3TvmSmrKyjpKpaCPJzCW8X4E5fxLWwf2w6-_aTGhX2g8VQL6qg7m99nr0HvqdHcHaAIBKLI1knrTqbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ce8fafd3.mp4?token=QEHN3N6ZeYqZq98YuGRUbBRy5SYb6Ubz9lfhDrMMy-ZY0t5XfK7xRiOKNoWR3bHCzd2V438364OXuaC88TeUJx99TlYrFQtzVhEQ1K1OiJApcI4l-mDciYXlLd46FGYo6UoCaGYPE9lAQIdZubNQIfBC3Xeu9pvSFN-KkjTBSPQFZMx0ltdo7yZAptRI8k5QnAdgNyCH_qUqBcmhAXD5jhhliEHwigW51Z8CXP5mLeTgC0BAKBfuzR42pT0qXtPPc_bKLr3TvmSmrKyjpKpaCPJzCW8X4E5fxLWwf2w6-_aTGhX2g8VQL6qg7m99nr0HvqdHcHaAIBKLI1knrTqbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الصيني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/naya_foriraq/80824" target="_blank">📅 17:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80823">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c6119361.mp4?token=qh70bulOEQ9_ISFD_IIWbRkBmvt7euszhVdEROX6Vl6uQLT-MhHmnMjO5awtShSQJ8v4mNUmem-kjsgVUg-JTaQz3wnYipMcTYS4HqqGgJGITmhtsgdBcNhBEp8KnGG-JiMH_pUInhX06kGl-zXf1JSg4fMIimEGEFju3bxCxHtambDLeMrhRRk6Z75w9DYbkUlDUxBSKbwF2jUdh42EAJZkFcYZ5JIzfVvclw31iDgWuy8xZ05FBRsmS9zDuK54YptOLiI-DGeHopgHDOFoemGDC4-G5gVDYM9jyYCKjA-rO_K_dNE7-mHe9_Mf1NRVUN71EodstfGOPM_ipM4N8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c6119361.mp4?token=qh70bulOEQ9_ISFD_IIWbRkBmvt7euszhVdEROX6Vl6uQLT-MhHmnMjO5awtShSQJ8v4mNUmem-kjsgVUg-JTaQz3wnYipMcTYS4HqqGgJGITmhtsgdBcNhBEp8KnGG-JiMH_pUInhX06kGl-zXf1JSg4fMIimEGEFju3bxCxHtambDLeMrhRRk6Z75w9DYbkUlDUxBSKbwF2jUdh42EAJZkFcYZ5JIzfVvclw31iDgWuy8xZ05FBRsmS9zDuK54YptOLiI-DGeHopgHDOFoemGDC4-G5gVDYM9jyYCKjA-rO_K_dNE7-mHe9_Mf1NRVUN71EodstfGOPM_ipM4N8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الامين العام لمنظمة B-4 الدولية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/naya_foriraq/80823" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80822">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=MdCz2pgbYwQRpRzQlZsQMrrEukFFFjnQAB9aVCwTQJ2GqtlvBQZDLkwxxNhNQS1EeygbUWp_5O9yxOt1PIfMkLB99Kdl3UKNWR9g3LntSV7Xc5d8IrXtdLVmEhUf34t9_VSovnWI8xuwh128frZt-FKpfK2dd2eV-n2uJXow_erAPq6gTLsAzkylPkrrq8DSyz-grTSIj79OmxzUHkwbialCJZrq-d2KxBasa13qOc-V8nDazIqYgFgBAeWXCxsDnbohXauxXCZapSJ2i8w0B9s2pEVUsXC2PX4XR-erXvbqKpNgmc_XTbWIjRzYuqBg9TkmqJsyAG80dKuMM0llgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86a1ad1097.mp4?token=MdCz2pgbYwQRpRzQlZsQMrrEukFFFjnQAB9aVCwTQJ2GqtlvBQZDLkwxxNhNQS1EeygbUWp_5O9yxOt1PIfMkLB99Kdl3UKNWR9g3LntSV7Xc5d8IrXtdLVmEhUf34t9_VSovnWI8xuwh128frZt-FKpfK2dd2eV-n2uJXow_erAPq6gTLsAzkylPkrrq8DSyz-grTSIj79OmxzUHkwbialCJZrq-d2KxBasa13qOc-V8nDazIqYgFgBAeWXCxsDnbohXauxXCZapSJ2i8w0B9s2pEVUsXC2PX4XR-erXvbqKpNgmc_XTbWIjRzYuqBg9TkmqJsyAG80dKuMM0llgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مبعوث منظمة التعاون الإسلامية يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/naya_foriraq/80822" target="_blank">📅 17:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80821">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979449faf7.mp4?token=fNUx9zdLQ7t4-ugnCoVsL7dzkdHJPAYxY0rRYZbYXaJe6g_kK7c9cAdZiUPLIRH2wXHHxph4nfTaWykI9qOCbmQJaN49i2tp_zrokoagslFs4Q_fm4oU7tFOxtyM4qXUG1EobMFNAWZKCcMfXuOnHbyJriYsG6Dj605UV81Gw7Ccs_o5YvH2c_E9WkNlJ4JNnRKAqXjMq6Pn5bfHkhMnr-rTc_AN1ACLhso7YpHubOs9kNH_4h9b7fMx7KnKf3Sa-3fkgBIsMTxytq-jfLLyMhYEUoKdrK_7Kz4oHWFD09xx0HreDwiIh9Zm2oT5-pa-X2PuYi4CT4mjycCfZWBYHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979449faf7.mp4?token=fNUx9zdLQ7t4-ugnCoVsL7dzkdHJPAYxY0rRYZbYXaJe6g_kK7c9cAdZiUPLIRH2wXHHxph4nfTaWykI9qOCbmQJaN49i2tp_zrokoagslFs4Q_fm4oU7tFOxtyM4qXUG1EobMFNAWZKCcMfXuOnHbyJriYsG6Dj605UV81Gw7Ccs_o5YvH2c_E9WkNlJ4JNnRKAqXjMq6Pn5bfHkhMnr-rTc_AN1ACLhso7YpHubOs9kNH_4h9b7fMx7KnKf3Sa-3fkgBIsMTxytq-jfLLyMhYEUoKdrK_7Kz4oHWFD09xx0HreDwiIh9Zm2oT5-pa-X2PuYi4CT4mjycCfZWBYHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لمنظمة التعاون الاقتصادي D-8 يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/naya_foriraq/80821" target="_blank">📅 17:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80820">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=HUSg-bLIxXUYCrPgSySd8-GbylNDRP3G9wKhY4bG9if8oq4_7OK61Uf3y5-Bq9MtVnDQUsqMDbcxqKF40bQLS5SsmlJEQA5RG8Ohp2B2pLY_-BcDSjOLHvizSjH8W5guy9E4kZgrX08b_lfKE26Asstd1tHauuDZ-dCIxbGi1yPo3OLZy3gH5N7UNxkWF7W1PIx-MqVjLe10ldaZwv3I-zaF8cgZiG1Oo4F618Zs7lIC7ARli8ZFQrh70vkoNravnuFE9myDa6MBLjvP4RCrtleP96nI-rWFUErkWNcFHxc2VnS6w5ghxBkLoabWvvp1F_byqMXodHisCTVialS6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ceb73e56e.mp4?token=HUSg-bLIxXUYCrPgSySd8-GbylNDRP3G9wKhY4bG9if8oq4_7OK61Uf3y5-Bq9MtVnDQUsqMDbcxqKF40bQLS5SsmlJEQA5RG8Ohp2B2pLY_-BcDSjOLHvizSjH8W5guy9E4kZgrX08b_lfKE26Asstd1tHauuDZ-dCIxbGi1yPo3OLZy3gH5N7UNxkWF7W1PIx-MqVjLe10ldaZwv3I-zaF8cgZiG1Oo4F618Zs7lIC7ARli8ZFQrh70vkoNravnuFE9myDa6MBLjvP4RCrtleP96nI-rWFUErkWNcFHxc2VnS6w5ghxBkLoabWvvp1F_byqMXodHisCTVialS6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد تايلاند يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/naya_foriraq/80820" target="_blank">📅 17:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80819">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4313681fa.mp4?token=mP0RoHYdgKVdAfmpwATz9jb3-GZYIWjKic3qt7AR_GxgGNqrYfwukzB_lPIqAO8UlFyTm4wcn27tR2JEfrTrUbF9ZYraeqY2o_t5PTP9RGks--OhIGsiIT_lyeELKL-hMI3Mc1SOVVMFNMmHJESuBDmj1PDZbB-5ngFrFrUPUgjf5PyRQkd2NAeRbTJoDLpAk5oeC0GccGPF8GW75v_PaySsjfLNFIDG4vd68VSC1zSbTklseKfI4QO50s0asSG_uYRrJz6nlinUvxgA0LPZw5ky56odOI0hf8Vy4CM_EP9mi7RorRkTrSw1A1Jc600b0HTMx3vnyavgvfxhZzTw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4313681fa.mp4?token=mP0RoHYdgKVdAfmpwATz9jb3-GZYIWjKic3qt7AR_GxgGNqrYfwukzB_lPIqAO8UlFyTm4wcn27tR2JEfrTrUbF9ZYraeqY2o_t5PTP9RGks--OhIGsiIT_lyeELKL-hMI3Mc1SOVVMFNMmHJESuBDmj1PDZbB-5ngFrFrUPUgjf5PyRQkd2NAeRbTJoDLpAk5oeC0GccGPF8GW75v_PaySsjfLNFIDG4vd68VSC1zSbTklseKfI4QO50s0asSG_uYRrJz6nlinUvxgA0LPZw5ky56odOI0hf8Vy4CM_EP9mi7RorRkTrSw1A1Jc600b0HTMx3vnyavgvfxhZzTw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد ميانمار يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/naya_foriraq/80819" target="_blank">📅 17:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80818">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=MyLnVDV34vkqjJY-aQY4ARX9Z4JYhbLRg6WrXN3dX0xRqDMJgMg6jprSc9TaYf4P_QaHLFl0OlMPMEv29tx2VDhwqazsTWdVh7brkl8Ic-OhkEd52e0MyKV5KPs8XWyhS1qYlKh-bw5CId8eiGrgTkTnp9X3wARFfAGncsowSzwHd3q9UbcJM72O0IaqpyR1s0Bya6r9BPjr5usqiTBY4QSHW1Aq9rDaEeNHhrajFnVB6vgw1vPlgRgsA-ZjCc9o-l_2EcQgH_8qd9RO009beHXW6Twvw2QbqfXgHcFHbKsvdq66EoSD13zSEoZNk3EehZNinIzZuJg7Xg8ItyQ9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d1f1d950.mp4?token=MyLnVDV34vkqjJY-aQY4ARX9Z4JYhbLRg6WrXN3dX0xRqDMJgMg6jprSc9TaYf4P_QaHLFl0OlMPMEv29tx2VDhwqazsTWdVh7brkl8Ic-OhkEd52e0MyKV5KPs8XWyhS1qYlKh-bw5CId8eiGrgTkTnp9X3wARFfAGncsowSzwHd3q9UbcJM72O0IaqpyR1s0Bya6r9BPjr5usqiTBY4QSHW1Aq9rDaEeNHhrajFnVB6vgw1vPlgRgsA-ZjCc9o-l_2EcQgH_8qd9RO009beHXW6Twvw2QbqfXgHcFHbKsvdq66EoSD13zSEoZNk3EehZNinIzZuJg7Xg8ItyQ9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزير الداخلية الباكستاني:
في إحدى اللقاءات، صافح القائد الشهيد يد قائد الجيش عاصم منير بحرارة وقال له: "أبناء الإمام علي (ع) لن ينحنوا أبدًا."</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/naya_foriraq/80818" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80817">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=Al5gLhkJHW9SxPEWSKzZKIl_ecY-xEwEPnhm3WzL2V_LENWtSoxdPCAbFgL2hzgiEVZVKdOueNrOtXmV3BxvjrqNQA1ZlhwpZ98R--T7FLQjNdRQ1n8TtOuzxFVSwb1Pv7lf5ytyeUDcYTPIgYu2sVOM9AVe7Ha5XFZZBpIy5S1tA8kuXnTQ1E5GsGVdYSmL7YUembReSpH2xXeDdYwvzel8O3CGmfiXGsCAIjbW-10AkWFLJfyBPFLKtaB-fVDlvx5pmhqN3lEU3wWZEcDzXFPQ_fQQQQ8MdpQx-iFHalaJUWyKsROLvclEy80tkoDEvcprENuljSCRvPFo3t2iUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08572f73b5.mp4?token=Al5gLhkJHW9SxPEWSKzZKIl_ecY-xEwEPnhm3WzL2V_LENWtSoxdPCAbFgL2hzgiEVZVKdOueNrOtXmV3BxvjrqNQA1ZlhwpZ98R--T7FLQjNdRQ1n8TtOuzxFVSwb1Pv7lf5ytyeUDcYTPIgYu2sVOM9AVe7Ha5XFZZBpIy5S1tA8kuXnTQ1E5GsGVdYSmL7YUembReSpH2xXeDdYwvzel8O3CGmfiXGsCAIjbW-10AkWFLJfyBPFLKtaB-fVDlvx5pmhqN3lEU3wWZEcDzXFPQ_fQQQQ8MdpQx-iFHalaJUWyKsROLvclEy80tkoDEvcprENuljSCRvPFo3t2iUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد صربيا يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/naya_foriraq/80817" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80816">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8718f7b7a.mp4?token=ss2aPA-5bJj09xWrTHGHsBCDKdhoqYLKXvXD-Efdx7hPh7b5gMerbdNRp7jW4Sk5QqUxzsDojqQpZ6JRtqK-03WRK0CPOH3QfAf-sM4gn-r3nmR3FOexYnFhpd5kPyiz1r9eL0pbSDqb0fbPAqAdWUt-zUGxPd-Qef6l1QUXdbnkILgDtvI3SesNh8VmeF1YdQ6__6cnEyGEju-u1EvYOerZePhm1u3yeeKxlp8RwqBncunLscrLyrZAaWxapp-aPKS36B42Z_bBAaQIKb0SObIudUlc7R1S5KpALGYl5omTnECh13x-QVYWcqT3warB9dXm5AcwX5vhbPPc66xcZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8718f7b7a.mp4?token=ss2aPA-5bJj09xWrTHGHsBCDKdhoqYLKXvXD-Efdx7hPh7b5gMerbdNRp7jW4Sk5QqUxzsDojqQpZ6JRtqK-03WRK0CPOH3QfAf-sM4gn-r3nmR3FOexYnFhpd5kPyiz1r9eL0pbSDqb0fbPAqAdWUt-zUGxPd-Qef6l1QUXdbnkILgDtvI3SesNh8VmeF1YdQ6__6cnEyGEju-u1EvYOerZePhm1u3yeeKxlp8RwqBncunLscrLyrZAaWxapp-aPKS36B42Z_bBAaQIKb0SObIudUlc7R1S5KpALGYl5omTnECh13x-QVYWcqT3warB9dXm5AcwX5vhbPPc66xcZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دمتري مدفيدف مبعوث الرئيس الروسي يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/naya_foriraq/80816" target="_blank">📅 17:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80815">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123fc63366.mp4?token=CUAXa6JgQucU3y5LAStxu9YF7SZkyt0LFn_ZWe149OV_yOVDtTJAuh3PFWmG46Uerf54cyYORuL7KCTRUVW3SFaaSZDG5RDOfXjLEeXN9DmNE-29b_AacOTskVB4PR-0mNBm4n4MUhzhZXARgpngx7jcMjDBKfFtlsDIT_6V4FkBST8Hvuv8GRsZIeMGhHNWFBOB44yOJXFOpualDvcwQnFnp3iOZyDQ3sACo_OY1RGmq5QYj1uzyzvasdx8I9gkgsUQjbsZGfksu8mrlZX-gHR0Lz8VxVPnDaGsZGyWl7f05tZKZ-KObwoDkfM0BU7FMhzAo0YCSgdk6biKOH689w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123fc63366.mp4?token=CUAXa6JgQucU3y5LAStxu9YF7SZkyt0LFn_ZWe149OV_yOVDtTJAuh3PFWmG46Uerf54cyYORuL7KCTRUVW3SFaaSZDG5RDOfXjLEeXN9DmNE-29b_AacOTskVB4PR-0mNBm4n4MUhzhZXARgpngx7jcMjDBKfFtlsDIT_6V4FkBST8Hvuv8GRsZIeMGhHNWFBOB44yOJXFOpualDvcwQnFnp3iOZyDQ3sACo_OY1RGmq5QYj1uzyzvasdx8I9gkgsUQjbsZGfksu8mrlZX-gHR0Lz8VxVPnDaGsZGyWl7f05tZKZ-KObwoDkfM0BU7FMhzAo0YCSgdk6biKOH689w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد كوبا يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/naya_foriraq/80815" target="_blank">📅 17:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80814">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df855a6622.mp4?token=Gixh_XDifjqD65cU3SPzj_spcirdxPH3ZEqAoyM1AR3HIb3lTxqNtFIDdCav5C9X_Rr4yU9C22qaVKwXfOKmo_VqbQfY-fCpfHYSjuAbzyiuQj-jyB4NdKcBqbHip-nIGJOVPG4FvmUfFcvnyw4bOgfz3RcA4-wTfI59dHB9QKBBhxO2S5z5kflZIN6YuO2ZakUlLhRaRVILMkTjqUza7kdvZdjMLFptoqsnYBgTQqbvBCOiWtqIH3mM1MrevcprF_F1FqCqG9U1rELkCjoH2YrKsmS_G_rWIMQ-jhisC9NXk1FvZPlU10rXrNdMqwMIfvAMhIZzRjLGgKBaLvbjNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df855a6622.mp4?token=Gixh_XDifjqD65cU3SPzj_spcirdxPH3ZEqAoyM1AR3HIb3lTxqNtFIDdCav5C9X_Rr4yU9C22qaVKwXfOKmo_VqbQfY-fCpfHYSjuAbzyiuQj-jyB4NdKcBqbHip-nIGJOVPG4FvmUfFcvnyw4bOgfz3RcA4-wTfI59dHB9QKBBhxO2S5z5kflZIN6YuO2ZakUlLhRaRVILMkTjqUza7kdvZdjMLFptoqsnYBgTQqbvBCOiWtqIH3mM1MrevcprF_F1FqCqG9U1rELkCjoH2YrKsmS_G_rWIMQ-jhisC9NXk1FvZPlU10rXrNdMqwMIfvAMhIZzRjLGgKBaLvbjNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
نائب الرئيس اليمني يشارك في مراسم توديع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/naya_foriraq/80814" target="_blank">📅 17:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80813">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3584cfed.mp4?token=NemkkM7IdjJGFCuDs26_SOWwvfL__VbVVkYdU8sfh-jQm0h99nCfVkXcatrjXel45oohNMVTWUGWcM_n6jSEDsPfzHAA7W8dL-qRv1cJVHrqSAxaq5TVaYYsq8bebPQwJTRM09d45DX8qa9pO22wiTvjO27zWpZeZditVpFGqMzCdgL6VcUwxZNvjr8sjI6BrZesvIoZEu3O6aOFT_mmAaxzalW7rD6uWUlJOX9uNIEXrxR7ZED1zMcZn0TYZFZEW3QCl8mQWzpaWu4Osj9hIsBkYA1179yOuJbMSlzvEBFk7LNcnLYcExJNThkTUB8sPzCVXm5bzFQpYyoKQiFngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3584cfed.mp4?token=NemkkM7IdjJGFCuDs26_SOWwvfL__VbVVkYdU8sfh-jQm0h99nCfVkXcatrjXel45oohNMVTWUGWcM_n6jSEDsPfzHAA7W8dL-qRv1cJVHrqSAxaq5TVaYYsq8bebPQwJTRM09d45DX8qa9pO22wiTvjO27zWpZeZditVpFGqMzCdgL6VcUwxZNvjr8sjI6BrZesvIoZEu3O6aOFT_mmAaxzalW7rD6uWUlJOX9uNIEXrxR7ZED1zMcZn0TYZFZEW3QCl8mQWzpaWu4Osj9hIsBkYA1179yOuJbMSlzvEBFk7LNcnLYcExJNThkTUB8sPzCVXm5bzFQpYyoKQiFngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سعودي يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/naya_foriraq/80813" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80812">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=TFgcgnvtGxROiq-78JQ0SNE7q3AGXi5Qsa3NRy98jE5LAJvmd-sJ7VfQL4jCdxVAcADc6cfFjDkKy7jT8D1anMTB9M81QuEC9qefmSsYwiG4Al5-riJg8E86fSQ0Zx9KNh3b5aO6gmS_ofOjZkKnUAVwkgaQmBcOWJHu2XGyd0tmgOvFUvN-OJK63WJw7BhkjV8IpdcweomlHSZdiHxgAGnId2yS8QSb1nLC14vYVvLXVjpOTOUDlHWX7vc7uBqv1WL4woBPQWK5kInn7qME_5P01E53x3o4F_F2HAZVU5GDl4T9jiH67YZsvYfPRr3evSkszdYVqzLi2ZmTm9XyUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9725ce55.mp4?token=TFgcgnvtGxROiq-78JQ0SNE7q3AGXi5Qsa3NRy98jE5LAJvmd-sJ7VfQL4jCdxVAcADc6cfFjDkKy7jT8D1anMTB9M81QuEC9qefmSsYwiG4Al5-riJg8E86fSQ0Zx9KNh3b5aO6gmS_ofOjZkKnUAVwkgaQmBcOWJHu2XGyd0tmgOvFUvN-OJK63WJw7BhkjV8IpdcweomlHSZdiHxgAGnId2yS8QSb1nLC14vYVvLXVjpOTOUDlHWX7vc7uBqv1WL4woBPQWK5kInn7qME_5P01E53x3o4F_F2HAZVU5GDl4T9jiH67YZsvYfPRr3evSkszdYVqzLi2ZmTm9XyUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد غوام يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/naya_foriraq/80812" target="_blank">📅 17:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80811">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb79238e21.mp4?token=lZc2fNMzju8y1A5kcvGQpXal-KnpzqkpKeH0w6s_2Gx-LEWDatIwyYjcEK3HkA0Pp4xyYcum9FuPwCTktAdw7E3yU0Ufkg2Ja3MH90Xh_x-LKBDl0WgJU0Iy_M0FSYGtRfJBBYNlPaB9vt4TxDqgNqz5LR_yJ4TRE-CgrKkop8W-lD1JtvlZ3BOPez6p15x9LsmCOpQj73-pK0yzgXREHwi-F_JVgYVb6lVSUcR88Fk5_Q5MU3E_zqy88HrJZqHh4VOfBDi17VAkSEoqz1y_wxnESmagMQsyMZd8McNVHs7lRTXDPVRo4ZFFDksgx6xMW6HPEOVhGU2NvjAcY9GXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb79238e21.mp4?token=lZc2fNMzju8y1A5kcvGQpXal-KnpzqkpKeH0w6s_2Gx-LEWDatIwyYjcEK3HkA0Pp4xyYcum9FuPwCTktAdw7E3yU0Ufkg2Ja3MH90Xh_x-LKBDl0WgJU0Iy_M0FSYGtRfJBBYNlPaB9vt4TxDqgNqz5LR_yJ4TRE-CgrKkop8W-lD1JtvlZ3BOPez6p15x9LsmCOpQj73-pK0yzgXREHwi-F_JVgYVb6lVSUcR88Fk5_Q5MU3E_zqy88HrJZqHh4VOfBDi17VAkSEoqz1y_wxnESmagMQsyMZd8McNVHs7lRTXDPVRo4ZFFDksgx6xMW6HPEOVhGU2NvjAcY9GXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حصرية حصلت عليها نايا توثق قيام الجيش الامريكي باطلاق صواريخ هيمارس من الاراضي الكويتية باتجاه الجمهورية الاسلامية بتاريخ 28 من الشهر الثاني</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/naya_foriraq/80811" target="_blank">📅 17:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80810">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=pfHEFOf9fJTPPREWxEQLqE8xroZGrZfwL6fCKgRSipVPAKqgYoSoojruwdr7FDXNozf5V6l6naqSM4V6L3ekopvvoNNk5tCCaAAY5F7eei0BxDBw2sgfeOvLUrjqrsk5AEZ0NaYTzo7vRbL5gWCW-r45L-h6U0jkiTf5OVBgCH1cZQPR8oBzcS0CtV0Cjv0MUTg0YJb27buorWjxLybM7M3c7PpBglcxKtyqwiwhJqCQs5RrVU1Xw0hLfnM0jKRwaKVXu_KntY5KJbSnm9LvLCpCnYeqpBF_o5IPvx6YHK0H3aWdtYJrXPlCY_agRJp333h_QXBEM7mtwSfWXr9Upw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3533d1cf.mp4?token=pfHEFOf9fJTPPREWxEQLqE8xroZGrZfwL6fCKgRSipVPAKqgYoSoojruwdr7FDXNozf5V6l6naqSM4V6L3ekopvvoNNk5tCCaAAY5F7eei0BxDBw2sgfeOvLUrjqrsk5AEZ0NaYTzo7vRbL5gWCW-r45L-h6U0jkiTf5OVBgCH1cZQPR8oBzcS0CtV0Cjv0MUTg0YJb27buorWjxLybM7M3c7PpBglcxKtyqwiwhJqCQs5RrVU1Xw0hLfnM0jKRwaKVXu_KntY5KJbSnm9LvLCpCnYeqpBF_o5IPvx6YHK0H3aWdtYJrXPlCY_agRJp333h_QXBEM7mtwSfWXr9Upw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس مجلس النواب الباكستاني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/naya_foriraq/80810" target="_blank">📅 17:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80809">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de0472153.mp4?token=EGQ6Awavo0yQhFrj4DWwU7-sDxjMc6yVS4HFguTdSqzJWrV4HkZgIyebgTOeky9s1njIKmkMo3oBeST0_NtiFlO-QrREINZjA5ZD31H9sKvANZ4yKSXsZ3ydrz6M1VhwfOlJEsdceLW2lM1xqP5YacbHnzd_bdApW4LBIzjQ0nhqUMio2SHATtH_2Xf4iwTIx0q1tssv2qQoW_6GJi4rU9on2rze-xmaLDhAUXZ6Hjx78y7tZEAL1kTaVC7KIZ_VYomjOwqifj6Gl7dg0sS3GhxUaXOQUpIcAAXlM7X26Qu1iPX2oMlvUaUUewyXWFkS4f_K_SiVnmzw79KUxOQ5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de0472153.mp4?token=EGQ6Awavo0yQhFrj4DWwU7-sDxjMc6yVS4HFguTdSqzJWrV4HkZgIyebgTOeky9s1njIKmkMo3oBeST0_NtiFlO-QrREINZjA5ZD31H9sKvANZ4yKSXsZ3ydrz6M1VhwfOlJEsdceLW2lM1xqP5YacbHnzd_bdApW4LBIzjQ0nhqUMio2SHATtH_2Xf4iwTIx0q1tssv2qQoW_6GJi4rU9on2rze-xmaLDhAUXZ6Hjx78y7tZEAL1kTaVC7KIZ_VYomjOwqifj6Gl7dg0sS3GhxUaXOQUpIcAAXlM7X26Qu1iPX2oMlvUaUUewyXWFkS4f_K_SiVnmzw79KUxOQ5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزير الدفاع اللبناني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/naya_foriraq/80809" target="_blank">📅 17:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80808">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135827909c.mp4?token=rwgTnvVO60ned8Cw66vac2ot982dxuKAvc8mcNSPWCC-FNzNWsHWRa8hR62y_5oiViDH1b8Vmgg1wTHwmy6uoJVSM2F4UmyiPdaukLlHe028poSNTsBwC5_6QDbqR7CmJCAFq4emkol45TWRBQzGN_OA748cSOqBCleDZdPm3ncWTIEXVObEQwQtVE2l7GgfvI2Zkn0fteey9gaoQInx4deJZXXHYSnKIpFXyn2h-h9xqV2IZN9WzH2ci-3Bnj219cHFmwBAN3b8JFhqeoKCIdorYYObYxndE4ReMVsspyISVoGWbt10WiCIRRiSnuJYrTiR-0-Fbi0vcOfN5SrZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135827909c.mp4?token=rwgTnvVO60ned8Cw66vac2ot982dxuKAvc8mcNSPWCC-FNzNWsHWRa8hR62y_5oiViDH1b8Vmgg1wTHwmy6uoJVSM2F4UmyiPdaukLlHe028poSNTsBwC5_6QDbqR7CmJCAFq4emkol45TWRBQzGN_OA748cSOqBCleDZdPm3ncWTIEXVObEQwQtVE2l7GgfvI2Zkn0fteey9gaoQInx4deJZXXHYSnKIpFXyn2h-h9xqV2IZN9WzH2ci-3Bnj219cHFmwBAN3b8JFhqeoKCIdorYYObYxndE4ReMVsspyISVoGWbt10WiCIRRiSnuJYrTiR-0-Fbi0vcOfN5SrZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لمنظمة شنغهاي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/naya_foriraq/80808" target="_blank">📅 16:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80807">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=chsDBRmo0DXHcgYYH2baYxF9mEkSTj47UNYPFlyPw0vVq1DbZFj51ABLyX04om1HAjMvikYXp8aUYsg6sw_vd-x1ie6azslGxi98DsQ-pDDHzDR9dWrzP46dhHU57oQ-Ia0XzS8DqkiAd9t83XQjuoVhZCZ7Ba-KZoNDpQ_6Gk21weZFggH-I7G9OhFzcGWifzYYfOipZ6t_1a5xYn4K0S4vCJ_UDuENCquChYauryEB-jPqoYyD9_LAnQqp1HJWnWOgCyDGcWvf73dCyuxvVJGOHocYAA1lMCzEO-YFWf3QM2194wg5uY49_mpXJ9-xN2Tnloh6hLhi7EbT2cQ9jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0695c6fc2.mp4?token=chsDBRmo0DXHcgYYH2baYxF9mEkSTj47UNYPFlyPw0vVq1DbZFj51ABLyX04om1HAjMvikYXp8aUYsg6sw_vd-x1ie6azslGxi98DsQ-pDDHzDR9dWrzP46dhHU57oQ-Ia0XzS8DqkiAd9t83XQjuoVhZCZ7Ba-KZoNDpQ_6Gk21weZFggH-I7G9OhFzcGWifzYYfOipZ6t_1a5xYn4K0S4vCJ_UDuENCquChYauryEB-jPqoYyD9_LAnQqp1HJWnWOgCyDGcWvf73dCyuxvVJGOHocYAA1lMCzEO-YFWf3QM2194wg5uY49_mpXJ9-xN2Tnloh6hLhi7EbT2cQ9jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد كازاخستان يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/naya_foriraq/80807" target="_blank">📅 16:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80806">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c785f3b.mp4?token=eSQOMDQg0bKLPcM8KcBr3TyqKHUlQUV3KZJj2y7JqibGehtN7Fj9amnLgqU85S2JKr-Wvw5qUtMkUqjUyOgle3kJ0UwyQqeLEWBQN6H3R01wUZXnZTcR7EJeZ6k0z7C_EkA53q0uHdeTRMFgnFm40M2Sg20u1vQHMRzxUm4UEvBJ9zANMRDjHbAUM4-T-SvhJhjD-it4OQLAIHrgsHXA7W0x2iAy-cQVTAZDf_nUjqdLAjUq771SZm7SCkcRCrNa5r3nNC1yL1PWyHTr2BFX2iROtJ9tZllU2dQvHLqCpslkdFZrj4tFNOTHEukiyPgp73rhkjGp44qZfz3BaUmEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c785f3b.mp4?token=eSQOMDQg0bKLPcM8KcBr3TyqKHUlQUV3KZJj2y7JqibGehtN7Fj9amnLgqU85S2JKr-Wvw5qUtMkUqjUyOgle3kJ0UwyQqeLEWBQN6H3R01wUZXnZTcR7EJeZ6k0z7C_EkA53q0uHdeTRMFgnFm40M2Sg20u1vQHMRzxUm4UEvBJ9zANMRDjHbAUM4-T-SvhJhjD-it4OQLAIHrgsHXA7W0x2iAy-cQVTAZDf_nUjqdLAjUq771SZm7SCkcRCrNa5r3nNC1yL1PWyHTr2BFX2iROtJ9tZllU2dQvHLqCpslkdFZrj4tFNOTHEukiyPgp73rhkjGp44qZfz3BaUmEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سعودي يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/naya_foriraq/80806" target="_blank">📅 16:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80805">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e927a24458.mp4?token=tZNGGEWEEGV1sqFoOFzhhgzg5JI46ii4tGPcTWS5BdETPWaQdoqvPBmBVoqQwvsSy344dJ3YEDT2zF7bky4DuvJEetz0Z8JjxSwua-bG755vdJwceSGEYB-JKdp6Gz4C-ma_4eJUIZiJFA4el-0-IqWFkm1EhBZaisaE_oWrJTnGMjWwymyN4Ts5iwuM7rCWQsnSucQS6bejcQRb_sO9BB-GEIWANlUnPhjFSY0sIt-KwLThF7EZEySw5NGbwhHQufOForqRyysu560wKrHhdKyojrELhzRfSn4ZDlV1h4IE53dDal_ofhCU45O07QVs5Nsp8dXf5_qbLNQwZemRZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e927a24458.mp4?token=tZNGGEWEEGV1sqFoOFzhhgzg5JI46ii4tGPcTWS5BdETPWaQdoqvPBmBVoqQwvsSy344dJ3YEDT2zF7bky4DuvJEetz0Z8JjxSwua-bG755vdJwceSGEYB-JKdp6Gz4C-ma_4eJUIZiJFA4el-0-IqWFkm1EhBZaisaE_oWrJTnGMjWwymyN4Ts5iwuM7rCWQsnSucQS6bejcQRb_sO9BB-GEIWANlUnPhjFSY0sIt-KwLThF7EZEySw5NGbwhHQufOForqRyysu560wKrHhdKyojrELhzRfSn4ZDlV1h4IE53dDal_ofhCU45O07QVs5Nsp8dXf5_qbLNQwZemRZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سريلانكا
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/naya_foriraq/80805" target="_blank">📅 16:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80803">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">إمام جمعة طهران:
طلب الثأر للشهيد القائد هو مطلب جميع المسلمين. العالم الإسلامي فقد أكبر شخصياته، وقتلُه ليس مسألةً صغيرة.</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/naya_foriraq/80803" target="_blank">📅 16:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80802">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=chnD_V-foXNFfWecsWslAYgovcoMQ-p31_Qemzn4Dea6s79-nyYG_GNZaZOA8E33RnQEHNJTyW1guKRV379xe_FVX2Fjm-scSiUtcXDd5KzDhkH0_6tNym5sMyLR9GArmOi2HWVAtDwxC9arblJm28sWyD6fQaEWbxNPmV4GMMb0_bqvXik5sE_OYX3oYMDws9woPj2nVi22Vm3kpbbypy_R2JjfS_BMdNB3EkmrAMiqGkSVFKkAPQ__gXE4saSKnIti979W5ywZYhFfCOQ9b6s8ZgzWionIrbKWLDj6DeaGOOEZcy1eW0rlWSRx-el55QN585OvsDiPXiGXNXcG4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807a058ab8.mp4?token=chnD_V-foXNFfWecsWslAYgovcoMQ-p31_Qemzn4Dea6s79-nyYG_GNZaZOA8E33RnQEHNJTyW1guKRV379xe_FVX2Fjm-scSiUtcXDd5KzDhkH0_6tNym5sMyLR9GArmOi2HWVAtDwxC9arblJm28sWyD6fQaEWbxNPmV4GMMb0_bqvXik5sE_OYX3oYMDws9woPj2nVi22Vm3kpbbypy_R2JjfS_BMdNB3EkmrAMiqGkSVFKkAPQ__gXE4saSKnIti979W5ywZYhFfCOQ9b6s8ZgzWionIrbKWLDj6DeaGOOEZcy1eW0rlWSRx-el55QN585OvsDiPXiGXNXcG4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد قطر
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/80802" target="_blank">📅 16:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80797">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBMY1EyoTWZFdVJ7tXjho1NKZjjf364XSCFSqYiuhB5RCR-CYKRU39Dhe1fCPvfSKnGN-HcqF6gt4Luc1M0IAZcuxD4ZBy4GbqeOimjfEHzBB5Ciwi4CZRJO2LxWkYJAjD4rlanK8J96et2N4vYRPGqp4-p14D41f-SWNpTjakRGHYDpQfOTMR5zkZteH7S7Q3hXxeH4jGQApjZRbtser8bFmqI2i-PSQrTy2UDnqPyG1s_s-3AQdkVkriLYd0qCgSgLD9X6eF71gjhmNpVPCadEbNui82k3EWwn7aibGr3dm1wylSDL2T3lTllbn0YKvktk1BzEalHd0qXKrA6qAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwmKojMcbv9lW2dr-s04wgY1V9u6a3LzxdPOxH7LKConEasPyQwTw9THu6NX7k0WOYADP82J3wgFWtK0HQuc534Muo1OSctmBkkcZaKF_y6tZRM4ZGUIxwz9-aHeUQEyHupRzSamtmi2orhviQDHoW_shrmm3228jEu3jyc0VvVGzmAQ44d-XeUzum78B9nkPCi4l0wjOE8hFgkUVfwRbXoyyWY5_E6SlQDQKVzQR_dndHY4VlTPYTG5AAwoShUNABgHybK81m8Zs0elMPP5oPobf7HHbWxdDd5GSzBAMdAuwrWlVjUT4waYLVqD9dX6-uAxU3D4FDrAX38E8D2ElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ctZVPE8Gr9E2fPlkXCgXazGLfSOfSaI5fc1DhnFeCo47n_7ba7RUg04lUYhsCj4l843ZGDVHt2YbNKRxJfCRbLCnXQQvZU9o1xk_ll6DUIkPGDkwWEC9ay__iU4fM_DZyaxLMowW3u96KLhLIsTRin6O9dwMdtQTONqb30MJ96wloxi2eiPvQvpCUwiZ_3Yxwy5nFI_vDze4_4xgmuaYfDl2e4Dr2jYymqCGgpqz_JX_QZxBkqB56EeVgYSBD4IU61lMM40XpY4jUgVp-pfZbV3qsjh2mSlTzKLeyFm4ldxXnJ_2Uk2CsM7UtdAdjs17Y0bimnlDcnsSz_vbOsiPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1RNTfOf2TxhULHh0_oykegpsxiy-OZNW4AM314USLZGayHwKr9xPcOy-hOrdK92OkXNNjfbKHQiKnKMl85-VdkkkWAEzwOAJFpVtUXOblyNHOwJwcW1pu-cgw0P6FWXKV2hcmdZksIxy03QEgasApFsjGisW8mAz_3kq7zVxSEpYCvngQmWrIX_6FnAYsFW_K_HOuS47-PohXZKHkj8QbPWA0jtkSW5NHChXPq7Nq3t-dNMG6yCU9noXAQZSGUKbhcfasp1IYVPK0_NNtqylb9G_2JZ_WmZ8qm0-xm5boI4Bi-mpYcjVjZYDZ1O8ipN9uf8Zax8jUsKAVmIWGg88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUuaE36UfQjUoqv6lccMHqFeWQINZsf7hRuR1NJzcOyENYMNCvyxExzeAXsmvdpQQIXtSYR4a1W8axFac6FjtUeo5lIxrxSIa4eL-LvN8C7cHrq32Iz3m7sFU7teZdHzC_X3DNc0v2dg58ji7sLvo_l4g_OxatAxwTKPf3wEq3WT5IqjWlmjh-FR3vzXGgszMhTgZw5hT-HsSjV73oMC1o4wLW_s1b0AnyvSmDnbRWFhH_6NOeyiEnU0VYykNk0OEI2GO2WVNfImPUjiU3gWCETW0pWfBxAIv06cJBav_BMyhqGjJE3bp2UseEYuO8IkoaA4Zjt5ywfytJdYU1af4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الوفود الاجنبية تواصل توديع قائد الثورة</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/naya_foriraq/80797" target="_blank">📅 16:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80796">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae22d0a81.mp4?token=VzpQM0OfkJxYZKUoIx0bv7Yl3d-fhblPE_DpNafMGIF6gfFOsOJhfTZekH3qmsM3vS1A9qGQ7sSoY37QonXsF_n4NKif9yp1chD4laTbQvZy8TspgYSyuRthcKkOaTDKuIAtTkflGSzBVo2_5YoqgtsYpBaeWGUOGtcLO8xFdg26X-S8DpCsxdvy2_lQ_bMNZvOt31jc3IBMSqsBLk-7d_LwnCiEkG5NBoZbOPmpUhZBVNyTL5_hw-clOEdrOxlp71Yt7za9G0XM-6CtQttOKLW3rlRxvPxBFCtaTYefgcAr_Shm9IRr6TExS2wZUdaIbTv2v51tOzBXCNKLHHj2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae22d0a81.mp4?token=VzpQM0OfkJxYZKUoIx0bv7Yl3d-fhblPE_DpNafMGIF6gfFOsOJhfTZekH3qmsM3vS1A9qGQ7sSoY37QonXsF_n4NKif9yp1chD4laTbQvZy8TspgYSyuRthcKkOaTDKuIAtTkflGSzBVo2_5YoqgtsYpBaeWGUOGtcLO8xFdg26X-S8DpCsxdvy2_lQ_bMNZvOt31jc3IBMSqsBLk-7d_LwnCiEkG5NBoZbOPmpUhZBVNyTL5_hw-clOEdrOxlp71Yt7za9G0XM-6CtQttOKLW3rlRxvPxBFCtaTYefgcAr_Shm9IRr6TExS2wZUdaIbTv2v51tOzBXCNKLHHj2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد تركيا
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/naya_foriraq/80796" target="_blank">📅 16:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80795">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=H_PuRETce66GTM8AXE7A516OMthxysealFFX-gFgwwslHsM-IkYdjfmoxoKT6YCtk-WBf58QJqTZiZOOo-1GAIzyPfjusJZ1p57wMQqIMjBwX0FHg5p8Q2yniusdFW6NJOEBvORMc9cQhadQVvF8NtM5ovJ_4nEYjzQu-E37uU1Pic1yJJUrvcmu1i4E3RTtKkOtVuvkeRqeY7M0wz-yFAkYw-m0SmXnTaFaS8GsCw8Rh0nhIXHazTdNSVG40W5VELGbHihcr_P1RO2jWFt29HuU0UVxU1QrauGx8HaeErbGxNJfCWyJFgwucdSi3qqehZL9bNIXRxjVIk69XICPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9cddcc3e.mp4?token=H_PuRETce66GTM8AXE7A516OMthxysealFFX-gFgwwslHsM-IkYdjfmoxoKT6YCtk-WBf58QJqTZiZOOo-1GAIzyPfjusJZ1p57wMQqIMjBwX0FHg5p8Q2yniusdFW6NJOEBvORMc9cQhadQVvF8NtM5ovJ_4nEYjzQu-E37uU1Pic1yJJUrvcmu1i4E3RTtKkOtVuvkeRqeY7M0wz-yFAkYw-m0SmXnTaFaS8GsCw8Rh0nhIXHazTdNSVG40W5VELGbHihcr_P1RO2jWFt29HuU0UVxU1QrauGx8HaeErbGxNJfCWyJFgwucdSi3qqehZL9bNIXRxjVIk69XICPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد نامبيا
يشارك في مراسم توديع قائد الثورة</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/naya_foriraq/80795" target="_blank">📅 16:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80794">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=fB-DeyeClPI7H_DykykKF86T4U4TKN3-YJ_yIg6ZqIH2SRFBPE6SpIXErl3OPoFqDY8R5OSh9a_zaqWW1kLluSqJI3RLQ-cYG3bv-3qKIyQxHYPl4DRbrtuEz2ip6SjbW2HrN153JeFcvwPuCxAijyxmHCjGMeaNs88CaeRI1R6dCJGdnB6f5F39L_Ru7RV4VSS4YDMc-9qXHkASFU5fuwVwcVjENg-_atkcxLG8SXq_-JXlg43yTFn0TYv2IeKqByD4AhbapJiXNUWZtwh6vDlaOzdXSPfBIyL1UOFLwVFPRPpcxil49l55oV5BIQ9P-3ZksR6cAfgK5RJRo7O-ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a0eebaab3.mp4?token=fB-DeyeClPI7H_DykykKF86T4U4TKN3-YJ_yIg6ZqIH2SRFBPE6SpIXErl3OPoFqDY8R5OSh9a_zaqWW1kLluSqJI3RLQ-cYG3bv-3qKIyQxHYPl4DRbrtuEz2ip6SjbW2HrN153JeFcvwPuCxAijyxmHCjGMeaNs88CaeRI1R6dCJGdnB6f5F39L_Ru7RV4VSS4YDMc-9qXHkASFU5fuwVwcVjENg-_atkcxLG8SXq_-JXlg43yTFn0TYv2IeKqByD4AhbapJiXNUWZtwh6vDlaOzdXSPfBIyL1UOFLwVFPRPpcxil49l55oV5BIQ9P-3ZksR6cAfgK5RJRo7O-ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس المجلس السياسي لحزب الله اللبناني
يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/naya_foriraq/80794" target="_blank">📅 16:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80793">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
🇮🇷
الاعلام اليمني: طائرة إيرانية مدنية وصلت إلى صنعاء كان على متنها أكثر من 200 مواطن يمني من المرضى والعالقين في الخارج وغادرت على متنها الوفد اليمني و أكثر من 200 مواطن يمني من المرضى والمسافرين</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/naya_foriraq/80793" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80792">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e102375304.mp4?token=EkAvo5JE8L_JBabnUGL-OBkvHcxz6bQ-TIkvSGT8Pvgz2WPSsvfb3Tt63eqwOXxHB8t7USpAjT13oLzCBFSaECN9pn9jqDzakviWgpO0fCQtHuwT8KvWHSU4jFJJ3LClgUd13USqrr09BpLWqZXcInkE4nsOWJDVEsLgRoglvPdibaVXh5iYdTK7pLDaW_qxPGoruauRP9A3aQWw1vLD7oqqocsoFU5gdHJ_9natiUi7HFhekQiHoMSV9zZ_WEhlG6ScPDcXulDADpb2hErZXUTktLvpOEOEjOzWFyijV5OdGzKZD61LysM_OKQ4HR5Z8ST401evnXsvXJp1pwyeIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e102375304.mp4?token=EkAvo5JE8L_JBabnUGL-OBkvHcxz6bQ-TIkvSGT8Pvgz2WPSsvfb3Tt63eqwOXxHB8t7USpAjT13oLzCBFSaECN9pn9jqDzakviWgpO0fCQtHuwT8KvWHSU4jFJJ3LClgUd13USqrr09BpLWqZXcInkE4nsOWJDVEsLgRoglvPdibaVXh5iYdTK7pLDaW_qxPGoruauRP9A3aQWw1vLD7oqqocsoFU5gdHJ_9natiUi7HFhekQiHoMSV9zZ_WEhlG6ScPDcXulDADpb2hErZXUTktLvpOEOEjOzWFyijV5OdGzKZD61LysM_OKQ4HR5Z8ST401evnXsvXJp1pwyeIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد حركة حماس الفلسطينية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/80792" target="_blank">📅 16:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80791">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a9913937.mp4?token=EAMQaF1N0NlBj05M8MvfURURdwDBjMHNJPSxotphsPgzjWRtgQ_VvjknFy_xo2YM_UiDY6gCPaQq8ulnK7KPMTgtq-MHQanIgX7DqC034tTuHf7Kz674ZtCmGXVHdXEOVIvfH-YuxECi_qmOsonC4ubRSpdv3LgR1Ju58EYr5yIiFlerVSmvrZFD3ljLdTRd2qVnL2QCc2GGag-r1glyCwXXB5G1-VZwRJk0mer8irAvKc9TjWeP24MsWxu58qYZutviCzJjmkCjO_kpwQ1YilLYVOZ7G4zw9u5JfwJmpqRH5cn0NGapmsOX7Ghz5lEp3H4YP0utyPmjtmYQAJR9VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a9913937.mp4?token=EAMQaF1N0NlBj05M8MvfURURdwDBjMHNJPSxotphsPgzjWRtgQ_VvjknFy_xo2YM_UiDY6gCPaQq8ulnK7KPMTgtq-MHQanIgX7DqC034tTuHf7Kz674ZtCmGXVHdXEOVIvfH-YuxECi_qmOsonC4ubRSpdv3LgR1Ju58EYr5yIiFlerVSmvrZFD3ljLdTRd2qVnL2QCc2GGag-r1glyCwXXB5G1-VZwRJk0mer8irAvKc9TjWeP24MsWxu58qYZutviCzJjmkCjO_kpwQ1YilLYVOZ7G4zw9u5JfwJmpqRH5cn0NGapmsOX7Ghz5lEp3H4YP0utyPmjtmYQAJR9VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول دمتري مدفيدف المبعوث الخاص للرئيس فلاديمير بوتين إلى إيران للمشاركة في مراسم الوداع وتشييع جثمان القائد الشهيد للثورة الإسلامية</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/80791" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80790">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmxxFEyC5JOVxib_UOngjgJEHf5FcZkBxPhDUU2UPDa66RXD6gsZlMtG6FX2iyKBooarvEtrcFefZOkuQ6E77Yh08SBInIhJ7AJ5uuiDX_kbZBwf5oBlbS2HCSQ6KLg64O2PVmGF8PHkPGH6AgTOLPV9sfGd4uM-6k2ttKIFEbIdMotO1I5xaIzuCeg-B_kPqyuNBS-e9_cEasJ40hrCXAI30vCpATF9_vSUCy8Wa9r_pXMGElk7T1DyYM44EsDU7xezyjLyoTWQ9mrhXyj20aRPN8n366hEbE2Q7CDPsgpeOIraFeotjq6Zar0Y2pVgnV8oVSDNB2NGscfgd7uK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنشر للمرة الاولى
🇮🇷
الإمام الراحل يمنح وسامًا للشهيد الحاج قاسم سليماني
.</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/naya_foriraq/80790" target="_blank">📅 16:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80789">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=mpQm06UMz2yJ519r3AzUxaWF7W-EsliFBOr7V6fLXxm9Ro_-uYwYolPAQrNZDQx7tSq4A3HkiweQ-Vtp2iPrRk5TK9NUlGADTWocdw6c6F_qWZDjNwC7ONsfHD_pRQ_nORLL25IoFyC7jx_Sz2rornPoAp7KL0zDrQR5TfSkUC3eO8tifJgkljGyhYxi5hAGFmol43C0TOkGhm7A3NPeOu5NL5KsDbgAMdWzlW_bx-ll8uLP6OGw3-AEnWYUUnhYHq60s4aXznS7WDst95DzR3YRDEOXuJ6Le6HsT2FSH9pM0-N8H-Scs6goYxuvN93w-Gux7uDkpChU88SC7yEDYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1034b5518a.mp4?token=mpQm06UMz2yJ519r3AzUxaWF7W-EsliFBOr7V6fLXxm9Ro_-uYwYolPAQrNZDQx7tSq4A3HkiweQ-Vtp2iPrRk5TK9NUlGADTWocdw6c6F_qWZDjNwC7ONsfHD_pRQ_nORLL25IoFyC7jx_Sz2rornPoAp7KL0zDrQR5TfSkUC3eO8tifJgkljGyhYxi5hAGFmol43C0TOkGhm7A3NPeOu5NL5KsDbgAMdWzlW_bx-ll8uLP6OGw3-AEnWYUUnhYHq60s4aXznS7WDst95DzR3YRDEOXuJ6Le6HsT2FSH9pM0-N8H-Scs6goYxuvN93w-Gux7uDkpChU88SC7yEDYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لحركة الجهاد الإسلامي الفلسطينية يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/naya_foriraq/80789" target="_blank">📅 16:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80788">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وصول الوفد الرسمي للجمهورية اليمنية إلى طهران للمشاركة في تشييع قائد الثورة الإسلامية السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/naya_foriraq/80788" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80787">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وصول الوفد الرسمي للجمهورية اليمنية إلى طهران للمشاركة في تشييع قائد الثورة الإسلامية السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/naya_foriraq/80787" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80786">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=YtC7KRHyKYUPRokZYPxkbfuE1gv3ID5LuSBNNDgttmsGuRpXjESYSmwI_EASOZFXSbwycroY7GLRc0ssSl3RBLhymFHAV734MzKUyqMzJNsEfTLhATPe3fdrPvSd2H-GB4zBPWAS_oRuVYM57kk0RHKPyzrJ1PjFfLCUZRUcZzs-2rsyJ7AzFYsUrTf-FCXvVrxtIJ6yt_bEjYkEEl5yPTa_gHBAU49KcdVltQNXPT64vz_BRp9-C5V2qOw1PehVcmoVDCAEkwVNSwjAMUeUJbelIGaelpI-fQSwNmhpPt6yKwbIEiVmhnGNDhBBOangq56QsKj1wbfw2BgcMi2jcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c47bdcde23.mp4?token=YtC7KRHyKYUPRokZYPxkbfuE1gv3ID5LuSBNNDgttmsGuRpXjESYSmwI_EASOZFXSbwycroY7GLRc0ssSl3RBLhymFHAV734MzKUyqMzJNsEfTLhATPe3fdrPvSd2H-GB4zBPWAS_oRuVYM57kk0RHKPyzrJ1PjFfLCUZRUcZzs-2rsyJ7AzFYsUrTf-FCXvVrxtIJ6yt_bEjYkEEl5yPTa_gHBAU49KcdVltQNXPT64vz_BRp9-C5V2qOw1PehVcmoVDCAEkwVNSwjAMUeUJbelIGaelpI-fQSwNmhpPt6yKwbIEiVmhnGNDhBBOangq56QsKj1wbfw2BgcMi2jcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد سلطنة عمان بقيادة رئيس البرلمان يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/naya_foriraq/80786" target="_blank">📅 16:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80785">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd3019015.mp4?token=iw9zNekWszFQ3Yhbu1La5nFlCgVnvmnhKPTo3yy2IHJ8DCYGqqCloqfbTvSMlHxcUb1iRgx7vbwtc49a7pGKrVS4Cpv56LDacBW1KFNB1r_Bx6lseFzmvF1-3UMcNTRceBLWsW3eQ3vi28X4u_TGq-DTAJrsXpok1C9vgwdJqompcAF-TuotYefAvVk315hc9E1t29i200EB5ba_n21igCjSZC9KGKmVg5VqgeT3-Xy0uUNhSEUelv4EkJ70sJWApjQum__6L8gkb1XieMl49dRe6L-qxFr01SylAjYDVyKtjXF22XLlNRraUE6is78O-p2EECki9_XAAFpqhkprHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd3019015.mp4?token=iw9zNekWszFQ3Yhbu1La5nFlCgVnvmnhKPTo3yy2IHJ8DCYGqqCloqfbTvSMlHxcUb1iRgx7vbwtc49a7pGKrVS4Cpv56LDacBW1KFNB1r_Bx6lseFzmvF1-3UMcNTRceBLWsW3eQ3vi28X4u_TGq-DTAJrsXpok1C9vgwdJqompcAF-TuotYefAvVk315hc9E1t29i200EB5ba_n21igCjSZC9KGKmVg5VqgeT3-Xy0uUNhSEUelv4EkJ70sJWApjQum__6L8gkb1XieMl49dRe6L-qxFr01SylAjYDVyKtjXF22XLlNRraUE6is78O-p2EECki9_XAAFpqhkprHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد الكونغو بقيادة وزير الخارجية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/naya_foriraq/80785" target="_blank">📅 16:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80784">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مصدر روسي لنايا : المجاهد الكبير ولعنة الناتو دمتري مدفيدف سوف يشارك في عزاء السيد القائد في طهران</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/80784" target="_blank">📅 16:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80783">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuLcmGgUlZM3qnXYhP_fc6zcBjSisXhXlno62WctSzfxkep_y6RowOddF1kEXPC2zbRJx6EOrD7cyT6b0tc8JIGjTmHQsez_2mMu6jwUTsis5GW1VI_93_9FE4uaDV_YZjYuC5_K_9PJW3H7-2nM66gKchKx4N-25fr0DtJ-B41jDRwFL8hbTbjeHPh0XLxWi-UWXJ8GYLnewpdbVTX-o3S-Icz5Dunc0XXC7kNdvjBrLJmFmRyzO6eYk6IAIGsCDA7UbNkCCNoH35yramyBPEtCZBTTv90wj8At5LRmqBVGGTOHCc7xMKdIqC35bb6htjUXRG170SSSGBePyeIj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب يهاجم الناتو مجددا: من السخف أن تستمر الولايات المتحدة الأمريكية في هذا المسار الأحادي الجانب في حين أن العلاقة ليست متبادلة. لم يكونوا موجودين من أجلنا!!!</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/naya_foriraq/80783" target="_blank">📅 16:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80782">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4429ac1471.mp4?token=Bhgf6UN08h4zfn2raXV8W1e-F_fMoDTCZJzQwwmnRyfxAtLAdLb79EanEe94llenH5Wya5iael1vTD522-7NVy6dalRsViEWwtxSKw6kfWKMskCpKj-7egSuHF7sIUOe7I2IHhdzz1UXGcFV18Rd7biqWryVLaa-5Rg6FX07KzejIXVEv8Qs23lSnRjuTHo6iTkyZI-UckZ_jmbBNuAWk-hludoYXdiANW1YxJvvwmf2m6p0uEl3riX9gAaTGBX1uavAjbE8nTYYD7XE32MuDBUBh3EQyYEcM_TKigciKaca8mMZ3u278cWN4Gerb3WuSeAmrI6GhI51u3Ql0WEwKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4429ac1471.mp4?token=Bhgf6UN08h4zfn2raXV8W1e-F_fMoDTCZJzQwwmnRyfxAtLAdLb79EanEe94llenH5Wya5iael1vTD522-7NVy6dalRsViEWwtxSKw6kfWKMskCpKj-7egSuHF7sIUOe7I2IHhdzz1UXGcFV18Rd7biqWryVLaa-5Rg6FX07KzejIXVEv8Qs23lSnRjuTHo6iTkyZI-UckZ_jmbBNuAWk-hludoYXdiANW1YxJvvwmf2m6p0uEl3riX9gAaTGBX1uavAjbE8nTYYD7XE32MuDBUBh3EQyYEcM_TKigciKaca8mMZ3u278cWN4Gerb3WuSeAmrI6GhI51u3Ql0WEwKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد جورجيا بقيادة رئيس الجمهورية يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/naya_foriraq/80782" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80781">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600ab9c890.mp4?token=PXgOefPjLU5a_cvOr4DPcvewLOdu_el-Qvbx4pLof3hnKohA2_f8Vjfx2YRb0cJHo9LPinFnXkJomAP38JinddICJdwa34is-IxTAOJqmobeE4vcPMYMAIeuhfxRwZqq_zj6vfrtepfEsBew9QhgYQaQJgumwvN6kEit_TQTvNZaIcshfWn42dyzkU4lXjhaacbSSSbhwf85R-hRGJKPLsVZl8S1QbmlZy7HBPbWJWR7Xxs74whu_I4Cu5ij4Phy35y4UAgJw3CS3b1xSufR6lQmoiVdCgZ3LEI5F6OPw1wn4DJpl3HwiqhZeLvjBRaUh4OCBMSk18V-zFjLJlGnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600ab9c890.mp4?token=PXgOefPjLU5a_cvOr4DPcvewLOdu_el-Qvbx4pLof3hnKohA2_f8Vjfx2YRb0cJHo9LPinFnXkJomAP38JinddICJdwa34is-IxTAOJqmobeE4vcPMYMAIeuhfxRwZqq_zj6vfrtepfEsBew9QhgYQaQJgumwvN6kEit_TQTvNZaIcshfWn42dyzkU4lXjhaacbSSSbhwf85R-hRGJKPLsVZl8S1QbmlZy7HBPbWJWR7Xxs74whu_I4Cu5ij4Phy35y4UAgJw3CS3b1xSufR6lQmoiVdCgZ3LEI5F6OPw1wn4DJpl3HwiqhZeLvjBRaUh4OCBMSk18V-zFjLJlGnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد بوركينا فاسو بقيادة وزير خارجيتها يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/80781" target="_blank">📅 15:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80780">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34e716852.mp4?token=fK-BpFzRrfxQSaQQ4_YU9kTpd7tXhTzJheTi4WOs-lmjsX_TDiEkaP99BVMmD55k3qB8Ywt3GNS0TBQmYxWTzkwP_cmZjAx2pLeRfjIyciDD9xGT4EA8ppjc62QmyabgWsRZ3t3Vj47_v0vQHA2Y9-rDEwIqLvf3Zz3ArFJCWXozrbvIAuV1IIFV-8rQUjGVYp70ygg6cCk5VsbBKbZ9YE_II5AMC-7eTBbJZJTv4gZXbZ34d0Fjt-byr1fC5aXGVGRPSRSvVd7Of8-FtDWWInAjxSpW5lr9MRUxkESjHxkgVFifY1tkWi1JooaJGFLz6yic1Lh9lxddZO2mSK3ZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34e716852.mp4?token=fK-BpFzRrfxQSaQQ4_YU9kTpd7tXhTzJheTi4WOs-lmjsX_TDiEkaP99BVMmD55k3qB8Ywt3GNS0TBQmYxWTzkwP_cmZjAx2pLeRfjIyciDD9xGT4EA8ppjc62QmyabgWsRZ3t3Vj47_v0vQHA2Y9-rDEwIqLvf3Zz3ArFJCWXozrbvIAuV1IIFV-8rQUjGVYp70ygg6cCk5VsbBKbZ9YE_II5AMC-7eTBbJZJTv4gZXbZ34d0Fjt-byr1fC5aXGVGRPSRSvVd7Of8-FtDWWInAjxSpW5lr9MRUxkESjHxkgVFifY1tkWi1JooaJGFLz6yic1Lh9lxddZO2mSK3ZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد المصري بقيادة رئيس مجلس الشيوخ المصري يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/naya_foriraq/80780" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80779">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ccb792b1.mp4?token=MJX63nufUZ0PKgHLPjc04B8NK0ELwGak84Sqo-WSodu6p0qCVeZkjEyo8D5ptID5M1_tjrTBADtcVdCOGhXPV725Lbh5KHRgq42I7CbN3V68zFoM0HCCarbMgxcHrHELbG9ur-qnu1IM2PNWVfJi4LGuKIB3P5VZCJS4avQxkV6m-BOf2bo6LT-UanHXR_VtXvHDsQazO8nJ35q8JZ1UhYx_SFkpmtSo_Ox5WWQ0TBH2lJNhBB8iShknLaY3cST9Gpk0VaztcEkf8aYQ9LCky8twW46nhzP2s8CS1V3-RRF_jgjXaoLngBfQrbnHN1I1niZmLGfEIyYJtsHFDLEYN36noDfHa6codPLADxBxQeg5EYFXpeHEM0vJddyGFkAiUBrAiF3y3nVsiBDpEkJJc39wLniheWJ6-Oxvmy1oo9i9x0RakV_PxvU-_xdjQw0VR0ysn6yzzpqDa7FpcNH1zyf_UGMVJqbN4eCJNkLZkMIz3UTgNsxleHb3gz7LHm82cebl47rjYBchkLeNKFlUFNma7bjrEqiJI2PxKLhxS94uyugnxX8ZZGgrijiALqNJgZSCwYitJpBc47fGWCDnvSMeyaZwxZWNbtKE8GJhBV7hXTUp2G6_uWetcghwuavUU1qCBzZCOolLg77G6sWLlQH_83N-LFIzkA9TdkytiLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ccb792b1.mp4?token=MJX63nufUZ0PKgHLPjc04B8NK0ELwGak84Sqo-WSodu6p0qCVeZkjEyo8D5ptID5M1_tjrTBADtcVdCOGhXPV725Lbh5KHRgq42I7CbN3V68zFoM0HCCarbMgxcHrHELbG9ur-qnu1IM2PNWVfJi4LGuKIB3P5VZCJS4avQxkV6m-BOf2bo6LT-UanHXR_VtXvHDsQazO8nJ35q8JZ1UhYx_SFkpmtSo_Ox5WWQ0TBH2lJNhBB8iShknLaY3cST9Gpk0VaztcEkf8aYQ9LCky8twW46nhzP2s8CS1V3-RRF_jgjXaoLngBfQrbnHN1I1niZmLGfEIyYJtsHFDLEYN36noDfHa6codPLADxBxQeg5EYFXpeHEM0vJddyGFkAiUBrAiF3y3nVsiBDpEkJJc39wLniheWJ6-Oxvmy1oo9i9x0RakV_PxvU-_xdjQw0VR0ysn6yzzpqDa7FpcNH1zyf_UGMVJqbN4eCJNkLZkMIz3UTgNsxleHb3gz7LHm82cebl47rjYBchkLeNKFlUFNma7bjrEqiJI2PxKLhxS94uyugnxX8ZZGgrijiALqNJgZSCwYitJpBc47fGWCDnvSMeyaZwxZWNbtKE8GJhBV7hXTUp2G6_uWetcghwuavUU1qCBzZCOolLg77G6sWLlQH_83N-LFIzkA9TdkytiLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الاتحاد الوطني الكردستاني بافل طالباني يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/80779" target="_blank">📅 15:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80778">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53048897d6.mp4?token=AzUMLLei3kS8b0eWh7n_eJacRfUopWXKQ7J-19NSdJjukdTCHAIYMYp3Zvgt2YFlxYxzCHhmUzue5ZPzwLckQeB4jiNGlmELVhTWozccSXMKdcbZQTsntjzAS2yiwVkK_NHDhGePMl8hi4miwgels5yRiTvWvngGietyVPkgAzvD4wYnpYvmNj9TaEI8kjMHdqAT5DJBECWH4usyDx3E9Mi0OkDgqXhx02BZrA-tUNlf2ROWXJHZCWMOkmjnMzKpmPZu44OODe4bsblyjH5Q7x2mza-5akUE8k5b8N7y3D4qvzy-z_vQMUojvMCjqE6WVzjthjXcdcU2lW26RidEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53048897d6.mp4?token=AzUMLLei3kS8b0eWh7n_eJacRfUopWXKQ7J-19NSdJjukdTCHAIYMYp3Zvgt2YFlxYxzCHhmUzue5ZPzwLckQeB4jiNGlmELVhTWozccSXMKdcbZQTsntjzAS2yiwVkK_NHDhGePMl8hi4miwgels5yRiTvWvngGietyVPkgAzvD4wYnpYvmNj9TaEI8kjMHdqAT5DJBECWH4usyDx3E9Mi0OkDgqXhx02BZrA-tUNlf2ROWXJHZCWMOkmjnMzKpmPZu44OODe4bsblyjH5Q7x2mza-5akUE8k5b8N7y3D4qvzy-z_vQMUojvMCjqE6WVzjthjXcdcU2lW26RidEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الجمهورية العراقي يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/80778" target="_blank">📅 15:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80777">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🌟
وزارة الخارجية العراقية:
وفد عراقي رفيع المستوى يزور أنقرة.. من المؤمل أن تشهد المرحلة المقبلة التوقيع على بروتوكول تنفيذي يضمن استمرار صادرات النفط العراقية على أن يشكل هذا البروتوكول خطوة انتقالية تمهد لإبرام اتفاقية جديدة بين الجانبين خلال مدة لا تتجاوز عاماً واحداً من تاريخ انتهاء الاتفاقية الحالية.</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/80777" target="_blank">📅 15:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80776">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dcabb0626.mp4?token=YNPvwhr-thbA7j7KH2-AWa91Vg-qjRwe5I92KY7pqiSE70J5iWVINlkoKhmFlRJa1IRAEv2eKSVJa5i0DEQRNTh3V0cq39F1fy6yDYAHdpGfzUd4sErzrYSx5YYnowJx0K2iPCFpf3Ee62o9bGA8f8GwEAwxUTQICjx9L9byLIBm8lFZhvOoOBsBOqobhqO6YSQovabfHmN8bhhBA7yFx84nJLY8uiS9h_genxvxgkpcMsK4sj8JsUd634ZJEHj6xDsO73epLez3HG6HM27qi5_yLg5kukgpM4rglwLGt9CkXQJH2-T4aj6ZpWJxZjz4R9qWQ8XqohAC_KBu9qCfAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dcabb0626.mp4?token=YNPvwhr-thbA7j7KH2-AWa91Vg-qjRwe5I92KY7pqiSE70J5iWVINlkoKhmFlRJa1IRAEv2eKSVJa5i0DEQRNTh3V0cq39F1fy6yDYAHdpGfzUd4sErzrYSx5YYnowJx0K2iPCFpf3Ee62o9bGA8f8GwEAwxUTQICjx9L9byLIBm8lFZhvOoOBsBOqobhqO6YSQovabfHmN8bhhBA7yFx84nJLY8uiS9h_genxvxgkpcMsK4sj8JsUd634ZJEHj6xDsO73epLez3HG6HM27qi5_yLg5kukgpM4rglwLGt9CkXQJH2-T4aj6ZpWJxZjz4R9qWQ8XqohAC_KBu9qCfAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد بنغلادش يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/naya_foriraq/80776" target="_blank">📅 15:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80775">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4a52e5368.mp4?token=N7m9vrDCEdxE6arrqSKl-liIspIzXGb8LZmm1cEwvMQsKbioBHUanGCK_4LrsMM-jkHOdtDE2ba70ZcHFVtnB6vnaHmbX3urv-cLDFB8nAoK1KwZy6ifdnkcZI-q3FFdWZhdFf2MapvmFka8bBaDJhXtGLYPc1rfpViHl4Dyd86ogrOOkBUpYbChSF1zqMp5396YKvOY2olpoS9urcu1qDWvRMPeJRgRbL8NAuURu_QOa5u8MuEpFaDMCvBcOQFKcmGzLqDorV1bSowry-lO7hMvt6sp8gU49w7ufK0x3zYGWFARcwSwGfiglHPXcNd3k_y55fJ0f_Cy6l3ZP2N73A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4a52e5368.mp4?token=N7m9vrDCEdxE6arrqSKl-liIspIzXGb8LZmm1cEwvMQsKbioBHUanGCK_4LrsMM-jkHOdtDE2ba70ZcHFVtnB6vnaHmbX3urv-cLDFB8nAoK1KwZy6ifdnkcZI-q3FFdWZhdFf2MapvmFka8bBaDJhXtGLYPc1rfpViHl4Dyd86ogrOOkBUpYbChSF1zqMp5396YKvOY2olpoS9urcu1qDWvRMPeJRgRbL8NAuURu_QOa5u8MuEpFaDMCvBcOQFKcmGzLqDorV1bSowry-lO7hMvt6sp8gU49w7ufK0x3zYGWFARcwSwGfiglHPXcNd3k_y55fJ0f_Cy6l3ZP2N73A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد طالبان يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/80775" target="_blank">📅 15:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80774">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e68ef245.mp4?token=nFjDSiYukMay1bD6pHpymzFh1evxMCjstct5H3tFW4M6pM3oaMAYcxMEzlXSU_WPutEtATmOH5RtL9SaWhDV7TgIYJeLZf13iGpjeWCISg7VB8B0ce8vfnJRJt7kInXyjz4q-oUeG3H9rcy6u0W9Yw0tz_5qYXB5bBUhNdsyLtZycOZ2WCYy2JfPfBDHGrvZYX7i1Gz4X6_qIUrlHRavmKU--Uko4JN19R5hMlyK5smTp5BOIR0Z_Ldy4oZeGNoJaMb6_2XG62h6nmiP-Ad742_HF-M6mp-wPdKw6a5BgCIkDLjVX7TrThvFhK1dKg6YbD3zDp_XxS3DCIHLTbS8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e68ef245.mp4?token=nFjDSiYukMay1bD6pHpymzFh1evxMCjstct5H3tFW4M6pM3oaMAYcxMEzlXSU_WPutEtATmOH5RtL9SaWhDV7TgIYJeLZf13iGpjeWCISg7VB8B0ce8vfnJRJt7kInXyjz4q-oUeG3H9rcy6u0W9Yw0tz_5qYXB5bBUhNdsyLtZycOZ2WCYy2JfPfBDHGrvZYX7i1Gz4X6_qIUrlHRavmKU--Uko4JN19R5hMlyK5smTp5BOIR0Z_Ldy4oZeGNoJaMb6_2XG62h6nmiP-Ad742_HF-M6mp-wPdKw6a5BgCIkDLjVX7TrThvFhK1dKg6YbD3zDp_XxS3DCIHLTbS8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل خمسة عناصر تابعين للجولاني جراء انفجار لغم بهم في مطار التيفور في البادية السورية</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/80774" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80773">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6962df27c0.mp4?token=sO2Xpnc7nYld5mWLSRMWtmTlknk1PRUipaat8HAhRBvMx7zjaFaLGfC4VHaGbSMYlrCH0cQexzP4TILXvRFQRdKD8KAS5ZjxLKDSTUxByDiLZzh-HQn4KgBW1f-7pE5FB7cIyfaFWCAAW0i0g2YA144-VH_f6eF9B9YBY8V9jEmsJEs0HgEOovZrKyT9qvYwakj8o2f1kNBKXp2kysSFgio8P7IpYDNf1M1YDXOrcE9dMBVl7y0pfm1kySQMEQ8Vi9B68Yo48yz0iNUz85AzeuFsb2EUBhnVYh38vljNbT2T4uFsq1erWaJ-UgxX2wWOthbhYkB9v1_91aZ93xNCrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6962df27c0.mp4?token=sO2Xpnc7nYld5mWLSRMWtmTlknk1PRUipaat8HAhRBvMx7zjaFaLGfC4VHaGbSMYlrCH0cQexzP4TILXvRFQRdKD8KAS5ZjxLKDSTUxByDiLZzh-HQn4KgBW1f-7pE5FB7cIyfaFWCAAW0i0g2YA144-VH_f6eF9B9YBY8V9jEmsJEs0HgEOovZrKyT9qvYwakj8o2f1kNBKXp2kysSFgio8P7IpYDNf1M1YDXOrcE9dMBVl7y0pfm1kySQMEQ8Vi9B68Yo48yz0iNUz85AzeuFsb2EUBhnVYh38vljNbT2T4uFsq1erWaJ-UgxX2wWOthbhYkB9v1_91aZ93xNCrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد النيكاراغوي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/naya_foriraq/80773" target="_blank">📅 15:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80772">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795d46a877.mp4?token=jqmwU7v56BL0Y_JGdu3ukaqSFVOD4xZVEratYTnevQ-w6DQxX4wC_IwWFRpFnC1oJkxEQRnmHMfC7XaBC5kXvyPBdpyLgFe0IyXkpJuxF2aF4H7PVQfWumZmOEM22nQkKRcyZDnLIxS_jEzo5mdbUBE67NCAlw_zXSyFYoMqypK-fIcqQJypgAJD62dU6s_n8L78BUGO01D6xKqxpOw6Q1lf-qn0w3bvydGpslOhCj81eyDC8EA-XAt9MlCBpwJX9vBUpebzSo1SxlDnH4yNnTJIMOfFH9bN4BUc7ebT7IFeFOCfpZD2KHxmIz35y609xvV_r0HiEgVhgkNltaoc9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795d46a877.mp4?token=jqmwU7v56BL0Y_JGdu3ukaqSFVOD4xZVEratYTnevQ-w6DQxX4wC_IwWFRpFnC1oJkxEQRnmHMfC7XaBC5kXvyPBdpyLgFe0IyXkpJuxF2aF4H7PVQfWumZmOEM22nQkKRcyZDnLIxS_jEzo5mdbUBE67NCAlw_zXSyFYoMqypK-fIcqQJypgAJD62dU6s_n8L78BUGO01D6xKqxpOw6Q1lf-qn0w3bvydGpslOhCj81eyDC8EA-XAt9MlCBpwJX9vBUpebzSo1SxlDnH4yNnTJIMOfFH9bN4BUc7ebT7IFeFOCfpZD2KHxmIz35y609xvV_r0HiEgVhgkNltaoc9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد اوزبكستان يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/80772" target="_blank">📅 15:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80771">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اعلام غربي: مشترين يابانيين يجريون محادثات أولية مع إيران لشراء النفط الخام.</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/naya_foriraq/80771" target="_blank">📅 15:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80770">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=pCvpA1D1G-cdwtKRxu6PCulSFRZ3gL_vX71UdSLQZ4oabuxZ8_6gs9bQp5RGKHPN1RfvF2zQhmAftJPiK21APNxMtrESVcksFYJtePCLnz315SU-Sym0E_BIKLlbmzrqDnhAkfg8y5LreynTx-AV2S8JqUDPKofy1-upTQhLly_lWHeihLWM42MnGRzpixPgQbjXCuJ68jckc4Ob5FW5MJBC8sye78-KfDsCOolC4x8ii2gcHlSj7lyYZPwh_ZM9UJq1YkPYGN3YhJ9MJiTUY64Lr10e98CroLqipJjzOeUgu_R6cSi0LWeb2rX9ct_RBqVdfUuYIhSQ9GbkAudx7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7de078a47.mp4?token=pCvpA1D1G-cdwtKRxu6PCulSFRZ3gL_vX71UdSLQZ4oabuxZ8_6gs9bQp5RGKHPN1RfvF2zQhmAftJPiK21APNxMtrESVcksFYJtePCLnz315SU-Sym0E_BIKLlbmzrqDnhAkfg8y5LreynTx-AV2S8JqUDPKofy1-upTQhLly_lWHeihLWM42MnGRzpixPgQbjXCuJ68jckc4Ob5FW5MJBC8sye78-KfDsCOolC4x8ii2gcHlSj7lyYZPwh_ZM9UJq1YkPYGN3YhJ9MJiTUY64Lr10e98CroLqipJjzOeUgu_R6cSi0LWeb2rX9ct_RBqVdfUuYIhSQ9GbkAudx7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد قرغيزستان يشارك في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/80770" target="_blank">📅 15:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80766">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo5EHO9n3dnk-9ngpio9C3wuiZ6BqNWpxTFxQ14rvSQtMug9dTZ9lpOLlzwDIdvKK0kOJOyDOs-AUwh62IxiuJjYHodoTQMBcvOALFeYBRa6eOWgrD6s2ecKNtvQ0G2bCQTotEFlZXI_WSW4LaIhEJe6C2C0MFCsAg-irTd9LV4LC-vP5ZC7oSFCcp6KGAxwiGGWOjetWmOInqyhVjaTU2oCbOPbwNYUg7zFnyRFKjUMuykcmGkRVJHjFuMe0bR55xmOq9wyr_fbLGBwtpw8YjbZcBkluHKT115k2WBQab19xXepz1qSG0szefsa1RIEwN-jhHtQyW4gIo2j0586rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6E4XySn8G_HuE1dsrwfCK74QG3L_bUvY9pS9L04nDKObf0P3TZXueRzlhsmQHt4Jg5YNxrtt0qyC8udt9g421mIFBJ-bXg5Mc4S1QPwbjjCqwgAevTV7bJih9NNLLc6vXRNBLxaZBnIq2k1fYju971S8QL-0h_Or3LVR0IJ5ygJN3mGR0UEFkjkz4keet9ZiXGBw9vqNYLq5gyIag-0NVVzKrVaDJzBDC4poIBHjEPem_-UYKQf1UPiFfVGW_NX7TKCKf38eNwkZYFIgx6h88ipiO1ETCDsxvnfdVSwXaCuLEytEsChvDrzFv3iEnOct8QtCqZtH6PiAkeLwnRkbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_eCH6Traf04675Bx--B9a9fYLWl2mrxURDeShVPAAKn_NUbeMFuLxs0OQNwpcmr27Ev33_7pdN_XgenxjgPWt-Ve8WxGWXTyCF5Ck0gTeVW596E7MIlsevTMJMqBR07qh-iYmjpY-69gx97nlwe1j0SLft41fLOFJN0y0zEPZOxDiLKNh3dSbYWx38yOwc__8ozYSub8DoHHarK-TnXhJmS_jyqyytoNhh4VUWQ3GThLDM0NiZmFPr9LgejV0SMiG0tLsQFd0-70pdf--DeM-IlrvMV5hXxLaD_UrH3atllA-LLBgpsMy3fCQeeQMG5iCI13rDHu4XThvRZNxqBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G08AhgpPJ0YMLZKqfaYx1QpMpUSm9IG0oQKRcp4kQpRj8DXjHSFBaL9s7Yd6xSPYuKXV9Sv3KEivg69wh3--GgAaKaMaKbhTGEgPDjHKrKFhmoQOk0gueAhMi8WjEL6P0ianFeT5iX3Otiu6rml70sTXjjNvAErAajzBv8N5V3YRN0A9dQJLjjKg723nX4eenvs9YhAUM9ylkPK5fF1zj-IbcW7WpcVl1TLKbngGZWHzjzMjP2UUPwvbSwsxE09QJQH80RX_UUC4zWcswGFCmt89uvRAyunSf8JMxJvzE10izZKa0Og8Yif0R6YSdfJ24XQxfzhyQwOoKAOSBKR1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الخطوط الجوية السعودية تمنح شركة ماهان للطيران الإيرانية خمس طائرات بوينغ 777-268ER عريضة البدن مستعملة ووصلت اثنتين منها إلى مطار مهرآباد في طهران  ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/naya_foriraq/80766" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80765">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الخطوط الجوية السعودية تمنح شركة ماهان للطيران الإيرانية خمس طائرات بوينغ 777-268ER عريضة البدن مستعملة ووصلت اثنتين منها إلى مطار مهرآباد في طهران
ادفع يا طويل العمر</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/naya_foriraq/80765" target="_blank">📅 15:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80764">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64825aa740.mp4?token=D3AYgBilgHu1C6EKXfx9hXvzIIDqqeZjLlVdydpjVdG0PZ6sbUNvItn_YBCMHxzJJas67pHyx01LyNYlzaiY6CsnkLk5tJl3WlzFkCLYh3jP0_cnJliGWwXwyXi3ddcYyFKASRMiegcqeHXnV9wHUs3hOri5bfIBPlJ9i5cQYUjkhtq2af_95JuA3_fsRfrtxMhL88aoYzn62xJvYAKTsr9B-FCPvyZ6khiWMHuWRjdThsljVNSG52GZ6rEmH8Ih_l0kiMEo1OboDvN3im2KFhBN6jSnrbrWa_E3RMbTGcFl7N1bbZNfgt-CrJwLR3tLlnVjUi9e_9gdtyd2Ymhevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64825aa740.mp4?token=D3AYgBilgHu1C6EKXfx9hXvzIIDqqeZjLlVdydpjVdG0PZ6sbUNvItn_YBCMHxzJJas67pHyx01LyNYlzaiY6CsnkLk5tJl3WlzFkCLYh3jP0_cnJliGWwXwyXi3ddcYyFKASRMiegcqeHXnV9wHUs3hOri5bfIBPlJ9i5cQYUjkhtq2af_95JuA3_fsRfrtxMhL88aoYzn62xJvYAKTsr9B-FCPvyZ6khiWMHuWRjdThsljVNSG52GZ6rEmH8Ih_l0kiMEo1OboDvN3im2KFhBN6jSnrbrWa_E3RMbTGcFl7N1bbZNfgt-CrJwLR3tLlnVjUi9e_9gdtyd2Ymhevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس اقليم كردستان العراق يشارك في مراسم وداع القائد الشهيد للثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/naya_foriraq/80764" target="_blank">📅 15:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=n7f0gt8u7bKlvqOTUxHJVdzs08VWCqtO9-5ord20pK8PugsOx6vgIZ9BipxImgCfBwM7_AVsfAAknvw2CcwGZ0jfFx1UhOMWf51DstSq_NDXKf_uHtYzePELR6p-IrFnUBFosEFAqnvDaIa53iKAWaZrIGaOlmGnPx90Yus92SL7sdVUzeCNtLlBWexs5_RDpgDt-n6Ksc9fqMr67m1G2_gktPU0mGTP0UX9iACjK90PeOVJM7NUsx1j-K5NTCi7UeKN4ofIJO6jes90qhZ4__X9qMhgVmToBSfPmEvhyGVVJjxMB7TTGAtxrlok8BvFMhUrSlMCGFunNqAjni1nDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db9faf02.mp4?token=n7f0gt8u7bKlvqOTUxHJVdzs08VWCqtO9-5ord20pK8PugsOx6vgIZ9BipxImgCfBwM7_AVsfAAknvw2CcwGZ0jfFx1UhOMWf51DstSq_NDXKf_uHtYzePELR6p-IrFnUBFosEFAqnvDaIa53iKAWaZrIGaOlmGnPx90Yus92SL7sdVUzeCNtLlBWexs5_RDpgDt-n6Ksc9fqMr67m1G2_gktPU0mGTP0UX9iACjK90PeOVJM7NUsx1j-K5NTCi7UeKN4ofIJO6jes90qhZ4__X9qMhgVmToBSfPmEvhyGVVJjxMB7TTGAtxrlok8BvFMhUrSlMCGFunNqAjni1nDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد هادي خامنئي، شقيق القائد الشهيد للثورة: الشهادة كانت الأجر الأمثل له.</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/naya_foriraq/80763" target="_blank">📅 15:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80762">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ab2eecaf.mp4?token=Ydrn1Wah5UC4hgYsOpla82BrkwPcJu2aAOA62V8m1TBvXcC-j9RT7fleT11ESoSnA0Qmxmmuo0xstej1clXIPLZa0DUUfqVLQtIbKWPbCPAl-S6Vn23gPnBJR_xe7mryxzTB5waD_LGvhuRM4Ne0wc2sLaTCEuS5pqoFzL5iWJtxh7QPq59Uv9rzKE_UlU4KglVJBmZLV5T-qAcrvfVxuAZc874-AjSZhcOtrDcdDmIxFEKcIuKT9SXyNVDGHuV-bEhFrqDKl854_SmrKYorMrkcsFCFjpdvtSgErNzFkeeIc4oyRJymWdwMx482rrs0TyEO_FStMDr4AAAf9pwukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ab2eecaf.mp4?token=Ydrn1Wah5UC4hgYsOpla82BrkwPcJu2aAOA62V8m1TBvXcC-j9RT7fleT11ESoSnA0Qmxmmuo0xstej1clXIPLZa0DUUfqVLQtIbKWPbCPAl-S6Vn23gPnBJR_xe7mryxzTB5waD_LGvhuRM4Ne0wc2sLaTCEuS5pqoFzL5iWJtxh7QPq59Uv9rzKE_UlU4KglVJBmZLV5T-qAcrvfVxuAZc874-AjSZhcOtrDcdDmIxFEKcIuKT9SXyNVDGHuV-bEhFrqDKl854_SmrKYorMrkcsFCFjpdvtSgErNzFkeeIc4oyRJymWdwMx482rrs0TyEO_FStMDr4AAAf9pwukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الباكستاني بقيادة رئيس الوزراء وقائد الجيش يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/80762" target="_blank">📅 15:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80761">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPm85U35oVYFmwa20SWbx6I54WGhFi2hBUP8KoFouEcL1tNc6fA7N38_cMB_MP5Zk4H-RuwVtfOGbMPzk2gvpku12p2PRmd90pCS0cBF7QoVd_5XO2peg7rkNeGcGdqLIFTcy8NmzPuwOH7r6YicTjYrRZJn3LAO5ZWecOm0ghcxb1n9iPNbeXk6ybPhHHU-L1YDEgmvDF850BMjzFXXzZqT5NI-ir0Nfk1jiq70IawMvOKmi9AWVtW7nHaPuFFVBuEBZaqt0WiN4S2QeEN7OUIVp5gN08A7bGruht3DEiQjgF8w0K3T2lSYfjPYIRXc5ZEII1dTIgsMr_p-VcJJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس السلطة القضائية الايرانية يوجه رسالة إلى القادة السياسيين الغربيين:
افتحوا كتب التاريخ، الأيام القادمة ليست مجرد مراسم تأبين؛ بل التاريخ في طور التشكّل. عندما يملأ الإيرانيون الشوارع لتكريم قائدهم الشهيد، لا يمكن لأي إطار أن يحتوي على حجم التعلق والولاء الذي يكنونه لقائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/80761" target="_blank">📅 15:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrDERSv3NuP0g1xGozIMjpH89Aioi3CM7rLoNqDaGUsXlMQatAFhmZnzv30qU6X3NufFWhRDLAI72Q0tZ1AMM19eKGDy7dOJ5KxgpQ5qHuWBQmxge-Hx2BjxJof87AckYLyK8VUajO4KR-gmTkF6XUvLz_mSRx6diqxBWoIp5buX76f1Py7kT0_lYLg67T0obckwELxkmz_lxz2xttZ7Ih8GZWQB-rrtxRRBe5o0ofPoDqHanw-4gpoZ812z_ROxtVn99VPaJEgHcJtao1j-Fg9DU8C5PmKW075u9DHX7ZyRGYrBqf2ExM6X_9KgFStXfGptL71t4GJ1vYwS5Kpusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرتين روسيتين من طراز إليوشن Il-96 Il-96-300 تتجه الى طهران.</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/naya_foriraq/80760" target="_blank">📅 15:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80758">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LaRxvMGd0cd7_Z8TyZY-tXYwOrJky7BueWnEEfTW5BT15LWy0xJ9t1bdS6pcVyyFeOvM7LF6Jln1dZD7WWtnOj8WRnkwNaPMw98xuVARhy-WACwUaPCR0ryC7tll_zE42Xr3ppZ_gAX3NgvHxNVWy1P-z_L2ooJtWh3w-CfzvlPVFngBQ_W9AFMOcLeFws4cL9enoJMo7TEV35Sj4JUu-HhEwoF-vLtHl-FIp2riIFr2h2bEM6PYrUuMd9fyJzdOKqtLRU5y1Shdn8smoYyFOX08SX4rG5VyTJyZSkA0EDjMAX07ym68hTzFkCozGli2A--W2yW4aa3TRQ9kyWVmrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mG17GXvvxLU5IoACp2OjFAmzqOcl19gEY_P7Lqp5s24ONDtuebtURYKeiBLIlbMiprYbnCQCCtCFJcoskoj0OykTuQ0Vkqd-jWkfu7CzMAePmRAfjy6cfv7o1c5F6qiLE6HWE1KastJ1lhe-7HT_x1HfyrQHFWz2XoFwUKerrmZhAt1hbXkUW4N31QFDhVrxKRU18QkCsdbqFqPFw7ue3ZNfMOcSZSm-MdGzZ_Jdokyxzgo12Z0h6xMbYYIAr_-ctUDxUVhr8fmWNwsW2ucLSOt6vH-YaCSWy8CyJYD_Qfo4EehDQ0r64-Evep1sbfIPTeTLml32OtaUbiiug-mJ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور علماء أهل السنة في مراسم وداع القائد الشهيد للثورة.</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/naya_foriraq/80758" target="_blank">📅 14:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80757">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3391779aa6.mp4?token=mCXnx6JUuItO0jqBl4cRS4klE9rutloBCOzlLB6CRk-itH_NULdXMX3oxGkl_2eCQ017PjNsaJ01EqgWiAc2uM24tuvyf47E_dyiUb6doaUO3yfdLRhwVtmCEIMIiB8x9pmxZk8LUr7hWmwRh8ZTMRvZCgv9MBwKA8R9GrNtl_FsDTF6bmIp-bJe9QqR0RRNOdR1wbiGQTCtnX0CgxdkPN4kL4vweIGyflmdT3oByTrBOG_t0hJyRLxZ2oBLFG5N3eCeRzwySgXyLWiXvoA4iutxvMSZveQgoXfn3VlqOEpKKE2D5-QoMd3eRpQQIFxPrEWSICd7XFMiqGhguiQ6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3391779aa6.mp4?token=mCXnx6JUuItO0jqBl4cRS4klE9rutloBCOzlLB6CRk-itH_NULdXMX3oxGkl_2eCQ017PjNsaJ01EqgWiAc2uM24tuvyf47E_dyiUb6doaUO3yfdLRhwVtmCEIMIiB8x9pmxZk8LUr7hWmwRh8ZTMRvZCgv9MBwKA8R9GrNtl_FsDTF6bmIp-bJe9QqR0RRNOdR1wbiGQTCtnX0CgxdkPN4kL4vweIGyflmdT3oByTrBOG_t0hJyRLxZ2oBLFG5N3eCeRzwySgXyLWiXvoA4iutxvMSZveQgoXfn3VlqOEpKKE2D5-QoMd3eRpQQIFxPrEWSICd7XFMiqGhguiQ6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الطاجيكي بقيادة رئيس الجمهورية يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/80757" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80756">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZwW7TjJTcYCWBc2vJOw_-hr-mXg_5p-obrsFdCbY8LNagLk2FOxF_daQruiM-zGHO4hJCkNd4blBNrF9emUqScw_FjY0awk9JKSzr3SyZuv6-xuDddkwtiT2zB1fYZKyZLSBWZV9Q9p03mbqLYeT6YEAq4au_dgGHz3tgKJpv2x_wj8oNetfI2MFjaWOkbAMxGoWqCItuS31ziL_JZnArFLIg-vWTxmGrukb1z6Bx0jf1sLY7X8dpec7zFp_S1XirTdyYPkq_ft266gMGgjQAq41hyfgCCtt1vg8oeI--6FkcXmfW8GM-v4-dDfVrYVuHPduCV0GiedYoqu6OPubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجمهورية الاسلامية تضع صور شهداء مدرسة ميناب عند مدخل القاعة التي أدى فيها المسؤولون من الدول الأجنبية احترامهم لجثمان القائد الشهيد، في مصلى طهران.</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/naya_foriraq/80756" target="_blank">📅 14:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80755">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe5996e691.mp4?token=LYU-8GusugkaqYBKJeECBxvRYtXPkCUCOLyWIHBngmYVt7hgUM383JuEGsjBdv1Li64WJMxPFfbqefc7ZTAMNbWuK4RuFK3N9bfs62Iid94SE5op48M79o2CifBrUZJ2bzneOMAuXKihZoXzuMTIB-BmOwhA47YlKkXfxdJn82r6hruU1RJTgrceXEc6EN7QPttg6ZS3hbl9clKcpyqnDD8DL8BM0WNyOLouxJWzMnsrvnKzmEdtONnaWIfxZhVIf5ZibvTz8FYpzXPDaqlQiZiDjPlGPakTVIwSOFYWPdYLTqVXvWv59qNKF2-hz8DSCerw0NfmeTSszOkdWTEPmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe5996e691.mp4?token=LYU-8GusugkaqYBKJeECBxvRYtXPkCUCOLyWIHBngmYVt7hgUM383JuEGsjBdv1Li64WJMxPFfbqefc7ZTAMNbWuK4RuFK3N9bfs62Iid94SE5op48M79o2CifBrUZJ2bzneOMAuXKihZoXzuMTIB-BmOwhA47YlKkXfxdJn82r6hruU1RJTgrceXEc6EN7QPttg6ZS3hbl9clKcpyqnDD8DL8BM0WNyOLouxJWzMnsrvnKzmEdtONnaWIfxZhVIf5ZibvTz8FYpzXPDaqlQiZiDjPlGPakTVIwSOFYWPdYLTqVXvWv59qNKF2-hz8DSCerw0NfmeTSszOkdWTEPmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد البيلاروسي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/naya_foriraq/80755" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80754">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a80961d7a.mp4?token=KV7GIxwkdZ6neWhcW1_G6lANi00gmD3sVf-a-TQVFhFPBiAm7udYEg5iFjimSGeIoxX23gAd8LjKf1rRBQFmFxiKAPIwNGoIbT1ypTXnKmYybIrOqCA_nYWtP5U0VSflqWX1ibXU67frBScJ01lqQcx6LrwSsMZZy8sjeaL-1t8_ZMUy3N7W23w0n7q-vfLqg96mW94GcCPufokkLcgZIh-kmAkKsoiVELlyvxBxbtUikCPbc7L8b_9U7mgRLYYxFMvw-ByAIp-khoiKWHB304vzUPItpXAa04V2bcMeb8YLGmw4LCK2Zf0IWpEv31FdSHDpWel3oEr0brhbLpzW6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a80961d7a.mp4?token=KV7GIxwkdZ6neWhcW1_G6lANi00gmD3sVf-a-TQVFhFPBiAm7udYEg5iFjimSGeIoxX23gAd8LjKf1rRBQFmFxiKAPIwNGoIbT1ypTXnKmYybIrOqCA_nYWtP5U0VSflqWX1ibXU67frBScJ01lqQcx6LrwSsMZZy8sjeaL-1t8_ZMUy3N7W23w0n7q-vfLqg96mW94GcCPufokkLcgZIh-kmAkKsoiVELlyvxBxbtUikCPbc7L8b_9U7mgRLYYxFMvw-ByAIp-khoiKWHB304vzUPItpXAa04V2bcMeb8YLGmw4LCK2Zf0IWpEv31FdSHDpWel3oEr0brhbLpzW6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الارمني بقيادة رئيس الوزراء الارمني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/80754" target="_blank">📅 14:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80753">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0a7346f1.mp4?token=INSTT7qSrMGFBi9KsYVcvKmHFgaMCq1SoUvb14hcqiRbNeg_OJYIH5oX0rpUWtHhmT2HOstNZw7CSpEExYWTrCU_R9nBKLQZVHApdsqHafNZDex0eBfT02pLq1JbqG1CiSuIRAMs1A9zozk6p6kZgbHoJjsVwfGk2xvmmA4D3YMNzM5BALKiEogM8Nb7Ag8PBkAJfnofEyX1C6B5zjwil2UfY8bxAkIVC5McMHD2nCKMCSoUvE8THeVkKx5uLoBIYy5cX7RWg70XHAzJAz7B7dLKEtHuPBx_RWQ2e9qZZKrLzs8_nWI06d5XpK94lZSFl9WXUKh8-KQ42YvPdyco2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0a7346f1.mp4?token=INSTT7qSrMGFBi9KsYVcvKmHFgaMCq1SoUvb14hcqiRbNeg_OJYIH5oX0rpUWtHhmT2HOstNZw7CSpEExYWTrCU_R9nBKLQZVHApdsqHafNZDex0eBfT02pLq1JbqG1CiSuIRAMs1A9zozk6p6kZgbHoJjsVwfGk2xvmmA4D3YMNzM5BALKiEogM8Nb7Ag8PBkAJfnofEyX1C6B5zjwil2UfY8bxAkIVC5McMHD2nCKMCSoUvE8THeVkKx5uLoBIYy5cX7RWg70XHAzJAz7B7dLKEtHuPBx_RWQ2e9qZZKrLzs8_nWI06d5XpK94lZSFl9WXUKh8-KQ42YvPdyco2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سائحة امريكية تتعرض للضرب على يد عصابات الجولاني في محافظة حمص السورية</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/80753" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80752">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e8c7e0e1.mp4?token=jKPrCoXgMplS-YDCejh4qZBArzVxtffZTtFHVltPVkAmM1JUZTWUQNWvCfQu15-6ABDAbJ3-l0HRPPzc4QHTHHw3sc8qv5EopPoyLj97D2fbXch5ngtxd7fNO3wd2Ko13Wd7tIevcdF8_-4Bk8c_moWzApgU_ShAsLnMliDCYfTpinAMBAeXWzPCDZpqUSyAqZCh8p9AbSkSItbDouMAGUORjQ55gNBmBiQUAbM8snC-DmUPqzWdHPGiMHbZOQWjDLqapLe5EaviZ4jPjI0QjccRkusUN0kgIBGoUW8JzCfwf3j8ShEvi73ri81cz1JCss63Dsk7_HqOJVpMFCGFUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e8c7e0e1.mp4?token=jKPrCoXgMplS-YDCejh4qZBArzVxtffZTtFHVltPVkAmM1JUZTWUQNWvCfQu15-6ABDAbJ3-l0HRPPzc4QHTHHw3sc8qv5EopPoyLj97D2fbXch5ngtxd7fNO3wd2Ko13Wd7tIevcdF8_-4Bk8c_moWzApgU_ShAsLnMliDCYfTpinAMBAeXWzPCDZpqUSyAqZCh8p9AbSkSItbDouMAGUORjQ55gNBmBiQUAbM8snC-DmUPqzWdHPGiMHbZOQWjDLqapLe5EaviZ4jPjI0QjccRkusUN0kgIBGoUW8JzCfwf3j8ShEvi73ri81cz1JCss63Dsk7_HqOJVpMFCGFUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد الاذربيجاني يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/80752" target="_blank">📅 14:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80751">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لجنة مراسم تشييع وتأبين قائد الثورة الشهيد: سيتم فتح أبواب مسجد طهران الكبير أمام المواطنين غدًا ابتداءً من الساعة 6 صباحًا.</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/naya_foriraq/80751" target="_blank">📅 14:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80750">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لجنة مراسم تشييع وتأبين قائد الثورة الشهيد: سيتم فتح أبواب مسجد طهران الكبير أمام المواطنين غدًا ابتداءً من الساعة 6 صباحًا.</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/naya_foriraq/80750" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80749">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رئيس البرلمان العراقي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/80749" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80748">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbbcf836c.mp4?token=p12dCtJMkwnu3-09cBedid0kvtxjZMIIvQ3J14ZPr3ftctQrS_be4IIyVTI5z9PyoTH-qKXeobeIjniXnTjTiK31RUdR83caS-CAmV7nZ-JSELfsCv23lJejwcHL0UiIsFygzKBv6DWI8ukoIa7-o6qmA1lIJym0OZ__Oa41P-vLwfNHvvZrRBuu8Lhw6wiGPVWNtJSh-Q6ANj4_8AGeO_nDJ8LGFEqwzMFzDntaoCMhsNzeo1Q74tmzpBcoikUpkmQ7Re59WzJ2ATps3Mk61fCdG_7oVlrgIbDbV-RG78DMzrdrgHUTRbpwXjll1SApbZFRWnlTixuGNBasgxaN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbbcf836c.mp4?token=p12dCtJMkwnu3-09cBedid0kvtxjZMIIvQ3J14ZPr3ftctQrS_be4IIyVTI5z9PyoTH-qKXeobeIjniXnTjTiK31RUdR83caS-CAmV7nZ-JSELfsCv23lJejwcHL0UiIsFygzKBv6DWI8ukoIa7-o6qmA1lIJym0OZ__Oa41P-vLwfNHvvZrRBuu8Lhw6wiGPVWNtJSh-Q6ANj4_8AGeO_nDJ8LGFEqwzMFzDntaoCMhsNzeo1Q74tmzpBcoikUpkmQ7Re59WzJ2ATps3Mk61fCdG_7oVlrgIbDbV-RG78DMzrdrgHUTRbpwXjll1SApbZFRWnlTixuGNBasgxaN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس البرلمان العراقي يشارك في مراسم توديع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/80748" target="_blank">📅 14:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80747">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة مراسم تشييع القائد الشهيد:
هناك احتمال لتغيير المواعيد؛ فمع أنه أُعلن رسمياً أن مراسم الوداع الرئيسية ستبدأ صباح السبت، إلا أن أبواب "المصلى" قد تُفتح أمام عامة الناس الليلة إذا كان ذلك ممكناً.</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/80747" target="_blank">📅 14:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80746">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo71ZhiU6V5afsFifru_NapO_y4Gfx4h_gNaEOPHbfre_V2Qq-w3qCKEyGsvMjuT282pOr06RT-V4_2o3D0bHXtkKnJrK_u_ZiwJzE8Lupj6_C2fzV13cYNijRWY8BnL4Rc8sDxmtawANjHmOvsLlh7aFOWL-VvfwA8y_sfdhO_3EzCYxUzooMamIBL-XPUOY8QOzsa4X-AU5Wo8idA8tXE-XCKUh8XiINr7pvHa8kyBTpOwX54YIJdWKmQ5Fbk0wG6At7rdmVSUHkDFHF3IF-AUFVMIgZQzF6YdQL-mBCvN2oav_iSXvhgjBYsYBqrW9xga2yaNOHhCKeJeTl2V6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
نسأل الله الصبر لكل المحبين
يوم الأربعاء
النجف الأشرف ٦:٠٠ صباحاً
كربلاء المقدسة ٤:٠٠ مساءً
#قوموا_لله
|
#باید_برخاست
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/naya_foriraq/80746" target="_blank">📅 14:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80745">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🌟
الاتحاد العراقي لكرة القدم:
تشكيلُ لجنةٍ للتفاوضِ مع مدربِ المنتخب الوطنيّ الأستراليّ آرنولد مؤلفة من رئيسِ الاتحادِ يونس محمود ونائبيه من أجلِ ترتيبِ الأوراق، وإكمالِ عمليةِ التفاوض بغية استمرارِ المدرب مع المنتخبِ الوطنيّ
المكتبُ التنفيذيُّ للاتحاد يوافق على حلِ جميع الملاكاتِ العاملة مع المنتخبِ الوطني
العمل على الإعدادِ لمؤتمرٍ خاصٍ بالمتخصصين في كرةِ القدم والأنديةِ وأهل الشأن للخروجِ بتوصياتٍ ومقترحاتٍ تهدفُ إلى تطويرِ الكرة العراقية
تشكيلُ لجنةٍ لاستضافةِ بطولةِ غرب آسيا للناشئين التي تقام في 24 اب المقبل في العراق ورفعها الى المكتبِ التنفيذيّ لغرضِ توفيرِ جميع مستلزمات نجاح البطولة
السَعي إلى استقدامِ مديرٍ فنيٍّ أجنبي يتمتعُ بخبرةٍ وقدرةٍ عالميةٍ لتطويرِ ووضع البرامج الكرويّة الهادفة إلى تعزيزِ قوةِ الكرة العراقية من الجوانبِ كافة</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/80745" target="_blank">📅 14:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مصدر روسي لنايا : المجاهد الكبير ولعنة الناتو دمتري مدفيدف سوف يشارك في عزاء السيد القائد في طهران</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/80744" target="_blank">📅 14:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd34ffceb.mp4?token=huK0_tb_xk8_x6DcejHhZaYEo7NezKQS7gVBgga7z350c8a3_NFOZl4YBv0AJU5oFZBLD2Ng1LXPN2z21WJFs_7fpBGSbjH2K5cjZmpcHWo45LOoMLlmftf1GrgO6pHSQJH8sO7A16LRetsDq4MqEBFvA1iEXO4fmR5IoEqukWQofqhv8kTSXJoiDIT3ao64p-tVb6gVI-LgOLenTv9JTB8bDaKlOU_o2OFrp8DS2g31fafHrBq8Getd9vpjMIlLs7F74qj0KqGngfS_W3jKjUQNYKOZ4nc4mHSicO4lc5tP7_h1qXhQK5ylmUR0IIJC8T8uQzR1RmxEP0pgkpnlpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd34ffceb.mp4?token=huK0_tb_xk8_x6DcejHhZaYEo7NezKQS7gVBgga7z350c8a3_NFOZl4YBv0AJU5oFZBLD2Ng1LXPN2z21WJFs_7fpBGSbjH2K5cjZmpcHWo45LOoMLlmftf1GrgO6pHSQJH8sO7A16LRetsDq4MqEBFvA1iEXO4fmR5IoEqukWQofqhv8kTSXJoiDIT3ao64p-tVb6gVI-LgOLenTv9JTB8bDaKlOU_o2OFrp8DS2g31fafHrBq8Getd9vpjMIlLs7F74qj0KqGngfS_W3jKjUQNYKOZ4nc4mHSicO4lc5tP7_h1qXhQK5ylmUR0IIJC8T8uQzR1RmxEP0pgkpnlpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد التركمانستاني يودع قائد الثورة</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/80743" target="_blank">📅 14:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80742">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXCzXYm7SysS-R9UaEYtJIkIVmd6hrozWUe8LCawihjzl7b1culBm1kX6M3Zr8z5X9xRyeVD3groChhWa_J4L7M-bn6rWrW8TDShGPE2oYoce_bDVJc0BDqdq3wio53c2njGBDvAPsjbtvYRjON3BO68Zka_EHkQTQGMQ_1kuryS_qHFjUN0OGBV6H40HY4alXwXnAWU8s154SgJZhTw_auZHPZrblLhYMXq2n9PmgqPomWyxLGY5_-2wn-SO0VpSRnmcNqB5Es0cPExr2Sb8Lscvhi0sIHOAGyEl9YWsABo8ZymqIvbXfSoLXCCZQTF-ElHICxgCNQRl_BCKcSA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشيخ اكرم الكعبي: المشاركة بتشيع الجثمان الطاهر للسيد الشهيد القائد الخامنئي (قدس سره) لا تقل عن المشاركة في محاربة هؤلاء الصهاينة الأرجاس في ميادين الجهاد.</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/naya_foriraq/80742" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80741">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5587a3fe4a.mp4?token=C0oUvGk4CPZNZfjRS2V9eqZNPke_uxQssmXLVc0jbbgCwr0LBjYvvr8xtI-SrB_sceA4ubHeCD9y77d3v_wnKIsHh8uFH59jLBl6MdMMkBVxmiE9Dah26AYJaylq6E4HVFn5cIqFr_l8WWkXLylml_kcgsbS83FhKg95PCxShMg1s3qpZayHc-Bl3fddUo1zUtTdCsYGc__8jSYg5urQoJ0hw3ZeOBS05qpkrnj2SlBRb0mY549BCqaKeZ5hAZ4qLf2bVjhJ8cgzO3tNpdwFpDEL5-9aFyCdc3Htj1WEqbIZM5aozvRnJ8R3RHt3FjATxVkIc57Atb9ckgBN1EKOMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5587a3fe4a.mp4?token=C0oUvGk4CPZNZfjRS2V9eqZNPke_uxQssmXLVc0jbbgCwr0LBjYvvr8xtI-SrB_sceA4ubHeCD9y77d3v_wnKIsHh8uFH59jLBl6MdMMkBVxmiE9Dah26AYJaylq6E4HVFn5cIqFr_l8WWkXLylml_kcgsbS83FhKg95PCxShMg1s3qpZayHc-Bl3fddUo1zUtTdCsYGc__8jSYg5urQoJ0hw3ZeOBS05qpkrnj2SlBRb0mY549BCqaKeZ5hAZ4qLf2bVjhJ8cgzO3tNpdwFpDEL5-9aFyCdc3Htj1WEqbIZM5aozvRnJ8R3RHt3FjATxVkIc57Atb9ckgBN1EKOMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول رئيس الوزراء الباكستاني الى طهران</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/80741" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80740">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6906509da4.mp4?token=QL_PTa7KWyzDYoQYaleR7XXNOEN-2gpcoQ9_uKJvQlW8qdIyVOwI_QFa0j12VDeMBvmrecB-79BmAegHwoXVawQzo7MYwJ--unEAciriHJciBWJW3-pCU5wRZUiyV_J5XLFDwbMn2MGcEA6miZt4EGPl_ewDNhY9atU7DqbvhcJS4ihDKEEe8XIQTv8qGP7DEqfxv_1Xe0MEA48CHPWCE1yakp4YCEQdMq5PP_RAlwg98a6CbuSX_W1R3UWeCBrwC5cYPI3P0l9THK-Iyp2KHNpA06xnb1zczz_2CiP9lXzWjuoIguag08i33KOYlHB7NshpUaz1GdCd72CVWpf_GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6906509da4.mp4?token=QL_PTa7KWyzDYoQYaleR7XXNOEN-2gpcoQ9_uKJvQlW8qdIyVOwI_QFa0j12VDeMBvmrecB-79BmAegHwoXVawQzo7MYwJ--unEAciriHJciBWJW3-pCU5wRZUiyV_J5XLFDwbMn2MGcEA6miZt4EGPl_ewDNhY9atU7DqbvhcJS4ihDKEEe8XIQTv8qGP7DEqfxv_1Xe0MEA48CHPWCE1yakp4YCEQdMq5PP_RAlwg98a6CbuSX_W1R3UWeCBrwC5cYPI3P0l9THK-Iyp2KHNpA06xnb1zczz_2CiP9lXzWjuoIguag08i33KOYlHB7NshpUaz1GdCd72CVWpf_GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس البرلمان الإيراني السابق غلام علي حداد عادل يودع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/80740" target="_blank">📅 13:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80739">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYne25Fq3ACaWf3XcTEbbGT-N-hjz2_sK9uWIrdUNcnBsHQce2xA9E2yp4Ye1kHIWY79EYAi8jDl91FKpv7uf-tjuYCG9lO-uU5UOoL9CwVDXDWqz1WXYcrCPsq-ig1xLqULxcM0pkyn9mOSoXwYQeUGQqosstDF93Apls7gmzfzkJLwNT-NpWaViqo5t3WHlwQ8ilhmWgXIf1Ns5VciGjr4PIkgXaTh5cs6uddlaf1zl5ou2cGj0Kwk25vte2A8GZeqwctFw9VXGSlO2CeH310zEa7pLXaSqQI3O50vXOkrExc6YUpynQ1vY9QyzhUfW8epMbNGTJ4aOfHgy3xUlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من وصول احد اعضاء الوفد الباكستاني</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/80739" target="_blank">📅 13:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80738">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b419c1671.mp4?token=oXIaMKDmPS-cvhhW0qVltUWpraV4gphWFZlExeMpy6ESij5gPk6InJEsdoGv5fRAXjRWiNWtWl6ukbqSD1fwOLGPbuw4qAR4RsPAljLY0kDNnWfR7Lg7XLYhq5mo2Vv4vHMReENNe2-fyFsGkdQPCWnt5dU9rCM5jrd3vEKQTgt1f8e4PuGHMzZcNnY-2JAgSZepioaUOMP7JPec1GIYKMWOvoIfI38IkAr-9WQCdsnoAAcbg9i2AKtoy60EHRP36YXgugAjTVFJ-YBcBo1Ypf3AGp6osMjlF2ZHVNW5Z-IR9qe5OFIIx9ZE9Lk-VsJBxlrBjfQ2K0kAAap14c7MBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b419c1671.mp4?token=oXIaMKDmPS-cvhhW0qVltUWpraV4gphWFZlExeMpy6ESij5gPk6InJEsdoGv5fRAXjRWiNWtWl6ukbqSD1fwOLGPbuw4qAR4RsPAljLY0kDNnWfR7Lg7XLYhq5mo2Vv4vHMReENNe2-fyFsGkdQPCWnt5dU9rCM5jrd3vEKQTgt1f8e4PuGHMzZcNnY-2JAgSZepioaUOMP7JPec1GIYKMWOvoIfI38IkAr-9WQCdsnoAAcbg9i2AKtoy60EHRP36YXgugAjTVFJ-YBcBo1Ypf3AGp6osMjlF2ZHVNW5Z-IR9qe5OFIIx9ZE9Lk-VsJBxlrBjfQ2K0kAAap14c7MBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عائلة الامام الخميني تشارك في مراسم وداع قائد الثورة الاسلامية السيد الخامنئي</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/naya_foriraq/80738" target="_blank">📅 13:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خلية الإعلام الأمني في العراق: لا حظر للتجوال أثناء مراسيم تشييع الشهيد السيد الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/80737" target="_blank">📅 13:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80736">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خلية الإعلام الأمني في العراق:
لا حظر للتجوال أثناء مراسيم تشييع الشهيد السيد الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/80736" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80735">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66cfc76b5.mp4?token=L1gS8lCBsm7Ao0epGzqe3zJhgDfRuT8FwWHPyPr1IJGOeaIxdX4Etq4uqC610qMfeyD56KrtQGzmpUvD1Lq8WaOJwRyFRetgz7IjM6hPZeQKhxqBwE0MBVdMEKxxHkE5Cx-xd8vi_iqhBYb6obT3NqLry2x18APOauEogqe08iPKOljuhrSyOXpN0HcBAItsK_pOr7e6wP9l34V6pGTfX7FrjkOEw4f2nMXNU738imIY5UzR25afZgZVsSMS-mxx-Blp-pIWuW_zk4hsiSSm5S97j7a5jWqJ1rM36sELuqxKkrGnFnjmWcyBf_gaa1woUaFLVu7C-cD7XEWudOuJ4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66cfc76b5.mp4?token=L1gS8lCBsm7Ao0epGzqe3zJhgDfRuT8FwWHPyPr1IJGOeaIxdX4Etq4uqC610qMfeyD56KrtQGzmpUvD1Lq8WaOJwRyFRetgz7IjM6hPZeQKhxqBwE0MBVdMEKxxHkE5Cx-xd8vi_iqhBYb6obT3NqLry2x18APOauEogqe08iPKOljuhrSyOXpN0HcBAItsK_pOr7e6wP9l34V6pGTfX7FrjkOEw4f2nMXNU738imIY5UzR25afZgZVsSMS-mxx-Blp-pIWuW_zk4hsiSSm5S97j7a5jWqJ1rM36sELuqxKkrGnFnjmWcyBf_gaa1woUaFLVu7C-cD7XEWudOuJ4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تركيب تمثال "قبضة يد مشدودة" في ميدان انقلاب في طهران تجسد وضعية يد الامام الخامنئي في لحظة شهادته المباركة</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/80735" target="_blank">📅 13:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80734">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87b6d075f.mp4?token=UpFqBrACMbRQcgE65IGFfIXGWgUqqEH8Tr8_khWBC1siplddGCvCpT3JuH9axD4t4b-dZxazIkhy66ZeyEhdR5bC2VYIDVxRpaFlDHuxBZdeIVPimz40VpagupKG07lxM_FOQU8TDRHT3laoQkrk2a0dbQQcD3atEdiJ-qGCdBExzFLCkygmgra8Imzck3nUupXrz79zaZ0P3NhZk1X45O0XaPe_mdoP63Hj7B-9IuC1blhZx9tUUVcnw--9X7_cW5ynb7Y9_Un21PwDQYCTCslAKofWJ_Enxt7jyVmlLwYc2-2sWupjpt7MzrYLESUYNMMQpyrGWnQWo03n1GqZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87b6d075f.mp4?token=UpFqBrACMbRQcgE65IGFfIXGWgUqqEH8Tr8_khWBC1siplddGCvCpT3JuH9axD4t4b-dZxazIkhy66ZeyEhdR5bC2VYIDVxRpaFlDHuxBZdeIVPimz40VpagupKG07lxM_FOQU8TDRHT3laoQkrk2a0dbQQcD3atEdiJ-qGCdBExzFLCkygmgra8Imzck3nUupXrz79zaZ0P3NhZk1X45O0XaPe_mdoP63Hj7B-9IuC1blhZx9tUUVcnw--9X7_cW5ynb7Y9_Un21PwDQYCTCslAKofWJ_Enxt7jyVmlLwYc2-2sWupjpt7MzrYLESUYNMMQpyrGWnQWo03n1GqZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئاسات الايرانية تودع قائد الثورة</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/80734" target="_blank">📅 13:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80733">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff15d4aac9.mp4?token=ZscPMoULahwfkzqBcm_1N30mMck-PvoA45IxcItBNCs-7MsQvDKaZxEk5A-BK7G7KF5hvzLevYr8Z77NswJwu480ihdoGiVNg_3AuOln9luw5KcbQQfp_YWSvVyZeRab-VYvKG6d1IEhXWscNiHCF-uLKj74CJdfXei585nVcAY9aPZw3z3xULL_e86EbdqqS5NtLN_NonlAEA9yAPIltDFSNJxf3-RbnwnhqaFOxhiCwtLA8bojG6VCYNiNdGPyEqUvgcms2DC0xBdGJo-XG2d1iJRvtkhXJDrUJSY0_vlwkwzu9bgnZD_4mHUlw8OVSelkRIS8qf1gSuhsoUQHCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff15d4aac9.mp4?token=ZscPMoULahwfkzqBcm_1N30mMck-PvoA45IxcItBNCs-7MsQvDKaZxEk5A-BK7G7KF5hvzLevYr8Z77NswJwu480ihdoGiVNg_3AuOln9luw5KcbQQfp_YWSvVyZeRab-VYvKG6d1IEhXWscNiHCF-uLKj74CJdfXei585nVcAY9aPZw3z3xULL_e86EbdqqS5NtLN_NonlAEA9yAPIltDFSNJxf3-RbnwnhqaFOxhiCwtLA8bojG6VCYNiNdGPyEqUvgcms2DC0xBdGJo-XG2d1iJRvtkhXJDrUJSY0_vlwkwzu9bgnZD_4mHUlw8OVSelkRIS8qf1gSuhsoUQHCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرئاسات الايرانية تودع قائد الثورة</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/naya_foriraq/80733" target="_blank">📅 13:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80732">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef3133b31.mp4?token=MdxpzNV1uu9UCKAdyiyMbAH8MMyXGNAIPYYkeWL563yvM8zcO4Uz_5DcPPJyW2PMyubIJe8P9xJJDp94zPBEuwcAlto-gyGLodfpNI4oTFcJzmNlCw2quYWt1K9AYah-teSqkoR7mdqZv8YgCZbx1UJP7CXekONeVh6a0LSTEHPpoVZVPUZDDxwK6oGhEi6YWw2KGoMKZwe3jmpUnDl0KSgeqBfk2p9I-4ZvCGJAPVi4P8c6ZUqAW2PcMPbK_7-8FD_dmWgDeK6KOZuMH_ZOJOyFqRzrYFu1J3_opfNTNATD2xtEu4zasoHVXqjKij3r2XUmQP7ax9w4GMnR-eJTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef3133b31.mp4?token=MdxpzNV1uu9UCKAdyiyMbAH8MMyXGNAIPYYkeWL563yvM8zcO4Uz_5DcPPJyW2PMyubIJe8P9xJJDp94zPBEuwcAlto-gyGLodfpNI4oTFcJzmNlCw2quYWt1K9AYah-teSqkoR7mdqZv8YgCZbx1UJP7CXekONeVh6a0LSTEHPpoVZVPUZDDxwK6oGhEi6YWw2KGoMKZwe3jmpUnDl0KSgeqBfk2p9I-4ZvCGJAPVi4P8c6ZUqAW2PcMPbK_7-8FD_dmWgDeK6KOZuMH_ZOJOyFqRzrYFu1J3_opfNTNATD2xtEu4zasoHVXqjKij3r2XUmQP7ax9w4GMnR-eJTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول الوفد الاذربيجاني الى طهران للمشاركة في مراسم وداع قائد الثورة</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/80732" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80731">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dce186c99e.mp4?token=Vzb9AdywMUsNki0HEf_MEm2e5_hlDXru7SBmPK2dHU5rF8kvjOu12tPK3RZmUB6uGI7kz6sd5EyBpjQgOSgTFCmf41ypsbLlQBzJD4ztW5b-8Y3rTDJL5kUtnghn0bRIee5RCPiUfXjpFB3DxtXoMCf-EjOzR99X_hFlQWaNjWU-NSGgFEVgbYpUA8Vs1VrrmZoG2DlDO_lp0McCdzQ9wkxig5kgynFdYb4UNZdIM7TpX66m8IwxXoLuO_iNUxQQPiO1Mru0Ml_6neJ4_LHxLfCgztC-3ru2zFcEUxFgc_TvBt_n2noF_kZM6A128gMmIXz-eVcgfQyGPVjfFY35nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dce186c99e.mp4?token=Vzb9AdywMUsNki0HEf_MEm2e5_hlDXru7SBmPK2dHU5rF8kvjOu12tPK3RZmUB6uGI7kz6sd5EyBpjQgOSgTFCmf41ypsbLlQBzJD4ztW5b-8Y3rTDJL5kUtnghn0bRIee5RCPiUfXjpFB3DxtXoMCf-EjOzR99X_hFlQWaNjWU-NSGgFEVgbYpUA8Vs1VrrmZoG2DlDO_lp0McCdzQ9wkxig5kgynFdYb4UNZdIM7TpX66m8IwxXoLuO_iNUxQQPiO1Mru0Ml_6neJ4_LHxLfCgztC-3ru2zFcEUxFgc_TvBt_n2noF_kZM6A128gMmIXz-eVcgfQyGPVjfFY35nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد قطري يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/80731" target="_blank">📅 13:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80730">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وصول وفد من دولة جمهورية كوريا الديمقراطية العظمى لطهران للمشاركة بعزاء السيد القائد</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/80730" target="_blank">📅 13:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80729">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e2423c7e3.mp4?token=ATEv3VSkpySYpSymQls5BZi2W2hVeBpaJ2s1fJoLXTeebD7eN_vegyZuuKbXMNjW14LP3WvwyGniFDIgEBx8H3AgHm4lQSl3bM8nppvPy8MzgtcpWofcKObZSRyx-K6z0bdlA6nbCo-g0UaHtTkKtmmUclb-1s1Wt5RiH3qWr7O03CxBvynj46Ibx1ZxtODPPu7aGk-y4N8TVKZIuGall3dA7nq9HdlYjr4Ao6DNaJN7HZIDgI5B9FSD8q2EJODnjkzVauLKfxftS6Ue-RA3oLhlwYH5iZc9IGGQCmeGO2E7vaSUtxnxhWKjHBteI7otJIry-K0dt610XHMC73xwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e2423c7e3.mp4?token=ATEv3VSkpySYpSymQls5BZi2W2hVeBpaJ2s1fJoLXTeebD7eN_vegyZuuKbXMNjW14LP3WvwyGniFDIgEBx8H3AgHm4lQSl3bM8nppvPy8MzgtcpWofcKObZSRyx-K6z0bdlA6nbCo-g0UaHtTkKtmmUclb-1s1Wt5RiH3qWr7O03CxBvynj46Ibx1ZxtODPPu7aGk-y4N8TVKZIuGall3dA7nq9HdlYjr4Ao6DNaJN7HZIDgI5B9FSD8q2EJODnjkzVauLKfxftS6Ue-RA3oLhlwYH5iZc9IGGQCmeGO2E7vaSUtxnxhWKjHBteI7otJIry-K0dt610XHMC73xwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط قتلى وجرحى من عصابات الجولاني جراء هجوم مسلح بواسطة القنابل وانباء عن انتحاري استهدف حاجزاً عسكريا لهم في منطقة الدويلعة في دمشق</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/80729" target="_blank">📅 13:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80727">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06facee14e.mp4?token=N8WZHVAz0ZRK9qVpFmWgsoJOx1afIlQ4hhSy-z3wlHQ3auOP0wQYERVhwNtr23RNc8HDJc4n0U0gCZxViqmyXmhRjYU6GYWa01U0fqaJOvoOOZY9YxzF-40FSplcVyfXX6g4gRXXp1e-d8uDLJqRCcV2xrzFGPCojozJJtFGS9wTS6bdodMIExk1jg3jyvySqOb8ADl26u6GSI2j0NjTp7k9bnitx2soAH7dvrUhNjAE8Xfp_KjZW4k1VWzLz84hztIM5eMHjo1e_1txeqnvmrZY1S6Pja7pqrosigXUM8bypgQY_WOdDXCQHr7jclW3hueJYHniJYNRWv1BiFrn2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06facee14e.mp4?token=N8WZHVAz0ZRK9qVpFmWgsoJOx1afIlQ4hhSy-z3wlHQ3auOP0wQYERVhwNtr23RNc8HDJc4n0U0gCZxViqmyXmhRjYU6GYWa01U0fqaJOvoOOZY9YxzF-40FSplcVyfXX6g4gRXXp1e-d8uDLJqRCcV2xrzFGPCojozJJtFGS9wTS6bdodMIExk1jg3jyvySqOb8ADl26u6GSI2j0NjTp7k9bnitx2soAH7dvrUhNjAE8Xfp_KjZW4k1VWzLz84hztIM5eMHjo1e_1txeqnvmrZY1S6Pja7pqrosigXUM8bypgQY_WOdDXCQHr7jclW3hueJYHniJYNRWv1BiFrn2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد قوات الامن الايرانية على هامش مراسم وداع قائد الثورة: إذا كانت القوات المسلحة اليوم قوية وتواجه أقوى الجيوش في العالم، فذلك بفضل جهود القائد الشهيد.</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/80727" target="_blank">📅 13:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80726">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUW8AEJJaiw43ApZ3UnMkt2qWL1hssGGtdDpCo22CTEAw9Ea06zfocZfYNOEjBoyXOvo0ym-lZQ4HgAwwb0atK6hwu2N45cv5Lrz6_pMNL1nKmAvXOEl8aGwG_zFrF_1l3Wdbj_w_CRiEjUZaTx1Hnd5hMJwzQ7D7asFjZGfopIDV7uDp1qvWAhUTyYHMyX2DA1j23GKtn7sHQTEtuVvgfKLWZEitt5E2C83AynFmbdiIeP2CvUJAVr6LAp_d5mhjwj8kq-77GWiv38A4aLBDtRWNUX6wNxT_ZCbvW93h96ASxvHDRePtLbp0OWFVySOe5N3UORRTI2kS_K4AlLaKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرئيس الايراني مسعود بزشكيان يستقبل وفود من الصين وناميبيا وأفغانستان ضمن مراسم وداع قائد الثورة الاسلامية.</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/80726" target="_blank">📅 13:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80725">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADl-tqetjIGIsMhcb7OWDpEMMroymk6ydDyv8c0JX3LsT3wEcuCShO9ZoK6q_pWUDm34kv22K-vDGOKM19RAUwQaFj7fGvXG0Hs-npsEw_DmjnoC7PimMEqskFhrWQ2dxMogKmKzECMHTuSFxmITKj6zhVCMDDZLijQvvoh6JXGZVeKW5Q3161La8pwENv2z7HlHgjZ0xMaBm4Bl8pRwr-DsjM4RHr8CR8jel4Na__k70itwP0e_nXXCWc6ZesXPhyxu65Cu81A3hr1EezrN5YtsImsM0kXglKnvT8daWdct9JlYmxBbwydIV0pBFy08otS3ch8ZnB99W0ve__R4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا سيدنا القائد؛ أفتخر بوجودكم المليء بالمحبة والطهر
رسالة من الشهيد مصباح الهدى باقري إلى السيد الشهيد، الدكتور مصباح الهدى باقري هو صهر القائد الشهيد للثورة الإسلامية واستشهد في بداية الحرب المفروضة الأخيرة برفقة آية الله العظمى السيد علي خامنئي</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/80725" target="_blank">📅 13:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80724">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بدأ جمع تواقيع نيابية في العراق لاعلان يومي 7 و8 تموز عطلة رسمية لاتاحة الفرصة للشعب العراقي للمشاركة في تشييع قائد الثورة</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/naya_foriraq/80724" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80723">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB2Gku5GCQ7qvHr--elo9hawIyLDnRFTDNqSg000Vy3Fce77mD7-Dl6r_Gk-WcTh2QnhBHkdzz_5lSosLjwE4nOnwbwPNjMyMRwWaBlTHbBUpkqiNaOV2kOfIHAcBSw8DDaxrD3C2ZHBqKvqhLgaVfezybAvdO9AesASy214DEeZB6XfnGXOVAr5-FxCcR3DtqRkpmdbDFxQ7tR6cNt6FQcZ4_d1AY2421MdrYT6ITVutregPwZBKVJJFlmWS5wKYU6g8eRp5hIOCrFs2WZKiPL53HLspSvIjTbtF0x5fr_oEHC765LpU3mZz9li-MYOD4zJw1YtHkyL0fTiQHVkpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/naya_foriraq/80723" target="_blank">📅 13:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80722">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e686e795f.mp4?token=IIcWWM6O1gg5jUKiVdeIlz-iKi7xWY7sV6rCzCsd2yBDrHDPeWciatzYZqNyqBM2UgUxxTMkRaNp77_Y9_MeXXw85rXxghQbcwoSubMYcQvaYrUJTjvsqOsm-0Kl2wlWOuk2ZLHgpjOZqYFNhIW8az0xj8dgQjVZCICcv_uXVTODkiFKdRKtQYt_1CqsZdJc97NE_Nngc68-aR5XUL-HE17t0Dn8YO_to5qxZWKeGC9BJ7N_Tr3HBfnruHJAIDNHJDhLsJ14kWpUn1cTD9KdQBZ_hV_ImS4PJSJTr-B_pV0Xnekj8tuZnbUxCgYKWOYbeosDKE45S2CJEq5CF5JfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e686e795f.mp4?token=IIcWWM6O1gg5jUKiVdeIlz-iKi7xWY7sV6rCzCsd2yBDrHDPeWciatzYZqNyqBM2UgUxxTMkRaNp77_Y9_MeXXw85rXxghQbcwoSubMYcQvaYrUJTjvsqOsm-0Kl2wlWOuk2ZLHgpjOZqYFNhIW8az0xj8dgQjVZCICcv_uXVTODkiFKdRKtQYt_1CqsZdJc97NE_Nngc68-aR5XUL-HE17t0Dn8YO_to5qxZWKeGC9BJ7N_Tr3HBfnruHJAIDNHJDhLsJ14kWpUn1cTD9KdQBZ_hV_ImS4PJSJTr-B_pV0Xnekj8tuZnbUxCgYKWOYbeosDKE45S2CJEq5CF5JfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد باكستاني يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/naya_foriraq/80722" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80714">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTi9XoW869kTFUeDmlInSZy-dXNxq-SeQedccFuXPJ8fjUH7PxMc5yuIb1cwVQRIIvcqTRq4XU1yRMkTmebp3by706Ce6VbaFfU_g_nRZQE9A-EfjTSLl782Yi4vpVSWpS9p4ygTEwsn784m2zzGMWZJrA9lFLlCVJwAgM4b-dqte6s2x5qur8lqAx25hjPMqW8P996wwo1gKeCfMx4f8BHB4e_29rxxcOeKkEnli5pYMPOpfz3pimFjetgi1JMpYFzPwB80nZaayRLQmUJZgtPnGrOXO7hyuNKXAh-AH1eofvlGlHK5ltzKues4MDx-aG1IqMHSriSeuNZRAS6ZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/patIZyPr4oByQz3EjRBpQmQzdijPn_TeHSoy6Xhb3gk9X4hktMPocTlG-s3ASQz0tkaOqsMkowxDB6Zd4sqRUjtBqNqAcIuzaZMIQ0JA6IW-3ZaBM0ysE0vOsefZO6ggMvaxj9rS4NM3-JXyBLBYbY078JKirPDL4rlzb8ZDIXGLfJ_A2Jm28ZlQn6GqnWwORIKzv4Y4QnB13hKzhcGIhFQFvWkvwrnVyPrOz3wDPbtNHzONu3532m-S6pKQgaotOgrSa_2DU9InK8fcXW2tcIOiA5lCqkkuE7u2ncScRUcCwTu_YeYLzI498QZrjYCtiq03_C-U7uy3GZ3XXRKMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGO_poCRiyGLBxo2ROgwTNMYqciS-QWBu-1QEwpsOP9dQ9h6Zpx1W0NdOBjDEnJHq_Srt4AgMTnrnIR-VVvYhTKHu-4XKzCsJTapLwyW8WJ6J8fUVSlO3p2KQgYnJ4N8jwgi1NXv_qeo_ZjjN3hKVOTIwcfB6C00YPmXB_0dj24RS5z9O6T_kIj_EKoZRxiPIZPzjkB-f0GmShAGfQDuLrmSEhJKZD-XzhMkGFP5HRU0bDkJVdA3sTRD0x31FrwnhNXJBBCYyw8N0ulqEX_KhZ5Fw4oK8uYgW6F8KpAVb742jtP6nMfEbfwZ-YXa9BmjayErpfCmLsoS2pL0H7Dr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBZ50L2nCTDmOGPDTS0-UQ7zoaf0_0-mHypArdc12olSZgE-zRkzB50d1KTm1DV6gYL4OwLvaUsIvJbhv16bs-eitj607pq81qWoFAN5Hl3PF4-7gwi4lxGpdDENRaX9DEK2jXmnw8J2EwPtzN333u-8gkzLZWphMOxI_p8mFh6UHqdydCC1H-ExeyQooNsDTHADSsEgiaYAlNNpvZFdEwFYxDyaWfRSgBU1sriCiow3qJiSCBIrrUf9ths0HdqPyc04JYkT0aRQsTUSYMAyQ9hDS4vtlSdmEmO1FfFyRMLJsMcKTd0N2gq0Pst5dd4oQndUqOh-j9CfvIQJL4CQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z2xh6-dioY2AFAuq0KFCChRcuqZEGGX05kMMkGms2eTNiRxcfFjyEjzbaU5EkEnGEvAOPsk06r8dF5Q5vLe7GetZuMZI7iSFEt0fBALUUT2xFXSWbNnifmUxA8yL-HZBM3Pw4Fy_mtIGfgYrpBJ3W0OCUQHu1j3DdpAHCpg_TBaHiL6nAPSSxD_hkbPXcZL_21UTuCkm8maB55ItD5bfnJ9ELtLoCLIaknse6U8XftEXmiogwDpnZ3YWZMWOST7rbgqQzMMiwhPtW2YtTnjCif8ZlqXZwFvHyEzXZrKUuVZBj2Un1iuOclNYFozJR-3grtQTWEKFAzr7l1xopvt-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEtmoZ66sENNWBWjafY9Z9jaZrEaWsWO7oDmUe3B2H9yPib5prtD77M1jJLgDZLMnyzrUONajrvongAHz_cd-N930ATzOk8Oawd4dR0CMToOx9GmdRINK4YntppETXnnWF73ze-yHDsFDAbJQcDccKR-ZUx_47pzlpbjtsvuRcWHGjVRgkXmpRvczK4YDkOSRNxXYt2FyJuFZ9OjrNCfm7ZLrR71PWtYNDlZMGMDQxEeIPXMYCAHz_vVMK4cV3MTXtTqGYbK7bJ2eNgRJfAEVEzDhtRcgMRbRdT5BlUS_HYXxP5DlNs7iB5YhkjOkKfm0jcv5iHBCNFr0SRjMUCGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoiY-EAi5AimwryokBeFYrd_jQSNpvddv06sgoCCuv1QRKuvsOCARD64Xqz3P99rcK0huQTwJfP0-N1mpjropHgjD2hU4Si5nGju0uurhtANJGrhNX9U7LNyLLmqGTUy5Iceu3dkC2HrUo-c193eDqmVQbAB6KRQwG_gK5GCu8AKnOH1mbWdWWDqIJBQDeUx_qquQaF5fzn8NTbDFRJnoGRLlMx8w9WygnYPgrw7l7ccU4QWflRXaw6-3Accp5GWmKfA8sudzZduND0cerGt3Kubr1fCzyCwG-daG6fVa5kPpTQ353AoYa4WaFVaDJ5wmL2IN8ypG8GXJh2khC8Eeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elZbAcAaXDDJXyGALxlePAPNfnbwNHOy3e3_g3Znh_2vIXFNbGlaGfMpMNZyzftnHq_HCot2KbtCm1gO83Ace_kEl0tvcPXfAzH7GteBAQT-a8dnbnzsiQx9Rn9HSwEA4u9Pfb1hY_3Z5JCvEFNhn1TGa7si9yYtaXIapEhtdQrykkqFHHyMcGhlnc0ZT76ULHLaSNFhoVTP-lxJ1NWZr_vRJMG3kYHydfxuSK6tj5CkxydkRiC6QXRtcpNxX3Y1bck2cw3-OHZNQq0ZSpLfxspmL3hfWa5w3mL88oB3KsZXm4gCYXQzRuiSAx2DMAlKJQeaFrA5Xt986Yke4x0YuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وفد هيئة الحشد الشعبي برئاسة الفياض يصل إلى طهران للمشاركة في مراسم توديع آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره)
وصل وفد هيئة الحشد الشعبي، برئاسة رئيس الهيئة السيد فالح الفياض، يرافقه رئيس الأركان السيد عبد العزيز المحمداوي، وعدد من القيادات ومديري الهيئة، إلى العاصمة الإيرانية طهران، للمشاركة في مراسم توديع قائد الثورة الإسلامية، آية الله العظمى الشهيد السيد علي الخامنئي (قدس سره).
وتأتي مشاركة وفد الهيئة في إطار حضور مراسم التوديع الرسمية التي تُقام في العاصمة الإيرانية طهران، بمشاركة شخصيات ووفود رسمية من داخل إيران وخارجها.</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/80714" target="_blank">📅 13:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80713">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940ab08d64.mp4?token=Jk79Dr0rvk9hocoOiXSSUf5Kg48DQ_8ybW84BSvy4nWcvHhSDd1gf76k9xa-Zeq0-OQZO-A5MpJGe5luOR5I1fTVTIwM9Q7HTF7fLgrW2PRp0wKpO-GtVbZ7Kw7SmJVBf6Q4sWFD5Ds8rc7O2ODqRDIwT4-zPuNEKkIlR-zCxOuKwBaT9ZzxCiuQ68X4KmG2tO1dvdNVrhTCgosEwJO8k098xvVP_zceeQfuMMEOY6JmrmWk3owNPjVZCRJdhFmavt33tuhrPtCaOcpKxGTa8IFF0-dDd5927fhVX1cwVu_WrZvN-Po0PooZyf1Br1jMxzd2rl7z7qJOMfI3VOtS9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940ab08d64.mp4?token=Jk79Dr0rvk9hocoOiXSSUf5Kg48DQ_8ybW84BSvy4nWcvHhSDd1gf76k9xa-Zeq0-OQZO-A5MpJGe5luOR5I1fTVTIwM9Q7HTF7fLgrW2PRp0wKpO-GtVbZ7Kw7SmJVBf6Q4sWFD5Ds8rc7O2ODqRDIwT4-zPuNEKkIlR-zCxOuKwBaT9ZzxCiuQ68X4KmG2tO1dvdNVrhTCgosEwJO8k098xvVP_zceeQfuMMEOY6JmrmWk3owNPjVZCRJdhFmavt33tuhrPtCaOcpKxGTa8IFF0-dDd5927fhVX1cwVu_WrZvN-Po0PooZyf1Br1jMxzd2rl7z7qJOMfI3VOtS9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد هندي يصل طهران للمشاركة في مراسم وداع قائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/naya_foriraq/80713" target="_blank">📅 13:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80712">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35aac3f0f7.mp4?token=lZkbzbosYg153rT-Lm7sZfB3C_F-DXllWJL_RDHYzTrGJKyO0YMs4Fy8IcPn4hmrPlXxDtQTShbzQE3ROPx7lhIHfip6BIroXhWKs5YVXpBrOSI1fZIcfARukiU86D6OBMC9jo7r-SvITPlC-a7LMjSQlQ-k39KtCd_lhxepDp-A_fgG4e5rTQAUdmWpwcC6vnlJQk2fAa2ukL3nc-7ABODxLGEEdv1AXMw4k6QYYFaTiuMtZ3obBEAUQpeNkexFqEQdglU3CLRiWh25ClVBKubd5UaJbzJ7VeOtGH7LU3lyBOIB0YUJebdQOdMKlCSDvqqyk7oraCBPtUoo8ndTdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35aac3f0f7.mp4?token=lZkbzbosYg153rT-Lm7sZfB3C_F-DXllWJL_RDHYzTrGJKyO0YMs4Fy8IcPn4hmrPlXxDtQTShbzQE3ROPx7lhIHfip6BIroXhWKs5YVXpBrOSI1fZIcfARukiU86D6OBMC9jo7r-SvITPlC-a7LMjSQlQ-k39KtCd_lhxepDp-A_fgG4e5rTQAUdmWpwcC6vnlJQk2fAa2ukL3nc-7ABODxLGEEdv1AXMw4k6QYYFaTiuMtZ3obBEAUQpeNkexFqEQdglU3CLRiWh25ClVBKubd5UaJbzJ7VeOtGH7LU3lyBOIB0YUJebdQOdMKlCSDvqqyk7oraCBPtUoo8ndTdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد الجيش الايراني على هامش المراسم: نعلن للأعداء، بإرادة أقوى، أننا سأخذ ثأر الإمام الشهيد والشهداء.</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/80712" target="_blank">📅 13:01 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
