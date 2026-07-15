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
<img src="https://cdn4.telesco.pe/file/pvyes6oSLmGvL7kjfqwqMLgJN8gYNEWZYj60VWT53UzW-qTYwXOkXH4tYxo6VzauMe4kDlde2zfW55iCdwweFWQT8vUI7-gNInwkXGXmA2hTCwVJ_AFZFTzyTIAh-4PbhGo8qHTVg7Pqd0eo770Pa-UrjMnktVfwm9rngEJkNBkxDAzjDOICTLxoEx7_wHEd-_LrdNZozOUSo0t1Gm4cwwkSKun7vI6Uq9cwqRrMRT0r76sr7yU7MH6S2jnRULgKn_R_9vP5xqpvrFH467fldhKLj2usYvqItxAtI2GAdzAu-X7TgRz_i0SV-V77ick3lvUzzsrf1ncUzFH4WgQILQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 00:57:43</div>
<hr>

<div class="tg-post" id="msg-450300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03358f42e.mp4?token=IYuVhcSK6kVBm5etrIYwBUjzgpP-jrRdnIDy3WgGDzpo5X4V64Za96woNWrSIcX5ezmGjo7OILc_Vn__PITQn1VrsBiUdZhIblxnm6ofikTxYW51AGntRRz_jYIePiPaPCM0t9zAeMvXCRcfTFeEVWJi7s2z2y2KsMLxqgVOWEBz740jauBeXUnycaDAm83LhUyiWlGjEfwm7n91liB3stHygBglVNEkzBaec--FHyj-eM20EiSCQbwDI3nCU0kNcAZhUn3AuwVO4rlHawiGp2VtzBC92uIdlZKYXQRUK-AC3ce-vQYHoWkKUMrV5WB_k3t5qnjPGa5obVBVYeBRxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03358f42e.mp4?token=IYuVhcSK6kVBm5etrIYwBUjzgpP-jrRdnIDy3WgGDzpo5X4V64Za96woNWrSIcX5ezmGjo7OILc_Vn__PITQn1VrsBiUdZhIblxnm6ofikTxYW51AGntRRz_jYIePiPaPCM0t9zAeMvXCRcfTFeEVWJi7s2z2y2KsMLxqgVOWEBz740jauBeXUnycaDAm83LhUyiWlGjEfwm7n91liB3stHygBglVNEkzBaec--FHyj-eM20EiSCQbwDI3nCU0kNcAZhUn3AuwVO4rlHawiGp2VtzBC92uIdlZKYXQRUK-AC3ce-vQYHoWkKUMrV5WB_k3t5qnjPGa5obVBVYeBRxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌ همدستی کویت با آمریکا در حملۀ بامدادی به ایران
🔹
برخی منابع خبری مدعی شدند که تعدادی از موشک‌های آمریکایی شلیک شده به سمت ایران، از مبدأ کویت بوده است. @Farsna</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/farsna/450300" target="_blank">📅 00:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450296">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Thp0K3qx3O0Q_f2hHSAMqWF0bub8mMCQUvmttknOjGXWYTF0i518E4o3qtvH4_01Z_UmMmvYBhExUNdVWjBoOLumLK-ns_ug2oJEg6XOwHOJgRtjupYiVPHMbncYMuxmw1-StuQUzHWmFIyV8OsB_PtDVFsvBLaPTi4Y8vcdkHSpe7x3-6HRyW_NKrhSzzoTrvLZvIcbId-wDcvFfvPYdTTSE59-oXuSG5UZTazKgDswGk6dwvJwKU25_KblDDLCaf9HEARtrm1Fm4ojyHIE0nlfK9Z4y3j5Atcbep3nECipKz8mlubMJBeNQyEjz20ea8SXraIiE7weY50YtPuEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhcJk6_c5GVT7Cl0SZGdNNb9vOmWXltpccPsVOQ-rp9iOmqRbKY5GavpHM6svDHHoscMwyr8z2MbxzycOEUhT1k-7JAwkiGnYi4W0LGGCvKf-JmcrhGCvQiiVo92q4xWo-FtlLu10bdqdjchsS52JgZ1f8ZSNUjerAa-FgImd4k2FgLYQ4FaOF9zPnyzFu0RLsIzlTF4PR_yi0H5MnWxo6TNkiW670Sv_rjlo3HaBgZGHF9HdDnpbpT1rc5-pCMLkJu4VRsEBOTyiWtyvN8qX5Vhy8R9mEKiAnFglqFUHzJZ9m-N0kO8TeL86mivQg-PA2vDY7GiBEz1ApbvnYTcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lAfnWAPpLP_695qiZHBX_tIJ0O23PBGlSFgNNroAO9BzF_Xmhpw6ICmefrLW2mNd2vFmtTBPjOL66IAGt0sxQoV5gX7Al8tX8QKsNjs6bDOTOlVHXH8zhxpFAH6OinnQxsRk_JmHkzBIdrldVVmcA_a4WssIsgZ8oq7d_M_IZSRC5tquEnoQASWr-ovlWpv_zhPKuVXWmp9vc29KyV4qvZrRRdsomJoO3DGgfykKuqr98LUk2tGSNHtAtZMHcONqaEM3G39Lelp0PwXUvT3GeQ3kn3_Rv6Yqko2QPH9lymOehOgNUmHi2tDLp9kbcdgRyXKGriZ7njz2-MYsUt8LgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIj-zymKzwIGDGrCBpcosYxYQpIQFP-En-MTcTYiZfj0ITjnG3YKkcG_l8lLSfxLuC9CpguzFsc-qGL-aixonxcsUh2znacQ4iIFVL3M3S--o8KE1NdluMLVel-LaCdxnNDxtKdxQGFpNfJ0wi0p0PEUtr0XItL3g1fXP8_MH8InQm0MILX3DYpHAkWqaI-xbAGYUAlmJ3OxhwdC3TekCu4IOq2hKZZ4ELBulFNRFz648YVCiGDFjlkxtZdA3QRl86WGNZOqmTK73DwFsZxNlvynY7zMjB4oqzZClTdsZaUZeAd3o0n1fWmITAvjBeviyGS3LvhJEKS1hnRh2v0Slw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۵ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/farsna/450296" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVkdcy7OQETR0tYB-ZoEm_e9mBZkszBNOVyuxE-VLE8ew3UXjDFuZepdVu4ll7nxGBh3-2xnHizJpEiVPPA5cYQV_atjMEbHEbQkNldI1CJbQ7Zdp_EBBfNOyY-VBi-ugNZLd9hH9jpC_ZnpMHQU7-H9B1x6efYUKpIjNKL5QTC-tIaQ60JfiUAqD4rNNbU_1pU9grX1WAf97DOQPMN-Az7RihvQipTy8AbcejLCAF3k2zR1yyttGBTdxNV3r3dKqVwU6iWaCV7qIq28qSAsRkYxC5R7k2Kz4sJ2RGQUJrEvMrkNEmdRrvGNWcYYjdESCfspIE70ECoHjlExXAw43Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p79A7KyHsDLmmJiqJE6ea4eryEkRcbD1QWKO1SPvGXunExOXQiwtTkfnadK70IR1uZLs1lNym4DtJBtdrNjGQmLlw5iTOFV9YZQgt_h7LuHsK0A4J1JuLqETASyOaAW8iyg3t0W15B5YKrrdqaBhEtdugaPp3qNiXuKuJX6YwS2LjGUWjmZKqr16HsCFm198841rkEjHcBacQ6nqlaciv3re9H2LJqbYkbAy_X9mMsB2BAlqe_ansJM2cDGqvA0JgMYvaHTQ0fnk8bXgHJBYlV67zvyVXkTydRWUP0aIk0C9vtzzXDUg0IBLGEv8H_jVbrcDwZHOXpSsXI7ZUG0TSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nsi6_kdwca3WvKDT-DNy_p-fqphQyHTvpMcvky0MtUbtXrXFwomR9WowPZVAUKT9PxwK2INYYlBdlWA5_i2I4liWbioOEe_l8_eGTiYcu1_GBWs1o8ChRX1CTZWYCSzefWNZ6v7rEae7iTW-JVWqMBM31hKs8viywNyZaclsQnPiGxJQEMJgdeACtjVsuD_WUJeJtfNli71GUQGMvIrpJ1CxnBwqG6_vPjpIqYG92KGwJaYhacjqXh2-IGTTOhpnSJL9mGbomHv1sSNUVl_5yFXi_f9TcOBiLgp1r5EZOv-F4s-x8XOKm7eHkagOu5mT8zG7s3ZPmatagCJiCT_Rlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJcuPcwNy53VkYv5C0VfxqJxUUELpJqJ0q7yA43fc9YOdjn8DA_ebvgI6eVo98lH6Z4wQxRm6Q--bJgeOsoatKftR1PDqDfSoWw5cJ0hHbJJhiOJ-VVme82FwoKyNermW7VNvf4G21PyOvICelPkIDt3KAcRf01m3jc5apuW7Vmanuj4sU_vuMszK2KxSinI7fMzYt18oUlttUu4jX5ZqtPR96Uc_QfdU4PoAfsfZy8qRO3y1qEqQobZh-EtAbNzwQMPlXMMc3hmhIVH5pIgCcOY-KrwyPq2q4ZfgFFYGsF3sfhrlaYHuSfEPmY5kkn-6YV_F1AuOxylayZ6JDhoIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l6djBGOxSkyqRJpGKUzFAObBWLeq6rtCBxCwuGSlyCli3vGHrKpMrDJN2h_6VNMKhQodt_JAtMiZ6pLJ2Q8zMQB2Y9VXmC3oT36FXRizOfmkb4hbXOXEJmJMnchI2tvrS0PTT41A-abovOeB4kVoJxQYqZ1VWsvDHU7LHffmVVqU3CU3i3clgcRdAobYO8ZqAFhk5YwbyHSNzjY1tUDN5E_yrxnIedHxikB8oHl4ATPcO1KmW_nZ-z11JyibZFdXZiLFht-0fF0m4dB8VDtRtcYVpeoXqkIUcokaEaWcbKuzOzL4kKBdlDdtoOD5UNbBt5fYmJg2OKxxZwNNbu-JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hr5A7OY65ssFon-XjQwyHsmyu6OlZ9dTyrbru5bWj46CN2ZhF6WubMC3NIVDOQdfTzgTX_ciZYAKkJcygjx4xSIs34Nrx-mwF1mf_XcvDZabM2_bhK5JgdFqqCXbfkhy3l5yKWLTcYsDMCGDJE0bO1J6fHVEuRSxF0d7NGLCImpoKQ3aErr-1locFX1W3fNdK5LE82hBsYJwjL7Rz82-PTAmrn9CAt0Z80XAiNpYtX8xbNQDwoAssTmnJplT3R2bZM8m9eZnxOPQNkg-Q9t0N0JgEueyOuCczAsB_kn_LAI6qNLqWR59M4t-IuwuQcXDygZ2AvhfoGH-zsRKE18c2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EfMRkjarg2YplZqEZN_g0YMrkBTLnb3UHQiUxvuH5429THo0ArUbDxdgPiYdG0n7Z7SLmYrKkioo55f8zSv5fjx-VXCLh1ELogOYgMG-RH7x8C5iSypsIeZjqeoO3XTWwN8g7hn2UKM1wDcyma1obs-631XRaCYSjJLSWp7AnmisJpWxTNPMgDNx4CfoMAXMnb5RtAPoaufXVhhZB1UBBX4JukKXoLGiNie1zFwEx2pjG7oBNI3-qAsH7wFF_yNK_oadi7l-_Do75Cq0pNMFKxutqS-ogB_AY3VzRYH3K_8_y48hOyv8Y-gzXEPyY17HWPxnyUxB5OG9XuKNqK6sDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDaSMuJEo-K6jRT_UOI3bOvEYcKuWpMNRyJtxPz9rCo0PAq5M59L9I_H1uZ6RVFdhlx8Ap32KglyHAk0nJG8PaMdvCz_79r-EerohoD6J0epNHFdEA4z_s3ompY-_CltDSA-zxGOlhsVXslCEB7YScELOxBimSAS_7BKA-eGS7lPFyEUVWfeIgnWTtDLjBzodyFN5qk3CiNJgE58NCg0EFfuX0yc2nANdLZ1y5jF56nawKBDySsO96EttceTlx3xVzMkflLFB9mqPGG48UgvCIMAN9M4eCIseTNCW_kul8vYWVT6IRUzSqTNVYVSFtQ3GizbajKUHwMNXIhGDmXk1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MrGWq3yCEwjAnkey3MiSlLdxndlnpB8XFbosWTD1sS-V5QSeo-PBLEHy6hwanqx3n9pq8yQ3fG4P2Z1bJNFMfkhN0q232TKzFX1MzJ3QasFiu9BiCtXqRJfpL-ELt3_ixi13r3N-y1xhKA7IUGIqvicyhN7f0VQRzoh0GNpcS0hMk8T0d9wQlyRfqAiQZGSd29Uv1lUifI7ZtBQbyfV753B_JlrtlJ_riJYTgMarFYLVR-cMWv_wsYX7b63WrcJlzBg3Zy6N7obVKrFcMUiDJLGpaR9FLOmxkQaqQUu_o7qwRRvO2CoV52czdlaeIiOxkrwDp_Vf41OrsG_UFqrowg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA2Lw7NkBo2CgsLW2l_G3LmDuF0uKJJQlt-WZmv_mFhHto3Fr81cdetU2n11qpNT788wa2y8iBUDc2Hms6uoXhdwvu1B3BnFS0IlOQ91IIaYnWn4xrrHhy3Phvpr8dGvmSwOz4h6olQHctrtlU6X5raL_2CDx0slrbkqw7CO0u1sui5wA7kjK2WgAMwCeMe5hLX5THrm-PfQYoKNjC0eLLelPuhT1hqAgJUDaLfWwpqDeqO8U0mWlsG2kkjc_Lo81tJdx_PWPoS08OE5MblewUJbvQMzMjbu5Jz3_ppLuZrcphxznyAzY9fHp2iSaDcfGZCVX4GV1f-sbrJMWaNqCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/farsna/450286" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8606043dd.mp4?token=HCLMItSefSJqO18cWq2FjJ5K0aaIZ2t3oHSt1JfUolPiQDUUTWDbf_0EYgcu3pnCfSpejnKbuJpLiFM4W_-02tiDOPW5m4kxZuO6aUfWEMqvBdoA18h1SASy-d_6A1Q1lTG1HQr6y7XRKeoNSLRNzO80pDOSvWtYY06V4y3yk6U6dx-vM9ld6PKaFOeZJYIhvueXCBleXNhGS_7RpBKvX9BN9UfogGWEND2RvaRgyeXshTTweRjWyBic_vNag77udU5QU8T_lCcSC2gLutKuBIvsKSbF7g1rkrIQ_F2eyoS-GZWZ02G_Vn3ul1EQjmTnmA1JG915nCMUQYAou4FOPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8606043dd.mp4?token=HCLMItSefSJqO18cWq2FjJ5K0aaIZ2t3oHSt1JfUolPiQDUUTWDbf_0EYgcu3pnCfSpejnKbuJpLiFM4W_-02tiDOPW5m4kxZuO6aUfWEMqvBdoA18h1SASy-d_6A1Q1lTG1HQr6y7XRKeoNSLRNzO80pDOSvWtYY06V4y3yk6U6dx-vM9ld6PKaFOeZJYIhvueXCBleXNhGS_7RpBKvX9BN9UfogGWEND2RvaRgyeXshTTweRjWyBic_vNag77udU5QU8T_lCcSC2gLutKuBIvsKSbF7g1rkrIQ_F2eyoS-GZWZ02G_Vn3ul1EQjmTnmA1JG915nCMUQYAou4FOPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ رکن اساسی خونخواهی رهبر شهید
حجت‌الاسلام اختری، رئیس کمیته حمایت از انقلاب اسلامی مردم فلسطین در مراسم یادبود امام شهید که با حضور عراقی‌های مقیم ایران در حسینیه کربلایی‌ها برگزار شد، زمینه‌های اساسی خونخواهی آقای شهید ایران را تشریح کرد.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/farsna/450285" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=Z1nJK-6r66ACCjvTJzqIed0erphaGW_3T18RDpBX635T4gXQn3gNRiizGAtha9_zMlUyS8urMJjFBgfR_KBkB8CK5RMAUVn00gXhATF8qXB80XHW4TM-xGLmVf-ddY4mDVZV1imnOk3MjjUjr9yMtkTjK4GQxTXevD75OpJmsX7a88Ai6Mwt830M98TQtJUzZu199Gp8yJVsUw0N2J8Z27Y0oEVF7C4rrqFIST2sodqlDkvf4-9XDv9Zk2dsdln6cGSX7ynCSSn_kfY85CzJgeMyAH4Tyy4aw2LU_zdJNCQ2smg9J-l9lUOn7q142mJpsw7QL7xxiAePtvhFWYKZYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=Z1nJK-6r66ACCjvTJzqIed0erphaGW_3T18RDpBX635T4gXQn3gNRiizGAtha9_zMlUyS8urMJjFBgfR_KBkB8CK5RMAUVn00gXhATF8qXB80XHW4TM-xGLmVf-ddY4mDVZV1imnOk3MjjUjr9yMtkTjK4GQxTXevD75OpJmsX7a88Ai6Mwt830M98TQtJUzZu199Gp8yJVsUw0N2J8Z27Y0oEVF7C4rrqFIST2sodqlDkvf4-9XDv9Zk2dsdln6cGSX7ynCSSn_kfY85CzJgeMyAH4Tyy4aw2LU_zdJNCQ2smg9J-l9lUOn7q142mJpsw7QL7xxiAePtvhFWYKZYoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
اصابت موشک‌های آمریکا به نزدیکی بیمارستان کودکان سرطانی اهواز
🔹
در ساعت گذشته مردم اهواز شاهد اصابت موشک‌های دشمن به مناطق مختلف این شهر بوده‌اند.
🔹
در یکی از این حملات چند فروند موشک به جنب بیمارستان بقایی که محل شیمی‌درمانی بیماران سرطانی خصوصا کودکان…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/450284" target="_blank">📅 00:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71b6789fc6.mp4?token=XQf0AywWhAq1_fGzwtV-HZpGQOSYhpB3_82-C_e3vRyR65jQDpzMPhozUGz750nO2mFCTSJQ8zgJcJWpbna3R83gSJlLFfIWqNJFcQcaMbHt99Rx16Zp8gAeyRcDIdbAVDiFOnAPmCCa11c379QkgDlky8VFY4iaWhJe2vmvegI7CzqWw_KnqbBeAYLnlslCCbKGlwzsubrQNZ0OXHs07BpnoRtGQGy5cyHG9fZkixoy2Qvm7Wsup2WSqsSxdw0qFhlG6RCt5youh_RI-ikJ-bAC1DKjI9Q8ivIika9rcNetcp215_cNWqbEP787Pl54ozWfCT2yzXi1fJtTtThKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71b6789fc6.mp4?token=XQf0AywWhAq1_fGzwtV-HZpGQOSYhpB3_82-C_e3vRyR65jQDpzMPhozUGz750nO2mFCTSJQ8zgJcJWpbna3R83gSJlLFfIWqNJFcQcaMbHt99Rx16Zp8gAeyRcDIdbAVDiFOnAPmCCa11c379QkgDlky8VFY4iaWhJe2vmvegI7CzqWw_KnqbBeAYLnlslCCbKGlwzsubrQNZ0OXHs07BpnoRtGQGy5cyHG9fZkixoy2Qvm7Wsup2WSqsSxdw0qFhlG6RCt5youh_RI-ikJ-bAC1DKjI9Q8ivIika9rcNetcp215_cNWqbEP787Pl54ozWfCT2yzXi1fJtTtThKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرژانتین گل دوم را هم زد
⚽️
آرژانتین ۲ - ۱ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/450282" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI5HZMahOUepSeg5u-RDM3ttMN4V95Zhc_CVGOd0WrsdNsAeh3HmMkARC2VGVMrDpCB4eDPpgjw8136DBjQ6XcXW3nn_QXSUcOIkYwmnOl37VQl4gknSI8PvV6NyBdArnJoilyE1JZMypZ5-773ewkfasAmf8TMb0tdGjuAxXudgTsSRp844nP5SyXZ0lUuKKhikrCM2FBBH9Bkvj1B0N0bM1DgFqkChV-eaKef8p9hT2XrCvfwPqZ2dgBuuQ-_PMpx2-fw6Ki3Vq2WcXnLp9l1UrNC3r4LzhEQNCFJK6o-7sXKox3zwIH8nl-ggteQDw6yM5JIfXB8kqYjWEIBwrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی اماراتی دیگر از جنوب تنگۀ هرمز برگشت خورد
🔹
تصاویر ماهواره‌ای نشان می‌دهد که یک کشتی اماراتی ناگهان مسیر خود را از مسیر جنوبی تنگۀ هرمز تغییر داده و برگشته است.
🔸
شب‌های گذشته دو کشتی اماراتی هدف حملۀ موشک‌های ایران قرار گرفتند که این هدف‌گیری به توقف صادرات نفت بندر فجیرۀ امارات منجر شد.
🔸
سپاه پاسداران هم هشدار داد، حالا که آمریکا مسیر نفت و گاز به دنیا را ناامن می‌کند، مسیرهای صادراتی نفت و گاز خودش و هم‌پیمانانش بسته خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/450281" target="_blank">📅 00:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ad3bdc6d.mp4?token=P-vpmnbphm-i5tkQRDGh0DXQAcCVnhPc0tVDwgf1O_u0c8OXKdCRF8QperEx3AXEkcoiGGyAuVfcBPZVSk_9iewWpL5jsYq6i0I4ScTFNBtGSbKoexee4klPcTZ5AiKqqPOsZhhpuEugveApxRE_Inhf4--xnYw7HIGjm_clby1myHgl-shYjWnZFV_e_9GgSX6Kg43NnSYMK9nC5BJQPn5-3RsHA1JoOsN7yOMs8Le4OPE3V2dghrb_QYrVRO0mAw917dMh2jiRXfsGqJMzNmynHKb6pZkroY5wtfGkmUfsD5z3EuPZxfS4_C6RMKw9hq-WeOvZEvaXqMO0Sm_Osw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ad3bdc6d.mp4?token=P-vpmnbphm-i5tkQRDGh0DXQAcCVnhPc0tVDwgf1O_u0c8OXKdCRF8QperEx3AXEkcoiGGyAuVfcBPZVSk_9iewWpL5jsYq6i0I4ScTFNBtGSbKoexee4klPcTZ5AiKqqPOsZhhpuEugveApxRE_Inhf4--xnYw7HIGjm_clby1myHgl-shYjWnZFV_e_9GgSX6Kg43NnSYMK9nC5BJQPn5-3RsHA1JoOsN7yOMs8Le4OPE3V2dghrb_QYrVRO0mAw917dMh2jiRXfsGqJMzNmynHKb6pZkroY5wtfGkmUfsD5z3EuPZxfS4_C6RMKw9hq-WeOvZEvaXqMO0Sm_Osw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرژانتین بالاخره در دقیقه ۸۵ گل زد
⚽️
آرژانتین ۱ - ۱ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/450280" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWqsOZRwmuw1SrKvHqrsSGfKeSrBv-tdeeI4PNhNN2P7p2Vd2aWGEo2RAk5JW3ff4epTcE2s6JzQtjFZ2Yvm1DJbV6naAZHnrowMT_swD2DJ9o2HjhtPkzhbGpRiC5zSrZPnzfcF4IC7ALYzpZmiKy2s9cKAoBn1BAMRE7tG66mPXKaNO4qNh-Wo5E3aLU0LrHm_bFWORzumKqeIqRrC16CvQgO_MHANbuNHa1YC5MYcW6lg_4AGjxtGBNgflUEyclM8eQmisCnQzNNTxdvvNy4903Gdz-TeLpxzxV5yNJui9IXwzKV4BweWylq3YT1EK75F9VBIgQuxKBAxiHCrsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: درپی حملات اخیر ایران و افزایش نگرانی‌های امنیتی در تنگۀ هرمز، کشتی‌های تجاری از تردد در مسیرهای تحت هدایت نیروهای آمریکایی خودداری می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/450279" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e8e8d33a.mp4?token=ZMI0t7OhvukITLfH0sqTC-X5FrxPZPlYX5--yhs6m7IbS-EiosPQ7ZPlQgXZB2Pe3p5yRqKZho35F9RdyRWS-gf3hgLRpMWz2zTOmVj0E2oGfmqRqFxis_Mtng_zRU9kk85ypK1fco61jyYNJwTrXSP_efTb7jnfR9HM5eZfRC-YrCBKEMARBKanwW87gdFzeccir5pbmcVTQh4D1OwxYqtaqkBJKhIwKdH_Mk1abq3qeb5Vnhi2wQOzZ71aqemqCc7KeiiaLLk7nHvsM1NVKDyA0-QnevpWg6uJbUNQP_ONa9ZtHpBtPUM9WqSCGcsLM9h7DXakXSQy5ssAd2smwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e8e8d33a.mp4?token=ZMI0t7OhvukITLfH0sqTC-X5FrxPZPlYX5--yhs6m7IbS-EiosPQ7ZPlQgXZB2Pe3p5yRqKZho35F9RdyRWS-gf3hgLRpMWz2zTOmVj0E2oGfmqRqFxis_Mtng_zRU9kk85ypK1fco61jyYNJwTrXSP_efTb7jnfR9HM5eZfRC-YrCBKEMARBKanwW87gdFzeccir5pbmcVTQh4D1OwxYqtaqkBJKhIwKdH_Mk1abq3qeb5Vnhi2wQOzZ71aqemqCc7KeiiaLLk7nHvsM1NVKDyA0-QnevpWg6uJbUNQP_ONa9ZtHpBtPUM9WqSCGcsLM9h7DXakXSQy5ssAd2smwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازهم توپ آرژانتین گل نشد  @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/450278" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9641ee486.mp4?token=Op5wG278s3-XQAO07T8n66ueIiTSjywqqmGfwIelkD4MKz9yhGGpV-IBA0VP-_3udBvIJthZmr-2YnYOPn3NDTEtBVNI7lTS2VFMotjQRZNFbHXcGKRl3ZpTU05arWuffajf6rjDadh2EVN40l34pyf-mLNVOivSCg8zYXIubqG_fsFiZsNvZprSf8qOuxiHoGuca5xGY7PgnwfbuEUwtQ2MKNynMlXmBKqiMqMtzlPU733cL_O-rQ8TrPKw9JYN76K90kwbSP7XmcoUkzFNzJmGnz3_-s-KBdT3bpO3HAJ6iK4l5k8iBTEXTheo5sNSYAeWJrTnC3jUP9zMcdPNLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9641ee486.mp4?token=Op5wG278s3-XQAO07T8n66ueIiTSjywqqmGfwIelkD4MKz9yhGGpV-IBA0VP-_3udBvIJthZmr-2YnYOPn3NDTEtBVNI7lTS2VFMotjQRZNFbHXcGKRl3ZpTU05arWuffajf6rjDadh2EVN40l34pyf-mLNVOivSCg8zYXIubqG_fsFiZsNvZprSf8qOuxiHoGuca5xGY7PgnwfbuEUwtQ2MKNynMlXmBKqiMqMtzlPU733cL_O-rQ8TrPKw9JYN76K90kwbSP7XmcoUkzFNzJmGnz3_-s-KBdT3bpO3HAJ6iK4l5k8iBTEXTheo5sNSYAeWJrTnC3jUP9zMcdPNLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگداشت رهبر شهید توسط عراقی‌‎های مقیم تهران
@Farsba
-
Link</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/450277" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pSkpReJsZ47a-qjK_1946HG6uExuGrqguH4ESdyotXIu2othQxZ2g4xKbbCir8pJm4JA24_BjlJVtb5pFAaEMl_rQF_tMgjgQrx0k1Ycl87vJlMluTzeagqEbIkA9J4bjiSRjNWKmZTIA64IvkeQJb8aead4eU3GnJOdQAhaDH-bu_eXikF5TDj7Lq9q42Fd97_TsbxBChA2uEWkx4MSadlGKHE4QQSr0kgBQ1gFymKqFjfuXuXAkIikZIJO6NwXsFhnzJny3zN9J25hGwqu5ZLOw0SxmJQTPeKjcXhtbnblZp705DIWj1D_g6WogABHv0QX5-qE2AUJqnBT_DTNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7uUj4c7_zZgToQDpGhC28IZvj402sKCwViVXT6moNMqgCQgGJzUrhmH962Y7pX-qP-dHcszrP1Vb4F5zurpEMRJbG2HJtfPyPuBJlA7WCdfXyOiutPoSHS_IdjMLC3x8IT6EEs4ojrrIfHo23Pu6LElbBBF885h3D0BQuo8i_0PIkNAFR8HQUDOS54Npr2kDYjLHJDdcRrwdh1wAmNbhCqPgfWKALmb8qVZDm1CFJcUa2BNpSVgqX6ZqpWaN2nT1x2aIpFd3akcK1_y4N2lub8zeqmIeKJx-AUwFdLYh3BdGEm5jV0ZsAgC61zmtVOYbpX9WbY5FyanOBQ5sWiJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUDedeBkOlb88IqjMqdTIM24nOmZ3wPNX3PyyajDlgklinPFPRtHciAfb3uYQ97J6NQjdxNS1NY4UBB6NL1WikuuA86pr6o7OH_UqiYDTUcTIIaj65hQ3VS8GF2MHs14O9km1EoywDo__-gxrnNPMNpIS9vNtBfGhrNtalRhaNYxzW7HWO1GmrqXr6YYOimerRZ8qiLfmS8Zk_-9rFFl_ZHc5TuvLJmYUyorVoRwiGhog9Mbhy_Ww3Rvq0Kd4B8zv7AjIhO31Kem2beTURIQkKAiJOtZu-889JAJ0RHtBX11r2Iqp81V_we70q_G2hZgnj6dm8DBcLD_SrZa42wjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYvAEPW-HsOxD4lgsU3gOSTpV-CmenUT5zRw3VG09dXZjajTCidOS5P2q196fyxbpPFJEm0Lt9Op_wTyfwmBe479BlCkIaMsu2b8j5mYL0UHdW6181GuMgW_2WUsi879o_GY5pTGhvBDJn9JVcjlMI5pO0v1KOk3SXqj55vrZMmLDl6YQIPsIbTAoe8-odF3iC39i7U-mNLCqM4U4NBkicCUkkbOlqMM-6xE50oSaiCWR-FfR4GYS-B_qcOCQ3Ju_-MsfUut6-Eck4serbIOY-0A4VL7Sc3YciLPxHuoJzCt9f4MA2bAML5LWOTSgf8gfptKpZDMq2axQvzfOrLJGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از مهار تماشایی پیکفورد
@Sportfars</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/450273" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc2e80471.mp4?token=uQGPARtkbpOSEmrMncFXE1n1uQzPwFS5VAQDIyTNmdI-Fs1cvnOibB9fNeJwG5cdSjVj1Evfhk0-WA5RSIsTyPDeb4B-_ZxIO12FeWObDdTTiKs76rSu9i8Ha-zEVqlOzDhjZ7oEOYqRiAm7EXb5mj986sVtlbP9wgZjeiEUVNNfDNyMP5qA3mXf22x3DMsK-3ObSuqA4YvsQR19iPWZF0gkwnycoqKt0uTW-Q5bQC_zVL5t5O6L4mVU7nhOFCKH83fvYxVHRjetx6OtUB4RCnXTx-pbIVsxTA07LBS82L6A4St9ZzSKEdmW-8eXaz1xQTK5ue1yotiIbXytk7iDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc2e80471.mp4?token=uQGPARtkbpOSEmrMncFXE1n1uQzPwFS5VAQDIyTNmdI-Fs1cvnOibB9fNeJwG5cdSjVj1Evfhk0-WA5RSIsTyPDeb4B-_ZxIO12FeWObDdTTiKs76rSu9i8Ha-zEVqlOzDhjZ7oEOYqRiAm7EXb5mj986sVtlbP9wgZjeiEUVNNfDNyMP5qA3mXf22x3DMsK-3ObSuqA4YvsQR19iPWZF0gkwnycoqKt0uTW-Q5bQC_zVL5t5O6L4mVU7nhOFCKH83fvYxVHRjetx6OtUB4RCnXTx-pbIVsxTA07LBS82L6A4St9ZzSKEdmW-8eXaz1xQTK5ue1yotiIbXytk7iDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دروازه‌بان انگلیس، آرژانتین را در گل‌زنی ناکام گذاشت  @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/450272" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
همزمان سازمان تروریستی سنتکام از آغاز حملات جدید به ایران خبر داده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/450271" target="_blank">📅 00:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78c8753d4.mp4?token=e-Aw6CrPJT47aUrX8mXrNe4Bzf4e-VIF4eui-F4l72mRKfuFZcWscqBzv_R-q353i3I8hdEZ9uuB1vxIAhEsdbN9xaJVACGzm-tvHLM6cjXh8pptXnmmdp6KV0mZtt9NNV3uusbBlOJmNj-3tuxMLjxgEKDb561ruV6P0THKlReSJK2A2mUKf7VIEZpy4Xw1iqzfmpmym3gbFh4yEXm-t6xoDp3bRsYNTe5GkFSdTTbO1NVf-wOuq__bKXDUZx5YsOq3CTAzrT7_2IEZc9DXao-McnBAzxDdbUfhUT-iPW7e49Z_e7IJCzqcZRuJbewCgUWWjRDDZlAWpGGUTDh_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78c8753d4.mp4?token=e-Aw6CrPJT47aUrX8mXrNe4Bzf4e-VIF4eui-F4l72mRKfuFZcWscqBzv_R-q353i3I8hdEZ9uuB1vxIAhEsdbN9xaJVACGzm-tvHLM6cjXh8pptXnmmdp6KV0mZtt9NNV3uusbBlOJmNj-3tuxMLjxgEKDb561ruV6P0THKlReSJK2A2mUKf7VIEZpy4Xw1iqzfmpmym3gbFh4yEXm-t6xoDp3bRsYNTe5GkFSdTTbO1NVf-wOuq__bKXDUZx5YsOq3CTAzrT7_2IEZc9DXao-McnBAzxDdbUfhUT-iPW7e49Z_e7IJCzqcZRuJbewCgUWWjRDDZlAWpGGUTDh_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول انگلیس به آرژانتین توسط گوردون در دقیقه ۵۵
⚽️
آرژانتین ۰ - ۱ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450270" target="_blank">📅 00:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
منابع عربی: چندین صدای انفجار مجددا در اربیل عراق شنیده شد  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/450269" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SShMxzij9jmuDIUIAiuAKeNnLenNWdBOHA4yH43S4PARCTiwMZ4bHu7L07sXkj36gcSsnWHEHXwHGqHnatrSNiuoesVWecs7bFKUmyT-D13DgvdveczeoabqXbgtQWNsWdikfKcjEz8aQoqIxvlT74KqFPtrjf_at7SoAbrJHjAjuByv-ZAr5GaUfwbpuhw2PMuFytaHPD9-SHT-YvCREf_qq2BDS5RQqlf9thhIUiCzXpl5iHqT9GlGsqCaprQ_E8WTZ6drkLKYEuKe-PtZBqDNCRDJ02jHJ0gGdw4ues4JFnyNv4waRbM89Aph4jErdXmVYZkzI2CR_a-CCTbWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شباهت دو تصویر از تقابل مسی و مارادونا با انگلیسی‌ها
@Sportfars</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/450268" target="_blank">📅 23:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=r15MEnAuyg1QBhu2sOxw1gI6uyYOe5zJdNVuIhBdu45BSCdRF0y7wMtjGOz-1eyDCbSDP6EOL9oiWI0gEgTLpnwjD3u-FBPzbeFczFw8rjD9mAxI3LKDtfk6cizK0E0PsdT5bdjzlJkwTb-OTkRaqgfCD3GwpxR5t-VHgwl3I-RAt4TH398KaTCClpi3XdJQx6YHgRd89LwwOkqmh3r2LvvP5csnnyfGLfnXkhQ4GamO7OpsHSfoWOAEs4ka1dYGN0L0IAXch3pP9vxpGxOlVGQyUyeRbJgSgFNCEsRKIVNrV2OI-BHYRDxIkYm8BXYXMnn_l7RVzdSewNCQumX9ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=r15MEnAuyg1QBhu2sOxw1gI6uyYOe5zJdNVuIhBdu45BSCdRF0y7wMtjGOz-1eyDCbSDP6EOL9oiWI0gEgTLpnwjD3u-FBPzbeFczFw8rjD9mAxI3LKDtfk6cizK0E0PsdT5bdjzlJkwTb-OTkRaqgfCD3GwpxR5t-VHgwl3I-RAt4TH398KaTCClpi3XdJQx6YHgRd89LwwOkqmh3r2LvvP5csnnyfGLfnXkhQ4GamO7OpsHSfoWOAEs4ka1dYGN0L0IAXch3pP9vxpGxOlVGQyUyeRbJgSgFNCEsRKIVNrV2OI-BHYRDxIkYm8BXYXMnn_l7RVzdSewNCQumX9ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ آرزوهای خودش را تکرار کرد
🔹
رئیس‌جمهور آمریکا: ایران به‌زودی شکست می‌خورد؛ آن‌ها خیلی زود شکست خواهند خورد.
@Farsna</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/450267" target="_blank">📅 23:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ac9262df.mp4?token=RpFVUTbiYkfQYH2WjE8w7vzIfn-L_yKuL8BCvIsXE0oeAs8R9lmFLOM0NOfsgBDdUN4ctaGF2RkMH42plJ7WXLAr_1syaNS969MlF8AMwGeznd6LG6hvjxo0qb-wbjIsNKDhsmyVYAMinaH6cO2AO9LfMRlxgvqIbT9l9XMm5x_cDOoOOd5nZa1MU8OqPoQVS5uQFPIWp4-pZnLtQlrerHCIka1vVKTNkk_1rGely6KJp-6UhauSpZvILAZszdqhPoFOBpRxSnov7c4kwFpOFtDxcAhEIFSIj3pJ0b0FlMmDf9hvtOcxz-v72107wHFjR-RUnA1gU0Aye5co9v__eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ac9262df.mp4?token=RpFVUTbiYkfQYH2WjE8w7vzIfn-L_yKuL8BCvIsXE0oeAs8R9lmFLOM0NOfsgBDdUN4ctaGF2RkMH42plJ7WXLAr_1syaNS969MlF8AMwGeznd6LG6hvjxo0qb-wbjIsNKDhsmyVYAMinaH6cO2AO9LfMRlxgvqIbT9l9XMm5x_cDOoOOd5nZa1MU8OqPoQVS5uQFPIWp4-pZnLtQlrerHCIka1vVKTNkk_1rGely6KJp-6UhauSpZvILAZszdqhPoFOBpRxSnov7c4kwFpOFtDxcAhEIFSIj3pJ0b0FlMmDf9hvtOcxz-v72107wHFjR-RUnA1gU0Aye5co9v__eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول انگلیس به آرژانتین توسط گوردون در دقیقه ۵۵
⚽️
آرژانتین ۰ - ۱ انگلیس
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/450266" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
وقوع انفجار در چابهار
🔹
دقایقی پیش مردم چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔹
دقایقی پیش بود که منابع عربی گزارش دادند صدای چند انفجار در کویت شنیده شده است. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/450265" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c164874f0.mp4?token=bHyUiZ4FpI_ern0dfNySop2eECkGJWboBmpvHyALmhMdP8zey8Rj_bPjSwZNxUBVxXoa8WsZxa_Xqp34XVWNBaH_LjNPmE7m-25JIh-XVchqrquE62DVehnz5sirAkktewx86JmMBZIiRQdZUr8Ivn7LfhZnlF0-7OEEL6rmcCsgr18RWLisxqt5Gk0m4VLjs3HAGQh06vUdxBBhrQg-aQuFWxQz98z_HHnOFBXaqrQBR-NSh2-PvODJVIS2C4IdPivs-eqxiKDvD0Mt5e1_CVWsp9vn9DRHxZSUwrNg3JQNUKjEQ2XFzfx6ZVX1pb9laVq5CxfuU0TIDnSTVM5aCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c164874f0.mp4?token=bHyUiZ4FpI_ern0dfNySop2eECkGJWboBmpvHyALmhMdP8zey8Rj_bPjSwZNxUBVxXoa8WsZxa_Xqp34XVWNBaH_LjNPmE7m-25JIh-XVchqrquE62DVehnz5sirAkktewx86JmMBZIiRQdZUr8Ivn7LfhZnlF0-7OEEL6rmcCsgr18RWLisxqt5Gk0m4VLjs3HAGQh06vUdxBBhrQg-aQuFWxQz98z_HHnOFBXaqrQBR-NSh2-PvODJVIS2C4IdPivs-eqxiKDvD0Mt5e1_CVWsp9vn9DRHxZSUwrNg3JQNUKjEQ2XFzfx6ZVX1pb9laVq5CxfuU0TIDnSTVM5aCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کازرون همچنان در میدان ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/450264" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
سنگری که پس از ۱۳۷ شب همچنان پابرجاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450263" target="_blank">📅 23:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9ac763854.mp4?token=HfFB8vGtrsGAIfjRN8WztUBl8WCG-Ps8G4DQtSbDlGVtjZ-y1bvfS3M8iw08RkRx0ydhC7UhcTbsaCI_SkwzcYz9eEAMN1nVfMAYKm8j0paBSxi_dQMTytZw1zeWDc0HssngGXIejR2KF9CwOHsSjt1CGXfwyZ3pN5L0DD9Qn6DMxqDa_bKLPLs4Kn447DMlaFhnIrbGJROCxc7UeRZLsF_clwK_NTSKvJiklSKkqAUPp8yI2pf7AtI1Ni4YBWwRd3FKrVrRXeFv4IBaO8U02Jl0HJV582adGAjwYe-oPqCMj1J2v8tQzM_Vfe3aNS6clmnYaK3dp6o4CfDGbDgku6U5H3AvvOP97wknoNhmXYwAxotOKhnRkrG4e9-C7SGZY3bgayC1ZDwbogWPUMTktoIupx_uqpE9ZzebgYio4Abr6_dUl14UbdU7why28RylMHRlBfeJifTT8eADwI1wSbsi3w3Ak66k_gWuJctyEmqTRxmKBF0vt5hrqNWGZtTR1fp1C7o3O6FqCEViDgK_WgpgIMWmZTeqwufH-4ljAdBY7TfjSpm2rZQdJrUXpdMpm5n-USj5DU82kiiv-tliv6q2XyvK7jSRno2LJ6XsuG4ys-2--MqbpyTnIJsBor_N7J7o5oFVRW6Ueu_1_HytA02HWfO7QjYWsS61WaA-5gI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9ac763854.mp4?token=HfFB8vGtrsGAIfjRN8WztUBl8WCG-Ps8G4DQtSbDlGVtjZ-y1bvfS3M8iw08RkRx0ydhC7UhcTbsaCI_SkwzcYz9eEAMN1nVfMAYKm8j0paBSxi_dQMTytZw1zeWDc0HssngGXIejR2KF9CwOHsSjt1CGXfwyZ3pN5L0DD9Qn6DMxqDa_bKLPLs4Kn447DMlaFhnIrbGJROCxc7UeRZLsF_clwK_NTSKvJiklSKkqAUPp8yI2pf7AtI1Ni4YBWwRd3FKrVrRXeFv4IBaO8U02Jl0HJV582adGAjwYe-oPqCMj1J2v8tQzM_Vfe3aNS6clmnYaK3dp6o4CfDGbDgku6U5H3AvvOP97wknoNhmXYwAxotOKhnRkrG4e9-C7SGZY3bgayC1ZDwbogWPUMTktoIupx_uqpE9ZzebgYio4Abr6_dUl14UbdU7why28RylMHRlBfeJifTT8eADwI1wSbsi3w3Ak66k_gWuJctyEmqTRxmKBF0vt5hrqNWGZtTR1fp1C7o3O6FqCEViDgK_WgpgIMWmZTeqwufH-4ljAdBY7TfjSpm2rZQdJrUXpdMpm5n-USj5DU82kiiv-tliv6q2XyvK7jSRno2LJ6XsuG4ys-2--MqbpyTnIJsBor_N7J7o5oFVRW6Ueu_1_HytA02HWfO7QjYWsS61WaA-5gI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحید جلیلی: غرب‌گراها از برخورد احساسی نسبت به پدران فکری‌‌شان اجتناب کنند و بگذارند ملت ایران عقلانی رفتار کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450262" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZ80Zo49aBBbk_93wbajVSPodZkqCRXn_kmxQng_DboCy09B9prNata1ci55ihPNAQSDhe1c-7r6xQEwdgQ3aRBiHdF0KBKMoVPXKXmVRkT3T9lchoAjDMWf-ML0sDMsoR2FNNgvMkOi1szmLj7nUdtMF1C3TY9Qw6xq_ThwHQjHdwf2lsJgzUbEARMuq-R7uIGtGpBn8sWvDLobPz6FR4t22rDp4PcV31bOXYeNHRCSDWpLoRlgC4OjwOPnrePDdUvVeYNPFkL3IqX00l0MTfSWTvzWL8TCPP0L8r6bO4hs4c_lF6ujqHgRJnL3z6CILUuE9MOs-3lGpCbLmT_wZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LA54NZH4Mz4L4eIoae16Gt0tgmojHHwSY9NSEZMLN1M6EURYiwQVYgfXzhZhJKTWTKl483ATyEctU9hjoPA89m1RFC-dO1i57-t8QnVlJ1-7HF7k6NpDfHE8oZuIilXAxwmuXN_fBMzvKknEEHVc2OC3F4m8nI34UZgyYO7N10ga_VKQyk7JHe4KxWOHAR9mf2r3HJgIc80o_EcunIMg5Kx4y7wWUeI7hMbznWjLuoq6QQf9SHxV4-Azsu3W1JCp8HpSLxAl2dz2PwG4M3Bz5xaeRn1cYwrR9M7gFUsgc5ZVL9nIPa_CY12Nbb1wTQTnCyOw6KM8iKtRWtN0_y45lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WEWmNVd1X6T4cI2cF7jNI3NM2vi18dJj1sZJNzXxuFF16gEsJd1qD26KLqNbA_R4Be6GTSBXCtp0BFpHFa_T57bmPTrZUIRxB6lxHIGHtwcHoedKenSukNX9uEcK6XmklrC8hTFvydb8wPC3PSQPbVfMeiTnhvXBCd4uXtIpKKXU4XkL1v7sVME4qV90bOQQkBv_OLPfos6zxQ7spH9ZArrA15s_vfUFEi95OF6s2d-hQtN9lv7EpOka-JsfDisLQzgD-svr7Y4b939zJvBzt_zT-vKZ4Mhbi-8vlBXBNCYKmpYedUdMcSXR0nK8y4wGRJWqn1QTWM-pc4deByrtcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFm7TBJ1uCQv23f_o_50OPCreG4za8NNjy8kqTA5Ed6pl8NKw1Q___a-Y_WP0QOPnlj-xxMszOMUtfPrDYgv6pXrgLDL6WQapG8e0Hsan_ugkG3kFjTgJ89LMXvn9kch8eoqUx0Y26YolKDI0uhFfwQtoV8A5srW39omXwz22xagA2wqrLIU2K3N6VWOzMW_9E2t68kXBfnRncILxkm6c-Rcd7Gx68Y52TtwIBKyFoaoac83q9nwIhLCZ8jODAxv78SAORgH04WFKm2vquVIdcKjpdlasdb5L9UTvAWTX04wjDQ9Sl60xJkB2UUfAVFW7LJoC_4elZ2dZF1lDAYfcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم گرامیداشت رهبر شهید ازسوی آیت‌الله سیستانی
🔹
این مراسم باحضور حجت‌الاسلام شهرستانی، نماینده تام‌الاختیار آیت‌الله سیستانی در ایران و جمعی دیگر از علمای قم برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/450258" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">معاون نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها: اخراج کارمند دانشگاه علامه به‌دلیل تذکر حجاب را تا برخورد با مدیر دانشگاه پیگیری می‌کنیم
🔹
کرمی، معاون فرهنگی نهاد نمایندگی مقام معظم رهبری در دانشگاه‌ها، در واکنش به اخراج یکی از کارکنان دانشگاه علامه طباطبایی به‌دلیل تذکر دربارهٔ رعایت حجاب، گفت: «اخراج کارمندی که دغدغه‌مند پیگیری پوشش قانونی در دانشگاه بوده، اقدامی فراقانونی، سلیقه‌ای و بنیادگرایانه است که حتی در کشورهای لیبرال نیز مردود است.
🔹
تا بازگشت این کارمند به محل کار و برخورد با مدیر مربوطه ماجرا پیگیری خواهیم کرد و اجازه نمی‌دهیم به ساحت دین و دینداران در دانشگاه توهین شود.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450257" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌
🔴
منابع عربی: از دقایقی پیش صدای چند انفجار در کویت شنیده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/450256" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f147e9804.mp4?token=PnH7BfZcbgAn4Z1FNhaz01e2iYyuBsVh2vnC0EOXkNMZ0QGCf1nm1ywcZVxjjlw_rzZSKdBJdRf6et659kJwFLTI89lwVJs5xOaEw4ygamGcgXkXiQg2vJ6zXYFve_KlHgoOcwOIrObgdbD_GS_KvR0vg7_tqrlruPPi5IG0AoIkMuZ82Rzf4wdb2XM6IijfS5sXkUz_Clilf93wTZGLMfcUyuhr5COIebiVqhDdhQ3J3lB1bxA2biPaIdnAEK6udNKfSJMcbZ28UbRDINWZzOZSBbf09U1ekHbVWl7Fk2d7f-r0TKJuumy7lqVpbFpbRFHA3qDrbmNMwsLpYIP-3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f147e9804.mp4?token=PnH7BfZcbgAn4Z1FNhaz01e2iYyuBsVh2vnC0EOXkNMZ0QGCf1nm1ywcZVxjjlw_rzZSKdBJdRf6et659kJwFLTI89lwVJs5xOaEw4ygamGcgXkXiQg2vJ6zXYFve_KlHgoOcwOIrObgdbD_GS_KvR0vg7_tqrlruPPi5IG0AoIkMuZ82Rzf4wdb2XM6IijfS5sXkUz_Clilf93wTZGLMfcUyuhr5COIebiVqhDdhQ3J3lB1bxA2biPaIdnAEK6udNKfSJMcbZ28UbRDINWZzOZSBbf09U1ekHbVWl7Fk2d7f-r0TKJuumy7lqVpbFpbRFHA3qDrbmNMwsLpYIP-3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت سرکش آرژانتینی‌ها از بالای دروازه انگلیس بیرون رفت
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450255" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
وقوع انفجار در چابهار
🔹
دقایقی پیش مردم چابهار صدای چند انفجار شنیدند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔹
دقایقی پیش بود که منابع عربی گزارش دادند صدای چند انفجار در کویت شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450254" target="_blank">📅 23:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">احضار سفیر انگلیس در تهران به وزارت امور خارجه
🔹
درپی اقدام ناموجه دولت انگلیس در قرار دادن نام سپاه پاسداران در ذیل قانون مقابله با تهدیدات دولتی، هوگو شورتر، سفیر انگلیس در تهران، امروز به وزارت امورخارجه احضار شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450253" target="_blank">📅 23:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450250">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
رسانه‌های عراقی از حمله پهپادی به پایگاه نظامیان آمریکایی در نزدیکی فرودگاه اربیل خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/450250" target="_blank">📅 22:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450249">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVMCU2N9ugSJRpS1Zdx0FRilwJOPnKrQFSht-LRTCN5SG3oBAivuuejkTfz9kL3GNIcnzTGA46O9KpSpjCvZDrmqwsoU0iiZqedzX-gIIAvPC17C4jegCShZjECAiH3LxpEKwDgJTHMu9tx3U2jHD0fDXmrvfBc0DASCjkJir5vV-B3OZlzHKxd8Z1NjICaq2SG4lvTFUYxooXX8WoKwY0QdgKYfi947vW2KkQkaZ8Cjwg_5HUT7xylSBBaAlaLkSawDxtvjEag2ZmxkmkbvryGodU2tZhHuh7vOiLxddlUCKz6KeUnk1yV6Q4ll8C8T3dUByBqKrCwfp8sLcYTBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: به
‌
دلیل تنگه هرمز تنها راه‌حل با ایران دیپلماسی است
🔹
ونس: من عمیقاً از آمریکایی‌هایی که می‌گویند مذاکره با ایرانی‌ها غیرممکن است، ناامید شده‌ام.
🔹
تهدیدی که ایران به‌طور نامتناسبی در تنگه هرمز ایجاد می‌کند، نشان می‌دهد که تنها راه‌حل این منازعه، دیپلماسی است.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450249" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450248">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در اهواز
🔹
دقایقی پیش مردم اهواز صدای چند انفجار شنیدند.
🔹
همزمان سازمان تروریستی سنتکام از آغاز حملات جدید به ایران خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450248" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450246">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847daa71d0.mp4?token=X-Jw3bQKnnz0v3BgNu9XVJKcdN4RNCmi2DQSr5NqZMbtvP8s6JyB-6xxRCCFzrMNNW_QI6aiCY_1-20KNa65OEqvcQB98V611YnAF2XORNzALHwO4yWDSa73PPfgdEuYZIgtrjE5tMisXcP9zwX2dVqvJoWb6oGpdWrEv6Y1XC1zHifZMh9aS22_l49Tpon7tiM5QUPit6uS-nR35_3pyAe0P3qV-3249LAgjHclP2AMED-T5X8YELXS5T0SOofj6ze926bncUjDQkf5-27YdByiR92QqyGa77k1Dho1sfNvb2ZCx8pWdEHCSTTUU9YBfYwt6OTW9gjoVgKMa9rL-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847daa71d0.mp4?token=X-Jw3bQKnnz0v3BgNu9XVJKcdN4RNCmi2DQSr5NqZMbtvP8s6JyB-6xxRCCFzrMNNW_QI6aiCY_1-20KNa65OEqvcQB98V611YnAF2XORNzALHwO4yWDSa73PPfgdEuYZIgtrjE5tMisXcP9zwX2dVqvJoWb6oGpdWrEv6Y1XC1zHifZMh9aS22_l49Tpon7tiM5QUPit6uS-nR35_3pyAe0P3qV-3249LAgjHclP2AMED-T5X8YELXS5T0SOofj6ze926bncUjDQkf5-27YdByiR92QqyGa77k1Dho1sfNvb2ZCx8pWdEHCSTTUU9YBfYwt6OTW9gjoVgKMa9rL-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پروژه آشوب با تصاویر قدیمی؛ ادعای تجمع در پاساژ چارسو تهران تکذیب شد
🔹
عصر امروز، چهارشنبه ۲۴ تیرماه، تصاویری با ادعای اعتراض مردم در پاساژهای چهارسو و علاءالدین تهران از سوی برخی اکانت‌های ضد انقلاب در شبکه‌های اجتماعی منتشر شد. شماری از کاربران در شبکه اجتماعی ایکس نیز با انتشار مطالب مشابه، این ویدئوها را بازنشر و تأیید کردند.
🔹
پیگیری خبرنگاران میدانی خبرگزاری فارس از کسبه پاساژهای چهارسو و علاءالدین نشان می‌دهد که امروز رخدادی با این مشخصات در این محدوده تجاری مشاهده نشده؛ همچنین، پیگیری‌ها از نهادهای انتظامی نیز برگزاری تجمع مردمی در تهران را تأیید نمی‌کند.
🔹
بررسی‌های تیم راستی‌آزمایی خبرگزاری فارس نشان می‌دهد بخش قابل‌توجهی از ویدئوهای منتشرشده مربوط به حدود ۷ سال پیش است و به دلیل شباهت شرایط نوری و پوشش افراد با روزهای جاری، عامدانه برای تحریک مردم انتخاب، فرآوری و توزیع شده است.
🔸
عبدالرضا صدیق، کارشناس حوزه امنیتی، معتقد است انتشار این تصاویر بخشی از یک «عملیات روانی» از سوی چند رسانه فارسی‌زبان معاند خارج‌نشین با هدف تحریک بازار تهران و ایجاد دوباره ناآرامی است.
🔹
در یکی از تصاویر منتشرشده، رادیو زمانه برای باورپذیرتر شدن محتوا، تاریخ ۲۴ تیرماه را بر روی تصویر درج کرده است؛ در حالی که بررسی‌های تیم راستی‌آزمایی این خبرگزاری نشان می‌دهد این ویدئو ۲۵ تیر ۱۳۹۸ ضبط و منتشر شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/450246" target="_blank">📅 22:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450245">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
ناگفته‌هایی از مراسم تشییع رهبر شهید از زبان سردار حسن‌زاده
🔹
رئیس ستاد تشییع آقای شهید در تهران از محدودیت‌ها و تلاش شبانه‌روزی دست‌اندرکاران برای تشییع رهبر شهید در تهران می‌گوید.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450245" target="_blank">📅 22:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450244">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
المیادین: سامانه‌‌ پدافندی کنسولگری آمریکا در اربیل فعال شده است. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450244" target="_blank">📅 22:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450243">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=bHWu_48jPQMUDPmVUlamdl7wfb-EbunLljJR1E_cumKGtl9n_ruhaAKYcRaqYSFcbpBnRud6TV9RuaMJjpBfexTUyQR4c8MiVtnFaiLQwgCEdA-SdVt1xu-NQMsEIVfXxOHLs2eNKEBjLbnqkWi8xNF0p5iwKCUWTQ2_nYRY5A6Ys_DYlgwUW5ZYaXsEBrRcLiBE7DYyT_T61yHbzyonJGnCx35T5bJVOOu8B7QBO7d7z6nCrYxAcWKS9ajtJex7FAFJI3ZV6b7sa8Apy6dtrRVOTJLzD0uJmg5zEcmeZhyw5e8oAklhJgZSW4Nu0unoSjvkh8UzbTVnBp1nyq6xUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=bHWu_48jPQMUDPmVUlamdl7wfb-EbunLljJR1E_cumKGtl9n_ruhaAKYcRaqYSFcbpBnRud6TV9RuaMJjpBfexTUyQR4c8MiVtnFaiLQwgCEdA-SdVt1xu-NQMsEIVfXxOHLs2eNKEBjLbnqkWi8xNF0p5iwKCUWTQ2_nYRY5A6Ys_DYlgwUW5ZYaXsEBrRcLiBE7DYyT_T61yHbzyonJGnCx35T5bJVOOu8B7QBO7d7z6nCrYxAcWKS9ajtJex7FAFJI3ZV6b7sa8Apy6dtrRVOTJLzD0uJmg5zEcmeZhyw5e8oAklhJgZSW4Nu0unoSjvkh8UzbTVnBp1nyq6xUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عامل اصلی آتش‌زنی فرمانداری و کلانتری شهرستان دهاقان به دار مجازات آویخته شد
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450243" target="_blank">📅 21:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450242">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044aa9d3c.mp4?token=U4wnVoa5sGJFvITlOEyqotavuEqGP9P_L8T94UMaslkB4Hc6hu2aPHcVmWrtsfOBeM68sM8ZU5e3yVzvoEKeW3oHdlw2hc9xJP0zyV-sJin36yrXXveHr1gkqJseKZco_Ot4JtDTh1_mzCVZBCVxXjuI8_Ia1XdqDHRqpiSBHgicJLwRrg1z8nKu7FDcxMTE09UDtYmltPJevDsw5a48ybP_Rqb6EfsI09zig_q1ILYdvx44PQZNMg7U_cVDNULn1Gl1qh1HAambLZTiw3SGUBS_OkJjFJt5MkaiECBF9beo-lBuo2WIfCjlq0Y0A0sl3B6fkjPeJkSUFS578nTduhDM5Lrom7GGXN1jfhhRynrJo1iR58HCur18j5iWEtvR3zIHfQRCf7d08m2pBLfoE_Mw9W7J-30CEvdRYJCMvOH9YkoVO7x-7UHzOPlW6Og7Iy4Mb6bxu2A29r10uFr0O6MezuH5qj3IqBonI9Yhynl3QhXyuB5UrzspWLZJchdeJZf3Y4IbXqL8mUobXpLUQYGc-3hii2g4QmdPaklSyUc1eR-7cKWqTurFxqpxMo9V4L30Wzqmq1fqzzP0vPW6PK6w08bbjsPafc3iqvZTLnHtj2qDx39_ut2q9hRaZl4CD12uc3jZn3AztitAJsCJv1NpxN95-LXY6b-gORLJH-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044aa9d3c.mp4?token=U4wnVoa5sGJFvITlOEyqotavuEqGP9P_L8T94UMaslkB4Hc6hu2aPHcVmWrtsfOBeM68sM8ZU5e3yVzvoEKeW3oHdlw2hc9xJP0zyV-sJin36yrXXveHr1gkqJseKZco_Ot4JtDTh1_mzCVZBCVxXjuI8_Ia1XdqDHRqpiSBHgicJLwRrg1z8nKu7FDcxMTE09UDtYmltPJevDsw5a48ybP_Rqb6EfsI09zig_q1ILYdvx44PQZNMg7U_cVDNULn1Gl1qh1HAambLZTiw3SGUBS_OkJjFJt5MkaiECBF9beo-lBuo2WIfCjlq0Y0A0sl3B6fkjPeJkSUFS578nTduhDM5Lrom7GGXN1jfhhRynrJo1iR58HCur18j5iWEtvR3zIHfQRCf7d08m2pBLfoE_Mw9W7J-30CEvdRYJCMvOH9YkoVO7x-7UHzOPlW6Og7Iy4Mb6bxu2A29r10uFr0O6MezuH5qj3IqBonI9Yhynl3QhXyuB5UrzspWLZJchdeJZf3Y4IbXqL8mUobXpLUQYGc-3hii2g4QmdPaklSyUc1eR-7cKWqTurFxqpxMo9V4L30Wzqmq1fqzzP0vPW6PK6w08bbjsPafc3iqvZTLnHtj2qDx39_ut2q9hRaZl4CD12uc3jZn3AztitAJsCJv1NpxN95-LXY6b-gORLJH-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک خطای راهبردی دیگر از ترامپ
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450242" target="_blank">📅 21:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450241">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28580c3d5d.mp4?token=Su2pRTdGGo8ZImxsuRmsa7XXSOFVZ93cFbK8ac1el6MM23QqeLVxem1HQdoz9ugzdEwbKdjhqCIPUuBPqxi3mqBH2ZbYCHJfOaPRUG3NE3j08Ja0T1Sz_K1t-ogTGQ6ntd0s1l5Mo7Re6nBzcteLXGe5zLzkGMdA5pZhLDJ-z_wXryCfK-IBxTYtzVRA5oDt41O0d8Md0pYbokDXTH6cXBbIIL3WbyBQz9ewg8eA5VlBo_TWQROKat-FQUFCa8yWW2wAKdnLN5eiGJcjG2PqCe0_1NzR-fN52X6FHgjSwfLYZswa16sGSwGcdB8xn-e5oF76S_iedxy7BgONdSLGW7y0cx8HTsYzi7EZylbL_e9YbREFzhFS6p3nD-TLIw57hFWP0Rckj9pd_187qgZ8NGNkoaeQaueqf7qJlfz7QI9OHcdiiOh3IY8avpNGwudpAZvox1BA4xMA4PA9wiwCBHq8njabuBqBS4utzUD2yEANZ159al376Jm6cd47NjoFNfVTFObKUi2ZQ7ZQPmafvfpy0kPNZs5eaRsx_-rCbbU384mFcjW0mHyv9PMD1x4pjqamYCOqy7fwAIdtgrLosTzUw7-O94FaU3dduBBVLSElk_T24s7cF3HZInywwRSNhrioRX0t8ypKRXVIICDLrL6Ms2E16wjWIyOzwOV1XLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28580c3d5d.mp4?token=Su2pRTdGGo8ZImxsuRmsa7XXSOFVZ93cFbK8ac1el6MM23QqeLVxem1HQdoz9ugzdEwbKdjhqCIPUuBPqxi3mqBH2ZbYCHJfOaPRUG3NE3j08Ja0T1Sz_K1t-ogTGQ6ntd0s1l5Mo7Re6nBzcteLXGe5zLzkGMdA5pZhLDJ-z_wXryCfK-IBxTYtzVRA5oDt41O0d8Md0pYbokDXTH6cXBbIIL3WbyBQz9ewg8eA5VlBo_TWQROKat-FQUFCa8yWW2wAKdnLN5eiGJcjG2PqCe0_1NzR-fN52X6FHgjSwfLYZswa16sGSwGcdB8xn-e5oF76S_iedxy7BgONdSLGW7y0cx8HTsYzi7EZylbL_e9YbREFzhFS6p3nD-TLIw57hFWP0Rckj9pd_187qgZ8NGNkoaeQaueqf7qJlfz7QI9OHcdiiOh3IY8avpNGwudpAZvox1BA4xMA4PA9wiwCBHq8njabuBqBS4utzUD2yEANZ159al376Jm6cd47NjoFNfVTFObKUi2ZQ7ZQPmafvfpy0kPNZs5eaRsx_-rCbbU384mFcjW0mHyv9PMD1x4pjqamYCOqy7fwAIdtgrLosTzUw7-O94FaU3dduBBVLSElk_T24s7cF3HZInywwRSNhrioRX0t8ypKRXVIICDLrL6Ms2E16wjWIyOzwOV1XLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مادر، سرزمین، سرزمین مادری
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450241" target="_blank">📅 21:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450240">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e48d78c83a.mp4?token=o1sT7L0aGJmchIxf6zx9d0vCDPPOt4qu2uJV_NdhSMDQXFlUSbnQbAIQDk1U4XGKMpGHbb4-j8WW9IjbVol1jhbwpJpa9ZOsc62WkzOVEoAzs1qGu8lrQIICPl6v83B9dai015OMOekHcEBJ__CouVXFmOXOd-Qjo1sgJzoEtAfHZBmzoq2jtYaiREHjftyNuHxGPPkaZrc74KZg5ecuxt5W9qVDoKSz6Q3SVOBLXxiKr9UCkx3LY-p8eJ4ber8b0SzUUy3AUYvDKmwPAq1lqR-8IkJEuJw2XbcSYoY1OKuJCQwH-rc7hbL6nkbcZyhJKugK176yAJQ1SDrJmYxAgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e48d78c83a.mp4?token=o1sT7L0aGJmchIxf6zx9d0vCDPPOt4qu2uJV_NdhSMDQXFlUSbnQbAIQDk1U4XGKMpGHbb4-j8WW9IjbVol1jhbwpJpa9ZOsc62WkzOVEoAzs1qGu8lrQIICPl6v83B9dai015OMOekHcEBJ__CouVXFmOXOd-Qjo1sgJzoEtAfHZBmzoq2jtYaiREHjftyNuHxGPPkaZrc74KZg5ecuxt5W9qVDoKSz6Q3SVOBLXxiKr9UCkx3LY-p8eJ4ber8b0SzUUy3AUYvDKmwPAq1lqR-8IkJEuJw2XbcSYoY1OKuJCQwH-rc7hbL6nkbcZyhJKugK176yAJQ1SDrJmYxAgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون شرکت برق تهران: هیچ جدول خاموشی برای تهران منتشر نشده
🔹
برنامهٔ خاموشی‌های احتمالی را از اپلیکیشن «برق من» پیگیری کنید.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450240" target="_blank">📅 21:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450239">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
منابع عربی: چندین صدای انفجار مجددا در اربیل عراق شنیده شد  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450239" target="_blank">📅 21:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552d85ba2e.mp4?token=HqxOzpEzyYTq3HKi-RfKMogirAuWaAhCBnYK1GxIK3L0MqrN2kh12LQAuK-RtTELKzB2Vv3C6ifj5F2OThXHqUzEtFYxTSxZzlWE7W8z48_TODDKNAclS4TIk76Kazx-medbuTuVfHjWAnAJD01NFr6bGxegCYqG4vN4dL4LXUoGCuhGNVLWlp_dznBWq9YwdeYa_5SxRTmsHRBN5avRd_Nbw6fIL_mPsmFnMRU0QKyvekIKa2F6BWEObITonLkd6qZ0aYxJxJDUcORhQOnxPWfN-ZtlzR13FolXhjAgsH4pP641vMvFFTuIlatWb19-mBbsplqNY-Dr51QUtAuCAafIrdrlggDyZWJUFWRHWVIOXTYg3b0fYw5CA-xS0v3l-2GTku8g1W4BTIMP_QwrvfahTK8EEX_9VP1pK0kodl38aQHQAhVpdVn6QGBObtlTjQZnh2AJS0KkN88xV-PGbWFNAk5sYAtRR80kL3gJ2q-V8ueWNkON_XJoGEELeyNkq4C4Us-imTHIdqzU6_an_HXyr-s4NVBhfUZzUA0dJ9cx_XyYKcAmI0kiOTbzdVAPZtW5T_WCENYnNqMATtDm1DlPt8zWurUgejKvSWeR7qC4ISJ5ZkW1SDQyrkKdXLF5XjRuW1Zfptn7fmXwZbyHZq8HkHQ-HCVA_LnRezuDLMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552d85ba2e.mp4?token=HqxOzpEzyYTq3HKi-RfKMogirAuWaAhCBnYK1GxIK3L0MqrN2kh12LQAuK-RtTELKzB2Vv3C6ifj5F2OThXHqUzEtFYxTSxZzlWE7W8z48_TODDKNAclS4TIk76Kazx-medbuTuVfHjWAnAJD01NFr6bGxegCYqG4vN4dL4LXUoGCuhGNVLWlp_dznBWq9YwdeYa_5SxRTmsHRBN5avRd_Nbw6fIL_mPsmFnMRU0QKyvekIKa2F6BWEObITonLkd6qZ0aYxJxJDUcORhQOnxPWfN-ZtlzR13FolXhjAgsH4pP641vMvFFTuIlatWb19-mBbsplqNY-Dr51QUtAuCAafIrdrlggDyZWJUFWRHWVIOXTYg3b0fYw5CA-xS0v3l-2GTku8g1W4BTIMP_QwrvfahTK8EEX_9VP1pK0kodl38aQHQAhVpdVn6QGBObtlTjQZnh2AJS0KkN88xV-PGbWFNAk5sYAtRR80kL3gJ2q-V8ueWNkON_XJoGEELeyNkq4C4Us-imTHIdqzU6_an_HXyr-s4NVBhfUZzUA0dJ9cx_XyYKcAmI0kiOTbzdVAPZtW5T_WCENYnNqMATtDm1DlPt8zWurUgejKvSWeR7qC4ISJ5ZkW1SDQyrkKdXLF5XjRuW1Zfptn7fmXwZbyHZq8HkHQ-HCVA_LnRezuDLMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فشار بر خبرنگاران خارجی پس از پوشش مراسم رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450238" target="_blank">📅 21:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0868a52354.mp4?token=RL2EAa6cK-RF_Rrn6IOufhqKT5u06QgPN0xnt0UZ1Oi6_qbltpORVOaXgh7c4Tvu9lK6Q9umie9w-lSnGDBnA5LcBABzqNc7NckmCWdtZ_vIUue2_R3JJn87M7DL6GqCmlMYT1YRr5vhE4M45AOTEtU-83y2JDaDL8yma8aokrU8oK8XQYaYj6RUnGm9Pab0cExdB60Ug2b3OA5yoClt9gXJ9J2ujLGWb23fqLrNDPQTgRHDlfAqLI7d0pMIrDt-ADghlt7lwMndqViuJC1Scsvt-rmk-wfAFoSXH5f17MdGLTKSjLvAdAS1MydKCvoTUkigtlr8BteMljQ9dEduKCt_4phcZmNXRp9lOSXWMhiN1Phimc0ULJeVlhJmrV-crqOhW4J8HPy18s7JWkMYcrZiH9-5DBJ70ZFEbXidmdVHa34ANnlVBpyuIfP8sVbRmklOoWeAfsX99O7CvHFk-fDw-8Qv5XtCqkcB8TTW0DJQ58ZA6jkBfIFX4erxCBwEyLOQbQfjLDP1IZqElweXpkmt1ZugRxLNYgf4Wj0e6TPc6DmtKOoo014qUP42GhSLry8R0i6pO47E4kCSaG27GO6MtXrgA0HSwAI8l2eC5wuM7XYzlEDf0Kll-v3wMVYX72z8uQvwbNep260RgRf4Sdsgtcta-SIxpWsRqYcx4Vc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0868a52354.mp4?token=RL2EAa6cK-RF_Rrn6IOufhqKT5u06QgPN0xnt0UZ1Oi6_qbltpORVOaXgh7c4Tvu9lK6Q9umie9w-lSnGDBnA5LcBABzqNc7NckmCWdtZ_vIUue2_R3JJn87M7DL6GqCmlMYT1YRr5vhE4M45AOTEtU-83y2JDaDL8yma8aokrU8oK8XQYaYj6RUnGm9Pab0cExdB60Ug2b3OA5yoClt9gXJ9J2ujLGWb23fqLrNDPQTgRHDlfAqLI7d0pMIrDt-ADghlt7lwMndqViuJC1Scsvt-rmk-wfAFoSXH5f17MdGLTKSjLvAdAS1MydKCvoTUkigtlr8BteMljQ9dEduKCt_4phcZmNXRp9lOSXWMhiN1Phimc0ULJeVlhJmrV-crqOhW4J8HPy18s7JWkMYcrZiH9-5DBJ70ZFEbXidmdVHa34ANnlVBpyuIfP8sVbRmklOoWeAfsX99O7CvHFk-fDw-8Qv5XtCqkcB8TTW0DJQ58ZA6jkBfIFX4erxCBwEyLOQbQfjLDP1IZqElweXpkmt1ZugRxLNYgf4Wj0e6TPc6DmtKOoo014qUP42GhSLry8R0i6pO47E4kCSaG27GO6MtXrgA0HSwAI8l2eC5wuM7XYzlEDf0Kll-v3wMVYX72z8uQvwbNep260RgRf4Sdsgtcta-SIxpWsRqYcx4Vc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروی هوایی روسیه ۳ کشتی باری اوکراین و ۴ قایق بدون سرنشین اوکراینی را به این شکل هدف قرار داد
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450236" target="_blank">📅 21:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450235">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c22bbbdae.mp4?token=TAGy2r5mvZguMn6K2-2wh1h7aM2enVi303eG5FD1-cR-8U69pWV6MJHcF_TTmFkFU_ADjuOpTWJFi-G3Shr1sGOBvnChZO1S4qdgmRpakoAdTKkPpxTGkKgxJRGEE7-b48Wwn2IPRgOe-Q0W8ms237RutDigLjyLxwVd0iW-RlCQQrsJ1X2pEWGOBfFO4sXMUx8ZpSdgxVYi2lMFA4PU32NSBwe2nbZ2kA3EYKeuUA4OuLmEUla_DtOfUBouDfMrWPdCaP_L1R3z9h1RRd4iST04MC0bTSgA8VDJkggIjyXOORZDJ900_7QREd3ittzN2Ar9gEqPk7fDL_MCo523Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c22bbbdae.mp4?token=TAGy2r5mvZguMn6K2-2wh1h7aM2enVi303eG5FD1-cR-8U69pWV6MJHcF_TTmFkFU_ADjuOpTWJFi-G3Shr1sGOBvnChZO1S4qdgmRpakoAdTKkPpxTGkKgxJRGEE7-b48Wwn2IPRgOe-Q0W8ms237RutDigLjyLxwVd0iW-RlCQQrsJ1X2pEWGOBfFO4sXMUx8ZpSdgxVYi2lMFA4PU32NSBwe2nbZ2kA3EYKeuUA4OuLmEUla_DtOfUBouDfMrWPdCaP_L1R3z9h1RRd4iST04MC0bTSgA8VDJkggIjyXOORZDJ900_7QREd3ittzN2Ar9gEqPk7fDL_MCo523Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: با مشترکان پرمصرف برق برخورد می‌کنیم
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450235" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450234">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
برخی از منابع عراقی از وقوع چند انفجار در اربیل عراق خبر می‌دهند  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450234" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450233">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a8746425.mp4?token=oji8dKmJf5GDE4s-0tSIoeBoiwrlEo0Pu6_irqwH81mA7AyJTdWpHzLjJW9PqMtmrI2jIMOGZVUL8_HsB5VaoYwCoAe3lUAOFmKKSrQ6mL4KqOz9WQy60k8vVT6ymLSzk8RG2NbsznXUXmXG6h3_4_sB3zO0_y7VNakYCipSS7oHKoo0frYUqhL54OsVzn5X7Tk8oXiuARFfXHg8Zeg6ip8QiOeUgoX11ZP6crGvT7U4a76yq-cihZf1hlwWh7JEXhuFur7DrUkGCLo3Uvgnfxvc3L_Cb2SwmgWpg_O3CvEkIEuLyN2wByqz-uCK6dXGCOz191wFci-5JJTu1Bd-sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a8746425.mp4?token=oji8dKmJf5GDE4s-0tSIoeBoiwrlEo0Pu6_irqwH81mA7AyJTdWpHzLjJW9PqMtmrI2jIMOGZVUL8_HsB5VaoYwCoAe3lUAOFmKKSrQ6mL4KqOz9WQy60k8vVT6ymLSzk8RG2NbsznXUXmXG6h3_4_sB3zO0_y7VNakYCipSS7oHKoo0frYUqhL54OsVzn5X7Tk8oXiuARFfXHg8Zeg6ip8QiOeUgoX11ZP6crGvT7U4a76yq-cihZf1hlwWh7JEXhuFur7DrUkGCLo3Uvgnfxvc3L_Cb2SwmgWpg_O3CvEkIEuLyN2wByqz-uCK6dXGCOz191wFci-5JJTu1Bd-sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگ کدام جملۀ آقای شهید هستید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450233" target="_blank">📅 21:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD-YOdoZDl-H4A5t35TVTCYtXDBCz6WLriHTVxyRERqS0TvS2OMEWnn-LyVOpsRG1GAHyuWYdrMssozss_3UJl5CtftqmUs0Dz5a_nh67As1K8NS4q6Ecn4FmHR8j8QzFXJo9MkoLN31OJvP2ZzznEGFTQ79Ukl2dQwf6nB4NTuqEWzOR5LADJuUsfg7UGwmpb0apJ_V_HB7CvPQaWPZmhQ7BoYNvcBRu2DlMbtTSjaEnF1TeKOZcytuUl1h4WpjKCPW1dNfcr8_B5-K9mIHBoh7UkZe3PQzvLAUfe7-m5xG00kSkhGsf4cHIzSDgdDJ3ft-RENpXksIjK_b2RyOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب آرژانتین و انگلیس
⚽️
نیمه‌نهایی جام‌جهانی ۲۰۲۶
⏰
ساعت ۲۲:۳۰
@Sportfars</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/450232" target="_blank">📅 21:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgh4G36xmIrCYxKfJxkcLV4q33hYRYDIwM-XeiVajLjXwA5fuoNUSTW_PuFIDw7RWU7T02nmlhp8W6lkn8U9D1M2ysvXnPof8mXTH4ga_G6R8E2Yb_Y99s7Hhya1U0nrHzR2on2QHh2qEQMoxQfHHlSR2pmz8WO7Hm6U-QEyzJDxUd8T3vhU8bpRYyutuueQjWXyX0VWw2bA-rmsrfdVczzm7V6AKWagkdrMigNtO0PsDuA7YW812EDXVwVu0pZ5fR4tmyZ0JfM1wsahMLcPVP_wwAQW7jx-mc9up7-UDca8L_ASO-QN8vwkKknVuN-JhM-rgp52iTtpE01h1CGwTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی وزارت خارجه: ایران یک جان به‌هم‌پیوسته است
🔹
ایران را نه با خط‌کش جغرافیا می‌توان برید و نه با واژه‌ها می‌توان تکه‌تکه کرد.
🔹
آنان که عامدانه از «جنوب ایران» سخن می‌گویند، درپی آن‌اند که در ذهن مخاطب تصویری از سرزمینی بسازند که به جهات جغرافیایی‌اش معرفی می‌شود.
🔹
ایران، شمال و جنوب و شرق و غرب ندارد؛ ایران، یک پیکر است، یک جانِ به‌هم‌پیوسته. از بلندای کوهستان‌هایش تا ژرفای دریایش، از سواحل آفتاب‌سوخته‌اش تا سکوت باشکوه کویرهایش، هر ذره از این خاک، ایران است.
🔹
این سرزمین، قلبی است به وسعت تاریخ؛ قلبی که هزاران سال است می‌تپد، زخمی می‌شود، می‌خروشد، اما هرگز از تپیدن بازنمی‌ایستد.
🔹
ایرانی همه جای این سرزمین را قلب می‌داند، قلبی در سینه مالامال از مهر به این میهن پرغرور و مقاوم.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450231" target="_blank">📅 21:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‌
🔴
قالیباف: مردم جنوب کشورم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما
🔹
به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید،…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/450230" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450229">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌
🔴
قالیباف: بنده هم در میدان دفاعی و هم در مقابل طراحی دشمن در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450229" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‌
🔴
قالیباف: حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند
🔹
مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/450227" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450226">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
🔴
قالیباف: برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/450226" target="_blank">📅 21:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450225">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
قالیباف: همه می‌دانیم که مسیر دشواری پیش رو داریم. آن‌ها قبلا هم ما را با ناو و حمله هوایی و زمینی و ... تهدید کرده‌اند، نتیجه‌اش را هم دیده‌اند پس نباید از تهدیدهای دشمن ترسید. @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/450225" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450224">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
🔴
قالیباف:  از همه ملت ایران با هر نگاه و سلیقه‌ای می‌خواهم در تبعیت از اوامر رهبر معظم انقلاب وحدت را حفظ کنند، در میدان باشند و این حضور و وحدت را به رخ دشمنان بکشند. @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/450224" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450223">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‌
🔴
قالیباف: مرز بین جنگ یا مذاکره با دشمن، براساس امنیت و منافع ملی مشخص می‌شود و تشخیص استفاده از هرکدام از این ابزارها، متناسب با اقتضای زمان و شرایط، با ولی امر و فرمانده کل قواست
🔹
همه ما وظیفه داریم متناسب با تکلیفی که نایب ولی عصر (عج) معلوم می‌کنند،…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/450223" target="_blank">📅 21:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450222">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‌
🔴
قالیباف: باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم
🔹
جنگ و مذاکره دو روش حفظ منافع ملی است. مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ، بخشی از راهبرد…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450222" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450221">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‌
🔴
قالیباف: آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی تنگۀ هرمز را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450221" target="_blank">📅 21:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450220">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
🔴
قالیباف: امروز امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود. @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/450220" target="_blank">📅 21:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
🔴
قالیباف:  نیروهای مسلح ما مثل همیشه برای مقابله با تهاجم دشمن آزادی عمل کامل دارند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/450219" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‌
🔴
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔹
اگر قرار باشد ایران از تفاهم‌نامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450218" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
🔴
قالیباف: باید همواره آماده نبرد باشیم و در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450217" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450216">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
🔴
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست.  @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/450216" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‌
🔴
قالیباف: باید بدانیم ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم
🔹
هدف جنگ ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450215" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
🔹
ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450214" target="_blank">📅 20:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
قالیباف: باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم
🔹
ما هیچ‌گاه از جنگ استقبال نکرده و نمی‌کنیم اما باید همواره آماده نبرد باشیم و برای حفظ امنیت و منافع  ملی خود تا پای جان بایستیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450213" target="_blank">📅 20:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82172044b9.mp4?token=cWltS9Gur_Pgdel9LDfSfIVujp8SQpJsghWa1COlDIVzsLnYV6rvz7r_EKywWDo3KBCho6EJwYHoFLUSN7IEfb5_Kf5e4B0sBBuNuXXgehtTR3VMf7MxtCHT3WD3QSY7CGwP_44jYzuVotP99fmRORi-T26YJOLPK1dxpWx_wyb7KQPoARmbdRLLs1mBF-hCAe4mMQtAE1Lo_u0tJE_g6y6KbtNlIGq7VZ-bBlT1zT70IEf9t2Y89a6-jRSe_UMyTzfV3lmGA6JVbrBExoSjJMyuS9jZ6rwqGOTZRFBDiUUQLJSpkm-mYGfK7fwp81nHAwb5zwu9K2DpSy0xF8Fljw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82172044b9.mp4?token=cWltS9Gur_Pgdel9LDfSfIVujp8SQpJsghWa1COlDIVzsLnYV6rvz7r_EKywWDo3KBCho6EJwYHoFLUSN7IEfb5_Kf5e4B0sBBuNuXXgehtTR3VMf7MxtCHT3WD3QSY7CGwP_44jYzuVotP99fmRORi-T26YJOLPK1dxpWx_wyb7KQPoARmbdRLLs1mBF-hCAe4mMQtAE1Lo_u0tJE_g6y6KbtNlIGq7VZ-bBlT1zT70IEf9t2Y89a6-jRSe_UMyTzfV3lmGA6JVbrBExoSjJMyuS9jZ6rwqGOTZRFBDiUUQLJSpkm-mYGfK7fwp81nHAwb5zwu9K2DpSy0xF8Fljw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا تاوان تجاوزات اخیر را پس داد
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450212" target="_blank">📅 20:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=Un1xEuPTfbzTgi71mQImKpeyO3A3Jpxc9t66NXjmEbBhGy7XdwvNemgw-aKt9QqC3NjXxWg9_TEmKw3K1gHqfqNiTZUqdgVIheSVsTiZ2LuBgxXrNdnzQsRvD7lYkzEEVC1sSr64jonc_j3Y2o8HCaWuYVeDv7laY79it5BIXJhbA47xs1Rwo_ZS2A9tWxP9vRzGlDac0wYVCQVE2lHtl-vlLnXG-jx3IqxYCtkcWMz05IuLAcLyELA_Eyrm_n5CNJSizmwcOV_X4pPjnAR-Frmwj4otpGT3VQzFEiiIHrP9sEpOlR8dKJ2uaj6IjAx26aXgCi0fQiu2nWY7HmvDPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=Un1xEuPTfbzTgi71mQImKpeyO3A3Jpxc9t66NXjmEbBhGy7XdwvNemgw-aKt9QqC3NjXxWg9_TEmKw3K1gHqfqNiTZUqdgVIheSVsTiZ2LuBgxXrNdnzQsRvD7lYkzEEVC1sSr64jonc_j3Y2o8HCaWuYVeDv7laY79it5BIXJhbA47xs1Rwo_ZS2A9tWxP9vRzGlDac0wYVCQVE2lHtl-vlLnXG-jx3IqxYCtkcWMz05IuLAcLyELA_Eyrm_n5CNJSizmwcOV_X4pPjnAR-Frmwj4otpGT3VQzFEiiIHrP9sEpOlR8dKJ2uaj6IjAx26aXgCi0fQiu2nWY7HmvDPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک ایرانی مقیم خارج از کشور: ایرانیان مقیم خارج جنگ‌طلب نیستند، ما نمی‌خواهیم کشورمان بمب بخورد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450211" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450206">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXxcvfWquXSb-pA8phE6UmIqap2DJufpvok6HDBKEtwQ0_k0w6rvSJdlt_lsnVdgQ1ssfo2zrsnmHL-Eo_nXcg24aaxpCVTzcGhw7wyS7PxnxwNbD3QdiJOsP7reRe76XjpHOCMrGW3mLwj5YWy8X5Neh9Te9CJyGV72ivFrQWNxIJouy9R7LJqJzaWVBx0L5x15XLxBYHA5MTg7DLjO3mPE0bdMI4NKNiV5rzhHnV07YI62PCDNy9aFSCU-Yg-ebk9_FZOLSTDqhOneZJgzuQ5keXOzlrDHLsxqVtu5G46qMtGtYwrbnDjzCtuouy0CpLKS-VV5kVLPDaWol8TFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZBKLQoDg6cLHZHJn4lWZzipBI6CSVXgGfMsfHtUP40rbgrYUAzrKE5YAb3WeinyWaoydMkfcpqxjzIP0DzCZOvl506ZN_DRauYJWC4z9dCr9pvEOyuFFeLWG-9sbIzmVnHrhosCVn1dtYyo1HKXLz5vxRE0BjvI9-n11QstzdW1w3qKhp1iylO678OpqfkynbibloOONVrw5NWqK6y5To4UrO3Zw0J2xJT4nLBkmrtFIuwZvDrLztIsZu6CgbdOOtd2ji9ipz3-3iw0RXh1BFZrwG9iJ7jJE5BDfdlBdVV8DC4PQynoQEWPbg7XYNyehDub5nc94-5_1h497Eb76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edo4VDRzOp5k6YBAEiORk9EMeVWqvfILb1H9rJhHHO1flKZ3XnLeCwgyUIZQlcXDUNgOGdmwhjPrv82gyiyIN6gKaL7u1B1ahisHoN1HPZ4j1BnsXCxQSRr4_YOUVRdeq-EZE9q1Bkw3LSDu792640gCiNAAWzkX7fIZohj1p8JaLOEScVBSbEhTCdxqHPDnFVgDY9KoyB8P6miaZAvsanwGEdRkfj3Xm6WpzjbbdBnjSAuQN03vdeNAYjC4fqxp2CvIyBF522QF-mlWoVs1v4MUAj4-QvuZJmSP_2TkTrKImpEwYe7XNaNFwFWIDEoVGQYBoV9mH7ldDZ6FK4cQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t1kBsYnEUzZK2hkW0-GFOHSmRfo_HvWkKCJis6ylt1PwP7MM2Nkh4zX7qPMMj3Z2peDUtfRtj4ZgjwJslKb7jA19aOyCRUn1RATCq9124mcU-dh1Ve1sf1CwQ15s3WxLseEii2jvn8svcy6PvqsNMePbPaghhTtWVky5vVy_CdLzmBZ1wE-rWoTGmOzSqN4nXbCcs-Hpadl99L8Y5OYGCjHpBydUM0oPDwLe4cbFBKzQm4SRbsB7gUkiyT1pyA0ff42ka7_rxtFKbZz2Vs164FN8SIcczn7y6uUucO17hA_QheVw3eTaZZU_EEONHI35ZG2UbnEzwhAv5j_s5u-17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvxGlYwKObEex528iWhUnXj66c_40VwzfhU4cJmK2brDwvNeS3zCmGKKQhlDUROo-0IMBa7dpjE8HZiAUkTP84AxFPS_Qt0cF_XVtWFjhrUiTuTwlI5GQ3xEKr65L2OPJwr03imWVo-rv6sfHXDJDzKvrIbM7pVbEYZ-wMHqIPIYxTv4NI1XUbapUEOl2tQsDZzk5YC3k5eMQD1KLRrgb4fS-ZR8FUBNRqRJWz13klplPmPSBg1JikuoCUqxVBtXYLGlK-XHu2Q8Yfkp5Z1ZFt1DYHQkGpTJyIsa1MpcVEnOAS81vLGSs-wOd_O4viDFlAjB-r8d6ktUYETAAuBIDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سالروز بازدید تاریخی رهبر شهید انقلاب از پژوهشگاه رویان
🔹
پژوهشگاه رویان به‌مناسبت سالگرد بازدید تاریخی رهبر شهید انقلاب از این پژوهشگاه، امروز مراسم یادبودی برگزار کرد.
عکس:
زینب خدابخشیان
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450206" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450203">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDe0YVCjadVJ3z9arcw-WiiaMx0tDSvVJVVfcubVmSU6Hs3hUzLHQlZLkmDDqe-_8paLBVuE18egGDVth2Pj1i6O_7ArjRVXwkrU0VixHwjrV0ocWH6CejClYMBmBxnUeDC69ZMAR2sFNxJ-Gv26SKuKheck_IhcQR9lRe1QwDQNDLmY3yM6-qzemXGgqmBVAcVWmD-CoPAbO55-EkdD8dorhOytvNZslxYkmTNz08ZaS7VIBrsFx5IM0vQUdQHgY5mvaWRiGICQVMCiEUDZkhJvcEWlu2fxzSqPYKg3nXJgLywsmDd-fXDKEXVXHwrvyX5ni37TzDlkh0WWXkF9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjeDiX-tl0ZMVIWaHMw8tOWn7suhcmEx-zCaGdbK5kRgQAjlXcf4kAridNjGhXL6ZIf_JNahduxBz1A1qt5L6esgK2vc21KVKkGo0VNA13ww8VT49f0WRnQUozE73LC5VYEdp5PQgoxUp1v7xKB82fGSVemZJCOYSnNa8HoOWaKX44YTdbJAmRfvRCk4x_NOuJxZec3x64iG9xq0OCA2lQFIYy_h6Q8FMcu1eziYcc5VDH-bl5kUMJ0_YsWs6KfzUnGI2ao9jNxRIDyaJmiVkHxwAk42lytAoD1R1Nr7jfrWBaMI3o1S6H2IEWi1gyZn1gSPBndwO-4KEX7gGTzftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k00BEcsbFp9H99kweYg6_iwwqV4JhInvN2IQZyaanra5xJa8Mv9__LbhfPa4BxhRBrXaTG9ANO8ZX3JOI01t6eOy6tjLjBtSeyZNacqvdQeuzHoJT3EeOiys0liEKLPdjCKxYhh1_oIXuy7cd4E2PR23jl0tNJ0WtyZE6M0KTuObYt-LT_4T90T9cL0oIiElYeorDY7VNMvCQCubeY4GbU8uP-M5G8PlEEzZvSIIM0NdXc-K7cy3NnK2BDcBj16vtXwTXg1bpPbLmSxso4vzGub51uDwXCQOQyp5LAWbeYL_FjYaWBiFNVPu3kFivkyf_Hp8Ec9qvlM_dlCXQ9dOMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
🔹
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/450203" target="_blank">📅 20:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450202">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e887824b.mp4?token=Y75g2GxfYGKXDImkrYwdOfKR0KJ9zLNDmX1cS0YZmHw75IBJezfcE6MmczqEgmrfYAsHEQ5x77fKJawgFu4OKVcaH9hX0eXYEaSLVUaVj-K2S5DWuFQ2ErcSCHeHcohtprKlf2z6VDVWZf4ep_R1y-7qiZ_mIfAhskgL4WWM9pOY2kI6ODbSanmAp9ZrzaKo6bx-2rz8PDZDMWD48cobPfQjPCATXsDQL--3ZK8SAlvRghWO_Xu4Go4MyH6KKyo2k2lE5OYxHuKc4ymmm671BcsvNnxjU1gQed3FBkB-VDufu6LkE8MubnvKlaKJkls_2GLIYh9hS46LqrwpsunZkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e887824b.mp4?token=Y75g2GxfYGKXDImkrYwdOfKR0KJ9zLNDmX1cS0YZmHw75IBJezfcE6MmczqEgmrfYAsHEQ5x77fKJawgFu4OKVcaH9hX0eXYEaSLVUaVj-K2S5DWuFQ2ErcSCHeHcohtprKlf2z6VDVWZf4ep_R1y-7qiZ_mIfAhskgL4WWM9pOY2kI6ODbSanmAp9ZrzaKo6bx-2rz8PDZDMWD48cobPfQjPCATXsDQL--3ZK8SAlvRghWO_Xu4Go4MyH6KKyo2k2lE5OYxHuKc4ymmm671BcsvNnxjU1gQed3FBkB-VDufu6LkE8MubnvKlaKJkls_2GLIYh9hS46LqrwpsunZkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والیبال ایران حریف اوکراین نشد
🏐
اوکراین ۳ - ۱ ایران
🇮🇷
۲۲| ۲۱ |۳۱ | ۲۵
🇺🇦
۲۵| ۲۵ |۲۹ | ۱۹
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450202" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450201">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj_muH1sl1YADCT7wyiqd8Fh9nkXZRO77yW_X5UOnHKa30ZDPnTAh_7za8Emxc_z9bHYMF-nwSKrceuXj4qWtUfi6D8Y-If9SX4GFPRY0Ab59gl67RzCwUdJX15oMPkLU32TIyN17fDawwlnTOVPs9S7Stb1kOmvspIh8hATPvyulHvhy7-8zjJl-oSvP2WOblTYznQ3e3HBCUWIKP9t_A__h43aMWGdzFIXPIpPedYVi-GL2cnWcZfUyWW2k6uk-JpFLl3DoSMGxo6KnPeFvwnLvDTIc2gPjP_vbiV5Ilpt0kSRY9oJzGMp4TOGJAADxn2aUvHowPgBzTUmUVKjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بمب نقل‌وانتقالاتی منفجر نمی‌شود
🔹
پس از فسخ قرارداد یاسر آسانی با استقلال شایعاتی درباره احتمال پیوستن این بازیکن به پرسپولیس مطرح شده است.
🔹
بااین‌حال یکی از مسئولان باشگاه پرسپولیس امروز در گفت‌وگو با فارس گفت سرخ‌پوشان هیچ مذاکره‌ای با آسانی نداشته‌اند و اخبار مطرح‌شده درحد شایعه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450201" target="_blank">📅 20:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450200">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67045d3b3.mp4?token=hijq1cQO3ORyrRY4n_QHniwboaiG2MUrozYb6PUSkcxaTTe5NpnJ1l3yEM679p2mNcAbtkQpU4lMrOOBKhwg3zCDn5tHib6cbKu_ZvHVh61pcw-5pQhlor-_Pa4T9k3fLGk3h0gsYO7UnCXQ8fcAElh_c4FS26L5QWzeA8HVByzcwIfgFxSROQhBQB7N-3ibGO5zLZnoKfZ6SlrKExv8lvyBU2V3NLyexRYG6nvomwXMGz-0KXvP8WMWzBlTXEtWdjARXGcwUPruhmLmcwm3YxZFn8EMvaLGKGVmYzAOECUXrt42laXwm5hLKJRl1lD7XB00QadKXG32bd0jm0W-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67045d3b3.mp4?token=hijq1cQO3ORyrRY4n_QHniwboaiG2MUrozYb6PUSkcxaTTe5NpnJ1l3yEM679p2mNcAbtkQpU4lMrOOBKhwg3zCDn5tHib6cbKu_ZvHVh61pcw-5pQhlor-_Pa4T9k3fLGk3h0gsYO7UnCXQ8fcAElh_c4FS26L5QWzeA8HVByzcwIfgFxSROQhBQB7N-3ibGO5zLZnoKfZ6SlrKExv8lvyBU2V3NLyexRYG6nvomwXMGz-0KXvP8WMWzBlTXEtWdjARXGcwUPruhmLmcwm3YxZFn8EMvaLGKGVmYzAOECUXrt42laXwm5hLKJRl1lD7XB00QadKXG32bd0jm0W-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اخاذی با عکس پروفایل در همدان و لرستان!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450200" target="_blank">📅 20:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450199">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شاهکار دولت لبنان در کسب مجوز برای ورود به روستای غیراشغالی!
🔹
دولت لبنان پس‌از چندین دور مذاکرات مستقیم با اسرائیل اعلام کرد که  بر سر ورود ارتش لبنان به ۲ روستای زوطر غربی و فرون با صهیونیست‌ها به توافق رسیده.
🔹
این درحالی است ‌که یکی از این روستاها یعنی…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450199" target="_blank">📅 19:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450198">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3eDG5cDalsdZEkxCo9sFhYyweWuUfEOAxL6USEYSZX7m8ljHdFcdCA0f-nVKpuOD9qtl0mwnSbqB25TS6C9BWSOVtRiUfHJRtbVoxP3VFsnj4Agn18HoBWersnZroMH8nS4vXT8lqZxJzrPHW9RPD52Bwi9fJZTK7sID0bTYE2cwQPjb4qV41HKVMaC_Rz5_bLKBk8NdnzkS9HlD8k3AboaVLwSJb6rphdutY5kYSCaWQD40wbLOMw9ny8JEm3igEUYXp_IP0lUUapP1aJcn4T8xZRvw6sEZc7RCiCW_lTcYIwAoCb5zxJnOxf5_yGx4FgGk6TLqjAhblEYzv5btA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار
نفت در آستانه تهی‌شدن با بسته شدن مجدد هرمز
🔹
درحالی‌که در جنگ ۴۰ روزه، آزادسازی ۴۰۰ میلیون بشکه ذخایر استراتژیک مانع از بروز فاجعه اقتصادی شد، با بسته شدن مجدد تنگۀ هرمز، این ذخایر در شرف پایان است و  فایننشال تایمز هشدار داد که بازار جهانی در آستانه تهی شدن از نفت قرار گرفته است.
🔹
یک تاجر بین‌المللی به فایننشال تایمز گفت: «همۀ ضربه‌گیرهایی که داشتیم را مصرف کردیم. همه‌چیز تمام شده است.»
🔹
حالا تجار نفت می‌گویند که اگر بسته‌شدن مجدد تنگه هرمز ماه‌ها ادامه یابد، مشخص نیست این‌بار نفت از کجا تأمین خواهد شد؟
🔗
پاسخ را از
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450198" target="_blank">📅 19:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450197">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
برخی از منابع عراقی از وقوع چند انفجار در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450197" target="_blank">📅 19:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
منابع عربی: دقایقی پیش ۲ انفجار، پایگاه آمریکا در کویت را به لرزه درآورد.  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450196" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450195">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcC8YIVVDeZBoddJ22ZomwL_c23ir9Se_9ag-GI6kFicuD3_8abLvP7cPij74iWp8X3rBppDwPj8uS-BvYMDqjuH8ZaF_X2a3eRpVAWwDdusKfKZt3UOEtbkORgbeZJZqz4OFQyrNUQ95jpJECbMEtk4u7cXk9ovssl5gGi8EzeNiKQ-Z16S3U2eWzSVylXXOzPnQidJM9yfppFwumYvX9YlHTh-EOas_e8HI4TeYCetS0iZXuhbp8iwEO6CASzVdlmLKkF8bjPvo7-QizFNR0a_ruGlBcyPYiTE19w9r-Rxu84-nx-2YqRTODFE2YswghnsB2Ob4C3Ikqa9f6mnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
لحظۀ بمباران فرودگاه صنعا توسط جنگنده‌های سعودی  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450195" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450194">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
منابع عربی: دقایقی پیش ۲ انفجار، پایگاه آمریکا در کویت را به لرزه درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450194" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450193">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otxci66Hx3aFRHHrmVYEX30l3BG2nSCQxwsk7rQajrca0oQpNlUd4JtN0KDL47uSxA8oVdERdtdBa9I8bkfv7o7jr7LFgbEEnWITKLo0wM17Mt71p6hNmEBKiNWmVpUmwAySyiQm2kqJk7lXXtOOXME77bJdUZyELuDQeGKD1bs4Xz7ytiLcnsv1RIm-nb6sDLgd-5TFTYHUlFoPeUdwlIlud-4FS6eN5AX314B0Vrp7zTNBqjY3VcedkXdMlrKqpeLn1jIsBPnOgTvE0ng82h-ZwudvpYsgWGsJNuIxaaH0B1tVBrnj0V9Si1B2cOhikFcILumxW-WPZj21Q3kClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقایی: نیروهای مسلح ما نشان داده‌اند هرگونه تعرض به خاک ایران، قطعاً با پاسخ متقابل مواجه خواهد شد
🔹
سخنگوی وزارت خارجه: تعهد در برابر تعهد به این معناست که ما تعهدات خود را تا زمانی اجرایی می‌دانیم که طرف مقابل به آنها پایبند باشد؛ در صورت نقض از سوی طرف مقابل، ما نیز متقابلاً هرجا که لازم بوده از اجرای تعهدات خود خودداری کرده‌ایم.
🔹
بقایی درخصوص ادامۀ روند مذاکرات گفت: فعلا روی دفاع متمرکزیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/450193" target="_blank">📅 19:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450192">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iySYdbPOuxRLfbknDSasYmF7bd7OObjO5n6Vvwpy-ahk_-P2tsYGATla-HvSqZIsqDz1tPNOG4F9Zxdz1STEZW0ntn8QTDj5WiIdTMLwAb0cpOvdtZXUc0aapcV2Q1cUQc2TrpoYU9ofDb-sZYZdzCdjWxs9ASH-6oi75ifskwkT1h7C31K-oGW1fjpo9FpdT3Zdzxp5QTapCX8uF1RGvFhj1vssLa8jBlVx0KD909RZItxuspra9mgWTFb7ScozCxwI6u3APk7H5-1dk2X7cAE40s1HtybcVq0Q-rnA3X3qP28Csg6XcKOEC8RKtGF1aqlfUkMGg8lU-L-D4WbLCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسایشگاه و محل اسکان یکی از پادگان‌های نیروی زمینی ارتش در بمپور</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450192" target="_blank">📅 19:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450191">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/focONh-tuF48Bd-1-7C0B1ysfha9nA56ut36WJO7xeaWTU1gXe28by11AYjXgMhV2NBrSBb2w97P2gQwpr5XI3GM3p0Sx6K0jJ3lOWGQpSVU6Vs1wM0LFacWbNldG7hXB13pWibccNKxoAqnCdIJkM_pXQ5Va1ErKcOCxN_gZpdaLNbP4SHFllwoI3UqHoVcpEJMz-luBGr44uvvcQ61OfrjNeAd5i2vOxzMl3nmdlGP76-CGR024O5GH1ln7HhOpwAHtYxj1FrG2RrJ_HVCScuXC71EK4zncz4PrRd5ostbZVEVILTUkRLxTCQhAxqEq4o1AYOk1azW-m0fWHoX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۱۶ دستگاه استخراج غیرمجاز رمزارز در هرمزگان
🔹
در دو عملیات مشترک پلیس امنیت اقتصادی، دستگاه قضایی و شرکت توزیع برق در بستک و قشم، ۱۱۶ دستگاه استخراج غیرمجاز رمزارز کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/450191" target="_blank">📅 19:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450190">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a04aff34e3.mp4?token=RmErsVa8CUAzznxv8jTo5dKx0X4kZ_Sl3RqCZAeobkWcD89e55I6-KB98IrUsh0iQRv7mUMBBpBHr1VM0dVkI_9irpR_R-_dVwfUarCTKSXt7hPAi9toUIwcXvSo8jfPuQMDI4CBwgFwpMRkqQL4jOR8OW_Oe2DKvJje0U5eHn2waLGa5OQU9-ksDImbYF19ZYoXbuhnBlL6RMTeEM7fcGB9njroaZMTrZyGsvdMAWAkIdjeHOAMjH7MnVWT40c5f2FFEkAW0PSpHVuC4z2ksfQ3gzPU0YUYiRIld_jtT1DPVIb1BWdPh8dKlfefXZqtnsulFcqoQg7j8dfssR3Jhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a04aff34e3.mp4?token=RmErsVa8CUAzznxv8jTo5dKx0X4kZ_Sl3RqCZAeobkWcD89e55I6-KB98IrUsh0iQRv7mUMBBpBHr1VM0dVkI_9irpR_R-_dVwfUarCTKSXt7hPAi9toUIwcXvSo8jfPuQMDI4CBwgFwpMRkqQL4jOR8OW_Oe2DKvJje0U5eHn2waLGa5OQU9-ksDImbYF19ZYoXbuhnBlL6RMTeEM7fcGB9njroaZMTrZyGsvdMAWAkIdjeHOAMjH7MnVWT40c5f2FFEkAW0PSpHVuC4z2ksfQ3gzPU0YUYiRIld_jtT1DPVIb1BWdPh8dKlfefXZqtnsulFcqoQg7j8dfssR3Jhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوک تنگۀ هرمز این‌بار سریع‌تر عمل کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450190" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450189">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9bce1e6.mp4?token=d5fg_b8WO6d-pcImt1PomYB0jrLNZMps5IR8AyMwRmp0885CvYG8IEEftkoxLOgqKo_dgKk8EVeH80tFX06S1g5CEhv-f7Tm2Z0pvuHhP12YE21v2fQwRB0jHCTebCzpRf9qjYqoUH4GmKXhhNOlv3ih95kxd4nCopRJBqxeYFZNus1R7kHX4mjQO2yE9esIZjDt0rAQTn0QbDqnE850bdPfd9DmCB5RIxF5ErLv9TpCe66JiAHFWhYdYjt4U7FJz8x1U1s1e39g4yLMKHBpnnaKTR-bvCr_e2iw9ksRCB1fePLCy9djgoCE13CwP9pI24Hk5GshAAjoSbpOXaVtPRm9hUllcqRCb8pLo6KmX2ZnMpJ9eNHPbLQjJOS88TdwufNkmq6Uxs-YYAsXuTUk3KW_GCV7-KAej4lY5lQgRPVycLIB80Wr1QfNMUanIDAzAh2Xn-6CK_vWpsydiulIu5921WTwlOY-n0SEWg8DdKOLK5pbBMQc5PMXktiO4a_anWKMjvmjytc1N2QK3cIQznH6ZcZf10mH4Cm5DavYoAQ3BlgU37hHFxbHJpOzkbs_49w9HrGYCUlWUF6t4m71KgdeD2MQd5olZXhSjrqWr-zOKm6Soql5PQaJLVWemOHITgu5RldHhpo235bvo9_yS_OSYSowVjHF_z_5ylvRQ_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9bce1e6.mp4?token=d5fg_b8WO6d-pcImt1PomYB0jrLNZMps5IR8AyMwRmp0885CvYG8IEEftkoxLOgqKo_dgKk8EVeH80tFX06S1g5CEhv-f7Tm2Z0pvuHhP12YE21v2fQwRB0jHCTebCzpRf9qjYqoUH4GmKXhhNOlv3ih95kxd4nCopRJBqxeYFZNus1R7kHX4mjQO2yE9esIZjDt0rAQTn0QbDqnE850bdPfd9DmCB5RIxF5ErLv9TpCe66JiAHFWhYdYjt4U7FJz8x1U1s1e39g4yLMKHBpnnaKTR-bvCr_e2iw9ksRCB1fePLCy9djgoCE13CwP9pI24Hk5GshAAjoSbpOXaVtPRm9hUllcqRCb8pLo6KmX2ZnMpJ9eNHPbLQjJOS88TdwufNkmq6Uxs-YYAsXuTUk3KW_GCV7-KAej4lY5lQgRPVycLIB80Wr1QfNMUanIDAzAh2Xn-6CK_vWpsydiulIu5921WTwlOY-n0SEWg8DdKOLK5pbBMQc5PMXktiO4a_anWKMjvmjytc1N2QK3cIQznH6ZcZf10mH4Cm5DavYoAQ3BlgU37hHFxbHJpOzkbs_49w9HrGYCUlWUF6t4m71KgdeD2MQd5olZXhSjrqWr-zOKm6Soql5PQaJLVWemOHITgu5RldHhpo235bvo9_yS_OSYSowVjHF_z_5ylvRQ_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیین بزرگداشت شهادت شهید صادق دروگر در رودان هرمزگان برگزار شد
🔸
شهید دروگر، بازیکن فوتبال هرمزگان، که در حملهٔ اخیر آمریکا و اسرائیل به شهادت رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450189" target="_blank">📅 19:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450188">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
تحریم مجدد ایران توسط آمریکا
🔹
وزارت خزانه‌داری آمریکا  از اعمال تحریم‌های جدید علیه یک فرد و یک نهاد ایرانی دیگر خبر داد.
🔹
افراد و نهادهایی از روسیه، ایتالیا و نیجریه نیز در این فهرست قرار گرفتند.
🔹
این تحریم به بهانه ممانعت از گسترش سلاح‌های هسته‌ای و مبارزه با تروریسم وضع شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450188" target="_blank">📅 19:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450187">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280a9857f2.mp4?token=YJIzvBUfDwv5HLYoCVAC43yTZ2Zd6w5mwYFkZ-EqWGROHyZrR0Q0DnxrlfV8ZJWIms2tKceBWHOAUz4fPxx6P1wHF7hUZ_iUVpzJDC-MNr8XclcCVZARin5dfDcgtLUN_V3dAZbpNJxAFXqUkFCzrMDtFyQiO3IZMdH0rBQefhKe5h-cVOz6Yd7L5fixJvSiUQaSSqlBIjqK6vaoOMWWH8pbU7PVpZ-esixLLaaRCOvrJ4Lvn6kiE0V6jvmqLCQK67b-ccFDXX5xMHj9zG-8pXI7O45fNuqTCXkl9KMWlFj-BO-lzCcUFKYKsIfjKzC1H3fKJSO4ZDLahpBBDYpt_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280a9857f2.mp4?token=YJIzvBUfDwv5HLYoCVAC43yTZ2Zd6w5mwYFkZ-EqWGROHyZrR0Q0DnxrlfV8ZJWIms2tKceBWHOAUz4fPxx6P1wHF7hUZ_iUVpzJDC-MNr8XclcCVZARin5dfDcgtLUN_V3dAZbpNJxAFXqUkFCzrMDtFyQiO3IZMdH0rBQefhKe5h-cVOz6Yd7L5fixJvSiUQaSSqlBIjqK6vaoOMWWH8pbU7PVpZ-esixLLaaRCOvrJ4Lvn6kiE0V6jvmqLCQK67b-ccFDXX5xMHj9zG-8pXI7O45fNuqTCXkl9KMWlFj-BO-lzCcUFKYKsIfjKzC1H3fKJSO4ZDLahpBBDYpt_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرویس عجیب والیبالیست جوان تیم ملی در دیدار با اوکراین
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450187" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450186">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وزارت خارجه یمن: اقدام انگلیس علیه سپاه پاسداران محکوم است
🔹
غربی‌ها خواهان کشورهای ضعیفی هستند که صرفاً ابزارهایی برای اجرای دستور کار شیطانی آن‌ها در منطقه باشند.
🔹
از سپاه پاسداران در دفاع از حاکمیت ایران و به شکست کشاندن توطئه‌های دشمنان قدردانی می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450186" target="_blank">📅 19:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حملۀ دشمن آمریکایی به جزیرۀ هنگام
🔹
ساعت ۱۸ امروز نقطه‌ای در جزیرۀ هنگام هدف حملۀ دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/450184" target="_blank">📅 18:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450177">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GDSh1OySHh2lJtJC1K5pkKAOdpEykPwkbuPYvBKFsSMaqrCPHfarNOzeULNQyNGD4mLbEnN_aW9_HDZTgf_3L1WCFKUbH-iLZ9c1eeCTsHe7cPPC0avnkxMxhNexVF02kbzNlZvpllXCGglyyl8-TX7n5arnX0RaxIaM3e7-617h4RlA2vgTbU6kpRxFAMXAkyHC33tkzNSUocvTvHybmIwradYsTLHZBBT28dilSGgPKqtiUNAH4KXAXmHKI9MBgxcZxfCwcV2ApV92Ifj7aRQm8Qo9uCIwv3wVzKeabjl-Fithzgp2yrN7I1Vfr3NzAHDSF6Crlxc7AJaYbIXDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBRzUCRRxCAXD3Bj11cmKj8bTVAoYHwxSBQhWwwdxbFz4P-JhqqxHtdw0DIpnKDbKYyj-fPDRDSYc2ejq3WoRNKH3gPoYJSC81ht1jk3YB4MsaOOAKo9iPHHphk4jpns8xH8dZYzrJDrazh6vs26UGn-uBTe4fgs1Jpmp5d8a-4mhfRC4SKQKT0NFx3CgBnhhkDa5ihXUIfzF2bKXV7UfeQOvF6FdfEQhlas9e08bw7sFfFPGgG_jpmzdvqKixV4Mohb-vBPSiLxsZ9VItTH8EjgkBoRtLmyZFcI-9XnZ95zAexa2DQFDf1qmKAPutGeT6QJh-XnwFAbiuUC_KSsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gunWHJSGoRLjTGpNJaGHNOurur0puvYw8xVO8798AOVLDX4BlZBm1DJKF37sRLXYN1Rln16usVgqad0EHqrpJ9p4uoqHRdQnaZkCLfAuWdYVlsNxzt51IciVH5LdjmQSjbmFWZm6k_IfGFjroEHXL2usOdHE20ITuifyFtS7W2gF9nKXjadJQqAizbVqCCLv_sRMtbAxgA2T-F0LpOKw0pjxvM8Qtc2Q1XDja-DciURdI7gAGcMJnw6rjpYH3ujf0raNkdZHg2jD6Ohw-dlXt1yd-M4z7YoZK7mlov9hdufiqzEm_F-hYA9ELL8U7UNlT_YdT6i18EthvNNl7jDwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwtHPffmkWoeuUPOvfjuiZL3MRrRx2rhJU1HR-cyNG60qEGYYG1dZCSgP7lJvcFmX2KuRKgkBW23etQcrFfRcWru3ixctqRL2SbxW-8s89TV-Hz11r2Qh__hgX33VZvfjpZlX0fL7KA4Cdwg1KG5QzbqEgHxASdV8-g3NSArwBekH7l5iL6XhL8K7Qh2X2mgfDud0-mQr6UTf73YhQFVf5hbrMbIXQ_GeEhCiylBhqwiD6fkOEiwwzjBq79hYsjcvZtcjYmbW2COo93e_ZLbRT-69eh6z8xp7Ec2YdCRjXvVSxI-lmshdRE-cKo49ylM357T8FKk7B98n6IqLH2MMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnHx8O9Cmm2bMVxhH438pR-AeGTAAdq0SAvPDsU19nhR8-EMLZHmKwHEoT0hEaOUzWLbhA7vgr36QX4fdNhiBr3G5rYBsPEq5PLAwtxxcm8Vis2Qy9kuPr-7n80647gWwl8R9s_jJ1uitMC__ciM955cFqpqUNNPmBbWSnAMx1uS4OFeOGY3Ct7Mq7sO6uKEbXfXK8sySnZ_TrpLagLlWIw-6_1N8tZOOsJwH7Y5FM7o8A3ANk2I9Pfl9YK_uARds-VZVKP-WwQLjb2k7gQSXfGAwP9zl3D2UBRDSKfQ29FhtWhsTIcsR1M4ny49jRZiUc5boKHTug-K-pHxSp7UBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVnHCzxnTR7RoueIMCfDNBUGv-HlaPOcf5Y69ZjSj1mdSjofbOb8nkVbRlKfLOpbxazgbV7QDsAobtlFfrynxv_uS0VPCSjTxdlDKAjB6sHuSHWpJMpt760Oy0V1D6zww3AYirvm9w-zzqvZw_thmoZNKaL8IVRfJ4JMzDi-7NwnuBjo9rPwVrJ0i9eEIE1cmeHtXE-ccHVlYuh5QLchxsM-YRgcpzPnnzNpR_Lj7XFp1OU-gMp1eGJH44daQeU6fxpkQCGurHOIxsLFsjEigtf4pcUsrFbtN19EeDflLEdq3UgLtb64SbnLPp7BRRq7Ax6RT1RYQyOPvUM_ZVHsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AinRZid6fB3ya1ggtJoBPq2OiV5dlrlEv6AIxRftCflTtqwTiZJdBvxdzS-ChMbgFgyPtqBGwNmO8COs5FQP7V7ESM1WQH7DXNE0wlnDhSScdqvAMOCoyah5kHomNjx5ZqhTEKJjNmy__4F7ZX7AsSWm8vVzr1dAPMZK0qlKezNQ__GAoQ_6F3Da3Z80WC6Smcl_arCfsyQBXaXwcjAZmU6qwJUFf1OfST8SPErO_Mh-zsh2UuK0kOi9ER8xQtH2QmbfVdnN85nCzY975ycKmTvOIFFFQWZTzMiTsb900C6my7zE6P05IesrE_Bal_I9JITR37dVS-njnpZAT56VCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خاکسپاری مادر داریوش فرضیایی
عکس:
الهه آسیابی
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450177" target="_blank">📅 18:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450176">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVFqcAL45hXXxRIKLsrzVnfgkK30wmv3wWjHsIZebZThP151P1dv5DIEUC4jyzBDLTGkjSsoUxE_dJgMAou8fADHMJvkotq7SRaoFt3_tjJT-MNeUim1Psx6JLEQIQBd229n_NJdhfbkd2gsOWT81rhYoqHHfMzJq7CLvZh62miJkX-9e4ZP-h9hQmIITjI4sJFRXF0n76n52bSJtVTlmAElg8UKKYgImui5neWs4KJ6R5y5BNY1z6uYgr6kQU55L1-dQZwS8zwvZH5vQIjSskgReIqrjiGJShztolJzWrNqnhEdB4grnGgF14KPLIVcvW1aOyD-BIDHy5V3nkrhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
توصیۀ پزشکی برای این روزها: از ساعت ۱۱ تا ۱۷ از خانه بیرون نروید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/450176" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMqIiOX3t2B5qwhj4EGe2MXWbMLvsTenZr2B8pOdFs7An8c1WdXQrLxFsdX186SKYQ_0C7M0q9K3ukOMpBUHGYfkhFd4BYi-gbg_qrTRxS4pQ3IcK4kmC0LHWM8ZGv7Hkeqsv5CfafVBUNDDcdloz_tM5qZGDpTVRszaozcjHmEsSRujpZ6S7DV2vQ7tDKOobhNPqqL_6r_S3JV0QMvbqpHcm4g9Zev1D6d_8baiFyIk1-JExIO-_KlOhS_pRT9_S596WC4BogA-GNIQbVfp6jyKL62h3GS4z8U9HLXEcZGHrnCyNmXcvGh1z0jZL9eVQtMp0UJhyA0bLwj7XVEsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلیلی: خون‌خواهی امروز ملت ایران یک مطالبه جهانی است
🔹
خون‌خواهی‌ که امروز ملت ایران آن را فریاد می‌زند، صرفاً یک مطالبه ملی نیست، بلکه مسئله‌ای جهانی است.
🔹
این مطالبه، دفاع از حق همه ملت‌ها در برابر کسانی است که به خود اجازه می‌دهند با نهایت گستاخی، حاکمیت ملت‌ها و عزیزان آن‌ها را هدف قرار دهند و به آن‌ها جسارت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450175" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450174">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64bc46239.mp4?token=ss4JIGNAuKL8hbCljSGklZQDbe6Z39wHN2wrCpvKX8DucF-hkAlmoYMSMn1SS8JNsQZrvftt1PUxr99RfkNxqJ2gZPuIKx2HK8HmSUby6nFIbv52OjFLQ0Bc4AJ7j_Fz2MKrEda0eDleO21Y8pKVgR3Jcf8LrQtX7O9qCSgqxKo_HYJuEzhldc6ILEWhKvpcE03Vgq76vSCZU0f1Da-cJ9nSJ58etUlykPsTK_jocKwEt8X_VCeR7sjjkzmuPmZApp1ql8ZkVyA6JIDBqZ4Kn2-qdrkYOc9-LueloXl2xs_p9b-drZOiR3dyhFes6epWB8LdiTpRFnHzzyj0_6oqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64bc46239.mp4?token=ss4JIGNAuKL8hbCljSGklZQDbe6Z39wHN2wrCpvKX8DucF-hkAlmoYMSMn1SS8JNsQZrvftt1PUxr99RfkNxqJ2gZPuIKx2HK8HmSUby6nFIbv52OjFLQ0Bc4AJ7j_Fz2MKrEda0eDleO21Y8pKVgR3Jcf8LrQtX7O9qCSgqxKo_HYJuEzhldc6ILEWhKvpcE03Vgq76vSCZU0f1Da-cJ9nSJ58etUlykPsTK_jocKwEt8X_VCeR7sjjkzmuPmZApp1ql8ZkVyA6JIDBqZ4Kn2-qdrkYOc9-LueloXl2xs_p9b-drZOiR3dyhFes6epWB8LdiTpRFnHzzyj0_6oqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: شاید تصاویر حملهٔ آمریکا به مدرسهٔ میناب با هوش مصنوعی تولید شده باشد!
🔹
فکر نمی‌کنم کسی بتواند با قطعیت بگوید که آنجا چه اتفاقی افتاده است. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/450174" target="_blank">📅 18:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450173">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsTH3Vim7RG8U0E3IJmxhjk9itBgsI2eRfcB1j-IVXwVgfFsXEpPDsy2-3nVNLRt6Ym4GRmwCpP1Qh_Q08zKj28S3ulfC6BO5oUJt1_RSDsF9iXUC44GVT5eTRq2VZk3_rhTMkRN-O0fqep_QVbAuTWmIZiTe6obkECaEbenUngtPNmnwBC2RvANw2xP-LCCcI81dLO3jGfx79kln-tlFRuJuFbG-GFER_v_40HiDpNQQcO1yMjC5NJ_ukzmJttGr6jaa1dVFc_6HfyvRQqcgawqnhk7xf7J-SfvqHpVMkXvLYZhNOYhqARLe94gPoJuf6YQQFSBBy3f1-WQaxe_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار دولت لبنان در کسب مجوز برای ورود به روستای غیراشغالی!
🔹
دولت لبنان پس‌از چندین دور مذاکرات مستقیم با اسرائیل اعلام کرد که  بر سر ورود ارتش لبنان به ۲ روستای زوطر غربی و فرون با صهیونیست‌ها به توافق رسیده.
🔹
این درحالی است ‌که یکی از این روستاها یعنی فرون اساسا تحت اشغال قرار ندارد!
🔸
ارتش اشغالگر طی مدت مذاکرات مستقیم با دولت لبنان همچنان در حال تخریب منازل مسکونی مردم لبنان در مناطق اشغالی جنوب است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/450173" target="_blank">📅 18:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450172">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkLdJOit-L_jEBIsqz5Jr3jk5q68CPagi5BvAfKgpZ_Ki2w3Fi6nDsMovhcut4qFYN01eNVR2kMpn-JDj3Muak160gWKc4rumLmYotM2uvQanhPYa0X8ma5D34Ji61zfL-EtCqj4Tb0rQUcevTwQOs7d0WEHd8nVl_cLWDk6ELP1tP4siGNyVeifT4elZO-FypSe42FzjXeseRHuoz8D1VsdtDvIoCOZv5y2ecmqsgkCmbE0KuXmd4_TfDhXf2_WyNMBL2VnepvHLdQn-GkpkGIl3YTeNGYTXV6T8XS7FmvEg-FFfWy4M9xCPg_iBy7fjR1NtDzs-MBxQDEqDiPoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصباحی‌مقدم: خون‌خواهی امام شهید حق ملت ایران است
🔹
مطابق قرآن، کسی که مظلومانه به شهادت می‌رسد، خداوند برای ولی او حق قصاص قرار داده است؛ این یک حق الهی و کاملاً طبیعی است و البته چون ایشان ولی جامعه بوده‌اند، خون‌خواه ایشان ملت ایران است.
🔹
این مسئله باید هم از نظر حقوقی و هم از نظر حقیقی دنبال شود و نباید چنین افراد خون‌آشامی به‌راحتی زندگی خود را به پایان برسانند.
عکس: مرضیه سلیمانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450172" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450170">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETHzo9R2dRJYj13-ibS4sENEZgnTNiZnFyVF5puxmETZv9ttTI4urPEmsD4nxj8w2n13JglwMWDdCaKxO3f3kyfjL-wUAOqB_iiaXMJw8rGSKUtYJn6S-PRl4rYDFJE33CvpddFVIBN2ReDLPrCPBEtFWKNbY-7m2QDXhxfTER633f557Q5GynP2WjCMLAlHWRcY4qgjxchtNSTZFaft86Ic0IELV22JU3-2zdPlLDl8uS5xUL40iBMt81BP6DwEQpAA4Cfn6kllWOorkB7yli7KlX_-YhuYp5DjLqFYB9frvFVMAinRz6FQ0XaetDZzO20GAAos6yhSe4hZCBU5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنرمندان کنار ایران ایستادند
🔹
با ادامه حملات آمریکا به مناطق جنوبی ایران در روزهای اخیر، موج تازه‌ای از واکنش‌های هنرمندان در فضای مجازی شکل گرفت؛ واکنش‌هایی که عمدتاً با محوریت همدردی با مردم جنوب، تأکید بر وحدت ملی و محکومیت رنجی که بر مردم این مناطق تحمیل شده، منتشر شد.
🔹
واکنش هنرمندان را
اینجا
ببینید.
@Farsnart</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450170" target="_blank">📅 18:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb2295736.mp4?token=RyJUqF2W3vedy76h-iltnu5R0TC2BPrhAbZdpxn8vayOPtbWweMzgx8pIVMqJ0yfzwZSPvijSIbY6i4YHuW8zXbRYroYh2euRRZF0aOdotWnU77J_tTeC9kSkdDqAW9PW9CDYUs1oUv8VX4Bu1szMpfHKU3ZmYYuxxrgaWGkQ9VyOz4htLXMPrZtykQ-kg8UNDGfKLu3RdqE98TsoeEvxy-A-InN5gC0p-W5hF7_40yqRSmHQY3g1QxJ9CdeGxXWc3IeD8dCUwQEk5qD-bS6Ls0K11A3VDgDiX3QtHXbXD2X6flss4St8RKEI8iyGqu2bK5zc98jmo1iDKiXeBTBIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb2295736.mp4?token=RyJUqF2W3vedy76h-iltnu5R0TC2BPrhAbZdpxn8vayOPtbWweMzgx8pIVMqJ0yfzwZSPvijSIbY6i4YHuW8zXbRYroYh2euRRZF0aOdotWnU77J_tTeC9kSkdDqAW9PW9CDYUs1oUv8VX4Bu1szMpfHKU3ZmYYuxxrgaWGkQ9VyOz4htLXMPrZtykQ-kg8UNDGfKLu3RdqE98TsoeEvxy-A-InN5gC0p-W5hF7_40yqRSmHQY3g1QxJ9CdeGxXWc3IeD8dCUwQEk5qD-bS6Ls0K11A3VDgDiX3QtHXbXD2X6flss4St8RKEI8iyGqu2bK5zc98jmo1iDKiXeBTBIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: شاید تصاویر حملهٔ آمریکا به مدرسهٔ میناب با هوش مصنوعی تولید شده باشد!
🔹
فکر نمی‌کنم کسی بتواند با قطعیت بگوید که آنجا چه اتفاقی افتاده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450168" target="_blank">📅 17:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd12106af.mp4?token=NTedZOU1-KeYMMJ24X8OzFyEJ4PMuT8OQWzWGNXdKY2UozP-h8Xxc3VPBclQVPvxpIKJzMWB_6FvHsSp76tzkzn_kJAzpDLV5RqV_mon_klRm7GerAmgh1CwqLqu9rJWQd6rOUVekIZWdyjggNHw8W-8dnvs37ixgsKLZHJfbANTTPAncmobsmVYSF6l-HiPiaxpqzOvL74Rb5eiZUYamUPPd3mDx0i_DVGHKp59SaJXyMSP7yTPw5gfuI6qf1uuntDvzr5h85O3McpBxLbwSAJVYUU08Fp2oxGUDfVjXSFJ3ivG428hjo7d8eF_KC9IMv78OTPbonEYM9K6b3fEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd12106af.mp4?token=NTedZOU1-KeYMMJ24X8OzFyEJ4PMuT8OQWzWGNXdKY2UozP-h8Xxc3VPBclQVPvxpIKJzMWB_6FvHsSp76tzkzn_kJAzpDLV5RqV_mon_klRm7GerAmgh1CwqLqu9rJWQd6rOUVekIZWdyjggNHw8W-8dnvs37ixgsKLZHJfbANTTPAncmobsmVYSF6l-HiPiaxpqzOvL74Rb5eiZUYamUPPd3mDx0i_DVGHKp59SaJXyMSP7yTPw5gfuI6qf1uuntDvzr5h85O3McpBxLbwSAJVYUU08Fp2oxGUDfVjXSFJ3ivG428hjo7d8eF_KC9IMv78OTPbonEYM9K6b3fEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیطان از شجاعان سخت در وحشت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450167" target="_blank">📅 17:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زلزله گرگان را لرزاند
🔹
دقایقی پیش زمین‌لرزه‌ای به بزرگی  ۳.۹ ریشتر با مرکزیت انبارالوم آق‌قلا، گرگان را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/450166" target="_blank">📅 17:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU47fdffGQ-e6BTKMpn4BqhPyPmGvSY_TexfD0JHSAspdsAfBZ157nwQse9Zf-Mbum59VZhgvvQol-F6xe28RVbsPPyKstFKr0SAGNhFnDiYk4T0fF-OoFGQBhNa8Q-rW_pIuR8sakVAqVqSKwjVY6PLEUu4CrAj8tanS02UJNwWyJaYt2iSydJpSXNyM6QXu-E28szQeTZhQI-TCZogbLfqPy_vCm--xEAlKQLS8vtaWrXgC4tVuKYqImKFBJaTvRv5glxpmQ5NygWTSROduuREItEvchO1n57LgVw0VGrc6B81oRTGuUboLCzYuAXg9FpJ-z4NSm35L1WJQrUz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیخ عیسی قاسم: مذهب شیعه در بحرین با تهدیدی وجودی روبه‌روست
🔹
مذهب شیعه در بحرین، به‌همراه علما، خطیبان، نویسندگان، معلمان و مبلغان دینی با تهدیدی شدید و وجودی روبرو است.
🔹
حقوق سیاسی شهروندان شیعه در بحرین و به‌طور کلی حقوق شهروندی آنان، به‌شدت دچار فرسایش شده و روند انکار این حقوق به شکلی گسترده و نگران‌کننده ادامه یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450165" target="_blank">📅 17:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4MJExQnZJAdo_R0E4bQnJPJfso2mZemRAQVf31-qIkuix43ud_WFnsnTwUkBce7Q06o9t9v-syhooYATrNwG5ulldfTOrUxsoQpISw5HdrLZcDSM3OeZXAZrHKxldt5tHcV6f25KSn7uVr3x6ECssDzn-uGZ5fNGxu2lUmxJJNF5zh0y0re5RfHkcu2L3K0yK1TSgxy4GN4hs14ScaPMyQWnnw7xI6JfCytdp3Ge3p56jN2JfgK6tUps658dcMRZpHNB2BxzVHrdZubpAqGGGKAgY0pnE5SazeTf7u1IyMl30DtoRy0O5GN9_Fnak8Mr7yDdk3193JDOStNColaaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مواظب میزان این ماده در بدن‌تان باشید
🔹
منیزیم یکی از مهم‌ترین مواد معدنی بدن است که در بیش‌از ۳۰۰ واکنش حیاتی از جمله تنظیم عملکرد عضلات، کنترل قند خون، فشار خون و ترشح انسولین تاثیر دارد.
🔹
بین ۲۵ تا ۳۸ درصد بیماران دیابتی با کمبود منیزیم مواجه هستند؛ مشکلی که می‌تواند باعث افزایش مقاومت به انسولین، اختلال در کنترل قند خون و افزایش خطر ابتلا یا پیشرفت دیابت نوع ۲ شود.
علائم کمبود منیزیم:
🔸
اضطراب، سردرد و بی‌اشتهایی
🔸
گرفتگی و اسپاسم عضلات
🔸
افزایش فشار خون و نامنظمی ضربان قلب
🔸
اختلال در عملکرد انسولین و متابولیسم قند
مهم‌ترین منابع غذایی غنی از منیزیم:
🔸
اسفناج و سبزیجات برگ‌سبز
🔸
آجیل و دانه‌ها
🔸
حبوبات
🔸
غلات کامل(جو دوسر، برنج قهوه‌ای)
🔹
متخصصان همچنین رژیم مدیترانه‌ای و رژیم DASH را برای حفظ سطح مناسب منیزیم توصیه می‌کنند.
🔹
نیاز روزانه بزرگسالان به منیزیم حدود ۴۰۰ تا ۴۲۰ میلی‌گرم برای مردان و ۳۱۰ تا ۳۲۰ میلی‌گرم برای زنان است.
🔹
در صورت تشخیص کمبود، مصرف ۳۰۰ تا ۵۰۰ میلی‌گرم مکمل منیزیم فقط با نظر پزشک و در دوره‌ای ۹۰ تا ۱۲۰ روزه توصیه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/450164" target="_blank">📅 17:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصوبهٔ جدید مجلس برای تشکیل جلسات در مواقع اضطرار
🔹
نمایندگان مجلس در جلسه علنی شامگاه دوشنبه، طرح اصلاح آیین‌نامه داخلی مجلس را تصویب کردند.
🔹
براساس این مصوبه، در شرایط اضطراری و خاص کشور که به تشخیص هیئت‌رئیسه امکان تشکیل جلسه در ساختمان مجلس وجود نداشته…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450163" target="_blank">📅 17:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450162">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDmUTt5BAW0bI26H45RH21RcnaQX8iPa81hRaeSsAd-v7uPGEixVdNNYXcMfR5WtV9ef3ytor_lvfplQ_jWT4aaQDwLOD2KufCAzpwOH6qyhaHS_u0dJVBMbz3hJHXMVPU3VCt6zWUZhM2dFKzb90pkKsAFUsMj2vcLg7o8GgjbJrpme3KBThpqCAwQNBX0O3VRmYa02UinJk_TLQ2P1yPoKTOQPEzdluk0nGuLJaHMGG1SL1AEpRmILy_o14_BuztAyTIU-_y0jm8rdLjxeC7-GP_JY7eG3Ec1TaqRJ1ocx6bRxN5gWnnHP2964v5LCIStL_ZvZwZgB4R4W9Rckag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فینال جام جهانی کش می‌آید
🔹
فیفا اعلام کرده بین دونیمه فینال جام جهانی به‌جای ۱۵ دقیقه ۳۰ دقیقه خواهد بود. هدف فدراسیون جهانی فوتبال از این کار فرصتی برای اجرای خوانندگان و برنامه‌های سرگرمی است.
🔹
فیفا این ایده را از مسابقات سوپرباول (فینال فوتبال آمریکایی) گرفته. اقدامی که پیش‌تر با انتقاد برخی فوتبالی‌ها روبه‌رو شده بود. آن‌ها عنوان کرده بودند که برای دیدن فینال جام جهانی این مسابقه را دنبال می‌کنند و نه دیدن اجرای گروهی از خوانندگان.
🔹
در فینال جام جهانی باشگاه‌ها نیز که از قضا در همین آمریکا بود رویۀ مشابهی پیش گرفته شده بود اما در جام جهانی تیم‌های ملی این اولین بار خواهد بود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/450162" target="_blank">📅 17:15 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
